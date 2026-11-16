# 研究方針：H3型内在的非可換三次曲面の完全分類

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

Rains・VdB・AS・anticanonical heartの一般次数比較は [nc-dp-surface-hearts](https://github.com/uedakazushi/nc-dp-surface-hearts) に移管した。本リポジトリではH3分類を最優先とし、必要な結果を固定commitと仮定に基づいて参照する。

## III. H3分類の現状と次の具体的着手

主原稿は `papers/weak_cubic_axioms.tex`、詳細は `research/cubic_14641_classification.md`、`notes/research_notes.md`、検証範囲は `research/cubic_classification_validation.json`。以下はこれらの現行成果を参照する要約であり、共鳴研究の更新時に全てを独立再監査したという意味ではない。

**固定PI4包絡の完全判定**：h=1、gamma^4=2、alpha=(−2,−2,0)、beta=(1,1,2)のD切断族で、中心特異値は13個だが非H3値は平方因子のない次数6式 b(D)=(D−Dstar)*P4(D)*Q1(D)の根に限る。他のDのaffine切断は大域次元2。`papers/sections/cubic_order4_local_orders.tex` はgrの最大性、中心正則列とbalanced local dualityによる対称双対、DVR標準形の非分岐性、A1二重被覆の指標多重度を使う。小次元表現のnorm・二中心点への分配・次数6式は厳密検算済み。D直線のH3条件は主開集合D(b)で、任意底変更・fpqc降下に適合し、そのaffine族は相対対角の長さ2以下の射影分解を持つ。これは一固定包絡の判定で、全位数4族・全H3の被覆ではない。

**滑らかな楕円境界部分（H3 classification-v36）**：中央境界では、次数3 translation THCRの全filtered deformationからCY AS4包絡と正則中心三次を復元し、全幾何学的矢をfiltered同型で記述した。有限Nのadmissibilityは中心McKay条件で完全判定し、被約固定N族ではH3開性・任意底変更・fpqc降下も得た。三捩れ量子Weyl chartの全中心と有限Hessian/character判定、j0 potential境界の非分裂例も保持する。

**非中央正規一次楕円境界**：共役位数は2または3に限る。位数2は量子involution（既存符号型）とClifford swapへ漏れなく被覆し、後者の三次は一本、中央volumeへの有限cocycle還元により長さ8 character完全交叉の被約性が必要十分。非skew・非CYの具体例を検算済み。位数3は最高Koszul tensorの8次元随伴模型と全Jordan型の計算から量子P2に限られ、全対象が既知の量子Fermat一対象、幾何学的群oidBH54となる。全H3が正規一次楕円境界を持つとは主張しない。

**滑らかな正規楕円境界の外の実例**：q³1のq-so3包絡のCasimir切断で、全H3判定(D−f)(3D+f)≠0を得た。中心はFricke cubic、無限遠triangleはterminal order、許容対象はどの正規一次境界でもsmooth elliptic THCRを持たない。これによりmissing-boundaryの実在部分を一つ完全判定した。全intrinsic矢はD不変・慣性A4、相対表示stackはgood Dline×BA4。一般qでも全切断の忠実差分模型と整域性、全候補矢[Q/S4]を得た（classification-v47）。非捩れまたは位数>3では全H3候補がこのpencilに限る。奇数位数N>=3では全中心Fricke式と任意次元の二種の三重対角既約表現から、H3 iff(D−D+)(D−D−)!=0を証明した（classification-v50）。全N−1内部特異値もMcKay条件を満たす。偶数位数も半Chebyshev正規元のweight分解から全端点を排除し、全有限位数qでH3 iffD!=D±を完全判定した（classification-v54）。粗座標theta=q+q^-1,w=−theta−h³D/q²、固定N表示stackはphi(N)/2個の(A1_w minus{+-2})×BA4。全中心形成は任意底変更と可換。これら全族は正規smoothE境界を持たず候補平面に稠密。非捩れqでもGWA反転固定環へのOre局所化から二端点の非H3性を証明した（classification-v55）。端点以外はこのOre開集合gl<=2。三頂点の形式的模型は全qでgl2、非捩れで完備量子平面と証明したがqgr降下は未完。さらに全標数0代数閉体上のproper楕円四次元Sklyanin（n∞又はn!=1,2,4）を全排除した：唯一の中心三次残余n3もdimZ3=dimS1=4により射影norm P3->P3が全射、全Gが一次式×二次式でnondomain（classification-v58）。一般にCY・PI3・normal-centre-finiteのH3包絡はdimZ3>=5が必要。さらに三乗根の固定量子so3包絡はpencilだけでなく全P4中心三次を完全判定した（classification-v60）。Delta=alpha³+27beta gamma delta!=0かつ五節点cubic3foldのdual外が必要十分。全表示stack[U/A4]はDM4、慣性1/C2/C3/A4、全中心basechangeと表示族降下。さらに指定qso3正常形の中心incidenceはp(q)(beta,gamma,delta)=0、dim2水平とdim4垂直がdim1で交叉する。固定Bのmissing smoothE locusは既約normal-crossing divisor、全点がsmoothE H3の特殊化。粗tetrahedral商・境界正規化も明示した（classification-v61）。一般Zhang twistも縮小した（classification-v63）：twisted-skewのH3はskewに戻る。非退化中央quadric pencilを持つproper Sklyaninの全自己同型Zhangtwistと標準V4cocycle twistは全排除。cocycle centre3はn3/6のみdim1で必ず一次×二次。Stafford三族と標準cocycle・循環変種も全T/全許容dで全排除した（classification-v68）。通常W1はL=alpha beta+alpha+3beta−1=0でだけdim2、全pencilがdegree3因子写像で分解。CY cocycleのcentre3は四つの互いに素な明示曲線でのみdim1となり全て分解する。sigmaの全T第三反復で特殊chartの欠落も除いた。

**as4具体表示の独立排除（classification-v89）**：固定commit a45f834f51a00c47443b51caf66abaf4629546b9からは具体表示のみを参照し、全CY/全AS4被覆・存在十分性・全同型を新規輸入しない。二重被覆DCC1二族、非被約のCF2/CF3/CT2、TT22六表示、DS3/DT1全列挙表示は排除済み。四単純基点ではFS4のSと標準cocycleを全値排除し、FZ2のQも零交換子CY skewの中心三次は純三乗一本以下という一般補題で全排除し、FZ4/FZ5のO/Hおよび標準Klein cocycleも全値排除した。さらにFN3七表示L/M/F0/F1/G0/G1/K、第五係数零のM_p二族とN/C、FO2の全二パラメータH_(lambda,p)、FG2の全R_lambda両符号を排除済み。Rはtwist後の非零中央二次の逆指標から全奇数中心が零となる。FI2のJ_h両符号も全h非零で中心3消滅により排除し、h0は五次次元58の独立計算でAS4から除外した。FT3のPも全二パラメータ・両符号を排除した。詳細な式・全値rank cover・Ore/normalizer証明は `papers/sections/cubic_as4_*exclusions.tex`、輸入範囲と実行済み検証は `research/as4_imports.json` と `research/cubic_classification_validation.json` を読む。隣接AZ2の二固定Lも、Ore normalizerの三乗がomega/omega²倍になることと純base切断の頂点無限Extにより排除した。一般にCYのB=S[z;sigma]でsigma³が非自明scalarならH3にならない。隣接AB3の全S_zetaも四次次元>=37で排除し、T_-2両符号がその特殊値に一致することを独立確認した。T両符号も全lambdaで排除した。全64三次語のprimitive交換子moduleについて独立なC_0 X=N恒等式と20三角pivotを検証し、追加因子ABC_*とその対合像が互いに素なので二枚で全残余を覆う。三次/四次商射影も元の全関係で再生確認し、全値AS4存在・平坦性は仮定しない。Pは全二変数の商射影と40次元realified rank恒等式を独立検証し、次数30の垂直例外をlambda反射と三特殊直線の全r計算で全て排除した。次は列挙表示から全H3へ至る必要被覆定理を監査し、残る未被覆領域と許容条件を縮小する。

**全体的なスペクトル制約（classification-v139）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定（v121–123）。(3,1)gamma0とcanonical量子Veronesecone枝は全排除。残る全候補のcanonical AS3基礎A0はB/R双方へ埋まる。vがQgr(A0)に入れば非零sGがA0∩(G)に入り矛盾するため、vは商体外。これにより純正二次関係3本は必ず二本の可逆crossと一本のmonic平方へ還元でき、vt=g(t)v+delta(t),v²=ell*v+qが全候補を被覆する。T=<W>は対角/Jordan両基礎でHT=1/((1-t)²(1-t²))、T2に関係なし。T基底×vv/zzを避ける交互語はHB=(1-t)^-4と一致して実際の基底となる。gはT自己同型、deltaは次数1skew derivation、平方互換は(g delta+delta g)(t)=ell*g(t)-g²(t)*ell。追加正規化仮定を課した部分chartではない。次はこの全被覆上の平方互換と正常三次を、対角/Jordan・共鳴値込みで排除又は分類する。(2,2)、三固有値以上、全CY被覆、全成分/圏族降下は未完。

**次の核心**：Clifford swapは境界一意性と全intrinsic矢を有限係数式で得て、一般次元2・一般慣性mu2×mu2を確定した。許容条件は明示四次式Delta_h(b,c)≠0（固定hで四つのbad方向）。この表示族は分離既約DMstack2へrigidifyできる。偶Veronese全中心はcubic scroll F1で、局所自由階数4の極大quaternion orderとなり、二本の滑らかな有理分岐曲線が四点横断する。次は抽象intrinsic family比較、中央無限位数の全admissibilityと、正規一次楕円境界を持たないH3の漏れのない被覆を進める。全既約成分・交叉・境界と全intrinsic family降下は未完成。

既存の主要な構造結果を維持する：

- 全H3でmu_R=1、sigma_G=mu_B^−1。固定Bの候補は単一の140×20線型核W1。一般正規三次incidenceは35×8乗法行列の5次minor。CY包絡ならG中心だが非CY・非中心例も実在する。
- 全skew包絡部分の幾何学的対象は31座標パラメータ・五型で分類済み。可換、CY符号、非CY符号、3乗根中心一次、3乗根二重指標。一般同型類次元4,1,2,1,0。37候補のうちgeneric algebra=M3(K)となる6点はrank-one条件で除外。
- Pym L112/R22/S23の一般点、E3の非零変形を中心三次消滅で除外。as4からの検証済み構造結果により量子基底の全非自明unipotent持上げも除外。非零微分Ore包絡は点の自己Extが1,3,4,4,…で全特殊値を除外。CY交換子次元4以上と三交換子beta層の指定持上げも除外。固定SHA・規約は `research/as4_imports.json`。
- 良い楕円R13中心切断はaffine中心商の有限大域次元に帰着。分裂B=S[t]、低次中心(0,0,kg)ではlambda≠0が一軌道、慣性はmu3によるPAut(S)の中心拡大、lambda=0は除外。有限位数境界の固定包絡では悪い中心値は有限。
- 位数二Hesse–Cliffordの分裂全切断は中心曲面の滑らかさで判定。固定h=1の位数54商、全指定h族の一般四次元・位数648商を得る。比較群が倍増するh^6+20h^3−8=0も判定済み。非分裂対称ポテンシャルの二次項は平行移動で消え、全beta族はClifford rank1点の通常二重点のみを許す局所条件で分類。一般七次元の明示的群商、Dの混合補正と慣性を保持。
- gamma≠0への積分族は明示開集合上で全次数平坦・noetherian quadratic Koszul CY AS4。Rains中心元を規約変換した中心三次持上げを持ち、全pointed幾何学的矢はHesse216と一意の混合平行移動で記述。表示商の一般次元8、一般慣性自明、H3部分の慣性有限、非自明unipotent自己同型なし。超越的中心値のH3例もある。

これらを全H3の成分分類とは呼ばない。未被覆のPym特殊locus、低交換子CY、非スカラー共鳴、非対称・非CY包絡、j=0その他の境界、Z-algebraとの差と相対降下を縮小する。詳細な全式と証明は現行papers/sectionsにあり、本書で省略した係数等を削除してはいない。

## IV. 関連研究と研究継続

四つのheart・Rains共鳴・cubic cornerの公表原稿・研究ノート・検算は [nc-dp-surface-hearts](https://github.com/uedakazushi/nc-dp-surface-hearts) を正本とする。次数1固有の非可換del Pezzoモジュライは [nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli)、非可換三次三様体は [nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli) を正本とする。量子FermatのOU障害とambient比較は `papers/quantum_fermat_not_as_surface.tex`、`papers/cubic_surface_ambient_moduli.tex` に保持する。

## V. H3の再現・検証

主原稿 `papers/weak_cubic_axioms.tex`、分類ノート `research/cubic_14641_classification.md`、検証 `research/cubic_classification_validation.json` を読む。再現例：
```sh
latexmk papers/weak_cubic_axioms.tex
python3 computations/verify_cubic_skew_jets.py
```
他の個別検算は現行分類validationに記す。今回の移管は数学的定理の再監査とは区別する。
