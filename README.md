# 内在的非可換del Pezzo曲面のモジュライとH3分類

2026-11-16。GitHub mainが現行ソースの正本。最初に [研究方針](00_research_plan.md) を読む。逐次研究・約15分checkpoint・通常のmain保存については [AGENTS.md](AGENTS.md) に従う。GitHub Actions、force push、不要なPRを使わず、PDF・ZIP・中間生成物は追跡しない。GitHub保存成功時はLibraryに保存しない。

## Rains共鳴：全heartのtiltと混合A2のアフィン商

**指定のgenuine楕円gluingでは、反標準heartは全Rains heartの一回のHRS tiltである。** 滑らかな可換genuine del Pezzo S、滑らかな反標準E、q∈Pic0(E)からの構成に範囲を限定し、既存dP1原稿の全q導来比較を、orbitのInd生成・実際の境界trace・両位数の有限性・source飽和性に分けて点検した。自然ΦはDb(Rains)≃Db(qgr R)、全heartで振幅[0,1]。T=ker H1Φ、F=ker H0Φにより反標準heartは〈F[1],T〉となる。q非torsionでは全境界外Serre部分圏Zにも制限できる。任意のnc曲面、weak avatar、特異境界や相対familyへの無条件な主張ではない。

**混合A2のconnecting rankは任意の正負指数で決定した。** 指数p>0,−n<0の隣接根の非分裂拡大Pではrankδ=min(p,n)、(h0,h1)=((p−n)+,(n−p)+)。この証明は導来比較を仮定しない。二根の有限長Serre部分圏はmod_fd Π(A2)で、四直既約S+,S−,P,Qの全cohomologyと両chamberのtorsion pairを記述する。p=nならPが消えるが、genuine avatarではこの同時共鳴自体が不可能。

**指数+2/−1ではcharacterの分離と非分裂性も解決した。** 反標準側の0→W→V→U→0（次元1,2,1）はW≄Uかつ非分裂であり、Vへの作用像は全三角2×2行列代数。逆向き拡大V'を合わせるとA=R/(g−1)から四次元商A/Ann(V⊕V')≃Π(A2)を得る。新しい根はalpha+beta,−beta、指数は1,1で局所Weyl反射に対応する。商写像はhomological epimorphismではなく、内部Extの二周期性とambient Ext>2消滅を区別する。

残る具体的課題は、元の楕円データの生成元に対する二つのcharacterの値と非対角係数、商のkernelの生成元を求めること。表現の同型型の決定と、指定生成元の作用係数の計算は別である。全E6のアフィン作用、VdB/AS heartとの指定同定、退化境界・相対familyも未解決。

[公表用原稿](papers/nc_del_pezzo_resonance_hearts.tex) ／ [任意混合指数の証明](papers/sections/resonance_mixed_a2_category.tex) ／ [大域比較とアフィン商](papers/sections/resonance_global_heart.tex) ／ [研究ノート](research/resonance_hearts.md) ／ [厳密検算](computations/verify_resonance_mixed_a2.py) ／ [検証状態](research/resonance_hearts_validation.json)

有理数上で40,000通りのcohomology、Hom/Euler/Ext、四次元商の積・両三角像・Weyl反射を検算した。更新二節を独立LuaLaTeX driverで9ページに組版しページ画像を確認した。主原稿全体の組版・既存四コードの再実行・外部独立査読・網羅的新規性調査は今回の完了事項ではない。

### 保持する共鳴の構造結果

既約境界非交叉root sheafの指数m=chi(e,M)について全tau-orbitでh0=max(m,0)、h1=max(−m,0)、h2=0。負指数はRains heartのAZ ampleness失敗を検出し、反標準側では有限次元A加群[-1]に移る。これは導来非同値やqgr特異化を意味しない。Hilbert値1+d n(n+1)/2は不変。

次数1–6の全根が非零指数で同時に数値共鳴するgenuine smooth del Pezzo配置は、固定楕円E・非torsion qの各E^(9−d)でZariski dense。整数の単純根指数とE[3]の9選択で共鳴配置を記述する。最大共鳴の既約根sheafは単純根に限り、その直和のExtはADE zigzag。既知の形式性から固定dg圏内のframed変形は各辺のx_ij*x_ji=0で決まる。cubic E6の32個の5次元formal分枝は、曲面自身のモジュライ成分ではない。

## 14641型intrinsic H3の分類

