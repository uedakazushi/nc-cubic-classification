#!/usr/bin/env python3
"""Exact actual unit-repeat Jordan top and quantum-plane cubic obstruction.
Ore recovery and the leading Ore-degree invariant argument are ordinary proofs.
"""
import itertools,json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix
z=s.Symbol('z');K=s.QQ.alg_field_from_poly(s.Poly(z**2+z+1));omega=K.unit;one=K.one;zero=K.zero
O=s.Symbol('omega');a=s.symbols('a:12');Q=s.Symbol('q')
def expr(c):
 co=c.to_list();return sum(s.Rational(v.numerator,v.denominator)*O**(len(co)-j-1) for j,v in enumerate(co))
def red(e):return s.rem(s.expand(e),O**2+O+1,O)
cases=[]
for exponent in [1,2]:
 weights=[0,0,exponent,(-exponent)%3];rho=omega**exponent;rhoE=expr(rho)
 nu=[[one,-one,zero,zero],[zero,one,zero,zero],[zero,zero,one/rho,zero],[zero,zero,zero,rho]]
 words=[w for w in itertools.product(range(4),repeat=4) if sum(weights[j] for j in w)%3==0];idx={w:j for j,w in enumerate(words)}
 assert len(words)==86
 D={j:{j:one} for j in range(86)}
 for j,w in enumerate(words):
  for v in range(4):
   c=nu[v][w[-1]]
   if c:
    k=idx[(v,)+w[:-1]];D[k][j]=D[k].get(j,zero)+c
 mat=DomainMatrix.from_dod(D,(86,86),K);basis=mat.nullspace();N=basis.to_list()
 assert mat.rank()==74 and len(N)==12 and mat.matmul(basis.transpose()).is_zero_matrix
 N=[[(-one if exponent==2 else one)*c for c in row] for row in N]
 H=s.zeros(16)
 for parameter,row in zip(a,N):
  for w,c in zip(words,row):
   if c:H[4*w[0]+w[1],4*w[2]+w[3]]+=parameter*expr(c)
 M=H.extract([2,6,8,9,15],[3,7,10,12,13]);reverse=H.extract([3,7,10,12,13],[2,6,8,9,15])
 two=s.Matrix([[2*a[6],2*a[5]],[0,0],[2*a[8],2*a[6]],[0,0],[0,0]])
 assert (M.extract(range(5),[1,4])-two).applyfunc(red)==s.zeros(5,2)
 assert (reverse[:,1]+2*rhoE*s.Matrix([a[6],0,0,a[5],0])).applyfunc(red)==s.zeros(5,1)
 determinant=M.extract([0,2],[1,4]).det()
 assert s.expand(determinant)==4*(a[6]**2-a[5]*a[8])
 sub={a[5]:0,a[6]:0,a[8]:0}
 assert M[1,:].subs(sub)==s.zeros(1,5) and M[3,:].subs(sub)==s.zeros(1,5)
 assert reverse[1,:].subs(sub)==s.zeros(1,5) and reverse[4,:].subs(sub)==s.zeros(1,5)
 t=s.Symbol('t',nonzero=True)
 assert two[:,1].subs({a[6]:t*a[5]})==2*a[5]*s.Matrix([1,0,t,0,0])
 # In the quantum-plane quotient the literal b,c normal equations require
 # q^r=q^s=rho for all r+s=3. Their polynomial gcd is 1 in QQ(rho)[q].
 gcds=[]
 for r in range(4):
  ss=3-r
  f=s.Poly(Q**r-K.to_sympy(rho),Q,domain=K)
  g=s.Poly(Q**ss-K.to_sympy(rho),Q,domain=K)
  gcd=s.gcd(f,g).monic()
  assert gcd.degree()==0
  gcds.append({'b_exponent':r,'c_exponent':ss,'normal_equation_gcd':1})
 sparse=[{''.join('xybc'[j] for j in w):str(expr(c)) for w,c in zip(words,row) if c} for row in N]
 cases.append({'rho_exponent':exponent,'word_count':86,'cyclic_rank':74,'top_dimension':12,
               'top_basis':sparse,'mixed_pure_columns_determinant':'4*(a6^2-a5*a8)',
               'zero_parameter_relation_rows_vanish':['yb,by','yc,cy'],'quantum_plane_degree3_obstructions':gcds})
out={'status':'PASS','scope':'full actual Jordan tensor systems, original mixed columns and all-parameter quantum-plane normal-cubic gcds; ordinary Ore/invariant proof separate',
 'cases':cases,'conclusion':'unit-repeat third-root Jordan H3 cuts all factor through x',
 'combined_frontier':'all three-eigenvalue H3 Nakayama automorphisms semisimple of order3',
 'not_claimed':['three semisimple spectra exist or are H3 admissible','four-eigenvalue/CY completeness','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_Jordan_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','actual_Jordan_cases':2,'top_dimensions':[12,12],'quantum_plane_gcds':8}))
