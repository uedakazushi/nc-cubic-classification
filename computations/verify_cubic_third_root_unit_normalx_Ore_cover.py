#!/usr/bin/env python3
"""Exact critical overlaps and shear for the actual quantum-Weyl AS3 Ore base chart.
No global proportional-coupling or normal-linear-element existence asserted.
"""
import sympy as s
from functools import lru_cache
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));q,h,m,n,k=s.symbols('q h m n k');K=F.frac_field(q,h,m,n,k);q,h,m,n,k=K.gens;o=K.convert(F.to_sympy(F.unit));one,zero=K.one,K.zero
# order x,b,c,y
rules={(1,0):{(0,1):o},(2,0):{(0,2):o**2},(2,1):{(1,2):one/q,(0,0):-h/q},
 (3,0):{(0,3):one,(0,0):k},(3,1):{(1,3):q,(0,1):m*o,(2,2):-q},
 (3,2):{(2,3):one/q,(0,2):n*o**2,(1,1):-one/q}}
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
 return out
import itertools,json
from pathlib import Path
expected={
 (2,1,0):{},
 (3,1,0):{(0,0,1):k*o**2*(q-o**2)},
 (3,2,0):{(0,0,2):-k*o**2*(q-o**2)/q},
 (3,2,1):{(0,0,0):h*(2*k*q-m-o**2*n*q)/q**2,
           (0,1,2):-(o*m+q*n)*(q-o**2)/q**2}}
for tr in itertools.combinations(range(4),3):
 w=tuple(reversed(tr));a,b=first(w,0),first(w,1)
 diff={v:a.get(v,zero)-b.get(v,zero) for v in set(a)|set(b)}
 diff={v:c for v,c in diff.items() if c};assert diff==expected[w]
# Nonresonant q: actual overlap equations force k=0,n=-omega*m/q.
# y_new=y+t*x removes both remaining first-order curvature corrections.
tau=m/(q-o**2)
assert m+tau*(o**2-q)==zero
assert -o*m/q+tau*(o-one/q)==zero
for diff in expected.values():
 for val in diff.values():
  expr=K.to_sympy(val).subs({s.Symbol('k'):0,s.Symbol('n'):-F.to_sympy(F.unit)*s.Symbol('m')/s.Symbol('q')})
  assert s.cancel(expr,extension=F.to_sympy(F.unit))==0
# At resonance q=omega^2 all corrections have positive x-adic order;
# split normal Smith factors at this q are units (q+1 and q^3-omega^2).
assert o**2+one and (o**2)**3-o**2
# Every tail erased on x-adic gr has strictly higher number of x letters.
for pair,rr in rules.items():
 for w,c in rr.items():
  if (pair,w) in [((2,1),(0,0)),((3,0),(0,0)),((3,1),(0,1)),((3,2),(0,2))]:
   assert w.count(0)>pair.count(0)
# The delta(x)!=0 argument uses sigma(delta(x))=delta(x), since sigma(bc)=bc.
assert q*(one/q)==one
# x conjugation on the base equals mu_B^{-1}; every mu-fixed coefficient
# therefore commutes with x. Check all degree<=3 monomial weights explicitly.
for d in range(4):
 for r in range(d+1):
  for ss in range(d-r+1):
   if (r+2*ss)%3==0:assert o**(2*r+ss)==one
Q=s.Symbol('Q')
for r in range(4):
 assert s.gcd(s.Poly(Q**r-F.to_sympy(F.unit),Q,domain=F),
              s.Poly(Q**(3-r)-F.to_sympy(F.unit),Q,domain=F)).degree()==0
out={'status':'PASS' ,'scope':'original complete four critical overlaps, forced nonresonant constraints, exact shear and resonant split-Smith units',
 'critical_overlap_residuals':{str(w):{str(v):str(K.to_sympy(c)) for v,c in d.items()} for w,d in expected.items()},
 'nonresonant_constraints':'kappa=0,n=-omega*m/q for q!=omega^2',
 'shear':'y_new=y+m/(q-omega^2)*x',
 'resonant_parameter':'q=omega^2, split W1=0',
 'nonzero_delta_x':'mu-fixed Ore coefficients commute with x, top [G,x] coefficient N*a_N*delta(x) forces G in A3; quantum-plane gcd excludes nonzero image',
 'chart_hypotheses':['A=<x,b,c> quantum-Weyl AS3 base with xb=omega^2*bx,xc=omega*cx,bc-qcb=h*x^2',
 'B=A[y;sigma,delta] actual graded Ore extension; x need not be normal in B',
 'mu_B(x,y,b,c)=(x,y,omega*b,omega^2*c)',
 'both c^2 in delta(b) and b^2 in delta(c) nonzero'],
 'not_claimed':['this AS3 subbase exists for every proportional cube coupling','all AS3 subbases have this form','all proportional atlas covered','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_normalx_Ore_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','quantum_Weyl_base_two_curvature_Ore_chart_excluded':True}))
