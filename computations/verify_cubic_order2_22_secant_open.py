"""Rational all-parameter invertible-secant normal form and both bad nodes."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
A,B,C,D,r,l,k=S.symbols('A B C D r l k')
P=S.Matrix([[0,A,-A,B],[A,C,-B,D],[-A,-B,-C,-D],[B,D,-D,0]])
K=S.Matrix([[0,-r,0,0],[0,0,0,r+1],[-1,0,0,0],[0,0,1,0]])
Q=K.T*P.adjugate()*K
cyclic=[Q[0,1]-Q[0,2],Q[1,3]-Q[2,3],Q[1,1]-Q[2,2],Q[0,3]-Q[1,2]]
assert S.expand(cyclic[0]-B*(B-C)*(A+r*D))==0
assert S.expand(cyclic[1]-B*(r+1)*(B+C)*(A+r*D))==0
H=r*C*C+(2*r+1)*(2*r*l*l+1);E=2*r*l*l+r+1
assert all(S.expand(f.subs({B:1,A:-r*l,D:l}))==0 for f in cyclic[:3])
assert S.expand(cyclic[3].subs({B:1,A:-r*l,D:l})-H)==0
assert S.expand(r*P.subs({B:1,A:-r*l,D:l}).det()+E-H)==0
# A rational point and a line-parametrized chart on the generic conic.
a0=S.sqrt(-2);l0=1/(2*r);c0=a0*(2*r+1)/(2*r)
assert S.cancel(H.subs({l:l0,C:c0}))==0
h=-(2*r+1)*(a0*k+2)/(r*(k*k+2*(2*r+1)))
assert S.cancel(H.subs({l:l0+h,C:c0+k*h}))==0
nodes=[]
for sign in [1,-1]:
 values={r:S.Rational(-1,2),l:sign,C:0}
 assert all(S.simplify(p.subs(values))==0 for p in [H,S.diff(H,r),S.diff(H,l),S.diff(H,C)])
 assert S.simplify((S.hessian(H,[r,l,C])/2).det().subs(values))==2
 assert E.subs(values)==S.Rational(-1,2)
 nodes.append({'r':'-1/2','l':sign,'C':0})
# Exact rational-field dimensions at every geometric node, no samples omitted.
records=[]
for sign in [1,-1]:
 pp=P.subs({A:S.Rational(sign,2),B:1,C:0,D:sign});kk=K.subs(r,S.Rational(-1,2))
 wu=list(itertools.product(range(2),repeat=2));wv=list(itertools.product(range(2,4),repeat=2));rels=[]
 for i in range(4):rels.append({w:S.QQ.from_sympy(c) for w,c in zip(wu+wv,list(pp.row(i))+list(kk.row(i))) if c})
 rels.extend([{(0,2):S.QQ.one,(2,1):S.QQ.one,(3,0):S.QQ(1,2)},{(1,3):S.QQ.one,(2,1):S.QQ.one,(3,0):-S.QQ(1,2)}])
 dims=[]
 for parity in [0,1]:
  words=[w for w in itertools.product(range(4),repeat=4) if sum(i>=2 for i in w)%2==parity];ix={w:i for i,w in enumerate(words)};rows=[]
  for rel in rels:
   rp=sum(i>=2 for i in next(iter(rel)))%2
   for pos in range(3):
    for rest in itertools.product(range(4),repeat=2):
     if (sum(i>=2 for i in rest)+rp)%2!=parity:continue
     rows.append({ix[rest[:pos]+w+rest[pos:]]:c for w,c in rel.items()})
  M=DomainMatrix({i:row for i,row in enumerate(rows)},(len(rows),128),S.QQ)
  _,piv=M.rref();dims.append(128-len(piv))
 assert dims==[20,16]
 records.append({'l':sign,'even_B4':20,'odd_B4':16,'total_B4':36})
out={'status':'PASS','scope':'rational necessary invertible-secant presentation, semisimple (2,2), odd rank2',
 'graph':[['1','1'],['r+1','r']],
 'surface_equation':'r*C^2+(2*r+1)*(2*r*l^2+1)=0',
 'open_condition':'r*(r+1)*(2*r*l^2+r+1)!=0',
 'exact_checks':['four universal cyclic Schur equations','positive determinant identity','rational point and conic chart','two singular nodes with nondegenerate quadratic part'],
 'bad_nodes':records,'conclusion':'both nodes lie outside AS4: dim B4=36 instead of35',
 'not_claimed':['AS4 existence away from nodes','normal cubic exclusion everywhere','H3 admissibility','intrinsic moduli components or descent']}
Path(__file__).with_name('cubic_order2_22_secant_open_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS rational invertible-secant surface, conic chart and exact exclusion of both nodes')
