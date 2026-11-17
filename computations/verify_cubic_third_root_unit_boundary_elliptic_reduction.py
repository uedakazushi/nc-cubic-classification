#!/usr/bin/env python3
"""Exact potential/untwist identities and finite singular-boundary cover.
The proper-elliptic H3 obstruction uses ordinary EG/Rains/trace proofs.
This program checks only the displayed algebraic identities and finite cover.
"""
from pathlib import Path
import json,sympy as s
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));P=F.poly_ring('D','E','Z','u','v');D,E,Z,u,v=P.gens;o=P.convert(F.unit,F);one=P.one;zero=P.zero
phi={(0,1,2):D*o,(0,2,1):E*o**2,(0,0,0):one/3,(1,1,1):one/3,(2,2,2):one/3,(0,):u,(0,0):v/2,(1,2):o**2*Z}
def derivative(letter):
 out={}
 for word,co in phi.items():
  for i,j in enumerate(word):
   if j==letter:
    ww=word[i+1:]+word[:i];out[ww]=out.get(ww,zero)+co
 return {w:c for w,c in out.items() if c}
# Original B quadratic relations in x,y,b,c, before right Zhang untwist.
R=[{(1,2):D,(2,1):E,(3,3):one,(0,2):o*Z},
   {(1,3):E,(3,1):D,(2,2):one,(0,3):Z},
   {(2,3):D,(3,2):E,(0,0):u,(0,1):v,(1,1):one}]
weights=[0,0,1,2]
RC=[{w:c/o**weights[w[1]] for w,c in rr.items()} for rr in R]
def affine(rr):
 out={}
 for w,c in rr.items():
  ww=tuple(j-1 for j in w if j);out[ww]=out.get(ww,zero)+c
 return out
gradients=[affine(RC[2]),{w:o*c for w,c in affine(RC[1]).items()},{w:o**2*c for w,c in affine(RC[0]).items()}]
for j in range(3):
 der=derivative(j);rr=gradients[j]
 assert all(not(der.get(w,zero)-rr.get(w,zero)) for w in set(der)|set(rr))
# Smooth point-curve criterion and the complete nine-line factorization.
ell=(D**3+E**3+one)**3-27*D**3*E**3
lines=[(a,b,D+o**a*E+o**b) for a in range(3) for b in range(3)]
prod=one
for _,_,line in lines:prod*=line
assert not(prod-ell)
# Restrict the previously proved necessary Delta locus to the nine lines.
Q=F.poly_ring('q');q=Q.gens[0];oo=Q.convert(F.unit,F)
line_data=[];hs=[];lcm=Q.one
for a,b,_ in lines:
 d=-oo**a*q-oo**b;e=q
 C=[d*d*e+oo**((-j)%3)*d+oo**j*e*e for j in range(3)]
 L=d**3+oo*e**3+oo**2
 factors=[d,e,d**3-e**3,e**3-1,d**3+oo*e**3,d**3+oo**2*e**3,*C,L]
 assert all(factors)
 raw=Q.one
 for factor in factors:raw*=factor
 radical=raw.exquo(raw.gcd(raw.diff(q))).monic()
 axes=radical.gcd(d*e)
 h=radical.exquo(axes).monic()
 # PHS necessity excludes D^3=E^3=1 (Iyudu--Shkarin Theorem1.1).
 bad=h.gcd(e**3-1).gcd(d**3-1)
 h=h.exquo(bad).monic()
 hs.append(h);lcm=(lcm*h).exquo(lcm.gcd(h)).monic()
 def encode(f):return [list(map(str,f.get((i,),F.zero).to_list())) for i in range(f.degree()+1)]
 fc=h.factor_list()
 line_data.append({'a':a,'b':b,'D':'-omega^a*E-omega^b','remaining_E_polynomial_low_to_high':encode(h),'degree':h.degree(),'factors':[{'degree':ff.degree(),'coefficients_low_to_high':encode(ff),'multiplicity':m} for ff,m in fc[1]]})
# All nine line polynomials have a single normalized degree11 parameter.
h0=hs[0]
for (a,b,_),h in zip(lines,hs):
 scale=oo**((a-b)%3);composed=Q.zero
 for i in range(h0.degree()+1):composed+=Q.convert(h0.get((i,),F.zero),F)*(scale*q)**i
 assert composed.monic()==h
assert h0.evaluate(0,F.zero) and h0.evaluate(0,-F.one)
# All overlaps between distinct nonparallel lines lie in QQ(omega).
multi={}
for i,(a,b,_) in enumerate(lines):
 aa=F.unit**a;bb=F.unit**b
 for j,(c,d,_) in enumerate(lines[:i]):
  cc=F.unit**c;dd=F.unit**d
  if not(aa-cc):continue
  e=(dd-bb)/(aa-cc);dv=-aa*e-bb
  if not e or not dv:continue
  if hs[i].evaluate(0,e) or hs[j].evaluate(0,e):continue
  key=(tuple(map(str,dv.to_list())),tuple(map(str,e.to_list())))
  multi.setdefault(key,set()).update([i,j])
for (ds,es),indices in multi.items():
 def decode(cs):
  out=F.zero
  for c in cs:out=out*F.unit+F.convert(s.Rational(c))
  return out
 dv,e=decode(ds),decode(es)
 actual={i for i,(a,b,_) in enumerate(lines) if not(dv+F.unit**a*e+F.unit**b) and not hs[i].evaluate(0,e)}
 assert actual==indices and len(indices)>=2
count=sum(h.degree() for h in hs)-sum(len(indices)-1 for indices in multi.values())
out={'status':'PASS','omega_relation':'omega^2+omega+1=0','potential_derivatives_equal_all_three_untwisted_relations':True,'proper_elliptic_criterion':'D*E*((D^3+E^3+1)^3-27*D^3*E^3) !=0','nine_line_factorization':'product_(a,b=0..2)(D+omega^a*E+omega^b)','finite_cover_after_axes_and_nonPHS_removal':line_data,'normalized_parameter_polynomial_low_to_high':encode(h0),'normalized_parameterization':'D=-omega^b*(t+1), E=omega^(b-a)*t, a,b=0..2','sum_line_degrees':sum(h.degree() for h in hs),'geometric_finite_point_count':count,'common_E_polynomial_degree':lcm.degree(),'multiple_line_points':[{'D':list(ds),'E':list(es),'line_indices':sorted(ids)} for (ds,es),ids in multi.items()],'scope':'conditional necessary cover from elliptic obstruction plus previous Delta-open exclusion, not admissibility at remaining points','not_claimed':['remaining finite points excluded','axis families classified','complete H3 classification','EG/Rains/trace geometry computer verified']}
Path(__file__).with_name('cubic_third_root_unit_boundary_elliptic_reduction_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','axis_families':2,'finite_geometric_points':count,'line_degrees':[h.degree() for h in hs],'E_polynomial_degree':lcm.degree()}))
