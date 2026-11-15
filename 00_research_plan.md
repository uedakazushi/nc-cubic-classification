# 研究方針：非可換del Pezzo曲面の内在的モジュライとheart比較

2026-11-16 / research-plan-v31 / resonance-hearts-v8。**再開時は本書を最初に読む。GitHub mainが唯一の正本。** 実行規則は `AGENTS.md`、H3の具体的な分類計画は `research/cubic_14641_codex_plan.md`。ここには現時点の目標・到達点・次の着手だけを置き、証明・計算は下記の現行原稿とノートを参照する。

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

**滑らかな正規楕円境界の外の実例**：q³1のq-so3包絡のCasimir切断で、全H3判定(D−f)(3D+f)≠0を得た。中心はFricke cubic、無限遠triangleはterminal order、許容対象はどの正規一次境界でもsmooth elliptic THCRを持たない。これによりmissing-boundaryの実在部分を一つ完全判定した。全intrinsic矢はD不変・慣性A4、相対表示stackはgood Dline×BA4。一般qでも全切断の忠実差分模型と整域性、全候補矢[Q/S4]を得た（classification-v47）。非捩れまたは位数>3では全H3候補がこのpencilに限る。奇数位数N>=3では全中心Fricke式と任意次元の二種の三重対角既約表現から、H3 iff(D−D+)(D−D−)!=0を証明した（classification-v50）。全N−1内部特異値もMcKay条件を満たす。偶数位数も半Chebyshev正規元のweight分解から全端点を排除し、全有限位数qでH3 iffD!=D±を完全判定した（classification-v54）。粗座標theta=q+q^-1,w=−theta−h³D/q²、固定N表示stackはphi(N)/2個の(A1_w minus{+-2})×BA4。全中心形成は任意底変更と可換。これら全族は正規smoothE境界を持たず候補平面に稠密。非捩れqでもGWA反転固定環へのOre局所化から二端点の非H3性を証明した（classification-v55）。端点以外はこのOre開集合gl<=2。三頂点の形式的模型は全qでgl2、非捩れで完備量子平面と証明したがqgr降下は未完。さらに全標数0代数閉体上のproper楕円四次元Sklyanin（n∞又はn!=1,2,4）を全排除した：唯一の中心三次残余n3もdimZ3=dimS1=4により射影norm P3->P3が全射、全Gが一次式×二次式でnondomain（classification-v58）。一般にCY・PI3・normal-centre-finiteのH3包絡はdimZ3>=5が必要。さらに三乗根の固定量子so3包絡はpencilだけでなく全P4中心三次を完全判定した（classification-v60）。Delta=alpha³+27beta gamma delta!=0かつ五節点cubic3foldのdual外が必要十分。全表示stack[U/A4]はDM4、慣性1/C2/C3/A4、全中心basechangeと表示族降下。さらに指定qso3正常形の中心incidenceはp(q)(beta,gamma,delta)=0、dim2水平とdim4垂直がdim1で交叉する。固定Bのmissing smoothE locusは既約normal-crossing divisor、全点がsmoothE H3の特殊化。粗tetrahedral商・境界正規化も明示した（classification-v61）。一般Zhang twistも縮小した（classification-v63）：twisted-skewのH3はskewに戻る。非退化中央quadric pencilを持つproper Sklyaninの全自己同型Zhangtwistと標準V4cocycle twistは全排除。cocycle centre3はn3/6のみdim1で必ず一次×二次。Stafford三族と標準cocycle・循環変種も全T/全許容dで全排除した（classification-v68）。通常W1はL=alpha beta+alpha+3beta−1=0でだけdim2、全pencilがdegree3因子写像で分解。CY cocycleのcentre3は四つの互いに素な明示曲線でのみdim1となり全て分解する。sigmaの全T第三反復で特殊chartの欠落も除いた。さらにas4低交換子一覧の二重被覆二族を正規四次の符号反転で全排除し、長さ四/3+1の三固定表示もcentre3 rank20で独立排除した（classification-v69）。全CY被覆は輸入せず表示だけを参照。TT22の六表示も全排除した（classification-v70）：C_rは全qのPBW/忠実量子トーラスと三乗根norm全射、E/Fは正規bdの半単純部分−I、三固定表示はcentre3 rank20。AS4/CY全被覆は輸入せず具体表示と独立恒等式のみ使用。DS211の二パラメータAと例外Bも全排除した（classification-v71）：正規bの単冪作用でcentre3を量子3平面へ戻して残余純三乗を排除し、Bはnormal c³dの半単純部分−Iを使う。DS3のT/Uと固定表示も全値rank coverで排除し、V_hは平方根被覆の忠実トーラスと唯一のh1/48のnorm全射で排除した（classification-v72）。これでDS3/DT1の全列挙表示を排除。四単純基点FS4の全S(lambda,t)と標準Klein cocycleも排除した（classification-v73）。proper部分は既証Sklyaninへ帰着、三つの退化曲線はS(1,-1,s)の正規二次N1=a²+d²,N2=b²−c²の積が−Iを実現するため奇数centre0。FZ2のQ共有係数族は六対とも可逆skew係数なので既存skew分類に含まれる。表示のみ参照し全四単純基点/全CY被覆は未輸入。共有頂点係数零の残余O/H表示も全排除した（classification-v74）。Oは四DiamondのPBWと正規a,bのcharacterにより中心三次がc³又はd³一本に限られる。正確な共鳴はlambda=-1/2,A²=-3/64でkc³、A²=-1/192でkd³、他0なので全切断分解。H0/H1は分母なし商座標と最大minor16384lambda^12(lambda+1)^9(2lambda+1)^4(4lambda+1)(4lambda+3)、三例外値のQQ rank20で全中心三次零。最高反巡回tensorからAS4仮定下mu=id。従ってFZ2/FZ4/FZ5/FS4列挙はskew部分だけが残る。全CY/四単純基点被覆は未輸入。次は共有頂点非零full-sharedの具体表示を調べる。

