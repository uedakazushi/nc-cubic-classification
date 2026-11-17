#!/usr/bin/env python3
"""Exact finite AS3 top-tensor orbits and literal final normalizer obstruction.
The Ore coverage and treatment of nonsemisimple sigma are ordinary proofs.
"""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
Q=S.Symbol('Q');K=S.QQ.alg_field_from_poly(S.Poly(Q**6+Q**3+1))
a=K.unit;zero=K.zero;one=K.one;omega=a**6;t=-a**2
assert a**3==omega**2 and omega**3==one and omega!=one
assert t**3==-omega and t!=omega**2
orbit_lists={}
for k in range(3):
    sig=[a,a*omega,-a*omega**k]
    fixed=[w for w in itertools.product(range(3),repeat=3) if sig[w[0]]*sig[w[1]]*sig[w[2]]==one]
    reps=sorted({min(w,(w[-1],)+w[:-1],w[1:]+w[:1]) for w in fixed})
    orbit_lists[k]=reps
assert orbit_lists=={0:[(0,0,1),(1,2,2)],1:[(0,0,1)],2:[(0,0,1),(0,2,2)]}
for k in range(3):
    sig=[a,a,-a*omega**k]
    fixed=[w for w in itertools.product(range(3),repeat=3) if sig[w[0]]*sig[w[1]]*sig[w[2]]==one]
    assert {w[1:] for w in fixed if w[0] in (0,1)}<={(2,2)}
# Original x,y,c top tensor, normalized to x^2=c^2.
w={(0,0,1):one,(0,1,0):a**7,(1,0,0):a**5,
   (1,2,2):-a**5,(2,1,2):-a**7,(2,2,1):-one}
sig=[a,a**7,-a];nu=[s*s for s in sig]
rot={}
for word,coefficient in w.items():
    assert sig[word[0]]*sig[word[1]]*sig[word[2]]==one
    rotated=(word[-1],)+word[:-1]
    rot[rotated]=rot.get(rotated,zero)+nu[word[-1]]*coefficient
assert rot==w
# u=x+c,v=x-c,y, with vu=-uv and y(u,v)=t(u,v)y.
rules={(1,0):{(0,1):-one},(2,0):{(0,2):t},(2,1):{(1,2):t}}
@lru_cache(None)
def nf(word):
    for j in range(len(word)-1):
        if word[j:j+2] not in rules:continue
        out={}
        for replacement,coefficient in rules[word[j:j+2]].items():
            for v,c in nf(word[:j]+replacement+word[j+2:]).items():out[v]=out.get(v,zero)+coefficient*c
        return {v:c for v,c in out.items() if c}
    return {word:one}
def add(A,B,scale=one):
    C=dict(A)
    for v,c in B.items():C[v]=C.get(v,zero)+scale*c
    return {v:c for v,c in C.items() if c}
def mul(A,B):
    C={}
    for v,c in A.items():
        for z,d in B.items():
            for h,e in nf(v+z).items():C[h]=C.get(h,zero)+c*d*e
    return {v:c for v,c in C.items() if c}
x={(0,):one/2,(1,):one/2};c={(0,):one/2,(1,):-one/2};y={(2,):one}
original=[x,y,c]
for first in range(3):
    relation={}
    for word,coefficient in w.items():
        if word[0]==first:relation=add(relation,mul(original[word[1]],original[word[2]]),coefficient)
    assert not relation
basis=[(0,)*i+(1,)*j+(2,)*k for i in range(4) for j in range(4-i) for k in [3-i-j]]
index={v:j for j,v in enumerate(basis)}
images=[{(1,):a},{(0,):a},{(2,):a**7}]
def sigma(P):
    out={}
    for word,coefficient in P.items():
        term={():coefficient}
        for letter in word:term=mul(term,images[letter])
        out=add(out,term)
    return out
columns=[sigma({v:one}) for v in basis]
M=DomainMatrix.from_dod({i:{j:columns[j].get(v,zero)-(one if i==j else zero) for j in range(10)} for i,v in enumerate(basis)},(10,10),K)
assert M.rank()==9
H=mul(mul(x,x),y)
assert sigma(H)==H
obstruction=add(mul(H,x),mul(x,H),-omega**2)
expected={v:(t-omega**2)*d for v,d in mul(mul(mul(x,x),x),y).items()}
assert obstruction==expected and obstruction
source=json.loads(Path(__file__).with_name('cubic_fourth_root_spectrum_reductions_certificate.json').read_text())
last=[r for r in source['final_survivors'] if r['N']==6]
assert [r['spectrum'] for r in last]==[[2,0,5],[4,0,1]]
final=[r for r in source['final_survivors'] if r['N']!=6]
assert len(final)==14
result={'status':'PASS','scope':'exact ninth-root sigma/top-tensor orbits, original relation slices, invariant A3 rank and nonzero normalizer; ordinary coverage proof separate',
        'field':'Q(a), a^6+a^3+1=0; omega=a^6','sigma_fixed_tensor_orbits':orbit_lists,
        'repeated_sigma_U_first_slice_tail_support':'at most c^2; rank<=1<2',
        'normalized_AS3_relations':['x^2=c^2','y*x=-a^2*x*y','y*c=-a^2*c*y'],
        'sigma':['a*x','a^7*y','-a*c'],'all_three_original_tensor_slices_reduce_to_zero':True,
        'sigma_minus_one_rank_on_A3':9,'sigma_fixed_A3':'k*x^2*y',
        'normal_x_obstruction':'(-a^2-omega^2)*x^3*y !=0',
        'sixth_order_excluded_spectra':last,'final_survivors':final,'final_spectrum_count':14,
        'remaining_orders':[3,4],'remaining_counts':{'3':3,'4':11},
        'not_claimed':['remaining14 H3 existence','complete four-eigenvalue or CY classification']}
Path(__file__).with_name('cubic_sixth_root_last_Ore_exclusion_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','sigma_fixed_A3_dimension':1,'original_slices':'PASS','normal_x_obstruction':'nonzero','remaining_spectra':14}))
