#!/usr/bin/env python3
"""Independent Koszul-dual Frobenius audit of the non-CY Clifford witness."""
import sympy as s,json
from sympy.polys.matrices import DomainMatrix
from itertools import product
from pathlib import Path
w2=list(product(range(4),repeat=2));rels=[]
for i in [1,2,3]:rels.append({(0,i):1,(i,0):1})
rels +=[{(2,3):1,(3,1):1,(1,2):-1,(0,0):-1},{(3,2):1,(1,3):1,(2,1):-1,(0,0):-1},{(1,1):1,(2,2):1,(3,3):-1,(0,0):-1}]
R=s.Matrix([[r.get(w,0) for w in w2] for r in rels]);perp=R.nullspace();assert len(perp)==10
dual=[{w:v[i] for i,w in enumerate(w2) if v[i]} for v in perp]
def rows(n):
 ws=list(product(range(4),repeat=n));ix={w:i for i,w in enumerate(ws)};out=[]
 for dl in range(n-1):
  for l in product(range(4),repeat=dl):
   for r in product(range(4),repeat=n-2-dl):
    for rel in dual:out.append({ix[l+w+r]:c for w,c in rel.items()})
 M=s.MutableSparseMatrix(len(out),len(ws),{(i,j):c for i,row in enumerate(out) for j,c in row.items()})
 return ws,DomainMatrix.from_Matrix(M).convert_to(s.QQ)
w3,M3=rows(3);_,piv=M3.rref();free=[i for i in range(64) if i not in piv];assert len(free)==4
w4,M4=rows(4);top=M4.nullspace().to_Matrix();assert top.rows==1
phi={w:top[0,i] for i,w in enumerate(w4)};basis=[w3[i] for i in free]
L=s.Matrix([[phi[(i,)+w] for w in basis] for i in range(4)]);RR=s.Matrix([[phi[w+(i,)] for i in range(4)] for w in basis]);assert L.det()!=0 and RR.det()!=0
muE=(L*RR.T.inv()).T
alpha=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
assert muE==alpha
perm=[0,2,1,3]
assert all(phi[tuple(perm[i] for i in w)]==phi[w] for w in w4)
muB=-alpha;assert muB.det()==-1 and muB*muB==s.eye(4)
cert={'version':'classification-v39','parameters':'h=b=c=1, ordered generators t,x,y,z','quadratic_dual_dimensions':[1,4,6,4,1],'E3_basis':[list(w) for w in basis],'E4_socle_functional':[{'word':list(w),'coefficient':str(c)} for w,c in phi.items() if c],'left_pairing_determinant':str(L.det()),'right_pairing_determinant':str(RR.det()),'Nakayama_E':[[str(c) for c in muE.row(i)] for i in range(4)],'Nakayama_B':'-diag(1,swap_xy,1)','ordinary_determinant_B':-1,'top_action_alpha':1,'scope':'Independent exact degree2/3/4 Koszul-dual Frobenius audit. E5 zero and whole AS4 not re-proved by this calculation; all-degree AS4 follows from the separately proved finite cocycle/PBW construction.'}
Path(__file__).with_name('cubic_normal_order2_nakayama_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS independent Frobenius Nakayama: ordinary determinant -1, top action 1')
