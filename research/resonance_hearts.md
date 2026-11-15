# Rains resonance と anticanonical heart：研究継続ノート

2026-11-15 / resonance-hearts-v7。再開時は `00_research_plan.md` を最初に読む。公表用原稿は `papers/nc_del_pezzo_resonance_hearts.tex`、完全な証明は同稿がinputする六つの `papers/sections/resonance_*.tex` にある。新しい局所比較の証明は `resonance_mixed_a2_category.tex`。名称は Rains heart / VdB heart / AS heart / anticanonical heart に統一する。GitHub mainが正本、保存成功時はLibraryに保存しない。

## 1. 現在の核心と次の着手

**指数+2/−1の混合A2でconnecting mapのrankは1と証明した。** より一般に隣接根の指数がp,−(p−1)ならrankはp−1。全q導来同値は入力でない。二根が生成する有限長Serre部分圏はΠ(A2)の有限次元加群圏となり、四つの直既約、局所torsion pair、全対象のcohomologyと非消失まで決定した。

**残る具体的問題**はA=R/(g−1)の二次元表現V+の作用である。今や0→W→V+→V−→0（dim W=dim V−=1）は無条件に存在する。自然Φが完全忠実なら、WとV−のcharacterは異なり、この加群拡大は非分裂でなければならない。そのとき作用の像は次元3の三角行列代数である。これらは必要条件であり十分条件とは未証明。

次は固定楕円データからAの生成元について二つのcharacterと非対角項を求める。差分作用素表示、または構造line bundleと根sheafのHomへの作用を使う。次いで既存 `papers/dp1_anticanonical_models.tex` の全q導来同値の完全忠実性・本質的全射性を独立監査する。全Z・全Rains heartのtorsion pair、VdB/AS側との対象の同定、特異境界・非局所自由gluingは引き続き未解決。

## 2. 規約と既約根sheafの符号別Ext

Rains型smooth elliptic nc del Pezzo Xに境界E、構造line bundle e、theta=S[-2]、tau=theta^{-1}、境界triangle theta M→M→i_*Li^*Mがある。R=⊕Hom(e,tau^n e)、中心正則g∈R1、A=(R[g^{-1}])0≅R/(g−1)。qの向きは

`Li^*M=0 ⇒ O_E(alpha)⊗q^m=O_E`, `m=chi(e,M)`

とする。すなわちrho(alpha)=q^(−m)。共鳴の数値式だけからsheaf存在を補わない。以下の根sheafの存在にはRainsのsimple-root effectivityと既約sheaf存在結果を使う。

既約純一次元root sheaf M、alpha²=−2、alpha K=0、Li^*M=0なら、全n∈ZでHom(e,tau^n M)の次元=max(m,0)、Ext¹の次元=max(−m,0)、Ext²=0。Mは2-spherical。自然導来切断Phi(M)はm>0でm次元A加群（degree0）、m<0で(−m)次元A加群[-1]、m=0で0となる。

証明は `resonance_sign_trichotomy.tex`。m≤0では非零e→Mのimage Iが同じc1を持ち、余核Tは零次元。Rains Cor10.16のχ(I)≥1、Prop7.6のχ(T)≥0でHom=0。m>0は反変導来ad双対（Cor5.9、Cor7.26/7.30/7.31、Prop7.16）で指数を反転しSerre双対を使う。自己ExtはCor7.13とEnd=kによる。

**既約性だけから非零e→Mの全射性を推論してはならない。** 非torsionかつ境界非交叉では後述の別補題で単純性を証明できるが、それを一般の既約sheafへ拡張しない。負指数の実在sheafはRains heartのAZ amplenessとpointedなanticanonical heartとのabel同値を妨げる。しかし自然Φの非t-exactnessから抽象的導来非同値・qgr特異化は結論できない。

中心正則gとR/(g)=B(E,L,σ)、deg L=dからdim R_n=1+d n(n+1)/2。共鳴でHilbert関数は跳ばない。genuine smooth classical avatarでは零指数根共鳴は存在しない。古典weak del Pezzoの(-2)曲線の収縮とは区別する。

