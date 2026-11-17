#!/usr/bin/env python3
"""Full first-shared x0=0 chart: independent unit elimination and eight quotients."""
from pathlib import Path
import json,sympy as s
from cubic_sparse_hilbert import SparseGradedAlgebra
from verify_cubic_as4_four_simple import source_matrix,U,K
from verify_cubic_as4_four_simple_first import fn_matrix
ROOT=Path(__file__).resolve().parent;D=json.loads((ROOT/'cubic_CY_four_point_first_input.json').read_text())
assert D['source_commit']=='6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0'
la=s.Symbol('lambda');x=s.symbols('x0:21');g=s.Symbol('g');R,A=source_matrix(la,dict(enumerate(x)));B=(A*((K.T*K).inv()*K.T*(R-U)).T).applyfunc(s.cancel)
C=s.zeros(6);C[1,4]=C[4,1]=(la+1)/8;C[2,3]=C[3,2]=-la/8
J=s.zeros(6)
for i,j,v in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=v
M=(C+g*J-B.T*A.inv()*B).applyfunc(s.cancel)
def parse(v):return s.sympify(v,locals={"lam":la})
def vals(data):return {(la if k=="lam" else s.Symbol(k)):parse(v) for k,v in data.items()}
def unit(v):
 for n in s.cancel(v).as_numer_denom():
  poly=s.Poly(n,la)
  for f in [s.Poly(la,la),s.Poly(la+1,la)]:
   while poly.degree()>0 and poly.rem(f).is_zero:poly=poly.exquo(f)
  assert poly.degree()==0 and poly.LC()!=0

def clean(eqs):return [v for v in dict.fromkeys(s.factor(s.cancel(v)) for v in eqs) if v!=0]
branches={}
for tag,rec in D['coverage'].items():
 eqs=clean(M.subs(vals(rec['initial']),simultaneous=True))
 for step in rec['eliminations']:
  v=s.Symbol(step['variable']);equation=parse(step['equation']);pivot=parse(step['unit_pivot']);value=parse(step['value'])
  assert any(s.cancel(q-equation)==0 for q in eqs)
  poly=s.Poly(s.together(equation).as_numer_denom()[0],v);assert poly.degree()==1 and s.cancel(poly.LC()-pivot)==0
  unit(pivot);assert s.cancel(-poly.TC()/pivot-value)==0
  eqs=clean([q.subs(v,value) for q in eqs])
 assert set(map(str,eqs))==set(map(str,clean(map(parse,rec['remaining_equations']))))
 assert clean(M.subs(vals(rec['resolved_coefficients']),simultaneous=True))==eqs
 branches[tag]=eqs
# Recompute every main saturated boundary consequence on the complete residual equations.
for tag,rec in D['saturated_consequences'].items():
 polys=[s.together(v).as_numer_denom()[0] for v in branches[tag]];inv=s.Symbol('inverse');polys.append(inv*parse(rec['localized_at'])-1)
 vs=sorted(set().union(*(p.free_symbols for p in polys)),key=str);G=s.groebner(polys,*vs,order='grevlex',domain=s.QQ)
 for target in [rec['consequence'],*rec['additional_consequences']]:assert G.reduce(s.expand(parse(target)))[1]==0
records=[]
for name,data in D['candidate_coefficients'].items():
 vv=vals(data);assert M.subs(vv,simultaneous=True).applyfunc(s.cancel)==s.zeros(6)
 RN=R.subs(vv,simultaneous=True).applyfunc(s.cancel)
 if name not in D['bad_dimensions']:continue
 params=sorted(set().union(*(v.free_symbols for v in RN)),key=str);F=s.QQ.frac_field(*params)
 for v in RN:
  den=s.Poly(s.cancel(v).as_numer_denom()[1],*params,domain=s.QQ)
  for f in [la,la+1]:
   if la not in params:continue
   ff=s.Poly(f,*params,domain=s.QQ)
   while den.total_degree()>0 and den.rem(ff).is_zero:den=den.exquo(ff)
  assert den.total_degree()==0
 rels=[{divmod(i,4):F.from_sympy(RN[i,j]) for i in range(16) if RN[i,j]} for j in range(6)]
 Q=SparseGradedAlgebra(F,4,rels,[0]*4);Q.build(3);dims=[len(Q.basis[n]) for n in range(4)];assert dims==[1,4,10,D['bad_dimensions'][name]] and dims[-1]>20
 records.append({'name':name,'dimensions':dims,'parameters':list(map(str,params))});print('PASS',name,dims,flush=True)
# Entire universal constrained normal form is the previously excluded FN2 presentation.
universal=vals(D['universal_coefficients']);constraints=list(map(parse,D['constraints']));c,e,f,r=s.symbols('c e f r');G=s.groebner(constraints,e,r,f,c,la)
for v in M.subs(universal,simultaneous=True):assert G.reduce(s.cancel(v).as_numer_denom()[0])[1]==0
old,_=fn_matrix(la,c,e,f,r);assert (R.subs(universal,simultaneous=True)-old).applyfunc(s.cancel)==s.zeros(16,6)
assert len(records)==8
out={'status':'PASS','source_commit':D['source_commit'],'scope':'necessary complete x1 nonzero, x0=x3=x4 zero chart; entire H3 stratum empty by old FN2 full exclusions','unit_elimination':'all four original21-variable branches replayed step by step, every equation and unit pivot independently checked','saturated_consequences':'all four main localized ideals recomputed over QQ','bad_original_quotients':records,'retained_transport':'literal constrained universal FN2 old presentation','ordinary_dependencies':['diagonal normalization x1=1 and independent x2,x5 to0/1 by algebraic closedness','full FN1-FN6 branch proof and isolated upstream controller replay','generic original relation rank gives lower bounds at every permitted closed value','existing all-parameter L/M/F/G/K H3 exclusions'],'not_claimed':['degree1 x0 nonzero chart covered','degree2 or full shared supports classified','AS sufficiency/full automorphisms imported','relative scheme coverage','full H3 classification','novelty confirmed']}
(ROOT/'cubic_CY_four_point_first_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS full first-shared necessary cover: every unit elimination, saturated consequence, eight original quotients and universal old transport')
