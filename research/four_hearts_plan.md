# 四つのheartの比較：研究方針

2026-11-16 / hearts-v23。この一式から再開する場合は本書を最初に読む。現行論文は `papers/nc_del_pezzo_hearts.tex`、補足知識は `research/heart_comparison.md`、検証状態は `research/four_hearts_validation.json`。リポジトリ全体の目標は `00_research_plan.md` にあり、本書はheart比較に対象を限定する。

## 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更は理由と元の目標の達成・未達成を簡潔に記し、現在有効な方針へ書き直す。時系列の変更記録を蓄積しない。

証明済み・追加仮定に依存・未完成・予想・計算的観察を分ける。仮定、既知入力、証明の所在、未解決箇所を明記し、原稿に証明があること、今回の点検、有限検算、外部独立査読を区別する。誤りが判明したら依存する本文・要約・方針を更新し、有用な反例や障害をノートに保持する。

公表用原稿は原則日本語LuaLaTeXとし、一次資料の仮定と適用範囲を確認する。未確認の文献内容を補わない。既知成果と本研究の組合せによる結果を区別し、網羅的新規性未確認を明記する。価値ある数学的内容と証明を軽量化のために削らない。

研究継続用bundleは現行方針・ノート・論文・再現に必要な最小限の原稿、PDF、文献情報、コードと小証明書から自己完結的にする。履歴、旧版、バックアップ、外部文献PDF、コンパイル中間物は含めない。必要な知識を会話だけに残さない。

研究区切りの承諾不要Library保存は一般に許可されている。ただし本研究ではユーザーのプロジェクト固有指示により **GitHub mainが正本であり、GitHub保存成功時にはLibraryへ保存しない。失敗時のみ緊急避難に使う**。既存Library資料は無断削除しない。mainへの通常の保存と遠隔確認を行い、force push・不要なPR・GitHub Actionsを使わない。共有mainの他の研究を損なわない。

生成・証明点検・数値検算・組版・保存を別々の状態として報告する。配布前に必要ファイル、参照、組版、計算、ZIP整合性を確認する。

## 最優先の目標：公表する論文の価値と正確性

自然な比較関手と構造対象を明示し、先行研究と区別できる正確な中心結果を優先する。主張やページ数を増やすことを目的としない。現行稿は41ページ、主TeXと八つのsectionからなる。現在の中心は `four_hearts_boundary_data.tex` の右加群規約での辞書、正規化したmutation列、decupleの順逆復元である。

## 確定した正規化と到達点

VdB (5.4)と§10の右加群規約を固定し、境界の正shiftをS+(M)=σ_*(M⊗L0)とする。負の平面twistの実際のrestrictionはU1=L0^−1、U2=(L0L1)^−1、L1=σ*L0。blow-upのβとsection-modelの境界同型を使って同じ境界同定で運ぶと、このtupleは最終Orlov collectionでも保たれる（lem:plane-negative-twists、prop:transported-tuple）。

この指定構成のRains辞書は **q=L0/L1、L=L1** であり、可換avatarはL1による平面内の六点blow-upとなる（thm:right-dictionary）。VdBのσpiがL0一般位置という条件は、piがL1一般位置と同じである。full collectionのforward RHomと合成の境界比較により、構造対象・境界つきdg同値を得る。これだけからheartのt-exactnessは結論しない。境界作用だけで残っていたε∈E[3]の九候補は、初期平面twistをさらに固定するとε=Oに決まる。

右mutationはR_F^-E=Cone(E→RHom(E,F)^*⊗F)[−1]、左はshiftなしのconeと定義する。AOUの隣接交換順を使うが、R6^-R7^-R8^-の後の末尾三対象に[1]を明示的に施す。境界で負次数2線束のcoevalution coneが逆線束[−1]になるためである。このsheaf-normalized列で得るdecupleは

    (O, (L0L1)^−1(D6), L0^−1(D123);
     O(p1), O(p2), O(p3); L0(−p4), L0(−p5), L0(−p6)).

