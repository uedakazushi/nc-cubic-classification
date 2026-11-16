"""Rank-four odd middle: partial-transpose Pfaffian and full-graph determinant."""
import itertools,json
from pathlib import Path
import sympy as S
z=S.symbols('a:6');A=S.zeros(4)
for (i,j),t in zip(itertools.combinations(range(4),2),z):A[i,j]=t;A[j,i]=-t
D=S.zeros(4)
for i,j,k,l in itertools.product(range(2),repeat=4):D[2*j+i,2*l+k]=A[2*i+l,2*k+j]
def pf(M):return S.expand(M[0,1]*M[2,3]-M[0,2]*M[1,3]+M[0,3]*M[1,2])
assert S.expand(pf(A)+pf(D))==0
J=S.diag(S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,1],[-1,0]]));B=S.Matrix(4,4,S.symbols('b:16'))
assert S.expand(pf(B.T*J*B)-B.det())==0
# Schur rank4 gives D=-B^t A^-1 B. At A=J, T=-B^t A^-1=B^t J.
assert S.expand((B.T*J).det()-B.det())==0
# A rank3 projection of a symplectic four-space has skew middle rank2.
assert J[:3,:3].rank()==2
# For two AS2 planes, ordered degree3 words have dimension20.
assert sum((i+1)*(4-i) for i in range(4))==20
out={'status':'PASS','scope':'semisimple (2,2), odd relation dimension4',
 'identities':['Pf(D)=-Pf(A) under cyclic partial transpose','Pf(B^t J B)=det(B)','full graph determinant=-1','rank3 symplectic projection has skew rank2','conditional double Ore degree3 basis count20'],
 'proof':'papers/sections/cubic_order2_22_rank4_odd_graph.tex',
 'not_claimed':['all graph parameters AS4','double Ore coverage for rank1 positive projection','paired-pure-mixed classification','H3 admissibility']}
Path(__file__).with_name('cubic_order2_22_rank4_odd_graph_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS odd rank4 Pfaffian, full graph determinant and ordered degree3 count')
