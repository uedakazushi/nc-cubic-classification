# 四つのheartの比較：研究方針

2026-11-16 / hearts-v19。この一式から再開する場合は本書を最初に読む。現行論文は `papers/nc_del_pezzo_hearts.tex`、補足知識は `research/heart_comparison.md`、検証状態は `research/four_hearts_validation.json`。リポジトリ全体の目標は `00_research_plan.md` にあり、本書はheart比較に対象を限定する。

## 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更は理由と元の目標の達成・未達成を簡潔に記し、現在有効な方針へ書き直す。時系列の変更記録を蓄積しない。

証明済み・追加仮定に依存・未完成・予想・計算的観察を分ける。仮定、既知入力、証明の所在、未解決箇所を明記し、原稿に証明があること、今回の点検、有限検算、外部独立査読を区別する。誤りが判明したら依存する本文・要約・方針を更新し、有用な反例や障害をノートに保持する。

公表用原稿は原則日本語LuaLaTeXとし、一次資料の仮定と適用範囲を確認する。未確認の文献内容を補わない。既知成果と本研究の組合せによる結果を区別し、網羅的新規性未確認を明記する。価値ある数学的内容と証明を軽量化のために削らない。

研究継続用bundleは現行方針・ノート・論文・再現に必要な最小限の原稿、PDF、文献情報、コードと小証明書から自己完結的にする。履歴、旧版、バックアップ、外部文献PDF、コンパイル中間物は含めない。必要な知識を会話だけに残さない。

研究区切りの承諾不要Library保存は一般に許可されている。ただし本研究ではユーザーのプロジェクト固有指示により **GitHub mainが正本であり、GitHub保存成功時にはLibraryへ保存しない。失敗時のみ緊急避難に使う**。既存Library資料は無断削除しない。mainへの通常の保存と遠隔確認を行い、force push・不要なPR・GitHub Actionsを使わない。共有mainの他の研究を損なわない。

生成・証明点検・数値検算・組版・保存を別々の状態として報告する。配布前に必要ファイル、参照、組版、計算、ZIP整合性を確認する。

## 現在の目標と達成基準

四つの構成を、構造対象eと反Serre作用sを指定した比較図式へ置く。圏の存在、dg導来同値、t-exactness、pointed性、境界・marking、相対降下を分ける。公表用原稿は `papers/nc_del_pezzo_hearts.tex` と五つのsectionからなる25ページの現行稿である。

既存のVdB–Rains一致条件、指定genuine楕円gluingの導来比較とHRS tilt、共鳴の符号判定、AOUの構造対象の同定、混合A2の証明を保持した。新しい中心は `papers/sections/four_hearts_corner_locus.tex`。同プロジェクトの別稿の有限corner判定を証明ごと統合し、指定AOU同値のt-exactnessの必要十分条件に接続した。別稿にある全Hilbert関数や一様cutoffの詳細も削除していない。

## 現在の主要な到達点

標準九頂点三block potential Wの構造頂点pを除く商C=B/BpBは、残る十八係数だけに依存する。C有限次元 iff 十八係数が非零で、Q=(w2bc/w1bc)の九つの2×2 minor、det Q、det(entrywise reciprocal Q)が全て非零。これは純粋な代数命題で、BのAS正則性・noetherian性を仮定しない。

ASへの適用では標準周期実現とBの右noetherian性を仮定する。C有限なら両corner bimoduleの有限生成性とpBpの右noetherian性は自動である。標準ASの有限projective解消とvery strong helixから全coherent対象への高次Extのtail消滅も得た。AOU許容領域で指定Ψがt-exactであること、自然cornerのabel同値、C有限、上記係数条件は同値となる。既存のE0=πFと反標準環Fの同定がこの接続に必要である。

行・列rescalingでQを第一行・第一列が1に正規化すると、四交比a,b,c,dと十一因子の積Δを得る。D(Δ)は標識付き一般位置六点のmoduli M_cubic。全二十七係数非零の八次元係数商では、有限corner開集合は非標準的にM_cubic×(Gm)^4となる。これは係数空間の結論であり、その全点がAS正則・noetherianであるとは主張しない。無限位数translationもZariski開条件とは呼ばない。

## 残る核心と優先順位

最優先は同じ楕円データに対するVdB最後のsection-model関手とRains自然Φを、構造対象・境界・gluing bimoduleを含めて同定すること。AOU側のpointed性と標準noetherian表示におけるt-exactness判定は済んだため、これらを再び未解決として繰り返さない。まずVdBの関手の構造対象と境界の像を照合し、生成orbit上の自然同型を全圏へ延長できる条件を調べる。

次に、AOUの楕円パラメータから十一因子の零点集合を直接記述し、どの退化が実際のAS/admissible locusに存在するかを確定する。係数判別因子からRains負指数根の存在を無条件に推論しない。標準周期表示外やnoetherian性未確認の対象はこの判定の外にある。

族では相対Homのperfectness、基底変更、同値kernelの相対性、t構造と標識の降下が残る。既存の相対構造対象の同定と係数開性だけでは全heartの相対同値にならない。混合A2のアフィン商は同型型まで決定済みだが、元の楕円生成元のcharacter値・非対角係数・kernelの生成元は未計算。

この方針は、従来の「有限cornerと両bimodule条件を検証する」という課題を標準三block表示で解決したために更新した。四者比較全体の元の目標のうち、AS–反標準の指定同値について必要十分条件を得たが、独立構成間のデータ・関手の一致と全相対降下は残る。2025年Rains monographとの網羅的新規性照合は未完了である。

## 再現と検証範囲

一式のrootで次を実行する。

    python3 computations/verify_cubic_heart_numerics.py
    python3 computations/verify_four_hearts.py
    python3 computations/verify_four_hearts_corner.py
    latexmk -lualatex -outdir=build papers/nc_del_pezzo_hearts.tex

Python標準ライブラリ、LuaLaTeX、LuaTeX-ja、tikz-cd、latexmkが必要。新コードは六点復元の六恒等式を12変数整数多項式として全係数検査し、具体例の全関係行列をQQと有限体で独立に消去する。係数torusの重み階数・四交比の不変性・整数切断も確認する。既存の40,000通りの混合A2検算、K0/Euler計算、mutation位置検査を再実行した。

全文25ページを組版し、全ページ画像を点検した。生成・有限検算・文献確認・GitHub保存の正確な状態は `research/four_hearts_validation.json` を読む。今回以前の全証明の独立再査読や外部査読、Lean等の形式化はしていない。GitHub保存後のLibraryアップロードは行わない。
