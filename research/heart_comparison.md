# 四つのheartの比較：現行研究ノート

2026-11-16 / hearts-v22。最初に `research/four_hearts_plan.md`（プロジェクト全体では `00_research_plan.md`）を読む。論文は `papers/nc_del_pezzo_hearts.tex` と八つの `papers/sections/four_hearts_*.tex`、検証は `research/four_hearts_validation.json`。本文の証明をここに重複させない。

## 比較対象と主張の水準

VdBはliteral/raw blow-upのcoherent heart、Rainsは指定blowdown/gluingのt構造、anticanonicalは指定eとs=S^−1[2]のorbit環のqgr、ASはAS正則三次元Z-algebraのqgr。名称が四つの異なる圏を意味するわけではない。ASのhelix全体と一頂点の反Serre orbit、AS正則三次元とambient AS4、Z-algebraと一周期graded algebraを分ける。

有界heartの存在はDb(heart)のrealization同値を含意しない。pointed同値には構造対象とsへの両立同型が必要で、境界・rank・marking・相対降下はさらに別である。右加群の積はab=s^(deg b)(a)∘b。

## 現行論文に収めた確定結果

**VdB–Rains（thm:RV）**：同じ初期heart・blow-up中心・gluing bimodule・blow-down関手を同定し、Rains Lemma4.9/Proposition4.17のpseudo-canonical認識を使う。全整数ellについてRα_*θ^ell Mが非負にあることが上のt構造を決めるため、誘導同値はt-exactとなる。独立なavatar間のパラメータ対応はこの定理に含まれない。

VdBの図式X_j←tilde X_j→X_(j+1)で左はblow-up、右δはsection model。Definition11.1.2の一般位置条件下のTheorem11.1.3とLemma9.1.5はRδ_*の振幅[0,1]と導来同値を与える。T=ker R1δ_*、F=ker δ_*、輸送heart=〈F[1],T〉。Chapter12のF=P/(C3)表示は同じ一般位置条件なしにも存在するので、表示の範囲を導来比較へ広げない。Remark12.0.5のraw/sectionの区別を保つ。

**Rains–反標準（thm:derived、thm:globaltilt）**：genuine smooth classical del Pezzo S、smooth E∈|−K_S|、q∈Pic0(E)の指定gluingが範囲。全qで自然Φ=πRΓ*はdg導来同値。証明はIndでのorbit生成、境界自己拡大を追ったtraceの非零性、sourceのsmooth proper性と飽和性による右随伴と全射性。target smoothnessを前提にしない。無限位数にはRSS Proposition2.4（degree1も許す）、有限位数にはYZのPI・中心持上げ・χの三定理を使う。

HnefのRains heartで全対象のExt2(e,s^nM)はn≫0で消える。従って全heartの振幅[0,1]、T=ker H1Φ、F=ker H0Φによる一回のHRS tiltとなる。q非torsionなら境界外有限長Serre圏Zへ制限され、T∩Z=ker Ext1(e,−)、F∩Z=ker Hom(e,−)。一般対象に生のExt消滅を同一視しない。

**共鳴（thm:sign、cor:negative）**：rho(alpha)=q^(−m)は数値条件。実在する境界非交叉既約root sheafではh0=max(m,0)、h1=max(−m,0)、h2=0で2-spherical。負指数はAZ生成性失敗と自然Φの非t-exactnessを検出するが、上記gluingで導来同値は保たれる。数値的ample coneとAZ条件は定義が違う。正指数根だけからAZ失敗とは言えず、負指数根が見つからないだけでF=0とも言えない。pointed heart非一致を抽象的abel非同値に強めない。

**AS–反標準（cor:ASac、cor:AOU-texact）**：AS helixのfoldingでqgrBを得てe=πpB、pBp=R(e,s)を同定した上で、B,R右noetherian、Bp右R有限、pB左R有限を要求する。この範囲で自然cornerがabel同値 iff dim B/BpB<∞。有限次数の消滅を使うには次数1生成等のtail制御が必要。相対有限cornerの開性はcoherent各次数の基底変更適合を明示した命題prop:relativecornerであり、heartの相対同値を意味しない。

**混合A2（prop:rank、prop:A2category）**：指数p,−nの隣接単純根の非分裂拡大Pのconnecting rankはmin(p,n)。C=〈S+,S−〉_Serre≃mod_fd Π(A2)、直既約S+,S−,P,Qで、cohomologyは(p,0),(0,n),((p−n)+,(n−p)+),(p,n)。両chamberのtorsion pairを得る。p=nはgenuine avatarに実在しない。指数+2/−1のアフィン側では異なる一次元W,Uと非分裂二次元Vがあり、逆向きV'を合わせてA/Ann(V⊕V')≃Π(A2)。局所反射で根はalpha+beta,−beta、指数は1,1。元の生成元の作用係数は未計算。内部Ext_Πの二周期性をambient Extと混同しない。

