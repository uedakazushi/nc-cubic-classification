#!/usr/bin/env python3
"""Full zero-fifth determinant boundary, including every coupling and number-field root."""
from pathlib import Path
from itertools import permutations
import json,sympy as s
from cubic_sparse_hilbert import SparseGradedAlgebra
from verify_cubic_as4_four_simple import source_matrix,U,K
from verify_cubic_as4_four_simple_boundary_R import r_matrix
ROOT=Path(__file__).resolve().parent;D=json.loads((ROOT/'cubic_CY_four_point_zero_determinant_input.json').read_text());assert D['source_commit']=='6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0'
la=s.Symbol('lambda');x=s.symbols('x0:21');g=s.Symbol('g');u,v,r=s.symbols('u v r');R,A=source_matrix(la,dict(enumerate(x)));B=(A*((K.T*K).inv()*K.T*(R-U)).T).applyfunc(s.cancel)
C=s.zeros(6);C[1,4]=C[4,1]=(la+1)/8;C[2,3]=C[3,2]=-la/8;J=s.zeros(6)
for i,j,value in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=value
M=(C+g*J-B.T*A.inv()*B).applyfunc(s.cancel)
def parse(z):return s.sympify(z,locals={'lam':la,'Matrix':s.Matrix})
def vals(data):return {(la if k=='lam' else s.Symbol(k)):parse(z) for k,z in data.items()}
def clean(es):return [z for z in dict.fromkeys(s.factor(s.cancel(z)) for z in es) if z!=0]
def unit(z,allow_minus=False):
 if not z or not z.free_symbols<={la}:return False
 for n in s.cancel(z).as_numer_denom():
  pol=s.Poly(n,la,domain=s.QQ_I)
  for ff in [la,la+1,*([la-1] if allow_minus else [])]:
   f=s.Poly(ff,la,domain=s.QQ_I)
   while pol.degree()>0 and pol.rem(f).is_zero:pol=pol.exquo(f)
  if pol.degree()>0 or not pol.LC():return False
 return True

def replay(eqs,trace):
 base={}
 for st in trace:
  var=s.Symbol(st['variable']);eq=parse(st['equation']);pivot=parse(st['unit_pivot']);value=parse(st['value'])
  assert any(s.cancel(z-eq)==0 for z in eqs)
  pol=s.Poly(s.together(eq).as_numer_denom()[0],var);assert pol.degree()==1 and s.cancel(pol.LC()-pivot)==0 and unit(pivot)
  assert s.cancel(-pol.TC()/pivot-value)==0
  base={k:s.cancel(z.subs(var,value)) for k,z in base.items()};base[var]=value;eqs=clean([z.subs(var,value) for z in eqs])
 return base,eqs

def compose(*parts):
 vv={k:s.sympify(z) for part in parts for k,z in part.items()}
 for _ in range(20):
  new={k:s.cancel(z.subs(vv,simultaneous=True)) for k,z in vv.items()}
  if new==vv:return vv
  vv=new
 raise AssertionError('coefficient substitution cycle')
