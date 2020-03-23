#
# EbcSimpleDebugger.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# EbcSimpleDebugger.py is free software: you can redistribute it and/or
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
from EfiPy.MdeModulePkg.Protocol.EbcVmTest import VM_CONTEXT
from EfiPy.MdePkg.Protocol.DebugSupport import EFI_EXCEPTION_TYPE

gEfiEbcSimpleDebuggerProtocolGuid = \
  EFI_GUID (0x2a72d11e, 0x7376, 0x40f6, (0x9c, 0x68, 0x23, 0xfa, 0x2f, 0xe3, 0x63, 0xf1))

class EFI_EBC_SIMPLE_DEBUGGER_PROTOCOL (Structure):
  pass

EBC_DEBUGGER_SIGNAL_EXCEPTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_SIMPLE_DEBUGGER_PROTOCOL),  # IN *This,
  POINTER(VM_CONTEXT),                        # IN *VmPtr,
  EFI_EXCEPTION_TYPE,                         # IN ExceptionType
  )

EBC_DEBUGGER_DEBUG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_SIMPLE_DEBUGGER_PROTOCOL),  # IN *This,
  POINTER(VM_CONTEXT)                         # IN *VmPtr
  )

EBC_DEBUGGER_DASM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_SIMPLE_DEBUGGER_PROTOCOL),  # IN *This,
  POINTER(VM_CONTEXT),                        # IN *VmPtr
  POINTER(UINT16),                            # IN *DasmString OPTIONAL,
  UINT32                                      # IN DasmStringSize
  )                                           

EBC_DEBUGGER_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_SIMPLE_DEBUGGER_PROTOCOL), # IN *This,
  UINT32,                                    # IN ConfigId,
  UINTN                                      # IN ConfigValue
  )                                           

EFI_EBC_SIMPLE_DEBUGGER_PROTOCOL._fields_ = [
  ("Debugger",        EBC_DEBUGGER_DEBUG),
  ("SignalException", EBC_DEBUGGER_SIGNAL_EXCEPTION),
  ("Dasm",            EBC_DEBUGGER_DASM),
  ("Configure",       EBC_DEBUGGER_CONFIGURE)
  ]

