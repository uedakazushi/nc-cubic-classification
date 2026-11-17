#!/usr/bin/env python3
"""Exact L-curve normal-cubic incidence, polynomial in u,v on a certified
function-field open; AS4 existence and H3 admissibility not asserted.
"""
from pathlib import Path
import sympy as s,itertools,json
from cubic_function_extension import CubicField
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));D,E=s.symbols('D E');J=F.frac_field(E);ee=J.gens[0];oo=J.convert(F.to_sympy(F.unit));K=CubicField(J,-oo*ee**3-oo**2);d=K.generator;e=K.convert(E);o=K.convert(F.to_sympy(F.unit));one,zero=K.one,K.zero
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
 print('dim',n,3**n-len(Ps[n]),flush=True)
free=[w for j,w in enumerate(Ws[3]) if j not in Ps[3] and sum([0,1,2][t] for t in w)%3==0]
print('free',free,flush=True)
cols=[]
for w in free:
 col={}
 for j,phase in enumerate([one,o**2,o]):
  row={Is[4][w+(j,)]:one};k=Is[4][(j,)+w];row[k]=row.get(k,zero)-phase
  for k,c in reduce(row,Ps[4]).items():col[j*81+k]=c
 cols.append(col)
keys=sorted(set().union(*(set(c) for c in cols)));rows=[{j:c[k] for j,c in enumerate(cols) if k in c} for k in keys]
log=[];piv=echelon(rows);print('L curve normal rank',len(piv),flush=True)
if len(piv)<4:print('kernel dimension',4-len(piv),flush=True)

# Recover normalized Gamma in the four quotient cubic classes.
coeff={3:one}
for j in sorted(piv,reverse=True):coeff[j]=-sum((c*coeff.get(k,zero) for k,c in piv[j].items() if k!=j),zero)
Gamma={tuple(t+1 for t in w):coeff[i] for i,w in enumerate(free)}
assert coeff[3]==one


from cubic_parameter_polynomials import ParameterRing
base=K;P=ParameterRing(base);d=P.convert(d);e=P.convert(e);o=P.convert(o);one,zero=P.one,P.zero;u,v=P.u,P.v
R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
 {(1,2):d,(2,1):e,(3,3):one},
 {(1,3):e,(3,1):d,(2,2):one},
 {(2,3):d,(3,2):e,(0,0):u,(0,1):v,(1,1):one}]
words=sorted(itertools.product(range(4),repeat=4),key=lambda w:(w.count(0),w));ix={w:j for j,w in enumerate(words)}
rows=[]
for rel in R:
 for left in range(3):
  for pre in itertools.product(range(4),repeat=left):
   for post in itertools.product(range(4),repeat=2-left):rows.append({ix[pre+w+post]:c for w,c in rel.items()})
log=[];QP=echelon(rows);assert 256-len(QP)==35
B4_basis=[words[j] for j in range(256) if j not in QP]
def residual(G):
 out={}
 for j,phase in enumerate([one,one,o**2,o]):
  row={}
  for w,c in G.items():
   for ww,cc in [(w+(j,),c),((j,)+w,-phase*c)]:row[ix[ww]]=row.get(ix[ww],zero)+cc
  for k,c in reduce(row,QP).items():out[j,k]=c
 return out
Gamma={w:P.convert(c) for w,c in Gamma.items()}
Gs=[{(1,1,0):one},{(2,3,0):one},{(1,0,0):one},{(0,0,0):one},Gamma]
cols=[residual(g) for g in Gs];keys=sorted(set().union(*(set(c) for c in cols)))
rows=[{j:c[k] for j,c in enumerate(cols) if k in c} for k in keys]
NP={};obstructions=[]
for row in rows:
 rr=reduce({j:c for j,c in row.items() if c},NP)
 if not rr:continue
 j=min(rr)
 if j<4:
  co=rr[j];NP[j]={k:c/co for k,c in rr.items()};continue
 assert set(rr)=={4};obstructions.append(rr[4])
print('correction pivots',list(NP),'nonzero obstruction count',len(obstructions),flush=True)
print('obstruction monomial supports',[list(c.d) for c in obstructions],flush=True)
if not obstructions:
 cc={4:one}
 for j in sorted(NP,reverse=True):cc[j]=-sum((c*cc.get(k,zero) for k,c in NP[j].items() if k!=j),zero)
 print('lift correction monomial supports',[list(cc[j].d) for j in range(4)],flush=True)

assert set(NP)=={0,1,2,3} and not obstructions
for key in keys:
 assert not sum((cols[j].get(key,zero)*cc[j] for j in range(5)),zero)
