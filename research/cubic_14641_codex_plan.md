# Codex: 14641 intrinsic nc cubic classification

**滑らかな楕円境界部分（H3 classification-v36）**：中央境界では、次数3 translation THCRの全filtered deformationからCY AS4包絡と正則中心三次を復元し、全幾何学的矢をfiltered同型で記述した。有限Nのadmissibilityは中心McKay条件で完全判定し、被約固定N族ではH3開性・任意底変更・fpqc降下も得た。三捩れ量子Weyl chartの全中心と有限Hessian/character判定、j0 potential境界の非分裂例も保持する。

**非中央正規一次楕円境界**：共役位数は2または3に限る。位数2は量子involution（既存符号型）とClifford swapへ漏れなく被覆し、後者の三次は一本、中央volumeへの有限cocycle還元により長さ8 character完全交叉の被約性が必要十分。非skew・非CYの具体例を検算済み。位数3は最高Koszul tensorの8次元随伴模型と全Jordan型の計算から量子P2に限られ、全対象が既知の量子Fermat一対象、幾何学的群oidBH54となる。全H3が正規一次楕円境界を持つとは主張しない。

**滑らかな正規楕円境界の外の実例**：q³1のq-so3包絡のCasimir切断で、全H3判定(D−f)(3D+f)≠0を得た。中心はFricke cubic、無限遠triangleはterminal order、許容対象はどの正規一次境界でもsmooth elliptic THCRを持たない。これによりmissing-boundaryの実在部分を一つ完全判定した。全intrinsic矢はD不変・慣性A4、相対表示stackはgood Dline×BA4。一般qでも全切断の忠実差分模型と整域性、全候補矢[Q/S4]を得た（classification-v47）。非捩れまたは位数>3では全H3候補がこのpencilに限る。奇数位数N>=3では全中心Fricke式と任意次元の二種の三重対角既約表現から、H3 iff(D−D+)(D−D−)!=0を証明した（classification-v50）。全N−1内部特異値もMcKay条件を満たす。偶数位数も半Chebyshev正規元のweight分解から全端点を排除し、全有限位数qでH3 iffD!=D±を完全判定した（classification-v54）。粗座標theta=q+q^-1,w=−theta−h³D/q²、固定N表示stackはphi(N)/2個の(A1_w minus{+-2})×BA4。全中心形成は任意底変更と可換。これら全族は正規smoothE境界を持たず候補平面に稠密。非捩れqでもGWA反転固定環へのOre局所化から二端点の非H3性を証明した（classification-v55）。端点以外はこのOre開集合gl<=2。三頂点の形式的模型は全qでgl2、非捩れで完備量子平面と証明したがqgr降下は未完。さらに全標数0代数閉体上のproper楕円四次元Sklyanin（n∞又はn!=1,2,4）を全排除した：唯一の中心三次残余n3もdimZ3=dimS1=4により射影norm P3->P3が全射、全Gが一次式×二次式でnondomain（classification-v58）。一般にCY・PI3・normal-centre-finiteのH3包絡はdimZ3>=5が必要。さらに三乗根の固定量子so3包絡はpencilだけでなく全P4中心三次を完全判定した（classification-v60）。Delta=alpha³+27beta gamma delta!=0かつ五節点cubic3foldのdual外が必要十分。全表示stack[U/A4]はDM4、慣性1/C2/C3/A4、全中心basechangeと表示族降下。さらに指定qso3正常形の中心incidenceはp(q)(beta,gamma,delta)=0、dim2水平とdim4垂直がdim1で交叉する。固定Bのmissing smoothE locusは既約normal-crossing divisor、全点がsmoothE H3の特殊化。粗tetrahedral商・境界正規化も明示した（classification-v61）。一般Zhang twistも縮小した（classification-v63）：twisted-skewのH3はskewに戻る。非退化中央quadric pencilを持つproper Sklyaninの全自己同型Zhangtwistと標準V4cocycle twistは全排除。cocycle centre3はn3/6のみdim1で必ず一次×二次。Stafford三族と標準cocycle・循環変種も全T/全許容dで全排除した（classification-v68）。通常W1はL=alpha beta+alpha+3beta−1=0でだけdim2、全pencilがdegree3因子写像で分解。CY cocycleのcentre3は四つの互いに素な明示曲線でのみdim1となり全て分解する。sigmaの全T第三反復で特殊chartの欠落も除いた。

**as4具体表示の独立排除（classification-v89）**：固定commit a45f834f51a00c47443b51caf66abaf4629546b9からは具体表示のみを参照し、全CY/全AS4被覆・存在十分性・全同型を新規輸入しない。二重被覆DCC1二族、非被約のCF2/CF3/CT2、TT22六表示、DS3/DT1全列挙表示は排除済み。四単純基点ではFS4のSと標準cocycleを全値排除し、FZ2のQも零交換子CY skewの中心三次は純三乗一本以下という一般補題で全排除し、FZ4/FZ5のO/Hおよび標準Klein cocycleも全値排除した。さらにFN3七表示L/M/F0/F1/G0/G1/K、第五係数零のM_p二族とN/C、FO2の全二パラメータH_(lambda,p)、FG2の全R_lambda両符号を排除済み。Rはtwist後の非零中央二次の逆指標から全奇数中心が零となる。FI2のJ_h両符号も全h非零で中心3消滅により排除し、h0は五次次元58の独立計算でAS4から除外した。FT3のPも全二パラメータ・両符号を排除した。詳細な式・全値rank cover・Ore/normalizer証明は `papers/sections/cubic_as4_*exclusions.tex`、輸入範囲と実行済み検証は `research/as4_imports.json` と `research/cubic_classification_validation.json` を読む。隣接AZ2の二固定Lも、Ore normalizerの三乗がomega/omega²倍になることと純base切断の頂点無限Extにより排除した。一般にCYのB=S[z;sigma]でsigma³が非自明scalarならH3にならない。隣接AB3の全S_zetaも四次次元>=37で排除し、T_-2両符号がその特殊値に一致することを独立確認した。T両符号も全lambdaで排除した。全64三次語のprimitive交換子moduleについて独立なC_0 X=N恒等式と20三角pivotを検証し、追加因子ABC_*とその対合像が互いに素なので二枚で全残余を覆う。三次/四次商射影も元の全関係で再生確認し、全値AS4存在・平坦性は仮定しない。Pは全二変数の商射影と40次元realified rank恒等式を独立検証し、次数30の垂直例外をlambda反射と三特殊直線の全r計算で全て排除した。次は列挙表示から全H3へ至る必要被覆定理を監査し、残る未被覆領域と許容条件を縮小する。

**現在のスペクトルfrontier（v261）**：(1,3)は全幾何学的分類済み、(3,1)及び(2,2) mixed rank2は空、(2,2) mixed rank4は全Jordan型込みで曲がったClifford族へ認識。最後のL飽和はv202で完了し、解決済みへ戻らない。
三固有値は二次/三次/四次共鳴・Frobenius関係・整域性から有限化し、全非有限pencilと位数4,5,6,9,12を排除。残る必要スペクトルはN3:3個のみ（Galoisラベル2軌道）、各関係パターン一つ。全単冪部分を排除し、中山は半単純・位数3に限る。三スペクトルの存在/許容性は未分類。
**次の最小課題**：位数4は全排除済み。最後の(i,i,-1,-i)は追加b4非零をSchur補と対称二次の巡回障害で排除、b4零の四表示は正常核因子/零。単冪も含む。N3非単位重複根の全Jordan層も85変数の実際の巡回式から排除した。重複1のJordan層も実際の12次元top核からOre表示を復元し、D不変三次の量子平面商障害で全因子とした。二ラベルの半単純22次元最高tensor atlasと8/7次元の正常係数を公開。可逆CY untwist C=B^muではGは正常化mu^-1を保つ非中心三次であり、中心三次の既分類では覆えない。重複1のP=Q=0とP,Q独立/S=T=0も排除。後者の一変数族は全pivot/Smith/二例外fiberで全値検証済み。独立P,QでS0はT非零も二変数平面と全境界/例外値を消去して排除済み。独立P,QのS非零も元Schurの全分枝と全例外根で排除済み。比例結合の一方的非零曲率AS2–Ore表示も全正常三次因子で排除。被覆は別途。比例S非零も全Schur分枝と正常一次商の二syzygy Hilbert障害で排除。unit-repeat残余はrank(P,Q)=1,S0のみ。二方向曲率split Ore族も全q W1を因子/頂点で排除。非split x²変形もCasimir/ノルムと曲面period=indexから九乗根商の非整域性を示し全排除。量子Weyl基底を持つ全二方向曲率Ore層もshear/共鳴付随次数で被覆し排除。両非零比例結合は元22tensorからT=a2=0と正常xの六係数境界へ被覆。w非零はw1へ、明示Δ非零の全開集合で境界商の正常核を排除。L曲線のΩ開集合では全u,vの正常核を一本の全多項式持上げとして解いた。全u,vを実AS4整域として認識し、中心ΨとΓの差をx,y多項式で明示。境界translation位数9、affine ambient/切断のPI性も証明。固定E2,u1,v0の全6埋込で中心部分環k[x,Ψ,z9]上自由階数81を証明。固定例の全中心多項式環/generic CSA9/primeも確定。E2,w1の全Z,u,vは位数3相対双対と二fiber resultantでH3排除済み。次は全L/Ωへの中心9と二fiber障害の持上げ、及び残る境界。並行分業はせず、他の退化projection/偶rank2と非単位重複根atlasも順に扱う。係数の意味と証明は分類ノート末尾。証明/certificate所在は分類ノート末尾。再生は `python computations/verify_cubic_spectral_reductions.py`。
四単純の二次非共鳴領域はskewへ還元して排除。さらにas4参照chart(a,-a,i/a,-i/a)はa4≠±1でAS2二平面因子により全排除、a4=-1も二固有値障害、a4=1の四単純境界は保持。四族分類は輸入していない。残る共鳴領域、全CY被覆、成分・境界・intrinsic族降下は未完。一般正規三次の四line frameはrank条件を別仮定とする補題で、有限H3検査/相対開性は未証明。

classification-v12 では、積分した族の全次数平坦性・noetherian quadratic Koszul CY AS4 認識を、明示的な開集合 V={h∈H, (1-gamma²)≠0, Delta≠0} 上で証明した。入力は Iyudu–Shkarin Theorem1.1/Corollary6.1、EG形式変形定理、および64個の三次持上げ恒等式・256個の四次巡回恒等式・単元小行列式 -p^6 を確認した LBS 中心拡大定理である。中心三次の関係類の非消滅も巡回商の二係数で全パラメータについて確認した。gamma≠0 では低次数中心が0,0,1、滑らかな楕円THCR境界となり、全中心値の H3 判定は正確に一つの affine 中心切断の有限大域次元へ帰着する。定義体上超越的な全 D は H3。位数4の枝 gamma^4=1+h^3 では固定包絡の悪い D は有限であり、h=1,gamma=2^(1/4),A=1,B=C=0,beta=(-1,0,0),D=pi は明示的な非Clifford H3 対象となる。悪い値の全一覧・全内在的群oid・H3相対開性・降下・全包絡被覆は未解決。

classification-v11 では、Etingof–Ginzburg の付録と著者サイトにある Rains の E6 中心元を規約変換し、全パラメータで三交換子の関係恒等式を独立検証した。`alpha=-4*gamma*(A,B,C)` と置き、正規化した中心元に定数補正を加えると、全 Clifford 切断が実際の有理式による中心表示へ積分する。gamma=0 での全係数・関係証明書の分母はよい h の全底上で正則であり、全次数の「中心性」の障害は解決した。これは包絡族の全次数平坦性、AS4 認識、切断後の H3 条件や新成分を証明したという意味ではない。次はこの積分した具体的表示でそれらを検証する。

