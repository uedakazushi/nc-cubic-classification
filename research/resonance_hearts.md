# Rains resonance と anticanonical heart：研究継続ノート

2026-11-15 / resonance-hearts-v6。再開時は `00_research_plan.md` を最初に読み、本ノート、`papers/nc_del_pezzo_resonance_hearts.tex` と同稿が input する5つの証明節 `papers/sections/resonance_sign_trichotomy.tex`、`resonance_extension_cancellation.tex`、`resonance_maximal_a2.tex`、`resonance_maximal_all_degrees.tex`、`resonance_zigzag_unique.tex` を参照する。名称は Rains heart / VdB heart / AS heart / anticanonical heart に統一する。

## 1. 主結果の仮定と符号別Ext

Rains型のsmooth elliptic nc del Pezzo Xに境界 E、構造line bundle e、theta=S[-2]、tau=theta^{-1}、自然変換 theta→id がある。R=⊕_{n≥0}Hom(e,tau^n e)、中心正則g∈R1、A=(R[g^{-1}])0≅R/(g-1)。rank-zero root alpha²=-2, alpha·K=0の**既約純一次元sheaf Mが実在し、Li^*M=0**なら m=chi(e,M) と置いて全n∈Zで

- Hom(e,tau^n M) の次元 = max(m,0)
- Ext¹(e,tau^n M) の次元 = max(-m,0)
- Ext²(e,tau^n M)=0
- Mは2-spherical。自然なderived section Phi(M)は、m>0でAのm次元加群（degree0）、m<0でAの(-m)次元加群の[-1] shift、m=0なら0に写す。

証明：m≤0では非零e→Mのimage Iはc1(I)=alphaで、余核Tは0次元。Rains Cor10.16よりχ(I)≥1、Prop7.6よりχ(T)≥0なので矛盾してHom=0。**「既約なら非零e→Mは全射」は誤りであり採用しない。** Ext²=0はRains Cor7.23。m>0はRainsの反変導来ad双対（Cor5.9, Cor7.26/7.30/7.31, Prop7.16）で指数を−mに反転し、Serre双対でHomとExt¹を交換する。自己ExtはRains Cor7.13のEuler自己値2とEnd=kから決まる。

**m<0**の実在根sheafがあればRains heartの(e,tau)はAZ-ampleでない。構造対象・tauを保つpointedなRains–anticanonical heartのabel同値は不可能。ただし自然なPhiがt-exactでないことから、抽象的な導来圏の非同値・qgrの特異化を結論しない。

## 2. 境界非交叉の非既約sheaf

Z={M in Rains heart | dim(M)≤1, Li^*M=0}は拡大閉のexact category。全M∈ZでtauM≅M、Ext^j(e,M)=0 (j≠0,1)、自然導来切断の振幅は[0,1]（**全Rains heart上の振幅ではない**）。各j=0,1のg周期的ExtからV^j(M)=(⊕_{n≥0}Ext^j(e,tau^nM)[g^{-1}])0という有限次元A加群が得られ、dim V^j=dim Ext^j(e,M)。

短完全列0→M1→M2→M3→0は6項A加群完全列0→V0(M1)→V0(M2)→V0(M3)→V1(M1)→V1(M2)→V1(M3)→0を誘導する。Z+=ker Ext¹(e,-)、Z-=ker Hom(e,-)はそれぞれ拡大閉だが、**Z全体のtorsion pairの存在は未証明**。

正根M+、負根M-の混合拡大0→M-→M→M+→0は、connecting δ:V+→V-のrank rによってdim V0(M)=m+−r、dim V1(M)=−m−−rとなる。δ同型なら非零MがPhiで消えるので、Phiが保守的または全導来同値ならそのような拡大は禁止される。弱del Pezzoの(-2)曲線上のEuler列0→O(-2)→O(-1)^2→O→0は完全相殺の古典的模型。genuine非可換への存在を断定しない。

