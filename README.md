# 内在的非可換del Pezzo曲面のモジュライとH3分類

2026-11-16。GitHub mainが現行ソースの正本。最初に [研究方針](00_research_plan.md) を読む。逐次研究・約15分checkpoint・通常のmain保存については [AGENTS.md](AGENTS.md) に従う。GitHub Actions、force push、不要なPRを使わず、PDF・ZIP・中間生成物は追跡しない。GitHub保存成功時はLibraryに保存しない。

## 論文別の現在の正本

| 研究 | 正本 |
|---|---|
| H3の内在的認識・完全分類 | **この `nc-cubic-moduli` のmain** |
| 楕円 $E_6$ 量子化成分・Fricke・DAHA | [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) |
| ambient／intrinsic／marked ASモジュライの比較 | [nc-cubic-ambient-moduli](https://github.com/uedakazushi/nc-cubic-ambient-moduli) |
| 量子Fermat三次曲面がAS surfaceでない短報 | [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) |

分類の主原稿に数学的に必要な認識定理・証明・コードは維持する。ここに残る別論文の旧TeX・ノートは更新の対象にせず、上記の独立mainを公表用正本とする。分類Codexはそれぞれの独立論文へ重複pushせず、必要な成果を正確に引用する。

## 独立したheart比較・Rains共鳴

四つのheart、Rains共鳴のHRS tiltと混合A2、cubic cornerの研究は [nc-dp-surface-hearts](https://github.com/uedakazushi/nc-dp-surface-hearts) を現行正本とする。

## 14641型intrinsic H3の分類

大域的な最優先目標は強い内在的非可換三次曲面H3の完全分類。[分類計画](research/cubic_14641_codex_plan.md)、[現行分類ノート](research/cubic_14641_classification.md)、[主原稿](papers/weak_cubic_axioms.tex)、[検証範囲](research/cubic_classification_validation.json)を参照する。全対象の被覆・相対降下・大域的成分性は未完成。

全H3でmu_R=1、Gv=mu_B^−1(v)Gとなり、固定包絡の候補は140×20行列の単一線型核に絞られる。全skew包絡部分の幾何学的対象は31パラメータ・五型で分類され、一般同型類次元は4,1,2,1,0。量子基底の全非自明unipotent持上げ、指定Ore/CY層とPymの一般L112/R22/S23・非零E3は除外済み。既知as4入力の固定SHAと規約は [輸入記録](research/as4_imports.json) に明記する。

良い楕円R13のH3判定はaffine中心商の有限大域次元に帰着する。分裂B=S[t]の全非零切断は一軌道で、零切断は除外。位数二Cliffordの分裂全切断・非分裂対称beta族は、中心の滑らかさまたはClifford rank1の通常二重点を許す局所条件で完全判定し、全pointed幾何学的矢・慣性を記述している。gamma≠0への積分族は明示開集合上で平坦CY AS4となり、Hesse216と混合平行移動による一般八次元の表示商を持つ。これらを全H3の被覆や成分分類とは呼ばない。

**指定位数4固定包絡のD切断は完全判定済み**（現行H3原稿）：h=1、gamma^4=2、alpha=(−2,−2,0)、beta=(1,1,2)で中心特異値は13個だが、非H3値は次数6の平方因子なし多項式b(D)=(D−Dstar)*P4(D)*Q1(D)の根に限る。他のDのaffine切断は大域次元2。D直線の主開集合D(b)は底変更・fpqc降下と両立する。[局所orderの証明](papers/sections/cubic_order4_local_orders.tex)を参照。さらに[位数4全係数の幾何学的判定](papers/sections/cubic_order4_general_criterion.tex)を得た：中心特異点A1/A2/A3で、それぞれ次元1又は2の単純表現、異なるcharacter2個以上、異なるcharacter4個が必要十分。固定位数の被約表示族では[相対中心・H3開性](papers/sections/cubic_finite_order_relative.tex)も証明した。任意底変更とfiber条件のfpqc降下に適合するが、有限位数を横断する変形・全intrinsic family stack・全H3被覆は未完成。 さらに[有限位数N一般の判定](papers/sections/cubic_finite_order_criterion.tex)を得た：中心がDuValで全McKay指標を含むことが必要十分で、次元3N²以下の有限中心fiberの正則trace形式から判定できる。中心がDu Valであることだけでは十分でない。この並行成果を共鳴研究で独立再監査したとはしていない。 [正規三次商の中央境界認識](papers/sections/cubic_normal_central_boundary.tex)ではCY包絡・中心Gの仮定を外し、境界が平行移動であること、有限位数がintrinsic PI次数であること、非可換中央境界の一意性も証明した。 さらに[中央滑らか楕円枝の包絡認識](papers/sections/cubic_central_elliptic_cy_envelope.tex)により、このH3部分の包絡は実際にCY、Gは中心となる。全H3がこの境界を持つとは主張しない。 [全filtered deformationの認識](papers/sections/cubic_filtered_elliptic_recognition.tex)ではAS4包絡と中心三次商を外部仮定なしに復元し、この非可換境界部分の全幾何学的矢をfiltered同型で記述した。

[正規一次楕円境界の認識](papers/sections/cubic_normal_elliptic_boundary.tex)も得た。非中央共役は位数2または3に限られ、位数3の全切断はD非零と同値にH3となり、[全包絡被覆](papers/sections/cubic_normal_order3_coverage.tex)から既知の量子Fermat一対象（幾何学的群oidBH54）に帰着する。位数2も[量子involutionの非skew排除](papers/sections/cubic_normal_order2_quantum.tex)と[Clifford swapの全候補・許容条件](papers/sections/cubic_normal_order2_clifford.tex)へ漏れなく被覆した。Clifford swapは中央volume切断の有限cocycle twistで、被約な長さ8 character完全交叉、同値に[明示四次式の非消滅](papers/sections/cubic_normal_order2_arrows.tex)が必要十分。境界は一意で、全intrinsic矢を任意底変更に適合する有限係数式で記述し、一般次元2・一般慣性mu2×mu2を得た。非skew・非CY H3の厳密例も得た。[中心幾何](papers/sections/cubic_normal_order2_scroll.tex)はcubic scroll F1上のrank4極大quaternion orderとなり、[二conicのBrauer分岐と全局所模型](papers/sections/cubic_normal_order2_ramification.tex)を記述した。表示族のrigidificationは分離既約DMstack2である。[三捩れ量子Weyl chart](papers/sections/cubic_quantum3_center.tex)は全中心とHessian・有限characterによる全係数の許容判定を持ち、b=(1,1,1),lambda=0では非H3四値を明示した。いずれも全H3被覆や全群oid・成分分類とは区別する。

[三角境界のq-so3切断](papers/sections/cubic_quantum_triangle.tex)でもDline全体を判定した。非H3値はD=f,−f/3の二つ。許容例は非skew CY包絡とFricke cubic中心を持ち、どの正規一次元でも滑らかな楕円境界を得られないため、上記normal-elliptic部分の外に実在する。

## heart比較とcornerの参照先

公表原稿・証明・研究ノート・検算コードは [専用リポジトリ](https://github.com/uedakazushi/nc-dp-surface-hearts) に移管済み。H3分類で必要な結果は固定commitと仮定を指定して参照する。

## 現行原稿と並行成果

| 対象 | 主原稿・再開ノート |
|---|---|
| H3の公理・認識・全切断の部分分類 | [weak_cubic_axioms.tex](papers/weak_cubic_axioms.tex)、[分類ノート](research/cubic_14641_classification.md) |
| 次数3のambient・R13・形式比較 | [nc-cubic-ambient-moduli](https://github.com/uedakazushi/nc-cubic-ambient-moduli)、[R13](research/r13_generic_moduli.md) |
| 量子FermatのOU AS障害 | [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) |
| 次数1のrank・weighted sextic・候補族（移管済み） | [nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli) |
| 次数1の反標準モデル・導来比較（移管済み） | [nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli) |
| 三次三様体と非可換P4（移管済み） | [独立研究リポジトリ](https://github.com/uedakazushi/nc-cubic-threefold-moduli) |

量子FermatはHH_{−1}=HH_1=2、HH_0=5によりOU AS型でなく、intrinsic対象全体をOU/AOUの商と同一視できない。次数1の10次元dg候補族と全intrinsic abelian成分性の問題は[独立研究](https://github.com/uedakazushi/nc-dp1-moduli)へ移管した。三次三様体の形式ambient37、中心対41、一般PGL商13/17、忘却fiber4等の結果とその証明・計算は[独立リポジトリ](https://github.com/uedakazushi/nc-cubic-threefold-moduli)へ移管した。

## 手動再現

```sh
latexmk papers/weak_cubic_axioms.tex
python3 computations/verify_cubic_skew_jets.py
```

その他のH3検証は `research/cubic_classification_validation.json` を参照する。heart比較・共鳴・cornerの再現は [独立リポジトリ](https://github.com/uedakazushi/nc-dp-surface-hearts) にある。PDFやキャッシュをGit追跡しない。
