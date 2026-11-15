#!/usr/bin/env python3
"""Exact arithmetic checks for the Nakayama restriction and non-CY sign example.

The general classification restriction and categorical/domain proofs are in TeX;
these finite checks do not replace them or classify all H3 surfaces.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product, permutations
import json
from pathlib import Path
from verify_cubic_skew_strata import pbw_product, exact_rank, multiplication_rank, matrix

D3=[a for a in product(range(4),repeat=4) if sum(a)==3]
D4=[a for a in product(range(5),repeat=4) if sum(a)==4]
EDGES=list(combinations(range(4),2))


def qmatrix(values):
    q=[[Fraction(1) for _ in range(4)] for _ in range(4)]
    for (i,j),x in zip(EDGES,values):
        q[i][j]=Fraction(x);q[j][i]=1/Fraction(x)
    return q


def canonical_character(q,a):
    return tuple(prod_fraction(q[i][j] for j in range(4))*
                 prod_fraction(q[j][i]**a[j] for j in range(4)) for i in range(4))


def prod_fraction(values):
    out=Fraction(1)
    for x in values:out*=x
    return out


def pencil_rank(q,c):
    m=[prod_fraction(row) for row in q]
    rows=[[Fraction(0) for _ in D3] for _ in range(140)]
    index={a:i for i,a in enumerate(D4)}
    for col,a in enumerate(D3):
        for i in range(4):
            unit=tuple(int(i==j) for j in range(4))
            v,s=pbw_product(q,a,unit);rows[35*i+index[v]][col]+=s
            v,s=pbw_product(q,unit,a);rows[35*i+index[v]][col]-=c*s/m[i]
    return exact_rank(rows)


def main():
    q=qmatrix([1,-1,-1,-1,-1,-1])
    m=[prod_fraction(row) for row in q]
    assert m==[1,1,-1,-1]
    support=[(3,0,0,0),(0,3,0,0),(1,0,2,0),(0,1,0,2)]
    assert all(canonical_character(q,a)==(1,)*4 for a in support)
    W1=[a for a in D3 if canonical_character(q,a)==(1,)*4]
    assert len(W1)==8
    degree1=[tuple(int(i==j) for j in range(4)) for i in range(4)]
    chars1=[tuple(prod_fraction(q[j][i]**a[j] for j in range(4)) for i in range(4)) for a in degree1]
    assert chars1[0]==chars1[1] and len(set(chars1))==3
    a,b,c,d=1,1,2,3
    delta=b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
    assert delta==-175 and a*d*delta and d*b**3!=a*c**3
    weights=[[3,2,1,0],[0,1,2,3],[-1,-1,-1,-1]]
    assert exact_rank([[Fraction(x) for x in row] for row in weights])==2
    for exponent in [(1,-2,1,0),(0,1,-2,1)]:
        assert all(sum(x*y for x,y in zip(row,exponent))==0 for row in weights)
    assert tuple(reversed((1,-2,1,0)))==(0,1,-2,1)
    assert multiplication_rank(q,support)==4
    assert pencil_rank(q,Fraction(1))==12
    assert pencil_rank(q,Fraction(-1))==20

    gamma=list(product(range(2),repeat=3))
    add=lambda a,b:tuple((x+y)%2 for x,y in zip(a,b))
    cocycle=lambda a,b:(-1)**(a[1]*b[0]+a[2]*b[0]+a[2]*b[1])
    for a,b,c in product(gamma,repeat=3):
        assert cocycle(a,b)*cocycle(add(a,b),c)==cocycle(b,c)*cocycle(a,add(b,c))
    degrees=[(1,0,0),(1,0,0),(0,1,0),(0,0,1)]
    for i,j in EDGES:
        assert Fraction(cocycle(degrees[i],degrees[j]),cocycle(degrees[j],degrees[i]))==q[i][j]
    for a in support:
        deg=(0,0,0);scalar=1
        for i in range(4):
            for _ in range(a[i]):
                scalar*=cocycle(deg,degrees[i]);deg=add(deg,degrees[i])
        assert deg==(1,0,0) and scalar==1

    # Ore-chart substitution, including negative exponents, in the Laurent PBW ring.
    def multiply(f,g):
        out={}
        for a,x in f.items():
            for b,y in g.items():
                v,c=pbw_product(q,a,b);out[v]=out.get(v,0)+x*y*c
        return {a:c for a,c in out.items() if c}
    def power(f,n):
        out={(0,0,0,0):Fraction(1)}
        for _ in range(n):out=multiply(out,f)
        return out
    y={(1,-1,0,0):Fraction(1)}
    u={(0,-1,1,0):Fraction(-1)}
    v={(0,-1,0,1):Fraction(-1)}
    uv=multiply(u,v);vu=multiply(v,u)
    assert uv=={a:-c for a,c in vu.items()}
    assert multiply(y,u)==multiply(u,y) and multiply(y,v)==multiply(v,y)
    chart=power(y,3)
    chart[(0,0,0,0)]=Fraction(1)
    for term in [multiply(y,power(u,2)),power(v,2)]:
        for a,c in term.items():chart[a]=chart.get(a,0)-c
    assert chart==multiply({a:Fraction(1) for a in support},{(0,-3,0,0):Fraction(1)})

    # Exponent arithmetic in roots of unity over characteristic zero.
    # No finite-field algebra is being lifted to characteristic zero here.
    torsion=[]
    for exponent in product(range(3),repeat=3):
        e=matrix(*exponent);blocks=Counter()
        for a in D3:
            char=tuple(-sum(e[i][j]*a[j] for j in range(4))%3 for i in range(4))
            blocks[char]+=1
            scalar=len(set(char))==1
            assert not scalar or char==(0,0,0,0)
        torsion.append({'parameter':exponent,'all_normal_cubic_monomials':20,
                        'anticanonical_candidate_dimension':blocks[(0,0,0,0)]})
    generic=qmatrix([2,3,5,7,11,13])
    assert all(len(set(canonical_character(generic,a)))>1 for a in D3)
    assert pencil_rank(generic,Fraction(1))==20

    permuted={tuple(q[p[i]][p[j]] for i,j in EDGES) for p in permutations(range(4))}
    assert len(permuted)==6
    cert={'date':'2026-11-15','scope':'Nakayama linear candidate incidence and explicit non-CY H3 example',
          'noncy_q_upper':[1,-1,-1,-1,-1,-1], 'nakayama_B':[1,1,-1,-1],
          'G_support':support,'W1_monomials':W1,'W1_dimension':8,
          'smooth_generic_stabilizer_witness':{'binary_coefficients':[1,1,2,3], 'discriminant':delta, 'projective_stabilizer_order':4},
          'fixed_ambient_generic_quotient_dimension':2,
          'pencil_ranks':{'c=1':12,'c=-1':20},'normal_multiplication_rank':4,
          'cocycle_triples_checked':512,'coordinate_permutation_orbit_size':6,
          'ore_chart':'uv=-vu; y central; v^2+y*u^2-y^3-1=0',
          'torsion_27_central_only':torsion,'generic_rational_W1_dimension':0,
          'proofs_not_replaced_by_calculation':['Serre scalar detection','AS-index-one scalar triviality with an explicit epsilon object',
              'CY centrality','smoothness via finite equivariant cocycle twist',
              'quaternion division via odd valuation of non-norm','Gabriel--Krull rank and AZ conditions'],
          'not_claimed':['all ambient coverage','intrinsic groupoid classification','independent peer review','exhaustive novelty audit']}
    Path(__file__).with_name('cubic_nakayama_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: exact Nakayama pencils, non-CY normal cubic, 512 cocycle identities, Laurent chart, 27 central-only restrictions')

if __name__=='__main__':main()
