#!/usr/bin/env python3
"""Independent exact center check and formal Morse type at the known bad value.
The cubic comes from proved-bounded exact reconstruction. All computations are
in QQ(g),g^4=2; the A3 normal form is over an algebraic closure, char0.
"""
import sympy as s,json
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
root=Path(__file__).parent;T,D=s.symbols('g D');K=s.QQ.alg_field_from_poly(s.Poly(T**4-2,T));g=K.unit;zero,one=K.zero,K.one
cert=json.loads((root/'cubic_order4_center_relation_certificate.json').read_text());assert cert['status'].startswith('complete exact')
def evalexpr(text,d):
 expr=s.cancel(s.sympify(text));num,den=s.fraction(expr)
 def pe(poly):
  out=zero
  for (i,j),c in s.Poly(poly,T,D,domain=s.QQ).terms():out+=K.convert(c)*g**i*d**j
  return out
 return pe(num)/pe(den)
def txt(c):
 v=c.to_list();return str(s.factor(sum(s.Rational(str(a))*T**(len(v)-1-i) for i,a in enumerate(v))))
dstar=(2*g**4+10*g**3+21*g*g+19*g+13)/(4*(1+g)**5)
center=json.loads((root/'cubic_order4_center_certificate.json').read_text())['basis'][:3];point=[]
for zi in center:point.append(sum((evalexpr(row['coefficient'],dstar) for row in zi if 2 not in row['word']),zero))
terms=[]
for exps,name in [((0,0,3),'Z3^3'),((0,3,0),'Z2^3'),((3,0,0),'Z1^3'),((1,1,1),'Z1*Z2*Z3')]:terms.append((0,*exps,evalexpr(cert['leading_cubic'][name],zero)))
for k,block in zip([2,1,0],cert['coefficient_blocks']):
 for row in block:
  d,i,j=row['exponents'];terms.append((d,i,j,k,evalexpr(row['coefficient'],zero)))
def ev(deriv=(0,0,0,0)):
 out=zero
 for *exps,c in terms:
  coeff=c
  for e,n,v in zip(exps,deriv,[dstar,*point]):
   if e<n:coeff=zero;break
   for t in range(n):coeff*=e-t
   coeff*=v**(e-n)
  out+=coeff
 return out
assert not ev();grad=[ev(tuple(int(j==i+1) for j in range(4))) for i in range(3)];H=[]
for i in range(3):
 row=[]
 for j in range(3):
  diff=[0]*4;diff[i+1]+=1;diff[j+1]+=1;row.append(ev(diff))
 H.append(row)
HM=DomainMatrix.from_dod({i:{j:c for j,c in enumerate(row) if c} for i,row in enumerate(H)},(3,3),K)
result={'version':'classification-v16','scope':'Exact full-center check at known bad Dstar; A3 center does not suffice for H3; no all-bad-D claim','Dstar':txt(dstar),'center_point':list(map(txt,point)),'center_equation_verified':True,'gradient':list(map(txt,grad)),'Hessian_rank':HM.rank(),'D_derivative':txt(ev((1,0,0,0)))}
if all(not q for q in grad):
 result['center_status']='singular'
 if HM.rank()==3:result['formal_center_type']='A1 by nondegenerate Hessian'
 if HM.rank()==2:
  ker=HM.nullspace().to_list()[0];coef=zero
  for d,i,j,k,c in terms:
   if i+j+k==3:coef+=c*ker[0]**i*ker[1]**j*ker[2]**k
  result['kernel_cubic']=txt(coef)
  if coef:result['formal_center_type']='A2 by rank2 Hessian and nonzero kernel cubic'
