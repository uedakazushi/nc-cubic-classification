# 四つのheartの比較：現行研究ノート

2026-11-16 / hearts-v23。最初に `research/four_hearts_plan.md`（プロジェクト全体では `00_research_plan.md`）を読む。論文は `papers/nc_del_pezzo_hearts.tex` と八つの `papers/sections/four_hearts_*.tex`、検証は `research/four_hearts_validation.json`。本文の証明をここに重複させない。

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

## AOU型のpointed比較：actual条件と規格化した構成

一般のmutation比較は `four_hearts_as.tex` の実際のrestriction条件(R)の下で扱う。初期tupleは(k_pi,U2,U1,O)、必要条件はU2(D6)とU1(D123)が非自明な次数零線束であること。forward RHomと境界の同定を使い、最後の二つの左mutationが構造対象を変えないことを示す。K0やrestrictionだけの一致から対象の同型を推論しない。

右加群の初期平面shiftをVdB (5.4),§10に固定した場合は、下記の具体的な辞書とsheaf-normalized mutationで(R)を三条件(U+)から確認できる。得られる代数と関手はA+,Ψ+と書き、未変更の印刷されたdecupleから作る代数・関手と無条件に同一視しない。元の隣接交換の順序は保つが、右mutationのcone[-1]と途中の三つの[1]を明示する。

pointed同値によりF≃R(e_AS,+,s_AS,+)を乗法込みで得る。系cor:AOU-texactと十一条件の判定は、actual条件を満たしたこの指定Ψ+に適用する。標準AS周期表示の右noetherian性は依然として条件である。

相対版は、相対mutation列と二つの相対Homのperfectness・導来基底変更、各fiberでの(R)を仮定すれば導来Nakayamaで自然なE0≃eを得る。相対圏全体の存在やheart・markingの降下をこの対象単独の同定からは結論しない。

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

## 楕円境界データ：右規約での辞書と印刷式の区別

証明は `four_hearts_boundary_data.tex`。Rains型のrank u,c1=D,c=χ(e,x)についてdetFq(x)=ρ(D)q^(c−u)。q=P_aならFq s=t_(a*)(−⊗ρ(H))Fqであり、構造対象の像はρ(H)q^d。actual tuple(k_pi,U2,U1,O)からq=U2U1^−2、L=U1U2^−1を一意に復元する。forward RHomと合成を保つrestrictionを入力として、Rains (4.11)の三角dg模型を同定する。単なる数値復元とは違う。

**右加群の固定規約**：VdB (5.4)のN_τの作用はτ_*(−⊗N)、§10のo_Y(1)=L_σ。従ってS+(M)=σ_*(M⊗L0)、S+^−1(M)=σ*M⊗L0^−1。初期平面O(−1),O(−2)のactual restrictionはL0^−1,(L0L1)^−1である。VdB Theorem6.3.1(1),(4)と随伴からLj*Lα*=Lβ*Li*、Proposition9.1.8の(9.11)からLi*Rδ*=Rδ_E*Lj*を得る。各段階の境界同型で運ぶと最終Orlov tupleも同じであり、例外点はk_pi、構造対象はOとなる。

**確定した辞書（thm:right-dictionary）**：q=L0/L1、L=L1。σpiのL0一般位置はpiのL1一般位置に等しい。sourceのfull EC、AOU Proposition9.3のforward RHom比較、Rainsのdg復元により境界・構造対象を保つdg同値を得る。σ=t_bならq=P_(3b)、ρ(H)=L1³(−D6)であり、境界反Serreはσ_*³(−⊗L1³(−D6))と一致する。固定した初期twist U1=L0^−1が九候補L=L1εのε=Oを決める。

**印刷tupleとの整合検査**：S−(M)=L0⊗σ*MとすればS−^−1O=L0^−2L1、S−^−2O=L0^−5L1³であり、印刷式(9.47)を再現する。S−とS+を同じshiftとして扱うと点支持でQ²、構造対象でQ³の障害が残る。この具体的な説明は得たが、原典の全記号の正式な翻訳や著者訂正を確定したとはしない。本文ではS+を明記して構成を追う。

**cohomological shiftも明示**：L_EF=Cone(RHom(E,F)⊗E→F)、R_F^-E=Cone(E→RHom(E,F)^*⊗F)[−1]とする。点を線束の右へ動かすとR^-_M k_p=M(p)。次数−2線束MをOの右へ動かすと、0→M→O²→M^−1→0からR^-_O M=M^−1[−1]。従ってR6^-R7^-R8^-の後の末尾三対象に[1]を施す。以後これらは動かず、個別shiftはfullnessとexceptionalityを保つ。この指定列と、印刷されたmutation記号をshift確認なしに併用しない。

**actual decuple（prop:normalized-admissible）**：最終restrictionは(O,(L0L1)^−1(D6),L0^−1(D123);O(p1),O(p2),O(p3);L0(−p4),L0(−p5),L0(−p6))。相異なる六点に対してadmissibilityはO(D123)≠L0、O(D456)≠L1、O(D6)≠L0L1の三条件(U+)と同値。固定E,σ,L0では一般位置との共通部分が非空開である。非torsion条件自体をvarying familyの開条件とはしない。forwardの境界Ext消滅からfull strongとなり、AOU §7/§9の方法によりactual decupleのAS代数A+とΨ+を構成する。条件(R)も成立するのでpointedである。

