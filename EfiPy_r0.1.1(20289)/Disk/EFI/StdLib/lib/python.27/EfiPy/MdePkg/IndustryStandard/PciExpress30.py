#
# PciExpress30.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PciExpress30.py is free software: you can redistribute it and/or
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
from PciExpress21 import *

PCI_EXPRESS_EXTENDED_CAPABILITY_SECONDARY_PCIE_ID    = 0x0019
PCI_EXPRESS_EXTENDED_CAPABILITY_SECONDARY_PCIE_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_SECONDARY_PCIE (Structure):
  _fields_ = [
    ("Header",              PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("LinkControl3",        UINT32),
    ("LaneErrorStatus",     UINT32),
    ("EqualizationControl", UINT16 * 2)
    ]

