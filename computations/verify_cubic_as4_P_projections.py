#!/usr/bin/env python3
"""Independent original-word replay for the full two-parameter P family.
SymPy required; python-flint is optional exact polynomial acceleration.
"""
import json,sys
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple_p import pvalues
from verify_cubic_as4_four_simple import source_matrix,W2
from verify_cubic_pym_generic import relation_rows
from exact_polynomial_complex_product import assert_complex_product


def verify(n):
    l,r=S.symbols('l r');F=S.QQ.frac_field(l,r);K=F.get_ring();a=2*l*l+2*l+1;d=a-(2*l+1)*r
    data=json.loads(Path(__file__).with_name(f'cubic_as4_P_projection_degree{n}.json').read_text())
    free=data['free_columns_zero_based'];nf={3:20,4:35}[n];assert len(free)==nf and len(set(free))==nf
    def load(key):
        entries={}
        for i,j,terms in data[key]:
            coefficients={(a,b):S.QQ.from_sympy(S.Rational(c)) for a,b,c in terms}
            assert len(coefficients)==len(terms)
            entries[i,j]=K.ring.from_dict(coefficients)
        assert len(entries)==len(data[key])
        return DomainMatrix.from_dok(entries,(nf,4**n),K)
    P,Q=load('real'),load('imag');D=K.from_sympy(S.sympify(data['common_real_denominator'],locals={'l':l,'r':r}));assert D
    den=D
    for f in [l,l+1,r-1,a]:
        factor=K.from_sympy(f)
        while True:
            quo,rem=divmod(den,factor)
            if rem:break
            den=quo
    assert den.is_ground
    pd,qd=P.to_dok(),Q.to_dok()
    for i in range(nf):
        for j,c in enumerate(free):assert pd.get((i,c),K.zero)==(D if i==j else K.zero) and not qd.get((i,c),K.zero)
    R,_=source_matrix(l,pvalues(l,r));rels=[{w:R[k,j] for k,w in enumerate(W2) if R[k,j]} for j in range(6)];M=relation_rows(rels,n).T
    ar={};ai={};cache={};E=K.from_sympy(l**3*(l+1)**3*d)
    for ij,e in M.todok().items():
        key=str(e)
        if key not in cache:
            z=S.cancel(e);bar=S.cancel(z.subs(S.I,-S.I));cache[key]=(F.from_sympy(S.cancel((z+bar)/2)),F.from_sympy(S.cancel((z-bar)/(2*S.I))))
        x,y=cache[key]
        if x:ar[ij]=x.numer*E.exquo(x.denom)
        if y:ai[ij]=y.numer*E.exquo(y.denom)
    AR=DomainMatrix.from_dok(ar,M.shape,K);AI=DomainMatrix.from_dok(ai,M.shape,K)
    backend=assert_complex_product(P,Q,AR,AI)
    print('PASS P degree',n,'original-word annihilation/free identity; denominator',S.factor(K.to_sympy(D)),'backend',backend,flush=True)
    return free,P,Q,D

if __name__=='__main__':
    for n in map(int,sys.argv[1:] or ['3','4']):verify(n)
