#
# PiStatusCode.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PiStatusCode.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol import DebugSupport

EFI_STATUS_CODE_TYPE    = UINT32
EFI_STATUS_CODE_TYPE_MASK     = 0x000000FF
EFI_STATUS_CODE_SEVERITY_MASK = 0xFF000000
EFI_STATUS_CODE_RESERVED_MASK = 0x00FFFF00

EFI_PROGRESS_CODE             = 0x00000001
EFI_ERROR_CODE                = 0x00000002
EFI_DEBUG_CODE                = 0x00000003

EFI_ERROR_MINOR               = 0x40000000
EFI_ERROR_MAJOR               = 0x80000000
EFI_ERROR_UNRECOVERED         = 0x90000000
EFI_ERROR_UNCONTAINED         = 0xa0000000

EFI_STATUS_CODE_VALUE = UINT32

EFI_STATUS_CODE_CLASS_MASK      = 0xFF000000
EFI_STATUS_CODE_SUBCLASS_MASK   = 0x00FF0000
EFI_STATUS_CODE_OPERATION_MASK  = 0x0000FFFF

class EFI_STATUS_CODE_DATA (Structure):
  _fields_ = [
    ("HeaderSize",  UINT16),
    ("Size",        UINT16),
    ("Type",        EFI_GUID)
  ]

EFI_SUBCLASS_SPECIFIC = 0x1000
EFI_OEM_SPECIFIC      = 0x8000

EFI_DC_UNSPECIFIED  = 0x0

EFI_COMPUTING_UNIT  = 0x00000000
EFI_PERIPHERAL      = 0x01000000
EFI_IO_BUS          = 0x02000000
EFI_SOFTWARE        = 0x03000000

EFI_COMPUTING_UNIT_UNSPECIFIED        = (EFI_COMPUTING_UNIT | 0x00000000)
EFI_COMPUTING_UNIT_HOST_PROCESSOR     = (EFI_COMPUTING_UNIT | 0x00010000)
EFI_COMPUTING_UNIT_FIRMWARE_PROCESSOR = (EFI_COMPUTING_UNIT | 0x00020000)
EFI_COMPUTING_UNIT_IO_PROCESSOR       = (EFI_COMPUTING_UNIT | 0x00030000)
EFI_COMPUTING_UNIT_CACHE              = (EFI_COMPUTING_UNIT | 0x00040000)
EFI_COMPUTING_UNIT_MEMORY             = (EFI_COMPUTING_UNIT | 0x00050000)
EFI_COMPUTING_UNIT_CHIPSET            = (EFI_COMPUTING_UNIT | 0x00060000)

EFI_CU_PC_INIT_BEGIN  = 0x00000000
EFI_CU_PC_INIT_END    = 0x00000001

EFI_CU_HP_PC_POWER_ON_INIT          = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_CU_HP_PC_CACHE_INIT             = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_CU_HP_PC_RAM_INIT               = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_CU_HP_PC_MEMORY_CONTROLLER_INIT = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_CU_HP_PC_IO_INIT                = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_CU_HP_PC_BSP_SELECT             = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_CU_HP_PC_BSP_RESELECT           = (EFI_SUBCLASS_SPECIFIC | 0x00000006)
EFI_CU_HP_PC_AP_INIT                = (EFI_SUBCLASS_SPECIFIC | 0x00000007)
EFI_CU_HP_PC_SMM_INIT               = (EFI_SUBCLASS_SPECIFIC | 0x00000008)

EFI_CU_CACHE_PC_PRESENCE_DETECT = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_CU_CACHE_PC_CONFIGURATION   = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_CU_MEMORY_PC_SPD_READ         = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_CU_MEMORY_PC_PRESENCE_DETECT  = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_CU_MEMORY_PC_TIMING           = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_CU_MEMORY_PC_CONFIGURING      = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_CU_MEMORY_PC_OPTIMIZING       = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_CU_MEMORY_PC_INIT             = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_CU_MEMORY_PC_TEST             = (EFI_SUBCLASS_SPECIFIC | 0x00000006)

EFI_CHIPSET_PC_PEI_CAR_SB_INIT      = (EFI_SUBCLASS_SPECIFIC|0x00000000)
EFI_CHIPSET_PC_PEI_CAR_NB_INIT      = (EFI_SUBCLASS_SPECIFIC|0x00000001)
EFI_CHIPSET_PC_PEI_MEM_SB_INIT      = (EFI_SUBCLASS_SPECIFIC|0x00000002)
EFI_CHIPSET_PC_PEI_MEM_NB_INIT      = (EFI_SUBCLASS_SPECIFIC|0x00000003)
EFI_CHIPSET_PC_DXE_HB_INIT          = (EFI_SUBCLASS_SPECIFIC|0x00000004)
EFI_CHIPSET_PC_DXE_NB_INIT          = (EFI_SUBCLASS_SPECIFIC|0x00000005)
EFI_CHIPSET_PC_DXE_NB_SMM_INIT      = (EFI_SUBCLASS_SPECIFIC|0x00000006)
EFI_CHIPSET_PC_DXE_SB_RT_INIT       = (EFI_SUBCLASS_SPECIFIC|0x00000007)
EFI_CHIPSET_PC_DXE_SB_INIT          = (EFI_SUBCLASS_SPECIFIC|0x00000008)
EFI_CHIPSET_PC_DXE_SB_SMM_INIT      = (EFI_SUBCLASS_SPECIFIC|0x00000009)
EFI_CHIPSET_PC_DXE_SB_DEVICES_INIT  = (EFI_SUBCLASS_SPECIFIC|0x0000000a)

