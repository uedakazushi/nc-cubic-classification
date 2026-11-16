# 研究ノート：モジュライの定義・比較・障害

## H3 位数4中心値：現在の再開点

最優先は位数4積分族の全 bad D の決定。一次元表現だけについては `cubic_character_serre.tex` と `verify_cubic_character_serre.py` に全奇数Ext1障害を判定する余因子恒等式を得た。Jacobian/2=M の階数2では、核の射影点が楕円 point curve E にあるとき正確に自己Ext1=1。階数1は2、階数3は0、階数0は3。これは全単純表現・高次Extの判定ではない。

固定 h1,gamma^4=2,a=(1/(2gamma),1/(2gamma),0),beta=(1,1,2) では character CI 長さ8、critical scheme は (x+y-2,(y-1)^2,z) の長さ2で台(1,1,0)。中心値のscheme imageは被約な一点 Dstar=(2gamma^4+10gamma^3+21gamma²+19gamma+13)/(4(1+gamma)^5)。Dstarは確実にbad、piは同じ包絡でgood。他のDの良否は未決定。この固定包絡で次数4以下の中心計算も完了した。`verify_cubic_order4_center.py` は g^4=2 の体上、包絡の次数0..5の次元(1,4,10,20,35,56)を逐次商で作り、中心三次商の次数4/5次元31/46を小行列で求める。138×31交換子行列はD一次。Dに関する重み付き一次ansatzは核次元5（定数1,Dと三四次中心元）、三つの最高四次は独立。全交換子はD記号のまま正確に零と確認、係数式を小JSONに保存した。中心全体の三生成元・全Dの任意底変更・中心上階数16をfiltered帰納で証明し `cubic_order4_center.tex` に統合した。先頭のHesse型三次関係は楕円座標環での厳密計算で取得済み。下位項26係数も、重み(r,D,Z)=(1,3,4)から事前次数境界を証明し、17個全ての厳密48次元sliceで再構成を完了した。設計行列式18432、全関係は `cubic_order4_center_relation_certificate.json` にcompleteとして保存済み。未計算の関係や全bad値を完成扱いしない。次はこの固定包絡で高次元単純表現／有限中心を計算し、Dstar以外のbadがあるかを判定する。characterだけの結果を完全bad一覧に昇格しない。

滑らかな次数3楕円THCR（translation）の全filtered deformationについて、Rees環の二次包絡がnoetherian quadratic Koszul CY AS4で、一本の正則中心三次の商になることを証明した。AS4包絡を外部に仮定せず復元できる。非可換では境界が一意なので、intrinsic中央楕円H3の幾何学的群oidは有限gldim filtered deformationとfiltered同型に一致する。Hesse/Moore・対称線型係数・中心三次の単一線型核による有限候補atlasと全同型係数比較を得た。有限Nは中心McKay条件で全admissibilityを判定し、被約固定N族では相対中心とH3開性も証明済み。無限位数の全bad値、全intrinsic family stack・既約成分、中央境界を持たないH3被覆は未完成。正規境界の被覆と三角境界全有限位数の判定は後述の現行結果を参照する。次は非捩れ三角境界の残る許容性と、全H3の未被覆CY/非CY領域を縮小する。
証明は cubic_filtered_elliptic_recognition.tex。重要な循環回避：ReesRのt正則性から二次係数A対称を先に導き、BGでBのPBW/AS4性を得る。BがAS4だからA対称、と仮定して戻ってはいない。非commSではZ(S)1=0→Z(B)1=kt。mu_B(t)=c*t、mu_S=id、RRZ Theorem6.3のhdet mu_B=1と(E3.9.1)のfactor cでc1。その後二次関係でtranslation0。RRZの一般AS Gorenstein conjecture/条件付きLemma7.1は輸入しない。B→RのkernelはHS s³HBとGの片側idealのHS一致で左右principalnormal。modtのgもcentral、Gnormalizerはt固定・modt identityなので再びtranslationminorからGcentral。
全filtered同型はX→MX+v、detM!=0の係数比較（3quad+1cubic、F3次元19）で尽くされる。境界tのrescaleはF_nUの部分空間を変えず、gradedR同型のkernelは次数スカラー。有限型候補incidenceは(E Hesse lambda,p)、A対称6、beta3、G下位10係数に単一中心核を課したもの。Gmodt=gの線型規格化は有限chartで行う。有限Nならadmissibilityは解決済みだが、全intrinsic族同定や成分分解は主張しない。
次は旧Γの(1+h³)倍のh=-1特殊化と最高三次係数gcdを実行する。既存候補atlasはj0も含むため、j0の存在を未分類扱いへ戻すのでなく、中心式・具体例・小さなパラメータ化を取得する課題として進める。

計算の目的・停止基準：まず全 character とそのcritical scheme・中心像を有限Groebner計算で完全に確認する（済）。次のPI中心計算は次数4の中心候補を正確に得た時点でcheckpointし、中心関係や局所global dimensionの証明なしにsmoothnessを断定しない。大きい次数の自由単語全列挙は避け、次数ごとの商基底と乗法を使う。

2026-11-14 / v8。再開は`00_research_plan.md`から。本書は現行の知識を整理し、完全な証明は論文の指定節に置く。

## 三次三様体・非可換P^4の研究は独立
この主題の現行原稿・証明・研究ノート・計算は https://github.com/uedakazushi/nc-cubic-threefold-moduli を正本とする。本ノートにはH3曲面の現在有効な結果だけを保持する。

### j0正規化境界での再開入口

旧Gammaの極は(1+h³)Gammaを先に約分してh=-1へ特殊化すれば除ける。新中央パラメータD*t³は特殊化後に自由に足す。全係数と厳密例はcubic_j0_boundary_certificate.json。h=-1,gamma=2のtranslationは無限位数（良い還元位数9 mod5、6 mod13）。これはpotentialのj0でありpoint schemeのj0ではない。全gammaで最高記号が非零とはまだ主張していない。次は具体例の代数的D判定、またはMoore係数abc=0の三捩れchartで中心三次持上げを明示する。無限位数の全bad値の有限性・相対開性は既知の固定有限N定理から推論しない。

### 三捩れ量子Weyl chartの全中心と固定切断（classification-v27）

関係yz=qzy+b1,zx=qxz+b2,xy=qyx+b3（q²+q+1=0）ではX=x³,Y=y³,Z=z³,W=xyz+(b1x+q b2y+b3z)/(q−1)が全中心を生成する。d=1/(q−1),e=−(2q+1)/9としてW³−d b1b2b3W−XYZ−eΣbi³Xi=0。滑らかなHesse中央切断X+Y+Z−3lambda W+Dの中心は実際にこの中心環の商と一致する（最高記号中心とRainsで証明）。b=(1,1,1),lambda=0では全非H3値は(D²+4e)(D²+36e)=0の四つ。D²+9e=0の二値は中心A1だがMcKay(1,2)でH3。他の四値にはcharactersがなく非H3。証明はcubic_quantum3_center.tex、全中心式と臨界値の厳密検算は二つのquantum3検証器。次は全beta/lambdaのMcKay分配と判別式、または中央境界のないH3被覆を進める。

### 正規一次楕円境界の現行分類（classification-v38）

mu_R=idの正規三次商でR/(t)が滑らかな次数3楕円THCRの場合、共役theta（ta=theta(a)t）は有限位数1,2,3,4,6。lambda1のunipotentはSklyanin二次minor（可換例外は三次方向微分）で消える。s=t^mの中央分母払いによりH3 iff gldim U有限（U=R[t^-1]_0）を証明。中央化Zhang twist R^(theta^-1)は同じUとgrU≅Hの通常の濾過を与えるが、mu_Rtwist=thetaでintrinsic反標準gradingは変わる。

