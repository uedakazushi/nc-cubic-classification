"""Exact certificates for the remaining Jordan monic charts.
No finite sample is used for the nonsemisimple W branch.
"""
import itertools
import json
from pathlib import Path
import sympy as S

words=list(itertools.product(range(2),repeat=4));ix={w:i for i,w in enumerate(words)}
rel=[{(0,0,1):1,(0,1,0):-2,(1,0,0):1},
     {(1,1,0):1,(1,0,1):-2,(0,1,1):1,(0,0,0):-2}]
rows=[]
for r in rel:
    for g in range(2):
        for side in [0,1]:
            row=[0]*16
            for w,c in r.items():row[ix[((g,)+w) if side==0 else (w+(g,))]]=c
            rows.append(row)
E,piv=S.Matrix(rows).rref();free=[i for i in range(16) if i not in piv]
assert len(piv)==7 and len(free)==9
P=S.zeros(9,16)
for i,j in enumerate(free):P[i,j]=1
for i,j in enumerate(piv):
    for k,l in enumerate(free):P[k,j]=-E[i,l]
variables=S.symbols('d0 d1 d2 d3 e0 e1 e2 e3');quad=list(itertools.product(range(2),repeat=2))
ranks=[]
for signs,ids,inner in [([1,-1],[1,2,4,7],[-1,1,0,2]),([-1,1],[0,3,5,6],[2,0,1,-1])]:
    out=[]
    for rr in rel:
        v=S.zeros(16,1)
        for w,co in rr.items():
            for pos in range(3):
                scale=co*S.prod(signs[i] for i in w[:pos])
                for j,q in enumerate(quad):v[ix[w[:pos]+q+w[pos+1:]]]+=scale*variables[4*w[pos]+j]
        out.extend(P*v)
    M=S.linear_eq_to_matrix(out,variables)[0][:,ids]
    assert M.rank()==3 and M*S.Matrix(inner)==S.zeros(18,1)
    ranks.append(3)
# Centralizers for CY Jordan T: [y,[y,x]]=2*x^3, [[y,x],x]=0.
w3=list(itertools.product(range(2),repeat=3));i3={w:i for i,w in enumerate(w3)}
R=S.Matrix([[r.get(w,0) for w in w3] for r in rel]);rr,pv=R.rref();fr=[i for i in range(8) if i not in pv]
P3=S.zeros(6,8)
for i,j in enumerate(fr):P3[i,j]=1
for i,j in enumerate(pv):
    for k,l in enumerate(fr):P3[k,j]=-rr[i,l]
for gen,expected in [(0,2),(1,3)]:
    cols=[]
    for w in quad:
        v=S.zeros(8,1);v[i3[w+(gen,)]]+=1;v[i3[(gen,)+w]]-=1;cols.append(P3*v)
    Z=S.Matrix.hstack(*cols);assert Z.rank()==expected
# Universal unipotent square-normalizer equations, all kappa and b.
k,b,d,B=S.symbols('k b d B');eta=k-b;xi=k*b
assert S.expand(d*d+eta*d-xi-(d-b)*(d+k))==0
A=-B*(eta+d)
assert S.expand(A.subs(d,b)+B*k)==0
assert S.expand(A.subs(d,-k)-B*b)==0
# The root algebra <x,v,z>: exact quadratic AS3 top and actual signs.
h=S.symbols('h');w3=list(itertools.product(range(3),repeat=3));ix3={w:i for i,w in enumerate(w3)}
rels=[{(0,1):1,(1,0):-1},{(0,2):1,(2,0):-1},{(1,1):1,(2,2):-1,(0,0):-h}]
left=[];right=[]
for r in rels:
    for g in range(3):
        l=S.zeros(27,1);rcol=S.zeros(27,1)
        for w,c in r.items():l[ix3[w+(g,)]]=c;rcol[ix3[(g,)+w]]=c
        left.append(l);right.append(rcol)
L=S.Matrix.hstack(*left);RR=S.Matrix.hstack(*right)
ker=S.Matrix.hstack(L,-RR).nullspace();assert len(ker)==1
Q=L*ker[0][:9,0];assert Q!=S.zeros(27,1)
sign=[1,-1,-1]
for w,i in ix3.items():assert S.expand(Q[i]-sign[w[0]]*Q[ix3[w[1:]+w[:1]]])==0
out={'status':'PASS','scope':'Jordan canonical bases, all monic H3 candidates; structural coverage and Ore arguments in paper',
 'checks':{'CY_Jordan_reflection_derivation_ranks':ranks,'CY_Jordan_centralizer_ranks':[2,3],
 'unipotent_square_normalizer':'(d-b)*(d+kappa)=0 identically',
 'root_AS3_top':'one-dimensional, Nakayama signs (x,v,z)=(+,-,-)'},
 'additional_required_validator':'verify_cubic_order2_nonsplit_tensor.py',
 'not_claimed':['complete H3 classification','relative intrinsic families']}
Path(__file__).with_name('cubic_positive3_Jordan_monic_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS Jordan monic reflection, centralizer, universal root and AS3 sign certificates')