**逆辞書（prop:inverse-decuple）**：based ordered decuple (O,A0,B0;K1,K2,K3;C1,C2,C3)からO(pi)=Ki、L0=K1K2K3/B0、O(p3+j)=L0/Cj、L1=O(D6)/(L0A0)、q=L0/L1。actual六点相異性とL1一般位置の範囲で正規化したforward constructionへ戻る。σ*L0=L1を解くと九つのσ、E[3] torsorを得る。これは入力にσがない逆辞書の曖昧さであり、σと初期twistを固定してε=Oを選んだ問題とは別。原点とline-classを固定したPicardパラメータで有限étale [3]引戻しとなるが、全moduli stackの九対一同型ではない。

**整数倍点との接続**：pi=Ni a、q=P_a、L1=O(3o)、L0=L1q、3b=aのσ=t_bを取る。三比はq^(N1+N2+N3−1)、q^(N4+N5+N6)、q^(ΣNi−1)で全て非自明。正整数倍点の既存共鳴例の全順序が正規化した許容decupleに入る。ここからΔ非零、標準AS noetherian性、各順序AS heartの相互同定を自動的に結論しない。

## 次の核心

右規約を固定した実際の構成の辞書、九候補εの選択、mutationのshiftと三条件、decupleの逆復元は完了した。次はactual normalized decupleのpotentialを計算し、十一因子の楕円表示とAS/noetherian適用域を決める。特に整数倍点例にΔを直接適用し、Rains順序heartの整列とAS+側の一致領域を同じ座標で比較する。U+だけからΔ≠0を推論しない。

変更のない印刷AOU表示への全記号の翻訳は別課題である。今回定義したΨ+の結果をそのまま印刷代数の同じ係数へ移さない。相対kernel・基底変更・標識とheartの降下、Rains2025全書との新規性照合、元のアフィン生成元の作用係数も残る。

## 別稿との役割分担と保持する補足

`papers/cubic_heart_corner.tex` は11 determinant条件、一様C7=0、C6非零、Hilbert関数8+21t+33t²+38t³+33t⁴+21t⁵+8t⁶、総次元162を扱う。道長gradingと反標準cut gradingを確認して使う。本比較稿はこれらの詳細証明を未確認の全AS表示へ拡張しない。古典的11根壁のi_*O_D(−1)の導来的消失は `papers/sections/cubic_corner_root_walls.tex` に保持され、非可換壁上のheart存在とは別である。

`papers/nc_del_pezzo_resonance_hearts.tex` と `research/resonance_hearts.md` は全次数最大共鳴・整数格子とE[3]の九選択・既約根の一意性・zigzag形式性・固定dg圏のframed分枝を保持する。cubicの32個の5次元formal分枝を曲面モジュライの成分と呼ばない。本比較稿はこの詳細分類を証明の必須入力としないため、単独bundleに別稿全体を複製しない。

可換cubicでは四者がcohSを再構成するが、その一点の一致から非可換一致locusの開性は導かない。weak(-2)曲線のEuler零の不可視対象と、非零負指数が[-1]に残る現象は異なる。相対比較にはperfectness・基底変更・消滅の一様性・t構造の適合性・pointed descentが追加で必要。

## 先行研究との差分・検証範囲

今回の直接入力はVdB (5.4)、§10冒頭、Theorem6.3.1(1),(4)、Proposition9.1.8/(9.11)、Proposition9.2.3、§11.1、AOU §3.5、Definition7.1、Lemma7.4とその後、Proposition9.3、(9.24)–(9.43)、Rains2022 (4.4),(4.11)–(4.13)。関連本文を一次HTML/PDF解析本文で照合した。VdBおよびRainsのweb PDF screenshotはCache missで失敗したため原典ページ画像を確認したとはしない。AOU arXivの取得した版情報はv1であり、正式な修正版や著者の訂正を確認したとは報告しない。

この正規化と順逆辞書はVdBのbimodule、既知のblow-up/section比較、AOUのmutation/AS構成、Rainsの三角dg復元を結び付けた帰結として書く。これらの一般理論を新規成果としない。Rains2025 monograph全文との網羅的照合は未完了。VdBの有限長性、BridgelandのADE反射、BCPWの単純tiltの既知入力も保持しており、今回それら全証明を新たに再監査したという意味ではない。

現行全文41ページ・109ラベル・13文献。六つの検算を実行した。新たな境界検査は325個の形式線束上のshift/inverse、符号付きrank・Picard exponentによるmutation列、末尾三対象の[1]、九候補からの唯一のε=0、逆decupleのround-trip、具体六点の全720順序での三条件を検査する。既存の1587数値類、六根系576chamber手順、240整数列と720整列順序、40,000混合A2、普遍六点恒等式とQQ/有限体corner消去も再実行した。数値検査でfull strong性・sheaf実在・dg同値・原典の正式訂正を証明したものではない。

全文の組版・画像確認・清浄ディレクトリ再現・遠隔保存はvalidationで別々に記す。外部独立査読・機械形式化・網羅的新規性確認は未実施。GitHub保存成功時にLibraryへ別途保存しない。
