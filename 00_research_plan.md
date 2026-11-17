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
三固有値領域は排除済み。全CY被覆、四単純共鳴、全成分とintrinsic族降下は未完成である。

## V. 再現・関連研究

分類研究の再現・検証は `research/cubic_classification_validation.json` と `AGENTS.md` に従う。
独立の楕円E6量子化成分のTeX・計算は [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) を正本とし、そこで `python3 computations/verify_all.py` と `latexmk -lualatex papers/quantum_cubic_component.tex` を実行する。分類内で必要なH3認識の定理はこのリポジトリの公表用主原稿に保持する。
全H3分類の再現手順は `research/cubic_classification_validation.json`、例は `python3 computations/verify_cubic_skew_jets.py`。

heart比較・Rains共鳴・cubic cornerは `uedakazushi/nc-dp-surface-hearts`、次数1は `uedakazushi/nc-dp1-moduli`、三次三様体は `uedakazushi/nc-cubic-threefold-moduli` が正本。
量子FermatのOU障害は [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as)、ambient比較は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) に移管済み。分類に必要な旧定理・コードはこのリポジトリの現行分類原稿からも参照する。

## 多固有値領域の現行到達点（v283）
強いintrinsic H3のAS4包絡は相異なる中山固有値をちょうど三つ持たない。全Jordan型の必要還元、重複1の全22tensor atlas、非単位重複rootの独立・非零比例・零b²列を全て排除した。全H3分類の完成ではない。全CY、四単純共鳴、全成分・境界、相対降下は未完成。

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

### 次の最小課題：39軌道の正常三次incidence
private追加因子計算で、全三変数とforced skewを持つnormalgen iの純i³をμ_i≠1ならG liftから除ける（φ_i eigen1と必要μ_iの不一致、共通固有liftが取れる）。さらにG指数がu²zとv z²だけで、u/z pair forcedskew、v/z relation support⊂{vz,zv,u²}かつrank1なら、向き別書換えで共通z因子。この追加で32軌道/95ラベルまで縮む見込み。private four_simple_finite_factor_advanced.py（入力は既存factor.jsonを明示load、古いchar.jsonの69軌道に戻らない）とlogにある。未公開なので39が現行正本frontier。
有力な全support sieveを進める：各候補でquarticの文字数support S（orbit全係数ではなくcount型）とG count support Tを列挙。全変数被覆・nonmultilinear・各I2 rank上界/domain prunerとfactor必要条件を課す。forcednormal zがあればnormalizer scalars u_i(u_z1)について全w∈S,v∈Tでu^w=u^v=μ_zが必要（正常一次hdet補題）。小整数Smith/左核でこのmonomial方程式の不整合を全supportについて判定する。特に残位数15二型はmultilinear+単一非multilinear top、二G型が必要で、normalizerからμ_z²1又はμ_z5=1となり実際の根位数に反するはず。通常証明と全support被覆を監査する。
新候補はW1非零だけでH3としない。全CY、全成分・境界、intrinsic群oidと相対降下は引き続き未完。新規性未確認。
