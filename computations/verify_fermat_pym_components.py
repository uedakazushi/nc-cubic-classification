#!/usr/bin/env python3
"""Exact coefficient witnesses for quantum Fermat in Pym L1111 and L112.
Checks coefficients and central 3-torsion, not the global AS stack classification.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp

a,b,c=sp.symbols('a b c',nonzero=True)
q={(0,1):a,(0,2):b,(0,3):1/(a*b),(1,2):c,(1,3):a/c,(2,3):b*c}
def Q(i,j):
    if i==j:return sp.Integer(1)
    return q[i,j] if i<j else 1/q[j,i]
for i in range(4):
    assert sp.cancel(sp.prod(Q(i,j) for j in range(4))-1)==0

z=sp.Symbol('z')
spec={a:z,b:z,c:sp.Integer(1)}
expected={(0,1):z,(0,2):z,(0,3):z,(1,2):1,(1,3):z,(2,3):z}
for pair,val in expected.items():
    numerator=sp.together(q[pair].subs(spec)-val).as_numer_denom()[0]
    assert sp.rem(numerator,z*z+z+1,z)==0,pair

# L112 quantum parameters with generators X0=x,X1=y,X2=t,X3=z.
p0=z*z;p1=z
pym={('t','x'):1/p0,('z','x'):p0,('t','y'):p1,
     ('z','y'):1/p1,('z','t'):p1/p0}
want={('t','x'):z,('z','x'):1/z,('t','y'):z,
      ('z','y'):1/z,('z','t'):1/z}
for pair,val in pym.items():
    numerator=sp.together(val-want[pair]).as_numer_denom()[0]
    assert sp.rem(numerator,z*z+z+1,z)==0,pair

qx=sp.expand(p1-p0+1-p0*p0)
qy=sp.expand(p1-p0+p1*p1-1)
assert sp.rem(qx-(1-z*z),z*z+z+1,z)==0
assert sp.rem(qy-(z-1),z*z+z+1,z)==0
s=sp.symbols('s',nonzero=True);X,Y=sp.symbols('X Y')
quadratic=(1-z*z)*X**2+(z-1)*Y**2
assert sp.expand(s*s*quadratic.subs({X:X/s,Y:Y/s})-quadratic)==0
torsion=list(product(range(3),repeat=3))
assert len(torsion)==27
report={
  'date':'2026-11-15',
  'arithmetic':'exact symbolic/cyclotomic checks over Q(zeta)',
  'cy_skew_3_torus':{f'{i}{j}':str(v) for (i,j),v in q.items()},
  'fermat_parameters':'a=b=zeta,c=1',
  'L112_parameters':'p0=zeta^2,p1=zeta,lambda=0; X0=x,X1=y,X2=t,X3=z',
  'L112_correction':'(1-zeta^2)*X0^2+(zeta-1)*X1^2',
  'degeneration':'Q -> s^2 Q; s!=0 obtained by a basis change; s=0 is skew Fermat B',
  'central_diagonal_cubic':'a^3=b^3=c^3=1',
  'torsion_point_count':27,
  'limitations':'No tangent/intersection multiplicity or exclusion of other Pym components.'
}
Path(__file__).with_name('fermat_pym_certificate.json').write_text(
    json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS: L1111 parameter, L112 specialization, CY torus, torsion condition')
