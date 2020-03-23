#
# BootLogo.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# BootLogo.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Protocol.GraphicsOutput import EFI_GRAPHICS_OUTPUT_BLT_PIXEL

gEfiBootLogoProtocolGuid  = \
  EFI_GUID (0xcdea2bd3, 0xfc25, 0x4c1c, (0xb9, 0x7c, 0xb3, 0x11, 0x86, 0x6, 0x49, 0x90 ))

class EFI_BOOT_LOGO_PROTOCOL (Structure):
  pass

EFI_SET_BOOT_LOGO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BOOT_LOGO_PROTOCOL),        #   IN *This,
  POINTER(EFI_GRAPHICS_OUTPUT_BLT_PIXEL), #   IN *BltBuffer       OPTIONAL,
  UINTN,                                  #   IN DestinationX,
  UINTN,                                  #   IN DestinationY,
  UINTN,                                  #   IN Width,
  UINTN                                   #   IN Height
  )

EFI_BOOT_LOGO_PROTOCOL._fields_ = [
    ("SetBootLogo", EFI_SET_BOOT_LOGO)
  ]

