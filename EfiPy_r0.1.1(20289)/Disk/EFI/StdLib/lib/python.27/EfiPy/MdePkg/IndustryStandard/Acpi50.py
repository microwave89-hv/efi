#
# Acpi50.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Acpi50.py is free software: you can redistribute it and/or
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
from Acpi40 import *

ACPI_SMALL_FIXED_DMA_DESCRIPTOR_NAME                         = 0x0A
ACPI_LARGE_GPIO_CONNECTION_DESCRIPTOR_NAME                   = 0x0C
ACPI_LARGE_GENERIC_SERIAL_BUS_CONNECTION_DESCRIPTOR_NAME     = 0x0E

ACPI_FIXED_DMA_DESCRIPTOR                         = 0x55
ACPI_GPIO_CONNECTION_DESCRIPTOR                   = 0x8C
ACPI_GENERIC_SERIAL_BUS_CONNECTION_DESCRIPTOR     = 0x8E

class EFI_ACPI_FIXED_DMA_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            ACPI_SMALL_RESOURCE_HEADER),
    ("DmaRequestLine",    UINT16),
    ("DmaChannel",        UINT16),
    ("DmaTransferWidth",  UINT8)
  ]

class EFI_ACPI_GPIO_CONNECTION_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                    ACPI_LARGE_RESOURCE_HEADER),
    ("RevisionId",                UINT8),
    ("ConnectionType",            UINT8),
    ("GeneralFlags",              UINT16),
    ("InterruptFlags",            UINT16),
    ("PinConfiguration",          UINT8 ),
    ("OutputDriveStrength",       UINT16),
    ("DebounceTimeout",           UINT16),
    ("PinTableOffset",            UINT16),
    ("ResourceSourceIndex",       UINT8),
    ("ResourceSourceNameOffset",  UINT16),
    ("VendorDataOffset",          UINT16),
    ("VendorDataLength",          UINT16)
  ]

EFI_ACPI_GPIO_CONNECTION_TYPE_INTERRUPT   = 0x0
EFI_ACPI_GPIO_CONNECTION_TYPE_IO          = 0x1

class EFI_ACPI_SERIAL_BUS_RESOURCE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  ACPI_LARGE_RESOURCE_HEADER),
    ("RevisionId",              UINT8),
    ("ResourceSourceIndex",     UINT8),
    ("SerialBusType",           UINT8),
    ("GeneralFlags",            UINT8),
    ("TypeSpecificFlags",       UINT16),
    ("TypeSpecificRevisionId",  UINT8),
    ("TypeDataLength",          UINT16)
  ]

EFI_ACPI_SERIAL_BUS_RESOURCE_TYPE_I2C   = 0x1
EFI_ACPI_SERIAL_BUS_RESOURCE_TYPE_SPI   = 0x2
EFI_ACPI_SERIAL_BUS_RESOURCE_TYPE_UART  = 0x3

class EFI_ACPI_SERIAL_BUS_RESOURCE_I2C_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  ACPI_LARGE_RESOURCE_HEADER),
    ("RevisionId",              UINT8),
    ("ResourceSourceIndex",     UINT8),
    ("SerialBusType",           UINT8),
    ("GeneralFlags",            UINT8),
    ("TypeSpecificFlags",       UINT16),
    ("TypeSpecificRevisionId",  UINT8),
    ("TypeDataLength",          UINT16),
    ("ConnectionSpeed",         UINT32),
    ("SlaveAddress",            UINT16)
  ]

class EFI_ACPI_SERIAL_BUS_RESOURCE_SPI_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                 ACPI_LARGE_RESOURCE_HEADER),
    ("RevisionId",             UINT8),
    ("ResourceSourceIndex",    UINT8),
    ("SerialBusType",          UINT8),
    ("GeneralFlags",           UINT8),
    ("TypeSpecificFlags",      UINT16),
    ("TypeSpecificRevisionId", UINT8),
    ("TypeDataLength",         UINT16),
    ("ConnectionSpeed",        UINT32),
    ("DataBitLength",          UINT8),
    ("Phase",                  UINT8),
    ("Polarity",               UINT8),
    ("DeviceSelection",        UINT16)
  ]

class EFI_ACPI_SERIAL_BUS_RESOURCE_SPI_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  ACPI_LARGE_RESOURCE_HEADER),
    ("RevisionId",              UINT8),
    ("ResourceSourceIndex",     UINT8),
    ("SerialBusType",           UINT8),
    ("GeneralFlags",            UINT8),
    ("TypeSpecificFlags",       UINT16),
    ("TypeSpecificRevisionId",  UINT8),
    ("TypeDataLength",          UINT16),
    ("DefaultBaudRate",         UINT32),
    ("RxFIFO",                  UINT16),
    ("TxFIFO",                  UINT16),
    ("Parity",                  UINT8),
    ("SerialLinesEnabled",      UINT8)
  ]

EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE = EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE

EFI_ACPI_5_0_SYSTEM_MEMORY              = 0
EFI_ACPI_5_0_SYSTEM_IO                  = 1
EFI_ACPI_5_0_PCI_CONFIGURATION_SPACE    = 2
EFI_ACPI_5_0_EMBEDDED_CONTROLLER        = 3
EFI_ACPI_5_0_SMBUS                      = 4
EFI_ACPI_5_0_PLATFORM_COMMUNICATION_CHANNEL  = 0x0A
EFI_ACPI_5_0_FUNCTIONAL_FIXED_HARDWARE       = 0x7F

EFI_ACPI_5_0_UNDEFINED  = 0
EFI_ACPI_5_0_BYTE       = 1
EFI_ACPI_5_0_WORD       = 2
EFI_ACPI_5_0_DWORD      = 3
EFI_ACPI_5_0_QWORD      = 4

EFI_ACPI_5_0_ROOT_SYSTEM_DESCRIPTION_POINTER = EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER

EFI_ACPI_5_0_ROOT_SYSTEM_DESCRIPTION_POINTER_REVISION = 0x02

EFI_ACPI_5_0_COMMON_HEADER = EFI_ACPI_4_0_COMMON_HEADER

EFI_ACPI_5_0_ROOT_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_5_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

