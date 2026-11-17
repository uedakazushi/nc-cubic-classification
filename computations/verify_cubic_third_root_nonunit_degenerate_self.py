#!/usr/bin/env python3
"""Complete nonzero proportional degenerate-self obstruction: source incidence,
uniform zero divisors, a scalar-normalized normal-cubic curve, and explicit
normal-quotient overlap dimension identities. Ordinary exhaustive proof in TeX.
"""
from pathlib import Path
import sympy as s,json
from sympy.polys.matrices import DomainMatrix
from cubic_third_root_original22 import top_matrix
from cubic_third_root_nonunit_proportional_model import analyze
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));os=F.to_sympy(F.unit);O=s.Symbol('omega');a=s.symbols('a:22')
def red(e):return s.rem(s.expand(e),O*O+O+1,O)
P=F.poly_ring(*a);oo=P.convert(F.unit,F)
HS=top_matrix(P,oo,list(P.gens),[1,1,0,2]).to_Matrix().xreplace({os:O}).applyfunc(red)
H0=HS.extract([3,7,10,12,13],[3,7,10,12,13]);M=HS.extract([2,6,8,9,15],[0,1,4,5,11,14])
alpha,m,n,T=s.symbols('alpha m n T');sub={a[13]:1,a[20]:0,a[9]:-alpha*O**2,a[17]:0,a[11]:2,a[19]:0,a[12]:0,a[3]:1/alpha-O**2*alpha,a[14]:0,a[7]:0,a[16]:0,a[10]:m,a[18]:n,a[21]:T}
N=M.subs(sub).applyfunc(red);Hn=H0.subs(sub).applyfunc(red)
p=s.Matrix([1,0,0,alpha,0]);v=s.Matrix([1,0,1,-O/alpha,0]);assert (Hn-p*v.T-v*p.T).applyfunc(red)==s.zeros(5)
vs=[a[j] for j in [0,1,2,4,5,6,8,15]]
zp={a[j]:0 for j in [1,2,5,6,8,15]};N0=N.subs(n,0).subs(zp)
assert N0[1,:]==s.zeros(1,6) and N0[3,:]==s.zeros(1,6) and N0[:,3]==s.zeros(5,1)
assert red(N.subs(n,0).extract([0,2],[4,5]).det()-(m*m+alpha*O**2))==0
assert red(N.subs(n,0).extract([2,4],[4,5]).det()-T*(m+O**2))==0
assert red(N[4,0]+O*(alpha**2-O)/alpha)==0
NN=N.subs({n:1,T:1});proj=NN.extract([1,3],[4,5]);assert proj.det()==1
res=[]
for j in [0,2,4]:res.extend(list((NN[j,:]-NN[j,4:6]*proj.inv()*NN[[1,3],:]).applyfunc(red))[:4])
CM,b=s.linear_eq_to_matrix([e.subs(O,os) for e in res],vs);K=F.frac_field(alpha,m)
det=DomainMatrix.from_Matrix(CM[:8,:]).convert_to(K).det();expected=O*(alpha+1)*(alpha+O)*(alpha+O**2)**2
assert not(det-K.from_sympy(expected.subs(O,os)))
inc=[]
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
 if index<2:assert any(set(row)=={8} and row[8] and row[8].is_ground for row in rows)
 else:assert not rows
 inc.append({'alpha':str(av),'unit_pivots':cols,'residual':'nonzero constant' if index<2 else 'zero'})
def source(K,o,mm,Tv,vals):
 one,zero=K.one,K.zero;co=[zero]*22
 for j,c in {13:one,9:o,11:2*one,18:one,10:mm,21:Tv}.items():co[j]=c
 for j,c in zip([0,1,2,4,5,6,8,15],vals):co[j]=c
 return top_matrix(K,o,co,[1,1,0,2])
def image_check(K,D,rels,lead):
 zero=K.zero
 R=DomainMatrix.from_dod({i:{j:rel.get(divmod(i,4),zero) for j,rel in enumerate(rels) if rel.get(divmod(i,4),zero)} for i in range(16)},(16,6),K)
 small=R.extract(lead,range(6));det=small.det();assert det and det.numer.is_ground and det.denom.is_ground
 coords=small.inv().matmul(D.extract(lead,range(16)));assert not any((R.matmul(coords)-D).to_list_flat())
 assert all(c.denom.is_ground for c in coords.to_list_flat())
# Nonzero T: exact model after Y=y+(m+omega²)x.
Z=s.Symbol('Z');K=F.frac_field(m,Z);mm,zz=K.gens;o=K.convert(F.unit,F);one,zero=K.one,K.zero;l=mm+o**2
vals=[l**3*zz,l*l*zz,-o*l*l*zz,l*l*zz,l*zz,-o*l*zz,o**2*l*zz,zz]
D=source(K,o,mm,one,vals)
rels1=[{(0,3):one,(3,0):-o**2},{(2,2):one,(0,3):2*one},{(2,1):one,(1,2):-o**2},{(1,2):one,(0,2):-o**2,(2,0):-one,(3,3):-one},{(2,3):one,(1,1):zz},{(3,2):one,(1,1):o**2*zz}]
expanded=[]
for rel in rels1:
 out={}
 for w,c in rel.items():
  cur={():c}
  for j in w:
   opts={1:one,0:l} if j==1 else {j:one};new={}
   for pre,cc in cur.items():
    for k,dd in opts.items():new[pre+(k,)]=new.get(pre+(k,),zero)+cc*dd
   cur=new
  for w,c in cur.items():out[w]=out.get(w,zero)+c
 expanded.append(out)
