"""Reverse tangent minus: opposite normalization and odd determinant centralizer obstruction."""
import itertools,json
from pathlib import Path
import sympy as S
T=S.symbols('T',nonzero=True);z=S.symbols('z:6');A=S.zeros(4)
for (i,j),c in zip(itertools.combinations(range(4),2),z):A[i,j]=c;A[j,i]=-c
J=S.Matrix([[0,1],[-1,0]]);H=S.Matrix([[0,1],[1,0]]);b1=S.diag(1,0);flip=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
M=-(S.kronecker_product(J.T,b1)+S.kronecker_product(H.T,H))*flip
values=[0,(T+1/T)/2,T,-1/T,0,0];rewrite=(-M.inv()*A).subs(dict(zip(z,values)))
c=(T-1/T)/2
expected=S.Matrix([[-T,0,0,0],[0,0,-1/T,0],[c,1/T,0,0],[0,0,c,T]])
assert (rewrite-expected).applyfunc(S.cancel)==S.zeros(4)
f=S.Matrix([[-T,c],[0,1/T]]);g=S.Matrix([[-1/T,c],[0,T]])
assert (f*g-S.eye(2)).applyfunc(S.cancel)==S.zeros(2)
assert f.det()==g.det()==-1
# a=xy=-(u2+uv+vu)/2, b=yx=-(u2-uv-vu)/2.
# Quadratic substitution in the FREE negative tensor space, not just its symmetric quotient.
def tensor_action(F):return S.kronecker_product(F,F)
aa=S.Matrix([-S.Rational(1,2),-S.Rational(1,2),-S.Rational(1,2),0]);bb=S.Matrix([-S.Rational(1,2),S.Rational(1,2),S.Rational(1,2),0])
assert (tensor_action(f)*aa-bb).applyfunc(S.cancel)==S.zeros(4,1)
assert (tensor_action(g)*bb-aa).applyfunc(S.cancel)==S.zeros(4,1)
# For every invertible 2x2 matrix, Sym2(F)=I implies F=+/-I; in particular determinant +1.
a,b,c0,d=S.symbols('a b c d');F=S.Matrix([[a,b],[c0,d]])
Sf=S.Matrix([[a*a,a*b,b*b],[2*a*c0,a*d+b*c0,2*b*d],[c0*c0,c0*d,d*d]])
# A polynomial ideal certificate with determinant -1 has no Sym2-fixed-all solution.
assert list(S.groebner(list(Sf-S.eye(3))+[a*d-b*c0+1],a,b,c0,d))==[1]
out={'status':'PASS','scope':'entire reverse tangent nondegenerate positive-top minus-Pfaffian stratum, all nonzero T', 'exact_graph_dictionary':True,'normalizers':{'f':[str(v) for v in f],'g':[str(v) for v in g],'fg':'I','determinants':[-1,-1]},'quadratic_products':['xy=-(u2+uv+vu)/2','yx=-(u2-uv-vu)/2'],'free_tensor_identities':['f(xy quadratic)=yx quadratic','g(yx quadratic)=xy quadratic'],'central_negative_quadratics':['u2','uv+vu','v2'],'odd_auxiliary_degree_obstruction':'every odd power of f has determinant -1, so cannot fix all Sym2(V); quadratic negative tensors embed, and domain forces each odd-degree normal component zero','conclusion':'no normal positive cubic, hence no H3 on this whole stratum','not_claimed':['reverse plus-Pfaffian stratum','reverse square rank2-cross boundary','other negative rank2 types','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_tangent_reverse_minus_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS reverse tangent minus: universal graph/normalizer identities and exact Sym2 determinant-minus-one obstruction')