位数4,6および位数3D0はskew elliptic coneとなり除外。位数3はB=S[t;lambda],G=g+D t³、B CY、g中心、mu_S=scalar(lambda)となり、全admissibilityはD!=0。S[g^-1]の中央cube-root有限etale/separable拡大が(S/(g−1))[z±]となるため有限glを得る。さらに巡回固有tensorの8次元空間をsl3の随伴模型へ同定し、全trace零Jordan行列のpoint determinantを計算した。滑らかな楕円境界を許すのは重複固有値の対角型、すなわち量子P2包絡のみ。中心三次はbinary cubic+z³で、滑らかさから全てFermatへ直せる。従って位数3非中央部分は既知の量子Fermat一対象、幾何学的群oidはBH54に一致する。

位数2の全包絡被覆も証明した。S=QHのmu_S(g)=−gとhdet mu_S=1から誘導楕円自己同型fは反転型involution。mu_S²=scalar(c),c³1を適切なscalarで補正したalphaでSをtwistすると、境界は二つの可換involutionの積、従ってtranslation order1or2。既証のtranslation包絡CY性がc1を強制し、Sは可換P2のinvolution twistまたはCliffordのswap twistに限る。前者の全非skew定数持上げはPBW overlapとWeyl中心化環k[w²]の奇偶で除外され、既存符号skew分類へ入る。

Clifford swap枝はBの関係yz+zx=hxy+b t²,zy+xz=hyx+b t²,x²+y²=hz²+c t²,tは全activeと反交換。W1は一本、6G*=x²z−xzy+yzx−y²z+zy²−zx²。有限Gamma cocycle (-1)^(a e'+r a')で中央Clifford beta=(b,b,c)に戻すとG*は純volume。H3 iff長さ8 CI（2yz−hx²−b,2zx−hy²−b,2xy−hz²−c）が被約。h=b=c=1は実際の非skew・非CY H3例で、degree4三正規式、CI長さ8・Jacobian unit、全512 cocycle恒等式を厳密検算済み。証明はcubic_normal_order2_clifford.tex、quantum排除はcubic_normal_order2_quantum.tex。

Clifford swapでは正規滑らか楕円境界ktが一意。mu_B負固有空間の候補au+bz+ctに反交換子rank1を課すと、minor−4h²でa=b0（非被約底でも同じ）。全intrinsic矢はt→a t′,X→M X′、M alpha=alpha M、r_h^0(MX′)=N r_h′^0(X′)、N beta′=a² betaという有限係数方程式を共通次数scalarで割ったもの。任意底変更の全graded同型functorを与え、一般次元2、一般慣性mu2×mu2。

許容条件は明示quartic Delta_h(b,c)=(h c−2b)((h³−2)b−3h c)(c²+h²bc+2h b²)の非消滅と同値。固定hで四つのbad方向は相異なる。P1_betaから四点を除く係数方向で、任意底変更・fpqc fiber条件に適合する。二character枝x=yと2z+h(x+y)=0の分解・全係数恒等式を検証済み。証明はcubic_normal_order2_arrows.tex。

非中央正規一次楕円境界部分では位数2の被覆・全許容条件・全幾何学的矢と位数3のBH54を得た。相対intrinsic圏の全stack降下、中央無限位数の全bad値、正規一次境界のないH3の被覆は未完成。全H3にこの境界があるとは主張しない。次は有限end dg模型を用いた中央無限位数のsmoothness locusと、境界被覆の欠落を調べる。

### 四shift windowと独立Nakayama監査

全正規三次商でBのKoszul分解をRへtensorするとTorはk,k(−3)のみなので、tailsでO(−4)→O(−3)^4→O(−2)^6→O(−1)^4→Oの完全列となる。四連続shiftで全shiftを生成。正規楕円境界認識済H3ではE=O⊕O1⊕O2⊕O3がDbのclassical generator、EnddgのH0dim55,H2dim21。76次元最小A∞台を得るが高次積を打ち切っていない。Toën math/0609762v3の有限An定理は両側smooth properを仮定し、Lemma3.14はquasicompactnessなので、これだけで中央無限位数bad D有限性を主張しない。

h=b=c=1のClifford swap包絡でKoszul双対を独立計算しE0..4=(1,4,6,4,1)、左右Frobenius積非退化、mu_E=swapxy(t,z固定)、mu_B=−swapxy(t,z負)、普通detmu_B−1・top作用1を確認。全次数AS4は別のcocycle証明による。

Clifford swapの中心模型は証明・原稿化した（classification-v40）。u=x+y,v=x−y,w=z+h u/2、A=u²,B=v²,C=w²,D={u,w}/2,a=vw,s={u,v}とする。G*=−[vw,u]/4なのでa,sがRで中心、T=t²,P=xy+yx,Z=z²は包絡で既に中心。Delta可逆ならT,P,Z↔B,C,Dは可逆で、五中心二次の全関係は三scroll minor BC−a²,Cs−2Da,as−2DB。Rは中心subring C上Clifford有限、Hilbert比rank8、generic三変数Cliffordの偶部分rank4 quaternion。normal cubic scroll Cの正規性によりZ(R^2)=C、ProjZ(R)=F1、PI degree2を証明した。Omega=(uw−D)t中心三次でOmega²=T(D²−AC)。qgrRはF1上rank4 quaternion order、tau²はhyperplane E+2F twist。全分岐と極大性も次の通り証明した。検証器はh=b=c=1で中心二次dim5、対称積rank12、全minor、volume交換子恒等式を独立確認。平面conic Γ_h=−2(1+h³)ξr+3h²r²+h(h³−8)s²/4 と Q=L2 ξ²−4(h²b−c)ξr+4hb r²+L1 s²（L1=hc−2b,L2=(h³−2)b−3hc）を得た。detQ=−4L1(c²+h²bc+2hb²)、L2zeroはQ=Γ自身。四bad方向は三singular conicsと一致member。許容conicはΓと四点横断。F1=Bl_pP2,p=[1:0:0]でgeneric quaternion symbol(−T/C,(D²−AC)/C²)のBrauer分岐は二conicのstrict/pullbackそのもの、例外E/fibreには分岐なし。分岐類3E4F、K+半分岐=−(E2F)/2、klt log del Pezzo degree3/4でrank4を掛けるとcubicdegree3。

Λ=~R²はB,C,D,sの四patchで三生成Cliffordとなりlocallyfree rank4。全閉完備局所模型は分岐外Mat2formalplane、smoothbranchはreflection skewgroup、四nodeではquantumformalplaneq−。各gl2。余次元1の非平方residueにより巡回valuation最大order、反射性で大域最大order。完成後最大性を主張しない。表示族のcommondegree scalar rigidificationは有限対角の分離既約DMstack2、generic inertia mu2²、任意底変更/fpqc局所表示族の降下を得た。抽象intrinsic Abel圏族との完全同一視は残る。

次は中央無限位数の全bad値・相対smoothness（有限76次元cohomologyだけでは高次A∞を省けない）と、正規一次楕円境界を持たないH3の被覆を進める。

### 三角境界のq-so3 Casimir pencil

q²+q+1=0、B=(t central; yz−qzy=tx,zx−qxz=ty,xy−qyx=tz)は既証PBW CY AS4。f=(1−q)/3,e=−(2q+1)/9,f³=e,e²=−1/27。V=B/(t−1)の中心はChebyshev X=x³+q²x cyclicとOmega=xyz+(q−1)(x²+z²)/3+(q+2)y²/3、関係Omega³+f Omega²−XYZ+eΣX²=0。Vはk[X,Y,Z]上free27、中心3foldに五つのODP。CY双対/filtered maximalityでVは対称MCM最大order、正則中心上Azumaya。

G_D=Omega_h+D t³、U=V/(Omega+D)の全中心はFricke XYZ−eΣX²+D²(D−f)=0。中心特異Dは0,f（各A1一つ）、2f/3,−f/3（各A1四つ）。Vの五characterはD0と2f/3に配置され、PI3のA1 McKay(1,2)で両値good。Df,−f3はV centre正則上でU=Mat3(singular centre)となりbad。compact中心C_Dは∞triangleで常にsmooth。辺のdegree0 radical v=ty^-1はv³=(T/Y)(1+q²v²),J³=(T),residue k(u)/k(u³)。非可換DVRでmax/PI3division、辺coverは両端totallyram3。CHI2.7/2.17 terminal theoremで∞全localgl2。従って全H3 iff(D−f)(3D+f)!=0、全Rdomain。

