#
# CpuIo2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# CpuIo2.py is free software: you can redistribute it and/or
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

gEfiCpuIo2ProtocolGuid                  = \
  EFI_GUID (0xad61f191, 0xae5f, 0x4c0e, (0xb9, 0xfa, 0xe8, 0x69, 0xd2, 0x88, 0xc6, 0x4f))

class EFI_CPU_IO2_PROTOCOL (Structure):
  pass

EfiCpuIoWidthUint8        =  0
EfiCpuIoWidthUint16       =  1
EfiCpuIoWidthUint32       =  2
EfiCpuIoWidthUint64       =  3
EfiCpuIoWidthFifoUint8    =  4
EfiCpuIoWidthFifoUint16   =  5
EfiCpuIoWidthFifoUint32   =  6
EfiCpuIoWidthFifoUint64   =  7
EfiCpuIoWidthFillUint8    =  8
EfiCpuIoWidthFillUint16   =  9
EfiCpuIoWidthFillUint32   = 10
EfiCpuIoWidthFillUint64   = 11
EfiCpuIoWidthMaximum      = 12
EFI_CPU_IO_PROTOCOL_WIDTH = ENUM

EFI_CPU_IO_PROTOCOL_IO_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_IO2_PROTOCOL),  # IN     *This,
  EFI_CPU_IO_PROTOCOL_WIDTH,      # IN     Width,
  UINT64,                         # IN     Address,
  UINTN,                          # IN     Count
  PVOID                           # IN OUT *Buffer
  )

class EFI_CPU_IO_PROTOCOL_ACCESS (Structure):
  _fields_ = [
    ("Read",  EFI_CPU_IO_PROTOCOL_IO_MEM),
    ("Write", EFI_CPU_IO_PROTOCOL_IO_MEM)
  ]

EFI_CPU_IO2_PROTOCOL._fields_ = [
    ("Mem", EFI_CPU_IO_PROTOCOL_ACCESS),
    ("Io",  EFI_CPU_IO_PROTOCOL_ACCESS)
  ]

