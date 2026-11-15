#!/usr/bin/env python3
"""Universal normalized-potential arrows on the integrated Hesse chart.
QQ(zeta3)(h,gamma,A,B,C,beta_x,beta_y,beta_z), no parameter sampling.
The center-value action is an exact degree3 quotient linear solve in the paper;
this script verifies the envelope formulas and all nine generator compositions.
"""
from pathlib import Path
import json
import sympy as s
z=s.symbols('zeta');K=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z))
syms=s.symbols('h gamma A B C beta_x beta_y beta_z');F=K.frac_field(*syms)
h,g,A,B,C,bx,by,bz=map(F.convert,syms);zero,one=F.zero,F.one;omega=F.convert(K.unit,K)
def mm(M,N):return tuple(sum((M[3*i+k]*N[3*k+j] for k in range(3)),zero) for i in range(3) for j in range(3))
def mv(M,v):return tuple(sum((M[3*i+j]*v[j] for j in range(3)),zero) for i in range(3))
def det(M):
 a,b,c,d,e,f,g,i,j=M;return a*(e*j-f*i)-b*(d*j-f*g)+c*(d*i-e*g)
def tr(M):return tuple(M[3*j+i] for i in range(3) for j in range(3))
def peq(v,w):return all(not(a-b) for a,b in zip(v,w))
def pmul(P,Q):
 out={}
 for a,c in P.items():
  for b,d in Q.items():
   e=tuple(i+j for i,j in zip(a,b));out[e]=out.get(e,zero)+c*d
 return {e:c for e,c in out.items() if c}
def add(*terms):
 out={}
 for c,P in terms:
  for e,v in P.items():out[e]=out.get(e,zero)+c*v
 return {e:c for e,c in out.items() if c}
def cube(P):return pmul(pmul(P,P),P)
def hes(H,X):return add((F.convert(2),pmul(pmul(X[0],X[1]),X[2])),*[(-H/3,cube(p)) for p in X])
def top(M,H):
 X=[{tuple(int(i==j) for j in range(3)):M[3*k+i] for i in range(3) if M[3*k+i]} for k in range(3)]
 poly=hes(H,X);c=poly[(1,1,1)]/2;hp=-3*poly[(3,0,0)]/c
 assert all(not v for e,v in poly.items() if e not in [(3,0,0),(0,3,0),(0,0,3),(1,1,1)])
 assert poly[(3,0,0)]==poly[(0,3,0)]==poly[(0,0,3)]
 return hp,c
def data(M,H,G,a,beta):
 hp,c=top(M,H);dm=det(M)
 Q=tuple(sum((a[k]*M[3*k+i]*M[3*k+j] for k in range(3)),zero) for i in range(3) for j in range(3))
 off=(Q[5],Q[2],Q[1]);v=tuple(-2*G*q/c for q in off)
 ap=tuple((Q[3*i+i]+hp*off[i])/dm for i in range(3));gp=G*dm/c
 grad=tuple(2*v[(i+1)%3]*v[(i+2)%3]-hp*v[i]**2 for i in range(3))
 lin=mv(tr(M),beta);Qv=mv(Q,v)
 bp=tuple(lin[i]/c-grad[i]-4*G*Qv[i]/c for i in range(3));shift=mv(M,v)
 return (hp,gp,ap,bp,shift,c)
Id=tuple(F.convert(int(i==j)) for i in range(3) for j in range(3))
gens=[tuple(map(F.convert,[0,1,0,0,0,1,1,0,0])),(one,zero,zero,zero,one,zero,zero,zero,omega),(omega,omega**2,one,omega**2,omega,one,one,one,one)]
base=(h,g,(A,B,C),(bx,by,bz));ncomp=0;npot=0
for M in gens:
 H,G,a,beta,shift,c=data(M,*base)
 # Direct full commutative potential identity; antisymmetric cubic transforms by det(M).
 X=[{tuple(int(i==j) for j in range(4)):one} for i in range(3)];T={(0,0,0,1):one}
 Y=[add(*[(M[3*i+j],X[j]) for j in range(3)],(shift[i],T)) for i in range(3)]
 source=add((one,hes(h,Y)),*[(2*g*base[2][i],pmul(T,pmul(Y[i],Y[i]))) for i in range(3)],*[(-base[3][i],pmul(pmul(T,T),Y[i])) for i in range(3)])
 target=add((c,hes(H,X)),*[(2*c*G*a[i],pmul(T,pmul(X[i],X[i]))) for i in range(3)],*[(-c*beta[i],pmul(pmul(T,T),X[i])) for i in range(3)])
 residual=add((one,source),(-one,target));assert all(not v for e,v in residual.items() if e!=(0,0,0,3));npot+=1
 for N in gens:
  d2=data(N,H,G,a,beta);direct=data(mm(M,N),*base)
  assert not(direct[0]-d2[0]) and not(direct[1]-d2[1]) and peq(direct[2],d2[2]) and peq(direct[3],d2[3])
  expected_shift=tuple(x+y for x,y in zip(shift,mv(M,d2[4])))
  assert peq(direct[4],expected_shift);ncomp+=1
certificate={'version':'classification-v13','field':'QQ(zeta3)(h,gamma,A,B,C,beta_x,beta_y,beta_z)',
 'full_potential_generator_identities':npot,'universal_generator_compositions':ncomp,
 'formulas':{'top':'H_h(MX)=c H_hprime(X), gamma_prime=gamma det(M)/c',
 'Q':'M^T diag(A,B,C) M','v':'-2 gamma a0/c*(Q23,Q13,Q12)','translation':'b=Mv',
 'a_prime':'a0/det(M)*(Q11+hprime Q23,Q22+hprime Q13,Q33+hprime Q12)',
 'beta_prime':'a0^2/c M^T beta-grad H_hprime(v)-4 gamma a0/c Qv',
 'D_prime':'Unique two-column linear solve of the transformed central cubic against (G_target(D=0),t^3) in the degree3 quotient, divided by the nonzero first coefficient'},
 't_scaling_weights':{'a':1,'beta':2,'D':3},
 'scope':'Universal envelope formulas and composition/translation laws; all geometric arrows in the stated smooth Hesse chart follow by the ordinary proof. Not full bad-D enumeration, relative intrinsic descent or global H3 coverage.'}
Path(__file__).with_name('cubic_integrated_arrows_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS:3 universal normalized potential identities;9 exact Hessian generator compositions including affine translations; envelope arrows verified')
