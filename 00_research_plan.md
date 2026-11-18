# 研究方針：H3型内在的非可換三次曲面の完全分類

2026-11-18 / research-plan-v53 / H3分類専用。
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
三・四固有値領域は排除済み。全単一固有値のCY性も完成した。全CY切断被覆、全成分とintrinsic族降下は未完成である。

## V. 再現・関連研究

分類研究の再現・検証は `research/cubic_classification_validation.json` と `AGENTS.md` に従う。
独立の楕円E6量子化成分のTeX・計算は [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) を正本とし、そこで `python3 computations/verify_all.py` と `latexmk -lualatex papers/quantum_cubic_component.tex` を実行する。分類内で必要なH3認識の定理はこのリポジトリの公表用主原稿に保持する。
全H3分類の再現手順は `research/cubic_classification_validation.json`、例は `python3 computations/verify_cubic_skew_jets.py`。

heart比較・Rains共鳴・cubic cornerは `uedakazushi/nc-dp-surface-hearts`、次数1は `uedakazushi/nc-dp1-moduli`、三次三様体は `uedakazushi/nc-cubic-threefold-moduli` が正本。
量子FermatのOU障害は [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as)、ambient比較は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) に移管済み。分類に必要な旧定理・コードはこのリポジトリの現行分類原稿からも参照する。

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

### 二交換子の残る孤立型
非共有Segre、混合階数一Veronese、混合階数二の全VRパラメータ族を排除した。本文 cubic_CY_two_commutators_Segre 節。特にVRでは正常元aの平行移動の先頭核から中心元をk[a,b,tac+βbd]に絞り、cとの交換で中心三次が零となる。次は固定VTの孤立型Iについて元六関係から中心三次を判定し、二交換子の七対称射影の必要全被覆を監査する。

二交換子の孤立型Iも元VT行列から中心三次rank20（有理小行列式 -32768/22876792454961）で排除した。固定as4の cor:cy-two-commutators-complete の必要方向と合わせて全二交換子CY排除。残る非可換CY包絡の交換子次元は1又は3（3のbeta型は既排除）。次は一交換子の十六必要射影と三交換子の残る層で中央切断を判定する。

一交換子の最初の確認事項は、対称階数4では U 単体でなく (im SS,U) を保つこと。固定 CY_ONE_COMMUTATOR_RANKFOUR_PROJECTIONS の十六候補は非共有5・共有11で、最後の二型だけ積写像の核次元が3・2、他は1。階数5の円錐曲線型は別の排除定理を要する。二交換子追加後の主原稿組版は成功し、最終定理参照も解決済み。

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

### 三交換子alphaの重複直線と共点境界（v312）
三重直線・二重直線と別直線の型は全排除した。固定必要表示で、中央三次の持ち上げと境界の全tails自己一次拡大を計算し、三次元Ext1へのshift作用が行列式1となるためSerre traceに反する。二重直線は上流の下位係数軌道で分けず、重複直線上で下位二次式が消える点を二チャートで統一処理。共点三直線も共点で下位二次式が消える場合は同じ障害で排除し、上流五族のうち二次式にd²を含む第一族だけが残る。正確な条件はcubic_CY_three_alpha_nonsmooth節を参照。

### 一交換子の共有Segre全体（v314）
共有Segre十一射影を全排除した。うち七射影の必要表示十三個と全例外値では中心が零か可約三次一元、残る二平方・三平方射影の40係数域では中心三次が全て零。二空射影と対称階数五は固定as4の必要排除を適用した。次は未判定の非共有Segre $a^2+cd$ の24族・一孤立類から、同じ元六関係の中心行列と可約性で絞り、その後 $ab+cd$ を判定する。三交換子はalphaの残る被約先頭式と外積階数三・列係数階数三に集中する。

