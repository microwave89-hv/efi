#
# MemoryProfile.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# MemoryProfile.py is free software: you can redistribute it and/or
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

from EfiPy  import *
from EfiPy.MdePkg.Protocol.FirmwareVolume2 import EFI_FV_FILETYPE

class MEMORY_PROFILE_COMMON_HEADER (Structure):
  _fields_ = [
  ("Signature", UINT32),
  ("Length",    UINT16),
  ("Revision",  UINT16)
  ]

MEMORY_PROFILE_CONTEXT_SIGNATURE = SIGNATURE_32 ('M','P','C','T')
MEMORY_PROFILE_CONTEXT_REVISION  = 0x0002

class MEMORY_PROFILE_CONTEXT (Structure):
  _fields_ = [
  ("Header",                    MEMORY_PROFILE_COMMON_HEADER),
  ("CurrentTotalUsage",         UINT64),
  ("PeakTotalUsage",            UINT64),
  ("CurrentTotalUsageByType",   UINT64 * (EfiMaxMemoryType + 2)),
  ("PeakTotalUsageByType",      UINT64 * (EfiMaxMemoryType + 2)),
  ("TotalImageSize",            UINT64),
  ("ImageCount",                UINT32),
  ("SequenceCount",             UINT32)
  ]

MEMORY_PROFILE_DRIVER_INFO_SIGNATURE = SIGNATURE_32 ('M','P','D','I')
MEMORY_PROFILE_DRIVER_INFO_REVISION  = 0x0002

class MEMORY_PROFILE_DRIVER_INFO (Structure):
  _fields_ = [
  ("Header",              MEMORY_PROFILE_COMMON_HEADER),
  ("FileName",            EFI_GUID),
  ("ImageBase",           PHYSICAL_ADDRESS),
  ("ImageSize",           UINT64),
  ("EntryPoint",          PHYSICAL_ADDRESS),
  ("ImageSubsystem",      UINT16),
  ("FileType",            EFI_FV_FILETYPE),
  ("Reserved",            UINT8 * 1),
  ("AllocRecordCount",    UINT32),
  ("CurrentUsage",        UINT64),
  ("PeakUsage",           UINT64),
  ("CurrentUsageByType",  UINT64 * (EfiMaxMemoryType + 2)),
  ("PeakUsageByType",     UINT64 * (EfiMaxMemoryType + 2))
  ]

MemoryProfileActionAllocatePages = 1
MemoryProfileActionFreePages = 2
MemoryProfileActionAllocatePool = 3
MemoryProfileActionFreePool = 4
MEMORY_PROFILE_ACTION = UINTN

MEMORY_PROFILE_ALLOC_INFO_SIGNATURE = SIGNATURE_32 ('M','P','A','I')
MEMORY_PROFILE_ALLOC_INFO_REVISION  = 0x0001
class MEMORY_PROFILE_ALLOC_INFO (Structure):
  _fields_ = [
  ("Header",        MEMORY_PROFILE_COMMON_HEADER),
  ("CallerAddress", PHYSICAL_ADDRESS),
  ("SequenceId",    UINT32),
  ("Reserved",      UINT8 * 4),
  ("Action",        MEMORY_PROFILE_ACTION),
  ("MemoryType",    EFI_MEMORY_TYPE),
  ("Buffer",        PHYSICAL_ADDRESS),
  ("Size",          UINT64)
  ]

MEMORY_PROFILE_DESCRIPTOR_SIGNATURE = SIGNATURE_32 ('M','P','D','R')
MEMORY_PROFILE_DESCRIPTOR_REVISION  = 0x0001

class MEMORY_PROFILE_DESCRIPTOR (Structure):
  _fields_ = [
  ("Header",    MEMORY_PROFILE_COMMON_HEADER),
  ("Address",   PHYSICAL_ADDRESS),
  ("Size",      UINT64)
  ]

MEMORY_PROFILE_FREE_MEMORY_SIGNATURE  = SIGNATURE_32 ('M','P','R','M')
MEMORY_PROFILE_FREE_MEMORY_REVISION   = 0x0001

class MEMORY_PROFILE_DESCRIPTOR (Structure):
  _fields_ = [
  ("Header",                MEMORY_PROFILE_COMMON_HEADER),
  ("TotalFreeMemoryPages",  UINT64),
  ("FreeMemoryEntryCount",  UINT32),
  ("Reserved",              UINT8 * 4)
  # ("MemoryDescriptor",    MEMORY_PROFILE_DESCRIPTOR * FreeMemoryEntryCount)
  ]

