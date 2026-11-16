#!/usr/bin/env python3
"""Inverse u-chart and exact Ext1 linearizations at the cubic-cone vertex."""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    a,b,c,d,f,g,h,pi,ga,j,tau=S.symbols('a b c d f g h pi gamma J tau')
    alpha=a*pi+b+c*ga;beta=d*pi+f*ga;H=g+h*ga
    F=alpha*alpha/4-H
    rules={(0,0):{():-pi},(1,1):{():-ga},(2,2):{():F},
           (1,0):{(0,1):-1,():-2*j},(2,0):{(0,2):-1,():-tau},
           (2,1):{(1,2):-1,():-beta}}
    def add(*terms):
        out={}
        for cc,poly in terms:
            for word,v in poly.items():out[word]=S.expand(out.get(word,0)+cc*v)
        return {w:cc for w,cc in out.items() if cc!=0}
    @lru_cache(None)
    def nf(word):
        for pos in range(len(word)-1):
            if word[pos:pos+2] in rules:
                return add(*[(cc,nf(word[:pos]+ww+word[pos+2:])) for ww,cc in rules[word[pos:pos+2]].items()])
        return {word:S.Integer(1)}
    def mul(p,q):return add(*[(cc*dd,nf(word+ww)) for word,cc in p.items() for ww,dd in q.items()])
    def eta(p):return add(*[((-1)**len(word),{word:cc}) for word,cc in p.items()])
    one={():S.Integer(1)};ss={(0,):S.Integer(1)};ww={(1,):S.Integer(1)};zz={(2,):S.Integer(1)}
    vv=add((1,zz),(alpha/2,one))
    # u is the degree-one Laurent variable; p=S*u,w=W*u,v=(Z+alpha/2)*u.
    def prod1(p,q):return mul(p,eta(q))
    assert not add((1,prod1(ss,one)),(1,prod1(one,ss)))
    assert not add((1,prod1(one,ww)),(1,prod1(ww,one)))
    L=add((1,mul(ss,ww)),(j,one))
    assert not add((1,prod1(ss,ww)),(-1,prod1(ww,ss)),(2,L))
    assert not add((1,prod1(one,vv)),(1,prod1(vv,one)),(-alpha,one))
    assert not add((1,prod1(ww,vv)),(1,prod1(vv,ww)),(-beta,one))
    assert not add((1,prod1(vv,vv)),(-H,one))
    assert not add((1,prod1(ss,vv)),(1,prod1(vv,ss)),(-tau,one))
    # Exact infinitesimal upper-triangular extensions, including centrality.
    q=S.symbols('q',nonzero=True)
    variables=S.symbols('s w z p0 y0 j0 t0')
    ds,dw,dz,dp,dy,dj,dt=variables
    I=S.eye(2)
    def nil(v):return S.Matrix([[0,v],[0,0]])
    def linear_system(zi,zj):
        sm,wm,zm=nil(ds),nil(dw),S.Matrix([[zi,dz],[0,zj]])
        pm,ym,jm,tm=map(nil,[dp,dy,dj,dt])
        am=b*I+a*pm+c*ym;bm=d*pm+f*ym
        hm=(b*b/4-q*q)*I+h*ym
        relations=[sm*sm+pm,wm*wm+ym,sm*wm+jm,wm*sm+jm,
                   sm*zm+zm*sm+tm,wm*zm+zm*wm+bm,
                   zm*zm-am*am/4+hm,tm*wm-bm*sm]
        for central in [pm,ym,jm,tm]:
            for gen in [sm,wm,zm]:relations.append(central*gen-gen*central)
        expressions=[S.expand(r[0,1]) for r in relations if r[0,1]!=0]
        matrix=S.Matrix([[expr.coeff(v) for v in variables] for expr in expressions])
        return matrix
    cases=[]
    for name,zi,zj,expected,inner in [('self+',q,q,1,0),('self-',-q,-q,1,0),
                                      ('cross+',q,-q,3,1),('cross-',-q,q,3,1),
                                      ('double',0,0,3,0)]:
        matrix=linear_system(zi,zj)
        if name=='double':matrix=matrix.subs(q,0)
        rows=[{j:entry for j,entry in enumerate(row) if entry!=0} for row in matrix.tolist()]
        columns=set(range(7));rank=0
        while True:
            def allowed(value):
                value=S.cancel(value)
                return value!=0 and value.free_symbols.issubset({q}) and (
                    value.is_number or S.Poly(value,q).is_monomial)
            hit=next(((ii,j,cc) for ii,row in enumerate(rows) for j,cc in row.items()
                      if j in columns and allowed(cc)),None)
            if hit is None:break
            ii,j,cc=hit;pivot={k:S.cancel(value/cc) for k,value in rows.pop(ii).items()}
            columns.remove(j);rank+=1
            for row in rows:
                if j not in row:continue
                scale=row[j]
                for k,value in pivot.items():
                    new=S.cancel(row.get(k,0)-scale*value)
                    if new==0:row.pop(k,None)
                    else:row[k]=new
        assert not any(rows) and 7-rank==expected
        cases.append({'case':name,'derivations':expected,'inner_derivations':inner,'Ext1':expected-inner})
    # At the double root the fibre is local, with radical cube zero.
    @lru_cache(None)
    def fiber(word):
        for pos in range(len(word)-1):
            pair=word[pos:pos+2]
            if pair in [(0,0),(1,1),(2,2),(0,1),(1,0)]:return {}
            if pair in [(2,0),(2,1)]:
                return {ww:-cc for ww,cc in fiber(word[:pos]+pair[::-1]+word[pos+2:]).items()}
        return {word:1}
    assert all(not fiber(word) for word in itertools.product(range(3),repeat=3))
    data={
      'hypotheses':'eight-coefficient H3 candidate, e=0,d!=0; central cubic-cone vertex',
      'result':'No H3 quotient exists in this cone-center locus; hence every H3 object of the (1,3) sector has e!=0 and center F1.',
      'u_chart':['S=p*u^-1,W=w*u^-1,Z=v*u^-1-alpha/2',
                 'central pi=P/X,gamma=Y/X,J=pw/X,tau=T/X',
                 'alpha=a*pi+b+c*gamma,beta=d*pi+f*gamma,H=g+h*gamma',
                 'S²=-pi,W²=-gamma,SW=WS=-J',
                 '{S,Z}=-tau,{W,Z}=-beta,Z²=alpha²/4-H,tau*W=beta*S'],
      'shift':'conjugation by u negates S,W,Z and fixes the central coefficients',
      'vertex_simple_roots':'Z²=b²/4-g; two simples exchanged by shift if b²!=4g, one shift-fixed simple if b²=4g',
      'exact_Ext1_linearizations':cases,
      'distinct_root_obstruction':'Ext1 matrix [[1,2],[2,1]] contradicts H3 Serre duality, which forces its four entries to have equal dimension for a shift-exchanged pair.',
      'double_root_obstruction':'Ext1=3, Ext2=1 and higher Ext=0 would force a minimal free resolution of ranks (1,3,1); generic central rank4 contradicts Euler rank.',
      'scope':'Inverse-generator identities and all-parameter infinitesimal extension systems checked exactly. Local-global comparison, Serre duality and the minimal-resolution argument are proved structurally in the manuscript.'}
    path=Path(__file__).with_name('cubic_order2_cone_obstruction_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS inverse cone chart and exact self/cross Ext1 dimensions in all root cases')


if __name__=='__main__':main()
