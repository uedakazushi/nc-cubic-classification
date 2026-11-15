#!/usr/bin/env python3
"""Exact small-representation trace schemes and central-value norms."""
import sympy as s,json,itertools,time
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
root=Path(__file__).parent;T=s.symbols('g');K=s.QQ.algebraic_field(2**s.Rational(1,4));gg=K.to_sympy(K.unit);g=K.unit;x,y,z,D=s.symbols('x y z D');xs=[x,y,z];zero=K.zero
source=json.load(open(root/'cubic_clifford_integration_certificate.json'))
def cv(e):return K.from_sympy(s.cancel(e))
def txt(c):
 v=c.to_list();return str(s.factor(sum(s.Rational(str(a))*T**(len(v)-1-i) for i,a in enumerate(v))))
def terms_poly(rows):return sum(s.sympify(t['coefficient'])*D**t['D_power'] for t in rows)
crit=json.load(open(root/'cubic_order4_center_critical_certificate.json'))
fixed={'h':1,'z':gg,'A':1/(2*gg),'B':1/(2*gg),'C':0,'beta_x':1,'beta_y':1,'beta_z':2,'D':0}
cut=[(r['active_word'],cv(s.sympify(r['coefficient']).subs(fixed,simultaneous=True))) for r in source['integrated_cut_coefficients']]
L=s.Matrix([[x-1,-z,-y],[-z,y-1,-x],[-y,-x,z]]);Adj=L.adjugate();G=-Adj/gg**2;orient=-L.det()/gg**3

def tr(word,n):
 if n==1:return s.prod(xs[i] for i in word)
 N=len(word)
 if N==0:return 1
 if N==1:return xs[word[0]]
 out=s.prod(xs[i] for i in word)
 for a,b in itertools.combinations(range(N),2):out+=G[word[a],word[b]]*s.prod(xs[word[c]] for c in range(N) if c not in [a,b])
 if N>=3:
  for inds in itertools.combinations(range(N),3):out+=orient*s.LeviCivita(*[word[c] for c in inds])*s.prod(xs[word[c]] for c in range(N) if c not in inds)
 if N==4:
  i,j,k,l=word;out+=G[i,j]*G[k,l]-G[i,k]*G[j,l]+G[i,l]*G[j,k]
 return s.expand(out)
