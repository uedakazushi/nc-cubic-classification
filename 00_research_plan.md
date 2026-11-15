# 研究方針：非可換del Pezzo曲面のheart比較と内在的モジュライ

現在のH3核心：位数4の固定包絡の全中心関係を厳密に復元し、中心が特異となる値を正確に13個へ絞った。消去式は対称枝次数16・非対称枝次数8、共通因子は(D-Dstar)^2。DstarはA3中心を持つが非H3である。中心の特異値と非H3値は同一視しない。次は一次元・二次元単純表現の中心像と局所orderを照合して、13値の良否を決定する。再現コードと証明は cubic_order4_center.tex および verify_cubic_order4_center_critical.py。全H3の被覆・相対降下は未完成。

classification-v13 では、gamma≠0 の積分族について全内在的 pointed 幾何学的な矢を記述した。Hesse216 の線形変換に、混合二次ポテンシャルを消す一意の t 平行移動 b=Mv を組み合わせる。a の作用、gamma'=gamma*det(M)/c、beta の非線形二次補正を明示し、三生成元の全ポテンシャル恒等式と九組全ての合成を有理関数体上で検証した。D の作用は20次元の次数3商で中心基底二列を解く有限線形計算で与え、実装と三つの厳密 control を保存した。全中心切断表示の商 stack の一般次元は8、一般慣性は自明、H3幾何学的部分の慣性は全て有限。非恒等な単冪 graded 自己同型は存在しない。これはこの指定chartの全矢であり、悪い D の全一覧、H3 相対開性・降下、全 H3 の被覆や成分分類は未解決。

classification-v12 では、積分した族の全次数平坦性・noetherian quadratic Koszul CY AS4 認識を、明示的な開集合 V={h∈H, (1-gamma²)≠0, Delta≠0} 上で証明した。入力は Iyudu–Shkarin Theorem1.1/Corollary6.1、EG形式変形定理、および64個の三次持上げ恒等式・256個の四次巡回恒等式・単元小行列式 -p^6 を確認した LBS 中心拡大定理である。中心三次の関係類の非消滅も巡回商の二係数で全パラメータについて確認した。gamma≠0 では低次数中心が0,0,1、滑らかな楕円THCR境界となり、全中心値の H3 判定は正確に一つの affine 中心切断の有限大域次元へ帰着する。定義体上超越的な全 D は H3。位数4の枝 gamma^4=1+h^3 では固定包絡の悪い D は有限であり、h=1,gamma=2^(1/4),A=1,B=C=0,beta=(-1,0,0),D=pi は明示的な非Clifford H3 対象となる。悪い値の全一覧・全内在的群oid・H3相対開性・降下・全包絡被覆は未解決。

classification-v11 では、Etingof–Ginzburg の付録と著者サイトにある Rains の E6 中心元を規約変換し、全パラメータで三交換子の関係恒等式を独立検証した。`alpha=-4*gamma*(A,B,C)` と置き、正規化した中心元に定数補正を加えると、全 Clifford 切断が実際の有理式による中心表示へ積分する。gamma=0 での全係数・関係証明書の分母はよい h の全底上で正則であり、全次数の「中心性」の障害は解決した。これは包絡族の全次数平坦性、AS4 認識、切断後の H3 条件や新成分を証明したという意味ではない。次はこの積分した具体的表示でそれらを検証する。

classification-v10 では、この族から外れる指定四方向の一次中心 incidence も全係数で判定した。双対数上で最高次を `(1+epsilon*gamma)yz+(1-epsilon*gamma)zy` に変え、対角項を `epsilon*alpha_x*tx`（巡回）だけ動かすと、三次中心切断の持ち上げは正確に `alpha=-4*gamma*(A,B,C)` のとき存在する。持ち上げを明示し、全ての h,beta,A,B,C,D に通用する次数4の階数86、三次交換子階数15、単元障害行列式 `-9/(4*(1+h^3)^2)` を検算した。これは指定方向の一次 incidence であり、積分可能性・全変形空間・新しい H3 成分を主張しない。 また、この明示的持ち上げの二次障害も全係数で消え、対角係数の二次補正 kappa と中心切断 G2 を計算した（epsilon^3=0）。中心性の全次数積分は v11 で解決し、H3 族への実現は未解決である。

## 最上位の分類目標と実行計画（2026-11-15）

**現在の最優先課題は強いintrinsic定義の14641型非可換三次曲面 H3 の完全分類。** 詳細なCodex指示は research/cubic_14641_codex_plan.md に置く。R=⊕Hom(O,tau^n O) は一次生成、二次包絡B=Q(R)は左右noetherian quadratic Koszul AS4、型14641。G∈B3の正則正規性とR=B/(G)は現行認識定理の結論であり公理ではない。

**現在の到達点：全H3にμ_R=1、σ_G=μ_B^{-1}が必要であり、固定Bの候補は単一の140×20線型核W1。** RRZtriのDε≠0はBの有限自由解消をRへtensorした非零perfect複体で検証した。CY包絡ではGは中心だが、非CY・非中心H3も実在する。

