#
# Ebc.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Ebc.py is free software: you can redistribute it and/or
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

gEfiEbcProtocolGuid   = \
  EFI_GUID (0x13AC6DD1, 0x73D0, 0x11D4, (0xB0, 0x6B, 0x00, 0xAA, 0x00, 0xBD, 0x6D, 0xE7 ))

class EFI_EBC_PROTOCOL (Structure):
  pass

EFI_EBC_CREATE_THUNK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_PROTOCOL),  # IN  *This
  EFI_HANDLE,                 # IN  ImageHandle,
  PVOID,                      # IN  *EbcEntryPoint,
  POINTER(PVOID)              # OUT **Thunk
  )

EFI_EBC_UNLOAD_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_PROTOCOL),  # IN  *This
  EFI_HANDLE                  # IN  ImageHandle
  )

EBC_ICACHE_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN  Start
  UINT64                # IN  Length
  )

EFI_EBC_REGISTER_ICACHE_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_PROTOCOL),  # IN  *This
  EBC_ICACHE_FLUSH            # IN  Flush
  )

EFI_EBC_GET_VERSION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_PROTOCOL),  # IN  *This
  POINTER(UINT64)             # IN  *Version
  )

EFI_EBC_PROTOCOL._fields_ = [
    ("CreateThunk",         EFI_EBC_CREATE_THUNK),
    ("UnloadImage",         EFI_EBC_UNLOAD_IMAGE),
    ("RegisterICacheFlush", EFI_EBC_REGISTER_ICACHE_FLUSH),
    ("GetVersion",          EFI_EBC_GET_VERSION)
  ]

