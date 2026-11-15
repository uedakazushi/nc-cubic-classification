#!/usr/bin/env python3
"""Finite checks supporting the ordinary local-order theorem: all PI4 cyclic
multiplicities, and the universal quartic Morse coefficient. Does NOT prove
rationality of centers, McKay/descent, or the order-theoretic implications.
"""
import itertools,json,sympy as s
from pathlib import Path
positive={}
for m in range(1,6):
 weak=[a for a in itertools.product(range(5),repeat=m) if sum(a)==4]
 positive[str(m)]=[list(a) for a in weak if all(a)]
 for a in weak:
  full=all(a)
  test=(any(v in [1,2] for v in a) if m==2 else a.count(1)>=2 if m==3 else a.count(1)>=4 if m==4 else True if m==1 else False)
  assert bool(full)==bool(test)
assert positive['5']==[]
a,b,c,q,r,p,t=s.symbols('a b c q r p t');H=s.Matrix([[a,b],[b,c]]);Q=s.Matrix([q,r]);Y=-H.inv()*Q*t**2
u,v=s.symbols('u v');cc=s.symbols('c0:7');F=(a*u*u+2*b*u*v+c*v*v)/2+p*t**3+t*t*(q*u+r*v)+t*(cc[0]*u*u+cc[1]*u*v+cc[2]*v*v)+cc[3]*u**3+cc[4]*u*u*v+cc[5]*u*v*v+cc[6]*v**3
expanded=s.Poly(s.expand(F.subs({u:Y[0],v:Y[1]},simultaneous=True)),t)
c3=s.factor(expanded.coeff_monomial(t**3));c4=s.factor(expanded.coeff_monomial(t**4))
assert c3==p and s.cancel(c4+(Q.T*H.inv()*Q)[0]/2)==0
result={'version':'classification-v20','PI_degree':4,'positive_cyclic_multiplicities':positive,
 'A1_test':'at least one simple of dimension1 or2','A2_test':'at least two distinct dimension1 simples','A3_test':'four distinct dimension1 simples',
 'Morse_kernel_cubic':str(c3),'Morse_kernel_quartic':str(c4),'verified':'all weak compositions of4 for cyclic orders1..5; general symbolic Hessian2 Morse elimination to degree4',
 'ordinary_proof_dependency':'cubic_order4_general_criterion.tex; Schur multiplier vanishing, reflexive descent, finite-pd MCM projectivity, rational center theorem; not established by these finite checks'}
Path(__file__).with_name('cubic_order4_local_types_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS PI4 local multiplicity tests and universal quartic Morse coefficient')
