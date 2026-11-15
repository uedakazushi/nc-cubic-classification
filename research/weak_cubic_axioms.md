# 現行研究ノート：weak cubicの四問

2026-11-15 / recognition-v5。最初に00_research_plan.mdを読む。完全な新証明はpapers/weak_cubic_axioms.tex。証明の重複は避け、再開に必要な補足をここに残す。

## 構造的な整理

定義に全整数のh0が入るので仮定1は自動。Rの負次数は零。sがheartを保つという条件は、負twistも使うため両方向のexact autoequivalenceとして読む。rankは裸のAbel圏には未定義なので、s不変のtorsion Serre部分圏とrank関数を固定するか、整域section環の商斜体から定義する。反例では後者が使える。

全weak対象、条件2付き、AS4二次包絡＋正則三次核という超曲面認識部分、R13中心拡大型部分は別々。含意を逆にしない。smooth proper enhancementを要求する定義と、今回のgd2＋Serreの定義も同一視しない。

## 統合後のweak定義とPymの交点

次数1・3の共通weakly marked条件は、Gabriel–Krull商圏でrank-one torsion-freeかつexceptionalなO、Serre逆作用s、AZ ample、h_d(n)=1+d n(n+1)/2（n≥0）。従来のexceptionalityなしの広いcubic公理はpre-weakと呼ぶ。Ext^1(O,O)=0が冗長とは未証明である。負次数の切断消滅はrank-one、正次数Hilbert増大により自動。quadric/weighted提示は共通公理に入れない。

量子Fermat BはPym §3.1のCY skew torus T=(Gm)^3、q01=a,q02=b,q03=(ab)^-1,q12=c,q13=a/c,q23=bc、(a,b,c)=(ζ,ζ,1) に属するためL(1,1,1,1)型。Pym §3.2のL(1,1,2)型でp0=ζ²,p1=ζ,λ=0とし、Q=(1−ζ²)X0²+(ζ−1)X1² を u² Q とする族はu≠0でL112型、u=0で量子Fermat B（X0,X1,X2,X3)=(x,y,t,z)を与える。PBWにより平坦なのでBはL1111とL112の交点。既存の四頂点正常直線return不変量によりR13の閉包外である。

中心対角Fermat三次 F=Σλ_i x_i³（全係数非零）の中心性はa³=b³=c³=1と同値。T[3]は27点であり、一般L1111で同じ中心切断があるわけではない。一般のnormal cubicやweak曲面の不在は示していない。残りR22/S23/E3との交叉、全四頂点AS stackの局所成分の重複度は未決定。Pymの一次資料 arXiv:1403.6444 Theorem 1.1, §§3.1–3.2を参照。

## 標準正規境界が認識問題を解く範囲

R/(t)=S0/(g)、t正則正規一次、S0がnoetherian Koszul AS3、g正則正規d次(d≥3)なら、Q(R)はAS4、Rはその一本の正規d次商（現行定理3.1）。条件2とAS包絡の存在を仮定しない。低次数一致B_i=R_i (i≤2)がtの低次数正則性を保証し、Cassidy–Shelton Theorem1.5のcomplexity2から全正則性を得る。この低次数regularityの導出が、単にambientをPBWと仮定する議論との違い。

中央化はta=σ(a)t、R'=R^{σ^-1}、a⋆b=aσ^{-deg a}(b)。σ(t)=tでtは中心化する。境界自己同型は二次包絡S0へ持ち上がる。gの直線とI_d=kGが不変なので、normal/regularを保ってuntwistできる。任意のnormal元が任意のtwistでnormalのまま、という一般命題ではない。

I∩tB=tI、I/tI=(g)の二つを両側で使うとI=BG=GB。regularity of Gはt-adic leading termのgから従う。S0 domainならB domainだが、R domainは一般には言えない。d=3では条件2、overlap rank4、中間コホモロジー消滅が従う。境界の存在を全weak公理から示したものではない。

