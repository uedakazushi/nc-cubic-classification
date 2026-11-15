# 非可換del Pezzo曲面の共通内在的枠組み（次数1と3）

2026-11-15 / integration-v2。これは次数1と次数3の既存研究を接続するための方針文書であり、全次数についての分類定理を主張するものではない。

## 共有する候補公理

基礎体k上のExt有限・noetherianなhomological dimension 2のabel圏Aと、Serre関手S、反標準作用tau=S^{-1}[2]を取る。tauはheartを両方向で保つexact autoequivalence、Oはrank-one torsion-free exceptional object、(O,tau)はArtin–Zhang ampleとする。次数dを全n≥0の

    dim_k Hom_A(O,tau^n O)=1+(d/2)n(n+1)

で指定する。Oを指定するのがweak marking。quiver、blowdown基底、例外列は定義に含めない。rankをGabriel–Krull長さで定義する場合の必要仮定・証明は次数1主論文を参照する。数値K群のrankと同一視するときには別途比較する。

反標準環 R=⊕_{n≥0}Hom_A(O,tau^nO) はArtin–Zhangの条件下でqgrへの再構成を与えるが、所望のambientの存在・正規境界・smoothnessをHilbert seriesだけから結論できない。

## 定義の整合

次数3の旧公理では構造対象のexceptionalityを独立には要求していなかった。その広い条件はpre-weakと呼び、現在のdegree 3のweakly markedは次数1と同様にexceptionalを要求する部分問題とする。pre-weakからExt^1(O,O)=0は未証明。量子Fermatと既存の正規三次超曲面商はexceptionalなので保持される。

Gabriel–Krull rank-one torsion-freeとn≥0のHilbert数値により負次数の切断数は零になる。非零のO→tau OとO→tau^{-m} Oを合成すれば非零射は単射なのでO(m)≅Oを強制し、h_d(m)>1に矛盾する。End(O)=kとExt^2(O,O)=0はこの結果とSerre双対から従う。追加のexceptionalityの実質はExt^1(O,O)=0。

## 共有する方法と次数別の差

| 項目 | cubic surface (d=3) | dP1 (d=1) |
|---|---|---|
| H_R(t) | (1+t+t²)/(1-t)³ = (1-t³)/(1-t)^4 | (1-t+t²)/(1-t)³ = (1-t⁶)/((1-t)²(1-t²)(1-t³)) |
| 典型ambient | AS4、4個の一次変数 | 重み(1,1,2,3)型 AS4 |
| 境界認識 | 3次元二次Koszul AS3 + 正規3次商 | 重み付き3次元AS3 + 正規6次商 |
| 可換モジュライ方向 | 4 | 8 |
| Poisson方向 | 4 | 2 |
| 合計期待次元 | 8 | 10 |
| 根格子 | E6 | E8 |

同じ帰結を無条件で証明したとみなさず、中心または正規一次境界が与えられたときの相対PBW / AS正則拡大と、内在的な境界の存在を別問題にする。例外collectionやpotentialは構成・計算上のchartとして使っても分類対象には含めない。BGRやBertini型自己同型を忘れる場合、同一視と残余慣性を明記する。

## 各論文の役割

- `papers/weak_cubic_axioms.tex`：d=3。標準正規境界の認識定理と量子Fermat反例。
- `papers/cubic_surface_ambient_moduli.tex`：d=3。モジュライ成分・marked potentialとの比較。
- `papers/nc_del_pezzo_degree1_moduli.tex`：d=1。内在的rank、weighted sextic、pointed dg族、avatar。
- `papers/dp1_anticanonical_models.tex`：d=1。楕円領域の反標準qgrと共鳴、導来比較。
- `papers/nc_cubic_threefold_moduli.tex`：3-fold。別の中心課題であり、研究・論文は独立維持。

## 論理的状態

既存の各論文に記載された証明と、全てのintrinsic対象の網羅性、全モジュライの代数性・既約成分性、heartを保つ標識忘却の大域同値は区別する。次数1の特異楕円境界での導来比較、次数3の正規一次境界の一般存在はいずれも未解決。今回の統合作業は論文内の全証明の独立再監査ではない。

## 量子Fermat ambientの所属成分

量子Fermat BはPymのgraded Calabi–Yauのskew-polynomial成分 L(1,1,1,1) の3-torsion特殊点であり、L(1,1,2)の関係式中の二次補正項Qをu^2 Qにする平坦退化のu=0にもなる。従って少なくとも二成分の交点に属する。一方、既存の四頂点正規直線returnの閉incidenceによりR(1,3)の閉包外。その他の成分との交叉は未解決。式と証明は papers/weak_cubic_axioms.tex recognition-v5。
