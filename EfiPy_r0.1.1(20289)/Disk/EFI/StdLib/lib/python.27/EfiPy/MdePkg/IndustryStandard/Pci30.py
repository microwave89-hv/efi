# 
# Pci30.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Pci30.py is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
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
from Pci23 import *

PCI_CLASS_MASS_STORAGE_SATADPA   = 0x06
PCI_IF_MASS_STORAGE_SATA         = 0x00
PCI_IF_MASS_STORAGE_AHCI         = 0x01

PCI_SUBCLASS_ETHERNET_80211A    = 0x20
PCI_SUBCLASS_ETHERNET_80211B    = 0x21

def IS_PCI_SATADPA(_p):
  return IS_CLASS2 (_p, PCI_CLASS_MASS_STORAGE, PCI_CLASS_MASS_STORAGE_SATADPA)

EFI_PCI_CAPABILITY_ID_PCIEXP  = 0x10

class PCI_3_0_DATA_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",                     UINT32),
    ("VendorId",                      UINT16),
    ("DeviceId",                      UINT16),
    ("DeviceListOffset",              UINT16),
    ("Length",                        UINT16),
    ("Revision",                      UINT8),
    ("ClassCode",                     UINT8 * 3),
    ("ImageLength",                   UINT16),
    ("CodeRevision",                  UINT16),
    ("CodeType",                      UINT8),
    ("Indicator",                     UINT8),
    ("MaxRuntimeImageLength",         UINT16),
    ("ConfigUtilityCodeHeaderOffset", UINT16),
    ("DMTFCLPEntryPointOffset",       UINT16)
    ]