initial={x[0]:1,x[1]:1,x[2]:1,x[3]:0,x[4]:0,x[5]:0};cover=D['coverage']
_,eqs1=replay(clean(M.subs({**initial,x[17]:1},simultaneous=True)),cover['nonzero_x17_elimination']);assert any(unit(z) for z in eqs1)
base,eqs=replay(clean(M.subs({**initial,x[17]:0},simultaneous=True)),cover['zero_x17_elimination']);base=compose(initial,{x[17]:0},base)
q,b,c,k=x[10],x[11],x[8],x[14];coupling=[x[6],x[7],x[13],x[9]];small=[s.together(z).as_numer_denom()[0] for z in eqs if not(z.free_symbols&set(coupling))]
split=(k+q*q)*(la*q+la*c+q);assert any(unit(s.cancel(z/split)) for z in eqs)
sat=s.Symbol('sat')
def gb(polys,gens,units):return s.groebner([s.together(z).as_numer_denom()[0] for z in polys]+[sat*units-1],sat,*gens,domain=s.QQ)
def same(G,H):assert [z.as_expr() for z in G.polys]==[z.as_expr() for z in H.polys]
GA=gb([z.subs(k,-q*q) for z in small],[c,b,q,la],la*(la+1));GB=gb([z.subs(c,-(la+1)*q/la) for z in small],[k,b,q,la],la*(la+1))
for target in cover['A_split_memberships']:assert GA.reduce(s.expand(parse(target)))[1]==0
for target in cover['B_split_memberships']:assert GB.reduce(s.expand(parse(target)))[1]==0
branches={};linear_matrices={}
for eta in [-1,1]:
 qq=eta*la/(4*(la-1))
 cases={'Ap':{q:qq,b:eta*la*la/(4*(la-1)),c:eta*(la+1)/4,k:-qq*qq},
 'Am':{q:qq,b:-eta*la*la/(4*(la-1)),c:-eta*(la*la+1)/(4*(la-1)),k:-qq*qq},
 'Az':{q:0,b:eta*la/4,c:eta*(la+1)/4,k:0},'B':{q:eta*la/4,b:0,c:-eta*(la+1)/4,k:0},
 'A1':{la:1,q:eta*s.I/8,b:-eta*s.I/8,c:0,k:s.Rational(1,64)},
 'Ah':{la:s.Rational(1,2),q:eta*s.sqrt(3)*s.I/12,b:-eta*s.sqrt(3)*s.I/24,c:-eta*s.sqrt(3)*s.I/8,k:s.Rational(1,48)},
 'Bh':{la:2,q:eta*s.sqrt(3)*s.I/6,b:-eta*s.sqrt(3)*s.I/3,c:-eta*s.sqrt(3)*s.I/4,k:-s.Rational(1,6)}}
 generic={q:qq,k:-qq*qq};unit0=la*(la+1)*(la-1)
 same(gb([z.subs(generic,simultaneous=True) for z in small],[c,b,la],unit0),gb([4*(la-1)*(c-b)+eta,16*(la-1)**2*b*b-la**4],[c,b,la],unit0))
 same(gb([z.subs({q:0,k:0}) for z in small],[c,b,la],la*(la+1)),gb([la*c-(la+1)*b,16*b*b-la*la],[c,b,la],la*(la+1)))
 sub={q:eta*la/4,c:-eta*(la+1)/4};same(gb([z.subs(sub,simultaneous=True) for z in small],[k,b,la],la*(la+1)),gb([k,b],[k,b,la],la*(la+1)))
 for name,sub in cases.items():
  assert all(s.simplify(z.subs(sub,simultaneous=True))==0 for z in small)
  es=[s.cancel(z.subs(sub,simultaneous=True)) for z in eqs];branches[name,eta]=(sub,es)
  lins=[z for z in es if s.Poly(z,*coupling).total_degree()==1 and not z.has(x[9])]
  LM=s.linear_eq_to_matrix(lins,coupling[:3])[0];linear_matrices[name,eta]=LM
  if name in ['Am','Ap','Az','B']:
   recorded=parse(D['bad_records'][name+str(eta)]['linear_matrix']);assert (LM-recorded).applyfunc(s.cancel)==s.zeros(*LM.shape)
   if name=='Am':
    assert LM.rank()==1 and any(unit(z,True) for z in LM)
    assert (LM*s.Matrix([-u/la,u,v])).applyfunc(s.cancel)==s.zeros(LM.rows,1)
   else:
    determinant={'Ap':la**4+1,'Az':(2*la+1)**2,'B':(la+2)**2}[name];assert LM.shape==(3,3) and unit(s.cancel(LM.det()/determinant),True)
  else:assert LM.rank()==3
 # At each fixed base root, verify no additional b,c,k points were discarded.
 for name in ['A1','Ah','Bh']:
  sub,_=branches[name,eta];known={la:sub[la],q:sub[q]}
  if name!='Bh':known[k]=-sub[q]**2
  else:known[c]=-(sub[la]+1)*sub[q]/sub[la]
  unknown=[z for z in [k,c,b] if z not in known];field=s.QQ_I if name=='A1' else s.QQ.algebraic_field(s.sqrt(3)*s.I)
  actual=s.groebner([s.simplify(z.subs(known,simultaneous=True)) for z in small],*unknown,domain=field)
  target=s.groebner([z-sub[z] for z in unknown],*unknown,domain=field);same(actual,target)
