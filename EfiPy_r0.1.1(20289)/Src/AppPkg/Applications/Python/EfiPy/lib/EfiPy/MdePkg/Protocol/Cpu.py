#
# Cpu.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Cpu.py is free software: you can redistribute it and/or
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

import DebugSupport

gEfiCpuArchProtocolGuid                 = \
  EFI_GUID (0x26baccb1, 0x6f42, 0x11d4, (0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

class EFI_CPU_ARCH_PROTOCOL (Structure):
  pass

EfiCpuFlushTypeWriteBackInvalidate  = 0
EfiCpuFlushTypeWriteBack            = 1
EfiCpuFlushTypeInvalidate           = 2
EfiCpuMaxFlushType                  = 3
EFI_CPU_FLUSH_TYPE                  = ENUM

EfiCpuInit          = 0
EfiCpuMaxInitType   = 1
EFI_CPU_INIT_TYPE   = ENUM

EFI_CPU_INTERRUPT_HANDLER = CFUNCTYPE (
  VOID,
  DebugSupport.EFI_EXCEPTION_TYPE,  # IN CONST  InterruptType
  DebugSupport.EFI_SYSTEM_CONTEXT   # IN CONST  SystemContext
  )

EFI_CPU_FLUSH_DATA_CACHE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_ARCH_PROTOCOL),  # IN *This
  EFI_PHYSICAL_ADDRESS,            # IN Start,
  UINT64,                          # IN Length,
  EFI_CPU_FLUSH_TYPE               # IN FlushType
  )

EFI_CPU_ENABLE_INTERRUPT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_ARCH_PROTOCOL)  # IN *This
  )

EFI_CPU_DISABLE_INTERRUPT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_ARCH_PROTOCOL)  # IN *This
  )

EFI_CPU_GET_INTERRUPT_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_ARCH_PROTOCOL), # IN      *This
  POINTER(BOOLEAN)                #    OUT  *State
  )

EFI_CPU_INIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_ARCH_PROTOCOL), # IN *This
  EFI_CPU_INIT_TYPE               # IN InitType
  )

EFI_CPU_REGISTER_INTERRUPT_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_ARCH_PROTOCOL),   # IN *This,
  DebugSupport.EFI_EXCEPTION_TYPE,  # IN InterruptType,
  EFI_CPU_INTERRUPT_HANDLER         # IN InterruptHandler
  )

EFI_CPU_GET_TIMER_VALUE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_ARCH_PROTOCOL),  # IN   *This,
  UINT32,                          # IN   TimerIndex,
  POINTER (UINT64),                # OUT  *TimerValue,
  POINTER (UINT64)                 # OUT  *TimerPeriod OPTIONAL
  )

EFI_CPU_SET_MEMORY_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CPU_ARCH_PROTOCOL),  # IN   *This,
  EFI_PHYSICAL_ADDRESS,            # IN   BaseAddress,
  UINT64,                          # IN   Length,
  UINT64                           # IN   Attributes
  )

EFI_CPU_ARCH_PROTOCOL._fields_ = [
    ("FlushDataCache",            EFI_CPU_FLUSH_DATA_CACHE),
    ("EnableInterrupt",           EFI_CPU_ENABLE_INTERRUPT),
    ("DisableInterrupt",          EFI_CPU_DISABLE_INTERRUPT),
    ("GetInterruptState",         EFI_CPU_GET_INTERRUPT_STATE),
    ("Init",                      EFI_CPU_INIT),
    ("RegisterInterruptHandler",  EFI_CPU_REGISTER_INTERRUPT_HANDLER),
    ("GetTimerValue",             EFI_CPU_GET_TIMER_VALUE),
    ("SetMemoryAttributes",       EFI_CPU_SET_MEMORY_ATTRIBUTES),
    ("NumberOfTimers",            UINT32),
    ("DmaBufferAlignment",        UINT32)
  ]

