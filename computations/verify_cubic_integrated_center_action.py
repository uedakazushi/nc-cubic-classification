#!/usr/bin/env python3
"""Executable degree3 center-value arrow algorithm, with three exact controls.
Reruns all-parameter envelope identities. The D controls are explicitly finite
witnesses, not a replacement for the ordinary all-parameter center-basis proof.
"""
import runpy
from pathlib import Path
root=Path(__file__).parent;output_path=root/'cubic_integrated_center_action_certificate.json'
v=runpy.run_path(str(root/'verify_cubic_integrated_arrows.py'));globals().update({k:value for k,value in v.items() if not k.startswith('__')})
from sympy.polys.matrices import DomainMatrix
from itertools import product
source_certificate=json.loads((root/'cubic_clifford_integration_certificate.json').read_text())
# Work over QQ(zeta3) at an exact rational parameter point.
point={syms[0]:1,syms[1]:s.Rational(1,2),syms[2]:1,syms[3]:2,syms[4]:3,syms[5]:-1,syms[6]:2,syms[7]:3}
def ev(x):return K.from_sympy(F.to_sympy(x).subs(point,simultaneous=True))
def kexpr(x):return K.to_sympy(x)
def gamma_cut(H,G,a,beta,D):
 subs={'h':kexpr(H),'z':kexpr(G),'A':kexpr(a[0]),'B':kexpr(a[1]),'C':kexpr(a[2]),
       'beta_x':kexpr(beta[0]),'beta_y':kexpr(beta[1]),'beta_z':kexpr(beta[2]),'D':kexpr(D)}
 return {tuple(row['active_word']):K.from_sympy(s.sympify(row['coefficient']).subs(subs,simultaneous=True)) for row in source_certificate['integrated_cut_coefficients']}
def nc_mul(P,Q):
 out={}
 for u,c in P.items():
  for w,d in Q.items():out[u+w]=out.get(u+w,K.zero)+c*d
 return {w:c for w,c in out.items() if c}
def transform(poly,M,shift):
 Y=[{(j,):M[3*i+j] for j in range(3) if M[3*i+j]} for i in range(3)]
 for i in range(3):Y[i][()]=shift[i]
 out={}
 for word,c in poly.items():
  term={():c}
  for i in word:term=nc_mul(term,Y[i])
  for w,d in term.items():out[w]=out.get(w,K.zero)+d
 return out
def project_degree3(H,G,a,beta):
 ws=[w for n in range(3,-1,-1) for w in product(range(3),repeat=n)];ix={w:i for i,w in enumerate(ws)}
 rels=[{(j,k):K.one+G,(k,j):K.one-G,(i,i):-H,(i,):4*G*a[i],():-beta[i]} for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]]
 cols=[]
 for d in range(2):
  for dl in range(d+1):
   for l in product(range(3),repeat=dl):
    for r in product(range(3),repeat=d-dl):
     for rel in rels:cols.append({ix[l+w+r]:s0 for w,s0 in rel.items()})
 mat=s.MutableSparseMatrix(40,21,{(i,j):kexpr(c) for j,col in enumerate(cols) for i,c in col.items()});rr,piv=DomainMatrix.from_Matrix(mat.T).convert_to(K).rref();rr=rr.to_Matrix();free=[j for j in range(40) if j not in piv]
 P=s.zeros(20,40)
 for i,j in enumerate(free):P[i,j]=1
 for i,j in enumerate(piv):
  for k,l in enumerate(free):P[k,j]=-rr[i,l]
 def projection(poly):
  vec=s.zeros(40,1)
  for w,c in poly.items():vec[ix[w]]+=kexpr(c)
  return DomainMatrix.from_Matrix(P*vec).convert_to(K).to_Matrix()
 return projection
controls=[];source=(K.one,K.from_sympy(s.Rational(1,2)),tuple(map(K.convert,[1,2,3])),tuple(map(K.convert,[-1,2,3])))
for i,M0 in enumerate(gens):
 target=data(M0,*base);H,G,a,beta,shift,c=target
 H,G=ev(H),ev(G);a=tuple(map(ev,a));beta=tuple(map(ev,beta));shift=tuple(map(ev,shift));M=tuple(map(ev,M0))
 src=gamma_cut(*source,K.convert(5));mapped=transform(src,M,shift);dst=gamma_cut(H,G,a,beta,K.zero);pr=project_degree3(H,G,a,beta)
 Z=pr(dst).row_join(pr({():K.one}));rhs=pr(mapped)
 _,rows=DomainMatrix.from_Matrix(Z.T).convert_to(K).rref();assert len(rows)==2
 coeff=DomainMatrix.from_Matrix(Z[list(rows),:]).convert_to(K).inv()*DomainMatrix.from_Matrix(rhs[list(rows),:]).convert_to(K)
 residual=DomainMatrix.from_Matrix(Z).convert_to(K)*coeff-DomainMatrix.from_Matrix(rhs).convert_to(K);assert residual.is_zero_matrix
 u,d0=coeff.to_Matrix();assert K.from_sympy(u)
 controls.append({'generator':i,'u':str(u),'D_prime_for_D5':str(K.to_sympy(K.from_sympy(d0/u)))})
certificate={'version':'classification-v13','center_action_algorithm':'Project transformed source G to degree3 target quotient; uniquely solve [G_target(D=0),t^3]*(u,d)=phi(G_source); Dprime=d/u',
 'finite_exact_controls':controls,'control_field':'QQ(zeta3)','control_source':'h1,gamma1/2,a=(1,2,3),beta=(-1,2,3),D5',
 'universal_envelope_checks_rerun':True,'scope':'Three exact controls of a general finite linear algorithm; universality/completeness of D arrows is the ordinary center-basis proof, not finite extrapolation. No H3 admissibility of control D values asserted.'}
output_path.write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS: universal envelope action rerun; degree3 center-value arrow algorithm on all3 exact Hessian controls; unique quotient identity checked')
