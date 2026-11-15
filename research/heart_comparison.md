# 非可換del Pezzo曲面のheart比較：現行研究ノート

2026-11-16 / hearts-v16。最初に `00_research_plan.md` を読む。共通比較の証明は `papers/nc_del_pezzo_hearts.tex`、共鳴と大域比較の証明は `papers/nc_del_pezzo_resonance_hearts.tex`、詳細な現行知識は `research/resonance_hearts.md`。対象は全次数、最初の実行対象はcubic surface（次数3）。

## 指定genuine楕円gluingの大域比較

**滑らかな可換genuine del Pezzo S、滑らかなE∈|−K_S|、q∈Pic0(E)からのRains gluingでは、自然Φ=πRΓ*は全qでDb(Rains heart)≃Db(qgr R)となる。** 既存 `papers/dp1_anticanonical_models.tex` の証明について、orbitのInd生成、実際の境界拡大による非零trace、有限/無限位数の両方での環の有限性、source飽和性を点検した。再構成した証明と入力は `papers/sections/resonance_global_heart.tex`。異なるqの圏どうしを同値とする主張ではない。

さらにH=−KがnefなRains heartの全対象Mについて、ΦMの振幅は[0,1]である。Mをline bundleの有限直和の商とし、Ext2(e,τ^nM)=Hom(M,θ^(n+1)e)*をn≫0で消す。T=ker H1Φ、F=ker H0Φは全heart上のtorsion pairで、反標準heartの引戻しは〈F[1],T〉。q非torsionでは境界外Serre部分圏Zにも制限し、T∩Z=ker Ext1(e,−)、F∩Z=ker Hom(e,−)。全任意nc del Pezzo、特異境界、weak avatar、非局所自由gluingやfamily降下はこの定理の範囲外。

VdB/AS heartとの指定同定は未解決である。今回の全Rains–反標準比較から、既知VdBの各段階の比較関手やAOUのmutation後の構造対象を自動的に同定しない。

## 共鳴での符号別比較と最大根配置

Rainsの境界非交叉な既約root sheaf M、alpha²=−2、m=chi(e,M)に対して、全tau-orbitでHom=max(m,0)、Ext1=max(−m,0)、Ext2=0。根sheafは2-spherical。Φはm>0でm次元A=R/(g−1)加群を次数0へ、m<0で(−m)次元加群を[-1]へ送り、m=0なら消す。負指数ではRains heartのAZ amplenessが失敗し、pointed anticanonical heartと一致しない。指定genuine gluingでは、このheart変化は導来同値を保つ。Hilbert値1+d n(n+1)/2は不変で、genuine avatarには零指数根共鳴がない。

正負各指数の共鳴は滑らかな楕円blow-up chartでそれぞれZariski dense。固定E・非torsion q、p_i=N_iq（相異なる正整数、r=9−d）で全根が非零指数で同時共鳴する。d=6,…,1の根数は8,20,40,72,126,240。単純根整数指数とE[3]の9通りから全共鳴配置を復元する。全モジュライの全成分での密度ではない。

最大共鳴で全単純根sheafが実在すれば、他の根類の既約sheafはなく、各単純根sheafはq非torsionで一意。直和のExtはDynkin zigzag、Liu–Wangの既知形式性から固定dg圏のframed変形は辺ごとのx_ij*x_ji=0となる。cubicでは32個の5次元formal分枝（gauge商前）。曲面の相対モジュライではない。

## 境界外圏と任意混合指数のA2

Z={M | dimM≤1,Li^*M=0}でV0,V1は有限次元A加群となり、短完全列は6項A線型完全列を誘導する。q非torsion、Hnef、H²>0ならZは有限長Serre部分圏である。零次元の境界外対象・商はdeterminant q^ellから排除され、既約境界外root sheafは全heartで単純となる。既約性だけから全射性を推論するものではない。

隣接根S+,S−の指数p>0,−n<0について、非分裂P:0→S−→P→S+→0のconnecting rankはmin(p,n)と証明した。非零e→Pがあれば全射であり、rank-one torsion-free核LのExt2(e,L)=0からh1(P)=0を得る。p>nではこれが起こり、p≤nではEuler値からHom(e,P)=0になる。この証明は導来比較に依存しない。Lがline bundleになるのはp−n=1だけである。

