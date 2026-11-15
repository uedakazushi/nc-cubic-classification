# Rains resonance と anticanonical heart：現行研究ノート

2026-11-15 / resonance-hearts-v2。再開時は `00_research_plan.md` → `papers/nc_del_pezzo_resonance_hearts.tex` → 本ノートを読む。四名称は Rains heart / VdB heart / AS heart / anticanonical heart。証明本文は現行原稿へ集約し、旧ノート・旧TeXを必要としない。

## 中心定理：符号別の完全な Ext 判定

Rains型 smooth elliptic noncommutative del Pezzo X に、境界 E、構造line bundle e、theta=S[-2]、tau=theta^{-1}、theta→id と中心正則g∈R1 がある。根 alpha²=-2、alpha·K=0、c1(M)=alpha の**既約純一次元sheaf Mが実在して境界制限 Li^*M=0**となるとき、m=chi(e,M) で

| m | dim Hom(e,tau^n M) | dim Ext¹(e,tau^n M) | Ext² | natural derived section |
|---|---:|---:|---:|---|
| m>0 | m | 0 | 0 | g-invertible finite module of dimension m in degree 0 |
| m=0 | 0 | 0 | 0 | M ≠0 but Phi(M)=0 |
| m<0 | 0 | -m | 0 | g-invertible finite module of dimension -m shifted by [-1] |

全整数nで成立。各 M は2-spherical（End=k、Ext¹(M,M)=0、Ext²(M,M)=k）。これは単なる数値的共鳴式だけの結論ではなく、**当該既約根sheafの存在、境界非交叉、Rains側のdual theoryが適用される範囲**を仮定する。

- **m≤0 の証明の訂正**：旧稿の「既約Mへのe→M非零射は全射」は誤り。正しくはimage Iのc1(I)=alpha、cokernel T=M/Iは零次元。Rains Cor10.16からchi(e,I)≥-alpha(alpha+K)/2=1、Prop7.6からchi(e,T)≥0。よってchi(e,M)≥1となりm≤0ではHom=0。Rains Cor7.23でExt²=0、EulerからExt¹=-m。
- **m>0 の新結果**：Rains R ad は双対曲面 X^adへの反変導来同値。N=R¹ad Mは双対側の既約純一次元境界非交叉根sheaf（Cor7.26,7.30,7.31）、χ(e^ad,N)=-m（Prop7.16）。負指数補題をNに適用して Hom(e^ad,N)=0、Ext¹(e^ad,N)=m。R ad と Serre dualを合成し Hom_X(e,M)=Ext¹_ad(e^ad,N)^*、Ext¹_X(e,M)=Hom_ad(e^ad,N)^*。従ってHom=m、Ext¹=0。**正指数共鳴のExt¹消滅問題は、既約根sheafに限って解決**。
- **m=0 の新帰結**：zero-index根sheaf Mが存在すればHom=Ext¹=Ext²=0で、全orbitに導来的に右直交。自然PhiはMを消す（保守的でない）。Genuine smooth classical del Pezzo avatar SではO_E(alpha)非自明なのでm=0根共鳴は存在しない。Weak del Pezzoの(-2)曲線収縮と対応するメカニズム。

## Anticanonical heartと代数の意味

R=⊕_{n≥0}Hom(e,tau^n e)、R/(g)=B(E,L,σ), deg L=d。Rainsの条件下で dim R_n=1+d n(n+1)/2 は共鳴全点で一定。m≠0では (P^j(M)=piigoplus_{nge0}Ext^j(e,	au^nM)) の唯一非零のjが0（m>0）または1（m<0）。gはM上で同型なので各次数を周期1で結び、局所化次数0 (V=(igoplusExt^j)[g^{-1}]_0) はA=R/(g-1)の|m|次元右加群。**非零表現が現れたことと R の Hilbert 数値の跳び・qgrの特異化・導来非同値を混同しない。**

m<0ではRains heartの(e,tau)はAZ ampleでない（全Hom零）。qgrRの標準対がAZ-ampleのとき、eとtauを保つ Rains–anticanonical abel同値は存在しない。自然導来切断Phi(M)=πP¹(M)[-1]でt-exactでない。m>0の**その根sheaf**についてPhi(M)=πP⁰(M)はheartにあり、他の根や一般対象でのt-exactnessは未判定。m=0で存在すればPhi非保守的。全qでの導来同値は本結果の入力ではない。

## 正・負それぞれのZariski dense resonance

smooth plane cubic E⊂P²上で非torsion q∈Pic⁰(E)と5点p1,p2,p4,p5,p6を固定。n≥1、ε=±1 に対し O_E(p3^ε(n))=O_E(1)(-p1-p2)⊗q^{-εn}。各符号について点は相異なり（一般位置を破るのは有限個）、六点blow-upはgenuine cubic。simple root alpha=h-e1-e2-e3のrestrictionはq^{εn}なので共鳴m=-εn。**負指数も正指数も別々に稠密**。基底の一般パラメータを動かすと各ファイバーで稠密、ゆえに関連するgluingチャート全体でも稠密。r=3..8 blowups（d=6..1）でも同様。全nc del Pezzoモジュライの任意成分への稠密性は主張しない。

## 根 sheaf が2-spherical

Rains既約性＋純一次元性より非零自己射は核を持たない。余核は数値類零の零次元sheafとなりRains Prop7.6で零。End(M)=k。Serre theta M=MからExt²(M,M)=k、Euler χ(M,M)=-alpha²=2からExt¹(M,M)=0。双対・[−1]・境界非交叉の論理的役割を区別する。

## 次の課題と検証

1. 同じ共鳴条件で**既約でない対象**の層とanticanonical側の有限次元A表現の全分類。根sheafの符号判定だけではheart全体のt-structureは決まらない。
2. 既存dP1原稿`papers/dp1_anticanonical_models.tex`の全q導来同値の証明を、完全忠実性・本質的全射性・核の消滅・smoothnessの順に**独立監査**する。原稿に証明記載はあるが今回独立に検証していない。正しければm<0の稠密共鳴は導来同値を保つheart変化。
3. VdB heart/AS heartの対象と自然導来比較、非自明HRS tiltのtorsion pairとsemistable finite-dimensional A moduleをつなぐ。Zariski dense非t-exact locusに非空Zariski開t-exact領域はない（現在のRains chartの範囲）。
4. 特異/非局所自由境界とweak avatarではm0の導来的消失に注意。局所qgr singularityか否かは別途調べる。

一次資料：Rains *Birational geometry* arXiv:1907.11301v1 §5 Cor5.9 Eq(5.24)、§7 Prop7.6, Cor7.23, Cor7.26,7.30,7.31, Prop7.16、§10 Cor10.16、§11 pp138–141（既約simple root sheafの存在）。Rains *Filtered deformations* arXiv:2107.13540v2 §§4–5（稠密有効根、natural boundary triangle、中心g）。引用と証明の全文は論文。PDFページ画像のWeb取得はcache missで、抽出原文との照合にとどまる。独立査読/新規性網羅調査は未実施。計算コード`computations/verify_resonance_hearts.py`、現在の原稿`papers/nc_del_pezzo_resonance_hearts.tex`をLuaLaTeXで再生成。GitHub mainを正本とし、push成功ならLibraryへの保存なし。
