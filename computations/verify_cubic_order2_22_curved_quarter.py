"""Quarter-root negative planes: complete normal-weight supports and curvature PBW."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
p,r,q,k,z=S.symbols('p r q k z');phase=q*q+1;loc=1-z*p*r
words=[w for w in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in w)%2==0]
groups={
 'x_cube':[p**3-1,r**3+1], 'x_factor':[p-1,r-q], 'y_factor':[p-1,r-1], 'y_cube':[p**3-1,r**3-q],
 'x_u_square':[p+1,r+1], 'x_v_square':[p+1,r-1], 'y_u_square':[p+1,r+q], 'y_v_square':[p+1,r-q]}
assignment=['x_cube','x_factor','y_factor','x_u_square','x_factor','x_v_square','y_cube','y_u_square','y_factor','y_v_square']
assert len(words)==len(assignment)==10
for word,name in zip(words,assignment):
 nx,ny,nu,nv=[word.count(i) for i in range(4)]
 wu=r**nx*(q/r)**ny*q**nv;wv=(p/r)**nx*(-q*r/p)**ny*(-q)**nu
 eq=[S.fraction(S.cancel(wu+1))[0],S.fraction(S.cancel(wv+1))[0],phase,loc]
 assert list(S.groebner(eq,p,r,q,z))==list(S.groebner(groups[name]+[phase,loc],p,r,q,z))
for a,b in itertools.combinations(groups.values(),2):assert list(S.groebner(a+b+[phase,loc],p,r,q,z))==[1]
rules={(1,0):{(0,1):S.Integer(1)/p,(2,3):-k/p},(3,2):{(2,3):-q},(2,0):{(0,2):r},(2,1):{(1,2):q/r},(3,0):{(0,3):p/r},(3,1):{(1,3):-q*r/p}}
def engine(rules):
 @lru_cache(None)
 def nf(word):
  for pos in range(len(word)-1):
   if word[pos:pos+2] in rules:
    out={}
    for mid,c in rules[word[pos:pos+2]].items():
     for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,0)+c*d
    return {w:S.cancel(c) for w,c in out.items() if S.cancel(c)}
  return {word:S.Integer(1)}
 return nf
def overlaps(rules,ideal,gens):
 nf=engine(rules);G=S.groebner(ideal,*gens);count=0
 for word in itertools.product(range(4),repeat=3):
  if word[:2] not in rules or word[1:] not in rules:continue
  out={}
  for pos,sgn in [(0,1),(1,-1)]:
   for mid,c in rules[word[pos:pos+2]].items():
    for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,0)+sgn*c*d
  assert all(G.reduce(S.expand(S.fraction(S.cancel(c))[0]))[1]==0 for c in out.values());count+=1
 assert count==4
 return nf
nf=overlaps(rules,[phase],[q,p,r,k])
for word in set(nf((2,3,1)))|set(nf((1,2,3))):
 c=(nf((2,3,1)).get(word,0)-nf((1,2,3)).get(word,0)).subs({p:1,r:1})
 assert S.rem(S.fraction(S.cancel(c))[0],phase,q)==0
# General non-diagonal commutative-positive projection, det(F)=q.
a,b,c,d=S.symbols('a b c d');matrules={(1,0):{(0,1):S.Integer(1),(2,3):-k},(3,2):{(2,3):-q},(2,0):{(0,2):a,(1,2):c},(2,1):{(0,2):b,(1,2):d},(3,0):{(0,3):-q*d,(1,3):q*c},(3,1):{(0,3):q*b,(1,3):-q*a}}
overlaps(matrules,[a*d-b*c-q,phase],[a,b,c,d,q,k])
# Repeated eigenvalue A has A^2=q, hence A^4=-1. No relevant odd weight is -1.
A=S.symbols('A')
for f in [A+1,A**3+1,1-A]:assert S.gcd(A**4+1,f)==1
# The top lift of a curvature k*uv is k*(uv+q*vu)/2 modulo the base relation.
bv=S.Matrix([0,1,-q,0]);cv=S.Matrix([0,k/2,q*k/2,0]);Q=-(bv*cv.T+cv*bv.T)
conditions=[Q[0,1]-Q[0,2],Q[1,3]-Q[2,3],Q[1,1]-Q[2,2],Q[0,3]-Q[1,2]]
assert all(S.rem(S.expand(x),phase,q)==0 for x in conditions)
out={'status':'PASS','scope':'q^2=-1 negative plane with nondegenerate positive projection, separated odd graph charts',
 'checks':['ten localized support ideals','28 pairwise branch-disjointness certificates','four diagonal-curvature PBW overlaps','four det(F)=q matrix-curvature PBW overlaps','uv commutes y on the right-factor branch','repeated-eigenvalue odd weights have no -1 eigenspace','cyclic negative curvature top'],
 'normal_support_groups':{name:[str(x) for x in eq] for name,eq in groups.items()},
 'conclusion':'every normal cubic in the diagonal charts has an explicit linear factor; repeated-eigenvalue commutative/Jordan charts have normal kernel0',
 'proof':'papers/sections/cubic_order2_22_curved_quarter.tex',
 'not_claimed':['rank1 positive projection','all rank4 moduli','relative descent']}
Path(__file__).with_name('cubic_order2_22_curved_quarter_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS curved quarter-root charts: 10 support ideals, 28 disjoint pairs, 8 PBW overlaps and all repeated roots')
