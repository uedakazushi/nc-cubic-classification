#!/usr/bin/env python3
"""All-parameter positive-three minus-one-plane coverage and normalizer-zero witnesses."""
import itertools,json,sympy as S
from pathlib import Path
base=S.QQ.algebraic_field(S.I);K=base.frac_field('g','A');g,A=K.gens;I=K.from_sympy(S.I);one=K.one

def unit(c):return bool(c) and all(not any(m) for m in c.numer) and all(not any(m) for m in c.denom)
def echelon(rows,n):
 rows=[{j:c for j,c in row.items() if c} for row in rows];ps=[];cols=set(range(n))
 while 1:
  hit=next(((i,j,c) for i,row in enumerate(rows) for j,c in row.items() if j in cols and unit(c)),None)
  if hit is None:break
  i,j,c=hit;p={k:v/c for k,v in rows.pop(i).items()};ps.append((j,p));cols.remove(j)
  for rr in rows:
   co=rr.get(j,K.zero)
   if not co:continue
   for k,v in p.items():
    cc=rr.get(k,K.zero)-co*v
    if cc:rr[k]=cc
    else:rr.pop(k,None)
 return ps,cols,rows

def quotient(n,axis,B,positive=False):
 nvar=3 if positive else 4
 words=list(itertools.product(range(nvar),repeat=n));ix={w:i for i,w in enumerate(words)};h=one if axis else g-one
 cross={(2,0):one,(0,2):-one} if axis else {(2,0):one,(2,1):one,(0,2):-one,(1,2):-one}
 rel=[{(0,1):one,(1,0):one},{(3,0):one,(0,3):-I},{(3,1):one,(1,3):I},cross,
      {(2,2):one,(0,0):-g,(1,1):-h},
      {(3,3):one,(0,1):-A,(1,2):-K(B),(2,1):K(B)}]
 if positive:rel=[rel[i] for i in [0,3,4]]
 rows=[]
 for rr in rel:
  for pos in range(n-1):
   for rest in itertools.product(range(nvar),repeat=n-2):rows.append({ix[rest[:pos]+w+rest[pos:]]:c for w,c in rr.items() if c})
 ps,free,remaining=echelon(rows,len(words))
 assert not any(remaining)
 free=sorted(free);proj={j:{i:one} for i,j in enumerate(free)}
 for j,row in reversed(ps):
  out={}
  for k,c in row.items():
   if k==j:continue
   for i,v in proj[k].items():out[i]=out.get(i,K.zero)-c*v
  proj[j]={i:c for i,c in out.items() if c}
 return words,ix,free,proj
records=[]
for axis in [False,True]:
 for B in [0,1]:
  w3,i3,f3,p3=quotient(3,axis,B)
  if not B:
   assert len(f3)==21;records.append({'axis':axis,'commutator_coefficient':0,'degree3_dimension':21});continue
  assert len(f3)==20
  w4,i4,f4,p4=quotient(4,axis,B);assert len(f4)==35
  rows={}
  for j,k in enumerate(f3):
   for gg,mu in enumerate([1,1,1,-1]):
    for ww,cc in [(w3[k]+(gg,),one),((gg,)+w3[k],-K(mu))]:
     for i,c in p4[i4[ww]].items():
      row=rows.setdefault((gg,i),{});row[j]=row.get(j,K.zero)+cc*c
  ps,free,remaining=echelon(list(rows.values()),20)
  records.append({'axis':axis,'commutator_coefficient':1,'degree3_dimension':20,'degree4_dimension':35,'normalizer_constant_pivot_rank':len(ps)})
  assert len(ps)==20 and not free and not any(remaining)