C=〈S+,S−〉_Serre≃mod_fd Π(A2)、直既約はS+,S−,P,Q（逆向き非分裂拡大）。cohomologyは(p,0),(0,n),((p−n)+,(n−p)+),(p,n)。quiver頂点次元a,b、一方の矢のrank tに対しh0=pa−min(p,n)t、h1=nb−min(p,n)t。p>nでは(T,F)=(add(S+,P),add(S−))、p<nでは(add(S+),add(S−,P))。p≠nで非零対象は消えず、p=nの仮想場合では核add(P)となる。genuine avatarでは隣接する等しい反対指数が零指数根を生むため存在しない。

内部Ext_Cは二周期で高次にも残るがambient Ext>2は零であり、Db(C)→Db(Rains heart)は完全忠実でない。Euler指数だけで非既約対象のheart位置は決まらず、P,Qが同じEuler値を持つことが具体例である。

## 二つのcharacterと四次元アフィン商

指数+2/−1では0→W→V→U→0（次元1,2,1）が非分裂でW≄Uとなる。導来比較によりHom_A(W,U)=Ext1_X(P,S−)=0、包含S−→Pが非零の加群拡大へ移ることを使う。Vへの作用像は全三角行列代数で、Hom_A(V,U)=k。これは必要条件のままではなく、指定genuine gluingで成立を証明した結果である。

逆向き非分裂拡大V'を合わせるとA/Ann(V⊕V')≃Π(A2)。二characterのSerre部分圏はmod_fd Π(A2)で、四つの直既約W,U,V,V'を持つ。根類alpha+beta,−betaと指数1,1はbetaの局所Weyl反射で得られる。全E6 heartが一反射で記述できるという意味ではない。商の内部Extとambient Extは異なるため、この商はhomological epimorphismでない。

**未計算**なのは、元の楕円データに対するAの生成元のcharacter値・非対角係数とkernelの生成元である。同型型の決定と係数式の計算を区別する。次はこの商の具体式、全E6の作用、VdB/ASとの指定同定、相対familyと退化境界を扱う。

## 比較の共通枠組みと一次資料

Rains heart、VdB heart、AS heart、anticanonical heartの四名称は由来を表し、四つが相異なるとも一致するとも仮定しない。VdB literal blow-upとsection-model qgrも自動的に同じではない。入力データの対応と指定導来同値を先に固定し、その後t-exactness、構造対象、反Serre、境界、rank、marking、族の降下を個別に確認する。

VdBの図式X_j ←α_j− tilde X_j −δ_j→ X_(j+1)で、αはblow-up、δはsection-algebra比較。σp_iが指定平面埋込みで一般位置ならThm11.1.3はRδ_*とLδ*の逆同値とheart振幅[0,1],[-1,0]を与え、coherent bounded保存にはLemma9.1.5も使う。cubicはX_7=Proj F。Ch12のF=P/(C3)表示は一般位置条件なしにも存在するので、表示だけから導来同値を使わない。Rem12.0.5はraw反復と各段階section-modelへの取り替えを区別する。

AOU arXiv:2404.00175 §9はcoh tilde X=qgr Fから始める。滑らかな楕円、次数3線束、無限位数σ、sufficiently general六点の設定で、Lemma9.2はSerre=(-1)[2]、Thm9.4はDb qgr F≃Db qgr A。左辺をraw blow-up heartと呼び替えず、abelian同値とも読まない。(9.44)は可換mutation表示で、その直後に非可換collectionを同じ記号で定義し直す。実際の先頭E0はO(0,0)へ移るが、E0≃πFは対象として確認する必要がある。K0や境界restrictionの一致だけでは不足。

OU arXiv:2508.04986 Def1.1,§6はAS heartと標識、一般幾何的blow-upとの導来比較を扱い、全パラメータheart一致ではない。Rains 2019 Introduction,§4も既存abelian構成を用いてrealizationを正当化しており、任意の抽象gluingのfaithful heart存在を無条件には与えない。

