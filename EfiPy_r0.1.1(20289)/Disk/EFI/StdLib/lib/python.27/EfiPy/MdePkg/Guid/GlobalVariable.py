#
# GlobalVariable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# GlobalVariable.py is free software: you can redistribute it and/or
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

gEfiGlobalVariableGuid  = EFI_GUID( 0x8BE4DF61, 0x93CA, 0x11d2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C))
EFI_GLOBAL_VARIABLE     = gEfiGlobalVariableGuid

EFI_LANG_CODES_VARIABLE_NAME                = u"LangCodes"
EFI_LANG_VARIABLE_NAME                      = u"Lang"
EFI_TIME_OUT_VARIABLE_NAME                  = u"Timeout"
EFI_PLATFORM_LANG_CODES_VARIABLE_NAME       = u"PlatformLangCodes"
EFI_PLATFORM_LANG_VARIABLE_NAME             = u"PlatformLang"
EFI_CON_IN_VARIABLE_NAME                    = u"ConIn"
EFI_CON_OUT_VARIABLE_NAME                   = u"ConOut"
EFI_ERR_OUT_VARIABLE_NAME                   = u"ErrOut"
EFI_CON_IN_DEV_VARIABLE_NAME                = u"ConInDev"
EFI_CON_OUT_DEV_VARIABLE_NAME               = u"ConOutDev"
EFI_ERR_OUT_DEV_VARIABLE_NAME               = u"ErrOutDev"
EFI_BOOT_ORDER_VARIABLE_NAME                = u"BootOrder"
EFI_BOOT_NEXT_VARIABLE_NAME                 = u"BootNext"
EFI_BOOT_CURRENT_VARIABLE_NAME              = u"BootCurrent"
EFI_BOOT_OPTION_SUPPORT_VARIABLE_NAME       = u"BootOptionSupport"

EFI_DRIVER_ORDER_VARIABLE_NAME              = u"DriverOrder"
EFI_SYS_PREP_ORDER_VARIABLE_NAME            = u"SysPrepOrder"
EFI_HW_ERR_REC_SUPPORT_VARIABLE_NAME        = u"HwErrRecSupport"
EFI_SETUP_MODE_NAME                         = u"SetupMode"
EFI_KEY_EXCHANGE_KEY_NAME                   = u"KEK"
EFI_PLATFORM_KEY_NAME                       = u"PK"
EFI_SIGNATURE_SUPPORT_NAME                  = u"SignatureSupport"
EFI_SECURE_BOOT_MODE_NAME                   = u"SecureBoot"
EFI_KEK_DEFAULT_VARIABLE_NAME               = u"KEKDefault"
EFI_PK_DEFAULT_VARIABLE_NAME                = u"PKDefault"
EFI_DB_DEFAULT_VARIABLE_NAME                = u"dbDefault"
EFI_DBX_DEFAULT_VARIABLE_NAME               = u"dbxDefault"
EFI_DBT_DEFAULT_VARIABLE_NAME               = u"dbtDefault"
EFI_OS_INDICATIONS_SUPPORT_VARIABLE_NAME    = u"OsIndicationsSupported"
EFI_OS_INDICATIONS_VARIABLE_NAME            = u"OsIndications"
EFI_VENDOR_KEYS_VARIABLE_NAME               = u"VendorKeys"
