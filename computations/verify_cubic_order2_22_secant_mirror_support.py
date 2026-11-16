"""Mirror residual support and complete first-curve exclusion by exact module and polynomial certificates."""
import itertools,json,os,subprocess,tempfile
from pathlib import Path
import sympy as S
from cubic_order2_22_secant_functionals import normal_matrix,RHO,SIGMA,TAU
from cubic_order2_22_secant_tools import relations,quotient
r,s,t=RHO,SIGMA,TAU
N=normal_matrix(['cubic_order2_22_secant_main_functionals_input.json','cubic_order2_22_secant_additional_functionals_input.json']);P=N.domain
alpha=(r-1)/(r+1);R=relations(S.Matrix([[0,r],[r,0]]),[1-r*r-t*t-alpha*s*s,-t,alpha*s,s,t,1]);words=[w for w in itertools.product(range(4),repeat=3) if sum(i>=2 for i in w)%2==0];index={w:i for i,w in enumerate(words)};R3=[]
for rel in R:
 for pos in range(2):
  for g in range(4):
   row={}
   for w,c in rel.items():
    word=(g,)+w if pos==0 else w+(g,)
    if word in index:row[index[word]]=P.from_sympy(S.cancel(c*(r-1)*(r+1)**2))
   if row:R3.append(row)
assert len(R3)==24
A=(r+1)*(1-r*r-t*t)-(r-1)*s*s;delta=r*r+2*t-1;records=[];singular=os.environ.get('SINGULAR_BIN','Singular')
for name,sub,variables,unit in [('mirror',{t:(r*r-1)/2},(r,s),r*(r*r-1)*((r+1)**2*(r*r+3)+4*s*s))]:
 Q=S.QQ.poly_ring(*variables);unit=Q.from_sympy(S.expand(unit.subs(sub)));factors=[Q.from_sympy(S.sympify(x).subs(sub)) for x in [r,r-1,r+1,A,delta]];factors=[f for f in factors if f and f.degree()>0]
 def transform(rows):
  out=[]
  for row in rows:
   data={j:Q.from_sympy(S.expand(P.to_sympy(v).subs(sub))) for j,v in row.items()};data={j:v for j,v in data.items() if v}
   if not data:continue
   for f in factors:
    while all(v.rem(f)==0 for v in data.values()):data={j:v.exquo(f) for j,v in data.items()}
   out.append(data)
  return out
 rels=transform(R3);norm=transform(list(N.to_dod().values()))
 def matrix(label,n,m,data):return f'matrix {label}[{n}][{m}]=\n'+',\n'.join(str(data.get(i,{}).get(j,Q.zero)).replace('**','^') for i in range(n) for j in range(m))+';\n'
 source='ring R=0,('+','.join(map(str,variables))+',z),dp;\npoly U='+str(unit).replace('**','^')+';\nideal I=z*U-1;\nqring Q=std(I);\n'
 source+=matrix('R3',len(rels),32,{i:row for i,row in enumerate(rels)})
 source+=matrix('Nall',32,len(norm),{j:{i:row[j] for i,row in enumerate(norm) if j in row} for j in range(32)})
 source+='ideal Zero=std(ideal(0));\nmatrix Ch=R3*Nall;\nideal Ch0=reduce(ideal(Ch),Zero);\nif(size(Ch0)!=0){print("FAILED NORMAL ROWS");quit;}\nprint("NORMAL ROW CONTAINMENT PASS");\nmodule E=syz(R3);\nmatrix CK=R3*E;\nideal CK0=reduce(ideal(CK),Zero);\nif(size(CK0)!=0){print("FAILED SYZYGY");quit;}\nmodule NN=Nall;\nmodule GN=std(NN);\n'
 tests=['(4*s^2+(r-1)*(r+1)^3)*(4*r^2*s^2+(r+1)^2*(r^2+1)^2)*E']
 for i,expr in enumerate(tests):source+=f'module T{i}={expr};\nmodule V{i}=reduce(T{i},GN);\nif(size(V{i})!=0){{print("FAILED MEMBERSHIP");quit;}}\nprint("MEMBERSHIP {i} PASS");\n'
 source+='print("SURFACE PASS");\nquit;\n'
 with tempfile.TemporaryDirectory(prefix='secant-module-') as tmp:
  script=Path(tmp)/'proof.sing';script.write_text(source);result=subprocess.run([singular,'-q',str(script)],capture_output=True,text=True,check=False)
 assert result.returncode==0 and 'SURFACE PASS' in result.stdout and 'NORMAL ROW CONTAINMENT PASS' in result.stdout and 'FAILED' not in result.stdout and '?' not in result.stdout,(result.stdout,result.stderr)
 records.append({'surface':name,'verified':'Bm4*J6*ker(R3) is contained in the normal-row module'})