class EFI_ACPI_5_0_FIXED_ACPI_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DESCRIPTION_HEADER),
    ("FirmwareCtrl",        UINT32),
    ("Dsdt",                UINT32),
    ("Reserved0",           UINT8),
    ("PreferredPmProfile",  UINT8),
    ("SciInt",              UINT16),
    ("SmiCmd",              UINT32),
    ("AcpiEnable",          UINT8),
    ("AcpiDisable",         UINT8),
    ("S4BiosReq",           UINT8),
    ("PstateCnt",           UINT8),
    ("Pm1aEvtBlk",          UINT32),
    ("Pm1bEvtBlk",          UINT32),
    ("Pm1aCntBlk",          UINT32),
    ("Pm1bCntBlk",          UINT32),
    ("Pm2CntBlk",           UINT32),
    ("PmTmrBlk",            UINT32),
    ("Gpe0Blk",             UINT32),
    ("Gpe1Blk",             UINT32),
    ("Pm1EvtLen",           UINT8),
    ("Pm1CntLen",           UINT8),
    ("Pm2CntLen",           UINT8),
    ("PmTmrLen",            UINT8),
    ("Gpe0BlkLen",          UINT8),
    ("Gpe1BlkLen",          UINT8),
    ("Gpe1Base",            UINT8),
    ("CstCnt",              UINT8),
    ("PLvl2Lat",            UINT16),
    ("PLvl3Lat",            UINT16),
    ("FlushSize",           UINT16),
    ("FlushStride",         UINT16),
    ("DutyOffset",          UINT8),
    ("DutyWidth",           UINT8),
    ("DayAlrm",             UINT8),
    ("MonAlrm",             UINT8),
    ("Century",             UINT8),
    ("IaPcBootArch",        UINT16),
    ("Reserved1",           UINT8 ),
    ("Flags",               UINT32),
    ("ResetReg",            EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("ResetValue",          UINT8),
    ("Reserved2",           UINT8 * 3),
    ("XFirmwareCtrl",       UINT64),
    ("XDsdt",               UINT64),
    ("XPm1aEvtBlk",         EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1bEvtBlk",         EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1aCntBlk",         EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1bCntBlk",         EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm2CntBlk",          EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPmTmrBlk",           EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("XGpe0Blk",            EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("XGpe1Blk",            EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("SleepControlReg",     EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("SleepStatusReg",      EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
  ]

EFI_ACPI_5_0_FIXED_ACPI_DESCRIPTION_TABLE_REVISION  = 0x05

EFI_ACPI_5_0_PM_PROFILE_UNSPECIFIED         = 0
EFI_ACPI_5_0_PM_PROFILE_DESKTOP             = 1
EFI_ACPI_5_0_PM_PROFILE_MOBILE              = 2
EFI_ACPI_5_0_PM_PROFILE_WORKSTATION         = 3
EFI_ACPI_5_0_PM_PROFILE_ENTERPRISE_SERVER   = 4
EFI_ACPI_5_0_PM_PROFILE_SOHO_SERVER         = 5
EFI_ACPI_5_0_PM_PROFILE_APPLIANCE_PC        = 6
EFI_ACPI_5_0_PM_PROFILE_PERFORMANCE_SERVER  = 7
EFI_ACPI_5_0_PM_PROFILE_TABLET              = 8

EFI_ACPI_5_0_LEGACY_DEVICES              = BIT0
EFI_ACPI_5_0_8042                        = BIT1
EFI_ACPI_5_0_VGA_NOT_PRESENT             = BIT2
EFI_ACPI_5_0_MSI_NOT_SUPPORTED           = BIT3
EFI_ACPI_5_0_PCIE_ASPM_CONTROLS          = BIT4
EFI_ACPI_5_0_CMOS_RTC_NOT_PRESENT        = BIT5

EFI_ACPI_5_0_WBINVD                                 = BIT0
EFI_ACPI_5_0_WBINVD_FLUSH                           = BIT1
EFI_ACPI_5_0_PROC_C1                                = BIT2
EFI_ACPI_5_0_P_LVL2_UP                              = BIT3
EFI_ACPI_5_0_PWR_BUTTON                             = BIT4
EFI_ACPI_5_0_SLP_BUTTON                             = BIT5
EFI_ACPI_5_0_FIX_RTC                                = BIT6
EFI_ACPI_5_0_RTC_S4                                 = BIT7
EFI_ACPI_5_0_TMR_VAL_EXT                            = BIT8
EFI_ACPI_5_0_DCK_CAP                                = BIT9
EFI_ACPI_5_0_RESET_REG_SUP                          = BIT10
EFI_ACPI_5_0_SEALED_CASE                            = BIT11
EFI_ACPI_5_0_HEADLESS                               = BIT12
EFI_ACPI_5_0_CPU_SW_SLP                             = BIT13
EFI_ACPI_5_0_PCI_EXP_WAK                            = BIT14
EFI_ACPI_5_0_USE_PLATFORM_CLOCK                     = BIT15
EFI_ACPI_5_0_S4_RTC_STS_VALID                       = BIT16
EFI_ACPI_5_0_REMOTE_POWER_ON_CAPABLE                = BIT17
EFI_ACPI_5_0_FORCE_APIC_CLUSTER_MODEL               = BIT18
EFI_ACPI_5_0_FORCE_APIC_PHYSICAL_DESTINATION_MODE   = BIT19
EFI_ACPI_5_0_HW_REDUCED_ACPI                        = BIT20
EFI_ACPI_5_0_LOW_POWER_S0_IDLE_CAPABLE              = BIT21

EFI_ACPI_5_0_FIRMWARE_ACPI_CONTROL_STRUCTURE = EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE

EFI_ACPI_5_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_VERSION  = 0x02

EFI_ACPI_5_0_S4BIOS_F                     = BIT0
EFI_ACPI_5_0_64BIT_WAKE_SUPPORTED_F       = BIT1

EFI_ACPI_5_0_OSPM_64BIT_WAKE_F            = BIT0

EFI_ACPI_5_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_REVISION   = 0x02
EFI_ACPI_5_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_REVISION        = 0x02

EFI_ACPI_5_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER = EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER

EFI_ACPI_5_0_MULTIPLE_APIC_DESCRIPTION_TABLE_REVISION = 0x03

EFI_ACPI_5_0_PCAT_COMPAT         = BIT0

EFI_ACPI_5_0_PROCESSOR_LOCAL_APIC           = 0x00
EFI_ACPI_5_0_IO_APIC                        = 0x01
EFI_ACPI_5_0_INTERRUPT_SOURCE_OVERRIDE      = 0x02
EFI_ACPI_5_0_NON_MASKABLE_INTERRUPT_SOURCE  = 0x03
EFI_ACPI_5_0_LOCAL_APIC_NMI                 = 0x04
EFI_ACPI_5_0_LOCAL_APIC_ADDRESS_OVERRIDE    = 0x05
EFI_ACPI_5_0_IO_SAPIC                       = 0x06
EFI_ACPI_5_0_LOCAL_SAPIC                    = 0x07
EFI_ACPI_5_0_PLATFORM_INTERRUPT_SOURCES     = 0x08
EFI_ACPI_5_0_PROCESSOR_LOCAL_X2APIC         = 0x09
EFI_ACPI_5_0_LOCAL_X2APIC_NMI               = 0x0A
EFI_ACPI_5_0_GIC                            = 0x0B
EFI_ACPI_5_0_GICD                           = 0x0C

EFI_ACPI_5_0_PROCESSOR_LOCAL_APIC_STRUCTURE = EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_STRUCTURE

EFI_ACPI_5_0_LOCAL_APIC_ENABLED        = BIT0

EFI_ACPI_5_0_IO_APIC_STRUCTURE = EFI_ACPI_4_0_IO_APIC_STRUCTURE

EFI_ACPI_5_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE = EFI_ACPI_4_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE

EFI_ACPI_5_0_PLATFORM_INTERRUPT_APIC_STRUCTURE = EFI_ACPI_4_0_PLATFORM_INTERRUPT_APIC_STRUCTURE

EFI_ACPI_5_0_POLARITY      = (3 << 0)
EFI_ACPI_5_0_TRIGGER_MODE  = (3 << 2)

EFI_ACPI_5_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE = EFI_ACPI_4_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE

EFI_ACPI_5_0_LOCAL_APIC_NMI_STRUCTURE = EFI_ACPI_4_0_LOCAL_APIC_NMI_STRUCTURE

EFI_ACPI_5_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE = EFI_ACPI_4_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE

EFI_ACPI_5_0_IO_SAPIC_STRUCTURE = EFI_ACPI_4_0_IO_SAPIC_STRUCTURE

EFI_ACPI_5_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE = EFI_ACPI_4_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE

EFI_ACPI_5_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE = EFI_ACPI_4_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE

EFI_ACPI_5_0_CPEI_PROCESSOR_OVERRIDE          = BIT0

EFI_ACPI_5_0_PROCESSOR_LOCAL_X2APIC_STRUCTURE = EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_STRUCTURE

EFI_ACPI_5_0_LOCAL_X2APIC_NMI_STRUCTURE = EFI_ACPI_4_0_LOCAL_X2APIC_NMI_STRUCTURE

class EFI_ACPI_5_0_GIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                      UINT8),
    ("Length",                    UINT8),
    ("Reserved",                  UINT16),
    ("GicId",                     UINT32),
    ("AcpiProcessorUid",          UINT32),
    ("Flags",                     UINT32),
    ("ParkingProtocolVersion",    UINT32),
    ("PerformanceInterruptGsiv",  UINT32),
    ("ParkedAddress",             UINT64),
    ("PhysicalBaseAddress",       UINT64)
  ]

