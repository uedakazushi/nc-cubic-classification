# 四つのheartの比較：現行研究ノート

2026-11-16 / hearts-v19。最初に `research/four_hearts_plan.md`（プロジェクト全体では `00_research_plan.md`）を読む。論文は `papers/nc_del_pezzo_hearts.tex` と五つの `papers/sections/four_hearts_*.tex`、検証は `research/four_hearts_validation.json`。本文の証明をここに重複させない。

## 比較対象と主張の水準

VdBはliteral/raw blow-upのcoherent heart、Rainsは指定blowdown/gluingのt構造、anticanonicalは指定eとs=S^−1[2]のorbit環のqgr、ASはAS正則三次元Z-algebraのqgr。名称が四つの異なる圏を意味するわけではない。ASのhelix全体と一頂点の反Serre orbit、AS正則三次元とambient AS4、Z-algebraと一周期graded algebraを分ける。

有界heartの存在はDb(heart)のrealization同値を含意しない。pointed同値には構造対象とsへの両立同型が必要で、境界・rank・marking・相対降下はさらに別である。右加群の積はab=s^(deg b)(a)∘b。

## 現行論文に収めた確定結果

**VdB–Rains（定理4.1、thm:RV）**：同じ初期heart・blow-up中心・gluing bimodule・blow-down関手を同定し、Rains Lemma4.9/Proposition4.17のpseudo-canonical認識を使う。全整数ellについてRα_*θ^ell Mが非負にあることが上のt構造を決めるため、誘導同値はt-exactとなる。独立なavatar間のパラメータ対応はこの定理に含まれない。

VdBの図式X_j←tilde X_j→X_(j+1)で左はblow-up、右δはsection model。Definition11.1.2の一般位置条件下のTheorem11.1.3とLemma9.1.5はRδ_*の振幅[0,1]と導来同値を与える。T=ker R1δ_*、F=ker δ_*、輸送heart=〈F[1],T〉。Chapter12のF=P/(C3)表示は同じ一般位置条件なしにも存在するので、表示の範囲を導来比較へ広げない。Remark12.0.5のraw/sectionの区別を保つ。

**Rains–反標準（定理5.2、5.4）**：genuine smooth classical del Pezzo S、smooth E∈|−K_S|、q∈Pic0(E)の指定gluingが範囲。全qで自然Φ=πRΓ*はdg導来同値。証明はIndでのorbit生成、境界自己拡大を追ったtraceの非零性、sourceのsmooth proper性と飽和性による右随伴と全射性。target smoothnessを前提にしない。無限位数にはRSS Proposition2.4（degree1も許す）、有限位数にはYZのPI・中心持上げ・χの三定理を使う。

HnefのRains heartで全対象のExt2(e,s^nM)はn≫0で消える。従って全heartの振幅[0,1]、T=ker H1Φ、F=ker H0Φによる一回のHRS tiltとなる。q非torsionなら境界外有限長Serre圏Zへ制限され、T∩Z=ker Ext1(e,−)、F∩Z=ker Hom(e,−)。一般対象に生のExt消滅を同一視しない。

**共鳴（定理6.1、系6.2）**：rho(alpha)=q^(−m)は数値条件。実在する境界非交叉既約root sheafではh0=max(m,0)、h1=max(−m,0)、h2=0で2-spherical。負指数はAZ生成性失敗と自然Φの非t-exactnessを検出するが、上記gluingで導来同値は保たれる。数値的ample coneとAZ条件は定義が違う。正指数根だけからAZ失敗とは言えず、負指数根が見つからないだけでF=0とも言えない。pointed heart非一致を抽象的abel非同値に強めない。

**AS–反標準（cor:ASac、cor:AOU-texact）**：AS helixのfoldingでqgrBを得てe=πpB、pBp=R(e,s)を同定した上で、B,R右noetherian、Bp右R有限、pB左R有限を要求する。この範囲で自然cornerがabel同値 iff dim B/BpB<∞。有限次数の消滅を使うには次数1生成等のtail制御が必要。相対有限cornerの開性はcoherent各次数の基底変更適合を明示した命題prop:relativecornerであり、heartの相対同値を意味しない。

**混合A2（§9）**：指数p,−nの隣接単純根の非分裂拡大Pのconnecting rankはmin(p,n)。C=〈S+,S−〉_Serre≃mod_fd Π(A2)、直既約S+,S−,P,Qで、cohomologyは(p,0),(0,n),((p−n)+,(n−p)+),(p,n)。両chamberのtorsion pairを得る。p=nはgenuine avatarに実在しない。指数+2/−1のアフィン側では異なる一次元W,Uと非分裂二次元Vがあり、逆向きV'を合わせてA/Ann(V⊕V')≃Π(A2)。局所反射で根はalpha+beta,−beta、指数は1,1。元の生成元の作用係数は未計算。内部Ext_Πの二周期性をambient Extと混同しない。

