#!/usr/bin/env python3
"""Alluv normal cubic, central cubic/ninth and Artinian81 at w0 resonance.
Division only by parameter constants; source relations checked both sides.
"""
#!/usr/bin/env python3
"""All-u,v normal cubic kernels at the six exceptional axis parameters.
The normalizer is delta=(1,1,omega^2,omega) in the CY untwist C.
This does not decide domain/finite global dimension of the resulting cuts.
"""
from pathlib import Path
import json,sympy as s
import sys
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z**6-z**3+1,z));tt=F.unit;out={'status':'PASS','field':'t^6-t^3+1','axes':{}}
K=F.poly_ring('u','v');u,v=K.gens;one,zero=K.one,K.zero;t=K.convert(tt,F)
o=K.convert(tt**3-F.one,F);d,e=one,t
R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
{(1,2):d,(2,1):e,(3,3):one},{(1,3):e,(3,1):d,(2,2):one},
{(2,3):d,(3,2):e,(0,0):u,(0,1):v}]
weights=[0,0,1,2];RC=[{w:c/o**weights[w[1]] for w,c in rr.items() if c} for rr in R]
class PolyAlgebra(GradedAlgebra):
 def echelon(self,rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j];assert co.is_ground
     piv[j]={k:K.exquo(c,co) for k,c in row.items()};break
    self.addto(row,piv[j],-row[j])
  return piv
A=PolyAlgebra(K,4,RC,weights);M,ids=A.normal_matrix(3,[one,one,o**2,o],fixed=True)
rows=list(M.to_dod().values());piv={}
while rows:
 chosen=next(((i,j) for i,row in enumerate(rows) for j,c in row.items() if c and c.is_ground),None)
 if chosen is None:break
 i,j=chosen;row=rows.pop(i);co=row[j];row={k:K.exquo(c,co) for k,c in row.items()};piv[j]=row
 for jj,old in piv.items():
  if jj!=j and j in old:A.addto(old,row,-old[j])
 for old in rows:
  if j in old:A.addto(old,row,-old[j])
 rows=[r for r in rows if r]

assert not rows and len(piv)==7
free=next(i for i in range(len(ids)) if i not in piv)
G={A.basis[3][ids[free]]:one}
for j,row in piv.items():
 if free in row:G[A.basis[3][ids[j]]]=-row[free]

for letter,phase in enumerate([one,one,o**2,o]):
 total={}
 for w,c in G.items():A.addto(total,A.word(w+(letter,)),c);A.addto(total,A.word((letter,)+w),-phase*c)
 assert not total


def central_kernels(alg,n):
 alg.build(n+1);ids=[i for i,w in enumerate(alg.basis[n]) if sum(weights[j] for j in w)%3==0];rows=[]
 for letter in range(4):
  rr={}
  for ii,i in enumerate(ids):
   col=dict(alg.right[n+1][i,letter]);alg.addto(col,alg.left[n+1][letter,i],-one)
   for j,c in col.items():rr.setdefault(j,{})[ii]=c
  rows+=list(rr.values())
 piv={}
 while rows:
  chosen=next(((i,j) for i,row in enumerate(rows) for j,c in row.items() if c and c.is_ground),None)
  if chosen is None:break
  i,j=chosen;row=rows.pop(i);co=row[j];row={k:K.exquo(c,co) for k,c in row.items()};piv[j]=row
  for jj,old in piv.items():
   if jj!=j and j in old:alg.addto(old,row,-old[j])
  for old in rows:
   if j in old:alg.addto(old,row,-old[j])
  rows=[r for r in rows if r]
 print('CENTER',n,'cols',len(ids),'pivots',len(piv),'residual',len(rows),flush=True);assert not rows
 free=[i for i in range(len(ids)) if i not in piv]
 kernels=[{**{ids[i]:-row[f] for i,row in piv.items() if f in row},ids[f]:one} for f in free]
 for ker in kernels:
  for letter in range(4):
   total={}
   for i,c in ker.items():alg.addto(total,alg.right[n+1][i,letter],c);alg.addto(total,alg.left[n+1][letter,i],-c)
   assert not total
 return kernels
C=PolyAlgebra(K,4,RC,weights);psk=central_kernels(C,3)
Psi=next({C.basis[3][i]:c for i,c in ker.items()} for ker in psk if any(0 not in C.basis[3][i] for i in ker))
assert len(psk)==2
A=PolyAlgebra(K,4,RC+[G],weights);kernels=central_kernels(A,9);assert len(kernels)==5
from sympy.polys.matrices import DomainMatrix
def ev00(co):return co.get((0,0),F.zero)
def boundary(poly):
 assert all(c.is_ground for w,c in poly.items() if 0 not in w)
 return {tuple(j-1 for j in w):ev00(c) for w,c in poly.items() if 0 not in w and ev00(c)}
def bvec(poly):
 ans={}
 for w,c in boundary(poly).items():S.addto(ans,S.word(w),c)
 return ans
def mul(a,b):
 out={}
 for w,c in a.items():
  for ww,dd in b.items():out[w+ww]=out.get(w+ww,zero)+c*dd
 return {w:c for w,c in out.items() if c}
S=GradedAlgebra(F,3,[boundary(r) for r in RC if any(0 not in w for w in r)]+[boundary(G)],[0,1,2]);S.build(9)
known=bvec(mul(mul(Psi,Psi),Psi))
def rank(rows):return DomainMatrix.from_dod(dict(enumerate(rows)),(len(rows),len(S.basis[9])),F).rank()
for ker in kernels:
 poly={A.basis[9][i]:c for i,c in ker.items()}
 if rank([known,bvec(poly)])==2:break
assert rank([known,bvec(poly)])==2
rels=[boundary(r) for r in RC+[G,Psi,poly] if any(0 not in w for w in r)]
T=GradedAlgebra(F,3,rels,[0,1,2]);T.build(13);dims=[len(T.basis[j]) for j in range(14)]
assert dims==[1,3,6,8,9,9,9,9,9,8,6,3,1,0]
def encode(poly):return {''.join('xybc'[j] for j in w):{str(mon):list(map(str,c.to_list())) for mon,c in co.items()} for w,co in poly.items()}
out={'status':'PASS','G':encode(G),'Psi':encode(Psi),'chosen_center':encode(poly),'dimensions':dims}
Path(__file__).with_name('cubic_third_root_unit_boundary_w0_center_certificate.json').write_text(json.dumps(out,indent=2))

# Check both action conventions against all original relation insertions.
for alg,top in [(A,10),(T,13)]:
 for rel in alg.relations:
  rlen=len(next(iter(rel)))
  for n in range(rlen,top+1):
   for i in range(len(alg.basis[n-rlen])):
    for side in [0,1]:
     total={}
     for w,c in rel.items():
      state={i:c};degree=n-rlen
      for letter in (w if side==0 else tuple(reversed(w))):
       nxt={}
       for j,co in state.items():alg.addto(nxt,alg.right[degree+1][j,letter] if side==0 else alg.left[degree+1][letter,j],co)
       state=nxt;degree+=1
      alg.addto(total,state,alg.K.one)
     assert not total
out['left_right_original_relation_actions']='PASS through degrees10/13'
Path(__file__).with_name('cubic_third_root_unit_boundary_w0_center_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS alluv w0 normal cubic and central free81 data')
