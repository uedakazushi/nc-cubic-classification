# 研究ノート：広いweak公理・包絡認識・比較の限界

2026-11-19 / recognition-v7。

再開時は `00_research_plan.md` を最初に読む。本書は、強い14641型H3の分類と、
それより広いweak公理からの認識問題を区別するための現行ノートである。
本リポジトリで必要な証明は `papers/nc-cubic-classification.tex` とその読込節、
全H3分類の詳細は `research/cubic_14641_classification.md` にある。

## 1. 対象の区別と現在残る問い

| 対象 | 定義または位置付け | 本ノートで保持する区別 |
|---|---|---|
| pre-weak | rank-one torsion-free、反Serre作用、豊富性、Hilbert切断数を要求する広い公理 | 構造対象のExt¹消滅が自動とは証明されていない |
| 統一weakly marked | Gabriel–Krull rank-one torsion-freeかつexceptionalな構造対象を要求する | 一次生成・低次数提示・AS4二次包絡を全対象で自動とはしない |
| 条件2付きweak | section環が一次生成で、関係イデアルが次数2,3で生成される | 二次包絡のAS正則性や最小三次関係一本を含意するとはしない |
| 強いH3 | 一次生成とnoetherian quadratic Koszul AS4型14641二次包絡を課す内在的部分クラス | 現行原稿の全幾何学的分類・四成分の対象 |
| 相対内在的H3族 | 相対Serre・豊富性、導来Homの底上完全性と底変更、包絡の三次平坦性等を明記した族 | 任意の平坦Abel圏変形を無条件にこの族と同定しない |

H3の分類定理を、広いweakクラスの包絡認識の完成と読み替えない。
相対定義からpropernessや三次平坦性を省略できる範囲も別問題である。
滑らかな可換三次点のArtin自動性と、一般の非可換点または任意のAbel圏変形での自動性は区別する。
正確な相対仮定は `def:h3-intrinsic-family`、相対分類は `thm:h3-intrinsic-algebraic-stack` を参照する。

## 2. 共通公理から自動となる事項

Gabriel–Krull商によるrankの定義を使う。有限長対象のSerre部分圏をA₀、
A/A₀で有限長となる対象の逆像をA₁とし、q:A→A/A₁について
qOが非零単純、かつ `Hom(T,O)=0`（T∈A₁）をrank-one torsion-freeの意味とする。
裸のAbel圏に説明なく通常のベクトル束のrankを持ち込まない。
具体的な整域section環では、次数零商斜体によるrankも照合できる。

`s=S^{-1}[2]` がheartを保つと、Serre双対から

\[
\operatorname{Ext}^i(M,N)
\simeq\operatorname{Hom}(sN,M[2-i])^*
\]

を得る。従ってi>2では零で、非零Nについて
`Ext²(sN,N)=End(sN)^*≠0` なので大域次元は正確に2である。
この命題単独ではsのheart上の本質的全射性を要しない。
ただし正負のtwistを共通の偏極として使う場合は、heart上のexact自己同値という定義を用いる。
証明は `prop:serre-heart-global-dimension`。

正次数Hilbert値 `h_d(n)=1+d n(n+1)/2`、rank-one torsion-freeとexactなsから、
負次数の切断消滅、`End(O)=k`、`Ext²(O,O)=0` が従う
（`lem:negative-auto`）。Ext¹(O,O)=0の冗長性はこれでは得られない。
負次数をsection環に加えても環は変わらない。
体上の大域次元2・Serre存在と、任意底上のsmooth proper enhancementを同一条件と扱わない。

## 3. 標準正規境界による包絡認識

`R/(t)=S_0/(g)`、tが正則正規一次、S₀がnoetherian Koszul AS3、
gが正則正規d次（d≥3）のとき、二次包絡B=Q(R)はAS4で、RはBの一本の正則正規d次商となる。
低次数提示条件やAS包絡の存在を先に仮定しない。
証明は `thm:normal-boundary-recognition`。

要点は `B_i=R_i`（i≤2）がtの低次数正則性を与え、
Cassidy–Shelton Theorem 1.5のcomplexity 2の判定で全次数の正則性へ進むことである。
ambientがPBWであることを結論の代わりに仮定しない。

