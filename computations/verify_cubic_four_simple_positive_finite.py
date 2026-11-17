import sys,json,sympy as s
from pathlib import Path
ROOT=Path(__file__).resolve().parent
from cubic_diagonal_top import top_basis,top_matrix
from cubic_incremental_graded import GradedAlgebra
from sympy.polys.matrices import DomainMatrix
D=json.loads((ROOT/'cubic_four_simple_positive_rank_certificate.json').read_text());assert D['status']=='PASS';out=[]
linear={1:(-2,4),2:(-2,4),4:(-2,7),5:(2,7),11:(2,9),12:(-2,9),14:(-2,11),15:(2,11)}
for i in [1,2,4,5,8,9,11,12,14,15]:
 p=D['branches'][i];L=24 if i in [8,9] else p['root_order'];z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(L,z),z));w=F.unit;zz=w**(L//p['root_order']);choices=[sgn*(w**11+w**5) for sgn in [1,-1]] if i in [8,9] else [linear[i][0]*zz**linear[i][1]]
 assert max(ex[0] for ex,coeff in p['rank_equation_native'])==len(choices) and len(set(choices))==len(choices)
 for tv in choices:
  assert tv
  equation=F.zero
  for ex,coeff in p['rank_equation_native']:
   c=F.zero
   for v in coeff:c=c*zz+F.convert(s.Rational(v))
   equation+=c*tv**ex[0]
  assert not equation
  lam=[zz**e for e in p['Nakayama_exponents']];co=[F.zero]*len(top_basis(F,lam))
  for j,phase,ex in zip(p['active_indices'],p['coefficient_phases'],p['free_exponents']):co[j]=zz**phase*tv**ex[0]
  H=top_matrix(F,lam,co);rank=H.rank();assert rank==6
  piv=H.rref()[1];cc=H.transpose().to_list();rels=[{divmod(j,4):c for j,c in enumerate(cc[k]) if c} for k in piv];B=GradedAlgebra(F,4,rels,p['spectrum']);B.build(4);dims=[len(B.basis[j]) for j in range(5)];rec={'branch':i,'root_order':L,'parameter_value':list(map(str,tv.to_list())),'dims':dims}
  if dims[3:]==[20,35]:
   ids=[j for j,word in enumerate(B.basis[3]) if sum(p['spectrum'][v] for v in word)%p['N']==0];cols=[]
   for j in ids:
    col={}
    for k in range(4):
     row=dict(B.right[4][j,k]);B.addto(row,B.left[4][k,j],-F.one/lam[k])
     for r,c in row.items():col[k*len(B.basis[4])+r]=c
    cols.append(col)
   rows=sorted(set().union(*(set(c) for c in cols))) if cols else [];M=DomainMatrix.from_dod({j:{k:c[r] for k,c in enumerate(cols) if r in c} for j,r in enumerate(rows)},(len(rows),len(cols)),F);rec['normal_shape']=list(M.shape);rec['normal_rank']=M.rank();rec['nullity']=len(cols)-M.rank()
  print('POINT',rec,flush=True);out.append(rec)
assert len(out)==12 and all(r['dims'][3:]==[20,35] and r['nullity']==0 for r in out)
assert {i for i,p in enumerate(D['branches']) if p['dimension']==1 and p['rank_locus']=='principal'}==set(linear)|{8,9}
(ROOT/'cubic_four_simple_positive_finite_certificate.json').write_text(json.dumps({'status':'PASS','scope':'all12 finite parameter representatives from positive toric pieces excluded by exact normal kernel','all12_points':out,'remaining_curve_branch_ids':[0,3,7,10,13],'remaining_Galois_labels':4,'remaining_root_sets':9},indent=2)+'\n')
print('PASS all12 finite representatives excluded; five necessary curves remain')
