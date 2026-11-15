# 研究方針：内在的非可換del Pezzo曲面と三次三様体のモジュライ

2026-11-15 / project-v14 / recognition-v5 / dp1-integration-v2。再開時は本書、`research/common_del_pezzo_framework.md`を読み、次数3は`research/weak_cubic_axioms.md`、次数1は`research/dp1_research_plan.md`に進む。各現行論文・研究ノートはその指示に従って読む。

## I. 恒常的原則と保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化する。方針は現時点で有効なものへ書き直し、変更履歴を蓄積しない。証明の記載、今回の検討、追加仮定、外部入力、計算、未完成、予想、新規性確認を区別する。誤りの影響は本文・要約・方針へ反映する。

一次資料の適用範囲を確認し、日本語LuaLaTeXで十分な証明を保持する。研究ノートは作業日誌ではなく有効な補足・障害・反例を整理する。軽量化では履歴、重複、中間物を除き、有効な数学や再現資産を削らない。

現行bundleには方針、ノート、論文ソースとPDF、必要コード・小証明書・再現手順を含め、旧会話や旧ZIPを再開の前提にしない。ユーザーは研究の区切りで承諾不要のLibrary保存を許可している。現行ソースをGitHub mainにも通常fast-forwardで保存する。既存Libraryファイルは無断削除しない。GitHub Actions・force push・不要なPRは禁止。GitではPDF・TeX中間物・キャッシュ・ZIPを追跡しない。生成、証明検討、計算、組版、Library、GitHubの状態を別々に確認する。

## II. 現在の目標と区別

上位目標は、次数1と3に共通するweakly marked非可換del Pezzo曲面の内在的rank、構造対象、反Serre偏極、AZ再構成、反標準環と幾何学的avatarのモジュライ理論を構築することである。異なる次数のHilbert関数、weighted/standard ambient、heartとdg圏、strong/weak markingを混同しない。共通枠組みは`research/common_del_pezzo_framework.md`、次数1固有の目標・証明状態・着手は`research/dp1_research_plan.md`に置く。論文は役割別に独立させ、現行の三次三様体論文と次数3の証明を削除しない。

次数3について対象は、gd2のk線形Abel圏Aとrank-one torsion-free対象O、s=S^{-1}[2]のheart保存、AZ ample、三次曲面と同じ全整数のh0で定義されるweakly marked nc cubic surface。通常のnoetherian/Hom有限条件、s不変のrank/torsion理論、相対Serre・Hom底変更を明示する。

全weak対象の認識と、R(1,3)中心拡大型の分枝の比較は別問題である。全公理と一次生成・二次三次関係・全twistのExt1消滅を満たす量子Fermat例のambientはR13閉包の外にある。従って全対象をR13一成分へ押し込めない。

固定ambientへの同定を保持した切断空間、ambient自己同型で割ったstack、ambientも変形する全モジュライの形式近傍も別。GL商/PGL商、任意周期/Frobenius適合周期、graded/Z代数/pointed圏の同値関係を揃える。

## 共通定義と量子Fermatの成分に関する新しい結論

dP1と共通のGabriel–Krull rank-one torsion-freeおよびexceptional構造対象Oを次数3にも採用した。例外性を要求しない旧条件はpre-weakと呼び、そこからExt1消滅が従うかは未解決。負次数の切断値はrank-one/Hilbert増大から従う。一次生成・二次三次提示・AS包絡は共通定義ではなく認識問題に置く。

量子Fermat BはPym L(1,1,1,1) CY skew-polynomial 3-torusの(a,b,c)=(ζ,ζ,1)であり、Pym L(1,1,2)のQ→u²Q平坦族の特殊点u=0でもある。従って二成分の交点に属するが、R(1,3)の閉包外（既存の四頂点閉incidence）。他成分との交差は未決定。四変数の対角中心Fermat三次を全係数非零で持つtorus点はT[3]の27点に限る。証明はrecognition-v5（papers/weak_cubic_axioms.tex）。

## III. 到達点と証明の所在

現行認識稿は `papers/weak_cubic_axioms.tex`（recognition-v5、16ページ）。