EFI_ACPI_5_0_GIC_ENABLED                     = BIT0
EFI_ACPI_5_0_PERFORMANCE_INTERRUPT_MODEL     = BIT1

class EFI_ACPI_5_0_GIC_DISTRIBUTOR_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                UINT8),
    ("Length",              UINT8),
    ("Reserved1",           UINT16),
    ("GicId",               UINT32),
    ("PhysicalBaseAddress", UINT64),
    ("SystemVectorBase",    UINT32),
    ("Reserved2",           UINT32)
  ]

EFI_ACPI_5_0_SMART_BATTERY_DESCRIPTION_TABLE = EFI_ACPI_4_0_SMART_BATTERY_DESCRIPTION_TABLE

EFI_ACPI_5_0_SMART_BATTERY_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_5_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE = EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE

EFI_ACPI_5_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION  = 0x01

EFI_ACPI_5_0_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER = EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER

EFI_ACPI_5_0_SYSTEM_RESOURCE_AFFINITY_TABLE_REVISION  = 0x03

EFI_ACPI_5_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY  = 0x00
EFI_ACPI_5_0_MEMORY_AFFINITY                      = 0x01
EFI_ACPI_5_0_PROCESSOR_LOCAL_X2APIC_AFFINITY      = 0x02

EFI_ACPI_5_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY_STRUCTURE = EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY_STRUCTURE

EFI_ACPI_5_0_PROCESSOR_LOCAL_APIC_SAPIC_ENABLED = (1 << 0)

EFI_ACPI_5_0_MEMORY_AFFINITY_STRUCTURE = EFI_ACPI_4_0_MEMORY_AFFINITY_STRUCTURE

EFI_ACPI_5_0_MEMORY_ENABLED       = (1 << 0)
EFI_ACPI_5_0_MEMORY_HOT_PLUGGABLE = (1 << 1)
EFI_ACPI_5_0_MEMORY_NONVOLATILE   = (1 << 2)

EFI_ACPI_5_0_PROCESSOR_LOCAL_X2APIC_AFFINITY_STRUCTURE = EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_AFFINITY_STRUCTURE

EFI_ACPI_5_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER = EFI_ACPI_4_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER

EFI_ACPI_5_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_REVISION  = 0x01

EFI_ACPI_5_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_HEADER = EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_HEADER

EFI_ACPI_5_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_REVISION = 0x01

EFI_ACPI_5_0_CPEP_PROCESSOR_APIC_SAPIC  = 0x00

EFI_ACPI_5_0_CPEP_PROCESSOR_APIC_SAPIC_STRUCTURE = EFI_ACPI_4_0_CPEP_PROCESSOR_APIC_SAPIC_STRUCTURE

EFI_ACPI_5_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_HEADER = EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_HEADER

EFI_ACPI_5_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_REVISION = 0x01

EFI_ACPI_5_0_MAXIMUM_PROXIMITY_DOMAIN_INFORMATION_STRUCTURE = EFI_ACPI_4_0_MAXIMUM_PROXIMITY_DOMAIN_INFORMATION_STRUCTURE

class EFI_ACPI_5_0_RAS_FEATURE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  EFI_ACPI_DESCRIPTION_HEADER),
    ("PlatformCommunicationChannelIdentifier",  UINT8)
  ]

EFI_ACPI_5_0_RAS_FEATURE_TABLE_REVISION = 0x01

class EFI_ACPI_5_0_RASF_PLATFORM_COMMUNICATION_CHANNEL_SHARED_MEMORY_REGION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",                   UINT32),
    ("Command",                     UINT16),
    ("Status",                      UINT16),
    ("Version",                     UINT16),
    ("RASCapabilities",             UINT8  * 16),
    ("SetRASCapabilities",          UINT8  * 16),
    ("NumberOfRASFParameterBlocks", UINT16),
    ("SetRASCapabilitiesStatus",    UINT32)
  ]

EFI_ACPI_5_0_RASF_PCC_COMMAND_CODE_EXECUTE_RASF_COMMAND  = 0x01

EFI_ACPI_5_0_RASF_PLATFORM_RAS_CAPABILITY_HARDWARE_BASED_PATROL_SCRUB_SUPPOTED                          = 0x01
EFI_ACPI_5_0_RASF_PLATFORM_RAS_CAPABILITY_HARDWARE_BASED_PATROL_SCRUB_SUPPOTED_AND_EXPOSED_TO_SOFTWARE  = 0x02

class EFI_ACPI_5_0_RASF_PATROL_SCRUB_PLATFORM_BLOCK_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                  UINT16),
    ("Version",               UINT16),
    ("Length",                UINT16),
    ("PatrolScrubCommand",    UINT16),
    ("RequestedAddressRange", UINT64 * 2),
    ("ActualAddressRange",    UINT64 * 2),
    ("Flags",                 UINT16),
    ("RequestedSpeed",        UINT8)
  ]

EFI_ACPI_5_0_RASF_PATROL_SCRUB_COMMAND_GET_PATROL_PARAMETERS   = 0x01
EFI_ACPI_5_0_RASF_PATROL_SCRUB_COMMAND_START_PATROL_SCRUBBER   = 0x02
EFI_ACPI_5_0_RASF_PATROL_SCRUB_COMMAND_STOP_PATROL_SCRUBBER    = 0x03