EFI_CU_EC_NON_SPECIFIC    = 0x00000000
EFI_CU_EC_DISABLED        = 0x00000001
EFI_CU_EC_NOT_SUPPORTED   = 0x00000002
EFI_CU_EC_NOT_DETECTED    = 0x00000003
EFI_CU_EC_NOT_CONFIGURED  = 0x00000004

EFI_CU_HP_EC_INVALID_TYPE         = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_CU_HP_EC_INVALID_SPEED        = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_CU_HP_EC_MISMATCH             = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_CU_HP_EC_TIMER_EXPIRED        = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_CU_HP_EC_SELF_TEST            = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_CU_HP_EC_INTERNAL             = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_CU_HP_EC_THERMAL              = (EFI_SUBCLASS_SPECIFIC | 0x00000006)
EFI_CU_HP_EC_LOW_VOLTAGE          = (EFI_SUBCLASS_SPECIFIC | 0x00000007)
EFI_CU_HP_EC_HIGH_VOLTAGE         = (EFI_SUBCLASS_SPECIFIC | 0x00000008)
EFI_CU_HP_EC_CACHE                = (EFI_SUBCLASS_SPECIFIC | 0x00000009)
EFI_CU_HP_EC_MICROCODE_UPDATE     = (EFI_SUBCLASS_SPECIFIC | 0x0000000A)
EFI_CU_HP_EC_CORRECTABLE          = (EFI_SUBCLASS_SPECIFIC | 0x0000000B)
EFI_CU_HP_EC_UNCORRECTABLE        = (EFI_SUBCLASS_SPECIFIC | 0x0000000C)
EFI_CU_HP_EC_NO_MICROCODE_UPDATE  = (EFI_SUBCLASS_SPECIFIC | 0x0000000D)

EFI_CU_FP_EC_HARD_FAIL  = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_CU_FP_EC_SOFT_FAIL  = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_CU_FP_EC_COMM_ERROR = (EFI_SUBCLASS_SPECIFIC | 0x00000002)

EFI_CU_CACHE_EC_INVALID_TYPE  = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_CU_CACHE_EC_INVALID_SPEED = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_CU_CACHE_EC_INVALID_SIZE  = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_CU_CACHE_EC_MISMATCH      = (EFI_SUBCLASS_SPECIFIC | 0x00000003)

EFI_CU_MEMORY_EC_INVALID_TYPE   = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_CU_MEMORY_EC_INVALID_SPEED  = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_CU_MEMORY_EC_CORRECTABLE    = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_CU_MEMORY_EC_UNCORRECTABLE  = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_CU_MEMORY_EC_SPD_FAIL       = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_CU_MEMORY_EC_INVALID_SIZE   = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_CU_MEMORY_EC_MISMATCH       = (EFI_SUBCLASS_SPECIFIC | 0x00000006)
EFI_CU_MEMORY_EC_S3_RESUME_FAIL = (EFI_SUBCLASS_SPECIFIC | 0x00000007)
EFI_CU_MEMORY_EC_UPDATE_FAIL    = (EFI_SUBCLASS_SPECIFIC | 0x00000008)
EFI_CU_MEMORY_EC_NONE_DETECTED  = (EFI_SUBCLASS_SPECIFIC | 0x00000009)
EFI_CU_MEMORY_EC_NONE_USEFUL    = (EFI_SUBCLASS_SPECIFIC | 0x0000000A)

EFI_CHIPSET_EC_BAD_BATTERY      = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_CHIPSET_EC_DXE_NB_ERROR     = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_CHIPSET_EC_DXE_SB_ERROR     = (EFI_SUBCLASS_SPECIFIC | 0x00000002)

EFI_PERIPHERAL_UNSPECIFIED      = (EFI_PERIPHERAL | 0x00000000)
EFI_PERIPHERAL_KEYBOARD         = (EFI_PERIPHERAL | 0x00010000)
EFI_PERIPHERAL_MOUSE            = (EFI_PERIPHERAL | 0x00020000)
EFI_PERIPHERAL_LOCAL_CONSOLE    = (EFI_PERIPHERAL | 0x00030000)
EFI_PERIPHERAL_REMOTE_CONSOLE   = (EFI_PERIPHERAL | 0x00040000)
EFI_PERIPHERAL_SERIAL_PORT      = (EFI_PERIPHERAL | 0x00050000)
EFI_PERIPHERAL_PARALLEL_PORT    = (EFI_PERIPHERAL | 0x00060000)
EFI_PERIPHERAL_FIXED_MEDIA      = (EFI_PERIPHERAL | 0x00070000)
EFI_PERIPHERAL_REMOVABLE_MEDIA  = (EFI_PERIPHERAL | 0x00080000)
EFI_PERIPHERAL_AUDIO_INPUT      = (EFI_PERIPHERAL | 0x00090000)
EFI_PERIPHERAL_AUDIO_OUTPUT     = (EFI_PERIPHERAL | 0x000A0000)
EFI_PERIPHERAL_LCD_DEVICE       = (EFI_PERIPHERAL | 0x000B0000)
EFI_PERIPHERAL_NETWORK          = (EFI_PERIPHERAL | 0x000C0000)

EFI_P_PC_INIT             = 0x00000000
EFI_P_PC_RESET            = 0x00000001
EFI_P_PC_DISABLE          = 0x00000002
EFI_P_PC_PRESENCE_DETECT  = 0x00000003
EFI_P_PC_ENABLE           = 0x00000004
EFI_P_PC_RECONFIG         = 0x00000005
EFI_P_PC_DETECTED         = 0x00000006