classification-v10 では、この族から外れる指定四方向の一次中心 incidence も全係数で判定した。双対数上で最高次を `(1+epsilon*gamma)yz+(1-epsilon*gamma)zy` に変え、対角項を `epsilon*alpha_x*tx`（巡回）だけ動かすと、三次中心切断の持ち上げは正確に `alpha=-4*gamma*(A,B,C)` のとき存在する。持ち上げを明示し、全ての h,beta,A,B,C,D に通用する次数4の階数86、三次交換子階数15、単元障害行列式 `-9/(4*(1+h^3)^2)` を検算した。これは指定方向の一次 incidence であり、積分可能性・全変形空間・新しい H3 成分を主張しない。 また、この明示的持ち上げの二次障害も全係数で消え、対角係数の二次補正 kappa と中心切断 G2 を計算した（epsilon^3=0）。中心性の全次数積分は v11 で解決し、H3 族への実現は未解決である。

2026-11-15. This document is the authoritative execution plan for the 14641 subclass. Read 00_research_plan.md, research/cubic_14641_classification.md and papers/weak_cubic_axioms.tex before beginning. Existing heart/corner and other del Pezzo projects remain current and must be preserved.

## Explicit continuation instruction from the user

完全分類までなるべく止まらずに作業を続ける。部分成果の保存を研究の終了条件にせず、必要な確認と実際の制約を除き、既に許可された研究・検算・原稿更新・mainへの通常pushを継続する。未証明の全被覆や降下を完成扱いしない。実行上の制約で中断する場合は具体的な未解決課題を残す。チャット終了後の未設定バックグラウンド実行は約束しない。

## Current completed subproblem and next action

The skew-polynomial envelope sector has a geometric-object/groupoid classification: 31 coordinate parameters in five types, all coefficient conditions and generic rank checked. See research/cubic_14641_classification.md. Whole H3 has mu_R=id and sigma_G=mu_B^{-1}; hence work with the single linear kernel W1 of a 140x20 matrix. The RRZtri epsilon hypothesis is proved by R tensor a finite B-resolution of k. The scalar ambiguity is eliminated by AS index1; do not continue treating c as a free candidate. CY ambient forces central G, but an explicit complete non-CY sign family exists. The six-point third-root orbit fails GK rank-one despite smooth tails. The standard Pym L112/R22/S23 generic charts and nonzero E3 quantization have Z3=0 (see cubic_pym_generic_exclusions.tex and exact QQ certificates). All nontrivial unipotent lifts of quantum canonical untwists now have W1=0, so that entire sector has the same five-type classification. Every nonzero ordinary differential Ore extension over a commutative three-variable ring is excluded by point self-Ext dimensions 1,3,4,4,..., even when central cubics exist. This also excludes all unipotent lifts of noncommutative CY canonical bases of commutator dimension >=4 and the three-commutator beta stratum. Exact as4 import SHA, hypotheses and original validator reruns are in research/as4_imports.json; inverse Nakayama conventions are converted in cubic_as4_reductions.tex. The good elliptic fixed-envelope cuts now have domain and intrinsic rank uniformly; admissibility is exactly finite global dimension of D/(omega+lambda). Over C the split B=S[t] sector is completely classified by Lambda=C*, one orbit with inertia a central mu3 extension of PAut(S); the zero cut has infinite point Ext. For fixed good B with finite-order translation boundary, bad central values are finite and Lambda_B is nonempty open (Rains Theorem2.13 plus RSV Proposition2.1); their explicit values and infinite-order generalizations remain. Next determine nonsplit R13 central values and cover degenerations outside the good elliptic assumptions, L112/R22/E3 special loci, remaining low-commutator CY and non-scalar resonant AS4 families, then prove coverage and family descent. Do not claim global completeness or componenthood from the skew classification.

## Newly completed explicit non-skew sector

Classification-v7: all H3 cuts and geometric arrows for B_h=S_h[t] with yz+zy=h x^2 cyclic, h!=0,h^3!=-1,8, are a dimension4 finite quotient by the order648 mu3-extension of Hessian216. At h=1 all cuts are an explicit dimension3 open quotient by G(3,3,3), with a proved monic quartic central-value norm and invariant coefficient interpolation. Axis bad values are exactly0,-16A^3/27,8A^3/49; nonzero-axis good inertia is S3. The fixed-h comparison group is54 or108 at h^6+20h^3-8=0. There are no nontrivial unipotent lifts of these canonical bases. See cubic_clifford_full_cuts.tex and both Clifford checkers. All rank/Serre/AZ/center/Azumaya conditions and geometric isomorphisms are proved within this explicit family, not full ambient coverage or relative descent. The next target is nonsplit Clifford central extensions, other elliptic orders and remaining low-commutator/non-scalar resonant strata.

## Nonsplit reduction now proved

Classification-v8: the normalized three diagonal f2 coefficients alpha_i in order-two Hesse central extensions are all zero for H3, independently of constant terms beta. Universal central-cubic obstruction determinant -27*h/(8*(1+h^3)^3),99 symbolic relation identities, and256 mixed-quartic cyclic identities certify the all-parameter reduction. Thus f2 is removable by translation. The surviving beta-only family and its rank-one non-Azumaya behavior are now solved in v9: ordinary nodes are allowed, worse singularities are excluded.

## Complete nonsplit beta-sector recognition and geometric classification

Classification-v9: The entire specified order-two symmetric-potential central-extension sector has all H3 cuts and all geometric arrows classified by [P/G], generic dimension7. Every singular point of the affine center must be a rank-one Clifford ordinary double point; this is necessary and sufficient. Such local orders complete to k[[s,t]] semidirect Z2 (gldim2); worse points are ruled out by odd self-Ext1 or a degenerate quadratic cross-Yoneda/Serre pairing. All beta envelopes are AS4 by explicit PBW/W3 checks and LBS2.6/2.7. Pure volume cuts are exactly reduced8-point character fibers and have4 nodal center points; h=1,beta=(-1,0,0) is an exact witness. Group G has Gm identity component and Hessian216 components, full beta/A/D action includes a mixed correction to D, and D=0 is allowed. Generic inertia is trivial, or mu2 on the3-dimensional volume subfamily. No additional unipotent lifts. Read cubic_clifford_beta_classification.tex and both beta checkers. Next: other elliptic orders, nonsymmetric/non-CY envelopes, deformations into other ambient directions, full coverage and relative descent.

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


## スペクトル・全単冪領域の現行到達点（v293）
強いintrinsic H3のAS4包絡は相異なる中山固有値をちょうど三つ持たない。全Jordan型の必要還元、重複1の全22tensor atlas、非単位重複rootの独立・非零比例・零b²列を全て排除した。全H3分類の完成ではない。全単一固有値非CYも排除済み。全CY切断、全成分・境界、相対降下は未完成。

### 完成した証明の入口
三固有値全体の結論は `papers/sections/cubic_third_root_nonunit_zero_column.tex` の `thm:cubic-three-eigenvalue-sector-empty`。重複1はunit_onezero_completion、非単位重複rootの非零列はnonunit_independent、nonunit_proportional_open、nonunit_proportional_Tzero、nonunit_isolated、nonunit_degenerate_selfの各節を経由する。Q=0の別分枝を含めて必要被覆を保持している。
最後のp=r0ではcがU上で正常、c u=F(u)c、FJF^t=−ω²J。元二列はLb=T c²,bL=ω²T c²（L=mx+ny）。domainからL,T非零。F²L=ω²Lで、Lが固有vectorならc全正常、B/cにLb=bL0が生じHilbert矛盾。L,F(L)独立ならCHからFdiag(ω,−ω)、self offdiagのみ。generator/top変更でs=m=n=T1。元rank2条件の12linear式はrank7で一変数Dへ。全値source画像はcx=ωxc,cy=−ωyc,(x+y)b=c²,b(x+y)=ω²c²,bc=−((D+ω)x+Dy)(x+y),cb=−ω²(x+y)((D+ω)x+Dy)。unit6minor/係数体分母で全値同定。正常33×7は定数7pivot、全source/normal例外はD(D+ω/2)(D+ω)。fresh D0,−ωは正常核零、D−ω/2はB3dim22。これで最後の列も全排除。
最新v275主原稿LuaLaTeX clean PASS、新checker default Sympy PASS。累計58validators across runs、単一58全再生は未実行。統合replayソースの現行候補は0、古いキャッシュ出力を新実行と扱わない。新規as4/外部定理輸入なし。新規性未確認。

### 四単純位数4の必要atlasと第一rank型（v276）
スペクトル(1,−1,i,−i)の元twisted-cyclic四次topは16次元。二次weight groupsは0:(xx,yy,bc,cb)、2:(xy,yx,bb,cc)、1:(xb,yc,bx,cy)、3:(xc,yb,by,cx)。0block対称、2block交代、1/3paired。trace成長の分母1+(r0−r2)t²+t⁴と1+(6−4r1)t²+t⁴から必要rank型は(2,2,1,1),(2,0,2,2),(0,2,2,2)のみ（重み0,2,1,3順）。各B3重み次元5。
最後の(0,2,2,2)は全H3排除済み。H0zeroから八係数零、domainでa3,a4,a7,a9全非零、対角でa3=a4=1,a7=a9=q。残りA=a5,h=a6,k=a8,E=a13、rank2Mの全minors GB13で必要被覆。A=E0はq=t²,k=t,h=±tの全t非零Oreモデル、x/y正常固有値により全Gがx又はyの因子を持つ。残余は対角十軌道へ。二軌道正常核2は全x因子、七軌道正常核零。唯一残るq−1,A1,E0,h=i,k−iの正常核1はG=c²y−bcx/2+i cbx/2。
この最後の包絡はb²+c²,xy−yx,xb+bx,xc+cx,yb+i by−i xc,yc−i cy−xb。normalx開集合の次数零環はYB−i BY=iC,YC+i CY=B,B²+C²0,2C²Y−BC+i CB0。原点characterの自己Ext1はY方向1。H3 Serre=(-1)[2]をnormalxで同定するとH(Y,B,C)=(Y,−B,−C)、Ext1に恒等作用。twisted Serre traceの符号から非退化交代対が必要となり矛盾。S(L)=L[2]だけで作用自明を仮定せず、唯一のY方向に実際に作用が自明と確認した。
通常証明はcubic_four_simple_order4_rankC節。公開checker default Sympy PASS（16top/rank/GB13/全値sourceunitminor/十軌道/因子/例外G/dehom/character接空間）。v276 main LuaLaTeX clean PASS。累計59validators across runs、単一59全再生未実行。全四単純又は全H3完成とは呼ばない。新規外部/as4輸入なし、新規性未確認。

### 四単純位数4の全完成（v278）
残る(2,2,1,1)はpaired M=P Q^tの巡回四binomial式とdomainから全十support、六chartへ。primitive iの選択変更とb/c交換で三chartを見れば十分。P02はH2純平方からa14zero,a0v非零、H0rank2 Schurから純x²又はy²。P13はH0純y²とH2純c²で全排除。P01/Q23はPfaff a0a14=−pqとH0Schurの(1+i)pq/a0非零で矛盾。元16tensor/全support/全Schur恒等式公開default Sympy PASS、v277主原稿clean PASS。
最後の(2,0,2,2)はH2zero。H0=[[0,0,u,v],[0,L,B,C],[u,B,D,0],[v,C,0,−iD]]。u=v0はdomainがD,BC,Ah非零を強制しMに3minor−A²C。片方のみ非零は純bc/cb。uv非零をu1,vρへ、H0SchurでL0,CρB,D(ρ²−i)0。B0はdomainE,k非零だがM3minorE²。B非零をB1へ、rank2の単元ρpivotで全条件hk+ρA²−iρ²=0,h(E+ρA)=0,k(E−ρA)=0,ρhk−E²+iρ=0。
全値は二つのOre曲線(h=k=D0,A=t,ρ−it²,E±t)と18有限対角軌道へ。曲線のb,c正常固有値の二条件は固定三次の全五基底方向でgcd定数、全t非零正常核0。有限点はhk非零2点、hのみ/kのみ各4点、D1かつt4−iの8点。QQ[z]/(z8+1),i=z4で全18根の元商dims3/4=20/35、正常28×5又は25×5全rank5。新checker default Sympy PASS、v278主原稿LuaLaTeX clean PASS。
従ってスペクトル集合{1,−1,i,−i}は全H3排除。既存一般chartと合わせ、全非零aで(a,−a,i/a,−i/a)も全排除。ただし全det負一スペクトルの被覆ではない。通常証明はfour_simple_order4_rankA/rankB節。累計61validators across runs、単一61全再生未実行。新規as4/外部定理輸入なし、新規性未確認。

