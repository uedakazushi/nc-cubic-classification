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


隣接AZ2の二固定Lも排除した（classification-v82）。centre3は各dim1で非零だが、B=S(a,b,d)[c;sigma]、sigma+³=omega I,sigma−³=omega² Iとなる。CYの自己同型Ore包絡でsigma³が非自明scalarのとき、中心三次は零、一次因子付き、又は純base cutの三場合となり全てH3を排除できる。三乗根の場合は純base切断R=(S/G)[c;sigma]の頂点P=pi k[c]が無限高次自己Extを持つ。
原稿cubic_as4_adjacent_L_exclusions.tex。一般cone補題はB=S[z;sigma] noethKoszulAS4、G∈S3 central regularで、Rees/local dualityから全line objectのPへのHom-acyclicityを得る。C=S/G上のkの最小解消を誘導しExt^n(P,P)=beta_n、1/H_C=(1-u)^2/(1+u+u²)が非多項式なのでbeta_n>0全n。未証明のOre open globaldimやGの因子性は用いない。有限入力はverify_cubic_as4_four_simple_adjacent_L.pyでOre輸送、base関係安定性、scalarcube、CY tensor、centre3 rank19と明示生成元を実行確認。因子探索は未決でもH3排除には不要となった。AZ2表示のみ参照、上流全chart/CY被覆・AS4十分性・全同型は輸入しない。次はT/P全残余、非捩れqso3許容性、大域成分・抽象族降下。


隣接AB3の全S_zetaとT_-2両符号を独立排除した（classification-v83）。Sの元の四次全語行列はQQ(zeta)上rank219、成分分母zetaのみなので全zeta!=0でdimB4>=37>35。T^eta_-2=S_(-eta i/4)は全六関係の文字どおりの一致で確認。一般商基底の特殊化ではなく、元の全語行列のrank上界を使用した。
原稿cubic_as4_adjacent_S_exclusions.tex、検証verify_cubic_as4_four_simple_adjacent_S.pyを実行。AB2/AB3具体表示のみ参照し、Tのlambda!=-2、全CY/chart被覆、AS4十分性・全同型は未輸入。TのQQ(i)(lambda)による無準備なcentral_data消去は600秒上限で未完（数学的結論なし）。同じ計算を反復しない。次はSingular 4.4.1等の厳密多項式module計算で商射影を生成し、char0で全関係消滅・自由列identity・分母支持を独立検証する。有限体は必要なら探索だけに使い、標数零の証明としない。P全残余、非捩れqso3許容性、大域成分・抽象族降下も未完。


## 隣接T全値の排除（classification-v86）

AB2のT_lambda両符号を全lambda!=0,-1で排除した。lambda=-2はS_zetaとの文字どおりの同一性とdim4>=37、lambda=-1±iは両符号の直接QQ(i)計算でcentre3 rank20。その他はAS4実現でdim3=20,dim4=35と最高反巡回tensorによるmu=idを必要条件として使う。T1での厳密rank20と一般presentation-rank二場合分けによる独立な有限性証明も原稿に保持する。全値AS4存在を仮定しない。

三次・四次商射影は元の全語関係消滅と自由列identityをQQ[lambda]の実部/虚部恒等式で独立再生した。D3=lambda²(lambda+1)²(lambda+2)²(lambda²+2lambda+2)E、E=lambda^4+2lambda³+10lambda²+24lambda+16。共通複素因子の除去後D4=lambda³(lambda+1)^5(lambda+2)³(lambda²+2lambda+2)AB、A=lambda²+(-1+3i)lambda−2+2i、B=lambda²+(1−3i)lambda−4i。AS4 Hilbert値の非極点でのみ商基底と結論し、全値平坦性は推論しない。P4分母を実normへ戻すと不要な共役極を増やすため、複素分母を維持する。

64本全三次語から作る64×140転置交換子行列の各列を、D4との共通因子h_jだけで割る。独立検証器はh_j|D4とC_0 X=NをQQ[lambda]の実部/虚部多項式行列で検証する。Nの20列は異なる先頭行を持つ三角形で、対角零点支持はlambda(lambda+1)(lambda+2)(lambda²+2lambda+2)AC_*、C_*=lambda²+(2−4i)lambda−4i。H=ABC_*とnum H(f(lambda))は互いに素、f=-lambda/(lambda+1)。literalなgraded同型P=diag(1,-1/q,-1/q²,-1/q)P_(bd),q=lambda+1、detP=q^-4、P(f)P=Iにより二枚で全残余を覆う。従ってcentre3は零。負符号は形式lambdaを固定した係数i共役で証明書全体を移す。20本の三次語が全特殊点で商基底になるとは仮定しない。

再生verify_cubic_as4_T_projections.py 3 4、verify_cubic_as4_T_centre_lift.py。入力generate_cubic_as4_T_centre_input.py、出力整形export_cubic_as4_T_centre_lift.py。商射影・centre liftのJSON証明データを保存し、証明再生はSymPyのみ、Singular 4.4.1は生成にのみ用いる。元のGaussian分数体消去と無縮約liftstdは設定上限で未完だったが、その結果は不使用。三角再帰の実部/虚部計算とprimitive列化に変更して成功した。GitHub正本から入力生成と証明の独立検証を再開できる。

これでAB2/AB3の隣接共有境界の列挙表示は全排除。次はFT3のP全二パラメータ残余。Pはlambda2の全rと非空開集合のみ排除済み。非捩れqso3許容性、全包絡被覆・大域成分・抽象族降下も未完であり、全H3完全分類とはしない。


## 十二共有P全二パラメータの排除（classification-v88）

FT2/FT3の全P_lambda,r両符号を排除した。全二変数商射影のD3=lambda^4(lambda+1)²(r−1)²、D4=lambda^7(lambda+1)³(r−1)³a、a=2lambda²+2lambda+1。全分母はFT2領域で非零。元の全語関係消滅と自由列identityはQQ[lambda,r]の実部/虚部でSymPyとFLINTの厳密多項式積により独立検証済み。AS4実現の商基底としてのみ用い、全値AS4存在を輸入しない。

20三次語の転置交換子行列からD4の約数の列因子を除き、40×280のrealificationを作る。独立検証した多項式AX=Nでは40三角pivotを持つ。r−1の因子を除く垂直例外の被約積g(lambda)は次数30、11既約因子であり、明示式は原稿とcubic_as4_P_full_certificate.json。通常stdの基底と係数追跡liftstdの基底の正規化は異なる。通常基底の対角がlambda,r−1のみでも追跡付き基底は余分なlambda因子を持つため、それを捨てずgへ全て含めた。この点を無検証で特殊化しない。

次数付き同型lambda'=-lambda−1, r'={a−(lambda+1)²r}/lambda², eta'=etaを全六関係で確認。生成元はdiag(1,−1/64,i lambda/[8(lambda+1)],−i(lambda+1)/(8lambda))P_(ab)、det=1/4096。FT2のd,e,f,r−1はそれぞれq²/lambda², q/lambda,−q²/lambda²,−q²/lambda²倍に移り領域を保つ。gcd(g(lambda),g(−lambda−1))はlambda(lambda+1)a(2lambda+1)(4lambda²+4lambda+5)の定数倍。従って元の領域では三直線lambda=−1/2,−1/2±iだけ残る。先に複素行列を特殊化してからrealifyしたQQ[r]上の三証明書を別々に作り、全r!=1で40三角pivotとAX=Nを独立検証した。両符号は形式変数を固定した係数共役で覆う。

再現verify_cubic_as4_P_projections.py 3 4、verify_cubic_as4_P_centre_lift.py。入力はgenerate_cubic_as4_P_centre_input.py。中心検証にはpython-flintを要し、再生成にはSingular 4.4.1互換CLIも要する。巨大な出力（一般lift約64MB）は作業領域のみとし、Gitには元の商データ、生成器、独立多項式再生器、係数gと全チェックのSHAを持つ小さい記録を保存する。生成時のSingular内A*X=Nだけで終わらず、元のP商座標から行列を組み直しFLINTのQQ[lambda,r]積で全残差零を確認した。単なる数値標本や有限体検査ではない。

生成法の要点：Gaussian分数体でなく各語実/虚を隣接させたQQ(lambda,r)消去で三次・四次商を取得。元のQQ(lambda)[r]関係module GBの未完計算を反復しない。証明データは単項式係数列として保持し、巨大式のSymPy再展開を避ける。局所化した三変数moduleによる別法は180秒で未完、結果不使用。

これで現在参照した四単純基点の共有係数境界の全列挙表示はPも含めて判定できたが、上流の全chart/CY被覆はまだ輸入していない。次はこの列挙と全H3包絡の関係を監査し、未被覆領域を特定する。非捩れqso3の正のadmissibility、全包絡被覆、大域成分・交叉、抽象族降下も引き続き未完。


## 零交換子CY skewと通常Qの排除（classification-v89）

四生成元CY skew多項式環で全q_ij!=1なら、中心三次は零か純三乗一本だけである。PBW重みにより中心は中心単項式の線型包。2+1型は平方変数との交換からq_ij1を強制し、1+1+1型はCY行積との比較で欠ける第四変数とのq1を強制する。二本の純三乗が中心なら全六対が三乗根となり、各行の三つの非自明三乗根指数が全て同符号となる必要と反対称性が矛盾する。よって全非零中心切断は純三乗でnondomain。

FZ2のQについてR=U+K diag(rho)、q=(2rho−1)/(2rho+1)を元の式から確認し、四つのCY行積−1の分子がAB+lambda AC−(lambda+1)BC−lambda(lambda+1)/16で割り切れることを厳密確認した。q−1=−2/(2rho+1)なのでc=0。従って通常Qも全排除。標準cocycle後にq1が生じる場合はこの補題を適用せず、既存skew分類へ戻す。原稿cubic_as4_four_simple_exclusions.tex、再現verify_cubic_as4_Q_centre_bound.py。

全零交換子CYの被覆監査はまだ別の課題。固定as4 a45f834f51a00c47443b51caf66abaf4629546b9のCY_COMPLETE、CI22_COMPLETE、IMAGE_REDUCTION、VERONESE_EXCLUSION、NONDEGENERATE_CHART、QUADRIC_PENCIL_PROJECTIONS、DEGENERATE_CHART_SECOND_QUADRICの論理を読み始めたが、これらの全必要被覆を新規輸入したとはしない。現在は階数六の二次関係を持つ六二次式系の退化微分像から第二二次関係を得るDC1–DC15の全枝を独立に検証し、CI(2,3)/CI(2,4)が消える幾何的核心を監査する。次いでVeronese除外、CI22七射影型と支持分岐の必要性だけを監査する。AS4十分性や全同型はH3排除のために輸入する必要がない。


## 全H3の二固有値中山：位数2/3への縮小（classification-v90）

既存の単一固有値フィルタを二固有値へ拡張した。H3包絡BのKoszul top wは任意の非自明なV=A⊕Cに対して純A四次と純C四次だけへ分離しない。Frobenius E2対合によりflattening像はR全体であり、もし分離すればR=R_A⊕R_C、Bは自由積となる。整域性からk[a]*k[c]が入り指数成長となってHilbert14641に反する。

二一般化固有空間の固有値alpha,betaに対し、mu_B(G)=Gからalpha^a beta^(3−a)=1、hdet(mu_B)=1と混合topからalpha^c beta^(4−c)=1、a0..3,c1..3。4a−3cの絶対値は1,2,3,5,6,9、1は二値が一致するので除外。粗い固有値集合はmu90内の非順序16組（位数2:1組、3:3組、5:4組、6:2組、9:6組）に限る。

位数5/6/9の12組ではalpha/betaの位数も5/6/9であり、topのA個数cとGのA個数aが各々一意となる。Rが二重斉次となり、Koszul Euler分母P(s,t)は全次数4以下・最高項s^c t^(4−c)。任意の正の再次数付けのHilbert極が4位なので、Pの(1,1)Taylor次数4未満は零、よってP=(1−s)^c(1−t)^(4−c)。一次係数からdimA=c,dimC=4−cを得る。

位数5は(a,c)=(1,3)/(2,1)、一次元側が正規一次元となりG=ell z²又はz²ellで分解。位数9は(0,3)/(3,1)で一次元側の純三乗。位数6はc2,a0/3で二生成元一二次関係の部分整域内の三次となり、全斉次二変数式の一次因子分解で排除。この二変数補題は可逆二次係数行列の等方方向からyx=qxy+kappa y²へ移し、yを逆にしたz=xy^-1でyz=(qz+kappa)yと書いて通常の一変数多項式の根へ還元する。Jordan q1も含む。

従って全H3の二固有値中山の半単純部分は位数2/3のみ、固有値集合は{1,−1}又はmu3の相異なる二元（三組）の計四組。Jordan単冪部分・各重複度・存在十分性・許容性を完成とはしない。三/四固有値の層も残る。証明はcubic_as4_reductions.texのthm:h3-two-eigenvalue-refined。verify_cubic_two_eigenvalue_filter.pyは有限整数演算16組と12排除の重み型、二変数因数分解式の三次までの普遍多項式恒等式を実行確認する。成長/Frobenius/二重Hilbertの議論は原稿の証明であり、有限列挙だけで証明したとしない。新規の全as4被覆は不要。


## 二固有値・位数3の構造帰着（classification-v91）

比の位数3では二次tensorの三つの一般化固有値が相異なり、Rは純A²/混合AC/純C²へ分解する。BはN²gradedとなり、Koszul topも一次元なので二重斉次。v90の二重Hilbert補題により、固有値集合{1,rho}は重複度1+3、{omega,omega²}は2+2となる。Gの固定重みは純三次の二成分だけ。

{1,rho}では固有値1の直線kzが正常化しmu_B(z)=z。混合三関係の両射影の核はaz又はzaという零因子になるため無く、B=S[z;sigma]、Sは三生成元noethquadraticKoszulAS3となる。AS3性は純S成分のKoszul解消と正常一次商のRees lemma。G=F+c z³、F!=0、sigma F=F、Fのnormalizerはmu_B^-1|S。c!=0ならsigma³=mu_B^-1|S。c0は後述の正規cone頂点障害で排除した。

{omega,omega²}ではG=F_A+F_C、両成分非零（片方だけなら二変数三次が分解）。二生成元一二次関係のdomainで、正常三次のnormalizerが唯一の固有値rho（原始三乗根）なら、その平面はq=rho^-1の量子平面、F=x²y、normalizer=rho Iに限る。可換型はnormalizerIdで不可能、Jordan型はF=p(z)y³とp(z)=rho p(z+1)の最高係数で不可能。量子型の単一固有値graded automorphismはスカラーであり、指標q^u=q^(u−3)=rhoからq³1,u1/2を得る。従ってこのH3候補ではmu_B自体がsemisimpleとなり、xy=omega yx,zt=omega²tz,G=x²y+z²tに規格化できる。

Frobenius対合により四次topのAA/CCブロック係数は非零。巡回式が混合flatteningのオフ対角を二つの可逆binary relation行列のKronecker積へ移すので、その4×4ブロックは可逆。混合rank4からR11のAC/CA両射影が同型、従って全体は標準単項式x^i y^j z^k t^lのPBW基底を持つ。残る混合四関係は可逆4×4twisting matrixで表せるが、全係数・H3 admissibilityは未解決。

原稿thm:h3-order3-two-blocks、検証verify_cubic_order3_two_eigenvalue_reduction.py。有限重み、Jordan最高係数、量子binary指標、混合ブロック行列式を実行確認。成長・Frobenius・AS3性・PBW比較は原稿の証明であり列挙だけで完成としない。2+2の最高tensorと混合係数の全判定は後述classification-v92で完了した。1+3の残るAS3/正常三次の分類、三固有値以上、零交換子CYの被覆監査、非捩れqso3許容性も残る。


## 二非自明三乗根固有値の全排除（classification-v92）

全H3で中山固有値集合{omega,omega²}は不可能と証明した。v91の2+2帰着から、xy=omega yx,zt=omega²tz,G=x²y+z²t、mu_Bはsemisimple、混合四関係はPBWgraph。最高tensorのAA/CC係数をr_A tensor r_Cへ規格化し、残る交互成分をAC=(xz,xt,yz,yt)順の対称4×4行列H（十係数h0..h9）で全表示した。

rank6のSchur16式、四Diamond（zyx,tyx,tzx,tzy）の24式、正規Gの32式から零・重複を除く68必要式Iを再生成。Singular4.4.1で発見した30式Gammaについて68×30の乗数Xを保存し、SymPyでI X=Gammaを元の係数から独立再生した（証明書約49KB、Singularなしでも再生可）。Gammaから(h5−omega²)(3h5−omega−2)=0を得る。

第一枝はh3=−omega²,h5=omega²以外零。skew係数(omega,omega,omega²,omega²,1,omega²)となり、既証skew H3必要リストの三乗根行が全てCYであることに反して排除。第二枝はp=h1,q=h2非零、h0=2(omega+2)pq,h3=−(2omega+1)/3,h4=(omega−1)p/(3q),h5=(omega+2)/3,h6=−omega/(3q),h7=(omega−1)q/(3p),h8=−omega/(3p),h9=(2omega+1)/(9pq)。元I/Gammaへの全逆代入を検証。u³=q/pを取りdiag(u,up,1,q)でG直線を保ってp=q1へ移るので、全域は一つの候補軌道。

標準候補ではtau³=omegaとして、tau G=(x+tau z)[tau xy+zt+tau²{omega²xz−(2omega+1)(xt+yz)/3−yt/3}]という非可換積恒等式をPBW全係数で独立検証。次数1/2の非零因子から商はnondomain、従って全枝でH3を排除する。候補自体のAS4十分性・noetherian存在は不要。

原稿thm:h3-order3-two-nontrivial-excluded、再現verify_cubic_order3_two_block_incidence.pyとcubic_order3_two_block_incidence_certificate.json。全H3二固有値の残る集合は{1,−1},{1,omega},{1,omega²}の三つ。位数3は正常一次元AS3 Ore表示の重複度1+3だけが残る。純base切断c0は次の正規cone障害で排除し、残る三次元AS3/正常三次を分類する。位数2Jordan/全admissibility、三種類以上の中山固有値、CY零交換子の必要被覆監査、非捩れqso3許容性、大域成分・相対降下は未完。


## 正規cone頂点障害と位数3 Ore切断（classification-v93）

既存のskew cone頂点補題を中心三次から正規三次へ拡張した。B=S[z;sigma]、G∈S3正規正則、Gz=zG、normalizer thetaがSを保ちzを固定する場合、M=k[z]はtheta-twistに不変。正規Rees lemmaのtwistはMを変えず、Ext_B(M,B)の次数3集中からExt_R(M,R)の次数2集中を得る。AS Gorenstein局所双対とsection比較、C=S/Gのkの最小自由解消のRへの誘導によりExt^n_qgr(P,P)=beta_n^C(k)。1/H_C=(1−u)^2/(1+u+u²)は多項式でないため全beta_n非零、H3のcohomological dimension2に反する。中心版の既存応用はtheta=idの特殊例として保持する。

従って{1,rho}の1+3 Ore型でG=F+c z³のc0は不可能。座標を規格化してG=F+z³、sigma F=F、Fのnormalizer=sigma³=mu_B^-1|S。さらに正規一次元zの商にRRZ1302.0437v2 Lemma1.5を適用してmu_S=mu_B|S sigma=sigma^-2を得る。一次資料のmu_B-normal仮定はmu_B(z)=zで満たす。これは必要帰着であり、Sの存在十分性や商のH3判定を結論しない。独立な大規模CAS計算は不要なホモロジー証明であり、新たな計算検証を実行済みとしない。次はsigma³に唯一の原始三乗根固有値を持つAS3とsigma-fixed正常三次Fの分類。三固有値以上の包絡・全許容性・相対分類も残る。


## 位数3 Ore型の三固有値base模型（classification-v94）

B=S[t;sigma], G=F+t³の帰着において、sigmaの単一固有値bは不可能。mu_S=sigma^-2のAS3最高tensorへの固有値b^-6=rho²!=1がhdet(mu_S)=1に反する（Jordanも含む）。三固有値ならsigmaはsemisimple、a³=rhoの原始九乗根aを使いsigma=diag(a8,a2,a5)、mu_S=diag(a2,a5,a8)。sigma固定最高tensorは三つのii(i+1)巡回orbitだけ。中山巡回係数を合わせた三係数A_iの一つが零なら前のAが非零である限り二次関係に純平方が出てnondomainとなるので、全A_i非零。指数行列det9の対角尺度変更で全て1へ規格化する。

得られるSの関係はxy+a²yx+a7z²、a4x²+yz+a5zy、ay²+zx+a8xz。全二/三/四次語の厳密商次元は6/10/15。sigma固定三次空間はy²z,yzy,zy²,z²xの四次元で、正常化a6Iの四次係数写像はrank3。従って唯一のF直線はF0=(-a4+a−2)y²z+(-a5+2a4−2a³+a−1)yzy+(a³−a+2)zy²+z²x。元の二次関係からSymPy QQ[a]/Phi9の厳密行消去、最高tensorの両slice一致、正常式全係数零、核rankをverify_cubic_order3_Ore_distinct.pyで再生した。小さいJSONに入力と出力を保持する。

これにより各rhoにつき三固有値sigmaのH3候補はS[t;sigma]/(F0+t³)一対象以下。Sの全次数AS3性、noetherian/domain、切断のH3許容性はまだ未証明。三次/四次Hilbert一致だけから十分性を言わない。原稿prop:h3-order3-Ore-distinct。sigma二固有値も次の議論で排除した。次はこの有限候補の許容性又は排除を判定する。全体のmu_B三固有値以上とは別のbase自己同型sigmaの固有値分類であり、両者を混同しない。


同命題でsigma二固有値も全排除した。比が原始三乗根なのでSは二重graded、hdet_S sigma=1からtopの型は2+1、正の再次数付けの三位Hilbert極から重複度も2+1。S=T[u;nu]、TはAS2整域。二次元側sigma_Uの固有値b、u上cについてb²c=1、b³=c³=rho^-1。固定三次はF=f2u。sigma_U(f2)=c^-1 f2とnu(f2)=rho f2、正規商公式mu_T=sigma_U^-2 nuからmu_T(f2)=c^-1 f2!=f2を得る。可換/Jordan平面はmu_Tが二次空間でunipotentなので不可能。量子平面なら単一固有値のsigma_Uはscalar、nuも対角で全Bがskewになるが、tx=bxtのbは原始九乗根となり既証skew37必要条件に反する。Jordan型を除外せずに含めた議論である。

hdet_S sigma=1は追加仮定ではない。BのKoszul双対の(3,0)と(0,1)のFrobenius積、mu_B(t)=t、hdet_B mu_B=1からhdet_S(mu_B|S)=1。sigma³=mu_B^-1|Sよりh³1、mu_S=sigma^-2とhdet mu_S=1よりh²1、従ってh1。この証明を構造帰着にも明記した。よって全二固有値・位数3 H3は有限の明示候補（各rho一つ以下）に縮小できた。単一固有値mu_B=1の単冪層、二固有値位数2、三/四固有値mu_Bを覆ったとはしない。


## 有限位数3候補の条件付き慣性とaffine表示（classification-v95）

候補がH3なら、mu_Bの固有空間から全graded自己同型はSとktを保ち、sigmaと可換するのでS上対角。関係から対角はd(1,r,r²), r³1、t上e。F0はd³r倍、t³はe³倍なのでG直線安定条件e³=d³r。grading scalarで割るとr=e³,e9=1、内在的慣性mu9（x,y,z,tに重み0,3,6,1）。二つのrhoは中山固有値集合が違い同値でない。従って二固有値・位数3の幾何学的群oidは二つのBmu9のうち許容されるものの非交和。これらは次の普遍Ore normで全排除されるため実在H3の慣性ではなく、表示候補の射影安定化群の計算として保持する。対角指標行列のSmith(1,1,9)と全関係/Gの重みを既存検証器で厳密確認した。

正規t開集合はD=S^(sigma^-1)、右twist積f*g=f sigma^-deg(f)(g)を使い、R[t^-1]0=D/(C+1)。Dの三関係はuv+a8vu+aw²、a7u²+vw+a²wv、a4v²+wu+a5uw、すなわちSのa->a4版。F0=c1y²z+c2yzy+c3zy²+z²xならC=a³c1v²w+c2vwv+a6c3wv²+a³w²u。F0のnormalizer=sigma³とsigma F0=F0からCは中心であり、三交換子をDの元関係の四次商で全係数零と検証した。ただしmu_D=sigma!=Idであり、CY用認識定理をこの表示へ適用しない。これも後の全排除候補の代数的な開集合表示であり、このaffineのglをH3分類の残課題とはしない。

古典型との同定：Le Bruyn–Smith–Van den Bergh, Central extensions of three dimensional Artin–Schelter regular algebras, Math.Z.222(1996), p.186のType E三関係をPDF画像で確認し、zeta9=a²、(X1,X2,X3)=(x,z,a³y)で三関係が(a r1,a r3,a7 r2)に一致することを元の係数から厳密検証した。AS3表示自体は古典的であり新規性を主張しない。全H3からの帰着と正常三次/候補許容性は別の課題。Type Eの中心・PI次数・局所orderの定理をこの式一致だけから輸入しない。恒久出典URL https://sites.math.washington.edu/~smith/Research/Central-extns.pdf 。

## 全二固有値・位数3領域の排除（classification-v96）

位数3の最後のType E候補にも明示的な普遍Ore norm因子が存在する。d=a5−a4−a²−2a,e=a5−a4+2a²+a,h=a5−a4+a³−a+1,k=a5+a、Q(U)=U²−(hd+k)U+h、X(U)=1−(d+e)U、W(U)=(a4+a)X+(a5−a³−a−1)U²と置く。QQ[a]/Phi9上でgcd(Q,X)=gcd(Q,W)=1。Q(u)=0,b³=X(u),c=u/bとするとell=x+by+czのnorm sigma²(ell)sigma(ell)ell=[bW(u)/X(u)]F0。この非零係数をlambdaと書き、s³lambda=−1,L=s ellとすればF0+t³=(t²+sigma²(L)t+sigma²(L)sigma(L))(t−L)。次数2/1の二因子は商で非零なのでnondomain。

元のS二次関係の全三次商で、c=U/bを代入しb³を掛け、b³=X(U),Q(U)=0により全10座標の残差零をSymPy厳密再生した。gcdも同じ数体のEuclid計算で確認。Singularが発見した二変数norm理想は最終証明の依存ではなく、公開検証器は補助二次方程式と全座標恒等式のみから再生する。AS3存在/PI/有限中心性/局所order/同型十分性を入力にしない。原稿thm:h3-order3-two-eigenvalues-excluded、verify_cubic_order3_Ore_distinct.py、同証明書のOre_norm_exclusion節。

これで全H3二固有値中山は{1,−1}だけに限る。二固有値位数3の幾何学的領域は空なので、候補に対して求めたmu9やaffine表示から実在成分を主張しない。次は位数2の全重複度/Jordan/正規三次の分類、又は中山三固有値以上を絞る。単一固有値1の単冪層、零交換子CY必要被覆、非捩れqso3正admissibility、全大域成分と相対降下も未完。

## 位数2の混合関係数と共通二平面（classification-v97）

全二固有値の残余muスペクトル{1,−1}で、Jordanを仮定せず、重複度(p,q)と混合二次関係次元rを絞った。E=B!の二次Frobenius対合は偶/奇に直交分解し、奇上の非対称性作用nuは固有値−1だけ。非退化双線型形式の非対称性det1からr偶数。一次元側があれば奇関係の両射影はdomainにより単射なのでr<=3。2+2では各射影の核が二次元なら2x2行列式の零からrank1関係＝零因子を生じるためr<=5。

等変Koszul分母はP=1−(p−q)t+(6−2r)t²−(p−q)t³+t4。traceはJordanがあっても各次数で絶対値<=dimB_nなのでP全根は単位円上。r0ではP/t²=(t+t^-1)²−(p−q)(t+t^-1)+4の判別式が負で不可能。従って3+1ならr2、trace分母(1−t)²(1+t²)、1+3ならr2、(1+t)²(1+t²)、2+2ならr2又は4、各(1+t²)²又は(1−t²)²。有限因数分解をverify_cubic_order2_mixed_rank.pyで厳密再生した。成長/対合/整域性の証明を有限検算で代替しない。

さらに一次元側をz、三次元側の固有値epsilonとすると、奇関係の両射影の二平面像は必ず一致する。四次topの奇flatteningはP M P^t（M可逆2x2）、Az/AzとzA/zAの対角ブロックはともにrank2で、先頭zの巡回からK=epsilon Hとなるので像U=W。この共通Wで奇関係はzw=f(w)z。Frobenius非対称性の固有値−1によりM非対称、f M f^t=epsilon Mの交代部分を取るとdet f=epsilon。muはWを保存する。単なる二つの異なる二平面間の部分写像へ広げて探索する必要はない。原稿prop:h3-order2-mixed-rank。

次はこの二平面W・z・残り一次元に関する偶四関係と正常三次を扱う。2+2の混合r2/4、全許容性、mu単一固有値1と三/四固有値層も残る。

## 位数2の隣接非退化二次と二生成元部分代数（classification-v98）

3+1/1+3の共通二平面Wと単一生成元zに対して、四次topのzz行はq0(W)+gamma z²という実際の二次関係を与え、q0の2x2係数行列は可逆である。これは奇flatteningの非対角ブロックがrank2で両像Wに入り、巡回に出るmuもWを保存するため。純z4巡回式gamma=−mu(z)gammaから、三次元側が負（mu(z)=+1）ならgamma0に限る。

gamma0ならWの生成するTは一本の非退化二次関係を持つ量子/Jordan平面そのもの。高次追加核はあり得ず、任意の非零斉次式が一次式の積へ分解するという二生成元平面の普遍因数分解とBのdomainがそれを排除する。この因数分解補題の証明は最初から全次数dの式を示していたため、本文の主張も全正次数へ整合させた（検証器の低次数恒等式を全次数の計算検証と呼ばない）。

gamma非零ならq0(W)=−gamma z²はT内の非零正規正則二次で、q0 w=f²(w)q0、f(q0)=q0。fはT上の自己同型：z h(W)=f(h)zとzの正則性からf,f^-1が全関係を保存する。この場合TのAS3性や関係が二つの正常化三次で尽きることは未証明。Tは普遍二生成元三次表示（q0 w−f²(w)q0）からの商である、という必要条件だけを用いる。原稿cor:h3-order2-plane-quadric。新規CAS実行を主張しないホモロジー/tensor/整域性の証明。

次の具体的着手：三次元側が負の全gamma0を量子/Jordan平面の自動同型f（det−1）で分け、残り一次元との偶四関係とW1を求める。三次元側が正のgamma非零は正規二次を持つ二生成元三次表示と比較する。部分代数がOre AS3であることやAS4十分性を先に仮定しない。2+2の混合rank2/4、mu固有値三種類以上も別に残る。

## 共通二平面の二行列標準形（classification-v99）

混合関係の基底r_i=z w_i−f(w_i)zで奇flattening=P M P^t、P=(-F;I)と書く。先頭zとWの巡回式を別々に使うとFMF^t=epsilon M、mu_W=−epsilon M^tM^-1、二次q0の係数行列は非零尺度を除きQ=MF^tとなる。これはdet Fだけより強い制約。mu_Wの唯一の固有値epsilonからM^tM^-1の特性式(X+1)²、すなわち対称部分rank<=1を得る。交代部分は非零なので、基底/尺度でM0=J又はM1=J+diag(1,0)の二型。

M0ではmu_W=epsilon I、F任意det F=epsilon。M1ではmu_W=epsilon[[1,2],[0,1]]、F=[[alpha,beta],[0,alpha]],alpha²epsilon、Q=[[alpha+beta,alpha],[-alpha,0]]。全型でmu_WとFは可換、FQF^t=epsilon Q。gamma0の実際の量子/Jordan平面T_Wの中山作用はmu_TW=mu_W f²。gamma非零の部分代数をAS2と誤認しない。残り三次元ブロックの第三生成元へのJordan拡大や偶関係・正常三次は未分類。

数体不要のSymPy厳密恒等式verify_cubic_order2_plane_matrices.pyで一般J相似式、対称部分detとtraceの同値、alpha=+-1,+-iの全beta式、mu_TW式を再生した。既知Clifford swapはu=x−y,w=z+h(x+y)/2,s=tで、正固有直線ku、W=<s,w>、us=−su,uw=wu,sw=−wsを元の六関係の線型結合として確認。従ってepsilon−、M0、F=diag(−1,1)、量子q−1であり、既知正例を排除していない。新たな一般FのH3許容性をこの照合から推論しない。原稿prop:h3-order2-plane-matrices。

次は三次元側が負、M0でFの共役標準形を取り、既知Clifford F=diag(−1,1)以外の全係数を正常三次incidenceで判定する。M1および残り生成元のJordan拡大も漏らさない。普遍三次元部分代数のAS正則性や偶関係のPBWを未証明のまま仮定しない。

## 負三次元側の非分裂Jordanは量子平面商を持つ（classification-v100）

重複度(1,3)、共通Wを持つ負空間A、正直線kzで、U=−mu|AのWへの拡大が非分裂とする。D=log Uの標準形はDv=w1,DW0又はDv=w2,Dw2=w1,Dw1=0の二つ。D不変四次tensorにv3W/v4項が無いことを、二次元+自明/三次元sl2加群のraising weightで証明し、別に81次元tensor空間上の18有理行恒等式（49非零乗数）を公開再生器で独立確認した。発見時のnullspaceそのものを信頼する必要はなく、証明書に各禁制座標=e_wordがDの行空間に入る乗数を保持する。

奇関係の像Wと巡回性から、四次topでzを含む項はW²z²だけ。負側gamma0とv3/v4消滅によりzz列はq0(W)、vv列もW²関係。domainによりR2∩W²は一本以下なので両列比例、B/(W)の二次関係はz²,v²間の一本。片方の係数が零なら平方一つを禁じる二文字語のFibonacci指数成長がBの多項式成長に反する。従ってB/(W)=k<z,v>/(v²+lambda z²),lambda!=0、基底変更でq−1量子平面。原稿prop:h3-order2-nonsplit-plane-quotient。

これはdouble Ore表示や全PBWの十分条件ではない。残る二つのcross偶関係がWv/vWのgraphをなすことは別に判定すべきであり、q0(W)+ell(W)vのような混合base項を無視してprojection単射をdomainだけから主張しない。次は外側二次が一本のこのchartでcross射影のrank2通常部分とrank1退化部分を分け、全偶係数・W1を計算する。既知正例のClifford swapはWへの拡大が分裂しており、この非分裂結論の対象と混同しない。

## 単項Ore一パラメータ族の全W1と排除（classification-v101）

共通平面第一型の具体族B_aをux=a xu,wx=a xw,uw=−wu,yx=−a^-2xy,yu=−a wy,yw=−a uyで定義（a!=0）。量子三平面T3[x,u,w]の自動同型Ore拡大で全aにAS4。一次資料Liu–Wang–Wu1205.0893v1 Theorem3.3を再確認：mu_B|T= sigma^-1 mu_T。mu_T=(a^-2x,−au,−aw)、よってmu_B=(-x,w,u,−y)。y成分の符号はy次数トーラスとhdet mu1、三平面topの指標−1から決定し、Theorem3.3だけから未記載のhdet公式を推測していない。

PBW x^i u^j w^k y^lでGx=−xGの指標は(−1)^l a^(j+k−2l)=−1。恒等的に許される三次はu²y,uwy,w²yだけで、他の列を許すaの位数は1,2,3,4,6,8（合計12根）。集合外ではGu=wGの三係数が−a−1/−a+1となってW1零。全六円分体で140x20行列を元のPBW積から厳密再生成し、a1はkuwy、a−1はk(w²−u²)y、他の位数は核零。両非零核もyを因子に持ち全切断nondomain。従ってこの全一パラメータ族を排除した。検証verify_cubic_order2_trimmed_Ore.pyは一般QQ(a)核、全例外核、64生成元三重積の整合、三平面top指標も厳密再生する。

正固有生成元はu+w、W=<x,y>、f=diag(a,−a^-1)、量子平面q=−a²。これは指定した単項/trimmed部分の一具体族であり、全trimmed double Oreやbase二次項・cross導分付きの表示を被覆したとしない。既知Clifford正例はこの族ではなく、除外と矛盾しない。原稿thm:h3-order2-monomial-Ore-excluded。次は係数付き外側二次/cross偶関係の残余、第二行列型と残るJordan拡大、2+2層を扱う。

## 単項Ore族の全base二次変形の排除（classification-v102）

前族のuw+wuをP=A x²+Cxy+B y²へ置き換え、他五関係を保つ全表示もH3から排除した。domainならx,y量子平面は忠実（高次核は一次因子分解で零因子）なので、P x=a²xP、P y=a^-2 yPから(a²−1)A=(a²−1)B=0,(a4+1)C=0。非零Pはa=+-1の平方和、又は原始八乗根のCxyだけ。全係数で四つの二次Diamondを多項式恒等式として確認し、PBW・重み(x,y)1,(u,w)2のgr=B_aを得た。

H3を仮定する場合のmuは変形前の(-x,-y,w,u)のまま。本文では各chartの最高tensorを全係数で直接保存・検証して決定する。符号二chart各32項、八乗根chart26項の計90項はパラメータ多項式で、全三隣接位置の関係商射影零、w_yxwu=1、指定muの巡回式を満たす。従って全特殊値で非零、AS4最高空間の一次元性からmuを確定する。cubic_order2_Ore_base_top_certificate.jsonを独立再生し、一般のNakayama変形不変性を仮定しない。代替説明として、二次双対の逆重みfiltrationと両Hilbert(1+t)4からgrE=E(B_a)、Frobenius対合からgr mu=mu_Baを得て、base符号反転とmuの可換性で低重み補正を除くこともできる。主証明は保存した直接tensor恒等式で完結する。

a1ではGx=−xGがy奇数を強制し全Gがy因子。a−1ではx次数偶数、y偶奇にGを分解。p=u+w,v=u−w,X=x²,Y=y²を取るとX,Y中心、p²−v²=2(AX+BY)、s=pv+vp=2(u²−w²)はC=<p,v,X,Y>の中心。y偶数部G_evenはCに入りsと可換するが、正常化mu(s)=−sから反交換もするので、domain/char0によりG_even0。全Gはy奇数でy因子を持ち非整域。

八乗根CxyではPBW基底上のW1行列はC多項式、C0でrank20、全C非零がu,w同時尺度変更の一軌道なので全値W1零。PBW全族が確認されているため、局所化や特殊化の根拠無しに一般点計算を全値へ広げた議論ではない。verify_cubic_order2_Ore_base_deformations.pyは全正常化条件gcd、任意A,B/CのDiamond、sの四交換子、八乗根基準核を再生する。原稿thm:h3-order2-Ore-base-deformations。全cross導分やbase--outer線型係数の被覆は残る。

## 共鳴cross導分と四パラメータ実AS4候補族（classification-v103）

T_a=(xy+a²yx)、nu=(a x,a^-1 y)の次数1skew derivationはa!=−1なら全て内部。a−1ではmod内部にdelta(x)=y²とdelta(y)=x²の二本だけ。係数比較は本文lem:h3-order2-skew-derivation-resonanceの四式、内部二列の各gcdは1。これは全cross表示の被覆ではなく、指定した対角normalizing chartの導分の完全判定。

共鳴でB_(alpha,beta,gamma,delta)=(xy+yx,px+xp,py−yp,vx+xv−alpha y²,vy+yv−beta x²,v²−p²−gamma x²−delta y²)を得る。全四パラメータでnoetherian quadratic Koszul AS4整域。u=(p+v)/2,w=(p−v)/2のPBWと重み(1,1,2,2)grが前a−1単項Oreなのでnoetherian/domain。54項polynomial最高tensorの三隣接関係射影零、固定係数w_yxwu1、flatteningrank4,6,4を有理定数pivotだけで全値再生しFrobenius/AS4とmu=(-x,-y,p,-v)を確定した。

140x20正常化行列も全係数で有理定数だけの19pivot消去があり、全値W1はG=beta x²p−y(pv+vp)の一本。Gのyu²係数−2は全値非零で、Bdomainより正常正則。R=B/GはASGor3index1、mu_Rid。beta0はGのy因子で非整域。beta!=0のdomainは未判定のままだが、H3は次節で全排除した。verify_cubic_order2_resonant_family.pyと54項cubic_order2_resonant_top_certificate.jsonがPBW・最高pairing・中山・全W1rankを独立再生。原稿thm:h3-order2-resonant-family。これは新たな候補族であり、新規性やH3実在は未確認。

参照用のdomain/Y開集合の着想（H3は後述の固定P開集合で排除済みなので分類上の次課題ではない。以下のY開集合/domain論は未検証で定理に使用しない）：X=x²,Y=y²,P=p²,s=pv+vpについてX,Y,P,s²がB中心で、G²=beta²X²P−Ys²と予想。Bがk[X,Y,P,s²]上32自由であればbeta!=0でG modYが正則、よってY正則R。Y開集合の次数零環はk[z,r]上二生成元Clifford、a²=−z、b²=beta²z²/4−r²−gamma z−delta、ab+ba=−alphaを予想（z=X/Y,r=py/Y,b=v y^-1−beta z/2）。これを元の関係から全係数で確認し、quaternion residueでdomain、centre cubic scroll F1とbranch cubic+fiberで全H3許容性へ進む。

参照用の中心像（次節でh,sの中心性とscroll関係は厳密確認済み。ここに残すvolume/ramification全体像は定理に使用しない）：Rでh=pyとsが中心となり、h²=PY,Ys=betaXh,hs=betaXPのcubic scrollを張る。負Cliffordvolume g=xyv+(alpha/2)y³−(beta/2)x³も中心でg²=(alpha²/4)Y³+(beta²/4)X³−XY(P+gammaX+deltaY)を予想。scrollにおけるramificationはplane cubicのpullback Eと一本のfiber、E affineはz r²−beta²z³/4+gamma z²+delta z−alpha²/4=0。alpha,beta非零でE smoothならH3の可能性があるが、最大order性・全局所global dimension・忠実rank・AZ認識を未証明のまま結論しない。

## 共鳴四パラメータ族の固定点無限Extによる全排除（classification-v104）

beta0は因子で排除、beta非零も全値H3でないことを確定した。B内でX=x²,Y=y²,P=p²中心、h=py,s=pv+vpについて[h,v]=−G,[s,y]=2G、他の必要交換子零。従ってRではX,Y,P,h,s中心、h²=PY,Ys=betaXh,hs=betaXP。全平方/反交換子がこの中心環に入るのでRは16本のsquare-free語で中心C上有限。R^(2)のSerre表示によりqgrRをProjC上coherent代数として扱える。

P開集合の次数零環はS=k[r,t]上rank4Clifford A：r=yp^-1=h/P,t=s/P,a=xp^-1,b=vp^-1−t/2、a²=−rt/beta,b²=H=t²/4−1−(gamma/beta)rt−delta r²、ab+ba=−alpha r²。逆にA[p,+-1;tau]、tau(a,b)=(-a,-b)でx=ap,y=rp,v=(b+t/2)pを代入し元六関係とG0、順逆生成元対応を再生するので局所環との正確な同型。r=t0の中心点は全パラメータで存在しH−1が単元。

完備局所Sでb0=b/sqrtH,a0=a+alpha r² b/(2H)とするとb0²1,b0a0=−a0b0,a0²=f=−rt/beta−alpha²r4/(4H)∈(r,t)²。ゆえにAhat=(k[[r,t,a0]]/(a0²−f))#mu2。可換環はdim2,embdim3で非正則。剰余体は無限pd、誘導M=k[mu2]も制限でk二本となるので無限pd。完備半局所代数の最小解消でExt^n(M,M)が無限高次非零。Mはchartのa=r=t0,b²−1という二単純点から来る。有限中心coherent代数の点支持Extは局所化/完備化と可換、local-to-globalは点支持で退化するのでqgrRでも無限ExtとなりH3hd2に反する。

verify_cubic_order2_resonant_obstruction.pyは全中心交換子・scroll関係・G²式、順逆chart六関係とG、完備化の平方完成とfの一次項零を厳密再生。無限pd/Extと点支持比較は本文のホモロジー証明であり、計算だけが全証明としない。原稿thm:h3-order2-resonant-excluded。局所orderの最大性や全中心被覆の未証明仮定を用いない。beta非零でのRdomainの独立判定やaffineYchartが良いかどうかを待たず、固定点一つで全H3を排除した。

次は第一行列型の残るbase--outer線型項とcross正規化chart（量子/Jordan/反対角を区別）、第二行列型および非分裂Jordanのcross射影退化部分。2+2や中山三/四固有値、全CY必要被覆、非捩れqso3正admissibility、全大域成分/相対降下も残る。

## 対角normalizing chart全cross係数の排除（classification-v105）

全六関係をT_a=(xy+a²yx)、p x=a xp,p y=−a^-1yp、v x=a xv+d_x,v y=a^-1yv+d_y、v²−p²=ell(W)v+q2(W)と書けるH3は存在しない。d_x,d_y,q2任意二次、ell任意一次を含む。H3domainからT_a忠実、dはnu-skew derivation。u=(p+v)/2,w=(p−v)/2で全語のordered monomial spanを得て、14641 Hilbert値との比較でPBWになるからT+Tvの係数比較が正当。

vを一次式だけずらして、a!=−1ではd0、a−1ではd(x)=alpha y²,d(y)=beta x²。後者はd nu+nu d0,d²0なので全aで(v²−p²)t=nu²(t)(v²−p²)。外側関係のv係数比較によりell t=nu(t)ell、内部derivation d_ell0。前補題の内部写像は全aで単射だからell0。残りq2はnu²正常化、a!=−1は全base二次変形の既排除族、a−1は四パラメータ共鳴の既排除族。vの対角係数を双方逆符号にしたchartもW交換とa->−a^-1で同じ結論。

新たなCASを仮装しない構造的な帰着。dの分類/gcdはv103、一般base変形はv102、共鳴全値はv104の再生器と証明へ依存する。原稿thm:h3-order2-diagonal-normalizing-chart。反対角normalizer、非対角f/Jordan平面、cross射影がgraphでない退化部分、外側二乗投影rank2の既知Clifford正例はこの定理の被覆ではない。次はこれらを区別して扱う。

## 反対角involution normalizing chartの全排除（classification-v106）

T=(xy=-yx)、p x=-xp,p y=yp、v x=lambda yv+d_x,v y=eta xv+d_y、v²−p²=ell v+q2の全六関係を持つH3は存在しない。HFB4のordered monomial比較でPBW、外側最高項の比較でnu²id⇒lambda eta1。対角base尺度でnuがx,y交換に正規化される。skew derivationの六係数にはd0+e0=d2+e2=d1−e1=0の三条件、内部二列独立なのでmod内部はd(x)=d(y)=kappa xyの一本。d²0、d nu+nu d0からell0（内部写像単射）、q2=Cx²+Dy²。

この三パラメータ表示の74項多項式最高tensorは全隣接関係に入り、固定係数w_yxwu1、mu=(-x,-y,p,-v)の巡回式を全値で満たす。AS4なら実際のmuを決定する。140x20正常化行列は定数pivot20段、全パラメータで核零。verify_cubic_order2_antidiagonal_chart.pyが全PBW、tensor/flattening4,6,4、導分、全正常化rank20を独立再生。三パラメータ分母は一切ない。原稿thm:h3-order2-antidiagonal-normalizing-chart。

次の統合：残るnormalizing chartではnu²=f²、hdet_T f=−1。nu=+-fのtrim先頭環は二段Ore（又はinvolution Zhang twist）となりmuの正固有値が二本出て重複度(1,3)に合わない可能性がある。このスペクトルのfiltered保存と二次元平方根分類を証明してから、対角・反対角排除と統合する。cross射影がgraphでない退化部分や外側二乗rank2のClifford正例は未被覆として保持する。

## 負三次元側の可逆normalizing chart全体の排除（classification-v107）

重複度(1,3)、共通AS2平面T=<W>、pの作用fに加え、残り負生成元vがTを可逆nuと二次skew derivationでnormalizingし、外側がv²−p²=ell v+q2となるchartは全排除した。Jordanを零と仮定しない。PBW比較からnu∈AutT、nu²=f²。共通平面の行列式/中山式によりdet f=hdet_T f=−1、mu_T=mu_W f²。

二次元平方根分類：f非自明Jordanならnu=+-f。fscalar+-iならTはcomm/Jordan、Jordanではnu=+-f、commでは更にdiag(i,−i)があり既排除対角chart。f相異なる二値なら第一M=J型、fdiag(a,−a^-1)、T量子q−a²。量子自己同型の対角/反対角分類とnu²=f²からnu=+-f、既排除対角normalizer、q−1の既排除反対角involutionの三場合だけ。第二M1型もscalar/Jordanなのでnu=+-fへ入る。

nu=fのtrim先頭環は二段Ore T[u;f][w;sigma],sigma|T=f,sigma u=−u。hdet f−1とRRZ hdet(mu)1/LWW制限公式からmu|W=mu_T f^-2=mu_W（負二値）、mu u=mu w=+1。nu−fならu,w交換Hの右Zhangtwistが同じ二段Oreに移り、Hhdet1,H²1,index4なのでmu一次作用不変。どちらも先頭中山の重複度2+2。実際のmuはW保存、p固定、v->−v+Wなので重みW1,p/v2を保存する。実際の最高tensorの先頭項はAS4先頭環の一次元W4を張り、その巡回式からgr mu=mu_grB。よって実際の重複度1+3に反して排除される。この先頭tensor比較は未証明の一般Nakayama変形不変性を仮定しない。

原稿thm:h3-order2-full-normalizing-chart。対角/反対角の全係数排除はv105/v106の既実行検証に依存し、平方根/先頭スペクトル統合は本文の構造証明、新規CAS実行を主張しない。外側二乗rank1でcrossの両射影がgraph同型となる通常領域が消え、非分裂Jordanのv100量子平面商領域も、残りcross射影が退化する場合へ縮小する。既知Clifford正例の外側二乗rank2は被覆していない。次はこのrank1射影退化とrank2外側領域を分けて全関係・W1・許容性を判定する。

## 全負三次元側は二平方商を持ちJordan拡大は分裂（classification-v108）

重複度(1,3)のH3包絡の全域でB/(W)=k<p,v>/(p²,v²)を確定し、負三次元中山加群のWへの拡大も分裂と証明した。従ってmu負側はsemisimple又はW上Jordan2+残り固有直線の2+1だけで、非分裂/Jordan3が全て消えた。普通のcross graphだけでなく射影が退化する場合も扱った全域必要条件である。

核心はp²とvが共通AS2平面Tのgraded商体へ入ることの排除。commTならf²=mu_W^-1は非恒等だが内作用は恒等。JordanTならhdet f−1からf²(y)=−y、p²=r(z)y²,z=xy^-1の正常化がr(z)=−r(z+1)を要求しrational最高項で不可能。量子Tではdet f=hdet f−1がq−1反対角を排除し、mu_W−Iからfdiag(a,−a^-1),a²−q。q無限位数ならr(q^-1z)=−q r(z)、零極の有限性でr単項式、q^(m+1)=−1が矛盾。q有限位数ならf有限、D=Q(T)は二変数中心不変体F上有限次元。v∈D,p²∈DならB⊂D+DpがF上有限次元、有限構造定数を含む可換係数環で語の成長を抑えるとGKdimB<=2となり4に反する。Weyl商体一般のGK次元へ誤って適用せず、有限中心量子の場合だけこの成長比較を使う。原稿lem:h3-order2-rational-collapse。

偶四関係をW0へ射影すると像はp²,v²の空間。rank0/片平方rank1は指数成長。両平方rank1ならkernelをkq0で割ったcross二次元空間の両射影がfullならv107全normalizing排除、どちらか退化ならv ell=q(W)又はell v=q(W)からvがT商体に入り、外側平方関係からp²も商体に入って上補題に反する。従ってrank2に限る。v100非分裂なら商が量子平面であることとHilbertが異なるため分裂も従う。原稿thm:h3-order2-two-square-quotient。

verify_cubic_order2_outer_square_reduction.pyは量子中山・反対角hdetの行列恒等式と、既知Clifford swapをW0にした二平方係数minor=h(8−h³)/8を厳密確認。商体のrational不可能性、有限中心成長、全projection帰着は原稿の証明であり有限標本で証明したとしない。

次の焦点：残るrank2平方領域ではeven relations kernelがq0とcross一本になり、p²,v²をそれぞれW²+vW+Wvで表せる。下記によりsplit M1も排除済みなので、半単純muの全Koszul/normalG条件から既知Clifford族への被覆又は新しい許容族を調べる。p²の中心性や負三生成元部分代数のAS3性はまだ未証明なので先に仮定しない。正三次元側、2+2、中山三/四固有値、全CY被覆・非捩れqso3正許容性、全成分/相対降下も未完。

## 負三次元側の全Jordan型を排除（classification-v109）

v108で残ったsplit M1も排除し、重複度(1,3)の全H3包絡でmu半単純と証明した。新たなAS4 atlasや有限標本に依存しない。原稿thm:h3-order2-negative-three-semisimple。

分裂基底ではD=log(mu_unipotent)の尺度を取りDy=x,Dx=Dp=Dv=0、平面yx=xy+kappa x²、px=a xp,a²−1。平方投影kernelのcross一本はD不変なので両射影がkxに入り、vx=c xv+d x²,c非零。射影の片方零はv,p²が平面商体に入りv108で既排除。従ってxは全Bの正規一次元となる。偶B2の基底x²,xy,y²,xv,yv,vyでD核はx²,xv,Z=vy−c yv−d xyの三次元。p²=Cx²+MZ+Nxvとpxの平方からp²x=−xp²、Zx=c xZ−kappa c d x³を比べ、(1+c)M=(1+c)N=0,2C+Nd−kappa c d M=0。c≠−1ならp²0なのでc−1。v->v−dx/2でd0にできる。

するとxv,Zはxと反可換するがv²はxと可換し、v²もD不変なのでv²=Cprime x²。s²=−Cprimeを取れば非零一次元v+sxの平方が零となって整域性に反する。kappa0（共通平面可換）も含む。verify_cubic_order2_split_jordan.pyは全導分核係数とZ/平方の恒等式をQ[c,d,kappa]上で再生しPASS、標本検査ではない。全域帰着・一次独立・整域矛盾は本文で証明。

次の具体的着手：半単純M=Jでfに制約det f−1、mu_T=−f²があり、量子平面の対角f（q−a²）又はq−1での反対角fを調べる。ただし後者はdet/hdet条件で既に消える。量子q1はcommutativeでf²−I、Jordan平面でもmu_W−Iとmu_T=−f²を満たすfが存在し得るため除外せず、rank2平方とcross一本・正常三次の全整合を調べる。既知Cliffordのq−1,fdiag(−1,1)を正例として保持する。p²中心性・負三生成元部分AS3は依然仮定しない。

## 標準二周期点対とH3のExt必要条件（classification-v110）

重複度(1,3)の全域で、全G∈W1(B)が(W)に入ることを証明。商A=k<p,v>/(p²,v²)でmu固定三次はvpvのみだが[vpv,p]=vpvp−pvpvは非零、正常化式Gp=pGから商像零。従ってR/(W)=A。z=pv+vpは中央正則、Aはk[z]上1,p,v,pvで自由。u=p+vはu²=z、A[u^-1]の次数零部分D=k[a]/(a²−1),a=(p−v)u^-1。uが二原始冪等元を交換するのでqgrA=mod(k×k)でシフトは二つの点P0,P1を交換する。点対はWから標準的でintrinsic pointed同型に自然。商からqgrRへの制限はHom完全忠実かつ完全だが高次Ext同一とは主張しない。原稿prop:h3-order2-canonical-two-cycle。

H3のS=(-1)[2]からExt^r(Pi,Pj)=Ext^(2−r)(Pj,P_(i+1))*。Homは単位行列、Ext2は交換行列、Ext1は四成分全て同じ整数n>=0、Eulerは全成分1−n、高次Ext0。原稿cor:h3-order2-cycle-ext。この必要条件だけでn1や局所H3十分性を主張しない。verify_cubic_order2_boundary_cycle.pyは忠実行列p=sE12,v=sE21、中央自由基底det−s4、次数零冪等元、シフト交換と正常三次の商消滅を厳密検算、PASS。圏同値とSerre/Extは本文構造証明。

次の焦点：半単純rank2のcross一本と二平方の全係数を、この二周期点対上の自己/交差Extと対照する。W一次近傍でGが消える場合の障害は有力だが、非可換Jacobian判定、n=1、負三生成元部分代数のAS3性、p²中心性はいずれも未証明。先に仮定して全被覆を縮めてはいけない。全係数の形式的近傍又は小次数Koszul計算で必要条件を得て、既知Clifford正例と照合する。

## 正規な共通量子座標を持つ領域のパラメータ（classification-v111）

追加仮定：共通平面T=(xy=qyx),q非1の量子座標xが全Bで正規。このときq=-1,f²1を証明。全域の座標正規性・q=-1十分性は未証明のまま保持する。原稿thm:h3-order2-normal-quantum-axis。

正規化theta_xはW上(1,q^-1)、p上a,a²−q、残りv上c v+d x+e y。thetaの単冪対数DはW,pを殺しDv=ell∈W。v²のrank2平方表示にD²を作用させると右辺0、左辺2ell²なのでell0。従ってthetaは半単純でvをWだけ移動しvx=c xvとできる。偶B2基底x²,xy,y²,xv,yv,vyのtheta重み1,q^-1,q^-2,c,cq^-1,cq^-1、p²重み−q,v²重みc²。q非−1ならf|T2固有値−q,−1,−q^-1に1が無いのでp²∉T2。ゆえにv成分の重みからc=-q又は-q²。v²の重み条件とのresultantは(q−1)^6(q+1)^6(q²+1)^4(q²−q+1)^2(q²+q+1)^2*Phi5(q)となり、残るqは原始3,4,5,6乗根のみ。

全八行のsupportは原稿とJSONに固定。位数5/6のc=-qはv²0。位数3/4のc=-qはp²=xL,Lにv係数非零なのでpp²=p²pから新しいpv/vp奇二次関係が出て関係数に反する。位数4のc1はvx=xv,v²∈span(x²,xv)で可換二次式が一次分解。位数5のc=-q²はv²=Axy非零からcvy=yvという独立な追加二次関係が出る。位数3/6のc=-q²はp²∈U2、U=<y,v>がv²係数非零の唯一の非退化二次関係を持つ真正AS2平面となり、yは非正規。p²y=-q^-1 y p²の倍率は±1外なので二元平面補題に反する。

新補題lem:h3-binary-nonnormal-quadratic-normalizer：量子/Jordan AS2で非正規一次元yが非零二次hによりhy=lambda yhと正常化されるならlambda∈{±1}。量子でy=u+v、lambda非1のu³,v³係数でh=Buv、残り二係数からlambda²1。Jordanでy=u、三角係数行列det(1−lambda)^3。verify_cubic_order2_normal_axis.pyがresultant、全八行のcyclotomic完全剰余、二元補題係数を標数零で厳密検算PASS。構造帰着と整域排除は本文で証明。

さらにq=-1でもc!=±1はc=±i,v²=Axyから追加二次関係で排除。c1はB/(x)の三次次元>=11が正規一次元商のHilbert次元10に反するため排除：py=epsilon yp,p²=Ay²,v²=Cy²の18列に独立な二つの全係数syzygyを明記し、検証器も定数pivot15と残余一列を再生した。従ってc−1。a1ならmu*theta_xがxのみ符号反転しGを−Gに送るので、Gは奇数個xを含む語の和、正規性でG=xHに因子分解してR整域性に反する。従ってa−1、xは残り三生成元全てと反可換しx²中心となる。正常共通座標が二本あることも不可能（他軸はa1だから）。

次：このx反可換・x²中心領域について全関係を既知Clifford型又は新候補へ還元する。同時に共通量子座標が全Bで正規でない場合、可換/Jordan共通平面のrank2を未被覆として保持する。全H3の半単純化や正常化をこの追加仮定付き定理から推論しない。

## 正規共通量子座標領域の三パラメータClifford正常形（classification-v112）

追加仮定付きだが、この領域の全H3包絡を三パラメータで被覆：xはp,y,v全てと反可換、py=yp、v²=y²+i x²、p²=a y²+yv+vy+d x²。H3三次はG=[py,v]の一本。原稿thm:h3-order2-normal-axis-clifford-form。全三パラメータでのH3十分性・幾何学的矢をまだ結論しない。

証明の要点：正規一次元商S=B/(x)はchange-of-rings二行TorによりKoszul、HS=(1−t)^−3とReesでAS3。RRZ Lemma1.5（一次資料rrz.txtを再確認）のnormalizerはx b=tau(b)x、この場合tau=theta_xはinvolutionで、muS=(-p,y,v)。最高三次rho=tau0(ppy−pyp+ypp)+Phi(y,v)。Phi二文字cyclic三次は完全対称なので平方関係はyv+vyだけを含む。v->v−F yでv²=E' y²+I x²,E'非零（零なら反可換xとvの非零一次元平方零）。最高tensorの収縮でp²の{y,v}係数B'=delta E'/tau0も非零。尺度でE'=B'=1にする。

Gamma=(active parity,p parity,x parity)、c(g,h)=(-1)^(active_g*p_h+x_g*active_h)でC=B^cに移すとx中央、{p,y}=0,v²=y²+i x²,p²=−a y²−{y,v}−d x²。Y=y²,L={y,v},T={p,v}が中央になることを全関係から証明し、CはZ0=k[x,Y,L,T]上rank8の真正Clifford環。M=[[-aY−L−dx²,0,T/2],[0,Y,L/2],[T/2,L/2,Y+ix²]]。十個の全overlapで自由基底1,p,y,v,py,pv,yv,pyvを確認し、全係数の平坦Hilbert1/(1−t)^4を得る。AS4/domain/H3十分性をこのPBW計算だけで言わない。

Z(C)=Z0+Z0*g、g=pyv−L p/2+T y/2、g²=−detM。detMのYT²係数−1/4なので全パラメータで分数体上非退化、中心はF+Fg。gのpyv係数1と定数係数0から格子との交差でZ0+Z0gへ戻る。Bの全W1はmuG1とthetaG−、次数3からGamma=(1,1,0)に限り、cocycleで中央になる。中心3でその次数はgだけ、Bの[py,v]は2gに対応する。よってW1一本。

net判別三次は4detM|x0=(L+aY)(L−2Y)(L+2Y)−Y T²。Y1の三次判別式16(a²−4)²、無限遠点は常に滑らか、a=±2の二重根は普通node。これはnetの判別曲線の計算であって、boundary THCRとの同一視、H3許容性や全AS4存在証明を代替しない。verify_cubic_order2_normal_axis_clifford.pyで十overlap、volume/平方、全符号cocycle、判別式を全パラメータで厳密検算PASS。

次の具体的着手：この三パラメータでH3十分性を、中心Clifford純volume商とprojective character完全交叉で判定する。既知smooth-boundary Clifford部分とのパラメータ対応を先に厳密確認し、a=±2のnodal判別と無限遠のcharacter点を勝手に除外しない。一般の正規座標存在、量子/Jordan/可換共通平面全体、他の中山スペクトル、大域群oid/相対降下は未完成。

## nodal判別a=±2の全値非H3（classification-v113）

原稿thm:h3-order2-normal-axis-nodal-exclusion。a=±2を全d,iで排除した。C/(g)へ有限cocycle輸送するとtailsの大域次元は有限群同変化/induction分裂で不変。最高Koszul Gamma次数(1,0,1)のcocycle指標がmuBを相殺するのでCはCY、中央三次商DのSerreは(-1)[2]。

Y=y²の開集合A=(D[Y^-1])0ではr=xy^-1,s=py^-1,b=vy^-1−u/2,u=L/Y。rs=−sr,rb=−br,sb=bs,r²=z,s²=h,b²=F(z,h)=(h−a−dz)²/4−1−iz、u=h−a−dz,T/Y=−2sb。Aは中央k[z,h]上rank8自由。逆のskew Laurent模型x=ry,p=sy,v=(b+u/2)y、yは(r,s,b)->(r,−s,−b)で作用し全六関係/gを復元する。

a=±2ではF(0,0)0。中央(z,h)完備化は特殊fiberがr²=s²=b²0の局所有限代数（radical四乗零）、唯一の単純k。一次関係がなくExt1(k,k)3。対応点x=p0,y1,v−a/2はシフト固定。有限中央orderの点Ext局所大域比較と完備化でExt_Ahat=Ext_qgrD、H3ならExt2self1,高次0。完備局所代数の最小自由解消はrank(1,3,1)となるが、Frac k[[z,h]]上ではAhat次元8、k消滅なのでEuler8(1−3+1)−8が矛盾。非可換Jacobianや奇数Ext1の未証明一般原理には依存しない。verify_cubic_order2_nodal_axis_obstruction.pyで全PBW/逆代入、節点の全係数接空間、特殊fiber四乗零、top符号を厳密検算PASS。

a²!=4の既知Clifford swapへの座標対応と許容判定は、下記v114で六関係・判別式の完全恒等式として検証済み。nodal排除はその被覆外のa=±2を補完する独立な局所証明である。

## 正規共通量子座標領域の完全H3判定・全矢（classification-v114）

この追加仮定付き領域の全H3対象は、正常形xp/xy/xv反可換,py=yp,v²=y²+i x²,p²=a y²+{y,v}+d x²、G=[py,v]、U={(a²−4)di(d²−adi+i²)!=0}で被覆される。原稿thm:h3-order2-normal-axis-complete-admissibility。全H3被覆ではなく、正規共通量子座標を持つ領域の完全必要十分条件である。

明示Clifford cover：k=h³,r²=k+1、a=(k²+20k−8)/(4r³)、d=h(k−8)[b(k−2)−3ch]/(4r³)、i=h(k−8)(2b−ch)/(4r²)。p_old=R*p,R²=16r³/[h²(k−8)²]、U_old=4r*v/[h(k−8)]+2(k−2)y/[h(k−8)]、X_old=(U_old+p_old)/2,Y_old=(U_old−p_old)/2,Z_old=y−hU_old/2,t=x。既知Clifford swap六関係に完全代入し零を検証。a²−4=k(k−8)³/[16(k+1)³]、a²!=4の全点でquartic coverの根はk0,8,−1を避け、b,c->d,i行列は可逆。従って既存thm:normal-order2-clifford-cutsの仮定h非0,h³非−1,8を漏れなく満たす。

中央cocycleも保つ座標変換なのでcharacter CIはpy0,p²+a y²+2yv+d x²0,v²−y²−i x²0へ移る。di0はJacobian退化。di非0ではy0枝が4点、p0枝はy1でa+2u+dz²0,u²−1−iz²0。消去二次Q=du²+2iu+ai−dの判別式4(d²−adi+i²)、z0はa²4だけ。よってreduced iffdi(d²−adi+i²)非0。既存四次判別との直接式di(d²−adi+i²)=−h6(k−8)6*Delta_h(b,c)/(1024r13)も検証し、適用範囲を二重確認した。これは可換character CIのJacobian計算であって一般NC Jacobian原理ではない。

全矢：共通次数スカラーを除き(lambda,zeta)∈Gm×mu4が(a,d,i)->(zeta²a,zeta²lambda²d,lambda²i)で作用。生成元x->lambda x',p->zeta p',y->y',v->zeta²v'。mu正直線p、共通W、fの異なる固有直線x/y、theta_xの固有空間から全矢は対角＋vへのy平行移動に限る。v²の独立な{y,v}係数が移動を零にし、平方比較で全矢が尽くされる。di非0により全点でlambda²=zeta²1、一様慣性mu2²（従来genericの主張をこの正常形で強化）。原稿thm:h3-order2-normal-axis-full-arrows。

粗空間はrho=ai/d,sigma=(d/i)²、sigma非0,(rho²sigma−4)(1+(1−rho)sigma)非0という滑らかな既約2次元開曲面。表示族のrigidified stack[U/(Gm×mu4)]はこの粗空間上mu2²-gerbe。中立とは主張しない。単位minorと符号固有直和により全係数矢は非被約底にも適合し、表示族の許容主開条件・fpqc降下を得る。一般intrinsic Abel圏族との同一視や全モジュライの成分性は未解決のまま。

verify_cubic_order2_normal_axis_admissibility.pyは六元関係、cover、正規化行列det、旧新四次判別式、全character消去、矢共変式と粗座標を標数零で独立検算PASS。H3十分性は既存Clifford定理への厳密還元、nodal全排除はv113局所構造証明、全矢は本文の自然性/係数比較に依存する。

次の具体的着手：重複度(1,3)の残りrank2についてcross一本の両射影を解析し、共通量子平面の正規座標が存在する条件をKoszul最高tensorから導く。正規座標存在を一般に仮定してはいけない。量子q−1以外の非正規cross、可換/Jordan共通平面をまず区別し、Clifford以外のH3候補又は排除を得る。正三次元側・2+2・三/四中山固有値、CY全被覆・非捩れqso3・大域成分/相対降下も未解決。

## (1,3)全域の共通平面はq=-1、負三平方は中心（classification-v115）

追加の正規座標仮定なしで、共通平面T=(uw=-wu)、pの作用は両軸に逆符号、u²,w²,v²全て中心と証明した。原稿lem:h3-order2-global-cross-formsとthm:h3-order2-global-minus-one-plane。可換/Jordan共通平面も全域排除したため、v114末尾の「可換/Jordan未被覆」はこの新定理により解決済み。正規軸の一般存在や全H3判定まで済んだわけではない。

最高tensorのA4部分はcyclic、偶flattening Hは対称rank4。pp行q0(W)、p²vW/p²v²成分零。外側四乗c=w_vvvv非零ならv平行移動でv³W0とし、cross行は平方kernelのq0/cross一本に入るのでcrossblockは非零rank1。cyclic両対角block一致からcrossはvell−lambda ellv,q0補正、lambda±1、vvW²はrank1 ell²となりv²=cprime ell²。

四乗零ならv³W非零（零ならvv行pp行が比例し二平方投影rank2に反する）。vv行のcrossはn(vell+ellv)。pp/q0座標の対称Schur補完後rank2、crossblock不変、vv対角0のままなのでHcross=rk^t+kr^t,r=(ell,ell)。cyclic両対角一致からk_left=k_right。vvW²はell*s+s*ell、W平行移動でcrossを{v,ell}=0とし全v²W²成分を零にする。vell行からv²∈T2も得る。ここでcrossblockを最初からrank1と誤って仮定しないこと：四乗零の場合はrank2まであり、Schur/cyclicによる平行移動が必要。

二元centralizer：量子q非±1の任意ellとJordan任意ellでT2 centralizer=k ell²。反可換二次は量子q±iのell座標軸で他軸平方の倍数だけ。q−1では任意ellのcentralizer=span(u²,w²)、反可換部分k uw。可換反可換0。これらは三係数の直接計算。

四乗零：v²commellなので非±1量子/Jordanはv²∝ell²となり非零一次式平方零。可換ではf²−I,detf−1からfscalar±i、ell全B正規の重みW1,v−,p±iにGの反可換固有値−が現れずW1零。四乗非零：lambda−ならq2commell、非±1/Jordanではq2∝ell²をv平行移動して同じ平方零。可換ではell²正規、pだけ反転する正常化にmu固定三次（p奇数個）の固定元がなくW1零。lambda+ならq2antiell、q2零は可換v/ellと平方比例で一次因子化。量子q±i例外は[v,x]=t y²,v²=c x²からv y²=-y²v、Y=y²の正規化(x,y,v,p)=(-x,y,-v,-q p)にmu固定三次の固有値1が無くW1零。q−1ではq2=tuwがvとも反可換、pとも反可換し、全4生成元を反転する正規二次q2とGの可換性が次数3に反する。従って全域でq−1、lambda−だけ残る。

負平方中心性：四乗零ならv²とell²がcentral T2に入り独立（比例なら平方零）、vは両者と可換するのでu²,w²とも可換。四乗非零ならq2とell²が独立（比例ならv移動で平方零）、vはq2とell²に可換。pはaxes squares固定なので全Bでu²,w²,v²中心。verify_cubic_order2_global_common_plane.pyはcyclicブロック、量子/Jordan centralizerと正規化符号を厳密検算PASS。Schur帰着と整域/正常G排除は本文の構造証明。

残る二chart：A)四乗零,{v,ell}=0,v²=h(u²,w²)、hとell²独立。ellが量子軸ならv114で既に完全分類なので未被覆はellが両軸成分非零の場合。B)四乗非零,v²=c ell²,{v,ell}=q2(u²,w²)、q2とell²独立。この両chartのp²関係・W1・許容性が次の核心。

未検証だが次に使う着想：負三生成元の三つの二次関係は全て対称で、負平方と交差反交換子が中心となるためClifford表示が期待される。S0の三元三関係quadratic dualは可換三二次式で、B整域はrank1対称関係を禁じるのでArtin complete intersectionを導ける可能性がある。B3のmu負成分dim11はS3とpvp一本で張られるためS3 dim10を強制し、負三生成元部分の三次関係の追加を除ける見込み。これでp²がTをcentralizeする条件をS0内で比較しp²全B中心を導く方策を試す。ただしS0全次数埋込み/AS3性、p²中心性はこの版ではまだ定理に含めない。

## 全(1,3)でp²と負反交換子も中心（classification-v116）

原稿thm:h3-order2-positive-square-central。全(1,3)H3でp²,u²,w²,v²,{u,v},{w,v}が中心と証明。pu=-up,pw=wpとしてP=p²,X=u²,Y=w²は一次独立、負反交換子L1(P,X,Y),L2(P,X,Y)、v²=H(X,Y)という六関係・八係数の必要表示へ還元した。L1/L2のP係数は同時には零でない。任意係数のAS4/H3十分性、三中心二次元の代数的独立性、負三生成元部分代数の全次数AS3埋込みはまだ主張しない。

負三生成元の三関係だけの抽象S0を取る。v115の独立二中心平方の議論は線型係数行列の可逆性だけでS0内でも通り、X,Y,v²中心。A={u,v},D={w,v}はそれぞれu/vとw/vに可換、[A,w]=[u,D]。crossのalpha A+beta D=q(X,Y)中心、alpha/beta少なくとも一方非零から両A,D中心となる。一方を自由Kとして他方を解けばS0はk[X,Y,K]上真正Clifford3、PBW rank8、HS(1−t)^−3。

B3のmu trace−2、dim20から負固有成分dim11。この成分はS0_3とpvp一本で張られる（p²をS0へ、pWpをf(W)p²へ移す）。S0_3dim10なので三次単射性が従う。p²=h2∈S0_2はTをcentralizeするため、同じ三次比較がS0でも成り立つ。S0 Clifford行列のK²係数−(X*dK²+Y*aK²)/4非零、genericで非退化。Cl2(u,w)は中心単純なのでCl3内centralizerは全体の二次元中心に等しい。よってh2はS0中心、次数2中心はspan(X,Y,K)。従ってp²=aX+bY+cK、特にvとも可換。

c0ならr1=pu+up,r2=pw−wp,r3=uw+wu,q=p²−a u²−b w²の間にmu正の独立二syzygyがある：r1w−u r2−p r3−r3p+w r1+r2u0、qp−pq−a(r1u−u r1)−b(r2w+w r2)0。AS4第三Koszul空間のmu正部分はFrobenius双対でdim1なので矛盾。ゆえにc非零、K=(p²−aX−bY)/cも全B中心となる。verify_cubic_order2_positive_square.pyがtrace/dim、generic Clifford determinant、両syzygy/独立unit minor/符号、交差交換子恒等式を厳密検算PASS。generic centralizerと三次単射性は本文構造証明。

次の具体的着手：八係数テンプレートA={u,v}=aP+bX+cY,B={w,v}=dP+eX+fY,H=gX+hYと置き、(a,d)非零、puanti,pwcomm,uwantiを使う。全PXY中心性はテンプレートからも導ける見込み（[v,X]=[v,Y]0、[v,A]=[v,B]0からP係数非零で[v,P]0）。T={p,v}はp,u,vと可換、Tw+wT=2Bp、T²中心、Gcan=Tw−Bpは期待されるmu正常三次、Gcan²=B²P−T²Y。これらは次版でPBW/正常化/非零性・実際のmuを検証するまで未使用。

未検証のPBW構成案：中心PXYとT上Clifford3(p,u,v)（puanti,pv+vp=T,uv+vu=A）を作り、wをsigma(p,u,v,T)=(p,−u,−v,−T)、delta(v)=B,delta(T)=2Bp,delta(p/u)=0のOre変数として加えw²=Yで割る。sigma²1,delta sigma+sigma delta0,delta²0が見込まれ、rank16のモデルとHS1/(1−t)^4を得る。実際のAS4/Nakayama符号条件を先に調べ、generic flatnessや明示正常三次だけでH3十分性としない。

## 全(1,3)候補の八係数AS4軌跡・正常三次を完全判定（classification-v117）

v116末尾のPBW案、実際の中山符号、正常三次非零/一意性、負三元Clifford全次数埋込みを解決した。全H3(1,3)候補包絡は八係数テンプレートpuanti,pwcomm,uwanti,A={u,v}=aP+bX+cY,B0={w,v}=dP+eX+fY,v²=H=gX+hY、(a,d)非同時零で被覆される。P/X/Y中心性はこのテンプレート自体からも導ける。原稿thm:h3-order2-eight-coefficient-AS4、cor:h3-order2-eight-unique-cubic。新規性は未確認であり、全係数のAS4 existenceとH3判定を区別する。

Clifford–Ore模型：中心Z=k[P,X,Y]とT上Clifford3(p,u,v)、p²P,u²X,v²H,puanti,pv+vpT,uv+vuAを作る。sigma(p,u,v,T)=(p,-u,-v,-T)、delta(v)=B0,delta(T)=2B0p,delta(p/u)=0。全六Clifford関係に適合しsigma²1,delta sigma+sigma delta0,delta²0なのでw Ore拡大/(w²−Y)が元の全六関係の環と同型。Z[T]上左rank16、PBW p^i u^j v^k w^l、全係数HS(1−t)^−4、noetherian。Tは中央ではないがD=T²は中央、Z[D]上rank32自由。従ってPXYとDは実際に代数的独立。

AS4完全条件：B1=bd−ae,C1=cd−af、Rscript=(d²h−a²g)²−(d² C1−a² B1)(B1 h−C1 g)。Rscript!=0 iff quadratic Koszul AS4、mu=(p,-u,-w,-v)。双対はQ/(PV,qP,qU,qW)、QはP/Wだけ反可換・他全可換のskew4、qP=P²+aUV+dWV,qU=U²+bUV+eWV+gV²,qW=W²+cUV+fWV+hV²。q三つはEbar=Q/(PV)で中央。P0の可換成分はV1としてU=dz,W=-azの二二次式d²z²+B1z+g,a²z²+C1z+hを持ち、そのresultantがRscript。Rscript0なら双対に非零射影点があり無限次元。

Rscript非零ならEbarはk[U,W,V]とquantum3(U,W,P)のk[U,W]上fiber productで、S=k[qP,qU,qW]は多項式環。両三変数成分はS上free8、二変数交差成分はS/(qP)上free4。depth lemma/commutative Auslander–BuchsbaumでEbarはS上free、三qは正則列。Q Koszulから正規正則二次PV商もKoszul、さらに三q商もKoszul（順方向のみ）。Ebar ASGor3index2から三q商はFrob top4,HS(1+t)^4。双対でB AS4、NakayamaはFrob双対符号から(p,-u,-w,-v)。noethAS4/成長4の既出Levasseur適用でdomain。

一次資料追加：A. Polishchuk–L. Positselski, Quadratic Algebras (AMS ULS37,2005), Chapter2 Cor6.3,p37を https://djvu.online/file/T1DOlccPNeqX0 の一次本文で確認した。Koszulから正規正則二次商への順方向を使う。直後のHeisenberg反例により「中央正則二次商がKoszulなら元もKoszul」は非可換一般には偽であり、これをこの族の証明には使わない。書誌も確認。as4から新たな包括定理は輸入していない。

正常三次G=T w−B0 p、G²=B0²P−T²Y、GのTw係数1、mu正常化全式を全八係数で確認。AS4/domain locusでは全W1はmu固定なので候補基底Pp,Xp,Yp,Tu,Tv,Tw,puv,puw,pvwの9本。係数行列46行9列は定数pivot8、残余零、Tw自由係数のみでW1=kGを全域で証明。負三元Clifford基底u^i v^j w^kはPBWの一部、自由中央KはPXYの可逆線型変換なので全次数埋込みも従う。その双対は可換三二次完全交叉E/(P)、従ってCY AS3。verify_cubic_order2_central_template.pyが全Ore/Clifford恒等式、G/平方、双対直交、resultant、全係数W1 rank8を厳密検算PASS。Koszul・Frobenius・正則列は本文構造証明。

次の具体的着手：この全八係数AS4主開集合のR=B/(G)がH3になる必要十分条件を求める。正常三次だけでH3としない。中央h0=pwはRで中心となり、Tも中心、h0²=PY,TY=B0 h0,T h0=B0 Pというscroll型中心式が期待される。Pchartでr=u p^-1,b=v p^-1−T/(2P)のrank4 Clifford模型r²=−X/P,b²=T²/(4P²)−H/P,{r,b}=−A/Pを調べ、全中心・各chart・完備局所gldim2/障害・rankとSerre/AZを判定する。これら中心/局所式は次の版で逆模型とともに検証するまで許容性定理に使わない。

## 全八係数商の中心scrollとPchart（classification-v118）

原稿thm:h3-order2-eight-scroll-order。包絡で[pw,v]=-G,[T,w]=2G、J=pwとTはRで中心。J²=PY,YT−B0J=Gw,JT−B0P=Gp。d=e0ならG=(T−fpw)wが因子化しR非整域、H3を排除。その他は中心候補C=k[P,X,Y,J,T]/三minorが正規dim3、e!=0ならB0を座標にしてcubic scroll S(1,2)、e0,d!=0ならT'=(T−fJ)/dでC=k[X] tensor k[s³,s²t,st²,t³]。ProjCはF1又はtwisted cubic cone、後者頂点完備中心k[[s,t]]^mu3(1,1)。

全反交換子と平方がCに入りRは有限、RのGK3によりCの追加核なし。R整域ならR2 torsion-free C、PchartgenericcentreがFracCなので全中心はC（有限代数の中央元は整、C正規）。evenRはgeneric rank4quaternion division order、qgrRは中心曲面上coherent order加群圏。中心の平滑性やorder局所gl2をまだ結論しない。

Pchart S=k[kappa,t,z]/(kappa*t−d−e z−f kappa²)、kappa=J/P,t=T/P,z=X/P。r=u p^-1,s=v p^-1−t/2、r²−z,s²=t²/4−g z−h kappa²,{r,s}=−(a+bz+c kappa²)というrank4Clifford。逆模型u=rp,w=kappa p,v=(s+t/2)p、pはr/s反転、中心固定。e!=0でS=A²_(kappa,t)、e0,d!=0でS=Gm_kappa×A1_z。形式行列det四倍=4z(gz+h kappa²)−z t²−(a+bz+c kappa²)²。e!=0でt³係数−kappa/e、e0d!=0でz kappa^-2係数−d²なのでgeneric非退化、chart全中心も正確S。verify_cubic_order2_scroll_order.pyで包絡恒等式、factor障害、逆chart全関係、detと錐parametrizationを厳密検算PASS。

次の具体的着手（未検証の局所障害案）：e0,d!=0の錐頂点をX=u²chartで調べる。S=p u^-1,W=w u^-1,V=v u^-1とすると中心P/X=-S²,Y/X=-W²、alpha=b−aS²−cW²、beta=−dS²−fW²、V²−alpha V+g−hW²0、SW=WS、{W,V}=alpha W−beta。tau=T/X=alpha S−{S,V}が中央、Gはtau W=beta S。頂点ではV²−bV+g0。b²−4g!=0なら二単純点がshiftで交換され、一次extension計算はExt1自己1・交差2となる見込みでSerre必要条件の全四成分同次元に反する。重根なら唯一単純のExt1が3、shift固定からExt2self1,高次0と合わせ最小自由解消Euler順位矛盾が見込まれる。正確なXchart逆表示とinfinitesimal extension線型計算を次に検証するまで、e0全域排除は定理に含めない。

F1側の次案（未検証）：Rでは全pair anticommutatorsが中央なので四生成元Clifford形式行列[[P,0,J,T/2],[0,X,0,A/2],[J,0,Y,B0/2],[T/2,A/2,B0/2,H]]を取れる。scroll三minorからp/w方向のkernelは(-J,0,P,0),(-Y,0,J,0),(-B0,0,T,0)が生成する線直和となるはずで、quotient rank3 bundleのeven Clifford orderとして全chartを記述できる見込み。conic bundleの平滑性・rank低下とgeneric divisionを調べるが、未証明のNC JacobianやH3 opennessには依存しない。

## 錐中心e=0の全値排除、全(1,3)H3はF1上order（classification-v119）

原稿thm:h3-order2-eight-cone-exclusion。d=e0はfactor既排除。e0,d!=0の錐頂点Xunitで正確なchartを作り全値非H3と証明。S=p u^-1,W=w u^-1,Z=v u^-1−alpha/2、中央pi=P/X,gamma=Y/X,j=J/X,tau=T/X、alpha=a*pi+b+c*gamma,beta=d*pi+f*gamma,H=g+h*gamma。S²−pi,W²−gamma,SW=WS=−j,{S,Z}=−tau,{W,Z}=−beta,Z²=alpha²/4−H、tau W=beta S。三変数Clifford環をSW+j,tau W−beta Sで割り、uがS/W/Zを全部反転するskew Laurent拡大で元の全六関係/Gを復元するのでexact表示。

頂点fiberはS²=W²=SW=WS0,{S,Z}={W,Z}0,Z²=b²/4−g。二根q!=0ではZ±qの二単純をshiftが交換。一次拡大は七変数（S/W/Zと四中央座標）で正確に計算：pi/gamma/jの一次成分零,tau=−(zi+zj)s,(zi+zj)w=(zi+zj)z0。自己はsだけ自由、crossはs/w/z自由からinner1を引くためExt1行列[[1,2],[2,1]]。H3 Serre(-1)[2]はshift交換二点の四成分を同次元にするので矛盾。これらの点加群はu作用1、v作用b/2±qを交互に取り、定数文字とはしない。

重根では唯一の単純k、fiber radical三乗零、Ext1self3、shift固定。H3ならExt2self1高次0で完備局所代数の最小自由解消rank(1,3,1)。中心完備k[[s,t]]^mu3(1,1)はdomain、generic order dim4でEuler4(1−3+1)−4が矛盾。従って全e0排除、全H3(1,3)でe!=0かつ中心F1。verify_cubic_order2_cone_obstruction.pyはinverse Clifford chart、七変数一次extension全系をqだけの単元pivotで全係数消去し自己1/cross2/重根3とradical冪零性を独立検算PASS。局所大域比較とSerre/Eulerは本文構造証明。

次の具体的着手（まだ未検証）：eunitでscroll標準座標Y=lambda*s²,J=lambda*s*t,P=lambda*t²,B0=mu*s,T=mu*tを使う。中心F1のkernel線は(-J,0,P,0),(-Y,0,J,0),(-B0,0,T,0)、quotient rank3 bundleはE=O(F)+O+O、q値線束L=O(E_exceptional+2F)。三変数quadric matrixは[[lambda,0,mu/2],[0,X,A/2],[mu/2,A/2,H]]、X=(mu*s−lambda(d t²+f s²))/e、A=a lambda t²+bX+c lambda s²,H=gX+h lambda s²。全R2 sheafがこのeven Clifford orderか、exact kernel quotientで証明する。lambda0のexceptional curveではmu単元、detはXの一次成分でs0の一地点だけ単純零なので、その近傍は常に局所gl2となる見込み。

その後の方針（未証明）：rank3 conic bundle総空間のsmoothnessが、rank2 fibreではdiscriminant smooth、rank1 fibreでは二中心線型係数のbasepoint-free pencil/nodeに等しく、Clifford order gl2と同値になる可能性。Pchartのnormal formとSerre pairingで必要性、formal congruenceで十分性を検証する。generic divisionはsmooth plane quartic discriminant上のQ_X=(plane coordinate A*C−d B²−f A²)/eがdouble lineでないことから残余二重被覆の非自明性を示せそう。nodeがある場合はformal quantum planeのBrauer residueで示す案。未証明のconic-bundle smoothness=>H3をこの版では使わない。

## F1上の大域Clifford束とplane quartic（classification-v120）

原稿thm:h3-order2-global-conic-bundle,prop:h3-order2-plane-quartic,cor:h3-order2-conic-recognition。全AS4/eunit候補でR even/odd sheafをrank3二次形式のC0/C1にexact同定した。scroll標準座標Y=lambda s²,J=lambda st,P=lambda t²,B0=mu s,T=mu t、kernel線O(-F)は(-s,0,t,0)、quotient V=O(F)+O+O、q値L=O(E+2F)。q matrix[[lambda,0,mu/2],[0,X,A/2],[mu/2,A/2,H]]、X=(mu s−lambda(d t²+f s²))/e,A=a lambda t²+bX+c lambda s²,H=gX+h lambda s²。M4 kernel三列がRの実際のlinear関係でもあり、逆Clifford表示で全rels/Gを復元するためsheaf同定はgenericのみに留まらない。C0=O+O(-E-F)^2+O(-E-2F),C1=V+Lambda3(V)L^-1、両者locally free rank4。lambda/mu非同時零でqrank0は全候補で起こらずconic bundle flat。

Z4=k[P,X,Y,D]上Bfree32、0B(-3)-G->B->R0はZ4自由解消、F=G²=B0²P−DYがRを殺しpd1/depth3。Z4+とC+のradicalは同じなので偶/奇のlocalcohom0,1,2も消え、両部分はClifford sheafのsection moduleで飽和。局所自由＋飽和でC-torsion-free、全候補でZ(R2)=Cまでdomain仮定なしに拡張。Rdomain iffgeneric quaternion division（P正則とexact skew Laurent chart）。構造対象のExtはH^i(C0)、負二線束はacyclicなので全候補で例外的。rank-one iffdivision、全完備局所order gl2ならASGor duality(-1)[2]が全Dbに延び、AZ/Serre/heart/Hilbert/AS4/飽和/torsion-freeと合わせH3全条件を得る。従って残る必要十分条件はdivisionとlocalgl2。

plane blowdown x=lambda s,y=lambda t,z=mu。Q=xz−dy²−fx²,U=ea y²+bQ+ec x²,V=gQ+eh x²、F4=4QV−U²−eQ z²。F4pullback=4e²lambda detq、判別類3E+4F、Eとの交点1。o=[0:0:1]はpartial_x F4=-eで常にsmooth。rank1 fibreはo外でQ=U=4V−ez²0。E(lambda0)ではdetq=−mu³s/(4e)、s0一点のみrank2単純判別、他Azumayaなので全E近傍gl2。Qのx/z minor−1/4、従ってQは決してdouble lineでない。verify_cubic_order2_conic_bundle.pyでkernel/quotientmatrix、quartic、rank1/例外曲線・conic非二重線を全係数厳密検算PASS。CM/飽和/圏認識は本文構造証明。

次の具体的着手（未証明）：qrank3点はAzumaya、rank2点はCl2 unit/parameter模型で判別の一次微分非零 iffgl2、rank1点は2x2Clifford係数(a,c,d)∈mのlinear maprank2かつ唯一の対称quadratic relationが非退化 iffgl2をSerre Yoneda pairingとformal congruenceで示す。これはconic bundle総空間smooth、又はF4がreduced nodalで全nodeがrank1 fibreという可換幾何条件に等しいはず。generic divisionはnodeがあればlocal quaternion(x,y)の非零Brauer residue、F4smoothならsqrt(Q/y²)が存在するとf*yがH0(D,O(1))のsectionとなりQがdouble lineになって矛盾（planequarticのH0(O1)は平面linear）。これを厳密化しH3全許容性へ進む。この版ではsmooth conic bundleだけからH3と結論しない。

## 全(1,3)H3 admissibilityをconic bundleで完全判定（classification-v121）

原稿lem:h3-order2-local-conic-criterion、thm:h3-order2-complete-conic-admissibility。八係数AS4/eunit領域でR H3 iff rank3 conic bundle総空間smooth iff plane quarticF4が被約nodalで全singular点がQ=U=4V−ez²0のrank1 fibreである。全(1,3)対象の被覆と必要十分許容条件が完成した。他の中山重複度や全intrinsicモジュライの完成とはしない。

局所rank3はAzumaya。rank2ではCl2(unit,f)=commutative doublecover(z²−f)#mu2、f linearならregular gl2、f∈m²ならsingular commcoverの剰余体無限pdがinduction/restrictionでorderにも残る。rank1ではCl2 r²=a,s²=c,{r,s}=d、a/c/d∈m。中央linear maprankmならExt1selfdim4−m。単位odd方向でpoint shift固定、H3 Serre Ext2self1高次0とfree resolutionEulerでm2必要。唯一のquadratic relation alpha r²+beta{r,s}+gamma s²の行列はYoneda/Serreで非退化、beta²−alpha gamma!=0必要。逆にlinear pencilをdiag(x,y)にしoffdiag高次をxA+yBによるGL2形式合同/中心座標変更で逐次消すとexact diag(x',y')、完成quantumplane−1 gl2。binary radical tangent pencilのresultantとdet-pencil discriminantもbeta²−alpha gammaに等しく、これがconic総空間smooth/判別nodeと同値。rank0は大域bundleで不存在。

Divisionも全許容点で証明。判別D=3E+4F ampleconnected。nodeがあればlocal quaternion(x,y)のx-residue y∈k((y))はvaluation1で非平方、globalBrauer非零。node無しならD smoothirreducibleplanequartic、genericresidueはsqrt(Q/(e y²))。仮に平方ならf*yはO_D1の有理sectionで平方Qが正則なので極なし。H0(P2,O1)=H0(D,O_D1)からf*y=linear ell、Q−ell²が次数2でD4上消えQdoublelineとなるが、Qのx/z minor−1/4に反する。よって全点genericdivision、v120認識でrank/Serre/AZ/例外性/整域/Hilbert/AS4を全て満たす。

H3係数locusはprojective conic bundleのrelative singular incidenceの像の補集合なのでZariski open、任意底変更/fpqc局所性に適合。この表示族のfiber条件であり一般intrinsic Abel圏族の効果的降下を主張しない。既知normalaxis点(0,0,0,1,-1,0,1,1)は二smooth conic四横断nodeで非空を確認。verify_cubic_order2_conic_admissibility.pyはlinear kernel/discriminant/resultant、formal合同の各次数消去、正例と悪いtriplepoint校正を厳密検算PASS。無限formal reduction、Brauer/residue、H3認識は本文構造証明。

具体的なnormal-axis外のH3：params(1,0,0,0,1,0,0,1)、rels puanti,pwcomm,uwanti,{u,v}=p²,{w,v}=u²,v²=w²、G=(pv+vp)w−u²p。AS4 resultant1、F4=xz(4x²−z²)−y4。binary quartic四因子が相異なり∂yでy0だけ調べればsmooth、従ってgenus3 smooth判別を持つH3。共通軸u/wどちらも全包絡で正規でなく既知Clifford swap部分とintrinsic pointed非同型。Nakayama通常det−1なのでskewにも非同型、非CY。文献新規性未確認。この例にはp->zeta8 p,u->u,w->zeta8^-2 w,v->zeta8² vというmu8部分群が見込まれ、全慣性は次で検証する。

次の具体的着手：全矢はp/u/w各線の尺度とv->s v+t u+r wに限る（mu正直線、commonW、f±axes自然）。8係数slice H0(P in v²)=0を保つにはtarget a*t+d*r=0という一条件。9係数にv²=kP+gX+hYを許せば全semi-direct group(Gm)^4 ⋉Ga²（共通gradingGmを割る）が作用し、sliceはfppf gauge。許容openへの全係数矢とstabilizerを正確に求め、4次元表示stackを作る方針。

未検証の慣性計算案：eunitでa,d両非零はdiagonal比較から全autoはmu2。a0,dunitでc0はnormalaxis mu2²、c非零ではmu2。d0,aunitで(b,c)非同時零もmu2。d0,aunit,b=c0ではvをwだけ移動しf0としてgbar=g−ef/2,hbar=h−f²/4、gbar非0ならmu4、gbar0,hbar非0ならmu8が期待される（hbar0は非H3になる見込み）。H3 criterionと全generator比較で次に証明する。


## 全(1,3)表示の全矢と四次元stack（classification-v122）

全(1,3)許容八係数表示の全幾何学的intrinsic矢を三角生成元写像と九係数式で確定した。正規三次はalpha*gamma*delta倍。共通次数尺度を除く明示表示群oidはsource滑らか相対次元4、安定化Lie環はAS4 resultant非零により全点零、従って滑らか既約DM4の表示stack。ad非零開ではa=d=e=1,b=0へfppf正規化し、許容A4_(c,f,g,h)×Bmu2。全intrinsic Abel圏族の認識/降下、全H3成分性は主張しない。次は全境界慣性を確定し、残る中山重複度(3,1)/(2,2)、三固有値以上・CY/unipotent被覆へ進む。

原稿thm:h3-order2-full-arrows、verify_cubic_order2_full_arrows.py/certificate。全矢p->alpha pprime,u->beta uprime,w->gamma wprime,v->delta vprime+r uprime+s wprime。各二次関係比較九式、G共変式、一般正規化は普遍Clifford--Ore模型で厳密検算PASS。Lie環はbeta1でC=-D,R=-bD/2,S=-fD。a(D-2A)=dA=3cD=(ab/2+df)D=(2g-b²/2-ef)D=(4h-bc/2-f²)D=0。D非零ならa0/dunitではc=f=h0、d0/aunitではb=c0,g=ef/2,h=f²/4となりAS resultant零。全点有限エタール慣性でDM。表示群oidは任意基底環上の明示式で定義し、全幾何学的intrinsic矢を被覆する。非被約基底上の任意圏族からこの表示への認識は未証明、分離性も未主張。


## 全(1,3)慣性と増大曲線（classification-v123）

全(1,3)の全幾何学的矢と滑らか既約DM4表示stackを確定。一般ad非零開は許容A4×Bmu2。全慣性は四種類：a=c0の閉正常軸面はmu2×mu2、d=b=c0の閉曲線はgbar=g−ef/2非零でmu4、gbar0で唯一のmu8点、その他全点mu2。曲線はgbar/hbar正規化により[A1_kappa minus{kappa²=-1}/mu8]、coarse j=gbar²/(e²hbar)∈A1 minus{-1}、hbar=h−f²/4。両増大閉部分は非交差。全(1,3)被覆・必要十分admissibility・幾何学的群oid/慣性・表示族stackまで完成。任意intrinsic圏族認識、全H3の他スペクトル・成分/交叉/閉包は未完。次は(3,1)/(2,2)の正規三次incidenceから未被覆域を減らす。

原稿thm:h3-order2-full-inertia。beta1で全自己矢はgamma*delta1。ad非零はalpha²=gamma=delta1,r=s0。a0,dunitはu平行移動でb0、自己矢r=s0,alpha²1。c非零ならgamma³1だがprimitive3はg=h0すなわちv²0を強制し非H3。c0ではg0がquartic Q*(4ehx²−ez²)の[0:1:0]にQ!=0のrank2 singular fibreを作るため非H3、gunitからgamma²1で独立二符号。d0,aunitはw平行移動でf0、自己矢r=s0,delta=alpha²,gamma=alpha^-2。b非零ならdelta1、b0c非零はdelta³1だがprimitive3でv²0。残りd=b=c=f0はAS resultant a4*(g²+e²h)、quartic xz(4ehx²+4gxz−ez²)−e²a²y4、H3 iff hunit（ASopen上）。h0なら[1:0:0]が退化接錐、hunitならbinary四根相異でquartic smooth。全慣性g(alpha4−1)=h(alpha8−1)=0。曲線の正規化a=e=h1はdelta4=he²,alpha²=delta/a,gamma=e/delta、残るkappa=g/delta²、全矢mu8のkappa->alpha^-4kappa。唯一mu8点はv121具体例。verify_cubic_order2_full_inertia.py/certificate全自己矢・discriminant・除外点・coarse不変量を厳密検算PASS。


## 正三次元bi-normal明示AS4族の全切断排除（classification-v124）

新たに(3,1)の明示bi-normal族 px=xp,xy=yx,py=-yp,zx=-xz,zy=-yz,z²=ap²+bx²+cy²を全係数で排除した。a非零ではClifford--Ore基底と中央自由階数32、二次双対の正規/中央正則列によりnoetherian Koszul AS4、実際mu=(+,+,+,-)。全正常三次はW1=x*span(p²,x²,y²)で全て因子化し非H3。a零では双対の無限次元商によりKoszul AS4外。これは(3,1)全被覆ではない。次は正三次元側の共通平面式q0(W)+gamma*z²（gamma非零も保持）と四次tensorのrank4偶flatteningから残る表示を絞り、(2,2)および他スペクトルの未被覆を減らす。全H3分類は未完。

原稿prop:h3-positive3-binormal-exclusion。P=p²,X=x²,Y=y²はaunitで全て中央、T=pz+zpはp/y/zと可換xと反可換。Cl3(p,y,z) over k[P,X,Y,T]、p/yとy/z反交換、{p,z}=T、z²=aP+bX+cY。xはp/y固定,z/T反転、x²XのOre商。全関係から逆模型を復元できPBW16、中央k[P,X,Y,T²]上free32、HB=(1-t)^-4。双対QはPX/XYだけanti、他comm、E=Q/(PZ,P²+aZ²,X²+bZ²,Y²+cZ²)。EbarのP0/Z0 fibreproductで中央三二次式正則列、前向きPP KoszulとASGor FrobeniusよりAS4。nuQ=(-,+,-,+)、tauPZ=(+,-,+,+)でnuE=(-,-,-,+)、muB=(+,+,+,-)。固定三次11基底P/X/Y times p/x/y plusTz,pyx。Gy=yGでp型/Tz/pyx五係数消去、Gp=pGでy型三係数消去、残りxP,xX,xY全て正常三次。常にxでfactorしR非整域。a0双対P0商はk[Z]自由rank4無限次元、Koszul AS4外。verify_cubic_positive3_binormal.py/certificateでClifford全overlap/自動同型、双対直交、十一列系constantpivot8を厳密検算PASS。文献新規性未確認。

正三次元の次案：mu半単純、共通平面作用f=diag(q,q^-1)なら偶flatteningはWW/vW/Wv/vv/zzの10x10対称行列。混合graph条件を線型に課すと普遍四次tensorは23係数（正三元反巡回21、z²W²一本、z4一本）。zz行はq^-2 xy−yx+gamma z²。rank偶4のSchur制約と整域性を使って三次正常核を絞る。scratch /workspace/work/order2_central_template/positive3_top.pyはこの線型空間を計算したが、rank制約・被覆・H3判定をまだ証明しておらず定理には用いない。


## 双対一次切断の普遍Hilbert値とAS3還元開部分（classification-v125）

一次元/三次元分解の全common-plane領域（単冪も保持）でE=B!の一次元側双対zetaは正規、zeta E1=E1 zeta dim3、階数列1,3,3,1。F=E/(zeta)は常にHilbert(1,3,3,1)、Ann(zeta)は(0,1,3,3,1)。F Frobenius iff Ann(zeta)=E xi=xi E、xiは共通平面の直交補線。この開部分ではAnn(xi)=(zeta)、二周期線型E解消とchange-of-ringsでF Koszul、F! AS3かつTor edge全射の双対によりF!->B単射。二つの3x3対合行列式で開条件を判定する。全(3,1)でのFrobenius自動性は未証明。次はFrobenius退化域を正規三次incidenceと併せて調べ、残る(3,1)/(2,2)被覆を進める。

原稿prop:h3-order2-dual-hyperplane。mixedgraph二関係より双対zetaの左右積U*像は同じodd2、核は同じxi=Wperp。top zz行q0非退化からzeta²非零、Lzeta:E1->E2 rank3。Frobenius双対で残る階数1,3,1が決まりF Hilbert(1,3,3,1)、annHilbert(0,1,3,3,1)。両側イデアル(zeta)はnuで不変、trace直交により左右ann一致。annはFの双対の捩れ/移動なのでF Frob iff annが左右xi一元生成。両者dim8から逆ann(xi)=(zeta)。E(-q)をzeta/xi交互乗法する線型解消ができ、TorE(F,k)内部q集中。change-of-ringsでF非Koszulの最初のTorF_p,j>pはq0から入る微分なく、出る先内部p-1で消えずKoszulEに矛盾。ゆえF Koszul、F! AS3。さらに全E2項内部p+qで全微分零、TorE(k,k)->TorF(k,k) edge全射。双対ExtF->ExtEの単射が自然F!->Bなので、実際にAS3部分代数が埋まる。Frobenius条件の全点非消滅は未証明なので全被覆とはしない。verify_cubic_order2_dual_hyperplane.py/certificateは全係数bi-normal E16模型でFrob対合、階数列、相互ann、F対合を厳密検算PASS。Frobenius条件は両方向F1/F2の3x3行列式非零で、退化域を黙って除外しない。


## 正三次元側の商体退化排除（classification-v126）

正三次元(3,1)側でも、gamma0で共通TがAS2平面の場合、残る正生成元vと負生成元z²が同時に斉次商体Qgr(T)へ入ることを排除した。可換/有限量子は固定中央体上有限次元でGK<=2、無限量子はhxyが非零次数4中心元となり矛盾、Jordanはh=cy²と(z/y)²=ac∈kから代数閉体上整域性によりz∈kyとなり矛盾。単冪も保持するがgamma非零には適用しない。次はgamma0の一平方投影でcross両射影が可逆となるpositive normalizing chartを分類する。半単純対角chartの先頭Ore環ではmu=(+,+,+,-)、正常三次はa³=-1でのみ残り全てyでfactorする見込み。この先頭因子化を変形後の因子化と混同せず、まず非共鳴a³!=-1の全変形除外を証明する。

原稿lem:h3-positive3-rational-collapse。f det=hdet1、muT=muW f²。量子q!=1ではmuWの固有値1のみなのでid、q−1反対角fはdet/hdet逆符号で除外、fdiag(a,a^-1),a²q。q無限位数のhomogeneouscentral r(u)y^mはycommからr(q^-1u)=r(u)、零極議論とq無限位数からr定数、xcommからm0。h=z²inner f²=muT=Ad_(xy)^-1ゆえhxy中央degree4矛盾。有限q/可換ではf有限、Q(T)はtrdeg2中央固定体F上有限、B subset D+DzもF有限、有限構造定数からGK<=2。Jordan yx=xy+y²、f(y)=a y,a²1なのでhcommy、h=r(x/y)y²のr周期は定数c、(zy^-1)²=ac、代数閉体上の整域で代数的元はscalarゆえz∈ky矛盾。verify_cubic_positive3_rational_collapse.py/certificateで量子muとf²、q−1反対角符号、Jordan/局所平方恒等式を厳密検算PASS。合理関数とGK論証は本文。


## 正三次元対角chartの共鳴と非共鳴変形の全排除（classification-v127）

(3,1)半単純対角normalizing chartの全先頭AS4族 xy=a²yx,zx=axz,zy=a^-1yz,vx=axv,vy=-a^-1yv,v²=z²の正常三次を完全計算：a³!=-1ならW1=0、a³=-1かつa!=-1ならky³、a=-1ならy*span(x²,y²,v²)。全先頭切断は因子化。重みW1/outer2の先頭環比較により、dx(W),dy(W),ell(W)v+q2(W)を任意に加えた14641/指定muの全変形もa³!=-1ではW1=0で排除。共鳴a³=-1の変形後因子化は未証明。次はa=-1とprimitive6のskew導分/平方補正を全係数で標準化し、正常三次とH3判定を求める。反対角/Jordan、gamma非零、Frobenius退化、(2,2)および三固有値以上は依然未被覆。

原稿thm:h3-positive3-diagonal-top。r=v+z,s=v−zでA=quantumplane−1、B0=A[x;sigma_x][y;sigma_y]、sigma_x(r/s)=a^-1(r/s)、sigma_y(r,s,x)=(-a s,-a r,a^-2 x)。noeth/PBW/domain/KoszulAS4。muA−、第一mu=(-a r,-a s,a^-2 x)、第二でr/s交換,x/y固定となり実際mu=(x,y,v,-z)。mu固定outerdegree0/1/2/3次元1/1/1/2で全三次11。W次数i/j、outer nなら正常化Gx=xG,Gy=yGはa^(n−2j)=1,(-1)^n a^(2i−n)=1。n1/n3は全gcd1で零、残るn0/2単項式はGv/Gzから(-1)^j a^(i−j)=1,a^(i−j)=-1、ゆえjodd。y³のgcd a³+1、x²y/yv²のgcd a+1、他gcd1。元来のgradeddegree固定で重み先頭環への全射とHS比較によりgrB=B0、正常Gの先頭もW1B0なので非共鳴変形全排除。共鳴先頭因子を変形後factorとしない。verify_cubic_positive3_diagonal_top.py/certificateでOre生成元三重積/六関係/固定11次元/全Laurentgcd/候補正常化を厳密検算PASS。


## 正三次元対角normalizing chartの共鳴も全排除（classification-v128）

正三次元(3,1)の指定対角normalizing chartを全係数・全aで排除した。非共鳴は先頭核零。a=-1は内部移動後vx=-xv+kappa*y²,vy=yv、商体退化排除からell0、x²/y²/v²中央、y正常mu、先頭核次元上界3と三独立候補でW1=y*span(x²,y²,v²)全てfactor。primitive6では全skew導分内部、ell/q2比較で全補正零、W1=ky³。AS4存在を任意補正係数へ主張しない。次は全normalizing chartのf/g平方根分類と残るq=-1反対角作用を調べ、gamma0の一平方投影領域を縮小する。

原稿thm:h3-positive3-diagonal-full-exclusion。g-skew導分条件はa(1−a)e0=(1+a)d2=0、(1+a^-3)d0+(a−1)e1=0、(1+a^-1)d1+(a−a^-2)e2=0。内部二列(d0,e1)=(1−a,1+a^-3),(d1,e2)=(a^-2−a,1+a^-1)。a−1では導分核3/内部2で残りdx=kappa y²,dy0。v²/z²commxとqWcommxからell[v,x]0、ell非零ならv∈Q(T)かつz²も入るので新商体lemma矛盾。ell0でqWはz反転に不変、v²commz、x²/y²/v²中央。yはmu正常なので三次候補三本、先頭kernel3次元で全核。primitive6は導分核2=内部2。delta0の後、外平方x比較で(a−a²)ellx=(a^-1−a²)elly0、T+Tv独立は商体lemmaによるのでell0。qWnormalization f²はx比較ky²,y比較kx²を強制しqW0。verify_cubic_positive3_diagonal_resonance.pyは全導分式と内部、Phi6上非消滅/gcd、a−1正規形の中心二次全交換子を次数3イデアルのparameter-free pivotsで証明PASS。全chart外を被覆とはしない。


## 正三次元の全normalizing chart排除と二平方商（classification-v129）

正三次元(3,1)gamma0で全normalizing chartを単冪込みで排除した。PBW整列/14641比較からg∈Aut(T),g²=f²。g±fは先頭mu重複度2+2で除外、他は対角全排除またはq−1四元数反対角。後者の先頭140x20正常化行列にdet=-128+128iの固定20minorがあり、全補正でもW1=0。対角でmuW=idの非分裂extensionはDv=wからg(w)=w,2wv+d(w)=ell*w⇒v∈Q(T)で排除。従ってgamma0全H3候補はB/(W)=k<z,v>/(z²,v²)かつ中山extension分裂。残るJordan型は半単純またはW上Jordan2＋自明1。gamma非零は未被覆。

原稿lem:h3-positive3-quaternion-chart,thm:h3-positive3-full-normalizing-chart,cor:h3-positive3-two-square-quotient。fの非自明Jordanならg²=f²の平方根は±f、fscalar±IのJordan平面でもg±f、これらは二段Ore先頭mu外側(-,-)で元の(+,-)と矛盾。g−fの場合の外側交換Zhangtwistはhdet1でmu不変。可換fscalarの反射gと量子fdiag(a,a^-1)のgdiag(a,-a^-1)はv128全対角排除、q−1の反対角g²−Iは尺度でvx=yv,vy=-xv,zx=i xz,zy=-i yz。r=v+z,s=v−z PBW全overlap一致、140x20正常化matrix固定20minor=-128+128i、全低重み補正除外。verify_cubic_positive3_antidiagonal.py/certificate厳密PASS。対角残りWµidではDv=w∈W、cross微分wt=g(t)w、t=wでg(w)=w、平方微分2wv+d(w)=ellw、v/h商体落ち矛盾でmu全体半単純。全normalizingchart空よりgamma0の一平方投影rank1はcross可逆なら全chart排除、退化なら商体lemmaで排除、rank0/一片平方は指数増大商。rank2だけ残り二平方商。非分裂Jordantensorの既存18恒等式を符号に依存せず適用するとzz/vv二列比例で平方像rank<=1となりrank2と矛盾、よってextension分裂。既存nonsplit_tensor/plane_matrices両検証を今回再実行PASS。全(3,1)被覆/排除としない。

次の具体的案（未証明）：gamma0半単純で正三元制限topはanti-cyclic、v4係数は常に零。二平方projectionrank2からv3W非零、vvrowcrossは[v,ell]型。rank4 Schurと二cross対角blockの逆符号から、vをW移動し[v,ell]=0かつv²∈T2という正側cross標準形が得られる見込み。量子q!=+-1/Jordanはcentralizer(v²,ell)=k ell²でcommuting平方factorのため排除候補。T可換又はq−1が残り、positive normalaxisまたはnormalquadratic重みでW1を調べる。正側cross標準形はまだ検証前なので定理には使わない。


## 正三次元半単純gamma0の全cross標準形と二平面制限（classification-v130）

(3,1)gamma0かつmu半単純で、正三元anti-cyclic topとrank4 SchurからvをW移動し[v,ell]=0,v²∈T2を全域で導いた。v4=0、v3W非零、vvrowcross=(ell,-ell)、Schur Hcross=rk^t+kr^tの二対角block逆符号でkleft=kright、三v orbitの移動でcross全消去。Tは可換かq=-1に限る。他の量子/JordanではcentralizerT2(ell)=kell²ゆえcommuting平方factorで整域性矛盾。可換f±Iならellはcentral又はmu正常一次、q−1 fdiag(i,-i)ならell²はmu正常二次、v²とell²独立で両軸平方もmu正常。Jordan正Wとgamma非零は未包含。

原稿thm:h3-positive3-global-cross。n(vell−ellv)をvvrowcrossとし、zz/q0coordの2x2blockでSchur。zz-cross0かつinverseqq0なのでcross-cross/vv-cross/vvdiagは変わらず残りrank2。r=(ell,-ell)からHcross=rk+kr、anti-cyclicでBRR=-BLL⇒k=(s,s)。crossC=ell s^t−s ell^t、vvWW=-C。vold=vnew−s/nによりvvv ell orbit(n,-n,n,-n)からAshift=-n(ell t+t ell),Cshift=-n(ell t−t ell),vvWWshift=+n(ell t−t ell)、全消去。[v,ell]0、crossrowからv²∈T2。量子q!=+-1/Jordan centralizer一次元で平方factor、可換又はq−1だけ残る。q−1 ell²/v²独立から両軸平方を線型復元してvcomm、zは両平方反転するのでmu正常二次。verify_cubic_positive3_global_cross.py/certificateでblock/三v項の実際の基底変更/centralizers/平方重み全係数厳密PASS。


## 正三次元可換共通平面の全排除（classification-v131）

(3,1)gamma0かつmu半単純で可換共通平面も全排除。正常ell=uと補元tに対しv²=Au²+But+Ct²、C0は平方factor又は余分な[v,t]二次関係で矛盾、Cunitからv²=t²+Iu²へ正規化。B/uは正規一次商の線型Tor議論でKoszul AS3、muC=(t,v,-epsilon*z)。三次topから全商はv²=t²,zt=epsilon*tz,z²=alpha*(tv+vt)+beta*t²,alphaunitに限る。z尺度でalpha1。両epsilon±、全betaで45x10正常化行列に定数pivot10があり、誘導muB=(t,v,-z)正常三次は零。ゆえ元Gはuでfactorし非H3。残る半単純gamma0全候補はT=q−1,fdiag(i,-i)、[v,ell]0,v²∈span(x²,y²)でell²と独立。両軸平方がmu正常。

原稿thm:h3-positive3-commutative-plane-exclusion。C=hのt²係数が0でut係数非零なら[v,v²]=Bu[v,t]0、整域性で[v,t]0となるがR_evenは[u,t],[u,v],v²-hと非零z²係数の一本しかなく余分なpurepositivequadを許さない。u正常regularlinearなのでC3=B/uは0B(-1)->B->C3とTor leastoffdiagでKoszul、HS3、ASGor/FrobからAS3。偶関係dim2/odd1とpositive一次dim2によりtopの元muB反転指標は+（奇なら二positive縮約がodd1へ入りrank欠損）。topz²v0はuniqueoddzt関係から。positivecyclicbinarytopのv縮約はBm²+C(mv+vm)+Dv²、purepositivequad v²-t²一本なのでC0,B=-D,Dunit。t縮約でz²=alpha{t,v}+beta t²,alphaunit。全beta両epsilonの次数3/4商を元の三関係からconstantpivotで10/15基底、正常muB(t,v,z)=(t,v,-z)行列45x10 constantpivot10で全kernel0。verify_cubic_positive3_commutative_plane.py/certificateはsampleではなく全係数恒等式PASS。muCはepsilonで異なるので、この核をmuC自身のW1と混同しない。GimageC0ゆえG=uQ factor。

残るq−1部分の次案（未証明）：ell軸又はell非軸に分ける。軸ell=xではvcommx,v²=gx²+hy²,hunit。双対F=E/(zeta)は明示Frob対合det∝hなのでv125でpositive AS3 SがBへ埋まる見込み。非軸はell=x+y,v²=gX+hY,h!=g、m=x−yでm²=ell²,{ell,m}=4/(g−h)v²−2(g+h)/(g−h)ell²、positive Sは上のepsilon+AS3商と同形でFrob top非退化が示せそう。S埋込み後、z²はWを反転するpositive二次なのでantiW2線型核からxyと[m,v]の二係数形に絞る。軸では正規xの重みで正常Gのzvz項が消え、Sの非零二次K=[y,v]がpositive全三元と反可換ゆえcentreS3零となってH3排除が見込まれる。非軸ではzvz項が残り得るので独立に検算する。これらは次の段階まで未証明扱い。


## 正三次元半単純gamma0の量子平面も全排除（classification-v132）

正三次元半単純gamma0の残るq−1部分も全排除した。ell軸/非軸でv²をgx²+y²又はgx²+(g−1)y²に正規化。positive Sの明示三次topの両flattenrank3でF=E/(z*)がFrob、v125からS AS3がBへ埋まる。z²はS2でW反転するため二次反交換子核がspan(xy,[y,v])に限り、z²=Axy+B[y,v]。B0は全係数でdegree3dim21、Bunitを1へ尺度変更すると両二parameterchart全係数のdegree3/4商20/35、正常三次140x20は定数pivot20でkernel0。AS4存在を任意係数へ主張せず、必要候補被覆と正常核零だけで全H3排除。

原稿thm:h3-positive3-semisimple-gamma-zero-exclusion。軸hunitでh1、非軸g−hunitでh=g−1。F Hilbert(1,3,3,1)は普遍lemma。positive Sの明示top：軸はvvx−vxv+xvv−gxxx−(xyy+yxy+yyx)。非軸u=x+y,m=x−yはm²=u²,[v,u]0,v²=alpha{u,m}+beta u²,alpha1/4,beta g−1/2、top alpha m³−alpha(uum+umu+muu)−beta u³+vvu−vuv+uvv。両flattenrank3でFrob、S AS3実埋込み、muSはW固定v反転でCYとしない。S2 antiW kernelは両chart次元2、xy/[y,v]が基底。z²=Axy+B[y,v]、B0はR3 constantpivot43でdim21だから不可、Bunit zscaleで1。R3/R4 constantpivot44/221、正常系constantpivot20で全param核零。verify_cubic_positive3_quantum_plane.py/certificateが全商射影・S top/反交換子核・正常kernelを元の関係から厳密再生PASS。

## 正三次元gamma0のJordanも排除、領域全体が空（classification-v133）

正三次元(3,1)gamma0領域を単冪込みで全排除。残るW Jordan2＋自明vではDy=x,Dv0、top v³x非零からvx=xv+d x²、x正常一次。偶B2D核はspan(x²,xv,vy−yv−dxy)。正常一次商C=B/xはKoszul AS3でmuC=(y,v,-epsilon z)、v²=c[v,y],zy=epsilon yz。三次topのpositive二元cyclic縮約が対称なのでc0、top正部分はAv³+By³だけ、残るz²=t y²。Cは二generator quadconeとv²0の自由積でHC=(1+s)/(1−2s)、degree3dim12とAS3値10が矛盾。全t/両epsilonの定数pivot15でdim12を厳密再生。従って(3,1)H3があるなら必ずgamma非零。

原稿thm:h3-positive3-gamma-zero-exclusion。v129で中山extension分裂、残りWJordanだけ。common f上三角epsilon²1、T yx=xy+kappa x²（kappa0可）。Dtop不変でv³y0、purev4はanti巡回0、二平方projectionrank2からvvrow/z²row独立なのでv³x!=0。v/x巡回からvvrowcross [v,x]、WWのD核x²よりvx=xv+d x²。x正規でB/xの線型Tor/Koszulとnormal ASGorでAS3、HS3、muC反転z符号−epsilon。B2even6基底x²,xy,y²,xv,yv,vyのDkernel3はx²,xv,vy−yv−dxy、ゆえmodx v²=ccomm。C oddR1/positiveV2でtopは元z反転偶、oddgraphzyがz²vを禁じ、purepositivebinarycyclicv縮約の対称性からc0。クロスcubiccoeff0でtop正二元部分v³/y³だけ、C三関係v²0,zy=epsilon yz,z²=t y²。自由積HS指数、又はdegree3原関係matrix定数pivot15/27でdim12、AS3dim10矛盾。verify_cubic_positive3_Jordan_obstruction.py/certificateでD核・対称縮約・両符号全tのdim12厳密PASS。

次の具体的着手：残る(3,1)はgamma非零。q0(W)+gamma*z²関係のためWにAS2平面分類を直接適用しない。mu半単純fdiag(a,a^-1)ならS(W,z)はxy−a²yx+gamma z²,zx=a xz,zy=a^-1 yzの三generator AS3型、q0非零正常二次。補positivevを含む偶flattenrank4/平方projection/dual Frob開条件から全正常三次を絞る。gamma非零でのW部分代数への高次核、positive unipotent、H3認識はまだ未証明。


## gamma非零対角基礎の二次AS3と三次CY根拡大（classification-v134）

残る(3,1)gamma非零のf対角chartについて抽象基礎S=<x,y,z>/(xy−a²yx+gamma z²,zx−axz,zy−a^-1yz)を構造認識。SはPBW x^i z^j y^k,noeth quadratic Koszul AS3、実際muS=(a x,a^-1 y,z)。T=<x,y>はcubicCY AS3/index4/解消1221、二つのquantumSerre係数a²+a^-2が全関係、C=xy−a²yx=-gamma z²のweightedOre基底x^i C^j y^k。S=T+Tz自由rank2、Cprime=xy−a^-2yxは逆正常化、CCprime中央degree4。H3包絡への自然写像の高次核は未排除、f Jordanchartは未包含。この基礎をAS2と混同しない。

原稿prop:h3-positive3-nonzero-gamma-base。Sの順序x<z<y、zx=a xz,yz=a zy,yx=a^-2xy+gamma a^-2 z²、唯一overlap yzx=xzy+gamma a^-1 z³。三次Koszultop yzx−a zyx−a yxz+a^-1xyz+a^-1zxy−xzy+gamma a^-1z³、巡回は実際muSの逆を使う規約で検証（符号固有値のみの以前の計算では逆と同一）。TはC x=a²xC,y C=a²Cy,yx=a^-2xy−a^-2CのweightedOre、Cweight2、PBW x^i C^j y^kがS内even z基底に単射。C消去でx²y−(a²+a^-2)xyx+yx²,y²x−(a²+a^-2)yxy+xy²。最高syzygy x*r_y+y*r_x=r_y*x+r_x*yはcyclic4、muT=id、ASindex4。Cprime逆normalizerf^-2、CCprimecentral。verify_cubic_positive3_nonzero_gamma_base.py/certificateで両overlap、三次rels、二次top/逆mu巡回、三次CYtop左右syzygyとcyclic、Cprime/中央積、Hilbertrootidentity全係数厳密PASS。既知形の新規性は主張しない。


## gamma非零抽象基礎内の指定正常三次全判定（classification-v135）

gamma非零対角chartの抽象基礎Sで、指定正常化sigma(x,y,z)=(x,y,-z)の三次全核を判定した。a²-a+1非零なら核0、aがprimitive6ならspan(x³,y³)。Sdomainよりsigma固定、PBW六候補のz重みがa³=-1を強制、a=-1は六交換子系の定数minor18で除外、primitive6で両cubeをPhi6剰余検証。このsigmaは一般にmuSではない。S->B単射とG∈imageSの両方が未証明なので、全(3,1)H3への共鳴条件とはまだしない。

原稿prop:h3-positive3-base-normal-cubics。sigma正常非零GはsigmaG=G、PBW evenz degree3六項。z weight a^(i−k)=-1、指数+-1/+-3からa³=-1。a−1はgamma1へzscale後、commx/yの六列matrix固定rows[3,7,10,12,18,25] minor18でkernel0。primitive6はa+1unitでx³/y³だけがphase許容、両者全正常式をPhi6剰余でzero確認。verify_cubic_positive3_base_normal_cubics.py/certificate厳密PASS。原H3GがSにある/基礎map単射の証明を欠くので全スペクトル共鳴制約へ拡張しない。

gamma非零の次案（未証明）：f対角のW生成cubicCY TはC=xy−a²yx,Cprime=xy−a^-2yx二normalquadを持ち、genericcentreにCCprime degree4。残るpositive vがWをOre正規化するchartではv²∈T2+Wvとなるため、T2のnormalquadとg actionを分類してH3正常Gの核を絞る。vがWを正規化することは未証明で、未被覆chartを黙って除外しない。S->B高次核とGのS成分外項の検算も必要。


## gamma非零対角基礎写像の全パラメータ核二分法（classification-v136）

gamma非零f対角基礎Sからgraded domainへの写像（z像非零）の核を全aで完全判定：0又は(Cprime=xy−a^-2yx)のみ。a4=1は必ず単射。z局所degree0はqWeyl wu=q uw+c,q=a^-4,c=gamma a^-3,d=c+(q−1)uw=−a Cprime/z²。q∞はGWA単純性、qrootはd非零開でAzumaya次数N、非零整域商は中心curve上Brauer0/Tsenでsplitし矛盾、ゆえ非零kernelはd0。商はparameter aのquantumtorus、これも完全素非零idealを持たずkernel正確Cprime。S/Cprimeはquantumplane偶Veronesecone、PBWdomainで飽和確認。追加positive vやH3全許容性は未分類。

原稿lem:h3-qweyl-domain-quotients,thm:h3-positive3-base-kernel-dichotomy。qWeyl dnormalはdu=q ud,dw=q^-1wd。q1は通常Weyl単純。q∞A[d^-1]はD=k[d±],sigma(d)=qd,t=(d−c)/(q−1),X=w,Y=uのGWA、Bavula作者原稿Theorem2.1を今回一次再読し4条件sigma-simple/no inner power/coprime all n/t regularを点検、resultant c(q^n−1)/(q−1)²。qrootNではZ(A)=k[uN,wN]、freeN²、dN=cN+(-1)^(N−1)(q−1)^N uNwN。dNunit開全closedfiberはuN!=0ならd相異eigen+巡回u、wN!=0対称、両0ならtruncated oscillatorでM_N、従ってAzumaya。完全素非零商は非零中心idealからtrdeg<=1field上division次数NになるがTsenBr0でM_Nにsplitして矛盾。量子torusも∞単純、rootMはcentreLaurent2上AzumayaMとTsenで非零完全素idealなし。S[z^-1]=A[z±;theta] stronglygraded、kernel非零ならJ=degree0nonzero completeprime、dJ⇒CprimeI。d0商はquantumtorusなので更なるkernelなし、S/CprimeのdomainとzsatでI正確(Cprime)。a4!=1coneはz²=(a4−1)/gamma xy、yx=a²xy,zx=a xz,yz=a zy、x=s²,y=t²,z=lambda st,st=rho ts,rho²a^-1,lambda²=rho(a4−1)/gammaでevenVeronese。

一次資料：Bavula overview local /workspace/work/sources/bavula_gwa_overview.txt のTheorem2.1（GWA defining conventionYX=t,XY=sigma tも確認）。Stacks Project Tag03RD Theorem59.67.10（functionfield over algclosed of dimr isCr）とTag03RF Lemma59.67.11（curve functionfield Br0）を2026-11-16に原ページ確認、キャッシュ /workspace/work/sources/stacks_03RD.html,stacks_03RF.html。原稿にStacksTsenBrauer書誌を追加、Bavula書誌に2.1を追加。Azumaya全rootのmatrixfiber証明は本文で与え既存被覆定理を輸入しない。verify_cubic_positive3_base_kernel.py/certificateは局所/GWA/normalizer/resultant/oscillator recurrenceとcone4overlap/Hilbertを全係数厳密PASS、Tsen/Azumaya全位数は構造証明。

重要な帰結cor:h3-positive3-base-survives-cut：同じSをH3のRdomainへ写す核も0/Cprimeの二択。B2=R2ゆえ二核のquadratic部分一致、両方二次生成なのでkernel完全一致。基礎像はcut後もRに単射、よってGは必ず基礎像の外にある。v135のprimitive6二平面は全H3の共鳴条件には使わない。これは根拠不明のG基礎所在を仮定する代わりに、実際にその所在を否定する。


## Jordan基礎の単射性と全正三次元canonical基礎被覆（classification-v137）

gamma非零の残るJordan基礎S_J(yx=xy+kappa*x²+gamma*z²,zx=epsilon*xz,zy=epsilon*yz+beta*xz)は全係数でPBW/noeth quadraticAS3。z局所degree0は微分Ore A=k[u][v;delta],delta(u)=(kappa+epsilon*beta)u²+epsilon*gamma。deltaを可逆にするとsimple、非零completelyprimeはdeltaの一次因子u−rを含み、元の基礎でx=r zとなるためH3の一次独立性に反する。従ってJordan基礎はB/R両方へ単射。既存全行列標準形と対角kernel二分法を併用し、全(3,1)H3候補のcanonical基礎像を対角AS3/JordanAS3/量子Veroneseconeの三表示で被覆、全てRにも埋まりGは基礎像外。AS3枝では追加positive vと純正二次関係3本、cone枝では2本が残る。追加関係/正常G/許容性/全矢は未分類。

原稿prop:h3-positive3-Jordan-base-injective,thm:h3-positive3-canonical-base-coverage。SJ順序x<z<y、唯一yzx overlap=xzy+(epsilon*kappa−beta)x²z+epsilon*gamma z³。base quantumplane(x,z)上Ore y, sigma(x,z)=(x,epsilon z),delta(x)=kappa x²+gamma z²,delta(z)=−epsilon beta xz。u=x/z,v=y/zで[v,u]=lambda u²+epsilon gamma,lambda=kappa+epsilon beta、z actiontheta(u,v)=(epsilon u,epsilon v+beta u)。inverse x=u z,y=v zで全関係正確復元。微分Oreのf(u)=delta(u)を可逆にしたbasek[u,f^-1]はdifferential-simple、idealの最小v次数とcommuでsimple ring。非零completeprimeがfを含み、lambda0ではA通常Weylsimpleで不可、lambda!=0では一次因子u−rを含む。gradedkernelzlocalのdegree0 J非零⇒x−r z∈I_z⇒zsatでI、一次像独立と矛盾。

全基礎被覆：M1 muWsemiのfdiagは対角S（positive補空間の非分裂Jordanを仮定で除かない）、fJordanはSJ。M2 muWJordanはfscalar含めSJ。両SJ/diagSはquadraticAS3domain、diagのみkernelCprimeのcone像もある。B/R同じ一次・二次より両基礎像保持、Goutsideすべて。gamma非零evenR4のz²射影unitでpurepositivequad3、AS3枝W²kernel0なのでv関係3、coneはWquadCprime一本を消費しv関係2。verify_cubic_positive3_Jordan_base.py/certificateで両epsilon全coeffPBW/局所Ore/逆変換/判別式恒等式厳密PASS。構造被覆を全H3対象分類・全家族降下と混同しない。


## cone枝全排除、全正三次元H3の基礎はAS3に限る（classification-v138）

残る(3,1)のcanonical基礎の量子Veronesecone枝も排除。Wはq=a^-2 AS2,a4!=1,z²=kappa xy。vがQgr(W)へ落ちるとBは曲線体k(u)上skewLaurent内に入り、degree-n極因子O(n)でGK<=2矛盾。追加2quadsにv²がなければcross退化はこの矛盾、両cross可逆はW PBW×zzを避ける外側語でdegree3dim21矛盾。v²があればv³W0はvvrowのrank2 Wquadとcrossrank<=1がanti-cyclicで矛盾、非分裂v Jordanも既存D invariantでv³W0を強制し排除。半単純化後、z²relのcross0とv4top0からHcross=rk+kr、v移動で[v,ell]0,v²∈W2。q!=+-1のcentralizerからv²=c ell²因子化しdomain矛盾。従って全(3,1)H3のcanonical基礎は対角/Jordan quadraticAS3としてB/R双方に埋まり、Gはその外。HR/HA0=1+t+t²だが有限自由3は未証明。

原稿lem:h3-curve-graded-division-growth,thm:h3-positive3-cone-base-exclusion,cor:h3-positive3-AS3-base-Hilbert。curvegradedfractionはcone zlocal qtorusからk(u)[z±;u->a u]、同次数1有限gen f_i(u)zのlengthn係数極D_n=sum sigma^j D、degreeO(n)でdim BnO(n)ゆえGK2。ConeW量子AS2へのv rationalを全aで排除（旧gamma0 rationallemmaのmuT=f²仮定をここに誤用しない）。v²projection0のcross2双方可逆ならg/skewderivT、z²Tnormalcompatとfxy1で全diamond成立、normalbasisT×words(v,z) avoidingzz、HS=(1+t)/((1-t)²(1-t-t²))のdegree3=21。片側cross退化はv rational矛盾。v²projection1ならcross1両射影非零、vvrow非零。v3W0ならvvrow純Wquad rank2、crossrows squares0なのでcross-crossrank<=1、anti-cycle QvvWW=-Ccrossで矛盾。mu v=v+w非semi補正も3vW0のとき2v tensorに影響なし、D invariant3vW0で非split排除。mu semi後R_evenbasis[rT,z²-kappa xy,rcross,rv²]、crossproj[0,0,r,s]、M44=v4=0、Hcross=M33 rr+M34(rs+sr)=rk+kr。v130anti-crosstranslationでcommvell,v²T2、AS2q=a^-2!=+-1でcentralizer minor=−(a4−1)² nonzero、平方factordomain矛盾。verify_cubic_positive3_cone_exclusion.py/certはgrowth/block/minor厳密PASS。positive3_global_cross/nonsplit_tensorも今回再実行PASS。全基礎像はAS3のみ、RHSratio1+t+t²からmodulefinite/freeを推測で済ませない。


## 全正三次元候補のmonic正規化被覆（classification-v139）

**全体的なスペクトル制約（classification-v139）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定（v121–123）。(3,1)gamma0とcanonical量子Veronesecone枝は全排除。残る全候補のcanonical AS3基礎A0はB/R双方へ埋まる。vがQgr(A0)に入れば非零sGがA0∩(G)に入り矛盾するため、vは商体外。これにより純正二次関係3本は必ず二本の可逆crossと一本のmonic平方へ還元でき、vt=g(t)v+delta(t),v²=ell*v+qが全候補を被覆する。T=<W>は対角/Jordan両基礎でHT=1/((1-t)²(1-t²))、T2に関係なし。T基底×vv/zzを避ける交互語はHB=(1-t)^-4と一致して実際の基底となる。gはT自己同型、deltaは次数1skew derivation、平方互換は(g delta+delta g)(t)=ell*g(t)-g²(t)*ell。追加正規化仮定を課した部分chartではない。次はこの全被覆上の平方互換と正常三次を、対角/Jordan・共鳴値込みで排除又は分類する。(2,2)、三固有値以上、全CY被覆、全成分/圏族降下は未完。

原稿lem:h3-positive3-no-fraction,prop:h3-positive3-Jordan-cubic-base,thm:h3-positive3-monic-coverage。A0 noeth整域とcut後の単射でv rationalを排除し、純正関係空間Lのv²射影rank1/L0両cross射影isoを証明。Jordan TはC=[y,x]−kappa*x²=gamma*z²、Cx=xC,yC=Cy−2epsilon*beta*xC,yx=xy+kappa*x²+Cのweighted微分Oreで、SJ PBWへ単射。全候補のnormalspanのHilbert一致で基底独立を得る。任意T関係へvを掛けT+Tvを分離してg/deltaのwell-definedを証明、v(vt)と(v²)tから平方互換。verify_cubic_positive3_monic_coverage.py/certificateはOre/級数/係数の厳密恒等式を検証、商体/全被覆は構造証明。全H3分類や全係数AS4存在は主張しない。


## 対角canonical基礎の全monic拡大を排除（classification-v140）

**全体的なスペクトル制約（classification-v140）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。全(3,1)はgamma0/cone枝に加え、対角canonical AS3基礎の全aも排除。v139の全monic正規化被覆上でmu vの非分裂成分を二次自由性により排除、top vv縮約からg固定一次元Lを得る。Tの二次centralizerはalpha=a²+a^-2!=2でkL²、alpha2でkL²+k[x,y]。inner deltaは平方差factor、Heisenberg残余は通常Ore中山で排除。平方完成後g delta+delta g0で非innerが残るのはc=+-i,alpha0だけだが、N=x²y²が全positive反転/z固定の正規元となりH3 Gと可換かつ反可換して矛盾。c−1反射と軸swapは全alphaでinnerのみ、定数pivotと一変数unit coefficient idealsで特殊値込み検証。次は残るJordan canonical AS3基礎のmonic拡大を、W中山Jordan型込みで判定する。(2,2)、三固有値以上、全CY被覆、全成分/圏族降下は未完。

原稿lem:h3-positive3-cubic-centralizers,thm:h3-positive3-diagonal-base-exclusion。三次関係の可換化gcdxyでalpha!=2のAutTはdiag/anti、alpha2はGL2。vvrowはvv/zz係数0で、W²rel0からcross非零、anti-cycleで[v,L]となりgL=L。inner後ell0、centralizerでfactor、Heisenbergだけq=bC/gIでv²~z²となり、a1ではq−1plane(r=v+z,s=v−z)[x]上の通常Ore-yによりmu v−矛盾。a−1はH=mu twist(hdet1,H4id)で同じ矛盾。c!=-1の平方完成でSigmaの固有値からc+-iだけdelta x=Ky²が残り、T cubic skewderivはalphaK0。alpha0のN=x²y²はx/y/v反転,z固定、G evenz/degree3かつcommWでG0矛盾。c−1のSigma compatible4coeffはinner yのみ、swapはinner gauge後6定数pivot。verify_cubic_positive3_diagonal_monic.py/certificateでT4定数7pivot、両centralizerの3minor gcdalpha−2とalpha2rank2、reflection一変数unit ideals、swap6定数pivot、imaginary resonance alphaを厳密PASS。全Jordan基礎と他スペクトルはまだ未分類。


## Jordan基礎も排除、全(3,1)領域が空（classification-v141）

**全体的なスペクトル制約（classification-v141）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。全(3,1)は正部分の全Jordan型を含めて空と証明した。gamma0とcone枝、対角canonical AS3基礎の全aに続き、残るJordan基礎も全monic被覆上で排除。非分裂拡大は18個のD invariant quartic恒等式でv4/v3W0となり、W²rel0とvvrow非退化に矛盾。分裂後gはmuWと可換し共通固定線を持つ。muW Jordanならg unipotentで平方完成後delta0。muW semi/fJordanならAutT三角e²=c²、反射のskew derivationはinnerのみ。純根はq~C又はCprime、v²=lambda*z²+rho*x²に限り、通常Ore-y表示のmu v−が正固有値と矛盾。次は残る(2,2)のmixed relation rank2/4と、三固有値以上の正常三次incidenceを縮小する。単一固有値/CY全被覆、全成分/圏族降下も未完で、完全分類とは呼ばない。

原稿lem:h3-positive3-AS3-split,thm:h3-positive3-Jordan-base-exclusion,cor:h3-positive3-total-exclusion。全monic被覆とW²rel0により、非分裂のD-invariant positivequartic v4/v3W0からvvrow0を得てFrobに矛盾。split後mu v=v、g commute muW、vv cross[v,L]非零でgL=muL=L。Jordan TはD=[y,x], [D,x]0,[y,D]=2eta*xD+2xi*x³,eta=kappa−b,xi=kappa*b,b=epsilon*beta。M1semiはkappa=b!=0でAutT upper/e²=c²、unipotent/反射に限る。反射Sigma-compatible18x4 matrix rank3でinner y又はxのみ。M2はkappa=1+b,muW nonsemiでg x=x,g y=y+d x、平方完成とSigma eigen2からdelta0。純根q=A x²+B D,Bunit、normalizer条件A=−B(eta+d),(d−b)(d+kappa)0よりq~C=D−kappa*x²又はCprime=D+b*x²。epsilon負はH=mu semisimplepartのtwist(hdet1,H4id)でepsilon正へ。A=<x,v,z>はcentralx、v²−lambda*z²=rho*x²、muA=(x,-v,-z)。B=A[y;ordinarydelta]、Ore中山のrestrictionでmu v−となりpositivevと矛盾。verify_cubic_positive3_Jordan_monic.py/certificateは両reflection/centralizer/全係数root方程式/rootAS3最高tensor符号を厳密PASS、order2_nonsplit_tensor18恒等式も今回再実行PASS。これでgamma0/cone/diag/Jordanの全被覆を通じ全(3,1)H3 empty。

次の具体的着手：全(2,2)の偶/奇関係階数を既存top flattening制約から再読し、mixed rank4がdouble Ore形を強制するか、rank2に正規一次境界又は共通平面を強制するかを判定する。全(3,1)へ戻らず、mu二固有値の残る重複度と三固有値以上を減らす。全内在的family認識/stack降下や全CY被覆は依然必要。


## 半単純(2,2) rank2の四graph被覆と純mixed枝排除（classification-v142）

**全体的なスペクトル制約（classification-v142）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。全(3,1)は正部分の全Jordan型を含めて空（v141）。次の半単純(2,2)/mixed rank2では、奇top交代行列の両対角blockがD_ji,lk=A_il,kj、PfD=−PfAとなり、A0なら両方向の純mixed二式、A非零なら両射影可逆graphへ漏れなく還元。graphは2x2行列pencilのsecant/tangent/二rulingの四標準形、graph detは−1/+1/−1/+1。純mixed枝はeven crossblock可逆からSchur条件を得て、pI/qJordanは係数ideal1、qdiagは五必要表示へ正規化。五つ全ての指定正常三次140x20は厳密rank20で全H3排除。次は残る四graph型のeven rank4条件と正常三次を判定する。非半単純(2,2)、mixed rank4、三固有値以上、単一固有値/CY全被覆、全成分/圏族降下は未完。

原稿prop:h3-order2-22-pencil-coverage,cor:h3-order2-22-pure-mixed-schur,thm:h3-order2-22-pure-exclusion。twistedquartic全語空間は32=positive4+mixed22+negative6。odd H=[A B;-Bt D]rank2、巡回reshape D_ji,lk=A_il,kjは可逆でPfD=−PfA。A0ではB rank1,pureUV/VU各一本でdomainにより両2x2quad非退化。A!=0はrankA=rankD2、odd relation両射影iso。E pencil determinantが二零点/重根/恒等0からsecant,tangent,二ruling、DからFとdetg表を全被覆。pure枝B=m vecp vecq^tのevenKdet=−m4(detp detq)²、evenrank4でP可逆/Q=KtP^-1K。pI,qdiag1r又はqJordanに正規化、purepositivequartic P(A,B,C,D)det=−B²(4AD−B²−C²)なのでBunit、relativehomothetyでB=m1。qdiagではcyclic条件DZ=ArZ0,2AD(1−r²)+C(1+r²)0,4AD−2−C²0,Z=1+r+C(1−r)。Z0はr−1,C0,AD1/2を対角残余でA1,D1/2へ。ZnonzeroはA=D0,C²=-2,r²=-1の四表示。qJordan係数idealはGroebner1。五必要表示全てB3dim20/B4dim35、指定normalizer140x20rank20でG0、H3排除。verify_cubic_order2_22_rank2.py/certificateとverify_cubic_order2_22_pure_exclusion.py/certificateで全恒等式/五exactfield計算PASS。半単純rank2の四graph型のみ残り、他Jordan/rank4の被覆は未主張。

次の具体的着手：secant E=(x0z0,x1z1),F=(z0x1,z1x0),detg−1でodd blockを固定し、even P anti-cyclic4coeff/Qcyclic6coeffのrank4条件をSchur分解（even crossblockのrank strataも保持）で解く。tangentとrulingは同様に全係数top→六関係→指定normalizerを計算する。rank4や非半単純をこの節に混同しない。


## 二ruling排除、半単純(2,2)rank2は二graphだけ（classification-v143）

**全体的なスペクトル制約（classification-v143）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。全(3,1)は正部分の全Jordan型を含めて空。半単純(2,2)/mixed rank2は、全pencil被覆に続きpure mixedと二rulingを排除し、secant/tangent二graph型だけに縮小。pure mixedはeven Schur条件から五必要表示に限り、全五つの指定正常三次行列rank20で核零。rulingではKが一行又は一列だけとなり、三つの純二元関係のrank<=1条件とdomainからそのblockが零、反対側に三次元以上の純二次関係を強制して矛盾。二次minor/単位飽和idealを全係数厳密検証。次はsecant/tangentのeven rank4条件と正常三次を全共鳴/退化値込みで判定する。非半単純(2,2)、mixed rank4、三固有値以上、単一固有値/CY全被覆、全成分/圏族降下は未完。

原稿thm:h3-order2-22-ruling-exclusion。任意binary planeのpurequadratic関係はdomainならdim<=1かつrankone禁止。U-rulingはmixedtop正文字が全x0でK一行、P(A,B,C,D)のxy/yx/yy三行がpure正関係なのでrank<=1。その2minor idealはB²,C²,D²を含み、残るrow AxxはrankoneゆえA0。Uprojection<=1からpureVV kernel>=3で矛盾。V-rulingはmixed負文字全z0でK一列、cyclicQのuv/vu/vv三行N=[[b,d,c,e],[b,c,d,e],[c,e,e,f]]がpure負関係rank<=1。2minor idealを各行の2x2係数detで飽和すると全てideal1、従って各行rankone又は0、domainから全0。VVprojection<=1からpureUU kernel>=3で矛盾。verify_cubic_order2_22_ruling_exclusion.py/certificateで全係数GB/3saturation exact PASS。secant/tangent、nonsemi、mixedrank4は未解決。

secant all-unit chartの再開用未公表計算：g=[[a,b],[c,d]],ad−bc=-1,abcdunit。Kの非零はxx->uv:-d,xy->vv:c,yx->uu:-b,yy->vu:a。K可逆でP可逆、Schur negativecyclicはAa+Dd0および2AD(ad+bc)−B²(ad+bc)−C²ad0を強制。gen尺度でa=d=s,b=c=t,t²−s²1、B1とするとD=-A、s²C²+(2s²+1)(2A²+1)=0、detP=−(2A²+s²+1)/s²非零。これらはscratchのsymbolic恒等式で確認した必要条件で、全AS4/正常三次・境界abcd0の証明は未了。次にこのchartのnormalizerを厳密検算し、rankK低下境界を別に保持する。scratch /workspace/work/order2_22/secant.py、未公表式を全H3結論に使わない。


## 可逆tangentの一変数必要表示（classification-v144）

**全体的なスペクトル制約（classification-v144）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。全(3,1)は正部分の全Jordan型を含めて空。半単純(2,2)/mixed rank2はpure mixedと二rulingを排除し、secant/tangent二graph型だけに縮小。さらにtangentのeven crossblock可逆部分は全係数のpencil安定化作用でg=[[0,-1],[1,0]]へ正規化でき、even Schur条件からC0,B1,A=(1+D²)/(2D),D(1+2D²)unitの一変数六関係へ全被覆。正常三次の全D判定はまだ未解決。次はこの一変数族の正常核を厳密判定し、tangent c0境界とsecant全rank strataを残さず扱う。非半単純(2,2)、mixed rank4、三固有値以上、単一固有値/CY全被覆、全成分/圏族降下も未完。

原稿prop:h3-order2-22-tangent-normalform。graphg=[[a,b],[c,d]],det1のevenK=[[-b,d,a,-c],[a,-c,0,0],[-d,0,c,0],[c,0,0,0]],detK=−c4。E/F tangent pencilのgenerator stabilizerはP=[[1,p],[0,r]],Q=[[1,q],[0,r]]、p/q独立でg->QgP^-1、p=d/c,q=−a/c,r=1/cがgcanonicalJへ。Schur負cyclicはX=−Cc+D(a−d)に対し2BDcX0と−2B(Bc+D(a+d))X0なのでBcunitからX0。残余−4ADc²+2B²c²+C²c²+2D²(ad−bc)0。gcanonical/B1でC0,4AD=2+2D²、DunitかつdetP=−(1+2D²)unit。六関係は本文、verify_cubic_order2_22_tangent_normalform.py/certificateが全恒等式PASS。任意D AS4存在/正常三次/H3性は未主張。

再開用計算状況：scratch /workspace/work/order2_22/pid_tangent.py は係数環Q[D,D^-1,(1+2D²)^-1]上のunit row/column gcd操作を追跡する実験。次数3で44pivot/商20、次数4で221pivot/商35までは到達したが、全projectionの再生が式膨張で遅く、中断したため正常核全値certificateはない。tangent_ff.py のfraction-free代替も次数4で遅く中断。現在はGがmu固定なのでeven parityだけを用いる tangent_even_ff.py を実行中であり、未完を完了と扱わない。高速化用python-flintは /workspace/work/python-deps に局所導入したが、公表済み恒等式verifierの必須依存ではない。正二次式だけのscalar-sign正常元探索はgeneric fieldで核0だが全族排除に利用しない。secant共鳴s²=-1/2のPID実験も中断しており未証明。次は一変数exact normalizerの計算方法を改善し、未完実験を成功と誤認しない。


## 半単純(2,2) mixed rank4の正top三分法（classification-v145）

**全体的なスペクトル制約（classification-v145）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。全(3,1)は正部分の全Jordan型を含めて空。半単純(2,2)/mixed rank2はpure mixedと二rulingを排除し、secant/tangentのみ。tangent K可逆部分はD(1+2D²)unit,A=(1+D²)/(2D)の一変数必要表示へ全被覆。指定正常三次はgeneric fieldで核0だが全D判定は未完。mixed rank4の半単純領域では偶top rank2により正二元anti-cyclic quarticのB係数が零となり、純正topはcommutator⊙対称二次式に限る。従ってGL2と尺度で零/平方型/非退化型の三種へ被覆。次はtangent一変数族の全値正常核を多項式汎関数で検証し、c0境界/secant全rank strata/rank4三型を判定する。非半単純(2,2)、三固有値以上、単一固有値/CY全被覆、全成分/圏族降下は未完。

原稿prop:h3-order2-22-rank4-positive-top。oddR4ならevenR2でevenH rank2、purepositiveP(A,B,C,D)もrank<=2。3minor idealはB³を含むのでB0。逆にB0ならP=comm*q^t+q*comm^t,q=(A,C/2,C/2,D) symmetric、qnonzeroはcommと独立なのでrank2、evenR->UU projectionisoonto span(comm,q)。二変数対称式のrank1/2で三標準型。verify_cubic_order2_22_rank4_top.py/certificateでminor idealと外積和恒等式を全係数PASS。包絡/正常G/許容性は未判定。

一変数tangentの現計算：tangent_even_ff.py でeven cubic32語→10、even quartic128語→19、正二元との交換子38x10がgeneric Q(D)上rank10、従って指定正常Gもgeneric0を確認。D1とD=iでも正二元centralizer degree3は零をexact確認したが、これを全Dへ延長しない。全値証明の候補は19個のpolynomial quartic annihilatorを構成し、正三次32語の交換子へ適用して38x32行列rank10をlocal ring Q[D,D^-1,(1+2D²)^-1]上で証明すること。H3ではtraceからpositiveB3dim10が既知なので、rank10なら全candidateの正常Gを排除でき、三次商の基底平坦性は不要。scratch tangent_functionals_valid.py は汎関数の全四次関係へのannihilationも別に再生する。初期実験ではFracElement.numerを用いる際に定数分母を失う実装不備があったため、その出力は破棄し全係数再検証中。全値結果は未証明、wrong cacheを結果として使わない。新cacheはnum/den両方を保持する。

全値tangent計算は次のv146で完成した。初期の19個の汎関数はh(D)=10D^6−D^4−4D²−1の零点で不足したが、全functionalを飽和して14個を補った33個の明示証明書を保存した。交換子行だけをhで割らず、全四次functionalのannihilation恒等式を再生することが正しい特殊値の検証である。


## 可逆tangentの全D排除（classification-v146）

**全体的なスペクトル制約（classification-v146）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。全(3,1)は正部分の全Jordan型を含めて空。半単純(2,2)/mixed rank2はpure mixedと二rulingを排除し、さらにtangent K可逆部分も全Dで排除。33個のpolynomial quartic functionalの4752恒等式と、66x32交換子行列の九つの10minorのgcd D^12を厳密検証。H3ではpositiveB3dim10なので、rank>=10が全Dunitで成立するとpositive三次centralizerは零、正常Gも零となる。従ってrank2の残りはsecant型とtangent K退化c0境界。mixed rank4は正topを零/commutator⊙平方/commutator⊙非退化対称式の三種へ被覆。次はtangent c0境界とsecant全rank strataから正常三次を絞り、rank4三型を判定する。非半単純(2,2)、三固有値以上、単一固有値/CY全被覆、全成分/圏族降下は未完。

原稿thm:h3-order2-22-tangent-fullrank-exclusion。input JSONは33個のQ[D]上quartic functional（even128語の辞書式座標）と九10x10 minorの位置を持つ。六関係を前後の二語で挟んだ全144 even quartic relationsへの4752 exact annihilation identitiesを確認。三関係を2D倍してFracElementを使わずQ[D]で直接検証し、定数分母もnum/den両方から復元する。positive cubic32語のx/y交換子にfunctionalを適用したN66x32について九minorは次数80,82,81,84,70,82,75,83,73、monic gcd D^12。ゆえ全Dunitでrank>=10。H3/指定AS4のtraceB3=0からpositiveB3dim10で、positive cubic relation dim22はkerN内、rank>=10からkerNと一致、positive cubic centralizer0。正常Gはmu固定かつcommx/yなので全値で排除。D1等の有限標本は証明に用いず、九exact polynomial minorsのgcdが全値coverを与える。

再現：python computations/verify_cubic_order2_22_tangent_exclusion.py。入力 computations/cubic_order2_22_tangent_annihilator_input.json、出力certificate同prefix。python-flint高速backend（PYTHONPATH=/workspace/work/python-deps SYMPY_GROUND_TYPES=flint）で今回PASS、通常SymPy backendでも今回再実行PASS。汎関数の構成に使ったh-rootのfield linear algebraやgeneric rrefを信頼入力にはせず、全33functionalと九minorを元の六関係から直接点検する。全AS4存在や全H3被覆をこの排除から主張しない。

次の具体的着手：tangent c0ではg upper/ad1、K=[[-b,d,a,0],[a,0,0,0],[-d,0,0,0],[0,0,0,0]] rank2。purepositive rowyy=(B,D,-D,0)とd*rowxy+a*rowyxがpureUU関係で、そのspan<=1/rankone禁止を使ってeven rank4を分岐する。これらから共通positive AS2平面又は正規一次方向を得られるか検証する。secant allunit Schur式は既存の未公表scratch必要条件だけであり、全rank strataを残す。全rank4/nonsemi/他スペクトルは未解決。


## tangent退化境界も排除、rank2はsecantのみ（classification-v147）

**全体的なスペクトル制約（classification-v147）**：全(1,3)は被覆・必要十分H3判定・全矢・DM4表示stack・慣性まで確定。全(3,1)は全Jordan型込みで空。半単純(2,2)/mixed rank2はpure mixed/二ruling/全tangentを排除し、secantだけが残る。tangent K可逆は33functional/九minor gcd D^12で全値排除。c0境界はyy縮約q=(B,D,-D,0)が零ならdomain消去で余分なodd quadを強制しAS4外、非零ならg=epsilon I,B0、Schurからxycomm/uvantiと二平方式へ。四平方が中央となり、W=yu+epsilon*uy,N=yv−epsilon*vyの積は−mu正規化かつmu固定、正常Gと可換/反可換してH3排除。mixed rank4は正top三型へ被覆。次はsecant全rank strataの正常三次を判定し、rank4三型を扱う。非半単純(2,2)、三固有値以上、単一固有値/CY全被覆、全成分/圏族降下は未完。

原稿thm:h3-order2-22-tangent-total-exclusion。c0/ad1のpureUU rows q=(B,D,-D,0),r=(A(d−a),dC−aB,−dB−aC,D(d−a))のspan<=1/rankone禁止を使う。qnonzeroはDunit、minorD²(d−a)と−2aBDからa=d=epsilon±1/B0、vのu移動でgraphb0。q0はB=D0で、C0だとA(d−a)xx purequadからA(d−a)0、evenUUprojection<=2でpureVVquad>=2のdomain矛盾。Cunitならu²=−a^-1*x(Ax+Cy),ux=−a^-1xu、uとu²可換からxをdomain消去しuy+a yu+(A/C)(a−a^-1)xu0というv無しodd quadを得るが、元odd2本の片方はxv係数unitなので新関係、AS4外。

Dunit branchはKepsilonI、evenHの(yy,xy,xx,uv)minorD²、SchurはnegativeQのa0=c0=d0=f0=0。negativeprojection>=3からe0unit、uv+vu0。positivecommとu²=−epsilon(Ax²+Cxy+Dy²),v²=−epsilon/e0*x²−b0/e0*u²、yshiftC0で必要表示。xu=−epsilon ux、xv−epsilon vx=−(yu+epsilon uy)、uvanti、u²=alpha x²+delta y²,v²=beta x²+gamma y²,delta*(alpha gamma−beta delta)unit。x²centralはxT=−epsilon Txより、u²centralはpositivecommとuvantiより、deltaunitでy²central、v²もcentral。W=yu+epsilon uy,N=yv−epsilon vyはB2非零、normalizersそれぞれ(-epsilon,epsilon,epsilon,-epsilon),(epsilon,-epsilon,epsilon,-epsilon)、双方mu eigen−なのでM=WNはmu固定かつnormalizer−mu。GはMと可換、Mはdegree3/muGfixedからGと反可換し矛盾。

verify_cubic_order2_22_tangent_boundary.py/certificateで二minor、Schur全係数constant matrix rank4、両epsilonのnormal covariance全八式を中心平方+三quadratic関係のdegree3 freeword行恒等式としてexact PASS。新規as4結果は輸入せず独立に境界を排除した。Zhang twistによるG正規化の変化を無視せず、この証明は両符号を直接扱う。

次はsecant gdet−1全strata。allunitでKdet非零のSchur必要式は既存scratchのとおり、rank低下a/b/c/d0を別に保持する。tangentを再開せず、正常四次元Mで−muを実現できるか、又は四次annihilatorのexact minor coverで正常Gを排除する。全rank4/nonsemi/他スペクトルと全族降下は依然未完。


## secant全退化境界の四graph被覆（classification-v148）

**全体的なスペクトル制約（classification-v148）**：全(1,3)は幾何学的被覆・必要十分H3判定・全矢/慣性まで確定、全(3,1)は全Jordan型込みで空。半単純(2,2)/mixed rank2はpure mixed/二ruling/全tangentを排除しsecantのみ。secant gdet−1のKはdet−abcd、退化全境界をtorus尺度と同時交換で四固定graph（rank2二種/rank3二種）へ全被覆した。K可逆部分は別に残す。次は四境界のうちrank2二種の正規二次/四次障害を厳密検証し、全係数even Schur条件と正常Gを判定する。rank4三型、非半単純(2,2)、三固有値以上、全CY被覆、全成分/圏族降下は未完。

原稿prop:h3-order2-22-secant-degenerate-strata。gen尺度はg(a,b,c,d)->g(r a,s b,c/s,d/r)、simultaneous x/y,u/v swapはa/d,b/c交換。K sparseのdet−abcd、rank=非零成分数。ad−bc−1から退化はzero2 diagonal/offdiag又はzero1の二軌道で、四固定gはdiag(1,-1),swap,[[0,1],[1,1]],[[1,0],[1,-1]]。verify_cubic_order2_22_secant_strata.py/certificate exact PASS。全境界AS4/H3排除はこの命題から主張しない。

rank2二境界の証明案はv149で全係数検証・原稿統合を完了した。以下の現行定理と証明書を参照し、未検証案を別に再実行しない。

有用な反省：secant sample(s=3/4,t=5/4,A0,C=sqrt(-34)/3)のpositiveU³はexact rank8であり、purepositive quartic topの縮約をT(U)の三次関係と同一視してはならない。T(U) cubicAS3仮説は破棄、実際のB degree3 quotientで点検する。as4 mainHEAD75a32fea51b61d976c7d5b54b91adca7ea8b211cを照会したが、新規結果輸入は行っていない。


## secant K rank2の二境界も全排除（classification-v149）

**全体的なスペクトル制約（classification-v149）**：全(1,3)は幾何学的被覆・必要十分H3判定・全矢/慣性まで確定、全(3,1)は全Jordan型込みで空。半単純(2,2)/mixed rank2はpure mixed/二ruling/全tangentに加え、secant K rank2の二固定graphも全排除。diag(1,-1)は純正縮約から二分枝、Schur/domainでuvが全生成元反転となる分枝と、q=+-iでM=x²y²が−mu正規化となる分枝で排除。swap graphはeven Schurからu²=v²、xy/{uv}中心。AD0は余分なodd quadでAS4外、ADunitは基底変更後の四平方中心と二paired正規二次式の積−muで排除。残るrank2候補はsecant K rank3二表示とK rank4開部分。mixed rank4三型、非半単純(2,2)、三固有値以上、全CY被覆、全成分/圏族降下は未完。

原稿lem:h3-order2-fixed-normal-obstruction,thm:h3-order2-22-secant-rank2-exclusion。mu固定の非零正規元Mが全生成元反転又は−muを正規化すれば、Gと可換/反可換して矛盾。diag graphのpureUU xy/yx rowsはAB=AC=DB=DC=B²+C²0を強制し、domainからB=C0/ADunitかA=D0/Bunit/C²=-B²。前者のSchurはnegativea=c=f0,b(A+D)=e(A+D)=d(A²+D²)0。domain negativeprojection>=3はb又はeunitを強制しA=-D/d0、uv=-vu、N=uvは全4gen反転かつmu固定。後者はpositive yx=zeta xy,zeta²−1、uv=-B y²,vu=-B x²、odd/associativityでu/vがx²,y²を交換。x²y²はpositive反転/negative固定=−muかつmu固定。両方H3排除。

swap graphはpureUU xx/yy 2minor−B²からB0、A/D両0はprojection<=2でdomain外。Aunitを交換で覆い、Schurはnegativec=d0,f=-a,e=-b、domainからbunit。u²=v²=-Q(U)が中心、xy=a u²+b{uv}よりxy/{uv}も中心、A x²+D y²中心。AD0はx²central等から新odd ux+xv0をdomain消去で得てB2矛盾。ADunitでp=sqrtA*x+sqrtD*y,q=sqrtA*x−sqrtD*y,r=u+v,s=u−vの全4平方中心、odd {r,q}=[s,p],{r,p}=[s,q]。W=[s,p],N=[s,q]はmu奇正規二次、normalizers(-,+,+,-),(+,-,+,-)、積mu固定/-mu正規化で排除。

verify_cubic_order2_22_secant_rank2.py/certificateは全係数の縮約ideal/両Schur条件、diag uv全反可換式、四平方交換式、swap pairednormalquad全八covarianceをexact PASS。有限標本や全AS4存在を入力にしない。次はsecant K rank3二固定graphのpureUU一行とpureVV一行から必要Schur領域を分け、B2整域性又は正規二次/四次障害を求める。K rank4開部分は別に残す。


## secant K rank3も全排除、rank2候補は可逆secantだけ（classification-v150）

**全体的なスペクトル制約（classification-v150）**：全(1,3)は幾何学的被覆・必要十分H3判定・全矢/慣性まで確定、全(3,1)は全Jordan型込みで空。半単純(2,2)/mixed rank2は全pencilからpure mixed/二ruling/全tangent/secant K rank2を排除し、さらにsecant K rank3二表示もAS4整域自体から排除。one-diagonal-zeroはdomain二次消去と非退化Pのcyclic Schur二式が矛盾。one-offdiagonal-zeroはpositiveAS2 T、vx=yv,v²/uv∈T2から分数環二次拡大へ落ち、次数0は非自明P1対合のノルム全射により曲線体となるのでB GK<=2、14641に矛盾。従って残る半単純(2,2)/mixed rank2はK可逆secantのall abcdunit開部分のみ。mixed rank4三型、非半単純(2,2)、三固有値以上、全CY被覆、全成分/圏族降下は未完。

原稿lem:h3-AS2-partial-root-growth,thm:h3-order2-22-secant-rank3-exclusion,cor:h3-order2-22-only-invertible-secant。one-diagonal-zero g[[0,1],[1,1]]のpureyy rowは(B,D,-D,0)。D0はdomainB0、v²=-x(Ax+Cy),vx=-xu,uy+yv+vx0からvとv²可換を使いx消去でA(ux+xv)+Cxu0。Aunitは独立odd quad、A0/Cunitはproduct0、A=C0はv²0。DunitならB0はuv0を強制、ゆえBunit。K^tはxx/xy/yx、Pxy行DyyからevenprojectionUU full4でP可逆。negativecyclicSchur二式BD(B−C)=BD(B+C)0が矛盾。

one-offdiagonal-zero g[[1,0],[1,-1]]ではpureyx q非零nondeg、AS2 Tがfactor lemmaでBへ単射、vx=yv,v²,uv∈T2非零。D=QgrT=K[x±;sigma],K=k(t)。f=Ad_vはf x=y,f y=QxQ^-1,Q=v²でDへ入り、f² innerQなのでfD=D。E=D+Dv、w=vx^-1、E0=K+Kw、phi=f_K sigma^-1は対合、w²h∈Kphi。phi非自明ならPGL2座標phi z=-z、algclosed factorizationとNorm(z-b)=b²-z²からh=Normr、(r^-1w)²1でdomain矛盾。phiidならE0=L曲線体有限拡大K、E=L[x±;theta]、u=(uv)v^-1も入りB全体がcurve graded Laurent内。一般曲線へ拡張したgrowth lemma（極因子の線形成長、h0<=deg+1）でGK<=2。Tsenの新規引用は不要、二次ノルムを初等的に証明。

verify_cubic_order2_22_secant_rank3.py/certificateはcyclic二式、x倍新oddquadの自由環恒等式、AS2 Mobius商/非退化det、norm因子恒等式をexact PASS。分数環と曲線成長は本文構造証明。growth lemmaの一般曲線拡張に伴いverify_cubic_positive3_cone_exclusion.pyも今回再実行PASS。

可逆secantの必要正規形は次節v151で有理graphへ統合した。以前の対称graph(s,t)はrho=s²,ell=−A_old/s,C_new=C_oldによる四重被覆であり、係数体を増やすため計算の正本には使わない。


## 残る可逆secantの有理二次元必要曲面（classification-v151）

**全体的なスペクトル制約（classification-v151）**：全(1,3)は幾何学的被覆・必要十分H3判定・全矢/慣性まで確定、全(3,1)は全Jordan型込みで空。半単純(2,2)/mixed rank2は全退化境界を排除しK可逆secantだけ。この全領域を有理graph g=[[1,1],[rho+1,rho]]へ正規化し、rho*C²+(2rho+1)(2rho*ell²+1)=0、rho(rho+1)(2rho*ell²+rho+1)unitの二次元必要曲面で被覆。P(A,B,C,D)はA=-rho*ell,B1,Dell。曲面の特異点はrho−1/2,C0,ell±1の通常二重点二つだけで、両点はB4dim36によりAS4外。全曲面の正常Gは未分類、次はrho−1/2特殊曲線の全正常核を証明書化し、非共鳴conic chartへ進む。mixed rank4三型、非半単純、三固有値以上、全CY被覆、全成分/圏族降下は未完。

原稿prop:h3-order2-22-secant-open-normalform,prop:h3-order2-22-secant-open-nodes。torusでa=b1、rho=ad,c=rho+1,d=rho。K=[[0,-rho,0,0],[0,0,0,rho+1],[-1,0,0,0],[0,0,1,0]]可逆、positiveBunitを1。Schur二式(1−C)(A+rhoD)=0,(rho+1)(1+C)(A+rhoD)0からA=-rhoD、Dell。残余H=rho*C²+(2rho+1)(2rho*ell²+1)0、rho*detP+(2rho*ell²+rho+1)=H恒等式。base ring UFD/generic conic rank3より必要曲面integral2dim。Jacobianはrho−1/2,C0,ell±1だけ、quadratic matrix det2。両表示をQQ上exact B4計算でeven20/odd16/total36としAS4排除。

非共鳴conicにはell0=1/(2rho),C0=sqrt(-2)*(2rho+1)/(2rho)のrationalpoint。C=C0+k(ell−ell0)でh=−(2rho+1)(sqrt(-2)k+2)/(rho(k²+2(2rho+1)))、ell=ell0+h,C=C0+kh。finitek chartの補点(ell0,-C0)はinversechart、rho−1/2のC0特殊fibreは別に扱う。必要曲面の族/節はintrinsic H3成分やAS4十分性ではない。verify_cubic_order2_22_secant_open.py/certificateが全Schur/有理点chart/二特異点/両B4dim36をexact PASS。

rho−1/2特殊fibreの全値正常核はv152でpublic証明書へ統合して排除済み。private ANP4実験へ戻らず、下記の有理係数verifierを正本とする。


## rho−1/2共鳴曲線の全値排除（classification-v152）

**全体的なスペクトル制約（classification-v152）**：全(1,3)は幾何学的被覆・必要十分H3判定・全矢/慣性まで確定、全(3,1)は全Jordan型込みで空。半単純(2,2)/mixed rank2は全境界を排除し、可逆secantの有理必要曲面rho*C²+(2rho+1)(2rho*ell²+1)=0へ被覆。二nodesはB4dim36でAS4外、さらにrho−1/2特殊曲線も全値H3排除。19functional/2736恒等式と12minorのgcd ell^10*(ell²−3/2)^5で三値まで絞り、ell0/+-sqrt6/2のfull normalizer rank10をexact検算。残る候補はrho(rho+1)(2rho+1)(2rho*ell²+rho+1)unitの滑らかな二次元必要曲面。全曲面正常G/AS4十分性は未分類。次は非共鳴conic chartの正常incidenceと、(2,2)rank2の単冪持上げの消滅を判定する。rank4三型、非半単純rank4、三固有値以上、全CY被覆、全成分/圏族降下は未完。

原稿thm:h3-order2-22-secant-resonant-exclusion。P(ell/2,1,0,ell),K有理、odd xu+uy+vx/2,yv+uy−vx/2。input JSONにQ[ell]上19quartic functionalと12maximalminor位置。全144 even quartic relationsへの2736 annihilation identities PASS、38x32 x/y commutator matrixの12 ten-minor gcd monic ell^10*(ell²−3/2)^5（degrees26,37,41,37,41,37,38,40,46,35,32,37）。したがってell0とell²3/2以外rank>=10、H3positiveB3dim10から正三次centralizer0。全残余三値をQQ(sqrt6)上exact検証：ell0とsqrt6/2でevenB3 10,evenB4 19,oddB4 16、full designatednormalizer rank10、negativeconjugateもfield embeddingで同時被覆。有限標本ではなくminor全零点を完全に処理。

再現python computations/verify_cubic_order2_22_secant_resonant.py、入力cubic_order2_22_secant_resonant_input.json、同prefixcertificate。今回通常SymPy backendでPASS。rho特殊fibre全点を排除したので残る必要曲面はsmooth nonresonantconic部分、AS4十分性/H3認識と全正常核は未解決。

単冪持上げの補題案はv153で証明・全stabilizer検証を完了した。右twistの指数−4を用い、Gを輸送せずAutCの単冪を排除する。下記現行定理を参照。


## (2,2) mixed rank2の全Jordan型も半単純（classification-v153）

**全体的なスペクトル制約（classification-v172）**：全(1,3)は幾何学的被覆・H3必要十分条件・全矢まで確定、全(3,1)は全Jordan型込みで空。(2,2) mixed rank2も全Jordan型込みで空。mixed rank4のcanonical正top P0全体は、退化境界と全Jordan型込みで固定非CY符号族へ完全に幾何学的認識、一般dim2/inertia mu2²。未知の(2,2)は正top非零のcomm⊙平方/comm⊙非退化quadの二型だけ。非退化型のJordanはなく、平方型の非半単純には正側Jordanが必要。三固有値以上、全CY被覆、全成分・intrinsic族降下は未完。

原稿lem:h3-order2-22-rank2-unipotent-rigidity,thm:h3-order2-22-rank2-no-Jordan,cor:h3-order2-22-rank2-all-Jordan-coverage。必要pencil被覆/必要Schur正規化はG存在を使わずnoeth quadratic Koszul AS4 domainにも有効であることを明示。H commute muC unipotentならU/Vを保つ。puremixedはpI/qdiag(1,z),z−1,+-iの両lineをpointwise固定し、T^t q=q T^t、simple eigenでTdiagonalunipotentId。secant Eの二rankone点はconnected unipotent closureでpointwise固定、両U/VaxesよりHId。tangentはx/u固定,y->y+beta x,v->v+eta u。E/F uppermatP(beta+eta),Q(beta−eta)、gJ固定はbeta=eta0、gepsilonI固定はeta0。後者のdomain必要関係u²=alpha x²+delta y²,deltaunitとpositivecommから2delta beta xy+delta beta²x²0でbeta0。rulingはAS4domain外。全caseでHId。

元Bでmu=muSs muU、blocks2+2なのでN=muU−I,N²0。H=I+N/4は整数nでI+nN=muU^nのrelation保存がpolynomialnとして全nへ延長されautoB、H4muU。右twist C=B^Hはnoeth/Koszul/AS4/domainを保存しmuC=muB H^-4=muSs、oddRdim2もid⊗H^-1で保存。HはC autoかつmuCと可換unipotentなのでrigidityからHId、muUsemi消滅。G輸送/右twist後のH3性は使わない。RRZ既存右twist公式を明示し新規as4被覆は輸入しない。

verify_cubic_order2_22_rank2_unipotent.py/certificateが両tangent upper stabilizer、puremixed centralizer、square-invariance、二Jordanblockのfourth-root/−4 formulaをexact PASS。既存必要被覆のG非依存性とfinite rank1点への単冪作用は本文構造証明。これで(2,2) mixed rank2の非半単純残余はなく、mu1±のこの領域は全てv151–152の必要曲面へ。mixed rank4/Jordanと他スペクトルは依然未分類。


## 可逆secantの全値排除（classification-v157）

**全体的なスペクトル制約（classification-v157）**：全(1,3)は幾何学的被覆・必要十分H3判定・全矢/慣性まで確定、全(3,1)は全Jordan型込みで空。(2,2)のmixed rank2も全Jordan型込みで空と確定した。最後の可逆secant必要曲面は七多項式四次汎関数の1008恒等式と単一10minor −2ell^15*rho^20*(rho+1)^15*(2rho+1)^2により全値排除し、ell0/共鳴fibreも既存全値検証で覆う。従って(2,2)はmixed rank4のみが残る。次は正top三型（零・comm⊙平方・comm⊙非退化quad）と全Jordan型の必要表示・正常三次を調べる。三固有値以上、全CY被覆、全成分/圏族降下は未完。

検証器 verify_cubic_order2_22_secant_surface.py と39KB入力は七汎関数のみを保持し、1008多項式消滅恒等式と14x32交換子行列の単一10minorを再生する。曲面式Hを法にdet=−2ell^15*rho^20*(rho+1)^15*(2rho+1)^2。恒等式は整域の分数体で計算するが、元のminorは多項式なので全特殊値へ適用され、途中pivot零点を例外扱いしない。rho(rho+1)ell(2rho+1)unitで核次元22。ell0とrho−1/2は既存の全値証明を使い、C0排除は独立な整合検算として保持する。従って半単純rank2全空、単冪剛性/右twist−4により全Jordan型も空。

可逆secantのgraded包絡矢Phiとrho/ell不変性は実際のAS4点に関する補助結果として保持するが、この領域にH3点の存在は主張しない。独立査読・新規性確認は未実施。追加のas4結果は輸入していない。

**次の核心（classification-v158）**：(2,2) mixed rank4で正top非零の場合、正平面を固定する片側単冪作用はH3から排除した。負固定VVは<u²,[u,v]>、cyclic Qと偶rank2から負射影line。u²-onlyはPBW三次21でAS4外、comm成分unitはT[u;f][v;sigma,delta]、Tcomm又はq−1へ還元。実際のNakからf²=muT,hdetf−1。commは正常Gが正規一次式yで割れ、q−1は正三次正常核零。従って非退化正topの全Jordan部分が消滅。平方topの非半単純候補は正側Jordan非零が必要。零top・平方topの正側Jordanと半単純rank4の正常incidence/許容性は未解決。

## rank4負topの必要五形（classification-v159）

半単純(2,2) mixed rank4の負cyclic二元topはrank<=2なので、零・第四乗・対称secant(u4+v4)・対称tangent(symu3v)・非対称(uvuv+vuvu)の五形で全被覆した。対称/交代分解とapolar二次核の二根/重根で証明。正top零なら第四乗は整域性で排除、Q零では偶関係が純正/純負非退化quad二本へ分裂、Qrank2では純負AS2平面が一本現れ、対称二型はq−1、非対称型はq±iに限る。混合奇関係と正常三次・admissibilityは未判定。

証明は cubic_order2_22_rank4_negative_top.tex。五形のrankと対称/交代分解をverify_cubic_order2_22_rank4_negative_top.pyで検証。P0でevenmiddleをr1⊙r2と分解し、P0から片方を純負関係に取る。Q1なら純負関係が平方で矛盾。Q2の二因子u²±iv²、u²/uv+vu、uv±ivuを読み、非退化二元関係の因数分解からAS2埋込みを得る。次はこの負平面に対するmixed四関係と正常Gを認識する。


## rank4奇graphの全二分法（classification-v160）

半単純(2,2) mixed rank4の奇関係は、可逆四次元graph(det=-1)か、純UV/VU非退化関係を一本ずつ持つ両射影rank3型の二択で全被覆。部分転置PfD=-PfAと四次元交代像・整域性で証明。正top零のgraph型では、正二次射影が非退化なら負AS2平面上のPBW double Ore表示へ認識。負top零ではこの条件は自動かつtail0、負rank2ではbase q−1又はq±i。退化正射影は別分枝として保持し、全graphやpairedpureを既知doubleOre分類で覆ったと主張しない。

O=[[A,B],[-B^t,D]]、rankO4、DはAのcyclic部分転置。純UV/VU関係空間はdomainよりdim<=1、従って両射影rank>=3。射影rank4なら主交代block rank4、rank3ならrank2。Pf恒等式より両射影は同時に4又は3。fullgraphはD=-B^t A^-1B、detB=-PfA²、detgraph=-1。P0graphと非退化正射影では6quadのmonic簡約が三次20語を持ち、実際のdimB3=20から全三次overlap0、DiamondでPBW。退化正射影のrank1行列は積又は平方であり、この認識に含めない。次は最小tail0 chartから正常三次を計算する。


## rank4可換正平面separated chart（classification-v161）

正平面可換・負二生成元がそれぞれ正平面を正規化するseparated chartを、量子/Jordan負平面とも全H3判定した。量子型は全F∈GL2のB(F):ut=F(t)u,vt=F^-1(t)v,vu=−det(F)uv。全AS4とmu++--、正正常核はker(Sym³F+I) +ker(F−detF I)uv、F²Iの場合だけker(F+I)u²/v²を加える。全Fで因数分解を追うとH3はF−Iの既知符号包絡だけ。Jordan負平面も反射Fを強制し、Gが正規一次式で割れるため全排除。一般mixed graph/正側非可換/純mixed二本型の全被覆は未完。

F²IはI/−I/反射の三択、正常核次元2/8/5。F²neqIではdet(F−DI)=Ddet(F−I)、固有値1がなければ純二元三次のみで因数分解、固有値1が単純なら全Gが他方の固有一次式で割れる、unipotent重根ならG=linear*uv。Jordan負平面はgf=fg=f²からg=f、muU=f^-2, muu=detf*uによりf反射、正規yで商を取って微分Ore内の反交換不可能性を使う。既知符号包絡の全幾何学的矢/判定へ接合し、新成分とはしない。

as4 a3ddc8c55e65f336f707ebba5810b26d0698712eのREADME/plan/COVERAGE/CLAIMSを入口監査し、1049主張からmixed(2,2)/twisted tensor/double Oreを検索した。今回分枝を覆う主張は確認せず、新しい数学的輸入はゼロ。入口sha256と範囲はas4_imports.json。既存輸入commitは更新しない。

 さらに可換正平面separated chartの全Jordan型も閉じた。量子負平面でμU=(fg)^−1、fg単冪、負μは厳密に−1。fg≠IならG30零、u²/v²成分が非零ならf=g、そうでなければG=linear*uv。f=gでは±単冪の一次固有直線が全係数の共通因子となる。従って非半単純を含め、このchartのH3は既知符号包絡のみ。


## 二AS2平面separated chartの全認識（classification-v162）

二AS2平面のseparated graphを全Jordan型込みで幾何学的H3認識した。可換正平面はv161、非可換正量子平面は対角作用なら全skew分類で空、q−1反対角作用は正常核零、Jordan負平面でもmuTとの一次絡み合わせ零から純二元三次の因数分解で排除。Jordan正平面では中山単冪shearの固定核kx^n又は一次normalizer条件から全Gがxで割れ、Jordan/Jordanは固有値自体が矛盾。従ってこのchartの全H3は既知非CY符号包絡のみ。一般negative-generator mixing graph、純mixed二本型、非零topや全相対降下は未完。

半単純(2,2) mixed rank4のP=Q=0領域で、K=vec(a)vec(b)^t、a/bは非退化AS2関係、cross M=−(a^t⊗b)flipで可逆。従って全奇関係はfullgraph、pairedpure分枝なし。PfA=h=eps*det(a)det(b)、A#=PfA A^-1線型よりh*tau(A)+M^t A#M=0の六線型必要atlasを得た。QQ/QJ/JQ/JJ両符号八chartの局所化多項式イデアル一致を検証し、p/q±1特殊値を全保持。半単純JJ両分枝はPf0で不存在。全AS4十分性・全H3被覆・全非半単純は未主張。


## 零top atlasの次の具体的計算

QQ p=q−1,eps+ではz2=z3=0、z0z5−z1z4=1。二対角torusとU/V軸交換で、両組成分が非零ならz0=z1=1,z4=t,z5=t+1へ正規化できる。公開verify_cubic_order2_22_rank4_zero_top_QQ_plus.pyで四PBW overlap全恒等0、54x10正常行列の指定minor定数−4を再生済み。QQ eps+全分枝は三chart/四minorで排除した。片組が零の境界は二方向separated。QQ p=q1 eps−はΛ²(U⊗V)=Sym²U⊗Λ²V + Λ²U⊗Sym²Vの二対称式へ分かれ、Pfneq0なら少なくとも一方非退化。GL2でその対称式をcrossへ移し、一方向separatedへ還元できそうである（未検証）。opposite-separatedも負comm/Jordanとq−1反対角を因子/centreで排除できそうだが、完全な変換と全Jordan輸送は未証明。これらを済ませる前にP=Q0全H3を既知符号だけと結論しない。


## QQ正Pfaffian分枝の全排除（classification-v164）

零top QQ atlasのeps+全分枝をH3排除した。線型式/Pf非零からp−1又はq−1。二つの片側chartと交点SL2四係数を対角二torus/軸交換で正規化した全t chartで被覆。三chartの12PBW overlap全恒等0、正正常行列の四10minorは−8(t+1)²/t9、8(t−1)²/t9、1、−4。Bezoutで第一chartの全t非零を覆い、他chartは定数minor。交点の非分離族t0/t−1含む全境界を処理した。eps−とQJ/JQ、元非半単純への輸送は未完。


## opposite-separated量子正平面の認識（classification-v165）

正量子二元が負AS2平面をそれぞれ正規化するopposite-separated chartも全Jordan型で認識した。負commは正常二次係数がF/Gの一方Idを強制し、正平面commとなってGが正一次因子で割れる。負quantumの対角作用は既存skew分類、q−1反対角は中心平方と奇数乗から正常核零。負Jordanでは二次intertwiner det=(a+1)^3から例外a−1のみ、正中山式p1と奇偶条件で再び因数分解。従ってこのchartの全H3は固定符号包絡のみ。正Jordanのopposite-separated全体は範囲外。

次の新着想（未採用）：P=Q0 canonical半単純CではA交代4x4が可逆。H_U/H_Vとも非自明単冪ならJ⊗JによるAの固定式は(z0,z1,0,0,0,0)だけでPf0。従ってHは片側のみ。正側単冪のみなら元BのG固定式からAS2次数3/1のshear固定核kx³/kxを使いGがx因子。負側単冪のみならmixedR4がut=f(t)u,vt=f(t)v+d(t)u、pureVquadはcomm+κu²となりOre表示。f²=muT/hdetf−1からTcommは反射でfactor、Tquantum≠1はmuTとの一次intertwiner零で純T3factor、TJordanはhdet符号矛盾。一般P=Q0全Jordan消滅として本文/検証器へ整える。


## canonical零top領域の全Jordan消滅（classification-v166）

canonical半単純untwistがP=Q=0のH3では中山の全Jordan部分が消滅する。可逆交代UV block Aに対して両側非自明単冪J⊗Jの固定式はPf0となり矛盾。片側正JordanのみはmuG固定式のAS2 shear核からGに一次因子。片側負Jordanのみはmixed graph可換環からT[u;f][v;sigma,delta]、f²=muT,hdetf−1となり、comm反射/quantum一次intertwiner/negative hdet符号で全排除。Gのtwist輸送やH3のtwist不変性は仮定しない。

両側単冪Pf0と片側graph[[f,d],[0,f]]、負二次固定空間をverify_cubic_order2_22_rank4_zero_top_unipotent.pyで確認。元Bは逆twistでpureAS2二本/fullgraphを保ち、Hilbert20/PBWでAS2単項式基底を得る。正側単冪のみではmuG固定の係数がkx³/kx。負側のみではvu−uv=κu²、muUId,muu−からf²=muT,hdetf−1。Tcomm反射はnormaly quotient微分Ore、TquantumはG12係数零→T3factor、TJordanはhdet1/−1矛盾。本文に統合済み。


## canonical零topの全幾何学的認識（classification-v167）

canonical零top(P=Q=0) mixed rank4領域の全H3を、全Jordan型・全幾何学的矢込みで既知非CY符号包絡へ認識した。v166全Jordan消滅の後、QQ eps+全排除、QQ eps−のseparated二型と両comm時の二対称式の非退化軸変換、QJ/JQ eps−の同様の軸変換、QJ/JQ eps+の特殊二点正常minor−16/−36、JJ両符号top不存在で八chartを完全被覆。全切断G=f3(U)+ell2(U)u²+ell3(U)v²、H3条件/全矢は固定sign定理へ接合。一般次元2/慣性mu2²。全H3や成分/族降下の完成ではない。

A=SU⊗E+E⊗SV、PfA=detSU−detSV。可換側GL2のnormalized congruenceで非退化対称式をcrossへ移し、全特殊係数をseparatedへ被覆。量子/Jordan正符号特殊点の四overlapと正常minor−16/−36はzero_top_coverage検証器で再生。次はP又はQ非零領域。最小課題として符号graphの曲がった偶関係[x,y]=alpha*u²+beta*v²、uv=-vu、crossantiを調べる。u²/v²/uvの偶Clifford係数上のWeyl関係から、alpha/beta非零なら正三次のx/y中央化核が零となりそうである（未検証）。


## 曲がった対角rank4包絡の正常核（classification-v168）

非零負topへ出る対角curved包絡[x,y]=alpha*u²+beta*v²、uv=-vu、u作用diag(lambda,lambda^-1)、v逆作用を全値でAS4/noeth/Koszul/domain・mu++--と認識した。全正常正三次核も判定。lambda±1の非零curvatureはWeyl中央化核零、lambda1零tailはfactor、lambda−1零tailは既知sign。新候補は原始6乗根lambda²−lambda+1=0のG=A x³+B y³、AB非零・tail非零だけで、正常核は全alpha/betaで厳密に2次元。商は正規正則AS-Gorenstein/μRIdだが、商domainとH3許容性は未判定。

原始6乗根curved候補G=A x³+B y³も全alpha/betaで非整域と判定した。u/x逆転chartはk[C,V]上のorder6 GWA、a0=C−delta−gammaV²、3norm P=C³−delta³−gamma³V6−3delta gamma C V²。cutをX6=r³Pへ直し、sigma²の3normもPであるためZ=(r a0)^−1 X²がZ³1。monic6基底上でZ−1とZ²+Z+1がともに非零かつ零積なのでdomain仮定に矛盾する。従って対角curved全chartのH3は零tail/F−Iの既知signのみ。全非零toprank4の完成ではない。


## 原始6乗根normal cutの全非整域性（classification-v169）

原始6乗根curved候補G=A x³+B y³も全alpha/betaで非整域と判定した。u/x逆転chartはk[C,V]上のorder6 GWA、a0=C−delta−gammaV²、3norm P=C³−delta³−gamma³V6−3delta gamma C V²。cutをX6=r³Pへ直し、sigma²の3normもPであるためZ=(r a0)^−1 X²がZ³1。monic6基底上でZ−1とZ²+Z+1がともに非零かつ零積なのでdomain仮定に矛盾する。従って対角curved全chartのH3は零tail/F−Iの既知signのみ。全非零toprank4の完成ではない。

局所化前後のbase単射はGWAのLaurent/monic6基底で証明する。K=k(C,V)へは非零係数のsigma6normという中心元を逆転して移る。r³=−B/A、X6=r³P。sigma³a0=a0によりsigma²norm3=P、Z³1。Lの係数field上の支持{0,2}/{0,2,4}が両因子の非零を保証する。次数2の部分crossed productだけを見てRのdomainを予想するのは誤りであり、実際の3normが全候補を排除した。頂点Extやaffineglを調べる必要はこの候補ではなくなった。次は非対角F=±Jのcurved chart：positive shear invariantsのU次数filtrationでGが共通一次因子を持ちそうである（未証明）。


## 曲がった量子対角chartの全H3認識（classification-v170）

正射影量子二次式を許す全二パラメータcurved対角包絡xy−p yx=alpha*u²+beta*v²、uv−、u作用diag(r,r^-1)、v作用diag(p/r,r/p)を全係数AS4/noeth/Koszul/domain・mu++--と認識し、H3はp1,r−1,alpha/beta0の既知signのみと判定。十語の二normalizer weightイデアルから例外はp1r±1とp³1/r³−1の九根のみ。九根でcurvature制約を全判定し、GWAのperiod3a0/monic6商で三次norm零因子を構成して全非sign候補を排除した。

一般norm補題：K可換field、sigma6Id、a0!=0/sigma³a0=a0、P=a0*sigmaa0*sigma²a0、rho≠0 fixedならL=K[X±;sigma]/(X6−rho³P)にはZ=(rho a0)^−1X²,Z³1の零因子。sigmaの最小位数は問わない。全根p³1,r³−1ではdehom t=p r²,c=−p/r²、XY−tYX=r alpha−r beta V²。delta(t−1)=r alpha、gamma(c^-2−t)=r betaを選べることが三次centralizer方程式の全条件。次はF=±Jordanのcurved comm射影をU次数filtration/shear固定核で因数分解へ帰着する。


## 全SL2 curved normalizing chart（classification-v171）

全F∈SL2のcurved normalizing包絡[x,y]=alpha*u²+beta*v²、uv−、u作用F/v逆作用を、非対角±Jordan込みでH3認識した。全閉detF1で4PBW overlap、curvatureを純負cyclic quarticで加えるKoszul-Frobenius topからmu++--。非対角±Jの正三次shear核は全alpha/betaで定数minor6、必要Gはxuv又はx*(c x²+d u²+e v²)に限り因数分解。対角は既証3norm排除へ接合し、H3はF−I/零curvatureの既知signのみ。

canonical正top P=0の(2,2)/mixed rank4全H3を、全Jordan型・全幾何学的矢込みで既知非CY符号族に認識した。P0の正二次射影がrank1ならcross M rank2/rulingとなり、奇交代4像の純UV直線がimMに入って積関係を強制するためAS4domain外。正射影は自動非退化。Q0は既知zero-top認識、Q非零では負base q−1/±i、H_V単冪Id/正側shear固定G因子で全Jordan消滅。eps+はfiltered正常核零、eps−は対角量子/全SL2/Jordan正射影/四乗根weightを全被覆し非零Qを全排除。全H3は既知sign、一般dim2/inertia mu2²。


## canonical正top零の全認識（classification-v172）

canonical正top P=0の(2,2)/mixed rank4全H3を、全Jordan型・全幾何学的矢込みで既知非CY符号族に認識した。P0の正二次射影がrank1ならcross M rank2/rulingとなり、奇交代4像の純UV直線がimMに入って積関係を強制するためAS4domain外。正射影は自動非退化。Q0は既知zero-top認識、Q非零では負base q−1/±i、H_V単冪Id/正側shear固定G因子で全Jordan消滅。eps+はfiltered正常核零、eps−は対角量子/全SL2/Jordan正射影/四乗根weightを全被覆し非零Qを全排除。全H3は既知sign、一般dim2/inertia mu2²。

rank2 cross補題：O=T Omega T^tの4次元交代像、L/N二射影rank>=3、rankM2なら両射影rank3。ell=kerNは等方直線なので純UV線Lell⊂L(ell perp)=imM。正projection rank1ならM=−(a^t⊗b)flipの像は固定正因子rulingで、純UV関係が積になる。従ってrank1境界も存在せずP0の非退化仮定は不要。標準3x3 minor det=z3 PfOmegaとPfOmega*e1=z5 col1−z4 col2が有限検算。

全非零Qの被覆ではcyclic cはq−1ならsquares、q±iならuv+qvu。正projection quantum p≠1はF/G対角、p1はdetF=−q^-1の全行列、JordanはF反復eig a²=−q^-1。q−1は既存curved quantum diagonal/fullSL2/shear384、q±iは10weight/28disjoint/primitive8 no−eig。全パラメータの境界を保つ。次はP非zero、まずQ0のClifford型{u,v}=quadratic(U)とcrossantiを、既存Clifford swap結果との重なりを確認して認識する。全rank4正top非零の被覆は未完。


## 正top非零Clifford chartのH3判定（classification-v173）

正top非零へ出るClifford型B_h（正側可換/cross反交換/{u,v}=h2）の全包絡AS4/domain/mu++--と八次元正常核を証明。u²/v²係数独立chartではF1上のeven/odd Clifford sheafを復元し、飽和性と例外曲線二節点の非自明quaternionにより全商domain。H3 iff conic総空間smooth iff planequartic reduced/nodalかつ全余分nodeがrank1。h=xy,G=x³+y³+xu²+yv²は厳密Jacobian検算付き実H3例。全正top非零被覆・依存係数境界・全矢/相対降下は未完。

証明：papers/sections/cubic_order2_22_clifford_curved.tex。検証器verify_cubic_order2_22_clifford_curved.pyは全係数四PBW overlap、八正常列零と補空間minor4、scroll determinant恒等式、実例の全射影Jacobianを厳密再生。新規性・独立査読は未確認。既存(1,3)定理を被覆として使用せず、共通局所Clifford補題とH3認識の証明を、今回再構成した束・飽和性・domainに適用した。

独立係数Clifford chartのH3判定と実例を確定した。次はこの族の全幾何学的矢と一般慣性、係数依存境界を判定し、Q0全体への必要被覆を調べる。正top非零全域・三固有値以上・全CY被覆・全成分/族降下は未完。


## 曲がったClifford全切断・全幾何学的矢（classification-v174）

Clifford型B_hの依存係数境界を全排除した。u²中心開集合を三変数skew/cocycle twistへ正確に復元し、依存係数なら対応可換affine曲面に必ず特異点が出る。従って既存独立chartのconic必要十分判定がB_h全体の全H3切断を尽くす。全pointed exact幾何学的矢はGL2U×((Gm)²⋊S2V)のh保存/三次直線保存式、次数Gm商。表示stack一般dim5/慣性mu2、h0は既知dim2/慣性mu2²。全非零正top被覆・成分性・intrinsic相対降下は未完。

新しい検証器verify_cubic_order2_22_clifford_boundary.pyは、X=x/u,Y=y/u,W=v/u+h(X,Y)/2とu反転の全六関係、およびG=-Fu³を非可換順序積で厳密確認。F=f3-alpha*X+beta*X*(W²-h²/4)は有限(Z2)² cocycle twistと可換曲面を比較でき、alpha=beta*c²なら(0,0,c)は全偏微分零。全幾何学的矢の証明と一般慣性計算は同じClifford節に統合。

次はQ0かつ純正二次関係がcommとなる領域の必要被覆を進める。零top odd線型atlasは偶topの正側curvatureを足しても同じcross/Pfaffian式を持つ見込みで、負側separated一般F・反射・Jordan/両commの反対separatedに還元する。これは未証明の全被覆であり、まず各curved包絡の正常因子判定を個別に証明する。


## 全逆行列normalizing包絡のClifford認識（classification-v175）

曲がったClifford全切断・全幾何学的矢の分類に加え、全F∈GL2の逆行列normalizing Ore包絡B(F,h)を全hでAS4/domain/mu++--と認識した。F²非Idでは正常条件をF固有直線商へ移して全G因数分解、FId核はL*(uv-h/2)、reflectionも定数minor16で共通一次因子を強制。従ってこの全行列族のH3はF−IdのClifford族に尽きる。B_hは係数独立/conic平滑の必要十分条件、全矢、一般dim5/慣性mu2まで確定。

B(F,h): positivecomm,u作用F/v逆作用,vu=-detF*uv+detF*h。F²neqIdではG=f3+Luv、FL=detF*L、(1+Sym³F)f3=-detF*L*Fh。Lneq0なら商U/kL上FIdで2f3=0、従ってLが共通因子。L0はbinarycubicfactor。FId核二列と補minor256、reflectionの非因子四列minor16（残る六列は指定四行零）をverify_cubic_order2_22_clifford_matrix.pyで検算。全Fの四PBW overlapも検算。

次は半単純Q0で純正二次関係がcommとなる全領域の必要被覆。odd線型atlasからq≠1負separatedは今回のB(F,h)へ。残りはq−1 eps+のswap cross、負Jordanの明示shear cross、両comm時の反対separated f*g=−Id。これらの正常核/因子を全係数で確認して必要被覆を閉じる。全非零正top・全CY・三固有値/成分/相対降下は未完。


## canonical負top零の完全な幾何学的認識（classification-v177）

canonical負topQ0の(2,2)/mixed rank4全H3を、全Jordan型込みで曲がったClifford族B_hに幾何学的認識した。半単純pure-positivecommの全odd atlasを一般F/swap/Jordan/両comm反対separatedへ必要被覆。pure-positive symmetric枝はp−1全atlasで正常核零又は一次因子。非半単純は非退化P/両JordanPf0/負片側/正片側固定核minor6で全排除。全切断は係数独立/conic平滑、全幾何学的矢、一般dim5/慣性mu2、h0符号部分族まで確定。

証明はcubic_order2_22_Qzero_commutative.texとcubic_order2_22_Qzero_complete.tex。新検証器Qzero_commutativeはswap正常rank10 minor4、負Jordan非x列minor16、両comm反対separatedのSL2全PBW/二scalar minor16とgraph辞書を再生。Qzero_completeは正対称分枝の四localized ideal一致、負Jordan Sym² fixed determinant−8二つ、両comm Sym²の2I恒等式、正片側Jordan yx=xy+eta*x²の全eta固定核補minor6を再生。従来zero-top eps+全核零/odd atlas/単冪untwist/片側Jordan排除を仮定付きで適用。Gのtwist輸送は使わず、元BでmuG固定を課す。新規性・独立査読は未確認。

次はcanonical正負top P,Qとも非零の残余。Pはcomm⊙q（q平方又は非退化）、Qはrank≤2 cyclic binaryquartic。まずQrank1がcross rank2 ruling障害でAS4domain外になるか確認し、rank2の三標準形と二本のcoupled even relationsから必要top/正常核を計算する。全CY/三固有値以上/成分/相対降下は未完。


## 両top非零の負rank1排除・tangent負分枝（classification-v178）

正負topとも非零の残余で、負top rank1をcrossのruling障害により全Jordan型のcanonical包絡から排除。負topはrank2三型に限定。tangent型は二つのisotropic-factor割当てを区別し、六つの可逆cross線型atlasと逆割当て平方型のrank2 cross境界を確定。第一割当て/負Pfaffianの全半単純領域は、平方型の一軌道正常核零と非退化型全Tneq0の三minor gcdT10により空。正Pfaffian、逆割当て、非半単純tangentは未完。

証明/certificateはcubic_order2_22_tangent_negativeのTeX/Python/JSON。非退化負PfaffianのT-parametrizationは(0,T^-1-T/4,-T/2,T/2,T,0)。元の288四次関係を消す35汎関数はLaurent多項式（分母定数*T冪のみ）であり、全係数恒等式を検証。正自由三次32語への正常式は64x32、多項式三10minor gcdは定数*T10。AS4正三次次元10と合わせ全核零。平方負分枝はz4非零を保存torusで1に正規化するので厳密一点消去が全軌道を覆う。AS4全係数存在、正Pfaffian、逆割当て、非半単純正常G輸送は主張しない。

次はtangent第一割当て正Pfaffian。残余torusでz5neq0は二パラメータmain chart、z5=0はz0=0/1の二一パラメータ境界へ被覆できる。平方型mainの一般quartic消去はNF分母Q*(P+Q)*((P+Q)²-2)、正常10minorは定数*P*(P+Q)^6*((P+Q)²-1)^3*((P+Q)²-2)^5（計算済み・公開certificate未整備）。従って次は有限本の例外直線を全係数で判定する。ランダムな高次数minorのGBは重すぎ中止し、この有限直線分解へ切替。全H3被覆/成分/相対降下は未完。

私的再開計算：/workspace/work/order2_22_rank4/both_top/ にexplore.py,probe.py,ff.py,ff_main.pyと小pickle。これらに依存せず公開verifierは入力から再計算する。ff_mainは平方正main A=(1-PQ,-1/2,P,Q,0,1)。残余z5=0境界A=(epsilon,0,T,T^-1,0,0),epsilon0/1。nondeg正mainはA=(1-PQ,(P-Q)/2,P,Q,0,1)、同境界z1=(T-T^-1)/2。逆nondeg負はA=(0,(T+T^-1)/2,T,-T^-1,0,0)。


## tangent第一割当ての全半単純排除（classification-v179）

負tangent第一割当てcU+u²,qU+uv+vuの全半単純H3を両Pfaffian・全境界込みで排除。正Pfaffianは全FSL2のS(F)[v;sigma,delta]へ必要被覆し、v-filtration grの非零片側curvature正常核を全Fで判定。±Jordan核は定数minor36で零に強化。traceF1のprimitive6共鳴だけ二次元正常核が残るが全Gは三生成元S内、既存三次norm零因子がmonic v商へ埋まるため全非domain。非退化qUはJordanなしなので全Jordan型込みで空。

証明はcubic_order2_22_tangent_plus_Ore.tex。verify_cubic_order2_22_tangent_plus_Ore.pyはqU平方/非退化の二つの全SL2 Ore表示について計8overlap、grの±Jordan二正常10minor36を厳密検証。既存curved_diagonalとprimitive6_nondomainのbeta0を適用。グラフF=[[-z2,z0],[-z5,-z3]]、detF1、grで正常Gがv次数0なら元GもS(F)内。Gv+vGからsigmaG=-G,deltaG0となりS/(G)がB/(G)へ埋まる。従ってfiltered domain性の逆推論やGのtwist輸送は不要。以前の二param main/例外直線計算はこの構造証明に置き換わり、再実行不要。

次はtangent第一割当て平方型の非半単純残余と逆割当て。M可逆の両JordanはPf0、負片側は既知排除。正片側H_U=J,H_VIdのA不変式はz5=0,z2=z3。平方正Pfaffianはz2=z3=±1,z0=0/1へ、平方負は既存一点軌道へ。Gはtwist輸送せず、canonical C3のH固定核がx*C2に入るかを厳密計算し、元BのmuG固定から一次因子を得る方策。逆割当て非退化の二atlas、平方のrank2 tangent cross、負secant/非対称型は未完。全H3/成分/相対降下も未完。


## tangent第一割当ての全Jordan型完全排除（classification-v180）

負tangent第一割当てcU+u²,qU+uv+vuを全Jordan型込みで完全排除。半単純は全SL2 Ore表示/gr正常核とprimitive6三次norm。非半単純平方型はH_UJ/H_VIdのA不変式z5=0,z2=z3から五canonical軌道へ必要被覆し、全軌道でH固定三次4次元が左因子xC2（6次元）へ入ることを厳密計算。muG固定と右twistの同一ベクトル空間/x*B2=xC2により元Bでも一次因子。Gのnormal cutとしてのtwist輸送は使わない。

証明cubic_order2_22_tangent_Jordan.tex。公開verifierは元の六二次関係の全三次商でH作用を計算し、負Pf代表(-1/2,1,0,0,1,0)と正Pf四代表(e,0,epsilon,epsilon,0,0),e0/1,epsilon±1の各4/6/6包含を検証。固定核の包含はshear非零parameterに不変で、保存torusはkxを保つ。muB(G)=G⇒H4G=G⇒HG=G、B=C^(H^-1)のx*B2=xC2で因子を戻す。正常Gの輸送を仮定しない点が重要。

次はtangent逆割当てcU+uv+vu,qU+u²。非退化qUは全Jordanなし/M可逆で二Pfaffian atlas、負分枝はA=(0,(T+T^-1)/2,T,-T^-1,0,0),Tneq0。平方型はcross rank2/tangent pencilで可逆graph法を使えず、奇投影はrank3,3の境界が残る。まず逆非退化負Pfaffianの正常核を全Tで判定し、Ore還元又はLaurent汎関数minor coverを探す。負secant/非対称型、三固有値以上、全CY/成分/相対降下は未完。


## tangent逆非退化の負Pfaffian全排除（classification-v181）

負tangent逆割当て/非退化正top/負Pfaffianを全Tneq0で排除。全graphは正x/yが負Vをf,gでnormalizeしfgId,detf=detg−1。xy,yxがu²/uv+vuを張るので負側Sym²Vが中心。補助x−y次数の奇成分に対しfの奇冪はdet−1でSym²を恒等にできず、包絡domain性と負二次式単射から正常三次が全て零。GWAの全高次被覆や有限標本外挿を使わない。

証明cubic_order2_22_tangent_reverse_minus.tex、検証器は同stemのPython。行列f=[[-T,(T-T^-1)/2],[0,T^-1]],g=[[-T^-1,(T-T^-1)/2],[0,T]]。fgId/det−1と自由負tensor上のf(a)=b,g(b)=a、Sym²FId+detF−1の矛盾idealを検証。補助Z次数は全六二次関係の斉次性から得られ、奇三次成分はx^n*t/y^-n*tへspanningできる。負高次環の普遍PBW性を仮定せず負二次式の単射だけを用いる。

次はtangent逆割当て正Pfaffian。非退化正topのatlasはA=(z0,z1,-z4/2,z4/2,z4,z5), z0z5-z1z4-z4²/4=1。z0=z5=0ではx/y opposite-normalizing,fgId,detf1、正常奇成分はSym²fの有限奇位数共鳴に限る見込み。逆平方型はcross rank2 tangent pencilで別境界。負secant/非対称型、全CY/三固有値/成分/相対降下も未完。


## 逆tangent正Pf共鳴の全正常pencil因数分解（classification-v182）

逆tangent正Pfaffian/非退化正topの共鳴z4=1を全z0,z5境界込みで排除。z5neq0はbeta一param、D=(beta−1)(beta+1)(2beta+1)(4beta+5)非零で正常核2次元、二8minor gcdD²。明示ell*Q2因子identityが正常pencilへ非定数写像を与え、projective比例incidenceのproper閉像から全Dopenのpencilを因数分解。四D例外も元関係でrank8/因子像span2を再検算。軸交換で片零境界を覆い、二重零点はell³−theta*C*ell=x³+theta³y³で全因子化。全正常核零ではなく全cut非domainによる排除。

証明cubic_order2_22_reverse_resonant.tex。公開verifierは元関係の商座標、D外だけに極を持つこと、正常基底二列、二8minor gcdD²、六係数quadratic因子identityを検証。proper incidenceはell,q,c三射影変数に対するL(ell)qとWcのwedge比例式で定義する（直接等式はmultihomogeneousでないので使わない）。形式上零積も許すが、仮定H3の包絡domain性と正二次基底の単射が零積を除く。B3の全係数平坦性を仮定せず、商汎関数rankとH3のHilbert値により当該点で座標を同定。四例外はbeta1/−1/−1/2/−5/4のexact point。二重零点のC=−3u²/4−v²は負中心かつf固定でありnormidentityを全語で検証。新規性/独立査読未確認。

次は逆tangent正Pfaffianの共鳴外z4neq1。z5neq0 mainはA=(1+beta*t+t²/4,beta,-t/2,t/2,t,1)の二param。私的reverse_general.pyで元三次/四次商汎関数と正常rank10を計算中（未公表・全値rankcover未証明）。消去分母と単一minor因子を調べ、必要なら有限例外曲線へ分解する。z5=0は軸交換でz0neq0をmainへ、二重零はopposite-normalizerの奇次数中心作用で直接判定できる見込み。逆平方rank2 tangent cross、負secant/非対称型、全CY/三固有値/成分/相対降下は未完。


## 逆tangent非退化全分枝の全値排除（classification-v183）

逆tangent非退化正topの全正Pfaffianを全値coverで排除。二param正常10minor分子(t−1)²(t+1)²、分母全因子の八例外曲線を新たな商汎関数/二minorで被覆、残り12有理点と二組の二次体共役を厳密再消去。唯一の正常一次元点(beta,t)=(1,−1)も(x−2y)*((x−2y)²+4v²)に分解。t1共鳴は既存全pencil因数分解、二重零境界はodd補助次数とf³−Idのlocalized idealでt1へ。これで負tangent型の未知は逆割当て/平方正topのrank2 tangent crossだけ。

証明cubic_order2_22_reverse_plus_cover.tex。検証器は二param全元関係の商汎関数の極因子、指定10minor（行毎分母を除きQQ[B,C]の多項式行列式で再検証）、八曲線それぞれ二minorと全極の平方因子除去多項式、有限因子の点集合への写像を剰余零で検証。curve群はC0,C−1,B±1,2B+C0,2BC+C²+1,4BC+C²+3,4BC+C²+4。有限実行は12有理点とQQ(sqrt2)/QQ(sqrt3)代表、全て正常核零ただし(1,−1)だけdim1で指定因子。計算はPYTHONPATH=/workspace/work/python-deps SYMPY_GROUND_TYPES=flint環境でexact実行、独立査読は未確認。正常核zeroの有限標本を全値へ外挿せず、全係数恒等式・例外cover・個別点を区別した。

次は残る逆平方型：[x,y]+uv+vu=0,x²+u²=0。cross M rank2、imM=span(xu,xv+yu)、奇関係二射影rank3,3。純UV/VU各一本は非分解tensorでなければならない。正側shearで純UVをxv+yuへ正規化し、奇交代top rank4とD=tauAの必要atlasを求める。まず非半単純候補を縮小：非零Q rank2のabelianized binaryquarticは第四乗でないので負unipotent不可、正片側JordanもH固定純UV線がxVの積線になりdomain外となる見込み（未公開証明）。負secant/非対称型、全CY/三固有値以上/成分/相対降下も未完。


## 負tangent型の全排除（classification-v184）

負tangent型の最後の逆平方/rank2 cross境界を全値排除。非零Q rank2は負unipotentを許さず、rank3奇射影の正片側Jordanも純UV不変線が積になるためdomain外。半単純境界は純UV線正規化からA=(a,a,0,b,c,c)、六Pfaffian ideal(b²,bc)、幾何点b0/cunit/保存torus c1へ還元。正常汎関数の極a±1、二10minor gcda、三例外a0/±1も元関係で核零。従ってcanonical負tangent Qは全Jordan型込みで完全に空。

証明cubic_order2_22_tangent_rank2.tex、verifierは同stem。必要atlasは純UV p∈imM∩imAとrank2Aからp wedge rに書く。b²0は幾何点でb0であり、非被約底上の消滅は主張しない。A正規化後の四関係とO全列の一致は単位minor/多項式生成恒等式で全aに確認し、generic rankだけで特殊値を被覆したのではない。

## mixed rank4全Jordan部分の消滅（classification-v185）

(2,2)/mixed rank4全H3の中山半単純性を証明。P0/Q0認識に加え、P,Q非零では負Jordanなし。非full graphは純mixed不変直線の積障害、full graphはH同変graph[[A,B],[0,A]]とx²=b(V)neq0から三次基底y³,xy²,yV²,xV²を用い、固定核がxV²に限られる。四rank6 minor=6*((A⊗A)b)_jが全chartを覆い、muG固定と同一ベクトル空間のuntwistで元Gにも一次因子。全未知は半単純、非零負topは対称secant/非対称の二型に縮小。

証明cubic_order2_22_Jordan_complete.tex。Q非零単冪固定cyclicQの一般解det=−3d⁴/16なのでrank≤2ではrank≤1となりrank1禁止に反する。full graphのH可換化idealとdetA²、det(A⊗A)=detA⁴、三次固定作用の四6minorとH4固定核一致を検証。C3正基底のspanningはx²/yx置換とmixed graphから、independenceはAS4正三次次元10から。N(xy²)=2b*y+x(b−a)のyV²成分が2(A⊗A)bneq0なので固定GはxV²。元BでmuG固定からH固定へ移すだけでnormal cutのtwist輸送はしない。新規性/独立査読未確認。

次は二つの負rank2型のcoupled even atlas。対称secantはb1=u²+v²,b2=u²−v²、非対称はb1=uv+i*vu,b2=uv−i*vu。各R1=cU+b1,R2=qU+b2。qU平方は相対係数を全正規化できる見込み、qU非退化はrho*(xy+yx)の残余係数rho≠0を保持する必要。secant Mは平方det−1、非退化det−(1−rho²)²、rho±1はrank2境界になる見込み（未公表計算）。まず全M/Pfaffian線型atlasを求め、可逆graphとrank2境界を区別する。全CY/三固有値以上/成分/相対降下は未完。


## 非対称負topの全排除（classification-v186）

非対称負top Q=uv⊗uv+vu⊗vuを全正top/全Jordan/全cross境界込みで完全排除。二つの等方因子uv±i*vuの割当ては負軸交換で同値。全可逆crossの閉/局所化六線型atlasで正Pf枝はA0矛盾、負Pf枝はuの正側作用F²=−iIdへ正規化。uv,vu正二次式とF(b)=aからu²v=−vu²、u4はUと反交換/Vと可換、正常三次がu4と可換かつ反交換となり零。rho±1のrank2 crossもPfaffian ideal(a²,ac,b,c²)で幾何A0となりdomain射影rankに反する。

証明cubic_order2_22_nonsymmetric_complete.tex、同stemの公開verifierは四つの閉/局所化ideal一致、M行列式、二正規化graph、F²−iIdと自由positivequadのF(b)=a、shearによるz0除去、等方因子交換と特異全Pfaffian idealを厳密検証。平方負枝s²=i、nondeg負枝z0z5=i(rho²−1)であり、rho*(rho²−1)を単元としたideal一致を使うため未処理特殊値はない。特異rho±1は別rank2 atlasで処理し、nilpotent baseまでa/c零とは主張しない。Bdomain上のu4共役作用による核零であり、Rdomainの一般論やtwist輸送を使わない。

次は唯一残る非零負top、対称secant。b1=u²+v²,b2=u²−v²、R1=cU+b1,R2=qU+b2。平方qU=x²の負Pf枝はA=(-s,t,s,s,t,0),t²−s²1、s=(w-w^-1)/2,t=(w+w^-1)/2で全wneq0へ一param化し正常核計算中。正Pf平方枝はA=(z0,-z4,-z3+z5,z3,z4,z5),z0z5−z3²+z3z5+z4²=1。非退化qU=rho*(xy+yx)ではrho≠0,±1の二Pf線型atlasとrho±1 rank2 secant boundaryを分ける。相対rhoや境界cを勝手に尺度で除去しない。全CY/三固有値/成分/相対降下も未完。

私的secant atlas計算（未公開）：rho≠0,±1でalpha=(rho−1)/(rho+1)。正Pf A=(z0,-z4,alpha*z3,z3,z4,z5),Pf式z0z5+z4²+alpha*z3²=1−rho²。負Pf A=(0,z4,-alpha*z3,z3,z4,0),z4²+alpha*z3²=1−rho²。rho1 rank2/p=xv+yu正規化ではA=(a,a,0,b,c,c)、全Pf ideal(a²−c²,ac+c²)⇒幾何a=−c,cneq0。p正規化後は一般にcを尺度で1にできないので、b,c二paramを保持する。


## 対称secantの全負Pfaffian排除（classification-v187）

唯一残る対称secant負topの全必要odd atlasを確定し、二つの可逆cross負Pfaffian分枝を全値排除。平方負枝はconic t²−s²1のw=t+s!=0 parametrization、全quartic汎関数がLaurent係数で四正常10minor gcd定数*w13。非退化負枝は全conic上のopposite normalizer fgId/det−1、xy/yxがu²/v²を張り負Sym²全体が中心となるため奇補助次数中心作用で核零。正Pf二枝とrho±1 rank2secant境界の必要atlasを保持し、境界b,cは勝手に尺度除去しない。

証明cubic_order2_22_secant_negative.tex、同stemの公開verifierは四つの閉/局所化linear ideal一致、rank2 Pfaffian ideal、非退化conicのfgId/det−1とxy/yx二次係数det−1/rho、平方全wneq0の元quartic関係汎関数と四minor gcdw13を厳密確認。Gaussian値でのrankはminor位置の設計にだけ使い、最終公開証明はQQ[w]多項式恒等式と全値gcdで完結。新規性/独立査読は未確認。

次は平方正Pfaffian。yshearでz5=q!=0 chartはA=((1−t²)/q,−t,q,0,t,q)の二paramへ還元。私的secant_square_general.pyで元三次/四次商と正常10minorを計算中（未公表・全値被覆未証明）。z5=0はz4²−z3²1、z3!=0ならshearでz00、z3=0ならz4±1/z0任意の境界を別に保持。非退化正Pfはrho非zero/±1と三係数quadric、rank2境界はA=(-c,-c,0,b,c,c),c!=0。全CY/三固有値以上/成分/相対降下は未完。


## 平方secant正Pf共鳴の全pencil因子化（classification-v188）

対称secant/平方正top/正Pfaffianのz5neq0共鳴z4=1/2を全パラメータで排除。yshearでz3=0へ全被覆しq=z5neq0。正常rank8二minor gcd定数*q10、六係数因子式(x+theta*y)*Q2が正常、theta係数行列の一2minor=256*q8で全q非零に非定数pencil写像。四次汎関数の極q±iはGaussian体上で元関係を再消去しrank8/因子像span2。properなprojective比例incidenceと包絡domain性により全正常pencilが一次因子を持つ。

証明cubic_order2_22_secant_square_resonant.tex。検証器と小入力JSONはnormal two-minor位置、quadratic factor六係数、因子像rank2minor位置を含む。共通original-relation linear algebraは公開cubic_order2_22_secant_tools.pyへ分離し、nf3/nf4の各元関係消去恒等式も毎回検証。N kernelの特定二列に座標化すると4q⁴+12q²+3という不要な分母が出るが、それは選んだ座標の退化であり、因子像theta係数行列のunit minor256q8を使えばそのquartic例外を作らず全pencilを覆える。新規性/独立査読未確認。

次は同じ平方正Pf主chartの共鳴外。A=((1−t²)/q,−t,q,0,t,q),qneq0。私的全二param消去はNF3分母2q²t、全NF4分母に複雑curveも出るが、正常minorに使う7汎関数(j=4,5,6,9,13,14,19)の極はq*t*(t²−1)*(q²−4t²+2)だけ。単一正常10minor=(2t−1)^4(2t+1)^4(2t²−1)/(16*q*t³*(t²−1)²*(q²−4t²+2)²)。genus2らしき全NF分母はこの7関数に不要なので扱わない。選択7関数全normalizer 28行でt=−1/2,±1/sqrt2の代替minorを探す計算中。残るF=q²−4t²+2=0はw=2t+qでt=(w+2/w)/4,q=(w−2/w)/2の有理一param。t0/±1各直線とq0境界、非退化正Pf、rank2secantも未完。全CY/三固有値/成分/相対降下未完。

私的巨大generic左逆行列計算は出力を得ず終了したため再実行不要。7つの選択四次汎関数だけを使うことで不要な高次分母を既に除外できる。私的secant_square_general.pklのN/nf3/nf4はSymPy式へ変換して保存済み（native QQ(q,t) FracElementをpickleするとring内部辞書変更例外が出たため）。公開のsecant_toolsからmain式で再生成可能。


## 平方secant正Pf主chartの全値排除（classification-v189）

平方正top/対称secant負top/正Pfaffianの全z5neq0主chartを全値排除。選択六四次関数の極q*t*(t²−1)*(q²−4t²+2)のみ、正常10minorは−(2t−1)³(2t+1)³/[16q t³(t²−1)(q²−4t²+2)²]。五有理曲線を二minorで被覆、Gaussian有限点ではt0核零/t−1/2唯一正常三次もx+2yを因子に持つ。残るconicの12次既約例外P(w)は厳密12次数体で元288四次関係を消去しrank10、全共役を同時に排除。t1/2全pencilは既存因子化と接合。

証明cubic_order2_22_secant_square_main.tex。verifierは共通secant_tools.normal_freeで全32自由正三次の正常式を作り、三次のgeneric座標基底を特殊値へ仮定しない。五curveの実際に使うquartic functionの極と二minor gcdの合併を調べ、定義域外と既知t1/2を除く残余因子をGaussian点、既知t0曲線、12次既約Pへ剰余零で写す。P=w12−12w10+28w8+96w6+112w4−192w2+64。QQ[alpha]/P上のR係数をQQ(w)の分子/分母からnative ANPで評価し、SymPy式へ12次根を大量展開せず256語商を消去、B4dim35/normalrank10を全元関係annihilator恒等式付きで検証。実行はoptional Flint exact ground environment、近似根計算なし。Gaussian唯一cutは(x+2y)*(-x²/2+xy+yx+2y²−i(uv+vu))、共役も同じ左因子。新規性/独立査読未確認。

## 平方secant全境界と平方正topの全排除（classification-v190）

平方正top/対称secant型の全境界z5=0を排除し、既存の主chart・負Pfaffianと合わせ、この型全体にH3がないことを証明。三有理曲線の二minor gcd cover、Gaussian/三次根の厳密再消去、唯一の原始六乗根正常pencilの明示的一次因子写像で全値を覆う。次は非退化正topの正Pfaffian三param quadricとrank2secant境界A=(-c,-c,0,b,c,c),c!=0。全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_square_boundary.tex。s!=0ではa0にshear正規化しw=t+s、s=(w-w^-1)/2,t=(w+w^-1)/2の一curve、s0ではt±1/a任意の二line。正常10minor二本と使用汎関数の極から有限例外はconicのw²+1,w²±w+1と二lineのa0だけ。Gaussianと原始三乗根及びa0は正常核零。原始六乗根は核2で、r²=-3としてQ2=(-3r theta²+2r)x²-r theta(xy+yx)+2r theta²y²-3(theta²+theta)uv+3(theta²-theta)vuが(x+theta y)との積を正常にする。theta係数span2を厳密検証しproperな射影比例incidenceで全正常pencilを覆う。二次体の共役も同時に覆い、全cutに一次因子。新規性/独立査読未確認。

## 対称secant特異混合blockの全排除（classification-v191）

対称secant負topのrank2混合block境界を全二パラメータで排除。最高テンソルの像の四列はminor4c²で全c非零の関係基底となり、正常10minorが−32c5というLaurent単元。平方正topは既に全排除なので、両top非零のmixed4(2,2)に残る未知は非退化正top/対称secant負top/正Pfaffian/混合block可逆の必要quadricだけ。全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_singular_cross.tex。rho1のatlas A=(-c,-c,0,b,c,c)を保持し、cを消す誤った正規化を用いない。交代8block Oの列0,1,2,4をCとし行0,1,2,4のminor4c²とC*T=Oを厳密検証。元六二次関係から四次商を消去すると一般次元35、正常32列に一つの10minor−32c5、実使用汎関数はc冪だけを分母とする。よって全値でrank10、AS4正三次次元10から正常核零。既存v149のrank2「奇関係」境界とは異なるため、新verifierをsecant_singular_crossと命名して区別。次はrho(rho²−1)!=0でalpha=(rho−1)/(rho+1)、A=(a,-t,alpha*s,s,t,q)、a*q+t²+alpha*s²=1−rho²。q!=0を正torusでq1とした三param chartと、q0の境界を保持して判定する。

## 非退化secant二重零境界の全排除（classification-v192）

非退化正top/対称secant負top/正Pfaffianのa=q=0二重零境界を全値排除。逆作用F/F^-1と負対称二次中心から補助次数±1の正常成分を消し、±3成分はtraceF1のx³,y³だけ。全pencilは(x+theta*y)(x²−theta F²(A2)+theta²y²)=x³+theta³y³で分解。x/y交換でq0,a非零をq非零へ移せるため、両top非零mixed4(2,2)の未知はq1の三param主chart一つだけ。全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_doublezero.tex。負部分Tのu²,v²,{u,v}が中心、B2で独立。補助次数±1のxQ2/yQ2が正常ならQ2は−Fをintertwineし、対称二次中心のdomain cancellationでSym²FId⇒F±Id⇒rho0という矛盾。±3はF³−Idが必要でSL2/非scalarよりtraceF1に限る。共鳴正常pencilは全て明示normで分解。F(A2)=B2と逆作用は円錐曲線の多項式恒等式として検証、元三次関係で数体fiberのnormも検算。残余主chartのQQ(rho,s,t)による全四次商の一括rrefは4分超で未完のため中断、結果なし。次は構造的制約又は低パラメータsliceから残余を縮める。s0のQQ(rho,t)正常計算を開始中、未公表・未完。大きなrrefを無制限に反復しない。

## 非退化secant共鳴面の全値因子pencil（classification-v193）

非退化正top/対称secant/正Pfaffian/q1主chartの共鳴面2t+rho²−1=0に、全AS4domain fiberで全て分解する正常pencilを構成。明示多項式Q2の係数ideal単元、generic正常恒等式と像rank2を最大rank三次/四次商の局所自由性で全AS4fiberへ延長し、domainと次数により像rank2を保証。正常8minorと使用汎関数の極から(rho²+1)(rho²+3)(rho²−9)D E非零の全開集合では正常核全体がそのpencil、H3なし。例外曲線と共鳴外は未完。

証明cubic_order2_22_secant_nondegenerate_resonance.tex。D=r4+2r3+4r²+6r+4s²+3、E=r6+4r5+7r4+8r3+4r²s²+7r²+12rs²+4r+1。因子六係数は最小JSON入力へ保持。係数ideal＋z*r*(r²−1)−1のGroebner基底1。generic商B3dim20/B4dim35の最大rank開集合は全AS4fiberを含み、その局所自由余核で正常恒等式と3次外積零が延長する。domainならQ2のz共通因子を除いた積が常に非零で、像rank1以下は正次数scalar polynomialの零点で矛盾。従って全fiberで分解pencil2を得る。正常核の次元jumpは別問題なので例外曲線を未解決として残す。

次の具体作業：正常8minorのr±3/Eの余分な因子を別minorで除き、残余曲線r²=-1,-3,D0等の正常核を個別判定する。主chart三変数のSymPy通常rref/分母払FF、私的native FLINT有理関数消去は、それぞれ数分で未完のため中断。後者はforward200行/rank184まで進んだが最終商・annihilator検証に達しておらず数学的結果として用いない。反復せず列順序/低パラメータ制約/構造的normalizerへ切り替える。s0の二変数商Nは私的保存されたが公開証明は未完。

## 一重零全排除と共鳴例外二曲線への還元（classification-v194）

非退化secant正Pfの全aq=0領域を排除。二重零環をOre基底Tの一般化Weyl代数として構成し全値domain/Hilbert14641を証明、一重零a0の補助次数先頭環と同定。正常核は非共鳴0/共鳴高々2、全値因子pencilで残りも排除。共鳴面は三追加minorとE,F4,J6 ideal=(s²,(rho+1)²)、一点(-3,0)の厳密再消去により例外rho²−9/E/Dを全て閉じ、残るのはrho²=-1,-3の二つの数体上一param曲線だけ。共鳴外aq非零主chart/全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_resonance_cover.tex。T=k[u,z][v;sigma,delta], vu=-uv+z,vz=zv,degz2。任意GL2VがTを保ち、A2中心/非零。T[X±1;F^-1]にx=X,y=F(A2)X^-1を置くWeyl表示でBdoublezero≅T⊕ΣTx^n⊕Ty^n、Hilbert1/(1-h)^4/domain。a0,q1はauxdegx1/y−1/V0でqtermだけ2低いのでgrBへdoublezeroから全射、AS4Hilbert同値で同型。gr正常核単射から非共鳴zero、共鳴dim≤2、既存全値normpencilが全kernelを覆う。追加minor三本は単元除去後(r+3)E,s²F4,s²J6、ideal(E,F4,J6)=(s²,(r+1)²)。残余(-3,0)もfresh original R4でrank8。D0=a0既に排除なので共鳴残余はr²=-1,-3だけ。私的secant_res_two_curves.pyでQQ(i)(s)及びQQ(sqrt3,i)(s)上の正常rank8と一変数minor gcdを計算中、未完結果を分類として使わない。

## 非退化secant共鳴面の全値排除（classification-v195）

非退化正top/対称secant/正Pfaffianの共鳴面2t+rho²−1=0を全値排除。三変数の明示多項式四次汎関数8本が元288関係を消す恒等式を直接検証。残余rho²=-1,-3で正常8minor三本のgcdはs³、s³*(s²+(2−2sqrt−3)/3)。Gaussian s0はB4dim36で非AS4。残る有限点はQQ(sqrt3,i)で元関係再消去しB4dim35/正常rank8、全共役を覆う。全値因子pencilが全正常核となりH3なし。次はq1主chartのa非零/非共鳴領域。全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_resonance_final.tex。私的FLINT rational-function sparse Markowitz eliminationで三変数B4dim35と全元関係annihilatorを取得。分母leading coefficientを1にする正規化で有理unit係数の巨大化を防ぎ、八つの汎関数だけを多項式化/primitive化して174KB JSONへ保存した。公開checkerは生成アルゴリズムを信頼するのでなく、六二次関係の全位置・全外語288行をその多項式汎関数が消すことを直接QQ[r,s,t]で検証する。両残余curveで行のs冪だけを除き三minor gcd cover。sqrt−3最後の点s=(1+r)/sqrt3は四次体QQ(sqrt3,i)の埋込みで全符号共役を覆いfresh正常rank8。

次の具体計算：同じ八多項式汎関数の正常10minorを主chart全体で構成し、非共鳴に残る必要supportを減らす。私的fullnormalminorは定数unit*r^4*s³*t12*(r−1)^18*(r+1)^29*(r²−2t−1)²*(r²+2t−1)²*L、L=r5+r4+2r3s²+2r3t²−2r²s²+2r²t²+2rt²−r+2t²−1。元の選択汎関数の極はr²*s*t²*(r−1)^4*(r+1)^6だけ。これを公表するには公開polyλからminor/逆行列恒等式を再生し、分母/poleと別minorで偽の因子r²−2t−1/Lを除く。公開証明未完のためこのgeneric主chart結果を分類済みとして使わない。

## 非共鳴主chartの開集合排除と四残余曲面（classification-v196）

非退化secant正Pf/q1主chartの明示開集合で正常核零を証明。八多項式四次汎関数の元288関係annihilatorに加え、正常10部分行列Cの多項式右逆証明CX=dI10を公開。d=r³*s*t²*(r−1)^5*(r+1)^6*(r²−2t−1)*(r²+2t−1)*L。既存の全aq0/全共鳴排除と合わせ、両top非零mixed4(2,2)の未知はs0,t0,r²−2t−1=0,L0の四曲面（a非零/非共鳴）だけ。全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_main_open.tex。L=r5+r4+2r3s²+2r3t²−2r²s²+2r²t²+2rt²−r+2t²−1。73KBの明示polynomialXでCX=dIを直接検証するため、生成に使ったFLINT消去や多変数detを再実行する必要はない。全正自由三次32列の正常条件が元三次関係を消すことと正三次商次元10から、全開集合で正常核零。公開polyλはprimitive化済みで元288行を直接消すため、特殊値にもそのまま有効。

次の具体作業：private mirror/tzero/lszero chartを、それぞれ(r,s,t)=(2,1,3/2),(2,1,0),(1/3,0,2/3)でpivotが非零になるsparse Markowitz順序から生成した。全て三変数B4dim35、全元annihilator検証/保存済み。各rawNFはsqnd_main_mirror_raw.pkl等、原稿用証明には未使用。mirror/tzero正常10minorと使用functionalsを計算中。最初の八λはmirror面でrank8/t0でrank4しか保証せず、実際の正常kernel rankをそこから推定しない。新chartのprimitive多項式λを少数選び、全元関係identityとnormal right inverseを公開して残余supportを減らす。s0は最初の八λだけでも一般rank10なので、s0をsampleに別minorを選べる。

## 二座標曲面の全値排除（classification-v197）

非退化secant正Pf/q1主chartの座標曲面s0,t0を全値排除。元288四次関係を消す追加多項式汎関数と正三次関係24×32行列から、局所化係数環でK=kerT3/正常行加群Fを比較。t0はK=F、s0は(t+1)K及び(rho²+1)KがFに所属。AS4最大rank開集合で核の底変更を使い正常核零。残るs0,t−1,rho±iは元関係でB4dim36、非AS4。未知は鏡共鳴rho²−2t−1=0とL0の二曲面だけ（a非零/真共鳴外）。全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_coordinate_planes.tex。Singularのsyzygyは商環k[parameters,z]/(zU−1)上で計算する。行列積は商環で自動的に正規化されるとは限らず、R3*E及びR3*Nの零検査をreduce(ideal(product),std(ideal(0)))で行う。module==0は列数付き零表示と一致しない場合があるのでsize(reduce(module,...))==0で判定する。所属はt0でE⊂N、s0で(t+1)E,(r²+1)E⊂N。N⊂Eは元四次annihilatorから独立に確認。AS4正三次商10/maxrank22開集合でkerT3のfiberが全双対となるため、全閉値の正常核判定へ適用できる。

再現にはSymPyとSingular。SINGULAR_BINで実行体を指定可。今回の環境は/workspace/work/cas/root/usr/bin/Singular、LD_LIBRARY_PATH=/workspace/work/cas/root/usr/lib/x86_64-linux-gnu、SINGULAR_PROCS_DIR=/workspace/work/cas/root/usr/lib/x86_64-linux-gnu/singular/MOD。native polynomial procedureの設定により既存CASを利用し、追加installはしていない。

次の着手：鏡共鳴t=(r²−1)/2の既存29汎関数module計算ではAnn(K/F)のパラメータ支持はP10=Bm4*J6、Bm4=4s²+(r−1)(r+1)³、J6=4r²s²+(r+1)²(r²+1)²の二曲線へ縮む（私的計算、未公表の全所属certificate）。全35商汎関数をoriginal/t0/ls0三chartからprimitive多項式化したprivate JSONを生成済みで、追加による曲線support除去を調べる。最後のL0は二次曲面表示とmodule飽和で扱う。全35入力は大きいため最終証明に必要な生成元を選ぶ。現在の公開追加入力は21汎関数、全元関係を検証する。

## 鏡共鳴の縮小と唯一の残余L曲面（classification-v198）

鏡共鳴t=(rho²−1)/2でBm*Jm*K⊂正常行加群Fを局所化加群として検証。Bm=4s²+(rho−1)(rho+1)³は全有理param rho=(1−w²)/(1+w²),s=2w/(1+w²)²で覆い、正常10minorが単元以外にw4−w²+1だけを零点に持つ。その残余はJm=16(w4−w²+1)/(1+w²)^4=0なので、鏡共鳴の全候補はJm0へ。L|mirror=(rho−1)Jm/2により、両top非零mixed4(2,2)の全未解決候補が一曲面L0へ縮んだ。全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_mirror_support.tex。K=kerT3のsyzygyと正常行Fで(Bm*Jm)K⊂Fを直接Singularで検証し、Annの巨大な標準基底を再現する必要をなくした。Bm曲線の有理paramは逆w=2s/(rho+1)²、w(w²−1)(w²+1)非零。私的nativeFLINT一変数四次消去でB4dim35/全元annihilatorを得て、必要な多項式汎関数だけを小JSONへ保持。公開checkerはその全288恒等式とnormal10minorの全根因子をQQ[w]で再生する。残余w4−w²1=0は3rho²+1=0でありJm曲線との交点なので、独立に排除済みとは扱わずJmへ含める。

次の具体着手：Jmの二枝はs=±i(rho+1)(rho²+1)/(2rho), t=(rho²−1)/2。rho(rho²−1)(rho²+1)非零、rho²+1=0は既存s0排除へ。rho2,s15i/4,t3/2の元関係再消去ではB3dim20/B4dim35、正常rank9で真に正常核一本が残る。正一次因子の条件は(3theta+4i)^3=0、従ってこの点はx−4i*y/3を因子に持つ。この点からの推測beta=−2i*rho/(rho+1)は、native Gaussian有理関数体上でNL(beta)のkernelが零となり一般式として棄却した。次はthetaの6minor gcdをQQ(i)(rho)[theta]で計算し、正しい因子条件を導く。交点3rho²+1=0のrho=i/sqrt3,s=(sqrt3+i)/3,t−2/3もfresh四次商35/normalrank9を得た。正常核の全curve coverと実際のQ2を次に構成する。

L0の非鏡領域はrho²+1=0ならs0なので排除済み。それ以外ではL上の真共鳴有理点t0=(1−rho²)/2,s0=i(rho+1)(rho²+1)/(2rho)から傾きk=(s−s0)/(t−t0)で有理paramを作れる。D=rho²(rho−1)k²+(rho+1)(rho²+1), E=(rho+1)−i*rho*k, Q=−D+2(rho²+1)E、t=(rho²−1)Q/(2D), s=s0+k*(rho²−1)(rho²+1)*E/D。非共鳴ではE,D非零で覆える見込み（全恒等式・被覆は未公表、検証してから使う）。元のLgeneric点rho3,s10i/3,t1はB3dim20/B4dim35/normalrank10で、L全体を正常核非零と推論しない。

## 鏡共鳴面の全排除（classification-v199）

鏡共鳴の最後のJm曲線の全正常切断を排除。両枝s=±i(rho+1)(rho²+1)/(2rho), t=(rho²−1)/2で、b=−2i*rho/(rho²−1), Q2=x²+b(rho²+1)(xy+yx)+b²y²+2rho²/(rho²−1)*(uv+vu)としG=(x+by)Q2。35明示多項式四次汎関数と一点B4dim35の上下界からgeneric商次元35、正常恒等式をAS4最大rank開集合へ延長。三normal9minor gcdと3rho²+1=0のfresh数体rank9で全正常核一本を保証し全cutに一次因子。鏡共鳴面全体が空、未知はL0の非鏡領域だけ。全CY/三固有値以上/成分/相対降下は未完。

証明cubic_order2_22_secant_mirror_J.tex。正しいtheta条件は((rho²−1)theta+2i*rho)^3であり、一般betaの分母はrho+1でなくrho²−1。Q2係数は入力へ明示しQxx1なのでdomainで非零。35多項式quartic annihilatorの指定35自由語への対角minorが非零、rho2の厳密B4dim35からgeneric四次商35をrigorous上下界で得る。Gの正常commutatorを全部消すためgeneric正常、係数regularかつAS4最大rank余核局所自由で全AS4fiberへ延長。kernel上界normal9minor三本gcdはbaseunitと3rho²+1だけ、交点はQQ(sqrt3,i)上で元R4を再消去しrank9。この証明は全値cutのfactorであって単なるgeneric排除ではない。

次は非鏡L0（a,s,t,delta_plus,delta_minus非零）。rho²+1=0ならLがrho²(rho−1)s²の定数倍でs0に入り既に排除。D=rho²+1−(rho²−1)z², Q=rho²+1−2(rho²+1)z+(rho²−1)z², H=Q+4zとして、t=(rho²−1)Q/(2D), s=i(rho+1)(rho²+1)H/(2rho D)という二param表示を次に厳密検証する。逆z=[2i*rho*s+(rho+1)(rho²+1)]/[(rho+1)(2t+rho²−1)]。a=(rho²−1)²*(Q²−2D²)/(4rho²D²)、delta_plus=2(rho²−1)(rho²+1)(1−z)/D、delta_minus=−2(rho²−1)z*((rho²−1)z−(rho²+1))/Dが候補恒等式。検証前に全被覆として使用しない。

## 両top非零の完全排除とmixed rank4領域の認識（classification-v202）

(2,2)/mixed rank4の全H3は、全Jordan型込みで既分類の曲がったClifford族B_hに一致する。新しく閉じたのはP,Qとも非零の最後のL0非鏡開集合であり、ここでは正常三次核が零。P0は既知符号族、Q0はB_h、符号族はh0部分族。全切断のadmissibility、全幾何学的矢、一般dim5/慣性mu2は既存の曲がったClifford定理を使う。他スペクトル・全CY被覆・全成分・intrinsic相対降下は未完成。

証明は `papers/sections/cubic_order2_22_secant_L_complete.tex`。前節までの全排除と主chart逆行列により両top非零全候補がL非鏡開集合へ帰着していることを使用する。最後の底はp=rho²−1,c=rho²+1,D=c−p*z²,Q=c−2c*z+p*z²,H=Q+4z,F=p*z−c,A=Q²−2D²、U=rho*p*c*D*z*(z−1)*F*A*Q*H。t=pQ/(2D),s=i(rho+1)cH/(2rhoD),a=p²A/(4rho²D²)。正則逆写像と分母の全値被覆は `verify_cubic_order2_22_secant_L_parameter.py` により検証済み。

公開29四次汎関数の各288元関係annihilator恒等式を検証し、正三次32自由語に対する24×32関係行列R3と32×44正常行Nを作る。QQ(i)[rho,z]上のkernelは15生成元から非零定数を持つ5関係で自由rank10のEへ縮約され、syz(E)=0。座標Tは全て多項式で、全32×44成分のET=Nを厳密確認。TのU単元因子だけを行・列から除き、単元pivot10回で行が零本となる。非定数pivotは定数/iを除きrho,D,Qだけ。各Gaussian normの単元因子分解も再検証する。従って正常行加群は全kernelに等しい。AS4点で正三次次元10、R3rank22が最大なのでkernelの底変更が成立し、正常三次は零。

再生手順（SymPy、python-flint、Singularが必要。生成する巨大入力/pickleはGitへ追跡しない）：
```sh
python computations/build_cubic_order2_22_secant_L_module.py --output /tmp/L.sing --method free
Singular -q /tmp/L.sing
python computations/solve_cubic_order2_22_secant_L_coordinates.py --prefix /tmp/L.sing
python computations/verify_cubic_order2_22_secant_L_saturation.py --prefix /tmp/L.sing --certificate /tmp/L-certificate.json
```
全三段階を公開コードから実行してPASS。小証明書は `computations/cubic_order2_22_secant_L_saturation_certificate.json`。ASCII exportはSingular 4.4.1のalgebraic minpoly dump不具合を避ける。旧direct/presentationの巨大Ann/lift計算は証明に不要。B0追加汎関数も不要となった。

次の最優先は共有方針の量子三次成分における全Artin底の相対二次包絡。一般H3分類では三固有値以上とCY残余の被覆も未完成である。

## 共通認識補題と多固有値の現在の必要被覆

### 正規三次切断の四line frame
`cubic_hypersurface_frame.tex`：noetherian quadratic Koszul AS4型14641の正則正規三次切断、整域、mu_R=idを仮定。四line compact generatorのproper dg cohomologyはH0=55,H2=21。Gb=nu(b)Gの規約ではTor1=R_nu(-3)、hypersurface作用eta_F:F→F_nu(-3)[2]。Gabriel–Krull rank-one torsion-freeを別仮定すると、全coherent Fのeta_F²消滅とH3性が同値。全heart対象は四lineから8段で生成。有限検査や相対開性、rank条件の自動性は未証明。

### スペクトル被覆と関係character
`cubic_spectral_resonance.tex`,`cubic_spectral_ore_reduction.tex`：mu(G)=Gから三次共鳴が必要、単純固有直線の唯一の純三乗共鳴は非整域で排除。四単純固有値の十個の二次積が相異なる領域はskew、(2,1,1)の二次非共鳴領域も二元AS2 Oreと全基底型の因子/正常核比較からskew。既分類skew H3は三固有値以上を持たないので、三固有値は六二次共鳴、四単純は21共鳴（反対固有値6、平方対二異値積12、互いに素なpair積3）上に限る。
三固有値はA=(a,-a,c),B=(a,b,-b),C=(a,at,a/t),D=(a,at,at²)の四chart。各七三次共鳴。AS4最高wの中山巡回を四回反復してmu^tensor4(w)=w、Frobenius次数1/3から各固有方向を含む四次重みが存在。三次/四次の文字格子detにより、共通N乗根(N≤24)又は二相反pencilに縮小。
二次関係の重みchiとchi^-1の次元は等しい。重み−1は中山巡回二回とdetから偶数（単冪込み）。重みspace次元Dchi、固有重複miならrank-one Segre回避でrchi≤Dchi−max(mi+mj−1)。KoszulcharacterはB2=V²-I、B3=V³-2VI+V*、R3=B3-1。R整域の線型乗法単射性を全重みで課す。

### 相反pencilとGK2傾き障害
`cubic_inverse_spectral_pencils.tex`：(z,z,1,z^-1)は位数1〜4外で関係数≤5となりAS4外。(1,1,z,z^-1)の必要atlasはbU=f(U)b,cU=g(U)cと二本のU²/bc/cb関係。偶射影rank1はAS2 inverse-Nakayama一次intertwinerとmodF正常式で全因子。rank2はbc=h(U),cb=k(U)、S=<U>が二元二本のcubic関係でHS=1/((1-t)²(1-t²))。bのOre局所化S[b±1;f]からS noetherian/gldim≤4。G∈S3、S/(G)↪B/(G)だが商のGK2傾き3/2はArtin–Staffordの一次生成GK2整域の整数傾きに反する。SのAS3性は仮定しない。root4 unit pencilも偶数性で同じ関係/charge0分布を確認して排除。
文献入力はStafford本人を含むStafford–Van den Bergh arXiv:math/9910082v2 Theorem5.2 p14（Artin–Stafford Theorem0.2の明示的再掲）。本文・代数閉体・次数1生成・GK2・有限余次元THCRの結論を実読。原論文DOI10.1007/BF01231444のabstract/書誌も照合したが、原論文全文証明の独立再監査とは称さない。PDF digestと適用範囲はvalidation JSON。曲線Riemann–RochでHilbert傾きが整数になる。これで全三固有値スペクトルはまず共通N≤24の有限集合へ。

### 有限スペクトルの全列挙と排除
`cubic_three_eigenvalue_finite_spectra.tex`：N≤24全最小共通位数・相異指数35424組を整数剰余で全列挙。共鳴/整域関係容量を通る99関係パターンに次数3までのcharacter/乗法単射を課し、57除外witness（56単射違反、1負次元）を保存。必要38スペクトルからN9/12の8組を純二元AS2三次の因子で排除。残余に以下を適用した。
- 位数5四候補：`cubic_fifth_root_spectrum_exclusion.tex`。AS2 Ore表示と全自己同型型を比較、最終強制p=eta³,q=eta^-1で元の三関係NF(c x²b-b c x²)=-2eta x c³≠0。全Jordan込みで排除。
- 位数6：`cubic_sixth_root_spectrum_reductions.tex`。四scalar-normalizer Ore cone、二曲率（q³1と原始三乗根の矛盾）、一補助Z-grading正常核、二つのAS2平面作用矛盾で九候補を排除。cone補題はGv=lambda*vGへ一般化しM=k[v]のtwist同型v^n↦lambda^-n v^nを明示、既存Betti/無限Ext証明を維持。旧adjacent-L verifierも再実行PASS。
- 位数4：`cubic_fourth_root_spectrum_reductions.tex`。四奇数重み−1パターンを除き、(1,1,i,-i)を既述charge0障害で排除。
- 最後の位数6：`cubic_sixth_root_last_Ore_exclusion.tex`。正常bでB=A[b;sigma]、coneでb³係数非零が必要。正常式からsigma³=muB^-1|A、muA=sigma^-2、hdet sigma1。sigmaUの同一固有値は最高AS3cubicのslice退化、相異なる場合は(a,a*omega),a³omega²、sigma c=-a*omega^k。最高tensorの固定orbitを直接列挙しk0だけ残る。Aはx²=kappa*c²,yx=-a²xy,yc=-a²cy、sigma=(a,a*omega,-a)。sigma固定A3はkx²y一本だが正常x残差(-a²-omega²)x³yが非零、従って全Gはkb³で非整域。先行AS3完全分類を輸入していない。QQ(a),Phi9で全tensor slice、固定A3 rank9、元の正常残差をexact PASS。単冪sigma候補もslice退化で排除。

### 現在の残余：半単純・位数3の3スペクトル（v251）
三固有値H3の中山は半単純であり、位数3のみ。必要リストはN3:3個で、各関係重みパターンは一つ。Galoisラベル2軌道の代表(N;a,b,c)、重複2を先頭、単純二固有値を昇順に書く：
(3;0,1,2),(3;1,0,2)。
Galoisラベルはk線型同値の商ではない。3候補のAS4存在・正常三次・H3許容性は未分類。全リストと現在値は `computations/cubic_fourth_root_last_negative_simple_certificate.json`。再生は `python computations/verify_cubic_spectral_reductions.py`、34検証器のPASSは有限計算であり通常の全証明の独立機械検証ではない。
N4(2,1,3)は `cubic_fourth_root_negative_repeat_exclusion.tex` で全排除。G=F b²+L c²、domainにF,L独立が必要。even rank2はS2自由なのでF f²(u)=mu^-1(u)Fが不可能。rank1はAS2 Oreへ復元し、可換はf=gとh0でskewへ、JordanはF,Lが同一正常線で因子、量子反対角はscalar linear normalizerなし、量子対角はF=x,L=y、alpha=i,alpha*gamma=-pとgamma²=-pからp1を強制。単冪中山込み。公開検証器が元Jordan relationのminorとkernel、量子のp(1-p)矛盾、free-tensor augmented rankをexact PASS。

次の課題：残る二Galoisラベルの必要最高tensor atlasと正常核。
N4(1,0,2)と(3,0,2)のeven rank1は `cubic_fourth_root_unit_simple_rank1.tex` で排除済み（v227）。G=C b³+F2 c+D bc²、bc-qcb=h。正常b式の純T4成分は-q^-1F2*hだけ。h非零ならF2=0でG左b因子、h0ならAS2自己同型Oreの既存全型認識へ。元AS4 Ore family QQ(i)(alpha,beta)で四重なりとF2三基底の純T4残差をexact PASS。
この二スペクトルのrank2も `cubic_fourth_root_unit_simple_rank2.tex` で全排除（v229）。bc=h,cb=k、S2自由4次元、HS=1/((1-t)^2(1-t^2))。h,kが双方rank1なら正常式で独立平方に帰着し、最高binary quarticの第一pair対称性と巡回固有値±iが矛盾する。従って少なくとも一方hが非退化な正常二次。S/(h)はAS2、正常Reesと既証noetherian/gldim上界からSはcubic AS3・index4。
B[b^-1]=S[b±1;f]=C[b^-1], C=S[b;f]の次数付きbimodule最高Extを比較する。B index4とC index5の差により同型の単元はscalar*b^-1に限られ、muC|S=f^-1*muB|SとOre公式muC|S=f^-1*muSからmuS=muB|S。無次数のinner同値だけではこの結論にならない。自由S2上でmuS(h)=-h、正常化tau(h)=h。RRZ Lemma1.5（mu-normalは固有vectorの意味であり固有値1を要求しない、一次資料rrz.txt448–464を確認）からmuT=muS*tau、hdetT(muT)=-1となり、AS2の量子/Jordan標準形のhdet1に矛盾する。単冪も含む。公開検証はbinary tensorの対称/巡回連立rank16、AS2元関係の固定と11候補への更新をexact PASS。正常Rees/Ore/局所化は通常の数学的証明であり有限計算がこれを形式検証したとは称さない。
旧rank2の25×4正常係数核は構造還元として保持するが、この枝にAS4整域自体がなくなったので現在の未解決課題ではない。残るN4 atlasの検討へ進んだ。
重複1の残存N4(0,1,2),(0,2,3)も `cubic_fourth_root_unit_repeat_resonance.tex` で全排除（v230）。半単純mu=(1,1,i,-1)の最高tensorは16軌道、重みblock rankは(2,1,2,1)。bc/cb関係の両係数非零でmixed列比qを置き、U基底を適合させる。重み-1のPfaffianからa8=q²a5,a10=q4a5,a11=0、必ずxc+q^-2cx関係。純U主block rank≤2はa1=0を強制し、A=e*v^t+v*e^t、e=xy-yx,v=(a0,a3/2,a3/2,a4)。a4非零ならxy=yxとc²∈U²、q4=-1が強制され、c²x=-xc²と可換性が矛盾。a4零なら二次提示を(x,c)で商にしてk<y,b>/(b²)、次数15は1597>AS4値816となる。正常一次商のAS正則性などの未確認一般定理は使わない。
単冪部分は既証の右twist公式mu_(B^H)=muB*H^-4でH=mu_u^(1/4)を取ると消える。関係重みとAS4整域性を保つので同じ矛盾。この枝ではAS4整域自体を排除しており、G正常性のZhang輸送は仮定しない。公開検証器は256語から全巡回軌道、元middle、Pfaffian、minor、商関係supportと語数を両符号でexact PASS。続いて重複-1の枝を調べた。
重複-1の残るN4(2,0,1),(2,0,3)は `cubic_fourth_root_negative_repeat_finite.tex` で全排除（v231）。mu=(-1,-1,1,i)の最高tensorは17軌道。rank1 mixedをqで正規化し、重み-1 Pfaffianでa13=0,a6=q4*a8,a7=q²*a8。H0のbb列は純U関係r=a3x²+a8q4xy+a8yx、domainにa8≠0が必要。yy列もrに比例しa12=0,a2=a3*a5/a8,a5(1-q4)=0。a5=0なら(x,b)商がk<y,c>/(c²)で指数増大。よってq4=1,a5≠0、xy/yx列差からa4=a2。yのshearでa3=a2=a4=0、rank2minorでa0=0。
全必要表示はyx+xy=0,b²+A x²+C y²=0,bx=q²xb,by+q²yb+d c²=0,cx=iqxc,cb=-q^-1bc（C,d≠0）。scalar変更でC=d=1,A0/1、q四乗根の八表示。元R3/R4を再消去して全八表示の次元20/35、正常核はq1でk*c²x、他三qで零をexact確認。両i符号の計16検算を公開。非零正常三次も因子なのでH3なし。八表示のAS4十分性は不要であり主張していない。
単冪untwist D=B^H後もHはDの自己同型、mu_sと可換。唯一のUc+cU関係からHx=x、Hy=y+t*x。純U関係xy+yxの保存は2t*x²=0を強制、H=1。従って全単冪候補も既述半単純の場合に含まれる。Gの正常性をtwistで輸送することは使わない。続いて重複i・単純1を調べた。
位数4の重複i・単純1の二スペクトルは `cubic_fourth_root_last_finite.tex` で全排除（v232）。mu=(i,i,1,-i)の最高tensor16軌道を展開、rank1 mixedを列比qとU基底で正規化。H0の三次minorからa11=a14=0,a10=a8q²,a4=a8/q²,a2=a7(1+iq4)/(2q²)。H2のcc列の純U関係は非退化でa8≠0、yy列比例からa3(1-q4)=0。a3零ならc²=κx²と正常cxの二本の二元関係でdomain外。a3非零ならq4=1、shearとPfaffianでa7=a2=a1=a0=0。
全必要表示はyx=i xy,c²+C y²=0,cx=-i q²xc,yc+q²cy+d b²=0,bx=q^-1xb,cb=-q^-1bc（C,d≠0）。scalar変更でC=d=1、四つのqのみ。元R3/R4と正常核を両i符号計八表示でexact確認、唯一の非零W1はq=-iのk*(i b³-i c y b+c b y)。これは純base切断でB=S[x;sigma],sigma=-i scalar、正常化はSを保ちxを-i倍するので既証一般Ore cone頂点補題がH3を排除する。非零核を因子だと誤認せず無限高次Extを用いた。単冪untwist後のHも唯一のUc relationとxy+i yxの保存でH1となり、Gのtwist輸送を使わず全Jordanを扱う。
追加b4を含む最後のN4(i,i,-1,-i)と共役も `cubic_fourth_root_last_negative_simple.tex` で全排除（v233）。最高tensor17軌道。b4係数z0は同じeven rank条件の四表示に戻り、W1はq1でk*(yb+by)x、他は零（両符号八表示を元関係でexact PASS）。z非零はz1とmixed正規化を両立させ、H0のbb pivotのSchur補Tが対称rank1となる。T=v v^t,v=(p,r,s,t)でt²=-i r²,st=-i pr,s²=-i p²+q^-4-i。r0は純x²関係又は二本のU²関係でdomain外、よってr非零。eta=t/rでeta²=-i,s=eta p,q4=-i。H2の純U関係はq^-2 x²+i eta(px+ry)²となり非退化対称。
muUiのbinary twisted quarticのskew middleに対角な純U関係alpha*x²+beta*y²を入れると、rank2 Pfaffian -i alpha B,beta A+alpha D,i(-beta A+alpha D)がA=B=D0を強制し、純c²関係が生じる。これでz非零全chartが空。untwist後はz0四表示だけで、唯一のUc関係とxy+i yxから単冪H1。G正常性のtwist輸送を使わない。17元軌道、Schur恒等式、対称二次の行列式、Pfaffianと有限正常核をexact PASS。次はN3の二Galoisラベルの最高tensoratlasと正常核。全三固有値の存在/許容性はまだ未完成。
位数3の非単位重複根の全Jordan層は `cubic_third_root_nonunit_Jordan.tex` で排除（v234）。実際のmuU=[[omega,1],[0,omega]]の逆中山巡回を半単純重み1の全85語で解き、rank75、top核10次元。H0の(xc,yc,cx,cy)主minor=256*a8^4*(omega+1)^4によりrank2にはa80が必要。このときI0にはyc/cy成分がなく、I2のyy成分は恒等的に零。よって(x,b)商はfree<y,c>又はfree<y,c>/(c²)となり、次数15が1597以上>816でAS4外。両omega符号について全kernel・元巡回式・全関係行をexact PASS。半単純topをJordanへ流用した計算ではない。
重複1のJordan層も `cubic_third_root_unit_Jordan.tex` で全排除（v235）。実際のmuU=[[1,1],[0,1]]の86語巡回系はrank74、top核12次元。局所冪零D(y)=xによりI0はx²,[x,y],bc,cb内でD0。元mixed middleの純xb,bx二列のdet=4(a6²-a5*a8)、domainにはdet0及びa5,a6,a8全非零が必要（全零は指数増大商）。t=a6/a5とするとbx=-t^-1xb,cx=-t xc、残る二mixedは同じ対角の完全graph。
I0の[x,y]射影零は(b,c)商で指数増大。射影非零を消去して、baseにbc-qcb=h x²（q非零）、残りにyx=xy+κx²+ell bcを得る。bc/cb一方だけのbase関係はdomaincancelで追加純base関係を生じI0dim3となるため除外。全六関係の順序y>c>b>xの標準語数がAS4 Hilbert値に一致し、実際にB=A[y;sigma,delta],A=<x,b,c>というOre表示を得る。sigma x=x,balpha^-1,calphaでAは量子Weyl型AS3基底。
H3 Gはmu固定なのでDG0。Ore次数最高n項へDはn*a_n*x*y^(n-1)を与えるためkerD=A。G∈A3をA/(x)=quantumplane(b,c;q)へ写すと、Gb=omega² bG,Gc=omega cGは各b^r c^s,r+s3にq^r=q^s=omegaを要求し、四通り全て不可能。従ってG∈xA2で因子化。両omegaについて全12tensor核・元mixed二列・全パラメータ量子平面gcdをexact PASS。通常のOre認識/最高次数議論は本文の証明であり有限計算の出力と区別。
全三固有値中山は半単純・位数3に限る。`cubic_third_root_CY_incidence.tex`（v236）は残る二atlas各22次元の全最高tensor軌道と、可逆CY還元を与える。theta=muBでC=B^thetaはmuC=theta*theta^-4=1。degG3,theta3=1,thetaG1によりG*_C u=Gu,u*_C G=uGが厳密に成立し、G正常化theta^-1、左右正則性、idealのvector空間は同じ。逆にCY Cのtheta（hdet1）と同じ正常GからB=C^(theta^-1)を復元しmuBtheta,muR1。thetaを余分な任意標識とした全intrinsicモジュライ分類はまだ主張しない。
GはCで非中心（中心ならdomaincancelでtheta1）。C/(G)のNakayamaはtheta^-1で、表示次数を反標準次数と混同しない。商圏はpointed Zhang同値だが元の反Serre orbit環はB/(G)。CY中心三次の既分類だけではこの正常incidenceを覆わない。
全22軌道を元のtwisted巡回式で検証し、wC=(1⊗theta^-1⊗theta^-2⊗theta^-3)wBが通常反巡回であることも全係数で検証。middle像から関係Iを回収、各重みrank2が全AS4候補の必要atlas（十分性は未証明）。character B3=V³-2VI+V*から正常三次係数はunit repeat8、nonunit repeat7。全basisは公開certificate。次の最小課題はこのrank2 atlasと8/7次元正常核を同時に解析し、整域/AS4/H3条件を判定する。as4のSEMISIMPLE211は正確な三共鳴2011/1111/0211のみの仮定であり、本残余の追加Ub³/Uc³又はU³b等の軌道を含まないのでその八行表を全被覆として使わない（固定commit6f798e0のCLAIM及び証明冒頭の仮定だけを照合、定理輸入なし）。
重複1の二閉領域の全排除（v237）：`cubic_third_root_unit_closed_strata.tex`。22軌道辞書順でP=(a10,a18)はUb³、Q=(a14,a19)はUc³、S=a20はbbcc、T=a21はbcbc。P0又はQ0ならS非零は純c²/b²関係を生じdomain外。P=Q=0はcharge gradingがあり、Gのpureb³/c³係数は自身への正常式で零、Gcharge0となる。関係分布とcharge0を確認して既証相反pencilのrank1因子/AS2とrank2 GK2傾き障害を適用でき、全排除。位数>4仮定を無条件に外した主張ではない。
P,Q独立でS=T=0はGL2でP=(1,0),Q=(0,1)へ。mixedの定数単元pivotで全rank2条件を解き、H0のminor omega*a11^4からa110。純U関係a2x²+a15y²はdomainでa2*a15非零、純U反巡回blockからa4=0,a0*a15=a5*a2。全六関係はscalar正規化で一変数族x²+y²0,bx=omega xb,cy=omega²yc,b²=omega²xc+cx,c²=-yb-omega²by,bc-omega²cb=kappa(xy-yx)へ。
元の全R3/R4をQQ(omega)(kappa)で消去し、全pivot因子はkappa,kappa+1のみ。8不変三次の正常行列41×8、共通分母kappa、分母除去後Smith因子は六単元と二kappa。よってkappa(kappa+1)非零全域でW1零。kappa0は元関係fresh dim20/35,normalrank8、kappa-1はdimB3=22で非AS4。全パラメータを排除し、generic rankの特殊値外挿ではない。公開verifierは元22tensor、単元Schur pivotの九条件、全関係pivot因子、Smith及び二例外値をexact PASS。
S=T=0排除を次のS0全領域へ拡張した。非単位重複根の半単純22次元atlasも残る。スペクトル三個の全存在/許容性は未分類。
独立P,QのS0全排除（v238）：`cubic_third_root_unit_independent_Szero.tex`。T非零ならH0のbc/cb block C=diag(T,-omega*T)が可逆で、Schur0からa1=0,a0=A*E/T,a4=-E²/T,a5=D*E/T、A=a2,D=a15,E=a11。全六関係を明記した。scalar変更でA非零はA=T1へ、d=AD*T²,e=ETの二変数平面。A0,D非零は生成元x/y,b/c同時交換とomega→omega²で同じatlas（明示パラメータ変換も本文）。
二変数の全元R3/R4はgeneric dim20/35、全関係pivot因子d,e,d-e,d-e²、正常pivot因子d,e,d-e²のみ。全開集合でW1零。境界d=eはgeneric B3dim22なので元多項式行列のrank上界から全fiber非AS4。d0/e0曲線はパラメータt非零で全pivot因子tのみ、d=e²曲線は関係pivot t,t-1・正常pivot t、残る交点0/1はd=e曲線に包含。これで二変数平面全域を排除。
A=D0ならE非零、T1,E=lambda一変数。関係pivot lambda,lambda±1、正常pivot lambdaのみ、全開W1零。fresh lambda±1はB4dim37、lambda0はB3dim26で非AS4。公開検証器は全入力、Schur恒等式/正規化、全pivot因子、全四境界と三例外値をexact PASS。generic値を境界へ外挿したのでなく、多項式rank上界を用いたd=eの全値非AS証明と、残るunit pivot coverを区別する。
独立P,QのS非零も全排除（v239）：`cubic_third_root_unit_independent_Snonzero.tex`。P=(1,0),Q=(0,1),S1のmixed Schur Nはrank1で、右上はa11+omega、第三行第四列は-omega²*a12-1（定数項を保持）。N=u*v^t、domainと四係数整合からu=(p,r,lambda*p,-lambda*r),v=(-lambda*c,lambda*d,c,d),lambda(pd-rc)=-1。H0のbc/cb block K=[[T,-omega],[-omega,-omega*T]]、cross四行も本文に全式を保存。
pr非零はK特異が行空間条件とT²=-omegaの矛盾。K可逆のbinary反巡回条件によりT=2lambda²omega/(lambda4omega-1)、X=rc,Y=pdはX+Y=1/(2lambda²omega)+omega/2,X-Y=1/lambda、残る式は許容領域でlambda=-1,-omegaだけ。対角torusとrank1 factor scalarでp=r1、元22tensorと六関係の像の一致を確認し両候補B3dim22で非AS4。r0軸はK可逆/特異ともlambda=-omega²から整域又はbinary rankに矛盾。
p0軸はr1,c1/lambda、K可逆ならd0,T=2omega*lambda/(lambda²-omega)、残り一変数。全関係pivot因子lambda,lambda±omega²,lambda²+omega,H=lambda4+4omega*lambda²-omega²、正常pivot因子lambda,lambda±1,lambda±omega,lambda±omega²。全unit領域W1零、fresh±1/±omegaとHの全八次体根もrank8。lambda0/±omega²は幾何条件で除外。K特異境界はlambda²=-omega,T=-lambda,d0、binary係数a4は0又は-2/lambda³。両有限表示をPhi12体で元消去してrank8。これで全Schur分枝を覆う。通常の層別化証明と、公開exact入力/元top像一致/全pivot/例外体の検算を区別する。
現在のunit-repeat残余はrank(P,Q)=1のみ（少なくとも一方非零、二本が比例）。次は片方零又は両方非零比例のchartをU基底でP,Qを一つの方向へ揃えて調べる。非単位重複根の半単純22次元atlasも残る。全三スペクトルの存在/許容性、四単純/CY全被覆、成分/降下は未分類。
比例結合の一方的曲率Ore部分の全排除（v240）：`cubic_third_root_unit_curved_Ore.tex`。実際にB=T[b;f][c;sigma,delta]、sigmaTg,sigmab=q^-1b,delta b=-q^-1h,delta u=d(u)b²（d非零）と提示され、muU1,bomega,comega²なら、G=H+Fbc+C b³+D c³。正常cの最高c4からまずD0、その後の正常bのb4からC0、正常uのb3からFd(u)0⇒F0、G∈T3で二元AS2斉次因子。Dを消さずb4を比較するとc³bの曲率項が混ざるため、必ずこの順序で行う。
全AS2型の通常証明と実際の検算族を区別する。公開検算はTcomm、bx=a xb,by=omega yb,cx=a^-1xc+b²,cy=omega²yc,cb=a bc-a(h0x²+h1xy+h2y²)の有理関数体全係数。全四重なりが零で実Ore AS4整域、mu=(1,1,omega,omega²)。元関係でc4/b4/b3の三段階残差をexact PASS。比例結合全体をこの表示で被覆したとは主張しない。
次の最小課題：rank1 cube結合を一方向へ合わせ、片方零の場合の退化mixed projectionと偶射影rank2、及び両方向非零比例の場合を調べる。非単位重複根の半単純22次元atlasも残る。AS4存在だけやnormal核非零だけでH3としない。
比例結合のS非零も全排除（v241）：`cubic_third_root_unit_proportional_Snonzero.tex`。P=Q=(1,0),S1の元mixed Schur rank1 N=uv^tはpa+sc=-2,pb+tc=ra+sd=rb+td=0。整合条件rt0。r0,t非零ではa6=a11=a150,a16=omega*t²*c/p非零。H0のbc/cb block Kが特異ならyy行(0,a16)がrowKに入らず矛盾、可逆ならyy対角零からT0、binary yy行比較でa20、純cb関係が生じ非整域。t0,r非零は反対代数（primitive omegaを逆にして全仮定保持）で同じAS4整域矛盾。
r=t0ではI1のyb/byとI2のyc/cy成分が零。a15=a160,a10。a50なら(x,c)商free<y,b>/(b²)で指数増大。a5非零なら純xy-yx関係があり、xはB全体で正常正則。A=B/(x)はHS=(1-t)^-3、3二次関係だがb²=c²0を含むため二つの独立三次overlap b³,c³を持ち、dimA3≥11>10となる。正常一次商のAS3正則性を仮定せず直接Hilbert矛盾を用いた。公開exact検算は全元22tensorSchur、rt恒等式、非零a16と全パラメータsyzygyをPASS。
従って全unit-repeat必要残余はrank(P,Q)=1,S0のみ。次はP非零Q0（及び交換）、両方非零比例のS0 atlasをU基底で一方向へ合わせ、退化mixed projection/偶rank2/二方向曲率を解析する。実際の一方的AS2 Ore表示は既にv240で排除済みだが、表示の全被覆は未証明。非単位重複根の半単純22次元atlasも残る。
split二方向曲率Ore族の全正常核（v244）：`cubic_third_root_unit_split_double_Ore.tex`。Aqはbc=qcb,yb=qby-qc²,yc=q^-1cy-q^-1b²のCY AS3 PBW整域。tau(y,b,c)=(y,omega²b,omega c)、B=Aq[x;tau]はmu=(1,1,omega,omega²)のAS4。Gのx次数分解はG3+G2x+a*y*x²+d*x³、x³正常係数でd0、yx²のc²残差でa0、G2∈Z(Aq)2^tau、G3はtau^-1正常三次。
固定二次の全q Smith因子1,q²(q+1)、正常三次は1,q²,q4,q6(q³-omega²)（分母はq冪のみ）。q-1はW1=k*x*y²で因子、q³omega²はW1=k*Gamma、Gamma=y³+q*omega²*bcy+q(2+omega)/3*b³+q²(1+2omega)/3*c³で純base。その他W1零。二条件はgcd1で交わらず、全値H3なし（純baseは一般Ore頂点補題）。全PBW重なり、x次数係数、SmithとPhi9体でのfresh核をexact PASS。一般x依存曲率変形へこのsplit排除を外挿しない。
二方向曲率非split変形の全排除（v243）：`cubic_third_root_unit_deformed_double_Ore.tex`。Bqのbc-qcb=h*x²だけを変形する全q,hの実Ore AS4整域。正常xの付随次数はsplitなので、q-1は全Gにx因子、q³omega²以外はW1零。q³omega²ではW1=k*(Gamma+h*K*x²*y)、K=[2+omega+(4omega-1)q-(1+2omega)q²]/3。h0既排除、h非零はxのscalarでh1へ。原始九乗根の全六埋込をPhi9体で元正常24×8行列rank7としてexact確認。正常核の存在だけではH3にならない。
x局所化degree0のB=b*x^-1,C=c*x^-1,Y=y*x^-1でQ=q*omega,kappa=omega²、BC-QCB=kappa,YB=QBY-omega²q*C²,YC=Q^-1CY-omega*q^-1*B²。z=BC-CB、S3=1+Q+Q²、H=(omega²q*Q²/S3)C³-(omega*q^-1/S3)B³、Z=zY-H中心。元NFでz9=kappa9+(Q-1)^9B9C9、z³*g=Z³+aZ+bC9+cB9、a³(Q-1)^9=27*kappa9*b*cをexact検証。a,b,cの全係数は本文/certificate。
中心一般点E=k(B9,Z)の代数は次数9cyclic symbol(B9,z9)。rho²=-a/3,Z=rho*T,u=(Q-1)^9*rho³/(b*kappa9)*B9でz9/kappa9=1-u(T³-3T)+u²=Norm_{s³=u}(s²-Ts+1)。symbolのcorestriction射影公式でBrauer周期は3以下。曲面period=indexを適用し指数≤3<9、非除法。もし元切断が整域なら次数零商/中心一般局所化も整域かつ有限次元なので除法となる矛盾。これで全族H3なし。正確なGoldie rank3やGの斉次因子分解は主張しない。
一次資料はMax Lieblich, Twisted sheaves and the period-index problem, Compositio Math144(1)(2008)1–31, DOI10.1112/S0010437X07003144。arXiv math/0511244v4 Theorem4.2.2.3 p23のstatement/定義/周辺の印刷された証明を実読し、Eが代数閉標数0体上超越次数2である仮定を照合。深い全証明の独立再監査ではない。PDF digest/URLを公開certificateへ記録。de Jong原論文の著者一次書誌も確認したが、全文DVI取得403のため未読、Lieblichの一次証明を実際の入力とした。公開checkerのPASSはこの外部定理自体の機械検証ではない。
量子Weyl基底の二方向曲率Ore層の被覆（v244）：`cubic_third_root_unit_normalx_Ore_cover.tex`。実際にA=<x,b,c>がxb=omega²bx,xc=omega*cx,bc-qcb=h*x²、B=A[y;sigma,delta]でmu=(1,1,omega,omega²)なら、Ore中山からsigma=(1,q,q^-1)。重みからdelta x=F∈<x²,bc>,delta b=m bx+u c²,delta c=n cx+v b²。F非零はsigmaF=F、Gの全Ore係数がmu固定でxと可換、[G,x]最高係数N*aN*FよりG∈A3となり量子平面商gcdからx因子。F0はx正常。uv非零はscalarでu=-q,v=-q^-1へ。
元の全四三次重なりをexact再生。ybxとycbからkappa(q-omega²)=0,(omega*m+q*n)(q-omega²)=0。q非共鳴はkappa0,n=-omega*m/q、y'=y+m/(q-omega²)*xで両一次補正を同時消去し既排除族へ。q=omega²はshear分母を使わず、x進付随次数がsplitでW1零となり全補正を排除。これでこの実Ore層はyx非可換補正を含め全てH3なし。xのB内正常性は仮定していない。全比例結合の中にこのAS3基底が存在するという全被覆は未証明。
両非零比例結合の六係数正常一次境界への必要被覆（v245）：`cubic_third_root_unit_proportional_Szero_cover.tex`。P=Q=(1,0),S0の元mixed二単元pivotからa3=-omega²A,a11=a12=D,a9=a13=E,a15=a16=a170、A=a2,D=a6,E=a7,Z=a8,T=a21。mixed像はxb-omega²bx,xc-omega*cx,Dyb+Eby+c²+(A+omegaZ)xb,Eyc+Dcy+b²+(Z-omega²A)xc。
even元blockを本文に全表示。T非零はSchur0からa1=a5=a40,D²=omega²E²,a0=A(D+omegaE)/T。D=E0は(x,c)商free<y,b>/(b²)で非AS4。その他D=eps*omega*E、q=-eps*omega²,h=-(1+eps)A/T、yx=xy+(A/D)x²+(T/D)bcの実量子Weyl基底Ore表示へ。標準語数とAS4 Hilbert値からPBW/Oreの実在を証明し、delta x非零障害で全H3なし。
T0,A非零はcross rank1がE=-omega²Dを強制。D0は純x²で非整域。D非零はeven rank2のbinary分解でa0=a1=a4=a50、even像はA*x²+D[x,y]とbc-omega²cb。qomega²,h0,delta x=(A/D)x²の実Oreに入り排除。従って両非零比例結合H3はT=A0に限る。
T=A0,D=E0ならI0が二次元純U²なので二次形式pencilにdecomposableがあり整域矛盾。よって(D,E)非同時零。rank2からa10、even像は[x,y]とD bc+E cb+u x²+v xy+w y²。全必要候補は6係数(D,E,Z,u,v,w)の六関係：xy=yx,xb=omega²bx,xc=omega*cx,Dyb+Eby+c²+omegaZxb0,Eyc+Dcy+b²+Zxc0,D bc+E cb+u x²+v xy+w y²0。D0/E0を捨てず元top像一致を公開exact検算。xは正常、正常化mu^-1。AS4十分性/H3許容性/同型は未分類。
正常一次境界の稠密開集合排除（v246）：`cubic_third_root_unit_normal_boundary_open.tex`。w非零をscalarでw1へ。S=B/xの三関係Dyb+Eby+c²,Eyc+Dcy+b²,Dbc+Ecb+y²から元次数3/4挿入を消去しdim10/15、全83pivotを再生。L=D³+omega*E³+omega²、Cj=D²E+omega^(-j)D+omega^j E²、Δ=D*E*(D³-E³)*(E³-1)*(D³+omegaE³)*(D³+omega²E³)*C0C1C2*L。全関係pivotと正常3pivotの分子/分母がΔ上だけで消えることを逐次gcd割切りでexact確認。固定三次基底b³,bcy,cby,c³、三pivot後の九残差分子idealに(E*(E³-1)*L)^3が入りGroebner零剰余。よって全Δ非零点で正常rank4、Gbar0、Gにx因子がありH3なし。u,v,Z全値同時。D2E3で開非空。Δ零やw0へ一般点rankを外挿しない。
L曲線上の全正常incidence（v247）：`cubic_third_root_unit_boundary_L_incidence.tex`。d³+omega*E³+omega²0、Ω=E*(E³-1)*(E³+omega)*(E³+(1+2omega)/3)*(E³+(omega-1)/3)非零。y'=y+t*x,t=omegaZ/(d+omegaE)でZ0へ、u'=u-vt+t²,v'=v-2t。Γ=omega*b³+c³-d*((omega+2)E³+omega²)bcy+E*(2-(omega+2)E³)cby。全u,vで正常G=Γ+v*Astar*y²x+v*Bstar*bcx+(u*Cstar+v²*Kstar)yx²+u*v*Kstar*x³、四係数は本文とcertificateに全表示。中山逆指標正常核は一本。
検算は関数体QQ(omega)(E)[d]/(d³+omegaE³+omega²)とその上の多項式環[u,v]で元R3/R4を消去。全parameter pivotはu,v非依存定数、dim20/35、固定三次8。境界正常rank3と四補正rank4、残差全零、独立な閉公式との比較を実施。1155余のcubic norm逆元を逐一積で確認し、全分子/分母のsquarefree支持がΩ（次数13）と判定。これで関数体一点だけでなくΩ開集合の全閉点/全u,vに有効。`cubic_function_extension.py`,`cubic_parameter_polynomials.py` は分数の構造同値でなく差の零を使い、非定数u,v pivotで割らない。低次dim20/35だけから全AS4十分性を宣言しない。
L開集合の実AS4認識と中心三次（v248）：`cubic_third_root_unit_boundary_L_recognition.tex`。S=Sklyanin(d,E,1)はE非零/E³≠1からIS Theorem1.1/Cor6.1でKoszul AS3。点曲線discriminant=(d³+E³+1)^3-27d³E³=3(omega²-omega)(E³-1)^3非零、proper ellipticでnoetherian domain。六関係とxB1の元rank10で1-regular xを確認。w3=y*r_y+b*r_b+c*r_c+u*x*r_xy=r_y*y+r_b*b+r_c*c-u*r_xy*x-v*r_xy*yの自由tensor恒等式、modxのb³係数1からW3(S)への全射。LBS2.6(5),2.7の全仮定を照合し、全u,vで実際のnoetherian quadratic Koszul AS4整域を認識した。元22軌道quartictopの全巡回と六関係への包含もexact再生しμBthetaを確定。単にdim20/35でAS4としたのではない。
G=Gamma_tildeは正則正規、R=B/GはAS-Gorenstein3 index1 muR1とcubicHS。Sdomain/Gbarregularより正常正則列x,Gを交換し、Rでもx正則。したがってRdomain iff U=(R[x^-1])0 domain。C=B^thetaではxcentral,muC1で、同じdegree0局所化Uを持つ。
中心Ψ=G+Q*y³+vH*y²x+(uH+v²J)yx²、Y=E³,Q=(omega+2)(1-Y)、H=[3(omega+1)Y+(2omega+1)(E²d+Ed²)-omega-2]/(Y-1)、J=[(1-omega)E²d-(2omega+1)Ed²]/(Y-1)^2。全交換子と閉係数、同じΩ支持をexact検証。UでT=y/xとすると中心ψ=Q T³+vH T²+(uH+v²J)T。全中心やPI次数はまだ主張しない。
境界translation位数9とアフィンPI還元（v249）：`cubic_third_root_unit_boundary_L_PI.tex`。S_CはSklyanin(d*omega,E*omega²,1)。Γ0非零δ正常、δ=(1,omega²,omega)。canonical central cubic g0の倍ならdomain/非scalarδと矛盾、よってTHCR像非零。その次数付き分数環k(E)[t±;tau]で次数3Γ0の共役は関数体上tau³であり、正常式からδに等しい。δの楕円曲線作用が非自明order3なのでtau正確order9（包絡Nakayama order3とは別）。Smith–Tate Theorem3.7 r1の中心生成次数3/9からZ(S_C)3=kg0、Ψ0は非零scalar*g0。Γ0³ modg0非零THCRdomainと斉次次数からΨ0,Γ0³は代数的独立。
D=(C[x^-1])0はgrD=S_CのPBW整域、GK3。中心ψ=Ψ/x³,g³=(G/x³)^3の最高記号が上の独立二元なのでk[ψ,g³]多項式。F=k(ψ,g³)、D_FのF一次独立な長さn語へψ^i g^(3j),i+j≤nを掛けるとbinom(n+2,2)f(n)≤binom(10n+3,3)、よってGK_F≤1。有限次元ならPI、そうでなければPappacena–Small–Wald Theorem5（affine semiprime over any field）で標準恒等式を得てDへ制限。U=D/gもPI。PI次数9、fullcenter、U prime/domainやH3は主張しない。
一次入力：C.J.Pappacena,L.W.Small,J.Wald, Affine semiprime algebras of GK dimension one are (still) PI, GlasgowMathJ45(2003)243–247, DOI10.1017/S0017089503001204, arXiv math/0211330v1 Theorem5 pp4–5と全印刷証明を実読。任意の基礎体、semiprime/affine/GK1の仮定を照合。Smith–Tate KTheory8(1994)19–63、標準g0/THCR, Lemma3.5と証明, Theorem3.7と証明を著者PDFで実読しcenter3/9入力だけ輸入。両PDF SHA/URLはv249公開certificate。有限checkerはscalar/discriminant/order/GK不等式の多項式算術を再生し、幾何・GK/外部定理の全形式検証とは称さない。
次の最小課題：PIアフィン切断の全中心、PI次数、Brauer周期・generic Goldie rank、整域性/有限大域次元。v0u0はsplit頂点で既排除、v0u非零はx scalarでu1、v非零はx scalarでv1へ。高次数全語4^nの行列は避け、B_n=(B_(n-1)⊗V)/(B_(n-2)⊗I)を既存乗法行列から再帰構成して中心degree9とδ²-normal degree6を求める。
独立代数体例の中心部分環上自由階数81（v250）：`cubic_third_root_unit_boundary_L_finite_center.tex`。K=QQ[t]/(t6-9t³+57),d=t,E2,omega=(1-t³)/7,u1,v0,Z0。既約な全6埋込を同時にexact検証し、B2..B10とnormal-cut次数2..10を元関係の再帰商から再構築。Cの中心次数1/2/3/6/9は1,1,2,3,7、cut A=C/Gは全基底で1,1,2,3,5。正常δ²次数6は115×30rank28/kernel2で、G²以外に一本ありG倍がdegree9中心。全パラメータへ外挿しない。
A中心9の既知四元x9,x6Ψ,x3Ψ²,Ψ³に独立なz9を選び、元語係数をcertificateへ保存。Q=A/(x,Ψ)、z9像非零、元3生成元関係にz9を加え次数13まで完全再帰消去すると[1,3,6,8,9,9,9,9,9,8,6,3,1,0]、13零以後一次生成で全零。Hilbert完全列からz9正則、x/Ψ/z9中央正則列、graded NakayamaとHSからAは多項式部分環K[x,Ψ,z9]（次数1,3,9）上自由rank81。fullcenterやPI次数9は未主張。
再現：`computations/verify_cubic_third_root_unit_boundary_L_finite_center.py`、汎用 `cubic_incremental_graded.py`。B_n=(B_(n-1)⊗V)/sum image(B_(n-r)⊗I_r)を全接尾関係から作り、元関係の左右作用をC/Aでdegree10、Artinianfiberで13まで再代入。全中心kernelの独立性と全交換子もexact。入力は最小多項式と元6関係/G、outputcertificateはz9/Ψの元語、全数値、33統一検算へ追加。
固定例の全中心・素性・PI次数9（v251）：`cubic_third_root_unit_boundary_L_finite_CSA.tex`。A=C/Gは中心部分環S=K[x,Ψ,z9]上free81。中心fiber x1,Ψ0,z91を斉次商degree12/13各81の左右乗法から復元。係数整環を109,t15,omega63へ還元（体Kからの体準同型ではない）。81基底のcentercommutator rank80とregulartrace Gram det45mod109の正のwitness、元全関係行列再代入/Gram対称性/整数overflow上限を確認。ゼロmodpから一般点upperrankを推論せず、char0free81で既知の次元上限と非零minorから同基底/center1/nondegtraceを持ち上げる。
よってgeneric A_Fは81次元central simple degree9、Z(A)はS上integralかつFracS内なのでSの整閉性からfullcenter=S。torsion-free orderのgeneric simpleからA prime。任意のalgclosedchar0kへの6埋込でU prime,Z(U)=k[ψ,z],PIdegree9。de Jong/Lieblich period=indexからRdomain iff Udomain iff Brauerperiod9。まだperiod1/3/9のどれかは未決定で、H3と宣言しない。
再現 `verify_cubic_third_root_unit_boundary_L_finite_CSA.py` はSympy+NumPyを使用。NumPyはint64 mod109だけでfloatなし、内積最大81*108²=944784<2^63、各積直後にmod。source Z/Psiの全分母109unitを確認し、固定fiberの全元関係を81×81生成元行列に再代入。Gram SHA/非零det/center次数をcertificateへ。全パラメータのfullcenterを一点から外挿していない。
次の最小課題：このfixed UのBrauer周期と有限大域次元。もしUがdomainかつfiniteglなら、中央平面上のFrobenius orderでNakayamaδ³1という事実から、height1 hereditary localizationのramification指数が3を割ることを導き、Brauer purity/Br(A2)=0/de Jongで周期≤3を強制できる可能性がある（まだ未監査・公表定理でない）。必要な局所order/codifferentとGorenstein finitegl⇒hereditaryを一次資料で照合してから使う。これが成立すればdomain+smoothを同時排除できる。現時点でfixed例すらH3排除済みとはしない。
全L/u/vへの中心持上げ、Ω零点/他Δ曲線、w0、片方零結合、非単位重複根atlas、全CY/四単純/成分/降下も未完成。
文献整合性の監査メモ：Smith–Tate, K-Theory8(1994)19–63, 著者PDF https://sites.math.washington.edu/~smith/Research/tate.pdf の導入と、Chan–Gaddis–Won–Zhang, Ozone groups of Artin–Schelter regular algebras satisfying a polynomial identity, MathZ310(2025)69, DOI10.1007/s00209-025-03777-9 の2.8–2.10本文を実読した。後者2.10はproper elliptic PI Sklyaninのcenter固定自己同型をscalarとするが、本直接正常核とSmith–Tate Lemma3.5の非scalar正常化、および上のtau9認識との整合性に問題があるため今回輸入していない。2.10末尾の「tauの冪も非linear」とする推論は、3-torsion translationとなる冪を別途確認する必要がある。新規性と正誤表の有無は未確認。PI次数nとprojective order次数を混同せず、一次資料の規約を照合する。非scalar正常元だけで位数9やPI degree9を推測して公表しない。
四単純の新しい全除外chart（v228）：`cubic_detminus1_spectral_exclusion.tex`。as4固定6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0のREADME、plan、COVERAGE、該当CLAIMS、DETMINUS1全文・自己監査・certificate状態を確認。nu=mu^-1なのでa→a^-1と後二基底交換で同じmu-chartになる。四族被覆/AS十分性/同型は輸入せず、H3域に次の直接証明を与えた。
mu=(a,-a,i/a,-i/a),a4≠±1ではU²,mixed,V²の二次重みが分離して二重次数が存在。各平面に関係がなければ自由二生成の次数7が128でAS4値120を超え、domainなら純二元関係は高々一本なので両平面はAS2。混合三次の重み±ia,±a^-1は1にならず、純U三次重み1はa6=1、純Vはa6=-1を要して同時に起きない。従って全Gは片方のAS2純三次となり因子化、H3なし。a4=-1境界は既証二固有値必要集合±1に反し空、残るa4=1境界は四単純集合{1,-1,i,-i}のみで未分類。全det負一又は全四単純をこのchartが覆うとは主張しない。公開verifierは全パラメータLaurent多項式の非零因子・共鳴・境界特性多項式と128>120をexact PASS。出典/仮定/未実行の上流検算はas4_imports.jsonに記録。
四単純の残る共鳴上の全被覆、全CY、全成分・境界、intrinsic族降下は依然未完。

## Frobenius双対とnormal orderの周期障害（v252）
固定例T=A/(x,Psi,z9)の最高次数は12。全補次数pairing rankは1,3,6,8,9,9,9,9,9,8,6,3,1で完全。lambda(a*v)=lambda(nu(v)*a)の規約でnu=(y,omega²b,omega*c)、exact位数3。公開verifier/certificateは `cubic_third_root_unit_boundary_L_Frobenius`。全六埋込みに有効。
原稿の条件付き命題：中心k[s,t]上有限自由なCSA orderで相対双対V_eta、eta^m=1、全高さ1完備化normalならBrauer周期|m。局所trace双対はpi^{-(e-1)}V、radical共役の剰余中心上位数eからe|m(e-1)すなわちe|m。真のBrauer留数次数はeを割る。m倍はA2上不分岐。P2で残る無限遠直線上のsecondary residue相殺とP1の単連結性から無限遠留数も0、BrP2=0で消滅。整域ならde Jongで次数|m。
一次資料：Daniel Chan, Lectures on Orders (16 May2011), https://web.maths.unsw.edu.au/~danielch/Lect_Orders.pdf、SHA256 2280d86df8844091d96311d226ec82fdb9c721929fe2faab0df7810c08b33b19。Thm10.8/Cor10.9/Prop10.12(全印刷証明)、Thm12.5(全印刷証明)、Thm15.1(statement、証明は原資料でも省略)、Example15.4(1)(説明全文)、Thm15.6(statement)を実読。深い入力の独立証明再監査ではない。
相対双対も解決：Tの全81語基底をS基底へ持上げ、top functionalのpairingはgraded Nakayamaで完全。基底次数≤12と生成元次数1からtwisted cyclic係数は定数/xだけなのでA/(Psi,z9)次数12/13のx可逆行列で全81×4等式をexact確認。Hom_S(A,S)=A_nu(12)、nu(x,y,b,c)=(x,y,omega²b,omega c)、affine版も位数3。

## 有限大域次元の局所order認識と固定例の排除（v253）
固定E2,u1,v0は全六埋込みでH3なし。原稿 `cubic_third_root_unit_boundary_L_order_obstruction.tex` に通常の証明。DVR trace dualがfree左加群なら自己単射次元≤1。完備化の単純左右加群は元orderの有限projective分解をbase changeして有限pdを持つ。極小分解の最後の非零Extから全単純pd≤1、従ってhereditary。格子鎖標準形のblock n_iとprojective columns P_iに対し、regular module=⊕P_i^{n_i}、trace dual=⊕P_(i-1)^{n_i}。FrobeniusとKrull–Schmidtから全n_i同じ、巡回block行列がradicalを左右生成しnormal。前節の周期障害から有限大域次元ならperiod|3。一方H3の整域条件ならperiod=index9で矛盾。実際の周期、整域性単独、正確Goldie rank、全L曲線は未決定。
外部局所分類入力：John Voight, Quaternion Algebras, GTM288(2021), Chapter21 pp343–352, DOI10.1007/978-3-030-56694-4_21。出版社一次HTML https://link.springer.com/chapter/10.1007/978-3-030-56694-4_21 の§21.3.1/Lemma21.3.3/Prop21.3.7の印刷証明、Theorem21.5.1 statementと印刷された参照（証明はHijikata–Nishida§1へ委託）、§21.5.3、Remark21.2.8のdivision版拡張を実読。原著Hijikata–Nishida/Reiner本文は未読で、読んだとは主張しない。この標準局所分類は外部入力、block双対計算とFrobeniusからnormalへの推論を本原稿で明記。機械検証の対象は固定例の相対双対であり局所分類自体ではない。
E2,v=Z=0,w1の全uも排除済み：u非零はxのscalar同型、u0は純base正常三次のOre頂点。次の具体的課題：L/Ω全パラメータの中心z9と自由81・CSA9を持上げれば同じ障害を適用できる。generic中心だけでは全Ωを覆わないので分母と例外locusを保持する。

## E2全u,vの多項式中心核と自由81（v254）
公開 `verify_cubic_third_root_unit_boundary_L_polynomial_center.py` はK[u,v]上で元の全relation moduleを次数10まで構成。全relation pivotがパラメータ定数であることをassert。中心9の136列行列は、行の先頭に限定せず任意の定数単元成分をpivotとして選び、既選pivot行も戻して消去。131pivotで残余全零、核free5。全5ベクトルの元四交換子を再代入して零。u1v0で既知4中心単項式と独立になる核を選ぶとZ9は37語で、x0の5語係数は定数。新Z9を用いるArtinian境界商もdims1,3,6,8,9,9,9,9,9,8,6,3,1,0、全元左右作用次数10/13でPASS。既証の全u,v AS4とx/Psi正則性、HSから全点でk[x,Psi,Z9]上free81。全中心/CSA9/素性が全点で同じとは結論しない。
単純な有理関数体上の逐次RREFは次数6で係数膨張し、4分程度進展しなかったため終了し、多項式定数単元pivot法へ切り替えた。後者はパラメータ分母を一つも使わず全u,vの証明に至った。一般Eの拡大体への移行でも、この定数pivot・再挿入方法を優先する。
次の最小課題は非空パラメータ開集合のH3排除。既知u1v0 CSA中心fiberの座標を新Z9へ移し、相対free81の固定中心fiberに対する中心rank80 minorと非零trace行列式をspreadすれば開集合が得られる。全中心とCSA次数を全点へ外挿しない。残る例外集合とE可変への持上げは別問題。

## E2全相対双対と稠密開集合のH3排除（v255）
公開 polynomial_Frobenius verifierはuniform Z9のT境界全13pairing完全、A/(Psi,Z9)次数12/13の二81行列のinverse denominatorがパラメータ定数、全81×4 twisted cyclic identity零を確認。Hom_S(A,S)=A_nu(12)、nu=(x,y,omega²b,omega c)位数3を全u,vで確定。
新中心9の(1,0)特殊化を旧基底(x9,x6Psi,x3Psi²,Psi³,oldZ9)へexact展開し、元語へ再代入PASS。a0=0、cold≠0。正の既知fiberはΨ0,Znew=b=a0+cへ移る。bの全六次体係数はuniform center certificateのold_positive_fiber_in_new_coordinatesに保存し、mod109では83。
uniform familyはP=K[u,v]上でも表示中心部分環P[x,Psi,Z]にfree81：Artinian商基底からgraded inductionで全射、各fiber同Hilbert値なので核は一般点で零の自由加群部分として零。固定中心fiberV=A/(x1,Psi0,Zb)もP-free81。traceGram T(u,v)と四交換子行列M(u,v)からU=D(detT)∩{rankM=80}を定義すると、(1,0)を含む非空開集合。全U点のgenericCSA9/fullcenterSが正のfiberから従い、相対Frobenius位数3と局所order障害で全UをH3排除。判別式/minorの展開係数は未計算、行列条件による開集合の定義と非空性の証明である。
scalar x作用の重みは(u,v)=(2,1)。UのGm飽和の不変閉補集合をP(2,1)へ写すと真の閉集合、従って有限。v0は全排除済みなので残るH3必要候補はv≠0, u/v²∈有限集合F_(d,omega)。Fの列挙・許容性未完。H3許容性自体の相対開性を仮定していない。次はfinite fiber判定のweighted成分を使ってFを計算する。u0v1のpositive witnessもv256で確定。

## 第二軸排除と例外比計算の行列モデル（v256）
u0v1の公開second_CSA validatorはp109,t15,omega63、fiberPsi0,Znew83で中心1、trace determinant64、元六R2/G3/中心fiber関係行列零をPASS。自由81は標数0全族で既知、非零minor/traceをliftして次数9CSA/fullcenter、相対双対ν3からH3なし。x scalarによりu0全v非零、原点vertexで第二軸全排除。E2で必要残余はuv非零の有限個の非零比のみ。
次の例外比探索用に、v1,u=a、p109における固定center fiber(Psi0,Z83)の81次元行列モデルをGF109[a]上で構成。全relation pivotとx逆行列分母がパラメータ定数、生成元matrix polynomial degree bounds0,6,5,5、中心交換子行列も多項式。private input `/workspace/work/spectral_remaining/unit_L_modular_parameter_fiber.py`、model JSON同dir。まだ標数0の例外列挙の証明ではない。次に有限体でtrace/rankの悪いaを探索し、polynomial determinant/weighted-component gcdの非零resultantをliftして有限例外比の厳密被覆を狙う。有限体の点全列挙のみから標数0の空性を結論しない。

行列探索の実行状態：公開 `explore_cubic_third_root_boundary_L_parameter_fiber.py --prime 109 --root 15 --output /tmp/L_model.json` と `explore_cubic_third_root_boundary_L_parameter_grid.py --model /tmp/L_model.json --output /tmp/L_grid.json` で再現可。GF109全109点で中心1、trace退化はa10,84(rank27)のみ。他の107点は非退化。これは固定center fiberの有限体観察で、標数0の例外比列挙ではない。prime/rootを省くexact modeも用意し、private先行版ではK[a]上の全行列を実際に構成済み（係数Horner変換を使用）。全生成元次数0,6,5,5。次にこの標数0行列をp1021,t169（六次poly根）等へ還元し、trace determinantの次数上界と補間、異なる中心fiberとのresultantを調べる。有限体gcd1だけでは次数落ちで隠れる標数0因子を排除できないので、少なくとも一方の次数保存又は正の固定次数Sylvester minorを確認する必要がある。

## E2全二変形・全ZのH3排除（v257）
有限例外比は残らない。公開two_fibers validatorは二center fibers(Psi0,Znew=b/1)の全モデルを先にK[a]上で実構成。全relation pivotとx inverse denominator定数、生成元の全非零係数で2deg_a(R)ji≤di+1-dj、basis filtered degreesの総和486をexact確認。trace Gram det次数≤486。モデル全rational denominatorsをp1021,t169でunit確認し、487点det評価から補間、追加8点を検査。両還元degree486で次数保存。
bar f_b=340[(a²+228a+306)(a²+471a+147)(a²+573a+1012)(a³+317a²+112a+981)]^54。bar f_1=340[(a+95)(a+110)(a+579)(a6+805a5+322a4+741a3+284a2+740a+787)]^54。全係数掛け戻しPASS、9次二因子のBezout1を再代入、486次二式のresultant965mod1021非零。次数486保存と正のSylvester resultantによりK[a]でもcoprime、全六埋込みの代数閉体上共通根なし。有限体点全列挙だけからの外挿ではない。
trace非退化開集合上で中心rank一定の補題：regular trace dual basisからE(a)=Σe_i a e^iを作ると半単純fiberごとに中心projector、被約base上で同じ恒等式が成立しrank局所一定。irreducible openで一点のcenter1から全点CSA。各fiberのa0でpositive trace/center1/source関係行列零を確認済み。従って二trace開集合は全aをcover、全E2,v1 genericCSA9/fullcenter。x scalarで全v非零、v0既排除、L/ΩのshearでZ任意も排除。E2,w1の全正常一次境界はH3なし。実際のBrauer周期や整域性単独の決定は不要・未決定。
次は全L/ΩのE可変へ中心9と二fiber obstructionを持上げる。必要なgeneric fieldはQQ(omega)(E)[d]/(d³+omegaE³+omega²)、既存custom cubic extensionをSympy DomainMatrixのFieldへ包むか、中心kernelのconstant-pivot解法をcustom scalarで実装する。u,v polynomialの非定数divisionは避ける。固定E2で非零resultantはE方向へopenにspreadするためのwitnessだが、中心9の存在をspecialpointからgenericEへ外挿してはならない。

## 全L/Ωのアフィン包絡のPI次数9（v258）
Dの中央psiはleading canonicalg0非零倍。全lambdaでgr(D/(psi−lambda))=S_C/g0 elliptic THCR、domain。Rains arxiv2107.13540v2 Thm2.13から中心もfiltered deformation、有限中心性をleading inductionで持上げ、Hilbert leading coefficient比[(1+t+t²)/(1−t)²]/[(1+t9+t18)/(1−t9)²]→81から各fiberPI9。Dはk[psi]にTHCR語基底でfree、∩全lambda(psi−lambda)D=0。全fiberのMat9多重線型恒等式がDに降り、逆にIdDはgrD=S_Cの恒等式を与えるのでDのPI次数exact9。全L/Ωと全u,vで有効。Uのprime factors degree≤9だけが従い、Uのfullcenter/素性/正確degree9は未主張。
一次資料RainsPDF SHA256 6b8ce29a6a0a8533fde76b98af8784229b4e09769e4e6628163d565b0078c050、arxiv2107.13540v2 (17Feb2022)。今回Thm2.13/前置translation説明pp15–16、Prop2.9の印刷された全証明とobstruction p11、Example2.5後Remark p14を再読。高次Rees代数のcenter liftは自動でないと明記されており、D/Uの中心への外挿はしない。新しいas4輸入なし。
直接genericE計算：公開 `explore_cubic_third_root_boundary_L_function_center.py --output /tmp/L_function.json` はGF109(E)[d]/(d³+63E³+63²)でu,v polynomial、relation/center pivotsはparameter constantsのみ。default Sympyはdegree5が14.74秒、degree6未了で停止。private FLINT backendではdegree5が4.2秒、6が32.15秒、7が132.02秒。degree8で係数膨張し、center9未到達なので結果未主張。inverse cacheと--fixed-uv u1v0/--fixed-uv v1を追加、次の最小課題は固定枝でgenericEのZ9を構成すること。--prime 0はchar0の同じcustom cubic extensionを使う。既存CF/parameter scalarはDomainMatrixを通さずGradedAlgebraと独自unit Gaussianに直接使用できた。
将来の理論的経路：D PI9とgrD PI9からreduced traceでcenter liftを得られるかを検討する。ただしmaximal order性、traceのD内整性とleading trace互換性が未監査なので、現時点の定理ではない。

## 関数体探索とtrace-closed中央商による次の証明（v259からv260で原稿統合済み）
GF109関数体、u1v0、重み0を選ぶと46列/41constant pivot/free5、残余零と全核の元四交換子零を153秒で確認。inverse cacheと最小係数degree/sparse row pivotで改善。char0ではdegree4後の係数膨張で停止、modular zeroをchar0上界にしていない。公開function_center helperはcompute_center(...)が(out,A,piv,ids)を返し、CLIも維持。
以下の経路はv260で正式な通常証明として原稿へ統合した。全H3分類の完成ではない。
1. v258でCのPI次数9（Dと中央Laurent拡大が同じ）を確定。LBS Cor2.7の実際の結論はAuslander-regular/CMも含む。Cはconnected graded finiteglなので、任意有限生成projectiveにgood filtrationを入れ、grの有限graded free resolutionをliftすればfinite free resolutionが得られ、splittingからstablyfree。Stafford Thm2.10/Cor2.11よりCは自身のtrace ring、有限中心、中心normal。
一次資料：J.T.Stafford, Auslander-Regular Algebras and Maximal Orders, J.LondonMathSoc(2)50(1994)276–292, DOI10.1112/jlms/50.2.276。著者所属機関一次repositoryPDF URL https://deepblue.lib.umich.edu/bitstream/handle/2027.42/135495/jlms0276.pdf?sequence=1 は直接取得403。ただしweb索引から同じ一次PDFのpp276/277/286を実読でき、Thm2.10 statement（Introにも掲載）、Cor2.11のstatementと印刷された証明（McConnell–Robson13.9.8/13.9.11参照）を確認。全PDF/全Thm2.10証明を読んだとは主張しない。LBS Cor2.3/Cor2.7も一次PDFの該当全文を再読。
2. 同PI次数中央商補題案：C trace closed PI n、x中央正則、S=C/x domain PI n。R=imageZ(C)⊂Z(S)、L=FracRと置く。Cの次数n reduced CHを還元すると全S元がR上次数≤n integral。従ってS_Lはdivision（nonzero元のannihilatorからT因子を除けばinverse多項式）、Q(S)に等しい。K=Z(Q(S))の各元もL上degree≤n、char0primitive elementから[K:L]有限≤n。Q(S)のmaximal subfield M/K degree nとM/Lのprimitive elementを使うとn[K:L]≤n、従ってK=L。還元traceはL-linear cyclicかつt(1)=nなのでQ(S)のreduced traceに等しい。任意z∈Z(S)に対しtbar(z)=nz∈RとなりZ(C)→Z(S)surj。homogeneous liftsはGm-equivarianceで選べる。v260で正式な中央商補題として証明した。
3. Γbar∈H=S/(g0) elliptic THCRのdegree3 normal sectionは非零、degree9の零因子DΓを持つ。ΓH1=H1Γの共通base divisorを比較するとDΓ=τDΓ。τはfreeなorder9 translationなのでDΓは一つのreduced9点軌道。Q=H/(Γbar)はその9点THCRのdegree≥4では全sectionsに一致（低次数dim1,3,6,8、以後9）。Z(H)9は商楕円上degree3 line bundleでbasepointfree、Smith–Tate Thm3.7のproofからZ(S)→Z(H) surj。軌道上非消滅の中心z9を選び、2でZ(C)へliftする。Q[z9^-1]は9点cycle crossed Laurent ringで、Q/(z9−1)=Mat9(k)。
4. A=C/Gのx,Psi正則性は既証、上のz9はQで正則。central regular sequenceとHSによりS0=k[x,Psi,z9]上A-free81。boundary central fiber(x0,Psi0,z1)がMat9なら、同じ正のtrace/center argumentでgenericCSA9、fullcenterS0、primeが全L/Ω全u,vに従う。AS-Gorenstein dualizingとS0のdegree sum13からrelative dual A_delta(12)、delta³1。局所order周期障害で全L/ΩのH3排除が従う。v260で原稿統合、有限9cycleチェックと全文組版を完了。
既存E2二fiber計算はこの経路とは独立なpositive verificationとして保持する。新規as4結果は輸入していない。

## 全L/Ωの完成したH3排除（v260）
正式な証明は trace_center節と orbit_exclusion節。中心持上げ補題：trace-closed Tと中央regular x、商S domainが同PI次数nなら、R=imageZ(T), L=FracR上S_LはCH次数nからdivision=Q(S)。中心K/Lはbounded algebraic度n、maximal subfieldのprimitive degree n[K:L]≤nからK=L。還元traceはL-linear cyclic/n正規化なのでreduced trace、全z∈Z(S)にnz=tbar(z)∈R、従ってcentre全射。kernel xZ(T)。CにStafford2.10/2.11を適用しZ(C)/(x)=Z(S_C)。
正常Γbar∈ellipticTHCRのzero divisor degree9はΓH1=H1ΓとbasepointfreeLからτ-invariant、自由order9translationの一軌道。Q=THCR/(Γbar)はdegree≥4でreduced9pointsの全sectionsに等しい。quotientE'のdegree3 central line bundleから非消滅z9を選び、SmithTate centre lift+上のtrace lemmaでCへ持上げ。Q/(z9−1)=k9⋊C9=Mat9。x,Psi,z9 centralregular sequence、Artinian total81、A centre polynomial/free81。boundary fiberMat9からgenericCSA9/fullcentre/prime。ASG dualityでrelativeHom=A_delta(12)、dehomogν³1。有限glならnormal localorder→period|3、整域ならperiod=index9、H3不可。全w1,L0,Ω非零,全Z,u,vを排除。
有限checker orbit.pyは6561 basis products、trace Gram determinant9^81、Hilbert regular-sequence total81をPASS。外部Stafford/Rainsやgeometryをcomputer proofしたとは言わない。v260主原稿組版PASS、overfull/undefined参照引用なし。E2 exact二fiber/resultant proofは独立な検証例として残した。
次の未解決：Ω0は固定omegaで33幾何点（E0三点、E³1九点、d0三点、二追加cube値各九点）。この点数はΩfactorとLからの数え上げで、まだ全normal kernel/AS4条件を判定していない。特にZ-shearが失敗する点とW1 jumpを含む。ほかのΔ曲線も残る。proper Sklyanin中央拡大にcanonical中央三次が存在すれば、一般的な9軌道障害の同じ証明を適用できる可能性がある。既存EG等の正確な仮定を調べる。E3でall u,v・weight0centreを独立計算中、normal-field centre claimの証明依存ではない。

## 全proper elliptic正常一次境界の排除と二軸/99点（v261）
Φ=DωYBC+Eω²YCB+(Y³+B³+C³)/3+ω²ZBC+(v/2)Y²+uY。元B二次関係right untwist後、y/b/c関係を1,ω,ω²倍すると∂Y/∂B/∂CΦにexact一致。LやΩ、Z-shearなし。H3 Gbar nonzero（零ならx因子）、properSのg0倍ではないのでellipticTHCRにnonzero normalγ、関数体共役からτ³=δ、τexact9。EG Thm3.3.2(ii)でnonscalar centralψ≤3、ZS degree1/2zero・degree3kg0なのでleadingcanonical。以後v260のcentre lift/9orbitMat9/free81/relativeν3/period obstructionが適用でき、全proper elliptic層H3なし。W1次元1を仮定しないのでΩ外のkernel jump/shear失敗点にも有効。
EG primary arxiv0709.3593v4、PDF SHA256 bb1730c492553a7e233a82e54b712f20b20a1e6d60e13324740f0d5580797901。Thm3.3.2(i),(ii)と§8.3 p32の全印刷証明を実読。iiはgeneric不要、genericが必要な3.4.5と区別。k=Cの定理は有限係数体embeddingとfiltered centre≤3有限線型系のrank降下で任意char0に適用。IS Thm1.1/Cor6.1も再読（同既知PDF/hash）。深い外部証明全体の独立再監査や機械検証ではない。
proper criterion DE*((D³+E³+1)³−27D³E³)≠0の補集合はaxesと9直線D+ω^aE+ω^b。既知Δ0必要条件を各直線へ代入しradical、axesとnonPHS D³=E³1を除くと、全て共通11次h(t)（本文の二linear+三cubic因子）。正規化D=−ω^b(t+1),E=ω^(b−a)tで99distinct points。全line degree11、共通E polynomial degree33、複数lineの残存重複なし。原点はPHS必要条件で除外。公開elliptic_reduction validatorは全potential derivative、Hesse factor、10 Δfactorsの代入/gcd/squarefree、normalized h一致、重複をexactPASS。
次は二軸と99点の正常核・cut判定。99点は45個のQ(ω)既約factor表示（9lines×[linear,linear,cubic,cubic,cubic]）で計算できるが、field conjugacyをgeometric isomorphism quotientと混同しない。w0と一方零coupling、非単位rootの22tensor atlasは依然別課題。
独立診断：E3の全u,v・weight0 centre9をchar0で46cols/41constant pivots/free5、全核の元交換子zeroまで85.35秒で確認。小JSONをboundary_E3_center_diagnosticとして保存し、一般証明の依存とはしない。

## 現在の正常一次境界：六軸点のみ（v263）
二軸のSmith標準形は(1,1,1,D³+ω²)、(1,1,1,E³+ω)。関係pivotは非零軸変数のmonomial、Smith変換はconstant determinantで全非零軸値に有効。軸は各3点へ必要制限。六軸点の全u,v正常三次は各一本、原稿axis-incidence命題のG_E/G_D。元四正常式の多項式再代入までPASS。ZはD+ωE≠0によりshear除去可能。u=v0は頂点障害で排除。残りはv1,u=aとv0,u1。
非軸99点は45算術ケース（9 Hesse線×2 linear+3 cubic）を厳密計算して全て境界正常核零。Q(ω)とQ[q]/(q6+q3+1)で次数3/4商を全元関係から再構成し、正常行列4列の非零4×4 minorを各ケースで確認。三つのcubicには(ω,t)=(q6,1/(q−1)), (q3,1/(q−1)), (q3,q+q^-1−1)を用い、対応する既約因子恒等式も検証。固定ωでの全99幾何点を覆う算術埋込みであり、moduli同型商ではない。従ってw1正常一次chartのH3候補は六軸点だけ（全Z,u,vの許容性は未完）。公開verify_cubic_third_root_unit_boundary_99.pyとcertificateが証明を再現する。
次の最小課題は六軸切断の整域性/有限gl判定。private exact診断でE0,u1,v0のC/Gはcentre次数1,2,3,6,9が1,1,2,3,5、ambient中心9は7。候補canonical中央三次Psi=y³+vxy²+ux²y。全u,v中心9持上げ、free81、正のcentral fiberの構成を検討するが、現段階でこれらを定理にしていない。proper ellipticの被約9点orbit証明をfat triangle境界へ無条件には適用しない。w0、一方零coupling、非単位重複root atlas、全CY/成分/相対降下は引き続き未完。as4の新規輸入なし。

## 正常一次chartの非零w全排除：現行frontier（v264）
六軸点の全Z,u,vもH3なしと証明。E0,D³=-ω²型では全u,v多項式係数のcentre9重み0行列46列を41constant unit pivotsで消去し、全5核を元交換子へ再挿入。Psi=y³+vxy²+ux²y、選択Z9のx0像はパラメータ非依存。A/(x,Psi,Z9)はArtinian Hilbert列1,3,6,8,9,9,9,9,9,8,6,3,1,0、総81。H3仮定で既知の全Hilbert級数とgradedNakにより、三中心元代数的独立/自由階数81。有限次数だけでAS4全次数を主張しない。
元x0,Psi1,Z0 fiberの補助中央hによる斉次化で、p109,t4,ω63の正則trace det108、centre rank80 minorが非零、元関係81次matrix再挿入PASS。正のminorが標数0にliftし、全uv共通fiberCSA9。従って全uvでgenericCSA9/full polynomial centre/prime。相対Frobeniusν3からfiniteglならperiod|3、domainならsurface period=index9で矛盾。他軸はB(D,E,0,u,v;ω)^op=B(E,D,0,u,v;ω²)及びG_E^op=G_Dを元関係で照合し、domain/左右finiteglの反対環不変性で排除。moduli同型とはしていない。全w≠0正常一次chartがこれでH3から除外された。
公開axis_center.py/axis_CSA.pyのdefault Sympy再生PASS。v264主原稿LuaLaTeX PASS clean。既存36 unified+10個別新規=46validators across runs（単一46一括実行とはしていない）。新規外部定理/as4輸入なし。
次はw0。探索段階ではD≠0をD1正規化し、E≠0,E6≠1の境界正常行列14×4のSmith因子(1,1,1,(E³−1)(E³+ω²))を得た。したがってこの開集合ではE³=-ω²だけが残り得る。E0、D0、E³=±1のfresh検算と全pivot supportの監査は未了なので、まだ全w0被覆定理にはしていない。E³=-ω²をPhi18体で扱うと全u,v正常核は27×8、constant7pivots、残余零で一本。v0は既存Ore除外に入る可能性があるが、その適用/パラメータ規約を監査してから用いる。v非零の正常切断/中心を次に判定する。一方零coupling、非単位重複root atlas、全CY/成分/降下も未完。

## 正常一次chartの完成した排除と次の未被覆層（v265）
両非零比例結合は元22tensorから六係数正常一次chartへ被覆され、そのw≠0はproper elliptic/99点/六軸点、w0も以下で全排除された。従ってunit-repeatのrank(P,Q)=1,S0において、残るのは片方のみ非零のP0又はQ0である。非単位重複rootの半単純22tensor atlas、四単純残余、全CY/成分/相対降下も未完で、全H3完成ではない。
w0全値の必要被覆：D1,E=eで元関係pivotと正常行列の分母支持がe(e6−1)のみ。14×4正常行列を行分母払後Smith因子(1,1,1,(e³−1)(e³+ω²))、変換det定数/掛け戻しPASS。e=±ω^jの6値、D0/E0両境界もfresh4×4 minor非零で核零。従ってe³=-ω²のみが残る。Phi18でE=t,ω=t³−1、全uv正常行列27×8が7unitpivots/free1。Zshear可、全uv中心3は8cols/6unitpivots/free2、中心9は46cols/41unitpivots/free5。全核元式再挿入、中央Psi/Z9のx0像はparameter非依存。
A/(x,Psi,Z9)のArtinian列は1,3,6,8,9,9,9,9,9,8,6,3,1,0。H3の既知HSとgradedNakで中心3元代数的独立/free81。x0,Psi1,Z2の全uv共通fiberがp109,t4,ω63でcentre1、trace det1の正のwitnessを持ち、標数0CSA9へlift。全uv full polynomial centre/genericCSA9/prime、相対Frobeniusν3からfinitegl⇒period|3、domain⇒period=index9で矛盾。有限次数から全AS4性を推論していない。
公開verify_cubic_third_root_unit_boundary_w0.py、w0_center.py、w0_CSA.pyはdefault Sympyで全PASS（左右元関係挿入含む）。既存36 unified+13後続個別=49 validators across runs、単一49 replayとはしていない。主原稿w0節を追加し、LuaLaTeX PASS、未解決参照/引用/overfullなし。新規外部/as4輸入なし。
次の最小課題：片方零結合P=(1,0),Q0,S0を元22tensorで解析する。重みω middleはrow/col b²に一単元pivot、残り3×4 rank1条件。even H0 rank2と合わせて全AS2–Ore被覆を証明できれば既存curved_Ore排除を適用できるが、その被覆は未証明。private unit_onezero_probe.pyに元middle/evenを構成し、T=a21非零のSchur条件をa2=±ωa3,a15=±ωa16の四符号に分け、rank1minorとのGroebner系を探索中。T0、projection退化を捨てない。実際のAS2–Ore部分だけは既に証明済みなので再証明しない。既存解決済みのL/ΩやE2中心計算へ戻らない。

## 片方零結合の新しい必要被覆（v266）
元22tensorのP=(1,0),Q0,S0ではc²行が恒等零なのでB/(x,y,b)=k[c]。H3正常式Gc=ωcGをこの商に写すと純c³係数が零。Ore表示を仮定しない。正常三次の残る7係数へ進める。
T=a21=0のeven対称blockは右下零、全rank2ならcross rank≤1。cross0なら純U²二関係pencilのrank1因子でdomain外、従ってcrossrank1、純Uのrank2二次Qが一本あり二元AS2を定める。b-mixedはUb+bUだけ、domainなら両射影自動同型。c-mixedの両射影(Uc及びcU)が同型で、evenのbc/cb両射影係数が非零なら、六関係の標準語T0語·b^i c^jが張る。AS4全Hilbert値との一致で独立になり、T0とb拡大が実際に埋込み、結合則が自己同型型の一方曲率Ore表示を与える。既存curved_Ore除外が適用可能。この条件領域は全排除。全片方零層、T非零、c射影退化、bc/cb係数零はまだ排除していない。
証明はcubic_third_root_unit_onezero_projection.tex。元22tensorからmiddle/even/c²行零と全2×2射影minorを再生するpublic validator/default Sympy PASS、v266主原稿LuaLaTeX PASS clean。数学的Ore認識は通常証明で、有限標本を全被覆証明に使っていない。36既存unified+14後続個別=50validators across runs。
T非零探索は大きな10変数Groebner出力を直接追わず、middleの残余3×4 rank1を単元pivotでパラメータ化する。private a16=s≠0 chartではa17=λ(ω+1)s,a15=λ²(ω+1)s,a6=λr,a12=λh,a7=r+κs,a11=λh+κλs,a8=(ω+1)A+κr,a3=(ω+1)A+κ(r−h),a9=r,a13=h,a2=A。Schur条件からλ4=ω。λ=ωならh=r、λ=−ωならκ0で他Schur全式が零。λ=±iω型、s0境界は未整理。T=s1の二型をGF109で各5標本検算し、四つはdegree3/4 dims20/35,正常核零、全零r/A等では23/55かつ正常核零。標本のみなので全値除外とはしていない。plus型のexact Q(ω)(A,r,κ)正常行列をprivate unit_onezero_plus_exact.pyで構成中（degree3まで到達、degree4未了）。これはT,sの全値正規化をまだ証明していない限定sliceで、全atlasの被覆と混同しない。
次はT0の射影退化閉集合又は上のT非零rank1chartの正常核。非単位重複rootの22tensor、四単純、全CY、成分/相対降下も未完。新規as4輸入なし。

## 重複1の片方零結合もT0全排除（v267）
前節の射影条件はT0で自動的に成立する。even cross列R=(a2,a6,−a11,a15),S=(a3,a7,−a13,a16)はrank1。R0ならmiddle最初二行の最後二列が零、domainが強制するUb射影rank2から全行の最後二列が零となる。a8,a9,a12,a17=0となって第二行零、矛盾。S0もbU射影rank2から第四行零の矛盾。従ってR=ρS、ρ非零。純U関係Q=[[a3,a7],[−a13,a16]]はdomainからdetQ非零。元middleのminor M[(bx,by),(xc,yc)]=(ω+1)²detQ、M[(xb,yb),(cx,cy)]=ρ²detQ。従ってc-mixed両射影可逆で、bc/cb両係数も非零。前節のAS2–Ore認識と既存curvature因子障害で全T0を排除。
この通常証明を同じonezero_projection節へ系として統合、元二minorとR0/S0強制零行を公開checkerでdefault Sympy exact PASS。v267主原稿LuaLaTeX PASS clean。全unit-repeat残余は片方零結合かつT≠0のみ。非単位重複root22tensor/四単純/全CY/成分/相対降下は未完。
次はT≠0。a16非零rank1chartのλ=±ω等を整理し、正常核を判定する。限定T=s1,λ=ω,h=rのexact3parameter sliceはdegree4まで商dims20/35を構成済み。DomainMatrix.rankは係数膨張で約4分停止したため中断し、最小次数のpivotを選ぶ8列sparse normal消去へ変更して再計算中。有限体10標本のnormal核零を全値証明にせず、s0/λ=±iω/係数零の境界を保持する。今の最優先はこのT非零残余の必要被覆である。

## T非零第一rank-one型の全値排除（v268）
P1,Q0,S0,T≠0,a16=s≠0のrank1残余はλ=a17/((ω+1)s), Schurからλ4=ω。λωではh=r、T,sはtop diagonal weights xb³/y²bc/b²c²でT=s1へ正規化可能。三係数A,r,κの全モデルを元22tensorから構成し、source pivot/denom支持はA,r,κ+r,κ+2r,J=(ω+1)A+κr+r²,H=−(ω+1)A+κ²+3κr+3r²,L=A+ωr²。全非零開集合の正常44×8行列は8個の係数体定数pivotで全核零。
残余scalar weights(A,r,κ)=(2,1,1)を使い、r1の6曲線A0,κ−1,κ−2,J0,H0,L0、r0κ1の1曲線とrκ0のA1/0二点で全境界を被覆。各一変数関数体で元関係・正常8pivotsと全分母/元画像6minorを再計算し、bad polyは全てQ(ω)でlinear split。重複除去後11fresh pointsは核零又はnonAS4 Hilbertで排除。J0一般点dims3/4=22/46を20/35に切り詰めていない。
public cubic_third_root_onezero_plus.py + verify_cubic_third_root_unit_onezero_plus.py はdefault Sympy全再生PASS（独立Schur二恒等式、top weights、元even Schur掛け戻し含む）。主原稿onezero_plus節LuaLaTeX clean PASS。これでa16T非零,λωの全層がH3なし。先行50＋新1=51validators across runs、単一51一括未実行。新規外部/as4輸入なし。
次の有力な通常証明（まだ未統合・未完成）：λ−ω,sT非零ならκ0,h自由でeven crossR=−ωS。bは全U上scalarω、c上ω²の正常元となり、中山固定三次上そのnormalizerは恒等。Gの正常b式はω²なのでG零。元関係像の同定を監査して正式化する。λ=±iωはh=r±iκs、他Schurからr=−(1±i)κs/2,A=∓iωκ²s/2のはず（private i_branch exact factor式）。T=s1後κ1/0の二点にscalar正規化し、Q(ω,i)でfresh核を判定できる。
a16=0,T非零の着想：Schurとmixed minorからa15=a17=0。domainのUb/bU射影を使うとa12=a11,a7=a9、a6=λa9,a11=λa13（λ≠0）。Schurからλ=±ω、a2=εωa3。符号が同じならcrossR=λSでb正常、μ固定三次上normalizer固有値は±1しかなく、要求固有値ωに矛盾する可能性がある（bのJordan補正も固有値議論なら許す）。符号が逆かつa3≠0ならa13=a9≠0を強制。x,b,cの量子Weyl AS3基底、yをOre変数とする表示に戻り、δ(x)にbc非零係数T/(λa9)が出る。既存normalx_Ore_coverのF≠0証明は曲率二方向仮定を使わないので、一方曲率にも適用して排除できる見込み。実際Ore被覆と全符号/零境界は未監査のため、まだ全unit-repeat完成とはしない。この最小課題から継続する。

## スペクトル・全単冪領域の現行到達点（v293）
強いintrinsic H3のAS4包絡は相異なる中山固有値をちょうど三つ持たない。全Jordan型の必要還元、重複1の全22tensor atlas、非単位重複rootの独立・非零比例・零b²列を全て排除した。全H3分類の完成ではない。全単一固有値非CYも排除済み。全CY切断、全成分・境界、相対降下は未完成。

### 完成した証明の入口
三固有値全体の結論は `papers/sections/cubic_third_root_nonunit_zero_column.tex` の `thm:cubic-three-eigenvalue-sector-empty`。重複1はunit_onezero_completion、非単位重複rootの非零列はnonunit_independent、nonunit_proportional_open、nonunit_proportional_Tzero、nonunit_isolated、nonunit_degenerate_selfの各節を経由する。Q=0の別分枝を含めて必要被覆を保持している。
最後のp=r0ではcがU上で正常、c u=F(u)c、FJF^t=−ω²J。元二列はLb=T c²,bL=ω²T c²（L=mx+ny）。domainからL,T非零。F²L=ω²Lで、Lが固有vectorならc全正常、B/cにLb=bL0が生じHilbert矛盾。L,F(L)独立ならCHからFdiag(ω,−ω)、self offdiagのみ。generator/top変更でs=m=n=T1。元rank2条件の12linear式はrank7で一変数Dへ。全値source画像はcx=ωxc,cy=−ωyc,(x+y)b=c²,b(x+y)=ω²c²,bc=−((D+ω)x+Dy)(x+y),cb=−ω²(x+y)((D+ω)x+Dy)。unit6minor/係数体分母で全値同定。正常33×7は定数7pivot、全source/normal例外はD(D+ω/2)(D+ω)。fresh D0,−ωは正常核零、D−ω/2はB3dim22。これで最後の列も全排除。
最新v275主原稿LuaLaTeX clean PASS、新checker default Sympy PASS。累計58validators across runs、単一58全再生は未実行。統合replayソースの現行候補は0、古いキャッシュ出力を新実行と扱わない。新規as4/外部定理輸入なし。新規性未確認。

### 四単純位数4の必要atlasと第一rank型（v276）
スペクトル(1,−1,i,−i)の元twisted-cyclic四次topは16次元。二次weight groupsは0:(xx,yy,bc,cb)、2:(xy,yx,bb,cc)、1:(xb,yc,bx,cy)、3:(xc,yb,by,cx)。0block対称、2block交代、1/3paired。trace成長の分母1+(r0−r2)t²+t⁴と1+(6−4r1)t²+t⁴から必要rank型は(2,2,1,1),(2,0,2,2),(0,2,2,2)のみ（重み0,2,1,3順）。各B3重み次元5。
最後の(0,2,2,2)は全H3排除済み。H0zeroから八係数零、domainでa3,a4,a7,a9全非零、対角でa3=a4=1,a7=a9=q。残りA=a5,h=a6,k=a8,E=a13、rank2Mの全minors GB13で必要被覆。A=E0はq=t²,k=t,h=±tの全t非零Oreモデル、x/y正常固有値により全Gがx又はyの因子を持つ。残余は対角十軌道へ。二軌道正常核2は全x因子、七軌道正常核零。唯一残るq−1,A1,E0,h=i,k−iの正常核1はG=c²y−bcx/2+i cbx/2。
この最後の包絡はb²+c²,xy−yx,xb+bx,xc+cx,yb+i by−i xc,yc−i cy−xb。normalx開集合の次数零環はYB−i BY=iC,YC+i CY=B,B²+C²0,2C²Y−BC+i CB0。原点characterの自己Ext1はY方向1。H3 Serre=(-1)[2]をnormalxで同定するとH(Y,B,C)=(Y,−B,−C)、Ext1に恒等作用。twisted Serre traceの符号から非退化交代対が必要となり矛盾。S(L)=L[2]だけで作用自明を仮定せず、唯一のY方向に実際に作用が自明と確認した。
通常証明はcubic_four_simple_order4_rankC節。公開checker default Sympy PASS（16top/rank/GB13/全値sourceunitminor/十軌道/因子/例外G/dehom/character接空間）。v276 main LuaLaTeX clean PASS。累計59validators across runs、単一59全再生未実行。全四単純又は全H3完成とは呼ばない。新規外部/as4輸入なし、新規性未確認。

### 四単純位数4の全完成（v278）
残る(2,2,1,1)はpaired M=P Q^tの巡回四binomial式とdomainから全十support、六chartへ。primitive iの選択変更とb/c交換で三chartを見れば十分。P02はH2純平方からa14zero,a0v非零、H0rank2 Schurから純x²又はy²。P13はH0純y²とH2純c²で全排除。P01/Q23はPfaff a0a14=−pqとH0Schurの(1+i)pq/a0非零で矛盾。元16tensor/全support/全Schur恒等式公開default Sympy PASS、v277主原稿clean PASS。
最後の(2,0,2,2)はH2zero。H0=[[0,0,u,v],[0,L,B,C],[u,B,D,0],[v,C,0,−iD]]。u=v0はdomainがD,BC,Ah非零を強制しMに3minor−A²C。片方のみ非零は純bc/cb。uv非零をu1,vρへ、H0SchurでL0,CρB,D(ρ²−i)0。B0はdomainE,k非零だがM3minorE²。B非零をB1へ、rank2の単元ρpivotで全条件hk+ρA²−iρ²=0,h(E+ρA)=0,k(E−ρA)=0,ρhk−E²+iρ=0。
全値は二つのOre曲線(h=k=D0,A=t,ρ−it²,E±t)と18有限対角軌道へ。曲線のb,c正常固有値の二条件は固定三次の全五基底方向でgcd定数、全t非零正常核0。有限点はhk非零2点、hのみ/kのみ各4点、D1かつt4−iの8点。QQ[z]/(z8+1),i=z4で全18根の元商dims3/4=20/35、正常28×5又は25×5全rank5。新checker default Sympy PASS、v278主原稿LuaLaTeX clean PASS。
従ってスペクトル集合{1,−1,i,−i}は全H3排除。既存一般chartと合わせ、全非零aで(a,−a,i/a,−i/a)も全排除。ただし全det負一スペクトルの被覆ではない。通常証明はfour_simple_order4_rankA/rankB節。累計61validators across runs、単一61全再生未実行。新規as4/外部定理輸入なし、新規性未確認。

### 全四単純の四曲線／有界有限点への必要被覆（v279）
四単純H3スペクトル全体は、ある共通位数N≤96の有限集合、又はλ_i=α_i t^{n_i}（α共通位数M≤24、t非零、有限位数も含む）の四方向n=(0,0,1,−1),(0,1,−3,2),(0,1,−2,1),(1,−2,−1,2)で必要被覆される。Mは24の約数とは限らない。これは存在やH3十分性・群oid分類ではない。
証明はfour_simple_spectral_curve_atlas節。二次指数u、Gの実際の全三次support、topの実際の全四次supportの有理span Lを使う。二次u/三次vだけの平面ではquartic全変数被覆が不可能なのでrankL≥3。rank4はu,v,wと追加cubic又はquarticのdeterminant、三型の最大det(48,96,48)/(36,72,36)から共通位数≤96。rank3は全top/Gがprimitive kernel n重み0なので、μが有限位数でも実際のtorus作用とG固定を得る。正のregrading deg=N+n_iのHilbertpole4からsum n_i0とΣr_s s²=2Σn_i²。全21×20×35指数kernelとquartic被覆で1062方向、sumzeroと置換/反転で10型。domain Segre上界とmomentで各I2重みrankが一意。六型は共通一次因子の通常証明で排除。残四型のphase代表はSmith最大因子≤3minor gcd、最大gcd(12,24,12)と符号から共通位数M≤24。
公開checker default Sympy PASS（全60平面、全kernel、全rank整数解、因子pair、全det/gcd）、v279主原稿LuaLaTeX clean PASS。累計62validators across runs、単一62全再生未実行。新規as4/外部定理輸入なし、新規性未確認。

### rank三supportのphase削減と二方向完成（v280）
全support格子rank3のうちn=(0,1,−3,2),(0,1,−2,1),(1,−2,−1,2)はそれぞれ(1,t,t^-3,t²),(1,t,t^-2,−t),(t,t^-2,t^-1,t²)へ必要削減した。topがmultilinearだけならmiddle像が六pair直和になりdomain/rank6からskew、という補題を使う。全M≤24位相/quad衝突/quartic支持を公開default Sympy PASS。
最初の方向はb,yが正常、Gにx³とybc双方が必要。B=A0[b;g]、A0はxy,yc skewとAxc+Ccx+Dy²のAS3。片側xc係数零は正常yとdomainから逆向き独立quadが生じるので不可。Ore/Koszul双対からA0 AS3、topのxyc非零によりhdetg=ade、μb=ade。正常bの固有値比較a³=de=ade⇒a=μb1、μx1と重複。全rank3 chart排除。
第二方向はU(y,c)のAS2関係y²+κc²、他五pairskewなのでB=T[x;f][b;g]。g(x)=q x、g|Uの平方scalar d²共通、μb=q d²。非因子Gにx³とU²b双方が必要、正常bからq³=d²=q d²⇒q=μb1、μx1と重複。全rank3 chart排除。
通常証明はfour_simple_curve_phase_reduction節、公開checker（全phase、domain自由語恒等式、正常izer ideal）default Sympy PASS、v280主原稿LuaLaTeX clean PASS。累計63validators across runs、単一63全再生未実行。新規外部/as4輸入なし、新規性未確認。
重要なscope：有限位数のμで追加の非零n重みtop/G supportがある点はrank4有限部分に保持する。上の斉次chart排除から曲線上の全finite ambientを排除したとは呼ばない。

### phaseなし最後のrank三chartも完成（v281）
(t,t^-2,t^-1,t²)の元10tensorを公開一般diagonal_top helperで構成。paired rank1二式とdomainで六multilinear係数非零、a1=1,a2=p,a4=q,a5=r,a7=pr,a6=pr/q。H0のU(xb,bx)/V(yc,cy) crossは[[q,r],[−pt,−prt/q]]=column(1,−pt/q)*row(q,r)、全rank1。対称rank2H0で両射影同型はcrossrank2を要求するので、純U又は純V関係が必ずある。前者x,b正常、後者y,c正常。残る混合関係の両向き係数は逆向き関係/domainで非零。全六逆順pairの標準三次語20とAS4dim20から全overlap零、量子平面上逐次Ore（最後は二次derivation）を得る。normalbase元の中山固有値は他三生成元への正常化scalar積。
Gはx²y,b²c双方を持つ。純Uの場合normalx scalars(a,b,c)にa=b²c=abc=λx、従ってac1,bλx。変形yc/cy対xbの自己同型固有値が1対λxなので変形非零ならλx1⇒t1。純Vの場合normaly scalarsa²=b²c=abc=λyからa=b,c1、変形xb/bx対ycの固有値λy対1なのでλy1⇒t²1。変形零はskew、いずれもfour-simple H3なし。
通常証明はfour_simple_last_rank3_curve節。default Sympy元10tensor/全rank1式/cross外積/両normalizer ideal/逆向き自由語identity PASS、v281主原稿LuaLaTeX clean PASS。前節の中山scalarとgeneratorの表記をλ_bに明確化した（数学的主張の変更なし）。累計64validators across runs、単一64全再生未実行。
従って残る全四単純の必要被覆はrank3の(α,β,t,γ/t)、phase共通位数M≤24と、rank4共通位数N≤96の有限部分だけ。finite tでも追加supportは有限部分に保持する。

### 最後のrank三phase chartも完成、全四単純を有限化（v282）
全四単純H3の中山は半単純で、共通位数N≤96の有限集合に限る。全support格子rank3を全排除した。これを全四単純又は全H3の完成とは呼ばない。
通常証明はfour_simple_zero_pair_rank3節。正常一次zとφ_zについてμ_B(z)=hdet_B(φ_z) zを証明：中心はAe-resolutionの二中央作用のchainhomotopyからNakに固定、B^{φ^-1}でz中心化、既存RRZ Thm0.3 fullscalar右公式μ_twist=μ H^-4 ξ_hdetHを適用。一次資料RRZ Thm0.3/5.4(a)/0.3の証明を再確認（PDF SHA28b4b649089bbebb722664452c665f8a43ad5b8d9589925b2f97818322736e25）。これは既存文献のscalar項を新たに明示適用したもの、as4新規輸入なし。
n=(0,0,1,−1)ではb,cはU上対角正常、FrobeniusからM:β−α,γα^-2又はS:αβγ1。Sの平方衝突γα²/β²は別分枝として保持した。α5/9は孤立因子、α3は追加7tensor chart(α,1,t,α²/t)で正常xのhdetからφxが全固定三次に1倍、必要固有値αと矛盾。平方衝突を省略してSのαβ±1を主張しない。残りSはskew/交代rank1不可からαβ=±1、非零Gからα6=1。Mもα6=1。七位相型の全default Sympy列挙。
M非符号2型はtop6のpureAS2因子、S非符号minus2型は唯一purecube。S primitivecubeはtop10 crossrank1からpureU又はpureV、前者binary因子、後者正常b scalara³=d³=λ=adeと変形ad=eからλ1。S符号(1,−1,t,−t^-1)はpure-square対称blockをdomainで消し、交代rank2のPfaffからpurebc/cb。PBW固定基底x³,xy²,ybcの非因子に第一/第三必須、正常bでa³=de=ade⇒λb1。
M符号(1,−1,t,t^-1)はxy/yx交代blockをdomainで消しI0⊂x²,y²,bc,cb。bc/cb射影rank1は純AS2 U、cb変形Pの正常izerfg=diag(−1,1)がU中心xy+yxを負にするのでP0、Ore正常固有値でλb1。射影rank2はbc=P(x²,y²),cb=Q。P/Q独立ならx²,y²中心、G=Ax³+Bxy²+Cyxyのx交換子C(xy+yx)(yx−xy)からC0⇒因子x。P/Q比例ならpaired rank1の全成分非零でP両平方係数非零。正常b scalars(A,±A,1,A²)によりtop固有値A4、G固有値A3、上hdet補題でA1,λb1。全rank3完成。
公開checker default Sympy PASS（全phaseと平方追加分枝、元10/9/10/6/7tensor、rank/Pfaff/中心freeword/normalizer ideals）。v282主原稿LuaLaTeX clean PASS。累計65validators across runs、単一65全再生未実行。新規性未確認、通常homological証明の全機械検証とは呼ばない。

### 全有限四単純の39必要ラベル軌道（v283）
共通位数N≤96の最小位数四根集合62,290,587個を全exact走査。二次衝突13,359,699、三次共鳴2,223,885、有効quartic全変数被覆134,703、raw全support rank4は5,338。Frobenius r_s=r_-s,sumr6,自己−1偶数,domain cap_s=dimtensor_s−1のDPで604集合/115 Galoisラベル軌道。
元巡回topの一monomial列をdomainから強制零にし安定化、9軌道top非退化性喪失、2軌道multilinear-only skew。全I2 character解のKoszul群環recurrenceで次数≤12に負multiplicityの出る解を全排除（各degree/component/負整数をcertificateに保存）⇒69軌道。強制pairskewによる共通一次因子と純AS2二元因子で40軌道、既排除位数4を除き39軌道/145根集合。残る位数5,6,7,8,9,10,11,12,13,14,15,18、各軌道数1,4,2,6,5,3,1,10,1,2,2,2。全指数代表と各必要relation characterはfour_simple_finite_atlas節/certificateに保持。Galoisラベル軌道はintrinsic同型商ではない。
公開verify_cubic_four_simple_finite_atlas.pyがC++17 sourceをtmpdirへcompileして全走査、Python標準整数で全115軌道を再検算。浮動根/有限体なし。C++rankは元行minorのみで各項|入力|≤4、det絶対上界4!4^4=6144、64bit overflowなし。公開full replay PASS、v283主原稿LuaLaTeX clean PASS。累計66validators across runs、単一66全再生未実行。原稿の有限表は必要被覆で、AS4存在・正常核・H3十分性を含まない。

### 全support sieveで20ラベル/45根集合へ（v284）
39必要ラベルの全I2 characterで、topの全非空count support SとGの全非空count support Tを走査した。rank0blockが触るorbitを零、monomial列domain pruningを安定化、全変数被覆/nonmultilinear、各blockのmatching rank上界を課す。残る強制pairskewから正常生成元zを決め、未知q_ijを向き付きpair scalarとする。
正常一次hdet補題とG正常式により、全zとw∈S∪Tで∏_{i>z}q_zi^{w_i}∏_{i<z}q_iz^{-w_i}=λ_z。φ_zとμが可換対角なので共通固有liftを選べることを通常証明に明記。小整数行列A/右辺bを作り、Smith U A V=D全恒等式とdetU/V±1を検算。整数左核ℓでℓb≠0modNなら排除、保存111本のℓについてSmithと独立にℓA0/非零剰余を再検証。
因子条件も全Tへ適用：旧common-skew/pure-AS2に加え、指数u²z/vz²、uz skew、vz/zv/u²内のrank1関係なら向き別書換えで共通z因子。単純sampleでなく全S/T/character被覆。39中19ラベル全排除、20 Galoisラベル/45根集合、残位数5,6,7,8,9,12、全1306必要support片。各片はcharacter番号/S,T bitmask/正常gen bitmaskで小証明書に保存。非空・AS4・正常三次存在・H3十分性を主張しない。
通常証明はfour_simple_support_sieve節、公開verify_cubic_four_simple_support_sieve.py default Sympy全PASS、v284主原稿LuaLaTeX clean PASS。累計67validators across runs、単一67全再生未実行。全20ラベル/片はcertificateから再開する。新外部/as4入力なし、新規性未確認。

### 元orbit全非零層とLaurent torus閉包（v285）
20ラベルの全top orbit非零maskを走査した。rank1blockは完全rectangleが必要、全(r+1)minorの1項matchingは不可、2項はroot付きbinomial。純二変数U²内に支持されるsource列の空間はdomainでrank≤1なので、その全2minorも課す。pairに正確に支持される一つの列があれば（block全体に限らず）forcedskew、q_ij=−H_ji/H_ijで実orbit係数比へ戻す。
全binomialは整数Smith行格子（飽和しない、torsion全成分保持）でLaurent指数を正規化、係数をQQ(ζ2N)でexact加算。minorが1非零monomialなら全層排除、2項でroot比なら必要binomialを追加して閉包。3項以上の残余や非root係数比を勝手に零としない。normalizer top/G式も同じorbit係数へ課す。全S/Tと必要characterを保持して13ラベル/33根集合、23非零mask/157G-support。
さらに(7;0,1,2,4)の唯一mask/片を通常Ore証明で排除。base S(y,b,c)は三pairskew、x追加はδ(y)=d_yc²,δ(b)=d_by²,δ(c)=d_cb²、全d非零。逆向き係数/domainとB3dim20の全overlap零からB=S[x;σ,δ]。G=Ax³+B ybc双方、μx1なのでGx=xGがδ(ybc)=0を要求するが、δvolumeは三つの異なるPBW単項式yb³,y³c,bc³を全非零係数で持ち矛盾。
現行必要被覆は12 Galoisラベル/31根集合、22非零orbit層/156G-support片。ラベルは(5;1,2,3,4)、(6;0,1,2,3),(6;0,1,3,5),(6;1,2,4,5)、(7;1,2,5,6)、(9;0,1,4,7),(9;1,3,4,7),(9;1,3,6,8)、(12;0,1,4,10),(12;1,3,4,7),(12;1,3,7,10),(12;1,4,6,10)。全必要orbit係数A,bと各G bitmaskをcertificateに保持。
公開verify_cubic_four_simple_orbit_torus.py default Sympy/数体全PASS、v285主原稿LuaLaTeX clean PASS。C対角generator重みでA C^t0も検証、effective_dimension=m−rankA−rankCはtoric必要式だけの対角商次元、実AS4/moduli次元ではない。累計68validators across runs、単一68全再生未実行。

### 対角商零次元片の全数体判定完成（v286）
全81零次元必要片を整数Smith全torsion成分と対角torus作用で30点へ漏れなく被覆した。A C^t0、rankC=p−rankAを全片で確認し、連結対角torus像が解の単位成分と一致するので自由座標を1へ正規化できる。全有限成分を保持。共通根位数5,6,9,10,12,18のQQ(ζL)上で全点をexact判定：26点正常核0、3点B3dim22/B4dim46で非AS4、1点はN9(0,1,4,7)のB=S(y,b,c)[x;σ], σ=ζ9^6で正常核pure S3。既存一般cone頂点補題lem:cubic-skew-cone-vertexから最後の点もH3なし。通常証明はfour_simple_zero_dimensional節、公開verify_cubic_four_simple_zero_dimensional.py/certificateに全81片から30点への被覆と各exact rankを保存。default Sympy PASS、v286主原稿LuaLaTeX clean PASS。累計69validators across runs、単一69全再生は未実行。
現行必要被覆は5 Galoisラベル/10根集合：N5(1,2,3,4)51support片（toric商dim1/2/3の個数18/18/15）、N6(0,1,2,3)11片dim1、N6(1,2,4,5)9片dim1、N7(1,2,5,6)2片dim1/2、N9(1,3,6,8)2片dim1/2。合計75必要片。存在やH3十分性は未判定。Galoisラベルをintrinsic同型商と呼ばない。

### 正次元片の元rank条件と五曲線への削減（v287）
75正次元必要片にCの独立列のorbit係数1 gaugeを追加し、Smith全torsion枝を保持して16表示へ。全元weight blockの(r+1)minorを数体Laurent多項式としてexact計算、単項式単元を除く。N5の唯一dim3表示は二minorの差−4ζ10³で空。他14の非自明表示では全minorのgcdが実際にminorとして現れるのでrank上界locusは証明書の単一式と一致（一般点のみでない）。一つは全torus。有限になった12parameter点はQQζ20/24/28/36でfresh全Hrank6、B3/4=20/35、W1核0を確認して排除した。N6(1,2,4,5)ラベル全体が消える。
現行必要被覆は4 Galoisラベル/9根集合、五つの一変数表示。positive_rank_certificateのbranch0,3はN5(1,2,3,4)、branch7はN6(0,1,2,3)、branch10はN7(1,2,5,6)、branch13はN9(1,3,6,8)。元75片から全表示への被覆・位相・係数Laurent指数・全rank式を公開certificateに保持する。通常証明はfour_simple_positive_rank節、verify_cubic_four_simple_positive_rank.py/positive_finite.py default Sympy全PASS（後者のdegree被覆assert追加後も再実行PASS）。v287主原稿LuaLaTeX clean PASS。累計71validators across runs、単一71全再生未実行。

### 三・四固有値領域の全排除完成（v288）
全H3包絡の中山作用は相異なる固有値を高々二つしか持たない。四単純全体も排除した。単一固有値は1だが、単冪部分の自明性は未証明。全H3分類の完成ではない。
通常証明はcubic_four_simple_final_curves節、thm:cubic-four-simple-sector-empty。v287の五曲線branch0,3,7,10,13を各F=QQζL(t)で一変数化。元Hの六列source minorΔ、全次数商のpivot分子/分母、正常行列の全pivotと係数分母/parameter定義域を記録し、非零積P上で全底変更を保証。generic正常shape26×4,23×4,22×4,17×2,14×2は全列rank。Pの全数体既約因子を積へ掛け戻し、各既約性を確認し、E=F[t]/fで元H/商/正常行列をfresh計算した。全因子数11,5,13,8,9、定義域内因子数8,2,12,5,6、F上次数和20,3,23,11,9。全有効例外もHrank6、B3/4=20/35、正常核0。有限標本・数値根は使わない。
公開verify_cubic_four_simple_final_curves.py/certificateに全pivot多項式と全例外の数体係数・source/商/正常rankを保存。default Sympy PASS（因数積一致・既約性assert追加後もPASS）、v288主原稿LuaLaTeX clean PASS。累計72validators across runs、単一72全再生未実行。以前の全被覆の独立再監査、新規性確認、全homological証明の機械形式化とは呼ばない。
次の核心は単一固有値1の全CY・単冪持上げと、既分類領域を含む全intrinsic群oid・成分・相対降下。as4-reference固定SHA6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0のCY_COMPLETE/UNIPOTENT_UNTWIST本文とCOVERAGEを対象を絞って読んだが、全CY統合定理を新規監査済み入力として輸入していない。前者の有限許容atlasだけでは本研究の全幾何学的分類・成分・降下の完成にならない。

### 最大単冪Jordan4領域も全排除（v290）
中山が単一固有値1・サイズ4単一JordanブロックのH3は存在しない。通常証明はcubic_principal_unipotent_vertex節thm:cubic-principal-unipotent-empty。既存の単冪ねじり解除B=C^H,H=expNと正常三次輸送を使用し、as4の新しい全CY分類やprincipal存在定理は輸入せず元tensorから独立構成した。
反巡回66方向のN総作用核12を元256語で計算し、指定12語座標を単位化。col33純x0²からa11zero、a9zeroならpurecolumnが3a10+5a8zeroを強制し、x0,x1を殺した商が自由二元/(x2²)へ全射して指数成長矛盾。従ってa9unit1。top最高weight6は交代tensorだけ、六pairのsource minor±1、全関係が逆順commutator＋低weight。AS4 Hilbertと順序語の張りから全次数weighted PBW、grC可換poly。
N固定三次Fの先頭は可換Sym³N核（weight0,2,3）なのでweight≤3、J=(x0,x1,x2)のJ²に入る。HはJを保ちBtwist後もJ²は同じ。P=πk[x3]の全tails自己拡大を2×2行列で構成し、x3恒等化後のJ三成分はA f(n+1)=D f(n)、A,D下三角対角1。元全係数のまま検証。F∈J²は一次条件を課さず、Ext1(P,P)3次元、shift単冪det1。一般のSerre trace補題b(v,w)=−b(Tw,v)からdimE奇数ならdetT−1が必要となり矛盾。S(P)=P[2]だけから作用恒等と仮定していない。
公開verify_cubic_principal_unipotent_cover.py/vertex.py default Sympy PASS、対応certificateに元12核、全rank6三枝とA/B全係数gauge、weighted六関係、拡大monodromy、可換三次核を保持。coverは幾何学的必要被覆でAS十分性を主張しない。v290主原稿LuaLaTeX clean PASS。累計74validators across runs、単一74全再生未実行。Serre/tailsの通常証明を機械形式化したとはしない、新規性未確認。

### 単一固有値のJordan(3,1)も全排除（v291）
全18元CYtop核を独立構成し、col22=a6 x0²からa6zero。a12zeroならcol12=a4 x0²でa4zero、x0,x3を殺した商が自由二元/(x1²)へ全射し指数成長矛盾。従ってa12unit1。weight(0,1,2,0)の元六関係unitminor−1、最高項はgrC=k[x0,x1,x2][x3;δ]、δ=(h x0²,h x0x1,−3h x0x2+2h x1²),h=a4。AS4 Hilbert＋順序語の張りから全次数weighted PBW。Nδ=δN、Nx3zeroなのでPBW上Nは可換baseだけ、三次核6次元/最高weight2。F Nfixed⇒F weight≤2⇒J=(x0,x1,x3)のJ²。全係数のpoint P=πk[x2]の自己拡大はExt1=k³、shift M=[[1,0,0],[1−2a11+3a16a4−a7−2a9,1,a16−a14],[3a4,0,1]]、det1, (M−I)³0。前節のgraded Serre determinant補題で全Jordan(3,1) H3 empty。通常証明cubic_jordan31_unipotent_vertex節、公開checker/certificate default Sympy PASS、v291主原稿LuaLaTeX clean PASS。累計75validators across runs、単一75全再生未実行。新規as4定理輸入なし、新規性未確認。

### 単一固有値のJordan(2,1,1)も全排除（v292）
通常証明cubic_jordan211_ore_vertex節thm:cubic-jordan211-unipotent-empty。元32CYtopでweight2唯一のcolzz純x0²をdomainで消し、残topweight≤1。weight1三次tensorfの両端収縮空間Qは、dim≤2ならdecomposable二次を含む（片端rank1又は両端2の支持A,Cを比較、A=Cならbinary determinant）。従ってdomainがrankM≥3、middle rank6が≤3を与え、rankM3/I2∩U²=Q3。
混合射影の片側核はuz+q又はzu+q、Nを作用してux0/x0uの関係となるためdomainで不可。両側同型からOregraph。N^d(Σs_i z^i)=d!s_d x0^dで冪独立、σ/δが実baseSへ降りC=S[z;σδ]、HS=(1−t)^−3。基礎AS3を仮定で追加しない：top四収縮の一つはpuref、他三つのmixed成分独立なのでS0=T(U)/QのW3dim1、S0_3dim10=実S3。σQ/δQは次数2/3で既にS0に零、Ore構成からS0=S。domainとHilbertEulerで線型1331複体完全、f両端非退化でKoszul AS3。noetherianはOre自由基底で降下。
H3正常FはNfixed、上の冪独立からF∈S3。B=C^Hも同じbase上のOre、normalizerH4はS固定/z→z+4x0。新一般lemma:cubic-derivation-Ore-vertexで排除した。導分付きOre B=S[z;σδ]、S noethKoszulAS3、G∈S3正規正則、θS=S,θz=λz+hならR=(S/G)[z;σbarδbar]。M=k[z]のExt_B集中3（S自由基底/AS3）、ReesでExt_R集中2、ASGor parameter1局所双対から全O(a)に対するP=πMのHom-acyclicityとHomdim1。基礎A=S/Gの最小解消をRへ誘導しExt^n(P,P)=β_n^A(k)。1/HA=(1−t)²/(1+t+t²)非多項式で無限高次Ext、H3に矛盾。z正常/未証明局所化を仮定しない。
公開verify_cubic_jordan211_ore_reduction.py/certificate default Sympy PASS（元32kernel/block/全収縮/自由語微分）。全rank-domain/AS3降下/局所双対は通常証明であり機械形式化としない。v292主原稿LuaLaTeX clean PASS。累計76validators across runs、単一76全再生未実行。新as4定理輸入なし、新規性未確認。

### 全単一固有値のCY性完成（v293）
単一固有値のH3包絡は必ずCY（μB=id）。最後の非自明単冪Jordan(2,2)も全排除した。通常証明cubic_jordan22_unipotent_vertex節thm:cubic-jordan22-unipotent-empty。元26反巡回N核、U=(x0,x2),V=(x1,x3)、V個数weightで最高2。純U²/V² sourceQは対称4×4、binary domain boundからrank≤1。Q0はrankH6とblockrank2rから純U²関係が3次元以上になり矛盾。従ってQ=qq^t≠0、q二次係数2×2可逆。Nを保つ同時GL2変換でq量子(0,1,−p,0),p非零又はJordan(1,1,−1,0)。mixed最高block5minor−p²(p−1)²(p+1)²、rankH6がmixed≤4を要求しp±1だけ残る。
可換・反可換・Jordan三chart全て元source principal6minor−1、最高逆順pairminor±1、U/V両AS2とVU→UVによりx0^i x2^j x1^k x3^lが張る。実AS4 Hilbertとの比較で全次数grC同定。最高三次商20dimの全N核は6dim/weight≤1、ゆえF Nfixedはweight≤1⇒J=(x0,x1,x2)のJ²。P=πk[x3]自己Ext1dim3、全低weight係数のままtwist後monodromy三型のdet1を検証。反可換ではdiag(−1,−1,1)で単冪でないが、odd-Serre determinant補題はdet1だけで排除する。全特殊値もunitpointpivotで保持。
公開verify_cubic_jordan22_unipotent_vertex.py/certificate default Sympy PASS、全26核/最高rank1/三chart/最高PBW/N三次行列と全6核/全point漸化式を保持。v293主原稿LuaLaTeX clean PASS。累計77validators across runs、単一77全再生未実行。通常の被覆/PBW/tails/Serre証明を機械形式化したとはしない、新規性未確認。新as4外部定理輸入なし。
全体の次の核心は全CY包絡の中央三次切断。三・四固有値全排除、単一固有値非CY全排除、既分類二固有値全Jordan領域を保持し、未処理Jordanへ戻らない。全intrinsic群oid・成分・相対降下も未完成であり、全H3完成と呼ばない。

### 全CY必要被覆の第二二次関係入力を局所全枝で検証（v294）
as4固定SHA6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0のNONDEGENERATE_CHARTとDEGENERATE_CHART_SECOND_QUADRICを必要範囲だけ輸入した。仮定：標数0代数閉体、P3上独立六二次式、rank6二次関係、像次元3。結論：独立な第二二次関係。接空間rank3/2の全Witt正規化、退化DC1–DC15の全整除枝と恒等特異/巡回pencil、非退化の一般対称Mの第二関係を本文へ通常証明付きで統合した。独立checkerでsyzygy rank10/parameter8、両非整除8線型条件、unit標的変換、二quadric、一般pencil行列式、恒等特異枝のrank3関係、一般16係数Tの外積、companion独立証拠−1、一般対称Mと交代部分除去をdefault Sympy exact検証PASS。主原稿v294 LuaLaTeX clean PASS（bibliography長名はallowbreakで修正済み）。累計78validators across runs、単一78全再生未実行。
証明cubic_CY_second_quadric節、verify_cubic_CY_second_quadric.py/certificate。as4_imports.jsonに固定SHA/全entrypointと証明hash/仮定/元audit pending/今回独立計算範囲を登録。全CY_COMPLETE、CI22全chart、AS十分性、全同型、Veronese除外の独立監査までは輸入していない。

### 零交換子CYの全像をCI(2,2)へ必要被覆（v295）
固定as4のVeronese排除を必要範囲で輸入し、全元データを当repoで独立再生した。Veronese21積rank15、対称係数rank1/2/3→関係rank3/4/6、全CY混合25核/全57係数cyclicrank31/KKrank20、同変等長Φとsl2二作用、全六最大等方planeと10三次係数のintegrable kernel、全三次正規化、零三次自由積lower25、全八非零代表の線型解/残余ideal、前四実平方/次二unitideal、最後二の全Ga3orbit（Jac8/27,−72）/両符号をdefault Sympy exactで確認。二representativeの元Hilbertは独立GradedAlgebraでalpha(1,4,10,22)、beta(1,4,10,20,37)、全候補非AS4。上流fullverifier isolated replay（flint）と当repo独立再生を区別。最小固定proof input19KBと新certificate/validatorを保存し、as4_importsにsourcecommit/hash/仮定/元audit pending/独立範囲を登録した。
通常証明cubic_CY_Veronese節prop:cubic-CY-Veronese-excluded,thm:cubic-CY-zero-commutator-CI22。CYc0は関係graphからSSrank6、その全対称化零が非退化Q関係。像次元r≤2ならrankr点の線型切断P^rを選び、Urestriction6dimからr2/fullVeronese像。rank1 symmetric3matrixを原始vector平方へ戻し、gcd/付値/次数から元U=Sym²Wを復元して上の排除に反する。従って像3dim。v294第二quadとrank6quadconeのfactoriality（z0prime,localLaurentpoly,素因子降下）から高さ1imageideal生成次数2、整CI22となる。全CI22上の包絡・切断分類やAS十分性ではない。
公開verify_cubic_CY_Veronese.py/input/certificate default Sympy PASS、v295主原稿LuaLaTeX clean PASS。累計79validators across runs、単一79全再生未実行。全CY分類・全CI22代数chart・幾何証明の機械形式化・新規性は未確認。

### 零交換子CYの七必要対称射影型を全被覆（v296）
通常証明cubic_CY_CI22_projection_atlas節thm:cubic-CY-CI22-seven-projections、固定as4のQUADRIC_PENCIL_PROJECTIONSから必要幾何被覆だけ輸入。CI22二次鉛筆Q/P、T=A^-1Hの接形式退化条件q^tAT²q0から常時退化iffT²∈span(I,T)。最小多項式2で二根ならrank1/2関係不可から3+3直和二Veronese=D、重根なら自己共役N²0rank3でrank3関係a²,ab,b²と全syzygy(−bℓ,aℓ−bm,am)、ℓ,m mod<a,b>独立からL。非退化point側は一般対称M表示でbaseZ≅smoothconic(B=0)のr-cut長さ4、全三base-elimination恒等式を確認。超平面に含まれないことから線型全section埋込み、U=I_Z2、curvilinear長さ4の全分割1111/211/22/31/4で五型。これらは中山Jordan型ではなく対称射影基点scheme型である。
公開verify_cubic_CY_CI22_projection_atlas.py/certificate default Sympy PASS：全七Uの21積rank19/二relation全kernel、全pencil determinant/T²criterion、五有限algebra乗算全kernel、binary quadratic syzygy rank22/nullity8、Lmarked関係全shear、一般M三basepoint恒等式、五symmetricM例のconic四次根型。v296主原稿LuaLaTeX clean PASS。累計80validators across runs、単一80全再生未実行。as4_importsに固定sourcehash/全仮定/被覆だけのscopeを登録。全AS4係数normalform・切断・群oidは同時輸入しない、新規性未確認。

### 全零交換子CYのD/L二射影をH3から全排除（v297）
必要係数全被覆を既存二族排除へ接続した。通常証明cubic_CY_DL_cover節thm:cubic-CY-DL-cover-empty。Dはrank6markedAを二Veronese判別式へ正規化、全mixed22/γ0/二binary discriminant−1/4、SL2×SL2で内部標準形、rank8線型系が八係数zero、残六binomialを全再生。domainが四係数pair非零を強制し、非零support二枝I/IIだけ。根R²=U/p又はR⁴=1/(p³r)のみの対角変更で(1,h,1,−h)全h非零へ。RS=TUも根idealで確認しmarkedA保持。元16語関係が既存D_I/II(h)と非零定数basis変換で全h一致し、thm:as4-double-cover-h3-exclusionで全排除。AS4存在十分性/全同型は輸入しない。
Lは全mixed22とSchurdiscriminant2(v1²−4v0v2)、一般四係数GL2でv変換Sym²T/det²を全tensorframeで確認、v0/平方v(1,0,0)の全二枝へ。v0はfree二元quotient、平方枝は全linear条件と四polynomiale_iの二恒等式から特殊zを除外せずu=w=p0、実a²sourcecolumnでdomain矛盾。全zero/非zero各場合の全値排除。
公開verify_cubic_CY_DL_cover.py/certificate default Sympy PASS（双方22核/混合cyclicrank14/全57係数rank34、D全normalization/全値旧表示移送、L全GL2・全分岐）。v297主原稿LuaLaTeX clean PASS。as4_importsは固定6f798...のDCC4–12/LBE2–10の必要範囲のみ登録。累計81validators across runs、単一81全再生未実行、新規性未確認。
残るCYc0の必要射影は有限基点五型1111/211/22/31/4。次は4と31の全必要係数被覆を、既存thm:as4-curvilinear4-h3-exclusion（CF2/CF3/CT2の中心3zero）へ接続する。固定sourceCURVILINEAR_FOUR_COMPLETEの必要CF6–13、CURVILINEAR_THREE_ONE_COMPLETEの必要CT3–17を全文読んだ（AS十分性と全Autは不要）。CFは全mixed21、全Ga4/トーラスnormalization、四emptybranches、五先頭tupleCF13、うち二empty/一Hilbert4dim37/二fixed CF2CF3。CTはx0/x10非零empty、x9非零全有限/一parameterHilbert4>35、x9=0二cube恒等式でx11=x15zero、x12非零二族のgenericHilbert4dim37又はdegree5dim62（必要56）で全特殊値排除、最後x17unit枝CT14六式からx1nonzeroが唯一CT2、x1zero三族allclosedHilbert4≥39/39/42。全family原関係の分母は記載unitだけで、genericrank上界により全閉値でdim下界を用いるので、generic商基底の無条件特殊化とは別。
次は固定source二verifierの必要controlを孤立workspaceでreplay（referenceを変更しない）し、最小proofdataと当repo独立raw quotientでbad代表/familiesをfresh確認する。正常CF2/CF3/CT2自体の中心排除は既に済みで再計算不要。全候補必要被覆のmetadata/通常証明を追加する。射影22/211/1111のAS4係数全被覆、全CY切断・群oid・成分・相対降下は未完成。

### 有限基点型4・31の全必要係数被覆とH3排除（v298）
通常証明cubic_CY_finite43_cover節thm:cubic-CY-finite43-empty。固定as4のCF6–13/CT3–17だけを必要被覆として利用し、全上流controlを隔離workspaceで再実行PASS。当repoの独立default exact controlもPASS：二つの全21混合frame、六空chart、CF先頭五tuple、全14非正則代表・族の元商次元、既存CF2/CF3/CT2への定数可逆な関係移送。非正則族の全閉値下界は、明記したunitだけを反転した元全語関係行列のrank特殊化で正当化する。CTのmu=-1例外は自由yも保持、x12境界は五次62>56を用いる。CF先頭消去式はv²(2v+1)(7v+1)であり、五tupleの幾何学的被覆を被約scheme/相対被覆と主張しない。
公開verify_cubic_CY_finite43_cover.py/input/certificate、主原稿LuaLaTeX clean PASS。固定source/hash/必要範囲をas4_importsへ登録。累計82validators across runs、単一82全再生未実行。上流通常証明の全gauge被覆と当repo独立商計算を区別し、AS十分性/全Aut/新規性を同時輸入しない。
残るCYc0必要射影は1111/211/22。次は固定CURVILINEAR_TWO_TWO_COMPLETEのTT1–14必要被覆を既存A/B/D/C_r/E_t/F_hの全値排除へ接続する。本文の必要枝は読了：全21frame、kappa非零二bad族(dim4=38/40)、kappa零mixed非零三bad族(dim4=39/42,dim3=21)、最終r=±1/4族(dim3=24)、実平方枝、六正則表示への全正規化。TT15以降のAS十分性/全Autは不要。次は固定verifierを隔離再実行し、最小データから全bad族の元商と六表示移送を独立確認する。全CY中央切断、全群oid・成分・相対降下は未完成。

### 有限基点型22の全H3排除（v299）
通常証明cubic_CY_finite22_cover節thm:cubic-CY-finite22-empty。固定as4のTT1–14必要全係数被覆だけを利用。固定全controllerの隔離再実行PASS、当repo default独立controlもPASS：全21mixed/cyclicrank15、N/T/W印付き共変性、九つの非正則代表・族の元商(dim4=38/40/39/42、dim3=21/24)、六表示のliteral移送とA両符号。全自由係数閉値は元関係行列rank特殊化と明示unitだけの分母で保持。残るA/B/D/C_r/E_t/F_hは既存三排除定理で全H3なし。公開verify_cubic_CY_finite22_cover.py/input/certificate、主原稿LuaLaTeX clean PASS。累計83validators across runs、単一83全再生未実行。AS十分性/全Aut/被約相対被覆/新規性は輸入しない。
CYc0残る必要射影は1111/211。次は211の三不変層x0非零、x0零x15非零、双方零の必要被覆。固定DOUBLE_SIMPLE_NONZERO_COMPLETEのDS1–10、SECOND_COMPLETEのDT4–11、FINAL_EXCLUSIONの全DZ1–20を読み終えた。前二層の残存全表示L±/T/P/U/V/A_lr/B_rは既存ds211節で全パラメータ排除済みなので再計算不要。最終零層では元Hilbert5=57の二族、四次36の四代数点、Hilbert7=123>120のM0/M1族、その他degree3/4/5障害を含めて必要被覆を確認する必要がある。現在三固定controllerを隔離逐次replay中。次は最小proofdataと当repo独立元商検証で接続する。全H3分類・CYc>=1・群oid・成分・相対降下は未完成。

### 有限基点型211の全必要被覆とH3排除（v300）
通常証明cubic_CY_finite211_cover節thm:cubic-CY-finite211-empty。固定as4のDS1–10/DT4–11/DZ1–20必要範囲を輸入し、三全controllerを参照checkoutを書き換えず隔離出力先で逐次replayし全PASS。当repoの独立元商controlも全27代表・族PASS（python-flint使用、default Sympy全実行PASSとは主張しない）。全21mixed/cyclicrank15、全N/T/W印付き群、D00=4x0x15、全非正則族の元商と全分母unitを確認。新しい疎pivot/右乗算だけの再帰商では各段階で全元関係挿入の座標像零も確認。最終零層22候補はHilbert5=57/60、四次36/39/42、三次21/22/23、二つのM族のHilbert7=123>120。係数共役も保持し、全閉値は元全語rank特殊化で下界保証。第二層5族も三次21/22。残る第一層全7表示と第二層二族は既存ds211の全パラメータ排除の元関係と一致。AS十分性/全Aut/相対scheme被覆は輸入しない。
公開verify_cubic_CY_finite211_cover.py/input/certificate、主原稿LuaLaTeX clean PASS。再現はPYTHONPATH=/workspace/work/python-deps SYMPY_GROUND_TYPES=flint python computations/verify_cubic_CY_finite211_cover.py --flint。累計84validators across runs、単一84全再生未実行、新規性未確認。
残るCYc0必要射影型は1111のみ。FZ2量子型Qもq_ij!=1のCY skewなので、既存lem:cubic-cy-skew-zero-commutatorにより全H3排除済み。全skew領域一般のH3とこの必要射影型のQを区別する。既存four_simple節のS/Q/O/H/L/M/F/G/K/J/R/N/C/adjacentL/S/T/fullPの表示別認識・全値排除を再計算せず、必要被覆を接続する。固定CI22_COMPLETEの支持被覆全文、FIRST_SHAREDの必要FN1–6、SHARED_ZEROの必要FZ1–10、INACTIVE_SHARED_VERTEX_EXCLUDED、SINGULAR_RANK_ONE_EXCLUDED、SINGULAR_RANK_TWO_EXCLUDEDの全文、FULL_SHARED_INVERTIBLE_REDUCTIONの必要FT1–12を読んだ（全AS十分性/Autは不要）。通常証明と各controlの局所化をこれから監査する。
独立な私的支持走査では4096有向支持は218 S4軌道、zero/degree1/degree2/partial_active/fullの支持数1/3471/609/14/1、軌道数1/173/40/3/1。全置換とdegree1/2標準chartの存在も公的元frameと合わせて検証・統合するのが次の小補題。部分活性三軌道・全共有可逆/特異枝を無条件に飛ばさない。CYc>=1中央切断、全群oid・成分・相対降下は未完成。

### 四単純基点の全元frame・支持被覆と共有零層の全排除（v301）
通常証明cubic_CY_four_point_support節lem:cubic-CY-four-point-support/thm:cubic-CY-four-point-shared-zero-empty。元FS21混合方向/一KK方向の全CYframeを独立証明：混合rank15、KKrank20、joint57rank35。全24置換の印付きlambda変換・B全21係数・gアフィン変換・共有辺単元、対角d_i/d_jを元行列で全検証。全4096支持/218軌道をzero/degree1/degree2/partial-active/fullへ支持数1/3471/609/14/1、軌道数1/173/40/3/1と被覆し、degree1/2標準chartへの全置換存在を検証。
共有零の全Schur対角六条件/残余三式/相補積恒等式を独立に再生した。ABC零は全非零S又はH0/H1、ABC非零は全相補積零からQ又はOへ全被覆。全torus規格化は独立三整数重みと代数閉性だけ。Oの四禁止A値には元係数1の実積関係がある。Qは全六対の二項式係数和1、Thetaと六係数積の比が単元、F=0下の全四CY行積を確認。従って全q_ij!=1であり、既存lem:cubic-cy-skew-zero-commutatorから中心三次は高々一本の純三乗。S/Q/O/H全て既存全値排除に接続し、共有零層全H3なし。
v300の再開文に「Qにはskew H3が残り得る」とした記述を訂正した。全skew領域一般のH3と、全q_ij!=1が必要なこの射影型を混同していた。該当現行notes全てを訂正し、量子型を未解決へ戻さない。
公開verify_cubic_CY_four_point_support.py/shared_zero.pyと小certificateはdefault Sympy exact全PASS。主原稿LuaLaTeX clean PASS。累計86validators across runs、単一86全再生未実行。固定as4 FS1–2/FZ1–10の式だけを出典化し、必要被覆そのものは元行列と通常の全場合分けで当repoに証明。新規性/AS十分性/全Aut/相対被覆は主張しない。
次は非零共有支持の必要係数chartを接続する。degree1のx0zero最初の共有chartは固定FIRST_SHAREDのFN1–6を読了、八bad境界は元三次dim21/22、残るL/M/F/G/Kは既存全値排除。固定fullcontrollerを隔離as4-fs-auditでreplay中（v302ログ）。次は最小必要proofdataから八bad元商と既存表示移送を独立確認する。degree1のx0nonnull、degree2、部分活性三軌道、全共有可逆/特異層はまだ必要被覆を統合していない。CYc>=1中央切断・全群oid・成分・相対降下も未完成。

### 最初の非零共有chartの全H3排除（v302）
通常証明cubic_CY_four_point_first_cover節thm:cubic-CY-four-point-first-empty。x1!=0,x0=x3=x4zeroと全monomial軌道を全排除。固定FIRST_SHAREDの必要FN1–6と全controller隔離replayPASSを使用し、当repoでも全21係数の四枝(x2,x5)=00/01/10/11の全消去式を元Schur行列から一手ずつ独立再生した。各式が実際の残余式であること、一次pivotがlambda/lambda+1だけの単元であること、代入式・最終残余の一致を確認。四主飽和idealも再計算。八bad境界の元三次商21/22、全元関係挿入の座標零・分母unitから全閉値障害を確認。残余全係数FN2の四制約idealへの逆代入と、既存fn_matrixのliteral一致を検証。通常の全対角規格化でL/M/F/G/Kに全被覆し既存全値排除を適用。
公開verify_cubic_CY_four_point_first_cover.py/input/certificate exact PASS（python-flint ground使用）、主原稿LuaLaTeX clean PASS。累計87validators across runs、単一87全再生未実行。v300の疎Hilbert classを共通cubic_sparse_hilbert.pyへAST同一のまま移し、class AST一致と旧211 transport-only controlを実行PASS。全211をもう一度走査したという意味ではない。AS十分性/全Aut/相対scheme被覆/新規性は主張しない。
次は出次数1のx0nonnullで行列式x0x2-x1²nonnullの二openchart。固定SECOND_SHARED_OPENのFO1–5とZERO_FIFTH_OPENの必要FZ1–6を読了。前者は全lambda/lambda+1/p-1だけの消去からq=x10nonnull空、qzero唯一H(lambda,p)へ。後者はqzeroでlambda1のM0/M1、p0は既完成firstchartへ直接移せるのでH3排除、pqnonnullは二factor枝で(lambda,p)=(1/2,-2),(2,-2)、四共役候補は既存Nへ。既存H/M/N中心排除は全値完成済みで再計算不要。二固定fullcontrollerを隔離逐次replay中(v303ログ)。次は必要trace/GB/normalcoefのみ抽出し当repoで元消去と移送を独立再生する。残る行列式零のgeneral/zero-fifth境界、出次数2、部分活性三軌道、全共有可逆/特異の必要被覆も未統合。CYc>=1/群oid/成分/相対降下は未完成。

### 出次数1の二つの行列式非零chartの全排除（v303）
通常証明cubic_CY_four_point_two_open節thm:cubic-CY-four-point-two-open-empty。x0*x1!=0,x3=x4zero,x0*x2-x1²!=0をx5zero/nonnull双方で全H3排除。固定必要FO1–5/zero-fifth-open FZ1–6と二全controller隔離replayPASSを使用。当repo default独立exact controlもPASS：全元21係数消去を式・単元pivot毎に再生、FO q(u-v),q(pu-v)の局所ideal所属とqnonzero空ideal、qzero全係数H(lambda,p)を確認。FZ qzeroはlambda-1の単元倍からlambda1/全M(p,r)係数、pzeroは元全matrixで既完成firstchartへ移送。pqnonnullは二factor枝それぞれの飽和idealを三必要有限条件と完全比較。残りx6/x7/x9は数体idealに各正冪が入り幾何学的に全zero。全四共役候補は具体P/対角/可逆関係基底で既存Nへliteral移送。既存H/M/N排除へ接続しAS十分性/全Autを輸入しない。
公開verify_cubic_CY_four_point_two_open.py/input/certificate default exact PASS、主原稿LuaLaTeX clean PASS。累計88validators across runs、単一88全再生未実行。有限残余idealの被約性・相対scheme被覆・新規性は未主張。
次は出次数1の残る行列式零二境界。固定GENERAL_BOUNDARY必要FG1–5、IMAGINARY_BOUNDARY必要FI1–4/h0五次58障害、ZERO_FIFTH_BOUNDARY必要FB1–9を全文読了（AS十分性/全Aut不要）。前者は全lambdaからR_eta(lambda)又はlambda=±iのJ_eta(h)、h0二点はHilbert5=58>56。後者はx17nonnull空、二factorA/B、七必要係数行と八種特殊結合係数境界を漏れなく扱い、genericbad四次37、lambda^4+1全根五次59、lambda²+1全根五次58、残るN/C/R±1は既存全値排除済み。三固定fullcontrollersを隔離逐次replay中(v304ログ)。次は必要入力抽出と独立元商/例外全数体/表示移送を作る。境界の一般点だけで済ませない。出次数2、部分活性三軌道、全共有可逆/特異の必要被覆、CYc>=1、群oid・成分・降下は未完成。

### 第五係数非零・行列式零境界の全H3排除（v304）
通常証明cubic_CY_four_point_determinant節thm:cubic-CY-four-point-determinant-empty。x0*x1*x5!=0,x3=x4zero,x0*x2-x1²zeroと全monomial軌道を全排除した。固定GENERAL_BOUNDARY必要FG1–5を使用し、一般境界/純虚境界の上流全controller隔離replayは双方PASS。当repo default exact controlもPASS：全21係数の二段階消去を元残余式・lambda/lambda+1単元pivot毎に再生、16(x15-x16)²+1とx9(16x9-lambda²+1)の全split、QQ(i)上の全二飽和idealと明示targetidealの一致。全R_eta(lambda)とlambda1重複は既存r_matrixにliteral一致。形式lambda固定の符号共役とlambda±iの全四fiberは、hを割らず可逆原関係基底で既存J_eta(±h/±ih)へliteral移送。既存prop:cubic-boundary-Jがh0のHilbert5=58も排除済みなので、同じ固定点のHilbertを新規に再計算したとはせず再利用。AS十分性/全Aut/相対scheme分類は輸入しない。
公開verify_cubic_CY_four_point_determinant.py/input/certificate default exact PASS、主原稿LuaLaTeX clean PASS。累計89validators across runs、単一89全再生未実行、新規性未確認。
次の核心は第五係数零・行列式零の最後のdegree1境界。固定ZERO_FIFTH_BOUNDARY必要FB1–9は全文読了、上流fullcontrollerも隔離replayPASS。x17nonnull空、x17zeroの二因子分岐、FB3/4所属と三generic/三例外baseideal一致、全七基本行±符号、FB7/8の全結合rank低下を扱う。badは16記録：genericAm/Apの四次37、Az/B三次21、Apのlambda^4+1全四根五次59とlambda²+1全二根五次58、Az(-1/2)/B(-2)特殊coupling三次21、全±符号。原係数分母だけを管理して全閉値下界を使う。残るA1(r)はr0で旧C/共役、rnonnullで旧R±1、Ah/Bh四点は旧Nに移るので既存中心排除を再利用できる。
次は最小必要trace/linear matrix/元badnormalだけを抽出し、元Schur消去・基本ideal比較・全coupling例外・独立元商/全数体・旧表示移送を作る。完了すれば全degree1支持3471個/173軌道がH3なしとなるが、まだその結論を先取りしない。degree2の609支持/40軌道、部分活性14支持/3軌道、全共有1支持/1軌道、CYc>=1、全群oid・成分・相対降下は未完成。

### 全出次数1共有支持の排除と停止時の再開点（v305）
通常証明cubic_CY_four_point_zero_determinant節thm:cubic-CY-four-point-zero-determinant-empty/cor:cubic-CY-four-point-degree-one-empty。最後のx5zero行列式境界を全H3排除し、全degree1支持3471個/173 S4支持軌道のH3なしが完成した。共有零支持も排除済みなので、全CYc0の残る必要支持は624個/44軌道：degree2が609/40、部分活性14/3、全共有1/1。これを存在するmoduli成分数・intrinsic同型類数と呼ばない。全H3分類は未完成。
固定FB1–9と上流fullcontroller隔離replayPASSを使用し、当repo exact controlも全PASS（python-flint ground使用）。元21係数からのx17nonnull単元矛盾/zero枝全消去、二split所属、七基本係数行の全局所ideal比較、両符号の全coupling行列・genericと例外rank/kernel/x9一意性、全16bad元商・全元関係挿入の座標零を確認した。genericAm/Ap四次37、Az/B三次21、lambda^4+1全四根五次59、lambda²+1全二根五次58、残る二有理特殊値三次21。全数体は既約性/minpolyと元係数評価で全共役を保持。元分母のunit管理とraw rank特殊化で全閉値下界を保証。全kernelのtorus規格化、旧C/係数共役、両R1への元移送、全四N点への可逆原関係基底移送を確認。旧C/R/Nの中心排除を新規に再計算したとはしない。
公開verify_cubic_CY_four_point_zero_determinant.py/input/certificate。累計90validators across runs、単一90全再生未実行。AS十分性/全Aut/相対schemeの被約性・降下・新規性は輸入しない。主原稿LuaLaTeX clean PASS（446頁）。
ユーザーの「切りの良いところで止まって下さい」に従い、この全degree1排除を停止checkpointとする。次の計算・上流controllerは起動しない。再開時は00_research_plan.mdとAGENTS.mdを読み、現在のmainから始める。次の数学的frontierはdegree2の全必要係数被覆（adjacent sharedのx0zero/x5zero/corner、開部分排除、全境界候補T/L/Sを既存全値排除へ接続）、次に部分活性三軌道と全共有可逆/特異支持。これらの必要証明の全面再監査・独立計算は未完了であり、まだ全CYc0空とは主張しない。CYc>=1中央切断、全群oid・成分・相対降下も未完成。
### 出次数2の共有支持（v306）
固定as4のAZ・AF・AV・AO・ABの必要被覆と既存L/J/S/T排除を接続し、出次数2の頂点を許す四単純基点型を排除した。本文は cubic_CY_four_point_degree_two 節。AO2両符号の元三次商は独立計算で次元21、分母は許容単元のみなので全閉値にも下界21が成立する。残る零交換子CYの必要支持は部分活性14支持・3軌道、全共有1支持・1軌道。次に部分活性の必要排除と全共有の可逆・特異主ブロック被覆を接続する。
### 部分活性支持から全共有支持への還元（v307）
固定as4のIV1–IV13を必要条件として接続し、零交換子CYのH3では四単純基点で十二共有係数全非零が必要となった。部分活性排除の証明依存先はas4_imports.jsonに固定した。次に全共有の可逆主ブロックFT1–FT12を既存P全排除へ接続し、全主ブロック特異の場合の階数1・2を監査する。
全共有支持についても、固定FT1–FT12から既存P全値排除へ接続し、全主ブロック特異の階数1・2は固定as4の必要排除を適用した。これで零交換子CYを全排除する。既存 cor:h3-cy-commutator-reduction と合わせると、非可換CY包絡で残る交換子次元は1,2,3であり、三交換子beta型は既排除。次はそれらの中心三次切断を判定する。上流全証明の独立再実装はしていない。

### 二交換子・非共有Segreの中心三次（再開用）
固定as4 CY_TWO_COMMUTATORS_DISJOINT_SEGRE.texの必要表示は Q_q, N_1, N_2。孤立型の元関係を直接読むと a,c は正常で、ac の正常化作用は -I 又は -I に b→b+8a の単冪shearを合成したもの。従って既存 lem:normalizer-minus-unipotent-odd-centre で両型はH3から消える。Q_q の中心単項式条件は q^(i-j)=q^(k-l)=1。総次数3では少なくとも一方の差が奇数なので、q≠1 なら原始三乗根かつ純三乗に限る。この場合の許容切断は既存skew分類との係数対応を確認する。ここではQ全排除を主張しない。二交換子の残る必要射影二型は固定CY_TWO_COMMUTATORS_VERONESE_MIXED_RANKONE/RANKTWOの表示を確認する。

非共有SegreのQ_qの純三乗例外は、順序(a,b,c,d)で交換指数(0,1,2,2,1,0)に一致し、既存 prop:third-six-rank-obstruction で全排除。混合階数一VM1では個数濾過の先頭と正常元aの平行移動から中心はk[a,b,z]（z=ac+bd）に含まれる。[c,z]=-bz,[d,z]=azから中心三次はkab²のみで、整域切断はない。本文 cubic_CY_two_commutators_Segre 節。次の混合階数二VRでもaは正常、同じ濾過の先頭核を与える線型形式は t ac+β bd。中心三次と孤立型Iの判定は未完了。

### 二交換子の残る孤立型
非共有Segre、混合階数一Veronese、混合階数二の全VRパラメータ族を排除した。本文 cubic_CY_two_commutators_Segre 節。特にVRでは正常元aの平行移動の先頭核から中心元をk[a,b,tac+βbd]に絞り、cとの交換で中心三次が零となる。次は固定VTの孤立型Iについて元六関係から中心三次を判定し、二交換子の七対称射影の必要全被覆を監査する。
二交換子の孤立型Iも元VT行列から中心三次rank20（有理小行列式 -32768/22876792454961）で排除した。固定as4の cor:cy-two-commutators-complete の必要方向と合わせて全二交換子CY排除。残る非可換CY包絡の交換子次元は1又は3（3のbeta型は既排除）。次は一交換子の十六必要射影と三交換子の残る層で中央切断を判定する。

### 一交換子の平方追加Segreを全排除（v309）
十六必要射影のうち非共有Segre＋平方の全被覆だけを固定as4から使用した。13表示の全中心三次を独立検算し、残る内部二族の原始三乗根値を全排除した。S_{a+b}は二元三次の積分解、S_aはaで局所化した量子Weyl表示の中央式からZ=(Xの二次多項式)/(v³+(B/D)X)を得て、分子・分母を三次巡回ノルムと認識する。従って整域切断が存在しない。証明はcubic_CY_one_segre_square節。次は同じ商射影・既約因数特殊化を流用し、並行して非共有二直線型の交換規則から中心を構造的に絞る。

### 中心・ノルム障害による一括削減（v310）
一交換子・非共有Segreの二直線追加型は既分類skewだけに帰着し、二平方追加型の外側交換子九表示は全排除した。固定必要表示23個で商射影の全例外数体を再計算。残った内部型H_sの原始三乗根では、交差項abがあると中心三次は二元で可約。f=a²+b²でもa-局所化の三次シンボルはk(v)上の滑らかな有理二次曲線上で全剰余零、FaddeevとTsenにより分裂する。論文cubic_CY_one_segre_extensions節。既存skewの合同を再分類に含める必要はない。
三交換子混合の外積階数一（七係数全域）はcubic_CY_three_mixed_rank_one節で排除。dの個数濾過で[d^n,a]の先頭は2n(bc+μa²)d^(n−1)で、中心は基礎三元環に含まれる。その中心三次a³,ab²,ac²は共通一次因子aを持つ。
次は一交換子二平方の交差有限・無限遠チャートと、三交換子外積階数二の共有した濾過条件。前者の有限2変数では、疎な商射影と中心小行列式の開被覆を試し、残余点だけ原関係へ帰る。中心零・共通因子・巡回分裂を先に調べ、包絡側の全自己同型の再分類を避ける。

### 一交換子の二平方と三交換子の構造的削減（v311）
一交換子・二平方追加Segreを全排除した。交差チャートの元トップから定数minorで六関係を復元し、固定as4の有限(p,t)・無限遠(e)とのliteral一致を確認。中心20次minorと次数別商射影の全因子から、有限残余は p=0,-2,-2/(t+1),-2/(2t+1),2/(t-1) の五曲線。各曲線の元関係から再計算すると例外は許容域外だけで、中心三次は全域零。無限遠はe=0を別QQ計算し全域零。通例のAS4次元20,35だけを特殊化に使った。
三交換子外積階数二は三係数層を一括排除。固定as4の反射型融合積の交代語基底を使い、次数三の奇数語と長さ二語は基礎a,bへの作用が非恒等なので中心に現れない。残る基礎の重み二変数Zの係数も二対合の一次固定空間の交わりが零。従って中心三次は可換二元で全て可約。外積階数三の列係数階数二は対称関係Cliffordへの二次ねじりで、任意の中心三次が中央二次{a,d}を反転して矛盾。alpha零先頭式二表示はa=1の中心の濾過次数が2以下なので共通因子aで排除した。
現時点の主要残余は、一交換子の非共有Segreの平方・二直線を両ブロックに加えた二型、共有Segreの十一型、および三交換子のalpha非零先頭式と外積階数三・列係数階数三。必要被覆および切断条件は別々に記録。次の具体的な一手はalphaのa=0におけるAS3中心三次を全先頭型で調べて中央三次のliftを絞る。同時に他のSegre候補は元関係から中心零・可約・twistの中心障害を先に見る。全H3分類・成分・相対降下は未完了。

### 三交換子alphaの重複直線と共点三直線の削減（v312）
固定as4の三重直線四表示で、中央三次切断がd軸の点イデアルの二乗に入ることを、S=B/(a)のWeyl中心と明示中央liftから証明した。二重直線b²cでは、七つの低次係数を保って中央三次liftを計算した。SのOre導分による中心はk[b²c]。重複直線上でaの係数の二次式が消える点の二チャートでは、いずれも全tails自己拡大の漸化式が行列式1でExt1が三次元となり、強いH3のSerre traceに反する。共点三直線では下位二次式が共点で零であればaを法としたOre中心とa²までの交換子で切断が点イデアル二乗に入る。同じSerre障害が固定五族のうち四族を排除する。
本文cubic_CY_three_alpha_nonsmooth節、公開再現器verify_cubic_CY_three_alpha_repeated_lines.py。三重直線四表示と二重直線の全係数・両チャートは厳密PASS。共点三直線の残る第一族、滑らか・節点・尖点・三角形・割線二次曲線・接線二次曲線、三交換子列階数三は要判定。一交換子の残る射影は中心三次を先に調べる。全成分・相対降下・全H3分類は未完成。

### 一交換子の共有Segre十一射影を全排除（v314）
対称階数5の必要排除と標識付き階数4の十六候補を固定as4から使用した。共有十一射影のうち固定空二射影以外を、元の六関係から中心三次を独立計算して判定。ad,bdは全域中心零。b²とb²+c²では中心三次はa²cとa²bの各一元。ad+b²とad+b²+c²ではt=-1/3でのみ中心三次kac²。bd+c²ではh=-1/4でのみ中心三次kb(b+3a/8)²（lambda=1/64も同じ）。いずれも整域切断なし。残るd²+b²,d²+b²+c²では、交換子比の零・非零、下位係数zの零・非零、非対角ellの四共鳴とその補集合、対角係数両符号を合わせた全40域で、商射影の分母と中心小行列式の全因子は許容単元のみ。全中心三次が零である。
本文cubic_CY_one_segre_shared節。公開verify_cubic_CY_one_segre_shared.pyとverify_cubic_CY_one_segre_shared_squares.py、対応JSON。全一交換子の未判定非skewは非共有Segreのa²+cdとab+cd。次に固定S4_12の24族・一孤立類を、全例外因子まで元関係の共通計算で判定する。固定as4の全排除の独立再実装や全統合replayは未実行。全H3分類・成分・相対降下は未完成。

### 一交換子の非共有平方・積追加の削減とZ切断の完全判定（v315）
横断外側七表示、等方外側八表示、非等方外側四族、上行交差Cθを判定。公開verify_cubic_CY_one_segre_square_split.pyは19計算とBn2の四例外直線の全既約因子を元の六関係から再検算。C(s,z≠0),L(s,h)はc,dの逆作用を同時対角化し、固有値q1,q2の相異性、1でないこと、積が1でないことから全中心三次を可換二元に限定。唯一残るZのs²=−1/12ではqが原始三乗根、中心三次はP(a,b)+Cc³+Dd³。二つの純三乗係数のどちらかが零、またはdeg P(1,z)≤1なら固定点の奇数Ext障害。
Zでの正確な条件はCD≠0、deg P(1,z)=m∈{2,3}、判別式Δ=P(1,z)^2−4CDν³が平方自由。ねじった量子Weyl表示でg=Cx²+P(1,z)x+Dν³の付値剰余曲線は種数m−1、xの二無限遠位数は±mなので立方でない（m=3では次数1写像の矛盾）。巡回ノルムの付値から斜体。c,dチャートの自由巡回軌道で完備環は冠積、Δ重根ならその一つの単純の射影次元無限。a≠0でX=Y=0は二単元辺で行列環。m=2のb軸では中心aを陰関数消去し、完備量子平面への降下濾過で左右kの長さ二解消を得る。従って全H3公理を満たす。例P=b³,C=D=1。包絡の全幾何矢を元の標識と関係から決定し、C=D=1規格化のAff₁×μ₆作用、一般慣性μ₃、次元2。二原始三乗根の包絡はc,d交換で同型。本文cubic_CY_one_segre_square_split節。これは全成分性や相対降下の主張を含まない。
平方・積追加の残りは等方外側b5と下行交差L^±_{w,e}, Z_{s,h}, M_{s,w,z}。b5は一般で中心零、例外h²+1/16,h²+1/48および三曲線での厳密再計算を終える。下行片成分の両符号で一般rank20の観察はあるが、全例外は未判定。二積追加ab+cd、三交換子alpha残余と列階数三、全成分・相対降下も未完成。
