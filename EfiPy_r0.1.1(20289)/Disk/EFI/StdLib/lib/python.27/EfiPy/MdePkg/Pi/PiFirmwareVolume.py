#
# PiFirmwareVolume.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PiFirmwareVolume.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

from EfiPy import *

EFI_FV_FILE_ATTRIBUTES                  = UINT32

EFI_FV_FILE_ATTRIB_ALIGNMENT      = 0x0000001F
EFI_FV_FILE_ATTRIB_FIXED          = 0x00000100
EFI_FV_FILE_ATTRIB_MEMORY_MAPPED  = 0x00000200

EFI_FVB_ATTRIBUTES_2                    = UINT32
EFI_FVB2_READ_DISABLED_CAP  = 0x00000001
EFI_FVB2_READ_ENABLED_CAP   = 0x00000002
EFI_FVB2_READ_STATUS        = 0x00000004
EFI_FVB2_WRITE_DISABLED_CAP = 0x00000008
EFI_FVB2_WRITE_ENABLED_CAP  = 0x00000010
EFI_FVB2_WRITE_STATUS       = 0x00000020
EFI_FVB2_LOCK_CAP           = 0x00000040
EFI_FVB2_LOCK_STATUS        = 0x00000080
EFI_FVB2_STICKY_WRITE       = 0x00000200
EFI_FVB2_MEMORY_MAPPED      = 0x00000400
EFI_FVB2_ERASE_POLARITY     = 0x00000800
EFI_FVB2_READ_LOCK_CAP      = 0x00001000
EFI_FVB2_READ_LOCK_STATUS   = 0x00002000
EFI_FVB2_WRITE_LOCK_CAP     = 0x00004000
EFI_FVB2_WRITE_LOCK_STATUS  = 0x00008000
EFI_FVB2_ALIGNMENT          = 0x001F0000
EFI_FVB2_ALIGNMENT_1        = 0x00000000
EFI_FVB2_ALIGNMENT_2        = 0x00010000
EFI_FVB2_ALIGNMENT_4        = 0x00020000
EFI_FVB2_ALIGNMENT_8        = 0x00030000
EFI_FVB2_ALIGNMENT_16       = 0x00040000
EFI_FVB2_ALIGNMENT_32       = 0x00050000
EFI_FVB2_ALIGNMENT_64       = 0x00060000
EFI_FVB2_ALIGNMENT_128      = 0x00070000
EFI_FVB2_ALIGNMENT_256      = 0x00080000
EFI_FVB2_ALIGNMENT_512      = 0x00090000
EFI_FVB2_ALIGNMENT_1K       = 0x000A0000
EFI_FVB2_ALIGNMENT_2K       = 0x000B0000
EFI_FVB2_ALIGNMENT_4K       = 0x000C0000
EFI_FVB2_ALIGNMENT_8K       = 0x000D0000
EFI_FVB2_ALIGNMENT_16K      = 0x000E0000
EFI_FVB2_ALIGNMENT_32K      = 0x000F0000
EFI_FVB2_ALIGNMENT_64K      = 0x00100000
EFI_FVB2_ALIGNMENT_128K     = 0x00110000
EFI_FVB2_ALIGNMENT_256K     = 0x00120000
EFI_FVB2_ALIGNMENT_512K     = 0x00130000
EFI_FVB2_ALIGNMENT_1M       = 0x00140000
EFI_FVB2_ALIGNMENT_2M       = 0x00150000
EFI_FVB2_ALIGNMENT_4M       = 0x00160000
EFI_FVB2_ALIGNMENT_8M       = 0x00170000
EFI_FVB2_ALIGNMENT_16M      = 0x00180000
EFI_FVB2_ALIGNMENT_32M      = 0x00190000
EFI_FVB2_ALIGNMENT_64M      = 0x001A0000
EFI_FVB2_ALIGNMENT_128M     = 0x001B0000
EFI_FVB2_ALIGNMENT_256M     = 0x001C0000
EFI_FVB2_ALIGNMENT_512M     = 0x001D0000
EFI_FVB2_ALIGNMENT_1G       = 0x001E0000
EFI_FVB2_ALIGNMENT_2G       = 0x001F0000
EFI_FVB2_WEAK_ALIGNMENT     = 0x80000000

class EFI_FV_BLOCK_MAP_ENTRY (Structure):
  _fields_ = [
    ("NumBlocks", UINT32),
    ("Length",    UINT32)
  ]

class EFI_FIRMWARE_VOLUME_HEADER (Structure):
  _fields_ = [
    ("ZeroVector",      UINT8 * 16),
    ("FileSystemGuid",  EFI_GUID),
    ("FvLength",        UINT64),
    ("Signature",       UINT32),
    ("Attributes",      EFI_FVB_ATTRIBUTES_2),
    ("HeaderLength",    UINT16),
    ("Checksum",        UINT16),
    ("ExtHeaderOffset", UINT16),
    ("Reserved",        UINT8 * 1),
    ("Revision",        UINT8),
    ("BlockMap",        EFI_FV_BLOCK_MAP_ENTRY * 1)
  ]

EFI_FVH_SIGNATURE = SIGNATURE_32 ('_', 'F', 'V', 'H')

EFI_FVH_REVISION  = 0x02

class EFI_FIRMWARE_VOLUME_EXT_HEADER (Structure):
  _fields_ = [
    ("FvName",        EFI_GUID),
    ("ExtHeaderSize", UINT32)
  ]

class EFI_FIRMWARE_VOLUME_EXT_ENTRY (Structure):
  _fields_ = [
    ("ExtEntrySize",  UINT16),
    ("ExtEntryType",  UINT16)
  ]

EFI_FV_EXT_TYPE_OEM_TYPE  = 0x01

class EFI_FIRMWARE_VOLUME_EXT_ENTRY_OEM_TYPE (Structure):
  _fields_ = [
    ("Hdr",       EFI_FIRMWARE_VOLUME_EXT_ENTRY),
    ("TypeMask",  UINT32)
  ]

EFI_FV_EXT_TYPE_GUID_TYPE = 0x0002

class EFI_FIRMWARE_VOLUME_EXT_ENTRY_GUID_TYPE (Structure):
  _fields_ = [
    ("Hdr",         EFI_FIRMWARE_VOLUME_EXT_ENTRY),
    ("FormatType",  EFI_GUID)
    # ("Data",        UINT8 * N)
  ]

