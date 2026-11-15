# 内在的非可換del Pezzo曲面と非可換三次三様体のモジュライ

2026-11-15 / v9（dP1統合）。まず[研究方針](00_research_plan.md)と[共通枠組み](research/common_del_pezzo_framework.md)を読む。次数1は[dP1方針](research/dp1_research_plan.md)、次数3は[weak cubicノート](research/weak_cubic_axioms.md)、三次三様体は[現行研究ノート](notes/research_notes.md)へ進む。GitHub mainを現行ソースの正本とする。

## 研究の構成

**次数1・dP1**：[内在的定義・10次元候補族・avatar](papers/nc_del_pezzo_degree1_moduli.tex)、[反標準qgr・共鳴と導来比較](papers/dp1_anticanonical_models.tex)、[現行方針](research/dp1_research_plan.md)、[研究ノート](research/dp1_research_notes.md)、[再現手順](research/dp1_reproduction.md)、[検証状態](research/dp1_validation.md)。反標準境界の特異点および全intrinsic abelian moduliへの成分性は未完成。旧ZIPやPDFはGitに収録しない。

**次数3・cubic surface**：[内在的公理と境界認識](papers/weak_cubic_axioms.tex)、[surfaceのambientとモジュライ](papers/cubic_surface_ambient_moduli.tex)、[研究ノート](research/weak_cubic_axioms.md)。量子Fermatの別分枝とR(1,3)の範囲を区別する。

**三次三様体**：[現行論文](papers/nc_cubic_threefold_moduli.tex)と従来の計算・原稿を維持。以下の「現在の結論」と再現コマンドは主に三次三様体の研究を述べる。全nc del Pezzoの分類を主張するものではない。

## 現在の結論

非可換cubicとambientの二つのモジュライを、まず相対Z-algebraのfpqc stackとして定義した。三次側のAから二次包絡Q(A)を取る自然な射があり、固定したambientへの厳密なファイバーは正規三次直線束族のincidence集合層である。全代数stackは有限窓の有限型商stackの2逆極限、incidenceは有限窓の準射影schemeの逆極限として記述できる。これを全体の有限型代数性と取り違えない。

圏による定義では豊富列を保持する。全対象の同定を保持する場合は厳密な代数同型と一致し、同定を弱めると頂点スカラーと相対線束による捩れが現れる。Q(A^L)=Q(A)^Lなので比較射はこれらの同値関係に両立する。相対category比較にはsaturation・Hom基底変換・相対復元を仮定する。可換ambientのfiberは非被約基底も含めP34であり、pointed categorical levelでは通常の[P34/PGL5]を回復する。

### 非可換P3の四頂点potential表示と三次側の比較

標準14641型の二次Koszul・左右AS正則Z-algebraは、Koszul双対のFrobenius traceで4周期を規格化すると、四頂点の4-CY代数になる。隣接頂点間に4本ずつの矢を取り、四重テンソルwから反巡回四次superpotential W=w−cw+c²w−c³wを作る。関係は長さ二の経路による微分で与える。

許容potentialをP255内のfpqc部分関手U4^ASとして定義すると、頂点スカラーを除いたpointed stackは[U4^AS/PGL4^4]と同値である。相対bar複体により、全成分が局所自由なAS族のKoszul双対とFrobenius対合は非被約基底でも任意の底変更と両立する。strictなZ-stackとはスカラー慣性が異なり、U4^ASの全体の有限型代数性は未証明。

同じ証明は標準N次元にも適用できる。特にambient P4のpointed stackは[U5^AS/PGL5^5]、U5^AS⊂P3124という五頂点の五次potential模型を持つ。可換点では五つの25×125 flatteningのscheme論的rank10条件が全Artin形式模型を与える。三次→ambientの二次包絡射はこの商へ写るが、三次イデアルを保つ周期の相対降下まで結論したものではない。

可換交代テンソルの形式近傍では、二つの16×16 flatteningのscheme論的rank6条件だけで全Artin基底上の平坦性・Koszul性・相対4-CY性が従う。線型化条件のrankは165、射影potential接空間は90、射影基底変更軌道は45、商の一次変形は45次元。数値は有理数上の厳密計算でも確認した。この接空間次元を成分次元とは解釈しない。

三次三様体A=B/(G)ではambient Bは5次元AS正則だが、Aはinjective dimension 4・AS index 2のAS Gorenstein代数で、global dimensionは無限。有限表示はambientの五次superpotentialと正規三次直線のincidenceである。滑らかな可換三次ではHH±1=k5なので通常の有限次元tilting代数では表せず、dg/A∞模型では残余圏を保持する。比較射の行き先は引き続き非可換P4である。

### 次数付き表示からZ-algebraへの比較

体上の正規三次対は1周期構造を持つが、その選択は一意とは限らない。周期を忘れる操作はPer_1(B)の共役商で記述され、Sierraの結果により一般のZhang twisting systemによる同一視に対応する。

