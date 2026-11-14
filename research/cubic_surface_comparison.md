# 現行研究ノート：R13・内在的三次曲面・Weyl商

2026-11-15 / surface-v2。最初に `00_research_plan.md` を読む。証明本文は `papers/cubic_surface_ambient_moduli.tex` とその唯一のinput。以下は作業日誌ではない。

## 表示と同値関係

四窓のR_i∈Gr(6,V_i⊗V_(i+1))をGL4^4で割るのは、AS Z代数に任意の4周期τを指定した問題。非捩れpotentialはFrobenius適合周期の部分。可換Cの周期にdiag(2,1,1,1)を合成するとR0=R1=R2=Λ²V、R3=(1⊗σ^-1)Λ²V。最高syzygyがΛ⁴VなのにR3が交代でないため非捩れpotentialは存在しない。twisted potentialを使うときはNakayamaとtraceの同値関係も必要。

GL4^4の各矢空間スカラーは射影potentialに自明に作用する。67次元parameter componentのraw stack次元は3、四つのGmをrigidifyした商は7。pointed圏、裸のAbel圏、graded代数、周期構造付きZ代数を区別する。

## 三次元quadratic AS正則とdirected/rolled-up箙の比較（既知結果）

この話題は本稿の四頂点・四次superpotentialの場合と同一視しない。非可換 P^2 のdirected Beilinson箙には三頂点・六矢があり、関係は rank 3 の R⊂V0⊗V1 (dim V0=dim V1=3)。三本の矢 V2:2→0 を加えたrolled-up箙の**三次の通常の巡回potential**は w∈V0⊗V1⊗V2。flattening w:V2*→V0⊗V1 が単射である開集合 U 上で、w↦im(w)=R は GL(V2) の主束である。よって族・自己同型込みで
[U/(GL(V0)×GL(V1)×GL(V2))] ≃ [Gr(3,V0⊗V1)/(GL(V0)×GL(V1))]
が成り立つ。逆は V2=R* として恒等テンソル w=Σ r_i⊗c_i。rolled-up potential W=Σ r_i c_i の ∂_(c_i)W=r_i、他の微分はRから一意に定まる。これはAOU *Compact moduli of noncommutative projective planes*, arXiv:1411.7770, (7.27)–(7.28) で**既に証明されている**。同Theorem 1.1(2) は半安定GIT商 M_quad≅M_rel≅P(6,9,12) も述べる。full-rankでないpotentialも含むraw affine quotient stack全体は同値でなく、上記は開埋込みである。projectivized potentialにGL(V2)で作用させる場合は残存G_m慣性を処理する。

以前の「任意の3周期同型を固定した三頂点relationの表示はordinary potentialにならない」という反例は、**指定した周期との両立**を問題にしたものであり、directed箙のRだけを保持し新矢をR*として追加するこの同値の反例ではない。3次元AS正則幾何対象に制限するにはBP/VdBのgeometric quadruple条件（任意の非零縮約がrank≥2など）を対応する双方へ課す。単なるfull flattening rank 3からAS正則性を導かない。一般の長さ6,9等のpotentialまで自由に許すと、ここでの同値から外れる。

## 明示族と計算

F=a(x³+y³+z³)+bxyz+t(x²+c2y²+c3z²)+t²(d1x+d2y+d3z)。w=Alt(txyz)-3(1-c+c²-c³)(t sym F)。全二階微分で[t,x]=[t,y]=[t,z]=0、[y,z]=sym F_x等を得る。t³はwに寄与しない。

witness=(3,5,2,3,1,2,4)。二flatteningのrank6条件の微分Tは200×256、rank188。軌道Oは256×64、rank61。7slice+軌道S7は256×71、rank68。TS7=0はQQ上の恒等式。従ってprojective tangent=67、orbit=60、商=7。最大小行列式はJSONに行・列とともに保存。19独立係数で微分関係の恒等式も検算した。

sourceの全次数AS性はMori–Smith、PBW、中心一次拡大とKoszul complexの証明を使う。有限階数だけからAS性を結論していない。接空間同型からH×N→O13は適切に縮小してétale surjective。これが実際の有限型DM開部分。全成分境界のAS性やgeneric stabilizerの位数は未計算。

二因子stabilizerのrank30証明書により一般点でLie=0。四窓のArtin変形のNakayamaの射影像は消え、scalar c_iだけが残る。∏c_i=1なのでtrace rescalingで消せる。従ってこの一般点では任意周期の関係式の形式変形も非捩れpotentialになる。大域反例とは矛盾しない。

## 内在的定義と認識の境界

H=S^-1[2]は両方向でheartを保つことを要求する。smooth proper enhancement、noetherian heart、Hom有限性、族での平坦性・相対Serre・底変更を指定する。Γ_acの積はH^m(g)∘f。AZの有限性・ample性により(A,O,H)を回復する。

