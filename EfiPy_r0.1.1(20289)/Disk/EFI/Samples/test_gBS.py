#!/usr/bin/python

#
# test_gBS.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# test_gBS.py is free software: you can redistribute it and/or modify
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

from EfiPy    import *

#
# EFI_BOOT_SERVICES header
#

print "************************************************"
print "* EFI_BOOT_SERVICES testing...                 *"
print "************************************************"
print
print " Address of gBS:         0x%016X" % addressof (gBS)
print " gBS.Hdr.Signature:   (*)0x%016X" % gBS.Hdr.Signature
print " gBS.Hdr.Revision:       0x%016X" % gBS.Hdr.Revision
print " gBS.Hdr.HeaderSize:     0x%016X (0x%016X)" % (gBS.Hdr.HeaderSize, sizeof (gBS))
print " gBS.Hdr.CRC32:          0x%016X" % gBS.Hdr.CRC32

#
# gBS functions for stall, PTL functions
#

print
print "================================================"
print "gBS Task function..."
print

TimeCur = EFI_TIME ()
TimeCap = EFI_TIME_CAPABILITIES ()

OriginalTpl = gBS.RaiseTPL (TPL_HIGH_LEVEL)
print " gBS.RaiseTPL (OriginalTpl = %d)" % OriginalTpl

Status  = gRT.GetTime (byref(TimeCur), byref(TimeCap))
print "   Time: %02d:%02d:%02d:%08X" % (
  TimeCur.Hour,
  TimeCur.Minute,
  TimeCur.Second,
  TimeCur.Nanosecond
  )

Status  = gBS.Stall (1 * 1000 * 1000)
print "     gBS.Stall 1 second(Status:0x%016X)" % Status

Status  = gRT.GetTime (byref(TimeCur), byref(TimeCap))
print "   Time: %02d:%02d:%02d:%08X" % (TimeCur.Hour, TimeCur.Minute, TimeCur.Second, TimeCur.Nanosecond)

gBS.RestoreTPL (OriginalTpl)
print " gBS.RestoreTPL... Done"

#
# gBS functions (new) task controller
#

print
print " gBS.LoadImage         SKIP ***********"
print " gBS.StartImage        SKIP ***********"
print " gBS.UnloadImage       SKIP ***********"
print " gBS.ExitBootServices  SKIP ***********"

Status = gBS.Exit (pImageHandle, EFI_SUCCESS, UINTN(0), None)
print " gBS.Exit(Status:0x%016X)" % Status

#
# gBS memory functions
#

print
print "================================================"
print "gBS memory function..."
print
PageAddr = EFI_PHYSICAL_ADDRESS (0xFFFFFFFFFFFFFFFFL)
Status = gBS.AllocatePages (AllocateAddress, EfiRuntimeServicesData, 1, byref (PageAddr))
print " gBS.AllocatePages with fixed address 0x%0X16, (Status:0x%016X)" % (PageAddr.value, Status)

PageAddr = EFI_PHYSICAL_ADDRESS (0)
Status = gBS.AllocatePages (AllocateAnyPages, EfiRuntimeServicesData, 1, byref (PageAddr))
print " gBS.AllocatePages(Status:0x%016X)" % Status
if Status == EFI_SUCCESS:
  print " PageAddr: 0x%016X" % PageAddr.value
  Status = gBS.FreePages (PageAddr, 1)
  print " gBS.FreePages(Status:0x%016X)" % Status
else:
  print " gBS.FreePages SKIP"

print
Blen = 3
Mem1 = PVOID ()
Mem2 = PVOID ()

Status = gBS.AllocatePool (EfiRuntimeServicesData, Blen, byref (Mem1))
print " Mem1: gBS.AllocatePool(Status:0x%016X, Address: 0x%016X)" % (Status, Mem1.value)
str1 = cast (Mem1, POINTER (CHAR8 * Blen))
print "   addressof (str1.contents): 0x%016X" % addressof (str1.contents)
print "   str1.contents:", repr (str1.contents.raw)
Status = gBS.AllocatePool (EfiRuntimeServicesData, Blen, byref (Mem2))
print " Mem2: gBS.AllocatePool(Status:0x%016X, Address: 0x%016X)" % (Status, Mem2.value)

