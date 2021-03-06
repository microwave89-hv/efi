#
# BaseAnalyze.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# BaseAnalyze.py is free software: you can redistribute it and/or modify
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

from dOut import *

#
# Default function, Before Native function
#
def _Pre_func (dOut, *args):

  return None, args

#
# Default function, After Native function
#
def _Post_func (dOut, rest, *args):

  return None, args

def GetDefaultFilter ():

  def function_filter2 (*args):

    Information = function_filter2.func_dict["Information"]
    dOut        = function_filter2.func_dict["dOut"]

    _xml = '<Function name="%s" fAddre="0x%X" Structure="%s" sAddr="0x%X">\n' % (
      Information[0],
      Information[2],
      Information[1].__name__,
      Information[3]
      )
    dOut.msg += _xml

    _xml = '<Input length="%d">\n' % len (args)

    cnt = 0
    for arg in args:
      s = get_arg_xml (arg)
      _xml += '<arg%d %s ></arg%d>\n' % (cnt, s, cnt)
      cnt += 1

    dOut.msg += _xml + '</Input>\n'

    Pre_func    = function_filter2.func_dict["Pre_func"]
    Post_func   = function_filter2.func_dict["Post_func"]

    func_type   = function_filter2.func_dict["Native_func"]
    func_addr   = function_filter2.func_dict["Native_addr"]
    Alias_type  = function_filter2.func_dict["Alias_type"]

    if Pre_func != None:
      fRest, args = Pre_func (dOut, *args)

    f = func_type(function_filter2)
    Alias_type.from_address (EfiPy.addressof (f)).value = func_addr

    rest = f (*args)

    if Post_func != None:
      fRest, args = Post_func (dOut, rest, *args)

    if rest != None:
      _xml = '<Output %s>\n' % get_arg_xml (rest)
    else:
      _xml = '<Output>\n'

    cnt = 0
    for arg in args:
      s = get_arg_xml (arg)
      _xml += '<arg%d %s></arg%d>\n' % (cnt, s, cnt)
      cnt += 1

    dOut.msg += _xml + '</Output>\n'

    dOut.msg += '</Function>\n'

    if rest != None:
      return rest

  return function_filter2

