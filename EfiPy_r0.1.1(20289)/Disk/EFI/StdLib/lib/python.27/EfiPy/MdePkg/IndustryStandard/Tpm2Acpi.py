#
# Tpm2Acpi.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Tpm2Acpi.py is free software: you can redistribute it and/or modify
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

EFI_TPM2_ACPI_TABLE_REVISION  = 3

class EFI_TPM2_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",                      Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Flags",                       UINT32),
    ("AddressOfControlArea",        UINT64),
    ("StartMethod",                 UINT32)
    # ("PlatformSpecificParameters",  UINT8 * N),
  ]

EFI_TPM2_ACPI_TABLE_START_METHOD_ACPI                                          = 2
EFI_TPM2_ACPI_TABLE_START_METHOD_TIS                                           = 6
EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE             = 7
EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE_WITH_ACPI   = 8

class EFI_TPM2_ACPI_TABLE (Structure):
  _fields_ = [
    ("Reserved",          UINT32),
    ("Error",             UINT32),
    ("Cancel",            UINT32),
    ("Start",             UINT32),
    ("InterruptControl",  UINT64),
    ("CommandSize",       UINT32),
    ("Command",           UINT64),
    ("ResponseSize",      UINT32),
    ("Response",          UINT64)
  ]

