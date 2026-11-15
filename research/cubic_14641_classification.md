# 14641反標準型：現行分類ノート

2026-11-15 / classification-v2。再開時は 00_research_plan.md を先に読み、証明は papers/weak_cubic_axioms.tex の sec:14641-classification を参照する。

## 対象と同値関係

次数1・3共通のintrinsic weakly marked nc del Pezzo（exceptionalでGabriel–Krull rank-one torsion-freeなO、Serre逆作用、AZ ample、所定Hilbert関数）を保ち、三次のRがR1で生成され、二次包絡Q(R)が左右noetherian 14641型quadratic Koszul AS4であるクラス H3 を当面分類する。外部ambient、埋込み、4周期構造を標識として追加しない。RからQ(R)を作るので1周期表示は存在するが、全4周期AS Z代数が1周期的とは主張しない。圏の同型、graded同型、周期付きZ代数同型を区別する。

## 証明済みの主張

Levasseur, Some properties of non-commutative regular graded rings, Glasgow Math J 34 (1992), Theorem 6.2(ii), DOI 10.1017/S0017089500008843 により、noetherian AS4でGKdim=4のBは整域。Hilbert値 dim B3=20, dim R3=19, dim B4=35, dim R4=31 から核I3=kG, dimI4=4、GB1=B1G、正規・正則G、R=B/(G)を得る。従って六二次関係＋一三次関係は公理に不要。正規一次境界も不要。

AS部分は非空な真部分：可換滑らかなcubicはOU AS型、量子FermatはH3だが HH_{±1}=2 により非OU型。証明の依存先は papers/quantum_fermat_not_as_surface.tex。全OU退化境界のH3包含や全heart比較を主張しない。

正規三次incidence N3(B)⊂P(B3)=P19 は35×8行列 [Gv_j | v_jG] の全5×5 minor。整域性で左右4列はrank4。相対的なAS-flat chart上では正規三次直線の閉部分schemeで、普遍三次商は全次数局所自由。全正規三次商がintrinsic weak条件を満たすとは限らない。

CY skew polynomial torusの3-torsion 27点はS4座標置換で4軌道：代表000,001,011,012、軌道長1,8,12,6、中心三次次元20,5,6,4。非AS量子Fermat 110 は011軌道。全線型同型、Zhang同値、Abel圏同値による分類ではない。

## Skew torusの全正規三次直線：被約部分分類

papers/sections/cubic_skew_normal_incidence.tex に完全な証明を追加した。固定座標の量子多項式環で、全正規三次元は交換指標 χ_i(a)=∏_j q_ji^{a_j} が等しい単項式の線型結合に限る。Newton多面体の積の加法性と凸集合の消去から、正規化の線型変換が必ず対角となることを証明した。従って N3(B)_red は指標blockごとの互いに素な射影空間の合併となる。六次元パラメータトーラスは有限個のLaurent指標等式・不等式で層別化できる。一般fiberは単項式20点、中心三次は零。これは20個のintrinsic曲面を意味しない。

27個のtorsion ambientの四代表で、成分のベクトル次元は (20)、(5,3,3,2,2,2,1,1,1)、(6,3,3,2,2,2,1,1)、(4,2,2,2,2,2,2,2,2)。量子Fermat軌道では中心P5に加え非中心の2P2・3P1・2点がある。中心限定では固定ambient対も尽くさない。全線型自己同型による商や、非中心商の反Serre偏極・滑らかさ・H3帰属は未判定。

正規minor schemeの非被約構造と相対平坦性はこの定理の結論に含めない。証明は閉点分類から被約schemeを同定するもの。検算は既存スクリプトを拡張し、27点の指標分割とPBW交換係数、Q上の一般点で20単項式のrank4・190組の二項和のrank>4を実行した。組版はltjsarticle.cls/luaotfload不足で停止し、PDF表示確認は未実施。検証範囲は research/cubic_skew_normal_validation.json。新規性の網羅調査・独立査読は未実施。

## 次に実行するincidence分類（Codex優先）

全AS4 ambientを先に分類するのではなく、正規三次元Gを持つBを構造的に制限する。research/cubic_14641_codex_plan.md に詳細を記載。最初の具体的計算は R(1,3)、Pym graded CY六族、skew torus/量子Fermat交点での N3(B) のgeneric fiber、成分、非中心G、自己同型群、正規自己同型、qgrのintrinsic条件。次にas4/asz4の別族、境界、AS/OU非ASの交叉と代数的stackの降下を調べる。分類対象が網羅された証明がない限り完全分類と呼ばない。

## 次の優先課題

14641型ambientの各既約成分上で N3(B) の既約成分・generic正規元・自己同型を求め、Serre作用、rank、heart、AZ ampleを認識する。全モジュライstackの代数性、境界、全対象を覆うAS chartと同型groupoidは未解決。強いクラスの完全分類後に一次生成性・noetherian性を弱める。

## 再現

python3 computations/verify_cubic_skew_strata.py で27点・24置換の完全列挙と中心次元、Hilbert数値を検査し、computations/cubic_skew_strata_certificate.json を生成する。主原稿はLuaLaTeXで組版する。有限計算と通常の証明を混同しない。外部査読・形式化・新規性網羅調査は未実施。