### 全四単純の四曲線／有界有限点への必要被覆（v279）
四単純H3スペクトル全体は、ある共通位数N≤96の有限集合、又はλ_i=α_i t^{n_i}（α共通位数M≤24、t非零、有限位数も含む）の四方向n=(0,0,1,−1),(0,1,−3,2),(0,1,−2,1),(1,−2,−1,2)で必要被覆される。Mは24の約数とは限らない。これは存在やH3十分性・群oid分類ではない。
証明はfour_simple_spectral_curve_atlas節。二次指数u、Gの実際の全三次support、topの実際の全四次supportの有理span Lを使う。二次u/三次vだけの平面ではquartic全変数被覆が不可能なのでrankL≥3。rank4はu,v,wと追加cubic又はquarticのdeterminant、三型の最大det(48,96,48)/(36,72,36)から共通位数≤96。rank3は全top/Gがprimitive kernel n重み0なので、μが有限位数でも実際のtorus作用とG固定を得る。正のregrading deg=N+n_iのHilbertpole4からsum n_i0とΣr_s s²=2Σn_i²。全21×20×35指数kernelとquartic被覆で1062方向、sumzeroと置換/反転で10型。domain Segre上界とmomentで各I2重みrankが一意。六型は共通一次因子の通常証明で排除。残四型のphase代表はSmith最大因子≤3minor gcd、最大gcd(12,24,12)と符号から共通位数M≤24。
公開checker default Sympy PASS（全60平面、全kernel、全rank整数解、因子pair、全det/gcd）、v279主原稿LuaLaTeX clean PASS。累計62validators across runs、単一62全再生未実行。新規as4/外部定理輸入なし、新規性未確認。

### rank三supportのphase削減と二方向完成（v280）
全support格子rank3のうちn=(0,1,−3,2),(0,1,−2,1),(1,−2,−1,2)はそれぞれ(1,t,t^-3,t²),(1,t,t^-2,−t),(t,t^-2,t^-1,t²)へ必要削減した。topがmultilinearだけならmiddle像が六pair直和になりdomain/rank6からskew、という補題を使う。全M≤24位相/quad衝突/quartic支持を公開default Sympy PASS。
最初の方向はb,yが正常、Gにx³とybc双方が必要。B=A0[b;g]、A0はxy,yc skewとAxc+Ccx+Dy²のAS3。片側xc係数零は正常yとdomainから逆向き独立quadが生じるので不可。Ore/Koszul双対からA0 AS3、topのxyc非零によりhdetg=ade、μb=ade。正常bの固有値比較a³=de=ade⇒a=μb1、μx1と重複。全rank3 chart排除。
第二方向はU(y,c)のAS2関係y²+κc²、他五pairskewなのでB=T[x;f][b;g]。g(x)=q x、g|Uの平方scalar d²共通、μb=q d²。非因子Gにx³とU²b双方が必要、正常bからq³=d²=q d²⇒q=μb1、μx1と重複。全rank3 chart排除。
通常証明はfour_simple_curve_phase_reduction節、公開checker（全phase、domain自由語恒等式、正常izer ideal）default Sympy PASS、v280主原稿LuaLaTeX clean PASS。累計63validators across runs、単一63全再生未実行。新規外部/as4輸入なし、新規性未確認。
重要なscope：有限位数のμで追加の非零n重みtop/G supportがある点はrank4有限部分に保持する。上の斉次chart排除から曲線上の全finite ambientを排除したとは呼ばない。

### phaseなし最後のrank三chartも完成（v281）
(t,t^-2,t^-1,t²)の元10tensorを公開一般diagonal_top helperで構成。paired rank1二式とdomainで六multilinear係数非零、a1=1,a2=p,a4=q,a5=r,a7=pr,a6=pr/q。H0のU(xb,bx)/V(yc,cy) crossは[[q,r],[−pt,−prt/q]]=column(1,−pt/q)*row(q,r)、全rank1。対称rank2H0で両射影同型はcrossrank2を要求するので、純U又は純V関係が必ずある。前者x,b正常、後者y,c正常。残る混合関係の両向き係数は逆向き関係/domainで非零。全六逆順pairの標準三次語20とAS4dim20から全overlap零、量子平面上逐次Ore（最後は二次derivation）を得る。normalbase元の中山固有値は他三生成元への正常化scalar積。
Gはx²y,b²c双方を持つ。純Uの場合normalx scalars(a,b,c)にa=b²c=abc=λx、従ってac1,bλx。変形yc/cy対xbの自己同型固有値が1対λxなので変形非零ならλx1⇒t1。純Vの場合normaly scalarsa²=b²c=abc=λyからa=b,c1、変形xb/bx対ycの固有値λy対1なのでλy1⇒t²1。変形零はskew、いずれもfour-simple H3なし。
通常証明はfour_simple_last_rank3_curve節。default Sympy元10tensor/全rank1式/cross外積/両normalizer ideal/逆向き自由語identity PASS、v281主原稿LuaLaTeX clean PASS。前節の中山scalarとgeneratorの表記をλ_bに明確化した（数学的主張の変更なし）。累計64validators across runs、単一64全再生未実行。
従って残る全四単純の必要被覆はrank3の(α,β,t,γ/t)、phase共通位数M≤24と、rank4共通位数N≤96の有限部分だけ。finite tでも追加supportは有限部分に保持する。

### 最後のrank三phase chartも完成、全四単純を有限化（v282）
全四単純H3の中山は半単純で、共通位数N≤96の有限集合に限る。全support格子rank3を全排除した。これを全四単純又は全H3の完成とは呼ばない。
通常証明はfour_simple_zero_pair_rank3節。正常一次zとφ_zについてμ_B(z)=hdet_B(φ_z) zを証明：中心はAe-resolutionの二中央作用のchainhomotopyからNakに固定、B^{φ^-1}でz中心化、既存RRZ Thm0.3 fullscalar右公式μ_twist=μ H^-4 ξ_hdetHを適用。一次資料RRZ Thm0.3/5.4(a)/0.3の証明を再確認（PDF SHA28b4b649089bbebb722664452c665f8a43ad5b8d9589925b2f97818322736e25）。これは既存文献のscalar項を新たに明示適用したもの、as4新規輸入なし。
n=(0,0,1,−1)ではb,cはU上対角正常、FrobeniusからM:β−α,γα^-2又はS:αβγ1。Sの平方衝突γα²/β²は別分枝として保持した。α5/9は孤立因子、α3は追加7tensor chart(α,1,t,α²/t)で正常xのhdetからφxが全固定三次に1倍、必要固有値αと矛盾。平方衝突を省略してSのαβ±1を主張しない。残りSはskew/交代rank1不可からαβ=±1、非零Gからα6=1。Mもα6=1。七位相型の全default Sympy列挙。
M非符号2型はtop6のpureAS2因子、S非符号minus2型は唯一purecube。S primitivecubeはtop10 crossrank1からpureU又はpureV、前者binary因子、後者正常b scalara³=d³=λ=adeと変形ad=eからλ1。S符号(1,−1,t,−t^-1)はpure-square対称blockをdomainで消し、交代rank2のPfaffからpurebc/cb。PBW固定基底x³,xy²,ybcの非因子に第一/第三必須、正常bでa³=de=ade⇒λb1。
M符号(1,−1,t,t^-1)はxy/yx交代blockをdomainで消しI0⊂x²,y²,bc,cb。bc/cb射影rank1は純AS2 U、cb変形Pの正常izerfg=diag(−1,1)がU中心xy+yxを負にするのでP0、Ore正常固有値でλb1。射影rank2はbc=P(x²,y²),cb=Q。P/Q独立ならx²,y²中心、G=Ax³+Bxy²+Cyxyのx交換子C(xy+yx)(yx−xy)からC0⇒因子x。P/Q比例ならpaired rank1の全成分非零でP両平方係数非零。正常b scalars(A,±A,1,A²)によりtop固有値A4、G固有値A3、上hdet補題でA1,λb1。全rank3完成。
公開checker default Sympy PASS（全phaseと平方追加分枝、元10/9/10/6/7tensor、rank/Pfaff/中心freeword/normalizer ideals）。v282主原稿LuaLaTeX clean PASS。累計65validators across runs、単一65全再生未実行。新規性未確認、通常homological証明の全機械検証とは呼ばない。

### 全有限四単純の39必要ラベル軌道（v283）
共通位数N≤96の最小位数四根集合62,290,587個を全exact走査。二次衝突13,359,699、三次共鳴2,223,885、有効quartic全変数被覆134,703、raw全support rank4は5,338。Frobenius r_s=r_-s,sumr6,自己−1偶数,domain cap_s=dimtensor_s−1のDPで604集合/115 Galoisラベル軌道。
元巡回topの一monomial列をdomainから強制零にし安定化、9軌道top非退化性喪失、2軌道multilinear-only skew。全I2 character解のKoszul群環recurrenceで次数≤12に負multiplicityの出る解を全排除（各degree/component/負整数をcertificateに保存）⇒69軌道。強制pairskewによる共通一次因子と純AS2二元因子で40軌道、既排除位数4を除き39軌道/145根集合。残る位数5,6,7,8,9,10,11,12,13,14,15,18、各軌道数1,4,2,6,5,3,1,10,1,2,2,2。全指数代表と各必要relation characterはfour_simple_finite_atlas節/certificateに保持。Galoisラベル軌道はintrinsic同型商ではない。
公開verify_cubic_four_simple_finite_atlas.pyがC++17 sourceをtmpdirへcompileして全走査、Python標準整数で全115軌道を再検算。浮動根/有限体なし。C++rankは元行minorのみで各項|入力|≤4、det絶対上界4!4^4=6144、64bit overflowなし。公開full replay PASS、v283主原稿LuaLaTeX clean PASS。累計66validators across runs、単一66全再生未実行。原稿の有限表は必要被覆で、AS4存在・正常核・H3十分性を含まない。

### 全support sieveで20ラベル/45根集合へ（v284）
39必要ラベルの全I2 characterで、topの全非空count support SとGの全非空count support Tを走査した。rank0blockが触るorbitを零、monomial列domain pruningを安定化、全変数被覆/nonmultilinear、各blockのmatching rank上界を課す。残る強制pairskewから正常生成元zを決め、未知q_ijを向き付きpair scalarとする。
正常一次hdet補題とG正常式により、全zとw∈S∪Tで∏_{i>z}q_zi^{w_i}∏_{i<z}q_iz^{-w_i}=λ_z。φ_zとμが可換対角なので共通固有liftを選べることを通常証明に明記。小整数行列A/右辺bを作り、Smith U A V=D全恒等式とdetU/V±1を検算。整数左核ℓでℓb≠0modNなら排除、保存111本のℓについてSmithと独立にℓA0/非零剰余を再検証。
因子条件も全Tへ適用：旧common-skew/pure-AS2に加え、指数u²z/vz²、uz skew、vz/zv/u²内のrank1関係なら向き別書換えで共通z因子。単純sampleでなく全S/T/character被覆。39中19ラベル全排除、20 Galoisラベル/45根集合、残位数5,6,7,8,9,12、全1306必要support片。各片はcharacter番号/S,T bitmask/正常gen bitmaskで小証明書に保存。非空・AS4・正常三次存在・H3十分性を主張しない。
通常証明はfour_simple_support_sieve節、公開verify_cubic_four_simple_support_sieve.py default Sympy全PASS、v284主原稿LuaLaTeX clean PASS。累計67validators across runs、単一67全再生未実行。全20ラベル/片はcertificateから再開する。新外部/as4入力なし、新規性未確認。

