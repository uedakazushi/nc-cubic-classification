"""Curved SL2 normalizing chart: universal PBW and exact non-diagonal shear kernels."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
r,s,t,w,a,b=S.symbols('r s t w a b');det=r*w-s*t
rules={(1,0):{(0,1):S.Integer(1),(2,2):-a,(3,3):-b},(3,2):{(2,3):-S.Integer(1)},(2,0):{(0,2):r,(1,2):t},(2,1):{(0,2):s,(1,2):w},(3,0):{(0,3):w,(1,3):-t},(3,1):{(0,3):-s,(1,3):r}}
def engine(rules):
 @lru_cache(None)
 def nf(word):
  for pos in range(len(word)-1):
   if word[pos:pos+2] in rules:
    out={}
    for mid,c in rules[word[pos:pos+2]].items():
     for v,d in nf(word[:pos]+mid+word[pos+2:]).items():out[v]=out.get(v,0)+c*d
    return {v:S.expand(c) for v,c in out.items() if S.expand(c)}
  return {word:S.Integer(1)}
 return nf
nf=engine(rules);G=S.groebner([det-1],r,s,t,w,a,b);overlaps=0
for word in itertools.product(range(4),repeat=3):
 if word[:2] not in rules or word[1:] not in rules:continue
 out={}
 for pos,sgn in [(0,1),(1,-1)]:
  for mid,c in rules[word[pos:pos+2]].items():
   for v,d in nf(word[:pos]+mid+word[pos+2:]).items():out[v]=out.get(v,0)+sgn*c*d
 assert all(G.reduce(S.expand(c))[1]==0 for c in out.values());overlaps+=1
assert overlaps==4
# Pure negative cyclic top deformation: image=span(positive comm-h, negative anti).
cU=S.Matrix([0,1,-1,0]);bV=S.Matrix([0,1,1,0]);hV=S.Matrix([a,0,0,b]);R1=cU.col_join(-hV);R2=S.zeros(4,1).col_join(bV)
Even=R1*R2.T+R2*R1.T;Q=Even[4:,4:]
assert Q[0,1]==Q[0,2] and Q[1,3]==Q[2,3] and Q[1,1]==Q[2,2] and Q[0,3]==Q[1,2]
assert Even.extract([1,5],[1,5]).det()==-1
# Both non-diagonal SL2 types have F=epsilon*J, J(x)=x,J(y)=y+x.
E=[(0,0,0),(0,0,1),(0,1,1),(1,1,1),(0,2,2),(1,2,2),(0,3,3),(1,3,3)];index={v:i for i,v in enumerate(E)}
records=[]
for eps in [1,-1]:
 sub={r:eps,s:eps,t:0,w:eps};rr={word:{v:S.expand(c.subs(sub)) for v,c in row.items() if S.expand(c.subs(sub))} for word,row in rules.items()};ff=engine(rr);H=S.zeros(8)
 for col,word in enumerate(E):
  terms=[[(0,)] if x==0 else ([(1,),(0,)] if x==1 else [(x,)]) for x in word]
  for choices in itertools.product(*terms):
   raw=tuple(i for v in choices for i in v)
   for v,c in ff(raw).items():H[index[v],col]+=c
 N=H-S.eye(8)
 assert N**4==S.zeros(8)
 for v in [(0,0,0),(0,2,2),(0,3,3)]:assert N[:,index[v]]==S.zeros(8,1)
 row=[index[v] for v in [(0,0,0),(0,0,1),(0,1,1),(0,2,2),(0,3,3)]]
 col=[index[v] for v in [(0,0,1),(0,1,1),(1,1,1),(1,2,2),(1,3,3)]]
 assert S.expand(N.extract(row,col).det())==6
 records.append({'F':'J' if eps==1 else '-J','shear_fixed_E_basis':['x^3','x*u^2','x*v^2'],'fixed_kernel_minor':6,'normal_candidate_factor':'x*u*v' if eps==1 else 'x*(c*x^2+d*u^2+e*v^2)'})
out={'status':'PASS','scope':'all F in SL2, [x,y]=alpha*u^2+beta*v^2, uv=-vu, u acts F and v inverse',
 'universal_PBW_overlaps':4,'cyclic_top_deformation_rank2_minor':-1,'non_diagonal_cases':records,
 'conclusion':'all non-diagonal candidates factor; diagonal cases already classified, so only the known zero-curvature sign family gives H3',
 'proof':'papers/sections/cubic_order2_22_curved_SL2.tex',
 'not_claimed':['all nonzero-top rank4 graphs','general non-inverse normalizing matrices','relative descent']}
Path(__file__).with_name('cubic_order2_22_curved_SL2_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS full curved SL2: 4 universal PBW overlaps, cyclic top and both exact shear kernels with minor6')
