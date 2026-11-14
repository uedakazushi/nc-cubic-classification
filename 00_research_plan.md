# 研究方針：非可換三次超曲面の内在的モジュライ

2026-11-14 / v7。再開時は本書、AGENTS.md、notes/research_notes.md、現行論文の順に読む。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。目標や論文構成を変更する際は、その理由と解決済み／未解決の核心を現行の方針として整理し、変更履歴は蓄積しない。

証明の記載、今回の証明検証、計算確認、外部結果に条件付けられた結論、未完成、予想を区別する。仮定・依存先・証明箇所を明記し、誤りの影響は本文・要約・方針まで訂正する。新規性・外部優先権の確認は証明の正否と別問題である。

先行研究は一次資料で確認し、適用範囲をIntroductionで比較する。書誌を推測しない。公表価値のある結果は日本語LuaLaTeXで十分な証明とともに保持し、研究ノートは現在有効な着想・障害・計算・反例を整理する。論文の全証明をノートに重複させない。

研究継続用の一式はこのリポジトリ自身とし、現在の方針・ノート・原稿・必要なコードと小さな証明書から自己完結的に再開できるようにする。過去のZIP・中間生成物・大量の外部資料を追加しない。軽量化のために有効な数学や再現資産を削らない。

継続保存の既存許可に従い、研究の区切りで承諾を求めずGitHub mainへ通常のfast-forward pushを行い遠隔先端を確認する。GitHubを正本とし、Libraryは実際のpush失敗時の緊急退避に限る。既存Library資産を無断削除しない。GitHub Actions、force push、不要なPRは使用しない。PDF・SyncTeX・ログはbuild/へ出力し追跡しない。生成、数学的確認、有限検算、組版、遠隔保存の状態を別々に報告する。

## II. 現在の目標とモジュライの規約

非可換cubicと非可換射影空間の二つのモジュライを定義し、二次包絡による比較射の像・ファイバー・成分性を調べる。まずn=3、ambientは標準5次元Koszul AS正則Z-algebraとする。数値的な族の構成だけでなく、何を対象とし、どの同値関係で割るかを研究の中心に置く。

最初の対象は、Hilbert ranks b_m=binom(m+4,4)の相対二次Z-algebra Bと、h_m=b_m-b_(m-3)の三次商Aである。各成分の局所自由性、幾何学的ファイバーの左右AS・noetherian条件、三次核の左右正則性を定義に含める。AからQ(A)を構成し、Phi:C_3^seq→P_4^ASを得る。両者はfpqc stackとして定義済みだが、全体の有限型代数性は未証明。

圏の表示には豊富列(C,(E_i))を用いる。全E_iの同定を保持するlevel、同定を弱めた2-stack、E_0だけ同定するpointed 1-stackを区別する。圏との比較には低次数までのsaturation、相対Homの基底変換、相対復元を仮定する。対象列すべてを忘れたAbel圏のモジュライは別問題。さらに次数付き表示は1周期構造を選んだデータであり、中心性はその表示に依存する。

滑らかなnc三様体にはsmooth properなdg enhancementの条件を加える。正規正則商・平坦性・AS ambientだけからtailsの滑らかさを結論しない。

## III. 現在の到達点と証明の所在

### A. 定義と比較射

- `papers/sections/intrinsic_cubic_reconstruction.tex`：二次合成核による一意復元。任意の底変更との可換性、三次核直線束による正規イデアルの相対認識。
- `papers/sections/algebraic_moduli_foundations.tex`：二つのfpqc stackを定義。全代数stackは有限窓の有限型商stackの2逆極限。固定ambientの厳密2-fiberは正規三次incidence集合層であり、有限窓の準射影schemeの逆極限として表す。接空間は添字を保つHom_(B-B)(I,B/I)。可換ambientの全ファイバーは非被約基底も含めP34、pointed categorical levelでの中立BPGL5上の底変更は[P34/PGL5]。
- `papers/sections/categorical_moduli_comparison.tex`：全同定付き圏の比較、頂点スカラーのcrossed module、pointed商、相対線束A^L_ij=L_i A_ij L_j^(-1)を定義・証明。Q(A^L)=Q(A)^Lにより復元と比較射がすべてのlevelへ降りる。一般の相対category再構成そのものは仮定。

### B. 周期忘却と一般ファイバー

- `papers/sections/ambient_periodicity.tex`：明記した左右AS条件の下で、正規次数d族を持つ対(B,I)の周期はgcd(N,d)を割る。有限頂点orbitの中心元をNakayamaが固定することを使用。N=5,d=3では対・商とも1周期化可能。体上の存在を証明したが、族での降下・一意性を結論しない。
- `papers/sections/period_forgetting_moduli.tex`：周期忘却の厳密fiberはPer_1(B)、固定同型類では共役商。二因子stabilizer H_Rの両射影が単射なら、スカラー以外のZ自己同型を有限型群K_Rへ還元する。PBW族の二つの中心一次変数がこの単射性を与える。
- 新しい150×50整数行列は二因子stabilizerのLie代数を計算する。二つのスカラー核を整数上で確認し、48次minor mod1000003=815096により階数48を証明した。一般H_Rは有限となり、既存13/17次元の有理商におけるZ同型による追加同一視は有限個である。有限群の位数や忘却射の次数は未計算。
- 同じ一般点では、次数付きambientの任意のArtin変形上で全Z正規三次族が一つの中心三次直線の繰返しになる。固定ambientの全normal incidenceの形式fiberはk[[t1,t2,t3,t4]]。従来の「central部分のP4」に限らない局所結論である。一般のZ ambient変形の相対周期化を証明したものではない。
- 相対Koszul双対の有限自由Frobenius構造とNakayama比較を仮定すれば、一般点のNakayamaはArtin変形でも恒等。これら相対仮定の自動成立は未証明。