Bのcentre1=kt、V character五点だからBはskewでない（skewなら中央tを外すと量子3変数のcoordinate axes characters）。B CYのため非中央normal smoothE境界なら既証m3skewFermatに限られるが矛盾。唯一の中央t境界はtriangle。よって許容Rは既研究normal smoothE locusの外に実在し、missing-boundaryの一部分を埋める。証明cubic_quantum_triangle.tex、厳密validator/certificateはquantum_triangle。全intrinsic矢も確定：D不変、Aut_gr B=Gm×A4、次数scalarを除く慣性A4が全Dで一定。固有値差unitとcross linear係数比較により非被約底でも追加矢なし。相対rigidified表示stackはgood Dline×BA4、全中心形成も任意basechangeに適合。次は一般qの三角境界をq-difference/GWA模型で調べ、中央無限位数と他missing boundaryへ進む。全H3被覆は未完成。

一般qの三角境界（classification-v47）：q!=0,+-1の全V_qに対し、q-difference表示の三関係とOmega=-Dを全係数で厳密検算し、PBW最高T係数のChebyshev独立性から全U_{q,D}・R_{q,D}の忠実性と整域性を証明した。B_qはCY AS4。非捩れでは全中心k[t,Omega_h]、位数N>=3ではChebyshev c_N(x),c_N(y),c_N(z),Omegaが全中心を生成。非捩れまたはN>3の全H3候補はこのpencilに限る。全候補graded矢は[Q/S4]、Q={(q,D):q!=0,+-1}、A4は基底に自明、奇置換は(q,D)->(q^-1,-q²D)。候補表示stackは分離DM2で慣性A4、任意基底のgraded同型functorを記述する。奇数位数N>=3ではclassification-v50で全判定を得た：全中心はFricke XYZ+alphaΣX²+beta_N(D)=0、alpha=(q²−1)^−N、beta_N=−(q²−1)^−3N[2+P_N(w_D)]、w_D=−(q+q^-1)−(q²−1)³D/q²。特異DはN+1個、端点w=+-2の二値D±だけが非H3。全N−1内部特異値は、古典型w=−(q^d+q^-d)と非古典型w=q^(2d)+q^(-2d)、1<=d<=(N−1)/2の明示既約三重対角表示で全A1点に次元d<Nのsimpleが存在し、McKay( r,N−r )が両方正。無限遠triangleは指数Nのterminal order。従ってH3 iff(D−D+)(D−D−)!=0。位数5では独立な全係数2x2表示とPhi5中心配置も確認。任意奇数Nの表現再帰・Casimirは形式Q=q^d,J=q^j,R²=−q²/Qで厳密検算済み。次は偶数位数と非捩れqの全許容条件を調べる。一般q全体のH3開性・抽象intrinsic family比較は未証明。証明cubic_quantum_triangle_general.tex、検算verify_cubic_quantum_triangle_difference.py。

偶数位数の三角境界（classification-v52）：N=2M>=4、Gamma_i=−(q²−1)^N c_N(x_i)、k=2+P_M(w_D)により全中心はGamma_x Gamma_y Gamma_z−ΣGamma_i²−2kΣGamma_i−k²−4k+4=0。Huang1509.08719v4 eq5/§4.3を正規化して使用し、N4は独立PBW次数12で全関係を検算した。k!=0,4は持続A1三点、k0四A1、k4一D4。両端対角bのM次元三重対角表示が全k!=4の持続三点を覆う。k0内部の追加点には古典型r<M（既存M-simpleとA1 rank和2Mの排他性で追加点配置を証明）、k4内部には非古典型四つのd-simpleと古典型r=M−2dを置いて全五McKay指標を覆う。従って全D!=D±はH3。D+はM奇数ならAzumayaの特異A1中心商、M偶数なら四つのM/2-simpleでrankを使い切るD4なので常にbad。D−もclassification-v53で全偶数位数に対してbadと証明した。c_M(x)がy,zと反交換する正規元で、D4中心fiberでは二乗零なので各simple上零。xはM個の相異なるweightに分解し、関係式/Casimirの二元一次系（行列式はqの奇数冪−1の積）から全隣接block合成が非零scalarとなる。従って全simple次元はMの正倍数、full D4ならrank>=6MだがPI次数2Mなので不可能。これで全有限位数q!=+-1についてH3 iffD!=D±を完全判定した。中心・order・表現・全矢の分類は指定pencil内の主張であり全H3被覆ではない。粗座標theta=q+q^-1,w=−theta−h³D/q²を得て、候補stackはtheta!=+-2の平面上のA4共役twist中立gerbe。固定NのH3表示stackはphi(N)/2個の(A1_w minus{+-2})×BA4、全中心形成は任意基底変更と可換。全有限位数許容族は正規smoothE境界を持たず候補空間に稠密。次は非捩れqの許容条件と全H3のmissing-boundary被覆を進める。1998 HKP math/9805048は根付き単位での表現を構成するが序文に完全性未証明と明記するため、全既約表現分類として輸入していない。


非捩れ三角境界（classification-v55）：f_j(x)=x²−kappa²(q^j+q^-j)²の左右Ore集合を、左/右x乗法の2x2行列でdet f_j(M)=f_(j-1) f_(j+1)と証明した。局所化U_SはGWA G=A0(sigma,a_D)の反転固定環。A0=k[u±,r(q^ju)^−1:j∈Z]、r=u−u^-1、a_D=(u²+q²u^-2+1+q²)/(q²−1)²+(q²−1)D/q、A=rT,B=rbT^-1。反転u->u^-1,A->−B,B->−A、反不変単元rによりaveraging e fullなのでG#Z2とMorita同値。Bavula著者講義Theorem3.1（Dedekind基底そのものの定理）を一次監査：重根はgl∞、単根はgl<=2。非捩れqでD±の重根u²=−q,qは除去軌道u²=q^(2j)から外れるためU_SもUもgl∞、従って全非捩れ端点も非H3。D!=D±ではU_S gl<=2だが、U自体と射影無限遠の許容性は未証明。式はverify_cubic_quantum_triangle_gwa.pyで全有理式検算、証明cubic_quantum_triangle_gwa.tex。

次の具体的着手：射影頂点[x:0:0:0]でPBW重みw(x)=0,w(y)=w(z)=1,w(t)=2を使う。各PBW還元は重みを下げず、先頭環でxは正規なのでxの形式的microlocalizationを取れる。degree0先頭環はa=y/x,b=z/x,s=t/xの量子Heisenberg as=qsa,bs=q^-1sb,q^-1ab−q²ba=s。G/x³の先頭はq^-1ab+s/(q²−1)=q/(q²−1)(ab−qba)、正則正規なので形式的頂点商の先頭環が厳密に量子平面となることを証明した（classification-v56）。PBW重みの降下濾過と形式x-microlocalizationで先頭環を計算し、正則先頭元の商と完備filtered-graded分解の持上げで局所gl2。非捩れqでは座標変更係数1−q^(1−i),1−q^(1−j)の片方が高次単項式ごとに非零なので、全高次補正を消して完備量子平面に同型。証明cubic_quantum_triangle_vertex.tex、検算vertex。qgrへのperfection降下はまだ未証明であり、形式局所環gl2だけで全境界smoothとは結論しない。

文献上の障害：Kaplan–Schedler ANT2023「Multiplicative preprojective algebras are2-CY」は一次PDFを読むとTheorem1.2がunoriented cycleを含むquiverに限定され、affineD4はConjecture1.1の範囲。検索snippetがこの仮定を省くので誤輸入しない。EOR math/0406480 §11はlegパラメータdistinct時のMPLAとのMorita対応であり、全DAHAパラメータで有限globaldimを保証していない。これらを非捩れpencil全H3の証明として使わない。


proper楕円四次元Sklyaninの全排除（classification-v58）：標数0代数閉体上、滑らかなE、degL4、sigma translationで位数nが∞又は1,2,4以外の標準Sを全排除した。g1,g2中央二次正則列のTHCR商と中山公式でmuS=id。n∞及び有限n>3は中心重みからZ3=0。残余n3はcentre z0..z3(deg3),g1,g2(deg2)、二つの六次完全交叉、Z3dim4、S1dim4、PIdegree3である。

