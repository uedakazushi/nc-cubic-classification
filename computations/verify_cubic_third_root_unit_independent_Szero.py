#!/usr/bin/env python3
"""Exact whole-plane pivot cover, four boundary curves and exceptional fibers.
A=1 and A=D=0 charts are literal original quadratic presentations; no samples
are substituted for a parameter-open proof.
"""
import itertools,json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z**2+z+1));O=s.Symbol('omega')
A,D,E,T=s.symbols('A D E T',nonzero=True);a0,a1,a4,a5=s.symbols('a0 a1 a4 a5')
def red(e):return s.rem(s.expand(e),O**2+O+1,O)
P=s.Matrix([[A,-O**2*A],[0,O**2*E],[-E,0],[D,-O**2*D]])
C=s.diag(T,-O*T)
U=s.Matrix([[0,a0,-a0,a1],[a0,a4,-a1,a5],[-a0,-a1,-a4,-a5],[a1,a5,-a5,0]])
R=U-P*C.inv()*P.T
sol={a1:0,a0:A*E/T,a4:-E**2/T,a5:D*E/T}
assert R.subs(sol).applyfunc(red)==s.zeros(4)
L,b=s.linear_eq_to_matrix(list(R),[a0,a1,a4,a5]);assert L.rank()==4
# Exact scalar-normalization invariants with v=1,u=t,r=1/(T*t),s=t^2/T.
t=s.Symbol('t',nonzero=True);rr=1/(T*t);ss=t*t/T
Ap=A*t*t/rr;Dp=D/(ss*t);Ep=E*t*t/ss;Tp=T*t*rr
assert s.cancel(Tp-1)==0 and s.cancel(Ep-E*T)==0
assert s.cancel(Ap*Dp-A*D*T*T)==0

def analyze(K,parameters,A,D,E,normal=True):
 one=K.one;zero=K.zero;o=K.convert(F.to_sympy(F.unit));relation_log=[]
 def echelon(rows,log):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     c=row[j];log.append(c);piv[j]={v:d/c for v,d in row.items()};break
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
 def factors(log):
  out=set()
  if not parameters:return []
  for value in log:
   for p in [value.numer,value.denom]:
    for f,e in s.Poly(p.as_expr(),*parameters,domain=F).factor_list()[1]:out.add(str(f.monic().as_expr()))
  return sorted(out)
 rel=[{(2,0):one,(0,2):-o},{(3,1):one,(1,3):-o**2},
      {(2,2):one,(0,3):-A*o**2,(3,0):-A,(3,1):E},
      {(3,3):one,(0,2):-E,(1,2):D,(2,1):o**2*D},
      {(2,3):one,(0,0):A,(1,0):-E,(1,1):D},
      {(3,2):one,(0,0):o*A,(0,1):-o*E,(1,1):o*D}]
 WS={n:list(itertools.product(range(4),repeat=n)) for n in [3,4]};IS={n:{w:j for j,w in enumerate(WS[n])} for n in [3,4]};Ps={}
 for n in [3,4]:
  rows=[]
  for r in rel:
   for l in range(n-1):
    for pre in itertools.product(range(4),repeat=l):
     for post in itertools.product(range(4),repeat=n-l-2):rows.append({IS[n][pre+w+post]:c for w,c in r.items() if c})
  Ps[n]=echelon(rows,relation_log)
 dims=[4**n-len(Ps[n]) for n in [3,4]]
 out={'B3_B4_dimensions':dims,'relation_pivot_factors':factors(relation_log)}
 if not normal:return out
 free=[w for j,w in enumerate(WS[3]) if j not in Ps[3] and sum([0,0,1,2][j] for j in w)%3==0]
 cols=[];inv=[one,one,o**2,o]
 for w in free:
  result={}
  for j in range(4):
   row={IS[4][w+(j,)]:one};k=IS[4][(j,)+w];row[k]=row.get(k,zero)-inv[j]
   for k,c in reduce(row,Ps[4]).items():result[j*256+k]=c
  cols.append(result)
 keys=sorted(set().union(*(set(c) for c in cols)))
 rows=[{j:c[k] for j,c in enumerate(cols) if k in c} for k in keys]
 log=[];pivot=echelon(rows,log)
 assert len(free)==8 and len(pivot)==8
 out.update({'normal_rank':8,'normal_pivot_factors':factors(log),'normal_matrix_shape':[len(rows),8]})
 return out

d,e=s.symbols('d e');K=F.frac_field(d,e);dd,ee=K.gens
plane=analyze(K,[d,e],K.one,dd,ee)
assert plane['B3_B4_dimensions']==[20,35]
assert set(plane['relation_pivot_factors'])=={'d','e','d - e','d - e**2'}
assert set(plane['normal_pivot_factors'])=={'d','e','d - e**2'}
q=s.Symbol('t');L=F.frac_field(q);u=L.gens[0];curves={}
for name,Dv,Ev,expected_rel,expected_normal in [
 ('d=0',L.zero,u,{'t'},{'t'}),('e=0',u,L.zero,{'t'},{'t'}),
 ('d=e^2',u*u,u,{'t','t - 1'},{'t'})]:
 result=analyze(L,[q],L.one,Dv,Ev)
 assert result['B3_B4_dimensions']==[20,35]
 assert set(result['relation_pivot_factors'])==expected_rel and set(result['normal_pivot_factors'])==expected_normal
 curves[name]=result
bad=analyze(L,[q],L.one,u,u,normal=False)
assert bad['B3_B4_dimensions']==[22,46]
bad['all_fiber_conclusion']='B3 dimension >=22 by polynomial generic-rank upper bound; includes t=0,1'
curves['d=e']=bad
zeroAD=analyze(L,[q],L.zero,L.zero,u)
assert zeroAD['B3_B4_dimensions']==[20,35]
assert set(zeroAD['relation_pivot_factors'])=={'t','t - 1','t + 1'}
assert set(zeroAD['normal_pivot_factors'])=={'t'}
exceptions=[]
for value in [0,1,-1]:
 result=analyze(F,[],F.zero,F.zero,F.convert(value),normal=False)
 assert result['B3_B4_dimensions']==([26,68] if value==0 else [20,37])
 exceptions.append({'lambda':value,**result,'exclusion':'not AS4 Hilbert series'})
out={'status':'PASS','scope':'original Schur atlas and scalar normalization, exact plane and curve presentations, every relation/normal pivot factor, polynomial-rank whole-curve exclusion and fresh exceptions',
 'field':'QQ(omega), omega^2+omega+1=0','normalized_plane_parameters':['d=ADT^2','e=ET'],
 'plane_open':plane,'boundary_curves':curves,'A=D=0_open':zeroAD,'A=D=0_exceptions':exceptions,
 'conclusion':'unit-repeat independent P,Q and S=0 has no H3 candidate for any T',
 'remaining_unit_repeat_sectors':['rank(P,Q)=1','rank(P,Q)=2 and S!=0'],
 'not_claimed':['remaining unit-repeat sectors excluded','nonunit semisimple spectrum classified','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_independent_Szero_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','plane_boundary_curves':4,'additional_fresh_exceptions':[0,1,-1]}))
