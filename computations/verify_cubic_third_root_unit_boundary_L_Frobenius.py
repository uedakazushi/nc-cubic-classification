#!/usr/bin/env python3
"""Exact Artinian Frobenius pairings, at the fixed six-embedding example.
This does not assert the unproved local-order implication for H3.
"""
import json
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
import verify_cubic_third_root_unit_boundary_L_finite_center as base
T=base.T;K=base.K;o=base.o
assert len(T.basis[12])==1
ranks=[]
for n in range(13):
 rows={i:{j:c for j,w in enumerate(T.basis[12-n]) if (c:=T.word(v+w).get(0,K.zero))} for i,v in enumerate(T.basis[n])}
 M=DomainMatrix.from_dod(rows,(len(T.basis[n]),len(T.basis[12-n])),K)
 rank=M.rank();assert rank==len(T.basis[n])==len(T.basis[12-n]);ranks.append(rank)
# Determine the convention directly: lambda(a*v)=lambda(nu(v)*a).
phases=[]
for letter in range(3):
 possible=[]
 for exponent in range(3):
  if all(not(T.word(w+(letter,)).get(0,K.zero)-o**exponent*T.word((letter,)+w).get(0,K.zero)) for w in T.basis[11]):possible.append(exponent)
 assert len(possible)==1;phases.append(possible[0])
assert phases in [[0,1,2],[0,2,1]]
out={'status':'PASS','scope':'fixed E2,u1,v0 all6 characteristic-zero embeddings; exact top-degree Artinian pairings only','top_degree':12,'pairing_ranks':ranks,'convention':'lambda(a*v)=lambda(nu(v)*a)','generators':['y','b','c'],'nu_omega_exponents':phases,'nu_order':3,'not_claimed':['finite global dimension exclusion','local Frobenius hereditary implies normal proof','full L-curve classification']}
Path(__file__).with_name('cubic_third_root_unit_boundary_L_Frobenius_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
# Lift the top functional to the relative S-dual using the proven free basis.
# Products of a basis lift (degree<=12) and a generator have degree<=13.
# Their lambda coefficients have degrees <=1; hence only 1 and x occur.
# Killing Psi,z9 and setting x=1 therefore detects each such coefficient.
H=base.GradedAlgebra(K,4,base.RC+[base.GC,base.Psi,base.Z],base.weights);H.build(13)
assert len(H.basis[12])==len(H.basis[13])==81
lifts=[(degree,tuple(letter+1 for letter in w)) for degree in range(13) for w in T.basis[degree]]
def vec(w):return H.word(w)
columns=[vec((0,)*(12-degree)+w) for degree,w in lifts]
mat=DomainMatrix.from_dod({i:{j:columns[j].get(i,K.zero) for j in range(81) if columns[j].get(i,K.zero)} for i in range(81)},(81,81),K)
assert mat.rank()==81
inv=mat.inv()
topid=next(j for j,(degree,w) in enumerate(lifts) if degree==12)
# degree13 -> degree12 via inverse x action
xm=DomainMatrix.from_dod({i:{j:H.right[13][j,0].get(i,K.zero) for j in range(81) if H.right[13][j,0].get(i,K.zero)} for i in range(81)},(81,81),K)
assert xm.rank()==81
xinv=xm.inv()
def relative_lambda(w):
 degree=len(w)
 if degree<12:return K.zero
 vv=DomainMatrix.from_dod({i:{0:c} for i,c in vec(w).items()},(81,1),K)
 if degree==13:vv=xinv.matmul(vv)
 else:assert degree==12
 return inv.matmul(vv).to_list()[topid][0]
for degree,w in lifts:
 for letter,exponent in enumerate([0,0,2,1]):
  assert not(relative_lambda(w+(letter,))-o**exponent*relative_lambda((letter,)+w))
out['relative_dual']='Hom_S(A,S) = A_nu(12), by homogeneous perfect pairing and exact basis/generator twisted cyclic identities'
out['relative_nu_xybc_exponents']=[0,0,2,1]
out['relative_nu_order']=3
out['not_claimed'].remove('local Frobenius hereditary implies normal proof')
out['not_claimed'].append('local Frobenius hereditary implies normal proof')
Path(__file__).with_name('cubic_third_root_unit_boundary_L_Frobenius_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('relative Frobenius lift PASS; exact order3')