EFI_P_KEYBOARD_PC_CLEAR_BUFFER  = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_P_KEYBOARD_PC_SELF_TEST     = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_P_MOUSE_PC_SELF_TEST  = (EFI_SUBCLASS_SPECIFIC | 0x00000000)

EFI_P_SERIAL_PORT_PC_CLEAR_BUFFER = (EFI_SUBCLASS_SPECIFIC | 0x00000000)

EFI_P_EC_NON_SPECIFIC       = 0x00000000
EFI_P_EC_DISABLED           = 0x00000001
EFI_P_EC_NOT_SUPPORTED      = 0x00000002
EFI_P_EC_NOT_DETECTED       = 0x00000003
EFI_P_EC_NOT_CONFIGURED     = 0x00000004
EFI_P_EC_INTERFACE_ERROR    = 0x00000005
EFI_P_EC_CONTROLLER_ERROR   = 0x00000006
EFI_P_EC_INPUT_ERROR        = 0x00000007
EFI_P_EC_OUTPUT_ERROR       = 0x00000008
EFI_P_EC_RESOURCE_CONFLICT  = 0x00000009

EFI_P_KEYBOARD_EC_LOCKED    = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_P_KEYBOARD_EC_STUCK_KEY = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_P_MOUSE_EC_LOCKED = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_IO_BUS_UNSPECIFIED  = (EFI_IO_BUS | 0x00000000)
EFI_IO_BUS_PCI          = (EFI_IO_BUS | 0x00010000)
EFI_IO_BUS_USB          = (EFI_IO_BUS | 0x00020000)
EFI_IO_BUS_IBA          = (EFI_IO_BUS | 0x00030000)
EFI_IO_BUS_AGP          = (EFI_IO_BUS | 0x00040000)
EFI_IO_BUS_PC_CARD      = (EFI_IO_BUS | 0x00050000)
EFI_IO_BUS_LPC          = (EFI_IO_BUS | 0x00060000)
EFI_IO_BUS_SCSI         = (EFI_IO_BUS | 0x00070000)
EFI_IO_BUS_ATA_ATAPI    = (EFI_IO_BUS | 0x00080000)
EFI_IO_BUS_FC           = (EFI_IO_BUS | 0x00090000)
EFI_IO_BUS_IP_NETWORK   = (EFI_IO_BUS | 0x000A0000)
EFI_IO_BUS_SMBUS        = (EFI_IO_BUS | 0x000B0000)
EFI_IO_BUS_I2C          = (EFI_IO_BUS | 0x000C0000)

EFI_IOB_PC_INIT     = 0x00000000
EFI_IOB_PC_RESET    = 0x00000001
EFI_IOB_PC_DISABLE  = 0x00000002
EFI_IOB_PC_DETECT   = 0x00000003
EFI_IOB_PC_ENABLE   = 0x00000004
EFI_IOB_PC_RECONFIG = 0x00000005
EFI_IOB_PC_HOTPLUG  = 0x00000006

EFI_IOB_PCI_BUS_ENUM   = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_IOB_PCI_RES_ALLOC  = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_IOB_PCI_HPC_INIT   = (EFI_SUBCLASS_SPECIFIC | 0x00000002)

EFI_IOB_ATA_BUS_SMART_ENABLE          = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_IOB_ATA_BUS_SMART_DISABLE         = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_IOB_ATA_BUS_SMART_OVERTHRESHOLD   = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_IOB_ATA_BUS_SMART_UNDERTHRESHOLD  = (EFI_SUBCLASS_SPECIFIC | 0x00000003)

EFI_IOB_EC_NON_SPECIFIC       = 0x00000000
EFI_IOB_EC_DISABLED           = 0x00000001
EFI_IOB_EC_NOT_SUPPORTED      = 0x00000002
EFI_IOB_EC_NOT_DETECTED       = 0x00000003
EFI_IOB_EC_NOT_CONFIGURED     = 0x00000004
EFI_IOB_EC_INTERFACE_ERROR    = 0x00000005
EFI_IOB_EC_CONTROLLER_ERROR   = 0x00000006
EFI_IOB_EC_READ_ERROR         = 0x00000007
EFI_IOB_EC_WRITE_ERROR        = 0x00000008
EFI_IOB_EC_RESOURCE_CONFLICT  = 0x00000009