# Degree3 flatness/character, with exactly the same polynomial-constant pivot rule.
ws3=sorted(itertools.product(range(4),repeat=3),key=lambda w:(w.count(0),w));is3={w:j for j,w in enumerate(ws3)};rows3=[]
for rel in R:
 for left in range(2):
  for pre in itertools.product(range(4),repeat=left):
   for post in itertools.product(range(4),repeat=1-left):rows3.append({is3[pre+w+post]:c for w,c in rel.items()})
q3=echelon(rows3);assert 64-len(q3)==20
assert sum(1 for j,w in enumerate(ws3) if j not in q3 and sum([0,0,1,2][t] for t in w)%3==0)==8
# Closed formulas, independently compared with the recovered kernel.
be=base.convert(E);bd=base.generator;bo=base.convert(F.to_sympy(F.unit));Y=be**3
Acoef=(-(bo+2)*Y**2-2*bo*Y-(bo+1)*be**2*bd-bo*be*bd**2+1)/(Y-1)
Bcoef=bd/(Y-1)
Ccoef=(-(bo+2)*Y**2+(1-bo)*Y-bo*be**2*bd-(bo+1)*be*bd**2)/(Y-1)
Kcoef=((bo+1)*Y+bo*be**2*bd+bo*be*bd**2-1)/(Y-1)**2
assert coeff[0]==bo and coeff[1]==-bd*((bo+2)*Y+bo**2)
assert coeff[2]==be*(2-(bo+2)*Y) and coeff[3]==base.one
assert cc[0]==P.convert(Acoef)*v and cc[1]==P.convert(Bcoef)*v
assert cc[2]==P.convert(Ccoef)*u+P.convert(Kcoef)*v**2
assert cc[3]==P.convert(Kcoef)*u*v
# The full Z parameter is removed by y_new=y+omega*Z/(d+omega*E)*x.
gauge_denom=bd+bo*be;gauge_denom.inverse()
# An explicit univariate open supporting every selected inverse and pivot.
Omega=base.J.field.ring.one
for norm in base.norm_log:
 Omega=Omega.lcm(norm.numer).lcm(norm.denom)
Omega_poly=s.Poly(Omega.as_expr(),E,domain=F).sqf_part().monic()
Omega=base.J.field.ring.from_expr(Omega_poly.as_expr())
# Record rational expressions in E and d, omega symbolic for readable input.
Om=s.Symbol('omega');ds=s.Symbol('d');os=F.to_sympy(F.unit)
def scalar_expr(c):
 den=base.J.field.ring.one
 for val in c.a:den=den.lcm(val.denom)
 den=den.monic()
 num=sum(((val.numer*den.exquo(val.denom)).as_expr().xreplace({os:Om})*ds**j for j,val in enumerate(c.a)),s.S.Zero)
 return num/den.as_expr().xreplace({os:Om})
def poly_record(c):return {str(mon):str(scalar_expr(val)) for mon,val in c.d.items()}
out={'status':'PASS','scope':'exact cubic function field plus complete polynomial u,v original B3/B4 and normal equations; extends only to recorded Omega-open of L',
 'base_curve':'d^3+omega*E^3+omega^2=0, omega^2+omega+1=0',
 'field_irreducibility_reason':'-omega*E^3-omega^2 has simple zeros, hence not a cube in QQ(omega)(E)',
 'Z_gauge':'t=omega*Z/(d+omega*E), y_new=y+t*x, u_new=u-v*t+t^2, v_new=v-2*t, Z_new=0',
 'B_relations':'xy=yx; xb=omega^2*bx; xc=omega*cx; d*yb+E*by+c^2=0; E*yc+d*cy+b^2=0; d*bc+E*cb+u*x^2+v*xy+y^2=0',
 'S3_S4_dimensions':[10,15],'S_inverse_Nakayama_normal_rank':3,
 'B3_B4_dimensions':[20,35],'B3_fixed_character_dimension':8,
 'all_u_v_parameter_pivots_constant':True,'normal_correction_rank':4,
 'normal_kernel_dimension':1,
 'Gamma_in_bbb_bcy_cby_ccc':[str(scalar_expr(coeff[j])) for j in range(4)],
 'lift_correction_basis':['y^2*x','b*c*x','y*x^2','x^3'],
 'lift_corrections':[poly_record(cc[j]) for j in range(4)],
 'Omega_E_monic':str(Omega.as_expr().xreplace({os:Om})),
 'selected_inverse_count':len(base.norm_log),
 'Omega_factor_list':[str(f.monic().as_expr().xreplace({os:Om})) for f,ex in Omega_poly.factor_list()[1]],
 'not_claimed':['all closed points of L covered','AS4 existence proved just from degrees3/4','normal quotient domain or H3 admissible','all other Delta-zero curves covered','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_boundary_L_incidence_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','L_open_normal_kernel_dimension':1,'all_polynomial_u_v':True,'Omega_degree':Omega.degree()}))
