#!/usr/bin/env python3
"""All-u,v normal cubic kernels at the six exceptional axis parameters.
The normalizer is delta=(1,1,omega^2,omega) in the CY untwist C.
This does not decide domain/finite global dimension of the resulting cuts.
"""
from pathlib import Path
import json,sympy as s
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z**6-z**3+1,z));tt=F.unit;out={'status':'PASS','field':'t^6-t^3+1','axes':{}}
for axis in ['Ezero','Dzero']:
 K=F.poly_ring('u','v');u,v=K.gens;one,zero=K.one,K.zero;t=K.convert(tt,F)
 o=K.convert(tt**3-F.one if axis=='Ezero' else -tt**3,F);d,e=(t,zero) if axis=='Ezero' else (zero,t)
 R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
 {(1,2):d,(2,1):e,(3,3):one},{(1,3):e,(3,1):d,(2,2):one},
 {(2,3):d,(3,2):e,(0,0):u,(0,1):v,(1,1):one}]
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
 assert not rows and len(piv)==7 and len(ids)==8
 G=({(1,3,2):one,(2,1,3):o**2,(3,2,1):one,(2,3,0):v*o**2,(3,2,0):v,(1,0,0):-u*d*d} if axis=='Ezero' else
    {(1,2,3):one,(2,3,1):one,(3,1,2):o,(2,3,0):v,(3,2,0):v*o,(1,0,0):-u*e*e})
 vector={}
 for w,c in G.items():A.addto(vector,A.word(w),c)
 assert all(i in ids for i in vector)
 free=next(j for j in range(8) if j not in piv)
 lc=vector.get(ids[free],zero);assert lc and lc.is_ground
 expected={free:one,**{j:-row[free] for j,row in piv.items() if free in row}}
 actual={j:K.exquo(vector.get(i,zero),lc) for j,i in enumerate(ids) if vector.get(i,zero)}
 assert actual==expected
 for letter,phase in enumerate([one,one,o**2,o]):
  total={}
  for w,c in G.items():A.addto(total,A.word(w+(letter,)),c);A.addto(total,A.word((letter,)+w),-phase*c)
  assert not total
 def encode(poly):return {''.join('xybc'[j] for j in w):{','.join(map(str,mon)):list(map(str,c.to_list())) for mon,c in co.items()} for w,co in poly.items() if co}
 out['axes'][axis]={'normal_matrix_shape':list(M.shape),'parameter_constant_pivots':7,'zero_residuals':True,'normal_free_rank':1,'all_original_generator_normal_equations':'PASS','G3_C_coordinates':encode(G),'omega':'t^3-1' if axis=='Ezero' else '-t^3'}
out['scope']='all six field embeddings and all u,v after allowed axis Z-shear; normal incidence only'
out['not_claimed']=['axis cut domain','axis cut finite global dimension','axis H3 admissibility','complete H3 classification']
Path(__file__).with_name('cubic_third_root_unit_boundary_axis_incidence_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','both_axis_normal_kernels':'free rank1 over coefficient field[u,v]','all_original_normal_equations':'PASS'}))