print('PASS complete base ideals and all seven coupling matrices for both signs',flush=True)
records=[]
def quotient(name,values,last,expected,mp=None,root=None):
 RR=R.subs(values,simultaneous=True).applyfunc(s.cancel)
 if mp is not None:
  assert s.Poly(mp,la).is_irreducible and s.minpoly(root,la)==mp
  F=s.QQ.algebraic_field(root);alpha=F.unit
  def convert(z):
   n,d=s.cancel(z).as_numer_denom()
   def at(pol):return sum((F.convert(co)*alpha**powers[0] for powers,co in s.Poly(pol,la,domain=s.QQ).terms()),F.zero)
   return at(n)/at(d)
  assert all(not convert(z) for z in M.subs(values,simultaneous=True))
 else:
  assert M.subs(values,simultaneous=True).applyfunc(s.cancel)==s.zeros(6)
  params=sorted(set().union(*(z.free_symbols for z in RR)),key=str);F=s.QQ.frac_field(*params) if params else s.QQ;convert=F.from_sympy
  for z in RR:assert unit(s.cancel(z).as_numer_denom()[1],name.startswith(('Am','Ap')))
 rels=[{divmod(i,4):convert(RR[i,j]) for i in range(16) if RR[i,j]} for j in range(6)]
 algebra=SparseGradedAlgebra(F,4,rels,[0]*4);algebra.build(last);dims=[len(algebra.basis[n]) for n in range(last+1)]
 assert dims[-1]==expected and expected>s.binomial(last+3,3),(name,dims)
 records.append({'name':name,'dimensions':dims,'minimal_polynomial':str(mp) if mp is not None else None});print('PASS',name,dims,flush=True)
for eta in [-1,1]:
 for name in ['Am','Ap','Az','B']:
  vv=vals(D['bad_records'][name+str(eta)]['generic_normal']);quotient(name+str(eta),vv,4 if name in ['Am','Ap'] else 3,37 if name in ['Am','Ap'] else 21)
 # Every exceptional one-dimensional coupling kernel is normalized to coordinate1.
 sub,es=branches['Ap',eta];LM=linear_matrices['Ap',eta];mp=la**4+1;root=s.sqrt(2)*(1+s.I)/2
 vector=s.Matrix([1,la*la,-eta*la/(4*(la-1))]);cp={x[6]:1,x[7]:la*la,x[13]:-eta*la/(4*(la-1)),x[9]:-1}
 assert all(s.rem(s.cancel(z).as_numer_denom()[0],mp,la)==0 for z in LM*vector)
 vv=compose(base,sub,cp);quotient('Ap8'+str(eta),vv,5,59,mp,root)
 vv=compose(base,sub,{x[6]:0,x[7]:0,x[13]:0,x[9]:1});quotient('Api'+str(eta),vv,5,58,la*la+1,s.I)
 for name,ll,vector,lastx9 in [('Az',-s.Rational(1,2),s.Matrix([1,0,0]),-1),('B',s.Integer(-2),s.Matrix([0,1,s.Rational(eta,2)]),1)]:
  sub,es=branches[name,eta];LM=linear_matrices[name,eta].subs(la,ll);assert LM.rank()==2 and LM*vector==s.zeros(3,1)
  vv=compose(base,sub,{la:ll,x[6]:vector[0],x[7]:vector[1],x[13]:vector[2],x[9]:lastx9});quotient(name+'special'+str(eta),vv,3,21)
assert len(records)==16
print('PASS all16 original bad quotient families and all algebraic conjugates',flush=True)
# Connect every computed bad family to the full residual coupling equations.
for eta in [-1,1]:
 for name in ['Am','Ap','Az','B']:
  sub,es=branches[name,eta]
  cp={x[6]:-u/la,x[7]:u,x[13]:v,x[9]:-eta*4*u*v*(la-1)/la**2} if name=='Am' else dict.fromkeys(coupling,0)
  actual=compose(base,sub,cp);recorded=vals(D['bad_records'][name+str(eta)]['generic_normal'])
  assert (R.subs(actual,simultaneous=True)-R.subs(recorded,simultaneous=True)).applyfunc(s.cancel)==s.zeros(16,6)
  before={key:value for key,value in cp.items() if key!=x[9]};left=[s.cancel(z.subs(before,simultaneous=True)) for z in es]
  factor=la*la+1 if name=='Ap' else 1
  assert any(unit(s.diff(z,x[9])/factor,True) for z in left)
  assert all(s.cancel(z.subs(cp,simultaneous=True))==0 for z in es)

