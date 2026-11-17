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

分類frontierは **classification-v202**。最後のL0非鏡開集合の正常行加群を自由rank10の核へ移し、全多項式恒等式と10回の局所化単元pivotを公開コードから厳密再生した。両top非零の全候補が消滅し、(2,2)/mixed rank4の全H3は全Jordan型込みで既分類の曲がったClifford族に一致する。詳細な被覆・AS4点での底変更の証明は `papers/sections/cubic_order2_22_secant_L_complete.tex`。この領域の完成を全H3分類と同一視しない。
独立の[楕円E6量子化成分](https://github.com/uedakazushi/nc-cubic-e6)の研究では、三次の二次関係挿入45×48行列を44×44単元minorで整理し、包絡の三次平坦性を四つの係数の消滅へ帰着した。全次数平坦性を別途仮定すれば三次核は自動的に左右正則正規な主イデアル。20巡回potential方向の80個の斉次一次overlapは全て零と検証済み。指定potential chart内の高次flat性は上記定理で解決した。全intrinsic被覆は未完成。
全CY被覆、三固有値以上、全成分とintrinsic族降下も未完成である。

## V. 再現・関連研究

分類研究の再現・検証は `research/cubic_classification_validation.json` と `AGENTS.md` に従う。
独立の楕円E6量子化成分のTeX・計算は [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6) を正本とし、そこで `python3 computations/verify_all.py` と `latexmk -lualatex papers/quantum_cubic_component.tex` を実行する。分類内で必要なH3認識の定理はこのリポジトリの公表用主原稿に保持する。
全H3分類の再現手順は `research/cubic_classification_validation.json`、例は `python3 computations/verify_cubic_skew_jets.py`。

heart比較・Rains共鳴・cubic cornerは `uedakazushi/nc-dp-surface-hearts`、次数1は `uedakazushi/nc-dp1-moduli`、三次三様体は `uedakazushi/nc-cubic-threefold-moduli` が正本。
量子FermatのOU障害は [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as)、ambient比較は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) に移管済み。分類に必要な旧定理・コードはこのリポジトリの現行分類原稿からも参照する。

## V. 最新の具体的frontier（v261）
三固有値の全半単純スペクトルを有限化し、位数4・5・6・9・12と相反pencilを排除した。残る必要候補は位数3の3個のみ（2 Galoisラベル軌道）、各関係パターン一つ。全Jordan層を排除し中山自体が半単純・位数3である。3候補の存在・H3許容性は未分類。
証明は `cubic_spectral_resonance.tex`、`cubic_inverse_spectral_pencils.tex` と `cubic_*root*`、有限リスト/全再生は `python computations/verify_cubic_spectral_reductions.py`。最新の証明・文献入力・certificateと次の最小課題は分類ノート末尾に統合した。
位数4は全排除済み。最後の(i,i,-1,-i)はb4零の四表示でW1因子/零、b4非零はrank2 middleのSchur補と非退化対称二次の巡回障害で空。単冪も含む。位数3の非単位重複根の全Jordan層も、実際の中山巡回式の85変数線型系と指数増大商で排除。重複1のJordan層も実際の12次元top核、Ore認識とker(D)=A、量子平面商の正常三次障害で因子を強制し全排除。残る二ラベルの半単純topは各22次元、正常三次係数は8/7次元。C=B^muという可逆なCY untwistを証明し、Gは同じ次数付きvectorで正常化mu^-1を保つ。GはCで非中心、CY中心三次分類を代用しない。重複1のatlasではP=Q=0及びP,Q独立/S=T=0を全排除。後者は一変数族へ還元し、全pivotとSmith因子、κ0/-1のfresh検算で全値W1零/非AS。独立P,QかつS0はT非零も二変数平面・四境界曲線・残る一変数族/三例外値の全pivotで全排除した。独立P,QのS非零も全Schur分枝と有限/一変数/行列式零境界を排除済み。比例結合の一方的非零曲率AS2–Ore表示も、正常c/b/基底一次の順序付き係数で全因子となり排除。Ore被覆は別問題。比例結合でもS非零は全AS4整域が存在せず、全unit-repeat H3はrank(P,Q)=1,S0に限る。最後は正常一次商の二つの三次overlapによるHilbert矛盾。二方向曲率split Ore族も全qのW1をSmith形式で分類し、因子/頂点で全排除。x²非split変形も中心Casimir/ノルム/曲面period=indexから九乗根商の非整域性を示し全排除。量子Weyl AS3基底を持つ全二方向曲率Ore層も、全補正項をshear又は共鳴付随次数で排除。両非零比例結合は元22tensorからT=a2=0と正常xを強制し六係数の正常一次境界へ被覆。w非零の境界商はw1へ正規化し、明示Δ非零の全開集合で正常核を排除。L曲線の明示Ω開集合では全u,vの正常核が一本で全次数持上げを明示。全u,vの実AS4整域性も1-regular xと明示W3持上げで認識し、中心Ψを明示。境界translation位数9とaffine ambient/切断のPI性も中心二元とGK1定理で証明。固定E2,u1,v0の独立閉点では中心部分環k[x,Ψ,z9]上自由階数81を完全な有限証明書で確認。その固定例の全中心も多項式環、generic CSA次数9・primeと正の有限体witnessで確定。E2,w1の全Z,u,vは位数3相対双対と二fiber resultantでH3排除済み。次は全L/Ωへの持上げ、残るΔ曲線/Ω零点、w0、片方零結合、非単位重複根atlasを調べる。P,QはUb3/Uc3、S,Tはbbcc/bcbc係数。
四単純chart(a,-a,i/a,-i/a)はa4≠±1全域をAS2因子で排除、a4=-1も既証二固有値障害で空、a4=1の有限四単純境界を保持。as4固定commitのchartを参照し被覆/AS十分性/同型は輸入していない。四単純の残る共鳴領域、全CY被覆、全成分・相対降下は未完。
一般正規三次の四line compact frameは `cubic_hypersurface_frame.tex`。rank-one torsion-freeは別仮定で、有限H3検査や相対開性は未証明。


