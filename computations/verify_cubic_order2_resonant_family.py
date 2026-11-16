#!/usr/bin/env python3
"""Universal exact identities for a resonant involution normal-cubic candidate family."""
import itertools,json
from pathlib import Path
import sympy as S
from functools import lru_cache
from sympy.polys.matrices import DomainMatrix
A,B,C,D=S.symbols('A B C D');K=S.QQ.frac_field(A,B,C,D);aa,bb,cc,dd=K.gens;one=K.one
rules={(1,0):{(0,1):-one},(2,0):{(0,2):-one,(1,1):aa/2},(3,0):{(0,3):-one,(1,1):-aa/2},(2,1):{(1,3):one,(0,0):bb/2},(3,1):{(1,2):one,(0,0):-bb/2},(3,2):{(2,3):-one,(0,0):-cc/2,(1,1):-dd/2}}
@lru_cache(None)
def nf(word):
 for pos in range(len(word)-1):
  if word[pos:pos+2] in rules:
   out={}
   for pair,c in rules[word[pos:pos+2]].items():
    for ww,d in nf(word[:pos]+pair+word[pos+2:]).items():out[ww]=out.get(ww,K.zero)+c*d
   return {w:c for w,c in out.items() if c}
 return {word:one}
def reduce_at(word,pos):
 out={}
 for pair,c in rules[word[pos:pos+2]].items():
  for ww,d in nf(word[:pos]+pair+word[pos+2:]).items():out[ww]=out.get(ww,K.zero)+c*d
 return {w:c for w,c in out.items() if c}
for word in itertools.product(range(4),repeat=3):
 if word[:2] in rules and word[1:] in rules:assert reduce_at(word,0)==reduce_at(word,1)

b3=[w for w in itertools.combinations_with_replacement(range(4),3)];b4=[w for w in itertools.combinations_with_replacement(range(4),4)];ix={w:i for i,w in enumerate(b4)};mu=[(0,-1),(1,-1),(3,1),(2,1)];rows={}
for j,w in enumerate(b3):
 for g in range(4):
  h,sign=mu[g]
  for word,scale in [(w+(g,),one),((h,)+w,-K(sign))]:
   for ww,c in nf(word).items():
    r=35*g+ix[ww];rows.setdefault(r,{})[j]=rows.get(r,{}).get(j,K.zero)+scale*c
rows={r:{j:c for j,c in rr.items() if c} for r,rr in rows.items()};rows={r:rr for r,rr in rows.items() if rr}

def unit_rank(data,ncols):
 remaining=[dict(row) for row in data.values()];columns=set(range(ncols));count=0
 def unit(c):return bool(c) and all(not any(m) for m in c.numer) and all(not any(m) for m in c.denom)
 while True:
  hit=next(((i,j,c) for i,row in enumerate(remaining) for j,c in row.items() if j in columns and unit(c)),None)
  if hit is None:break
  i,j,c=hit;pivot=remaining.pop(i);pivot={k:d/c for k,d in pivot.items()};columns.remove(j);count+=1
  for ii,row in enumerate(remaining):
   if row.get(j,K.zero):
    co=row[j];out=dict(row)
    for k,d in pivot.items():out[k]=out.get(k,K.zero)-co*d
    remaining[ii]={k:d for k,d in out.items() if d}
 assert not any(remaining)
 return count
assert unit_rank(rows,20)==19
G={(0,0,2):bb,(0,0,3):bb,(1,2,2):-K(2),(1,3,3):K(2)}
vector=[G.get(w,K.zero) for w in b3]
assert all(not sum((c*vector[j] for j,c in rr.items()),K.zero) for rr in rows.values())
top_data=json.loads(Path(__file__).with_name('cubic_order2_resonant_top_certificate.json').read_text());w={}
for record in top_data:
 co=K.zero
 for term in record['terms']:
  c=K.convert(S.QQ(term['coefficient']),S.QQ)
  for parameter,power in zip(K.gens,term['powers']):c*=parameter**power
  co+=c
 w[tuple(record['word'])]=co
assert not(w[(1,0,3,2)]-K.one)
for pos in range(3):
 out={}
 for word,c in w.items():
  for pair,d in nf(word[pos:pos+2]).items():
   ww=word[:pos]+pair+word[pos+2:];out[ww]=out.get(ww,K.zero)+c*d
 assert not any(out.values())
left={word[1:]+word[:1]:c for word,c in w.items()};right={}
for word,c in w.items():
 h,sgn=mu[word[-1]];ww=word[:-1]+(h,);right[ww]=right.get(ww,K.zero)-sgn*c
assert all(not(left.get(ww,K.zero)-right.get(ww,K.zero)) for ww in set(left)|set(right))
flatten_ranks=[]
for pos in [1,2,3]:
 lr=list(itertools.product(range(4),repeat=pos));rr=list(itertools.product(range(4),repeat=4-pos));li={w:i for i,w in enumerate(lr)};ri={w:i for i,w in enumerate(rr)};data={}
 for word,c in w.items():data.setdefault(li[word[:pos]],{})[ri[word[pos:]]]=c
 rank=unit_rank(data,len(rr));flatten_ranks.append(rank)
assert flatten_ranks==[4,6,4]
# Skew derivations of the quantum plane xy=-a²yx, nu=(a,a^-1).
a=S.Symbol('a');q=-a*a
inner=S.Matrix([[1-a,0],[0,q**-1-a],[0,0],[0,0],[1-a**-1*q**-1,0],[0,1-a**-1]])
cond=S.Matrix([[0,0,0,a-q,0,0],[0,0,1-q*a**-1,0,0,0],[1-a**-1*q**-1,0,0,0,a-1,0],[0,1-a**-1,0,0,0,a-q**-1]])
assert (cond*inner).applyfunc(S.cancel)==S.zeros(4,2)
for pair in [(1-a,1+a**-3),(-a**-2-a,1-a**-1)]:
 nums=[S.fraction(S.cancel(f))[0] for f in pair];assert S.Poly(S.gcd(*nums),a).degree()==0
assert cond.subs(a,-1).rank()==2 and inner.subs(a,-1).rank()==2
summary={'family':'xy=-yx; px=-xp; py=yp; vx+xv=A*y²; vy+yv=B*x²; v²-p²=C*x²+D*y²',
 'PBW_variables':'x,y,u,w with p=u+w, v=u-w',
 'top_terms':54,'universal_flattening_ranks':flatten_ranks,
 'normality_unit_rank':19,'W1':'span(B*x²*p-y*(p*v+v*p)) at every parameter value',
 'necessary_H3':'B!=0; B=0 gives a factor by y',
 'skew_derivations':'Degree-one nu-skew derivations are all inner except a=-1; at a=-1 residual basis delta(x)=y² and delta(y)=x².',
 'scope':'AS4 envelopes and a normal cubic line constructed. All cuts are separately excluded by the fixed local obstruction; this construction validator alone does not establish H3.'}
path=Path(__file__).with_name('cubic_order2_resonant_family_certificate.json')
if path.exists():assert json.loads(path.read_text())==summary
else:path.write_text(json.dumps(summary,indent=2)+'\n')
print('PASS resonant PBW, polynomial top/Frobenius ranks4-6-4, universal W1 rank19, skew derivation resonance')
