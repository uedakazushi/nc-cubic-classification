#!/usr/bin/env python3
"""Finite exact exponent atlas and integer rank bounds. The regrading, domain
factorization and torus-coset arguments are ordinary proofs in the paper.
"""
import itertools,math,json,sympy as s
from collections import Counter
from pathlib import Path
def exps(d):return [v for v in itertools.product(range(d+1),repeat=4) if sum(v)==d]
def det3(m):
 a,b,c=m;return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def rawcross(rows):return tuple((-1)**j*det3([tuple(r[k] for k in range(4) if k!=j) for r in rows]) for j in range(4))
def primitive(n):
 g=math.gcd(*n)
 if not g:return None
 if next(x for x in n if x)<0:g=-g
 return tuple(x//g for x in n)
def canon(n):
 out=[]
 for pp in itertools.permutations(range(4)):
  v=tuple(n[j] for j in pp)
  if next(x for x in v if x)<0:v=tuple(-x for x in v)
  out.append(v)
 return min(out)
U=[]
for j,k in itertools.combinations(range(4),2):U.append(tuple(1 if i==j else -1 if i==k else 0 for i in range(4)))
for j in range(4):
 for k,l in itertools.combinations([i for i in range(4) if i!=j],2):U.append(tuple(2 if i==j else -1 if i in [k,l] else 0 for i in range(4)))
for S in [(0,1),(0,2),(0,3)]:U.append(tuple(1 if i in S else -1 for i in range(4)))
V=exps(3);W=exps(4);assert len(U)==21 and len(V)==20 and len(W)==35
# Independent quartic lemma: rational plane contains no full-variable support.
lemma=[]
for u in [(1,-1,0,0),(2,-1,-1,0),(1,1,-1,-1)]:
 for v in V:
  ws=[w for w in W if not any(rawcross([u,v,w]))];covered=[any(w[j] for w in ws) for j in range(4)];assert not all(covered)
  lemma.append({'u':u,'v':v,'quartics_in_rational_plane':ws,'missing':[j for j,x in enumerate(covered) if not x]})
# All primitive rank3 kernels compatible with quartic support, then sumzero.
directions={}
for u,v,w in itertools.product(U,V,W):
 n=primitive(rawcross([u,v,w]))
 if n is None or n in directions:continue
 active=[q for q in W if sum(a*b for a,b in zip(q,n))==0]
 if all(any(q[j] for q in active) for j in range(4)):directions[n]=(u,v,w)
assert len(directions)==1062
orbits=sorted({canon(n) for n in directions if sum(n)==0});assert len(orbits)==10
# Regrading coefficient of second logarithmic Euler derivative.
N,S1,S2,R2=s.symbols('N S1 S2 R2');nn=s.symbols('n:4');kk=s.symbols('k:6')
poly=-sum((N+x)**2 for x in nn)+sum((2*N+x)**2 for x in kk)-sum((3*N-x)**2 for x in nn)+(4*N)**2
expected=4*N*sum(nn)+sum(x*x for x in kk)-2*sum(x*x for x in nn)+4*N*sum(kk)
assert not s.expand(poly-expected)
rankdata=[]
for n in orbits:
 c=Counter(n);Wt=Counter(a+b for a in n for b in n);caps={w:Wt[w]-max(c[a]+c[b]-1 for a in c for b in c if a+b==w) for w in Wt}
 pos=[w for w in Wt if w>0 and -w in Wt];solutions=[]
 for rr in itertools.product(*(range(min(caps[w],caps[-w],3)+1) for w in pos)):
  r0=6-2*sum(rr)
  if not(0<=r0<=caps.get(0,0)) or sum(r*w*w for r,w in zip(rr,pos))!=sum(a*a for a in n):continue
  out={0:r0}
  for w,r in zip(pos,rr):
   if r:out[w]=out[-w]=r
  solutions.append(out)
 assert len(solutions)==1
 cubes=[v for v in V if sum(a*b for a,b in zip(v,n))==0]
 rankdata.append({'direction':n,'relation_weights':solutions[0],'domain_caps':caps,'fixed_cubic_exponents':cubes})
remaining=[(0,0,1,-1),(0,1,-3,2),(0,1,-2,1),(1,-2,-1,2)]
single=[(1,-6,2,3),(1,-5,-2,6),(1,-4,-3,6),(1,-4,1,2)]
for row in rankdata:
 n=tuple(row['direction'])
 if n in single:
  assert len(row['fixed_cubic_exponents'])==1
  pair=[j for j,x in enumerate(row['fixed_cubic_exponents'][0]) if x];assert len(pair)==2
  w=n[pair[0]]+n[pair[1]];assert sum(1 for a in range(4) for b in range(4) if n[a]+n[b]==w)==2 and row['relation_weights'][w]==1
 elif n==(1,-2,-2,3):
  assert row['fixed_cubic_exponents']==[(2,0,1,0),(2,1,0,0)] and row['relation_weights'][-1]==2 and row['relation_weights'][4]==1
 elif n==(1,-3,-2,4):
  assert row['fixed_cubic_exponents']==[(0,0,2,1),(2,0,1,0)] and row['relation_weights'][2]==1 and row['relation_weights'][-1]==1
 else:assert n in remaining
# All matrix determinant bounds and torsion phase bounds, including a second cubic row.
bounds=[]
for u in [(1,-1,0,0),(2,-1,-1,0),(1,1,-1,-1)]:
 gcds=set();dq=set();dc=set()
 for v,w in itertools.product(V,W):
  n=rawcross([u,v,w]);g=math.gcd(*n)
  if g:gcds.add(g)
  for w2 in W:
   d=abs(sum(a*b for a,b in zip(n,w2)))
   if d:dq.add(d)
  for v2 in V:
   d=abs(sum(a*b for a,b in zip(n,v2)))
   if d:dc.add(d)
 bounds.append({'u':u,'max_gcd3minors':max(gcds),'max_det_two_quartics':max(dq),'max_det_two_cubics':max(dc),'gcd3minors':sorted(gcds),'determinants_two_quartics':sorted(dq),'determinants_two_cubics':sorted(dc)})
assert [b['max_gcd3minors'] for b in bounds]==[12,24,12]
assert [b['max_det_two_quartics'] for b in bounds]==[48,96,48]
assert [b['max_det_two_cubics'] for b in bounds]==[36,72,36]
assert max((2 if j==0 else 1)*b['max_gcd3minors'] for j,b in enumerate(bounds))==24
assert max((2 if j==0 else 1)*max(b['max_det_two_quartics'],b['max_det_two_cubics']) for j,b in enumerate(bounds))==96
out={'status':'PASS','scope':'complete necessary spectral cover: bounded finite torsion points or four phase-decorated one-parameter directions; no existence or H3 sufficiency','independent_quartic_lemma_all60':lemma,'rank3_support_directions_before_sumzero':len(directions),'sumzero_permutation_parameter_inversion_orbits':rankdata,'six_excluded_directions':single+[(1,-2,-2,3),(1,-3,-2,4)],'four_remaining_curve_directions':remaining,'integer_bounds_by_quadratic_type':bounds,'finite_point_common_order_bound':96,'curve_phase_common_order_bound':24,'parameter':'arbitrary nonzero t, including roots of unity; phase order some M<=24, not necessarily dividing24','full_support_lattice':'one quadratic resonance plus all actual cubic G and quartic top support exponents; rank3 or4, so finite-order points with rank3 remain covered by curves','not_claimed':['geometric orbit quotient','all four-simple classified','all finite points admissible','all phase curves contain H3','global H3 classification','ordinary proofs mechanically checked in entirety']}
Path(__file__).with_name('cubic_four_simple_spectral_curve_atlas_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS complete necessary four-curve / bounded-finite spectral atlas')
