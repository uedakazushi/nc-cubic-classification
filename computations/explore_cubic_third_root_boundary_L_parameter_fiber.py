#!/usr/bin/env python3
"""Build exact or modular v1,u=a center-fiber polynomial matrices.
Example: --prime 109 --root 15 --output /tmp/L_matrices.json
Omit prime/root for characteristic zero; --fiber-z 1 selects a second fiber.
"""
import argparse,json,sympy as s
from pathlib import Path
from cubic_incremental_graded import GradedAlgebra
from sympy.polys.matrices import DomainMatrix

def build_model(prime=None,root=None,fiber_z=None):
 if prime:
  p,t=prime,root
  assert t is not None and s.isprime(p) and (t**6-9*t**3+57)%p==0
  F=s.GF(p);K=F.poly_ring('a');u=K.gens[0];v=K.one;d=K.convert(t);e=K.convert(2)
  o=(K.one-d**3)/K.convert(7)
 else:
  z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z**6-9*z**3+57,z));K=F.poly_ring('a');u=K.gens[0];v=K.one;d=K.convert(F.unit,F);e=K.convert(2);o=(1-d**3)/7
 one,zero=K.one,K.zero;Y=e**3
 assert not(o*o+o+one) and o!=one
 D=json.loads(Path(__file__).with_name('cubic_third_root_unit_boundary_L_polynomial_center_certificate.json').read_text())
 def coeff(cs):
  if prime:
   ans=0
   for c in cs:
    q=s.Rational(c);ans=(ans*t+int(q.p)*pow(int(q.q),-1,p))%p
   return K.convert(ans)
  acc=F.zero
  for c in cs:acc=acc*F.unit+F.convert(s.Rational(c))
  return K.convert(acc,F)

 Z={tuple('xybc'.index(j) for j in w):sum((coeff(cs)*u**int(mon.split(',')[0]) for mon,cs in cos.items()),zero) for w,cos in D['Z9_C_word_polynomial_coefficients'].items()}
 R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
  {(1,2):d,(2,1):e,(3,3):one},{(1,3):e,(3,1):d,(2,2):one},
  {(2,3):d,(3,2):e,(0,0):u,(0,1):v,(1,1):one}]
 C=(-(o+2)*Y**2+(one-o)*Y-o*e**2*d-(o+1)*e*d**2)/(Y-one)
 Ac=(-(o+2)*Y**2-2*o*Y-(o+1)*e**2*d-o*e*d**2+one)/(Y-one)
 Bc=d/(Y-one);Kc=((o+1)*Y+o*e**2*d+o*e*d**2-one)/(Y-one)**2
 G={(2,2,2):o,(2,3,1):-d*((o+2)*Y+o**2),(3,2,1):e*(2-(o+2)*Y),(3,3,3):one,(1,1,0):v*Ac,(2,3,0):v*Bc,(1,0,0):u*C+v**2*Kc,(0,0,0):u*v*Kc}
 weights=[0,0,1,2];RC=[{w:c/o**weights[w[1]] for w,c in rr.items()} for rr in R];GC={w:c/o**sum(j*weights[ww] for j,ww in enumerate(w)) for w,c in G.items() if c}
 Psi=dict(GC);Q=(o+2)*(one-Y)
 H=(3*(o+1)*Y+(2*o+one)*(e**2*d+e*d**2)-o-2)/(Y-one)
 J=((one-o)*e**2*d-(2*o+one)*e*d**2)/(Y-one)**2
 for w,c in {(1,1,1):Q,(1,1,0):v*H,(1,0,0):u*H+v**2*J}.items():Psi[w]=Psi.get(w,zero)+c
 fiber_coefficients=D['old_positive_fiber_in_new_coordinates']['Z9'] if fiber_z is None else [str(fiber_z)]
 rz=dict(Z);rz[(0,)*9]=rz.get((0,)*9,zero)-coeff(fiber_coefficients)
 class PolyAlgebra(GradedAlgebra):
  def echelon(self,rows):
   piv={}
   for row in rows:
    row={j:c for j,c in row.items() if c}
    while row:
     j=min(row)
     if j not in piv:
      co=row[j];assert co.is_ground,('nonunit',str(co))
      piv[j]={k:K.exquo(c,co) for k,c in row.items()};break
     self.addto(row,piv[j],-row[j])
   return piv
 A=PolyAlgebra(K,4,RC+[GC,Psi,rz],weights);A.build(13)
 assert len(A.basis[12])==len(A.basis[13])==81
 X=DomainMatrix.from_dod({i:{j:A.right[13][j,0].get(i,zero) for j in range(81) if A.right[13][j,0].get(i,zero)} for i in range(81)},(81,81),K)
 num,den=X.inv_den();assert den.is_ground
 XI=num.applyfunc(lambda c:K.exquo(c,den),K)
 ops=[]
 for j in range(4):
  M=DomainMatrix.from_dod({i:{k:A.right[13][k,j].get(i,zero) for k in range(81) if A.right[13][k,j].get(i,zero)} for i in range(81)},(81,81),K)
  ops.append(XI.matmul(M))
 CM,ids=A.normal_matrix(12,[one]*4,fixed=False)
 def encode(M):return {'shape':list(M.shape),'entries':{str(i)+','+str(j):{str(mon[0]):(int(c) if prime else list(map(str,c.to_list()))) for mon,c in co.items() if c} for i,row in M.to_dod().items() for j,co in row.items() if co}}
 out={'field':'t^6-9t^3+57','v':1,'fiber_Psi':0,'fiber_Z_coefficients':fiber_coefficients,'basis':A.basis[12],'generators':[encode(M) for M in ops],'commutators':encode(CM),'status':'exact matrix construction only; no exceptional-ratio classification claim'}
 out.update({'p':prime,'root':root,'fiber_Z':(int(coeff(fiber_coefficients).get((0,),F.zero)) if prime else None)})
 out['relations']=[{''.join('xybc'[j] for j in w):{str(mon[0]):(int(c) if prime else list(map(str,c.to_list()))) for mon,c in co.items() if c} for w,co in rr.items() if co} for rr in RC+[GC,Psi,rz]]
 return out

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--prime',type=int);parser.add_argument('--root',type=int)
 parser.add_argument('--fiber-z');parser.add_argument('--output',required=True)
 args=parser.parse_args();out=build_model(args.prime,args.root,args.fiber_z)
 Path(args.output).write_text(json.dumps(out))
 print('polynomial matrix model PASS')
