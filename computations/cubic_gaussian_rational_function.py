"""Exact QQ(i)(r,z) arithmetic; middle polynomial variable encodes i, with i^2=-1."""
from flint import fmpq_mpoly_ctx
CTX=fmpq_mpoly_ctx.get(('r','s','t'))
MOD=CTX.gens()[1]**2+1
class F:
 __slots__=('n','d')
 def __init__(self,n=0,d=1):
  self.n=CTX.constant(n) if not hasattr(n,'gcd') else n;self.d=CTX.constant(d) if not hasattr(d,'gcd') else d
  self.n=divmod(self.n,MOD)[1];self.d=divmod(self.d,MOD)[1]
  if self.d and self.d.degrees()[1]>0:
   bar=CTX.from_dict({m:(-c if m[1]%2 else c) for m,c in self.d.to_dict().items()});self.n=divmod(self.n*bar,MOD)[1];self.d=divmod(self.d*bar,MOD)[1]
  if not self.d:raise ZeroDivisionError
  if not self.n:self.d=CTX.constant(1);return
  g=self.n.gcd(self.d);self.n=self.n//g;self.d=self.d//g
  lc=self.d.leading_coefficient();self.n=self.n/lc;self.d=self.d/lc
 def __bool__(self):return bool(self.n)
 def __neg__(self):return F(-self.n,self.d)
 def __add__(self,o):
  if not isinstance(o,F):o=F(o)
  if not self:return o
  if not o:return self
  if self.d==o.d:return F(self.n+o.n,self.d)
  g=self.d.gcd(o.d);a=self.d//g;b=o.d//g;return F(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __sub__(self,o):return self+-o
 def __mul__(self,o):
  if not isinstance(o,F):o=F(o)
  if not self or not o:return F()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d);return F((self.n//g)*(o.n//h),(self.d//h)*(o.d//g))
 __rmul__=__mul__
 def __truediv__(self,o):
  if not isinstance(o,F):o=F(o)
  return F(self.n*o.d,self.d*o.n)
 def __repr__(self):return f'({self.n})/({self.d})'