## 3. 境界外圏と一般の拡大

Z={M | dim M≤1, Li^*M=0}の全対象でtau M=M、Ext^j(e,M)=0（j≠0,1）。自然Φの振幅はZ上で[0,1]であって全heart上の主張ではない。g周期的Extを局所化して有限次元A加群V^0(M),V^1(M)を得る。dim V^j=dim Ext^j(e,M)。任意の短完全列は

`0→V0(M1)→V0(M2)→V0(M3)→V1(M1)→V1(M2)→V1(M3)→0`

というA線型六項完全列を与える。正負既約根の拡大0→M−→M→M+→0でconnecting δのrankをrとすればh0=m+−r、h1=−m−−r。δ同型なら非零MがΦで消える。weak del Pezzoの(-2)曲線上のEuler列0→O(−2)→O(−1)^2→O→0がその古典的模型であり、genuine非可換での存在を主張しない。

異なる既約根alpha,betaではHom=Ext²=0、dim Ext¹=alpha beta（Rains Cor7.13）。交点負なら同時存在不可、0なら拡大無し、1ならExt¹=k。genuine avatarでalpha beta=1かつm_alpha+m_beta=0の同時共鳴は、alpha+betaが零指数の根になるため不可能。Φが二根間のExt¹で完全忠実ならdim Hom_A(V+,V−)=alpha betaが必要。

**非torsionでの強化**（`resonance_mixed_a2_category.tex`, lem:offboundary-no-points / prop:offboundary-serre-length）：境界外sheafの零次元商は存在しない。商Zにはi^*Z=0が従い、theta Z→Zは同数値類間の全射なので同型（Cor7.7）。restriction determinant q^ellとq非torsion性からell=0となる。従って既約境界外root sheafは全heartの単純対象である。

H=−Kがnef、H²>0ならZはSerre部分圏。部分商のc1のH次数はともに0となり、thetaの数値作用とCor7.7で境界非交叉が部分商に保たれる。零次元対象がなく、Prop7.32のfinitely partitive性とnoetherian性から全対象は有限長。単純SはH⊥の負定値性、D²の偶数性、−D²=2−dim Ext¹(S,S)からD²=−2となる。最大共鳴で全単純根が実在すればZの単純対象はちょうどr個である。

Z+=ker Ext¹(e,−)、Z−=ker Hom(e,−)は拡大閉で各V0/V1はexactだが、**Z全体でtorsion pairになることは未証明**。下記の二根部分圏では証明済み。

## 4. 最大数値共鳴の整数表示と稠密性

滑らかな平面三次Eのflex oを原点、q∈Eを非torsionとする。S=Bl_{p_i}P²、r=9−d、rho(ah−Σb_i e_i)=O_E(3ao−Σb_i p_i)。単純根alpha0=h−e1−e2−e3、alpha_i=e_i−e_{i+1}（1≤i<r）に対し、全根共鳴はr単純根共鳴と同値で、整数m0,…,m_(r−1)から

`3p1=(m0−2m1−m2)q`, `p_i=p1+(Σ_{j<i}m_j)q`

と復元される。p1の選択はE[3]の9通り。全根指数非零がgenuine del Pezzo条件に等しい。

互いに異なる正整数N_iに対しp_i=N_i qとすると全根指数が非零で、genuine smooth del Pezzoとなる。d=6,5,4,3,2,1に対し根系はA2+A1,A4,D5,E6,E7,E8、根数は8,20,40,72,126,240。この点集合は各E^rにZariski dense。N1<N3<N2という大小制約を加えてもdenseである（E³の整数行列式−1の自己同型(u,v,w)→(u,u+v+w,u+v)を使う）。全ncモジュライの全成分での密度を主張しない。