EFI_IOB_PCI_EC_PERR = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_IOB_PCI_EC_SERR = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_IOB_ATA_BUS_SMART_NOTSUPPORTED  = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_IOB_ATA_BUS_SMART_DISABLED      = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_SOFTWARE_UNSPECIFIED          = (EFI_SOFTWARE | 0x00000000)
EFI_SOFTWARE_SEC                  = (EFI_SOFTWARE | 0x00010000)
EFI_SOFTWARE_PEI_CORE             = (EFI_SOFTWARE | 0x00020000)
EFI_SOFTWARE_PEI_MODULE           = (EFI_SOFTWARE | 0x00030000)
EFI_SOFTWARE_DXE_CORE             = (EFI_SOFTWARE | 0x00040000)
EFI_SOFTWARE_DXE_BS_DRIVER        = (EFI_SOFTWARE | 0x00050000)
EFI_SOFTWARE_DXE_RT_DRIVER        = (EFI_SOFTWARE | 0x00060000)
EFI_SOFTWARE_SMM_DRIVER           = (EFI_SOFTWARE | 0x00070000)
EFI_SOFTWARE_EFI_APPLICATION      = (EFI_SOFTWARE | 0x00080000)
EFI_SOFTWARE_EFI_OS_LOADER        = (EFI_SOFTWARE | 0x00090000)
EFI_SOFTWARE_RT                   = (EFI_SOFTWARE | 0x000A0000)
EFI_SOFTWARE_AL                   = (EFI_SOFTWARE | 0x000B0000)
EFI_SOFTWARE_EBC_EXCEPTION        = (EFI_SOFTWARE | 0x000C0000)
EFI_SOFTWARE_IA32_EXCEPTION       = (EFI_SOFTWARE | 0x000D0000)
EFI_SOFTWARE_IPF_EXCEPTION        = (EFI_SOFTWARE | 0x000E0000)
EFI_SOFTWARE_PEI_SERVICE          = (EFI_SOFTWARE | 0x000F0000)
EFI_SOFTWARE_EFI_BOOT_SERVICE     = (EFI_SOFTWARE | 0x00100000)
EFI_SOFTWARE_EFI_RUNTIME_SERVICE  = (EFI_SOFTWARE | 0x00110000)
EFI_SOFTWARE_EFI_DXE_SERVICE      = (EFI_SOFTWARE | 0x00120000)
EFI_SOFTWARE_X64_EXCEPTION        = (EFI_SOFTWARE | 0x00130000)
EFI_SOFTWARE_ARM_EXCEPTION        = (EFI_SOFTWARE | 0x00140000)

EFI_SW_PC_INIT                = 0x00000000
EFI_SW_PC_LOAD                = 0x00000001
EFI_SW_PC_INIT_BEGIN          = 0x00000002
EFI_SW_PC_INIT_END            = 0x00000003
EFI_SW_PC_AUTHENTICATE_BEGIN  = 0x00000004
EFI_SW_PC_AUTHENTICATE_END    = 0x00000005
EFI_SW_PC_INPUT_WAIT          = 0x00000006
EFI_SW_PC_USER_SETUP          = 0x00000007

EFI_SW_SEC_PC_ENTRY_POINT     = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_SEC_PC_HANDOFF_TO_NEXT = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_SW_PEI_CORE_PC_ENTRY_POINT      = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_PEI_CORE_PC_HANDOFF_TO_NEXT  = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_PEI_CORE_PC_RETURN_TO_LAST   = (EFI_SUBCLASS_SPECIFIC | 0x00000002)

EFI_SW_PEI_PC_RECOVERY_BEGIN  = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_PEI_PC_CAPSULE_LOAD    = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_PEI_PC_CAPSULE_START   = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_PEI_PC_RECOVERY_USER   = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_PEI_PC_RECOVERY_AUTO   = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_SW_PEI_PC_S3_BOOT_SCRIPT  = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_SW_PEI_PC_OS_WAKE         = (EFI_SUBCLASS_SPECIFIC | 0x00000006)

EFI_SW_DXE_CORE_PC_ENTRY_POINT      = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_DXE_CORE_PC_HANDOFF_TO_NEXT  = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_DXE_CORE_PC_RETURN_TO_LAST   = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_DXE_CORE_PC_START_DRIVER     = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_DXE_CORE_PC_ARCH_READY       = (EFI_SUBCLASS_SPECIFIC | 0x00000004)

EFI_SW_DXE_BS_PC_LEGACY_OPROM_INIT            = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_DXE_BS_PC_READY_TO_BOOT_EVENT          = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_DXE_BS_PC_LEGACY_BOOT_EVENT            = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_DXE_BS_PC_EXIT_BOOT_SERVICES_EVENT     = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_DXE_BS_PC_VIRTUAL_ADDRESS_CHANGE_EVENT = (EFI_SUBCLASS_SPECIFIC | 0x00000004)

EFI_SW_RT_PC_ENTRY_POINT      = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_RT_PC_HANDOFF_TO_NEXT  = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_RT_PC_RETURN_TO_LAST   = (EFI_SUBCLASS_SPECIFIC | 0x00000002)

EFI_SW_PS_PC_INSTALL_PPI              = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_PS_PC_REINSTALL_PPI            = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_PS_PC_LOCATE_PPI               = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_PS_PC_NOTIFY_PPI               = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_PS_PC_GET_BOOT_MODE            = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_SW_PS_PC_SET_BOOT_MODE            = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_SW_PS_PC_GET_HOB_LIST             = (EFI_SUBCLASS_SPECIFIC | 0x00000006)
EFI_SW_PS_PC_CREATE_HOB               = (EFI_SUBCLASS_SPECIFIC | 0x00000007)
EFI_SW_PS_PC_FFS_FIND_NEXT_VOLUME     = (EFI_SUBCLASS_SPECIFIC | 0x00000008)
EFI_SW_PS_PC_FFS_FIND_NEXT_FILE       = (EFI_SUBCLASS_SPECIFIC | 0x00000009)
EFI_SW_PS_PC_FFS_FIND_SECTION_DATA    = (EFI_SUBCLASS_SPECIFIC | 0x0000000A)
EFI_SW_PS_PC_INSTALL_PEI_MEMORY       = (EFI_SUBCLASS_SPECIFIC | 0x0000000B)
EFI_SW_PS_PC_ALLOCATE_PAGES           = (EFI_SUBCLASS_SPECIFIC | 0x0000000C)
EFI_SW_PS_PC_ALLOCATE_POOL            = (EFI_SUBCLASS_SPECIFIC | 0x0000000D)
EFI_SW_PS_PC_COPY_MEM                 = (EFI_SUBCLASS_SPECIFIC | 0x0000000E)
EFI_SW_PS_PC_SET_MEM                  = (EFI_SUBCLASS_SPECIFIC | 0x0000000F)
EFI_SW_PS_PC_RESET_SYSTEM             = (EFI_SUBCLASS_SPECIFIC | 0x00000010)
EFI_SW_PS_PC_FFS_FIND_FILE_BY_NAME    = (EFI_SUBCLASS_SPECIFIC | 0x00000013)
EFI_SW_PS_PC_FFS_GET_FILE_INFO        = (EFI_SUBCLASS_SPECIFIC | 0x00000014)
EFI_SW_PS_PC_FFS_GET_VOLUME_INFO      = (EFI_SUBCLASS_SPECIFIC | 0x00000015)
EFI_SW_PS_PC_FFS_REGISTER_FOR_SHADOW  = (EFI_SUBCLASS_SPECIFIC | 0x00000016)

