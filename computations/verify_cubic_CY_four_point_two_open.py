#!/usr/bin/env python3
"""Necessary full degree-one determinant-open CY charts, all exceptional branches."""
from pathlib import Path
from itertools import permutations
import json,sympy as s
from verify_cubic_as4_four_simple import source_matrix,U,K
ROOT=Path(__file__).resolve().parent;D=json.loads((ROOT/'cubic_CY_four_point_two_open_input.json').read_text());assert D['source_commit']=='6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0'
la=s.Symbol('lambda');x=s.symbols('x0:21');g=s.Symbol('g');p,q=x[2],x[10];R,A=source_matrix(la,dict(enumerate(x)));B=(A*((K.T*K).inv()*K.T*(R-U)).T).applyfunc(s.cancel)
C=s.zeros(6);C[1,4]=C[4,1]=(la+1)/8;C[2,3]=C[3,2]=-la/8
J=s.zeros(6)
for i,j,v in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=v
M=(C+g*J-B.T*A.inv()*B).applyfunc(s.cancel)
def parse(v):return s.sympify(v,locals={'lam':la})
def vals(data):return {(la if k=='lam' else s.Symbol(k)):parse(v) for k,v in data.items()}
def clean(es):return [v for v in dict.fromkeys(s.factor(s.cancel(v)) for v in es) if v!=0]
def assert_unit(expr,allowed):
 assert expr!=0
 for n in s.cancel(expr).as_numer_denom():
  vs=sorted(n.free_symbols|{la,p},key=str);poly=s.Poly(n,*vs,domain=s.QQ)
  for f in allowed:
   f=s.Poly(f,*vs,domain=s.QQ)
   while poly.total_degree()>0 and poly.rem(f).is_zero:poly=poly.exquo(f)
  assert poly.total_degree()==0 and poly.LC()!=0,(expr,poly)
def replay(eqs,trace,allowed):
 base={}
 for st in trace:
  var=s.Symbol(st['variable']);eq=parse(st['equation']);lc=parse(st['unit_pivot']);value=parse(st['value'])
  assert any(s.cancel(v-eq)==0 for v in eqs)
  poly=s.Poly(s.together(eq).as_numer_denom()[0],var);assert poly.degree()==1 and s.cancel(poly.LC()-lc)==0
  assert_unit(lc,allowed);assert s.cancel(-poly.TC()/lc-value)==0
  base={k:s.cancel(v.subs(var,value)) for k,v in base.items()};base[var]=value;eqs=clean([v.subs(var,value) for v in eqs])
 return base,eqs
units=[la,la+1,p-1];iv=s.Symbol('inverse')
def gb(eqs,unit):
 polys=[s.together(v).as_numer_denom()[0] for v in eqs]+[iv*unit-1];vs=sorted(set().union(*(v.free_symbols for v in polys)),key=str);return s.groebner(polys,*vs,order='grevlex',domain=s.QQ)
