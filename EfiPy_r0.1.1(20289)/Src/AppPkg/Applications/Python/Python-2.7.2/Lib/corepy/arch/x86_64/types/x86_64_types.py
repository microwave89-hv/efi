# Copyright 2006-2007 The Trustees of Indiana University.

# This software is available for evaluation purposes only.  It may not be
# redistirubted or used for any other purposes without express written
# permission from the authors.

# Authors:
#   Andrew Friedley     (afriedle@cs.indiana.edu)
#   Christopher Mueller (chemuell@cs.indiana.edu)
#   Andrew Lumsdaine    (lums@cs.indiana.edu)

# TODO - AWF - needs major work


import array

import corepy.arch.x86_64.isa as x86
import corepy.spre.spe as spe
import corepy.arch.x86_64.lib.util as util
  
__doc__ = """
"""

# ------------------------------------------------------------
# 'Type' Classes
# ------------------------------------------------------------

# Type classes implement the operator overloads for a type and hold
# other type-specific information, such as register types and valid
# literal types.

# They are separate from the type so they can be used as mix-ins in
# different contexts, e.g. Variables and Expressions subclasses can
# both share operator semantics by subclassing the same operator
# class.  

# Operator classes also provide static interfaces to typed versions of
# the operations.  

# Operator methods return an Expression of an appropriate type for the
# operation.

# To always return the same type:
#  return SignedWord.expr_class(inst, *(self, other))

# To upcast to the type of the first operand:
#  return self.expr_class(inst, *(self, other))

# To upcast to the type of the second operand:
#  return other.expr_class(inst, *(self, other))

# Upcasting can be useful for two types of different specificity are
# used in expressions and the more specific type should be 
# preserved type the expressions.  For instance, the logical
# operators are the base classes of all integer-like types.  A logical 
# operation, e.g. (a & b), should preserve the most specific type of a
# and b.

def _most_specific(a, b, default = None):
  """
  If a and b are from the same hierarcy, return the more specific of
  [type(a), type(b)], or the default type if they are from different
  hierarchies. If default is None, return type(a), or type(b) if a
  does not have a type_cls
  """
  if (hasattr(a, 'type_cls') and hasattr(a, 'type_cls')):
    if issubclass(b.type_cls, a.type_cls):
      return type(b)
    elif issubclass(a.type_cls, b.type_cls):
      return type(a)
  elif default is None:
    if hasattr(a, 'type_cls'):
      return type(a)
    elif hasattr(b, 'type_cls'):
      return type(b)
    
  return default
  
_int_literals = (spe.Immediate, int, long)

class PPCType(spe.Type):
  def _get_active_code(self):
    return x86.get_active_code()

  def _set_active_code(self, code):
    return x86.set_active_code(code)
  active_code = property(_get_active_code, _set_active_code)

# ------------------------------------------------------------
# General Purpose Register Types
# ------------------------------------------------------------

