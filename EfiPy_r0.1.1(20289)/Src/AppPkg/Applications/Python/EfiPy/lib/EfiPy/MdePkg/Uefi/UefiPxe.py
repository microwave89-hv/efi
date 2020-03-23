#
# UefiPxe.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UefiPxe.py is free software: you can redistribute it and/or
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

PXE_PVOID   = PVOID
PXE_UINT8   = UINT8
PXE_UINT16  = UINT16
PXE_UINT32  = UINT32
PXE_UINTN   = UINTN
PXE_UINT64  = UINT64
PXE_BOOL    = PXE_UINT8

def PXE_BUSTYPE(a, b, c, d):

  if type(a) is str:
    a = ord (a)

  if type(b) is str:
    b = ord (b)

  if type(c) is str:
    c = ord (c)

  if type(d) is str:
    d = ord (d)

  return ((d & 0xFF) << 24) | ((c & 0xFF) << 16) | ((b & 0xFF) << 8) | (a & 0xFF)

PXE_BUSTYPE_PXE = PXE_BUSTYPE ('!', 'P', 'X', 'E')

PXE_BUSTYPE_PCI     = PXE_BUSTYPE ('P', 'C', 'I', 'R')
PXE_BUSTYPE_PC_CARD = PXE_BUSTYPE ('P', 'C', 'C', 'R')
PXE_BUSTYPE_USB     = PXE_BUSTYPE ('U', 'S', 'B', 'R')
PXE_BUSTYPE_1394    = PXE_BUSTYPE ('1', '3', '9', '4')

def PXE_SWAP_UINT16(n):
  return ((n & 0x00FF) << 8) | ((n & 0xFF00) >> 8)


def PXE_SWAP_UINT32(n):
  return ((n & 0x000000FFL) << 24) | \
         ((n & 0x0000FF00L) << 8)  | \
         ((n & 0x00FF0000L) >> 8)  | \
         ((n & 0xFF000000L) >> 24)


def PXE_SWAP_UINT64(n):
 return ((n & 0x00000000000000FFL) << 56) | \
        ((n & 0x000000000000FF00L) << 40) | \
        ((n & 0x0000000000FF0000L) << 24) | \
        ((n & 0x00000000FF000000L) << 8)  | \
        ((n & 0x000000FF00000000L) >> 8)  | \
        ((n & 0x0000FF0000000000L) >> 24) | \
        ((n & 0x00FF000000000000L) >> 40) | \
        ((n & 0xFF00000000000000L) >> 56)

PXE_CPBSIZE_NOT_USED  = 0
PXE_DBSIZE_NOT_USED   = 0
PXE_CPBADDR_NOT_USED  = 0
PXE_DBADDR_NOT_USED   = 0

PXE_FALSE = 0
PXE_TRUE  = 1
PXE_OPCODE  = PXE_UINT16
PXE_OPCODE_GET_STATE  = 0x0000
PXE_OPCODE_START  = 0x0001
PXE_OPCODE_STOP = 0x0002
PXE_OPCODE_GET_INIT_INFO  = 0x0003
PXE_OPCODE_GET_CONFIG_INFO  = 0x0004
PXE_OPCODE_INITIALIZE = 0x0005
PXE_OPCODE_RESET  = 0x0006
PXE_OPCODE_SHUTDOWN = 0x0007
PXE_OPCODE_INTERRUPT_ENABLES  = 0x0008
PXE_OPCODE_RECEIVE_FILTERS  = 0x0009
PXE_OPCODE_STATION_ADDRESS  = 0x000A
PXE_OPCODE_STATISTICS = 0x000B
PXE_OPCODE_MCAST_IP_TO_MAC  = 0x000C
PXE_OPCODE_NVDATA = 0x000D
PXE_OPCODE_GET_STATUS = 0x000E
PXE_OPCODE_FILL_HEADER  = 0x000F
PXE_OPCODE_TRANSMIT = 0x0010
PXE_OPCODE_RECEIVE  = 0x0011
PXE_OPCODE_LAST_VALID = 0x0011
PXE_OPFLAGS = PXE_UINT16
PXE_OPFLAGS_NOT_USED  = 0x0000

PXE_OPFLAGS_INITIALIZE_CABLE_DETECT_MASK    = 0x0001
PXE_OPFLAGS_INITIALIZE_DETECT_CABLE         = 0x0000
PXE_OPFLAGS_INITIALIZE_DO_NOT_DETECT_CABLE  = 0x0001

PXE_OPFLAGS_RESET_DISABLE_INTERRUPTS  = 0x0001
PXE_OPFLAGS_RESET_DISABLE_FILTERS     = 0x0002

