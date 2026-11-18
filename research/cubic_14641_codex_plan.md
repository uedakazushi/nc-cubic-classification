# H3分類の検証・実行方針

2026-11-19 / classification-v375。
研究の対象と保存原則は [研究方針](../00_research_plan.md)、実行規則は [AGENTS.md](../AGENTS.md)。本書は現在有効な検証の入口であり、版ごとの進捗記録を置かない。

## 1. 主張と検証の区別

現行主原稿は強いH3の全幾何学的分類と、定義した相対族に対する有限型商stackの証明を記載する。今回の整理で数学的な全被覆を新たに証明した、あるいは全証明を独立検証し終えたとはしない。

- **原稿に証明あり**：現行の定理と参照する補題を読める。
- **重点点検済み**：検証記録に列挙した論理段階を今回読んで確認した。未監査の依存補題まで含めない。
- **再実行成功**：指定コード・入力を実行し終了状態と出力を確認した。有限計算が通常証明を代替するとはしない。
- **既存証明書を保持**：再現に必要なので保持するが、今回未実行のものはPASSを今回の結果として数えない。
- **未完了**：一般の非可換点の三次平坦性自動性、全weakクラスへの拡張、全証明の独立査読・新規性監査。

## 2. 主定理の依存関係

| 段階 | 読む箇所（`papers/sections/`） | 検証上の注意 |
|---|---|---|
| 反標準環・中山条件 | `cubic_nakayama_incidence.tex`、主原稿の認識定理 | AS指数1、epsilon仮定、右左・中山規約 |
| スペクトルの必要被覆 | `cubic_spectral_resonance.tex` から各三・四固有値排除、`cubic_jordan22_unipotent_vertex.tex` | 一般点のrank計算と全パラメータ被覆を区別 |
| 非CYの二符号型 | `cubic_order2_full_moduli.tex`、`cubic_order2_22_secant_L_complete.tex` | 全Jordan型・例外pivot・整域性・rank条件 |
| CYの交換子別被覆 | `cubic_CY_second_quadric.tex`、`cubic_CY_one_segre_double_split.tex`、`cubic_CY_three_alpha_smooth_boundary.tex` | cは関係空間と外積の交叉次元 |
| 楕円許容性 | `cubic_CY_three_alpha_elliptic_diagonal.tex`、`...fixed_boundary.tex`、`...line_modules.tex` | 双加群非滑らかだけで左大域次元無限としない |
| 退化境界 | `cubic_CY_three_alpha_additive.tex`、`...quantum_triangle.tex`、`...nodal_E6.tex`、`...primitive_triangle.tex` | 有限判定の存在と実装完了を区別 |
| 四成分 | `cubic_presentation_components.tex` | trace分離とCY二部分の極限分離を別々に確認 |
| 相対stack | 同節、`cubic_formal_intrinsic_reconstruction.tex`、`...elliptic_relative.tex` | A完全性・豊富性・底変更・三次平坦性を省略しない |
| 可換点の全Artin変形 | `cubic_formal_intrinsic_reconstruction.tex` 最終節 | HH²の4+4、枠付き接次元23、各可換点の局所次元下界、小拡大のtorsor比較 |

個々の補題の数式・反例・計算資産は [現行分類ノート](cubic_14641_classification.md) に整理する。一次資料の輸入は [as4_imports.json](as4_imports.json) の個別記録に従う。

## 3. 計算を選ぶ基準

必要被覆の全値性に関わる場合、有限標本の成功で済ませず、単元minor、飽和、例外根、数体上の厳密演算を再生する。楕円判別式では、有限重み窓が全Extを計算する通常証明を先に確認し、その後に作用行列と特性多項式を再実行する。

モノドロミー検証器の25点は次数上界を使った有理数からの厳密補間である。追加12点は**復元した多項式の判別式の特殊化整合性検査**であり、新たに対角複体を計算した12例ではない。

検算は別の一時ディレクトリで行うか、出力JSONの変更を必ずdiffで確認する。計算資産を過去版のキャッシュと取り違えない。独立な確認として、文献の仮定、有限窓の全次数への論理、例外パラメータの被覆を優先する。

## 4. 次に着手する最小課題

非可換点の三次平坦性について、固定包絡Bと正規三次Gを一つ選び、`prop:h3-cubic-flatness-small-extension` の四係数残差を計算する。一次のHochschild核が零なら一次自動性までを記録し、全Artinへの延長には接写像の全射性と持ち上げ障害を別に確認する。核が非零でも、次数別平坦な商の全次数積を構成するまで反例としない。

独立監査を続ける場合は、全H3の必要被覆に使うas4入力を一つ選び、固定SHA、前提、通常証明、計算証明書の四者を照合する。難しい補題については未確認箇所を特定し、計算だけを増やさない。

## 5. 検証結果の保存

[検証記録](cubic_classification_validation.json) は現行状態だけを置く。今回の実行、保持した証明書、通常証明の点検、組版の状態を別項目で記す。過去版のページ数や累計PASS数を現行状態として使わない。ソース・証明書・参照先の欠落とdiffを点検し、通常のmain保存後にリモートSHAを確認する。
