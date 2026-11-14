# 三次曲面とP3：研究ノート

2026-11-14 / surface-v1。研究方針は先に `00_research_plan.md` を読む。証明は `papers/cubic_surface_ambient_moduli.tex`。

## 現在有効な結論

三次曲面はn=2。Poisson側はスカラーを残して23次元incidence→22次元R(1,3)錐、PGL4の一般有理商は8→7。一般fiberはF+c h^3。hの零平面と共通楕円境界が保持され、F/h^3の値だけが忘れられる。射影化されたPoisson構造の21次元と錐の22次元を混同しない。

量子側ではPBW/低次数中心/三次中心持上げを仮定してZ(B)_3=k Omega+k t^3。固定ambientへの同定を保持するcentral fiberはP1。二因子stabilizer有限なら全indexed normal fiberの形式完備化も1次元。構造対象とSerreを保つ復元にはsaturationとSerre=(-1)[2]を使う。正規商の任意の表示でこのSerre式を使えるとはしない。

可換smooth cubic surfaceではHH2=8、HH3=0。三次三様体のPluecker二次障害をsurfaceへ移さない。全例外列が存在するのでthreefoldでのHH±1によるtilting不可能性もsurfaceには該当しない。

## 一次資料と比較の穴

AOU: https://arxiv.org/abs/2404.00175 。Introduction、§5.4、Theorems1.1/9.4、Lemma9.2を確認。9頂点18矢9関係、rolled-upは27矢27三次閉路。dense torusはGm^8。Theorem9.4は所定の条件下の導来同値であり、全境界のheartや反標準環の同定ではない。

Van den Bergh: https://arxiv.org/abs/math/9809116 、Chapter12とRemark12.0.5。AS4 ambientと正規三次商の構成、反標準モデルと実際のblow-upの区別。

Pym: https://arxiv.org/abs/1403.6444 、§3.4。R(1,3)と中心一次拡大。次数付きCY変形の成分を全4周期Z代数の大域成分分類へ無条件に拡張しない。本文Table1の数値は規約を別途照合し、本稿の22は源の次元と実際の微分rank22から独立に計算した。

Le Bruyn–Smith–Van den Bergh: Central extensions of three-dimensional Artin–Schelter regular algebras, Math.Z.222(1996),171–212。著者PDF https://sites.math.washington.edu/~smith/Research/Central-extns.pdf 。本稿では一般論を仮定のない新定理として再宣言しない。

Etingof–Ginzburg: https://arxiv.org/abs/0709.3593v4 。中心商構成と§9の有限中心式が量子側の入力。低次数中心の一定rank開部分を使い、全中心一定の単一開部分を仮定しない。

## 計算の意味

コードは特性零の有理数上で実行した。M(60×24) rank22、O(60×16) rank15、J(96×60) rank38、H(60×32) rank30。JM=0、Jacobi、divergence、Casimirを厳密確認。Fの勾配イデアルが零次元なのでsmoothな射影曲面のwitnessである。

非零minorは一般階数を証明する。これだけでAS正則性、全次数の平坦性、smooth tails、大域stackの代数性、AOUの全域との同値を証明したわけではない。本文命題3.1は既約像の次元と全Poisson接空間を併用して成分の一般正則性を証明する。

## 次の計算対象

LambdaとP0からinverse Serre orbitの低次数を計算し、A1のrank4、A2のrank10、A3のrank19、Q(A)3のrank20を検査する。AOUの楕円decuple側とVdB構成で同じOが選ばれること、族でHomが底変更と両立することを最初に確認する。そこからpotential間の射を作る。単なる矢印の削除やpotentialへの代入ではなく、反標準section algebraを介する。