PXE_OPFLAGS_INTERRUPT_OPMASK  = 0xC000
PXE_OPFLAGS_INTERRUPT_ENABLE  = 0x8000
PXE_OPFLAGS_INTERRUPT_DISABLE = 0x4000
PXE_OPFLAGS_INTERRUPT_READ    = 0x0000

PXE_OPFLAGS_INTERRUPT_RECEIVE = 0x0001
PXE_OPFLAGS_INTERRUPT_TRANSMIT  = 0x0002
PXE_OPFLAGS_INTERRUPT_COMMAND = 0x0004
PXE_OPFLAGS_INTERRUPT_SOFTWARE  = 0x0008

PXE_OPFLAGS_RECEIVE_FILTER_OPMASK   = 0xC000
PXE_OPFLAGS_RECEIVE_FILTER_ENABLE   = 0x8000
PXE_OPFLAGS_RECEIVE_FILTER_DISABLE  = 0x4000
PXE_OPFLAGS_RECEIVE_FILTER_READ     = 0x0000

PXE_OPFLAGS_RECEIVE_FILTER_RESET_MCAST_LIST = 0x2000
PXE_OPFLAGS_RECEIVE_FILTER_UNICAST  = 0x0001
PXE_OPFLAGS_RECEIVE_FILTER_BROADCAST  = 0x0002
PXE_OPFLAGS_RECEIVE_FILTER_FILTERED_MULTICAST = 0x0004
PXE_OPFLAGS_RECEIVE_FILTER_PROMISCUOUS  = 0x0008
PXE_OPFLAGS_RECEIVE_FILTER_ALL_MULTICAST  = 0x0010

PXE_OPFLAGS_STATION_ADDRESS_READ   = 0x0000
PXE_OPFLAGS_STATION_ADDRESS_WRITE  = 0x0000
PXE_OPFLAGS_STATION_ADDRESS_RESET  = 0x0001

PXE_OPFLAGS_STATISTICS_READ   = 0x0000
PXE_OPFLAGS_STATISTICS_RESET  = 0x0001

PXE_OPFLAGS_MCAST_IP_TO_MAC_OPMASK  = 0x0003
PXE_OPFLAGS_MCAST_IPV4_TO_MAC       = 0x0000
PXE_OPFLAGS_MCAST_IPV6_TO_MAC       = 0x0001

PXE_OPFLAGS_NVDATA_OPMASK = 0x0001
PXE_OPFLAGS_NVDATA_READ   = 0x0000
PXE_OPFLAGS_NVDATA_WRITE  = 0x0001

PXE_OPFLAGS_GET_INTERRUPT_STATUS  = 0x0001
PXE_OPFLAGS_GET_TRANSMITTED_BUFFERS = 0x0002
PXE_OPFLAGS_GET_MEDIA_STATUS    = 0x0004

PXE_OPFLAGS_FILL_HEADER_OPMASK      = 0x0001
PXE_OPFLAGS_FILL_HEADER_FRAGMENTED  = 0x0001
PXE_OPFLAGS_FILL_HEADER_WHOLE       = 0x0000

PXE_OPFLAGS_SWUNDI_TRANSMIT_OPMASK  = 0x0001
PXE_OPFLAGS_TRANSMIT_BLOCK          = 0x0001
PXE_OPFLAGS_TRANSMIT_DONT_BLOCK     = 0x0000

PXE_OPFLAGS_TRANSMIT_OPMASK     = 0x0002
PXE_OPFLAGS_TRANSMIT_FRAGMENTED = 0x0002
PXE_OPFLAGS_TRANSMIT_WHOLE      = 0x0000

PXE_STATFLAGS = PXE_UINT16
PXE_STATFLAGS_INITIALIZE  = 0x0000

PXE_STATFLAGS_STATUS_MASK       = 0xC000
PXE_STATFLAGS_COMMAND_COMPLETE  = 0xC000
PXE_STATFLAGS_COMMAND_FAILED    = 0x8000
PXE_STATFLAGS_COMMAND_QUEUED    = 0x4000

PXE_STATFLAGS_GET_STATE_MASK        = 0x0003
PXE_STATFLAGS_GET_STATE_INITIALIZED = 0x0002
PXE_STATFLAGS_GET_STATE_STARTED     = 0x0001
PXE_STATFLAGS_GET_STATE_STOPPED     = 0x0000

PXE_STATFLAGS_CABLE_DETECT_MASK           = 0x0001
PXE_STATFLAGS_CABLE_DETECT_NOT_SUPPORTED  = 0x0000
PXE_STATFLAGS_CABLE_DETECT_SUPPORTED      = 0x0001

