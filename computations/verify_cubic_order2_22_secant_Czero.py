"""Entire C=0 nonresonant branch: a single exact polynomial minor."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
R=S.QQ.poly_ring('L');L=R.gens[0];one=R.one;zero=R.zero
data=json.loads(Path(__file__).with_name('cubic_order2_22_secant_Czero_input.json').read_text())
assert data['generator_order']==['x','y','u','v'] and len(data['functionals'])==19
funcs=[{int(j):R.ring.from_dict({(n,):S.QQ(c) for n,c in co}) for j,co in f.items()} for f in data['functionals']]
w3=[w for w in itertools.product(range(4),repeat=3) if sum(i>=2 for i in w)%2==0]
w4=[w for w in itertools.product(range(4),repeat=4) if sum(i>=2 for i in w)%2==0];ix={w:i for i,w in enumerate(w4)}
# All six relations multiplied by 2L^2, a unit on this branch.
rels=[
 {(0,1):L,(1,0):-L,(1,1):2*L*L,(2,3):one},
 {(0,0):L,(1,0):-2*L*L,(1,1):2*L**3,(3,3):2*L*L-one},
 {(0,0):-L,(0,1):-2*L*L,(1,1):-2*L**3,(2,2):-2*L*L},
 {(0,0):2*L*L,(0,1):2*L**3,(1,0):-2*L**3,(3,2):2*L*L},
 {(0,2):2*L*L,(2,1):2*L*L,(3,0):2*L*L-one},
 {(1,3):2*L*L,(2,1):2*L*L,(3,0):-one}]
checks=0
for rel in rels:
 for pos in range(3):
  for rest in itertools.product(range(4),repeat=2):
   if (sum(i>=2 for i in rest)+sum(i>=2 for i in next(iter(rel))))%2:continue
   row={ix[rest[:pos]+w+rest[pos:]]:c for w,c in rel.items()}
   for f in funcs:
    assert sum((c*f.get(j,zero) for j,c in row.items()),zero)==zero;checks+=1
assert checks==2736
rows={}
for i,f in enumerate(funcs):
 for g in range(2):
  row={}
  for j,w in enumerate(w3):
   c=f.get(ix[w+(g,)],zero)-f.get(ix[(g,)+w],zero)
   if c:row[j]=c
  rows[2*i+g]=row
M=DomainMatrix(rows,(38,32),R);witness=data['rank_minor']
assert len(witness['rows'])==len(witness['columns'])==10
p=M.extract(witness['rows'],witness['columns']).det()
assert p and p.monic()==L**16*(L*L-S.QQ(1,2))**4
out={'status':'PASS','scope':'entire branch C=0, rho=-1/(2*L^2) of the necessary secant surface',
 'polynomial_functionals':19,'quartic_annihilator_identities':checks,'normal_constraint_shape':[38,32],
 'minor_size':[10,10],'minor_degree':24,'monic_minor':'L^16*(L^2-1/2)^4',
 'open_condition':'L*(2*L^2-1)!=0','residual_values_in_domain':[],
 'conclusion':'no H3 on this whole branch; combined with the resonant-fiber theorem, no H3 anywhere with C=0',
 'not_claimed':['normal cubic classification off C=0','AS4 existence elsewhere','relative intrinsic family recognition']}
Path(__file__).with_name('cubic_order2_22_secant_Czero_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS entire C=0 branch: 2736 identities and one degree24 minor, no residual values')
