# 研究方針：非可換三次曲面と射影三空間のモジュライ

2026-11-15 / project-v10、surface-v2。最初に本書、次に `research/cubic_surface_comparison.md`、現行論文を読む。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化する。重要な変更では理由と達成済み／未解決の核心を現行方針として整理し、変更履歴を積み重ねない。

証明の記載、今回の検討、追加仮定への依存、計算証明書、未完成、予想、新規性確認を区別する。仮定と証明箇所を明示し、誤りの影響を本文・要約・方針にも反映する。一次資料の適用範囲を確認し、書誌情報を推測しない。公表原稿は日本語LuaLaTeXで、十分な証明を保つ。

研究継続用bundleは現行の方針・ノート・論文・再現用ソースと最小の証明書から自己完結させる。有効な数学や再現資産は削らず、履歴・旧ZIP・重複・中間生成物を除く。ノートは日誌でなく現在有効な知識を整理する。旧会話・旧版の取得を再開の前提にしない。

ユーザーの常設指示は、研究の区切りで承諾を求めず現行bundleをLibraryへ保存することを許可している。現行ソースはGitHub mainにも通常のfast-forwardで保存する。GitHubではPDF・ログ・キャッシュを追跡せず、Actions・force push・不要なPRを用いない。既存Library資産の削除は別の操作であり明示指示なしには行わない。生成、数学的検討、計算、組版、GitHub保存、Library保存は別々に確認し、失敗や未実行を明示する。

## II. 現在の目標と定義の範囲

最優先はn=2：weakly marked非可換三次曲面を(A,O)、H=S^{-1}[2]、AZ ampleness、反標準Hilbert級数で定義し、AOUのmarkedモジュライ、W(E6)、四頂点ambientのR(1,3)成分を比較する。n=3の既存研究は保持するが、surfaceとthreefoldの次元・周期・障害を混同しない。

任意に選ぶ4周期、Frobenius/CY適合周期、非捩れpotential、twisted potentialを区別する。GL4^4商の4次元スカラー慣性とPGL4^4によるrigidificationも別。Hilbert級数とAZ ampleだけで二次包絡のAS性を宣言しない。相対stackにはHom底変更、平坦heart、相対Serreとenhancementを指定する。

## III. 現在の到達点と証明の所在

現行論文は `papers/cubic_surface_ambient_moduli.tex`。主要新証明は `papers/sections/surface_stack_comparison.tex`。

1. 関係式stack=[R^AS/GL4^4]と、周期同型を指定したAS Z代数のstackは同値（命題2.1）。任意の周期を非捩れpotentialと同一視するのは誤りで、可換4変数環にdiag(2,1,1,1)を合成した周期が反例（命題2.2）。これはFrobenius適合周期についての既存定理を否定しない。
2. R13の四次potentialを Alt(txyz)-3(1-c+c^2-c^3)(t sym(F)) と明示。F=f3+tq2+t²l1 mod t³。七係数slice、全256テンソル方向でのrank条件微分rank188、GL4^4軌道rank61、slice+軌道rank68を厳密QQ計算。射影成分67次元、PGL4^4商7次元。滑らかな有限型DM開部分と七係数のエタールatlasを構成した（定理3.2）。全境界、正規化、有限群oidの一般次数は未計算。
3. 一般点の二因子stabilizer有限性から、任意周期付きAS関係式のArtin変形も非捩れpotentialへ規格化できる（命題3.3）。大域的に任意周期と適合周期が同じとはしない。
4. 内在的反標準環Γ_acとAZ再構成を定義。次数一生成、Q(Γ)標準AS4、正則三次核という超曲面認識部分ではambient射Φが底変更に両立して存在する。全weakly marked対象がこの部分に入ることは未証明（第4節）。
5. 一般の滑らかな可換三次曲面の全Artin形式近傍では、例外対象の唯一持上げとDe Deken–Lowenのhelix比較を用いてAOUのmarked完備化と内在的変形を同定。通常markingのW(E6)-torsorから形式Weyl商を得る（定理5.1）。大域同定にはmarkingの存在、数値類による一意性、全同型と降下の三条件が残る（命題5.3）。
6. AOUの45次元有限代数Λ、P0、inverse Serre bimoduleからm=0..4のHomを有限複体として構成。可換点を含む開でrankは1,4,10,19,31。一般blow-up表示とSerre公式を既知入力としてambientへの有理射を得る。次数≤3が可換点の全8変形を検出するため、三次対への一般有理像は8次元、R13 ambient像は7次元で支配的、一般fiberは1次元（定理6.2）。一般次数をWeyl群の位数とは同定していない。
7. 固定一般ambientでは中心三次はP1、二因子stabilizer有限なら全indexed normal三次形式fiberもSpf k[[s]]。Poisson一意延長、ペンシル、22次元成分の一般正則性と既存証明を保持（第7–10節）。