PXE_STATFLAGS_GET_STATUS_NO_MEDIA_MASK           = 0x0002
PXE_STATFLAGS_GET_STATUS_NO_MEDIA_NOT_SUPPORTED  = 0x0000
PXE_STATFLAGS_GET_STATUS_NO_MEDIA_SUPPORTED      = 0x0002

PXE_STATFLAGS_INITIALIZED_NO_MEDIA  = 0x0001

PXE_STATFLAGS_RESET_NO_MEDIA  = 0x0001

PXE_STATFLAGS_INTERRUPT_RECEIVE = 0x0001
PXE_STATFLAGS_INTERRUPT_TRANSMIT  = 0x0002
PXE_STATFLAGS_INTERRUPT_COMMAND = 0x0004
PXE_STATFLAGS_RECEIVE_FILTER_UNICAST  = 0x0001
PXE_STATFLAGS_RECEIVE_FILTER_BROADCAST  = 0x0002
PXE_STATFLAGS_RECEIVE_FILTER_FILTERED_MULTICAST = 0x0004
PXE_STATFLAGS_RECEIVE_FILTER_PROMISCUOUS  = 0x0008
PXE_STATFLAGS_RECEIVE_FILTER_ALL_MULTICAST  = 0x0010

PXE_STATFLAGS_GET_STATUS_INTERRUPT_MASK = 0x000F
PXE_STATFLAGS_GET_STATUS_NO_INTERRUPTS  = 0x0000
PXE_STATFLAGS_GET_STATUS_RECEIVE  = 0x0001
PXE_STATFLAGS_GET_STATUS_TRANSMIT = 0x0002
PXE_STATFLAGS_GET_STATUS_COMMAND  = 0x0004
PXE_STATFLAGS_GET_STATUS_SOFTWARE = 0x0008
PXE_STATFLAGS_GET_STATUS_TXBUF_QUEUE_EMPTY  = 0x0010
PXE_STATFLAGS_GET_STATUS_NO_TXBUFS_WRITTEN  = 0x0020
PXE_STATFLAGS_GET_STATUS_NO_MEDIA  = 0x0040

PXE_STATCODE  = PXE_UINT16
PXE_STATCODE_INITIALIZE = 0x0000

PXE_STATCODE_SUCCESS              = 0x0000
PXE_STATCODE_INVALID_CDB          = 0x0001
PXE_STATCODE_INVALID_CPB          = 0x0002
PXE_STATCODE_BUSY                 = 0x0003
PXE_STATCODE_QUEUE_FULL           = 0x0004
PXE_STATCODE_ALREADY_STARTED      = 0x0005
PXE_STATCODE_NOT_STARTED          = 0x0006
PXE_STATCODE_NOT_SHUTDOWN         = 0x0007
PXE_STATCODE_ALREADY_INITIALIZED  = 0x0008
PXE_STATCODE_NOT_INITIALIZED      = 0x0009
PXE_STATCODE_DEVICE_FAILURE       = 0x000A
PXE_STATCODE_NVDATA_FAILURE       = 0x000B
PXE_STATCODE_UNSUPPORTED          = 0x000C
PXE_STATCODE_BUFFER_FULL          = 0x000D
PXE_STATCODE_INVALID_PARAMETER    = 0x000E
PXE_STATCODE_INVALID_UNDI         = 0x000F
PXE_STATCODE_IPV4_NOT_SUPPORTED   = 0x0010
PXE_STATCODE_IPV6_NOT_SUPPORTED   = 0x0011
PXE_STATCODE_NOT_ENOUGH_MEMORY    = 0x0012
PXE_STATCODE_NO_DATA              = 0x0013

PXE_IFNUM = PXE_UINT16
PXE_IFNUM_START = 0x0000

PXE_IFNUM_INVALID = 0x0000

PXE_CONTROL = PXE_UINT16

PXE_CONTROL_QUEUE_IF_BUSY = 0x0002

PXE_CONTROL_LINK              = 0x0001
PXE_CONTROL_LAST_CDB_IN_LIST  = 0x0000

PXE_FRAME_TYPE  = PXE_UINT8
PXE_FRAME_TYPE_NONE                     = 0x00
PXE_FRAME_TYPE_UNICAST                  = 0x01
PXE_FRAME_TYPE_BROADCAST                = 0x02
PXE_FRAME_TYPE_FILTERED_MULTICAST       = 0x03
PXE_FRAME_TYPE_PROMISCUOUS              = 0x04
PXE_FRAME_TYPE_PROMISCUOUS_MULTICAST    = 0x05

