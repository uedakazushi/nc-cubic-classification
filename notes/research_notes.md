# 研究ノート：モジュライの定義・比較・障害

2026-11-14 / v7。再開は`00_research_plan.md`から。本書は現行の知識を整理し、完全な証明は論文の指定節に置く。

## 1. 何をモジュライのデータに含めるか

二つの座標代数stackは、各成分が局所自由な正の連結Z-algebraのfpqc stackの部分問題として定義する。ambient Bはb_m=binom(m+4,4)、cubic Aはh_m=b_m-b_(m-3)。Aの長さ一のHomと長さ二の積の核からQ(A)を得る。原稿`intrinsic_cubic_reconstruction.tex`の相対復元と、`algebraic_moduli_foundations.tex`の定義・比較定理を使う。

有限窓J_N=[-N,N]では、全Homの乗法の有限個の係数に結合律を課したaffine schemeを、各HomのGLの積で割る。全stackはこれらの2逆極限。AS正則性・noetherian性・無限個のHilbert rank条件の有限決定性は別に必要であり、逆極限表示を有限型代数性と呼ばない。

全対象同定付き圏の1射は(F,alpha_i:F(E_i)≅E'_i)、2射はbeta_i eta_i=alpha_i。Hom群oidは離散化され、厳密Z同型と一致する。同定を忘れると頂点スカラーrho_lambda(a_ij)=lambda_i lambda_j^(-1)a_ijが現れる。weak圏の自己同値の2同型類はAut_Z(A)/rho(T)、恒等自己同値の2自己同型は対角Gm。E_0の同定を残すとT0={lambda_0=1}で正規化でき、2慣性が消える。

相対弱い射は線束族L_iとphi:A→(A')^L、(A')^L_ij=L_i A'_ij L_j^(-1)で記述する。この規約ではF(E_i)≅E'_i⊗L_i。共通線束Lは代数式では相殺するが、圏ではtensor-by-Lとなる。自己同型商はfpqc商層であり、大域点集合の単純な商と同じとは限らない。weak 2-stack化では大域的な代数で表示できないtwisted formsも含み得る。証明は`categorical_moduli_comparison.tex`。

Q(A^L)=Q(A)^Lなので三次→ambientの射は全levelに降りる。ただし相対category比較にはHomの任意の基底変換、低次数saturation、相対section復元を仮定する。裸のAbel圏・導来圏・Kuznetsov成分のみからの復元は含まない。

## 2. ファイバー、中心条件、正規条件

指定したBへの同型まで含む厳密2-fiberは、B_i,i+3の直線部分束L_iについて、左右の全乗法が部分束を与え、L_i B_i+3,i+4=B_i,i+1 L_i+1となる集合層。有限窓ごとに有限積の射影束の局所閉schemeで表せる。固定したk-同型類ならaction groupoid、fpqc局所形式も含めるなら[Inc/Aut0(B)]となる。

接空間は添字を保つHom_(B-B)(I,B/I)。次数付きかつ中心Gの問題なら全normal接空間はZ(B/(G))_3、中心直線だけを動かす部分はZ(B)_3/kGであり、一般には同じとは限らない。

可換B=check Sym(V)では、非被約基底でもnormalityが全L_iの一致を強制し、fiberはP(Sym³V)=P34。局所生成元F,GについてFV=GVからFx_j=G l_jを得て、正則性と係数比較でl_j=lambda x_j、F=lambda Gを示す。頂点スカラーを除いたAut0はPGL5。pointed category levelでBPGL5上へ底変更すれば[P34/PGL5]となり、smooth部分は通常の10次元cubic moduli。

相対中心incidenceはP(B3)上の交換子写像delta:B3→Hom(B1,B4)の零点。核の形成は一般の非平坦底変更に可換とは限らない。schemeとして一定rankを課した層で初めて核束となり、射影束になる。一次持上げ障害は[dot delta(G)]∈coker(delta)。証明は`ambient_incidence_morphism.tex`。

量子多項式の10次元qトーラスでは中心三次を持つ条件は35個の重みごとのcodim4部分トーラスの有限和だが、normal単項式は全点にある。このcodimを全Zモジュライやsmooth cubic部分のcodimと解釈しない。

## 3. 周期構造と有限な追加同一視

`ambient_periodicity.tex`では、左右global dimensionとuniform AS Ext条件を明記する。正規次数d族をsigmaで畳み込むd頂点orbit Dの中心正則元zを作り、Reyes–RogalskiのTheorem5.15、Lemma5.9(1)、Lemma4.5を適用する。Nakayamaはzを固定するので、unfoldしたN周期rhoも三次イデアルを保つ。N=5,d=3ならtheta=rho^(-1)sigma²により対・商が1周期化する。残る正規自己同型tau=rho³ sigma^(-5)が恒等とは限らず、大域族への降下は別問題。

中心性はgraded表示に依存する。smooth F=x0²x1+x1³+x2³+x3³+x4³とphi(x0)=−x0, phi(xj)=xj(j>0)では、S^phiのFは非中心正規だが、Z-algebra対は可換中心対と同型。中心商だけを全intrinsic定義にしてはいけない。

`period_forgetting_moduli.tex`ではPer_1(B)の共役商でgraded表示を比較する。Sierra Cor4.4は任意のZhang twisting systemを含む。単一の自己同型の冪によるtwistに限定しない。厳密fiber Per_1(B)と同型類上の共役商を混同しない。

H_R={(g,h)∈PGL5²:(g⊗h)R=R}の両射影が単射なら、Rを保つ両無限列の自己同型は、閉部分群の降鎖を安定化して得る有限型群K_Rで決まる。周期の同一視はka alpha(k)^(-1)。無限小周期変動はcoker(1-d alpha)。有限なgraded自己同型群だけから結論する前に、この有限次元化が必要。

本族ではPBW基底と中心一次変数u,vから両射影の単射性を証明した。さらにF0で作った150×50整数行列M(X,Y)=vec(Q(X⊗1+1⊗Y)R)には二つのスカラー核があり、48次minor mod1000003=815096である。したがってrank_Q M=48、一般H_Rは有限。行列は`verify_two_factor_stabilizer.py`、小証明書は`two_factor_stabilizer_certificate.json`。有限群の位数・周期忘却の次数は未計算。

この一般開部分では、13次元ambient族と17次元三次対族におけるZ同型による追加同一視は有限個。これは同型類の一般変動次元を保つ結果であり、全stackの有限型性・成分性を単独で証明しない。

## 4. 全normal fiberの形式的中心化

特殊Bに有限H_R、中心正則一次元u、中心正則三次元Gがあるとする。任意のgraded Artin変形B_T上のindexed normal liftで生成元G_iを選ぶと、G_i x=phi_i(x)G_i+1となる。正則性から(phi_i⊗phi_i+1)R_T=R_T。特殊H_RのLieが0なのでArtin帰納でphi_iはスカラーとなり、G_iを再規格化してG_i x=xG_i+1とする。

次数3へ延長してb=G_iを代入すればG_i+3=G_i。平均H=(G_0+G_1+G_2)/3は中心であり、差D_iはD_i u_T=u_T D_i+1を満たす。最初の非零m進層で特殊uの中心性と正則性を使い、d_iが全て等しく和0なので消える。帰納で全G_i=H。従ってindexed normal liftは単一の中心直線であり、逆写像はL_0なので自然性もある。

固定Bかつdim Z(B)_3=5なら、全normal厳密fiberの形式完備化はSpf k[[t1,t2,t3,t4]]。証明は同節のprop:indexed-normal-central-rigidityとcor:indexed-normal-four-dimensional-fibre。一般のZ ambient変形がgradedから来ることは仮定していないので、この結果から相対周期化そのものを結論しない。

同節の相対Nakayama剛性は、相対Koszul双対の有限自由Frobenius構造と双加群複体の存在を入力にしている。有限射影自己同型群からmu=xi_c、Frobenius trace不変性からc^5=1、c≡1からmu=1。相対双対性の自動成立は未証明。

## 5. 可換点の形式モジュライ

P4とsmooth cubic XはH1(O(j))=H2(O(j))=0を全jで満たす。De Deken–Lowen Theorem4.5によりAbel変形とsection Z-algebraの線型変形を比較でき、O(i)は同型類として一意に持ち上がる。自己同型1+mは残り、対象の持上げからshift自己同値の持上げを自動的に得ない。Lowenのringed-space/algebroid比較とYekutieli Cor11.2により、全Artinで構造代数層とPoisson変形のgauge類へ比較する。詳細と一次参照は`formal_ambient_comparison.tex`。

P4ではPoisson変形関手は、Jacobi零点錐の原点完備化をPGL5_1で割ったもの。接空間は126。epsilon³上でpi=epsilon Pとexp(epsilon xi)piは二次で異なる代表となるため、接空間が等しいだけでは裸の錐とgauge商を同定できない。

有限Beilinson窓O,…,O(4)にHom(O,O(1))の射影基底を指定し、対象スカラーを除くと特殊点の無限小固定群が消える。形式陰関数定理でsliceができ、射影基底付きAbel変形をprorepresentする。frame忘却とPoisson錐は同じ関手のminimal hull。Pymの規格化CY芽との比較から両完備局所環が抽象的に同型と分かり、その後に実際のQmod自然写像の接空間同型を使って実際の写像の同型を証明する。この順序が重要であり、接空間だけの推論ではない。

帰結：規格化CY芽と射影基底付きAbel/Z形式模型は全Artinで一致。frameを忘れるとPGL5_1を割る。集合値の標識付き変形関手についての結論であり、2-stackや全大域モジュライの同値ではない。

smooth cubicのArtin局所環は、明記した同次formality入力の下でk[[s1..s10,a01..a34]]/(Pluecker5式)、次元17・接空間20。全framed中心対の41/44模型とは区別する。実際のambient写像の接写像は(dot F,a)↦Pi(F,a)、dot F方向の核10・像10。H0(T_X)=0であるためcubic側にP4と同じ24次元の形式gaugeは残らない。

独立に選んだ射影とaffine formalityの座標で、全高次のactual mapが(F_R,a)↦Pi(F_R,a)という式と一致することは未確認。写像自体の存在と一次式、中心対局所環の記述はこの未確認点を前提にしない。

## 6. 成分・像・次元の範囲

poisson-p4の参照mainはf118dfbfc5bb9b7a394d1985b4800b6228eebaf6。smooth cubic上のPoissonはJacobian P(F,L,M)へ一意延長し、ambient固定fiberはF+g(L,M)、二元三次gのA4開。これは既存入力を証明再掲したもの。

全Poisson微分Mは375×150、源の微分Sは150×37。整数MS=0とmod1000003の非零minor（M113=844194、S37=948131）で全接空間37を証明する。37次元既約像が通るのでRat113錐は全Poissonスキームの一般正則成分。全147分類や有限体での零の推論は使わない。

Pymのscheme/formal germ比較と実際のQmod比較により、Q113は射影基底付きAbel/Z形式模型の37次元成分でもある。頂点完備化が整域であることは斉次最低項の積で示し、一般正則性にはexcellenceを使う。中心三次incidenceの支配的成分の射影閉包を取り、可換ambientの全fiberに沿って完備化すると、flat base changeとformal functionsにより像の形式閉包はこの成分全体となる。特定の一点Fの完備化だけの支配性とは異なる。

閉包に現れる全特殊cubicは可換多項式環で非零正則なので、Artin持上げでも各乗法のunit minorから正則性と商の自由性が従う。この完備incidenceは正規三次型のモジュライへ写る。smooth properな三次部分だけが同じ成分を支配するかは未証明。

一般中心はk[a,b,c]、重み(1,1,3)。中心3次5次元からfiberP4、ambient37・incidence41、PGL軌道24を引いて13・17。GL商stackは共通Gmの慣性のため12・16。Poissonスカラー射影化では36。可換cubic忘却fiber7=6 moving plane+1 Poisson scaleと、ambient忘却fiber4を混同しない。

## 7. 保持する既存成果と次の技術的入口

17係数sliceの31次整数行列式−5538243375000、分離型余次元15、可換cubic忘却核7、全混合中心、相対Picard障害、偶数Veronese、構造対象を保つ導来復元、固定剛体ambientの4係数族と有限位数境界は現行原稿に保持する。完全な証明は重複しない。

次の技術的入口は、一般H_R有限点の相対helix再構成とKoszul–Frobenius双対性。可換点の形式比較は済んでいるため、それを繰り返すことより、一般非可換点で有限窓のatlasと全Z変形を結び付けることを優先する。smooth proper部分の開性には、相対dg模型と対角のperfect性の有限検査が必要。

文献上の範囲：Sierraの厳密twist比較、AOUのAS3での内部O(n)認識、Behrend–Noohiの切断stackは一次資料を確認。AOUの裸のqgr復元をAS5/cubicへ無証明で一般化しない。新しい主張の初出・優先権と、保持した全旧証明の独立全面監査は未完了。実施した計算・組版・証明監査はvalidation.jsonで区別する。
