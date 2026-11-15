#!/usr/bin/env python3
"""Verify characteristic-zero integer lattice certificates and root-of-unity cases.

Default verification uses only the standard library. --regenerate additionally
uses SymPy 1.14 to rebuild the small unimodular Smith certificates.
The categorical coordinate-jet necessity is proved in the manuscript.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import json
from pathlib import Path

EDGES=list(combinations(range(4),2))
PERMS=list(permutations(range(4)))
D3=[a for a in product(range(4),repeat=4) if sum(a)==3]
CERT=Path(__file__).with_name('cubic_skew_jet_lattices.json')


def conjugate(f,p):
    inv=[p.index(i) for i in range(4)]
    return tuple(p[f[inv[i]]] for i in range(4))


def relation_matrix(f):
    rows=[]
    for u,j in enumerate(f):
        d=[2*int(t==u)+int(t==j)-1 for t in range(4)]
        for i in range(4):
            rows.append([d[a]*int(b==i)-d[b]*int(a==i) for a,b in EDGES])
    return rows


def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def determinant(a):
    a=[[Fraction(x) for x in row] for row in a];out=Fraction(1)
    for j in range(len(a)):
        p=next((i for i in range(j,len(a)) if a[i][j]),None)
        if p is None:return Fraction(0)
        if p!=j:a[j],a[p]=a[p],a[j];out=-out
        pivot=a[j][j];out*=pivot
        for i in range(j+1,len(a)):
            factor=a[i][j]/pivot
            for k in range(j,len(a)):a[i][k]-=factor*a[j][k]
    return out


def dense(sparse,n):
    out=[[0]*n for _ in range(n)]
    for i,j,x in sparse:
        assert isinstance(x,int) and out[i][j]==0
        out[i][j]=x
    return out


def regenerate():
    from sympy import Matrix,ZZ
    from sympy.polys.matrices import DomainMatrix
    from sympy.polys.matrices.normalforms import smith_normal_decomp
    remaining=set(product(range(4),repeat=4));records=[]
    for f in sorted(remaining):
        if f not in remaining:continue
        orb={conjugate(f,p) for p in PERMS};remaining-=orb
        dm=DomainMatrix.from_Matrix(Matrix(relation_matrix(f))).convert_to(ZZ)
        dd,uu,vv=smith_normal_decomp(dm)
        D,U,V=[x.to_Matrix() for x in [dd,uu,vv]]
        def sparse(m):
            return [[i,j,int(m[i,j])] for i in range(m.rows) for j in range(m.cols) if m[i,j]]
        diag=[int(D[i,i]) for i in range(6)]
        records.append({'pattern':f,'orbit_size':len(orb),'smith_diagonal':diag,
                        'annihilator':max(map(abs,diag)),
                        'left_unimodular_sparse':sparse(U),'right_unimodular_sparse':sparse(V)})
    cert={'date':'2026-11-15',
          'scope':'Integer Smith certificates for all 256 coordinate jet patterns, modulo 24 permutations',
          'matrix_shape':[16,6],'records':records}
    CERT.write_text(json.dumps(cert,separators=(',',':'))+'\n')


def matrix(values,n):
    e=[[0]*4 for _ in range(4)]
    for (i,j),v in zip(EDGES,values):e[i][j]=v;e[j][i]=-v%n
    return e


def candidate_support(values,n):
    e=matrix(values,n);m=[sum(row)%n for row in e]
    support=[a for a in D3 if all((m[i]-sum(e[i][j]*a[j] for j in range(4)))%n==0 for i in range(4))]
    return support,not any(m)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--regenerate',action='store_true')
    if parser.parse_args().regenerate:regenerate()
    cert=json.loads(CERT.read_text());covered=set();counts=Counter()
    for rec in cert['records']:
        f=tuple(rec['pattern']);orb={conjugate(f,p) for p in PERMS}
        assert len(orb)==rec['orbit_size'] and not covered&orb;covered|=orb
        U=dense(rec['left_unimodular_sparse'],16)
        V=dense(rec['right_unimodular_sparse'],6)
        assert abs(determinant(U))==abs(determinant(V))==1
        D=mul(mul(U,relation_matrix(f)),V)
        diag=rec['smith_diagonal']
        assert all(D[i][j]==(diag[i] if i==j and i<6 else 0) for i in range(16) for j in range(6))
        assert all(diag) and all(diag[i+1]%diag[i]==0 for i in range(5))
        n=rec['annihilator'];assert n in (1,2,3) and all(n%abs(x)==0 for x in diag)
        counts[tuple(map(abs,diag))]+=len(orb)
    assert covered==set(product(range(4),repeat=4)) and len(cert['records'])==19
    expected={(1,1,1,1,1,1):149,(1,1,1,1,1,2):84,(1,1,1,1,1,3):18,
              (1,1,1,2,2,2):4,(1,1,1,3,3,3):1}
    assert dict(counts)==expected

    records=[];gross_counts={};bad_counts={}
    for n in (2,3):
        good=[];bad=[];gross=0
        for values in product(range(n),repeat=6):
            support,cy=candidate_support(values,n)
            if not all(any(a[i]>=2 for a in support) for i in range(4)):continue
            gross+=1
            common=tuple(min(a[i] for a in support) for i in range(4))
            if any(common):
                bad.append(values);continue
            good.append(values)
            if n==3 and not any(values):continue # identity already in the order-two list
            records.append({'root_order':n if any(values) else 1,'q_exponents':values,
                            'CY':cy,'candidate_vector_dimension':len(support),'candidate_monomials':support})
        gross_counts[str(n)]=gross;bad_counts[str(n)]=len(bad)
        assert (gross,len(bad),len(good))==((23,12,11) if n==2 else (27,0,27))
        if n==3:assert all(not any(sum(row)%3 for row in matrix(v,3)) for v in good)
    assert len(records)==37
    orbit_records=[]
    for n in (2,3):
        available={tuple(r['q_exponents']) for r in records if r['root_order']==n}
        while available:
            values=min(available);e=matrix(values,n)
            orb={tuple(e[p[i]][p[j]]%n for i,j in EDGES) for p in PERMS}
            assert orb<=available
            available-=orb
            support,cy=candidate_support(values,n)
            orbit_records.append({'order':n,'representative':values,'orbit_size':len(orb),
                                  'CY':cy,'candidate_vector_dimension':len(support)})
    assert sorted(r['orbit_size'] for r in orbit_records)==[4,6,6,8,12]
    summary={'date':'2026-11-15','jet_patterns':256,'coordinate_orbits':19,
             'integer_smith_counts':[{'diagonal':k,'patterns':v} for k,v in sorted(counts.items())],
             'jet_parameter_counts':gross_counts,'common_factor_exclusions':bad_counts,
             'remaining_parameter_count':37,'nontrivial_coordinate_orbits':orbit_records,
             'parameters':records,
             'scope':'Necessary ambient list for H3 in the entire six-parameter skew polynomial torus; not sufficient. Further rank and smoothness conclusions are separately verified in cubic_skew_admissible_certificate.json.'}
    Path(__file__).with_name('cubic_skew_jet_certificate.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('PASS: 19 unimodular Smith certificates cover 256 patterns; 49 jet parameters; 12 common-factor exclusions; 37 candidates in six coordinate types')

if __name__=='__main__':main()
