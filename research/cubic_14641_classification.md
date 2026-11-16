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
