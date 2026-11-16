#!/usr/bin/env python3
"""Universal Clifford identities for the normal-common-axis reduction.

Checks polynomial identities, not AS4 or H3 sufficiency of all parameters.
"""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    a,d,i,x,Y,L,T=S.symbols('a d i x Y L T')
    P=-a*Y-L-d*x*x;V=Y+i*x*x
    rules={(0,0):{():P},(1,1):{():Y},(2,2):{():V},
           (1,0):{(0,1):-1},(2,0):{(0,2):-1,():T},
           (2,1):{(1,2):-1,():L}}
    def add(*terms):
        out={}
        for scalar,poly in terms:
            for word,coeff in poly.items():
                out[word]=S.expand(out.get(word,0)+scalar*coeff)
        return {w:c for w,c in out.items() if c!=0}
    @lru_cache(None)
    def nf(word):
        for pos in range(len(word)-1):
            if word[pos:pos+2] in rules:return reduce_at(word,pos)
        return {word:S.Integer(1)}
    def reduce_at(word,pos):
        return add(*[(c,nf(word[:pos]+w+word[pos+2:]))
                     for w,c in rules[word[pos:pos+2]].items()])
    def mul(p,q):return add(*[(a*b,nf(u+v)) for u,a in p.items() for v,b in q.items()])
    diamonds=0
    for word in itertools.product(range(3),repeat=3):
        if word[:2] in rules and word[1:] in rules:
            assert not add((1,reduce_at(word,0)),(-1,reduce_at(word,1)))
            diamonds+=1
    gens=[{(j,):S.Integer(1)} for j in range(3)]
    g={(0,1,2):S.Integer(1),(0,):-L/2,(1,):T/2}
    for v in gens:assert not add((1,mul(g,v)),(-1,mul(v,g)))
    matrix=S.Matrix([[P,0,T/2],[0,Y,L/2],[T/2,L/2,V]])
    det=S.expand(matrix.det())
    assert not add((1,mul(g,g)),(det,{():S.Integer(1)}))
    # B is the sign-cocycle twist of C.  Degree=(active parity,p parity,x parity).
    degrees=[(1,1,0),(1,0,0),(1,0,0)]
    def cocycle(g,h):return (-1)**(g[0]*h[1]+g[2]*h[0])
    def bw(word):
        degree=(0,0,0);sign=1
        for j in word:
            sign*=cocycle(degree,degrees[j])
            degree=tuple((u+v)%2 for u,v in zip(degree,degrees[j]))
        return add((sign,nf(word)))
    assert not add((1,bw((0,1,2))),(-1,bw((2,0,1))),(-2,g))
    # Volume degree (1,1,0) has precisely the required B-normalizer.
    volume_degree=(1,1,0)
    characters=[]
    for h in degrees+[(0,0,1)]:
        characters.append(cocycle(volume_degree,h)*cocycle(h,volume_degree))
    assert characters==[1,-1,-1,-1]
    # A finite exact check of the sign rule for all group elements.
    group=list(itertools.product(range(2),repeat=3))
    def plus(g,h):return tuple((u+v)%2 for u,v in zip(g,h))
    for g1,g2,g3 in itertools.product(group,repeat=3):
        assert cocycle(g1,g2)*cocycle(plus(g1,g2),g3)==cocycle(g2,g3)*cocycle(g1,plus(g2,g3))
    boundary=S.expand(4*det.subs(x,0))
    assert S.expand(boundary-((L+a*Y)*(L-2*Y)*(L+2*Y)-Y*T*T))==0
    disc=S.factor(S.discriminant((L+a)*(L-2)*(L+2),L))
    assert S.expand(disc-16*(a*a-4)**2)==0
    data={
      'hypotheses':'H3 multiplicities(1,3), with a normal coordinate in its common noncommutative quantum plane',
      'necessary_normal_form':['x anticommutes with p,y,v','py=yp','v²=y²+i*x²','p²=a*y²+yv+vy+d*x²'],
      'scope':'Necessary form and unique H3 normal cubic; AS4/domain/H3 sufficiency of every parameter is not claimed.',
      'normal_cubic':'G=[py,v], spanning W1(B) under the H3 envelope hypotheses',
      'central_cocycle_model':['x central','py+yp=0','v²=Y+i*x²','p²=-a*Y-L-d*x²','y²=Y','yv+vy=L','pv+vp=T'],
      'central_base':'k[x,Y,L,T], degrees (1,2,2,2)',
      'clifford_basis':['1','p','y','v','py','pv','yv','pyv'],
      'overlap_identities_checked':diamonds,
      'volume':'g=pyv-L*p/2+T*y/2; G maps to 2g',
      'volume_square':'g²=-det M, M=[[ -aY-L-dx²,0,T/2 ],[0,Y,L/2],[T/2,L/2,Y+i*x²]]',
      'normalizer_character_order_p_y_v_x':characters,
      'boundary_net_discriminant':'4det(M)|x=0=(L+aY)(L-2Y)(L+2Y)-Y*T²',
      'binary_cubic_discriminant':'16*(a²-4)²',
      'remaining':'H3 admissibility and all intrinsic arrows in this normal form; overlap with known smooth-boundary Clifford sectors; nodal discriminant cases a=+-2; all charts without the extra normal-coordinate hypothesis.'}
    path=Path(__file__).with_name('cubic_order2_normal_axis_clifford_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS universal Clifford diamonds, volume, cocycle and discriminant identities')


if __name__=='__main__':main()
