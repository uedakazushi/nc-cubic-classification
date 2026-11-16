# 研究方針：H3分類と量子三次曲面を含む既約成分

2026-11-17 / research-plan-v33 / triangle-component-v3。
**再開時は本書を最初に読む。GitHub mainが唯一の正本。**
実行規則は `AGENTS.md`。既存の全H3分類の詳細と必要な式は
`research/cubic_14641_classification.md`、`research/cubic_14641_codex_plan.md`、
`research/cubic_classification_validation.json` に保持する。
本書は現在の優先順位と文書の入口を整理し、証明・計算の重複を置かない。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。
目標と方針は柔軟に変更し、重要な変更の理由、元の目標の達成部分と残存部分を現在有効な方針として書き直す。

証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定、既知入力、証明の所在、未解決箇所を明記する。
原稿に証明があること、今回の点検、計算の実行、独立査読は別である。誤りは依存する本文・要約・方針にも反映する。
文献は一次資料で仮定と適用範囲を確認し、未確認の書誌・内容・新規性を推測しない。

公表原稿は原則として日本語LuaLaTeXで、現在の成果を論理順に構成する。価値ある結果と十分な証明を保持する。
研究ノートには有用な着想、補題、例、反例、障害、文献比較を整理し、作業日誌や旧版の対応表にしない。
再開に必要な知識を会話だけに残さず、現行の方針・ノート・論文と必要コード・入力・小証明書で再開できる状態を保つ。
旧ZIP、旧原稿、バックアップ、ログ、キャッシュ、コンパイル中間物、入れ子のbundleは収録しない。数学的内容を削って軽量化しない。

研究区切りの承諾不要Library保存は一般的に許可されているが、本プロジェクトでは**GitHub mainを正本とし、GitHub保存成功時はLibraryへ保存しない。失敗時だけ緊急避難先として用いる。**
Library既存ファイルは明示指示なしに削除しない。GitではPDF・ZIP・中間生成物を追跡せず、TeX等から再生成する。
生成、検証、commit、リモート到達、Library保存は別状態として、実際に確認できたことだけを報告する。
通常のfast-forwardのみでmainへ保存し、force push、不要なPR、GitHub Actionsは使わない。
共有mainの更新は読み直して保存し、約15分checkpointは研究の終了条件ではない。未設定の背景実行や自動再開を約束しない。

## II. 現在の目標と達成基準

大域的な目標は強いintrinsic 14641型非可換三次曲面H3の完全分類である。
対象は構造対象付きAbel圏で、反Serre作用、Gabriel–Krull rank、exceptionality、AZ ampleness、三次曲面のHilbert値を満たし、
反標準環が一次生成、その二次包絡がnoetherian quadratic Koszul AS4型14641となるもの。
外部ambient・四周期表示・例外列を追加標識にしない。
全対象の被覆、全許容切断、pointed exact同値の全群oidと慣性、成分・交叉・境界、相対再構成・降下を達成基準とする。

**現在の最優先課題は、量子so3固定包絡の4次元族と、それを含む7次元H3族を通る既約成分の完全決定である。**
この焦点はユーザーの成分決定の依頼に基づく。4次元族の非成分性は解決済みだが、全成分の大域的同定と全境界は未解決である。
7次元族を最終成分と決め打ちせず、一般Etingof–Ginzburg型中央三次商を含む8次元成分を検証する。
全H3分類の他の枝の成果・未解決問題を消したり、この限定研究の結論で置き換えたりしない。

## III. 成分研究の到達点と直ちに着手する課題

専用方針は `research/quantum_cubic_component/00_research_plan.md`、ノートは同ディレクトリの `component_notes.md`。
公表原稿は `papers/quantum_cubic_component.tex`。新しいArtin再構成の証明は
`papers/sections/quantum_cubic_artin_reconstruction.tex` から読み込む。

現行原稿は、7次元PBW族と全中心・全矢、固定位数3の開正常形、三捩れを離れる全次数の中心三次持上げ、
超越的中心値のH3性、滑らかな中心と反標準分岐の下でのHH^2=8・HH^3=0を保持する。
105×40の一次incidenceはrank18、核22、座標変更14方向、商8であり、既知7方向と横断1方向が核を張る。
これを全intrinsic変形の被覆や全成分分類と混同しない。