一般norm補題：connected graded domain Bが正規中心Z上有限、PIdegree n>=2なら、Nrd:B1->Z_nはbasepointfreeなn次写像。射影normのpullbackO1=O(n)がampleなので像へfinite、従ってdimZ_n>=dimB1。等号なら射影全射、各Gは一次元ellのnorm、Cayley-Hamiltonでell times degree(n-1)へ分解する。商に零因子が生じる。よってCY・normal-centre-finite・PI3のH3包絡にはdimZ3>=5が必要。SklyaninN3は等号dim4で全Gが一次式×二次式となり排除される。射影norm P3->P3はdegree27。複素数への限定やgenericGへの限定は不要。退化非楕円Sklyaninや任意Zhang twistは含まない。

一次資料WWY1802.06487v2 Lemma2.9,Props2.11/2.12/2.18,Thm3.13を読み、regularseq/domain/centre/normalityを使用。as4最新429d8a3...は4entrypointsの現行概要とSklyanin/CY claimを参照したが新定理輸入なし。検算verify_cubic_sklyanin_rank_obstruction.pyは重みHilbert・a-invariant−1・rank9・K²1/3と、一般traceless3x3行列のnorm因数分解を厳密検算。全排除はprojective normの通常の証明であり有限標本からの外挿でない。第三者独立査読・形式検証・新規性確認は未実施。

独立な複素幾何補題も保持：商特異点だけのprojective Q-delPezzo上のorderがcodim1 AzumayaかつH1Lambda0ならgeneric Brauer類は零。traceでq0、quotientresolutionはKod−∞でrational、small quotient群GのH2(G,Z)=0をS3/Gから示して例外residueを消し、Br rational resolution0を用いる。Sklyanin排除にはこの補題へ依存する必要はなく、norm補題の直接証明を正本とする。


三乗根量子so3固定包絡の全切断（classification-v60）：全ZB3=P4[alphaOmega+betaX+gammaY+deltaZ+epsilon t³]を判定。線型元のnormは b³X+c³Y+d³Z−3q bcd Omega+(a³+q²a(b²+c²+d²))t³、像は正確にDelta=alpha³+27beta gamma delta=0の三次超曲面。全Delta0 cutは一次×二次に因数分解しnondomain。Delta!=0では境界はsmoothE、I1 nodalcubic、I2 line+conic、I3triangleの四種、phi=diag(1,q,q²)は各成分でdegree3、node両枝でfullyram3。centre境界滑らか、terminalorderでlocalgl2、非自明residueでgenericdivision3、全商domain。

Compact centreをS=3Omega/2f,U=X/2e cyclic,T=t³で正規化するとY:2UVW−T(U²+V²+W²)+3TS²+2S³=0 inP4。五ODP p0=(0,0,0,0,1),p_eta=(−1,eta1,eta2,eta3,1),eta product1。全四点rank4なのでplaneを含まず、全hyperplane section integral。H3 iff Delta!=0 andH notinY^dual。Yregular点のtangent cutはAzumaya singularcentreでbad、Ynodeで非退化A1ならonecharでfullMcKay(1,2)、退化rank2ならA2以上でonechar/PI3rankがfullMcKayを阻む。全矢・相対graded表示stack=[U/A4]、分離既約DM4、generic inertia1。全慣性は1,C2（v=(beta,gamma,delta)座標軸）,C3（四符号軸）,A4（v0）だけ。C2/C3固定planeはdim2、A4pencilはdim1、異なるplaneはpencilで交わる。表示族flat、全中心commutes任意basechange、fpqc降下。抽象intrinsic圏族の全被覆や全H3のcomponent性は未主張。

有限判定：affT1のF1=2UVW−ΣU²+3S²+2S³、H=aS+bU+cV+dW+epsilon0についてF1=H=0,gradF1=lambda(a,b,c,d),lambda!=0が空、かつHの通る各五nodeで法線Hessian逆二次式!=0。Groebner unit idealと五二次式で全切断を判定できる。検証full_cutsはuniversalPBWnorm、norm cubic、五node・全四点rank・inverseHessian、Casimirpencil bad2値との一致、H=S/S+U/U+V+Wのgood examplesとA4/C2/C3慣性をexact確認。論文cubic_quantum_triangle_full_cuts.tex。次は非捩れ一般qの残るadmissibility、未被覆CY/非CY包絡、全大域component/交叉/abstractfamily比較を進める。


三乗根共鳴incidenceと境界閉包（classification-v61）：任意非被約底で全中心三次はalphaOmega_q+beta c3x+gamma c3y+delta c3z+epsilon t³、正確な条件は(q²+q+1)(beta,gamma,delta)=0。最高active次数でq−1,q²−1の単元比較により証明。被約incidenceは水平2次元と二つの垂直P4、交叉P1。qroot3、alpha1の局所式u beta=u gamma=u delta=0（u=q−q0）でdim2と4がdim1curveで交わり、接空間dim5。全候補矢はS4商、奇置換(q;alpha,beta,gamma,delta,epsilon)->(q^-1;qalpha,gamma,beta,delta,−q³epsilon)。整域fiber locusはDelta=alpha³+27beta gamma delta!=0。候補成分を全H3成分と呼ばない。

固定三乗根U/A4ではintrinsic normal smoothE locusが正確にbeta gamma delta!=0。他のnormal smoothE境界はB非skew/CYと既証m3認識で排除。missing-boundary Dは3座標超平面の商として既約normal-crossing divisor、正規化[U_beta0/V4]。I1/I2/I3のdim3/2/1、慣性1/C2/A4、全てsmoothE H3の特殊化。alpha1粗chartはepsilonとtetrahedral不変P=Σbeta²,Q=beta gamma delta,R=Σbeta²gamma²,J=平方差三積、J²=P²R²−4R³−4P³Q²−27Q4+18PRQ²。I2横断coarseA1、smoothE-C3横断A2、I3はA3/A4×curve。粗境界Q0はJ²=R²(P²−4R)、正規化A=gamma²,B=delta²でP=A+B,R=AB,J=AB(B−A)。証明cubic_quantum_triangle_incidence.tex、検算incidenceは普遍comm/divisibility/q反転と全12不変式、Molien一致を厳密確認。


一般Zhang/cocycle twist包絡の排除（classification-v63）：A noethKoszulAS4 domain、B=A^phi、eta=hdet phiとすると、W1(B)はphi安定なので非零eigen F(phiF=lambda F)を選べる。untwistするとFv=theta(v)F,theta=lambda eta^-1 phi muA^-1。このnormalizerはZAをpointwise固定する。量子QではNewton normalizerがdiagonalなのでphi diagonal、全Zhang twistsQのH3は既存skew五型31coordsだけ。単冪/半単純の仮定不要。

properSklyanin Sでalpha beta gamma非零かつ中央quadric pencilの4固有値distinctを明示仮定。Sym²S1->S2 injective（六関係の交代射影非退化）なのでtheta g1=g1,theta g2=g2はordinary quadraticformsの厳密保存。pencil作用素distinct固有値よりtheta diagonal±、関係式よりeven sign。phi scalar times signであり、非自明case(1,1,−1,−1)のtwistはrescale(1,−i b c,i c,b),beta=b²,gamma=c²でS(alpha,beta^-1,gamma^-1)へ同型。六関係を全係数で単元倍比較した。点Eの作用は二捩れtranslation、4tau不変なのでpropernnotdiv4のまま、前節norm排除で全ZhangtwistH3を除外。退化pencilには適用しない。

標準V4cocycle mu((p,q),(r,s))=(−1)^(ps)、degxiが4群次数を各一回持つDavies twistも除外。CYはsign group top hdet1（中央quadric正則列とtranslation THCRcanonicalから）とKoszulFrobenius topGdegree0により証明。centerはGgraded、中心成分F_gをuntwistするとnormalizer theta_g=alternating bicharacter sign、theta_g F_g=F_gなのでF_gはS^(theta_g)でcentral。新translationtau_g=tau−s_g(E2)がorder3の場合だけ存在し、3tau=s_gなので高々一つのg。従って中心3はn3又は6の時だけdim1、それ以外0。唯一の生成元は標準PI3centreのG-degree gのzi=xi³+xi*(centralquadric)、quadricはGdegree0、theta_gもcocycleも積xi*Qを変えないので全cubiccutsnondomain。

