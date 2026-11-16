"""All-parameter tangent exclusion by explicit polynomial identities.

Requires SymPy. python-flint is optional and speeds up polynomial determinants.
No sampling, generic-rank inference, AS4-existence assumption, or division by
an exceptional parameter polynomial is used in this verifier.
"""
import itertools
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix

R=S.QQ.poly_ring('D');D=R.gens[0];one=R.one;zero=R.zero
source=Path(__file__).with_name('cubic_order2_22_tangent_annihilator_input.json')
data=json.loads(source.read_text())
assert data['generator_order']==['x','y','u','v']
assert len(data['functionals'])==33 and len(data['rank_minors'])==9

def decode(value):
    num=R.ring.from_dict({(n,):S.QQ(c) for n,c in value['num']})
    den=R.ring.from_dict({(n,):S.QQ(c) for n,c in value['den']})
    assert den and den.degree()==0
    # Preserve rational constant denominators, not just a fraction numerator.
    return num.mul_ground(S.QQ.one/den[(0,)])

L=[{int(j):decode(c) for j,c in row.items()} for row in data['functionals']]
w3=[w for w in itertools.product(range(4),repeat=3) if sum(i>=2 for i in w)%2==0]
w4=[w for w in itertools.product(range(4),repeat=4) if sum(i>=2 for i in w)%2==0]
index={w:j for j,w in enumerate(w4)}
assert len(w3)==32 and len(w4)==128
# Three relations were multiplied by 2D, a unit on the necessary chart.
rels=[
 {(0,1):one+D*D,(1,0):-one-D*D,(1,1):2*D,(2,2):2*D,(3,3):-2*D},
 {(0,0):one+D*D,(1,0):-2*D,(1,1):2*D*D,(2,3):-2*D},
 {(0,0):-one-D*D,(0,1):-2*D,(1,1):-2*D*D,(3,2):2*D},
 {(0,0):one,(0,1):D,(1,0):-D,(2,2):one},
 {(0,2):one,(2,1):one,(3,0):-one},
 {(0,3):one,(1,2):one,(2,0):-one}]
checks=0
for rel in rels:
    parity=sum(i>=2 for i in next(iter(rel)))%2
    for pos in range(3):
        for rest in itertools.product(range(4),repeat=2):
            if (sum(i>=2 for i in rest)+parity)%2:continue
            row={index[rest[:pos]+w+rest[pos:]]:c for w,c in rel.items()}
            for f in L:
                assert sum((c*f.get(j,zero) for j,c in row.items()),zero)==zero
                checks+=1
assert checks==4752
# Any positive-parity cubic commuting with x,y lies in this polynomial kernel.
rows={}
for i,f in enumerate(L):
    for g in range(2):
        row={}
        for j,w in enumerate(w3):
            c=f.get(index[w+(g,)],zero)-f.get(index[(g,)+w],zero)
            if c:row[j]=c
        rows[2*i+g]=row
M=DomainMatrix(rows,(66,32),R);gcd=zero;degrees=[]
for witness in data['rank_minors']:
    rr,cc=witness['rows'],witness['columns']
    assert len(rr)==len(set(rr))==len(cc)==len(set(cc))==10
    minor=M.extract(rr,cc).det()
    assert minor
    degrees.append(minor.degree());gcd=gcd.gcd(minor)
assert gcd.monic()==D**12
out={'status':'PASS','scope':'entire full-rank tangent chart in semisimple (2,2), odd rank2',
     'polynomial_functionals':33,'exact_quartic_annihilator_identities':checks,
     'normal_constraint_shape':[66,32],'maximal_minor_sizes':[10,10],
     'minor_degrees':degrees,'minor_count':9,'monic_minor_gcd':'D^12',
     'conclusion':'rank at least10 for every D!=0; H3 positive cubic dimension10 forces centralizer kernel to be relations, so no nonzero designated normal cubic',
     'not_claimed':['tangent degenerate cross-block boundary','secant chart','AS4 existence for arbitrary D','complete H3 classification']}
Path(__file__).with_name('cubic_order2_22_tangent_exclusion_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all-D tangent exclusion: 4752 identities and nine exact minors with gcd D^12')