Hilbert級数(1-t³)/(1-t)^4だけから次数一生成・二次包絡AS4・正則三次核はまだ導いていない。一般反例を発見したという意味でもない。超曲面認識部分ではI3=1、I4=4から左右の生成像が一致してnormalityを得る。これによりambient射は自然かつ底変更に両立する。

## 形式Weyl商と未解決の大域商

一般可換Xの標準markingはW(E6)-torsor。Ext¹(E,E)=Ext²(E,E)=0とLowenにより九対象は各Artin変形へ一意に持ち上がる。DDLの幾何的helix比較で全関係式変形とAbel変形が一致。Oも唯一、逆Serre=helix九移動、ample列によるheartの検出でt-exactness、Artin帰納で反標準ample性とHilbert値が保たれる。HH²=8、HH¹=HH³=0。よって全usual-markingの形式chartのWeyl商はweak形式変形と一致する。

大域化には、全対象へのmarkingの局所存在、K0数値markingによる例外列の一意性、全同型・降下の比較が必要。形式chartの同型や8次元の一致だけで大域商やdegree=|W(E6)|を結論しない。Oを固定するだけでaffine Weyl由来の全追加同一視が自動的に消えるとはしていない。

## AOUからambientへの有限計算

AOU有限代数はrank45、globaldim≤2の三block quiver。Θ=RHom_(Λe)(Λ,Λe)はinverse Serre bimodule。P0=e_(0,0)ΛとしてK_m=RHom(P0,P0⊗Θ^⊗m[2m])、m=0..4を計算する。可換点近傍ではrank1,4,10,19,31、V=H0K1、R2=ker(V²→H0K2)でGrassmannianへの候補射がある。

AOU§9の(9.44),(9.55)–(9.57)でP0はOへ送られる。Lemma9.2でHは反標準shift。VdBのgeneric blow-up表示から全orbit環がAS4中心一次拡大Pの正規三次商F=P/(G)になる。Sklyanin頂部でGが中心、σ(t)=t、σ(x_i)=x_i+c_i t、Hessian比較でc_i=0なので一般にはGも中心。

可換点でtruncation≤3の微分はinjective。関係module J/(VJ+JV)の次数>3が特殊化で零なのでArtin Nakayamaにより消える。このため低次数の自明化は全環・Abel圏の自明化となる。AOUの8方向と射影基底15方向を加えた像は23次元。一般の固定ambient中心三次はP1なのでambient像≥22、既知R13族dim22より等号。四頂点rigidified商では8→7、一般fiber1、像の閉包codim0。

ここでは8座標→7座標の展開済み有理式を出していない。finite Serre algorithmの実装、generic degree、Weyl同定、境界での正則性は次の課題。全weakly marked stackの有限型性や全認識定理とも区別する。

## 一次資料（必要箇所）

- Bocklandt–Schedler–Wemyss, arXiv:0802.0162v3, §1、Theorems6.2/6.8。signed/twisted potentialとKoszul解消の関係。
- Mori–Smith, arXiv:1502.07403v2, Theorem4.2(1)。smoothなcommutative最高三次ならA_(f,λ)は3CY。
- Pym, arXiv:1403.6444, §2, §3.4。規格化graded CY変形とR13の中心拡大表示。全任意周期stackの分類ではない。
- AOU, arXiv:2404.00175v1, Introduction(2), §5.4, §9, Lemma9.2, Theorem9.4。(9.44)等のOとmarked threadの対応を確認。
- VdB, arXiv:math/9809116, Chapter12、Remark12.0.5。反標準モデルとblow-upそのものを区別。
- Le Bruyn–Smith–Van den Bergh, Math.Z.222(1996),171–212。一般中心一次拡大のAS性と7次元族。
- Etingof–Ginzburg, arXiv:0709.3593v4, Proposition7.3.1(ii)、Theorem3.3.2、§9。PBWと中心元。
- Lowen, arXiv:math/0407019, TheoremA。対象の持上げのExt²障害／Ext¹自由度。
- De Deken–Lowen, JNCG5(2011),477–505, DOI10.4171/JNCG/83, Theorems4.5/5.13/5.15、Definition5.12。公式PDF https://ems.press/content/serial-article-files/30497 。forward Ext消滅、flat性、Z生成helixを確認して使用。
- Okawa–Ueda, arXiv:2508.04986v1, Definition1.1, Theorem6.4。marked AS面と楕円データの双有理比較。weak Weyl quotient定理ではない。
- Okawa–Ueda, OWR44/2024, pp2557–2558, DOI10.4171/OWR/2024/44。affine Weyl、K0一意性、pure helixに関するConjectures1–3。

新規性の網羅的確認・外部査読は未実施。再現手順と今回の検証範囲は隣のreproduce/validationを読む。
