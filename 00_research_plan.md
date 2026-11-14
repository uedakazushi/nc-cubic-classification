# 研究方針：内在的非可換三次曲面とambientの成分

2026-11-15 / project-v11 / recognition-v3。再開時は本書、`research/weak_cubic_axioms.md`、`papers/weak_cubic_axioms.tex`を先に読む。中心拡大型を進める際は`research/cubic_surface_comparison.md`と`research/r13_generic_moduli.md`、対応する既存論文も読む。

## I. 恒常的な研究原則・保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更は理由・達成済み・未解決の核心を現行方針として整理し、変更履歴を時系列に蓄積しない。

証明記載、今回の証明検討、計算確認、外部入力、追加仮定、未解決、予想、新規性の確認は別の状態として扱う。仮定・依存先・証明箇所を明示し、誤りは本文・要約・方針にも反映する。一次資料の適用範囲と書誌を確認する。日本語LuaLaTeXで公表価値のある結果を十分な証明とともに整理し、成果の数学的内容を削って軽量化しない。

研究継続bundleは現行方針・ノート・論文・ソース・PDF・必要なコード・小証明書と再現手順だけを含む。過去のZIP、旧稿、ログ、キャッシュ、重複を含めず、現行一式から再開できるようにする。既存の有効なsurface/R13/threefold研究は保持する。

ユーザーは区切りごとの承諾不要のLibrary保存を許可している。現行bundleをLibraryへ保存し、利用可能ならGitHub mainにも通常のfast-forwardで保存する。既存Library資産の削除は別操作であり無断で行わない。GitHub Actions・force push・不要なPRなし。PDF・コンパイル中間物はGit追跡しない。生成、証明検討、計算、組版、Library保存、GitHub保存を別々に確認する。

## II. 上位目標と認識範囲

対象は、gd2のk線形Abel圏Aとrank-one torsion-free構造対象O、s=S^{-1}[2]のheart保存、AZ ample、全整数mで可換三次曲面と同じh0により定義されるweakly marked nc cubic surfaceである。通常のnoetherian/Hom有限条件、rank/torsionの意味、族での相対SerreとHom底変更を明示する。

**全weak対象の認識と、R(1,3)中心拡大型の分枝の比較は別問題である。** 全公理と一次生成・二次三次関係を満たし、さらに全twistのExt1が消えても、ambientがR13成分の閉包に入らない量子Fermat例がある。全対象をR13一成分へ押し込める目標は採らない。全モジュライの認識・代数性・他成分を追う一方、R13分枝のAOU/Weyl比較を独立に進める。

任意周期、Frobenius適合周期、graded表示、directed関係、rolled-up potential、pointed圏を区別する。GL商とPGL商のスカラー慣性も揃える。Hilbert級数だけから二次包絡のAS性を結論しない。

## III. 新しい結果：四つの問い

新稿は`papers/weak_cubic_axioms.tex`、補足ノートは`research/weak_cubic_axioms.md`。

1. h0(O)=1からR0=kは自動。Serre双対はExt2(O,O(m))=R(-m-1)*とExt1の対称性を与えるが、Ext1の消滅はそれだけでは出ない。
2. 全次数有限自由な局所Artin変形では、一次生成と関係次数≤3は特殊ファイバーからNakayamaで持ち上がる。正則正規一次元tを持ち、R/(t)がこの提示を持つ場合もRの条件2が従う。中心性は不要。全公理から条件2を導く証明は未完成。
3. 二次包絡B、三次overlap K3についてdim B3=16+dim K3、新三次関係数=dim K3−3。一本の三次関係はdimK3=4に対応する。AS正則性にはさらに全Koszul複体の完全性が必要。
4. 量子Fermat反例：ζ³=1≠ζ、E=[[0,1,1,1],[-1,0,0,1],[-1,0,0,1],[-1,-1,-1,0]]、B=k<x_i>/(x_ix_j−ζ^{Eij}x_jx_i)、R=B/(Σx_i³)。BはCY4、Rは整域AS-Gorenstein index1。qgrRはgd2、Serre=(-1)[2]、AZ ampleと全切断数、rank1を満たす。Ext1(O,O(m))も全mで零。整域性は3次cyclic algebraのNorm障害、tails正則性はFermat chartの正則正規元による帰納で証明する。
5. このBのR13排除は、周期正規直線族の射影returnが恒等というproper閉incidenceで証明する。四つの独立基底変更に不変であり、単にZ(B)1=0という主張ではない。support classは{0},{1,2},{3}、四周returnはいずれも非スカラー。
6. 有限提示incidence P（J2 rank6、J3 rank45）と全Hilbert rank条件を構成。上界minorのイデアルはNoetherian性で有限生成なので、正しいHilbert値の点の完備化はframed環変形の有限型形式模型を与える。全weak stackの通常の代数性・局所有限型性は未証明。
7. AS4二次包絡と正則三次核を持つ認識部分には、全ncP3へのambient射がある。R13中心incidenceはP1束で、一般有理商の関数体はK(λ)。幾何学的一般切断がweakとなることは既存のvery-general正則切断の証明を入力とする。正確なweak fiberの除外集合と開性は未完成。