PXE_FRAME_TYPE_MULTICAST                = PXE_FRAME_TYPE_FILTERED_MULTICAST
PXE_IPV4  = PXE_UINT32
PXE_IPV6  = PXE_UINT32 * 4
PXE_MAC_LENGTH  = 32
PXE_MAC_ADDR    = PXE_UINT8 * PXE_MAC_LENGTH
PXE_IFTYPE      = PXE_UINT8
PXE_MEDIA_PROTOCOL  = UINT16

PXE_IFTYPE_ETHERNET       = 0x01
PXE_IFTYPE_TOKENRING      = 0x04
PXE_IFTYPE_FIBRE_CHANNEL  = 0x12

class PXE_HW_UNDI (Structure):
  _pack_   = 1
  _fields_ = [
    ("Signature",       PXE_UINT32),
    ("Len",             PXE_UINT8),
    ("Fudge",           PXE_UINT8),
    ("Rev",             PXE_UINT8),
    ("IFcnt",           PXE_UINT8),
    ("MajorVer",        PXE_UINT8),
    ("MinorVer",        PXE_UINT8),
    ("IFcntExt",        PXE_UINT8),
    ("reserved",        PXE_UINT8),
    ("Implementation",  PXE_UINT32)
  ]

PXE_HWSTAT_STATE_MASK   = 0xC0000000
PXE_HWSTAT_BUSY         = 0xC0000000
PXE_HWSTAT_INITIALIZED  = 0x80000000
PXE_HWSTAT_STARTED      = 0x40000000
PXE_HWSTAT_STOPPED      = 0x00000000

PXE_HWSTAT_COMMAND_FAILED = 0x20000000

PXE_HWSTAT_PROMISCUOUS_MULTICAST_RX_ENABLED = 0x00001000
PXE_HWSTAT_PROMISCUOUS_RX_ENABLED           = 0x00000800
PXE_HWSTAT_BROADCAST_RX_ENABLED             = 0x00000400
PXE_HWSTAT_MULTICAST_RX_ENABLED             = 0x00000200
PXE_HWSTAT_UNICAST_RX_ENABLED               = 0x00000100

PXE_HWSTAT_SOFTWARE_INT_ENABLED     = 0x00000080
PXE_HWSTAT_TX_COMPLETE_INT_ENABLED  = 0x00000040
PXE_HWSTAT_PACKET_RX_INT_ENABLED    = 0x00000020
PXE_HWSTAT_CMD_COMPLETE_INT_ENABLED = 0x00000010

PXE_HWSTAT_SOFTWARE_INT_PENDING     = 0x00000008
PXE_HWSTAT_TX_COMPLETE_INT_PENDING  = 0x00000004
PXE_HWSTAT_PACKET_RX_INT_PENDING    = 0x00000002
PXE_HWSTAT_CMD_COMPLETE_INT_PENDING = 0x00000001

PXE_HWCMD_ISSUE_COMMAND   = 0x80000000
PXE_HWCMD_INTS_AND_FILTS  = 0x00000000

PXE_HWCMD_PROMISCUOUS_MULTICAST_RX_ENABLE = 0x00001000
PXE_HWCMD_PROMISCUOUS_RX_ENABLE           = 0x00000800
PXE_HWCMD_BROADCAST_RX_ENABLE             = 0x00000400
PXE_HWCMD_MULTICAST_RX_ENABLE             = 0x00000200
PXE_HWCMD_UNICAST_RX_ENABLE               = 0x00000100

PXE_HWCMD_SOFTWARE_INT_ENABLE     = 0x00000080
PXE_HWCMD_TX_COMPLETE_INT_ENABLE  = 0x00000040
PXE_HWCMD_PACKET_RX_INT_ENABLE    = 0x00000020
PXE_HWCMD_CMD_COMPLETE_INT_ENABLE = 0x00000010

PXE_HWCMD_CLEAR_SOFTWARE_INT      = 0x00000008
PXE_HWCMD_CLEAR_TX_COMPLETE_INT   = 0x00000004
PXE_HWCMD_CLEAR_PACKET_RX_INT     = 0x00000002
PXE_HWCMD_CLEAR_CMD_COMPLETE_INT  = 0x00000001