# x5 !=0, determinant nonzero.
data=D['second_shared_open'];initial={x[0]:1,x[1]:1,x[3]:0,x[4]:0,x[5]:1};base,eqs=replay(clean(M.subs(initial,simultaneous=True)),data['complete_elimination'],units)
assert set(map(str,eqs))==set(map(str,clean(map(parse,data['remaining_equations']))))
G=gb(eqs,la*(la+1)*(p-1))
for v in [q*(x[6]-x[7]),q*(p*x[6]-x[7])]:assert G.reduce(s.expand(v))[1]==0
assert list(gb([v.subs({x[6]:0,x[7]:0}) for v in eqs],q*la*(la+1)*(p-1)))==[1]
small,rest=replay(clean([v.subs(q,0) for v in eqs]),data['zero_x10_elimination'],units);assert not rest
small={q:0,**small}
normal=vals(data['normal_coefficients']);resolved={**initial,**{k:s.cancel(v.subs(small,simultaneous=True)) for k,v in base.items()},**small,q:0}
for key,value in normal.items():assert s.cancel(s.sympify(resolved.get(key,key)).subs(p,s.Symbol('p'))-value)==0,(key,resolved.get(key,key),value)
assert M.subs(normal,simultaneous=True).applyfunc(s.cancel)==s.zeros(6)
# x5=0, determinant nonzero.
data=D['zero_fifth_open'];initial={x[0]:1,x[1]:1,x[3]:0,x[4]:0,x[5]:0};base,eqs=replay(clean(M.subs(initial,simultaneous=True)),data['coverage']['unit_elimination'],units)
zero,zeroeqs=replay(clean(M.subs({**initial,q:0},simultaneous=True)),data['coverage']['q_zero_elimination'],units)
assert any(v!=0 and (s.cancel(v/(la-1)).free_symbols<={la,p}) for v in zeroeqs)
assert all(s.cancel(v.subs(la,1))==0 for v in zeroeqs)
unit_lambda=False
for v in zeroeqs:
 if not v:continue
 try:assert_unit(s.cancel(v/(la-1)),units);unit_lambda=True;break
 except (AssertionError,s.PolynomialError):pass
assert unit_lambda
zfamily=vals(data['zero_family']);zfamily={k:s.sympify(v).subs({s.Symbol('p'):p,s.Symbol('r'):x[9]},simultaneous=True) for k,v in zfamily.items()}
resolved_zero={**initial,q:0,**zero,la:1}
for key,value in zfamily.items():assert s.cancel(s.sympify(resolved_zero.get(key,key)).subs(la,1)-value)==0

# p=0 maps literally into the already H3-excluded first-shared chart.
P=s.diag(1,1/la,1/la,1/la)*s.eye(4)[:,[0,2,1,3]];PP=s.kronecker_product(P,P);lu=(U.T*U).inv()*U.T;lk=(K.T*K).inv()*K.T
SS=lu*PP*U;KK=lk*PP*K;scale=2*(SS*A*SS.T)[0,5];BP=(SS*B.subs({**initial,**base},simultaneous=True).subs(p,0)*KK.T/scale).applyfunc(s.cancel)
pos={j:next((a,b) for a in range(6) for b in range(6) if B[a,b]==x[j]) for j in range(21)};image={j:BP[a,b] for j,(a,b) in pos.items()}
assert image[0]==image[3]==image[4]==0 and image[1]==1
split=p*(-la*la+16*q*x[8])*(-la*q+la*x[8]-q)
assert any(v!=0 and not(s.cancel(v/split).free_symbols-{la,p,q}) for v in eqs)
# The split is a unit multiple of an actual residual equation.
found=False
for v in eqs:
 try:assert_unit(s.cancel(v/split),units);found=True;break
 except (AssertionError,s.PolynomialError):pass
assert found
for name,zvalue,ll,q2 in [('A',la*la/(16*q),s.Rational(1,2),-s.Rational(1,192)),('B',(la+1)*q/la,s.Integer(2),-s.Rational(1,12))]:
 es=[s.cancel(v.subs(x[8],zvalue)) for v in eqs];small=[v for v in es if not(v.free_symbols&{x[6],x[7],x[9]})]
 actual=gb(small,la*(la+1)*p*(p-1)*q);target=gb([p+2,la-ll,q*q-q2],la*(la+1)*p*(p-1)*q)
 assert [v.as_expr() for v in actual.polys]==[v.as_expr() for v in target.polys]
 vv=vals(data['coverage']['branches'][name]['normal']);assert M.subs(vv,simultaneous=True).applyfunc(s.simplify)==s.zeros(6)
 zeta=s.sqrt(3)*s.I;root=zeta/(24 if name=='A' else 6);sub={la:ll,p:-2,q:root,x[8]:zvalue.subs({la:ll,q:root},simultaneous=True)}
 residual=s.Matrix([s.simplify(v.subs(sub,simultaneous=True)) for v in eqs]);free=[x[6],x[7],x[9]]
 assert residual.subs(dict.fromkeys(free,0))==s.zeros(len(residual),1)
 finiteG=s.groebner(list(residual),*free,domain=s.QQ.algebraic_field(s.sqrt(3)*s.I))
 for variable in free:assert any(finiteG.reduce(variable**power)[1]==0 for power in range(1,9))

