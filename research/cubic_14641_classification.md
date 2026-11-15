# 14641反標準型：現行分類ノート

滑らかな次数3楕円THCR（translation）の全filtered deformationについて、Rees環の二次包絡がnoetherian quadratic Koszul CY AS4で、一本の正則中心三次の商になることを証明した。AS4包絡を外部に仮定せず復元できる。非可換では境界が一意なので、intrinsic中央楕円H3の幾何学的群oidは有限gldim filtered deformationとfiltered同型に一致する。Hesse/Moore・対称線型係数・中心三次の単一線型核による有限候補atlasと全同型係数比較を得た。有限Nは中心McKay条件で全admissibilityを判定し、被約固定N族では相対中心とH3開性も証明済み。無限位数の全bad値、全intrinsic family stack・既約成分、中央境界を持たないH3被覆は未完成。正規境界の被覆と三角境界全有限位数の判定は後述の現行結果を参照する。次は非捩れ三角境界の残る許容性と、全H3の未被覆CY/非CY領域を縮小する。

classification-v12 では、積分した族の全次数平坦性・noetherian quadratic Koszul CY AS4 認識を、明示的な開集合 V={h∈H, (1-gamma²)≠0, Delta≠0} 上で証明した。入力は Iyudu–Shkarin Theorem1.1/Corollary6.1、EG形式変形定理、および64個の三次持上げ恒等式・256個の四次巡回恒等式・単元小行列式 -p^6 を確認した LBS 中心拡大定理である。中心三次の関係類の非消滅も巡回商の二係数で全パラメータについて確認した。gamma≠0 では低次数中心が0,0,1、滑らかな楕円THCR境界となり、全中心値の H3 判定は正確に一つの affine 中心切断の有限大域次元へ帰着する。定義体上超越的な全 D は H3。位数4の枝 gamma^4=1+h^3 では固定包絡の悪い D は有限であり、h=1,gamma=2^(1/4),A=1,B=C=0,beta=(-1,0,0),D=pi は明示的な非Clifford H3 対象となる。悪い値の全一覧・全内在的群oid・H3相対開性・降下・全包絡被覆は未解決。

classification-v11 では、Etingof–Ginzburg の付録と著者サイトにある Rains の E6 中心元を規約変換し、全パラメータで三交換子の関係恒等式を独立検証した。`alpha=-4*gamma*(A,B,C)` と置き、正規化した中心元に定数補正を加えると、全 Clifford 切断が実際の有理式による中心表示へ積分する。gamma=0 での全係数・関係証明書の分母はよい h の全底上で正則であり、全次数の「中心性」の障害は解決した。これは包絡族の全次数平坦性、AS4 認識、切断後の H3 条件や新成分を証明したという意味ではない。次はこの積分した具体的表示でそれらを検証する。

classification-v10 では、この族から外れる指定四方向の一次中心 incidence も全係数で判定した。双対数上で最高次を `(1+epsilon*gamma)yz+(1-epsilon*gamma)zy` に変え、対角項を `epsilon*alpha_x*tx`（巡回）だけ動かすと、三次中心切断の持ち上げは正確に `alpha=-4*gamma*(A,B,C)` のとき存在する。持ち上げを明示し、全ての h,beta,A,B,C,D に通用する次数4の階数86、三次交換子階数15、単元障害行列式 `-9/(4*(1+h^3)^2)` を検算した。これは指定方向の一次 incidence であり、積分可能性・全変形空間・新しい H3 成分を主張しない。 また、この明示的持ち上げの二次障害も全係数で消え、対角係数の二次補正 kappa と中心切断 G2 を計算した（epsilon^3=0）。中心性の全次数積分は v11 で解決し、H3 族への実現は未解決である。

2026-11-15 / classification-v9。最優先目標は全H3の分類。**Skew包絡部分の幾何学的対象は分類したが，全AS4包絡を覆ったわけではない。** 主証明は papers/weak_cubic_axioms.tex の sec:14641-classification とそこでinputされるcubic分類節。

## 対象・認識・同値

共通のintrinsic weakly marked nc del Pezzo（Gabriel–Krull rank-one torsion-free exceptional O、Serre逆作用tau、AZ ample、三次のHilbert関数）を保ち、反標準環Rが一次生成、二次包絡B=Q(R)が左右noetherian quadratic Koszul AS4型14641であるH3を扱う。外部ambient、埋込み、周期表示を標識に追加しない。

Levasseurの整域定理とHilbert値からR=B/(G)、正則正規G∈B3、六二次＋一三次関係が従う。H3の幾何学的pointed exact同値は反標準環のgraded同型を誘導し、その自己同型群はAut_gr(R)/次数スカラー。族の2-stack・相対降下は別に残す。OU/AOUのmarkingやZhang同値、導来同値で置き換えない。

## 全ambientに対する新しい構造制限

papers/sections/cubic_nakayama_incidence.tex。

- 構造対象の飽和とEnd(O(n))=kから、商圏で自明なgraded twistは次数スカラーに限る。
- 正規化をGv=σ_G(v)Gとすると、H3では **μ_R=1、σ_G=μ_B^{-1}、μ_B(G)=G** となる。まずSerre比較からμ_R=ξ_cを得て、RRZtri Theorem 4.1(2)へAS index 1で適用しc=1とする。
- RRZtriの追加仮定Dε(R)≠0は省略しない。Bの有限自由k解消PからR⊗_B Pを作ると、perfectでcohomologyはkとk(-3)だけとなり、非零ε複体が得られる。これにより全H3で仮定を満たす。一次資料はRRZ arXiv:1302.0437v2 Lemma 1.5、RRZtri arXiv:1408.0536v3 Theorem 4.1(2)、Zhou–Shen–Lu Proposition 2.3、YZ Theorem 4.2。
- 固定Bに対して **W1={G:Gv=μ_B^{-1}(v)G}という単一の140×20線型核** に絞られる。非零G∈W1は自動的に正則正規でμ_R=1となるが、滑らかさ・rankの十分性は別問題。一般のWc={G:Gv=c μ_B^{-1}(v)G}はc≠1で零。
- Bがgraded CYならσ_G=1なのでGは中心。一般のXi=hdet予想を入力には使わない。
- ただし全H3のBがCYであるとは限らない。非CY符号型の全H3族を下記で構成・分類した。

## Skew包絡部分の幾何学的分類：31パラメータ・五型

papers/sections/cubic_skew_normal_incidence.tex は全正規三次直線の被約locusを交換指標blockの射影空間として記述する。一般qで正規直線は単項式20点だが、これを20個のH3曲面と数えない。

H3に限ると全skew torusでc=1となり、W1={χ_i(a)=μ_B(x_i)/x_iの逆数}に制限される。任意のcocycle untwistと線型簡約な対角群の同変Extを使い、各座標点のjetにx_i²x_jが必要と証明。256通りのjet選択を19共役型にまとめ、整数Smith証明書を標準ライブラリで全等式・unimodularityまで再検証する。これにより全qは2乗根か3乗根。49個のjet候補から共通因子を持つ12個を除き37個、さらに次のrank障害で6個を除き31個となる。

| ambient型 | 座標パラメータ数 | 一般同型類の次元 | 全admissible係数・慣性 |
|---|---:|---:|---|
| 可換 | 1 | 4 | 滑らかな三次式のPGL4商 |
| CY符号型 | 4 | 1 | G=At³+t(Bx²+Cy²+Dz²)+Exyz、ABCDE(AE²−4BCD)≠0。粗い同型類w=AE²/BCD∈Gm\{4}、自己同型S4 |
| 非CY符号型 | 6 | 2 | G=binary cubic+ℓ2 x2²+ℓ3 x3²。ℓ2,ℓ3をx0,x1にした後adΔ≠0。全開部分P7のPAut(B)商、一般慣性μ2² |
| 3乗根・中心一次型 | 8 | 1 | G=At³+Bx³+Cy³+Dz³+Exyz、ABCD(E³+27BCD)≠0。粗い同型類w=E³/BCD∈A1\{−27}、w≠0で位数27、w=0で位数81 |
| 3乗根・二重指標型 | 12 | 0 | G=At³+binary cubic+Cz³、ACΔ≠0。全admissible開部分は既存のBH54 |

各族のsmoothnessは有限同変cocycle比較で可換三次の滑らかさと比較し、**rank条件は別途** quaternionまたは3次巡回代数の非Normで整域性を証明した。S4座標置換だけでなく、全線型ambient自己同型とintrinsic pointed exact同値の幾何学的群oidまで扱う。上表は全H3の成分表でも、相対stackの分類でもない。

### 除外する3乗根の六点

既存27点の(0,1,2)軌道6点は滑らかなtailsを持つ対角Fermat商を与えるが、generic代数はM3(K)となる。chartでs=−t(t+1)/(t+r³)=Norm(−u(u+1)/(u+r))、u³=tという明示的Normがあり、構造対象のgeneric像は単純加群三個の直和となる。Gabriel–Krull rank-one条件に反する。27点をそのまま27個のH3型と読むのは誤り。

### 非CY分枝

q01=1、他の五係数−1、G=x0³+x1³+x0 x2²+x1 x3²。μ_B=σ_G=diag(1,1,−1,−1)、μ_R=1。滑らかさ、整域性、Serre作用、例外性、GK rank、AZを全て証明した。固定Bの全H3係数はP7の明示開部分で、Aut(B)=GL2×(Gm²⋊S2)。一般の有理商はk(u+v,uv)、u=ac/b²,v=bd/c²。これはPymのCY族のみで全H3を覆う方針への具体的反例。

## 非skew標準CY chartの一般点の除外

papers/sections/cubic_pym_generic_exclusions.tex。Pymの指定標準chartでL(1,1,2)、R(2,2)、S(2,3)の非空稠密開部分とE(3)の非零変形は中心三次が零となる。全CY包絡の分類ではなく、一次資料のAS4/CY chartを入力とした結果。