**Skew包絡部分の幾何学的H3対象を分類した。** 六次元全skew torusを座標jet・整数Smith証明書で37候補へ絞り、generic代数がM3(K)でrank-one条件に反する6点を除いて31パラメータ・五型となる。可換、CY符号、非CY符号、3乗根中心一次、3乗根二重指標。全admissible係数、滑らかさ、整域性、Serre/GK rank/AZ、幾何学的同型群oidを証明した。一般同型類の次元は順に4,1,2,1,0。全AS4包絡上のH3被覆や族のstack分類ではない。次はskewでないR13・Clifford・Ore等のW1、admissible切断・境界・相対降下。詳細はresearch/cubic_14641_classification.mdとresearch/cubic_classification_validation.json。日本語TeX依存はworkspace内で復旧し、全文組版を実行した。

非skewの標準CY chartでも、Pym L112/R22/S23の一般点とE3の非零変形は中心三次が零となりH3包絡から除外された。R22ではQQの20次小行列式280000000000/279926361、S23では−243の証明書を得た。Pym六標準chartの一般点で残るのはR13だが、特殊locus・交叉・他のAS4は未分類である。

**as4連携による全層除外（classification-v5）。** 固定SHA `60eacafa28156a5fc62f74eae004d64a84675f4b` の必要な構造定理だけを輸入し、逆中山規約を変換した。量子基底の全非自明unipotent持上げではW1=0なので、半単純化が量子基底となる部分全体を上記五型で分類した。非零微分Ore包絡は点対象の自己Extが1,3,4,4,…であり、全特殊値でもH3から除外される。CY基底の交換子次元4以上の非可換層、および三交換子beta層は全unipotent持上げも除外した。原資料の三検算を実行し、新規独立検算は computations/verify_cubic_as4_reductions.py。詳細な仮定・未輸入範囲は research/as4_imports.json。次はR13全切断、L112/R22/E3特殊locus、残る低交換子CY・非スカラー共鳴層。S23の非零Ore族を再び未分類扱いしない。

**R13切断の現状（classification-v6）。** 良い楕円中心拡大の全λで整域性と内在的rankを証明し、H3をアフィン中心商D/(ω+λ)の有限大域次元へ帰着した。複素数体上の分裂B=S[t]はΛ_B=C*、全非零λが一軌道、慣性H_Sはμ3によるPAut Sの中心拡大と完全に判定した。λ=0は点対象の無限自己Extで除外。非分裂Λ_Bの有効な決定と良い楕円仮定外の被覆が次のR13課題。有限位数translationの楕円境界を持つ固定Bでは例外値の有限性とΛ_Bの非空開性も証明した。例外値の明示、無限位数境界への同じ結論、全相対開性は未証明。新証明 cubic_r13_cut_reduction.tex と検算 verify_cubic_r13_cuts.py を参照。

**Clifford全切断（classification-v7）。** S_h=(yz+zy=h x²,巡回),B_h=S_h[t],h≠0,h³≠−1,8の明示的位数二楕円Hesse族では、全H3切断と全包絡間の幾何学的矢を分類した。全中心三次はg_h,tu,tv,tw,t³。D=0は反Serre固定点の奇数Ext1障害で除外し、D≠0はAzumaya中心曲面T_h+(Au+Bv+Cw+D)²の滑らかさが必要十分。固定h=1では明示的四次Ψ、位数54有限商、粗い三次元同型類空間を与えた。一係数方向の悪い値は0,−16A³/27,8A³/49。hを動かす全指定族は四次元の位数648有限商で、固定h比較群はh⁶+20h³−8=0で54から108へ増える。非自明な単冪持上げもない。これは全非分裂R13の被覆や全H3成分性・相対降下を意味しない。papers/sections/cubic_clifford_full_cuts.tex、二つのclifford検証器とvalidationを参照。

**非分裂への進展（classification-v8）。** 位数二Hesseの中心拡大 yz+zy=h x²+α_x tx+β_x t²（巡回）がH3包絡なら全α=0を証明した。一般の二次ポテンシャルf2はJac(H0)2に属する必要があり、t平行移動で全て除ける。mixed quarticからH3下のμ_B=1を確認し、中心三次持上げの一次障害行列式−27h/(8(1+h³)³)を全パラメータで証明。99関係恒等式と256巡回恒等式を厳密照合した。残る定数関係項β族のClifford rank-one退化点もclassification-v9で判定した。中心の特異性だけで非可換特異性を推論しない。

**非分裂全β分類（classification-v9）。** 位数二の指定対称ポテンシャル中心拡大部分について、全β・全切断の必要十分条件と全pointed幾何学的矢を証明した。中心F=detQ_β+(Au+Bv+Cw+D)²の全特異点がrankQ_β=1の通常二重点だけなら、かつそのときに限りH3。A1点の完備化はk[[s,t]]⋊Z2、退化点はExt1/Ext2のSerre対で除外する。pure volume切断はcharacter完全交叉8点の被約性と同値で、中心四nodeも許容する。全指定部分はGm恒等成分・Hessian216成分群による一般次元7の群商で、全慣性を明示的stabilizerとして判定。Dには混合補正がありD=0も許容される。一般慣性は自明、volume部分の一般慣性はμ2。単冪持上げも追加なし。次は他ambient方向の変形、別の楕円位数、非対称・非CY包絡の被覆と相対降下。

