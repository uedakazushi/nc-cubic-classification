#!/usr/bin/env python3
"""Complete characteristic-zero controls on all five remaining curves.
Track every elimination pivot and source-image minor. Recompute every exceptional
irreducible factor in its full monogenic number-field extension; no root samples.
"""
from pathlib import Path
import json,sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.polyclasses import DMP
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from cubic_diagonal_top import top_basis,top_matrix
from cubic_incremental_graded import GradedAlgebra
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_four_simple_positive_rank_certificate.json').read_text());assert D['status']=='PASS'
E0=json.loads((ROOT/'cubic_four_simple_positive_finite_certificate.json').read_text());assert E0['status']=='PASS' and E0['remaining_curve_branch_ids']==[0,3,7,10,13]
def domain(i,z,t):
 return {0:t*(t*t+z),3:t*(t*t-z*z),7:t,10:t*(t*t-z*z),13:t*(t*t+z**4-z)}[i]
def values(i,z,t):
 if i==0:return [2*t*t/(t*t+z),t]
 if i==3:return [t,-2*z*z*t/(t*t-z*z)]
 if i==7:return [t]
 if i==10:return [2*z**3*t/(t*t-z*z),t]
 if i==13:return [t,2*t/(t*t+z**4-z)]
 raise ValueError(i)
def serialize(pp):
 return [[list(e),list(map(str,c.to_list()))] for e,c in sorted(pp.to_dict().items())]
class Track(GradedAlgebra):
 def __init__(self,*args,bad,**kwargs):super().__init__(*args,**kwargs);self.bad=bad
 def echelon(self,rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j]
     for pp in [co.numer,co.denom]:self.bad[str(pp)]=pp
     piv[j]={k:c/co for k,c in row.items()};break
    self.addto(row,piv[j],-row[j])
  return piv

def analyze(p,i,K,z,t,bad=None):
 vals=values(i,z,t);lam=[z**e for e in p['Nakayama_exponents']];co=[K.zero]*len(top_basis(K,lam))
 for j,phase,ex in zip(p['active_indices'],p['coefficient_phases'],p['free_exponents']):
  v=z**phase
  for x,e in zip(vals,ex):v*=x**e
  co[j]=v
  if bad is not None:
   for pp in [v.numer,v.denom]:bad[str(pp)]=pp
 # Verify the parameterization satisfies the exact rank equation.
 if p['rank_locus']=='principal':
  total=K.zero
  for ex,coeff in p['rank_equation_native']:
   c=K.zero
   for q in coeff:c=c*z+K.convert(s.Rational(q))
   for x,e in zip(vals,ex):c*=x**e
   total+=c
  assert not total
 H=top_matrix(K,lam,co);hr=H.rank();result={'source_rank':hr}
 if hr!=6:return result
 piv=H.rref()[1];assert len(piv)==6;cc=H.transpose().to_list()
 if bad is not None:
  R=H.extract(range(16),piv);rp=R.transpose().rref()[1];delta=R.extract(rp,range(6)).det();assert delta
  for pp in [delta.numer,delta.denom]:bad[str(pp)]=pp
 rels=[{divmod(j,4):c for j,c in enumerate(cc[k]) if c} for k in piv]
 B=GradedAlgebra(K,4,rels,p['spectrum']) if bad is None else Track(K,4,rels,p['spectrum'],bad=bad)
 B.build(4);dims=[len(B.basis[n]) for n in range(5)];result['dimensions']=dims
 if dims[3:]!=[20,35]:return result
 ids=[j for j,w in enumerate(B.basis[3]) if sum(p['spectrum'][v] for v in w)%p['N']==0];cols=[]
 for j in ids:
  col={}
  for k in range(4):
   row=dict(B.right[4][j,k]);B.addto(row,B.left[4][k,j],-K.one/lam[k])
   for r,c in row.items():col[k*len(B.basis[4])+r]=c
  cols.append(col)
 rows=sorted(set().union(*(set(c) for c in cols))) if cols else[]
 rr=[{j:c[r] for j,c in enumerate(cols) if r in c} for r in rows]
 if bad is not None:rank=len(B.echelon(rr))
 else:rank=DomainMatrix.from_dod({i:r for i,r in enumerate(rr)},(len(rows),len(cols)),K).rank()
 result.update(normal_shape=[len(rows),len(cols)],normal_rank=rank,nullity=len(cols)-rank)
 return result
out=[]
for i in E0['remaining_curve_branch_ids']:
 p=D['branches'][i];zvar=s.Symbol('z');tvar=s.Symbol('t');F=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(p['root_order'],zvar),zvar));K=F.frac_field(tvar);zz=K.convert(F.unit,F);tt=K.gens[0];bad={};generic=analyze(p,i,K,zz,tt,bad)
 assert generic['source_rank']==6 and generic['dimensions'][3:]==[20,35] and generic['nullity']==0
 # Include parameter-domain exclusions independently of every row reduction.
 d=domain(i,zz,tt)
 for pp in [d.numer,d.denom]:bad[str(pp)]=pp
 factors={}
 for pp in bad.values():
  assert pp
  unit,parts=pp.factor_list(); product=pp.ring.ground_new(unit)
  for f,m in parts:product*=f**m
  assert product==pp
  for f,m in parts:
   f=f.monic();factors[str(f)]=f
 fresh=[]
 for f in factors.values():
  pol=s.Poly.new(DMP.from_dict(f.to_dict(),0,F),tvar);assert pol.is_irreducible;E=MonogenicFiniteExtension(pol);tau=E.generator;eta=E.convert(F.unit,F);rec={'irreducible_factor':serialize(f),'degree_over_cyclotomic_field':pol.degree()}
  if not domain(i,eta,tau):rec['status']='outside parameter domain'
  else:
   rec.update(analyze(p,i,E,eta,tau));assert rec['source_rank']!=6 or rec.get('dimensions',[0]*5)[3:]!=[20,35] or rec['nullity']==0;rec['status']='excluded'
  fresh.append(rec);print('FRESH',i,pol.degree(),rec['status'],rec.get('nullity'),flush=True)
 out.append({'branch_id':i,'N':p['N'],'spectrum':p['spectrum'],'root_order':p['root_order'],'generic':generic,'tracked_pivot_polynomial_count':len(bad),'all_pivot_polynomials':[serialize(pp) for pp in bad.values()],'all_exceptional_irreducible_factors':fresh})
 print('CURVE',i,'ALL VALUES PASS',len(fresh),flush=True)
(ROOT/'cubic_four_simple_final_curves_certificate.json').write_text(json.dumps({'status':'PASS','scope':'all five remaining one-parameter necessary charts, all source/graded/normal elimination pivots and every irreducible exceptional factor; four-simple H3 sector empty','all_five_curves':out,'not_claimed':['complete H3 classification','CY or unipotent coverage','novelty confirmed','homological source lemmas fully formalized']},indent=2)+'\n')
print('PASS all five curves including all exceptional roots; four-simple H3 sector empty')