### 非共有平方・積追加型と原始三乗根の新しいH3族（v315）
外側・上行交差を元六関係の19検算と二固有値の濾過で判定した。等方外側の最後のb5と下行交差四族は残る。判定済み範囲で残る包絡Zの原始三乗根の両値は同型。中心切断P(a,b)+Cc³+Dd³は、CD非零、deg P(1,z)≥2、判別式P(1,z)^2−4CDν³の平方自由性が正確なH3条件である。三次巡回Brauer類の非分裂、分岐曲線上の巡回整環、b軸の完備量子平面とAS Gorenstein双対で証明。P=b³、C=D=1で非skew CYの具体例。固定包絡の幾何群oidはAff₁×μ₆作用、一般慣性μ₃、次元2。次は残るb5および下行交差の全因子被覆を完了する。

### 平方・積追加型の残る一族（v316）
等方外側b5は可換二元外の16座標を中心行列で一括して排除した。下行片成分Lの両符号と両下行・cd零のZも中心零。各五例外曲線の有理化・全残余数体・別の一孤立点を厳密再計算。固定された平方・積追加24族・一孤立類のうち未判定は下行開族M(s,w,z)だけである。次は元の三変数関係と係数の許容因子から中心三次を調べ、続いて二積追加へ進む。原始三乗根Z(s)の正確なH3判定と矢は確定済み。

### 三交換子alphaの対称ポテンシャル部分の完結（v317）
gamma=0の全切断と幾何学的矢を判定した。三角形・節点・割線二次曲線では、元挿入行の一次lift計算から低次二次式Q=0。指定軸の係数が非零で、アフィン中心の全特異点が階数1の通常二重点であることが正確なH3条件。無限遠のSchur補と四元数環の非分裂で貼合せと整域性を示した。滑らかな先頭式はHesse正規化と平方関係の排除を通じ、既存Clifford全判定へ接続した。この部分では固定as4の必要被覆を使用。三交換子の次はgamma非零のalphaと外積階数三・列係数階数三。一交換子のM(s,w,z)では三変数の四次商射影が計算上の障害なので、座標切片または疎な別基底による厳密rank証明を優先する。

### 三交換子alphaの量子三角形（v318）
gamma非零の三角形で全六係数の中心三次を決定した。q³≠1では中央ペンシルだけで、三つの一次係数が非零でなければ軸の奇数Serre障害が出る。従って一次係数1、三定数項任意へ規格化できる。全ペンシルは忠実差分模型で整域、全矢は符号・置換のS₄。非捩れOre開集合では四次式の重根で有限大域次元を正確に判定し、重根の一部でH3を排除した。全許容性は未完了で、次は非捩れの除いたweight軌道と射影境界、有限位数全定数項の中心と局所整環。有限位数の全定数項でChebyshev中心生成と中心自由基底も得た。原始三乗根の四つの活動中心三次は全六係数で再現可能。

### 三交換子alphaの節点・割線の中央切断（v319）
gamma非零の節点と割線で、原始三乗根を含め全中心三次をJとt³の二元に限定した。点対象のSerre障害により指定軸の一次係数は非零が必要。割線の原始三乗根はJがt,xの可換二元三次となり全排除。他の割線は二一次係数を1にして全ペンシルの忠実差分表示、整域・rank-one、非捩れOre局所化の五次式による有限大域次元を得た。節点の整域と滑らかさ、割線の閉軌道および有限位数の全許容性は残る。

### 有限位数の量子三角形とMの三境界（v320）
有限位数量子三角形の体積ペンシルは、全三定数項で射影境界の辺・頂点が有限大域次元。アフィンの単純加群間Ext³の消滅が正確なH3条件で、N³次元上界と有限双加群解消により有限代数判定を与えた（未実装）。q³≠1かつ有限位数の全量子三角形を覆う。M(s,w,z)のW±零と(16s²+1)w+64零は全中心三次が零で排除。Mの三境界因子非零域と二積追加が一交換子の残余。