## AOUのpointed比較：実際のrestrictionに対する条件付き結果

AOU §9の既知の導来同値と、我々が構造対象の保存を確認するための条件を区別する。実際のordered restrictionを(k_pi,U2,U1,O)とし、LA=U2(Σ_1^6 pi)、LB=U1(p1+p2+p3)が非自明な次数零線束となる条件(R)を明示する。未整合な印刷座標を自動代入して(R)を結論しない。次の「楕円境界データ」節にその理由を記す。

AOU (9.28)–(9.43)のmutationで標識構造対象の位置は9,9,9,6,6,3と移る。最後のL1L2の直前は(A,B,πF)。実際のrestrictionとAOU Proposition9.3によるforward RHom比較の下で、RHom(A,πF)=RΓ(LA^−1)、RHom(B,πF)=RΓ(LB^−1)。条件(R)なら両方零で、評価triangleの自然射からE0=πFが従う。これは実際のrestrictionを入力とする証明であり、K0一致からの推論ではない。

この条件付きpointed性の下で、自然な飽和F_n=Hom(πF,πF(n))と反Serre作用を用いF=R(e_AS,s_AS)を乗法込みで得る。条件付き相対版は相対Homのperfectnessと基底変更を仮定し、導来Nakayamaを使う。相対圏やheart全体の降下は別問題である。

## 標準三次曲面型における明示的な一致領域

完全な証明は `four_hearts_corner_locus.tex` の thm:eleven / thm:AOUexactlocus / cor:coefficientopen。別稿の有限corner判定は証明付きで比較稿へ統合してある。十一条件を独立に新発見したとはしない。この部分の全証明を今回再監査したという意味でもない。

W=Σw_abc[z_ca y_bc x_ab]、B=Jac(Q,W)、p=e_A0、C=B/BpB。道長とcut次数はell=3cut+lambda(end)−lambda(start)、lambda(A,B,C)=0,1,2で関係する。標準周期coverはAOUの無限quiverへreindexされ、qgr BcutがAS heartとなる。道長qgrそのものを同じheartにしない。

Cはw1bc,w2bcの十八係数にしか依存しない。いずれかが零なら三角閉路の全冪を残すk[t]表現がある。全て非零ならQ=(w2/w1)。C有限 iff Qの九つの2×2 minor、detQ、det Qentrywise-inverseが全て非零。minor零は2×2長方形支持の表現、det零はA1のrankを2にした表現で無限性を示す。十分性はP=(Qentrywise-inverse)^tと座標三点から一般位置六点を復元し、その可換cubicのrolled-up環の高次HomをOのorbit経由で因数分解する。これは全次数の幾何学的証明であり、C7の有限実験を一般パラメータへ外挿していない。

Qを[[1,1,1],[1,a,b],[1,c,d]]と正規化し、Δ=(a−1)(b−1)(c−1)(d−1)(a−b)(c−d)(a−c)(b−d)(ad−bc)*((a−1)(d−1)−(b−1)(c−1))*(bc(1−a)(1−d)−ad(1−b)(1−c))と置く。D(Δ)はM_cubic。八次元係数商トーラスから四交比トーラスへの写像はw0=w1=1,w2=Qという整数切断を持つ。従って有限corner係数開集合は非標準的にM_cubic×(Gm)^4。

有限cornerからBpの右pBp有限性とpBの左pBp有限性が道の分解で従う。B右noetherianならpBpも右noetherian。標準noetherian AS加群の有限projective解消とvery strong helixからExt^j(Ev,s^nM)=0（j>0,n≫0）を得る。実際の条件(R)の下でのAOUのpointed比較と合わせ、指定Ψのt-exactness iff 自然cornerのabel同値 iff C有限 iff 十八非零かつΔ≠0。逆向きはAS上のAZ生成を高次Homに適用し、全高次がBpBに入ることで証明する。

範囲外：全potentialのAS正則性・noetherian性、無限位数条件のZariski開性、Δ零の全点での実在負指数Rains根、任意の別abel同値の不存在、全相対stack降下。AOU birational対応の定義域で係数開集合の逆像が非空稠密開であることと、圏の定理の適用条件を別に記す。

## 自然関手の接続とEuler chamberによる選択

