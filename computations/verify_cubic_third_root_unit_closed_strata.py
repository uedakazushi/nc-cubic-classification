#!/usr/bin/env python3
"""Original22-orbit block reduction and all-parameter finite normal-kernel cover.
Smith factors plus every elimination pivot and fresh exceptions give a global
parameter check. No AS4 sufficiency or H3 completeness is asserted.
"""
import itertools,json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.matrices.normalforms import smith_normal_form
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z**2+z+1));O=s.Symbol('omega');kap=s.Symbol('kappa')
def expr(c):
 co=c.to_list();return sum(s.Rational(v.numerator,v.denominator)*O**(len(co)-j-1) for j,v in enumerate(co))
def red(e):return s.rem(s.expand(e),O**2+O+1,O)
a=s.symbols('a:22');weights=[0,0,1,2];seen=set();top=[]
for w in itertools.product(range(4),repeat=4):
 if w in seen:continue
 T={};v=w;c=F.one
 while v not in T:
  T[v]=c;seen.add(v);v=(v[-1],)+v[:-1];c=-c/F.unit**weights[v[0]]
 if c==F.one:top.append(T)
assert len(top)==22
H=s.zeros(16)
for parameter,T in zip(a,top):
 for w,c in T.items():H[4*w[0]+w[1],4*w[2]+w[3]]+=parameter*expr(c)
M=H.extract([2,6,8,9,15],[3,7,10,12,13]);H0=H.extract([0,1,4,5,11,14],[0,1,4,5,11,14])
assert (M[:,2]-s.Matrix([a[10],a[18],-O**2*a[10],-O**2*a[18],O**2*a[20]])).applyfunc(red)==s.zeros(5,1)
# Independent P,Q, S=T=0 chart; rank2 has a literal constant unit pivot.
norm={a[10]:1,a[18]:0,a[14]:0,a[19]:1,a[20]:0,a[21]:0}
M=M.subs(norm);assert M.extract([0,4],[2,4]).det()==-1
sol={a[6]:0,a[9]:0,a[12]:0,a[13]:0,a[3]:-O**2*a[2],a[8]:-O**2*a[2],
     a[7]:O**2*a[11],a[17]:O**2*a[15],a[16]:-O**2*a[15]}
pivot=M.extract([0,4],[2,4])
residual=M-M.extract(range(5),[2,4])*pivot.inv()*M.extract([0,4],range(5))
variables=[a[6],a[9],a[12],a[13],a[3],a[8],a[7],a[17],a[16]]
L,b=s.linear_eq_to_matrix([red(v) for v in residual.extract([1,2,3],[0,1,3])],variables)
unit=red(L.det());assert unit!=0 and unit.free_symbols<={O}
assert all(red(v.subs(sol))==0 for v in residual)
assert all(red(M.extract(I,J).det().subs(sol))==0 for I in itertools.combinations(range(5),3) for J in itertools.combinations(range(5),3))
H0=H0.subs(norm).subs(sol).subs(a[1],0).applyfunc(red)
assert red(H0.extract([1,2,4,5],[1,2,4,5]).det()-O*a[11]**4)==0
H0=H0.subs({a[11]:0,a[4]:0,a[5]:a[0]*a[15]/a[2]})
assert all(red(H0.extract(I,J).det())==0 for I in itertools.combinations(range(6),3) for J in itertools.combinations(range(6),3))

