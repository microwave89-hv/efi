#
# EfiShellParameters.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiShellParameters.py is free software: you can redistribute it and/or
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

from EfiPy          import *
from EfiPy.ShellPkg import *

gEfiShellParametersProtocolGuid   = \
  EFI_GUID (0x752f3136, 0x4e16, 0x4fdc, ( 0xa2, 0x2a, 0xe5, 0xf4, 0x68, 0x12, 0xf4, 0xca ))
class EFI_SHELL_PARAMETERS_PROTOCOL (Structure):
  _fields_ = [
    ("Argv",    POINTER(PCHAR16)),
    ("Argc",    UINTN),
    ("StdIn",   SHELL_FILE_HANDLE),
    ("StdOut",  SHELL_FILE_HANDLE),
    ("StdErr",  SHELL_FILE_HANDLE)
  ]
