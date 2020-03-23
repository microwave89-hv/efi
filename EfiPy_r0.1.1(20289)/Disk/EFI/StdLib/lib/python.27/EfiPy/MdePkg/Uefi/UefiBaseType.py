#
# UefiBaseType.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UefiBaseType.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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
from EfiPy.MdePkg.Base import *
from EfiPy.MdePkg.Uefi.ProcessorBind import *

PVOID      = c_void_p
ENUM       = UINT32

EFI_GUID = GUID

EFI_STATUS = RETURN_STATUS

EFI_HANDLE = c_void_p

EFI_EVENT = c_void_p

EFI_TPL = UINTN

EFI_LBA = UINT64

EFI_PHYSICAL_ADDRESS = UINT64

EFI_VIRTUAL_ADDRESS = UINT64

class EFI_TIME (Structure):
  _fields_ = [
    ("Year",      UINT16),
    ("Month",     UINT8),
    ("Day",       UINT8),
    ("Hour",      UINT8),
    ("Minute",    UINT8),
    ("Second",    UINT8),
    ("Pad1",      UINT8),
    ("Nanosecond",UINT32),
    ("TimeZone",  UINT16),
    ("Daylight",  UINT8),
    ("Pad2",      UINT8)
    ]
class EFI_IPv4_ADDRESS (Structure):
  _fields_ = [
    ("Addr",      UINT8 * 4)
    ]

class EFI_IPv6_ADDRESS (Structure):
  _fields_ = [
    ("Addr",      UINT8 * 16)
    ]

class EFI_MAC_ADDRESS (Structure):
  _fields_ = [
    ("Addr",      UINT8 * 32)
    ]

class EFI_IP_ADDRESS (Union):
  _fields_ = [
    ("Addr",  UINT32 * 4),
    ("v4",    EFI_IPv4_ADDRESS),
    ("v6",    EFI_IPv6_ADDRESS)
    ]

EFI_SUCCESS                       = RETURN_SUCCESS
EFI_LOAD_ERROR                    = RETURN_LOAD_ERROR
EFI_INVALID_PARAMETER             = RETURN_INVALID_PARAMETER
EFI_UNSUPPORTED                   = RETURN_UNSUPPORTED
EFI_BAD_BUFFER_SIZE               = RETURN_BAD_BUFFER_SIZE
EFI_BUFFER_TOO_SMALL              = RETURN_BUFFER_TOO_SMALL
EFI_NOT_READY                     = RETURN_NOT_READY
EFI_DEVICE_ERROR                  = RETURN_DEVICE_ERROR
EFI_WRITE_PROTECTED               = RETURN_WRITE_PROTECTED
EFI_OUT_OF_RESOURCES              = RETURN_OUT_OF_RESOURCES
EFI_VOLUME_CORRUPTED              = RETURN_VOLUME_CORRUPTED
EFI_VOLUME_FULL                   = RETURN_VOLUME_FULL
EFI_NO_MEDIA                      = RETURN_NO_MEDIA
EFI_MEDIA_CHANGED                 = RETURN_MEDIA_CHANGED
EFI_NOT_FOUND                     = RETURN_NOT_FOUND
EFI_ACCESS_DENIED                 = RETURN_ACCESS_DENIED
EFI_NO_RESPONSE                   = RETURN_NO_RESPONSE
EFI_NO_MAPPING                    = RETURN_NO_MAPPING
EFI_TIMEOUT                       = RETURN_TIMEOUT
EFI_NOT_STARTED                   = RETURN_NOT_STARTED
EFI_ALREADY_STARTED               = RETURN_ALREADY_STARTED
EFI_ABORTED                       = RETURN_ABORTED
EFI_ICMP_ERROR                    = RETURN_ICMP_ERROR
EFI_TFTP_ERROR                    = RETURN_TFTP_ERROR
EFI_PROTOCOL_ERROR                = RETURN_PROTOCOL_ERROR
EFI_INCOMPATIBLE_VERSION          = RETURN_INCOMPATIBLE_VERSION
EFI_SECURITY_VIOLATION            = RETURN_SECURITY_VIOLATION
EFI_CRC_ERROR                     = RETURN_CRC_ERROR
EFI_END_OF_MEDIA                  = RETURN_END_OF_MEDIA
EFI_END_OF_FILE                   = RETURN_END_OF_FILE
EFI_INVALID_LANGUAGE              = RETURN_INVALID_LANGUAGE
EFI_COMPROMISED_DATA              = RETURN_COMPROMISED_DATA

