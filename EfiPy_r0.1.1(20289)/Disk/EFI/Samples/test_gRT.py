#!/usr/bin/python

#
# test_gRT.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# test_gRT.py is free software: you can redistribute it and/or modify
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
# Generic function address testing
#

print "************************************************"
print "EFIPY testing..."
print "************************************************"

print "gRT: 0x%016X (size:0x%08X)" % (addressof(gRT), sizeof (gRT))
print "gST: 0x%016X (size:0x%08X)" % (addressof(gST), sizeof (gST))
print "gBS: 0x%016X (size:0x%08X)" % (addressof(gBS), sizeof (gBS))

print "gRT.GetVariable::%x" % addressof (gRT.GetVariable)
print "gRT.GetTime::%x" % addressof (gRT.GetTime)
print

#
# EFI_RUNTIME_SERVICES header
#

print "************************************************"
print "EFI_RUNTIME_SERVICES testing..."
print "************************************************"
print
print " gRT :"
print " gRT.Hdr.Signature: (*)0x%016X" % gRT.Hdr.Signature
print " gRT.Hdr.Revision:     0x%016X" % gRT.Hdr.Revision
print " gRT.Hdr.HeaderSize:   0x%016X (0x%016X)" % (gRT.Hdr.HeaderSize, sizeof (gRT))
print " gRT.Hdr.CRC32:        0x%016X" % gRT.Hdr.CRC32
print

#
# gRT functions for Date Time functions
#

print
print "================================================"
print "gRT Date/Time function..."
print

TimeCur = EFI_TIME ()
TimeCap = EFI_TIME_CAPABILITIES ()

Status  = gRT.GetTime (byref(TimeCur), byref(TimeCap))
print " gRT.GetTime(Status:0x%016X)" % Status
print
print "   Date: %4d/%02d/%02d"  % (TimeCur.Year, TimeCur.Month,  TimeCur.Day)
print "   Time: %02d:%02d:%02d" % (TimeCur.Hour, TimeCur.Minute, TimeCur.Second)
print
print "   TimeCap.Resolution: %08X" % TimeCap.Resolution
print "   TimeCap.Accuracy:   %d"   % TimeCap.Accuracy
print "   TimeCap.SetsToZero: %08X" % TimeCap.SetsToZero
print

TimeCur.Year = 2014
TimeCur.Hour = 3

Status  = gRT.SetTime (byref(TimeCur))
print " gRT.SetTime(Status:0x%016X)" % Status
print
Status  = gRT.GetTime (byref(TimeCur), None)
print " gRT.GetTime(Status:0x%016X)" % Status
print
print "   Date: %4d/%02d/%02d"  % (TimeCur.Year, TimeCur.Month,  TimeCur.Day)
print "   Time: %02d:%02d:%02d" % (TimeCur.Hour, TimeCur.Minute, TimeCur.Second)
print

Status = gRT.SetWakeupTime (BOOLEAN (1), byref(TimeCur))
print " gRT.SetWakeupTime(Status:0x%016X)" % Status
print

Enabled = BOOLEAN (0)
Pending = BOOLEAN ()

Status = gRT.GetWakeupTime (byref(Enabled), byref(Pending), byref(TimeCur))
print " gRT.GetWakeupTime(Status:0x%016X)" % Status
print
print "   Enabled:", Enabled.value
print "   Pending:", Pending.value
print "   Date: %04d/%02d/%02d" % (TimeCur.Year, TimeCur.Month, TimeCur.Day)
print "   Time: %02d:%02d:%02d" % (TimeCur.Hour, TimeCur.Minute, TimeCur.Second)
print

#
# gRT ignore for testing function
#

print
print "================================================"
print "gRT ignore for testing function..."
print
print " gRT.SetVirtualAddressMap:     SKIP ***********"
print " gRT.ConvertPointer:           SKIP ***********"
print " gRT.UpdateCapsule:            SKIP ***********"
print " gRT.QueryCapsuleCapabilities: SKIP ***********"

print
print "================================================"
print "gRT GetNextHighMonotonicCount function..."
print

HighCount = UINT32 ()
Status = gRT.GetNextHighMonotonicCount (byref(HighCount))
print " gRT.GetNextHighMonotonicCount(Status:0x%016X), HighCount: 0x%08X" % (Status, HighCount.value)
print

# 
# print "ResetSystem ..."
# gRT.ResetSystem (EfiResetCold, EFI_SUCCESS, 0, None)
#

print
print "================================================"
print "gRT variable function..."
print

Attributes    = UINT32 (
                  EFI_VARIABLE_BOOTSERVICE_ACCESS |
                  EFI_VARIABLE_NON_VOLATILE       |
                  EFI_VARIABLE_RUNTIME_ACCESS
                  )