**最初は全AS4 ambientの完全分類を目指さず、正規三次incidence I3={(B,[G]):GB1=B1G} の構造定理を最優先。** 一般正規対は35×8積行列の5×5 minorsで求め、H3はさらにW1の線型核へ絞り、既知族の一般fiber、成分、境界、同型、非中心Gを調べる。Pym六成分で全14641型を尽くすとはしない。as4/asz4とpoisson-p4、既存のheart/corner研究を検証済み入力として利用する。正規商が無条件にintrinsic weak条件を満たすとは仮定しない。

完成基準は全対象の被覆、明示的な幾何データ、同型群oidと慣性、成分・交叉・境界、Serre/heart/rank/AZ条件、相対stack・降下。まず一般点と主要成分を決定し、未分類領域を厳密に縮小する。分類未完なら部分分類の正しい定理と証明を残す。GitHub mainを正本とし、push成功時Library保存なし。

## 14641型の内在的非可換三次曲面：当面の完全分類対象（2026-11-15）

統一intrinsic weakly marked三次曲面 (A,O) の反標準環 R をR1で生成されるものに限定し、二次包絡 B=Q(R) が左右noetherianな14641型quadratic Koszul AS4であることを要求するクラス H3 を分類する。外部ambient・埋込み・4周期同型は標識として加えない。公表用の主証明は papers/weak_cubic_axioms.tex の sec:14641-classification、再開用ノートは research/cubic_14641_classification.md。

【証明済み】Levasseurの整域定理（noetherian AS4, GKdim=4）とHilbert数値から、R=B/(G) で G∈B3 が左右正則正規となる。六二次＋一三次関係、三次核の正則性、正規一次境界は追加公理に不要。AS型は非空真部分：可換cubicはOU AS型、量子FermatはH3に属するが HH±1=2 で非OU。全OU退化境界が無条件にH3に入るとは未証明。

【有限方程式】固定ambient B上の全正規三次直線はP(B3)=P19の35×8乗法行列 [Gv|vG] の5次minorで表される。AS-flatな相対chartでも底変更と両立。内在的Serre/heart/rank/AZ条件の認識は別。量子skew torusの3-torsion 27点は座標置換で4軌道（1,8,12,6）、中心三次次元（20,5,6,4）。この27点のうち軌道長6の対角Fermat商はgeneric rank3でH3から除外される。全skew包絡のH3は上記31パラメータ・五型の分類で尽くされる。全AS4包絡の分類とは区別する。

【優先課題】全14641 ambient成分上の正規三次incidenceの成分・同型群oid・曲面条件・境界・族と降下を決定し、その後intrinsic定義を弱める。GitHub mainを正本とし、GitHub push成功時はLibraryへの保存を行わない。PDFやZIPをGitで追跡せず、TeX・ノート・検算コードを追跡する。


2026-11-15 / project-v29 / recognition-v6 / hearts-v14。最初に本書、`research/cubic_corner.md`、`papers/cubic_heart_corner.tex`を読む。比較の共通枠組みは`research/heart_comparison.md`と`papers/nc_del_pezzo_hearts.tex`、共通公理は`research/common_del_pezzo_framework.md`。次数別・三次三様体の研究はそれぞれの現行ノートから再開する。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化し、目標と論文構成を柔軟に改訂する。方針は現在有効な形へ書き直し、変更履歴を蓄積しない。証明済み、追加仮定、既知入力、未完成、予想、有限検算を区別する。証明の記載、今回の点検、外部独立査読、新規性確認を混同せず、誤りの影響を依存する本文・要約・方針へ反映する。

一次資料の仮定と適用範囲を確認する。公表用原稿は日本語LuaLaTeXとし、有効な主張と完全な証明を保持する。研究ノートは現在有効な補足・障害・反例・再取得困難な情報を整理し、論文の証明を全文重複させない。軽量化は履歴・重複・不要物の除去で行い、数学的内容や検証可能性を削らない。

研究継続用bundleは現行方針・ノート・論文ソース/PDF・必要コード・小証明書・再現手順から自己完結的に再開できるものとする。旧会話・旧ZIPを前提にせず、旧版・中間生成物・キャッシュを収録しない。研究区切りの承諾不要Library保存は一般的に許可されているが、本リポジトリはGitHub mainを正本とし、pushが成功した場合はLibraryに保存しない。pushが失敗した場合のみ緊急避難としてLibraryを利用する。通常fast-forwardで保存し遠隔HEADを確認する。既存Library資料は無断削除しない。GitHub Actions・force push・不要なPRを使わず、GitでPDF/ZIP/TeX中間物を追跡しない。生成、証明点検、計算、組版、Library保存、GitHub保存を別々に報告する。

## II. 上位目標と最初の対象

