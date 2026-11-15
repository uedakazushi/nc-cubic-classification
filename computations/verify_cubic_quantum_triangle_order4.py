import sympy as s,time
from functools import lru_cache
q=s.symbols('q')
def red(c):return s.rem(s.expand(c),q*q+1,q).expand()
rules={(1,0):[(-q,(0,1)),(q,(2,))],(2,0):[(q,(0,2)),(1,(1,))],(2,1):[(-q,(1,2)),(q,(0,))]}
@lru_cache(None)
def nf(w):
 for i in range(len(w)-1):
  if w[i]>w[i+1]:
   out={}
   for a,v in rules[w[i:i+2]]:
    for u,c in nf(w[:i]+v+w[i+2:]).items():out[u]=red(out.get(u,0)+a*c)
   return {u:c for u,c in out.items() if c!=0}
 return {w:s.Integer(1)}
def add(f,g,c=1):
 out=dict(f)
 for w,a in g.items():out[w]=red(out.get(w,0)+c*a)
 return {w:a for w,a in out.items() if a!=0}
def mul(f,g):
 out={}
 for u,a in f.items():
  for v,b in g.items():
   for w,c in nf(u+v).items():out[w]=red(out.get(w,0)+a*b*c)
 return {w:c for w,c in out.items() if c!=0}
O={(0,1,2):1,(0,0):-s.Rational(1,2),(1,1):s.Rational(1,2),(2,2):-s.Rational(1,2)}
XYZ=[{(i,i,i,i):1,(i,i):-q,():-s.Rational(1,8)} for i in range(3)]
for C in XYZ+[O]:
 for i in range(3):assert not add(mul(C,{(i,):1}),mul({(i,):1},C),-1)
O2=mul(O,O);F=mul(mul(XYZ[0],XYZ[1]),XYZ[2]);F=add(F,mul(O2,O2))
for C in XYZ:F=add(add(F,mul(C,C),s.Rational(1,16)),mul(O2,C),-s.Rational(1,2))
F=add(add(F,O2,s.Rational(1,16)),{():s.Rational(1,1024)},-1)
assert not F,F
print('PASS exact q4 full centre relation')
# Complete singular-centre cases, including collision D4.
u,v,w,k,z=s.symbols('u v w k z');F4=u*v*w-u*u-v*v-w*w-2*k*(u+v+w)-k*k-4*k+4
assert s.expand(F4.subs({u:-2,v:-2,w:2-k}))==0
assert s.expand(F4.subs({u:z,v:z,w:z,k:(z*z-2*z)/2})+(z-2)*(z+2)**3/4)==0
assert s.factor(s.hessian(F4,(u,v,w)).det().subs({u:-2,v:-2,w:2-k}))==2*(k-4)**2
A,B,C=s.symbols('A B C');assert s.expand(F4.subs({u:A-2,v:B-2,w:C-2,k:4})-(A*B*C-(A+B+C)**2))==0
# Universal fifth-root-independent 2D family at q4; c nonzero unless D=1/4.
b=s.symbols('b')
def rat(c):
 n,d=s.cancel(c).as_numer_denom();return red(red(n)*s.invert(red(d),q*q+1,q))
a=(1+q)/2;c=a*a-b*b;xx=s.diag(a,-a);yy=s.Matrix([[b,1],[c,b]]);zz=s.Matrix([[b,q],[-q*c,-b]]);Id=s.eye(2)
for L,M,N in [(yy,zz,xx),(zz,xx,yy),(xx,yy,zz)]:assert all(rat(t)==0 for t in L*M-q*M*L-N)
Om=(xx*yy*zz+(xx*xx+q*q*yy*yy+zz*zz)/(q*q-1)).applyfunc(rat);assert Om==(q*b*b+s.Rational(1,4))*Id
centres=[(M**4-q*M*M-Id/8).applyfunc(rat) for M in [xx,yy,zz]]
assert centres[0]==Id/8 and centres[2]==Id/8
assert centres[1]==(-4*b**4+2*q*b*b+s.Rational(1,8))*Id
assert rat(-16*centres[1][0,0]-(2-64*Om[0,0]**2))==0
import json
from pathlib import Path
cert={'version':'classification-v51','base':'q^2+1=0','full_centre':'XYZ+(X²+Y²+Z²)/16-Omega²*(X+Y+Z)/2+Omega^4+Omega²/16-1/1024=0','normalization':'Gamma_i=-16 X_i, k=64D²','singularities':'three A1 for k!=0,4; four A1 at k0; one D4 at k4','bad_D':['1/4','-1/4'],'good':'Every other D; persistent A1 receive 2D reps, extra A1 at D0 receives origin character','exact_checks':['PBW full centre relation degree12','all central commutators','singular fibre factorization and D4 tangent model','2x2 family relations, Casimir and central positions'],'limits':'Ordinary proof supplies full-centre equality, maximality, McKay and terminal infinity; not all even orders.'}
Path(__file__).with_name('cubic_quantum_triangle_order4_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS q4 full H3 singular-centre and representation certificates')
