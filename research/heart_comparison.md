# 非可換del Pezzo曲面のheart比較：現行研究ノート

2026-11-15 / hearts-v15。最初に `00_research_plan.md` を読む。共通比較の証明は `papers/nc_del_pezzo_hearts.tex`、共鳴の証明は `papers/nc_del_pezzo_resonance_hearts.tex`、詳細な現行知識は `research/resonance_hearts.md`。対象は全次数、最初の実行対象はcubic surface（次数3）。

## 共鳴での現在の比較結果

Rainsの境界非交叉な既約root sheaf M、alpha²=−2、m=chi(e,M)に対して、全tau-orbitでHom=max(m,0)、Ext¹=max(−m,0)、Ext²=0。根sheafは2-spherical。自然導来切断Phiはm>0でm次元A=R/(g−1)加群を次数0へ、m<0で(−m)次元加群を[-1]へ送り、m=0なら消す。負指数ではRains heartのAZ amplenessが失敗し、pointed anticanonical heartと一致しない。これは抽象的導来非同値やqgr特異化を意味しない。反標準Hilbert値1+d n(n+1)/2は不変。genuine smooth classical avatarでは零指数根共鳴はない。

正負各指数の共鳴は滑らかな楕円blow-up chartでそれぞれZariski dense。さらに固定E・非torsion q、p_i=N_iq（相異なる正整数、r=9−d）で全根が非零指数で同時共鳴する。d=6,5,4,3,2,1の根数は8,20,40,72,126,240、単純根整数指数とE[3]の9通りから全共鳴配置を復元できる。全モジュライの全成分での密度ではない。

最大共鳴で全単純根sheafが実在すれば、他の根類の既約sheafは存在せず、各単純根sheafはq非torsionで一意。直和のExtはDynkin zigzag、Liu–Wangの既知の形式性から固定dg圏のframed変形は辺ごとのx_ij*x_ji=0で決まる。cubicでは32個の5次元formal分枝（gauge商前）。曲面の相対モジュライではない。

## 境界外圏と混合A2の局所heart比較

Z={M | dim M≤1, Li^*M=0}で自然Phiの振幅は[0,1]。V0,V1は有限次元A加群で、短完全列は6項A線型完全列を誘導する。一般の混合拡大0→M−→M→M+→0はconnecting δのrank rによりh0=m+−r、h1=−m−−r。隣接根の等しい反対指数はgenuine avatarで根の和が零指数になるため同時共鳴不可。weak del PezzoのEuler列による完全相殺は古典模型であってgenuine非可換の存在例ではない。

**非torsionかつH=−K nef、H²>0ではZが有限長Serre部分圏であることを証明した。** 零次元の境界外対象・商はrestriction determinant q^ellから排除される。従って既約境界外root sheafは全heartの単純対象である。部分商のH次数とthetaの数値作用、Rains Cor7.7でSerre性、Prop7.32で有限長性を得る。これは「既約性だけなら非零e→Mは全射」という誤った推論とは異なる。

**混合A2のconnecting rankは解決済み**：隣接根S+,S−の指数p,−(p−1)、p≥2について、非分裂拡大0→S−→P→S+→0はeの商で、その核はRains Prop10.13の等号条件によりline bundle。従ってh0(P)=1,h1(P)=0、rank δ=p−1。具体例N=(1,3,2,5,7,11)の指数+2,−1ではrank δ=1。全q導来同値は入力にしていない。

C=〈S+,S−〉_Serre≃mod_fd Π(A2)の直既約はS+,S−,P,Q（逆向き非分裂拡大Q）の四つ。cohomologyはそれぞれ(p,0),(0,p−1),(1,0),(p,p−1)。T=add(S+,P)、F=add(S−)がC上のtorsion pairで、PhiはCの非零対象を消さない。これは全Z・全heartのtorsion pairを証明したものではない。内部Ext_Cは二周期で高次にも残る一方、ambient Ext>2は消えるため、Db(C)→Db(Rains heart)は完全忠実でない。

**導来比較に残る具体的テスト**：p=2で0→W→V+→V−→0（両端1次元）が存在する。Hom_A(V+,V−)はrepeated scalar V+≅V−²のみ次元2、それ以外は1。全三角圏上の完全忠実性には、WとV−のcharacterが相異なり、加群拡大が非分裂であることが必要。そのとき作用の像は全三角2×2行列代数。実際のcharacterと非対角作用は未計算。この必要条件は十分条件とは未証明。証明と再現は `papers/sections/resonance_mixed_a2_category.tex`、`computations/verify_resonance_mixed_a2.py`。

## 目標と比較の共通枠組み

Rains heart、VdB heart、AS heart、anticanonical heartの四名称は由来を表し、四つが相異なるとも一致するとも仮定しない。VdBのliteral blow-up heartとsection-model qgrも自動的に同じではない。同じ入力データの対応と指定導来同値を先に固定し、その後にt-exactness、構造対象、反Serre作用、境界restriction、rank、marking、族の降下を個別に確認する。

cubicでの到達基準は、最後のVdB section-model移行のtorsion pairを実在対象で記述し、AS–反標準比較のt-exactnessを証明するか、非一致を検出する対象を与えること。数値的一致だけでheart一致とはしない。既存dP1の全q導来同値は独立再監査しておらず入力にしない。

## 一次資料が与える比較図

VdBの図式はX_j ←α_j− tilde X_j −δ_j→ X_(j+1)。αはblow-up、δはsection-algebraモデルへの比較。σp_iが指定平面埋込みで一般位置ならTheorem11.1.3はRδ_*とLδ*の逆同値、heart上の振幅[0,1]および[-1,0]を与える。coherent bounded部分の保存にはLemma9.1.5も用いる。cubicはX_7=Proj F。

