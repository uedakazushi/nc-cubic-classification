"""Finite polynomial parameters over the cubic boundary function field.
Division is permitted only by nonzero parameter constants.
"""
class ParameterPolynomial:
 def __init__(self,K,d):self.K=K;self.d={w:c for w,c in d.items() if c}
 def cv(self,b):return b if isinstance(b,ParameterPolynomial) else self.K.convert(b)
 def __bool__(self):return bool(self.d)
 def __neg__(self):return ParameterPolynomial(self.K,{w:-c for w,c in self.d.items()})
 def __add__(self,b):
  out=dict(self.d)
  for w,c in self.cv(b).d.items():out[w]=out.get(w,self.K.base.zero)+c
  return ParameterPolynomial(self.K,out)
 __radd__=__add__
 def __sub__(self,b):return self+-self.cv(b)
 def __rsub__(self,b):return self.cv(b)+-self
 def __mul__(self,b):
  out={}
  for a,c in self.d.items():
   for w,d in self.cv(b).d.items():
    v=tuple(x+y for x,y in zip(a,w));out[v]=out.get(v,self.K.base.zero)+c*d
  return ParameterPolynomial(self.K,out)
 __rmul__=__mul__
 def __truediv__(self,b):
  b=self.cv(b)
  if set(b.d)!={(0,0)}:raise ValueError('nonconstant parameter pivot: '+str(list(b.d)))
  inv=b.d[(0,0)].inverse()
  return ParameterPolynomial(self.K,{w:c*inv for w,c in self.d.items()})
 def __rtruediv__(self,b):return self.cv(b)/self
 def __pow__(self,n):
  out=self.K.one
  for _ in range(n):out=out*self
  return out
 def __eq__(self,b):return not(self-self.cv(b))
 def __repr__(self):return str(self.d)
class ParameterRing:
 def __init__(self,base):
  self.base=base;self.zero=self.convert(0);self.one=self.convert(1)
  self.u=ParameterPolynomial(self,{(1,0):base.one});self.v=ParameterPolynomial(self,{(0,1):base.one})
 def convert(self,c):
  if not hasattr(c,'a'):c=self.base.convert(c)
  return ParameterPolynomial(self,{(0,0):c})