class EFI_ACPI_5_0_MEMORY_POWER_STATUS_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  EFI_ACPI_DESCRIPTION_HEADER),
    ("PlatformCommunicationChannelIdentifier",  UINT8),
    ("Reserved",                                UINT8 * 3)
  ]

EFI_ACPI_5_0_MEMORY_POWER_STATE_TABLE_REVISION = 0x01

class EFI_ACPI_5_0_MPST_PLATFORM_COMMUNICATION_CHANNEL_SHARED_MEMORY_REGION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",                   UINT32),
    ("Command",                     UINT16),
    ("Status",                      UINT16),
    ("MemoryPowerCommandRegister",  UINT32),
    ("MemoryPowerStatusRegister",   UINT32),
    ("PowerStateId",                UINT32),
    ("MemoryPowerNodeId",           UINT32),
    ("MemoryEnergyConsumed",        UINT64),
    ("ExpectedAveragePowerComsuned",UINT64)
  ]

EFI_ACPI_5_0_MPST_PCC_COMMAND_CODE_EXECUTE_MPST_COMMAND  = 0x03

EFI_ACPI_5_0_MPST_MEMORY_POWER_COMMAND_GET_MEMORY_POWER_STATE       = 0x01
EFI_ACPI_5_0_MPST_MEMORY_POWER_COMMAND_SET_MEMORY_POWER_STATE       = 0x02
EFI_ACPI_5_0_MPST_MEMORY_POWER_COMMAND_GET_AVERAGE_POWER_CONSUMED   = 0x03
EFI_ACPI_5_0_MPST_MEMORY_POWER_COMMAND_GET_MEMORY_ENERGY_CONSUMED   = 0x04

class EFI_ACPI_5_0_MPST_MEMORY_POWER_STATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerStateValue",             UINT8),
    ("PowerStateInformationIndex",  UINT8)
  ]

class EFI_ACPI_5_0_MPST_MEMORY_POWER_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Flag",                        UINT8),
    ("Reserved",                    UINT8),
    ("MemoryPowerNodeId",           UINT16),
    ("Length",                      UINT32),
    ("AddressBase",                 UINT64),
    ("AddressLength",               UINT64),
    ("NumberOfPowerStates",         UINT32),
    ("NumberOfPhysicalComponents",  UINT32),
    # ("MemoryPowerState",            EFI_ACPI_5_0_MPST_MEMORY_POWER_STATE * NumberOfPowerStates),
    # ("PhysicalComponentIdentifier", UINT16 * NumberOfPhysicalComponents)
  ]

EFI_ACPI_5_0_MPST_MEMORY_POWER_STRUCTURE_FLAG_ENABLE          = 0x01
EFI_ACPI_5_0_MPST_MEMORY_POWER_STRUCTURE_FLAG_POWER_MANAGED   = 0x02
EFI_ACPI_5_0_MPST_MEMORY_POWER_STRUCTURE_FLAG_HOT_PLUGGABLE   = 0x04

class EFI_ACPI_5_0_MPST_MEMORY_POWER_NODE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryPowerNodeCount",  UINT16),
    ("Reserved",              UINT8 * 2)
  ]

class EFI_ACPI_5_0_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerStateStructureID",       UINT8),
    ("Flag",                        UINT8),
    ("Reserved",                    UINT16),
    ("AveragePowerConsumedInMPS0",  UINT32),
    ("RelativePowerSavingToMPS0",   UINT32),
    ("ExitLatencyToMPS0",           UINT64)
  ]

EFI_ACPI_5_0_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE_FLAG_MEMORY_CONTENT_PRESERVED              = 0x01
EFI_ACPI_5_0_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE_FLAG_AUTONOMOUS_MEMORY_POWER_STATE_ENTRY   = 0x02
EFI_ACPI_5_0_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE_FLAG_AUTONOMOUS_MEMORY_POWER_STATE_EXIT    = 0x04

class EFI_ACPI_5_0_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryPowerStateCharacteristicsCount",  UINT16),
    ("Reserved",                              UINT8 * 2)
  ]

class EFI_ACPI_5_0_MEMORY_TOPOLOGY_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved",  UINT32)
  ]

EFI_ACPI_5_0_MEMORY_TOPOLOGY_TABLE_REVISION = 0x01

class EFI_ACPI_5_0_PMMT_COMMON_MEMORY_AGGREGATOR_DEVICE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",      UINT8),
    ("Reserved",  UINT8),
    ("Length",    UINT16),
    ("Flags",     UINT16),
    ("Reserved1", UINT16)
  ]

EFI_ACPI_5_0_PMMT_MEMORY_AGGREGATOR_DEVICE_TYPE_SOCKET            = 0x1
EFI_ACPI_5_0_PMMT_MEMORY_AGGREGATOR_DEVICE_TYPE_MEMORY_CONTROLLER = 0x2
EFI_ACPI_5_0_PMMT_MEMORY_AGGREGATOR_DEVICE_TYPE_DIMM              = 0x3

class EFI_ACPI_5_0_PMMT_SOCKET_MEMORY_AGGREGATOR_DEVICE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_ACPI_5_0_PMMT_COMMON_MEMORY_AGGREGATOR_DEVICE_STRUCTURE),
    ("SocketIdentifier",  UINT16),
    ("Reserved",          UINT16)
    # ("MemoryController",  EFI_ACPI_5_0_PMMT_MEMORY_CONTROLLER_MEMORY_AGGREGATOR_DEVICE_STRUCTURE * N)
  ]

class EFI_ACPI_5_0_PMMT_MEMORY_CONTROLLER_MEMORY_AGGREGATOR_DEVICE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                    EFI_ACPI_5_0_PMMT_COMMON_MEMORY_AGGREGATOR_DEVICE_STRUCTURE),
    ("ReadLatency",               UINT32),
    ("WriteLatency",              UINT32),
    ("ReadBandwidth",             UINT32),
    ("WriteBandwidth",            UINT32),
    ("OptimalAccessUnit",         UINT16),
    ("OptimalAccessAlignment",    UINT16),
    ("Reserved",                  UINT16),
    ("NumberOfProximityDomains",  UINT16)
    # ("ProximityDomain",           UINT32 * NumberOfProximityDomains),
    # ("PhysicalComponent",         EFI_ACPI_5_0_PMMT_DIMM_MEMORY_AGGREGATOR_DEVICE_STRUCTURE * N),
  ]

class EFI_ACPI_5_0_PMMT_DIMM_MEMORY_AGGREGATOR_DEVICE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      EFI_ACPI_5_0_PMMT_COMMON_MEMORY_AGGREGATOR_DEVICE_STRUCTURE),
    ("PhysicalComponentIdentifier", UINT16 ),
    ("Reserved",                    UINT16 ),
    ("SizeOfDimm",                  UINT32),
    ("SmbiosHandle",                UINT32)
  ]