def number_field(mp,root):
 assert s.Poly(mp,la).is_irreducible and s.minpoly(root,la)==mp
 F=s.QQ.algebraic_field(root);alpha=F.unit
 def cv(z):
  n,d=s.cancel(z).as_numer_denom()
  def at(pol):return sum((F.convert(co)*alpha**powers[0] for powers,co in s.Poly(pol,la,domain=s.QQ).terms()),F.zero)
  return at(n)/at(d)
 return F,cv
from sympy.polys.matrices import DomainMatrix
for eta in [-1,1]:
 LM=linear_matrices['Ap',eta]
 for mp,root,rank in [(la**4+1,s.sqrt(2)*(1+s.I)/2,2),(la*la+1,s.I,3)]:
  F,cv=number_field(mp,root);mat=DomainMatrix.from_dod({i:{j:cv(LM[i,j]) for j in range(3) if LM[i,j]} for i in range(3)},(3,3),F);assert mat.rank()==rank
  if rank==2:
   sub,es=branches['Ap',eta];before={x[6]:1,x[7]:la*la,x[13]:-eta*la/(4*(la-1))};left=[s.cancel(z.subs(before,simultaneous=True)) for z in es]
   assert any(s.Poly(z,x[9]).degree()==1 and bool(cv(s.diff(z,x[9]))) for z in left)
 for name,ll,vector in [('Az',-s.Rational(1,2),s.Matrix([1,0,0])),('B',s.Integer(-2),s.Matrix([0,1,s.Rational(eta,2)]))]:
  sub,es=branches[name,eta];before={x[6]:vector[0],x[7]:vector[1],x[13]:vector[2]};left=[s.cancel(z.subs(before,simultaneous=True).subs(la,ll)) for z in es]
  assert any(s.Poly(z,x[9]).degree()==1 and s.diff(z,x[9])!=0 for z in left)
 # All retained base fibers have full-rank coupling matrices; only A1 keeps x9 free.
 for name in ['A1','Ah','Bh']:
  sub,es=branches[name,eta];cp={x[6]:0,x[7]:0,x[13]:0,x[9]:r if name=='A1' else 0};actual=compose(base,sub,cp)
  recorded=vals(D['good_fibers'][str((name,eta))]);assert (R.subs(actual,simultaneous=True)-R.subs(recorded,simultaneous=True)).applyfunc(s.simplify)==s.zeros(16,6)
  assert M.subs(actual,simultaneous=True).applyfunc(s.simplify)==s.zeros(6)
  if name!='A1':
   left=[s.cancel(z.subs(dict.fromkeys(coupling[:3],0))) for z in es]
   assert any(s.Poly(z,x[9]).degree()==1 and s.diff(z,x[9])!=0 for z in left)