証明cubic_twisted_envelope_exclusions.tex、検証器twisted_envelope_exclusionsは全六符号関係・param式・centralpencil固有値差・alternatingprojection・cocycle16tableをexact確認。一次資料Davies1512.05717v2の(3.4),(3.5),(4.3)を読みgrading/cocycle規約だけ使用。Hyp4.1のinfiniteorder point/fatpoint結果を有限位数へ輸入しない。AS4性全specialをこの資料から無条件に推論していない。抽象有限群cocycle、任意twisting systems、退化/他exoticelliptic全体の被覆は未主張。


Stafford型と標準cocycle全族の排除（classification-v68）：Davies1502.06101§6.1の全許容領域T（alpha,beta,gamma!=0,+-1,alpha+beta+gamma+alpha beta gamma0）、d∈P1から指定二禁止値を除くS_infinity,S_d1,S_d2と標準Klein cocycle、循環変種は全てH3包絡から排除した。退化/他exotic楕円/全AS4の被覆は未主張。

全TでNakayamaは通常(-I,diag--++,diag++--)、cocycle後(-I,-I,I)。群作用により対角、平方関係からmu=lambda*sign、hdetmu1からlambda8=1、族Frobenius pairingの正則性と既約性で一定とし、QQの一点計算で定数を決定。低次数計算だけからAS4性を推論せずDaviesThm6.1.10を入力。全Tの五関係上でg1,g2は中央、除いたfiはmuで正規、残余中心二次qとfiはTHCRへの核の正則正規列。W1はTHCRへ単射（核ならG=ell q、q中央でellも正規一次となるがTHCRで不可能）。

point curveの二次式は中心g1,g2と異なる：v0²+v1²+v2²+v3²=0,(1+beta)v1²+(1−alpha)v2²+(1+alpha beta)v3²=0。WWY1802.06487v2 Definition-Lemma2.4,(2.5)のsigmaをE点(0:r:s:1),r²=−a(1+b)/(a+b),s²=b(a−1)/(a+b)で反復。第二反復の第一係数−4(a+1)(a+b)(b−1)非零から4tau!=0が全Tで従う。第三正規化座標の条件u3=2(a+b)(ab−3a−b−1)KLM,v3+z3=−2(a−1)L²M²,w3−z3=2a(b+1)K²L²。K=ab+a−b+3,L=ab+a+3b−1,M=3ab−a+b+1。K=M0は(a−1)M−(3a+1)K=−4(a+1)²で不可、L0上z3=1024(a−1)²(a+1)^6/(a+3)^5非零。正規化第三座標は全Tで非零なのでK²除去はregular sigma³への延長で正当化される。従ってsigma³=theta_e1 iffL0、chart欠落なし。固定点不在は正しいpoint curve二式で確認済み。

通常Sd1/Sd2のW1はL!=0で0、L0でdim2。L0を(alpha,beta,gamma)=(a,(1−a)/(a+3),(a+1)/(a−3))、a!=0,+-1,+-3で表示。Sd1はF2=x2Q2,F3=x3Q3、Sd2はF0=x0Q0,F1=x1Q1で、全a,dにおいて非零・独立。THCRのnormalizer付き三次の比はsigma不変、自由な六重商上degree2の切断へ入るのでdim<=2。両pencilは一次因子s x2+t x3又はs x0+t x1で覆われ、明示degree3 basepointfree写像P1->P(W1)が全射なので全Gfactor。Q0..Q3,H,H0の式はcubic_stafford_exclusions.tex。

残余CY cocycleSd2の中心群次数gをuntwistしてnormalizer theta_gを得る。h=g+e1による通常の符号Zhang twistはStafford同士へ移り、h=e1は(a,b^-1,c^-1),d'=−(d+1+bc)/(bc)で偶奇保存、h=e2は(a^-1,b,c^-1),d'=−(d+1+c)/c、h=e1+e2は(a^-1,b^-1,c),d'=(d−b+1)/bで偶奇交換。全六関係・pencil・禁止値の対応をexact検証。中心成分は変換先W1_gと線型同型。従って群次数0/e1/e2/e1+e2の中心三次はK/L/N/M=0でだけ各dim1、N=ab−3a−b−1。四曲線はTで互いに素。生成元はxj times群次数0のquadricで符号Zhang/cocycleでも因子が保たれ、全切断nondomain。

検証器verify_cubic_stafford.py（六QQ Frobenius/rank witness）、stafford_resonance.py、stafford_resonance_even.py（全係数factor identity）、sklyanin_order6.py（全T反復）、stafford_transport.py（QQ(a,b)中央二次24式、三符号関係・pencil・禁止値・六対のdisjoint Groebner）を実行。全specialへの延長とTHCR次元評価は原稿の通常の証明であり有限標本外挿でない。全H3の被覆、非捩れ量子so3の残るaffine/qgr admissibility、退化/他exotic包絡、大域成分・抽象intrinsic族降下は未完。次は非捩れqの特殊weight軌道または残る未被覆包絡を進める。


低交換子as4表示の独立排除（classification-v69）：as4のa45f834f51a00c47443b51caf66abaf4629546b9を四entrypointとCY統合/CI22概要、二重被覆DCC1・長さ四CF2/CF3・長さ3+1CT2の具体的表示について参照。全CY被覆やAS4存在/整域/noetherian定理は新規入力にしていない。二重被覆の二族h!=0は、H3包絡を仮定したKoszul AS4双対の最高次数汎関数をQQ(i)[h,h^-1]上で独立構成し、全次数四関係を消す恒等式と左右pairingdet=+-1/(2h²)を確認して全hのmu=idを得る。一般点rrefだけでAS4十分性や特殊fiber平坦性を推論しない。a²,b²の正規作用は互いに反対符号、N=a²b²のnormalizer=-Iなのでdomainでは奇数centre0。一般にNが-Iを実現するH3包絡ならmu(N)=-Nが必要。CF2/CF3とCT2の三つの固定表示も独立Frobenius計算でmu=id、中心3の140x20行列に非零20minorがあり全排除。検算verify_cubic_as4_double_cover.pyとverify_cubic_as4_curvilinear_fixed.py、原稿cubic_as4_low_commutator_exclusions.tex。表示の借用と独立検算を、as4全分類の輸入と区別する。次はTT22の六表示の中心3/正規元を調べる。


TT22六表示の直接全排除（classification-v70）：as4固定commit a45f834... のCY_ZERO_COMMUTATORS_CURVILINEAR_TWO_TWO_COMPLETE.tex TT1-TT3から六表示のみ参照し、全射影型の被覆/AS4十分性は輸入しない。C_r(r!=0,+-1/4)をq=(4r+1)/(4r−1)で表示し、四DiamondからPBW b^i d^j a^k c^l、中央変数z1,z2上の量子トーラスdb=q^-1bdへの忠実模型a=z1 b^-1−kappa q²b^-1d²,c=z2d^-1−eta b²d^-1を構成。kappa=1/(2(q²−1)),eta=2q(q−1)/(q+1)。z1=ab+kappa d²,z2=cd+eta b²中央。先頭z1^k z2^l b^(i-k)d^(j-l)の比較からcentre3はq³!=1で0、q³1でa³,b³,c³,d³のdim4。この条件は48r²+1=0。三乗根ではdivision量子トーラスがcentre上rank9、Tr ell0、Tr ell²/2=3(uvz1+wtz2)。Nrd ell=ell(ell²−3(uvz1+wtz2))がBのcentre3へ入り、非零ellのnorm非零なのでP3->P3全射、全Gfactor。centre有限/正規の別入力は不要。generic determinantの他の零16r²+1,16r²+3はcentre0であり、最終証明はmatrixchartでなく上の全q先頭項論法。

