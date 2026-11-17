#!/usr/bin/env python3
"""Last order4 rank: exhaustive middle/domain cover, two all-value Ore curves,
18 exact fresh coefficient points; ordinary proof in accompanying paper.
"""
from pathlib import Path
import sympy as s,itertools,json
from sympy.polys.matrices import DomainMatrix
from cubic_four_simple_order4_model import top,rels,analyze
F=s.QQ_I;i=F.from_sympy(s.I);u,v,B,C,D,L,A,h,k,E,rho=s.symbols('u v B C D L A h k E rho');vars=[u,v,B,C,D,L,A,h,k,E,rho];K=F.frac_field(*vars);ik=K.convert(i,F)
groups={j:[4*a+b for a in range(4) for b in range(4) if ([0,2,1,3][a]+[0,2,1,3][b])%4==j] for j in range(4)}
def get(co):
 cc=[K.zero]*16
 for j,e in co.items():cc[j]=K.from_sympy(s.sympify(e))
 H=top(K,ik,cc).to_Matrix();return H.extract(groups[0],groups[0]),H.extract(groups[1],groups[3])
H0,M=get({1:u,2:v,10:L,11:B,12:C,15:D,5:A,6:h,8:k,13:E})
assert H0==s.Matrix([[0,0,u,v],[0,L,B,C],[u,B,D,0],[v,C,0,-s.I*D]])
Z=H0.subs({u:0,v:0,D:0});assert list(Z[:,2])==[0,B,0,0] and list(Z[:,3])==[0,C,0,0]
MM=M.subs({u:0,v:0});assert s.expand(MM.extract([0,1,2],[0,2,3]).det())==-A*A*C
# If A=h=0, image is span(yc,cy); if exactly one nonzero, row0 is pure product.
assert MM.subs({A:0,h:0})[0,:]==s.zeros(1,4) and MM.subs({A:0,h:0})[2,:]==s.zeros(1,4)
# Nonzero first column implies u,v both nonzero; normalize u=1,v=rho.
N=H0.subs({u:1,v:rho});order=[0,2,1,3];N=N.extract(order,order);Z=(N[2:,2:]-N[2:,:2]*N[:2,:2].inv()*N[:2,2:]).applyfunc(s.cancel)
assert all(not s.expand(c0) for c0 in Z-s.Matrix([[L,C-B*rho],[C-B*rho,D*(rho*rho-s.I)]]))
MM=M.subs({u:1,v:rho,L:0,C:rho*B})
assert s.expand(MM.subs(B,0).extract([0,1,3],[1,2,3]).det())==E*E
# If E or k vanish, row1 gives a pure product or both rows1/3 vanish.
assert MM.subs({B:0,E:0,k:0})[1,:]==s.zeros(1,4) and MM.subs({B:0,E:0,k:0})[3,:]==s.zeros(1,4)
# Normalize B=1 by x/y scaling; exact rank2 residuals with unit rho pivot.
M1=MM.subs(B,1);pivot=M1.extract([0,1],[2,3]);assert pivot.det()==rho
res=[]
for row in [2,3]:res.extend(list((M1[row,:]-M1[row,2:4]*pivot.inv()*M1[[0,1],:]).applyfunc(s.cancel))[:2])
f=[h*k+rho*A*A-s.I*rho*rho,h*(E+rho*A),k*(E-rho*A),rho*h*k-E*E+s.I*rho]
assert all(not s.cancel(x-y) for x,y in zip(res,[-f[0]/rho,-f[1]/rho,f[2]/rho,-f[3]/rho]))
# Exact all-value model identity on two h=k=D0 curves; coefficients have no t denominators beyond Laurent units.
ts=s.Symbol('t');T=F.frac_field(ts);t=T.gens[0];it=T.convert(i,F);one,zero=T.one,T.zero
curve=[]
for eps in [1,-1]:
 co=[zero]*16
 for j,c0 in {1:one,2:-it*t*t,11:one,12:-it*t*t,5:t,13:eps*t}.items():co[j]=c0
 HH=top(T,it,co)
 rs=[{(2,3):one,(3,2):-it*t*t},{(0,0):one,(1,1):one},{(0,2):one,(2,0):t},{(1,3):one,(3,1):eps/t},{(3,0):one,(0,3):-t},{(2,1):one,(1,2):eps/t}]
 RM=DomainMatrix.from_dod({n:{j:r.get(divmod(n,4),zero) for j,r in enumerate(rs) if r.get(divmod(n,4),zero)} for n in range(16)},(16,6),T).to_dense();leads=[11,0,2,7,12,9];small=RM.extract(leads,range(6));assert not(small.det()-one)
 coords=small.inv().matmul(HH.extract(leads,range(16)));assert not any((RM.matmul(coords)-HH).to_list_flat())
 assert all(not c or len(c.denom.terms())==1 for c in coords.to_list_flat())
 # Both normal-generator eigenconditions on all five fixed cubic basis lines.
 # Basis x3,yxy,xbc,yb2,yc2; pure U entries identical.
 eb=[-t**-3,-t**-3,-it*t,-eps/t,eps*t**3];ec=[t**3,t**3,-it/t,eps/t**3,-eps*t]
 pairs=[]
 for b0,c0 in zip(eb,ec):
  p0=(b0-it).numer;p1=(c0+it).numer;assert p0.gcd(p1).is_ground;pairs.append([str(p0),str(p1)])
 curve.append({'eps':eps,'normal_b_c_equation_numerators':pairs,'all_five_gcds':'nonzero constants'})
