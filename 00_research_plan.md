# 研究方針：非可換del Pezzo曲面の内在的モジュライとheart比較

2026-11-15 / research-plan-v30 / resonance-hearts-v7。**再開時は本書を最初に読む。GitHub mainが唯一の正本。** 実行規則は `AGENTS.md`、H3の具体的な分類計画は `research/cubic_14641_codex_plan.md`。ここには現時点の目標・到達点・次の着手だけを置き、証明・計算は下記の現行原稿とノートを参照する。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化し、目標・方針・論文構成を柔軟に変更する。重要な変更の理由と元の目標の達成部分・残存部分を現行方針として整理し、変更履歴を蓄積しない。

証明済み、追加仮定に依存する結果、未完成、予想、計算的観察を区別する。主要な主張の仮定、既知入力、証明の所在、未解決箇所を明記し、原稿に証明があること、今回の点検、計算、独立査読を同一視しない。誤りは依存する本文・要約・方針にも反映し、有用な反例や障害は研究ノートへ整理する。

重要な文献は一次資料で仮定・適用範囲を確認する。未確認の内容や書誌を推測しない。公表用原稿は特に指定がなければ日本語LuaLaTeX、現在の成果を理解しやすい論理順に構成する。価値ある結果と必要な証明は削除せず保持する。研究ノートには現行論文にない有用な着想・例・障害・再取得困難な情報を残し、作業実況・旧版対応表・重複証明は収録しない。

研究継続用bundleは現行方針・研究ノート・公表用原稿と再現に必要な最小限の計算資産から自己完結的に再開できる一式とする。研究区切りの承諾不要Library保存は一般的に許可されているが、**本リポジトリはGitHub mainを正本とし、GitHub保存成功時にはLibraryに保存しない。失敗した場合だけ緊急避難に用いる。** Library既存資料は明示指示なしに削除しない。

旧ZIP・旧原稿・ログ・キャッシュ・入れ子のアーカイブは不要。GitでPDF/ZIP/TeX中間生成物を追跡せず、TeX、ノート、必要コード・入力・小証明書を保持する。再生成方法、依存関係、実行済みと未実行の検証を明記する。生成、検証、commit、リモート保存は別々に報告する。

通常のfast-forwardでmainへ保存し、遠隔への到達を確認する。force push、不要なPR、GitHub Actionsを使わない。共有mainの他の更新を保存し、競合時は内容を読み直して両立させる。研究実行中の約15分checkpointは終了条件ではなく、その後も実際の制約の範囲で研究を続ける。未設定の背景作業や自動再開は約束しない。

## II. 最上位の目標と完成条件

**最優先の大域目標は強いintrinsic定義の14641型非可換三次曲面H3の完全分類。** (A,O)はExt有限noetherian Abel圏、Serre、tau=S^−1[2]のheart保存、Gabriel–Krull rank-one torsion-free exceptional O、AZ amplenessと三次曲面のHilbert値を満たす。R=⊕Hom(O,tau^n O)は一次生成、その二次包絡B=Q(R)は左右noetherian quadratic Koszul AS4（14641）。外部ambient、埋込み、4周期同型は追加標識にしない。R=B/(G)、G∈B3正則正規は認識定理の結論であり追加公理でない。

全対象の被覆、全admissible切断、幾何学的同型群oidと慣性、既約成分・交叉・境界、Serre/heart/rank/AZ認識、相対開性・底変更・stack降下を達成基準とする。全AS4の先行完全分類を要求せず、正規三次incidenceとH3条件から包絡を絞る。1-periodic graded、Zhang twist、4-periodic Z-algebra、qgr同値を区別し、Pym六標準chartだけで全AS4被覆としない。

上位の別の構造目標は全次数のRains heart・VdB heart・AS heart・anticanonical heartの比較である。四名称は由来を示し、四つの相異なるheartの存在を意味しない。realization、指定導来同値、t-exactness、構造対象、反Serre、境界、rank、marking、族の降下を分離する。VdB literal blow-upとsection-model qgrを自動的に同一視しない。現在の共鳴課題はIV節から再開する。

## III. H3分類の現状と次の具体的着手