E_t(t!=0,-2),F_h(allh)ではb,dが正規、N=bdのnormalizerはE_tで−I+二乗零nilpotent（a->−a+(t+2)b/(2t),c->−c+4(t+2)d,b/d->負）、F_hで−I。normalizerの半単純部分−Iなら整域の奇数centre0という一般補題で全排除。三固定A,B,DもQQ(i)/QQ上でcentre3 rank20をexact確認。全表示のmu=idは、対称射影U固定のRとA0=半Hess(-z2z5+z3z4−z0z1+z5²)による非零w=R A0 R^Tが巡回−という256恒等式からAS4実現の下で独立に従う。AS4最高Koszul線にwが入り双対FrobeniusmuE=-Iになるためで、存在十分性を低次数rankから推論しない。検算verify_cubic_as4_tt22_c.py/tt22_remaining.py、論文cubic_as4_tt22_exclusions.tex。次はTT211と四単純基点の未処理表示、または非捩れqso3の特殊weight軌道を進める。


DS211第二層二族の全排除（classification-v71）：as4同commitのDS1/DS2/DT1具体表示だけを参照。A_(l,r),l!=0,+-1/4は量子3平面S(b,c,d)上のcanonical Ore。q=(4l+1)/(4l−1),sigma=(1,q^-1,q),delta=(beta b²,u bc,v bd),beta=−1/(4l),u=−(16lr+1)/(2l(16l²−1)),v=8(l+r)/(16l²−1)。正規bのnormalizer単冪部分がa->a−beta bなので中心3はS3へ入る。十指数のcharacter gcdでScentre3はq3のみpurecubes三本、deltaG0からb³は消え、c³/d³はu0/v0のみ、同時零は不可。従ってBcentre3は48l²+1=0,r=3lでkc³、r=−lでkd³、他0。全Gfactor。例外B_rはc,d正規、N=c³dのnormalizer=-I+(8r−4i)E_baなので奇数centre0。AS4条件下のmu=idはA1=半Hess(-z1z4+z2z3−z0z5+z3z4)とRの非零反巡回最高tensorから独立判定。検算verify_cubic_as4_ds211.pyで四PBW diamond、全tensor係数、normalizers、三乗根comm、全十指数をexact確認。全DS211被覆はまだ輸入していない。DS3の残余も下記の全値rank coverと忠実模型により排除済み。


DS211列挙表示の全排除（classification-v72）：DS3のT_h(h!=0),U_u(u!=0)はcentre3の最大minorを全関係から構成し、Tでは(8h+1)(16h+1)/(2^23 h6)、Uでは−2^29 u6(4u−1)(48u²+8u+1)。商座標分母はTでhの冪、Uで定数のみ。座標は全関係を消し自由列でidentityなので、AS4仮定の各特殊fiberでも真の基底となる。残るT二値とU二種の値（quadric二根はQQ(sqrt−2)）を再計算して全rank20。L_±i/4,PもQQ(i)上rank20、V0もQQ上rank20。CY判定は全256反巡回最高tensor恒等式で独立に行う。一般rrefの係数だけからAS4平坦性を推論しない。

V_h(h!=-1/16)のh!=0は平方根r²=−h、p=(4r−1)/(4r+1)で全被覆。a'=a+gamma b,x=c−r d,y=c+r d、alpha=p²/(2(p+1)²),beta=1/(2(p+1)²),gamma=p/(p+1)²。四DiamondでPBW b^i x^j y^k(a')^l。中央z1,z2上の量子トーラスxb=p^-1bxにy=z2 x^-1−p b²x^-1,a'=b^-1(z1−alpha x²−beta y²)で忠実に入る（補助重みz1=3,z2=1の先頭項が相異なる）。z2=xy+p^-1b²,z1=ba'+alpha x²+beta y²中央。先頭指数からcentre3はp³!=1で0、p³1すなわちh1/48でdim4。三乗根division rank9でTr ell0,Tr ell²/2=3(uvz1+(wt+u²/4)z2)。Nrd a'=(a')³−3z2a'/4とb³,x³,y³が中心基底、全linear normはBcentre3に入りP3->P3全射なので全Gfactor。h0は固定rank20で処理。これでDS3/DT1列挙の三固定・四1param・一2paramを全排除。上流の全AS4射影型の被覆/存在十分性は依然新規輸入していない。

検証verify_cubic_as4_ds211_remaining.py（全値rank cover）とds211_v.py（全平方根被覆model/norm）を実行。共有cyclic関数は有理式の展開後に零を比較するよう正規化し、既存A/B検証も再実行済み。次は四単純基点1111の具体表示、または必要被覆定理の適用域を確認して低交換子H3候補を統合する。全H3被覆・抽象族降下・非捩れ量子so3残余は未完。


四単純基点FS4の全S(lambda,t)と標準Klein cocycleも排除した（classification-v73）。proper部分は既証Sklyaninへ帰着、三つの退化曲線はS(1,-1,s)の正規二次N1=a²+d²,N2=b²−c²の積が−Iを実現するため奇数centre0。FZ2のQ共有係数族は六対とも可逆skew係数なので既存skew分類に含まれる。表示のみ参照し全四単純基点/全CY被覆は未輸入。次は残るO/H共有零境界とfull-shared表示を調べる。

境界normalityはQQ(s)の三次関係moduleで八恒等式を証明し、係数分母はs,s±1のみ。最高反巡回tensor w=R A R^Tは非零かつKlein次数0なのでAS4実現の下で通常/標準cocycleともmu=id。全値AS4存在・平坦性をgeneric rrefから推論していない。原稿cubic_as4_four_simple_exclusions.tex、検証verify_cubic_as4_four_simple.py。任意境界Zhang twistと全H3被覆は未完。


共有頂点係数零の残余O/H表示も全排除した（classification-v74）。Oは四DiamondのPBWと正規a,bのcharacterにより中心三次がc³又はd³一本に限られる。正確な共鳴はlambda=-1/2,A²=-3/64でkc³、A²=-1/192でkd³、他0なので全切断分解。H0/H1は分母なし商座標と最大minor16384lambda^12(lambda+1)^9(2lambda+1)^4(4lambda+1)(4lambda+3)、三例外値のQQ rank20で全中心三次零。最高反巡回tensorからAS4仮定下mu=id。従ってFZ2/FZ4/FZ5/FS4列挙はskew部分だけが残る。全CY/四単純基点被覆は未輸入。次は共有頂点非零full-sharedの具体表示を調べる。
検証verify_cubic_as4_four_simple_remaining.py。AS4性を仮定して必要条件で排除しており、AS4十分性・全同型・full atlas coverageは輸入しない。中心rank coverは両generic投影の全関係消滅と自由列identityを確認し、分母1なので全特殊fiberへ適用できる。


十二共有非零P族のlambda=2切片を両符号・全r!=1,13/5で排除した（classification-v75）。三次/四次商座標分母はr−1のみ、中心行列の二つの最大minorの分子Q(deg3),P(deg5)がQQ(i)[r]で互いに素なので全閉値rank20。元の二パラメータFT3全域の最高反巡回tensorも256係数で独立検証し、AS4仮定下mu=id。全Pの非空determinant openでもH3なしだが、全lambdaの例外集合は未排除。次はP全二パラメータの残余か、共有零族の標準cocycle境界を調べる。
検算verify_cubic_as4_four_simple_p.pyは全二変数最高tensor、一変数の全関係消滅/自由列identityと分母のr−1支持、最大minor二本の厳密gcdを確認。今回python-flintで高速化して実行（数学的計算はSymPy有理関数体）。全P/全四単純基点/全CY被覆は新規輸入せず、FT3表示だけを参照。対角生成元変換だけではPの複素係数は消せない。二変数の無準備なGJ/FF消去を長時間反復せず、次は正規元・次数3 characterや全値minorの分母制御を優先する。


