# 内在的非可換del Pezzo曲面と三次三様体のモジュライ

2026-11-15。GitHub mainが現行ソースの正本。最初に [研究方針](00_research_plan.md) を読む。逐次研究・約15分checkpoint・通常のmain保存については [AGENTS.md](AGENTS.md) に従う。GitHub Actions、force push、不要なPRを使わず、PDF・ZIP・中間生成物は追跡しない。GitHub保存成功時はLibraryに保存しない。

## Rains共鳴：混合A2のconnecting rankと局所heart比較

**指数+2/−1の実在混合A2で、connecting map δ:k²→k のrankは1と証明した。** 全q導来同値は仮定していない。より一般に、隣接根の指数がp,−(p−1)なら非分裂拡大Pのconnecting mapはrank p−1であり、(h0(P),h1(P))=(1,0)。非零e→Pが全射となり、その核がRainsのEuler等号条件からline bundleになることが鍵である。

q非torsion、H=−K nef、H²>0の下で、境界外圏Zは有限長Serre部分圏となる。二根S+,S−が生成するCはΠ(A2)の有限次元加群圏に同値で、直既約はS+,S−,P,Qの四つ。cohomologyは(p,0),(0,p−1),(1,0),(p,p−1)、T=add(S+,P)、F=add(S−)がC上のtorsion pairとなる。ΦはCの非零対象を消さない。全Z・全heartのtorsion pairとは区別し、内部Ext_Cとambient Extも同一視しない。

**残る導来比較**：p=2では0→W→V+→V−→0（両端一次元）が得られる。Φの完全忠実性には、WとV−のcharacterが異なり、この加群拡大が非分裂であることが必要。その場合A=R/(g−1)の作用像は次元3の三角行列代数。実際のcharacterと非対角項、全q導来同値は未決定。対象の非消失と射の忠実性は別である。

[公表用原稿](papers/nc_del_pezzo_resonance_hearts.tex) ／ [新しい完全証明](papers/sections/resonance_mixed_a2_category.tex) ／ [研究ノート](research/resonance_hearts.md) ／ [厳密検算](computations/verify_resonance_mixed_a2.py) ／ [検証状態](research/resonance_hearts_validation.json)

新スクリプトでHom/Euler/Ext表、4375通りのcohomologyと三角作用の四模型を有理数上で検算し、新証明節を独立LuaLaTeX driverで5ページに組版した。主原稿全体の組版・既存コードの全再実行・独立査読・網羅的新規性調査は今回の完了事項ではない。

### 保持する共鳴の構造結果

既約境界非交叉root sheafの指数m=chi(e,M)について全tau-orbitでh0=max(m,0)、h1=max(−m,0)、h2=0。負指数はRains heartのAZ ampleness失敗を検出し、反標準側では有限次元A加群[-1]に移る。これは導来非同値やqgr特異化を意味しない。Hilbert値1+d n(n+1)/2は不変。

次数1–6の全根が非零指数で同時に数値共鳴するgenuine smooth del Pezzo配置は、固定楕円E・非torsion qの各E^(9−d)でZariski dense。整数の単純根指数とE[3]の9選択で共鳴配置を記述する。最大共鳴の既約根sheafは単純根に限り、その直和のExtはADE zigzag。既知の形式性から固定dg圏内のframed変形は各辺のx_ij*x_ji=0で決まる。cubic E6の32個の5次元formal分枝は、曲面自身のモジュライ成分ではない。

## 14641型intrinsic H3の分類

大域的な最優先目標は強い内在的非可換三次曲面H3の完全分類。[分類計画](research/cubic_14641_codex_plan.md)、[現行分類ノート](research/cubic_14641_classification.md)、[主原稿](papers/weak_cubic_axioms.tex)、[検証範囲](research/cubic_classification_validation.json)を参照する。全対象の被覆・相対降下・大域的成分性は未完成。

全H3でmu_R=1、Gv=mu_B^−1(v)Gとなり、固定包絡の候補は140×20行列の単一線型核に絞られる。全skew包絡部分の幾何学的対象は31パラメータ・五型で分類され、一般同型類次元は4,1,2,1,0。量子基底の全非自明unipotent持上げ、指定Ore/CY層とPymの一般L112/R22/S23・非零E3は除外済み。既知as4入力の固定SHAと規約は [輸入記録](research/as4_imports.json) に明記する。

良い楕円R13のH3判定はaffine中心商の有限大域次元に帰着する。分裂B=S[t]の全非零切断は一軌道で、零切断は除外。位数二Cliffordの分裂全切断・非分裂対称beta族は、中心の滑らかさまたはClifford rank1の通常二重点を許す局所条件で完全判定し、全pointed幾何学的矢・慣性を記述している。gamma≠0への積分族は明示開集合上で平坦CY AS4となり、Hesse216と混合平行移動による一般八次元の表示商を持つ。これらを全H3の被覆や成分分類とは呼ばない。

**指定位数4固定包絡のD切断は完全判定済み**（現行H3原稿）：h=1、gamma^4=2、alpha=(−2,−2,0)、beta=(1,1,2)で中心特異値は13個だが、非H3値は次数6の平方因子なし多項式b(D)=(D−Dstar)*P4(D)*Q1(D)の根に限る。他のDのaffine切断は大域次元2。D直線の主開集合D(b)は底変更・fpqc降下と両立する。[局所orderの証明](papers/sections/cubic_order4_local_orders.tex)を参照。さらに[位数4全係数の幾何学的判定](papers/sections/cubic_order4_general_criterion.tex)を得た：中心特異点A1/A2/A3で、それぞれ次元1又は2の単純表現、異なるcharacter2個以上、異なるcharacter4個が必要十分。全係数族の相対開性・降下と全H3被覆は未完成。中心がDu Valであることだけでは十分でない。この並行成果を共鳴研究で独立再監査したとはしていない。

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
| 三次三様体と非可換P4 | [nc_cubic_threefold_moduli.tex](papers/nc_cubic_threefold_moduli.tex)、[研究ノート](notes/research_notes.md) |

量子FermatはHH_{−1}=HH_1=2、HH_0=5によりOU AS型でなく、intrinsic対象全体をOU/AOUの商と同一視できない。次数1の10次元dg候補族と全intrinsic abelian成分性は別問題。三次三様体の形式ambient37、中心対41、一般PGL商13/17、忘却fiber4という結果と、全大域stackの代数性・成分性も区別する。既存の全文・証明・必要計算は現行原稿に保持する。

## 手動再現

    python3 computations/verify_resonance_mixed_a2.py
    latexmk papers/nc_del_pezzo_resonance_hearts.tex
    python3 computations/verify_cubic_heart_numerics.py
    latexmk papers/nc_del_pezzo_hearts.tex
    latexmk papers/weak_cubic_axioms.tex

旧共鳴・corner・H3・次数1・三次三様体の検算と依存関係は、それぞれの現行研究ノート・validation・再現手順を参照する。Python3（必要箇所はSymPy）、日本語LuaLaTeX・LuaTeX-ja・latexmkを使用する。PDF/SyncTeX/ログは `.latexmkrc` の出力先へ再生成し、Gitでは追跡しない。実行済みの検証と、原稿に証明があるだけの事項を区別する。