positive_checks=[]
for axis in [False,True]:
 w2,i2,f2,p2=quotient(2,axis,1,True)
 w3,i3,f3,p3=quotient(3,axis,1,True)
 assert len(f2)==6 and len(f3)==10
 # A nondegenerate cubic top for the positive subalgebra; it has reflection
 # Nakayama fixing W and negating v. Its existence proves Frobenius of
 # F=E/(zstar), whose Hilbert values were established universally.
 if axis:
  top={(2,2,0):one,(2,0,2):-one,(0,2,2):one,(0,0,0):-g,
       (0,1,1):-one,(1,0,1):-one,(1,1,0):-one}
 else:
  alpha=one/4;beta=g-one/2
  abstract={(1,1,1):alpha,(0,0,1):-alpha,(0,1,0):-alpha,(1,0,0):-alpha,
            (0,0,0):-beta,(2,2,0):one,(2,0,2):-one,(0,2,2):one}
  change={0:{0:one,1:one},1:{0:one,1:-one},2:{2:one}}
  top={}
  for word,cc in abstract.items():
   for terms in itertools.product(*(list(change[j].items()) for j in word)):
    ww=tuple(i for i,c in terms);co=cc
    for i,c in terms:co*=c
    top[ww]=top.get(ww,K.zero)+co
  top={w:c for w,c in top.items() if c}
 for pos in [0,1]:
  reduced={}
  for word,cc in top.items():
   for i,c in p2[i2[word[pos:pos+2]]].items():
    key=(word[:pos],i,word[pos+2:]);reduced[key]=reduced.get(key,K.zero)+cc*c
  assert not any(reduced.values())
 left={};right={}
 for word,cc in top.items():
  left.setdefault(word[0],{})[3*word[1]+word[2]]=cc
  right.setdefault(3*word[0]+word[1],{})[word[2]]=cc
  assert cc==[1,1,-1][word[0]]*top.get(word[1:]+word[:1],K.zero)
 assert len(echelon(list(left.values()),9)[0])==3
 assert len(echelon(list(right.values()),3)[0])==3
 # All positive quadrics anticommuting with x and y form exactly
 # span(xy,[y,v]), in both charts and all normalized parameters.
 rows={}
 for j,k in enumerate(f2):
  for gg in [0,1]:
   for word in [w2[k]+(gg,),(gg,)+w2[k]]:
    for i,c in p3[i3[word]].items():
     row=rows.setdefault((gg,i),{});row[j]=row.get(j,K.zero)+c
 ps,free,remaining=echelon(list(rows.values()),6)
 assert len(ps)==4 and len(free)==2 and not any(remaining)
 candidates=[{(0,1):one},{(1,2):one,(2,1):-one}]
 vectors=[]
 for candidate in candidates:
  vec={}
  for w,cc in candidate.items():
   for i,c in p2[i2[w]].items():vec[i]=vec.get(i,K.zero)+cc*c
  vectors.append(vec)
  for gg in [0,1]:
   out={}
   for w,cc in candidate.items():
    for word in [w+(gg,),(gg,)+w]:
     for i,c in p3[i3[word]].items():out[i]=out.get(i,K.zero)+cc*c
   assert not any(out.values())
 assert len(echelon(vectors,6)[0])==2
 positive_checks.append({'axis':axis,'positive_top_flatten_ranks':[3,3],
                         'anti_common_plane_quadrics_dimension':2})

data={
 'normalized_presentations':{
  'common_relations':['xy=-yx','zx=i*xz','zy=-i*yz','z²=A*xy+B*[y,v]'],
  'axis':['vx=xv','v²=g*x²+y²'],
  'nonaxis':['[v,x+y]=0','v²=g*x²+(g-1)*y²']},
 'positive_AS3_embedding_test':positive_checks,
 'cases':records,
 'normalization':'B=0 has degree3 dimension21, so cannot be14641; B!=0 scales to1 over algebraically closed k',
 'conclusion':'All H3 candidates with Nakayama multiplicities(3,1), semisimple mu, and gamma=0 are excluded.',
 'scope':'Universal constant Gaussian-rational pivots; no sampling or parameter division. Geometric chart normalization, the Frobenius-open AS3 embedding and coverage use manuscript proofs. Positive-W Jordan and gamma!=0 are not excluded.'}
path=Path(__file__).with_name('cubic_positive3_quantum_plane_certificate.json')
if path.exists():assert json.loads(path.read_text())==data
else:path.write_text(json.dumps(data,indent=2)+'\n')
print('PASS all positive-three semisimple gamma-zero charts: positive AS3 embedding, full coverage and rank20')
