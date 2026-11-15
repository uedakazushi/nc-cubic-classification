#!/usr/bin/env python3
"""Universal faithful-model identities in rational q-difference operators."""
import sympy as s,json
from pathlib import Path
rho,u,D=s.symbols('rho u D');q=rho*rho;kappa=-rho/(q*q-1)
bfun=(q*(u*u+1)*(u*u+q*q)+u*u*(q*q-1)**3*D)/((q*q-1)**2*(u*u-q*q)*(u*u-1))
def clean(f):return {n:s.cancel(c) for n,c in f.items() if s.cancel(c)!=0}
def add(f,g,c=1):
 out=dict(f)
 for n,a in g.items():out[n]=out.get(n,0)+c*a
 return clean(out)
def mul(f,g):
 out={}
 for n,a in f.items():
  for m,b in g.items():out[n+m]=out.get(n+m,0)+a*b.subs(u,q**n*u)
 return clean(out)
x={0:kappa*(u+1/u)};y={1:s.Integer(1),-1:bfun};z={1:rho*u,-1:rho*bfun/u};gens=[x,y,z]
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
 assert not add(add(mul(gens[j],gens[k]),mul(gens[k],gens[j]),-q),gens[i],-1)
O=mul(mul(x,y),z)
for i,c in [(0,1),(1,q*q),(2,1)]:O=add(O,mul(gens[i],gens[i]),c/(q*q-1))
assert not add(O,{0:D})
# Numerator collision values, not asserted as complete H3 criterion.
v=s.symbols('v');N=q*(v+1)*(v+q*q)+v*(q*q-1)**3*D
dplus=-q/((q-1)*(q+1)**3);dminus=-q/((q-1)**3*(q+1))
assert s.factor(s.discriminant(N,v)-(q*q-1)**6*(D-dplus)*(D-dminus))==0
# Quadratic matrix controlling left multiplication of x, over k[right-x].
r=s.symbols('r');M=s.Matrix([[q*r,-1/q],[1,r/q]])
assert s.cancel(M.det()-r*r-1/q)==0
# Odd variable swap with t -> -q*t identifies q and q^-1, and sends D -> -q^2 D.
a=1/(q*q-1);by=q*q/(q*q-1);ai=1/(q**-2-1);byi=q**-2/(q**-2-1)
assert s.cancel(-q*by-q*ai)==0
assert s.cancel(-q*a-q*byi)==0
assert s.cancel(-q*(1+a)-q*ai)==0
assert s.cancel(-q**-2*(-q*q*D)-D)==0
cert={'version':'classification-v47','base':'q=rho^2, q!=0,+-1','x':'kappa*(u+u^-1), kappa=-rho/(q^2-1)','y':'T+B(u)*T^-1','z':'rho*(u*T+u^-1*B(u)*T^-1)','B(u)':str(bfun),'difference_rule':'T*f(u)=f(q*u)*T','all_three_relations':True,'q_inversion_arrow':'(q,D)->(q^-1,-q^2 D), Omega->q*Omega_prime','Casimir':'Omega=-D','numerator_double_root_values':[str(dplus),str(dminus)],'H3_warning':'The two collision values are candidates only for general q; complete admissibility has been proved only on the primitive-three slice.','scope':'Universal rational operator identities. Faithfulness by PBW leading T coefficients/Chebyshev argument is an ordinary proof.'}
Path(__file__).with_name('cubic_quantum_triangle_difference_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS universal difference realization, exact Casimir level, two numerator collision values')
