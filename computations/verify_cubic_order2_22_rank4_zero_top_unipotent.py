"""Zero-top odd symplectic block: both-side unipotents impossible; one-side forms."""
import itertools,json
from pathlib import Path
import sympy as S
J=S.Matrix([[1,1],[0,1]]);K=S.kronecker_product(J,J);z=S.symbols('z:6');A=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),z):A[i,j]=v;A[j,i]=-v
solution=list(S.linsolve(list(K*A*K.T-A),z));assert solution==[(z[0],z[1],0,0,0,0)]
pf=z[0]*z[5]-z[1]*z[4]+z[2]*z[3]
assert S.expand(pf.subs(dict(zip(z,solution[0])),simultaneous=True))==0
# A full mixed graph commuting with the one-sided shear is upper triangular
# in the two negative blocks, with equal diagonal 2x2 blocks.
v=S.symbols('l:16');L=S.Matrix(4,4,v);H=S.kronecker_product(J,S.eye(2))
sol=list(S.linsolve(list(H*L-L*H),v))[0]
F=S.Matrix([[sol[0],sol[1]],[sol[4],sol[5]]]);D=S.Matrix([[sol[2],sol[3]],[sol[6],sol[7]]]);expected=F.row_join(D).col_join(S.zeros(2).row_join(F))
assert S.Matrix(4,4,sol)==expected and S.expand(expected.det()-F.det()**2)==0
# Fixed pure negative quad and its nondegenerate commutator component.
a,b,c,d=S.symbols('a b c d');q=S.Matrix([a,b,c,d]);sol=list(S.linsolve(list(S.kronecker_product(J,J)*q-q),[a,b,c,d]))[0]
assert sol==(a,-c,c,0)
out={'status':'PASS','scope':'H3 with canonical semisimple untwist in the mixed-rank4 zero-positive/zero-negative-top sector',
 'checks':['both nontrivial unipotent sides force Pf(A)=0','one-sided mixed graph block form [[F,D],[0,F]]','det graph=det(F)^2 in that ordering','fixed negative quad span u^2 and uv-vu'],
 'proof':'papers/sections/cubic_order2_22_rank4_zero_top_unipotent.tex',
 'conclusion':'every H3 object in this canonical zero-top sector has semisimple Nakayama',
 'not_claimed':['all AS4 unipotents absent','other rank4 top types','all H3 classification','relative nonreduced-base statement']}
Path(__file__).with_name('cubic_order2_22_rank4_zero_top_unipotent_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS zero-top symplectic unipotent obstruction and one-sided graph/quad forms')
