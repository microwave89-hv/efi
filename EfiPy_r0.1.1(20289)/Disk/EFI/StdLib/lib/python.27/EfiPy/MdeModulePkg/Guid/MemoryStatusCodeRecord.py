#
# MemoryStatusCodeRecord.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# MemoryStatusCodeRecord.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi.PiStatusCode import EFI_STATUS_CODE_TYPE, EFI_STATUS_CODE_VALUE

class MEMORY_STATUSCODE_PACKET_HEADER (Structure):
  _fields_ = [
  ("PacketIndex",       UINT16),
  ("RecordIndex",       UINT16),
  ("MaxRecordsNumber",  UINT32)
  ]

class MEMORY_STATUSCODE_RECORD (Structure):
  _fields_ = [
  ("CodeType",  EFI_STATUS_CODE_TYPE),
  ("Value",     EFI_STATUS_CODE_VALUE),
  ("Instance",  UINT32)
  ]

gMemoryStatusCodeRecordGuid         = \
  EFI_GUID (0x60cc026, 0x4c0d, 0x4dda, (0x8f, 0x41, 0x59, 0x5f, 0xef, 0x0, 0xa5, 0x2))