点が相異なるとき、そのadmissibilityは三条件 **O(D123)≠L0、O(D456)≠L1、O(D6)≠L0L1** と同値。固定E,σ,L0上では一般位置条件との共通部分は非空Zariski開である。そこではactual restriction条件(R)が成立し、このdecupleから構成したAS代数A+と指定Ψ+のpointed比較を得る。標準周期表示が右noetherianであれば、十一因子ΔはΨ+のt-exactnessを判定する。未変更の印刷decuple・同じラベルのAS代数への無条件な同一視はしていない。

逆に(O,A0,B0;K1,K2,K3;C1,C2,C3)から、O(pi)=Ki、L0=K1K2K3/B0、O(p3+j)=L0/Cj、L1=O(D6)/(L0A0)、q=L0/L1を一意に復元する（prop:inverse-decuple）。平行移動σそのものは[3]のfiberの九選択を持つ。これはdecupleだけからσを復元する曖昧さであり、σを既に固定した前記εの選択とは異なる。全moduli stackの九対一同型とは主張しない。

整数倍点pi=Ni a、q=P_a、L1=O(3o)、L0=L1q、3b=aとすれば、従来の共鳴族はこの正規化した共通領域に入る。三条件の比はq^(N1+N2+N3−1)、q^(N4+N5+N6)、q^(ΣNi−1)で全て非自明。これは全対応potentialのnoetherian性やΔ非零を保証するものではない。

## 原典の印刷式との関係と保持する成果

印刷されたtuple U1=L0^−2L1、U2=L0^−5L1³は別のshift S−(M)=L0⊗σ*Mの負twistから得られる。一方、S+の境界作用とそのtupleを同時に用いるとQ²=Q³=Oという不整合が出る。この検査と、原典全記号の正式な読み替え・訂正の確定は区別する。本稿は初期右加群規約と各transport、各cohomological shiftを明示して独立に構成したΨ+を扱う。著者による正式訂正の確認や未変更の印刷AS代数との同一視は未完了。

十一条件の純代数定理、Rains単独のgenuine gluingの導来比較、全heartの差の局在、Euler chamberと整列結果、同じ六点から得る720個の埋め込まれたRains heartsは保持する。これら全証明を今回新たに独立再査読したという意味ではない。今回の共同領域の構成は旧成果との接続を与えるが、全パラメータ・全heart・相対familyの分類を意味しない。

## 次の着手と成功条件

最優先は **正規化した実際のdecupleからpotentialを作り、十一因子の楕円パラメータ式とnoetherian適用域を確定すること**。右規約での辞書、εの選択、三つのactual admissibility条件は解決済みなので再び未決定としない。原典の変更されていない各記号への翻訳は別の確認課題として残す。

逆decuple辞書を用い、一般位置と三条件の開集合上でどの係数chartに入るかを明示する。特に整数倍点例のAS+がΔ非零となるかは、三条件だけから推測せず別計算する。その後、比較kernelの相対perfectness、基底変更、標識・heartの降下へ進む。対象の同型・pointed dg同値・t-exactnessを分ける。

Rains2025 monograph全文との網羅的新規性照合、外部独立査読、機械形式化、元の楕円生成元のアフィン表現係数は未完了。公表稿の主張は既知のVdB・AOU・Rainsの入力と追加的な正規化・辞書・heart選択の帰結を区別する。

## 再現と検証

    python3 computations/verify_cubic_heart_numerics.py
    python3 computations/verify_four_hearts.py
    python3 computations/verify_four_hearts_corner.py
    python3 computations/verify_four_hearts_chambers.py
    python3 computations/verify_four_hearts_sorted.py
    python3 computations/verify_four_hearts_boundary.py
    latexmk -lualatex -outdir=build papers/nc_del_pezzo_hearts.tex

Python標準ライブラリ、LuaLaTeX、LuaTeX-ja、tikz-cd、latexmkを使う。六コードを現行入力で実行した。境界コードは1587個のK0ベクトルに加え、325個のshift逆演算、符号付きrankを含むmutation列、[1]補正、逆decupleのround-trip、具体六点の720順序の三条件を検査する。実際の線束同型、full strong性、dg同値は計算の帰結ではなく本文と一次資料による。

全文41ページ・109ラベル・13文献。全文組版・画像点検・清浄ディレクトリでの再現・遠隔保存をvalidationで分けて記す。GitHub保存成功時にLibraryへ別途アップロードしない。