一般の非可換del Pezzo surfaceに対し、Rains heart、VdB heart、AS heart、anticanonical heartを比較する。これはdP1だけの補助問題ではなく内在的モジュライの中心課題であり、最初の実行対象はcubic surface（次数3）。四構成の存在、同じ入力、realization、指定同値のt-exactness、構造対象と反Serre作用、境界restriction、rank、marking、族への降下を分離する。四ラベルが四つの相異なるheartを与えるとも、全て同じとも仮定しない。以後この四名称を固定し、Rainsのgluing由来・VdBのliteral blow-up由来などは構成の説明に限って用いる。特にVdBのblow-up heartとsection-model側のheartを定義上同一視しない。

最初のAS–反標準比較は、標識と構造頂点を固定したnoetherian AS chartの非空開部分でabel同値まで進んだ。全域比較、VdB/Rains側とのpointedness、共鳴ごとの非自明tiltは未解決。どのabel圏・構造対象を分類するかを確定してから全intrinsic moduliへ進む。数値的共鳴の稠密性をAZ失敗・導来特異化へ直結しない。

## III. 現在の到達点

### Cubicの四交比還元と明示的corner開集合

`papers/cubic_heart_corner.tex`が完全な証明と計算の意味を記す。B=Jac(Q,W)、e=e_(A0)、C=B/BeB。Cは道長1で生成されるのでC_N=0から全高次数消滅が従う。最大minorによるU_Nは開、U=union U_NはC有限次元locus。C有限から両corner bimoduleの有限生成性を導き、B右noetherianの下でqgr B_cut→qgr eB_cut eをabel同値とする。標準AS helixのfolding・Serre・飽和の範囲でeB_cut eは指定構造対象の反標準環。道長gradingと反標準cut gradingは必ず区別する。

六点(1:0:0),(0:1:0),(0:0:1),(1:1:1),(1:2:3),(1:4:2)から27係数potentialを切断の積で構成した。全関係を含む厳密計算でCのHilbert関数は[8,21,33,38,33,21,8,0]、総次元162。7次6804列・21blockがQQとF_1000003でfull rank。従ってU7非空。可換点のAS性はAOU既知定理を使い、有限rankからAS性を推論していない。U7の外が全部非一致であるとはしない。

**四交比への還元（証明済み）**：構造頂点A0を除いた商Cはw_{0bc}の9係数に依存しない。残る18係数の非零トーラスは矢rescalingで四交比lambda_ij=q_ij q_00/(q_i0 q_0j)、q_bc=w_{2bc}/w_{1bc}の四変数に還元される。C有限次元なら18係数が全て非零でqの全九つの2×2小行列式も非零。さらにqと成分ごとの逆数行列の二つの行列式も非零でなければならない（rank2因子分解からk[t]値のJacobi表示を構成し非冪零閉路を得る）。minorが零なら2×2支持のJacobi関係を満たす表現に非零3-cycleを作り、Cの無限次元性を示す。有限corner locusは四次元トーラスの非空真開集合である。11個の明示的divisorが悪いlocusの全体であることを六点配置の復元とSerre消滅により証明した。P=(Qの成分逆数)^Tの三列と座標三点が一般位置であることは十一条件と同値。AOU(4.9)の幾何的rolled-up algebraで高次数のHomがO(-mK)を経由するためCが有限次元となる。四交比の有限corner locusは標識付き可換cubicの六点配置空間に同型。F7の80点でC7=0という既存検算は補助結果であり、標数0の十分性はこの幾何学的証明に依存する。新しい証明は`papers/sections/cubic_corner_determinantal_obstructions.tex`、検算は`computations/verify_cubic_corner_rank2.py`。証明は`papers/cubic_heart_corner.tex`、有理数検算は`computations/verify_cubic_corner_torus.py`。AS locusとの交叉と導来同値の問題は別途確認する。

**一様消滅次数の完成（今回証明）**：AOU幾何的rolled-up helixの道長7にある21ブロックを(6,9,6)に分け、4つのblow-down線束と例外曲線への制限、base-point-free pencil trick、Kodaira/Kawamata–Viehweg消滅から全てe=A0を経由することを示した。したがって11条件⇔C有限⇔C_7=0、さらに8頂点の対角でdim C_6≥8。M_7の最大minorイデアルの根基は四交比Laurent環でrad(Δ11)に一致する。証明は`papers/sections/cubic_corner_uniform_cutoff.tex`、整数交点検算は`computations/verify_cubic_corner_c7_geometry.py`。前回の特定六点のH_C計算とF7での80点計算は保持するが、一般定理の証明ではない。AS heartとanticanonical heartの自然同値は、既存のAS/noetherian/folding条件下のみで主張する。

**Hilbert関数・平坦性の完成（証明済み）**：AOUの幾何的rolled-up helixで八頂点間の全Hom次元は n=0..7 で(8,21,42,74,105,147,206,252)、e経由の像の次元は(0,0,9,36,72,126,198,252)。例外曲線、二つのconic-bundle pencil、四つのblowdown線束の積写像で全て計算した。道長6の2つのblowdown線束の積の単射性は縮約曲線3本のconic制限から従う。従ってCのHilbert関数は(8,21,33,38,33,21,8)に一様、総次元162。一定階数の関係行列から十一条件開集合上の有限局所自由な代数族が得られる。証明は`papers/sections/cubic_corner_hilbert_series.tex`、再現可能な整数数値台帳は`computations/verify_cubic_corner_hilbert.py`。以前の特定六点の厳密消去と有限体検算は独立の証拠であり、一般定理の証明入力ではない。全AS/全weak対象のheart一致を結論していない。

