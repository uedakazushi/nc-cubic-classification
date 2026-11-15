#!/usr/bin/env python3
"""AB3 bad S family and the AB2 T(lambda=-2) endpoint, presentation only."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple import source_matrix,W2
from verify_cubic_pym_generic import relation_rows


def t_matrix(lam,eta=1):
    lam,eta=map(S.sympify,(lam,eta));q=lam+1;z=eta*S.I*q/4
    x16=eta*S.I*(q*q+1)/(8*q);x19=lam*lam*(q*q+1)/(64*q*q)
    return source_matrix(lam,{0:1,1:1,4:1,2:lam+2,5:1/q,6:lam*z/2,8:-lam*z/2,7:-z*(q*q+1)/2,
      10:eta*S.I*lam*lam/(8*q),12:-eta*S.I*lam*lam/(8*q),17:eta*S.I*lam/(8*q),15:-eta*S.I*lam/(8*q),16:x16,11:-lam*x16,
      18:lam*lam*(lam+2)/64,13:-lam*lam*(q*q+1)/64,19:x19,14:-lam*x19,
      9:-(lam**5+4*lam**4+9*lam**3+14*lam*lam+12*lam+4)/64,20:(lam**3+6*lam*lam+8*lam+4)/(64*q*q)})


def s_matrix(z):
    z=S.sympify(z);u=(1-16*z*z)/(32*z)
    return source_matrix(S.Integer(-2),{0:1,1:1,4:1,5:-1,8:z,15:z,10:2*z,11:2*z,12:-2*z,
      6:u,7:u,17:u,16:-u,13:z*z-S.Rational(1,16),19:S.Rational(1,16)-z*z,14:-4*z*z,9:-u*u,20:-u*u})


def main():
    z=S.symbols('zeta');field=S.QQ.frac_field(z);R,A=s_matrix(z)
    rels=[{v:S.cancel(R[k,j]) for k,v in enumerate(W2) if R[k,j]} for j in range(6)]
    rd=DomainMatrix.from_Matrix(R).convert_to(field)
    for e in rd.to_dok().values():
        den=e.denom;factor=den.ring.from_expr(z)
        while den.degree()>0:
            quo,rem=divmod(den,factor);assert not rem
            den=quo
    source=DomainMatrix.from_Matrix(relation_rows(rels,4)).convert_to(field)
    _,piv=source.rref();assert len(piv)==219
    # R_4 is regular on zeta!=0. Rank cannot exceed its generic value at a
    # closed point, so all closed fibres have dimension >=256-219=37.
    endpoints=[]
    for eta in [1,-1]:
        T,AT=t_matrix(S.Integer(-2),eta);SS,AA=s_matrix(-eta*S.I/4)
        assert all(S.cancel(c)==0 for c in T-SS)
        endpoints.append({'eta':eta,'T_lambda':-2,'equals_S_zeta':str(-eta*S.I/4)})
    cert={'version':'classification-v83','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source_presentation':'ADJACENT_SHARED_BOUNDARY_REDUCTION.tex AB2/AB3 explicit coefficients only',
          'S_parameter_domain':'zeta!=0','presentation_denominator_support':'zeta',
          'S_generic_degree4_relation_rank':219,'S_all_closed_degree4_dimension_lower_bound':37,
          'AS4_degree4_required':35,'T_bad_endpoints':endpoints,
          'scope':'All explicit S_zeta and both T_-2 endpoints excluded by Hilbert obstruction. No claim for T_lambda away from -2, and no full CY/chart coverage, AS4 sufficiency or isomorphism theorem imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_adjacent_S_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS all S_zeta dimensions4>=37 and both literal T_-2 endpoint identities')

if __name__=='__main__':main()