- L112：weight filtrationのassociated graded skew環で、独立なp0,p1に対する中心指数は四成分が全て等しい必要があり、次数3では不可能。
- R22：Sklyaninパラメータ(2,3,−5/7)でQQ上に商空間B3,B4を構成。中心交換子140×20行列の20次小行列式280000000000/279926361≠0。外部AS/CY入力と核の上半連続性で一般点を除外。
- S23：Ore中心は基礎可換三変数環のδ不変式。divergence-freeなb=c=−1,d=0でδ:A3→A4の10次小行列式−243。一般点も単射。
- E3：CGG積の中心はkerX∩kerY。4Xの三次weightは全て1 mod4で非零。従って中心三次なし。

これでPym六つの標準CY chartの一般点として残るのはR13。特殊locus・交叉・他のAS4族は除外していない。量子Fermatと非CY符号型を保持する。

## as4からの限定的輸入と全パラメータ除外

固定SHA `60eacafa28156a5fc62f74eae004d64a84675f4b` のas4を使用した。正確な入力・hash・仮定・元の監査状態はresearch/as4_imports.json。README、plan、COVERAGE、CLAIMSと必要な証明本文を確認し、元の量子単冪42ケース・scalar大交換子・CY四交換子の三検証器を再実行して元証明書と一致した。全CY統合証明や全AS4被覆を独立監査したとはしない。

規約は **as4の右巡回ν=本稿μ^{-1}**。量子環で列積と行積が逆であることを確認し、右twist B=C^H に対してμ_B=μ_C H^{-4}を用いる。

papers/sections/cubic_as4_reductions.texで以下を証明した。

- H3包絡の中山固有値には次数3の積が1となる共鳴が必要。一種類の固有値λしかなければ、λ³=λ⁴=1からλ=1。従ってas4で未処理部分が残るscalar半単純部分−I,±iIの全Jordan層はH3には不要である。通常のdet μ=1は仮定しない。
- 半単純化Cと単冪Hに対して、W1(C^H)のFはH(F)=F、Fv=H μ_C^{-1}(v)Fを満たす。この輸送公式で、Cが量子多項式環なら正規化の対角性によりH=1。**量子標準半単純化を持つ全AS4部分のH3は既存31点・五型だけ**となる。非skew単冪持上げも含む全被覆の主張である。
- 中心二平面上の[u,v]=q(b,c)≠0というCY基底は、中心体上でWeyl環になるため全正規元が中心に限られる。全単冪持上げでもH3は存在しない。
- **任意の非零斉次二次導分δに対する普通のOre包絡 k[x,y,z][T;δ] はH3にならない。** W1の三次元Gは基礎可換環内にあり、R=(k[x,y,z]/G)[T;δ]。Ore軸P=πk[T]の自己Extは次元1,3,4,4,...となる。Rees/change-of-ringsと局所双対でline objectsのPに対するacyclicityを証明し、Tate解消を誘導して計算した。未証明のT局所化や有限rankからの高次外挿を使わない。
- 可換三平面を保つCY Ore基底の単冪持上げも除外した。微分体上の単純環K[T;δ]で正規元を局所化するとF∈k[x,y,z]、従ってHはTの線型shearだけになる。twist後も非零普通Ore導分δ−h Eulerなので上の障害が残る。
- as4の指定構造定理へ適用し、**CY標準半単純化の交換子次元が4以上なら、H3包絡は可換環だけ**と分かった。三交換子beta型を標準半単純化とする全持上げも除外される。Pym S23の非零Ore族は一般点だけでなく特殊値も除外された。

いずれもgraded/1周期の包絡に対する結果であり、as4の最小周期2・4のZ-algebraを直接H3へ移していない。元のheart・構造対象・反Serre orbitを同定しないまま周期性を内在的障害と読まない。

## 良い楕円中心拡大の全切断と分裂族の完全な固定ambient分類

papers/sections/cubic_r13_cut_reduction.tex。固定Bについて、CY AS4・中心正則一次t・active随伴環S[t]・Sの低次中心Z1=Z2=0,Z3=kg・gを持ち上げる中心Ω・H=S/(g)が滑らかな整楕円曲線のTHCR、という仮定を明示した。全R13境界を覆うという仮定はしていない。

- 全λで gr_active Rλ=H[t] が整域となり、Rλ=B/(Ω+λt³)も整域。Hilbert多項式の加法性から低成長部分をA0,A1へ入れ、tの冪の鎖と境界coh EによりO∉A1を証明した。全非零右イデアルがfRを含むことと商の成長低下により、Oは全λで内在的Gabriel–Krull rank-one torsion-freeとなる。整域性からこのrank条件を無条件に推論したものではない。
- D=B[t^-1]_0, ω=Ω/t³ とすると、正確な残条件は **Λ_B={λ:gldim D/(ω+λ)<∞}**。滑らかな境界と行列因子化の分母払いにより、この条件からtails gldim=2を証明した。逆向きも中心局所化のExtで確認した。例外値の有限性やΛ_Bの代数的開性は一般に未証明。
- その他の飽和、例外性、AZ、Serreとheart保存は全て確認した。固定ambientのH3幾何学的群oidはΛ_BへのPAut(B)の作用群oid。φt=at, φΩ=bΩ+ct³ならλ↦(c+a³λ)/b。相対stackの表示と無条件には同一視しない。
- 複素数体上、有限生成定義体k0上超越的な全λはadmissible。RSV Lemmas3.2/3.3を原文で再確認し、中心局所化と代数的分離拡大だけを用いた。可算例外から有限例外や有理点の存在は推論しない。
- **有限位数translationの楕円境界を持つ固定Bでは非admissible値が有限個、Λ_Bは非空Zariski開となる。** Rains arXiv:2107.13540v2 Theorem2.13を原文で確認し、全切断代数U=D[a]/(ω+a)≅Dの中心をfiberwise一定rankの交換子行列から持ち上げた。中心上有限を示してRSV Proposition2.1へ適用する。一変数の十分な開集合の補集合が有限なので実際の悪い集合も有限となる。例外値の明示、無限位数境界への適用、ambientも動く全相対族の開性は未解決。
- **分裂中心拡大B=S[t]では複素数体上Λ_B=C*を完全に決定した。** 非零λはスカラー作用で一軌道で、超越的な良い値から全非零値へ移せる。λ=0ではP=πk[t]のExt^n(P,P)がH上kの最小Betti数と一致し全nで非零。逆Hilbert級数(1-z)²/(1+z+z²)が多項式でないため解消は終了しない。
- Sのpoint schemeが滑らかなEで非零translationを持つならAut B=Aut S×Gm。固定ambientの全H3群oidは **BH_S**、H_S={(ψ,a):ψg=a³g}/対角次数スカラー。1→μ3→H_S→PAut S→1。これは非分裂変形のrigidityではない。

新規検算 computations/verify_cubic_r13_cuts.py はQQのSklyanin(a,b,c)=(1,2,3)で中心次元0,0,1、分裂包絡の中心三次140×20行列rank18、point曲線の滑らかさ三chart・非零character不在三chart、Hilbertと作用の恒等式を確認した。AS正則性、THCR認識、高次Extや全λの滑らかさを低次rankから推論していない。

## 位数二Clifford–Sklyaninの分裂包絡族：全切断・有限比較を解決

papers/sections/cubic_clifford_full_cuts.tex。これは前節のZ(S)2=0を外した新しい非skew族である。S_hの三関係を yz+zy=h x² とその巡回形とし、h≠0,h³≠−1,8、B_h=S_h[t]とする。

- S_hは中心多項式環P=k[u=x²,v=y²,w=z²]上階数8のClifford環。g_h=xyz−h(z³−y³+x³)/2、T_h=((4+h³)uvw−h²(u³+v³+w³))/4 とすると、全中心はP[g_h]/(g_h²+T_h)。S_hのAS3/CY/Koszul/noetherian条件を確認した。THCRへの射はpoint graphと楕円曲線のpencil trickから直接構成し、g_hによる商とHilbert級数まで照合した。translationは位数2。中心原点以外ではAzumaya quaternionとなる。
- Z(B_h)3 は g_h,tu,tv,tw,t³ の五基底。全H3切断はG=g_h+t(Au+Bv+Cw)+Dt³で、全係数で商は整域かつGabriel–Krull rank-one。D=0ではaugmentation点のExt1が3次元となる。中心tでSerreを[2]へ自明化するとExt1は非退化交代形式を持つはずなので、奇数次元障害により除外される。
- D≠0ではアフィン中心曲面 T_h+(Au+Bv+Cw+D)²=0 が滑らかであることがH3の必要十分条件。中心原点を避けるためAzumaya性を全域で使える。単に中心が特異なら非可換環も特異と推論したものではない。
- h=1の固定包絡について、悪い非零Dを正確に与えるmonic四次式Ψを明示した。係数はI=A³+B³+C³,J=A³B³+B³C³+C³A³,K=ABCの多項式。polar写像P2→P2の次数4の有限flat族における中心値のnormがΨとなる。係数の次数と不変式空間を通常証明で先に制限し、次元2,4,6,9の全空間について16点の有理数評価行列の全rankと4×4normを照合した。これにより全パラメータの恒等式を厳密に証明した。補間を全AS4の正則性の外挿に使っていない。
- **h=1の全固定包絡H3群oidは [V/G(3,3,3)]**。V={Ψ(I,J,K,1)≠0}⊂A3、群の位数54。粗い同型類空間はSpec k[I,J,K,Ψ(I,J,K,1)^−1]、全慣性は明示的monomial作用のstabilizer。
- **一係数切断G=g+A t x²+Dt³の全例外はD=0,−16A³/27,8A³/49**。A≠0ではκ=D/A³が完全不変量で、群oidは(A1−{0,−16/27,8/49})×BS3。A=0,D≠0は一軌道で慣性G(3,3,3)。
- **hも動く上記Hesse族全体の全切断は四次元の有限商 [W/Γtilde]**。Dを1へ規格化し、T_h+s(Au+Bv+Cw+s)²の四つの偏微分のresultant非零を要求する。ΓtildeはHessian群216のμ3中心拡大で位数648。全包絡間の矢をC_h(MX)=c C_h'という九flex保存行列で覆い、二次中心への具体的作用も与えた。全648比較の定義と54/108への固定h stabilizerの増大条件 h⁶+20h³−8=0 を証明した。実際の切断慣性は(h,A,B,C)のstabilizerであり、この比較群全体を一般切断の慣性とは呼ばない。
- Aut B_hの恒等成分はGm²なので単冪自己同型は恒等のみ。標準半単純化がこのB_hとなる部分にも非自明な単冪持上げはない。

