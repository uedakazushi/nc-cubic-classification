#!/usr/bin/env python3
"""Exact character multiplicities and dimension constraints for inverse pencils.
Frobenius reciprocity and domain bounds are ordinary proofs in the paper.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json

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
result = {'status':'PASS','scope':'exact character counts and finite integer dimension constraints; ordinary Frobenius/domain proof separate',
          'quadratic_weight_dimensions':weights,'unit_repeated_relation_dimensions_s_r':unit_solutions,
          'nonunit_repeated_maximum_number_of_relations':nonunit_max,
          'possible_weight_collision_orders':collision_orders}
Path(__file__).with_name('cubic_inverse_spectral_pencils_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','nonunit_max_relations':nonunit_max,'unit_relation_dimensions':unit_solutions}))