異なる根類alpha≠betaの境界非交叉既約sheafについてHomとExt²は零、dim Ext¹(M_alpha,M_beta)=alpha·beta（Rains Cor7.13）。alpha·beta<0なら同時存在不可、=0なら拡大無し、=1ならExt¹が1次元。genuine classical avatarではalpha·beta=1、m_alpha+m_beta=0の同時共鳴は不可（alpha+betaがrootとなりそのE制限が自明になってしまうため）。Phiがmixed pairで完全忠実ならdim Hom_A(V+,V-)=alpha·betaという具体的テストを得る。

## 3. 今回の新結果：最大E6根共鳴を整数格子で分類

滑らかな平面三次Eの変曲点oを原点とし、非torsion q∈Eを固定する。六点p_i∈EでS=Bl_{p_i}P²、根格子Lambda=K_S^perp≅E6。alpha=a h−Σ b_i e_iのrestrictionはO_E(3a o−Σ b_i p_i)。

単純根alpha0=h−e1−e2−e3、alpha_i=e_i−e_{i+1} (i=1,...,5)。**72根全てのrestrictionが<q>に入ることと、次を満たす整数m0,...,m5の存在は同値：**

`3 p1=(m0−2m1−m2) q,``p_i=p1+(Σ_{j<i}m_j)q` (i=2,...,6)。

m(alpha_i)=m_iで、任意の根alpha=Σc_i alpha_iの指数はm(alpha)=Σc_i m_i。mを固定するとp1は3-torsion分だけ9通りある。**六点が一般位置でgenuine cubicとなる必要十分条件はm(alpha)≠0 (全72根)**。根の型は±(e_i−e_j)、±(h−e_i−e_j−e_k)、±(2h−Σe_i)、それぞれ二点の一致・三点共線・六点conicに対応する。

より強く、互いに異なる正整数N_iについてp_i=N_i qとすれば、全根が非零指数で同時共鳴し、六点は常に一般位置。正整数倍集合はEにZariski denseで、その六重直積から対角を除いてもdense。N1<N3<N2と課してもdense（(u,v,w)→(u,u+v+w,u+v)はdet=−1のE³自己同型）。

**具体的な混合A2根対**：N=(1,3,2,5,7,11)では六単純根の指数は(m0,...,m5)=(6,2,−1,3,2,4)。alpha=e1−e2のm=2、beta=e2−e3のm=−1、alpha·beta=1、alpha+beta=e1−e3のm=1。Rains 2022 §4のsimple-root effectivity判定、Rains 2019 §9,§11のformal(-2)-curve/sheaf存在の入力から、同じRains heartに両方の既約境界非交叉sheafが**実在**し、Ext¹(M_alpha,M_beta)=k。全72根が数値的に共鳴することは、全72向きのroot sheafが同じheartで既約になることを意味しない。

その非分裂拡大0→M_beta→M→M_alpha→0のconnecting δ:V_alpha (dim2)→V_beta (dim1)のrankは0か1。従って(dim V0(M),dim V1(M))=(2,1)または(1,0)。**rankそのものは未決定**。

任意の二段直和拡大0→M_beta^⊕b→M→M_alpha^⊕a→0 (a≥1,b≥0)について、Ext¹(M_alpha,M_beta)=kのgeneratorのconnecting dと、拡大の係数行列T∈Mat_{b×a}(k)を使いδ=d⊗T。r=rank d × rank T≤min(a,b)なのでdim V0(M)=2a−r≥a>0、dim V1(M)=b−r。**この二段拡大はEuler標数が0の場合(b=2a)でもPhiで消失しない**。

もしPhiがこの二対象間で完全忠実なら、dim Hom_A(V_alpha,V_beta)=1で、2次元A加群V_alphaは1次元V_betaを商として持つ（すなわち単純加群ではない）。これが既存dP1論文の全q導来同値主張の明示的な検証課題。現在、Aの表現行列とconnecting dを計算したわけではない。

