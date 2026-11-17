#!/usr/bin/env python3
"""Scoped necessary finite-base4/31 covers with independent bad Hilbert checks.
Proof data come from pinned as4; all original relation matrices are rebuilt.
No AS4 sufficiency or automorphism statement is imported.
"""
from pathlib import Path
import json,itertools,sympy as s
from cubic_incremental_graded import GradedAlgebra
from verify_cubic_as4_curvilinear_fixed import rels1,rels2,rels31
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_CY_finite43_input.json').read_text());assert D['source_commit']=='6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0'
a,b,c,d=s.symbols('a b c d');Y=[a,b,c,d];pairs=list(itertools.combinations(range(4),2));K=s.zeros(16,6)
for j,(i,k) in enumerate(pairs):K[4*i+k,j]=1;K[4*k+i,j]=-1
J=s.zeros(6);J[0,5]=J[5,0]=1;J[1,4]=J[4,1]=-1;J[2,3]=J[3,2]=1;g=s.Symbol('g');x=s.symbols('x:21');words=list(itertools.product(range(4),repeat=4))
def parse(t):return s.sympify(t,locals={'Matrix':s.Matrix})
def quad(q):
 p=s.Poly(s.expand(q),*Y);v=s.zeros(16,1)
 for i in range(4):
  v[5*i]=p.coeff_monomial(Y[i]**2)
  for j in range(i+1,4):v[4*i+j]=v[4*j+i]=p.coeff_monomial(Y[i]*Y[j])/2
 return v
def frame(qs,A,B,C0):
 U=s.Matrix.hstack(*map(quad,qs));assert A.det()!=0
 H=U*A*U.T+U*B*K.T+K*B.T*U.T+K*(C0+g*J)*K.T
 assert all(s.expand(H[4*w[0]+w[1],4*w[2]+w[3]]+H[4*w[3]+w[0],4*w[1]+w[2]])==0 for w in words)
 assert s.Matrix(list(B)).jacobian(x).rank()==21
 cols=[]
 for i,j in itertools.product(range(6),repeat=2):
  HH=U[:,i]*K[:,j].T+K[:,j]*U[:,i].T;cols.append(s.Matrix([HH[4*w[0]+w[1],4*w[2]+w[3]]+HH[4*w[3]+w[0],4*w[1]+w[2]] for w in words]))
 assert s.Matrix.hstack(*cols).rank()==15
 return U,(C0+g*J-B.T*A.inv()*B).applyfunc(s.expand),U+K*B.T*A.inv()
def empty(M,values):
 vals={s.Symbol(k):parse(v) for k,v in values.items()};dd=M.subs(vals,simultaneous=True).applyfunc(s.expand);vs=sorted(set().union(*(q.free_symbols for q in dd)),key=str);G=s.groebner(list(dd),*vs,order='grevlex',domain=s.QQ);assert list(G)==[1]
def transport(R,U,rr):
 E=s.zeros(16,6)
 for j,rel in enumerate(rr):
  for (i,k),c in rel.items():E[4*i+k,j]=c
 change=(U.T*U).inv()*U.T*E;assert (R*change-E).applyfunc(s.expand)==s.zeros(16,6) and change.det()!=0
records=[]
def bad_quotient(name,R,expected,units):
 params=sorted(set().union(*(q.free_symbols for q in R)),key=str);assert set(map(str,params))<={'h','mu','j'}
 if any(q.has(s.sqrt(2)) for q in R):base=s.QQ.algebraic_field(s.I,s.sqrt(2))
 elif any(q.has(s.I) for q in R):base=s.QQ_I
 else:base=s.QQ
 F=base.frac_field(*params) if params else base
 for q in R:
  if params:
   den=s.Poly(s.cancel(q).as_numer_denom()[1],*params,domain=base);assert len(den.terms())==1
   for p,e in zip(params,den.monoms()[0]):assert not e or str(p) in units
 rels=[{divmod(i,4):F.from_sympy(R[i,j]) for i in range(16) if R[i,j]} for j in range(6)];B=GradedAlgebra(F,4,rels,[0]*4);B.build(len(expected)-1);dims=[len(B.basis[i]) for i in range(len(expected))];assert dims==expected and dims[-1]>s.binomial(len(expected)+2,3);records.append({'case':name,'dimensions':dims,'parameters':list(map(str,params)),'inverted_parameters':sorted(units)})