共有零O/Hの標準Klein cocycleも全排除した（classification-v76）。Oは(r,s)を(r,−s)へ替えた同じPBW、r,s!=0,+-1の二十characterから全中心三次が純三乗一本以下となる（rs=1を除外しない）。H0/H1のcocycleはgeneric rank20、lambda−1/2でrank20、lambda−1/4/−3/4ではrank19でそれぞれd(d²−3c²),c(d²−c²/3)の中心一本。全候補分解。最高tensorのtwist pairing A^c=A diag(1,1,−1,−1,1,1)を全係数で確認しAS4仮定下mu=id。これで列挙共有零表示と標準cocycleのH3はskewだけ。次はP全二パラメータ残余・他の共有非零支持、または非捩れ量子so3の許容性を進める。
検証verify_cubic_as4_four_simple_cocycles.py。通常Hとcocycle Hでgeneric最大minorは一致するが特殊値のkernelは異なるため、通常の全値rank20を流用しない。二例外のrank19と明示factored generatorを別計算済み。全CY/全四単純基点の被覆は未輸入、全intrinsic family降下等の大域未完部分も維持する。


最初の共有係数FN3の七列挙表示も全排除した（classification-v77）。L/MをB(1;h/4,0,f,0)へ統一し、四Diamond/Ore PBW、normal adのcharacterからh0,h²−1,h²−3だけへ絞る。h0ではbc−2f adが−Iを実現、他二共鳴では候補4/2本とaの交換子が単射なので全centre3零。F0/F1のgeneric最大minorはlambda^6(lambda−1)^(4+eps)(lambda+1)^(6+eps)(lambda²+1)^(2−eps)(lambda²−lambda+1)(lambda²+lambda+1)/2^(40+2eps)。商分母lambda,lambda±1,lambda²+1と全七例外値を合わせ、QQ/QQ(i)/QQ(sqrt−3)の独立rank20で全値centre3零。G0/G1/KもQQ rank20。全mu判定は最高反巡回tensorで独立。次は第五係数零のM_p二族と固定N/C、他の共有非零表示、P全二パラメータ残余を進める。
原稿cubic_as4_first_shared_exclusions.tex、検証verify_cubic_as4_four_simple_first.pyとfirst_remaining.py。fn_matrixは全入力をSymPy exactへ先に変換し、整数e/16のPython float化を避ける。L/M検証もこの修正後に再実行し、F0/F1全値rank coverと三固定表示を実行済み。FN3の具体七表示のみ参照し、上流全chart被覆・AS4存在十分性・全同型は輸入しない。全H3被覆、P全残余、非捩れqso3許容性、大域成分と抽象intrinsic族降下は未完。


第五係数零のM_p^0/M_p^1と固定N/Cも全排除した（classification-v78）。generic中心minorは(3p+1)/(2^33(p−1)^11)と(p+3)(3p+1)/(2^23(p−1)^13)、商分母p−1だけ。p−1/3とeps1のp−3をQQで別計算し全rank20。N/CはQQ(sqrt−3)/QQ(i)でrank20、係数共役も含む。全AS4実現のmu=idを最高反巡回tensorで独立確認。境界R±_1は未処理なので第五係数零全被覆とは呼ばない。次は第二共有の実係数二変数H_(lambda,p)を分母制御付きで調べ、R/J/T境界とP全残余を進める。
原稿cubic_as4_zero_fifth_exclusions.tex、検証verify_cubic_as4_four_simple_zero_fifth.pyを実行済み。上流FZ2/FZ3/FB2の表示だけを参照し、AS4存在十分性・全同型・全chart被覆は輸入しない。第二共有HのQQ(lambda,p)消去は疎な関係行列とDomainMatrix内の商射影で試し、一段ごとの出力と上限を設ける。重いGaussian二変数Pの無準備な消去とは分ける。全H3被覆・非捩れqso3許容性・大域成分・抽象intrinsic族降下は未完。


第二共有FO2の二パラメータH_(lambda,p)を全値排除した（classification-v79）。generic商分母lambda,lambda±1,p−1だけ、中心minor=lambda6(lambda−1)^4(lambda+1)^5 D1 D2/(2^40(p−1)^13)、D1=lambda²+(2lambda+1)p,D2=lambda²+lambda p+lambda+1。lambda1直線、D1/D2二曲線を全関係から別計算し、minor m0=(3p+1)/(2^33(p−1)^11),m1=−lambda7(lambda−1)^4(2lambda+1)^10/(2^40(lambda+1)^15),m2=−lambda17(lambda−1)^3/(2^37(lambda+1)^15)。最後(1,−1/3)をQQ rank20で排除。全中心3零、mu=idは全二変数最高tensorで独立確認。次は一般境界R_lambda、純虚J_h、隣接TとP全残余を進める。
原稿cubic_as4_second_shared_exclusions.tex、検証verify_cubic_as4_four_simple_second.pyを実行。疎なQQ(lambda,p)関係行列と係数体内のDomainMatrix商射影で全関係恒等式を保持。curveBの分数体detがSymPy HeuristicGCDFailedとなる場合は、行毎分母を払ったQQ[lambda]行列のdetと分母対角detの多項式交差積で厳密検証する。これは数学的例外でない。FO2具体表示のみを参照し、上流全chart/CY被覆・AS4十分性・全同型を輸入しない。未被覆のR/J/T/P、非捩れqso3許容性、大域成分・抽象intrinsic族降下は未完。


一般行列式零境界R_lambdaの全許容lambda・両符号も排除した（classification-v80）。右Zhang twist A=D^psi に同次数の非零中心元q1,q2（psi指標chi1,chi2）があれば、Z(D)_n!=0は(chi1/chi2)^n=1を必要とする。Rを固定可逆基底とtwistでFG6のA_tへ移し、非零中央a²,d²の指標−1,+1から全奇数中心を消す。六関係・基底det・最高tensorとQQ[t]上の八中央恒等式を独立確認し、lambda1/±iも含む。これで第五係数零の列挙M/N/CとR±_1は全排除。次は純虚J_h、隣接Tと追加二固定L、P全二パラメータ残余を進める。
原稿cubic_as4_boundary_R_exclusions.tex、検証verify_cubic_as4_four_simple_boundary_R.pyを実行済み。右規約 x*y=x psi^deg(x)(y) では At=(RのC基底)^(sigma^-1)、sigma=diag(i,−i,1,−1)。sourceの(1 tensor phi)関係表示をこの規約へ明示変換し、twistの向きを混同しない。中央二次a²/d²の恒等式はtを一切割らない。AS4の存在十分性・全同型・全CY被覆は未輸入。Zhang twistによる同値をintrinsic同型に置換せず、補助的な中心障害としてだけ使用する。全H3被覆・非捩れqso3許容性・大域成分・抽象族降下は未完。


純虚境界FI2のJ_h両符号を全値排除した（classification-v81）。全h!=0で商座標の分母はhのみ、中心20minorはeta+でi h9/2^11、eta−で(1−i)h10/2^7。両符号を別々に検証し、全hの最高反巡回tensorからAS4仮定下mu=idを確認した。h0はQQ(i)上の五次全関係行列rank966、dim58>56により独立にAS4から排除。
原稿cubic_as4_boundary_J_exclusions.tex、検証verify_cubic_as4_four_simple_boundary_J.pyを実行済み。lambda=iは固定して両etaを直接計算した。h0を一般商射影の極のまま捨てず、五次Hilbert障害で処理。FI2の具体表示だけを参照し、上流全chart/CY被覆・AS4存在十分性・全同型は輸入しない。次のAZ2二固定LはQQ(sqrt−3)でcentre3各dim1を計算確認したが、因子性・H3 admissibilityは未判定。T/P全残余、非捩れqso3許容性、大域成分・抽象族降下は未完。


