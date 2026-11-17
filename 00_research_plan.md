# 研究方針：H3型内在的非可換三次曲面の完全分類

2026-11-17 / research-plan-v35 / H3分類専用。
**再開時は本書を最初に読む。GitHub mainが唯一の正本。**
実行規則は `AGENTS.md`。既存の全H3分類の詳細と必要な式は
`research/cubic_14641_classification.md`、`research/cubic_14641_codex_plan.md`、
`research/cubic_classification_validation.json` に保持する。
本書は現在の優先順位と文書の入口を整理し、証明・計算の重複を置かない。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。
目標と方針は柔軟に変更し、重要な変更の理由、元の目標の達成部分と残存部分を現在有効な方針として書き直す。

証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定、既知入力、証明の所在、未解決箇所を明記する。
原稿に証明があること、今回の点検、計算の実行、独立査読は別である。誤りは依存する本文・要約・方針にも反映する。
文献は一次資料で仮定と適用範囲を確認し、未確認の書誌・内容・新規性を推測しない。

公表原稿は原則として日本語LuaLaTeXで、現在の成果を論理順に構成する。価値ある結果と十分な証明を保持する。
研究ノートには有用な着想、補題、例、反例、障害、文献比較を整理し、作業日誌や旧版の対応表にしない。
再開に必要な知識を会話だけに残さず、現行の方針・ノート・論文と必要コード・入力・小証明書で再開できる状態を保つ。
旧ZIP、旧原稿、バックアップ、ログ、キャッシュ、コンパイル中間物、入れ子のbundleは収録しない。数学的内容を削って軽量化しない。

研究区切りの承諾不要Library保存は一般的に許可されているが、本プロジェクトでは**GitHub mainを正本とし、GitHub保存成功時はLibraryへ保存しない。失敗時だけ緊急避難先として用いる。**
Library既存ファイルは明示指示なしに削除しない。GitではPDF・ZIP・中間生成物を追跡せず、TeX等から再生成する。
生成、検証、commit、リモート到達、Library保存は別状態として、実際に確認できたことだけを報告する。
通常のfast-forwardのみでmainへ保存し、force push、不要なPR、GitHub Actionsは使わない。
共有mainの更新は読み直して保存し、約15分checkpointは研究の終了条件ではない。未設定の背景実行や自動再開を約束しない。

## II. 現在の目標と達成基準

大域的な目標は強いintrinsic 14641型非可換三次曲面H3の完全分類である。
対象は構造対象付きAbel圏で、反Serre作用、Gabriel–Krull rank、exceptionality、AZ ampleness、三次曲面のHilbert値を満たし、
反標準環が一次生成、その二次包絡がnoetherian quadratic Koszul AS4型14641となるもの。
外部ambient・四周期表示・例外列を追加標識にしない。
全対象の被覆、全許容切断、pointed exact同値の全群oidと慣性、成分・交叉・境界、相対再構成・降下を達成基準とする。

**このリポジトリの最優先課題は強いintrinsic H3の完全分類である。**
(2,2) mixed rank4の全Jordan型の判定に続き、未被覆のCY・多固有値部分、全成分・相対降下に取り組む。具体的な最新frontierは下記第IV節と `research/cubic_14641_codex_plan.md` を読む。
楕円E6量子化成分の完全決定は [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) に分離済みであり、E6論文の改訂はその正本で行う。

## III. 現在の分類研究の最優先課題

本リポジトリの最優先は強い内在的14641型H3の**完全分類**であり、全対象の漏れない被覆、正規三次incidence、全幾何学的群oid、成分・境界、相対認識を完成させる。詳細な現行分類frontierと未解決の最小補題は `research/cubic_14641_codex_plan.md` と `research/cubic_14641_classification.md` を読む。

