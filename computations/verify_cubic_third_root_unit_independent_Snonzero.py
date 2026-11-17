#!/usr/bin/env python3
"""Full original Schur parameterization, off-axis finite inputs, axis pivot
cover and fresh algebraic boundary fields. Ordinary rank-case exhaustion is
in the manuscript; all displayed coefficient and finite elimination inputs
are independently regenerated here.
"""
import itertools,json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1));O=s.Symbol('omega')
l,p,r,c,d=s.symbols('l p r c d');a=s.symbols('a:22')
def red(e):
 e=s.expand(e).replace(lambda n:n.is_Pow and n.base==O and n.exp.is_Integer,lambda n:O**(int(n.exp)%3))
 return s.rem(s.expand(e),O*O+O+1,O)
# Original22 twisted orbits; the Schur constant a11+omega is checked.
seen=set();tops=[];weights=[0,0,1,2]
for w in itertools.product(range(4),repeat=4):
 if w in seen:continue
 T={};v=w;co=F.one
 while v not in T:
  T[v]=co;seen.add(v);v=(v[-1],)+v[:-1];co=-co/F.unit**weights[v[0]]
 if co==F.one:tops.append(T)
assert len(tops)==22
def expr(co):
 cs=co.to_list();return sum(s.Rational(v.numerator,v.denominator)*O**(len(cs)-j-1) for j,v in enumerate(cs))
H=s.zeros(16)
for aa,T in zip(a,tops):
 for w,co in T.items():H[4*w[0]+w[1],4*w[2]+w[3]]+=aa*expr(co)
M=H.extract([2,6,8,9,15],[3,7,10,12,13]).subs({a[10]:1,a[18]:0,a[14]:0,a[19]:1,a[20]:1})
N=M[:4,:4] # correct columns below exclude b^2 and row c^2
J=[0,1,3,4]
N=M.extract(range(4),J)-M.extract(range(4),[2])*M.extract([4],J)/O**2
mapping={a[2]:-p*c,a[3]:l*l*O*p*c,a[6]:-r*c,a[7]:1-l*l*O*p*d,
 a[8]:-l*p*c,a[9]:l*r*c,a[11]:p*d-O,a[12]:-l*O*r*c,a[13]:l*l*O*r*c,
 a[15]:-r*d,a[16]:l*l*O*r*d,a[17]:l*r*d}
u=s.Matrix([p,r,l*p,-l*r]);v=s.Matrix([-l*c,l*d,c,d]);f=l*(p*d-r*c)+1
for entry in (N.subs(mapping)-u*v.T):
 entry=red(entry)
 assert entry==0 or s.cancel(entry/f).free_symbols<={O}
assert red(N[0,3]-(a[11]+O))==0

def analyze(K,R,o,parameters=(),normal=True):
 one=K.one;zero=K.zero
 relation_log=[]
 def echelon(rows,log):
  piv={}
  for row in rows:
   row={j:co for j,co in row.items() if co}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j];log.append(co);piv[j]={k:v/co for k,v in row.items()};break
    co=row[j]
    for k,v in piv[j].items():
     row[k]=row.get(k,zero)-co*v
     if not row[k]:row.pop(k,None)
  return piv
 def reduce(row,P):
  row=dict(row)
  for j,poly in sorted(P.items()):
   co=row.get(j,zero)
   if co:
    for k,v in poly.items():
     row[k]=row.get(k,zero)-co*v
     if not row[k]:row.pop(k,None)
  return row
 def factors(log):
  out=set()
  if not parameters:return out
  for co in log:
   for poly in [co.numer,co.denom]:
    for g,e in s.Poly(poly.as_expr(),*parameters,domain=F).factor_list()[1]:out.add(g.monic().as_expr())
  return out
 WS={n:list(itertools.product(range(4),repeat=n)) for n in [3,4]};IS={n:{w:j for j,w in enumerate(WS[n])} for n in [3,4]};Ps={}
 quad=echelon([{4*w[0]+w[1]:co for w,co in rel.items() if co} for rel in R],[]);assert len(quad)==6
 for n in [3,4]:
  rows=[]
  for rel in R:
   for left in range(n-1):
    for pre in itertools.product(range(4),repeat=left):
     for post in itertools.product(range(4),repeat=n-left-2):rows.append({IS[n][pre+w+post]:co for w,co in rel.items() if co})
  Ps[n]=echelon(rows,relation_log)
 out={'B3_B4_dimensions':[4**n-len(Ps[n]) for n in [3,4]]}
 if parameters:out['relation_pivot_factors']=[str(g) for g in sorted(factors(relation_log),key=str)]
 if not normal:return out,quad,reduce
 free=[w for j,w in enumerate(WS[3]) if j not in Ps[3] and sum(weights[t] for t in w)%3==0]
 inv=[one,one,o**2,o];cols=[]
 for w in free:
  result={}
  for j in range(4):
   row={IS[4][w+(j,)]:one};k=IS[4][(j,)+w];row[k]=row.get(k,zero)-inv[j]
   for k,co in reduce(row,Ps[4]).items():result[j*256+k]=co
  cols.append(result)
 keys=sorted(set().union(*(set(co) for co in cols)));rows=[{j:co[k] for j,co in enumerate(cols) if k in co} for k in keys]
 log=[];pivot=echelon(rows,log);assert len(free)==8 and len(pivot)==8
 out.update({'normal_coefficient_dimension':8,'normal_rank':8})
 if parameters:out['normal_pivot_factors']=[str(g) for g in sorted(factors(log),key=str)]
 return out,quad,reduce

