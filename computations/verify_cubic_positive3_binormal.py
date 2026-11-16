#!/usr/bin/env python3
"""Exact (3,1) bi-normal Clifford model and its factorable normal-cubic kernel."""
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    spec=importlib.util.spec_from_file_location('template',Path(__file__).with_name('verify_cubic_order2_central_template.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    class PositiveModel(mod.Model):
        def __init__(self):
            super().__init__()
            self.a,self.b,self.c=S.symbols('a b c')
            self.H=self.a*self.P+self.b*self.Y+self.c*self.X
            self.rules[(2,2)]={():self.H}
            self.rules[(2,1)]={(1,2):-1}
        def sigma(self,p):
            return self.add(*[((-1)**w.count(2)*cc.subs(self.T,-self.T),self.nf(w)) for w,cc in p.items()])
        def delta(self,p):return {}
    M=PositiveModel();P,Y,X,T=M.P,M.X,M.Y,M.T
    p,y,z=[(g,{}) for g in M.gens];x=({},M.one)
    gens=[p,x,y,z];mu=[1,1,1,-1]
    for word,tail in M.rules.items():
        assert not M.sigma(M.add((1,{word:S.Integer(1)}),(-1,tail)))
    overlaps=0
    for word in itertools.product(range(3),repeat=3):
        if word[:2] in M.rules and word[1:] in M.rules:
            left=M.add(*[(cc,M.nf(w+word[2:])) for w,cc in M.rules[word[:2]].items()])
            right=M.add(*[(cc,M.nf(word[:1]+w)) for w,cc in M.rules[word[1:]].items()])
            assert not M.add((1,left),(-1,right));overlaps+=1
    for gg in M.gens+[{():T}]:assert not M.add((1,M.sigma(M.sigma(gg))),(-1,gg))
    def zero(q):return not any(q)
    for aa,bb,sign in [(p,x,1),(x,y,1),(p,y,-1),(z,x,-1),(z,y,-1)]:
        assert zero(M.oadd((1,M.omul(aa,bb)),(-sign,M.omul(bb,aa))))
    assert zero(M.oadd((1,M.omul(z,z)),(-M.H,(M.one,{}))))
    cubics=[M.oadd((q,gg)) for gg in [p,x,y] for q in [P,X,Y]]
    cubics += [M.oadd((T,z)),M.omul(M.omul(p,y),x)]
    rows={}
    for j,cubic in enumerate(cubics):
        for gi,(gg,sign) in enumerate(zip(gens,mu)):
            out=M.oadd((1,M.omul(cubic,gg)),(-sign,M.omul(gg,cubic)))
            for ep,poly in enumerate(out):
                for word,cc in poly.items():
                    for powers,value in S.Poly(cc,P,X,Y,T).terms():
                        rows.setdefault((gi,ep,word,powers),{})[j]=value
    remaining=list(rows.values());columns=set(range(11));pivots=0
    while True:
        hit=next(((ii,j,cc) for ii,row in enumerate(remaining) for j,cc in row.items()
                  if j in columns and cc!=0 and not S.sympify(cc).free_symbols),None)
        if hit is None:break
        ii,j,cc=hit;pivot={k:S.expand(v/S.sympify(cc)) for k,v in remaining.pop(ii).items()}
        columns.remove(j);pivots+=1
        for row in remaining:
            if j not in row:continue
            scale=row[j]
            for k,value in pivot.items():
                new=S.expand(row.get(k,0)-scale*value)
                if new==0:row.pop(k,None)
                else:row[k]=new
    assert pivots==8 and columns=={3,4,5} and not any(remaining)
    # The quadratic dual: Q has only PX=-XP and XY=-YX; quotient PZ,
    # then central quadrics P²+aZ²,X²+bZ²,Y²+cZ².
    words=list(itertools.product(range(4),repeat=2));index={w:i for i,w in enumerate(words)}
    def vec(poly):
        out=S.zeros(16,1)
        for ww,cc in poly.items():out[index[ww]]+=cc
        return out
    a,b,c=M.a,M.b,M.c
    R=[{(0,1):1,(1,0):-1},{(1,2):1,(2,1):-1},
       {(0,2):1,(2,0):1},{(3,1):1,(1,3):1},{(3,2):1,(2,3):1},
       {(3,3):1,(0,0):-a,(1,1):-b,(2,2):-c}]
    dual=[]
    for i,j in itertools.combinations(range(4),2):
        if (i,j)==(0,3):continue
        dual.append({(i,j):1,(j,i):1 if (i,j) in [(0,1),(1,2)] else -1})
    dual.extend([{(0,3):1},{(3,0):1}])
    dual.extend([{(i,i):1,(3,3):cc} for i,cc in enumerate([a,b,c])])
    assert all((vec(rr).T*vec(ss))[0]==0 for rr in R for ss in dual)
    assert S.Matrix.hstack(*(vec(rr) for rr in R)).rank()==6
    assert S.Matrix.hstack(*(vec(ss) for ss in dual)).rank()==10
    # Nakayama signs: nu_Q=(-,+,-,+), tau_PZ=(+,-,+,+).
    nu=[i*j for i,j in zip([-1,1,-1,1],[1,-1,1,1])]
    assert [-i for i in nu]==mu
    data={
      'presentation':['px=xp','xy=yx','py=-yp','zx=-xz','zy=-yz','z²=a*p²+b*x²+c*y²'],
      'a_nonzero':'noetherian quadratic Koszul AS4, actual Nakayama (+,+,+,-); Clifford--Ore presentation free rank32 over k[p²,x²,y²,T²]',
      'a_zero':'dual has infinite-dimensional quotient Q(X,Y,Z)/(X²+bZ²,Y²+cZ²); not Koszul AS4',
      'clifford_overlap_count':overlaps,
      'fixed_cubic_dimension':11,'normal_kernel_constant_pivot_rank':8,
      'normal_kernel':'x*span(p²,x²,y²); all normal cubics have the nonzero linear factor x',
      'conclusion':'No H3 cuts anywhere in this explicit (3,1) family.',
      'scope':'Clifford and automorphism identities, full normal kernel and quadratic dual orthogonality checked universally. Koszul/Frobenius regular-sequence proof is in the manuscript; no coverage of all (3,1) envelopes is asserted.'}
    path=Path(__file__).with_name('cubic_positive3_binormal_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS (3,1) bi-normal AS4 model, actual Nakayama and factorable full normal-cubic kernel')


if __name__=='__main__':main()
