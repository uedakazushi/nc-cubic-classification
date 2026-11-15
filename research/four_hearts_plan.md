# 四つのheartの比較：研究方針

2026-11-16 / hearts-v21。この一式から再開する場合は本書を最初に読む。現行論文は `papers/nc_del_pezzo_hearts.tex`、補足知識は `research/heart_comparison.md`、検証状態は `research/four_hearts_validation.json`。リポジトリ全体の目標は `00_research_plan.md` にあり、本書はheart比較に対象を限定する。

## 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更は理由と元の目標の達成・未達成を簡潔に記し、現在有効な方針へ書き直す。時系列の変更記録を蓄積しない。

証明済み・追加仮定に依存・未完成・予想・計算的観察を分ける。仮定、既知入力、証明の所在、未解決箇所を明記し、原稿に証明があること、今回の点検、有限検算、外部独立査読を区別する。誤りが判明したら依存する本文・要約・方針を更新し、有用な反例や障害をノートに保持する。

公表用原稿は原則日本語LuaLaTeXとし、一次資料の仮定と適用範囲を確認する。未確認の文献内容を補わない。既知成果と本研究の組合せによる結果を区別し、網羅的新規性未確認を明記する。価値ある数学的内容と証明を軽量化のために削らない。

研究継続用bundleは現行方針・ノート・論文・再現に必要な最小限の原稿、PDF、文献情報、コードと小証明書から自己完結的にする。履歴、旧版、バックアップ、外部文献PDF、コンパイル中間物は含めない。必要な知識を会話だけに残さない。

研究区切りの承諾不要Library保存は一般に許可されている。ただし本研究ではユーザーのプロジェクト固有指示により **GitHub mainが正本であり、GitHub保存成功時にはLibraryへ保存しない。失敗時のみ緊急避難に使う**。既存Library資料は無断削除しない。mainへの通常の保存と遠隔確認を行い、force push・不要なPR・GitHub Actionsを使わない。共有mainの他の研究を損なわない。

生成・証明点検・数値検算・組版・保存を別々の状態として報告する。配布前に必要ファイル、参照、組版、計算、ZIP整合性を確認する。

## 最優先の目標：公表する論文の価値を最大化する

個々の未解決項目を順番に埋めることより、正確で独立した中心結果と、先行研究に対する明確な貢献を優先する。主張の数やページ数を目的としない。中心は自然関手の同定、反標準heartを選ぶ原理、実在する対象・表現への帰結である。現行稿は34ページ、主TeXと七つのsectionからなる。

## 現在の主要な到達点

VdB最後のsection-model関手は、同じ最終raw blow-upの構造対象と反Serre作用から作る自然な反標準導来切断に同定される。同じRains表示とAOU比較はこれにより接続する。標準noetherian三block表示のAS–反標準のt-exactnessは十八係数非零と十一因子Δの非零で判定する。独立な全avatarの同一視ではない。

指定genuine smooth楕円gluingでq非torsionなら、全heartのtorsionfree部分Fは境界非交叉有限長圏Zに含まれる。従って自然Φがt-exact、(e,s)がAZ-ample、全ての実在Z単純のχ(e,S)>0という三条件が同値となる（thm:globaldefect）。数値共鳴そのものとAZ失敗を同一視しない。

Zの全単純は有限個の2-spherical対象で、その根類は線形独立な有限ADE系となる。局所Euler-chamber手順は全Rains heartへ延長でき、負の単純を順次tiltして全反標準heartへ到達する（thm:globalADEtilts）。回数は初期負正根数。これは一回のHRS tiltを有限個の単純tiltに細分する記述で、任意のtilt列の最短性を主張してはいない。

整数倍点p_i=N_i q（3≤r≤8、相異なる正整数）では、各blowdown単純根にRainsの既知の実在結果を適用した。全有限次元単純A=R/(g−1)加群はr個で、Nを昇順νに並べると次元は(ν1+ν2+ν3,ν2−ν1,…,νr−ν_(r−1))。負単純tiltの回数は元の順序の逆転数であり、全heartが反標準heartと一致するのは昇順の場合だけである。同じ無順序点集合のr!順序は同じpointed導来圏内で相異なるRains heartsを与える（thm:sorted-spectrum、cor:permuted-hearts）。

六点(1,3,2,5,7,11)の全六根sheafの実在は、この具体的なblowdownとdeterminant条件で確認した既知結果の適用であり、追加の未検証仮定ではない。次元は(6,1,1,2,2,4)、characterは二つ、720個の順序heartのうち昇順のみ反標準heart。抽象的abel圏として720個が互いに非同値とは主張しない。

## 先行研究と主張の確実性

Rains 2022 §4 pp34–35は固定blowdownの単純根のq冪共鳴と有効性を記述する。Rains 2019 §11 p141、Proposition11.23の直前は、有効単純根そのものとdeterminant条件を満たすEuler標数に対する境界非交叉既約sheafの実在を明記する。今回の実在入力はこの記述であり、nefなfundamental chamberを仮定するProposition11.23自体を単純根に誤適用しない。

VdBの境界非交叉有限長性と単純数、BridgelandのADE反射、BCPWの単純tilt理論は先行結果である。本稿の追加帰結は、指定反標準関手の全heartの差の局在、Euler値による認識、実際の整数倍点族での整列公式に置く。数学的証明は内部点検済みだが、外部独立査読・機械形式化・網羅的新規性確認は未実施。Rains2025 monograph全文との照合も未完了。

## 次に着手する課題

最優先は、独立な楕円データ表示の辞書を、境界作用とgluingまで整合させること。AOU (9.47)とRains (4.13)の形式determinant辞書はノートに保持しているが、境界shiftの規約と途中のsection-model置換をまだ同定していない。同じ最終VdB表示での関手同定と、今回の具体的整数倍点族の実在・全heart判定を未解決として反復しない。

次に、十一因子を実際の楕円パラメータで書き、許容AS/noetherian領域との交わりと負指数根との対応を決める。整数倍点族は明示的な共鳴例であるが、全AS領域や全パラメータの壁を分類したものではない。r!個は順序から得るheartの数であり、同じ導来圏の全heart数ではない。

相対heart、基底変更と標識・kernelの降下、元の楕円生成元のアフィン作用係数は残る。論文の中心結果の独立点検とRains monographとの新規性照合を優先し、結果を増やすためだけの一般化は行わない。

## 再現と検証範囲

    python3 computations/verify_cubic_heart_numerics.py
    python3 computations/verify_four_hearts.py
    python3 computations/verify_four_hearts_corner.py
    python3 computations/verify_four_hearts_chambers.py
    python3 computations/verify_four_hearts_sorted.py
    latexmk -lualatex -outdir=build papers/nc_del_pezzo_hearts.tex

Python標準ライブラリ、LuaLaTeX、LuaTeX-ja、tikz-cd、latexmkを使う。新しい整列検算は六根系で240組の相異なる正整数を選び、Picard格子の明示根列挙とWeyl列挙を照合し、具体六点の全720順列を検査する。従来の576回のchamber手順、40,000通りのA2、六点普遍恒等式、具体cornerのQQ/有限体消去も再実行した。sheaf実在とt構造の証明は文献と本文によるもので、有限検算の帰結ではない。

組版・ページ画像・清浄ディレクトリでの再現・GitHub到達はvalidationに別々に記す。GitHub保存成功時にLibraryへアップロードしない。