証明は `four_hearts_canonical_comparison.tex`、`four_hearts_root_chambers.tex`。VdB (9.5)とProposition9.2.3(1)によりRδ_*O_W=πF。target Serre=(-1)[2]と同値性から反Serre作用も保存する。pointedなdg同値のRHom右作用を、QGrのsection右随伴ωとπRω=Idで再構成すると、指定Rδ_*は自然な反標準導来切断と同型になる。ここでは環の同定を誘導されたものに固定し、単なるK0一致・次元一致を使わない。

同じ最終raw blow-upのRains実現はこれで接続する。AOU側に実際の条件(R)を加え、Δ≠0の適用域ではVdB/Rains–AS比較も単一HRS tilt。VdB Theorem9.1.9とProposition9.1.8により、torsionfree側kerδ_*と高次像は境界非交叉部分に入り、境界restrictionは保存される。境界非交叉部分によるabel商圏では既に同値である。この事実はVdBの既知結果を適用したもの。

Zの全cohomologyを持つambient三角部分圏D_Zは、反標準側の有限次元A=R/(g−1)cohomologyを持つ充満部分圏へ写る。内部Db(Z)やDb(mod_fd A)をambient圏と同一視しない。θ→Idが自然に同型なのでSerre=[2]となる。χ(e,Φ^−1 U)=dim Uは非零target対象で正。

T∩Zは全非零商Qでχ(e,Q)>0、F∩Zは全非零部分対象Nでχ(e,N)<0と同値。総Euler値やcomposition factorsの符号だけでは代用できない。証明はtorsion分解のT部分/F商を使うだけだが、全対象に有効な認識式となる。

有限ADE型のspherical simplesを持つ旧heartで、負の単純S_jを選び、F_j=add(S_j)、T_j=Hom(−,S_j)=0として〈S_j[1],T_j〉へ移る。隣接単純は0→S_j→P_i→S_i→0の非分裂拡大へ変わり、非隣接は不変、根類はs_j反射。有限長性は候補の有限filtrationとHom直交性から直接証明する。各段階でtarget振幅[0,1]を保つため、単純のEuler値は零にならない。負正根数は一つずつ減り、全単純が正になればtarget heartへの包含から一致を得る。終端heartは経路によらないが、経路の合成自己同値の同型は主張しない。

E6では辺03,12,23,34,45、旧指数(6,2,−1,3,2,4)。以下のRainsの有効単純根実在結果を全六根に適用し、Zの全単純を尽くす。α2を一度反射すると根はα0,α1+α2,−α2,α3+α2,α4,α5、次元は6,1,1,2,2,4となる。全有限次元simpleと二つのcharacterを決定する。一般E型でmod_fd A≃modΠ(E)という主張ではない。

## 全heartの局在と整数倍点の整列公式

`thm:globaldefect` は指定genuine gluing・q非torsionで全torsionfree部分F⊂Zを示す。Φi_*の境界上の同定からLi_R*Φ=Li_q*。M∈FをΦM=U[-1]と書き、両restrictionの振幅[-1,0]を比較するとi_R*U=0となる。有限生成graded代表MのM/gMが有限なら、高次でg:M_(n−1)↠M_n、次元の単調減少は停止するのでgはqgrで同型、局所化は有限次元。この補題でM∈Zを得る。従って全heartのt-exactness iff AZ ampleness iff 全Z単純のEuler正値である。数値共鳴とは同値でない。

Zの単純根が有限ADE型であることも既存の幾何仮定から示した（lem:finiteADEautomatic）。同根の異なる単純はEuler矛盾、根の有限性はH⊥の負定値性、独立性は正負係数を分けたx=yの交点x²≥0と有効錐のpointednessから従う。したがって局所Euler手順を適用するための有限ADE仮定はこの幾何範囲では自動。

全heartの単純tiltではZ'のSerre性をcohomology長完全列で保つ。次の残余torsionfree対象Xは、H^−1(X)[1]が標的H0(X)=0へ単射するため旧heartにも属し、旧Fの対象となる。この帰納法で残余の差は常にD_Z内にあり、局所手順の終了は全heartの一致を意味する（thm:globalADEtilts）。一回のHRS比較を複数の単純tiltに細分しているので、二つの回数概念を混同しない。

Rainsの実在入力（lem:Rains-simple-existence）：2022稿§4 pp34–35の指定blowdown単純根のq冪restrictionによる有効性と、2019稿§11 p141のProposition11.23直前の記述を使用する。後者は有効単純根Dそのものなら適切なdeterminantを持つD,χについて境界非交叉既約sheafが存在すると明記する。Proposition11.23自体のnef/fundamental条件を単純根に適用しない。任意の数値的共鳴根の実在を推論せず、固定heartの向き付きblowdown単純根に限定する。