## 形式的帰結と適用範囲

**振幅1のHRS比較**（heart原稿§3）：F:Db(A)≃Db(B)、F(A)⊂D^[0,1](B)、G(B)⊂D^[-1,0](A)ならT=ker H1F、U=ker H0Fはtorsion pair、G(B)=〈U[1],T〉、Fがt-exact iff U=0。VdBではT_j=ker R1δ_j*、U_j=ker δ_j*。非零M∈U_jもRδ_j*M=(R1δ_j*M)[−1]≠0で、heartからの消失と導来的消失は異なる。既知HRS理論の適用である。

**ample orbit一意性**（§4）：faithful bounded heart、tauのheart保存、AZ amplenessと全対象の高次Extの一様tail消滅の下で、heartはHom(e,tau^nX[i])=0（i≠0,n≫0）で一意。高次消滅をAZ二公理だけから導かない。

**固定対象のEuler障害**（§4）：上のheartの非零tau固定対象はchi(e,M)>0。別heartの実在固定対象のchi≤0で非一致を検出する。周期rではresidue和の正性だけ。数値共鳴だけから存在を補わない。

**corner判定**（§5）：必要な左右有限性・noetherian性の下でqgr B→qgr eBeが同値 iff dim B/BeB<∞。AS helixのfoldingとbimodule有限性を照合した範囲に限る。有限次数実験やHilbert級数一致だけでは不足。

## 古典的根壁とcubicでの着手

弱del Pezzoの(-2)曲線D上のF=i_*O_D(−1)は2-sphericalで全反標準orbitに直交し、反標準収縮で消える。AZ生成性失敗とDb(coh S)≄Db(qgr反標準環)を得る。十一のcubic根壁と一壁の節点三次の有理例は `papers/sections/cubic_corner_root_walls.tex`、`verify_cubic_root_wall.py`。非可換壁上のheart存在やt-exactnessとは別であり、HRS tiltは初めから導来同値を仮定する。

cubicでは最後のVdB段階Rδ_6*のker δ_6*を実在対象で求める。AOU九対象とmutationを追ってE0とπF、反Serre、境界を照合しcorner有限性を使う。今回のRains–反標準の一回のtiltから、VdB六段の合成が同じ指定関手だと無条件に結論しない。有限位数、特異境界、非局所自由gluing、他次数へは適用条件を保って進む。

初期exact検算ではAOU九線束のEuler行列は対角I3・隣接J3・離れたblock2J3の上三角、総和45、det1。C^−1 C^tの逆がH twist、E6は72根、H²=3。反標準Euler値n=0,…,8は1,4,10,19,31,46,64,85,109。再現は `python3 computations/verify_cubic_heart_numerics.py`、`latexmk papers/nc_del_pezzo_hearts.tex`。有限検算はeffective root、strong性、heart同値の証明ではない。

## 文献・検証範囲

Van den Bergh, *Blowing up of non-commutative smooth surfaces*, arXiv:math/9809116v1：Lemma9.1.5、Def11.1.2、Thm11.1.3、Ch12、Rem12.0.5。AOU, *Compact moduli of marked noncommutative cubic surfaces*, arXiv:2404.00175v1：§4.1、§9、Lemma9.2、Thm9.4、(9.44)直後、(9.54)–(9.57)。Okawa–Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, arXiv:2508.04986v1：Def1.1、Def3.1、§6。Chen–Han–Zhou, *Derived equivalences via HRS-tilting*, Adv.Math.354(2019),106749、arXiv:1804.05629v2：ThmA,B、§§2–3。Rains二論文、RSS Prop2.4、YZ Th4.5/5.1/5.13、Orlov Th3.18/3.25/Cor3.19の精密な監査箇所は共鳴ノートとvalidationを参照する。

今回の更新二節は独立LuaLaTeX driverで9ページに組版・画像確認し、新コードを40,000通りの厳密有理数計算で実行した。主原稿全文の組版、旧コード全再実行、独立査読・網羅的新規性調査は未実施。原典は解析本文で照合したがweb PDF screenshotはCache missで取得できなかった。詳細は `research/resonance_hearts_validation.json`。
