# 研究方針：非可換del Pezzo曲面のheart比較と内在的モジュライ

2026-11-15 / project-v16 / recognition-v6 / hearts-v1。再開時は本書、`research/heart_comparison.md`、`papers/nc_del_pezzo_hearts.tex`を読む。共通公理は`research/common_del_pezzo_framework.md`。次数3、次数1、三次三様体の専門原稿は各ノートから参照する。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化し、目標と論文構成を柔軟に改訂する。方針は現在有効な形に書き直し、変更履歴を蓄積しない。証明済み、追加仮定、既知入力、未完成、予想、有限検算を区別する。証明の記載、今回の点検、外部独立査読、新規性確認を混同しない。誤りの影響を依存する本文・要約・方針へ反映する。

一次資料の仮定と適用範囲を確認する。公表用原稿は日本語LuaLaTeXとし、有効な主張と完全な証明を保持する。研究ノートは現在有効な補足・障害・反例・再取得困難な情報を整理し、論文の証明を重複させない。軽量化は履歴・重複・不要物の除去で行い、数学的内容や検証可能性を削らない。

研究継続用bundleは現行方針・ノート・論文ソース/PDF・必要コード・小証明書・再現手順から自己完結的に再開できるものとする。旧会話・旧ZIPを前提にせず、旧版・中間生成物・キャッシュを収録しない。ユーザーは研究区切りで再承諾なくLibraryへ保存することを許可している。現行ソースはGitHub mainにも通常fast-forwardで保存し、遠隔HEADを確認する。既存Library資料は無断削除しない。GitHub Actions・force push・不要なPRを使わず、GitでPDF/ZIP/TeX中間物を追跡しない。生成、証明点検、計算、組版、Library保存、GitHub保存を別々に報告する。

## 量子FermatはOU AS surfaceではない（証明済み）

`papers/quantum_fermat_not_as_surface.tex` で金沢型量子Fermat cubicの曲面導来圏を非退化な離散torsion付きFermat商stackと同定し、HH_{-1}=HH_1=2, HH_0=5を証明。OUのAS surfaceならvery strong helix由来の有限完全強例外列を持つため奇数次HHは消滅する。従って量子Fermatはintrinsic weak cubicだがOUのAS surfaceではない。以前のPym L1111/L112帰属、R13閉包外というambient成分の記述とは独立な、**曲面圏そのもの**の障害である。全weakをOU/AOUのWeyl商と同定する全域仮説は成り立たない。OUのある部分族がweakのどの開集合に埋め込まれるかは引き続き研究する。

## II. 上位目標と最初の対象

一般の非可換del Pezzo surfaceに対し、Rainsの幾何学的heart、Van den Berghのblow-up heart、大川–植田のAS helix heart、反標準環のqgrを比較する。これはdP1だけの補助問題ではなく、内在的モジュライの重要な中心課題とする。最初の実行対象はcubic surface（次数3）。

四構成の存在、同じ入力への対応、Db(heart)→Tのrealization同値、指定同値のt-exactness、構造対象と反Serre作用、境界restriction、rank、marking、族での降下を分離する。四ラベルが四つの異なるheartを与えるとも、全て同じとも仮定しない。数値的共鳴をAZ amplenessの失敗や導来特異化へ直結させない。

この優先順位は、ambient認識や成分性の前に、どのabel圏・どの構造対象を分類しているかを確定するためである。既存のcubic/dP1の認識・候補族・成分計算は保持するが、heartの比較を飛ばして全intrinsic moduliの分類へ昇格させない。

## 共通公理と既存の成分判定

次数1・3のweakly markedは、非零のExt有限・noetherianなAbel圏A、Db(A)のSerre関手S、tau=S^{-1}[2]のheart保存、Gabriel–Krull rank-one torsion-free exceptional対象O、AZ amplenessと次数dのHilbert数値を用いる。hdim A=2は独立公理ではなくSerre双対から従う。exceptionalityを要求しない広い旧条件はpre-weakと呼び、そこからExt¹(O,O)=0が従うかは未解決。低次数提示やAS ambientは定義ではなく認識問題である。

量子Fermat ambientはPym L(1,1,1,1)の(a,b,c)=(ζ,ζ,1)で、L(1,1,2)のQ→u²Q平坦族の特殊点でもある。従って少なくとも二成分の交点に属する一方R(1,3)閉包外。全係数非零の対角中心Fermat三次を持つtorus点はT[3]の27点。他成分との交差は未決定。これらの既存の証明・検算は保持し、今回新たに検証したとは報告しない。

## III. 現在の到達点

### Heart比較：今回の開始結果

証明本文は`papers/nc_del_pezzo_hearts.tex`、補足と文献位置は`research/heart_comparison.md`。