class BitType(PPCType):
  register_type_id = 'gp'
  literal_types = (int,long)

  def _upcast(self, other, inst):
    return inst.ex(self, other, type_cls = _most_specific(self, other))

  def __and__(self, other):
    if isinstance(other, BitType):
      return self._upcast(other, x86.andx)
    elif isinstance(other, _int_literals):
      return x86.andi.ex(self, other, type_cls = self.var_cls)
    raise Exception('__and__ not implemented for %s and %s' % (type(self), type(other)))    

  and_ = staticmethod(__and__)

  def __lshift__(self, other):
    if isinstance(other, BitType):
      return x86.slwx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__lshift__ not implemented for %s and %s' % (type(self), type(other)))    
  lshift = staticmethod(__lshift__)

  def __rshift__(self, other):
    if isinstance(other, BitType):
      return x86.srwx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__rshift__ not implemented for %s and %s' % (type(self), type(other)))    
  rshift = staticmethod(__rshift__)

  def __or__(self, other):
    if isinstance(other, BitType):
      return self._upcast(other, x86.orx)
    elif isinstance(other, _int_literals):
      return x86.ori.ex(self, other, type_cls = self.var_cls)
    raise Exception('__or__ not implemented for %s and %s' % (type(self), type(other)))    
  or_ = staticmethod(__or__)

  def __xor__(self, other):
    if isinstance(other, BitType):
      return self._upcast(other, x86.xorx)
    elif isinstance(other, _int_literals):
      return x86.xori.ex(self, other, type_cls = self.var_cls)
    raise Exception('__xor__ not implemented for %s and %s' % (type(self), type(other)))    
  xor = staticmethod(__xor__)

  def _set_literal_value(self, value):
    # Put the lower 16 bits into r-temp
    self.code.add(x86.addi(self.reg, 0, value))
  
    # Addis r-temp with the upper 16 bits (shifted add immediate) and
    # put the result in r-target
    if (value & 0x7FFF) != value:
      self.code.add(x86.addis(self.reg, self.reg, ((value + 32768) >> 16)))
      
    return

  def copy_register(self, other):
    return self.code.add(x86.addi(self, other, 0))


# ------------------------------
# Integer Types
# ------------------------------

class UnsignedWordType(BitType):
  def __add__(self, other):
    if isinstance(other, UnsignedWordType):
      return x86.addx.ex(self, other, type_cls = self.var_cls)
    elif isinstance(other, (spe.Immediate, int)):
      return self.expr_cls(x86.addi, *(self, other))
    raise Exception('__add__ not implemented for %s and %s' % (type(self), type(other)))    
  add = staticmethod(__add__)
  
  def __div__(self, other):
    if isinstance(other, SignedWordType):
      return self.expr_cls(x86.divwux, *(self, other))
    raise NotImplemented
  div = staticmethod(__div__)

  def __mul__(self, other):
    if isinstance(other, UnsignedWordType):
      return self.expr_cls(x86.mullwx, *(self, other))
    elif isinstance(other, (spe.Immediate, int)):
      return self.expr_cls(x86.mulli, *(self, other))      
    raise Exception('__mul__ not implemented for %s and %s' % (type(self), type(other)))          
  div = staticmethod(__div__)


class SignedWordType(BitType):

  def __add__(self, other):
    if isinstance(other, SignedWordType):
      return x86.addx.ex(self, other, type_cls = self.var_cls)
    elif isinstance(other, (spe.Immediate, int)):
      return self.expr_cls(x86.addi, *(self, other))
    raise Exception('__add__ not implemented for %s and %s' % (type(self), type(other)))    
  add = staticmethod(__add__)
  
  def __div__(self, other):
    if isinstance(other, SignedWordType):
      return self.expr_cls(x86.divwx, *(self, other))
    raise Exception('__div__ not implemented for %s and %s' % (type(self), type(other)))      
  div = staticmethod(__div__)

  def __mul__(self, other):
    if isinstance(other, SignedWordType):
      return self.expr_cls(x86.mullwx, *(self, other))
    elif isinstance(other, (spe.Immediate, int)):
      return self.expr_cls(x86.mulli, *(self, other))      
    raise Exception('__mul__ not implemented for %s and %s' % (type(self), type(other)))          
  div = staticmethod(__div__)

  def __neg__(self):
    return x86.negx(self, type_cls = self.var_cls)

  def __sub__(self, other):
    if isinstance(other, SignedWordType):
      return self.expr_cls(x86.subfx, other, self) # swap a and b
    raise Exception('__add__ not implemented for %s and %s' % (type(self), type(other)))    
  sub = staticmethod(__sub__)

  
# ------------------------------------------------------------
# Floating Point Register Types
# ------------------------------------------------------------

