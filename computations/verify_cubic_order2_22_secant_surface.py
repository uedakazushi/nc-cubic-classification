"""Exact all-parameter rank2 secant exclusion, with polynomial specialization witnesses."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.agca.extensions import MonogenicFiniteExtension
r,l,c=S.symbols('r l c');R=S.QQ.poly_ring(r,l,c);rr,ll,cc=R.gens
H=rr*cc**2+(2*rr+1)*(2*rr*ll**2+1)
data=json.loads(Path(__file__).with_name('cubic_order2_22_secant_surface_input.json').read_text())
assert data['generator_order']==['x','y','u','v'] and len(data['functionals'])==7
funcs=[{int(j):R.ring.from_dict({tuple(m):S.QQ(a) for m,a in co}) for j,co in f.items()} for f in data['functionals']]
w4=[w for w in itertools.product(range(4),repeat=4) if sum(i>=2 for i in w)%2==0];ix={w:i for i,w in enumerate(w4)}
w3=[w for w in itertools.product(range(4),repeat=3) if sum(i>=2 for i in w)%2==0]
P=[[0,-rr*ll,rr*ll,R.one],[-rr*ll,cc,-R.one,ll],[rr*ll,-R.one,-cc,-ll],[R.one,ll,-ll,0]]
K=[[0,-rr,0,0],[0,0,0,rr+1],[-R.one,0,0,0],[0,0,R.one,0]]
wu=list(itertools.product(range(2),repeat=2));wv=list(itertools.product(range(2,4),repeat=2));rels=[]
for i in range(4):rels.append({w:R(a) for w,a in zip(wu+wv,P[i]+K[i]) if a})
rels.extend([{(0,2):R.one,(2,1):R.one,(3,0):rr+1},{(1,3):R.one,(2,1):R.one,(3,0):rr}])
checks=0
for rel in rels:
 for pos in range(3):
  for rest in itertools.product(range(4),repeat=2):
   if (sum(i>=2 for i in rest)+sum(i>=2 for i in next(iter(rel))))%2:continue
   row={ix[rest[:pos]+w+rest[pos:]]:a for w,a in rel.items()}
   for f in funcs:
    p=sum((a*f.get(j,R.zero) for j,a in row.items()),R.zero)
    assert all(m[2]<=2 for m in p)
    coefficient=R.ring.from_dict({(m[0],m[1],0):a for m,a in p.items() if m[2]==2})
    assert rr*p-coefficient*H==R.zero
    checks+=1
assert checks==1008
rows=[]
for f in funcs:
 for g in range(2):rows.append({j:f.get(ix[w+(g,)],R.zero)-f.get(ix[(g,)+w],R.zero) for j,w in enumerate(w3)})
witness=data['rank_minor'];assert len(witness['rows'])==len(witness['columns'])==10
mat=[[rows[i][j] for j in witness['columns']] for i in witness['rows']]
# These are exact polynomial divisions; all factors are retained in the determinant.
content=R.one
for i in range(10):
 d=R.zero
 for p in mat[i]:d=d.gcd(p)
 assert d
 content*=d;mat[i]=[p//d for p in mat[i]]
for j in range(10):
 d=R.zero
 for i in range(10):d=d.gcd(mat[i][j])
 assert d
 content*=d
 for i in range(10):mat[i][j]=mat[i][j]//d
# Compute determinant in the function field of the irreducible necessary surface.
# Extension.exquo does polynomial division in c, so use explicit field / in Bareiss.
KK=S.QQ.frac_field(r,l)
F=MonogenicFiniteExtension(S.Poly(c*c+(2*r+1)*(2*r*l*l+1)/r,c,domain=KK))
mat=[[F.convert(R.to_sympy(p)) for p in row] for row in mat]
previous=F.one;sign=1
for k in range(9):
 if not mat[k][k]:
  i=next(i for i in range(k+1,10) if mat[i][k]);mat[k],mat[i]=mat[i],mat[k];sign=-sign
 pivot=mat[k][k]
 for i in range(k+1,10):
  for j in range(k+1,10):mat[i][j]=(pivot*mat[i][j]-mat[i][k]*mat[k][j])/previous
  mat[i][k]=F.zero
 previous=pivot
determinant=sign*mat[9][9]*F.convert(R.to_sympy(content))
expected=-2*l**15*r**20*(r+1)**15*(2*r+1)**2
assert determinant==F.convert(expected)
out={'status':'PASS','scope':'entire invertible secant necessary surface on r*(r+1)*l*(2*r+1)!=0',
 'polynomial_functionals':7,'quartic_annihilator_identities':checks,'constraint_shape':[14,32],
 'minor_size':[10,10],'determinant_mod_surface':str(expected),
 'conclusion':'positive cubic centralizer of x,y is zero at every actual AS4 point of this open; l=0 and r=-1/2 separately excluded, hence the entire secant sector is H3-empty',
 'not_claimed':['AS4 nonexistence','all H3 classification','mixed rank4 exclusion','family classification']}
Path(__file__).with_name('cubic_order2_22_secant_surface_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS whole secant surface: 1008 polynomial identities and one exact rank10 minor')
