# Codex: 14641 intrinsic nc cubic classification

2026-11-15. This document is the authoritative execution plan for the 14641 subclass. Read 00_research_plan.md, research/cubic_14641_classification.md and papers/weak_cubic_axioms.tex before beginning. Existing heart/corner and other del Pezzo projects remain current and must be preserved.

## Explicit continuation instruction from the user

完全分類までなるべく止まらずに作業を続ける。部分成果の保存を研究の終了条件にせず、必要な確認と実際の制約を除き、既に許可された研究・検算・原稿更新・mainへの通常pushを継続する。未証明の全被覆や降下を完成扱いしない。実行上の制約で中断する場合は具体的な未解決課題を残す。チャット終了後の未設定バックグラウンド実行は約束しない。

## Current completed subproblem and next action

The skew-polynomial envelope sector has a geometric-object/groupoid classification: 31 coordinate parameters in five types, all coefficient conditions and generic rank checked. See research/cubic_14641_classification.md. Whole H3 has mu_R=id and sigma_G=mu_B^{-1}; hence work with the single linear kernel W1 of a 140x20 matrix. The RRZtri epsilon hypothesis is proved by R tensor a finite B-resolution of k. The scalar ambiguity is eliminated by AS index1; do not continue treating c as a free candidate. CY ambient forces central G, but an explicit complete non-CY sign family exists. The six-point third-root orbit fails GK rank-one despite smooth tails. The standard Pym L112/R22/S23 generic charts and nonzero E3 quantization have Z3=0 (see cubic_pym_generic_exclusions.tex and exact QQ certificates). All nontrivial unipotent lifts of quantum canonical untwists now have W1=0, so that entire sector has the same five-type classification. Every nonzero ordinary differential Ore extension over a commutative three-variable ring is excluded by point self-Ext dimensions 1,3,4,4,..., even when central cubics exist. This also excludes all unipotent lifts of noncommutative CY canonical bases of commutator dimension >=4 and the three-commutator beta stratum. Exact as4 import SHA, hypotheses and original validator reruns are in research/as4_imports.json; inverse Nakayama conventions are converted in cubic_as4_reductions.tex. Next classify all R13 cuts, L112/R22/E3 special loci, remaining low-commutator CY and non-scalar resonant AS4 families, then prove coverage and family descent. Do not claim global completeness or componenthood from the skew classification.

## Ultimate mathematical goal

**Completely classify the strong intrinsic weakly marked nc cubic surface subclass H3**, not merely its generic points. In characteristic-zero algebraically closed k, a member is (A,O), with the Gabriel–Krull rank-one torsion-free exceptional O, inverse Serre heart-preserving polarization tau=S^{-1}[2], Artin–Zhang ampleness, cubic Hilbert series, R=⊕Hom(O,tau^n O) generated in degree one, and its quadratic envelope B=Q(R) left/right noetherian quadratic Koszul AS-regular of type (1,4,6,4,1). Do not include an external ambient, arbitrary four-periodicity, a quiver basis, or an exceptional collection as extra marking. Homological dimension 2 is derived from Serre and heart preservation.

The current recognition proof gives R=B/(G) with G∈B3 regular normal. This is a conclusion, not a separate axiom. Verify its external theorem hypotheses when using it. The OU AS locus is a nonempty proper subclass, and the quantum Fermat counterexample lies outside it. An OU/AOU marking and an intrinsic weak marking are not automatically the same.

## Immediate top priority: structural classification of normal cubic incidence

**Do not first attempt complete classification of every quadratic AS4 ambient B.** Instead restrict ambients by the existence of a regular normal cubic. Study
I3={(B,[G]): B is AS4 of type 14641, [G]∈P(B3), G B1=B1 G}.
For fixed B, use the 35×8 multiplication matrix [Gv_i | v_iG]; all its 5×5 minors define the scheme of normal cubic lines inside P(B3)=P19. Compare its rank strata, scheme structure, flatness and normal automorphisms. This incidence may be substantially smaller than ambient moduli.

A first proposed structure theorem is that every pair (B,[G]) belongs to finitely many explicit geometric construction types; **prove it or supply a counterexample and correct formulation**. Do not claim the theorem from parameter counts, experiments, or an unproved list of families. Investigate general points and major components first, then degenerations and boundary schemes.

## Execution phases

A. For each grounded family R(1,3), Pym's six graded CY families, the skew polynomial torus and quantum Fermat intersections, compute the generic scheme N3(B), normal automorphism of G, center versus noncentral components, dimensions, stabilizers and generic orbits. Use existing proofs and sources instead of reinventing them. Pym's six graded CY components do NOT exhaust all AS4 Z-algebra moduli by fiat. Keep 1-periodic graded, arbitrary four-periodic Z, Frobenius-compatible periodicity and rolled-up potentials distinct.

B. Check AS4 and ASZ4 results and examples for other normal-cubic ambients. Establish coverage rather than assuming it. Identify explicit unclassified strata. Determine whether apparent components coincide under the correct intrinsic exact abelian equivalence, not just graded isomorphism, Zhang twist or derived equivalence. Preserve stabilizer/inertia and family descent.

C. On each normal cubic quotient B/(G), verify the actual intrinsic conditions: qgr heart, Serre action and t-exactness, exceptional rank-one structure object, Artin–Zhang ample, saturation and base change. Not every normal cubic quotient is automatically a smooth weak nc cubic. Check AS-regularity, noetherianity and Koszul exactness throughout degenerations; finite numerical rank tests alone cannot certify them.

D. FULL classification requires all objects covered; explicit geometric moduli; correct isomorphism groupoid, stabilizers and rigidification; all irreducible components, intersections and boundaries; intrinsic Serre/heart/rank/AZ conditions; and algebraic stack and descent for families. Until these are proved, call results partial or generic classifications and state the exact remaining cases. Publish valuable complete partial theorems with full proofs as needed.

## Scientific and operational discipline

Coordinate with the current as4, asz4 and poisson-p4 repositories for ambient and Poisson deformation data. Reuse the current cubic-corner, AOU/OU, Rains, VdB and degree-one research only when their hypotheses apply. Do not restrict to R(1,3) or central cubics merely for simplicity. Preserve the non-AS quantum Fermat branch. Keep exact numerical calculations and characteristic-zero proofs separate; finite-field evidence is not a theorem. If a classification route fails, retain useful counterexamples and refocus on the most mathematically valuable tractable subproblem.

For each result record assumptions, dependencies, proof location, whether freshly verified, exact computation input and certificate, unresolved points and novelty status. Keep a current self-contained research plan, research notes and Japanese LuaLaTeX paper, not chronological logs. Update source, code and small reproducibility certificates on GitHub main via ordinary fast-forward; do not track PDFs, ZIPs, caches, TeX outputs, or use GitHub Actions, PRs or force push. Verify remote HEAD. For this repository, do not save to Library if the GitHub push succeeds; Library is an emergency fallback only.
