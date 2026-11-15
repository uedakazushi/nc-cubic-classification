# 四つのheartの比較：研究方針

2026-11-16 / hearts-v18。この一式から再開する場合は本書を最初に読む。現行論文は `papers/nc_del_pezzo_hearts.tex`、補足知識は `research/heart_comparison.md`、検証状態は `research/four_hearts_validation.json`。リポジトリ全体の目標は `00_research_plan.md` にあり、本書はheart比較に対象を限定する。

## 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更は理由と元の目標の達成・未達成を簡潔に記し、現在有効な方針へ書き直す。時系列の変更記録を蓄積しない。

証明済み・追加仮定に依存・未完成・予想・計算的観察を分ける。仮定、既知入力、証明の所在、未解決箇所を明記し、原稿に証明があること、今回の点検、有限検算、外部独立査読を区別する。誤りが判明したら依存する本文・要約・方針を更新し、有用な反例や障害をノートに保持する。

公表用原稿は原則日本語LuaLaTeXとし、一次資料の仮定と適用範囲を確認する。未確認の文献内容を補わない。既知成果と本研究の組合せによる結果を区別し、網羅的新規性未確認を明記する。価値ある数学的内容と証明を軽量化のために削らない。

研究継続用bundleは現行方針・ノート・論文・再現に必要な最小限の原稿、PDF、文献情報、コードと小証明書から自己完結的にする。履歴、旧版、バックアップ、外部文献PDF、コンパイル中間物は含めない。必要な知識を会話だけに残さない。

研究区切りの承諾不要Library保存は一般に許可されている。ただし本研究ではユーザーのプロジェクト固有指示により **GitHub mainが正本であり、GitHub保存成功時にはLibraryへ保存しない。失敗時のみ緊急避難に使う**。既存Library資料は無断削除しない。mainへの通常の保存と遠隔確認を行い、force push・不要なPR・GitHub Actionsを使わない。共有mainの他の研究を損なわない。

生成・証明点検・数値検算・組版・保存を別々の状態として報告する。配布前に必要ファイル、参照、組版、計算、ZIP整合性を確認する。

## 現在の目標と達成基準

四つの構成を、構造対象eと反Serre作用sを指定した同じ比較図式へ置く。各比較について、圏の存在、dg導来同値、t-exactness、pointed性、境界・marking、相対降下を別々に確定する。全四heartの無条件な一致を目標の代用にしない。

現行稿は21ページの比較論文として、VdB–Rainsの一致条件、Rains–反標準の指定gluingでの導来同値と全heartのHRS tilt、AS–反標準の有限corner判定、混合A2の具体模型を証明付きでまとめた。関連する詳細な最大共鳴・zigzag・cubic cornerの成果は別の現行原稿に保持され、本比較稿の未証明入力として暗黙に使用していない。

## 到達点と未解決の核心

同じ初期heart・中心・gluing・blow-downを同定したVdBとRainsはt-exactに比較できる。section modelへの置換は別操作である。genuine smooth classical del Pezzoとsmooth elliptic boundaryからの指定gluingでは、自然な反標準導来切断が同値となり、全heartは一回のHRS tiltで比較される。負指数の実在根はAZ失敗とheart非一致を検出するが導来同値は保たれる。

AS側ではAOUの許容楕円データについて、mutation後の先頭E0とπFの実際の同定を証明した。最後の二つの左mutationに現れる全Homは、境界の非自明な次数零線束のcohomologyと同型であり零となる。従ってAOU同値はpointedで、AS構造対象の反標準環はFそのものである。これはAOUの既知結果の明示的な帰結として位置づける。

foldingと両corner bimoduleの有限生成性の下で、有限corner条件から指定AOU関手のt-exactnessも得る。未完成なのは全AS/AOU領域におけるその条件の検証と、独立なVdB/Rainsデータ・関手の照合である。構造対象の相対同定は相対Homのperfectness・基底変更を仮定して証明したが、相対heartやstack降下全体は未完成。

## 優先順位と具体的な着手

公表に向けた最優先課題は、指定AOU領域で有限cornerと両bimodule条件がどの範囲に成立するかを確定することである。構造対象の同定は解決済みであり、それを新たな未解決課題として繰り返さない。同じ六点とσの規約を揃え、VdB最後のsection-model関手とRainsの自然Φをkernelまたはgluing moduleで比較する。

この優先順位は、pointed比較の障害を解消したために変更した。元の四者比較のうち、AOU側の構造対象と反標準環の接続は達成し、全域のt-exactness、別構成とのデータ照合、族の降下は残る。論文の主張は既知入力からの帰結と本稿の構造定理を明確に分け、2025年Rains monographとの新規性照合をさらに進める。

AS–反標準では、指定folded代数の構造頂点pについてB/BpBの有限性と両bimodule条件を照合する。既存cubic corner計算を使う場合には道長gradingと反標準cut gradingを明示する。点での同値を確認してから、相対perfect性・基底変更・消滅の一様性・pointed descentへ進む。

混合A2ではAからΠ(A2)への商の同型型は決まっている。残るのは元の楕円生成元のcharacter値・非対角係数・kernelの生成元であり、分離と非分裂性の真偽を再び未解決としない。

## 再現

一式のrootで `python3 computations/verify_cubic_heart_numerics.py`、`python3 computations/verify_four_hearts.py`、`latexmk -lualatex -outdir=build papers/nc_del_pezzo_hearts.tex` を実行する。Python標準ライブラリ、LuaLaTeX、LuaTeX-ja、tikz-cd、latexmkが必要。文献情報と識別子は論文末尾に含まれる。

今回の実行範囲：全文21ページのLuaLaTeX組版、参照50個・文献11件の整合、既存数値コードと40,000通りの検算の再実行、AOU mutationの標識位置と二つのrestriction次数の検算。既存の全証明を独立に再査読したという意味ではない。Libraryへのアップロード操作は行っていない。