class PXE_SW_UNDI (Structure):
  _pack_   = 1
  _fields_ = [
    ("Signature",       PXE_UINT32),
    ("Len",             PXE_UINT8),
    ("Fudge",           PXE_UINT8),
    ("Rev",             PXE_UINT8),
    ("IFcnt",           PXE_UINT8),
    ("MajorVer",        PXE_UINT8),
    ("MinorVer",        PXE_UINT8),
    ("IFcntExt",        PXE_UINT8),
    ("reserved1",       PXE_UINT8),
    ("Implementation",  PXE_UINT32),
    ("EntryPoint",      PXE_UINT64),
    ("reserved2",       PXE_UINT8 * 3),
    ("BusCnt",          PXE_UINT8),
    ("BusType",         PXE_UINT32 * 1)
  ]

class PXE_UNDI (Union):
  _pack_   = 1
  _fields_ = [
    ("hw",  PXE_HW_UNDI),
    ("sw",  PXE_SW_UNDI)
  ]

PXE_ROMID_SIGNATURE = PXE_BUSTYPE ('!', 'P', 'X', 'E')

PXE_ROMID_REV = 0x02

PXE_ROMID_MAJORVER    = 0x03
PXE_ROMID_MINORVER    = 0x01

PXE_ROMID_IMP_HW_UNDI                             = 0x80000000
PXE_ROMID_IMP_SW_VIRT_ADDR                        = 0x40000000
PXE_ROMID_IMP_64BIT_DEVICE                        = 0x00010000
PXE_ROMID_IMP_FRAG_SUPPORTED                      = 0x00008000
PXE_ROMID_IMP_CMD_LINK_SUPPORTED                  = 0x00004000
PXE_ROMID_IMP_CMD_QUEUE_SUPPORTED                 = 0x00002000
PXE_ROMID_IMP_MULTI_FRAME_SUPPORTED               = 0x00001000
PXE_ROMID_IMP_NVDATA_SUPPORT_MASK                 = 0x00000C00
PXE_ROMID_IMP_NVDATA_BULK_WRITABLE                = 0x00000C00
PXE_ROMID_IMP_NVDATA_SPARSE_WRITABLE              = 0x00000800
PXE_ROMID_IMP_NVDATA_READ_ONLY                    = 0x00000400
PXE_ROMID_IMP_NVDATA_NOT_AVAILABLE                = 0x00000000
PXE_ROMID_IMP_STATISTICS_SUPPORTED                = 0x00000200
PXE_ROMID_IMP_STATION_ADDR_SETTABLE               = 0x00000100
PXE_ROMID_IMP_PROMISCUOUS_MULTICAST_RX_SUPPORTED  = 0x00000080
PXE_ROMID_IMP_PROMISCUOUS_RX_SUPPORTED            = 0x00000040
PXE_ROMID_IMP_BROADCAST_RX_SUPPORTED              = 0x00000020
PXE_ROMID_IMP_FILTERED_MULTICAST_RX_SUPPORTED     = 0x00000010
PXE_ROMID_IMP_SOFTWARE_INT_SUPPORTED              = 0x00000008
PXE_ROMID_IMP_TX_COMPLETE_INT_SUPPORTED           = 0x00000004
PXE_ROMID_IMP_PACKET_RX_INT_SUPPORTED             = 0x00000002
PXE_ROMID_IMP_CMD_COMPLETE_INT_SUPPORTED          = 0x00000001

class PXE_CDB (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",    PXE_OPCODE),
    ("OpFlags",   PXE_OPFLAGS),
    ("CPBsize",   PXE_UINT16),
    ("DBsize",    PXE_UINT16),
    ("CPBaddr",   PXE_UINT64),
    ("DBaddr",    PXE_UINT64),
    ("StatCode",  PXE_STATCODE),
    ("StatFlags", PXE_STATFLAGS),
    ("IFnum",     PXE_UINT16),
    ("Control",   PXE_CONTROL)
  ]

class PXE_IP_ADDR (Union):
  _pack_   = 1
  _fields_ = [
    ("IPv6",  PXE_IPV6),
    ("IPv4",  PXE_IPV4)
  ]

class PXE_DEVICE_Union_P (Structure):
  _pack_   = 1
  _fields_ = [
    ("BusType",   PXE_UINT32),
    ("Bus",       PXE_UINT16),
    ("Device",    PXE_UINT8),
    ("Function",  PXE_UINT8)
  ]

class PXE_DEVICE (Union):
  _pack_   = 1
  _fields_ = [
    ("PCI",  PXE_DEVICE_Union_P),
    ("PCC",  PXE_DEVICE_Union_P)
  ]

MAX_PCI_CONFIG_LEN    = 64
MAX_EEPROM_LEN        = 128
MAX_XMIT_BUFFERS      = 32
MAX_MCAST_ADDRESS_CNT = 8

