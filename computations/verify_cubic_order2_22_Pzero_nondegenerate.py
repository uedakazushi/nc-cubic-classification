"""Coverage identities for canonical P=0, nondegenerate positive quadratic projection."""
import itertools,json
from pathlib import Path
import sympy as S
q,c0,c1,c2,c3=S.symbols('q c0 c1 c2 c3');b=S.Matrix([0,1,-q,0]);c=S.Matrix([c0,c1,c2,c3]);Q=b*c.T+c*b.T
cyc=[Q[0,1]-Q[0,2],Q[1,3]-Q[2,3],Q[1,1]-Q[2,2],Q[0,3]-Q[1,2]]
for phase,target in [(q+1,[c1,c2]),(q*q+1,[c0,c3,c2-q*c1])]:
 assert list(S.groebner(cyc+[phase],c0,c1,c2,c3,q))==list(S.groebner(target+[phase],c0,c1,c2,c3,q))
# The pure quantum negative relation admits no nontrivial geometric unipotent.
a,b0,c0=S.symbols('a b0 c0');P=S.Matrix([[1+a,b0],[c0,1-a]]);M=S.Matrix([[0,1],[-q,0]])
for phase in [q+1,q*q+1]:
 G=S.groebner(list(P*M*P.T-M)+[a*a+b0*c0,phase],a,b0,c0,q)
 assert all(G.reduce(v)[1]==0 for v in [a*a,b0,c0])
# QQ epsilon- diagonal subchart, including the exact dictionary to (p,r,q).
p,r=S.symbols('p r',nonzero=True);z0,z2,z3,z5=S.symbols('z0 z2 z3 z5');pf=z0*z5+z2*z3
Tu=S.Matrix([[z3/p,z0/p],[-z5,z2]])
Tv=S.Matrix([[-z2/(p*q),z0/(p*q)],[-z5/q,-z3/q]])
F=-Tu.inv();G=-Tv.inv();sub={z0:0,z5:0,z2:q*r,z3:-p/r}
assert (F.subs(sub)-S.diag(r,-1/(q*r))).applyfunc(S.cancel)==S.zeros(2)
assert (G.subs(sub)-S.diag(p/r,-q*r/p)).applyfunc(S.cancel)==S.zeros(2)
# In the commutative positive plane, Pf=-q gives G=F^-1 and det(F)=-q^-1.
Tu=Tu.subs(p,1);Tv=Tv.subs(p,1)
assert (Tv*Tu+pf/q*S.eye(2)).applyfunc(S.expand)==S.zeros(2)
assert S.expand(Tu.det()-pf)==0
# Jordan positive projection: all epsilon- q!=1 graphs have these two matrices.
z,t=S.symbols('z t');F=S.Matrix([[-z/q,(t-z)/q],[0,-z/q]]);G=S.Matrix([[z,t+z],[0,z]])
assert (F*G+z*z/q*S.Matrix([[1,2],[0,1]])).applyfunc(S.expand)==S.zeros(2)
assert S.rem(S.fraction(S.cancel(F[0,0]**2+1/q))[0],z*z+q,z)==0
# q=-1 gives the shear-normalizing family; q^2=-1 gives primitive eighth weights.
for eps in [1,-1]:
 assert F.subs({q:-1,z:eps})==S.Matrix([[eps,eps-t],[0,eps]])
 assert G.subs({q:-1,z:eps})==S.Matrix([[eps,eps+t],[0,eps]])
# Rank2 cross lemma in canonical rank3 projection coordinates.
y=S.symbols('y:6');Omega=S.Matrix([[0,y[0],y[1],y[2]],[-y[0],0,y[3],y[4]],[-y[1],-y[3],0,y[5]],[-y[2],-y[4],-y[5],0]])
Pf=y[0]*y[5]-y[1]*y[4]+y[2]*y[3];cross=Omega[:3,1:]
assert S.expand(cross.det()-y[3]*Pf)==0
cross0=cross.subs(y[3],0)
assert (y[5]*cross0[:,0]-y[4]*cross0[:,1]-Pf.subs(y[3],0)*S.Matrix([1,0,0])).applyfunc(S.expand)==S.zeros(3,1)
# A rank1 positive quadratic projection makes every vector in im(M) a product.
u0,u1,v0,v1=S.symbols('u0 u1 v0 v1');h=S.Matrix(2,2,S.symbols('h:4'));aa=S.Matrix([u0,u1])*S.Matrix([[v0,v1]])
flip=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]);MM=-S.kronecker_product(aa.T,h)*flip
coef=S.Matrix(S.symbols('c:4'));vector=MM*coef
assert S.expand(S.Matrix(2,2,list(vector)).det())==0
out={'status':'PASS','scope':'the entire canonical P=0 mixed-rank4 sector; the positive quadratic projection is automatically nondegenerate for an AS4 domain',
 'checks':['both possible cyclic negative curvature spaces','geometric negative quantum unipotent rigidity','exact QQ diagonal dictionary','commutative positive full-matrix dictionary','Jordan positive full dictionary and shear/primitive8 alternatives','rank2 cross forces pure mixed line into cross image','rank1 positive projection cross image consists entirely of products'],
 'proof':'papers/sections/cubic_order2_22_Pzero_nondegenerate.tex',
 'dependencies':['zero_top_classification','filtered_normal_exclusion','curved_quantum_diagonal','curved_SL2','curved_Jordan_projection','curved_quarter','zero_top_QQ_plus and exceptional JQ normal minor'],
 'conclusion':'all H3 objects and geometric arrows in the entire canonical P=0 sector are the known fixed sign-envelope cuts; rank1 positive projection is excluded already by domain',
 'not_claimed':['P nonzero rank4 classification','global H3 classification','relative or nonreduced-base descent']}
Path(__file__).with_name('cubic_order2_22_Pzero_nondegenerate_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS P-zero nondegenerate coverage: cyclic tails, negative unipotents and all three graph dictionaries')
