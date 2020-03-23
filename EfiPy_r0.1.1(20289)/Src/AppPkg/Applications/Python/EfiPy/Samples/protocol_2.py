#
# protocol_2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# protocol_2.py is free software: you can redistribute it and/or modify
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

TestGuid1 = EfiPy.EFI_GUID( 0x8BE4DF61, 0x93CA, 0x11d2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x81))

#
# Protocol memeber functions
#

def ProtocolFunc1 (Val1, Val2):

  print
  print "   ProtocolFunc1 Val1:", Val1

  if not Val2:
    print "   Get NULL pointer of Val2"
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 3

  return EfiPy.EFI_SUCCESS

def ProtocolFunc2 (Val1, Val2):

  print
  print "   ProtocolFunc2 Val1:", Val1

  if not Val2:
    print "   Get NULL pointer of Val2"
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 5

  return EfiPy.EFI_SUCCESS

#
# Protocl function type
#
PROTOCOL_FUNC1 = EfiPy.CFUNCTYPE (
                   EfiPy.EFI_STATUS,
                   EfiPy.UINTN,
                   EfiPy.POINTER(EfiPy.UINT32)
                   )

PROTOCOL_FUNC2 = EfiPy.CFUNCTYPE (
                   EfiPy.EFI_STATUS,
                   EfiPy.UINTN,
                   EfiPy.POINTER(EfiPy.UINT32)
                   )

#
# Protocol Structure
#

class TEST_PROTOCOL (EfiPy.Structure):
  _fields_ = [("P1Func1", PROTOCOL_FUNC1),
              ("P1Val",   EfiPy.UINT32),
              ("P1Func2", PROTOCOL_FUNC2)
             ]

#
# Building protocol object
#

P1 = PROTOCOL_FUNC1 (ProtocolFunc1)
P2 = PROTOCOL_FUNC2 (ProtocolFunc2)
TestProtocol1 = TEST_PROTOCOL (P1, 3, P2)

#
# Protocl event variable
#

def ProtocolRegisterFunc (Event, Context):
  print "    Protocl Register notification call back."

Event = EfiPy.EFI_EVENT ()
tFunc = EfiPy.EFI_EVENT_NOTIFY(ProtocolRegisterFunc)
gContext = EfiPy.UINTN (1024)

Status = EfiPy.gBS.CreateEvent (
                     EfiPy.EVT_NOTIFY_SIGNAL,
                     EfiPy.TPL_NOTIFY,
                     tFunc,
                     EfiPy.PVOID.from_address (EfiPy.addressof(gContext)),
                     EfiPy.byref (Event)
                     )

print "gBS.CreateEvent(Status:0x%016X)" % Status

#
# RegisterProtocolNotify
#

Registration = EfiPy.PVOID()

Status = EfiPy.gBS.RegisterProtocolNotify (
                     EfiPy.byref (TestGuid1),
                     Event,
                     EfiPy.byref(Registration)
                     )

print "gBS.RegisterProtocolNotify(Status:0x%016X)" % Status

#
# InstallProtocolInterface
#
Handle1 = EfiPy.EFI_HANDLE()

Status = EfiPy.gBS.InstallProtocolInterface (
                     EfiPy.byref (Handle1),
                     EfiPy.byref (TestGuid1),
                     EfiPy.EFI_NATIVE_INTERFACE,
                     EfiPy.byref (TestProtocol1)
                     )

print
print "gBS.InstallProtocolInterface(Status:0x%016X)" % Status

Interface = EfiPy.PVOID ()
Status = EfiPy.gBS.LocateProtocol (
                     EfiPy.byref (TestGuid1),
                     None,
                     EfiPy.byref (Interface)
                     )

print "gBS.LocateProtocol(Status:0x%016X)" % Status

print
IntProt = EfiPy.cast (Interface, EfiPy.POINTER(TEST_PROTOCOL))
Status = IntProt[0].P1Func1 (20, None)
print "IntProt[0].P1Func1 (Status:0x%016X)" % Status

Ret = EfiPy.UINT32 (8)

Status = IntProt[0].P1Func2 (30, EfiPy.byref(Ret))
print "IntProt[0].P1Func2 (Status:0x%016X), Val:%d" % (Status, Ret.value)

print

Status = EfiPy.gBS.UninstallProtocolInterface (
                     Handle1,
                     EfiPy.byref (TestGuid1),
                     Interface
                     )

print "gBS.UninstallProtocolInterface(Status:0x%016X)" % Status

Status = EfiPy.gBS.CloseEvent (Event)
print "gBS.CloseEvent(Status:0x%016X)" % Status

