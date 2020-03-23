#
# Performance.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Performance.py is free software: you can redistribute it and/or
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

PEI_PERFORMANCE_STRING_SIZE     = 8
PEI_PERFORMANCE_STRING_LENGTH   = (PEI_PERFORMANCE_STRING_SIZE - 1)

class PEI_PERFORMANCE_LOG_ENTRY (Structure):
  _fields_ = [
  ("Handle",          EFI_PHYSICAL_ADDRESS),
  ("Token",           CHAR8 * PEI_PERFORMANCE_STRING_SIZE),
  ("Module",          CHAR8 * PEI_PERFORMANCE_STRING_SIZE),
  ("StartTimeStamp",  UINT64),
  ("EndTimeStamp",    UINT64)
  ]

class PEI_PERFORMANCE_LOG_HEADER (Structure):
  _fields_ = [
  ("NumberOfEntries", UINT32),
  ("Reserved",        UINT32)
  ]

PERFORMANCE_SIGNATURE   = SIGNATURE_32 ('P', 'e', 'r', 'f')
PERF_TOKEN_SIZE         = 28
PERF_TOKEN_LENGTH       = (PERF_TOKEN_SIZE - 1)
PERF_PEI_ENTRY_MAX_NUM  = 50
PERF_DATA_MAX_LENGTH    = 0x4000

class PERF_DATA (Structure):
  _fields_ = [
  ("Token",     CHAR8 * PERF_TOKEN_SIZE),
  ("Duration",  UINT32)
  ]

class PERF_HEADER (Structure):
  _fields_ = [
  ("BootToOs",    UINT64),
  ("S3Resume",    UINT64),
  ("S3EntryNum",  UINT32),
  ("S3Entry",     PERF_DATA * PERF_PEI_ENTRY_MAX_NUM),
  ("CpuFreq",     UINT64),
  ("BDSRaw",      UINT64),
  ("Count",       UINT32),
  ("Signiture",   UINT32)
  ]

class PERFORMANCE_PROTOCOL (Structure):
  pass

class PERFORMANCE_EX_PROTOCOL (Structure):
  pass

DXE_PERFORMANCE_STRING_SIZE     = 32
DXE_PERFORMANCE_STRING_LENGTH   = (DXE_PERFORMANCE_STRING_SIZE - 1)

INIT_DXE_GAUGE_DATA_ENTRIES     = 800

class GAUGE_DATA_ENTRY (Structure):
  _fields_ = [
  ("Handle",          EFI_PHYSICAL_ADDRESS),
  ("Token",           CHAR8 * DXE_PERFORMANCE_STRING_SIZE),
  ("Module",          CHAR8 * DXE_PERFORMANCE_STRING_SIZE),
  ("StartTimeStamp",  UINT64),
  ("EndTimeStamp",    UINT64)
  ]

class GAUGE_DATA_ENTRY_EX (Structure):
  _fields_ = [
  ("Handle",          EFI_PHYSICAL_ADDRESS),
  ("Token",           CHAR8 * DXE_PERFORMANCE_STRING_SIZE),
  ("Module",          CHAR8 * DXE_PERFORMANCE_STRING_SIZE),
  ("StartTimeStamp",  UINT64),
  ("EndTimeStamp",    UINT64),
  ("Identifier",      UINT32)
  ]

class GAUGE_DATA_HEADER (Structure):
  _fields_ = [
  ("NumberOfEntries", UINT32),
  ("Reserved",        UINT32)
  ]

SMM_PERFORMANCE_STRING_SIZE     = 32
SMM_PERFORMANCE_STRING_LENGTH   = (SMM_PERFORMANCE_STRING_SIZE - 1)

INIT_SMM_GAUGE_DATA_ENTRIES     = 200

class SMM_PERF_COMMUNICATE (Structure):
  _fields_ = [
  ("Function",        UINTN),
  ("ReturnStatus",    EFI_STATUS),
  ("NumberOfEntries", UINTN),
  ("LogEntryKey",     UINTN),
  ("GaugeData",       POINTER(GAUGE_DATA_ENTRY))
  ]