MaximumVariableStorageSize    = UINT64 ()
RemainingVariableStorageSize  = UINT64 ()
MaximumVariableSize           = UINT64 ()

Status = gRT.QueryVariableInfo(
               Attributes,
               byref (MaximumVariableStorageSize),
               byref (RemainingVariableStorageSize),
               byref (MaximumVariableSize),
               )

print " gRT.QueryVariableInfo(Status:0x%016X)"  % Status
print "     MaximumVariableStorageSize:   %d"   % MaximumVariableStorageSize.value
print "     RemainingVariableStorageSize: %d"   % RemainingVariableStorageSize.value
print "     MaximumVariableSize:          %d"   % MaximumVariableSize.value
print

VariableName  = u"TestingVariable"
VariableGuid  = EFI_GUID( 0x8BE4DF61, 0x93CA, 0x11d2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8D))
Attributes    = UINT32(EFI_VARIABLE_BOOTSERVICE_ACCESS | EFI_VARIABLE_NON_VOLATILE | EFI_VARIABLE_RUNTIME_ACCESS)
DataSize      = UINTN (0x05)
DataBuffer    = PCHAR8 ("AbCdE")

Status = gRT.SetVariable(
               VariableName,
               byref (VariableGuid),
               Attributes,
               DataSize,
               byref (DataBuffer)
               )

print " gRT.SetVariable(Name: \"%s\", Status:0x%016X)" % (VariableName, Status)

DataSize      = UINTN (0x00)

Status = gRT.GetVariable(
               VariableName,
               byref (VariableGuid),
               None,
               byref (DataSize),
               None
               )

print " gRT.GetVariable(Name: \"%s\", Status:0x%016X)" % (VariableName, Status)
print "     DataSize: %d" % DataSize.value
print

Attributes    = UINT32(0x00)
DataBuffer    = PCHAR8 ("\00" * DataSize.value)
print " New DataBuffer:", DataBuffer.value
print

Status = gRT.GetVariable(
               VariableName,
               byref (VariableGuid),
               byref (Attributes),
               byref (DataSize),
               byref (DataBuffer)
               )
print " gRT.GetVariable(Name: \"%s\", Status:0x%016X)" % (VariableName, Status)
print "     DataSize: %d, Attributes: %x" % (DataSize.value, Attributes.value)
print "     DataBuffer:", DataBuffer.value
print

print "================================================"
print "gRT Delete Variable..."
print

Attributes    = UINT32 (
                  EFI_VARIABLE_BOOTSERVICE_ACCESS |
                  EFI_VARIABLE_NON_VOLATILE       |
                  EFI_VARIABLE_RUNTIME_ACCESS
                  )
DataSize      = UINTN (0x00)

Status = gRT.SetVariable(
               VariableName,
               byref (VariableGuid),
               Attributes,
               DataSize,
               None
               )

print " gRT.SetVariable(Status:0x%016X)" % Status

DataSize      = UINTN (0x00)

Status = gRT.GetVariable(
               VariableName,
               byref (VariableGuid),
               None,
               byref (DataSize),
               None
               )

print " gRT.GetVariable(Status:0x%016X)" % Status

print
print "================================================"
print "gRT GetNextVariableName..."
print

VariableName  = u""
VariableSize  = UINTN (sizeof (CHAR16))
VariableGuid  = EFI_GUID()

print
print " Initial value"
print "   VariableName:%s\n   VariableSize: %d\n   VariableGuid: %s" % (
        PCHAR16(VariableName).value,
        VariableSize.value,
        VariableGuid
        )

Status = gRT.GetNextVariableName(
               byref (VariableSize),
               PCHAR16 (VariableName),
               byref (VariableGuid),
               )

print
print " gRT.GetNextVariableName(Status:0x%016X)" % Status
print "   VariableName:%s\n   VariableSize: %d\n   VariableGuid: %s" % (
        PCHAR16(VariableName).value,
        VariableSize.value,
        VariableGuid
        )

VariableName  = u"\x00" * (VariableSize.value / sizeof (CHAR16))

Status = gRT.GetNextVariableName(
               byref (VariableSize),
               PCHAR16 (VariableName),
               byref (VariableGuid),
               )

print
print " gRT.GetNextVariableName(Status:0x%016X)" % Status
print "   VariableName:%s\n   VariableSize: %d\n   VariableGuid: %s" % (
        PCHAR16(VariableName).value,
        VariableSize.value,
        VariableGuid
        )

Status = gRT.GetNextVariableName(             \
               byref (VariableSize),          \
               PCHAR16 (VariableName),        \
               byref (VariableGuid),          \
               )

print
print " gRT.GetNextVariableName(Status:0x%016X)" % Status
print "   VariableName:%s\n   VariableSize: %d\n   VariableGuid: %s" % (
        PCHAR16(VariableName).value,
        VariableSize.value,
        VariableGuid
        )