class PXE_CPB_START_30 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Delay",     UINT64),
    ("Block",     UINT64),
    ("Virt2Phys", UINT64),
    ("Mem_IO",    UINT64)
  ]

class PXE_CPB_START_31 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Delay",     UINT64),
    ("Block",     UINT64),
    ("Virt2Phys", UINT64),
    ("Mem_IO",    UINT64),
    ("Map_Mem",   UINT64),
    ("UnMap_Mem", UINT64),
    ("Sync_Mem",  UINT64),
    ("Unique_ID", UINT64)
  ]

TO_AND_FROM_DEVICE    = 0
FROM_DEVICE           = 1
TO_DEVICE             = 2

PXE_DELAY_MILLISECOND = 1000
PXE_DELAY_SECOND      = 1000000
PXE_IO_READ           = 0
PXE_IO_WRITE          = 1
PXE_MEM_READ          = 2
PXE_MEM_WRITE         = 4

class PXE_DB_GET_INIT_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("MemoryRequired",          PXE_UINT32),
    ("FrameDataLen",            PXE_UINT32),
    ("LinkSpeeds",              PXE_UINT32 * 4),
    ("NvCount",                 PXE_UINT32),
    ("NvWidth",                 PXE_UINT16),
    ("MediaHeaderLen",          PXE_UINT16),
    ("HWaddrLen",               PXE_UINT16),
    ("MCastFilterCnt",          PXE_UINT16),
    ("TxBufCnt",                PXE_UINT16),
    ("TxBufSize",               PXE_UINT16),
    ("RxBufCnt",                PXE_UINT16),
    ("RxBufSize",               PXE_UINT16),
    ("IFtype",                  PXE_UINT8),
    ("SupportedDuplexModes",    PXE_UINT8),
    ("SupportedLoopBackModes",  PXE_UINT8)
  ]

PXE_MAX_TXRX_UNIT_ETHER           = 1500

PXE_HWADDR_LEN_ETHER              = 0x0006
PXE_MAC_HEADER_LEN_ETHER          = 0x000E

PXE_DUPLEX_ENABLE_FULL_SUPPORTED  = 1
PXE_DUPLEX_FORCE_FULL_SUPPORTED   = 2

PXE_LOOPBACK_INTERNAL_SUPPORTED   = 1
PXE_LOOPBACK_EXTERNAL_SUPPORTED   = 2

class PXE_PCI_CONFIG_INFO_Config (Union):
  _pack_   = 1
  _fields_ = [
    ("Byte",  UINT8  * 256),
    ("Word",  UINT16 * 128),
    ("Dword", UINT32 * 64)
  ]

class PXE_PCI_CONFIG_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("BusType",   UINT32),
    ("Bus",       UINT16),
    ("Device",    UINT8),
    ("Function",  UINT8),
    ("Config",    PXE_PCI_CONFIG_INFO_Config)
  ]

class PXE_PCC_CONFIG_INFO_Config (Union):
  _pack_   = 1
  _fields_ = [
    ("Byte",  PXE_UINT8  * 256),
    ("Word",  PXE_UINT16 * 128),
    ("Dword", PXE_UINT32 * 64)
  ]

class PXE_PCC_CONFIG_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("BusType",   PXE_UINT32),
    ("Bus",       PXE_UINT16),
    ("Device",    PXE_UINT8),
    ("Function",  PXE_UINT8),
    ("Config",    PXE_PCC_CONFIG_INFO_Config)
  ]

class PXE_DB_GET_CONFIG_INFO (Union):
  _pack_   = 1
  _fields_ = [
    ("pci",  PXE_PCI_CONFIG_INFO),
    ("pcc",  PXE_PCC_CONFIG_INFO)
  ]

class PXE_CPB_INITIALIZE (Structure):
  _pack_   = 1
  _fields_ = [
    ("MemoryAddr",    PXE_UINT64),
    ("MemoryLength",  PXE_UINT32),
    ("LinkSpeed",     PXE_UINT32),
    ("TxBufCnt",      PXE_UINT16),
    ("TxBufSize",     PXE_UINT16),
    ("RxBufCnt",      PXE_UINT16),
    ("RxBufSize",     PXE_UINT16),
    ("DuplexMode",    PXE_UINT8),
    ("LoopBackMode",  PXE_UINT8)
  ]

PXE_DUPLEX_DEFAULT      = 0x00
PXE_FORCE_FULL_DUPLEX   = 0x01
PXE_ENABLE_FULL_DUPLEX  = 0x02
PXE_FORCE_HALF_DUPLEX   = 0x04
PXE_DISABLE_FULL_DUPLEX = 0x08