中央化の規約は `ta=σ(a)t`、`R'=R^{σ^{-1}}`、
`a⋆b=aσ^{-deg a}(b)` とする。σ(t)=tなのでtは中心化する。
境界自己同型はS₀へ持ち上がり、gの直線と `I_d=kG` が不変なので、
untwist後も該当する元のnormal/regular性を保持する。
任意のnormal元が任意のtwistでnormalなままとは主張しない。

左右両側で `I∩tB=tI`、`I/tI=(g)` を使って `I=BG=GB` を得る。
Gの正則性はt進最高記号gから従う。S₀が整域ならBは整域だが、
中心元による商Rが整域になるとは一般には言えない。
d=3では条件2、overlap次元4、中間コホモロジー消滅を得る。
この定理は標準正規境界の存在を全weak公理から証明したものではない。

固定 `S_0=T(W)/(U)`、`L=(U⊗W)∩(W⊗U)` で用いるBG条件は
`δα(L)⊂U`、`αδα+δβ=0`、`βδα=0`。
可換S₀についての12独立係数の検算はLie Jacobiと中心2-cocycleに一致する。
一般の非可換境界のPBW性は、文献定理を使う通常証明として区別する。

## 4. 量子Fermat例が区別する三つの概念

### 4.1 H3であることとOUのAS surfaceであること

OUのAS surfaceでないことを示す独立論文の正本は
https://github.com/uedakazushi/nc-cubic-non-as にある。
移管前のローカルパスへ独立論文を再作成しない。
本分類で必要な結論と適用範囲は主原稿の `thm:strict-AS-inclusion` に保持する。

比較の有限データを記す。
可換Fermat環 `S=k[t,x,y,z]/(t³+x³+y³+z³)`、`L=(Z/3)²` に対し、
重み `(t,x,y,z)=((1,0),(0,1),(0,1),(-1,1))`、
cocycle `μ(g,h)=ζ^{g₁h₂}` を使うと量子環は `R=S^μ`。
`T=k_μL≃Mat₃(k)`、`H=L^∨` とすると `(S⊗T)^H=R`、
`T#H≃Mat₉(k)` によりaveraging idempotentはfullとなる。
X=Proj Sと書けば `qgr R≃coh^α[X/H]` となる。
このMorita記述を捩れ付きorbifold HKRと合わせると

\[
\dim HH_{-1}=2,\qquad \dim HH_0=5,\qquad \dim HH_1=2.
\]

Hの作用は `(a,b):(t,x,y,z)↦(ζ^at,ζ^bx,ζ^by,ζ^{-a+b}z)`。
固定楕円はE_tの二要素 `(0,1),(0,2)` とE_zの二要素 `(1,1),(2,2)` で、
それぞれ奇数次Hochschild成分へ寄与し、その他の固定点集合は有限である。
OUのAS surfaceは有限完全強例外列を持ち、HH_{±1}=0なのでこの例はOU型ではない。
固定点型・character・Picard不変部分・次元の有限計算と、Morita同値・HKRによる通常証明を区別する。

### 4.2 整域性と局所大域次元の証明を省略しない

包絡の変数を(t,x,y,z)とすると
`tx=ζxt, ty=ζyt, tz=ζzt, xy=yx, xz=ζzx, yz=ζzy`。
q行積1とq³=1からBはCY4で、`F=t³+x³+y³+z³` は正則中心元である。
三次中心は `t³,z³,x³,x²y,xy²,y³` の六次元、中心一次・二次は零。

t局所化の次数零環ではu₁,u₂が可換、`u_i u₃=ζu₃u_i`、`Σu_i³+1=0`。
`r=u₁/u₂, v=u₂³, w=-1-(r³+1)v` と置くと、中心体k(r,v)上のsymbol algebra
`(v,w)_ζ` はw付値でのvの残余が非cubeなのでdivisionとなる。
この議論がrank-one/torsion-freeの具体的根拠であり、中心元で整域を割るだけでは代替できない。

tailsの大域次元2にはKanazawaの「指数=変数数」の主定理を直接適用せず、
指数3・変数4の局所証明を使う。中心完備化でnormal y_iの三乗がradicalに入ること、
それが生成するイデアルのnilpotence、正規正則元の大域次元降下を用いる。
全座標非零のfiberではtwisted finite-group algebraの半単純性を使い、
chart上の局所perfect性を貼り合わせた後にSerre双対へ進む。

