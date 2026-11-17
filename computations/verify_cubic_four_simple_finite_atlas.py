#!/usr/bin/env python3
"""Replay the entire finite scan and exact necessary reductions.
Requires a C++17 compiler; all arithmetic is integer, never numerical roots.
"""
from pathlib import Path
import tempfile,subprocess,json,math,collections,os
from cubic_four_simple_finite_model import prune,characters,factors
ROOT=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='nc_cubic_finite_') as td:
 exe=Path(td)/'scan';subprocess.run([os.environ.get('CXX','g++'),'-O3','-std=c++17',str(ROOT/'cubic_four_simple_finite_scan.cpp'),'-o',str(exe)],check=True)
 scan=json.loads(subprocess.run([str(exe)],capture_output=True,text=True,check=True).stdout)
assert scan['counts']=={'minimal_order_sets':62290587,'quadratic_collision':13359699,'cubic_resonance':2223885,'quartic_support':134703,'raw_rank4':5338,'frobenius_feasible':604}
orbits={}
for N,*a in scan['candidates']:
 canon=min(tuple(sorted(k*x%N for x in a)) for k in range(1,N) if math.gcd(k,N)==1);orbits.setdefault((N,*canon),0);orbits[(N,*canon)]+=1
assert len(orbits)==115
records=[];final=[];stats=collections.Counter()
for spec,count in sorted(orbits.items()):
 N,*a=spec;basis,active,stages,status=prune(N,a);rec={'spectrum':spec,'Galois_label_orbit_size':count,'top_dimension':len(basis),'representatives':[''.join('xybc'[j] for j in next(iter(ts))) for ts in basis],'domain_prune_stages':stages,'active_orbits':sorted(active),'prune_status':status}
 if status!='survives':stats[status]+=1;records.append(rec);continue
 good,bad=characters(N,a,12);rec['negative_character_witnesses']=bad;rec['characters_nonnegative_through12']=good
 if not good:records.append(rec);continue
 stats['character_survivor_orbits']+=1
 good,fac,vs=factors(N,a,basis,active,good);rec['cubic_exponents']=vs;rec['factor_exclusions']=fac;rec['remaining_relation_characters']=good
 if good:
  stats['factor_survivor_orbits']+=1
  if spec==(4,0,1,2,3):rec['prior_exclusion']='whole order4 three-rank proof';stats['prior_order4']+=1
  else:final.append({'N':N,'exponents':a,'Galois_label_orbit_size':count,'relation_characters':good})
 records.append(rec)
assert stats=={'degenerate or zero top':9,'multilinear skew':2,'character_survivor_orbits':69,'factor_survivor_orbits':40,'prior_order4':1}
assert len(final)==39 and sum(r['Galois_label_orbit_size'] for r in final)==145
assert sorted({r['N'] for r in final})==[5,6,7,8,9,10,11,12,13,14,15,18]
assert max(f['degree'] for r in records for f in r.get('negative_character_witnesses',[]))==12
out={'status':'PASS','scope':'complete necessary finite four-simple spectral atlas; not existence, admissibility or geometric quotient','scan_counts':scan['counts'],'Galois_label_orbits_before_top':115,'reduction_counts':dict(stats),'all115_orbit_checks':records,'remaining_Galois_label_orbits':39,'remaining_root_sets':145,'remaining_orders':[5,6,7,8,9,10,11,12,13,14,15,18],'final_necessary_atlas':final,'not_claimed':['Galois labels are intrinsic isomorphism classes','nonnegative characters through12 suffice for AS4','all39 root orbits have H3','normal incidence classified','full H3 classification','ordinary proofs independently mechanically checked']}
(ROOT/'cubic_four_simple_finite_atlas_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS complete integer scan; four-simple H3 necessary atlas39 Galois labels /145 root sets')
