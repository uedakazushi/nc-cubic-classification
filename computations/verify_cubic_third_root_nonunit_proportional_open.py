#!/usr/bin/env python3
"""All n-nonzero nondegenerate proportional-self stratum, exact char0 proof data.
Polynomial unit incidence, complete two-parameter model/four curves/two points.
"""
from pathlib import Path
import sympy as s,json
from sympy.polys.matrices import DomainMatrix
from cubic_third_root_original22 import top_matrix,relation_vector
from cubic_third_root_nonunit_proportional_model import analyze,relations
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));os=F.to_sympy(F.unit);O=s.Symbol('omega');a=s.symbols('a:22')
def red(e):return s.rem(s.expand(e),O*O+O+1,O)
P=F.poly_ring(*a);o=P.convert(F.unit,F)
HS=top_matrix(P,o,list(P.gens),[1,1,0,2]).to_Matrix().xreplace({os:O}).applyfunc(red)
M=HS.extract([2,6,8,9,15],[0,1,4,5,11,14]);H0=HS.extract([3,7,10,12,13],[3,7,10,12,13])
alpha,m,n,T=s.symbols('alpha m n T');sub={a[13]:1,a[20]:0,a[9]:-alpha*O**2,a[17]:0,a[11]:0,a[19]:0,a[12]:1,a[3]:0,a[14]:-O/alpha,a[7]:-O**2*alpha,a[16]:0,a[10]:m,a[18]:n,a[21]:T}
N=M.subs(sub).applyfunc(red);Hn=H0.subs(sub).applyfunc(red)
p=s.Matrix([1,0,0,alpha,0]);v=s.Matrix([0,1,1,0,-O/alpha]);assert (Hn-p*v.T-v*p.T).applyfunc(red)==s.zeros(5)
# For n0 and full bc/cb projection, the zero right coordinates force
# the yb/by rows and hence all yy coordinates to vanish (Fibonacci quotient).
zeroP={a[j]:0 for j in [1,2,5,6,8,15]};Nz=N.subs(n,0).subs(zeroP)
assert Nz[1,:]==s.zeros(1,6) and Nz[3,:]==s.zeros(1,6) and Nz[:,3]==s.zeros(5,1)
assert red(N.subs(n,0).extract([0,2],[4,5]).det()-(m*m+alpha*O**2))==0
assert red(N.subs(n,0).extract([2,4],[4,5]).det()-T*(m+O**2))==0
NN=N.subs({n:1,T:1});proj=NN.extract([1,3],[4,5]);assert proj.det()==1
res=[]
for i in [0,2,4]:res.extend(list((NN[i,:]-NN[i,4:6]*proj.inv()*NN[[1,3],:]).applyfunc(red))[:4])
vs=[a[j] for j in [0,1,2,4,5,6,8,15]];CM,b=s.linear_eq_to_matrix([e.subs(O,os) for e in res],vs)
K=F.frac_field(alpha,m);det=DomainMatrix.from_Matrix(CM[:8,:]).convert_to(K).det()
assert not(det-K.from_sympy((O*(alpha+1)*(alpha+O)*(alpha+O**2)**2).subs(O,os)))
incidence=[];points=[]
for index,av in enumerate([-s.Integer(1),-os,-os**2]):
 P=F.poly_ring(m);A=DomainMatrix.from_Matrix(CM.subs(alpha,av).row_join(b.subs(alpha,av))).convert_to(P);rows=list(A.to_dod().values());piv={};cols=7 if index==2 else 8
 while True:
  chosen=next(((i,j) for i,row in enumerate(rows) for j,c in row.items() if j<cols and c and c.is_ground),None)
  if chosen is None:break
  i,j=chosen;row=rows.pop(i);cc=row[j];row={k:P.exquo(c,cc) for k,c in row.items()};piv[j]=row
  for jj,old in piv.items():
   if jj!=j and j in old:
    cc=old[j]
    for k,c in row.items():old[k]=old.get(k,P.zero)-cc*c
    for k in list(old):
     if not old[k]:old.pop(k)
  for old in rows:
   if j in old:
    cc=old[j]
    for k,c in row.items():old[k]=old.get(k,P.zero)-cc*c
    for k in list(old):
     if not old[k]:old.pop(k)
  rows=[r for r in rows if r]
 assert len(piv)==cols
 if index<2:
  assert all(set(row)=={8} for row in rows);g=P.zero
  for row in rows:g=g.gcd(row[8])
  expected=P.from_sympy(m-(os if index==0 else 1));assert g.monic()==expected
  mm=F.unit if index==0 else F.one;co=[F.zero]*22;alph=F.from_sympy(av)
  for j,c in {13:F.one,9:-alph*F.unit**2,12:F.one,14:-F.unit/alph,7:-F.unit**2*alph,10:mm,18:F.one,21:F.one}.items():co[j]=c
  for j,row in piv.items():co[list(a).index(vs[j])]=row.get(8,P.zero).evaluate(0,mm)
  D=top_matrix(F,F.unit,co,[1,1,0,2]);dr,_=D.transpose().rref();rels=[{divmod(j,4):c for j,c in enumerate(row) if c} for row in dr.to_list() if any(row)]
  B=GradedAlgebra(F,4,rels,[1,1,0,2]);B.build(3);assert len(B.basis[3])==22
  points.append({'alpha':str(av),'m':str(F.to_sympy(mm)),'B3_dimension':22})
 else:assert not rows
 incidence.append({'alpha':str(av),'constant_pivots':cols,'residual':'m-omega' if index==0 else 'm-1' if index==1 else 'zero','free_a15':index==2})
