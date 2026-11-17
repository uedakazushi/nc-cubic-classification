#!/usr/bin/env python3
"""Exact original twisted-quartic blocks, Pfaffians and growth obstruction.
Chart coverage, basis normalization and unipotent untwist are ordinary proofs.
"""
import itertools
import json
import math
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parent
words=list(itertools.product(range(4),repeat=4))
expected=['xxxy','xxyy','xxcc','xyxy','xyyy','xycc','xbbc','xbcb',
          'xcyc','xcbb','xccy','yycc','ybbc','ybcb','ycbb','cccc']
letters='xybc'; a=s.symbols('a:16');q=s.symbols('q',nonzero=True)
checked=[]
for imaginary in [s.I,-s.I]:
    mu=[s.S.One,s.S.One,imaginary,-s.S.One];nu=[1/m for m in mu]
    seen=set();tensors=[];reps=[]
    for w in words:
        if w in seen:continue
        v=w;c=s.S.One;terms={}
        while v not in terms:
            terms[v]=c;seen.add(v)
            v=(v[-1],)+v[:-1];c=s.expand(-nu[v[0]]*c)
        if c!=1:continue
        reps.append(''.join(letters[j] for j in w));tensors.append(terms)
    assert reps==expected
    H=s.zeros(16)
    for coefficient,T in zip(a,tensors):
        # Check every original right twisted-cyclic coefficient.
        for w,c in T.items():
            v=(w[-1],)+w[:-1]
            assert s.expand(T[v]+nu[v[0]]*c)==0
            H[4*w[0]+w[1],4*w[2]+w[3]]+=coefficient*c
    H0=H.extract([0,1,4,5,15],[0,1,4,5,15])
    H2=H.extract([3,7,10,12,13],[3,7,10,12,13])
    M=H.extract([2,6,8,9],[11,14])
    assert H0==H0.T and H2==-H2.T
    assert M==s.Matrix([[a[6],a[7]],[a[12],a[13]],
                        [imaginary*a[7],imaginary*a[9]],[imaginary*a[13],imaginary*a[14]]])
    normalized={a[6]:q**-2,a[7]:q**-1,a[9]:1,a[12]:0,a[13]:0,a[14]:0}
    N=H2.subs(normalized)
    assert (M[:,1]-q*M[:,0]).subs(normalized)==s.zeros(4,1)
    pf=[]
    for i,j,k,l in itertools.combinations(range(5),4):
        pf.append(s.factor(N[i,j]*N[k,l]-N[i,k]*N[j,l]+N[i,l]*N[j,k]))
    assert pf==[(a[5]*q**2-a[8])/q**2,a[11],
                 -a[10]*a[5]-a[11]*a[2]+a[8]**2,
                 (-a[10]+a[8]*q**2)/q**2,a[11]/q**2]
    solved={a[8]:q**2*a[5],a[10]:q**4*a[5],a[11]:0}
    assert all(s.cancel(p.subs(solved))==0 for p in pf)
    assert N[:,2]==s.Matrix([1,0,0,q**-2,0])
    A=H0[:4,:4]
    minors={s.factor(A.extract(I,J).det()) for I in itertools.combinations(range(4),3)
            for J in itertools.combinations(range(4),3)}
    for obstruction in [2*a[0]**2*a[1],2*a[1]*a[4]**2,
                        -a[1]*(2*a[0]*a[4]-a[1]**2)]:
        assert obstruction in minors or -obstruction in minors
    e=s.Matrix([0,1,-1,0]);v=s.Matrix([a[0],a[3]/2,a[3]/2,a[4]])
    assert A.subs(a[1],0)==e*v.T+v*e.T
    H0=H0.subs(solved).subs(a[1],0)
    assert H0[:,3]==a[4]*s.Matrix([0,1,-1,0,0])
    assert H0[4,:].subs(a[4],0)[3]==0
    # Original relation space after x=c=0 has only the bb coordinate.
    projected={}
    for i in [5,6,9,10]: # yy,yb,by,bb
        projected[i]=[s.expand(H[i,j].subs(normalized).subs(solved).subs({a[1]:0,a[4]:0})) for j in range(16)]
    assert all(not any(projected[i]) for i in [5,6,9])
    assert any(projected[10])
    checked.append({'imaginary_root':str(imaginary),'twisted_tensor_dimension':16,
                    'normalized_Pfaffians_solved':True,'quotient_relation_support':['bb']})
# Literal growth of the monomial quotient: no consecutive bb.
without_b,with_b=1,0
for degree in range(1,16):without_b,with_b=without_b+with_b,without_b
assert without_b+with_b==1597 and math.comb(18,3)==816
source=json.loads((root/'cubic_fourth_root_unit_simple_rank2_certificate.json').read_text())
assert source['final_spectrum_count']==11
removed=[r for r in source['final_survivors'] if r['N']==4 and r['spectrum'] in [[0,1,2],[0,2,3]]]
assert len(removed)==2 and all(r['relation_weight_multiplicities']==[[2,1,2,1]] for r in removed)
final=[r for r in source['final_survivors'] if r not in removed]
assert len(final)==9
reps=set()
for r in final:
    N=r['N'];A,b,c=r['spectrum']
    reps.add(min((N,(A*u)%N,*sorted([(b*u)%N,(c*u)%N])) for u in range(1,N) if math.gcd(u,N)==1))
assert len(reps)==5
out={'status':'PASS','scope':'all original twisted tensor orbits and block identities, exact Pfaffians/minors, monomial Hilbert obstruction, finite list; ordinary coverage/untwist proof separate',
     'orbit_representatives':expected,'checks':checked,'quotient_degree15':1597,'AS4_degree15':816,
     'excluded_spectra':removed,'final_survivors':final,'final_spectrum_count':9,
     'remaining_orders':[3,4],'remaining_counts':{'3':3,'4':6},
     'Galois_label_orbit_count':5,'Galois_label_representatives':sorted(reps),
     'not_claimed':['remaining9 H3 existence or admissibility','complete four-eigenvalue/CY coverage','complete H3 classification']}
(root/'cubic_fourth_root_unit_repeat_resonance_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','unit_repeat_fourth_root_spectra_excluded':2,'remaining_spectra':9}))