**Artin再構成の成果**：適合したenhancementを持つflat Abel変形からdg圏変形への写像は、全局所Artin底で同型類上単射である。
反標準ample列のExt消滅とDe Deken–Lowen Theorem4.5、exceptional対象の持上げを使う。
従ってこの相対変形問題では、一般点のH3接空間の次元は8以下。
また相対Serre作用が底変更に適合するsmooth proper dg変形では、反標準環は次数別有限自由、左右noetherianで、四一次生成元・六二次関係・一三次関係の表示を持つ。
一般dg変形のheart存在、二次包絡のAS4性、三次核の正則正規性は結論していない。

次は、二次関係の三次syzygyと高次Koszul複体を持ち上げ、二次包絡の平坦性・AS4性を証明する。
R_Aの平坦性だけからQ(R_A)の平坦性を推論しない。その後、相対H3族の実現・代数性、
滑らかな楕円境界を失う点を含む閉包の全境界・同型群oidを決定する。
八次元成分の一意性は現行の比較仮定付き定理であり、全成分の完全決定ではない。

## IV. 全H3分類で保持する成果と未解決領域

詳細な証明と全係数は `papers/weak_cubic_axioms.tex` と読み込まれる各節、現行分類ノートにある。
今回この大規模分類の証明を独立再監査したわけではない。

- 全H3でmu_R=1、Gのnormalizerはmu_Bの逆。固定包絡の候補は単一140×20線型核。全skew包絡は31パラメータ・五型で幾何学的分類され、一般次元は4,1,2,1,0。
- 中央滑らか楕円境界はfiltered deformationからCY包絡を認識。有限位数の許容性は中心McKay条件、固定有限位数の被約表示族では中心形成・H3開性・底変更を扱う。非中央正規楕円境界は位数2または3で、Clifford swap・符号型・量子Fermatへ認識される。
- 分裂・非分裂Clifford族、指定PI4包絡の悪い中心値6個、有限位数一般の判定、非CY符号族のorderとBrauer分岐、量子三角境界の有限位数切断判定、固定三乗根の全P4中心切断・境界因子・慣性を保持する。
- proper Sklyanin、Stafford、指定Pym chart、指定as4具体表示の排除を保持する。全AS4の被覆を仮定しない。外部入力は `research/as4_imports.json` の固定SHAと規約を用いる。
- スペクトル(1,3)は幾何学的分類、(3,1)と(2,2) mixed rank2は全Jordan型込みで排除。mixed rank4のP=0,Q=0は既知族へ認識。両top非零の残余は詳細分類ノートの現行frontierを読む。

確認時の分類frontierは **classification-v200**。最後のL0非鏡開集合の有理二パラメータ表示と正則逆写像・分母条件を検証済みで、portableな正常行加群builderがある。
最終飽和判定は未完であり、この有理表示だけからH3排除を結論しない。
次はkernel/正常行加群商のAnnを指定分母Uで飽和するか、B=0で正則な汎関数を追加する。
具体式・入力・未完箇所は `research/cubic_14641_classification.md` と `research/cubic_classification_validation.json` に保持する。
全CY被覆、三固有値以上、全成分とintrinsic族降下も未完成である。

## V. 再現・関連研究

成分研究はリポジトリrootで次を実行する。
```sh
python3 -m pip install -r computations/quantum_cubic_component/requirements.txt
python3 computations/quantum_cubic_component/verify_all.py
latexmk -lualatex papers/quantum_cubic_component.tex
```
検証証明書は `computations/quantum_cubic_component/validation.json`。5検証器は厳密演算で再実行済み。
Artin再構成は通常の数学的証明であり、計算PASSと区別する。独立原稿をLuaLaTeXで組版し、既存H3主原稿全体は再組版していない。
全H3分類の再現手順は `research/cubic_classification_validation.json`、例は `python3 computations/verify_cubic_skew_jets.py`。

heart比較・Rains共鳴・cubic cornerは `uedakazushi/nc-dp-surface-hearts`、次数1は `uedakazushi/nc-dp1-moduli`、三次三様体は `uedakazushi/nc-cubic-threefold-moduli` が正本。
量子FermatのOU障害は `papers/quantum_fermat_not_as_surface.tex`、ambient比較は `papers/cubic_surface_ambient_moduli.tex` に保持する。