1. **標準正規境界からの認識（定理3.1）**：Rに左右正則正規一次元tがあり、R/(t)=S0/(g)、S0がnoetherianな3次元二次Koszul AS正則、gが正則正規d次元(d≥3)なら、Rは一次生成、Q(R)はnoetherian Koszul AS4で、R=Q(R)/(G)、Gは正則正規d次元。d=3では六二次関係＋一三次関係が結論となる。ambientのAS性や条件2を前提としていない。
2. **証明の核心**：中心化後、B=Q(R)の次数0,1,2はRと一致するのでtは低次数正則。Cassidy–SheltonのKoszul複雑度2の定理から全次数正則性が従う。LBSの正則一次拡大からAS4へ進み、I∩tB=tIとI/tI=(g)から三次核を持ち上げる。正規の場合はZhang twistで中心化。g,Gの直線が捩り自己同型に不変であることを使い、一般の正規元が任意twistで正規のままだとは主張しない。
3. **圏的帰結（系3.2）**：この境界を持つweak cubicは超曲面認識部分に属し、Ext1(O,O(m))=0、Oは例外対象。全weak対象がこの境界を持つかは未証明。境界S0は楕円Sklyaninに限定せず、量子多項式例も含む。
4. **有限PBW入力（§3.1）**：S0=T(W)/(U)、dimW=dimU=3、L=(U⊗W)∩(W⊗U)が一次元のとき、中心拡大は12個のα,β係数とBGの三条件で記述される。係数等式は最大6+3+1本だが独立性を仮定しない。全stackの代数性を結論するものではない。
5. **量子Fermat反例を保持（§§4–5）**：ζ³=1、B=k<t,x,y,z>のq行列は(0,1,1,1),(2,0,0,1),(2,0,0,1),(2,2,2,0)。R=B/(t³+x³+y³+z³)は整域、qgrはgd2、Serre=(-1)[2]。properな周期正規直線incidenceの四周returnでR13閉包から排除する。
6. **量子Fermat中心切断の開部分を完全分類（定理6.2）**：Z(B)3=kt³⊕k[x,y]3⊕kz³。U_F={At³+f(x,y)+Cz³ : AC disc(f)≠0}⊂P5。G=(Gm×GL2×Gm)/Gm_degによる商はBH54、H54=(μ3^4/μ3_diag)⋊S2、位数54。全切断は実際にFermat商とgraded同型なのでweak条件を満たす。全weak変形のrigidityや孤立成分とは主張しない。
7. **以前の認識結果を保持**：R0=k自動、条件2のArtin平坦変形での保持、任意の正規一次商を使う提示十分条件、三次overlap数値、有限型形式代数模型、超曲面認識部分のambient射。全stackの代数性・全weak fibreの開性は未完成。

新旧二つの検算を実行した。一般認識定理・軌道stackの同定は通常の証明であり、有限検算だけの結論ではない。独立査読・形式化・新規性の網羅的確認は未実施。

### 次数1（dP1）の独立した現行結果

`papers/nc_del_pezzo_degree1_moduli.tex`は、Gabriel–Krullによるrank、内在的定義、境界AS正則被覆を仮定したweighted sextic認識、可換dP1の普遍点からの10次元dg候補族、KS計算、補助的A∞表示空間の成分性、avatar/heartの復元問題を保持する。`papers/dp1_anticanonical_models.tex`は滑らかなgenuine del Pezzoと滑らかな楕円境界を仮定した共鳴・反標準qgrの導来比較を保持する。既存稿に証明を記載した結果であり、今回の統合を全証明の独立再検証や新規性確認とは呼ばない。全intrinsic abelian moduliでの10次元成分性と特異/非局所自由境界は未証明。Rainsの数値的non-amplenessの稠密性をAZ失敗や導来変化の稠密性へ読み替えない。詳細は`research/dp1_research_plan.md`、`research/dp1_research_notes.md`。

## IV. 次の着手方法

最優先は、内在的公理から標準正規一次境界の存在をどこまで導けるかである。まずR1の正規直線incidenceを構成し、反標準切断の商圏のgd1性、楕円型/退化型のHilbert数とSerre作用を調べる。正規切断が存在しない対象もあり得るので、定理3.1の仮定を全域で自明と扱わない。

次に、定理3.1とPBW三条件を相対化する。境界のKoszul解消とgの直線をベクトル束として保持し、t正則性・sectionの底変更・相対Serreの一様な条件を作る。有限型の境界付きchartを先に構成し、その後で境界を忘れる射と全被覆を検討する。有限型形式hullを全stack代数性へ昇格しない。

量子FermatではAC disc(f)=0の境界の正則性と、ambientも動くHochschild変形を調べる。BH54という固定ambient中心sectorの計算はHH2=0を意味しない。残余自然自己同型を除く規約なしにH54を裸のAbel圏の全自己同値群と呼ばない。

R13分枝ではAOUのfinite inverse-Serre計算、W(E6)マーキングの存在・数値的一意性・相対降下、weak locusの開性、P1 fibreの除外点を追う。量子Fermat反例の存在とこれらの中心分枝の結果は両立する。

### 次数1の優先課題

特異な反標準曲線と非局所自由gluingの境界における反標準qgrのderived比較とsingularityを最優先とする。その後、AZ heartとGabriel–Krull rankの認識、finite chartからpointed dg/abel moduliへの比較、weighted sexticの相対境界、weak marking忘却を扱う。一般次数への抽象化は、現在の次数1・3の正確な適用範囲を確保してから進める。

## V. 保持する現行研究

`papers/cubic_surface_ambient_moduli.tex`はsurfaceのPoisson一意延長、8→7、AOUの形式比較、四頂点potential成分と中心incidenceを保持する。配布bundleの`papers/r13_component_moduli.tex`は一般R13のAff3商、Hessian216対応、8臨界点と可積分1形式を保持する（GitHubでの対応資料は`research/r13_generic_moduli.md`）。今回これら全文と全コードは再監査していない。GitHubにはthreefoldの現行論文も保持し、surface専用bundleには重複収録しない。

## VI. 再現

`python3 computations/verify_boundary_fermat.py`、`python3 computations/verify_quantum_fermat.py`、`latexmk papers/weak_cubic_axioms.tex`。静的参照・全13ページ・ZIPを確認する。実施範囲とハッシュは`research/weak_cubic_validation.json`。旧版・ログ・キャッシュを新bundleへ収録しない。