class EFI_ACPI_5_0_BOOT_GRAPHICS_RESOURCE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_ACPI_DESCRIPTION_HEADER),
    ("Version",       UINT16),
    ("Status",        UINT8),
    ("ImageType",     UINT8),
    ("ImageAddress",  UINT64),
    ("ImageOffsetX",  UINT32),
    ("ImageOffsetY",  UINT32)
  ]

EFI_ACPI_5_0_BOOT_GRAPHICS_RESOURCE_TABLE_REVISION = 1

EFI_ACPI_5_0_BGRT_VERSION         = 0x01

EFI_ACPI_5_0_BGRT_STATUS_NOT_DISPLAYED = 0x00
EFI_ACPI_5_0_BGRT_STATUS_DISPLAYED     = 0x01
EFI_ACPI_5_0_BGRT_STATUS_INVALID       = EFI_ACPI_5_0_BGRT_STATUS_NOT_DISPLAYED
EFI_ACPI_5_0_BGRT_STATUS_VALID         = EFI_ACPI_5_0_BGRT_STATUS_DISPLAYED

EFI_ACPI_5_0_BGRT_IMAGE_TYPE_BMP  = 0x00

EFI_ACPI_5_0_FIRMWARE_PERFORMANCE_DATA_TABLE_REVISION = 0x01

EFI_ACPI_5_0_FPDT_RECORD_TYPE_FIRMWARE_BASIC_BOOT_POINTER      = 0x0000
EFI_ACPI_5_0_FPDT_RECORD_TYPE_S3_PERFORMANCE_TABLE_POINTER     = 0x0001

EFI_ACPI_5_0_FPDT_RECORD_REVISION_FIRMWARE_BASIC_BOOT_POINTER  = 0x01
EFI_ACPI_5_0_FPDT_RECORD_REVISION_S3_PERFORMANCE_TABLE_POINTER = 0x01

EFI_ACPI_5_0_FPDT_RUNTIME_RECORD_TYPE_S3_RESUME                = 0x0000
EFI_ACPI_5_0_FPDT_RUNTIME_RECORD_TYPE_S3_SUSPEND               = 0x0001
EFI_ACPI_5_0_FPDT_RUNTIME_RECORD_TYPE_FIRMWARE_BASIC_BOOT      = 0x0002

EFI_ACPI_5_0_FPDT_RUNTIME_RECORD_REVISION_S3_RESUME            = 0x01
EFI_ACPI_5_0_FPDT_RUNTIME_RECORD_REVISION_S3_SUSPEND           = 0x01
EFI_ACPI_5_0_FPDT_RUNTIME_RECORD_REVISION_FIRMWARE_BASIC_BOOT  = 0x02

class EFI_ACPI_5_0_FPDT_PERFORMANCE_RECORD_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",      UINT16),
    ("Length",    UINT8),
    ("Revision",  UINT8)
  ]

class EFI_ACPI_5_0_FPDT_PERFORMANCE_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature", UINT32),
    ("Length",    UINT32)
  ]

class EFI_ACPI_5_0_FPDT_BOOT_PERFORMANCE_TABLE_POINTER_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      EFI_ACPI_5_0_FPDT_PERFORMANCE_RECORD_HEADER),
    ("Reserved",                    UINT32),
    ("BootPerformanceTablePointer", UINT64)
  ]

class EFI_ACPI_5_0_FPDT_S3_PERFORMANCE_TABLE_POINTER_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      EFI_ACPI_5_0_FPDT_PERFORMANCE_RECORD_HEADER),
    ("Reserved",                    UINT32),
    ("S3PerformanceTablePointer",   UINT64)
  ]

class EFI_ACPI_5_0_FPDT_FIRMWARE_BASIC_BOOT_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_5_0_FPDT_PERFORMANCE_RECORD_HEADER),
    ("Reserved",                UINT32),
    ("ResetEnd",                UINT64),
    ("OsLoaderLoadImageStart",  UINT64),
    ("OsLoaderStartImageStart", UINT64),
    ("ExitBootServicesEntry",   UINT64),
    ("ExitBootServicesExit",    UINT64)
  ]

EFI_ACPI_5_0_FPDT_BOOT_PERFORMANCE_TABLE_SIGNATURE  = SIGNATURE_32('F', 'B', 'P', 'T')
class EFI_ACPI_5_0_FPDT_FIRMWARE_BASIC_BOOT_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_ACPI_5_0_FPDT_PERFORMANCE_TABLE_HEADER)
  ]

EFI_ACPI_5_0_FPDT_S3_PERFORMANCE_TABLE_SIGNATURE  = SIGNATURE_32('S', '3', 'P', 'T')
class EFI_ACPI_5_0_FPDT_FIRMWARE_S3_BOOT_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_ACPI_5_0_FPDT_PERFORMANCE_TABLE_HEADER)
  ]

class EFI_ACPI_5_0_FPDT_S3_RESUME_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_ACPI_5_0_FPDT_PERFORMANCE_RECORD_HEADER),
    ("ResumeCount",   UINT32),
    ("FullResume",    UINT64),
    ("AverageResume", UINT64)
  ]

class EFI_ACPI_5_0_FPDT_S3_SUSPEND_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_ACPI_5_0_FPDT_PERFORMANCE_RECORD_HEADER),
    ("SuspendStart",  UINT64),
    ("SuspendEnd",    UINT64)
  ]

class EFI_ACPI_5_0_FIRMWARE_PERFORMANCE_RECORD_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_ACPI_DESCRIPTION_HEADER)
  ]

class EFI_ACPI_5_0_GENERIC_TIMER_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_DESCRIPTION_HEADER),
    ("PhysicalAddress",         UINT64),
    ("GlobalFlags",             UINT32),
    ("SecurePL1TimerGSIV",      UINT32),
    ("SecurePL1TimerFlags",     UINT32),
    ("NonSecurePL1TimerGSIV",   UINT32),
    ("NonSecurePL1TimerFlags",  UINT32),
    ("VirtualTimerGSIV",        UINT32),
    ("VirtualTimerFlags",       UINT32),
    ("NonSecurePL2TimerGSIV",   UINT32),
    ("NonSecurePL2TimerFlags",  UINT32)
  ]

EFI_ACPI_5_0_GENERIC_TIMER_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_5_0_GTDT_GLOBAL_FLAG_MEMORY_MAPPED_BLOCK_PRESENT   = BIT0
EFI_ACPI_5_0_GTDT_GLOBAL_FLAG_INTERRUPT_MODE                = BIT1

EFI_ACPI_5_0_GTDT_TIMER_FLAG_TIMER_INTERRUPT_MODE          = BIT0
EFI_ACPI_5_0_GTDT_TIMER_FLAG_TIMER_INTERRUPT_POLARITY      = BIT1

class EFI_ACPI_5_0_BOOT_ERROR_RECORD_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                EFI_ACPI_DESCRIPTION_HEADER),
    ("BootErrorRegionLength", UINT32),
    ("BootErrorRegion",       UINT64)
  ]

EFI_ACPI_5_0_BOOT_ERROR_RECORD_TABLE_REVISION = 0x01

