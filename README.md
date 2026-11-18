# 内在的非可換del Pezzo曲面のモジュライとH3分類

2026-11-16。GitHub mainが現行ソースの正本。最初に [研究方針](00_research_plan.md) を読む。逐次研究・約15分checkpoint・通常のmain保存については [AGENTS.md](AGENTS.md) に従う。GitHub Actions、force push、不要なPRを使わず、PDF・ZIP・中間生成物は追跡しない。GitHub保存成功時はLibraryに保存しない。

## 論文別の現在の正本

| 研究 | 正本 |
|---|---|
| H3の内在的認識・完全分類 | **この `nc-cubic-moduli` のmain** |
| 楕円 $E_6$ 量子化成分・Fricke・DAHA | [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) |
| ambient射・R(1,3)成分 | [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) |
| 標識忘却・Picard作用 | [nc-cubic-unmark](https://github.com/uedakazushi/nc-cubic-unmark) |
| 量子Fermat三次曲面がAS surfaceでない短報 | [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) |

分類の主原稿に数学的に必要な認識定理・証明・コードは維持する。別論文の旧独立TeX・専用ノートは分離し、上記の独立mainを公表用正本とする。分類Codexは独立論文を旧パスへ再生成せず、必要な成果を正確に引用する。

## 独立したheart比較・Rains共鳴

四つのheart、Rains共鳴のHRS tiltと混合A2、cubic cornerの研究は [nc-dp-surface-hearts](https://github.com/uedakazushi/nc-dp-surface-hearts) を現行正本とする。

## 14641型intrinsic H3の分類

標数0の強い内在的非可換三次曲面 H3 について、全幾何学的対象、全許容切断、構造対象付き同値および慣性を決定した。有限次数の正規三次入射の H3 開を `X^H3` とすると、相対内在的モジュライは有限型代数スタック `[X^H3/PGL₄]` である。互いに交わらない四既約成分の一般次元は 3、4、5、8。

- [全幾何学的判定・四成分・有限型表示](papers/sections/cubic_presentation_components.tex)
- [相対内在族の定義・反標準環の再構成・有効降下](papers/sections/cubic_formal_intrinsic_reconstruction.tex)
- [全位数に共通する楕円境界の H3 開](papers/sections/cubic_CY_three_alpha_elliptic_relative.tex)
- [研究方針](00_research_plan.md)・[現行分類ノート](research/cubic_14641_classification.md)・[主原稿](papers/weak_cubic_axioms.tex)・[検証範囲](research/cubic_classification_validation.json)・[as4 の輸入記録](research/as4_imports.json)

相対分類は、noetherian 底上の相対 Serre・反標準豊富性・二次包絡の三次平坦性を満たす族を扱う。滑らかな可換三次点では、全次数平坦な任意の Artin 次数変形で三次平坦性が自動になる。非可換点での自動性の範囲は未決定である。

## heart比較とcornerの参照先

公表原稿・証明・研究ノート・検算コードは [専用リポジトリ](https://github.com/uedakazushi/nc-dp-surface-hearts) に移管済み。H3分類で必要な結果は固定commitと仮定を指定して参照する。

## 現行原稿と並行成果

| 対象 | 主原稿・再開ノート |
|---|---|
| H3の幾何学的・相対内在的分類 | [weak_cubic_axioms.tex](papers/weak_cubic_axioms.tex)、[分類ノート](research/cubic_14641_classification.md) |
| 次数3のambient・R13比較 | [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient)、[R13](research/r13_generic_moduli.md) |
| 標識忘却・形式Weyl商・Picard作用 | [nc-cubic-unmark](https://github.com/uedakazushi/nc-cubic-unmark) |
| 量子FermatのOU AS障害 | [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) |
| 次数1のrank・weighted sextic・候補族（移管済み） | [nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli) |
| 次数1の反標準モデル・導来比較（移管済み） | [nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli) |
| 三次三様体と非可換P4（移管済み） | [独立研究リポジトリ](https://github.com/uedakazushi/nc-cubic-threefold-moduli) |

量子FermatはHH_{−1}=HH_1=2、HH_0=5によりOU AS型でなく、intrinsic対象全体をOU/AOUの商と同一視できない。次数1の10次元dg候補族と全intrinsic abelian成分性の問題は[独立研究](https://github.com/uedakazushi/nc-dp1-moduli)へ移管した。三次三様体の形式ambient37、中心対41、一般PGL商13/17、忘却fiber4等の結果とその証明・計算は[独立リポジトリ](https://github.com/uedakazushi/nc-cubic-threefold-moduli)へ移管した。

## 手動再現

```sh
latexmk papers/weak_cubic_axioms.tex
python3 computations/verify_cubic_skew_jets.py
```

その他のH3検証は `research/cubic_classification_validation.json` を参照する。heart比較・共鳴・cornerの再現は [独立リポジトリ](https://github.com/uedakazushi/nc-dp-surface-hearts) にある。PDFやキャッシュをGit追跡しない。
