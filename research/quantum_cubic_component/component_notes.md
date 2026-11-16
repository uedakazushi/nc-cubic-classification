# 成分研究ノート

2026-11-17 / triangle-component-v3。方針はこのディレクトリの `00_research_plan.md`、証明は `papers/quantum_cubic_component.tex`（rootからのパス）。
このノートは履歴ではなく、現在の入力・障害・再開のための知識を記す。

## 1. 記法と既存入力

qは原始三乗根。B_aの低次係数はa,b,c、中心三次線の係数はalpha,beta,gamma,delta,epsilon。
添字RはEtingof--Ginzburg/Rains公式の変数であり、包絡の中心一次元tとは区別する。

依存する既存原稿の固定参照は nc-cubic-moduli commit
`846c1361651790082f54b524350370ead81811d5`。
この保存済み基点には七次元族と以下の入力がある。別の旧bundleの復元は不要である。

| 入力 | ファイルとラベル | 今回の使い方 |
|---|---|---|
| 固定qso3包絡の全H3切断 | `papers/sections/cubic_quantum_triangle_full_cuts.tex`, `thm:quantum-triangle-full-H3` | 原点切片の非空性・滑らかな中心を持つ例 |
| 位数固定の相対H3開性 | `papers/sections/cubic_finite_order_relative.tex`, `thm:finite-order-relative-H3-open` | 七次元族のH3開集合 |
| 境界の局所order | 同上 `lem:finite-order-boundary-order` | HH層計算の局所Morita入力 |
| 中央境界CY認識と対称PBW | `papers/sections/cubic_central_elliptic_cy_envelope.tex`, `prop:central-sklyanin-linear-lifts-symmetric` | 正常形と一般Sklyanin持上げ |
| 楕円境界からのaffine認識 | `papers/sections/cubic_normal_elliptic_boundary.tex`, `thm:normal-elliptic-affine-recognition` | 超越的中心値のH3性 |
| 包絡・商の復元 | `papers/weak_cubic_axioms.tex` のH3認識部分 | pointed exact同値とgraded同型の比較 |

これらの入力の内容は現行論文に明記してある。全依存定理の独立再監査は未実施である。
この専用ディレクトリに既存の全AS4分類ノートや旧論文のコピーを重複させない。入力の現行ファイルは同じリポジトリに存在する。

## 2. 固定位数3の正常形で有効な式

対称PBW行列Aに対してv=(A23,A13,A12)/(1-q)を平行移動量に取る。
対角h_i=Aiiは不変、新定数はb'_i=b_i+h_i v_i+(1-q)v_jv_k。
hiが単元ならri²=hj hk、r1r2r3=h1h2h3を選んで対角を1へ正規化する。
4つの偶符号と巡回置換が残る。これに中心三次線P4を加えたものが7次元正常形。
対角係数零は未被覆の境界であり、この正規化から消してはいけない。

## 3. 全次数持上げで重要な障害の回避

中心が跳ぶ点で「一般中心元が存在する」だけでは指定切断へ特殊化できない。
まずEと移動点rhoを使って、先頭中央三次g_sを指定する。
その後、F_2Z(V_0)=kを使うと低次補正の9未知数に単元minorがある。
一般fiberでの存在と特殊fiberでの一意性を組み合わせれば、極を導入せず持ち上げられる。
これは全中央三次を一括して中心束のrank一定とみなす誤りを避ける方法である。

一般中心値DのH3性はV⊗_{F[G]}F(G)という中心局所化で証明できる。
有限PI次数を横断する全係数のH3開性と混同しない。
数値D=5に対する明示的な有理積分は中心性・平坦性まで確認しており、一般uのH3性は未判定。
Dを独立な超越変数にすれば中心局所化の議論が使える。

## 4. HH計算で保持すべき区別

一般点の中心Cと分岐Dは滑らか、D=-K_C。局所orderはk[[s,w]]⋊mu3。
非恒等sectorは法線の非自明指標のためHH cohomologyへの寄与が消える。
恒等sectorを粗空間へ押すとO_C、T_C(-logD)、O_Cとなる。
H^1(T_C(-logD))=7、H^0(O_C)=1、他の正の障害項は零。
従ってHH²=8、HH³=0。Hochschild homologyのtwisted sectorと混同しない。
Brauer捩れ付き圏を無条件に非捩れroot stackと同一視しない。
局所Moritaと層の貼合せによる証明を使い、root stackのn=2限定公式をn=3へ転用しない。

## 5. 厳密計算の意味

witness A: a=b=c=0, central coefficients(2,1,2,3,5)。
affine中心特異点idealはQ(q)上で(1)、境界Delta170、beta gamma delta6。
ポテンシャル20係数と中心元20係数に対し105×40行列rank18、核22。
12 affine座標方向+potential scalar+cut scalarのrank14を直接確認。
既知7方向とのspanはrank21、横断Phi'=x³+2y³+3z³+2xyzを加えて22。
「105式あるから余次元105」などの単純な方程式数の議論は無効。