EFI_ACPI_5_0_ERROR_BLOCK_STATUS = EFI_ACPI_4_0_ERROR_BLOCK_STATUS

EFI_ACPI_5_0_BOOT_ERROR_REGION_STRUCTURE = EFI_ACPI_4_0_BOOT_ERROR_REGION_STRUCTURE

EFI_ACPI_5_0_ERROR_SEVERITY_CORRECTABLE  = 0x00
EFI_ACPI_5_0_ERROR_SEVERITY_FATAL        = 0x01
EFI_ACPI_5_0_ERROR_SEVERITY_CORRECTED    = 0x02
EFI_ACPI_5_0_ERROR_SEVERITY_NONE         = 0x03

EFI_ACPI_5_0_GENERIC_ERROR_DATA_ENTRY_STRUCTURE = EFI_ACPI_4_0_GENERIC_ERROR_DATA_ENTRY_STRUCTURE

EFI_ACPI_5_0_GENERIC_ERROR_DATA_ENTRY_REVISION  = 0x0201

EFI_ACPI_5_0_HARDWARE_ERROR_SOURCE_TABLE_HEADER = EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_HEADER

EFI_ACPI_5_0_HARDWARE_ERROR_SOURCE_TABLE_REVISION = 0x01

EFI_ACPI_5_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION  = 0x00
EFI_ACPI_5_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK  = 0x01
EFI_ACPI_5_0_IA32_ARCHITECTURE_NMI_ERROR                = 0x02
EFI_ACPI_5_0_PCI_EXPRESS_ROOT_PORT_AER                  = 0x06
EFI_ACPI_5_0_PCI_EXPRESS_DEVICE_AER                     = 0x07
EFI_ACPI_5_0_PCI_EXPRESS_BRIDGE_AER                     = 0x08
EFI_ACPI_5_0_GENERIC_HARDWARE_ERROR                     = 0x09

EFI_ACPI_5_0_ERROR_SOURCE_FLAG_FIRMWARE_FIRST       = (1 << 0)
EFI_ACPI_5_0_ERROR_SOURCE_FLAG_GLOBAL               = (1 << 1)

EFI_ACPI_5_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION_STRUCTURE = EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION_STRUCTURE

EFI_ACPI_5_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_BANK_STRUCTURE = EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_BANK_STRUCTURE

EFI_ACPI_5_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_IA32      = 0x00
EFI_ACPI_5_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_INTEL64   = 0x01
EFI_ACPI_5_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_AMD64     = 0x02

EFI_ACPI_5_0_HARDWARE_ERROR_NOTIFICATION_POLLED                = 0x00
EFI_ACPI_5_0_HARDWARE_ERROR_NOTIFICATION_EXTERNAL_INTERRUPT    = 0x01
EFI_ACPI_5_0_HARDWARE_ERROR_NOTIFICATION_LOCAL_INTERRUPT       = 0x02
EFI_ACPI_5_0_HARDWARE_ERROR_NOTIFICATION_SCI                   = 0x03
EFI_ACPI_5_0_HARDWARE_ERROR_NOTIFICATION_NMI                   = 0x04

EFI_ACPI_5_0_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE = EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE

EFI_ACPI_5_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE = EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE

EFI_ACPI_5_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK_STRUCTURE = EFI_ACPI_4_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK_STRUCTURE

EFI_ACPI_5_0_IA32_ARCHITECTURE_NMI_ERROR_STRUCTURE = EFI_ACPI_4_0_IA32_ARCHITECTURE_NMI_ERROR_STRUCTURE

EFI_ACPI_5_0_PCI_EXPRESS_ROOT_PORT_AER_STRUCTURE = EFI_ACPI_4_0_PCI_EXPRESS_ROOT_PORT_AER_STRUCTURE

EFI_ACPI_5_0_PCI_EXPRESS_DEVICE_AER_STRUCTURE = EFI_ACPI_4_0_PCI_EXPRESS_DEVICE_AER_STRUCTURE

EFI_ACPI_5_0_PCI_EXPRESS_BRIDGE_AER_STRUCTURE = EFI_ACPI_4_0_PCI_EXPRESS_BRIDGE_AER_STRUCTURE

EFI_ACPI_5_0_GENERIC_HARDWARE_ERROR_SOURCE_STRUCTURE = EFI_ACPI_4_0_GENERIC_HARDWARE_ERROR_SOURCE_STRUCTURE

EFI_ACPI_5_0_GENERIC_ERROR_STATUS_STRUCTURE = EFI_ACPI_4_0_GENERIC_ERROR_STATUS_STRUCTURE

EFI_ACPI_5_0_ERROR_RECORD_SERIALIZATION_TABLE_HEADER = EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_HEADER

EFI_ACPI_5_0_ERROR_RECORD_SERIALIZATION_TABLE_REVISION = 0x01

EFI_ACPI_5_0_ERST_BEGIN_WRITE_OPERATION                    = 0x00
EFI_ACPI_5_0_ERST_BEGIN_READ_OPERATION                     = 0x01
EFI_ACPI_5_0_ERST_BEGIN_CLEAR_OPERATION                    = 0x02
EFI_ACPI_5_0_ERST_END_OPERATION                            = 0x03
EFI_ACPI_5_0_ERST_SET_RECORD_OFFSET                        = 0x04
EFI_ACPI_5_0_ERST_EXECUTE_OPERATION                        = 0x05
EFI_ACPI_5_0_ERST_CHECK_BUSY_STATUS                        = 0x06
EFI_ACPI_5_0_ERST_GET_COMMAND_STATUS                       = 0x07
EFI_ACPI_5_0_ERST_GET_RECORD_IDENTIFIER                    = 0x08
EFI_ACPI_5_0_ERST_SET_RECORD_IDENTIFIER                    = 0x09
EFI_ACPI_5_0_ERST_GET_RECORD_COUNT                         = 0x0A
EFI_ACPI_5_0_ERST_BEGIN_DUMMY_WRITE_OPERATION              = 0x0B
EFI_ACPI_5_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE              = 0x0D
EFI_ACPI_5_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE_LENGTH       = 0x0E
EFI_ACPI_5_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE_ATTRIBUTES   = 0x0F

EFI_ACPI_5_0_ERST_STATUS_SUCCESS                           = 0x00
EFI_ACPI_5_0_ERST_STATUS_NOT_ENOUGH_SPACE                  = 0x01
EFI_ACPI_5_0_ERST_STATUS_HARDWARE_NOT_AVAILABLE            = 0x02
EFI_ACPI_5_0_ERST_STATUS_FAILED                            = 0x03
EFI_ACPI_5_0_ERST_STATUS_RECORD_STORE_EMPTY                = 0x04
EFI_ACPI_5_0_ERST_STATUS_RECORD_NOT_FOUND                  = 0x05