本文の通常証明を今回検討し、指定した二つの計算を実行した。外部査読、Lean形式化、新規性の網羅的確認は別であり未実施。

## Directed P3 relationsとpotentialの位置づけ

P3のdirected Beilinson四頂点12矢は、二つのrank6二次関係R0,R1を持つ。K=(R0⊗V2)∩(V0⊗R1)がrank4で、Kの両縮約がrank6となる層上では、四次potential w=coev(K)を構成する。GL4^4で割った非射影化potentialの群oidとGL4^3で割ったdirected relationの群oidが同値。Koszul/AS条件は両側の共通代数に課し、全Gr(6,16)^2が適合するとはしない。P2のAOUの単純な「関係の双対を矢へ追加する」操作とは異なり、三次syzygyのrank層が必要。四次は二階微分であり、BSWの符号付きsuperpotentialとDWZの一階Jacobianを区別する。証明は threefold原稿の projective_three_space_potentials.tex、現在有効な記述と境界の課題は research/cubic_surface_comparison.md。GIT境界でKが跳ぶ場合のsyzygy incidence compactificationを次に調べる。

## R(1,3)既約成分の一般モジュライの決定（2026-11-15 / r13-v1）

証明の骨格・仮定・計算・残る境界問題は `research/r13_generic_moduli.md` に集約した。主結果は一般のSklyanin中心一次拡大型におけるpointed moduliの開部分
`[U_19/Aff_3]` （determinant-twisted作用、19−12=7次元）と、Hessian群 `G_216` の七係数正規形の有理商である。中心一次正規族が一意であることを楕円point schemeのtranslation (3p\ne0) から証明し、一般のZhang追加同一視を排除した。したがって七係数写像の一般次数は216。さらに `Hilb^8(A^3)` の特殊なcomplete intersection上の非零integrable 1-formのモジュライと同定する。八つの臨界点・中心変形の線型条件・integrability rank8・216群の有限列挙は新しい独立QQ検算を実施。四頂点rank188と67次元成分性は既存の証明書を入力とし、この回には再実行していない。

この結果は**一般開部分の分類**であり、既約成分の全境界のscheme構造、正規化、GIT半安定商、特異なSklyanin境界、3-torsionでのZhang同一視、有限群の不変関数体の最小生成元は未解決である。今後はこの境界と不変量計算を最優先にする。独立査読と新規性の総合確認も未了。

## IV. 次に着手する課題

最優先はW(E6)商の大域化である。定理5.1を単に代数化しただけでは、別のmarkingや自己同値による追加同一視を排除できない。AOUの楕円decuple上でsimple reflectionの有理変換を構成し、P0、Serre orbit、heart、ample locusの保存を証明する。K0上同じmarkingを持つ例外列の一意性が核心。2024年OWRのaffine Weylに関する予想と、有限W(E6)へ制限するための条件を照合する。

次に、式(6)のfinite Serre algorithmをAOUの八つのトーラス座標で実装し、A1、R2、三次核の実際の有理式を出す。これにより七係数sliceへの写像、一般次数、Weyl作用との可換性を検査する。現在は有限アルゴリズムと支配性の証明があり、展開済み座標式はない。

並行して、内在的条件から超曲面認識を導く。可換形式近傍と幾何学的一般点では比較できるが、全成分・全境界の次数一生成／AS cover／正則三次核は残る。smooth proper性・AZ amplenessの相対開性を別に検査する。

R13の七係数atlasの有限群oidを解き、generic stabilizer、一般次数、不変関数体、成分の正規化を求める。rank6 locus全体をAS locusと同一視しない。任意周期の別成分をFrobenius sliceで落とさない。

## V. 保持する三次三様体研究

`papers/nc_cubic_threefold_moduli.tex` (v8)、`notes/research_notes.md` と既存の必要コードは引き続き現行資料であり、今回削除・置換しない。相対二次包絡、37/41次元incidence、13/17次元一般有理商、体上の対の周期性、可換P4形式比較、四・五頂点potentialについての詳細がそこにある。今回その102ページ全体は再監査していない。任意周期と適合周期については本書の訂正された区別を用いる。

## VI. 再現

`research/cubic_surface_reproduce.md` のコマンドで二つのQQ計算とLuaLaTeX組版を再現する。証明書のrank、minor、行列の行列番号、参照閉包、PDFを確認する。`research/surface_validation.json` は今回実行した範囲のみを記録する。Library用surface bundleはこのsurface研究の全ソース・論文PDF・計算・方針・ノートを含み、別のthreefold論文を再開の前提にしない。