- **既知比較の範囲**：VdB Theorem 11.1.3は一般位置の下でraw blow-upから次のsectionモデルへの導来同値を与える。AOU §9の左辺は最初からqgr Fであり、Theorem 9.4はAS qgrとの導来同値である。両者を無条件に同じheartとはしない。AOUのmutation後の先頭E0とπFの同定は実際の対象として追う。
- **振幅1からHRS tilt**：T_j=ker R¹δ_j*、U_j=ker δ_j*はtorsion pairで、Lδ_j*(coh X_(j+1))=〈U_j[1],T_j〉。heart一致はU_j=0と同値。非零M∈U_jは導来的には消えず、R¹δ_j*Mのshiftとなる。これは標準理論の適用で、原稿に証明を記載し点検した。
- **二つの判定方法**：固定した(e,τ)のAZ amplenessと高次Ext tail消滅の下でheartは一意。必要な有限性を明記したidempotent cornerでは、自然なqgr B→qgr eBeの同値性はB/BeBの有限次元性に等しい。全helixの豊富性を一対象の反Serre orbitの豊富性と混同しない。
- **非一致の検出**：反標準ample heart内の非零τ固定対象はχ(e,M)>0。実在対象で反例を示せればheart非一致を検出する。共鳴式だけで対象を作ったとはしない。
- **初期厳密検算**：AOUの九線束のEuler行列、総和45、反Serre作用と反標準twist、E6の72根、H²=3を有理数計算で確認。heartのt-exactnessや非可換effectivityの証明ではない。

### 保持する次数3の結果

`papers/weak_cubic_axioms.tex`は、正則正規一次境界R/(t)=S0/(g)から一次生成・二次包絡AS4・正規超曲面表示を導く。d=3では六二次関係と一三次関係が結論。Cassidy–Sheltonの低次数判定、正規直線の不変性を使うtwistを区別する。全weak対象の境界存在は未証明。

量子Fermat例は全weak対象をR(1,3)へ押し込める主張を排除する。固定ambientの良い中心三次切断U_F={At³+f(x,y)+Cz³:AC disc(f)≠0}のrigidified商はBH54で、全変形のrigidityではない。PBWの12係数と三条件、Artin平坦変形での低次数関係保持、有限型形式模型も保持する。

`papers/cubic_surface_ambient_moduli.tex`はR13分枝、surfaceのPoisson一意延長、8→7、AOU形式比較、四頂点potentialと中心incidenceを保持する。`research/r13_generic_moduli.md`は一般R13の商・臨界点等の現行知識を保持する。全weak moduliの代数性、大域marking存在/一意性/降下、全対象の成分分類は未完成。

### 保持する次数1と三次三様体

`papers/nc_del_pezzo_degree1_moduli.tex`はGabriel–Krull rank、条件付きweighted sextic認識、普遍点からの10次元dg候補族、KS、補助A∞表示空間の成分性、avatar復元を保持する。`papers/dp1_anticanonical_models.tex`の滑らかな楕円領域の比較証明は保持するが、今回独立に再監査した結果でも、本heart研究の入力でもない。特異/非局所自由境界と全intrinsic abelian成分性は未完成。

`papers/nc_cubic_threefold_moduli.tex`とそのsection・計算資産は独立した現行研究として保持する。37次元形式ambient成分、41次元中心対、商13/17、fiber4、全大域stackでの代数性/成分性の区別を維持する。今回これらを再証明・再検算したとは報告しない。

## IV. 次の課題と具体的着手

1. **cubicの最後のVdB段階**：j=6のker δ_6*を実在するcoherent対象で記述し、R¹δ_6*を計算する。非自明なtiltか否かを決める。まず既知導来同値の一般位置条件内で行う。
2. **AS–反標準heart**：AOUの実際の九対象を追いE0≃πFを照合。反Serre orbitの生成性/高次消滅、またはfolding・cornerの有限性とB/BeBを調べ、t-exactnessを判定する。有限次数検算だけで全次数性を主張しない。
3. **Rainsとraw blow-up**：同じ六点・楕円データで各段階のrestriction/構造対象を追う。sectionモデルの入替えを挟む構成とraw反復を区別する。これを共鳴root対象の挙動へ接続する。
4. **境界と一般次数**：cubicの有限位数・特異境界を扱い、その後dP1等へ展開する。既存の正規境界の存在問題、相対PBW、marking降下、Fermat別分枝も並行するが、heart比較の主線を優先する。

## V. 再現と達成基準

    python3 computations/verify_cubic_heart_numerics.py
    latexmk papers/nc_del_pezzo_hearts.tex

新しい検証状態は`research/heart_comparison_validation.json`。既存のcubic認識には`computations/verify_boundary_fermat.py`、`computations/verify_quantum_fermat.py`、`computations/verify_fermat_pym_components.py`、`papers/weak_cubic_axioms.tex`、dP1には`research/dp1_reproduction.md`を使う。初期研究の達成は、文献の正確な比較図、証明付きのheart判定、再現可能な数値基準を揃えること。四heartの全域一致や全moduliの完成を現在の成果として扱わない。
