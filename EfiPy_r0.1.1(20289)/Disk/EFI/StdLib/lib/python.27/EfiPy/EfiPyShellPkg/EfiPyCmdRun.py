#!/usr/bin/python

#
# EfiPyCmdRun.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdRun.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy

from EfiPy.EfiPyShellPkg import EfiPyCmdBase
from EfiPy.EfiPyShellPkg import EfiPyCmdFileOp

from EfiPy.EfiPyShellPkg.Utility import EfiPyFileOp
from EfiPy.MdePkg.Protocol.SimpleFileSystem import    \
         EFI_FILE_MODE_READ,                            \
         EFI_FILE_PROTOCOL,                             \
         EFI_FILE_DIRECTORY,                            \
         EFI_FILE_ARCHIVE,                            \
         EFI_FILE_SYSTEM,                            \
         EFI_FILE_HIDDEN,                            \
         EFI_FILE_READ_ONLY

from EfiPy.MdePkg.Protocol.DevicePathFromText import  \
        EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL, \
        gEfiDevicePathFromTextProtocolGuid

from EfiPy.EfiPyShellPkg.EfiPyCmdMap import             \
                   WsIdxVol,        \
                   WsIdxAlias,      \
                   WsIdxHandle,     \
                   WsIdxDevPath,    \
                   WsIdxFont,       \
                   WsIdxBackGround, \
                   WsIdxPath

from    EfiPy.MdePkg.Guid.FileInfo  import EFI_FILE_INFO, gEfiFileInfoGuid

#
# EfiPy Command utility FS Mapping utility class
#