上記は明示的なHesse分裂包絡族を持つ部分の全幾何学的分類であり、全H3の成分性・非分裂包絡の被覆・相対降下ではない。前節の「分裂包絡のペンシルΛ=C*」はZ(S)2=0等の低次中心仮定下の定理であり、この五次元中心三次族へ誤って拡張しない。

外部入力はIyudu–ShkarinのLemma3.7/Theorem1.1（このp=qの場合のKoszul性）とLemma5.1の全九flex保存群。必要な証明本文を確認し、全216射影行列・base作用12・kernel18・全特殊固定点多項式をQQ(ζ3)で独立照合した。再現はverify_cubic_clifford_cuts.py と verify_cubic_clifford_hesse.py。source hashと検証範囲はvalidationに記録する。

## 非分裂Clifford中心拡大：二次ポテンシャルを全パラメータで除外

同じ証明節の sec:clifford-nonsplit-lift-obstruction。h∈Hについて、中心tと三関係 yz+zy=h x²+α_x t x+β_x t²（巡回）を持つ包絡を調べた。

**この表示がH3包絡ならα_x=α_y=α_z=0。βは任意で、この必要条件に例外hはない。** 先に六関係の混合quarticを構成し、256個の符号付き巡回恒等式と常数minor−1から、H3下でμ_B=1を証明した。正規三次Gは中心で、G mod t は非零g_hでなければならない。G=g_h+tq+t²ℓ+t³dのt²商において、三つの係数汎関数は任意のqの寄与を消し、−3α_z/(2(1+h³)),3hα_x/(2(1+h³)),3α_y/(2(1+h³))を与える。障害行列の行列式−27h/(8(1+h³)³)は全Hで非零。

停止する五つの非可換置換から表を計算し、99個全ての次数4関係挿入をQQ[h,α,1/h,1/(1+h³)]上の恒等式で確認した。有限パラメータの標本からの推論ではない。H3のAS4仮定とt正則性を用いており、低次検算だけで任意係数の包絡をAS4と認定していない。

一般の対称ポテンシャルH=H0+t f2+t² f1、H0=2xyz−h(x³+y³+z³)/3では、唯一のt平行移動でf2の混合項を消せる。残る対角項が上の障害で零となるので、H3ではf2はJac(H0)2の三次元部分空間に属し、平行移動でf2=0へできる。従ってこの非分裂問題は**定数関係項βだけのClifford拡大**へ縮小された。

β族のrank-one Clifford退化点ではAzumaya性が失われる。分裂族の「中心曲面の滑らかさのみ」の判定をそこへ拡張してはならない。この局所homological判定は次節で解決した。as4のα表示から用いたのは固定SHAのmixed quartic式だけで、全軌道や全係数AS4判定は輸入していない。輸入範囲はas4_imports.jsonに更新した。

## 全β族の判定を完了：非Azumaya通常二重点と七次元groupoid

主証明 papers/sections/cubic_clifford_beta_classification.tex。前節で残ったB_{h,β}（yz+zy=h x²+β_x t²と巡回）の全βと全中心三次切断を扱う。これは指定した対称ポテンシャル中心拡大部分の完全な幾何学的分類であり、全AS4包絡の被覆とは区別する。

