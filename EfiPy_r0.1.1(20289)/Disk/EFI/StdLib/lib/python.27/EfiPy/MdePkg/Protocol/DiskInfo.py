#
# DiskInfo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DiskInfo.py is free software: you can redistribute it and/or
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

gEfiDiskInfoProtocolGuid      = \
  EFI_GUID (0xd432a67f, 0x14dc, 0x484b, (0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27 ))

class EFI_DISK_INFO_PROTOCOL (Structure):
  pass

gEfiDiskInfoIdeInterfaceGuid  = \
  EFI_GUID (0x5e948fe3, 0x26d3, 0x42b5, (0xaf, 0x17, 0x61, 0x2, 0x87, 0x18, 0x8d, 0xec ))

gEfiDiskInfoScsiInterfaceGuid = \
  EFI_GUID (0x8f74baa, 0xea36, 0x41d9, (0x95, 0x21, 0x21, 0xa7, 0xf, 0x87, 0x80, 0xbc ))

gEfiDiskInfoUsbInterfaceGuid  = \
  EFI_GUID (0xcb871572, 0xc11a, 0x47b5, (0xb4, 0x92, 0x67, 0x5e, 0xaf, 0xa7, 0x77, 0x27 ))

gEfiDiskInfoAhciInterfaceGuid = \
  EFI_GUID (0x9e498932, 0x4abc, 0x45af, (0xa3, 0x4d, 0x2, 0x47, 0x78, 0x7b, 0xe7, 0xc6 ))

gEfiDiskInfoNvmeInterfaceGuid = \
  EFI_GUID (0x3ab14680, 0x5d3f, 0x4a4d, (0xbc, 0xdc, 0xcc, 0x38, 0x0, 0x18, 0xc7, 0xf7 ))

gEfiDiskInfoUfsInterfaceGuid  = \
  EFI_GUID (0x4b3029cc, 0x6b98, 0x47fb, ( 0xbc, 0x96, 0x76, 0xdc, 0xb8, 0x4, 0x41, 0xf0 ))

EFI_DISK_INFO_INQUIRY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_INFO_PROTOCOL),    # IN     *This
  PVOID,                              # IN OUT *InquiryData,
  POINTER(UINT32)                     # IN OUT *InquiryDataSize 
  )

EFI_DISK_INFO_IDENTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_INFO_PROTOCOL),    # IN     *This
  PVOID,                              # IN OUT *IdentifyData,
  POINTER(UINT32)                     # IN OUT *IdentifyDataSize 
  )

EFI_DISK_INFO_SENSE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_INFO_PROTOCOL),    # IN     *This
  PVOID,                              # IN OUT *SenseData,
  POINTER(UINT32),                    # IN OUT *SenseDataSize 
  POINTER(UINT8)                      #    OUT *SenseDataNumber 
  )

EFI_DISK_INFO_WHICH_IDE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_INFO_PROTOCOL),    # IN     *This
  POINTER(UINT32),                    #    OUT *IdeChannel 
  POINTER(UINT32)                     #    OUT *IdeDevice 
  )

EFI_DISK_INFO_PROTOCOL._fields_ = [
    ("Interface", EFI_GUID),
    ("Inquiry",   EFI_DISK_INFO_INQUIRY),
    ("Identify",  EFI_DISK_INFO_IDENTIFY),
    ("SenseData", EFI_DISK_INFO_SENSE_DATA),
    ("WhichIde",  EFI_DISK_INFO_WHICH_IDE)
  ]