隣接AZ2の二固定Lも排除した（classification-v82）。centre3は各dim1で非零だが、B=S(a,b,d)[c;sigma]、sigma+³=omega I,sigma−³=omega² Iとなる。CYの自己同型Ore包絡でsigma³が非自明scalarのとき、中心三次は零、一次因子付き、又は純base cutの三場合となり全てH3を排除できる。三乗根の場合は純base切断R=(S/G)[c;sigma]の頂点P=pi k[c]が無限高次自己Extを持つ。
原稿cubic_as4_adjacent_L_exclusions.tex。一般cone補題はB=S[z;sigma] noethKoszulAS4、G∈S3 central regularで、Rees/local dualityから全line objectのPへのHom-acyclicityを得る。C=S/G上のkの最小解消を誘導しExt^n(P,P)=beta_n、1/H_C=(1-u)^2/(1+u+u²)が非多項式なのでbeta_n>0全n。未証明のOre open globaldimやGの因子性は用いない。有限入力はverify_cubic_as4_four_simple_adjacent_L.pyでOre輸送、base関係安定性、scalarcube、CY tensor、centre3 rank19と明示生成元を実行確認。因子探索は未決でもH3排除には不要となった。AZ2表示のみ参照、上流全chart/CY被覆・AS4十分性・全同型は輸入しない。次はT/P全残余、非捩れqso3許容性、大域成分・抽象族降下。


隣接AB3の全S_zetaとT_-2両符号を独立排除した（classification-v83）。Sの元の四次全語行列はQQ(zeta)上rank219、成分分母zetaのみなので全zeta!=0でdimB4>=37>35。T^eta_-2=S_(-eta i/4)は全六関係の文字どおりの一致で確認。一般商基底の特殊化ではなく、元の全語行列のrank上界を使用した。
原稿cubic_as4_adjacent_S_exclusions.tex、検証verify_cubic_as4_four_simple_adjacent_S.pyを実行。AB2/AB3具体表示のみ参照し、Tのlambda!=-2、全CY/chart被覆、AS4十分性・全同型は未輸入。TのQQ(i)(lambda)による無準備なcentral_data消去は600秒上限で未完（数学的結論なし）。同じ計算を反復しない。次はSingular 4.4.1等の厳密多項式module計算で商射影を生成し、char0で全関係消滅・自由列identity・分母支持を独立検証する。有限体は必要なら探索だけに使い、標数零の証明としない。P全残余、非捩れqso3許容性、大域成分・抽象族降下も未完。


## 隣接T全値の排除（classification-v86）

AB2のT_lambda両符号を全lambda!=0,-1で排除した。lambda=-2はS_zetaとの文字どおりの同一性とdim4>=37、lambda=-1±iは両符号の直接QQ(i)計算でcentre3 rank20。その他はAS4実現でdim3=20,dim4=35と最高反巡回tensorによるmu=idを必要条件として使う。T1での厳密rank20と一般presentation-rank二場合分けによる独立な有限性証明も原稿に保持する。全値AS4存在を仮定しない。

三次・四次商射影は元の全語関係消滅と自由列identityをQQ[lambda]の実部/虚部恒等式で独立再生した。D3=lambda²(lambda+1)²(lambda+2)²(lambda²+2lambda+2)E、E=lambda^4+2lambda³+10lambda²+24lambda+16。共通複素因子の除去後D4=lambda³(lambda+1)^5(lambda+2)³(lambda²+2lambda+2)AB、A=lambda²+(-1+3i)lambda−2+2i、B=lambda²+(1−3i)lambda−4i。AS4 Hilbert値の非極点でのみ商基底と結論し、全値平坦性は推論しない。P4分母を実normへ戻すと不要な共役極を増やすため、複素分母を維持する。

64本全三次語から作る64×140転置交換子行列の各列を、D4との共通因子h_jだけで割る。独立検証器はh_j|D4とC_0 X=NをQQ[lambda]の実部/虚部多項式行列で検証する。Nの20列は異なる先頭行を持つ三角形で、対角零点支持はlambda(lambda+1)(lambda+2)(lambda²+2lambda+2)AC_*、C_*=lambda²+(2−4i)lambda−4i。H=ABC_*とnum H(f(lambda))は互いに素、f=-lambda/(lambda+1)。literalなgraded同型P=diag(1,-1/q,-1/q²,-1/q)P_(bd),q=lambda+1、detP=q^-4、P(f)P=Iにより二枚で全残余を覆う。従ってcentre3は零。負符号は形式lambdaを固定した係数i共役で証明書全体を移す。20本の三次語が全特殊点で商基底になるとは仮定しない。

再生verify_cubic_as4_T_projections.py 3 4、verify_cubic_as4_T_centre_lift.py。入力generate_cubic_as4_T_centre_input.py、出力整形export_cubic_as4_T_centre_lift.py。商射影・centre liftのJSON証明データを保存し、証明再生はSymPyのみ、Singular 4.4.1は生成にのみ用いる。元のGaussian分数体消去と無縮約liftstdは設定上限で未完だったが、その結果は不使用。三角再帰の実部/虚部計算とprimitive列化に変更して成功した。GitHub正本から入力生成と証明の独立検証を再開できる。

これでAB2/AB3の隣接共有境界の列挙表示は全排除。次はFT3のP全二パラメータ残余。Pはlambda2の全rと非空開集合のみ排除済み。非捩れqso3許容性、全包絡被覆・大域成分・抽象族降下も未完であり、全H3完全分類とはしない。


## 十二共有P全二パラメータの排除（classification-v88）

FT2/FT3の全P_lambda,r両符号を排除した。全二変数商射影のD3=lambda^4(lambda+1)²(r−1)²、D4=lambda^7(lambda+1)³(r−1)³a、a=2lambda²+2lambda+1。全分母はFT2領域で非零。元の全語関係消滅と自由列identityはQQ[lambda,r]の実部/虚部でSymPyとFLINTの厳密多項式積により独立検証済み。AS4実現の商基底としてのみ用い、全値AS4存在を輸入しない。

20三次語の転置交換子行列からD4の約数の列因子を除き、40×280のrealificationを作る。独立検証した多項式AX=Nでは40三角pivotを持つ。r−1の因子を除く垂直例外の被約積g(lambda)は次数30、11既約因子であり、明示式は原稿とcubic_as4_P_full_certificate.json。通常stdの基底と係数追跡liftstdの基底の正規化は異なる。通常基底の対角がlambda,r−1のみでも追跡付き基底は余分なlambda因子を持つため、それを捨てずgへ全て含めた。この点を無検証で特殊化しない。

次数付き同型lambda'=-lambda−1, r'={a−(lambda+1)²r}/lambda², eta'=etaを全六関係で確認。生成元はdiag(1,−1/64,i lambda/[8(lambda+1)],−i(lambda+1)/(8lambda))P_(ab)、det=1/4096。FT2のd,e,f,r−1はそれぞれq²/lambda², q/lambda,−q²/lambda²,−q²/lambda²倍に移り領域を保つ。gcd(g(lambda),g(−lambda−1))はlambda(lambda+1)a(2lambda+1)(4lambda²+4lambda+5)の定数倍。従って元の領域では三直線lambda=−1/2,−1/2±iだけ残る。先に複素行列を特殊化してからrealifyしたQQ[r]上の三証明書を別々に作り、全r!=1で40三角pivotとAX=Nを独立検証した。両符号は形式変数を固定した係数共役で覆う。

再現verify_cubic_as4_P_projections.py 3 4、verify_cubic_as4_P_centre_lift.py。入力はgenerate_cubic_as4_P_centre_input.py。中心検証にはpython-flintを要し、再生成にはSingular 4.4.1互換CLIも要する。巨大な出力（一般lift約64MB）は作業領域のみとし、Gitには元の商データ、生成器、独立多項式再生器、係数gと全チェックのSHAを持つ小さい記録を保存する。生成時のSingular内A*X=Nだけで終わらず、元のP商座標から行列を組み直しFLINTのQQ[lambda,r]積で全残差零を確認した。単なる数値標本や有限体検査ではない。

生成法の要点：Gaussian分数体でなく各語実/虚を隣接させたQQ(lambda,r)消去で三次・四次商を取得。元のQQ(lambda)[r]関係module GBの未完計算を反復しない。証明データは単項式係数列として保持し、巨大式のSymPy再展開を避ける。局所化した三変数moduleによる別法は180秒で未完、結果不使用。

これで現在参照した四単純基点の共有係数境界の全列挙表示はPも含めて判定できたが、上流の全chart/CY被覆はまだ輸入していない。次はこの列挙と全H3包絡の関係を監査し、未被覆領域を特定する。非捩れqso3の正のadmissibility、全包絡被覆、大域成分・交叉、抽象族降下も引き続き未完。
