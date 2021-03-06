#
# dOut.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# dOut.py is free software: you can redistribute it and/or modify
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

import ctypes

def get_arg_xml (arg):

  sType  = ""
  sAddr  = ""
  sValue = ""
  sGuid  = ''
  sException = ""

  try:

    if arg == None:
      sType  = 'Type="None" '
      return sType + sAddr + sValue

    elif type(arg) in (int, long, float):
      sType  = 'Type="%s" ' % type(arg).__name__
      sValue = 'Value="0x%X"' % arg
      return sType + sAddr + sValue

    elif type(arg) in (str, unicode):
      sType  = 'Type="%s" ' % type(arg).__name__
      sValue = 'Value="%s"' % arg
      return sType + sAddr + sValue

    elif isinstance (arg, ctypes._SimpleCData):
      # print "==>", arg.__class__.__name__
    
      sType  = 'Type="%s" ' % arg.__class__.__name__

      if arg._type_ in 'bBhHlLdDqQfdq':
        sValue = 'Value="0x%X"' % arg.value

      elif arg._type_ in 'cu':
        sValue = 'Value="%c"' % arg.value

      elif arg._type_ in 'zZ':
        sAddr  = ctypes.cast (arg, ctypes.c_void_p)
        if sAddr.value == None:
          sAddr = 'Address="0x00"'
        else:
          sAddr = 'Address="0x%X" ' % sAddr.value
          sValue = 'Value="%s"' % arg.value

      elif arg._type_ in 'P':
        if arg.value == None:
          sValue = 'Address="0x00"'
        else:
          sValue = 'Address="0x%X"' % (arg.value)

      return sType + sAddr + sValue

    #
    # Pure class object
    #
    if issubclass (arg.__class__, ctypes.Structure):
      sType  = 'Type="%s" ' % arg.__class__.__name__

    #
    # pointer structure
    #
    elif issubclass (arg._type_, ctypes.Structure):
      sType  = 'Type="%s" ' % arg.__class__.__name__
      vAddr  = ctypes.cast (arg, ctypes.c_void_p)
      if vAddr.value == None:
        sAddr = 'Address="0x%X"' % (0x00)
      else:
        sAddr = 'Address="0x%X" ' % (vAddr.value)

    #
    # pointer simple datatype
    #
    elif issubclass (arg._type_, ctypes._SimpleCData):
      sType  = 'Type="%s" ' % arg.__class__.__name__
      vAddr  = ctypes.cast (arg, ctypes.c_void_p)
      if vAddr.value == None:
        sAddr = 'Address="0x%X"' % (0x00)
      else:
        sAddr = 'Address="0x%X"' % (vAddr.value)

        if arg._type_._type_ in 'bBhHlLdDqQfdq':
          sValue = ' Value="0x%X"' % arg[0]

        elif arg._type_._type_ in 'cu':
          sValue = ' Value="%c"' % arg[0]

    else:
      sType  = 'Type="%s" ' % arg.__class__.__name__

  except:
    sException  = ' EXCEPT="exception error" '

  if sType == 'Type="LP_GUID" ':

    vAddr = ctypes.cast (arg, ctypes.c_void_p)

    if vAddr.value != None:
      sGuid = 'GUID="%s"' % str(arg[0])

  elif sType == 'Type="LP_c_void_p" ':
  
    vAddr = ctypes.cast (arg, ctypes.c_void_p)

    if vAddr.value != None:
      sValue = ' Value="0x%X"' % vAddr.value

  return sType + sAddr + sValue + sGuid + sException

class dOutClass:

  def __init__ (self, fName = None, msg = None):

    if msg == None:
      self.msg = '<?xml version="1.0"?><Panalyzer>\n'
    else:
      self.msg = msg

    self.name = None

    self.fName = fName

  def __del__ (self):

    if self.name != None:
      self.msg += '</Section>\n'

  def terminate(self):

    self.__del__()

    self.msg += "</Panalyzer>\n"

    if self.fName == None:
      print self.msg
    else:
      f = open(self.fName, 'w')
      print >> f, self.msg
      f.close()

  def section (self, name):

    if self.name == None and name != None:

      self.name = name
      self.msg += '<Section name="%s">\n' % name

      return

    if name != self.name:

      self.msg += '</Section>\n'
      self.msg += '<Section name="%s">\n' % name
      self.name = name

if __name__ == '__main__':

  # d = dOutClass(fName='test.xml')
  d = dOutClass()

  d.msg += '<arg ' + get_arg_xml (0x100) + '></arg>'
  v = ctypes.c_short    (0x01)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v = ctypes.c_ushort   (0x02)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v = ctypes.c_long     (0x03)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_ulong     (0x0A)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_int       (0x0B)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_uint      (0x0C)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_float     (0x0D)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_double    (0x0E)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_longdouble(0x0F)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_longlong  (0x10)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_ulonglong (0x11)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_ubyte     (0x12)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_byte      (0x13)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_char      ('a')
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v= ctypes.c_wchar     (u'b')
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  d.msg += '<arg ' + get_arg_xml ("string test") + '></arg>'
  d.msg += '<arg ' + get_arg_xml (u"unicode test") + '></arg>'

  s=ctypes.c_char_p     ('testing c_char_p')
  d.msg += '<arg ' + get_arg_xml (s) + '></arg>'
  v=ctypes.cast (s, ctypes.c_void_p)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v=ctypes.c_void_p     (0x1234)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v=EfiPy.EFI_HANDLE     ()
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  v=ctypes.c_void_p     (0x00)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'
  s=ctypes.c_wchar_p     ("testing c_wchar_p")
  d.msg += '<arg ' + get_arg_xml (s) + '></arg>'
  v=ctypes.cast (s, ctypes.c_void_p)
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  # s = ctypes.c_ulonglong(4)
  # v = ctypes.POINTER(ctypes.c_ulonglong).fromaddress (ctypes.addressof (s))
  # d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  v= ctypes.POINTER(ctypes.c_ulonglong)()
  print "v._type_", v._type_
  print "v._type_._type_", v._type_._type_
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  v= ctypes.POINTER(ctypes.POINTER(ctypes.c_ulonglong))()
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

  v = POINT()
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  v = ctypes.POINTER(POINT)()
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  v = ctypes.POINTER(ctypes.POINTER(POINT))()
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  v = ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(POINT)))()
  d.msg += '<arg ' + get_arg_xml (v) + '></arg>'

  d.terminate()