**有理数上の証明書**：E:y²=x³−x+1、q=(0,1)。2q=(1/4,−7/8)のxが非整数なのでNagell–Lutzによりqは非torsion。上の六倍点(1,3,2,5,7,11)は有理点で、20通りの三点determinantとconic評価行列式が全て非零。E6全72根の指数は非零、単純根指数[6,2,−1,3,2,4]。整数・有理数計算は `computations/verify_resonance_maximal_a2.py` と小証明書にある。

## 4. 次数1から6への最大根共鳴の拡張

**証明済み**：任意の$d=1,…,6$で$r=9-d$点を楕円平面三次$E$の相異なる正整数倍$p_i=N_iq$（$q$非torsion）として選べば、滑らかなgenuine del Pezzo blow-upを保ちながら当該根系の全ての根が非零指数で同時に数値的共鳴する。根系と根数は$d=6:A_2+A_1(8)$、$5:A_4(20)$、$4:D_5(40)$、$3:E_6(72)$、$2:E_7(126)$、$1:E_8(240)$。いずれもこの最大共鳴点集合は$E^r$にZariski dense。$N_1<N_3<N_2$を追加してもdenseであり、Rainsのsimple-root effectiveness/irreducible-sheaf存在仮定下で正負の隣接するroot sheafが同じheartに実在し、$\operatorname{Ext}^1=k$、負指数によるAZ ampleness失敗が起こる。

**全次数の指数チャート**：単純根$α_0=h-e_1-e_2-e_3$と$α_i=e_i-e_{i+1}$（$1≤i<r$）による$r$整数$m_0,…,m_{r-1}$から $3p_1=(m_0-2m_1-m_2)q$, $p_i=p_1+(m_1+…+m_{i-1})q$ を復元。$p_1$は$E[3]$の9通り。genuineであることと全根指数非零は同値。$a h-Σb_ie_i$の根は$Σb_i=3a, Σb_i^2=a^2+2$を満たし、positive-$a$根は$a=1$の三点、$a=2$の六点、$r=8$に限って$a=3$の$(2,1,…,1)$型と分類される。楕円曲線の正整数倍では全ての非差根指数が正、差根の指数は$N_i-N_j≠0$。滑らかな反標準曲線の存在から$-K$はnef・bigであり、非ampleなら有効$(-2)$曲線の根制限が自明になるため矛盾する。

論文中の完全な証明は`papers/sections/resonance_maximal_all_degrees.tex`（`papers/nc_del_pezzo_resonance_hearts.tex`がinput）。既存の`computations/verify_resonance_maximal_a2.py`に$r=3,…,8$の全根列挙と整数指数検算を統合した。数学的に同等なローカル整数コードを実行し root counts=(8,20,40,72,126,240)を検査。push後のGitHub版スクリプト自体を実行したとはまだ報告しない。これは**全モジュライ成分での稠密性や全根既約sheafの同時存在を証明した結果ではない**。

## 5. 最大共鳴での既約根sheaf・zigzag形式性

**証明済み（Rainsのsimple-root存在入力）**：最大共鳴でr=9−d個の単純根に対応する境界非交叉既約純一次元sheaf M_iが実在するとき、他の根類の既約sheafは存在しない。非単純正根gamma=Σc_i alpha_iについてgamma²=-2からgamma·alpha_i<0となるsimpleがあり、RainsのExt¹次元=交点数に矛盾。負根は有効錐のpointedness（Rains Prop7.19）に反する。q非torsionなら同根sheafのEuler指数はrestriction determinantにより一意。二sheaf間のEuler χ=2から非零Homが存在し、純粋性・既約性で単射、同数値類の単射はRains Cor7.7で同型。よって同型類数はd6,..,1で3,4,5,6,7,8。**全根数値共鳴≠全根既約sheaf存在**。

**graded Ext**：T=⊕M_iのYoneda代数はDynkin図Δのzigzag Z(Δ)。次数(0,1,2)の次元は(r,2s,r)、s=辺数。Serre pairingにより往復矢の積が非零、非往復の長さ二の積は零。全次元はd6,..,1で(8,14,18,22,26,30)。

