# 研究方針：強い内在的非可換三次曲面 H3

2026-11-19 / research-plan-v70 / classification-v375。
**再開時は本書を最初に読む。GitHub main が唯一の正本。**

## 1. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。目標・方針は柔軟に変更し、その理由と元の目標の達成部分・残存部分を、現時点で有効な方針として記す。変更履歴を追記しない。

証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。主要主張の仮定・既知入力・証明箇所・未解決点を明記する。**原稿に証明があること、今回その証明を点検したこと、計算を実行したこと、独立査読を受けたことは別である。** 誤りが見つかれば依存する本文・要約・方針も更新する。

文献は一次資料で適用範囲を確認する。未確認の内容・書誌・新規性を推測しない。原稿は原則日本語LuaLaTeXとし、現在有効な成果を論理順に配置する。研究ノートには論文外で有用な着想・補題・計算・反例・障害・文献比較を保持し、十分な証明が本文にある事項は要点と参照先を置く。

研究の区切りごとの承諾不要保存は許可済み。本プロジェクトでは **GitHub main を正本とし、通常の fast-forward 保存が成功した場合はLibraryに重複保存しない。失敗時のみLibraryを緊急避難先とする。** Libraryの既存ファイルを明示指示なく削除しない。force push、不要なPR、GitHub Actionsは使わない。実行規則は [AGENTS.md](AGENTS.md)。

現行方針・ノート・公表原稿と、理解・検証・再生成に必要な最小限のソース、文献情報、コード、入力、証明書を保持する。旧ZIP・旧原稿・バックアップ・履歴・ログ・キャッシュ・組版中間物を含めない。数学的内容や検証可能性を削って軽量化しない。PDFはソースから再生成しGitでは追跡しない。生成、検証、commit、リモート到達、Library保存は別々に確認・報告する。

## 2. 現在の対象と達成基準

標数0の代数閉体上で、構造対象付きAbel圏 `(A,O)` を扱う。反Serre作用 `tau=S^{-1}[2]` はexactでArtin–Zhang ample、`O` はGabriel–Krull rank-one torsion-free exceptional、反標準Hilbert値は `1+3n(n+1)/2`。反標準環 `R` は一次生成で、二次包絡 `B=Q(R)` は左右noetherian quadratic Koszul AS4型14641である。これが **強いH3** の範囲であり、AS4条件を課さない全weakクラスとは区別する。外部ambient・例外列・周期表示は追加標識にしない。

分類の達成基準は、全対象の必要被覆、全許容切断、pointed exact同値の全矢と慣性、成分・交叉・境界、明示した族条件の下での相対再構成・底変更・降下である。

## 3. 現行原稿の到達点と確実性

主原稿は [papers/nc-cubic-classification.tex](papers/nc-cubic-classification.tex)。以下は**原稿に証明を備える主張**であり、全文の独立監査完了を意味しない。今回の重点点検・再実行の範囲は [検証記録](research/cubic_classification_validation.json) と [実行方針](research/cubic_14641_codex_plan.md) を読む。

| 主張 | 仮定・範囲 | 主な証明箇所 |
|---|---|---|
| 反標準認識 | 強いH3では `R=B/(G)`、`mu_R=1`、`Gv=mu_B^{-1}(v)G` | 主原稿の認識定理、`cubic_nakayama_incidence.tex` |
| 全幾何学的判定 | 非CY二符号型、CY一交換子Ore型・三交換子中心拡大型・可換型 | `cubic_presentation_components.tex`, `thm:h3-complete-geometric-admissibility` |
| 四成分 | 互いに開かつ閉、一般次元3,4,5,8 | 同節 `thm:h3-presentation-four-components` |
| 相対分類 | 明示した相対H3族に対する `[X^H3/PGL4]` | `cubic_formal_intrinsic_reconstruction.tex`, `def:h3-intrinsic-family`, `thm:h3-intrinsic-algebraic-stack` |
| 三次平坦性判定 | 二次関係が部分束、剰余環KoszulならB3平坦から全次数平坦 | 同節 `lem:h3-degree-three-flat-koszul` |
| 可換点の全Artin変形 | 特殊fiberが滑らかな可換三次、次数別平坦な次数変形 | 同節 `thm:h3-commutative-artin-envelope-automatic` |