class SingleFloatType(PPCType):
  register_type_id = 'fp'
  literal_types = (float,)

  def __abs__(self):
    return x86.fabsx.ex(self, type_cls = self.var_cls)
  abs = staticmethod(__abs__)
  
  def __add__(self, other):
    if isinstance(other, SingleFloatType):
      return x86.faddsx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__add__ not implemented for %s and %s' % (type(self), type(other)))        
  add = staticmethod(__add__)
  
  def __div__(self, other):
    if isinstance(other, SingleFloatType):
      return x86.fdivsx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__div__ not implemented for %s and %s' % (type(self), type(other)))    
  div = staticmethod(__div__)

  def __mul__(self, other):
    if isinstance(other, SingleFloatType):
      return x86.fmulsx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__mul__ not implemented for %s and %s' % (type(self), type(other)))
  mul = staticmethod(__mul__)

  def __neg__(self):
    return x86.fnegx.ex(self, type_cls = self.var_cls)
  neg = staticmethod(__neg__)

  def __sub__(self, other):
    if isinstance(other, SingleFloatType):
      return x86.fsubsx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__sub__ not implemented for %s and %s' % (type(self), type(other)))
  sub = staticmethod(__sub__)

  def _set_literal_value(self, value):
    storage = array.array('f', (float(self.value),))
    self.code.add_storage(storage)
    
    r_storage = self.code.acquire_register()
    addr = Bits(storage.buffer_info()[0], reg = r_storage)
    self.code.add(x86.lfs(self.reg, addr.reg, 0))
    self.code.release_register(r_storage)

    return

  def copy_register(self, other):
    return self.code.add(x86.fmr(self, other))

class DoubleFloatType(PPCType):
  register_type_id = 'fp'
  literal_types = (float,)

  def __abs__(self):
    return x86.fabsx.ex(self, type_cls = self.var_cls)
  abs = staticmethod(__abs__)
  
  def __add__(self, other):
    if isinstance(other, DoubleFloatType):
      return x86.faddx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__add__ not implemented for %s and %s' % (type(self), type(other)))
  add = staticmethod(__add__)
  
  def __div__(self, other):
    if isinstance(other, DoubleFloatType):
      return x86.fdivx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__div__ not implemented for %s and %s' % (type(self), type(other)))
  div = staticmethod(__div__)

  def __mul__(self, other):
    if isinstance(other, DoubleFloatType):
      return x86.fmulx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__mul__ not implemented for %s and %s' % (type(self), type(other)))
  mul = staticmethod(__mul__)

  def __neg__(self):
    return x86.fnegx.ex(self, type_cls = self.var_cls)
  neg = staticmethod(__neg__)
    
  def __sub__(self, other):
    if isinstance(other, DoubleFloatType):
      return x86.fsubx.ex(self, other, type_cls = self.var_cls)
    raise Exception('__sub__ not implemented for %s and %s' % (type(self), type(other)))
  sub = staticmethod(__sub__)
    
  def _set_literal_value(self, value):
    storage = array.array('d', (float(value),))
    self.code.add_storage(storage)

    self.load(storage.buffer_info()[0])
#     r_storage = self.code.acquire_register()
#     addr = Bits(storage.buffer_info()[0], reg = r_storage)
#     self.code.add(x86.lfd(self.reg, addr.reg, 0))
#     self.code.release_register(r_storage)

    return

  def copy_register(self, other):
    return self.code.add(x86.fmrx(self, other))

  def load(self, addr, offset = 0):

    # If addr is a constant, create a variable and store the value
    if not issubclass(type(addr), spe.Type):
      r_storage = self.code.acquire_register()
      addr = Bits(addr, reg = r_storage)
    else:
      r_storage = None

    # If offset is a constant, use lfd, otherwise use lfdx
    if issubclass(type(offset), spe.Type):
      self.code.add(x86.lfdx(self, addr, offset))
    else:
      # TODO: Check size of offset to ensure it fits in the immediate field 
      self.code.add(x86.lfd(self, addr, offset))

    if r_storage is not None:
      self.code.release_register(r_storage)

    return

  def store(self, addr, offset = 0):

    # If addr is a constant, create a variable and store the value
    if not issubclass(type(addr), spe.Type):
      r_storage = self.code.acquire_register()
      addr = Bits(addr, reg = r_storage)
    else:
      r_storage = None

    # If offset is a constant, use lfd, otherwise use lfdx
    if issubclass(type(offset), spe.Type):
      self.code.add(x86.stfdx(self, addr, offset))
    else:
      # TODO: Check size of offset to ensure it fits in the immediate field 
      self.code.add(x86.stfd(self, addr, offset))

    if r_storage is not None:
      self.code.release_register(r_storage)

    return