## 正常一次L境界の現在位置と次の実行（v261）

E2の全正常一次境界の排除（v257）：v1,u=aの二中心fiber(Znew=b及び1)を標数0K[a]上で構成。全生成元のfiltered degree inequalityからtrace det次数≤486、p1021,t169の還元でも両486次を保存。487点補間+8点再確認、各340*h9^54の掛け戻し、h9同士Bezout1、trace resultant965非零で標数0coprime。trace非退化開集合では中心projectorのrank一定なので、各fiberで一点の中心1から全semisimple点がCSA。二trace開集合が全aを覆い、E2全v非零がgenericCSA9/fullcenter。相対双対ν3の局所order障害、v0既排除、Zの既知shearでE2,w1の全Z,u,vはH3なし。有限例外比の列挙問題はこの固定E2では解消し、解決済みへ戻らない。次はE可変のL/Ωで中心9の定数pivot型を認識し、同様の二fiber resultantを持上げる。全L曲線/他Δ境界/非単位根/CY/成分/降下は未完。

全L/Ωのアフィン包絡PI次数（v258）：Rains Thm2.13を各中央商D/(psi−lambda)へ適用し、全fiberの中心flat、domain、中心rank81・PI9を得た。Dはk[psi]上自由で∩(psi−lambda)D=0、全fiberのmatrix9恒等式がDへ戻る。grDもPI9なのでD自身のPI次数は正確に9。正常商Uの全素因子はPI degree≤9。Uの全中心/素性/degree9をこれだけから外挿しない。直接のgenericE中心探索は公開function_center scriptを使い、GF109(E)[d]・u,v多項式でdegree7まで到達。係数膨張があるので次はinverse cacheとu1v0固定枝で最小center9持上げを確認する。center9の完成結果はまだない。

全L/Ω正常一次境界の完成した排除（v260）：同PI次数を保つtrace-closed中央商の中心持上げを通常証明で確立。CはLBSのAR/CMとgraded stablyfree、PI9からStafford2.10/2.11によりtrace-closed。Z(C)→Z(S_C)全射。正常ΓのTHCR像は一つの被約9点軌道を切り、軌道上非消滅の中心9をCへ持上げるとAのboundary fiber(x0,Psi0,z1)=Mat9。全L/Ω,全u,vでfull polynomial centerとfree81/genericCSA9、relative Frobeniusν3を認識し、finiteglならperiod|3、domainならperiod9の矛盾で全Z,u,vをH3排除。有限field center探索はこの一般証明の前提でなく、E2全exact計算を独立な検証例として保持。
正常一次境界の現在の必要被覆（v261）：Etingof–Ginzburg Thm3.3.2(ii)は任意のhomogeneous CY topと任意lower potentialでnonscalar centre≤3を与え、genericを要求しない。全六係数untwistのpotentialを元関係でexact確認。H3のproper Sklyanin境界なら正常Gからτ9、従ってEG中心のleadingはcanonicalg0。v260のRains/Stafford/9軌道/周期障害を適用でき、全proper elliptic層をL/ΩやZ-shearに依存せず排除した。残るw1必要候補はD0,E≠0又はE0,D≠0の二軸と99個の明示点のみ。99点はD=−ω^b(t+1), E=ω^(b−a)t, a,b=0,1,2、共通squarefree11次h(t)=0で与え、全係数はelliptic_reduction節/certificate。Δ上への9Hesse線代入、axes/nonPHS除去、全点重複なしをexact確認。Ω33点を独立優先課題として再開せず、この二軸/99点を次に判定する。各点でもZ,u,vの正常核とadmissibilityは未完。w0、一方零結合、非単位根atlas、全CY・成分・降下も未完。

