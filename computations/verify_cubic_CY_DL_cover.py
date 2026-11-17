#!/usr/bin/env python3
"""All necessary D/L coefficient charts, no AS4 sufficiency imported.
New universal coefficient controls connect D to the old all-h exclusion.
"""
from pathlib import Path
import itertools,json,sympy as s
ROOT=Path(__file__).resolve().parent
a,b,c,d=s.symbols('a b c d');Y=[a,b,c,d];pairs=list(itertools.combinations(range(4),2));x=s.symbols('x:22');g=s.Symbol('g');K=s.zeros(16,6)
for j,(i,k) in enumerate(pairs):K[4*i+k,j]=1;K[4*k+i,j]=-1
J=s.zeros(6);J[0,5]=J[5,0]=1;J[1,4]=J[4,1]=-1;J[2,3]=J[3,2]=1
W=list(itertools.product(range(4),repeat=4))
def quad(q):
 p=s.Poly(s.expand(q),*Y);u=s.zeros(16,1)
 for i in range(4):
  u[5*i]=p.coeff_monomial(Y[i]**2)
  for j in range(i+1,4):u[4*i+j]=u[4*j+i]=p.coeff_monomial(Y[i]*Y[j])/2
 return u

def check_frame(qs,A,B,C0):
 U=s.Matrix.hstack(*map(quad,qs));H=U*A*U.T+U*B*K.T+K*B.T*U.T+K*(C0+g*J)*K.T
 assert all(s.expand(H[4*w[0]+w[1],4*w[2]+w[3]]+H[4*w[3]+w[0],4*w[1]+w[2]])==0 for w in W)
 assert s.Matrix(list(B)).jacobian(x).rank()==22
 columns=[]
 for i,j in itertools.product(range(6),repeat=2):
  M=U[:,i]*K[:,j].T+K[:,j]*U[:,i].T;columns.append(s.Matrix([M[4*w[0]+w[1],4*w[2]+w[3]]+M[4*w[3]+w[0],4*w[1]+w[2]] for w in W]))
 MC=s.Matrix.hstack(*columns);assert MC.rank()==14
 KK=[]
 for i,j in itertools.combinations_with_replacement(range(6),2):
  M=K[:,i]*K[:,j].T+(K[:,j]*K[:,i].T if i!=j else s.zeros(16));KK.append(s.Matrix([M[4*w[0]+w[1],4*w[2]+w[3]]+M[4*w[3]+w[0],4*w[1]+w[2]] for w in W]))
 CK=s.Matrix.hstack(*KK);assert CK.rank()==20 and MC.row_join(CK).rank()==34
 return U,(C0+g*J-B.T*A.inv()*B).applyfunc(s.expand),U+K*B.T*A.inv()
