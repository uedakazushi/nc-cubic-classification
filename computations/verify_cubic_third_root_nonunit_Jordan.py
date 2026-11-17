#!/usr/bin/env python3
"""Full exact actual-Jordan twisted top kernel, relation rows and growth.
No semisimple top substitution or sample point is used.
"""
import itertools,json,math
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix
z=s.Symbol('z');K=s.QQ.alg_field_from_poly(s.Poly(z**2+z+1));omega=K.unit;one=K.one;zero=K.zero
O=s.Symbol('omega');a=s.symbols('a:10')
def expr(c):
 co=c.to_list();return sum(s.Rational(v.numerator,v.denominator)*O**(len(co)-j-1) for j,v in enumerate(co))
def red(e):return s.rem(s.expand(e),O**2+O+1,O)
cases=[]
for exponent in [1,2]:
 weights=[exponent,exponent,0,(-exponent)%3];rho=omega**exponent
 nu=[[one/rho,-one/(rho*rho),zero,zero],[zero,one/rho,zero,zero],
     [zero,zero,one,zero],[zero,zero,zero,one/(omega**weights[3])]]
 words=[w for w in itertools.product(range(4),repeat=4) if sum(weights[j] for j in w)%3==0];idx={w:j for j,w in enumerate(words)}
 assert len(words)==85
 D={j:{j:one} for j in range(85)}
 for j,w in enumerate(words):
  for v in range(4):
   c=nu[v][w[-1]]
   if not c:continue
   k=idx[(v,)+w[:-1]];D[k][j]=D[k].get(j,zero)+c
 mat=DomainMatrix.from_dod(D,(85,85),K);basis=mat.nullspace();N=basis.to_list()
 assert mat.rank()==75 and len(N)==10
 assert mat.matmul(basis.transpose()).is_zero_matrix
 H=s.zeros(16)
 for parameter,row in zip(a,N):
  for w,c in zip(words,row):
   if c:H[4*w[0]+w[1],4*w[2]+w[3]]+=parameter*expr(c)
 H0=H.extract([3,7,10,12,13],[3,7,10,12,13]);H2=H.extract([0,1,4,5,11,14],[2,6,8,9,15])
 rhoE=expr(rho)
 expected=4*s.Matrix([[a[4]*(rhoE+1),0,a[6]*(rhoE+1),a[7]*(rhoE+1)-a[8]*rhoE,a[8]*(rhoE+1)],
  [0,0,0,-a[8]*(rhoE+1),0],[a[6]*(rhoE+1),0,0,a[3],0],
  [a[7]*(rhoE+1),-a[8]*(rhoE+1),a[3],a[4],0],[a[8]*(rhoE+1),0,0,0,0]])
 # A conjugate basis may be scaled by the field implementation; the current
 # fraction-free nullspace is Galois compatible and checked explicitly here.
 assert (H0-expected).applyfunc(red)==s.zeros(5)
 minor=H0.extract([0,1,3,4],[0,1,3,4]).det()
 assert red(minor-256*a[8]**4*(rhoE+1)**4)==0
 assert H0[1,:].subs(a[8],0)==s.zeros(1,5) and H0[4,:].subs(a[8],0)==s.zeros(1,5)
 assert H2[3,:]==s.zeros(1,5)
 sparse=[{''.join('xybc'[j] for j in w):str(expr(c)) for w,c in zip(words,row) if c} for row in N]
 cases.append({'rho_exponent':exponent,'restricted_word_count':85,'linear_system_rank':75,
               'top_kernel_dimension':10,'top_basis':sparse,'forbidden_minor':'256*a8^4*(rho+1)^4',
               'relation_rows_vanish':['yc,cy after a8=0','yy identically']})
x,y=1,0
for n in range(15):x,y=x+y,x
assert x+y==1597>math.comb(18,3)==816
out={'status':'PASS','scope':'complete finite actual-Jordan tensor linear systems and relation/growth obstruction',
 'field':'QQ(omega), omega^2+omega+1=0','cases':cases,'quotient_degree15_lower_bound':1597,'AS4_degree15':816,
 'conclusion':'nonunit repeated third-root spectra require semisimple Nakayama',
 'not_claimed':['semisimple nonunit spectra excluded','unit-repeat Jordan spectrum excluded','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_nonunit_Jordan_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','actual_Jordan_cases':2,'top_kernel_dimensions':[10,10]}))
