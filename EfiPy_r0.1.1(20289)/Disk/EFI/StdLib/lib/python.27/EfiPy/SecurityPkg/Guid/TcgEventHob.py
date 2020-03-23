#
# TcgEventHob.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# TcgEventHob.py is free software: you can redistribute it and/or
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

gTcgEventEntryHobGuid = \
  EFI_GUID (0x2b9ffb52, 0x1b13, 0x416f, (0xa8, 0x7b, 0xbc, 0x93, 0xd, 0xef, 0x92, 0xa8))

gTcgEvent2EntryHobGuid = \
  EFI_GUID (0xd26c221e, 0x2430, 0x4c8a, (0x91, 0x70, 0x3f, 0xcb, 0x45, 0x0, 0x41, 0x3f))

gTpmErrorHobGuid = \
  EFI_GUID (0xef598499, 0xb25e, 0x473a, (0xbf, 0xaf, 0xe7, 0xe5, 0x7d, 0xce, 0x82, 0xc4))

