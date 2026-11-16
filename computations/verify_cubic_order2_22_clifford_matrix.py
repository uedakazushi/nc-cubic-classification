"""All invertible F: universal curved inverse-matrix Ore chart, exceptional kernels."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
r,s,t,w,h0,h1,h2=S.symbols('r s t w h0 h1 h2');D=r*w-s*t
h={(0,0):h0,(0,1):2*h1,(1,1):h2}
rules={(1,0):{(0,1):1},(2,0):{(0,2):r,(1,2):t},(2,1):{(0,2):s,(1,2):w},(3,0):{(0,3):w/D,(1,3):-t/D},(3,1):{(0,3):-s/D,(1,3):r/D},(3,2):{(2,3):-D,**{v:D*c for v,c in h.items()}}}
def engine(rr):
 @lru_cache(None)
 def nf(word):
  for i in range(len(word)-1):
   if word[i:i+2] in rr:
    out={}
    for mid,c in rr[word[i:i+2]].items():
     for v,d in nf(word[:i]+mid+word[i+2:]).items():out[v]=out.get(v,0)+c*d
    return {v:S.cancel(c) for v,c in out.items() if S.cancel(c)}
  return {word:S.Integer(1)}
 return nf
nf=engine(rules);overlaps=0
for word in itertools.product(range(4),repeat=3):
 if word[:2] not in rules or word[1:] not in rules:continue
 out={}
 for i,sgn in [(0,1),(1,-1)]:
  for mid,c in rules[word[i:i+2]].items():
   for v,d in nf(word[:i]+mid+word[i+2:]).items():out[v]=out.get(v,0)+sgn*c*d
 assert all(S.cancel(c)==0 for c in out.values());overlaps+=1
E=[v for v in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in v)%2==0]
words=list(itertools.combinations_with_replacement(range(4),4));index={v:i for i,v in enumerate(words)}
def matrix(sub):
 rr={v:{word:S.cancel(c.subs(sub)) if hasattr(c,'subs') else S.Integer(c) for word,c in row.items()} for v,row in rules.items()};ff=engine(rr);N=S.zeros(4*len(words),10)
 for j,word in enumerate(E):
  for g in range(4):
   for raw,c in [(word+(g,),1),((g,)+word,-1 if g<2 else 1)]:
    for v,d in ff(raw).items():N[g*len(words)+index[v],j]+=c*d
 return N.applyfunc(S.expand)
I=matrix({r:1,s:0,t:0,w:1})
K=S.zeros(10,2)
for j,u0 in enumerate([0,1]):
 K[E.index((u0,2,3)),j]=1
 for v,c in h.items():K[E.index(tuple(sorted((u0,)+v))),j]-=c/2
assert I*K==S.zeros(I.rows,2)
zero=I.subs({h0:0,h1:0,h2:0});cols=list(zero.rref()[1]);rows=list(zero[:,cols].T.rref()[1]);minor=S.expand(I.extract(rows,cols).det());assert minor!=0 and not minor.free_symbols
R=matrix({r:1,s:0,t:0,w:-1});bad=[(0,0,0),(0,2,2),(0,2,3),(0,3,3)];rows=[2*len(words)+index[v] for v in [(0,0,0,2),(0,2,2,2),(0,2,2,3),(0,2,3,3)]];cols=[E.index(v) for v in bad]
assert S.expand(R.extract(rows,cols).det())==16
assert R.extract(rows,[i for i in range(10) if i not in cols])==S.zeros(4,6)
out={'status':'PASS','scope':'all F in GL2, commuting U, u acts F, v acts inverse F, vu=-detF*uv+detF*h2(U)','universal_PBW_overlaps':overlaps,'F_identity':{'normal_kernel':['x*(uv-h/2)','y*(uv-h/2)'],'complement_minor':str(minor)},'F_reflection':{'four_forbidden_columns':['x3','xu2','xuv','xv2'],'minor':16,'remaining_candidates':'all divisible by negative F-eigenline y'},'F_noninvolution':'normal cubic=f3+Luv; F(L)=detF*L and (1+Sym3F)f3=-detF*L*F(h); quotient by L makes F identity, so f3 divisible by L. L=0 gives a binary cubic, also reducible.','conclusion':'all H3 cuts in this entire matrix/curvature family occur at F=-I and are exactly the recognized curved Clifford cuts','not_claimed':['all rank4 graphs','necessary envelope coverage','intrinsic relative descent']}
Path(__file__).with_name('cubic_order2_22_clifford_matrix_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS universal GL2 PBW; identity normal kernel minor',minor,'; reflection forbidden minor16')
