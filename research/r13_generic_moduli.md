# R(1,3) の一般モジュライ：アフィン三次函数、Hessian群、八点配置

2026-11-15 / r13-v1。研究再開時には \`00_research_plan.md\` を先に読む。詳細なLuaLaTeX原稿は同日作成した \`r13_component_moduli_20261115_v1.tex\`（現行bundleに収録）。本ノートは現行の新しい定理・証明の骨格・未解決箇所を自己完結して説明する。従来の四頂点potential・directed syzygyの定理は \`papers/sections/projective_three_space_potentials.tex\`、有限行列証明は \`computations/verify_p3_potentials.py\` を参照。

## 対象と既知の入力

標準14641型quadratic Koszul AS正則Z代数のpointed/頂点スカラーを除いたモジュライ。四頂点16矢の符号付きquartic superpotential（長さ2の経路微分）と、directed四頂点12矢の二つのrank6関係空間による同値は別節で証明済み。Pym, *Quantum deformations of projective three-space* (Adv. Math. 281 (2015), §3.4, arXiv:1403.6444) の R(1,3) は中心一次拡大、Le Bruyn–Smith–Van den Bergh, *Central extensions of three-dimensional Artin–Schelter regular algebras* (Math. Z. 222 (1996), Introduction/Thm3.2.6/Prop4.3.9) が一般中心拡大の7次元族・楕円曲線+8点を与える。以下はこの既存の7次元という数だけから商同値を推論するのではなく、余分なZhang同型を排除する証明を追加したもの。新規性の最終確認・外部査読は未完了。

## 定理 A：19係数から7次元の正確な幾何的商

三変数 \(x,y,z\) に対し \(f=f_3+f_2+f_1\) を次数3,2,1の斉次部分とする。定数は不要。係数空間は \(\mathcal F=\operatorname{Sym}^3(k^3)\oplus\operatorname{Sym}^2(k^3)\oplus k^3\simeq\mathbb A^{19}\)。中心一次元tを導入し \(F=f_3+t f_2+t^2 f_1\)。代数 \(B_f\) は
\[
[t,x]=[t,y]=[t,z]=0,\qquad
[y,z]=\operatorname{sym}\partial_xF,\quad
[z,x]=\operatorname{sym}\partial_yF,\quad
[x,y]=\operatorname{sym}\partial_zF.
\]
ここでsymは二次の平均対称化。f3が滑らかで \(B_f/(t)\) が楕円型3D Sklyanin (point scheme \(E\), shift \(\sigma_p\) はtranslation \(3p\ne0\))、B_fが標準AS4である開集合 \(\mathcal F^\circ\) に制限する。この開はPymおよびLBSの一般型から非空。

アフィン群 \(G=\mathrm{Aff}_3=\mathrm{GL}_3\ltimes k^3\) は
\[
(A,b): f(X)\mapsto [f(AX+b)-f(b)]/\det A
\]
で作用（右作用の規約）。証明：四変数の線型座標変換 \(X\mapsto AX+b t,\ t\mapsto c t\) の二次交換子変換に交代テンソルの恒等式
\(\sum_{l,m}A_{il}A_{jm}\epsilon_{lmn}=(\det A)\sum_k\epsilon_{ijk}(A^{-1})_{nk}\)
を使う。 \(F'\equiv(\det A)^{-1}F(AX+b t,c t)\pmod{k t^3}\)。四変数全体のスカラーを除けばc=1とできる。よって中心直線を保存するgraded同型はこの12次元群の作用と正確に一致する。

### 補題：楕円Sklyaninには一次正規直線族がない

\(S=B_f/(t)\) の点schemeを滑らかな平面三次曲線 \(E\)、shiftをtranslation \(\sigma_p\)、 \(\mathcal L=\mathcal O_E(1)\) (deg3)、 \(3p\ne0\) とする。もし非零直線 \(L_i=k\ell_i\subset S_1\) が \(L_i S_1=S_1L_{i+1}\) を満たせば、point module graph \((q,\sigma_pq)\) 上で二つの3次元切断空間のbase divisorはそれぞれ \(\mathrm{div}(\ell_i)\) と \(\sigma_p^{-1}\mathrm{div}(\ell_{i+1})\)。部分空間の一致は零schemeの一致を与え、\(\mathcal L\simeq\sigma_p^*\mathcal L\) を強制する。しかしdegree3線束のtranslationによるPicard変化は3pなので矛盾。よって存在しない。

### 定理：一般中心拡大では余分なZhang同一視はない

添字保存Z-algebra同型 \(\check B_f\simeq\check B_{f'}\) を各次数一次の \(g_i\) で書く。 \(t_i\) の像 \(\ell_i=g_i(t)\) は正規直線族をなす。ターゲット中心元t'による商Sklyaninへ射影すると、上の補題と整域性から全像が零となり、 \(\ell_i=c_i t'\)。さらに元の中心性 \(t_i v_{i+1}=v_i t_{i+1}\) を輸送すると \(c_i t'g_{i+1}(v)=c_{i+1}g_i(v)t'\)。t'を消去し \(g_{i+1}=(c_{i+1}/c_i)g_i\)。従ってg_iは一つの線型同型のスカラー倍であり、頂点スカラーを除けばgraded同型。小Artin拡大でも、t'からの一次変位α_iが満たす \(\alpha_i v=v\alpha_{i+1}\) を楕円点graphに評価し、 \(\sigma_p(q)\ne q\) の稠密開からα_i=0を得る。したがって形式自己同型群oidにも余分なZhang変形がない。

従来の四頂点全rank6 scheme \(Z_6\) の \(R(1,3)\) 成分のgeneric tangentは射影67次元、群軌道60次元（既存rank188証明書）。19係数からの七係数sliceが商接空間を張る。ゆえに一般のsmooth DM開上、上記Zhang剛性とétale性により、ある非空開部分で
\[
\boxed{\mathfrak M^\circ_{R(1,3)}\simeq[\mathcal F^\circ/\mathrm{Aff}_3]},\qquad \dim=19-12=7 .
\]
ここで \(\mathcal F^\circ\) は必要に応じた非空不変開への縮小。全成分・全境界の同型ではない。

## 定理 B：七係数と位数216の有限群

三次最高項をHesseにして \(f_3=a(x^3+y^3+z^3)+bxyz\)。一般f2を \(\sum q_{ii}x_i^2+q_{yz}yz+q_{xz}xz+q_{xy}xy\) とする。translation \(x_i\mapsto x_i+\beta_i\) は二次オフ対角係数をそれぞれ
\(q_{yz}\mapsto q_{yz}+b\beta_x,\ q_{xz}\mapsto q_{xz}+b\beta_y,\ q_{xy}\mapsto q_{xy}+b\beta_z\)
へ送る。b≠0なら唯一のtranslationで対角化できる。中心スケール \(X\mapsto\lambda X\) はf3不変、f2をλ^-1倍、f1をλ^-2倍にする。qxx≠0ならqxx=1に規格化。七係数
\[
f_7=a(x^3+y^3+z^3)+bxyz+x^2+c y^2+d z^2+e x+f y+g z.
\]
Hesse pencilのflex 9点を保つprojective群は \(G_{216}=(\mathbb Z/3)^2\rtimes SL_2(\mathbb F_3)\)（Artebani–Dolgachev, *The Hesse pencil of plane cubic curves*, §4, Proposition4.1）。一般Hesse cubicを別のHesse cubicに移す全射影変換はこの群。各h∈G216を3×3行列A_hで代表し、det^-1 f(A_hX)に先の唯一translation/scaleを適用することで7係数上の具体的な**有理作用**を得る。必要なら全216元が定義される開部分へ縮める。代表A_hのスカラー選択は規格化後消える。従って一般の商は
\[
\boxed{[\mathcal F^\circ/\mathrm{Aff}_3]\stackrel{\mathrm{bir}}{\simeq}[\mathcal S_7/G_{216}]},
\]
七係数写像の一般次数216。計算ではQ(ω)上の3×3行列をprojectiveに216個全列挙し、数値(a,b)=(3,5)のHesse係数軌道24点・安定化群9を確認。有限群の不変関数体の最小生成元・関係式は未計算。

## 定理 C：特殊な8点配置による代数幾何学的同定

一般のfについて \(Z_f=V(f_x,f_y,f_z)\subset\mathbb A^3\)。f3が滑らかなので三つの最高次数二次式には無限遠で共通零点がなく、Z_fは長さ8の(2,2,2) complete intersection、一般には8個の異なる点。これらはB_fのt≠0のpoint modules（t中心なので点のshiftは定常、t=1で交換子を零にすることは∂f=0）。

Hilb^8(A3)の「8個の異なる点が三つの二次式でscheme論的に切り出される」局所閉locusを取り、 \(J_Z=I(Z)\cap k[x,y,z]_{\le2}\) が3次元であるものに制限。閉1形式を作る三つ組の線形空間
\[
\mathcal I_Z=\{(q_1,q_2,q_3)\in J_Z^3:\partial_iq_j=\partial_jq_i\}
\]
が1次元で、その非零元がJ_Zの基底になる開部分を \(\mathcal H_8\) とする。積分（char0）によって非零 \(\omega=\sum q_idx_i\in\mathcal I_Z\) は定数を除いたfを一意に定め、逆にZ_fから勾配の1形式dfが得られる。ゆえに一般のfの係数空間は \(\mathcal I^\times\to\mathcal H_8\)（直線束の零切断を除いたもの）と同型。Aff3作用には \(\omega\mapsto(\det A)^{-1}(AX+b)^*\omega\) の密度捩れを入れる。従って
\[
\boxed{\mathfrak M^\circ_{R(1,3)}\simeq[\mathcal I^\times/\mathrm{Aff}_3]}
\]
（対応する同じ非空開に制限）。これは「楕円曲線＋8点」よりも復元操作を明示した正確な代数幾何学的モジュライであり、point schemeは楕円Eと8点Z_fを持つ。ただし(E,σ,Z_f)のみからの無条件な一意復元は主張しない。

非空性のQQ証明書：f=3(x³+y³+z³)+5xyz+x²+2y²+3z²+x+2y+4z。Groebner消去の一変数多項式は8次squarefree。Sklyanin商の一次central pair条件18×6行列rank6。勾配二次式の別frameのintegrabilityは12×9行列rank8で核がスカラー恒等行列。translate offdiag=b I3、Aff determinant twistの合成は整数有理記号式でPASS。再現コードは継続bundle内の \`verify_r13_generic_geometry.py\` と \`verify_hesse216.py\`。前回のrank188はこの作業では再実行していない。

## 全既約成分の境界で未解決の問題

\(R(1,3)\) 成分の被約な台は四頂点rank6 potential schemeの中の67次元orbit closureとして与えられるが、一般開の商だけから全境界のscheme、非被約構造、正規化、GIT半安定点、別成分との交点、f3 singular / 3torsionでの追加Zhang同一視は決定できない。「full global irreducible component classified」は未証明。新規性・先行研究の最終確定、外部査読、Lean形式化も未実施。