**次の核心**：Clifford swapは境界一意性と全intrinsic矢を有限係数式で得て、一般次元2・一般慣性mu2×mu2を確定した。許容条件は明示四次式Delta_h(b,c)≠0（固定hで四つのbad方向）。この表示族は分離既約DMstack2へrigidifyできる。偶Veronese全中心はcubic scroll F1で、局所自由階数4の極大quaternion orderとなり、二本の滑らかな有理分岐曲線が四点横断する。次は抽象intrinsic family比較、中央無限位数の全admissibilityと、正規一次楕円境界を持たないH3の漏れのない被覆を進める。全既約成分・交叉・境界と全intrinsic family降下は未完成。

既存の主要な構造結果を維持する：

- 全H3でmu_R=1、sigma_G=mu_B^−1。固定Bの候補は単一の140×20線型核W1。一般正規三次incidenceは35×8乗法行列の5次minor。CY包絡ならG中心だが非CY・非中心例も実在する。
- 全skew包絡部分の幾何学的対象は31座標パラメータ・五型で分類済み。可換、CY符号、非CY符号、3乗根中心一次、3乗根二重指標。一般同型類次元4,1,2,1,0。37候補のうちgeneric algebra=M3(K)となる6点はrank-one条件で除外。
- Pym L112/R22/S23の一般点、E3の非零変形を中心三次消滅で除外。as4からの検証済み構造結果により量子基底の全非自明unipotent持上げも除外。非零微分Ore包絡は点の自己Extが1,3,4,4,…で全特殊値を除外。CY交換子次元4以上と三交換子beta層の指定持上げも除外。固定SHA・規約は `research/as4_imports.json`。
- 良い楕円R13中心切断はaffine中心商の有限大域次元に帰着。分裂B=S[t]、低次中心(0,0,kg)ではlambda≠0が一軌道、慣性はmu3によるPAut(S)の中心拡大、lambda=0は除外。有限位数境界の固定包絡では悪い中心値は有限。
- 位数二Hesse–Cliffordの分裂全切断は中心曲面の滑らかさで判定。固定h=1の位数54商、全指定h族の一般四次元・位数648商を得る。比較群が倍増するh^6+20h^3−8=0も判定済み。非分裂対称ポテンシャルの二次項は平行移動で消え、全beta族はClifford rank1点の通常二重点のみを許す局所条件で分類。一般七次元の明示的群商、Dの混合補正と慣性を保持。
- gamma≠0への積分族は明示開集合上で全次数平坦・noetherian quadratic Koszul CY AS4。Rains中心元を規約変換した中心三次持上げを持ち、全pointed幾何学的矢はHesse216と一意の混合平行移動で記述。表示商の一般次元8、一般慣性自明、H3部分の慣性有限、非自明unipotent自己同型なし。超越的中心値のH3例もある。

これらを全H3の成分分類とは呼ばない。未被覆のPym特殊locus、低交換子CY、非スカラー共鳴、非対称・非CY包絡、j=0その他の境界、Z-algebraとの差と相対降下を縮小する。詳細な全式と証明は現行papers/sectionsにあり、本書で省略した係数等を削除してはいない。