print('PASS all coupling ranks, kernels, exceptional multiplicities and good/bad family connections',flush=True)
# The remaining torus rescales each nonzero kernel coordinate to1, and x9 by its square.
z=s.Symbol('z',nonzero=True);T=s.diag(1,z,z,1);TT=s.kronecker_product(T,T);lu=(U.T*U).inv()*U.T;lk=(K.T*K).inv()*K.T;BP=(lu*TT*U*B*(lk*TT*K).T/s.det(T)).applyfunc(s.cancel)
pos={j:next((a,b) for a in range(6) for b in range(6) if B[a,b]==x[j]) for j in range(21)}
for j in [0,1,2,8,10,11,14]:a,b0=pos[j];assert s.cancel(BP[a,b0]-x[j])==0
for j in [6,7,13]:a,b0=pos[j];assert s.cancel(BP[a,b0]-z*x[j])==0
a,b0=pos[9];assert s.cancel(BP[a,b0]-z*z*x[9])==0
# Literal old C and R_1 transports, both signs; h=0 centre ranks are reused.
Q=s.Rational
oldC,_=source_matrix(s.Integer(1),{0:1,1:1,2:1,10:s.I/8,16:s.I/8,11:-s.I/8,15:-s.I/8,14:Q(1,64),19:Q(1,64),20:Q(1,64)})
for eta in [-1,1]:
 good=vals(D['good_fibers'][str(('A1',eta))]);target0=R.subs(good,simultaneous=True).subs(r,0);assert (target0-oldC.xreplace({s.I:eta*s.I})).applyfunc(s.simplify)==s.zeros(16,6)
 target1=R.subs(good,simultaneous=True).subs(r,1);oldR,_=r_matrix(1,eta);i=eta*s.I;P=s.diag(1,Q(1,8),i,i/8)*s.eye(4)[:,[1,0,3,2]];transport=s.kronecker_product(P,P)*oldR;change=(lu*transport).applyfunc(s.simplify);assert change.det()!=0 and (target1*change-transport).applyfunc(s.simplify)==s.zeros(16,6)
# Literal original relation transports for every Ah/Bh exceptional point from old N.
zeta=s.sqrt(3)*s.I;oldN,_=source_matrix(s.Integer(2),{0:1,1:1,2:-2,8:zeta/4,10:zeta/6,11:zeta/6,16:zeta/6,15:-zeta/12,14:Q(1,12),19:Q(1,12),20:Q(1,12)})
AN=A.subs(la,2);BN=(AN*((K.T*K).inv()*K.T*(oldN-U)).T).applyfunc(s.simplify)
targets={str((name,eta)):R.subs(vals(D['good_fibers'][str((name,eta))]),simultaneous=True).applyfunc(s.simplify) for name in ['Ah','Bh'] for eta in [-1,1]};matched={}
for perm in permutations(range(4)):
 P=s.eye(4)[:,perm];PP=s.kronecker_product(P,P);SS=lu*PP*U;KK=lk*PP*K;sc=s.factor(2*(SS*AN*SS.T)[0,5]);BP=(SS*BN*KK.T/sc).applyfunc(s.simplify);beta=BP[pos[1][0],pos[1][1]];b0=BP[pos[0][0],pos[0][1]]
 if not beta or not b0:continue
 T=s.diag(1,beta/b0,1,beta);transport=s.kronecker_product(T*P,T*P)*oldN;change=(lu*transport).applyfunc(s.simplify)
 if not change.det():continue
 for name,target in targets.items():
  if (target*change-transport).applyfunc(s.simplify)==s.zeros(16,6):matched[name]={'permutation':perm,'diagonal':list(map(str,T.diagonal()))}
assert set(matched)==set(targets)
out={'status':'PASS','source_commit':D['source_commit'],'scope':'entire zero-fifth determinant boundary H3 empty; together with earlier necessary covers, all degree1 shared supports empty','independent_coverage':['both original unit elimination traces and nonzero x17 unit contradiction','both split memberships and all localized base ideal equalities, both signs','all seven full coupling matrices; generic rank/determinant and complete kernels','all exceptional number-field ranks and coupling1 normalization, every conjugate retained','actual family connections and all original inserted relation coordinates checked'],'bad_quotients':records,'literal_exceptional_N_transports':matched,'old_fixed_exclusions_reused':'C and its coefficient conjugate, R_1 signs/all nonzero r, N; no fresh downstream centre3 run claimed','ordinary_dependencies':['base polynomial memberships give seven exhaustive cases','raw relation rank gives all-closed dimension lower bounds on stated units','torus normalization of nonzero kernel coordinate and nonzero x9 over algebraically closed field','existing all-parameter first/open/general-boundary exclusions and old C/R/N centre obstructions'],'not_claimed':['relative reduced scheme coverage','degree2/partial-active/full shared supports excluded','AS sufficiency/full automorphism theorem imported','complete CY or H3 classification','novelty confirmed']}
(ROOT/'cubic_CY_four_point_zero_determinant_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS full zero-fifth determinant boundary, every base/coupling/number-field branch and all old C/R/N transports')