1. **全βで包絡はnoetherian quadratic Koszul CY AS4型14641。** 中心多項式環上の階数8 Clifford PBW基底でtの正則性を確認し、mixed quarticのt収縮がS_hの三次トップへ全射となることを確認してLBS Theorem2.6/Corollary2.7を適用した。原文の全仮定と該当証明を点検した。低次rankからのAS4外挿ではない。
2. **全H3候補はG=g_β+t(Au+Bv+Cw)+Dt³。** 全候補の整域/rank・飽和・例外性・AZは既存認識で保証され、残るアフィン商Uの中心はF=det Q_β+(Au+Bv+Cw+D)²。Q_βの対角はu,v,w、off-diagonalは(hw+β_z)/2等である。
3. **完全な必要十分条件：F=0の全特異点は、rank Q_β=1にある通常二重点のみ。** rank>=2ではAzumayaなので中心特異点は不許容。rank1の通常二重点では完備化環がk[[s,t]]⋊{±1}となり大域次元2。中心が特異でも許容される。より退化したrank1点は、自己Ext1の奇数性またはcross-Ext1のYoneda対の退化でSerre双対性に反する。rank0も除外される。二つの明示的な空集合条件（Jacobian/minor/Hessian）で全係数を有限判定できる。
4. 局所証明はSchur補a,b,c,mと二頂点表示を使う。E=d(a,b,c,m)のrankは2か3。rank2なら自己Ext1=1。rank3ではquadratic relation Kの非退化性が必要で、Cauchy–Binet恒等式 det(E^T Hess(ab−c²+m²)E)=8detK が中心のHessian条件と同一視する。十分性はA1の階数一反射的加群の二分類とEnd(C⊕M_odd)=k[[s,t]]⋊Z2から証明した。一般NCCR存在の未監査分類を入力にしていない。
5. **pure volume切断G=g_βの全許容条件**は、三つのquadrics 2yz−hx²=β_x等の長さ8 character完全交叉が被約であること。その場合中心は四個の通常二重点を持つ。h=1,β=(-1,0,0)では中心 (5u−1)vw−u(u−1)²−v³−w³=0 の四点 (1,0,0),(-1/7,-4η/7,-4η²/7)（η³=1）が全て許容nodeである。
6. **指定対称ポテンシャル中心拡大部分全体の幾何学的groupoidは[P/G]、一般次元7。** GはGm恒等成分とHessian216成分群を持つ。全矢はC_h(MX)=cC_h'(X)、β'=a0² M^Tβ/c、a'=a0 a q(M)/detM、D'=(a0³D+a0 a k_{β'}(M))/detMで完全に判定される。Dの混合補正を落とさず、D=0の許容対象も含む。恒等成分の重みはβ2・a1・D3。全慣性は明示的stabilizer、一般には自明。pure volume三次元部分の一般慣性はμ2。
7. 全B_{h,β}のAut恒等成分はtorusなので非自明な単冪自己同型はなく、この標準半単純化を持つ部分にも追加の単冪持上げはない。

再現は verify_cubic_clifford_beta.py（全h,βの8×8 volume・Schur・character変換・普遍Hessian/Ext対恒等式、四node具体例）と verify_cubic_clifford_beta_action.py（QQ(ζ3)(h)上の全9生成元合成とD混合項）。verify_cubic_clifford_lift.pyも再実行した。相対intrinsic stackの効果的降下、全ambientの被覆や成分性は未完成。

## 次の最優先課題：skewでない包絡

1. 位数二対称ポテンシャル中心拡大は、非分裂β族も全切断・全幾何学的矢まで解決した。次はこの七次元部分の他ambient方向への変形と、別の楕円位数・非対称ポテンシャル中心拡大を扱う。一般の良い非分裂R(1,3)のアフィン中心値Λ_Bを有効に決定し、良い楕円仮定の外の境界を覆う。分裂B=S[t]の全切断と群oid、良い固定Bの整域/rank認識は完了したため再び未判定扱いしない。既存7次元ambient、8→7、markingの比較を同じ対象で照合する。
2. L112/R22/E3境界と他のClifford・skew Ore・非CY AS4族でW1を計算し、三次商が存在するambientを制限する。非CY符号型を保持し、全対象をPym六族へ押し込めない。
3. 位数二Hesse分裂族で未判定扱いしていた全切断・全包絡間有限比較・単冪持上げは解決した。残るCY標準半単純化のc<=3（betaを除く）と、次数3共鳴を持つ非スカラー半単純部分を優先する。Skew五型の形式近傍、他ambientとの交叉、一般cubicからの非skew変形を調べる。固定ambient分類を既約成分性や変形rigidityと読み替えない。
4. 相対Nakayama・飽和・GK rank・Serre/AZ条件、自己同型の相対rigidification、族の効果的降下を証明する。全H3被覆の証明前に全分類とは呼ばない。

## 再現と今回の検証範囲

- python3 computations/verify_cubic_skew_strata.py
- python3 computations/verify_cubic_nakayama.py
- python3 computations/verify_cubic_skew_jets.py
- python3 computations/verify_cubic_skew_admissible.py
- python3 computations/verify_cubic_pym_generic.py
- python3 computations/verify_cubic_as4_reductions.py
- python3 computations/verify_cubic_r13_cuts.py
- python3 computations/verify_cubic_clifford_cuts.py
- python3 computations/verify_cubic_clifford_hesse.py
- python3 computations/verify_cubic_clifford_lift.py
- python3 computations/verify_cubic_clifford_beta.py
- python3 computations/verify_cubic_clifford_beta_action.py
- latexmk papers/weak_cubic_axioms.tex

最初の三検証器は標準ライブラリ。整数証明書の再生成だけ--regenerateとSymPy 1.14を使う。admissible検証器はSymPy 1.14で特性零の恒等式・Jacobian unit idealを、Pym検証器はQQ上の商空間・非零小行列式を検査する。TeX依存をworkspace内に復旧しLuaLaTeX全文組版を実施した。生成PDFは追跡しない。詳細な検証状態はresearch/cubic_classification_validation.json、今回のas4適用範囲はresearch/as4_imports.json。独立査読・形式化・網羅的新規性調査は未実施。並行のheart/corner更新は保存し、今回その全証明を独立監査したとは報告しない。

### 対称potentialのj0境界（classification-v26）

h=-1,gamma=2,A=1,B=C=0,beta=0の非分裂CY AS4包絡に、729G0=13y³−3yzx+13zyx+z³−30tyz+6tzy−72t²xという正則中心三次を得た。旧積分式を1+h³倍して特殊化する。point schemeはx³+y³+z³+9xyz=0で、potentialのj0とは区別する。translation点(3:−1:1)の良い還元位数は5上9、13上6なので無限位数。超越的Dの全切断G0+Dt³はH3。代数的D全体は未判定。証明はcubic_j0_boundary.tex、独立な有理数次数4交換子・最高記号非消滅と有限体位数の検算はverify_cubic_j0_boundary.py。

### 三捩れ量子Weyl chartの全中心と固定切断（classification-v27）

関係yz=qzy+b1,zx=qxz+b2,xy=qyx+b3（q²+q+1=0）ではX=x³,Y=y³,Z=z³,W=xyz+(b1x+q b2y+b3z)/(q−1)が全中心を生成する。d=1/(q−1),e=−(2q+1)/9としてW³−d b1b2b3W−XYZ−eΣbi³Xi=0。滑らかなHesse中央切断X+Y+Z−3lambda W+Dの中心は実際にこの中心環の商と一致する（最高記号中心とRainsで証明）。b=(1,1,1),lambda=0では全非H3値は(D²+4e)(D²+36e)=0の四つ。D²+9e=0の二値は中心A1だがMcKay(1,2)でH3。他の四値にはcharactersがなく非H3。証明はcubic_quantum3_center.tex、全中心式と臨界値の厳密検算は二つのquantum3検証器。次は全beta/lambdaのMcKay分配と判別式、または中央境界のないH3被覆を進める。

### 正規一次楕円境界の現行分類（classification-v38）

mu_R=idの正規三次商でR/(t)が滑らかな次数3楕円THCRの場合、共役theta（ta=theta(a)t）は有限位数1,2,3,4,6。lambda1のunipotentはSklyanin二次minor（可換例外は三次方向微分）で消える。s=t^mの中央分母払いによりH3 iff gldim U有限（U=R[t^-1]_0）を証明。中央化Zhang twist R^(theta^-1)は同じUとgrU≅Hの通常の濾過を与えるが、mu_Rtwist=thetaでintrinsic反標準gradingは変わる。

位数4,6および位数3D0はskew elliptic coneとなり除外。位数3はB=S[t;lambda],G=g+D t³、B CY、g中心、mu_S=scalar(lambda)となり、全admissibilityはD!=0。S[g^-1]の中央cube-root有限etale/separable拡大が(S/(g−1))[z±]となるため有限glを得る。さらに巡回固有tensorの8次元空間をsl3の随伴模型へ同定し、全trace零Jordan行列のpoint determinantを計算した。滑らかな楕円境界を許すのは重複固有値の対角型、すなわち量子P2包絡のみ。中心三次はbinary cubic+z³で、滑らかさから全てFermatへ直せる。従って位数3非中央部分は既知の量子Fermat一対象、幾何学的群oidはBH54に一致する。

位数2の全包絡被覆も証明した。S=QHのmu_S(g)=−gとhdet mu_S=1から誘導楕円自己同型fは反転型involution。mu_S²=scalar(c),c³1を適切なscalarで補正したalphaでSをtwistすると、境界は二つの可換involutionの積、従ってtranslation order1or2。既証のtranslation包絡CY性がc1を強制し、Sは可換P2のinvolution twistまたはCliffordのswap twistに限る。前者の全非skew定数持上げはPBW overlapとWeyl中心化環k[w²]の奇偶で除外され、既存符号skew分類へ入る。

Clifford swap枝はBの関係yz+zx=hxy+b t²,zy+xz=hyx+b t²,x²+y²=hz²+c t²,tは全activeと反交換。W1は一本、6G*=x²z−xzy+yzx−y²z+zy²−zx²。有限Gamma cocycle (-1)^(a e'+r a')で中央Clifford beta=(b,b,c)に戻すとG*は純volume。H3 iff長さ8 CI（2yz−hx²−b,2zx−hy²−b,2xy−hz²−c）が被約。h=b=c=1は実際の非skew・非CY H3例で、degree4三正規式、CI長さ8・Jacobian unit、全512 cocycle恒等式を厳密検算済み。証明はcubic_normal_order2_clifford.tex、quantum排除はcubic_normal_order2_quantum.tex。

Clifford swapでは正規滑らか楕円境界ktが一意。mu_B負固有空間の候補au+bz+ctに反交換子rank1を課すと、minor−4h²でa=b0（非被約底でも同じ）。全intrinsic矢はt→a t′,X→M X′、M alpha=alpha M、r_h^0(MX′)=N r_h′^0(X′)、N beta′=a² betaという有限係数方程式を共通次数scalarで割ったもの。任意底変更の全graded同型functorを与え、一般次元2、一般慣性mu2×mu2。

許容条件は明示quartic Delta_h(b,c)=(h c−2b)((h³−2)b−3h c)(c²+h²bc+2h b²)の非消滅と同値。固定hで四つのbad方向は相異なる。P1_betaから四点を除く係数方向で、任意底変更・fpqc fiber条件に適合する。二character枝x=yと2z+h(x+y)=0の分解・全係数恒等式を検証済み。証明はcubic_normal_order2_arrows.tex。

非中央正規一次楕円境界部分では位数2の被覆・全許容条件・全幾何学的矢と位数3のBH54を得た。相対intrinsic圏の全stack降下、中央無限位数の全bad値、正規一次境界のないH3の被覆は未完成。全H3にこの境界があるとは主張しない。次は有限end dg模型を用いた中央無限位数のsmoothness locusと、境界被覆の欠落を調べる。

### 四shift windowと独立Nakayama監査

全正規三次商でBのKoszul分解をRへtensorするとTorはk,k(−3)のみなので、tailsでO(−4)→O(−3)^4→O(−2)^6→O(−1)^4→Oの完全列となる。四連続shiftで全shiftを生成。正規楕円境界認識済H3ではE=O⊕O1⊕O2⊕O3がDbのclassical generator、EnddgのH0dim55,H2dim21。76次元最小A∞台を得るが高次積を打ち切っていない。Toën math/0609762v3の有限An定理は両側smooth properを仮定し、Lemma3.14はquasicompactnessなので、これだけで中央無限位数bad D有限性を主張しない。

h=b=c=1のClifford swap包絡でKoszul双対を独立計算しE0..4=(1,4,6,4,1)、左右Frobenius積非退化、mu_E=swapxy(t,z固定)、mu_B=−swapxy(t,z負)、普通detmu_B−1・top作用1を確認。全次数AS4は別のcocycle証明による。

Clifford swapの中心模型は証明・原稿化した（classification-v40）。u=x+y,v=x−y,w=z+h u/2、A=u²,B=v²,C=w²,D={u,w}/2,a=vw,s={u,v}とする。G*=−[vw,u]/4なのでa,sがRで中心、T=t²,P=xy+yx,Z=z²は包絡で既に中心。Delta可逆ならT,P,Z↔B,C,Dは可逆で、五中心二次の全関係は三scroll minor BC−a²,Cs−2Da,as−2DB。Rは中心subring C上Clifford有限、Hilbert比rank8、generic三変数Cliffordの偶部分rank4 quaternion。normal cubic scroll Cの正規性によりZ(R^2)=C、ProjZ(R)=F1、PI degree2を証明した。Omega=(uw−D)t中心三次でOmega²=T(D²−AC)。qgrRはF1上rank4 quaternion order、tau²はhyperplane E+2F twist。全分岐と極大性も次の通り証明した。検証器はh=b=c=1で中心二次dim5、対称積rank12、全minor、volume交換子恒等式を独立確認。平面conic Γ_h=−2(1+h³)ξr+3h²r²+h(h³−8)s²/4 と Q=L2 ξ²−4(h²b−c)ξr+4hb r²+L1 s²（L1=hc−2b,L2=(h³−2)b−3hc）を得た。detQ=−4L1(c²+h²bc+2hb²)、L2zeroはQ=Γ自身。四bad方向は三singular conicsと一致member。許容conicはΓと四点横断。F1=Bl_pP2,p=[1:0:0]でgeneric quaternion symbol(−T/C,(D²−AC)/C²)のBrauer分岐は二conicのstrict/pullbackそのもの、例外E/fibreには分岐なし。分岐類3E4F、K+半分岐=−(E2F)/2、klt log del Pezzo degree3/4でrank4を掛けるとcubicdegree3。

Λ=~R²はB,C,D,sの四patchで三生成Cliffordとなりlocallyfree rank4。全閉完備局所模型は分岐外Mat2formalplane、smoothbranchはreflection skewgroup、四nodeではquantumformalplaneq−。各gl2。余次元1の非平方residueにより巡回valuation最大order、反射性で大域最大order。完成後最大性を主張しない。表示族のcommondegree scalar rigidificationは有限対角の分離既約DMstack2、generic inertia mu2²、任意底変更/fpqc局所表示族の降下を得た。抽象intrinsic Abel圏族との完全同一視は残る。

次は中央無限位数の全bad値・相対smoothness（有限76次元cohomologyだけでは高次A∞を省けない）と、正規一次楕円境界を持たないH3の被覆を進める。

### 三角境界のq-so3 Casimir pencil

q²+q+1=0、B=(t central; yz−qzy=tx,zx−qxz=ty,xy−qyx=tz)は既証PBW CY AS4。f=(1−q)/3,e=−(2q+1)/9,f³=e,e²=−1/27。V=B/(t−1)の中心はChebyshev X=x³+q²x cyclicとOmega=xyz+(q−1)(x²+z²)/3+(q+2)y²/3、関係Omega³+f Omega²−XYZ+eΣX²=0。Vはk[X,Y,Z]上free27、中心3foldに五つのODP。CY双対/filtered maximalityでVは対称MCM最大order、正則中心上Azumaya。

G_D=Omega_h+D t³、U=V/(Omega+D)の全中心はFricke XYZ−eΣX²+D²(D−f)=0。中心特異Dは0,f（各A1一つ）、2f/3,−f/3（各A1四つ）。Vの五characterはD0と2f/3に配置され、PI3のA1 McKay(1,2)で両値good。Df,−f3はV centre正則上でU=Mat3(singular centre)となりbad。compact中心C_Dは∞triangleで常にsmooth。辺のdegree0 radical v=ty^-1はv³=(T/Y)(1+q²v²),J³=(T),residue k(u)/k(u³)。非可換DVRでmax/PI3division、辺coverは両端totallyram3。CHI2.7/2.17 terminal theoremで∞全localgl2。従って全H3 iff(D−f)(3D+f)!=0、全Rdomain。

Bのcentre1=kt、V character五点だからBはskewでない（skewなら中央tを外すと量子3変数のcoordinate axes characters）。B CYのため非中央normal smoothE境界なら既証m3skewFermatに限られるが矛盾。唯一の中央t境界はtriangle。よって許容Rは既研究normal smoothE locusの外に実在し、missing-boundaryの一部分を埋める。証明cubic_quantum_triangle.tex、厳密validator/certificateはquantum_triangle。全intrinsic矢も確定：D不変、Aut_gr B=Gm×A4、次数scalarを除く慣性A4が全Dで一定。固有値差unitとcross linear係数比較により非被約底でも追加矢なし。相対rigidified表示stackはgood Dline×BA4、全中心形成も任意basechangeに適合。次は一般qの三角境界をq-difference/GWA模型で調べ、中央無限位数と他missing boundaryへ進む。全H3被覆は未完成。

一般qの三角境界（classification-v47）：q!=0,+-1の全V_qに対し、q-difference表示の三関係とOmega=-Dを全係数で厳密検算し、PBW最高T係数のChebyshev独立性から全U_{q,D}・R_{q,D}の忠実性と整域性を証明した。B_qはCY AS4。非捩れでは全中心k[t,Omega_h]、位数N>=3ではChebyshev c_N(x),c_N(y),c_N(z),Omegaが全中心を生成。非捩れまたはN>3の全H3候補はこのpencilに限る。全候補graded矢は[Q/S4]、Q={(q,D):q!=0,+-1}、A4は基底に自明、奇置換は(q,D)->(q^-1,-q²D)。候補表示stackは分離DM2で慣性A4、任意基底のgraded同型functorを記述する。奇数位数N>=3ではclassification-v50で全判定を得た：全中心はFricke XYZ+alphaΣX²+beta_N(D)=0、alpha=(q²−1)^−N、beta_N=−(q²−1)^−3N[2+P_N(w_D)]、w_D=−(q+q^-1)−(q²−1)³D/q²。特異DはN+1個、端点w=+-2の二値D±だけが非H3。全N−1内部特異値は、古典型w=−(q^d+q^-d)と非古典型w=q^(2d)+q^(-2d)、1<=d<=(N−1)/2の明示既約三重対角表示で全A1点に次元d<Nのsimpleが存在し、McKay( r,N−r )が両方正。無限遠triangleは指数Nのterminal order。従ってH3 iff(D−D+)(D−D−)!=0。位数5では独立な全係数2x2表示とPhi5中心配置も確認。任意奇数Nの表現再帰・Casimirは形式Q=q^d,J=q^j,R²=−q²/Qで厳密検算済み。次は偶数位数と非捩れqの全許容条件を調べる。一般q全体のH3開性・抽象intrinsic family比較は未証明。証明cubic_quantum_triangle_general.tex、検算verify_cubic_quantum_triangle_difference.py。

偶数位数の三角境界（classification-v52）：N=2M>=4、Gamma_i=−(q²−1)^N c_N(x_i)、k=2+P_M(w_D)により全中心はGamma_x Gamma_y Gamma_z−ΣGamma_i²−2kΣGamma_i−k²−4k+4=0。Huang1509.08719v4 eq5/§4.3を正規化して使用し、N4は独立PBW次数12で全関係を検算した。k!=0,4は持続A1三点、k0四A1、k4一D4。両端対角bのM次元三重対角表示が全k!=4の持続三点を覆う。k0内部の追加点には古典型r<M（既存M-simpleとA1 rank和2Mの排他性で追加点配置を証明）、k4内部には非古典型四つのd-simpleと古典型r=M−2dを置いて全五McKay指標を覆う。従って全D!=D±はH3。D+はM奇数ならAzumayaの特異A1中心商、M偶数なら四つのM/2-simpleでrankを使い切るD4なので常にbad。D−もclassification-v53で全偶数位数に対してbadと証明した。c_M(x)がy,zと反交換する正規元で、D4中心fiberでは二乗零なので各simple上零。xはM個の相異なるweightに分解し、関係式/Casimirの二元一次系（行列式はqの奇数冪−1の積）から全隣接block合成が非零scalarとなる。従って全simple次元はMの正倍数、full D4ならrank>=6MだがPI次数2Mなので不可能。これで全有限位数q!=+-1についてH3 iffD!=D±を完全判定した。中心・order・表現・全矢の分類は指定pencil内の主張であり全H3被覆ではない。粗座標theta=q+q^-1,w=−theta−h³D/q²を得て、候補stackはtheta!=+-2の平面上のA4共役twist中立gerbe。固定NのH3表示stackはphi(N)/2個の(A1_w minus{+-2})×BA4、全中心形成は任意基底変更と可換。全有限位数許容族は正規smoothE境界を持たず候補空間に稠密。次は非捩れqの許容条件と全H3のmissing-boundary被覆を進める。1998 HKP math/9805048は根付き単位での表現を構成するが序文に完全性未証明と明記するため、全既約表現分類として輸入していない。


非捩れ三角境界（classification-v55）：f_j(x)=x²−kappa²(q^j+q^-j)²の左右Ore集合を、左/右x乗法の2x2行列でdet f_j(M)=f_(j-1) f_(j+1)と証明した。局所化U_SはGWA G=A0(sigma,a_D)の反転固定環。A0=k[u±,r(q^ju)^−1:j∈Z]、r=u−u^-1、a_D=(u²+q²u^-2+1+q²)/(q²−1)²+(q²−1)D/q、A=rT,B=rbT^-1。反転u->u^-1,A->−B,B->−A、反不変単元rによりaveraging e fullなのでG#Z2とMorita同値。Bavula著者講義Theorem3.1（Dedekind基底そのものの定理）を一次監査：重根はgl∞、単根はgl<=2。非捩れqでD±の重根u²=−q,qは除去軌道u²=q^(2j)から外れるためU_SもUもgl∞、従って全非捩れ端点も非H3。D!=D±ではU_S gl<=2だが、U自体と射影無限遠の許容性は未証明。式はverify_cubic_quantum_triangle_gwa.pyで全有理式検算、証明cubic_quantum_triangle_gwa.tex。

次の具体的着手：射影頂点[x:0:0:0]でPBW重みw(x)=0,w(y)=w(z)=1,w(t)=2を使う。各PBW還元は重みを下げず、先頭環でxは正規なのでxの形式的microlocalizationを取れる。degree0先頭環はa=y/x,b=z/x,s=t/xの量子Heisenberg as=qsa,bs=q^-1sb,q^-1ab−q²ba=s。G/x³の先頭はq^-1ab+s/(q²−1)=q/(q²−1)(ab−qba)、正則正規なので形式的頂点商の先頭環が厳密に量子平面となることを証明した（classification-v56）。PBW重みの降下濾過と形式x-microlocalizationで先頭環を計算し、正則先頭元の商と完備filtered-graded分解の持上げで局所gl2。非捩れqでは座標変更係数1−q^(1−i),1−q^(1−j)の片方が高次単項式ごとに非零なので、全高次補正を消して完備量子平面に同型。証明cubic_quantum_triangle_vertex.tex、検算vertex。qgrへのperfection降下はまだ未証明であり、形式局所環gl2だけで全境界smoothとは結論しない。

文献上の障害：Kaplan–Schedler ANT2023「Multiplicative preprojective algebras are2-CY」は一次PDFを読むとTheorem1.2がunoriented cycleを含むquiverに限定され、affineD4はConjecture1.1の範囲。検索snippetがこの仮定を省くので誤輸入しない。EOR math/0406480 §11はlegパラメータdistinct時のMPLAとのMorita対応であり、全DAHAパラメータで有限globaldimを保証していない。これらを非捩れpencil全H3の証明として使わない。


proper楕円四次元Sklyaninの全排除（classification-v58）：標数0代数閉体上、滑らかなE、degL4、sigma translationで位数nが∞又は1,2,4以外の標準Sを全排除した。g1,g2中央二次正則列のTHCR商と中山公式でmuS=id。n∞及び有限n>3は中心重みからZ3=0。残余n3はcentre z0..z3(deg3),g1,g2(deg2)、二つの六次完全交叉、Z3dim4、S1dim4、PIdegree3である。

一般norm補題：connected graded domain Bが正規中心Z上有限、PIdegree n>=2なら、Nrd:B1->Z_nはbasepointfreeなn次写像。射影normのpullbackO1=O(n)がampleなので像へfinite、従ってdimZ_n>=dimB1。等号なら射影全射、各Gは一次元ellのnorm、Cayley-Hamiltonでell times degree(n-1)へ分解する。商に零因子が生じる。よってCY・normal-centre-finite・PI3のH3包絡にはdimZ3>=5が必要。SklyaninN3は等号dim4で全Gが一次式×二次式となり排除される。射影norm P3->P3はdegree27。複素数への限定やgenericGへの限定は不要。退化非楕円Sklyaninや任意Zhang twistは含まない。

一次資料WWY1802.06487v2 Lemma2.9,Props2.11/2.12/2.18,Thm3.13を読み、regularseq/domain/centre/normalityを使用。as4最新429d8a3...は4entrypointsの現行概要とSklyanin/CY claimを参照したが新定理輸入なし。検算verify_cubic_sklyanin_rank_obstruction.pyは重みHilbert・a-invariant−1・rank9・K²1/3と、一般traceless3x3行列のnorm因数分解を厳密検算。全排除はprojective normの通常の証明であり有限標本からの外挿でない。第三者独立査読・形式検証・新規性確認は未実施。

独立な複素幾何補題も保持：商特異点だけのprojective Q-delPezzo上のorderがcodim1 AzumayaかつH1Lambda0ならgeneric Brauer類は零。traceでq0、quotientresolutionはKod−∞でrational、small quotient群GのH2(G,Z)=0をS3/Gから示して例外residueを消し、Br rational resolution0を用いる。Sklyanin排除にはこの補題へ依存する必要はなく、norm補題の直接証明を正本とする。


三乗根量子so3固定包絡の全切断（classification-v60）：全ZB3=P4[alphaOmega+betaX+gammaY+deltaZ+epsilon t³]を判定。線型元のnormは b³X+c³Y+d³Z−3q bcd Omega+(a³+q²a(b²+c²+d²))t³、像は正確にDelta=alpha³+27beta gamma delta=0の三次超曲面。全Delta0 cutは一次×二次に因数分解しnondomain。Delta!=0では境界はsmoothE、I1 nodalcubic、I2 line+conic、I3triangleの四種、phi=diag(1,q,q²)は各成分でdegree3、node両枝でfullyram3。centre境界滑らか、terminalorderでlocalgl2、非自明residueでgenericdivision3、全商domain。

Compact centreをS=3Omega/2f,U=X/2e cyclic,T=t³で正規化するとY:2UVW−T(U²+V²+W²)+3TS²+2S³=0 inP4。五ODP p0=(0,0,0,0,1),p_eta=(−1,eta1,eta2,eta3,1),eta product1。全四点rank4なのでplaneを含まず、全hyperplane section integral。H3 iff Delta!=0 andH notinY^dual。Yregular点のtangent cutはAzumaya singularcentreでbad、Ynodeで非退化A1ならonecharでfullMcKay(1,2)、退化rank2ならA2以上でonechar/PI3rankがfullMcKayを阻む。全矢・相対graded表示stack=[U/A4]、分離既約DM4、generic inertia1。全慣性は1,C2（v=(beta,gamma,delta)座標軸）,C3（四符号軸）,A4（v0）だけ。C2/C3固定planeはdim2、A4pencilはdim1、異なるplaneはpencilで交わる。表示族flat、全中心commutes任意basechange、fpqc降下。抽象intrinsic圏族の全被覆や全H3のcomponent性は未主張。

有限判定：affT1のF1=2UVW−ΣU²+3S²+2S³、H=aS+bU+cV+dW+epsilon0についてF1=H=0,gradF1=lambda(a,b,c,d),lambda!=0が空、かつHの通る各五nodeで法線Hessian逆二次式!=0。Groebner unit idealと五二次式で全切断を判定できる。検証full_cutsはuniversalPBWnorm、norm cubic、五node・全四点rank・inverseHessian、Casimirpencil bad2値との一致、H=S/S+U/U+V+Wのgood examplesとA4/C2/C3慣性をexact確認。論文cubic_quantum_triangle_full_cuts.tex。次は非捩れ一般qの残るadmissibility、未被覆CY/非CY包絡、全大域component/交叉/abstractfamily比較を進める。


三乗根共鳴incidenceと境界閉包（classification-v61）：任意非被約底で全中心三次はalphaOmega_q+beta c3x+gamma c3y+delta c3z+epsilon t³、正確な条件は(q²+q+1)(beta,gamma,delta)=0。最高active次数でq−1,q²−1の単元比較により証明。被約incidenceは水平2次元と二つの垂直P4、交叉P1。qroot3、alpha1の局所式u beta=u gamma=u delta=0（u=q−q0）でdim2と4がdim1curveで交わり、接空間dim5。全候補矢はS4商、奇置換(q;alpha,beta,gamma,delta,epsilon)->(q^-1;qalpha,gamma,beta,delta,−q³epsilon)。整域fiber locusはDelta=alpha³+27beta gamma delta!=0。候補成分を全H3成分と呼ばない。

固定三乗根U/A4ではintrinsic normal smoothE locusが正確にbeta gamma delta!=0。他のnormal smoothE境界はB非skew/CYと既証m3認識で排除。missing-boundary Dは3座標超平面の商として既約normal-crossing divisor、正規化[U_beta0/V4]。I1/I2/I3のdim3/2/1、慣性1/C2/A4、全てsmoothE H3の特殊化。alpha1粗chartはepsilonとtetrahedral不変P=Σbeta²,Q=beta gamma delta,R=Σbeta²gamma²,J=平方差三積、J²=P²R²−4R³−4P³Q²−27Q4+18PRQ²。I2横断coarseA1、smoothE-C3横断A2、I3はA3/A4×curve。粗境界Q0はJ²=R²(P²−4R)、正規化A=gamma²,B=delta²でP=A+B,R=AB,J=AB(B−A)。証明cubic_quantum_triangle_incidence.tex、検算incidenceは普遍comm/divisibility/q反転と全12不変式、Molien一致を厳密確認。


一般Zhang/cocycle twist包絡の排除（classification-v63）：A noethKoszulAS4 domain、B=A^phi、eta=hdet phiとすると、W1(B)はphi安定なので非零eigen F(phiF=lambda F)を選べる。untwistするとFv=theta(v)F,theta=lambda eta^-1 phi muA^-1。このnormalizerはZAをpointwise固定する。量子QではNewton normalizerがdiagonalなのでphi diagonal、全Zhang twistsQのH3は既存skew五型31coordsだけ。単冪/半単純の仮定不要。

properSklyanin Sでalpha beta gamma非零かつ中央quadric pencilの4固有値distinctを明示仮定。Sym²S1->S2 injective（六関係の交代射影非退化）なのでtheta g1=g1,theta g2=g2はordinary quadraticformsの厳密保存。pencil作用素distinct固有値よりtheta diagonal±、関係式よりeven sign。phi scalar times signであり、非自明case(1,1,−1,−1)のtwistはrescale(1,−i b c,i c,b),beta=b²,gamma=c²でS(alpha,beta^-1,gamma^-1)へ同型。六関係を全係数で単元倍比較した。点Eの作用は二捩れtranslation、4tau不変なのでpropernnotdiv4のまま、前節norm排除で全ZhangtwistH3を除外。退化pencilには適用しない。

標準V4cocycle mu((p,q),(r,s))=(−1)^(ps)、degxiが4群次数を各一回持つDavies twistも除外。CYはsign group top hdet1（中央quadric正則列とtranslation THCRcanonicalから）とKoszulFrobenius topGdegree0により証明。centerはGgraded、中心成分F_gをuntwistするとnormalizer theta_g=alternating bicharacter sign、theta_g F_g=F_gなのでF_gはS^(theta_g)でcentral。新translationtau_g=tau−s_g(E2)がorder3の場合だけ存在し、3tau=s_gなので高々一つのg。従って中心3はn3又は6の時だけdim1、それ以外0。唯一の生成元は標準PI3centreのG-degree gのzi=xi³+xi*(centralquadric)、quadricはGdegree0、theta_gもcocycleも積xi*Qを変えないので全cubiccutsnondomain。

証明cubic_twisted_envelope_exclusions.tex、検証器twisted_envelope_exclusionsは全六符号関係・param式・centralpencil固有値差・alternatingprojection・cocycle16tableをexact確認。一次資料Davies1512.05717v2の(3.4),(3.5),(4.3)を読みgrading/cocycle規約だけ使用。Hyp4.1のinfiniteorder point/fatpoint結果を有限位数へ輸入しない。AS4性全specialをこの資料から無条件に推論していない。抽象有限群cocycle、任意twisting systems、退化/他exoticelliptic全体の被覆は未主張。


Stafford型と標準cocycle全族の排除（classification-v68）：Davies1502.06101§6.1の全許容領域T（alpha,beta,gamma!=0,+-1,alpha+beta+gamma+alpha beta gamma0）、d∈P1から指定二禁止値を除くS_infinity,S_d1,S_d2と標準Klein cocycle、循環変種は全てH3包絡から排除した。退化/他exotic楕円/全AS4の被覆は未主張。

全TでNakayamaは通常(-I,diag--++,diag++--)、cocycle後(-I,-I,I)。群作用により対角、平方関係からmu=lambda*sign、hdetmu1からlambda8=1、族Frobenius pairingの正則性と既約性で一定とし、QQの一点計算で定数を決定。低次数計算だけからAS4性を推論せずDaviesThm6.1.10を入力。全Tの五関係上でg1,g2は中央、除いたfiはmuで正規、残余中心二次qとfiはTHCRへの核の正則正規列。W1はTHCRへ単射（核ならG=ell q、q中央でellも正規一次となるがTHCRで不可能）。

point curveの二次式は中心g1,g2と異なる：v0²+v1²+v2²+v3²=0,(1+beta)v1²+(1−alpha)v2²+(1+alpha beta)v3²=0。WWY1802.06487v2 Definition-Lemma2.4,(2.5)のsigmaをE点(0:r:s:1),r²=−a(1+b)/(a+b),s²=b(a−1)/(a+b)で反復。第二反復の第一係数−4(a+1)(a+b)(b−1)非零から4tau!=0が全Tで従う。第三正規化座標の条件u3=2(a+b)(ab−3a−b−1)KLM,v3+z3=−2(a−1)L²M²,w3−z3=2a(b+1)K²L²。K=ab+a−b+3,L=ab+a+3b−1,M=3ab−a+b+1。K=M0は(a−1)M−(3a+1)K=−4(a+1)²で不可、L0上z3=1024(a−1)²(a+1)^6/(a+3)^5非零。正規化第三座標は全Tで非零なのでK²除去はregular sigma³への延長で正当化される。従ってsigma³=theta_e1 iffL0、chart欠落なし。固定点不在は正しいpoint curve二式で確認済み。

通常Sd1/Sd2のW1はL!=0で0、L0でdim2。L0を(alpha,beta,gamma)=(a,(1−a)/(a+3),(a+1)/(a−3))、a!=0,+-1,+-3で表示。Sd1はF2=x2Q2,F3=x3Q3、Sd2はF0=x0Q0,F1=x1Q1で、全a,dにおいて非零・独立。THCRのnormalizer付き三次の比はsigma不変、自由な六重商上degree2の切断へ入るのでdim<=2。両pencilは一次因子s x2+t x3又はs x0+t x1で覆われ、明示degree3 basepointfree写像P1->P(W1)が全射なので全Gfactor。Q0..Q3,H,H0の式はcubic_stafford_exclusions.tex。

残余CY cocycleSd2の中心群次数gをuntwistしてnormalizer theta_gを得る。h=g+e1による通常の符号Zhang twistはStafford同士へ移り、h=e1は(a,b^-1,c^-1),d'=−(d+1+bc)/(bc)で偶奇保存、h=e2は(a^-1,b,c^-1),d'=−(d+1+c)/c、h=e1+e2は(a^-1,b^-1,c),d'=(d−b+1)/bで偶奇交換。全六関係・pencil・禁止値の対応をexact検証。中心成分は変換先W1_gと線型同型。従って群次数0/e1/e2/e1+e2の中心三次はK/L/N/M=0でだけ各dim1、N=ab−3a−b−1。四曲線はTで互いに素。生成元はxj times群次数0のquadricで符号Zhang/cocycleでも因子が保たれ、全切断nondomain。

検証器verify_cubic_stafford.py（六QQ Frobenius/rank witness）、stafford_resonance.py、stafford_resonance_even.py（全係数factor identity）、sklyanin_order6.py（全T反復）、stafford_transport.py（QQ(a,b)中央二次24式、三符号関係・pencil・禁止値・六対のdisjoint Groebner）を実行。全specialへの延長とTHCR次元評価は原稿の通常の証明であり有限標本外挿でない。全H3の被覆、非捩れ量子so3の残るaffine/qgr admissibility、退化/他exotic包絡、大域成分・抽象intrinsic族降下は未完。次は非捩れqの特殊weight軌道または残る未被覆包絡を進める。


低交換子as4表示の独立排除（classification-v69）：as4のa45f834f51a00c47443b51caf66abaf4629546b9を四entrypointとCY統合/CI22概要、二重被覆DCC1・長さ四CF2/CF3・長さ3+1CT2の具体的表示について参照。全CY被覆やAS4存在/整域/noetherian定理は新規入力にしていない。二重被覆の二族h!=0は、H3包絡を仮定したKoszul AS4双対の最高次数汎関数をQQ(i)[h,h^-1]上で独立構成し、全次数四関係を消す恒等式と左右pairingdet=+-1/(2h²)を確認して全hのmu=idを得る。一般点rrefだけでAS4十分性や特殊fiber平坦性を推論しない。a²,b²の正規作用は互いに反対符号、N=a²b²のnormalizer=-Iなのでdomainでは奇数centre0。一般にNが-Iを実現するH3包絡ならmu(N)=-Nが必要。CF2/CF3とCT2の三つの固定表示も独立Frobenius計算でmu=id、中心3の140x20行列に非零20minorがあり全排除。検算verify_cubic_as4_double_cover.pyとverify_cubic_as4_curvilinear_fixed.py、原稿cubic_as4_low_commutator_exclusions.tex。表示の借用と独立検算を、as4全分類の輸入と区別する。次はTT22の六表示の中心3/正規元を調べる。


TT22六表示の直接全排除（classification-v70）：as4固定commit a45f834... のCY_ZERO_COMMUTATORS_CURVILINEAR_TWO_TWO_COMPLETE.tex TT1-TT3から六表示のみ参照し、全射影型の被覆/AS4十分性は輸入しない。C_r(r!=0,+-1/4)をq=(4r+1)/(4r−1)で表示し、四DiamondからPBW b^i d^j a^k c^l、中央変数z1,z2上の量子トーラスdb=q^-1bdへの忠実模型a=z1 b^-1−kappa q²b^-1d²,c=z2d^-1−eta b²d^-1を構成。kappa=1/(2(q²−1)),eta=2q(q−1)/(q+1)。z1=ab+kappa d²,z2=cd+eta b²中央。先頭z1^k z2^l b^(i-k)d^(j-l)の比較からcentre3はq³!=1で0、q³1でa³,b³,c³,d³のdim4。この条件は48r²+1=0。三乗根ではdivision量子トーラスがcentre上rank9、Tr ell0、Tr ell²/2=3(uvz1+wtz2)。Nrd ell=ell(ell²−3(uvz1+wtz2))がBのcentre3へ入り、非零ellのnorm非零なのでP3->P3全射、全Gfactor。centre有限/正規の別入力は不要。generic determinantの他の零16r²+1,16r²+3はcentre0であり、最終証明はmatrixchartでなく上の全q先頭項論法。

E_t(t!=0,-2),F_h(allh)ではb,dが正規、N=bdのnormalizerはE_tで−I+二乗零nilpotent（a->−a+(t+2)b/(2t),c->−c+4(t+2)d,b/d->負）、F_hで−I。normalizerの半単純部分−Iなら整域の奇数centre0という一般補題で全排除。三固定A,B,DもQQ(i)/QQ上でcentre3 rank20をexact確認。全表示のmu=idは、対称射影U固定のRとA0=半Hess(-z2z5+z3z4−z0z1+z5²)による非零w=R A0 R^Tが巡回−という256恒等式からAS4実現の下で独立に従う。AS4最高Koszul線にwが入り双対FrobeniusmuE=-Iになるためで、存在十分性を低次数rankから推論しない。検算verify_cubic_as4_tt22_c.py/tt22_remaining.py、論文cubic_as4_tt22_exclusions.tex。次はTT211と四単純基点の未処理表示、または非捩れqso3の特殊weight軌道を進める。


DS211第二層二族の全排除（classification-v71）：as4同commitのDS1/DS2/DT1具体表示だけを参照。A_(l,r),l!=0,+-1/4は量子3平面S(b,c,d)上のcanonical Ore。q=(4l+1)/(4l−1),sigma=(1,q^-1,q),delta=(beta b²,u bc,v bd),beta=−1/(4l),u=−(16lr+1)/(2l(16l²−1)),v=8(l+r)/(16l²−1)。正規bのnormalizer単冪部分がa->a−beta bなので中心3はS3へ入る。十指数のcharacter gcdでScentre3はq3のみpurecubes三本、deltaG0からb³は消え、c³/d³はu0/v0のみ、同時零は不可。従ってBcentre3は48l²+1=0,r=3lでkc³、r=−lでkd³、他0。全Gfactor。例外B_rはc,d正規、N=c³dのnormalizer=-I+(8r−4i)E_baなので奇数centre0。AS4条件下のmu=idはA1=半Hess(-z1z4+z2z3−z0z5+z3z4)とRの非零反巡回最高tensorから独立判定。検算verify_cubic_as4_ds211.pyで四PBW diamond、全tensor係数、normalizers、三乗根comm、全十指数をexact確認。全DS211被覆はまだ輸入していない。DS3の残余も下記の全値rank coverと忠実模型により排除済み。


DS211列挙表示の全排除（classification-v72）：DS3のT_h(h!=0),U_u(u!=0)はcentre3の最大minorを全関係から構成し、Tでは(8h+1)(16h+1)/(2^23 h6)、Uでは−2^29 u6(4u−1)(48u²+8u+1)。商座標分母はTでhの冪、Uで定数のみ。座標は全関係を消し自由列でidentityなので、AS4仮定の各特殊fiberでも真の基底となる。残るT二値とU二種の値（quadric二根はQQ(sqrt−2)）を再計算して全rank20。L_±i/4,PもQQ(i)上rank20、V0もQQ上rank20。CY判定は全256反巡回最高tensor恒等式で独立に行う。一般rrefの係数だけからAS4平坦性を推論しない。

V_h(h!=-1/16)のh!=0は平方根r²=−h、p=(4r−1)/(4r+1)で全被覆。a'=a+gamma b,x=c−r d,y=c+r d、alpha=p²/(2(p+1)²),beta=1/(2(p+1)²),gamma=p/(p+1)²。四DiamondでPBW b^i x^j y^k(a')^l。中央z1,z2上の量子トーラスxb=p^-1bxにy=z2 x^-1−p b²x^-1,a'=b^-1(z1−alpha x²−beta y²)で忠実に入る（補助重みz1=3,z2=1の先頭項が相異なる）。z2=xy+p^-1b²,z1=ba'+alpha x²+beta y²中央。先頭指数からcentre3はp³!=1で0、p³1すなわちh1/48でdim4。三乗根division rank9でTr ell0,Tr ell²/2=3(uvz1+(wt+u²/4)z2)。Nrd a'=(a')³−3z2a'/4とb³,x³,y³が中心基底、全linear normはBcentre3に入りP3->P3全射なので全Gfactor。h0は固定rank20で処理。これでDS3/DT1列挙の三固定・四1param・一2paramを全排除。上流の全AS4射影型の被覆/存在十分性は依然新規輸入していない。