### 4.3 全域R(1,3)帰属と、全ambient変形の問題

量子Fermat包絡はPymのCY skew torus
`q01=a,q02=b,q03=(ab)^(-1),q12=c,q13=a/c,q23=bc`
における `(a,b,c)=(ζ,ζ,1)` で、L(1,1,1,1)型である。
L(1,1,2)の `p0=ζ²,p1=ζ,lambda=0` において
`Q=(1-ζ²)X0²+(ζ-1)X1²` をu²QとするPBW族は、
u≠0でL(1,1,2)、u=0で量子Fermatを与える。
座標の同定は `(X0,X1,X2,X3)=(x,y,t,z)`。
従って両型の閉包はこの包絡で交わる。

対角三次 `Σλ_i x_i³`（全λ_i≠0）の中心性は `a³=b³=c³=1` と同値で、
torusの三捩れは27点である。一般のL(1,1,1,1)点で同じ中心切断が存在するわけではない。
一般normal cubicの単項式的存在とも区別する。
強いH3に限る全skew包絡の五型・31パラメータ分類は分類ノートと
`thm:all-skew-H3-geometric` を参照する。27点の軌道長6の枝はgeneric rank 3で除外される。
H3へ制限しない全四頂点AS stackの他型（R22/S23/E3）との交叉や局所成分重複度は、このノートの確定結果には含めない。

R(1,3)閉包を排除する不変量では、Z(B)₁だけでは足りない。
四頂点の非零一次元が二次零因子を持たない開集合で、四本のnormal lineと
return `φ0φ1φ2φ3` が射影恒等となるprojective incidenceを取る。
proper射影の像は閉で、四つの独立基底変更に不変であり、中央tを持つR(1,3)一般点はこの条件を満たす。

量子Bのnormal line pairのsupportはq行が一致するclassである。
4と3が互いに素なので行の比例は一致に帰着し、classは `{0},{1,2},{3}`。
return指数はそれぞれ `(0,1,1,1),(2,0,0,1),(2,2,2,0)` で、いずれも射影恒等ではない。
この排除はpointed/rolled-up表示でも成立する。
ambient射の独立研究は https://github.com/uedakazushi/nc-cubic-ambient 、
標識忘却は https://github.com/uedakazushi/nc-cubic-unmark を正本とする。

## 5. 固定量子Fermat包絡上の切断と慣性

全中心三次は `At³+f(x,y)+Cz³` の六係数で、
normal一次直線schemeは二孤立点[t],[z]と `P(span(x,y))` からなる。
t,zの交換はζをζ^{-1}へ逆転するためgraded自己同型ではない。
従って `Aut_gr B=G_m×GL₂×G_m`。

`AC disc(f)≠0` のP⁵開部分U_Fは一つの軌道である。
binary cubicの三根をPGL₂で移し、係数を三乗根で規格化できる。
F₀を元として固定する群は `μ₃⁴⋊S₂`（162元）、
次数スカラーとの共通μ₃を除くと
`H54=(μ₃⁴/μ₃^diag)⋊S₂` を得る。
`G=Aut_gr B/G_m^deg` に対して `G/H54→U_F` はエタールかつ幾何学的に単射・全射なので同型、
`[U_F/G]≃BH54` となる（`thm:fermat-gerbe`）。

ambientとの同定付きのfiberはU_F、ambient自己同型で割ったsectorはBH54である。
全weak moduliでambientも動かす形式近傍をこのBH54と同定しない。
境界 `AC disc(f)=0` は現行の全skew分類により強いH3から除外される。
任意の構造対象・偏極を取り直した裸の圏についての主張とは区別する。
またH54を、自然自己同型・次数スカラーの規約を指定しない全Abel圏自己同値群とは呼ばない。

## 6. 有限提示・形式局所性・一般fiber

Artin上の全次数平坦な次数変形では、有限次元Nakayamaを各次数に使って低次数の生成・関係上界を保つ。
これは全次数平坦性を仮定した環の変形の議論であり、任意のcategory変形への無条件な適用ではない。

