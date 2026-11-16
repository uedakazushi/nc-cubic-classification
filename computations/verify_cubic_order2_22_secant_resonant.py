"""Exact entire-fiber exclusion at rho=-1/2, including every minor exception."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
R=S.QQ.poly_ring('L');L=R.gens[0];one=R.one;zero=R.zero
source=Path(__file__).with_name('cubic_order2_22_secant_resonant_input.json');data=json.loads(source.read_text())
assert data['generator_order']==['x','y','u','v'] and len(data['functionals'])==19 and len(data['rank_minors'])==12
funcs=[{int(j):R.ring.from_dict({(n,):S.QQ(c) for n,c in co}) for j,co in f.items()} for f in data['functionals']]
w3=[w for w in itertools.product(range(4),repeat=3) if sum(i>=2 for i in w)%2==0]
w4=[w for w in itertools.product(range(4),repeat=4) if sum(i>=2 for i in w)%2==0];ix={w:i for i,w in enumerate(w4)}
P=[[0,L/2,-L/2,one],[L/2,0,-one,L],[-L/2,-one,0,-L],[one,L,-L,0]]
K=[[0,one/2,0,0],[0,0,0,one/2],[-one,0,0,0],[0,0,one,0]]
wu=list(itertools.product(range(2),repeat=2));wv=list(itertools.product(range(2,4),repeat=2));rels=[]
for i in range(4):rels.append({w:R(c) for w,c in zip(wu+wv,P[i]+K[i]) if c})
rels.extend([{(0,2):one,(2,1):one,(3,0):one/2},{(1,3):one,(2,1):one,(3,0):-one/2}])
checks=0
for rel in rels:
 for pos in range(3):
  for rest in itertools.product(range(4),repeat=2):
   if (sum(i>=2 for i in rest)+sum(i>=2 for i in next(iter(rel))))%2:continue
   row={ix[rest[:pos]+w+rest[pos:]]:c for w,c in rel.items()}
   for f in funcs:
    assert sum((c*f.get(j,zero) for j,c in row.items()),zero)==zero;checks+=1
assert checks==2736
rows={}
for i,f in enumerate(funcs):
 for g in range(2):
  row={}
  for j,w in enumerate(w3):
   c=f.get(ix[w+(g,)],zero)-f.get(ix[(g,)+w],zero)
   if c:row[j]=c
  rows[2*i+g]=row
M=DomainMatrix(rows,(38,32),R);gcd=zero;degrees=[]
for witness in data['rank_minors']:
 assert len(witness['rows'])==len(witness['columns'])==10
 p=M.extract(witness['rows'],witness['columns']).det();assert p
 degrees.append(p.degree());gcd=gcd.gcd(p)
assert gcd.monic()==L**10*(L*L-S.QQ(3,2))**5
# All residual values: L=0 and the two conjugate roots 2L^2=3.
F=S.QQ.algebraic_field(S.sqrt(6));records=[]
for ell in [S.Integer(0),S.sqrt(6)/2]:
 node_rels=[]
 for rel in rels:
  rr={}
  for w,c in rel.items():
   val=F.from_sympy(R.to_sympy(c).subs(S.Symbol('L'),ell))
   if val:rr[w]=val
  node_rels.append(rr)
 def quotient(n,parity):
  words=[w for w in itertools.product(range(4),repeat=n) if sum(i>=2 for i in w)%2==parity];index={w:i for i,w in enumerate(words)};rows=[]
  for rel in node_rels:
   rp=sum(i>=2 for i in next(iter(rel)))%2
   for pos in range(n-1):
    for rest in itertools.product(range(4),repeat=n-2):
     if (sum(i>=2 for i in rest)+rp)%2!=parity:continue
     rows.append({index[rest[:pos]+w+rest[pos:]]:c for w,c in rel.items()})
  mat=DomainMatrix({i:row for i,row in enumerate(rows)},(len(rows),len(words)),F)
  rr,piv=mat.rref(method='GJ');rr=rr.to_dod();free=[j for j in range(len(words)) if j not in piv];proj={j:{i:F.one} for i,j in enumerate(free)}
  for row,j in enumerate(piv):proj[j]={i:-rr[row].get(k,F.zero) for i,k in enumerate(free) if rr[row].get(k,F.zero)}
  return words,index,free,proj
 words3,index3,free3,proj3=quotient(3,0);q4=[quotient(4,p) for p in [0,1]]
 assert len(free3)==10 and [len(q[2]) for q in q4]==[19,16]
 eqs={}
 for col,k in enumerate(free3):
  for g,mu in enumerate([1,1,-1,-1]):
   ww,index,free,proj=q4[g//2]
   for word,c in [(words3[k]+(g,),F.one),((g,)+words3[k],-F(mu))]:
    for j,z in proj[index[word]].items():
     row=eqs.setdefault((g,j),{});row[col]=row.get(col,F.zero)+c*z
 eqs=[{j:c for j,c in row.items() if c} for row in eqs.values()];eqs=[row for row in eqs if row]
 mat=DomainMatrix({i:row for i,row in enumerate(eqs)},(len(eqs),10),F);_,piv=mat.rref(method='GJ');assert len(piv)==10
 records.append({'parameter':str(ell),'positive_B3':10,'even_B4':19,'odd_B4':16,'designated_normalizer_rank':10,'geometric_values_covered':1 if ell==0 else 2})
out={'status':'PASS','scope':'entire geometric resonant fiber rho=-1/2, C=0, in the necessary secant surface',
 'annihilator_identities':checks,'polynomial_functionals':19,'minor_count':12,'minor_degrees':degrees,
 'monic_minor_gcd':'L^10*(L^2-3/2)^5','all_minor_exceptions':records,
 'conclusion':'no H3 point anywhere on the resonant fiber; finite exceptional set completely checked over Q(sqrt6)',
 'not_claimed':['nonresonant surface normalizers','AS4 existence elsewhere','relative intrinsic families']}
Path(__file__).with_name('cubic_order2_22_secant_resonant_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS whole resonant secant fiber: 2736 identities, twelve exact minors, all three residual values')
