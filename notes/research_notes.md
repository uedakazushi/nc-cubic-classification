# 研究ノート：具体例・計算上の注意・比較への入口

2026-11-19 / research-notes-v9。

再開時は `00_research_plan.md` を最初に読む。全H3分類の現在の主張と依存関係は
`research/cubic_14641_classification.md`、証明は `papers/weak_cubic_axioms.tex` とその読込節、
実際の検証状態は `research/cubic_classification_validation.json` を参照する。
本書は具体的な計算で再利用する情報を保持する。広いweak公理との比較は
`research/weak_cubic_axioms.md` に分ける。

## 1. Character障害と位数4の具体例

### Characterだけで分かること

`papers/sections/cubic_character_serre.tex` の `prop:character-odd-ext` は、
characterのJacobianを `J=2M` としたときの余因子恒等式による自己Ext判定である。
rank M=2では、核の射影点が楕円point curve Eにある場合に正確に自己Ext¹の次元が1となる。
rank M=1,3,0ではそれぞれ2,0,3となる。
これはcharacterの障害を尽くすが、全単純表現・高次Extの判定ではない。
対応する検算器は `computations/verify_cubic_character_serre.py`。

固定した包絡

\[
h=1,\qquad \gamma^4=2,\qquad
a=(1/(2\gamma),1/(2\gamma),0),\qquad \beta=(1,1,2)
\]

ではcharacter schemeは長さ8の完全交叉で、critical schemeは
`(x+y-2,(y-1)^2,z)`、長さ2、台 `(1,1,0)` である。
中心値のscheme imageは被約な一点

\[
D_*=\frac{2\gamma^4+10\gamma^3+21\gamma^2+19\gamma+13}
          {4(1+\gamma)^5}
\]

となる。この値は非H3である。全切断の現在の結論は
`papers/sections/cubic_order4_local_orders.tex` の `thm:order4-fixed-all-bad` にあり、
非H3値は正確に `(D-D_*)P_4(D)Q_1(D)=0` の相異なる六根である。
係数は `computations/cubic_order4_center_critical_certificate.json` にある。
character障害一個だけからこの六根を得たのではなく、中心・小次元単純表現・局所orderの判定を組み合わせる。

### 中心式の再構成で保持する事項

`computations/verify_cubic_order4_center.py` は `gamma^4=2` の係数体上で、
包絡の次数0から5の次元 `(1,4,10,20,35,56)` を逐次商で作る。
三次中心商の次数4,5の次元は31,46である。
138×31交換子行列はDに一次で、重み付き一次ansatzの核は
定数1、D、三つの四次中心元の五方向となる。最高四次三元は独立で、
交換子はDを記号のまま扱って零を確認する。

全中心の三生成元、任意底変更、中心上階数16の証明は
`papers/sections/cubic_order4_center.tex` の `thm:order4-relative-center` に置く。
先頭Hesse型三次関係は楕円座標環で計算する。
低次26係数の再構成では重み `(r,D,Z)=(1,3,4)` から事前の次数上界を証明し、
17個の厳密な48次元sliceを用いる。設計行列式は18432で、関係全体は
`computations/cubic_order4_center_relation_certificate.json` に保存されている。
補間の十分性はこの事前上界に依存し、標本一致だけを証明としない。

一般の位数4積分chartの必要十分判定は
`papers/sections/cubic_order4_general_criterion.tex` の `thm:order4-sector-admissibility` を参照する。
Du Val中心という条件だけでH3を結論せず、McKay指標の全出現を確かめる。
固定例のD_*におけるA₃中心は、この区別を必要とする具体例である。

## 2. 楕円filtered deformationの認識で循環を避ける

滑らかな次数3楕円THCRのfiltered deformationから強い14641包絡を回復する証明は
`papers/sections/cubic_filtered_elliptic_recognition.tex` の
`thm:all-filtered-elliptic-strong-envelope` にある。
手順はRees環R上のt正則性から二次係数行列Aの対称性を導き、
Braverman–GaitsgoryのPBW条件で二次包絡BのAS4性を得る順である。
AS4性を仮定して対称性を導き、同じAS4性へ戻る議論にしない。

非可換先頭環Sでは `Z(S)_1=0` から `Z(B)_1=kt` となる。
`mu_B(t)=ct` と書き、RRZ Theorem 6.3の `hdet(mu_B)=1` と式(E3.9.1)の因子cによりc=1を得る。
その後、二次関係のminorで残る平行移動を消す。
ここでRRZの一般AS Gorenstein conjectureや条件付きLemma 7.1を入力にしない。
`B→R` の核はHilbert級数と左右の主イデアルの比較で正則正規三次Gに生成される。
Gのnormalizerはtを固定し、mod tで恒等なので、同じ平行移動の判定からGは中心となる。

