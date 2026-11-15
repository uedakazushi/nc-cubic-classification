#!/usr/bin/env python3
"""Independent exact audits of three fixed as4 nonreduced-base presentations."""
from verify_cubic_stafford import nakayama
from verify_cubic_pym_generic import *
Q=S.Rational
def add(*xs):
 d={}
 for x in xs:
  for w,c in x.items():d[w]=d.get(w,0)+c
 return d
comm=lambda i,j,c:{(i,j):c,(j,i):-c}
sym=lambda i,j,c:{(i,j):c/2,(j,i):c/2}
sq=lambda i,c:{(i,i):c}
rels1=[add(sym(0,2,Q(1)),sq(1,-1),comm(0,1,-Q(10,21)),comm(0,3,Q(47,280)),comm(2,3,-Q(9,800))),add(sym(0,3,Q(1)),sym(1,2,-Q(1)),comm(0,2,Q(10,7)),comm(1,3,-Q(3,8))),add(sym(1,3,Q(1)),comm(0,3,-Q(2,7)),comm(2,3,Q(3,40))),add(sq(2,1),comm(0,3,-Q(2,7)),comm(1,2,-Q(10,3)),comm(2,3,-Q(9,40))),add(sym(2,3,Q(1)),comm(1,3,-Q(2,3))),add(sq(3,1),comm(2,3,2))]
rels2=[add(sym(0,2,Q(1)),sq(1,-1),comm(0,1,-2),comm(0,3,Q(1,8))),add(sym(0,3,Q(1)),sym(1,2,-Q(1)),comm(0,2,2),comm(1,3,-Q(1,8))),add(sym(1,3,Q(1)),comm(1,2,2)),add(sq(2,1),comm(0,3,2),comm(1,2,2),comm(2,3,-Q(1,8))),add(sym(2,3,Q(1)),comm(1,3,-2)),add(sq(3,1),comm(2,3,2))]

rels31=[add(sym(0,2,Q(1)),sq(1,-1),comm(0,3,-2)),add(sym(1,2,Q(1)),comm(1,3,-2)),add(sq(2,1),comm(2,3,2)),add(sym(0,3,Q(1)),comm(0,1,2),comm(0,2,-Q(1,8))),add(sym(1,3,Q(1)),comm(0,2,-2),comm(1,2,Q(1,8))),add(sym(2,3,Q(1)),comm(1,2,2))]

def main():
 results=[]
 for fam,rr in enumerate([rels1,rels2,rels31],1):
  mu,audit=nakayama(rr);assert mu==S.eye(4)
  f3,P3,_=quotient_projection(rr,3);f4,P4,_=quotient_projection(rr,4);assert len(f3)==20 and len(f4)==35
  ix={w:j for j,w in enumerate(words(4))};M=S.zeros(140,20)
  for j,k in enumerate(f3):
   w=words(3)[k]
   for i in range(4):M[35*i:35*(i+1),j]=P4[:,ix[w+(i,)]]-P4[:,ix[(i,)+w]]
  _,rows=DomainMatrix.from_Matrix(M.T).convert_to(S.QQ).rref();assert len(rows)==20
  det=DomainMatrix.from_Matrix(M[list(rows),:]).convert_to(S.QQ).det();assert det!=0
  audit.update(family=fam,relations=[{str(w):str(v) for w,v in r.items()} for r in rr],Nakayama='identity conditional on AS4',dimensions_3_4=[20,35],centre3_dimension=0,minor_rows=list(rows),minor_determinant=str(det));results.append(audit)
  print('PASS fixed curvilinear presentation',fam,'Frobenius mu=id and central cubic rank20')
 cert={'version':'classification-v69','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9','presentation_source':'research/proofs/CY_ZERO_COMMUTATORS_CURVILINEAR_FOUR_COMPLETE.tex (CF2),(CF3) and CY_ZERO_COMMUTATORS_CURVILINEAR_THREE_ONE_COMPLETE.tex (CT2)','field':'QQ','witnesses':results,'scope':'Exact verification of three fixed presentations. No AS4 existence/atlas coverage/noetherianity/domain theorem imported. At any H3 realization the exact Frobenius calculation forces CY and rank20 excludes its cubic.'}
 Path(__file__).with_name('cubic_as4_curvilinear_fixed_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')

if __name__=='__main__':main()
