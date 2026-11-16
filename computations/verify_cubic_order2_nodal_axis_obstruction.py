#!/usr/bin/env python3
"""Exact affine chart for the nodal normal-axis obstruction, all d,i."""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    a,d,i,z,h=S.symbols('a d i z h')
    u=h-a-d*z
    F=S.expand(u*u/4-1-i*z)
    rules={(0,0):{():z},(1,1):{():h},(2,2):{():F},
           (1,0):{(0,1):-1},(2,0):{(0,2):-1},(2,1):{(1,2):1}}
    def add(*terms):
        out={}
        for c,p in terms:
            for w,v in p.items():out[w]=S.expand(out.get(w,0)+c*v)
        return {w:c for w,c in out.items() if c!=0}
    @lru_cache(None)
    def nf(word):
        for pos in range(len(word)-1):
            if word[pos:pos+2] in rules:return reduce_at(word,pos)
        return {word:S.Integer(1)}
    def reduce_at(word,pos):
        return add(*[(c,nf(word[:pos]+w+word[pos+2:]))
                     for w,c in rules[word[pos:pos+2]].items()])
    def mul(p,q):return add(*[(c*d,nf(w+v)) for w,c in p.items() for v,d in q.items()])
    def eta(p):return add(*[((-1)**sum(j in [1,2] for j in w),{w:c}) for w,c in p.items()])
    diamonds=0
    for word in itertools.product(range(3),repeat=3):
        if word[:2] in rules and word[1:] in rules:
            assert not add((1,reduce_at(word,0)),(-1,reduce_at(word,1)))
            diamonds+=1
    one={():S.Integer(1)};r={(0,):S.Integer(1)};s={(1,):S.Integer(1)};b={(2,):S.Integer(1)}
    t=add((1,b),(u/2,one))
    # Original C/g generators are x=r*y, p=s*y, v=t*y in
    # A[y,y^-1;eta], eta(r,s,b)=(r,-s,-b).
    def degree_one_product(c1,c2):return mul(c1,eta(c2))
    for c1 in [one,s,t]:
        assert not add((1,degree_one_product(r,c1)),(-1,degree_one_product(c1,r)))
    assert not add((1,degree_one_product(s,one)),(1,degree_one_product(one,s)))
    assert not add((1,degree_one_product(t,t)),(-(1+i*z),one))
    assert not add((1,degree_one_product(s,s)),(a+u+d*z,one))
    L=add((1,degree_one_product(one,t)),(1,degree_one_product(t,one)))
    T=add((1,degree_one_product(s,t)),(1,degree_one_product(t,s)))
    assert not add((1,L),(-u,one))
    assert not add((1,T),(2,mul(s,b)))
    volume=add((1,mul(s,t)),(-u/2,s),(S.Rational(1,2),T))
    assert not volume
    # The completion at z=h=0 is local exactly in the nodal cases under study.
    for av in [2,-2]:
        assert S.expand(F.subs({a:av,z:0,h:0}))==0
        # On substituting z=r^2,h=s^2, every defining relation has order >=2.
        R,Q=S.symbols('R Q')
        formal=S.Poly(S.expand(F.subs({a:av,z:R*R,h:Q*Q})),R,Q)
        assert all(sum(m)>=2 for m,c in formal.terms())
        # All fourth powers of the positive-word ideal vanish in the fibre.
        for word in itertools.product(range(3),repeat=4):
            assert all(S.expand(c.subs({a:av,z:0,h:0}))==0 for c in nf(word).values())
    def cocycle(g,t):return (-1)**(g[0]*t[1]+g[2]*t[0])
    top=(1,0,1)
    chars=[cocycle(top,t)*cocycle(t,top) for t in [(1,1,0),(1,0,0),(1,0,0),(0,0,1)]]
    assert chars==[1,-1,-1,-1]
    data={
      'hypotheses':'normal-axis H3 necessary normal form, a=2 or a=-2, arbitrary d,i',
      'chart':'A=(C/(g)[Y^-1])_0, Y=y²',
      'generators':['r=x*y^-1','s=p*y^-1','b=v*y^-1-(L/Y)/2'],
      'central_coordinates':['z=r²','h=s²','u=h-a-dz','w=-2sb'],
      'relations':['rs=-sr','rb=-br','sb=bs','r²=z','s²=h','b²=(h-a-dz)²/4-1-i*z'],
      'PBW_over_k_z_h':'free rank8, basis r^e*s^f*b^g, e,f,g in {0,1}',
      'overlap_identities_checked':diamonds,
      'cocycle_top_character_p_y_v_x':chars,
      'inverse':'x=r*y,p=s*y,v=(b+u/2)*y; y acts by eta(r,s,b)=(r,-s,-b)',
      'local_obstruction':'At a=+-2, completion at z=h=0 is local with Ext1(k,k)=3. H3 Serre duality at its shift-fixed point would give Ext2(k,k)=1 and higher Ext=0. A minimal free resolution with ranks (1,3,1) contradicts Euler rank over Frac(k[[z,h]]), where A has dimension8.',
      'scope':'All chart/PBW/inverse identities are checked exactly. The Serre, completion and minimal-resolution argument is a structural proof in the manuscript, not a finite-degree homological test.'}
    path=Path(__file__).with_name('cubic_order2_nodal_axis_obstruction_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS nodal chart PBW, inverse Clifford relations and all-parameter tangent identities')


if __name__=='__main__':main()