## AOUのpointed比較

AOU §9は最初からcoh tilde X=qgr Fである。smooth elliptic、degree3線束、無限位数σ、sufficiently general六点とadmissibilityが範囲。Lemma9.2はSerre=(-1)[2]、Theorem9.4はDb qgr F≃Db AS。本稿の `thm:AOU-pointed` ではmutation後先頭E0≃πFを実際の評価triangleにより同定した。

AOU (9.28)–(9.43)のτ1,…,τ6で、πFの位置は9,9,9,6,6,3と移る。右mutationは右側の対象を変えずに移動し、それ以外の操作はその位置に触れない。従ってτ6の先頭は(A,B,πF)。最後のL1L2にだけπF自身のmutationがある。

(9.52)のrestrictionはLA=L0^(−5) L1^3 O(p1+…+p6)、LB=L0^(−2)L1 O(p1+p2+p3)、Li*πF=O_Y。LA,LBの次数は零で、Definition7.1と(9.53)により双方非自明。Proposition9.3が全RHom(A,πF),RHom(B,πF)をそれぞれRΓ(LA^−1),RΓ(LB^−1)と同定する。楕円曲線上の非自明次数零線束の全cohomologyは零なので、最後の二評価triangleの自然射が同型となる。K0またはrestrictionの一致だけから対象を同定してはいない。

**環の接続（cor:AOU-ring）**：中心正則一次元と正次数境界のH1消滅からF_n→Hom(πF,πF(n))が全n≥0で自然に同型となる。pointedなΨと整合的に反復した反Serre同型によりF≃R(e_AS,s_AS)が乗法込みで従う。これはAS標準heartがqgr Fに無条件で一致するという主張ではない。

**条件付きの相対同定（prop:AOU-relative-object）**：相対mutation列とeが存在し、二つの相対Homがperfectで導来基底変更に適合し、各fiberが上の許容条件を満たすなら、導来Nakayamaで二Homは零。評価triangleの自然射がE0≃eを族として与える。この対象の同定のためのfiberごとの任意なスカラー選択は不要だが、相対圏と全heartの構成・降下は別である。

## 標準三次曲面型における明示的な一致領域

完全な証明は `four_hearts_corner_locus.tex` の thm:eleven / thm:AOUexactlocus / cor:coefficientopen。別稿の有限corner判定を今回再点検して比較稿へ統合した。十一条件自体を今回初めて発見したとはしていない。

W=Σw_abc[z_ca y_bc x_ab]、B=Jac(Q,W)、p=e_A0、C=B/BpB。道長とcut次数はell=3cut+lambda(end)−lambda(start)、lambda(A,B,C)=0,1,2で関係する。標準周期coverはAOUの無限quiverへreindexされ、qgr BcutがAS heartとなる。道長qgrそのものを同じheartにしない。

Cはw1bc,w2bcの十八係数にしか依存しない。いずれかが零なら三角閉路の全冪を残すk[t]表現がある。全て非零ならQ=(w2/w1)。C有限 iff Qの九つの2×2 minor、detQ、det Qentrywise-inverseが全て非零。minor零は2×2長方形支持の表現、det零はA1のrankを2にした表現で無限性を示す。十分性はP=(Qentrywise-inverse)^tと座標三点から一般位置六点を復元し、その可換cubicのrolled-up環の高次HomをOのorbit経由で因数分解する。これは全次数の幾何学的証明であり、C7の有限実験を一般パラメータへ外挿していない。

Qを[[1,1,1],[1,a,b],[1,c,d]]と正規化し、Δ=(a−1)(b−1)(c−1)(d−1)(a−b)(c−d)(a−c)(b−d)(ad−bc)*((a−1)(d−1)−(b−1)(c−1))*(bc(1−a)(1−d)−ad(1−b)(1−c))と置く。D(Δ)はM_cubic。八次元係数商トーラスから四交比トーラスへの写像はw0=w1=1,w2=Qという整数切断を持つ。従って有限corner係数開集合は非標準的にM_cubic×(Gm)^4。

