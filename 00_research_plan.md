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

## 三固有値の現行必要被覆と再開課題（v273）
三固有値H3の中山は半単純位数3、必要スペクトルは(ω,ω,1,ω²)と(ω²,ω²,1,ω)のみ（一つのGaloisラベル軌道、幾何学的同型商ではない）。重複1の(1,1,ω,ω²)は元22tensor atlas全体を排除済み。全CY・四単純・成分/境界/相対降下と全H3分類は未完成。

### 完成した証明と再現入口
重複1：独立cube結合/S非零/両非零比例の六係数正常一次chart/片方零T0及び全T非零を排除。最後はonezero_completion節・checkerの正常b固有値、Phi12二点nonAS4、a16zeroの最後の実Ore表示δx非零。source originalH=displayedR*coords、unit6minor、分母rTだけを確認。古いL/ΩやE2中心へ戻らない。
非単位重複根：自己対称H0のb²列はp(U)c+c r(U)、p=(a13,a20),r=(−ωa9,−ωa17)。一方零のみは因子でdomain外。独立p/rはp=x,r=y、self xc+cy,b²+t yc−ωt cxへ。t/T非零、対角変更でt=T1、Mのbc/cb射影minor J=mn−ω−1とmnで全値rank2。8homdet ωJ4*(m³+ωmn−n³)*(m+(ω+1)(n+1))。F/L/J三曲線のpolySmith inhomgcdで全値不可能、最後node m=n0の正常36×7rank7で排除。証明nonunit_independent節/checker。
両非零比例：p=x,r=αx (α非零)、self rank2からP=(1,0,0,α,0),V=(u,v,1,−ωu/α,−ωv/α)。v非零はu0,v1。v0ならdomainからu非零,α²+ω非零でu1へ。v1の全値は以下で完成：
- n=a18非零：T非零、n=T1正規化、α−1/−ω/−ω²の三相。前二相はB3dim22。主相はY=y+(m+ω²)xの二変数(l,Z)モデル、正常41×7の7constantpivotsと4境界曲線/2fresh点で全排除。nonunit_proportional_open節/checker。
- n0は射影rank2なら商k<y,b>/(b²)指数増大。残りnT0,α−ωm²は13m値へ有限化し、正常x固有値/因子/実skew-cone頂点で全排除。nonunit_proportional_Tzero節/checker。
- n0,T非零はT1,α=m−ω²。4×4pureU行列の36minor GB11個、線型a1=(1+ω)a2,a5=ωa8,a6=(1+ω)a8。A=a0,B=a2,D=a4,C=a8,E=a15,W=B+ωD−2ωでW非零はpurec²/domain外。W0はB=ω(2−D),AC=ω²(2−D)(1−D),AE=−ω(2−D)C,C²=ωE(D−1)。純Uの選択行Qdet=1−DだがQ=0を捨てず、D1,A0,C0,E1を別fresh点へ（B3dim22）。A非零はweights(A,C,E)=(-1,1,2)でA1のD一変数へ、D1はこのA1族では純x²、正常38×7の7constantpivots、bad=(D−1)(D−2)、D2はB4dim36。A0,D2はC1/0二点、前者正常7核零、後者B4dim36。これでv1全体完成。nonunit_isolated節/checker。
最新主原稿v273 LuaLaTeX clean PASS。新checkersは全てdefault Sympy PASS、共有model変更後にprevious proportional_openも再PASS。累計56validators across runs（既存36統合再生と20後続個別）、単一56全再生未実行。新規as4/外部入力なし。

### 現在の未解決：比例v0と零b²結合
最優先はv0,u1のself xc+αcx,b²+xc−(ω/α)cx、α非零,α²+ω非零。元coはa13=1,a9=−αω²,a11=2,a3=1/α−ω²α、a12=a14=a7=a16=a17=a19=a200,a10=m,a18=n,a21=T。Mはprivate nonunit_prop_v0_unitlinear.py等に再構成済み。まだこの層を全排除していない。
private確認済みの次の小課題：nT両非零はn=T1へ正規化。最初8homdetはv1と同じα三相を強制。α−1/−ωのpolynomial unit消去は残余が非零定数なので不可能。α−ω²相は7unitpivots/freea15、rhs零でhomogeneous kernel。Y=y+(m+ω²)x後の候補モデルはxc=ω²cx,b²+2xc=0,bY=ω²Yb,Yb−ω²xb−bx−c²=0,bc+ZY²=0,cb+ω²ZY²=0のはず。これを元画像で監査する。domainならxc=-b²/2とcb=ω²bcの結合則から(xb−ωbx)c=0、従ってxb=ωbx。この二次式が表示I2にないことをunit matrixで確認すれば全モデル非整域となる。未統合。
n非零,T0はrowcc purex²からα²=ω。α正ω²はhomdet非零/P0でdomain外、主相α−ω²ではfirst8homogeneous rank6（T1のrank7と混同しない）、二つのfree cube係数が残る。private nonunit_prop_v0_T0_unitlinear.pyで確認。T0相をT1の1parameter modelへ勝手に代入しない。
n0でbc/cb射影rank2なら前と同じ指数商で非AS4。rank1残余はα=−ωm²,n0かつT(m+ω²)=0。T0ならrowcc purex²のdomain条件からα²=ω、従ってm4=ω²の4点。rowcc0なのでI1は純Ub+bU、domainからb正常onU、かつbx=mxb。b²=(α+ω/α)cxとxc=-αcxからbb²=b²bを使えばbc=m^-1cbでbが全Bに正常となる。正常正則bの商S=B/bはHS(1−t)^-3だが、xc=cx0を含み、二つの独立なcubic overlaps xcx/cxcによりdimS3≥11（HSは10）となる見込み。一次正規商AS3domain定理を新規輸入せず、このHilbert矛盾を検証・証明する。
T非零のn0,α=m−ω²ではbase cb=ω²bc,b²+2xcとxcω²cxから再びxb=ωbxをdomainが強制。I1 pureUb部分は1次元なのでその式が入るならyb/by成分が全零となり指数商、入らなければ非整域。全source像で監査して正式化する。
両結合零p=r0は別領域：H0はUc+cUの二関係だけ、domainなら両射影が同型でcがU上の正常元になる。Mとbc/cbの連結、正常三次7核と全H3条件は未判定。次は上のv0の小さい三境界から継続する。