**古典的根壁の導来障害（証明済み）**：11禁止divisorはE6の有効根（10種類の共線性、1種類のconic）に対応。各因子一般点で六点blow-up Sは弱del Pezzo3、(-2)曲線Eは反標準射 f:S→X によりA1点へ収縮される。F=i_*O_E(-1)は2-sphericalかつ全nでRHom(O_S(n(-K)),F)=0、Rf_*F=0。従ってblow-up側で反標準AZ ampleは失敗し、Db(coh S)≄Db(qgr R)=Db(coh X)。任意次数の弱dPで(-2)曲線があれば同じ障害がある。Q=[[1,1,1],[1,2,2],[1,3,4]]の一壁例でnodeのHessian det=-2304を厳密計算。詳細 `papers/sections/cubic_corner_root_walls.tex`、再現 `computations/verify_cubic_root_wall.py`。非可換Rains/VdB/AS heartの特殊化と11壁のAS locusとの交叉は未解決。導来同値を前提とするHRS tiltとの混同を避ける。

### 稠密なRains共鳴でのanticanonical heartの変化（今回証明）

Rainsのsimple-root既約sheaf存在結果を用い、smooth elliptic/genuine del Pezzo avatarの負Euler指数共鳴 `O_E(alpha)⊗q^m=O_E`, `m=chi(e,M)<0` を解析した。境界に制限して零となる既約一次元sheaf M はtau固定で、全 n に対しHom(e,tau^nM)=Ext²(e,tau^nM)=0、dim Ext¹(e,tau^nM)=-m。Homが非零なら既約性でO_X→Mは全射だが、Rains Cor10.16のroot quotient下界chi≥1に矛盾する。よって**Rains heartのAZ amplenessが実際に失敗**する。反標準環Rの中心正則一次元gはMに同型として作用するため、N=⊕Ext¹(e,tau^n M)は各次数-m、anticanonical heartの境界外で非零。R/(g-1)の-m次元表現を与え、自然導来切断はPhi(M)=πN[-1]。従って自然比較はt-exactでない。反標準環のHilbert値1+d n(n+1)/2は共鳴で跳ばない。

楕円曲線Eでqを無限位数に固定し、p3(n)をO_E(p3(n))=O_E(1)(-p1-p2)⊗q^{-n}で動かすと、simple root h-e1-e2-e3のm=-n（n≥1）がgenuine滑らかなdel Pezzoを保ったままZariski dense。一般の6点配置パラメータでもファイバーごとに稠密で、次数1...6の適切なblow-up族にも及ぶ。標数零、適用できるRainsの既約sheaf存在とgluingの範囲での定理であり、全非可換del Pezzo成分の命題ではない。

**重大な区別**：genuine Sではm=0の根共鳴は存在せず、古典的weak dPの(-2)曲線の反標準収縮（導来圏の非同値）と、負指数の稠密共鳴（有限次元表現として[-1]へ移る）は異なる。負指数の稠密性だけからanticanonical qgrの特異化・導来非同値は導けない。既存`papers/dp1_anticanonical_models.tex`は全qでの導来同値を証明記載するが、今回は独立再監査していない。本結果の入力ではない。新原稿`papers/nc_del_pezzo_resonance_hearts.tex`、再開ノート`research/resonance_hearts.md`、整数計算`computations/verify_resonance_hearts.py`を読む。

### Resonanceの符号別Ext判定（現行定理）

境界に制限して零の既約純一次元root sheaf Mが実在し、alpha²=-2, alpha·K=0、m=chi(e,M)である場合、全n∈Zについてdim Hom(e,tau^nM)=max(m,0)、dim Ext¹=max(-m,0)、Ext²=0となる（Rains Cor7.23, Cor10.16, duality Cor5.9/Cor7.26,7.30,7.31/Prop7.16）。負指数m<0のRains heartでは(e,tau)のAZ amplenessが失敗、anticanonical heartの境界外にR/(g-1)の(-m)次元表現が[-1]で現れる。正指数m>0ではm次元表現がheartの次数0に現れる。零指数m=0では非零Mが全orbitに導来的に直交し、自然導来切断はMを消す。根sheafはどのmでも2-spherical。正負各符号の共鳴は、楕円曲線上の吹上げ点移動でそれぞれZariski denseとなる。反標準環Hilbert値は1+d n(n+1)/2で跳ばない。

**重要な証明訂正**：旧稿の「既約Mへのe→Mの非零射は全射」は誤り。正しくはimage Iと零次元cokernel Tを取り、chi(e,I)≥1とchi(e,T)≥0からm≥1となるためm≤0でHom=0。この変更を論文・ノートへ反映。正指数m>0のExt¹=0はRainsの反変双対R adがEuler指数の符号を反転することで今回証明した。既存dP1原稿の全q導来同値の独立再監査は未実施であり、この符号別判定に用いていない。