EFI_ACPI_5_0_ERST_READ_REGISTER                            = 0x00
EFI_ACPI_5_0_ERST_READ_REGISTER_VALUE                      = 0x01
EFI_ACPI_5_0_ERST_WRITE_REGISTER                           = 0x02
EFI_ACPI_5_0_ERST_WRITE_REGISTER_VALUE                     = 0x03
EFI_ACPI_5_0_ERST_NOOP                                     = 0x04
EFI_ACPI_5_0_ERST_LOAD_VAR1                                = 0x05
EFI_ACPI_5_0_ERST_LOAD_VAR2                                = 0x06
EFI_ACPI_5_0_ERST_STORE_VAR1                               = 0x07
EFI_ACPI_5_0_ERST_ADD                                      = 0x08
EFI_ACPI_5_0_ERST_SUBTRACT                                 = 0x09
EFI_ACPI_5_0_ERST_ADD_VALUE                                = 0x0A
EFI_ACPI_5_0_ERST_SUBTRACT_VALUE                           = 0x0B
EFI_ACPI_5_0_ERST_STALL                                    = 0x0C
EFI_ACPI_5_0_ERST_STALL_WHILE_TRUE                         = 0x0D
EFI_ACPI_5_0_ERST_SKIP_NEXT_INSTRUCTION_IF_TRUE            = 0x0E
EFI_ACPI_5_0_ERST_GOTO                                     = 0x0F
EFI_ACPI_5_0_ERST_SET_SRC_ADDRESS_BASE                     = 0x10
EFI_ACPI_5_0_ERST_SET_DST_ADDRESS_BASE                     = 0x11
EFI_ACPI_5_0_ERST_MOVE_DATA                                = 0x12

EFI_ACPI_5_0_ERST_PRESERVE_REGISTER                        = 0x01

EFI_ACPI_5_0_ERST_SERIALIZATION_INSTRUCTION_ENTRY = EFI_ACPI_4_0_ERST_SERIALIZATION_INSTRUCTION_ENTRY

EFI_ACPI_5_0_ERROR_INJECTION_TABLE_HEADER = EFI_ACPI_4_0_ERROR_INJECTION_TABLE_HEADER

EFI_ACPI_5_0_ERROR_INJECTION_TABLE_REVISION = 0x01

EFI_ACPI_5_0_EINJ_BEGIN_INJECTION_OPERATION                = 0x00
EFI_ACPI_5_0_EINJ_GET_TRIGGER_ERROR_ACTION_TABLE           = 0x01
EFI_ACPI_5_0_EINJ_SET_ERROR_TYPE                           = 0x02
EFI_ACPI_5_0_EINJ_GET_ERROR_TYPE                           = 0x03
EFI_ACPI_5_0_EINJ_END_OPERATION                            = 0x04
EFI_ACPI_5_0_EINJ_EXECUTE_OPERATION                        = 0x05
EFI_ACPI_5_0_EINJ_CHECK_BUSY_STATUS                        = 0x06
EFI_ACPI_5_0_EINJ_GET_COMMAND_STATUS                       = 0x07
EFI_ACPI_5_0_EINJ_TRIGGER_ERROR                            = 0xFF

EFI_ACPI_5_0_EINJ_STATUS_SUCCESS                           = 0x00
EFI_ACPI_5_0_EINJ_STATUS_UNKNOWN_FAILURE                   = 0x01
EFI_ACPI_5_0_EINJ_STATUS_INVALID_ACCESS                    = 0x02

EFI_ACPI_5_0_EINJ_ERROR_PROCESSOR_CORRECTABLE                 = (1 << 0)
EFI_ACPI_5_0_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_NONFATAL      = (1 << 1)
EFI_ACPI_5_0_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_FATAL         = (1 << 2)
EFI_ACPI_5_0_EINJ_ERROR_MEMORY_CORRECTABLE                    = (1 << 3)
EFI_ACPI_5_0_EINJ_ERROR_MEMORY_UNCORRECTABLE_NONFATAL         = (1 << 4)
EFI_ACPI_5_0_EINJ_ERROR_MEMORY_UNCORRECTABLE_FATAL            = (1 << 5)
EFI_ACPI_5_0_EINJ_ERROR_PCI_EXPRESS_CORRECTABLE               = (1 << 6)
EFI_ACPI_5_0_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_NONFATAL    = (1 << 7)
EFI_ACPI_5_0_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_FATAL       = (1 << 8)
EFI_ACPI_5_0_EINJ_ERROR_PLATFORM_CORRECTABLE                  = (1 << 9)
EFI_ACPI_5_0_EINJ_ERROR_PLATFORM_UNCORRECTABLE_NONFATAL       = (1 << 10)
EFI_ACPI_5_0_EINJ_ERROR_PLATFORM_UNCORRECTABLE_FATAL          = (1 << 11)

EFI_ACPI_5_0_EINJ_READ_REGISTER                            = 0x00
EFI_ACPI_5_0_EINJ_READ_REGISTER_VALUE                      = 0x01
EFI_ACPI_5_0_EINJ_WRITE_REGISTER                           = 0x02
EFI_ACPI_5_0_EINJ_WRITE_REGISTER_VALUE                     = 0x03
EFI_ACPI_5_0_EINJ_NOOP                                     = 0x04

EFI_ACPI_5_0_EINJ_PRESERVE_REGISTER                        = 0x01

EFI_ACPI_5_0_EINJ_INJECTION_INSTRUCTION_ENTRY = EFI_ACPI_4_0_EINJ_INJECTION_INSTRUCTION_ENTRY

EFI_ACPI_5_0_EINJ_TRIGGER_ACTION_TABLE = EFI_ACPI_4_0_EINJ_TRIGGER_ACTION_TABLE

class EFI_ACPI_5_0_PLATFORM_COMMUNICATION_CHANNEL_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_ACPI_DESCRIPTION_HEADER),
    ("Flags",     UINT32),
    ("Reserved",  UINT64)
  ]

EFI_ACPI_5_0_PLATFORM_COMMUNICATION_CHANNEL_TABLE_REVISION = 0x01

EFI_ACPI_5_0_PCCT_FLAGS_SCI_DOORBELL                      = BIT0

EFI_ACPI_5_0_PCCT_SUBSPACE_TYPE_GENERIC  = 0x00

class EFI_ACPI_5_0_PCCT_SUBSPACE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8),
    ("Length",  UINT8)
  ]

class EFI_ACPI_5_0_PCCT_SUBSPACE_GENERIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT8),
    ("Length",                        UINT8),
    ("Reserved",                      UINT8 * 6),
    ("BaseAddress",                   UINT64),
    ("AddressLength",                 UINT64),
    ("DoorbellRegister",              EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("DoorbellPreserve",              UINT64),
    ("DoorbellWrite",                 UINT64),
    ("NominalLatency",                UINT32),
    ("MaximumPeriodicAccessRate",     UINT32),
    ("MinimumRequestTurnaroundTime",  UINT16)
  ]

class EFI_ACPI_5_0_PCCT_GENERIC_SHARED_MEMORY_REGION_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Command",     UINT8),
    ("Reserved",    UINT8, 7),
    ("GenerateSci", UINT8, 1)
  ]

