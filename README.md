# 内在的非可換del Pezzo曲面と三次三様体のモジュライ

classification-v12 では、積分した族の全次数平坦性・noetherian quadratic Koszul CY AS4 認識を、明示的な開集合 V={h∈H, (1-gamma²)≠0, Delta≠0} 上で証明した。入力は Iyudu–Shkarin Theorem1.1/Corollary6.1、EG形式変形定理、および64個の三次持上げ恒等式・256個の四次巡回恒等式・単元小行列式 -p^6 を確認した LBS 中心拡大定理である。中心三次の関係類の非消滅も巡回商の二係数で全パラメータについて確認した。gamma≠0 では低次数中心が0,0,1、滑らかな楕円THCR境界となり、全中心値の H3 判定は正確に一つの affine 中心切断の有限大域次元へ帰着する。定義体上超越的な全 D は H3。位数4の枝 gamma^4=1+h^3 では固定包絡の悪い D は有限であり、h=1,gamma=2^(1/4),A=1,B=C=0,beta=(-1,0,0),D=pi は明示的な非Clifford H3 対象となる。悪い値の全一覧・全内在的群oid・H3相対開性・降下・全包絡被覆は未解決。

classification-v11 では、Etingof–Ginzburg の付録と著者サイトにある Rains の E6 中心元を規約変換し、全パラメータで三交換子の関係恒等式を独立検証した。`alpha=-4*gamma*(A,B,C)` と置き、正規化した中心元に定数補正を加えると、全 Clifford 切断が実際の有理式による中心表示へ積分する。gamma=0 での全係数・関係証明書の分母はよい h の全底上で正則であり、全次数の「中心性」の障害は解決した。これは包絡族の全次数平坦性、AS4 認識、切断後の H3 条件や新成分を証明したという意味ではない。次はこの積分した具体的表示でそれらを検証する。

classification-v10 では、この族から外れる指定四方向の一次中心 incidence も全係数で判定した。双対数上で最高次を `(1+epsilon*gamma)yz+(1-epsilon*gamma)zy` に変え、対角項を `epsilon*alpha_x*tx`（巡回）だけ動かすと、三次中心切断の持ち上げは正確に `alpha=-4*gamma*(A,B,C)` のとき存在する。持ち上げを明示し、全ての h,beta,A,B,C,D に通用する次数4の階数86、三次交換子階数15、単元障害行列式 `-9/(4*(1+h^3)^2)` を検算した。これは指定方向の一次 incidence であり、積分可能性・全変形空間・新しい H3 成分を主張しない。 また、この明示的持ち上げの二次障害も全係数で消え、対角係数の二次補正 kappa と中心切断 G2 を計算した（epsilon^3=0）。中心性の全次数積分は v11 で解決し、H3 族への実現は未解決である。

2026-11-15 / project-v16 / recognition-v6 / hearts-v1。GitHub mainを現行ソースの正本とする。最初に[研究方針](00_research_plan.md)を読む。

**ユーザー指定の進め方：完全分類までなるべく止まらずに研究を続ける。** 部分成果の保存後も次の未解決課題へ進み、必要な確認と実際の制約を除いて自律的に作業する。未証明の被覆・相対降下を完成扱いしない。具体的な継続指示と達成基準は [AGENTS.md](AGENTS.md) と [分類計画](research/cubic_14641_codex_plan.md) に記す。

## 14641分類：全skew包絡部分の幾何学的対象

**全H3ではμ_R=1、Gv=μ_B^{-1}(v)G。固定ambientの候補は単一の140×20線型核に絞られる。** 包絡が量子多項式環である部分は、全六次元skew torusから31パラメータ・五型へ絞り、各型の全admissible係数・内在的rank・幾何学的同型群oidまで分類した。可換、CY符号、非CY符号、3乗根中心一次、3乗根二重指標の五型で、一般同型類の次元は4,1,2,1,0。既存27点の軌道長6の商はgeneric代数M3(K)でrank-one条件に反し除外される。