固定S0=T(W)/(U)とL=(U⊗W)∩(W⊗U)上のBG条件はδα(L)⊂U、αδα+δβ=0、βδα=0。新スクリプトはcommutative S0で12独立係数を使い、これがLie Jacobi＋中心2-cocycleとなることを恒等式で確認する。一般の非可換境界のPBW性は文献定理を入力にした通常証明であり、この検算で置き換えない。

## 反例の代数

Bの変数を(t,x,y,z)と書けば、tx=ζxt、ty=ζyt、tz=ζzt、xy=yx、xz=ζzx、yz=ζzy。F=t³+x³+y³+z³。q行積1、q³1なのでBはCY4、Fは中心正則。R=B/(F)は標準cubic Hilbert値を持つ。三次中心は一般R13より大きく、x³,x²y,xy²,y³,t³,z³の6次元。中心一次・二次は零。

t局所化のdegree0ではu1,u2が可換、ui u3=ζu3 ui、Σui³+1=0。r=u1/u2、v=u2³、w=-1-(r³+1)v。中心体k(r,v)上のsymbol algebra(v,w)_ζはw付値でvの残余が非cubeなのでdivision。この理由でRのrank1/torsion-freeの意味が保証される。単に中心元でdomainを割ったからdomain、と推論していない。

tailsのgd2はKanazawaの指数=変数数の定理をそのまま引用せず、指数3・変数4へ局所証明を適用。中心完備化でnormal yiの三乗がradicalに入るので(yi)がnilpotent ideal mod radicalとなりyi自体radical。正規正則元によるgldim降下と、all-nonzero fibreのtwisted finite group algebraの半単純性からchart gldim2。全局所perfect性を貼り合わせた後にSerre双対を使う。

## R13閉包を排除する不変量

Z(B)1だけでは周期表示の差を排除できない。四頂点の非零線型元が二次零因子にならない開集合で、四つのnormal line Liとreturn φ0φ1φ2φ3が射影恒等であるというprojective incidenceを取る。proper射影なので像は閉、四つの独立基底変更で不変。中心tを持つR13一般点はこれを満たす。

量子Bのnormal line pairのsupportはqの同一行のclass。4と3が互いに素なことを使って行の比例は一致になる。classは{0},{1,2},{3}、returnの指数は(0,1,1,1)、(2,0,0,1)、(2,2,2,0)。どれも射影恒等でない。従ってcomponent exclusionはpointed/rolled-up表示においても成立する。

## 固定量子Fermat ambientの中心開部分

中心三次はAt³+f(x,y)+Cz³、6係数。正規一次直線schemeは二孤立点[t],[z]とP(span(x,y))であり、t,zを交換するとζとζ^-1が逆になるのでgraded自己同型にはならない。従ってAut_gr B=Gm×GL2×Gm。

AC disc(f)≠0のP5開部分は一つの軌道。binary cubicの三根をPGL2で移し、代数閉体の三乗根で係数を規格化する。F0のexact stabilizerはμ3^4⋊S2（162元）、次数スカラーとの共通μ3を除いてH54。G/H54→U_Fはétaleかつ幾何的に単射全射なのでscheme同型、商stackはBH54。慣性はstackの内容であり粗い点だけではない。

strict fibre（ambientとの同定付き）はU_F⊂P5、ambient自己同型で割ったsectorはBH54、全weak moduliの変形は未計算。H54を全Abel自己同値群と呼ばない。AC disc(f)=0の点がすべて非weakだという主張も未証明。既存R13の一般中心P1と異なる現象だが、比較しているlevelは区別する。

## 提示と代数性

Artin平坦変形で低次数生成・関係上界が保持される証明は有限次元Nakayamaを各次数に適用する。全次数の平坦性を先に仮定しており、categoryの任意変形へ無条件に適用しない。

P=incidence(J2⊂V² rank6,J3⊂V³ rank45,VJ2+J2V⊂J3)は有限型projective。J3はminimal cubic generatorsではなく全次数3のkernel。B=Q(R)のoverlap次元kなら新三次関係はk−3本。AS4ではk=4。

全upper-rank minor idealはNoetherian性で有限生成だが、全部のlower-rank opensの交わりが一つの通常開集合とは限らない。Artin近傍では各非零minorが単元に持ち上がるので有限型formal hullが得られる。全stack代数性へ飛躍しない。通常の族にはnoetherian/saturation/relative Serre/Hom basechangeを指定する必要がある。