## IV. Rains共鳴：現在の到達点と次の核心

現行原稿 `papers/nc_del_pezzo_resonance_hearts.tex`、ノート `research/resonance_hearts.md`、検証状態 `research/resonance_hearts_validation.json` を読む。現在の中心証明は `papers/sections/resonance_mixed_a2_category.tex` と `papers/sections/resonance_global_heart.tex`。

**符号別Extと最大数値共鳴**：実在する既約境界非交叉root sheafについてm=chi(e,M)と置くと全tau-orbitでh0=max(m,0)、h1=max(−m,0)、h2=0。負指数はRains heartのAZ失敗を検出し、反標準側では有限次元A=R/(g−1)加群[-1]へ移る。Hilbert値1+d n(n+1)/2は不変。genuine avatarでは零指数根共鳴なし。全次数1–6で全根数値共鳴の稠密配置を整数格子とE[3]の9選択で記述し、既約根sheafの直和のExtをADE zigzagと同定した。固定dg圏のframed変形のcubic E6における32個の5次元分枝は、曲面モジュライの成分ではない。

**任意正負指数の局所完全判定**：q非torsion、Hnef、H²>0では境界外Zは有限長Serre部分圏。指数p,−nの隣接根の非分裂拡大Pのconnecting rankはmin(p,n)、cohomologyは((p−n)+,(n−p)+)。二根部分圏C≃mod_fd Π(A2)の全対象のcohomologyは、quiverの頂点次元a,bと一方の矢のrank tから(pa−min(p,n)t,nb−min(p,n)t)で決まる。p>nとp<nの両torsion pairを得る。p=nならPが消えるがgenuine avatarではこの同時共鳴自体が不可能。kernel e→Pがline bundleになるのはp−n=1だけであり、一般証明はrank-one torsion-freeのまま行う。

**指定楕円gluingの導来比較と全heart**：genuine smooth classical del Pezzo Sとsmooth E、q∈Pic0(E)からのRains gluingについて、既存dP1原稿のorbitのInd生成・境界traceの非零性・両位数の環の有限性・source飽和性を一次資料と照合した。自然Φは全qでDb(Rains)≃Db(qgr R)。この範囲で全Rains heartの振幅が[0,1]となり、T=ker H1Φ、F=ker H0Φによる一回のHRS tiltが反標準heartである。q非torsionではZにも制限し、T∩Z=ker Ext1(e,−)、F∩Z=ker Hom(e,−)。全任意nc曲面・weak avatar・特異境界への主張ではない。

**具体的混合A2のアフィン商**：指数+2/−1では0→W→V→U→0（次元1,2,1）は非分裂でW≄U、作用像は全三角2×2行列代数。逆向き非分裂拡大V'も存在し、A/Ann(V⊕V')≃Π(A2)という四次元商を得る。新しい二単純の根はalpha+beta,−beta、指数は1,1で局所Weyl反射に対応する。商はhomological epimorphismでない。内部Ext_Πの二周期性とambient Ext>2消滅を混同しない。

**残る具体的着手**：楕円データからAの生成元を固定し、上の四次元商への像を係数式で求める。character分離・非分裂性の真偽と指定gluingの導来同値は解決済みとして扱い、未計算のchi_W(a),chi_U(a),eta(a)と区別する。次に全E6境界外圏のアフィン作用、VdB/AS heartとの指定対象の照合、相対familyと特異/weak境界を調べる。大域H3の未被覆分類はIII節のまま維持する。

## V. 他のheart/corner成果と継続課題

共通ノートは `research/heart_comparison.md`、原稿は `papers/nc_del_pezzo_hearts.tex`。振幅1の既知導来同値から(T,U)=(ker R¹δ_*,ker δ_*)、transported heart=〈U[1],T〉、t-exact iff U=0。pointedness・反Serre・標的AZと高次消滅の下で、周期1単純対象のEuler正負はT/Uを判定するが、非単純対象へ符号だけで拡張しない。ample orbitによるheart一意性には高次Ext tail消滅が必要。

Cubic cornerの主原稿は `papers/cubic_heart_corner.tex`、ノートは `research/cubic_corner.md`。18係数非零torusを四交比へ還元し、九つの2×2 minorとq・成分逆数行列の二つのdeterminant、計11条件が有限cornerの必要十分条件。六点復元により標識付き可換cubicの一般位置配置空間と同型。全一般位置でC7=0、C6に8次元以上残り、7が最良の一様消滅次数。Hilbert関数は8+21t+33t²+38t³+33t⁴+21t⁵+8t⁶、総次元162で、底変更と可換する有限平坦代数族を得る。道長gradingと反標準cut gradingを区別する。