**dg形式性とframed形式変形**：Liu–Wang, *A∞-deformations of zigzag algebras via Ginzburg dg algebras*, J. Algebra 677 (2025), Theorem1.1, arXiv:2301.06757v3 の一次資料を確認。標数0のADE zigzagはintrinsically formal。d6のA2+A1は成分別、孤立A1は次数理由で形式的。固定したRains enhanced dg圏の中のTのframed形式変形はMaurer–Cartan方程式m₂(x,x)=0のみ。Dynkin森の葉からの帰納法で定義イデアルは各辺の(x_ij x_ji)に等しく、gauge商前の形式的スキームは2^s個のs次元formal座標部分空間の合併。d6,..,1で成分数(2,8,16,32,64,128)、cubic E6で32個の5次元formal分枝。高次A∞障害による追加切断はない。**Rains曲面自身の相対変形／anticanonical heart全体の変形／A=R/(g−1)の表現行列・connecting δ rankは別問題**。

完全証明：`papers/sections/resonance_zigzag_unique.tex`。標準Python検算：`computations/verify_resonance_zigzag.py`（各次数の全根、非単純正根のnegative pairing、Ext次数と葉消去）。これはRainsの既約sheaf存在・Liu–Wangの形式性を計算で証明するものではない。新規性全面調査と独立査読は未実施。

## 6. 保存する全次数の知識と未解決の核

- 中心正則g∈R1とR/(g)=B(E,L,σ), deg L=dよりdim R_n=1+d n(n+1)/2は共鳴で跳ばない。
- q非torsion、smooth genuine classical avatarではm=0の根共鳴はない。古典weak dPの(-2)曲線が反標準収縮で消える現象とは区別する。
- 正指数と負指数の個別共鳴は各々Zariski dense（楕円点p3(n)の正負q軌道）。全72根同時共鳴の点も稠密であり、次数1,...,6の全てに当該根系の最大共鳴稠密点集合がある。一般のnc dP moduliの全成分での稠密性までは主張しない。
- **優先1**：具体的混合A2においてaffine A=R/(g−1)の2次元・1次元表現行列を算出し、dのrankとHom_A(V_alpha,V_beta)を決定する。必要ならRainsの差分作用素表示から構成する。
- **優先2**：既存`papers/dp1_anticanonical_models.tex`の全q derived equivalenceの完全忠実性・本質的全射性を独立に監査する。原稿に証明が書かれていることと今回の監査を区別する。
- **優先3**：Zのtorsion pair/全heart、非既約対象、VdB/AS heartとの対象の同定、特異楕円境界、非局所自由gluingを調べる。負指数の自然Phiの非t-exact性やqgrのHilbert不変性から導来非同値・qgrの特異化は結論しない。

## 文献・再現・検証範囲

Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2, §4 pp33--35（単純根のeffectivityと稠密性、K0の制限）。Rains, *The birational geometry of noncommutative surfaces*, arXiv:1907.11301v1, Definition 9.1, Theorem 9.2 (simple roots/formal(-2)-curves), §11 pp139--141 (root sheaf existence), Cor7.13 (Euler形式), Cor7.23/7.26--31/10.16等。原典PDFのtext layerを照合した。Web screenshot取得はcache miss、独立査読と網羅的新規性調査は未実施。

主要再現コマンド：`python3 computations/verify_resonance_zigzag.py`、`python3 computations/verify_resonance_maximal_a2.py`、`python3 computations/verify_resonance_extensions.py`、`python3 computations/verify_resonance_hearts.py`、`latexmk papers/nc_del_pezzo_resonance_hearts.tex`。新しい算術コードと数学的に同等のローカルコードを有理数上で実行したが、GitHubにpushしたコード自体の実行・全原稿組版は別途確認事項。GitHub mainを正本としてpush成功ならLibraryへ保存しない。
