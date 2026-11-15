# 研究方針：非可換del Pezzo曲面のheart比較と内在的モジュライ

## 14641型の内在的非可換三次曲面：当面の完全分類対象（2026-11-15）

統一intrinsic weakly marked三次曲面 (A,O) の反標準環 R をR1で生成されるものに限定し、二次包絡 B=Q(R) が左右noetherianな14641型quadratic Koszul AS4であることを要求するクラス H3 を分類する。外部ambient・埋込み・4周期同型は標識として加えない。公表用の主証明は papers/weak_cubic_axioms.tex の sec:14641-classification、再開用ノートは research/cubic_14641_classification.md。

【証明済み】Levasseurの整域定理（noetherian AS4, GKdim=4）とHilbert数値から、R=B/(G) で G∈B3 が左右正則正規となる。六二次＋一三次関係、三次核の正則性、正規一次境界は追加公理に不要。AS型は非空真部分：可換cubicはOU AS型、量子FermatはH3に属するが HH±1=2 で非OU。全OU退化境界が無条件にH3に入るとは未証明。

【有限方程式】固定ambient B上の全正規三次直線はP(B3)=P19の35×8乗法行列 [Gv|vG] の5次minorで表される。AS-flatな相対chartでも底変更と両立。内在的Serre/heart/rank/AZ条件の認識は別。量子skew torusの3-torsion 27点は座標置換で4軌道（1,8,12,6）、中心三次次元（20,5,6,4）。これは有限部分分類であり全moduliの完全分類ではない。

【優先課題】全14641 ambient成分上の正規三次incidenceの成分・同型群oid・曲面条件・境界・族と降下を決定し、その後intrinsic定義を弱める。GitHub mainを正本とし、GitHub push成功時はLibraryへの保存を行わない。PDFやZIPをGitで追跡せず、TeX・ノート・検算コードを追跡する。


2026-11-15 / project-v18 / recognition-v6 / hearts-v3。最初に本書、`research/cubic_corner.md`、`papers/cubic_heart_corner.tex`を読む。比較の共通枠組みは`research/heart_comparison.md`と`papers/nc_del_pezzo_hearts.tex`、共通公理は`research/common_del_pezzo_framework.md`。次数別・三次三様体の研究はそれぞれの現行ノートから再開する。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化し、目標と論文構成を柔軟に改訂する。方針は現在有効な形へ書き直し、変更履歴を蓄積しない。証明済み、追加仮定、既知入力、未完成、予想、有限検算を区別する。証明の記載、今回の点検、外部独立査読、新規性確認を混同せず、誤りの影響を依存する本文・要約・方針へ反映する。

一次資料の仮定と適用範囲を確認する。公表用原稿は日本語LuaLaTeXとし、有効な主張と完全な証明を保持する。研究ノートは現在有効な補足・障害・反例・再取得困難な情報を整理し、論文の証明を全文重複させない。軽量化は履歴・重複・不要物の除去で行い、数学的内容や検証可能性を削らない。

研究継続用bundleは現行方針・ノート・論文ソース/PDF・必要コード・小証明書・再現手順から自己完結的に再開できるものとする。旧会話・旧ZIPを前提にせず、旧版・中間生成物・キャッシュを収録しない。ユーザーは研究区切りで再承諾なくLibraryへ保存することを許可している。現行ソースはGitHub mainにも通常fast-forwardで保存し遠隔HEADを確認する。既存Library資料は無断削除しない。GitHub Actions・force push・不要なPRを使わず、GitでPDF/ZIP/TeX中間物を追跡しない。生成、証明点検、計算、組版、Library保存、GitHub保存を別々に報告する。

## II. 上位目標と最初の対象

一般の非可換del Pezzo surfaceに対し、Rains heart、VdB heart、AS heart、anticanonical heartを比較する。これはdP1だけの補助問題ではなく内在的モジュライの中心課題であり、最初の実行対象はcubic surface（次数3）。四構成の存在、同じ入力、realization、指定同値のt-exactness、構造対象と反Serre作用、境界restriction、rank、marking、族への降下を分離する。四ラベルが四つの相異なるheartを与えるとも、全て同じとも仮定しない。以後この四名称を固定し、Rainsのgluing由来・VdBのliteral blow-up由来などは構成の説明に限って用いる。特にVdBのblow-up heartとsection-model側のheartを定義上同一視しない。