11根壁では古典的(-2)曲線のi_*O(−1)が反標準導来切断で消える。一般の一壁の節点三次を含め証明・検算は `cubic_corner_root_walls.tex` に保持する。非可換Rains/VdB/AS壁上のheart存在やAS locus交叉へ無条件に拡張しない。

次はAOUの実際のmutationでE0≃πFを確認し、AS corner同値とqgr F比較を接続する。AOU Theorem9.4の左辺はqgr Fでraw blow-upのabel同値ではない。VdB最後のker δ_6*とR¹δ_6*を同じ楕円六点データで実在対象に対して計算する。有限位数・特異楕円境界・非局所自由gluingではgrading、noetherian性、realization、標識降下を再確認する。

## VI. 維持する並行成果と参照先

次数3の共通公理・境界認識は `papers/weak_cubic_axioms.tex` と `research/weak_cubic_axioms.md`。hdim=2はSerreから従う。exceptionalityなしのpre-weakからExt¹(O,O)=0、全weak対象の正規境界存在は未証明。PBW12係数・三条件、Artin平坦変形の提示保持、有限型形式模型を保持する。

量子Fermatはintrinsic H3の例だがOU AS型ではない。`papers/quantum_fermat_not_as_surface.tex` は離散torsion付きFermat商stackからHH_{−1}=HH_1=2、HH_0=5を計算する。ambientはPym L1111とL112の交点で、全対象がR13に入るという主張を排除する。曲面圏のOU障害とambient成分帰属は別問題。`papers/cubic_surface_ambient_moduli.tex`、`research/r13_generic_moduli.md` にR13の8→7、Poisson持上げ、中心incidence、Hessian商、AOU形式比較などの詳細を保持する。

次数1は `papers/nc_del_pezzo_degree1_moduli.tex`、`papers/dp1_anticanonical_models.tex`、`research/dp1_research_plan.md`。内在的rank、条件付きweighted sextic認識、10次元dg候補族、KS、補助A∞表示成分、avatar復元を保持する。全intrinsic abelian成分性と特異/非局所自由境界は未完成。genuine smooth楕円gluingの全q導来比較は今回その証明と主要引用を点検したが、他の次数1の主張を一括して再検証したわけではない。

三次三様体は `papers/nc_cubic_threefold_moduli.tex`、`notes/research_notes.md` と各sectionに保持する。相対Z-algebra fpqc stack、二次包絡と正規三次incidence、有限窓、周期忘却、形式成分を扱う。Rat(1,1,3)の非射影化Poisson/形式ambient37、中心対41、一般PGL商13/17、忘却fiber4と、全大域stackの代数性・成分性を区別する。可換cubic点の局所次元17・接空間20・ambient接写像の核10像10は一般fiber4と別。17係数slice、分離型余次元15、可換cubic忘却核7、混合中心、相対Picard、偶数Veronese等の既存全文・証明・計算を維持する。

## VII. 再現と検証状態

共鳴の有限検算：`python3 computations/verify_resonance_mixed_a2.py`。p,n=1,…,8と直既約重複度0,…,4の40,000通りのcohomology、両chamber、balanced仮想場合、四次元商の積・両三角像・commutant・局所Weyl反射を厳密有理数演算で確認した。更新した二証明節を独立LuaLaTeX driverで9ページに組版し、全ページ画像を点検した。**主原稿全体の組版、旧共鳴四スクリプトの再実行、実際の楕円A生成元の作用係数計算は今回未実施。** 一次資料はPDF解析本文で照合したが、原典web screenshotはCache missで取得できなかった。状態の詳細は `research/resonance_hearts_validation.json`。

主原稿の再生成は `latexmk papers/nc_del_pezzo_resonance_hearts.tex`。旧共鳴検算は `verify_resonance_hearts.py`、`verify_resonance_extensions.py`、`verify_resonance_maximal_a2.py`、`verify_resonance_zigzag.py`。cubic cornerは `research/cubic_corner_validation.json` と同ノートの再現手順、H3は `research/cubic_surface_reproduce.md` と現行分類validation、次数1・三次三様体は各現行ノートを参照する。Python3（必要箇所はSymPy）、LuaLaTeX・LuaTeX-ja・latexmkを使い、生成PDFはGit追跡しない。数学的証明、有限検算、文献入力、独立査読を区別する。
