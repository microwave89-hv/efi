#
# SmmVariableCommon.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# SmmVariableCommon.py is free software: you can redistribute it and/or
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
from EfiPy.MdeModulePkg.Protocol.VarCheck import VAR_CHECK_VARIABLE_PROPERTY
from EfiPy.MdePkg.Uefi.UefiAcpiDataTable import EFI_SMM_COMMUNICATE_HEADER

gSmmVariableWriteGuid         = \
  EFI_GUID (0x93ba1826, 0xdffb, 0x45dd, (0x82, 0xa7, 0xe7, 0xdc, 0xaa, 0x3b, 0xbd, 0xf3))

class SMM_VARIABLE_COMMUNICATE_HEADER (Structure):
  _fields_ = [
  ("Function",      UINTN),
  ("ReturnStatus",  EFI_STATUS),
  ("Data",          UINT8 * 1)
  ]

SMM_VARIABLE_FUNCTION_GET_VARIABLE            = 1
SMM_VARIABLE_FUNCTION_GET_NEXT_VARIABLE_NAME  = 2
SMM_VARIABLE_FUNCTION_SET_VARIABLE            = 3
SMM_VARIABLE_FUNCTION_QUERY_VARIABLE_INFO     = 4
SMM_VARIABLE_FUNCTION_READY_TO_BOOT           = 5
SMM_VARIABLE_FUNCTION_EXIT_BOOT_SERVICE       = 6
SMM_VARIABLE_FUNCTION_GET_STATISTICS          = 7
SMM_VARIABLE_FUNCTION_LOCK_VARIABLE           = 8
SMM_VARIABLE_FUNCTION_VAR_CHECK_VARIABLE_PROPERTY_SET  = 9
SMM_VARIABLE_FUNCTION_VAR_CHECK_VARIABLE_PROPERTY_GET  = 10
SMM_VARIABLE_FUNCTION_GET_PAYLOAD_SIZE        = 11
SMM_COMMUNICATE_HEADER_SIZE  = EFI_SMM_COMMUNICATE_HEADER.Data.offset
SMM_VARIABLE_COMMUNICATE_HEADER_SIZE = SMM_VARIABLE_COMMUNICATE_HEADER.Data.offset

class SMM_VARIABLE_COMMUNICATE_ACCESS_VARIABLE (Structure):
  _fields_ = [
  ("Guid",        EFI_GUID),
  ("DataSize",    UINTN),
  ("NameSize",    UINTN),
  ("Attributes",  UINT32),
  ("Name",        CHAR16 * 1)
  ]

class SMM_VARIABLE_COMMUNICATE_GET_NEXT_VARIABLE_NAME (Structure):
  _fields_ = [
  ("Guid",        EFI_GUID),
  ("NameSize",    UINTN),
  ("Name",        CHAR16 * 1)
  ]

class SMM_VARIABLE_COMMUNICATE_QUERY_VARIABLE_INFO (Structure):
  _fields_ = [
  ("MaximumVariableStorageSize",    UINT64),
  ("RemainingVariableStorageSize",  UINT64),
  ("MaximumVariableSize",           UINT64),
  ("Attributes",                    UINT32)
  ]

SMM_VARIABLE_COMMUNICATE_LOCK_VARIABLE = SMM_VARIABLE_COMMUNICATE_GET_NEXT_VARIABLE_NAME
class SMM_VARIABLE_COMMUNICATE_VAR_CHECK_VARIABLE_PROPERTY (Structure):
  _fields_ = [
  ("Guid",              EFI_GUID),
  ("NameSize",          UINTN),
  ("VariableProperty",  VAR_CHECK_VARIABLE_PROPERTY),
  ("Name",              CHAR16 * 1)
  ]

class SMM_VARIABLE_COMMUNICATE_GET_PAYLOAD_SIZE (Structure):
  _fields_ = [
  ("VariablePayloadSize",  UINTN)
  ]

