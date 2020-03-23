#
# BaseLib.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# BaseLib.py is free software: you can redistribute it and/or
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

class IA32_FLAGS16_Bits (Structure):
  _fields_ = [
  ("CF",            UINT32, 1),
  ("Reserved_0",    UINT32, 1),
  ("PF",            UINT32, 1),
  ("Reserved_1",    UINT32, 1),
  ("AF",            UINT32, 1),
  ("Reserved_2",    UINT32, 1),
  ("ZF",            UINT32, 1),
  ("SF",            UINT32, 1),
  ("TF",            UINT32, 1),
  ("IF",            UINT32, 1),
  ("DF",            UINT32, 1),
  ("OF",            UINT32, 1),
  ("IOPL",          UINT32, 2),
  ("NT",            UINT32, 1),
  ("Reserved_3",    UINT32, 1)
  ]

class IA32_FLAGS16 (Union):
  _fields_ = [
  ("Bits",      IA32_FLAGS16_Bits),
  ("Uint16",    UINT16)
  ]

class IA32_EFLAGS32_Bits (Structure):
  _fields_ = [
  ("CF",            UINT32, 1),
  ("Reserved_0",    UINT32, 1),
  ("PF",            UINT32, 1),
  ("Reserved_1",    UINT32, 1),
  ("AF",            UINT32, 1),
  ("Reserved_2",    UINT32, 1),
  ("ZF",            UINT32, 1),
  ("SF",            UINT32, 1),
  ("TF",            UINT32, 1),
  ("IF",            UINT32, 1),
  ("DF",            UINT32, 1),
  ("OF",            UINT32, 1),
  ("IOPL",          UINT32, 2),
  ("NT",            UINT32, 1),
  ("Reserved_3",    UINT32, 1),
  ("RF",            UINT32, 1),
  ("VM",            UINT32, 1),
  ("AC",            UINT32, 1),
  ("VIF",           UINT32, 1),
  ("VIP",           UINT32, 1),
  ("ID",            UINT32, 1),
  ("Reserved_4",    UINT32, 10)
  ]

class IA32_EFLAGS32 (Union):
  _fields_ = [
  ("Bits",      IA32_EFLAGS32_Bits),
  ("UintN",     UINTN)
  ]

class IA32_CR0_Bits (Structure):
  _fields_ = [
  ("PE",            UINT32, 1),
  ("MP",            UINT32, 1),
  ("EM",            UINT32, 1),
  ("TS",            UINT32, 1),
  ("ET",            UINT32, 1),
  ("NE",            UINT32, 1),
  ("Reserved_0",    UINT32, 10),
  ("WP",            UINT32, 1),
  ("Reserved_1",    UINT32, 1),
  ("AM",            UINT32, 1),
  ("Reserved_2",    UINT32, 10),
  ("NW",            UINT32, 1),
  ("CD",            UINT32, 1),
  ("PG",            UINT32, 1)
  ]

class IA32_CR0 (Union):
  _fields_ = [
  ("Bits",      IA32_CR0_Bits),
  ("UintN",     UINTN)
  ]

class IA32_CR4_Bits (Structure):
  _fields_ = [
  ("VME",             UINT32, 1),
  ("PVI",             UINT32, 1),
  ("TSD",             UINT32, 1),
  ("DE",              UINT32, 1),
  ("PSE",             UINT32, 1),
  ("PAE",             UINT32, 1),
  ("MCE",             UINT32, 1),
  ("PGE",             UINT32, 1),
  ("PCE",             UINT32, 1),
  ("OSFXSR",          UINT32, 1),
  ("OSXMMEXCPT",      UINT32, 1),
  ("Reserved_0",      UINT32, 2),
  ("VMXE",            UINT32, 1),
  ("Reserved_1",      UINT32, 18)
  ]

class IA32_CR4 (Union):
  _fields_ = [
  ("Bits",      IA32_CR4_Bits),
  ("UintN",     UINTN)
  ]

class IA32_SEGMENT_DESCRIPTOR_Bits (Structure):
  _fields_ = [
  ("VME",           UINT32, 1),
  ("PVI",           UINT32, 1),
  ("TSD",           UINT32, 1),
  ("DE",            UINT32, 1),
  ("PSE",           UINT32, 1),
  ("PAE",           UINT32, 1),
  ("MCE",           UINT32, 1),
  ("PGE",           UINT32, 1),
  ("PCE",           UINT32, 1),
  ("OSFXSR",        UINT32, 1),
  ("OSXMMEXCPT",    UINT32, 1),
  ("Reserved_0",    UINT32, 2),
  ("VMXE",          UINT32, 1),
  ("Reserved_1",    UINT32, 18)
  ]

class IA32_SEGMENT_DESCRIPTOR (Union):
  _fields_ = [
  ("Bits",      IA32_SEGMENT_DESCRIPTOR_Bits),
  ("Uint64",    UINT64)
  ]

