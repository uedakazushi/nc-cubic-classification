# 四つのheartの比較：研究方針

2026-11-16 / hearts-v22。この一式から再開する場合は本書を最初に読む。現行論文は `papers/nc_del_pezzo_hearts.tex`、補足知識は `research/heart_comparison.md`、検証状態は `research/four_hearts_validation.json`。リポジトリ全体の目標は `00_research_plan.md` にあり、本書はheart比較に対象を限定する。

## 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更は理由と元の目標の達成・未達成を簡潔に記し、現在有効な方針へ書き直す。時系列の変更記録を蓄積しない。

証明済み・追加仮定に依存・未完成・予想・計算的観察を分ける。仮定、既知入力、証明の所在、未解決箇所を明記し、原稿に証明があること、今回の点検、有限検算、外部独立査読を区別する。誤りが判明したら依存する本文・要約・方針を更新し、有用な反例や障害をノートに保持する。

公表用原稿は原則日本語LuaLaTeXとし、一次資料の仮定と適用範囲を確認する。未確認の文献内容を補わない。既知成果と本研究の組合せによる結果を区別し、網羅的新規性未確認を明記する。価値ある数学的内容と証明を軽量化のために削らない。

研究継続用bundleは現行方針・ノート・論文・再現に必要な最小限の原稿、PDF、文献情報、コードと小証明書から自己完結的にする。履歴、旧版、バックアップ、外部文献PDF、コンパイル中間物は含めない。必要な知識を会話だけに残さない。

研究区切りの承諾不要Library保存は一般に許可されている。ただし本研究ではユーザーのプロジェクト固有指示により **GitHub mainが正本であり、GitHub保存成功時にはLibraryへ保存しない。失敗時のみ緊急避難に使う**。既存Library資料は無断削除しない。mainへの通常の保存と遠隔確認を行い、force push・不要なPR・GitHub Actionsを使わない。共有mainの他の研究を損なわない。

生成・証明点検・数値検算・組版・保存を別々の状態として報告する。配布前に必要ファイル、参照、組版、計算、ZIP整合性を確認する。

## 最優先の目標：公表する論文の価値と正確性

自然な比較関手と構造対象を明示し、先行研究と区別できる正確な中心結果を優先する。主張を増やすことより、依存する規約・仮定を解決することを重視する。現行稿は38ページ、主TeXと八つのsectionからなる。今回の中心は `four_hearts_boundary_data.tex` の復元式と整合性検査である。

## 現在の結論と要注意事項

**公表前の最優先事項**：AOU v1 (9.2),(9.3),(9.25)の境界shiftと(9.47)のrestriction tupleを、同じ曲線・点ラベル・restriction同定で文字通り併用すると、非torsion translationと両立しない。このことは原典の主定理全体の否定でも、どの式が誤植かを確定した結果でもない。独立な表示を接続する際の規約の障害である。

σ=t_b、L1=σ*L0、Q=L1/L0=P_(−3b)とすると、restriction側からq=Q、境界translation t_(−3b)、構造対象の境界像L0³Q^−3(−D)を得る。印刷されたshiftをσ_*³(−⊗N)、N=L0 σ*L0 σ²*L0(−D)と読むと、translation t_(3b)、構造対象像L0³(−D)。同時成立にはQ²=Q³=Oが必要である。点支持と構造対象を使う独立の検査であり、単なる符号の好みではない。

このためAOUのpointed性と、それを使う指定AOU関手のt-exactness・四者接続は、**実際のrestrictionが与える二つの次数零線束が非自明である条件(R)**の下の結果として書き直した。既存のmutationの評価triangleによる証明は保持するが、未整合な座標式から(R)が自動成立するとは現在主張しない。前の自動的な座標適用の評価は修正した。独立の十一条件の純代数定理とRainsのgenuine gluing・整列結果はこの座標同定に依存しないので保持する（今回それら全証明を新たに独立再監査したという意味ではない）。

**復元の明示式**：Rains gluingのrank u、c1=D、c=χ(e,x)に対しdet Fq(x)=ρ(D)q^(c−u)。q=P_aなら境界反Serre作用はt_(a*) (−⊗ρ(H))である。実際のordered restriction tupleが(k_pi,U2,U1,O)ならq=U2 U1^−2、L=U1 U2^−1。forward RHomと合成を保つrestrictionの下で、Rainsの既知の三角dg模型を使ってpointed復元ができる。これはheartのt-exact同定ではない。

境界作用t_(a*)(−⊗N)を先に固定すればq=P_a、L³=N(Σpi)となり、Lの候補はE[3]の九通り。印刷shiftを保持する場合にはq=L0/L1、L=L1 ε、U1=L0^−1 ε^−1、U2=(L0L1)^−1 ε^−2（ε∈E[3]）が必要な候補となる。これを未検証の原典訂正式として採用してはならない。実際のrestriction tupleを計算して九候補のどれかを決める必要がある。

## 保持する成果と適用範囲

同じ最終VdB blow-upの構造対象・Serre作用を使う抽象的な関手認識は保持する。ASへ接続するときには上の実際の条件(R)を明示する。十一因子ΔによるC=B/BpBの有限性判定は独立の代数定理であり、ASの標準noetherian周期表示への適用と分離する。

Rains単独の指定genuine楕円gluing、q非torsionでは、全heartの差Fは境界非交叉有限長圏Zに集中し、t-exactness、AZ ampleness、全実在Z単純のEuler正値が同値となる。有限ADEのEuler chamber手順と、正整数倍点の整列公式、同じ六点から得る720個の埋め込まれたheart、全simple次元(6,1,1,2,2,4)は現行稿に保持する。具体行列や全heartの分類ではない。

## 次の着手と成功条件

最優先はAOUの元のblow-up構成から、同じ固定境界同定でB1,B2の実際のrestrictionとshiftを独立に再計算すること。(9.3),(9.25)を採るなら上のE[3]候補に一致するかを確認する。(9.47)を採るなら境界shift側の同定を追い直す。inverse、点の移動、push/pull、途中のsection-modelへの置換のどれが必要かを明示する。未確認のどれか一つを修正式として固定しない。

実際の二つの次数零restrictionの非自明性を確認して初めて、AOU許容パラメータへの無条件なpointed適用を回復する。その後、十一因子の楕円パラメータ表示と実在AS/noetherian領域との交叉へ進む。境界作用のみを合わせても全gluingやheartが一致したとはしない。

Rains 2025 monographの全文との新規性照合は未完了。今回も取得を試みたが成功せず、概要以上を確認したとはしない。外部査読・形式化・相対heartと降下・元の生成元の作用係数も未完了である。

## 再現と検証

    python3 computations/verify_cubic_heart_numerics.py
    python3 computations/verify_four_hearts.py
    python3 computations/verify_four_hearts_corner.py
    python3 computations/verify_four_hearts_chambers.py
    python3 computations/verify_four_hearts_sorted.py
    python3 computations/verify_four_hearts_boundary.py
    latexmk -lualatex -outdir=build papers/nc_del_pezzo_hearts.tex

Python標準ライブラリ、LuaLaTeX、LuaTeX-ja、tikz-cd、latexmkを用いる。六コードを現行入力で実行した。新しい境界検査は六次数の1587個のK0ベクトル、Orlov Euler行列からの反Serre列、Picardの形式計算と九つの3捩れ候補を検査する。これは実際の境界同定や原典の修正式を計算で証明したものではない。

全文38ページ・95ラベル・13文献。生成、全文組版、画像点検、清浄ディレクトリでの再現、遠隔保存の状態はvalidationで区別する。GitHub保存成功時にはLibraryへ別途保存しない。