LOOPBACK_NORMAL         = 0
LOOPBACK_INTERNAL       = 1
LOOPBACK_EXTERNAL       = 2

class PXE_DB_INITIALIZE (Structure):
  _pack_   = 1
  _fields_ = [
    ("MemoryUsed",  PXE_UINT32),
    ("TxBufCnt",    PXE_UINT16),
    ("TxBufSize",   PXE_UINT16),
    ("RxBufCnt",    PXE_UINT16),
    ("RxBufSize",   PXE_UINT16)
  ]

class PXE_CPB_RECEIVE_FILTERS (Structure):
  _pack_   = 1
  _fields_ = [
    ("MCastList",  PXE_MAC_ADDR * MAX_MCAST_ADDRESS_CNT)
  ]

class PXE_DB_RECEIVE_FILTERS (Structure):
  _pack_   = 1
  _fields_ = [
    ("MCastList",  PXE_MAC_ADDR * MAX_MCAST_ADDRESS_CNT)
  ]

class PXE_CPB_STATION_ADDRESS (Structure):
  _pack_   = 1
  _fields_ = [
    ("StationAddr",  PXE_MAC_ADDR)
  ]

class PXE_DB_STATION_ADDRESS (Structure):
  _pack_   = 1
  _fields_ = [
    ("StationAddr",   PXE_MAC_ADDR),
    ("BroadcastAddr", PXE_MAC_ADDR),
    ("PermanentAddr", PXE_MAC_ADDR)
  ]

class PXE_DB_STATISTICS (Structure):
  _pack_   = 1
  _fields_ = [
    ("Supported", PXE_UINT64),
    ("Data",      PXE_UINT64 * 64)
  ]

PXE_STATISTICS_RX_TOTAL_FRAMES  = 0x00
PXE_STATISTICS_RX_GOOD_FRAMES = 0x01
PXE_STATISTICS_RX_UNDERSIZE_FRAMES  = 0x02
PXE_STATISTICS_RX_OVERSIZE_FRAMES = 0x03
PXE_STATISTICS_RX_DROPPED_FRAMES  = 0x04
PXE_STATISTICS_RX_UNICAST_FRAMES  = 0x05
PXE_STATISTICS_RX_BROADCAST_FRAMES  = 0x06
PXE_STATISTICS_RX_MULTICAST_FRAMES  = 0x07
PXE_STATISTICS_RX_CRC_ERROR_FRAMES  = 0x08
PXE_STATISTICS_RX_TOTAL_BYTES = 0x09

PXE_STATISTICS_TX_TOTAL_FRAMES      = 0x0A
PXE_STATISTICS_TX_GOOD_FRAMES       = 0x0B
PXE_STATISTICS_TX_UNDERSIZE_FRAMES  = 0x0C
PXE_STATISTICS_TX_OVERSIZE_FRAMES   = 0x0D
PXE_STATISTICS_TX_DROPPED_FRAMES    = 0x0E
PXE_STATISTICS_TX_UNICAST_FRAMES    = 0x0F
PXE_STATISTICS_TX_BROADCAST_FRAMES  = 0x10
PXE_STATISTICS_TX_MULTICAST_FRAMES  = 0x11
PXE_STATISTICS_TX_CRC_ERROR_FRAMES  = 0x12
PXE_STATISTICS_TX_TOTAL_BYTES       = 0x13
PXE_STATISTICS_COLLISIONS = 0x14
PXE_STATISTICS_UNSUPPORTED_PROTOCOL = 0x15

class PXE_CPB_MCAST_IP_TO_MAC (Structure):
  _pack_   = 1
  _fields_ = [
    ("IP", PXE_IP_ADDR)
  ]

class PXE_DB_MCAST_IP_TO_MAC (Structure):
  _pack_   = 1
  _fields_ = [
    ("MAC", PXE_MAC_ADDR)
  ]

class PXE_CPB_NVDATA_SPARSE_Item_Data (Union):
  _pack_   = 1
  _fields_ = [
    ("Byte",  PXE_UINT8),
    ("Word",  PXE_UINT16),
    ("Dword", PXE_UINT32)
  ]

class PXE_CPB_NVDATA_SPARSE_Item (Structure):
  _pack_   = 1
  _fields_ = [
    ("Addr", PXE_UINT32),
    ("Data", PXE_CPB_NVDATA_SPARSE_Item_Data)
  ]

class PXE_CPB_NVDATA_SPARSE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Item", PXE_CPB_NVDATA_SPARSE_Item * MAX_EEPROM_LEN)
  ]

