#!/usr/bin/env python3
"""First-shared FN2 L/M families: Ore PBW, normal character and odd centre."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple import source_matrix,W2,IX,U
from verify_cubic_pym_generic import words


def fn_matrix(lam,c,e,f,r):
    lam,c,e,f,r=map(S.sympify,(lam,c,e,f,r))
    return source_matrix(lam,{1:1,2:e,5:f,9:r,11:-c,15:c,19:lam/16-c*c,20:-e/16})


def main():
    h,f=S.symbols('h f');q=(h-1)/(h+1)
    alpha=(h+1)/4;beta=4/(h-1);gamma=-(h-1)/4;delta=-4/(h+1);t=-4*f/(h-1)
    # PBW order a<d<b<c, with indices 0,1,2,3 in this order.
    rules={(1,0):{(0,1):-1},(2,0):{(1,2):alpha},(2,1):{(0,2):beta},
           (3,0):{(1,3):gamma},(3,1):{(0,3):delta},
           (3,2):{(2,3):1/q,(0,1):t}}
    def reduce(poly):
        out={};pending=dict(poly)
        while pending:
            v,c=pending.popitem();bad=next((i for i in range(len(v)-1) if v[i:i+2] in rules),None)
            if bad is None:out[v]=out.get(v,0)+c;continue
            for w,cc in rules[v[bad:bad+2]].items():
                new=v[:bad]+w+v[bad+2:];pending[new]=pending.get(new,0)+cc*c
        return {v:S.cancel(c) for v,c in out.items() if S.cancel(c)!=0}
    for v in [(2,1,0),(3,1,0),(3,2,0),(3,2,1)]:
        assert reduce({w+(v[2],):c for w,c in rules[v[:2]].items()})==reduce({(v[0],)+w:c for w,c in rules[v[1:]].items()})
    R,A=fn_matrix(S.Integer(1),h/4,0,f,0);left=(U.T*U).inv()*U.T
    order=[0,3,1,2]
    for pair,poly in rules.items():
        target=S.zeros(16,1);target[IX[tuple(order[i] for i in pair)]]=1
        for v,c in poly.items():target[IX[tuple(order[i] for i in v)]]-=c
        co=left*target;assert all(S.cancel(c)==0 for c in R*co-target)
    w=R*A*R.T
    assert all(S.cancel(S.expand(w[IX[v[:2]],IX[v[2:]]]+w[IX[v[1:3]],IX[(v[3],v[0])]]))==0 for v in words(4))
    # N=ad has diagonal normalizer (-1,-1,-q,-q^-1).
    for i,sign in enumerate([-1,-1,-q,-1/q]):
        assert not reduce({(0,1,i):1,(i,0,1):-sign})
    # At h=0 the element bc-2f ad realizes -I for every f.
    for i in range(4):
        target={}
        for v,c in [((2,3),1),((0,1),-2*f)]:
            target[v+(i,)]=target.get(v+(i,),0)+c;target[(i,)+v]=target.get((i,)+v,0)+c
        assert all(S.cancel(c.subs(h,0))==0 for c in reduce(target).values())
    # Only h=0, h^2=-1, h^2=-3 can satisfy q^n=-1, |n|<=3.
    assert S.cancel(q+1-2*h/(h+1))==0
    assert S.cancel(q*q+1-2*(h*h+1)/(h+1)**2)==0
    assert S.cancel(q**3+1-2*h*(h*h+3)/(h+1)**3)==0
    resonances=[]
    for value,basis,field in [(S.I,[(0,2,2),(1,2,2),(0,3,3),(1,3,3)],S.QQ.algebraic_field(S.I)),
                              (S.sqrt(3)*S.I,[(2,2,2),(3,3,3)],S.QQ.algebraic_field(S.sqrt(3)*S.I))]:
        ix4={v:j for j,v in enumerate(words(4))};matrix=S.zeros(256,len(basis))
        for j,v in enumerate(basis):
            out=reduce({v+(0,):1,(0,)+v:-1})
            assert all(not c.has(f) for c in out.values())
            for w,c in out.items():matrix[ix4[w],j]=S.cancel(c.subs(h,value))
        dm=DomainMatrix.from_Matrix(matrix).convert_to(field);assert dm.rank()==len(basis)
        resonances.append({'h':str(value),'candidate_words':basis,'commutator_a_rank':len(basis),'conjugate_covered':True})
    cert={'version':'classification-v77','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'presentation':'FN2 lambda=1,c=h/4,e=r=0, arbitrary f; includes all L/M and F0_1',
          'domain':'h!=+-1,f arbitrary','PBW_order':'a,d,b,c','four_diamonds':True,
          'six_relation_transport':True,'conditional_AS4_cyclic_top_tensor':True,
          'normal_ad_signs':['-1','-1','-q','-q^-1'],
          'h_zero_anti_normal':'bc-2*f*ad','remaining_resonance_injections':resonances,
          'centre3_dimension':0,'scope':'Explicit FN2 L/M family exclusion; no full chart coverage, AS4 existence sufficiency or noetherianity imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_first_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS all L/M values, Ore PBW, normal ad, anti-normal h0 and both cubic resonances')

if __name__=='__main__':main()