p_i=N_iq、N_i相異なる正整数、3≤r≤8なら全根のrestriction指数は非零でgenuineとなる。根の直接列挙は差根、三点直線、六点conic、r8の(2,1,…,1)三次。各blowdown単純根に実在入力を適用することで全r単純を得る。Nをν1<…<νrと整列すれば、反標準側の全simpleはr個、次元(ν1+ν2+ν3,ν2−ν1,…,νr−ν_(r−1))。負単純手順は隣接逆転の交換となり、正の次数a>0の根は常に正なので回数はinv(N)。全heart一致 iff元の順序が昇順。

同じ無順序点集合ではcommutative Sとqと構造対象eが同じgluingを決めるので、導来圏と反標準環を共通に固定できる。二順序で前後が逆の点の差根は、一方で有効、他方で逆向きが有効となるため、heartが同じならpointed有効錐に反する。従って順序由来のr! heartsは同じ導来圏内で相異なる。抽象的abel非同値の分類ではなく、全heart数がr!とも言わない。

具体例はν=(1,2,3,5,7,11)、全simple次元(6,1,1,2,2,4)、一次元二個。元の順序(1,3,2,5,7,11)から一手、同無順序六点から720 hearts。全根の数値共鳴とAZ amplenessは昇順heartで両立する。明示行列やkernel生成元は未計算である。

## 楕円境界データ：確定した式と未確定の原典規約

証明は `four_hearts_boundary_data.tex`。原点o、t_a(x)=x+a、P_a=O(a−o)とする。次数dの線束Mにt_a^*はP_a^(−d)、t_(a*)はP_a^dをtensorする。pushforwardとpullbackを混同しない。

Rainsの基底(T_i=O_ei(−1),B2=O(−2h),B1=O(−h),e=O)は境界で(k_pi,L^−2q^−1,L^−1q^−1,O)となる。一般類の数値を(u,D,c)=(rank,c1,χ(e,−))とするとdetFq=ρ(D)q^(c−u)、rankFq=u。sは(u,D+uH,c+DH+ud)と作用する。従ってq=P_aの境界作用はΨ=t_(a*)(−⊗ρ(H))、ΨO=ρ(H)q^d。既知のtranslation-tensor型の中で支持とOの像を決めており、K0から任意の関手を同定したわけではない。

実際のrestriction tuple(U2,U1)からはq=U2 U1^−2、L=U1 U2^−1。境界へのforward RHomと合成がquasi-isomorphismならRains(4.11)のdirected dg模型でpointed復元ができる。必要な整合条件は、点支持がqのtranslationで動くことと、ΨO=U2^(d−3)U1^(3−2d)(−Σpi)。三次曲面ではΨO=U1^−3(−Σpi)。独立にOrlov Euler行列Cからs=(C^t)^−1 Cを計算すると、pt=B2−2B1+e、sT_i=T_i+pt、se=4e−3B1−ΣT_iで同じ条件を得る。

**共通座標での障害**：AOU v1 (9.47)をU2=L0^−5L1^3、U1=L0^−2L1、L1=σ*L0、σ=t_bとして読むと、Q=L1/L0=P_(−3b)、q=Q、L=L0³L1^−2。必要な境界translationはt_(−3b)、ΨO=L0³Q^−3(−Σpi)。一方(9.2),(9.3),(9.25)のshiftをσ_*³(−⊗N)、N=L0 σ*L0 σ²*L0(−Σpi)と同じ同定で読むと、translationはt_(3b)、ΨO=L0³(−Σpi)。前者にはQ²=O、後者にはQ³=Oが必要なのでQ=Oとなり、無限位数σでは両立しない。

これは原典全体の誤りを断定する結果ではない。逆同値、異なる境界同定、点のrelabeling、push/pull、または誤植のどれを修正すべきかは元の構成で未確定。今回の原稿はこの同時代入を取りやめ、AOUのpointed性と依存するt-exactnessを実際の条件(R)付きへ修正した。十一条件の純代数判定とRains単独の整列結果はこのAOU座標入力に依存しないが、保持した全証明を今回再監査したという意味ではない。

**境界作用から先に復元する候補**：実際のΨ=t_(a*)(−⊗N)と支持piが固定ならq=P_a、L³=N(Σpi)。L∈Pic³Eの九候補はE[3] torsor。印刷されたshiftを採る場合にはq=L0/L1、L=L1ε、U1=L0^−1ε^−1、U2=(L0L1)^−1ε^−2（ε∈E[3]）。この式は必要な整合的候補であり、(9.47)の確認済み訂正式ではない。実際のordered restrictionを確認すれば一つに決まる。同じ境界作用で九つのgluing圏が互いに同値とはしない。

