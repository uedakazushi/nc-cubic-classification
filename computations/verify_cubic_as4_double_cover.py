#!/usr/bin/env python3
"""Conditional-AS4 Nakayama audit and Laurent identities for two as4 presentations.

No AS4 existence, noetherianity or atlas coverage theorem is imported.
At an AS4 realization the displayed socle functional and pairings determine mu.
"""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_pym_generic import words,relation_rows


def main():
    h=S.Symbol('h');field=S.QQ.algebraic_field(S.I).frac_field(h);audits=[]
    def laurent(expr):
        den=S.fraction(S.cancel(expr))[1]
        return len(S.Poly(den,h,extension=S.I).terms())==1
    for family in [1,2]:
        rels=[{(1,0):1,(0,1):-S.I},{(3,2):1,(2,3):-S.I}]
        if family==1:
            rels += [{(0,0):1,(1,3):2*h,(3,1):-2*h},
                     {(1,1):1,(0,2):2,(2,0):-2},
                     {(2,2):1,(1,3):-2*h,(3,1):2*h},
                     {(3,3):1,(0,2):2,(2,0):-2}]
            normal_signs=[[1,-1,1,-1],[-1,1,-1,1]]
        else:
            rels += [{(0,0):1,(1,2):2*h,(2,1):-2*h},
                     {(1,1):1,(0,3):2,(3,0):-2},
                     {(2,2):1,(0,3):-2*h,(3,0):2*h},
                     {(3,3):1,(1,2):2,(2,1):-2}]
            normal_signs=[[1,-1,-1,1],[-1,1,1,-1]]
        assert all(normal_signs[0][i]*normal_signs[1][i]==-1 for i in range(4))
        R=S.Matrix([[rel.get(w,0) for w in words(2)] for rel in rels])
        perp=R.nullspace();assert len(perp)==10
        dual=[{w:v[j] for j,w in enumerate(words(2)) if v[j]} for v in perp]
        r3,piv3=DomainMatrix.from_Matrix(relation_rows(dual,3)).convert_to(field).rref()
        basis=[w for j,w in enumerate(words(3)) if j not in piv3];assert len(basis)==4
        m4=relation_rows(dual,4)
        r4,piv4=DomainMatrix.from_Matrix(m4).convert_to(field).rref();r4=r4.to_Matrix()
        free=[j for j in range(256) if j not in piv4];assert len(free)==1
        phi=S.Matrix([1 if j==free[0] else -r4[piv4.index(j),free[0]] for j in range(256)])
        assert all(laurent(x) for x in phi)
        assert DomainMatrix.from_Matrix(m4*phi).convert_to(field).is_zero_matrix
        functional=dict(zip(words(4),list(phi)))
        left=S.Matrix([[functional[(i,)+w] for w in basis] for i in range(4)])
        right=S.Matrix([[functional[w+(i,)] for i in range(4)] for w in basis])
        assert S.cancel(left.det()**2-1/(4*h**4))==0
        assert S.cancel(right.det()**2-1/(4*h**4))==0
        mu_e=(left*right.T.inv()).T
        assert S.simplify(-mu_e.T.inv())==S.eye(4)
        # Eight quadratic normality identities with explicit Laurent coefficients.
        m3=relation_rows(rels,3);A=m3.T;index={w:j for j,w in enumerate(words(3))};targets=[]
        for q,signs in zip([(0,0),(1,1)],normal_signs):
            for i in range(4):
                col=S.zeros(64,1);col[index[q+(i,)]]+=1;col[index[(i,)+q]]-=signs[i];targets.append(col)
        T=S.Matrix.hstack(*targets)
        rr,piv=DomainMatrix.from_Matrix(A.row_join(T)).convert_to(field).rref();rr=rr.to_Matrix()
        assert all(j<A.cols for j in piv)
        witnesses=S.zeros(A.cols,T.cols)
        for row,j in enumerate(piv):witnesses[j,:]=rr[row,A.cols:]
        assert all(laurent(x) for x in witnesses)
        assert DomainMatrix.from_Matrix(A*witnesses-T).convert_to(field).is_zero_matrix
        audits.append({'family':family,'E3_monomials':[list(w) for w in basis],
                       'socle_functional':[{'word':list(w),'coefficient':str(v)} for w,v in functional.items() if v],
                       'left_pairing_determinant':str(S.factor(left.det())),
                       'right_pairing_determinant':str(S.factor(right.det())),
                       'Nakayama_at_any_Koszul_AS4_realization':'identity',
                       'normal_signs_a2_b2':normal_signs,
                       'normality_witnesses':[[{'row':i,'coefficient':str(witnesses[i,j])} for i in range(A.cols) if witnesses[i,j]] for j in range(T.cols)]})
        print('PASS family',family,'Laurent socle/pairings, mu=id conditional AS4, eight quadratic normal identities',flush=True)
    cert={'version':'classification-v69','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'presentation_source':'research/proofs/CY_ZERO_COMMUTATORS_DOUBLE_COVER_COMPLETE.tex (DCC1)',
          'field':'QQ(i), h nonzero','families':audits,
          'obstruction':'a^2*b^2 normal with conjugation -I; in a domain odd centre vanishes.',
          'scope':'No new AS4 existence/coverage/noetherianity/domain theorem imported. If either presentation is a strong H3 envelope, AS4/domain give mu=id by the universal functional, contradicting the normal quartic obstruction.'}
    Path(__file__).with_name('cubic_as4_double_cover_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')


if __name__=='__main__':main()
