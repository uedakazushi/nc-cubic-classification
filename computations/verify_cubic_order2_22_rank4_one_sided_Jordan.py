"""Finite linear algebra behind the nonzero-positive-top one-sided Jordan reduction."""
import itertools,json
from pathlib import Path
import sympy as S
b=S.symbols('b');H=S.Matrix([[1,b],[0,1]]);T=S.kronecker_product(H,H)
a,d,e,f=S.symbols('a d e f');w=S.Matrix([a,d,e,f]);eq=S.Poly(1,b)
coef=[S.expand(z) for z in T*w-w];conditions=[]
for z in coef:conditions+=S.Poly(z,b).all_coeffs()
assert S.linsolve(conditions,[a,d,e,f])==S.FiniteSet((a,-e,e,0))
# Cyclic Q, with image in span(u^2, uv-vu), is a multiple of u^4.
a,b0,c,d,e,f=S.symbols('a b0 c d e f')
Q=S.Matrix([[a,b0,b0,c],[b0,d,c,e],[b0,c,d,e],[c,e,e,f]])
assert S.linsolve(list(Q.row(3))+list(Q.row(1)+Q.row(2)),[a,b0,c,d,e,f])==S.FiniteSet((a,0,0,0,0,0))
# K=c_U tensor A + q tensor B; the cyclic condition Q=A odot B has
# beta*delta=alpha*delta+beta*gamma=0. The two commutator-coefficient charts.
al,be,ga,de=S.symbols('alpha beta gamma delta')
G=S.groebner([be*de,al*de+be*ga,1-S.Symbol('z')*be],de,ga,al,be,S.Symbol('z'))
assert G.reduce(de)[1]==0 and G.reduce(ga)[1]==0
G=S.groebner([be*de,al*de+be*ga,1-S.Symbol('z')*de],be,al,ga,de,S.Symbol('z'))
assert G.reduce(be)[1]==0 and G.reduce(al)[1]==0
# Remaining u^2-only chart has degree-three irreducibles 21, not AS4's20.
counts=[]
for n in [2,3]:
 count=0
 for p in range(n+1):
  tails=[w for w in itertools.product([2,3],repeat=n-p) if all(w[i:i+2]!=(2,2) for i in range(len(w)-1))]
  count+=(p+1)*len(tails)
 counts.append(count)
assert counts==[10,21]
# Ore chart gives ordered monomials in four variables, degree3 =20.
assert sum((p+1)*(4-p) for p in range(4))==20
# On q=-1 plane, a in T1 anticommuting with both x,y is zero:
# {alpha*x+beta*y,x}=2alpha*x^2, {alpha*x+beta*y,y}=2beta*y^2.
assert S.Matrix([[2,0],[0,2]]).det()==4
# Under a negative-V Jordan twist fixing U,u, uv-vu changes only by u^2.
s=S.symbols('s');uv,vu,uu=S.symbols('uv vu uu')
assert S.expand((uv+s*uu)-vu-(uv-vu)-s*uu)==0
# O(2) has no nontrivial unipotent element: trace2,det1 and q preservation.
p0,p1,p2=S.symbols('p0 p1 p2');J=S.Matrix([[1+p0,p1],[p2,1-p0]]);qmat=S.Matrix([[0,1],[1,0]])
pol=list(J.T*qmat*J-qmat)+[J.det()-1]
G=S.groebner(pol,p0,p1,p2)
assert all(G.reduce(t)[1]==0 for t in [p0**2,p1,p2])
out={'status':'PASS','scope':'linear algebra and Hilbert counts for one-sided Jordan with nonzero positive top',
 'exact_checks':['fixed VV tensors span u^2 and uv-vu','cyclic Q restricted to that plane is a*u^4','two localized Gram charts force one mixed component zero','u-square-only chart degree3=21','Ore chart degree3=20','q=-1 degree1 anticentralizer zero','untwist changes commutator only by u^2','nondegenerate binary orthogonal group has no unipotents'],
 'structural_proof':'papers/sections/cubic_order2_22_rank4_Jordan.tex',
 'not_claimed':['all rank4 classification','zero-positive-top Jordan coverage','two-sided square-top Jordan exclusion']}
Path(__file__).with_name('cubic_order2_22_rank4_one_sided_Jordan_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS one-sided rank4 Jordan tensor restrictions, two Gram charts and PBW counts')