# ------------------------------
# Floating Point Free Functions
# ------------------------------

class _float_function(object):
  """
  Callable object that performs basic type checking and dispatch for
  floating point operations.
  """

  def __init__(self, name, single_func, double_func):
    self.name = name
    self.single_func = single_func
    self.double_func = double_func
    return

  def __call__(self, *operands, **koperands):
    a = operands[0]
    for op in operands[1:]:
      if op.var_cls != a.var_cls:
        raise Exception('Types for all operands must be the same')
      
    if isinstance(a, SingleFloatType):
      return self.single_func.ex(*operands, **{'type_cls': SingleFloat})
    elif isinstance(a, DoubleFloatType):
      return self.double_func.ex(*operands, **{'type_cls': DoubleFloat})    

    raise Exception(self.name + ' is not implemeneted for ' + str(type(a)))

    
fmadd = _float_function('fmadd', x86.fmaddsx, x86.fmaddx)
fmsub = _float_function('fmsub', x86.fmsubsx, x86.fmsubx)
fnmadd = _float_function('fnmadd', x86.fnmaddsx, x86.fnmaddx)
fnmsub = _float_function('fnmsub', x86.fnmsubsx, x86.fnmsubx)
fsqrt = _float_function('fsqrt', x86.fsqrtsx, x86.fsqrtx)

# ------------------------------------------------------------
# User Types
# ------------------------------------------------------------

# Type classes are mixed-in with Variables and Expressions to form the
# final user types.  

def make_user_type(name, type_cls, g = None):
  """
  Create a Variable class and an Expression class for a type class.

  This is equivalent to creating two classes and updating the type
  class (except that the Expression class is not added to the global 
  namespace):

    class [name](spe.Variable, type_cls):
      type_cls = type_cls
    class [name]Ex(spe.Expression, type_cls):
      type_cls = type_cls    
    type_class.var_cls = [name]
    type_class.expr_cls = [name]Ex

  type_cls is added to help determine type precedence among Variables
  and Expressions.

  (note: there's probably a better way to model these hierarchies that
   avoids the type_cls, var_cls, expr_cls references.  But, this works
   and keeping explicit references avoids tricky introspection
   operations) 
  """

  # Create the sublasses of Varaible and Expression
  var_cls = type(name, (spe.Variable, type_cls), {'type_cls': type_cls})
  expr_cls = type(name + 'Ex', (spe.Expression, type_cls), {'type_cls': type_cls})

  # Update the type class with references to the variable and
  # expression classes 
  type_cls.var_cls = var_cls
  type_cls.expr_cls = expr_cls

  # Add the Variable class to the global namespace
  if g is None: g = globals()
  g[name] = var_cls

  return


_user_types = ( # name, type class
  ('Bits', BitType),
  ('UnsignedWord', UnsignedWordType),
  ('SignedWord', SignedWordType),
  ('SingleFloat', SingleFloatType),
  ('DoubleFloat', DoubleFloatType)
  )

for t in _user_types:
  make_user_type(*(t + (globals(),)))


# ------------------------------------------------------------
# Unit Tests
# ------------------------------------------------------------

