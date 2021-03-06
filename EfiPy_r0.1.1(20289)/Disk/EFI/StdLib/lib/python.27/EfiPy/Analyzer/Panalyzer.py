#
# Panalyzer.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Panalyzer.py is free software: you can redistribute it and/or modify
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

from EfiPy.ShellPkg.Protocol.EfiShell import *
from EfiPy.MdePkg.Protocol.LoadedImage import     \
                      EFI_LOADED_IMAGE_PROTOCOL,  \
                      gEfiLoadedImageProtocolGuid

from EfiPy.MdePkg.Protocol.LoadedImage import     \
                      EFI_LOADED_IMAGE_PROTOCOL,  \
                      gEfiLoadedImageProtocolGuid

from BaseAnalyze import BaseAnalyze as _bAnalyze
from EfiPy.ShellPkg.Protocol import EfiShellParameters as sPara
from BaseAnalyze import dOutClass

class pAnalyzer (_bAnalyze):

  def __init__ (self, dOut):

    _bAnalyze.__init__(self, dOut)
    self.Guid         = None            # pAnalyzer

    AppList = []
    DrvList = []

    self.ProtocolFuncList = (("InstallProtocolInterface",           None),
                             ("ReinstallProtocolInterface",         None),
                             ("UninstallProtocolInterface",         None),
                             # ("LocateHandleBuffer",                 None),
                             # ("HandleProtocol",                     None),
                             # ("OpenProtocol",                       None),
                             # ("CloseProtocol",                      None),
                             # ("ProtocolsPerHandle",                 None),
                             # ("LocateProtocol",                     None),
                             # ("InstallMultipleProtocolInterfaces",  None),
                             # ("UninstallMultipleProtocolInterfaces",None),
                            )

    self._ProtocolFilter = _bAnalyze(dOut)
    self._ProtocolFilter.Build_Capability (EfiPy.EFI_BOOT_SERVICES)
    self._ProtocolFilter.Filter.append (self._ProtocolFilter.Build_Filter (EfiPy.byref(EfiPy.gBS), None))

    for ProtoclFun in self.ProtocolFuncList:
      self._ProtocolFilter.install(ProtoclFun[0])


    self._ProtocolAllStart ()

  def _ProtocolAllStart (self):
    for ProtoclFun in self.ProtocolFuncList:
      self._ProtocolFilter.start(ProtoclFun[0])

  def _ProtocolAllStop (self):

    for ProtoclFun in self.ProtocolFuncList:
      self._ProtocolFilter.stop(ProtoclFun[0])

  def uninstall (self, FuncName):
    _bAnalyze.uninstall (self, FuncName)

  def __del__(self):
    _bAnalyze.__del__ (self)
    self._ProtocolFilter.__del__()

  def DriverLoad (self, pFullPathDev):

    NewHandle = EfiPy.EFI_HANDLE ()

    Status = EfiPy.gBS.LoadImage(
      0,
      EfiPy.gImageHandle,
      pFullPathDev,
      None,
      0,
      EfiPy.byref (NewHandle))

    if EfiPy.EFI_ERROR (Status):
      return Status, -1

    TmpImage = EfiPy.PVOID ()

    Status = EfiPy.gBS.HandleProtocol (
                         NewHandle,
                         EfiPy.byref (gEfiLoadedImageProtocolGuid),
                         EfiPy.byref (TmpImage)
                         )

    if EfiPy.EFI_ERROR (Status):

      EfiPy.gBS.Exit (
                 EfiPy.byref (TmpImage),
                 EfiPy.EFI_INVALID_PARAMETER,
                 0,
                 None
                 )

      return EfiPy.EFI_INVALID_PARAMETER, -2

    LoadedDriverImage = EfiPy.cast (TmpImage, EfiPy.POINTER (EFI_LOADED_IMAGE_PROTOCOL))

    if (LoadedDriverImage[0].ImageCodeType != EfiBootServicesCode) and \
       (LoadedDriverImage[0].ImageCodeType != EfiRuntimeServicesCode):

      return EfiPy.EFI_INVALID_PARAMETER, LoadedDriverImage[0].ImageCodeType

    self._ProtocolAllStart ()

    StartStatus = EfiPy.gBS.StartImage(
      NewHandle,
      None,
      None)

    self._ProtocolAllStop ()

    return Status, StartStatus

  def ApplicationExec (self, pFullPathDev, FullPath):

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

    ShellParamsProtocol = sPara.EFI_SHELL_PARAMETERS_PROTOCOL ()

    # ShellParamsProtocol.Argc    = len (self.args)
    ShellParamsProtocol.Argc    = 0
    # ShellParamsProtocol.Argv    = (EfiPy.PCHAR16 * ShellParamsProtocol.Argc) ()
    ShellParamsProtocol.Argv    = None
    ShellParamsProtocol.StdIn   = EfiPy.gST.ConsoleInHandle
    ShellParamsProtocol.StdOut  = EfiPy.gST.ConsoleOutHandle
    ShellParamsProtocol.StdErr  = EfiPy.gST.StandardErrorHandle


    # CmdLine = u""
    # CmdCnt = 0
    # for Cmd in self.args:
    #   CmdLine += Cmd + u" "
    #   ShellParamsProtocol.Argv[CmdCnt] = EfiPy.PCHAR16 (Cmd)
    #   CmdCnt  += 1
    # 
    # ShellParamsProtocol.Argv[0] = EfiPy.PCHAR16 (FullPath)

    # NewCmdLine = EfiPy.PCHAR16 (CmdLine)
    # print "NewCmdLine", NewCmdLine.value
    # print "size", len (NewCmdLine.value) * 2

    # LoadedImage[0].LoadOptions      = EfiPy.cast (NewCmdLine, EfiPy.PVOID)
    LoadedImage[0].LoadOptions        = None
    # LoadedImage[0].LoadOptionsSize  = EfiPy.UINT32 (len (NewCmdLine.value) * 2)
    LoadedImage[0].LoadOptionsSize    = 0

    # self._ProtocolFilter.stop("InstallProtocolInterface")
    Status = EfiPy.gBS.InstallProtocolInterface(
      NewHandle,
      sPara.gEfiShellParametersProtocolGuid,
      EfiPy.EFI_NATIVE_INTERFACE,
      EfiPy.byref (ShellParamsProtocol)
      )
    # self._ProtocolFilter.start("InstallProtocolInterface")

    if EfiPy.EFI_ERROR (Status):

      # self._ProtocolFilter.stop("OpenProtocol")
      # self._ProtocolFilter.stop("HandleProtocol")

      Status = EfiPy.gBS.UnloadImage(NewHandle)

      # self._ProtocolFilter.start("OpenProtocol")
      # self._ProtocolFilter.start("HandleProtocol")

      return Status, -1

    self._ProtocolAllStart ()

    StartStatus = EfiPy.gBS.StartImage(
      NewHandle,
      None,
      None)

    self._ProtocolAllStop ()

    # self._ProtocolFilter.stop("UninstallProtocolInterface")
    Status = EfiPy.gBS.UninstallProtocolInterface(
               NewHandle,
               EfiPy.byref (sPara.gEfiShellParametersProtocolGuid),
               EfiPy.byref (ShellParamsProtocol)
               )
    # self._ProtocolFilter.start("UninstallProtocolInterface")

    return Status, StartStatus

  def LoadEfiFiles (self, DrvList, AppList):

    Interface = EfiPy.PVOID ()
    # self._ProtocolFilter.stop("LocateProtocol")
    Status = EfiPy.gBS.LocateProtocol (
               EfiPy.byref (gEfiShellProtocolGuid),
               None,
               EfiPy.byref (Interface)
               )
    # self._ProtocolFilter.start("LocateProtocol")

    ShellProtocl = None

    if Status == EFI_ERROR:
      self.dOut.msg += '<ERROR>"Locate protocol gEfiShellProtocolGuid"</ERROR>\n'
      return
    else:
      ShellProtocl = EfiPy.cast (Interface, EfiPy.POINTER(EFI_SHELL_PROTOCOL))[0]

    self._ProtocolAllStop ()

    for DrvName in DrvList:

      self.dOut.msg += '<Driver Name ="%s">\n' % DrvName

      # self._ProtocolFilter.stop("HandleProtocol")
      DrvPath = ShellProtocl.GetDevicePathFromFilePath(DrvName);
      # self._ProtocolFilter.start("HandleProtocol")

      if DrvPath == None:

        self.dOut.msg += "Load Driver Error...\n"

      else:

        Status, DrvStatus = self.DriverLoad (DrvPath)

        if Status != EfiPy.EFI_SUCCESS:

          self.dOut.msg += "Load Driver Error... %X\n" % Status

      self.dOut.msg += '<return Func="%X" Driver="%X">\n</return>\n</Driver>\n' % (Status, DrvStatus)

    for AppName in AppList:

      self.dOut.msg += '<Application Name ="%s">\n' % AppName

      # self._ProtocolFilter.stop("HandleProtocol")
      AppPath = ShellProtocl.GetDevicePathFromFilePath(AppName);
      self._ProtocolFilter.start("HandleProtocol")

      if AppPath == None:

        self.dOut.msg += "Load Application Error...\n"

      else:

        Status, AppStatus = self.ApplicationExec (AppPath, AppName)

        if Status != EfiPy.EFI_SUCCESS:
          self.dOut.msg += "Load Application Error... %X\n" % Status
        else:
          self.dOut.msg += '<Return Value="%X"></Return>\n' % AppStatus

      self.dOut.msg += '</Application>\n'

    self._ProtocolAllStart ()

  def Detect_Protocol (self, Guid, Protocol):

    TmpCount  = EfiPy.UINTN (0)
    TmpBuff   = EfiPy.POINTER (EfiPy.EFI_HANDLE) ()

    self._ProtocolFilter.stop("LocateHandleBuffer")
    Status = EfiPy.gBS.LocateHandleBuffer (
                  EfiPy.ByProtocol,
                  EfiPy.byref (Guid),
                  None,
                  EfiPy.byref (TmpCount),
                  EfiPy.byref (TmpBuff)
                 )
    self._ProtocolFilter.start("LocateHandleBuffer")

    if Status != EfiPy.EFI_SUCCESS:
      return 

    self._ProtocolFilter.stop("HandleProtocol")

    for Index in range (TmpCount.value):

      Target = EfiPy.PVOID ()
      Status = EfiPy.gBS.HandleProtocol (
                     TmpBuff[Index],
                     EfiPy.byref (Guid),
                     EfiPy.byref (Target)
                    )

      if Status != EfiPy.EFI_SUCCESS:
        continue

      self.Target.append ((Target, TmpBuff[Index]))

    self._ProtocolFilter.start("HandleProtocol")
