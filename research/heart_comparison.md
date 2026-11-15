# 非可換del Pezzo曲面のheart比較：現行研究ノート

2026-11-15 / hearts-v1。最初に `00_research_plan.md` を読む。証明本文は `papers/nc_del_pezzo_hearts.tex`。対象は全次数の非可換del Pezzo曲面、最初の実行対象はcubic surface（次数3）。

## 目標・達成基準

Rainsの幾何学的heart、Van den Berghのraw blow-up heart、Okawa–UedaのAS helix heart、反標準環のqgrを比較する。四ラベルを四つの相異なるheartと仮定しない。まず同じ入力データの対応と導来同値を指定し、その後にheartをtransportする。存在、realization Db(heart)→Tの同値、t-exactness、構造対象、反Serre作用、境界restriction、rank、marking、族の降下をそれぞれ判定する。

cubicでの第一達成基準は、Van den Berghの最後のsection-model移行のtorsion pairを実在対象で記述し、AS–反標準比較のt-exactnessを証明するか、非一致を示す実在対象を与えること。数値的一致だけをもってheartの一致とはしない。

## 一次資料が与える比較図

VdBの記号では X_j ←α_j− tilde X_j −δ_j→ X_(j+1)。αはblow-up、δはsection-algebraモデルへの比較。σp_iが指定の平面埋込みに関して一般位置なら、Theorem 11.1.3はRδ_*とLδ*の逆同値と、heart上の振幅[0,1]および[-1,0]を与える。coherent bounded部分の保存はLemma 9.1.5も使用する。cubicのX_7=Proj Fである。

Chapter 12のF=P/(C_3)表示はTheorem 11.1.3の一般位置条件なしでも構成される。従って表示が存在する全点で導来同値を使ってはいけない。Remark 12.0.5は、raw blow-upを反復することと、各段階でsectionモデルに取り替えることの差を明記する。

AOU arXiv:2404.00175 §9は最初からcoh tilde X=qgr Fと定義する。滑らかな楕円曲線、次数3の線束、無限位数σ、sufficiently generalな六点という設定で、Lemma 9.2はSerre=(-1)[2]、Theorem 9.4はDb qgr F≃Db qgr Aを与える。したがって左辺をraw blow-up heartと呼び替えない。この定理はabelian equivalenceを述べていない。

AOUの式(9.44)は可換の場合のmutation表示で、その直後に非可換collectionを同じ記号で定義し直す。実際のmutation後の先頭をE0とすると、同値はE0をO(0,0)へ送る。E0≃πFという構造対象の同定は実際の対象として追う。境界restrictionやK0が一致するだけでは足りない。

OU arXiv:2508.04986 Definition 1.1, §6はAS heartと標識を定義し、一般の幾何学的blow-up模型との導来比較を扱う。それを全パラメータでのheartの一致と読まない。Rains arXiv:1907.11301 Introduction, §4は、既存のabelian構成を使ってt-構造とそのrealizationを正当化する。任意の抽象gluingへのfaithful heart存在定理ではない。

## 今回証明した形式的帰結

1. **振幅1のHRS比較**（原稿§3）。F:Db(A)≃Db(B)、F(A)⊂D^[0,1](B)、G(B)⊂D^[-1,0](A)なら、T=ker H¹F、U=ker H⁰Fはtorsion pairで、G(B)=〈U[1],T〉。Fがt-exact iff U=0。VdBではT_j=ker R¹δ_j*、U_j=ker δ_j*。非零M∈U_jはRδ_j*M=(R¹δ_j*M)[−1]≠0となる。heartからの消失と導来的消失を区別できる。これは既知HRS理論の適用で、新規性は未確認。
2. **ample orbitの一意性**（§4）。faithfulな有界heart、τのheart保存、(e,τ)のAZ ampleness、全対象についての高次Extの一様なtail消滅を仮定すると、heartはHom(e,τ^n X[i])=0 (i≠0,n≫0)で一意に決まる。高次消滅をAZの二公理だけから無条件に導かない。
3. **固定対象のEuler障害**（§4）。上のheartの非零τ固定対象はχ(e,M)>0。別heartの実在τ固定対象でχ≤0なら二つのheartの非一致を検出する。周期rの場合は各residueの和の正性のみ。共鳴式から固定対象の存在を補わない。
4. **corner判定**（§5）。B,e,R=eBeの左右の必要有限性とnoetherian性の下で、自然なqgr B→qgr Rが同値 iff dim_k B/BeB<∞。AS helixのfoldingとBe/eBの有限生成性を確認した範囲でだけ適用する。有限次数の計算や同じHilbert級数だけでは全次数の有限次元性にならない。

