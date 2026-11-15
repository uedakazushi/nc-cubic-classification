#!/usr/bin/env python3
"""Exact all-parameter centre-rank covers for DS211 T/U, and fixed cases."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_ds211 import source_matrix,cyclic,ww
from verify_cubic_as4_tt22_remaining import projection
from verify_cubic_pym_generic import words


def centre_matrix(R,field):
    rels=[{w:R[i,j] for i,w in enumerate(ww) if R[i,j]} for j in range(6)]
    f3,p3=projection(rels,3,field);f4,p4=projection(rels,4,field)
    assert len(f3)==20 and len(f4)==35
    ix={w:j for j,w in enumerate(words(4))};m=S.zeros(140,20)
    for j,col in enumerate(f3):
        w=words(3)[col]
        for i in range(4):m[35*i:35*(i+1),j]=p4[:,ix[w+(i,)]]-p4[:,ix[(i,)+w]]
    return m,p3,p4


def rank_certificate(name,R,field):
    cyclic(R);m,p3,p4=centre_matrix(R,field)
    _,rows=DomainMatrix.from_Matrix(m.T).convert_to(field).rref();assert len(rows)==20
    det=DomainMatrix.from_Matrix(m[list(rows),:]).convert_to(field).det();assert det!=0
    print('PASS exact centre3 rank20',name,flush=True)
    return {'name':name,'field':str(field),'dimensions_3_4':[20,35],
            'minor_rows':list(rows),'minor_determinant':str(field.to_sympy(det))}


def main():
    p=S.Symbol('p');Q=S.Rational;field=S.QQ.frac_field(p)
    T=source_matrix({0:1,3:1,5:p,12:p,8:-1/(16*p),14:p-Q(1,16),20:Q(1,8)})
    U=source_matrix({0:1,7:1,11:p,13:p,9:p,12:p*p+Q(1,16),14:2*p*p+Q(1,8),20:Q(1,8)})
    generic=[];critical=[]
    families=[('T',T,[p,8*p+1,16*p+1],[-Q(1,8),-Q(1,16)]),
              ('U',U,[p,4*p-1,48*p*p+8*p+1],[Q(1,4),(-1+S.sqrt(-2))/12])]
    for name,R,factors,values in families:
        cyclic(R);m,p3,p4=centre_matrix(R,field)
        denominators=set(S.denom(z) for matrix in [p3,p4] for z in matrix)
        for d in denominators:
            poly=S.Poly(d,p)
            assert len(poly.terms())==1
            if name=='U':assert poly.degree()==0
        _,rows=DomainMatrix.from_Matrix(m.T).convert_to(field).rref();assert len(rows)==20
        det=field.to_sympy(DomainMatrix.from_Matrix(m[list(rows),:]).convert_to(field).det())
        numerator=S.Poly(S.fraction(S.cancel(det))[0],p)
        residual=numerator
        for factor in factors:
            f=S.Poly(factor,p)
            while not residual.rem(f):residual=residual.exquo(f)
        assert residual.degree()==0
        generic.append({'family':name,'projection_denominators':list(map(str,sorted(denominators,key=str))),
                        'minor_rows':list(rows),'minor_determinant':str(S.factor(det)),
                        'all_possible_zero_factors':list(map(str,factors)),
                        'scope':'Projection relations and identity free columns hold away from the displayed parameter-unit poles. At an AS4 realization these are quotient bases; no rank-flatness extrapolation is used.'})
        for value in values:
            special=R.applyfunc(lambda z:S.cancel(z.subs(p,value)))
            K=S.QQ.algebraic_field(S.sqrt(-2)) if value.has(S.I) else S.QQ
            critical.append(rank_certificate(name+' at '+str(value),special,K))
    fixed=[('L_plus; L_minus by conjugation',{0:1,3:1,4:S.I/4,11:S.I/4,13:S.I/4,9:S.I/4,5:-Q(1,16),12:-Q(1,8),14:-Q(1,4),20:Q(1,8)},S.QQ.algebraic_field(S.I)),
           ('P',{0:1,11:S.I/4,20:Q(1,8)},S.QQ.algebraic_field(S.I)),
           ('V_0',{0:1,7:1,12:0,14:Q(1,16),20:Q(1,16)},S.QQ)]
    fixed_certs=[rank_certificate(name,source_matrix(values),K) for name,values,K in fixed]
    cert={'version':'classification-v72','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source':'CY_ZERO_COMMUTATORS_DOUBLE_SIMPLE_NONZERO_COMPLETE.tex DS1-DS3',
          'generic_rank_covers':generic,'critical_rank_covers':critical,'fixed_rank_covers':fixed_certs,
          'scope':'All allowed T/U parameters and three fixed L+/L-/P presentations excluded. V_0 boundary checked. Cyclic tensor gives mu=id conditional AS4; full upstream existence/coverage is not imported.'}
    Path(__file__).with_name('cubic_as4_ds211_remaining_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS all allowed T/U values covered, fixed cases and V_0 rank20')


if __name__=='__main__':main()