str2 = cast (Mem2, POINTER (CHAR8 * Blen))
print "   str2.contents:", repr (str2.contents.raw)

print

gBS.SetMem (Mem1, Blen, 0x01)
print " gBS.SetMem for Mem1 buffer:", repr (str1.contents.raw)
gBS.CopyMem (Mem2, Mem1, Blen)
print " gBS.CopyMem, copy from Mem1 to Mem 2:", repr (str2.contents.raw)

print

Status = gBS.FreePool (Mem1)
print " gBS.FreePool(Mem1, Status:0x%016X)" % Status
Status = gBS.FreePool (Mem2)
print " gBS.FreePool(Mem2, Status:0x%016X)" % Status
print

MemoryMapSize     = UINTN(0)
MemoryMap         = PVOID()
MapKey            = UINTN()
DescriptorSize    = UINTN()
DescriptorVersion = UINT32()

Status = gBS.GetMemoryMap (
               byref (MemoryMapSize),
               None,
               byref (MapKey),
               byref (DescriptorSize),
               byref (DescriptorVersion)
               )

print " gBS.GetMemoryMap(Status:0x%016X) MemoryMapSize = %d, DescriptorSize = %d, Structure size = %d" % (
        Status,
        MemoryMapSize.value,
        DescriptorSize.value,
        sizeof (EFI_MEMORY_DESCRIPTOR)
        )

print "   MapKey = 0x%016X, DescriptorSize = 0x%016X, DescriptorVersion = 0x%016X" % (
        MapKey.value,
        DescriptorSize.value,
        DescriptorVersion.value
        )

print

# print "================================================"
# print "Memory UNIT TESTING ..."
# print
# _EfiPyAllocatePool = EFI_ALLOCATE_POOL (EfiPyAllocatePool)
# _EfiPyFreePool     = EFI_FREE_POOL (EfiPyFreePool)
# 
# Blen = 3
# Mem1 = PVOID ()
# Mem2 = PVOID ()
# 
# Status = _EfiPyAllocatePool (EfiRuntimeServicesData, Blen, byref (Mem1))
# print " _EfiPyAllocatePool(Status:0x%016X, Address: 0x%016X)" % (Status, Mem1.value)
# 
# str1 = cast (Mem1, POINTER (CHAR8 * Blen))
# print "   Mem1:", repr (str1.contents.raw)
# str1.contents.value="12"
# print "   Mem1:", repr (str1.contents.raw)
# print "   addressof (str1.contents) : 0x%016X" % addressof (str1.contents)
# 
# Status = _EfiPyFreePool (Mem1)
# print " _EfiPyFreePool(Status:0x%016X)" % Status
# print

#
# gBS Event functions
#

print "================================================"
print "gBS event function..."
print

#
# Timer call-back function
#

def TimerFunction (Event, Context):
  print "    Enter TimerFunction"

  if Context == None:
    print "      No context input"
  else:
    print "      type(Context):", type(Context), Context

Event = EFI_EVENT ()
tFunc = EFI_EVENT_NOTIFY(TimerFunction)
gContext = UINTN (1024)

#
# It doesn't work
#
# Status = gBS.CreateEvent (
#                EVT_TIMER | EVT_NOTIFY_SIGNAL,
#                TPL_NOTIFY,
#                EFI_EVENT_NOTIFY(TimerFunction), # root cause
#                None,
#                byref (Event)
#                )
#
# It provides NULL context sample
#
# Status = gBS.CreateEvent (
#                EVT_TIMER | EVT_NOTIFY_SIGNAL,
#                TPL_NOTIFY,
#                tFunc,
#                None,
#                byref (Event)
#                )
#

Status = gBS.CreateEvent (
               EVT_TIMER | EVT_NOTIFY_SIGNAL,
               TPL_NOTIFY,
               tFunc,
               PVOID.from_address (addressof(gContext)),
               byref (Event)
               )

print " gBS.CreateEvent(Status:0x%016X)" % Status

Status = gBS.SetTimer (Event, TimerPeriodic, 3000000)
print " gBS.SetTimer(Status:0x%016X)" % Status

Status = gBS.Stall (1 * 1000 * 1000)