class EFIPY_CMD_RUN (EfiPyCmdFileOp.EFIPY_CMD_FILE_OP):
  '''[INIT] Run external EFI application.'''

  name     = u"run"
  Paras    = {}

  def __init__ (self, Shell):

    self.Shell   = Shell
    self.args    = []

    self.StdIn  = Shell.StdIn
    self.StdOut = Shell.StdOut
    self.StdErr = Shell.StdErr

  def ParaBuild(self, args):
    self.args = args

  def PostRun (self):
    pass

  def InternalExec (self, pFullPathDev, FullPath):

    NewHandle = EfiPy.EFI_HANDLE ()
    Status = EfiPy.gBS.LoadImage(
      0,
      EfiPy.gImageHandle,
      pFullPathDev,
      None,
      0,
      EfiPy.byref (NewHandle))

    if EfiPy.EFI_ERROR (Status):
      Status = EfiPy.gBS.UnloadImage(NewHandle)
      return Status, -1

    # print "EfiPy.gBS.LoadImage : %x" % Status

    from EfiPy.MdePkg.Protocol.LoadedImage import     \
                          EFI_LOADED_IMAGE_PROTOCOL,  \
                          gEfiLoadedImageProtocolGuid

    Interface   = EfiPy.PVOID ()

    Status = EfiPy.gBS.OpenProtocol(
      NewHandle,
      EfiPy.byref (gEfiLoadedImageProtocolGuid),
      EfiPy.byref (Interface),
      EfiPy.gImageHandle,
      None,
      EfiPy.EFI_OPEN_PROTOCOL_GET_PROTOCOL)

    if EfiPy.EFI_ERROR (Status):
      Status = EfiPy.gBS.UnloadImage(NewHandle)
      return Status, -1

    LoadedImage = EfiPy.cast (Interface, EfiPy.POINTER (EFI_LOADED_IMAGE_PROTOCOL))

    # print "EfiPy.gBS.OpenProtocol : %x" % Status
    # print "LoadedImage[0].LoadOptionsSize", LoadedImage[0].LoadOptionsSize

    from EfiPy.ShellPkg.Protocol import EfiShellParameters as sPara

    ShellParamsProtocol = sPara.EFI_SHELL_PARAMETERS_PROTOCOL ()

    ShellParamsProtocol.Argc    = len (self.args)
    ShellParamsProtocol.Argv    = (EfiPy.PCHAR16 * ShellParamsProtocol.Argc) ()
    ShellParamsProtocol.StdIn   = EfiPy.gST.ConsoleInHandle
    ShellParamsProtocol.StdOut  = EfiPy.gST.ConsoleOutHandle
    ShellParamsProtocol.StdErr  = EfiPy.gST.StandardErrorHandle


    CmdLine = u""
    CmdCnt = 0
    for Cmd in self.args:
      CmdLine += Cmd + u" "
      ShellParamsProtocol.Argv[CmdCnt] = EfiPy.PCHAR16 (Cmd)
      CmdCnt  += 1

    ShellParamsProtocol.Argv[0] = EfiPy.PCHAR16 (FullPath)

    NewCmdLine = EfiPy.PCHAR16 (CmdLine)
    # print "NewCmdLine", NewCmdLine.value
    # print "size", len (NewCmdLine.value) * 2

    LoadedImage[0].LoadOptions      = EfiPy.cast (NewCmdLine, EfiPy.PVOID)
    LoadedImage[0].LoadOptionsSize  = EfiPy.UINT32 (len (NewCmdLine.value) * 2)

    Status = EfiPy.gBS.InstallProtocolInterface(
      NewHandle,
      sPara.gEfiShellParametersProtocolGuid,
      EfiPy.EFI_NATIVE_INTERFACE,
      EfiPy.byref (ShellParamsProtocol)
      )

    if EfiPy.EFI_ERROR (Status):
      Status = EfiPy.gBS.UnloadImage(NewHandle)
      return Status, -1

    # print "EfiPy.gBS.InstallProtocolInterface : %x" % Status

    StartStatus = EfiPy.gBS.StartImage(
      NewHandle,
      None,
      None)

    # print "EfiPy.gBS.StartImage : %x" % StartStatus

    Status = EfiPy.gBS.UninstallProtocolInterface(
               NewHandle,
               EfiPy.byref (sPara.gEfiShellParametersProtocolGuid),
               EfiPy.byref (ShellParamsProtocol)
               )

    # print "EfiPy.gBS.UninstallProtocolInterface : %x" % Status

    return Status, StartStatus

  def Run (self):

    # if len (self.args) == 1:
    #   self.StdOut.printf("Invalide parameter %s\r\n" % str(self.args))
    #   return 0

    FilePath    = self.args[0]
    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    FileFolder  = self.Shell.WorkSpace[WsIdxPath]

    FileSpace, TempFolder, SpaceOnly, SpaceFound = self.ParseFolder (FilePath)
    # print "===>", FileSpace, TempFolder, SpaceOnly, SpaceFound

    Fs1, FilePath1 = EfiPyFileOp.GetRootFsOperation (self.Shell.WS, u"%s%s" %(FileSpace, TempFolder))

    if Fs1 == None:
      self.StdOut.printf(u"File %s cannot be opened\r\n" % self.args[0])
      return 0

    Handle1 = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()
    Status = Fs1.Open (
               EfiPy.byref (Fs1),
               EfiPy.byref (Handle1),
               FilePath1,
               EFI_FILE_MODE_READ,
               0
               )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf(u"File %s cannot be opened\r\n" % self.args[0])
      return 0

    Fs1.Close (EfiPy.byref (Fs1))

    BufferSize = EfiPy.UINTN (0)
    Status = Handle1[0].GetInfo (
                              Handle1,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              None
                              )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      Handle1[0].Close()
      return 0

    TmpBuffer = bytearray (BufferSize.value)
    fInfo1    = EFI_FILE_INFO.from_buffer (TmpBuffer)
    Status = Handle1[0].GetInfo (
                              Handle1,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              EfiPy.byref (fInfo1)
                              )

    if Status != EfiPy.EFI_SUCCESS:
      Handle1[0].Close(Handle1)
      return 0

    if fInfo1.Attribute & EFI_FILE_ARCHIVE != EFI_FILE_ARCHIVE:
      self.StdOut.printf(u"Cannot run file %s%s\r\n" %(FileSpace, TempFolder))
      Handle1[0].Close(Handle1)
      return 0

    Handle1[0].Close (Handle1)

    if not TempFolder.upper().endswith (".EFI"):
      self.StdOut.printf(u"Cannot run file %s%s\r\n" %(FileSpace, TempFolder))
      return 0

    # print "Prepare to run %s%s\r\n" %(FileSpace, TempFolder)
    # print type(self.Shell.WS[FileSpace.upper()][WsIdxDevPath])
    Folder = self.Shell.WS[FileSpace.upper()][WsIdxDevPath]

    RawData = EfiPy.cast (EfiPy.pointer(Folder), EfiPy.POINTER(EfiPy.CHAR8 * (16 * 10)))

    Folder.DisplayOnly    = False
    Folder.AllowShortcuts = False
    FullPath = "%s/%s" % (Folder, TempFolder)
    # print FullPath

    Interface = EfiPy.PVOID ()
    Status = EfiPy.gBS.LocateProtocol (EfiPy.byref (gEfiDevicePathFromTextProtocolGuid), None, EfiPy.byref (Interface))
    if EfiPy.EFI_ERROR (Status):
      return 0

    Text2Dev = EfiPy.cast (Interface, EfiPy.POINTER(EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL))
    pFullPathDev = Text2Dev[0].ConvertTextToDevicePath (FullPath)

    # print "%s" % pFullPathDev[0], EfiPy.sizeof (pFullPathDev[0])

    self.InternalExec (pFullPathDev, FullPath)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_RUN.name + ""
  Args    = Para.split()

  class CMD_SET:
    def __init__ (self):

      from EfiPy.EfiPyShellPkg import EfiPyShellIo
      import EfiPy

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.StdOut.ConOutModeDefault()

      self.CmdSet     = {}
      self.WS         = {}
      self.WorkFolder = u"EFI"
      self.WorkSpace  = None

  CmdSet  = CMD_SET ()

  #
  # Establish Volume Map database
  #

  from EfiPy.EfiPyShellPkg.EfiPyCmdMap  import EFIPY_CMD_MAP
  EfiPyCmdMap = EFIPY_CMD_MAP (CmdSet)
  ret = EfiPyCmdMap.Run()

  # for WorkSpace in EfiPyCmdMap.WS:
  #   print WorkSpace, ":", EfiPyCmdMap.WS[WorkSpace]

  CmdSet.WorkSpace = EfiPyCmdMap.WS[u"FS0:"]

  EfiPyCmdObj = EFIPY_CMD_RUN (CmdSet)

  print

  Para    = "EFI\Tools\__init__.py"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = "EFI\Tools\Hello.efi 1 2"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = "EFI\Tools\main.efi 1 2"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = "fs1:"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