新しい現行証明は`papers/nc_del_pezzo_resonance_hearts.tex`と`papers/sections/resonance_sign_trichotomy.tex`。再開ノート`research/resonance_hearts.md`、E6/E8格子とP1上の双対モデルの数値検算`computations/verify_resonance_hearts.py`。非既約対象のtorsion pair、AS/VdB/Rains各heartの全体的比較、qgr smoothnessは未解決。

### 境界非交叉sheafの二項振幅と混合共鳴の相殺（新定理）

Rains heartの`Z={M | dim M≤1, Li^*M=0}`は拡大閉のexact category。θM→Mが同型、τM=M、Rains Cor7.23からExt²(e,M)=0。中心正則gの周期性により、自然導来切断はZ上でcohomological amplitude [0,1]、`V^j(M)=(⊕Ext^j(e,τ^nM)[g^-1])_0` (j=0,1) は有限次元A=R/(g-1)加群。短完全列からの6項A線型完全列`0→V0(M1)→V0(M2)→V0(M3)→V1(M1)→V1(M2)→V1(M3)→0`を証明。Z+=ker Ext¹(e,-)とZ-=ker Hom(e,-)は拡大閉で各V0/V1はexactだが、この二者がZ上のtorsion pairという結論は未証明。

混合拡大0→M-→M→M+→0のconnecting`δ_M:V+→V-`のrankをrとすると`dim V0(M)=m+-r`、`dim V1(M)=-m--r`。δが同型なら非零Mが自然導来切断で零となり、全q導来同値主張の直接検証条件になる。古典的weak dPの(-2)曲線のEuler完全列`O(-2)→O(-1)^2→O`は実際にδが同型となる例。genuine非可換への存在は未証明。

異なる境界非交叉既約根sheaf Mα,Mβが同じRains heartに存在すれば`Hom=Ext²=0`、`dim Ext¹(Mα,Mβ)=α·β`（Rains Cor7.13 Euler形式）。交点<0なら同時存在不可、=0なら拡大無し、=1ならExt¹が1次元。自然Φがこの二対象間で完全忠実なら`dim Hom_A(V+,V-)=α·β`が必要。αβ=1かつmα+mβ=0の同時共鳴はgenuine Sで不可能：α+βが根となり、そのE制限が自明になってしまうため。E6の72根と46組のrank式を厳密検算した。原稿`papers/sections/resonance_extension_cancellation.tex`、再現`computations/verify_resonance_extensions.py`。

これは負・正指数の稠密性と矛盾せず、共鳴軌跡の交叉に制約を与える。いまだ全Zのheartの完全な分類、全q導来同値、特異qgrの分類は未解決。旧dP1の導来同値の独立監査で、実在する混合拡大のδとアフィン加群間Homの次元を優先的に照合する。

### 最大E6共鳴の完全な整数表示と実在混合A2対（新定理）

smooth plane cubic E（flex origin o）、非torsion qを固定。六点blowupの根格子E6の単純根alpha0=h-e1-e2-e3、alpha_i=e_i-e_(i+1) (1≤i≤5)を用いる。全72根のrestrictionが<q>にあることは六単純根共鳴と同値。共鳴指数m0,...,m5∈Zを指定すると、六点は`3p1=(m0-2m1-m2)q`、`p_i=p1+(Σ_{j<i}m_j)q`で決まり、p1の選択は3-torsionの9通り。全72根の指数が非零であることが六点一般位置（genuine smooth cubic）の必要十分条件であり、整数のE6根超平面を避けるregular lattice pointsとして記述できる。

相異なる**正整数**N_iについてp_i=N_i qとすると全72根が非零指数で共鳴し六点は一般位置。これらの点はE^6にZariski dense。N1<N3<N2を課した部分もdense。N=(1,3,2,5,7,11)では六単純根指数[6,2,-1,3,2,4]、alpha=e1-e2はm=2、beta=e2-e3はm=-1、alpha·beta=1。Rains 2022 §4のsimple-root effectivityと2019 §9,§11のformal(-2)根sheaf存在から、同じRains heartに境界非交叉の**実在する**正負既約根sheaf M_alpha,M_betaがあり、Ext¹(M_alpha,M_beta)=k。72根が共鳴しても72のroot sheafが全て既約で存在するとは言わない。

混合拡大0→M_beta→M→M_alpha→0のδ:V_alpha(2d)→V_beta(1d)のrankは0/1、従って自然導来切断のcohomologyは(2,1)または(1,0)。δの値は未計算。より一般にb個のM_betaとa≥1個のM_alphaの二段拡大でδ=d⊗T、rank≤min(a,b)、dimV0≥a>0。従ってb=2aでχ(e,M)=0でもPhi(M)は非零。**Phiがこのpairで完全忠実なら**Hom_A(V_alpha,V_beta)=kとなり、2次元V_alphaは1次元V_betaを商に持つため単純A-moduleではない。これは独立検証すべき具体的予測であって、全q導来同値の証明ではない。

有理数例：E:y²=x³−x+1、q=(0,1) は2q=(1/4,−7/8)とNagell–Lutzから無限位数。上の六倍点は全20三点行列式とconic評価行列式が非零、E6全72根のmが非零。原稿`papers/sections/resonance_maximal_a2.tex`（`papers/nc_del_pezzo_resonance_hearts.tex`からinput）、再現`computations/verify_resonance_maximal_a2.py`。今回全根共鳴の**数値条件**とRainsの**効果的simple根の実在**を区別する。

