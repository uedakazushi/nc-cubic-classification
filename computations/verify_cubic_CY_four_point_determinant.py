#!/usr/bin/env python3
"""Entire degree-one determinant-zero boundary with x5 nonzero, to old R/J."""
from pathlib import Path
from itertools import combinations
import json,sympy as s
from verify_cubic_as4_four_simple import source_matrix,U,K
from verify_cubic_as4_four_simple_boundary_R import r_matrix
from verify_cubic_as4_four_simple_boundary_J import j_matrix
ROOT=Path(__file__).resolve().parent;D=json.loads((ROOT/'cubic_CY_four_point_determinant_input.json').read_text());assert D['source_commit']=='6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0'
la=s.Symbol('lambda');x=s.symbols('x0:21');g=s.Symbol('g');h=s.Symbol('h');R,A=source_matrix(la,dict(enumerate(x)));B=(A*((K.T*K).inv()*K.T*(R-U)).T).applyfunc(s.cancel)
C=s.zeros(6);C[1,4]=C[4,1]=(la+1)/8;C[2,3]=C[3,2]=-la/8;J=s.zeros(6)
for i,j,v in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=v
M=(C+g*J-B.T*A.inv()*B).applyfunc(s.cancel)
def parse(v):return s.sympify(v,locals={'lam':la})
def vals(data):return {(la if k=='lam' else s.Symbol(k)):parse(v) for k,v in data.items()}
def clean(es):return [v for v in dict.fromkeys(s.factor(s.cancel(v)) for v in es) if v!=0]
def unit(v):
 assert v!=0 and v.free_symbols<={la}
 for n in s.cancel(v).as_numer_denom():
  poly=s.Poly(n,la,domain=s.QQ_I)
  for f in [s.Poly(la,la,domain=s.QQ_I),s.Poly(la+1,la,domain=s.QQ_I)]:
   while poly.degree()>0 and poly.rem(f).is_zero:poly=poly.exquo(f)
  assert poly.degree()==0 and poly.LC()!=0

def replay(eqs,trace):
 base={}
 for st in trace:
  var=s.Symbol(st['variable']);eq=parse(st['equation']);pivot=parse(st['unit_pivot']);value=parse(st['value'])
  assert any(s.cancel(v-eq)==0 for v in eqs)
  poly=s.Poly(s.together(eq).as_numer_denom()[0],var);assert poly.degree()==1 and s.cancel(poly.LC()-pivot)==0
  unit(pivot);assert s.cancel(-poly.TC()/pivot-value)==0
  base={k:s.cancel(v.subs(var,value)) for k,v in base.items()};base[var]=value;eqs=clean([v.subs(var,value) for v in eqs])
 return base,eqs

def compose(*parts):
 vv={k:s.sympify(v) for part in parts for k,v in part.items()}
 for _ in range(20):
  new={k:s.cancel(v.subs(vv,simultaneous=True)) for k,v in vv.items()}
  if new==vv:return vv
  vv=new
 raise AssertionError('coefficient substitution cycle')
initial={x[0]:1,x[1]:1,x[2]:1,x[5]:1,x[3]:0,x[4]:0};data=D['coverage'];_,eqs=replay(clean(M.subs(initial,simultaneous=True)),data['initial_unit_elimination'])
first=(la+1)*(16*(x[15]-x[16])**2+1)/8
assert any(s.cancel(v+w-first)==0 for v,w in combinations(eqs,2))
signed={**initial,x[16]:x[15]-s.I/4};base,eqs=replay(clean(M.subs(signed,simultaneous=True)),data['signed_unit_elimination'])
assert set(map(str,eqs))==set(map(str,clean(map(parse,data['signed_remaining_equations']))))
second=x[9]*(16*x[9]-la*la+1);found=False
for v in eqs:
 try:unit(s.cancel(v/second));found=True;break
 except (AssertionError,s.PolynomialError):pass
