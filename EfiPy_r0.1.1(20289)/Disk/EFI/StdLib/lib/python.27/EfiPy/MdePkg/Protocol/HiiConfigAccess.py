#
# HiiConfigAccess.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# HiiConfigAccess.py is free software: you can redistribute it and/or
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

import FormBrowser2

from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import \
      EFI_STRING,       \
      EFI_QUESTION_ID,  \
      EFI_IFR_TYPE_VALUE


gEfiHiiConfigAccessProtocolGuid = \
  EFI_GUID (0x330d4706, 0xf2a0, 0x4e4f, ( 0xa3, 0x69, 0xb6, 0x6f, 0xa8, 0xd5, 0x43, 0x85 ))

class EFI_HII_CONFIG_ACCESS_PROTOCOL (Structure):
  pass

EFI_BROWSER_ACTION  = UINTN
EFI_BROWSER_ACTION_CHANGING   = 0
EFI_BROWSER_ACTION_CHANGED    = 1
EFI_BROWSER_ACTION_RETRIEVE   = 2
EFI_BROWSER_ACTION_FORM_OPEN  = 3
EFI_BROWSER_ACTION_FORM_CLOSE = 4
EFI_BROWSER_ACTION_DEFAULT_STANDARD      = 0x1000
EFI_BROWSER_ACTION_DEFAULT_MANUFACTURING = 0x1001
EFI_BROWSER_ACTION_DEFAULT_SAFE          = 0x1002
EFI_BROWSER_ACTION_DEFAULT_PLATFORM      = 0x2000
EFI_BROWSER_ACTION_DEFAULT_HARDWARE      = 0x3000
EFI_BROWSER_ACTION_DEFAULT_FIRMWARE      = 0x4000

EFI_HII_ACCESS_EXTRACT_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ACCESS_PROTOCOL),  # IN        *This
  EFI_STRING,                               # IN CONST  Request,
  POINTER(EFI_STRING),                      # OUT       *Progress,
  POINTER(EFI_STRING)                       # OUT       *Results
  )

EFI_HII_ACCESS_ROUTE_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ACCESS_PROTOCOL),  # IN        *This
  EFI_STRING,                               # IN CONST  Configuration,
  POINTER(EFI_STRING)                       # OUT       *Progress
  )

EFI_HII_ACCESS_FORM_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ACCESS_PROTOCOL),          # IN     *This
  EFI_BROWSER_ACTION,                               # IN     Action,
  EFI_QUESTION_ID,                                  # IN     QuestionId,
  UINT8,                                            # IN     Type,
  POINTER(EFI_IFR_TYPE_VALUE),                      # IN OUT *Value,
  POINTER(FormBrowser2.EFI_BROWSER_ACTION_REQUEST)  # OUT    *ActionRequest
  )

EFI_HII_CONFIG_ACCESS_PROTOCOL._fields_ = [
  ("ExtractConfig", EFI_HII_ACCESS_EXTRACT_CONFIG),
  ("RouteConfig",   EFI_HII_ACCESS_ROUTE_CONFIG),
  ("Callback",      EFI_HII_ACCESS_FORM_CALLBACK)
  ]