def analyze(K,k,o):
 one=K.one;zero=K.zero;pivot_log=[]
 def echelon(rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     c=row[j];pivot_log.append(c);piv[j]={v:d/c for v,d in row.items()};break
    c=row[j]
    for v,d in piv[j].items():
     row[v]=row.get(v,zero)-c*d
     if not row[v]:row.pop(v,None)
  return piv
 def reduce(row,P):
  row=dict(row)
  for j,p in sorted(P.items()):
   c=row.get(j,zero)
   if c:
    for v,d in p.items():
     row[v]=row.get(v,zero)-c*d
     if not row[v]:row.pop(v,None)
  return row
 R=[{(0,0):one,(1,1):one},{(2,0):one,(0,2):-o},{(3,1):one,(1,3):-o**2},
    {(2,2):one,(0,3):-o**2,(3,0):-one},{(3,3):one,(1,2):one,(2,1):o**2},
    {(2,3):one,(3,2):-o**2,(0,1):-k,(1,0):k}]
 WS={n:list(itertools.product(range(4),repeat=n)) for n in [3,4]};IS={n:{w:j for j,w in enumerate(WS[n])} for n in [3,4]};Ps={}
 for n in [3,4]:
  rows=[]
  for r in R:
   for l in range(n-1):
    for pre in itertools.product(range(4),repeat=l):
     for post in itertools.product(range(4),repeat=n-l-2):rows.append({IS[n][pre+w+post]:c for w,c in r.items() if c})
  Ps[n]=echelon(rows)
 dims=[4**n-len(Ps[n]) for n in [3,4]]
 free=[w for j,w in enumerate(WS[3]) if j not in Ps[3] and sum(weights[j] for j in w)%3==0]
 inv=[one,one,o**2,o];cols=[]
 for w in free:
  out={}
  for j in range(4):
   row={IS[4][w+(j,)]:one};v=IS[4][(j,)+w];row[v]=row.get(v,zero)-inv[j]
   for v,c in reduce(row,Ps[4]).items():out[j*256+v]=c
  cols.append(out)
 keys=sorted(set().union(*(set(c) for c in cols)))
 mat=DomainMatrix.from_dod({r:{c:col[v] for c,col in enumerate(cols) if v in col} for r,v in enumerate(keys)},(len(keys),len(cols)),K)
 return dims,mat,pivot_log,[''.join('xybc'[j] for j in w) for w in free]
K=F.frac_field(kap);k=K.gens[0];o=K.convert(F.to_sympy(F.unit))
dims,mat,pivots,free=analyze(K,k,o)
assert dims==[20,35] and mat.shape==(41,8)
pivot_factors=set()
for value in pivots:
 for poly in [value.numer,value.denom]:
  for f,e in s.Poly(poly.as_expr(),kap,domain=F).factor_list()[1]:
   f=f.monic();assert f.as_expr() in [kap,kap+1];pivot_factors.add(str(f.as_expr()))
assert pivot_factors=={'kappa','kappa + 1'}
D=K.field.ring.one
for row in mat.to_list():
 for c in row:D=D.lcm(c.denom)
assert s.Poly(D.as_expr(),kap,domain=F).monic().as_expr()==kap
cleared=(mat.to_Matrix()*D.as_expr()).applyfunc(s.cancel)
smith=smith_normal_form(cleared,domain=F.poly_ring(kap));invariants=[]
for j in range(8):
 f=s.Poly(smith[j,j],kap,domain=F).monic()
 assert f.as_expr()==(1 if j<6 else kap);invariants.append(str(f.as_expr()))
for j in range(smith.rows):
 for l in range(smith.cols):
  if j!=l:assert smith[j,l]==0
exceptions=[]
for value in [0,-1]:
 dim,m,_,basis=analyze(F,F.convert(value),F.unit)
 assert dim==([20,35] if value==0 else [22,46])
 if value==0:assert m.shape[1]==8 and m.rank()==8
 exceptions.append({'kappa':value,'B3_B4_dimensions':dim,'normal_rank':m.rank(),
                     'exclusion':'W1 zero' if value==0 else 'B3 dimension22 !=20'})
out={'status':'PASS','scope':'original22-orbit block identities, exact all-parameter normal matrix and every relation-pivot factor, Smith invariants, fresh exceptional fibers; ordinary coverage and charge proofs separate',
 'field':'QQ(omega), omega^2+omega+1=0','normalized_family_relations':['x^2+y^2','bx-omega*xb','cy-omega^2*yc','b^2-omega^2*xc-cx','c^2+yb+omega^2*by','bc-omega^2*cb-kappa*(xy-yx)'],
 'generic_B3_B4_dimensions':dims,'all_relation_pivot_factors':sorted(pivot_factors),
 'invariant_cubic_basis':free,'normal_matrix_shape':list(mat.shape),'normal_common_denominator':'kappa',
 'cleared_normal_Smith_monic_factors':invariants,'fresh_exceptions':exceptions,
 'excluded_unit_repeat_strata':['P=Q=0','P,Q independent and S=T=0'],
 'not_claimed':['rank1 P,Q strata excluded','independent P,Q with nonzero pure bc quartic block excluded','all semisimple third-root spectra classified','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_closed_strata_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','one_parameter_family_all_kappa_excluded':True,'exceptions':[0,-1]}))
