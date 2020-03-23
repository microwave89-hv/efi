#
# Ip4Config2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Ip4Config2.py is free software: you can redistribute it and/or
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

import Ip4

gEfiIp4Config2ProtocolGuid = \
  EFI_GUID (0x5b446ed1, 0xe30b, 0x4faa, (0x87, 0x1a, 0x36, 0x54, 0xec, 0xa3, 0x60, 0x80 ))

class EFI_IP4_CONFIG2_PROTOCOL (Structure):
  pass

Ip4Config2DataTypeInterfaceInfo   = 0
Ip4Config2DataTypePolicy          = 1
Ip4Config2DataTypeManualAddress   = 2
Ip4Config2DataTypeGateway         = 3
Ip4Config2DataTypeDnsServer       = 4
Ip4Config2DataTypeMaximum         = 5
EFI_IP4_CONFIG2_DATA_TYPE         = ENUM

class EFI_IP4_CONFIG2_INTERFACE_INFO (Structure):
  _fields_ = [
    ("Name",            CHAR16 * 32),
    ("IfType",          UINT8),
    ("HwAddressSize",   UINT32),
    ("HwAddress",       EFI_MAC_ADDRESS),
    ("StationAddress",  EFI_IPv4_ADDRESS),
    ("SubnetMask",      EFI_IPv4_ADDRESS),
    ("RouteTableSize",  UINT32),
    ("RouteTable",      POINTER(Ip4.EFI_IP4_ROUTE_TABLE))
  ]

Ip4Config2PolicyStatic  = 0
Ip4Config2PolicyDhcp    = 1
Ip4Config2PolicyMax     = 2
EFI_IP4_CONFIG2_POLICY  = ENUM

class EFI_IP4_CONFIG2_MANUAL_ADDRESS (Structure):
  _fields_ = [
    ("Address",     EFI_IPv4_ADDRESS),
    ("SubnetMask",  EFI_IPv4_ADDRESS)
  ]

EFI_IP4_CONFIG2_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_CONFIG2_PROTOCOL),  # IN *This
  EFI_IP4_CONFIG2_DATA_TYPE,          # IN DataType,
  UINTN,                              # IN DataSize,
  PVOID                               # IN *Data
  )

EFI_IP4_CONFIG2_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_CONFIG2_PROTOCOL),  # IN      *This
  EFI_IP4_CONFIG2_DATA_TYPE,          # IN      DataType,
  POINTER(UINTN),                     # IN OUT  *DataSize,
  PVOID                               # IN      *Data
  )

EFI_IP4_CONFIG2_REGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_CONFIG2_PROTOCOL),  # IN      *This
  EFI_IP4_CONFIG2_DATA_TYPE,          # IN      DataType,
  EFI_EVENT                           # IN      Event
  )

EFI_IP4_CONFIG2_UNREGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_CONFIG2_PROTOCOL),  # IN  *This
  EFI_IP4_CONFIG2_DATA_TYPE,          # IN  DataType,
  EFI_EVENT                           # IN  Event
  )

EFI_IP4_CONFIG2_PROTOCOL._fields_ = [
    ("SetData",               EFI_IP4_CONFIG2_SET_DATA),
    ("GetData",               EFI_IP4_CONFIG2_GET_DATA),
    ("RegisterDataNotify",    EFI_IP4_CONFIG2_REGISTER_NOTIFY),
    ("UnregisterDataNotify",  EFI_IP4_CONFIG2_UNREGISTER_NOTIFY)
  ]