class BaseAnalyze:

  #
  # _filter[iMember][self._Idx_...]
  #
  _Idx_NativeFunc = 0
  _Idx_FilterAddr = 1
  _Idx_FilterFunc = 2
  _Idx_funcActive = 3
  _Idx_Enable     = 4
  _Idx_AliasType  = 5

  #
  # self._sCapability[iMember][self._Idx...]
  #
  _IdxPmIsFunc    = 0
  _IdxPmOfs       = 1
  _IdxPmSize      = 2
  _IdxPmType      = 3

  def __init__ (self, dOut=None):

    self._Structure   = None            # Base
    self.Target       = []              # Base
    self._sCapability = {}              # Base
    self.Filter       = []              # Base
    self.dOut         = dOut

  def Build_Filter (self, Target, pattern = None):

    _filter = {}
    _filter["pattern_"] = pattern
    p_base = EfiPy.cast (Target, EfiPy.PVOID)

    for iMember in self._sCapability:

      _filter[iMember] = {}

      if self._sCapability[iMember][self._IdxPmIsFunc] == False:

        _filter[iMember][self._Idx_funcActive] = EfiPy.UINT8(0)
        _filter[iMember][self._Idx_AliasType]  = EfiPy.UINT8
        _filter[iMember][self._Idx_NativeFunc] = \
          _filter[iMember][self._Idx_funcActive].value
        _filter[iMember][self._Idx_FilterFunc] = None
        _filter[iMember][self._Idx_FilterAddr] = EfiPy.UINT8(0)

        continue

      mSizeDict = {8: EfiPy.UINT64, 4: EfiPy.UINT32, 2: EfiPy.UINT16, 1: EfiPy.UINT8}
      mSize     = self._sCapability[iMember][self._IdxPmSize]

      _filter[iMember][self._Idx_AliasType]  = mSizeDict[mSize]

      _filter[iMember][self._Idx_funcActive] = \
        mSizeDict[mSize].from_address(p_base.value + self._sCapability[iMember][self._IdxPmOfs])

      _filter[iMember][self._Idx_NativeFunc] =  \
          _filter[iMember][self._Idx_funcActive].value


      #
      # Build filter function
      #

      args = self._sCapability[iMember][self._IdxPmType]._argtypes_
      rest = self._sCapability[iMember][self._IdxPmType]._restype_
      I_FILTER = EfiPy.CFUNCTYPE (rest, *args)

      iFilter = GetDefaultFilter ()
      iFilter.Native_addr = _filter[iMember][self._Idx_NativeFunc]
      iFilter.Alias_type  = _filter[iMember][self._Idx_AliasType]
      iFilter.Native_func = I_FILTER
      iFilter.Pre_func    = _Pre_func
      iFilter.Post_func   = _Post_func
      # (Function name, Structure Name, Function Address, Structure Addree)
      iFilter.Information = (iMember, self._Structure, _filter[iMember][self._Idx_NativeFunc], p_base.value)
      iFilter.dOut        = self.dOut

      FilterFunc  = I_FILTER(iFilter)

      FilterAddr    = EfiPy.cast (FilterFunc, EfiPy.PVOID)

      _filter[iMember][self._Idx_FilterFunc] = iFilter
      _filter[iMember][self._Idx_FilterAddr] = FilterAddr
      _filter[iMember][self._Idx_Enable]     = False

    return _filter

  def Build_Capability (self, _Structure):

    self._Structure = _Structure

    for f,t in _Structure._fields_:

      a = getattr(self._Structure, f)

      #
      # check if an function by string
      #
      if str(t) == "<class 'ctypes.CFunctionType'>":
        self._sCapability[f] = (True, a.offset, a.size, t)
      else:
        self._sCapability[f] = (False, a.offset, a.size, t)

  def install (self, FuncName, Pre_func = None, Post_func = None):

    if FuncName not in self._sCapability.keys():
      self.dOut.msg += '<WARNNING install="%s"> is not function</WARNNING>\n' % FuncName
      return

    for _filter in self.Filter:

      if Pre_func != None:
        _filter[FuncName][self._Idx_FilterFunc].Pre_func = Pre_func

      if Post_func != None:
        _filter[FuncName][self._Idx_FilterFunc].Post_func = Post_func

  def start (self, FuncName = None):

    if FuncName == None:
      _FuncNames = self._sCapability.keys()
    else:
      _FuncNames = (FuncName,)

    for _FuncName in _FuncNames:

      if _FuncName not in self._sCapability.keys():
        self.dOut.msg += '<WARNNING start="%s"> is not function</WARNNING>\n' % _FuncName
        continue

      if self._sCapability[_FuncName][self._IdxPmIsFunc] == False:
        self.dOut.msg += '<WARNNING start="%s"> is not function</WARNNING>\n' % _FuncName
        continue

      for _filter in self.Filter:
      
        _filter[_FuncName][self._Idx_funcActive].value = \
          _filter[_FuncName][self._Idx_FilterAddr].value

  def stop (self, FuncName = None):

    if FuncName == None:
      _FuncNames = self._sCapability.keys()
    else:
      _FuncNames = (FuncName,)

    for _FuncName in _FuncNames:
      for _filter in self.Filter:

        _filter[_FuncName][self._Idx_funcActive].value = \
          _filter[_FuncName][self._Idx_NativeFunc]


  def uninstall (self, FuncName):

    if FuncName not in self._sCapability.keys():
      self.dOut.msg += '<WARNNING uninstall="%s"> is not function</WARNNING>\n' % FuncName
      return

    for _filter in self.Filter:

      _filter[FuncName][self._Idx_funcActive].value = \
        _filter[FuncName][self._Idx_NativeFunc]

  def __del__(self):

    for iMember in self._sCapability:

      if self._sCapability[iMember][self._IdxPmIsFunc] == False:
        continue

      self.uninstall (iMember)

  def debug_dump (self):

    self.dOut.msg += '<Dump>\n'

    for iMember in self._sCapability:
      self.dOut.msg += '<Function name="%s">\n' % iMember

      for _filter in self.Filter:
        self.dOut.msg += '<Address Native="0x%08X" filter="0x%08X" Active="0x%08X"></Address>\n' % \
          (_filter[iMember][self._Idx_NativeFunc],
           _filter[iMember][self._Idx_FilterAddr].value,
           _filter[iMember][self._Idx_funcActive].value)

      self.dOut.msg += '</Function>\n'

    self.dOut.msg += '</Dump>\n'