class EFI_ACPI_5_0_PCCT_GENERIC_SHARED_MEMORY_REGION_STATUS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CommandComplete",       UINT8, 1),
    ("SciDoorbell",           UINT8, 1),
    ("Error",                 UINT8, 1),
    ("PlatformNotification",  UINT8, 1),
    ("Reserved",              UINT8, 4),
    ("Reserved1",             UINT8)
  ]

class EFI_ACPI_5_0_PCCT_GENERIC_SHARED_MEMORY_REGION_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature", UINT32),
    ("Command",   EFI_ACPI_5_0_PCCT_GENERIC_SHARED_MEMORY_REGION_COMMAND),
    ("Command",   EFI_ACPI_5_0_PCCT_GENERIC_SHARED_MEMORY_REGION_STATUS)
  ]

EFI_ACPI_5_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE  = SIGNATURE_64('R', 'S', 'D', ' ', 'P', 'T', 'R', ' ') 
EFI_ACPI_5_0_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('A', 'P', 'I', 'C')
EFI_ACPI_5_0_BOOT_ERROR_RECORD_TABLE_SIGNATURE  = SIGNATURE_32('B', 'E', 'R', 'T')
EFI_ACPI_5_0_BOOT_GRAPHICS_RESOURCE_TABLE_SIGNATURE  = SIGNATURE_32('B', 'G', 'R', 'T')
EFI_ACPI_5_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE  = SIGNATURE_32('C', 'P', 'E', 'P')
EFI_ACPI_5_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('D', 'S', 'D', 'T')
EFI_ACPI_5_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE  = SIGNATURE_32('E', 'C', 'D', 'T')
EFI_ACPI_5_0_ERROR_INJECTION_TABLE_SIGNATURE  = SIGNATURE_32('E', 'I', 'N', 'J')
EFI_ACPI_5_0_ERROR_RECORD_SERIALIZATION_TABLE_SIGNATURE  = SIGNATURE_32('E', 'R', 'S', 'T')
EFI_ACPI_5_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('F', 'A', 'C', 'P')
EFI_ACPI_5_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE  = SIGNATURE_32('F', 'A', 'C', 'S')
EFI_ACPI_5_0_FIRMWARE_PERFORMANCE_DATA_TABLE_SIGNATURE  = SIGNATURE_32('F', 'P', 'D', 'T')
EFI_ACPI_5_0_GENERIC_TIMER_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('G', 'T', 'D', 'T')
EFI_ACPI_5_0_HARDWARE_ERROR_SOURCE_TABLE_SIGNATURE  = SIGNATURE_32('H', 'E', 'S', 'T')
EFI_ACPI_5_0_MEMORY_POWER_STATE_TABLE_SIGNATURE  = SIGNATURE_32('M', 'P', 'S', 'T')
EFI_ACPI_5_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_SIGNATURE  = SIGNATURE_32('M', 'S', 'C', 'T')
EFI_ACPI_5_0_PLATFORM_MEMORY_TOPOLOGY_TABLE_SIGNATURE  = SIGNATURE_32('P', 'M', 'T', 'T')
EFI_ACPI_5_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('P', 'S', 'D', 'T')
EFI_ACPI_5_0_ACPI_RAS_FEATURE_TABLE_SIGNATURE  = SIGNATURE_32('R', 'A', 'S', 'F')
EFI_ACPI_5_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('R', 'S', 'D', 'T')
EFI_ACPI_5_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'B', 'S', 'T')
EFI_ACPI_5_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'L', 'I', 'T')
EFI_ACPI_5_0_SYSTEM_RESOURCE_AFFINITY_TABLE_SIGNATURE  = SIGNATURE_32('S', 'R', 'A', 'T')
EFI_ACPI_5_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'S', 'D', 'T')
EFI_ACPI_5_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('X', 'S', 'D', 'T')
EFI_ACPI_5_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE  = SIGNATURE_32('B', 'O', 'O', 'T')
EFI_ACPI_5_0_CORE_SYSTEM_RESOURCE_TABLE_SIGNATURE  = SIGNATURE_32('C', 'S', 'R', 'T')
EFI_ACPI_5_0_DEBUG_PORT_2_TABLE_SIGNATURE  = SIGNATURE_32('D', 'B', 'G', '2')
EFI_ACPI_5_0_DEBUG_PORT_TABLE_SIGNATURE  = SIGNATURE_32('D', 'B', 'G', 'P')
EFI_ACPI_5_0_DMA_REMAPPING_TABLE_SIGNATURE  = SIGNATURE_32('D', 'M', 'A', 'R')
EFI_ACPI_5_0_DYNAMIC_ROOT_OF_TRUST_FOR_MEASUREMENT_TABLE_SIGNATURE  = SIGNATURE_32('D', 'R', 'T', 'M')
EFI_ACPI_5_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('E', 'T', 'D', 'T')
EFI_ACPI_5_0_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE  = SIGNATURE_32('H', 'P', 'E', 'T')
EFI_ACPI_5_0_ISCSI_BOOT_FIRMWARE_TABLE_SIGNATURE  = SIGNATURE_32('i', 'B', 'F', 'T')
EFI_ACPI_5_0_IO_VIRTUALIZATION_REPORTING_STRUCTURE_SIGNATURE  = SIGNATURE_32('I', 'V', 'R', 'S')
EFI_ACPI_5_0_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('M', 'C', 'F', 'G')
EFI_ACPI_5_0_MANAGEMENT_CONTROLLER_HOST_INTERFACE_TABLE_SIGNATURE  = SIGNATURE_32('M', 'C', 'H', 'I')
EFI_ACPI_5_0_DATA_MANAGEMENT_TABLE_SIGNATURE  = SIGNATURE_32('M', 'S', 'D', 'M')
EFI_ACPI_5_0_SOFTWARE_LICENSING_TABLE_SIGNATURE  = SIGNATURE_32('S', 'L', 'I', 'C')
EFI_ACPI_5_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'P', 'C', 'R')
EFI_ACPI_5_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE  = SIGNATURE_32('S', 'P', 'M', 'I')
EFI_ACPI_5_0_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE  = SIGNATURE_32('T', 'C', 'P', 'A')
EFI_ACPI_5_0_TRUSTED_COMPUTING_PLATFORM_2_TABLE_SIGNATURE  = SIGNATURE_32('T', 'P', 'M', '2')
EFI_ACPI_5_0_UEFI_ACPI_DATA_TABLE_SIGNATURE  = SIGNATURE_32('U', 'E', 'F', 'I')
EFI_ACPI_5_0_WINDOWS_ACPI_EMULATED_DEVICES_TABLE_SIGNATURE  = SIGNATURE_32('W', 'A', 'E', 'T')
EFI_ACPI_5_0_WATCHDOG_ACTION_TABLE_SIGNATURE  = SIGNATURE_32('W', 'D', 'A', 'T')
EFI_ACPI_5_0_WATCHDOG_RESOURCE_TABLE_SIGNATURE  = SIGNATURE_32('W', 'D', 'R', 'T')
EFI_ACPI_5_0_PLATFORM_BINARY_TABLE_SIGNATURE  = SIGNATURE_32('W', 'P', 'B', 'T')