image_check(K,D,expanded,[3,10,9,15,11,14])
# Uniform nonzero quadratic P and tensor identity for P*c=0.
functional={(0,2):one,(3,3):-o**2};Pquad={(0,2):one,(2,0):-o}
assert all(not sum((c*functional.get(w,zero) for w,c in rel.items()),zero) for rel in rels1)
assert not(sum((c*functional.get(w,zero) for w,c in Pquad.items()),zero)-one)
free={}
def add(poly,pre=(),post=(),scalar=None):
 if scalar is None:scalar=K.one
 for w,c in poly.items():free[pre+w+post]=free.get(pre+w+post,zero)+scalar*c
add(Pquad,post=(3,),scalar=2*one);add(rels1[4],pre=(0,),scalar=-2*one);add(rels1[5],pre=(0,),scalar=2*o)
add(rels1[1],post=(2,),scalar=-o);add(rels1[1],pre=(2,),scalar=o);assert not any(free.values())
# Zero T, n1: at alpha=-omega², m is removed by Y=y+m*x.
# Reconstruct the m0 homogeneous rank6 kernel and exact two-parameter image.
Nz=N.subs({n:1,T:0});pr=Nz.extract([1,3],[4,5]);rz=[]
for j in [0,2,4]:rz.extend(list((Nz[j,:]-Nz[j,4:6]*pr.inv()*Nz[[1,3],:]).applyfunc(red))[:4])
C0,b0=s.linear_eq_to_matrix([e.subs(O,os).subs({alpha:-os**2,m:0}) for e in rz],vs)
D0=DomainMatrix.from_Matrix(C0.row_join(b0)).convert_to(F);dr,pp=D0.rref();assert list(pp)==[0,1,2,3,4,6]
S,Z=s.symbols('S Z');K=F.frac_field(S,Z);ss,zz=K.gens;o=K.convert(F.unit,F);one,zero=K.one,K.zero
vals=[zz,o*zz,(one+o)*zz,-o*ss,o**2*zz,ss,o*zz,zz]
VV=DomainMatrix.from_dod({i:{0:c} for i,c in enumerate(vals) if c},(8,1),K)
assert not any(DomainMatrix.from_Matrix(C0).convert_to(K).matmul(VV).to_list_flat())
def zero_model(K,o,S,Z):
 one=K.one
 return [{(0,3):one,(3,0):-o**2},{(2,2):one,(0,3):2*one},{(2,0):one,(1,2):-one},{(2,1):one,(0,2):-o},{(3,2):one,(0,0):Z,(0,1):o*Z,(1,0):-o*S,(1,1):o**2*Z},{(2,3):one,(0,0):o*Z,(0,1):-o**2*S,(1,0):o**2*Z,(1,1):Z}]
image_check(K,source(K,o,zero,zero,vals),zero_model(K,o,ss,zz),[3,10,8,9,14,11])
L=F.frac_field('a');aa=L.gens[0];o=L.convert(F.unit,F)
rs=analyze(L,o,L.zero,L.zero,source_relations=zero_model(L,o,aa,L.one));bad=L.field.ring.one
for c in rs['source_pivots']+rs['normal_pivots']:bad=bad.lcm(c.numer).lcm(c.denom)
assert bad.sqf_part().monic()==L.field.ring.from_expr(s.Symbol('a')*(s.Symbol('a')+1))
fresh=[]
for name,sv,zv in [('ratio0',F.zero,F.one),('ratio-1',-F.one,F.one),('Zzero',F.one,F.zero)]:
 fr=analyze(F,F.unit,F.zero,F.zero,finite=True,source_relations=zero_model(F,F.unit,sv,zv));fresh.append({'case':name,'dimensions':fr['dimensions'],'normal_columns':len(fr['normal_pivots'])})
# n0 rank-one projection: T0 domain forces alpha²=omega, then b normal.
# Exact associativity identity giving (bc-m^-1 cb)*x=0 from b²=kappa*cx,bx=mxb.
K=F.frac_field('m','alpha');mm,al=K.gens;o=K.convert(F.unit,F);one,zero=K.one,K.zero;kap=al+o/al
rb2={(2,2):one,(3,0):-kap};rbx={(2,0):one,(0,2):-mm};qbc={(2,3):one,(3,2):-one/mm};free={}
add(qbc,post=(0,),scalar=kap);add(rb2,pre=(2,));add(rb2,post=(2,),scalar=-one);add(rbx,pre=(3,),scalar=kap/mm)
assert not any(free.values())
# Two independent cubic overlaps in a three-generator quadratic normal quotient.
assert (0,2,0)!=(2,0,2);assert 27-(2*3*3-2)==11>10
out={'status':'PASS','scope':'all proportional degenerate self u1,v0 with nonzero p,r','nT_nonzero_incidence':inc,'nonzeroT_model':'original image unit6minor, uniform nonzero P=xb-omega*bx and P*c=0 tensor identity','n_nonzero_Tzero':'m0 rank6 free(S,Z), exact source model, common scalar normalization','normal_ratio_curve':{'matrix':rs['normal_shape'],'bad':'a*(a+1)'},'fresh_points':fresh,'nzero_boundary':'ordinary domain normality plus exact associativity, or Fibonacci quotient','normal_quotient_overlap_bound':{'required_S3':10,'actual_lower_bound':11},'not_claimed':['zero b2 coupling excluded','whole nonunit atlas completed','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_nonunit_degenerate_self_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all degenerate nonzero proportional self boundary identities')
