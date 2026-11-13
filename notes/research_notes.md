# 現行の数学・仮定・残る障害

2026-11-13 / v6。最初に00_research_plan.mdを読む。完全な証明は主論文と各sectionに置く。

## 1. 内在的定義と二次包絡

作業定義は豊富列付きAbel圏(C,(E_i))。section Z-algebraの長さ一HomをV_i、長さ二合成の核をR_iとし、Q(A)=T_Z(V)/(R_i)を作る。これが標準5次元Koszul AS正則で、三次核が正則正規族を生成するとき正規三次超曲面型とする。smooth cubicには導来圏の指定したdg enhancementのsmooth proper性を追加する。

三次関係は長さ二までを変えないためambientは一意。相対的には短い完全列の商の局所自由性から核が分裂し、任意の基底変換と可換になる。section Hom自体の基底変換は別仮定である。豊富列の添字を固定する同値を使い、自己同値での1ステップ移動は追加データとする。

Polishchuk, Noncommutative Proj and coherent algebras, MRL12(2005)63–74, Theorem2.4／直後Remarks2（arXiv:math/0212182v4）はample sequenceとgraded表示の違いを直接述べる。Artin–Zhangのsection ring復元は低次数の飽和が必要であり、AS Gorenstein商ではExt^0,Ext^1の消滅を用いる。

## 2. 成分とファイバー

poisson-p4のpapers/poisson_subvariety_incidence_ja.texのthm:cubicとprop:cubic-fibreを参照した。滑らかなcubic上のPoissonはJ(F,L,M)で一意延長され、ambientを固定したファイバーはF+g(L,M)の滑らかな三次を与えるA4開。これは証明を再掲した既存入力で、新規発見として数えない。

新計算は全Poisson方程式を使う。二次bivector係数150、strict Jacobi350係数とdivergence25係数の微分M、37パラメータJacobian源の微分Sを整数で生成した。MS=0を整数で確認し、mod1000003で113次minor844194と37次minor948131が非零。よってrank_Q M=113、全接空間37。37次元源がその点を通るので正則点であり、Rat113錐は全スキームの一般被約成分。147成分分類や浮動小数点ランクは使わない。

Pym, Quantum deformations of projective three-space, Definition2.8／Proposition2.9／Theorem2.10は任意のdimVの規格化CY変形芽を扱う。四生成元の六成分分類は別節。形式同型からArtin近似で得る解析同型とKontsevich級数の収束は別の主張。本稿のgraph関係式がKontsevich級数そのものだとは主張しない。

対応成分の一般中心はk[a,b,c], degrees(1,1,3)。次数三中心5次元から中心直線P4、ambient37・中心対41、一般PGL軌道24を引いて13・17。同じambientを復元する多くの三次があり、一意復元と4次元ファイバーは両立する。

Poisson構造をスカラーで射影化すると36になる。量子代数族の尺度を勝手に割らない。GL5商stackでは共通Gm安定化群により次元12／16、PGL5で剛体化したstackと一般有理商では13／17。一般Z-algebra同型による商への比較は別途必要。

## 3. 相対中心と一次持上げ障害

二次代数族BのB1,B3,B4が局所自由なら、中心三次直線のincidenceはP(B3)上の交換子写像の零点スキーム。核の形成は一般に非平坦な基底変換と可換ではない。一定rankをスキームとして課した層では核束となり、初めてP(kernel)という射影束表示が正当化される。

一次変形delta Bと中心元Gに対してdelta_B(dot G)+dot delta_B(G)=0が持上げ条件。障害はcoker(delta_B)内のdot delta_B(G)。従って中心三次を持つ条件は全ambient成分で一様な余次元を持たない。Jacobian成分では支配的だが他の成分は別に調べる。

## 4. 周期性・滑らかさ・Artin比較

正規次数d族から得るsigmaでd頂点orbit Dを作ると、D0=k^d、z=sum g_iは中心正則元になる。graded右D加群はvertex−degree mod dでd個のB加群圏に分解されるので、明記したAS条件がDへ移る。Reyes–RogalskiのTheorem5.15でtwisted CY、Lemma5.9(1)とuniform AS index NでNakayama双加群がD_mu(N)、mu(e_i)=e_(i+N)となる。Lemma4.5よりmu(z)=z。unfoldしてrho(g_i)=g_(i+N)を得るため、対と商のgcd(N,d)周期性が従う。N=5,d=3ならtheta=rho^(-1)sigma²で三次イデアルを保つ1周期化が得られる。完全な証明はambient_periodicity.texに置く。

この構成でthetaとsigmaは可換にでき、通常の次数付き表示の正規自己同型はtau=theta^(-3)sigma=rho³ sigma^(-5)となる。tau=1は未証明。中心化には、適切なtauの3乗根による捩れなどが候補となるが、その存在は未確認。Zhang twistの具体例として、smooth F=x0²x1+x1³+x2³+x3³+x4³とphi(x0)=−x0, phi(xj)=xj (j>0)では、S^phiのFは非中心正規だが、Z-algebra対は可換中心三次対と同型になる。従って中心性は選んだ次数付き表示に依存する。相対核直線束の自明化・周期構造の降下も体上の証明には含まれない。

上記一次資料はM. L. Reyes–D. Rogalski, Graded twisted Calabi–Yau algebras are generalized Artin–Schelter regular, Nagoya Math. J.245(2022)100–153, doi:10.1017/nmj.2020.32, arXiv:1807.10249。重要な三箇所の本文とgradingの規約を確認した。Z-algebra版のNakayama保存定理を無確認に引用しているのではなく、有限頂点graded代数へ移して適用する。

17次元性は中心正則商の代数的同型類についての結論。ambient AS正則・三次元正則・商平坦からtails smoothnessは従わない。固定剛体ambient B_*の4係数族の正則開は有限位数境界節の仮定で扱う。全37次元ambient族上への相対開性は未証明。

中心対Artin模型は同次formality入力の下でk[[s1..s34,a01..a34]]/(Pluecker5式)、41/44。PGL方向を除くsliceは17/20。構造代数層の変形は後者と比較し、framed41/44の関手とは直接同型でない。Yekutieli Cor11.2はsmooth X、H1(O)=H2(O)=0の下で全ArtinのPoisson／associative gauge類を比較する。De Deken–Lowenの比較はZ-algebra変形であり、1周期化を自動的には与えない。相対Bott/Koszulと実際のOre自然変換の照合条件は本文に明記する。無標識の導来stackやKuznetsov成分の同定とは区別する。

## 5. 保持する既存計算と文献範囲

17係数sliceの31次整数行列式、分離型余次元15、可換cubic忘却核7=6+1、全混合中心・相対Picard障害・偶数Veronese復元・構造対象を保つ導来復元は現行原稿に保持する。完全な証明をノートに重複しない。

Mori–Smith Theorem4.2(1)の「滑らかな平面三次fに対しA(f,lambda)は3-CY」は一次PDFで確認した。相対PBW構成の入力である。PBW、Rains中心、finite-order Bertiniを含む既存原稿全体の独立全面監査・新規性調査は未完了。新しいintrinsic復元・incidence線型代数・Rat113接空間は、それぞれの明示仮定で個別に検証する。
