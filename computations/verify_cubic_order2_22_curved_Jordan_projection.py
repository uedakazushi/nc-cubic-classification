"""All curved Jordan-positive / negative-sign separated graphs: exact shear factor kernel."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
t,a,b=S.symbols('t a b');records=[]
for eps in [1,-1]:
 F=S.Matrix([[eps,eps-t],[0,eps]]);G=S.Matrix([[eps,eps+t],[0,eps]])
 assert F*G==S.Matrix([[1,2],[0,1]]) and F.det()==G.det()==1
 rules={(1,0):{(0,1):S.Integer(1),(0,0):S.Integer(1),(2,2):a,(3,3):b},(3,2):{(2,3):-S.Integer(1)},(2,0):{(0,2):S.Integer(eps)},(2,1):{(1,2):S.Integer(eps),(0,2):eps-t},(3,0):{(0,3):S.Integer(eps)},(3,1):{(1,3):S.Integer(eps),(0,3):eps+t}}
 @lru_cache(None)
 def nf(word):
  for pos in range(len(word)-1):
   if word[pos:pos+2] in rules:
    out={}
    for mid,c in rules[word[pos:pos+2]].items():
     for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,0)+c*d
    return {w:S.expand(c) for w,c in out.items() if S.expand(c)}
  return {word:S.Integer(1)}
 overlaps=0
 for word in itertools.product(range(4),repeat=3):
  if word[:2] not in rules or word[1:] not in rules:continue
  out={}
  for pos,sgn in [(0,1),(1,-1)]:
   for mid,c in rules[word[pos:pos+2]].items():
    for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,0)+sgn*c*d
  assert all(S.expand(c)==0 for c in out.values());overlaps+=1
 assert overlaps==4
 words=[w for w in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in w)%2==0];index={w:i for i,w in enumerate(words)};H=S.zeros(10)
 for col,word in enumerate(words):
  choices=[[(x,S.Integer(1))] if x!=1 else [(1,S.Integer(1)),(0,S.Integer(2))] for x in word]
  for term in itertools.product(*choices):
   raw=tuple(x for x,c in term);co=S.prod(c for x,c in term)
   for w,d in nf(raw).items():H[index[w],col]+=co*d
 N=H-S.eye(10)
 fixed=[(0,0,0),(0,2,2),(0,2,3),(0,3,3)]
 for word in fixed:assert N[:,index[word]]==S.zeros(10,1)
 rr=[(0,0,0),(0,0,1),(0,1,1),(0,2,2),(0,2,3),(0,3,3)]
 cc=[(0,0,1),(0,1,1),(1,1,1),(1,2,2),(1,2,3),(1,3,3)]
 assert S.expand(N.extract([index[w] for w in rr],[index[w] for w in cc]).det())==384
 records.append({'epsilon':eps,'PBW_overlaps':4,'normalizer_composition':'y->y+2*x, x fixed, negative variables negated','shear_kernel_minor':384,'fixed_kernel':['x^3','x*u^2','x*u*v','x*v^2']})
out={'status':'PASS','scope':'curved Jordan positive projection with q=-1 negative plane, all coefficient/boundary values',
 'cases':records,'conclusion':'every H3 normal cubic would be shear-fixed and hence divisible by x; no H3 in this chart',
 'proof':'papers/sections/cubic_order2_22_curved_Jordan_projection.tex',
 'not_claimed':['rank1 positive projection','all nonzero-positive-top rank4','relative family classification']}
Path(__file__).with_name('cubic_order2_22_curved_Jordan_projection_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS curved Jordan projection: 8 universal PBW overlaps and both constant shear minors384')
