#!/usr/bin/env python3
"""Independent QQ[l] replay of rational T word-quotient witnesses.
Generation may use Singular; this replay uses only SymPy and original relations.
"""
import json,sys
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple_adjacent_S import t_matrix
from verify_cubic_as4_four_simple import W2
from verify_cubic_pym_generic import relation_rows


def verify(n):
    l=S.symbols('l');F=S.QQ.frac_field(l);K=F.get_ring()
    data=json.loads(Path(__file__).with_name(f'cubic_as4_T_projection_degree{n}.json').read_text())
    free=data['free_columns_zero_based'];nf={3:20,4:35}[n]
    assert len(free)==nf and len(set(free))==nf
    shape=(nf,4**n)
    def load(key):
        entries={(i,j):K.from_sympy(S.sympify(e,locals={'l':l})) for i,j,e in data[key]}
        assert len(entries)==len(data[key])
        return DomainMatrix.from_dok(entries,shape,K)
    P,Q=load('real'),load('imag')
    dr=data.get('common_denominator_real',data.get('common_real_denominator'));di=data.get('common_denominator_imag','0')
    D=K.from_sympy(S.sympify(dr,locals={'l':l}));DI=K.from_sympy(S.sympify(di,locals={'l':l}));assert D or DI
    pd,qd=P.to_dok(),Q.to_dok()
    for a in range(nf):
        for b,j in enumerate(free):
            assert pd.get((a,j),K.zero)==(D if a==b else K.zero)
            assert qd.get((a,j),K.zero)==(DI if a==b else K.zero)
    R,_=t_matrix(l);rels=[{v:R[k,j] for k,v in enumerate(W2) if R[k,j]} for j in range(6)]
    M=relation_rows(rels,n).T;ar={};ai={};cache={}
    for ij,e in M.todok().items():
        key=str(e)
        if key not in cache:
            z=S.cancel(e);bar=S.cancel(z.subs(S.I,-S.I))
            cache[key]=[F.from_sympy(S.cancel((z+bar)/2)),F.from_sympy(S.cancel((z-bar)/(2*S.I)))]
        a,b=cache[key]
        if a:ar[ij]=a
        if b:ai[ij]=b
    E=F.field.ring.one
    for a in list(ar.values())+list(ai.values()):E=E.lcm(a.denom)
    def clear(entries):return DomainMatrix.from_dok({ij:a.numer*E.exquo(a.denom) for ij,a in entries.items()},M.shape,K)
    A,B=clear(ar),clear(ai)
    assert (P*A-Q*B).is_zero_matrix and (P*B+Q*A).is_zero_matrix
    print('PASS T degree',n,'original-word annihilation and free identity; denominator',S.factor(K.to_sympy(D)+S.I*K.to_sympy(DI),extension=S.I),flush=True)
    return free,P,Q,D,DI

if __name__=='__main__':
    for n in map(int,sys.argv[1:] or ['3']):verify(n)
