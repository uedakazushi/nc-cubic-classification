#!/usr/bin/env python3
"""Pinned necessary 211 cover, with independent original graded quotients."""
from pathlib import Path
import json,itertools,sys,sympy as s
TRANSPORT_ONLY="--transport-only" in sys.argv
from cubic_incremental_graded import GradedAlgebra
from verify_cubic_as4_ds211 import source_matrix,U,K,A
class SparseGradedAlgebra(GradedAlgebra):
 # Prefer sparse source rows before choosing pivots, to control exact coefficient growth.
 def echelon(self,rows):
  active=[dict(row) for row in rows if row];piv={}
  while active:
   row=active.pop(min(range(len(active)),key=lambda i:len(active[i])))
   j=min(row);co=row[j];pivot={k:c/co for k,c in row.items()};piv[j]=pivot
   remaining=[]
   for other in active:
    if j in other:self.addto(other,pivot,-other[j])
    if other:remaining.append(other)
   active=remaining
  return piv


 def build(self,n):
  # Only right multiplication is needed for these Hilbert obstructions.
  if n in self.basis:return
  self.build(n-1);F=self.K;previous=len(self.basis[n-1]);rows=[]
  for prefix in range(len(self.basis[n-2])):
   for rel in self.relations:
    row={}
    for (i,j),co in rel.items():
     for k,value in self.right[n-1][prefix,i].items():row[4*k+j]=row.get(4*k+j,F.zero)+co*value
    row={k:v for k,v in row.items() if v}
    if row:rows.append(row)
  piv=self.echelon(rows);free=[j for j in range(4*previous) if j not in piv];fi={j:k for k,j in enumerate(free)}
  self.basis[n]=[self.basis[n-1][j//4]+(j%4,) for j in free]
  self.right[n]={(i,j):{fi[k]:co for k,co in self.reduce({4*i+j:F.one},piv).items()} for i in range(previous) for j in range(4)}
  # Check every original inserted relation against the full coordinate map.
  for row in rows:
   check={}
   for col,co in row.items():self.addto(check,self.right[n][col//4,col%4],co)
   assert not check
  print('degree',n,'dimension',len(free),flush=True)

ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_CY_finite211_input.json').read_text());assert D['source_commit']=='6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0'
x=s.symbols('x0:21');g=s.Symbol('g');R=source_matrix(dict(enumerate(x)));B=(A*((K.T*K).inv()*K.T*(R-U)).T).applyfunc(s.expand)
C=s.zeros(6)
for i,j,v in [(1,4,-s.Rational(1,8)),(2,3,s.Rational(1,8)),(3,4,-s.Rational(1,8))]:C[i,j]=C[j,i]=v
J=s.zeros(6)
for i,j,v in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=v
M=(C+g*J-B.T*A.inv()*B).applyfunc(s.expand);H=U*A*U.T+U*B*K.T+K*B.T*U.T+K*(C+g*J)*K.T
ws=list(itertools.product(range(4),repeat=4));assert all(s.expand(H[4*a+b,4*c+d]+H[4*d+a,4*b+c])==0 for a,b,c,d in ws)
assert s.Matrix(list(B)).jacobian(x).rank()==21
cols=[]
for i,j in itertools.product(range(6),repeat=2):
 HH=U[:,i]*K[:,j].T+K[:,j]*U[:,i].T;cols.append(s.Matrix([HH[4*a+b,4*c+d]+HH[4*d+a,4*b+c] for a,b,c,d in ws]))
assert s.Matrix.hstack(*cols).rank()==15
p,v,w=s.symbols('p v w',nonzero=True);lu=(U.T*U).inv()*U.T;lk=(K.T*K).inv()*K.T
N=s.eye(4);N[1,0]=p;T=s.diag(1,1,v,w);W=s.Matrix([[1,0,0,0],[0,-1,0,0],[0,0,0,1],[0,0,1,0]])
for P,scale in [(N,1),(T,v*w),(W,1)]:
 PP=s.kronecker_product(P,P);SS=lu*PP*U;KK=lk*PP*K
 for mat in [PP*U-U*SS,SS*A*SS.T-scale*A,KK*C*KK.T-scale*C,KK*J*KK.T-scale*J]:assert mat.applyfunc(s.cancel)==s.zeros(*mat.shape)
assert s.expand(M[0,0]-4*x[0]*x[15])==0
records=[]
def check_bad(name,vals,degree,last,allowed):
 if TRANSPORT_ONLY:return
 assert M.subs(vals,simultaneous=True).applyfunc(s.cancel)==s.zeros(6),name
 RN=R.subs(vals,simultaneous=True).applyfunc(s.cancel);params=sorted(set().union(*(q.free_symbols for q in RN)),key=str)
 if any(q.has(s.sqrt(2)) for q in RN):base=s.QQ.algebraic_field(s.I,s.sqrt(2))
 elif any(q.has(s.sqrt(3),s.sqrt(-3)) for q in RN):base=s.QQ.algebraic_field(s.sqrt(-3))
 elif any(q.has(s.I) for q in RN):base=s.QQ_I
 else:base=s.QQ
 F=base.frac_field(*params) if params else base
 if "--flint" in sys.argv and params and len(params)<=2 and base in [s.QQ,s.QQ_I]:
  from cubic_gaussian_rational_function import F as GaussianFraction,CTX
  class NativeField:
   zero=GaussianFraction();one=GaussianFraction(1)
   def from_sympy(self,value):
    imaginary=s.Dummy('imaginary');value=s.sympify(value).xreplace({s.I:imaginary});n,d=s.cancel(value).as_numer_denom()
    def conv(poly):
     data={}
     for powers,c in s.Poly(poly,*params,imaginary,domain=s.QQ).terms():
      exponent=(powers[0],powers[-1],powers[1] if len(params)==2 else 0);data[exponent]=str(c)
     from flint import fmpq
     return CTX.from_dict({m:fmpq(c) for m,c in data.items()})
    return GaussianFraction(conv(n),conv(d))
  F=NativeField()
  test=params[0]+s.I
  assert not (F.from_sympy(test)*F.from_sympy(1/test)-F.one)

 allowed_polys=[s.Poly(q,*params,domain=base) for q in allowed] if params else []
 for q in RN:
  if not params:continue
  den=s.Poly(s.cancel(q).as_numer_denom()[1],*params,domain=base)
  for factor in allowed_polys:
   while den.total_degree()>0:
    quotient,remainder=den.div(factor)
    if not remainder.is_zero:break
    den=quotient
  assert den.total_degree()==0,(name,q,den)
 rels=[{divmod(i,4):F.from_sympy(RN[i,j]) for i in range(16) if RN[i,j]} for j in range(6)]
 Q=SparseGradedAlgebra(F,4,rels,[0]*4);Q.build(degree);dims=[len(Q.basis[i]) for i in range(degree+1)]
 assert dims[-1]==last and last>s.binomial(degree+3,3),(name,dims,last)
 records.append({'name':name,'dimensions':dims,'parameters':list(map(str,params)),'inverted_polynomials':list(map(str,allowed))});print('PASS',name,dims,flush=True)
h,u,z=s.symbols('h u z')
for name,data in D['normal_forms']['final_exclusion'].items():
 vals={s.Symbol(k):s.sympify(v) for k,v in data.items()}
 if name.startswith('vector_'):degree,last=(5,57) if name.endswith('generic') else (4,36)
 elif name.startswith('upper_'):degree,last=7,123
 elif name=='zero_n00_p':degree,last=5,60
 elif name=='zero_n00_r0':degree,last=4,39
 elif name in ['zero_n00_rplus','zero_n00_rminus','zero_d01','zero_d10']:degree,last=3,23
 elif name=='zero_d00':degree,last=3,22
 elif name.startswith('zero_d11'):degree,last=3,21
 else:degree,last=4,42 if name in ['zero_n01_conic','zero_n1_zero'] else 39
 allowed=[] if name=='zero_d00' else [z,u*u-z] if name=='zero_n1_nonzero' else [h,u] if name=='zero_n1_zero' else [h]
 check_bad('DZ_'+name,vals,degree,last,allowed)
# Five discarded families in the second invariant stratum, all polynomial.
l,r,t,p,q,u,v=s.symbols('l r t p q u v');defaults=dict.fromkeys([*x,g],s.S.Zero)
for e in [-1,1]:
 vals={**defaults,x[3]:1,x[15]:s.Rational(e,4),x[13]:-s.Rational(e,4),x[9]:s.Rational(e,4),g:-s.Rational(1,8),x[16]:p,x[18]:u,x[19]:-e*p/4,x[20]:-p*p};check_bad('DT_diagonal'+str(e),vals,3,21,[])
vals={**defaults,x[15]:t,x[11]:t+s.Rational(1,4),x[13]:s.Rational(1,2),g:t/2,x[18]:u,x[19]:v};check_bad('DT_quarter_generic',vals,3,22,[])
vals={**defaults,x[15]:-s.Rational(1,2),x[11]:-s.Rational(1,4),x[9]:r,x[13]:r+s.Rational(1,2),g:-s.Rational(1,4),x[18]:u,x[19]:v};check_bad('DT_boundary_zero_pq',vals,3,22,[])
vals={**vals,x[9]:-s.Rational(1,4),x[13]:s.Rational(1,4),x[16]:p,x[17]:q,x[20]:4*p*q-4*p*v+4*q*u};check_bad('DT_boundary_special_r',vals,3,22,[])
# Original all-parameter source representations already excluded in this repo.
retained=[]
for name,data in D['normal_forms']['nonzero_complete'].items():
 vals={s.Symbol(k):s.sympify(v) for k,v in data.items()};assert M.subs(vals).applyfunc(s.cancel)==s.zeros(6);retained.append(name)
# Match all first-stratum models to the coefficient inputs used by the old exclusions.
Q=s.Rational
expected={
'a2':{0:1,3:1,5:h,12:h,8:-1/(16*h),14:h-Q(1,16),20:Q(1,8)},
'c1u':{0:1,7:1,11:h,13:h,9:h,12:h*h+Q(1,16),14:2*h*h+Q(1,8),20:Q(1,8)},
'c1s':{0:1,7:1,12:h,14:h+Q(1,16),20:h+Q(1,16)}}
for e in [-1,1]:
 k=e*s.I/4
 expected['a1_'+str(e)]={0:1,3:1,4:k,11:k,13:k,9:k,5:-Q(1,16),12:-Q(1,8),14:-Q(1,4),20:Q(1,8)}
 expected['c2_'+str(e)]={0:1,11:k,20:Q(1,8)}
for name,coeff in expected.items():
 vals={s.Symbol(k):s.sympify(vv) for k,vv in D['normal_forms']['nonzero_complete'][name].items()}
 assert (R.subs(vals)-source_matrix(coeff)).applyfunc(s.cancel)==s.zeros(16,6)
for vals in [{15:-2*l,11:-l,9:r,13:r+l+1/(16*l)},{15:-s.I/2,11:-s.I/4,9:r,13:r,20:1}]:
 vv={**defaults,**{x[k]:value for k,value in vals.items()}}
 vv[g]=-2*l*l-Q(1,8) if 20 not in vals else 0
 assert M.subs(vv).applyfunc(s.cancel)==s.zeros(6)

if TRANSPORT_ONLY:
 print("PASS all retained presentation identities including both second-stratum families");sys.exit(0)
assert len(records)==27
out={'status':'PASS','source_commit':D['source_commit'],'coefficient_backend':'existing exact flint Gaussian rational functions with conversion identity checks' if '--flint' in sys.argv else 'Sympy exact fields','scope':'necessary full projection211 cover: 27 bad original quotients and exact retained original frames','bad_quotients':records,'retained_first_stratum':retained,'ordinary_dependencies':['pinned DS1-10, DT4-11 and DZ1-20 necessary full stabilizer and branch covers; upstream replay recorded separately','all-closed rank specialization of original full word relations on stated unit domains','existing all-parameter ds211 H3 exclusions'],'not_claimed':['all branch Groebner calculations independently reimplemented','AS sufficiency or full automorphism theorem imported','relative reduced scheme cover','full H3 classification','novelty confirmed']}
(ROOT/'cubic_CY_finite211_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS full211 frame, group,27 bad quotients')
