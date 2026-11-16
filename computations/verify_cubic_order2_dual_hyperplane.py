#!/usr/bin/env python3
"""Universal rank bookkeeping and exact bi-normal calibration for the dual section."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    t=S.symbols('t');HE=(1+t)**4
    ideal=t+3*t*t+3*t**3+t**4
    assert S.expand(HE-ideal-(1+t)**3)==0
    annihilator=t+3*t*t+3*t**3+t**4
    assert S.expand(HE-(1+3*t+3*t*t+t**3)-annihilator)==0
    a=S.symbols('a',nonzero=True)
    b,c=S.symbols('b c')
    # E=Q/(PZ,P²+aZ²,X²+bZ²,Y²+cZ²), a!=0. Thus Z³=0.
    basis=[(i,j,k,0) for i,j,k in itertools.product(range(2),repeat=3)]
    basis += [(0,j,k,l) for l in [1,2] for j,k in itertools.product(range(2),repeat=2)]
    index={w:i for i,w in enumerate(basis)}
    def product(w,v):
        # Only PX and XY anticommute; all squares are central.
        sign=(-1)**(w[1]*v[0]+w[2]*v[1])
        powers=[w[i]+v[i] for i in range(4)]
        coeff=S.Integer(sign)
        for i,cc in enumerate([a,b,c]):
            coeff*=(-cc)**(powers[i]//2)
            powers[3]+=2*(powers[i]//2);powers[i]%=2
        if powers[3]>=3 or (powers[0] and powers[3]):return S.Integer(0),None
        return coeff,tuple(powers)
    def matrix_left(w):
        out=S.zeros(16)
        for j,v in enumerate(basis):
            coeff,ww=product(w,v)
            if coeff:out[index[ww],j]=coeff
        return out
    P,X,Y,Z=[tuple(int(i==j) for i in range(4)) for j in range(4)]
    generators=[P,X,Y,Z];matrices=[matrix_left(w) for w in generators]
    for w,v in itertools.product(generators,repeat=2):
        coeff,ww=product(w,v)
        expected=S.zeros(16) if not coeff else coeff*matrix_left(ww)
        assert (matrix_left(w)*matrix_left(v)-expected).applyfunc(S.expand)==S.zeros(16)
    LZ=matrices[3];LP=matrices[0]
    ranks=[]
    for degree in range(4):
        columns=[i for i,w in enumerate(basis) if sum(w)==degree]
        ranks.append(LZ[:,columns].rank())
    assert ranks==[1,3,3,1]
    assert LZ*LP==LP*LZ==S.zeros(16)
    assert LP.rank()==LZ.rank()==8
    # Exact two-periodic linear resolution: image(P)=kernel(Z), and vice versa.
    top=(0,1,1,2)
    pairing=S.Matrix([[product(w,v)[0] if product(w,v)[1]==top else 0 for v in basis] for w in basis])
    assert S.factor(pairing.det())==a**4
    nu=[-1,-1,-1,1]
    for i,w in enumerate(generators):
        for v in basis:
            cw,ww=product(w,v);cv,vv=product(v,w)
            assert (cw if ww==top else 0)==nu[i]*(cv if vv==top else 0)
    # F=E/(Z) is the three-generator quantum exterior algebra.
    one=[w for w in basis if sum(w)==1 and not w[3]]
    two=[w for w in basis if sum(w)==2 and not w[3]]
    topF=(1,1,1,0)
    left=S.Matrix([[product(w,v)[0] if product(w,v)[1]==topF else 0 for v in two] for w in one])
    right=S.Matrix([[product(v,w)[0] if product(v,w)[1]==topF else 0 for v in two] for w in one])
    assert left.det()!=0 and right.det()!=0
    data={
      'universal_hypotheses':'quadratic Koszul AS4 with the proved common-plane graph in either Nakayama multiplicity(1,3) or(3,1)',
      'dual_linear_element':'zstar*E1=E1*zstar has dimension3; common kernel is the complementary positive/negative dual line kvstar',
      'multiplication_ranks_by_degree':[1,3,3,1],
      'quotient_Hilbert':[1,3,3,1],'annihilator_Hilbert':[0,1,3,3,1],
      'Frobenius_test':'both degree1/degree2 3x3 pairing matrices are invertible',
      'equivalent_exact_pair':'Ann(zstar)=Estar*vstar=vstar*Estar; then Ann(vstar)=(zstar)',
      'consequence_on_test_open':'linear two-periodic E-resolution implies F Koszul; its quadratic dual is AS3 and embeds canonically into B by spectral-sequence edge-map injectivity',
      'calibration':'explicit(3,1) bi-normal E, a!=0: all identities checked symbolically, ranks1,3,3,1 and exact annihilator pair(P,Z)',
      'scope':'The universal statement uses Frobenius duality and a change-of-rings spectral-sequence proof. The exact model calibrates ranks and annihilators; no universal Frobenius nonvanishing or full (3,1) coverage is asserted.'}
    path=Path(__file__).with_name('cubic_order2_dual_hyperplane_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS dual hyperplane Hilbert bookkeeping and exact zero-divisor calibration')


if __name__=='__main__':main()
