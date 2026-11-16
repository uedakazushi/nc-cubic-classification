"""Qzero symmetric branch and positive-only Jordan obstruction, exact certificates."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
q,r,z,k,vv,eta=S.symbols('q r z k vv eta');loc=1-vv*q*r
# Centralizer-U constraints on the four possible U*negative-square columns.
conditions=[([r*r-1,1+1/(q*q*r*r)],r*r-1),([r*r+1,1/(q*q*r*r)-1],r*r+1),([1/(r*r)-1,q*q*r*r+1],r*r-1),([1/(r*r)+1,q*q*r*r-1],r*r+1)]
for pol,target in conditions:
 generators=[S.fraction(S.cancel(e))[0] for e in pol]
 assert list(S.groebner(generators+[loc],vv,r,q))==list(S.groebner([q*q+1,target,loc],vv,r,q))
assert S.expand((r*r+1)-(r*r-1))==2
# Symmetric-square functor, basis u2,uv,v2 in the commutative associated graded.
def sym2(A):
 a,b,c,d=A[0,0],A[0,1],A[1,0],A[1,1]
 return S.Matrix([[a*a,a*b,b*b],[2*a*c,a*d+b*c,2*b*d],[c*c,c*d,d*d]])
f=S.Matrix([[-z,k+z],[0,-z]]);g=S.Matrix([[-z,-k+z],[0,-z]])
assert S.rem(S.expand((sym2(f)-S.eye(3)).det()-(-8)),z*z+1,z)==0
assert S.rem(S.expand((sym2(g)-S.eye(3)).det()-(-8)),z*z+1,z)==0
z1,z2,z3,z4=S.symbols('z1 z2 z3 z4');pf=-z1*z4+z2*z3
f=S.Matrix([[z2,-z1],[z4,-z3]]);g=S.Matrix([[-z3,z1],[-z4,z2]])
assert (f*g+pf*S.eye(2)).applyfunc(S.expand)==S.zeros(2)
Sf,Sg=sym2(f),sym2(g)
assert (Sf*Sg-pf*pf*S.eye(3)).applyfunc(S.expand)==S.zeros(3)
assert (Sf*(Sg+S.eye(3))-(Sf-S.eye(3))-(pf*pf+1)*S.eye(3)).applyfunc(S.expand)==S.zeros(3)
# Positive-only Jordan: yx=xy+eta*x2; mu(y)=y+x, mu(V)=-V.
@lru_cache(None)
def nf(word):
 for i in range(len(word)-1):
  if word[i:i+2]==(1,0):
   out={}
   for mid,c in [((0,1),1),((0,0),eta)]:
    for v,d in nf(word[:i]+mid+word[i+2:]).items():out[v]=out.get(v,0)+c*d
   return {v:S.expand(c) for v,c in out.items() if S.expand(c)}
 return {word:S.Integer(1)}
E=[v for v in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in v)%2==0];index={v:i for i,v in enumerate(E)};N=-S.eye(10)
for j,word in enumerate(E):
 options=[[(0,)] if v==0 else ([(1,),(0,)] if v==1 else [(v,)]) for v in word]
 for choices in itertools.product(*options):
  raw=tuple(i for v in choices for i in v)
  for v,c in nf(raw).items():N[index[v],j]+=c
fixed=[(0,0,0),(0,2,2),(0,2,3),(0,3,3)];cols=[i for i,v in enumerate(E) if v not in fixed]
rows=[index[v] for v in [(0,0,0),(0,0,1),(0,1,1),(0,2,2),(0,2,3),(0,3,3)]]
assert S.expand(N.extract(rows,cols).det())==6
assert N[:,[index[v] for v in fixed]]==S.zeros(10,4)
out={'status':'PASS','scope':'canonical Q=0 completion beyond pure-positive commutative semisimple branch','symmetric_positive_quantum_chart':{'four_localized_ideal_equalities':True,'possible_parameters':'q2=-1; r2=1 gives common factor x, r2=-1 gives common factor y','pure_cubic_and_Uuv_columns':'centralizer U zero'},'negative_Jordan_symmetric_square_fixed_minors':[-8,-8],'both_commutative_projection':'Sf*(Sg+I)-(Sf-I)=2I on Pf=1; thus simultaneous fixed/anti-fixed quadratic kernel zero','positive_only_Jordan':{'universal_relation':'yx=xy+eta*x2','fixed_cubic_basis':['x3','xu2','xuv','xv2'],'constant_complement_minor':6},'dependencies':['rank1-cross domain obstruction','six-linear odd atlas','zero-top epsilon+ exact normal exclusions','canonical right Zhang untwist','one-sided Jordan exclusion'],'conclusion':'all canonical Qzero H3 in mixed-rank4 (2,2), including all Jordan types, are curved Clifford cuts','not_claimed':['Q nonzero positive-top nonzero coverage','global H3 classification','componenthood','intrinsic relative descent']}
Path(__file__).with_name('cubic_order2_22_Qzero_complete_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS Qzero completion: four localized ideals, symmetric-square minors -8, identity2I, Jordan fixed minor6')