EFI_SW_BS_PC_RAISE_TPL                      = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_BS_PC_RESTORE_TPL                    = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_BS_PC_ALLOCATE_PAGES                 = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_BS_PC_FREE_PAGES                     = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_BS_PC_GET_MEMORY_MAP                 = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_SW_BS_PC_ALLOCATE_POOL                  = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_SW_BS_PC_FREE_POOL                      = (EFI_SUBCLASS_SPECIFIC | 0x00000006)
EFI_SW_BS_PC_CREATE_EVENT                   = (EFI_SUBCLASS_SPECIFIC | 0x00000007)
EFI_SW_BS_PC_SET_TIMER                      = (EFI_SUBCLASS_SPECIFIC | 0x00000008)
EFI_SW_BS_PC_WAIT_FOR_EVENT                 = (EFI_SUBCLASS_SPECIFIC | 0x00000009)
EFI_SW_BS_PC_SIGNAL_EVENT                   = (EFI_SUBCLASS_SPECIFIC | 0x0000000A)
EFI_SW_BS_PC_CLOSE_EVENT                    = (EFI_SUBCLASS_SPECIFIC | 0x0000000B)
EFI_SW_BS_PC_CHECK_EVENT                    = (EFI_SUBCLASS_SPECIFIC | 0x0000000C)
EFI_SW_BS_PC_INSTALL_PROTOCOL_INTERFACE     = (EFI_SUBCLASS_SPECIFIC | 0x0000000D)
EFI_SW_BS_PC_REINSTALL_PROTOCOL_INTERFACE   = (EFI_SUBCLASS_SPECIFIC | 0x0000000E)
EFI_SW_BS_PC_UNINSTALL_PROTOCOL_INTERFACE   = (EFI_SUBCLASS_SPECIFIC | 0x0000000F)
EFI_SW_BS_PC_HANDLE_PROTOCOL                = (EFI_SUBCLASS_SPECIFIC | 0x00000010)
EFI_SW_BS_PC_PC_HANDLE_PROTOCOL             = (EFI_SUBCLASS_SPECIFIC | 0x00000011)
EFI_SW_BS_PC_REGISTER_PROTOCOL_NOTIFY       = (EFI_SUBCLASS_SPECIFIC | 0x00000012)
EFI_SW_BS_PC_LOCATE_HANDLE                  = (EFI_SUBCLASS_SPECIFIC | 0x00000013)
EFI_SW_BS_PC_INSTALL_CONFIGURATION_TABLE    = (EFI_SUBCLASS_SPECIFIC | 0x00000014)
EFI_SW_BS_PC_LOAD_IMAGE                     = (EFI_SUBCLASS_SPECIFIC | 0x00000015)
EFI_SW_BS_PC_START_IMAGE                    = (EFI_SUBCLASS_SPECIFIC | 0x00000016)
EFI_SW_BS_PC_EXIT                           = (EFI_SUBCLASS_SPECIFIC | 0x00000017)
EFI_SW_BS_PC_UNLOAD_IMAGE                   = (EFI_SUBCLASS_SPECIFIC | 0x00000018)
EFI_SW_BS_PC_EXIT_BOOT_SERVICES             = (EFI_SUBCLASS_SPECIFIC | 0x00000019)
EFI_SW_BS_PC_GET_NEXT_MONOTONIC_COUNT       = (EFI_SUBCLASS_SPECIFIC | 0x0000001A)
EFI_SW_BS_PC_STALL                          = (EFI_SUBCLASS_SPECIFIC | 0x0000001B)
EFI_SW_BS_PC_SET_WATCHDOG_TIMER             = (EFI_SUBCLASS_SPECIFIC | 0x0000001C)
EFI_SW_BS_PC_CONNECT_CONTROLLER             = (EFI_SUBCLASS_SPECIFIC | 0x0000001D)
EFI_SW_BS_PC_DISCONNECT_CONTROLLER          = (EFI_SUBCLASS_SPECIFIC | 0x0000001E)
EFI_SW_BS_PC_OPEN_PROTOCOL                  = (EFI_SUBCLASS_SPECIFIC | 0x0000001F)
EFI_SW_BS_PC_CLOSE_PROTOCOL                 = (EFI_SUBCLASS_SPECIFIC | 0x00000020)
EFI_SW_BS_PC_OPEN_PROTOCOL_INFORMATION      = (EFI_SUBCLASS_SPECIFIC | 0x00000021)
EFI_SW_BS_PC_PROTOCOLS_PER_HANDLE           = (EFI_SUBCLASS_SPECIFIC | 0x00000022)
EFI_SW_BS_PC_LOCATE_HANDLE_BUFFER           = (EFI_SUBCLASS_SPECIFIC | 0x00000023)
EFI_SW_BS_PC_LOCATE_PROTOCOL                = (EFI_SUBCLASS_SPECIFIC | 0x00000024)
EFI_SW_BS_PC_INSTALL_MULTIPLE_INTERFACES    = (EFI_SUBCLASS_SPECIFIC | 0x00000025)
EFI_SW_BS_PC_UNINSTALL_MULTIPLE_INTERFACES  = (EFI_SUBCLASS_SPECIFIC | 0x00000026)
EFI_SW_BS_PC_CALCULATE_CRC_32               = (EFI_SUBCLASS_SPECIFIC | 0x00000027)
EFI_SW_BS_PC_COPY_MEM                       = (EFI_SUBCLASS_SPECIFIC | 0x00000028)
EFI_SW_BS_PC_SET_MEM                        = (EFI_SUBCLASS_SPECIFIC | 0x00000029)
EFI_SW_BS_PC_CREATE_EVENT_EX                = (EFI_SUBCLASS_SPECIFIC | 0x0000002A)

