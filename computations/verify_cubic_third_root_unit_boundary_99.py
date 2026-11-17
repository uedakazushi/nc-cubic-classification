#!/usr/bin/env python3
"""Exact characteristic-zero exclusion of all99 nonaxis singular boundary points.
Arithmetic embeddings cover points; no geometric Galois quotient is asserted.
"""
import sys,json,sympy as s
from pathlib import Path
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');cases=[]
F2=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));cases+=[('linear1',F2,F2.unit,F2.one,1),('linearhalf',F2,F2.unit,F2.convert(s.Rational(-1,2)),1)]
assert s.Poly(z**6+z**3+1,z).is_irreducible
F6=s.QQ.alg_field_from_poly(s.Poly(z**6+z**3+1,z));q=F6.unit
cases += [('cubicA',F6,q**6,F6.one/(q-F6.one),3),('cubicB',F6,q**3,F6.one/(q-F6.one),3),('cubicC',F6,q**3,q+F6.one/q-F6.one,3)]
records=[]
for name,F,o,t,degree in cases:
 assert not(o*o+o+F.one)
 ss=t*t+t+F.one/3
 if name=='cubicA':assert not(t**3+(F.one-o)*ss)
 if name=='cubicB':assert not(t**3+(2+o)*ss)
 if name=='cubicC':assert not(t**3+3*t*t-F.one)
 for a in range(3):
  for b in range(3):
   d=-o**b*(t+F.one);e=o**((b-a)%3)*t
   assert d and e and not(d**3==e**3==F.one)
   R=[{(0,1):d,(1,0):e,(2,2):F.one},{(0,2):e,(2,0):d,(1,1):F.one},{(1,2):d,(2,1):e,(0,0):F.one}]
   A=GradedAlgebra(F,3,R,[0,1,2]);M,ids=A.normal_matrix(3,[F.one,o**2,o],fixed=True)
   assert [len(A.basis[j]) for j in range(5)]==[1,3,6,10,15]
   rank=M.rank();print(name,a,b,'shape',M.shape,'rank',rank,flush=True)
   assert len(ids)==4 and rank==4
   _,rows=M.transpose().rref();assert len(rows)==4
   minor=M.extract(rows,range(4));det=minor.det();assert det
   records.append({'case':name,'a':a,'b':b,'covered_roots_at_fixed_omega':degree,'matrix_shape':list(M.shape),'positive_minor_rows':list(rows),'determinant':list(map(str,det.to_list()))})
assert sum(r['covered_roots_at_fixed_omega'] for r in records)==99
Path(__file__).with_name('cubic_third_root_unit_boundary_99_certificate.json').write_text(json.dumps({'status':'PASS','records':records,'all99_normal_boundary_kernels_zero':True},indent=2)+'\n')