大域的な最優先目標は強い内在的非可換三次曲面H3の完全分類。[分類計画](research/cubic_14641_codex_plan.md)、[現行分類ノート](research/cubic_14641_classification.md)、[主原稿](papers/weak_cubic_axioms.tex)、[検証範囲](research/cubic_classification_validation.json)を参照する。全対象の被覆・相対降下・大域的成分性は未完成。

全H3でmu_R=1、Gv=mu_B^−1(v)Gとなり、固定包絡の候補は140×20行列の単一線型核に絞られる。全skew包絡部分の幾何学的対象は31パラメータ・五型で分類され、一般同型類次元は4,1,2,1,0。量子基底の全非自明unipotent持上げ、指定Ore/CY層とPymの一般L112/R22/S23・非零E3は除外済み。既知as4入力の固定SHAと規約は [輸入記録](research/as4_imports.json) に明記する。

良い楕円R13のH3判定はaffine中心商の有限大域次元に帰着する。分裂B=S[t]の全非零切断は一軌道で、零切断は除外。位数二Cliffordの分裂全切断・非分裂対称beta族は、中心の滑らかさまたはClifford rank1の通常二重点を許す局所条件で完全判定し、全pointed幾何学的矢・慣性を記述している。gamma≠0への積分族は明示開集合上で平坦CY AS4となり、Hesse216と混合平行移動による一般八次元の表示商を持つ。これらを全H3の被覆や成分分類とは呼ばない。

**指定位数4固定包絡のD切断は完全判定済み**（現行H3原稿）：h=1、gamma^4=2、alpha=(−2,−2,0)、beta=(1,1,2)で中心特異値は13個だが、非H3値は次数6の平方因子なし多項式b(D)=(D−Dstar)*P4(D)*Q1(D)の根に限る。他のDのaffine切断は大域次元2。D直線の主開集合D(b)は底変更・fpqc降下と両立する。[局所orderの証明](papers/sections/cubic_order4_local_orders.tex)を参照。さらに[位数4全係数の幾何学的判定](papers/sections/cubic_order4_general_criterion.tex)を得た：中心特異点A1/A2/A3で、それぞれ次元1又は2の単純表現、異なるcharacter2個以上、異なるcharacter4個が必要十分。固定位数の被約表示族では[相対中心・H3開性](papers/sections/cubic_finite_order_relative.tex)も証明した。任意底変更とfiber条件のfpqc降下に適合するが、有限位数を横断する変形・全intrinsic family stack・全H3被覆は未完成。 さらに[有限位数N一般の判定](papers/sections/cubic_finite_order_criterion.tex)を得た：中心がDuValで全McKay指標を含むことが必要十分で、次元3N²以下の有限中心fiberの正則trace形式から判定できる。中心がDu Valであることだけでは十分でない。この並行成果を共鳴研究で独立再監査したとはしていない。 [正規三次商の中央境界認識](papers/sections/cubic_normal_central_boundary.tex)ではCY包絡・中心Gの仮定を外し、境界が平行移動であること、有限位数がintrinsic PI次数であること、非可換中央境界の一意性も証明した。 さらに[中央滑らか楕円枝の包絡認識](papers/sections/cubic_central_elliptic_cy_envelope.tex)により、このH3部分の包絡は実際にCY、Gは中心となる。全H3がこの境界を持つとは主張しない。 [全filtered deformationの認識](papers/sections/cubic_filtered_elliptic_recognition.tex)ではAS4包絡と中心三次商を外部仮定なしに復元し、この非可換境界部分の全幾何学的矢をfiltered同型で記述した。

[正規一次楕円境界の認識](papers/sections/cubic_normal_elliptic_boundary.tex)も得た。非中央共役は位数2または3に限られ、位数3の全切断はD非零と同値にH3となり、[全包絡被覆](papers/sections/cubic_normal_order3_coverage.tex)から既知の量子Fermat一対象（幾何学的群oidBH54）に帰着する。位数2も[量子involutionの非skew排除](papers/sections/cubic_normal_order2_quantum.tex)と[Clifford swapの全候補・許容条件](papers/sections/cubic_normal_order2_clifford.tex)へ漏れなく被覆した。Clifford swapは中央volume切断の有限cocycle twistで、被約な長さ8 character完全交叉、同値に[明示四次式の非消滅](papers/sections/cubic_normal_order2_arrows.tex)が必要十分。境界は一意で、全intrinsic矢を任意底変更に適合する有限係数式で記述し、一般次元2・一般慣性mu2×mu2を得た。非skew・非CY H3の厳密例も得た。[中心幾何](papers/sections/cubic_normal_order2_scroll.tex)はcubic scroll F1上のrank4極大quaternion orderとなり、[二conicのBrauer分岐と全局所模型](papers/sections/cubic_normal_order2_ramification.tex)を記述した。表示族のrigidificationは分離既約DMstack2である。[三捩れ量子Weyl chart](papers/sections/cubic_quantum3_center.tex)は全中心とHessian・有限characterによる全係数の許容判定を持ち、b=(1,1,1),lambda=0では非H3四値を明示した。いずれも全H3被覆や全群oid・成分分類とは区別する。

