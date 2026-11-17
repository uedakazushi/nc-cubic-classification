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

## VI. 現在の全H3 frontier（v266）
三固有値H3の中山は半単純位数3に限られ、必要スペクトルは(1,1,ω,ω²),(ω,ω,1,ω²)と後者の共役の3個（2 Galoisラベル軌道）である。これはk-linear moduli同型による商ではない。重複1の全22tensor atlasはrank(P,Q)=1,S0まで必要制限され、両結合非零比例の場合は六係数正常一次chartへ被覆し、wの全値をH3排除した。残る重複1は片方零結合のみ。非単位重複根atlas、四単純の未被覆共鳴、全CY、成分・境界・相対降下は未完。各還元の証明は主原稿と分類ノートにあり、現在の最小課題は以下を読む。

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
