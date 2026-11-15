#!/usr/bin/env python3
"""Export optional Singular output; the independent validator proves identities.
Usage: python computations/export_cubic_as4_T_centre_lift.py LOG SCALES_JSON OUTPUT_JSON
"""
import json,sys
from pathlib import Path
log,scales,output=map(Path,sys.argv[1:]);s=log.read_text()
assert s.rstrip().endswith('DONE') and '?' not in s and 'FAIL' not in s and 'int division' not in s
out={'meaning':'C is the transpose of the polynomial-numerator commutator map on all 64 cubic words, with each column divided by its listed scale. Each scale divides verified D4. Polynomial identity C*X=N and triangular pivots certify rank20 away from their zero loci; independent replay does not trust Groebner-basis correctness.','column_scales':json.loads(scales.read_text()),'pivots':[],'N':[],'X':[]}
for line in s.splitlines():
    if line.startswith('PIV:'):
        _,j,p=line.split(':');out['pivots'].append([int(j),int(p)])
    elif line.startswith(('N:','X:')):
        key,i,j,e=line.split(':',3);out[key].append([int(i),int(j),e])
assert len(out['pivots'])==20
output.write_text(json.dumps(out,separators=(',',':'))+'\n')
print('exported rank witness',output.stat().st_size,'bytes')
