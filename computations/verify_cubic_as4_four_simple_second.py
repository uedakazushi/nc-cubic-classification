#!/usr/bin/env python3
"""Entire real two-parameter second-shared H family: finite rank cover."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.polyerrors import HeuristicGCDFailed
from verify_cubic_as4_four_simple import source_matrix,W2,IX
from verify_cubic_pym_generic import words,relation_rows


def h_matrix(lam,p):
    lam,p=map(S.sympify,(lam,p))
    return source_matrix(lam,{0:1,1:1,5:1,2:p,9:(lam*lam-1)/16,14:lam*lam/(16*(p-1)),
                              19:-lam/(16*(p-1)),20:p/(16*(p-1))})


def central_data(R,field):
    """Keep projection and commutator arithmetic in the exact coefficient field."""
    rels=[{v:S.cancel(R[k,j]) for k,v in enumerate(W2) if R[k,j]} for j in range(6)]
    def project(n):
        source=DomainMatrix.from_Matrix(relation_rows(rels,n)).convert_to(field)
        rr,piv=source.rref();free=[j for j in range(4**n) if j not in piv];rd=rr.to_dok()
        out={(i,j):field.one for i,j in enumerate(free)}
        for row,j in enumerate(piv):
            for i,k in enumerate(free):
                c=rd.get((row,k),field.zero)
                if c:out[i,j]=-c
        P=DomainMatrix.from_dok(out,(len(free),4**n),field)
        assert (P*source.transpose()).is_zero_matrix
        return free,P
    f3,p3=project(3);f4,p4=project(4);assert (len(f3),len(f4))==(20,35)
    pd=p4.to_dok();ix={v:j for j,v in enumerate(words(4))};out={}
    for j,k in enumerate(f3):
        v=words(3)[k]
        for gen in range(4):
            a,b=ix[v+(gen,)],ix[(gen,)+v]
            for i in range(35):
                c=pd.get((i,a),field.zero)-pd.get((i,b),field.zero)
                if c:out[35*gen+i,j]=c
    matrix=DomainMatrix.from_dok(out,(140,20),field)
    _,rows=matrix.transpose().rref()
    return matrix,list(rows),(p3,p4)


def check_denominators(projections,allowed):
    for P in projections:
        for entry in P.to_dok().values():
            den=entry.denom
            for expr in allowed:
                factor=den.ring.from_expr(expr)
                while True:
                    quo,rem=divmod(den,factor)
                    if rem:break
                    den=quo
            assert den.is_ground


def check_minor(matrix,rows,expected,polynomial=False):
    assert len(rows)==20
    C=matrix.extract(rows,list(range(20)))
    if not polynomial:
        try:
            assert C.det()==matrix.domain.from_sympy(expected)
            return
        except HeuristicGCDFailed:
            pass
    # Deterministic polynomial exact division avoids a SymPy heuristic-GCD
    # failure that occurs for the curve-B fraction-field determinant.
    denominators,cleared=C.clear_denoms_rowwise(convert=True)
    num,den=cleared.det(),denominators.det();domain=cleared.domain
    en,ed=S.fraction(expected)
    assert not (num*domain.from_sympy(ed)-den*domain.from_sympy(en))


def main():
    l,p=S.symbols('lambda p');R,A=h_matrix(l,p);F=S.QQ.frac_field(l,p)
    rd=DomainMatrix.from_Matrix(R).convert_to(F);ad=DomainMatrix.from_Matrix(A).convert_to(F)
    w=(rd*ad*rd.transpose()).to_dok()
    assert all(not(w.get((IX[v[:2]],IX[v[2:]]),F.zero)+w.get((IX[v[1:3]],IX[(v[3],v[0])]),F.zero)) for v in words(4))
    ca=l*l+2*l*p+p;cb=l*l+l*p+l+1
    generic=l**6*(l-1)**4*(l+1)**5*ca*cb/(2**40*(p-1)**13)
    M,rows,projections=central_data(R,F);check_denominators(projections,[l,l-1,l+1,p-1]);check_minor(M,rows,generic)
    covers=[{'chart':'generic','minor_rows':rows,'minor':str(generic),'denominator_support':['lambda','lambda-1','lambda+1','p-1']}]
    print('PASS generic H two-parameter centre rank20 away from three loci',flush=True)
    charts=[('lambda=1',S.Integer(1),p,S.QQ.frac_field(p),[p-1],(3*p+1)/(2**33*(p-1)**11),False),
            ('curve A',l,-l*l/(2*l+1),S.QQ.frac_field(l),[l,l-1,l+1,2*l+1],-l**7*(l-1)**4*(2*l+1)**10/(2**40*(l+1)**15),False),
            ('curve B',l,-(l*l+l+1)/l,S.QQ.frac_field(l),[l,l-1,l+1],-l**17*(l-1)**3/(2**37*(l+1)**15),True)]
    for name,ll,pp,field,units,expected,poly in charts:
        RR,AA=h_matrix(ll,pp);M,rows,projections=central_data(RR,field)
        check_denominators(projections,units);check_minor(M,rows,expected,poly)
        covers.append({'chart':name,'p':str(pp),'lambda':str(ll),'minor_rows':rows,'minor':str(expected),
                       'denominator_support':list(map(str,units))})
        print('PASS H',name,'controlled-denominator centre rank20',flush=True)
    RR,AA=h_matrix(S.Integer(1),-S.Rational(1,3));M,rows,_=central_data(RR,S.QQ);assert len(rows)==20
    det=S.QQ.to_sympy(M.extract(rows,list(range(20))).det())
    assert S.cancel(-l*l/(2*l+1)-1+(l+1)**2/(2*l+1))==0
    assert S.cancel(-(l*l+l+1)/l-1+(l+1)**2/l)==0
    cert={'version':'classification-v79','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source_presentation':'SECOND_SHARED_OPEN_COMPLETE.tex FO2 only',
          'parameter_domain':'lambda!=0,-1; p!=1','universal_anti_cyclic_top_tensor':True,
          'rank_cover':covers,'last_point':{'lambda':1,'p':'-1/3','minor_rows':rows,'minor_determinant':str(det),'rank':20},
          'centre3_dimension_all_allowed_parameters':0,
          'scope':'Entire explicit two-parameter H family excluded conditional AS4; no full chart/CY coverage, AS4 sufficiency or all-isomorphism theorem imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_second_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS entire H family: three curve charts and last QQ point cover all allowed parameters',flush=True)

if __name__=='__main__':main()