class IA32_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
  ("Limit",         UINT16),
  ("Base",          UINTN)
  ]

IA32_IDT_GATE_TYPE_TASK          = 0x85
IA32_IDT_GATE_TYPE_INTERRUPT_16  = 0x86
IA32_IDT_GATE_TYPE_TRAP_16       = 0x87
IA32_IDT_GATE_TYPE_INTERRUPT_32  = 0x8E
IA32_IDT_GATE_TYPE_TRAP_32       = 0x8F

if EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_IA32:
  class IA32_IDT_GATE_DESCRIPTOR_Bits (Structure):
    _fields_ = [
    ("OffsetLow",   UINT32, 16),
    ("Selector",    UINT32, 16),
    ("Reserved_0",  UINT32, 8),
    ("GateType",    UINT32, 8),
    ("OffsetHigh",  UINT32, 16)
    ]

  class IA32_IDT_GATE_DESCRIPTOR (Union):
    _fields_ = [
    ("Bits",      IA32_IDT_GATE_DESCRIPTOR_Bits),
    ("Uint64",    UINT64)
    ]

if EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_X64:
  class IA32_IDT_GATE_DESCRIPTOR_Bits (Structure):
    _fields_ = [
    ("OffsetLow",   UINT32, 16),
    ("Selector",    UINT32, 16),
    ("Reserved_0",  UINT32, 8),
    ("GateType",    UINT32, 8),
    ("OffsetHigh",  UINT32, 16),
    ("OffsetUpper", UINT32, 32),
    ("Reserved_1",  UINT32, 32)
    ]

  class IA32_IDT_GATE_DESCRIPTOR (Union):
    _fields_ = [
    ("Bits",      IA32_IDT_GATE_DESCRIPTOR_Bits),
    ("Uint64",    UINT64),
    ("Uint64_1",  UINT64)
    ]

class IA32_FX_BUFFER (Structure):
  _fields_ = [
  ("Buffer",   UINT8 * 512)
  ]

class IA32_BYTE_REGS (Structure):
  _fields_ = [
  ("Reserved1", UINT32),
  ("Reserved2", UINT32),
  ("Reserved3", UINT32),
  ("Reserved4", UINT32),
  ("BL",        UINT8),
  ("BH",        UINT8),
  ("Reserved5", UINT16),
  ("DL",        UINT8),
  ("DH",        UINT8),
  ("Reserved6", UINT16),
  ("CL",        UINT8),
  ("CH",        UINT8),
  ("Reserved7", UINT16),
  ("AL",        UINT8),
  ("AH",        UINT8),
  ("Reserved8", UINT16)
  ]

class IA32_WORD_REGS (Structure):
  _fields_ = [
  ("DI",        UINT16),
  ("Reserved1", UINT16),
  ("SI",        UINT16),
  ("Reserved2", UINT16),
  ("BP",        UINT16),
  ("Reserved3", UINT16),
  ("SP",        UINT16),
  ("Reserved4", UINT16),
  ("BX",        UINT16),
  ("Reserved5", UINT16),
  ("DX",        UINT16),
  ("Reserved6", UINT16),
  ("CX",        UINT16),
  ("Reserved7", UINT16),
  ("AX",        UINT16),
  ("Reserved8", UINT16)
  ]

class IA32_DWORD_REGS (Structure):
  _fields_ = [
  ("EDI",     UINT32),
  ("ESI",     UINT32),
  ("EBP",     UINT32),
  ("ESP",     UINT32),
  ("EBX",     UINT32),
  ("EDX",     UINT32),
  ("ECX",     UINT32),
  ("EAX",     UINT32),
  ("DS",      UINT16),
  ("ES",      UINT16),
  ("FS",      UINT16),
  ("GS",      UINT16),
  ("EFLAGS",  IA32_EFLAGS32),
  ("Eip",     UINT32),
  ("CS",      UINT16),
  ("SS",      UINT16)
  ]

class IA32_REGISTER_SET (Union):
  _fields_ = [
  ("E",     IA32_DWORD_REGS),
  ("X",     IA32_WORD_REGS),
  ("H",     IA32_BYTE_REGS)
  ]

class THUNK_CONTEXT (Structure):
  _fields_ = [
  ("RealModeState",       POINTER(IA32_REGISTER_SET)),
  ("RealModeBuffer",      PVOID),
  ("RealModeBufferSize",  UINT32),
  ("ThunkAttributes",     UINT32)
  ]

THUNK_ATTRIBUTE_BIG_REAL_MODE             = 0x00000001
THUNK_ATTRIBUTE_DISABLE_A20_MASK_INT_15   = 0x00000002
THUNK_ATTRIBUTE_DISABLE_A20_MASK_KBD_CTRL = 0x00000004

