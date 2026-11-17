#!/usr/bin/env python3
"""All original four-point CY frames and all4096 directed shared supports."""
from pathlib import Path
from itertools import product,combinations,permutations
from collections import Counter
import json,sympy as s
pairs=list(combinations(range(4),2));U=s.zeros(16,6);K=s.zeros(16,6)
for j,(i,k) in enumerate(pairs):U[4*i+k,j]=U[4*k+i,j]=s.Rational(1,2);K[4*i+k,j]=1;K[4*k+i,j]=-1
la,g=s.symbols('lambda g');x=s.symbols('x0:21');z=s.symbols('z0:6')
def AA(l):return s.hessian(z[0]*z[5]+l*z[1]*z[4]-(1+l)*z[2]*z[3],z)/2
def CC(l):
 C=s.zeros(6);C[1,4]=C[4,1]=(l+1)/8;C[2,3]=C[3,2]=-l/8;return C
A=AA(la);C=CC(la);J=s.zeros(6)
for i,j,v in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=v
B=s.Matrix([[x[0],x[1],x[3],-x[6],-x[10],-x[11]+x[8]],
[x[1],x[2],x[4],x[7],-x[15]+x[8],-x[16]],
[x[3],x[4],x[5],x[11]-x[15],x[12],x[17]],
[x[6],x[7],x[8],x[9],x[13],-x[18]],
[x[10],x[11],x[12],x[13],x[14],x[19]],
[x[15],x[16],x[17],x[18],x[19],x[20]]])
ws=list(product(range(4),repeat=4))
def cyclic(H):return s.Matrix([H[4*a+b,4*c+d]+H[4*d+a,4*b+c] for a,b,c,d in ws])
H=U*A*U.T+U*B*K.T+K*B.T*U.T+K*(C+g*J)*K.T
assert cyclic(H).applyfunc(s.expand)==s.zeros(256,1)
assert s.Matrix(list(B)).jacobian(x).rank()==21
mixed=s.Matrix.hstack(*[cyclic(U[:,i]*K[:,j].T+K[:,j]*U[:,i].T) for i,j in product(range(6),repeat=2)])
assert mixed.rank()==15
kk=s.Matrix.hstack(*[cyclic(K[:,i]*K[:,j].T+(K[:,j]*K[:,i].T if i!=j else s.zeros(16))) for i in range(6) for j in range(i,6)])
assert kk.rank()==20
assert s.Matrix.hstack(mixed,kk).rank()==35
# Every coefficient is a shared directed edge, as determined by its diagonal weight.
edge_coeff={(0,1):4,(0,2):3,(0,3):1,(1,0):13,(1,2):10,(1,3):6,(2,0):18,(2,1):16,(2,3):7,(3,0):19,(3,1):17,(3,2):12}
edges=list(edge_coeff);ix={e:k for k,e in enumerate(edges)}
positions={j:next((r,c) for r,c in product(range(6),repeat=2) if B[r,c]==x[j]) for j in edge_coeff.values()}
lu=(U.T*U).inv()*U.T;lk=(K.T*K).inv()*K.T;ps=list(permutations(range(4)));actions=[]
for p in ps:
 P=s.zeros(4)
 for i in range(4):P[p[i],i]=1
 PP=s.kronecker_product(P,P);SS=lu*PP*U;KK=lk*PP*K;Ap=SS*A*SS.T;scale=2*Ap[0,5];lp=s.cancel(2*Ap[1,4]/scale)
 assert scale!=0 and (Ap/scale-AA(lp)).applyfunc(s.cancel)==s.zeros(6)
 Bp=(SS*B*KK.T/scale).applyfunc(s.cancel)
 all_positions={j:next((r,c) for r,c in product(range(6),repeat=2) if B[r,c]==x[j]) for j in range(21)}
 images={x[j]:Bp[r,c] for j,(r,c) in all_positions.items()}
 assert (B.subs(images,simultaneous=True)-Bp).applyfunc(s.cancel)==s.zeros(6)
 delta=(KK*C*KK.T/scale-CC(lp)).applyfunc(s.cancel);shift=s.cancel(delta[0,5]);factor=s.cancel((KK*J*KK.T)[0,5]/scale)
 assert (delta-shift*J).applyfunc(s.cancel)==s.zeros(6)
 assert (KK*J*KK.T/scale-factor*J).applyfunc(s.cancel)==s.zeros(6)

 edge_ratios=[]
 for (i,j),old in edge_coeff.items():
  new=edge_coeff[p[i],p[j]];expr=Bp[positions[new][0],positions[new][1]];ratio=s.cancel(expr/x[old]);assert not (set(x)&ratio.free_symbols)
  num,den=ratio.as_numer_denom()
  for poly in [num,den]:
   poly=s.Poly(poly,la)
   for factor in [s.Poly(la,la),s.Poly(la+1,la)]:
    while poly.degree()>0 and poly.rem(factor).is_zero:poly=poly.exquo(factor)
   assert poly.degree()==0
  edge_ratios.append(str(ratio))
 actions.append({'permutation':p,'lambda':str(lp),'scale':str(scale),'g_affine_shift':str(shift),'g_multiplier':str(factor),'shared_edge_units':edge_ratios})
# All diagonal torus weights, with a fourth-power common scale from the marking.
d=s.symbols('d0:4',nonzero=True);P=s.diag(*d);PP=s.kronecker_product(P,P);SS=lu*PP*U;KK=lk*PP*K;Bp=SS*B*KK.T/s.prod(d)
for (i,j),k in edge_coeff.items():r,c=positions[k];assert s.cancel(Bp[r,c]/x[k]-d[i]/d[j])==0

def action(mask,p):return sum(1<<ix[p[i],p[j]] for k,(i,j) in enumerate(edges) if mask>>k&1)
def typ(mask):
 deg=[sum(mask>>ix[i,j]&1 for j in range(4) if i!=j) for i in range(4)]
 if not mask:return 'zero'
 if 1 in deg:return 'degree1'
 if 2 in deg:return 'degree2'
 return 'partial_active' if 0 in deg else 'full'
seen=set();orbits=[];counts=Counter()
for mask in range(4096):
 kind=typ(mask);counts[kind]+=1
 if kind in ['degree1','degree2']:
  desired={(0,3)} if kind=='degree1' else {(0,1),(0,3)}
  assert any({(0,j) for j in range(1,4) if action(mask,p)>>ix[0,j]&1}==desired for p in ps)
 if mask not in seen:
  orb={action(mask,p) for p in ps};assert all(typ(m)==kind for m in orb);seen|=orb;orbits.append({'representative':mask,'type':kind,'size':len(orb)})
assert len(seen)==4096 and len(orbits)==218
assert counts=={'zero':1,'degree1':3471,'degree2':609,'partial_active':14,'full':1}
out={'status':'PASS','scope':'complete original CY four-point frame and shared-support reduction only; no algebra coefficient chart or H3 admissibility imported','mixed_cyclic_rank':15,'KK_cyclic_rank':20,'joint_rank':35,'all24_marked_actions':actions,'support_counts':dict(counts),'orbit_counts':dict(Counter(o['type'] for o in orbits)),'all218_support_orbits':orbits,'not_claimed':['all degree1/2 coefficient charts audited','partial active supports excluded','full shared singular supports excluded','complete CYc0 classification','complete H3 classification','novelty confirmed']}
Path(__file__).with_name('cubic_CY_four_point_support_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS original21+1 affine CY frame, all24 marked actions/diagonal weights, all4096 supports/218 orbits')
