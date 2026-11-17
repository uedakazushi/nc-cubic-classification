#!/usr/bin/env python3
"""Exact all-value w0 necessary boundary cover using Smith and fresh minors."""
import sys,json,sympy as s
from pathlib import Path
from cubic_incremental_graded import GradedAlgebra
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));P=F.poly_ring('e');K=F.frac_field('e');e=K.gens[0];o=K.convert(F.unit,F);one,zero=K.one,K.zero
pivot_log=[]
class Alg(GradedAlgebra):
 def echelon(self,rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j];pivot_log.append(co);piv[j]={k:c/co for k,c in row.items()};break
    self.addto(row,piv[j],-row[j])
  return piv
R=[{(0,1):one,(1,0):e,(2,2):one},{(0,2):e,(2,0):one,(1,1):one},{(1,2):one,(2,1):e}]
A=Alg(K,3,R,[0,1,2]);M,ids=A.normal_matrix(3,[one,o**2,o],fixed=True)
assert M.shape==(14,4) and len(ids)==4
rows={}
for i,row in M.to_dod().items():
 den=K.field.ring.one
 for c in row.values():den=den.lcm(c.denom)
 rows[i]={j:P.convert(c*K.new(den),K) for j,c in row.items()}
MP=DomainMatrix.from_dod(rows,M.shape,P).to_dense();SD,U,V=smith_normal_decomp(MP);assert U.matmul(MP).matmul(V)==SD

expected=P.from_sympy((s.Symbol('e')**3-1)*(s.Symbol('e')**3+F.to_sympy(F.unit**2)))
factors=[SD.to_list()[j][j].monic() for j in range(4)]
assert factors==[P.one,P.one,P.one,expected]
assert U.det().degree()==V.det().degree()==0 and U.det() and V.det()
support=e.numer*(e.numer**6-K.field.ring.one)
def supported(poly):
 while any(sum(mm)>0 for mm in poly.monoms()):
  gg=poly.gcd(support);assert any(sum(mm)>0 for mm in gg.monoms()),str(poly);poly=poly.exquo(gg)
for co in pivot_log:
 supported(co.numer);supported(co.denom)
for row in M.to_dod().values():
 for co in row.values():supported(co.denom)
fresh=[]
for name,dd,ee in [('Dzero',F.zero,F.one),('Ezero',F.one,F.zero)]+[('cube'+str(sign)+'_'+str(j),F.one,sign*F.unit**j) for sign in [1,-1] for j in range(3)]:
 R0=[{(0,1):dd,(1,0):ee,(2,2):F.one},{(0,2):ee,(2,0):dd,(1,1):F.one},{(1,2):dd,(2,1):ee}]
 R0=[{w:c for w,c in rr.items() if c} for rr in R0]
 B=GradedAlgebra(F,3,R0,[0,1,2]);NM,ni=B.normal_matrix(3,[F.one,F.unit**2,F.unit],fixed=True)
 assert len(ni)==4 and NM.rank()==4
 _,rp=NM.transpose().rref();det=NM.extract(rp,range(4)).det();assert det
 fresh.append({'case':name,'dimensions':[len(B.basis[j]) for j in range(5)],'minor_rows':list(rp),'determinant':list(map(str,det.to_list()))})
out={'status':'PASS','normalization':'w0,D1,E=e; axes tested separately','matrix_shape':list(M.shape),'relation_pivot_support':'e*(e^6-1)','Smith_factors':[str(f.as_expr()) for f in factors],'Smith_transformation_reinserted':True,'fresh_excluded':fresh,'only_possible_E':'E^3+omega^2=0','scope':'necessary boundary normal kernel only'}
Path(__file__).with_name('cubic_third_root_unit_boundary_w0_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS w0 allvalue necessary boundary cover')