## Generic fibreの意味

R13 central incidenceはP(E3)、rankE3=2。kt³の内在的sectionはBrauer-conicの捩れを分裂する。一般の有限自己同型で割ってもcoarse birational fibreはrational。K(λ)が正確な関数体。weak条件の成立は保持稿のgeometric generic central valueで確認するが、全P1の点で成立するわけではない。特にt³商は除外される。一般k=Qbarの固定ambientに超越λを選ぶことはできず、幾何学的一般体へ進むものとして述べる。

## 一次資料と参照箇所

- Artin–Zhang, Noncommutative projective schemes, Adv.Math.109(1994),228–287, DOI10.1006/aima.1994.1087。Theorem4.5、χとSerre消滅の区別。DOI書誌確認。元PDFの全再監査ではない。
- Kanazawa, arXiv:1409.4101v2, Proposition2.4、§2.3/Lemmas2.8–2.9。既存の反例証明で確認した適用箇所。本文の主定理は指数=変数個数。今回のFano cubicはlocal proofの適用で別に証明する。
- Yekutieli–Zhang, Serre duality for noncommutative projective schemes, Proc.AMS125(1997),697–707。著者公開ページ https://www.math.bgu.ac.il/~amyekut/publications/nc-serre/nc-serre.html 。balanced dualizing input。著者ページ確認、PDF取得失敗もあり全原文再監査としない。
- Pym, arXiv:1403.6444, §3.1および§3.4。quantum polynomialとcentral Sklyanin拡大を区別。全6成分の成分交叉の分類を本稿の前提にはしない。
- Behrend–Noohi, arXiv:1507.07054 / https://webspace.maths.qmul.ac.uk/b.noohi/papers/NCStable.pdf 、§1,§3.5。graded algebraモジュライと有限切断。内在的weak substackの代数性をこの論文だけで宣言しない。
- AOU, arXiv:2404.00175v1, Introduction,§5,§9。複数のnc cubic定義と9頂点marking。全weak分類との一致は既知入力ではない。
- Rennemo–Segal–Van den Bergh, arXiv:1705.01366v2, Lemmas3.2,3.3を既存の中心分枝証明で使用。任意の超越体拡大がglobal dimensionを保つとはしていない。centre localisation後に代数的分離拡大を用いる。

## 確実性

量子Fermat反例の通常証明を保持し、今回その有限検算を再実行した。新しく検討した証明は正規境界による認識と中心三次軌道の同定である。外部独立査読、proof assistant、新規性の網羅確認はなし。保持したsurface/R13稿は今回全再監査しておらず、そこでのWeyl商・有限Hessian商の主張を新たに検証したと報告しない。新稿の最重要な否定結果はそれらの一般商の詳細に依存しない。

## 今回確認した追加の一次資料

- Cassidy–Shelton, PBW-deformation theory and regular central extensions, arXiv:math/0603375v2。Definition1.2、Theorems1.3/1.5を原文で確認。complexity c(S0)=2、低次数での正則性の意味はAnn(t^n)_≤2=0。
- Le Bruyn–Smith–Van den Bergh, Math.Z.222(1996),171–212、著者PDF https://sites.math.washington.edu/~smith/Research/Central-extns.pdf 。Theorem2.6、Corollary2.7、Remark2.8と§3.1（normal linear elementのtwist中央化）を原文画像で確認。
- Braverman–Gaitsgory, arXiv:hep-th/9411113、Theorem0.5、Lemma3.3、Theorem4.1。αδα=−δβの符号も原文と照合。
- Zhang, Twisted graded algebras and equivalences of graded categories, Proc.LMS(3)72(1996),281–311。本文では中央化の具体的積を示し、必要なnormal直線の不変性を別途確認する。

新規性未確認。今回、新しい認識とFermat軌道の通常証明を検討し、新旧二つの計算を再実行した。前回のKanazawa依存を保持するが、同論文全文を今回再取得・再監査したとは報告しない。
