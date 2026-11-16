"""Exact all-parameter identities excluding both rank-two secant boundary graphs."""
import itertools,json
from pathlib import Path
import sympy as S
A,B,C,D=S.symbols('A B C D')
aa,bb,cc,dd,ee,ff=S.symbols('aa bb cc dd ee ff')
P=S.Matrix([[0,A,-A,B],[A,C,-B,D],[-A,-B,-C,-D],[B,D,-D,0]])
# Pure-positive contractions in the diagonal graph.
M=P[[1,2],:];minors=[M[:,cols].det() for cols in itertools.combinations(range(4),2)]
G=S.groebner(minors,A,B,C,D)
for f in [A*B,A*C,D*B,D*C,B*B+C*C]:assert G.reduce(f)[1]==0
Q=S.Matrix([[aa,bb,bb,cc],[bb,dd,cc,ee],[bb,cc,dd,ee],[cc,ee,ee,ff]])
def schur(P,K,ids):
 H=P.row_join(K).col_join(K.T.row_join(Q));T=H.extract(ids,ids)
 E=(H-H[:,ids]*T.inv()*H[ids,:]).applyfunc(S.factor)
 return T,E
KD=S.Matrix([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0]])
T,E=schur(P.subs({B:0,C:0}),KD,[0,1,3,5])
assert S.expand(T.det()-D*D)==0
expected=[aa,cc,ff,bb*(A+D)/D,ee*(A+D)/D,(dd*(A*A+D*D)+2*A*D*cc)/(D*D)]
actual=list({x for x in E if x})
assert all(any(S.cancel(x-y)==0 for y in expected) for x in actual)
assert all(any(S.cancel(x-y)==0 for x in actual) for y in expected)
# Antidiagonal graph: pure xx,yy contractions force B=0.
assert P[[0,3],[0,3]].det()==-B*B
KA=S.Matrix([[0,0,0,0],[0,0,0,1],[-1,0,0,0],[0,0,0,0]])
T,E=schur(P.subs(B,0),KA,[0,1,2,4]);assert S.expand(T.det()-A*A)==0
Eqs,_=S.linear_eq_to_matrix(list(E),[aa,bb,cc,dd,ee,ff]);assert all(not x.free_symbols for x in Eqs)
assert Eqs.rank()==4 and all(x==0 for x in E.subs({cc:0,dd:0,ee:-bb,ff:-aa}))
# Free cubic row identities for the normal-quadratic obstructions.
words=list(itertools.product(range(4),repeat=3))
def add(*terms):
 out={}
 for scalar,poly in terms:
  for w,c in poly.items():out[w]=S.expand(out.get(w,0)+scalar*c)
 return {w:c for w,c in out.items() if c}
def mul(p,q):
 out={}
 for w,c in p.items():
  for v,b in q.items():out[w+v]=out.get(w+v,0)+c*b
 return out
x,y,u,v=[{(i,):S.Integer(1)} for i in range(4)]
def assert_membership(rels,tests,central_squares=False):
 rows=[]
 for rel in rels:
  for g in range(4):
   for side in [0,1]:rows.append([rel.get(w[1:] if side==0 else w[:-1],0) if w[0 if side==0 else -1]==g else 0 for w in words])
 if central_squares:
  for i,j in itertools.product(range(4),repeat=2):
   poly=add((1,{(i,i,j):1}),(-1,{(j,i,i):1}));rows.append([poly.get(w,0) for w in words])
 rr,piv=S.Matrix(rows).rref()
 for test in tests:
  row=S.Matrix([[test.get(w,0) for w in words]])
  for i,j in enumerate(piv):row-=row[j]*rr[i,:]
  assert row==S.zeros(1,64)
ND=mul(u,v)
rd=[add((1,mul(u,y)),(1,mul(x,u))),add((1,mul(v,x)),(-1,mul(y,v))),add((1,mul(u,v)),(1,mul(v,u)))]
assert_membership(rd,[add((1,mul(ND,g)),(1,mul(g,ND))) for g in [x,y,u,v]])
# The second diagonal branch uses square interchange and q^2=-1.
rd2=rd[:2]+[add((1,mul(u,v)),(1,mul(y,y))),add((1,mul(v,u)),(1,mul(x,x)))]
swap_tests=[]
for g in [u,v]:
 swap_tests.extend([add((1,mul(g,mul(x,x))),(-1,mul(mul(y,y),g))),add((1,mul(g,mul(y,y))),(-1,mul(mul(x,x),g)))])
assert_membership(rd2,swap_tests)
# In antidiagonal branch, order (p,q,R,S) has all squares central.
p,q,r,s=x,y,u,v
W=add((1,mul(s,p)),(-1,mul(p,s)));N=add((1,mul(s,q)),(-1,mul(q,s)))
ra=[add((1,mul(r,q)),(1,mul(q,r)),(-1,W)),add((1,mul(r,p)),(1,mul(p,r)),(-1,N))]
tests=[]
for poly,signs in [(W,[-1,1,1,-1]),(N,[1,-1,1,-1])]:
 for g,sg in zip([p,q,r,s],signs):tests.append(add((1,mul(poly,g)),(-sg,mul(g,poly))))
assert_membership(ra,tests,central_squares=True)
out={'status':'PASS','scope':'both rank-two even-cross-block secant boundary graphs, semisimple (2,2), odd relation rank2',
 'checks':['diagonal pure-U contraction ideal','diagonal first-branch universal Schur equations','antidiagonal universal Schur equations','diagonal normal uv and square-interchange identities','antidiagonal paired normal-quadratic covariance'],
 'structural_inputs':['domain forbids two independent pure binary quadrics','rank projection bounds','central-square recognition and domain cancellation'],
 'conclusion':'both rank2 secant boundary graphs have no H3 candidates; only rank3 and rank4 secant strata remain'}
Path(__file__).with_name('cubic_order2_22_secant_rank2_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS both rank-two secant boundary graphs: Schur and normal-element certificates')
