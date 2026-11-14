#!/usr/bin/env python3
"""Check current surface manuscript closure and finite certificate metadata.
This does not re-run the exact computations or certify categorical proofs.
"""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
seen={}
def visit(path):
    if path in seen:return
    text=re.sub(r'(?<!\\)%[^\n]*','',(root/path).read_text(encoding='utf8'))
    seen[path]=text
    for name in re.findall(r'\\input\{([^}]+)\}',text):
        visit(name if name.endswith('.tex') else name+'.tex')
visit('papers/cubic_surface_ambient_moduli.tex')
text='\n'.join(seen.values())
labels=re.findall(r'\\label\{([^}]+)\}',text)
refs=re.findall(r'\\(?:eqref|ref|autoref|pageref)\{([^}]+)\}',text)
bib=re.findall(r'\\bibitem\{([^}]+)\}',text)
cites=[a.strip() for s in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}',text) for a in s.split(',')]
assert len(labels)==len(set(labels)), 'duplicate label'
assert len(bib)==len(set(bib)), 'duplicate bibliography key'
assert not set(refs)-set(labels),set(refs)-set(labels)
assert not set(cites)-set(bib),set(cites)-set(bib)
a=json.loads((root/'computations/r13_potential_certificate.json').read_text())
assert (a['rank_T'],a['rank_orbit_GL4_four_factors'],a['rank_seven_slice_with_orbit'])==(188,61,68)
for name in ('rank_condition_differential','orbit','family_with_orbit','seven_slice_with_orbit'):
    c=a[name];assert len(c['rows_zero_based'])==len(c['columns_zero_based'])==c['rank']
b=json.loads((root/'computations/surface_incidence_certificate.json').read_text())
for name in ('jacobian_incidence_differential','projective_orbit_differential','full_unimodular_poisson_linearization','two_factor_graph_stabilizer'):
    c=b[name];assert len(c['rows_zero_based'])==len(c['columns_zero_based'])==c['rank']
print(f'PASS {len(seen)} TeX sources; {len(labels)} unique labels; {len(refs)} refs; {len(bib)} bibliography entries; {len(cites)} citations; certificate dimensions')