## 現在の正常一次境界：六軸点のみ（v263）
二軸のSmith標準形は(1,1,1,D³+ω²)、(1,1,1,E³+ω)。関係pivotは非零軸変数のmonomial、Smith変換はconstant determinantで全非零軸値に有効。軸は各3点へ必要制限。六軸点の全u,v正常三次は各一本、原稿axis-incidence命題のG_E/G_D。元四正常式の多項式再代入までPASS。ZはD+ωE≠0によりshear除去可能。u=v0は頂点障害で排除。残りはv1,u=aとv0,u1。
非軸99点は45算術ケース（9 Hesse線×2 linear+3 cubic）を厳密計算して全て境界正常核零。Q(ω)とQ[q]/(q6+q3+1)で次数3/4商を全元関係から再構成し、正常行列4列の非零4×4 minorを各ケースで確認。三つのcubicには(ω,t)=(q6,1/(q−1)), (q3,1/(q−1)), (q3,q+q^-1−1)を用い、対応する既約因子恒等式も検証。固定ωでの全99幾何点を覆う算術埋込みであり、moduli同型商ではない。従ってw1正常一次chartのH3候補は六軸点だけ（全Z,u,vの許容性は未完）。公開verify_cubic_third_root_unit_boundary_99.pyとcertificateが証明を再現する。
次の最小課題は六軸切断の整域性/有限gl判定。private exact診断でE0,u1,v0のC/Gはcentre次数1,2,3,6,9が1,1,2,3,5、ambient中心9は7。候補canonical中央三次Psi=y³+vxy²+ux²y。全u,v中心9持上げ、free81、正のcentral fiberの構成を検討するが、現段階でこれらを定理にしていない。proper ellipticの被約9点orbit証明をfat triangle境界へ無条件には適用しない。w0、一方零coupling、非単位重複root atlas、全CY/成分/相対降下は引き続き未完。as4の新規輸入なし。

## 正常一次chartの非零w全排除：現行frontier（v264）
六軸点の全Z,u,vもH3なしと証明。E0,D³=-ω²型では全u,v多項式係数のcentre9重み0行列46列を41constant unit pivotsで消去し、全5核を元交換子へ再挿入。Psi=y³+vxy²+ux²y、選択Z9のx0像はパラメータ非依存。A/(x,Psi,Z9)はArtinian Hilbert列1,3,6,8,9,9,9,9,9,8,6,3,1,0、総81。H3仮定で既知の全Hilbert級数とgradedNakにより、三中心元代数的独立/自由階数81。有限次数だけでAS4全次数を主張しない。
元x0,Psi1,Z0 fiberの補助中央hによる斉次化で、p109,t4,ω63の正則trace det108、centre rank80 minorが非零、元関係81次matrix再挿入PASS。正のminorが標数0にliftし、全uv共通fiberCSA9。従って全uvでgenericCSA9/full polynomial centre/prime。相対Frobeniusν3からfiniteglならperiod|3、domainならsurface period=index9で矛盾。他軸はB(D,E,0,u,v;ω)^op=B(E,D,0,u,v;ω²)及びG_E^op=G_Dを元関係で照合し、domain/左右finiteglの反対環不変性で排除。moduli同型とはしていない。全w≠0正常一次chartがこれでH3から除外された。
公開axis_center.py/axis_CSA.pyのdefault Sympy再生PASS。v264主原稿LuaLaTeX PASS clean。既存36 unified+10個別新規=46validators across runs（単一46一括実行とはしていない）。新規外部定理/as4輸入なし。
次はw0。探索段階ではD≠0をD1正規化し、E≠0,E6≠1の境界正常行列14×4のSmith因子(1,1,1,(E³−1)(E³+ω²))を得た。したがってこの開集合ではE³=-ω²だけが残り得る。E0、D0、E³=±1のfresh検算と全pivot supportの監査は未了なので、まだ全w0被覆定理にはしていない。E³=-ω²をPhi18体で扱うと全u,v正常核は27×8、constant7pivots、残余零で一本。v0は既存Ore除外に入る可能性があるが、その適用/パラメータ規約を監査してから用いる。v非零の正常切断/中心を次に判定する。一方零coupling、非単位重複root atlas、全CY/成分/降下も未完。