witness B: Phi_u=(1+2u)xyz-qxzy+u(x³+8y³+27z³)-(x²+y²+z²)/2。
中央三次元の有理係数は `transverse_rains_lift_certificate.json` に収録。
正則なu0極限は2Omega+X+8Y+27Z+D。三交換子をQ(q)(u)上で厳密に零へ還元した。
有限標本からの補間・外挿ではない。

一般の121語の大きな有理行列を直接逆転すると式が膨張する。
現在の再現コードは書換え依存グラフの強連結成分に分け、最大12×12ブロックを多項式分母付きで解く。
失敗した重複実装や作業ログは同梱せず、この有効な実装だけを残す。

## 6. 文献確認と未確認点

- Etingof--Ginzburg: arXiv:0709.3593v4, Theorem3.3.2(i),(ii), Appendix9.1。
  一次本文を確認。今回のRains式は規約変換後に原関係でも独立検証した。
- Negron--Schedler: arXiv:1809.08715, Theorem1.1, AppendixA。
  固定部分のdet normalと局所から大域のspectral sequenceを確認。
- Faber--Ingalls--Okawa--Satriano: arXiv:2206.13359v2, Theorem1.5, Corollary1.7。
  smooth tame orderと捩れ付きstacky曲面の比較として使う。非捩れ同値とはしない。
- Fu--Porta--Scherotzke--Sibilla: arXiv:2509.00501v3 (2026-01-20), Proposition6.17。
  一般root stackのHH恒等sectorへの帰着と比較した。n=2限定の後半は利用しない。
- Rains: arXiv:2107.13540v2 (2022-02-17), Props2.2,2.3, Example2.1, §6末尾。
  次数3の全パラメータ被覆は論文の証明済み結論として使わない。
- De Deken--Lowen: J. Noncommut. Geom. 5 (2011), 477–505, DOI 10.4171/JNCG/83。
  Theorem4.5とProposition4.6、pp.495–496をEMSの一次本文で確認。Z-generating列のExt1,2消滅を照合。
  第5節のgeometric helix/有限例外列の定理は使用しない。
- Stacks Project Tag0BDK: perfect複体のfiberが一つの次数の自由加群である条件。
  Artin局所版は最小自由複体を使い本文で直接証明。
- Lowen--Van den Bergh: arXiv:math/0405227、Lowen: arXiv:0707.2602。
  abelian deformationのHH障害理論、exceptional object持上げの根拠。

PDF一次資料の抽出本文を使用した。web screenshot取得はキャッシュエラーで成功していない。
今回の新規PDFはローカルでレンダリングして点検した。
新規性の網羅的な調査、全H3原稿の独立査読は未了。

## 7. 大域成分の完全決定に必要なもの

現在の成分定理 `thm:conditional-component` は相対モジュライ比較仮定付きである。
条件(2)の単射性は次節の適合したenhanced Abel変形の範囲で解決したが、他の条件は未完成。
形式圏変形の正則8次元性だけから、全H3の代数性・全境界の分類は出ない。
E6型のweighted projective/Weyl商が候補だが、境界のH3必要十分条件と全群oidを証明するまで同一視しない。
次の作業は研究方針§IVを読む。

## 8. Artin再構成の現在有効な要点

証明は `papers/sections/quantum_cubic_artin_reconstruction.tex`、主論文第8節へ組込む。
E_i=pi R(i)についてj>=iならExt^{>0}(E_i,E_j)=0。AS-CM性でH1が消え、
H2はR_{i-j-1}の双対なので消える。全E_iはexceptionalでAZ ampleなZ列となる。
De Deken--Lowen Theorem4.5をGrothendieck圏Ind(qgr R)へ適用して、
有向Z代数のflat線型変形とflat Abel変形の同値を得る。

適合したenhancementの意味：持ち上げたE_iがperfect、derived Homが底上perfectで底変更に適合する。
特殊fiberで恒等なMorita同値があれば、各exceptional E_iの持上げはExt1=Ext2=0により同型類として一意。
各iの同型を選んで正方向Homと合成を同定し、Z代数再構成によりpointed exact同値を得る。
これは全Artin底での同型類の単射性であり、与えたMorita同値自体のt-exact性や群oidの充満忠実性ではない。
無限列を有限完全例外列に置き換えない。一般dg変形のheart存在も別問題である。

smooth proper dg変形と底変更に適合する相対Serre作用の下で、
P_n=RHom(E_A,tau_A^n E_A)はperfectかつ特殊fiberがR_n[0]。
最小自由複体の議論によりP_nは有限自由加群の次数0集中となる。
乗法の余核を次数ごとにNakayamaで消して一次生成を得る。
T(A^4)からR_Aへの核I_nは有限自由で特殊fiberと可換。
I2の六基底とI3の三次生成元を持ち上げ、各次数のI_n/J_nへNakayamaを適用すると全関係を生成する。
有限m-adic filtrationにより左右noetherian性も従う。

残る障害：この証明は二次包絡B_Aのflat性・AS4性を含まない。
三次関係の両側イデアル生成と正則正規な左右主イデアル生成を区別する。
主張の状態を強めるには三次syzygyと高次Koszul複体の持上げを実証する必要がある。