検証verify_cubic_as4_ds211_remaining.py（全値rank cover）とds211_v.py（全平方根被覆model/norm）を実行。共有cyclic関数は有理式の展開後に零を比較するよう正規化し、既存A/B検証も再実行済み。次は四単純基点1111の具体表示、または必要被覆定理の適用域を確認して低交換子H3候補を統合する。全H3被覆・抽象族降下・非捩れ量子so3残余は未完。


四単純基点FS4の全S(lambda,t)と標準Klein cocycleも排除した（classification-v73）。proper部分は既証Sklyaninへ帰着、三つの退化曲線はS(1,-1,s)の正規二次N1=a²+d²,N2=b²−c²の積が−Iを実現するため奇数centre0。FZ2のQ共有係数族は六対とも可逆skew係数なので既存skew分類に含まれる。表示のみ参照し全四単純基点/全CY被覆は未輸入。次は残るO/H共有零境界とfull-shared表示を調べる。

境界normalityはQQ(s)の三次関係moduleで八恒等式を証明し、係数分母はs,s±1のみ。最高反巡回tensor w=R A R^Tは非零かつKlein次数0なのでAS4実現の下で通常/標準cocycleともmu=id。全値AS4存在・平坦性をgeneric rrefから推論していない。原稿cubic_as4_four_simple_exclusions.tex、検証verify_cubic_as4_four_simple.py。任意境界Zhang twistと全H3被覆は未完。