主原稿は `papers/weak_cubic_axioms.tex`、詳細は `research/cubic_14641_classification.md`、`notes/research_notes.md`、検証範囲は `research/cubic_classification_validation.json`。以下はこれらの現行成果を参照する要約であり、共鳴研究の更新時に全てを独立再監査したという意味ではない。

**固定PI4包絡の完全判定**：h=1、gamma^4=2、alpha=(−2,−2,0)、beta=(1,1,2)のD切断族で、中心特異値は13個だが非H3値は平方因子のない次数6式 b(D)=(D−Dstar)*P4(D)*Q1(D)の根に限る。他のDのaffine切断は大域次元2。`papers/sections/cubic_order4_local_orders.tex` はgrの最大性、中心正則列とbalanced local dualityによる対称双対、DVR標準形の非分岐性、A1二重被覆の指標多重度を使う。小次元表現のnorm・二中心点への分配・次数6式は厳密検算済み。D直線のH3条件は主開集合D(b)で、任意底変更・fpqc降下に適合し、そのaffine族は相対対角の長さ2以下の射影分解を持つ。これは一固定包絡の判定で、全位数4族・全H3の被覆ではない。

**滑らかな楕円境界部分（H3 classification-v36）**：中央境界では、次数3 translation THCRの全filtered deformationからCY AS4包絡と正則中心三次を復元し、全幾何学的矢をfiltered同型で記述した。有限Nのadmissibilityは中心McKay条件で完全判定し、被約固定N族ではH3開性・任意底変更・fpqc降下も得た。三捩れ量子Weyl chartの全中心と有限Hessian/character判定、j0 potential境界の非分裂例も保持する。

**非中央正規一次楕円境界**：共役位数は2または3に限る。位数2は量子involution（既存符号型）とClifford swapへ漏れなく被覆し、後者の三次は一本、中央volumeへの有限cocycle還元により長さ8 character完全交叉の被約性が必要十分。非skew・非CYの具体例を検算済み。位数3は最高Koszul tensorの8次元随伴模型と全Jordan型の計算から量子P2に限られ、全対象が既知の量子Fermat一対象、幾何学的群oidBH54となる。全H3が正規一次楕円境界を持つとは主張しない。

**次の核心**：Clifford swapの全intrinsic矢・相対stack、中央無限位数の全admissibility、正規一次楕円境界を持たないH3の漏れのない被覆を進める。全既約成分・交叉・境界と全intrinsic family降下は未完成。

既存の主要な構造結果を維持する：

- 全H3でmu_R=1、sigma_G=mu_B^−1。固定Bの候補は単一の140×20線型核W1。一般正規三次incidenceは35×8乗法行列の5次minor。CY包絡ならG中心だが非CY・非中心例も実在する。
- 全skew包絡部分の幾何学的対象は31座標パラメータ・五型で分類済み。可換、CY符号、非CY符号、3乗根中心一次、3乗根二重指標。一般同型類次元4,1,2,1,0。37候補のうちgeneric algebra=M3(K)となる6点はrank-one条件で除外。
- Pym L112/R22/S23の一般点、E3の非零変形を中心三次消滅で除外。as4からの検証済み構造結果により量子基底の全非自明unipotent持上げも除外。非零微分Ore包絡は点の自己Extが1,3,4,4,…で全特殊値を除外。CY交換子次元4以上と三交換子beta層の指定持上げも除外。固定SHA・規約は `research/as4_imports.json`。
- 良い楕円R13中心切断はaffine中心商の有限大域次元に帰着。分裂B=S[t]、低次中心(0,0,kg)ではlambda≠0が一軌道、慣性はmu3によるPAut(S)の中心拡大、lambda=0は除外。有限位数境界の固定包絡では悪い中心値は有限。
- 位数二Hesse–Cliffordの分裂全切断は中心曲面の滑らかさで判定。固定h=1の位数54商、全指定h族の一般四次元・位数648商を得る。比較群が倍増するh^6+20h^3−8=0も判定済み。非分裂対称ポテンシャルの二次項は平行移動で消え、全beta族はClifford rank1点の通常二重点のみを許す局所条件で分類。一般七次元の明示的群商、Dの混合補正と慣性を保持。
- gamma≠0への積分族は明示開集合上で全次数平坦・noetherian quadratic Koszul CY AS4。Rains中心元を規約変換した中心三次持上げを持ち、全pointed幾何学的矢はHesse216と一意の混合平行移動で記述。表示商の一般次元8、一般慣性自明、H3部分の慣性有限、非自明unipotent自己同型なし。超越的中心値のH3例もある。