条件2の候補は
`P=incidence(J2⊂V² rank6,J3⊂V³ rank45,VJ2+J2V⊂J3)`
という有限型projective incidenceである。
J₃は最小三次関係でなく全三次核。
B=Q(R)のoverlap次元をkとすると新しい三次関係はk−3本で、AS4ではk=4である。

全upper-rank minor idealはnoetherian性により有限生成だが、
無限個のlower-rank openの交わりが通常の開になるとは限らない。
所望Hilbert値の点におけるArtin近傍では各非零minorが単元へ持ち上がり、
有限型の形式局所模型が得られる（`prop:hull`）。
この一般論だけから全weak stackの代数性を宣言しない。
強いH3の開性・代数性は、現行原稿の有限次数平坦性・許容性・相対再構成の追加証明による。
通常の族にはnoetherian性、saturation、相対Serre、導来Homの完全性と底変更等を指定する。

R(1,3)中央incidenceの一般fiberはrank 2のE₃によるP(E₃)である。
kt³の内在的sectionがBrauer-conicの捩れを分裂させ、
一般の有限自己同型で割ったcoarse birational fiberも有理となる。
正確な一般関数体はK(λ)であり、H3条件は全P¹でなく許容開で課す。特にt³商は除外する。
k=Qbarの固定包絡の中に超越λが存在するとせず、幾何学的一般体へ移る主張として述べる。
中心局所化後の代数的分離拡大と、任意の超越体拡大の大域次元保存も区別する。

## 7. 文献と検証状態

以下は原稿の入力に関する参照情報であり、今回すべての原文・証明を再監査したという記録ではない。
実行した検算と今回の限定的点検は `research/cubic_classification_validation.json` を参照する。
外部独立査読、proof assistantによる形式化、新規性の網羅的確認は実施済みとしない。

- Artin–Zhang, *Noncommutative projective schemes*, Adv. Math. 109 (1994), 228–287, DOI 10.1006/aima.1994.1087。Theorem 4.5。χ条件とSerre消滅を区別する。
- Kanazawa, https://arxiv.org/abs/1409.4101v2 、Proposition 2.4、§2.3 / Lemmas 2.8–2.9。指数=変数数の主定理と、本例で使う局所証明を区別する。
- Yekutieli–Zhang, *Serre duality for noncommutative projective schemes*, Proc. AMS 125 (1997), 697–707。balanced dualizingの入力。著者ページ https://www.math.bgu.ac.il/~amyekut/publications/nc-serre/nc-serre.html 。
- Pym, https://arxiv.org/abs/1403.6444 、Theorem 1.1、§§3.1–3.2、§3.4。量子多項式環と中央Sklyanin拡大を区別し、全成分交叉の分類を入力にしない。
- Behrend–Noohi, https://arxiv.org/abs/1507.07054 、§1、§3.5。graded algebra moduliと有限切断。これだけでintrinsic weak substackの代数性を得ない。
- AOU, https://arxiv.org/abs/2404.00175v1 、Introduction、§5、§9。非可換三次曲面の複数の定義と9頂点marking。全weak分類との一致を既知入力としない。
- Rennemo–Segal–Van den Bergh, https://arxiv.org/abs/1705.01366v2 、Lemmas 3.2–3.3。中心局所化後の代数的分離拡大に用いる。
- Cassidy–Shelton, https://arxiv.org/abs/math/0603375v2 、Definition 1.2、Theorems 1.3, 1.5。complexity c(S₀)=2、低次数正則性 `Ann(t^n)_{≤2}=0`。
- Le Bruyn–Smith–Van den Bergh, Math. Z. 222 (1996), 171–212、Theorem 2.6、Corollary 2.7、Remark 2.8、§3.1。著者PDF https://sites.math.washington.edu/~smith/Research/Central-extns.pdf 。
- Braverman–Gaitsgory, https://arxiv.org/abs/hep-th/9411113 、Theorem 0.5、Lemma 3.3、Theorem 4.1。`αδα=-δβ` の符号を含む。
- Zhang, *Twisted graded algebras and equivalences of graded categories*, Proc. LMS (3) 72 (1996), 281–311。中央化では具体的な積と必要なnormal直線の不変性を併記する。
- OU, https://arxiv.org/abs/2508.04986 、Definition 1.1、§3。有限完全強例外列を持つAS surfaceという比較対象。
