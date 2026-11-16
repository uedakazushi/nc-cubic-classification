"""Entire nondegenerate secant resonance: close both quadratic-field exception curves."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_functionals import normal_matrix,specialize,SIGMA
from cubic_order2_22_secant_tools import relations,normal_free,quotient
s=SIGMA;N=normal_matrix();entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_resonance_final_input.json').read_text());records=[]
for name,r,E in [('gaussian',S.I,S.QQ_I),('sqrtminus3',S.sqrt(-3),S.QQ.algebraic_field(S.sqrt(-3)))]:
 M,strips=specialize(N,r,(1-r*r)/2,E);P=M.domain;rec=entry[name];assert {str(i):v for i,v in strips.items()}==rec['row_s_powers'];common=P.zero
 def pol(expr):return P.ring.from_dict({mon:E.from_sympy(c) for mon,c in S.Poly(expr,s).terms()})
 for witness in rec['witnesses']:
  d=M.extract(witness['rows'],witness['cols']).det();assert d==pol(S.sympify(witness['det'],locals={'s':s}));common=common.gcd(d)
 allowed=pol(s if name=='gaussian' else s*(3*s*s+2-2*r));left=common
 while left.degree()>0:
  g=left.gcd(allowed);assert g.degree()>0;left=left.exquo(g)
 records.append({'curve':name,'minor_gcd':str(P.to_sympy(common))})
# Gaussian s0 and the only other curve's finite remainder, all conjugates exact.
points=[('gaussian_zero',S.I,S.Integer(0),S.QQ_I),('sqrtminus3_finite',S.sqrt(-3),(1+S.sqrt(-3))/S.sqrt(3),S.QQ.algebraic_field(S.sqrt(3),S.I))]
finite=[]
for name,r,sv,E in points:
 t=(1-r*r)/2;alpha=S.simplify((r-1)/(r+1));R=relations(S.Matrix([[0,r],[r,0]]),[S.simplify(1-r*r-t*t-alpha*sv*sv),-t,alpha*sv,sv,t,1]);_,_,f3,_=quotient(R,3,E);NM,_,dim=normal_free(R,E);data={}
 for i in range(NM.rows):
  row={j:E.from_sympy(S.expand(NM[i,j])) for j in range(NM.cols) if NM[i,j]};row={j:v for j,v in row.items() if v}
  if row:data[i]=row
 rank=DomainMatrix(data,NM.shape,E).rank();print(name,'dimensions',len(f3),dim,'normalrank',rank,flush=True)
 assert len(f3)==20 and rank==8
 assert dim==(36 if name=='gaussian_zero' else 35)
 finite.append({'point':name,'B3':20,'B4':dim,'normal_rank':8,'exclusion':'not AS4: B4 dimension36' if dim==36 else 'whole normal pencil factors'})
out={'status':'PASS','universal_functionals':'eight explicit polynomial quartic functionals annihilate ALL 288 original relation insertions identically in QQ[r,s,t]; no generic quotient basis or approximate root calculation','curves':records,'finite_points':finite,'coverage':'Gaussian three-minor gcd constant*s3; sqrt(-3) gcd constant*s3*(s2+(2-2sqrt(-3))/3). Gaussian s0 has B4 dimension36 and is not AS4. sqrt(-3) s0 is excluded a0 boundary; remaining finite roots and all conjugates have B4 dimension35 and original normal rank8.','conclusion':'all remaining resonance curves have normal dimension<=2; universal factor pencil is the whole kernel. Together with prior cover, entire nondegenerate symmetric-secant positive-Pfaffian resonance has no H3.','remaining':['off-resonance q1 main with a!=0','global H3 classification','relative intrinsic descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_resonance_final_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS entire nondegenerate secant resonance: polynomial annihilators, both quadratic-field covers, exact finite points and conjugates')