`computations/verify_quantum_fermat.py`は指数演算、CY行積、低次数中心、四周return、四次potentialの符号、QQ(ζ)上の64×48 overlap行列rank44、Hilbert値、Norm障害の単純極を厳密確認する。通常の証明と計算を区別する。新稿9ページを組版・描画確認済み。外部査読、形式化、新規性の網羅確認は未実施。

## IV. 保持する中心拡大型・potential研究

`papers/cubic_surface_ambient_moduli.tex`とそのinputs、`research/cubic_surface_comparison.md`は次の有効な研究を保持する。今回これら全証明を再監査したわけではない。

- 4周期付き関係式stackと任意周期付きAS Z代数は同値。ordinary potentialはFrobenius適合周期の部分。任意周期の可換反例との区別を保つ。
- Directed P3の二つのrank6関係R0,R1から、rank4の三次syzygy K=(R0⊗V2)∩(V0⊗R1)とV3=K*、coevKにより四次potentialを作る。縮約全射とKoszul/AS条件を課して両moduliを比較する。全Gr(6,16)^2ではない。
- R13の七係数slice、普遍四次potential、rank条件の全接行列rank188、軌道rank61、slice+軌道rank68から、射影成分67・有効商7の一般正則性とエタールchartを得る。境界の全AS性と正規化は未決定。
- 可換三次曲面近傍の形式AOU/W(E6)比較と、相対inverse Serreの有限低次数模型を保持する。全weak対象の大域Weyl商を意味しない。
- Poisson一意延長と8→7、固定ambientの中心P1・全normal形式fiber1を保持する。
- `research/r13_generic_moduli.md`は一般R13の19係数Aff3商、七係数Hessian216有限対応、8臨界点と可積分1形式を整理する。今回配布bundleにはその専門稿の全文も含めた。全境界の分類ではない。
- Threefold原稿`papers/nc_cubic_threefold_moduli.tex`と既存コードを保持する。surfaceとthreefoldの次元・障害・周期を混同しない。

## V. 次の優先課題

最初に公理から提示を認識する：Ext1消滅、反標準環のCohen–Macaulay性、正規一次切断、三次overlap rank4を別々に検討する。条件2のArtin安定性を大域開性に無断で昇格しない。

全モジュライの代数性は、全Hilbert関数・saturation・gd2・相対Serre・AZ ample・rank1の一様な有限型chartと全被覆を示すことが核心。有限提示や有限型形式hullだけを代数性の証明としない。

R13分枝では、AOU有限代数ΛとP0からinverse Serre orbitの低次数section環を相対計算する。W(E6)の代数的作用、マーキング存在・数値的一意性・降下、weak locusの開性、generic fibreの正確な除外点と慣性を調べる。

量子Fermat例のHH変形、数値K群、AOU型例外列の有無を計算し、R13以外の分枝を調べる。現在はR13閉包の外にあることだけを示しており、別成分の次元やrigidityを主張していない。

## VI. 再現

新計算：`python3 computations/verify_quantum_fermat.py`。
新稿：`latexmk papers/weak_cubic_axioms.tex`。
検証範囲：`research/weak_cubic_validation.json`。
従来のsurface/R13計算の手順はそれぞれの既存ノートとREADMEに保持する。新しいresearch bundleは現行の認識稿・中心分枝稿・一般R13稿・必要コードだけを含み、旧ZIPやコンパイル中間物を含めない。
