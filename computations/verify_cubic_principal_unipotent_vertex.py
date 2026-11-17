#!/usr/bin/env python3
"""Universal weighted-PBW/odd-Ext vertex controls, no parameter samples.
The Serre trace and tails-extension arguments are ordinary proofs in the paper.
"""
from pathlib import Path
import itertools,json,sympy as s
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_principal_unipotent_cover_certificate.json').read_text());assert D['status']=='PASS'
W=list(itertools.product(range(4),repeat=4));ix={w:i for i,w in enumerate(W)};B=s.zeros(256,12)
for k,record in enumerate(D['all12_cyclic_D_invariant_basis']):
 for w,c in record.items():B[ix[tuple(map(int,w))],k]=s.Rational(c)
a=s.symbols('a0:12');v=B*s.Matrix(a);alt=[]
for j,word in enumerate(W):
 if sum(word)>6:assert not v[j]
 if sum(word)==6:
  actual=v[j].subs(a[11],0)
  inv=sum(word[i]>word[k] for i in range(4) for k in range(i+1,4))
  expected=-(-1)**inv*a[9] if len(set(word))==4 else 0
  assert actual==expected
v=v.subs({a[11]:0,a[9]:1});H=s.Matrix(16,16,lambda i,j:v[ix[divmod(i,4)+divmod(j,4)]]);J=[1,2,3,6,7,11];L=[4,8,12,9,13,14];A=H.extract(L,J);assert A.det() in [1,-1];R=(H.extract(range(16),J)*A.inv()).applyfunc(s.expand);assert R.extract(L,range(6))==s.eye(6)
for col,inversion in enumerate(L):
 i,j=divmod(inversion,4);assert i>j and R[4*j+i,col]==-1
 for row in range(16):
  if row not in [inversion,4*j+i] and R[row,col]:assert sum(divmod(row,4))<i+j
N=s.zeros(4)
for j in range(1,4):N[j-1,j]=1
HH=s.eye(4)+N+N**2/2+N**3/6;HI=s.eye(4)-N+N**2/2-N**3/6;assert HH*HI==s.eye(4)
RB=s.zeros(16,6)
for i,j,k,col in itertools.product(range(4),range(4),range(4),range(6)):RB[4*i+k,col]+=R[4*i+j,col]*HI[k,j]
for col in [0,1,3]:assert all(not RB[4*i+j,col] for i,j in itertools.product(range(4),repeat=2) if i==3 or j==3)
RB=RB.applyfunc(s.expand)
AA=s.Matrix([[RB[12+k,col] for k in range(3)] for col in [2,4,5]]);BB=s.Matrix([[-RB[4*k+3,col] for k in range(3)] for col in [2,4,5]]);M=(AA.inv()*BB).applyfunc(s.expand)
assert AA.det()==BB.det()==M.det()==1
assert all(not M[i,j] for i in range(3) for j in range(i+1,3)) and all(M[i,i]==1 for i in range(3));assert (M-s.eye(3))**3==s.zeros(3)
# Classical associated-graded invariants in total degree3, with index weights.
exps=[e for e in itertools.product(range(4),repeat=4) if sum(e)==3];ee={e:i for i,e in enumerate(exps)};der=s.zeros(20)
for j,e in enumerate(exps):
 for k in range(1,4):
  if e[k]:f=list(e);f[k]-=1;f[k-1]+=1;der[ee[tuple(f)],j]+=e[k]
null=der.nullspace();assert len(null)==3
assert all(sum(j*e[j] for j in range(4))<=3 for col in null for i,e in enumerate(exps) if col[i])
# Every degree3 word of weight<=3 contains at least two J=(x0,x1,x2) letters.
assert all(sum(i!=3 for i in word)>=2 for word in itertools.product(range(4),repeat=3) if sum(word)<=3)
out={'status':'PASS','scope':'universal principal Jordan4 H3 vertex obstruction, conditional only on actual H3/AS hypotheses stated in paper','top_weight6':'minus a9 times alternating tensor after a11=0','source_minor_det':str(A.det()),'weighted_PBW_relations':[{''.join(map(str,divmod(i,4))):str(R[i,j]) for i in range(16) if R[i,j]} for j in range(6)],'extension_recurrence_A':s.sstr(AA),'extension_recurrence_B':s.sstr(BB),'extension_shift_monodromy':s.sstr(M),'monodromy_determinant':1,'classical_cubic_invariant_dimension':3,'max_invariant_index_weight':3,'ordinary_proof_inputs':['principal CY untwist and domain growth exclusions from preceding section','weighted PBW from AS4 Hilbert dimensions and quadratic overlaps','D-fixed normal cubic has index weight at most3, hence lies in J^2','tails point extensions have dimension3 from full recurrence, shift acts by M or its inverse','graded Serre trace gives nondegenerate b with b(v,w)=-b(Tw,v); odd dimension and detT1 impossible'],'not_claimed':['Serre proof mechanically formalized','all unipotent Jordan types classified','complete H3 classification','novelty confirmed']}
(ROOT/'cubic_principal_unipotent_vertex_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS universal principal vertex: Ext1 dimension3, shift unipotent determinant1')