EFI_SW_RS_PC_GET_TIME                       = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_RS_PC_SET_TIME                       = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_RS_PC_GET_WAKEUP_TIME                = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_RS_PC_SET_WAKEUP_TIME                = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_RS_PC_SET_VIRTUAL_ADDRESS_MAP        = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_SW_RS_PC_CONVERT_POINTER                = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_SW_RS_PC_GET_VARIABLE                   = (EFI_SUBCLASS_SPECIFIC | 0x00000006)
EFI_SW_RS_PC_GET_NEXT_VARIABLE_NAME         = (EFI_SUBCLASS_SPECIFIC | 0x00000007)
EFI_SW_RS_PC_SET_VARIABLE                   = (EFI_SUBCLASS_SPECIFIC | 0x00000008)
EFI_SW_RS_PC_GET_NEXT_HIGH_MONOTONIC_COUNT  = (EFI_SUBCLASS_SPECIFIC | 0x00000009)
EFI_SW_RS_PC_RESET_SYSTEM                   = (EFI_SUBCLASS_SPECIFIC | 0x0000000A)
EFI_SW_RS_PC_UPDATE_CAPSULE                 = (EFI_SUBCLASS_SPECIFIC | 0x0000000B)
EFI_SW_RS_PC_QUERY_CAPSULE_CAPABILITIES     = (EFI_SUBCLASS_SPECIFIC | 0x0000000C)
EFI_SW_RS_PC_QUERY_VARIABLE_INFO            = (EFI_SUBCLASS_SPECIFIC | 0x0000000D)

EFI_SW_DS_PC_ADD_MEMORY_SPACE             = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_DS_PC_ALLOCATE_MEMORY_SPACE        = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_DS_PC_FREE_MEMORY_SPACE            = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_DS_PC_REMOVE_MEMORY_SPACE          = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_DS_PC_GET_MEMORY_SPACE_DESCRIPTOR  = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_SW_DS_PC_SET_MEMORY_SPACE_ATTRIBUTES  = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_SW_DS_PC_GET_MEMORY_SPACE_MAP         = (EFI_SUBCLASS_SPECIFIC | 0x00000006)
EFI_SW_DS_PC_ADD_IO_SPACE                 = (EFI_SUBCLASS_SPECIFIC | 0x00000007)
EFI_SW_DS_PC_ALLOCATE_IO_SPACE            = (EFI_SUBCLASS_SPECIFIC | 0x00000008)
EFI_SW_DS_PC_FREE_IO_SPACE                = (EFI_SUBCLASS_SPECIFIC | 0x00000009)
EFI_SW_DS_PC_REMOVE_IO_SPACE              = (EFI_SUBCLASS_SPECIFIC | 0x0000000A)
EFI_SW_DS_PC_GET_IO_SPACE_DESCRIPTOR      = (EFI_SUBCLASS_SPECIFIC | 0x0000000B)
EFI_SW_DS_PC_GET_IO_SPACE_MAP             = (EFI_SUBCLASS_SPECIFIC | 0x0000000C)
EFI_SW_DS_PC_DISPATCH                     = (EFI_SUBCLASS_SPECIFIC | 0x0000000D)
EFI_SW_DS_PC_SCHEDULE                     = (EFI_SUBCLASS_SPECIFIC | 0x0000000E)
EFI_SW_DS_PC_TRUST                        = (EFI_SUBCLASS_SPECIFIC | 0x0000000F)
EFI_SW_DS_PC_PROCESS_FIRMWARE_VOLUME      = (EFI_SUBCLASS_SPECIFIC | 0x00000010)

EFI_SW_EC_NON_SPECIFIC            = 0x00000000
EFI_SW_EC_LOAD_ERROR              = 0x00000001
EFI_SW_EC_INVALID_PARAMETER       = 0x00000002
EFI_SW_EC_UNSUPPORTED             = 0x00000003
EFI_SW_EC_INVALID_BUFFER          = 0x00000004
EFI_SW_EC_OUT_OF_RESOURCES        = 0x00000005
EFI_SW_EC_ABORTED                 = 0x00000006
EFI_SW_EC_ILLEGAL_SOFTWARE_STATE  = 0x00000007
EFI_SW_EC_ILLEGAL_HARDWARE_STATE  = 0x00000008
EFI_SW_EC_START_ERROR             = 0x00000009
EFI_SW_EC_BAD_DATE_TIME           = 0x0000000A
EFI_SW_EC_CFG_INVALID             = 0x0000000B
EFI_SW_EC_CFG_CLR_REQUEST         = 0x0000000C
EFI_SW_EC_CFG_DEFAULT             = 0x0000000D
EFI_SW_EC_PWD_INVALID             = 0x0000000E
EFI_SW_EC_PWD_CLR_REQUEST         = 0x0000000F
EFI_SW_EC_PWD_CLEARED             = 0x00000010
EFI_SW_EC_EVENT_LOG_FULL          = 0x00000011

