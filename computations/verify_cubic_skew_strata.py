#!/usr/bin/env python3
"""Exact 27-point coordinate-permutation classification, not categorical classification."""
from __future__ import annotations
import itertools as it
import json
from pathlib import Path
from math import comb, prod
from collections import defaultdict, Counter
from fractions import Fraction

def matrix(a,b,c):
    e=[[0]*4 for _ in range(4)]
    vals={(0,1):a,(0,2):b,(0,3):-a-b,(1,2):c,(1,3):a-c,(2,3):b+c}
    for (i,j),v in vals.items(): e[i][j],e[j][i]=v%3,-v%3
    assert all(sum(row)%3==0 for row in e)
    return tuple(map(tuple,e))

def permute(e,p):
    return tuple(tuple(e[p[i]][p[j]] for j in range(4)) for i in range(4))

def central(e,v):
    return all(sum(e[i][j]*v[j] for j in range(4))%3==0 for i in range(4))

def pbw_product(q,a,b):
    scalar=Fraction(1)
    for j in range(4):
        for i in range(j):
            scalar*=q[j][i]**(a[j]*b[i])
    return tuple(x+y for x,y in zip(a,b)),scalar

def exact_rank(rows):
    rows=[list(row) for row in rows];pivot=0
    for j in range(len(rows[0])):
        p=next((i for i in range(pivot,len(rows)) if rows[i][j]),None)
        if p is None: continue
        rows[pivot],rows[p]=rows[p],rows[pivot]
        divisor=rows[pivot][j]
        rows[pivot]=[x/divisor for x in rows[pivot]]
        for i in range(pivot+1,len(rows)):
            c=rows[i][j]
            if c: rows[i]=[x-c*y for x,y in zip(rows[i],rows[pivot])]
        pivot+=1
    return pivot

def multiplication_rank(q,support):
    degree4=[v for v in it.product(range(5),repeat=4) if sum(v)==4]
    index={v:i for i,v in enumerate(degree4)}
    rows=[[Fraction(0) for _ in range(8)] for _ in degree4]
    for a in support:
        for i in range(4):
            unit=tuple(int(i==j) for j in range(4))
            v,c=pbw_product(q,a,unit);rows[index[v]][i]+=c
            v,c=pbw_product(q,unit,a);rows[index[v]][4+i]+=c
    return exact_rank(rows)

def main():
    perms=list(it.permutations(range(4)))
    matrices={matrix(*u):u for u in it.product(range(3),repeat=3)}
    monomials=[v for v in it.product(range(4),repeat=4) if sum(v)==3]
    assert len(matrices)==27 and len(monomials)==20
    reps=[(0,0,0),(0,0,1),(0,1,1),(0,1,2)]
    sizes=[1,8,12,6]; center_dims=[20,5,6,4]
    block_sizes=[[20],[5,3,3,2,2,2,1,1,1],
                 [6,3,3,2,2,2,1,1],[4,2,2,2,2,2,2,2,2]]
    covered=set();records=[];our=matrix(1,1,0)
    for u,size,zd,expected_blocks in zip(reps,sizes,center_dims,block_sizes):
        e=matrix(*u);orb={permute(e,p) for p in perms}
        stab=[p for p in perms if permute(e,p)==e]
        center=[v for v in monomials if central(e,v)]
        assert len(orb)==size and len(stab)*size==24
        assert len(center)==zd and not (covered&orb) and orb<=matrices.keys()
        blocks=defaultdict(list)
        for v in monomials:
            character=tuple(-sum(e[i][j]*v[j] for j in range(4))%3 for i in range(4))
            blocks[character].append(v)
            # Direct ordered-PBW products x^v*x_i and x_i*x^v.
            for i in range(4):
                right=sum(v[j]*e[j][i] for j in range(i+1,4))%3
                left=sum(v[j]*e[i][j] for j in range(i))%3
                assert (right-left)%3==character[i]
        assert sorted(map(len,blocks.values()),reverse=True)==expected_blocks
        covered|=orb
        records.append({"representative":u,"orbit_size":size,
                        "coordinate_stabilizer_order":len(stab),
                        "orbit_parameters":sorted(matrices[x] for x in orb),
                        "central_degree_three_monomials":center,
                        "central_degree_three_dimension":len(center),
                        "normal_cubic_character_blocks":[
                            {"character_exponents":c,"monomials":v,
                             "projective_dimension":len(v)-1}
                            for c,v in sorted(blocks.items())],
                        "normal_component_vector_dimensions":expected_blocks,
                        "contains_non_AS_Fermat_example":our in orb})
    assert covered==matrices.keys()
    b=lambda n:comb(n+3,3) if n>=0 else 0
    h=lambda n:b(n)-b(n-3)
    assert (b(3),h(3),b(4),h(4))==(20,19,35,31)
    assert all(h(n)==1+3*n*(n+1)//2 for n in range(16))
    # An exact characteristic-zero point off all cubic character collisions.
    q=[[Fraction(1) for _ in range(4)] for _ in range(4)]
    for (i,j),prime in zip(it.combinations(range(4),2),[2,3,5,7,11,13]):
        q[i][j]=Fraction(prime);q[j][i]=Fraction(1,prime)
    chars=[tuple(prod(q[j][i]**v[j] for j in range(4)) for i in range(4))
           for v in monomials]
    assert len(set(chars))==20 and (Fraction(1),)*4 not in chars
    assert all(multiplication_rank(q,[v])==4 for v in monomials)
    pair_ranks=[multiplication_rank(q,[a,b]) for a,b in it.combinations(monomials,2)]
    assert len(pair_ranks)==190 and min(pair_ranks)>4
    assert multiplication_rank(q,monomials)>4
    cert={"version":"classification-v2","date":"2026-11-15",
          "field":"F3 exponent arithmetic; characteristic-zero quantum algebras",
          "generic_rational_witness_q_upper":[2,3,5,7,11,13],
          "generic_witness_distinct_characters":20,
          "exact_QQ_multiplication_checks":{"monomial_rank4":20,
              "two_term_rank_above4":190,"two_term_rank_counts":dict(Counter(pair_ranks))},"parameters":27,"coordinate_permutations":24,"orbits":records,
          "principal_recognition_dimensions":{"B3":20,"R3":19,"B4":35,"R4":31},
          "normal_cubic_incidence_matrix":[35,8],"minor_size":5,
          "scope":"Finite coordinate-permutation classification only. Reduced normal cubic character blocks also enumerated; no intrinsic quotient classification or scheme reducedness claim. Other proofs are in the manuscript."}
    Path(__file__).with_name("cubic_skew_strata_certificate.json").write_text(
        json.dumps(cert,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("PASS: 27 parameters, orbit sizes 1/8/12/6, center dimensions 20/5/6/4; all normal character blocks; generic rational witness")
if __name__=="__main__":main()