根の整数分類はΣb_i=3a、Σb_i²=a²+2から得る。a=0は差根、a=1は三点、a=2は六点、r=8でのみa=3の(2,1,…,1)型がある。Cauchy–Schwarzで|a|≤4、b(b−1)≥0を使うとa=4は不可能。p_i=N_i qでは正のaの根の指数は正係数和、差根e_i−e_jの指数はN_j−N_i≠0。滑らかな反標準曲線からHはnef・big。非ampleならHに直交する有効(-2)曲線がありE制限自明となるため矛盾する。完全証明は `resonance_maximal_a2.tex` と `resonance_maximal_all_degrees.tex`。

三次曲面の具体例はN=(1,3,2,5,7,11)、単純根指数(6,2,−1,3,2,4)。alpha=e1−e2は+2、beta=e2−e3は−1、交点1、gamma=alpha+betaは指数1。Rains 2022 §4と2019 §§9,11の入力で同じheartに両既約sheafが実在する。全72根の数値共鳴は全72向きの既約sheafの実在を意味しない。

有理数例E:y²=x³−x+1、q=(0,1)では2q=(1/4,−7/8)なのでNagell–Lutzによりqは非torsion。上記六倍点の20個の三点行列式とconic評価行列式は全て非零、全72根指数も非零。既存 `verify_resonance_maximal_a2.py` と証明書に厳密算術がある。

## 5. 最大共鳴の既約根とzigzag

全r単純根sheafが実在するとき、それ以外の根類の既約sheafはない。非単純正根gamma=Σc_i alpha_iにはgamma alpha_i<0となるiがあり、Ext¹の非負性に矛盾。負根は有効錐のpointedness（Prop7.19）に反する。同根sheafの指数はq非torsionで一意、Euler値2と純粋性、Cor7.7から同型類も一意。d=6,…,1の個数は3,4,5,6,7,8。

T=⊕M_iのgraded ExtはDynkin zigzag Z(Delta)。次数0,1,2の次元はr,2s,r、全次元はd=6,…,1で8,14,18,22,26,30。Serre pairingから往復矢の積非零、他の長さ二の積零。Liu–Wang, J. Algebra 677 (2025), Thm1.1（arXiv:2301.06757v3）の既知のintrinsic formalityを適用する。A2+A1は成分別、孤立A1は次数から形式的。

固定Rains enhanced dg圏でのTのframed形式変形は各辺のx_ij x_ji=0だけで定義される。木の葉からの消去で障害イデアルを同定でき、gauge商前の形式スキームは2^s個のs次元分枝となる。d=6,…,1の分枝数は2,8,16,32,64,128。cubic E6は32個の5次元分枝。曲面自身の相対変形や全anticanonical heartのモジュライではない。完全証明は `resonance_zigzag_unique.tex`。形式性だけから自然関手のA∞-module構造やconnecting mapは決まらない。下記のrank定理は独立のline-bundle論証による。

## 6. 指数和一の混合A2：rank、全対象、局所torsion pair

仮定は非torsion q、Hnef、H²>0、e exceptional、実在する隣接根S+,S−の指数がp,−(p−1)（p≥2）。非分裂拡大を

`0→S−→P→S+→0`, `0→S+→Q→S−→0`

と書く。証明は `resonance_mixed_a2_category.tex` の thm:a2-delta-rank。

Hom(e,P)=ker(δ:k^p→k^(p−1))は非零。非零e→Pの像がS−と交わらないなら拡大を分裂させるので、この射は全射になる。核Lはrank1 torsion-free、c1=−(alpha+beta)、χ(e,L)=0、χ(L,L)=1。Rains Prop10.13の等号条件でLはline bundle。Hom(e,L)=0、Ext²(e,L)=0（K+gammaのH次数が−dなのでCor10.12によりHom(L,theta e)=0）、RRでExt¹(e,L)=0。eのexceptionalityからh0(P)=1,h1(P)=0となる。従って**rankδ=p−1**。rank1 reflexiveならlineという誤った一般化は不要である。

二段直和拡大の係数行列T∈Mat_(b×a)、t=rank Tならrankδ_M=(p−1)t、h0=pa−(p−1)t、h1=(p−1)(b−t)。p=2では(2a−t,b−t)。Euler0（b=2a）の場合も消失しない。

