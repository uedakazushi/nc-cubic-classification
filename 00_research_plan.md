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
次は低次元像→Veronese復元と元AS4 Veronese除外（上流VEX1–VEX14）を監査する。本文全証明を読んだ。固定上流verifierを/workspace/work/as4-vex-auditへコピーし、固定referenceは書き換えず、PYTHONPATH python-deps+as4code, SYMPY_GROUND_TYPES=flintで全controlを再実行しPASS（8.93秒）。元25混合kernel、六最大等方plane/全八cubic代表、全GB、translation全orbit、alpha Hilbert22/beta degree4dim37を全再生した。これは上流control replayであり独立再実装とは別。まだ公表入力へ未統合。19KBの証明書はprivate as4-vex-audit/certificatesにある。次は最小元inputに全26?（Veroneseは25）混合matrixと全八枝/二fixed代表を保持し、当repo独立GradedAlgebraでalpha/betaの元Hilbertをfresh再計算する。定理を使う際はas4_importsへsourcehash/全仮定/検証区別を追加する。
これが完成するとCYc0対称像の低次元ケースを消し、三次元像の第二二次関係からCI22必要被覆の幾何論証へ接続できる。CI22七射影型と全表示の被覆監査は次段階であり、既存具体表示T/P等の中心排除は全値完成済みなので再計算しない。全CY切断・intrinsic群oid・成分・相対降下は未完成、新規性未確認。
