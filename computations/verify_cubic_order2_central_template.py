#!/usr/bin/env python3
"""Universal Clifford--Ore model and dual resultant of the (1,3) template."""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


class Model:
    def __init__(self):
        self.parameters=S.symbols('a b c d e f g h')
        a,b,c,d,e,f,g,h=self.parameters
        self.P,self.X,self.Y,self.T=S.symbols('P X Y T')
        P,X,Y,T=self.P,self.X,self.Y,self.T
        self.A=a*P+b*X+c*Y;self.B=d*P+e*X+f*Y;self.H=g*X+h*Y
        self.rules={(0,0):{():P},(1,1):{():X},(2,2):{():self.H},
                    (1,0):{(0,1):-1},(2,0):{(0,2):-1,():T},
                    (2,1):{(1,2):-1,():self.A}}
        self.one={():S.Integer(1)}
        self.gens=[{(j,):S.Integer(1)} for j in range(3)]

    def add(self,*terms):
        out={}
        for scalar,poly in terms:
            for word,c in poly.items():out[word]=S.expand(out.get(word,0)+scalar*c)
        return {w:c for w,c in out.items() if c!=0}

    @lru_cache(None)
    def nf(self,word):
        for pos in range(len(word)-1):
            if word[pos:pos+2] in self.rules:
                return self.add(*[(c,self.nf(word[:pos]+w+word[pos+2:]))
                                 for w,c in self.rules[word[pos:pos+2]].items()])
        return {word:S.Integer(1)}

    def mul(self,p,q):
        return self.add(*[(c*d,self.nf(w+v)) for w,c in p.items() for v,d in q.items()])

    def sigma(self,p):
        return self.add(*[((-1)**sum(j!=0 for j in w)*c.subs(self.T,-self.T),self.nf(w))
                          for w,c in p.items()])

    @lru_cache(None)
    def delta_word(self,w):
        if not w:return {}
        first=self.gens[w[0]]
        return self.add((1,self.mul(self.sigma(first),self.delta_word(w[1:]))),
                        (self.B if w[0]==2 else 0,self.nf(w[1:])))

    def delta(self,p):
        terms=[]
        for w,c in p.items():
            diff=S.cancel(self.B*(c-c.subs(self.T,-self.T))/self.T)
            terms.append((diff,self.mul(self.gens[0],self.nf(w))))
            terms.append((c.subs(self.T,-self.T),self.delta_word(w)))
        return self.add(*terms)

    # Ore quotient element represented by (coefficient without w, coefficient of w).
    def oadd(self,*terms):
        return tuple(self.add(*[(c,p[j]) for c,p in terms]) for j in range(2))

    def omul(self,p,q):
        a,b=p;c,d=q
        constant=self.add((1,self.mul(a,c)),(1,self.mul(b,self.delta(c))),
                          (self.Y,self.mul(b,self.sigma(d))))
        linear=self.add((1,self.mul(a,d)),(1,self.mul(b,self.sigma(c))),
                        (1,self.mul(b,self.delta(d))))
        return constant,linear