MEMORY_PROFILE_MEMORY_RANGE_SIGNATURE = SIGNATURE_32 ('M','P','M','R')
MEMORY_PROFILE_MEMORY_RANGE_REVISION  = 0x0001

class MEMORY_PROFILE_DESCRIPTOR (Structure):
  _fields_ = [
  ("Header",                MEMORY_PROFILE_COMMON_HEADER),
  ("MemoryRangeCount",      UINT32),
  ("Reserved",              UINT8 * 4)
  # ("MemoryDescriptor",    MEMORY_PROFILE_DESCRIPTOR * MemoryRangeCount)
  ]

class EDKII_MEMORY_PROFILE_PROTOCOL (Structure):
  pass

EDKII_MEMORY_PROFILE_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_MEMORY_PROFILE_PROTOCOL),   # IN     *This,
  UINT64,                                   # IN OUT *ProfileSize
  PVOID                                     #    OUT *ProfileBuffer
  )

EDKII_MEMORY_PROFILE_REGISTER_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_MEMORY_PROFILE_PROTOCOL),   # IN *This,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),        # IN *FilePath,
  PHYSICAL_ADDRESS,                         # IN ImageBase,
  UINT64,                                   # IN ImageSize,
  EFI_FV_FILETYPE                           # IN FileType
  )

EDKII_MEMORY_PROFILE_UNREGISTER_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_MEMORY_PROFILE_PROTOCOL),   # IN *This,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),        # IN *FilePath,
  PHYSICAL_ADDRESS,                         # IN ImageBase,
  UINT64                                    # IN ImageSize
  )

EDKII_MEMORY_PROFILE_PROTOCOL._fields_ = [
  ("GetData",         EDKII_MEMORY_PROFILE_GET_DATA),
  ("RegisterImage",   EDKII_MEMORY_PROFILE_REGISTER_IMAGE),
  ("UnregisterImage", EDKII_MEMORY_PROFILE_UNREGISTER_IMAGE)
  ]

SMRAM_PROFILE_COMMAND_GET_PROFILE_INFO         = 0x1
SMRAM_PROFILE_COMMAND_GET_PROFILE_DATA         = 0x2

SMRAM_PROFILE_COMMAND_REGISTER_IMAGE           = 0x3
SMRAM_PROFILE_COMMAND_UNREGISTER_IMAGE         = 0x4

class SMRAM_PROFILE_PARAMETER_HEADER (Structure):
  _fields_ = [
  ("Command",       UINT32),
  ("DataLength",    UINT32),
  ("ReturnStatus",  UINT64)
  ]

class SMRAM_PROFILE_PARAMETER_GET_PROFILE_INFO (Structure):
  _fields_ = [
  ("Header",      SMRAM_PROFILE_PARAMETER_HEADER),
  ("ProfileSize", UINT64)
  ]

class SMRAM_PROFILE_PARAMETER_GET_PROFILE_DATA (Structure):
  _fields_ = [
  ("Header",        SMRAM_PROFILE_PARAMETER_HEADER),
  ("ProfileSize",   UINT64),
  ("ProfileBuffer", PHYSICAL_ADDRESS)
  ]

class SMRAM_PROFILE_PARAMETER_REGISTER_IMAGE (Structure):
  _fields_ = [
  ("Header",        SMRAM_PROFILE_PARAMETER_HEADER),
  ("FileName",      EFI_GUID),
  ("ImageBuffer",   PHYSICAL_ADDRESS),
  ("NumberOfPage",  UINT64)
  ]

class SMRAM_PROFILE_PARAMETER_UNREGISTER_IMAGE (Structure):
  _fields_ = [
  ("Header",        SMRAM_PROFILE_PARAMETER_HEADER),
  ("FileName",      EFI_GUID),
  ("ImageBuffer",   PHYSICAL_ADDRESS),
  ("NumberOfPage",  UINT64)
  ]

gEdkiiMemoryProfileGuid         = \
  EFI_GUID (0x821c9a09, 0x541a, 0x40f6, (0x9f, 0x43, 0xa, 0xd1, 0x93, 0xa1, 0x2c, 0xfe))

