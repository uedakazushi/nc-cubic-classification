#!/usr/bin/env python3
"""Exact universal anti-diagonal involution normal-cubic exclusion."""
import itertools,json
from pathlib import Path
import sympy as S
from functools import lru_cache
from sympy.polys.matrices import DomainMatrix
A,C,D=S.symbols('A C D');K=S.QQ.frac_field(A,C,D);aa,cc,dd=K.gens;one=K.one
rules={(1,0):{(0,1):-one},
(2,0):{(0,2):-one/2,(1,2):one/2,(0,3):-one/2,(1,3):-one/2,(0,1):aa/2},
(3,0):{(0,2):-one/2,(1,2):-one/2,(0,3):-one/2,(1,3):one/2,(0,1):-aa/2},
(2,1):{(0,2):one/2,(1,2):one/2,(0,3):-one/2,(1,3):one/2,(0,1):aa/2},
(3,1):{(0,2):-one/2,(1,2):one/2,(0,3):one/2,(1,3):one/2,(0,1):-aa/2},
(3,2):{(2,3):-one,(0,0):-cc/2,(1,1):-dd/2}}
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
assert unit_rank(rows,20)==20
top_data=json.loads(Path(__file__).with_name('cubic_order2_antidiagonal_top_certificate.json').read_text());w={}
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

condition=S.Matrix([[1,0,0,1,0,0],[0,0,1,0,0,1],[0,1,0,0,-1,0]])
inner=S.Matrix([[1,0],[1,-1],[0,-1],[-1,0],[1,-1],[0,1]])
residual=S.Matrix([0,1,0,0,1,0])
assert condition.rank()==3 and inner.rank()==2
assert condition*inner==S.zeros(3,2) and condition*residual==S.zeros(3,1)
assert inner.row_join(residual).rank()==3
# Residual derivation delta(x)=delta(y)=A*x*y has delta²=0 and anti-commutes with nu.
def deriv(word):
 out={}
 for pos in range(len(word)):
  term=tuple(1-i for i in word[:pos])+(0,1)+word[pos+1:]
  for ww,c in nf(term).items():out[ww]=out.get(ww,K.zero)+aa*c
 return {ww:c for ww,c in out.items() if c}
assert not deriv((0,1))
for i in [0,1]:
 out={}
 for ww,c in nf((1,0)).items():out[ww]=out.get(ww,K.zero)+aa*c
 for ww,c in deriv((1-i,)).items():out[ww]=out.get(ww,K.zero)+c
 assert not any(out.values())
summary={'normalizing_chart':'xy=-yx; px=-xp; py=yp; vx=yv+dx; vy=xv+dy; v²-p²=ell*v+P',
 'skew_derivations':'Modulo inner, delta(x)=delta(y)=A*x*y; delta²=0 and delta*nu+nu*delta=0',
 'canonical_family':'vx=yv+A*xy; vy=xv+A*xy; v²-p²=C*x²+D*y²',
 'top_terms':74,'universal_top_ranks':flatten_ranks,
 'normality_unit_rank':20,'W1':'zero for every A,C,D',
 'result':'Entire anti-diagonal involution normalizing chart excluded after removing inner derivations and the forced-zero outer linear term.',
 'scope':'No general degenerate cross-projection or non-diagonal common-plane matrix coverage asserted.'}
path=Path(__file__).with_name('cubic_order2_antidiagonal_chart_certificate.json')
if path.exists():assert json.loads(path.read_text())==summary
else:path.write_text(json.dumps(summary,indent=2)+'\n')
print('PASS anti-diagonal derivation class, polynomial top ranks, universal normality rank20: W1 zero')