assert found
sat=s.Symbol('sat')
def gb(eqs):return s.groebner([s.together(v).as_numer_denom()[0] for v in eqs]+[sat*la*(la+1)-1],sat,x[14],x[12],la,domain=s.QQ_I)
def same(G,H):assert [v.as_expr() for v in G.polys]==[v.as_expr() for v in H.polys]
same(gb([v.subs(x[9],(la*la-1)/16) for v in eqs]),gb([x[12],16*(la+1)**2*x[14]-la**4]))
zero_constraints=[(la-1)*(la*la+1),x[12]*(la*la+1),16*(la+1)**2*(x[14]-x[12]**2)-la*la]
same(gb([v.subs(x[9],0) for v in eqs]),gb(zero_constraints))
# Signed delta=+i/4 branch. Its conjugate with formal lambda fixed gives the other sign.
rvals=compose(signed,base,{x[9]:(la*la-1)/16,x[12]:0,x[14]:la**4/(16*(la+1)**2)})
candidate=vals(D['R_candidate'])
for key,value in candidate.items():assert s.cancel(rvals.get(key,key)-value)==0
for eta in [1,-1]:
 vv={k:v.xreplace({s.I:eta*s.I}) for k,v in rvals.items()};target,_=r_matrix(la,eta)
 assert (R.subs(vv,simultaneous=True)-target).applyfunc(s.cancel)==s.zeros(16,6)
# lambda=1 in the zero branch is the same retained R_1, for both signs.
for eta in [1,-1]:
 formal={k:v.xreplace({s.I:eta*s.I}) for k,v in compose(signed,base).items()}
 vv=compose(formal,{la:1,x[9]:0,x[12]:0,x[14]:s.Rational(1,64)})
 target,_=r_matrix(1,eta);assert (R.subs(vv,simultaneous=True)-target).applyfunc(s.cancel)==s.zeros(16,6)
# Entire imaginary fibers, including h=0, literally reach the old J presentations.
lu=(U.T*U).inv()*U.T;matches=[]
for eta in [1,-1]:
 formal={k:v.xreplace({s.I:eta*s.I}) for k,v in compose(signed,base).items()}
 for ll in [s.I,-s.I]:
  vv=compose(formal,{la:ll,x[9]:0,x[12]:h,x[14]:h*h+ll/32});RR=R.subs(vv,simultaneous=True).applyfunc(s.cancel)
  assert M.subs(vv,simultaneous=True).applyfunc(s.cancel)==s.zeros(6)
  P=s.eye(4) if ll==s.I else s.diag(1,s.I,s.I,s.I)*s.eye(4)[:,[0,2,1,3]]
  transported=s.kronecker_product(P,P)*RR;change=(lu*transported).applyfunc(s.cancel);assert change.det()!=0
  found=[]
  for sign in [1,-1]:
   for hh in [h,-h,s.I*h,-s.I*h]:
    target,_=j_matrix(hh,sign)
    if (target*change-transported).applyfunc(s.cancel)==s.zeros(16,6):found.append({'target_eta':sign,'target_h':str(hh)})
  assert found;matches.append({'source_delta_sign':eta,'source_lambda':str(ll),'literal_J_transports':found})
out={'status':'PASS','source_commit':D['source_commit'],'scope':'entire x0*x1*x5 nonzero determinant-zero degree1 chart H3 empty, including all imaginary h=0 fibers','independent_checks':['both full unit elimination traces, every source equation and unit pivot','first signed split and second factor split','both saturated ideals equal complete target ideals over QQ(i)','all R signs and lambda1 literal old frames','all four signed imaginary fibers literal old J transports, no h division'],'imaginary_transports':matches,'ordinary_dependencies':['independent diagonal normalization and first signed split over algebraically closed field','existing prop:cubic-boundary-R all lambda and prop:cubic-boundary-J including h0 degree5 failure','pinned necessary FG1-FG5 proof and isolated upstream full replay'],'not_claimed':['AS sufficiency or full automorphisms imported','x5 zero determinant boundary excluded','all degree2/full supports excluded','relative reduced scheme cover','complete H3 classification','novelty confirmed']}
(ROOT/'cubic_CY_four_point_determinant_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS entire nonzero-x5 determinant boundary, all unit eliminations/saturated ideals and all R/J fibers including h0')
