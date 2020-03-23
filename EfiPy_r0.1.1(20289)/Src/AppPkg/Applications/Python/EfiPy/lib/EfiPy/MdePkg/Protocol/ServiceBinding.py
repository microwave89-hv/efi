#
# ServiceBinding.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# ServiceBinding.py is free software: you can redistribute it and/or
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

class EFI_SERVICE_BINDING_PROTOCOL (Structure):
  pass

EFI_SERVICE_BINDING_CREATE_CHILD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERVICE_BINDING_PROTOCOL),  # IN      *This
  POINTER(EFI_HANDLE)                     # IN  OUT *ChildHandle
  )

EFI_SERVICE_BINDING_DESTROY_CHILD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERVICE_BINDING_PROTOCOL),  # IN  *This
  EFI_HANDLE                              # IN  ChildHandle
  )

EFI_SERVICE_BINDING_PROTOCOL._fields_ = [
    ("CreateChild",   EFI_SERVICE_BINDING_CREATE_CHILD),
    ("DestroyChild",  EFI_SERVICE_BINDING_DESTROY_CHILD)
  ]

