"""All-parameter exact derivation certificates for the diagonal canonical base."""
import json
from pathlib import Path
import itertools,sympy as S
alpha,c=S.symbols('alpha c');vars=S.symbols('d0 d1 d2 d3 e0 e1 e2 e3')
words4=list(itertools.product(range(2),repeat=4));ix={w:i for i,w in enumerate(words4)}
rels=[{(0,0,1):1,(0,1,0):-alpha,(1,0,0):1},{(1,1,0):1,(1,0,1):-alpha,(0,1,1):1}]
def elim(rows,n):
 rows=[{j:S.expand(c) for j,c in row.items() if c!=0} for row in rows];ps=[];cols=set(range(n))
 while 1:
  hit=next(((i,j,cc) for i,row in enumerate(rows) for j,cc in row.items() if j in cols and cc!=0 and not S.sympify(cc).free_symbols),None)
  if hit is None:break
  i,j,cc=hit;p={k:S.expand(v/S.sympify(cc)) for k,v in rows.pop(i).items()};ps.append((j,p));cols.remove(j)
  for row in rows:
   co=row.get(j,0)
   if not co:continue
   for k,v in p.items():
    new=S.expand(row.get(k,0)-co*v)
    if new==0:row.pop(k,None)
    else:row[k]=new
 return ps,cols,rows
rows=[]
for r in rels:
 for gg in range(2):
  for side in [0,1]:rows.append({ix[((gg,)+w) if side==0 else (w+(gg,))]:cc for w,cc in r.items()})
ps,free,remain=elim(rows,16);assert len(ps)==7 and not any(remain);free=sorted(free);proj={j:{i:1} for i,j in enumerate(free)}
for j,row in reversed(ps):
 out={}
 for k,cc in row.items():
  if k==j:continue
  for i,co in proj[k].items():out[i]=S.expand(out.get(i,0)-cc*co)
 proj[j]={i:co for i,co in out.items() if co!=0}
quad=list(itertools.product(range(2),repeat=2))
def matrices(kind):
 out=[]
 for rel in rels:
  rr={}
  for word,cc in rel.items():
   for pos in range(3):
    prefix=word[:pos]
    if kind=='diag': gp=prefix;scale=c**prefix.count(1)
    elif kind=='swap':gp=tuple(1-j for j in prefix);scale=1
    else:
     raise Exception()
    for j,qword in enumerate(quad):
     term=gp+qword+word[pos+1:];coef=cc*scale*vars[4*word[pos]+j]
     for k,z in proj[ix[term]].items():rr[k]=S.expand(rr.get(k,0)+coef*z)
  out.extend(rr.get(j,0) for j in range(9))
 return S.linear_eq_to_matrix(out,vars)[0]

# Every reduction of T_4 used only nonzero constant pivots.
assert len(ps)==7 and len(free)==9
M=matrices('swap')[:,[1,2,4,5,6,7]]
piv,cols,rows=elim([{j:M[i,j] for j in range(6) if M[i,j]!=0} for i in range(18)],6)
assert len(piv)==6 and not cols
# g=diag(1,-1), square-compatible four coefficient columns.
M=matrices('diag').subs(c,-1)[:,[1,2,4,7]]
inner=S.Matrix([-1,1,0,2]); assert M*inner==S.zeros(18,1)
# Remove the inner derivation using its constant e3=2 coefficient.
N=M[:,[0,1,2]]
piv,cols,rows=elim([{j:N[i,j] for j in range(3) if N[i,j]!=0} for i in range(18)],3)
assert len(piv)==1
# Remaining rows are supported on individual columns; their coefficient
# ideals are unit ideals in Q[alpha], rather than generic-rank claims.
for row in rows:
    assert len(row)<=1
for col in cols:
    polys=[row[col] for row in rows if col in row]
    gcd=S.Poly(polys[0],alpha)
    for p in polys[1:]:gcd=S.gcd(gcd,S.Poly(p,alpha))
    assert gcd.degree()==0
# g=diag(1,c), c^2=-1: only delta(x)=d3*y^2 survives square compatibility.
M=matrices('diag')[:,3]
polys=[]
for p in M:
    p=S.rem(S.Poly(p,c),S.Poly(c*c+1,c)).as_expr()
    polys.extend(S.Poly(p,c).all_coeffs())
gcd=S.Poly(0,alpha)
for p in polys:gcd=S.gcd(gcd,S.Poly(p,alpha))
assert S.expand(gcd.monic().as_expr()-alpha)==0
# Direct centralizer computations in T_3 from the original cubic relations.
words3=list(itertools.product(range(2),repeat=3));index3={w:i for i,w in enumerate(words3)}
R=S.Matrix([[r.get(w,0) for w in words3] for r in rels]);rr,piv=R.rref()
free3=[i for i in range(8) if i not in piv];P=S.zeros(6,8)
for j,i in enumerate(free3):P[j,i]=1
for j,i in enumerate(piv):
    for k,l in enumerate(free3):P[k,i]=-rr[j,l]
for L in [{0:1},{0:1,1:1}]:
    cols=[]
    for w in quad:
        v=S.zeros(8,1)
        for i,co in L.items():
            v[index3[w+(i,)]]+=co;v[index3[(i,)+w]]-=co
        cols.append(P*v)
    Z=S.Matrix.hstack(*cols)
    square=S.Matrix([L.get(i,0)*L.get(j,0) for i,j in quad])
    assert Z*square==S.zeros(6,1)
    minors=[S.factor(Z.extract(rs,cs).det()) for rs in itertools.combinations(range(6),3) for cs in itertools.combinations(range(4),3)]
    gcd=S.Poly(0,alpha)
    for p in minors:gcd=S.gcd(gcd,S.Poly(p,alpha))
    assert gcd.monic().as_expr()==alpha-2
    assert Z.subs(alpha,2).rank()==2
out={'status':'PASS','scope':'all parameters alpha, including roots of unity; diagonal-base necessary charts',
 'checks':{'T4_constant_pivots':7,'swap_inner_gauge_constant_pivots':6,
 'diag_reflection_skew_derivations':'inner only, univariate unit coefficient ideals',
 'imaginary_resonance':'delta(x)=K*y^2 requires alpha=0',
 'quadratic_centralizer':'rank3 except alpha=2, rank2 there, axes and nonaxes'},
 'structural_steps':['global monic coverage','top tensor supplies a fixed linear vector','square completion','normal quartic obstruction at alpha=0','Ore Nakayama obstruction in Heisenberg case']}
Path(__file__).with_name('cubic_positive3_diagonal_monic_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS diagonal monic all-parameter derivation and centralizer certificates')
