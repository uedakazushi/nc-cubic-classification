#!/usr/bin/env python3
"""Explore degree9 center over the L-curve function field, polynomial in u,v.
Only parameter-constant pivots are used; this script is not a completed
characteristic-zero certificate. --prime 109 --omega 63 gives a diagnostic.
"""
import argparse,json,time,sympy as s
from pathlib import Path
from cubic_function_extension import CubicField
from cubic_parameter_polynomials import ParameterRing
from cubic_incremental_graded import GradedAlgebra
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--fixed-uv',choices=['u1v0','u0v1','v1']);parser.add_argument('--prime',type=int,default=109);parser.add_argument('--omega',type=int,default=63);parser.add_argument('--output',required=True)
args=parser.parse_args();start=time.monotonic()
E=s.Symbol('E')
if args.prime:
 assert s.isprime(args.prime)
 F=s.GF(args.prime);J=F.frac_field(E);ee=J.gens[0];oo=J.convert(args.omega)
 assert args.omega!=1 and (args.omega**2+args.omega+1)%args.prime==0
else:
 z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));J=F.frac_field(E);ee=J.gens[0];oo=J.convert(F.to_sympy(F.unit))
CF=CubicField(J,-oo*ee**3-oo**2);K=ParameterRing(CF);d=K.convert(CF.generator);e=K.convert(CF.convert(ee));o=K.convert(CF.convert(oo));u,v=K.u,K.v;one,zero=K.one,K.zero;Y=e**3
if args.fixed_uv=='u1v0':u,v=one,zero
if args.fixed_uv=='u0v1':u,v=zero,one
if args.fixed_uv=='v1':v=one
inverse_cache={}
def field_inverse(c):
 key=tuple(c.a)
 if key not in inverse_cache:inverse_cache[key]=c.inverse()
 return inverse_cache[key]
class PolyAlgebra(GradedAlgebra):
 def echelon(self,rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j];assert set(co.d)=={(0,0)},('nonconstant relation pivot',j,str(co))
     inv=field_inverse(co.d[(0,0)]);piv[j]={k:c*inv for k,c in row.items()};break
    self.addto(row,piv[j],-row[j])
  return piv
 def build(self,n):
  already=n in self.basis
  super().build(n)
  if not already:print('elapsed',n,round(time.monotonic()-start,2),'inverse count',len(CF.norm_log),flush=True)
R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
 {(1,2):d,(2,1):e,(3,3):one},{(1,3):e,(3,1):d,(2,2):one},
 {(2,3):d,(3,2):e,(0,0):u,(0,1):v,(1,1):one}]
C=(-(o+2)*Y**2+(one-o)*Y-o*e**2*d-(o+1)*e*d**2)/(Y-one)
Ac=(-(o+2)*Y**2-2*o*Y-(o+1)*e**2*d-o*e*d**2+one)/(Y-one)
Bc=d/(Y-one);Kc=((o+1)*Y+o*e**2*d+o*e*d**2-one)/(Y-one)**2
G={(2,2,2):o,(2,3,1):-d*((o+2)*Y+o**2),(3,2,1):e*(2-(o+2)*Y),(3,3,3):one,(1,1,0):v*Ac,(2,3,0):v*Bc,(1,0,0):u*C+v**2*Kc,(0,0,0):u*v*Kc}
weights=[0,0,1,2];RC=[{w:c/o**weights[w[1]] for w,c in rr.items()} for rr in R];GC={w:c/o**sum(j*weights[ww] for j,ww in enumerate(w)) for w,c in G.items() if c}
A=PolyAlgebra(K,4,RC+[GC],weights);A.build(10)
rows=[]
for letter in range(4):
 rr={}
 for i in range(len(A.basis[9])):
  col=dict(A.right[10][i,letter]);A.addto(col,A.left[10][letter,i],-one)
  for j,c in col.items():rr.setdefault(j,{})[i]=c
 rows+=list(rr.values())
piv={};waiting=rows
while waiting:
 chosen=next(((index,j) for index,row in enumerate(waiting) for j,c in row.items() if c and set(c.d)=={(0,0)}),None)
 if chosen is None:break
 index,j=chosen;row=waiting.pop(index);inv=field_inverse(row[j].d[(0,0)]);row={k:c*inv for k,c in row.items()};piv[j]=row
 for jj,old in piv.items():
  if jj!=j and j in old:A.addto(old,row,-old[j])
 for other in waiting:
  if j in other:A.addto(other,row,-other[j])
 waiting=[r for r in waiting if r]
 if len(piv)%10==0 or not waiting:print('center pivots',len(piv),'residuals',len(waiting),'seconds',round(time.monotonic()-start,2),flush=True)
free=[i for i in range(len(A.basis[9])) if i not in piv]
if not waiting:
 for f in free:
  kernel={**{i:-row[f] for i,row in piv.items() if f in row},f:one}
  for letter in range(4):
   total={}
   for i,c in kernel.items():A.addto(total,A.right[10][i,letter],c);A.addto(total,A.left[10][letter,i],-c)
   assert not total
out={'prime':args.prime,'omega':args.omega if args.prime else 'primitive symbolic','fixed_uv':args.fixed_uv,'constant_center_pivots':len(piv),'nonzero_residuals':len(waiting),'free_columns':len(free),'dimensions':[len(A.basis[j]) for j in range(11)],'inverse_count':len(CF.norm_log),'seconds':time.monotonic()-start,'scope':'function-field exploration; no assertion for every elliptic parameter or characteristic zero unless prime0 is completed'}
Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(out)