### 元orbit全非零層とLaurent torus閉包（v285）
20ラベルの全top orbit非零maskを走査した。rank1blockは完全rectangleが必要、全(r+1)minorの1項matchingは不可、2項はroot付きbinomial。純二変数U²内に支持されるsource列の空間はdomainでrank≤1なので、その全2minorも課す。pairに正確に支持される一つの列があれば（block全体に限らず）forcedskew、q_ij=−H_ji/H_ijで実orbit係数比へ戻す。
全binomialは整数Smith行格子（飽和しない、torsion全成分保持）でLaurent指数を正規化、係数をQQ(ζ2N)でexact加算。minorが1非零monomialなら全層排除、2項でroot比なら必要binomialを追加して閉包。3項以上の残余や非root係数比を勝手に零としない。normalizer top/G式も同じorbit係数へ課す。全S/Tと必要characterを保持して13ラベル/33根集合、23非零mask/157G-support。
さらに(7;0,1,2,4)の唯一mask/片を通常Ore証明で排除。base S(y,b,c)は三pairskew、x追加はδ(y)=d_yc²,δ(b)=d_by²,δ(c)=d_cb²、全d非零。逆向き係数/domainとB3dim20の全overlap零からB=S[x;σ,δ]。G=Ax³+B ybc双方、μx1なのでGx=xGがδ(ybc)=0を要求するが、δvolumeは三つの異なるPBW単項式yb³,y³c,bc³を全非零係数で持ち矛盾。
現行必要被覆は12 Galoisラベル/31根集合、22非零orbit層/156G-support片。ラベルは(5;1,2,3,4)、(6;0,1,2,3),(6;0,1,3,5),(6;1,2,4,5)、(7;1,2,5,6)、(9;0,1,4,7),(9;1,3,4,7),(9;1,3,6,8)、(12;0,1,4,10),(12;1,3,4,7),(12;1,3,7,10),(12;1,4,6,10)。全必要orbit係数A,bと各G bitmaskをcertificateに保持。
公開verify_cubic_four_simple_orbit_torus.py default Sympy/数体全PASS、v285主原稿LuaLaTeX clean PASS。C対角generator重みでA C^t0も検証、effective_dimension=m−rankA−rankCはtoric必要式だけの対角商次元、実AS4/moduli次元ではない。累計68validators across runs、単一68全再生未実行。

### 対角商零次元片の全数体判定完成（v286）
全81零次元必要片を整数Smith全torsion成分と対角torus作用で30点へ漏れなく被覆した。A C^t0、rankC=p−rankAを全片で確認し、連結対角torus像が解の単位成分と一致するので自由座標を1へ正規化できる。全有限成分を保持。共通根位数5,6,9,10,12,18のQQ(ζL)上で全点をexact判定：26点正常核0、3点B3dim22/B4dim46で非AS4、1点はN9(0,1,4,7)のB=S(y,b,c)[x;σ], σ=ζ9^6で正常核pure S3。既存一般cone頂点補題lem:cubic-skew-cone-vertexから最後の点もH3なし。通常証明はfour_simple_zero_dimensional節、公開verify_cubic_four_simple_zero_dimensional.py/certificateに全81片から30点への被覆と各exact rankを保存。default Sympy PASS、v286主原稿LuaLaTeX clean PASS。累計69validators across runs、単一69全再生は未実行。
現行必要被覆は5 Galoisラベル/10根集合：N5(1,2,3,4)51support片（toric商dim1/2/3の個数18/18/15）、N6(0,1,2,3)11片dim1、N6(1,2,4,5)9片dim1、N7(1,2,5,6)2片dim1/2、N9(1,3,6,8)2片dim1/2。合計75必要片。存在やH3十分性は未判定。Galoisラベルをintrinsic同型商と呼ばない。

### 正次元片の元rank条件と五曲線への削減（v287）
75正次元必要片にCの独立列のorbit係数1 gaugeを追加し、Smith全torsion枝を保持して16表示へ。全元weight blockの(r+1)minorを数体Laurent多項式としてexact計算、単項式単元を除く。N5の唯一dim3表示は二minorの差−4ζ10³で空。他14の非自明表示では全minorのgcdが実際にminorとして現れるのでrank上界locusは証明書の単一式と一致（一般点のみでない）。一つは全torus。有限になった12parameter点はQQζ20/24/28/36でfresh全Hrank6、B3/4=20/35、W1核0を確認して排除した。N6(1,2,4,5)ラベル全体が消える。
現行必要被覆は4 Galoisラベル/9根集合、五つの一変数表示。positive_rank_certificateのbranch0,3はN5(1,2,3,4)、branch7はN6(0,1,2,3)、branch10はN7(1,2,5,6)、branch13はN9(1,3,6,8)。元75片から全表示への被覆・位相・係数Laurent指数・全rank式を公開certificateに保持する。通常証明はfour_simple_positive_rank節、verify_cubic_four_simple_positive_rank.py/positive_finite.py default Sympy全PASS（後者のdegree被覆assert追加後も再実行PASS）。v287主原稿LuaLaTeX clean PASS。累計71validators across runs、単一71全再生未実行。

### 三・四固有値領域の全排除完成（v288）
全H3包絡の中山作用は相異なる固有値を高々二つしか持たない。四単純全体も排除した。単一固有値は1だが、単冪部分の自明性は未証明。全H3分類の完成ではない。
通常証明はcubic_four_simple_final_curves節、thm:cubic-four-simple-sector-empty。v287の五曲線branch0,3,7,10,13を各F=QQζL(t)で一変数化。元Hの六列source minorΔ、全次数商のpivot分子/分母、正常行列の全pivotと係数分母/parameter定義域を記録し、非零積P上で全底変更を保証。generic正常shape26×4,23×4,22×4,17×2,14×2は全列rank。Pの全数体既約因子を積へ掛け戻し、各既約性を確認し、E=F[t]/fで元H/商/正常行列をfresh計算した。全因子数11,5,13,8,9、定義域内因子数8,2,12,5,6、F上次数和20,3,23,11,9。全有効例外もHrank6、B3/4=20/35、正常核0。有限標本・数値根は使わない。
公開verify_cubic_four_simple_final_curves.py/certificateに全pivot多項式と全例外の数体係数・source/商/正常rankを保存。default Sympy PASS（因数積一致・既約性assert追加後もPASS）、v288主原稿LuaLaTeX clean PASS。累計72validators across runs、単一72全再生未実行。以前の全被覆の独立再監査、新規性確認、全homological証明の機械形式化とは呼ばない。
次の核心は単一固有値1の全CY・単冪持上げと、既分類領域を含む全intrinsic群oid・成分・相対降下。as4-reference固定SHA6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0のCY_COMPLETE/UNIPOTENT_UNTWIST本文とCOVERAGEを対象を絞って読んだが、全CY統合定理を新規監査済み入力として輸入していない。前者の有限許容atlasだけでは本研究の全幾何学的分類・成分・降下の完成にならない。

### 最大単冪Jordan4領域も全排除（v290）
中山が単一固有値1・サイズ4単一JordanブロックのH3は存在しない。通常証明はcubic_principal_unipotent_vertex節thm:cubic-principal-unipotent-empty。既存の単冪ねじり解除B=C^H,H=expNと正常三次輸送を使用し、as4の新しい全CY分類やprincipal存在定理は輸入せず元tensorから独立構成した。
反巡回66方向のN総作用核12を元256語で計算し、指定12語座標を単位化。col33純x0²からa11zero、a9zeroならpurecolumnが3a10+5a8zeroを強制し、x0,x1を殺した商が自由二元/(x2²)へ全射して指数成長矛盾。従ってa9unit1。top最高weight6は交代tensorだけ、六pairのsource minor±1、全関係が逆順commutator＋低weight。AS4 Hilbertと順序語の張りから全次数weighted PBW、grC可換poly。
N固定三次Fの先頭は可換Sym³N核（weight0,2,3）なのでweight≤3、J=(x0,x1,x2)のJ²に入る。HはJを保ちBtwist後もJ²は同じ。P=πk[x3]の全tails自己拡大を2×2行列で構成し、x3恒等化後のJ三成分はA f(n+1)=D f(n)、A,D下三角対角1。元全係数のまま検証。F∈J²は一次条件を課さず、Ext1(P,P)3次元、shift単冪det1。一般のSerre trace補題b(v,w)=−b(Tw,v)からdimE奇数ならdetT−1が必要となり矛盾。S(P)=P[2]だけから作用恒等と仮定していない。
公開verify_cubic_principal_unipotent_cover.py/vertex.py default Sympy PASS、対応certificateに元12核、全rank6三枝とA/B全係数gauge、weighted六関係、拡大monodromy、可換三次核を保持。coverは幾何学的必要被覆でAS十分性を主張しない。v290主原稿LuaLaTeX clean PASS。累計74validators across runs、単一74全再生未実行。Serre/tailsの通常証明を機械形式化したとはしない、新規性未確認。

### 単一固有値のJordan(3,1)も全排除（v291）
全18元CYtop核を独立構成し、col22=a6 x0²からa6zero。a12zeroならcol12=a4 x0²でa4zero、x0,x3を殺した商が自由二元/(x1²)へ全射し指数成長矛盾。従ってa12unit1。weight(0,1,2,0)の元六関係unitminor−1、最高項はgrC=k[x0,x1,x2][x3;δ]、δ=(h x0²,h x0x1,−3h x0x2+2h x1²),h=a4。AS4 Hilbert＋順序語の張りから全次数weighted PBW。Nδ=δN、Nx3zeroなのでPBW上Nは可換baseだけ、三次核6次元/最高weight2。F Nfixed⇒F weight≤2⇒J=(x0,x1,x3)のJ²。全係数のpoint P=πk[x2]の自己拡大はExt1=k³、shift M=[[1,0,0],[1−2a11+3a16a4−a7−2a9,1,a16−a14],[3a4,0,1]]、det1, (M−I)³0。前節のgraded Serre determinant補題で全Jordan(3,1) H3 empty。通常証明cubic_jordan31_unipotent_vertex節、公開checker/certificate default Sympy PASS、v291主原稿LuaLaTeX clean PASS。累計75validators across runs、単一75全再生未実行。新規as4定理輸入なし、新規性未確認。