[証明付き原稿](papers/weak_cubic_axioms.tex)／[研究ノート](research/cubic_14641_classification.md)／[検証範囲](research/cubic_classification_validation.json)。厳密検算とLuaLaTeX全文組版を実施。**全AS4包絡を覆うH3の完全分類・相対stackの降下・成分性は未完成。** Pymの標準CY chartではL112/R22/S23の一般点とE3の非零変形を中心三次の消滅で除外した。as4の半単純化を使うと、量子基底の全非自明unipotent持上げも除外され、この部分全体は同じ五型で尽くされる。可換三変数の非零微分Ore拡大は、点対象の自己Extが1,3,4,4,…となるため、特殊値も全て除外した。CY半単純化の交換子次元4以上の非可換層と三交換子beta層も全持上げを除外した。輸入元の固定SHA・仮定・原検算は[輸入記録](research/as4_imports.json)に明記。次はR13の全admissible切断、L112/R22/E3の特殊locus、残る低交換子CY・非スカラー共鳴層と相対降下を扱う。並行heart/corner研究は維持する。

良い楕円境界を持つ固定CY中心拡大では、全切断の整域性と内在的rank条件を証明し、H3条件をアフィン中心商の有限大域次元へ正確に帰着した。さらに**低次中心Z(S)1=Z(S)2=0,Z(S)3=kgを仮定した複素数体上の分裂中心拡大 B=S[t] は全切断を判定**：g+λt³はλ≠0で一つのH3同型軌道、λ=0とt³は除外。慣性はμ3によるPAut(S)の中心拡大。証明は[全切断の認識](papers/sections/cubic_r13_cut_reduction.tex)。有限位数translationの楕円境界を持つ固定包絡では、非admissible値が有限個であることも証明した。一般の非分裂中心値の明示と全境界・相対降下は未完成。

**位数二Clifford–Sklyaninの明示的Hesse分裂包絡族についても全切断を分類した。** 中心三次の五基底から全切断を復元し、H3条件をアフィン中心曲面の滑らかさへ帰着。h=1の固定包絡では四次式Ψを明示し、三次元の位数54有限商を得た。一係数方向の悪い値は0,−16A³/27,8A³/49。hも動かす全指定族は**四次元・位数648の有限商**で、全矢と慣性の判定を与える。証明は[Clifford全切断](papers/sections/cubic_clifford_full_cuts.tex)。全AS4包絡の被覆や成分性とは区別する。

非分裂の位数二Clifford中心拡大にも進み、**H3では二次ポテンシャルf2を平行移動で全て除ける**ことを証明した。標準形の三つの係数αに対する障害行列式は−27h/(8(1+h³)³)で全対象範囲で非零。定数関係項β族の全切断も下記の局所判定で解決した。

**非分裂β族も全切断・全幾何学的矢まで分類した。** H3条件は、中心曲面の特異点がClifford rank1点の通常二重点だけとなること。そこでは完備化環が二変数形式冪級数環のZ2交差積となり、中心の特異性を許容する。h=1,β=(-1,0,0),G=g_βは四node中心を持つ明示例。全指定対称ポテンシャル中心拡大部分は**一般次元7の明示的群商**で、一般慣性は自明、pure volume部分ではμ2。全作用式とDの混合補正を[全β分類の証明](papers/sections/cubic_clifford_beta_classification.tex)に記す。全AS4被覆・成分性・相対降下はなお未完成。

## 現在の重点：heart比較、まずcubic surface