# A separate rational parameter covers the complete Bm4=0 curve.
w=S.symbols('w');rho=(1-w*w)/(1+w*w);sv=2*w/(1+w*w)**2;tv=-2*w*w/(1+w*w)**2;av=4*w*w/(1+w*w)**2
R=relations(S.Matrix([[0,rho],[rho,0]]),[av,-tv,S.cancel((rho-1)/(rho+1)*sv),sv,tv,1]);P=S.QQ.poly_ring(w);base=S.Poly(w*(w*w-1)*(w*w+1),w)
rows=[]
for rel in R:
 den=S.lcm([S.denom(S.cancel(c)) for c in rel.values()]);left=S.Poly(den,w)
 while left.degree()>0:
  g=S.gcd(left,base);assert g.degree()>0;left=left.exquo(g)
 rows.append({word:P.from_sympy(S.cancel(c*den)) for word,c in rel.items()})
entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_mirror_B_input.json').read_text());funcs=[{int(i):P.from_sympy(S.sympify(v,locals={'w':w})) for i,v in row.items()} for row in entry['functionals'].values()]
words4=list(itertools.product(range(4),repeat=4));idx4={word:i for i,word in enumerate(words4)}
for lam in funcs:
 for rel in rows:
  for pos in range(3):
   for extra in itertools.product(range(4),repeat=2):assert not sum((c*lam.get(idx4[extra[:pos]+word+extra[pos:]],P.zero) for word,c in rel.items()),P.zero)
data={}
for a,lam in enumerate(funcs):
 for g in range(4):
  row={j:lam.get(idx4[word+(g,)],P.zero)+(-1 if g<2 else 1)*lam.get(idx4[(g,)+word],P.zero) for j,word in enumerate(words)};row={j:c for j,c in row.items() if c}
  if row:data[4*a+g]=row
from sympy.polys.matrices import DomainMatrix
NM=DomainMatrix(data,(4*len(funcs),32),P);rec=entry['normal_minor'];det=NM.extract(rec['rows'],rec['cols']).det();assert det
allowed=P.from_sympy(w*(w*w-1)*(w*w+1)*(w**4-w*w+1));left=det
while left.degree()>0:
 g=left.gcd(allowed);assert g.degree()>0;left=left.exquo(g)
J=4*rho*rho*sv*sv+(rho+1)**2*(rho*rho+1)**2;assert S.cancel(J-16*(w**4-w*w+1)/(1+w*w)**4)==0
r,s,t=RHO,SIGMA,TAU;L=r**5+r**4+2*r**3*s*s+2*r**3*t*t-2*r*r*s*s+2*r*r*t*t+2*r*t*t-r+2*t*t-1;J=4*r*r*s*s+(r+1)**2*(r*r+1)**2
assert S.cancel(L.subs(t,(r*r-1)/2)-(r-1)*J/2)==0
out={'status':'PASS','mirror_support':'localized exact module inclusion Bm4*J6*ker(R3) subset normal-row module','Bm4_curve':'complete rational parameter rho=(1-w2)/(1+w2), s=2w/(1+w2)2, t=-2w2/(1+w2)2; parameter w(w2-1)(w2+1)!=0; polynomial original-relation annihilators and normal10minor exclude w4-w2+1!=0','Bm4_exception':'all remaining w4-w2+1 roots lie on J6=0 by exact rational identity','conclusion':'mirror candidates lie on J6=0 and hence L=0. Together with coordinate-plane and open exclusions, all remaining both-top-nonzero mixed4 (2,2) H3 candidates lie on the single L=0 surface.','remaining':['normal cuts on J6 mirror curve','nonmirror L=0 surface','global H3 classification','relative intrinsic descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_mirror_support_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS mirror support reduced to J6: exact module membership, complete Bm4 curve and polynomial normal10minor; main residual is L0 only')
