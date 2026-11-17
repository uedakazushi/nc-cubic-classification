#!/usr/bin/env python3
"""All-u,v polynomial central degree9 and free rank81 certificate at E=2.
All divisions in relation and central Gaussian reduction are parameter constants.
No full-center or generic-CSA assertion for every parameter is made.
"""
from pathlib import Path
import sympy as s,json
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z**6-9*z**3+57,z));K=F.poly_ring('u','v');u,v=K.gens;d=K.convert(F.unit,F);e=K.convert(2);o=(1-d**3)/7;one,zero=K.one,K.zero
# Only parameter-constant pivots are accepted in relation reduction.
class PolyAlgebra(GradedAlgebra):
 def echelon(self,rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j]
     assert co.is_ground,('nonconstant relation pivot',j,str(co))
     piv[j]={k:K.exquo(c,co) for k,c in row.items()};break
    self.addto(row,piv[j],-row[j])
  return piv
R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
 {(1,2):d,(2,1):e,(3,3):one},{(1,3):e,(3,1):d,(2,2):one},
 {(2,3):d,(3,2):e,(0,0):u,(0,1):v,(1,1):one}]
Y=e**3
C=(-(o+2)*Y**2+(one-o)*Y-o*e**2*d-(o+1)*e*d**2)/(Y-one)
Ac=(-(o+2)*Y**2-2*o*Y-(o+1)*e**2*d-o*e*d**2+one)/(Y-one)
Bc=d/(Y-one);Kc=((o+1)*Y+o*e**2*d+o*e*d**2-one)/(Y-one)**2
G={(2,2,2):o,(2,3,1):-d*((o+2)*Y+o**2),(3,2,1):e*(2-(o+2)*Y),(3,3,3):one,(1,1,0):v*Ac,(2,3,0):v*Bc,(1,0,0):u*C+v**2*Kc,(0,0,0):u*v*Kc}
weights=[0,0,1,2];RC=[{w:c/o**weights[w[1]] for w,c in r.items()} for r in R];GC={w:c/o**sum(j*weights[ww] for j,ww in enumerate(w)) for w,c in G.items() if c}
A=PolyAlgebra(K,4,RC+[GC],weights);A.build(10)
# Assemble centrality rows directly, with no field-of-fractions conversion.
rows=[]
for letter in range(4):
 rr={}
 for i in range(len(A.basis[9])):
  col=dict(A.right[10][i,letter]);A.addto(col,A.left[10][letter,i],-one)
  for j,c in col.items():rr.setdefault(j,{})[i]=c
 rows+=list(rr.values())
# Pick any unit pivot first. Nonconstant residuals are retained, never divided.
piv={};waiting=rows
while waiting:
 chosen=next(((index,j) for index,row in enumerate(waiting) for j,c in row.items() if c and c.is_ground),None)
 if chosen is None:break
 index,j=chosen;row=waiting.pop(index);co=row[j];row={k:K.exquo(c,co) for k,c in row.items()};piv[j]=row
 for jj,oldrow in piv.items():
  if jj!=j and j in oldrow:A.addto(oldrow,row,-oldrow[j])
 for other in waiting:
  if j in other:A.addto(other,row,-other[j])
 waiting=[r for r in waiting if r]
 if len(piv)%20==0 or not waiting:print('constant central pivots',len(piv),'remaining',len(waiting),flush=True)
print('FINAL constant pivots',len(piv),'residuals',len(waiting),'free',len(A.basis[9])-len(piv),flush=True)

free=[i for i in range(len(A.basis[9])) if i not in piv]
kernels=[{**{i:-row[f] for i,row in piv.items() if f in row},f:one} for f in free]
assert len(kernels)==5 and not waiting
for kernel in kernels:
 for letter in range(4):
  total={}
  for i,c in kernel.items():
   A.addto(total,A.right[10][i,letter],c);A.addto(total,A.left[10][letter,i],-c)
  assert not total
# Compare to the known four central monomials at u=1,v=0.
from sympy.polys.matrices import DomainMatrix
reference=json.loads(Path(__file__).with_name('cubic_third_root_unit_boundary_L_finite_center_certificate.json').read_text())
def anp(cc):return F.from_sympy(sum(s.Rational(c)*F.ext**(len(cc)-1-i) for i,c in enumerate(cc)))
def eval10(c):return sum((cc for (i,j),cc in c.items() if j==0),F.zero)
def eval00(c):return c.get((0,0),F.zero)
N=GradedAlgebra(F,4,[{w:eval10(c) for w,c in r.items() if eval10(c)} for r in RC+[GC]],weights);N.build(9)
ps={tuple('xybc'.index(c) for c in w):anp(cc) for w,cc in reference['Psi3_original_polynomial_C_coordinates'].items()}
def mul(a,b):
 out={}
 for w,c in a.items():
  for ww,dd in b.items():out[w+ww]=out.get(w+ww,F.zero)+c*dd
 return {w:c for w,c in out.items() if c}
def vector(poly):
 out={}
 for w,c in poly.items():N.addto(out,N.word(w),c)
 return out