共有頂点係数零の残余O/H表示も全排除した（classification-v74）。Oは四DiamondのPBWと正規a,bのcharacterにより中心三次がc³又はd³一本に限られる。正確な共鳴はlambda=-1/2,A²=-3/64でkc³、A²=-1/192でkd³、他0なので全切断分解。H0/H1は分母なし商座標と最大minor16384lambda^12(lambda+1)^9(2lambda+1)^4(4lambda+1)(4lambda+3)、三例外値のQQ rank20で全中心三次零。最高反巡回tensorからAS4仮定下mu=id。従ってFZ2/FZ4/FZ5/FS4列挙はskew部分だけが残る。全CY/四単純基点被覆は未輸入。次は共有頂点非零full-sharedの具体表示を調べる。
検証verify_cubic_as4_four_simple_remaining.py。AS4性を仮定して必要条件で排除しており、AS4十分性・全同型・full atlas coverageは輸入しない。中心rank coverは両generic投影の全関係消滅と自由列identityを確認し、分母1なので全特殊fiberへ適用できる。


十二共有非零P族のlambda=2切片を両符号・全r!=1,13/5で排除した（classification-v75）。三次/四次商座標分母はr−1のみ、中心行列の二つの最大minorの分子Q(deg3),P(deg5)がQQ(i)[r]で互いに素なので全閉値rank20。元の二パラメータFT3全域の最高反巡回tensorも256係数で独立検証し、AS4仮定下mu=id。全Pの非空determinant openでもH3なしだが、全lambdaの例外集合は未排除。次はP全二パラメータの残余か、共有零族の標準cocycle境界を調べる。
検算verify_cubic_as4_four_simple_p.pyは全二変数最高tensor、一変数の全関係消滅/自由列identityと分母のr−1支持、最大minor二本の厳密gcdを確認。今回python-flintで高速化して実行（数学的計算はSymPy有理関数体）。全P/全四単純基点/全CY被覆は新規輸入せず、FT3表示だけを参照。対角生成元変換だけではPの複素係数は消せない。二変数の無準備なGJ/FF消去を長時間反復せず、次は正規元・次数3 characterや全値minorの分母制御を優先する。


