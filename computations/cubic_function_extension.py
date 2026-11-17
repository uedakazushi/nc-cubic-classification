"""Small exact cubic function-field arithmetic for the boundary exploration.
R must be a noncube in the ground field; every inverse checks its product.
Equality uses a zero difference, avoiding nonmonic FracElement normalization.
"""
# Exact cubic extension J[d]/(d^3-R), using explicit adjugate inverse.
class CubicElement:
 def __init__(self,K,a):self.K=K;self.a=tuple(a)
 def cv(self,b):return b if isinstance(b,CubicElement) else self.K.convert(b)
 def __bool__(self):return any(self.a)
 def __eq__(self,b):return all(not(x-y) for x,y in zip(self.a,self.cv(b).a))
 def __neg__(self):return CubicElement(self.K,[-a for a in self.a])
 def __add__(self,b):return CubicElement(self.K,[x+y for x,y in zip(self.a,self.cv(b).a)])
 __radd__=__add__
 def __sub__(self,b):return self+-self.cv(b)
 def __rsub__(self,b):return self.cv(b)+-self
 def __mul__(self,b):
  b=self.cv(b);c=[self.K.J.zero]*5
  for i,x in enumerate(self.a):
   for j,y in enumerate(b.a):c[i+j]+=x*y
  c[0]+=c[3]*self.K.R;c[1]+=c[4]*self.K.R
  return CubicElement(self.K,c[:3])
 __rmul__=__mul__
 def inverse(self):
  a,b,c=self.a;R=self.K.R;N=a**3+b**3*R+c**3*R**2-3*a*b*c*R
  if not N:raise ZeroDivisionError('cubic norm zero')
  out=CubicElement(self.K,[(a*a-b*c*R)/N,(c*c*R-a*b)/N,(b*b-a*c)/N]);assert self*out==self.K.one
  return out
 def __truediv__(self,b):return self*self.cv(b).inverse()
 def __rtruediv__(self,b):return self.cv(b)*self.inverse()
 def __pow__(self,n):
  if n<0:return self.inverse()**(-n)
  out=self.K.one
  for _ in range(n):out*=self
  return out
 def __repr__(self):return str(self.a)
class CubicField:
 def __init__(self,J,R):
  self.J=J;self.R=R;self.zero=self.convert(0);self.one=self.convert(1);self.generator=CubicElement(self,[J.zero,J.one,J.zero])
 def convert(self,x):return CubicElement(self,[self.J.convert(x),self.J.zero,self.J.zero])
