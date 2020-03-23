# 
# GraphicsInfoHob.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# GraphicsInfoHob.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol  import GraphicsOutput

gEfiGraphicsInfoHobGuid = \
  EFI_GUID (0x39f62cce, 0x6825, 0x4669, ( 0xbb, 0x56, 0x54, 0x1a, 0xba, 0x75, 0x3a, 0x07 ))

class EFI_PEI_GRAPHICS_INFO_HOB (Structure):
  _fields_ = [
    ("FrameBufferBase", EFI_PHYSICAL_ADDRESS),
    ("FrameBufferSize", UINT32),
    ("GraphicsMode",    GraphicsOutput.EFI_GRAPHICS_OUTPUT_MODE_INFORMATION)
  ]