def mixed(K,o,l,p,r,c,d):
 one=K.one
 return [{(0,2):p,(1,2):r,(2,0):l*p,(2,1):-l*r},
  {(0,2):one,(2,0):-o**2,(3,3):o**2},
  {(0,3):-l*c,(1,3):l*d,(3,0):c,(3,1):d},
  {(1,3):o**2,(2,2):o**2,(3,1):-one}]
def even_from_PC(K,o,lam,T,P):
 det=-o*T*T-o*o;inv=[[-o*T/det,o/det],[o/det,T/det]]
 PC=[[sum((P[j][v]*inv[v][k] for v in range(2)),K.zero) for k in range(2)] for j in range(4)]
 words=[(0,0),(0,1),(1,0),(1,1)]
 return [{w:K.one,**{words[j]:PC[j][k] for j in range(4)}} for k,w in enumerate([(2,3),(3,2)])]
def check_top(K,o,coeff,quad,reduce):
 HH=[[K.zero for j in range(16)] for k in range(16)]
 for aa,top in zip(coeff,tops):
  for w,co in top.items():
   lifted=K.zero
   for qq in co.to_list():lifted=lifted*o+K.convert(qq)
   HH[4*w[0]+w[1]][4*w[2]+w[3]]+=aa*lifted
 assert all(not reduce({k:HH[k][j] for k in range(16) if HH[k][j]},quad) for j in range(16))
 dm=DomainMatrix.from_dod({k:{j:HH[k][j] for j in range(16) if HH[k][j]} for k in range(16)},(16,16),K)
 assert dm.rank()==6

finite=[];o=F.unit;one=F.one;zero=F.zero
for lam in [-one,-o]:
 m=lam*lam*o;X=one/(4*m)+o/4+one/(2*lam);Y=one/(4*m)+o/4-one/(2*lam);T=2*m/(lam**4*o-one)
 P=[[-X,m*X],[-X,one-m*Y],[-Y+o,-m*X],[-Y,m*Y]]
 R=mixed(F,o,lam,one,one,X,Y)+even_from_PC(F,o,lam,T,P)
 result,quad,reduce=analyze(F,R,o,normal=False)
 assert result['B3_B4_dimensions']==[22,46]
 # Check original top-image equality, including a11=Y-omega.
 inv=[[-o*T/(-o*T*T-o*o),o/(-o*T*T-o*o)],[o/(-o*T*T-o*o),T/(-o*T*T-o*o)]]
 inner=lambda x,y:sum((x[j]*inv[j][k]*y[k] for j in range(2) for k in range(2)),zero)
 coeff=[inner(P[0],P[1]),zero,-X,m*X,inner(P[1],P[1]),inner(P[1],P[3]),-X,one-m*Y,-lam*X,lam*X,one,Y-o,-lam*o*X,m*X,zero,-Y,m*Y,lam*Y,zero,one,one,T]
 check_top(F,o,coeff,quad,reduce)
 finite.append({'lambda':str(F.to_sympy(lam)),**result,'exclusion':'B3 dimension22 !=20','original_top_image_equal_relations':True})

L=s.Symbol('L');K=F.frac_field(L);lam=K.gens[0];o=K.convert(F.to_sympy(F.unit));one=K.one;zero=K.zero
T=2*o*lam/(lam*lam-o);P=[[zero,zero],[-one/lam,one],[o,-lam*o],[zero,zero]]
R=mixed(K,o,lam,zero,one,one/lam,zero)+even_from_PC(K,o,lam,T,P)
# Verify the off-axis binary compatibility has only two roots after all
# explicitly excluded units are removed; no numerical root sampling.
m=lam*lam*o;XX=one/(4*m)+o/4+one/(2*lam);YY=one/(4*m)+o/4-one/(2*lam)
TT=2*m/(lam**4*o-one);det=-o*TT*TT-o*o
PP=[[-XX,m*XX],[-XX,one-m*YY],[-YY+o,-m*XX],[-YY,m*YY]]
metric=lambda x,y:(-o*TT*x[0]*y[0]+o*(x[0]*y[1]+x[1]*y[0])+TT*x[1]*y[1])/det
compat=metric(PP[1],PP[2]);units=s.Poly(L*(F.to_sympy(F.unit)*L**4-1)*(F.to_sympy(F.unit)*L**4+1),L,domain=F)
remaining=[]
for factor,power in s.Poly(compat.numer.as_expr(),L,domain=F).factor_list()[1]:
 factor=factor.monic()
 if s.gcd(factor,units).degree()==0:remaining.append(factor)
