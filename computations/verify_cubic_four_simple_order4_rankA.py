#!/usr/bin/env python3
"""Exhaustive paired-rank1 support atlas and three elementary domain/rank
contradictions. Symmetry is b/c exchange with primitive i renamed -i.
"""
from pathlib import Path
import itertools,json,sympy as s
from cubic_four_simple_order4_model import top
F=s.QQ_I;ii=F.from_sympy(s.I);ps=s.symbols('p:4');qs=s.symbols('q:4');pairs=[((2,3),(0,0)),((2,2),(0,1)),((3,3),(1,0)),((3,2),(1,1))]
eqs=[ps[2]*qs[3]+ps[0]*qs[0],ps[2]*qs[2]-s.I*ps[0]*qs[1],ps[3]*qs[3]+s.I*ps[1]*qs[0],ps[3]*qs[2]-ps[1]*qs[1]]
patterns=[];cover=[]
for sizep in [2,3,4]:
 for pp in itertools.combinations(range(4),sizep):
  for sizeq in [2,3,4]:
   for qq in itertools.combinations(range(4),sizeq):
    if any(((a in pp and b in qq)!=(c in pp and d in qq)) for (a,b),(c,d) in pairs):continue
    sub={ps[j]:0 for j in range(4) if j not in pp}|{qs[j]:0 for j in range(4) if j not in qq};sub[ps[pp[0]]]=1;sub[qs[qq[0]]]=1
    es=[s.expand(e.subs(sub)) for e in eqs];vs=[v for v in ps+qs if v not in sub];z=s.Symbol('z');gb=s.groebner(es+[z*s.prod(vs)-1],z,*vs,extension=s.I)
    if list(gb)==[1]:continue
    patterns.append([list(pp),list(qq)])
    assert pp==(0,2) or pp==(1,3) or qq==(0,3) or qq==(1,2) or (pp,qq) in [((0,1),(2,3)),((2,3),(0,1))]
assert len(patterns)==10
p,u,v,a0,a10,a14,a15,q=s.symbols('p u v a0 a10 a14 a15 q');vars=[p,u,v,a0,a10,a14,a15,q];K=F.frac_field(*vars);ik=K.convert(ii,F)
groups={j:[4*a+b for a in range(4) for b in range(4) if ([0,2,1,3][a]+[0,2,1,3][b])%4==j] for j in range(4)}
def blocks(co):
 cc=[K.zero]*16
 for j,e in co.items():cc[j]=K.from_sympy(s.sympify(e))
 H=top(K,ik,cc).to_Matrix();return H.extract(groups[0],groups[0]),H.extract(groups[2],groups[2]),H.extract(groups[1],groups[3])
