#
# DebugPort2Table.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DebugPort2Table.py is free software: you can redistribute it and/or modify
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

from EfiPy.MdePkg.IndustryStandard import *

import Acpi

class EFI_ACPI_DBG2_DEBUG_DEVICE_INFORMATION_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Revision",                        UINT8 ),
    ("Length",                          UINT16),
    ("NumberofGenericAddressRegisters", UINT8 ),
    ("NameSpaceStringLength",           UINT16),
    ("NameSpaceStringOffset",           UINT16),
    ("OemDataLength",                   UINT16),
    ("OemDataOffset",                   UINT16),
    ("PortType",                        UINT16),
    ("PortSubtype",                     UINT16),
    ("Reserved",                        UINT8 * 2),
    ("BaseAddressRegisterOffset",       UINT16),
    ("AddressSizeOffset",               UINT16)
  ]

EFI_ACPI_DBG2_DEBUG_DEVICE_INFORMATION_STRUCT_REVISION      = 0x00

EFI_ACPI_DBG2_PORT_TYPE_SERIAL                                               = 0x8000
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_FULL_16550                                 = 0x0000
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_16550_SUBSET_COMPATIBLE_WITH_MS_DBGP_SPEC  = 0x0001
EFI_ACPI_DBG2_PORT_TYPE_1394                                                 = 0x8001
EFI_ACPI_DBG2_PORT_SUBTYPE_1394_STANDARD                                     = 0x0000
EFI_ACPI_DBG2_PORT_TYPE_USB                                                  = 0x8002
EFI_ACPI_DBG2_PORT_SUBTYPE_USB_XHCI                                          = 0x0000
EFI_ACPI_DBG2_PORT_SUBTYPE_USB_EHCI                                          = 0x0001
EFI_ACPI_DBG2_PORT_TYPE_NET                                                  = 0x8003

class EFI_ACPI_DEBUG_PORT_2_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("OffsetDbgDeviceInfo",   UINT32),
    ("NumberDbgDeviceInfo",   UINT32)
  ]

EFI_ACPI_DEBUG_PORT_2_TABLE_REVISION      = 0x00