# Projection4: all four empty leading charts and all five residual tuples.
data=D['4'];A=s.zeros(6)
for i,j,v in [(0,5,-s.Rational(1,2)),(1,4,s.Rational(1,2)),(2,2,-1),(2,3,s.Rational(1,2))]:A[i,j]=v;A[j,i]=v
C0=s.zeros(6)
for i,j in [(2,5),(3,5)]:C0[i,j]=C0[j,i]=-s.Rational(1,8)
C0[4,4]=s.Rational(1,4);B=parse(data['full_mixed_matrix']);U,M,R=frame([a*c-b*b,a*d-b*c,b*d,c*c,c*d,d*d],A,B,C0)
for r in data['empty_leading_charts']:
 if 'normalization' in r:empty(M,r['normalization'])
 else:empty(M,{str(x[0]):'0',str(x[4]):'0',str(x[9]):'0',str(x[1]):'1',str(x[5]):str(r['x5']),str(x[15]):'0','g':'0',str(x[2]):'0',str(x[6]):'0'})
lead=list(map(parse,data['remaining_leading_equations']));u,v,w,t=x[2],x[6],x[7],x[15];G=s.groebner(lead,u,v,w,t,domain=s.QQ);assert G.is_zero_dimensional
assert G.reduce(v*v*(2*v+1)*(7*v+1))[1]==0
low={x[0]:0,x[1]:0,x[4]:0,x[5]:0,x[9]:0,x[10]:1+2*x[6],g:2*x[15]}
for rec in data['candidate_orbits']:
 vals=dict(zip([u,v,w,t],map(parse,rec['leading'])));assert all(not s.expand(q.subs(vals)) for q in lead)
 if rec['branch'] in [1,2]:empty(M,{**{str(k):str(v) for k,v in low.items()},**{str(k):str(v) for k,v in vals.items()}});continue
 normal={s.Symbol(k):parse(v) for k,v in rec['normal_coefficients'].items()};assert M.subs(normal).applyfunc(s.expand)==s.zeros(6);RN=R.subs(normal).applyfunc(s.expand)
 if rec['branch']==0:bad_quotient('CF_branch0',RN,[1,4,10,20,37],set())
 else:transport(RN,U,rels1 if rec['branch']==3 else rels2)
# Projection31: two empty nonzero charts and every one of13 excluded families.
data=D['31'];A=parse(data['A']);B=parse(data['B']);C0=parse(data['C']);U,M,R=frame([a*c-b*b,b*c,c*c,a*d,b*d,c*d],A,B,C0);assert U==parse(data['U'])
for rec in data['empty_nonzero_branches']:empty(M,rec['constant_pivot_elimination'])
for rec in data['excluded_normal_families']:
 vals={s.Symbol(k):parse(v) for k,v in rec['coefficients'].items()};assert M.subs(vals).applyfunc(s.cancel)==s.zeros(6);RR=R.subs(vals).applyfunc(s.cancel)
 units={'h'} if rec['name']=='x12_main' else {'mu'} if rec['name'] in ['x17_mu','x17_zero'] else set();bad_quotient(rec['name'],RR,rec['generic_Hilbert_dimensions'],units)
normal={s.Symbol(k):parse(v) for k,v in data['regular_coefficients'].items()};RN=R.subs(normal);assert RN==parse(data['regular_relations']);transport(RN,U,rels31)
assert len(records)==14
out={'status':'PASS','scope':'scoped necessary projection4/31 covers reduce to the three previously H3-excluded fixed presentations; all14 bad representatives/families independently checked','source_commit':D['source_commit'],'all14_bad_quotients':records,'CF_leading_annihilator':'v^2*(2v+1)*(7v+1), geometric tuple cover only; necessary leading scheme is not asserted reduced','all_three_old_presentation_transports':'literal constant invertible relation bases','coverage_control':'full pinned upstream controllers replayed in isolated workspace, distinguished from this independent downstream control','ordinary_dependencies':['full marked stabilizers and nonzero weight normalizations from pinned proofs','complete branch and special-value coverage using recorded nonzero gauge coefficients','generic raw relation matrix rank gives all-closed quotient dimension lower bound on stated unit domains','existing thm:as4-curvilinear4-h3-exclusion for remaining CF2/CF3/CT2'],'not_claimed':['AS4 sufficient conditions imported','all isomorphisms or automorphism groups imported','remaining projections22/211/1111 excluded','full CY/H3 classification','novelty confirmed']}
(ROOT/'cubic_CY_finite43_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS full21+21 original frames, all empty charts,14 bad quotients and literal transport of all remaining models')