共有零O/Hの標準Klein cocycleも全排除した（classification-v76）。Oは(r,s)を(r,−s)へ替えた同じPBW、r,s!=0,+-1の二十characterから全中心三次が純三乗一本以下となる（rs=1を除外しない）。H0/H1のcocycleはgeneric rank20、lambda−1/2でrank20、lambda−1/4/−3/4ではrank19でそれぞれd(d²−3c²),c(d²−c²/3)の中心一本。全候補分解。最高tensorのtwist pairing A^c=A diag(1,1,−1,−1,1,1)を全係数で確認しAS4仮定下mu=id。これで列挙共有零表示と標準cocycleのH3はskewだけ。次はP全二パラメータ残余・他の共有非零支持、または非捩れ量子so3の許容性を進める。
検証verify_cubic_as4_four_simple_cocycles.py。通常Hとcocycle Hでgeneric最大minorは一致するが特殊値のkernelは異なるため、通常の全値rank20を流用しない。二例外のrank19と明示factored generatorを別計算済み。全CY/全四単純基点の被覆は未輸入、全intrinsic family降下等の大域未完部分も維持する。


最初の共有係数FN3の七列挙表示も全排除した（classification-v77）。L/MをB(1;h/4,0,f,0)へ統一し、四Diamond/Ore PBW、normal adのcharacterからh0,h²−1,h²−3だけへ絞る。h0ではbc−2f adが−Iを実現、他二共鳴では候補4/2本とaの交換子が単射なので全centre3零。F0/F1のgeneric最大minorはlambda^6(lambda−1)^(4+eps)(lambda+1)^(6+eps)(lambda²+1)^(2−eps)(lambda²−lambda+1)(lambda²+lambda+1)/2^(40+2eps)。商分母lambda,lambda±1,lambda²+1と全七例外値を合わせ、QQ/QQ(i)/QQ(sqrt−3)の独立rank20で全値centre3零。G0/G1/KもQQ rank20。全mu判定は最高反巡回tensorで独立。次は第五係数零のM_p二族と固定N/C、他の共有非零表示、P全二パラメータ残余を進める。
原稿cubic_as4_first_shared_exclusions.tex、検証verify_cubic_as4_four_simple_first.pyとfirst_remaining.py。fn_matrixは全入力をSymPy exactへ先に変換し、整数e/16のPython float化を避ける。L/M検証もこの修正後に再実行し、F0/F1全値rank coverと三固定表示を実行済み。FN3の具体七表示のみ参照し、上流全chart被覆・AS4存在十分性・全同型は輸入しない。全H3被覆、P全残余、非捩れqso3許容性、大域成分と抽象intrinsic族降下は未完。


