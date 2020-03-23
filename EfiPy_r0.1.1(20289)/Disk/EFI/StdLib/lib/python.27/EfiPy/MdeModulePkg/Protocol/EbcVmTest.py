#
# EbcVmTest.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# EbcVmTest.py is free software: you can redistribute it and/or
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

gEfiEbcVmTestProtocolGuid = \
  EFI_GUID (0xAAEACCFD, 0xF27B, 0x4C17, (0xB6, 0x10, 0x75, 0xCA, 0x1F, 0x2D, 0xFB, 0x52))

class EFI_EBC_VM_TEST_PROTOCOL (Structure):
  pass

VMIP  = POINTER(UINT8)

VM_REGISTER     = INT64
EXCEPTION_FLAGS = UINT32

class VM_CONTEXT (Structure):
  _fields_ = [
  ("Gpr",                     VM_REGISTER * 8),
  ("Flags",                   UINT64),
  ("Ip",                      VMIP),
  ("LastException",           UINTN),
  ("ExceptionFlags",          EXCEPTION_FLAGS),
  ("StopFlags",               UINT32),
  ("CompilerVersion",         UINT32),
  ("HighStackBottom",         UINTN),
  ("LowStackTop",             UINTN),
  ("StackRetAddr",            UINT64),
  ("*StackMagicPtr",          UINTN),
  ("ImageHandle",             EFI_HANDLE),
  ("*SystemTable",            EFI_SYSTEM_TABLE),
  ("LastAddrConverted",       UINTN),
  ("LastAddrConvertedValue",  UINTN),
  ("FramePtr",                PVOID),
  ("EntryPoint",              PVOID),
  ("ImageBase",               UINTN),
  ("StackPool",               PVOID),
  ("StackTop",                PVOID)
  ]

EBC_VM_TEST_EXECUTE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_VM_TEST_PROTOCOL),    # IN      *This,
  VM_CONTEXT,                           # IN      *VmPtr,
  UINTN                                 # IN OUT  *InstructionCount
  )

EBC_VM_TEST_ASM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_VM_TEST_PROTOCOL),    # IN      *This,
  POINTER(CHAR16),                      # IN      *AsmText,
  POINTER(INT8),                        # IN OUT  *Buffer,
  POINTER(UINTN)                        # IN OUT  *BufferLen
  )

EBC_VM_TEST_DASM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_VM_TEST_PROTOCOL),    # IN     *This,
  POINTER(CHAR16),                      # IN OUT *AsmText,
  POINTER(INT8),                        # IN OUT *Buffer,
  POINTER(UINTN)                        # IN OUT *Len
  )

EFI_EBC_VM_TEST_PROTOCOL._fields_ = [
  ("Execute",     EBC_VM_TEST_EXECUTE),
  ("Assemble",    EBC_VM_TEST_ASM),
  ("Disassemble", EBC_VM_TEST_DASM)
  ]
