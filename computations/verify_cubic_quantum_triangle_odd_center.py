"""Exact commutative identities supporting the odd-order centre proof.
The PBW/difference argument in the paper supplies the all-N statement.
"""
import sympy as s,json
from pathlib import Path
q,v,w,a,p,t,X,Y,Z=s.symbols('q v w a p t X Y Z')
def C(n,x):
 c,d=s.Integer(2),x
 for i in range(1,n):c,d=d,s.expand(x*d-c)
 return c if n==0 else d
# Universal eliminated difference coordinates (nu^2=1, choose nu=1).
xx=a+1/a; yy=t+p/t; zz=a*t+p/(a*t)
assert s.cancel(zz**2-xx*yy*zz+yy**2+p*(xx**2-4))==0
checked=[]
for n in [3,5,7,9]:
 phi=s.cyclotomic_poly(n,q)
 def red(f):return s.rem(s.expand(f),phi,q).expand()
 # Orbit product for each numerator root, q^(2j) runs all roots.
 prod=s.Integer(1)
 for j in range(n):prod=red(prod*(q**(2*j)*v-w))
 assert red(prod-(v**n-w**n))==0
 # Endpoint factorization: all non-endpoint roots have multiplicity2.
 for sign in [1,-1]:
  P=s.Poly(C(n,w)-2*sign,w)
  gcd=s.gcd(P,P.diff());squarefree=P.exquo(gcd)
  assert gcd.degree()==(n-1)//2 and squarefree.degree()==(n+1)//2
  assert P.eval(2*sign)==0 and P.diff().eval(2*sign)!=0
 checked.append(n)
# n=3 normalization agrees exactly with the independently PBW-verified centre.
h=q*q-1;D=s.symbols('D');omega=-(q+1/q)-h**3*D/q**2
num,den=s.cancel(-(2+C(3,omega))/h**9-D**2*(D-(1-q)/3)).as_numer_denom()
assert s.rem(num,q*q+q+1,q)==0
# Fricke singular points and nondegenerate Hessians, all parameters.
alpha,beta=s.symbols('alpha beta');F=X*Y*Z+alpha*(X*X+Y*Y+Z*Z)+beta
H=s.hessian(F,(X,Y,Z))
assert H.det().subs({X:0,Y:0,Z:0})==8*alpha**3
assert s.expand(H.det().subs({X:-2*alpha,Y:-2*alpha,Z:-2*alpha}))==-32*alpha**3
cert={'version':'classification-v48','odd_orders_checked':checked,'orbit_product':True,'universal_elimination_identity':True,'root_three_normalization_matches_PBW':True,'Fricke_Hessians':[ '8 alpha^3','-32 alpha^3'],'scope':'Exact supporting identities and finite cyclotomic checks; all odd N centre and full-centre equality are ordinary proofs, not inferred from samples.','admissibility':'Only endpoint non-H3 obstruction proved here; interior singular fibres require full McKay multiplicities.'}
Path(__file__).with_name('cubic_quantum_triangle_odd_center_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS odd centre orbit/elimination, endpoint multiplicities, root-three normalization, Fricke Hessians')
