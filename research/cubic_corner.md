# Cubic：AS heartと反標準heartの一致開集合

2026-11-15 / hearts-v2 / corner-v1。最初に `00_research_plan.md` を読む。証明本文は `papers/cubic_heart_corner.tex`。従来のHRS・orbit・一般corner判定は `papers/nc_del_pezzo_hearts.tex` に保持する。

## 現在の結論

AOUの3×3 block cyclic quiverに27係数potential Wを入れ、B=Jac(Q,W)、e=e_(A0)、C=B/BeBとする。道長gradingではBは矢で生成され、関係は二次。C_N=0なら全n≥NでC_n=0。ゆえに U_N={rank M_N=dim paths_N} は最大minorの非消滅による開集合で、U=union U_N はCが有限次元であるlocusそのもの。係数空間のnoetherian性からU=U_N0となる一様なN0は存在するが、N0=7とは未証明。従ってこの有限係数chartの自然corner比較の失敗は相対閉条件であり、抽象的な導来同値の失敗locusとは別。

C有限次元からBeの右eBe有限生成性とeBの左eBe有限生成性を道の分解で導ける。B右noetherianならcorner eBeも右noetherianで、M→Meはqgr同値。逆に自然restrictionが同値ならπC=0なのでC有限。既存のcorner判定のbimodule有限性を今回の道長条件で具体的に確保した。

反標準比較にはcut grading deg(x)=deg(y)=0,deg(z)=1を使う。道長gradingをそのままAS heartと同一視しない。標準AS helixのfolding/Serre同定とprojective飽和の下でeB_cut e=⊕Hom(O,tau^n O)、O=π(eB)、tau=S^-1[2]。したがってU上のnoetherian AS領域でAS heartとこの反標準heartは自然にabel同値。全potentialのAS性・noetherian性を判定した結果ではない。

## 明示的な非空性

六点は(1:0:0),(0:1:0),(0:0:1),(1:1:1),(1:2:3),(1:4:2)。全三点は非共線、六点conic評価行列式は-12。AOU(4.1)の九線束を用い、各二段道の切断を直線・conicの積として構成する。唯一の関係を原始整数係数で正規化すると、w_abcのb行c列行列は

    W0 = [[1,1,1],[-1,-2,-2],[1,3,1]]
    W1 = [[2,1,1],[-1,2,-4],[-1,-3,1]]
    W2 = [[1,1,2],[-1,-1,-1],[1,1,1]].

A0を削除すると21矢・21二次関係。全prefix×relation×suffixの行空間を始終点ごとに構成し、FractionによるQQ消去とF_1000003消去を実行した。Cの次元列は[8,21,33,38,33,21,8,0]、総次元162。7次では6804列、21blockがすべてfull rank。従ってU7非空。有限体rankだけから低次数の正確な次元を主張せず、QQ計算で確認している。

この可換点のAS性はAOUの既知helix結果、noetherian性は反標準環上の有限加群性による。数値rankをAS性の代用にしない。計算の証明書はコードから再生成する。保存したsummary JSONに生成される全block証明書のSHA256を記す。

## HRSの追加判定

振幅[0,1]の同値F、逆振幅[-1,0]、F(e)=e'、F tau=tau' F、標的のAZ豊富性と高次Serre消滅を仮定する。tau固定の非零単純対象MはT=ker H1FまたはU=ker H0Fに属し、chi(e,M)>0 iff M∈T、chi(e,M)<0 iff M∈U。chi=0はこの仮定下で起きない。U側のRHom(e,M)は次数1のみで次元-chi。非単純MのEuler符号だけからM全体がUに属するとはしない。実在する共鳴単純対象とpointednessの照合は未完成。

## 次の課題

1. U7外でもU_N(N>7)に入る点を切り分け、有限corner条件の最小境界を調べる。U7の補集合を非一致locusと同一視しない。
2. AOU§9のmutation後E0とVdB模型のπFを対象として同定し、既知導来同値と自然corner同値の比較を行う。本結果はAS側のOから作る反標準環についての定理である。
3. VdB最後の段階のker δ_*を、実在するroot単純対象で調べる。上の符号判定を、pointednessと周期作用を確認した場合に適用する。
4. 有限位数・特異境界・他次数では生成次数、cutと周期、noetherian性を個別に検証する。

## 文献・確認範囲

AOU, arXiv:2404.00175v1, (3.19), (4.1)–(4.13), §9。§4のquiver/potential図・公式はPDF画像と本文で確認。OU, arXiv:2508.04986v1, Definitions1.1,5.2,§6、p8画像確認。VdB, arXiv:math/9809116v1, Theorems9.1.9,11.1.3の本文を照合したが今回の一部画像取得は失敗。本結果の新規性は未確認。証明の検討・厳密計算・組版を行ったが外部独立査読やproof assistantによる形式化はない。

再現: `python3 computations/verify_cubic_corner.py`、`latexmk papers/cubic_heart_corner.tex`。Python標準ライブラリのみ。既存の数学や計算は変更・削除していない。