# D: full22-dimensional original mixed matrix.
qs=[a*a,a*b,b*b,c*c,c*d,d*d];A=s.zeros(6)
for i,j in [(0,2),(3,5)]:A[i,j]=A[j,i]=s.Rational(1,2)
A[1,1]=A[4,4]=-1
B=s.Matrix([[x[0],x[1],x[2],x[4]/2,x[5]/2,0],[x[3],x[4],x[5],2*x[7],2*x[8],0],[x[6],x[7],x[8],x[9],x[10],0],[0,x[11],x[14]/2,x[12],x[15]/2,x[13]],[0,x[14],2*x[17],x[15],2*x[19],x[16]],[0,x[17],x[18],x[19],x[20],x[21]]]);C0=s.diag(s.Rational(1,4),0,0,0,0,s.Rational(1,4));U,D,R=check_frame(qs,A,B,C0)
assert D[0,5]==g and s.expand(D[0,0]-x[3]**2+4*x[0]*x[6]-s.Rational(1,4))==0 and s.expand(D[5,5]-x[16]**2+4*x[13]*x[21]-s.Rational(1,4))==0
base={x[0]:0,x[6]:0,x[13]:0,x[21]:0,x[3]:s.I/2,x[16]:s.I/2,g:0};forced=[x[i] for i in [4,5,7,8,14,15,17,19]];DD=D.subs(base);coeff,rhs=s.linear_eq_to_matrix(list(DD[0,1:5])+list(DD[5,1:5]),forced);assert coeff.rank()==8 and rhs==s.zeros(8,1);base.update(dict.fromkeys(forced,0));DD=D.subs(base).applyfunc(s.expand)
eq=[x[1]*x[9],x[2]*x[10],x[11]*x[18],x[12]*x[20],x[1]*x[10]+x[11]*x[20],x[12]*x[18]+x[2]*x[9]];assert set(q for q in DD if q)==set(-2*q for q in eq)
for indices,col in [([9,10],0),([1,2],2),([18,20],3),([11,12],5)]:assert (R.subs(base).subs(dict.fromkeys([x[j] for j in indices],0))[:,col]-U[:,col]).applyfunc(s.expand)==s.zeros(16,1)
p,q,rr,z,r0,s0,t0,u0,h=s.symbols('p q rr z r0 s0 t0 u0 h',nonzero=True);di=s.diag(r0,s0,t0,u0);sc=s.diag(r0*r0,r0*s0,s0*s0,t0*t0,t0*u0,u0*u0);normals={}
for typ,ids in [('I',[1,10,11,20]),('II',[2,9,12,18])]:
 sub=dict.fromkeys(x,0);sub.update({x[3]:s.I/2,x[16]:s.I/2,g:0});sub.update(dict(zip([x[i] for i in ids],[p,q,rr,z])));RG=R.subs(sub)
 maps=[p*r0*t0/s0**2,q*s0*u0/r0**2,rr*r0*t0/u0**2,z*s0*u0/t0**2] if typ=='I' else [p*r0*u0/s0**2,q*s0*t0/r0**2,rr*s0*t0/u0**2,z*r0*u0/t0**2]
 assert (s.kronecker_product(di,di)*RG-RG.subs(dict(zip([p,q,rr,z],maps)),simultaneous=True)*sc).applyfunc(s.cancel)==s.zeros(16,6)
 rv,uv=s.symbols('rv uv',nonzero=True)
 if typ=='I':su={r0:rv,s0:1,t0:1/(p*rv),u0:uv,rr:p*uv**2,z:-q/uv**2};poly=rv**2-uv/p
 else:su={r0:rv,s0:1,u0:1/(p*rv),t0:1/(p*p*rv**2*rr),z:-p*q/rr};poly=rv**4-1/(p**3*rr)
 for val,target in zip(maps,[1,p*q,1,-p*q]):assert s.rem(s.cancel(val.subs(su,simultaneous=True)-target).as_numer_denom()[0],poly,rv)==0
 assert s.rem(s.cancel((r0*s0-t0*u0).subs(su,simultaneous=True)).as_numer_denom()[0],poly,rv)==0
 sub.update(dict(zip([x[i] for i in ids],[1,h,1,-h])));RN=R.subs(sub);assert D.subs(sub)==s.zeros(6);normals[typ]=str(RN)
 # Literal polynomial transport to the old all-h excluded presentation.
 def word(i,j):
  v=s.zeros(16,1);v[4*i+j]=1;return v
 def comm(i,j):return word(i,j)-word(j,i)
 E=[word(1,0)-s.I*word(0,1),word(3,2)-s.I*word(2,3)]
 if typ=='I':E += [word(0,0)+2*h*comm(1,3),word(1,1)+2*comm(0,2),word(2,2)-2*h*comm(1,3),word(3,3)+2*comm(0,2)]
 else:E += [word(0,0)+2*h*comm(1,2),word(1,1)+2*comm(0,3),word(2,2)-2*h*comm(0,3),word(3,3)+2*comm(1,2)]
 E=s.Matrix.hstack(*E);change=(U.T*U).inv()*U.T*E;assert (RN*change-E).applyfunc(s.expand)==s.zeros(16,6) and change.det()!=0 and h not in change.det().free_symbols