### 単一固有値のJordan(2,1,1)も全排除（v292）
通常証明cubic_jordan211_ore_vertex節thm:cubic-jordan211-unipotent-empty。元32CYtopでweight2唯一のcolzz純x0²をdomainで消し、残topweight≤1。weight1三次tensorfの両端収縮空間Qは、dim≤2ならdecomposable二次を含む（片端rank1又は両端2の支持A,Cを比較、A=Cならbinary determinant）。従ってdomainがrankM≥3、middle rank6が≤3を与え、rankM3/I2∩U²=Q3。
混合射影の片側核はuz+q又はzu+q、Nを作用してux0/x0uの関係となるためdomainで不可。両側同型からOregraph。N^d(Σs_i z^i)=d!s_d x0^dで冪独立、σ/δが実baseSへ降りC=S[z;σδ]、HS=(1−t)^−3。基礎AS3を仮定で追加しない：top四収縮の一つはpuref、他三つのmixed成分独立なのでS0=T(U)/QのW3dim1、S0_3dim10=実S3。σQ/δQは次数2/3で既にS0に零、Ore構成からS0=S。domainとHilbertEulerで線型1331複体完全、f両端非退化でKoszul AS3。noetherianはOre自由基底で降下。
H3正常FはNfixed、上の冪独立からF∈S3。B=C^Hも同じbase上のOre、normalizerH4はS固定/z→z+4x0。新一般lemma:cubic-derivation-Ore-vertexで排除した。導分付きOre B=S[z;σδ]、S noethKoszulAS3、G∈S3正規正則、θS=S,θz=λz+hならR=(S/G)[z;σbarδbar]。M=k[z]のExt_B集中3（S自由基底/AS3）、ReesでExt_R集中2、ASGor parameter1局所双対から全O(a)に対するP=πMのHom-acyclicityとHomdim1。基礎A=S/Gの最小解消をRへ誘導しExt^n(P,P)=β_n^A(k)。1/HA=(1−t)²/(1+t+t²)非多項式で無限高次Ext、H3に矛盾。z正常/未証明局所化を仮定しない。
公開verify_cubic_jordan211_ore_reduction.py/certificate default Sympy PASS（元32kernel/block/全収縮/自由語微分）。全rank-domain/AS3降下/局所双対は通常証明であり機械形式化としない。v292主原稿LuaLaTeX clean PASS。累計76validators across runs、単一76全再生未実行。新as4定理輸入なし、新規性未確認。

### 全単一固有値のCY性完成（v293）
単一固有値のH3包絡は必ずCY（μB=id）。最後の非自明単冪Jordan(2,2)も全排除した。通常証明cubic_jordan22_unipotent_vertex節thm:cubic-jordan22-unipotent-empty。元26反巡回N核、U=(x0,x2),V=(x1,x3)、V個数weightで最高2。純U²/V² sourceQは対称4×4、binary domain boundからrank≤1。Q0はrankH6とblockrank2rから純U²関係が3次元以上になり矛盾。従ってQ=qq^t≠0、q二次係数2×2可逆。Nを保つ同時GL2変換でq量子(0,1,−p,0),p非零又はJordan(1,1,−1,0)。mixed最高block5minor−p²(p−1)²(p+1)²、rankH6がmixed≤4を要求しp±1だけ残る。
可換・反可換・Jordan三chart全て元source principal6minor−1、最高逆順pairminor±1、U/V両AS2とVU→UVによりx0^i x2^j x1^k x3^lが張る。実AS4 Hilbertとの比較で全次数grC同定。最高三次商20dimの全N核は6dim/weight≤1、ゆえF Nfixedはweight≤1⇒J=(x0,x1,x2)のJ²。P=πk[x3]自己Ext1dim3、全低weight係数のままtwist後monodromy三型のdet1を検証。反可換ではdiag(−1,−1,1)で単冪でないが、odd-Serre determinant補題はdet1だけで排除する。全特殊値もunitpointpivotで保持。
公開verify_cubic_jordan22_unipotent_vertex.py/certificate default Sympy PASS、全26核/最高rank1/三chart/最高PBW/N三次行列と全6核/全point漸化式を保持。v293主原稿LuaLaTeX clean PASS。累計77validators across runs、単一77全再生未実行。通常の被覆/PBW/tails/Serre証明を機械形式化したとはしない、新規性未確認。新as4外部定理輸入なし。
全体の次の核心は全CY包絡の中央三次切断。三・四固有値全排除、単一固有値非CY全排除、既分類二固有値全Jordan領域を保持し、未処理Jordanへ戻らない。全intrinsic群oid・成分・相対降下も未完成であり、全H3完成と呼ばない。

### 全CY必要被覆の第二二次関係入力を局所全枝で検証（v294）
as4固定SHA6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0のNONDEGENERATE_CHARTとDEGENERATE_CHART_SECOND_QUADRICを必要範囲だけ輸入した。仮定：標数0代数閉体、P3上独立六二次式、rank6二次関係、像次元3。結論：独立な第二二次関係。接空間rank3/2の全Witt正規化、退化DC1–DC15の全整除枝と恒等特異/巡回pencil、非退化の一般対称Mの第二関係を本文へ通常証明付きで統合した。独立checkerでsyzygy rank10/parameter8、両非整除8線型条件、unit標的変換、二quadric、一般pencil行列式、恒等特異枝のrank3関係、一般16係数Tの外積、companion独立証拠−1、一般対称Mと交代部分除去をdefault Sympy exact検証PASS。主原稿v294 LuaLaTeX clean PASS（bibliography長名はallowbreakで修正済み）。累計78validators across runs、単一78全再生未実行。
証明cubic_CY_second_quadric節、verify_cubic_CY_second_quadric.py/certificate。as4_imports.jsonに固定SHA/全entrypointと証明hash/仮定/元audit pending/今回独立計算範囲を登録。全CY_COMPLETE、CI22全chart、AS十分性、全同型、Veronese除外の独立監査までは輸入していない。

### 零交換子CYの全像をCI(2,2)へ必要被覆（v295）
固定as4のVeronese排除を必要範囲で輸入し、全元データを当repoで独立再生した。Veronese21積rank15、対称係数rank1/2/3→関係rank3/4/6、全CY混合25核/全57係数cyclicrank31/KKrank20、同変等長Φとsl2二作用、全六最大等方planeと10三次係数のintegrable kernel、全三次正規化、零三次自由積lower25、全八非零代表の線型解/残余ideal、前四実平方/次二unitideal、最後二の全Ga3orbit（Jac8/27,−72）/両符号をdefault Sympy exactで確認。二representativeの元Hilbertは独立GradedAlgebraでalpha(1,4,10,22)、beta(1,4,10,20,37)、全候補非AS4。上流fullverifier isolated replay（flint）と当repo独立再生を区別。最小固定proof input19KBと新certificate/validatorを保存し、as4_importsにsourcecommit/hash/仮定/元audit pending/独立範囲を登録した。
通常証明cubic_CY_Veronese節prop:cubic-CY-Veronese-excluded,thm:cubic-CY-zero-commutator-CI22。CYc0は関係graphからSSrank6、その全対称化零が非退化Q関係。像次元r≤2ならrankr点の線型切断P^rを選び、Urestriction6dimからr2/fullVeronese像。rank1 symmetric3matrixを原始vector平方へ戻し、gcd/付値/次数から元U=Sym²Wを復元して上の排除に反する。従って像3dim。v294第二quadとrank6quadconeのfactoriality（z0prime,localLaurentpoly,素因子降下）から高さ1imageideal生成次数2、整CI22となる。全CI22上の包絡・切断分類やAS十分性ではない。
公開verify_cubic_CY_Veronese.py/input/certificate default Sympy PASS、v295主原稿LuaLaTeX clean PASS。累計79validators across runs、単一79全再生未実行。全CY分類・全CI22代数chart・幾何証明の機械形式化・新規性は未確認。

### 零交換子CYの七必要対称射影型を全被覆（v296）
通常証明cubic_CY_CI22_projection_atlas節thm:cubic-CY-CI22-seven-projections、固定as4のQUADRIC_PENCIL_PROJECTIONSから必要幾何被覆だけ輸入。CI22二次鉛筆Q/P、T=A^-1Hの接形式退化条件q^tAT²q0から常時退化iffT²∈span(I,T)。最小多項式2で二根ならrank1/2関係不可から3+3直和二Veronese=D、重根なら自己共役N²0rank3でrank3関係a²,ab,b²と全syzygy(−bℓ,aℓ−bm,am)、ℓ,m mod<a,b>独立からL。非退化point側は一般対称M表示でbaseZ≅smoothconic(B=0)のr-cut長さ4、全三base-elimination恒等式を確認。超平面に含まれないことから線型全section埋込み、U=I_Z2、curvilinear長さ4の全分割1111/211/22/31/4で五型。これらは中山Jordan型ではなく対称射影基点scheme型である。
公開verify_cubic_CY_CI22_projection_atlas.py/certificate default Sympy PASS：全七Uの21積rank19/二relation全kernel、全pencil determinant/T²criterion、五有限algebra乗算全kernel、binary quadratic syzygy rank22/nullity8、Lmarked関係全shear、一般M三basepoint恒等式、五symmetricM例のconic四次根型。v296主原稿LuaLaTeX clean PASS。累計80validators across runs、単一80全再生未実行。as4_importsに固定sourcehash/全仮定/被覆だけのscopeを登録。全AS4係数normalform・切断・群oidは同時輸入しない、新規性未確認。

### 全零交換子CYのD/L二射影をH3から全排除（v297）
必要係数全被覆を既存二族排除へ接続した。通常証明cubic_CY_DL_cover節thm:cubic-CY-DL-cover-empty。Dはrank6markedAを二Veronese判別式へ正規化、全mixed22/γ0/二binary discriminant−1/4、SL2×SL2で内部標準形、rank8線型系が八係数zero、残六binomialを全再生。domainが四係数pair非零を強制し、非零support二枝I/IIだけ。根R²=U/p又はR⁴=1/(p³r)のみの対角変更で(1,h,1,−h)全h非零へ。RS=TUも根idealで確認しmarkedA保持。元16語関係が既存D_I/II(h)と非零定数basis変換で全h一致し、thm:as4-double-cover-h3-exclusionで全排除。AS4存在十分性/全同型は輸入しない。
Lは全mixed22とSchurdiscriminant2(v1²−4v0v2)、一般四係数GL2でv変換Sym²T/det²を全tensorframeで確認、v0/平方v(1,0,0)の全二枝へ。v0はfree二元quotient、平方枝は全linear条件と四polynomiale_iの二恒等式から特殊zを除外せずu=w=p0、実a²sourcecolumnでdomain矛盾。全zero/非zero各場合の全値排除。
公開verify_cubic_CY_DL_cover.py/certificate default Sympy PASS（双方22核/混合cyclicrank14/全57係数rank34、D全normalization/全値旧表示移送、L全GL2・全分岐）。v297主原稿LuaLaTeX clean PASS。as4_importsは固定6f798...のDCC4–12/LBE2–10の必要範囲のみ登録。累計81validators across runs、単一81全再生未実行、新規性未確認。
残るCYc0の必要射影は有限基点五型1111/211/22/31/4。次は4と31の全必要係数被覆を、既存thm:as4-curvilinear4-h3-exclusion（CF2/CF3/CT2の中心3zero）へ接続する。固定sourceCURVILINEAR_FOUR_COMPLETEの必要CF6–13、CURVILINEAR_THREE_ONE_COMPLETEの必要CT3–17を全文読んだ（AS十分性と全Autは不要）。CFは全mixed21、全Ga4/トーラスnormalization、四emptybranches、五先頭tupleCF13、うち二empty/一Hilbert4dim37/二fixed CF2CF3。CTはx0/x10非零empty、x9非零全有限/一parameterHilbert4>35、x9=0二cube恒等式でx11=x15zero、x12非零二族のgenericHilbert4dim37又はdegree5dim62（必要56）で全特殊値排除、最後x17unit枝CT14六式からx1nonzeroが唯一CT2、x1zero三族allclosedHilbert4≥39/39/42。全family原関係の分母は記載unitだけで、genericrank上界により全閉値でdim下界を用いるので、generic商基底の無条件特殊化とは別。
次は固定source二verifierの必要controlを孤立workspaceでreplay（referenceを変更しない）し、最小proofdataと当repo独立raw quotientでbad代表/familiesをfresh確認する。正常CF2/CF3/CT2自体の中心排除は既に済みで再計算不要。全候補必要被覆のmetadata/通常証明を追加する。射影22/211/1111のAS4係数全被覆、全CY切断・群oid・成分・相対降下は未完成。

