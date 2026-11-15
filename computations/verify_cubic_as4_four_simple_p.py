#!/usr/bin/env python3
"""Exact P-family lambda=2 centre exclusion and all-parameter CY identity.

SymPy is required; optional python-flint makes the rational-function elimination
substantially faster. No AS4 sufficiency or full four-simple coverage imported.
"""
import json,time
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple import source_matrix,W2,IX
from verify_cubic_pym_generic import words,relation_rows

def pvalues(l,r):
 a=2*l*l+2*l+1;b=2*l+1;d=a-b*r;e=(l+1)*r-a;f=a*r-2*l*a-1;i=S.I
 return {0:1,1:1,3:1,4:1,2:(a*r-b)/d,5:r,6:i*(l+1)/(8*l),8:i*(l+1)/(8*l),10:-i*l/(8*(l+1)),11:-i*l/(8*(l+1)),7:i*(l+1)*f/(8*l*d),12:i*e/(8*(l+1)),15:i*b/(8*l*(l+1)),17:i*a/(8*l*(l+1)),16:-i*a/(8*l*(l+1)),13:-S.Rational(1,64),18:a/(64*l*l),19:a/(64*(l+1)**2),20:-a*b/(64*l*l*(l+1)**2),14:-((l+1)**2*r-a)/(64*(l+1)**2),9:-(l+1)**2*(a*r-4*l*l-2*l-1)/(64*l*l*d)}

def projection(rels,n,field):
    source=DomainMatrix.from_Matrix(relation_rows(rels,n).applyfunc(S.expand)).convert_to(field)
    rr,piv=source.rref();rr=rr.to_Matrix()
    free=[j for j in range(4**n) if j not in piv];p=S.zeros(len(free),4**n)
    for i,j in enumerate(free):p[i,j]=1
    for i,j in enumerate(piv):
        for u,v in enumerate(free):p[u,j]=-rr[i,v]
    dp=DomainMatrix.from_Matrix(p).convert_to(field)
    assert (dp*source.transpose()).is_zero_matrix
    # Each coordinate remains valid at every r!=1, conditional on AS4 dimension.
    maxpower=0
    for entry in dp.to_dok().values():
        den=entry.denom
        factor=den.ring.from_expr(field.symbols[0]-1)
        power=0
        while den.degree()>0:
            quo,rem=divmod(den,factor);assert not rem
            den=quo;power+=1
        maxpower=max(maxpower,power)
    return free,p,maxpower


def main():
    start=time.monotonic();l,r=S.symbols('lambda r')
    R,A=source_matrix(l,pvalues(l,r));w=R*A*R.T
    assert all(S.cancel(S.expand(w[IX[v[:2]],IX[v[2:]]]+w[IX[v[1:3]],IX[(v[3],v[0])]]))==0 for v in words(4))
    print('PASS all-parameter P anti-cyclic tensor',flush=True)
    R,A=source_matrix(S.Integer(2),pvalues(S.Integer(2),r))
    rels=[{v:S.cancel(R[k,j]) for k,v in enumerate(W2) if R[k,j]} for j in range(6)]
    field=S.QQ_I.frac_field(r)
    f3,p3,d3=projection(rels,3,field);assert len(f3)==20
    print('PASS P lambda2 degree3 all-relation coordinates',flush=True)
    f4,p4,d4=projection(rels,4,field);assert len(f4)==35
    print('PASS P lambda2 degree4 all-relation coordinates',flush=True)
    ix={v:j for j,v in enumerate(words(4))};matrix=S.zeros(140,20)
    for j,k in enumerate(f3):
        v=words(3)[k]
        for i in range(4):matrix[35*i:35*(i+1),j]=p4[:,ix[v+(i,)]]-p4[:,ix[(i,)+v]]
    matrix=matrix.applyfunc(S.cancel)
    dm=DomainMatrix.from_Matrix(matrix).convert_to(field)
    rr,rows=dm.transpose().rref();assert len(rows)==20
    print('PASS P lambda2 generic centre rank20',flush=True)
    determinant=dm.extract(list(rows),list(range(20))).det()
    Q=(130-195*S.I)*r**3+(-2046+785*S.I)*r**2+(6646+1255*S.I)*r-5242-4405*S.I
    constant=-S.Rational(371293,66483263599150104576)-S.Rational(371293,531866108793200836608)*S.I
    delta=field.from_sympy(Q/(r-1)**5)
    assert determinant==field.from_sympy(constant)*delta
    common=delta.numer;selected=[]
    for (i,j),entry in rr.to_dok().items():
        if j in rows:continue
        minor=delta*entry;g=common.gcd(minor.numer)
        if g.degree()<common.degree():
            selected.append({'replace_slot':i,'row':j,'polynomial':str(minor.numer.as_expr()),'denominator':str(minor.denom.as_expr())})
            common=g
        if common.degree()==0:break
    assert common.degree()==0
    # Every chosen numerator is a genuine maximal minor up to a fixed scalar
    # and a power of r-1. Their gcd=1 gives an all-closed-value rank cover.
    cert={'version':'classification-v75','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source_presentation':'CY_ZERO_COMMUTATORS_FOUR_SIMPLE_FULL_SHARED_INVERTIBLE_REDUCTION.tex FT2-FT3',
          'universal_P_anti_cyclic_tensor':True,'lambda':2,'free_columns_3':f3,'free_columns_4':f4,
          'projection_denominator_maxpowers_r_minus1':[d3,d4],
          'centre_minor_rows':list(rows),'centre_minor_constant':str(constant),
          'centre_minor_polynomial':str(Q),'centre_minor_denominator':'(r-1)^5',
          'replacement_minors':selected,'maximal_minor_numerator_gcd':str(common.as_expr()),
          'scope':'All allowed r on lambda=2 slice excluded; nonempty determinant open of full P parameter plane excluded by openness conditional AS4. Not all P, all four-simple, or all CY coverage.',
          'coefficient_field':'QQ(i)(r); universal tensor checked over QQ(i)(lambda,r)'}
    Path(__file__).with_name('cubic_as4_four_simple_p_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS all P lambda2 centre3 zero; universal nonempty determinant open, seconds',round(time.monotonic()-start,3),flush=True)

if __name__=='__main__':main()
