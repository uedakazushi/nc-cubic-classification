"""Whole s=0 and t=0 residual surfaces: exact localized module membership and non-AS4 points."""
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
for name,sub,variables,unit in [('szero',{s:0},(r,t),r*(r*r-1)*(1-r*r-t*t)*delta),('tzero',{t:0},(r,s),r*(r*r-1)*((r+1)**2+s*s))]:
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
 tests=['E'] if name=='tzero' else ['(t+1)*E','(r^2+1)*E']
 for i,expr in enumerate(tests):source+=f'module T{i}={expr};\nmodule V{i}=reduce(T{i},GN);\nif(size(V{i})!=0){{print("FAILED MEMBERSHIP");quit;}}\nprint("MEMBERSHIP {i} PASS");\n'
 source+='print("SURFACE PASS");\nquit;\n'
 with tempfile.TemporaryDirectory(prefix='secant-module-') as tmp:
  script=Path(tmp)/'proof.sing';script.write_text(source);result=subprocess.run([singular,'-q',str(script)],capture_output=True,text=True,check=False)
 assert result.returncode==0 and 'SURFACE PASS' in result.stdout and 'NORMAL ROW CONTAINMENT PASS' in result.stdout and 'FAILED' not in result.stdout and '?' not in result.stdout,(result.stdout,result.stderr)
 records.append({'surface':name,'localization_unit':str(unit),'checks':'E=ker(R3), normal rows lie in E; E contained in N' if name=='tzero' else '(t+1)E and (rho2+1)E contained in normal row module','source_reconstructed_from':'all original quadratic relations and checked polynomial quartic annihilators'})
# The only remaining geometric points on s0, including conjugate rho=-i.
R=relations(S.Matrix([[0,S.I],[S.I,0]]),[1,1,0,0,-1,1]);_,_,f3,_=quotient(R,3,S.QQ_I);_,_,f4,_=quotient(R,4,S.QQ_I);assert len(f3)==20 and len(f4)==36
out={'status':'PASS','surfaces':records,'finite_remainder':'s0,t=-1,rho=+/-i: exact B3dim20/B4dim36, not AS4','mathematical_input':'on AS4 maximal-rank R3 locus, the kernel module specializes to the full positive cubic dual. Membership in the polynomial normal-row module forces all normal cubic classes zero. Unit factors a and delta were already excluded.','conclusion':'entire two coordinate planes s=0,t=0 have no H3; main residual support is mirror rho2-2t-1=0 or L=0','dependencies':['SymPy exact arithmetic','Singular standard-basis and syzygy algorithms; SINGULAR_BIN may specify executable'],'not_claimed':['mirror or L surfaces','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_coordinate_planes_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS entire s0 and t0 secant residual surfaces: original annihilators, localized module membership, and non-AS4 Gaussian points')
