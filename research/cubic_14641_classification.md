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