### 列係数階数三の次の判定（v321）
外積階数三・列係数階数三の必要鉛筆12型は、二次中心商と持ち上げで、比4の半単純二重、係数1/4の長さ二・異固有値、四基点の曲線P_Bの三範囲に絞った。各包絡で唯一の中央三次がある。次は元の七係数表示でこの切断の整域性を優先し、残る場合に局所正則性を判定する。全証明・係数・検証器はcubic_CY_three_column_three節と現行分類ノートに保持する。

### 三交換子の外積階数三の完結（v322）
列係数階数三の三鉛筆で唯一の中央三次をL(da−cb)と因数分解し、残る全切断は非整域。既排除の列係数階数二と合わせ外積階数三を完結した。次は三交換子alphaのgamma非零に集中する。一交換子のMの三因子非零域と二積追加は残る。証明と公開検算はcubic_CY_three_column_three節および最新分類ノートに保持する。

### 尖点・接線・共点の最短経路（v323）
三型の全中央切断を決め、尖点・接線のd²係数零を点自己拡大で排除した。残る切断の整域性と内在的rank-oneは重み付き随伴環から判定できる。a=1はそれぞれE₆,D₅,D₄のKleinian量子化。次はアフィン量子化の正則パラメータ比較と射影境界の非可換な正則性を判定する。係数と計算はcubic_CY_three_alpha_additive節に保持する。

### 尖点・接線・共点の局所判定（v324）
アフィン有限大域次元は有限Dynkin根超平面とPBW像の有限多項式式で必要十分に判定できる。d軸の完備局所環は随伴Jordan平面・可換平面により左右有限大域次元。次はこの完備局所化とtails Extを比較し、射影境界の貼合せを証明する。実装されていない消去、未判定の貼合せ、具体的な着手は最新分類ノートを参照する。

### 尖点・接線・共点型の許容性を完了（v325）
点自己Extの直極限を可換退化と比較し、射影境界の唯一の特異点の完全性を示した。アフィン有限根判定が三型のH3に必要十分で、幾何矢も決定した。各残る固定包絡では除外された三次切断値は有限個。次は同じ点truncationの方法を非捩れ量子境界へ移すか、一交換子のM開域・二積追加を判定する。全成分・相対降下は未完成。

### 量子境界の完了範囲（v326）
規格化量子三角形の体積ペンシル全位数、q³≠1の割線・節点の必要軸条件全域では、H3はアフィンの有限大域次元と同値。節点の整域と内在rankも確定した。未判定のアフィン閉weight軌道・節点と原始三乗根、滑らかな先頭式、一交換子の残りを優先する。成分・相対降下の判定は残る。

### 滑らかな先頭式の全中央切断（v327）
滑らかな先頭三次の点曲線を楕円・成分巡回三角形に分け、全低次係数で中央三次kL+kt³を決定した。楕円境界有限位数の判定は既存中心・局所McKayへ接続。成分巡回の三角形と一部アフィン判定が残る。三交換子alphaの中央三次候補は全先頭型で決定済み。一交換子の二積追加は反交換二次元とOre表示の層から判定を進める。

### 二積追加の外側Ore族（v328）
非等方片外側三族は原始三乗根の一包絡だけに絞り、その全H3切断、幾何矢、一般慣性を決定した。非分解四交差の全候補は反交換二次元により排除。残る二積追加は18連続族・5孤立類。まず孤立類と等方片外側の構造を判定する。証明はcubic_CY_one_segre_double_split節。

### 二積追加の全孤立類（v329）
孤立五包絡を全排除した。四つは中央三次零、一つは全中央三次が一次式の立方。二積追加の残る18連続族では隣接・対角二交差と等方外側から判定する。

### 二積追加を分解交換子の三交差族へ削減（v330）
等方片外側九族は可換二元三次に限定し、六交差族は全例外を含め中心零で排除した。二積追加は分解交換子のTD1、FO1–FO2、FDC3の三族だけが未判定。実交換子平面を使った低係数表示を優先し、平方・積追加Mの開域と合わせて一交換子を詰める。