**最大共鳴の既約根sheaf・zigzag形式性**：全根が数値的に共鳴する滑らかなRains chartでも、境界非交叉の既約root sheafの根類はr個の単純根だけ（q非torsionで各一意）。T=⊕Miのgraded ExtはADE Dynkin zigzagで、Liu–Wang (J Algebra 677, 2025) Thm1.1のintrinsic A∞ formalityから、**固定Rains dg圏のframed形式変形**は各辺の積方程式x_ij x_ji=0だけで決まる。cubic E6では32個の5次元formal分枝（gauge商前）。曲面自体の相対変形、anticanonical heartの全体、混合根のA加群の行列やδは別問題。[数学的証明](papers/sections/resonance_zigzag_unique.tex)／[整数検算](computations/verify_resonance_zigzag.py)。


**全次数1–6の最大根共鳴定理**：固定した滑らかな楕円三次E、非torsion qと、r=9−d個の相異なる正整数倍p_i=N_iqからgenuine del Pezzoを作ると、次数d=6,5,4,3,2,1の根系A₂+A₁(8根),A₄(20),D₅(40),E₆(72),E₇(126),E₈(240)の全ての根が同時に非零指数で共鳴する。各E^rでこのような点はZariski dense。根指数をr整数とE[3]の9選択から完全に記述。[全次数の証明](papers/sections/resonance_maximal_all_degrees.tex)。ただし全根sheafの同時実在や全非可換モジュライの既約成分での密度は主張しない。

**最大E6根共鳴の新定理**：smooth plane cubic上で非torsion qを固定し、六点p_i=N_iq（相異なる正整数N_i）を取るとgenuine smooth cubicを保ちつつE6の72根が全て非零指数で数値的に共鳴する。これらの点は六点配置空間でZariski dense。共鳴チャートを六単純根に対する整数m0,...,m5と3-torsionの9通りで完全に記述。N=(1,3,2,5,7,11)では同じRains heartにm=2とm=-1の隣接する既約根sheafが存在し、Ext¹は1次元。二段直和混合拡大はEuler 0でも自然な反標準導来切断で消失しない。全q導来同値が正しければ対応する2次元アフィン加群は1次元加群を商に持つ必要がある。[定理・証明](papers/sections/resonance_maximal_a2.tex)／[再開ノート](research/resonance_hearts.md)。


**RainsのZariski denseな共鳴への符号別完全判定**：既約根sheaf Mが境界に制限して零となるとき、m=chi(e,M)の正負でdim Hom(e,tau^n M)=max(m,0)、dim Ext¹=max(-m,0)、Ext²=0。正指数はanticanonical heartでm次元の境界外表現が次数0、負指数は(-m)次元表現が[-1]、零指数なら自然導来切断はMを消す。正負各指数の共鳴がそれぞれZariski dense。負指数ではRains heartのAZ amplenessが実際に失敗。すべての根sheafは2-spherical。既約性からの誤った全射性推論を修正し、Rainsの反変双対で正指数を証明した。反標準環のHilbert関数は一定。全パラメータの導来同値・qgr特異化は主張しない。**[証明原稿](papers/nc_del_pezzo_resonance_hearts.tex)**／[研究ノート](research/resonance_hearts.md)。さらに非既約で境界と交わらないsheafについて導来切断の振幅[0,1]と6項A加群完全列を証明。混合正負共鳴の拡大が定めるδのrankによりanticanonical側のcohomologyが決まり、根系の交叉は同時共鳴に明示的な禁止条件を与える。[拡大・根交叉の証明](papers/sections/resonance_extension_cancellation.tex)。


一般の非可換del Pezzoに対する **Rains heart・VdB heart・AS heart・anticanonical heart** の四構成を比較する。dP1に限定せず、最初に次数3のcubic surfaceを扱う。heartの存在、faithfulなrealization、導来同値、t-exactness、構造対象・反Serre・境界・markingの保存と族の降下を区別する。

[研究ノートと具体的着手](research/heart_comparison.md) ／ [証明付き原稿](papers/nc_del_pezzo_hearts.tex) ／ [共通枠組み](research/common_del_pezzo_framework.md) ／ [今回の検証範囲](research/heart_comparison_validation.json)

