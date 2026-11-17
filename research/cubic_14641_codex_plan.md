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


## 多固有値領域の現行到達点（v288）
強いintrinsic H3のAS4包絡は相異なる中山固有値をちょうど三つ持たない。全Jordan型の必要還元、重複1の全22tensor atlas、非単位重複rootの独立・非零比例・零b²列を全て排除した。全H3分類の完成ではない。全CY・単一固有値単冪、全成分・境界、相対降下は未完成。

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
次は単一固有値1のJordan(3,1),(2,2),(2,1,1)と全CY。最大Jordan4の各branchの正常行列をこれ以上調べる必要はない。private A/B normal計算ではA核0、B u1/3,1/7,1/15に核1（後二つ全suffixx因子）だったが、上の全係数vertex障害が全てを含むため未公表の巨大数値を重ねない。principal零枝C0/C1も同じvertex証明で排除済み。
次の着手はN型(3,1)のCYtop核18方向を元66巡回方向から構成し、chainのindex weightで最高topと純二元二次列を調べる。最大Jordan4でのweighted PBWを他のJordan型へ無条件に流用しない。全CY/単一固有値残Jordan、成分・群oid・相対降下は未完成。
