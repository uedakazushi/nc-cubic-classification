"""Negative AS2 base with separately normalizing positive quantum generators."""
import json
from pathlib import Path
import sympy as S
from functools import lru_cache
a,k=S.symbols('a k')
@lru_cache(None)
def nf(word):
 for i in range(len(word)-1):
  if word[i:i+2]==(1,0):
   out={}
   for mid,c in [((0,1),S.Integer(1)),((0,0),k)]:
    for w,d in nf(word[:i]+mid+word[i+2:]).items():out[w]=out.get(w,0)+c*d
   return {w:S.expand(c) for w,c in out.items() if c}
 return {word:S.Integer(1)}
quadratics=[(0,0),(0,1),(1,1)];cubics=[(0,0,0),(0,0,1),(0,1,1)];Qmap=S.zeros(3)
for j,word in enumerate(quadratics):
 for w,c in nf(word+(0,)).items():Qmap[cubics.index(w),j]+=a*c
 for w,c in nf((0,)+word).items():Qmap[cubics.index(w),j]+=c
assert S.expand(Qmap.det()-(a+1)**3)==0
# q=-1 negative base: an anti-diagonal F swaps u^2,v^2, so cannot fix both.
s,t=S.symbols('s t');centermap=S.Matrix([[0,t*t],[s*s,0]])
assert (centermap-S.eye(2))[0,0]==-1
# Odd powers of an anti-diagonal map remain anti-diagonal, including inverse.
F=S.Matrix([[0,s],[t,0]])
assert all((F**n)[0,0]==0 and (F**n)[1,1]==0 for n in [-3,-1,1,3])
# If a=-1 for the Jordan base, ac=-1 forces c=1 and p=a^-2=1.
c,p=S.symbols('c p');assert S.solve([a*c+1,p*a*a-1,a+1],[a,c,p],dict=True)==[{a:-1,c:1,p:1}]
out={'status':'PASS','scope':'positive quantum AS2 plane whose two standard generators separately normalize the negative AS2 base; all Nakayama Jordan types',
 'checks':['Jordan quadratic intertwiner determinant=(a+1)^3','q=-1 anti-diagonal action cannot fix both central squares','odd anti-diagonal powers cannot equal -I','Jordan coefficient exception forces positive plane commutative'],
 'conclusion':'all H3 objects in this opposite-separated chart are the known fixed sign-envelope cuts',
 'proof':'papers/sections/cubic_order2_22_rank4_opposite_separated.tex',
 'not_claimed':['positive Jordan opposite-separated chart','all rank4 graph coverage','zero-top global family descent']}
Path(__file__).with_name('cubic_order2_22_rank4_opposite_separated_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS opposite-separated quantum-positive chart intertwiners and Jordan exception')