有限cornerからBpの右pBp有限性とpBの左pBp有限性が道の分解で従う。B右noetherianならpBpも右noetherian。標準noetherian AS加群の有限projective解消とvery strong helixからExt^j(Ev,s^nM)=0（j>0,n≫0）を得る。AOUのpointed比較と合わせ、指定Ψのt-exactness iff 自然cornerのabel同値 iff C有限 iff 十八非零かつΔ≠0。逆向きはAS上のAZ生成を高次Homに適用し、全高次がBpBに入ることで証明する。

範囲外：全potentialのAS正則性・noetherian性、無限位数条件のZariski開性、Δ零の全点での実在負指数Rains根、任意の別abel同値の不存在、全相対stack降下。AOU birational対応の定義域で係数開集合の逆像が非空稠密開であることと、圏の定理の適用条件を別に記す。

## 次の核心

同じ楕円データでVdB最後のδとRains自然Φのkernelまたはgluing moduleを同定し、構造対象・境界の保存を確認する。AOUの構造対象と標準三blockのt-exactness判定は済んでいる。楕円パラメータ上の十一因子の式、退化点とAS admissibilityの交叉、標準表示外・noetherian未確認域、相対heart・標識降下を進める。混合A2では商の元の生成元に対する係数が残る。

## 別稿との役割分担と保持する補足

`papers/cubic_heart_corner.tex` は11 determinant条件、一様C7=0、C6非零、Hilbert関数8+21t+33t²+38t³+33t⁴+21t⁵+8t⁶、総次元162を扱う。道長gradingと反標準cut gradingを確認して使う。本比較稿はこれらの詳細証明を未確認の全AS表示へ拡張しない。古典的11根壁のi_*O_D(−1)の導来的消失は `papers/sections/cubic_corner_root_walls.tex` に保持され、非可換壁上のheart存在とは別である。

`papers/nc_del_pezzo_resonance_hearts.tex` と `research/resonance_hearts.md` は全次数最大共鳴・整数格子とE[3]の九選択・既約根の一意性・zigzag形式性・固定dg圏のframed分枝を保持する。cubicの32個の5次元formal分枝を曲面モジュライの成分と呼ばない。本比較稿はこの詳細分類を証明の必須入力としないため、単独bundleに別稿全体を複製しない。

可換cubicでは四者がcohSを再構成するが、その一点の一致から非可換一致locusの開性は導かない。weak(-2)曲線のEuler零の不可視対象と、非零負指数が[-1]に残る現象は異なる。相対比較にはperfectness・基底変更・消滅の一様性・t構造の適合性・pointed descentが追加で必要。

## 先行研究と検証上の限界

論文末尾に11件の書誌・識別子・使用箇所を収録した。Rains2019のblow-up/t構造、Rains2022の共鳴とtrace、VdB §11–12、AOU §9、OUのAS定義、CHZのrealization、RSS/YZ/Orlovの有限性・飽和性が主要入力。Rains2025 monographの書誌と概要を確認したが、全定理番号対応と全内容の新規性照合は未完了。

今回、全文をLuaLaTeXで25ページに組版し、全ページのレンダリングを点検した。61ラベルと11引用キーの整合を検査し、数値コード三つを再実行した。40,000通りの混合A2検算に加え、AOUの標識対象の位置9,9,9,6,6,3,1と最後の二Hom消滅入力、restrictionの形式指数と次数零を検査した。線束の幾何学的非自明性や対象の同型を数値コードで証明したわけではない。

今回の追加証明ではAOUの§4、§8のpotentialとrolled-up同定、係数商、OU Definition3.1、(3.9)–(3.10)、Remark5.4を一次本文で照合した。OUの該当ページ画像も確認した。AOUの構造対象の証明は既存の一次HTML確認を保持し、今回独立に全て再監査したとはしない。既存のRains入力の確認を保持するが、保持した全証明・全文献を今回再監査したとはしない。2025年monographの全内容との新規性照合、外部独立査読、機械形式化は未実施。生成・再現・遠隔保存の状態はvalidationを参照する。Libraryへの別途保存は行っていない。

新コード `computations/verify_four_hearts_corner.py` は、六つの普遍恒等式をZ上で検査し、指定WのHilbert値(8,21,33,38,33,21,8,0)をQQとF_1000003の別消去で確認する。7次は21endpoint blocks、総6804列。rank2障害Q0=[[3,4,5],[5,6,7],[7,8,9]]は九minor非零だがdet0、逆数行列式1/198450。逆数を2520倍したQ1も九minor非零だが逆数行列式0であり、最後の二条件は省けない。係数重み階数は27係数で19、18係数で14、四交比と切断の整数pairingはI4。これらは具体算術・恒等式検証であり、noetherian性やsheaf存在の計算証明ではない。