EFI_WARN_UNKNOWN_GLYPH            = RETURN_WARN_UNKNOWN_GLYPH
EFI_WARN_DELETE_FAILURE           = RETURN_WARN_DELETE_FAILURE
EFI_WARN_WRITE_FAILURE            = RETURN_WARN_WRITE_FAILURE
EFI_WARN_BUFFER_TOO_SMALL         = RETURN_WARN_BUFFER_TOO_SMALL
EFI_WARN_STALE_DATA               = RETURN_WARN_STALE_DATA

def EFIERR (_a):
  return ENCODE_ERROR (_a)

def EFI_ERROR (A):
  return RETURN_ERROR (A)

EFI_NETWORK_UNREACHABLE           = EFIERR(100)
EFI_HOST_UNREACHABLE              = EFIERR(101) 
EFI_PROTOCOL_UNREACHABLE          = EFIERR(102)
EFI_PORT_UNREACHABLE              = EFIERR(103)

EFI_CONNECTION_FIN                = EFIERR(104)
EFI_CONNECTION_RESET              = EFIERR(105)
EFI_CONNECTION_REFUSED            = EFIERR(106)

EFI_PAGE_SIZE             = SIZE_4KB
EFI_PAGE_MASK             = 0xFFF
EFI_PAGE_SHIFT            = 12

def EFI_SIZE_TO_PAGES (Size):

  if (Size & EFI_PAGE_MASK) != 0:
    IsMask = 1
  else:
    IsMask = 0

  return (Size >> EFI_PAGE_SHIFT) + IsMask

def EFI_PAGES_TO_SIZE (Pages):

  return Pages << EFI_PAGE_SHIFT

EFI_IMAGE_MACHINE_IA32            = 0x014C
EFI_IMAGE_MACHINE_IA64            = 0x0200
EFI_IMAGE_MACHINE_EBC             = 0x0EBC
EFI_IMAGE_MACHINE_X64             = 0x8664
EFI_IMAGE_MACHINE_ARMTHUMB_MIXED  = 0x01C2
EFI_IMAGE_MACHINE_AARCH64  = 0xAA64

from _EfiPy import EFIPY_MDE_CPU_IA32
from _EfiPy import EFIPY_MDE_CPU_IPF
from _EfiPy import EFIPY_MDE_CPU_X64
from _EfiPy import EFIPY_MDE_CPU_ARM
from _EfiPy import EFIPY_MDE_CPU_AARCH64
from _EfiPy import EFIPY_MDE_CPU_EBC
from _EfiPy import EFIPY_MDE_CPU_TYPE

if EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_IA32:

  def EFI_IMAGE_MACHINE_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_IA32 or Machine == EFI_IMAGE_MACHINE_EBC

  def EFI_IMAGE_MACHINE_CROSS_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_X64

elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_IPF:

  def EFI_IMAGE_MACHINE_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_IA64 or Machine == EFI_IMAGE_MACHINE_EBC

  def EFI_IMAGE_MACHINE_CROSS_TYPE_SUPPORTED(Machine):
    return False

elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_X64:

  def EFI_IMAGE_MACHINE_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_X64 or Machine == EFI_IMAGE_MACHINE_EBC

  def EFI_IMAGE_MACHINE_CROSS_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_IA32

elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_ARM:

  def EFI_IMAGE_MACHINE_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_ARMTHUMB_MIXED or Machine == EFI_IMAGE_MACHINE_EBC

  def EFI_IMAGE_MACHINE_CROSS_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_ARMTHUMB_MIXED

elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_AARCH64:

  def EFI_IMAGE_MACHINE_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_AARCH64 or Machine == EFI_IMAGE_MACHINE_EBC

  def EFI_IMAGE_MACHINE_CROSS_TYPE_SUPPORTED(Machine):
    return False

elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_EBC:

  def EFI_IMAGE_MACHINE_TYPE_SUPPORTED(Machine):
    return Machine == EFI_IMAGE_MACHINE_EBC

  def EFI_IMAGE_MACHINE_CROSS_TYPE_SUPPORTED(Machine):
    return False


if __name__ == '__main__':

  print type(EFI_SUCCESS)
  print "%016X" % EFI_SUCCESS

  print type(EFI_ALREADY_STARTED)
  print "%016X" % EFI_ALREADY_STARTED

  print RETURN_ERROR(EFI_SUCCESS)
  print RETURN_ERROR(EFI_ALREADY_STARTED)

  sys.exit(0)