class SMM_PERF_COMMUNICATE_EX (Structure):
  _fields_ = [
  ("Function",        UINTN),
  ("ReturnStatus",    EFI_STATUS),
  ("NumberOfEntries", UINTN),
  ("LogEntryKey",     UINTN),
  ("GaugeDataEx",     POINTER(GAUGE_DATA_ENTRY_EX))
  ]

SMM_PERF_FUNCTION_GET_GAUGE_ENTRY_NUMBER          = 1
SMM_PERF_FUNCTION_GET_GAUGE_DATA                  = 2

PERFORMANCE_START_GAUGE = CFUNCTYPE (
  EFI_STATUS,
  PVOID,            # IN CONST *Handle,  OPTIONAL
  POINTER(CHAR8),   # IN CONST *Token,   OPTIONAL
  POINTER(CHAR8),   # IN CONST *Module,  OPTIONAL
  UINT64            # IN       TimeStamp
  )

PERFORMANCE_END_GAUGE = CFUNCTYPE (
  EFI_STATUS,
  PVOID,          #   IN CONST  *Handle,  OPTIONAL
  POINTER(CHAR8), #   IN CONST  *Token,   OPTIONAL
  POINTER(CHAR8), #   IN CONST  *Module,  OPTIONAL
  UINT64          #   IN        TimeStamp
  )

PERFORMANCE_GET_GAUGE = CFUNCTYPE (
  EFI_STATUS,
  UINTN,                              #   IN  LogEntryKey,
  POINTER(POINTER(GAUGE_DATA_ENTRY))  #   OUT **GaugeDataEntry
  )

PERFORMANCE_START_GAUGE_EX = CFUNCTYPE (
  EFI_STATUS,
  PVOID,          # IN CONST *Handle,   OPTIONAL
  POINTER(CHAR8), # IN CONST *Token,    OPTIONAL
  POINTER(CHAR8), # IN CONST *Module,   OPTIONAL
  UINT64,         # IN       TimeStamp, 
  UINT32          # IN       Identifier 
  )

PERFORMANCE_END_GAUGE_EX = CFUNCTYPE (
  EFI_STATUS,
  PVOID,          #   IN CONST *Handle,  OPTIONAL
  POINTER(CHAR8), #   IN CONST *Token,   OPTIONAL
  POINTER(CHAR8), #   IN CONST *Module,  OPTIONAL
  UINT64,         #   IN       TimeStamp,
  UINT32          #   IN       Identifier
  )

PERFORMANCE_GET_GAUGE_EX = CFUNCTYPE (
  EFI_STATUS,
  UINTN,                                #   IN  LogEntryKey,
  POINTER(POINTER(GAUGE_DATA_ENTRY_EX)) #   OUT **GaugeDataEntryEx
  )

PERFORMANCE_PROTOCOL._fields_ = [
    ("StartGauge",  PERFORMANCE_START_GAUGE),
    ("EndGauge",    PERFORMANCE_END_GAUGE),
    ("GetGauge",    PERFORMANCE_GET_GAUGE)
  ]

PERFORMANCE_EX_PROTOCOL._fields_ = [
    ("StartGaugeEx",  PERFORMANCE_START_GAUGE_EX),
    ("EndGaugeEx",    PERFORMANCE_END_GAUGE_EX),
    ("GetGaugeEx",    PERFORMANCE_GET_GAUGE_EX)
  ]

gPerformanceProtocolGuid         = \
  EFI_GUID (0x76b6bdfa, 0x2acd, 0x4462, (0x9E, 0x3F, 0xcb, 0x58, 0xC9, 0x69, 0xd9, 0x37))

gSmmPerformanceProtocolGuid         = \
  EFI_GUID (0xf866226a, 0xeaa5, 0x4f5a, (0xa9, 0xa,  0x6c, 0xfb, 0xa5, 0x7c, 0x58, 0x8e))

gPerformanceExProtocolGuid         = \
  EFI_GUID (0x1ea81bec, 0xf01a, 0x4d98, (0xa2, 0x1,  0x4a, 0x61, 0xce, 0x2f, 0xc0, 0x22))

gSmmPerformanceExProtocolGuid         = \
  EFI_GUID (0x931fc048, 0xc71d, 0x4455, (0x89, 0x30, 0x47, 0x6,  0x30, 0xe3, 0xe,  0xe5))

