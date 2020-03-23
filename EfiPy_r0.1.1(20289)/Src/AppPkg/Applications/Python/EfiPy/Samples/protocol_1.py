#
# protocol_1.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# protocol_1.py is free software: you can redistribute it and/or modify
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

import EfiPy

from EfiPy.MdePkg.Protocol.SimpleTextOut import     \
                    gEfiSimpleTextOutProtocolGuid,  \
                    EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL

Interface = EfiPy.PVOID ()
Status = EfiPy.gBS.LocateProtocol (
           EfiPy.byref (gEfiSimpleTextOutProtocolGuid),
           None,
           EfiPy.byref (Interface)
           )

print "Locate protocol.(Status:0x%016X)" % Status

TestConOut = EfiPy.cast (
               Interface,
               EfiPy.POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)
               )

print "MaxMode:", TestConOut[0].Mode[0].MaxMode

TestConOut[0].OutputString (
  TestConOut,
  EfiPy.PCHAR16 (u"Locate protocol testing.\n\r")
  )
