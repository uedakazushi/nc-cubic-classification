# 内在的非可換del Pezzo曲面と三次三様体のモジュライ

2026-11-15 / project-v16 / recognition-v6 / hearts-v1。GitHub mainを現行ソースの正本とする。最初に[研究方針](00_research_plan.md)を読む。

## 14641分類：固定skew ambientの正規三次直線

量子多項式ambient上の全正規三次直線の被約locusを、交換指標が一致する単項式blockの射影空間として分類した。[証明](papers/sections/cubic_skew_normal_incidence.tex)／[研究ノート](research/cubic_14641_classification.md)／[検証範囲](research/cubic_skew_normal_validation.json)。一般fiberは単項式20点。量子Fermatの固定ambientには中心P5以外にも非中心成分が存在する。これらの商がintrinsic曲面条件を満たすか、全線型自己同型による商、minor schemeの非被約構造、全ambientの被覆は未解決。厳密計算は実行済み、今回の組版は日本語TeX依存不足で停止した。

## 現在の重点：heart比較、まずcubic surface

一般の非可換del Pezzoに対する **Rains heart・VdB heart・AS heart・anticanonical heart** の四構成を比較する。dP1に限定せず、最初に次数3のcubic surfaceを扱う。heartの存在、faithfulなrealization、導来同値、t-exactness、構造対象・反Serre・境界・markingの保存と族の降下を区別する。

[研究ノートと具体的着手](research/heart_comparison.md) ／ [証明付き原稿](papers/nc_del_pezzo_hearts.tex) ／ [共通枠組み](research/common_del_pezzo_framework.md) ／ [今回の検証範囲](research/heart_comparison_validation.json)

開始結果は、VdBの振幅1の比較同値を **T=ker R¹δ_*、U=ker δ_* による一回のHRS tilt** として記述したこと。heart一致はU=0と同値で、Uの非零対象も導来的には消えずshiftとして残る。AOU Theorem 9.4はqgr FとAS qgrの導来比較であり、raw blow-upと反標準heartの一致定理ではない。実際のmutation対象E0と構造対象πFの同定も別に追う。

Cubic のcornerについて、四交比における九つの小行列式に加え、qと成分逆数qの二つの行列式の非零性も必要と証明した。十一条件の十分性は標数0で未解決。詳細は[corner原稿](papers/cubic_heart_corner.tex)と[ノート](research/cubic_corner.md)。次は最後のcubic段階のker δ_6*の実在対象による記述と、AS–反標準比較のt-exactness判定。全四heartの一致や、共鳴壁ごとの非自明なtiltはまだ証明していない。数値的amplenessの稠密な失敗からAZ失敗や導来特異化を結論しない。

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
