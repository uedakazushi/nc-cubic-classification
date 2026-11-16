"""Exact Schur and normal-quadratic certificates for the degenerate tangent boundary."""
import itertools,json
from pathlib import Path
import sympy as S
A,B,C,D,a,d=S.symbols('A B C D a d')
q=S.Matrix([[B,D,-D,0]])
r=S.Matrix([[A*(d-a),d*C-a*B,-d*B-a*C,D*(d-a)]])
assert S.expand(q.col_join(r).extract([0,1],[1,3]).det()-D**2*(d-a))==0
assert S.expand(q.col_join(r).subs(d,a).extract([0,1],[1,2]).det()+2*a*B*D)==0
# Nonzero yy contraction forces d=a, B=0; g then has a^2=1.
aa,bb,cc,dd,ee,ff=S.symbols('aa bb cc dd ee ff')
P=S.Matrix([[0,A,-A,0],[A,C,0,D],[-A,0,-C,-D],[0,D,-D,0]])
K=S.Matrix([[0,1,1,0],[1,0,0,0],[-1,0,0,0],[0,0,0,0]])
Q=S.Matrix([[aa,bb,bb,cc],[bb,dd,cc,ee],[bb,cc,dd,ee],[cc,ee,ee,ff]])
H=P.row_join(K).col_join(K.T.row_join(Q));ids=[3,1,0,5];T=H.extract(ids,ids)
assert S.expand(T.det()-D**2)==0
E=(H-H[:,ids]*T.inv()*H[ids,:]).applyfunc(S.cancel)
M,_=S.linear_eq_to_matrix(list(E),[aa,bb,cc,dd,ee,ff]);red,piv=M.rref()
assert piv==(0,2,3,5)
assert all(not x.free_symbols for x in M)
assert all(S.expand(x)==0 for x in E.subs({aa:0,cc:0,dd:0,ff:0}))
# Both epsilon signs: K changes sign by a block congruence, preserving rank.
words=list(itertools.product(range(4),repeat=3));index={w:i for i,w in enumerate(words)}
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
records=[]
for eps in [1,-1]:
 W=add((1,mul(y,u)),(eps,mul(u,y)))
 N=add((1,mul(y,v)),(-eps,mul(v,y)))
 # Only xy=yx, uv=-vu and xv-eps*vx+W=0 are needed once squares are central.
 rels=[add((1,mul(x,y)),(-1,mul(y,x))),add((1,mul(u,v)),(1,mul(v,u))),
       add((1,mul(x,v)),(-eps,mul(v,x)),(1,W))]
 rows=[]
 for rel in rels:
  for g in range(4):
   for side in [0,1]:rows.append([rel.get(w[1:] if side==0 else w[:-1],0) if w[0 if side==0 else -1]==g else 0 for w in words])
 for i,j in itertools.product(range(4),repeat=2):
  poly=add((1,{(i,i,j):1}),(-1,{(j,i,i):1}));rows.append([poly.get(w,0) for w in words])
 R=S.Matrix(rows);rr,pv=R.rref();free=[j for j in range(64) if j not in pv]
 for name,poly,signs in [('W',W,[-eps,eps,eps,-eps]),('N',N,[eps,-eps,eps,-eps])]:
  for g,sg in enumerate(signs):
   test=add((1,mul(poly,{(g,):1})),(-sg,mul({(g,):1},poly)))
   vector=S.Matrix([[test.get(w,0) for w in words]])
   for i,j in enumerate(pv):vector-=vector[j]*rr[i,:]
   assert vector==S.zeros(1,64)
 records.append({'epsilon':eps,'W_normalizer':[-eps,eps,eps,-eps],'N_normalizer':[eps,-eps,eps,-eps],'product_normalizer':[-1,-1,1,1]})
out={'status':'PASS','scope':'entire degenerate tangent boundary, semisimple (2,2), odd rank2',
 'checks':['boundary contraction minors','rank4 Schur equations force aa=cc=dd=ff=0','both-sign normal-quadratic covariance identities under central squares'],
 'normal_quadratics':records,
 'structural_steps':['D=0 branch forces extra independent quadratic relation after domain cancellation','D!=0 branch has central squares and two nonzero mu-odd normal quadratics','their product implements -mu and contradicts a designated normal cubic'],
 'conclusion':'whole tangent pencil has no H3 candidates, using the previous full-rank exclusion'}
Path(__file__).with_name('cubic_order2_22_tangent_boundary_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS entire tangent boundary: Schur and both-sign normal-quadratic certificates')
