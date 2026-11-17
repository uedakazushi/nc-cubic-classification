#!/usr/bin/env python3
"""Exact character multiplicities and dimension constraints for inverse pencils.
Frobenius reciprocity and domain bounds are ordinary proofs in the paper.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import sympy as S

characters = {'unit_repeated':[0,0,1,-1], 'nonunit_repeated':[1,1,0,-1]}
weights = {name:dict(sorted(Counter(a+b for a,b in product(v,repeat=2)).items()))
           for name,v in characters.items()}
assert weights['unit_repeated']=={-2:1,-1:4,0:6,1:4,2:1}
assert weights['nonunit_repeated']=={-2:1,-1:2,0:5,1:4,2:4}
unit_solutions = [(s,r) for s in range(4) for r in range(3) if s+2*r==6]
assert unit_solutions==[(2,2)]
nonunit_max = max(s+2*r for s in range(4) for r in range(2))
assert nonunit_max==5
# Distinct formal weights -2,-1,0,1,2 can coincide only at orders <=4.
collision_orders = sorted({abs(i-j) for i in range(-2,3) for j in range(-2,i)})
assert collision_orders==[1,2,3,4]
# Frobenius middle block with two invertible graph projections.
f=S.Matrix(2,2,S.symbols('f0:4'))
g=S.Matrix(2,2,S.symbols('g0:4'))
M=S.Matrix(2,2,S.symbols('m0:4'))
H=f.col_join(S.eye(2))*M*g.col_join(S.eye(2)).T
expected=[f.det()*M.det()*g.det(), f.det()*M.det(), M.det()*g.det(),M.det()]
actual=[H[i:i+2,j:j+2].det() for i,j in [(0,0),(0,2),(2,0),(2,2)]]
assert all(S.expand(a-b)==0 for a,b in zip(actual,expected))
assert sum((d+1)*(4-d) for d in range(4))==20
# Original quadratic normal forms test the linear inverse-Nakayama intertwiner.
p,kappa=S.symbols('p kappa',nonzero=True)
def product_linear(a,b,kind):
    # Standard basis x^2,xy,y^2.
    if kind=='quantum': return S.Matrix([a[0]*b[0],a[0]*b[1]+a[1]*b[0]/p,a[1]*b[1]])
    return S.Matrix([a[0]*b[0]+kappa*a[1]*b[0],a[0]*b[1]+a[1]*b[0],a[1]*b[1]])
intertwiner_minors={}
for kind,muinv in [('quantum',S.diag(1/p,p)),('Jordan',S.Matrix([[1,-2*kappa],[0,1]]))]:
    columns=[]
    for L in [S.Matrix([1,0]),S.Matrix([0,1])]:
        columns.append(S.Matrix.vstack(*[product_linear(L,S.eye(2)[:,j],kind)-product_linear(muinv[:,j],L,kind) for j in range(2)]))
    C=columns[0].row_join(columns[1])
    rows=(0,5) if kind=='quantum' else (0,3)
    det=S.factor(C[list(rows),:].det())
    assert S.simplify(det-(-(p-1)**2/p if kind=='quantum' else -kappa**2))==0
    intertwiner_minors[kind]=str(det)
t=S.symbols('t')
HS=1/((1-t)**2*(1-t**2))
assert S.cancel(HS*(1+t)/(1-t)-1/(1-t)**4)==0
HS_coeff=[S.expand(S.series(HS,t,0,8).removeO()).coeff(t,n) for n in range(8)]
assert HS_coeff==[1,2,4,6,9,12,16,20]
HA=S.cancel((1-t**3)*HS)
assert S.limit((1-t)**2*HA,t,1)==S.Rational(3,2)
HA_coeff=[int(S.expand(S.series(HA,t,0,14).removeO()).coeff(t,n)) for n in range(14)]
assert all(HA_coeff[2*m]==3*m+1 and HA_coeff[2*m+1]==3*m+2 for m in range(7))
result = {'status':'PASS','scope':'exact characters, graph determinants, original AS2 relations and rank2 Hilbert identities; ordinary proofs separate',
          'quadratic_weight_dimensions':weights,'unit_repeated_relation_dimensions_s_r':unit_solutions,
          'nonunit_repeated_maximum_number_of_relations':nonunit_max,
          'possible_weight_collision_orders':collision_orders,
          'four_graph_block_determinant_identities':'PASS',
          'AS2_Ore_standard_cubic_word_count':20,
          'linear_inverse_Nakayama_intertwiner_minors':intertwiner_minors,
          'rank2_base_Hilbert_coefficients_0_to_7':[int(x) for x in HS_coeff],
          'rank2_normal_cubic_quotient_coefficients_0_to_13':HA_coeff,
          'quotient_asymptotic_slope':'3/2',
          'ordinary_literature_input':'Stafford-Van den Bergh math/9910082v2 Theorem5.2 p14, explicitly Artin-Stafford Theorem0.2'}
Path(__file__).with_name('cubic_inverse_spectral_pencils_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','nonunit_max_relations':nonunit_max,'AS2_intertwiner_minors':intertwiner_minors,'rank2_cut_slope':'3/2'}))
