#
# TrEEProtocol.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# TrEEProtocol.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard      import UefiTcgPlatform
from EfiPy.MdePkg.IndustryStandard      import Tpm20

gEfiTrEEProtocolGuid    = \
  EFI_GUID (0x607f766c, 0x7455, 0x42be, (0x93, 0x0b, 0xe4, 0xd7, 0x6d, 0xb2, 0x72, 0x0f))

class EFI_TREE_PROTOCOL (Structure):
  pass

class TREE_VERSION (Structure):
  _fields_ = [
    ("Major",     UINT8),
    ("Minor",     UINT8)
  ]

TREE_EVENT_LOG_BITMAP = UINT32
TREE_EVENT_LOG_FORMAT = UINT32

TREE_EVENT_LOG_FORMAT_TCG_1_2       = 0x00000001

class TREE_BOOT_SERVICE_CAPABILITY_1_0 (Structure):
  _fields_ = [
    ("Size",                UINT8),
    ("StructureVersion",    TREE_VERSION),
    ("ProtocolVersion",     TREE_VERSION),
    ("HashAlgorithmBitmap", UINT32),
    ("SupportedEventLogs",  TREE_EVENT_LOG_BITMAP),
    ("TrEEPresentFlag",     BOOLEAN),
    ("MaxCommandSize",      UINT16),
    ("MaxResponseSize",     UINT16),
    ("ManufacturerID",      UINT32)
  ]

TREE_BOOT_SERVICE_CAPABILITY  = TREE_BOOT_SERVICE_CAPABILITY_1_0
TREE_BOOT_HASH_ALG_SHA1   = 0x00000001
TREE_BOOT_HASH_ALG_SHA256 = 0x00000002
TREE_BOOT_HASH_ALG_SHA384 = 0x00000004
TREE_BOOT_HASH_ALG_SHA512 = 0x00000008

TREE_EXTEND_ONLY  = 0x0000000000000001
PE_COFF_IMAGE     = 0x0000000000000010
EV_EFI_VARIABLE_AUTHORITY     = 0x800000E0

FIRMWARE_DEBUGGER_EVENT_STRING  = "UEFI Debug Mode"
class EFI_VARIABLE_DATA_TREE (Structure):
  _pack_   = 1
  _fields_ = [
    ("VariableName",        EFI_GUID),
    ("UnicodeNameLength",   UINT64),
    ("VariableDataLength",  UINT64),
    ("UnicodeName",         CHAR16 * 1),
    ("VariableData",        INT8 * 1)
  ]

TrEE_PCRINDEX   = UINT32
TrEE_EVENTTYPE  = UINT32

MAX_PCR_INDEX  = 23
TREE_EVENT_HEADER_VERSION  = 1

class TrEE_EVENT_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("HeaderSize",    UINT32),
    ("HeaderVersion", UINT16),
    ("PCRIndex",      TrEE_PCRINDEX),
    ("EventType",     TrEE_EVENTTYPE)
  ]

class TrEE_EVENT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Size",    UINT32),
    ("Header",  TrEE_EVENT_HEADER),
    ("Event",   UINT8 * 1)
  ]

EFI_TREE_GET_CAPABILITY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TREE_PROTOCOL),           # IN      *This
  POINTER(TREE_BOOT_SERVICE_CAPABILITY) # IN  OUT *ProtocolCapability
  )

EFI_TREE_GET_EVENT_LOG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TREE_PROTOCOL),     # IN  *This
  TREE_EVENT_LOG_FORMAT,          # IN  EventLogFormat,
  POINTER(EFI_PHYSICAL_ADDRESS),  # OUT *EventLogLocation,
  POINTER(EFI_PHYSICAL_ADDRESS),  # OUT *EventLogLastEntry,
  POINTER(BOOLEAN)                # OUT *EventLogTruncated
  )

EFI_TREE_HASH_LOG_EXTEND_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TREE_PROTOCOL),     # IN *This
  UINT64,                         # IN Flags,
  EFI_PHYSICAL_ADDRESS,           # IN DataToHash,
  UINT64,                         # IN DataToHashLen,
  POINTER(TrEE_EVENT)             # IN *Event
  )

EFI_TREE_SUBMIT_COMMAND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TREE_PROTOCOL),     # IN *This
  UINT32,                         # IN InputParameterBlockSize,
  POINTER(UINT8),                 # IN *InputParameterBlock,
  UINT32,                         # IN OutputParameterBlockSize,
  POINTER(UINT8)                  # IN *OutputParameterBlock
  )

EFI_TREE_PROTOCOL._fields_ = [
    ("GetCapability",       EFI_TREE_GET_CAPABILITY),
    ("GetEventLog",         EFI_TREE_GET_EVENT_LOG),
    ("HashLogExtendEvent",  EFI_TREE_HASH_LOG_EXTEND_EVENT),
    ("SubmitCommand",       EFI_TREE_SUBMIT_COMMAND)
  ]