Status = gBS.SetTimer (Event, TimerCancel, 0)
print " gBS.SetTimer Cancel(Status:0x%016X)" % Status
Status = gBS.CloseEvent (Event)
print " gBS.CloseEvent(Status:0x%016X)" % Status

Index = UINTN()

print "   Press Any key to continue..."
Status = gBS.WaitForEvent (1, byref(EFI_EVENT(gST.ConIn[0].WaitForKey)), byref(Index))

print "   gBS.WaitForEvent(Status:0x%016X)" % Status
print "   gBS.WaitForEvent, Index: 0x%016X" % Index.value
print "   gBS.WaitForEvent, Key:   0x%016X" % gST.ConIn[0].WaitForKey

#
# Input key initialize
#

from EfiPy.MdePkg.Protocol.SimpleTextIn import EFI_INPUT_KEY
InputKey = EFI_INPUT_KEY ()

Status = gST.ConIn[0].ReadKeyStroke (gST.ConIn, byref (InputKey))
print "   gST.ConIn[0].ReadKeyStroke(Status:0x%016X)" % Status

if InputKey.ScanCode != 0:
  print "   ScanCode:     0x%04X" % InputKey.ScanCode
else:
  print "   UnicodeChar:  \"%c\"" % InputKey.UnicodeChar

#
# Event group testing
#

TestGuid  = EFI_GUID( 0x8BE4DF61, 0x93CA, 0x11d2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x81))
Event1    = EFI_EVENT ()
Event2    = EFI_EVENT ()

def EventTestGuidFunc1 (Event, Context):
  print "    Enter TimerFunction ==> 1"

tFunc1 = EFI_EVENT_NOTIFY(EventTestGuidFunc1)

def EventTestGuidFunc2 (Event, Context):
  print "    Enter TimerFunction ==> 2"

tFunc2 = EFI_EVENT_NOTIFY(EventTestGuidFunc2)

Status = gBS.CreateEventEx (
               EVT_NOTIFY_WAIT,
               TPL_NOTIFY,
               tFunc1,
               None,
               byref (TestGuid),
               Event1
               )

print " gBS.CreateEventEx(Status:0x%016X)" % Status

Status = gBS.CreateEventEx (
               EVT_NOTIFY_WAIT,
               TPL_NOTIFY,
               tFunc2,
               None,
               byref (TestGuid),
               Event2
               )

print " gBS.CreateEventEx(Status:0x%016X)" % Status

Status = gBS.CheckEvent (Event2)
print " gBS.CheckEvent(Status:0x%016X)" % Status
Status = gBS.SignalEvent (Event1)
print " gBS.SignalEvent(Status:0x%016X)" % Status
Status = gBS.CheckEvent (Event1)
print " gBS.CheckEvent(Status:0x%016X)" % Status
Status = gBS.CloseEvent (Event1)
print " gBS.CloseEvent(Status:0x%016X)" % Status
Status = gBS.CloseEvent (Event2)
print " gBS.CloseEvent(Status:0x%016X)" % Status
print
print "gBS gBS protocol/hanlde function... Please check test_protocol.py"

#
# Other gBS functions
#

print
print "================================================"
print "gBS misc function..."
print

print " gBS.Reserved  Note function ***********"
Status = gBS.SetWatchdogTimer (5 * 60, 0x0000, 0x00, None);
print " gBS.SetWatchdogTimer(Status:0x%016X)" % Status
Status = gBS.SetWatchdogTimer (0, 0x10000, 0, None);
print " gBS.SetWatchdogTimer(Status:0x%016X)" % Status
print

Count = UINT64 ()
Status = gBS.GetNextMonotonicCount (byref(Count))
print " gBS.GetNextMonotonicCount(Status:0x%016X): Count: 0x%016X" % (Status, Count.value)

Crc32 = UINT32 ()
gBS.Hdr.CRC32 = 0
Status = gBS.CalculateCrc32 (addressof (gBS), gBS.Hdr.HeaderSize, byref(Crc32))
print " gBS.CalculateCrc32(Status:0x%016X): Crc32: 0x%016X" % (Status, Crc32.value)
gBS.Hdr.CRC32 = Crc32.value
print