相対定義では、底上平坦なcoherent対象から生成する厚い圏の導来HomのA完全性、相対Serre、exact反標準作用、AZ豊富性、orbitの底変更、**二次包絡の三次平坦性**を要求する。幾何fiberの条件だけからこれらを自動としない。

重点点検では、三次平坦性の帰納法、可換点のHochschild接計算、一交換子Ore型の極限の分離、可換三次への平滑化、楕円の有限重み窓・線加群・モノドロミーの論理鎖を検討した。スペクトル・CY必要被覆の全排除補題、全外部入力、全検証器の一括再実行、独立査読、新規性の網羅調査は未完了である。

## 4. 未解決の核心と優先順位

1. **全被覆の依存関係を独立に確認する。** 分類ノートの領域別入口から、各被覆定理の必要性と排除証明を対にして読む。外部入力は [as4_imports.json](research/as4_imports.json) の個別SHA・仮定・規約を照合する。新たな反例や欠落が出た場合は全体の完成主張まで遡って訂正する。
2. **非可換点で三次平坦性が自動となる範囲を決める。** Artin小拡大の残差 `delta:W3(B_k) -> kG tensor I` を出発点とする。一次ではG倍のHochschildホモロジー核を計算し、実際の次数別平坦な商変形へ積分できるかを分けて調べる。単なる一次候補を反例としない。
3. **有限判定を実行可能な形へ整える。** 原始三乗根三角形の全中心切断、加法型Kleinian比較などでは、有限判定の証明と、全入力に対する消去・実装の完了を区別する。必要な一領域を選び、入力・停止基準・証明書を固定する。
4. **公表前の文献・可読性監査。** 重要主張の一次資料とIntroductionでの新規性の位置づけを更新し、長い個別排除証明は削らず数学的な単位へ整理する。

AS4条件を課さない広いweakクラスの低次数提示・全包絡存在・全代数性は、本分類からは従わない。別の認識問題として保持する。

## 5. 再開と再現

1. 本書、[実行方針](research/cubic_14641_codex_plan.md)、[現行分類ノート](research/cubic_14641_classification.md)を読む。
2. 主原稿の該当ラベルと検証記録から、必要な計算・一次資料だけを選ぶ。
3. `python3 -m pip install -r requirements.txt`。Python依存はSymPy、python-flint、NumPy、NetworkX。LuaLaTeXはLuaTeX-ja・原ノ味フォント・latexmkを必要とする。
4. `python3 computations/verify_research_bundle.py` で入力・参照・依存宣言の整合性を確認し、リポジトリrootで `latexmk papers/nc-cubic-classification.tex`。PDFは `build/weak_cubic_axioms.pdf`。構造検査は数学的証明の検証ではない。
5. 再実行時は検証器のJSON書出し先を確認する。旧証明書の存在を新たな実行成功と扱わず、実行した入力・終了状態・比較結果を検証記録へ置く。

## 6. 関連研究の正本

| 研究 | 正本 |
|---|---|
| 楕円E6量子化成分・Fricke・DAHA | [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) |
| ambient射・R(1,3) | [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) |
| 標識忘却・Picard作用 | [nc-cubic-unmark](https://github.com/uedakazushi/nc-cubic-unmark) |
| 量子Fermat非AS短報 | [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) |
| heart・Rains共鳴・corner | [nc-dp-surface-hearts](https://github.com/uedakazushi/nc-dp-surface-hearts) |
| 次数1・三次三様体 | [nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli)、[nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli) |

分類に必要な有効な定理・証明・コードは保持する。移管済みの独立論文を旧パスへ再作成しない。別リポジトリの再現コマンドは、その現行READMEを確認して用いる。