assert set(remaining)=={s.Poly(L+1,L,domain=F),s.Poly(L+F.to_sympy(F.unit),L,domain=F)}
axis,quad,reduce=analyze(K,R,o,[L])
coeff=[zero,zero,zero,zero,zero,zero,-one/lam,one,zero,one,one,-o,-o,lam*o,zero,zero,zero,zero,zero,one,one,T]
check_top(K,o,coeff,quad,reduce)
assert axis['B3_B4_dimensions']==[20,35]
oe=F.to_sympy(F.unit)
def polys(strings):return {s.Poly(s.sympify(x),L,domain=F).monic() for x in strings}
expected_rel=[L,L-oe**2,L+oe**2,L*L+oe,L**4+4*oe*L*L-oe**2]
expected_normal=[L,L-1,L+1,L-oe,L+oe,L-oe**2,L+oe**2]
assert polys(axis['relation_pivot_factors'])=={s.Poly(g,L,domain=F).monic() for g in expected_rel}
assert polys(axis['normal_pivot_factors'])=={s.Poly(g,L,domain=F).monic() for g in expected_normal}
exceptions=[]
for lam in [F.one,-F.one,F.unit,-F.unit]:
 o=F.unit;T=2*o*lam/(lam*lam-o);P=[[F.zero,F.zero],[-F.one/lam,F.one],[o,-lam*o],[F.zero,F.zero]]
 R=mixed(F,o,lam,F.zero,F.one,F.one/lam,F.zero)+even_from_PC(F,o,lam,T,P)
 result,_,_=analyze(F,R,o)
 assert result['B3_B4_dimensions']==[20,35]
 exceptions.append({'lambda':str(F.to_sympy(lam)),**result})
h=L**8-4*L**6+17*L**4+4*L**2+1;assert s.Poly(h,L).is_irreducible
J=s.QQ.alg_field_from_poly(s.Poly(h,L));lam=J.unit;one=J.one;zero=J.zero;o=-(lam**4+one)/(4*lam*lam+one)
assert o*o+o+one==zero and lam**4+4*o*lam*lam-o*o==zero
T=2*o*lam/(lam*lam-o);P=[[zero,zero],[-one/lam,one],[o,-lam*o],[zero,zero]]
R=mixed(J,o,lam,zero,one,one/lam,zero)+even_from_PC(J,o,lam,T,P)
root_exception,_,_=analyze(J,R,o)
assert root_exception['B3_B4_dimensions']==[20,35]
singular=[];g=L**4-L**2+1;assert s.Poly(g,L).is_irreducible
J=s.QQ.alg_field_from_poly(s.Poly(g,L));lam=J.unit;one=J.one;zero=J.zero;o=-lam*lam
assert o*o+o+one==zero
for sign in [-1,1]:
 R=mixed(J,o,lam,zero,one,one/lam,zero)+[{(0,1):one,(1,0):sign*lam*o},
  {(2,3):one,(3,2):-lam,(0,1):-o**2,(1,0):lam}]
 result,quad,reduce=analyze(J,R,o)
 assert result['B3_B4_dimensions']==[20,35]
 j=zero if sign==-1 else -2*one/(lam**3)
 coeff=[zero,zero,zero,zero,j,zero,-one/lam,one,zero,one,one,-o,-o,lam*o,zero,zero,zero,zero,zero,one,one,-lam]
 check_top(J,o,coeff,quad,reduce)
 singular.append({'pure_U_sign':sign,'field':'L^4-L^2+1; omega=-L^2',**result})
out={'status':'PASS','scope':'original Schur constants and rank1 parameterization, finite off-axis top-image equality, complete axis pivot cover, fresh root fields and singular middle boundaries; ordinary case exhaustion separate',
 'off_axis_finite_cases':finite,'axis_open':axis,'axis_four_rational_field_exceptions':exceptions,
 'axis_H_exception_field':{'minimal_polynomial':str(h),'omega':'-(L^4+1)/(4L^2+1)',**root_exception},
 'axis_singular_middle_cases':singular,'conclusion':'unit-repeat independent P,Q entirely excluded',
 'remaining_unit_repeat_sector':'rank(P,Q)=1',
 'not_claimed':['rank1 cube-coupling sector classified','nonunit semisimple spectrum classified','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_independent_Snonzero_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','independent_cube_couplings_excluded':True,'axis_singular_cases':2}))
