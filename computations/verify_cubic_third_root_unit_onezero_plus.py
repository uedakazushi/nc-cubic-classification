#!/usr/bin/env python3
"""All-value exclusion of the T,s nonzero, lambda=omega one-zero chart.
Exact generic seven-surface support, seven rational curves and fresh points.
No finite-field sampling and no full atlas claim.
"""
from pathlib import Path
import json,sympy as s
from cubic_third_root_onezero_plus import F,compute
# Independent Schur identities used to reduce the full rank-one chart.
O,lam,ss,aa,rr,hh,kk=s.symbols('O lambda s A r h k')
R=s.Matrix([aa,lam*rr,-lam*(hh+kk*ss),lam**2*(O+1)*ss])
S=s.Matrix([(O+1)*aa+kk*(rr-hh),rr+kk*ss,-hh,ss])
HH=R*R.T-O**2*S*S.T
def red(e):return s.rem(s.expand(e),O**2+O+1,O)
assert red(HH[3,3]-O*ss**2*(lam**4-O))==0
assert red((HH[1,3]+HH[2,3]).subs(lam,O)-2*ss*(O+1)*(rr-hh))==0
K=F.frac_field('A','r','k');a,r,k=K.gens;o=K.convert(F.unit,F);one=K.one
out={'status':'PASS','field':'omega^2+omega+1','chart':'P1,Q0,S0,T=s1,lambda=omega,h=r'}
res=compute(K,a,r,k)
factors=[a,r,k+r,k+2*r,(o+one)*a+k*r+r*r,-(o+one)*a+k*k+3*k*r+3*r*r,a+o*r*r]
support=one
for f in factors:support*=f
support=support.numer
def supported(poly):
 while any(sum(mm)>0 for mm in poly.monoms()):
  gg=poly.gcd(support);assert any(sum(mm)>0 for mm in gg.monoms()),str(poly);poly=poly.exquo(gg)
for c in res['source_pivots']+res['normal_pivots']+[res['source_minor']]:supported(c.numer);supported(c.denom)
for rr in res['relations']:
 for c in rr.values():supported(c.denom)
assert all(c.numer.is_ground and c.denom.is_ground for c in res['normal_pivots'])
out['generic']={'normal_shape':res['normal_shape'],'constant_normal_pivots':[str(K.to_sympy(c)) for c in res['normal_pivots']],'source_rows':res['source_rows'],'source_columns':res['source_columns'],'support_factors':[str(K.to_sympy(c)) for c in factors]}
print('PASS generic seven-surface support',flush=True)
curves=[];fresh=[];seen=set()
for case in ['A0','kminus1','kminus2','J0','H0','r0','L0']:
 L=F.frac_field('t');t=L.gens[0];oo=L.convert(F.unit,F);u,zz=L.one,L.zero
 params={'A0':(zz,u,t),'kminus1':(t,u,-u),'kminus2':(t,u,-2*u),'J0':(-(t+u)/(oo+u),u,t),'H0':((t*t+3*t+3*u)/(oo+u),u,t),'r0':(t,zz,u),'L0':(-oo,u,t)}[case]
 cr=compute(L,*params);bad=L.field.ring.one
 for cc in cr['source_pivots']+cr['normal_pivots']+[cr['source_minor']]:bad=bad.lcm(cc.numer).lcm(cc.denom)
 for rr in cr['relations']:
  for cc in rr.values():bad=bad.lcm(cc.denom)
 bad=bad.sqf_part().monic();curves.append({'case':case,'bad_polynomial':str(bad.as_expr()),'normal_shape':cr['normal_shape'],'normal_pivots':8})
 # Every exceptional root is in the original quadratic coefficient field.
 poly=s.Poly(bad.as_expr(),s.Symbol('t'),domain=F)
 for f,m in poly.factor_list()[1]:
  assert f.degree()==1
  cs=f.rep.to_list();tt=-cs[1]/cs[0];oo=F.unit;u,zz=F.one,F.zero
  pars={'A0':(zz,u,tt),'kminus1':(tt,u,-u),'kminus2':(tt,u,-2*u),'J0':(-(tt+u)/(oo+u),u,tt),'H0':((tt*tt+3*tt+3*u)/(oo+u),u,tt),'r0':(tt,zz,u),'L0':(-oo,u,tt)}[case]
  key=tuple(str(F.to_sympy(c)) for c in pars)
  if key not in seen:seen.add(key);fresh.append((case,pars))
 print('PASS curve',case,'bad',bad.as_expr(),flush=True)
fresh += [('r0k0A1',(F.one,F.zero,F.zero)),('origin',(F.zero,F.zero,F.zero))]
records=[]
for name,pars in fresh:
 rr=compute(F,*pars,finite=True)
 records.append({'case':name,'parameters':[list(map(str,c.to_list())) for c in pars],'dimensions':rr['dimensions'],'excluded':'nonAS4 Hilbert' if rr.get('nonAS4') else 'normal kernel zero'})
out.update({'curves':curves,'fresh_points':records,'fresh_count':len(records),'scope':'all normalized plus-chart parameters by weighted scalar action (A,r,k) weights(2,1,1), explicit7 surface cover and fresh points','not_claimed':['lambda=-omega or primitive4 types','s0 stratum','whole onezero atlas','complete H3 classification']})
Path(__file__).with_name('cubic_third_root_unit_onezero_plus_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS whole plus chart; fresh points',len(records),flush=True)
