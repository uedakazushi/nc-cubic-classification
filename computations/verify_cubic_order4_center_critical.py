#!/usr/bin/env python3
"""Exact elimination of all center singular values; no H3 equivalence asserted."""
import sympy as s,json,itertools
from pathlib import Path
from sympy.polys.rings import ring
T=s.symbols('g');K=s.QQ.alg_field_from_poly(s.Poly(T**4-2,T));g=K.unit;R,D=ring('D',K);one,zero=R.one,R.zero
source=json.load(open(Path(__file__).parent/'cubic_order4_symmetric_center_certificate.json'))
def cv(text):return K.new(s.Poly(s.sympify(text),T,domain=s.QQ).all_coeffs())
def txt(c):
 v=c.to_list();return str(s.factor(sum(s.Rational(str(a))*T**(len(v)-1-i) for i,a in enumerate(v))))
def ser(P):return [{'D_power':e[0],'coefficient':txt(c)} for e,c in P.to_dict().items() if c]
polys={}
for row in source['terms']:
 d,i,j,k=row['powers'];polys[(i,j,k)]=polys.get((i,j,k),zero)+R(cv(row['coefficient']))*D**d
lam=cv(source['leading_Hesse_coefficient']);B=polys[(1,1,0)];C=polys[(1,0,1)];L=polys[(1,0,0)];N=polys[(0,0,1)];J=polys[(0,0,0)]
assert not (B.diff(D))
assert polys[(0,1,1)]==C and polys[(0,1,0)]==L
third=K.convert(s.Rational(1,3));a=-2*lam*third;b=-2*B*third;c=-4*C*third;d=-4*L*third
e=-lam*a/12;f=-lam*b/12-C*third;h=-lam*c/12;i=-lam*d/12-N*third
# u^2=a*uz+b*u+c*z+d ; z^2=e*uz+f*u+h*z+i.
A0=[c*i,c*f,c*h+d,b+c*e];B0=[f*d,f*b+i,f*c,f*a+h];den=1-a*e;assert den
A=[(x+a*y)/den for x,y in zip(A0,B0)];BB=[y+e*x for x,y in zip(A,B0)]
Mu=[[zero for _ in range(4)] for _ in range(4)];Mz=[[zero for _ in range(4)] for _ in range(4)]
for col,vec in enumerate([[zero,one,zero,zero],[d,b,c,R(a)],[zero,zero,zero,one],A]):
 for row,v in enumerate(vec):Mu[row][col]=v
for col,vec in enumerate([[zero,zero,one,zero],[zero,zero,zero,one],[i,f,h,R(e)],BB]):
 for row,v in enumerate(vec):Mz[row][col]=v
I=[[R(int(i==j)) for j in range(4)] for i in range(4)]
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(4)),zero) for j in range(4)] for i in range(4)]
def add(*args):return [[sum((c*A[i][j] for c,A in args),zero) for j in range(4)] for i in range(4)]
UU=mm(Mu,Mu);UZ=mm(Mu,Mz);ZZ=mm(Mz,Mz)
assert UZ==mm(Mz,Mu)
assert add((3,UU),(2*lam,UZ),(2*B,Mu),(4*C,Mz),(4*L,I))==[[zero]*4 for _ in range(4)]
assert add((lam,UU),(12,ZZ),(4*C,Mu),(4*N,I))==[[zero]*4 for _ in range(4)]
V=add((B*third,UU),(4*C*third,UZ),(8*L*third,Mu),(8*N*third,Mz),(4*J,I))
def det4(M):
 out=zero
 for p in itertools.permutations(range(4)):
  term=one
  for j in range(4):term*=M[j][p[j]]
  out+=(-1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1)*term
 return out
sym=det4(V)
w=lam*third;v=B*third
aa=R(w**3+lam*w*w+4);bb=3*w*w*v+2*lam*w*v+B*w*w+4*C*w
cc=3*w*v*v+lam*v*v+2*B*w*v+4*C*v+4*L*w+4*N
dd=v**3+B*v*v+4*L*v+4*J
assert aa and aa.degree()==0
off=18*aa*bb*cc*dd-4*bb**3*dd+bb**2*cc**2-4*aa*cc**3-27*aa**2*dd**2
print('degrees: symmetric',sym.degree(),'off-axis',off.degree(),flush=True)
dstar=(2*g**4+10*g**3+21*g*g+19*g+13)/(4*(1+g)**5)
def evalp(P,t):return sum((c*t**e[0] for e,c in P.to_dict().items()),K.zero)
def deflate(P):
 count=0;linear=D-R(dstar)
 while P and not evalp(P,dstar):
  P,rem=P.div(linear);assert not rem;count+=1
 return count,P
ms,sr=deflate(sym);mo,orr=deflate(off)
print('Dstar multiplicities',ms,mo,flush=True)
result={'field':'QQ(g)[D],g^4=2','method':'Exact4x4 Jacobian norm for the symmetric branch, exact univariate cubic discriminant for off-axis branch',
 'Jacobian_multiplication_relations_verified':True,'symmetric_branch_degree':sym.degree(),'off_axis_degree':off.degree(),
 'symmetric_Dstar_multiplicity':ms,'off_axis_Dstar_multiplicity':mo,'symmetric_norm':ser(sym),'off_axis_discriminant':ser(off),
 'symmetric_deflated':ser(sr),'off_axis_deflated':ser(orr),
 'scope':'All CENTER singular values are roots of the two polynomials; not an all-bad-D classification without local noncommutative order conditions.'}
def mono(P):return P.monic() if P else P
def sf(P):
 P=mono(P);c=P.gcd(P.diff(D));w=P.exquo(c);out=[];j=1
 while w.degree()>0:
  y=w.gcd(c);f=w.exquo(y)
  if f.degree()>0:out.append((j,mono(f)))
  w=y;c=c.exquo(y);j+=1
 return out
common=mono(sym).gcd(mono(off));print('common degree',common.degree(),flush=True)
sfs=sf(sym);sfo=sf(off)
print('symmetric squarefree degrees',[(i,p.degree()) for i,p in sfs],flush=True)
print('off squarefree degrees',[(i,p.degree()) for i,p in sfo],flush=True)

assert common==(D-R(dstar))**2
result["common_monic"]=ser(common)
result["symmetric_squarefree"]=[{"multiplicity":i,"factor":ser(p)} for i,p in sfs]
result["off_axis_squarefree"]=[{"multiplicity":i,"factor":ser(p)} for i,p in sfo]
result["distinct_center_singular_values"]=sum(p.degree() for _,p in sfs+sfo)-1
assert result["distinct_center_singular_values"]==13
(Path(__file__).parent/'cubic_order4_center_critical_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('CENTER CRITICAL POLYNOMIALS VERIFIED',flush=True)
