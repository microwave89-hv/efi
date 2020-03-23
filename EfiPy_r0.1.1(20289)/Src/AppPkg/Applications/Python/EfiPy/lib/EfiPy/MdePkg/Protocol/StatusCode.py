#
# StatusCode.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# StatusCode.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi.PiStatusCode  import \
    EFI_STATUS_CODE_TYPE,   \
    EFI_STATUS_CODE_VALUE,  \
    EFI_STATUS_CODE_DATA

gEfiStatusCodeRuntimeProtocolGuid   = \
  EFI_GUID (0xd2b2b828, 0x826, 0x48a7,  ( 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0 ))

EFI_REPORT_STATUS_CODE = CFUNCTYPE (
  EFI_STATUS,
  EFI_STATUS_CODE_TYPE,         # IN Type,
  EFI_STATUS_CODE_VALUE,        # IN Value,
  UINT32,                       # IN Instance,
  POINTER(EFI_GUID),            # IN *CallerId  OPTIONAL,
  POINTER(EFI_STATUS_CODE_DATA) # IN *Data      OPTIONAL
  )

class EFI_STATUS_CODE_PROTOCOL (Structure):
  _fields_ = [
    ("ReportStatusCode",  EFI_REPORT_STATUS_CODE)
  ]

