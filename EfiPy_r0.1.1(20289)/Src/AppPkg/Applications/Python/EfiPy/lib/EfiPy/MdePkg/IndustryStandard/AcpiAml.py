#
# AcpiAml.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# AcpiAml.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard import *

AML_ZERO_OP                  = 0x00
AML_ONE_OP                   = 0x01
AML_ALIAS_OP                 = 0x06
AML_NAME_OP                  = 0x08
AML_BYTE_PREFIX              = 0x0a
AML_WORD_PREFIX              = 0x0b
AML_DWORD_PREFIX             = 0x0c
AML_STRING_PREFIX            = 0x0d
AML_QWORD_PREFIX             = 0x0e
AML_SCOPE_OP                 = 0x10
AML_BUFFER_OP                = 0x11
AML_PACKAGE_OP               = 0x12
AML_VAR_PACKAGE_OP           = 0x13
AML_METHOD_OP                = 0x14
AML_DUAL_NAME_PREFIX         = 0x2e
AML_MULTI_NAME_PREFIX        = 0x2f
AML_NAME_CHAR_A              = 0x41
AML_NAME_CHAR_B              = 0x42
AML_NAME_CHAR_C              = 0x43
AML_NAME_CHAR_D              = 0x44
AML_NAME_CHAR_E              = 0x45
AML_NAME_CHAR_F              = 0x46
AML_NAME_CHAR_G              = 0x47
AML_NAME_CHAR_H              = 0x48
AML_NAME_CHAR_I              = 0x49
AML_NAME_CHAR_J              = 0x4a
AML_NAME_CHAR_K              = 0x4b
AML_NAME_CHAR_L              = 0x4c
AML_NAME_CHAR_M              = 0x4d
AML_NAME_CHAR_N              = 0x4e
AML_NAME_CHAR_O              = 0x4f
AML_NAME_CHAR_P              = 0x50
AML_NAME_CHAR_Q              = 0x51
AML_NAME_CHAR_R              = 0x52
AML_NAME_CHAR_S              = 0x53
AML_NAME_CHAR_T              = 0x54
AML_NAME_CHAR_U              = 0x55
AML_NAME_CHAR_V              = 0x56
AML_NAME_CHAR_W              = 0x57
AML_NAME_CHAR_X              = 0x58
AML_NAME_CHAR_Y              = 0x59
AML_NAME_CHAR_Z              = 0x5a
AML_ROOT_CHAR                = 0x5c
AML_PARENT_PREFIX_CHAR       = 0x5e
AML_NAME_CHAR__              = 0x5f
AML_LOCAL0                   = 0x60
AML_LOCAL1                   = 0x61
AML_LOCAL2                   = 0x62
AML_LOCAL3                   = 0x63
AML_LOCAL4                   = 0x64
AML_LOCAL5                   = 0x65
AML_LOCAL6                   = 0x66
AML_LOCAL7                   = 0x67
AML_ARG0                     = 0x68
AML_ARG1                     = 0x69
AML_ARG2                     = 0x6a
AML_ARG3                     = 0x6b
AML_ARG4                     = 0x6c
AML_ARG5                     = 0x6d
AML_ARG6                     = 0x6e
AML_STORE_OP                 = 0x70
AML_REF_OF_OP                = 0x71
AML_ADD_OP                   = 0x72
AML_CONCAT_OP                = 0x73
AML_SUBTRACT_OP              = 0x74
AML_INCREMENT_OP             = 0x75
AML_DECREMENT_OP             = 0x76
AML_MULTIPLY_OP              = 0x77
AML_DIVIDE_OP                = 0x78
AML_SHIFT_LEFT_OP            = 0x79
AML_SHIFT_RIGHT_OP           = 0x7a
AML_AND_OP                   = 0x7b
AML_NAND_OP                  = 0x7c
AML_OR_OP                    = 0x7d
AML_NOR_OP                   = 0x7e
AML_XOR_OP                   = 0x7f
AML_NOT_OP                   = 0x80
AML_FIND_SET_LEFT_BIT_OP     = 0x81
AML_FIND_SET_RIGHT_BIT_OP    = 0x82
AML_DEREF_OF_OP              = 0x83
AML_CONCAT_RES_OP            = 0x84
AML_MOD_OP                   = 0x85
AML_NOTIFY_OP                = 0x86
AML_SIZE_OF_OP               = 0x87
AML_INDEX_OP                 = 0x88
AML_MATCH_OP                 = 0x89
AML_CREATE_DWORD_FIELD_OP    = 0x8a
AML_CREATE_WORD_FIELD_OP     = 0x8b
AML_CREATE_BYTE_FIELD_OP     = 0x8c
AML_CREATE_BIT_FIELD_OP      = 0x8d
AML_OBJECT_TYPE_OP           = 0x8e
AML_CREATE_QWORD_FIELD_OP    = 0x8f
AML_LAND_OP                  = 0x90
AML_LOR_OP                   = 0x91
AML_LNOT_OP                  = 0x92
AML_LEQUAL_OP                = 0x93
AML_LGREATER_OP              = 0x94
AML_LLESS_OP                 = 0x95
AML_TO_BUFFER_OP             = 0x96
AML_TO_DEC_STRING_OP         = 0x97
AML_TO_HEX_STRING_OP         = 0x98
AML_TO_INTEGER_OP            = 0x99
AML_TO_STRING_OP             = 0x9c
AML_COPY_OBJECT_OP           = 0x9d
AML_MID_OP                   = 0x9e
AML_CONTINUE_OP              = 0x9f
AML_IF_OP                    = 0xa0
AML_ELSE_OP                  = 0xa1
AML_WHILE_OP                 = 0xa2
AML_NOOP_OP                  = 0xa3
AML_RETURN_OP                = 0xa4
AML_BREAK_OP                 = 0xa5
AML_BREAK_POINT_OP           = 0xcc
AML_ONES_OP                  = 0xff

AML_EXT_OP                   = 0x5b

AML_EXT_MUTEX_OP             = 0x01
AML_EXT_EVENT_OP             = 0x02
AML_EXT_COND_REF_OF_OP       = 0x12
AML_EXT_CREATE_FIELD_OP      = 0x13
AML_EXT_LOAD_TABLE_OP        = 0x1f
AML_EXT_LOAD_OP              = 0x20
AML_EXT_STALL_OP             = 0x21
AML_EXT_SLEEP_OP             = 0x22
AML_EXT_ACQUIRE_OP           = 0x23
AML_EXT_SIGNAL_OP            = 0x24
AML_EXT_WAIT_OP              = 0x25
AML_EXT_RESET_OP             = 0x26
AML_EXT_RELEASE_OP           = 0x27
AML_EXT_FROM_BCD_OP          = 0x28
AML_EXT_TO_BCD_OP            = 0x29
AML_EXT_UNLOAD_OP            = 0x2a
AML_EXT_REVISION_OP          = 0x30
AML_EXT_DEBUG_OP             = 0x31
AML_EXT_FATAL_OP             = 0x32
AML_EXT_TIMER_OP             = 0x33
AML_EXT_REGION_OP            = 0x80
AML_EXT_FIELD_OP             = 0x81
AML_EXT_DEVICE_OP            = 0x82
AML_EXT_PROCESSOR_OP         = 0x83
AML_EXT_POWER_RES_OP         = 0x84
AML_EXT_THERMAL_ZONE_OP      = 0x85
AML_EXT_INDEX_FIELD_OP       = 0x86
AML_EXT_BANK_FIELD_OP        = 0x87
AML_EXT_DATA_REGION_OP       = 0x88