known=[];pp={():F.one}
for j in range(4):
 known.append(vector(mul({(0,)*(9-3*j):F.one},pp)));pp=mul(pp,ps)
def rank(vectors):return DomainMatrix.from_dod({i:v for i,v in enumerate(vectors)},(len(vectors),len(N.basis[9])),F).rank()
assert rank(known)==4
for kernel in kernels:
 poly={A.basis[9][i]:c for i,c in kernel.items()}
 vv=vector({w:eval10(c) for w,c in poly.items() if eval10(c)})
 if rank(known+[vv])==5:break
assert rank(known+[vv])==5
oldz={tuple('xybc'.index(c) for c in w):anp(cc) for w,cc in reference['Z9_original_polynomial_C_coordinates'].items()}
center_rows=known+[vector(oldz)]
Cmat=DomainMatrix.from_dod({i:row for i,row in enumerate(center_rows)},(5,len(N.basis[9])),F)
_,center_pivots=Cmat.rref();assert len(center_pivots)==5
small=Cmat.extract(range(5),center_pivots)
vr=DomainMatrix.from_dod({0:{j:vv.get(c,F.zero) for j,c in enumerate(center_pivots) if vv.get(c,F.zero)}},(1,5),F)
coordinates=vr.matmul(small.inv()).to_list()[0]
reinsert={}
for co,row in zip(coordinates,center_rows):N.addto(reinsert,row,co)
assert reinsert==vv and coordinates[4]
family_CSA_fiber_b=coordinates[0]+coordinates[4]
zb={tuple(j-1 for j in w):c for w,c in poly.items() if 0 not in w}
assert zb and all(c.is_ground for c in zb.values())
def encode(poly):return {''.join('xybc'[j] for j in w):{','.join(map(str,mon)):list(map(str,c.to_list())) for mon,c in co.items()} for w,co in poly.items() if co}
out={'status':'PASS','field':'t^6-9t^3+57','parameters':['u','v'],'E':2,'constant_center9_pivots':len(piv),'center9_free_rank':5,'Z9_C_word_polynomial_coefficients':encode(poly),'boundary_Z9_parameter_independent':True,'original_generator_commutators_all5_kernel_vectors':'PASS','new_Z9_independent_of_known4_at_u1v0':'PASS','dimensions':[len(A.basis[j]) for j in range(11)]}

out['old_positive_fiber_in_new_coordinates']={'Psi':0,'Z9':list(map(str,family_CSA_fiber_b.to_list())),'coordinates_in_old_center9_basis':[list(map(str,c.to_list())) for c in coordinates],'old_basis_order':['x9','x6Psi','x3Psi2','Psi3','oldZ9'],'coordinate_identity_reinserted':'PASS'}
print('all-parameter polynomial center PASS; Z9 terms',len(poly),'boundary terms',len(zb),flush=True)

# The boundary Artinian quotient is independent of u,v.
Q=(o+2)*(one-Y)
Psi=dict(GC)
H=(3*(o+1)*Y+(2*o+one)*(e**2*d+e*d**2)-o-2)/(Y-one)
J=((one-o)*e**2*d-(2*o+one)*e*d**2)/(Y-one)**2
for w,c in {(1,1,1):Q,(1,1,0):v*H,(1,0,0):u*H+v**2*J}.items():Psi[w]=Psi.get(w,zero)+c
def boundary(poly):
 result={tuple(j-1 for j in w):eval00(c) for w,c in poly.items() if 0 not in w and c}
 assert all(c.is_ground for w,c in poly.items() if 0 not in w and c)
 return result
rels=[r for poly0 in RC+[GC,Psi,poly] if (r:=boundary(poly0))]
T=GradedAlgebra(F,3,rels,[0,1,2]);T.build(13)
dims=[len(T.basis[j]) for j in range(14)]
assert dims==[1,3,6,8,9,9,9,9,9,8,6,3,1,0]
def check_actions(alg,top):
 for rel in alg.relations:
  rrlen=len(next(iter(rel)))
  for n in range(rrlen,top+1):
   for i in range(len(alg.basis[n-rrlen])):
    for side in [0,1]:
     total={}
     for ww,c in rel.items():
      state={i:c};degree=n-rrlen
      for letter in (ww if side==0 else tuple(reversed(ww))):
       new={}
       for j,co in state.items():
        action=alg.right[degree+1][j,letter] if side==0 else alg.left[degree+1][letter,j]
        alg.addto(new,action,co)
       state=new;degree+=1
      alg.addto(total,state,alg.K.one)
     assert not total
check_actions(A,10);check_actions(T,13)
out.update({'Artinian_dimensions':dims,'central_base_degrees':[1,3,9],'all_parameter_free_central_rank':81,'original_left_right_relation_actions':'PASS polynomial through10, Artinian through13','scope':'E2 all6 embeddings, all u,v; fixed Z9 polynomial and central regular sequence; full center and CSA degree not asserted for every parameter','not_claimed':['all-parameter full center','all-parameter generic CSA degree9','all-parameter H3 exclusion','complete H3 classification']})
Path(__file__).with_name('cubic_third_root_unit_boundary_L_polynomial_center_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('all-u,v finite-free rank81 and source actions PASS')