### 分解交換子の中央二次商（v331）
残る二積追加のTD1とFO1–FO2で、実交換子平面の中央二次で割った商に中心三次が単射となった。元の三変数式と再現器はcubic_CY_one_segre_double_split節。四変数のFDC3と平方・積追加Mは残る。次は二次商の中心または係数の低い元関係の小行列式で、三変数に残る例外面を判定する。

### 片外側四交差の線型例外を完了（v332）
FO1–FO2で別の低係数関係基底から第二の中心小行列式を構成した。二つの小行列式と商の分母の線型因子は包絡対称性の下で四軌道であり、四面およびその全例外曲線・点で中央三次零。次は両小行列式に残る二次・三次因子とその対称移送の共通零集合を判定し、次いでTD1・FDC3を詰める。

### 片外側四交差の全排除（v333）
FO1–FO2の中央三次は全許容域で零。残る四曲線は直接の二次数体計算、中央二次商の小行列式の終結式、次数8・18のファイバーの厳密最大公約数で完了した。二積追加はTD1とFDC3のみ。次はTD1にも中央二次商の小行列式と包絡対称性を適用し、FDC3の中央二次の候補を厳密検証する。

### 分解三交差の全排除（v334）
TD1の中央三次は全許容域で零。中央二次商と反対代数、元小行列式で五有理曲線に絞り、全曲線と例外九既約因子の数体を完了した。二積追加の残余はFDC3だけ。その中央二次候補を元関係で検証し、平方・積追加Mの三因子非零域と合わせて一交換子を完了する。

### 平方・積追加Mの中央二次商（v335）
Mの全許容域で実交換子平面内の中央二次を厳密検証した。X=4s,T=(kw−1)/(kw+1),Z=(wz−k)/kで、同型は三符号、反対代数はXの符号だけを変える。未判定域の三境界はX±TとX²+T。次は小次元の二次商で中央三次を絞り、FDC3と合わせて一交換子を完了する。

### 原始三乗根三角形の全切断と両外側四交差の中央二次（v336）
原始三乗根の量子三角形の中心は五生成元・一三次関係（t³を一変数とする）。可換三次曲面上の有限orderとして、全切断の整域性をtorsionとBrauer剰余、射影側を四チャートのExt³で必要十分判定し、全幾何矢を決定した。一般入力に対する消去の実装・相対降下・成分は残る。有限位数量子割線はChebyshev中心の二特殊ファイバー外を完了。FDC3も全係数の中央二次商へ還元。次はMとFDC3の中央三次、残る量子境界・アフィン判定を優先する。

### 原始三乗根節点と成分巡回三角境界の全排除（v337）
節点の原始三乗根はx+λyとtの二元三次に還元して全排除。滑らかな先頭式の成分巡回三角境界は対称低次項を平行移動し、結合則で中央三次をX f(X,t)へ還元して全排除。M・FDC3も許容有理点とFO1への退化で一般中心三次零。例外閉集合の明示判定と、残るアフィンの許容性を続ける。

### 有限位数量子割線の全切断（v338）
差分表示の反転に対するノルム因子を選ぶとk[x]が安定になる。周期行列の特性多項式から二つの最高モニック中心元を得て、全アフィンの中心有限性と単純の次元上界N³を確定。二つのChebyshev特殊ファイバーも単純間Ext³で有限判定し、切断値を含む全点付き矢も決定した。残る量子側の最小未判定は非捩れ割線・三角形の除外weight軌道、節点の非原始三乗根、滑らかな楕円境界の無限位数。一交換子のM・FDC3例外閉集合を引き続き優先する。

### Mの例外曲線と非捩れ型の差分認識（v339）
Mの中央二次商は五固定・二変動関係で次数四を計算し、符号作用後の13因子の共通二面を全排除。例外は次元高々一。次はZ方向の終結式と、残る有理グラフ・混合曲線の数体ファイバーで完了する。FDC3もe一次行列の階数が2で同じ分解を試す。非捩れ三角形の体積切断は全係数で球面DAHA。非捩れ割線は五次分子の同じ型。両者の射影境界は既決定で、アフィン全正則性を判定する。