### C. 可換点の形式モジュライと成分

- `papers/sections/formal_ambient_comparison.tex`：P4の有限Beilinson窓にHom(O,O(1))の射影基底を指定した形式sliceを構成。De Deken–Lowen、Lowen、Yekutieli、Pymとminimal hullの一意性を用い、実際のQmod写像が規格化CY芽と射影基底付きAbel/Z変形関手を全Artin基底上で同定する。基底を忘れるとPGL5_1による商となる。接空間126だけからの推論ではない。
- `papers/sections/central_pair_generic_component.tex`：poisson-p4の三次一意延長・4次元fiberを照合。全Poisson微分375×150とJacobian源150×37の整数積零、非零113次・37次minorによりRat113錐が一般点で正則な37次元成分であると証明。全147分類は入力にしない。
- 新しい形式比較により、この37次元成分は実際の射影基底付きAbel/Z形式モジュライの成分でもある。支配的中心incidenceを可換ambient上の全fiberに沿って完備化した像の形式閉包はこの成分全体で、そこで余次元0。単一の指定三次Fの完備化が同じ意味で支配するとは主張しない。
- 一般中心はk[a,b,c], degrees(1,1,3)。incidence41、ambient37、PGL一般有理商17/13、ambientへの一般fiber4。GL商stackは共通Gm慣性により16/12。可換cubicへの忘却fiber7とは別の射。
- `papers/sections/central_pair_artin_formal_moduli.tex`：明記した同次formality入力の下で、滑らかな可換三次の関手は10個の可換変形変数と10個のPluecker変数・5方程式の完備局所環で表され、次元17・接空間20。実際のambient射の可換点での接写像は(dot F,a)↦Pi(F,a)、核10・像10。異なる量子化座標を選んだときの全高次での式の一致は未確認。

### D. 保持する成果・文献範囲

17係数sliceと31次minor、分離型余次元15、可換cubic忘却核7=6+1、全混合中心、相対Picard障害、偶数Veronese、条件付き導来復元、固定剛体ambientの4係数族と有限位数境界を現行論文に保持する。旧成果を現在の論文から削除していないが、全文の独立全面監査は未完了。

poisson-p4参照点はf118dfbfc5bb9b7a394d1985b4800b6228eebaf6（現行mainと再照合）。nc-cubicの二次包絡、asz4の周期構造の区別について従前の参照点もvalidation.jsonに保持する。必要な証明は本稿に収録し、他研究・大量証明書を複製しない。新しい比較定理・剛性・証明書の新規性と初出は未確認。

## IV. 未解決の核心と優先課題

1. **一般非可換点での有限型局所模型。** 可換点の全Artin比較は解決した。次は一般H_R有限点で、相対AS/Koszul–Frobenius構造と有限Beilinson/helix模型を照合する。有限窓から全Z代数への相対再構成とその基底変換を証明し、13次元像の成分性を大域モジュライへ移す。無限条件の逆極限を有限型性と呼ばない。
2. **相対周期化と降下。** 体上のgcd周期性は解決。相対直線束を含むorbit構成、相対Nakayama双加群、周期選択のtorsor/gerbeを記述する。一般族では追加同一視が有限でも、族の周期構造の存在や降下が自動とは限らない。有限群K_Rと捩れ共役の具体的計算も行う。
3. **滑らかな三次部分の支配性。** 正規三次モジュライでの形式的成分支配と、smooth properな三次圏の部分が支配することを区別する。相対対角双加群のperfect性または具体的dg模型を構成し、可換smooth fiberからの開性を示す。固定ambientでの有限位数仮定付きBertiniを全ambientへ無条件に運ばない。
4. **形式比較の高次互換性。** 実際の射はQ(A)で定義済み。独立に選んだ射影・affine formality同定の下で、全高次の式が(F_R,a)↦Pi(F_R,a)と一致するか、Casimir商と局所化の自然性を検証する。一次式と全高次式を区別する。
5. **豊富列を忘れたintrinsic性。** AOUのAS3での内部的O(n)認識を比較し、AS5/cubicで必要なrank・Euler形式・Serre条件を探す。現状の定義は列を備えた圏のモジュライであり、裸のAbel圏やKuznetsov成分のモジュライではない。
6. **一般n。** N=n+2、h(t)=(1-t^3)/(1-t)^N、周期上界gcd(N,3)と有限窓/incidenceの構成は共通骨格。n=4では3周期が残り得るため、n=3の1周期結論をそのまま使わない。

## V. 再開・再現・達成基準

README.mdのコマンドで再現する。今回の新しい証明書は`python3 computations/verify_two_factor_stabilizer.py`、成分証明書は`python3 computations/verify_rat113_tangent.py`。`scripts/verify.py`は参照閉包、`latexmk`は組版の検証であり、数学的証明検証とは区別する。

現行原稿には仮定・証明・依存先を収録する。作成・検算・組版・独立監査・遠隔保存の実施範囲をvalidation.jsonに記し、GitHub mainへの保存と遠隔SHA確認をもって区切りとする。全大域モジュライの分類を達成したとは報告しない。