### 全次数1–6における最大根共鳴の稠密性（証明済み）

Eを変曲点oで原点を定めた滑らかな平面三次、q∈Eを非torsionとする。次数d=9-r（r=3,...,8）に対して、任意の相異なる正整数N_iを選びp_i=N_i qとするとBl_{p_i}P²はsmooth genuine del Pezzoで、A2+A1,A4,D5,E6,E7,E8の全根（順に8,20,40,72,126,240個）が同時に非零整数指数で数値的共鳴する。この最大共鳴点は各E^rでZariski dense。単純根指数m0,...,m_(r-1)から 3p1=(m0-2m1-m2)q、p_i=p1+Σ_{j<i}m_j q で復元し、p1は9個の3-torsion選択を持つ。一般位置は全根指数非零と同値。r8の追加3h−2e_i−Σ_{j≠i}e_jも正整数指数を持つ。N1<N3<N2の部分も稠密で、Rains既約simple-root sheaf existenceが適用されれば正負の隣接A2根が同時存在し、Ext¹=kかつ負指数Rains AZ失敗が稠密に起こる。

証明`papers/sections/resonance_maximal_all_degrees.tex`を既存の`papers/nc_del_pezzo_resonance_hearts.tex`へ統合。再現可能な全根整数列挙は`computations/verify_resonance_maximal_a2.py`に集約し、既存cubic有理楕円証明書を保持。数値共鳴≠全根sheaf既約existence。Z全体のtorsion pair、Aの2次元/1次元表現とδ rank、全q導来同値、特異境界は未解決。

### 最大共鳴の既約root分類・zigzag形式性（証明済み）

Rainsのsimple-root存在の仮定下、最大共鳴でr=9−d個の単純根sheaf M_iが実在するとき、他の根類の境界非交叉既約純一次元sheafは存在しない。非単純正根gammaはgamma²=-2からどれかのsimple alpha_iとgamma·alpha_i<0になり、Ext¹次元の非負性に反する。負根はRains Prop7.19で排除、q非torsionなら同根sheafは数値EulerとRains Cor7.7で一意。T=⊕M_iのgraded Yoneda代数はDynkin zigzag Z(Δ)、次数別次元(r,2s,r)、総次元d6,...,1で8,14,18,22,26,30。既知一次定理 Liu–Wang, J. Algebra 677 (2025), Thm1.1（Etgü–Lekili/Lekili–Uedaの先行結果）を実際のPDFで確認し、char0のADE zigzagのintrinsic formalityを適用。d6のA2+A1は成分分離と孤立A1の次数理由による。

結果として**固定したenhanced Rains導来圏でのTのframed形式変形**は二次Maurer–Cartan方程式m₂(x,x)=0のみ。Dynkin森の葉からの帰納法で定義イデアルは各辺積(x_ij x_ji)。gauge商前の形式スキームは2^s個のs次元形式座標空間の合併：d6,...,1で分枝数2,8,16,32,64,128、cubic E6は32個の5次元分枝。高次A∞障害はないが、Rains曲面そのものの相対moduli、anticanonical heart全体、有限次元A=R/(g−1)表現の行列と混合δのrankはまだ決定していない。

全文`papers/sections/resonance_zigzag_unique.tex`を`papers/nc_del_pezzo_resonance_hearts.tex`にinput、計算は`computations/verify_resonance_zigzag.py`。Rains Prop7.19, Cor7.7, Cor7.13とLiu–Wang Thm1.1を使用。新規性・独立査読未確認。

### HRSと一般heart判定

既存`papers/nc_del_pezzo_hearts.tex`の振幅1比較は(T,U)=(ker R1δ_*,ker δ_*)、transported heart=<U[1],T>、t-exact iff U=0を与える。対象は導来的には消えずshiftされる。既存の豊富orbitによる一意性は高次Ext tail消滅を明示的に必要とする。

今回、pointedness・反Serre適合性・標的AZ/高次消滅の下で、周期1の非零単純対象Mについてchi(e,M)>0 iff M∈T、chi(e,M)<0 iff M∈Uを証明した。chi=0はこの仮定下で不可能。非単純対象や未構成の共鳴対象へ無条件で適用しない。

AOU§9の左辺はqgr Fであり、Theorem9.4の導来同値をraw blow-up heartのabel同値と読まない。mutation後E0とπFは実際の対象として照合する。今回のcorner同値はAS側Oから作った反標準環との比較であり、特定のVdB比較との一致は残る。

### 保持する共通公理と次数3の成果

weakly markedは非零Ext有限noetherian Abel圏、Serre、tau=S^-1[2]のheart保存、Gabriel–Krull rank-one torsion-free exceptional O、AZ ampleness、次数dのHilbert数値。hdim=2はSerreから従い独立公理でない。exceptionalityなしのpre-weakからExt1(O,O)=0は未証明。提示やAS ambientは認識問題である。