これらを全H3の成分分類とは呼ばない。未被覆のPym特殊locus、低交換子CY、非スカラー共鳴、非対称・非CY包絡、j=0その他の境界、Z-algebraとの差と相対降下を縮小する。詳細な全式と証明は現行papers/sectionsにあり、本書で省略した係数等を削除してはいない。

## IV. Rains共鳴：現在の到達点と次の核心

現行原稿 `papers/nc_del_pezzo_resonance_hearts.tex`、ノート `research/resonance_hearts.md`、検証状態 `research/resonance_hearts_validation.json` を読む。新しい証明節は `papers/sections/resonance_mixed_a2_category.tex`。

**既存の確定結果**：実在する既約境界非交叉root sheafについてm=chi(e,M)と置くと全tau-orbitでh0=max(m,0)、h1=max(−m,0)、h2=0。正指数は有限次元A=R/(g−1)加群がdegree0、負指数は[-1]、零指数は自然Phiで消える。負指数ではRains heartのAZ amplenessが失敗するが、導来非同値やqgr特異化は導けない。Hilbert値は1+d n(n+1)/2で不変。genuine avatarでは零指数根共鳴なし。

全次数d=1,…,6で、固定楕円E・非torsion qの相異なる正整数倍p_i=N_iqによる全根数値共鳴がE^(9−d)に稠密。単純根指数の整数格子とE[3]の9選択で記述できる。最大共鳴の既約根sheafは単純根に限り一意、その直和のExtはADE zigzag。既知の形式性から固定dg圏のframed変形は辺積x_ij x_ji=0で決まり、cubic E6は32個の5次元分枝。全曲面モジュライの成分ではない。

**今回解決した核心**：q非torsion、H=−K nef、H²>0で境界外圏Zは有限長Serre部分圏となり、既約境界外root sheafは全heartの単純対象になる。指数p,−(p−1)の隣接根の非分裂拡大Pについて、e↠Pの核がline bundleとなることからconnecting mapのrankはp−1と証明した。具体的N=(1,3,2,5,7,11)、指数+2/−1では**rank δ=1**であり、全q導来同値は入力でない。

二根が生成するCはmod_fd Π(A2)に同値で、四つの直既約S+,S−,P,Qを持つ。cohomologyは(p,0),(0,p−1),(1,0),(p,p−1)、T=add(S+,P)、F=add(S−)が局所torsion pair。PhiはCの非零対象を消さない。内部Ext_Cは二周期的でありambientのExtと異なるので、Db(C)をambient導来部分圏と同一視しない。

**次の具体的着手**：p=2の0→W→V+→V−→0（両端一次元）について、Aの生成元のcharacter chi_W、chi_−と非対角項etaを求める。Phiが完全忠実ならcharacterは異なり拡大は非分裂、作用の像は全三角2×2行列代数でなければならない。Hom_A(V+,V−)の次元だけではJordan同一character型や異character分裂型を排除できない。対象の非消失と射の忠実性を区別する。実際の作用行列、全Z・全heartのtorsion pair、既存dP1全q導来比較の独立監査、相対モジュライは未解決。

## V. 他のheart/corner成果と継続課題

共通ノートは `research/heart_comparison.md`、原稿は `papers/nc_del_pezzo_hearts.tex`。振幅1の既知導来同値から(T,U)=(ker R¹δ_*,ker δ_*)、transported heart=〈U[1],T〉、t-exact iff U=0。pointedness・反Serre・標的AZと高次消滅の下で、周期1単純対象のEuler正負はT/Uを判定するが、非単純対象へ符号だけで拡張しない。ample orbitによるheart一意性には高次Ext tail消滅が必要。

Cubic cornerの主原稿は `papers/cubic_heart_corner.tex`、ノートは `research/cubic_corner.md`。18係数非零torusを四交比へ還元し、九つの2×2 minorとq・成分逆数行列の二つのdeterminant、計11条件が有限cornerの必要十分条件。六点復元により標識付き可換cubicの一般位置配置空間と同型。全一般位置でC7=0、C6に8次元以上残り、7が最良の一様消滅次数。Hilbert関数は8+21t+33t²+38t³+33t⁴+21t⁵+8t⁶、総次元162で、底変更と可換する有限平坦代数族を得る。道長gradingと反標準cut gradingを区別する。

