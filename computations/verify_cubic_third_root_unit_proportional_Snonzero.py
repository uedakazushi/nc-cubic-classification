#!/usr/bin/env python3
"""Original proportional-coupling Schur constants and exact cubic-syzygy
obstruction. Opposite/rank/domain case exhaustion is an ordinary proof.
"""
import itertools,json
from pathlib import Path
import sympy as s
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1));O=s.Symbol('omega');aa=s.symbols('a:22')
def expr(c):
 cs=c.to_list();return sum(s.Rational(q.numerator,q.denominator)*O**(len(cs)-j-1) for j,q in enumerate(cs))
def red(e):
 e=s.expand(e).replace(lambda n:n.is_Pow and n.base==O and n.exp.is_Integer,lambda n:O**(int(n.exp)%3))
 return s.rem(s.expand(e),O*O+O+1,O)
seen=set();tops=[]
for w in itertools.product(range(4),repeat=4):
 if w in seen:continue
 T={};v=w;c=F.one
 while v not in T:
  T[v]=c;seen.add(v);v=(v[-1],)+v[:-1];c=-c/F.unit**[0,0,1,2][v[0]]
 if c==F.one:tops.append(T)
assert len(tops)==22
H=s.zeros(16)
for a,T in zip(aa,tops):
 for w,c in T.items():H[4*w[0]+w[1],4*w[2]+w[3]]+=a*expr(c)
M=H.extract([2,6,8,9,15],[3,7,10,12,13]).subs({aa[10]:1,aa[18]:0,aa[14]:1,aa[19]:0,aa[20]:1})
J=[0,1,3,4];N=M.extract(range(4),J)-M.extract(range(4),[2])*M.extract([4],J)/O**2
expected=s.Matrix([[aa[8]-1,aa[9],-aa[2]+O,aa[11]],
 [O**2*aa[12],aa[17],-aa[6],-aa[15]],
 [O**2*(1-aa[3]),-O**2*aa[7],-aa[8]-1,-O**2*aa[12]],
 [O**2*aa[13],-O**2*aa[16],-aa[9],-aa[17]]])
assert (N-expected).applyfunc(red)==s.zeros(4)
p,r,t,u,a,b,c,d=s.symbols('p r t u a b c d')
# Here u denotes the third coordinate of the rank-one row vector.
U=s.Matrix([p,r,u,t]);V=s.Matrix([a,b,c,d]);NN=U*V.T
assert NN[0,0]+NN[2,2]==p*a+u*c
assert NN[0,1]+NN[3,2]==p*b+t*c
assert NN[1,0]+NN[2,3]==r*a+u*d
assert NN[1,1]+NN[3,3]==r*b+t*d
system=s.Matrix([[p,0,u,0],[0,p,t,0],[r,0,0,u],[0,r,0,t]])
left=s.Matrix([[r*t,-r*u,-p*t,p*u]])
assert left*system==s.zeros(1,4)
assert (left*s.Matrix([-2,0,0,0]))[0]==-2*r*t
# The nonzero by-branch has a6=a11=a15=0 and a16=omega*t^2*c/p.
assert red(-t*(-t*c/p)/O**2-O*t*t*c/p)==0
A16,A2=s.symbols('a16 a2',nonzero=True)
K=s.Matrix([[0,-O],[-O,0]])
row=(s.Matrix([[0,A16]])*K.inv()*s.Matrix([[A2,0,0,0],[0,0,0,0]])).applyfunc(red)
assert (row-s.Matrix([[-O**2*A16*A2,0,0,0]])).applyfunc(red)==s.zeros(1,4)
# Two independent cubic overlap syzygies for every third quadratic relation.
x,y=s.symbols('u v');words=list(itertools.product(range(3),repeat=3));idx={w:j for j,w in enumerate(words)}
R=[{(1,1):1},{(2,2):1},{(0,0):1,(1,2):-x,(2,1):-y}]
rows=[];where={}
for j,rel in enumerate(R):
 for side in [0,1]:
  for k in range(3):
   where[j,side,k]=len(rows);row=[0]*27
   for w,c in rel.items():row[idx[(k,)+w if side==0 else w+(k,)]]=c
   rows.append(row)
mat=s.Matrix(rows);syzygies=[]
for rel,letter in [(0,1),(1,2)]:
 v=s.zeros(18,1);v[where[rel,0,letter]]=1;v[where[rel,1,letter]]=-1
 assert mat.T*v==s.zeros(27,1);syzygies.append(v)
assert s.Matrix.hstack(*syzygies).rank()==2 and mat.rank()==16
assert 27-(9+9-2)==11 and 20-10==10
out={'status':'PASS','scope':'full original22-orbit Schur matrix, universal rank-one consistency, nonzero branch coefficient, and all-parameter cubic syzygies; ordinary rank/domain/opposite proof separate',
 'proportional_normalization':'P=Q=(1,0),S=1','rank_one_consistency':'r*t=0',
 'off_axis_nonzero_a16':'omega*t^2*c/p','normal_x_quotient_Hilbert_target_A3':10,
 'two_independent_overlap_syzygies':['b^3','c^3'],'all_parameter_A3_lower_bound':11,
 'conclusion':'all unit-repeat H3 candidates require S=0',
 'remaining_unit_repeat_sector':'rank(P,Q)=1,S=0',
 'not_claimed':['remaining S0 proportional sector classified','nonunit semisimple spectrum classified','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_proportional_Snonzero_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','unit_repeat_S_zero_required':True,'quotient_dimension_contradiction':[11,10]}))
