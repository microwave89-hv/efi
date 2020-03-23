#
# UefiTcgPlatform.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UefiTcgPlatform.py is free software: you can redistribute it and/or modify
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

from EfiPy.MdePkg.IndustryStandard          import *
from EfiPy.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL
from EfiPy.MdePkg.Uefi.UefiSpec             import EFI_CONFIGURATION_TABLE
from EfiPy.MdePkg.Uefi                      import UefiGpt

import Tpm12
# import Uefi

TCG_EVENTTYPE = UINT32

EV_POST_CODE                = TCG_EVENTTYPE (0x00000001).value
EV_SEPARATOR                = TCG_EVENTTYPE (0x00000004).value
EV_S_CRTM_CONTENTS          = TCG_EVENTTYPE (0x00000007).value
EV_S_CRTM_VERSION           = TCG_EVENTTYPE (0x00000008).value
EV_CPU_MICROCODE            = TCG_EVENTTYPE (0x00000009).value
EV_TABLE_OF_DEVICES         = TCG_EVENTTYPE (0x0000000B).value

EV_EFI_EVENT_BASE                   = TCG_EVENTTYPE (0x80000000).value
EV_EFI_VARIABLE_DRIVER_CONFIG       = (EV_EFI_EVENT_BASE + 1)
EV_EFI_VARIABLE_BOOT                = (EV_EFI_EVENT_BASE + 2)
EV_EFI_BOOT_SERVICES_APPLICATION    = (EV_EFI_EVENT_BASE + 3)
EV_EFI_BOOT_SERVICES_DRIVER         = (EV_EFI_EVENT_BASE + 4)
EV_EFI_RUNTIME_SERVICES_DRIVER      = (EV_EFI_EVENT_BASE + 5)
EV_EFI_GPT_EVENT                    = (EV_EFI_EVENT_BASE + 6)
EV_EFI_ACTION                       = (EV_EFI_EVENT_BASE + 7)
EV_EFI_PLATFORM_FIRMWARE_BLOB       = (EV_EFI_EVENT_BASE + 8)
EV_EFI_HANDOFF_TABLES               = (EV_EFI_EVENT_BASE + 9)

EFI_CALLING_EFI_APPLICATION         = \
   "Calling EFI Application from Boot Option"
EFI_RETURNING_FROM_EFI_APPLICATOIN  = \
   "Returning from EFI Application from Boot Option"
EFI_EXIT_BOOT_SERVICES_INVOCATION   = \
   "Exit Boot Services Invocation"
EFI_EXIT_BOOT_SERVICES_FAILED       = \
   "Exit Boot Services Returned with Failure"
EFI_EXIT_BOOT_SERVICES_SUCCEEDED    = \
   "Exit Boot Services Returned with Success"

EV_POSTCODE_INFO_POST_CODE    = "POST CODE"
POST_CODE_STR_LEN             = len (EV_POSTCODE_INFO_POST_CODE)

EV_POSTCODE_INFO_SMM_CODE     = "SMM CODE"
SMM_CODE_STR_LEN             = len (EV_POSTCODE_INFO_SMM_CODE)

EV_POSTCODE_INFO_ACPI_DATA    = "ACPI DATA"
ACPI_DATA_LEN                 = len (EV_POSTCODE_INFO_ACPI_DATA)

EV_POSTCODE_INFO_BIS_CODE     = "BIS CODE"
BIS_CODE_LEN                  = len (EV_POSTCODE_INFO_BIS_CODE)

EV_POSTCODE_INFO_UEFI_PI      = "UEFI PI"
UEFI_PI_LEN                   = len (EV_POSTCODE_INFO_UEFI_PI)

EV_POSTCODE_INFO_OPROM        = "Embedded Option ROM"
OPROM_LEN                     = len (EV_POSTCODE_INFO_OPROM)

TCG_PCRINDEX  = Tpm12.TPM_PCRINDEX
TCG_DIGEST    = Tpm12.TPM_DIGEST

class TCG_PCR_EVENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PCRIndex",  TCG_PCRINDEX),
    ("EventType", TCG_EVENTTYPE),
    ("Digest",    TCG_DIGEST),
    ("EventSize", UINT32),
    ("Event",     UINT8 * 1)
  ]

TSS_EVENT_DATA_MAX_SIZE   = 256

class TCG_PCR_EVENT_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PCRIndex",  TCG_PCRINDEX),
    ("EventType", TCG_EVENTTYPE),
    ("Digest",    TCG_DIGEST),
    ("EventSize", UINT32),
  ]

class EFI_PLATFORM_FIRMWARE_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlobBase",    EFI_PHYSICAL_ADDRESS),
    ("BlobLength",  UINT64)
  ]

class EFI_IMAGE_LOAD_EVENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ImageLocationInMemory", EFI_PHYSICAL_ADDRESS),
    ("ImageLengthInMemory",   UINTN),
    ("ImageLinkTimeAddress",  UINTN),
    ("LengthOfDevicePath",    UINTN),
    ("DevicePath",            EFI_DEVICE_PATH_PROTOCOL * 1)
  ]

class EFI_HANDOFF_TABLE_POINTERS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumberOfTables",  UINTN),
    ("TableEntry",      EFI_CONFIGURATION_TABLE * 1)
  ]

class EFI_VARIABLE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VariableName",        EFI_GUID),
    ("UnicodeNameLength",   UINTN),
    ("VariableDataLength",  UINTN),
    ("UnicodeName",         CHAR16 * 1),
    ("VariableData",        INT8 * 1)
  ]

class EFI_GPT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EfiPartitionHeader",  UefiGpt.EFI_PARTITION_TABLE_HEADER),
    ("NumberOfPartitions",  UINTN),
    ("Partitions",          UefiGpt.EFI_PARTITION_ENTRY * 1)
  ]