11根壁では古典的(-2)曲線のi_*O(−1)が反標準導来切断で消える。一般の一壁の節点三次を含め証明・検算は `cubic_corner_root_walls.tex` に保持する。非可換Rains/VdB/AS壁上のheart存在やAS locus交叉へ無条件に拡張しない。

次はAOUの実際のmutationでE0≃πFを確認し、AS corner同値とqgr F比較を接続する。AOU Theorem9.4の左辺はqgr Fでraw blow-upのabel同値ではない。VdB最後のker δ_6*とR¹δ_6*を同じ楕円六点データで実在対象に対して計算する。有限位数・特異楕円境界・非局所自由gluingではgrading、noetherian性、realization、標識降下を再確認する。

## VI. 維持する並行成果と参照先

次数3の共通公理・境界認識は `papers/weak_cubic_axioms.tex` と `research/weak_cubic_axioms.md`。hdim=2はSerreから従う。exceptionalityなしのpre-weakからExt¹(O,O)=0、全weak対象の正規境界存在は未証明。PBW12係数・三条件、Artin平坦変形の提示保持、有限型形式模型を保持する。

量子Fermatはintrinsic H3の例だがOU AS型ではない。`papers/quantum_fermat_not_as_surface.tex` は離散torsion付きFermat商stackからHH_{−1}=HH_1=2、HH_0=5を計算する。ambientはPym L1111とL112の交点で、全対象がR13に入るという主張を排除する。曲面圏のOU障害とambient成分帰属は別問題。`papers/cubic_surface_ambient_moduli.tex`、`research/r13_generic_moduli.md` にR13の8→7、Poisson持上げ、中心incidence、Hessian商、AOU形式比較などの詳細を保持する。

次数1は `papers/nc_del_pezzo_degree1_moduli.tex`、`papers/dp1_anticanonical_models.tex`、`research/dp1_research_plan.md`。内在的rank、条件付きweighted sextic認識、10次元dg候補族、KS、補助A∞表示成分、avatar復元を保持する。全intrinsic abelian成分性と特異/非局所自由境界は未完成。全q導来同値の原稿上の主張を今回監査済みとはしない。

三次三様体は `papers/nc_cubic_threefold_moduli.tex`、`notes/research_notes.md` と各sectionに保持する。相対Z-algebra fpqc stack、二次包絡と正規三次incidence、有限窓、周期忘却、形式成分を扱う。Rat(1,1,3)の非射影化Poisson/形式ambient37、中心対41、一般PGL商13/17、忘却fiber4と、全大域stackの代数性・成分性を区別する。可換cubic点の局所次元17・接空間20・ambient接写像の核10像10は一般fiber4と別。17係数slice、分離型余次元15、可換cubic忘却核7、混合中心、相対Picard、偶数Veronese等の既存全文・証明・計算を維持する。

## VII. 再現と検証状態

共鳴の新しい有限検算：`python3 computations/verify_resonance_mixed_a2.py`。有理数でHom/Euler/Ext表、4375通りのcohomology、三角作用の四模型を実行済み。新証明節の独立LuaLaTeX driverは5ページで組版・ページ画像確認済み。**主原稿全体の組版、旧共鳴四スクリプトの再実行、実際の楕円A作用行列計算は今回未実施。** 状態の詳細は `research/resonance_hearts_validation.json`。

主原稿の再生成は `latexmk papers/nc_del_pezzo_resonance_hearts.tex`。旧共鳴検算は `verify_resonance_hearts.py`、`verify_resonance_extensions.py`、`verify_resonance_maximal_a2.py`、`verify_resonance_zigzag.py`。cubic cornerは `research/cubic_corner_validation.json` と同ノートの再現手順、H3は `research/cubic_surface_reproduce.md` と現行分類validation、次数1・三次三様体は各現行ノートを参照する。Python3（必要箇所はSymPy）、LuaLaTeX・LuaTeX-ja・latexmkを使い、生成PDFはGit追跡しない。数学的証明、有限検算、文献入力、独立査読を区別する。
