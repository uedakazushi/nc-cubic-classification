# 研究方針：非可換三次超曲面の内在的モジュライ

2026-11-14 / v8。再開時は本書、AGENTS.md、notes/research_notes.md、現行論文の順に読む。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。目標や論文構成を変更する際は、その理由と解決済み／未解決の核心を現行の方針として整理し、変更履歴は蓄積しない。

証明の記載、今回の証明検証、計算確認、外部結果に条件付けられた結論、未完成、予想を区別する。仮定・依存先・証明箇所を明記し、誤りの影響は本文・要約・方針まで訂正する。新規性・外部優先権の確認は証明の正否と別問題である。

先行研究は一次資料で確認し、適用範囲をIntroductionで比較する。書誌を推測しない。公表価値のある結果は日本語LuaLaTeXで十分な証明とともに保持し、研究ノートは現在有効な着想・障害・計算・反例を整理する。論文の全証明をノートに重複させない。

研究継続用の一式はこのリポジトリ自身とし、現在の方針・ノート・原稿・必要なコードと小さな証明書から自己完結的に再開できるようにする。過去のZIP・中間生成物・大量の外部資料を追加しない。軽量化のために有効な数学や再現資産を削らない。

継続保存の既存許可に従い、研究の区切りで承諾を求めずGitHub mainへ通常のfast-forward pushを行い遠隔先端を確認する。GitHubを正本とし、Libraryは実際のpush失敗時の緊急退避に限る。既存Library資産を無断削除しない。GitHub Actions、force push、不要なPRは使用しない。PDF・SyncTeX・ログはbuild/へ出力し追跡しない。生成、数学的確認、有限検算、組版、遠隔保存の状態を別々に報告する。

## II. 現在の目標とモジュライの規約

非可換cubicと非可換射影空間の二つのモジュライを定義し、二次包絡による比較射の像・ファイバー・成分性を調べる。まずn=3、ambientは標準5次元Koszul AS正則Z-algebraとする。数値的な族の構成だけでなく、何を対象とし、どの同値関係で割るかを研究の中心に置く。

非可換P3を比較対象とし、4周期性を使った四頂点superpotentialの商表示を構成する。この有限tensor模型で、周期選択・頂点スカラー・全次数のAS条件を分離する。三次三様体そのものは5次元ambientの正規三次商として扱い、ambient P4のpotentialと正規三次incidenceを結ぶ。元の目標である三次→P4の復元射と像の研究を維持し、P3で得た相対・形式局所の方法をambient側へ展開する。

最初の対象は、Hilbert ranks b_m=binom(m+4,4)の相対二次Z-algebra Bと、h_m=b_m-b_(m-3)の三次商Aである。各成分の局所自由性、幾何学的ファイバーの左右AS・noetherian条件、三次核の左右正則性を定義に含める。AからQ(A)を構成し、Phi:C_3^seq→P_4^ASを得る。両者はfpqc stackとして定義済みだが、全体の有限型代数性は未証明。

圏の表示には豊富列(C,(E_i))を用いる。全E_iの同定を保持するlevel、同定を弱めた2-stack、E_0だけ同定するpointed 1-stackを区別する。圏との比較には低次数までのsaturation、相対Homの基底変換、相対復元を仮定する。対象列すべてを忘れたAbel圏のモジュライは別問題。さらに次数付き表示は1周期構造を選んだデータであり、中心性はその表示に依存する。

滑らかなnc三様体にはsmooth properなdg enhancementの条件を加える。正規正則商・平坦性・AS ambientだけからtailsの滑らかさを結論しない。

## III. 現在の到達点と証明の所在

### A. 定義と比較射

- `papers/sections/intrinsic_cubic_reconstruction.tex`：二次合成核による一意復元。任意の底変更との可換性、三次核直線束による正規イデアルの相対認識。
- `papers/sections/algebraic_moduli_foundations.tex`：二つのfpqc stackを定義。全代数stackは有限窓の有限型商stackの2逆極限。固定ambientの厳密2-fiberは正規三次incidence集合層であり、有限窓の準射影schemeの逆極限として表す。接空間は添字を保つHom_(B-B)(I,B/I)。可換ambientの全ファイバーは非被約基底も含めP34、pointed categorical levelでの中立BPGL5上の底変更は[P34/PGL5]。
- `papers/sections/categorical_moduli_comparison.tex`：全同定付き圏の比較、頂点スカラーのcrossed module、pointed商、相対線束A^L_ij=L_i A_ij L_j^(-1)を定義・証明。Q(A^L)=Q(A)^Lにより復元と比較射がすべてのlevelへ降りる。一般の相対category再構成そのものは仮定。

### B. 非可換P3のpotentialモジュライ

