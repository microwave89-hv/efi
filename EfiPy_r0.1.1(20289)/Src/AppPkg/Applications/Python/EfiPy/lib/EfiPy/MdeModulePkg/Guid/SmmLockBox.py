#
# SmmLockBox.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# SmmLockBox.py is free software: you can redistribute it and/or
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

gEfiSmmLockBoxCommunicationGuid         = \
  EFI_GUID (0x2a3cfebd, 0x27e8, 0x4d0a, (0x8b, 0x79, 0xd6, 0x88, 0xc2, 0xa3, 0xe1, 0xc0))

EFI_SMM_LOCK_BOX_COMMAND_SAVE                 = 0x1
EFI_SMM_LOCK_BOX_COMMAND_UPDATE               = 0x2
EFI_SMM_LOCK_BOX_COMMAND_RESTORE              = 0x3
EFI_SMM_LOCK_BOX_COMMAND_SET_ATTRIBUTES       = 0x4
EFI_SMM_LOCK_BOX_COMMAND_RESTORE_ALL_IN_PLACE = 0x5

class EFI_SMM_LOCK_BOX_PARAMETER_HEADER (Structure):
  _fields_ = [
  ("Command",       UINT32),
  ("DataLength",    UINT32),
  ("ReturnStatus",  UINT64)
  ]

class EFI_SMM_LOCK_BOX_PARAMETER_SAVE (Structure):
  _fields_ = [
  ("Header",  EFI_SMM_LOCK_BOX_PARAMETER_HEADER),
  ("Guid",    GUID),
  ("Buffer",  PHYSICAL_ADDRESS),
  ("Length",  UINT64)
  ]

class EFI_SMM_LOCK_BOX_PARAMETER_UPDATE (Structure):
  _fields_ = [
  ("Header", EFI_SMM_LOCK_BOX_PARAMETER_HEADER),
  ("Guid",   GUID),
  ("Offset", UINT64),
  ("Buffer", PHYSICAL_ADDRESS),
  ("Length", UINT64)
  ]

class EFI_SMM_LOCK_BOX_PARAMETER_RESTORE (Structure):
  _fields_ = [
  ("Header",  EFI_SMM_LOCK_BOX_PARAMETER_HEADER),
  ("Guid",    GUID),
  ("Buffer",  PHYSICAL_ADDRESS),
  ("Length",  UINT64)
  ]

class EFI_SMM_LOCK_BOX_PARAMETER_SET_ATTRIBUTES (Structure):
  _fields_ = [
  ("Header",      EFI_SMM_LOCK_BOX_PARAMETER_HEADER),
  ("Guid",        GUID),
  ("Attributes",  UINT64)
  ]

class EFI_SMM_LOCK_BOX_PARAMETER_RESTORE_ALL_IN_PLACE (Structure):
  _fields_ = [
  ("Header",      EFI_SMM_LOCK_BOX_PARAMETER_HEADER)
  ]

