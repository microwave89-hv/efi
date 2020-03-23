#
# Ps2Policy.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Ps2Policy.py is free software: you can redistribute it and/or
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

gEfiPs2PolicyProtocolGuid = \
  EFI_GUID (0x4df19259, 0xdc71, 0x4d46, (0xbe, 0xf1, 0x35, 0x7b, 0xb5, 0x78, 0xc4, 0x18))

EFI_KEYBOARD_CAPSLOCK   = 0x0004
EFI_KEYBOARD_NUMLOCK    = 0x0002
EFI_KEYBOARD_SCROLLLOCK = 0x0001

EFI_PS2_INIT_HARDWARE = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE    # IN Handle
  )

class EFI_PS2_POLICY_PROTOCOL (Structure):
  _fields_ = [
    ("KeyboardLight",   UINT8),
    ("Ps2InitHardware", EFI_PS2_INIT_HARDWARE)
  ]