else:result['center_status']='smooth'
# Formal Morse elimination at fixed Dstar: F(point+delta)=1/2 delta^T H delta+Phi(delta).
if not any(grad) and HM.rank()==2:
 from itertools import combinations
 kernel=HM.nullspace().to_list()[0];scale=next(q for q in kernel if q);kernel=[q/scale for q in kernel]
 for i,j in combinations(range(3),2):
  a,b=H[i][i],H[i][j];c,d=H[j][i],H[j][j];delta=a*d-b*c
  if delta:
   transverse=(i,j);inv=[[d/delta,-b/delta],[-c/delta,a/delta]];break
 # Polynomials in (u,v,s), over K.
 def pmul(P,Q):
  out={}
  for e,a in P.items():
   for f,b in Q.items():
    w=tuple(x+y for x,y in zip(e,f));out[w]=out.get(w,zero)+a*b
  return {e:c for e,c in out.items() if c}
 lin=[]
 for k in range(3):
  z={}
  if k==transverse[0]:z[(1,0,0)]=one
  if k==transverse[1]:z[(0,1,0)]=one
  if kernel[k]:z[(0,0,1)]=kernel[k]
  lin.append(z)
 cubic={}
 for deg,i,j,k,c in terms:
  if i+j+k!=3:continue
  poly={(0,0,0):c}
  for L,n0 in zip(lin,[i,j,k]):
   for _ in range(n0):poly=pmul(poly,L)
  for e,c in poly.items():cubic[e]=cubic.get(e,zero)+c
 N=8
 def smul(A,B):
  out=[zero]*(N+1)
  for i,a in enumerate(A):
   if not a:continue
   for j,b in enumerate(B[:N+1-i]):
    if b:out[i+j]+=a*b
  return out
 def speval(P,series):
  out=[zero]*(N+1)
  for powers,c in P.items():
   val=[c]+[zero]*N
   for A,n0 in zip(series,powers):
    for _ in range(n0):val=smul(val,A)
   out=[a+b for a,b in zip(out,val)]
  return out
 derivative=[]
 for i in range(2):
  P={}
  for e,c in cubic.items():
   if e[i]:f=list(e);f[i]-=1;P[tuple(f)]=c*e[i]
  derivative.append(P)
 U=[zero]*(N+1);V=[zero]*(N+1);S=[zero,one]+[zero]*(N-1)
 for n0 in range(2,N+1):
  rhs=[speval(P,[U,V,S])[n0] for P in derivative]
  U[n0]=-inv[0][0]*rhs[0]-inv[0][1]*rhs[1];V[n0]=-inv[1][0]*rhs[0]-inv[1][1]*rhs[1]
 for i in range(2):
  res=speval(derivative[i],[U,V,S]);res=[c+H[transverse[i]][transverse[0]]*u+H[transverse[i]][transverse[1]]*v for c,u,v in zip(res,U,V)]
  assert not any(res)
 residual=speval(cubic,[U,V,S]);UU=smul(U,U);UV=smul(U,V);VV=smul(V,V)
 residual=[c+(H[transverse[0]][transverse[0]]*uu+2*H[transverse[0]][transverse[1]]*uv+H[transverse[1]][transverse[1]]*vv)/2 for c,uu,uv,vv in zip(residual,UU,UV,VV)]
 first=next((i for i,c in enumerate(residual) if c),None)
 qv=[cubic.get((1,0,2),zero),cubic.get((0,1,2),zero)]
 schur=-sum((qv[i]*inv[i][j]*qv[j] for i in range(2) for j in range(2)),zero)/2
 assert residual[4]==schur
 result.update({'normalized_Hessian_kernel':list(map(txt,kernel)),'Morse_transverse_indices':list(transverse),'Morse_residual_first_degree':first,'Morse_residual_first_coefficient':txt(residual[first]) if first is not None else '0 through8','formal_center_type':'A'+str(first-1) if first is not None else 'not identified through8','Morse_gradient_identity_checked_through':N,'independent_quartic_Schur_check':True})
 assert first==4 and residual[first] and not ev((1,0,0,0))
 (root/'cubic_order4_bad_center_certificate.json').write_text(json.dumps(result,indent=2)+'\n');print('FORMAL MORSE RESULT',json.dumps(result,indent=2),flush=True)
