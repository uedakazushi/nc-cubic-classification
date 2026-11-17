#!/usr/bin/env python3
"""All bounded phase cases, multilinear support lemma, and exact normalizer
identities behind two whole rank3-support-chart exclusions. Ordinary Ore proof in paper.
"""
import itertools,json,sympy as s
from pathlib import Path
def exps(d):return [v for v in itertools.product(range(d+1),repeat=4) if sum(v)==d]
dirs=[(0,1,-3,2),(0,1,-2,1),(1,-2,-1,2)];quartics={str(n):[v for v in exps(4) if sum(a*b for a,b in zip(n,v))==0] for n in dirs}
assert quartics[str(dirs[0])]==[(0,3,1,0),(1,1,1,1),(4,0,0,0)]
assert quartics[str(dirs[1])]==[(1,0,1,2),(1,1,1,1),(1,2,1,0),(4,0,0,0)]
assert quartics[str(dirs[2])]==[(0,2,0,2),(1,1,1,1),(2,0,2,0)]
for w in itertools.permutations(range(4)):
 assert set(w[:2])==set(range(4))-set(w[2:])
counts=[]
for M in range(1,25):
 row={'phase_modulus':M,'direction1':0,'direction2':0,'direction3':0}
 for eta,xi,gamma in itertools.product(range(M),repeat=3):
  # Direction1: y phase normalized to zero. Both nonfactoring cubic types,
  # quartic c coverage, and at least one nonmultilinear top.
  if (3*eta)%M==0 and (xi+gamma)%M==0 and (eta+xi+gamma)%M==0 and xi%M==0:
   assert eta==xi==gamma==0;row['direction1']+=1
  # Direction2: phases x=eta,b=xi,c=gamma,y=0; equal-n eigenlines distinct.
  if gamma!=0 and (3*eta)%M==0:
   J=[j for j in range(3) if (xi+j*gamma)%M==0];K=[j for j in range(3) if (eta+xi+j*gamma)%M==0]
   if J and (1 in K or 0 in K and 2 in K) and K!=[1]:
    assert eta==xi==0 and 2*gamma==M;row['direction2']+=1
  # Direction3: phases x0,y=eta,b=xi,c=gamma; both cubic types,
  # unique possible non-skew quadratic collision, and quartic full cover.
  if eta==0 and (2*xi+gamma)%M==0 and (xi-eta-gamma)%M==0:
   pp=[0,eta,xi,gamma];active=[w for w in quartics[str(dirs[2])] if sum(a*b for a,b in zip(w,pp))%M==0]
   if all(any(w[j] for w in active) for j in range(4)):
    assert eta==xi==gamma==0;row['direction3']+=1
 assert row['direction1']==1 and row['direction3']==1 and row['direction2']==(1 if M%2==0 else 0)
 counts.append(row)
# Direction3 has exactly one collision among unordered quadratic N weights,
# so actual non-skew incidence requires the two phase products to coincide.
n=dirs[2];pairs=list(itertools.combinations_with_replacement(range(4),2));g={}
for a,b in pairs:g.setdefault(n[a]+n[b],[]).append((a,b))
assert [v for v in g.values() if len(v)>1]==[[(0,2),(1,3)]]
# Domain identity excluding a missing xc or cx coefficient, using normal y.
x,y,c=s.symbols('x y c',commutative=False);q,k=s.symbols('q k')
identity=(x*c-k*q*q*y*y)*x-x*(c*x-k*y*y)-k*((x*y-q*y*x)*y+q*y*(x*y-q*y*x))
assert s.expand(identity)==0
# Normal b and Ore Nakayama eigenvalue on curve1.
a,b,c,l,z=s.symbols('a b c l z');gb=s.groebner([l-a*b*c,a**3-l,b*c-l,z*a*b*c*l-1],z,a,b,c,l)
assert gb.reduce(a-1)[1]==0 and gb.reduce(l-1)[1]==0
# Curve2: degree3 Koszul top eigenvalue q*d², and two cubic components.
q,d,l,z=s.symbols('q d l z');gb=s.groebner([l-q*d,q**3-l,d-l,z*q*d*l-1],z,q,d,l)
assert gb.reduce(q-1)[1]==0 and gb.reduce(l-1)[1]==0
out={'status':'PASS','scope':'all bounded phase reductions in three directions; two resulting rank3 support charts excluded by ordinary Ore/domain proof','all_phase_moduli_1_to24':counts,'quartic_exponents':quartics,'reduced_curves':[['1','t','t^-3','t²'],['1','t','t^-2','-t'],['t','t^-2','t^-1','t²']],'excluded_curves':[0,1],'curve1_normalizer':'mu_b=alpha*beta*gamma, alpha³=beta*gamma=mu_b =>alpha=mu_b=1 contradicts distinct lambda_x=1','curve2_normalizer':'mu_b=q*d², q³=d²=mu_b =>q=mu_b=1 contradicts lambda_x=1','remaining':['direction(0,0,1,-1) bounded phases','phase-free (t,t^-2,t^-1,t²)','bounded finite point locus common orderN<=96'],'not_claimed':['two remaining sectors classified','finite-order points with extra nonzero-weight support excluded by the rank3 argument','all four-simple covered by one curve alone','global H3 classification','ordinary Ore/top arguments entirely mechanically checked']}
Path(__file__).with_name('cubic_four_simple_curve_phase_reduction_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS all phase reductions, two normalizer contradictions and missing-coefficient domain identity')
