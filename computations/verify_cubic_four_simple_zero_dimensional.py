#!/usr/bin/env python3
"""Every Smith component of every zero-dimensional diagonal torus quotient,
followed by exact cyclotomic graded/normal calculations (no finite fields).
"""
from pathlib import Path
import json,itertools,math,collections,sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from cubic_diagonal_top import top_basis,top_matrix
from cubic_incremental_graded import GradedAlgebra
from cubic_four_simple_finite_model import top_basis as integer_top_basis
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_four_simple_orbit_torus_certificate.json').read_text());assert D['status']=='PASS' and D['remaining_Galois_labels']==12
points=[];seen={};coverage=[];positive=[]
for rec in D['all20_label_records']:
 if rec.get('ordinary_exclusion'):continue
 N=rec['N'];a=rec['exponents']
 for ip,pat in enumerate(rec['patterns']):
  act=pat['active_indices']
  for case in pat['cubic_masks']:
   if case['effective_dimension']:
    positive.append({'N':N,'exponents':a,'label_count':rec['label_count'],'pattern_index':ip,'cubic_mask':case['cubic_mask'],'effective_dimension':case['effective_dimension']});continue
   A=case['A'];b=case['b'];dm=DomainMatrix.from_Matrix(s.Matrix(A)).convert_to(s.ZZ).to_dense();DD,U,V=smith_normal_decomp(dm);assert U.matmul(dm).matmul(V)==DD and abs(U.det())==1 and abs(V.det())==1
   rank=sum(bool(DD[j,j].element) for j in range(min(DD.shape)));diags=[int(DD[j,j].element) for j in range(rank)];ub=[sum(int(x)*y for x,y in zip(row,b))%(2*N) for row in U.to_list()];vv=[list(map(int,row)) for row in V.to_list()];assert all(x==0 for x in ub[rank:])
   # Reconstruct coefficient weights and the full connected diagonal action.
   # The original orbit representatives, independent of coefficient values.
   ib=integer_top_basis(N,a);C=s.Matrix([[next(iter(ib[j])).count(k) for j in act] for k in range(4)])
   assert all(x==0 for x in s.Matrix(A)*C.T) and C.rank()==len(act)-rank
   L=2*N*math.lcm(*map(abs,diags));ids=[]
   for ks in itertools.product(*(range(abs(d)) for d in diags)):
    exps=[sum(vv[j][i]*(ub[i]+2*N*ks[i])*(L//(2*N*diags[i])) for i in range(rank))%L for j in range(len(act))];mu=[(L//N)*v for v in a]
    g=math.gcd(L,*exps,*mu);LL=L//g;ep=tuple(v//g for v in exps);mp=tuple(v//g for v in mu);key=(N,LL,tuple(act),ep,mp)
    if key not in seen:seen[key]=len(points);points.append({'N':N,'spectrum':a,'active_indices':act,'root_order':LL,'coefficient_exponents':ep,'Nakayama_exponents':mp})
    ids.append(seen[key])
   coverage.append({'N':N,'exponents':a,'pattern_index':ip,'cubic_mask':case['cubic_mask'],'Smith_diagonal':diags,'diagonal_action_rank':int(C.rank()),'representative_point_ids':sorted(set(ids))})
assert len(coverage)==81 and len(points)==30 and len(positive)==75
fields={};statuses=collections.Counter();cone_count=0
for pt in points:
 L=pt['root_order']
 if L not in fields:
  z=s.Symbol('z');fields[L]=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(L,z),z))
 F=fields[L];z=F.unit;lam=[z**e for e in pt['Nakayama_exponents']];basis=top_basis(F,lam);co=[F.zero]*len(basis)
 for j,e in zip(pt['active_indices'],pt['coefficient_exponents']):co[j]=z**e
 H=top_matrix(F,lam,co);assert H.rank()==6
 piv=H.rref()[1];cc=H.transpose().to_list();rels=[{divmod(j,4):c for j,c in enumerate(cc[k]) if c} for k in piv];assert len(rels)==6
 B=GradedAlgebra(F,4,rels,pt['spectrum']);B.build(4);dims=[len(B.basis[j]) for j in range(5)];pt['dimensions']=dims
 if dims[3]!=20 or dims[4]!=35:
  assert dims[3:]==[22,46];pt['exclusion']='nonAS4_Hilbert';statuses[pt['exclusion']]+=1;continue
 ids=[j for j,w in enumerate(B.basis[3]) if sum(pt['spectrum'][v] for v in w)%pt['N']==0];cols=[]
 for j in ids:
  col={}
  for k in range(4):
   row=dict(B.right[4][j,k]);B.addto(row,B.left[4][k,j],-F.one/lam[k])
   for r,c in row.items():col[k*len(B.basis[4])+r]=c
  cols.append(col)
 rows=sorted(set().union(*(set(c) for c in cols))) if cols else[];M=DomainMatrix.from_dod({i:{j:c[r] for j,c in enumerate(cols) if r in c} for i,r in enumerate(rows)},(len(rows),len(cols)),F);nr=M.rank();pt['normal_shape']=list(M.shape);pt['normal_rank']=nr
 if nr==len(cols):pt['exclusion']='normal_kernel_zero';statuses[pt['exclusion']]+=1;continue
 assert pt['N']==9 and pt['spectrum']==[0,1,4,7] and len(cols)-nr==1
 null=M.nullspace().to_list();assert len(null)==1
 assert all(0 not in B.basis[3][ids[j]] for j,c in enumerate(null[0]) if c)
 pt['normal_basis']=[{''.join('xybc'[i] for i in B.basis[3][ids[j]]):list(map(str,c.to_list())) for j,c in enumerate(v) if c} for v in null]
 pure=[r for r in rels if all(0 not in w for w in r)];mixed=[r for r in rels if r not in pure];assert len(pure)==len(mixed)==3
 sigma={}
 for r in mixed:
  letters={i for w in r for i in w if i!=0};assert len(letters)==1;k=letters.pop();assert set(r)=={(0,k),(k,0)} and r[0,k] and r[k,0];sigma[k]=-r[k,0]/r[0,k]
 assert set(sigma)=={1,2,3} and all(c==z**6 for c in sigma.values())
 PM=DomainMatrix.from_dod({i:{j:r.get(divmod(i,4),F.zero) for j,r in enumerate(pure) if r.get(divmod(i,4),F.zero)} for i in range(16)},(16,3),F).to_dense()
 for r in pure:
  image={w:c*sigma[w[0]]*sigma[w[1]] for w,c in r.items()};v=DomainMatrix.from_dod({4*w[0]+w[1]:{0:c} for w,c in image.items()},(16,1),F).to_dense();assert PM.hstack(v).rank()==3
 pt['sigma_on_base']=[list(map(str,sigma[k].to_list())) for k in [1,2,3]];pt['exclusion']='existing_skew_cone_vertex_lemma';pt['ordinary_lemma']='lem:cubic-skew-cone-vertex';cone_count+=1;statuses[pt['exclusion']]+=1
assert statuses=={'normal_kernel_zero':26,'nonAS4_Hilbert':3,'existing_skew_cone_vertex_lemma':1}
labels={}
for r in positive:labels.setdefault((r['N'],*r['exponents']),r['label_count'])
assert len(labels)==5 and sum(labels.values())==10
out={'status':'PASS','scope':'all81 zero-dimensional necessary toric support pieces excluded; five positive-dimensional necessary spectral labels remain','zero_dimensional_piece_count':81,'all_Smith_component_cover':coverage,'algebraic_point_count':30,'cyclotomic_root_orders':sorted(fields),'all30_exact_points':points,'exclusion_counts':dict(statuses),'remaining_positive_support_pieces':positive,'remaining_Galois_labels':5,'remaining_root_sets':10,'final_necessary_labels':[{'N':k[0],'exponents':list(k[1:]),'label_count':v} for k,v in sorted(labels.items())],'ordinary_proof_inputs':['integer Smith representatives with every finite component','rankC equals torus free dimension, diagonal action transitive on each connected component over algebraically closed field','all coefficient/generator weights A Ctranspose0','exact QQ(cyclotomic) images and graded quotient modules','existing arbitrary-automorphism skew-cone vertex lemma for unique remaining cubic'],'not_claimed':['finite-field tests used as proof','all positive-dimensional pieces AS4 or have normal cubic','Galois labels geometric quotient','complete H3 classification','ordinary descent or cone lemma mechanically proved in entirety']}
(ROOT/'cubic_four_simple_zero_dimensional_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS all30 exact cyclotomic points; five Galois labels /10 root sets remain')
