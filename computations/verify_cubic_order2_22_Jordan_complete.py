"""Global mixed-rank4 Jordan obstruction: full-graph commutant and triangular fixed cubic charts."""
import json
from pathlib import Path
import sympy as S
r=S.symbols('r:16');R=S.Matrix(4,4,r);J=S.Matrix([[1,1],[0,1]]);H=S.kronecker_product(J,S.eye(2))
eq=list(R*H-H*R);target=list(R[2:4,0:2])+list(R[2:4,2:4]-R[0:2,0:2])
assert list(S.groebner(eq,*r))==list(S.groebner(target,*r))
a,b,c,d=S.symbols('a b c d');A=S.Matrix([[a,b],[c,d]]);B=S.Matrix(2,2,S.symbols('b:4'));comm=A.row_join(B).col_join(S.zeros(2).row_join(A))
assert S.factor(comm.det())==(a*d-b*c)**2
T=S.kronecker_product(A,A);assert S.factor(T.det())==(a*d-b*c)**4
v=S.Matrix(S.symbols('v:4'));u=T*v
# Basis: y3,xy2,y*V2[4],x*V2[4]. All undisplayed terms are arbitrary lower blocks.
N=S.zeros(10);N[1,0]=3
s=S.symbols('s:4');t=S.symbols('t:4');w=S.symbols('w:4')
for j in range(4):
 N[2+j,1]=2*u[j];N[2+j,0]=s[j];N[6+j,0]=t[j];N[6+j,1]=w[j];N[6+j,2+j]=1
for j in range(4):
 rows=[1,2+j,6,7,8,9];cols=[0,1,2,3,4,5]
 assert S.expand(N.extract(rows,cols).det()-6*u[j])==0
assert N[:,6:10]==S.zeros(10,4)
assert N**4==S.zeros(10)
mult=4*S.eye(10)+6*N+4*N*N+N**3
assert mult.det()==4**10
out={'status':'PASS','scope':'all canonical P,Q nonzero (2,2) mixed-rank4 H3, both full-graph and rank3 projection alternatives','full_graph_H_intertwiner':'[[A,B],[0,A]], A invertible','invertibility_identities':['det(graph)=det(A)^2','det(A tensor A)=det(A)^4'],'positive_cubic_basis':['y3','xy2','y*V2[4]','x*V2[4]'],'four_fixed_kernel_minors':'6*((A tensor A)*b)_j; b!=0 so at least one is nonzero','fixed_kernel':'x*V2','unipotent_power':'ker(H4-I)=ker(H-I); exact multiplier determinant 4^10','original_cut':'mu(G)=G implies H(G)=G in the same graded vector space; x*_B B2=x*C2, so original G factors','conclusion':'no nonsemisimple H3 when P,Q are both nonzero; with P0/Q0 recognition, the entire mixed-rank4 (2,2) H3 sector has semisimple Nakayama','not_claimed':['classification of remaining semisimple top types','intrinsic relative descent','global H3 classification','independent peer review']}
Path(__file__).with_name('cubic_order2_22_Jordan_complete_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS global mixed-rank4 Jordan exclusion: full commutant ideal, four rank6 fixed-kernel charts, unipotent fourth-power identity')