# Exact polynomial parametrization and the change Y=y+(m+omega²)x.
Z=s.Symbol('Z');K=F.frac_field(m,Z);mm,zz=K.gens;o=K.convert(F.unit,F);one,zero=K.one,K.zero;l=mm+o**2
pv=[mm*(o*mm+one)+l**3*zz,o*mm+l*l*zz,-o**2*mm-o*l*l*zz,one+l*l*zz,l*zz,-o**2-o*l*zz,o**2*l*zz,zz]
CV=DomainMatrix.from_Matrix(CM.subs(alpha,-os**2)).convert_to(K);BV=DomainMatrix.from_Matrix(b.subs(alpha,-os**2)).convert_to(K)
VV=DomainMatrix.from_dod({i:{0:c} for i,c in enumerate(pv) if c},(8,1),K)
assert not any((CV.matmul(VV)-BV).to_list_flat())
co=[zero]*22;alph=-o**2
for j,c in {13:one,9:-alph*o**2,12:one,14:-o/alph,7:-o**2*alph,10:mm,18:one,21:one}.items():co[j]=c
for sym,c in zip(vs,pv):co[list(a).index(sym)]=c
D=top_matrix(K,o,co,[1,1,0,2])
expanded=[]
for rel in relations(K,o,l,zz):
 out={}
 for w,c in rel.items():
  cur={():c}
  for letter in w:
   opts={1:one,0:l} if letter==1 else {letter:one};new={}
   for pre,cc in cur.items():
    for jj,dd in opts.items():new[pre+(jj,)]=new.get(pre+(jj,),zero)+cc*dd
   cur=new
  for w,cc in cur.items():out[w]=out.get(w,zero)+cc
 expanded.append(out)
RM=DomainMatrix.from_dod({i:{j:r.get(divmod(i,4),zero) for j,r in enumerate(expanded) if r.get(divmod(i,4),zero)} for i in range(16)},(16,6),K)
lead=[3,10,9,15,11,14];small=RM.extract(lead,range(6));assert small.det() and small.det().numer.is_ground and small.det().denom.is_ground
coords=small.inv().matmul(D.extract(lead,range(16)));assert not any((RM.matmul(coords)-D).to_list_flat())
assert all(c.denom.is_ground for c in coords.to_list_flat())
# Complete normal-cubic check in the simpler (l,Z) model.
K=F.frac_field('l','Z');ll,zz=K.gens;o=K.convert(F.unit,F);rs=analyze(K,o,ll,zz)
factors=[zz,zz*ll+o/2,zz-o**2,zz-2*o**2];support=K.one
for f in factors:support*=f
support=support.numer
def supported(poly):
 while any(sum(mm)>0 for mm in poly.monoms()):
  gg=poly.gcd(support);assert any(sum(mm)>0 for mm in gg.monoms());poly=poly.exquo(gg)
for c in rs['source_pivots']+rs['normal_pivots']:supported(c.numer);supported(c.denom)
assert len(rs['normal_pivots'])==7 and all(c.numer.is_ground and c.denom.is_ground for c in rs['normal_pivots'])
curves=[];fresh=[];seen=set()
for case in ['z0','z1','z2','hyper']:
 L=F.frac_field('t');t=L.gens[0];oo=L.convert(F.unit,F)
 pars={'z0':(t,L.zero),'z1':(t,oo**2),'z2':(t,2*oo**2),'hyper':(-oo/(2*t),t)}[case]
 cr=analyze(L,oo,*pars);bad=L.field.ring.one
 for c in cr['source_pivots']+cr['normal_pivots']:bad=bad.lcm(c.numer).lcm(c.denom)
 bad=bad.sqf_part().monic();curves.append({'case':case,'bad':str(bad.as_expr()),'normal_columns':len(cr['normal_pivots'])})
 for f,pow0 in s.Poly(bad.as_expr(),s.Symbol('t'),domain=F).factor_list()[1]:
  assert f.degree()==1;cs=f.rep.to_list();tt=-cs[1]/cs[0]
  if case=='hyper' and not tt:continue
  pars0={'z0':(tt,F.zero),'z1':(tt,F.unit**2),'z2':(tt,2*F.unit**2),'hyper':(-F.unit/(2*tt),tt)}[case] if tt else (tt,F.zero)
  key=tuple(str(F.to_sympy(c)) for c in pars0)
  if key not in seen:seen.add(key);fresh.append(pars0)
for pars0 in fresh:
 fr=analyze(F,F.unit,*pars0,finite=True);assert fr['dimensions'][3]==22
assert len(fresh)==2
out={'status':'PASS','scope':'nonzero proportional b2 coupling, second self direction independent (v1), n nonzero; all parameters','source_incidence':incidence,'two_nonAS4_phase_points':points,'simple_model_parameters':['l','Z'],'source_model_identity':'originalH=displayedR*coordinates, unit6minor and only coefficient-field denominators','generic_normal_shape':rs['normal_shape'],'generic_constant_normal_pivots':7,'four_support_factors':['Z','Z*l+omega/2','Z-omega²','Z-2omega²'],'curves':curves,'fresh_points':[[list(map(str,c.to_list())) for c in pars] for pars in fresh],'fresh_dimensions3':22,'v1_remaining_necessary':['n=0,T=0,alpha=-omega*m^2,m nonzero','n=0,T nonzero,alpha=m=-omega^2'],'not_claimed':['these v1 residual branches excluded','v0 self covered','zero b2 coupling covered','wholeH3 complete']}
Path(__file__).with_name('cubic_third_root_nonunit_proportional_open_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS entire v1 n-nonzero nonunit proportional stratum',flush=True)
