"""Remaining semisimple Q=0, pure-positive-commutator graph checks."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
h0,h1,h2,k,r,s,t,w=S.symbols('h0 h1 h2 k r s t w');H={(0,0):h0,(0,1):2*h1,(1,1):h2}
def engine(rr):
 @lru_cache(None)
 def nf(word):
  for i in range(len(word)-1):
   if word[i:i+2] in rr:
    out={}
    for mid,c in rr[word[i:i+2]].items():
     for v,d in nf(word[:i]+mid+word[i+2:]).items():out[v]=out.get(v,0)+c*d
    return {v:S.expand(c) for v,c in out.items() if S.expand(c)}
  return {word:S.Integer(1)}
 return nf
E=[v for v in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in v)%2==0];W=list(itertools.combinations_with_replacement(range(4),4));index={v:i for i,v in enumerate(W)}
def check(name,rr,mod=None):
 nf=engine(rr);count=0
 for word in itertools.product(range(4),repeat=3):
  if word[:2] not in rr or word[1:] not in rr:continue
  out={}
  for i,sgn in [(0,1),(1,-1)]:
   for mid,c in rr[word[i:i+2]].items():
    for v,d in nf(word[:i]+mid+word[i+2:]).items():out[v]=out.get(v,0)+sgn*c*d
  for c in out.values():assert (mod.reduce(S.expand(c))[1] if mod else S.expand(c))==0
  count+=1
 assert count==4
 N=S.zeros(4*len(W),10)
 for j,word in enumerate(E):
  for g in range(4):
   for raw,c in [(word+(g,),1),((g,)+word,-1 if g<2 else 1)]:
    for v,d in nf(raw).items():N[g*len(W)+index[v],j]+=c*d
 return N.applyfunc(S.expand)
swap={(1,0):{(0,1):1},(2,0):{(0,3):-1},(2,1):{(1,3):-1},(3,0):{(0,2):-1},(3,1):{(1,2):-1},(3,2):{(2,3):-1,**H}}
N=check('swap',swap);zero=N.subs({h0:0,h1:0,h2:0});rows=list(zero.T.rref()[1]);assert len(rows)==10
swapminor=S.expand(N[rows,:].det());assert swapminor!=0 and not swapminor.free_symbols
jr={(1,0):{(0,1):1},(2,0):{(0,2):-1},(2,1):{(1,2):1},(3,0):{(0,2):k+1,(0,3):-1},(3,1):{(1,2):k-1,(1,3):1},(3,2):{(2,3):1,(2,2):1,**H}}
N=check('Jordan',jr);bad=[(1,1,1),(1,2,2),(1,2,3),(1,3,3)];rows=[2*len(W)+index[v] for v in [(1,1,1,2),(1,2,2,2),(1,2,2,3),(1,2,3,3)]];cols=[E.index(v) for v in bad]
assert S.expand(N.extract(rows,cols).det())==16
assert N.extract(rows,[i for i in range(10) if i not in cols])==S.zeros(4,6)
opp={(1,0):{(0,1):1},(2,0):{(0,2):r,(0,3):t},(3,0):{(0,2):s,(0,3):w},(2,1):{(1,2):-w,(1,3):t},(3,1):{(1,2):s,(1,3):-r},(3,2):{(2,3):1,**H}}
G=S.groebner([r*w-s*t-1],r,s,t,w,h0,h1,h2);check('opposite',opp,G)
for eps,factor in [(-1,0),(1,1)]:
 rr={v:{word:S.sympify(c).subs({r:eps,w:eps,s:0,t:0}) for word,c in row.items()} for v,row in opp.items()};N=check('opposite_scalar',rr)
 other=1-factor;bad=[(other,other,other),(other,2,2),(other,2,3),(other,3,3)];rows=[2*len(W)+index[v] for v in [(other,other,other,2),(other,2,2,2),(other,2,2,3),(other,2,3,3)]];cols=[E.index(v) for v in bad]
 assert S.expand(N.extract(rows,cols).det())==16
 assert N.extract(rows,[i for i in range(10) if i not in cols])==S.zeros(4,6)
# Both-commutative opposite-separated dictionary on SU cross chart.
z1,z2,z3,z4=S.symbols('z1 z2 z3 z4');pf=-z1*z4+z2*z3
f=S.Matrix([[z2,-z1],[z4,-z3]]);g=S.Matrix([[z3,-z1],[z4,-z2]])
assert (f*g-pf*S.eye(2)).applyfunc(S.expand)==S.zeros(2)
assert S.expand(f.det()+pf)==0
# Exact six-linear atlas is unchanged by adding a pure positive top.
# Reconstruct both exceptional graph dictionaries from its cross matrix.
for name,b,values,target in [
 ('swap',S.Matrix([[0,1],[1,0]]),[0,1,0,0,1,0],S.Matrix([[0,-1,0,0],[0,0,0,-1],[-1,0,0,0],[0,0,-1,0]])),
 ('Jordan',S.Matrix([[-1,-1],[1,0]]),[0,k,1,-1,0,0],S.Matrix([[-1,0,0,0],[0,0,1,0],[k+1,-1,0,0],[0,0,k-1,1]]))]:
 A=S.zeros(4)
 for (i,j),c0 in zip(itertools.combinations(range(4),2),values):A[i,j]=c0;A[j,i]=-c0
 a0=S.Matrix([[0,1],[-1,0]]);M=S.zeros(4)
 for i,j,l,m in itertools.product(range(2),repeat=4):M[2*l+j,2*m+i]=-a0[i,l]*b[j,m]
 assert (-(-M.T*A.inv()).inv().T-target).applyfunc(S.cancel)==S.zeros(4)
out={'status':'PASS','scope':'remaining semisimple Q=0 pure-positive-commutator charts','swap':{'PBW':4,'normal_rank10_minor':str(swapminor)},'negative_Jordan':{'PBW':4,'non_x_factor_minor':16,'all_other_columns_on_chosen_rows':0},'both_commutative_opposite':{'universal_SL2_PBW':4,'f_not_scalar':'top V-degree forces all UV2 coefficients zero; remaining binary cubic factors','scalar_f_plus_or_minus_I_minors':[16,16]},'not_claimed':['pure-positive symmetric relation branch','nonsemisimple coverage','all H3 classification']}
Path(__file__).with_name('cubic_order2_22_Qzero_commutative_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS Qzero commutative: swap full minor',swapminor,'; Jordan minor16; universal opposite SL2 PBW and two scalar minors16')