開始結果は、VdBの振幅1の比較同値を **T=ker R¹δ_*、U=ker δ_* による一回のHRS tilt** として記述したこと。heart一致はU=0と同値で、Uの非零対象も導来的には消えずshiftとして残る。AOU Theorem 9.4はqgr FとAS qgrの導来比較であり、raw blow-upと反標準heartの一致定理ではない。実際のmutation対象E0と構造対象πFの同定も別に追う。

Cubic のcornerについて、四交比における九つの小行列式に加え、qと成分逆数qの二つの行列式の非零性も必要と証明した。十一条件の十分性も六点配置への明示的復元とSerre消滅から証明した。四交比トーラスにおける有限corner locusは標識付き可換cubicの一般位置六点配置空間に同型。さらに11条件と一様なC7=0は同値で、一般位置ではC6に8次元以上残るため、道長7が最良の一様消滅次数。関係行列M7の最大minorイデアルの根基も11 divisorの積で記述した。証明は[一様次数の定理](papers/sections/cubic_corner_uniform_cutoff.tex)。さらに、一般位置全域のHilbert関数が **8+21t+33t²+38t³+33t⁴+21t⁵+8t⁶**、総次元 **162** で一定であることを証明し、11条件開集合上に基底変更と可換する階数162の有限平坦代数族を構成した。[証明](papers/sections/cubic_corner_hilbert_series.tex)。さらに11壁は10個の共線性根と1個のconic根で、古典的blow-up側では非零2-spherical i_*O_E(-1)が反標準orbitに不可視となり、反標準収縮後の特異三次との有界導来圏は非同値。[完全証明と一壁の節点三次](papers/sections/cubic_corner_root_walls.tex)。ただし非可換AS/Rains/VdB heartの壁での存在は未解決。詳細は[corner原稿](papers/cubic_heart_corner.tex)と[ノート](research/cubic_corner.md)。次は最後のcubic段階のker δ_6*の実在対象による記述と、AS–反標準比較のt-exactness判定。全四heartの一致や、共鳴壁ごとの非自明なtiltはまだ証明していない。数値的amplenessの稠密な失敗からAZ失敗や導来特異化を結論しない。

## 各研究の現行原稿

| 対象 | 原稿とノート |
|---|---|
| 全次数のheart比較、cubicから開始 | [heart原稿](papers/nc_del_pezzo_hearts.tex)、[ノート](research/heart_comparison.md) |
| 次数3の公理・境界認識・Fermat別分枝 | [認識原稿](papers/weak_cubic_axioms.tex)、[ノート](research/weak_cubic_axioms.md) |
| 次数3のambientと成分 | [surface原稿](papers/cubic_surface_ambient_moduli.tex)、[比較ノート](research/cubic_surface_comparison.md)、[R13](research/r13_generic_moduli.md) |
| 次数1のrank・weighted sextic・候補族・avatar | [dP1原稿](papers/nc_del_pezzo_degree1_moduli.tex)、[方針](research/dp1_research_plan.md)、[ノート](research/dp1_research_notes.md) |
| 次数1の反標準モデルと共鳴 | [専門稿](papers/dp1_anticanonical_models.tex)、[再現](research/dp1_reproduction.md)、[検証](research/dp1_validation.md) |
| 三次三様体と非可換P4 | [threefold原稿](papers/nc_cubic_threefold_moduli.tex)、[ノート](notes/research_notes.md)、[検証](validation.json) |

既存の全文・証明・計算資産を保持する。今回のheart研究は、dP1の強い導来比較定理を入力として使わず、その独立再監査を実施したとも主張しない。

## 保持する既存研究の要点

次数1・3の共通定義はGabriel–Krull rank-one torsion-free exceptional Oを用いる。hdim A=2はSerreのheart保存から従い、独立公理にしない。exceptionalityなしの広い条件はpre-weakとして区別する。

