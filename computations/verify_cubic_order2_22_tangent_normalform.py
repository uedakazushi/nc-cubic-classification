"""Universal Schur and pencil-stabilizer identities for the full-rank tangent chart."""
import json
from pathlib import Path
import sympy as S
A,B,C,D,a,b,c,d=S.symbols('A B C D a b c d')
P=S.Matrix([[0,A,-A,B],[A,C,-B,D],[-A,-B,-C,-D],[B,D,-D,0]])
K=S.Matrix([[-b,d,a,-c],[a,-c,0,0],[-d,0,c,0],[c,0,0,0]])
assert S.expand(K.det()+c**4)==0
Q=K.T*P.adjugate()*K
X=-C*c+D*(a-d)
conditions=[Q[0,1]-Q[0,2],Q[1,3]-Q[2,3],Q[1,1]-Q[2,2],Q[0,3]-Q[1,2]]
expected=[B*X*(-2*A*c+B*(a+d)+C*(a-d)+2*D*b),2*B*D*c*X,
 -2*B*(B*c+D*(a+d))*X,
 -B*(-4*A*D*c*c+2*B*B*c*c+C*C*c*c+2*D*D*(a*d-b*c))]
assert all(S.expand(p-q)==0 for p,q in zip(conditions,expected))
g=S.Matrix([[a,b],[c,d]]);pp=d/c;qq=-a/c;rr=1/c
E=S.Matrix([[1,pp],[0,rr]]);F=S.Matrix([[1,qq],[0,rr]])
normalized=(F*g*E.inv()).applyfunc(S.cancel)
assert normalized[0,0]==normalized[1,1]==0 and normalized[1,0]==1
assert S.cancel(normalized[0,1]+(a*d-b*c))==0
# det(g)=1 yields normalized [[0,-1],[1,0]].
AA=(1+D*D)/(2*D)
PP=P.subs({A:AA,B:1,C:0})
assert S.cancel(PP.det()+1+2*D*D)==0
out={'status':'PASS','scope':'semisimple (2,2), odd rank2, tangent graph, invertible even cross block only',
 'exact_checks':['det(K)=-c^4','four universal cyclic Schur equations','independent upper-triangular pencil stabilizers normalize g to [[0,-1],[1,0]]','D nonzero and det(P)=-(1+2D^2)'],
 'normalizer_status':'not settled by this verifier; no all-parameter exclusion asserted',
 'not_claimed':['AS4 existence','H3 admissibility','tangent c=0 boundary','secant chart']}
Path(__file__).with_name('cubic_order2_22_tangent_normalform_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS full-rank tangent one-parameter necessary normal form')
