# 三次曲面研究の再現

2026-11-15 / surface-v2。最初に `00_research_plan.md` を読む。

必要環境はPython3、SymPy1.14.0、日本語LuaLaTeX（LuaTeX-ja、HaranoAji）、latexmk。計算はネットワークや外部データを使わない。リポジトリまたはsurface bundleのrootから実行する。

```sh
python3 -m pip install -r requirements-surface.txt
python3 computations/verify_surface_incidence.py
python3 computations/verify_r13_potential.py
latexmk papers/cubic_surface_ambient_moduli.tex
python3 scripts/verify_surface_bundle.py
```

二つの計算はQQ上で行い、JSON証明書を所定パスへ再生成する。potential側は数分程度かかり得る。`--quick`はminor一覧を出さないので完全再現の代用にしない。証明書には行・列番号と非零行列式を保存し、容易に再生成できる巨大行列そのものは保存しない。

PDFの出力先はbuild/。GitではPDFを追跡しないが、Library用bundleには組版済みの現行PDF一つを含める。旧版・ログ・aux・cache・外部文献PDFは含めない。surface bundleは三次曲面とR13比較を自己完結的に再開できる。別の三次三様体研究のソースはGitHubで保持されるが、このsurface稿の組版・検証には不要。

検証コードは有限線型代数を証明し、本文の全次数AS性、Artinの圏比較、markingの降下を計算だけで証明するものではない。後者の通常証明と一次資料の適用条件は本文にある。global weak=Weyl quotient、全認識定理、七係数atlasの一般次数、コンパクト化境界は未解決。