def equal(A,B):return all(not s.cancel(e) for e in A-B)
def pf(A):return s.expand(A[0,1]*A[2,3]-A[0,2]*A[1,3]+A[0,3]*A[1,2])
# P=(1,0,p,0), Q=(u,v,i*v/p,-u/p).
c02={0:a0,10:a10,14:a14,15:a15,5:u,6:v,7:s.I*v/p,1:u/p,2:-s.I*p*u,3:-s.I*p*v}
H0,H2,M=blocks(c02);assert equal(M,s.Matrix([1,0,p,0])*s.Matrix([[u,v,s.I*v/p,-u/p]]))
assert pf(H2)==-a0*a14
assert list(H2[:,3])==[0,0,a14,0] # a14 nonzero gives pure b².
T=H2.subs(a14,0);assert T.subs({a0:0})[2,0]!=0 # a0 zero, v nonzero gives pure b².
assert list(T.subs(v,0)[:,0])==[0,a0,0,0] # v zero gives pure yx.
A=H0[:2,:2];B=H0[:2,2:];C=H0[2:,2:];S=(C-B.T*A.inv()*B).applyfunc(s.cancel).subs(a14,0)
assert s.cancel(S[0,1]+s.I*a10*u*u/a0**2)==0
assert list(H0.subs({a14:0,u:0})[:,0])==[0,a0,0,0] # pure y².
assert list(H0.subs({a14:0,a10:0,a15:0})[:,1])==[a0,0,0,0] # pure x².
assert S.subs({u:1,a10:0})==s.diag(a15,-s.I*a15)
# P=(0,1,0,p), Q=(u,v,v/p,-i*u/p).
c13={0:a0,10:a10,14:a14,15:a15,8:s.I*u,13:s.I*v,12:v/p,4:s.I*u/p,9:s.I*p*u,11:s.I*p*v}
H0,H2,M=blocks(c13);assert equal(M,s.Matrix([0,1,0,p])*s.Matrix([[u,v,v/p,-s.I*u/p]]))
assert list(H0[:,0])==[0,a0,0,0] # domain forces a0 zero.
assert list(H2[:,2])==[0,0,0,-a14] # domain forces a14 zero.
assert list(H2.subs({a0:0,a14:0})[:,0])==[0,0,0,-s.I*u/p] # u nonzero gives pure c², u zero makes H2 zero.
assert H2.subs({a0:0,a14:0,u:0})==s.zeros(4)
# P=(1,p,0,0), Q=(0,0,1,q), normalized by the nonzero top scale.
cross={0:a0,10:a10,14:a14,15:a15,7:1,1:-q,12:p,4:-p*q}
H0,H2,M=blocks(cross);assert equal(M,s.Matrix([1,p,0,0])*s.Matrix([[0,0,1,q]]))
assert pf(H2)==-a0*a14-p*q
A=H0[:2,:2];B=H0[:2,2:];C=H0[2:,2:];S=(C-B.T*A.inv()*B).applyfunc(s.cancel)
assert S[1,1]==-s.I*a15
assert s.cancel(S[0,0]-a15-q*q*a10/a0**2)==0
assert s.cancel(S[0,1]+s.I*a14-p*q/a0)==0
assert not s.expand((a0*S[0,1]).subs(a14,-p*q/a0)-(1+s.I)*p*q)
# Renaming b,c and i -> -i interchanges paired spaces:
# P basis xb,yc,bx,cy -> Q basis xc,yb,cx,by (0,1,3,2),
# Q basis xc,yb,by,cx -> P basis xb,yc,cy,bx (0,1,3,2).
perm=[0,1,3,2]
for pp,qq in patterns:
 newp=tuple(sorted(perm[j] for j in qq));newq=tuple(sorted(perm[j] for j in pp))
 assert [list(newp),list(newq)] in patterns
 assert tuple(pp) in [(0,2),(1,3)] or (tuple(pp),tuple(qq))==((0,1),(2,3)) or newp in [(0,2),(1,3)] or (newp,newq)==((0,1),(2,3))
out={'status':'PASS','scope':'whole rank(2,2,1,1) empty by exhaustive domain and middle-rank proof','support_patterns':patterns,'six_chart_cover':['P02','P13','Q03','Q12','P01-Q23','P23-Q01'],'paired_outer_equations':list(map(str,eqs)),'symmetry':'exchange b,c and rename primitive i to -i; no intrinsic orbit quotient asserted','three_chart_obstructions':{'P02':'a14zero; domain forces a0,v nonzero; u0 gives purey²; u nonzero Schur forces a10=a15zero and purex²','P13':'pure y² forces a0zero; pure c² forces a14zero; H2rank2 then forces another purec²','P01-Q23':'pfaff requires a0*a14=-p*q nonzero; H0 Schur offdiagonal gives (1+i)*p*q contradiction'},'remaining_order4_relation_ranks_weight0_2_1_3':[[2,0,2,2]],'not_claimed':['whole order4 boundary excluded','all four-simple or CY coverage','complete H3 classification','ordinary domain arguments entirely mechanically checked']}
Path(__file__).with_name('cubic_four_simple_order4_rankA_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS exhaustive rank1 support atlas and all elementary obstructions')