これらの完全な証明は論文に置き、ここで重複しない。既知文献の全証明、新しい命題の外部独立査読、新規性の網羅調査は未実施。dP1原稿の強い反標準導来比較は本研究の入力にしていない。

## cubicの具体的着手

**P1：最後のVdB段階。** A=coh tilde X_6、B=qgr F、F=Rδ_6*についてker δ_6*を求める。対象Mの通常pushforwardとR¹pushforwardを個別に計算する。ker δ_*が非零なら一回のtiltが非自明である。導来同値の既知適用範囲を先に固定する。

**P2：AS–反標準。** AOUの九対象とmutationsを実際の複体として追う。先頭E0と構造対象πFの同定、反Serre周期、境界restrictionを確認する。次にT=⊕E_iからB_n=Hom(T,τ^nT)を作り、e=E0のcornerを調べる。folding、Be/eBの有限性、B/BeBの全次数判定を行う。別法として、指定構造対象のorbitのAZ条件と高次消滅を直接示す。

**P3：Rainsの幾何学的heart。** 同じ楕円データと六点に対し、各段階のraw blow-upとsection-model移行を比較する。六段のt-構造を無条件に一回のtiltや六回のtiltにまとめない。標識、σとσ³、構造対象の違いを追う。

**P4：共鳴・境界・他次数。** まずcubicで実在root対象を作り、上のtorsion pairやEuler障害と照合する。数値的non-ampleness、AZ失敗、heart変化、導来変化、qgrの特異性は別のlocusとして扱う。その後に有限位数・特異境界・非局所自由gluing、さらに次数1,2,4等へ拡張する。

## exactな初期検算

AOU (4.1)の9線束の数値類を使う。Pic(S)=Zl⊕⊕Ze_i、H=3l−Σe_i。Euler行列は三blockの上三角行列で、対角I3、隣接block J3、離れたblock 2J3。成分総和45、det=1。Serre行列C^−1 C^tの逆はHによるtwistと一致する。E6の72根とH²=3も確認する。

    python3 computations/verify_cubic_heart_numerics.py
    latexmk papers/nc_del_pezzo_hearts.tex

Python標準ライブラリの有理数計算のみ。反標準Euler値n=0..8は1,4,10,19,31,46,64,85,109。有限検算はeffective root、非可換strong性、heart比較の証明ではない。

## 文献位置・確認範囲

- Van den Bergh, *Blowing up of non-commutative smooth surfaces*, arXiv:math/9809116v1：Lemma 9.1.5、Definition 11.1.2、Theorem 11.1.3、Chapter 12、Remark 12.0.5。https://arxiv.org/abs/math/9809116
- Abdelgadir–Okawa–Ueda, *Compact moduli of marked noncommutative cubic surfaces*, arXiv:2404.00175v1：§4.1、§9冒頭、Lemma 9.2、Theorem 9.4、(9.44)直後、(9.54)–(9.57)。https://arxiv.org/abs/2404.00175
- Okawa–Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, arXiv:2508.04986v1：Definition 1.1、Definition 3.1、§6。https://arxiv.org/abs/2508.04986
- Rains, *The birational geometry of noncommutative surfaces*, arXiv:1907.11301v1：Introduction、§4冒頭、Lemma 5.7。https://arxiv.org/abs/1907.11301
- Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2：§4のeffective coneと共鳴。https://arxiv.org/abs/2107.13540
- Chen–Han–Zhou, *Derived equivalences via HRS-tilting*, Adv. Math.354(2019),106749、arXiv:1804.05629v2：Theorems A,B、§§2–3。https://arxiv.org/abs/1804.05629

一次PDFの抽出本文で上記の記述を確認した。OU、CHZでは関連ページ画像も確認。AOU、VdB、Rainsの画像取得はCache missで失敗し、抽出本文に基づく照合にとどまる。未確認の原文箇所を推測で補っていない。
