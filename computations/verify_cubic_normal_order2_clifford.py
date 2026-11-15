"""Exact nonsplit non-CY normal-boundary witness and cocycle identities."""
import sympy as s,json
from pathlib import Path
from itertools import product
rels=[{(1,2):1,(2,0):1,(0,1):-1,():1},{(2,1):1,(0,2):1,(1,0):-1,():1},{(0,0):1,(1,1):1,(2,2):-1,():1}]
ws=[w for d in range(5) for w in product(range(3),repeat=d)];ix={w:i for i,w in enumerate(ws)};cols=[]
for d in range(3):
 for l in range(d+1):
  for left in product(range(3),repeat=l):
   for right in product(range(3),repeat=d-l):
    for r in rels:cols.append({ix[left+w+right]:c for w,c in r.items()})
M=s.SparseMatrix(len(ws),len(cols),{(i,j):c for j,col in enumerate(cols) for i,c in col.items()});rank=M.rank();assert rank==86
F={(0,0,2):1,(0,2,1):-1,(1,2,0):1,(1,1,2):-1,(2,1,1):1,(2,0,0):-1}
for i,j in [(0,1),(1,0),(2,2)]:
 v=s.zeros(len(ws),1)
 for w,c in F.items():v[ix[w+(i,)]]+=c;v[ix[(j,)+w]]+=c
 assert M.row_join(v).rank()==rank

# B0 character CI is reduced, of length8, for h=b=c=1.
x,y,z=s.symbols('x y z');f=[2*y*z-x*x-1,2*z*x-y*y-1,2*x*y-z*z-1]
J=s.Matrix(f).jacobian([x,y,z]).det()
assert list(s.groebner(f+[J],x,y,z))==[1]
GB=s.groebner(f,x,y,z);lead=[p.LM(order=GB.order).exponents for p in GB.polys]
bounds=[]
for i in range(3):bounds.append(min(a[i] for a in lead if a[i]>0 and all(a[j]==0 for j in range(3) if i!=j)))
std=[a for a in product(*(range(b) for b in bounds)) if not any(all(a[i]>=b[i] for i in range(3)) for b in lead)]
assert len(std)==8
Gamma=list(product(range(2),repeat=3))
def coc(a,b):return (-1)**((a[0]*b[1]+a[2]*b[0])%2)
def plus(a,b):return tuple((a[i]+b[i])%2 for i in range(3))
for a,b,c in product(Gamma,repeat=3):assert coc(a,b)*coc(plus(a,b),c)==coc(b,c)*coc(a,plus(b,c))
g=(1,1,0)
for v,eigen in [((1,0,0),-1),((1,1,0),1),((0,0,1),-1)]:assert coc(g,v)*coc(v,g)==eigen
cert={'version':'classification-v34','example':'h=1,beta_x=beta_y=beta_z=1; Clifford involution x<->y','affine_quadratic_relation_rank_degree4':rank,'exact_Gstar_normal_identities':['Gstar*x=-y*Gstar','Gstar*y=-x*Gstar','Gstar*z=-z*Gstar'],'central_Clifford_character_CI_length':len(std),'Jacobian_unit_ideal':True,'finite_cocycle_identities':512,'volume_degree':'(active parity1, alpha parity1, t parity0)','scope':'Exact specified witness and finite bicharacter checks; all-parameter cocycle reduction and W1 exhaustion are ordinary proofs in cubic_normal_order2_clifford.tex'}
Path(__file__).with_name('cubic_normal_order2_clifford_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS non-CY Clifford involution witness, exact cubic normality, reduced length8 CI, all512 cocycle identities')