Chapter12のF=P/(C3)表示は上記一般位置条件なしでも構成されるので、表示の存在だけで導来同値を使わない。Remark12.0.5はraw blow-up反復と各段階のsection-modelへの取り替えの差を明記する。

AOU arXiv:2404.00175 §9は最初からcoh tilde X=qgr F。滑らかな楕円曲線、次数3線束、無限位数σ、sufficiently generalな六点の設定で、Lemma9.2はSerre=(-1)[2]、Theorem9.4はDb qgr F≃Db qgr A。左辺をraw blow-up heartと呼び替えず、abelian equivalenceとも読まない。式(9.44)は可換mutation表示で、その直後に非可換collectionを同じ記号で定義し直す。実際の先頭E0はO(0,0)へ移るが、E0≃πFは対象として確認する必要がある。境界restrictionやK0の一致だけでは不足。

OU arXiv:2508.04986 Definition1.1, §6はAS heartと標識、一般幾何的blow-upとの導来比較を扱い、全パラメータのheart一致定理ではない。Rains arXiv:1907.11301 Introduction, §4も既存abelian構成でt構造とrealizationを正当化しており、任意の抽象gluingのfaithful heart存在を与えるものではない。

## 形式的帰結と適用範囲

**振幅1のHRS比較**（heart原稿§3）：F:Db(A)≃Db(B)、F(A)⊂D^[0,1](B)、G(B)⊂D^[-1,0](A)ならT=ker H¹F、U=ker H⁰Fはtorsion pair、G(B)=〈U[1],T〉、Fがt-exact iff U=0。VdBではT_j=ker R¹δ_j*、U_j=ker δ_j*。非零M∈U_jもRδ_j*M=(R¹δ_j*M)[−1]≠0で、heartからの消失と導来的消失は異なる。これは既知HRS理論の適用。

**ample orbitの一意性**（§4）：faithful bounded heart、tauのheart保存、(e,tau)のAZ amplenessと全対象の高次Extの一様tail消滅の下で、heartはHom(e,tau^n X[i])=0（i≠0,n≫0）で一意に決まる。高次消滅をAZ二公理だけから無条件に導かない。

**固定対象のEuler障害**（§4）：上のheartの非零tau固定対象はchi(e,M)>0。別heartの実在固定対象でchi≤0なら非一致を検出する。周期rの場合はresidueの和の正性だけ。数値共鳴だけから対象存在を補わない。

**corner判定**（§5）：B,e,R=eBeの必要な左右有限性とnoetherian性の下で自然qgr B→qgr Rが同値 iff dim B/BeB<∞。AS helixのfolding、Be/eB有限性を照合した範囲だけで適用。有限次数の実験や同じHilbert級数だけでは不十分。

## 古典的根壁とcubicでの着手

弱del Pezzo S上の(-2)曲線D、F=i_*O_D(−1)は2-sphericalで、全nでRHom(O_S(n(−K)),F)=0、反標準収縮fへのRf_*F=0。従ってAZ生成性は失敗し、Db(coh S)≄Db(qgr反標準環)。十一のcubic根壁と一壁の節点三次の有理例は `papers/sections/cubic_corner_root_walls.tex`、`verify_cubic_root_wall.py`。これは非可換壁上のheart存在やt-exactnessと別。HRS tiltは初めから導来同値を仮定する。

cubicの比較では、最後のVdB段階F=Rδ_6*のker δ_6*を実在対象で求める。AS–反標準側ではAOU九対象とmutationを追い、E0とπFを同定し、反Serre・境界を照合してcorner有限性を使う。Rains側では同じ楕円データと六点のraw blow-upとsection-modelを段ごとに比較し、六段を無条件に一回のtiltへまとめない。有限位数、特異境界、非局所自由gluing、他次数へはこの比較の適用条件を保って進む。

初期のexact検算ではAOU九線束のEuler行列は三blockの上三角、対角I3、隣接J3、離れたblock 2J3で総和45、det1。Serre行列C^−1 C^tの逆がH twistと一致し、E6の72根とH²=3を確認した。反標準Euler値n=0,…,8は1,4,10,19,31,46,64,85,109。再現：`python3 computations/verify_cubic_heart_numerics.py`、`latexmk papers/nc_del_pezzo_hearts.tex`。この有限検算はeffective root、strong性、heart同値の証明ではない。

## 文献と検証範囲

Van den Bergh, *Blowing up of non-commutative smooth surfaces*, arXiv:math/9809116v1：Lemma9.1.5、Def11.1.2、Thm11.1.3、Ch12、Rem12.0.5。AOU, *Compact moduli of marked noncommutative cubic surfaces*, arXiv:2404.00175v1：§4.1、§9、Lemma9.2、Thm9.4、(9.44)直後、(9.54)–(9.57)。Okawa–Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, arXiv:2508.04986v1：Def1.1、Def3.1、§6。Rainsの二論文は共鳴ノートの精密な参照箇所を使う。Chen–Han–Zhou, *Derived equivalences via HRS-tilting*, Adv. Math.354 (2019),106749、arXiv:1804.05629v2：ThmA,B、§§2–3。

既存の比較文献は原典本文を照合済みだが全証明を今回再検証してはいない。新しい混合A2のRains入力は今回一次HTMLと関連PDF画像で照合した。新スクリプトは実行済み、独立driverで新証明節のLuaLaTeX5ページを生成。主原稿全体の組版、外部独立査読、網羅的新規性確認は未実施。正確な状態は `research/resonance_hearts_validation.json`。
