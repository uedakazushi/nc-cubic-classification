import sys,json,itertools,math,collections
from pathlib import Path

import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from cubic_four_simple_finite_model import top_basis as ibasis
from cubic_diagonal_top import top_basis,top_matrix
root=Path(__file__).resolve().parent
D=json.loads((root/'cubic_four_simple_orbit_torus_certificate.json').read_text());S=json.loads((root/'cubic_four_simple_support_sieve_certificate.json').read_text());src={(r['N'],*r['exponents']):r for r in S['all39_support_records']};out=[];seen={};coverage=[]
for rec in D['all20_label_records']:
 if rec.get('ordinary_exclusion'):continue
 N=rec['N'];a=rec['exponents'];ib=ibasis(N,a)
 for ip,pat in enumerate(rec['patterns']):
  act=pat['active_indices'];C=s.Matrix([[next(iter(ib[j])).count(k) for j in act] for k in range(4)]);gauge=C.rref()[1]
  for case in pat['cubic_masks']:
   dim=case['effective_dimension']
   if not dim:continue
   assert all(x==0 for x in s.Matrix(case['A'])*C.T) and C.rank()==case['diagonal_rank'] and len(act)-s.Matrix(case['A']).rank()-C.rank()==dim
   A=case['A']+[[int(k==j) for k in range(len(act))] for j in gauge];b=case['b']+[0]*len(gauge)
   dm=DomainMatrix.from_Matrix(s.Matrix(A)).convert_to(s.ZZ).to_dense();dd,u,v=smith_normal_decomp(dm);assert u.matmul(dm).matmul(v)==dd and abs(u.det())==1 and abs(v.det())==1
   ds=[int(dd[j,j].element) for j in range(min(dd.shape)) if dd[j,j]];r=len(ds);assert len(act)-r==dim
   ub=[sum(int(x)*y for x,y in zip(row,b))%(2*N) for row in u.to_list()];assert not any(ub[r:]);vv=[list(map(int,row)) for row in v.to_list()];L=2*N*math.lcm(*map(abs,ds));ids=[]
   for ks in itertools.product(*(range(abs(d)) for d in ds)):
    ep=[sum(vv[j][i]*(ub[i]+2*N*ks[i])*(L//(2*N*ds[i])) for i in range(r))%L for j in range(len(act))];mu=[L//N*x for x in a];g=math.gcd(L,*ep,*mu);LL=L//g;ep=[x//g for x in ep];mu=[x//g for x in mu];free=[row[r:] for row in vv]
    key=(N,tuple(a),tuple(act),LL,tuple(ep),tuple(map(tuple,free)),pat['character_index'])
    if key not in seen:
     seen[key]=len(out);out.append({'N':N,'spectrum':a,'active_indices':act,'root_order':LL,'coefficient_phases':ep,'Nakayama_exponents':mu,'free_exponents':free,'dimension':dim,'character':src[N,*a]['relation_characters'][pat['character_index']]})
    ids.append(seen[key])
   coverage.append({'N':N,'spectrum':a,'pattern_index':ip,'cubic_mask':case['cubic_mask'],'gauge_columns':list(gauge),'Smith_diagonal':ds,'branch_ids':sorted(set(ids))})
assert len(coverage)==75
print('COVER',len(out),collections.Counter((x['N'],x['dimension']) for x in out),flush=True)
for i,p in enumerate(out):
 z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(p['root_order'],z),z));ts=s.symbols('t1:'+str(p['dimension']+1));K=F.frac_field(*ts);zz=K.convert(F.unit,F);tt=K.gens;lam=[zz**e for e in p['Nakayama_exponents']];co=[K.zero]*len(top_basis(K,lam))
 for j,phase,powers in zip(p['active_indices'],p['coefficient_phases'],p['free_exponents']):
  val=zz**phase
  for t,e in zip(tt,powers):val*=t**e
  co[j]=val
 H=top_matrix(K,lam,co);constraints=[];native=[]
 for w,rank in enumerate(p['character']):
  ids=[4*j+k for j in range(4) for k in range(4) if (p['spectrum'][j]+p['spectrum'][k])%p['N']==w]
  cols=[4*j+k for j in range(4) for k in range(4) if (p['spectrum'][j]+p['spectrum'][k])%p['N']==(-w)%p['N']]
  for rr in itertools.combinations(ids,rank+1):
   for cc in itertools.combinations(cols,rank+1):
    val=H.extract(rr,cc).det()
    if val:
     constraints.append(str(K.to_sympy(val))); pp=val.numer; mins=tuple(min(e[j] for e in pp) for j in range(p['dimension'])); pp=pp.exquo(pp.ring.from_dict({mins:F.one})).monic(); native.append(pp)
 p['nonzero_rank_constraints']=sorted(set(constraints));
 if not native:p['rank_locus']='whole torus'
 elif i==6:
  witnesses=[(j,k,native[j]-native[k]) for j in range(len(native)) for k in range(j) if (native[j]-native[k]).is_ground and native[j]!=native[k]];assert witnesses;p['rank_locus']='empty';p['constant_difference_witness']=[witnesses[0][0],witnesses[0][1],str(witnesses[0][2].as_expr())]
 else:
  g=native[0]
  for q in native[1:]:g=g.gcd(q)
  g=g.monic();assert any(q==g for q in native) and all(not q.rem(g) for q in native);p['rank_locus']='principal';p['rank_equation']=str(g.as_expr());p['rank_equation_native']=[[list(ex),list(map(str,c.to_list()))] for ex,c in sorted(g.to_dict().items())]
 p['generic_top_rank']=H.rank();print(i,p['N'],p['dimension'],p['generic_top_rank'],len(p['nonzero_rank_constraints']),flush=True)
assert len(out)==16 and sum(p['rank_locus']=='empty' for p in out)==1
(root/'cubic_four_simple_positive_rank_certificate.json').write_text(json.dumps({'status':'PASS','scope':'all75 positive toric support pieces, all gauge torsion branches and original top rank equations; normal cubic incidence unresolved','branches':out,'support_coverage':coverage},indent=2)+'\n')
print('PASS all75 support pieces,16 gauge branches, all original top rank loci')