### 有限基点型4・31の全必要係数被覆とH3排除（v298）
通常証明cubic_CY_finite43_cover節thm:cubic-CY-finite43-empty。固定as4のCF6–13/CT3–17だけを必要被覆として利用し、全上流controlを隔離workspaceで再実行PASS。当repoの独立default exact controlもPASS：二つの全21混合frame、六空chart、CF先頭五tuple、全14非正則代表・族の元商次元、既存CF2/CF3/CT2への定数可逆な関係移送。非正則族の全閉値下界は、明記したunitだけを反転した元全語関係行列のrank特殊化で正当化する。CTのmu=-1例外は自由yも保持、x12境界は五次62>56を用いる。CF先頭消去式はv²(2v+1)(7v+1)であり、五tupleの幾何学的被覆を被約scheme/相対被覆と主張しない。
公開verify_cubic_CY_finite43_cover.py/input/certificate、主原稿LuaLaTeX clean PASS。固定source/hash/必要範囲をas4_importsへ登録。累計82validators across runs、単一82全再生未実行。上流通常証明の全gauge被覆と当repo独立商計算を区別し、AS十分性/全Aut/新規性を同時輸入しない。
残るCYc0必要射影は1111/211/22。次は固定CURVILINEAR_TWO_TWO_COMPLETEのTT1–14必要被覆を既存A/B/D/C_r/E_t/F_hの全値排除へ接続する。本文の必要枝は読了：全21frame、kappa非零二bad族(dim4=38/40)、kappa零mixed非零三bad族(dim4=39/42,dim3=21)、最終r=±1/4族(dim3=24)、実平方枝、六正則表示への全正規化。TT15以降のAS十分性/全Autは不要。次は固定verifierを隔離再実行し、最小データから全bad族の元商と六表示移送を独立確認する。全CY中央切断、全群oid・成分・相対降下は未完成。

### 有限基点型22の全H3排除（v299）
通常証明cubic_CY_finite22_cover節thm:cubic-CY-finite22-empty。固定as4のTT1–14必要全係数被覆だけを利用。固定全controllerの隔離再実行PASS、当repo default独立controlもPASS：全21mixed/cyclicrank15、N/T/W印付き共変性、九つの非正則代表・族の元商(dim4=38/40/39/42、dim3=21/24)、六表示のliteral移送とA両符号。全自由係数閉値は元関係行列rank特殊化と明示unitだけの分母で保持。残るA/B/D/C_r/E_t/F_hは既存三排除定理で全H3なし。公開verify_cubic_CY_finite22_cover.py/input/certificate、主原稿LuaLaTeX clean PASS。累計83validators across runs、単一83全再生未実行。AS十分性/全Aut/被約相対被覆/新規性は輸入しない。
CYc0残る必要射影は1111/211。次は211の三不変層x0非零、x0零x15非零、双方零の必要被覆。固定DOUBLE_SIMPLE_NONZERO_COMPLETEのDS1–10、SECOND_COMPLETEのDT4–11、FINAL_EXCLUSIONの全DZ1–20を読み終えた。前二層の残存全表示L±/T/P/U/V/A_lr/B_rは既存ds211節で全パラメータ排除済みなので再計算不要。最終零層では元Hilbert5=57の二族、四次36の四代数点、Hilbert7=123>120のM0/M1族、その他degree3/4/5障害を含めて必要被覆を確認する必要がある。現在三固定controllerを隔離逐次replay中。次は最小proofdataと当repo独立元商検証で接続する。全H3分類・CYc>=1・群oid・成分・相対降下は未完成。

### 有限基点型211の全必要被覆とH3排除（v300）
通常証明cubic_CY_finite211_cover節thm:cubic-CY-finite211-empty。固定as4のDS1–10/DT4–11/DZ1–20必要範囲を輸入し、三全controllerを参照checkoutを書き換えず隔離出力先で逐次replayし全PASS。当repoの独立元商controlも全27代表・族PASS（python-flint使用、default Sympy全実行PASSとは主張しない）。全21mixed/cyclicrank15、全N/T/W印付き群、D00=4x0x15、全非正則族の元商と全分母unitを確認。新しい疎pivot/右乗算だけの再帰商では各段階で全元関係挿入の座標像零も確認。最終零層22候補はHilbert5=57/60、四次36/39/42、三次21/22/23、二つのM族のHilbert7=123>120。係数共役も保持し、全閉値は元全語rank特殊化で下界保証。第二層5族も三次21/22。残る第一層全7表示と第二層二族は既存ds211の全パラメータ排除の元関係と一致。AS十分性/全Aut/相対scheme被覆は輸入しない。
公開verify_cubic_CY_finite211_cover.py/input/certificate、主原稿LuaLaTeX clean PASS。再現はPYTHONPATH=/workspace/work/python-deps SYMPY_GROUND_TYPES=flint python computations/verify_cubic_CY_finite211_cover.py --flint。累計84validators across runs、単一84全再生未実行、新規性未確認。
残るCYc0必要射影型は1111のみ。FZ2量子型Qもq_ij!=1のCY skewなので、既存lem:cubic-cy-skew-zero-commutatorにより全H3排除済み。全skew領域一般のH3とこの必要射影型のQを区別する。既存four_simple節のS/Q/O/H/L/M/F/G/K/J/R/N/C/adjacentL/S/T/fullPの表示別認識・全値排除を再計算せず、必要被覆を接続する。固定CI22_COMPLETEの支持被覆全文、FIRST_SHAREDの必要FN1–6、SHARED_ZEROの必要FZ1–10、INACTIVE_SHARED_VERTEX_EXCLUDED、SINGULAR_RANK_ONE_EXCLUDED、SINGULAR_RANK_TWO_EXCLUDEDの全文、FULL_SHARED_INVERTIBLE_REDUCTIONの必要FT1–12を読んだ（全AS十分性/Autは不要）。通常証明と各controlの局所化をこれから監査する。
独立な私的支持走査では4096有向支持は218 S4軌道、zero/degree1/degree2/partial_active/fullの支持数1/3471/609/14/1、軌道数1/173/40/3/1。全置換とdegree1/2標準chartの存在も公的元frameと合わせて検証・統合するのが次の小補題。部分活性三軌道・全共有可逆/特異枝を無条件に飛ばさない。CYc>=1中央切断、全群oid・成分・相対降下は未完成。

### 四単純基点の全元frame・支持被覆と共有零層の全排除（v301）
通常証明cubic_CY_four_point_support節lem:cubic-CY-four-point-support/thm:cubic-CY-four-point-shared-zero-empty。元FS21混合方向/一KK方向の全CYframeを独立証明：混合rank15、KKrank20、joint57rank35。全24置換の印付きlambda変換・B全21係数・gアフィン変換・共有辺単元、対角d_i/d_jを元行列で全検証。全4096支持/218軌道をzero/degree1/degree2/partial-active/fullへ支持数1/3471/609/14/1、軌道数1/173/40/3/1と被覆し、degree1/2標準chartへの全置換存在を検証。
共有零の全Schur対角六条件/残余三式/相補積恒等式を独立に再生した。ABC零は全非零S又はH0/H1、ABC非零は全相補積零からQ又はOへ全被覆。全torus規格化は独立三整数重みと代数閉性だけ。Oの四禁止A値には元係数1の実積関係がある。Qは全六対の二項式係数和1、Thetaと六係数積の比が単元、F=0下の全四CY行積を確認。従って全q_ij!=1であり、既存lem:cubic-cy-skew-zero-commutatorから中心三次は高々一本の純三乗。S/Q/O/H全て既存全値排除に接続し、共有零層全H3なし。
v300の再開文に「Qにはskew H3が残り得る」とした記述を訂正した。全skew領域一般のH3と、全q_ij!=1が必要なこの射影型を混同していた。該当現行notes全てを訂正し、量子型を未解決へ戻さない。
公開verify_cubic_CY_four_point_support.py/shared_zero.pyと小certificateはdefault Sympy exact全PASS。主原稿LuaLaTeX clean PASS。累計86validators across runs、単一86全再生未実行。固定as4 FS1–2/FZ1–10の式だけを出典化し、必要被覆そのものは元行列と通常の全場合分けで当repoに証明。新規性/AS十分性/全Aut/相対被覆は主張しない。
次は非零共有支持の必要係数chartを接続する。degree1のx0zero最初の共有chartは固定FIRST_SHAREDのFN1–6を読了、八bad境界は元三次dim21/22、残るL/M/F/G/Kは既存全値排除。固定fullcontrollerを隔離as4-fs-auditでreplay中（v302ログ）。次は最小必要proofdataから八bad元商と既存表示移送を独立確認する。degree1のx0nonnull、degree2、部分活性三軌道、全共有可逆/特異層はまだ必要被覆を統合していない。CYc>=1中央切断・全群oid・成分・相対降下も未完成。

### 最初の非零共有chartの全H3排除（v302）
通常証明cubic_CY_four_point_first_cover節thm:cubic-CY-four-point-first-empty。x1!=0,x0=x3=x4zeroと全monomial軌道を全排除。固定FIRST_SHAREDの必要FN1–6と全controller隔離replayPASSを使用し、当repoでも全21係数の四枝(x2,x5)=00/01/10/11の全消去式を元Schur行列から一手ずつ独立再生した。各式が実際の残余式であること、一次pivotがlambda/lambda+1だけの単元であること、代入式・最終残余の一致を確認。四主飽和idealも再計算。八bad境界の元三次商21/22、全元関係挿入の座標零・分母unitから全閉値障害を確認。残余全係数FN2の四制約idealへの逆代入と、既存fn_matrixのliteral一致を検証。通常の全対角規格化でL/M/F/G/Kに全被覆し既存全値排除を適用。
公開verify_cubic_CY_four_point_first_cover.py/input/certificate exact PASS（python-flint ground使用）、主原稿LuaLaTeX clean PASS。累計87validators across runs、単一87全再生未実行。v300の疎Hilbert classを共通cubic_sparse_hilbert.pyへAST同一のまま移し、class AST一致と旧211 transport-only controlを実行PASS。全211をもう一度走査したという意味ではない。AS十分性/全Aut/相対scheme被覆/新規性は主張しない。
次は出次数1のx0nonnullで行列式x0x2-x1²nonnullの二openchart。固定SECOND_SHARED_OPENのFO1–5とZERO_FIFTH_OPENの必要FZ1–6を読了。前者は全lambda/lambda+1/p-1だけの消去からq=x10nonnull空、qzero唯一H(lambda,p)へ。後者はqzeroでlambda1のM0/M1、p0は既完成firstchartへ直接移せるのでH3排除、pqnonnullは二factor枝で(lambda,p)=(1/2,-2),(2,-2)、四共役候補は既存Nへ。既存H/M/N中心排除は全値完成済みで再計算不要。二固定fullcontrollerを隔離逐次replay中(v303ログ)。次は必要trace/GB/normalcoefのみ抽出し当repoで元消去と移送を独立再生する。残る行列式零のgeneral/zero-fifth境界、出次数2、部分活性三軌道、全共有可逆/特異の必要被覆も未統合。CYc>=1/群oid/成分/相対降下は未完成。

