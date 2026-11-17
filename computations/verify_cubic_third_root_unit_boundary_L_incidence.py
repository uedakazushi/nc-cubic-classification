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
# The regular AS4 recognition uses the actual W3 lift, not degree counts alone.
ws2=sorted(itertools.product(range(4),repeat=2),key=lambda w:(w.count(0),w));is2={w:j for j,w in enumerate(ws2)}
rows2=[{is2[w]:c for w,c in rel.items()} for rel in R]
q2=echelon(rows2);assert len(q2)==6
assert len(echelon(rows2+[{is2[(j,0)]:one} for j in range(4)]))==10

def tensor_sum(parts):
 out={}
 for scalar,pre,rel,post in parts:
  for w,c in rel.items():
   key=pre+w+post;out[key]=out.get(key,zero)+scalar*c
 return {w:c for w,c in out.items() if c}
w3left=tensor_sum([(one,(1,),R[5],()),(one,(2,),R[4],()),
                  (one,(3,),R[3],()),(u,(0,),R[0],())])
w3right=tensor_sum([(one,(),R[5],(1,)),(one,(),R[4],(2,)),
                   (one,(),R[3],(3,)),(-u,(),R[0],(0,)),(-v,(),R[0],(1,))])
assert w3left==w3right and w3left[(2,2,2)]==one
# Full original quartic top and its inverse-Nakayama cyclic convention.
seen=set();tops=[];weights=[0,0,1,2]
for word in itertools.product(range(4),repeat=4):
 if word in seen:continue
 ww=word;co=F.one;top={}
 while ww not in top:
  top[ww]=co;seen.add(ww);ww=(ww[-1],)+ww[:-1];co=-co/F.unit**weights[ww[0]]
 if co==F.one:tops.append(top)
aa=[zero]*22
for i,c in {0:u,4:v,5:one,6:d,7:e,9:e,10:one,11:d,12:d,13:e,14:one}.items():aa[i]=c
w4={}
for a,top in zip(aa,tops):
 for ww,c in top.items():w4[ww]=w4.get(ww,zero)+a*P.convert(base.convert(F.to_sympy(c)))
w4={w:c for w,c in w4.items() if c}
assert w4[(0,2,2,2)]==one
for ww,c in w4.items():
 vv=(ww[-1],)+ww[:-1]
 assert w4[vv]==-c/(o**weights[vv[0]])
for j in range(16):
 col={is2[w[:2]]:c for w,c in w4.items() if 4*w[2]+w[3]==j}
 assert not reduce(col,q2)
# Central cubic obtained from Gamma and the polynomial algebra k[x,y].
Glift=dict(Gamma)
for j,ww in enumerate([(1,1,0),(2,3,0),(1,0,0),(0,0,0)]):Glift[ww]=Glift.get(ww,zero)+cc[j]
def central_residual(G):
 result={}
 for j in range(4):
  row={}
  for ww,c in G.items():
   for vv,co in [(ww+(j,),c),((j,)+ww,-c)]:row[ix[vv]]=row.get(ix[vv],zero)+co
  for k,c in reduce({k:c for k,c in row.items() if c},QP).items():result[j,k]=c
 return result
Cgs=[{(1,1,1):one},{(1,1,0):one},{(1,0,0):one},Glift]
Ccols=[central_residual(g) for g in Cgs];cks=sorted(set().union(*(set(c) for c in Ccols)))
CP={};center_obstructions=[]
for key in cks:
 row={j:c[key] for j,c in enumerate(Ccols) if key in c and c[key]}
 rr=reduce(row,CP)
 if not rr:continue
 j=min(rr)
 if j<3:
  co=rr[j];CP[j]={k:c/co for k,c in rr.items()};continue
 center_obstructions.append(rr)
assert set(CP)=={0,1,2} and not center_obstructions
cs={3:one}
for j in sorted(CP,reverse=True):cs[j]=-sum((c*cs.get(k,zero) for k,c in CP[j].items() if k!=j),zero)
for key in cks:assert not sum((Ccols[j].get(key,zero)*cs[j] for j in range(4)),zero)
# Every additional inverse remains supported on the same Omega-open.
def supported_by_Omega(poly):
 while poly.degree()>0:
  gg=poly.gcd(Omega);assert gg.degree()>0
  poly=poly.exquo(gg)
for nn in base.norm_log:
 supported_by_Omega(nn.numer);supported_by_Omega(nn.denom)
assert set(cs[0].d)=={(0,0)} and set(cs[1].d)<={(0,1)} and set(cs[2].d)<={(1,0),(0,2)}
recognition={'status':'PASS','scope':'all-polynomial-u-v 1-regular normal x, explicit W3 lift and quartic Nakayama tensor; ordinary LBS AS4 recognition; central cubic relation exact',
 'same_L_and_Omega_open':True,'B2_relation_rank':6,'B2_relations_plus_xB1_rank':10,
 'W3_lift_left':'y*r_even+b*r_b+c*r_c+u*x*r_xy',
 'W3_lift_right':'r_even*y+r_b*b+r_c*c-u*r_xy*x-v*r_xy*y',
 'W3_projection_nonzero':'coefficient of b^3 equals1',
 'top_inverse_Nakayama':'(x,y,omega*b,omega^2*c)',
 'ordinary_AS4_inputs':{'Sklyanin_Koszul_CY':'Iyudu-Shkarin arXiv1601.00564 Theorem1.1, Corollary6.1; E nonzero, E^3!=1',
 'normal_extension':'Le Bruyn-Smith-Van den Bergh MathZ222(1996)171-212, Theorem2.6(5), Corollary2.7; 1-regularity and W3 surjectivity checked'},
 'conclusion':'every u,v in the recorded open is an actual noetherian quadratic Koszul AS4 domain with prescribed Nakayama',
 'central_cubic':'Psi=Gamma_tilde+q0*y^3+q1*y^2*x+q2*y*x^2',
 'central_correction_coefficients':[poly_record(cs[j]) for j in range(3)],
 'not_claimed':['full center or PI degree','normal quotient domain or H3 admissibility','all closed L points covered','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_boundary_L_recognition_certificate.json').write_text(json.dumps(recognition,indent=2)+'\n')
print(json.dumps({'status':'PASS','actual_AS4_recognition_inputs':True,'central_Psi_identity':True}))
