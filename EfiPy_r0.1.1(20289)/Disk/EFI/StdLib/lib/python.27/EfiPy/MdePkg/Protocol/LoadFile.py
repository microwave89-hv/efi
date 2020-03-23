#
# LoadFile.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# LoadFile.py is free software: you can redistribute it and/or
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

gEfiLoadFileProtocolGuid  = \
  EFI_GUID (0x56EC3091, 0x954C, 0x11d2, (0x8E, 0x3F, 0x00, 0xA0, 0xC9, 0x69, 0x72, 0x3B ))

class EFI_LOAD_FILE_PROTOCOL (Structure):
  pass

EFI_LOAD_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LOAD_FILE_PROTOCOL),    # IN      *This
  POINTER(EFI_DEVICE_PATH_PROTOCOL),  # IN      *FilePath,
  BOOLEAN,                            # IN      BootPolicy,
  POINTER(UINTN),                     # IN OUT  *BufferSize,
  PVOID                               # IN      *Buffer OPTIONAL
  )

EFI_LOAD_FILE_PROTOCOL._fields_ = [
    ("LoadFile",    EFI_LOAD_FILE)
  ]

