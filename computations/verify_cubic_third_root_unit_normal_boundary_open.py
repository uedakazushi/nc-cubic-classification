#!/usr/bin/env python3
"""Exact dense-open normal-linear boundary obstruction, with original relation
pivots and a zero-dimensional residual ideal; exceptional curves remain open.
"""
from pathlib import Path
import sympy as s,itertools,json
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));D,E=s.symbols('D E');K=F.frac_field(D,E);d,e=K.gens;o=K.convert(F.to_sympy(F.unit));one,zero=K.one,K.zero
# y,b,c with w=1
R=[{(0,1):d,(1,0):e,(2,2):one},{(0,2):e,(2,0):d,(1,1):one},{(1,2):d,(2,1):e,(0,0):one}]
log=[]
def echelon(rows):
 piv={}
 for row in rows:
  row={j:c for j,c in row.items() if c}
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
Ws={n:list(itertools.product(range(3),repeat=n)) for n in [3,4]};Is={n:{w:j for j,w in enumerate(Ws[n])} for n in [3,4]};Ps={}
for n in [3,4]:
 rows=[]
 for rel in R:
  for left in range(n-1):
   for pre in itertools.product(range(3),repeat=left):
    for post in itertools.product(range(3),repeat=n-left-2):rows.append({Is[n][pre+w+post]:c for w,c in rel.items()})
 Ps[n]=echelon(rows)
 assert 3**n-len(Ps[n])=={3:10,4:15}[n]
relation_log=list(log)
free=[w for j,w in enumerate(Ws[3]) if j not in Ps[3] and sum([0,1,2][t] for t in w)%3==0]
assert len(free)==4
cols=[]
for w in free:
 col={}
 for j,phase in enumerate([one,o**2,o]):
  row={Is[4][w+(j,)]:one};k=Is[4][(j,)+w];row[k]=row.get(k,zero)-phase
  for k,c in reduce(row,Ps[4]).items():col[j*81+k]=c
 cols.append(col)
keys=sorted(set().union(*(set(c) for c in cols)));rows=[{j:c[k] for j,c in enumerate(cols) if k in c} for k in keys]
piv={};last=[];normal_log=[]
for row in rows:
 rr=reduce(row,piv)
 if not rr:continue
 j=min(rr)
 if len(piv)<3:
  co=rr[j];normal_log.append(co);piv[j]={k:v/co for k,v in rr.items()};continue
 assert set(rr)=={3};last.append(rr[3])
assert list(piv)==[0,1,2] and len(last)==9
os=F.to_sympy(F.unit)
curves=[D,E,D**3-E**3,E**3-1,D**3+os*E**3,D**3+os**2*E**3,
 D**2*E+D+E**2,D**2*E+os**2*D+os*E**2,D**2*E+os*D+os**2*E**2,
 D**3+os*E**3+os**2]
assert all(F.convert(c.subs({D:2,E:3})) for c in curves)
Delta=s.prod(curves);delta=K.field.ring.from_expr(Delta)
def supported(poly):
 while any(sum(mm)>0 for mm in poly.monoms()):
  g=poly.gcd(delta)
  assert any(sum(mm)>0 for mm in g.monoms()),str(poly)
  poly=poly.exquo(g)
for c in relation_log+normal_log+last:
 supported(c.denom)
for c in relation_log+normal_log:supported(c.numer)
polys=[c.numer.as_expr() for c in last]
GB=s.groebner(polys,D,E,domain=F)
P=E*(E**3-1)*(D**3+os*E**3+os**2)
assert GB.reduce(s.expand(P**3))[1]==0
out={'status':'PASS','scope':'original three relations degree3/4 row modules, complete pivot support, three normal pivots and residual-ideal open cover',
 'w_normalization':1,'original_S3_S4_dimensions':[10,15],
 'relation_pivot_count':len(relation_log),'first_normal_pivot_count':3,'last_residual_count':9,
 'dense_open_Delta_factor_list':[str(p) for p in curves],
 'normal_coefficient_basis':['bbb','bcy','cby','ccc'],
 'residual_Groebner_basis':[str(p.as_expr()) for p in GB.polys],
 'open_cover_identity':'(E*(E^3-1)*(D^3+omega*E^3+omega^2))^3 in ideal(all nine residual numerators)',
 'normal_rank_on_Delta_nonzero':4,
 'not_claimed':['all exceptional Delta-zero curves excluded','w0 boundary covered','all proportional couplings classified','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_normal_boundary_open_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','dense_open_normal_boundary_excluded':True,'normal_rank':4}))
