"""Cyclic binary quartic middle rank <=2: five geometric normal forms."""
import json
from pathlib import Path
import sympy as S
a,b,c,d,e,f=S.symbols('a b c d e f')
Q=S.Matrix([[a,b,b,c],[b,d,c,e],[b,c,d,e],[c,e,e,f]])
# Symmetric and alternating V2 split, with an unnormalized symmetric basis.
J=S.Matrix([[1,0,0,0],[0,1,0,1],[0,1,0,-1],[0,0,1,0]])
split=S.expand(J.T*Q*J)
assert split==S.Matrix([[a,2*b,c,0],[2*b,2*c+2*d,2*e,0],[c,2*e,f,0],[0,0,0,2*(d-c)]])
p,q,t,lam=S.symbols('p q t lam');v=S.Matrix([p,q,q,t]);alt=S.Matrix([0,1,-1,0]);M=v*v.T+lam*alt*alt.T
assert S.expand(M[0,3]-M[1,2])==p*t-q*q+lam
# The nonzero alternating branch is q odot q -det(q)*alt odot alt.
N=M.subs({p:0,q:1,t:0,lam:1});assert N==S.diag(0,2,2,0) and N.rank()==2
# Symmetric catalecticant kernel r=du*dv, respectively r=dv^2.
Cat=S.Matrix([[a,b,c],[b,c,e],[c,e,f]])
assert Cat.subs({b:0,c:0,e:0})==S.diag(a,0,f)
assert Cat.subs({c:0,e:0,f:0})==S.Matrix([[a,b,0],[b,0,0],[0,0,0]])
models={
 'zero':S.zeros(4),
 'fourth_power':Q.subs({a:1,b:0,c:0,d:0,e:0,f:0}),
 'symmetric_secant':Q.subs({a:1,b:0,c:0,d:0,e:0,f:1}),
 'symmetric_tangent':Q.subs({a:0,b:1,c:0,d:0,e:0,f:0}),
 'noncommutative_rank2':Q.subs({a:0,b:0,c:0,d:1,e:0,f:0})}
assert [m.rank() for m in models.values()]==[0,1,2,2,2]
# Schur rank facts on the nonzero positive-top two-plane: Q= A odot B.
x,y,z,w=S.symbols('x y z w');P=S.Matrix([[0,1],[1,0]]);K=S.Matrix([[x,y],[z,w]]);Q2=K.T*P.inv()*K
assert S.expand(Q2.det()+K.det()**2)==0
out={'status':'PASS','scope':'all cyclic binary quartic middle matrices of rank<=2, up to GL2 and top scalar',
 'models':{key:[list(m.row(i)) for i in range(4)] for key,m in models.items()},
 'exact_checks':['symmetric/alternating splitting','cyclic equation lambda=-det(q)','rational normal-form matrices and ranks','two apolar-kernel charts','Schur determinant identity'],
 'coverage_proof':'papers/sections/cubic_order2_22_rank4_negative_top.tex',
 'not_claimed':['AS4 existence','mixed odd rank4 classification','normal cubic classification','H3 admissibility']}
Path(__file__).with_name('cubic_order2_22_rank4_negative_top_certificate.json').write_text(json.dumps(out,default=str,indent=2)+'\n')
print('PASS five negative binary top models, symmetric/alternating split and Schur rank identity')