# L: full22-dimensional original mixed matrix and its all-rank action.
qs=[a*a,a*b,b*b,b*c,a*c-b*d,a*d];A=s.zeros(6)
for i,j,v in [(0,3,1),(1,4,-1),(2,5,-1)]:A[i,j]=A[j,i]=s.Rational(v,2)
B=s.Matrix([[x[0],x[1],x[2],(x[4]-x[14])/2,(x[5]-x[17])/2,-(x[18]+x[21])/2],[x[3],x[4],x[5],-x[11]+2*x[7],x[14]+2*x[8],x[16]-x[20]],[x[6],x[7],x[8],x[9],x[10],(x[13]+x[15])/2],[x[11],x[15],x[16],x[12],x[13],0],[x[14],-x[20],-x[21],x[15],x[16],0],[x[17],x[18],x[19],x[20],x[21],0]]);C0=s.zeros(6)
for i,j in [(0,1),(0,4)]:C0[i,j]=C0[j,i]=s.Rational(1,8)
U,D,R=check_frame(qs,A,B,C0);v=B[:3,5];assert s.expand(D[1,5]+D[4,5]-2*(v[1]**2-4*v[0]*v[2]))==0
T=s.Matrix(2,2,s.symbols('t:4'));det=T.det();E=s.diag(T,T.inv().T);EE=s.kronecker_product(E,E);SU=((U.T*U).inv()*U.T*EE*U).applyfunc(s.cancel);SK=((K.T*K).inv()*K.T*EE*K).applyfunc(s.cancel);assert (EE*U-U*SU).applyfunc(s.cancel)==s.zeros(16,6) and (SU*A*SU.T-det*A).applyfunc(s.cancel)==s.zeros(6);BT=SU*B*SK.T/det;assert (BT[:,5]-SU*B[:,5]/det**2).applyfunc(s.cancel)==s.zeros(6,1)
zero={x[18]:-x[21],x[16]:x[20],x[13]:-x[15]};assert R.subs(zero).extract([10,11,14,15],range(6))==s.zeros(4,6)
norm={x[18]:-2-x[21],x[16]:x[20],x[13]:-x[15]};DD=D.subs(norm).applyfunc(s.expand);assert DD[:,5]==s.Matrix([g-2*x[11],-2*x[15],-2*x[20],-2*x[12],2*x[15],0]);norm.update({x[12]:0,x[13]:0,x[15]:0,x[16]:0,x[20]:0,g:2*x[11]});DD=D.subs(norm).applyfunc(s.expand);z=x[21];uu=x[7];ww=x[10];pp=x[11]
assert s.expand(DD[1,3]+DD[3,4]+4*x[9])==0
assert s.expand(DD[1,1]+4*(z+2)*uu)==0 and s.expand(DD[4,4]-4*z*ww)==0
assert s.expand(DD[1,4]+2*(pp-z*uu+(z+2)*ww))==0
assert s.expand(DD[2,3]-2*(pp*(z+1)-2*z*uu)-2*x[19]*x[9])==0
e1=z*ww;e2=(z+2)*uu;e3=pp-z*uu+(z+2)*ww;e4=pp*(z+1)-2*z*uu;combo=s.expand(e4-(z+1)*e3-(z-3)*e2+(z+3)*e1);assert combo==6*uu-2*ww and s.expand(z*combo+2*e1-6*e2)==-12*uu
assert (R.subs(norm)[:,0]-quad(a*a)-2*pp*K[:,0]).applyfunc(s.expand)==s.zeros(16,1)
out={'status':'PASS','scope':'full necessary D coefficient cover by the two previously excluded families; complete L projection exclusion','D_normal_relations':normals,'D_full_mixed_dimension':22,'D_internal_SL2_discriminants':'both -1/4, no zero values','D_all_supports':'four nonzero coefficient pairs force exactly I or II by six explicit binomials','D_all_nonzero_normalization':'auxiliary roots rv2=uv/p or rv4=1/(p3 rr), preserving r0s0=t0u0','L_full_mixed_dimension':22,'D_old_presentation_transport':'all polynomial identities and constant invertible relation basis, for every h','L_all_GL2_covariance':True,'L_rank0_obstruction':'free two-generator quotient','L_rank1_obstruction':'all-parameter polynomial identities force actual a2 relation','ordinary_dependencies':['all rank6 marked relation normalizations from prior seven-projection theorem','SL2 transitivity on fixed nonzero binary discriminants','domain support exclusions and integral-field nonzero root choices','existing theorem thm:as4-double-cover-h3-exclusion handles all nonzero h'],'not_claimed':['AS4 existence sufficiency imported','all finite-base CY projection types excluded','full CY or H3 classification','novelty confirmed']}
(ROOT/'cubic_CY_DL_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS all necessary22+22 coefficient directions, full D normalizations and L complete exclusion')
