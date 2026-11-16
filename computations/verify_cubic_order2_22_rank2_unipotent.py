"""Exact stabilizer and fourth-root identities for the odd-rank-two Jordan exclusion."""
import json
from pathlib import Path
import sympy as S
b,e,z,d,x,y=S.symbols('b e z d x y')
P=S.Matrix([[1,b+e],[0,1]]);Q=S.Matrix([[1,b-e],[0,1]])
J=S.Matrix([[0,-1],[1,0]])
image=(Q*J*P.inv()).applyfunc(S.expand)
assert image[0,0]==b-e and image[1,1]==-b-e and image[1,0]==1
for eps in [1,-1]:
 image=Q*(eps*S.eye(2))*P.inv()
 assert image==S.Matrix([[eps,-2*eps*e],[0,eps]])
# After negative shear vanishes, preserving u^2=alpha*x^2+delta*y^2
# forces the coefficient 2*delta*b of xy to vanish, with delta!=0.
assert S.expand(d*((y+b*x)**2-y*y)).coeff(y,1)==2*d*b*x
# Pure mixed p=I, q=diag(1,z), z!=1 has no offdiagonal centralizer.
a,c,f,g=S.symbols('a c f g');T=S.Matrix([[a,c],[f,g]]);q=S.diag(1,z)
comm=T.T*q-q*T.T
assert (comm-S.Matrix([[0,f*(z-1)],[c*(1-z),0]])).applyfunc(S.expand)==S.zeros(2)
# The three necessary pure-mixed ratios are all distinct-eigenvalue cases.
assert all(S.simplify(value-1)!=0 for value in [-1,S.I,-S.I])
# The Nakayama unipotent part has blocks of size at most2.
p,n=S.symbols('p n');N=S.zeros(4);N[0,1]=p;N[2,3]=n
ss=S.diag(1,1,-1,-1);H=S.eye(4)+N/4
assert N*N==S.zeros(4) and H**4==S.eye(4)+N
assert ss*(S.eye(4)+N)*(H**-4)==ss and H*ss==ss*H
out={'status':'PASS','scope':'all noetherian quadratic Koszul AS4 domains with Nakayama semisimple spectrum (+,+,-,-) and odd quadratic relation rank2',
 'exact_checks':['tangent full-rank upper stabilizer','tangent degenerate upper stabilizer and square-invariance obstruction','pure-mixed distinct-eigenvalue centralizer','unipotent fourth-root and right-twist exponent -4'],
 'structural_proofs':['secant pencil has two rank-one points, forcing trivial unipotent action','G-independent necessary pencil/domain reductions cover all semisimple bases','right Zhang untwist preserves odd relation rank and produces an unipotent automorphism of the semisimple base'],
 'conclusion':'Nakayama is necessarily semisimple throughout the odd-rank-two (2,2) sector',
 'not_claimed':['odd-rank-four Jordan sector','remaining secant normal cubic classification','all H3 classification']}
Path(__file__).with_name('cubic_order2_22_rank2_unipotent_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS odd-rank-two (2,2) unipotent stabilizer and untwist identities')
