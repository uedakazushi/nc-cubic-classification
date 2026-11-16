"""Exact all-value cover of square-positive symmetric-secant z5=0 boundary."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_tools import relations,normal_free,coordinates,polynomial_rows,THETA
w=S.symbols('w');K=S.QQ.frac_field(w);theta=THETA
entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_square_boundary_input.json').read_text())
records=[]
for rec in entry['curves']:
 values=[S.sympify(x,locals={'w':w}) for x in rec['values']]
 assert S.cancel(values[4]**2-values[3]**2)==1
 N,nf,dim=normal_free(relations(S.diag(1,0),values),K);Q=polynomial_rows(N,w);polys=[];used=set()
 original=[i for i in range(N.rows) if any(N[i,:])]
 for minor in rec['minors']:
  polys.append(S.Poly(K.to_sympy(DomainMatrix.from_Matrix(Q.extract(minor['rows'],minor['cols'])).convert_to(K).det()),w))
  used.update(original[i]%dim for i in minor['rows'])
 pole=S.factor(S.lcm([S.denom(K.to_sympy(row[j])) for row in nf.values() for j in used if j in row]))
 expected=S.sympify(rec['functional_pole'],locals={'w':w})
 assert S.cancel(pole/expected).is_Rational
 common=S.gcd(*polys);unit=S.Poly(S.sympify(rec['unit'],locals={'w':w}),w)
 for source in [common,S.Poly(pole,w)]:
  while source.degree():
   g=S.gcd(source,unit)
   if g.degree()==0:break
   source=source.exquo(g)
  if rec['name']=='conic':
   for f in [w*w+1,w*w-w+1,w*w+w+1]:
    while S.rem(source,S.Poly(f,w)).is_zero:source=source.exquo(S.Poly(f,w))
   assert source.degree()==0
  else:assert source.monic().as_expr() in [S.Integer(1),w,w**2,w**3,w**4]
 records.append({'name':rec['name'],'normal_minor_gcd':str(S.factor(common.as_expr())),'selected_functional_pole':str(pole)})
root=S.sqrt(-3);E=S.QQ.algebraic_field(S.sqrt(3),S.I)
cases=[('pluszero',0,0,1,S.QQ),('minuszero',0,0,-1,S.QQ),('gaussian',0,S.I,0,S.QQ_I),('primitive3',0,root/2,-S.Rational(1,2),E),('primitive6',0,root/2,S.Rational(1,2),E)]
points=[]
for name,a,s,t,field in cases:
 N,L,_,_=coordinates(relations(S.diag(1,0),[a,-t,-s,s,t,0]),field)
 rank=DomainMatrix.from_Matrix(N).convert_to(field).rank()
 if name!='primitive6':assert rank==10
 else:
  assert rank==8
  factor=S.Matrix([S.sympify(x,locals={'theta':theta}) for x in entry['quadratic_factor']]);G=(L*factor).applyfunc(S.expand)
  assert all(S.simplify(x)==0 for x in N*G)
  assert max(S.Poly(x,theta).degree() for x in factor)<=2
  J=S.Matrix([[S.expand(x).coeff(theta,i) for i in range(4)] for x in G])
  assert DomainMatrix.from_Matrix(J).convert_to(field).rank()==2
 points.append({'point':name,'normal_dimension':10-rank})
out={'status':'PASS','scope':'entire z5=0 boundary for square positive top / symmetric secant / positive Pfaffian','curves':records,'finite_points':points,'factor_pencil':'at primitive6, explicit Q2(theta) satisfies N L Q2=0; theta coefficient span2 equals normal pencil. Proper projective factor incidence and domain exclude every normal cut. Exact number-field embeddings cover conjugates.','consequence':'together with full main and negative Pfaffian results, no square-positive symmetric secant H3 exists','not_claimed':['nondegenerate positive secant plus','rank2 secant boundary','global H3 classification','relative intrinsic descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_square_boundary_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS square secant z5=0: three rational covers, exact finite points, full primitive6 factor pencil')