最初のAS–反標準比較は、標識と構造頂点を固定したnoetherian AS chartの非空開部分でabel同値まで進んだ。全域比較、VdB/Rains側とのpointedness、共鳴ごとの非自明tiltは未解決。どのabel圏・構造対象を分類するかを確定してから全intrinsic moduliへ進む。数値的共鳴の稠密性をAZ失敗・導来特異化へ直結しない。

## III. 現在の到達点

### Cubicの四交比還元と明示的corner開集合

`papers/cubic_heart_corner.tex`が完全な証明と計算の意味を記す。B=Jac(Q,W)、e=e_(A0)、C=B/BeB。Cは道長1で生成されるのでC_N=0から全高次数消滅が従う。最大minorによるU_Nは開、U=union U_NはC有限次元locus。C有限から両corner bimoduleの有限生成性を導き、B右noetherianの下でqgr B_cut→qgr eB_cut eをabel同値とする。標準AS helixのfolding・Serre・飽和の範囲でeB_cut eは指定構造対象の反標準環。道長gradingと反標準cut gradingは必ず区別する。

六点(1:0:0),(0:1:0),(0:0:1),(1:1:1),(1:2:3),(1:4:2)から27係数potentialを切断の積で構成した。全関係を含む厳密計算でCのHilbert関数は[8,21,33,38,33,21,8,0]、総次元162。7次6804列・21blockがQQとF_1000003でfull rank。従ってU7非空。可換点のAS性はAOU既知定理を使い、有限rankからAS性を推論していない。U7の外が全部非一致であるとはしない。

**四交比への還元（証明済み）**：構造頂点A0を除いた商Cはw_{0bc}の9係数に依存しない。残る18係数の非零トーラスは矢rescalingで四交比lambda_ij=q_ij q_00/(q_i0 q_0j)、q_bc=w_{2bc}/w_{1bc}の四変数に還元される。C有限次元なら18係数が全て非零でqの全九つの2×2小行列式も非零。minorが零なら2×2支持のJacobi関係を満たす表現に非零3-cycleを作り、Cの無限次元性を示す。有限corner locusは四次元トーラスの非空真開集合である。九divisorが悪いlocusの全体かは未証明。証明は`papers/cubic_heart_corner.tex`、有理数検算は`computations/verify_cubic_corner_torus.py`。AS locusとの交叉と導来同値の問題は別途確認する。

### HRSと一般heart判定

既存`papers/nc_del_pezzo_hearts.tex`の振幅1比較は(T,U)=(ker R1δ_*,ker δ_*)、transported heart=<U[1],T>、t-exact iff U=0を与える。対象は導来的には消えずshiftされる。既存の豊富orbitによる一意性は高次Ext tail消滅を明示的に必要とする。

今回、pointedness・反Serre適合性・標的AZ/高次消滅の下で、周期1の非零単純対象Mについてchi(e,M)>0 iff M∈T、chi(e,M)<0 iff M∈Uを証明した。chi=0はこの仮定下で不可能。非単純対象や未構成の共鳴対象へ無条件で適用しない。

AOU§9の左辺はqgr Fであり、Theorem9.4の導来同値をraw blow-up heartのabel同値と読まない。mutation後E0とπFは実際の対象として照合する。今回のcorner同値はAS側Oから作った反標準環との比較であり、特定のVdB比較との一致は残る。

### 保持する共通公理と次数3の成果

weakly markedは非零Ext有限noetherian Abel圏、Serre、tau=S^-1[2]のheart保存、Gabriel–Krull rank-one torsion-free exceptional O、AZ ampleness、次数dのHilbert数値。hdim=2はSerreから従い独立公理でない。exceptionalityなしのpre-weakからExt1(O,O)=0は未証明。提示やAS ambientは認識問題である。