次数3では正則正規一次境界R/(t)=S0/(g)からAS4二次包絡と正規三次商を認識する。全weak対象への境界存在は未証明。量子Fermat例は全対象のR(1,3)帰属を否定し、固定ambientの良い中心切断の商BH54は全変形のrigidityを意味しない。R13分枝の8→7、中心fiber P1と全weak moduliの問題を区別する。Fermat ambientはPym L(1,1,1,1)とL(1,1,2)の交点に属し、R(1,3)閉包外。明示退化と27個のtorus点の検算も保持する。

次数1では内在的rank、境界の正則被覆を仮定したweighted sextic認識、10次元pointed dg候補族と補助A∞表示の成分性を保持する。全intrinsic abelian成分性、特異/非局所自由境界の比較は未完成。

三次三様体では、相対Z-algebraのfpqc stack、二次包絡射と正規三次incidence、有限窓の逆極限、周期忘却、形式成分を保持する。全体の有限型代数性は別問題。標準AS4の四頂点potentialとAS5の五頂点potential、GL/PGLの慣性、任意周期とFrobenius適合周期を区別する。可換P3の射影potential接空間90、軌道45、商45は成分次元ではない。

Rat(1,1,3)の非射影化Poisson/形式ambient成分は37次元、中心対41次元、一般PGL商は13/17次元、一般ambient忘却fiberは4次元。射影Poissonは36次元、GL商stackは12/16次元。可換cubic点では局所次元17・接空間20、ambient接写像の核10・像10であり、一般fiber4と混同しない。全大域モジュライの代数性・成分性、任意の非可換点の相対周期化/降下、smooth proper部分の相対開性などは未完成。

17係数slice、分離型余次元15、可換cubic忘却核7、混合中心、相対Picard、偶数Veronese、固定ambientの4係数族を含む詳細は既存論文と各sectionに保持する。今回それらを再検証したとは報告しない。

## 手動再現

現在のheart課題：

    python3 computations/verify_cubic_heart_numerics.py
    latexmk papers/nc_del_pezzo_hearts.tex

次数3認識：

    python3 computations/verify_boundary_fermat.py
    python3 computations/verify_quantum_fermat.py
    python3 computations/verify_fermat_pym_components.py
    latexmk papers/weak_cubic_axioms.tex

次数1：

    latexmk papers/nc_del_pezzo_degree1_moduli.tex
    latexmk papers/dp1_anticanonical_models.tex

既存threefold計算：

    python3 scripts/verify.py
    python3 computations/verify_p3_potentials.py
    python3 computations/verify_two_factor_stabilizer.py
    python3 computations/verify_rat113_tangent.py
    python3 computations/independent/verify_generic17_slice.py
    python3 computations/independent/verify_generic17_center.py
    python3 computations/verify_split_codimension.py
    python3 computations/verify_central_pair_centers.py
    python3 computations/verify_central_pair_orbits.py
    python3 computations/verify_central_symmetry.py --output build/central_symmetry.json
    latexmk papers/nc_cubic_threefold_moduli.tex

Python3・必要に応じSymPy、日本語LuaLaTeX・LuaTeX-ja・latexmkを使う。新heart計算はPython標準ライブラリのみ。既存二因子stabilizerコードはverify_rat113_tangent.pyも必要。PDF/SyncTeX/ログは`.latexmkrc`に従いbuild/へ出力しGit追跡しない。GitHub Actionsは使用しない。実行した検証と未実行の既存検証を区別する。

## 14641型intrinsic cubicの現行分類課題（2026-11-15）

研究方針は `00_research_plan.md`、詳細は `research/cubic_14641_classification.md`、証明は `papers/weak_cubic_axioms.tex` の `sec:14641-classification`。noetherian 14641二次包絡から一本の正則正規三次関係を導く定理、AS型の真部分性、35×8の正規三次incidence、27点の有限分類を含む。検算は `python3 computations/verify_cubic_skew_strata.py`。PDF・ZIPはGit追跡しない。完全分類と全intrinsic stackの代数性は未解決。
