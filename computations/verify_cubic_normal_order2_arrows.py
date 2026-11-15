#!/usr/bin/env python3
"""Unit minor ruling out hidden movement of the unique elliptic boundary."""
import sympy as s,json
from itertools import product
from pathlib import Path
h,b,c=s.symbols('h b c');ws=list(product(range(4),repeat=2));ix={w:i for i,w in enumerate(ws)}
# t=0,x=1,y=2,z=3.
cols=[]
for i in [1,2,3]:cols.append({(0,i):1,(i,0):1})
cols +=[{(2,3):1,(3,1):1,(1,2):-h,(0,0):-b},{(3,2):1,(1,3):1,(2,1):-h,(0,0):-b},{(1,1):1,(2,2):1,(3,3):-h,(0,0):-c}, {(1,1):2,(2,2):-2}, {(3,1):1,(1,3):1,(3,2):-1,(2,3):-1}, {(0,0):1}]
M=s.Matrix([[col.get(w,0) for col in cols] for w in ws]);_,rows=M.subs({h:1,b:1,c:1}).T.rref();minor=s.factor(M[list(rows),:].det());assert minor==-4*h**2
# Cubic is the alternating tensor with alpha on the middle letter; alpha itself sends it to minus itself.
F={(1,1,3):1,(1,3,2):-1,(2,3,1):1,(2,2,3):-1,(3,2,2):1,(3,1,1):-1};alpha={1:2,2:1,3:3}
assert {tuple(alpha[i] for i in w):v for w,v in F.items()}=={w:-v for w,v in F.items()}
cert={'version':'classification-v37','quadratic_unit_minor':str(minor),'minor_rows':[list(ws[i]) for i in rows],'columns':'six B relations, {x+y,x-y}, {z,x-y}, t^2','scope':'All h,b,c over Z[1/(2h)]; independence holds over nonreduced bases. Scheme-level uniqueness and complete arrow proof use this minor plus the geometric elliptic boundary argument.'}
Path(__file__).with_name('cubic_normal_order2_arrows_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS universal unit minor',minor,'and alpha-odd cubic')
