# 非可換三次超曲面の内在的モジュライ

2026-11-13 / v6。最初に[研究方針](00_research_plan.md)、次に[研究ノート](notes/research_notes.md)を読む。主論文は[nc_cubic_threefold_moduli.tex](papers/nc_cubic_threefold_moduli.tex)。GitHub mainを正本とする。

## 何が分かったか

豊富列付きAbel圏のsection Z-algebraから、長さ二の合成核だけでambientを一意に復元する。相対平坦性・基底変換の条件下ではモジュライ群oidの射となる。一般のZ-algebraを扱う定義と、既に次数シフトを選んだ1周期的定義を区別する。

既存17次元中心三次族では、同じambient上の三次方程式に4次元の自由度があるため、ambient像の一般有理商は13次元。poisson-p4の三次incidenceに対応するRat(1,1,3)錐の全Poisson接空間が37次元であることを新しい整数行列証明書で示し、一般点で滑らかな成分であると証明した。Pymの局所比較を通じ、可換点の規格化CY変形芽の対応成分にも一般被約性が移る。中心三次incidenceは一般P^4ファイバーでこの成分を支配し、この範囲で像の余次元は0。

| 対象・同値関係 | 一般の次元 |
| --- | ---: |
| Poisson構造をスカラーで射影化したRat(1,1,3) | 36 |
| スカラーを保持したPoisson錐／標識付きCY変形成分 | 37 |
| 中心三次直線を加えたincidence | 41 |
| PGL5によるambientの一般有理商 | 13 |
| PGL5による中心三次対の一般有理商 | 17 |
| ambientへの忘却の一般ファイバー | 4 |

GL5商stackは共通スカラーGmの安定化群を持ち、stack次元は12/16。13/17はPGL5で剛体化した記述・一般有理商の規約である。

正規三次イデアルを保つ1周期化も、体上で証明した。正規族から作る3頂点orbit代数の中心元をNakayama自己同型が固定するため、イデアルを保つ5周期を得て3周期と合成できる。一般にはAS index Nと正規次数dのgcd周期を得る。仮定は左右global dimensionとuniformなAS Ext条件として本文に明記する。得られる通常の次数付き表示は正規三次商であり、中心三次商であるとは限らない。

**未解決**：全AS正則Z-algebraの大域的代数的モジュライとそこでの成分性、豊富列を忘れた圏の復元、周期構造の族への降下・一意性・中心化、全族上の滑らかなtailsの開性。中心商の平坦性だけを滑らかさと呼ばない。原稿の全Artin比較の適用範囲も明示する。

17係数sliceと31次minor、分離型余次元15、可換cubicへの忘却核7、混合中心・相対Picard・偶数Veronese・固定剛体ambientの4係数族は現行論文に保持する。一次資料の新規性・優先権の全面調査は未完了。

## 手動再現

    python3 scripts/verify.py
    python3 computations/verify_rat113_tangent.py
    python3 computations/independent/verify_generic17_slice.py
    python3 computations/independent/verify_generic17_center.py
    python3 computations/verify_split_codimension.py
    python3 computations/verify_central_pair_centers.py
    python3 computations/verify_central_pair_orbits.py
    python3 computations/verify_central_symmetry.py --output build/central_symmetry.json
    latexmk papers/nc_cubic_threefold_moduli.tex

Python3・SymPy、日本語LuaLaTeX・LuaTeX-ja・HaranoAji・latexmkを使う。新しいRat113計算はPython標準ライブラリだけで動く。生成物はbuild/へ出力し、PDF・SyncTeX・中間ファイルは追跡しない。VS Code LaTeX Workshopも同じ設定を使う。GitHub Actionsは使用しない。

新しい小証明書は[rat113_tangent_certificate.json](computations/rat113_tangent_certificate.json)。非零minorの合同式で特性零の下界を証明し、整数上の積零で上界を証明する。有限体の零を特性零の恒等式と扱っていない。組版・今回の検算・数学的監査の限界は[validation.json](validation.json)に記載する。
