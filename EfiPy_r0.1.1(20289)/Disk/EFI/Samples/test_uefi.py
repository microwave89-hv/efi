#!/usr/bin/python

#
# test_uefi.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# test_uefi.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

#
# Protocol import testing
#

import EfiPy

print "EFIPY_MDE_CPU_IA32:",    EfiPy.EFIPY_MDE_CPU_IA32
print "EFIPY_MDE_CPU_IPF:",     EfiPy.EFIPY_MDE_CPU_IPF
print "EFIPY_MDE_CPU_X64:",     EfiPy.EFIPY_MDE_CPU_X64
print "EFIPY_MDE_CPU_ARM:",     EfiPy.EFIPY_MDE_CPU_ARM
print "EFIPY_MDE_CPU_AARCH64:", EfiPy.EFIPY_MDE_CPU_AARCH64
print "EFIPY_MDE_CPU_TYPE:",    EfiPy.EFIPY_MDE_CPU_TYPE
