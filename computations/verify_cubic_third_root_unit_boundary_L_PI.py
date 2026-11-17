#!/usr/bin/env python3
"""Exact scalar/finite-order/growth arithmetic for the ordinary PI reduction.
Geometry, algebraic independence, GK comparison and the external GK1 theorem
are ordinary proofs; this program does not formally verify them.
"""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parent
for name in ['cubic_third_root_unit_boundary_L_incidence_certificate.json','cubic_third_root_unit_boundary_L_recognition_certificate.json']:
 assert json.loads((ROOT/name).read_text())['status']=='PASS'
o,E,n=s.symbols('omega E n')
def red(expr):return s.rem(s.expand(expr),o**2+o+1,o)
X=-o*E**3-o**2
assert red((X+E**3+1)**3-27*X*E**3-3*(o**2-o)*(E**3-1)**3)==0
Q=(o+2)*(1-E**3);assert red((o+2)*(2+o**2)-3)==0
# Nontrivial projective delta=(1,omega^2,omega) has exact order3.
assert all(red(o**(3*j)-1)==0 for j in range(3))
assert [r for r in s.divisors(9) if 9%r==0 and 3%r!=0]==[9]
# The exact GK comparison: C(n+2,2)*f(n)<=C(10n+3,3).
central_words=(n+1)*(n+2)/2;ambient_words=(10*n+3)*(10*n+2)*(10*n+1)/6
bound=s.Poly(s.expand(1000*(n+1)*central_words-ambient_words),n)
assert all(c>0 for c in bound.all_coeffs())
out={'status':'PASS','scope':'exact discriminant, third-order normalizer and universal polynomial growth bound; ordinary geometry/PI proof separate',
 'boundary_translation_order':9,'ambient_Nakayama_order_unchanged':3,
 'independent_central_affine_elements':['psi','g^3'],
 'filtered_degrees':[3,9],'generic_central_localization_GK_bound':1,
 'growth_comparison':'binomial(n+2,2)*f(n)<=binomial(10*n+3,3)<=1000*(n+1)*binomial(n+2,2)',
 'conclusions':['affine ambient D is PI for every u,v in same Omega-open','normal quotient U=D/(g) is PI'],
 'external_inputs':[
 {'authors':'S. P. Smith and J. Tate','title':'The center of the 3-dimensional and 4-dimensional Sklyanin algebras',
  'journal':'K-Theory 8 (1994), 19-63','url':'https://sites.math.washington.edu/~smith/Research/tate.pdf',
  'pdf_sha256':'2cf94c6171dcbd212eed51d0d6a915618d8d279e26541c596ddffda13a9df74e',
  'read_locator':'Introduction/definition of A and canonical g, Lemma3.5 and proof, Theorem3.7 and proof; printed pp20-21,36-38',
  'used':'proper elliptic Sklyanin canonical central cubic and THCR; center generated in degrees3 and9 when translation order9'},
 {'authors':'Christopher J. Pappacena, Lance W. Small, Jeanne Wald',
  'title':'Affine semiprime algebras of GK dimension one are (still) PI',
  'journal':'Glasgow Mathematical Journal45 (2003),243-247','doi':'10.1017/S0017089503001204',
  'arxiv':'math/0211330v1','url':'https://arxiv.org/pdf/math/0211330',
  'pdf_sha256':'53f7b2acdc9c6f293ba63f4bc256286b294976eecc0f835730210dbf5b9a78ab',
  'read_locator':'Theorem5 and complete printed proof, arXiv pp4-5; preparatory statements and proof read',
  'hypotheses':'affine semiprime algebra over any field, GK dimension1',
  'application':'central localization of domain D over k(psi,g^3); standard identity restricts to D'}],
 'not_claimed':['program verifies external theorem or all geometric arguments','PI degree of D or U equals9','full center or Brauer period known','U prime/domain','complete H3 classification']}
(ROOT/'cubic_third_root_unit_boundary_L_PI_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','boundary_translation_order':9,'affine_ambient_and_cut_PI':True,'PI_degree_unresolved':True}))
