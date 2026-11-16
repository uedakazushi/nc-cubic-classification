"""Complete pure-projection subcase of semisimple (2,2), odd rank2."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
FIELD=S.QQ.algebraic_field(S.I,S.sqrt(-2))
def check(C0,A0,D0,q0):
 A,B,C,D,p,q=map(S.sympify,[A0,1,C0,D0,1,q0])
 U=S.Matrix([[0,A,-A,B],[A,C,-B,D],[-A,-B,-C,-D],[B,D,-D,0]])
 K=S.Matrix([[-p,0,0,0],[0,0,-p,0],[0,-q,0,0],[0,0,0,-q]])
 wordsU=list(itertools.product(range(2),repeat=2));wordsV=list(itertools.product(range(2,4),repeat=2));rels=[]
 for i in range(4):rels.append({w:c for w,c in zip(wordsU+wordsV,list(U.row(i))+list(K.row(i))) if c})
 rels.extend([{(0,2):1,(1,3):1},{(2,0):p,(3,1):q}])
 def quotient(n):
  words=list(itertools.product(range(4),repeat=n));ix={w:i for i,w in enumerate(words)};rows=[]
  for r in rels:
   for pos in range(n-1):
    for rest in itertools.product(range(4),repeat=n-2):rows.append({ix[rest[:pos]+w+rest[pos:]]:FIELD.from_sympy(S.sympify(c)) for w,c in r.items()})
  dm=DomainMatrix({i:r for i,r in enumerate(rows)},(len(rows),len(words)),FIELD)
  rr,pv=dm.rref();assert len(words)-len(pv)=={3:20,4:35}[n]
  return words,ix,rr.to_dod(),pv
 w3,i3,r3,p3=quotient(3);w4,i4,r4,p4=quotient(4)
 free=[i for i in range(256) if i not in p4];proj={j:{i:FIELD.one} for i,j in enumerate(free)}
 for row,j in reversed(list(enumerate(p4))):
  proj[j]={i:-r4[row].get(k,FIELD.zero) for i,k in enumerate(free) if r4[row].get(k,FIELD.zero)}
 f3=[i for i in range(64) if i not in p3];rows={}
 for col,k in enumerate(f3):
  for g,mu in enumerate([1,1,-1,-1]):
   for w,c in [(w3[k]+(g,),FIELD.one),((g,)+w3[k],-FIELD.from_sympy(S.Integer(mu)))]:
    for j,z in proj[i4[w]].items():
     row=rows.setdefault(g*len(free)+j,{});row[col]=row.get(col,FIELD.zero)+c*z
 rows={i:{j:c for j,c in row.items() if c} for i,row in rows.items()};rows={i:r for i,r in rows.items() if r}
 rr,pv=DomainMatrix(rows,(4*len(free),len(f3)),FIELD).rref()
 assert len(f3)==20 and len(pv)==20
 return {'degree3':20,'degree4':35,'normalizer_rank':20}

# Exact universal residual equations after normalizing the invertible pure
# odd relations to p=I, q=diag(1,r), and the positive quartic B coefficient to1.
r=S.symbols('r');cc=-(1+r)/(1-r)
res=S.factor((2+cc**2)*(1-r*r)+2*cc*(1+r*r))
assert S.cancel(res-(1-r)*(1+r))==0
# Jordan q: the four cyclicity conditions have no common zero, all parameters.
a,c,d=S.symbols('a c d')
polys=[-(a-a*c-2*a*d+c-2*d+c*c),-2*a*(a-1),-2*(a-1)*(a-c),-(4*a*d-2-c*c)]
assert list(S.groebner(polys,a,c,d))==[1]
records=[]
records.append({'q':'diag(1,-1)','U':[1,1,0,'1/2'],**check(0,1,S.Rational(1,2),-1)})
for sig1,sig2 in itertools.product([1,-1],repeat=2):
 records.append({'q':f'diag(1,{sig1}*i)','U':[0,1,f'{sig2}*sqrt(-2)',0],**check(sig2*S.sqrt(-2),0,0,sig1*S.I)})
out={'status':'PASS','scope':'complete pure-projection subcase of semisimple (2,2), mixed rank2',
 'universal_checks':['diagonal residual identity forcing r=-1 or r^2=-1','Jordan coefficient ideal is the unit ideal'],
 'five_normalized_necessary_presentations':records,
 'conclusion':'all five have zero designated Nakayama-normal cubic kernel, hence no H3',
 'not_claimed':['four graph-pencil cases','nonsemisimple (2,2)','mixed rank4','AS4 existence for the necessary presentations']}
Path(__file__).with_name('cubic_order2_22_pure_exclusion_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS whole pure-projection (2,2) rank2 subcase: five exact rank20 normalizer certificates')