### 出次数1の二つの行列式非零chartの全排除（v303）
通常証明cubic_CY_four_point_two_open節thm:cubic-CY-four-point-two-open-empty。x0*x1!=0,x3=x4zero,x0*x2-x1²!=0をx5zero/nonnull双方で全H3排除。固定必要FO1–5/zero-fifth-open FZ1–6と二全controller隔離replayPASSを使用。当repo default独立exact controlもPASS：全元21係数消去を式・単元pivot毎に再生、FO q(u-v),q(pu-v)の局所ideal所属とqnonzero空ideal、qzero全係数H(lambda,p)を確認。FZ qzeroはlambda-1の単元倍からlambda1/全M(p,r)係数、pzeroは元全matrixで既完成firstchartへ移送。pqnonnullは二factor枝それぞれの飽和idealを三必要有限条件と完全比較。残りx6/x7/x9は数体idealに各正冪が入り幾何学的に全zero。全四共役候補は具体P/対角/可逆関係基底で既存Nへliteral移送。既存H/M/N排除へ接続しAS十分性/全Autを輸入しない。
公開verify_cubic_CY_four_point_two_open.py/input/certificate default exact PASS、主原稿LuaLaTeX clean PASS。累計88validators across runs、単一88全再生未実行。有限残余idealの被約性・相対scheme被覆・新規性は未主張。
次は出次数1の残る行列式零二境界。固定GENERAL_BOUNDARY必要FG1–5、IMAGINARY_BOUNDARY必要FI1–4/h0五次58障害、ZERO_FIFTH_BOUNDARY必要FB1–9を全文読了（AS十分性/全Aut不要）。前者は全lambdaからR_eta(lambda)又はlambda=±iのJ_eta(h)、h0二点はHilbert5=58>56。後者はx17nonnull空、二factorA/B、七必要係数行と八種特殊結合係数境界を漏れなく扱い、genericbad四次37、lambda^4+1全根五次59、lambda²+1全根五次58、残るN/C/R±1は既存全値排除済み。三固定fullcontrollersを隔離逐次replay中(v304ログ)。次は必要入力抽出と独立元商/例外全数体/表示移送を作る。境界の一般点だけで済ませない。出次数2、部分活性三軌道、全共有可逆/特異の必要被覆、CYc>=1、群oid・成分・降下は未完成。

### 第五係数非零・行列式零境界の全H3排除（v304）
通常証明cubic_CY_four_point_determinant節thm:cubic-CY-four-point-determinant-empty。x0*x1*x5!=0,x3=x4zero,x0*x2-x1²zeroと全monomial軌道を全排除した。固定GENERAL_BOUNDARY必要FG1–5を使用し、一般境界/純虚境界の上流全controller隔離replayは双方PASS。当repo default exact controlもPASS：全21係数の二段階消去を元残余式・lambda/lambda+1単元pivot毎に再生、16(x15-x16)²+1とx9(16x9-lambda²+1)の全split、QQ(i)上の全二飽和idealと明示targetidealの一致。全R_eta(lambda)とlambda1重複は既存r_matrixにliteral一致。形式lambda固定の符号共役とlambda±iの全四fiberは、hを割らず可逆原関係基底で既存J_eta(±h/±ih)へliteral移送。既存prop:cubic-boundary-Jがh0のHilbert5=58も排除済みなので、同じ固定点のHilbertを新規に再計算したとはせず再利用。AS十分性/全Aut/相対scheme分類は輸入しない。
公開verify_cubic_CY_four_point_determinant.py/input/certificate default exact PASS、主原稿LuaLaTeX clean PASS。累計89validators across runs、単一89全再生未実行、新規性未確認。
次の核心は第五係数零・行列式零の最後のdegree1境界。固定ZERO_FIFTH_BOUNDARY必要FB1–9は全文読了、上流fullcontrollerも隔離replayPASS。x17nonnull空、x17zeroの二因子分岐、FB3/4所属と三generic/三例外baseideal一致、全七基本行±符号、FB7/8の全結合rank低下を扱う。badは16記録：genericAm/Apの四次37、Az/B三次21、Apのlambda^4+1全四根五次59とlambda²+1全二根五次58、Az(-1/2)/B(-2)特殊coupling三次21、全±符号。原係数分母だけを管理して全閉値下界を使う。残るA1(r)はr0で旧C/共役、rnonnullで旧R±1、Ah/Bh四点は旧Nに移るので既存中心排除を再利用できる。
次は最小必要trace/linear matrix/元badnormalだけを抽出し、元Schur消去・基本ideal比較・全coupling例外・独立元商/全数体・旧表示移送を作る。完了すれば全degree1支持3471個/173軌道がH3なしとなるが、まだその結論を先取りしない。degree2の609支持/40軌道、部分活性14支持/3軌道、全共有1支持/1軌道、CYc>=1、全群oid・成分・相対降下は未完成。

### 全出次数1共有支持の排除と停止時の再開点（v305）
通常証明cubic_CY_four_point_zero_determinant節thm:cubic-CY-four-point-zero-determinant-empty/cor:cubic-CY-four-point-degree-one-empty。最後のx5zero行列式境界を全H3排除し、全degree1支持3471個/173 S4支持軌道のH3なしが完成した。共有零支持も排除済みなので、全CYc0の残る必要支持は624個/44軌道：degree2が609/40、部分活性14/3、全共有1/1。これを存在するmoduli成分数・intrinsic同型類数と呼ばない。全H3分類は未完成。
固定FB1–9と上流fullcontroller隔離replayPASSを使用し、当repo exact controlも全PASS（python-flint ground使用）。元21係数からのx17nonnull単元矛盾/zero枝全消去、二split所属、七基本係数行の全局所ideal比較、両符号の全coupling行列・genericと例外rank/kernel/x9一意性、全16bad元商・全元関係挿入の座標零を確認した。genericAm/Ap四次37、Az/B三次21、lambda^4+1全四根五次59、lambda²+1全二根五次58、残る二有理特殊値三次21。全数体は既約性/minpolyと元係数評価で全共役を保持。元分母のunit管理とraw rank特殊化で全閉値下界を保証。全kernelのtorus規格化、旧C/係数共役、両R1への元移送、全四N点への可逆原関係基底移送を確認。旧C/R/Nの中心排除を新規に再計算したとはしない。
公開verify_cubic_CY_four_point_zero_determinant.py/input/certificate。累計90validators across runs、単一90全再生未実行。AS十分性/全Aut/相対schemeの被約性・降下・新規性は輸入しない。主原稿LuaLaTeX clean PASS（446頁）。
ユーザーの「切りの良いところで止まって下さい」に従い、この全degree1排除を停止checkpointとする。次の計算・上流controllerは起動しない。再開時は00_research_plan.mdとAGENTS.mdを読み、現在のmainから始める。次の数学的frontierはdegree2の全必要係数被覆（adjacent sharedのx0zero/x5zero/corner、開部分排除、全境界候補T/L/Sを既存全値排除へ接続）、次に部分活性三軌道と全共有可逆/特異支持。これらの必要証明の全面再監査・独立計算は未完了であり、まだ全CYc0空とは主張しない。CYc>=1中央切断、全群oid・成分・相対降下も未完成。
固定as4のAZ・AF・AV・AO・ABの必要被覆と既存L/J/S/T排除を接続し、出次数2の頂点を許す四単純基点型を排除した。本文は cubic_CY_four_point_degree_two 節。AO2両符号の元三次商は独立計算で次元21、分母は許容単元のみなので全閉値にも下界21が成立する。残る零交換子CYの必要支持は部分活性14支持・3軌道、全共有1支持・1軌道。次に部分活性の必要排除と全共有の可逆・特異主ブロック被覆を接続する。

### 部分活性支持から全共有支持への還元（v307）
固定as4のIV1–IV13を必要条件として接続し、零交換子CYのH3では四単純基点で十二共有係数全非零が必要となった。部分活性排除の証明依存先はas4_imports.jsonに固定した。次に全共有の可逆主ブロックFT1–FT12を既存P全排除へ接続し、全主ブロック特異の場合の階数1・2を監査する。

全共有支持についても、固定FT1–FT12から既存P全値排除へ接続し、全主ブロック特異の階数1・2は固定as4の必要排除を適用した。これで零交換子CYを全排除する。既存 cor:h3-cy-commutator-reduction と合わせると、非可換CY包絡で残る交換子次元は1,2,3であり、三交換子beta型は既排除。次はそれらの中心三次切断を判定する。上流全証明の独立再実装はしていない。
### 二交換子の残る孤立型
非共有Segre、混合階数一Veronese、混合階数二の全VRパラメータ族を排除した。本文 cubic_CY_two_commutators_Segre 節。特にVRでは正常元aの平行移動の先頭核から中心元をk[a,b,tac+βbd]に絞り、cとの交換で中心三次が零となる。次は固定VTの孤立型Iについて元六関係から中心三次を判定し、二交換子の七対称射影の必要全被覆を監査する。

二交換子の孤立型Iも元VT行列から中心三次rank20（有理小行列式 -32768/22876792454961）で排除した。固定as4の cor:cy-two-commutators-complete の必要方向と合わせて全二交換子CY排除。残る非可換CY包絡の交換子次元は1又は3（3のbeta型は既排除）。次は一交換子の十六必要射影と三交換子の残る層で中央切断を判定する。

### 中心・ノルム障害による一括削減（v310）
一交換子・非共有Segreの二直線追加型は既分類skewだけに帰着し、二平方追加型の外側交換子九表示は全排除した。固定必要表示23個で商射影の全例外数体を再計算。残った内部型H_sの原始三乗根では、交差項abがあると中心三次は二元で可約。f=a²+b²でもa-局所化の三次シンボルはk(v)上の滑らかな有理二次曲線上で全剰余零、FaddeevとTsenにより分裂する。論文cubic_CY_one_segre_extensions節。既存skewの合同を再分類に含める必要はない。
三交換子混合の外積階数一（七係数全域）はcubic_CY_three_mixed_rank_one節で排除。dの個数濾過で[d^n,a]の先頭は2n(bc+μa²)d^(n−1)で、中心は基礎三元環に含まれる。その中心三次a³,ab²,ac²は共通一次因子aを持つ。
次は一交換子二平方の交差有限・無限遠チャートと、三交換子外積階数二の共有した濾過条件。前者の有限2変数では、疎な商射影と中心小行列式の開被覆を試し、残余点だけ原関係へ帰る。中心零・共通因子・巡回分裂を先に調べ、包絡側の全自己同型の再分類を避ける。

### 一交換子の二平方と三交換子の構造的削減（v311）
一交換子・二平方追加Segreを全排除した。交差チャートの元トップから定数minorで六関係を復元し、固定as4の有限(p,t)・無限遠(e)とのliteral一致を確認。中心20次minorと次数別商射影の全因子から、有限残余は p=0,-2,-2/(t+1),-2/(2t+1),2/(t-1) の五曲線。各曲線の元関係から再計算すると例外は許容域外だけで、中心三次は全域零。無限遠はe=0を別QQ計算し全域零。通例のAS4次元20,35だけを特殊化に使った。
三交換子外積階数二は三係数層を一括排除。固定as4の反射型融合積の交代語基底を使い、次数三の奇数語と長さ二語は基礎a,bへの作用が非恒等なので中心に現れない。残る基礎の重み二変数Zの係数も二対合の一次固定空間の交わりが零。従って中心三次は可換二元で全て可約。外積階数三の列係数階数二は対称関係Cliffordへの二次ねじりで、任意の中心三次が中央二次{a,d}を反転して矛盾。alpha零先頭式二表示はa=1の中心の濾過次数が2以下なので共通因子aで排除した。
現時点の主要残余は、一交換子の非共有Segreの平方・二直線を両ブロックに加えた二型、共有Segreの十一型、および三交換子のalpha非零先頭式と外積階数三・列係数階数三。必要被覆および切断条件は別々に記録。次の具体的な一手はalphaのa=0におけるAS3中心三次を全先頭型で調べて中央三次のliftを絞る。同時に他のSegre候補は元関係から中心零・可約・twistの中心障害を先に見る。全H3分類・成分・相対降下は未完了。

### 三交換子alphaの重複直線と共点三直線の削減（v312）
固定as4の三重直線四表示で、中央三次切断がd軸の点イデアルの二乗に入ることを、S=B/(a)のWeyl中心と明示中央liftから証明した。二重直線b²cでは、七つの低次係数を保って中央三次liftを計算した。SのOre導分による中心はk[b²c]。重複直線上でaの係数の二次式が消える点の二チャートでは、いずれも全tails自己拡大の漸化式が行列式1でExt1が三次元となり、強いH3のSerre traceに反する。共点三直線では下位二次式が共点で零であればaを法としたOre中心とa²までの交換子で切断が点イデアル二乗に入る。同じSerre障害が固定五族のうち四族を排除する。
本文cubic_CY_three_alpha_nonsmooth節、公開再現器verify_cubic_CY_three_alpha_repeated_lines.py。三重直線四表示と二重直線の全係数・両チャートは厳密PASS。共点三直線の残る第一族、滑らか・節点・尖点・三角形・割線二次曲線・接線二次曲線、三交換子列階数三は要判定。一交換子の残る射影は中心三次を先に調べる。全成分・相対降下・全H3分類は未完成。

