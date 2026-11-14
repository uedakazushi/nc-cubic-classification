# Codex research instructions — 2026-11-15 / recognition-v3

Read `00_research_plan.md` first, then `research/weak_cubic_axioms.md` and `papers/weak_cubic_axioms.tex`. The existing `research/cubic_surface_comparison.md`, `research/r13_generic_moduli.md`, surface paper, threefold paper and computations remain current research assets; preserve their mathematical content.

## Scope and current correction

The intrinsic weak-cubic axioms, even with generation in degree one, relations in degrees two and three, and vanishing of Ext1(O,O(m)) for all twists, do NOT force the ambient into R(1,3). Use the quantum Fermat example and proofs in the new paper. Its ambient is separated from the four-vertex R13 orbit closure by a proper closed normal-line incidence with projectively trivial fourfold return. The non-invariant assertion Z(B)_1=0 alone is not the proof.

Separate universal intrinsic recognition from the R13 central-extension branch. Do not conflate arbitrary periodic markings, Frobenius-compatible periods, graded isomorphisms, indexed Z-algebras, directed relation models and rolled-up potentials. Match GL/PGL scalar inertia before claiming a stack equivalence.

Questions still unresolved are global redundancy of the low-degree presentation axiom, universal AS4 recognition, algebraicity of the entire intrinsic weak stack, a uniform finite-type atlas covering all objects, categorical openness, and the exact weak fibre. A finite presentation or a finite-type formal hull alone does not prove algebraicity. The R13 central-incidence model has P1 fibres and rational generic function field, and the geometric generic central quotient is weak under the stated hypotheses; not every central quotient is a weak smooth surface.

The quantum example has an actual domain section ring. For a general Abelian category, state the rank/torsion theory rather than assuming the phrase rank one is self-defining. Relative families need flatness, section base change and relative Serre data.

## Work and checks

Keep complete proofs in Japanese LuaLaTeX. Use `python3 computations/verify_quantum_fermat.py` and `latexmk papers/weak_cubic_axioms.tex`. The tracked certificate and regenerated certificate agree as JSON; whitespace need not match. Validation scope is `research/weak_cubic_validation.json`. Distinguish a written proof, this work's proof examination, an exact calculation, an external theorem, a conjecture, formal verification, and novelty. Existing proofs not reexamined this time must not be labelled reverified.

For the central branch, continue the relative inverse-Serre construction from AOU's finite algebra, numerical marking uniqueness, Weyl descent and weak-locus openness. For universal recognition, investigate intermediate cohomology, Cohen-Macaulayness, normal anticanonical boundaries, cubic overlaps and finite-type recognition separately. The R13 generic Hessian and critical-point descriptions are not a classification of all weak cubic surfaces or all component boundaries.

## Persistence

The user has authorized research-break saves without further approval. Maintain a self-contained current bundle and save it to Library; save current source changes to GitHub main by ordinary fast-forward when available. Do not delete existing Library assets without an explicit instruction. No GitHub Actions, force push or unsolicited PR. Do not track PDFs, TeX intermediates, caches or ZIP archives in Git. Preserve useful prior results while removing redundant history from new bundles. Report generation, mathematical checking, computation, typesetting, GitHub save and Library save as separate verified states.
