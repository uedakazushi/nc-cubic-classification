#!/usr/bin/env python3
"""Replay the classification spectral certificates in dependency order.
PASS certifies these finite checks, not all ordinary proofs or H3 completeness.
"""
import json
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
CHECKS=[
 'verify_cubic_hypersurface_frame.py',
 'verify_cubic_spectral_resonance.py',
 'verify_cubic_spectral_ore_reduction.py',
 'verify_cubic_inverse_spectral_pencils.py',
 'verify_cubic_three_eigenvalue_finite_spectra.py',
 'verify_cubic_fifth_root_spectrum_exclusion.py',
 'verify_cubic_sixth_root_spectrum_reductions.py',
 'verify_cubic_fourth_root_spectrum_reductions.py',
 'verify_cubic_sixth_root_last_Ore_exclusion.py',
 'verify_cubic_fourth_root_negative_repeat_exclusion.py',
 'verify_cubic_fourth_root_unit_simple_rank1.py',
 'verify_cubic_detminus1_spectral_exclusion.py',
 'verify_cubic_fourth_root_unit_simple_rank2.py',
]
results=[]
for name in CHECKS:
    result=subprocess.run([sys.executable,str(ROOT/name)],capture_output=True,text=True)
    if result.returncode:
        print(result.stdout);print(result.stderr,file=sys.stderr)
        raise SystemExit(result.returncode)
    results.append({'validator':name,'status':'PASS'})
    print('PASS',name)
final=json.loads((ROOT/'cubic_fourth_root_unit_simple_rank2_certificate.json').read_text())
assert final['status']=='PASS' and final['final_spectrum_count']==11 and final['remaining_orders']==[3,4]
out={'status':'PASS','checks':results,'current_three_eigenvalue_necessary_spectra':11,
     'current_minimal_common_semisimple_orders':[3,4],
     'additional_four_simple_sector':'(a,-a,i/a,-i/a) excluded outside a^4=1; finite boundary unclassified',
     'not_claimed':['H3 existence or admissibility of11 spectra','ordinary proofs independently checked by program','four-eigenvalue or CY completeness','complete H3 classification']}
(ROOT/'cubic_spectral_reductions_validation.json').write_text(json.dumps(out,indent=2)+'\n')