本稿の一般Jacobian族では、二因子stabilizerの150×50整数行列に二つのスカラー核があり、48次minorがmod1000003で815096となる。したがって射影二因子stabilizerは有限で、Z-algebra同型による追加同一視も有限個である。さらに一般中心三次点では、全indexed normal incidenceの形式fiberが中心incidenceに一致し、固定ambient上の厳密fiberは4次元形式円板になる。

### 可換点の形式モジュライと像

可換P4では、Hom(O,O(1))の射影基底を付けたAbel/Z変形関手と規格化CY芽を、実際のQmod自然変換が全Artin基底上で同定する。証明は有限Beilinson窓のsliceとminimal hullの一意性を使い、接空間126の一致だけに依存しない。基底を忘れるとPGL5_1作用が残る。

Rat(1,1,3)の全Poisson接空間の整数証明書とPymの比較により得た37次元成分は、実際の射影基底付きAbel/Z形式モジュライの成分でもある。中心incidenceを可換ambient上の全fiberに沿って完備化した像の形式閉包は、この成分全体である。ここで像の余次元は0。一つの指定cubic点での完備化や全大域モジュライについて、同じ結論を無条件に主張していない。

| 対象・同値関係 | 一般の次元 |
| --- | ---: |
| 射影化したRat(1,1,3) | 36 |
| Poisson錐／対応する射影基底付き形式成分 | 37 |
| 中心三次直線incidence | 41 |
| ambientのPGL5一般有理商 | 13 |
| 三次対のPGL5一般有理商 | 17 |
| 一般中心三次点での全normal厳密fiberの形式次元 | 4 |

13/17次元の族ではZ同型による追加同一視が有限。GL5商stackの次元は共通Gm慣性により12/16。Poissonのスカラー射影化、頂点スカラー、周期忘却は別の操作である。

滑らかな可換cubic点では、明記した同次formality入力の下で局所環は17次元・接空間20次元。実際のambient射の接写像は核10・像10であり、一般点でのfiber4とは異なる。

**未解決**：全モジュライの有限型代数性と大域成分性、任意の非可換点での相対周期化と降下、豊富列を忘れた圏の認識、smooth proper三次部分の相対開性と支配性、独立なformality座標の全高次での互換性。新規性と優先権の全面調査も未完了。

17係数slice、分離型余次元15、可換cubic忘却核7、混合中心・相対Picard・偶数Veronese・固定剛体ambientの4係数族などの既存成果も現行論文に保持する。

## 主なファイル

- [内在的復元](papers/sections/intrinsic_cubic_reconstruction.tex)
- [二つのstackとnormal incidence](papers/sections/algebraic_moduli_foundations.tex)
- [豊富列付き圏との比較](papers/sections/categorical_moduli_comparison.tex)
- [四頂点potential・相対stack・可換点のrank模型](papers/sections/projective_three_space_potentials.tex)
- [非可換P3と三次三様体の比較](papers/sections/cubic_projective_three_comparison.tex)
- [potentialの符号・rank・接空間の証明書](computations/p3_potential_certificate.json)
- [周期忘却・有限同一視・全normal fiber](papers/sections/period_forgetting_moduli.tex)
- [可換点の全Artin比較・形式成分](papers/sections/formal_ambient_comparison.tex)
- [二因子stabilizer証明書](computations/two_factor_stabilizer_certificate.json)
- [Poisson接空間証明書](computations/rat113_tangent_certificate.json)
- [検証範囲](validation.json)

## 手動再現

    python3 scripts/verify.py
    python3 computations/verify_p3_potentials.py
    python3 computations/verify_two_factor_stabilizer.py
    python3 computations/verify_rat113_tangent.py
    python3 computations/independent/verify_generic17_slice.py
    python3 computations/independent/verify_generic17_center.py
    python3 computations/verify_split_codimension.py
    python3 computations/verify_central_pair_centers.py
    python3 computations/verify_central_pair_orbits.py
    python3 computations/verify_central_symmetry.py --output build/central_symmetry.json
    latexmk papers/nc_cubic_threefold_moduli.tex

Python3・SymPy、日本語LuaLaTeX・LuaTeX-ja・HaranoAji・latexmkを使う。potential・二因子stabilizer・Poisson接空間の厳密行列計算はPython標準ライブラリだけで動く。二因子コードは同じディレクトリのverify_rat113_tangent.pyを入力生成と小行列式の共通実装に使うため、両ファイルが必要。

生成物はbuild/に置き、PDF・SyncTeX・中間ファイル・キャッシュは追跡しない。VS Code LaTeX Workshopも同じ.latexmkrcを使う。GitHub Actionsは使用しない。生成、計算確認、証明監査、組版、保存を区別し、実施範囲をvalidation.jsonに記す。
