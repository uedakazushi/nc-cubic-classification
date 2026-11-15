#!/usr/bin/env python3
"""All-value H rank cover and O PBW/normal-character exclusion, FS shared-zero."""
import json
from pathlib import Path
from itertools import product
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple import source_matrix,W2,IX,U
from verify_cubic_as4_tt22_remaining import projection
from verify_cubic_pym_generic import words


def cyclic(R,A):
    w=R*A*R.T
    assert all(S.cancel(S.expand(w[IX[v[:2]],IX[v[2:]]]+w[IX[v[1:3]],IX[(v[3],v[0])]]))==0 for v in words(4))


def centre(R,field):
    rels=[{w:R[k,j] for k,w in enumerate(W2) if R[k,j]} for j in range(6)]
    f3,p3=projection(rels,3,field);f4,p4=projection(rels,4,field)
    assert (len(f3),len(f4))==(20,35)
    ix={w:j for j,w in enumerate(words(4))};M=S.zeros(140,20)
    for j,k in enumerate(f3):
        v=words(3)[k]
        for i in range(4):M[35*i:35*(i+1),j]=p4[:,ix[v+(i,)]]-p4[:,ix[(i,)+v]]
    _,rows=DomainMatrix.from_Matrix(M.T).convert_to(field).rref();assert len(rows)==20
    det=field.to_sympy(DomainMatrix.from_Matrix(M[list(rows),:]).convert_to(field).det())
    return list(rows),S.factor(det),p3,p4


def main():
    l,a=S.symbols('lambda A');hs=[]
    expected=16384*l**12*(l+1)**9*(2*l+1)**4*(4*l+1)*(4*l+3)
    for eps in [0,1]:
        R,AA=source_matrix(l,{2:1,5:1,9:l*(l+1)/16,14:l*(l+1)/16,20:eps});cyclic(R,AA)
        rows,det,p3,p4=centre(R,S.QQ.frac_field(l));assert S.cancel(det-expected)==0
        assert all(S.fraction(S.cancel(c))[1]==1 for c in list(p3)+list(p4))
        special=[]
        for lv in [-S.Rational(1,2),-S.Rational(1,4),-S.Rational(3,4)]:
            RR,AAA=source_matrix(lv,{2:1,5:1,9:lv*(lv+1)/16,14:lv*(lv+1)/16,20:eps})
            cyclic(RR,AAA);rs,ds,_,_=centre(RR,S.QQ)
            special.append({'lambda':str(lv),'minor_rows':rs,'minor_determinant':str(ds)})
        hs.append({'epsilon':eps,'generic_minor_rows':rows,'generic_determinant':str(det),
                   'projection_denominators_one':True,'special_rank20':special})
        print('PASS H',eps,'all-parameter centre3 rank20 cover',flush=True)
    R,AA=source_matrix(l,{0:1,8:a,11:l*(l+1)/(16*a)});cyclic(R,AA)
    r=-(4*a-l-1)/(4*a+l+1);s=-(4*a+l)/(4*a-l)
    q=r*s;k=-32*a/((4*a-l)*(4*a+l+1))
    left=(U.T*U).inv()*U.T
    # Direct normality of a,b in degree two, all-value denominators allowed.
    normal=[]
    for gen,ss in [(0,[1,-1,r,-1/r]),(1,[-1,1,s,-1/s])]:
        for i in range(4):
            v=S.zeros(16,1);v[IX[(gen,i)]]+=1;v[IX[(i,gen)]]-=ss[i]
            co=left*v;assert all(S.cancel(c)==0 for c in R*co-v)
        normal.append(list(map(str,ss)))
    # Generic PBW algebra on a<b<c<d. Four length-three ambiguities.
    rr,ss,kk=S.symbols('r s k');qq=rr*ss
    rules={(1,0):{(0,1):-1},(2,0):{(0,2):1/rr},(3,0):{(0,3):-rr},
           (2,1):{(1,2):1/ss},(3,1):{(1,3):-ss},
           (3,2):{(2,3):1/qq,(0,1):-kk/qq}}
    def reduce(poly):
        done={};pending=dict(poly)
        while pending:
            w,c=pending.popitem()
            bad=next((j for j in range(len(w)-1) if w[j:j+2] in rules),None)
            if bad is None:done[w]=done.get(w,0)+c;continue
            for term,v in rules[w[bad:bad+2]].items():
                nw=w[:bad]+term+w[bad+2:];pending[nw]=pending.get(nw,0)+c*v
        return {w:S.cancel(v) for w,v in done.items() if S.cancel(v)!=0}
    for w in [(2,1,0),(3,1,0),(3,2,0),(3,2,1)]:
        first={t+(w[2],):c for t,c in rules[w[:2]].items()}
        last={(w[0],)+t:c for t,c in rules[w[1:]].items()}
        assert reduce(first)==reduce(last)
    # Six source relations are exactly the above PBW relations.
    for pair,poly in rules.items():
        v=S.zeros(16,1);v[IX[pair]]=1
        for w,c in poly.items():v[IX[w]]-=c.subs({rr:r,ss:s,kk:k}) if hasattr(c,'subs') else c
        co=left*v;assert all(S.cancel(c)==0 for c in R*co-v)
    # At the only possible cubic characters, the pure cube is indeed central.
    root=S.QQ.algebraic_field(S.sqrt(3)*S.I)
    omega=(-1+S.sqrt(3)*S.I)/2
    for rv,gen in [(omega,2),(-omega,3)]:
        for i in range(4):
            out=reduce({(gen,)*3+(i,):1,(i,)+(gen,)*3:-1}) if gen!=i else {}
            assert all(root.from_sympy(S.cancel(c.subs({rr:rv,ss:rv})))==root.zero for c in out.values())
    # Rational parameter characterization; r*s!=1 excludes inverse roots.
    assert S.factor(r-s)==8*a*(2*l+1)/((4*a-l)*(4*a+l+1))
    assert S.cancel(r*s-1+8*a/((4*a-l)*(4*a+l+1)))==0
    identities=[S.factor(S.together(expr)) for expr in [r*r+r+1,s*s+s+1,r*r-r+1,s*s-s+1]]
    character_table=[]
    for ex in product(range(4),repeat=4):
        if sum(ex)!=3:continue
        i,j,u,v=ex;n=u-v
        character_table.append({'exponents':ex,'a_sign':(-1)**(j+v),'b_sign':(-1)**(i+v),'power':n})
        if n==0:assert (i+j)%2==1
        elif abs(n)==2:assert ((j+v)%2==0) or ((i+v)%2==0)
        elif abs(n)==3:assert ex in [(0,0,3,0),(0,0,0,3)]
        else:assert abs(n)==1
    cert={'version':'classification-v74','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'H_rank_cover':hs,'O_normalizers_a_b':normal,'O_q_and_correction':list(map(str,[q,k])),
          'O_PBW_four_diamonds':True,'O_twenty_degree3_characters':character_table,
          'O_cubic_root_conditions':list(map(str,identities)),
          'O_centre3':'k c^3 if lambda=-1/2,A^2=-3/64; k d^3 if lambda=-1/2,A^2=-1/192; zero otherwise',
          'cyclic_top_tensor_all_three_families':True,
          'scope':'Independent all-value obstruction for explicit FZ4/FZ5 presentations conditional AS4/domain as required by H3. No full CY/projection coverage theorem imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_remaining_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS O PBW, normal characters, pure cubic resonance and all three CY top tensors',flush=True)

if __name__=='__main__':main()