第五係数零のM_p^0/M_p^1と固定N/Cも全排除した（classification-v78）。generic中心minorは(3p+1)/(2^33(p−1)^11)と(p+3)(3p+1)/(2^23(p−1)^13)、商分母p−1だけ。p−1/3とeps1のp−3をQQで別計算し全rank20。N/CはQQ(sqrt−3)/QQ(i)でrank20、係数共役も含む。全AS4実現のmu=idを最高反巡回tensorで独立確認。境界R±_1は未処理なので第五係数零全被覆とは呼ばない。次は第二共有の実係数二変数H_(lambda,p)を分母制御付きで調べ、R/J/T境界とP全残余を進める。
原稿cubic_as4_zero_fifth_exclusions.tex、検証verify_cubic_as4_four_simple_zero_fifth.pyを実行済み。上流FZ2/FZ3/FB2の表示だけを参照し、AS4存在十分性・全同型・全chart被覆は輸入しない。第二共有HのQQ(lambda,p)消去は疎な関係行列とDomainMatrix内の商射影で試し、一段ごとの出力と上限を設ける。重いGaussian二変数Pの無準備な消去とは分ける。全H3被覆・非捩れqso3許容性・大域成分・抽象intrinsic族降下は未完。


第二共有FO2の二パラメータH_(lambda,p)を全値排除した（classification-v79）。generic商分母lambda,lambda±1,p−1だけ、中心minor=lambda6(lambda−1)^4(lambda+1)^5 D1 D2/(2^40(p−1)^13)、D1=lambda²+(2lambda+1)p,D2=lambda²+lambda p+lambda+1。lambda1直線、D1/D2二曲線を全関係から別計算し、minor m0=(3p+1)/(2^33(p−1)^11),m1=−lambda7(lambda−1)^4(2lambda+1)^10/(2^40(lambda+1)^15),m2=−lambda17(lambda−1)^3/(2^37(lambda+1)^15)。最後(1,−1/3)をQQ rank20で排除。全中心3零、mu=idは全二変数最高tensorで独立確認。次は一般境界R_lambda、純虚J_h、隣接TとP全残余を進める。
原稿cubic_as4_second_shared_exclusions.tex、検証verify_cubic_as4_four_simple_second.pyを実行。疎なQQ(lambda,p)関係行列と係数体内のDomainMatrix商射影で全関係恒等式を保持。curveBの分数体detがSymPy HeuristicGCDFailedとなる場合は、行毎分母を払ったQQ[lambda]行列のdetと分母対角detの多項式交差積で厳密検証する。これは数学的例外でない。FO2具体表示のみを参照し、上流全chart/CY被覆・AS4十分性・全同型を輸入しない。未被覆のR/J/T/P、非捩れqso3許容性、大域成分・抽象intrinsic族降下は未完。


一般行列式零境界R_lambdaの全許容lambda・両符号も排除した（classification-v80）。右Zhang twist A=D^psi に同次数の非零中心元q1,q2（psi指標chi1,chi2）があれば、Z(D)_n!=0は(chi1/chi2)^n=1を必要とする。Rを固定可逆基底とtwistでFG6のA_tへ移し、非零中央a²,d²の指標−1,+1から全奇数中心を消す。六関係・基底det・最高tensorとQQ[t]上の八中央恒等式を独立確認し、lambda1/±iも含む。これで第五係数零の列挙M/N/CとR±_1は全排除。次は純虚J_h、隣接Tと追加二固定L、P全二パラメータ残余を進める。
原稿cubic_as4_boundary_R_exclusions.tex、検証verify_cubic_as4_four_simple_boundary_R.pyを実行済み。右規約 x*y=x psi^deg(x)(y) では At=(RのC基底)^(sigma^-1)、sigma=diag(i,−i,1,−1)。sourceの(1 tensor phi)関係表示をこの規約へ明示変換し、twistの向きを混同しない。中央二次a²/d²の恒等式はtを一切割らない。AS4の存在十分性・全同型・全CY被覆は未輸入。Zhang twistによる同値をintrinsic同型に置換せず、補助的な中心障害としてだけ使用する。全H3被覆・非捩れqso3許容性・大域成分・抽象族降下は未完。


純虚境界FI2のJ_h両符号を全値排除した（classification-v81）。全h!=0で商座標の分母はhのみ、中心20minorはeta+でi h9/2^11、eta−で(1−i)h10/2^7。両符号を別々に検証し、全hの最高反巡回tensorからAS4仮定下mu=idを確認した。h0はQQ(i)上の五次全関係行列rank966、dim58>56により独立にAS4から排除。
原稿cubic_as4_boundary_J_exclusions.tex、検証verify_cubic_as4_four_simple_boundary_J.pyを実行済み。lambda=iは固定して両etaを直接計算した。h0を一般商射影の極のまま捨てず、五次Hilbert障害で処理。FI2の具体表示だけを参照し、上流全chart/CY被覆・AS4存在十分性・全同型は輸入しない。次のAZ2二固定LはQQ(sqrt−3)でcentre3各dim1を計算確認したが、因子性・H3 admissibilityは未判定。T/P全残余、非捩れqso3許容性、大域成分・抽象族降下は未完。
