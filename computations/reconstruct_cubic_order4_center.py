#!/usr/bin/env python3
"""Recover the full cubic center by exact finite evaluations with PROVED bounds.
See rem:order4-center-interpolation. Runs samples SEQUENTIALLY, preserves completed
cases, and atomically updates a small partial certificate after each case.
"""
import argparse,itertools,json,subprocess,sys
from pathlib import Path
import sympy as s
parser=argparse.ArgumentParser();parser.add_argument('--work-dir',type=Path,required=True);args=parser.parse_args();args.work_dir.mkdir(parents=True,exist_ok=True)
root=Path(__file__).parent;output=root/'cubic_order4_center_relation_certificate.json'
T,D,Z1,Z2,Z3=s.symbols('g D Z1 Z2 Z3');K=s.QQ.alg_field_from_poly(s.Poly(T**4-2,T));g=K.unit
monoms=[(d,i,j) for i,j in [(2,0),(1,1),(0,2)] for d in range(2)]+[(d,i,j) for i,j in [(1,0),(0,1)] for d in range(3)]+[(d,0,0) for d in range(5)]
points=[];rows=[]
for d,x,y in itertools.product(range(5),[-1,0,1,2],[-1,0,1,2]):
 row=[s.Integer(d)**e*s.Integer(x)**i*s.Integer(y)**j for e,i,j in monoms]
 if s.Matrix(rows+[row]).rank()>len(rows):points.append([d,x,y]);rows.append(row)
 if len(rows)==17:break
matrix=s.Matrix(rows);assert matrix.det()==18432
certificate={'version':'classification-v15','status':'partial evaluations, not yet a computed all-parameter cubic','degree_bound_proof':'papers/sections/cubic_order4_center.tex, rem:order4-center-interpolation; weights(r,D,Z)=(1,3,4), total12','unisolvent_points':points,'constant_coefficient_monomials':monoms,'constant_evaluation_determinant':'18432','completed_samples':[]}
def save():
 tmp=output.with_suffix('.tmp');tmp.write_text(json.dumps(certificate,indent=2)+'\n');tmp.replace(output)
for d,x,y in points:
 result=args.work_dir/f'sample_{d}_{x}_{y}_result.json';log=args.work_dir/f'sample_{d}_{x}_{y}.log'
 if not result.exists():
  print('starting exact case',d,x,y,flush=True)
  with log.open('w') as file:
   ret=subprocess.run([sys.executable,str(root/'verify_cubic_order4_center_sample.py'),'--D',str(d),'--z1',str(x),'--z2',str(y),'--work-dir',str(args.work_dir)],stdout=file,stderr=subprocess.STDOUT)
  if ret.returncode:save();raise RuntimeError('sample failed; inspect '+str(log))
 entry=json.loads(result.read_text());assert entry['minimum_polynomial_identity_verified'] and entry['power_rank']==3
 certificate['completed_samples'].append(entry);save();print('completed',len(certificate['completed_samples']),'of17',flush=True)
def cv(text):return K.new(s.Poly(s.sympify(text),T,domain=s.QQ).all_coeffs())
def txt(c):
 v=c.to_list();return str(s.factor(sum(s.Rational(str(a))*T**(len(v)-1-i) for i,a in enumerate(v))))
lead=json.loads((root/'cubic_order4_leading_center_certificate.json').read_text());leadmap={tuple(e):cv(c) for e,c in zip(lead['monomials'],lead['coefficients'])}
a=leadmap[(0,3,0)];b=leadmap[(1,1,1)];c=leadmap[(3,0,0)]
spaces=[[(0,0,0),(1,0,0)],[(d,i,j) for i,j in [(1,0),(0,1)] for d in range(2)]+[(d,0,0) for d in range(3)],monoms]
values=[[],[],[]]
for point,entry in zip(points,certificate['completed_samples']):
 d,x,y=point;v=list(map(cv,entry['minimum_polynomial_coefficients']));values[0].append(v[1]);values[1].append(v[2]-b*x*y);values[2].append(v[3]-c*x**3-a*y**3)
polys=[];coefficient_records=[]
for space,target in zip(spaces,values):
 A=s.Matrix([[s.Integer(d)**e*s.Integer(x)**i*s.Integer(y)**j for e,i,j in space] for d,x,y in points]);_,selected=A.T.rref();assert len(selected)==len(space)
 inv=A[list(selected),:].inv();coeff=[sum((K.convert(inv[i,j])*target[selected[j]] for j in range(len(space))),K.zero) for i in range(len(space))]
 for r,truth in zip(A.tolist(),target):assert sum((K.convert(q)*v for q,v in zip(r,coeff)),K.zero)==truth
 polys.append(sum(s.sympify(txt(q))*D**d*Z1**i*Z2**j for q,(d,i,j) in zip(coeff,space)));coefficient_records.append([{'exponents':list(e),'coefficient':txt(q)} for e,q in zip(space,coeff)])
F=Z3**3+s.sympify(txt(a))*Z2**3+s.sympify(txt(c))*Z1**3+s.sympify(txt(b))*Z1*Z2*Z3+polys[0]*Z3**2+polys[1]*Z3+polys[2]
certificate.update({'status':'complete exact cubic recovered by proved finite coefficient spaces','coefficient_blocks':coefficient_records,'center_cubic':str(s.expand(F)),'leading_cubic':leadmap and {'Z2^3':txt(a),'Z1*Z2*Z3':txt(b),'Z1^3':txt(c),'Z3^3':'1'},'verification':'All17 exact48-dimensional sample matrices satisfy their cubic identities and have power-rank3; interpolation matrices full rank; ordinary pre-proved weight bound gives the full-parameter identity.'});save();print('FULL CENTER CUBIC RECONSTRUCTED',flush=True)
