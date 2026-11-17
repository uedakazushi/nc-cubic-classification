"""Exact Laurent-binomial reduction with all torsion components retained.
Every scalar is computed in a cyclotomic number field; no chosen torus branch.
"""
import sympy as s,functools
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
@functools.lru_cache(None)
def roots(mod):
 z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(mod,z),z));powers=[F.unit**j for j in range(mod)];return F,powers,{c:j for j,c in enumerate(powers)}
class Reducer:
 def __init__(self,A,b,nvar,mod):
  self.mod=mod;self.nvar=nvar;self.F,self.powers,self.rootmap=roots(mod)
  if not A:self.V=s.eye(nvar).tolist();self.diag=[];self.h=[];return
  DM=DomainMatrix.from_Matrix(s.Matrix(A)).convert_to(s.ZZ).to_dense();D,U,V=smith_normal_decomp(DM);assert U.matmul(DM).matmul(V)==D and abs(U.det())==1 and abs(V.det())==1
  dl=D.to_list();self.diag=[int(dl[j][j]) for j in range(min(D.shape)) if dl[j][j]];self.V=[list(map(int,r)) for r in V.to_list()];self.h=[sum(int(c)*v for c,v in zip(row,b))%mod for row in U.to_list()];assert all(x==0 for x in self.h[len(self.diag):])
 def mono(self,e):
  vals=[sum(e[j]*self.V[j][k] for j in range(self.nvar)) for k in range(self.nvar)];phase=0
  for k,d in enumerate(self.diag):r=vals[k]%abs(d);q=(vals[k]-r)//d;vals[k]=r;phase+=q*self.h[k]
  return tuple(vals),phase%self.mod
 def polynomial(self,terms):
  groups={};reps={};shifts={}
  for ex,phase in terms:
   key,sh=self.mono(ex)
   if key not in groups:groups[key]=self.F.zero;reps[key]=ex;shifts[key]=sh
   groups[key]+=self.powers[(phase+sh)%self.mod]
  return [(tuple(reps[k]),c*self.powers[-shifts[k]%self.mod]) for k,c in groups.items() if c]
def close(A,b,polys,nvar,mod):
 A=list(A);b=list(b);count=0
 while True:
  red=Reducer(A,b,nvar,mod);new=False
  for terms in polys:
   pp=red.polynomial(terms)
   if len(pp)==1:return None,None,count
   if len(pp)==2:
    ratio=-pp[1][1]/pp[0][1]
    if ratio in red.rootmap:
     A.append(tuple(x-y for x,y in zip(pp[0][0],pp[1][0])));b.append(red.rootmap[ratio]);new=True;count+=1;break
  if not new:return A,b,count
  # Check the enlarged root-valued torus equations before creating next reducer.
  DM=DomainMatrix.from_Matrix(s.Matrix(A)).convert_to(s.ZZ).to_dense();DD,U,V=smith_normal_decomp(DM);assert U.matmul(DM).matmul(V)==DD and abs(U.det())==1 and abs(V.det())==1;r=sum(bool(DD[i,i].element) for i in range(min(DD.shape)))
  if any(sum(int(x)*y for x,y in zip(row,b))%mod for row in U.to_list()[r:]):return None,None,count