class PXE_CPB_NVDATA_BULK (Union):
  _pack_   = 1
  _fields_ = [
    ("Byte",  PXE_UINT8  * (MAX_EEPROM_LEN << 2)),
    ("Word",  PXE_UINT16 * (MAX_EEPROM_LEN << 1)),
    ("Dword", PXE_UINT32 * (MAX_EEPROM_LEN))
  ]

class PXE_DB_NVDATA_Data (Union):
  _pack_   = 1
  _fields_ = [
    ("Byte",  PXE_UINT8  * (MAX_EEPROM_LEN << 2)),
    ("Word",  PXE_UINT16 * (MAX_EEPROM_LEN << 1)),
    ("Dword", PXE_UINT32 * (MAX_EEPROM_LEN))
  ]

class PXE_DB_NVDATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("Data",  PXE_DB_NVDATA_Data)
  ]

class PXE_DB_GET_STATUS (Structure):
  _pack_   = 1
  _fields_ = [
    ("RxFrameLen",  PXE_UINT32),
    ("reserved",    PXE_UINT32),
    ("TxBuffer",    PXE_UINT64 * MAX_XMIT_BUFFERS),
  ]

class PXE_CPB_FILL_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("SrcAddr",         PXE_MAC_ADDR),
    ("DestAddr",        PXE_MAC_ADDR),
    ("MediaHeader",     PXE_UINT64),
    ("PacketLen",       PXE_UINT32),
    ("Protocol",        PXE_UINT16),
    ("MediaHeaderLen",  PXE_UINT16)
  ]

PXE_PROTOCOL_ETHERNET_IP  = 0x0800
PXE_PROTOCOL_ETHERNET_ARP = 0x0806
MAX_XMIT_FRAGMENTS        = 16

class PXE_CPB_FILL_HEADER_FRAGMENTED_FragDesc (Structure):
  _pack_   = 1
  _fields_ = [
    ("FragAddr",  PXE_UINT64),
    ("FragLen",   PXE_UINT32),
    ("reserved",  PXE_UINT32)
  ]

class PXE_CPB_FILL_HEADER_FRAGMENTED (Structure):
  _pack_   = 1
  _fields_ = [
    ("SrcAddr",         PXE_MAC_ADDR),
    ("DestAddr",        PXE_MAC_ADDR),
    ("PacketLen",       PXE_UINT32),
    ("Protocol",        PXE_MEDIA_PROTOCOL),
    ("MediaHeaderLen",  PXE_UINT16),
    ("FragCnt",         PXE_UINT16),
    ("reserved",        PXE_UINT16),
    ("FragDesc",        PXE_CPB_FILL_HEADER_FRAGMENTED_FragDesc * MAX_XMIT_FRAGMENTS)
  ]

class PXE_CPB_TRANSMIT (Structure):
  _pack_   = 1
  _fields_ = [
    ("FrameAddr",       PXE_UINT64),
    ("DataLen",         PXE_UINT32),
    ("MediaheaderLen",  PXE_UINT16),
    ("reserved",        PXE_UINT16)
  ]

class PXE_CPB_TRANSMIT_FRAGMENTS_FragDesc (Structure):
  _pack_   = 1
  _fields_ = [
    ("FragAddr",  PXE_UINT64),
    ("FragLen",   PXE_UINT32),
    ("reserved",  PXE_UINT32)
  ]

class PXE_CPB_TRANSMIT_FRAGMENTS (Structure):
  _pack_   = 1
  _fields_ = [
    ("FrameLen",        PXE_UINT32),
    ("MediaheaderLen",  PXE_UINT16),
    ("FragCnt",         PXE_UINT16),
    ("FragDesc",        PXE_CPB_TRANSMIT_FRAGMENTS_FragDesc * MAX_XMIT_FRAGMENTS)
  ]

class PXE_CPB_RECEIVE (Structure):
  _pack_   = 1
  _fields_ = [
    ("BufferAddr",  PXE_UINT64),
    ("BufferLen",   PXE_UINT32),
    ("reserved",    PXE_UINT32)
  ]

class PXE_DB_RECEIVE (Structure):
  _pack_   = 1
  _fields_ = [
    ("SrcAddr",         PXE_MAC_ADDR),
    ("DestAddr",        PXE_MAC_ADDR),
    ("FrameLen",        PXE_UINT32),
    ("Protocol",        PXE_MEDIA_PROTOCOL),
    ("MediaHeaderLen",  PXE_UINT16),
    ("Type",            PXE_FRAME_TYPE),
    ("reserved",        PXE_UINT8 * 7)
  ]

