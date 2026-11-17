#!/usr/bin/env python3
"""All-u,v exact central degree9 and Artinian rank81 data at E=0,D^3=-omega^2.
Only parameter-constant pivots are used; ordinary finite-free proof is in TeX.
"""
import sys,json,sympy as s
from pathlib import Path
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z**6-z**3+1,z));K=F.poly_ring('u','v');u,v=K.gens;d=K.convert(F.unit,F);o=d**3-K.one;one,zero=K.one,K.zero
class PolyAlgebra(GradedAlgebra):
 def echelon(self,rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j];assert co.is_ground,('nonconstant relation pivot',j,str(co));piv[j]={k:K.exquo(c,co) for k,c in row.items()};break
    self.addto(row,piv[j],-row[j])
  return piv
R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o}, {(1,2):d,(3,3):one},{(2,2):one,(3,1):d},{(2,3):d,(0,0):u,(0,1):v,(1,1):one}]
weights=[0,0,1,2];RC=[{w:c/o**weights[w[1]] for w,c in r.items()} for r in R]
G={(1,3,2):one,(2,1,3):o**2,(3,2,1):one,(2,3,0):v*o**2,(3,2,0):v,(1,0,0):-u*d*d}
A=PolyAlgebra(K,4,RC+[G],weights);A.build(10)
ids=[i for i,w in enumerate(A.basis[9]) if sum(weights[j] for j in w)%3==0]
rows=[]
for letter in range(4):
 rr={}
 for ii,i in enumerate(ids):
  col=dict(A.right[10][i,letter]);A.addto(col,A.left[10][letter,i],-one)
  for j,c in col.items():rr.setdefault(j,{})[ii]=c
 rows+=list(rr.values())
piv={};waiting=rows
while waiting:
 chosen=next(((index,j) for index,row in enumerate(waiting) for j,c in row.items() if c and c.is_ground),None)
 if chosen is None:break
 index,j=chosen;row=waiting.pop(index);co=row[j];row={k:K.exquo(c,co) for k,c in row.items()};piv[j]=row
 for jj,old in piv.items():
  if jj!=j and j in old:A.addto(old,row,-old[j])
 for other in waiting:
  if j in other:A.addto(other,row,-other[j])
 waiting=[r for r in waiting if r]
 if len(piv)%10==0:print('pivots',len(piv),'waiting',len(waiting),flush=True)
free=[i for i in range(len(ids)) if i not in piv];print('FINAL',len(ids),len(piv),len(waiting),len(free),flush=True)
assert not waiting and len(free)==5
kernels=[{**{ids[i]:-row[f] for i,row in piv.items() if f in row},ids[f]:one} for f in free]
for ker in kernels:
 for letter in range(4):
  total={}
  for i,c in ker.items():A.addto(total,A.right[10][i,letter],c);A.addto(total,A.left[10][letter,i],-c)
  assert not total
out={'status':'PASS','weight0_columns':len(ids),'constant_pivots':len(piv),'free':5,'centers':[{''.join('xybc'[j] for j in A.basis[9][i]):{str(w):list(map(str,c.to_list())) for w,c in co.items()} for i,co in ker.items()} for ker in kernels]}
from sympy.polys.matrices import DomainMatrix
def ev00(co):return co.get((0,0),F.zero)
def boundary(poly):
 assert all(c.is_ground for w,c in poly.items() if 0 not in w)
 return {tuple(j-1 for j in w):ev00(c) for w,c in poly.items() if 0 not in w and ev00(c)}
S=GradedAlgebra(F,3,[boundary(r) for r in RC if any(0 not in w for w in r)]+[boundary(G)],[0,1,2]);S.build(9)
def bvec(poly):
 ans={}
 for w,c in boundary(poly).items():S.addto(ans,S.word(w),c)
 return ans
known=S.word((0,)*9)
def rank(rows):return DomainMatrix.from_dod(dict(enumerate(rows)),(len(rows),len(S.basis[9])),F).rank()
for ker in kernels:
 poly={A.basis[9][i]:c for i,c in ker.items()}
 bv=bvec(poly)
 if rank([known,bv])==2:break
assert rank([known,bv])==2
Psi={(1,1,1):one,(0,1,1):v,(0,0,1):u}
for letter in range(4):
 total={}
 for w,c in Psi.items():A.addto(total,A.word(w+(letter,)),c);A.addto(total,A.word((letter,)+w),-c)
 assert not total
rels=[boundary(r) for r in RC+[G,Psi,poly] if any(0 not in w for w in r)]
T=GradedAlgebra(F,3,rels,[0,1,2]);T.build(13);dims=[len(T.basis[j]) for j in range(14)]
print('ARTINIAN',dims,'SUM',sum(dims),flush=True)
assert dims==[1,3,6,8,9,9,9,9,9,8,6,3,1,0]
out.update({'field':'t^6-t^3+1','omega':'t^3-1','parameters':['u','v'],'scope':'all six characteristic-zero embeddings; all parameter-constant pivot identities','chosen_center':{''.join('xybc'[j] for j in w):{str(mon):list(map(str,c.to_list())) for mon,c in co.items()} for w,co in poly.items()},'Artinian_dimensions':dims,'Psi':'y3+vxy2+ux2y'})
Path(__file__).with_name('cubic_third_root_unit_boundary_axis_center_certificate.json').write_text(json.dumps(out,indent=2))

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
Path(__file__).with_name('cubic_third_root_unit_boundary_axis_center_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS allu,v polynomial center, parameter-independent boundary and Artinian total81')