### Mの六低次面を完了し、非捩れ三角形の許容開を決定（v340）
Mは三つのT有理面と三つのZ一次面を全排除。78剰余体の厳密rankを含む。残る必要支持はT二次式一つとZ次数2,2,3,4の四式の対称交差。次は第二小行列式と終結式でこの閉集合をさらに縮める。非捩れ三角形は球面DAHAのfull性と自由積の大域次元から四次式平方自由でH3。定数項なしの全体積ペンシルを確定。定数項付きの残余は除かれたweight軌道にのみ重根を持つ場合。

### 平方・積追加Mを全排除（v341）
Mの最後の五因子は第二の中央二次商の階数証明書と四符号移送の両方で絞った。ZとTの終結式、Xの数体での二段の最大公約数により、残る11剰余体の元中心階数は全て20。これで平方・積追加の最後の未判定族が閉じ、一交換子の未判定は二積追加FDC3だけ。次はFDC3の五固定・二変動関係で第四次の商を構成し、符号移送又は特殊化で例外を絞る。三交換子の非捩れ割線・節点・楕円のアフィン、全成分と相対降下も残る。

### 非捩れ量子三角形・割線の全二重根を判定（v342）
割線は折り畳み五次式が平方自由ならH3。二反転の遺伝的orderのLaurent環上自由積を作り、球面cornerを差分生成環と同定し、平方自由なら冪等元がfull。三角形・割線の根の重複度が高々2なら、非平方自由は全て排除した。冪等元を殺した半単純商の全単純は自己Ext²が非零であり、導来corner三角から大域次元無限。非捩れの未判定は三重根以上を含み、全重根が例外weight軌道に載る場合に縮む。FDC3と節点・楕円のアフィンを最優先し、高重根の残余、全成分・相対降下へ続ける。

### 非分岐の単独三重根とFDC3の積表示（v343）
非捩れ三角形・割線で単独三重根が分岐値±2の外なら、例外weight軌道上も排除。冪等元を殺した商はIwahori型orderの中心ファイバーで、全非零加群MについてExt²_H(M,Q)≠0。残る高重根は分岐の三重根、五次の3+2、および重複度4以上。FDC3は全許容点でab=ba=−cdの基底があり、中央二次の判別式はLの四線型因子に分かれる。この基底で次数四の行消去を進める。節点ではE6一般化DAHAの三関係と中央三次のスカラー化を厳密に確認したので、球面cornerの認識と係数像を次に確定する。

### 節点切断をE6一般化DAHAへ接続（v344）
単純根λの球面cornerでx,y,zを明示し、七変数の四書換えで節点三関係・中央三次のスカラー化を検算。F123随伴環でxは次数1の定数、yは隣接二極を持つ次数2の切断となり、全位数で生成。重みHilbert値により同型。生成元倍率付き係数写像は全許容qで支配的。有限位数の稠密開H3、単純根表示の全有限位数のExt必要十分判定、各非捩れqの量子トーラス半直積点を得た。次は係数像の補集合と非捩れの有限大域次元を決める。FDC3の四変数次数四計算とm=0の例外面、残る高重根・楕円アフィン、全成分と相対降下も続ける。

### 節点E6表示の分離スペクトルを全判定（v345）
分離三次部分代数の自由積とabc=κから長さ2の双加群射影解消。左端核は有限次元右イデアルを与え、F123の次数1定数で消える。H3はH/HeH=0と同値。商は17語と関係像の不変閉包で厳密判定、零と次元4の両例を検算。fullなら重根は全排除。非捩れも各許容qの稠密開H3を確定した。次はE6係数像の補集合と重根かつ非fullの非捩れ域、FDC3の厳密例外支持、残る高重根・楕円・成分・相対降下。