# Exact literal relation transport of all four exceptional candidates from old N.
special=vals(data['special']);RN=R.subs(special,simultaneous=True).applyfunc(s.simplify);BN=B.subs(special,simultaneous=True);AN=A.subs(la,2);targets={}
for name in ['A','B']:
 vv=vals(data['coverage']['branches'][name]['normal'])
 for sign in [-1,1]:
  choice={k:s.simplify(v.subs(s.I,sign*s.I)) for k,v in vv.items()};targets[name+str(sign)]=R.subs(choice,simultaneous=True).applyfunc(s.simplify)
matched={}
for perm in permutations(range(4)):
 P=s.eye(4)[:,perm];PP=s.kronecker_product(P,P);SS=lu*PP*U;KK=lk*PP*K;sc=s.factor(2*(SS*AN*SS.T)[0,5]);BP=(SS*BN*KK.T/sc).applyfunc(s.simplify);beta=BP[pos[1][0],pos[1][1]];b0=BP[pos[0][0],pos[0][1]]
 if not beta or not b0:continue
 T=s.diag(1,beta/b0,1,beta);G=s.kronecker_product(T*P,T*P)*RN;change=(lu*G).applyfunc(s.simplify)
 if not change.det():continue
 for name,target in targets.items():
  if (target*change-G).applyfunc(s.simplify)==s.zeros(16,6):matched[name]={'permutation':perm,'diagonal':list(map(str,T.diagonal()))}
assert set(matched)==set(targets)
from verify_cubic_as4_four_simple_zero_fifth import m_matrix
for eps in [0,1]:
 expected,_=m_matrix(p,eps);actual=R.subs(zfamily,simultaneous=True).subs(x[9],eps)
 assert (actual-expected).applyfunc(s.cancel)==s.zeros(16,6)
oldN,_=source_matrix(s.Integer(2),{0:1,1:1,2:-2,8:s.sqrt(3)*s.I/4,10:s.sqrt(3)*s.I/6,11:s.sqrt(3)*s.I/6,16:s.sqrt(3)*s.I/6,15:-s.sqrt(3)*s.I/12,14:s.Rational(1,12),19:s.Rational(1,12),20:s.Rational(1,12)})
assert (RN-oldN).applyfunc(s.simplify)==s.zeros(16,6)
P=s.Symbol('p');oldH,_=source_matrix(la,{0:1,1:1,2:P,5:1,9:(la*la-1)/16,14:la*la/(16*(P-1)),19:-la/(16*(P-1)),20:P/(16*(P-1))})
assert (R.subs(normal,simultaneous=True)-oldH).applyfunc(s.cancel)==s.zeros(16,6)

out={'status':'PASS','source_commit':D['source_commit'],'scope':'both full degree1 x0 nonzero determinant-open CY charts are H3 empty','coverage':'all unit elimination equations independently replayed; FO vector consequences and empty ideal; FZ q-zero/lambda1, p-zero original matrix transport into first chart, both saturated finite-branch ideals','all_four_exceptional_literal_transports':matched,'ordinary_dependencies':['independent torus normalization over algebraically closed field','p-1 and every recorded nonzero coefficient kept as units','existing all-value H/M/N exclusions','full necessary branch derivations and isolated pinned upstream controller replays'],'not_claimed':['determinant-zero boundaries covered','all degree2 or full shared supports excluded','AS sufficiency/full automorphisms imported','relative scheme cover','full H3 classification','novelty confirmed']}
(ROOT/'cubic_CY_four_point_two_open_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS both full determinant-open charts, all unit eliminations/saturated finite branches and four literal N transports')