楕円E6量子化成分の8次元変形・全Artin形式分類とFricke–Askey–Wilson locusは、独立正本 [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) へ移管した。本分類には必要な認識定理と有効な具体例・証明を保持するが、E6成分そのものの相対H3開性・全境界・DAHA比較の研究は同リポジトリの研究方針に従う。ambient射の論文は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient)、標識忘却の論文は [nc-cubic-unmark](https://github.com/uedakazushi/nc-cubic-unmark)、量子Fermat非AS短報は [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) を新しい正本とする。

## IV. 全H3分類で保持する成果と未解決領域

詳細な証明と全係数は `papers/weak_cubic_axioms.tex` と読み込まれる各節、現行分類ノートにある。
今回この大規模分類の証明を独立再監査したわけではない。

- 全H3でmu_R=1、Gのnormalizerはmu_Bの逆。固定包絡の候補は単一140×20線型核。全skew包絡は31パラメータ・五型で幾何学的分類され、一般次元は4,1,2,1,0。
- 中央滑らか楕円境界はfiltered deformationからCY包絡を認識。有限位数の許容性は中心McKay条件、固定有限位数の被約表示族では中心形成・H3開性・底変更を扱う。非中央正規楕円境界は位数2または3で、Clifford swap・符号型・量子Fermatへ認識される。
- 分裂・非分裂Clifford族、指定PI4包絡の悪い中心値6個、有限位数一般の判定、非CY符号族のorderとBrauer分岐、量子三角境界の有限位数切断判定、固定三乗根の全P4中心切断・境界因子・慣性を保持する。
- proper Sklyanin、Stafford、指定Pym chart、指定as4具体表示の排除を保持する。全AS4の被覆を仮定しない。外部入力は `research/as4_imports.json` の固定SHAと規約を用いる。
- スペクトル(1,3)は幾何学的分類、(3,1)と(2,2) mixed rank2は全Jordan型込みで排除。mixed rank4のP=0,Q=0は既知族へ認識。両top非零の残余は詳細分類ノートの現行frontierを読む。

(2,2)完成部分のfrontierは **classification-v202**。最後のL0非鏡開集合の正常行加群を自由rank10の核へ移し、全多項式恒等式と10回の局所化単元pivotを公開コードから厳密再生した。両top非零の全候補が消滅し、(2,2)/mixed rank4の全H3は全Jordan型込みで既分類の曲がったClifford族に一致する。詳細な被覆・AS4点での底変更の証明は `papers/sections/cubic_order2_22_secant_L_complete.tex`。この領域の完成を全H3分類と同一視しない。
独立の[楕円E6量子化成分](https://github.com/uedakazushi/nc-cubic-e6)の研究では、三次の二次関係挿入45×48行列を44×44単元minorで整理し、包絡の三次平坦性を四つの係数の消滅へ帰着した。全次数平坦性を別途仮定すれば三次核は自動的に左右正則正規な主イデアル。20巡回potential方向の80個の斉次一次overlapは全て零と検証済み。指定potential chart内の高次flat性は上記定理で解決した。全intrinsic被覆は未完成。
全CY被覆、三固有値以上、全成分とintrinsic族降下も未完成である。

## V. 再現・関連研究

分類研究の再現・検証は `research/cubic_classification_validation.json` と `AGENTS.md` に従う。
独立の楕円E6量子化成分のTeX・計算は [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) を正本とし、そこで `python3 computations/verify_all.py` と `latexmk -lualatex papers/quantum_cubic_component.tex` を実行する。分類内で必要なH3認識の定理はこのリポジトリの公表用主原稿に保持する。
全H3分類の再現手順は `research/cubic_classification_validation.json`、例は `python3 computations/verify_cubic_skew_jets.py`。

heart比較・Rains共鳴・cubic cornerは `uedakazushi/nc-dp-surface-hearts`、次数1は `uedakazushi/nc-dp1-moduli`、三次三様体は `uedakazushi/nc-cubic-threefold-moduli` が正本。
量子FermatのOU障害は [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as)、ambient比較は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) に移管済み。分類に必要な旧定理・コードはこのリポジトリの現行分類原稿からも参照する。

## 現在の全H3 frontierと次の実行（v269）
三固有値H3の中山は半単純位数3で、必要スペクトルは(ω,ω,1,ω²)と(ω²,ω²,1,ω)の二つのみ（一つのGaloisラベル軌道）。幾何学的同型商とは区別する。重複1の(1,1,ω,ω²)は全22tensor atlasを排除した。全H3分類が完成したという意味ではない。
重複1の証明経路：独立結合を全排除、比例S非零をdomain外、両非零比例を六係数正常一次chartへ被覆し全w値を排除、片方零結合T0を強制mixed射影/Oreで排除。最後のT非零も以下で全排除。元atlasからの必要被覆にAS4先行完全分類を仮定していない。
T非零,a16非零：rank1表示のλ4=ω。λωはgeneric7因子/7曲線/11fresh点のexact全値判定。λ−ωはκ0でb正常、normalizerはUにω,cにω²なのでμ固定三次上固有値1だけ、要求固有値ωに矛盾。λ±iωはSchurからh=r±iκs,r=−(1±i)κs/2,A=∓iωκ²s/2。T=s1,κ0/1へ正規化した二点はQ(ω,i)=Q[t]/Phi12でどちらもdimB3=23、AS4値20に反する。
a16=0：Schurからa15=0,middle minorからa17=0。Ub/bU両射影rank2でa6=λr,a7=r,a11=a12=λh,a9=r,a13=h、(r,h)非零。正しい残余式はr(B−Z)+h(Z−(ω+1)A)=0（前節の未検証scratchのZ符号を訂正）。Schurからλ=σω,A=εωB。符号一致又はB0ならcrossR=λS、b正常normalizerのU固有値ω,−σω,c固有値−σω²。μ固定三次上固有値±1のみなので要求ωに矛盾。符号逆B非零ならh=r非零、残余式はB=(ω+1)Aを強制し、σ1,ε−1だけ。元22tensorは量子Weyl AS3(x,b,c)上の実y-Ore表示でq−ω²、bc+ω²cb=(2ωB/T)x²、δ(x)=−B/r*x²+T/(ωr)*bc非零。既存F非零最高y次数障害は一方曲率でも有効で、Gにx因子を強制。全T非零を排除。b,c交換で逆片方零も覆う。
公開証明はonezero_completion節。verify_cubic_third_root_unit_onezero_completion.pyのdefault Sympy再生PASS：正常bの固定三次固有値、minus元列恒等式、i-Schur二式/Phi12二fresh点、a16zero正しいminor/Schur、最後のOre元画像をdisplayed6関係で再挿入。最後はunit6minorでoriginalH=displayedR*coordinates、全分母支持rTのみを検証し、generic rankだけを全特殊化へ外挿していない。v269主原稿LuaLaTeX clean PASS。既存36 unified+16後続個別=52validators across runs、単一52一括未実行。新規as4/外部輸入なし。
次の最小課題：非単位重複rootの半単純22tensor atlasを実際に読み、mu=(ω,ω,1,ω²)の重み[1,1,0,2]で元quartic middle/正常三次を構成する。既存semisimple atlasとCY untwist定理はcubic_third_root_*及び分類ノートで確認し、unit-repeatの「固定平面U/正常x」議論を無条件に移植しない。U純quarticがなく、quartic型U³b,U²c²,U b²c,b⁴,b c³が許されるのでmiddle block分割が異なる。まず実関係パターンと正常三次7係数の必要条件を再構成する。
四単純の残る共鳴、全CY被覆、全成分・境界・相対降下も未完。移管済み独立E6/ambient/unmark/Fermat論文をここで再開しない。次は非単位root atlasから研究を続ける。

## 非単位重複rootの独立b²結合も全排除（v270）
mu weights[1,1,0,2]の元22tensorを構成。自己対称H0の語順(xc,yc,bb,cx,cy)はrank2、bbdiag0。b²列p(U)c+c r(U)のp=(a13,a20),r=(−ωa9,−ωa17)。一方のみ非零はfactorでdomain外。p,r独立ならGLUでp=x,r=y、rank2対称isotropic分解H0=PVt+VPt、P=(1,0,0,0,1),V=(0,t,1,−ωt,0)。従ってself関係xc+cy,b²+t yc−ωt cx。t0は純b²なのでdomain外。
残るM5×6のbc/cb射影minorはJ=mn−ω−1及びmnで差ω²、従って全m,nで射影rank2。c²行のt項からT=a21も非零。commonU/c/top diagonal actionでt=T1へ正規化可能（m,n不変）。bc/cbのJminorをpivotにした12linear式の最初8homogeneous determinantはω*J4*(m³+ωmn−n³)*(m+(ω+1)(n+1))。J非零なら二曲線F0又はL0に必要制限。F0非節点はm=−ωq²/(q³−1),n=−ωq/(q³−1)。L0はm=ω²(q+1),n=q。全値polySmith U A V=DとdetU/V constantsを掛け戻し、inhom最後4成分gcdはF:q(q6−q3+1)、L:q²+q+1。各Jの分子なのでJ非零で不可能、Fのq0節点のみ別扱い。J0はm=q非零,n=−ω²/q、別minorでpolySmithgcd qとなり全値不可能。
最後のnode m=n0はP8coeff唯一(0,−1,0,0,ω,0,0,0)。元22Bをfresh構成しdims3/4=20/35、正常36×7行列rank7、非零7minorで全核零。従って独立p,r全域をH3排除。通常証明はcubic_third_root_nonunit_independent.tex。公開verify_cubic_third_root_nonunit_independent.py default Sympy全PASS（3Smith/detunit/gcd/clear-denom support/node含む）、主原稿LuaLaTeX clean PASS。original22 utilityにweights引数を追加、旧completion validatorも再生確認。既存52+新1=53validators across runs、単一53全再生未実行。新規外部/as4輸入なし。
現行の非単位重複root残余はp=r0又はp,r両非零比例のみ。重複1は全排除済み、ここへ戻らない。二つの非単位スペクトルは共役で同じ証明入力を共有するがintrinsic同型としない。
次の最小課題：p=x,r=αx (α≠0)のrank2selfを整理する。H0=PVt+VPtとbottom=−ωtopからV=(u,v,1,−ωu/α,−ωv/α)、self関係xc+αcx、b²+u xc+v yc−(ω/α)(u cx+v cy)。v非零はUのy変更でu0,v1、v0はdomainからu非零及びα²+ω非零を必要とする見込み（純b²因子を避ける）。この分類と全境界を元画像で監査してから使用する。
v1候補coはa13=1,a20=a17=0,a9=−αω²,a11=a19=a3=a160,a12=1,a14=−ω/α,a7=−ω²α,a10=m,a18=n,a21=T。Mのbc/cb射影はn非零又はm²+αω²非零ならrank2。v1のc²行U²成分非零なのでこの開集合でT非零。残余torusでn,T両非零をn=T1へ正規化できる可能性があり、まず二係数α,mのrank2/正常7核を調べる。n0、射影退化、v0、p=r0を捨てない。四単純、全CY、成分/相対降下も未完。

## 非単位比例結合のv1,n非零の全排除（v271）
p=x,r=αxのself rank2はP=(1,0,0,α,0),V=(u,v,1,−ωu/α,−ωv/α)。v非零はy=ux+vyでu0,v1。v0はdomainからu非零,α²+ω非零、u1へ正規化。v1でn=a18非零ならbc/cb射影rank2、c²行からT非零。generator/top diagonalでn=T1を保つ正規化を明示。8homogeneous determinantはω(α+1)(α+ω)(α+ω²)²、αは−1,−ω,−ω²。polyQ(ω)[m] constant-unit消去で前三相rank8,8,7、残余m−ω,m−1,0。前二相は唯一二点ともB3dim22で非AS4。
α−ω²相はa15=Z自由、l=m+ω²,Y=y+lxで六関係の二変数表示を得る（本文）。originalH=displayedR*coordinates、unit6minor、全分母は係数体のみでall-specialisationの必要同定を検証。正常41×7は7constant pivots、source pivot支持4因子Z,Zl+ω/2,Z−ω²,Z−2ω²。4曲線の全関係/正常pivotのbad polyはそれぞれ1,l+ω²/2,l+ω²/4,Z(Z−ω²)(Z−2ω²)。全有限例外は二点、B3dim22で非AS4。よって全v1,n非零はH3なし。
v1,n0でもbc/cb射影rank2ならyb/by行が零、全y²成分も零、商(x,c)がk<y,b>/(b²)で指数増大し非AS4。従って残余はn0,T0,α=−ωm²,m非零、又はn0,T非零,α=m=−ω²のみ。T非零はT1へ正規化可能。u1,v0及びp=r0も未解決。
public verify_cubic_third_root_nonunit_proportional_open.py+model helper default Sympy全PASS（source incidence、7/8 constant polynomial pivots、source画像全掛け戻し、4曲線/2fresh点、n0projection minor/指数商支持）。v271主原稿LuaLaTeX clean PASS。累計54validators across runs、単一54全再生未実行。外部/as4新規輸入なし。
次の有力なT0証明（未統合・未検証）：v1,nT0,α=−ωm²ではrowcc pureQ=yx−ωm4xy、bc/cb射影rank1。domainQ非退化よりpureU rows比例。これからa1=a2=a150,a6=(ω²/α²)a5,a8=m a5、(m−ω²)a0=0,(m5−ω)a4=0,(m9−1)a5=0を得る見込み。全a0,a4,a50はpurec²でdomain外なのでm5=ω又はm9=1の13点へ必要制限。xは正常、normalizerφ=(1,ω²m^-4,m^-1,ωm²)。μ固定三次上要求固有値はω。m5=ωのorder15点は全φ固有値5乗根でW1零、mω²は全φ固有値1でW1零。m1/ωはGにx因子、m9primitiveでm³ωはW1零、m³ω²はG∈k<y,b,c>3。最後は実skew-cone B=A[x;φ]（purebaseA3関係）で既存lem:cubic-skew-cone-vertex排除が使える。各式・全根・実skew被覆を元22画像で監査してから正式化する。
T非零隔離相α=m−ω²,n0,T1では8cube係数のrank1pureU matrixが残り、domainのQdet非零を用いて必要被覆を調べる。v0,p=r0、四単純/CY/成分/降下も未完。