全filtered同型は `X→MX+v`、`det M≠0` の係数比較で得る。
三つの二次関係と一つの三次関係を比較する空間はF₃の次元19である。
tのrescalingは `F_nU=R_nt^{-n}` を変えず、graded同型からfiltered同型への核は次数スカラーである。
候補の係数はHesse境界と点、対称Aの六成分、定数三成分、Gの低次十成分で、
中心性は単一線型核、`G mod t=g` の規格化は有限個のchartで扱う。

現在、無限位数の許容性は八次対角判別式と線加群による排除、有限位数は中心と局所McKay条件へ接続される。
混合位数の開性と相対族の正確な仮定は主原稿を参照する。
一般の平坦Abel圏変形に対し、相対propernessや二次包絡の三次平坦性を無条件に仮定落ちさせない。

## 3. Potentialのj=0と点曲線のjを区別する例

`papers/sections/cubic_j0_boundary.tex` の `prop:j0-nontorsion-cut` は
`h=-1, gamma=2, A=1, B=C=0, beta=0` の例である。
中心tを持つ包絡の三関係は

\[
3yz-zy+x^2+8tx=0,\qquad 3zx-xz+y^2=0,\qquad 3xy-yx+z^2=0,
\]

で、正則中心三次は

\[
729G_0=13y^3-3yzx+13zyx+z^3-30tyz+6tzy-72t^2x.
\]

積分式の見かけの極は、`(1+h^3)Gamma_0` を先に約分してh=-1へ特殊化することで除く。
自由な切断係数 `Dt^3` は特殊化後に加える。
分母はgamma+1の冪と定数であり、この例の包絡の退化を意味しない。
全係数は `computations/cubic_j0_boundary_certificate.json`、検算器は
`computations/verify_cubic_j0_boundary.py` にある。

point schemeは `x^3+y^3+z^3+9xyz=0` で、potentialのj=0と混同しない。
translation点 `(3:-1:1)` の良い還元位数はmod 5で9、mod 13で6であり、無限位数を示す。
この具体例で最高記号が非零なことは確認されているが、この特殊化式を使うだけで全gammaの非消滅を主張しない。

全切断値の抽象的な必要十分判定は、現在の全無限位数楕円判定
`thm:cubic-CY-three-alpha-elliptic-diagonal-all-nontorsion` に従う。
この例について八次多項式の全係数を具体的に算出する課題と、一般判定定理の有無は区別する。

## 4. 分類ノート・原稿への主題別参照

下記の詳細な係数、例外被覆、証明書の説明は `research/cubic_14641_classification.md` と対応する現行原稿に保持する。

| 主題 | 原稿の入口（`papers/sections/`） |
|---|---|
| 三捩れ量子Weylの全中心・固定切断 | `cubic_quantum3_center.tex` |
| 非中央正規楕円境界、Clifford swapと量子Fermat | `cubic_normal_elliptic_boundary.tex`、`cubic_normal_order2_clifford.tex`、`cubic_normal_order3_coverage.tex` |
| 三角境界のCasimir pencil・全中心切断・共鳴incidence | `cubic_quantum_triangle_general.tex`、`cubic_quantum_triangle_full_cuts.tex`、`cubic_quantum_triangle_incidence.tex` |
| SklyaninのZhang/cocycle twistとStafford排除 | `cubic_twisted_envelope_exclusions.tex`、`cubic_stafford_exclusions.tex` |
| 低交換子・共有係数chartの必要被覆と全値排除 | 分類ノートの対応主題、`cubic_as4_reductions.tex` とそこで参照する各排除節 |
| 四shiftによる生成とNakayama規約 | 分類ノート「四shift windowと独立Nakayama監査」、`cubic_four_window.tex`、`cubic_hypersurface_frame.tex` |

一般rrefの係数から全特殊値の平坦性を推論しない。全関係消滅・自由列identity・分母の単元性を組で確認する。
文字どおりの同型、Zhang twist、cocycle twist、intrinsic pointed同値は区別する。
有限生成元や有限次元cohomologyだけで、高次A∞積または全局所大域次元を省略しない。
大きい自由単語全列挙より、次数ごとの商基底・乗法・事前次数上界を用いる。

三次三様体・非可換P⁴の独立研究は https://github.com/uedakazushi/nc-cubic-threefold-moduli を正本とする。
関連する移管済み論文の所在と研究間の境界は `00_research_plan.md` を参照する。

## 5. 検証状態

本書の整理は新たな全検算の実行を意味しない。
原稿にある証明、限定的な内部点検、実行した計算、独立査読の状態は
`research/cubic_classification_validation.json` の現行記録で区別する。
ここに古い「次の課題」や過去の実行状態を継ぎ足して現行方針としない。