### 節点E6単純根チャートの全H3判定（v346）
重根があり非fullの場合も排除した。F123からHはnoetherian、eHは球面環上有限。相対双加群列は重根でも完全で、H係数のExt²は有限次元加群の線型双対、高次Extは零。非fullの導来corner三角を完全化すると正次数自己Homが生じる。従ってE6単純根チャートのH3は三スペクトル平方自由かつ17語商零に厳密同値。節点型で残るのはE6係数像の補集合。次はこの双対法を非捩れ三角形・割線の高重根へ適用し、FDC3例外支持・楕円アフィンと相対分類を続ける。

### 非捩れ量子三角形・割線を全判定（v347）
四次・五次のFが平方自由であることがH3に必要十分。補角の差分係数はa,bをqa,qbへ移し、逆ノルム認識で両角noetherian。反転orderの余誘導した入射解消と留数対合により、有限次元MでExt²_H(M,H)=M*、高次零。従って非fullは常に排除され、任意の重根を非fullへ置ける。非捩れ三角形・割線の許容切断は完了。分類の次は唯一の一交換子FDC3、E6像の補集合、非捩れ楕円アフィン、全相対降下・成分。

### FDC3の中央三次候補を次元2以下へ削減し、節点群oidを決定（v348）
FDC3は新基底のE一次性を使い、三・四次の商を疎な列ピボットで作った。独立の分母・ピボットを分けると例外は10既約因子。八実同型移送の主チャート外も含め、共通超曲面は五つ。それぞれ許容有理点で元階数20なので中央三次候補は次元高々2。m=0は六例外チャートで局所計算を進め、残る曲線と剰余体、一般の二次元残余を判定する。節点型の全幾何矢は規格化後μ₃とq逆転で、交換時に切断定数のB_z補正を含む。節点の残余はE6係数像の補集合、楕円は非捩れアフィン、全成分と相対降下も継続。

### FDC3のm=0と二判別式面を全排除（v349）
m=0は二つの対称式、十有理チャート、11曲線、133個の剰余体と別の終結式枝で全階数20。四変数の第二階数証明書は8因子で全16移送に共通する超曲面を二判別式面に削減。第一判別式面は局所全域、第二面はSの外の二次剰余体を含め全排除。次は四L一次面、L二次面、一つのE一次面を両証明書で判定。節点E6像補集合、非捩れ楕円アフィン、全成分・相対降下も残る。


### FDC3の二つの非線形枝を六平面曲線へ射影（v350）
四L一次面の外では、二つの階数証明書と八移送の必要支持をE、Lの順に消去できる。L二次枝はM=P±1、PM+1=0、M²+4MP+P²+3=0および有限集合に、E一次枝はMP+M−P=0、(PM−1)²+(M−P)²(M−P+1)=0および有限集合に射影される。前者の四曲線ではLの全許容根が有理式となる。各枝で局所階数と残る剰余体を判定し、四L一次面を閉じる。節点E6係数像補集合、非捩れ楕円アフィン、全成分・相対降下も残る。

### FDC3の四L一次面を全排除（v351）
四つのL一次面は局所階数証明書と全16移送で14基底曲線と有限個の剰余体に還元。全14曲線では許容候補がなく、曲線外の14剰余体はいずれも元中心階数20。FDC3で残るのはL二次・E一次枝だけで、六平面曲線上および曲線外の有限部分を階数判定する。節点E6像の補集合、非捩れ楕円アフィン、全成分・相対降下も続ける。

### 節点型をE6 Weyl判別式で完全判定（v352）
規格化六係数は、選択c根をq倍した三つ組の対称係数を通じてE6トーラスの基本軌道和から三角的に生成される。全許容qで有限全射。三根のいずれかを戻せば単純根を選べる。H3は根指標が全て1と異なることと同値。根上はWeyl群でbの重根へ移す。根外の非full単純を積写像の微分で次元3以下に絞ると、行列式が根上を強制する。節点層は既約次元7、各qで稠密開、全幾何矢は既決定。残る優先課題はFDC3の非線形枝の最終有限検算、非捩れ楕円アフィン、全成分と相対降下。