[三角境界のq-so3切断](papers/sections/cubic_quantum_triangle.tex)でもDline全体を判定した。非H3値はD=f,−f/3の二つ。許容例は非skew CY包絡とFricke cubic中心を持ち、どの正規一次元でも滑らかな楕円境界を得られないため、上記normal-elliptic部分の外に実在する。

## 四つのheartとcubic corner

Rains、VdB、AS、anticanonicalの四名称は由来を表す。VdB raw blow-upとsection-model qgrを区別し、導来同値・t-exactness・構造対象・反Serre・境界・rank・marking・族の降下を個別に検証する。振幅1の既知導来同値は(T,U)=(ker R¹δ_*,ker δ_*)によるHRS tiltを与えるが、全共鳴でのheart一致を意味しない。

Cubic cornerでは四交比の11 determinant条件が有限性に必要十分で、一般位置六点配置空間を復元する。一様C7=0が成立し7は最良、Hilbert関数は8+21t+33t²+38t³+33t⁴+21t⁵+8t⁶、総次元162で有限平坦族となる。古典的11根壁では2-sphericalなi_*O_D(−1)が反標準導来収縮で消える。非可換AS/Rains/VdBの壁上への適用は別問題。

[heart比較](research/heart_comparison.md) ／ [heart原稿](papers/nc_del_pezzo_hearts.tex) ／ [corner原稿](papers/cubic_heart_corner.tex) ／ [cornerノート](research/cubic_corner.md)

## 現行原稿と並行成果

| 対象 | 主原稿・再開ノート |
|---|---|
| H3の公理・認識・全切断の部分分類 | [weak_cubic_axioms.tex](papers/weak_cubic_axioms.tex)、[分類ノート](research/cubic_14641_classification.md) |
| 次数3のambient・R13・形式比較 | [cubic_surface_ambient_moduli.tex](papers/cubic_surface_ambient_moduli.tex)、[R13](research/r13_generic_moduli.md) |
| 量子FermatのOU AS障害 | [quantum_fermat_not_as_surface.tex](papers/quantum_fermat_not_as_surface.tex) |
| 次数1のrank・weighted sextic・候補族 | [nc_del_pezzo_degree1_moduli.tex](papers/nc_del_pezzo_degree1_moduli.tex)、[dP1方針](research/dp1_research_plan.md) |
| 次数1の反標準モデル・導来比較 | [dp1_anticanonical_models.tex](papers/dp1_anticanonical_models.tex)、[再現](research/dp1_reproduction.md) |
| 三次三様体と非可換P4（移管済み） | [独立研究リポジトリ](https://github.com/uedakazushi/nc-cubic-threefold-moduli) |

量子FermatはHH_{−1}=HH_1=2、HH_0=5によりOU AS型でなく、intrinsic対象全体をOU/AOUの商と同一視できない。次数1の10次元dg候補族と全intrinsic abelian成分性は別問題。三次三様体の形式ambient37、中心対41、一般PGL商13/17、忘却fiber4等の結果とその証明・計算は[独立リポジトリ](https://github.com/uedakazushi/nc-cubic-threefold-moduli)へ移管した。

## 手動再現

    python3 computations/verify_resonance_mixed_a2.py
    latexmk papers/nc_del_pezzo_resonance_hearts.tex
    python3 computations/verify_cubic_heart_numerics.py
    latexmk papers/nc_del_pezzo_hearts.tex
    latexmk papers/weak_cubic_axioms.tex

旧共鳴・corner・H3・次数1の検算と依存関係は各現行研究ノート・validation・再現手順を参照する。三次三様体は独立リポジトリを参照する。Python3（必要箇所はSymPy）、日本語LuaLaTeX・LuaTeX-ja・latexmkを使用する。PDF/SyncTeX/ログは `.latexmkrc` の出力先へ再生成し、Gitでは追跡しない。実行済みの検証と、原稿に証明があるだけの事項を区別する。
