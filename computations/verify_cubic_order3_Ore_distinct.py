#!/usr/bin/env python3
"""Exact necessary-model computation; this does not establish AS3 or H3 existence."""
import itertools
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.rings import ring


def main():
    two_weight_cases=[]
    for rho in [3,6]:
        roots=[b for b in range(9) if 3*b%9==(-rho)%9]
        assert len(roots)==3
        assert all((-6*b)%9 for b in roots)
        for b in roots:
            c=(-2*b)%9
            assert c in roots and c!=b
            assert (rho+2*c)%9==(-c)%9
            assert S.gcd(b,9)==1 and c!=0
            two_weight_cases.append([rho,b,c])
    M=S.Matrix([[0,-1],[1,-1]])
    N=-M.T*M.inv()
    z=S.Symbol('z')
    assert N.charpoly(z).as_expr()==(z-1)**2 or S.expand(N.charpoly(z).as_expr()-(z-1)**2)==0
    t=S.Symbol('t')
    K=S.QQ.algebraic_field(S.CRootOf(t**6+t**3+1,0))
    a=K.unit
    mu=[a**2,a**5,a**8]
    sigma=[a**8,a**2,a**5]
    assert all(s**3==a**6 for s in sigma)
    assert all(m==s**-2 for m,s in zip(mu,sigma))
    w={}
    for i in range(3):
        j=(i+1)%3
        w[i,i,j]=K.one
        w[i,j,i]=mu[i]
        w[j,i,i]=mu[i]**2
    assert all(mu[i]*mu[j]*mu[k]==K.one for i,j,k in w)
    assert all(sigma[i]*sigma[j]*sigma[k]==K.one for i,j,k in w)
    rel=[{word[1:]:c for word,c in w.items() if word[0]==i} for i in range(3)]
    # Literal Type E presentation in LBS (1996), page186, not an atlas import.
    source_root=a**2
    source_relations=[
        {(2,0):K.one,(0,2):source_root**8,(1,1):source_root**4},
        {(0,1):K.one,(1,0):source_root**5,(2,2):source_root**7},
        {(0,0):source_root,(1,2):K.one,(2,1):source_root**2},
    ]
    perm=[0,2,1]
    scales=[K.one,K.one,a**3]
    for src,target,factor in zip(source_relations,[rel[0],rel[2],rel[1]],[a,a,a**7]):
        transformed={(perm[i],perm[j]):c*scales[i]*scales[j] for (i,j),c in src.items()}
        assert transformed=={word:factor*c for word,c in target.items()}
    # Both first and last slices define exactly the same quadratic relation space.
    for i in range(3):
        last={word[:2]:c for word,c in w.items() if word[2]==i}
        assert last=={word:mu[i]*c for word,c in rel[i].items()}

    dimensions={}
    def quotient(d):
        words=list(itertools.product(range(3),repeat=d))
        inds={word:i for i,word in enumerate(words)}
        rows=[]
        for pos in range(d-1):
            for pre in itertools.product(range(3),repeat=pos):
                for post in itertools.product(range(3),repeat=d-2-pos):
                    for r in rel:
                        rows.append({inds[pre+word+post]:c for word,c in r.items()})
        D=DomainMatrix({i:row for i,row in enumerate(rows) if row},(len(rows),len(words)),K)
        rr,piv=D.rref()
        rd=rr.to_dod()
        free=[i for i in range(len(words)) if i not in piv]
        fi={k:i for i,k in enumerate(free)}
        pi={p:i for i,p in enumerate(piv)}
        dimensions[str(d)]=len(free)
        def project(word):
            k=inds[word]
            if k in pi:
                return {fi[j]:-c for j,c in rd[pi[k]].items() if j in fi}
            return {fi[k]:K.one}
        return [words[k] for k in free],project

    quotient(2)
    basis3,p3=quotient(3)
    basis4,p4=quotient(4)
    assert dimensions=={'2':6,'3':10,'4':15}
    # Weight-one monomials span the entire sigma-fixed cubic subspace.
    candidates=[word for word in basis3 if sigma[word[0]]*sigma[word[1]]*sigma[word[2]]==K.one]
    assert candidates==[(1,1,2),(1,2,1),(2,1,1),(2,2,0)]
    C={}
    for col,word in enumerate(candidates):
        row={}
        for i in range(3):
            for ww,c in [(word+(i,),K.one),((i,)+word,-a**6)]:
                for j,d in p4(ww).items():
                    k=len(basis4)*i+j
                    row[k]=row.get(k,K.zero)+c*d
        C[col]={j:c for j,c in row.items() if c}
    D=DomainMatrix(C,(4,3*len(basis4)),K)
    assert D.rank()==3
    kernel=D.transpose().nullspace().to_list()
    assert len(kernel)==1 and kernel[0][-1]
    vector=[c/kernel[0][-1] for c in kernel[0]]
    expected=[-a**4+a-2,-a**5+2*a**4-2*a**3+a-1,a**3-a+2,K.one]
    assert vector==expected
    for col in range(3*len(basis4)):
        assert sum((vector[i]*C[i].get(col,K.zero) for i in range(4)),K.zero)==K.zero
    # All four cubic normal-form coefficients are nonzero.
    assert all(vector)
    # Universal Ore norm identity over a quadratic algebraic parameter.
    # This proves non-domain of the remaining cubic cuts, without AS3 sufficiency.
    PU,U=ring('U',K)
    d=a**5-a**4-a**2-2*a
    e=a**5-a**4+2*a**2+a
    h=a**5-a**4+a**3-a+1
    j=a**4+a**2
    k=a**5+a
    qU=U**2-(h*d+k)*U+h
    xU=1-(d+e)*U
    wU=(a**4+a)*xU+(a**5-a**3-a-1)*U**2
    assert h*e+j==k
    assert not (U**3-d*(d+e)*U**2+(2*d+e)*U-1).rem(qU)
    assert qU.gcd(xU)==PU.one and qU.gcd(wU)==PU.one
    assert qU.gcd(qU.diff(U))==PU.one and h
    PB,b,c=ring('b,c',K)
    coeff=[PB.one,b,c]
    norm=[PB.zero for _ in basis3]
    for word in itertools.product(range(3),repeat=3):
        i,jj,kk=word
        co=coeff[i]*coeff[jj]*coeff[kk]*sigma[i]**2*sigma[jj]
        for ix,vv in p3(word).items():
            norm[ix]+=co*vv
    fvector=[K.zero]*len(basis3)
    for word,co in zip(candidates,vector):
        fvector[basis3.index(word)]=co
    # Substitute c=U/b, b^3=X(U), Q(U)=0 after clearing b^3.
    for f,target in zip(norm,fvector):
        residues=[PU.zero,PU.zero,PU.zero]
        for (ib,ic),co in f.terms():
            power=3+ib-ic
            assert power>=0
            residues[power%3]+=co*U**ic*xU**(power//3)
        residues[1]-=wU*target
        assert all(not f.rem(qU) for f in residues)
    # Ore expansion (t²+sigma²(L)t+sigma²(L)sigma(L))(t-L)
    # has coefficients 1,0,0,-sigma²(L)sigma(L)L by direct multiplication.
    inertia_matrix=S.Matrix([[1,-2,0],[1,1,0],[-2,1,0],[2,1,-3]])
    snf=smith_normal_form(inertia_matrix,domain=S.ZZ)
    assert [abs(snf[i,i]) for i in range(3)]==[1,1,9]
    inertia_weights=[0,3,6,1]
    for r in rel:
        assert len({sum(inertia_weights[i] for i in word)%9 for word in r})==1
    assert {sum(inertia_weights[i] for i in word)%9 for word in candidates}=={3}
    assert 3*inertia_weights[3]%9==3
    # Degree-zero localization at the normal Ore variable uses S^(sigma^-1).
    rel=[
        {(0,1):K.one,(1,0):a**8,(2,2):a},
        {(0,0):a**7,(1,2):K.one,(2,1):a**2},
        {(1,1):a**4,(2,0):K.one,(0,2):a**5},
    ]
    affine_basis4,affine_p4=quotient(4)
    central_coefficients=[c*sigma[word[1]]*sigma[word[2]]**2
                          for word,c in zip(candidates,vector)]
    assert central_coefficients==[a**3*vector[0],vector[1],a**6*vector[2],a**3]
    for i in range(3):
        residual=[K.zero]*len(affine_basis4)
        for word,c in zip(candidates,central_coefficients):
            for ww,sign in [(word+(i,),1),((i,)+word,-1)]:
                for j,d in affine_p4(ww).items():
                    residual[j]+=sign*c*d
        assert not any(residual)
    data={
        'field':'QQ[a]/(a^6+a^3+1)',
        'final_H3_result':'All two-eigenvalue order-three H3 excluded; only {1,-1} can remain among exactly two Nakayama eigenvalues.',
        'sigma_exponents':[8,2,5],
        'classical_Type_E_source':'Le Bruyn-Smith-Van den Bergh (1996), page186',
        'classical_Type_E_map':'zeta9=a^2; (X1,X2,X3)=(x,z,a^3*y); (f1,f2,f3)=(a*r1,a*r3,a^7*r2)',
        'mu_S_exponents':[2,5,8],
        'quadratic_relations':'xy+a^2*yx+a^7*z^2; a^4*x^2+yz+a^5*zy; a*y^2+zx+a^8*xz',
        'quotient_dimensions':dimensions,
        'sigma_fixed_cubic_dimension':4,
        'normality_map_rank':3,
        'normal_cubic_dimension':1,
        'Ore_norm_exclusion':{
            'd':'a^5-a^4-a^2-2*a',
            'e':'a^5-a^4+2*a^2+a',
            'h':'a^5-a^4+a^3-a+1',
            'k':'a^5+a',
            'Q':'U^2-(h*d+k)*U+h',
            'X':'1-(d+e)*U',
            'W':'(a^4+a)*X+(a^5-a^3-a-1)*U^2',
            'parameters':'Q(u)=0; b^3=X(u); c=u/b; ell=x+b*y+c*z',
            'identity':'sigma^2(ell)*sigma(ell)*ell = b*W(u)/X(u)*F0',
            'nonzero':'gcd(Q,X)=gcd(Q,W)=1',
            'conclusion':'Scale ell to L with norm(L)=-F0; then t^3+F0=(t^2+sigma^2(L)*t+sigma^2(L)*sigma(L))*(t-L). No H3 candidate survives.'
        },
        'two_eigenvalue_weight_cases_mu9':two_weight_cases,
        'Jordan_plane_Nakayama_eigenvalues':[1,1],
        'projective_candidate_inertia_Smith_diagonal':[1,1,9],
        'projective_candidate_inertia_mu9_weights':inertia_weights,
        'normal_Ore_affine_chart':'S_(a^4)/(C+1)',
        'central_affine_cubic_coefficient_multipliers':['a^3','1','a^6','a^3'],
        'F_words':['yyz','yzy','zyy','zzx'],
        'F_coefficients':['-a^4+a-2','-a^5+2*a^4-2*a^3+a-1','a^3-a+2','1'],
        'scope':'Necessary model only. No all-degree AS3/noetherian/domain/H3 sufficiency assertion.'
    }
    path=Path(__file__).with_name('cubic_order3_Ore_distinct_certificate.json')
    if path.exists():
        assert json.loads(path.read_text())==data
    else:
        path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS exact quotients, top slices, cubic line, universal Ore norm factorisation, inertia and affine chart')


if __name__=='__main__':
    main()