### 節点の相対係数表示と分裂楕円切断の双加群滑らかさ（v353）
節点の全規格化係数はq方向とE6根正則トーラス商の積。対角三乗根と接線交換は中心乗法・qとトーラスの同時逆転となり、半直積による代数的表示スタックを得た。分裂楕円切断の非零値は中心三乗根の有限分離拡大と対角の導来基底変更により、任意の標数零代数閉体で双加群滑らかなCY2と証明。非分裂の無限位数アフィン判定は残る。FDC3のE一次面最後の有限枝の数体検算と、全成分・相対内在再構成へ進む。

### 非分裂・無限位数の楕円切断に明示的な非H3族（v354）
有限次元加群の自己Ext¹はH3なら2-CYの交代対合で偶数次元。一次元表現では三アフィン関係と切断の可換Jacobianから判定できる。(p,q,r)=(1,2,3)のSklyanin境界点(1:2:3)は5,17で点数9,21の良い還元により非捩れ。平行移動で消せない2係数の対称二次項に対し中央三次を厳密に持ち上げ、原点のJacobian階数2で全二係数域を排除した。この偶奇条件は全無限位数切断の必要条件。非分裂楕円の有限大域次元の十分判定、FDC3最後の有限枝、全成分・相対降下を続ける。

### 一交換子CYを完結し、楕円のキャラクター障害を境界式で記述（v355）
FDC3のL二次枝とE一次枝を全排除。六平面曲線と七有理表示、ノルム、曲線外25剰余体（6+19）の元階数20で一交換子CY全域が完了。楕円の一次元表現では、階数2のHessianの核方向への中央三次の微分が境界楕円式の非零係数倍である。自己Ext¹は核点がE上なら1、外なら0。階数0,1,3では3,2,0。次の焦点は非分裂無限位数楕円の全有限大域次元、および全成分、交叉、相対再構成・降下。

### 楕円の全一次元加群の射影次元と、二次元障害（v356）
Sklyaninのアフィン包絡で自由解消1,3,3,1に中央三次のホモトピーを作り、切断上の周期解消へ移す。原点の奇数微分は零、偶数の4×4行列式はHessianの余因子行列の明示的三次式。一次元加群の射影次元は正確に2または無限。固定包絡で無限射影次元の一次元加群を持つ切断値は高々8。別の明示的な無限位数切断は一次元表現が空で、二次元単純の奇数自己Ext¹から非H3。全非分裂楕円の有限大域次元判定、全交叉、相対再構成・降下へ続ける。

### 三交換子CYと可換三次の共通八次元表示閉包（v357）
中心三次次元2の全α表示は先頭三次を滑らかにし、DVR上の同Hilbert値と交換子核で中央切断を持ち上げる。原始三乗根で中心が跳ぶ三角形では、正則な普遍Jの四一次方向がΩ,X,Y,Z全体。q=−1ではA_i=(q+1)U_iで全Clifford切断、q=1では一次項から全滑らかな可換三次を同じ滑らかな楕円の既約閉包へ特殊化。一般幾何商は8次元、節点層は余次元1。次は他交換子層や非CYとの交叉、相対内在再構成、無限位数非分裂楕円の全アフィン判定。

### 幾何表示の四成分と相互特殊化の排除（v358）
一交換子CYの全許容表示は固定原始三乗根で二元二次式fを持つ同じOre族に入る。非退化fから全点へ特殊化し、部分空間・二直線の極限で整域性が枠の退化を排除するので、この部分は閉。三交換子・可換三次は前版の共通閉包。一方、中山traceは二次双対の次数3・4の有限rank stratum上のFrobenius対合から正則で、値4,−2,0を分離する。H3幾何表示の四成分と一般次元3,8,4,5を決定した。次は未判定の無限位数非分裂楕円の有限大域次元と、一般の内在圏の族から表示への再構成・降下。
