# 
# PciExpress21.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PciExpress21.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard import *

EFI_PCIE_CAPABILITY_BASE_OFFSET                             = 0x100
EFI_PCIE_CAPABILITY_ID_SRIOV_CONTROL_ARI_HIERARCHY          = 0x10 
EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_2_OFFSET            = 0x24 
EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_2_ARI_FORWARDING    = 0x20 
EFI_PCIE_CAPABILITY_DEVICE_CONTROL_2_OFFSET                 = 0x28 
EFI_PCIE_CAPABILITY_DEVICE_CONTROL_2_ARI_FORWARDING         = 0x20 

EFI_PCIE_CAPABILITY_ID_ARI        = 0x0E
EFI_PCIE_CAPABILITY_ID_ATS        = 0x0F
EFI_PCIE_CAPABILITY_ID_SRIOV      = 0x10
EFI_PCIE_CAPABILITY_ID_MRIOV      = 0x11

class SR_IOV_CAPABILITY_REGISTER (Structure):
  _fields_ = [
    ("CapabilityHeader",            UINT32),
    ("Capability",                  UINT32),
    ("Control",                     UINT16),
    ("Status",                      UINT16),
    ("InitialVFs",                  UINT16),
    ("TotalVFs",                    UINT16),
    ("NumVFs",                      UINT16),
    ("FunctionDependencyLink",      UINT8),
    ("Reserved0",                   UINT8),
    ("FirstVFOffset",               UINT16),
    ("VFStride",                    UINT16),
    ("Reserved1",                   UINT16),
    ("VFDeviceID",                  UINT16),
    ("SupportedPageSize",           UINT32),
    ("SystemPageSize",              UINT32),
    ("VFBar",                       UINT32 * 6),
    ("VFMigrationStateArrayOffset", UINT32)
    ]

EFI_PCIE_CAPABILITY_ID_SRIOV_CAPABILITIES               = 0x04
EFI_PCIE_CAPABILITY_ID_SRIOV_CONTROL                    = 0x08
EFI_PCIE_CAPABILITY_ID_SRIOV_STATUS                     = 0x0A
EFI_PCIE_CAPABILITY_ID_SRIOV_INITIALVFS                 = 0x0C
EFI_PCIE_CAPABILITY_ID_SRIOV_TOTALVFS                   = 0x0E
EFI_PCIE_CAPABILITY_ID_SRIOV_NUMVFS                     = 0x10
EFI_PCIE_CAPABILITY_ID_SRIOV_FUNCTION_DEPENDENCY_LINK   = 0x12
EFI_PCIE_CAPABILITY_ID_SRIOV_FIRSTVF                    = 0x14
EFI_PCIE_CAPABILITY_ID_SRIOV_VFSTRIDE                   = 0x16
EFI_PCIE_CAPABILITY_ID_SRIOV_VFDEVICEID                 = 0x1A
EFI_PCIE_CAPABILITY_ID_SRIOV_SUPPORTED_PAGE_SIZE        = 0x1C
EFI_PCIE_CAPABILITY_ID_SRIOV_SYSTEM_PAGE_SIZE           = 0x20
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR0                       = 0x24
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR1                       = 0x28
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR2                       = 0x2C
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR3                       = 0x30
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR4                       = 0x34
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR5                       = 0x38
EFI_PCIE_CAPABILITY_ID_SRIOV_VF_MIGRATION_STATE         = 0x3C

class PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER (Structure):
  _fields_ = [
    ("CapabilityId",            UINT32, 16),
    ("CapabilityVersion",       UINT32,  4),
    ("NextCapabilityOffset",    UINT32, 12)
    ]

PCI_EXP_EXT_HDR = PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER

PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_ID   = 0x0001
PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_VER1 = 0x1   
PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_VER2 = 0x2   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_ADVANCED_ERROR_REPORTING (Structure):
  _fields_ = [
    ("Header",                                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("UncorrectableErrorStatus",              UINT32),
    ("UncorrectableErrorMask",                UINT32),
    ("UncorrectableErrorSeverity",            UINT32),
    ("CorrectableErrorStatus",                UINT32),
    ("CorrectableErrorMask",                  UINT32),
    ("AdvancedErrorCapabilitiesAndControl",   UINT32),
    ("HeaderLog",                             UINT32),
    ("RootErrorCommand",                      UINT32),
    ("RootErrorStatus",                       UINT32),
    ("ErrorSourceIdentification",             UINT16),
    ("CorrectableErrorSourceIdentification",  UINT16),
    ("TlpPrefixLog",                          UINT32 * 4)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_ID    = 0x0002
PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_MFVC  = 0x0009
PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_VC (Structure):
  _fields_ = [
    ("VcResourceCapability",  UINT32, 24),
    ("PortArbTableOffset",    UINT32,  8),
    ("VcResourceControl",     UINT32),
    ("Reserved1",             UINT16),
    ("VcResourceStatus",      UINT16)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_CAPABILITY (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("ExtendedVcCount",   UINT32,  3),
    ("PortVcCapability1", UINT32, 29),
    ("PortVcCapability2", UINT32, 24),
    ("VcArbTableOffset",  UINT32,  8),
    ("PortVcControl",     UINT16),
    ("PortVcStatus",      UINT16),
    ("Capability",        PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_VC * 1)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_SERIAL_NUMBER_ID    = 0x0003
PCI_EXPRESS_EXTENDED_CAPABILITY_SERIAL_NUMBER_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_SERIAL_NUMBER (Structure):
  _fields_ = [
    ("Header",        PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("SerialNumber",  UINT64)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_ID   = 0x0005
PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_LINK_DECLARATION (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("ElementSelfDescription",  UINT32),
    ("Reserved",                UINT32),
    ("LinkEntry",               UINT32 * 1)
    ]

def PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_GET_LINK_COUNT (LINK_DECLARATION):

  return cast(((LINK_DECLARATION.ElementSelfDescription) & 0x0000ff00)>>8, UINT8)

PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_CONTROL_ID   = 0x0006
PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_CONTROL_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_INTERNAL_LINK_CONTROL (Structure):
  _fields_ = [
    ("Header",                      PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("RootComplexLinkCapabilities", UINT32),
    ("RootComplexLinkControl",      UINT16),
    ("RootComplexLinkStatus",       UINT16)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_POWER_BUDGETING_ID   = 0x0004
PCI_EXPRESS_EXTENDED_CAPABILITY_POWER_BUDGETING_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_POWER_BUDGETING (Structure):
  _fields_ = [
    ("Header",                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DataSelect",            UINT32,  8),
    ("Reserved",              UINT32, 24),
    ("Data",                  UINT32),
    ("PowerBudgetCapability", UINT32,  1),
    ("Reserved2",             UINT32,  7),
    ("Reserved3",             UINT32, 24)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_ID   = 0x000D
PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_ACS_EXTENDED (Structure):
  _fields_ = [
    ("Header",                    PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AcsCapability",             UINT16),
    ("AcsControl",                UINT16),
    ("EgressControlVectorArray",  UINT8 * 1)
    ]

def PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_GET_EGRES_CONTROL (ACS_EXTENDED):

  return cast(((ACS_EXTENDED.AcsCapability)&0x00000020), UINT8)

def PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_GET_EGRES_VECTOR_SIZE(ACS_EXTENDED):

  return cast(((ACS_EXTENDED.AcsCapability)&0x0000FF00), UINT8)

PCI_EXPRESS_EXTENDED_CAPABILITY_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_ID   = 0x0007
PCI_EXPRESS_EXTENDED_CAPABILITY_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AssociationBitmap", UINT32)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_MULTI_FUNCTION_VIRTUAL_CHANNEL_ID    = 0x0008
PCI_EXPRESS_EXTENDED_CAPABILITY_MULTI_FUNCTION_VIRTUAL_CHANNEL_VER1  = 0x1   

PCI_EXPRESS_EXTENDED_CAPABILITIES_MULTI_FUNCTION_VIRTUAL_CHANNEL_CAPABILITY = PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_CAPABILITY

PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_ID   = 0x000B
PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_VENDOR_SPECIFIC (Structure):
  _fields_ = [
    ("Header",                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("VendorSpecificHeader",  UINT32),
    ("VendorSpecific",        UINT8 * 1)
    ]

def PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_GET_SIZE(VENDOR):

  return cast(((VENDOR.VendorSpecificHeader)&0xFFF00000)>>20, UINT16)

PCI_EXPRESS_EXTENDED_CAPABILITY_RCRB_HEADER_ID   = 0x000A
PCI_EXPRESS_EXTENDED_CAPABILITY_RCRB_HEADER_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RCRB_HEADER (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("VendorId",          UINT16),
    ("DeviceId",          UINT16),
    ("RcrbCapabilities",  UINT32),
    ("RcrbControl",       UINT32),
    ("Reserved",          UINT32)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_MULTICAST_ID   = 0x0012
PCI_EXPRESS_EXTENDED_CAPABILITY_MULTICAST_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_MULTICAST (Structure):
  _fields_ = [
    ("Header",              PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("MultiCastCapability", UINT16),
    ("MulticastControl",    UINT16),
    ("McBaseAddress",       UINT64),
    ("McReceiveAddress",    UINT64),
    ("McBlockAll",          UINT64),
    ("McBlockUntranslated", UINT64),
    ("McOverlayBar",        UINT64)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_RESIZABLE_BAR_ID    = 0x0015
PCI_EXPRESS_EXTENDED_CAPABILITY_RESIZABLE_BAR_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_ENTRY (Structure):
  _fields_ = [
    ("ResizableBarCapability",  UINT32),
    ("ResizableBarControl",     UINT16),
    ("Reserved",                UINT16)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR (Structure):
  _fields_ = [
    ("Header",      PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("Capability",  PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_ENTRY * 1)
    ]

def GET_NUMBER_RESIZABLE_BARS(x):

  return (((x.Capability[0].ResizableBarControl) & 0xE0) >> 5)

PCI_EXPRESS_EXTENDED_CAPABILITY_ARI_CAPABILITY_ID    = 0x000E
PCI_EXPRESS_EXTENDED_CAPABILITY_ARI_CAPABILITY_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_ARI_CAPABILITY (Structure):
  _fields_ = [
    ("Header",        PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AriCapability", UINT16),
    ("AriControl",    UINT16)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_ID    = 0x0016
PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_DYNAMIC_POWER_ALLOCATION (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DpaCapability",           UINT32),
    ("DpaLatencyIndicator",     UINT32),
    ("DpaStatus",               UINT16),
    ("DpaControl",              UINT16),
    ("DpaPowerAllocationArray", UINT8 * 1)
    ]

def PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_GET_SUBSTATE_MAX(POWER):

  return cast(((POWER.DpaCapability)&0x0000000F), UINT16)

PCI_EXPRESS_EXTENDED_CAPABILITY_LATENCE_TOLERANCE_REPORTING_ID    = 0x0018
PCI_EXPRESS_EXTENDED_CAPABILITY_LATENCE_TOLERANCE_REPORTING_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_LATENCE_TOLERANCE_REPORTING (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DpaCapability",           UINT32),
    ("DpaLatencyIndicator",     UINT32),
    ("DpaStatus",               UINT16),
    ("DpaControl",              UINT16),
    ("DpaPowerAllocationArray", UINT8 * 1)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_TPH_ID    = 0x0017
PCI_EXPRESS_EXTENDED_CAPABILITY_TPH_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_TPH (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("TphRequesterCapability",  UINT32),
    ("TphRequesterControl",     UINT32),
    ("TphStTable",              UINT16 * 1)
    ]

def GET_TPH_TABLE_SIZE(x):

  return ((x.TphRequesterCapability & 0x7FF0000)>>16) * sizeof(UINT16)