def SimpleTest():
  """
  Just make sure things are working...
  """
  from corepy.arch.x86.platform import Processor, InstructionStream

  code = InstructionStream()
  proc = Processor()

  # Without active code
  a = SignedWord(11, code)
  b = SignedWord(31, reg = code.acquire_register())
  c = SignedWord(reg = code.gp_return)

  byte_mask = Bits(0xFF, code)
  code.add(x86.addi(code.gp_return, 0, 31))

  # c.v = a + SignedWord.cast(b & byte_mask) + 12
  c.v = a + (byte_mask & b) + 12

  if True:
    r = proc.execute(code)
    assert(r == (42 + 12))
  
  # With active code
  code.reset()

  x86.set_active_code(code)
  
  a = SignedWord(11)
  b = SignedWord(31)
  c = SignedWord(reg = code.gp_return)

  byte_mask = Bits(0xFF)

  c.v = a + (b & byte_mask)

  x86.set_active_code(None)
  r = proc.execute(code)
  # code.print_code()
  assert(r == 42)
  return


def TestBits():
  from corepy.arch.x86.platform import Processor, InstructionStream

  code = InstructionStream()
  proc = Processor()

  x86.set_active_code(code)
  
  b = Bits(0xB0)
  e = Bits(0xE0000)
  a = Bits(0xCA)
  f = Bits(0x5)
  x = Bits(0, reg = code.gp_return)
  
  mask = Bits(0xF)
  byte = Bits(8) # 8 bits
  halfbyte = Bits(4) 

  f.v = (a & mask) ^ f
  x.v = (b << byte) | (e >> byte) | ((a & mask) << halfbyte) | (f | mask)

  r = proc.execute(code)
  assert(r == 0xBEAF)
  return
  
def TestFloatingPoint(float_type):
  from corepy.arch.x86.platform import Processor, InstructionStream
  
  code = InstructionStream()
  proc = Processor()

  x86.set_active_code(code)

  x = float_type(1.0)
  y = float_type(2.0)
  z = float_type(3.0)

  a = float_type()
  b = float_type()
  c = float_type()
  d = float_type()
  
  # Create some data
  data = array.array('d', (1.0, 2.0, 3.0, 4.0))
  addr = data.buffer_info()[0]

  # Load from addr
  a.load(addr) 

  # Load from addr with idx in register
  offset = Bits(8)
  b.load(data.buffer_info()[0], offset)

  # Load from addr with constant idx 
  c.load(data.buffer_info()[0], 8*2)
  
  # Load from addr with addr as a register
  reg_addr = Bits(addr)
  d.load(reg_addr)
  
  r = float_type(reg = code.fp_return)

  r.v = (x + y) / y

  r.v = fmadd(a, y, z + z) + fnmadd(a, y, z + z) + fmsub(x, y, z) + fnmsub(x, y, z) 
  x.v = -x
  r.v = r + x - x + a + b - c + d - d

  # Store from addr
  a.v = 11.0
  a.store(addr) 

  # Store from addr with idx in register
  offset = Bits(8)
  b.v = 12.0
  b.store(data.buffer_info()[0], offset)

  # Store from addr with constant idx
  c.v = 13.0
  c.store(data.buffer_info()[0], 8*2)
  
  # Store from addr with addr as a register
  d.v = 14.0
  reg_addr = UnsignedWord(addr)
  reg_addr.v = reg_addr + 8 * 3
  d.store(reg_addr)
  
  r = proc.execute(code, mode='fp')
  assert(r == 0.0)
  assert(data[0] == 11.0)
  assert(data[1] == 12.0)
  assert(data[2] == 13.0)
  assert(data[3] == 14.0)
  
  return

if __name__=='__main__':
  from corepy.arch.x86.lib.util import RunTest
  RunTest(SimpleTest)
  RunTest(TestFloatingPoint, SingleFloat)
  RunTest(TestFloatingPoint, DoubleFloat)
  RunTest(TestBits)