EFI_SW_PEI_CORE_EC_DXE_CORRUPT           = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_PEI_CORE_EC_DXEIPL_NOT_FOUND      = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_PEI_CORE_EC_MEMORY_NOT_INSTALLED  = (EFI_SUBCLASS_SPECIFIC | 0x00000002)

EFI_SW_PEI_EC_NO_RECOVERY_CAPSULE          = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_PEI_EC_INVALID_CAPSULE_DESCRIPTOR   = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_PEI_EC_S3_RESUME_PPI_NOT_FOUND      = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_PEI_EC_S3_BOOT_SCRIPT_ERROR         = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_PEI_EC_S3_OS_WAKE_ERROR             = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_SW_PEI_EC_S3_RESUME_FAILED             = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_SW_PEI_EC_RECOVERY_PPI_NOT_FOUND       = (EFI_SUBCLASS_SPECIFIC | 0x00000006)
EFI_SW_PEI_EC_RECOVERY_FAILED              = (EFI_SUBCLASS_SPECIFIC | 0x00000007)

EFI_SW_DXE_CORE_EC_NO_ARCH                = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_DXE_BS_EC_LEGACY_OPROM_NO_SPACE   = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_DXE_BS_EC_INVALID_PASSWORD        = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_DXE_BS_EC_BOOT_OPTION_LOAD_ERROR  = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_DXE_BS_EC_BOOT_OPTION_FAILED      = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_DXE_BS_EC_INVALID_IDE_PASSWORD    = (EFI_SUBCLASS_SPECIFIC | 0x00000004)

EFI_SW_EC_EBC_UNDEFINED             = 0x00000000
EFI_SW_EC_EBC_DIVIDE_ERROR          = DebugSupport.EXCEPT_EBC_DIVIDE_ERROR
EFI_SW_EC_EBC_DEBUG                 = DebugSupport.EXCEPT_EBC_DEBUG
EFI_SW_EC_EBC_BREAKPOINT            = DebugSupport.EXCEPT_EBC_BREAKPOINT
EFI_SW_EC_EBC_OVERFLOW              = DebugSupport.EXCEPT_EBC_OVERFLOW
EFI_SW_EC_EBC_INVALID_OPCODE        = DebugSupport.EXCEPT_EBC_INVALID_OPCODE
EFI_SW_EC_EBC_STACK_FAULT           = DebugSupport.EXCEPT_EBC_STACK_FAULT
EFI_SW_EC_EBC_ALIGNMENT_CHECK       = DebugSupport.EXCEPT_EBC_ALIGNMENT_CHECK
EFI_SW_EC_EBC_INSTRUCTION_ENCODING  = DebugSupport.EXCEPT_EBC_INSTRUCTION_ENCODING
EFI_SW_EC_EBC_BAD_BREAK             = DebugSupport.EXCEPT_EBC_BAD_BREAK
EFI_SW_EC_EBC_STEP                  = DebugSupport.EXCEPT_EBC_STEP

EFI_SW_EC_IA32_DIVIDE_ERROR     = DebugSupport.EXCEPT_IA32_DIVIDE_ERROR
EFI_SW_EC_IA32_DEBUG            = DebugSupport.EXCEPT_IA32_DEBUG
EFI_SW_EC_IA32_NMI              = DebugSupport.EXCEPT_IA32_NMI
EFI_SW_EC_IA32_BREAKPOINT       = DebugSupport.EXCEPT_IA32_BREAKPOINT
EFI_SW_EC_IA32_OVERFLOW         = DebugSupport.EXCEPT_IA32_OVERFLOW
EFI_SW_EC_IA32_BOUND            = DebugSupport.EXCEPT_IA32_BOUND
EFI_SW_EC_IA32_INVALID_OPCODE   = DebugSupport.EXCEPT_IA32_INVALID_OPCODE
EFI_SW_EC_IA32_DOUBLE_FAULT     = DebugSupport.EXCEPT_IA32_DOUBLE_FAULT
EFI_SW_EC_IA32_INVALID_TSS      = DebugSupport.EXCEPT_IA32_INVALID_TSS
EFI_SW_EC_IA32_SEG_NOT_PRESENT  = DebugSupport.EXCEPT_IA32_SEG_NOT_PRESENT
EFI_SW_EC_IA32_STACK_FAULT      = DebugSupport.EXCEPT_IA32_STACK_FAULT
EFI_SW_EC_IA32_GP_FAULT         = DebugSupport.EXCEPT_IA32_GP_FAULT
EFI_SW_EC_IA32_PAGE_FAULT       = DebugSupport.EXCEPT_IA32_PAGE_FAULT
EFI_SW_EC_IA32_FP_ERROR         = DebugSupport.EXCEPT_IA32_FP_ERROR
EFI_SW_EC_IA32_ALIGNMENT_CHECK  = DebugSupport.EXCEPT_IA32_ALIGNMENT_CHECK
EFI_SW_EC_IA32_MACHINE_CHECK    = DebugSupport.EXCEPT_IA32_MACHINE_CHECK
EFI_SW_EC_IA32_SIMD             = DebugSupport.EXCEPT_IA32_SIMD

