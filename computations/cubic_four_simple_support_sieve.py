"""Exact all-support necessary sieve using forced normal generators and hdet.
Compatible support masks are necessary pieces, never existence assertions.
"""
import itertools,json,functools,collections,sympy as s
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from cubic_four_simple_finite_model import prune
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_four_simple_finite_atlas_certificate.json').read_text());assert D['status']=='PASS' and len(D['final_necessary_atlas'])==39
certs={tuple(r['spectrum']):r for r in D['all115_orbit_checks']}
@functools.lru_cache(None)
def leftkern(A):
 dm=DomainMatrix.from_Matrix(s.Matrix(A)).convert_to(s.ZZ).to_dense();DD,U,V=smith_normal_decomp(dm);assert U.matmul(dm).matmul(V)==DD and abs(U.det())==1 and abs(V.det())==1
 rank=sum(bool(DD[i,i].element) for i in range(min(DD.shape)));return tuple(tuple(map(int,r)) for r in U.to_list()[rank:])
def maxmatch(edges):
 match={}
 def visit(r,seen):
  for c in edges.get(r,[]):
   if c in seen:continue
   seen.add(c)
   if c not in match or visit(match[c],seen):match[c]=r;return True
  return False
 return sum(visit(r,set()) for r in edges)
def factor(vs,skew,I,support,a,N):
 for i in range(4):
  if all(v[i] for v in vs) and all(i==j or tuple(sorted((i,j))) in skew for v in vs for j,c in enumerate(v) if c):return True
 for S in itertools.combinations(range(4),2):
  if all(all(v[j]==0 for j in range(4) if j not in S) for v in vs):
   if any(I[w] and support[w] and all(i in S and j in S for i,j in support[w]) for w in range(N)):return True
 for z,u,v in itertools.permutations(range(4),3):
  va=tuple(2*(j==u)+(j==z) for j in range(4));vb=tuple((j==v)+2*(j==z) for j in range(4));w=(a[v]+a[z])%N
  if all(x in [va,vb] for x in vs) and tuple(sorted((u,z))) in skew and support[w]<={(v,z),(z,v),(u,u)} and I[w]==1:return True
 return False
def replay():
 out=[]
 for row in D['final_necessary_atlas']:
  N=row['N'];a=row['exponents'];rec=certs[(N,*a)];basis,active0,_,status=prune(N,a);assert status=='survives' and active0==set(rec['active_orbits']);qcounts=sorted({tuple(next(iter(basis[j])).count(k) for k in range(4)) for j in active0});vc=rec['cubic_exponents'];good=[];stats=collections.Counter();witness=[]
  for I in row['relation_characters']:
   patterns=[]
   for sm in range(1,1<<len(qcounts)):
    S=[qcounts[j] for j in range(len(qcounts)) if sm>>j&1]
    if S==[(1,1,1,1)] or not all(any(w[i] for w in S) for i in range(4)):continue
    act={j for j in active0 if tuple(next(iter(basis[j])).count(k) for k in range(4)) in S and all(I[(a[w[0]]+a[w[1]])%N] for w in basis[j])}
    while True:
     kill=set()
     for col in range(16):
      es={4*w[0]+w[1]:j for j in act for w in basis[j] if 4*w[2]+w[3]==col}
      if len(es)==1:kill.update(es.values())
     if not kill:break
     act-=kill
    if {tuple(next(iter(basis[j])).count(k) for k in range(4)) for j in act}!=set(S):continue
    support={w:set() for w in range(N)};edges={w:{} for w in range(N)}
    for j in act:
     for w in basis[j]:
      weight=(a[w[0]]+a[w[1]])%N;support[weight].add(w[:2]);edges[weight].setdefault(4*w[0]+w[1],set()).add(4*w[2]+w[3])
    if any(I[w]>maxmatch(edges[w]) for w in range(N)):continue
    skew={tuple(sorted((i,j))) for i in range(4) for j in range(i+1,4) if support[(a[i]+a[j])%N]=={(i,j),(j,i)} and I[(a[i]+a[j])%N]==1}
    if len(skew)==6:continue
    normal=[i for i in range(4) if all(i==j or tuple(sorted((i,j))) in skew for j in range(4))];ee=sorted({e for e in skew if any(z in e for z in normal)})
    for tm in range(1,1<<len(vc)):
     T=[tuple(vc[j]) for j in range(len(vc)) if tm>>j&1]
     if factor(T,skew,I,support,a,N):stats['factor']+=1;continue
     if normal:
      A=[];b=[]
      for z in normal:
       for v in S+T:
        A.append(tuple(v[e[1]] if z==e[0] else -v[e[0]] if z==e[1] else 0 for e in ee));b.append(a[z])
      bad=next((v for v in leftkern(tuple(A)) if sum(x*y for x,y in zip(v,b))%N),None)
      if bad is not None:
       assert all(sum(bad[j]*A[j][k] for j in range(len(A)))==0 for k in range(len(ee)))
       stats['normalizer']+=1;witness.append({'relation_character_index':row['relation_characters'].index(I),'S':S,'T':T,'normal':normal,'edges':ee,'integer_left_relation':bad,'rhs_modN':sum(x*y for x,y in zip(bad,b))%N});continue
     patterns.append({'relation_character':I,'top_support':S,'cubic_support':T,'normal_generators':normal})
   good+=patterns
  patterns=[[row['relation_characters'].index(g['relation_character']),sum(1<<qcounts.index(tuple(w)) for w in g['top_support']),sum(1<<vc.index(list(v)) for v in g['cubic_support']),sum(1<<z for z in g['normal_generators'])] for g in good]
  out.append({'N':N,'exponents':a,'label_count':row['Galois_label_orbit_size'],'quartic_count_types':qcounts,'cubic_count_types':vc,'relation_characters':row['relation_characters'],'compatible_support_masks':patterns,'stats':dict(stats),'normalizer_witnesses':witness})
 return out