# All18 isolated orbits, at all conjugate roots of X8+1 (irreducible).
z=s.Symbol('z');Lfield=s.QQ.alg_field_from_poly(s.Poly(z**8+1,z));zz=Lfield.unit;ii=zz**4;one,zero=Lfield.one,Lfield.zero
cases=[]
for rv in [ii,-ii]:cases.append((rv,zero,zero,one,-ii,zero,'both'))
for rv in [one,-one]:
 for av in [zz**j for j in range(16) if not(zz**(2*j)-ii*rv)]:
  cases.append((rv,av,-rv*av,one,zero,zero,'h'))
  cases.append((rv,av,rv*av,zero,one,zero,'k'))
for av in [zz**j for j in range(16) if not(zz**(4*j)+ii)]:
 for ep in [1,-1]:cases.append((-ii*av*av,av,ep*av,zero,zero,one,'D'))
assert len(cases)==18
fresh=[]
for rv,av,ev,hv,kv,dv,label in cases:
 assert not(hv*kv+rv*av*av-ii*rv*rv) and not(hv*(ev+rv*av)) and not(kv*(ev-rv*av)) and not(rv*hv*kv-ev*ev+ii*rv) and not(dv*(rv*rv-ii))
 co=[zero]*16
 for j,c0 in {1:one,2:rv,11:one,12:rv,15:dv,5:av,6:hv,8:kv,13:ev}.items():co[j]=c0
 HH=top(Lfield,ii,co);assert HH.rank()==6
 rr=analyze(Lfield,ii,rels(HH),finite=True);assert rr['dimensions']==[1,4,10,20,35] and rr['normal_kernel']==0 and len(rr['normal_pivots'])==5
 fresh.append({'label':label,'rho_A_E_h_k_D_power_basis':[list(map(str,c0.to_list())) for c0 in [rv,av,ev,hv,kv,dv]],'normal_shape':list(rr['normal_shape']),'normal_kernel':0})
out={'status':'PASS','scope':'whole final rank(2,0,2,2) excluded; with previous two ranks whole order4 spectrum empty by paper proof','zero_first_column':'pure-square H0 and nonzero 3minor A²C contradiction','nonzero_first_column':'u=v nonzero individually, normalize u1, rho=v; H0 rank2 gives L0,C=rho B,D(rho²-i)0','Bzero':'domain forces E,k nonzero but rank2 has 3minor E²','Bnonzero':'normalize B1; full rank2 system four displayed polynomials','rank2_equations':list(map(str,f)),'source_curves':curve,'finite_field':'QQ[z]/(z8+1), i=z4','fresh_all18':fresh,'conclusion':'no H3 with Nakayama eigenvalue set {1,-1,i,-i}; entire specified detminus1 spectral chart excluded','not_claimed':['all determinant-minus-one spectra covered by this chart','all four-simple or CY classification','complete H3 classification','ordinary proofs fully mechanically checked']}
Path(__file__).with_name('cubic_four_simple_order4_rankB_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS final rankB full cover, all-value normalizer curves and all18 fresh points')
