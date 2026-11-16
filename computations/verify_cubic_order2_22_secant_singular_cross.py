"""Whole singular symmetric-secant cross boundary, both parameters retained."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_tools import normal_free,polynomial_rows
b,c=S.symbols('b c');K=S.QQ.frac_field(b,c)
comm=S.Matrix([[0,1],[-1,0]]);h=S.Matrix([[0,1],[1,0]]);flip=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
M=-(S.kronecker_product(comm.T,S.diag(1,-1))+S.kronecker_product(h.T,S.eye(2)))*flip
A=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),[-c,-c,0,b,c,c]):A[i,j]=v;A[j,i]=-v
D=S.zeros(4)
for i,j,k,l in itertools.product(range(2),repeat=4):D[2*j+i,2*l+k]=A[2*i+l,2*k+j]
O=A.row_join(M).col_join((-M.T).row_join(D));C=O[:,[0,1,2,4]];rows=[0,1,2,4]
assert S.factor(C[rows,:].det())==4*c*c
T=C[rows,:].inv()*O[rows,:];assert (C*T-O).applyfunc(S.cancel)==S.zeros(8)
odd=[(i,j) for i in range(2) for j in range(2,4)]+[(i,j) for i in range(2,4) for j in range(2)]
R=[{(0,1):1,(1,0):-1,(2,2):1,(3,3):1},{(0,1):1,(1,0):1,(2,2):1,(3,3):-1}]+[{word:C[j,i] for j,word in enumerate(odd) if C[j,i]} for i in range(4)]
N,nf,dim=normal_free(R,K);assert dim==35
Q=polynomial_rows(N,c);entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_singular_cross_input.json').read_text());minor=DomainMatrix.from_Matrix(Q.extract(entry['rows'],entry['cols'])).convert_to(S.QQ.poly_ring(b,c)).det().as_expr()
assert S.factor(minor)==-32*c**5
original=[i for i in range(N.rows) if any(N[i,:])];used={original[i]%dim for i in entry['rows']}
for row in nf.values():
 for k in used:
  if k in row:
   den=S.Poly(S.denom(K.to_sympy(row[k])),b,c)
   assert len(den.terms())==1 and den.monoms()[0][0]==0
out={'status':'PASS','scope':'all rank2-cross symmetric secant boundary, rho=+/-1, A=(-c,-c,0,b,c,c), b arbitrary, c!=0','odd_relation_basis':'columns 0,1,2,4 of alternating top; basis minor4c2 and exact C*T=O over QQ[b,c,c^-1]','quartic_quotient_dimension':35,'selected_functional_poles':'only c=0','normal_rank10_minor':'-32*c5 after row denominator clearing','conclusion':'unit normal10minor annihilates all normal positive cubics modulo original cubic relations; AS4 positive B3 dimension10 implies no normal cubic. No H3 anywhere on this two-parameter boundary.','not_claimed':['AS4 sufficiency of atlas','nondegenerate positive secant full-cross plus','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_singular_cross_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS complete secant rank2 boundary: both parameters, original top image, Laurent-unit normal minor -32*c5')
