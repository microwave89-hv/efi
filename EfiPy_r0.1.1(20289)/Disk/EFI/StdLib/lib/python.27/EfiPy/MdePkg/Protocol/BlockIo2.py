#
# BlockIo2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# BlockIo2.py is free software: you can redistribute it and/or
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

import BlockIo
gEfiBlockIo2ProtocolGuid                = \
  EFI_GUID (0xa77b2472, 0xe282, 0x4e9f, (0xa2, 0x45, 0xc2, 0xc0, 0xe2, 0x7b, 0xbc, 0xc1))

class EFI_BLOCK_IO2_PROTOCOL (Structure):
  pass

class EFI_BLOCK_IO2_TOKEN (Structure):
  _fields_ = [
    ("Event",               EFI_EVENT),
    ("TransactionStatus",   EFI_STATUS)
  ]

EFI_BLOCK_RESET_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO2_PROTOCOL), # IN  *This,              
  BOOLEAN                           # IN  ExtendedVerification         
  )

EFI_BLOCK_READ_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO2_PROTOCOL), # IN     *This,              
  UINT32,                           # IN     MediaId,
  EFI_LBA,                          # IN     LBA,
  POINTER (EFI_BLOCK_IO2_TOKEN),    # IN OUT *Token,
  UINTN,                            # IN     BufferSize,
  PVOID                             #    OUT *Buffer
  )

EFI_BLOCK_WRITE_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO2_PROTOCOL), # IN     *This,              
  UINT32,                           # IN     MediaId,
  EFI_LBA,                          # IN     LBA,
  POINTER (EFI_BLOCK_IO2_TOKEN),    # IN OUT *Token,
  UINTN,                            # IN     BufferSize,
  PVOID                             # IN     *Buffer
  )

EFI_BLOCK_FLUSH_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO2_PROTOCOL), # IN     *This,              
  POINTER (EFI_BLOCK_IO2_TOKEN)     # IN OUT *Token,
  )

EFI_BLOCK_IO2_PROTOCOL._fields_ = [
    ("Media",         POINTER (BlockIo.EFI_BLOCK_IO_MEDIA)),
    ("Reset",         EFI_BLOCK_RESET_EX),
    ("ReadBlocksEx",  EFI_BLOCK_READ_EX),
    ("WriteBlocksEx", EFI_BLOCK_WRITE_EX),
    ("FlushBlocksEx", EFI_BLOCK_FLUSH_EX)
  ]

