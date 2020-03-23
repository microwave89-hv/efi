#
# PlatformToDriverConfiguration.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PlatformToDriverConfiguration.py is free software: you can redistribute it and/or
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

gEfiPlatformToDriverConfigurationProtocolGuid   = \
  EFI_GUID (0x642cd590, 0x8059, 0x4c0a, ( 0xa9, 0x58, 0xc5, 0xec, 0x7, 0xd2, 0x3c, 0x4b ))

class EFI_PLATFORM_TO_DRIVER_CONFIGURATION_PROTOCOL (Structure):
  pass

EFI_PLATFORM_TO_DRIVER_CONFIGURATION_QUERY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PLATFORM_TO_DRIVER_CONFIGURATION_PROTOCOL), # IN CONST  *This,
  EFI_HANDLE,                                             # IN CONST  ControllerHandle,
  EFI_HANDLE,                                             # IN CONST  ChildHandle OPTIONAL,
  POINTER(UINTN),                                         # IN CONST  *Instance,
  POINTER(POINTER(EFI_GUID)),                             # OUT       **ParameterTypeGuid,
  POINTER(PVOID),                                         # OUT       **ParameterBlock,
  POINTER(UINTN)                                          # OUT       *ParameterBlockSize
  )

EfiPlatformConfigurationActionNone              = 0
EfiPlatformConfigurationActionStopController    = 1
EfiPlatformConfigurationActionRestartController = 2
EfiPlatformConfigurationActionRestartPlatform   = 3
EfiPlatformConfigurationActionNvramFailed       = 4
EfiPlatformConfigurationActionMaximum           = 5
EFI_PLATFORM_CONFIGURATION_ACTION               = ENUM

EFI_PLATFORM_TO_DRIVER_CONFIGURATION_RESPONSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PLATFORM_TO_DRIVER_CONFIGURATION_PROTOCOL), # IN CONST  *This,
  EFI_HANDLE,                                             # IN CONST  ControllerHandle,
  EFI_HANDLE,                                             # IN CONST  ChildHandle OPTIONAL,
  POINTER(UINTN),                                         # IN CONST  *Instance,
  POINTER(EFI_GUID),                                      # IN CONST  *ParameterTypeGuid,
  PVOID,                                                  # IN CONST  *ParameterBlock,
  POINTER(UINTN),                                         # IN CONST  *ParameterBlockSize
  EFI_PLATFORM_CONFIGURATION_ACTION                       # IN CONST  ConfigurationAction
  )

EFI_PLATFORM_TO_DRIVER_CONFIGURATION_PROTOCOL._fields_ = [
  ("Query",    EFI_PLATFORM_TO_DRIVER_CONFIGURATION_QUERY),
  ("Response", EFI_PLATFORM_TO_DRIVER_CONFIGURATION_RESPONSE)
  ]

gEfiPlatformToDriverConfigurationClpGuid        = \
  EFI_GUID (0x345ecc0e, 0xcb6, 0x4b75, ( 0xbb, 0x57, 0x1b, 0x12, 0x9c, 0x47, 0x33,0x3e ))

class EFI_CONFIGURE_CLP_PARAMETER_BLK (Structure):
  _fields_ = [
    ("CLPCommand",            PCHAR8),
    ("CLPCommandLength",      UINT32),
    ("CLPReturnString",       PCHAR8),
    ("CLPReturnStringLength", UINT32),
    ("CLPCmdStatus",          UINT8),
    ("CLPErrorValue",         UINT8),
    ("CLPMsgCode",            UINT16)
  ]

