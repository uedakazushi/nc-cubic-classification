# H3分類：現在の数学と検証上の注意

2026-11-19 / classification-notes-v375。

再開時には [研究方針](../00_research_plan.md) を最初に読む。本書は主原稿の詳細証明を複製するものではなく、認識、必要被覆、具体模型、反例・障害、計算規約を主題別に参照するためのノートである。
主張の所在は `papers/weak_cubic_axioms.tex` と入力される各節、実際の検証状態は `research/cubic_classification_validation.json`、外部入力は `research/as4_imports.json` を正本とする。
原稿に証明があること、限定した監査で論証を確認したこと、検証器を実行したこと、独立査読が済んだことを同一視しない。

**対象の範囲。** 強い内在的H3は、反標準環が一次生成で、その二次包絡が左右noetherian quadratic Koszul AS4型14641であることを含む。相対族は本文 `def:h3-intrinsic-family` の仮定を持つものを指す。相対Serre作用、AZ ampleな反標準orbitとその導来Homの任意noetherian底変更、二次包絡B₃の平坦性を課し、底上平坦なcoherent対象から生成する厚い圏の二対象間のRHomがA-perfectであることも含む。AS4包絡を仮定しないweakクラス、任意の平坦Abel圏変形、全AS4代数の分類とは区別する。

## 主題と証明の入口

| 主題 | 主な参照先 |
|---|---|
| 内在的認識・中山正規三次 | `cubic_nakayama_incidence.tex`, `cubic_hypersurface_frame.tex` |
| 非CYの符号型 | `cubic_order2_full_moduli.tex`, `cubic_order2_22_clifford_curved.tex` |
| 全スペクトルの排除 | `cubic_third_root_nonunit_zero_column.tex`, `cubic_four_simple_final_curves.tex`, `cubic_jordan22_unipotent_vertex.tex` |
| CYの交換子別被覆 | `cubic_as4_reductions.tex`, `cubic_CY_one_segre_double_split.tex` |
| alpha型の境界判定 | `cubic_CY_three_alpha_*` の各節 |
| 四成分・相対族 | `cubic_presentation_components.tex`, `cubic_formal_intrinsic_reconstruction.tex` |
| 検算・外部入力 | `cubic_classification_validation.json`, `as4_imports.json` |

## 1. 内在的対象、認識、同値

主原稿 `sec:14641-classification`、`cubic_nakayama_incidence.tex`、`cubic_hypersurface_frame.tex`、`cubic_filtered_elliptic_recognition.tex`。強いH3とAS4包絡を仮定しないweakクラスを区別する。

### 対象・認識・同値

共通のintrinsic weakly marked nc del Pezzo（Gabriel–Krull rank-one torsion-free exceptional O、Serre逆作用tau、AZ ample、三次のHilbert関数）を保ち、反標準環Rが一次生成、二次包絡B=Q(R)が左右noetherian quadratic Koszul AS4型14641であるH3を扱う。外部ambient、埋込み、周期表示を標識に追加しない。

Levasseurの整域定理とHilbert値からR=B/(G)、正則正規G∈B3、六二次＋一三次関係が従う。H3の幾何学的pointed exact同値は反標準環のgraded同型を誘導し、その自己同型群はAut_gr(R)/次数スカラー。相対族の仮定・全矢・降下は第12節の参照先で扱う。OU/AOUのmarkingやZhang同値、導来同値で置き換えない。

### 全ambientに対する構造制限

papers/sections/cubic_nakayama_incidence.tex。

- 構造対象の飽和とEnd(O(n))=kから、商圏で自明なgraded twistは次数スカラーに限る。
- 正規化をGv=σ_G(v)Gとすると、H3では **μ_R=1、σ_G=μ_B^{-1}、μ_B(G)=G** となる。まずSerre比較からμ_R=ξ_cを得て、RRZtri Theorem 4.1(2)へAS index 1で適用しc=1とする。
- RRZtriの追加仮定Dε(R)≠0は省略しない。Bの有限自由k解消PからR⊗_B Pを作ると、perfectでcohomologyはkとk(-3)だけとなり、非零ε複体が得られる。これにより全H3で仮定を満たす。一次資料はRRZ arXiv:1302.0437v2 Lemma 1.5、RRZtri arXiv:1408.0536v3 Theorem 4.1(2)、Zhou–Shen–Lu Proposition 2.3、YZ Theorem 4.2。
- 固定Bに対して **W1={G:Gv=μ_B^{-1}(v)G}という単一の140×20線型核** に絞られる。非零G∈W1は自動的に正則正規でμ_R=1となるが、滑らかさ・rankの十分性は別問題。一般のWc={G:Gv=c μ_B^{-1}(v)G}はc≠1で零。
- Bがgraded CYならσ_G=1なのでGは中心。一般のXi=hdet予想を入力には使わない。
- ただし全H3のBがCYであるとは限らない。非CY符号型の全H3族を下記で構成・分類した。

### 四shift windowと独立Nakayama監査

全正規三次商でBのKoszul分解をRへtensorするとTorはk,k(−3)のみなので、tailsでO(−4)→O(−3)^4→O(−2)^6→O(−1)^4→Oの完全列となる。四連続shiftで全shiftを生成。正規楕円境界認識済H3ではE=O⊕O1⊕O2⊕O3がDbのclassical generator、EnddgのH0dim55,H2dim21。76次元最小A∞台を得るが高次積を打ち切っていない。Toën math/0609762v3の有限An定理は両側smooth properを仮定し、Lemma3.14はquasicompactnessなので、これだけで中央無限位数bad D有限性を主張しない。

h=b=c=1のClifford swap包絡でKoszul双対を独立計算しE0..4=(1,4,6,4,1)、左右Frobenius積非退化、mu_E=swapxy(t,z固定)、mu_B=−swapxy(t,z負)、普通detmu_B−1・top作用1を確認。全次数AS4は別のcocycle証明による。

### 正規三次切断の四line frame

`cubic_hypersurface_frame.tex`：noetherian quadratic Koszul AS4型14641の正則正規三次切断、整域、mu_R=idを仮定。四line compact generatorのproper dg cohomologyはH0=55,H2=21。Gb=nu(b)Gの規約ではTor1=R_nu(-3)、hypersurface作用eta_F:F→F_nu(-3)[2]。Gabriel–Krull rank-one torsion-freeを別仮定すると、全coherent Fのeta_F²消滅とH3性が同値。全heart対象は四lineから8段で生成。この四line補題単独では有限検査・相対開性・rank条件を与えない。これらの適用範囲は `cubic_presentation_components.tex` と `cubic_formal_intrinsic_reconstruction.tex` に従う。

## 2. Skew包絡と標準境界の具体例

`cubic_skew_admissible_classification.tex` の `thm:all-skew-H3-geometric`、`cubic_normal_elliptic_boundary.tex` および `cubic_normal_order3_coverage.tex`。五型は固定skew部分の分類であり、全成分表ではない。

### Skew包絡部分の幾何学的分類：31パラメータ・五型

papers/sections/cubic_skew_normal_incidence.tex は全正規三次直線の被約locusを交換指標blockの射影空間として記述する。一般qで正規直線は単項式20点だが、これを20個のH3曲面と数えない。

H3に限ると全skew torusでc=1となり、W1={χ_i(a)=μ_B(x_i)/x_iの逆数}に制限される。任意のcocycle untwistと線型簡約な対角群の同変Extを使い、各座標点のjetにx_i²x_jが必要と証明。256通りのjet選択を19共役型にまとめ、整数Smith証明書を標準ライブラリで全等式・unimodularityまで再検証する。これにより全qは2乗根か3乗根。49個のjet候補から共通因子を持つ12個を除き37個、さらに次のrank障害で6個を除き31個となる。

| ambient型 | 座標パラメータ数 | 一般同型類の次元 | 全admissible係数・慣性 |
|---|---:|---:|---|
| 可換 | 1 | 4 | 滑らかな三次式のPGL4商 |
| CY符号型 | 4 | 1 | G=At³+t(Bx²+Cy²+Dz²)+Exyz、ABCDE(AE²−4BCD)≠0。粗い同型類w=AE²/BCD∈Gm\{4}、自己同型S4 |
| 非CY符号型 | 6 | 2 | G=binary cubic+ℓ2 x2²+ℓ3 x3²。ℓ2,ℓ3をx0,x1にした後adΔ≠0。全開部分P7のPAut(B)商、一般慣性μ2² |
| 3乗根・中心一次型 | 8 | 1 | G=At³+Bx³+Cy³+Dz³+Exyz、ABCD(E³+27BCD)≠0。粗い同型類w=E³/BCD∈A1\{−27}、w≠0で位数27、w=0で位数81 |
| 3乗根・二重指標型 | 12 | 0 | G=At³+binary cubic+Cz³、ACΔ≠0。全admissible開部分は既存のBH54 |

各族のsmoothnessは有限同変cocycle比較で可換三次の滑らかさと比較し、**rank条件は別途** quaternionまたは3次巡回代数の非Normで整域性を証明した。S4座標置換だけでなく、全線型ambient自己同型とintrinsic pointed exact同値の幾何学的群oidまで扱う。上表は全H3の成分表でも、相対stackの分類でもない。

### 除外する3乗根の六点

既存27点の(0,1,2)軌道6点は滑らかなtailsを持つ対角Fermat商を与えるが、generic代数はM3(K)となる。chartでs=−t(t+1)/(t+r³)=Norm(−u(u+1)/(u+r))、u³=tという明示的Normがあり、構造対象のgeneric像は単純加群三個の直和となる。Gabriel–Krull rank-one条件に反する。27点をそのまま27個のH3型と読むのは誤り。

### 非CY分枝

q01=1、他の五係数−1、G=x0³+x1³+x0 x2²+x1 x3²。μ_B=σ_G=diag(1,1,−1,−1)、μ_R=1。滑らかさ、整域性、Serre作用、例外性、GK rank、AZを全て証明した。固定Bの全H3係数はP7の明示開部分で、Aut(B)=GL2×(Gm²⋊S2)。一般の有理商はk(u+v,uv)、u=ac/b²,v=bd/c²。これはPymのCY族のみで全H3を覆う方針への具体的反例。

### 正規一次楕円境界の現行分類

mu_R=idの正規三次商でR/(t)が滑らかな次数3楕円THCRの場合、共役theta（ta=theta(a)t）は有限位数1,2,3,4,6。lambda1のunipotentはSklyanin二次minor（可換例外は三次方向微分）で消える。s=t^mの中央分母払いによりH3 iff gldim U有限（U=R[t^-1]_0）を証明。中央化Zhang twist R^(theta^-1)は同じUとgrU≅Hの通常の濾過を与えるが、mu_Rtwist=thetaでintrinsic反標準gradingは変わる。

位数4,6および位数3D0はskew elliptic coneとなり除外。位数3はB=S[t;lambda],G=g+D t³、B CY、g中心、mu_S=scalar(lambda)となり、全admissibilityはD!=0。S[g^-1]の中央cube-root有限etale/separable拡大が(S/(g−1))[z±]となるため有限glを得る。さらに巡回固有tensorの8次元空間をsl3の随伴模型へ同定し、全trace零Jordan行列のpoint determinantを計算した。滑らかな楕円境界を許すのは重複固有値の対角型、すなわち量子P2包絡のみ。中心三次はbinary cubic+z³で、滑らかさから全てFermatへ直せる。従って位数3非中央部分は既知の量子Fermat一対象、幾何学的群oidはBH54に一致する。

位数2の全包絡被覆も証明した。S=QHのmu_S(g)=−gとhdet mu_S=1から誘導楕円自己同型fは反転型involution。mu_S²=scalar(c),c³1を適切なscalarで補正したalphaでSをtwistすると、境界は二つの可換involutionの積、従ってtranslation order1or2。既証のtranslation包絡CY性がc1を強制し、Sは可換P2のinvolution twistまたはCliffordのswap twistに限る。前者の全非skew定数持上げはPBW overlapとWeyl中心化環k[w²]の奇偶で除外され、既存符号skew分類へ入る。

Clifford swap枝はBの関係yz+zx=hxy+b t²,zy+xz=hyx+b t²,x²+y²=hz²+c t²,tは全activeと反交換。W1は一本、6G*=x²z−xzy+yzx−y²z+zy²−zx²。有限Gamma cocycle (-1)^(a e'+r a')で中央Clifford beta=(b,b,c)に戻すとG*は純volume。H3 iff長さ8 CI（2yz−hx²−b,2zx−hy²−b,2xy−hz²−c）が被約。h=b=c=1は実際の非skew・非CY H3例で、degree4三正規式、CI長さ8・Jacobian unit、全512 cocycle恒等式を厳密検算済み。証明はcubic_normal_order2_clifford.tex、quantum排除はcubic_normal_order2_quantum.tex。

Clifford swapでは正規滑らか楕円境界ktが一意。mu_B負固有空間の候補au+bz+ctに反交換子rank1を課すと、minor−4h²でa=b0（非被約底でも同じ）。全intrinsic矢はt→a t′,X→M X′、M alpha=alpha M、r_h^0(MX′)=N r_h′^0(X′)、N beta′=a² betaという有限係数方程式を共通次数scalarで割ったもの。任意底変更の全graded同型functorを与え、一般次元2、一般慣性mu2×mu2。

許容条件は明示quartic Delta_h(b,c)=(h c−2b)((h³−2)b−3h c)(c²+h²bc+2h b²)の非消滅と同値。固定hで四つのbad方向は相異なる。P1_betaから四点を除く係数方向で、任意底変更・fpqc fiber条件に適合する。二character枝x=yと2z+h(x+y)=0の分解・全係数恒等式を検証済み。証明はcubic_normal_order2_arrows.tex。

非中央正規一次楕円境界部分では位数2の被覆・全許容条件・全幾何学的矢と位数3のBH54を得た。全H3にこの境界があるとは主張しない。

## 3. 中山スペクトルと単冪部分の排除

個々の還元段階に現れる必要候補の全域排除は、この節の冒頭三定理に集約する。unit-repeatの片方零結合は `cubic_third_root_unit_onezero_completion.tex`、正常一次のproper楕円・軸・w0の境界は `cubic_third_root_unit_boundary_elliptic_exclusion.tex`、`cubic_third_root_unit_boundary_axes.tex`、`cubic_third_root_unit_boundary_w0.tex`。

三固有値の結論は `cubic_third_root_nonunit_zero_column.tex` の `thm:cubic-three-eigenvalue-sector-empty`、四単純は `cubic_four_simple_final_curves.tex` の `thm:cubic-four-simple-sector-empty`、単一固有値は `cubic_jordan22_unipotent_vertex.tex` の `thm:cubic-jordan22-unipotent-empty`。以下の有限必要候補は分類の結論に至る補助模型である。

### スペクトル・全単冪領域の結論

強いintrinsic H3のAS4包絡は相異なる中山固有値をちょうど三つ持たない。全Jordan型の必要還元、重複1の全22tensor atlas、非単位重複rootの独立・非零比例・零b²列を全て排除した。全単一固有値非CYも排除済み。

### 単一固有値領域のCY性

単一固有値のH3包絡は必ずCY（μB=id）。最後の非自明単冪Jordan(2,2)も全排除した。通常証明cubic_jordan22_unipotent_vertex節thm:cubic-jordan22-unipotent-empty。元26反巡回N核、U=(x0,x2),V=(x1,x3)、V個数weightで最高2。純U²/V² sourceQは対称4×4、binary domain boundからrank≤1。Q0はrankH6とblockrank2rから純U²関係が3次元以上になり矛盾。従ってQ=qq^t≠0、q二次係数2×2可逆。Nを保つ同時GL2変換でq量子(0,1,−p,0),p非零又はJordan(1,1,−1,0)。mixed最高block5minor−p²(p−1)²(p+1)²、rankH6がmixed≤4を要求しp±1だけ残る。
可換・反可換・Jordan三chart全て元source principal6minor−1、最高逆順pairminor±1、U/V両AS2とVU→UVによりx0^i x2^j x1^k x3^lが張る。実AS4 Hilbertとの比較で全次数grC同定。最高三次商20dimの全N核は6dim/weight≤1、ゆえF Nfixedはweight≤1⇒J=(x0,x1,x2)のJ²。P=πk[x3]自己Ext1dim3、全低weight係数のままtwist後monodromy三型のdet1を検証。反可換ではdiag(−1,−1,1)で単冪でないが、odd-Serre determinant補題はdet1だけで排除する。全特殊値もunitpointpivotで保持。
公開verify_cubic_jordan22_unipotent_vertex.py/certificate 、全26核/最高rank1/三chart/最高PBW/N三次行列と全6核/全point漸化式を保持。通常の被覆/PBW/tails/Serre証明を機械形式化したとはしない、新規性未確認。新as4外部定理輸入なし。

### 三・四固有値領域の排除

全H3包絡の中山作用は相異なる固有値を高々二つしか持たない。四単純全体も排除した。単一固有値の単冪部分は `cubic_jordan22_unipotent_vertex.tex` により自明である。
通常証明はcubic_four_simple_final_curves節、thm:cubic-four-simple-sector-empty。五曲線branch0,3,7,10,13を各F=QQζL(t)で一変数化。元Hの六列source minorΔ、全次数商のpivot分子/分母、正常行列の全pivotと係数分母/parameter定義域を記録し、非零積P上で全底変更を保証。generic正常shape26×4,23×4,22×4,17×2,14×2は全列rank。Pの全数体既約因子を積へ掛け戻し、各既約性を確認し、E=F[t]/fで元H/商/正常行列をfresh計算した。全因子数11,5,13,8,9、定義域内因子数8,2,12,5,6、F上次数和20,3,23,11,9。全有効例外もHrank6、B3/4=20/35、正常核0。有限標本・数値根は使わない。
公開verify_cubic_four_simple_final_curves.py/certificateに全pivot多項式と全例外の数体係数・source/商/正常rankを保存。検証器は因数積の一致と使用する数体多項式の既約性を含めて照合する。以前の全被覆の独立再監査、新規性確認、全homological証明の機械形式化とは呼ばない。
as4-reference固定SHA6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0のCY_COMPLETE/UNIPOTENT_UNTWIST本文とCOVERAGEを対象を絞って読んだが、全CY統合定理を新規監査済み入力として輸入していない。前者の有限許容atlasだけでは本研究の全幾何学的分類・成分・降下の完成にならない。

### 全H3の二固有値中山：位数2/3への縮小

既存の単一固有値フィルタを二固有値へ拡張した。H3包絡BのKoszul top wは任意の非自明なV=A⊕Cに対して純A四次と純C四次だけへ分離しない。Frobenius E2対合によりflattening像はR全体であり、もし分離すればR=R_A⊕R_C、Bは自由積となる。整域性からk[a]*k[c]が入り指数成長となってHilbert14641に反する。

二一般化固有空間の固有値alpha,betaに対し、mu_B(G)=Gからalpha^a beta^(3−a)=1、hdet(mu_B)=1と混合topからalpha^c beta^(4−c)=1、a0..3,c1..3。4a−3cの絶対値は1,2,3,5,6,9、1は二値が一致するので除外。粗い固有値集合はmu90内の非順序16組（位数2:1組、3:3組、5:4組、6:2組、9:6組）に限る。

位数5/6/9の12組ではalpha/betaの位数も5/6/9であり、topのA個数cとGのA個数aが各々一意となる。Rが二重斉次となり、Koszul Euler分母P(s,t)は全次数4以下・最高項s^c t^(4−c)。任意の正の再次数付けのHilbert極が4位なので、Pの(1,1)Taylor次数4未満は零、よってP=(1−s)^c(1−t)^(4−c)。一次係数からdimA=c,dimC=4−cを得る。

位数5は(a,c)=(1,3)/(2,1)、一次元側が正規一次元となりG=ell z²又はz²ellで分解。位数9は(0,3)/(3,1)で一次元側の純三乗。位数6はc2,a0/3で二生成元一二次関係の部分整域内の三次となり、全斉次二変数式の一次因子分解で排除。この二変数補題は可逆二次係数行列の等方方向からyx=qxy+kappa y²へ移し、yを逆にしたz=xy^-1でyz=(qz+kappa)yと書いて通常の一変数多項式の根へ還元する。Jordan q1も含む。

従って全H3の二固有値中山の半単純部分は位数2/3のみ、固有値集合は{1,−1}又はmu3の相異なる二元（三組）の計四組。この重み計算は二固有値の必要集合を決める補題であり、各重複度の分類は符号型および三乗根排除の証明を用いる。証明はcubic_as4_reductions.texのthm:h3-two-eigenvalue-refined。verify_cubic_two_eigenvalue_filter.pyは有限整数演算16組と12排除の重み型、二変数因数分解式の三次までの普遍多項式恒等式を実行確認する。成長/Frobenius/二重Hilbertの議論は原稿の証明であり、有限列挙だけで証明したとしない。新規の全as4被覆は不要。

### 全二固有値・位数3領域の排除

位数3の最後のType E候補にも明示的な普遍Ore norm因子が存在する。d=a5−a4−a²−2a,e=a5−a4+2a²+a,h=a5−a4+a³−a+1,k=a5+a、Q(U)=U²−(hd+k)U+h、X(U)=1−(d+e)U、W(U)=(a4+a)X+(a5−a³−a−1)U²と置く。QQ[a]/Phi9上でgcd(Q,X)=gcd(Q,W)=1。Q(u)=0,b³=X(u),c=u/bとするとell=x+by+czのnorm sigma²(ell)sigma(ell)ell=[bW(u)/X(u)]F0。この非零係数をlambdaと書き、s³lambda=−1,L=s ellとすればF0+t³=(t²+sigma²(L)t+sigma²(L)sigma(L))(t−L)。次数2/1の二因子は商で非零なのでnondomain。

元のS二次関係の全三次商で、c=U/bを代入しb³を掛け、b³=X(U),Q(U)=0により全10座標の残差零をSymPy厳密再生した。gcdも同じ数体のEuclid計算で確認。Singularが発見した二変数norm理想は最終証明の依存ではなく、公開検証器は補助二次方程式と全座標恒等式のみから再生する。AS3存在/PI/有限中心性/局所order/同型十分性を入力にしない。原稿thm:h3-order3-two-eigenvalues-excluded、verify_cubic_order3_Ore_distinct.py、同証明書のOre_norm_exclusion節。

これで全H3二固有値中山は{1,−1}だけに限る。二固有値位数3の幾何学的領域は空なので、候補に対して求めたmu9やaffine表示から実在成分を主張しない。

### 二固有値・位数3の構造帰着

比の位数3では二次tensorの三つの一般化固有値が相異なり、Rは純A²/混合AC/純C²へ分解する。BはN²gradedとなり、Koszul topも一次元なので二重斉次。二重Hilbert補題により、固有値集合{1,rho}は重複度1+3、{omega,omega²}は2+2となる。Gの固定重みは純三次の二成分だけ。

{1,rho}では固有値1の直線kzが正常化しmu_B(z)=z。混合三関係の両射影の核はaz又はzaという零因子になるため無く、B=S[z;sigma]、Sは三生成元noethquadraticKoszulAS3となる。AS3性は純S成分のKoszul解消と正常一次商のRees lemma。G=F+c z³、F!=0、sigma F=F、Fのnormalizerはmu_B^-1|S。c!=0ならsigma³=mu_B^-1|S。c0は後述の正規cone頂点障害で排除した。

{omega,omega²}ではG=F_A+F_C、両成分非零（片方だけなら二変数三次が分解）。二生成元一二次関係のdomainで、正常三次のnormalizerが唯一の固有値rho（原始三乗根）なら、その平面はq=rho^-1の量子平面、F=x²y、normalizer=rho Iに限る。可換型はnormalizerIdで不可能、Jordan型はF=p(z)y³とp(z)=rho p(z+1)の最高係数で不可能。量子型の単一固有値graded automorphismはスカラーであり、指標q^u=q^(u−3)=rhoからq³1,u1/2を得る。従ってこのH3候補ではmu_B自体がsemisimpleとなり、xy=omega yx,zt=omega²tz,G=x²y+z²tに規格化できる。

Frobenius対合により四次topのAA/CCブロック係数は非零。巡回式が混合flatteningのオフ対角を二つの可逆binary relation行列のKronecker積へ移すので、その4×4ブロックは可逆。混合rank4からR11のAC/CA両射影が同型、従って全体は標準単項式x^i y^j z^k t^lのPBW基底を持つ。混合四関係は可逆4×4twisting matrixで表せる。この必要表示からのH3排除は、二固有値・位数3の構造還元の参照先に従う。

原稿thm:h3-order3-two-blocks、検証verify_cubic_order3_two_eigenvalue_reduction.py。有限重み、Jordan最高係数、量子binary指標、混合ブロック行列式を実行確認。成長・Frobenius・AS3性・PBW比較は原稿の証明であり列挙だけで完成としない。

### 二非自明三乗根固有値の全排除

全H3で中山固有値集合{omega,omega²}は不可能と証明した。2+2帰着から、xy=omega yx,zt=omega²tz,G=x²y+z²t、mu_Bはsemisimple、混合四関係はPBWgraph。最高tensorのAA/CC係数をr_A tensor r_Cへ規格化し、残る交互成分をAC=(xz,xt,yz,yt)順の対称4×4行列H（十係数h0..h9）で全表示した。

rank6のSchur16式、四Diamond（zyx,tyx,tzx,tzy）の24式、正規Gの32式から零・重複を除く68必要式Iを再生成。Singular4.4.1で発見した30式Gammaについて68×30の乗数Xを保存し、SymPyでI X=Gammaを元の係数から独立再生した（証明書約49KB、Singularなしでも再生可）。Gammaから(h5−omega²)(3h5−omega−2)=0を得る。

第一枝はh3=−omega²,h5=omega²以外零。skew係数(omega,omega,omega²,omega²,1,omega²)となり、既証skew H3必要リストの三乗根行が全てCYであることに反して排除。第二枝はp=h1,q=h2非零、h0=2(omega+2)pq,h3=−(2omega+1)/3,h4=(omega−1)p/(3q),h5=(omega+2)/3,h6=−omega/(3q),h7=(omega−1)q/(3p),h8=−omega/(3p),h9=(2omega+1)/(9pq)。元I/Gammaへの全逆代入を検証。u³=q/pを取りdiag(u,up,1,q)でG直線を保ってp=q1へ移るので、全域は一つの候補軌道。

標準候補ではtau³=omegaとして、tau G=(x+tau z)[tau xy+zt+tau²{omega²xz−(2omega+1)(xt+yz)/3−yt/3}]という非可換積恒等式をPBW全係数で独立検証。次数1/2の非零因子から商はnondomain、従って全枝でH3を排除する。候補自体のAS4十分性・noetherian存在は不要。

原稿thm:h3-order3-two-nontrivial-excluded、再現verify_cubic_order3_two_block_incidence.pyとcubic_order3_two_block_incidence_certificate.json。位数3は正常一次元AS3 Ore表示の重複度1+3だけが残る。純base切断c0は正規cone障害で排除する。三次元AS3と正常三次の必要被覆は二固有値・位数3の排除証明を参照する。

### 正規cone頂点障害と位数3 Ore切断

既存のskew cone頂点補題を中心三次から正規三次へ拡張した。B=S[z;sigma]、G∈S3正規正則、Gz=zG、normalizer thetaがSを保ちzを固定する場合、M=k[z]はtheta-twistに不変。正規Rees lemmaのtwistはMを変えず、Ext_B(M,B)の次数3集中からExt_R(M,R)の次数2集中を得る。AS Gorenstein局所双対とsection比較、C=S/Gのkの最小自由解消のRへの誘導によりExt^n_qgr(P,P)=beta_n^C(k)。1/H_C=(1−u)^2/(1+u+u²)は多項式でないため全beta_n非零、H3のcohomological dimension2に反する。中心版の既存応用はtheta=idの特殊例として保持する。

従って{1,rho}の1+3 Ore型でG=F+c z³のc0は不可能。座標を規格化してG=F+z³、sigma F=F、Fのnormalizer=sigma³=mu_B^-1|S。さらに正規一次元zの商にRRZ1302.0437v2 Lemma1.5を適用してmu_S=mu_B|S sigma=sigma^-2を得る。一次資料のmu_B-normal仮定はmu_B(z)=zで満たす。これは必要帰着であり、Sの存在十分性や商のH3判定を結論しない。独立な大規模CAS計算は不要なホモロジー証明であり、新たな計算検証を検証器で照合するとしない。

### 位数3 Ore型の三固有値base模型

B=S[t;sigma], G=F+t³の帰着において、sigmaの単一固有値bは不可能。mu_S=sigma^-2のAS3最高tensorへの固有値b^-6=rho²!=1がhdet(mu_S)=1に反する（Jordanも含む）。三固有値ならsigmaはsemisimple、a³=rhoの原始九乗根aを使いsigma=diag(a8,a2,a5)、mu_S=diag(a2,a5,a8)。sigma固定最高tensorは三つのii(i+1)巡回orbitだけ。中山巡回係数を合わせた三係数A_iの一つが零なら前のAが非零である限り二次関係に純平方が出てnondomainとなるので、全A_i非零。指数行列det9の対角尺度変更で全て1へ規格化する。

得られるSの関係はxy+a²yx+a7z²、a4x²+yz+a5zy、ay²+zx+a8xz。全二/三/四次語の厳密商次元は6/10/15。sigma固定三次空間はy²z,yzy,zy²,z²xの四次元で、正常化a6Iの四次係数写像はrank3。従って唯一のF直線はF0=(-a4+a−2)y²z+(-a5+2a4−2a³+a−1)yzy+(a³−a+2)zy²+z²x。元の二次関係からSymPy QQ[a]/Phi9の厳密行消去、最高tensorの両slice一致、正常式全係数零、核rankをverify_cubic_order3_Ore_distinct.pyで再生した。小さいJSONに入力と出力を保持する。

これにより各rhoにつき三固有値sigmaのH3候補はS[t;sigma]/(F0+t³)一対象以下。三次/四次Hilbert一致だけから十分性を言わない。原稿prop:h3-order3-Ore-distinct。sigma二固有値も次の議論で排除した。全体のmu_B三固有値以上とは別のbase自己同型sigmaの固有値分類であり、両者を混同しない。

同命題でsigma二固有値も全排除した。比が原始三乗根なのでSは二重graded、hdet_S sigma=1からtopの型は2+1、正の再次数付けの三位Hilbert極から重複度も2+1。S=T[u;nu]、TはAS2整域。二次元側sigma_Uの固有値b、u上cについてb²c=1、b³=c³=rho^-1。固定三次はF=f2u。sigma_U(f2)=c^-1 f2とnu(f2)=rho f2、正規商公式mu_T=sigma_U^-2 nuからmu_T(f2)=c^-1 f2!=f2を得る。可換/Jordan平面はmu_Tが二次空間でunipotentなので不可能。量子平面なら単一固有値のsigma_Uはscalar、nuも対角で全Bがskewになるが、tx=bxtのbは原始九乗根となり既証skew37必要条件に反する。Jordan型を除外せずに含めた議論である。

hdet_S sigma=1は追加仮定ではない。BのKoszul双対の(3,0)と(0,1)のFrobenius積、mu_B(t)=t、hdet_B mu_B=1からhdet_S(mu_B|S)=1。sigma³=mu_B^-1|Sよりh³1、mu_S=sigma^-2とhdet mu_S=1よりh²1、従ってh1。この証明を構造帰着にも明記した。よって全二固有値・位数3 H3は有限の明示候補（各rho一つ以下）に縮小できた。単一固有値mu_B=1の単冪層、二固有値位数2、三/四固有値mu_Bを覆ったとはしない。

### 有限位数3候補の条件付き慣性とaffine表示

候補がH3なら、mu_Bの固有空間から全graded自己同型はSとktを保ち、sigmaと可換するのでS上対角。関係から対角はd(1,r,r²), r³1、t上e。F0はd³r倍、t³はe³倍なのでG直線安定条件e³=d³r。grading scalarで割るとr=e³,e9=1、内在的慣性mu9（x,y,z,tに重み0,3,6,1）。二つのrhoは中山固有値集合が違い同値でない。従って二固有値・位数3の幾何学的群oidは二つのBmu9のうち許容されるものの非交和。これらは次の普遍Ore normで全排除されるため実在H3の慣性ではなく、表示候補の射影安定化群の計算として保持する。対角指標行列のSmith(1,1,9)と全関係/Gの重みを既存検証器で厳密確認した。

正規t開集合はD=S^(sigma^-1)、右twist積f*g=f sigma^-deg(f)(g)を使い、R[t^-1]0=D/(C+1)。Dの三関係はuv+a8vu+aw²、a7u²+vw+a²wv、a4v²+wu+a5uw、すなわちSのa->a4版。F0=c1y²z+c2yzy+c3zy²+z²xならC=a³c1v²w+c2vwv+a6c3wv²+a³w²u。F0のnormalizer=sigma³とsigma F0=F0からCは中心であり、三交換子をDの元関係の四次商で全係数零と検証した。ただしmu_D=sigma!=Idであり、CY用認識定理をこの表示へ適用しない。これも後の全排除候補の代数的な開集合表示であり、このaffineのglをH3分類の残課題とはしない。

古典型との同定：Le Bruyn–Smith–Van den Bergh, Central extensions of three dimensional Artin–Schelter regular algebras, Math.Z.222(1996), p.186のType E三関係をPDF画像で確認し、zeta9=a²、(X1,X2,X3)=(x,z,a³y)で三関係が(a r1,a r3,a7 r2)に一致することを元の係数から厳密検証した。AS3表示自体は古典的であり新規性を主張しない。全H3からの帰着と正常三次/候補許容性は別の課題。Type Eの中心・PI次数・局所orderの定理をこの式一致だけから輸入しない。恒久出典URL https://sites.math.washington.edu/~smith/Research/Central-extns.pdf 。

### スペクトル被覆と関係character

`cubic_spectral_resonance.tex`,`cubic_spectral_ore_reduction.tex`：mu(G)=Gから三次共鳴が必要、単純固有直線の唯一の純三乗共鳴は非整域で排除。四単純固有値の十個の二次積が相異なる領域はskew、(2,1,1)の二次非共鳴領域も二元AS2 Oreと全基底型の因子/正常核比較からskew。既分類skew H3は三固有値以上を持たないので、三固有値は六二次共鳴、四単純は21共鳴（反対固有値6、平方対二異値積12、互いに素なpair積3）上に限る。
三固有値はA=(a,-a,c),B=(a,b,-b),C=(a,at,a/t),D=(a,at,at²)の四chart。各七三次共鳴。AS4最高wの中山巡回を四回反復してmu^tensor4(w)=w、Frobenius次数1/3から各固有方向を含む四次重みが存在。三次/四次の文字格子detにより、共通N乗根(N≤24)又は二相反pencilに縮小。
二次関係の重みchiとchi^-1の次元は等しい。重み−1は中山巡回二回とdetから偶数（単冪込み）。重みspace次元Dchi、固有重複miならrank-one Segre回避でrchi≤Dchi−max(mi+mj−1)。KoszulcharacterはB2=V²-I、B3=V³-2VI+V*、R3=B3-1。R整域の線型乗法単射性を全重みで課す。

### 相反pencilとGK2傾き障害

`cubic_inverse_spectral_pencils.tex`：(z,z,1,z^-1)は位数1〜4外で関係数≤5となりAS4外。(1,1,z,z^-1)の必要atlasはbU=f(U)b,cU=g(U)cと二本のU²/bc/cb関係。偶射影rank1はAS2 inverse-Nakayama一次intertwinerとmodF正常式で全因子。rank2はbc=h(U),cb=k(U)、S=<U>が二元二本のcubic関係でHS=1/((1-t)²(1-t²))。bのOre局所化S[b±1;f]からS noetherian/gldim≤4。G∈S3、S/(G)↪B/(G)だが商のGK2傾き3/2はArtin–Staffordの一次生成GK2整域の整数傾きに反する。SのAS3性は仮定しない。root4 unit pencilも偶数性で同じ関係/charge0分布を確認して排除。
文献入力はStafford本人を含むStafford–Van den Bergh arXiv:math/9910082v2 Theorem5.2 p14（Artin–Stafford Theorem0.2の明示的再掲）。本文・代数閉体・次数1生成・GK2・有限余次元THCRの結論を実読。原論文DOI10.1007/BF01231444のabstract/書誌も照合したが、原論文全文証明の独立再監査とは称さない。PDF digestと適用範囲はvalidation JSON。曲線Riemann–RochでHilbert傾きが整数になる。これで全三固有値スペクトルはまず共通N≤24の有限集合へ。

### 有限スペクトルの全列挙と排除

`cubic_three_eigenvalue_finite_spectra.tex`：N≤24全最小共通位数・相異指数35424組を整数剰余で全列挙。共鳴/整域関係容量を通る99関係パターンに次数3までのcharacter/乗法単射を課し、57除外witness（56単射違反、1負次元）を保存。必要38スペクトルからN9/12の8組を純二元AS2三次の因子で排除。残余に以下を適用した。
- 位数5四候補：`cubic_fifth_root_spectrum_exclusion.tex`。AS2 Ore表示と全自己同型型を比較、最終強制p=eta³,q=eta^-1で元の三関係NF(c x²b-b c x²)=-2eta x c³≠0。全Jordan込みで排除。
- 位数6：`cubic_sixth_root_spectrum_reductions.tex`。四scalar-normalizer Ore cone、二曲率（q³1と原始三乗根の矛盾）、一補助Z-grading正常核、二つのAS2平面作用矛盾で九候補を排除。cone補題はGv=lambda*vGへ一般化しM=k[v]のtwist同型v^n↦lambda^-n v^nを明示、既存Betti/無限Ext証明を維持。旧adjacent-L verifierも検証器で照合する。
- 位数4：`cubic_fourth_root_spectrum_reductions.tex`。四奇数重み−1パターンを除き、(1,1,i,-i)を既述charge0障害で排除。
- 最後の位数6：`cubic_sixth_root_last_Ore_exclusion.tex`。正常bでB=A[b;sigma]、coneでb³係数非零が必要。正常式からsigma³=muB^-1|A、muA=sigma^-2、hdet sigma1。sigmaUの同一固有値は最高AS3cubicのslice退化、相異なる場合は(a,a*omega),a³omega²、sigma c=-a*omega^k。最高tensorの固定orbitを直接列挙しk0だけ残る。Aはx²=kappa*c²,yx=-a²xy,yc=-a²cy、sigma=(a,a*omega,-a)。sigma固定A3はkx²y一本だが正常x残差(-a²-omega²)x³yが非零、従って全Gはkb³で非整域。先行AS3完全分類を輸入していない。QQ(a),Phi9で全tensor slice、固定A3 rank9、元の正常残差を厳密に照合する。単冪sigma候補もslice退化で排除。

### 補助必要候補：半単純・位数3の3スペクトル

三固有値H3の中山は半単純であり、位数3のみ。必要リストはN3:3個で、各関係重みパターンは一つ。Galoisラベル2軌道の代表(N;a,b,c)、重複2を先頭、単純二固有値を昇順に書く：
(3;0,1,2),(3;1,0,2)。
Galoisラベルはk線型同値の商ではない。三つのスペクトルは必要候補であり、AS4存在の十分条件ではない。全候補のH3排除は `thm:cubic-three-eigenvalue-sector-empty` に集約される。全リストと現在値は `computations/cubic_fourth_root_last_negative_simple_certificate.json`。再生は `python computations/verify_cubic_spectral_reductions.py`、34検証器のは有限計算であり通常の全証明の独立機械検証ではない。
N4(2,1,3)は `cubic_fourth_root_negative_repeat_exclusion.tex` で全排除。G=F b²+L c²、domainにF,L独立が必要。even rank2はS2自由なのでF f²(u)=mu^-1(u)Fが不可能。rank1はAS2 Oreへ復元し、可換はf=gとh0でskewへ、JordanはF,Lが同一正常線で因子、量子反対角はscalar linear normalizerなし、量子対角はF=x,L=y、alpha=i,alpha*gamma=-pとgamma²=-pからp1を強制。単冪中山込み。公開検証器が元Jordan relationのminorとkernel、量子のp(1-p)矛盾、free-tensor augmented rankを厳密に照合する。

### N4(1,0,2)と(3,0,2)のeven rank1は `cubic_fourth_root_unit_simple_rank1.tex` で排除済み

G=C b³+F2 c+D bc²、bc-qcb=h。正常b式の純T4成分は-q^-1F2*hだけ。h非零ならF2=0でG左b因子、h0ならAS2自己同型Oreの既存全型認識へ。元AS4 Ore family QQ(i)(alpha,beta)で四重なりとF2三基底の純T4残差を厳密に照合する。

### この二スペクトルのrank2も `cubic_fourth_root_unit_simple_rank2.tex` で全排除

bc=h,cb=k、S2自由4次元、HS=1/((1-t)^2(1-t^2))。h,kが双方rank1なら正常式で独立平方に帰着し、最高binary quarticの第一pair対称性と巡回固有値±iが矛盾する。従って少なくとも一方hが非退化な正常二次。S/(h)はAS2、正常Reesと既証noetherian/gldim上界からSはcubic AS3・index4。
B[b^-1]=S[b±1;f]=C[b^-1], C=S[b;f]の次数付きbimodule最高Extを比較する。B index4とC index5の差により同型の単元はscalar*b^-1に限られ、muC|S=f^-1*muB|SとOre公式muC|S=f^-1*muSからmuS=muB|S。無次数のinner同値だけではこの結論にならない。自由S2上でmuS(h)=-h、正常化tau(h)=h。RRZ Lemma1.5（mu-normalは固有vectorの意味であり固有値1を要求しない、一次資料rrz.txt448–464を確認）からmuT=muS*tau、hdetT(muT)=-1となり、AS2の量子/Jordan標準形のhdet1に矛盾する。単冪も含む。公開検証はbinary tensorの対称/巡回連立rank16、AS2元関係の固定と11候補への更新を厳密に照合する。正常Rees/Ore/局所化は通常の数学的証明であり有限計算がこれを形式検証したとは称さない。
rank2の25×4正常係数核は構造還元に使えるが、この枝ではAS4整域自体が排除される。残るN4 atlasの検討へ進んだ。

### 重複1のN4(0,1,2),(0,2,3)も `cubic_fourth_root_unit_repeat_resonance.tex` で全排除

半単純mu=(1,1,i,-1)の最高tensorは16軌道、重みblock rankは(2,1,2,1)。bc/cb関係の両係数非零でmixed列比qを置き、U基底を適合させる。重み-1のPfaffianからa8=q²a5,a10=q4a5,a11=0、必ずxc+q^-2cx関係。純U主block rank≤2はa1=0を強制し、A=e*v^t+v*e^t、e=xy-yx,v=(a0,a3/2,a3/2,a4)。a4非零ならxy=yxとc²∈U²、q4=-1が強制され、c²x=-xc²と可換性が矛盾。a4零なら二次提示を(x,c)で商にしてk<y,b>/(b²)、次数15は1597>AS4値816となる。正常一次商のAS正則性などの未確認一般定理は使わない。
単冪部分は既証の右twist公式mu_(B^H)=muB*H^-4でH=mu_u^(1/4)を取ると消える。関係重みとAS4整域性を保つので同じ矛盾。この枝ではAS4整域自体を排除しており、G正常性のZhang輸送は仮定しない。公開検証器は256語から全巡回軌道、元middle、Pfaffian、minor、商関係supportと語数を両符号で厳密照合。続いて重複-1の枝を調べた。

### 重複-1のN4(2,0,1),(2,0,3)は `cubic_fourth_root_negative_repeat_finite.tex` で全排除

mu=(-1,-1,1,i)の最高tensorは17軌道。rank1 mixedをqで正規化し、重み-1 Pfaffianでa13=0,a6=q4*a8,a7=q²*a8。H0のbb列は純U関係r=a3x²+a8q4xy+a8yx、domainにa8≠0が必要。yy列もrに比例しa12=0,a2=a3*a5/a8,a5(1-q4)=0。a5=0なら(x,b)商がk<y,c>/(c²)で指数増大。よってq4=1,a5≠0、xy/yx列差からa4=a2。yのshearでa3=a2=a4=0、rank2minorでa0=0。
全必要表示はyx+xy=0,b²+A x²+C y²=0,bx=q²xb,by+q²yb+d c²=0,cx=iqxc,cb=-q^-1bc（C,d≠0）。scalar変更でC=d=1,A0/1、q四乗根の八表示。元R3/R4を再消去して全八表示の次元20/35、正常核はq1でk*c²x、他三qで零をexact確認。両i符号の計16検算を公開。非零正常三次も因子なのでH3なし。八表示のAS4十分性は不要であり主張していない。
単冪untwist D=B^H後もHはDの自己同型、mu_sと可換。唯一のUc+cU関係からHx=x、Hy=y+t*x。純U関係xy+yxの保存は2t*x²=0を強制、H=1。従って全単冪候補も既述半単純の場合に含まれる。Gの正常性をtwistで輸送することは使わない。続いて重複i・単純1を調べた。

### 位数4の重複i・単純1の二スペクトルは `cubic_fourth_root_last_finite.tex` で全排除

mu=(i,i,1,-i)の最高tensor16軌道を展開、rank1 mixedを列比qとU基底で正規化。H0の三次minorからa11=a14=0,a10=a8q²,a4=a8/q²,a2=a7(1+iq4)/(2q²)。H2のcc列の純U関係は非退化でa8≠0、yy列比例からa3(1-q4)=0。a3零ならc²=κx²と正常cxの二本の二元関係でdomain外。a3非零ならq4=1、shearとPfaffianでa7=a2=a1=a0=0。
全必要表示はyx=i xy,c²+C y²=0,cx=-i q²xc,yc+q²cy+d b²=0,bx=q^-1xb,cb=-q^-1bc（C,d≠0）。scalar変更でC=d=1、四つのqのみ。元R3/R4と正常核を両i符号計八表示でexact確認、唯一の非零W1はq=-iのk*(i b³-i c y b+c b y)。これは純base切断でB=S[x;sigma],sigma=-i scalar、正常化はSを保ちxを-i倍するので既証一般Ore cone頂点補題がH3を排除する。非零核を因子だと誤認せず無限高次Extを用いた。単冪untwist後のHも唯一のUc relationとxy+i yxの保存でH1となり、Gのtwist輸送を使わず全Jordanを扱う。

### 追加b4を含む最後のN4(i,i,-1,-i)と共役も `cubic_fourth_root_last_negative_simple.tex` で全排除

最高tensor17軌道。b4係数z0は同じeven rank条件の四表示に戻り、W1はq1でk*(yb+by)x、他は零（両符号八表示を元関係でexact ）。z非零はz1とmixed正規化を両立させ、H0のbb pivotのSchur補Tが対称rank1となる。T=v v^t,v=(p,r,s,t)でt²=-i r²,st=-i pr,s²=-i p²+q^-4-i。r0は純x²関係又は二本のU²関係でdomain外、よってr非零。eta=t/rでeta²=-i,s=eta p,q4=-i。H2の純U関係はq^-2 x²+i eta(px+ry)²となり非退化対称。
muUiのbinary twisted quarticのskew middleに対角な純U関係alpha*x²+beta*y²を入れると、rank2 Pfaffian -i alpha B,beta A+alpha D,i(-beta A+alpha D)がA=B=D0を強制し、純c²関係が生じる。これでz非零全chartが空。untwist後はz0四表示だけで、唯一のUc関係とxy+i yxから単冪H1。G正常性のtwist輸送を使わない。17元軌道、Schur恒等式、対称二次の行列式、Pfaffianと有限正常核を厳密に照合する。

### 位数3の非単位重複根の全Jordan層は `cubic_third_root_nonunit_Jordan.tex` で排除

実際のmuU=[[omega,1],[0,omega]]の逆中山巡回を半単純重み1の全85語で解き、rank75、top核10次元。H0の(xc,yc,cx,cy)主minor=256*a8^4*(omega+1)^4によりrank2にはa80が必要。このときI0にはyc/cy成分がなく、I2のyy成分は恒等的に零。よって(x,b)商はfree<y,c>又はfree<y,c>/(c²)となり、次数15が1597以上>816でAS4外。両omega符号について全kernel・元巡回式・全関係行を厳密に照合する。半単純topをJordanへ流用した計算ではない。

### 重複1のJordan層も `cubic_third_root_unit_Jordan.tex` で全排除

実際のmuU=[[1,1],[0,1]]の86語巡回系はrank74、top核12次元。局所冪零D(y)=xによりI0はx²,[x,y],bc,cb内でD0。元mixed middleの純xb,bx二列のdet=4(a6²-a5*a8)、domainにはdet0及びa5,a6,a8全非零が必要（全零は指数増大商）。t=a6/a5とするとbx=-t^-1xb,cx=-t xc、残る二mixedは同じ対角の完全graph。
I0の[x,y]射影零は(b,c)商で指数増大。射影非零を消去して、baseにbc-qcb=h x²（q非零）、残りにyx=xy+κx²+ell bcを得る。bc/cb一方だけのbase関係はdomaincancelで追加純base関係を生じI0dim3となるため除外。全六関係の順序y>c>b>xの標準語数がAS4 Hilbert値に一致し、実際にB=A[y;sigma,delta],A=<x,b,c>というOre表示を得る。sigma x=x,balpha^-1,calphaでAは量子Weyl型AS3基底。
H3 Gはmu固定なのでDG0。Ore次数最高n項へDはn*a_n*x*y^(n-1)を与えるためkerD=A。G∈A3をA/(x)=quantumplane(b,c;q)へ写すと、Gb=omega² bG,Gc=omega cGは各b^r c^s,r+s3にq^r=q^s=omegaを要求し、四通り全て不可能。従ってG∈xA2で因子化。両omegaについて全12tensor核・元mixed二列・全パラメータ量子平面gcdを厳密に照合する。通常のOre認識/最高次数議論は本文の証明であり有限計算の出力と区別。

### 全三固有値中山は半単純・位数3に限る。`cubic_third_root_CY_incidence.tex`

は残る二atlas各22次元の全最高tensor軌道と、可逆CY還元を与える。theta=muBでC=B^thetaはmuC=theta*theta^-4=1。degG3,theta3=1,thetaG1によりG*_C u=Gu,u*_C G=uGが厳密に成立し、G正常化theta^-1、左右正則性、idealのvector空間は同じ。逆にCY Cのtheta（hdet1）と同じ正常GからB=C^(theta^-1)を復元しmuBtheta,muR1。
GはCで非中心（中心ならdomaincancelでtheta1）。C/(G)のNakayamaはtheta^-1で、表示次数を反標準次数と混同しない。商圏はpointed Zhang同値だが元の反Serre orbit環はB/(G)。CY中心三次の既分類だけではこの正常incidenceを覆わない。
全22軌道を元のtwisted巡回式で検証し、wC=(1⊗theta^-1⊗theta^-2⊗theta^-3)wBが通常反巡回であることも全係数で検証。middle像から関係Iを回収、各重みrank2が全AS4候補の必要atlas（必要条件としてのみ使用）。character B3=V³-2VI+V*から正常三次係数はunit repeat8、nonunit repeat7。全basisは公開certificate。as4のSEMISIMPLE211は正確な三共鳴2011/1111/0211のみの仮定であり、本残余の追加Ub³/Uc³又はU³b等の軌道を含まないのでその八行表を全被覆として使わない（固定commit6f798e0のCLAIM及び証明冒頭の仮定だけを照合、定理輸入なし）。

### 重複1の二閉領域の全排除

`cubic_third_root_unit_closed_strata.tex`。22軌道辞書順でP=(a10,a18)はUb³、Q=(a14,a19)はUc³、S=a20はbbcc、T=a21はbcbc。P0又はQ0ならS非零は純c²/b²関係を生じdomain外。P=Q=0はcharge gradingがあり、Gのpureb³/c³係数は自身への正常式で零、Gcharge0となる。関係分布とcharge0を確認して既証相反pencilのrank1因子/AS2とrank2 GK2傾き障害を適用でき、全排除。位数>4仮定を無条件に外した主張ではない。
P,Q独立でS=T=0はGL2でP=(1,0),Q=(0,1)へ。mixedの定数単元pivotで全rank2条件を解き、H0のminor omega*a11^4からa110。純U関係a2x²+a15y²はdomainでa2*a15非零、純U反巡回blockからa4=0,a0*a15=a5*a2。全六関係はscalar正規化で一変数族x²+y²0,bx=omega xb,cy=omega²yc,b²=omega²xc+cx,c²=-yb-omega²by,bc-omega²cb=kappa(xy-yx)へ。
元の全R3/R4をQQ(omega)(kappa)で消去し、全pivot因子はkappa,kappa+1のみ。8不変三次の正常行列41×8、共通分母kappa、分母除去後Smith因子は六単元と二kappa。よってkappa(kappa+1)非零全域でW1零。kappa0は元関係fresh dim20/35,normalrank8、kappa-1はdimB3=22で非AS4。全パラメータを排除し、generic rankの特殊値外挿ではない。公開verifierは元22tensor、単元Schur pivotの九条件、全関係pivot因子、Smith及び二例外値を厳密に照合する。
S=T=0排除を次のS0全領域へ拡張した。

### 独立P,QのS0全排除

`cubic_third_root_unit_independent_Szero.tex`。T非零ならH0のbc/cb block C=diag(T,-omega*T)が可逆で、Schur0からa1=0,a0=A*E/T,a4=-E²/T,a5=D*E/T、A=a2,D=a15,E=a11。全六関係を明記した。scalar変更でA非零はA=T1へ、d=AD*T²,e=ETの二変数平面。A0,D非零は生成元x/y,b/c同時交換とomega→omega²で同じatlas（明示パラメータ変換も本文）。
二変数の全元R3/R4はgeneric dim20/35、全関係pivot因子d,e,d-e,d-e²、正常pivot因子d,e,d-e²のみ。全開集合でW1零。境界d=eはgeneric B3dim22なので元多項式行列のrank上界から全fiber非AS4。d0/e0曲線はパラメータt非零で全pivot因子tのみ、d=e²曲線は関係pivot t,t-1・正常pivot t、残る交点0/1はd=e曲線に包含。これで二変数平面全域を排除。
A=D0ならE非零、T1,E=lambda一変数。関係pivot lambda,lambda±1、正常pivot lambdaのみ、全開W1零。fresh lambda±1はB4dim37、lambda0はB3dim26で非AS4。公開検証器は全入力、Schur恒等式/正規化、全pivot因子、全四境界と三例外値を厳密に照合する。generic値を境界へ外挿したのでなく、多項式rank上界を用いたd=eの全値非AS証明と、残るunit pivot coverを区別する。

### 独立P,QのS非零も全排除

`cubic_third_root_unit_independent_Snonzero.tex`。P=(1,0),Q=(0,1),S1のmixed Schur Nはrank1で、右上はa11+omega、第三行第四列は-omega²*a12-1（定数項を保持）。N=u*v^t、domainと四係数整合からu=(p,r,lambda*p,-lambda*r),v=(-lambda*c,lambda*d,c,d),lambda(pd-rc)=-1。H0のbc/cb block K=[[T,-omega],[-omega,-omega*T]]、cross四行も本文に全式を保存。
pr非零はK特異が行空間条件とT²=-omegaの矛盾。K可逆のbinary反巡回条件によりT=2lambda²omega/(lambda4omega-1)、X=rc,Y=pdはX+Y=1/(2lambda²omega)+omega/2,X-Y=1/lambda、残る式は許容領域でlambda=-1,-omegaだけ。対角torusとrank1 factor scalarでp=r1、元22tensorと六関係の像の一致を確認し両候補B3dim22で非AS4。r0軸はK可逆/特異ともlambda=-omega²から整域又はbinary rankに矛盾。
p0軸はr1,c1/lambda、K可逆ならd0,T=2omega*lambda/(lambda²-omega)、残り一変数。全関係pivot因子lambda,lambda±omega²,lambda²+omega,H=lambda4+4omega*lambda²-omega²、正常pivot因子lambda,lambda±1,lambda±omega,lambda±omega²。全unit領域W1零、fresh±1/±omegaとHの全八次体根もrank8。lambda0/±omega²は幾何条件で除外。K特異境界はlambda²=-omega,T=-lambda,d0、binary係数a4は0又は-2/lambda³。両有限表示をPhi12体で元消去してrank8。これで全Schur分枝を覆う。通常の層別化証明と、公開exact入力/元top像一致/全pivot/例外体の検算を区別する。
unit-repeatの比例結合atlasではrank(P,Q)=1、少なくとも一方は非零で二本は比例する。

### 比例結合の一方的曲率Ore部分の全排除

`cubic_third_root_unit_curved_Ore.tex`。実際にB=T[b;f][c;sigma,delta]、sigmaTg,sigmab=q^-1b,delta b=-q^-1h,delta u=d(u)b²（d非零）と提示され、muU1,bomega,comega²なら、G=H+Fbc+C b³+D c³。正常cの最高c4からまずD0、その後の正常bのb4からC0、正常uのb3からFd(u)0⇒F0、G∈T3で二元AS2斉次因子。Dを消さずb4を比較するとc³bの曲率項が混ざるため、必ずこの順序で行う。
全AS2型の通常証明と実際の検算族を区別する。公開検算はTcomm、bx=a xb,by=omega yb,cx=a^-1xc+b²,cy=omega²yc,cb=a bc-a(h0x²+h1xy+h2y²)の有理関数体全係数。全四重なりが零で実Ore AS4整域、mu=(1,1,omega,omega²)。元関係でc4/b4/b3の三段階残差を厳密に照合する。比例結合全体をこの表示で被覆したとは主張しない。
AS4存在だけやnormal核非零だけでH3としない。

### 比例結合のS非零も全排除

`cubic_third_root_unit_proportional_Snonzero.tex`。P=Q=(1,0),S1の元mixed Schur rank1 N=uv^tはpa+sc=-2,pb+tc=ra+sd=rb+td=0。整合条件rt0。r0,t非零ではa6=a11=a150,a16=omega*t²*c/p非零。H0のbc/cb block Kが特異ならyy行(0,a16)がrowKに入らず矛盾、可逆ならyy対角零からT0、binary yy行比較でa20、純cb関係が生じ非整域。t0,r非零は反対代数（primitive omegaを逆にして全仮定保持）で同じAS4整域矛盾。
r=t0ではI1のyb/byとI2のyc/cy成分が零。a15=a160,a10。a50なら(x,c)商free<y,b>/(b²)で指数増大。a5非零なら純xy-yx関係があり、xはB全体で正常正則。A=B/(x)はHS=(1-t)^-3、3二次関係だがb²=c²0を含むため二つの独立三次overlap b³,c³を持ち、dimA3≥11>10となる。正常一次商のAS3正則性を仮定せず直接Hilbert矛盾を用いた。公開exact検算は全元22tensorSchur、rt恒等式、非零a16と全パラメータsyzygyを。
従って全unit-repeat必要残余はrank(P,Q)=1,S0のみ。

### split二方向曲率Ore族の全正常核

`cubic_third_root_unit_split_double_Ore.tex`。Aqはbc=qcb,yb=qby-qc²,yc=q^-1cy-q^-1b²のCY AS3 PBW整域。tau(y,b,c)=(y,omega²b,omega c)、B=Aq[x;tau]はmu=(1,1,omega,omega²)のAS4。Gのx次数分解はG3+G2x+a*y*x²+d*x³、x³正常係数でd0、yx²のc²残差でa0、G2∈Z(Aq)2^tau、G3はtau^-1正常三次。
固定二次の全q Smith因子1,q²(q+1)、正常三次は1,q²,q4,q6(q³-omega²)（分母はq冪のみ）。q-1はW1=k*x*y²で因子、q³omega²はW1=k*Gamma、Gamma=y³+q*omega²*bcy+q(2+omega)/3*b³+q²(1+2omega)/3*c³で純base。その他W1零。二条件はgcd1で交わらず、全値H3なし（純baseは一般Ore頂点補題）。全PBW重なり、x次数係数、SmithとPhi9体でのfresh核を厳密に照合する。一般x依存曲率変形へこのsplit排除を外挿しない。

### 二方向曲率非split変形の全排除

`cubic_third_root_unit_deformed_double_Ore.tex`。Bqのbc-qcb=h*x²だけを変形する全q,hの実Ore AS4整域。正常xの付随次数はsplitなので、q-1は全Gにx因子、q³omega²以外はW1零。q³omega²ではW1=k*(Gamma+h*K*x²*y)、K=[2+omega+(4omega-1)q-(1+2omega)q²]/3。h0既排除、h非零はxのscalarでh1へ。原始九乗根の全六埋込をPhi9体で元正常24×8行列rank7としてexact確認。正常核の存在だけではH3にならない。
x局所化degree0のB=b*x^-1,C=c*x^-1,Y=y*x^-1でQ=q*omega,kappa=omega²、BC-QCB=kappa,YB=QBY-omega²q*C²,YC=Q^-1CY-omega*q^-1*B²。z=BC-CB、S3=1+Q+Q²、H=(omega²q*Q²/S3)C³-(omega*q^-1/S3)B³、Z=zY-H中心。元NFでz9=kappa9+(Q-1)^9B9C9、z³*g=Z³+aZ+bC9+cB9、a³(Q-1)^9=27*kappa9*b*cをexact検証。a,b,cの全係数は本文/certificate。
中心一般点E=k(B9,Z)の代数は次数9cyclic symbol(B9,z9)。rho²=-a/3,Z=rho*T,u=(Q-1)^9*rho³/(b*kappa9)*B9でz9/kappa9=1-u(T³-3T)+u²=Norm_{s³=u}(s²-Ts+1)。symbolのcorestriction射影公式でBrauer周期は3以下。曲面period=indexを適用し指数≤3<9、非除法。もし元切断が整域なら次数零商/中心一般局所化も整域かつ有限次元なので除法となる矛盾。これで全族H3なし。正確なGoldie rank3やGの斉次因子分解は主張しない。
一次資料はMax Lieblich, Twisted sheaves and the period-index problem, Compositio Math144(1)(2008)1–31, DOI10.1112/S0010437X07003144。arXiv math/0511244v4 Theorem4.2.2.3 p23のstatement/定義/周辺の印刷された証明を実読し、Eが代数閉標数0体上超越次数2である仮定を照合。深い全証明の独立再監査ではない。PDF digest/URLを公開certificateへ記録。de Jong原論文の著者一次書誌も確認したが、全文DVI取得403のため未読、Lieblichの一次証明を実際の入力とした。公開checkerのはこの外部定理自体の機械検証ではない。

### 量子Weyl基底の二方向曲率Ore層の被覆

`cubic_third_root_unit_normalx_Ore_cover.tex`。実際にA=<x,b,c>がxb=omega²bx,xc=omega*cx,bc-qcb=h*x²、B=A[y;sigma,delta]でmu=(1,1,omega,omega²)なら、Ore中山からsigma=(1,q,q^-1)。重みからdelta x=F∈<x²,bc>,delta b=m bx+u c²,delta c=n cx+v b²。F非零はsigmaF=F、Gの全Ore係数がmu固定でxと可換、[G,x]最高係数N*aN*FよりG∈A3となり量子平面商gcdからx因子。F0はx正常。uv非零はscalarでu=-q,v=-q^-1へ。
元の全四三次重なりをexact再生。ybxとycbからkappa(q-omega²)=0,(omega*m+q*n)(q-omega²)=0。q非共鳴はkappa0,n=-omega*m/q、y'=y+m/(q-omega²)*xで両一次補正を同時消去し既排除族へ。q=omega²はshear分母を使わず、x進付随次数がsplitでW1零となり全補正を排除。これでこの実Ore層はyx非可換補正を含め全てH3なし。xのB内正常性は仮定していない。

### 両非零比例結合の六係数正常一次境界への必要被覆

`cubic_third_root_unit_proportional_Szero_cover.tex`。P=Q=(1,0),S0の元mixed二単元pivotからa3=-omega²A,a11=a12=D,a9=a13=E,a15=a16=a170、A=a2,D=a6,E=a7,Z=a8,T=a21。mixed像はxb-omega²bx,xc-omega*cx,Dyb+Eby+c²+(A+omegaZ)xb,Eyc+Dcy+b²+(Z-omega²A)xc。
even元blockを本文に全表示。T非零はSchur0からa1=a5=a40,D²=omega²E²,a0=A(D+omegaE)/T。D=E0は(x,c)商free<y,b>/(b²)で非AS4。その他D=eps*omega*E、q=-eps*omega²,h=-(1+eps)A/T、yx=xy+(A/D)x²+(T/D)bcの実量子Weyl基底Ore表示へ。標準語数とAS4 Hilbert値からPBW/Oreの実在を証明し、delta x非零障害で全H3なし。
T0,A非零はcross rank1がE=-omega²Dを強制。D0は純x²で非整域。D非零はeven rank2のbinary分解でa0=a1=a4=a50、even像はA*x²+D[x,y]とbc-omega²cb。qomega²,h0,delta x=(A/D)x²の実Oreに入り排除。従って両非零比例結合H3はT=A0に限る。
T=A0,D=E0ならI0が二次元純U²なので二次形式pencilにdecomposableがあり整域矛盾。よって(D,E)非同時零。rank2からa10、even像は[x,y]とD bc+E cb+u x²+v xy+w y²。全必要候補は6係数(D,E,Z,u,v,w)の六関係：xy=yx,xb=omega²bx,xc=omega*cx,Dyb+Eby+c²+omegaZxb0,Eyc+Dcy+b²+Zxc0,D bc+E cb+u x²+v xy+w y²0。D0/E0を捨てず元top像一致を公開exact検算。xは正常、正常化mu^-1。この必要表示の排除にAS4存在十分性や全同型の計算は必要ない。

### 正常一次境界の稠密開集合排除

`cubic_third_root_unit_normal_boundary_open.tex`。w非零をscalarでw1へ。S=B/xの三関係Dyb+Eby+c²,Eyc+Dcy+b²,Dbc+Ecb+y²から元次数3/4挿入を消去しdim10/15、全83pivotを再生。L=D³+omega*E³+omega²、Cj=D²E+omega^(-j)D+omega^j E²、Δ=D*E*(D³-E³)*(E³-1)*(D³+omegaE³)*(D³+omega²E³)*C0C1C2*L。全関係pivotと正常3pivotの分子/分母がΔ上だけで消えることを逐次gcd割切りでexact確認。固定三次基底b³,bcy,cby,c³、三pivot後の九残差分子idealに(E*(E³-1)*L)^3が入りGroebner零剰余。よって全Δ非零点で正常rank4、Gbar0、Gにx因子がありH3なし。u,v,Z全値同時。D2E3で開非空。Δ零やw0へ一般点rankを外挿しない。

### L曲線上の全正常incidence

`cubic_third_root_unit_boundary_L_incidence.tex`。d³+omega*E³+omega²0、Ω=E*(E³-1)*(E³+omega)*(E³+(1+2omega)/3)*(E³+(omega-1)/3)非零。y'=y+t*x,t=omegaZ/(d+omegaE)でZ0へ、u'=u-vt+t²,v'=v-2t。Γ=omega*b³+c³-d*((omega+2)E³+omega²)bcy+E*(2-(omega+2)E³)cby。全u,vで正常G=Γ+v*Astar*y²x+v*Bstar*bcx+(u*Cstar+v²*Kstar)yx²+u*v*Kstar*x³、四係数は本文とcertificateに全表示。中山逆指標正常核は一本。
検算は関数体QQ(omega)(E)[d]/(d³+omegaE³+omega²)とその上の多項式環[u,v]で元R3/R4を消去。全parameter pivotはu,v非依存定数、dim20/35、固定三次8。境界正常rank3と四補正rank4、残差全零、独立な閉公式との比較を実施。1155余のcubic norm逆元を逐一積で確認し、全分子/分母のsquarefree支持がΩ（次数13）と判定。これで関数体一点だけでなくΩ開集合の全閉点/全u,vに有効。`cubic_function_extension.py`,`cubic_parameter_polynomials.py` は分数の構造同値でなく差の零を使い、非定数u,v pivotで割らない。低次dim20/35だけから全AS4十分性を宣言しない。

### L開集合の実AS4認識と中心三次

`cubic_third_root_unit_boundary_L_recognition.tex`。S=Sklyanin(d,E,1)はE非零/E³≠1からIS Theorem1.1/Cor6.1でKoszul AS3。点曲線discriminant=(d³+E³+1)^3-27d³E³=3(omega²-omega)(E³-1)^3非零、proper ellipticでnoetherian domain。六関係とxB1の元rank10で1-regular xを確認。w3=y*r_y+b*r_b+c*r_c+u*x*r_xy=r_y*y+r_b*b+r_c*c-u*r_xy*x-v*r_xy*yの自由tensor恒等式、modxのb³係数1からW3(S)への全射。LBS2.6(5),2.7の全仮定を照合し、全u,vで実際のnoetherian quadratic Koszul AS4整域を認識した。元22軌道quartictopの全巡回と六関係への包含もexact再生しμBthetaを確定。単にdim20/35でAS4としたのではない。
G=Gamma_tildeは正則正規、R=B/GはAS-Gorenstein3 index1 muR1とcubicHS。Sdomain/Gbarregularより正常正則列x,Gを交換し、Rでもx正則。したがってRdomain iff U=(R[x^-1])0 domain。C=B^thetaではxcentral,muC1で、同じdegree0局所化Uを持つ。
中心Ψ=G+Q*y³+vH*y²x+(uH+v²J)yx²、Y=E³,Q=(omega+2)(1-Y)、H=[3(omega+1)Y+(2omega+1)(E²d+Ed²)-omega-2]/(Y-1)、J=[(1-omega)E²d-(2omega+1)Ed²]/(Y-1)^2。全交換子と閉係数、同じΩ支持をexact検証。UでT=y/xとすると中心ψ=Q T³+vH T²+(uH+v²J)T。この中心元の式だけから全中心やPI次数は決まらない。

### 境界translation位数9とアフィンPI還元

`cubic_third_root_unit_boundary_L_PI.tex`。S_CはSklyanin(d*omega,E*omega²,1)。Γ0非零δ正常、δ=(1,omega²,omega)。canonical central cubic g0の倍ならdomain/非scalarδと矛盾、よってTHCR像非零。その次数付き分数環k(E)[t±;tau]で次数3Γ0の共役は関数体上tau³であり、正常式からδに等しい。δの楕円曲線作用が非自明order3なのでtau正確order9（包絡Nakayama order3とは別）。Smith–Tate Theorem3.7 r1の中心生成次数3/9からZ(S_C)3=kg0、Ψ0は非零scalar*g0。Γ0³ modg0非零THCRdomainと斉次次数からΨ0,Γ0³は代数的独立。
D=(C[x^-1])0はgrD=S_CのPBW整域、GK3。中心ψ=Ψ/x³,g³=(G/x³)^3の最高記号が上の独立二元なのでk[ψ,g³]多項式。F=k(ψ,g³)、D_FのF一次独立な長さn語へψ^i g^(3j),i+j≤nを掛けるとbinom(n+2,2)f(n)≤binom(10n+3,3)、よってGK_F≤1。有限次元ならPI、そうでなければPappacena–Small–Wald Theorem5（affine semiprime over any field）で標準恒等式を得てDへ制限。U=D/gもPI。このGK次元の議論の結論はPI性までであり、PI次数・全中心・素性には後の中心持上げとCSAの証明が必要である。
一次入力：C.J.Pappacena,L.W.Small,J.Wald, Affine semiprime algebras of GK dimension one are (still) PI, GlasgowMathJ45(2003)243–247, DOI10.1017/S0017089503001204, arXiv math/0211330v1 Theorem5 pp4–5と全印刷証明を実読。任意の基礎体、semiprime/affine/GK1の仮定を照合。Smith–Tate KTheory8(1994)19–63、標準g0/THCR, Lemma3.5と証明, Theorem3.7と証明を著者PDFで実読しcenter3/9入力だけ輸入。両PDFのSHAとURLは `cubic_third_root_unit_boundary_L_PI_certificate.json` に記す。有限checkerはscalar/discriminant/order/GK不等式の多項式算術を再生し、幾何・GK/外部定理の全形式検証とは称さない。
v0u0はsplit頂点で既排除、v0u非零はx scalarでu1、v非零はx scalarでv1へ。高次数全語4^nの行列は避け、B_n=(B_(n-1)⊗V)/(B_(n-2)⊗I)を既存乗法行列から再帰構成して中心degree9とδ²-normal degree6を求める。

### 独立代数体例の中心部分環上自由階数81

`cubic_third_root_unit_boundary_L_finite_center.tex`。K=QQ[t]/(t6-9t³+57),d=t,E2,omega=(1-t³)/7,u1,v0,Z0。既約な全6埋込を同時にexact検証し、B2..B10とnormal-cut次数2..10を元関係の再帰商から再構築。Cの中心次数1/2/3/6/9は1,1,2,3,7、cut A=C/Gは全基底で1,1,2,3,5。正常δ²次数6は115×30rank28/kernel2で、G²以外に一本ありG倍がdegree9中心。全パラメータへ外挿しない。
A中心9の既知四元x9,x6Ψ,x3Ψ²,Ψ³に独立なz9を選び、元語係数をcertificateへ保存。Q=A/(x,Ψ)、z9像非零、元3生成元関係にz9を加え次数13まで完全再帰消去すると[1,3,6,8,9,9,9,9,9,8,6,3,1,0]、13零以後一次生成で全零。Hilbert完全列からz9正則、x/Ψ/z9中央正則列、graded NakayamaとHSからAは多項式部分環K[x,Ψ,z9]（次数1,3,9）上自由rank81。自由階数81だけではfullcenterやPI次数9は決まらず、CSA判定を併用する。
再現：`computations/verify_cubic_third_root_unit_boundary_L_finite_center.py`、汎用 `cubic_incremental_graded.py`。B_n=(B_(n-1)⊗V)/sum image(B_(n-r)⊗I_r)を全接尾関係から作り、元関係の左右作用をC/Aでdegree10、Artinianfiberで13まで再代入。全中心kernelの独立性と全交換子もexact。入力は最小多項式と元6関係/G、outputcertificateはz9/Ψの元語、全数値、33統一検算へ追加。

### 固定例の全中心・素性・PI次数9

`cubic_third_root_unit_boundary_L_finite_CSA.tex`。A=C/Gは中心部分環S=K[x,Ψ,z9]上free81。中心fiber x1,Ψ0,z91を斉次商degree12/13各81の左右乗法から復元。係数整環を109,t15,omega63へ還元（体Kからの体準同型ではない）。81基底のcentercommutator rank80とregulartrace Gram det45mod109の正のwitness、元全関係行列再代入/Gram対称性/整数overflow上限を確認。ゼロmodpから一般点upperrankを推論せず、char0free81で既知の次元上限と非零minorから同基底/center1/nondegtraceを持ち上げる。
よってgeneric A_Fは81次元central simple degree9、Z(A)はS上integralかつFracS内なのでSの整閉性からfullcenter=S。torsion-free orderのgeneric simpleからA prime。任意のalgclosedchar0kへの6埋込でU prime,Z(U)=k[ψ,z],PIdegree9。de Jong/Lieblich period=indexからRdomain iff Udomain iff Brauerperiod9。正確なBrauer周期はこの計算の対象外であり、H3排除は有限大域次元と整域性が要求する周期の矛盾を用いる。
再現 `verify_cubic_third_root_unit_boundary_L_finite_CSA.py` はSympy+NumPyを使用。NumPyはint64 mod109だけでfloatなし、内積最大81*108²=944784<2^63、各積直後にmod。source Z/Psiの全分母109unitを確認し、固定fiberの全元関係を81×81生成元行列に再代入。Gram SHA/非零det/center次数をcertificateへ。全パラメータのfullcenterを一点から外挿していない。

文献整合性の監査メモ：Smith–Tate, K-Theory8(1994)19–63, 著者PDF https://sites.math.washington.edu/~smith/Research/tate.pdf の導入と、Chan–Gaddis–Won–Zhang, Ozone groups of Artin–Schelter regular algebras satisfying a polynomial identity, MathZ310(2025)69, DOI10.1007/s00209-025-03777-9 の2.8–2.10本文を実読した。後者2.10はproper elliptic PI Sklyaninのcenter固定自己同型をscalarとするが、本直接正常核とSmith–Tate Lemma3.5の非scalar正常化、および上のtau9認識との整合性に問題があるため本研究の結論の入力に採用しない。2.10末尾の「tauの冪も非linear」とする推論は、3-torsion translationとなる冪を別途確認する必要がある。新規性と正誤表の有無は未確認。PI次数nとprojective order次数を混同せず、一次資料の規約を照合する。非scalar正常元だけで位数9やPI degree9を推測して公表しない。

### 四単純の全除外chart

`cubic_detminus1_spectral_exclusion.tex`。as4固定6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0のREADME、plan、COVERAGE、該当CLAIMS、DETMINUS1全文・自己監査・certificate状態を確認。nu=mu^-1なのでa→a^-1と後二基底交換で同じmu-chartになる。四族被覆/AS十分性/同型は輸入せず、H3域に次の直接証明を与えた。
mu=(a,-a,i/a,-i/a),a4≠±1ではU²,mixed,V²の二次重みが分離して二重次数が存在。各平面に関係がなければ自由二生成の次数7が128でAS4値120を超え、domainなら純二元関係は高々一本なので両平面はAS2。混合三次の重み±ia,±a^-1は1にならず、純U三次重み1はa6=1、純Vはa6=-1を要して同時に起きない。従って全Gは片方のAS2純三次となり因子化、H3なし。a4=-1の境界は二固有値の必要集合±1に反して空である。a4=1の境界は四単純集合{1,-1,i,-i}で、`cubic_four_simple_order4_rankA.tex` と `cubic_four_simple_order4_rankB.tex` の排除を適用する。全det負一又は全四単純をこのchartが覆うとは主張しない。公開verifierは全パラメータLaurent多項式の非零因子・共鳴・境界特性多項式と128>120を厳密に照合する。出典/仮定/未実行の上流検算はas4_imports.jsonに記録。

### Frobenius双対とnormal orderの周期障害

固定例T=A/(x,Psi,z9)の最高次数は12。全補次数pairing rankは1,3,6,8,9,9,9,9,9,8,6,3,1で完全。lambda(a*v)=lambda(nu(v)*a)の規約でnu=(y,omega²b,omega*c)、exact位数3。公開verifier/certificateは `cubic_third_root_unit_boundary_L_Frobenius`。全六埋込みに有効。
原稿の条件付き命題：中心k[s,t]上有限自由なCSA orderで相対双対V_eta、eta^m=1、全高さ1完備化normalならBrauer周期|m。局所trace双対はpi^{-(e-1)}V、radical共役の剰余中心上位数eからe|m(e-1)すなわちe|m。真のBrauer留数次数はeを割る。m倍はA2上不分岐。P2で残る無限遠直線上のsecondary residue相殺とP1の単連結性から無限遠留数も0、BrP2=0で消滅。整域ならde Jongで次数|m。
一次資料：Daniel Chan, Lectures on Orders (16 May2011), https://web.maths.unsw.edu.au/~danielch/Lect_Orders.pdf、SHA256 2280d86df8844091d96311d226ec82fdb9c721929fe2faab0df7810c08b33b19。Thm10.8/Cor10.9/Prop10.12(全印刷証明)、Thm12.5(全印刷証明)、Thm15.1(statement、証明は原資料でも省略)、Example15.4(1)(説明全文)、Thm15.6(statement)を実読。深い入力の独立証明再監査ではない。
相対双対も解決：Tの全81語基底をS基底へ持上げ、top functionalのpairingはgraded Nakayamaで完全。基底次数≤12と生成元次数1からtwisted cyclic係数は定数/xだけなのでA/(Psi,z9)次数12/13のx可逆行列で全81×4等式をexact確認。Hom_S(A,S)=A_nu(12)、nu(x,y,b,c)=(x,y,omega²b,omega c)、affine版も位数3。

### 有限大域次元の局所order認識と固定例の排除

固定E2,u1,v0は全六埋込みでH3なし。原稿 `cubic_third_root_unit_boundary_L_order_obstruction.tex` に通常の証明。DVR trace dualがfree左加群なら自己単射次元≤1。完備化の単純左右加群は元orderの有限projective分解をbase changeして有限pdを持つ。極小分解の最後の非零Extから全単純pd≤1、従ってhereditary。格子鎖標準形のblock n_iとprojective columns P_iに対し、regular module=⊕P_i^{n_i}、trace dual=⊕P_(i-1)^{n_i}。FrobeniusとKrull–Schmidtから全n_i同じ、巡回block行列がradicalを左右生成しnormal。前節の周期障害から有限大域次元ならperiod|3。一方H3の整域条件ならperiod=index9で矛盾。この固定例の証明は正確な周期・整域性単独・Goldie rankの値を用いない。全L曲線にはtrace-closed中心持上げと軌道商の証明を適用する。
外部局所分類入力：John Voight, Quaternion Algebras, GTM288(2021), Chapter21 pp343–352, DOI10.1007/978-3-030-56694-4_21。出版社一次HTML https://link.springer.com/chapter/10.1007/978-3-030-56694-4_21 の§21.3.1/Lemma21.3.3/Prop21.3.7の印刷証明、Theorem21.5.1 statementと印刷された参照（証明はHijikata–Nishida§1へ委託）、§21.5.3、Remark21.2.8のdivision版拡張を実読。原著Hijikata–Nishida/Reiner本文は未読で、読んだとは主張しない。この標準局所分類は外部入力、block双対計算とFrobeniusからnormalへの推論を本原稿で明記。機械検証の対象は固定例の相対双対であり局所分類自体ではない。
E2,v=Z=0,w1の全uも排除済み：u非零はxのscalar同型、u0は純base正常三次のOre頂点。generic中心だけでは全Ωを覆わないので分母と例外locusを保持する。

### E2全u,vの多項式中心核と自由81

公開 `verify_cubic_third_root_unit_boundary_L_polynomial_center.py` はK[u,v]上で元の全relation moduleを次数10まで構成。全relation pivotがパラメータ定数であることをassert。中心9の136列行列は、行の先頭に限定せず任意の定数単元成分をpivotとして選び、既選pivot行も戻して消去。131pivotで残余全零、核free5。全5ベクトルの元四交換子を再代入して零。u1v0で既知4中心単項式と独立になる核を選ぶとZ9は37語で、x0の5語係数は定数。新Z9を用いるArtinian境界商もdims1,3,6,8,9,9,9,9,9,8,6,3,1,0、全元左右作用次数10/13で。既証の全u,v AS4とx/Psi正則性、HSから全点でk[x,Psi,Z9]上free81。全中心/CSA9/素性が全点で同じとは結論しない。
有理関数体上の逐次RREFは係数膨張を起こしやすい。多項式行列の任意の定数単元成分をpivotに選び、既選pivot行も戻して消去すると、パラメータ分母を導入せず全u,vの核と再挿入恒等式を証明できる。
既知u1v0 CSA中心fiberの座標を新Z9へ移し、相対free81の固定中心fiberに対する中心rank80 minorと非零trace行列式をspreadすれば開集合が得られる。全中心とCSA次数を全点へ外挿しない。全u,vとE可変の結論は二fiber比較とtrace-closed中心持上げの証明を用いる。

### E2全相対双対と稠密開集合のH3排除

公開 polynomial_Frobenius verifierはuniform Z9のT境界全13pairing完全、A/(Psi,Z9)次数12/13の二81行列のinverse denominatorがパラメータ定数、全81×4 twisted cyclic identity零を確認。Hom_S(A,S)=A_nu(12)、nu=(x,y,omega²b,omega c)位数3を全u,vで確定。
新中心9の(1,0)特殊化を旧基底(x9,x6Psi,x3Psi²,Psi³,oldZ9)へexact展開し、元語へ再代入で零を確認する。a0=0、cold≠0。正の既知fiberはΨ0,Znew=b=a0+cへ移る。bの全六次体係数はuniform center certificateのold_positive_fiber_in_new_coordinatesに保存し、mod109では83。
uniform familyはP=K[u,v]上でも表示中心部分環P[x,Psi,Z]にfree81：Artinian商基底からgraded inductionで全射、各fiber同Hilbert値なので核は一般点で零の自由加群部分として零。固定中心fiberV=A/(x1,Psi0,Zb)もP-free81。traceGram T(u,v)と四交換子行列M(u,v)からU=D(detT)∩{rankM=80}を定義すると、(1,0)を含む非空開集合。全U点のgenericCSA9/fullcenterSが正のfiberから従い、相対Frobenius位数3と局所order障害で全UをH3排除。判別式/minorの展開係数は未計算、行列条件による開集合の定義と非空性の証明である。
scalar x作用の重みは(u,v)=(2,1)。UのGm飽和の不変閉補集合をP(2,1)へ写すと真の閉集合、従って有限。この稠密開集合の議論だけでは、v≠0, u/v²∈有限集合F_(d,omega)の必要候補まで絞られる。二fiber比較がこの有限残余も排除する。H3許容性自体の相対開性を仮定していない。u0v1にも正のtrace・中心rankの証明書がある。

### 第二軸排除と例外比計算の行列モデル

u0v1の公開second_CSA validatorはp109,t15,omega63、fiberPsi0,Znew83で中心1、trace determinant64、元六R2/G3/中心fiber関係行列零を。自由81は標数0全族で既知、非零minor/traceをliftして次数9CSA/fullcenter、相対双対ν3からH3なし。x scalarによりu0全v非零、原点vertexで第二軸全排除。E2で必要残余はuv非零の有限個の非零比のみ。
二つの中心fiberを比較するため、v1,u=a,p109における固定fiber(Psi0,Z83)の81次元行列モデルをGF109[a]上で作る。全relation pivotとx逆行列分母はパラメータ定数、生成元行列の多項式次数上界は0,6,5,5である。有限体の全点列挙だけから標数0の空性は従わず、標数0の全値結論には次数保存と正のSylvester resultantを使う。

二fiber比較の補助観察として、GF109の全109点では中心は一次元、traceの退化点はa=10,84（rank27）で、他の107点は非退化となる。これは固定fiberの有限体データである。有限体gcd1だけでは次数落ちで隠れる標数0因子を排除できず、一方の次数保存または固定次数Sylvester minorの非消滅が必要である。公開入力と再現コードは `explore_cubic_third_root_boundary_L_parameter_fiber.py` と `explore_cubic_third_root_boundary_L_parameter_grid.py`。

### E2全二変形・全ZのH3排除

有限例外比は残らない。公開two_fibers validatorは二center fibers(Psi0,Znew=b/1)の全モデルを先にK[a]上で実構成。全relation pivotとx inverse denominator定数、生成元の全非零係数で2deg_a(R)ji≤di+1-dj、basis filtered degreesの総和486をexact確認。trace Gram det次数≤486。モデル全rational denominatorsをp1021,t169でunit確認し、487点det評価から補間、追加8点を検査。両還元degree486で次数保存。
bar f_b=340[(a²+228a+306)(a²+471a+147)(a²+573a+1012)(a³+317a²+112a+981)]^54。bar f_1=340[(a+95)(a+110)(a+579)(a6+805a5+322a4+741a3+284a2+740a+787)]^54。全係数掛け戻し、9次二因子のBezout1を再代入、486次二式のresultant965mod1021非零。次数486保存と正のSylvester resultantによりK[a]でもcoprime、全六埋込みの代数閉体上共通根なし。有限体点全列挙だけからの外挿ではない。
trace非退化開集合上で中心rank一定の補題：regular trace dual basisからE(a)=Σe_i a e^iを作ると半単純fiberごとに中心projector、被約base上で同じ恒等式が成立しrank局所一定。irreducible openで一点のcenter1から全点CSA。各fiberのa0でpositive trace/center1/source関係行列零を確認済み。従って二trace開集合は全aをcover、全E2,v1 genericCSA9/fullcenter。x scalarで全v非零、v0既排除、L/ΩのshearでZ任意も排除。E2,w1の全正常一次境界はH3なし。実際のBrauer周期や整域性単独の決定は不要・未決定。
必要なgeneric fieldはQQ(omega)(E)[d]/(d³+omegaE³+omega²)、既存custom cubic extensionをSympy DomainMatrixのFieldへ包むか、中心kernelのconstant-pivot解法をcustom scalarで実装する。u,v polynomialの非定数divisionは避ける。固定E2で非零resultantはE方向へopenにspreadするためのwitnessだが、中心9の存在をspecialpointからgenericEへ外挿してはならない。

### 全L/Ωのアフィン包絡のPI次数9

Dの中央psiはleading canonicalg0非零倍。全lambdaでgr(D/(psi−lambda))=S_C/g0 elliptic THCR、domain。Rains arxiv2107.13540v2 Thm2.13から中心もfiltered deformation、有限中心性をleading inductionで持上げ、Hilbert leading coefficient比[(1+t+t²)/(1−t)²]/[(1+t9+t18)/(1−t9)²]→81から各fiberPI9。Dはk[psi]にTHCR語基底でfree、∩全lambda(psi−lambda)D=0。全fiberのMat9多重線型恒等式がDに降り、逆にIdDはgrD=S_Cの恒等式を与えるのでDのPI次数exact9。全L/Ωと全u,vで有効。Uのprime factors degree≤9だけが従い、Uのfullcenter/素性/正確degree9は未主張。
一次資料RainsPDF SHA256 6b8ce29a6a0a8533fde76b98af8784229b4e09769e4e6628163d565b0078c050、arxiv2107.13540v2 (17Feb2022)。参照箇所はThm2.13/前置translation説明pp15–16、Prop2.9の印刷された全証明とobstruction p11、Example2.5後Remark p14。高次Rees代数のcenter liftは自動でないと明記されており、D/Uの中心への外挿はしない。
関数体上の中心計算では GF109(E)[d]/(d³+63E³+63²) と u,v の多項式係数を使い、relation/centerのpivotはパラメータ定数に限定する。`explore_cubic_third_root_boundary_L_function_center.py --prime 0` は標数0の対応する三次拡大を扱う。特殊点の中心核の次元を一般点へ外挿せず、全値の結論にはtrace-closed中心持上げの証明を用いる。
中心持上げで必要なのは、reduced traceの環内整性と最高記号との両立である。PI次数の一致だけから中心の全射性を推論しない。必要な条件と証明は `cubic_third_root_unit_boundary_L_trace_center.tex` に記す。

### 全L/ΩのH3排除

正式な証明は trace_center節と orbit_exclusion節。中心持上げ補題：trace-closed Tと中央regular x、商S domainが同PI次数nなら、R=imageZ(T), L=FracR上S_LはCH次数nからdivision=Q(S)。中心K/Lはbounded algebraic度n、maximal subfieldのprimitive degree n[K:L]≤nからK=L。還元traceはL-linear cyclic/n正規化なのでreduced trace、全z∈Z(S)にnz=tbar(z)∈R、従ってcentre全射。kernel xZ(T)。CにStafford2.10/2.11を適用しZ(C)/(x)=Z(S_C)。
正常Γbar∈ellipticTHCRのzero divisor degree9はΓH1=H1ΓとbasepointfreeLからτ-invariant、自由order9translationの一軌道。Q=THCR/(Γbar)はdegree≥4でreduced9pointsの全sectionsに等しい。quotientE'のdegree3 central line bundleから非消滅z9を選び、SmithTate centre lift+上のtrace lemmaでCへ持上げ。Q/(z9−1)=k9⋊C9=Mat9。x,Psi,z9 centralregular sequence、Artinian total81、A centre polynomial/free81。boundary fiberMat9からgenericCSA9/fullcentre/prime。ASG dualityでrelativeHom=A_delta(12)、dehomogν³1。有限glならnormal localorder→period|3、整域ならperiod=index9、H3不可。全w1,L0,Ω非零,全Z,u,vを排除。
有限checker orbit.pyは6561 basis products、trace Gram determinant9^81、Hilbert regular-sequence total81を。外部Stafford/Rainsやgeometryをcomputer proofしたとは言わない。E2 exact二fiber/resultant proofは独立な検証例として残した。
Ω=0境界は固定omegaで33幾何点からなり、E=0が三点、E³=1が九点、d=0が三点、二つの追加cube値が各九点である。Z-shearが失敗する点とW1の次元が跳ぶ点を含むため、Ω非零の座標計算だけで除外してはいけない。全proper楕円層と残る軸点は `cubic_third_root_unit_boundary_elliptic_exclusion.tex`、`cubic_third_root_unit_boundary_axes.tex` による。

### 全proper elliptic正常一次境界の排除と二軸/99点

Φ=DωYBC+Eω²YCB+(Y³+B³+C³)/3+ω²ZBC+(v/2)Y²+uY。元B二次関係right untwist後、y/b/c関係を1,ω,ω²倍すると∂Y/∂B/∂CΦにexact一致。LやΩ、Z-shearなし。H3 Gbar nonzero（零ならx因子）、properSのg0倍ではないのでellipticTHCRにnonzero normalγ、関数体共役からτ³=δ、τexact9。EG Thm3.3.2(ii)でnonscalar centralψ≤3、ZS degree1/2zero・degree3kg0なのでleadingcanonical。trace-closed centre lift/9orbitMat9/free81/relativeν3/period obstructionが適用でき、全proper elliptic層H3なし。W1次元1を仮定しないのでΩ外のkernel jump/shear失敗点にも有効。
EG primary arxiv0709.3593v4、PDF SHA256 bb1730c492553a7e233a82e54b712f20b20a1e6d60e13324740f0d5580797901。Thm3.3.2(i),(ii)と§8.3 p32の全印刷証明を実読。iiはgeneric不要、genericが必要な3.4.5と区別。k=Cの定理は有限係数体embeddingとfiltered centre≤3有限線型系のrank降下で任意char0に適用。IS Thm1.1/Cor6.1も再読（同既知PDF/hash）。深い外部証明全体の独立再監査や機械検証ではない。
proper criterion DE*((D³+E³+1)³−27D³E³)≠0の補集合はaxesと9直線D+ω^aE+ω^b。既知Δ0必要条件を各直線へ代入しradical、axesとnonPHS D³=E³1を除くと、全て共通11次h(t)（本文の二linear+三cubic因子）。正規化D=−ω^b(t+1),E=ω^(b−a)tで99distinct points。全line degree11、共通E polynomial degree33、複数lineの残存重複なし。原点はPHS必要条件で除外。公開elliptic_reduction validatorは全potential derivative、Hesse factor、10 Δfactorsの代入/gcd/squarefree、normalized h一致、重複をexact。
99点は45個のQ(ω)既約factor表示（9lines×[linear,linear,cubic,cubic,cubic]）で計算できるが、field conjugacyをgeometric isomorphism quotientと混同しない。w=0、一方零coupling、非単位rootの22tensor atlasは、主原稿の対応する全スペクトル排除節へ接続する。
独立診断：E3の全u,v・weight0 centre9をchar0で46cols/41constant pivots/free5、全核の元交換子zeroまで確認した診断データである。小JSONをboundary_E3_center_diagnosticとして保存し、一般証明の依存とはしない。

### 正常一次境界の必要候補：六軸点のみ

二軸のSmith標準形は(1,1,1,D³+ω²)、(1,1,1,E³+ω)。関係pivotは非零軸変数のmonomial、Smith変換はconstant determinantで全非零軸値に有効。軸は各3点へ必要制限。六軸点の全u,v正常三次は各一本、原稿axis-incidence命題のG_E/G_D。元四正常式の多項式再代入まで。ZはD+ωE≠0によりshear除去可能。u=v0は頂点障害で排除。残りはv1,u=aとv0,u1。
非軸99点は45算術ケース（9 Hesse線×2 linear+3 cubic）を厳密計算して全て境界正常核零。Q(ω)とQ[q]/(q6+q3+1)で次数3/4商を全元関係から再構成し、正常行列4列の非零4×4 minorを各ケースで確認。三つのcubicには(ω,t)=(q6,1/(q−1)), (q3,1/(q−1)), (q3,q+q^-1−1)を用い、対応する既約因子恒等式も検証。固定ωでの全99幾何点を覆う算術埋込みであり、moduli同型商ではない。w=1の正常一次chartは六軸点へ必要還元される。全Z,u,vの排除は正常一次chartの完成節の証明に従う。公開verify_cubic_third_root_unit_boundary_99.pyとcertificateが証明を再現する。
軸境界E0,u1,v0のC/Gでは中心次数1,2,3,6,9の次元は1,1,2,3,5、包絡の中心9は7。候補canonical中央三次はPsi=y³+vxy²+ux²y。proper楕円の被約9点軌道の証明をfat triangle境界へ無条件に適用せず、全u,vの中心持上げ・自由81・共通CSA fiberは `cubic_third_root_unit_boundary_axes.tex` の独立証明を用いる。

### 正常一次chartの非零w全排除：補助還元

六軸点の全Z,u,vもH3なしと証明。E0,D³=-ω²型では全u,v多項式係数のcentre9重み0行列46列を41constant unit pivotsで消去し、全5核を元交換子へ再挿入。Psi=y³+vxy²+ux²y、選択Z9のx0像はパラメータ非依存。A/(x,Psi,Z9)はArtinian Hilbert列1,3,6,8,9,9,9,9,9,8,6,3,1,0、総81。H3仮定で既知の全Hilbert級数とgradedNakにより、三中心元代数的独立/自由階数81。有限次数だけでAS4全次数を主張しない。
元x0,Psi1,Z0 fiberの補助中央hによる斉次化で、p109,t4,ω63の正則trace det108、centre rank80 minorが非零、元関係81次matrix再挿入で零を確認する。正のminorが標数0にliftし、全uv共通fiberCSA9。従って全uvでgenericCSA9/full polynomial centre/prime。相対Frobeniusν3からfiniteglならperiod|3、domainならsurface period=index9で矛盾。他軸はB(D,E,0,u,v;ω)^op=B(E,D,0,u,v;ω²)及びG_E^op=G_Dを元関係で照合し、domain/左右finiteglの反対環不変性で排除。moduli同型とはしていない。全w≠0正常一次chartがこれでH3から除外された。

w0の正常一次chartでD1,E=eと置くと、e(e6−1)非零上の14×4正常行列のSmith因子は (1,1,1,(e³−1)(e³+ω²)) である。e³=-ω²をPhi18体で扱う全u,vの正常行列は27×8、定数単元pivotは7個で核は一本。例外e=0,e6=1,D=0と中心持上げを含む全値の排除は `cubic_third_root_unit_boundary_w0.tex` を参照する。

### 正常一次chartの全値排除

両非零比例結合は元22tensorから六係数正常一次chartへ被覆され、そのw≠0はproper elliptic/99点/六軸点、w0も以下で全排除された。従ってunit-repeatのrank(P,Q)=1,S0において、残るのは片方のみ非零のP0又はQ0である。
w0全値の必要被覆：D1,E=eで元関係pivotと正常行列の分母支持がe(e6−1)のみ。14×4正常行列を行分母払後Smith因子(1,1,1,(e³−1)(e³+ω²))、変換det定数/掛け戻し。e=±ω^jの6値、D0/E0両境界もfresh4×4 minor非零で核零。従ってe³=-ω²のみが残る。Phi18でE=t,ω=t³−1、全uv正常行列27×8が7unitpivots/free1。Zshear可、全uv中心3は8cols/6unitpivots/free2、中心9は46cols/41unitpivots/free5。全核元式再挿入、中央Psi/Z9のx0像はparameter非依存。
A/(x,Psi,Z9)のArtinian列は1,3,6,8,9,9,9,9,9,8,6,3,1,0。H3の既知HSとgradedNakで中心3元代数的独立/free81。x0,Psi1,Z2の全uv共通fiberがp109,t4,ω63でcentre1、trace det1の正のwitnessを持ち、標数0CSA9へlift。全uv full polynomial centre/genericCSA9/prime、相対Frobeniusν3からfinitegl⇒period|3、domain⇒period=index9で矛盾。有限次数から全AS4性を推論していない。

### 片方零結合の必要被覆

元22tensorのP=(1,0),Q0,S0ではc²行が恒等零なのでB/(x,y,b)=k[c]。H3正常式Gc=ωcGをこの商に写すと純c³係数が零。Ore表示を仮定しない。
T=a21=0のeven対称blockは右下零、全rank2ならcross rank≤1。cross0なら純U²二関係pencilのrank1因子でdomain外、従ってcrossrank1、純Uのrank2二次Qが一本あり二元AS2を定める。b-mixedはUb+bUだけ、domainなら両射影自動同型。c-mixedの両射影(Uc及びcU)が同型で、evenのbc/cb両射影係数が非零なら、六関係の標準語T0語·b^i c^jが張る。AS4全Hilbert値との一致で独立になり、T0とb拡大が実際に埋込み、結合則が自己同型型の一方曲率Ore表示を与える。既存curved_Ore除外が適用可能。この条件領域は全排除。
証明はcubic_third_root_unit_onezero_projection.tex。元22tensorのmiddle、even、c²行零と全2×2射影minorを公開検証器で照合する。数学的Ore認識は通常証明で、有限標本を全被覆証明に使っていない。

### 重複1の片方零結合もT0全排除

前節の射影条件はT0で自動的に成立する。even cross列R=(a2,a6,−a11,a15),S=(a3,a7,−a13,a16)はrank1。R0ならmiddle最初二行の最後二列が零、domainが強制するUb射影rank2から全行の最後二列が零となる。a8,a9,a12,a17=0となって第二行零、矛盾。S0もbU射影rank2から第四行零の矛盾。従ってR=ρS、ρ非零。純U関係Q=[[a3,a7],[−a13,a16]]はdomainからdetQ非零。元middleのminor M[(bx,by),(xc,yc)]=(ω+1)²detQ、M[(xb,yb),(cx,cy)]=ρ²detQ。従ってc-mixed両射影可逆で、bc/cb両係数も非零。前節のAS2–Ore認識と既存curvature因子障害で全T0を排除。
この通常証明を同じonezero_projection節へ系として統合、元二minorとR0/S0強制零行を公開checkerで厳密に照合する。

### T非零第一rank-one型の全値排除

P1,Q0,S0,T≠0,a16=s≠0のrank1残余はλ=a17/((ω+1)s), Schurからλ4=ω。λωではh=r、T,sはtop diagonal weights xb³/y²bc/b²c²でT=s1へ正規化可能。三係数A,r,κの全モデルを元22tensorから構成し、source pivot/denom支持はA,r,κ+r,κ+2r,J=(ω+1)A+κr+r²,H=−(ω+1)A+κ²+3κr+3r²,L=A+ωr²。全非零開集合の正常44×8行列は8個の係数体定数pivotで全核零。
残余scalar weights(A,r,κ)=(2,1,1)を使い、r1の6曲線A0,κ−1,κ−2,J0,H0,L0、r0κ1の1曲線とrκ0のA1/0二点で全境界を被覆。各一変数関数体で元関係・正常8pivotsと全分母/元画像6minorを再計算し、bad polyは全てQ(ω)でlinear split。重複除去後11fresh pointsは核零又はnonAS4 Hilbertで排除。J0一般点dims3/4=22/46を20/35に切り詰めていない。
`cubic_third_root_onezero_plus.py` と `verify_cubic_third_root_unit_onezero_plus.py` は、独立な二つのSchur恒等式、top weights、元のeven Schurの掛け戻しを照合する。これでa16T非零,λωの全層がH3なし。

### 片方零結合の全排除

三固有値全体の結論は `papers/sections/cubic_third_root_nonunit_zero_column.tex` の `thm:cubic-three-eigenvalue-sector-empty`。重複1はunit_onezero_completion、非単位重複rootの非零列はnonunit_independent、nonunit_proportional_open、nonunit_proportional_Tzero、nonunit_isolated、nonunit_degenerate_selfの各節を経由する。Q=0の別分枝を含めて必要被覆を保持している。
最後のp=r0ではcがU上で正常、c u=F(u)c、FJF^t=−ω²J。元二列はLb=T c²,bL=ω²T c²（L=mx+ny）。domainからL,T非零。F²L=ω²Lで、Lが固有vectorならc全正常、B/cにLb=bL0が生じHilbert矛盾。L,F(L)独立ならCHからFdiag(ω,−ω)、self offdiagのみ。generator/top変更でs=m=n=T1。元rank2条件の12linear式はrank7で一変数Dへ。全値source画像はcx=ωxc,cy=−ωyc,(x+y)b=c²,b(x+y)=ω²c²,bc=−((D+ω)x+Dy)(x+y),cb=−ω²(x+y)((D+ω)x+Dy)。unit6minor/係数体分母で全値同定。正常33×7は定数7pivot、全source/normal例外はD(D+ω/2)(D+ω)。fresh D0,−ωは正常核零、D−ω/2はB3dim22。これで最後の列も全排除。

### 四単純位数4の必要atlasと第一rank型

スペクトル(1,−1,i,−i)の元twisted-cyclic四次topは16次元。二次weight groupsは0:(xx,yy,bc,cb)、2:(xy,yx,bb,cc)、1:(xb,yc,bx,cy)、3:(xc,yb,by,cx)。0block対称、2block交代、1/3paired。trace成長の分母1+(r0−r2)t²+t⁴と1+(6−4r1)t²+t⁴から必要rank型は(2,2,1,1),(2,0,2,2),(0,2,2,2)のみ（重み0,2,1,3順）。各B3重み次元5。
最後の(0,2,2,2)は全H3排除済み。H0zeroから八係数零、domainでa3,a4,a7,a9全非零、対角でa3=a4=1,a7=a9=q。残りA=a5,h=a6,k=a8,E=a13、rank2Mの全minors GB13で必要被覆。A=E0はq=t²,k=t,h=±tの全t非零Oreモデル、x/y正常固有値により全Gがx又はyの因子を持つ。残余は対角十軌道へ。二軌道正常核2は全x因子、七軌道正常核零。唯一残るq−1,A1,E0,h=i,k−iの正常核1はG=c²y−bcx/2+i cbx/2。
この最後の包絡はb²+c²,xy−yx,xb+bx,xc+cx,yb+i by−i xc,yc−i cy−xb。normalx開集合の次数零環はYB−i BY=iC,YC+i CY=B,B²+C²0,2C²Y−BC+i CB0。原点characterの自己Ext1はY方向1。H3 Serre=(-1)[2]をnormalxで同定するとH(Y,B,C)=(Y,−B,−C)、Ext1に恒等作用。twisted Serre traceの符号から非退化交代対が必要となり矛盾。S(L)=L[2]だけで作用自明を仮定せず、唯一のY方向に実際に作用が自明と確認した。
通常証明はcubic_four_simple_order4_rankC節。公開検証器が照合する事項（16top/rank/GB13/全値sourceunitminor/十軌道/因子/例外G/dehom/character接空間）。全四単純又は全H3完成とは呼ばない。

### 四単純位数4の排除

残る(2,2,1,1)はpaired M=P Q^tの巡回四binomial式とdomainから全十support、六chartへ。primitive iの選択変更とb/c交換で三chartを見れば十分。P02はH2純平方からa14zero,a0v非零、H0rank2 Schurから純x²又はy²。P13はH0純y²とH2純c²で全排除。P01/Q23はPfaff a0a14=−pqとH0Schurの(1+i)pq/a0非零で矛盾。元16tensor/全support/全Schur恒等式公開default 。
最後の(2,0,2,2)はH2zero。H0=[[0,0,u,v],[0,L,B,C],[u,B,D,0],[v,C,0,−iD]]。u=v0はdomainがD,BC,Ah非零を強制しMに3minor−A²C。片方のみ非零は純bc/cb。uv非零をu1,vρへ、H0SchurでL0,CρB,D(ρ²−i)0。B0はdomainE,k非零だがM3minorE²。B非零をB1へ、rank2の単元ρpivotで全条件hk+ρA²−iρ²=0,h(E+ρA)=0,k(E−ρA)=0,ρhk−E²+iρ=0。
全値は二つのOre曲線(h=k=D0,A=t,ρ−it²,E±t)と18有限対角軌道へ。曲線のb,c正常固有値の二条件は固定三次の全五基底方向でgcd定数、全t非零正常核0。有限点はhk非零2点、hのみ/kのみ各4点、D1かつt4−iの8点。QQ[z]/(z8+1),i=z4で全18根の元商dims3/4=20/35、正常28×5又は25×5全rank5。
従ってスペクトル集合{1,−1,i,−i}は全H3排除。既存一般chartと合わせ、全非零aで(a,−a,i/a,−i/a)も全排除。ただし全det負一スペクトルの被覆ではない。通常証明はfour_simple_order4_rankA/rankB節。

### 全四単純の四曲線／有界有限点への必要被覆

四単純H3スペクトル全体は、ある共通位数N≤96の有限集合、又はλ_i=α_i t^{n_i}（α共通位数M≤24、t非零、有限位数も含む）の四方向n=(0,0,1,−1),(0,1,−3,2),(0,1,−2,1),(1,−2,−1,2)で必要被覆される。Mは24の約数とは限らない。これは存在やH3十分性・群oid分類ではない。
証明はfour_simple_spectral_curve_atlas節。二次指数u、Gの実際の全三次support、topの実際の全四次supportの有理span Lを使う。二次u/三次vだけの平面ではquartic全変数被覆が不可能なのでrankL≥3。rank4はu,v,wと追加cubic又はquarticのdeterminant、三型の最大det(48,96,48)/(36,72,36)から共通位数≤96。rank3は全top/Gがprimitive kernel n重み0なので、μが有限位数でも実際のtorus作用とG固定を得る。正のregrading deg=N+n_iのHilbertpole4からsum n_i0とΣr_s s²=2Σn_i²。全21×20×35指数kernelとquartic被覆で1062方向、sumzeroと置換/反転で10型。domain Segre上界とmomentで各I2重みrankが一意。六型は共通一次因子の通常証明で排除。残四型のphase代表はSmith最大因子≤3minor gcd、最大gcd(12,24,12)と符号から共通位数M≤24。

### rank三supportのphase削減と二方向排除

全support格子rank3のうちn=(0,1,−3,2),(0,1,−2,1),(1,−2,−1,2)はそれぞれ(1,t,t^-3,t²),(1,t,t^-2,−t),(t,t^-2,t^-1,t²)へ必要削減した。topがmultilinearだけならmiddle像が六pair直和になりdomain/rank6からskew、という補題を使う。全M≤24位相/quad衝突/quartic支持を公開default 。
最初の方向はb,yが正常、Gにx³とybc双方が必要。B=A0[b;g]、A0はxy,yc skewとAxc+Ccx+Dy²のAS3。片側xc係数零は正常yとdomainから逆向き独立quadが生じるので不可。Ore/Koszul双対からA0 AS3、topのxyc非零によりhdetg=ade、μb=ade。正常bの固有値比較a³=de=ade⇒a=μb1、μx1と重複。全rank3 chart排除。
第二方向はU(y,c)のAS2関係y²+κc²、他五pairskewなのでB=T[x;f][b;g]。g(x)=q x、g|Uの平方scalar d²共通、μb=q d²。非因子Gにx³とU²b双方が必要、正常bからq³=d²=q d²⇒q=μb1、μx1と重複。全rank3 chart排除。
通常の証明は `cubic_four_simple_curve_phase_reduction.tex`。公開検証器は全phase、domainの自由語恒等式、normalizer idealを照合する。
重要なscope：有限位数のμで追加の非零n重みtop/G supportがある点はrank4有限部分に保持する。上の斉次chart排除から曲線上の全finite ambientを排除したとは呼ばない。

### phaseなしrank三chartの排除

(t,t^-2,t^-1,t²)の元10tensorを公開一般diagonal_top helperで構成。paired rank1二式とdomainで六multilinear係数非零、a1=1,a2=p,a4=q,a5=r,a7=pr,a6=pr/q。H0のU(xb,bx)/V(yc,cy) crossは[[q,r],[−pt,−prt/q]]=column(1,−pt/q)*row(q,r)、全rank1。対称rank2H0で両射影同型はcrossrank2を要求するので、純U又は純V関係が必ずある。前者x,b正常、後者y,c正常。残る混合関係の両向き係数は逆向き関係/domainで非零。全六逆順pairの標準三次語20とAS4dim20から全overlap零、量子平面上逐次Ore（最後は二次derivation）を得る。normalbase元の中山固有値は他三生成元への正常化scalar積。
Gはx²y,b²c双方を持つ。純Uの場合normalx scalars(a,b,c)にa=b²c=abc=λx、従ってac1,bλx。変形yc/cy対xbの自己同型固有値が1対λxなので変形非零ならλx1⇒t1。純Vの場合normaly scalarsa²=b²c=abc=λyからa=b,c1、変形xb/bx対ycの固有値λy対1なのでλy1⇒t²1。変形零はskew、いずれもfour-simple H3なし。
通常証明はfour_simple_last_rank3_curve節。公開検証器は元10tensor、全rank1式、cross外積、両normalizer ideal、逆向き自由語恒等式を照合する。前節の中山scalarとgeneratorの表記をλ_bに明確化した（数学的主張の変更なし）。
従って残る全四単純の必要被覆はrank3の(α,β,t,γ/t)、phase共通位数M≤24と、rank4共通位数N≤96の有限部分だけ。finite tでも追加supportは有限部分に保持する。

### rank三phase chartと四単純の有限化

全四単純H3の中山は半単純で、共通位数N≤96の有限集合に限る。全support格子rank3を全排除した。これを全四単純又は全H3の完成とは呼ばない。
通常証明はfour_simple_zero_pair_rank3節。正常一次zとφ_zについてμ_B(z)=hdet_B(φ_z) zを証明：中心はAe-resolutionの二中央作用のchainhomotopyからNakに固定、B^{φ^-1}でz中心化、既存RRZ Thm0.3 fullscalar右公式μ_twist=μ H^-4 ξ_hdetHを適用。一次資料RRZ Thm0.3/5.4(a)/0.3の証明を再確認（PDF SHA28b4b649089bbebb722664452c665f8a43ad5b8d9589925b2f97818322736e25）。これは既存文献のscalar項を新たに明示適用したもの、as4新規輸入なし。
n=(0,0,1,−1)ではb,cはU上対角正常、FrobeniusからM:β−α,γα^-2又はS:αβγ1。Sの平方衝突γα²/β²は別分枝として保持した。α5/9は孤立因子、α3は追加7tensor chart(α,1,t,α²/t)で正常xのhdetからφxが全固定三次に1倍、必要固有値αと矛盾。平方衝突を省略してSのαβ±1を主張しない。残りSはskew/交代rank1不可からαβ=±1、非零Gからα6=1。Mもα6=1。七位相型の全default Sympy列挙。
M非符号2型はtop6のpureAS2因子、S非符号minus2型は唯一purecube。S primitivecubeはtop10 crossrank1からpureU又はpureV、前者binary因子、後者正常b scalara³=d³=λ=adeと変形ad=eからλ1。S符号(1,−1,t,−t^-1)はpure-square対称blockをdomainで消し、交代rank2のPfaffからpurebc/cb。PBW固定基底x³,xy²,ybcの非因子に第一/第三必須、正常bでa³=de=ade⇒λb1。
M符号(1,−1,t,t^-1)はxy/yx交代blockをdomainで消しI0⊂x²,y²,bc,cb。bc/cb射影rank1は純AS2 U、cb変形Pの正常izerfg=diag(−1,1)がU中心xy+yxを負にするのでP0、Ore正常固有値でλb1。射影rank2はbc=P(x²,y²),cb=Q。P/Q独立ならx²,y²中心、G=Ax³+Bxy²+Cyxyのx交換子C(xy+yx)(yx−xy)からC0⇒因子x。P/Q比例ならpaired rank1の全成分非零でP両平方係数非零。正常b scalars(A,±A,1,A²)によりtop固有値A4、G固有値A3、上hdet補題でA1,λb1。全rank3完成。
公開検証器が照合する事項（全phaseと平方追加分枝、元10/9/10/6/7tensor、rank/Pfaff/中心freeword/normalizer ideals）。

### 全有限四単純の39必要ラベル軌道

共通位数N≤96の最小位数四根集合62,290,587個を全exact走査。二次衝突13,359,699、三次共鳴2,223,885、有効quartic全変数被覆134,703、raw全support rank4は5,338。Frobenius r_s=r_-s,sumr6,自己−1偶数,domain cap_s=dimtensor_s−1のDPで604集合/115 Galoisラベル軌道。
元巡回topの一monomial列をdomainから強制零にし安定化、9軌道top非退化性喪失、2軌道multilinear-only skew。全I2 character解のKoszul群環recurrenceで次数≤12に負multiplicityの出る解を全排除（各degree/component/負整数をcertificateに保存）⇒69軌道。強制pairskewによる共通一次因子と純AS2二元因子で40軌道、既排除位数4を除き39軌道/145根集合。残る位数5,6,7,8,9,10,11,12,13,14,15,18、各軌道数1,4,2,6,5,3,1,10,1,2,2,2。全指数代表と各必要relation characterはfour_simple_finite_atlas節/certificateに保持。Galoisラベル軌道はintrinsic同型商ではない。
公開verify_cubic_four_simple_finite_atlas.pyがC++17 sourceをtmpdirへcompileして全走査、Python標準整数で全115軌道を再検算。浮動根/有限体なし。C++rankは元行minorのみで各項|入力|≤4、det絶対上界4!4^4=6144、64bit overflowなし。原稿の有限表は必要被覆で、AS4存在・正常核・H3十分性を含まない。

### 全support sieveで20ラベル/45根集合へ

39必要ラベルの全I2 characterで、topの全非空count support SとGの全非空count support Tを走査した。rank0blockが触るorbitを零、monomial列domain pruningを安定化、全変数被覆/nonmultilinear、各blockのmatching rank上界を課す。残る強制pairskewから正常生成元zを決め、未知q_ijを向き付きpair scalarとする。
正常一次hdet補題とG正常式により、全zとw∈S∪Tで∏_{i>z}q_zi^{w_i}∏_{i<z}q_iz^{-w_i}=λ_z。φ_zとμが可換対角なので共通固有liftを選べることを通常証明に明記。小整数行列A/右辺bを作り、Smith U A V=D全恒等式とdetU/V±1を検算。整数左核ℓでℓb≠0modNなら排除、保存111本のℓについてSmithと独立にℓA0/非零剰余を再検証。
因子条件も全Tへ適用：旧common-skew/pure-AS2に加え、指数u²z/vz²、uz skew、vz/zv/u²内のrank1関係なら向き別書換えで共通z因子。単純sampleでなく全S/T/character被覆。39中19ラベル全排除、20 Galoisラベル/45根集合、残位数5,6,7,8,9,12、全1306必要support片。各片はcharacter番号/S,T bitmask/正常gen bitmaskで小証明書に保存。非空・AS4・正常三次存在・H3十分性を主張しない。
通常の証明と検証器は `cubic_four_simple_support_sieve.tex`、`verify_cubic_four_simple_support_sieve.py`。全20ラベル/片はcertificateから再開する。新外部/as4入力なし、新規性未確認。

### 元orbit全非零層とLaurent torus閉包

20ラベルの全top orbit非零maskを走査した。rank1blockは完全rectangleが必要、全(r+1)minorの1項matchingは不可、2項はroot付きbinomial。純二変数U²内に支持されるsource列の空間はdomainでrank≤1なので、その全2minorも課す。pairに正確に支持される一つの列があれば（block全体に限らず）forcedskew、q_ij=−H_ji/H_ijで実orbit係数比へ戻す。
全binomialは整数Smith行格子（飽和しない、torsion全成分保持）でLaurent指数を正規化、係数をQQ(ζ2N)でexact加算。minorが1非零monomialなら全層排除、2項でroot比なら必要binomialを追加して閉包。3項以上の残余や非root係数比を勝手に零としない。normalizer top/G式も同じorbit係数へ課す。全S/Tと必要characterを保持して13ラベル/33根集合、23非零mask/157G-support。
さらに(7;0,1,2,4)の唯一mask/片を通常Ore証明で排除。base S(y,b,c)は三pairskew、x追加はδ(y)=d_yc²,δ(b)=d_by²,δ(c)=d_cb²、全d非零。逆向き係数/domainとB3dim20の全overlap零からB=S[x;σ,δ]。G=Ax³+B ybc双方、μx1なのでGx=xGがδ(ybc)=0を要求するが、δvolumeは三つの異なるPBW単項式yb³,y³c,bc³を全非零係数で持ち矛盾。
現行必要被覆は12 Galoisラベル/31根集合、22非零orbit層/156G-support片。ラベルは(5;1,2,3,4)、(6;0,1,2,3),(6;0,1,3,5),(6;1,2,4,5)、(7;1,2,5,6)、(9;0,1,4,7),(9;1,3,4,7),(9;1,3,6,8)、(12;0,1,4,10),(12;1,3,4,7),(12;1,3,7,10),(12;1,4,6,10)。全必要orbit係数A,bと各G bitmaskをcertificateに保持。
公開検証器は `verify_cubic_four_simple_orbit_torus.py`。C対角generator重みでA C^t0も検証、effective_dimension=m−rankA−rankCはtoric必要式だけの対角商次元、実AS4/moduli次元ではない。

### 対角商零次元片の全数体判定

全81零次元必要片を整数Smith全torsion成分と対角torus作用で30点へ漏れなく被覆した。A C^t0、rankC=p−rankAを全片で確認し、連結対角torus像が解の単位成分と一致するので自由座標を1へ正規化できる。全有限成分を保持。共通根位数5,6,9,10,12,18のQQ(ζL)上で全点をexact判定：26点正常核0、3点B3dim22/B4dim46で非AS4、1点はN9(0,1,4,7)のB=S(y,b,c)[x;σ], σ=ζ9^6で正常核pure S3。既存一般cone頂点補題lem:cubic-skew-cone-vertexから最後の点もH3なし。通常証明はfour_simple_zero_dimensional節、公開verify_cubic_four_simple_zero_dimensional.py/certificateに全81片から30点への被覆と各exact rankを保存。
現行必要被覆は5 Galoisラベル/10根集合：N5(1,2,3,4)51support片（toric商dim1/2/3の個数18/18/15）、N6(0,1,2,3)11片dim1、N6(1,2,4,5)9片dim1、N7(1,2,5,6)2片dim1/2、N9(1,3,6,8)2片dim1/2。合計75必要片。ここで得る表示は必要候補であり、AS4存在やH3十分性を意味しない。Galoisラベルをintrinsic同型商と呼ばない。

### 正次元片の元rank条件と五曲線への削減

75正次元必要片にCの独立列のorbit係数1 gaugeを追加し、Smith全torsion枝を保持して16表示へ。全元weight blockの(r+1)minorを数体Laurent多項式としてexact計算、単項式単元を除く。N5の唯一dim3表示は二minorの差−4ζ10³で空。他14の非自明表示では全minorのgcdが実際にminorとして現れるのでrank上界locusは証明書の単一式と一致（一般点のみでない）。一つは全torus。有限になった12parameter点はQQζ20/24/28/36でfresh全Hrank6、B3/4=20/35、W1核0を確認して排除した。N6(1,2,4,5)ラベル全体が消える。
現行必要被覆は4 Galoisラベル/9根集合、五つの一変数表示。positive_rank_certificateのbranch0,3はN5(1,2,3,4)、branch7はN6(0,1,2,3)、branch10はN7(1,2,5,6)、branch13はN9(1,3,6,8)。元75片から全表示への被覆・位相・係数Laurent指数・全rank式を公開certificateに保持する。通常証明はfour_simple_positive_rank節、verify_cubic_four_simple_positive_rank.py/positive_finite.py default Sympy（後者のdegree被覆assert追加後も検証器で照合する）。

### 最大単冪Jordan4領域も全排除

中山が単一固有値1・サイズ4単一JordanブロックのH3は存在しない。通常証明はcubic_principal_unipotent_vertex節thm:cubic-principal-unipotent-empty。既存の単冪ねじり解除B=C^H,H=expNと正常三次輸送を使用し、as4の新しい全CY分類やprincipal存在定理は輸入せず元tensorから独立構成した。
反巡回66方向のN総作用核12を元256語で計算し、指定12語座標を単位化。col33純x0²からa11zero、a9zeroならpurecolumnが3a10+5a8zeroを強制し、x0,x1を殺した商が自由二元/(x2²)へ全射して指数成長矛盾。従ってa9unit1。top最高weight6は交代tensorだけ、六pairのsource minor±1、全関係が逆順commutator＋低weight。AS4 Hilbertと順序語の張りから全次数weighted PBW、grC可換poly。
N固定三次Fの先頭は可換Sym³N核（weight0,2,3）なのでweight≤3、J=(x0,x1,x2)のJ²に入る。HはJを保ちBtwist後もJ²は同じ。P=πk[x3]の全tails自己拡大を2×2行列で構成し、x3恒等化後のJ三成分はA f(n+1)=D f(n)、A,D下三角対角1。元全係数のまま検証。F∈J²は一次条件を課さず、Ext1(P,P)3次元、shift単冪det1。一般のSerre trace補題b(v,w)=−b(Tw,v)からdimE奇数ならdetT−1が必要となり矛盾。S(P)=P[2]だけから作用恒等と仮定していない。
公開verify_cubic_principal_unipotent_cover.py/vertex.py 、対応certificateに元12核、全rank6三枝とA/B全係数gauge、weighted六関係、拡大monodromy、可換三次核を保持。coverは幾何学的必要被覆でAS十分性を主張しない。Serre/tailsの通常証明を機械形式化したとはしない、新規性未確認。

### 単一固有値のJordan(3,1)も全排除

全18元CYtop核を独立構成し、col22=a6 x0²からa6zero。a12zeroならcol12=a4 x0²でa4zero、x0,x3を殺した商が自由二元/(x1²)へ全射し指数成長矛盾。従ってa12unit1。weight(0,1,2,0)の元六関係unitminor−1、最高項はgrC=k[x0,x1,x2][x3;δ]、δ=(h x0²,h x0x1,−3h x0x2+2h x1²),h=a4。AS4 Hilbert＋順序語の張りから全次数weighted PBW。Nδ=δN、Nx3zeroなのでPBW上Nは可換baseだけ、三次核6次元/最高weight2。F Nfixed⇒F weight≤2⇒J=(x0,x1,x3)のJ²。全係数のpoint P=πk[x2]の自己拡大はExt1=k³、shift M=[[1,0,0],[1−2a11+3a16a4−a7−2a9,1,a16−a14],[3a4,0,1]]、det1, (M−I)³0。前節のgraded Serre determinant補題で全Jordan(3,1) H3 empty。通常の証明は `cubic_jordan31_unipotent_vertex.tex`。

### 単一固有値のJordan(2,1,1)も全排除

通常証明cubic_jordan211_ore_vertex節thm:cubic-jordan211-unipotent-empty。元32CYtopでweight2唯一のcolzz純x0²をdomainで消し、残topweight≤1。weight1三次tensorfの両端収縮空間Qは、dim≤2ならdecomposable二次を含む（片端rank1又は両端2の支持A,Cを比較、A=Cならbinary determinant）。従ってdomainがrankM≥3、middle rank6が≤3を与え、rankM3/I2∩U²=Q3。
混合射影の片側核はuz+q又はzu+q、Nを作用してux0/x0uの関係となるためdomainで不可。両側同型からOregraph。N^d(Σs_i z^i)=d!s_d x0^dで冪独立、σ/δが実baseSへ降りC=S[z;σδ]、HS=(1−t)^−3。基礎AS3を仮定で追加しない：top四収縮の一つはpuref、他三つのmixed成分独立なのでS0=T(U)/QのW3dim1、S0_3dim10=実S3。σQ/δQは次数2/3で既にS0に零、Ore構成からS0=S。domainとHilbertEulerで線型1331複体完全、f両端非退化でKoszul AS3。noetherianはOre自由基底で降下。
H3正常FはNfixed、上の冪独立からF∈S3。B=C^Hも同じbase上のOre、normalizerH4はS固定/z→z+4x0。新一般lemma:cubic-derivation-Ore-vertexで排除した。導分付きOre B=S[z;σδ]、S noethKoszulAS3、G∈S3正規正則、θS=S,θz=λz+hならR=(S/G)[z;σbarδbar]。M=k[z]のExt_B集中3（S自由基底/AS3）、ReesでExt_R集中2、ASGor parameter1局所双対から全O(a)に対するP=πMのHom-acyclicityとHomdim1。基礎A=S/Gの最小解消をRへ誘導しExt^n(P,P)=β_n^A(k)。1/HA=(1−t)²/(1+t+t²)非多項式で無限高次Ext、H3に矛盾。z正常/未証明局所化を仮定しない。
公開verify_cubic_jordan211_ore_reduction.py/certificate （元32kernel/block/全収縮/自由語微分）。全rank-domain/AS3降下/局所双対は通常証明であり機械形式化としない。新as4定理輸入なし、新規性未確認。

## 4. 非CY符号型：重複度 (1,3) と (3,1)

`cubic_order2_full_moduli.tex` の `thm:h3-order2-full-arrows` と `thm:h3-order2-full-inertia` が (1,3) の全切断・矢・慣性をまとめる。(3,1) の排除は `cubic_positive3_diagonal_monic.tex`、`cubic_positive3_Jordan_monic.tex` までの被覆を用いる。

### 全(1,3)H3 admissibilityをconic bundleで完全判定

原稿lem:h3-order2-local-conic-criterion、thm:h3-order2-complete-conic-admissibility。八係数AS4/eunit領域でR H3 iff rank3 conic bundle総空間smooth iff plane quarticF4が被約nodalで全singular点がQ=U=4V−ez²0のrank1 fibreである。全(1,3)対象の被覆と必要十分許容条件が完成した。

局所rank3はAzumaya。rank2ではCl2(unit,f)=commutative doublecover(z²−f)#mu2、f linearならregular gl2、f∈m²ならsingular commcoverの剰余体無限pdがinduction/restrictionでorderにも残る。rank1ではCl2 r²=a,s²=c,{r,s}=d、a/c/d∈m。中央linear maprankmならExt1selfdim4−m。単位odd方向でpoint shift固定、H3 Serre Ext2self1高次0とfree resolutionEulerでm2必要。唯一のquadratic relation alpha r²+beta{r,s}+gamma s²の行列はYoneda/Serreで非退化、beta²−alpha gamma!=0必要。逆にlinear pencilをdiag(x,y)にしoffdiag高次をxA+yBによるGL2形式合同/中心座標変更で逐次消すとexact diag(x',y')、完成quantumplane−1 gl2。binary radical tangent pencilのresultantとdet-pencil discriminantもbeta²−alpha gammaに等しく、これがconic総空間smooth/判別nodeと同値。rank0は大域bundleで不存在。

Divisionも全許容点で証明。判別D=3E+4F ampleconnected。nodeがあればlocal quaternion(x,y)のx-residue y∈k((y))はvaluation1で非平方、globalBrauer非零。node無しならD smoothirreducibleplanequartic、genericresidueはsqrt(Q/(e y²))。仮に平方ならf*yはO_D1の有理sectionで平方Qが正則なので極なし。H0(P2,O1)=H0(D,O_D1)からf*y=linear ell、Q−ell²が次数2でD4上消えQdoublelineとなるが、Qのx/z minor−1/4に反する。よって全点genericdivision、Clifford束認識でrank/Serre/AZ/例外性/整域/Hilbert/AS4を全て満たす。

H3係数locusはprojective conic bundleのrelative singular incidenceの像の補集合なのでZariski open、任意底変更/fpqc局所性に適合。この表示族のfiber条件である。内在相対族への認識・降下は第12節の仮定の下で適用する。既知normalaxis点(0,0,0,1,-1,0,1,1)は二smooth conic四横断nodeで非空を確認。verify_cubic_order2_conic_admissibility.pyはlinear kernel/discriminant/resultant、formal合同の各次数消去、正例と悪いtriplepoint校正を厳密に照合する。無限formal reduction、Brauer/residue、H3認識は本文構造証明。

具体的なnormal-axis外のH3：params(1,0,0,0,1,0,0,1)、rels puanti,pwcomm,uwanti,{u,v}=p²,{w,v}=u²,v²=w²、G=(pv+vp)w−u²p。AS4 resultant1、F4=xz(4x²−z²)−y4。binary quartic四因子が相異なり∂yでy0だけ調べればsmooth、従ってgenus3 smooth判別を持つH3。共通軸u/wどちらも全包絡で正規でなく既知Clifford swap部分とintrinsic pointed非同型。Nakayama通常det−1なのでskewにも非同型、非CY。文献新規性未確認。この例のmu8作用はp->zeta8 p,u->u,w->zeta8^-2 w,v->zeta8² vで与えられ、全慣性は `thm:h3-order2-full-inertia` による。

8係数slice H0(P in v²)=0を保つにはtarget a*t+d*r=0という一条件。9係数にv²=kP+gX+hYを許せば全semi-direct group(Gm)^4 ⋉Ga²（共通gradingGmを割る）が作用し、sliceはfppf gauge。許容openの全係数矢とstabilizerは `thm:h3-order2-full-arrows` と `thm:h3-order2-full-inertia` により四次元表示stackを定める。

### 全(1,3)表示の全矢と四次元stack

全(1,3)許容八係数表示の全幾何学的intrinsic矢を三角生成元写像と九係数式で確定した。正規三次はalpha*gamma*delta倍。共通次数尺度を除く明示表示群oidはsource滑らか相対次元4、安定化Lie環はAS4 resultant非零により全点零、従って滑らか既約DM4の表示stack。ad非零開ではa=d=e=1,b=0へfppf正規化し、許容A4_(c,f,g,h)×Bmu2。

原稿thm:h3-order2-full-arrows、verify_cubic_order2_full_arrows.py/certificate。全矢p->alpha pprime,u->beta uprime,w->gamma wprime,v->delta vprime+r uprime+s wprime。各二次関係比較九式、G共変式、一般正規化は普遍Clifford--Ore模型で厳密に照合する。Lie環はbeta1でC=-D,R=-bD/2,S=-fD。a(D-2A)=dA=3cD=(ab/2+df)D=(2g-b²/2-ef)D=(4h-bc/2-f²)D=0。D非零ならa0/dunitではc=f=h0、d0/aunitではb=c0,g=ef/2,h=f²/4となりAS resultant零。全点有限エタール慣性でDM。表示群oidは任意基底環上の明示式で定義し、全幾何学的intrinsic矢を被覆する。

### 全(1,3)慣性と増大曲線

全(1,3)の全幾何学的矢と滑らか既約DM4表示stackを確定。一般ad非零開は許容A4×Bmu2。全慣性は四種類：a=c0の閉正常軸面はmu2×mu2、d=b=c0の閉曲線はgbar=g−ef/2非零でmu4、gbar0で唯一のmu8点、その他全点mu2。曲線はgbar/hbar正規化により[A1_kappa minus{kappa²=-1}/mu8]、coarse j=gbar²/(e²hbar)∈A1 minus{-1}、hbar=h−f²/4。両増大閉部分は非交差。全(1,3)被覆・必要十分admissibility・幾何学的群oid/慣性・表示族stackまで完成。

原稿thm:h3-order2-full-inertia。beta1で全自己矢はgamma*delta1。ad非零はalpha²=gamma=delta1,r=s0。a0,dunitはu平行移動でb0、自己矢r=s0,alpha²1。c非零ならgamma³1だがprimitive3はg=h0すなわちv²0を強制し非H3。c0ではg0がquartic Q*(4ehx²−ez²)の[0:1:0]にQ!=0のrank2 singular fibreを作るため非H3、gunitからgamma²1で独立二符号。d0,aunitはw平行移動でf0、自己矢r=s0,delta=alpha²,gamma=alpha^-2。b非零ならdelta1、b0c非零はdelta³1だがprimitive3でv²0。残りd=b=c=f0はAS resultant a4*(g²+e²h)、quartic xz(4ehx²+4gxz−ez²)−e²a²y4、H3 iff hunit（ASopen上）。h0なら[1:0:0]が退化接錐、hunitならbinary四根相異でquartic smooth。全慣性g(alpha4−1)=h(alpha8−1)=0。曲線の正規化a=e=h1はdelta4=he²,alpha²=delta/a,gamma=e/delta、残るkappa=g/delta²、全矢mu8のkappa->alpha^-4kappa。唯一のmu8点は前記の正常軸外の具体例である。verify_cubic_order2_full_inertia.py/certificate全自己矢・discriminant・除外点・coarse不変量を厳密に照合する。

### 符号型の必要被覆と全(3,1)排除

全(3,1)は正部分の全Jordan型を含めて空と証明した。gamma0とcone枝、対角canonical AS3基礎の全aに続き、残るJordan基礎も全monic被覆上で排除。非分裂拡大は18個のD invariant quartic恒等式でv4/v3W0となり、W²rel0とvvrow非退化に矛盾。分裂後gはmuWと可換し共通固定線を持つ。muW Jordanならg unipotentで平方完成後delta0。muW semi/fJordanならAutT三角e²=c²、反射のskew derivationはinnerのみ。純根はq~C又はCprime、v²=lambda*z²+rho*x²に限り、通常Ore-y表示のmu v−が正固有値と矛盾。

原稿lem:h3-positive3-AS3-split,thm:h3-positive3-Jordan-base-exclusion,cor:h3-positive3-total-exclusion。全monic被覆とW²rel0により、非分裂のD-invariant positivequartic v4/v3W0からvvrow0を得てFrobに矛盾。split後mu v=v、g commute muW、vv cross[v,L]非零でgL=muL=L。Jordan TはD=[y,x], [D,x]0,[y,D]=2eta*xD+2xi*x³,eta=kappa−b,xi=kappa*b,b=epsilon*beta。M1semiはkappa=b!=0でAutT upper/e²=c²、unipotent/反射に限る。反射Sigma-compatible18x4 matrix rank3でinner y又はxのみ。M2はkappa=1+b,muW nonsemiでg x=x,g y=y+d x、平方完成とSigma eigen2からdelta0。純根q=A x²+B D,Bunit、normalizer条件A=−B(eta+d),(d−b)(d+kappa)0よりq~C=D−kappa*x²又はCprime=D+b*x²。epsilon負はH=mu semisimplepartのtwist(hdet1,H4id)でepsilon正へ。A=<x,v,z>はcentralx、v²−lambda*z²=rho*x²、muA=(x,-v,-z)。B=A[y;ordinarydelta]、Ore中山のrestrictionでmu v−となりpositivevと矛盾。verify_cubic_positive3_Jordan_monic.py/certificateは両reflection/centralizer/全係数root方程式/rootAS3最高tensor符号を厳密、order2_nonsplit_tensor18恒等式も当該検証器の照合対象に含む。これでgamma0/cone/diag/Jordanの全被覆を通じ全(3,1)H3 empty。

内在族の認識・降下は第12節、全CY必要被覆は第6–11節の参照先による。

### 全(1,3)候補の八係数AS4軌跡・正常三次を完全判定

八係数模型ではPBW・中山符号・正常三次の非零性と一意性・負三元Clifford全次数埋込みが成立する。全H3(1,3)候補包絡は八係数テンプレートpuanti,pwcomm,uwanti,A={u,v}=aP+bX+cY,B0={w,v}=dP+eX+fY,v²=H=gX+hY、(a,d)非同時零で被覆される。P/X/Y中心性はこのテンプレート自体からも導ける。原稿thm:h3-order2-eight-coefficient-AS4、cor:h3-order2-eight-unique-cubic。新規性は未確認であり、全係数のAS4 existenceとH3判定を区別する。

Clifford–Ore模型：中心Z=k[P,X,Y]とT上Clifford3(p,u,v)、p²P,u²X,v²H,puanti,pv+vpT,uv+vuAを作る。sigma(p,u,v,T)=(p,-u,-v,-T)、delta(v)=B0,delta(T)=2B0p,delta(p/u)=0。全六Clifford関係に適合しsigma²1,delta sigma+sigma delta0,delta²0なのでw Ore拡大/(w²−Y)が元の全六関係の環と同型。Z[T]上左rank16、PBW p^i u^j v^k w^l、全係数HS(1−t)^−4、noetherian。Tは中央ではないがD=T²は中央、Z[D]上rank32自由。従ってPXYとDは実際に代数的独立。

AS4完全条件：B1=bd−ae,C1=cd−af、Rscript=(d²h−a²g)²−(d² C1−a² B1)(B1 h−C1 g)。Rscript!=0 iff quadratic Koszul AS4、mu=(p,-u,-w,-v)。双対はQ/(PV,qP,qU,qW)、QはP/Wだけ反可換・他全可換のskew4、qP=P²+aUV+dWV,qU=U²+bUV+eWV+gV²,qW=W²+cUV+fWV+hV²。q三つはEbar=Q/(PV)で中央。P0の可換成分はV1としてU=dz,W=-azの二二次式d²z²+B1z+g,a²z²+C1z+hを持ち、そのresultantがRscript。Rscript0なら双対に非零射影点があり無限次元。

Rscript非零ならEbarはk[U,W,V]とquantum3(U,W,P)のk[U,W]上fiber productで、S=k[qP,qU,qW]は多項式環。両三変数成分はS上free8、二変数交差成分はS/(qP)上free4。depth lemma/commutative Auslander–BuchsbaumでEbarはS上free、三qは正則列。Q Koszulから正規正則二次PV商もKoszul、さらに三q商もKoszul（順方向のみ）。Ebar ASGor3index2から三q商はFrob top4,HS(1+t)^4。双対でB AS4、NakayamaはFrob双対符号から(p,-u,-w,-v)。noethAS4/成長4の既出Levasseur適用でdomain。

一次資料追加：A. Polishchuk–L. Positselski, Quadratic Algebras (AMS ULS37,2005), Chapter2 Cor6.3,p37を https://djvu.online/file/T1DOlccPNeqX0 の一次本文で確認した。Koszulから正規正則二次商への順方向を使う。直後のHeisenberg反例により「中央正則二次商がKoszulなら元もKoszul」は非可換一般には偽であり、これをこの族の証明には使わない。書誌も確認。as4から新たな包括定理は輸入していない。

正常三次G=T w−B0 p、G²=B0²P−T²Y、GのTw係数1、mu正常化全式を全八係数で確認。AS4/domain locusでは全W1はmu固定なので候補基底Pp,Xp,Yp,Tu,Tv,Tw,puv,puw,pvwの9本。係数行列46行9列は定数pivot8、残余零、Tw自由係数のみでW1=kGを全域で証明。負三元Clifford基底u^i v^j w^kはPBWの一部、自由中央KはPXYの可逆線型変換なので全次数埋込みも従う。その双対は可換三二次完全交叉E/(P)、従ってCY AS3。verify_cubic_order2_central_template.pyが全Ore/Clifford恒等式、G/平方、双対直交、resultant、全係数W1 rank8を厳密に照合する。Koszul・Frobenius・正則列は本文構造証明。

### 位数2の混合関係数と共通二平面

全二固有値の残余muスペクトル{1,−1}で、Jordanを仮定せず、重複度(p,q)と混合二次関係次元rを絞った。E=B!の二次Frobenius対合は偶/奇に直交分解し、奇上の非対称性作用nuは固有値−1だけ。非退化双線型形式の非対称性det1からr偶数。一次元側があれば奇関係の両射影はdomainにより単射なのでr<=3。2+2では各射影の核が二次元なら2x2行列式の零からrank1関係＝零因子を生じるためr<=5。

等変Koszul分母はP=1−(p−q)t+(6−2r)t²−(p−q)t³+t4。traceはJordanがあっても各次数で絶対値<=dimB_nなのでP全根は単位円上。r0ではP/t²=(t+t^-1)²−(p−q)(t+t^-1)+4の判別式が負で不可能。従って3+1ならr2、trace分母(1−t)²(1+t²)、1+3ならr2、(1+t)²(1+t²)、2+2ならr2又は4、各(1+t²)²又は(1−t²)²。有限因数分解をverify_cubic_order2_mixed_rank.pyで厳密再生した。成長/対合/整域性の証明を有限検算で代替しない。

さらに一次元側をz、三次元側の固有値epsilonとすると、奇関係の両射影の二平面像は必ず一致する。四次topの奇flatteningはP M P^t（M可逆2x2）、Az/AzとzA/zAの対角ブロックはともにrank2で、先頭zの巡回からK=epsilon Hとなるので像U=W。この共通Wで奇関係はzw=f(w)z。Frobenius非対称性の固有値−1によりM非対称、f M f^t=epsilon Mの交代部分を取るとdet f=epsilon。muはWを保存する。単なる二つの異なる二平面間の部分写像へ広げて探索する必要はない。原稿prop:h3-order2-mixed-rank。

### 位数2の隣接非退化二次と二生成元部分代数

3+1/1+3の共通二平面Wと単一生成元zに対して、四次topのzz行はq0(W)+gamma z²という実際の二次関係を与え、q0の2x2係数行列は可逆である。これは奇flatteningの非対角ブロックがrank2で両像Wに入り、巡回に出るmuもWを保存するため。純z4巡回式gamma=−mu(z)gammaから、三次元側が負（mu(z)=+1）ならgamma0に限る。

gamma0ならWの生成するTは一本の非退化二次関係を持つ量子/Jordan平面そのもの。高次追加核はあり得ず、任意の非零斉次式が一次式の積へ分解するという二生成元平面の普遍因数分解とBのdomainがそれを排除する。この因数分解補題の証明は最初から全次数dの式を示していたため、本文の主張も全正次数へ整合させた（検証器の低次数恒等式を全次数の計算検証と呼ばない）。

gamma非零ならq0(W)=−gamma z²はT内の非零正規正則二次で、q0 w=f²(w)q0、f(q0)=q0。fはT上の自己同型：z h(W)=f(h)zとzの正則性からf,f^-1が全関係を保存する。この局所還元だけからTのAS3性や二つの正常化三次による全関係生成は従わない。全被覆には後述のmonic表示と商体障害を用いる。Tは普遍二生成元三次表示（q0 w−f²(w)q0）からの商である、という必要条件だけを用いる。原稿cor:h3-order2-plane-quadric。新規CAS実行を主張しないホモロジー/tensor/整域性の証明。

三次元側が正のgamma非零は正規二次を持つ二生成元三次表示と比較する。部分代数がOre AS3であることやAS4十分性を先に仮定しない。2+2の混合rank2/4、mu固有値三種類以上も別に残る。

### 共通二平面の二行列標準形

混合関係の基底r_i=z w_i−f(w_i)zで奇flattening=P M P^t、P=(-F;I)と書く。先頭zとWの巡回式を別々に使うとFMF^t=epsilon M、mu_W=−epsilon M^tM^-1、二次q0の係数行列は非零尺度を除きQ=MF^tとなる。これはdet Fだけより強い制約。mu_Wの唯一の固有値epsilonからM^tM^-1の特性式(X+1)²、すなわち対称部分rank<=1を得る。交代部分は非零なので、基底/尺度でM0=J又はM1=J+diag(1,0)の二型。

M0ではmu_W=epsilon I、F任意det F=epsilon。M1ではmu_W=epsilon[[1,2],[0,1]]、F=[[alpha,beta],[0,alpha]],alpha²epsilon、Q=[[alpha+beta,alpha],[-alpha,0]]。全型でmu_WとFは可換、FQF^t=epsilon Q。gamma0の実際の量子/Jordan平面T_Wの中山作用はmu_TW=mu_W f²。gamma非零の部分代数をAS2と誤認しない。

数体不要のSymPy厳密恒等式verify_cubic_order2_plane_matrices.pyで一般J相似式、対称部分detとtraceの同値、alpha=+-1,+-iの全beta式、mu_TW式を再生した。既知Clifford swapはu=x−y,w=z+h(x+y)/2,s=tで、正固有直線ku、W=<s,w>、us=−su,uw=wu,sw=−wsを元の六関係の線型結合として確認。従ってepsilon−、M0、F=diag(−1,1)、量子q−1であり、既知正例を排除していない。新たな一般FのH3許容性をこの照合から推論しない。原稿prop:h3-order2-plane-matrices。

### 負三次元側の非分裂Jordanは量子平面商を持つ

重複度(1,3)、共通Wを持つ負空間A、正直線kzで、U=−mu|AのWへの拡大が非分裂とする。D=log Uの標準形はDv=w1,DW0又はDv=w2,Dw2=w1,Dw1=0の二つ。D不変四次tensorにv3W/v4項が無いことを、二次元+自明/三次元sl2加群のraising weightで証明し、別に81次元tensor空間上の18有理行恒等式（49非零乗数）を公開再生器で独立確認した。発見時のnullspaceそのものを信頼する必要はなく、証明書に各禁制座標=e_wordがDの行空間に入る乗数を保持する。

奇関係の像Wと巡回性から、四次topでzを含む項はW²z²だけ。負側gamma0とv3/v4消滅によりzz列はq0(W)、vv列もW²関係。domainによりR2∩W²は一本以下なので両列比例、B/(W)の二次関係はz²,v²間の一本。片方の係数が零なら平方一つを禁じる二文字語のFibonacci指数成長がBの多項式成長に反する。従ってB/(W)=k<z,v>/(v²+lambda z²),lambda!=0、基底変更でq−1量子平面。原稿prop:h3-order2-nonsplit-plane-quotient。

これはdouble Ore表示や全PBWの十分条件ではない。残る二つのcross偶関係がWv/vWのgraphをなすことは別に判定すべきであり、q0(W)+ell(W)vのような混合base項を無視してprojection単射をdomainだけから主張しない。既知正例のClifford swapはWへの拡大が分裂しており、この非分裂結論の対象と混同しない。

### 単項Ore一パラメータ族の全W1と排除

共通平面第一型の具体族B_aをux=a xu,wx=a xw,uw=−wu,yx=−a^-2xy,yu=−a wy,yw=−a uyで定義（a!=0）。量子三平面T3[x,u,w]の自動同型Ore拡大で全aにAS4。一次資料Liu–Wang–Wu1205.0893v1 Theorem3.3を再確認：mu_B|T= sigma^-1 mu_T。mu_T=(a^-2x,−au,−aw)、よってmu_B=(-x,w,u,−y)。y成分の符号はy次数トーラスとhdet mu1、三平面topの指標−1から決定し、Theorem3.3だけから未記載のhdet公式を推測していない。

PBW x^i u^j w^k y^lでGx=−xGの指標は(−1)^l a^(j+k−2l)=−1。恒等的に許される三次はu²y,uwy,w²yだけで、他の列を許すaの位数は1,2,3,4,6,8（合計12根）。集合外ではGu=wGの三係数が−a−1/−a+1となってW1零。全六円分体で140x20行列を元のPBW積から厳密再生成し、a1はkuwy、a−1はk(w²−u²)y、他の位数は核零。両非零核もyを因子に持ち全切断nondomain。従ってこの全一パラメータ族を排除した。検証verify_cubic_order2_trimmed_Ore.pyは一般QQ(a)核、全例外核、64生成元三重積の整合、三平面top指標も厳密再生する。

正固有生成元はu+w、W=<x,y>、f=diag(a,−a^-1)、量子平面q=−a²。これは指定した単項/trimmed部分の一具体族であり、全trimmed double Oreやbase二次項・cross導分付きの表示を被覆したとしない。既知Clifford正例はこの族ではなく、除外と矛盾しない。原稿thm:h3-order2-monomial-Ore-excluded。

### 単項Ore族の全base二次変形の排除

前族のuw+wuをP=A x²+Cxy+B y²へ置き換え、他五関係を保つ全表示もH3から排除した。domainならx,y量子平面は忠実（高次核は一次因子分解で零因子）なので、P x=a²xP、P y=a^-2 yPから(a²−1)A=(a²−1)B=0,(a4+1)C=0。非零Pはa=+-1の平方和、又は原始八乗根のCxyだけ。全係数で四つの二次Diamondを多項式恒等式として確認し、PBW・重み(x,y)1,(u,w)2のgr=B_aを得た。

H3を仮定する場合のmuは変形前の(-x,-y,w,u)のまま。本文では各chartの最高tensorを全係数で直接保存・検証して決定する。符号二chart各32項、八乗根chart26項の計90項はパラメータ多項式で、全三隣接位置の関係商射影零、w_yxwu=1、指定muの巡回式を満たす。従って全特殊値で非零、AS4最高空間の一次元性からmuを確定する。cubic_order2_Ore_base_top_certificate.jsonを独立再生し、一般のNakayama変形不変性を仮定しない。代替説明として、二次双対の逆重みfiltrationと両Hilbert(1+t)4からgrE=E(B_a)、Frobenius対合からgr mu=mu_Baを得て、base符号反転とmuの可換性で低重み補正を除くこともできる。主証明は保存した直接tensor恒等式で完結する。

a1ではGx=−xGがy奇数を強制し全Gがy因子。a−1ではx次数偶数、y偶奇にGを分解。p=u+w,v=u−w,X=x²,Y=y²を取るとX,Y中心、p²−v²=2(AX+BY)、s=pv+vp=2(u²−w²)はC=<p,v,X,Y>の中心。y偶数部G_evenはCに入りsと可換するが、正常化mu(s)=−sから反交換もするので、domain/char0によりG_even0。全Gはy奇数でy因子を持ち非整域。

八乗根CxyではPBW基底上のW1行列はC多項式、C0でrank20、全C非零がu,w同時尺度変更の一軌道なので全値W1零。PBW全族が確認されているため、局所化や特殊化の根拠無しに一般点計算を全値へ広げた議論ではない。verify_cubic_order2_Ore_base_deformations.pyは全正常化条件gcd、任意A,B/CのDiamond、sの四交換子、八乗根基準核を再生する。原稿thm:h3-order2-Ore-base-deformations。

### 共鳴cross導分と四パラメータ実AS4候補族

T_a=(xy+a²yx)、nu=(a x,a^-1 y)の次数1skew derivationはa!=−1なら全て内部。a−1ではmod内部にdelta(x)=y²とdelta(y)=x²の二本だけ。係数比較は本文lem:h3-order2-skew-derivation-resonanceの四式、内部二列の各gcdは1。これは全cross表示の被覆ではなく、指定した対角normalizing chartの導分の完全判定。

共鳴でB_(alpha,beta,gamma,delta)=(xy+yx,px+xp,py−yp,vx+xv−alpha y²,vy+yv−beta x²,v²−p²−gamma x²−delta y²)を得る。全四パラメータでnoetherian quadratic Koszul AS4整域。u=(p+v)/2,w=(p−v)/2のPBWと重み(1,1,2,2)grが前a−1単項Oreなのでnoetherian/domain。54項polynomial最高tensorの三隣接関係射影零、固定係数w_yxwu1、flatteningrank4,6,4を有理定数pivotだけで全値再生しFrobenius/AS4とmu=(-x,-y,p,-v)を確定した。

140x20正常化行列も全係数で有理定数だけの19pivot消去があり、全値W1はG=beta x²p−y(pv+vp)の一本。Gのyu²係数−2は全値非零で、Bdomainより正常正則。R=B/GはASGor3index1、mu_Rid。beta0はGのy因子で非整域。beta!=0におけるdomain性の単独判定を、この族のH3排除の入力に用いる必要はない。verify_cubic_order2_resonant_family.pyと54項cubic_order2_resonant_top_certificate.jsonがPBW・最高pairing・中山・全W1rankを独立再生。原稿thm:h3-order2-resonant-family。この包絡族のH3切断は固定点の無限Ext障害によって全排除される。

補助的なY開集合の候補式（未検証）：X=x²,Y=y²,P=p²,s=pv+vp と置くと、G²=beta²X²P−Ys²、Bのk[X,Y,P,s²]上自由階数32、Y開集合の二生成元Clifford表示 a²=−z, b²=beta²z²/4−r²−gamma z−delta, ab+ba=−alpha が候補となる。座標は z=X/Y,r=py/Y,b=v y^-1−beta z/2。このY模型の同定や整域性を定理の入力には用いず、H3全排除には以下の固定P開集合の無限Ext障害を使う。

共鳴族の中心像ではh=py,s=pv+vpがh²=PY,Ys=betaXh,hs=betaXPというcubic scroll関係を満たす。補助volume g=xyv+(alpha/2)y³−(beta/2)x³について、g²=(alpha²/4)Y³+(beta²/4)X³−XY(P+gammaX+deltaY) と、scroll上のplane cubic z r²−beta²z³/4+gamma z²+delta z−alpha²/4=0 は未検証の候補式として区別する。これらの候補式からH3許容性は推論しない。

### 共鳴四パラメータ族の固定点無限Extによる全排除

beta0は因子で排除、beta非零も全値H3でないことを確定した。B内でX=x²,Y=y²,P=p²中心、h=py,s=pv+vpについて[h,v]=−G,[s,y]=2G、他の必要交換子零。従ってRではX,Y,P,h,s中心、h²=PY,Ys=betaXh,hs=betaXP。全平方/反交換子がこの中心環に入るのでRは16本のsquare-free語で中心C上有限。R^(2)のSerre表示によりqgrRをProjC上coherent代数として扱える。

P開集合の次数零環はS=k[r,t]上rank4Clifford A：r=yp^-1=h/P,t=s/P,a=xp^-1,b=vp^-1−t/2、a²=−rt/beta,b²=H=t²/4−1−(gamma/beta)rt−delta r²、ab+ba=−alpha r²。逆にA[p,+-1;tau]、tau(a,b)=(-a,-b)でx=ap,y=rp,v=(b+t/2)pを代入し元六関係とG0、順逆生成元対応を再生するので局所環との正確な同型。r=t0の中心点は全パラメータで存在しH−1が単元。

完備局所Sでb0=b/sqrtH,a0=a+alpha r² b/(2H)とするとb0²1,b0a0=−a0b0,a0²=f=−rt/beta−alpha²r4/(4H)∈(r,t)²。ゆえにAhat=(k[[r,t,a0]]/(a0²−f))#mu2。可換環はdim2,embdim3で非正則。剰余体は無限pd、誘導M=k[mu2]も制限でk二本となるので無限pd。完備半局所代数の最小解消でExt^n(M,M)が無限高次非零。Mはchartのa=r=t0,b²−1という二単純点から来る。有限中心coherent代数の点支持Extは局所化/完備化と可換、local-to-globalは点支持で退化するのでqgrRでも無限ExtとなりH3hd2に反する。

verify_cubic_order2_resonant_obstruction.pyは全中心交換子・scroll関係・G²式、順逆chart六関係とG、完備化の平方完成とfの一次項零を厳密再生。無限pd/Extと点支持比較は本文のホモロジー証明であり、計算だけが全証明としない。原稿thm:h3-order2-resonant-excluded。局所orderの最大性や全中心被覆の未証明仮定を用いない。beta非零でのRdomainの独立判定やaffineYchartが良いかどうかを待たず、固定点一つで全H3を排除した。

### 対角normalizing chart全cross係数の排除

全六関係をT_a=(xy+a²yx)、p x=a xp,p y=−a^-1yp、v x=a xv+d_x,v y=a^-1yv+d_y、v²−p²=ell(W)v+q2(W)と書けるH3は存在しない。d_x,d_y,q2任意二次、ell任意一次を含む。H3domainからT_a忠実、dはnu-skew derivation。u=(p+v)/2,w=(p−v)/2で全語のordered monomial spanを得て、14641 Hilbert値との比較でPBWになるからT+Tvの係数比較が正当。

vを一次式だけずらして、a!=−1ではd0、a−1ではd(x)=alpha y²,d(y)=beta x²。後者はd nu+nu d0,d²0なので全aで(v²−p²)t=nu²(t)(v²−p²)。外側関係のv係数比較によりell t=nu(t)ell、内部derivation d_ell0。前補題の内部写像は全aで単射だからell0。残りq2はnu²正常化、a!=−1は全base二次変形の既排除族、a−1は四パラメータ共鳴の既排除族。vの対角係数を双方逆符号にしたchartもW交換とa->−a^-1で同じ結論。

新たなCASを仮装しない構造的な帰着。dの分類/gcd、一般base変形、共鳴全値には、それぞれskew derivation・Ore変形・共鳴障害の検証器と構造証明を使う。原稿thm:h3-order2-diagonal-normalizing-chart。反対角normalizer、非対角f/Jordan平面、cross射影がgraphでない退化部分、外側二乗投影rank2の既知Clifford正例はこの定理の被覆ではない。

### 反対角involution normalizing chartの全排除

T=(xy=-yx)、p x=-xp,p y=yp、v x=lambda yv+d_x,v y=eta xv+d_y、v²−p²=ell v+q2の全六関係を持つH3は存在しない。HFB4のordered monomial比較でPBW、外側最高項の比較でnu²id⇒lambda eta1。対角base尺度でnuがx,y交換に正規化される。skew derivationの六係数にはd0+e0=d2+e2=d1−e1=0の三条件、内部二列独立なのでmod内部はd(x)=d(y)=kappa xyの一本。d²0、d nu+nu d0からell0（内部写像単射）、q2=Cx²+Dy²。

この三パラメータ表示の74項多項式最高tensorは全隣接関係に入り、固定係数w_yxwu1、mu=(-x,-y,p,-v)の巡回式を全値で満たす。AS4なら実際のmuを決定する。140x20正常化行列は定数pivot20段、全パラメータで核零。verify_cubic_order2_antidiagonal_chart.pyが全PBW、tensor/flattening4,6,4、導分、全正常化rank20を独立再生。三パラメータ分母は一切ない。原稿thm:h3-order2-antidiagonal-normalizing-chart。

### 負三次元側の可逆normalizing chart全体の排除

重複度(1,3)、共通AS2平面T=<W>、pの作用fに加え、残り負生成元vがTを可逆nuと二次skew derivationでnormalizingし、外側がv²−p²=ell v+q2となるchartは全排除した。Jordanを零と仮定しない。PBW比較からnu∈AutT、nu²=f²。共通平面の行列式/中山式によりdet f=hdet_T f=−1、mu_T=mu_W f²。

二次元平方根分類：f非自明Jordanならnu=+-f。fscalar+-iならTはcomm/Jordan、Jordanではnu=+-f、commでは更にdiag(i,−i)があり既排除対角chart。f相異なる二値なら第一M=J型、fdiag(a,−a^-1)、T量子q−a²。量子自己同型の対角/反対角分類とnu²=f²からnu=+-f、既排除対角normalizer、q−1の既排除反対角involutionの三場合だけ。第二M1型もscalar/Jordanなのでnu=+-fへ入る。

nu=fのtrim先頭環は二段Ore T[u;f][w;sigma],sigma|T=f,sigma u=−u。hdet f−1とRRZ hdet(mu)1/LWW制限公式からmu|W=mu_T f^-2=mu_W（負二値）、mu u=mu w=+1。nu−fならu,w交換Hの右Zhangtwistが同じ二段Oreに移り、Hhdet1,H²1,index4なのでmu一次作用不変。どちらも先頭中山の重複度2+2。実際のmuはW保存、p固定、v->−v+Wなので重みW1,p/v2を保存する。実際の最高tensorの先頭項はAS4先頭環の一次元W4を張り、その巡回式からgr mu=mu_grB。よって実際の重複度1+3に反して排除される。この先頭tensor比較は未証明の一般Nakayama変形不変性を仮定しない。

原稿thm:h3-order2-full-normalizing-chart。対角・反対角の全係数排除を平方根・先頭スペクトルの構造証明と合わせる。外側二乗rank1でcrossの両射影がgraph同型となる通常領域が消え、非分裂Jordanの量子平面商領域も、残りcross射影が退化する場合へ縮小する。既知Clifford正例の外側二乗rank2は被覆していない。

### 全負三次元側は二平方商を持ちJordan拡大は分裂

重複度(1,3)のH3包絡の全域でB/(W)=k<p,v>/(p²,v²)を確定し、負三次元中山加群のWへの拡大も分裂と証明した。従ってmu負側はsemisimple又はW上Jordan2+残り固有直線の2+1だけで、非分裂/Jordan3が全て消えた。普通のcross graphだけでなく射影が退化する場合も扱った全域必要条件である。

核心はp²とvが共通AS2平面Tのgraded商体へ入ることの排除。commTならf²=mu_W^-1は非恒等だが内作用は恒等。JordanTならhdet f−1からf²(y)=−y、p²=r(z)y²,z=xy^-1の正常化がr(z)=−r(z+1)を要求しrational最高項で不可能。量子Tではdet f=hdet f−1がq−1反対角を排除し、mu_W−Iからfdiag(a,−a^-1),a²−q。q無限位数ならr(q^-1z)=−q r(z)、零極の有限性でr単項式、q^(m+1)=−1が矛盾。q有限位数ならf有限、D=Q(T)は二変数中心不変体F上有限次元。v∈D,p²∈DならB⊂D+DpがF上有限次元、有限構造定数を含む可換係数環で語の成長を抑えるとGKdimB<=2となり4に反する。Weyl商体一般のGK次元へ誤って適用せず、有限中心量子の場合だけこの成長比較を使う。原稿lem:h3-order2-rational-collapse。

偶四関係をW0へ射影すると像はp²,v²の空間。rank0/片平方rank1は指数成長。両平方rank1ならkernelをkq0で割ったcross二次元空間の両射影がfullなら全normalizing排除、どちらか退化ならv ell=q(W)又はell v=q(W)からvがT商体に入り、外側平方関係からp²も商体に入って上補題に反する。従ってrank2に限る。非分裂なら商が量子平面であることとHilbertが異なるため分裂も従う。原稿thm:h3-order2-two-square-quotient。

verify_cubic_order2_outer_square_reduction.pyは量子中山・反対角hdetの行列恒等式と、既知Clifford swapをW0にした二平方係数minor=h(8−h³)/8を厳密確認。商体のrational不可能性、有限中心成長、全projection帰着は原稿の証明であり有限標本で証明したとしない。

下記によりsplit M1も排除済みなので、半単純muの全Koszul/normalG条件から既知Clifford族への被覆又は新しい許容族を調べる。p²の中心性と負三生成元部分代数のAS3性は、八係数模型の証明を経て使う。二平方商の段階で仮定してはいけない。

### 負三次元側の全Jordan型を排除

split M1を排除し、重複度(1,3)の全H3包絡でmu半単純と証明した。新たなAS4 atlasや有限標本に依存しない。原稿thm:h3-order2-negative-three-semisimple。

分裂基底ではD=log(mu_unipotent)の尺度を取りDy=x,Dx=Dp=Dv=0、平面yx=xy+kappa x²、px=a xp,a²−1。平方投影kernelのcross一本はD不変なので両射影がkxに入り、vx=c xv+d x²,c非零。射影の片方零はv,p²が平面商体に入り商体退化補題により排除。従ってxは全Bの正規一次元となる。偶B2の基底x²,xy,y²,xv,yv,vyでD核はx²,xv,Z=vy−c yv−d xyの三次元。p²=Cx²+MZ+Nxvとpxの平方からp²x=−xp²、Zx=c xZ−kappa c d x³を比べ、(1+c)M=(1+c)N=0,2C+Nd−kappa c d M=0。c≠−1ならp²0なのでc−1。v->v−dx/2でd0にできる。

するとxv,Zはxと反可換するがv²はxと可換し、v²もD不変なのでv²=Cprime x²。s²=−Cprimeを取れば非零一次元v+sxの平方が零となって整域性に反する。kappa0（共通平面可換）も含む。verify_cubic_order2_split_jordan.pyは全導分核係数とZ/平方の恒等式をQ[c,d,kappa]上で再生し、標本検査ではない。全域帰着・一次独立・整域矛盾は本文で証明。

### 標準二周期点対とH3のExt必要条件

重複度(1,3)の全域で、全G∈W1(B)が(W)に入ることを証明。商A=k<p,v>/(p²,v²)でmu固定三次はvpvのみだが[vpv,p]=vpvp−pvpvは非零、正常化式Gp=pGから商像零。従ってR/(W)=A。z=pv+vpは中央正則、Aはk[z]上1,p,v,pvで自由。u=p+vはu²=z、A[u^-1]の次数零部分D=k[a]/(a²−1),a=(p−v)u^-1。uが二原始冪等元を交換するのでqgrA=mod(k×k)でシフトは二つの点P0,P1を交換する。点対はWから標準的でintrinsic pointed同型に自然。商からqgrRへの制限はHom完全忠実かつ完全だが高次Ext同一とは主張しない。原稿prop:h3-order2-canonical-two-cycle。

H3のS=(-1)[2]からExt^r(Pi,Pj)=Ext^(2−r)(Pj,P_(i+1))*。Homは単位行列、Ext2は交換行列、Ext1は四成分全て同じ整数n>=0、Eulerは全成分1−n、高次Ext0。原稿cor:h3-order2-cycle-ext。この必要条件だけでn1や局所H3十分性を主張しない。verify_cubic_order2_boundary_cycle.pyは忠実行列p=sE12,v=sE21、中央自由基底det−s4、次数零冪等元、シフト交換と正常三次の商消滅を厳密に照合する。圏同値とSerre/Extは本文構造証明。

先に仮定して全被覆を縮めてはいけない。全係数の形式的近傍又は小次数Koszul計算で必要条件を得て、既知Clifford正例と照合する。

### 正規な共通量子座標を持つ領域のパラメータ

追加仮定：共通平面T=(xy=qyx),q非1の量子座標xが全Bで正規。このときq=-1,f²1を証明。原稿thm:h3-order2-normal-quantum-axis。

正規化theta_xはW上(1,q^-1)、p上a,a²−q、残りv上c v+d x+e y。thetaの単冪対数DはW,pを殺しDv=ell∈W。v²のrank2平方表示にD²を作用させると右辺0、左辺2ell²なのでell0。従ってthetaは半単純でvをWだけ移動しvx=c xvとできる。偶B2基底x²,xy,y²,xv,yv,vyのtheta重み1,q^-1,q^-2,c,cq^-1,cq^-1、p²重み−q,v²重みc²。q非−1ならf|T2固有値−q,−1,−q^-1に1が無いのでp²∉T2。ゆえにv成分の重みからc=-q又は-q²。v²の重み条件とのresultantは(q−1)^6(q+1)^6(q²+1)^4(q²−q+1)^2(q²+q+1)^2*Phi5(q)となり、残るqは原始3,4,5,6乗根のみ。

全八行のsupportは原稿とJSONに固定。位数5/6のc=-qはv²0。位数3/4のc=-qはp²=xL,Lにv係数非零なのでpp²=p²pから新しいpv/vp奇二次関係が出て関係数に反する。位数4のc1はvx=xv,v²∈span(x²,xv)で可換二次式が一次分解。位数5のc=-q²はv²=Axy非零からcvy=yvという独立な追加二次関係が出る。位数3/6のc=-q²はp²∈U2、U=<y,v>がv²係数非零の唯一の非退化二次関係を持つ真正AS2平面となり、yは非正規。p²y=-q^-1 y p²の倍率は±1外なので二元平面補題に反する。

新補題lem:h3-binary-nonnormal-quadratic-normalizer：量子/Jordan AS2で非正規一次元yが非零二次hによりhy=lambda yhと正常化されるならlambda∈{±1}。量子でy=u+v、lambda非1のu³,v³係数でh=Buv、残り二係数からlambda²1。Jordanでy=u、三角係数行列det(1−lambda)^3。verify_cubic_order2_normal_axis.pyがresultant、全八行のcyclotomic完全剰余、二元補題係数を標数零で厳密に照合する。構造帰着と整域排除は本文で証明。

さらにq=-1でもc!=±1はc=±i,v²=Axyから追加二次関係で排除。c1はB/(x)の三次次元>=11が正規一次元商のHilbert次元10に反するため排除：py=epsilon yp,p²=Ay²,v²=Cy²の18列に独立な二つの全係数syzygyを明記し、検証器も定数pivot15と残余一列を再生した。従ってc−1。a1ならmu*theta_xがxのみ符号反転しGを−Gに送るので、Gは奇数個xを含む語の和、正規性でG=xHに因子分解してR整域性に反する。従ってa−1、xは残り三生成元全てと反可換しx²中心となる。正常共通座標が二本あることも不可能（他軸はa1だから）。

次：このx反可換・x²中心領域について全関係を既知Clifford型又は新候補へ還元する。全H3の半単純化や正常化をこの追加仮定付き定理から推論しない。

### 正規共通量子座標領域の三パラメータClifford正常形

追加仮定付きだが、この領域の全H3包絡を三パラメータで被覆：xはp,y,v全てと反可換、py=yp、v²=y²+i x²、p²=a y²+yv+vy+d x²。H3三次はG=[py,v]の一本。原稿thm:h3-order2-normal-axis-clifford-form。

証明の要点：正規一次元商S=B/(x)はchange-of-rings二行TorによりKoszul、HS=(1−t)^−3とReesでAS3。RRZ Lemma1.5（一次資料rrz.txtを再確認）のnormalizerはx b=tau(b)x、この場合tau=theta_xはinvolutionで、muS=(-p,y,v)。最高三次rho=tau0(ppy−pyp+ypp)+Phi(y,v)。Phi二文字cyclic三次は完全対称なので平方関係はyv+vyだけを含む。v->v−F yでv²=E' y²+I x²,E'非零（零なら反可換xとvの非零一次元平方零）。最高tensorの収縮でp²の{y,v}係数B'=delta E'/tau0も非零。尺度でE'=B'=1にする。

Gamma=(active parity,p parity,x parity)、c(g,h)=(-1)^(active_g*p_h+x_g*active_h)でC=B^cに移すとx中央、{p,y}=0,v²=y²+i x²,p²=−a y²−{y,v}−d x²。Y=y²,L={y,v},T={p,v}が中央になることを全関係から証明し、CはZ0=k[x,Y,L,T]上rank8の真正Clifford環。M=[[-aY−L−dx²,0,T/2],[0,Y,L/2],[T/2,L/2,Y+ix²]]。十個の全overlapで自由基底1,p,y,v,py,pv,yv,pyvを確認し、全係数の平坦Hilbert1/(1−t)^4を得る。AS4/domain/H3十分性をこのPBW計算だけで言わない。

Z(C)=Z0+Z0*g、g=pyv−L p/2+T y/2、g²=−detM。detMのYT²係数−1/4なので全パラメータで分数体上非退化、中心はF+Fg。gのpyv係数1と定数係数0から格子との交差でZ0+Z0gへ戻る。Bの全W1はmuG1とthetaG−、次数3からGamma=(1,1,0)に限り、cocycleで中央になる。中心3でその次数はgだけ、Bの[py,v]は2gに対応する。よってW1一本。

net判別三次は4detM|x0=(L+aY)(L−2Y)(L+2Y)−Y T²。Y1の三次判別式16(a²−4)²、無限遠点は常に滑らか、a=±2の二重根は普通node。これはnetの判別曲線の計算であって、boundary THCRとの同一視、H3許容性や全AS4存在証明を代替しない。verify_cubic_order2_normal_axis_clifford.pyで十overlap、volume/平方、全符号cocycle、判別式を全パラメータで厳密に照合する。

既知smooth-boundary Clifford部分とのパラメータ対応を先に厳密確認し、a=±2のnodal判別と無限遠のcharacter点を勝手に除外しない。

### nodal判別a=±2の全値非H3

原稿thm:h3-order2-normal-axis-nodal-exclusion。a=±2を全d,iで排除した。C/(g)へ有限cocycle輸送するとtailsの大域次元は有限群同変化/induction分裂で不変。最高Koszul Gamma次数(1,0,1)のcocycle指標がmuBを相殺するのでCはCY、中央三次商DのSerreは(-1)[2]。

Y=y²の開集合A=(D[Y^-1])0ではr=xy^-1,s=py^-1,b=vy^-1−u/2,u=L/Y。rs=−sr,rb=−br,sb=bs,r²=z,s²=h,b²=F(z,h)=(h−a−dz)²/4−1−iz、u=h−a−dz,T/Y=−2sb。Aは中央k[z,h]上rank8自由。逆のskew Laurent模型x=ry,p=sy,v=(b+u/2)y、yは(r,s,b)->(r,−s,−b)で作用し全六関係/gを復元する。

a=±2ではF(0,0)0。中央(z,h)完備化は特殊fiberがr²=s²=b²0の局所有限代数（radical四乗零）、唯一の単純k。一次関係がなくExt1(k,k)3。対応点x=p0,y1,v−a/2はシフト固定。有限中央orderの点Ext局所大域比較と完備化でExt_Ahat=Ext_qgrD、H3ならExt2self1,高次0。完備局所代数の最小自由解消はrank(1,3,1)となるが、Frac k[[z,h]]上ではAhat次元8、k消滅なのでEuler8(1−3+1)−8が矛盾。非可換Jacobianや奇数Ext1の未証明一般原理には依存しない。verify_cubic_order2_nodal_axis_obstruction.pyで全PBW/逆代入、節点の全係数接空間、特殊fiber四乗零、top符号を厳密に照合する。

a²!=4のClifford swapへの座標対応と許容判定は、正規軸の許容性定理の六関係・判別式恒等式を使う。nodal排除はその被覆外のa=±2を補完する独立な局所証明である。

### 正規共通量子座標領域の完全H3判定・全矢

この追加仮定付き領域の全H3対象は、正常形xp/xy/xv反可換,py=yp,v²=y²+i x²,p²=a y²+{y,v}+d x²、G=[py,v]、U={(a²−4)di(d²−adi+i²)!=0}で被覆される。原稿thm:h3-order2-normal-axis-complete-admissibility。全H3被覆ではなく、正規共通量子座標を持つ領域の完全必要十分条件である。

明示Clifford cover：k=h³,r²=k+1、a=(k²+20k−8)/(4r³)、d=h(k−8)[b(k−2)−3ch]/(4r³)、i=h(k−8)(2b−ch)/(4r²)。p_old=R*p,R²=16r³/[h²(k−8)²]、U_old=4r*v/[h(k−8)]+2(k−2)y/[h(k−8)]、X_old=(U_old+p_old)/2,Y_old=(U_old−p_old)/2,Z_old=y−hU_old/2,t=x。既知Clifford swap六関係に完全代入し零を検証。a²−4=k(k−8)³/[16(k+1)³]、a²!=4の全点でquartic coverの根はk0,8,−1を避け、b,c->d,i行列は可逆。従って既存thm:normal-order2-clifford-cutsの仮定h非0,h³非−1,8を漏れなく満たす。

中央cocycleも保つ座標変換なのでcharacter CIはpy0,p²+a y²+2yv+d x²0,v²−y²−i x²0へ移る。di0はJacobian退化。di非0ではy0枝が4点、p0枝はy1でa+2u+dz²0,u²−1−iz²0。消去二次Q=du²+2iu+ai−dの判別式4(d²−adi+i²)、z0はa²4だけ。よってreduced iffdi(d²−adi+i²)非0。既存四次判別との直接式di(d²−adi+i²)=−h6(k−8)6*Delta_h(b,c)/(1024r13)も検証し、適用範囲を二重確認した。これは可換character CIのJacobian計算であって一般NC Jacobian原理ではない。

全矢：共通次数スカラーを除き(lambda,zeta)∈Gm×mu4が(a,d,i)->(zeta²a,zeta²lambda²d,lambda²i)で作用。生成元x->lambda x',p->zeta p',y->y',v->zeta²v'。mu正直線p、共通W、fの異なる固有直線x/y、theta_xの固有空間から全矢は対角＋vへのy平行移動に限る。v²の独立な{y,v}係数が移動を零にし、平方比較で全矢が尽くされる。di非0により全点でlambda²=zeta²1、一様慣性mu2²（従来genericの主張をこの正常形で強化）。原稿thm:h3-order2-normal-axis-full-arrows。

粗空間はrho=ai/d,sigma=(d/i)²、sigma非0,(rho²sigma−4)(1+(1−rho)sigma)非0という滑らかな既約2次元開曲面。表示族のrigidified stack[U/(Gm×mu4)]はこの粗空間上mu2²-gerbe。中立とは主張しない。単位minorと符号固有直和により全係数矢は非被約底にも適合し、表示族の許容主開条件・fpqc降下を得る。

verify_cubic_order2_normal_axis_admissibility.pyは六元関係、cover、正規化行列det、旧新四次判別式、全character消去、矢共変式と粗座標を標数零で独立に照合する。H3十分性は既存Clifford定理への厳密還元、nodal全排除は局所構造証明、全矢は本文の自然性/係数比較に依存する。

正規座標存在を一般に仮定してはいけない。量子q−1以外の非正規cross、可換/Jordan共通平面をまず区別し、Clifford以外のH3候補又は排除を得る。

### (1,3)全域の共通平面はq=-1、負三平方は中心

追加の正規座標仮定なしで、共通平面T=(uw=-wu)、pの作用は両軸に逆符号、u²,w²,v²全て中心と証明した。原稿lem:h3-order2-global-cross-formsとthm:h3-order2-global-minus-one-plane。可換/Jordan共通平面も同じ定理で全域排除される。

最高tensorのA4部分はcyclic、偶flattening Hは対称rank4。pp行q0(W)、p²vW/p²v²成分零。外側四乗c=w_vvvv非零ならv平行移動でv³W0とし、cross行は平方kernelのq0/cross一本に入るのでcrossblockは非零rank1。cyclic両対角block一致からcrossはvell−lambda ellv,q0補正、lambda±1、vvW²はrank1 ell²となりv²=cprime ell²。

四乗零ならv³W非零（零ならvv行pp行が比例し二平方投影rank2に反する）。vv行のcrossはn(vell+ellv)。pp/q0座標の対称Schur補完後rank2、crossblock不変、vv対角0のままなのでHcross=rk^t+kr^t,r=(ell,ell)。cyclic両対角一致からk_left=k_right。vvW²はell*s+s*ell、W平行移動でcrossを{v,ell}=0とし全v²W²成分を零にする。vell行からv²∈T2も得る。ここでcrossblockを最初からrank1と誤って仮定しないこと：四乗零の場合はrank2まであり、Schur/cyclicによる平行移動が必要。

二元centralizer：量子q非±1の任意ellとJordan任意ellでT2 centralizer=k ell²。反可換二次は量子q±iのell座標軸で他軸平方の倍数だけ。q−1では任意ellのcentralizer=span(u²,w²)、反可換部分k uw。可換反可換0。これらは三係数の直接計算。

四乗零：v²commellなので非±1量子/Jordanはv²∝ell²となり非零一次式平方零。可換ではf²−I,detf−1からfscalar±i、ell全B正規の重みW1,v−,p±iにGの反可換固有値−が現れずW1零。四乗非零：lambda−ならq2commell、非±1/Jordanではq2∝ell²をv平行移動して同じ平方零。可換ではell²正規、pだけ反転する正常化にmu固定三次（p奇数個）の固定元がなくW1零。lambda+ならq2antiell、q2零は可換v/ellと平方比例で一次因子化。量子q±i例外は[v,x]=t y²,v²=c x²からv y²=-y²v、Y=y²の正規化(x,y,v,p)=(-x,y,-v,-q p)にmu固定三次の固有値1が無くW1零。q−1ではq2=tuwがvとも反可換、pとも反可換し、全4生成元を反転する正規二次q2とGの可換性が次数3に反する。従って全域でq−1、lambda−だけ残る。

負平方中心性：四乗零ならv²とell²がcentral T2に入り独立（比例なら平方零）、vは両者と可換するのでu²,w²とも可換。四乗非零ならq2とell²が独立（比例ならv移動で平方零）、vはq2とell²に可換。pはaxes squares固定なので全Bでu²,w²,v²中心。verify_cubic_order2_global_common_plane.pyはcyclicブロック、量子/Jordan centralizerと正規化符号を厳密に照合する。Schur帰着と整域/正常G排除は本文の構造証明。

平方投影rank2の二chart：A)四乗零,{v,ell}=0,v²=h(u²,w²)、hとell²独立。ellが量子軸の場合と、両軸成分が非零の場合を分けて扱う。B)四乗非零,v²=c ell²,{v,ell}=q2(u²,w²)、q2とell²独立。

### 全(1,3)でp²と負反交換子も中心

原稿thm:h3-order2-positive-square-central。全(1,3)H3でp²,u²,w²,v²,{u,v},{w,v}が中心と証明。pu=-up,pw=wpとしてP=p²,X=u²,Y=w²は一次独立、負反交換子L1(P,X,Y),L2(P,X,Y)、v²=H(X,Y)という六関係・八係数の必要表示へ還元した。L1/L2のP係数は同時には零でない。この中心性の補題は必要表示を与える。全係数のAS4判定・Clifford埋込み・H3許容性には八係数模型とconic bundleの定理を併用する。

負三生成元の三関係だけの抽象S0を取る。独立二中心平方の議論は線型係数行列の可逆性だけでS0内でも通り、X,Y,v²中心。A={u,v},D={w,v}はそれぞれu/vとw/vに可換、[A,w]=[u,D]。crossのalpha A+beta D=q(X,Y)中心、alpha/beta少なくとも一方非零から両A,D中心となる。一方を自由Kとして他方を解けばS0はk[X,Y,K]上真正Clifford3、PBW rank8、HS(1−t)^−3。

B3のmu trace−2、dim20から負固有成分dim11。この成分はS0_3とpvp一本で張られる（p²をS0へ、pWpをf(W)p²へ移す）。S0_3dim10なので三次単射性が従う。p²=h2∈S0_2はTをcentralizeするため、同じ三次比較がS0でも成り立つ。S0 Clifford行列のK²係数−(X*dK²+Y*aK²)/4非零、genericで非退化。Cl2(u,w)は中心単純なのでCl3内centralizerは全体の二次元中心に等しい。よってh2はS0中心、次数2中心はspan(X,Y,K)。従ってp²=aX+bY+cK、特にvとも可換。

c0ならr1=pu+up,r2=pw−wp,r3=uw+wu,q=p²−a u²−b w²の間にmu正の独立二syzygyがある：r1w−u r2−p r3−r3p+w r1+r2u0、qp−pq−a(r1u−u r1)−b(r2w+w r2)0。AS4第三Koszul空間のmu正部分はFrobenius双対でdim1なので矛盾。ゆえにc非零、K=(p²−aX−bY)/cも全B中心となる。verify_cubic_order2_positive_square.pyがtrace/dim、generic Clifford determinant、両syzygy/独立unit minor/符号、交差交換子恒等式を厳密に照合する。generic centralizerと三次単射性は本文構造証明。

### 全八係数商の中心scrollとPchart

原稿thm:h3-order2-eight-scroll-order。包絡で[pw,v]=-G,[T,w]=2G、J=pwとTはRで中心。J²=PY,YT−B0J=Gw,JT−B0P=Gp。d=e0ならG=(T−fpw)wが因子化しR非整域、H3を排除。その他は中心候補C=k[P,X,Y,J,T]/三minorが正規dim3、e!=0ならB0を座標にしてcubic scroll S(1,2)、e0,d!=0ならT'=(T−fJ)/dでC=k[X] tensor k[s³,s²t,st²,t³]。ProjCはF1又はtwisted cubic cone、後者頂点完備中心k[[s,t]]^mu3(1,1)。

全反交換子と平方がCに入りRは有限、RのGK3によりCの追加核なし。R整域ならR2 torsion-free C、PchartgenericcentreがFracCなので全中心はC（有限代数の中央元は整、C正規）。evenRはgeneric rank4quaternion division order、qgrRは中心曲面上coherent order加群圏。この中心計算と、conic bundleによる局所大域次元の判定を区別する。

Pchart S=k[kappa,t,z]/(kappa*t−d−e z−f kappa²)、kappa=J/P,t=T/P,z=X/P。r=u p^-1,s=v p^-1−t/2、r²−z,s²=t²/4−g z−h kappa²,{r,s}=−(a+bz+c kappa²)というrank4Clifford。逆模型u=rp,w=kappa p,v=(s+t/2)p、pはr/s反転、中心固定。e!=0でS=A²_(kappa,t)、e0,d!=0でS=Gm_kappa×A1_z。形式行列det四倍=4z(gz+h kappa²)−z t²−(a+bz+c kappa²)²。e!=0でt³係数−kappa/e、e0d!=0でz kappa^-2係数−d²なのでgeneric非退化、chart全中心も正確S。verify_cubic_order2_scroll_order.pyで包絡恒等式、factor障害、逆chart全関係、detと錐parametrizationを厳密に照合する。

### 錐中心e=0の全値排除、全(1,3)H3はF1上order

原稿thm:h3-order2-eight-cone-exclusion。d=e0はfactor既排除。e0,d!=0の錐頂点Xunitで正確なchartを作り全値非H3と証明。S=p u^-1,W=w u^-1,Z=v u^-1−alpha/2、中央pi=P/X,gamma=Y/X,j=J/X,tau=T/X、alpha=a*pi+b+c*gamma,beta=d*pi+f*gamma,H=g+h*gamma。S²−pi,W²−gamma,SW=WS=−j,{S,Z}=−tau,{W,Z}=−beta,Z²=alpha²/4−H、tau W=beta S。三変数Clifford環をSW+j,tau W−beta Sで割り、uがS/W/Zを全部反転するskew Laurent拡大で元の全六関係/Gを復元するのでexact表示。

頂点fiberはS²=W²=SW=WS0,{S,Z}={W,Z}0,Z²=b²/4−g。二根q!=0ではZ±qの二単純をshiftが交換。一次拡大は七変数（S/W/Zと四中央座標）で正確に計算：pi/gamma/jの一次成分零,tau=−(zi+zj)s,(zi+zj)w=(zi+zj)z0。自己はsだけ自由、crossはs/w/z自由からinner1を引くためExt1行列[[1,2],[2,1]]。H3 Serre(-1)[2]はshift交換二点の四成分を同次元にするので矛盾。これらの点加群はu作用1、v作用b/2±qを交互に取り、定数文字とはしない。

重根では唯一の単純k、fiber radical三乗零、Ext1self3、shift固定。H3ならExt2self1高次0で完備局所代数の最小自由解消rank(1,3,1)。中心完備k[[s,t]]^mu3(1,1)はdomain、generic order dim4でEuler4(1−3+1)−4が矛盾。従って全e0排除、全H3(1,3)でe!=0かつ中心F1。verify_cubic_order2_cone_obstruction.pyはinverse Clifford chart、七変数一次extension全系をqだけの単元pivotで全係数消去し自己1/cross2/重根3とradical冪零性を独立に照合する。局所大域比較とSerre/Eulerは本文構造証明。

### F1上の大域Clifford束とplane quartic

原稿thm:h3-order2-global-conic-bundle,prop:h3-order2-plane-quartic,cor:h3-order2-conic-recognition。全AS4/eunit候補でR even/odd sheafをrank3二次形式のC0/C1にexact同定した。scroll標準座標Y=lambda s²,J=lambda st,P=lambda t²,B0=mu s,T=mu t、kernel線O(-F)は(-s,0,t,0)、quotient V=O(F)+O+O、q値L=O(E+2F)。q matrix[[lambda,0,mu/2],[0,X,A/2],[mu/2,A/2,H]]、X=(mu s−lambda(d t²+f s²))/e,A=a lambda t²+bX+c lambda s²,H=gX+h lambda s²。M4 kernel三列がRの実際のlinear関係でもあり、逆Clifford表示で全rels/Gを復元するためsheaf同定はgenericのみに留まらない。C0=O+O(-E-F)^2+O(-E-2F),C1=V+Lambda3(V)L^-1、両者locally free rank4。lambda/mu非同時零でqrank0は全候補で起こらずconic bundle flat。

Z4=k[P,X,Y,D]上Bfree32、0B(-3)-G->B->R0はZ4自由解消、F=G²=B0²P−DYがRを殺しpd1/depth3。Z4+とC+のradicalは同じなので偶/奇のlocalcohom0,1,2も消え、両部分はClifford sheafのsection moduleで飽和。局所自由＋飽和でC-torsion-free、全候補でZ(R2)=Cまでdomain仮定なしに拡張。Rdomain iffgeneric quaternion division（P正則とexact skew Laurent chart）。構造対象のExtはH^i(C0)、負二線束はacyclicなので全候補で例外的。rank-one iffdivision、全完備局所order gl2ならASGor duality(-1)[2]が全Dbに延び、AZ/Serre/heart/Hilbert/AS4/飽和/torsion-freeと合わせH3全条件を得る。従って残る必要十分条件はdivisionとlocalgl2。

plane blowdown x=lambda s,y=lambda t,z=mu。Q=xz−dy²−fx²,U=ea y²+bQ+ec x²,V=gQ+eh x²、F4=4QV−U²−eQ z²。F4pullback=4e²lambda detq、判別類3E+4F、Eとの交点1。o=[0:0:1]はpartial_x F4=-eで常にsmooth。rank1 fibreはo外でQ=U=4V−ez²0。E(lambda0)ではdetq=−mu³s/(4e)、s0一点のみrank2単純判別、他Azumayaなので全E近傍gl2。Qのx/z minor−1/4、従ってQは決してdouble lineでない。verify_cubic_order2_conic_bundle.pyでkernel/quotientmatrix、quartic、rank1/例外曲線・conic非二重線を全係数厳密に照合する。CM/飽和/圏認識は本文構造証明。

rank3 conic bundleの総空間の滑らかさと、F4が被約nodalで全nodeがrank1 fibreである条件の同値、およびgeneric quaternionのdivision性は `thm:h3-order2-complete-conic-admissibility` の証明を用いる。局所global dimensionとgeneric rankを別々に確認してからH3認識を適用する。

### 正三次元bi-normal明示AS4族の全切断排除

新たに(3,1)の明示bi-normal族 px=xp,xy=yx,py=-yp,zx=-xz,zy=-yz,z²=ap²+bx²+cy²を全係数で排除した。a非零ではClifford--Ore基底と中央自由階数32、二次双対の正規/中央正則列によりnoetherian Koszul AS4、実際mu=(+,+,+,-)。全正常三次はW1=x*span(p²,x²,y²)で全て因子化し非H3。a零では双対の無限次元商によりKoszul AS4外。これは(3,1)全被覆ではない。

原稿prop:h3-positive3-binormal-exclusion。P=p²,X=x²,Y=y²はaunitで全て中央、T=pz+zpはp/y/zと可換xと反可換。Cl3(p,y,z) over k[P,X,Y,T]、p/yとy/z反交換、{p,z}=T、z²=aP+bX+cY。xはp/y固定,z/T反転、x²XのOre商。全関係から逆模型を復元できPBW16、中央k[P,X,Y,T²]上free32、HB=(1-t)^-4。双対QはPX/XYだけanti、他comm、E=Q/(PZ,P²+aZ²,X²+bZ²,Y²+cZ²)。EbarのP0/Z0 fibreproductで中央三二次式正則列、前向きPP KoszulとASGor FrobeniusよりAS4。nuQ=(-,+,-,+)、tauPZ=(+,-,+,+)でnuE=(-,-,-,+)、muB=(+,+,+,-)。固定三次11基底P/X/Y times p/x/y plusTz,pyx。Gy=yGでp型/Tz/pyx五係数消去、Gp=pGでy型三係数消去、残りxP,xX,xY全て正常三次。常にxでfactorしR非整域。a0双対P0商はk[Z]自由rank4無限次元、Koszul AS4外。verify_cubic_positive3_binormal.py/certificateでClifford全overlap/自動同型、双対直交、十一列系constantpivot8を厳密に照合する。文献新規性未確認。

正三次元の次案：mu半単純、共通平面作用f=diag(q,q^-1)なら偶flatteningはWW/vW/Wv/vv/zzの10x10対称行列。混合graph条件を線型に課すと普遍四次tensorは23係数（正三元反巡回21、z²W²一本、z4一本）。zz行はq^-2 xy−yx+gamma z²。rank偶4のSchur制約と整域性を使って三次正常核を絞る。

### 双対一次切断の普遍Hilbert値とAS3還元開部分

一次元/三次元分解の全common-plane領域（単冪も保持）でE=B!の一次元側双対zetaは正規、zeta E1=E1 zeta dim3、階数列1,3,3,1。F=E/(zeta)は常にHilbert(1,3,3,1)、Ann(zeta)は(0,1,3,3,1)。F Frobenius iff Ann(zeta)=E xi=xi E、xiは共通平面の直交補線。この開部分ではAnn(xi)=(zeta)、二周期線型E解消とchange-of-ringsでF Koszul、F! AS3かつTor edge全射の双対によりF!->B単射。二つの3x3対合行列式で開条件を判定する。

原稿prop:h3-order2-dual-hyperplane。mixedgraph二関係より双対zetaの左右積U*像は同じodd2、核は同じxi=Wperp。top zz行q0非退化からzeta²非零、Lzeta:E1->E2 rank3。Frobenius双対で残る階数1,3,1が決まりF Hilbert(1,3,3,1)、annHilbert(0,1,3,3,1)。両側イデアル(zeta)はnuで不変、trace直交により左右ann一致。annはFの双対の捩れ/移動なのでF Frob iff annが左右xi一元生成。両者dim8から逆ann(xi)=(zeta)。E(-q)をzeta/xi交互乗法する線型解消ができ、TorE(F,k)内部q集中。change-of-ringsでF非Koszulの最初のTorF_p,j>pはq0から入る微分なく、出る先内部p-1で消えずKoszulEに矛盾。ゆえF Koszul、F! AS3。さらに全E2項内部p+qで全微分零、TorE(k,k)->TorF(k,k) edge全射。双対ExtF->ExtEの単射が自然F!->Bなので、実際にAS3部分代数が埋まる。この双対超平面補題はFrobenius条件の非消滅を仮定するため、その退化域に直接適用してはいけない。verify_cubic_order2_dual_hyperplane.py/certificateは全係数bi-normal E16模型でFrob対合、階数列、相互ann、F対合を厳密に照合する。Frobenius条件は両方向F1/F2の3x3行列式非零で、退化域を黙って除外しない。

### 正三次元側の商体退化排除

正三次元(3,1)側でも、gamma0で共通TがAS2平面の場合、残る正生成元vと負生成元z²が同時に斉次商体Qgr(T)へ入ることを排除した。可換/有限量子は固定中央体上有限次元でGK<=2、無限量子はhxyが非零次数4中心元となり矛盾、Jordanはh=cy²と(z/y)²=ac∈kから代数閉体上整域性によりz∈kyとなり矛盾。単冪も保持するがgamma非零には適用しない。先頭環での正常三次の因子化を変形後の因子化と混同しない。対角chartの変形全体には `thm:h3-positive3-diagonal-full-exclusion` を用いる。

原稿lem:h3-positive3-rational-collapse。f det=hdet1、muT=muW f²。量子q!=1ではmuWの固有値1のみなのでid、q−1反対角fはdet/hdet逆符号で除外、fdiag(a,a^-1),a²q。q無限位数のhomogeneouscentral r(u)y^mはycommからr(q^-1u)=r(u)、零極議論とq無限位数からr定数、xcommからm0。h=z²inner f²=muT=Ad_(xy)^-1ゆえhxy中央degree4矛盾。有限q/可換ではf有限、Q(T)はtrdeg2中央固定体F上有限、B subset D+DzもF有限、有限構造定数からGK<=2。Jordan yx=xy+y²、f(y)=a y,a²1なのでhcommy、h=r(x/y)y²のr周期は定数c、(zy^-1)²=ac、代数閉体上の整域で代数的元はscalarゆえz∈ky矛盾。verify_cubic_positive3_rational_collapse.py/certificateで量子muとf²、q−1反対角符号、Jordan/局所平方恒等式を厳密に照合する。合理関数とGK論証は本文。

### 正三次元対角chartの共鳴と非共鳴変形の全排除

(3,1)半単純対角normalizing chartの全先頭AS4族 xy=a²yx,zx=axz,zy=a^-1yz,vx=axv,vy=-a^-1yv,v²=z²の正常三次を完全計算：a³!=-1ならW1=0、a³=-1かつa!=-1ならky³、a=-1ならy*span(x²,y²,v²)。全先頭切断は因子化。重みW1/outer2の先頭環比較により、dx(W),dy(W),ell(W)v+q2(W)を任意に加えた14641/指定muの全変形もa³!=-1ではW1=0で排除。

原稿thm:h3-positive3-diagonal-top。r=v+z,s=v−zでA=quantumplane−1、B0=A[x;sigma_x][y;sigma_y]、sigma_x(r/s)=a^-1(r/s)、sigma_y(r,s,x)=(-a s,-a r,a^-2 x)。noeth/PBW/domain/KoszulAS4。muA−、第一mu=(-a r,-a s,a^-2 x)、第二でr/s交換,x/y固定となり実際mu=(x,y,v,-z)。mu固定outerdegree0/1/2/3次元1/1/1/2で全三次11。W次数i/j、outer nなら正常化Gx=xG,Gy=yGはa^(n−2j)=1,(-1)^n a^(2i−n)=1。n1/n3は全gcd1で零、残るn0/2単項式はGv/Gzから(-1)^j a^(i−j)=1,a^(i−j)=-1、ゆえjodd。y³のgcd a³+1、x²y/yv²のgcd a+1、他gcd1。元来のgradeddegree固定で重み先頭環への全射とHS比較によりgrB=B0、正常Gの先頭もW1B0なので非共鳴変形全排除。共鳴先頭因子を変形後factorとしない。verify_cubic_positive3_diagonal_top.py/certificateでOre生成元三重積/六関係/固定11次元/全Laurentgcd/候補正常化を厳密に照合する。

### 正三次元対角normalizing chartの共鳴も全排除

正三次元(3,1)の指定対角normalizing chartを全係数・全aで排除した。非共鳴は先頭核零。a=-1は内部移動後vx=-xv+kappa*y²,vy=yv、商体退化排除からell0、x²/y²/v²中央、y正常mu、先頭核次元上界3と三独立候補でW1=y*span(x²,y²,v²)全てfactor。primitive6では全skew導分内部、ell/q2比較で全補正零、W1=ky³。AS4存在を任意補正係数へ主張しない。

原稿thm:h3-positive3-diagonal-full-exclusion。g-skew導分条件はa(1−a)e0=(1+a)d2=0、(1+a^-3)d0+(a−1)e1=0、(1+a^-1)d1+(a−a^-2)e2=0。内部二列(d0,e1)=(1−a,1+a^-3),(d1,e2)=(a^-2−a,1+a^-1)。a−1では導分核3/内部2で残りdx=kappa y²,dy0。v²/z²commxとqWcommxからell[v,x]0、ell非零ならv∈Q(T)かつz²も入るので新商体lemma矛盾。ell0でqWはz反転に不変、v²commz、x²/y²/v²中央。yはmu正常なので三次候補三本、先頭kernel3次元で全核。primitive6は導分核2=内部2。delta0の後、外平方x比較で(a−a²)ellx=(a^-1−a²)elly0、T+Tv独立は商体lemmaによるのでell0。qWnormalization f²はx比較ky²,y比較kx²を強制しqW0。verify_cubic_positive3_diagonal_resonance.pyは全導分式と内部、Phi6上非消滅/gcd、a−1正規形の中心二次全交換子を次数3イデアルのparameter-free pivotsで恒等式として検証する。全chart外を被覆とはしない。

### 正三次元の全normalizing chart排除と二平方商

正三次元(3,1)gamma0で全normalizing chartを単冪込みで排除した。PBW整列/14641比較からg∈Aut(T),g²=f²。g±fは先頭mu重複度2+2で除外、他は対角全排除またはq−1四元数反対角。後者の先頭140x20正常化行列にdet=-128+128iの固定20minorがあり、全補正でもW1=0。対角でmuW=idの非分裂extensionはDv=wからg(w)=w,2wv+d(w)=ell*w⇒v∈Q(T)で排除。従ってgamma0全H3候補はB/(W)=k<z,v>/(z²,v²)かつ中山extension分裂。残るJordan型は半単純またはW上Jordan2＋自明1。

原稿lem:h3-positive3-quaternion-chart,thm:h3-positive3-full-normalizing-chart,cor:h3-positive3-two-square-quotient。fの非自明Jordanならg²=f²の平方根は±f、fscalar±IのJordan平面でもg±f、これらは二段Ore先頭mu外側(-,-)で元の(+,-)と矛盾。g−fの場合の外側交換Zhangtwistはhdet1でmu不変。可換fscalarの反射gと量子fdiag(a,a^-1)のgdiag(a,-a^-1)は全対角排除、q−1の反対角g²−Iは尺度でvx=yv,vy=-xv,zx=i xz,zy=-i yz。r=v+z,s=v−z PBW全overlap一致、140x20正常化matrix固定20minor=-128+128i、全低重み補正除外。verify_cubic_positive3_antidiagonal.py/certificate厳密。対角残りWµidではDv=w∈W、cross微分wt=g(t)w、t=wでg(w)=w、平方微分2wv+d(w)=ellw、v/h商体落ち矛盾でmu全体半単純。全normalizingchart空よりgamma0の一平方投影rank1はcross可逆なら全chart排除、退化なら商体lemmaで排除、rank0/一片平方は指数増大商。rank2だけ残り二平方商。非分裂Jordantensorの既存18恒等式を符号に依存せず適用するとzz/vv二列比例で平方像rank<=1となりrank2と矛盾、よってextension分裂。全(3,1)被覆/排除としない。

### 正三次元半単純gamma0の全cross標準形と二平面制限

(3,1)gamma0かつmu半単純で、正三元anti-cyclic topとrank4 SchurからvをW移動し[v,ell]=0,v²∈T2を全域で導いた。v4=0、v3W非零、vvrowcross=(ell,-ell)、Schur Hcross=rk^t+kr^tの二対角block逆符号でkleft=kright、三v orbitの移動でcross全消去。Tは可換かq=-1に限る。他の量子/JordanではcentralizerT2(ell)=kell²ゆえcommuting平方factorで整域性矛盾。可換f±Iならellはcentral又はmu正常一次、q−1 fdiag(i,-i)ならell²はmu正常二次、v²とell²独立で両軸平方もmu正常。

原稿thm:h3-positive3-global-cross。n(vell−ellv)をvvrowcrossとし、zz/q0coordの2x2blockでSchur。zz-cross0かつinverseqq0なのでcross-cross/vv-cross/vvdiagは変わらず残りrank2。r=(ell,-ell)からHcross=rk+kr、anti-cyclicでBRR=-BLL⇒k=(s,s)。crossC=ell s^t−s ell^t、vvWW=-C。vold=vnew−s/nによりvvv ell orbit(n,-n,n,-n)からAshift=-n(ell t+t ell),Cshift=-n(ell t−t ell),vvWWshift=+n(ell t−t ell)、全消去。[v,ell]0、crossrowからv²∈T2。量子q!=+-1/Jordan centralizer一次元で平方factor、可換又はq−1だけ残る。q−1 ell²/v²独立から両軸平方を線型復元してvcomm、zは両平方反転するのでmu正常二次。verify_cubic_positive3_global_cross.py/certificateでblock/三v項の実際の基底変更/centralizers/平方重み全係数厳密。

### 正三次元可換共通平面の全排除

(3,1)gamma0かつmu半単純で可換共通平面も全排除。正常ell=uと補元tに対しv²=Au²+But+Ct²、C0は平方factor又は余分な[v,t]二次関係で矛盾、Cunitからv²=t²+Iu²へ正規化。B/uは正規一次商の線型Tor議論でKoszul AS3、muC=(t,v,-epsilon*z)。三次topから全商はv²=t²,zt=epsilon*tz,z²=alpha*(tv+vt)+beta*t²,alphaunitに限る。z尺度でalpha1。両epsilon±、全betaで45x10正常化行列に定数pivot10があり、誘導muB=(t,v,-z)正常三次は零。ゆえ元Gはuでfactorし非H3。残る半単純gamma0全候補はT=q−1,fdiag(i,-i)、[v,ell]0,v²∈span(x²,y²)でell²と独立。両軸平方がmu正常。

原稿thm:h3-positive3-commutative-plane-exclusion。C=hのt²係数が0でut係数非零なら[v,v²]=Bu[v,t]0、整域性で[v,t]0となるがR_evenは[u,t],[u,v],v²-hと非零z²係数の一本しかなく余分なpurepositivequadを許さない。u正常regularlinearなのでC3=B/uは0B(-1)->B->C3とTor leastoffdiagでKoszul、HS3、ASGor/FrobからAS3。偶関係dim2/odd1とpositive一次dim2によりtopの元muB反転指標は+（奇なら二positive縮約がodd1へ入りrank欠損）。topz²v0はuniqueoddzt関係から。positivecyclicbinarytopのv縮約はBm²+C(mv+vm)+Dv²、purepositivequad v²-t²一本なのでC0,B=-D,Dunit。t縮約でz²=alpha{t,v}+beta t²,alphaunit。全beta両epsilonの次数3/4商を元の三関係からconstantpivotで10/15基底、正常muB(t,v,z)=(t,v,-z)行列45x10 constantpivot10で全kernel0。verify_cubic_positive3_commutative_plane.py/certificateはsampleではなく全係数恒等式。muCはepsilonで異なるので、この核をmuC自身のW1と混同しない。GimageC0ゆえG=uQ factor。

### 正三次元半単純gamma0の量子平面も全排除

正三次元半単純gamma0の残るq−1部分も全排除した。ell軸/非軸でv²をgx²+y²又はgx²+(g−1)y²に正規化。positive Sの明示三次topの両flattenrank3でF=E/(z*)がFrob、双対超平面補題からS AS3がBへ埋まる。z²はS2でW反転するため二次反交換子核がspan(xy,[y,v])に限り、z²=Axy+B[y,v]。B0は全係数でdegree3dim21、Bunitを1へ尺度変更すると両二parameterchart全係数のdegree3/4商20/35、正常三次140x20は定数pivot20でkernel0。AS4存在を任意係数へ主張せず、必要候補被覆と正常核零だけで全H3排除。

原稿thm:h3-positive3-semisimple-gamma-zero-exclusion。軸hunitでh1、非軸g−hunitでh=g−1。F Hilbert(1,3,3,1)は普遍lemma。positive Sの明示top：軸はvvx−vxv+xvv−gxxx−(xyy+yxy+yyx)。非軸u=x+y,m=x−yはm²=u²,[v,u]0,v²=alpha{u,m}+beta u²,alpha1/4,beta g−1/2、top alpha m³−alpha(uum+umu+muu)−beta u³+vvu−vuv+uvv。両flattenrank3でFrob、S AS3実埋込み、muSはW固定v反転でCYとしない。S2 antiW kernelは両chart次元2、xy/[y,v]が基底。z²=Axy+B[y,v]、B0はR3 constantpivot43でdim21だから不可、Bunit zscaleで1。R3/R4 constantpivot44/221、正常系constantpivot20で全param核零。verify_cubic_positive3_quantum_plane.py/certificateが全商射影・S top/反交換子核・正常kernelを元の関係から厳密に照合する。

### 正三次元gamma0のJordanも排除、領域全体が空

正三次元(3,1)gamma0領域を単冪込みで全排除。残るW Jordan2＋自明vではDy=x,Dv0、top v³x非零からvx=xv+d x²、x正常一次。偶B2D核はspan(x²,xv,vy−yv−dxy)。正常一次商C=B/xはKoszul AS3でmuC=(y,v,-epsilon z)、v²=c[v,y],zy=epsilon yz。三次topのpositive二元cyclic縮約が対称なのでc0、top正部分はAv³+By³だけ、残るz²=t y²。Cは二generator quadconeとv²0の自由積でHC=(1+s)/(1−2s)、degree3dim12とAS3値10が矛盾。全t/両epsilonの定数pivot15でdim12を厳密再生。従って(3,1)H3があるなら必ずgamma非零。

原稿thm:h3-positive3-gamma-zero-exclusion。中山extensionは分裂、残りWJordanだけ。common f上三角epsilon²1、T yx=xy+kappa x²（kappa0可）。Dtop不変でv³y0、purev4はanti巡回0、二平方projectionrank2からvvrow/z²row独立なのでv³x!=0。v/x巡回からvvrowcross [v,x]、WWのD核x²よりvx=xv+d x²。x正規でB/xの線型Tor/Koszulとnormal ASGorでAS3、HS3、muC反転z符号−epsilon。B2even6基底x²,xy,y²,xv,yv,vyのDkernel3はx²,xv,vy−yv−dxy、ゆえmodx v²=ccomm。C oddR1/positiveV2でtopは元z反転偶、oddgraphzyがz²vを禁じ、purepositivebinarycyclicv縮約の対称性からc0。クロスcubiccoeff0でtop正二元部分v³/y³だけ、C三関係v²0,zy=epsilon yz,z²=t y²。自由積HS指数、又はdegree3原関係matrix定数pivot15/27でdim12、AS3dim10矛盾。verify_cubic_positive3_Jordan_obstruction.py/certificateでD核・対称縮約・両符号全tのdim12厳密。

q0(W)+gamma*z²関係のためWにAS2平面分類を直接適用しない。mu半単純fdiag(a,a^-1)ならS(W,z)はxy−a²yx+gamma z²,zx=a xz,zy=a^-1 yzの三generator AS3型、q0非零正常二次。補positivevを含む偶flattenrank4/平方projection/dual Frob開条件から全正常三次を絞る。

### gamma非零対角基礎の二次AS3と三次CY根拡大

残る(3,1)gamma非零のf対角chartについて抽象基礎S=<x,y,z>/(xy−a²yx+gamma z²,zx−axz,zy−a^-1yz)を構造認識。SはPBW x^i z^j y^k,noeth quadratic Koszul AS3、実際muS=(a x,a^-1 y,z)。T=<x,y>はcubicCY AS3/index4/解消1221、二つのquantumSerre係数a²+a^-2が全関係、C=xy−a²yx=-gamma z²のweightedOre基底x^i C^j y^k。S=T+Tz自由rank2、Cprime=xy−a^-2yxは逆正常化、CCprime中央degree4。H3包絡への自然写像の高次核は未排除、f Jordanchartは未包含。この基礎をAS2と混同しない。

原稿prop:h3-positive3-nonzero-gamma-base。Sの順序x<z<y、zx=a xz,yz=a zy,yx=a^-2xy+gamma a^-2 z²、唯一overlap yzx=xzy+gamma a^-1 z³。三次Koszultop yzx−a zyx−a yxz+a^-1xyz+a^-1zxy−xzy+gamma a^-1z³、巡回は実際muSの逆を使う規約で検証（符号固有値のみの以前の計算では逆と同一）。TはC x=a²xC,y C=a²Cy,yx=a^-2xy−a^-2CのweightedOre、Cweight2、PBW x^i C^j y^kがS内even z基底に単射。C消去でx²y−(a²+a^-2)xyx+yx²,y²x−(a²+a^-2)yxy+xy²。最高syzygy x*r_y+y*r_x=r_y*x+r_x*yはcyclic4、muT=id、ASindex4。Cprime逆normalizerf^-2、CCprimecentral。verify_cubic_positive3_nonzero_gamma_base.py/certificateで両overlap、三次rels、二次top/逆mu巡回、三次CYtop左右syzygyとcyclic、Cprime/中央積、Hilbertrootidentity全係数厳密。既知形の新規性は主張しない。

### gamma非零抽象基礎内の指定正常三次全判定

gamma非零対角chartの抽象基礎Sで、指定正常化sigma(x,y,z)=(x,y,-z)の三次全核を判定した。a²-a+1非零なら核0、aがprimitive6ならspan(x³,y³)。Sdomainよりsigma固定、PBW六候補のz重みがa³=-1を強制、a=-1は六交換子系の定数minor18で除外、primitive6で両cubeをPhi6剰余検証。このsigmaは一般にmuSではない。抽象基礎S内の正常核だけから全(3,1)H3への共鳴条件は従わない。実際、`cor:h3-positive3-base-survives-cut` はGが基礎像の外にあることを示す。

原稿prop:h3-positive3-base-normal-cubics。sigma正常非零GはsigmaG=G、PBW evenz degree3六項。z weight a^(i−k)=-1、指数+-1/+-3からa³=-1。a−1はgamma1へzscale後、commx/yの六列matrix固定rows[3,7,10,12,18,25] minor18でkernel0。primitive6はa+1unitでx³/y³だけがphase許容、両者全正常式をPhi6剰余でzero確認。verify_cubic_positive3_base_normal_cubics.py/certificate厳密。原H3GがSにある/基礎map単射の証明を欠くので全スペクトル共鳴制約へ拡張しない。

### gamma非零対角基礎写像の全パラメータ核二分法

gamma非零f対角基礎Sからgraded domainへの写像（z像非零）の核を全aで完全判定：0又は(Cprime=xy−a^-2yx)のみ。a4=1は必ず単射。z局所degree0はqWeyl wu=q uw+c,q=a^-4,c=gamma a^-3,d=c+(q−1)uw=−a Cprime/z²。q∞はGWA単純性、qrootはd非零開でAzumaya次数N、非零整域商は中心curve上Brauer0/Tsenでsplitし矛盾、ゆえ非零kernelはd0。商はparameter aのquantumtorus、これも完全素非零idealを持たずkernel正確Cprime。S/Cprimeはquantumplane偶Veronesecone、PBWdomainで飽和確認。

原稿lem:h3-qweyl-domain-quotients,thm:h3-positive3-base-kernel-dichotomy。qWeyl dnormalはdu=q ud,dw=q^-1wd。q1は通常Weyl単純。q∞A[d^-1]はD=k[d±],sigma(d)=qd,t=(d−c)/(q−1),X=w,Y=uのGWA、Bavula作者原稿Theorem2.1の適用では4条件sigma-simple/no inner power/coprime all n/t regularを点検、resultant c(q^n−1)/(q−1)²。qrootNではZ(A)=k[uN,wN]、freeN²、dN=cN+(-1)^(N−1)(q−1)^N uNwN。dNunit開全closedfiberはuN!=0ならd相異eigen+巡回u、wN!=0対称、両0ならtruncated oscillatorでM_N、従ってAzumaya。完全素非零商は非零中心idealからtrdeg<=1field上division次数NになるがTsenBr0でM_Nにsplitして矛盾。量子torusも∞単純、rootMはcentreLaurent2上AzumayaMとTsenで非零完全素idealなし。S[z^-1]=A[z±;theta] stronglygraded、kernel非零ならJ=degree0nonzero completeprime、dJ⇒CprimeI。d0商はquantumtorusなので更なるkernelなし、S/CprimeのdomainとzsatでI正確(Cprime)。a4!=1coneはz²=(a4−1)/gamma xy、yx=a²xy,zx=a xz,yz=a zy、x=s²,y=t²,z=lambda st,st=rho ts,rho²a^-1,lambda²=rho(a4−1)/gammaでevenVeronese。

一次資料：Bavula overview local /workspace/work/sources/bavula_gwa_overview.txt のTheorem2.1（GWA defining conventionYX=t,XY=sigma tも確認）。Stacks Project Tag03RD Theorem59.67.10（functionfield over algclosed of dimr isCr）とTag03RF Lemma59.67.11（curve functionfield Br0）を2026-11-16に原ページ確認、キャッシュ /workspace/work/sources/stacks_03RD.html,stacks_03RF.html。原稿にStacksTsenBrauer書誌を追加、Bavula書誌に2.1を追加。Azumaya全rootのmatrixfiber証明は本文で与え既存被覆定理を輸入しない。verify_cubic_positive3_base_kernel.py/certificateは局所/GWA/normalizer/resultant/oscillator recurrenceとcone4overlap/Hilbertを全係数厳密、Tsen/Azumaya全位数は構造証明。

重要な帰結cor:h3-positive3-base-survives-cut：同じSをH3のRdomainへ写す核も0/Cprimeの二択。B2=R2ゆえ二核のquadratic部分一致、両方二次生成なのでkernel完全一致。基礎像はcut後もRに単射、よってGは必ず基礎像の外にある。primitive6の二平面例は全H3の共鳴条件には使わない。これは根拠不明のG基礎所在を仮定する代わりに、実際にその所在を否定する。

### Jordan基礎の単射性と全正三次元canonical基礎被覆

gamma非零の残るJordan基礎S_J(yx=xy+kappa*x²+gamma*z²,zx=epsilon*xz,zy=epsilon*yz+beta*xz)は全係数でPBW/noeth quadraticAS3。z局所degree0は微分Ore A=k[u][v;delta],delta(u)=(kappa+epsilon*beta)u²+epsilon*gamma。deltaを可逆にするとsimple、非零completelyprimeはdeltaの一次因子u−rを含み、元の基礎でx=r zとなるためH3の一次独立性に反する。従ってJordan基礎はB/R両方へ単射。既存全行列標準形と対角kernel二分法を併用し、全(3,1)H3候補のcanonical基礎像を対角AS3/JordanAS3/量子Veroneseconeの三表示で被覆、全てRにも埋まりGは基礎像外。AS3枝では追加positive vと純正二次関係3本、cone枝では2本が残る。

原稿prop:h3-positive3-Jordan-base-injective,thm:h3-positive3-canonical-base-coverage。SJ順序x<z<y、唯一yzx overlap=xzy+(epsilon*kappa−beta)x²z+epsilon*gamma z³。base quantumplane(x,z)上Ore y, sigma(x,z)=(x,epsilon z),delta(x)=kappa x²+gamma z²,delta(z)=−epsilon beta xz。u=x/z,v=y/zで[v,u]=lambda u²+epsilon gamma,lambda=kappa+epsilon beta、z actiontheta(u,v)=(epsilon u,epsilon v+beta u)。inverse x=u z,y=v zで全関係正確復元。微分Oreのf(u)=delta(u)を可逆にしたbasek[u,f^-1]はdifferential-simple、idealの最小v次数とcommuでsimple ring。非零completeprimeがfを含み、lambda0ではA通常Weylsimpleで不可、lambda!=0では一次因子u−rを含む。gradedkernelzlocalのdegree0 J非零⇒x−r z∈I_z⇒zsatでI、一次像独立と矛盾。

全基礎被覆：M1 muWsemiのfdiagは対角S（positive補空間の非分裂Jordanを仮定で除かない）、fJordanはSJ。M2 muWJordanはfscalar含めSJ。両SJ/diagSはquadraticAS3domain、diagのみkernelCprimeのcone像もある。B/R同じ一次・二次より両基礎像保持、Goutsideすべて。gamma非零evenR4のz²射影unitでpurepositivequad3、AS3枝W²kernel0なのでv関係3、coneはWquadCprime一本を消費しv関係2。verify_cubic_positive3_Jordan_base.py/certificateで両epsilon全coeffPBW/局所Ore/逆変換/判別式恒等式厳密。構造被覆を全H3対象分類・全家族降下と混同しない。

### cone枝全排除、全正三次元H3の基礎はAS3に限る

残る(3,1)のcanonical基礎の量子Veronesecone枝も排除。Wはq=a^-2 AS2,a4!=1,z²=kappa xy。vがQgr(W)へ落ちるとBは曲線体k(u)上skewLaurent内に入り、degree-n極因子O(n)でGK<=2矛盾。追加2quadsにv²がなければcross退化はこの矛盾、両cross可逆はW PBW×zzを避ける外側語でdegree3dim21矛盾。v²があればv³W0はvvrowのrank2 Wquadとcrossrank<=1がanti-cyclicで矛盾、非分裂v Jordanも既存D invariantでv³W0を強制し排除。半単純化後、z²relのcross0とv4top0からHcross=rk+kr、v移動で[v,ell]0,v²∈W2。q!=+-1のcentralizerからv²=c ell²因子化しdomain矛盾。従って全(3,1)H3のcanonical基礎は対角/Jordan quadraticAS3としてB/R双方に埋まり、Gはその外。Hilbert比HR/HA0=1+t+t²だけでは有限自由階数3を推論できない。

原稿lem:h3-curve-graded-division-growth,thm:h3-positive3-cone-base-exclusion,cor:h3-positive3-AS3-base-Hilbert。curvegradedfractionはcone zlocal qtorusからk(u)[z±;u->a u]、同次数1有限gen f_i(u)zのlengthn係数極D_n=sum sigma^j D、degreeO(n)でdim BnO(n)ゆえGK2。ConeW量子AS2へのv rationalを全aで排除（旧gamma0 rationallemmaのmuT=f²仮定をここに誤用しない）。v²projection0のcross2双方可逆ならg/skewderivT、z²Tnormalcompatとfxy1で全diamond成立、normalbasisT×words(v,z) avoidingzz、HS=(1+t)/((1-t)²(1-t-t²))のdegree3=21。片側cross退化はv rational矛盾。v²projection1ならcross1両射影非零、vvrow非零。v3W0ならvvrow純Wquad rank2、crossrows squares0なのでcross-crossrank<=1、anti-cycle QvvWW=-Ccrossで矛盾。mu v=v+w非semi補正も3vW0のとき2v tensorに影響なし、D invariant3vW0で非split排除。mu semi後R_evenbasis[rT,z²-kappa xy,rcross,rv²]、crossproj[0,0,r,s]、M44=v4=0、Hcross=M33 rr+M34(rs+sr)=rk+kr。anti-crosstranslationでcommvell,v²T2、AS2q=a^-2!=+-1でcentralizer minor=−(a4−1)² nonzero、平方factordomain矛盾。verify_cubic_positive3_cone_exclusion.py/certはgrowth/block/minor厳密。positive3_global_cross/nonsplit_tensorも当該検証器の照合対象に含む。全基礎像はAS3のみ、RHSratio1+t+t²からmodulefinite/freeを推測で済ませない。

### 正三次元のmonic正規形と商体障害

全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。(3,1)gamma0とcanonical量子Veronesecone枝は全排除。残る全候補のcanonical AS3基礎A0はB/R双方へ埋まる。vがQgr(A0)に入れば非零sGがA0∩(G)に入り矛盾するため、vは商体外。これにより純正二次関係3本は必ず二本の可逆crossと一本のmonic平方へ還元でき、vt=g(t)v+delta(t),v²=ell*v+qが全候補を被覆する。T=<W>は対角/Jordan両基礎でHT=1/((1-t)²(1-t²))、T2に関係なし。T基底×vv/zzを避ける交互語はHB=(1-t)^-4と一致して実際の基底となる。gはT自己同型、deltaは次数1skew derivation、平方互換は(g delta+delta g)(t)=ell*g(t)-g²(t)*ell。追加正規化仮定を課した部分chartではない。

原稿lem:h3-positive3-no-fraction,prop:h3-positive3-Jordan-cubic-base,thm:h3-positive3-monic-coverage。A0 noeth整域とcut後の単射でv rationalを排除し、純正関係空間Lのv²射影rank1/L0両cross射影isoを証明。Jordan TはC=[y,x]−kappa*x²=gamma*z²、Cx=xC,yC=Cy−2epsilon*beta*xC,yx=xy+kappa*x²+Cのweighted微分Oreで、SJ PBWへ単射。全候補のnormalspanのHilbert一致で基底独立を得る。任意T関係へvを掛けT+Tvを分離してg/deltaのwell-definedを証明、v(vt)と(v²)tから平方互換。verify_cubic_positive3_monic_coverage.py/certificateはOre/級数/係数の厳密恒等式を検証、商体/全被覆は構造証明。全H3分類や全係数AS4存在は主張しない。

### 正三次元の対角基礎全排除

全(3,1)はgamma0/cone枝に加え、対角canonical AS3基礎の全aも排除。全monic正規化被覆上でmu vの非分裂成分を二次自由性により排除、top vv縮約からg固定一次元Lを得る。Tの二次centralizerはalpha=a²+a^-2!=2でkL²、alpha2でkL²+k[x,y]。inner deltaは平方差factor、Heisenberg残余は通常Ore中山で排除。平方完成後g delta+delta g0で非innerが残るのはc=+-i,alpha0だけだが、N=x²y²が全positive反転/z固定の正規元となりH3 Gと可換かつ反可換して矛盾。c−1反射と軸swapは全alphaでinnerのみ、定数pivotと一変数unit coefficient idealsで特殊値込み検証。

原稿lem:h3-positive3-cubic-centralizers,thm:h3-positive3-diagonal-base-exclusion。三次関係の可換化gcdxyでalpha!=2のAutTはdiag/anti、alpha2はGL2。vvrowはvv/zz係数0で、W²rel0からcross非零、anti-cycleで[v,L]となりgL=L。inner後ell0、centralizerでfactor、Heisenbergだけq=bC/gIでv²~z²となり、a1ではq−1plane(r=v+z,s=v−z)[x]上の通常Ore-yによりmu v−矛盾。a−1はH=mu twist(hdet1,H4id)で同じ矛盾。c!=-1の平方完成でSigmaの固有値からc+-iだけdelta x=Ky²が残り、T cubic skewderivはalphaK0。alpha0のN=x²y²はx/y/v反転,z固定、G evenz/degree3かつcommWでG0矛盾。c−1のSigma compatible4coeffはinner yのみ、swapはinner gauge後6定数pivot。verify_cubic_positive3_diagonal_monic.py/certificateでT4定数7pivot、両centralizerの3minor gcdalpha−2とalpha2rank2、reflection一変数unit ideals、swap6定数pivot、imaginary resonance alphaを厳密。

## 5. 非CY符号型：重複度 (2,2)

全認識は `cubic_order2_22_secant_L_complete.tex` の `thm:h3-order2-22-L-complete`。許容切断と全矢は `cubic_order2_22_clifford_curved.tex` の `thm:h3-order2-22-clifford-conic`、`thm:h3-order2-22-clifford-arrows`。以下のrank・tangent・secant分解はこの結論の補助還元である。

### 両top非零の完全排除とmixed rank4領域の認識

(2,2)/mixed rank4の全H3は、全Jordan型込みで既分類の曲がったClifford族B_hに一致する。P,Qとも非零のL0非鏡開集合では、正常三次核が零である。P0は既知符号族、Q0はB_h、符号族はh0部分族。全切断のadmissibility、全幾何学的矢、一般dim5/慣性mu2は既存の曲がったClifford定理を使う。

証明は `papers/sections/cubic_order2_22_secant_L_complete.tex`。前節までの全排除と主chart逆行列により両top非零全候補がL非鏡開集合へ帰着していることを使用する。最後の底はp=rho²−1,c=rho²+1,D=c−p*z²,Q=c−2c*z+p*z²,H=Q+4z,F=p*z−c,A=Q²−2D²、U=rho*p*c*D*z*(z−1)*F*A*Q*H。t=pQ/(2D),s=i(rho+1)cH/(2rhoD),a=p²A/(4rho²D²)。正則逆写像と分母の全値被覆は `verify_cubic_order2_22_secant_L_parameter.py` により検証済み。

公開29四次汎関数の各288元関係annihilator恒等式を検証し、正三次32自由語に対する24×32関係行列R3と32×44正常行Nを作る。QQ(i)[rho,z]上のkernelは15生成元から非零定数を持つ5関係で自由rank10のEへ縮約され、syz(E)=0。座標Tは全て多項式で、全32×44成分のET=Nを厳密確認。TのU単元因子だけを行・列から除き、単元pivot10回で行が零本となる。非定数pivotは定数/iを除きrho,D,Qだけ。各Gaussian normの単元因子分解も再検証する。従って正常行加群は全kernelに等しい。AS4点で正三次次元10、R3rank22が最大なのでkernelの底変更が成立し、正常三次は零。

再生手順（SymPy、python-flint、Singularが必要。生成する巨大入力/pickleはGitへ追跡しない）：
```sh
python computations/build_cubic_order2_22_secant_L_module.py --output /tmp/L.sing --method free
Singular -q /tmp/L.sing
python computations/solve_cubic_order2_22_secant_L_coordinates.py --prefix /tmp/L.sing
python computations/verify_cubic_order2_22_secant_L_saturation.py --prefix /tmp/L.sing --certificate /tmp/L-certificate.json
```
小証明書は `computations/cubic_order2_22_secant_L_saturation_certificate.json`。ASCII exportはSingular 4.4.1のalgebraic minpoly dump不具合を避ける。旧direct/presentationの巨大Ann/lift計算は証明に不要。B0追加汎関数も不要となった。

### 正top非零Clifford chartのH3判定

正top非零へ出るClifford型B_h（正側可換/cross反交換/{u,v}=h2）の全包絡AS4/domain/mu++--と八次元正常核を証明。u²/v²係数独立chartではF1上のeven/odd Clifford sheafを復元し、飽和性と例外曲線二節点の非自明quaternionにより全商domain。H3 iff conic総空間smooth iff planequartic reduced/nodalかつ全余分nodeがrank1。h=xy,G=x³+y³+xu²+yv²は厳密Jacobian検算付き実H3例。

証明：papers/sections/cubic_order2_22_clifford_curved.tex。検証器verify_cubic_order2_22_clifford_curved.pyは全係数四PBW overlap、八正常列零と補空間minor4、scroll determinant恒等式、実例の全射影Jacobianを厳密再生。既存(1,3)定理を被覆として使用せず、共通局所Clifford補題とH3認識の証明を、本節で構成した束・飽和性・domainに適用した。

独立係数Clifford chartのH3判定と実例を確定した。

### 曲がったClifford全切断・全幾何学的矢

Clifford型B_hの依存係数境界を全排除した。u²中心開集合を三変数skew/cocycle twistへ正確に復元し、依存係数なら対応可換affine曲面に必ず特異点が出る。従って既存独立chartのconic必要十分判定がB_h全体の全H3切断を尽くす。全pointed exact幾何学的矢はGL2U×((Gm)²⋊S2V)のh保存/三次直線保存式、次数Gm商。表示stack一般dim5/慣性mu2、h0は既知dim2/慣性mu2²。

新しい検証器verify_cubic_order2_22_clifford_boundary.pyは、X=x/u,Y=y/u,W=v/u+h(X,Y)/2とu反転の全六関係、およびG=-Fu³を非可換順序積で厳密確認。F=f3-alpha*X+beta*X*(W²-h²/4)は有限(Z2)² cocycle twistと可換曲面を比較でき、alpha=beta*c²なら(0,0,c)は全偏微分零。全幾何学的矢の証明と一般慣性計算は同じClifford節に統合。

### (2,2)のmixed rank2排除

(2,2)のmixed rank2も全Jordan型込みで空と確定した。最後の可逆secant必要曲面は七多項式四次汎関数の1008恒等式と単一10minor −2ell^15*rho^20*(rho+1)^15*(2rho+1)^2により全値排除し、ell0/共鳴fibreも既存全値検証で覆う。従って(2,2)はmixed rank4のみが残る。

検証器 verify_cubic_order2_22_secant_surface.py と39KB入力は七汎関数のみを保持し、1008多項式消滅恒等式と14x32交換子行列の単一10minorを再生する。曲面式Hを法にdet=−2ell^15*rho^20*(rho+1)^15*(2rho+1)^2。恒等式は整域の分数体で計算するが、元のminorは多項式なので全特殊値へ適用され、途中pivot零点を例外扱いしない。rho(rho+1)ell(2rho+1)unitで核次元22。ell0とrho−1/2は既存の全値証明を使い、C0排除は独立な整合検算として保持する。従って半単純rank2全空、単冪剛性/右twist−4により全Jordan型も空。

可逆secantのgraded包絡矢Phiとrho/ell不変性は実際のAS4点に関する補助結果として保持するが、この領域にH3点の存在は主張しない。独立査読・新規性確認は未実施。追加のas4結果は輸入していない。

### mixed rank2のpencil被覆と純mixed排除

次の半単純(2,2)/mixed rank2では、奇top交代行列の両対角blockがD_ji,lk=A_il,kj、PfD=−PfAとなり、A0なら両方向の純mixed二式、A非零なら両射影可逆graphへ漏れなく還元。graphは2x2行列pencilのsecant/tangent/二rulingの四標準形、graph detは−1/+1/−1/+1。純mixed枝はeven crossblock可逆からSchur条件を得て、pI/qJordanは係数ideal1、qdiagは五必要表示へ正規化。五つ全ての指定正常三次140x20は厳密rank20で全H3排除。

原稿prop:h3-order2-22-pencil-coverage,cor:h3-order2-22-pure-mixed-schur,thm:h3-order2-22-pure-exclusion。twistedquartic全語空間は32=positive4+mixed22+negative6。odd H=[A B;-Bt D]rank2、巡回reshape D_ji,lk=A_il,kjは可逆でPfD=−PfA。A0ではB rank1,pureUV/VU各一本でdomainにより両2x2quad非退化。A!=0はrankA=rankD2、odd relation両射影iso。E pencil determinantが二零点/重根/恒等0からsecant,tangent,二ruling、DからFとdetg表を全被覆。pure枝B=m vecp vecq^tのevenKdet=−m4(detp detq)²、evenrank4でP可逆/Q=KtP^-1K。pI,qdiag1r又はqJordanに正規化、purepositivequartic P(A,B,C,D)det=−B²(4AD−B²−C²)なのでBunit、relativehomothetyでB=m1。qdiagではcyclic条件DZ=ArZ0,2AD(1−r²)+C(1+r²)0,4AD−2−C²0,Z=1+r+C(1−r)。Z0はr−1,C0,AD1/2を対角残余でA1,D1/2へ。ZnonzeroはA=D0,C²=-2,r²=-1の四表示。qJordan係数idealはGroebner1。五必要表示全てB3dim20/B4dim35、指定normalizer140x20rank20でG0、H3排除。verify_cubic_order2_22_rank2.py/certificateとverify_cubic_order2_22_pure_exclusion.py/certificateで全恒等式/五exactfield計算。半単純rank2の四graph型のみ残り、他Jordan/rank4の被覆は未主張。

### 二つのrulingの排除

半単純(2,2)/mixed rank2は、全pencil被覆に続きpure mixedと二rulingを排除し、secant/tangent二graph型だけに縮小。pure mixedはeven Schur条件から五必要表示に限り、全五つの指定正常三次行列rank20で核零。rulingではKが一行又は一列だけとなり、三つの純二元関係のrank<=1条件とdomainからそのblockが零、反対側に三次元以上の純二次関係を強制して矛盾。二次minor/単位飽和idealを全係数厳密検証。

原稿thm:h3-order2-22-ruling-exclusion。任意binary planeのpurequadratic関係はdomainならdim<=1かつrankone禁止。U-rulingはmixedtop正文字が全x0でK一行、P(A,B,C,D)のxy/yx/yy三行がpure正関係なのでrank<=1。その2minor idealはB²,C²,D²を含み、残るrow AxxはrankoneゆえA0。Uprojection<=1からpureVV kernel>=3で矛盾。V-rulingはmixed負文字全z0でK一列、cyclicQのuv/vu/vv三行N=[[b,d,c,e],[b,c,d,e],[c,e,e,f]]がpure負関係rank<=1。2minor idealを各行の2x2係数detで飽和すると全てideal1、従って各行rankone又は0、domainから全0。VVprojection<=1からpureUU kernel>=3で矛盾。verify_cubic_order2_22_ruling_exclusion.py/certificateで全係数GB/3saturation 。

### tangent graphの可逆部分の正規形

半単純(2,2)/mixed rank2はpure mixedと二rulingを排除し、secant/tangent二graph型だけに縮小。さらにtangentのeven crossblock可逆部分は全係数のpencil安定化作用でg=[[0,-1],[1,0]]へ正規化でき、even Schur条件からC0,B1,A=(1+D²)/(2D),D(1+2D²)unitの一変数六関係へ全被覆。

原稿prop:h3-order2-22-tangent-normalform。graphg=[[a,b],[c,d]],det1のevenK=[[-b,d,a,-c],[a,-c,0,0],[-d,0,c,0],[c,0,0,0]],detK=−c4。E/F tangent pencilのgenerator stabilizerはP=[[1,p],[0,r]],Q=[[1,q],[0,r]]、p/q独立でg->QgP^-1、p=d/c,q=−a/c,r=1/cがgcanonicalJへ。Schur負cyclicはX=−Cc+D(a−d)に対し2BDcX0と−2B(Bc+D(a+d))X0なのでBcunitからX0。残余−4ADc²+2B²c²+C²c²+2D²(ad−bc)0。gcanonical/B1でC0,4AD=2+2D²、DunitかつdetP=−(1+2D²)unit。六関係は本文、verify_cubic_order2_22_tangent_normalform.py/certificateが全恒等式。任意D AS4存在/正常三次/H3性は未主張。

### mixed rank4の正top三標準型

半単純(2,2)/mixed rank2はpure mixedと二rulingを排除し、secant/tangentのみ。tangent K可逆部分はD(1+2D²)unit,A=(1+D²)/(2D)の一変数必要表示へ全被覆。指定正常三次のgenericな核零だけでは全Dを排除しない。全Dの排除は `cubic_order2_22_tangent_normalform.tex` と退化境界の計算を合わせる。mixed rank4の半単純領域では偶top rank2により正二元anti-cyclic quarticのB係数が零となり、純正topはcommutator⊙対称二次式に限る。従ってGL2と尺度で零/平方型/非退化型の三種へ被覆。

原稿prop:h3-order2-22-rank4-positive-top。oddR4ならevenR2でevenH rank2、purepositiveP(A,B,C,D)もrank<=2。3minor idealはB³を含むのでB0。逆にB0ならP=comm*q^t+q*comm^t,q=(A,C/2,C/2,D) symmetric、qnonzeroはcommと独立なのでrank2、evenR->UU projectionisoonto span(comm,q)。二変数対称式のrank1/2で三標準型。verify_cubic_order2_22_rank4_top.py/certificateでminor idealと外積和恒等式を全係数。

tangent計算で19個の汎関数はh(D)=10D^6−D^4−4D²−1の零点で不足したが、全functionalを飽和して14個を補った33個の明示証明書を保存した。交換子行だけをhで割らず、全四次functionalのannihilation恒等式を再生することが正しい特殊値の検証である。

### tangent可逆部分の全値排除

半単純(2,2)/mixed rank2はpure mixedと二rulingを排除し、さらにtangent K可逆部分も全Dで排除。33個のpolynomial quartic functionalの4752恒等式と、66x32交換子行列の九つの10minorのgcd D^12を厳密検証。H3ではpositiveB3dim10なので、rank>=10が全Dunitで成立するとpositive三次centralizerは零、正常Gも零となる。従ってrank2の残りはsecant型とtangent K退化c0境界。mixed rank4は正topを零/commutator⊙平方/commutator⊙非退化対称式の三種へ被覆。

原稿thm:h3-order2-22-tangent-fullrank-exclusion。input JSONは33個のQ[D]上quartic functional（even128語の辞書式座標）と九10x10 minorの位置を持つ。六関係を前後の二語で挟んだ全144 even quartic relationsへの4752 exact annihilation identitiesを確認。三関係を2D倍してFracElementを使わずQ[D]で直接検証し、定数分母もnum/den両方から復元する。positive cubic32語のx/y交換子にfunctionalを適用したN66x32について九minorは次数80,82,81,84,70,82,75,83,73、monic gcd D^12。ゆえ全Dunitでrank>=10。H3/指定AS4のtraceB3=0からpositiveB3dim10で、positive cubic relation dim22はkerN内、rank>=10からkerNと一致、positive cubic centralizer0。正常Gはmu固定かつcommx/yなので全値で排除。D1等の有限標本は証明に用いず、九exact polynomial minorsのgcdが全値coverを与える。

再現：python computations/verify_cubic_order2_22_tangent_exclusion.py。入力 computations/cubic_order2_22_tangent_annihilator_input.json、出力certificate同prefix。python-flint backendまたは通常のSymPy backendで照合できる。汎関数の構成に使ったh-rootのfield linear algebraやgeneric rrefを信頼入力にはせず、全33functionalと九minorを元の六関係から直接点検する。全AS4存在や全H3被覆をこの排除から主張しない。

### tangent退化境界の排除

全(3,1)は全Jordan型込みで空。半単純(2,2)/mixed rank2はpure mixed/二ruling/全tangentを排除し、secantだけが残る。tangent K可逆は33functional/九minor gcd D^12で全値排除。c0境界はyy縮約q=(B,D,-D,0)が零ならdomain消去で余分なodd quadを強制しAS4外、非零ならg=epsilon I,B0、Schurからxycomm/uvantiと二平方式へ。四平方が中央となり、W=yu+epsilon*uy,N=yv−epsilon*vyの積は−mu正規化かつmu固定、正常Gと可換/反可換してH3排除。mixed rank4は正top三型へ被覆。

原稿thm:h3-order2-22-tangent-total-exclusion。c0/ad1のpureUU rows q=(B,D,-D,0),r=(A(d−a),dC−aB,−dB−aC,D(d−a))のspan<=1/rankone禁止を使う。qnonzeroはDunit、minorD²(d−a)と−2aBDからa=d=epsilon±1/B0、vのu移動でgraphb0。q0はB=D0で、C0だとA(d−a)xx purequadからA(d−a)0、evenUUprojection<=2でpureVVquad>=2のdomain矛盾。Cunitならu²=−a^-1*x(Ax+Cy),ux=−a^-1xu、uとu²可換からxをdomain消去しuy+a yu+(A/C)(a−a^-1)xu0というv無しodd quadを得るが、元odd2本の片方はxv係数unitなので新関係、AS4外。

Dunit branchはKepsilonI、evenHの(yy,xy,xx,uv)minorD²、SchurはnegativeQのa0=c0=d0=f0=0。negativeprojection>=3からe0unit、uv+vu0。positivecommとu²=−epsilon(Ax²+Cxy+Dy²),v²=−epsilon/e0*x²−b0/e0*u²、yshiftC0で必要表示。xu=−epsilon ux、xv−epsilon vx=−(yu+epsilon uy)、uvanti、u²=alpha x²+delta y²,v²=beta x²+gamma y²,delta*(alpha gamma−beta delta)unit。x²centralはxT=−epsilon Txより、u²centralはpositivecommとuvantiより、deltaunitでy²central、v²もcentral。W=yu+epsilon uy,N=yv−epsilon vyはB2非零、normalizersそれぞれ(-epsilon,epsilon,epsilon,-epsilon),(epsilon,-epsilon,epsilon,-epsilon)、双方mu eigen−なのでM=WNはmu固定かつnormalizer−mu。GはMと可換、Mはdegree3/muGfixedからGと反可換し矛盾。

verify_cubic_order2_22_tangent_boundary.py/certificateで二minor、Schur全係数constant matrix rank4、両epsilonのnormal covariance全八式を中心平方+三quadratic関係のdegree3 freeword行恒等式として厳密照合。Zhang twistによるG正規化の変化を無視せず、この証明は両符号を直接扱う。

allunitでKdet非零のSchur必要式と、rankが落ちるa/b/c/d=0の境界を区別する。正常元の低次数作用で−muを実現する障害と、四次annihilatorの全値minor被覆は別の排除機構である。

### secant graphの退化四型

半単純(2,2)/mixed rank2はpure mixed/二ruling/全tangentを排除しsecantのみ。secant gdet−1のKはdet−abcd、退化全境界をtorus尺度と同時交換で四固定graph（rank2二種/rank3二種）へ全被覆した。K可逆部分は別に残す。

原稿prop:h3-order2-22-secant-degenerate-strata。gen尺度はg(a,b,c,d)->g(r a,s b,c/s,d/r)、simultaneous x/y,u/v swapはa/d,b/c交換。K sparseのdet−abcd、rank=非零成分数。ad−bc−1から退化はzero2 diagonal/offdiag又はzero1の二軌道で、四固定gはdiag(1,-1),swap,[[0,1],[1,1]],[[1,0],[1,-1]]。verify_cubic_order2_22_secant_strata.py/certificate 。全境界AS4/H3排除はこの命題から主張しない。

有用な反省：secant sample(s=3/4,t=5/4,A0,C=sqrt(-34)/3)のpositiveU³はexact rank8であり、purepositive quartic topの縮約をT(U)の三次関係と同一視してはならない。T(U) cubicAS3仮説は破棄、実際のB degree3 quotientで点検する。

### secant graphのrank2境界の排除

半単純(2,2)/mixed rank2はpure mixed/二ruling/全tangentに加え、secant K rank2の二固定graphも全排除。diag(1,-1)は純正縮約から二分枝、Schur/domainでuvが全生成元反転となる分枝と、q=+-iでM=x²y²が−mu正規化となる分枝で排除。swap graphはeven Schurからu²=v²、xy/{uv}中心。AD0は余分なodd quadでAS4外、ADunitは基底変更後の四平方中心と二paired正規二次式の積−muで排除。残るrank2候補はsecant K rank3二表示とK rank4開部分。

原稿lem:h3-order2-fixed-normal-obstruction,thm:h3-order2-22-secant-rank2-exclusion。mu固定の非零正規元Mが全生成元反転又は−muを正規化すれば、Gと可換/反可換して矛盾。diag graphのpureUU xy/yx rowsはAB=AC=DB=DC=B²+C²0を強制し、domainからB=C0/ADunitかA=D0/Bunit/C²=-B²。前者のSchurはnegativea=c=f0,b(A+D)=e(A+D)=d(A²+D²)0。domain negativeprojection>=3はb又はeunitを強制しA=-D/d0、uv=-vu、N=uvは全4gen反転かつmu固定。後者はpositive yx=zeta xy,zeta²−1、uv=-B y²,vu=-B x²、odd/associativityでu/vがx²,y²を交換。x²y²はpositive反転/negative固定=−muかつmu固定。両方H3排除。

swap graphはpureUU xx/yy 2minor−B²からB0、A/D両0はprojection<=2でdomain外。Aunitを交換で覆い、Schurはnegativec=d0,f=-a,e=-b、domainからbunit。u²=v²=-Q(U)が中心、xy=a u²+b{uv}よりxy/{uv}も中心、A x²+D y²中心。AD0はx²central等から新odd ux+xv0をdomain消去で得てB2矛盾。ADunitでp=sqrtA*x+sqrtD*y,q=sqrtA*x−sqrtD*y,r=u+v,s=u−vの全4平方中心、odd {r,q}=[s,p],{r,p}=[s,q]。W=[s,p],N=[s,q]はmu奇正規二次、normalizers(-,+,+,-),(+,-,+,-)、積mu固定/-mu正規化で排除。

verify_cubic_order2_22_secant_rank2.py/certificateは全係数の縮約ideal/両Schur条件、diag uv全反可換式、四平方交換式、swap pairednormalquad全八covarianceを厳密に照合する。有限標本や全AS4存在を入力にしない。K rank4開部分は別に残す。

### secant graphのrank3境界の排除

半単純(2,2)/mixed rank2は全pencilからpure mixed/二ruling/全tangent/secant K rank2を排除し、さらにsecant K rank3二表示もAS4整域自体から排除。one-diagonal-zeroはdomain二次消去と非退化Pのcyclic Schur二式が矛盾。one-offdiagonal-zeroはpositiveAS2 T、vx=yv,v²/uv∈T2から分数環二次拡大へ落ち、次数0は非自明P1対合のノルム全射により曲線体となるのでB GK<=2、14641に矛盾。従って残る半単純(2,2)/mixed rank2はK可逆secantのall abcdunit開部分のみ。

原稿lem:h3-AS2-partial-root-growth,thm:h3-order2-22-secant-rank3-exclusion,cor:h3-order2-22-only-invertible-secant。one-diagonal-zero g[[0,1],[1,1]]のpureyy rowは(B,D,-D,0)。D0はdomainB0、v²=-x(Ax+Cy),vx=-xu,uy+yv+vx0からvとv²可換を使いx消去でA(ux+xv)+Cxu0。Aunitは独立odd quad、A0/Cunitはproduct0、A=C0はv²0。DunitならB0はuv0を強制、ゆえBunit。K^tはxx/xy/yx、Pxy行DyyからevenprojectionUU full4でP可逆。negativecyclicSchur二式BD(B−C)=BD(B+C)0が矛盾。

one-offdiagonal-zero g[[1,0],[1,-1]]ではpureyx q非零nondeg、AS2 Tがfactor lemmaでBへ単射、vx=yv,v²,uv∈T2非零。D=QgrT=K[x±;sigma],K=k(t)。f=Ad_vはf x=y,f y=QxQ^-1,Q=v²でDへ入り、f² innerQなのでfD=D。E=D+Dv、w=vx^-1、E0=K+Kw、phi=f_K sigma^-1は対合、w²h∈Kphi。phi非自明ならPGL2座標phi z=-z、algclosed factorizationとNorm(z-b)=b²-z²からh=Normr、(r^-1w)²1でdomain矛盾。phiidならE0=L曲線体有限拡大K、E=L[x±;theta]、u=(uv)v^-1も入りB全体がcurve graded Laurent内。一般曲線へ拡張したgrowth lemma（極因子の線形成長、h0<=deg+1）でGK<=2。Tsenの新規引用は不要、二次ノルムを初等的に証明。

verify_cubic_order2_22_secant_rank3.py/certificateはcyclic二式、x倍新oddquadの自由環恒等式、AS2 Mobius商/非退化det、norm因子恒等式を厳密に照合する。分数環と曲線成長は本文構造証明。growth lemmaの一般曲線拡張に伴いverify_cubic_positive3_cone_exclusion.pyも当該検証器の照合対象に含む。

可逆secantの必要正規形は有理graphで表す。以前の対称graph(s,t)はrho=s²,ell=−A_old/s,C_new=C_oldによる四重被覆であり、係数体を増やすため計算の正本には使わない。

### 可逆secantの有理必要曲面

半単純(2,2)/mixed rank2は全退化境界を排除しK可逆secantだけ。この全領域を有理graph g=[[1,1],[rho+1,rho]]へ正規化し、rho*C²+(2rho+1)(2rho*ell²+1)=0、rho(rho+1)(2rho*ell²+rho+1)unitの二次元必要曲面で被覆。P(A,B,C,D)はA=-rho*ell,B1,Dell。曲面の特異点はrho−1/2,C0,ell±1の通常二重点二つだけで、両点はB4dim36によりAS4外。

原稿prop:h3-order2-22-secant-open-normalform,prop:h3-order2-22-secant-open-nodes。torusでa=b1、rho=ad,c=rho+1,d=rho。K=[[0,-rho,0,0],[0,0,0,rho+1],[-1,0,0,0],[0,0,1,0]]可逆、positiveBunitを1。Schur二式(1−C)(A+rhoD)=0,(rho+1)(1+C)(A+rhoD)0からA=-rhoD、Dell。残余H=rho*C²+(2rho+1)(2rho*ell²+1)0、rho*detP+(2rho*ell²+rho+1)=H恒等式。base ring UFD/generic conic rank3より必要曲面integral2dim。Jacobianはrho−1/2,C0,ell±1だけ、quadratic matrix det2。両表示をQQ上exact B4計算でeven20/odd16/total36としAS4排除。

非共鳴conicにはell0=1/(2rho),C0=sqrt(-2)*(2rho+1)/(2rho)のrationalpoint。C=C0+k(ell−ell0)でh=−(2rho+1)(sqrt(-2)k+2)/(rho(k²+2(2rho+1)))、ell=ell0+h,C=C0+kh。finitek chartの補点(ell0,-C0)はinversechart、rho−1/2のC0特殊fibreは別に扱う。必要曲面の族/節はintrinsic H3成分やAS4十分性ではない。verify_cubic_order2_22_secant_open.py/certificateが全Schur/有理点chart/二特異点/両B4dim36を厳密に照合する。

### 可逆secantの共鳴fiber

半単純(2,2)/mixed rank2は全境界を排除し、可逆secantの有理必要曲面rho*C²+(2rho+1)(2rho*ell²+1)=0へ被覆。二nodesはB4dim36でAS4外、さらにrho−1/2特殊曲線も全値H3排除。19functional/2736恒等式と12minorのgcd ell^10*(ell²−3/2)^5で三値まで絞り、ell0/+-sqrt6/2のfull normalizer rank10をexact検算。残る候補はrho(rho+1)(2rho+1)(2rho*ell²+rho+1)unitの滑らかな二次元必要曲面。この必要表示の排除にAS4存在の十分性は必要ない。

原稿thm:h3-order2-22-secant-resonant-exclusion。P(ell/2,1,0,ell),K有理、odd xu+uy+vx/2,yv+uy−vx/2。input JSONにQ[ell]上19quartic functionalと12maximalminor位置。全144 even quartic relationsへの2736 annihilation identities 、38x32 x/y commutator matrixの12 ten-minor gcd monic ell^10*(ell²−3/2)^5（degrees26,37,41,37,41,37,38,40,46,35,32,37）。したがってell0とell²3/2以外rank>=10、H3positiveB3dim10から正三次centralizer0。全残余三値をQQ(sqrt6)上exact検証：ell0とsqrt6/2でevenB3 10,evenB4 19,oddB4 16、full designatednormalizer rank10、negativeconjugateもfield embeddingで同時被覆。有限標本ではなくminor全零点を完全に処理。

再現python computations/verify_cubic_order2_22_secant_resonant.py、入力cubic_order2_22_secant_resonant_input.json、同prefixcertificate。

### mixed rank2の単冪剛性

全(1,3)は幾何学的被覆・H3必要十分条件・全矢まで確定、全(3,1)は全Jordan型込みで空。(2,2) mixed rank2も全Jordan型込みで空。mixed rank4のcanonical正top P0全体は、退化境界と全Jordan型込みで固定非CY符号族へ完全に幾何学的認識、一般dim2/inertia mu2²。未知の(2,2)は正top非零のcomm⊙平方/comm⊙非退化quadの二型だけ。非退化型のJordanはなく、平方型の非半単純には正側Jordanが必要。

原稿lem:h3-order2-22-rank2-unipotent-rigidity,thm:h3-order2-22-rank2-no-Jordan,cor:h3-order2-22-rank2-all-Jordan-coverage。必要pencil被覆/必要Schur正規化はG存在を使わずnoeth quadratic Koszul AS4 domainにも有効であることを明示。H commute muC unipotentならU/Vを保つ。puremixedはpI/qdiag(1,z),z−1,+-iの両lineをpointwise固定し、T^t q=q T^t、simple eigenでTdiagonalunipotentId。secant Eの二rankone点はconnected unipotent closureでpointwise固定、両U/VaxesよりHId。tangentはx/u固定,y->y+beta x,v->v+eta u。E/F uppermatP(beta+eta),Q(beta−eta)、gJ固定はbeta=eta0、gepsilonI固定はeta0。後者のdomain必要関係u²=alpha x²+delta y²,deltaunitとpositivecommから2delta beta xy+delta beta²x²0でbeta0。rulingはAS4domain外。全caseでHId。

元Bでmu=muSs muU、blocks2+2なのでN=muU−I,N²0。H=I+N/4は整数nでI+nN=muU^nのrelation保存がpolynomialnとして全nへ延長されautoB、H4muU。右twist C=B^Hはnoeth/Koszul/AS4/domainを保存しmuC=muB H^-4=muSs、oddRdim2もid⊗H^-1で保存。HはC autoかつmuCと可換unipotentなのでrigidityからHId、muUsemi消滅。G輸送/右twist後のH3性は使わない。RRZ既存右twist公式を明示し新規as4被覆は輸入しない。

verify_cubic_order2_22_rank2_unipotent.py/certificateが両tangent upper stabilizer、puremixed centralizer、square-invariance、二Jordanblockのfourth-root/−4 formulaを厳密に照合する。既存必要被覆のG非依存性とfinite rank1点への単冪作用は本文構造証明。これで(2,2) mixed rank2の非半単純残余はなく、mu1±のこの領域は全て可逆secant必要曲面へ。

### 零topの必要atlas

(2,2) mixed rank4で正top非零の場合、正平面を固定する片側単冪作用はH3から排除した。負固定VVは<u²,[u,v]>、cyclic Qと偶rank2から負射影line。u²-onlyはPBW三次21でAS4外、comm成分unitはT[u;f][v;sigma,delta]、Tcomm又はq−1へ還元。実際のNakからf²=muT,hdetf−1。commは正常Gが正規一次式yで割れ、q−1は正三次正常核零。従って非退化正topの全Jordan部分が消滅。平方topの非半単純候補は正側Jordan非零が必要。

### rank4負topの必要五形

半単純(2,2) mixed rank4の負cyclic二元topはrank<=2なので、零・第四乗・対称secant(u4+v4)・対称tangent(symu3v)・非対称(uvuv+vuvu)の五形で全被覆した。対称/交代分解とapolar二次核の二根/重根で証明。正top零なら第四乗は整域性で排除、Q零では偶関係が純正/純負非退化quad二本へ分裂、Qrank2では純負AS2平面が一本現れ、対称二型はq−1、非対称型はq±iに限る。

証明は cubic_order2_22_rank4_negative_top.tex。五形のrankと対称/交代分解をverify_cubic_order2_22_rank4_negative_top.pyで検証。P0でevenmiddleをr1⊙r2と分解し、P0から片方を純負関係に取る。Q1なら純負関係が平方で矛盾。Q2の二因子u²±iv²、u²/uv+vu、uv±ivuを読み、非退化二元関係の因数分解からAS2埋込みを得る。

### rank4奇graphの全二分法

半単純(2,2) mixed rank4の奇関係は、可逆四次元graph(det=-1)か、純UV/VU非退化関係を一本ずつ持つ両射影rank3型の二択で全被覆。部分転置PfD=-PfAと四次元交代像・整域性で証明。正top零のgraph型では、正二次射影が非退化なら負AS2平面上のPBW double Ore表示へ認識。負top零ではこの条件は自動かつtail0、負rank2ではbase q−1又はq±i。退化正射影は別分枝として保持し、全graphやpairedpureを既知doubleOre分類で覆ったと主張しない。

O=[[A,B],[-B^t,D]]、rankO4、DはAのcyclic部分転置。純UV/VU関係空間はdomainよりdim<=1、従って両射影rank>=3。射影rank4なら主交代block rank4、rank3ならrank2。Pf恒等式より両射影は同時に4又は3。fullgraphはD=-B^t A^-1B、detB=-PfA²、detgraph=-1。P0graphと非退化正射影では6quadのmonic簡約が三次20語を持ち、実際のdimB3=20から全三次overlap0、DiamondでPBW。退化正射影のrank1行列は積又は平方であり、この認識に含めない。

### rank4可換正平面separated chart

正平面可換・負二生成元がそれぞれ正平面を正規化するseparated chartを、量子/Jordan負平面とも全H3判定した。量子型は全F∈GL2のB(F):ut=F(t)u,vt=F^-1(t)v,vu=−det(F)uv。全AS4とmu++--、正正常核はker(Sym³F+I) +ker(F−detF I)uv、F²Iの場合だけker(F+I)u²/v²を加える。全Fで因数分解を追うとH3はF−Iの既知符号包絡だけ。Jordan負平面も反射Fを強制し、Gが正規一次式で割れるため全排除。

F²IはI/−I/反射の三択、正常核次元2/8/5。F²neqIではdet(F−DI)=Ddet(F−I)、固有値1がなければ純二元三次のみで因数分解、固有値1が単純なら全Gが他方の固有一次式で割れる、unipotent重根ならG=linear*uv。Jordan負平面はgf=fg=f²からg=f、muU=f^-2, muu=detf*uによりf反射、正規yで商を取って微分Ore内の反交換不可能性を使う。既知符号包絡の全幾何学的矢/判定へ接合し、新成分とはしない。

mixed(2,2)、twisted tensor、double Oreに関する外部結果の採用範囲は `as4_imports.json` を正本とする。別commitの入口探索を、新しい被覆定理の輸入と同一視しない。

 さらに可換正平面separated chartの全Jordan型も閉じた。量子負平面でμU=(fg)^−1、fg単冪、負μは厳密に−1。fg≠IならG30零、u²/v²成分が非零ならf=g、そうでなければG=linear*uv。f=gでは±単冪の一次固有直線が全係数の共通因子となる。従って非半単純を含め、このchartのH3は既知符号包絡のみ。

### 二AS2平面separated chartの全認識

二AS2平面のseparated graphを全Jordan型込みで幾何学的H3認識した。可換正平面はseparated認識定理、非可換正量子平面は対角作用なら全skew分類で空、q−1反対角作用は正常核零、Jordan負平面でもmuTとの一次絡み合わせ零から純二元三次の因数分解で排除。Jordan正平面では中山単冪shearの固定核kx^n又は一次normalizer条件から全Gがxで割れ、Jordan/Jordanは固有値自体が矛盾。従ってこのchartの全H3は既知非CY符号包絡のみ。

半単純(2,2) mixed rank4のP=Q=0領域で、K=vec(a)vec(b)^t、a/bは非退化AS2関係、cross M=−(a^t⊗b)flipで可逆。従って全奇関係はfullgraph、pairedpure分枝なし。PfA=h=eps*det(a)det(b)、A#=PfA A^-1線型よりh*tau(A)+M^t A#M=0の六線型必要atlasを得た。QQ/QJ/JQ/JJ両符号八chartの局所化多項式イデアル一致を検証し、p/q±1特殊値を全保持。半単純JJ両分枝はPf0で不存在。全AS4十分性・全H3被覆・全非半単純は未主張。

### 零top atlasの補助計算

QQ p=q−1,eps+ではz2=z3=0、z0z5−z1z4=1。二対角torusとU/V軸交換で、両組成分が非零ならz0=z1=1,z4=t,z5=t+1へ正規化できる。公開verify_cubic_order2_22_rank4_zero_top_QQ_plus.pyで四PBW overlap全恒等0、54x10正常行列の指定minor定数−4を再生済み。QQ eps+全分枝は三chart/四minorで排除した。片組が零の境界は二方向separated。QQ p=q1 eps−はΛ²(U⊗V)=Sym²U⊗Λ²V + Λ²U⊗Sym²Vの二対称式へ分かれ、Pfneq0なら少なくとも一方非退化。

### QQ正Pfaffian分枝の全排除

零top QQ atlasのeps+全分枝をH3排除した。線型式/Pf非零からp−1又はq−1。二つの片側chartと交点SL2四係数を対角二torus/軸交換で正規化した全t chartで被覆。三chartの12PBW overlap全恒等0、正正常行列の四10minorは−8(t+1)²/t9、8(t−1)²/t9、1、−4。Bezoutで第一chartの全t非零を覆い、他chartは定数minor。交点の非分離族t0/t−1含む全境界を処理した。

### opposite-separated量子正平面の認識

正量子二元が負AS2平面をそれぞれ正規化するopposite-separated chartも全Jordan型で認識した。負commは正常二次係数がF/Gの一方Idを強制し、正平面commとなってGが正一次因子で割れる。負quantumの対角作用は既存skew分類、q−1反対角は中心平方と奇数乗から正常核零。負Jordanでは二次intertwiner det=(a+1)^3から例外a−1のみ、正中山式p1と奇偶条件で再び因数分解。従ってこのchartの全H3は固定符号包絡のみ。正Jordanのopposite-separated全体は範囲外。

### canonical零top領域の全Jordan消滅

canonical半単純untwistがP=Q=0のH3では中山の全Jordan部分が消滅する。可逆交代UV block Aに対して両側非自明単冪J⊗Jの固定式はPf0となり矛盾。片側正JordanのみはmuG固定式のAS2 shear核からGに一次因子。片側負Jordanのみはmixed graph可換環からT[u;f][v;sigma,delta]、f²=muT,hdetf−1となり、comm反射/quantum一次intertwiner/negative hdet符号で全排除。Gのtwist輸送やH3のtwist不変性は仮定しない。

両側単冪Pf0と片側graph[[f,d],[0,f]]、負二次固定空間をverify_cubic_order2_22_rank4_zero_top_unipotent.pyで確認。元Bは逆twistでpureAS2二本/fullgraphを保ち、Hilbert20/PBWでAS2単項式基底を得る。正側単冪のみではmuG固定の係数がkx³/kx。負側のみではvu−uv=κu²、muUId,muu−からf²=muT,hdetf−1。Tcomm反射はnormaly quotient微分Ore、TquantumはG12係数零→T3factor、TJordanはhdet1/−1矛盾。本文に統合済み。

### canonical零topの全幾何学的認識

canonical零top(P=Q=0) mixed rank4領域の全H3を、全Jordan型・全幾何学的矢込みで既知非CY符号包絡へ認識した。全Jordan消滅を用い、QQ eps+全排除、QQ eps−のseparated二型と両comm時の二対称式の非退化軸変換、QJ/JQ eps−の同様の軸変換、QJ/JQ eps+の特殊二点正常minor−16/−36、JJ両符号top不存在で八chartを完全被覆。全切断G=f3(U)+ell2(U)u²+ell3(U)v²、H3条件/全矢は固定sign定理へ接合。一般次元2/慣性mu2²。

A=SU⊗E+E⊗SV、PfA=detSU−detSV。可換側GL2のnormalized congruenceで非退化対称式をcrossへ移し、全特殊係数をseparatedへ被覆。量子/Jordan正符号特殊点の四overlapと正常minor−16/−36はzero_top_coverage検証器で再生。

### 曲がった対角rank4包絡の正常核

非零負topへ出る対角curved包絡[x,y]=alpha*u²+beta*v²、uv=-vu、u作用diag(lambda,lambda^-1)、v逆作用を全値でAS4/noeth/Koszul/domain・mu++--と認識した。全正常正三次核も判定。lambda±1の非零curvatureはWeyl中央化核零、lambda1零tailはfactor、lambda−1零tailは既知sign。新候補は原始6乗根lambda²−lambda+1=0のG=A x³+B y³、AB非零・tail非零だけで、正常核は全alpha/betaで厳密に2次元。商が正規正則なAS-Gorenstein商でμR=idであることだけでは、商の整域性とH3許容性を結論しない。

原始6乗根curved候補G=A x³+B y³も全alpha/betaで非整域と判定した。u/x逆転chartはk[C,V]上のorder6 GWA、a0=C−delta−gammaV²、3norm P=C³−delta³−gamma³V6−3delta gamma C V²。cutをX6=r³Pへ直し、sigma²の3normもPであるためZ=(r a0)^−1 X²がZ³1。monic6基底上でZ−1とZ²+Z+1がともに非零かつ零積なのでdomain仮定に矛盾する。従って対角curved全chartのH3は零tail/F−Iの既知signのみ。全非零toprank4の完成ではない。

### 原始6乗根normal cutの全非整域性

原始6乗根curved候補G=A x³+B y³も全alpha/betaで非整域と判定した。u/x逆転chartはk[C,V]上のorder6 GWA、a0=C−delta−gammaV²、3norm P=C³−delta³−gamma³V6−3delta gamma C V²。cutをX6=r³Pへ直し、sigma²の3normもPであるためZ=(r a0)^−1 X²がZ³1。monic6基底上でZ−1とZ²+Z+1がともに非零かつ零積なのでdomain仮定に矛盾する。従って対角curved全chartのH3は零tail/F−Iの既知signのみ。全非零toprank4の完成ではない。

局所化前後のbase単射はGWAのLaurent/monic6基底で証明する。K=k(C,V)へは非零係数のsigma6normという中心元を逆転して移る。r³=−B/A、X6=r³P。sigma³a0=a0によりsigma²norm3=P、Z³1。Lの係数field上の支持{0,2}/{0,2,4}が両因子の非零を保証する。次数2の部分crossed productだけを見てRのdomainを予想するのは誤りであり、実際の3normが全候補を排除した。頂点Extやaffineglを調べる必要はこの候補ではなくなった。

### 曲がった量子対角chartの全H3認識

正射影量子二次式を許す全二パラメータcurved対角包絡xy−p yx=alpha*u²+beta*v²、uv−、u作用diag(r,r^-1)、v作用diag(p/r,r/p)を全係数AS4/noeth/Koszul/domain・mu++--と認識し、H3はp1,r−1,alpha/beta0の既知signのみと判定。十語の二normalizer weightイデアルから例外はp1r±1とp³1/r³−1の九根のみ。九根でcurvature制約を全判定し、GWAのperiod3a0/monic6商で三次norm零因子を構成して全非sign候補を排除した。

一般norm補題：K可換field、sigma6Id、a0!=0/sigma³a0=a0、P=a0*sigmaa0*sigma²a0、rho≠0 fixedならL=K[X±;sigma]/(X6−rho³P)にはZ=(rho a0)^−1X²,Z³1の零因子。sigmaの最小位数は問わない。全根p³1,r³−1ではdehom t=p r²,c=−p/r²、XY−tYX=r alpha−r beta V²。delta(t−1)=r alpha、gamma(c^-2−t)=r betaを選べることが三次centralizer方程式の全条件。

### 全SL2 curved normalizing chart

全F∈SL2のcurved normalizing包絡[x,y]=alpha*u²+beta*v²、uv−、u作用F/v逆作用を、非対角±Jordan込みでH3認識した。全閉detF1で4PBW overlap、curvatureを純負cyclic quarticで加えるKoszul-Frobenius topからmu++--。非対角±Jの正三次shear核は全alpha/betaで定数minor6、必要Gはxuv又はx*(c x²+d u²+e v²)に限り因数分解。対角は既証3norm排除へ接合し、H3はF−I/零curvatureの既知signのみ。

canonical正top P=0の(2,2)/mixed rank4全H3を、全Jordan型・全幾何学的矢込みで既知非CY符号族に認識した。P0の正二次射影がrank1ならcross M rank2/rulingとなり、奇交代4像の純UV直線がimMに入って積関係を強制するためAS4domain外。正射影は自動非退化。Q0は既知zero-top認識、Q非零では負base q−1/±i、H_V単冪Id/正側shear固定G因子で全Jordan消滅。eps+はfiltered正常核零、eps−は対角量子/全SL2/Jordan正射影/四乗根weightを全被覆し非零Qを全排除。全H3は既知sign、一般dim2/inertia mu2²。

### canonical正top零の全認識

canonical正top P=0の(2,2)/mixed rank4全H3を、全Jordan型・全幾何学的矢込みで既知非CY符号族に認識した。P0の正二次射影がrank1ならcross M rank2/rulingとなり、奇交代4像の純UV直線がimMに入って積関係を強制するためAS4domain外。正射影は自動非退化。Q0は既知zero-top認識、Q非零では負base q−1/±i、H_V単冪Id/正側shear固定G因子で全Jordan消滅。eps+はfiltered正常核零、eps−は対角量子/全SL2/Jordan正射影/四乗根weightを全被覆し非零Qを全排除。全H3は既知sign、一般dim2/inertia mu2²。

rank2 cross補題：O=T Omega T^tの4次元交代像、L/N二射影rank>=3、rankM2なら両射影rank3。ell=kerNは等方直線なので純UV線Lell⊂L(ell perp)=imM。正projection rank1ならM=−(a^t⊗b)flipの像は固定正因子rulingで、純UV関係が積になる。従ってrank1境界も存在せずP0の非退化仮定は不要。標準3x3 minor det=z3 PfOmegaとPfOmega*e1=z5 col1−z4 col2が有限検算。

全非零Qの被覆ではcyclic cはq−1ならsquares、q±iならuv+qvu。正projection quantum p≠1はF/G対角、p1はdetF=−q^-1の全行列、JordanはF反復eig a²=−q^-1。q−1は既存curved quantum diagonal/fullSL2/shear384、q±iは10weight/28disjoint/primitive8 no−eig。全パラメータの境界を保つ。

### 全逆行列normalizing包絡のClifford認識

曲がったClifford全切断・全幾何学的矢の分類に加え、全F∈GL2の逆行列normalizing Ore包絡B(F,h)を全hでAS4/domain/mu++--と認識した。F²非Idでは正常条件をF固有直線商へ移して全G因数分解、FId核はL*(uv-h/2)、reflectionも定数minor16で共通一次因子を強制。従ってこの全行列族のH3はF−IdのClifford族に尽きる。B_hは係数独立/conic平滑の必要十分条件、全矢、一般dim5/慣性mu2まで確定。

B(F,h): positivecomm,u作用F/v逆作用,vu=-detF*uv+detF*h。F²neqIdではG=f3+Luv、FL=detF*L、(1+Sym³F)f3=-detF*L*Fh。Lneq0なら商U/kL上FIdで2f3=0、従ってLが共通因子。L0はbinarycubicfactor。FId核二列と補minor256、reflectionの非因子四列minor16（残る六列は指定四行零）をverify_cubic_order2_22_clifford_matrix.pyで検算。全Fの四PBW overlapも検算。

odd線型atlasのq≠1負separatedはB(F,h)へ帰着する。q−1 eps+のswap cross、負Jordanのshear cross、両comm時の反対separated f*g=−Idは別の必要chartであり、全被覆と正常核・因子の判定は `cubic_order2_22_rank4_zero_top_classification.tex` とその前後の認識節を参照する。

### canonical負top零の完全な幾何学的認識

canonical負topQ0の(2,2)/mixed rank4全H3を、全Jordan型込みで曲がったClifford族B_hに幾何学的認識した。半単純pure-positivecommの全odd atlasを一般F/swap/Jordan/両comm反対separatedへ必要被覆。pure-positive symmetric枝はp−1全atlasで正常核零又は一次因子。非半単純は非退化P/両JordanPf0/負片側/正片側固定核minor6で全排除。全切断は係数独立/conic平滑、全幾何学的矢、一般dim5/慣性mu2、h0符号部分族まで確定。

証明はcubic_order2_22_Qzero_commutative.texとcubic_order2_22_Qzero_complete.tex。新検証器Qzero_commutativeはswap正常rank10 minor4、負Jordan非x列minor16、両comm反対separatedのSL2全PBW/二scalar minor16とgraph辞書を再生。Qzero_completeは正対称分枝の四localized ideal一致、負Jordan Sym² fixed determinant−8二つ、両comm Sym²の2I恒等式、正片側Jordan yx=xy+eta*x²の全eta固定核補minor6を再生。従来zero-top eps+全核零/odd atlas/単冪untwist/片側Jordan排除を仮定付きで適用。Gのtwist輸送は使わず、元BでmuG固定を課す。

Pはcomm⊙q（q平方又は非退化）、Qはrank≤2 cyclic binaryquartic。まずQrank1がcross rank2 ruling障害でAS4domain外になるか確認し、rank2の三標準形と二本のcoupled even relationsから必要top/正常核を計算する。

### 両top非零の負rank1排除・tangent負分枝

正負topとも非零の残余で、負top rank1をcrossのruling障害により全Jordan型のcanonical包絡から排除。負topはrank2三型に限定。tangent型は二つのisotropic-factor割当てを区別し、六つの可逆cross線型atlasと逆割当て平方型のrank2 cross境界を確定。第一割当て/負Pfaffianの全半単純領域は、平方型の一軌道正常核零と非退化型全Tneq0の三minor gcdT10により空。

証明/certificateはcubic_order2_22_tangent_negativeのTeX/Python/JSON。非退化負PfaffianのT-parametrizationは(0,T^-1-T/4,-T/2,T/2,T,0)。元の288四次関係を消す35汎関数はLaurent多項式（分母定数*T冪のみ）であり、全係数恒等式を検証。正自由三次32語への正常式は64x32、多項式三10minor gcdは定数*T10。AS4正三次次元10と合わせ全核零。平方負分枝はz4非零を保存torusで1に正規化するので厳密一点消去が全軌道を覆う。AS4全係数存在、正Pfaffian、逆割当て、非半単純正常G輸送は主張しない。

残余torusでz5neq0は二パラメータmain chart、z5=0はz0=0/1の二一パラメータ境界へ被覆できる。平方型mainの一般quartic消去はNF分母Q*(P+Q)*((P+Q)²-2)、正常10minorは定数*P*(P+Q)^6*((P+Q)²-1)^3*((P+Q)²-2)^5（計算済み・公開certificate未整備）。ランダムな高次数minorのGBは重すぎ中止し、この有限直線分解へ切替。

元関係から使うatlasは、平方正mainが平方正main A=(1-PQ,-1/2,P,Q,0,1)。残余z5=0境界A=(epsilon,0,T,T^-1,0,0),epsilon0/1。nondeg正mainはA=(1-PQ,(P-Q)/2,P,Q,0,1)、同境界z1=(T-T^-1)/2。逆nondeg負はA=(0,(T+T^-1)/2,T,-T^-1,0,0)。

### tangent第一割当ての全半単純排除

負tangent第一割当てcU+u²,qU+uv+vuの全半単純H3を両Pfaffian・全境界込みで排除。正Pfaffianは全FSL2のS(F)[v;sigma,delta]へ必要被覆し、v-filtration grの非零片側curvature正常核を全Fで判定。±Jordan核は定数minor36で零に強化。traceF1のprimitive6共鳴だけ二次元正常核が残るが全Gは三生成元S内、既存三次norm零因子がmonic v商へ埋まるため全非domain。非退化qUはJordanなしなので全Jordan型込みで空。

証明はcubic_order2_22_tangent_plus_Ore.tex。verify_cubic_order2_22_tangent_plus_Ore.pyはqU平方/非退化の二つの全SL2 Ore表示について計8overlap、grの±Jordan二正常10minor36を厳密検証。既存curved_diagonalとprimitive6_nondomainのbeta0を適用。グラフF=[[-z2,z0],[-z5,-z3]]、detF1、grで正常Gがv次数0なら元GもS(F)内。Gv+vGからsigmaG=-G,deltaG0となりS/(G)がB/(G)へ埋まる。従ってfiltered domain性の逆推論やGのtwist輸送は不要。

M可逆の両JordanはPf0、負片側は既知排除。正片側H_U=J,H_VIdのA不変式はz5=0,z2=z3。平方正Pfaffianはz2=z3=±1,z0=0/1へ、平方負は既存一点軌道へ。Gはtwist輸送せず、canonical C3のH固定核がx*C2に入るかを厳密計算し、元BのmuG固定から一次因子を得る方策。

### tangent第一割当ての全Jordan型完全排除

負tangent第一割当てcU+u²,qU+uv+vuを全Jordan型込みで完全排除。半単純は全SL2 Ore表示/gr正常核とprimitive6三次norm。非半単純平方型はH_UJ/H_VIdのA不変式z5=0,z2=z3から五canonical軌道へ必要被覆し、全軌道でH固定三次4次元が左因子xC2（6次元）へ入ることを厳密計算。muG固定と右twistの同一ベクトル空間/x*B2=xC2により元Bでも一次因子。Gのnormal cutとしてのtwist輸送は使わない。

証明cubic_order2_22_tangent_Jordan.tex。公開verifierは元の六二次関係の全三次商でH作用を計算し、負Pf代表(-1/2,1,0,0,1,0)と正Pf四代表(e,0,epsilon,epsilon,0,0),e0/1,epsilon±1の各4/6/6包含を検証。固定核の包含はshear非零parameterに不変で、保存torusはkxを保つ。muB(G)=G⇒H4G=G⇒HG=G、B=C^(H^-1)のx*B2=xC2で因子を戻す。正常Gの輸送を仮定しない点が重要。

非退化qUは全Jordanなし/M可逆で二Pfaffian atlas、負分枝はA=(0,(T+T^-1)/2,T,-T^-1,0,0),Tneq0。平方型はcross rank2/tangent pencilで可逆graph法を使えず、奇投影はrank3,3の境界が残る。まず逆非退化負Pfaffianの正常核を全Tで判定し、Ore還元又はLaurent汎関数minor coverを探す。

### tangent逆非退化の負Pfaffian全排除

負tangent逆割当て/非退化正top/負Pfaffianを全Tneq0で排除。全graphは正x/yが負Vをf,gでnormalizeしfgId,detf=detg−1。xy,yxがu²/uv+vuを張るので負側Sym²Vが中心。補助x−y次数の奇成分に対しfの奇冪はdet−1でSym²を恒等にできず、包絡domain性と負二次式単射から正常三次が全て零。GWAの全高次被覆や有限標本外挿を使わない。

証明cubic_order2_22_tangent_reverse_minus.tex、検証器は同stemのPython。行列f=[[-T,(T-T^-1)/2],[0,T^-1]],g=[[-T^-1,(T-T^-1)/2],[0,T]]。fgId/det−1と自由負tensor上のf(a)=b,g(b)=a、Sym²FId+detF−1の矛盾idealを検証。補助Z次数は全六二次関係の斉次性から得られ、奇三次成分はx^n*t/y^-n*tへspanningできる。負高次環の普遍PBW性を仮定せず負二次式の単射だけを用いる。

非退化正topのatlasはA=(z0,z1,-z4/2,z4/2,z4,z5), z0z5-z1z4-z4²/4=1。z0=z5=0ではx/y opposite-normalizing,fgId,detf1を使う。全共鳴・零境界の判定は `cubic_order2_22_reverse_plus_cover.tex` を参照する。逆平方型はcross rank2 tangent pencilで別境界。

### 逆tangent正Pf共鳴の全正常pencil因数分解

逆tangent正Pfaffian/非退化正topの共鳴z4=1を全z0,z5境界込みで排除。z5neq0はbeta一param、D=(beta−1)(beta+1)(2beta+1)(4beta+5)非零で正常核2次元、二8minor gcdD²。明示ell*Q2因子identityが正常pencilへ非定数写像を与え、projective比例incidenceのproper閉像から全Dopenのpencilを因数分解。四D例外も元関係でrank8/因子像span2を再検算。軸交換で片零境界を覆い、二重零点はell³−theta*C*ell=x³+theta³y³で全因子化。全正常核零ではなく全cut非domainによる排除。

証明cubic_order2_22_reverse_resonant.tex。公開verifierは元関係の商座標、D外だけに極を持つこと、正常基底二列、二8minor gcdD²、六係数quadratic因子identityを検証。proper incidenceはell,q,c三射影変数に対するL(ell)qとWcのwedge比例式で定義する（直接等式はmultihomogeneousでないので使わない）。形式上零積も許すが、仮定H3の包絡domain性と正二次基底の単射が零積を除く。B3の全係数平坦性を仮定せず、商汎関数rankとH3のHilbert値により当該点で座標を同定。四例外はbeta1/−1/−1/2/−5/4のexact point。二重零点のC=−3u²/4−v²は負中心かつf固定でありnormidentityを全語で検証。新規性/独立査読未確認。

z5neq0 mainはA=(1+beta*t+t²/4,beta,-t/2,t/2,t,1)の二param。z5=0は軸交換でz0neq0を主chartへ移す。二重零境界は `cubic_order2_22_reverse_plus_cover.tex` の奇次数中心作用による排除に従う。

### 逆tangent非退化全分枝の全値排除

逆tangent非退化正topの全正Pfaffianを全値coverで排除。二param正常10minor分子(t−1)²(t+1)²、分母全因子の八例外曲線を新たな商汎関数/二minorで被覆、残り12有理点と二組の二次体共役を厳密再消去。唯一の正常一次元点(beta,t)=(1,−1)も(x−2y)*((x−2y)²+4v²)に分解。t1共鳴は既存全pencil因数分解、二重零境界はodd補助次数とf³−Idのlocalized idealでt1へ。これで負tangent型の未知は逆割当て/平方正topのrank2 tangent crossだけ。

証明cubic_order2_22_reverse_plus_cover.tex。検証器は二param全元関係の商汎関数の極因子、指定10minor（行毎分母を除きQQ[B,C]の多項式行列式で再検証）、八曲線それぞれ二minorと全極の平方因子除去多項式、有限因子の点集合への写像を剰余零で検証。curve群はC0,C−1,B±1,2B+C0,2BC+C²+1,4BC+C²+3,4BC+C²+4。有限実行は12有理点とQQ(sqrt2)/QQ(sqrt3)代表、全て正常核零ただし(1,−1)だけdim1で指定因子。計算はSYMPY_GROUND_TYPES=flint環境でexact実行、独立査読は未確認。正常核zeroの有限標本を全値へ外挿せず、全係数恒等式・例外cover・個別点を区別した。

### 負tangent型の全排除

負tangent型の最後の逆平方/rank2 cross境界を全値排除。非零Q rank2は負unipotentを許さず、rank3奇射影の正片側Jordanも純UV不変線が積になるためdomain外。半単純境界は純UV線正規化からA=(a,a,0,b,c,c)、六Pfaffian ideal(b²,bc)、幾何点b0/cunit/保存torus c1へ還元。正常汎関数の極a±1、二10minor gcda、三例外a0/±1も元関係で核零。従ってcanonical負tangent Qは全Jordan型込みで完全に空。

証明cubic_order2_22_tangent_rank2.tex、verifierは同stem。必要atlasは純UV p∈imM∩imAとrank2Aからp wedge rに書く。b²0は幾何点でb0であり、非被約底上の消滅は主張しない。A正規化後の四関係とO全列の一致は単位minor/多項式生成恒等式で全aに確認し、generic rankだけで特殊値を被覆したのではない。

### mixed rank4全Jordan部分の消滅

(2,2)/mixed rank4全H3の中山半単純性を証明。P0/Q0認識に加え、P,Q非零では負Jordanなし。非full graphは純mixed不変直線の積障害、full graphはH同変graph[[A,B],[0,A]]とx²=b(V)neq0から三次基底y³,xy²,yV²,xV²を用い、固定核がxV²に限られる。四rank6 minor=6*((A⊗A)b)_jが全chartを覆い、muG固定と同一ベクトル空間のuntwistで元Gにも一次因子。

証明cubic_order2_22_Jordan_complete.tex。Q非零単冪固定cyclicQの一般解det=−3d⁴/16なのでrank≤2ではrank≤1となりrank1禁止に反する。full graphのH可換化idealとdetA²、det(A⊗A)=detA⁴、三次固定作用の四6minorとH4固定核一致を検証。C3正基底のspanningはx²/yx置換とmixed graphから、independenceはAS4正三次次元10から。N(xy²)=2b*y+x(b−a)のyV²成分が2(A⊗A)bneq0なので固定GはxV²。元BでmuG固定からH固定へ移すだけでnormal cutのtwist輸送はしない。新規性/独立査読未確認。

負topの二型は、対称secant b1=u²+v²,b2=u²−v² と、非対称 b1=uv+i*vu,b2=uv−i*vu で表す。各R1=cU+b1,R2=qU+b2。qU非退化ではrho*(xy+yx)の残余係数rho≠0を保持し、rho=±1のrank2境界を可逆graphと分ける。正規形・全Pfaffian式は `cubic_order2_22_nonsymmetric_complete.tex` と `cubic_order2_22_secant_negative.tex` に従う。

### 非対称負topの全排除

非対称負top Q=uv⊗uv+vu⊗vuを全正top/全Jordan/全cross境界込みで完全排除。二つの等方因子uv±i*vuの割当ては負軸交換で同値。全可逆crossの閉/局所化六線型atlasで正Pf枝はA0矛盾、負Pf枝はuの正側作用F²=−iIdへ正規化。uv,vu正二次式とF(b)=aからu²v=−vu²、u4はUと反交換/Vと可換、正常三次がu4と可換かつ反交換となり零。rho±1のrank2 crossもPfaffian ideal(a²,ac,b,c²)で幾何A0となりdomain射影rankに反する。

証明cubic_order2_22_nonsymmetric_complete.tex、同stemの公開verifierは四つの閉/局所化ideal一致、M行列式、二正規化graph、F²−iIdと自由positivequadのF(b)=a、shearによるz0除去、等方因子交換と特異全Pfaffian idealを厳密検証。平方負枝s²=i、nondeg負枝z0z5=i(rho²−1)であり、rho*(rho²−1)を単元としたideal一致を使うため未処理特殊値はない。特異rho±1は別rank2 atlasで処理し、nilpotent baseまでa/c零とは主張しない。Bdomain上のu4共役作用による核零であり、Rdomainの一般論やtwist輸送を使わない。

b1=u²+v²,b2=u²−v²、R1=cU+b1,R2=qU+b2。平方qU=x²の負Pf枝はA=(-s,t,s,s,t,0),t²−s²1、s=(w-w^-1)/2,t=(w+w^-1)/2で全wneq0を一param化する。全正常核の排除は `cubic_order2_22_secant_negative.tex` による。正Pf平方枝はA=(z0,-z4,-z3+z5,z3,z4,z5),z0z5−z3²+z3z5+z4²=1。非退化qU=rho*(xy+yx)ではrho≠0,±1の二Pf線型atlasとrho±1 rank2 secant boundaryを分ける。相対rhoや境界cを勝手に尺度で除去しない。

対称secant atlasではrho≠0,±1でalpha=(rho−1)/(rho+1)。正PfはA=(z0,-z4,alpha*z3,z3,z4,z5), Pf式z0z5+z4²+alpha*z3²=1−rho²。負PfはA=(0,z4,-alpha*z3,z3,z4,0), z4²+alpha*z3²=1−rho²。rho1 rank2/p=xv+yu正規化ではA=(a,a,0,b,c,c)、全Pf idealは(a²−c²,ac+c²)、幾何点ではa=−c,c≠0となる。p正規化後はcを尺度で1にできず、b,c二係数を保持する。全atlasと排除は `cubic_order2_22_secant_negative.tex` と `cubic_order2_22_secant_singular_cross.tex` による。

### 対称secantの全負Pfaffian排除

唯一残る対称secant負topの全必要odd atlasを確定し、二つの可逆cross負Pfaffian分枝を全値排除。平方負枝はconic t²−s²1のw=t+s!=0 parametrization、全quartic汎関数がLaurent係数で四正常10minor gcd定数*w13。非退化負枝は全conic上のopposite normalizer fgId/det−1、xy/yxがu²/v²を張り負Sym²全体が中心となるため奇補助次数中心作用で核零。正Pf二枝とrho±1 rank2secant境界の必要atlasを保持し、境界b,cは勝手に尺度除去しない。

証明cubic_order2_22_secant_negative.tex、同stemの公開verifierは四つの閉/局所化linear ideal一致、rank2 Pfaffian ideal、非退化conicのfgId/det−1とxy/yx二次係数det−1/rho、平方全wneq0の元quartic関係汎関数と四minor gcdw13を厳密確認。Gaussian値でのrankはminor位置の設計にだけ使い、最終公開証明はQQ[w]多項式恒等式と全値gcdで完結。新規性/独立査読は未確認。

yshearでz5=q!=0 chartはA=((1−t²)/q,−t,q,0,t,q)の二paramへ還元。z5=0はz4²−z3²1、z3!=0ならshearでz00、z3=0ならz4±1/z0任意の境界を別に保持。非退化正Pfはrho非zero/±1と三係数quadric、rank2境界はA=(-c,-c,0,b,c,c),c!=0。

### 平方secant正Pf共鳴の全pencil因子化

対称secant/平方正top/正Pfaffianのz5neq0共鳴z4=1/2を全パラメータで排除。yshearでz3=0へ全被覆しq=z5neq0。正常rank8二minor gcd定数*q10、六係数因子式(x+theta*y)*Q2が正常、theta係数行列の一2minor=256*q8で全q非零に非定数pencil写像。四次汎関数の極q±iはGaussian体上で元関係を再消去しrank8/因子像span2。properなprojective比例incidenceと包絡domain性により全正常pencilが一次因子を持つ。

証明cubic_order2_22_secant_square_resonant.tex。検証器と小入力JSONはnormal two-minor位置、quadratic factor六係数、因子像rank2minor位置を含む。共通original-relation linear algebraは公開cubic_order2_22_secant_tools.pyへ分離し、nf3/nf4の各元関係消去恒等式も毎回検証。N kernelの特定二列に座標化すると4q⁴+12q²+3という不要な分母が出るが、それは選んだ座標の退化であり、因子像theta係数行列のunit minor256q8を使えばそのquartic例外を作らず全pencilを覆える。新規性/独立査読未確認。

A=((1−t²)/q,−t,q,0,t,q),qneq0。全二param消去ではNF3分母2q²t、全NF4分母に複雑curveも出るが、正常minorに使う7汎関数(j=4,5,6,9,13,14,19)の極はq*t*(t²−1)*(q²−4t²+2)だけ。単一正常10minor=(2t−1)^4(2t+1)^4(2t²−1)/(16*q*t³*(t²−1)²*(q²−4t²+2)²)。全NFの追加分母は、この7汎関数を使う正常小行列式には不要である。残るF=q²−4t²+2=0はw=2t+qでt=(w+2/w)/4,q=(w−2/w)/2の有理一param。t=0,±1の各直線とq=0は別の境界として扱う。

### 平方secant正Pf主chartの全値排除

平方正top/対称secant負top/正Pfaffianの全z5neq0主chartを全値排除。選択六四次関数の極q*t*(t²−1)*(q²−4t²+2)のみ、正常10minorは−(2t−1)³(2t+1)³/[16q t³(t²−1)(q²−4t²+2)²]。五有理曲線を二minorで被覆、Gaussian有限点ではt0核零/t−1/2唯一正常三次もx+2yを因子に持つ。残るconicの12次既約例外P(w)は厳密12次数体で元288四次関係を消去しrank10、全共役を同時に排除。t1/2全pencilは既存因子化と接合。

証明cubic_order2_22_secant_square_main.tex。verifierは共通secant_tools.normal_freeで全32自由正三次の正常式を作り、三次のgeneric座標基底を特殊値へ仮定しない。五curveの実際に使うquartic functionの極と二minor gcdの合併を調べ、定義域外と既知t1/2を除く残余因子をGaussian点、既知t0曲線、12次既約Pへ剰余零で写す。P=w12−12w10+28w8+96w6+112w4−192w2+64。QQ[alpha]/P上のR係数をQQ(w)の分子/分母からnative ANPで評価し、SymPy式へ12次根を大量展開せず256語商を消去、B4dim35/normalrank10を全元関係annihilator恒等式付きで検証。実行はoptional Flint exact ground environment、近似根計算なし。Gaussian唯一cutは(x+2y)*(-x²/2+xy+yx+2y²−i(uv+vu))、共役も同じ左因子。新規性/独立査読未確認。

### 平方secant全境界と平方正topの全排除

平方正top/対称secant型の全境界z5=0を排除し、既存の主chart・負Pfaffianと合わせ、この型全体にH3がないことを証明。三有理曲線の二minor gcd cover、Gaussian/三次根の厳密再消去、唯一の原始六乗根正常pencilの明示的一次因子写像で全値を覆う。

証明cubic_order2_22_secant_square_boundary.tex。s!=0ではa0にshear正規化しw=t+s、s=(w-w^-1)/2,t=(w+w^-1)/2の一curve、s0ではt±1/a任意の二line。正常10minor二本と使用汎関数の極から有限例外はconicのw²+1,w²±w+1と二lineのa0だけ。Gaussianと原始三乗根及びa0は正常核零。原始六乗根は核2で、r²=-3としてQ2=(-3r theta²+2r)x²-r theta(xy+yx)+2r theta²y²-3(theta²+theta)uv+3(theta²-theta)vuが(x+theta y)との積を正常にする。theta係数span2を厳密検証しproperな射影比例incidenceで全正常pencilを覆う。二次体の共役も同時に覆い、全cutに一次因子。新規性/独立査読未確認。

### 対称secant特異混合blockの全排除

対称secant負topのrank2混合block境界を全二パラメータで排除。最高テンソルの像の四列はminor4c²で全c非零の関係基底となり、正常10minorが−32c5というLaurent単元。平方正topを排除した後の必要層は、非退化正top・対称secant負top・正Pfaffian・混合block可逆のquadricである。この層の全値排除は `cubic_order2_22_secant_L_complete.tex` へ至る各境界判定を用いる。

証明cubic_order2_22_secant_singular_cross.tex。rho1のatlas A=(-c,-c,0,b,c,c)を保持し、cを消す誤った正規化を用いない。交代8block Oの列0,1,2,4をCとし行0,1,2,4のminor4c²とC*T=Oを厳密検証。元六二次関係から四次商を消去すると一般次元35、正常32列に一つの10minor−32c5、実使用汎関数はc冪だけを分母とする。よって全値でrank10、AS4正三次次元10から正常核零。rank2の奇関係境界とは異なるため、新verifierをsecant_singular_crossと命名して区別。q!=0を正torusでq1とした三param chartと、q0の境界を保持して判定する。

### 非退化secant二重零境界の全排除

非退化正top/対称secant負top/正Pfaffianのa=q=0二重零境界を全値排除。逆作用F/F^-1と負対称二次中心から補助次数±1の正常成分を消し、±3成分はtraceF1のx³,y³だけ。全pencilは(x+theta*y)(x²−theta F²(A2)+theta²y²)=x³+theta³y³で分解。x/y交換でq0,a非零をq非零へ移せるため、両top非零mixed4(2,2)の未知はq1の三param主chart一つだけ。

証明cubic_order2_22_secant_doublezero.tex。負部分Tのu²,v²,{u,v}が中心、B2で独立。補助次数±1のxQ2/yQ2が正常ならQ2は−Fをintertwineし、対称二次中心のdomain cancellationでSym²FId⇒F±Id⇒rho0という矛盾。±3はF³−Idが必要でSL2/非scalarよりtraceF1に限る。共鳴正常pencilは全て明示normで分解。F(A2)=B2と逆作用は円錐曲線の多項式恒等式として検証、元三次関係で数体fiberのnormも検算。大きなrrefを無制限に反復しない。

### 非退化secant共鳴面の全値因子pencil

非退化正top/対称secant/正Pfaffian/q1主chartの共鳴面2t+rho²−1=0に、全AS4domain fiberで全て分解する正常pencilを構成。明示多項式Q2の係数ideal単元、generic正常恒等式と像rank2を最大rank三次/四次商の局所自由性で全AS4fiberへ延長し、domainと次数により像rank2を保証。正常8minorと使用汎関数の極から(rho²+1)(rho²+3)(rho²−9)D E非零の全開集合では正常核全体がそのpencil、H3なし。

証明cubic_order2_22_secant_nondegenerate_resonance.tex。D=r4+2r3+4r²+6r+4s²+3、E=r6+4r5+7r4+8r3+4r²s²+7r²+12rs²+4r+1。因子六係数は最小JSON入力へ保持。係数ideal＋z*r*(r²−1)−1のGroebner基底1。generic商B3dim20/B4dim35の最大rank開集合は全AS4fiberを含み、その局所自由余核で正常恒等式と3次外積零が延長する。domainならQ2のz共通因子を除いた積が常に非零で、像rank1以下は正次数scalar polynomialの零点で矛盾。従って全fiberで分解pencil2を得る。

### 一重零全排除と共鳴例外二曲線への還元

非退化secant正Pfの全aq=0領域を排除。二重零環をOre基底Tの一般化Weyl代数として構成し全値domain/Hilbert14641を証明、一重零a0の補助次数先頭環と同定。正常核は非共鳴0/共鳴高々2、全値因子pencilで残りも排除。共鳴面は三追加minorとE,F4,J6 ideal=(s²,(rho+1)²)、一点(-3,0)の厳密再消去により例外rho²−9/E/Dを全て閉じ、残るのはrho²=-1,-3の二つの数体上一param曲線だけ。

証明cubic_order2_22_secant_resonance_cover.tex。T=k[u,z][v;sigma,delta], vu=-uv+z,vz=zv,degz2。任意GL2VがTを保ち、A2中心/非零。T[X±1;F^-1]にx=X,y=F(A2)X^-1を置くWeyl表示でBdoublezero≅T⊕ΣTx^n⊕Ty^n、Hilbert1/(1-h)^4/domain。a0,q1はauxdegx1/y−1/V0でqtermだけ2低いのでgrBへdoublezeroから全射、AS4Hilbert同値で同型。gr正常核単射から非共鳴zero、共鳴dim≤2、既存全値normpencilが全kernelを覆う。追加minor三本は単元除去後(r+3)E,s²F4,s²J6、ideal(E,F4,J6)=(s²,(r+1)²)。残余(-3,0)もfresh original R4でrank8。D0=a0既に排除なので共鳴残余はr²=-1,-3だけ。

### 非退化secant共鳴面の全値排除

非退化正top/対称secant/正Pfaffianの共鳴面2t+rho²−1=0を全値排除。三変数の明示多項式四次汎関数8本が元288関係を消す恒等式を直接検証。残余rho²=-1,-3で正常8minor三本のgcdはs³、s³*(s²+(2−2sqrt−3)/3)。Gaussian s0はB4dim36で非AS4。残る有限点はQQ(sqrt3,i)で元関係再消去しB4dim35/正常rank8、全共役を覆う。全値因子pencilが全正常核となりH3なし。

証明cubic_order2_22_secant_resonance_final.tex。FLINTの有理関数体上の疎消去で三変数B4dim35と全元関係annihilatorを取得。分母leading coefficientを1にする正規化で有理unit係数の巨大化を防ぎ、八つの汎関数だけを多項式化/primitive化して174KB JSONへ保存した。公開checkerは生成アルゴリズムを信頼するのでなく、六二次関係の全位置・全外語288行をその多項式汎関数が消すことを直接QQ[r,s,t]で検証する。両残余curveで行のs冪だけを除き三minor gcd cover。sqrt−3最後の点s=(1+r)/sqrt3は四次体QQ(sqrt3,i)の埋込みで全符号共役を覆いfresh正常rank8。

### 非共鳴主chartの開集合排除と四残余曲面

非退化secant正Pf/q1主chartの明示開集合で正常核零を証明。八多項式四次汎関数の元288関係annihilatorに加え、正常10部分行列Cの多項式右逆証明CX=dI10を公開。d=r³*s*t²*(r−1)^5*(r+1)^6*(r²−2t−1)*(r²+2t−1)*L。既存の全aq0/全共鳴排除と合わせ、両top非零mixed4(2,2)の未知はs0,t0,r²−2t−1=0,L0の四曲面（a非零/非共鳴）だけ。

証明cubic_order2_22_secant_main_open.tex。L=r5+r4+2r3s²+2r3t²−2r²s²+2r²t²+2rt²−r+2t²−1。73KBの明示polynomialXでCX=dIを直接検証するため、生成に使ったFLINT消去や多変数detを再実行する必要はない。全正自由三次32列の正常条件が元三次関係を消すことと正三次商次元10から、全開集合で正常核零。公開polyλはprimitive化済みで元288行を直接消すため、特殊値にもそのまま有効。

### 二座標曲面の全値排除

非退化secant正Pf/q1主chartの座標曲面s0,t0を全値排除。元288四次関係を消す追加多項式汎関数と正三次関係24×32行列から、局所化係数環でK=kerT3/正常行加群Fを比較。t0はK=F、s0は(t+1)K及び(rho²+1)KがFに所属。AS4最大rank開集合で核の底変更を使い正常核零。残るs0,t−1,rho±iは元関係でB4dim36、非AS4。未知は鏡共鳴rho²−2t−1=0とL0の二曲面だけ（a非零/真共鳴外）。

証明cubic_order2_22_secant_coordinate_planes.tex。Singularのsyzygyは商環k[parameters,z]/(zU−1)上で計算する。行列積は商環で自動的に正規化されるとは限らず、R3*E及びR3*Nの零検査をreduce(ideal(product),std(ideal(0)))で行う。module==0は列数付き零表示と一致しない場合があるのでsize(reduce(module,...))==0で判定する。所属はt0でE⊂N、s0で(t+1)E,(r²+1)E⊂N。N⊂Eは元四次annihilatorから独立に確認。AS4正三次商10/maxrank22開集合でkerT3のfiberが全双対となるため、全閉値の正常核判定へ適用できる。

この加群計算の再現にはSymPy、python-flint、Singularが必要である。`SINGULAR_BIN`で実行体を指定できる。実行環境固有の一時パスやキャッシュを入力として要求せず、公開コードと小証明書から再生成する。

### 鏡共鳴の縮小と唯一の残余L曲面

鏡共鳴t=(rho²−1)/2でBm*Jm*K⊂正常行加群Fを局所化加群として検証。Bm=4s²+(rho−1)(rho+1)³は全有理param rho=(1−w²)/(1+w²),s=2w/(1+w²)²で覆い、正常10minorが単元以外にw4−w²+1だけを零点に持つ。その残余はJm=16(w4−w²+1)/(1+w²)^4=0なので、鏡共鳴の全候補はJm0へ。L|mirror=(rho−1)J_m/2を用いると、鏡共鳴と主chartの必要支持を一曲面L=0へまとめられる。その排除は `cubic_order2_22_secant_L_complete.tex`。

証明cubic_order2_22_secant_mirror_support.tex。K=kerT3のsyzygyと正常行Fで(Bm*Jm)K⊂Fを直接Singularで検証し、Annの巨大な標準基底を再現する必要をなくした。Bm曲線の有理paramは逆w=2s/(rho+1)²、w(w²−1)(w²+1)非零。FLINTの一変数四次消去でB4dim35/全元annihilatorを得て、必要な多項式汎関数だけを小JSONへ保持。公開checkerはその全288恒等式とnormal10minorの全根因子をQQ[w]で再生する。残余w4−w²1=0は3rho²+1=0でありJm曲線との交点なので、独立に排除済みとは扱わずJmへ含める。

固定点から因子を外挿する方法の障害：Jmの二枝はs=±i(rho+1)(rho²+1)/(2rho), t=(rho²−1)/2。rho(rho²−1)(rho²+1)非零を仮定する。rho2,s15i/4,t3/2では元関係の三次/四次商は20/35、正常rank9で核一本、正一次因子の条件は(3theta+4i)^3=0なのでx−4i*y/3が因子となる。しかしこの一点から推測したbeta=−2i*rho/(rho+1)は、Gaussian有理関数体上でNL(beta)のkernelが零となるため一般式としては誤りである。交点3rho²+1=0のrho=i/sqrt3,s=(sqrt3+i)/3,t−2/3も四次商35/正常rank9となるが、有限個の値だけで全曲線を被覆しない。全曲線の結論は `cubic_order2_22_secant_mirror_J.tex` を参照する。

L0の非鏡領域ではrho²+1=0はs0へ帰着する。rho²+1非零ではL上の真共鳴有理点t0=(1−rho²)/2,s0=i(rho+1)(rho²+1)/(2rho)から、傾きk=(s−s0)/(t−t0)を使う有理表示が得られる。D=rho²(rho−1)k²+(rho+1)(rho²+1), E=(rho+1)−i*rho*k, Q=−D+2(rho²+1)E と置き、t=(rho²−1)Q/(2D), s=s0+k*(rho²−1)(rho²+1)*E/D。全被覆の正則逆写像と分母条件は `cubic_order2_22_secant_L_parameter.tex` の座標を正本とする。rho3,s10i/3,t1では三次/四次商20/35・正常rank10であり、L=0という必要支持だけで全点の正常核非零を推論できない。

### 鏡共鳴面の全排除

鏡共鳴の最後のJm曲線の全正常切断を排除。両枝s=±i(rho+1)(rho²+1)/(2rho), t=(rho²−1)/2で、b=−2i*rho/(rho²−1), Q2=x²+b(rho²+1)(xy+yx)+b²y²+2rho²/(rho²−1)*(uv+vu)としG=(x+by)Q2。35明示多項式四次汎関数と一点B4dim35の上下界からgeneric商次元35、正常恒等式をAS4最大rank開集合へ延長。三normal9minor gcdと3rho²+1=0のfresh数体rank9で全正常核一本を保証し全cutに一次因子。鏡共鳴面全体が空、未知はL0の非鏡領域だけ。

証明cubic_order2_22_secant_mirror_J.tex。正しいtheta条件は((rho²−1)theta+2i*rho)^3であり、一般betaの分母はrho+1でなくrho²−1。Q2係数は入力へ明示しQxx1なのでdomainで非零。35多項式quartic annihilatorの指定35自由語への対角minorが非零、rho2の厳密B4dim35からgeneric四次商35をrigorous上下界で得る。Gの正常commutatorを全部消すためgeneric正常、係数regularかつAS4最大rank余核局所自由で全AS4fiberへ延長。kernel上界normal9minor三本gcdはbaseunitと3rho²+1だけ、交点はQQ(sqrt3,i)上で元R4を再消去しrank9。この証明は全値cutのfactorであって単なるgeneric排除ではない。

rho²+1=0ならLがrho²(rho−1)s²の定数倍でs0に入り既に排除。補助的な二param表示は D=rho²+1−(rho²−1)z², Q=rho²+1−2(rho²+1)z+(rho²−1)z², H=Q+4z, t=(rho²−1)Q/(2D), s=i(rho+1)(rho²+1)H/(2rho D) である。この式単独を全域被覆の証明とせず、分母と例外点を含む最終判定は `cubic_order2_22_secant_L_complete.tex` を用いる。逆z=[2i*rho*s+(rho+1)(rho²+1)]/[(rho+1)(2t+rho²−1)]。a=(rho²−1)²*(Q²−2D²)/(4rho²D²)、delta_plus=2(rho²−1)(rho²+1)(1−z)/D、delta_minus=−2(rho²−1)z*((rho²−1)z−(rho²+1))/Dが候補恒等式。検証前に全被覆として使用しない。

## 6. CYの構造還元、零・二交換子の排除

外部入力の固定SHA・仮定は `as4_imports.json`。全CYの必要被覆と各具体表示の排除を区別する。零交換子の結論は `thm:cubic-CY-zero-commutator-empty`、二交換子は `thm:cubic-CY-two-commutators-empty`。

### 部分活性支持から全共有支持への還元

固定as4のIV1–IV13を必要条件として接続し、零交換子CYのH3では四単純基点で十二共有係数全非零が必要となった。部分活性排除の証明依存先はas4_imports.jsonに固定した。全共有の可逆主ブロックFT1–FT12と特異主ブロックの階数1・2は、対応する必要被覆・排除節で扱う。
全共有支持についても、固定FT1–FT12から既存P全値排除へ接続し、全主ブロック特異の階数1・2は固定as4の必要排除を適用した。これで零交換子CYを全排除する。既存 cor:h3-cy-commutator-reduction と合わせると、非可換CY包絡で残る交換子次元は1,2,3であり、三交換子beta型は既排除。上流全証明の独立再実装はしていない。

### 中心・ノルム障害による一括削減

一交換子・非共有Segreの二直線追加型は既分類skewだけに帰着し、二平方追加型の外側交換子九表示は全排除した。固定必要表示23個で商射影の全例外数体を再計算。残った内部型H_sの原始三乗根では、交差項abがあると中心三次は二元で可約。f=a²+b²でもa-局所化の三次シンボルはk(v)上の滑らかな有理二次曲線上で全剰余零、FaddeevとTsenにより分裂する。論文cubic_CY_one_segre_extensions節。既存skewの合同を再分類に含める必要はない。
三交換子混合の外積階数一（七係数全域）はcubic_CY_three_mixed_rank_one節で排除。dの個数濾過で[d^n,a]の先頭は2n(bc+μa²)d^(n−1)で、中心は基礎三元環に含まれる。その中心三次a³,ab²,ac²は共通一次因子aを持つ。
前者の有限2変数では、疎な商射影と中心小行列式の開被覆を試し、残余点だけ原関係へ帰る。中心零・共通因子・巡回分裂を先に調べ、包絡側の全自己同型の再分類を避ける。

### 全CY必要被覆の第二二次関係入力を局所全枝で検証

as4固定SHA6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0のNONDEGENERATE_CHARTとDEGENERATE_CHART_SECOND_QUADRICを必要範囲だけ輸入した。仮定：標数0代数閉体、P3上独立六二次式、rank6二次関係、像次元3。結論：独立な第二二次関係。接空間rank3/2の全Witt正規化、退化DC1–DC15の全整除枝と恒等特異/巡回pencil、非退化の一般対称Mの第二関係を本文へ通常証明付きで統合した。独立checkerでsyzygy rank10/parameter8、両非整除8線型条件、unit標的変換、二quadric、一般pencil行列式、恒等特異枝のrank3関係、一般16係数Tの外積、companion独立証拠−1、一般対称Mと交代部分除去をdefault Sympy exact検証する。
証明cubic_CY_second_quadric節、verify_cubic_CY_second_quadric.py/certificate。as4_imports.jsonに固定SHA/全entrypointと証明hash/仮定/外部入力の監査状態/本分類での独立計算範囲を登録。全CY_COMPLETE、CI22全chart、AS十分性、全同型、Veronese除外の独立監査までは輸入していない。

### 零交換子CYの全像をCI(2,2)へ必要被覆

固定as4のVeronese排除を必要範囲で輸入し、全元データを当repoで独立再生した。Veronese21積rank15、対称係数rank1/2/3→関係rank3/4/6、全CY混合25核/全57係数cyclicrank31/KKrank20、同変等長Φとsl2二作用、全六最大等方planeと10三次係数のintegrable kernel、全三次正規化、零三次自由積lower25、全八非零代表の線型解/残余ideal、前四実平方/次二unitideal、最後二の全Ga3orbit（Jac8/27,−72）/両符号をdefault Sympy exactで確認。二representativeの元Hilbertは独立GradedAlgebraでalpha(1,4,10,22)、beta(1,4,10,20,37)、全候補非AS4。上流の検証器と当repoの元関係からの独立検算を区別する。最小固定proof input19KBと新certificate/validatorを保存し、as4_importsにsourcecommit/hash/仮定/元audit pending/独立範囲を登録した。
通常証明cubic_CY_Veronese節prop:cubic-CY-Veronese-excluded,thm:cubic-CY-zero-commutator-CI22。CYc0は関係graphからSSrank6、その全対称化零が非退化Q関係。像次元r≤2ならrankr点の線型切断P^rを選び、Urestriction6dimからr2/fullVeronese像。rank1 symmetric3matrixを原始vector平方へ戻し、gcd/付値/次数から元U=Sym²Wを復元して上の排除に反する。従って像3dim。第二quadとrank6quadconeのfactoriality（z0prime,localLaurentpoly,素因子降下）から高さ1imageideal生成次数2、整CI22となる。全CI22上の包絡・切断分類やAS十分性ではない。
公開検証器・入力・証明書は `verify_cubic_CY_Veronese.py` と対応するJSON。全CY分類・全CI22代数chart・幾何証明の機械形式化・新規性は未確認。

### 零交換子CYの七必要対称射影型を全被覆

通常証明cubic_CY_CI22_projection_atlas節thm:cubic-CY-CI22-seven-projections、固定as4のQUADRIC_PENCIL_PROJECTIONSから必要幾何被覆だけ輸入。CI22二次鉛筆Q/P、T=A^-1Hの接形式退化条件q^tAT²q0から常時退化iffT²∈span(I,T)。最小多項式2で二根ならrank1/2関係不可から3+3直和二Veronese=D、重根なら自己共役N²0rank3でrank3関係a²,ab,b²と全syzygy(−bℓ,aℓ−bm,am)、ℓ,m mod<a,b>独立からL。非退化point側は一般対称M表示でbaseZ≅smoothconic(B=0)のr-cut長さ4、全三base-elimination恒等式を確認。超平面に含まれないことから線型全section埋込み、U=I_Z2、curvilinear長さ4の全分割1111/211/22/31/4で五型。これらは中山Jordan型ではなく対称射影基点scheme型である。
公開verify_cubic_CY_CI22_projection_atlas.py/certificate ：全七Uの21積rank19/二relation全kernel、全pencil determinant/T²criterion、五有限algebra乗算全kernel、binary quadratic syzygy rank22/nullity8、Lmarked関係全shear、一般M三basepoint恒等式、五symmetricM例のconic四次根型。as4_importsに固定sourcehash/全仮定/被覆だけのscopeを登録。全AS4係数normalform・切断・群oidは同時輸入しない、新規性未確認。

### 非skew標準CY chartの一般点の除外

papers/sections/cubic_pym_generic_exclusions.tex。Pymの指定標準chartでL(1,1,2)、R(2,2)、S(2,3)の非空稠密開部分とE(3)の非零変形は中心三次が零となる。全CY包絡の分類ではなく、一次資料のAS4/CY chartを入力とした結果。

- L112：weight filtrationのassociated graded skew環で、独立なp0,p1に対する中心指数は四成分が全て等しい必要があり、次数3では不可能。
- R22：Sklyaninパラメータ(2,3,−5/7)でQQ上に商空間B3,B4を構成。中心交換子140×20行列の20次小行列式280000000000/279926361≠0。外部AS/CY入力と核の上半連続性で一般点を除外。
- S23：Ore中心は基礎可換三変数環のδ不変式。divergence-freeなb=c=−1,d=0でδ:A3→A4の10次小行列式−243。一般点も単射。
- E3：CGG積の中心はkerX∩kerY。4Xの三次weightは全て1 mod4で非零。従って中心三次なし。

これでPym六つの標準CY chartの一般点として残るのはR13。特殊locus・交叉・他のAS4族は除外していない。量子Fermatと非CY符号型を保持する。

### as4からの限定的輸入と全パラメータ除外

固定SHA `60eacafa28156a5fc62f74eae004d64a84675f4b` のas4を使用した。正確な入力・hash・仮定・元の監査状態はresearch/as4_imports.json。README、plan、COVERAGE、CLAIMSと必要な証明本文を確認し、元の量子単冪42ケース・scalar大交換子・CY四交換子の三検証器を再実行して元証明書と一致した。全CY統合証明や全AS4被覆を独立監査したとはしない。

規約は **as4の右巡回ν=本稿μ^{-1}**。量子環で列積と行積が逆であることを確認し、右twist B=C^H に対してμ_B=μ_C H^{-4}を用いる。

papers/sections/cubic_as4_reductions.texで以下を証明した。

- H3包絡の中山固有値には次数3の積が1となる共鳴が必要。一種類の固有値λしかなければ、λ³=λ⁴=1からλ=1。従ってas4で未処理部分が残るscalar半単純部分−I,±iIの全Jordan層はH3には不要である。通常のdet μ=1は仮定しない。
- 半単純化Cと単冪Hに対して、W1(C^H)のFはH(F)=F、Fv=H μ_C^{-1}(v)Fを満たす。この輸送公式で、Cが量子多項式環なら正規化の対角性によりH=1。**量子標準半単純化を持つ全AS4部分のH3は既存31点・五型だけ**となる。非skew単冪持上げも含む全被覆の主張である。
- 中心二平面上の[u,v]=q(b,c)≠0というCY基底は、中心体上でWeyl環になるため全正規元が中心に限られる。全単冪持上げでもH3は存在しない。
- **任意の非零斉次二次導分δに対する普通のOre包絡 k[x,y,z][T;δ] はH3にならない。** W1の三次元Gは基礎可換環内にあり、R=(k[x,y,z]/G)[T;δ]。Ore軸P=πk[T]の自己Extは次元1,3,4,4,...となる。Rees/change-of-ringsと局所双対でline objectsのPに対するacyclicityを証明し、Tate解消を誘導して計算した。未証明のT局所化や有限rankからの高次外挿を使わない。
- 可換三平面を保つCY Ore基底の単冪持上げも除外した。微分体上の単純環K[T;δ]で正規元を局所化するとF∈k[x,y,z]、従ってHはTの線型shearだけになる。twist後も非零普通Ore導分δ−h Eulerなので上の障害が残る。
- as4の指定構造定理へ適用し、**CY標準半単純化の交換子次元が4以上なら、H3包絡は可換環だけ**と分かった。三交換子beta型を標準半単純化とする全持上げも除外される。Pym S23の非零Ore族は一般点だけでなく特殊値も除外された。

いずれもgraded/1周期の包絡に対する結果であり、as4の最小周期2・4のZ-algebraを直接H3へ移していない。元のheart・構造対象・反Serre orbitを同定しないまま周期性を内在的障害と読まない。

### proper楕円四次元Sklyaninの全排除

標数0代数閉体上、滑らかなE、degL4、sigma translationで位数nが∞又は1,2,4以外の標準Sを全排除した。g1,g2中央二次正則列のTHCR商と中山公式でmuS=id。n∞及び有限n>3は中心重みからZ3=0。残余n3はcentre z0..z3(deg3),g1,g2(deg2)、二つの六次完全交叉、Z3dim4、S1dim4、PIdegree3である。

一般norm補題：connected graded domain Bが正規中心Z上有限、PIdegree n>=2なら、Nrd:B1->Z_nはbasepointfreeなn次写像。射影normのpullbackO1=O(n)がampleなので像へfinite、従ってdimZ_n>=dimB1。等号なら射影全射、各Gは一次元ellのnorm、Cayley-Hamiltonでell times degree(n-1)へ分解する。商に零因子が生じる。よってCY・normal-centre-finite・PI3のH3包絡にはdimZ3>=5が必要。SklyaninN3は等号dim4で全Gが一次式×二次式となり排除される。射影norm P3->P3はdegree27。複素数への限定やgenericGへの限定は不要。退化非楕円Sklyaninや任意Zhang twistは含まない。

一次資料WWY1802.06487v2 Lemma2.9,Props2.11/2.12/2.18,Thm3.13を読み、regularseq/domain/centre/normalityを使用。as4最新429d8a3...は4entrypointsの現行概要とSklyanin/CY claimを参照したが新定理輸入なし。検算verify_cubic_sklyanin_rank_obstruction.pyは重みHilbert・a-invariant−1・rank9・K²1/3と、一般traceless3x3行列のnorm因数分解を厳密検算。全排除はprojective normの通常の証明であり有限標本からの外挿でない。第三者独立査読・形式検証・新規性確認は未実施。

独立な複素幾何補題も保持：商特異点だけのprojective Q-delPezzo上のorderがcodim1 AzumayaかつH1Lambda0ならgeneric Brauer類は零。traceでq0、quotientresolutionはKod−∞でrational、small quotient群GのH2(G,Z)=0をS3/Gから示して例外residueを消し、Br rational resolution0を用いる。Sklyanin排除にはこの補題へ依存する必要はなく、norm補題の直接証明を正本とする。

### 一般Zhang/cocycle twist包絡の排除

A noethKoszulAS4 domain、B=A^phi、eta=hdet phiとすると、W1(B)はphi安定なので非零eigen F(phiF=lambda F)を選べる。untwistするとFv=theta(v)F,theta=lambda eta^-1 phi muA^-1。このnormalizerはZAをpointwise固定する。量子QではNewton normalizerがdiagonalなのでphi diagonal、全Zhang twistsQのH3は既存skew五型31coordsだけ。単冪/半単純の仮定不要。

properSklyanin Sでalpha beta gamma非零かつ中央quadric pencilの4固有値distinctを明示仮定。Sym²S1->S2 injective（六関係の交代射影非退化）なのでtheta g1=g1,theta g2=g2はordinary quadraticformsの厳密保存。pencil作用素distinct固有値よりtheta diagonal±、関係式よりeven sign。phi scalar times signであり、非自明case(1,1,−1,−1)のtwistはrescale(1,−i b c,i c,b),beta=b²,gamma=c²でS(alpha,beta^-1,gamma^-1)へ同型。六関係を全係数で単元倍比較した。点Eの作用は二捩れtranslation、4tau不変なのでpropernnotdiv4のまま、前節norm排除で全ZhangtwistH3を除外。退化pencilには適用しない。

標準V4cocycle mu((p,q),(r,s))=(−1)^(ps)、degxiが4群次数を各一回持つDavies twistも除外。CYはsign group top hdet1（中央quadric正則列とtranslation THCRcanonicalから）とKoszulFrobenius topGdegree0により証明。centerはGgraded、中心成分F_gをuntwistするとnormalizer theta_g=alternating bicharacter sign、theta_g F_g=F_gなのでF_gはS^(theta_g)でcentral。新translationtau_g=tau−s_g(E2)がorder3の場合だけ存在し、3tau=s_gなので高々一つのg。従って中心3はn3又は6の時だけdim1、それ以外0。唯一の生成元は標準PI3centreのG-degree gのzi=xi³+xi*(centralquadric)、quadricはGdegree0、theta_gもcocycleも積xi*Qを変えないので全cubiccutsnondomain。

証明cubic_twisted_envelope_exclusions.tex、検証器twisted_envelope_exclusionsは全六符号関係・param式・centralpencil固有値差・alternatingprojection・cocycle16tableをexact確認。一次資料Davies1512.05717v2の(3.4),(3.5),(4.3)を読みgrading/cocycle規約だけ使用。Hyp4.1のinfiniteorder point/fatpoint結果を有限位数へ輸入しない。AS4性全specialをこの資料から無条件に推論していない。抽象有限群cocycle、任意twisting systems、退化/他exoticelliptic全体の被覆は未主張。

### Stafford型と標準cocycle全族の排除

Davies1502.06101§6.1の全許容領域T（alpha,beta,gamma!=0,+-1,alpha+beta+gamma+alpha beta gamma0）、d∈P1から指定二禁止値を除くS_infinity,S_d1,S_d2と標準Klein cocycle、循環変種は全てH3包絡から排除した。退化/他exotic楕円/全AS4の被覆は未主張。

全TでNakayamaは通常(-I,diag--++,diag++--)、cocycle後(-I,-I,I)。群作用により対角、平方関係からmu=lambda*sign、hdetmu1からlambda8=1、族Frobenius pairingの正則性と既約性で一定とし、QQの一点計算で定数を決定。低次数計算だけからAS4性を推論せずDaviesThm6.1.10を入力。全Tの五関係上でg1,g2は中央、除いたfiはmuで正規、残余中心二次qとfiはTHCRへの核の正則正規列。W1はTHCRへ単射（核ならG=ell q、q中央でellも正規一次となるがTHCRで不可能）。

point curveの二次式は中心g1,g2と異なる：v0²+v1²+v2²+v3²=0,(1+beta)v1²+(1−alpha)v2²+(1+alpha beta)v3²=0。WWY1802.06487v2 Definition-Lemma2.4,(2.5)のsigmaをE点(0:r:s:1),r²=−a(1+b)/(a+b),s²=b(a−1)/(a+b)で反復。第二反復の第一係数−4(a+1)(a+b)(b−1)非零から4tau!=0が全Tで従う。第三正規化座標の条件u3=2(a+b)(ab−3a−b−1)KLM,v3+z3=−2(a−1)L²M²,w3−z3=2a(b+1)K²L²。K=ab+a−b+3,L=ab+a+3b−1,M=3ab−a+b+1。K=M0は(a−1)M−(3a+1)K=−4(a+1)²で不可、L0上z3=1024(a−1)²(a+1)^6/(a+3)^5非零。正規化第三座標は全Tで非零なのでK²除去はregular sigma³への延長で正当化される。従ってsigma³=theta_e1 iffL0、chart欠落なし。固定点不在は正しいpoint curve二式で確認済み。

通常Sd1/Sd2のW1はL!=0で0、L0でdim2。L0を(alpha,beta,gamma)=(a,(1−a)/(a+3),(a+1)/(a−3))、a!=0,+-1,+-3で表示。Sd1はF2=x2Q2,F3=x3Q3、Sd2はF0=x0Q0,F1=x1Q1で、全a,dにおいて非零・独立。THCRのnormalizer付き三次の比はsigma不変、自由な六重商上degree2の切断へ入るのでdim<=2。両pencilは一次因子s x2+t x3又はs x0+t x1で覆われ、明示degree3 basepointfree写像P1->P(W1)が全射なので全Gfactor。Q0..Q3,H,H0の式はcubic_stafford_exclusions.tex。

残余CY cocycleSd2の中心群次数gをuntwistしてnormalizer theta_gを得る。h=g+e1による通常の符号Zhang twistはStafford同士へ移り、h=e1は(a,b^-1,c^-1),d'=−(d+1+bc)/(bc)で偶奇保存、h=e2は(a^-1,b,c^-1),d'=−(d+1+c)/c、h=e1+e2は(a^-1,b^-1,c),d'=(d−b+1)/bで偶奇交換。全六関係・pencil・禁止値の対応をexact検証。中心成分は変換先W1_gと線型同型。従って群次数0/e1/e2/e1+e2の中心三次はK/L/N/M=0でだけ各dim1、N=ab−3a−b−1。四曲線はTで互いに素。生成元はxj times群次数0のquadricで符号Zhang/cocycleでも因子が保たれ、全切断nondomain。

検証器verify_cubic_stafford.py（六QQ Frobenius/rank witness）、stafford_resonance.py、stafford_resonance_even.py（全係数factor identity）、sklyanin_order6.py（全T反復）、stafford_transport.py（QQ(a,b)中央二次24式、三符号関係・pencil・禁止値・六対のdisjoint Groebner）を実行。全specialへの延長とTHCR次元評価は原稿の通常の証明であり有限標本外挿でない。

### 低交換子as4表示の独立排除

as4のa45f834f51a00c47443b51caf66abaf4629546b9を四entrypointとCY統合/CI22概要、二重被覆DCC1・長さ四CF2/CF3・長さ3+1CT2の具体的表示について参照。全CY被覆やAS4存在/整域/noetherian定理は新規入力にしていない。二重被覆の二族h!=0は、H3包絡を仮定したKoszul AS4双対の最高次数汎関数をQQ(i)[h,h^-1]上で独立構成し、全次数四関係を消す恒等式と左右pairingdet=+-1/(2h²)を確認して全hのmu=idを得る。一般点rrefだけでAS4十分性や特殊fiber平坦性を推論しない。a²,b²の正規作用は互いに反対符号、N=a²b²のnormalizer=-Iなのでdomainでは奇数centre0。一般にNが-Iを実現するH3包絡ならmu(N)=-Nが必要。CF2/CF3とCT2の三つの固定表示も独立Frobenius計算でmu=id、中心3の140x20行列に非零20minorがあり全排除。検算verify_cubic_as4_double_cover.pyとverify_cubic_as4_curvilinear_fixed.py、原稿cubic_as4_low_commutator_exclusions.tex。表示の借用と独立検算を、as4全分類の輸入と区別する。

### TT22六表示の直接全排除

as4固定commit a45f834... のCY_ZERO_COMMUTATORS_CURVILINEAR_TWO_TWO_COMPLETE.tex TT1-TT3から六表示のみ参照し、全射影型の被覆/AS4十分性は輸入しない。C_r(r!=0,+-1/4)をq=(4r+1)/(4r−1)で表示し、四DiamondからPBW b^i d^j a^k c^l、中央変数z1,z2上の量子トーラスdb=q^-1bdへの忠実模型a=z1 b^-1−kappa q²b^-1d²,c=z2d^-1−eta b²d^-1を構成。kappa=1/(2(q²−1)),eta=2q(q−1)/(q+1)。z1=ab+kappa d²,z2=cd+eta b²中央。先頭z1^k z2^l b^(i-k)d^(j-l)の比較からcentre3はq³!=1で0、q³1でa³,b³,c³,d³のdim4。この条件は48r²+1=0。三乗根ではdivision量子トーラスがcentre上rank9、Tr ell0、Tr ell²/2=3(uvz1+wtz2)。Nrd ell=ell(ell²−3(uvz1+wtz2))がBのcentre3へ入り、非零ellのnorm非零なのでP3->P3全射、全Gfactor。centre有限/正規の別入力は不要。generic determinantの他の零16r²+1,16r²+3はcentre0であり、最終証明はmatrixchartでなく上の全q先頭項論法。

E_t(t!=0,-2),F_h(allh)ではb,dが正規、N=bdのnormalizerはE_tで−I+二乗零nilpotent（a->−a+(t+2)b/(2t),c->−c+4(t+2)d,b/d->負）、F_hで−I。normalizerの半単純部分−Iなら整域の奇数centre0という一般補題で全排除。三固定A,B,DもQQ(i)/QQ上でcentre3 rank20をexact確認。全表示のmu=idは、対称射影U固定のRとA0=半Hess(-z2z5+z3z4−z0z1+z5²)による非零w=R A0 R^Tが巡回−という256恒等式からAS4実現の下で独立に従う。AS4最高Koszul線にwが入り双対FrobeniusmuE=-Iになるためで、存在十分性を低次数rankから推論しない。検算verify_cubic_as4_tt22_c.py/tt22_remaining.py、論文cubic_as4_tt22_exclusions.tex。

### DS211第二層二族の全排除

as4同commitのDS1/DS2/DT1具体表示だけを参照。A_(l,r),l!=0,+-1/4は量子3平面S(b,c,d)上のcanonical Ore。q=(4l+1)/(4l−1),sigma=(1,q^-1,q),delta=(beta b²,u bc,v bd),beta=−1/(4l),u=−(16lr+1)/(2l(16l²−1)),v=8(l+r)/(16l²−1)。正規bのnormalizer単冪部分がa->a−beta bなので中心3はS3へ入る。十指数のcharacter gcdでScentre3はq3のみpurecubes三本、deltaG0からb³は消え、c³/d³はu0/v0のみ、同時零は不可。従ってBcentre3は48l²+1=0,r=3lでkc³、r=−lでkd³、他0。全Gfactor。例外B_rはc,d正規、N=c³dのnormalizer=-I+(8r−4i)E_baなので奇数centre0。AS4条件下のmu=idはA1=半Hess(-z1z4+z2z3−z0z5+z3z4)とRの非零反巡回最高tensorから独立判定。検算verify_cubic_as4_ds211.pyで四PBW diamond、全tensor係数、normalizers、三乗根comm、全十指数をexact確認。DS3の残余も下記の全値rank coverと忠実模型により排除済み。

### DS211列挙表示の全排除

DS3のT_h(h!=0),U_u(u!=0)はcentre3の最大minorを全関係から構成し、Tでは(8h+1)(16h+1)/(2^23 h6)、Uでは−2^29 u6(4u−1)(48u²+8u+1)。商座標分母はTでhの冪、Uで定数のみ。座標は全関係を消し自由列でidentityなので、AS4仮定の各特殊fiberでも真の基底となる。残るT二値とU二種の値（quadric二根はQQ(sqrt−2)）を再計算して全rank20。L_±i/4,PもQQ(i)上rank20、V0もQQ上rank20。CY判定は全256反巡回最高tensor恒等式で独立に行う。一般rrefの係数だけからAS4平坦性を推論しない。

V_h(h!=-1/16)のh!=0は平方根r²=−h、p=(4r−1)/(4r+1)で全被覆。a'=a+gamma b,x=c−r d,y=c+r d、alpha=p²/(2(p+1)²),beta=1/(2(p+1)²),gamma=p/(p+1)²。四DiamondでPBW b^i x^j y^k(a')^l。中央z1,z2上の量子トーラスxb=p^-1bxにy=z2 x^-1−p b²x^-1,a'=b^-1(z1−alpha x²−beta y²)で忠実に入る（補助重みz1=3,z2=1の先頭項が相異なる）。z2=xy+p^-1b²,z1=ba'+alpha x²+beta y²中央。先頭指数からcentre3はp³!=1で0、p³1すなわちh1/48でdim4。三乗根division rank9でTr ell0,Tr ell²/2=3(uvz1+(wt+u²/4)z2)。Nrd a'=(a')³−3z2a'/4とb³,x³,y³が中心基底、全linear normはBcentre3に入りP3->P3全射なので全Gfactor。h0は固定rank20で処理。これでDS3/DT1列挙の三固定・四1param・一2paramを全排除。この局所的な検算は上流の全AS4射影型の被覆・存在十分性の独立検証ではない。

検証verify_cubic_as4_ds211_remaining.py（全値rank cover）とds211_v.py（全平方根被覆model/norm）を実行。共有cyclic関数は有理式の展開後に零を比較するよう正規化し、既存A/B検証も検証器で照合する。

### 四単純基点FS4の全S(lambda,t)と標準Klein cocycleも排除した

proper部分は既証Sklyaninへ帰着、三つの退化曲線はS(1,-1,s)の正規二次N1=a²+d²,N2=b²−c²の積が−Iを実現するため奇数centre0。FZ2のQ共有係数族は六対とも可逆skew係数なので既存skew分類に含まれる。表示のみ参照し全四単純基点/全CY被覆は未輸入。

境界normalityはQQ(s)の三次関係moduleで八恒等式を証明し、係数分母はs,s±1のみ。最高反巡回tensor w=R A R^Tは非零かつKlein次数0なのでAS4実現の下で通常/標準cocycleともmu=id。全値AS4存在・平坦性をgeneric rrefから推論していない。原稿cubic_as4_four_simple_exclusions.tex、検証verify_cubic_as4_four_simple.py。

### 共有頂点係数零の残余O/H表示も全排除した

Oは四DiamondのPBWと正規a,bのcharacterにより中心三次がc³又はd³一本に限られる。正確な共鳴はlambda=-1/2,A²=-3/64でkc³、A²=-1/192でkd³、他0なので全切断分解。H0/H1は分母なし商座標と最大minor16384lambda^12(lambda+1)^9(2lambda+1)^4(4lambda+1)(4lambda+3)、三例外値のQQ rank20で全中心三次零。最高反巡回tensorからAS4仮定下mu=id。従ってFZ2/FZ4/FZ5/FS4列挙はskew部分だけが残る。全CY/四単純基点被覆は未輸入。
検証verify_cubic_as4_four_simple_remaining.py。AS4性を仮定して必要条件で排除しており、AS4十分性・全同型・full atlas coverageは輸入しない。中心rank coverは両generic投影の全関係消滅と自由列identityを確認し、分母1なので全特殊fiberへ適用できる。

### 十二共有非零P族のlambda=2切片を両符号・全r!=1,13/5で排除した

三次/四次商座標分母はr−1のみ、中心行列の二つの最大minorの分子Q(deg3),P(deg5)がQQ(i)[r]で互いに素なので全閉値rank20。元の二パラメータFT3全域の最高反巡回tensorも256係数で独立検証し、AS4仮定下mu=id。全Pの非空determinant openでもH3なしだが、全lambdaの例外集合は未排除。
検算verify_cubic_as4_four_simple_p.pyは全二変数最高tensor、一変数の全関係消滅/自由列identityと分母のr−1支持、最大minor二本の厳密gcdを確認。全P/全四単純基点/全CY被覆は新規輸入せず、FT3表示だけを参照。対角生成元変換だけではPの複素係数は消せない。二変数の一般Gaussian消去では係数膨張が大きい。正規元・次数3のcharacterと、全値小行列式の分母支持を先に調べる。

### 共有零O/Hの標準Klein cocycleも全排除した

Oは(r,s)を(r,−s)へ替えた同じPBW、r,s!=0,+-1の二十characterから全中心三次が純三乗一本以下となる（rs=1を除外しない）。H0/H1のcocycleはgeneric rank20、lambda−1/2でrank20、lambda−1/4/−3/4ではrank19でそれぞれd(d²−3c²),c(d²−c²/3)の中心一本。全候補分解。最高tensorのtwist pairing A^c=A diag(1,1,−1,−1,1,1)を全係数で確認しAS4仮定下mu=id。これで列挙共有零表示と標準cocycleのH3はskewだけ。
検証verify_cubic_as4_four_simple_cocycles.py。通常Hとcocycle Hでgeneric最大minorは一致するが特殊値のkernelは異なるため、通常の全値rank20を流用しない。二例外のrank19と明示factored generatorを別計算済み。

### 最初の共有係数FN3の七列挙表示も全排除した

L/MをB(1;h/4,0,f,0)へ統一し、四Diamond/Ore PBW、normal adのcharacterからh0,h²−1,h²−3だけへ絞る。h0ではbc−2f adが−Iを実現、他二共鳴では候補4/2本とaの交換子が単射なので全centre3零。F0/F1のgeneric最大minorはlambda^6(lambda−1)^(4+eps)(lambda+1)^(6+eps)(lambda²+1)^(2−eps)(lambda²−lambda+1)(lambda²+lambda+1)/2^(40+2eps)。商分母lambda,lambda±1,lambda²+1と全七例外値を合わせ、QQ/QQ(i)/QQ(sqrt−3)の独立rank20で全値centre3零。G0/G1/KもQQ rank20。全mu判定は最高反巡回tensorで独立。
原稿cubic_as4_first_shared_exclusions.tex、検証verify_cubic_as4_four_simple_first.pyとfirst_remaining.py。fn_matrixは全入力をSymPy exactへ先に変換し、整数e/16のPython float化を避ける。FN3の具体七表示のみ参照し、上流全chart被覆・AS4存在十分性・全同型は輸入しない。

### 第五係数零のM_p^0/M_p^1と固定N/Cも全排除した

generic中心minorは(3p+1)/(2^33(p−1)^11)と(p+3)(3p+1)/(2^23(p−1)^13)、商分母p−1だけ。p−1/3とeps1のp−3をQQで別計算し全rank20。N/CはQQ(sqrt−3)/QQ(i)でrank20、係数共役も含む。全AS4実現のmu=idを最高反巡回tensorで独立確認。
原稿cubic_as4_zero_fifth_exclusions.tex、検証verify_cubic_as4_four_simple_zero_fifth.pyを検証器で照合する。上流FZ2/FZ3/FB2の表示だけを参照し、AS4存在十分性・全同型・全chart被覆は輸入しない。第二共有HのQQ(lambda,p)消去は疎な関係行列とDomainMatrix内の商射影で試し、一段ごとの出力と上限を設ける。重いGaussian二変数Pの無準備な消去とは分ける。

### 第二共有FO2の二パラメータH_(lambda,p)を全値排除した

generic商分母lambda,lambda±1,p−1だけ、中心minor=lambda6(lambda−1)^4(lambda+1)^5 D1 D2/(2^40(p−1)^13)、D1=lambda²+(2lambda+1)p,D2=lambda²+lambda p+lambda+1。lambda1直線、D1/D2二曲線を全関係から別計算し、minor m0=(3p+1)/(2^33(p−1)^11),m1=−lambda7(lambda−1)^4(2lambda+1)^10/(2^40(lambda+1)^15),m2=−lambda17(lambda−1)^3/(2^37(lambda+1)^15)。最後(1,−1/3)をQQ rank20で排除。全中心3零、mu=idは全二変数最高tensorで独立確認。
原稿cubic_as4_second_shared_exclusions.tex、検証verify_cubic_as4_four_simple_second.pyを実行。疎なQQ(lambda,p)関係行列と係数体内のDomainMatrix商射影で全関係恒等式を保持。curveBの分数体detがSymPy HeuristicGCDFailedとなる場合は、行毎分母を払ったQQ[lambda]行列のdetと分母対角detの多項式交差積で厳密検証する。これは数学的例外でない。FO2具体表示のみを参照し、上流全chart/CY被覆・AS4十分性・全同型を輸入しない。

### 一般行列式零境界R_lambdaの全許容lambda・両符号も排除した

右Zhang twist A=D^psi に同次数の非零中心元q1,q2（psi指標chi1,chi2）があれば、Z(D)_n!=0は(chi1/chi2)^n=1を必要とする。Rを固定可逆基底とtwistでFG6のA_tへ移し、非零中央a²,d²の指標−1,+1から全奇数中心を消す。六関係・基底det・最高tensorとQQ[t]上の八中央恒等式を独立確認し、lambda1/±iも含む。これで第五係数零の列挙M/N/CとR±_1は全排除。
原稿cubic_as4_boundary_R_exclusions.tex、検証verify_cubic_as4_four_simple_boundary_R.pyを検証器で照合する。右規約 x*y=x psi^deg(x)(y) では At=(RのC基底)^(sigma^-1)、sigma=diag(i,−i,1,−1)。sourceの(1 tensor phi)関係表示をこの規約へ明示変換し、twistの向きを混同しない。中央二次a²/d²の恒等式はtを一切割らない。AS4の存在十分性・全同型・全CY被覆は未輸入。Zhang twistによる同値をintrinsic同型に置換せず、補助的な中心障害としてだけ使用する。

### 純虚境界FI2のJ_h両符号を全値排除した

全h!=0で商座標の分母はhのみ、中心20minorはeta+でi h9/2^11、eta−で(1−i)h10/2^7。両符号を別々に検証し、全hの最高反巡回tensorからAS4仮定下mu=idを確認した。h0はQQ(i)上の五次全関係行列rank966、dim58>56により独立にAS4から排除。
原稿cubic_as4_boundary_J_exclusions.tex、検証verify_cubic_as4_four_simple_boundary_J.pyを検証器で照合する。lambda=iは固定して両etaを直接計算した。h0を一般商射影の極のまま捨てず、五次Hilbert障害で処理。FI2の具体表示だけを参照し、上流全chart/CY被覆・AS4存在十分性・全同型は輸入しない。AZ2の二固定LではQQ(sqrt−3)上のcentre3は各dim1だが、中心元の因子性を決めずにOre coneの頂点障害を適用できる。証明は `cubic_as4_adjacent_L_exclusions.tex`。

### 隣接AZ2の二固定Lも排除した

centre3は各dim1で非零だが、B=S(a,b,d)[c;sigma]、sigma+³=omega I,sigma−³=omega² Iとなる。CYの自己同型Ore包絡でsigma³が非自明scalarのとき、中心三次は零、一次因子付き、又は純base cutの三場合となり全てH3を排除できる。三乗根の場合は純base切断R=(S/G)[c;sigma]の頂点P=pi k[c]が無限高次自己Extを持つ。
原稿cubic_as4_adjacent_L_exclusions.tex。一般cone補題はB=S[z;sigma] noethKoszulAS4、G∈S3 central regularで、Rees/local dualityから全line objectのPへのHom-acyclicityを得る。C=S/G上のkの最小解消を誘導しExt^n(P,P)=beta_n、1/H_C=(1-u)^2/(1+u+u²)が非多項式なのでbeta_n>0全n。未証明のOre open globaldimやGの因子性は用いない。有限入力はverify_cubic_as4_four_simple_adjacent_L.pyでOre輸送、base関係安定性、scalarcube、CY tensor、centre3 rank19と明示生成元を実行確認。因子探索は未決でもH3排除には不要となった。AZ2表示のみ参照、上流全chart/CY被覆・AS4十分性・全同型は輸入しない。

### 隣接AB3の全S_zetaとT_-2両符号を独立排除した

Sの元の四次全語行列はQQ(zeta)上rank219、成分分母zetaのみなので全zeta!=0でdimB4>=37>35。T^eta_-2=S_(-eta i/4)は全六関係の文字どおりの一致で確認。一般商基底の特殊化ではなく、元の全語行列のrank上界を使用した。
原稿cubic_as4_adjacent_S_exclusions.tex、検証verify_cubic_as4_four_simple_adjacent_S.pyを実行。AB2/AB3具体表示のみ参照し、Tのlambda!=-2、全CY/chart被覆、AS4十分性・全同型は未輸入。同じ計算を反復しない。有限体は必要なら探索だけに使い、標数零の証明としない。

### 隣接T全値の排除

AB2のT_lambda両符号を全lambda!=0,-1で排除した。lambda=-2はS_zetaとの文字どおりの同一性とdim4>=37、lambda=-1±iは両符号の直接QQ(i)計算でcentre3 rank20。その他はAS4実現でdim3=20,dim4=35と最高反巡回tensorによるmu=idを必要条件として使う。T1での厳密rank20と一般presentation-rank二場合分けによる独立な有限性証明も原稿に保持する。全値AS4存在を仮定しない。

三次・四次商射影は元の全語関係消滅と自由列identityをQQ[lambda]の実部/虚部恒等式で独立再生した。D3=lambda²(lambda+1)²(lambda+2)²(lambda²+2lambda+2)E、E=lambda^4+2lambda³+10lambda²+24lambda+16。共通複素因子の除去後D4=lambda³(lambda+1)^5(lambda+2)³(lambda²+2lambda+2)AB、A=lambda²+(-1+3i)lambda−2+2i、B=lambda²+(1−3i)lambda−4i。AS4 Hilbert値の非極点でのみ商基底と結論し、全値平坦性は推論しない。P4分母を実normへ戻すと不要な共役極を増やすため、複素分母を維持する。

64本全三次語から作る64×140転置交換子行列の各列を、D4との共通因子h_jだけで割る。独立検証器はh_j|D4とC_0 X=NをQQ[lambda]の実部/虚部多項式行列で検証する。Nの20列は異なる先頭行を持つ三角形で、対角零点支持はlambda(lambda+1)(lambda+2)(lambda²+2lambda+2)AC_*、C_*=lambda²+(2−4i)lambda−4i。H=ABC_*とnum H(f(lambda))は互いに素、f=-lambda/(lambda+1)。literalなgraded同型P=diag(1,-1/q,-1/q²,-1/q)P_(bd),q=lambda+1、detP=q^-4、P(f)P=Iにより二枚で全残余を覆う。従ってcentre3は零。負符号は形式lambdaを固定した係数i共役で証明書全体を移す。20本の三次語が全特殊点で商基底になるとは仮定しない。

再生verify_cubic_as4_T_projections.py 3 4、verify_cubic_as4_T_centre_lift.py。入力generate_cubic_as4_T_centre_input.py、出力整形export_cubic_as4_T_centre_lift.py。商射影・centre liftのJSON証明データを保存し、証明再生はSymPyのみ、Singular 4.4.1は生成にのみ用いる。GitHub正本から入力生成と証明の独立検証を再開できる。

これでAB2/AB3の隣接共有境界の列挙表示は全排除。Pはlambda2の全rと非空開集合のみ排除済み。

### 十二共有P全二パラメータの排除

FT2/FT3の全P_lambda,r両符号を排除した。全二変数商射影のD3=lambda^4(lambda+1)²(r−1)²、D4=lambda^7(lambda+1)³(r−1)³a、a=2lambda²+2lambda+1。全分母はFT2領域で非零。元の全語関係消滅と自由列identityはQQ[lambda,r]の実部/虚部でSymPyとFLINTの厳密多項式積により独立検証済み。AS4実現の商基底としてのみ用い、全値AS4存在を輸入しない。

20三次語の転置交換子行列からD4の約数の列因子を除き、40×280のrealificationを作る。独立検証した多項式AX=Nでは40三角pivotを持つ。r−1の因子を除く垂直例外の被約積g(lambda)は次数30、11既約因子であり、明示式は原稿とcubic_as4_P_full_certificate.json。通常stdの基底と係数追跡liftstdの基底の正規化は異なる。通常基底の対角がlambda,r−1のみでも追跡付き基底は余分なlambda因子を持つため、それを捨てずgへ全て含めた。この点を無検証で特殊化しない。

次数付き同型lambda'=-lambda−1, r'={a−(lambda+1)²r}/lambda², eta'=etaを全六関係で確認。生成元はdiag(1,−1/64,i lambda/[8(lambda+1)],−i(lambda+1)/(8lambda))P_(ab)、det=1/4096。FT2のd,e,f,r−1はそれぞれq²/lambda², q/lambda,−q²/lambda²,−q²/lambda²倍に移り領域を保つ。gcd(g(lambda),g(−lambda−1))はlambda(lambda+1)a(2lambda+1)(4lambda²+4lambda+5)の定数倍。従って元の領域では三直線lambda=−1/2,−1/2±iだけ残る。先に複素行列を特殊化してからrealifyしたQQ[r]上の三証明書を別々に作り、全r!=1で40三角pivotとAX=Nを独立検証した。両符号は形式変数を固定した係数共役で覆う。

再現verify_cubic_as4_P_projections.py 3 4、verify_cubic_as4_P_centre_lift.py。入力はgenerate_cubic_as4_P_centre_input.py。中心検証にはpython-flintを要し、再生成にはSingular 4.4.1互換CLIも要する。巨大な出力（一般lift約64MB）は作業領域のみとし、Gitには元の商データ、生成器、独立多項式再生器、係数gと全チェックのSHAを持つ小さい記録を保存する。生成時のSingular内A*X=Nだけで終わらず、元のP商座標から行列を組み直しFLINTのQQ[lambda,r]積で全残差零を確認した。単なる数値標本や有限体検査ではない。

生成法の要点：Gaussian分数体でなく各語実/虚を隣接させたQQ(lambda,r)消去で三次・四次商を取得。QQ(lambda)[r]上の関係module全体を先に消去するより、必要な商射影と正常行加群の局所化証明書を作り、元の関係への再代入で検証する。証明データは単項式係数列として保持し、巨大式のSymPy再展開を避ける。

### 零交換子CY skewと通常Qの排除

四生成元CY skew多項式環で全q_ij!=1なら、中心三次は零か純三乗一本だけである。PBW重みにより中心は中心単項式の線型包。2+1型は平方変数との交換からq_ij1を強制し、1+1+1型はCY行積との比較で欠ける第四変数とのq1を強制する。二本の純三乗が中心なら全六対が三乗根となり、各行の三つの非自明三乗根指数が全て同符号となる必要と反対称性が矛盾する。よって全非零中心切断は純三乗でnondomain。

FZ2のQについてR=U+K diag(rho)、q=(2rho−1)/(2rho+1)を元の式から確認し、四つのCY行積−1の分子がAB+lambda AC−(lambda+1)BC−lambda(lambda+1)/16で割り切れることを厳密確認した。q−1=−2/(2rho+1)なのでc=0。従って通常Qも全排除。標準cocycle後にq1が生じる場合はこの補題を適用せず、既存skew分類へ戻す。原稿cubic_as4_four_simple_exclusions.tex、再現verify_cubic_as4_Q_centre_bound.py。

固定as4 a45f834f51a00c47443b51caf66abaf4629546b9のCY_COMPLETE、CI22_COMPLETE、IMAGE_REDUCTION、VERONESE_EXCLUSION、NONDEGENERATE_CHART、QUADRIC_PENCIL_PROJECTIONS、DEGENERATE_CHART_SECOND_QUADRICの論理を読み始めたが、これらの全必要被覆を新規輸入したとはしない。現在は階数六の二次関係を持つ六二次式系の退化微分像から第二二次関係を得るDC1–DC15の全枝を独立に検証し、CI(2,3)/CI(2,4)が消える幾何的核心を監査する。次いでVeronese除外、CI22七射影型と支持分岐の必要性だけを監査する。AS4十分性や全同型はH3排除のために輸入する必要がない。

### 全零交換子CYのD/L二射影をH3から全排除

必要係数全被覆を既存二族排除へ接続した。通常証明cubic_CY_DL_cover節thm:cubic-CY-DL-cover-empty。Dはrank6markedAを二Veronese判別式へ正規化、全mixed22/γ0/二binary discriminant−1/4、SL2×SL2で内部標準形、rank8線型系が八係数zero、残六binomialを再現。domainが四係数pair非零を強制し、非零support二枝I/IIだけ。根R²=U/p又はR⁴=1/(p³r)のみの対角変更で(1,h,1,−h)全h非零へ。RS=TUも根idealで確認しmarkedA保持。元16語関係が既存D_I/II(h)と非零定数basis変換で全h一致し、thm:as4-double-cover-h3-exclusionで全排除。AS4存在十分性/全同型は輸入しない。
Lは全mixed22とSchurdiscriminant2(v1²−4v0v2)、一般四係数GL2でv変換Sym²T/det²を全tensorframeで確認、v0/平方v(1,0,0)の全二枝へ。v0はfree二元quotient、平方枝は全linear条件と四polynomiale_iの二恒等式から特殊zを除外せずu=w=p0、実a²sourcecolumnでdomain矛盾。全zero/非zero各場合の全値排除。
公開verify_cubic_CY_DL_cover.py/certificate （双方22核/混合cyclicrank14/全57係数rank34、D全normalization/全値旧表示移送、L全GL2・全分岐）。as4_importsは固定6f798...のDCC4–12/LBE2–10の必要範囲のみ登録。
残るCYc0の必要射影は有限基点五型1111/211/22/31/4。固定sourceCURVILINEAR_FOUR_COMPLETEの必要CF6–13、CURVILINEAR_THREE_ONE_COMPLETEの必要CT3–17を全文読んだ（AS十分性と全Autは不要）。CFは全mixed21、全Ga4/トーラスnormalization、四emptybranches、五先頭tupleCF13、うち二empty/一Hilbert4dim37/二fixed CF2CF3。CTはx0/x10非零empty、x9非零全有限/一parameterHilbert4>35、x9=0二cube恒等式でx11=x15zero、x12非零二族のgenericHilbert4dim37又はdegree5dim62（必要56）で全特殊値排除、最後x17unit枝CT14六式からx1nonzeroが唯一CT2、x1zero三族allclosedHilbert4≥39/39/42。全family原関係の分母は記載unitだけで、genericrank上界により全閉値でdim下界を用いるので、generic商基底の無条件特殊化とは別。
正常CF2/CF3/CT2自体の中心排除は既に済みで再計算不要。全候補必要被覆のmetadata/通常証明を追加する。

### 有限基点型4・31の全必要係数被覆とH3排除

通常証明cubic_CY_finite43_cover節thm:cubic-CY-finite43-empty。固定as4のCF6–13/CT3–17だけを必要被覆として利用し、全上流controlを隔離workspaceで検証器で照合する。当repoの独立default exact controlも：二つの全21混合frame、六空chart、CF先頭五tuple、全14非正則代表・族の元商次元、既存CF2/CF3/CT2への定数可逆な関係移送。非正則族の全閉値下界は、明記したunitだけを反転した元全語関係行列のrank特殊化で正当化する。CTのmu=-1例外は自由yも保持、x12境界は五次62>56を用いる。CF先頭消去式はv²(2v+1)(7v+1)であり、五tupleの幾何学的被覆を被約scheme/相対被覆と主張しない。
公開検証器・入力・証明書は `verify_cubic_CY_finite43_cover.py` と対応するJSON。固定source/hash/必要範囲をas4_importsへ登録。上流通常証明の全gauge被覆と当repo独立商計算を区別し、AS十分性/全Aut/新規性を同時輸入しない。
残るCYc0必要射影は1111/211/22。本文の必要枝は読了：全21frame、kappa非零二bad族(dim4=38/40)、kappa零mixed非零三bad族(dim4=39/42,dim3=21)、最終r=±1/4族(dim3=24)、実平方枝、六正則表示への全正規化。TT15以降のAS十分性/全Autは不要。

### 有限基点型22の全H3排除

通常証明cubic_CY_finite22_cover節thm:cubic-CY-finite22-empty。固定as4のTT1–14必要全係数被覆だけを利用。固定全controllerの隔離検証器で照合する、当repo default独立controlも：全21mixed/cyclicrank15、N/T/W印付き共変性、九つの非正則代表・族の元商(dim4=38/40/39/42、dim3=21/24)、六表示のliteral移送とA両符号。全自由係数閉値は元関係行列rank特殊化と明示unitだけの分母で保持。残るA/B/D/C_r/E_t/F_hは既存三排除定理で全H3なし。公開検証器・入力・証明書は `verify_cubic_CY_finite22_cover.py` と対応するJSON。AS十分性/全Aut/被約相対被覆/新規性は輸入しない。
CYc0残る必要射影は1111/211。固定DOUBLE_SIMPLE_NONZERO_COMPLETEのDS1–10、SECOND_COMPLETEのDT4–11、FINAL_EXCLUSIONの全DZ1–20を読み終えた。前二層の残存全表示L±/T/P/U/V/A_lr/B_rは既存ds211節で全パラメータ排除済みなので再計算不要。最終零層では元Hilbert5=57の二族、四次36の四代数点、Hilbert7=123>120のM0/M1族、その他degree3/4/5障害を含めて必要被覆を確認する必要がある。

### 有限基点型211の全必要被覆とH3排除

通常証明cubic_CY_finite211_cover節thm:cubic-CY-finite211-empty。固定as4のDS1–10/DT4–11/DZ1–20必要範囲を輸入し、元商の独立controlは全27代表・族を扱う。全21mixed/cyclicrank15、全N/T/W印付き群、D00=4x0x15、全非正則族の元商と全分母unitを確認。新しい疎pivot/右乗算だけの再帰商では各段階で全元関係挿入の座標像零も確認。最終零層22候補はHilbert5=57/60、四次36/39/42、三次21/22/23、二つのM族のHilbert7=123>120。係数共役も保持し、全閉値は元全語rank特殊化で下界保証。第二層5族も三次21/22。残る第一層全7表示と第二層二族は既存ds211の全パラメータ排除の元関係と一致。AS十分性/全Aut/相対scheme被覆は輸入しない。
公開検証器・入力・証明書は `verify_cubic_CY_finite211_cover.py` と対応するJSON。再現はSYMPY_GROUND_TYPES=flint python computations/verify_cubic_CY_finite211_cover.py --flint。
残るCYc0必要射影型は1111のみ。FZ2量子型Qもq_ij!=1のCY skewなので、既存lem:cubic-cy-skew-zero-commutatorにより全H3排除済み。全skew領域一般のH3とこの必要射影型のQを区別する。既存four_simple節のS/Q/O/H/L/M/F/G/K/J/R/N/C/adjacentL/S/T/fullPの表示別認識・全値排除を再計算せず、必要被覆を接続する。固定CI22_COMPLETEの支持被覆全文、FIRST_SHAREDの必要FN1–6、SHARED_ZEROの必要FZ1–10、INACTIVE_SHARED_VERTEX_EXCLUDED、SINGULAR_RANK_ONE_EXCLUDED、SINGULAR_RANK_TWO_EXCLUDEDの全文、FULL_SHARED_INVERTIBLE_REDUCTIONの必要FT1–12を読んだ（全AS十分性/Autは不要）。
元frameの支持走査では4096有向支持は218 S4軌道、zero/degree1/degree2/partial_active/fullの支持数1/3471/609/14/1、軌道数1/173/40/3/1。部分活性三軌道・全共有可逆/特異枝を無条件に飛ばさない。

### 四単純基点の全元frame・支持被覆と共有零層の全排除

通常証明cubic_CY_four_point_support節lem:cubic-CY-four-point-support/thm:cubic-CY-four-point-shared-zero-empty。元FS21混合方向/一KK方向の全CYframeを独立証明：混合rank15、KKrank20、joint57rank35。全24置換の印付きlambda変換・B全21係数・gアフィン変換・共有辺単元、対角d_i/d_jを元行列で全検証。全4096支持/218軌道をzero/degree1/degree2/partial-active/fullへ支持数1/3471/609/14/1、軌道数1/173/40/3/1と被覆し、degree1/2標準chartへの全置換存在を検証。
共有零の全Schur対角六条件/残余三式/相補積恒等式を独立に再生した。ABC零は全非零S又はH0/H1、ABC非零は全相補積零からQ又はOへ全被覆。全torus規格化は独立三整数重みと代数閉性だけ。Oの四禁止A値には元係数1の実積関係がある。Qは全六対の二項式係数和1、Thetaと六係数積の比が単元、F=0下の全四CY行積を確認。従って全q_ij!=1であり、既存lem:cubic-cy-skew-zero-commutatorから中心三次は高々一本の純三乗。S/Q/O/H全て既存全値排除に接続し、共有零層全H3なし。
全skew領域に存在するH3と、全q_ij!=1を要求する特定の射影型を混同しない。後者の条件はskewの許容五型への帰着に必要である。
公開verify_cubic_CY_four_point_support.py/shared_zero.pyと小certificateはdefault Sympy exact。固定as4 FS1–2/FZ1–10の式だけを出典化し、必要被覆そのものは元行列と通常の全場合分けで当repoに証明。新規性/AS十分性/全Aut/相対被覆は主張しない。
degree1のx0zero最初の共有chartは固定FIRST_SHAREDのFN1–6を読了、八bad境界は元三次dim21/22、残るL/M/F/G/Kは既存全値排除。

### 最初の非零共有chartの全H3排除

通常証明cubic_CY_four_point_first_cover節thm:cubic-CY-four-point-first-empty。x1!=0,x0=x3=x4zeroと全monomial軌道を全排除。固定FIRST_SHAREDの必要FN1–6を用い、全21係数の四枝(x2,x5)=00/01/10/11の全消去式を元Schur行列から一手ずつ独立再生した。各式が実際の残余式であること、一次pivotがlambda/lambda+1だけの単元であること、代入式・最終残余の一致を確認。四主飽和idealも再計算。八bad境界の元三次商21/22、全元関係挿入の座標零・分母unitから全閉値障害を確認。残余全係数FN2の四制約idealへの逆代入と、既存fn_matrixのliteral一致を検証。通常の全対角規格化でL/M/F/G/Kに全被覆し既存全値排除を適用。
公開検証器・入力・証明書は `verify_cubic_CY_four_point_first_cover.py` と対応するJSON。AS十分性/全Aut/相対scheme被覆/新規性は主張しない。
固定SECOND_SHARED_OPENのFO1–5とZERO_FIFTH_OPENの必要FZ1–6を読了。前者は全lambda/lambda+1/p-1だけの消去からq=x10nonnull空、qzero唯一H(lambda,p)へ。後者はqzeroでlambda1のM0/M1、p0は既完成firstchartへ直接移せるのでH3排除、pqnonnullは二factor枝で(lambda,p)=(1/2,-2),(2,-2)、四共役候補は既存Nへ。既存H/M/N中心排除は全値完成済みで再計算不要。

### 出次数1の二つの行列式非零chartの全排除

通常証明cubic_CY_four_point_two_open節thm:cubic-CY-four-point-two-open-empty。x0*x1!=0,x3=x4zero,x0*x2-x1²!=0をx5zero/nonnull双方で全H3排除。固定必要FO1–5/zero-fifth-open FZ1–6を用いる。独立exact controlは、全元21係数消去を式・単元pivot毎に再生、FO q(u-v),q(pu-v)の局所ideal所属とqnonzero空ideal、qzero全係数H(lambda,p)を確認。FZ qzeroはlambda-1の単元倍からlambda1/全M(p,r)係数、pzeroは元全matrixで既完成firstchartへ移送。pqnonnullは二factor枝それぞれの飽和idealを三必要有限条件と完全比較。残りx6/x7/x9は数体idealに各正冪が入り幾何学的に全zero。全四共役候補は具体P/対角/可逆関係基底で既存Nへliteral移送。既存H/M/N排除へ接続しAS十分性/全Autを輸入しない。
公開検証器・入力・証明書は `verify_cubic_CY_four_point_two_open.py` と対応するJSON。有限残余idealの被約性・相対scheme被覆・新規性は未主張。
固定GENERAL_BOUNDARY必要FG1–5、IMAGINARY_BOUNDARY必要FI1–4/h0五次58障害、ZERO_FIFTH_BOUNDARY必要FB1–9を全文読了（AS十分性/全Aut不要）。前者は全lambdaからR_eta(lambda)又はlambda=±iのJ_eta(h)、h0二点はHilbert5=58>56。後者はx17nonnull空、二factorA/B、七必要係数行と八種特殊結合係数境界を漏れなく扱い、genericbad四次37、lambda^4+1全根五次59、lambda²+1全根五次58、残るN/C/R±1は既存全値排除済み。境界の一般点だけで済ませない。

### 第五係数非零・行列式零境界の全H3排除

通常証明cubic_CY_four_point_determinant節thm:cubic-CY-four-point-determinant-empty。x0*x1*x5!=0,x3=x4zero,x0*x2-x1²zeroと全monomial軌道を全排除した。固定GENERAL_BOUNDARY必要FG1–5を使用し、一般境界・純虚境界とも、独立exact controlは、全21係数の二段階消去を元残余式・lambda/lambda+1単元pivot毎に再生、16(x15-x16)²+1とx9(16x9-lambda²+1)の全split、QQ(i)上の全二飽和idealと明示targetidealの一致。全R_eta(lambda)とlambda1重複は既存r_matrixにliteral一致。形式lambda固定の符号共役とlambda±iの全四fiberは、hを割らず可逆原関係基底で既存J_eta(±h/±ih)へliteral移送。既存prop:cubic-boundary-Jがh0のHilbert5=58も排除済みなので、同じ固定点のHilbertを新規に再計算したとはせず再利用。AS十分性/全Aut/相対scheme分類は輸入しない。
公開検証器・入力・証明書は `verify_cubic_CY_four_point_determinant.py` と対応するJSON。
固定ZERO_FIFTH_BOUNDARYの必要FB1–9を用いる。x17nonnull空、x17zeroの二因子分岐、FB3/4所属と三generic/三例外baseideal一致、全七基本行±符号、FB7/8の全結合rank低下を扱う。badは16記録：genericAm/Apの四次37、Az/B三次21、Apのlambda^4+1全四根五次59とlambda²+1全二根五次58、Az(-1/2)/B(-2)特殊coupling三次21、全±符号。原係数分母だけを管理して全閉値下界を使う。残るA1(r)はr0で旧C/共役、rnonnullで旧R±1、Ah/Bh四点は旧Nに移るので既存中心排除を再利用できる。
必要支持はdegree2が609支持/40軌道、部分活性が14支持/3軌道、全共有が1支持/1軌道である。

### 全出次数1共有支持の排除

通常証明cubic_CY_four_point_zero_determinant節thm:cubic-CY-four-point-zero-determinant-empty/cor:cubic-CY-four-point-degree-one-empty。最後のx5zero行列式境界を全H3排除し、全degree1支持3471個/173 S4支持軌道のH3なしが完成した。これを存在するmoduli成分数・intrinsic同型類数と呼ばない。
固定FB1–9の必要表示に対し、当repoのexact controlは元関係から次を照合する。元21係数からのx17nonnull単元矛盾/zero枝全消去、二split所属、七基本係数行の全局所ideal比較、両符号の全coupling行列・genericと例外rank/kernel/x9一意性、全16bad元商・全元関係挿入の座標零を確認した。genericAm/Ap四次37、Az/B三次21、lambda^4+1全四根五次59、lambda²+1全二根五次58、残る二有理特殊値三次21。全数体は既約性/minpolyと元係数評価で全共役を保持。元分母のunit管理とraw rank特殊化で全閉値下界を保証。全kernelのtorus規格化、旧C/係数共役、両R1への元移送、全四N点への可逆原関係基底移送を確認。旧C/R/Nの中心排除を新規に再計算したとはしない。
公開verify_cubic_CY_four_point_zero_determinant.py/input/certificate。AS十分性/全Aut/相対schemeの被約性・降下・新規性は輸入しない。
次の計算・上流controllerは起動しない。

### 出次数2の共有支持

固定as4のAZ・AF・AV・AO・ABの必要被覆と既存L/J/S/T排除を接続し、出次数2の頂点を許す四単純基点型を排除した。本文は cubic_CY_four_point_degree_two 節。AO2両符号の元三次商は独立計算で次元21、分母は許容単元のみなので全閉値にも下界21が成立する。残る零交換子CYの必要支持は部分活性14支持・3軌道、全共有1支持・1軌道。部分活性の必要排除と全共有の可逆・特異主ブロック被覆を合わせて用いる。

### 二交換子・非共有Segreの中心三次

固定as4 CY_TWO_COMMUTATORS_DISJOINT_SEGRE.texの必要表示は Q_q, N_1, N_2。孤立型の元関係を直接読むと a,c は正常で、ac の正常化作用は -I 又は -I に b→b+8a の単冪shearを合成したもの。従って既存 lem:normalizer-minus-unipotent-odd-centre で両型はH3から消える。Q_q の中心単項式条件は q^(i-j)=q^(k-l)=1。総次数3では少なくとも一方の差が奇数なので、q≠1 なら原始三乗根かつ純三乗に限る。Q_q の特殊値と、固定CY_TWO_COMMUTATORS_VERONESE_MIXED_RANKONE/RANKTWOを含む全必要表示のH3排除は `cubic_CY_two_commutators_Segre.tex` に従う。原始三乗根で中心単項式が存在するという計算だけから許容切断の存在を結論しない。

非共有SegreのQ_qの純三乗例外は、順序(a,b,c,d)で交換指数(0,1,2,2,1,0)に一致し、既存 prop:third-six-rank-obstruction で全排除。混合階数一VM1では個数濾過の先頭と正常元aの平行移動から中心はk[a,b,z]（z=ac+bd）に含まれる。[c,z]=-bz,[d,z]=azから中心三次はkab²のみで、整域切断はない。本文 cubic_CY_two_commutators_Segre 節。次の混合階数二VRでもaは正常、同じ濾過の先頭核を与える線型形式は t ac+β bd。

### 二交換子の残る孤立型

非共有Segre、混合階数一Veronese、混合階数二の全VRパラメータ族を排除した。本文 cubic_CY_two_commutators_Segre 節。特にVRでは正常元aの平行移動の先頭核から中心元をk[a,b,tac+βbd]に絞り、cとの交換で中心三次が零となる。
二交換子の孤立型Iも元VT行列から中心三次rank20（有理小行列式 -32768/22876792454961）で排除した。固定as4の cor:cy-two-commutators-complete の必要方向と合わせて全二交換子CY排除。残る非可換CY包絡の交換子次元は1又は3（3のbeta型は既排除）。

### 一交換子の平方追加Segreを全排除

十六必要射影のうち非共有Segre＋平方の全被覆だけを固定as4から使用した。13表示の全中心三次を独立検算し、残る内部二族の原始三乗根値を全排除した。S_{a+b}は二元三次の積分解、S_aはaで局所化した量子Weyl表示の中央式からZ=(Xの二次多項式)/(v³+(B/D)X)を得て、分子・分母を三次巡回ノルムと認識する。従って整域切断が存在しない。証明はcubic_CY_one_segre_square節。

## 7. 一交換子CY：三乗根Ore型と排除障害

`cubic_CY_one_segre_double_split.tex` の `thm:cubic-CY-one-commutator-presentation-closure` が共通Ore型と閉性をまとめる。MとFDC3を含む途中の必要支持は、同ファイルおよび `cubic_CY_one_segre_square_split.tex` の全値排除へ接続する。

### FDC3と一交換子CYの完結、全楕円キャラクターの自己Ext¹

六平面曲線上はL二次の七有理表示と二生成元順の階数16、E一次で有理グラフと二次代数ノルムにより全排除。曲線外はL二次の6個およびE一次の19個の剰余体で元中心階数20。最後のE枝の17個のP因子は、高次数では素数還元でM共通因子次数を高々1と抑え、提案根を元数体で検証。全FDC3の中央三次は零で、一交換子CYの全許容切断・幾何矢が揃った。滑らかな楕円切断の一次元表現を原点に移し、HessianをAとする。全許容Hesse係数p=1の中央持上げの分母はr(q−1)の因子のみ。rank A=2、核(u:v:1)の線型微分は−(ac−b²)/(q−1)×[(1+q³+r³)uv−qr(u³+v³+1)]。核がE上であれば自己Ext¹=1、外で0。rank 0,1,3では各3,2,0。この一次元加群の必要障害だけでアフィン有限大域次元は決まらない。全楕円域の十分性は `cubic_CY_three_alpha_elliptic_diagonal.tex` の八次判別式による判定を用いる。

### 二積追加の片外側非等方三族と非分解四交差

固定as4 DN5のOre行列Mは固有値1,detMを持たず、M²≠1。中央三次はM³≠1で可換二元三次のみ、従って非整域。M³=1ならM=qIの原始三乗根に限り、Z(s,0),s²=−1/12となる。全切断はP(a,b)+C c³+D d³。対称外側代表のある非分解四交差全域は反交換する非零二次元により奇数中心なし。
固定共鳴の全H3条件はCD≠0、Pは二座標軸で消える場合単純、P(1,z)²−4CD z³はトーラスで重根なし。軸でPが重根なら完備二生成元環の最小三次関係が三つあり、shift固定点のExt²=1に反する。単純軸の付値1,2、両軸非零なら種数2の剰余曲線により巡回斜体。中心chartではtorus分岐、非零積の行列環、および単純軸の完備量子平面で全判定。規格化C=D=1で(uv)³=1の対角作用とa,b交換、一般慣性μ₃、次元3。P=a³+2b³は明示H3。
残る二積追加の固定as4必要被覆は他の連続18族と孤立5類。

### 一交換子の非共有平方・積追加の削減とZ切断の完全判定

横断外側七表示、等方外側八表示、非等方外側四族、上行交差Cθを判定。公開verify_cubic_CY_one_segre_square_split.pyは19計算とBn2の四例外直線の全既約因子を元の六関係から再検算。C(s,z≠0),L(s,h)はc,dの逆作用を同時対角化し、固有値q1,q2の相異性、1でないこと、積が1でないことから全中心三次を可換二元に限定。唯一残るZのs²=−1/12ではqが原始三乗根、中心三次はP(a,b)+Cc³+Dd³。二つの純三乗係数のどちらかが零、またはdeg P(1,z)≤1なら固定点の奇数Ext障害。
Zでの正確な条件はCD≠0、deg P(1,z)=m∈{2,3}、判別式Δ=P(1,z)^2−4CDν³が平方自由。ねじった量子Weyl表示でg=Cx²+P(1,z)x+Dν³の付値剰余曲線は種数m−1、xの二無限遠位数は±mなので立方でない（m=3では次数1写像の矛盾）。巡回ノルムの付値から斜体。c,dチャートの自由巡回軌道で完備環は冠積、Δ重根ならその一つの単純の射影次元無限。a≠0でX=Y=0は二単元辺で行列環。m=2のb軸では中心aを陰関数消去し、完備量子平面への降下濾過で左右kの長さ二解消を得る。従って全H3公理を満たす。例P=b³,C=D=1。包絡の全幾何矢を元の標識と関係から決定し、C=D=1規格化のAff₁×μ₆作用、一般慣性μ₃、次元2。二原始三乗根の包絡はc,d交換で同型。本文cubic_CY_one_segre_square_split節。これは全成分性や相対降下の主張を含まない。
平方・積追加の残りは等方外側b5と下行交差L^±_{w,e}, Z_{s,h}, M_{s,w,z}。b5は一般で中心零、例外h²+1/16,h²+1/48および三曲線での厳密再計算を終える。下行片成分の両符号のgeneric rank20だけで全例外を排除してはいけない。特殊値は対応する全値排除証明を用いる。

### 平方・積追加Mの全域排除

(LO5)の元六列と中央二次を(d,c,a,b)の順、規格化(X,Z,T)で計算した第二の階数16証明書は、既排除面と単元を除いて14因子。二つの証明書の四符号移送による八因子積を交差させ、第一証明書の五枝ごとにZとTを終結式で消去した。Xの既約因子数は3,14,2,4,2。数体上でT、Zを最大公約数で戻して規格化単元を除くと、2,6,0,3,0個の剰余体で元六関係の中心行列を階数20と検証。枝の重複を含む。Mの全(LO4)域で中央三次は零。証明はcubic_CY_one_segre_square_split節、公開検証器M_witness（--alternate）、M_finalと証明書。

### FDC3の四L一次面の全域排除

NL+1、(N+1)L+1、(N−1)L+1、KL+N−1の全許容点で中央三次は零。各面で中央二次商の新しい局所階数証明書と既存二証明書の八移送を併用。E方向の終結式で14曲線（面ごとに5,4,2,3）と有限部分に絞り、曲線パラメータ上の二つの生成元順の証明書で全曲線を排除。曲線外の14剰余体は全て元階数20。全四面の公開FDC_linear検証器と個別証明書を照合した。残るFDC3候補はL二次枝とE一次枝だけ。

### FDC3の二つの非線形枝の平面射影

m=0と二判別式面を除くFDC3候補は、N=PM、K=(P²−1)(M²−1) とすると NL+1、(N+1)L+1、(N−1)L+1、KL+N−1 の四L一次面、NKL²+(K+N²+N−2)L+N+1 のL二次面および第二証明書の唯一のE一次面に含まれる。四L一次面の外では全16必要因子積からE,L終結式を取る。L二次枝の平面支持はM=P±1、PM+1=0、M²+4MP+P²+3=0と有限集合。E一次枝の平面支持はMP+M−P=0、(PM−1)²+(M−P)²(M−P+1)=0と有限集合。四曲線でのL全根の有理式と第二E一次曲線の二次拡大表示は論文のFDC3節。再現器は `computations/verify_cubic_CY_one_segre_double_split_FDC_projection.py`。

### 一交換子の二平方と三交換子の構造的削減

一交換子・二平方追加Segreを全排除した。交差チャートの元トップから定数minorで六関係を復元し、固定as4の有限(p,t)・無限遠(e)とのliteral一致を確認。中心20次minorと次数別商射影の全因子から、有限残余は p=0,-2,-2/(t+1),-2/(2t+1),2/(t-1) の五曲線。各曲線の元関係から再計算すると例外は許容域外だけで、中心三次は全域零。無限遠はe=0を別QQ計算し全域零。通例のAS4次元20,35だけを特殊化に使った。
三交換子外積階数二は三係数層を一括排除。固定as4の反射型融合積の交代語基底を使い、次数三の奇数語と長さ二語は基礎a,bへの作用が非恒等なので中心に現れない。残る基礎の重み二変数Zの係数も二対合の一次固定空間の交わりが零。従って中心三次は可換二元で全て可約。外積階数三の列係数階数二は対称関係Cliffordへの二次ねじりで、任意の中心三次が中央二次{a,d}を反転して矛盾。alpha零先頭式二表示はa=1の中心の濾過次数が2以下なので共通因子aで排除した。
CY必要被覆では、一交換子の非共有Segreの平方・二直線追加、共有Segre十一型、三交換子のalpha非零先頭式と外積階数三・列係数階数三を区別する。必要被覆および切断条件は別々に記録。同時に他のSegre候補は元関係から中心零・可約・twistの中心障害を先に見る。

### 一交換子の共有Segre十一射影を全排除

対称階数5の必要排除と標識付き階数4の十六候補を固定as4から使用した。共有十一射影のうち固定空二射影以外を、元の六関係から中心三次を独立計算して判定。ad,bdは全域中心零。b²とb²+c²では中心三次はa²cとa²bの各一元。ad+b²とad+b²+c²ではt=-1/3でのみ中心三次kac²。bd+c²ではh=-1/4でのみ中心三次kb(b+3a/8)²（lambda=1/64も同じ）。いずれも整域切断なし。残るd²+b²,d²+b²+c²では、交換子比の零・非零、下位係数zの零・非零、非対角ellの四共鳴とその補集合、対角係数両符号を合わせた全40域で、商射影の分母と中心小行列式の全因子は許容単元のみ。全中心三次が零である。
本文cubic_CY_one_segre_shared節。公開verify_cubic_CY_one_segre_shared.pyとverify_cubic_CY_one_segre_shared_squares.py、対応JSON。一交換子の非共有Segreではa²+cdとab+cdの二型を区別する。

### 平方・積追加のb5と下行交差の二領域

等方外側b5は順序語基底で二元三次四列を零にする行に制限し、非二元の16列のminorは −17179869184 s⁴(48s²+1)²/((4s−1)¹⁴(4s+1)⁹)。残る48s²+1=0で全θの定数minorを厳密再計算し、可換二元三次しか残らない。下行片成分Lの二符号は反対代数。片成分と両下行・cd零Zの各五例外曲線を元六関係から有理化した。数体の全残点とZの別点(s,h)=(3/8,−48/5)を含め中心rank20。公開verify_cubic_CY_one_segre_square_split_lower.pyとJSON、本文cubic_CY_one_segre_square_split節。
平方・積追加の三変数M(s,w,z)は、中央二次商とその例外面・数体の計算で扱う。Rains系の既分類、固定Z(s)の全判定は繰り返さない。

### 二積追加の孤立五包絡を全排除

DE2/DC1/EN3の二表示は元の六関係の中心行列が階数20。例外体積DX1は階数18だが、ell=a+i√3 d/18、m=b−6i√3 cが原始三乗根の逆数で交換し、その二立方が中央三次を張る。任意の非零中央三次は線型結合の立方となり非整域。二数体の公開検証器で全商と中央恒等式を再生。二積追加の残りは18連続族。

### 二積追加の十五連続族を排除

DA1,DD1,EN2,EB2,TN1,FZ1の全中心三次は零。最初の三種の単元因子チェックとEN2の七点・TN1の二点を厳密再計算。FZ1の例外はy−z=±1/512と(y−z)(y+3z)=1/262144、(y−z)(y+z)=1/262144で、四有理表示とそれらの全例外点で階数20。等方片外側はe=a又はa+bがc,dと反交換するのでc,d合計次数の偶数しか残らない。e=0でbの二倍率q,q⁻¹により混合三次をbcdへ絞り、cとの交換で排除。e²を法としたb係数と元のc係数で残るe c²,e cd,e d²も零。従って全九族の中央三次は可換二元で因数分解。全式と単元関係基底は公開検証器・JSON。
二積追加の補助模型には、分解交換子の三交差TD1、片外側四交差FO1–FO2、両外側四交差FDC3がある。この三表示は実交換子平面を明示でき、元関係の低次数構造を用いた中心判定に利用できる。

### 分解三交差と片外側四交差の中央二次商

実交換子平面U,Vの中央二次Q₀を元次数3で全三変数厳密検証。TD1ではp²U²+pw(16p+64w−2)UV+w²V²、FO1–FO2ではpU²+2ηUV+16p(η²+(1−16p²)/1024)V²（η=pw+1/32）。係数の一つuに依存しない。許容域の一定次数三商に中央性が全て特殊化し、整域で可換二元二次の積なので非零。中心一次零によりZ₃は中央二次商へ単射、商次数(9,16,25)。
TD1とFO1–FO2の元六関係については三変数FLINT関数体で次数四まで構成し、中央行列階数20の小行列式と商行列分母の全因子をJSONへ保存。再実行は同検証器の--cubic TD1または--cubic FO1。

### 片外側四交差の線型例外面を全排除

FU座標はx=4t,r=tσ,v=16tqで、x(x²−1)rv(v+1)を可逆とする。FR2から対称性(x,r,v)↦(−x,r,v),(x,r,v)↦(x,−r,−v−1)。元表示と線型基底表示の二つの小行列式および分母のr線型因子は、rv(x−1)+2x、r(v+1)(x²−1)+2x²、r(v+1)(x²−1)+4x²、r(2v+1)(x²−1)+4x²の四軌道。各面・八有理グラフ・二つの二次拡大曲線と全例外特殊点で中心行列階数20。残る候補は二つの小行列式それぞれのr二次・三次因子の積と対称移送の共通零点。検証器・証明書・元関係基底の式はcubic_CY_one_segre_double_split節。

### 片外側四交差の非線型例外を全排除

正規化したR=r(x²−1)/x²,C=Rv+2,D=−R(v+1)−2,Y=x²により、二つの元の階数20証明書の例外因子はF₁F₃=F₀F₂=0。それぞれY線型で、対称性によりCD=−4、CD=4、D=C−4と、F₁=F₂=0の混合曲線を判定すれば十分。最初の二曲線は二次関数体上で元の中心階数20を厳密に証明し、全例外因子は単元か曲線式に反する。後二曲線は中央二次商の二つの階数16証明書・四移送を制限する。終結式でD=C−4を除外。混合曲線のC方向の残りは次数8・18の二因子で、各数体のx多項式の最大公約数で全排除。従ってFO1–FO2は全H3なし。二積追加の残余はTD1とFDC3のみ。全式・証明・再現器はcubic_CY_one_segre_double_split節。

### 分解三交差を全排除

A=8p−1,B=h/w−A/2,E=uw²で、AS4のTD12は反対代数をAの符号変換に移す。中央二次商の階数16例外因子は2B−1、A+2B−2、A²−1+64E(2B−1)(−A−2B)。B=1/2の元階数20証明書と反対代数を合わせると、全例外は五有理曲線。元六関係から五曲線と九既約因子の数体で階数20。TD1は全H3なし。二積追加は両外側四交差FDC3だけが残る。正則条件と全係数はcubic_CY_one_segre_double_split節、検証器およびJSON。

### 平方・積追加Mの中央二次商

U=a−(c+kd)/s、V=s(b−d)により[U,V]は実交換子。Q₀=(sw/(4(kw+1)))² U²−2sm UV+V²が全LO4で正則かつ中央。元の線型関係基底で次数三までを厳密検算し、次元一定で全値へ特殊化。Z₃は二次商（次数2,3,4で9,16,25）に単射。X=4s,T=(kw−1)/(kw+1),Z=(wz−k)/kで同型(X,T,Z)↦(−X,−T,−Z)、反対代数はXのみ反転。三境界はX±T,X²+T。全式はcubic_CY_one_segre_square_split節。

### Mの例外を次元一以下へ縮小、非捩れ量子型の差分模型

M中央二次商のz一次係数のpivot列は0,5（0始まり）。他の五列をz非依存にし、その次数2,3,4の商次元11,26,57から変動二列の全挿入を加える。次数四の追加96行・57列、商25、中心階数16。正規座標で元の境界と対称移送X²−Tを単元にすると全例外因子13、四移送の共通因子T・ZT−1。ZT−1は全域元階数20。T=0はξ=XZで三グラフ・三有理conicに縮め、全曲線及び五例外既約因子の数体で階数20。残りは次元高々一。FDC3の(p,m,d/e,e)でも係数行列のe微分のpivot列0,5、五固定関係の次数二〜四は11,26,57、変動追加後次数三16を別途厳密計算。第四次の全rank証明書は引き続き必要。
非捩れ三角形・割線の忠実な多項式模型ではDₐ=a(u)(σ−1)+a(u⁻¹)(σ⁻¹−1)とxで生成。aの分母(1−u²)(1−qu²)、分子次数4／5、定数非零。留数の符号は非固定零点の反転と定数符号で調整。三角形で全四根の反転を選ぶとKoornwinderのabcd∉q^(−Z≥0), ab≠1を満たし、Theorems 2.2,3.2により全係数で階数一球面DAHA。アフィンの有限大域次元の判定は残る。

### Mの低次六面と非捩れ三角形の平方自由開

MのT一次三面とZ一次三面を全排除。五有理表示（三つのT面のうち二つは反対代数で同じ）。Z=(X+1)/(T+X), (X²+1)/(T+X²)は局所証明書だけで全域。残り三面で局所証明書と四対称移送を交差して共通曲線なし。終結式と数体上最大公約数から43,29,6剰余体に減らし全階数20。従ってT二次一式とZ次数2,2,3,4の四式だけが残る。M初回公開証明書の独立再実行も同因子に収束。
非捩れ三角形の球面DAHAで、各二次Hecke因子が分離しeがfullならH3。左右自由な交代語とMayer–Vietoris列によりH=A添字の二つのhereditary自由積から大域次元≤2。eを殺した商は1,Z,T₀,ZT₀で張り、単純は次元≤2。GWA四次F(ξ)=(ξ²−4)aは各AW軌道 ξ_i=a_i/ρ+ρ/a_i を根とする。この四軌道が相異なればeを殺す一・二次元単純は存在せず全H3。定数項なしは四次Fの二重化が既排除の二端点のみなので非捩れも完了、水平incidenceの全幾何学的群oidを更新した。相対降下の完了は主張しない。

### FDC3の二次元必要支持と節点の全矢

FDC3の(P,M,L,E)でEの一次係数はpivot 0,5の階数2。五固定列は次数2,3,4で11,26,57。変動二列の16・96挿入を加えて商16,25、中央行列階数16を厳密計算。選択ピボットを積にせず、183個の射影分母と個々のピボットから既知因子を順にGCDで除くと10既約因子。固定as4 FBOの八移送ではp'e'd'=0も必要支持へ加える。共通は二つの判別式線型因子、二つのL一次面、KL²−1の五既約超曲面。各面の許容有理点を元六関係でrank20と検算したので中央三次候補閉集合は次元2以下。五面そのものの全排除は主張しない。
節点規格化P_x=P_y=A_z=1では、固定as4 N1–N2からμ₃対角と接線交換で全幾何矢。交換(x,y,z)↦(q⁻²y',q⁻²x',−q⁻³z')、q↦q⁻¹、係数(A_x,A_y,B_x,B_y,B_z,D)↦(q²A_y,q²A_x,q⁴B_y,q⁴B_x,−q³B_z,−q⁶(D−B_z/(q³−1)))。Dの補正は中央Jのxy項の順序化。厳密恒等式。慣性はA_x,A_y,B_x,B_yの全零でμ₃、その他は自明。

### FDC3のm=0と二判別式面の全域排除

規格化(P,W,E₀)=(4p,(d/e)/p,1024pe)。S,Q,Pの順の合成はPのみ反転し、Sは(P,1/((1−P²)W),1−E₀)でE₀=1以外に適用。m=0専用証明書の共通七面とE₀=1を六表示で覆い、四変数証明書の四有効移送を足して外の四有理面とE₀一次終結式枝を覆った。十半開チャートの全例外は11有理曲線と剰余体9,15,18,37,3,0,3,2,24,22。曲線・各例外剰余体は全元階数20。最後の自由E₀枝は終結式の基底候補なし。公開mzero input・certificateと検証器。
四変数第二証明書は(d,c,a,b)順で8因子。全16移送の共通面は1+(P−1)(M+1)Lと1+(P+1)(M−1)Lの二つだけ。第一面の局所証明書の因子は全て単元。第二面の二証明書でM²P−MP²+MP−1とM−P−1、Sの主チャート外f=0から(P,M,L,E)=(P,P+1,−2,−2P)、2P²+2P−1=0に限られ、許容かつ元階数20。両判別式面は全排除。公開FDC_witnessの--alternate、--discriminants 。

## 8. 三交換子CY：Clifford中心拡大と対称部分

`cubic_clifford_full_cuts.tex`、`cubic_clifford_beta_classification.tex`、`cubic_integrated_envelope.tex`、`cubic_CY_three_alpha_nonsmooth.tex`。固定包絡・表示族の分類と全H3での成分性を区別する。

### 中央楕円認識とClifford変形の補助計算

滑らかな次数3楕円THCR（translation）の全filtered deformationについて、Rees環の二次包絡がnoetherian quadratic Koszul CY AS4で、一本の正則中心三次の商になることを証明した。AS4包絡を外部に仮定せず復元できる。非可換では境界が一意なので、intrinsic中央楕円H3の幾何学的群oidは有限gldim filtered deformationとfiltered同型に一致する。Hesse/Moore・対称線型係数・中心三次の単一線型核による有限候補atlasと全同型係数比較を得た。有限Nは中心McKay条件で全admissibilityを判定し、被約固定N族では相対中心とH3開性も証明済み。正規境界の被覆と三角境界全有限位数の判定は後述の現行結果を参照する。

積分した族の全次数平坦性・noetherian quadratic Koszul CY AS4 認識を、明示的な開集合 V={h∈H, (1-gamma²)≠0, Delta≠0} 上で証明した。入力は Iyudu–Shkarin Theorem1.1/Corollary6.1、EG形式変形定理、および64個の三次持上げ恒等式・256個の四次巡回恒等式・単元小行列式 -p^6 を確認した LBS 中心拡大定理である。中心三次の関係類の非消滅も巡回商の二係数で全パラメータについて確認した。gamma≠0 では低次数中心が0,0,1、滑らかな楕円THCR境界となり、全中心値の H3 判定は正確に一つの affine 中心切断の有限大域次元へ帰着する。定義体上超越的な全 D は H3。位数4の枝 gamma^4=1+h^3 では固定包絡の悪い D は有限であり、h=1,gamma=2^(1/4),A=1,B=C=0,beta=(-1,0,0),D=pi は明示的な非Clifford H3 対象となる。

Etingof–Ginzburg の付録と著者サイトにある Rains の E6 中心元を規約変換し、全パラメータで三交換子の関係恒等式を独立検証した。`alpha=-4*gamma*(A,B,C)` と置き、正規化した中心元に定数補正を加えると、全 Clifford 切断が実際の有理式による中心表示へ積分する。gamma=0 での全係数・関係証明書の分母はよい h の全底上で正則であり、全次数の「中心性」の障害は解決した。これは包絡族の全次数平坦性、AS4 認識、切断後の H3 条件や新成分を証明したという意味ではない。

この族から外れる指定四方向の一次中心 incidence も全係数で判定した。双対数上で最高次を `(1+epsilon*gamma)yz+(1-epsilon*gamma)zy` に変え、対角項を `epsilon*alpha_x*tx`（巡回）だけ動かすと、三次中心切断の持ち上げは正確に `alpha=-4*gamma*(A,B,C)` のとき存在する。持ち上げを明示し、全ての h,beta,A,B,C,D に通用する次数4の階数86、三次交換子階数15、単元障害行列式 `-9/(4*(1+h^3)^2)` を検算した。これは指定方向の一次 incidence であり、積分可能性・全変形空間・新しい H3 成分を主張しない。 また、この明示的持ち上げの二次障害も全係数で消え、対角係数の二次補正 kappa と中心切断 G2 を計算した（epsilon^3=0）。

**Skew包絡部分の幾何学的対象は分類したが，全AS4包絡を覆ったわけではない。** 主証明は papers/weak_cubic_axioms.tex の sec:14641-classification とそこでinputされるcubic分類節。

### 位数二Clifford–Sklyaninの分裂包絡族：全切断・有限比較を解決

papers/sections/cubic_clifford_full_cuts.tex。これは前節のZ(S)2=0を外した新しい非skew族である。S_hの三関係を yz+zy=h x² とその巡回形とし、h≠0,h³≠−1,8、B_h=S_h[t]とする。

- S_hは中心多項式環P=k[u=x²,v=y²,w=z²]上階数8のClifford環。g_h=xyz−h(z³−y³+x³)/2、T_h=((4+h³)uvw−h²(u³+v³+w³))/4 とすると、全中心はP[g_h]/(g_h²+T_h)。S_hのAS3/CY/Koszul/noetherian条件を確認した。THCRへの射はpoint graphと楕円曲線のpencil trickから直接構成し、g_hによる商とHilbert級数まで照合した。translationは位数2。中心原点以外ではAzumaya quaternionとなる。
- Z(B_h)3 は g_h,tu,tv,tw,t³ の五基底。全H3切断はG=g_h+t(Au+Bv+Cw)+Dt³で、全係数で商は整域かつGabriel–Krull rank-one。D=0ではaugmentation点のExt1が3次元となる。中心tでSerreを[2]へ自明化するとExt1は非退化交代形式を持つはずなので、奇数次元障害により除外される。
- D≠0ではアフィン中心曲面 T_h+(Au+Bv+Cw+D)²=0 が滑らかであることがH3の必要十分条件。中心原点を避けるためAzumaya性を全域で使える。単に中心が特異なら非可換環も特異と推論したものではない。
- h=1の固定包絡について、悪い非零Dを正確に与えるmonic四次式Ψを明示した。係数はI=A³+B³+C³,J=A³B³+B³C³+C³A³,K=ABCの多項式。polar写像P2→P2の次数4の有限flat族における中心値のnormがΨとなる。係数の次数と不変式空間を通常証明で先に制限し、次元2,4,6,9の全空間について16点の有理数評価行列の全rankと4×4normを照合した。これにより全パラメータの恒等式を厳密に証明した。補間を全AS4の正則性の外挿に使っていない。
- **h=1の全固定包絡H3群oidは [V/G(3,3,3)]**。V={Ψ(I,J,K,1)≠0}⊂A3、群の位数54。粗い同型類空間はSpec k[I,J,K,Ψ(I,J,K,1)^−1]、全慣性は明示的monomial作用のstabilizer。
- **一係数切断G=g+A t x²+Dt³の全例外はD=0,−16A³/27,8A³/49**。A≠0ではκ=D/A³が完全不変量で、群oidは(A1−{0,−16/27,8/49})×BS3。A=0,D≠0は一軌道で慣性G(3,3,3)。
- **hも動く上記Hesse族全体の全切断は四次元の有限商 [W/Γtilde]**。Dを1へ規格化し、T_h+s(Au+Bv+Cw+s)²の四つの偏微分のresultant非零を要求する。ΓtildeはHessian群216のμ3中心拡大で位数648。全包絡間の矢をC_h(MX)=c C_h'という九flex保存行列で覆い、二次中心への具体的作用も与えた。全648比較の定義と54/108への固定h stabilizerの増大条件 h⁶+20h³−8=0 を証明した。実際の切断慣性は(h,A,B,C)のstabilizerであり、この比較群全体を一般切断の慣性とは呼ばない。
- Aut B_hの恒等成分はGm²なので単冪自己同型は恒等のみ。標準半単純化がこのB_hとなる部分にも非自明な単冪持上げはない。

上記は明示的なHesse分裂包絡族を持つ部分の全幾何学的分類であり、全H3の成分性・非分裂包絡の被覆・相対降下ではない。前節の「分裂包絡のペンシルΛ=C*」はZ(S)2=0等の低次中心仮定下の定理であり、この五次元中心三次族へ誤って拡張しない。

外部入力はIyudu–ShkarinのLemma3.7/Theorem1.1（このp=qの場合のKoszul性）とLemma5.1の全九flex保存群。必要な証明本文を確認し、全216射影行列・base作用12・kernel18・全特殊固定点多項式をQQ(ζ3)で独立照合した。再現はverify_cubic_clifford_cuts.py と verify_cubic_clifford_hesse.py。source hashと検証範囲はvalidationに記録する。

### 非分裂Clifford中心拡大：二次ポテンシャルを全パラメータで除外

同じ証明節の sec:clifford-nonsplit-lift-obstruction。h∈Hについて、中心tと三関係 yz+zy=h x²+α_x t x+β_x t²（巡回）を持つ包絡を調べた。

**この表示がH3包絡ならα_x=α_y=α_z=0。βは任意で、この必要条件に例外hはない。** 先に六関係の混合quarticを構成し、256個の符号付き巡回恒等式と常数minor−1から、H3下でμ_B=1を証明した。正規三次Gは中心で、G mod t は非零g_hでなければならない。G=g_h+tq+t²ℓ+t³dのt²商において、三つの係数汎関数は任意のqの寄与を消し、−3α_z/(2(1+h³)),3hα_x/(2(1+h³)),3α_y/(2(1+h³))を与える。障害行列の行列式−27h/(8(1+h³)³)は全Hで非零。

停止する五つの非可換置換から表を計算し、99個全ての次数4関係挿入をQQ[h,α,1/h,1/(1+h³)]上の恒等式で確認した。有限パラメータの標本からの推論ではない。H3のAS4仮定とt正則性を用いており、低次検算だけで任意係数の包絡をAS4と認定していない。

一般の対称ポテンシャルH=H0+t f2+t² f1、H0=2xyz−h(x³+y³+z³)/3では、唯一のt平行移動でf2の混合項を消せる。残る対角項が上の障害で零となるので、H3ではf2はJac(H0)2の三次元部分空間に属し、平行移動でf2=0へできる。従ってこの非分裂問題は**定数関係項βだけのClifford拡大**へ縮小された。

β族のrank-one Clifford退化点ではAzumaya性が失われる。分裂族の「中心曲面の滑らかさのみ」の判定をそこへ拡張してはならない。この局所homological判定は次節で解決した。as4のα表示から用いたのは固定SHAのmixed quartic式だけで、全軌道や全係数AS4判定は輸入していない。輸入範囲はas4_imports.jsonに更新した。

### 全β族の判定を完了：非Azumaya通常二重点と七次元groupoid

主証明 papers/sections/cubic_clifford_beta_classification.tex。前節で残ったB_{h,β}（yz+zy=h x²+β_x t²と巡回）の全βと全中心三次切断を扱う。これは指定した対称ポテンシャル中心拡大部分の完全な幾何学的分類であり、全AS4包絡の被覆とは区別する。

1. **全βで包絡はnoetherian quadratic Koszul CY AS4型14641。** 中心多項式環上の階数8 Clifford PBW基底でtの正則性を確認し、mixed quarticのt収縮がS_hの三次トップへ全射となることを確認してLBS Theorem2.6/Corollary2.7を適用した。原文の全仮定と該当証明を点検した。低次rankからのAS4外挿ではない。
2. **全H3候補はG=g_β+t(Au+Bv+Cw)+Dt³。全候補の整域/rank・飽和・例外性・AZは既存認識で保証され、残るアフィン商Uの中心はF=det Q_β+(Au+Bv+Cw+D)²。Q_βの対角はu,v,w、off-diagonalは(hw+β_z)/2等である。
3. **完全な必要十分条件：F=0の全特異点は、rank Q_β=1にある通常二重点のみ。** rank>=2ではAzumayaなので中心特異点は不許容。rank1の通常二重点では完備化環がk[[s,t]]⋊{±1}となり大域次元2。中心が特異でも許容される。より退化したrank1点は、自己Ext1の奇数性またはcross-Ext1のYoneda対の退化でSerre双対性に反する。rank0も除外される。二つの明示的な空集合条件（Jacobian/minor/Hessian）で全係数を有限判定できる。
4. 局所証明はSchur補a,b,c,mと二頂点表示を使う。E=d(a,b,c,m)のrankは2か3。rank2なら自己Ext1=1。rank3ではquadratic relation Kの非退化性が必要で、Cauchy–Binet恒等式 det(E^T Hess(ab−c²+m²)E)=8detK が中心のHessian条件と同一視する。十分性はA1の階数一反射的加群の二分類とEnd(C⊕M_odd)=k[[s,t]]⋊Z2から証明した。一般NCCR存在の未監査分類を入力にしていない。
5. **pure volume切断G=g_βの全許容条件**は、三つのquadrics 2yz−hx²=β_x等の長さ8 character完全交叉が被約であること。その場合中心は四個の通常二重点を持つ。h=1,β=(-1,0,0)では中心 (5u−1)vw−u(u−1)²−v³−w³=0 の四点 (1,0,0),(-1/7,-4η/7,-4η²/7)（η³=1）が全て許容nodeである。
6. **指定対称ポテンシャル中心拡大部分全体の幾何学的groupoidは[P/G]、一般次元7。** GはGm恒等成分とHessian216成分群を持つ。全矢はC_h(MX)=cC_h'(X)、β'=a0² M^Tβ/c、a'=a0 a q(M)/detM、D'=(a0³D+a0 a k_{β'}(M))/detMで完全に判定される。Dの混合補正を落とさず、D=0の許容対象も含む。恒等成分の重みはβ2・a1・D3。全慣性は明示的stabilizer、一般には自明。pure volume三次元部分の一般慣性はμ2。
7. 全B_{h,β}のAut恒等成分はtorusなので非自明な単冪自己同型はなく、この標準半単純化を持つ部分にも追加の単冪持上げはない。

再現は verify_cubic_clifford_beta.py（全h,βの8×8 volume・Schur・character変換・普遍Hessian/Ext対恒等式、四node具体例）と verify_cubic_clifford_beta_action.py（QQ(ζ3)(h)上の全9生成元合成とD混合項）。

### 対称potentialのj0境界

h=-1,gamma=2,A=1,B=C=0,beta=0の非分裂CY AS4包絡に、729G0=13y³−3yzx+13zyx+z³−30tyz+6tzy−72t²xという正則中心三次を得た。旧積分式を1+h³倍して特殊化する。point schemeはx³+y³+z³+9xyz=0で、potentialのj0とは区別する。translation点(3:−1:1)の良い還元位数は5上9、13上6なので無限位数。超越的Dの全切断G0+Dt³はH3。超越的中心切断の議論だけから、定義体上代数的な切断値の許容性を推論してはいけない。証明はcubic_j0_boundary.tex、独立な有理数次数4交換子・最高記号非消滅と有限体位数の検算はverify_cubic_j0_boundary.py。

### 三捩れ量子Weyl chartの全中心と固定切断

関係yz=qzy+b1,zx=qxz+b2,xy=qyx+b3（q²+q+1=0）ではX=x³,Y=y³,Z=z³,W=xyz+(b1x+q b2y+b3z)/(q−1)が全中心を生成する。d=1/(q−1),e=−(2q+1)/9としてW³−d b1b2b3W−XYZ−eΣbi³Xi=0。滑らかなHesse中央切断X+Y+Z−3lambda W+Dの中心は実際にこの中心環の商と一致する（最高記号中心とRainsで証明）。b=(1,1,1),lambda=0では全非H3値は(D²+4e)(D²+36e)=0の四つ。D²+9e=0の二値は中心A1だがMcKay(1,2)でH3。他の四値にはcharactersがなく非H3。証明はcubic_quantum3_center.tex、全中心式と臨界値の厳密検算は二つのquantum3検証器。

### Clifford swapの中心模型は証明・原稿化した

u=x+y,v=x−y,w=z+h u/2、A=u²,B=v²,C=w²,D={u,w}/2,a=vw,s={u,v}とする。G*=−[vw,u]/4なのでa,sがRで中心、T=t²,P=xy+yx,Z=z²は包絡で既に中心。Delta可逆ならT,P,Z↔B,C,Dは可逆で、五中心二次の全関係は三scroll minor BC−a²,Cs−2Da,as−2DB。Rは中心subring C上Clifford有限、Hilbert比rank8、generic三変数Cliffordの偶部分rank4 quaternion。normal cubic scroll Cの正規性によりZ(R^2)=C、ProjZ(R)=F1、PI degree2を証明した。Omega=(uw−D)t中心三次でOmega²=T(D²−AC)。qgrRはF1上rank4 quaternion order、tau²はhyperplane E+2F twist。全分岐と極大性も次の通り証明した。検証器はh=b=c=1で中心二次dim5、対称積rank12、全minor、volume交換子恒等式を独立確認。平面conic Γ_h=−2(1+h³)ξr+3h²r²+h(h³−8)s²/4 と Q=L2 ξ²−4(h²b−c)ξr+4hb r²+L1 s²（L1=hc−2b,L2=(h³−2)b−3hc）を得た。detQ=−4L1(c²+h²bc+2hb²)、L2zeroはQ=Γ自身。四bad方向は三singular conicsと一致member。許容conicはΓと四点横断。F1=Bl_pP2,p=[1:0:0]でgeneric quaternion symbol(−T/C,(D²−AC)/C²)のBrauer分岐は二conicのstrict/pullbackそのもの、例外E/fibreには分岐なし。分岐類3E4F、K+半分岐=−(E2F)/2、klt log del Pezzo degree3/4でrank4を掛けるとcubicdegree3。

Λ=~R²はB,C,D,sの四patchで三生成Cliffordとなりlocallyfree rank4。全閉完備局所模型は分岐外Mat2formalplane、smoothbranchはreflection skewgroup、四nodeではquantumformalplaneq−。各gl2。余次元1の非平方residueにより巡回valuation最大order、反射性で大域最大order。完成後最大性を主張しない。表示族のcommondegree scalar rigidificationは有限対角の分離既約DMstack2、generic inertia mu2²、任意底変更/fpqc局所表示族の降下を得た。

### 三交換子alphaのgamma=0全切断と幾何矢

固定必要被覆でgamma=0を許すのは滑らかな先頭三次と三角形・節点三次・二次曲線と割線の四型。後者三型はaを法として三平方中心のClifford環。中心三次の交代積のa²までの持ち上げに対して、元関係の次数四挿入を固定QQ射影で次数三商へ送る全行列は階数6。核の三下位係数への射影が零でQ=0となる。公開verify_cubic_CY_three_alpha_symmetric_first_order.py、三型を厳密再生。残る切断はω+a(Ab²+B₀c²+Cd²)+Da³。三角形ではAB₀C、節点ではC、割線ではAB₀の非零が固定点Serreから必要。
これらの軸条件で無限遠は全て有限大域次元。中央平方根を付加し、反転される単元によるMorita同値を使う。階数2ではAzumaya、指定軸の階数1ではSchur補の二平方とaが独立な非退化Hessianを与え、既存通常二重点の局所証明を適用。境界行列式uvw、uvw−9u³−9v³、w(uv−9w²)と軸の局所整域性から中心は既約。a=0の指定位数1境界の剰余四元数(u₁,u₂)が非分裂なので一般中心でも斜体、CMから整域。H3はアフィン中心T=detK+(Au+B₀v+Cw+D)^2の全特異点が階数1かつHessian非退化であることと同値。矢はF(LX)=ell F(X)とV'=r²V(LX)/ell、切断二次係数の行列式規格化で全判定し、共通スカラーで割る。
滑らかなFはHesse標準形へ移し、Fermat先頭は平方関係、h³=−1は(b+c+d)²で排除。残るh∈Hは既存betaの中心・局所全判定と全幾何矢に入る。従ってalphaのgamma=0部を完結。相対降下・大域成分の主張は含まない。一般点の中心零や全除外は未主張。

## 9. 三交換子CY：量子三角形・割線・節点

`cubic_CY_three_alpha_quantum_triangle.tex` の `thm:cubic-CY-three-alpha-nontorsion-full-folded`、`cubic_CY_three_alpha_primitive_triangle.tex`、`cubic_CY_three_alpha_nodal_E6.tex`。原始三乗根の追加中心方向を体積ペンシルと分ける。

### 三角境界のq-so3 Casimir pencil

q²+q+1=0、B=(t central; yz−qzy=tx,zx−qxz=ty,xy−qyx=tz)は既証PBW CY AS4。f=(1−q)/3,e=−(2q+1)/9,f³=e,e²=−1/27。V=B/(t−1)の中心はChebyshev X=x³+q²x cyclicとOmega=xyz+(q−1)(x²+z²)/3+(q+2)y²/3、関係Omega³+f Omega²−XYZ+eΣX²=0。Vはk[X,Y,Z]上free27、中心3foldに五つのODP。CY双対/filtered maximalityでVは対称MCM最大order、正則中心上Azumaya。

G_D=Omega_h+D t³、U=V/(Omega+D)の全中心はFricke XYZ−eΣX²+D²(D−f)=0。中心特異Dは0,f（各A1一つ）、2f/3,−f/3（各A1四つ）。Vの五characterはD0と2f/3に配置され、PI3のA1 McKay(1,2)で両値good。Df,−f3はV centre正則上でU=Mat3(singular centre)となりbad。compact中心C_Dは∞triangleで常にsmooth。辺のdegree0 radical v=ty^-1はv³=(T/Y)(1+q²v²),J³=(T),residue k(u)/k(u³)。非可換DVRでmax/PI3division、辺coverは両端totallyram3。CHI2.7/2.17 terminal theoremで∞全localgl2。従って全H3 iff(D−f)(3D+f)!=0、全Rdomain。

Bのcentre1=kt、V character五点だからBはskewでない（skewなら中央tを外すと量子3変数のcoordinate axes characters）。B CYのため非中央normal smoothE境界なら既証m3skewFermatに限られるが矛盾。唯一の中央t境界はtriangle。よって許容Rは既研究normal smoothE locusの外に実在し、missing-boundaryの一部分を埋める。証明cubic_quantum_triangle.tex、厳密validator/certificateはquantum_triangle。全intrinsic矢も確定：D不変、Aut_gr B=Gm×A4、次数scalarを除く慣性A4が全Dで一定。固有値差unitとcross linear係数比較により非被約底でも追加矢なし。相対rigidified表示stackはgood Dline×BA4、全中心形成も任意basechangeに適合。

### 一般qの三角境界

q!=0,+-1の全V_qに対し、q-difference表示の三関係とOmega=-Dを全係数で厳密検算し、PBW最高T係数のChebyshev独立性から全U_{q,D}・R_{q,D}の忠実性と整域性を証明した。B_qはCY AS4。非捩れでは全中心k[t,Omega_h]、位数N>=3ではChebyshev c_N(x),c_N(y),c_N(z),Omegaが全中心を生成。非捩れまたはN>3の全H3候補はこのpencilに限る。全候補graded矢は[Q/S4]、Q={(q,D):q!=0,+-1}、A4は基底に自明、奇置換は(q,D)->(q^-1,-q²D)。候補表示stackは分離DM2で慣性A4、任意基底のgraded同型functorを記述する。奇数位数N>=3では全許容性の判定は次の通りである：全中心はFricke XYZ+alphaΣX²+beta_N(D)=0、alpha=(q²−1)^−N、beta_N=−(q²−1)^−3N[2+P_N(w_D)]、w_D=−(q+q^-1)−(q²−1)³D/q²。特異DはN+1個、端点w=+-2の二値D±だけが非H3。全N−1内部特異値は、古典型w=−(q^d+q^-d)と非古典型w=q^(2d)+q^(-2d)、1<=d<=(N−1)/2の明示既約三重対角表示で全A1点に次元d<Nのsimpleが存在し、McKay( r,N−r )が両方正。無限遠triangleは指数Nのterminal order。従ってH3 iff(D−D+)(D−D−)!=0。位数5では独立な全係数2x2表示とPhi5中心配置も確認。任意奇数Nの表現再帰・Casimirは形式Q=q^d,J=q^j,R²=−q²/Qで厳密検算済み。証明cubic_quantum_triangle_general.tex、検算verify_cubic_quantum_triangle_difference.py。

### 偶数位数の三角境界

N=2M>=4、Gamma_i=−(q²−1)^N c_N(x_i)、k=2+P_M(w_D)により全中心はGamma_x Gamma_y Gamma_z−ΣGamma_i²−2kΣGamma_i−k²−4k+4=0。Huang1509.08719v4 eq5/§4.3を正規化して使用し、N4は独立PBW次数12で全関係を検算した。k!=0,4は持続A1三点、k0四A1、k4一D4。両端対角bのM次元三重対角表示が全k!=4の持続三点を覆う。k0内部の追加点には古典型r<M（既存M-simpleとA1 rank和2Mの排他性で追加点配置を証明）、k4内部には非古典型四つのd-simpleと古典型r=M−2dを置いて全五McKay指標を覆う。従って全D!=D±はH3。D+はM奇数ならAzumayaの特異A1中心商、M偶数なら四つのM/2-simpleでrankを使い切るD4なので常にbad。D−も全偶数位数でbadである。c_M(x)がy,zと反交換する正規元で、D4中心fiberでは二乗零なので各simple上零。xはM個の相異なるweightに分解し、関係式/Casimirの二元一次系（行列式はqの奇数冪−1の積）から全隣接block合成が非零scalarとなる。従って全simple次元はMの正倍数、full D4ならrank>=6MだがPI次数2Mなので不可能。これで全有限位数q!=+-1についてH3 iffD!=D±を完全判定した。中心・order・表現・全矢の分類は指定pencil内の主張であり全H3被覆ではない。粗座標theta=q+q^-1,w=−theta−h³D/q²を得て、候補stackはtheta!=+-2の平面上のA4共役twist中立gerbe。固定NのH3表示stackはphi(N)/2個の(A1_w minus{+-2})×BA4、全中心形成は任意基底変更と可換。全有限位数許容族は正規smoothE境界を持たず候補空間に稠密。1998 HKP math/9805048は根付き単位での表現を構成するが序文に完全性未証明と明記するため、全既約表現分類として輸入していない。

### 非捩れ三角境界

f_j(x)=x²−kappa²(q^j+q^-j)²の左右Ore集合を、左/右x乗法の2x2行列でdet f_j(M)=f_(j-1) f_(j+1)と証明した。局所化U_SはGWA G=A0(sigma,a_D)の反転固定環。A0=k[u±,r(q^ju)^−1:j∈Z]、r=u−u^-1、a_D=(u²+q²u^-2+1+q²)/(q²−1)²+(q²−1)D/q、A=rT,B=rbT^-1。反転u->u^-1,A->−B,B->−A、反不変単元rによりaveraging e fullなのでG#Z2とMorita同値。Bavula著者講義Theorem3.1（Dedekind基底そのものの定理）を一次監査：重根はgl∞、単根はgl<=2。非捩れqでD±の重根u²=−q,qは除去軌道u²=q^(2j)から外れるためU_SもUもgl∞、従って全非捩れ端点も非H3。D!=D±のU_S gl<=2だけで射影H3性は結論せず、U自体と無限遠には量子三角形の全許容性・境界認識定理を適用する。式はverify_cubic_quantum_triangle_gwa.pyで全有理式検算、証明cubic_quantum_triangle_gwa.tex。

文献上の障害：Kaplan–Schedler ANT2023「Multiplicative preprojective algebras are2-CY」は一次PDFを読むとTheorem1.2がunoriented cycleを含むquiverに限定され、affineD4はConjecture1.1の範囲。検索snippetがこの仮定を省くので誤輸入しない。EOR math/0406480 §11はlegパラメータdistinct時のMPLAとのMorita対応であり、全DAHAパラメータで有限globaldimを保証していない。これらを非捩れpencil全H3の証明として使わない。

### 三乗根量子so3固定包絡の全切断

全ZB3=P4[alphaOmega+betaX+gammaY+deltaZ+epsilon t³]を判定。線型元のnormは b³X+c³Y+d³Z−3q bcd Omega+(a³+q²a(b²+c²+d²))t³、像は正確にDelta=alpha³+27beta gamma delta=0の三次超曲面。全Delta0 cutは一次×二次に因数分解しnondomain。Delta!=0では境界はsmoothE、I1 nodalcubic、I2 line+conic、I3triangleの四種、phi=diag(1,q,q²)は各成分でdegree3、node両枝でfullyram3。centre境界滑らか、terminalorderでlocalgl2、非自明residueでgenericdivision3、全商domain。

Compact centreをS=3Omega/2f,U=X/2e cyclic,T=t³で正規化するとY:2UVW−T(U²+V²+W²)+3TS²+2S³=0 inP4。五ODP p0=(0,0,0,0,1),p_eta=(−1,eta1,eta2,eta3,1),eta product1。全四点rank4なのでplaneを含まず、全hyperplane section integral。H3 iff Delta!=0 andH notinY^dual。Yregular点のtangent cutはAzumaya singularcentreでbad、Ynodeで非退化A1ならonecharでfullMcKay(1,2)、退化rank2ならA2以上でonechar/PI3rankがfullMcKayを阻む。全矢・相対graded表示stack=[U/A4]、分離既約DM4、generic inertia1。全慣性は1,C2（v=(beta,gamma,delta)座標軸）,C3（四符号軸）,A4だけ。C2/C3固定planeはdim2、A4pencilはdim1、異なるplaneはpencilで交わる。表示族flat、全中心commutes任意basechange、fpqc降下。抽象intrinsic圏族の全被覆や全H3のcomponent性は未主張。

有限判定：affT1のF1=2UVW−ΣU²+3S²+2S³、H=aS+bU+cV+dW+epsilon0についてF1=H=0,gradF1=lambda(a,b,c,d),lambda!=0が空、かつHの通る各五nodeで法線Hessian逆二次式!=0。Groebner unit idealと五二次式で全切断を判定できる。検証full_cutsはuniversalPBWnorm、norm cubic、五node・全四点rank・inverseHessian、Casimirpencil bad2値との一致、H=S/S+U/U+V+Wのgood examplesとA4/C2/C3慣性をexact確認。論文cubic_quantum_triangle_full_cuts.tex。

### 三乗根共鳴incidenceと境界閉包

任意非被約底で全中心三次はalphaOmega_q+beta c3x+gamma c3y+delta c3z+epsilon t³、正確な条件は(q²+q+1)(beta,gamma,delta)=0。最高active次数でq−1,q²−1の単元比較により証明。被約incidenceは水平2次元と二つの垂直P4、交叉P1。qroot3、alpha1の局所式u beta=u gamma=u delta=0（u=q−q0）でdim2と4がdim1curveで交わり、接空間dim5。全候補矢はS4商、奇置換(q;alpha,beta,gamma,delta,epsilon)->(q^-1;qalpha,gamma,beta,delta,−q³epsilon)。整域fiber locusはDelta=alpha³+27beta gamma delta!=0。候補成分を全H3成分と呼ばない。

固定三乗根U/A4ではintrinsic normal smoothE locusが正確にbeta gamma delta!=0。他のnormal smoothE境界はB非skew/CYと既証m3認識で排除。missing-boundary Dは3座標超平面の商として既約normal-crossing divisor、正規化[U_beta0/V4]。I1/I2/I3のdim3/2/1、慣性1/C2/A4、全てsmoothE H3の特殊化。alpha1粗chartはepsilonとtetrahedral不変P=Σbeta²,Q=beta gamma delta,R=Σbeta²gamma²,J=平方差三積、J²=P²R²−4R³−4P³Q²−27Q4+18PRQ²。I2横断coarseA1、smoothE-C3横断A2、I3はA3/A4×curve。粗境界Q0はJ²=R²(P²−4R)、正規化A=gamma²,B=delta²でP=A+B,R=AB,J=AB(B−A)。証明cubic_quantum_triangle_incidence.tex、検算incidenceは普遍comm/divisibility/q反転と全12不変式、Molien一致を厳密確認。

### 三交換子alphaの量子三角形：全中心三次と三定数項の忠実模型

gamma非零・三角先頭のq≠0,±1、六下位係数A_i,B_iで中央Ωを決定。原始三乗根ではX=x³+q²A_yA_z t²x cyclicも中央。全低次数中心は随伴量子多項式の指数比較で尽くされる。各軸でA_iと純三乗切断係数が同時零なら自己Ext1三次元/shift行列式1で排除。非三乗根では全A_i非零となりA_i=1へ対角規格化、候補はΩ+Dt³。
規格化ペンシルでは差分作用素の指数0係数y₀,z₀とb(u)を三定数項付きで明示。全三関係、Ω=−D、反転・GWA定義元を厳密検算。最高shift指数の独立性で全B_i,Dの整域とGK rank-one。q³≠1の全幾何矢はS₄で、偶置換と二符号、奇置換は(q,B_x,B_y,B_z,D)↦(q⁻¹,−qB_y,−qB_x,−qB_z,−q²D)。
非捩れではu²∈q^Zを除くOre局所化は反転GWAの固定環。定義元a(u)はξ=u/ρ+ρ/uの四次式/(ξ²−4)。残る零点が単純であることがこの開集合の正確な有限大域次元条件であり、許容域の重根は既にH3を除外する。閉部分に沿う障害までは判定していない。公開verify_cubic_CY_three_alpha_triangle_center.pyとverify_cubic_CY_three_alpha_triangle_difference.py、本文cubic_CY_three_alpha_quantum_triangle節。全位数・全定数項の最終判定は `cubic_CY_three_alpha_quantum_triangle.tex` に従う。

### 節点と割線における全中央三次と割線の原始三乗根排除

gamma非零の節点・割線の元三関係を量子三角形へ二純平方P_xx²,P_yy²を加えた形で扱う。割線はP_x≠0,P_y=0。一般Casimirにq³−1を掛けて純三乗、txyおよび三つのt²一次補正を加えたJは全係数で中央。t=0の商をz個数濾過すると、q³≠1は最高xyzのみ。q³=1では[z³,y]のz²x²、[xyz,y]のx³yが他の項で消去不能で、中央三次はP_xx³+P_yy³だけ。この像をJが持ち上げるので全中心三次はkJ+kt³。z軸のA_z=0と割線y軸のA_y=0は点の全tails Ext1三次元とshift行列式1で排除。割線のq³=1ではJがx,tの可換二元三次となるため全切断を排除。
残る割線はA_y,A_zを1へ規格化し、量子三角形の差分係数の基本項b₀を(A_x−qP_x ξ/(q³−1))b₀へ置換。q²≠1の全残るqで忠実、整域とGK rank-one。非捩れの同じOre開集合のgldim有限性も、定義元の分子五次式の許容零点の単純性で必要十分。公開二検証器は両型の全中央恒等式、割線の三関係・切断・反転・定義元を厳密。本文cubic_CY_three_alpha_quantum_triangle節。

### 全有限位数量子三角形の体積ペンシルとMの境界

三定数項付きq有限位数Nの量子三角形の射影境界を全判定。Chebyshev中心のN乗根を中央付加して次数零を取る。自身が単元となる活動変数が指標冪等元を移すので固定環と半直積はMorita同値。辺はtを法として1次元 regularの巡回交差積、t正則より左単純pd≤2。頂点は重み(0,1,1,2)の先頭がx^N=1の量子Heisenbergとその正則三次商、得る随伴環は量子平面の巡回半直積。中央イデアル濾過との共終性と完備解消の持上げで局所有限大域次元。従ってH3とアフィンUのgldim≤2が同値。
Uが三Chebyshev中心上有限なので、全単純加群間のExt³消滅は完備中心ファイバーの極小解消から正確な判定。次元上界N³、U^e上有限自由解消を第四項まで可換中心多項式環上syzygyで構成。生成元行列代入とBurnsideにより単純性およびExt³非零条件は有限多項式/階数条件。実装は未実施。非三乗根の全有限位数量子三角形では許容性と既出幾何矢まで決定。
平方・積追加のM(s,w,z)のW-=0で新しい生成元順(b,a,c,d)から例外三曲線が残り、各zを解くと全域中心rank20。W+は固定as4の反対代数対応。M=0では順(a,c,b,d)で三線型と一二次曲線。二次の判別式はガウス有理数体の平方、両グラフの元商を再計算し全域rank20（別の消去で残ったs=1/2−i/4も再計算）。公開lower検証器・JSON 。

### 量子三角形・割線・節点の射影境界の判定

三角形体積ペンシルの全q、およびq³≠1の割線・節点の必要軸条件下で、H3はアフィン環Uの有限大域次元と同値。H=R/(t)は点行列と三次の連続点評価から三角・割線二次・節点三次のTHCR。節点は境界が整域なのでt濾過により全切断が整域でrank-one。
各境界特異点の活動軸uについて重み(u,v,w,t)=(0,1,1,2)の先頭を取る。随伴環の正規uをOre局所化してtを切断で消去すると次数零は量子平面。点加群のtruncation上の一様重みスペクトル系列でExt⁴消滅、行列因子化の貼合せとTHCR境界の生成を適用。証明はcubic_CY_three_alpha_quantum_triangle末尾。

### 原始三乗根三角形の全許容性、有限割線の開域、FDC3の中央二次

原始三乗根の全六係数でZ(B)=k[t,X,Y,Z,Ω]/(F)。T=t³でFは三次、最高活動部はΩ³−XYZ、t=1中心はJacobianから正規。全中央切断で既約中心商CとC-torsion検査、正規中心の高さ一DVR上で階数9を得る。一般代数は三次reduced CHを満たし、斜体なら中心K上の次数3。可換三次曲面は有理または曲線上ruledなので、Brauer剰余の非零が分裂しないために必要十分。四中心標準アフィンの次元27以下の単純間Ext³（有限多項式判定）で射影許容性を厳密に決定。元三量子関係の単項変換と切断直線で全点付き矢。中心の厳密恒等式のみ実装・実行し、一般切断のBrauer/Ext全判定は通常証明で与えた。
有限位数の量子割線ではChebyshev中心Cₓの二特殊値の補集合でGWA固定環となり、有限大域次元は残る零点の単純性に同値。
FDC3のU=a−(hc+kd)/s、V=sb+c+d、r₀=A/eではQ₀=r₀²U²+(64hk r₀²/s+32pm r₀+64s)UV+V²。p,m,d/e,eで元関係係数がeに関して一次。次数三の48×64の関係行空間は四変数関数体上で階数44、全四交換子を含む。全許容域で中央性が特殊化しZ₃は二次商に単射。

### 原始三乗根節点と成分巡回三角境界を完了

q³=1の節点でλ³=P_y/P_x、ℓ=x+λyとすると、J/P_xはℓ³+q²A_zλ²P_x tℓ²+[q²A_z(A_y+λ²A_x)−λ(1−q²)B_z]t²ℓにkt³を加えたもの。元関係による全係数検算、全切断非整域。滑らかな先頭式の成分巡回三角境界では、対称低次項の平行移動でYZ=f_x(X,t)と巡回二式になる。結合則でX f_x=Y f_y=Z f_zは中央かつ最高部が非零。全中央三次が可換二元になり全排除。
Mの許容点(1,1,1)は中心階数20、中央二次商も16。FDC3はt=z=v=1,p=s+1,m=s−1としてs=0で許容FO1点(1,1216/22831,−1343/480)へ延び、元中心階数20。s=1/2は許容FDC3。従ってM・FDC3とも一般中心三次零。

### 有限位数量子割線の全許容性と幾何矢

b(qv)はv↦q⁻¹/vで不変。零・極を分けてノルム因子a₊を取り、その極をv²=1,q⁻¹と0,∞に限定。±ρ⁻¹でb(qv)の二重極係数は−Res(y₀)²（全係数検算）。ノルム一の−1,ρvで二留数の符号を独立調整し、差分作用がk[x]を保つ。N周期行列の特性多項式の定数項以外はT^Nに依存せず、底変更されたk[x]作用と一致してk[Cₓ]に属す。極次数はN未満なので実は定数。y,zのモニック次数N多項式が中心となり、斉次化も中央。全アフィンを有限中心上N³生成として単純間Ext³で必要十分判定、二特殊ファイバーを含む。A_y=A_z=1で対角・交換の全矢を明示し、DはD/r²又は−D/r²。中心の実行可能構成とExt有限判定は証明、一般入力のExt計算そのものは未実装。

### 非捩れの反転orderと全二重根の許容性

割線の差分分子を二根・三根に分け、s₀(u)=1/uの射影e=ω(u)+ω(1/u)s₀と、s₁(u)=1/(qu)の生成元T=(α/ω)(s₁−1)を取る。個々の折り畳み軌道根が単純な二orderは中心完備化で全行列環かIwahori型になり遺伝的。Laurent環上の交代自由積は導来誘導の完全列で大域次元高々2。Tの個数の濾過でeHeの最高係数はDⁿと[Dⁿ,x]で生成され、アフィン環と一致。平方自由五次ではeがfullなので全H3。四次・五次の重複度高々2では二根の配置を変えると両orderは遺伝的のまま、eを殺した非零半単純商の全単純で自己Ext²非零。導来corner三角の最高・最低コホモロジーの間に非零の正次数自己Homが生じるため、cornerの大域次元は無限。全二重根を例外weight軌道上も排除した。残る三重根以上は例外軌道以外に重根があれば既出GWAで排除。normと交差関係の恒等式は公開three_alpha_triangle_difference検算、遺伝性・導来消滅は通常証明。

### 非分岐の単独三重根とFDC3の積表示

四次・五次の唯一の重根が三重でξ≠±2なら、同じs₁軌道の二点をe側に一つずつ置く。両反転orderは遺伝的、e=0商QはIwahori行列orderの中央一様化元での商。Qは両矢長二零の二頂点Frobenius環。有限次元MについてExt¹_D₀(M,Q)=0、Ext¹_Aが2dim M、Ext¹_D₁がdim MなのでExt²_H(M,Q)≠0。任意の非零Mに有限長非零直和因子があるので導来corner障害が適用できる。残る高重根は固定点三重、3+2、重複度4以上で、非例外軌道外に重根があれば従来GWAで除く。
FDC3で固定as4のFDC5変換を全域へ適用しab=ba=−cdを厳密検算。P=4p,M=4m,L=r₀/(64s)でQ₀=L²a²+((P²−1)(M²−1)L²+2PML+1)ab+b²、判別式は4個の(1+(P±1)(M±1)L)の積。公開FDC --product-plane 。

### 節点のE6一般化DAHAの明示認識

Etingof–Oblomkov–Rains arXiv:math/0406480v3、第8.1節の四書換えを固定。qは同論文の変形係数の三乗。cの単純根λに対応する冪等元eに対しX=ebe,Y=eb⁻¹e,Z=eb⁻¹cbe。Z−f₂λX−e₂Yと三平行移動により節点三関係となり、Pₓ=−λ(q³−1)/q、Pᵧ=−(q³−1)/λ²、A_z=−λ(q²−1)/(q Δ)。中央Jはスカラー。公開検証器は全係数と許容な分母を七変数関数体で検証。定理6.5のF123模型でb=(ηE₁₃−E₂₁)/(η−1)、eの像は階数一。x,yの先頭が定数と隣接二極なので位数によらず生成、重み(1,2,3)のHilbert値で同型。倍率付き9×9ヤコビアンは(q−1)^17(q+1)^6(q²+q+1)^3/(59049q^8)なので全許容qで係数写像は支配的。
有限位数は定理5.6,5.9のAzumaya・中心滑らかさから稠密開H3。定理6.7と節点曲線のη↦η^Nによる中心部分環上の有限性、定理5.3のPI上界3Nから、E6単純根表示内の全有限位数は単純対第三Extで必要十分判定。非捩れは無変形の量子トーラスとC₃半直積から各qで一つのH3点。

### 節点E6の分離スペクトル全域で17語判定

分離三次部分代数A_iの自由積にabc=κを加えた微分の普遍性から、双加群解消の中間完全性を得る。左端の三成分はκ倍の1−T_a,T_a−T_ab,T_ab−1。各共通核の第一係数空間は有限次元右イデアルとなるがF123の次数1スカラー行列の持ち上げが次数を上げるので零。d₂のHom像は同時共役の差であり、非零Q=H/HeH加群Mに対するHom_H(Q,M)のtr対合がこれを消してExt²_H(M,Q)≠0。導来corner障害によりH3 iff Q=0。Qのcは二次式、逆元の二乗関係も用いてbbb,cc,bcbc,cbcb,bbcbbc,cbbcbbを短縮。17語で定義関係の左乗法行列の像を不変閉包し次元を厳密判定。公開検証器でq=2の零例と次元4の非full例を実行。有限位数・非捩れで稠密開H3が従う。
各A_iについてF123の正次数商はMat₃の直和でA_i双加群として自由、従ってHがA_iを双加群直和因子に持つ。fullでいずれかの三次多項式が重根なら、誘導と制限でA_iの無限大域次元がHと球面環へ伝わる。

### 節点E6表示で重根かつ非fullの全排除

次数2の基点自由pencilとF123の行列値節点曲線模型から、全行列値随伴環とeHの随伴加群はスカラー捩れ斉次環上有限。Hは左noetherian、eHはeHe上有限。各三次部分代数A_iがFrobeniusでHが左右A_i自由なので、相対双加群列の完全性とd₂の同時共役差は重根でも成立。有限次元MについてHは各A_i上入射的で、Ext高次零とExt²_H(M,H)=M*を右H加群として得る。eHeの有限大域次元を仮定するとC=cone(He⊗^L eH→H)が完全、コホモロジーは有限次元Q加群。最高次数の双対をQとテンソルすると非零の正次数自己Homが生じるが、eC=0からRHom_H(C,C)=Cとなり矛盾。E6単純根表示の全有限位数・非捩れで、平方自由三スペクトルかつ17語商零がH3と同値。

### 非捩れ量子三角形・割線の全重複度判定

補冪等元をr=ω^{s₀}(u−u⁻¹)で共役すると、差分係数は最初の二根係数a,bをqa,qbへ移し−1/qを掛けた形。定数移動の残りは有限極を持たずk[x]に入る。逆ノルムで四次・五次差分環をそれぞれ既知アフィンへ戻せるため両角はnoetherian。角からHへの左加群は各四生成なのでHも左noetherian。D_i=A⊕AY_iのY_i係数への射影からD_i≃Coind_A^D_i A。AのK/K/A入射解消を余誘導し、du/u留数和でExt¹の制限像をv⊗Y_i−vY_i⊗1と同定。交代自由積の完全列から有限次元MにExt²_H(M,H)=M*かつ高次零。E6で使った完全導来corner三角により、非fullかつ有限次元商なら大域次元無限。重複軌道の一根をe側に選ぶと非零商を作れる。一軌道の場合も二点を選ぶか固定点二コピーで非零となる。従ってFが平方自由との必要十分性が全値で成立し、従来の特別weight軌道・三重以上も全て閉じた。補角係数と極消去の公開恒等式。

### 節点型全域のE6トーラス商と判別式

cの選択固有値を一度q倍し、残る二対称係数をU,Vとする。qの三乗根θに対する三つの積1スペクトルの指標は(f₁,f₂)、(U/θ,V/θ²)、(e₁/θ²,e₂/θ)。規格化六係数をE6重み格子のLaurent式に直すと全単純反射に不変で、27,27,243,243,73,1063項。六つの基本軌道和を三角的に復元でき、各主要係数は全許容qで単元。元の単純根は三候補のどれかに存在するので球面認識は全射。72根（比18、三つ組の積と逆54）のいずれかの指標値が1なら、Weyl対称性でbの重根として全排除。根外で非full単純があれば、三共役類の積写像の微分と同時共役軌道の次元からn≤3。n=1,2,3の行列式はいずれも根指標1を強制する。従って節点H3は既約Weyl判別式の補集合で、全係数・全位数を判定済み。各qの次元6、q込み次元7の既約層、一般慣性自明。成分性・境界・定義された相対族の分類は第12節の成分定理と相対認識へ接続する。

### 節点の一様E6座標と分裂楕円の双加群滑らかさ

P_x=P_y=A_z=1への倍率を適用すると、六軌道和展開でθ指数は3の倍数となる。全qでqと根正則トーラス商の積になり、対角三乗根はE6中心の乗法、接線交換は(q,t)の同時逆転。切断定数のB_z補正込みで厳密検証し、μ₃⋊C₂の代数的表示スタックを得た。分裂楕円のS/(g−1)はS[g⁻¹]へ中心三乗根uを加えた環とのLaurent積比較で双加群滑らか。積の対角をu_L=u_R=1に導来基底変換してU⊕U[1]を取り、S^eの中心正則列による双対移行でCY2を得る。従って標数零の全非零切断でH3。無限位数の非分裂切断は八次対角判別式と線加群の判定に従う。

### 三角形と割線の混合位数判別式

元のPBW忠実差分表示の移動生成元をα(u)Lへ置換する。L=s₁s₀は形式無限二面体群の元で、qが有限位数でもLの冪は独立。e₀=(1+s₀)/2とe₀e=e、ee₀=e₀で角を形式差分環の共役不変部分に入れる。最高正移動係数はα_n A。D_α^nと[D_α,x]D_α^{n−1}の係数でその全体を生成し、q^n=±1にも同じ。従って角の同定・平方自由時の遺伝的反転orderからの大域次元2・重根時の非full障害が全位数で成立。三角体積切断は全q²≠1、割線は加えてq³≠1の範囲で四次または五次平方自由性がH3の必要十分条件。既存validatorにQQ(i)の位数4で角の形式積・最高係数をn=4まで追加して。有限中心の既存記述は保持し、許容性の位数別分岐を除いた。

## 10. 三交換子CY：加法境界と残余外積型

`cubic_CY_three_alpha_additive.tex` の `thm:cubic-CY-three-alpha-additive-H3`、`cubic_CY_three_alpha_nonsmooth.tex`、`cubic_CY_three_column_three.tex`。有限Dynkin根判定の理論と全係数消去の実装状態を区別する。

### 三交換子alphaの重複直線と共点三直線の削減

固定as4の三重直線四表示で、中央三次切断がd軸の点イデアルの二乗に入ることを、S=B/(a)のWeyl中心と明示中央liftから証明した。二重直線b²cでは、七つの低次係数を保って中央三次liftを計算した。SのOre導分による中心はk[b²c]。重複直線上でaの係数の二次式が消える点の二チャートでは、いずれも全tails自己拡大の漸化式が行列式1でExt1が三次元となり、強いH3のSerre traceに反する。共点三直線では下位二次式が共点で零であればaを法としたOre中心とa²までの交換子で切断が点イデアル二乗に入る。同じSerre障害が固定五族のうち四族を排除する。
本文cubic_CY_three_alpha_nonsmooth節、公開再現器verify_cubic_CY_three_alpha_repeated_lines.py。三重直線四表示と二重直線の全係数・両チャートは厳密。

### 外積・列係数とも階数三の全中央三次

固定as4の必要鉛筆12型で、対称二次中心二元による商Cを復元した。元関係からの商次元(8,12,16)と中心三次を、分母・小行列式の全例外値を含む28検算で厳密に決定した。包絡の中心三次はCの中心三次へ単射。残るのは半単純二重円錐の比4、長さ二・異固有値の係数1/4、四基点の\(P_B=\lambda^2+(-4\mu^3+6\mu^2-4\mu)\lambda+\mu^4=0\)だけである。
三範囲では中心三次が正確に一次元。Cでの生成元は最初の二型でc³、四基点の有理化ではc²(d−(η−1)c/3)。対称五関係の各持ち上げ方向に対し、一次補正列と全を合わせた行列はともに階数4。逆転対合で二次中心イデアルの平方の誤差を消去し、四基点の残る値は一定Hilbert値の元の包絡族における核次元の上半連続性で覆う。本文cubic_CY_three_column_three節と公開二検証器・JSON。固定as4の元の鉛筆被覆と七係数表示は輸入。

### 外積階数三の残る三鉛筆を全排除

三つの中央三次はすべてL(da−cb)となる。半単純二重ではL=b−c、長さ二・異固有値ではL=(3a+2b+4c)/8、四基点P_BではLをηの多項式で与えた。全対称関係係数から独立な積恒等式を、三交代関係のみで割った次数三商で厳密検証。四基点の計算で除いた値も、元の定Hilbert値の包絡族の次数四で中央性を特殊化。da−cbは元の対称関係の補方向で非零。切断は低次数に非零零因子を持ちH3ではない。外積階数三は列係数階数二と三を尽くしたので全排除。三交換子の残る候補はalphaのgamma非零のみ。

### 尖点・接線・共点型の中央ペンシル、整域とアフィンKleinian還元

固定as4必要表示の尖点 b³+c²d、接線 b²d+bc²、共点 bc(b−c) に対し、中央三次を全てkL+ka³に決定。境界中心次元は次数1,2,3で0,0,1。尖点・接線でa d²の係数Cが零なら、d軸の自己Ext¹が三次元、shiftの行列式1となり排除。共点の先行排除の後はC=1。
三型の重み(a,b,c,d)=(0,4,3,6),(0,2,3,4),(0,2,2,3)で三次切断の可換随伴環は k[a,b,c,d]/(F₀+C a d²) となり、aに原始一次なので全値整域。R/(a)でのdの正則性とd冪降鎖、Rでのa冪降鎖により内在的rank-one。a=1でJacobian Poisson付きKleinian E₆,D₅,D₄量子化となる。可換随伴射影の境界は滑らか。本文cubic_CY_three_alpha_additive節・全係数を再生する公開検証器。

### アフィンの有限判定とd軸の完備局所環

尖点・接線・共点の量子化を重み二倍でk[k²]^Γへ同定し、Losev命題3.17とCrawley–Boevey–Hollandの対応を用いる。元の三生成元の球状像を重み上界内のPBW語で未知係数表示し、三関係と切断を代入、最高記号の生成を階数条件とする。有限式の存在は複素数体から標数零代数閉体へ移る。根条件xi·alpha非零を加えればアフィン有限大域次元の必要十分判定。有限式の消去は未実装。
別の減少重み(2,1,1,0),(2,1,1,0),(3,1,1,0)で最低記号を取り、有限商でdのadjointが局所冪零なので左右Ore局所化。次数零の逆極限の随伴環は尖点・接線でJordan平面、共点で可換平面。従って三完備局所環は左右大域次元高々2。具体的にはH=R/aの点行列の行列式は順に−3(b³−bc²+c²d), −b(b²−3bd−3c²), 3bc(b−c)で、各曲線の唯一の特異点はd軸。Hの点スキームへの表示、特異点の完備局所化とtails Extの比較、またはd軸点の完全性を行列因子化で直接証明する。

### 尖点・接線・共点型の全H3切断と幾何矢

三つのH=R/(a)を被約三次曲線EのTHCRと同定した。点行列は左右で階数2、全成分の開A¹でshiftはu↦u+1。L₀の連続三点評価は零、六二次語の評価階数6、n≥2は基点自由pencilで積全射。唯一の特異点p=d軸。
P=πk[d]の自己Extを、増大重みからw(d)·元次数を引いて可換随伴環と比較する。Pの全truncationは元次数のみシフトし、各解消段のHom重み支持は一様有界。tails Extのtruncation直極限に重みスペクトル系列を適用し、可換面でpが滑らかなのでExt⁴(P,P)=0。AS4からのderived restrictionのTor₀=P,Tor₁=P(−3)により、line twistの厚い部分圏を法としたP→P(−3)[2]は同型。二乗が零なのでPはその厚い部分圏に入る。
Eでは線束とk(p)でDᵇを生成。pだけで消える切断の補集合は滑らかなアフィンで、そこでのベクトル束の分裂射を分母払いして延長できる。従って全a-torsionがR twistの厚い部分圏に入り、既存の中央行列因子化の貼合せが適用可能。H3条件はアフィンの有限根判定と同値。包絡全同型の作用phi(L)=sL′+u(a′)³, phi(a)=r a′で切断座標はlambda′=(u+r³lambda)/s、次数スカラーを除く。各固定包絡の幾何学的一般アフィンはDの中心局所化なので有限大域次元、有限多項式判定の構成可能性から除外切断値は有限。有限消去自体は未実装。
gamma非零alphaの判定では、滑らかな先頭式、節点、割線、量子三角形を別々に扱う。特に点truncation法は非捩れ量子三角形・割線の境界頂点へ適用候補。

## 11. 三交換子CY：滑らかな楕円境界と加群による障害

`cubic_r13_cut_reduction.tex`、`cubic_finite_order_criterion.tex`、`cubic_CY_three_alpha_elliptic_diagonal.tex`、`cubic_CY_three_alpha_elliptic_line_modules.tex`。双加群滑らかさ、左大域次元、低次元表現による必要条件は別々の主張である。監査上の状態は `cubic_classification_validation.json` に従う。

### 全無限位数楕円における八次判別式の必要十分性

先頭Hesseの滑らかな係数空間でτの1,2,3回恒等を除く。相対対角cochain F₋₃,F₀の第四コホモロジーがともに階数8、比較同型となる開Vは全無限位数点を含む。中央作用のモニック八次根被覆に固定(1,2,3)の有限エタール部分を入れると全係数の幾何群もS₈、有限平坦性により判別因子は既約。線加群のDVR延長は先頭を動かしても成り立つ。中心値のスカラー性は重み≤3なのでτの小位数除外だけを用いる。4,7,10の第四自己Ext有限窓を全体で閉条件とし、無限位数で真の非完全性に等しい。一般先頭の変曲点におけるm₁=prx+qry+pqz,m₂=q²x+p²y+r²zと(α₁,α₂)=(p+q,r)uから、最高二次係数は−r((p+q)³+r³)≠0。種数≥1の曲線と有限分岐により一般の一根に障害があり、モノドロミーが全根へ移し、proper閉像が全特殊無限位数へ伸びる。
これで非分裂無限位数楕円のH3はdet(λI−M_ω)≠0と同値。全H3幾何学的対象・切断・構造対象付き同値を定理thm:h3-complete-geometric-admissibilityに集約し、成分の幾何表示位相は一般次元3,4,5,8の互いに交わらない四成分。

### 無限位数楕円の全固定包絡に対する双加群判別式

先頭SのB(E,L,σ)商の次数n≥4で、a+b=n・a,b≥2の順積と逆順積をE×Eの対角とσ⁻ⁿのグラフへの同時制限にする。二曲線を引いた外積線束は(3a−4)H₁+(3b−4)H₂+2Δ₋の類でampleなので、Kodaira消滅により積の差が全射。Sの低次数可換子商は1,3,3,2で、次数3にgの非零像がある。従って8生成元、一般Etingof–Ginzburg公式を各有限行列のrank下界として比較すると全無限位数でk[g]上自由。斉次導分は商斜体上で内部化し、実装元の極支持に無限軌道がないので正則。次数0の偏極自己同型群のLie代数と中央元での降下でHH¹=k[g]Euler。体積類へのEuler縮約とConnesのCartan恒等式でHH₁≅HH₀の正重み部分をk[g]線型に得る。
中心差によるShamash完全列ではgh=0、相対HH³=HH⁵=0、HH⁴の分布は内部重み−6,−5,−4,−3に1,3,3,1。フィルターを持ち上げてもこの第四Extは8次元、第五Extは零。全切断の第四対角自己Extは8次元空間のω倍をλで余核にしたもの。切断の二周期作用とCY2双対から、その消滅は双加群滑らかさに必要十分。従って8×8の特性多項式の根以外はH3。定理thm:cubic-CY-three-alpha-elliptic-diagonal-test。

### 二次元単純の全trace表示と八次判別式の有理数検証

行列を半trace uとtrace零Y_iへ分ける。三関係のtrace零部分は構造行列P=−2Jac(F)/(p−q)を持つLie括弧であり、spanが2以下なら可解性から単純でない。Pが可逆対称ならsl2の基底として実現し、PGL2 torsor。半trace二次は−adj(P)/4、三次は−det(P)ε/8。三関係の半trace二次とdet非零、中央切断式で全幾何共役類と自己Ext¹のJacobianを記述。先頭二次の係数a=r(p²+pq+q²),c=−pq(p+q)−r³は、a³+c³=−(p³−r³)(q³−r³)((p+q)³+r³)。Hesse座標の三乗一致は射影対合の固定点で六捩れなので、無限位数ではa≠0かつa³+c³≠0。三二次の候補は長さ8。
公開diagonal検証器はaffine PBW値次数7まで、差のShamashホモトピー、3,4,5次cochain、8×8作用を計算。先頭(1,2,3)上のsplitはλ⁸、下次対角(1,1,1/2)は既知の障害λ=0を含む。下次対角(1,2,4)では有理数上既約八次。中央値代入後のスカラー理想と可逆trace二次元理想は双方単位。八つ全ての双加群非滑らか根に一次元・二次元単純なし。

### 固定先頭の重み付きfilteredモジュライと幾何S₈

先頭C=S/(g)の同定付きfiltered deformationを任意底で認識。二次補正の線型行列は巡回恒等式と純交換子の独立性で対称。平行移動u_i=A_ii/(2r)で一意に対角零にする。三次切断核をgへ底変更し、左右乗法の階数で主イデアル。正常化作用はtを固定、Sで恒等なのでX_i↦X_i+v_it、二次式の対角線型係数2rv_iにより消える。低次係数A⁷、倍率重み1,1,1,2,2,2,3。固定無限位数先頭の八次Extは相対有限窓のベクトル束なので判別式は重み24。
先頭(1,2,3)の有理標本A=diag(1,2,4), b=0は八次既約、5と17で(1,7),(2,3,3)。推移的原始群の互換により算術S₈。A=diag(1,2,a)のλ^j係数はa次数≤3(8−j)。整数a=0..24の有理数計算を37で還元補間し、λ根の判別式にa⁴+2a³+22a²+9a+21が重複度3。未使用12点でも判別式評価を照合。幾何正規部分群は奇置換を含むのでS₈、固定境界の重み24の双加群非滑らか因子は幾何既約。Rainsの重みと一致するが、楕円E6 Weyl商からの写像の基点の有無や、根での左大域次元を同一視しない。

### 無限遠一点の二周期加群と固定(1,2,3)楕円のH3完全判定

無限遠Pの点加群は左一次関係ℓ₁,ℓ₂とsyzygy(m₁,m₂)。m鉛筆の基点はτ⁻²Pで、点グラフでの評価と次数2線束のPicard移動から従う。持ち上げℓ_i+α_iが点随伴を持つ必要十分条件は低次T₁+Σα_i m_i+Σc_iℓ_i=0とT₀+Σc_iα_i=0。前者はアフィン直線、後者は二次。自己Endは点の非周期性からk。中心切断fにmℓ=0、aℓ=f、b m=fI−ℓaを解き、P=(m;a),Q=(b,ℓ)のPQ=QP=fIで周期解消。有限pdなら1であり第四自己Ext消滅と同値。斉次先頭の絶対自己Extは次数0重み0、一次重み−1,0、二次重み−2に各1。変換列で商の第三・第四の正側の重みを制限し、重み≤−3の4,7,10項が正確な有限pd判定となる。
filtered点加群schemeの接空間はExt¹_D(M,M)：次数≤1の関係の変分とsyzygyのstrict持ち上げで全クラスを得る。中央正則商の境界射はωの微分で、微分零と無限pdは同値。切断係数への線加群写像はproper。DVRで同次巡回イデアルを交叉させ、特殊化のtが一次関係に入ると境界の一一次関係商のHilbert値が≤3でn+1に矛盾。tが一次関係に入らないと二一次関係の境界商値が≤1で、tの全次数正則性と点随伴を得る。従って非完全な線加群の像は閉。
点上のアフィン直線束の方向Kが次数−3、syzygy線Jも−3。二次最高係数はJ^∨⊗K⁻²の次数9切断で、(1,2,3)の変曲点で−18u²なので無限遠の点が生じる。一般の包絡で曲線は滑らか、終端はproper性で中心値の極となる。Eを支配する成分の種数≥1なのでRiemann–Hurwitzで有限臨界値が存在。S₈により一般の全八根、proper閉像により固定先頭の全係数で非H3。

### 良い楕円中心拡大の全切断と分裂族の完全な固定ambient分類

papers/sections/cubic_r13_cut_reduction.tex。固定Bについて、CY AS4・中心正則一次t・active随伴環S[t]・Sの低次中心Z1=Z2=0,Z3=kg・gを持ち上げる中心Ω・H=S/(g)が滑らかな整楕円曲線のTHCR、という仮定を明示した。全R13境界を覆うという仮定はしていない。

- 全λで gr_active Rλ=H[t] が整域となり、Rλ=B/(Ω+λt³)も整域。Hilbert多項式の加法性から低成長部分をA0,A1へ入れ、tの冪の鎖と境界coh EによりO∉A1を証明した。全非零右イデアルがfRを含むことと商の成長低下により、Oは全λで内在的Gabriel–Krull rank-one torsion-freeとなる。整域性からこのrank条件を無条件に推論したものではない。
- D=B[t^-1]_0, ω=Ω/t³ とすると、正確な残条件は **Λ_B={λ:gldim D/(ω+λ)<∞}**。滑らかな境界と行列因子化の分母払いにより、この条件からtails gldim=2を証明した。逆向きも中心局所化のExtで確認した。この固定ambient認識補題単独は例外値の有限性を与えない。楕円全域の八次判別式と相対開性は `cubic_CY_three_alpha_elliptic_diagonal.tex` および `cubic_presentation_components.tex` を用いる。
- その他の飽和、例外性、AZ、Serreとheart保存は全て確認した。固定ambientのH3幾何学的群oidはΛ_BへのPAut(B)の作用群oid。φt=at, φΩ=bΩ+ct³ならλ↦(c+a³λ)/b。相対stackの表示と無条件には同一視しない。
- 複素数体上、有限生成定義体k0上超越的な全λはadmissible。RSV Lemmas3.2/3.3を原文で再確認し、中心局所化と代数的分離拡大だけを用いた。可算例外から有限例外や有理点の存在は推論しない。
- **有限位数translationの楕円境界を持つ固定Bでは非admissible値が有限個、Λ_Bは非空Zariski開となる。** Rains arXiv:2107.13540v2 Theorem2.13を原文で確認し、全切断代数U=D[a]/(ω+a)≅Dの中心をfiberwise一定rankの交換子行列から持ち上げた。中心上有限を示してRSV Proposition2.1へ適用する。一変数の十分な開集合の補集合が有限なので実際の悪い集合も有限となる。
- **分裂中心拡大B=S[t]では複素数体上Λ_B=C*を完全に決定した。** 非零λはスカラー作用で一軌道で、超越的な良い値から全非零値へ移せる。λ=0ではP=πk[t]のExt^n(P,P)がH上kの最小Betti数と一致し全nで非零。逆Hilbert級数(1-z)²/(1+z+z²)が多項式でないため解消は終了しない。
- Sのpoint schemeが滑らかなEで非零translationを持つならAut B=Aut S×Gm。固定ambientの全H3群oidは **BH_S**、H_S={(ψ,a):ψg=a³g}/対角次数スカラー。1→μ3→H_S→PAut S→1。これは非分裂変形のrigidityではない。

検証器 computations/verify_cubic_r13_cuts.py はQQのSklyanin(a,b,c)=(1,2,3)で中心次元0,0,1、分裂包絡の中心三次140×20行列rank18、point曲線の滑らかさ三chart・非零character不在三chart、Hilbertと作用の恒等式を確認した。AS正則性、THCR認識、高次Extや全λの滑らかさを低次rankから推論していない。

### 滑らかな先頭三次の全中央ペンシルと楕円境界

Hesseで先頭をSklyanin(p,q,r)へ移し、r(p−q)≠0、(p+q)³+r³≠0。点曲線は滑らかな楕円か三角形。楕円では平行移動(p:q:r)の位数1,2,3を元の条件で排除。三角形では位相とFourier変換で(1,0,−h)、h≠0,h³≠1。点shiftは三成分を巡回し、三乗が各辺でh³の非自明倍率。両場合でTHCRへの全射と低次数中心なし。Etingof–Ginzburg定理3.3.2を全低次ポテンシャルへ適用し、次数3の中央持ち上げを得る。複素数体外へは有限次数の線型階数を移す。従って全包絡で中央三次はkL+kt³。元の変曲点枠による全矢の切断条件も決定した。
楕円の場合は既存良い楕円中心拡大へ全域で接続。有限位数は既存中心・局所McKayが必要十分、無限位数は一つのアフィン判定。gamma非零alphaのうち中央三次だけは全先頭型で判定済み。

### 非捩れ楕円切断のキャラクター偶奇障害

アフィン包絡CY3と中心正則商の双対移行から、有限次元U加群MにRHom_U(M,U)=M*[-2]。H3での完全性によりExt¹(M,M)のYoneda積は非退化交代対合となる。一次元表現では次元=3−rank Jacobian。(1,2,3)のSklyanin先頭とAの行(a,a,0),(a,a,0),(0,0,b)（ab≠0）で、斉次Gを二変数有理体で厳密検証。Gの線型項はAとの同一行空間で、原点自己Ext¹が1となる。先頭Eの5,17素数還元点数9,21と非変曲点により全例の境界は無限位数。中央三次と還元の小証明書を保持。

### 全楕円一次元加群の有限射影次元と非スカラー障害

中心正則切断の周期自由解消を、包絡の長さ3の解消と二つの次数1,3ホモトピーで構成。分母はrとq−1のみ。原点で第5微分は零、第4は4×4でdet=(q−1)⁻²Ψ(adj A)。Ψは余因子行列の成分の三次式。第4自己Extの消滅は完全性に同値で、有限射影次元は2。階数1以下は全排除、階数2は境界式の平方、階数3にも排除例がある。三二次可換完全交叉により固定包絡でスカラー障害となる中心値は高々8。別の(1,2,3)非捩れ切断では5s²=9、包絡の右辺sx+3,sy+3,−z/s−3s²、二次元単純(X,Y,sXY)の16×12接行列は階数8、自己Ext¹は1。スカラー理想はGröbner基底1で一次元表現は空。Waltonの博士論文のV.9にも反例。これは高次元・無限次元を含む全アフィン判定の必要性を示す実例。

## 12. 成分、有限表示、相対再構成

相対結論の定義域は、本書冒頭と `def:h3-intrinsic-family` に記す。有限次数条件、通常の開性、全相対矢、有効降下を現行の二つの参照原稿で組み合わせる。任意の平坦Abel圏変形にこれらの仮定が自動的に備わるという主張は含まない。

`cubic_presentation_components.tex` と `cubic_formal_intrinsic_reconstruction.tex`。相対族の定義は `def:h3-intrinsic-family`、四成分は `thm:h3-presentation-four-components`。三次平坦性を含む相対定義と、任意の平坦Abel圏変形でその仮定が自動かという問題を区別する。

### 全H3幾何表示の四成分

一交換子CYの全包絡は固定原始三乗根qで、可換二平面Uと二軸c,d、Uに対する倍率q,q⁻¹、dc=q²cd+f(U)（f任意二元二次）を持つ。唯一可換対を持つskew族では軸点の奇数自己Ext障害がc³,d³の存在を強制し、CY条件によりこの族のf=0となる。全許容切断はP+Cc³+Dd³、P≠0かつCD≠0。fをPと共通零点のない非退化式へ動かし、その倍率を動かすと基点自由の六次式ペンシルが一般に平方自由になるため、既知の許容開が全一交換子を特殊化として含む。U,c,dを固有空間ではなくGrassmann多様体と射影空間で延長し、整域性からc,dのUへの入り込み・U法比例・第六関係の二元式への退化を全て排除した。従って全整域表示内でこの包絡族は閉。
中山traceは二次双対Eの次数3,4のrankを4,1とする局所閉stratumにおける二つのFrobenius対合から正則である。全H3で値4,−2,0。trace4は一交換子と三交換子・可換三次曲面の二成分、trace−2は既約な全(1,3)符号表示、trace0は全(2,2) mixed rank4の曲がったClifford表示。一般幾何商はそれぞれ3,8,4,5次元、許容表示内で成分間の交叉・特殊化はない。定理thm:h3-presentation-four-components。

### 三交換子CY全域と可換三次の共通表示閉包

中心三次次元2の全α表示は先頭対称三次を変形し、各次数のDVR自由性と交換子核の底変更で中央三次を持ち上げる。原始三乗根の中心次元5では、独立純平方P_iとqを加えた普遍正則中央三次Jの一次項がΩ,X,Y,Z。q=−1でA_i=(q+1)U_iとすると、Jは全Clifford交代積＋t平方の切断を尽くす。q=1の一次項はxyz、純三乗、t平方、t²線型を独立に動かし、Hesseと平行移動で全可換滑三次を覆う。独立な中心値を加えた一般ファイバーは中心局所化でH3。滑らかな楕円表示は20次元、座標群12次元で一般慣性有限、幾何商8次元。節点全域は余次元1の同じ閉包に入る。表示空間の閉包としての結論を、`cubic_presentation_components.tex` の成分定理と `cubic_formal_intrinsic_reconstruction.tex` の相対認識・降下へ接続する。

### 一般noetherian底の相対内在族の全群oid

相対Serreと反標準軌道の導来Hom底変更により正次数sectionは有限局所自由。三次成分平坦な二次包絡は全次数平坦で、正則正規三次が主核になる。AZ再構成で反標準shiftを認識し、一般局所底でも有限自由torsion完全複体のtraceが中山次数スカラーを消す。従って表示は全H3開X^H3へ写る。逆向きはW₄⊗G^∨の重み一による規格化と、全表示の強noetherian性・coherent tails降下・相対Serreを用いる。構造対象を保つexact同値はSerre自然性と軌道の有限表示から全て次数同型を共通スカラーで割った矢。任意noetherian底の定義された相対群oidは有限型PGL₄商と同値で、四成分の一般次元は3,4,5,8。任意の平坦Abel圏Artin変形について、二次包絡の三次平坦性が自動かは未解決である。滑らかな可換三次点の次数付き環変形での結果を、非可換点や任意の圏変形へ拡張したとは主張しない。具体的には小拡大でW₃から三次切断線への残差を調べる。

### 三次平坦性の小拡大障害と可換三次点の全Artin変形

64×48の三次挿入の単元44minorを分離すると、小拡大の残差はW₃(B_k)→kG⊗Iであり、その消滅が全次数包絡平坦性と同値。一次では二次関係変分のKoszul dφ、正規商の短完全列・Frobenius双対により、HH₁(B)_1→HH₁(B,B_μ)_4のG倍核へ入る。可換点ではΩ¹のG倍が単射。HH²(R)_0の対称部分はJacobiansの20−16=4、交代部分は勾配の正則列から定数交代三形式Λ³k⁴で次元4。導分はEulerの1次元、枠付き接次元8+16−1=23。八次元成分の枠付き局所次元に等しく滑らかで、全次数変形への接写像は同型。Artin小拡大で滑らかなH3持ち上げと任意の次数変形の差を同じ接ベクトルで調整する。これで可換三次点の全Artin次数変形に二次包絡平坦性を要請しなくてよい。非可換点の全域は未決定。

### 内在Artin表示の有限次数条件と一般底での平坦性

二次関係Qの三次挿入の余核B₃が自由なら、核W₃も自由で底変更する。W₃⊗B_{n−3}→Q⊗B_{n−2}→V⊗B_{n−1}では、剰余体で中項がKoszul完全。最後の微分の剰余核を最初の微分の像から持ち上げると、余核B_nは自由。局所環の完備性やnoetherian性なしで全次数を帰納する。B₃=20とB₄=35、双対の次数3,4,5の階数4,1,0、Frobenius対合、B₄の四本の線型式だけで形式atlasを記述できる。幾何fiberが全てH3の任意底で、同じ条件から次数別平坦性が従う。追加文献入力を使わない直接Koszul証明。

### 全表示の通常の開性と有限型PGL₄商

整域B,R・正常Nakayama三次・有限大域次元という表示条件で、全必要被覆の入力を正規線型核・Frobenius/積階数・整域性・Serre作用に照合。符号族の一般斜体条件は整域性、残る射影・affine局所条件は有限大域次元で検査され、CYの全許容模型も既証のrankを持つ。従ってtrait一般化でrankを含むH3全条件が保たれる。全有限係数模型の構成可能像を取る。原始三乗根の追加中央切断では有限中心加群のtorsion判定と一般trace階数を広げ、一般分裂なら行列環同型を広げる。一般非分裂なら滑らかな射影中心の非零剰余一つをとり、tame symbolの三乗根被覆の幾何整域性で稠密開へ広げる。単純次元27の有限Ext条件も係数族上の構成可能条件。よって全H3集合は構成可能。正規化blow-upからDVRを取れば一般化安定、Zariski開。有限型PGL₄商、有限次数形式atlas、全四成分が同じ表示に載った。

### 強noetherian性・任意noetherian底変更・全平坦対象のSerre

有限中心、Ore、重みPBW、または中央t,gで曲線THCRへ落とす各幾何模型のnoetherian性は全noetherian係数環で成立。任意整な底の分数体の代数閉包で模型を選び、有限拡大と有限係数恒等式を主開へ広げる。閉補集合はnoetherian帰納法。補集合のf進完備化は随伴(T/fT)[s]と次数別収束でnoetherian、主開との積は忠実平坦。被約底は有限個の整商への埋め込み、非被約底はnilradical有限濾過。QGrは平坦線型加群圏のtorsion商なのでLVdB平坦。底代数作用と飽和右随伴により非平坦底変更も準coherent圏から得る。包絡のBeilinson四対象の自己準同型はdirectedで、E=A⁴に関するrelative barの非対角テンソルは長さ4で消える。底上平坦なcoherent対象の押出しは包絡perfect。各局所環で第四Extが零のため自己交叉二乗零、全平坦対象は商のshift生成厚い圏に入る。orientation付き相対Serreと任意noetherian底変更、fpqc降下が成立。

### 有限次数の相対H3開、包絡の有効降下と楕円表示の相対矢

Hesse係数空間の上で絶対小解消の生成元差・非可換微分・生成元差を使い、中央差のShamashホモトピーを有限重みで局所的に選ぶ。strict比較からフィルター付きHomは選択不変。切断対角の重み0以下の四次コチェイン完全性は二行列のrankでZariski開。そこでは中央差の変換二乗が境界なので対角は完全、相対CY双対で長さ2以下に短縮。任意底変更でも完全・射影。無限位数ではF₋₃C→F₀C→F₀C_λの短完全列と第三・第五の随伴消滅からH⁴(F₀C_λ)=coker(ω−λ; V)を得る。よって全無限位数の非判別式点が、その先頭位数を固定しないH3開に含まれる。公開diagonal検証器で三包絡の中心値0,1に、この有限ウィンドウの第四Extがそれぞれ8/0,1/0,0/0となることを有理数上で直接再生。
表示のPGL₄商のGL₄ gerbeにはdet(V)⊗G^∨の重み一の線があり、各次数を逆重みで捩ると包絡・切断・商が任意底変更に両立して有効降下する。強noetherian表示では飽和加群形成のflat base changeからtailsの対象・射もfpqc降下。楕円表示はtで割った相対楕円THCRのample filterと中央正則tで任意noetherian底上noetherian。相対Koszul解消と正則三次変換でRの飽和を証明し、shiftに可換する比較をデータに含めない相対矢を次数付き同型／次数スカラーに同定した。

### Artin上の内在section再構成・形式圏変形と相対双対

Lowen–Van den Berghの平坦Abel圏Artin変形に既知のexact反標準作用のliftがある場合、VdB命題5.1,5.3で例外構造対象の一意flat liftと全次数section自由・底変更を得る。幾何fiberのstrong amplenessは、任意のFへの負shift直和の全射、Serre双対によるExt²消滅、その核の同じ消滅からExt¹消滅で示す。VdB定理4.2とAZからsection環で圏を再構成。関係核の底変更とNakayamaにより任意のArtin変形で一次生成、全関係次数2,3。逆に平坦な次数変形のGrはLowen–VdB定理8.16の平坦加群圏、torsion局所化は入射のcoflat性と定理7.1で変形、8.8でnoetherian対象に戻る。これでliftしたexact偏極付き圏と次数環を往復する。
二次包絡も平坦な場合はB,Rの全次数Hilbert上界の小行列式を有限型Grassmann上で閉条件にし、各幾何点のArtin局所では下界が単元minorから自動。正規三次と相対Koszul複体を得る。相対Koszul双加群解消と正規商の二項変換でH³(R)のgraded双対は{}^μR(-1)⊗W₄⊗G^∨、μ=(μ_B σ)|R。orientationは共通次数重み1で、表示のcanonical降下にも使える。相対Serreが構造対象orbitで反標準と整合するなら、H³の左・右積のtrace比較からμは次数スカラー。Artinスカラーの自明性・相対Serre・一般底の開性と代数性は `cubic_formal_intrinsic_reconstruction.tex` と `cubic_presentation_components.tex` に従う。任意の平坦Abel圏変形で二次包絡の三次平坦性が自動か、という問題はそれらの仮定の外に残る。

### Artin相対Serre、中山スカラーの消滅、有限型形式atlas

包絡のaugmentation Koszul複体を商へ移したtorsion完全複体Xの内部次数0は底環一項。恒等射の分裂から相対traceは値1を取る。標的を[3](−1)と次数c^{-1}捩りに分け、traceの自然性とコホモロジー符号(+1)を比較するとc=1。従って非被約底でもμ_R=1およびGx=μ_B⁻¹(x)G。底上平坦なcoherent対象は、包絡への押出しの有限自由解消と三次変換射の二乗零により、商の全shiftで生成される厚い圏に入る。左右局所torsion複体をL、局所化をDとすると、D_A L=ω_R[3]とtorsion随伴よりD_A D=ω_R⊗D[2]。局所化されたshiftのdg Homの双対から相対Serreは逆中山twist・次数−1・orientation・コホモロジー2で与えられる。両環のHilbert上界と四本の中山線型式による有限型incidenceの形式完備化が内在Artin群oidを表す。全次数平坦な二次包絡を持つ場合の結果。

### 滑らかな楕円表示の全位数混合H3開

R^op⊗Rは楕円THCR二つの外積と中央二元の持ち上げで強noetherian。二重次数対角Δ_{i,j}=R_{i+j}の自由shiftからの導来Homは一重局所化複体D_Rの内部次数i+j。有限切り詰めから第六自己Extに底変更つき完全複体を得る。境界二元の導来制限は次数0,−1に相対対角と平行移動グラフの線束を持ち、そのExtは境界上で2より上にない。従ってj≥5で左右のtが同型を与え、射影第六自己Extはアフィン対角自己Extと等しい。消滅なら周期変換の三乗が零で完全。無限位数H3は双加群pd≤2、有限位数H3の各中心完備tensorは四変数正則環の有限群skew環にMorita同値なので第六が零。これで全位数共通のZariski開。相対的にも同じ消滅とCY双対でアフィン対角の長さ2以下の有限生成射影解消を得る。Chan 2000定理3.4・系5.8は著者一次本文で確認し、相対有限生成へ必要な帯の議論を原稿に記載。

### 局所noetherian底の平坦対象と幾何trait

次数別自由な連結環は残余noetherianなら完備化の随伴環T_k⊗gr Aからnoetherian。斉次イデアル各次数の補正係数を完備収束させ、一般イデアルは最高次数で有限帰納。局所底の平坦coherent代表はTor₁のtorsion性から高次数で各成分自由。B上の残余自由解消を持ち上げて長さ4を得る。BとRのcofinal局所torsionの同定から飽和各次数は底変更付き完全。有限切り詰めのHomを逐次錐で重ね、振幅が剰余で[0,2]なので局所極小化で同じ振幅を得る。自己交叉二乗零で全平坦対象はshift生成の厚い圏に入り、その相対Serreはorientationつき逆shift[2]。DVR一般fiberの全coherent対象を平坦格子で延ばして幾何一般fiberの大域次元2を証明。無限体拡大でのnoetherian性は非離散付値格子と各次数部分空間の自由直和分解から従う。この一般化の議論では、G-K二段商のrank条件の保存も `cubic_presentation_components.tex` の構造証明で確認する。重み一のorientation W₄⊗G^∨を使う次数スカラー降下は反標準section環そのものを降下させる。

## 13. 計算・文献照合の注意

検証器と入力・証明書は `computations/`、実行した検証の状態は `cubic_classification_validation.json`、外部分類の輸入範囲は `as4_imports.json`。本書には作業ログではなく、計算を誤用しないための条件を置く。

### 包絡・局所計算を用いる際の区別

固定包絡の正規三次核W1は必要条件であり、各切断の整域・rank・有限大域次元を別に判定する。非CY符号型を保持し、全対象をPymの一般族へ押し込めない。固定包絡上の切断分類を、全モジュライの既約成分性や内在変形のrigidityへ読み替えない。
全必要被覆と相対族の範囲は主原稿の定理を用い、個々のrank検算から全族の降下や一般の平坦Abel圏変形の認識を推論しない。現在の未解決問題と着手方法は研究方針を参照する。

### 再現と検証範囲

- python3 computations/verify_cubic_skew_strata.py
- python3 computations/verify_cubic_nakayama.py
- python3 computations/verify_cubic_skew_jets.py
- python3 computations/verify_cubic_skew_admissible.py
- python3 computations/verify_cubic_pym_generic.py
- python3 computations/verify_cubic_as4_reductions.py
- python3 computations/verify_cubic_r13_cuts.py
- python3 computations/verify_cubic_clifford_cuts.py
- python3 computations/verify_cubic_clifford_hesse.py
- python3 computations/verify_cubic_clifford_lift.py
- python3 computations/verify_cubic_clifford_beta.py
- python3 computations/verify_cubic_clifford_beta_action.py
- latexmk papers/weak_cubic_axioms.tex

最初の三検証器は標準ライブラリ。整数証明書の再生成だけ--regenerateとSymPy 1.14を使う。admissible検証器はSymPy 1.14で特性零の恒等式・Jacobian unit idealを、Pym検証器はQQ上の商空間・非零小行列式を検査する。詳細な検証状態はresearch/cubic_classification_validation.json、as4の採用範囲はresearch/as4_imports.json。独立査読・形式化・網羅的新規性調査は未実施。

### 正規三次incidenceを扱う二段階

中山条件を使う前の正常三次直線は、固定包絡の35×8乗法行列
`[Gv_1,...,Gv_4 | v_1G,...,v_4G]` の5次小行列式で記述する。
H3を認識した後は、商の中山作用が恒等であることにより
`Gv=mu_B^{-1}(v)G` の単一140×20線型核へ絞る。
正常三次を持つという必要条件だけでH3を結論しない。

### CYの低交換子射影で保存するデータ

対称階数4の一交換子問題では、対称射影 `U` 単体でなく組 `(im SS,U)` を保存する。
固定入力 `CY_ONE_COMMUTATOR_RANKFOUR_PROJECTIONS` の十六候補は非共有5・共有11。
最後の二型の積写像の核次元は3・2、他は1であり、階数5の円錐曲線型は別の排除を要する。
対応する必要被覆は `cubic_CY_one_segre_shared.tex`、`cubic_CY_one_segre_extensions.tex` と `as4_imports.json` を照合する。

### 再現環境と検証状態

SymPyだけでは全検証器を実行できない。少なくともFLINT有理関数体を用いる検証器は `python-flint` を必要とする。
数体・多変数有理関数の実装、数値行列の整数範囲、元関係への再代入、分母の単元性、特殊値を覆う証明書を個別に確認する。
部分関数の成功をスクリプト全体の成功と記録せず、有限標本を全パラメータの恒等式と扱わない。
### 独立E6研究との接点

楕円E6量子化成分の現行正本は [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) である。
同プロジェクトでの三次平坦性の整理には、45×48の二次関係挿入行列、44×44の単元小行列式、四つの残差係数、20の巡回potential方向に対する80個の斉次一次overlapという計算がある。
これは独立プロジェクトの参照事項であり、本分類でその全係数式や検証器を今回再実行したことを意味しない。輸入して用いる際は現行正本のcommit・定理の仮定・検算入力を改めて固定する。