def main():
    M=Model();P,X,Y,T=M.P,M.X,M.Y,M.T
    a,b,c,d,e,f,g,h=M.parameters
    # Every defining Clifford relation is preserved by sigma and delta.
    relations=[]
    for word,tail in M.rules.items():relations.append(M.add((1,{word:S.Integer(1)}),(-1,tail)))
    for rel in relations:
        assert not M.sigma(rel) and not M.delta(rel)
    for gen in M.gens+[{():T}]:
        assert not M.add((1,M.sigma(M.sigma(gen))),(-1,gen))
        assert not M.add((1,M.delta(M.sigma(gen))),(1,M.sigma(M.delta(gen))))
        assert not M.delta(M.delta(gen))
    # The ten Clifford overlap checks are independent of the Ore argument.
    count=0
    for word in itertools.product(range(3),repeat=3):
        if word[:2] in M.rules and word[1:] in M.rules:
            left=M.add(*[(cc,M.nf(w+word[2:])) for w,cc in M.rules[word[:2]].items()])
            right=M.add(*[(cc,M.nf(word[:1]+w)) for w,cc in M.rules[word[1:]].items()])
            assert not M.add((1,left),(-1,right));count+=1
    p,u,v=[(z,{}) for z in M.gens];w=({},M.one)
    gens=[p,u,w,v];mu=[1,-1,-1,-1]
    Tc=({():T},{})
    G=M.oadd((1,M.omul(Tc,w)),(-M.B,p))
    assert G[1]=={():T}  # A fixed nonzero PBW coefficient.
    for gen,sign in zip(gens,mu):
        assert not any(M.oadd((1,M.omul(G,gen)),(-sign,M.omul(gen,G))))
        assert not any(M.oadd((1,M.omul(M.omul(Tc,Tc),gen)),(-1,M.omul(gen,M.omul(Tc,Tc)))))
    assert not any(M.oadd((1,M.omul(G,G)),(-(M.B*M.B*P-T*T*Y),(M.one,{}))))
    # Orthogonality of the stated quadratic dual presentation.
    words=list(itertools.product(range(4),repeat=2));index={z:j for j,z in enumerate(words)}
    def vec(poly):
        out=S.zeros(16,1)
        for ww,cc in poly.items():out[index[ww]]+=cc
        return out
    R=[{(0,1):1,(1,0):1},{(0,2):1,(2,0):-1},{(1,2):1,(2,1):1},
       {(1,3):1,(3,1):1,(0,0):-a,(1,1):-b,(2,2):-c},
       {(2,3):1,(3,2):1,(0,0):-d,(1,1):-e,(2,2):-f},
       {(3,3):1,(1,1):-g,(2,2):-h}]
    dual=[]
    for i,j in [(1,2),(1,3),(2,3),(0,1)]:dual.append({(i,j):1,(j,i):-1})
    dual += [{(0,2):1,(2,0):1},{(0,3):1},{(3,0):1},
             {(0,0):1,(1,3):a/2,(3,1):a/2,(2,3):d/2,(3,2):d/2},
             {(1,1):1,(1,3):b/2,(3,1):b/2,(2,3):e/2,(3,2):e/2,(3,3):g},
             {(2,2):1,(1,3):c/2,(3,1):c/2,(2,3):f/2,(3,2):f/2,(3,3):h}]
    assert all((vec(rr).T*vec(ss))[0]==0 for rr in R for ss in dual)
    z=S.symbols('z');B0=b*d-a*e;C0=c*d-a*f
    q1=d*d*z*z+B0*z+g;q2=a*a*z*z+C0*z+h
    resultant=S.expand((d*d*h-a*a*g)**2-(d*d*C0-a*a*B0)*(B0*h-C0*g))
    assert S.expand(S.resultant(q1,q2,z)-resultant)==0
    # Every normal cubic in the AS4/domain locus is mu-fixed.  Its nine
    # possible PBW monomials give a constant-pivot rank-eight system.
    cubics=[({(0,):q},{}) for q in [P,X,Y]]+[
        ({(1,):T},{}),({(2,):T},{}),({}, {():T}),
        M.omul(M.omul(p,u),v),M.omul(M.omul(p,u),w),M.omul(M.omul(p,v),w)]
    rows={}
    for j,cubic in enumerate(cubics):
        for gi,(gen,sign) in enumerate(zip(gens,mu)):
            out=M.oadd((1,M.omul(cubic,gen)),(-sign,M.omul(gen,cubic)))
            for ep,poly in enumerate(out):
                for word,coeff in poly.items():
                    for powers,value in S.Poly(coeff,P,X,Y,T).terms():
                        rows.setdefault((gi,ep,word,powers),{})[j]=value
    remaining=list(rows.values());columns=set(range(9));pivots=0
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
    assert pivots==8 and columns=={5} and not any(remaining)
    data={
      'template':['pu=-up','pw=wp','uw=-wu','uv+vu=aP+bX+cY','wv+vw=dP+eX+fY','v²=gX+hY'],
      'central_definitions':['P=p²','X=u²','Y=w²'],
      'parameter_hypothesis':'(a,d)!=(0,0)',
      'PBW_model':'Clifford3(p,u,v) over k[P,X,Y,T], then w with sigma(p,u,v,T)=(p,-u,-v,-T), delta(v)=B,delta(T)=2Bp,delta(p/u)=0, w²=Y',
      'clifford_overlaps_checked':count,
      'flatness':'free rank16 over k[P,X,Y,T] as a left module; T is not asserted central',
      'central_polynomial_base':'k[P,X,Y,D=T²], free rank32',
      'normal_cubic':'G=T*w-B*p, G²=B²P-T²Y, normalizer(p,u,w,v)=(p,-u,-w,-v)',
      'normal_cubic_uniqueness':'nine mu-fixed PBW cubics, constant-pivot rank8, free coefficient T*w; W1(B)=kG on the AS4/domain locus',
      'dual':'E=Q/(PV,qP,qU,qW), Q skew polynomial with PW=-WP and all other pairs commuting',
      'dual_central_quadrics':['qP=P²+aUV+dWV','qU=U²+bUV+eWV+gV²','qW=W²+cUV+fWV+hV²'],
      'AS4_open_resultant':str(resultant),
      'resultant_compact':'(d²h-a²g)²-[d²(cd-af)-a²(bd-ae)]*[(bd-ae)h-(cd-af)g]',
      'AS4_criterion':'For (a,d)!=(0,0), the template is noetherian quadratic Koszul AS4 with mu=(p,-u,-w,-v) iff the displayed resultant is nonzero.',
      'scope':'Universal Ore/Clifford, normalizer, uniqueness, square and dual identities checked. The AS4 criterion and Koszul/Frobenius argument use the structural proof in the manuscript; no H3 sufficiency follows from a normal cubic alone.'}
    path=Path(__file__).with_name('cubic_order2_central_template_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS universal Clifford-Ore model, normal cubic, quadratic dual and AS4 resultant')


if __name__=='__main__':main()