#BUGBUG EFI_SW_EC_IPF_ALT_DTLB            = DebugSupport.EXCEPT_IPF_ALT_DTLB
#BUGBUG EFI_SW_EC_IPF_DNESTED_TLB         = DebugSupport.EXCEPT_IPF_DNESTED_TLB
#BUGBUG EFI_SW_EC_IPF_BREAKPOINT          = DebugSupport.EXCEPT_IPF_BREAKPOINT
#BUGBUG EFI_SW_EC_IPF_EXTERNAL_INTERRUPT  = DebugSupport.EXCEPT_IPF_EXTERNAL_INTERRUPT
#BUGBUG EFI_SW_EC_IPF_GEN_EXCEPT          = DebugSupport.EXCEPT_IPF_GEN_EXCEPT
#BUGBUG EFI_SW_EC_IPF_NAT_CONSUMPTION     = DebugSupport.EXCEPT_IPF_NAT_CONSUMPTION
#BUGBUG EFI_SW_EC_IPF_DEBUG_EXCEPT        = DebugSupport.EXCEPT_IPF_DEBUG_EXCEPT
#BUGBUG EFI_SW_EC_IPF_UNALIGNED_ACCESS    = DebugSupport.EXCEPT_IPF_UNALIGNED_ACCESS
#BUGBUG EFI_SW_EC_IPF_FP_FAULT            = DebugSupport.EXCEPT_IPF_FP_FAULT
#BUGBUG EFI_SW_EC_IPF_FP_TRAP             = DebugSupport.EXCEPT_IPF_FP_TRAP
#BUGBUG EFI_SW_EC_IPF_TAKEN_BRANCH        = DebugSupport.EXCEPT_IPF_TAKEN_BRANCH
#BUGBUG EFI_SW_EC_IPF_SINGLE_STEP         = DebugSupport.EXCEPT_IPF_SINGLE_STEP

EFI_SW_PS_EC_RESET_NOT_AVAILABLE     = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_PS_EC_MEMORY_INSTALLED_TWICE  = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_SW_DXE_BS_PC_BEGIN_CONNECTING_DRIVERS   = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_SW_DXE_BS_PC_VERIFYING_PASSWORD         = (EFI_SUBCLASS_SPECIFIC | 0x00000006)

EFI_SW_DXE_RT_PC_S0                         = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_DXE_RT_PC_S1                         = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_DXE_RT_PC_S2                         = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_DXE_RT_PC_S3                         = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_DXE_RT_PC_S4                         = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_SW_DXE_RT_PC_S5                         = (EFI_SUBCLASS_SPECIFIC | 0x00000005)

EFI_SW_EC_X64_DIVIDE_ERROR                   = DebugSupport.EXCEPT_X64_DIVIDE_ERROR
EFI_SW_EC_X64_DEBUG                          = DebugSupport.EXCEPT_X64_DEBUG
EFI_SW_EC_X64_NMI                            = DebugSupport.EXCEPT_X64_NMI
EFI_SW_EC_X64_BREAKPOINT                     = DebugSupport.EXCEPT_X64_BREAKPOINT
EFI_SW_EC_X64_OVERFLOW                       = DebugSupport.EXCEPT_X64_OVERFLOW
EFI_SW_EC_X64_BOUND                          = DebugSupport.EXCEPT_X64_BOUND
EFI_SW_EC_X64_INVALID_OPCODE                 = DebugSupport.EXCEPT_X64_INVALID_OPCODE
EFI_SW_EC_X64_DOUBLE_FAULT                   = DebugSupport.EXCEPT_X64_DOUBLE_FAULT
EFI_SW_EC_X64_INVALID_TSS                    = DebugSupport.EXCEPT_X64_INVALID_TSS
EFI_SW_EC_X64_SEG_NOT_PRESENT                = DebugSupport.EXCEPT_X64_SEG_NOT_PRESENT
EFI_SW_EC_X64_STACK_FAULT                    = DebugSupport.EXCEPT_X64_STACK_FAULT
EFI_SW_EC_X64_GP_FAULT                       = DebugSupport.EXCEPT_X64_GP_FAULT
EFI_SW_EC_X64_PAGE_FAULT                     = DebugSupport.EXCEPT_X64_PAGE_FAULT
EFI_SW_EC_X64_FP_ERROR                       = DebugSupport.EXCEPT_X64_FP_ERROR
EFI_SW_EC_X64_ALIGNMENT_CHECK                = DebugSupport.EXCEPT_X64_ALIGNMENT_CHECK
EFI_SW_EC_X64_MACHINE_CHECK                  = DebugSupport.EXCEPT_X64_MACHINE_CHECK
EFI_SW_EC_X64_SIMD                           = DebugSupport.EXCEPT_X64_SIMD

EFI_SW_EC_ARM_RESET                          = DebugSupport.EXCEPT_ARM_RESET 
EFI_SW_EC_ARM_UNDEFINED_INSTRUCTION          = DebugSupport.EXCEPT_ARM_UNDEFINED_INSTRUCTION 
EFI_SW_EC_ARM_SOFTWARE_INTERRUPT             = DebugSupport.EXCEPT_ARM_SOFTWARE_INTERRUPT 
EFI_SW_EC_ARM_PREFETCH_ABORT                 = DebugSupport.EXCEPT_ARM_PREFETCH_ABORT
EFI_SW_EC_ARM_DATA_ABORT                     = DebugSupport.EXCEPT_ARM_DATA_ABORT
EFI_SW_EC_ARM_RESERVED                       = DebugSupport.EXCEPT_ARM_RESERVED
EFI_SW_EC_ARM_IRQ                            = DebugSupport.EXCEPT_ARM_IRQ
EFI_SW_EC_ARM_FIQ                            = DebugSupport.EXCEPT_ARM_FIQ

