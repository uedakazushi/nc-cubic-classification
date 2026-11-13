# 非可換cubic threefoldの17次元モジュライ族

2026-11-13 / v1。主論文は `papers/nc_cubic_threefold_moduli.tex`。17次元の真の同型類族と、その適切なモジュライstackでの既約成分性を研究する。

41次元中心三次対incidence、17係数sliceと31次minor、分離型余次元15、忘却核7=6+1、混合中心と偏極付き復元、固定剛体ambientの四係数族、Artin局所構造を証明付きで保持する。可換点の次元/接空間は41/44、商sliceは17/20であり、滑らかな17次元moduliという主張ではない。

既約成分性・generic reducedness・全nc cubicの分類・無標識導来復元は未証明。ambientの最小周期がgcd(N,d)を割る定理と、商イデアルを保つ周期性も区別する。

```sh
latexmk papers/nc_cubic_threefold_moduli.tex
python3 scripts/verify.py
python3 computations/independent/verify_generic17_slice.py
python3 computations/verify_central_pair_centers.py
```

Python3とSymPy、日本語LuaLaTeX・LuaTeX-ja・HaranoAji・latexmkを使用。LaTeX Workshopはroot起点でbuild/へ出力する。PDF・SyncTeXは非追跡。Actions・force pushなし。主張記載・有限検算・全独立監査・新規性を区別する。