`papers/weak_cubic_axioms.tex`は正則正規一次境界R/(t)=S0/(g)から一次生成・二次包絡AS4・正規超曲面を認識する。Cassidy–Sheltonの低次数判定とnormal直線を保つtwistを使う。全weak対象の境界存在は未証明。量子Fermatは全対象のR(1,3)帰属を排除し、Pym L(1,1,1,1)とL(1,1,2)の交点に属する。他の成分交差は未決定。対角中心Fermat三次を持つtorus点は27点。固定ambientの中心開部分の商BH54は全変形rigidityではない。PBW12係数・三条件、Artin平坦変形の提示保持・有限型形式模型を保持する。

`papers/cubic_surface_ambient_moduli.tex`と`research/r13_generic_moduli.md`はR13、Poisson延長、8→7、AOU形式比較、四頂点potential、中心incidence、Hessian商・臨界点等を保持する。全weak stackの代数性・marking存在一意性降下・全成分分類は未完成。既存の72root・Euler/Serre行列検算は保持するが今回再実行したとはしない。

### 保持する並行成果：量子FermatのOU障害

`papers/quantum_fermat_not_as_surface.tex` は量子Fermat cubicの圏を離散torsion付きFermat商stackと同定し、HH_{-1}=HH_1=2、HH_0=5を計算して、完全強例外列を持つOU AS surfaceではないと結論する現行原稿である。従ってintrinsic weak cubic全体をOU/AOUのWeyl商と同定しない。この曲面圏そのものの障害はambientのPym成分帰属と独立である。コード `computations/verify_quantum_fermat_ou_sectors.py` と証明書を含む並行更新を保持したが、今回その証明・計算を独立に再監査したとは報告しない。今回のcorner定理もOU/AS領域に限定し、量子Fermatを適用範囲へ入れない。

### 保持する次数1と三次三様体

`papers/nc_del_pezzo_degree1_moduli.tex`はrank、条件付きweighted sextic、10次元dg族、KS、補助A∞表示成分、avatar復元を保持する。`papers/dp1_anticanonical_models.tex`の楕円領域比較は今回再監査せず、本結果の入力としない。特異/非局所自由境界と全intrinsic abelian成分性は未完成。

`papers/nc_cubic_threefold_moduli.tex`と全section・計算を独立維持する。37次元形式ambient、41次元中心対、商13/17、fiber4と全大域stackでの代数性/成分性は区別する。今回再証明・再検算したとは報告しない。

## IV. 優先順位と具体的な着手

1. **Cubicの構造対象と同値の照合**：AOUの実際のmutationでE0≃πFを検証し、AS corner同値と既知のqgr F比較を接続する。数値K0や境界restrictionだけで同定しない。
2. **四交比トーラスの境界**：九つの小行列式が非零な四次元領域でCの有限次元性を決定し、U7外をU_N(N>7)と真の無限次元Cへ分類する。AS locusとの交叉と全モジュライの閉性を混同しない。
3. **VdB最後の段階**：同じ楕円・六点データでker δ_6*とR1δ_6*を実在root対象で計算する。pointednessと周期作用を確認後、単純対象のEuler符号判定を適用する。Rains raw反復と各段階section模型への置換も区別する。
4. **境界・一般次数**：有限位数、nodal/cuspidal境界、weak avatar、dP1への拡張ではgrading・noetherian性・realizationを再確認する。正規境界の一般存在、相対PBW、marking降下、Fermat分枝の研究は維持する。

## V. 再現と検証状態

    python3 computations/verify_cubic_corner_torus.py
    python3 computations/verify_cubic_corner.py
    latexmk papers/cubic_heart_corner.tex

Python標準ライブラリで全有理数計算と有限体計算を再現する。証明書summaryは`computations/cubic_corner_certificate.json`、検証状態は`research/cubic_corner_validation.json`。原稿5ページをLuaLaTeXで組版し参照を確認する。一般cornerの証明、計算機による厳密rank証明、既知AS入力を分ける。独立査読・形式化・網羅的新規性調査は未実施。従来の研究の再現はその現行ノートを参照する。
