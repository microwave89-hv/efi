#
# HiiConfigKeyword.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# HiiConfigKeyword.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import \
      EFI_STRING

gEfiConfigKeywordHandlerProtocolGuid    = \
  EFI_GUID (0x0a8badd5, 0x03b8, 0x4d19, (0xb1, 0x28, 0x7b, 0x8f, 0x0e, 0xda, 0xa5, 0x96 ))

KEYWORD_HANDLER_NO_ERROR                       = 0x00000000
KEYWORD_HANDLER_NAMESPACE_ID_NOT_FOUND         = 0x00000001
KEYWORD_HANDLER_MALFORMED_STRING               = 0x00000002
KEYWORD_HANDLER_KEYWORD_NOT_FOUND              = 0x00000004
KEYWORD_HANDLER_INCOMPATIBLE_VALUE_DETECTED    = 0x00000008
KEYWORD_HANDLER_ACCESS_NOT_PERMITTED           = 0x00000010
KEYWORD_HANDLER_UNDEFINED_PROCESSING_ERROR     = 0x80000000

class EFI_CONFIG_KEYWORD_HANDLER_PROTOCOL (Structure):
  pass

EFI_CONFIG_KEYWORD_HANDLER_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CONFIG_KEYWORD_HANDLER_PROTOCOL), # IN       *This
  EFI_STRING,                                   # IN CONST KeywordString,
  POINTER(EFI_STRING),                          # OUT      *Progress,
  POINTER(UINT32)                               # OUT      *ProgressErr
  )

EFI_CONFIG_KEYWORD_HANDLER_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CONFIG_KEYWORD_HANDLER_PROTOCOL), # IN       *This
  EFI_STRING,                                   # IN CONST NameSpaceId, OPTIONAL
  EFI_STRING,                                   # IN CONST KeywordString, OPTIONAL
  POINTER(EFI_STRING),                          # OUT      *Progress, 
  POINTER(UINT32),                              # OUT      *ProgressErr,
  POINTER(EFI_STRING)                           # OUT      *Results
  )

EFI_CONFIG_KEYWORD_HANDLER_PROTOCOL._fields_ = [
  ("SetData", EFI_CONFIG_KEYWORD_HANDLER_SET_DATA),
  ("GetData", EFI_CONFIG_KEYWORD_HANDLER_GET_DATA)
  ]

