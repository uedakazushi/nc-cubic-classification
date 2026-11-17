#!/usr/bin/env python3
"""All-value axis normal-cubic Smith forms and exact exceptional generators.
This is a necessary boundary restriction, not cut admissibility at105 points.
"""
from pathlib import Path
import json,sympy as s
from cubic_incremental_graded import GradedAlgebra
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));T=s.Symbol('T');K=F.frac_field(T);t=K.gens[0];o=K.convert(F.unit,F);P=F.poly_ring(T);one,zero=K.one,K.zero
class AxisAlgebra(GradedAlgebra):
 def echelon(self,rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j];assert len(co.numer.terms())==len(co.denom.terms())==1
     piv[j]={k:c/co for k,c in row.items()};break
    self.addto(row,piv[j],-row[j])
  return piv
def relations(K,d,e):
 return [{(0,1):d,(1,0):e,(2,2):K.one},{(0,2):e,(2,0):d,(1,1):K.one},{(1,2):d,(2,1):e,(0,0):K.one}]
out={'status':'PASS','scope':'all nonzero axis parameters: necessary normalizer-fixed boundary cubics only','axes':{}}
for axis in ['Ezero','Dzero']:
 d,e=(t,zero) if axis=='Ezero' else (zero,t)
 A=AxisAlgebra(K,3,relations(K,d,e),[0,1,2]);M,ids=A.normal_matrix(3,[one,o**2,o],fixed=True)
 assert M.shape==(11,4) and [len(A.basis[j]) for j in range(5)]==[1,3,6,10,15]
 rows={}
 for i,row in M.to_dod().items():
  for c in row.values():assert len(c.denom.terms())==1
  power=max((c.denom.degree() for c in row.values()),default=0)
  rows[i]={j:P.convert(c*t**power,K) for j,c in row.items()}
 MP=DomainMatrix.from_dod(rows,M.shape,P).to_dense()
 SD,U,V=smith_normal_decomp(MP);assert U.matmul(MP).matmul(V)==SD
 ud,vd=U.det(),V.det();assert ud and vd and ud.degree()==vd.degree()==0
 factors=[SD.to_list()[j][j].monic() for j in range(4)]
 expected=P.from_sympy(T**3+F.to_sympy(F.unit**(2 if axis=='Ezero' else 1)))
 assert factors==[P.one,P.one,P.one,expected]
 # Fresh quotient at all six characteristic-zero embeddings of Phi18.
 poly=s.Poly(z**6-z**3+1,z);assert poly.is_irreducible
 L=s.QQ.alg_field_from_poly(poly);a=L.unit;omega=a**3-L.one if axis=='Ezero' else -a**3
 assert not(omega**2+omega+L.one)
 dd,ee=(a,L.zero) if axis=='Ezero' else (L.zero,a)
 B=GradedAlgebra(L,3,relations(L,dd,ee),[0,1,2]);NM,ni=B.normal_matrix(3,[L.one,omega**2,omega],fixed=True)
 ker=NM.nullspace();assert ker.shape[0]==1 and NM.rank()==3 and not any(ker.matmul(NM.transpose()).to_list_flat())
 row=ker.to_list()[0];lc=next(c for c in row if c);gamma={B.basis[3][ni[j]]:c/lc for j,c in enumerate(row) if c}
 out['axes'][axis]={'matrix_shape':list(M.shape),'Smith_factors':[str(f.as_expr()) for f in factors],'relation_pivots_units_on_nonzero_axis':True,'Smith_transformation_identity':'PASS','Smith_transformation_determinants_constant':True,'exceptional_field':'t^6-t^3+1','parameter':'D=t' if axis=='Ezero' else 'E=t','omega':'t^3-1' if axis=='Ezero' else '-t^3','Gamma3_in_original_ybc_words':{''.join('ybc'[j] for j in w):list(map(str,c.to_list())) for w,c in gamma.items()},'fresh_exceptional_normal_dimension':1}
print(json.dumps({'status':'PASS','Ezero':'D^3+omega^2=0','Dzero':'E^3+omega=0','exceptional_axis_points_per_fixed_omega':6,'total_with_previous99':105}))
Path(__file__).with_name('cubic_third_root_unit_boundary_axes_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
