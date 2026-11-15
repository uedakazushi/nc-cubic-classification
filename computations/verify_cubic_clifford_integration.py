#!/usr/bin/env python3
"""Rains E6 central formula, universal relation identities and Clifford integration.
Primary formula: https://math.mit.edu/~etingof/delpezzocenter (E6 only).
Independent verification uses all-parameter identities over QQ(h,gamma,alpha,beta).
No finite interpolation, H3 smoothness, all-AS4 coverage or descent assertion.
"""
import sympy as s
from sympy.polys.matrices import DomainMatrix
from itertools import product
from pathlib import Path
import json
h,z=s.symbols('h z');aa=list(s.symbols('alpha_x alpha_y alpha_z'));bb=list(s.symbols('beta_x beta_y beta_z'));K=s.QQ.frac_field(h,z)
words=lambda n:[w for d in range(n,-1,-1) for w in product(range(3),repeat=d)]
def mat(rs,n):
 ws=words(n);ix={w:i for i,w in enumerate(ws)};cols=[]
 for d in range(n-1):
  for dl in range(d+1):
   for l in product(range(3),repeat=dl):
    for r in product(range(3),repeat=d-dl):
     for q in rs:cols.append({ix[l+w+r]:c for w,c in q.items() if c})
 return s.MutableSparseMatrix(len(ws),len(cols),{(i,j):c for j,col in enumerate(cols) for i,c in col.items()})
rels=[];full=[]
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
 q={(j,k):1+z,(k,j):1-z,(i,i):-h};rels.append(q);full.append({**q,(i,):-aa[i],():-bb[i]})
M0=mat(rels,4);M=mat(full,4);ws=words(4);ix={w:i for i,w in enumerate(ws)}
# Select a chart from the Clifford point, not a gamma-generic chart singular there.
_,pc=DomainMatrix.from_Matrix(M0.subs(z,0)).convert_to(s.QQ.frac_field(h)).rref();N0=M0[:,list(pc)];N=M[:,list(pc)]
_,rows=DomainMatrix.from_Matrix(N0.T.subs(z,0)).convert_to(s.QQ.frac_field(h)).rref();free=[i for i in range(121) if i not in rows]
assert len(pc)==86
L0=DomainMatrix.from_Matrix(N0[list(rows),:]).convert_to(K).inv().to_Matrix()

Delta=N-N0;W=L0*Delta[list(rows),:]
# Verify only three central commutators, rather than invert a large multivariate matrix.
q,t,a1,b1,c1,a2,b2,c2=s.symbols('q tau a1 b1 c1 a2 b2 c2')
# Polynomial normalization t^2*(q+1)*(t^3+1) of Rains' author-hosted MAGMA formula.
G={(1,1,1):t*t*(q+1)*(t**3+1),(1,2,0):t*(q+1)*(q**3-t**3),(2,1,0):-q*t*(q+1)*(t**3+1),(2,2,2):t*t*(q+1)*(q**3-t**3),
(1,0):q*(q+1)*t**3*c1,(1,1):-t*(q*q+q*t**3+q+2*t**3+1)*b1,(1,2):(-q*q+q*t**3)*a1,(2,0):t**3*(q+1)*b1,(2,1):(q**3+q*t**3)*a1,(2,2):t*(-q**4-q**3-q*q+2*q*t**3+t**3)*c1,
(0,):-(q**3*t*a2+2*q*q*t*a2+q*q*a1*a1+q*t*t*b1*c1+q*t*a2),
(1,):t*(-q**3*b2-2*q*q*b2-q*t**3*b2-q*t*a1*c1-2*q*b2-t**3*b2+t*t*b1*b1-b2),
(2,):t*(-q**4*c2-2*q**3*c2-2*q*q*c2+q*t**3*c2-q*t*t*c1*c1-q*t*a1*b1-q*c2+t**3*c2)}

subs={q:-(1-z)/(1+z),t:h/(1+z),a1:-aa[0]/(1+z),b1:-aa[1]/(1+z),c1:-aa[2]/(1+z),a2:-bb[0]/(1+z),b2:-bb[1]/(1+z),c2:-bb[2]/(1+z)}
gp={w:s.cancel(c.subs(subs,simultaneous=True)) for w,c in G.items()}
certs=[]
for x in range(3):
 v=s.zeros(121,1)
 for w,c in gp.items():v[ix[w+(x,)]]+=c;v[ix[(x,)+w]]-=c
 term=(L0*v[list(rows),:]).applyfunc(s.cancel);c=term
 for j in range(1,5):
  term=(-W*term).applyfunc(s.cancel);c+=term
 c=c.applyfunc(s.cancel)
 assert (N*c-v).applyfunc(s.cancel)==s.zeros(121,1)
 certs.append(c)
 print('central commutator verified',x,flush=True)