`papers/weak_cubic_axioms.tex`は正則正規一次境界R/(t)=S0/(g)から一次生成・二次包絡AS4・正規超曲面を認識する。Cassidy–Sheltonの低次数判定とnormal直線を保つtwistを使う。全weak対象の境界存在は未証明。量子Fermatは全対象のR(1,3)帰属を排除し、Pym L(1,1,1,1)とL(1,1,2)の交点に属する。他の成分交差は未決定。対角中心Fermat三次を持つtorus点は27点。固定ambientの中心開部分の商BH54は全変形rigidityではない。PBW12係数・三条件、Artin平坦変形の提示保持・有限型形式模型を保持する。

`papers/cubic_surface_ambient_moduli.tex`と`research/r13_generic_moduli.md`はR13、Poisson延長、8→7、AOU形式比較、四頂点potential、中心incidence、Hessian商・臨界点等を保持する。全weak stackの代数性・marking存在一意性降下・全成分分類は未完成。既存の72root・Euler/Serre行列検算は保持するが今回再実行したとはしない。

### 保持する並行成果：量子FermatのOU障害

`papers/quantum_fermat_not_as_surface.tex` は量子Fermat cubicの圏を離散torsion付きFermat商stackと同定し、HH_{-1}=HH_1=2、HH_0=5を計算して、完全強例外列を持つOU AS surfaceではないと結論する現行原稿である。従ってintrinsic weak cubic全体をOU/AOUのWeyl商と同定しない。この曲面圏そのものの障害はambientのPym成分帰属と独立である。コード `computations/verify_quantum_fermat_ou_sectors.py` と証明書を含む並行更新を保持したが、今回その証明・計算を独立に再監査したとは報告しない。今回のcorner定理もOU/AS領域に限定し、量子Fermatを適用範囲へ入れない。

### 保持する次数1と三次三様体

`papers/nc_del_pezzo_degree1_moduli.tex`はrank、条件付きweighted sextic、10次元dg族、KS、補助A∞表示成分、avatar復元を保持する。`papers/dp1_anticanonical_models.tex`の楕円領域比較は今回再監査せず、本結果の入力としない。特異/非局所自由境界と全intrinsic abelian成分性は未完成。

`papers/nc_cubic_threefold_moduli.tex`と全section・計算を独立維持する。37次元形式ambient、41次元中心対、商13/17、fiber4と全大域stackでの代数性/成分性は区別する。今回再証明・再検算したとは報告しない。

## IV. 優先順位と具体的な着手

**Rains dense resonanceの次の優先問題**：既約rootの全根類分類・zigzag Ext代数・形式性・固定dg圏内のframed形式変形は解決した。最優先は実在する混合A2根対のA=R/(g−1)の2次元と1次元表現の作用行列を構成し、connecting δのrank(0または1)とHom_A(Vα,Vβ)を実測し、既存dP1全q導来同値の完全忠実性を独立検証する。全Rains heartのtorsion pairと相対moduliは未解決。

1. **Cubicの構造対象と同値の照合**：AOUの実際のmutationでE0≃πFを検証し、AS corner同値と既知のqgr F比較を接続する。数値K0や境界restrictionだけで同定しない。
2. **非可換AS locusと根壁**：古典的11根壁では反標準収縮が2-spherical対象を消し、導来非同値になることを確定した。次は非可換AS-regular potentialと各壁の交叉、Rains/VdB heartの特殊化、実在する核やpointednessを判定する。古典的障害を全非可換境界へ無条件には拡張しない。
3. **VdB最後の段階**：同じ楕円・六点データでker δ_6*とR1δ_6*を実在root対象で計算する。pointednessと周期作用を確認後、単純対象のEuler符号判定を適用する。Rains raw反復と各段階section模型への置換も区別する。
4. **境界・一般次数**：有限位数、nodal/cuspidal境界、weak avatar、dP1への拡張ではgrading・noetherian性・realizationを再確認する。正規境界の一般存在、相対PBW、marking降下、Fermat分枝の研究は維持する。

## V. 再現と検証状態

    python3 computations/verify_cubic_corner_torus.py
    python3 computations/verify_cubic_corner_rank2.py --scan-f7
    python3 computations/verify_cubic_six_points.py
    python3 computations/verify_cubic_corner_c7_geometry.py
    python3 computations/verify_cubic_corner_hilbert.py
    python3 computations/verify_cubic_root_wall.py
    python3 computations/verify_cubic_corner.py
    python3 computations/verify_resonance_hearts.py  # sign table and roots
    python3 computations/verify_resonance_extensions.py # E6 root intersections and mixed extensions
    python3 computations/verify_resonance_maximal_a2.py # 72 simultaneous roots and rational A2 witness
    python3 computations/verify_resonance_zigzag.py # root classes, zigzag and formal cone
    latexmk papers/cubic_heart_corner.tex

Python標準ライブラリで全有理数計算と有限体計算を再現する。証明書summaryは`computations/cubic_corner_certificate.json`、検証状態は`research/cubic_corner_validation.json`。追加した六点復元の完全な証明を含む原稿10ページをLuaLaTeXで組版し参照を確認した。一般cornerの証明、計算機による厳密rank証明、既知AS入力を分ける。独立査読・形式化・網羅的新規性調査は未実施。従来の研究の再現はその現行ノートを参照する。
