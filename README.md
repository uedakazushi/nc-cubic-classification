# 強い内在的非可換三次曲面 H3 の分類

**共同研究：** 本リポジトリは大川新之介・植田一石の共同研究プロジェクトです。この表示は個々の論文の著者を確定するものではありません。

2026-11-19 / classification-v375。最初に [研究方針](00_research_plan.md) を読む。
GitHub main が現行ソースの正本。研究・保存の規則は [AGENTS.md](AGENTS.md)。

## 対象と主結果

標数0の強い内在的H3は、反標準環が一次生成で、その二次包絡がnoetherian quadratic Koszul AS4型14641となる構造対象付きAbel圏である。AS4条件を課さない全weakクラスは別の認識問題として残る。

現行原稿は、強いH3の全幾何学的対象・許容切断・構造対象付き同値と慣性を記述する。四つの開かつ閉な既約成分の一般次元は **3、4、5、8**。全幾何学的判定は `thm:h3-complete-geometric-admissibility`、四成分は `thm:h3-presentation-four-components` を参照する。

相対分類は、**導来HomのA完全性、相対Serre、exact反標準作用、AZ豊富性、orbitの底変更、二次包絡の三次平坦性**を明記した相対族について、モジュライスタック `\mathfrak H_3\simeq[X^{\mathrm{H3}}/\mathrm{PGL}_4]`を有限型代数stackとして与える。定義は `def:h3-intrinsic-family`。滑らかな可換三次点では、次数別平坦な全Artin次数変形の包絡平坦性は自動となる。一般の非可換点での自動性は未決定である。

**証明が原稿にあることと、全文の独立監査が完了したことは区別する。** 今回の重点点検、実際に再実行した検算、未実行の証明書、組版の状態は [検証記録](research/cubic_classification_validation.json) に分けて記す。

## 現行資料

| 目的 | 入口 |
|---|---|
| 目標・未解決の核心・再開 | [研究方針](00_research_plan.md) |
| 証明の依存関係・次の検証 | [実行方針](research/cubic_14641_codex_plan.md) |
| 数式・反例・計算上の障害 | [分類ノート](research/cubic_14641_classification.md) |
| 公表原稿と全証明 | [nc-cubic-classification.tex](papers/nc-cubic-classification.tex) |
| 全幾何学的判定と四成分 | [cubic_presentation_components.tex](papers/sections/cubic_presentation_components.tex) |
| 相対内在族とArtin変形 | [cubic_formal_intrinsic_reconstruction.tex](papers/sections/cubic_formal_intrinsic_reconstruction.tex) |
| 計算・組版・点検の範囲 | [検証記録](research/cubic_classification_validation.json) |
| 外部as4入力の仮定・固定SHA | [as4_imports.json](research/as4_imports.json) |

## 再現

Python依存を揃え、リポジトリrootで実行する。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_research_bundle.py
python3 computations/verify_cubic_CY_three_alpha_elliptic_line.py
python3 computations/verify_cubic_skew_jets.py
python3 computations/verify_cubic_CY_three_alpha_elliptic_diagonal.py
python3 computations/verify_cubic_CY_three_alpha_elliptic_monodromy.py
latexmk papers/nc-cubic-classification.tex
```

LuaLaTeXにはLuaTeX-ja・原ノ味フォント・latexmkが必要。出力PDFは `build/nc-cubic-classification.pdf`。検算はそれぞれの入力に対する主張を確認するもので、上の少数コマンドだけで全分類を再検証するものではない。JSONを書き直す検証器もあるため、出力diffを確認する。

現行ソース・必要なコード・入力・証明書だけを保持し、PDF・ZIP・組版中間物・実行ログはGit追跡しない。通常のmain保存が成功した場合はLibraryに重複保存しない。

## 関連する独立研究

E6量子化成分・Fricke・DAHAは [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6)、ambient射は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient)、標識忘却は [nc-cubic-unmark](https://github.com/uedakazushi/nc-cubic-unmark)、量子Fermat非AS短報は [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) が正本。分類に必要な定理・証明・コードは本リポジトリにも保持するが、移管済みの独立論文を旧パスへ再作成しない。

heart・共鳴・cornerは [nc-dp-surface-hearts](https://github.com/uedakazushi/nc-dp-surface-hearts)、次数1は [nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli)、三次三様体は [nc-cubic-threefold](https://github.com/uedakazushi/nc-cubic-threefold)。