C=〈S+,S−〉_Serreはmod_fd Π(A2)に同値で、直既約はS+,S−,P,Qだけ。Hom表は順序(S+,S−,P,Q)で

`[[1,0,0,1],[0,1,1,0],[1,0,1,1],[0,1,1,1]]`。

ambient Ext¹はS+とS−間の両向きだけ一次元。P,QはC内でprojective、P⊕Qがgenerator。Endは次元4の二頂点・二矢・両長さ二の道零の代数。表現をx:U+→U−、y:U−→U+、xy=yx=0とすれば、直既約重複度は(a−rank x−rank y,b−rank x−rank y,rank x,rank y)。

cohomologyの組(h0,h1)はS+:(p,0)、S−:(0,p−1)、P:(1,0)、Q:(p,p−1)。よってT=add(S+,P)、F=add(S−)がCのtorsion pairである。全CでΦ(M)=0 iff M=0。P,QのEuler値はともに1だがcohomological degreeは異なる。非既約対象のEulerの符号だけではheart位置は判定できない。

**内在的Extとambient Extの区別**：Π(A2)の単純加群は二周期解消を持ち、Ext_C^(2n)(S+,S+)=k。一方ambient Extは次数>2で消えるためDb(C)→Db(Rains heart)は完全忠実でない。Cのabel分類をそのままambient導来部分圏の同定に読み替えない。

## 7. 二次元表現に残る明示的な障害

p=2では0→W→V+→V−→0、dim W=dim V−=1が存在する。Hom_A(V+,V−)はV+≅V−⊕V−の場合のみ次元2、それ以外は次元1。自然Ext¹_X(S+,S−)→Hom_A(V+,V−)はrank定理により常に単射。この一群での全射性はrepeated scalar表現でないことと同値。

右加群を行ベクトルで表しWを第一座標に取ると

`rho(a)=[[chi_W(a),0],[eta(a),chi_−(a)]]`,
`eta(ab)=eta(a)chi_W(b)+chi_−(a)eta(b)`。

Φが二根の生成する三角圏で完全忠実なら、さらにW≄V−かつこの短完全列は非分裂でなければならない。前者はExt¹_X(P,S−)=0、後者は非零包含S−→Pの像から従う。従ってimage rhoは全三角行列代数（次元3）。characterが同じJordan型はHom次元1テストだけには合格するが完全忠実性には反する。characterが異なる分裂型も非零射を消す。**対象の非消失と射の忠実性を区別する。** 実際の楕円データのcharacterとetaは未計算、全q導来同値の真偽も未決定。

## 8. 一次資料、検証範囲、再現

Rains, *The birational geometry of noncommutative surfaces*, arXiv:1907.11301v1：Cor7.7、Cor7.13/7.15/7.23、Prop7.6/7.32、Cor10.12、Prop10.13を今回HTML一次資料で直接照合。零次元determinantはProp7.24直前。根存在はDef9.1、Thm9.2、§11 pp139–141。Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2：§4 pp33–35のsimple-root effectivityとnef性を本文とPDFページ画像で確認。Liu–Wangの形式性は既知入力であり本研究の新定理ではない。新規性の網羅調査と外部独立査読は未実施。

現行再現コマンド：

    python3 computations/verify_resonance_mixed_a2.py
    python3 computations/verify_resonance_zigzag.py
    python3 computations/verify_resonance_maximal_a2.py
    python3 computations/verify_resonance_extensions.py
    python3 computations/verify_resonance_hearts.py
    latexmk papers/nc_del_pezzo_resonance_hearts.tex

今回の新スクリプトはPython標準ライブラリ・有理数演算で実行し、Hom表、Euler/Ext表、kernelのEuler値、4375通りの直和・cohomology、三角表現の四模型を確認した。実際の楕円A作用行列やsheaf存在を計算したものではない。新証明節を独立のLuaLaTeX driverで組版し5ページを生成した。主原稿全体の組版と既存四スクリプトの再実行は今回未実施。詳しい状態は `research/resonance_hearts_validation.json`。生成・検証・GitHub保存の状態を区別する。
