#!/usr/bin/python

#
# test_gST.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# test_gST.py is free software: you can redistribute it and/or modify
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
# EFI_SYSTEM_TABLE header
#

print "************************************************"
print "EFI_SYSTEM_TABLE testing..."
print "************************************************"
print
print " gST :"
print " gST.Hdr.Signature:   (*)0x%016X" % gST.Hdr.Signature
print " gST.Hdr.Revision:       0x%016X" % gST.Hdr.Revision
print " gST.Hdr.HeaderSize:     0x%016X (0x%016X)" % (gST.Hdr.HeaderSize, sizeof (gST))
print " gST.Hdr.CRC32:          0x%016X" % gST.Hdr.CRC32

print
print "================================================"
print "Firmware Information..."
print
print " gST.FirmwareVendor:     \"%s\""   % gST.FirmwareVendor
print " gST.FirmwareRevision:   0x%08X"   % gST.FirmwareRevision
print " gST.RuntimeServices:    0x%016X"  % addressof (gST.RuntimeServices[0])
print " gST.BootServices:       0x%016X"  % addressof (gST.BootServices[0])

print
print "================================================"
print "Console Input..."
print
print " gST.ConsoleInHandle:      0x%016X" % gST.ConsoleInHandle

print
print "================================================"
print "Console Output..."
print
print " gST.ConsoleOutHandle:     0x%016X" % gST.ConsoleOutHandle
print " addressof (gST.ConOut[0]) 0x%016X" % addressof (gST.ConOut[0])
print " Max Mode:                 %d"      % gST.ConOut[0].Mode[0].MaxMode

print
print "================================================"
print "Error Output..."
print
print " gST.StandardErrorHandle:  0x%016X" % gST.StandardErrorHandle

print
print "================================================"
print "Configuration Tables..."
print
print " gST.NumberOfTableEntries: 0x%016X" % gST.NumberOfTableEntries
print

for i in range (gST.NumberOfTableEntries):
  print "  gST.ConfigurationTable[%d]: %s" % (i, gST.ConfigurationTable[i].VendorGuid)
