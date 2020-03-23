#
# UefiAcpiDataTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UefiAcpiDataTable.py is free software: you can redistribute it and/or
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

from EfiPy import *

from EfiPy.MdePkg.IndustryStandard  import Acpi
class EFI_ACPI_DATA_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Identifier",  GUID),
    ("DataOffset",  UINT16)
  ]

class EFI_SMM_COMMUNICATION_ACPI_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("UefiAcpiDataTable", EFI_ACPI_DATA_TABLE),
    ("SwSmiNumber",       UINT32),
    ("BufferPtrAddress",  UINT64)
  ]

class EFI_SMM_COMMUNICATE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("HeaderGuid",    EFI_GUID),
    ("MessageLength", UINTN),
    ("Data",          UINT8 * 1)
  ]