print('ALL-PARAMETER RAINS CENTRAL IDENTITY VERIFIED',flush=True)

A,B,C,D=s.symbols('A B C D');beta_x,beta_y,beta_z=bb;d=1+h**3
replacement={aa[0]:-4*z*A,aa[1]:-4*z*B,aa[2]:-4*z*C}
integrated={w:s.cancel(c.subs(replacement)/(-4*h*d*z)) for w,c in gp.items()}
integrated[()]=D-A*beta_x/h
# The relation certificates also divide by gamma after this substitution;
# their denominators are units on the complete good Clifford base gamma=0.
def good_denominator(q):
    den=s.denom(s.cancel(q))
    assert den.free_symbols <= {h,z}
    boundary=s.factor(den.subs(z,0));assert boundary!=0
    return all(s.rem(h*(1+h**3),factor,h)==0 for factor,power in s.factor_list(boundary,h)[1])
assert all(good_denominator(q) for q in integrated.values())
for c in certs:
    assert all(good_denominator(q.subs(replacement)/(-4*h*d*z)) for q in c)
# At gamma=0, reduce the limit against the complete Clifford relation ideal.
ws3=words(3);ix3={w:i for i,w in enumerate(ws3)}
base=[{(j,k):1,(k,j):1,(i,i):-h,():-bb[i]} for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]]
M3=mat(base,3)
rr,piv=DomainMatrix.from_Matrix(M3.T).convert_to(s.QQ.frac_field(h,*bb)).rref();rr=rr.to_Matrix();free3=[j for j in range(40) if j not in piv]
P3=s.zeros(20,40)
for i,j in enumerate(free3):P3[i,j]=1
for i,j in enumerate(piv):
    for k,l in enumerate(free3):P3[k,j]=-rr[i,l]
expected={(0,1,2):1,(2,2,2):-h/2,(1,1,1):h/2,(0,0,0):-h/2,
          (2,):-bb[2]/2,(1,):bb[1]/2,(0,):-bb[0]/2,
          (0,0):A,(1,1):B,(2,2):C,():D}
difference=s.zeros(40,1)
for w,c in integrated.items():difference[ix3[w]]+=s.cancel(c.subs(z,0))
for w,c in expected.items():difference[ix3[w]]-=c
assert (P3*difference).applyfunc(s.cancel)==s.zeros(20,1)
certificate={'version':'classification-v11',
    'primary_formula_url':'https://math.mit.edu/~etingof/delpezzocenter',
    'paper':'Etingof–Ginzburg, arXiv:0709.3593, Theorem3.3.2 and Appendix9.1; author-hosted E6 formula used',
    'relations':'(1+gamma)yz+(1-gamma)zy=h*x^2+alpha_x*t*x+beta_x*t^2, cyclic; central t',
    'all_parameter_commutator_relation_identities':3,
    'relation_matrix':[121,102], 'selected_independent_relations':86,
    'polynomial_normalization_of_author_formula':'tau^2*(q+1)*(tau^3+1)',
    'conversion':{'q':'-(1-gamma)/(1+gamma)','tau':'h/(1+gamma)','a1,b1,c1':'-alpha/(1+gamma)','a2,b2,c2':'-beta/(1+gamma)'},
    'integrated_envelope':'alpha=-4*gamma*(A,B,C)',
    'integrated_central_cut':'Omega/(-4*h*(1+h^3)*gamma)+(D-A*beta_x/h)*t^3',
    'coefficient_limit':'g_beta+t*(A*x^2+B*y^2+C*z^2)+D*t^3',
    'all_certificate_denominators_regular_at_gamma0':True,
    'integrated_cut_coefficients':[{'active_word':list(w),'t_power':3-len(w),'coefficient':str(s.factor(c))} for w,c in integrated.items() if c],
    'scope':'Actual rational central presentations near gamma=0 and all-order formal central integration of every Clifford cut. Not full graded flatness/AS4 of the entire presentation family, H3 openness or recognition, all-AS4 coverage, a moduli component or relative stack descent.'}
Path(__file__).with_name('cubic_clifford_integration_certificate.json').write_text(json.dumps(certificate,indent=2,ensure_ascii=False)+'\n')
print('PASS: Rains central formula independently verified; all Clifford cuts integrate to all orders as central presentations; denominators regular over entire good gamma0 base; exact prescribed limit',flush=True)
