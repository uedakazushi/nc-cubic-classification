#!/usr/bin/env python3
"""Replay every top-count/G-count support mask of the39 finite labels.
Uses exact Smith identities and actual integer obstruction witnesses.
"""
from pathlib import Path
import json,collections
from cubic_four_simple_support_sieve import replay,leftkern
records=replay();remaining=[r for r in records if r['compatible_support_masks']]
assert len(records)==39 and len(remaining)==20
assert sum(r['label_count'] for r in remaining)==45
assert sum(len(r['compatible_support_masks']) for r in records)==1306
assert sorted({r['N'] for r in remaining})==[5,6,7,8,9,12]
# Check every stored incompatibility independently of the Smith implementation.
for r in records:
 N=r['N'];a=r['exponents']
 for w in r['normalizer_witnesses']:
  A=[];b=[]
  for z in w['normal']:
   for v in w['S']+w['T']:
    A.append([v[e[1]] if z==e[0] else -v[e[0]] if z==e[1] else 0 for e in w['edges']]);b.append(a[z])
  l=w['integer_left_relation'];assert len(l)==len(A)
  assert all(sum(l[j]*A[j][k] for j in range(len(A)))==0 for k in range(len(w['edges'])))
  assert sum(l[j]*b[j] for j in range(len(b)))%N==w['rhs_modN']!=0
summary=[{'N':r['N'],'exponents':r['exponents'],'Galois_label_orbit_size':r['label_count'],'compatible_support_masks':len(r['compatible_support_masks'])} for r in remaining]
out={'status':'PASS','scope':'complete necessary all-support sieve on39 finite labels;20 Galois labels /45 root sets remain','input':'cubic_four_simple_finite_atlas_certificate.json','support_count':1306,'remaining_orders':[5,6,7,8,9,12],'remaining_Galois_labels':20,'remaining_root_sets':45,'all39_support_records':records,'final_necessary_labels':summary,'ordinary_lemmas':['normal linear mu_z=hdet(phi_z)','simultaneous diagonal eigenlifts for mu and all forced normalizers','full top/G count support masks, rankzero and pure-column domain pruning, matching rank upper bounds','common skew-normal or pureAS2 factors','linked u²z /vz² factor using uzskew and one vz/zv/u² relation','integer leftkernel monomial compatibility with reciprocal normal-generator commutation scalars'],'not_claimed':['compatible masks have a top with rank6','normal cubes exist on compatible masks','Galois label equivalence is intrinsic isomorphism','all20 labels contain H3','complete H3 classification','ordinary homological proofs mechanically checked']}
Path(__file__).with_name('cubic_four_simple_support_sieve_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all support masks;20 Galois labels /45 root sets;1306 necessary support pieces')
