# 研究方針：非可換del Pezzo曲面のheart比較と内在的モジュライ

2026-11-15 / project-v17 / recognition-v6 / hearts-v2。最初に本書、`research/cubic_corner.md`、`papers/cubic_heart_corner.tex`を読む。比較の共通枠組みは`research/heart_comparison.md`と`papers/nc_del_pezzo_hearts.tex`、共通公理は`research/common_del_pezzo_framework.md`。次数別・三次三様体の研究はそれぞれの現行ノートから再開する。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化し、目標と論文構成を柔軟に改訂する。方針は現在有効な形へ書き直し、変更履歴を蓄積しない。証明済み、追加仮定、既知入力、未完成、予想、有限検算を区別する。証明の記載、今回の点検、外部独立査読、新規性確認を混同せず、誤りの影響を依存する本文・要約・方針へ反映する。

一次資料の仮定と適用範囲を確認する。公表用原稿は日本語LuaLaTeXとし、有効な主張と完全な証明を保持する。研究ノートは現在有効な補足・障害・反例・再取得困難な情報を整理し、論文の証明を全文重複させない。軽量化は履歴・重複・不要物の除去で行い、数学的内容や検証可能性を削らない。

研究継続用bundleは現行方針・ノート・論文ソース/PDF・必要コード・小証明書・再現手順から自己完結的に再開できるものとする。旧会話・旧ZIPを前提にせず、旧版・中間生成物・キャッシュを収録しない。ユーザーは研究区切りで再承諾なくLibraryへ保存することを許可している。現行ソースはGitHub mainにも通常fast-forwardで保存し遠隔HEADを確認する。既存Library資料は無断削除しない。GitHub Actions・force push・不要なPRを使わず、GitでPDF/ZIP/TeX中間物を追跡しない。生成、証明点検、計算、組版、Library保存、GitHub保存を別々に報告する。

## II. 上位目標と最初の対象

一般の非可換del Pezzo surfaceに対し、Rains幾何学的heart、VdB raw blow-up heart、大川–植田AS helix heart、反標準環qgrを比較する。これはdP1だけの補助問題ではなく内在的モジュライの中心課題であり、最初の実行対象はcubic surface（次数3）。四構成の存在、同じ入力、realization、指定同値のt-exactness、構造対象と反Serre作用、境界restriction、rank、marking、族への降下を分離する。四ラベルが四つの相異なるheartを与えるとも、全て同じとも仮定しない。

最初のAS–反標準比較は、標識と構造頂点を固定したnoetherian AS chartの非空開部分でabel同値まで進んだ。全域比較、VdB/Rains側とのpointedness、共鳴ごとの非自明tiltは未解決。どのabel圏・構造対象を分類するかを確定してから全intrinsic moduliへ進む。数値的共鳴の稠密性をAZ失敗・導来特異化へ直結しない。

## III. 現在の到達点

### Cubicの明示的corner開集合

`papers/cubic_heart_corner.tex`が完全な証明と計算の意味を記す。B=Jac(Q,W)、e=e_(A0)、C=B/BeB。Cは道長1で生成されるのでC_N=0から全高次数消滅が従う。最大minorによるU_Nは開、U=union U_NはC有限次元locus。C有限から両corner bimoduleの有限生成性を導き、B右noetherianの下でqgr B_cut→qgr eB_cut eをabel同値とする。標準AS helixのfolding・Serre・飽和の範囲でeB_cut eは指定構造対象の反標準環。道長gradingと反標準cut gradingは必ず区別する。

六点(1:0:0),(0:1:0),(0:0:1),(1:1:1),(1:2:3),(1:4:2)から27係数potentialを切断の積で構成した。全関係を含む厳密計算でCのHilbert関数は[8,21,33,38,33,21,8,0]、総次元162。7次6804列・21blockがQQとF_1000003でfull rank。従ってU7非空。可換点のAS性はAOU既知定理を使い、有限rankからAS性を推論していない。U7の外が全部非一致であるとはしない。

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
2. **Corner開集合の境界**：U7外をU_N(N>7)と真の無限次元Cへ分類する。有限次数の零は道長1生成を根拠に全次数へ進める。標識を忘れた全モジュライの閉性と混同しない。
3. **VdB最後の段階**：同じ楕円・六点データでker δ_6*とR1δ_6*を実在root対象で計算する。pointednessと周期作用を確認後、単純対象のEuler符号判定を適用する。Rains raw反復と各段階section模型への置換も区別する。
4. **境界・一般次数**：有限位数、nodal/cuspidal境界、weak avatar、dP1への拡張ではgrading・noetherian性・realizationを再確認する。正規境界の一般存在、相対PBW、marking降下、Fermat分枝の研究は維持する。

## V. 再現と検証状態

    python3 computations/verify_cubic_corner.py
    latexmk papers/cubic_heart_corner.tex

Python標準ライブラリで全有理数計算と有限体計算を再現する。証明書summaryは`computations/cubic_corner_certificate.json`、検証状態は`research/cubic_corner_validation.json`。原稿5ページをLuaLaTeXで組版し参照を確認する。一般cornerの証明、計算機による厳密rank証明、既知AS入力を分ける。独立査読・形式化・網羅的新規性調査は未実施。従来の研究の再現はその現行ノートを参照する。