result={}
for n in [1,2]:
 if n==1:F=[2*y*z-(x-1)**2,2*z*x-(y-1)**2,2*x*y-z*z-2]
 else:F=[s.expand(gg**2*(2*xs[(i+1)%3]*xs[(i+2)%3]-xs[i]**2-[-2,-2,0][i]*xs[i]-[1,1,2][i])-2*Adj[(i+1)%3,(i+2)%3]+Adj[i,i]) for i in range(3)]
 I=s.groebner(F,x,y,z,domain=K);heads=[p.monoms()[0] for p in I.polys];basis=[]
 for deg in range(12):
  for a in range(deg+1):
   for b in range(deg-a+1):
    e=(a,b,deg-a-b)
    if not any(all(ei>=hi for ei,hi in zip(e,h)) for h in heads):basis.append(e)
 assert len(basis)==8
 idx={e:i for i,e in enumerate(basis)}
 def nf(expr):return I.reduce(expr)[1]
 def mat(expr):
  rows=[[zero]*8 for _ in range(8)]
  for j,e in enumerate(basis):
   p=s.Poly(nf(s.expand(expr*s.prod(v**i for v,i in zip(xs,e)))),x,y,z,domain=K)
   for exp,c in p.rep.to_dict().items():rows[idx[exp]][j]=c
  return DomainMatrix.from_dod({i:{j:c for j,c in enumerate(row) if c} for i,row in enumerate(rows)},(8,8),K)
 value=nf(s.expand(-sum(K.to_sympy(c)*tr(w,n) for w,c in cut)))
 print('representation',n,'central value reduced',flush=True)
 cp=mat(value).charpoly();poly=s.Poly.from_list([K.to_sympy(c) for c in cp],D,domain=K)
 # Separate the two off-axis center points at the unique off-axis value in this trace scheme.
 offpoly=s.Poly(terms_poly(next(t['factor'] for t in crit['off_axis_squarefree'] if t['multiplicity']==2)).subs(T,gg),D,domain=K)
 offgcd=poly.gcd(offpoly).monic();assert offgcd.degree()==1
 dval=-offgcd.all_coeffs()[1]
 offI=s.groebner(F+[value-dval],x,y,z,domain=K)
 offheads=[p.monoms()[0] for p in offI.polys];offbasis=[]
 for deg in range(10):
  for a in range(deg+1):
   for b in range(deg-a+1):
    e=(a,b,deg-a-b)
    if not any(all(ei>=hi for ei,hi in zip(e,h)) for h in offheads):offbasis.append(e)
 assert len(offbasis)==(2 if n==1 else 4)
 normal=json.load(open(root/'cubic_order4_symmetric_center_certificate.json'));centers=json.load(open(root/'cubic_order4_center_certificate.json'))['basis']
 zv=[]
 for zi in centers[:2]:
  expr=0
  for row in zi:
   coef=cv(s.sympify(row['coefficient']).subs({T:gg,D:dval},simultaneous=True))
   expr+=K.to_sympy(coef)*tr([i for i in row['word'] if i!=3],n)
  zv.append(offI.reduce(s.expand(expr))[1])
 rr=[s.sympify(q).subs(T,gg) for q in normal['roots']]
 shifts=[sum(s.sympify(q).subs(T,gg)*dval**j for j,q in enumerate(row)) for row in normal['shifts']]
 vv=offI.reduce(s.expand(rr[0]*zv[0]-rr[1]*zv[1]-shifts[0]+shifts[1]))[1]
 size=len(offbasis);oidx={e:i for i,e in enumerate(offbasis)};rows=[[zero]*size for _ in range(size)]
 for j,e in enumerate(offbasis):
  pp=s.Poly(offI.reduce(s.expand(vv*s.prod(q**i for q,i in zip(xs,e))))[1],x,y,z,domain=K)
  for exp,c in pp.rep.to_dict().items():rows[oidx[exp]][j]=c
 VV=DomainMatrix.from_dod({i:{j:c for j,c in enumerate(row) if c} for i,row in enumerate(rows)},(size,size),K)
 square=VV.matmul(VV).to_list();v2=square[0][0]
 assert v2 and all(square[i][j]==(v2 if i==j else zero) for i in range(size) for j in range(size))
 assert sum((rows[i][i] for i in range(size)),zero)==zero
 separation={'off_axis_D':txt(cv(dval)),'fiber_length':size,'v_square':txt(v2),'v_nonzero_square_and_zero_trace_verified':True,'simples_per_off_axis_center_point':size//2}
 print('PASS off-axis center separation dimension',n,flush=True)
 J=s.Matrix([[s.diff(f,v) for v in xs] for f in F])
 reduced=s.groebner(F+[J.det()],x,y,z,domain=K).contains(s.Integer(1))
 det_nonzero=s.groebner(F+[L.det()],x,y,z,domain=K).contains(s.Integer(1)) if n==2 else None
 result[str(n)]={'scheme_length':8,'off_axis_separation':separation,'reduced':reduced,'detL_everywhere_nonzero':det_nonzero,'value_polynomial':[txt(c) for c in cp],'scope':'Exact central-value norm of the character scheme / nondegenerate Pauli trace scheme'}
 print('PASS norm computed for dimension',n,'reduced',reduced,'detL nonzero',det_nonzero,flush=True)
from sympy.polys.rings import ring
R,dd=ring('D',K)
def rp(rows):return sum((R(cv(s.sympify(t['coefficient']).subs(T,gg)))*dd**t['D_power'] for t in rows),R.zero)
Ps=[]
for n in ['1','2']:
 coeff=result[n]['value_polynomial'];Ps.append(sum((R(cv(s.sympify(c).subs(T,gg)))*dd**(len(coeff)-1-i) for i,c in enumerate(coeff)),R.zero))
sy=next(rp(t['factor']) for t in crit['symmetric_squarefree'] if t['multiplicity']==2)
of=next(rp(t['factor']) for t in crit['off_axis_squarefree'] if t['multiplicity']==2)
ds=(4467*g**3-5311*g*g+6316*g-7511)/4
assert Ps[0]**2*Ps[1]==sy**2*of**4*(dd-R(ds))**4
assert Ps[0].gcd(Ps[1]).degree()==0
def sqf_degrees(p):
 p=p.monic();c=p.gcd(p.diff(dd));w=p.exquo(c);out=[];i=1
 while w.degree()>0:
  y=w.gcd(c);q=w.exquo(y)
  if q.degree()>0:out.append([q.degree(),i])
  w=y;c=c.exquo(y);i+=1
 return out
assert sqf_degrees(Ps[0])==[[3,1],[1,2],[1,3]]
assert sqf_degrees(Ps[1])==[[2,2],[1,4]]
result['norm_squarefree_degree_multiplicities']={str(i+1):sqf_degrees(p) for i,p in enumerate(Ps)}
result['norms_mutually_coprime']=True
result['combined_norm_identity_verified']=True
result['branch_gcd_degrees']={n:{branch:{str(t['multiplicity']):Ps[int(n)-1].gcd(rp(t['factor'])).degree() for t in crit[branch]} for branch in ['symmetric_squarefree','off_axis_squarefree']} for n in ['1','2']}
assert result['2']['reduced'] and result['2']['detL_everywhere_nonzero']
print('PASS exact combined character / two-dimensional trace norm identity',flush=True)
(root/'cubic_order4_small_rep_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