- `papers/sections/projective_three_space_potentials.tex`：標準14641型の二次Koszul・左右AS正則Z代数を対象とする。Frobenius周期で畳み込むと4-CYとなり、w∈V0⊗V1⊗V2⊗V3からW=w−cw+c²w−c³wを作る。二階の経路微分が二次関係を与える。体上の周期規格化はasz4の既存議論を確認・再掲し、通常の対称traceに頂点符号を入れてgraded対称性を得る。
- 同節の相対bar補題は、全成分が有限局所自由で標準ASの幾何学的ファイバーを持つ族について、二次双対の局所自由性・任意の底変更・完全Frobenius対合を証明する。N次元にも同じ証明が通る。
- 許容potential関手U4^AS⊂P255を定義し、[U4^AS/PGL4^4]≃P3^ptをfpqc stackとして証明した。相対traceの同時fpqc自明化、頂点スカラーによる周期補正、PGL torsorの降下を含む。strict Z-stackとの同値でも、U4^ASの有限型schemeとしての構成でもない。
- 同じ証明から、標準N次元のpointed stackは[U_N^AS/PGL_N^N]となる。N=5では係数空間P3124、符号なし五次potential、三階微分の二次関係rank10。ambient P4にもこの商表示を得た。可換点の形式模型は五つの25×125 flatteningのrank10条件で与える。normal三次イデアルを保つ周期降下はこの帰結に含めない。
- 可換交代テンソルでのrank6 locus Z6の完備化は全Artin potential変形を表す。内部次数帰納法で全次数のflatnessとKoszul解消を証明する。二つのflatteningの線型化条件rank165、射影接空間90、射影軌道45、商の接空間45。有理数上の計算は`verify_p3_potentials.py`と`p3_potential_certificate.json`。
- `papers/sections/cubic_projective_three_comparison.tex`：三次商はinjdim4・index2のAS Gorensteinでgldim∞。可換smooth cubicのHH±1=k5は通常のtilting代数への障害となる。ambientの五次potential＋normal三次直線が三次側の有限表示候補であり、一般族でのイデアルを保つ周期降下は別問題。

### C. 周期忘却と一般ファイバー

- `papers/sections/ambient_periodicity.tex`：明記した左右AS条件の下で、正規次数d族を持つ対(B,I)の周期はgcd(N,d)を割る。有限頂点orbitの中心元をNakayamaが固定することを使用。N=5,d=3では対・商とも1周期化可能。体上の存在を証明したが、族での降下・一意性を結論しない。
- `papers/sections/period_forgetting_moduli.tex`：周期忘却の厳密fiberはPer_1(B)、固定同型類では共役商。二因子stabilizer H_Rの両射影が単射なら、スカラー以外のZ自己同型を有限型群K_Rへ還元する。PBW族の二つの中心一次変数がこの単射性を与える。
- 新しい150×50整数行列は二因子stabilizerのLie代数を計算する。二つのスカラー核を整数上で確認し、48次minor mod1000003=815096により階数48を証明した。一般H_Rは有限となり、既存13/17次元の有理商におけるZ同型による追加同一視は有限個である。有限群の位数や忘却射の次数は未計算。
- 同じ一般点では、次数付きambientの任意のArtin変形上で全Z正規三次族が一つの中心三次直線の繰返しになる。固定ambientの全normal incidenceの形式fiberはk[[t1,t2,t3,t4]]。従来の「central部分のP4」に限らない局所結論である。一般のZ ambient変形の相対周期化を証明したものではない。
- 相対Koszul双対の有限自由Frobenius構造は全成分の局所自由性から相対bar補題で得る。相対双加群複体によるNakayama構成と双対比較を仮定すれば、一般点のNakayamaはArtin変形でも恒等。後者の具体的比較は明示的な入力として残す。

### D. 可換点の形式モジュライと成分

- `papers/sections/formal_ambient_comparison.tex`：P4の有限Beilinson窓にHom(O,O(1))の射影基底を指定した形式sliceを構成。De Deken–Lowen、Lowen、Yekutieli、Pymとminimal hullの一意性を用い、実際のQmod写像が規格化CY芽と射影基底付きAbel/Z変形関手を全Artin基底上で同定する。基底を忘れるとPGL5_1による商となる。接空間126だけからの推論ではない。
- `papers/sections/central_pair_generic_component.tex`：poisson-p4の三次一意延長・4次元fiberを照合。全Poisson微分375×150とJacobian源150×37の整数積零、非零113次・37次minorによりRat113錐が一般点で正則な37次元成分であると証明。全147分類は入力にしない。
- 新しい形式比較により、この37次元成分は実際の射影基底付きAbel/Z形式モジュライの成分でもある。支配的中心incidenceを可換ambient上の全fiberに沿って完備化した像の形式閉包はこの成分全体で、そこで余次元0。単一の指定三次Fの完備化が同じ意味で支配するとは主張しない。
- 一般中心はk[a,b,c], degrees(1,1,3)。incidence41、ambient37、PGL一般有理商17/13、ambientへの一般fiber4。GL商stackは共通Gm慣性により16/12。可換cubicへの忘却fiber7とは別の射。
- `papers/sections/central_pair_artin_formal_moduli.tex`：明記した同次formality入力の下で、滑らかな可換三次の関手は10個の可換変形変数と10個のPluecker変数・5方程式の完備局所環で表され、次元17・接空間20。実際のambient射の可換点での接写像は(dot F,a)↦Pi(F,a)、核10・像10。異なる量子化座標を選んだときの全高次での式の一致は未確認。

