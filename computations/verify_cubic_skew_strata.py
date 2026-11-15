#!/usr/bin/env python3
"""Exact 27-point coordinate-permutation classification, not categorical classification."""
from __future__ import annotations
import itertools as it
import json
from pathlib import Path
from math import comb

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

def main():
    perms=list(it.permutations(range(4)))
    matrices={matrix(*u):u for u in it.product(range(3),repeat=3)}
    monomials=[v for v in it.product(range(4),repeat=4) if sum(v)==3]
    assert len(matrices)==27 and len(monomials)==20
    reps=[(0,0,0),(0,0,1),(0,1,1),(0,1,2)]
    sizes=[1,8,12,6]; center_dims=[20,5,6,4]
    covered=set();records=[];our=matrix(1,1,0)
    for u,size,zd in zip(reps,sizes,center_dims):
        e=matrix(*u);orb={permute(e,p) for p in perms}
        stab=[p for p in perms if permute(e,p)==e]
        center=[v for v in monomials if central(e,v)]
        assert len(orb)==size and len(stab)*size==24
        assert len(center)==zd and not (covered&orb) and orb<=matrices.keys()
        covered|=orb
        records.append({"representative":u,"orbit_size":size,
                        "coordinate_stabilizer_order":len(stab),
                        "orbit_parameters":sorted(matrices[x] for x in orb),
                        "central_degree_three_monomials":center,
                        "central_degree_three_dimension":len(center),
                        "contains_non_AS_Fermat_example":our in orb})
    assert covered==matrices.keys()
    b=lambda n:comb(n+3,3) if n>=0 else 0
    h=lambda n:b(n)-b(n-3)
    assert (b(3),h(3),b(4),h(4))==(20,19,35,31)
    assert all(h(n)==1+3*n*(n+1)//2 for n in range(16))
    cert={"version":"classification-v1","date":"2026-11-15",
          "field":"F3 exponent arithmetic; characteristic-zero quantum algebras",
          "parameters":27,"coordinate_permutations":24,"orbits":records,
          "principal_recognition_dimensions":{"B3":20,"R3":19,"B4":35,"R4":31},
          "normal_cubic_incidence_matrix":[35,8],"minor_size":5,
          "scope":"Finite coordinate-permutation classification only. Other proofs are in the manuscript."}
    Path(__file__).with_name("cubic_skew_strata_certificate.json").write_text(
        json.dumps(cert,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("PASS: 27 parameters, orbit sizes 1/8/12/6, center dimensions 20/5/6/4")
if __name__=="__main__":main()
