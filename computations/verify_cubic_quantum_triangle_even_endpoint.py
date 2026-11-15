"""All-order endpoint weight equations and sample normal half-Chebyshev matrices."""
import sympy as s,json
from pathlib import Path
q,J,K,r=s.symbols('q J K r');h=q*q-1
lam=lambda J:-(q*J+1/J)/h
A=lambda J:J-q/J
c=lambda J:q*q*(J*J+J**-2-2)/(h*h*A(J)*A(q*J))
Omega0=q/((q-1)**3*(q+1));l=lam(J);B=(q*q+1)/h
cp=l*J+B;cq=l/(q*J)+B
assert s.factor(A(J)*c(J)-A(q*q*J)*c(q*J)-l)==0
assert s.factor(cp*c(J)+cq*c(q*J)+l*l/h-Omega0)==0
expected=(-J*J+q)*(J*J*q-1)*(J*J*q**3-1)/(J**3*q*h)
assert s.factor(A(J)*cq+A(q*q*J)*cp-expected)==0
# Endpoint block: diagonal y^2 and adjacent product are uniquely determined.
a=lam(1);det=(1-q)*(a/q+B)+A(q*q)*(a+B)
assert s.factor(det-(q-1)**2*(q*q+q+1)/(q*(q+1)))==0
assert s.factor(-A(q*q)*c(q)-a)==0
assert s.factor((a/q+B)*c(q)+a*a/h-Omega0)==0
# All possible weight pairs: a path and the two endpoint loops.
E=(1+q*q)*lam(J)*lam(K)-q*(lam(J)**2+lam(K)**2)-1
assert s.factor(E-(-J+K*q)*(J*K-1)*(J*q-K)*(J*K*q*q-1)/(J*J*K*K*h*h))==0
# Independent exact finite-order checks of the half-Chebyshev normality.
checked=[]
for N in [4,6,8,10,12]:
 m=N//2;Mx=s.Matrix([[q*r,-1/q],[1,r/q]]);kappa2=q/h**2
 C,D=2*s.eye(2),Mx;cc,dd=s.Integer(2),r
 for j in range(1,m):C,D=D,(Mx*D-kappa2*C).applyfunc(s.cancel);cc,dd=dd,s.cancel(r*dd-kappa2*cc)
 for v in D+dd*s.eye(2):
  num,den=s.cancel(v).as_numer_denom();assert s.rem(num,s.cyclotomic_poly(N,q),q)==0
 checked.append(N)
cert={'version':'classification-v53','base':'all even N=2M>=4','half_Chebyshev_normality_samples':checked,'universal_weight_adjacency_factorization':True,'universal_interior_product_equations_and_nonzero_determinant':True,'universal_endpoint_unique_product_and_nilpotent_diagonal':True,'ordinary_proof':'Normal half-Chebyshev elements square to zero at D4 centre; they kill simple modules. x semisimple with M weights; adjacent products are invertible constants, so every simple dimension is a positive multiple of M. Full D4 would require rank>=6M, but rank degree is2M.','consequence':'Dminus is non-H3 at every even order. Together with prior results, all finite-order q!=+-1 cuts are H3 iff D!=Dplus,Dminus.','limits':'Nonroot q admissibility and global H3 classification remain open.'}
Path(__file__).with_name('cubic_quantum_triangle_even_endpoint_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS universal even endpoint weight equations, all determinants and half-Chebyshev checks')
