"""Entire square-positive secant plus main: selected functionals, five curves, Gaussian factors and degree12 field."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_tools import relations,normal_free,polynomial_rows,coordinates,THETA
q,t,w=S.symbols('q t w');entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_square_main_input.json').read_text())
def main_rel(q,t):return relations(S.diag(1,0),[(1-t*t)/q,-t,q,0,t,q])
K=S.QQ.frac_field(q,t);N,nf,dim=normal_free(main_rel(q,t),K);assert dim==35
functions=sorted(set(i%dim for i in entry['generic_rows']));D=q*t*(t*t-1)*(q*q-4*t*t+2)
for row in nf.values():
 for j in functions:
  if j not in row:continue
  for f,n in S.factor_list(S.denom(K.to_sympy(row[j])))[1]:assert S.rem(S.Poly(D,q,t),S.Poly(f,q,t)).is_zero
M=N.extract(entry['generic_rows'],entry['generic_cols']);poly=[];scale=[]
for i in range(10):
 den=S.lcm([S.denom(S.cancel(c)) for c in M[i,:]]);scale.append(den);poly.append([S.cancel(c*den) for c in M[i,:]])
expected=-(2*t-1)**3*(2*t+1)**3/(16*q*t**3*(t*t-1)*(q*q-4*t*t+2)**2)
ring=S.QQ.poly_ring(q,t);assert DomainMatrix.from_Matrix(S.Matrix(poly)).convert_to(ring).det()==ring.from_sympy(S.cancel(expected*S.prod(scale)))
print('PASS generic six-functional minor; no extraneous high-degree pole',flush=True)
P=w**12-12*w**10+28*w**8+96*w**6+112*w**4-192*w*w+64;polyP=S.Poly(P,w)
assert polyP.is_irreducible
F=S.QQ.frac_field(w);cover=[]
def remainder(expr,modulus):return S.rem(S.Poly(S.fraction(S.cancel(expr))[0],w),modulus)
for rec in entry['curves']:
 qq=S.sympify(rec['q'],locals={'w':w});tt=S.sympify(rec['t'],locals={'w':w});unit=S.Poly(S.sympify(rec['unit'],locals={'w':w}),w)
 NN,nf0,d0=normal_free(main_rel(qq,tt),F);Q=polynomial_rows(NN,w);original=[i for i in range(NN.rows) if any(NN[i,j] for j in range(32))]
 witness=rec['witnesses'];polys=[]
 for pos in witness:
  value=F.to_sympy(DomainMatrix.from_Matrix(Q.extract(pos['rows'],pos['cols'])).convert_to(F).det());polys.append(S.Poly(value,w))
 gcd=S.gcd(*polys);assert not gcd.is_zero
 used=set(original[i]%d0 for pos in witness for i in pos['rows'])
 den=S.lcm([S.denom(F.to_sympy(row[j])) for row in nf0.values() for j in used if j in row]);e=S.Poly(den*gcd.as_expr(),w).sqf_part().monic()
 for remove in [unit,S.Poly(S.fraction(S.cancel(tt-S.Rational(1,2)))[0],w)]:
  while True:
   gg=S.gcd(e,remove)
   if gg.degree()==0:break
   e=e.exquo(gg)
 for factor,n in S.factor_list(e.as_expr())[1]:
  pp=S.Poly(factor,w).monic()
  if pp==polyP.monic():continue
  if remainder(tt,pp).is_zero and S.gcd(S.Poly(S.fraction(S.cancel(qq*qq+1))[0],w),pp).degree()==0:continue
  gaussian=remainder(qq*qq+1,pp).is_zero and (remainder(tt,pp).is_zero or remainder(tt+S.Rational(1,2),pp).is_zero)
  assert gaussian
 cover.append({'curve':rec['name'],'selected_poles':str(S.factor(den)),'two_minor_gcd':str(S.factor(gcd.as_expr())),'remaining_exception_polynomial':str(S.factor(e.as_expr()))})
 print('PASS curve',rec['name'],flush=True)
# Gaussian finite exceptions; the negative chirality isolated kernel is reducible.
gaussian=[]
for qq in [S.I,-S.I]:
 for tt in [S.Integer(0),-S.Rational(1,2)]:
  NN,LL,_,_=coordinates(main_rel(qq,tt),S.QQ_I);rank=DomainMatrix.from_Matrix(NN).convert_to(S.QQ_I).rank()
  if tt==0:assert rank==10
  else:
   assert rank==9
   quad=S.Matrix([-S.Rational(1,2),1,1,2,-qq,-qq]);G=LL.subs(THETA,2)*quad
   assert G!=S.zeros(10,1) and (NN*G).applyfunc(S.expand)==S.zeros(NN.rows,1)
  gaussian.append({'q':str(qq),'t':str(tt),'normal_dimension':10-rank,'left_factor':'x+2y' if rank==9 else None})
print('PASS both Gaussian pairs and unique linear factors',flush=True)
# One exact degree12 field check covers all conjugate roots of P, without approximate evaluation.
root=S.CRootOf(P,0);Afield=S.QQ.algebraic_field(root);alpha=Afield.unit;frac=S.QQ.frac_field(w)
def evalpoly(poly):
 out=Afield.zero
 for monomial,c in poly.items():out+=Afield.convert(c,S.QQ)*alpha**monomial[0]
 return out
def evaluate(e):
 f=frac.from_sympy(S.sympify(e));return evalpoly(f.numer)/evalpoly(f.denom)
assert not evaluate(P)
qq=(w-2/w)/2;tt=(w+2/w)/4;Rs=main_rel(qq,tt);Rnative=[{word:evaluate(c) for word,c in rel.items() if c} for rel in Rs]
words=list(itertools.product(range(4),repeat=4));ix={v:i for i,v in enumerate(words)};relrows=[]
for rel in Rnative:
 for pos in range(3):
  for extra in itertools.product(range(4),repeat=2):relrows.append({ix[extra[:pos]+word+extra[pos:]]:c for word,c in rel.items() if c})
dm=DomainMatrix({i:row for i,row in enumerate(relrows) if row},(len(relrows),256),Afield);rr,piv=dm.rref();assert 256-len(piv)==35
data=rr.to_dod();free=[i for i in range(256) if i not in piv];fi={v:i for i,v in enumerate(free)}
native_nf={i:{fi[j]:-c for j,c in data[k].items() if j in fi and c} for k,i in enumerate(piv)};native_nf.update({i:{fi[i]:Afield.one} for i in free})
for row in relrows:
 out={}
 for j,c in row.items():
  for v,d in native_nf[j].items():out[v]=out.get(v,Afield.zero)+c*d
 assert not any(out.values())
positive=[v for v in itertools.product(range(4),repeat=3) if sum(i>=2 for i in v)%2==0];normal={}
for col,word in enumerate(positive):
 for g in range(4):
  for raw,c in [(word+(g,),1),((g,)+word,-1 if g<2 else 1)]:
   for row,d in native_nf[ix[raw]].items():
    j=g*35+row;normal.setdefault(j,{})[col]=normal.setdefault(j,{}).get(col,Afield.zero)+c*d
normal={i:{j:c for j,c in row.items() if c} for i,row in normal.items() if any(row.values())}
assert DomainMatrix(normal,(140,32),Afield).rank()==10
print('PASS exact degree12 field and all conjugates',flush=True)
out={'status':'PASS','scope':'entire symmetric-secant square-positive-top positive-Pfaffian main z5!=0, combined with prior t=1/2 factor-pencil exclusion','generic_minor':str(expected),'generic_functional_indices':functions,'generic_pole_divisor':str(D),'complete_curve_cover':cover,'Gaussian_checks':gaussian,'degree12_exception':{'polynomial':str(P),'irreducible':True,'B4':35,'normal_rank':10,'all_conjugates':True},'conclusion':'all main points have zero normal kernel or a reducible normal cut; no H3 anywhere in z5!=0 main','not_claimed':['z5=0 boundary','nondegenerate positive-top secant plus','rank2 secant boundary','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_square_main_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS full square secant main: six-function minor, five rational curves, all Gaussian/degree12 exceptions')
