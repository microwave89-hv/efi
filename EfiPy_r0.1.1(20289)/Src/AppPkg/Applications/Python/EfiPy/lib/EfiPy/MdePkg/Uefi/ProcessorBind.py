#!/usr/bin/python

#
# ProcessorBind.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# ProcessorBind.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

from ctypes   import *

UINT64  = c_uint64
INT64   = c_int64
UINT32  = c_uint32
INT32   = c_int32
UINT16  = c_uint16
CHAR16  = c_wchar
PCHAR16 = c_wchar_p
INT16   = c_int16
BOOLEAN = c_uint8
UINT8   = c_uint8
CHAR8   = c_char
PCHAR8  = c_char_p
INT8    = c_int8
UINTN   = c_uint64
INTN    = c_int64
