#!/usr/bin/env python3
"""Full-q PBW, invariant quadratic/cubic Smith forms and fresh primitive9
normal generator for a split two-curvature AS4 family. No general proportional
coupling coverage is claimed.
"""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.matrices.normalforms import smith_normal_form
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1));Q=s.Symbol('q');K=F.frac_field(Q);q=K.gens[0];o=K.convert(F.to_sympy(F.unit))
def factory(K,q,o,extension=False):
 one=K.one;zero=K.zero
 rules={(1,0):{(0,1):one/q},(2,0):{(0,2):q,(1,1):-q},(2,1):{(1,2):one/q,(0,0):-one/q}}
 if extension:rules.update({(3,0):{(0,3):o**2},(3,1):{(1,3):o},(3,2):{(2,3):one}})
 @lru_cache(None)
 def nf(w):
  for j in range(len(w)-1):
   if w[j:j+2] not in rules:continue
   out={}
   for rep,c in rules[w[j:j+2]].items():
    for v,d in nf(w[:j]+rep+w[j+2:]).items():out[v]=out.get(v,zero)+c*d
   return {v:c for v,c in out.items() if c}
  return {w:one}
 def first(w,j):
  out={}
  for rep,c in rules[w[j:j+2]].items():
   for v,d in nf(w[:j]+rep+w[j+2:]).items():out[v]=out.get(v,zero)+c*d
  return {v:c for v,c in out.items() if c}
 for triple in itertools.combinations(range(4 if extension else 3),3):
  w=tuple(reversed(triple));assert first(w,0)==first(w,1)
 def residual(w,j,scalar):
  out=dict(nf(w+(j,)))
  for v,c in nf((j,)+w).items():out[v]=out.get(v,zero)-scalar*c
  return {v:c for v,c in out.items() if c}
 return nf,residual
nf,residual=factory(K,q,o);nf4,residual4=factory(K,q,o,True)
one=K.one;zero=K.zero
assert residual4((3,3,3),0,o**2).get((0,3,3,3),zero)==one-o**2
assert residual4((2,3,3),0,o**2).get((1,1,3,3),zero)==-o*q
basis2=[(0,1),(2,2)];basis3=[(0,0,0),(1,1,1),(0,1,2),(2,2,2)]
def matrix(K,residual,basis,inv):
 cols=[]
 for w in basis:
  out={}
  for j in range(3):
   for v,c in residual(w,j,inv[j]).items():out[(j,v)]=c
  cols.append(out)
 keys=sorted(set().union(*(set(c) for c in cols)))
 return DomainMatrix.from_dod({r:{j:c[k] for j,c in enumerate(cols) if k in c} for r,k in enumerate(keys)},(len(keys),len(cols)),K)
Z=matrix(K,residual,basis2,[one]*3);G=matrix(K,residual,basis3,[o**2,o,one]);smiths={}
for name,M in [('Z2fixed',Z),('normalG3',G)]:
 D=K.field.ring.one
 for row in M.to_list():
  for c in row:D=D.lcm(c.denom)
 SM=smith_normal_form((M.to_Matrix()*D.as_expr()).applyfunc(s.cancel),domain=F.poly_ring(Q))
 factors=[s.Poly(SM[j,j],Q,domain=F).monic().as_expr() for j in range(M.shape[1])]
 expected=[s.S.One,Q**2*(Q+1)] if name=='Z2fixed' else [s.S.One,Q**2,Q**4,Q**6*(Q**3-F.to_sympy(F.unit)**2)]
 assert all(s.Poly(a-b,Q,domain=F).is_zero for a,b in zip(factors,expected))
 smiths[name]={'shape':list(M.shape),'common_denominator':str(D.as_expr()),'monic_invariant_factors':[str(f) for f in factors]}
assert s.gcd(s.Poly(Q+1,Q,domain=F),s.Poly(Q**3-F.to_sympy(F.unit)**2,Q,domain=F)).degree()==0
# x-degree1 block equals the fixed central-quadratic block up to unit scalars.
for w in basis2:
 for j,scale in enumerate([o**2,o,one]):
  expected={v+(3,):scale*c for v,c in residual(w,j,one).items()}
  assert residual4(w+(3,),j,[o**2,o,one][j])==expected
# Fresh q=-1 central fixed quadratic, exactly y^2.
_,rm=factory(F,-F.one,F.unit);Zm=matrix(F,rm,basis2,[F.one]*3)
assert Zm.rank()==1 and all(not rm((2,2),j,F.one) for j in range(3))
# All primitive9 roots and both cubic roots in a faithful irreducible field.
t=s.Symbol('t');h=t**6+t**3+1;assert s.Poly(h,t).is_irreducible
J=s.QQ.alg_field_from_poly(s.Poly(h,t));u=J.unit;oo=u**6;one=J.one
_,r9=factory(J,u,oo);G9=matrix(J,r9,basis3,[oo**2,oo,one]);assert G9.rank()==3
coeff=[u*(2+oo)/3,u*u*(1+2*oo)/3,u*oo**2,one]
for j in range(3):
 out={}
 for w,c in zip(basis3,coeff):
  for v,d in r9(w,j,[oo**2,oo,one][j]).items():out[v]=out.get(v,J.zero)+c*d
 assert not any(out.values())
out={'status':'PASS','scope':'all-q original PBW overlaps, exact Laurent-polynomial Smith forms, x-degree decomposition coefficients and fresh complete primitive9 kernel; ordinary cone/factor proof separate',
 'B_original_cubic_critical_overlaps':4,'fixed_quadric_and_normal_cubic_Smith':smiths,
 'disjoint_parameter_conditions_gcd':1,'fresh_q_minus1_fixed_quadric':'k*y^2',
 'fresh_primitive9_field':'t^6+t^3+1; omega=t^6','primitive9_normal_rank':3,
 'Gamma_coefficients_in_b3_c3_bcy_y3':[str(J.to_sympy(c)) for c in coeff],
 'W1_classification':{'q=-1':'k*x*y^2','q^3=omega^2':'k*Gamma_q','otherwise':'0'},
 'not_claimed':['general x-dependent deformations covered','all proportional cube couplings classified','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_split_double_Ore_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','all_q_split_family_classified':True,'primitive9_kernel_dimension':1}))
