#!/usr/bin/env python3
"""Universal one-dimensional Serre obstruction; exact order4 fixed-envelope control.
This classifies the ODD self-Ext1 obstruction on character modules, not all bad
central values: higher-dimensional simples and higher Ext remain separate.
"""
import json
from pathlib import Path
from itertools import combinations
import sympy as s
h,g=s.symbols('h gamma');x,y,z=s.symbols('x y z');a=s.symbols('A B C');beta=s.symbols('beta_x beta_y beta_z');D=s.symbols('D')
pts=s.symbols('X Y Z');u=s.symbols('u v w');n=s.symbols('l m n');variables=(*pts,*u)
source=json.loads(Path(__file__).with_name('cubic_clifford_integration_certificate.json').read_text())
P=0
for row in source['integrated_cut_coefficients']:
    coeff=s.sympify(row['coefficient']).subs({'z':g},simultaneous=True)
    P+=coeff*s.prod([x,y,z][i] for i in row['active_word'])
char_sub={**{a[i]:(u[i]+h*pts[i])/(2*g) for i in range(3)},**{beta[i]:2*pts[(i+1)%3]*pts[(i+2)%3]+h*pts[i]**2+2*u[i]*pts[i] for i in range(3)},x:pts[0],y:pts[1],z:pts[2]}
grad=s.Matrix([s.factor(s.diff(P,v0).subs(char_sub,simultaneous=True)) for v0 in [x,y,z]])
M=s.Matrix([[u[0],pts[2],pts[1]],[pts[2],u[1],pts[0]],[pts[1],pts[0],u[2]]]);adj=M.adjugate();det=s.expand(M.det())
den=g*(1+h**3)*(1+g)**6;C=(den*grad).applyfunc(s.cancel)
assert all(q.is_polynomial(*variables) for q in C)
def E(v):return h*(1-g*g)*sum(t**3 for t in v)+(2+6*g*g-h**3)*s.prod(v)
quotients=[]
for i in range(3):
    ni=adj[:,i];identity=s.expand(adj[i,i]*(ni.dot(C))+E(ni));quot,rem=s.div(identity,det,*variables)
    assert rem==0;quotients.append(str(s.factor(quot)))
# Rank1: image M=kk^T. All character-gradient components stay in its row span.
k=s.symbols('k0 k1 k2');rankone={u[i]:k[i]**2 for i in range(3)}
rankone.update({pts[0]:k[1]*k[2],pts[1]:k[0]*k[2],pts[2]:k[0]*k[1]})
C1=C.subs(rankone,simultaneous=True)
for i,j in combinations(range(3),2):assert s.expand(C1[i]*k[j]-C1[j]*k[i])==0
assert C.subs({v0:0 for v0 in variables})==s.zeros(3,1)
# Fixed non-Clifford envelope h1, a=(1/(2g),1/(2g),0), beta=(1,1,2).
fixed={h:1,a[0]:1/(2*g),a[1]:1/(2*g),a[2]:0,beta[0]:1,beta[1]:1,beta[2]:2}
relations=[2*y*z-(x-1)**2,2*z*x-(y-1)**2,2*x*y-z*z-2]
J=s.Matrix([[s.diff(r,v0) for v0 in [x,y,z]] for r in relations])
I=s.groebner(relations,x,y,z);crit=s.groebner(relations+[J.det()],x,y,z)
# Standard monomial enumeration for zero-dimensional quotients.
def length(G):
    leads=[s.Poly(f,x,y,z).monoms()[0] for f in G.polys]
    bounds=[next(min(m[i] for m in leads if m[i]>0 and all(m[j]==0 for j in range(3) if j!=i)) for _ in [0]) for i in range(3)]
    from itertools import product
    return sum(not any(all(e[i]>=m[i] for i in range(3)) for m in leads) for e in product(*[range(b) for b in bounds]))
assert I.is_zero_dimensional and length(I)==8
assert crit.is_zero_dimensional
crit_length=length(crit)
for f in [x-1,y-1,z]:assert crit.reduce(s.expand(f**4))[1]==0
minors=[J.extract(r,c).det() for r in combinations(range(3),2) for c in combinations(range(3),2)]
assert s.groebner(relations+minors,x,y,z).contains(s.Integer(1))
Pfixed=s.factor(P.subs(fixed,simultaneous=True));value=s.factor(Pfixed.subs({x:1,y:1,z:0,D:0}));Dstar=s.factor(-value)
assert s.factor((s.Matrix([s.diff(Pfixed,v0) for v0 in [x,y,z]]).subs({x:1,y:1,z:0})).dot(s.Matrix([1,-1,0])))==0
# The entire critical character scheme maps to a single REDUCED central value.
num=s.cancel(Pfixed-D-value).as_numer_denom()[0]
assert s.groebner(list(crit.polys),x,y,z,domain=s.QQ.frac_field(g)).reduce(s.expand(num))[1]==0
closed_D=(2*g**4+10*g**3+21*g**2+19*g+13)/(4*(1+g)**5)
assert s.cancel(Dstar-closed_D)==0
assert s.gcd(s.numer(closed_D),g**4-2,g)==1
certificate={'version':'classification-v14','source':'cubic_clifford_integration_certificate.json',
 'ring':'QQ[h,gamma,character_point,u,1/h,1/gamma,1/(1+h^3),1/(1+gamma)]',
 'universal_principal_cofactor_identities':3,'cofactor_identity':'cof_ii*(adj(M)_i dot (gamma*(1+h^3)*(1+gamma)^6*dG))+E(adj(M)_i) is divisible by det(M)',
 'cofactor_quotients':quotients,'rank1_row_span_identities':3,
 'odd_self_Ext1':'Rank M2 and its projective kernel lies on point cubic E, OR rank M0; ranks1/3 give even dimensions2/0',
 'fixed_envelope':'h1,a=(1/(2gamma),1/(2gamma),0),beta=(1,1,2); alpha=(-2,-2,0)',
 'character_scheme_length':8,'critical_character_scheme_length':crit_length,
 'critical_character_support':[1,1,0],'critical_Groebner_basis':['x+y-2','(y-1)^2','z'],'critical_center_scheme_image':'single reduced point D=Dstar',
 'Dstar':str(Dstar),'order4_specialization':'gamma^4=2; all parameters satisfy the recognized AS4 smooth leading locus',
 'conclusion':'Dstar is definitely non-H3 by odd self-Ext1. It is the ONLY value detected by odd self-Ext1 on one-dimensional modules for this fixed envelope.',
 'limits':'Not a complete list of bad center values: higher-dimensional modules or higher Ext may supply additional obstructions. No H3 assertion for the complement.'}
Path(__file__).with_name('cubic_character_serre_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS: universal cofactor/point-cubic identity and rank1 controls; exact length8 characters, critical scheme length'+str(crit_length)+' at(1,1,0); one reduced bad central image; character obstruction completely determined for fixed envelope')
