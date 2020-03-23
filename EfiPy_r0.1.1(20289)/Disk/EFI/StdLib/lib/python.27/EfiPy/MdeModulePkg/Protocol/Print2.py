#
# Print2.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Print2.py is free software: you can redistribute it and/or
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

gEfiPrint2ProtocolGuid = \
  EFI_GUID (0xf05976ef, 0x83f1, 0x4f3d, (0x86, 0x19, 0xf7, 0x59, 0x5d, 0x41, 0xe5, 0x38))

class EFI_PRINT2_PROTOCOL (Structure):
  pass

UNICODE_BS_PRINT = CFUNCTYPE (
  UINTN,
  POINTER(CHAR16),  # OUT *StartOfBuffer,
  UINTN,            # IN  BufferSize,
  POINTER(CHAR16),  # IN  CONST *FormatString,
  BASE_LIST         # IN  Marker
  )

UNICODE_S_PRINT = CFUNCTYPE (
  UINTN,
  POINTER(CHAR16),  # OUT *StartOfBuffer,
  UINTN,            # IN  BufferSize,
  POINTER(CHAR16)   # IN  CONST *FormatString,
                    # ...
  )

UNICODE_BS_PRINT_ASCII_FORMAT = CFUNCTYPE (
  UINTN,
  POINTER(CHAR16),  # OUT *StartOfBuffer,
  UINTN,            # IN  BufferSize,
  POINTER(CHAR8),   # IN  CONST *FormatString,
  BASE_LIST         # IN  Marker
  )

UNICODE_S_PRINT_ASCII_FORMAT = CFUNCTYPE (
  UINTN,
  POINTER(CHAR16),  # OUT *StartOfBuffer,
  UINTN,            # IN  BufferSize,
  POINTER(CHAR8),   # IN  CONST *FormatString,
                    # ...
  )

UNICODE_VALUE_TO_STRING = CFUNCTYPE (
  UINTN,
  POINTER(CHAR16),  # IN OUT *Buffer,
  UINTN,            # IN Flags,
  INT64,            # IN Value,
  UINTN             # IN Width
  )

ASCII_BS_PRINT = CFUNCTYPE (
  UINTN,
  POINTER(CHAR8), #   OUT       *StartOfBuffer,
  UINTN,          #   IN        BufferSize,
  POINTER(CHAR8), #   IN  CONST *FormatString,
  BASE_LIST       #   IN        Marker
  )

ASCII_S_PRINT = CFUNCTYPE (
  UINTN,
  POINTER(CHAR8), #   OUT       *StartOfBuffer,
  UINTN,          #   IN        BufferSize,
  POINTER(CHAR8), #   IN  CONST *FormatString,
                  #   ...
  )

ASCII_BS_PRINT_UNICODE_FORMAT = CFUNCTYPE (
  UINTN,
  POINTER(CHAR8),   #   OUT        *StartOfBuffer,
  UINTN,            #   IN         BufferSize,
  POINTER(CHAR16),  #   IN  CONST  *FormatString,
  BASE_LIST         #   IN         Marker
  )

ASCII_S_PRINT_UNICODE_FORMAT = CFUNCTYPE (
  UINTN,
  POINTER(CHAR8),   #   OUT        *StartOfBuffer,
  UINTN,            #   IN         BufferSize,
  POINTER(CHAR16),  #   IN  CONST  *FormatString,
                    #   ...
  )

ASCII_VALUE_TO_STRING = CFUNCTYPE (
  UINTN,
  POINTER(CHAR8), # OUT *Buffer,
  UINTN,          # IN  Flags,
  INT64,          # IN  Value,
  UINTN           # IN  Width
  )

EFI_PRINT2_PROTOCOL._fields_ = [
  ("UnicodeBSPrint",              UNICODE_BS_PRINT),
  ("UnicodeSPrint",               UNICODE_S_PRINT),
  ("UnicodeBSPrintAsciiFormat",   UNICODE_BS_PRINT_ASCII_FORMAT),
  ("UnicodeSPrintAsciiFormat",    UNICODE_S_PRINT_ASCII_FORMAT),
  ("UnicodeValueToString",        UNICODE_VALUE_TO_STRING),
  ("AsciiBSPrint",                ASCII_BS_PRINT),
  ("AsciiSPrint",                 ASCII_S_PRINT),
  ("AsciiBSPrintUnicodeFormat",   ASCII_BS_PRINT_UNICODE_FORMAT),
  ("AsciiSPrintUnicodeFormat",    ASCII_S_PRINT_UNICODE_FORMAT),
  ("AsciiValueToString",          ASCII_VALUE_TO_STRING)
  ]