### E. 保持する成果・文献範囲

17係数sliceと31次minor、分離型余次元15、可換cubic忘却核7=6+1、全混合中心、相対Picard障害、偶数Veronese、条件付き導来復元、固定剛体ambientの4係数族と有限位数境界を現行論文に保持する。旧成果を現在の論文から削除していないが、全文の独立全面監査は未完了。

poisson-p4参照点はf118dfbfc5bb9b7a394d1985b4800b6228eebaf6、asz4は91b45047739187fc5acb6f906b25e48f49a42c2d。nc-cubicの二次包絡の参照点もvalidation.jsonに保持する。BSWの符号・高階微分、Mori–NymanのAS/ASF条件、Pymの局所六成分、2025/2026年のFrobeniusモジュライ・離散不変量preprintを一次本文で比較した。後二者はgraded同型の問題であり、Koszul条件やZhang twistの同値関係が本稿と異なる。必要な証明は本稿に収録し、外部PDFを複製しない。新しい比較定理・局所rank模型・剛性・証明書の新規性と初出は未確認。

## IV. 未解決の核心と優先課題

1. **potentialの有限型局所模型と成分。** P3可換点ではZ6の完備局所環まで得た。次は二つのrank6条件の既約枝をPymの局所六族と比較し、AS条件を有限次数で判定できるPBW/Gröbner chartを作る。一般H_R有限なP4点では相対Frobenius構造と有限helix模型を結び、13次元像の大域成分性へ進む。有限係数表示や全Artin比較を、そのままAS locus全体の有限型性とは呼ばない。
2. **正規イデアルを保つ相対周期化。** P3のpointed stackではFrobenius周期とスカラーの降下を解決した。三次対については体上のgcd周期性があるが、相対直線束を含むorbit構成と、相対Nakayamaが正規族を保つことを検証する。ambientの五次potential上でnormal三次incidenceを五頂点の有限条件へ降ろすことが次の具体的目標である。有限群K_Rと捩れ共役の具体的計算も行う。
3. **滑らかな三次部分の支配性。** 正規三次モジュライでの形式的成分支配と、smooth properな三次圏の部分が支配することを区別する。相対対角双加群のperfect性または具体的dg模型を構成し、可換smooth fiberからの開性を示す。固定ambientでの有限位数仮定付きBertiniを全ambientへ無条件に運ばない。
4. **形式比較の高次互換性。** 実際の射はQ(A)で定義済み。独立に選んだ射影・affine formality同定の下で、全高次の式が(F_R,a)↦Pi(F_R,a)と一致するか、Casimir商と局所化の自然性を検証する。一次式と全高次式を区別する。
5. **豊富列を忘れたintrinsic性。** AOUのAS3での内部的O(n)認識を比較し、AS5/cubicで必要なrank・Euler形式・Serre条件を探す。現状の定義は列を備えた圏のモジュライであり、裸のAbel圏やKuznetsov成分のモジュライではない。
6. **一般n。** N=n+2、h(t)=(1-t^3)/(1-t)^N、周期上界gcd(N,3)と有限窓/incidenceの構成は共通骨格。n=4では3周期が残り得るため、n=3の1周期結論をそのまま使わない。

## V. 再開・再現・達成基準

README.mdのコマンドで再現する。P3の有限検算は`python3 computations/verify_p3_potentials.py`、周期忘却は`python3 computations/verify_two_factor_stabilizer.py`、成分証明書は`python3 computations/verify_rat113_tangent.py`。`scripts/verify.py`は参照閉包、`latexmk`は組版の検証であり、数学的証明検証とは区別する。

現行原稿には仮定・証明・依存先を収録する。作成・検算・組版・独立監査・遠隔保存の実施範囲をvalidation.jsonに記し、GitHub mainへの保存と遠隔SHA確認をもって区切りとする。全大域モジュライの分類を達成したとは報告しない。
