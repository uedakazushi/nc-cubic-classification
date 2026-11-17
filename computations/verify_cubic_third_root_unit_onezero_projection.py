#!/usr/bin/env python3
"""Original22 one-zero relation blocks and explicit projection minors.
The ordinary Ore recognition/exclusion proof is in the accompanying TeX.
"""
import itertools,json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));O=s.Symbol('omega');a=s.symbols('a:22')
def red(e):
 e=s.expand(e).replace(lambda n:n.is_Pow and n.base==O and n.exp.is_Integer,lambda n:O**(int(n.exp)%3))
 return s.rem(s.expand(e),O**2+O+1,O)
def expr(c):
 return sum(s.Rational(v.numerator,v.denominator)*O**(len(c.to_list())-j-1) for j,v in enumerate(c.to_list()))
tops=[];seen=set()
for word in itertools.product(range(4),repeat=4):
 if word in seen:continue
 w=word;c=F.one;T={}
 while w not in T:
  T[w]=c;seen.add(w);w=(w[-1],)+w[:-1];c=-c/F.unit**[0,0,1,2][w[0]]
 if c==F.one:tops.append(T)
assert len(tops)==22
H=s.zeros(16)
for aa,T in zip(a,tops):
 for w,c in T.items():H[4*w[0]+w[1],4*w[2]+w[3]]+=aa*expr(c)
base={a[10]:1,a[14]:0,a[18]:0,a[19]:0,a[20]:0}
HH=H.subs(base).applyfunc(red)
assert HH[15,:]==s.zeros(1,16)
# Thus killing x,y,b leaves no relation on c, in any coefficient specialization.
M=HH.extract([2,6,8,9,15],[3,7,10,12,13]);assert M[4,:]==s.zeros(1,5)
H0=HH.extract([0,1,4,5,11,14],[0,1,4,5,11,14]);assert H0==H0.T
H00=H0.subs(a[21],0);assert H00[4:,4:]==s.zeros(2)
R=H00[:4,4:]
def minors(cols):
 return [red(M.extract(ii,cols).det()) for ii in itertools.combinations(range(5),2)]
left,right=minors([0,1]),minors([3,4])
assert any(left) and any(right)
# A right/left projection is invertible at rank2 points iff one listed minor
# is nonzero; no unrecorded generic pivot choice is made.
rho=s.Symbol('rho')
qdet=a[3]*a[16]+a[7]*a[13]
assert red(M.extract([2,3],[0,1]).det()-(O+1)**2*qdet)==0
prop={a[2]:rho*a[3],a[6]:rho*a[7],a[11]:rho*a[13],a[15]:rho*a[16]}
assert red(M.extract([0,1],[3,4]).det().subs(prop)-rho**2*qdet)==0
# Vanishing one cross column and the forced opposite projections annihilates
# a required b-mixed basis row, exactly as in the ordinary proof.
zeros={a[j]:0 for j in [8,9,12,17]}
assert M[1,:].subs({a[j]:0 for j in [2,6,11,15]}).subs(zeros)==s.zeros(1,5)
assert M[3,:].subs({a[j]:0 for j in [3,7,13,16]}).subs(zeros)==s.zeros(1,5)
out={'status':'PASS','normalization':'P=(1,0),Q0,S0','pure_c_quotient':'k[c] at all parameters','middle_rows':['xb','yb','bx','by','cc'],'middle_columns':['xc','yc','bb','cx','cy'],'middle':[[str(v) for v in M.row(i)] for i in range(5)],'even_basis':['xx','xy','yx','yy','bc','cb'],'even':[[str(v) for v in H0.row(i)] for i in range(6)],'c_left_projection_minors':[str(v) for v in left],'c_right_projection_minors':[str(v) for v in right],'T0_cross_block':[[str(v) for v in R.row(i)] for i in range(4)],'ordinary_proof':'T0 rank2 even gives cross rank1; domain gives AS2 pure relation and invertible b projections; c projection conditions and both nonzero cross columns give actual curved Ore by spanning and full AS4 Hilbert equality','T0_full_exclusion':'domain forces both cross columns nonzero and nondegenerate pure Q; displayed minors force both c projections invertible; ordinary Ore recognition then excludes allT0','not_claimed':['all one-zero atlas covered','Tnonzero excluded','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_onezero_projection_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS original22 onezero blocks and all projection minors')