## 次の核心

最優先はAOUの構成から実際のB1,B2のrestrictionと反Serre boundary shiftを同じ同定で再計算し、条件(R)の成立と上記九候補の選択を確定すること。式の矛盾を隠して辞書を完成したと報告しない。この作業の後で、十一因子の楕円パラメータ表示、実在AS領域、独立avatar同定、相対heartへ進む。Rains単独の実在・整列結果とVdBの抽象的pointed認識は保持する。

## 別稿との役割分担と保持する補足

`papers/cubic_heart_corner.tex` は11 determinant条件、一様C7=0、C6非零、Hilbert関数8+21t+33t²+38t³+33t⁴+21t⁵+8t⁶、総次元162を扱う。道長gradingと反標準cut gradingを確認して使う。本比較稿はこれらの詳細証明を未確認の全AS表示へ拡張しない。古典的11根壁のi_*O_D(−1)の導来的消失は `papers/sections/cubic_corner_root_walls.tex` に保持され、非可換壁上のheart存在とは別である。

`papers/nc_del_pezzo_resonance_hearts.tex` と `research/resonance_hearts.md` は全次数最大共鳴・整数格子とE[3]の九選択・既約根の一意性・zigzag形式性・固定dg圏のframed分枝を保持する。cubicの32個の5次元formal分枝を曲面モジュライの成分と呼ばない。本比較稿はこの詳細分類を証明の必須入力としないため、単独bundleに別稿全体を複製しない。

可換cubicでは四者がcohSを再構成するが、その一点の一致から非可換一致locusの開性は導かない。weak(-2)曲線のEuler零の不可視対象と、非零負指数が[-1]に残る現象は異なる。相対比較にはperfectness・基底変更・消滅の一様性・t構造の適合性・pointed descentが追加で必要。

## 先行研究との差分・検証範囲

主文献に加え、Bridgeland *Stability conditions and Kleinian singularities*, IMRN2009 no21,4142–4157, arXiv:math/0508257v3の§2とLemma3.5を一次PDF本文・ページ画像で照合した。内部Db(modΠ)とambient圏の区別、spherical twistとWeyl反射は既知入力・先行する機構である。Broomhead–Coelho Simões–Pauksztello–Woolf *Simple tilts of length hearts and simple-minded mutation*, Adv.Math.503(2026)111197, arXiv:2401.02947v3のTheorem2.7,Remark2.8を本文で確認し、TheoremAのページ画像も確認した。一般のsimple tiltの有限長性を自動としないことが重要で、本稿のrigid spherical場合は直接証明した。

VdB (9.5),9.1.8,9.1.9,9.2.3,11.1.1,11.1.3,11.2.1,11.2.4を関連本文で照合した。PDFページ画像の取得はCache missで失敗したので、その原典を画像で確認したとはしない。Rains2025 monographの全文取得は複数経路で成功せず、書誌・概要以上の新規性照合は未完了。VdBの有限長性/単純数、Bridgelandの一般機構を本研究の新規成果に数えない。

現行全文38ページ、95ラベル、13文献。六コードを現行入力で実行した。新コード `verify_four_hearts_boundary.py` は六次数の1587個のK0ベクトル、Euler行列からの反Serre作用、restriction determinant、支持と構造対象の二つの不整合、九つのE[3]候補を厳密整数・有理数で確認する。shared checkerは実際のU2,U1を指数基底とするよう変更し、原典の幾何学的非自明性を計算済みとしない。

従来の40,000通りのA2、576回のchamber、240組の整数列と全720順列、六点の普遍恒等式、QQ/有限体のcorner消去も再実行した。古いコードの固有versionタグは保持しているが、現行ソースで実行した出力である。有限算術は実在sheaf・heart同値・原典の修正式を証明しない。

今回の一次資料確認はAOU v1の(9.2),(9.3),(9.25),(9.47)をprimary HTMLで、Rains2022 v2の(4.4),(4.11)–(4.13)をPDF解析本文で行った。Rains原典ページ画像はweb screenshotがCache missで取得できず、画像確認済みとはしない。arXivで表示された版はAOU v1とRains2022 v2を確認した。Rains2025 monograph全文取得は今回も成功しなかった。外部査読・機械形式化・網羅的新規性確認は未実施。生成・組版・画像・清浄再現・遠隔保存はvalidationに分けて記す。GitHub保存成功時にLibraryへ別途保存しない。
