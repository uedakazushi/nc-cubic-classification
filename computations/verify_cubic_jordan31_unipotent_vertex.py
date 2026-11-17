#!/usr/bin/env python3
"""Universal original-top and odd-Ext controls for unipotent Jordan(3,1)."""
from pathlib import Path
import itertools,json,sympy as s
from cubic_diagonal_top import top_basis
ROOT=Path(__file__).resolve().parent
W=list(itertools.product(range(4),repeat=4));ix={w:i for i,w in enumerate(W)};cb=top_basis(s.QQ,[s.QQ.one]*4);C=s.zeros(256,66);DC=s.zeros(256,66);Nmap={1:0,2:1};weights=[0,1,2,0]
for j,b in enumerate(cb):
 for word,c in b.items():
  C[ix[word],j]=c
  for pos,l in enumerate(word):
   if l in Nmap:DC[ix[word[:pos]+(Nmap[l],)+word[pos+1:]],j]+=c
KK=s.Matrix.hstack(*DC.nullspace());B=C*KK;assert B.cols==18;rows=B.T.rref()[1];B=B*B.extract(rows,range(18)).inv();a=s.symbols('a0:18');v=B*s.Matrix(a);H=s.Matrix(16,16,lambda i,j:v[ix[divmod(i,4)+divmod(j,4)]])
assert [(i,H[i,10]) for i in range(16) if H[i,10]]==[(0,a[6])]
Hzero=H.subs({a[6]:0,a[12]:0});assert [(i,Hzero[i,6]) for i in range(16) if Hzero[i,6]]==[(0,a[4])]
Hzero=Hzero.subs(a[4],0);assert Hzero.extract([6,9,10],range(16))==s.zeros(3,16)
# With a12 normalized to1, every source relation has a unit pivot.
H=H.subs({a[6]:0,a[12]:1});J=[1,2,3,6,7,11];L=[4,8,12,9,13,14];A=H.extract(L,J);assert A.det()==-1;R=(H.extract(range(16),J)*A.inv()).applyfunc(s.expand);assert R.extract(L,range(6))==s.eye(6)
lead=s.zeros(16,6)
for col,inv in enumerate(L):
 i,j=divmod(inv,4);wt=weights[i]+weights[j]
 for row in range(16):
  if R[row,col]:assert weights[row//4]+weights[row%4]<=wt
  if weights[row//4]+weights[row%4]==wt:lead[row,col]=R[row,col]
expected=s.zeros(16,6)
for col,inv in enumerate(L):
 i,j=divmod(inv,4);expected[inv,col]=1;expected[4*j+i,col]=-1
expected[0,2]=-a[4];expected[1,4]=-a[4];expected[2,5]=3*a[4];expected[5,5]=-2*a[4];assert lead==expected
# Associated graded is k[x0,x1,x2][x3;delta], with N killing x3.
x=s.symbols('x0:4');delta=[a[4]*x[0]**2,a[4]*x[0]*x[1],-3*a[4]*x[0]*x[2]+2*a[4]*x[1]**2];D=lambda p:s.expand(x[0]*s.diff(p,x[1])+x[1]*s.diff(p,x[2]));de=lambda p:s.expand(sum(delta[j]*s.diff(p,x[j]) for j in range(3)))
assert all(s.expand(D(delta[j])-de(D(x[j])))==0 for j in range(3)) and s.expand(sum(s.diff(delta[j],x[j]) for j in range(3)))==0
# On PBW words base^e*x3^k, N acts just on the commutative base.
exps=[e for e in itertools.product(range(4),repeat=4) if sum(e)==3];ee={e:i for i,e in enumerate(exps)};dn=s.zeros(20)
for j,e in enumerate(exps):
 for k,l in Nmap.items():
  if e[k]:f=list(e);f[k]-=1;f[l]+=1;dn[ee[tuple(f)],j]+=e[k]
null=dn.nullspace();assert len(null)==6 and all(sum(weights[j]*e[j] for j in range(4))<=2 for col in null for i,e in enumerate(exps) if col[i])
assert all(sum(l!=2 for l in word)>=2 for word in itertools.product(range(4),repeat=3) if sum(weights[l] for l in word)<=2)
N=s.zeros(4);N[0,1]=N[1,2]=1;HI=s.eye(4)-N+N**2/2;RB=s.zeros(16,6)
for i,j,k,col in itertools.product(range(4),range(4),range(4),range(6)):RB[4*i+k,col]+=R[4*i+j,col]*HI[k,j]
RB=RB.applyfunc(s.expand);q=2;others=[0,1,3];pivotcols=[1,3,5]
for col in [0,2,4]:assert all(not RB[4*i+j,col] for i,j in itertools.product(range(4),repeat=2) if i==q or j==q)
AA=s.Matrix([[RB[4*q+k,c] for k in others] for c in pivotcols]);BB=s.Matrix([[-RB[4*k+q,c] for k in others] for c in pivotcols]);assert AA.det()==BB.det()==-1;M=(AA.inv()*BB).applyfunc(s.expand);assert M.det()==1 and (M-s.eye(3))**3==s.zeros(3)
out={'status':'PASS','scope':'entire unipotent Jordan(3,1) H3 sector empty via universal odd-Ext point, ordinary proof in paper','coordinate_words':[''.join(map(str,W[j])) for j in rows],'all18_basis':[{''.join(map(str,W[j])):str(c) for j,c in enumerate(B.col(k)) if c} for k in range(18)],'source_unit_minor':-1,'weighted_relations':[{''.join(map(str,divmod(i,4))):str(R[i,j]) for i in range(16) if R[i,j]} for j in range(6)],'associated_graded_Ore_delta':list(map(str,delta)),'associated_cubic_N_kernel_dimension':6,'maximum_invariant_weight':2,'point_generator':2,'point_Ext1_dimension':3,'extension_A':str(AA),'extension_B':str(BB),'shift_monodromy':str(M),'shift_determinant':1,'ordinary_dependencies':['standard CY unipotent untwist and normal cubic transport','domain/growth exclusions of a6 and a12zero','weighted PBW and filtered leading N kernel','all tails extensions recurrence and graded Serre determinant obstruction'],'not_claimed':['remaining Jordan(2,2)/(2,1,1) classified','complete H3 classification','novelty confirmed','Serre/tails proof mechanically formalized']}
(ROOT/'cubic_jordan31_unipotent_vertex_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS all18 original tops, weighted Ore limit, full point recurrence; Jordan(3,1) H3 empty')
