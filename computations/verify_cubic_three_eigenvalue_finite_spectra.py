#!/usr/bin/env python3
"""Exhaust necessary three-eigenvalue H3 spectra through degree three.
Ordinary inputs: common order <=24, resonance/pencil exclusions, Frobenius
reciprocity, rank-one-free relation bounds, and equivariant Koszul resolution.
Survival is not AS4 existence or H3 admissibility. No floating point arithmetic.
"""
import itertools
import json
from collections import Counter
from math import gcd
from pathlib import Path

CUBIC = [v for v in itertools.product(range(4),repeat=3) if sum(v)==3]
QUARTIC = [v for v in itertools.product(range(5),repeat=3) if sum(v)==4]
MULT = (2,1,1)

def convolution(x,y):
    N=len(x)
    return [sum(x[j]*y[(i-j)%N] for j in range(N)) for i in range(N)]

def relation_options(N,lam):
    dims=Counter(); segregation={}
    for i in range(3):
        for j in range(3):
            w=(lam[i]+lam[j])%N
            dims[w]+=MULT[i]*MULT[j]
            segregation[w]=max(segregation.get(w,0),MULT[i]+MULT[j]-1)
    cap={w:dims[w]-segregation[w] for w in dims}
    options=[];seen=set()
    for w in sorted(dims):
        if w in seen:continue
        inv=(-w)%N;seen.update([w,inv])
        options.append([(w,inv,r) for r in range(min(cap[w],cap.get(inv,0))+1)])
    for choice in itertools.product(*options):
        rel=[0]*N
        for w,inv,r in choice:rel[w]=rel[inv]=r
        if sum(rel)==6:yield rel

def degree_three_test(N,lam,rel):
    V=[0]*N
    for w,m in zip(lam,MULT):V[w]+=m
    invV=[V[(-w)%N] for w in range(N)]
    one=[1]+[0]*(N-1)
    B2=[x-y for x,y in zip(convolution(V,V),rel)]
    B3=[x-2*y+z for x,y,z in zip(convolution(convolution(V,V),V),convolution(V,rel),invV)]
    R3=[x-y for x,y in zip(B3,one)]
    rows=[one,V,B2,R3]
    for degree,row in enumerate(rows):
        for w,value in enumerate(row):
            if value<0:return {'kind':'negative_dimension','degree':degree,'weight':w,'value':value}
    for degree in range(3):
        for linear in lam:
            for w,value in enumerate(rows[degree]):
                if value>rows[degree+1][(w+linear)%N]:
                    return {'kind':'linear_multiplication_not_injective','source_degree':degree,
                            'source_weight':w,'linear_weight':linear,'source_dimension':value,
                            'target_dimension':rows[degree+1][(w+linear)%N]}
    return None

survivors=[];failures=[];stages=Counter();assignments=0
for N in range(3,25):
    for a in range(N):
        for b,c in itertools.combinations(range(N),2):
            if a in (b,c) or gcd(gcd(gcd(N,a),b),c)!=1:continue
            stages['minimal_order_distinct']+=1
            lam=(a,b,c)
            cub=[v for v in CUBIC if sum(x*y for x,y in zip(v,lam))%N==0]
            if not cub:continue
            if len(cub)==1 and any(cub[0][i]==3 and MULT[i]==1 for i in range(3)):continue
            stages['cubic_and_no_isolated_simple_cube']+=1
            if any(not any(v[i] and sum(x*y for x,y in zip(v,lam))%N==0 for v in QUARTIC) for i in range(3)):continue
            stages['quartic_support_all_eigenspaces']+=1
            quadratic=[(2*a)%N,(a+b)%N,(a+c)%N,(2*b)%N,(b+c)%N,(2*c)%N]
            if len(set(quadratic))==6:continue
            if N>4 and ((a==0 and (b+c)%N==0) or (b==0 and (a+c)%N==0) or (c==0 and (a+b)%N==0)):continue
            stages['quadratic_resonance_and_pencil_exclusions']+=1
            accepted=[]
            for rel in relation_options(N,lam):
                assignments+=1
                failure=degree_three_test(N,lam,rel)
                if failure is None:accepted.append(rel)
                else:failures.append({'N':N,'spectrum':lam,'relations':rel,'witness':failure})
            if accepted:survivors.append({'N':N,'spectrum':lam,'relation_weight_multiplicities':accepted})
counts=Counter(row['N'] for row in survivors)
assert counts=={3:3,4:12,5:4,6:11,9:6,12:2}
assert len(survivors)==38 and sum(len(x['relation_weight_multiplicities']) for x in survivors)==42
pool={(row['N'],*row['spectrum']) for row in survivors};orbits=[]
while pool:
    N,a,b,c=min(pool)
    orbit={(N,u*a%N,*sorted([u*b%N,u*c%N])) for u in range(1,N) if gcd(u,N)==1}
    assert orbit<=pool
    pool-=orbit
    orbits.append({'representative':[N,a,b,c],'members':sorted(orbit)})
assert len(orbits)==18 and assignments==99 and len(failures)==57
result={'status':'PASS','scope':'exhaustive necessary finite character filter only; not AS4 existence or H3 admissibility',
        'maximum_common_order_input':24,'maximum_checked_internal_degree':3,
        'multiplicities':MULT,'stage_counts':dict(stages),'tested_relation_assignments':assignments,
        'survivor_count':len(survivors),'relation_pattern_count':42,'counts_by_order':dict(sorted(counts.items())),
        'survivors':survivors,'Galois_label_orbits':orbits,'excluded_relation_pattern_witnesses':failures,
        'not_claimed':['Galois conjugacy is k-linear equivalence','all degrees verified','H3 existence of surviving spectra']}
Path(__file__).with_name('cubic_three_eigenvalue_finite_spectra_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','spectra':38,'relation_patterns':42,'Galois_label_orbits':18,'counts_by_order':dict(sorted(counts.items()))}))
