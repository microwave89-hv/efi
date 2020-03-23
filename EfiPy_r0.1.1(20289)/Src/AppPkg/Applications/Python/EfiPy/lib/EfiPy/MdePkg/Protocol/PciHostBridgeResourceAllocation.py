#
# PciHostBridgeResourceAllocation.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PciHostBridgeResourceAllocation.py is free software: you can redistribute it and/or
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

import PciRootBridgeIo

gEfiPciHostBridgeResourceAllocationProtocolGuid = \
  EFI_GUID (0xCF8034BE, 0x6768, 0x4d8b, (0xB7,0x39,0x7C,0xCE,0x68,0x3A,0x9F,0xBE ))

class EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL (Structure):
  pass

EFI_PCI_HOST_BRIDGE_COMBINE_MEM_PMEM  = 1
EFI_PCI_HOST_BRIDGE_MEM64_DECODE   = 2
EFI_RESOURCE_ALLOCATION_STATUS  = UINT64
EFI_RESOURCE_SATISFIED      = 0x0000000000000000L

EFI_RESOURCE_NOT_SATISFIED  = 0xFFFFFFFFFFFFFFFFL
EfiPciHostBridgeBeginEnumeration                = 0
EfiPciHostBridgeBeginBusAllocation              = 1
EfiPciHostBridgeEndBusAllocation                = 2
EfiPciHostBridgeBeginResourceAllocation         = 3
EfiPciHostBridgeAllocateResources               = 4
EfiPciHostBridgeSetResources                    = 5
EfiPciHostBridgeFreeResources                   = 6
EfiPciHostBridgeEndResourceAllocation           = 7
EfiPciHostBridgeEndEnumeration                  = 8
EfiMaxPciHostBridgeEnumerationPhase             = 9
EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PHASE   = ENUM

EfiPciBeforeChildBusEnumeration               = 0
EfiPciBeforeResourceCollection                = 1
EFI_PCI_CONTROLLER_RESOURCE_ALLOCATION_PHASE  = ENUM

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_NOTIFY_PHASE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL),# IN *This
  EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PHASE             # IN Phase
  )

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_GET_NEXT_ROOT_BRIDGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL),  # IN *This
  POINTER(EFI_HANDLE)                                         # IN  OUT *RootBridgeHandle
  )

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_GET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL),  # IN  *This,
  EFI_HANDLE,                                                 # IN  RootBridgeHandle,
  POINTER(UINT64)                                             # OUT *Attributes
  )

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_START_BUS_ENUMERATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL),  # IN  *This,
  EFI_HANDLE,                                                 # IN  RootBridgeHandle,
  POINTER(PVOID)                                              # OUT **Configuration
  )

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_SET_BUS_NUMBERS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL),  # IN  *This,
  EFI_HANDLE,                                                 # IN  RootBridgeHandle,
  PVOID                                                       # IN  *Configuration
  )

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_SUBMIT_RESOURCES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL),  # IN  *This,
  EFI_HANDLE,                                                 # IN  RootBridgeHandle,
  PVOID                                                       # IN  *Configuration
  )

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_GET_PROPOSED_RESOURCES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL),  # IN  *This,
  EFI_HANDLE,                                                 # IN  RootBridgeHandle,
  POINTER(PVOID)                                              # OUT **Configuration
  )

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_PREPROCESS_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL),    # IN  *This,
  PciRootBridgeIo.EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_PCI_ADDRESS,  # IN PciAddress,
  EFI_PCI_CONTROLLER_RESOURCE_ALLOCATION_PHASE                  # IN Phase
  )

EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL._fields_ = [
    ("NotifyPhase",           EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_NOTIFY_PHASE),
    ("GetNextRootBridge",     EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_GET_NEXT_ROOT_BRIDGE),
    ("GetAllocAttributes",    EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_GET_ATTRIBUTES),
    ("StartBusEnumeration",   EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_START_BUS_ENUMERATION),
    ("SetBusNumbers",         EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_SET_BUS_NUMBERS),
    ("SubmitResources",       EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_SUBMIT_RESOURCES),
    ("GetProposedResources",  EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_GET_PROPOSED_RESOURCES),
    ("PreprocessController",  EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PROTOCOL_PREPROCESS_CONTROLLER)
  ]

