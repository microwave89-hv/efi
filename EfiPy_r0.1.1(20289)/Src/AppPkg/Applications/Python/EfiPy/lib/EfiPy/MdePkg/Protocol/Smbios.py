#
# Smbios.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Smbios.py is free software: you can redistribute it and/or
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

gEfiSmbiosProtocolGuid    = \
  EFI_GUID (0x3583ff6, 0xcb36, 0x4940, ( 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7 ))

EFI_SMBIOS_TYPE_BIOS_INFORMATION                    = 0
EFI_SMBIOS_TYPE_SYSTEM_INFORMATION                  = 1
EFI_SMBIOS_TYPE_BASEBOARD_INFORMATION               = 2
EFI_SMBIOS_TYPE_SYSTEM_ENCLOSURE                    = 3
EFI_SMBIOS_TYPE_PROCESSOR_INFORMATION               = 4
EFI_SMBIOS_TYPE_MEMORY_CONTROLLER_INFORMATION       = 5
EFI_SMBIOS_TYPE_MEMORY_MODULE_INFORMATON            = 6
EFI_SMBIOS_TYPE_CACHE_INFORMATION                   = 7
EFI_SMBIOS_TYPE_PORT_CONNECTOR_INFORMATION          = 8
EFI_SMBIOS_TYPE_SYSTEM_SLOTS                        = 9
EFI_SMBIOS_TYPE_ONBOARD_DEVICE_INFORMATION          = 10
EFI_SMBIOS_TYPE_OEM_STRINGS                         = 11
EFI_SMBIOS_TYPE_SYSTEM_CONFIGURATION_OPTIONS        = 12
EFI_SMBIOS_TYPE_BIOS_LANGUAGE_INFORMATION           = 13
EFI_SMBIOS_TYPE_GROUP_ASSOCIATIONS                  = 14
EFI_SMBIOS_TYPE_SYSTEM_EVENT_LOG                    = 15
EFI_SMBIOS_TYPE_PHYSICAL_MEMORY_ARRAY               = 16
EFI_SMBIOS_TYPE_MEMORY_DEVICE                       = 17
EFI_SMBIOS_TYPE_32BIT_MEMORY_ERROR_INFORMATION      = 18
EFI_SMBIOS_TYPE_MEMORY_ARRAY_MAPPED_ADDRESS         = 19
EFI_SMBIOS_TYPE_MEMORY_DEVICE_MAPPED_ADDRESS        = 20
EFI_SMBIOS_TYPE_BUILT_IN_POINTING_DEVICE            = 21
EFI_SMBIOS_TYPE_PORTABLE_BATTERY                    = 22
EFI_SMBIOS_TYPE_SYSTEM_RESET                        = 23
EFI_SMBIOS_TYPE_HARDWARE_SECURITY                   = 24
EFI_SMBIOS_TYPE_SYSTEM_POWER_CONTROLS               = 25
EFI_SMBIOS_TYPE_VOLTAGE_PROBE                       = 26
EFI_SMBIOS_TYPE_COOLING_DEVICE                      = 27
EFI_SMBIOS_TYPE_TEMPERATURE_PROBE                   = 28
EFI_SMBIOS_TYPE_ELECTRICAL_CURRENT_PROBE            = 29
EFI_SMBIOS_TYPE_OUT_OF_BAND_REMOTE_ACCESS           = 30
EFI_SMBIOS_TYPE_BOOT_INTEGRITY_SERVICE              = 31
EFI_SMBIOS_TYPE_SYSTEM_BOOT_INFORMATION             = 32
EFI_SMBIOS_TYPE_64BIT_MEMORY_ERROR_INFORMATION      = 33
EFI_SMBIOS_TYPE_MANAGEMENT_DEVICE                   = 34
EFI_SMBIOS_TYPE_MANAGEMENT_DEVICE_COMPONENT         = 35
EFI_SMBIOS_TYPE_MANAGEMENT_DEVICE_THRESHOLD_DATA    = 36
EFI_SMBIOS_TYPE_MEMORY_CHANNEL                      = 37
EFI_SMBIOS_TYPE_IPMI_DEVICE_INFORMATION             = 38
EFI_SMBIOS_TYPE_SYSTEM_POWER_SUPPLY                 = 39
EFI_SMBIOS_TYPE_ADDITIONAL_INFORMATION              = 40
EFI_SMBIOS_TYPE_ONBOARD_DEVICES_EXTENDED_INFORMATION = 41
EFI_SMBIOS_TYPE_MANAGEMENT_CONTROLLER_HOST_INTERFACE = 42
EFI_SMBIOS_TYPE_INACTIVE                            = 126
EFI_SMBIOS_TYPE_END_OF_TABLE                        = 127
EFI_SMBIOS_OEM_BEGIN                                = 128
EFI_SMBIOS_OEM_END                                  = 255

EFI_SMBIOS_STRING = UINT8
EFI_SMBIOS_TYPE   = UINT8

EFI_SMBIOS_HANDLE   = UINT16

class EFI_SMBIOS_TABLE_HEADER (Structure):
  _fields_ = [
    ("Type",    EFI_SMBIOS_TYPE),
    ("Length",  UINT8),
    ("Handle",  EFI_SMBIOS_HANDLE)
  ]

class EFI_SMBIOS_PROTOCOL (Structure):
  pass

EFI_SMBIOS_ADD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBIOS_PROTOCOL),         # IN      *This
  EFI_HANDLE,                           # IN      ProducerHandle OPTIONAL,
  POINTER(EFI_SMBIOS_HANDLE),           # IN OUT  *SmbiosHandle,
  POINTER(EFI_SMBIOS_TABLE_HEADER)      # IN      *Record
  )

EFI_SMBIOS_UPDATE_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBIOS_PROTOCOL),         # IN *This
  POINTER(EFI_SMBIOS_HANDLE),           # IN *SmbiosHandle,
  POINTER(UINTN),                       # IN *StringNumber,
  PCHAR8                                # IN *String
  )

EFI_SMBIOS_REMOVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBIOS_PROTOCOL),         # IN *This
  EFI_SMBIOS_HANDLE                     # IN SmbiosHandle
  )

EFI_SMBIOS_GET_NEXT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBIOS_PROTOCOL),               # IN  *This
  POINTER(EFI_SMBIOS_HANDLE),                 # IN  *SmbiosHandle,
  POINTER(EFI_SMBIOS_TYPE),                   # IN  *Type              OPTIONAL,
  POINTER(POINTER(EFI_SMBIOS_TABLE_HEADER)),  # OUT **Record,
  POINTER(EFI_HANDLE)                         # OUT *ProducerHandle    OPTIONAL
  )

EFI_SMBIOS_PROTOCOL._fields_ = [
    ("Add",           EFI_SMBIOS_ADD),
    ("UpdateString",  EFI_SMBIOS_UPDATE_STRING),
    ("Remove",        EFI_SMBIOS_REMOVE),
    ("GetNext",       EFI_SMBIOS_GET_NEXT),
    ("MajorVersion",  UINT8),
    ("MinorVersion",  UINT8)
  ]

