#!/usr/bin/env python3
"""Relative Frobenius dual identities for E2 with both u,v polynomial.
Depends on the polynomial central rank81 checker, with no parameter division.
"""
import json
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
import verify_cubic_third_root_unit_boundary_L_polynomial_center as base
K,F,o,one=base.K,base.F,base.o,base.one
T=base.T
assert len(T.basis[12])==1
ranks=[]
for n in range(13):
 rows={i:{j:c for j,w in enumerate(T.basis[12-n]) if (c:=T.word(v+w).get(0,F.zero))} for i,v in enumerate(T.basis[n])}
 M=DomainMatrix.from_dod(rows,(len(T.basis[n]),len(T.basis[12-n])),F)
 rank=M.rank();assert rank==len(T.basis[n])==len(T.basis[12-n]);ranks.append(rank)
H=base.PolyAlgebra(K,4,base.RC+[base.GC,base.Psi,base.poly],base.weights);H.build(13)
assert len(H.basis[12])==len(H.basis[13])==81
lifts=[(degree,tuple(letter+1 for letter in w)) for degree in range(13) for w in T.basis[degree]]
columns=[H.word((0,)*(12-degree)+w) for degree,w in lifts]
mat=DomainMatrix.from_dod({i:{j:columns[j].get(i,K.zero) for j in range(81) if columns[j].get(i,K.zero)} for i in range(81)},(81,81),K)
def inverse_unit(M):
 num,den=M.inv_den()
 assert den and den.is_ground
 inv=num.applyfunc(lambda c:K.exquo(c,den),K)
 assert M.matmul(inv)==DomainMatrix.eye(81,K)
 return inv
inv=inverse_unit(mat)
topid=next(j for j,(degree,w) in enumerate(lifts) if degree==12)
xm=DomainMatrix.from_dod({i:{j:H.right[13][j,0].get(i,K.zero) for j in range(81) if H.right[13][j,0].get(i,K.zero)} for i in range(81)},(81,81),K)
xinv=inverse_unit(xm)
def relative_lambda(w):
 degree=len(w)
 if degree<12:return K.zero
 vv=DomainMatrix.from_dod({i:{0:c} for i,c in H.word(w).items()},(81,1),K)
 if degree==13:vv=xinv.matmul(vv)
 else:assert degree==12
 return inv.matmul(vv).to_list()[topid][0]
for degree,w in lifts:
 for letter,exponent in enumerate([0,0,2,1]):
  assert not(relative_lambda(w+(letter,))-o**exponent*relative_lambda((letter,)+w))
out={'status':'PASS','scope':'E2 all6 embeddings, all u,v; exact polynomial identities','pairing_ranks':ranks,'relative_dual':'Hom_S(A,S)=A_nu(12)','convention':'lambda(a*v)=lambda(nu(v)*a)','nu_xybc_omega_exponents':[0,0,2,1],'nu_order':3,'number_of_basis_generator_identities':324,'inverse_denominators_parameter_constants':True,'not_claimed':['all parameter generic CSA degree9','all parameter H3 exclusion','entire L curve classification','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_boundary_L_polynomial_Frobenius_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('all-u,v relative Frobenius polynomial identities PASS')