### 一交換子の共有Segre十一射影を全排除（v314）
対称階数5の必要排除と標識付き階数4の十六候補を固定as4から使用した。共有十一射影のうち固定空二射影以外を、元の六関係から中心三次を独立計算して判定。ad,bdは全域中心零。b²とb²+c²では中心三次はa²cとa²bの各一元。ad+b²とad+b²+c²ではt=-1/3でのみ中心三次kac²。bd+c²ではh=-1/4でのみ中心三次kb(b+3a/8)²（lambda=1/64も同じ）。いずれも整域切断なし。残るd²+b²,d²+b²+c²では、交換子比の零・非零、下位係数zの零・非零、非対角ellの四共鳴とその補集合、対角係数両符号を合わせた全40域で、商射影の分母と中心小行列式の全因子は許容単元のみ。全中心三次が零である。
本文cubic_CY_one_segre_shared節。公開verify_cubic_CY_one_segre_shared.pyとverify_cubic_CY_one_segre_shared_squares.py、対応JSON。全一交換子の未判定非skewは非共有Segreのa²+cdとab+cd。次に固定S4_12の24族・一孤立類を、全例外因子まで元関係の共通計算で判定する。固定as4の全排除の独立再実装や全統合replayは未実行。全H3分類・成分・相対降下は未完成。

### 一交換子の非共有平方・積追加の削減とZ切断の完全判定（v315）
横断外側七表示、等方外側八表示、非等方外側四族、上行交差Cθを判定。公開verify_cubic_CY_one_segre_square_split.pyは19計算とBn2の四例外直線の全既約因子を元の六関係から再検算。C(s,z≠0),L(s,h)はc,dの逆作用を同時対角化し、固有値q1,q2の相異性、1でないこと、積が1でないことから全中心三次を可換二元に限定。唯一残るZのs²=−1/12ではqが原始三乗根、中心三次はP(a,b)+Cc³+Dd³。二つの純三乗係数のどちらかが零、またはdeg P(1,z)≤1なら固定点の奇数Ext障害。
Zでの正確な条件はCD≠0、deg P(1,z)=m∈{2,3}、判別式Δ=P(1,z)^2−4CDν³が平方自由。ねじった量子Weyl表示でg=Cx²+P(1,z)x+Dν³の付値剰余曲線は種数m−1、xの二無限遠位数は±mなので立方でない（m=3では次数1写像の矛盾）。巡回ノルムの付値から斜体。c,dチャートの自由巡回軌道で完備環は冠積、Δ重根ならその一つの単純の射影次元無限。a≠0でX=Y=0は二単元辺で行列環。m=2のb軸では中心aを陰関数消去し、完備量子平面への降下濾過で左右kの長さ二解消を得る。従って全H3公理を満たす。例P=b³,C=D=1。包絡の全幾何矢を元の標識と関係から決定し、C=D=1規格化のAff₁×μ₆作用、一般慣性μ₃、次元2。二原始三乗根の包絡はc,d交換で同型。本文cubic_CY_one_segre_square_split節。これは全成分性や相対降下の主張を含まない。
平方・積追加の残りは等方外側b5と下行交差L^±_{w,e}, Z_{s,h}, M_{s,w,z}。b5は一般で中心零、例外h²+1/16,h²+1/48および三曲線での厳密再計算を終える。下行片成分の両符号で一般rank20の観察はあるが、全例外は未判定。二積追加ab+cd、三交換子alpha残余と列階数三、全成分・相対降下も未完成。

### 平方・積追加のb5と下行交差の二領域（v316）
等方外側b5は順序語基底で二元三次四列を零にする行に制限し、非二元の16列のminorは −17179869184 s⁴(48s²+1)²/((4s−1)¹⁴(4s+1)⁹)。残る48s²+1=0で全θの定数minorを厳密再計算し、可換二元三次しか残らない。下行片成分Lの二符号は反対代数。片成分と両下行・cd零Zの各五例外曲線を元六関係から有理化した。数体の全残点とZの別点(s,h)=(3/8,−48/5)を含め中心rank20。公開verify_cubic_CY_one_segre_square_split_lower.pyとJSON、本文cubic_CY_one_segre_square_split節。
平方・積追加で未判定は三変数M(s,w,z)のみ。次の具体的作業は元の必要LO3–LO5から係数許容域での中心小行列式を求め、追加既約因子だけ再計算すること。Rains系の既分類、固定Z(s)の全判定は繰り返さない。非共有二積追加、三交換子の残余、全成分・相対降下は未完成。

### 三交換子alphaのgamma=0全切断と幾何矢（v317）
固定必要被覆でgamma=0を許すのは滑らかな先頭三次と三角形・節点三次・二次曲線と割線の四型。後者三型はaを法として三平方中心のClifford環。中心三次の交代積のa²までの持ち上げに対して、元関係の次数四挿入を固定QQ射影で次数三商へ送る全行列は階数6。核の三下位係数への射影が零でQ=0となる。公開verify_cubic_CY_three_alpha_symmetric_first_order.py、三型を厳密再生。残る切断はω+a(Ab²+B₀c²+Cd²)+Da³。三角形ではAB₀C、節点ではC、割線ではAB₀の非零が固定点Serreから必要。
これらの軸条件で無限遠は全て有限大域次元。中央平方根を付加し、反転される単元によるMorita同値を使う。階数2ではAzumaya、指定軸の階数1ではSchur補の二平方とaが独立な非退化Hessianを与え、既存通常二重点の局所証明を適用。境界行列式uvw、uvw−9u³−9v³、w(uv−9w²)と軸の局所整域性から中心は既約。a=0の指定位数1境界の剰余四元数(u₁,u₂)が非分裂なので一般中心でも斜体、CMから整域。H3はアフィン中心T=detK+(Au+B₀v+Cw+D)^2の全特異点が階数1かつHessian非退化であることと同値。矢はF(LX)=ell F(X)とV'=r²V(LX)/ell、切断二次係数の行列式規格化で全判定し、共通スカラーで割る。
滑らかなFはHesse標準形へ移し、Fermat先頭は平方関係、h³=−1は(b+c+d)²で排除。残るh∈Hは既存betaの中心・局所全判定と全幾何矢に入る。従ってalphaのgamma=0部を完結。相対降下・大域成分の主張は含まない。具体的には次にgamma非零alphaの各先頭型と列階数三、一交換子の残るMと二積追加を扱う。Mの元三変数の二・三次商は10,20を得たが四次射影の式増大が残る。一般点の中心零や全除外は未主張。

### 三交換子alphaの量子三角形：全中心三次と三定数項の忠実模型（v318）
gamma非零・三角先頭のq≠0,±1、六下位係数A_i,B_iで中央Ωを決定。原始三乗根ではX=x³+q²A_yA_z t²x cyclicも中央。全低次数中心は随伴量子多項式の指数比較で尽くされる。各軸でA_iと純三乗切断係数が同時零なら自己Ext1三次元/shift行列式1で排除。非三乗根では全A_i非零となりA_i=1へ対角規格化、候補はΩ+Dt³。原始三乗根の全許容性は既分類部分以外に残る。
規格化ペンシルでは差分作用素の指数0係数y₀,z₀とb(u)を三定数項付きで明示。全三関係、Ω=−D、反転・GWA定義元を厳密検算。最高shift指数の独立性で全B_i,Dの整域とGK rank-one。q³≠1の全幾何矢はS₄で、偶置換と二符号、奇置換は(q,B_x,B_y,B_z,D)↦(q⁻¹,−qB_y,−qB_x,−qB_z,−q²D)。
非捩れではu²∈q^Zを除くOre局所化は反転GWAの固定環。定義元a(u)はξ=u/ρ+ρ/uの四次式/(ξ²−4)。残る零点が単純であることがこの開集合の正確な有限大域次元条件であり、許容域の重根は既にH3を除外する。閉部分に沿う障害までは判定していない。公開verify_cubic_CY_three_alpha_triangle_center.pyとverify_cubic_CY_three_alpha_triangle_difference.py、本文cubic_CY_three_alpha_quantum_triangle節。次に非捩れ閉軌道・射影端点と、有限位数全定数項で局所証明を延長する。一交換子Mと二積追加、三交換子の残余、相対降下・大域成分は未完成。

### 節点と割線における全中央三次と割線の原始三乗根排除（v319）
gamma非零の節点・割線の元三関係を量子三角形へ二純平方P_xx²,P_yy²を加えた形で扱う。割線はP_x≠0,P_y=0。一般Casimirにq³−1を掛けて純三乗、txyおよび三つのt²一次補正を加えたJは全係数で中央。t=0の商をz個数濾過すると、q³≠1は最高xyzのみ。q³=1では[z³,y]のz²x²、[xyz,y]のx³yが他の項で消去不能で、中央三次はP_xx³+P_yy³だけ。この像をJが持ち上げるので全中心三次はkJ+kt³。z軸のA_z=0と割線y軸のA_y=0は点の全tails Ext1三次元とshift行列式1で排除。割線のq³=1ではJがx,tの可換二元三次となるため全切断を排除。
残る割線はA_y,A_zを1へ規格化し、量子三角形の差分係数の基本項b₀を(A_x−qP_x ξ/(q³−1))b₀へ置換。q²≠1の全残るqで忠実、整域とGK rank-one。非捩れの同じOre開集合のgldim有限性も、定義元の分子五次式の許容零点の単純性で必要十分。公開二検証器は両型の全中央恒等式、割線の三関係・切断・反転・定義元を厳密PASS。本文cubic_CY_three_alpha_quantum_triangle節。節点の切断整域性・許容性、割線の残り全局所、量子三角形閉軌道、非共有SegreのMと二積追加、外積列階数三と他のalpha、全成分・相対降下は未完成。

### 全有限位数量子三角形の体積ペンシルとMの境界（v320）
三定数項付きq有限位数Nの量子三角形の射影境界を全判定。Chebyshev中心のN乗根を中央付加して次数零を取る。自身が単元となる活動変数が指標冪等元を移すので固定環と半直積はMorita同値。辺はtを法として1次元 regularの巡回交差積、t正則より左単純pd≤2。頂点は重み(0,1,1,2)の先頭がx^N=1の量子Heisenbergとその正則三次商、得る随伴環は量子平面の巡回半直積。中央イデアル濾過との共終性と完備解消の持上げで局所有限大域次元。従ってH3とアフィンUのgldim≤2が同値。
Uが三Chebyshev中心上有限なので、全単純加群間のExt³消滅は完備中心ファイバーの極小解消から正確な判定。次元上界N³、U^e上有限自由解消を第四項まで可換中心多項式環上syzygyで構成。生成元行列代入とBurnsideにより単純性およびExt³非零条件は有限多項式/階数条件。実装は未実施。非三乗根の全有限位数量子三角形では許容性と既出幾何矢まで決定。非捩れの閉軌道、原始三乗根の体積以外の全切断は残る。
平方・積追加のM(s,w,z)のW-=0で新しい生成元順(b,a,c,d)から例外三曲線が残り、各zを解くと全域中心rank20。W+は固定as4の反対代数対応。M=0では順(a,c,b,d)で三線型と一二次曲線。二次の判別式はガウス有理数体の平方、両グラフの元商を再計算し全域rank20（別の消去で残ったs=1/2−i/4も再計算）。公開lower検証器・JSON PASS。Mの三因子非零部分、非共有二積追加、三交換子の残り、成分と降下は未完成。
