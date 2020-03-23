#
# FormBrowserEx.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FormBrowserEx.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Protocol.SimpleTextIn import EFI_INPUT_KEY

from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import \
      EFI_STRING,     \
      EFI_HII_HANDLE

gEfiFormBrowserExProtocolGuid = \
  EFI_GUID (0x1f73b18d, 0x4630, 0x43c1, (0xa1, 0xde, 0x6f, 0x80, 0x85, 0x5d, 0x7d, 0xa4))

class EFI_FORM_BROWSER_EXTENSION_PROTOCOL (Structure):
  pass

BROWSER_NO_CHANGES          = 0
BROWSER_SAVE_CHANGES        = 1
BROWSER_DISCARD_CHANGES     = 2
BROWSER_KEEP_CURRENT        = 3

BROWSER_ACTION_UNREGISTER   = 0
BROWSER_ACTION_DISCARD      = BIT0
BROWSER_ACTION_DEFAULT      = BIT1
BROWSER_ACTION_SUBMIT       = BIT2
BROWSER_ACTION_RESET        = BIT3
BROWSER_ACTION_EXIT         = BIT4
BROWSER_ACTION_GOTO         = BIT5

FormLevel     = 1
FormSetLevel  = 2
SystemLevel   = 3
MaxLevel      = 4
BROWSER_SETTING_SCOPE = UINTN

SET_SCOPE = CFUNCTYPE (
  EFI_STATUS,
  BROWSER_SETTING_SCOPE # IN Scope
  )

REGISTER_HOT_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_INPUT_KEY), # IN *KeyData,
  UINT32,                 # IN Action,
  UINT16,                 # IN DefaultId,
  EFI_STRING              # IN HelpString OPTIONAL
  )

EXIT_HANDLER = CFUNCTYPE (
  VOID
  )

REGISTER_EXIT_HANDLER = CFUNCTYPE (
  VOID,
  EXIT_HANDLER  # IN Handler
  )

SAVE_REMINDER = CFUNCTYPE (
  UINT32
  )

EFI_FORM_BROWSER_EXTENSION_PROTOCOL._fields_ = [
  ("SetScope",             SET_SCOPE),
  ("RegisterHotKey",       REGISTER_HOT_KEY),
  ("RegiserExitHandler",   REGISTER_EXIT_HANDLER),
  ("SaveReminder",         SAVE_REMINDER)
  ]

