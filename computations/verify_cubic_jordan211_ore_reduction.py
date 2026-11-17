#!/usr/bin/env python3
"""Original32 tops for Jordan(2,1,1), with exact universal Ore-block data.
Domain contraction-rank, AS3 descent and derived vertex exclusion are ordinary
proofs in the accompanying paper, not numerical consequences of this checker.
"""
from pathlib import Path
import itertools,json,math,sympy as s
from cubic_diagonal_top import top_basis
ROOT=Path(__file__).resolve().parent
W=list(itertools.product(range(4),repeat=4));ix={w:i for i,w in enumerate(W)};cb=top_basis(s.QQ,[s.QQ.one]*4);C=s.zeros(256,66);DC=s.zeros(256,66)
for j,b in enumerate(cb):
 for word,c in b.items():
  C[ix[word],j]=c
  for pos,l in enumerate(word):
   if l==1:DC[ix[word[:pos]+(0,)+word[pos+1:]],j]+=c
KK=s.Matrix.hstack(*DC.nullspace());B=C*KK;assert B.cols==32;rows=B.T.rref()[1];B=B*B.extract(rows,range(32)).inv();a=s.symbols('a0:32');v=B*s.Matrix(a);H=s.Matrix(16,16,lambda i,j:v[ix[divmod(i,4)+divmod(j,4)]])
assert [(i,H[i,5]) for i in range(16) if H[i,5]]==[(0,a[3])]
v=v.subs(a[3],0);H=H.subs(a[3],0);assert all(not c or W[j].count(1)<=1 for j,c in enumerate(v))
U=[0,2,3];ur=[4*i+j for i in U for j in U];mixed=[4*i+j for i,j in itertools.product(range(4),repeat=2) if (i==1)+(j==1)==1];assert len(mixed)==6
assert H.extract(mixed,mixed)==s.zeros(6) and H[:,5]==s.zeros(16,1) and H==H.T
f={word:v[ix[(1,)+word]] for word in itertools.product(U,repeat=3)}
M=H.extract(ur,mixed);left=s.Matrix([[f[k,i,j] for k in U] for i,j in itertools.product(U,repeat=2)]);right=s.Matrix([[f[i,j,k] for k in U] for i,j in itertools.product(U,repeat=2)])
for j,pair in enumerate(mixed):
 i,k=divmod(pair,4)
 assert M[:,j]==(left[:,U.index(k)] if i==1 else -right[:,U.index(i)])
# All weight1 coordinates occur in f; vanishing f means no z occurs in the top.
active=sorted(set().union(*(c.free_symbols for c in f.values())),key=str);expected=[a[j] for j in [0,4,5,6,9,12,13,14,15,18]];assert set(active)==set(expected)
# Exact free-word differentiation at every z degree needed for a cubic.
def derive(poly):
 out={}
 for word,c in poly.items():
  for pos,l in enumerate(word):
   if l==1:
    t=word[:pos]+(0,)+word[pos+1:];out[t]=out.get(t,0)+c
 return {w:c for w,c in out.items() if c}
for d in range(1,4):
 p={(1,)*d:1}
 for k in range(d):p=derive(p)
 assert p=={(0,)*d:math.factorial(d)}
t=s.Symbol('t');assert s.cancel((1-t**3)/(1-t)**3-(1+t+t*t)/(1-t)**2)==0
assert s.cancel((1-t)**3/(1-t**3)-(1-t)**2/(1+t+t*t))==0
out={'status':'PASS','scope':'all unipotent Jordan(2,1,1) original top blocks and universal Ore-reduction data; full domain and homological proof is in paper','coordinate_words':[''.join(map(str,W[j])) for j in rows],'all32_basis':[{''.join(map(str,W[j])):str(c) for j,c in enumerate(B.col(k)) if c} for k in range(32)],'forbidden_square_coefficient':'a3, source col11 pure x0^2','base_generators':U,'Ore_generator':1,'highest_weight1_cubic':{''.join(map(str,w)):str(c) for w,c in f.items() if c},'mixed_block':str(M),'ordinary_proof_dependencies':['nonzero cubic with combined first/last contractions rank<=2 has decomposable contraction','rankH6 gives mixed rank<=3, domain gives>=3','N maps a one-sided mixed relation to a nonzero decomposable quadratic, so both projections invertible','N^d forces independence of all Ore powers and fixed cubic belongs to base','Koszul top gives exactly one base cubic syzygy, then all AS3 base and Ore descent','general derivation-Ore vertex lemma gives infinite selfExt after a cubic base cut'],'not_claimed':['all CY classification','remaining Jordan(2,2) classified','ordinary proofs mechanically formalized','novelty confirmed']}
(ROOT/'cubic_jordan211_ore_reduction_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS all32 top directions, pure-square exclusion, full Ore block/contraction identities')
