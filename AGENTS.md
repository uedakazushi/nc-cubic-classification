# 研究実行指示 — 2026-11-15 / project-v10

最初に `00_research_plan.md`、`research/cubic_surface_comparison.md`、surface論文とその唯一のinputを読む。現在の最優先はweakly marked非可換三次曲面と四頂点ambientのR(1,3)成分の比較である。既存の三次三様体原稿・必要な証明・計算は保持する。他repoはこのタスクでは変更しない。

## 数学的な区別

任意の4周期τを指定する関係式stackと非捩れpotential stackを同一視しない。非捩れpotentialはFrobenius適合周期を扱う。可換環のτにdiag(2,1,1,1)を合成する反例がある。GL4^4の4次元スカラー慣性とPGL4^4のrigidificationを揃えて比較する。内在的な曲面からのambient射はpointed targetに取る。

R13では明示quartic potential、7係数slice、全256方向でrank188/61/68のQQ証明書があり、67次元parameter成分の一般点は正則。PGL4^4商の有限型DM開部分は7次元。全境界のAS性・正規化・有限群oidの一般次数は未決定。一般点では二因子stabilizer有限性により任意周期の全Artin関係式変形も非捩れpotentialに規格化できる。

weakly markedは(A,O)、H=S^-1[2]の両方向t-exactness、所定Hilbert級数、AZ amplenessで定義し、族の平坦性・Hom底変更・相対Serreを明記する。全対象の次数一生成、二次包絡AS性、正則三次核は未証明。認識部分ではambient射がある。

AOUからのW(E6)商は一般可換点の形式近傍で証明している。大域商にはmarking存在、K0による一意性、全同型・降下が残る。形式同値から大域商を断定しない。AOUの一般blow-up表示とSerre公式を入力としてambientへの有理射はR13を支配し、一般fiberは1次元。AOUから中心三次対への有限次数をWeyl群の位数とは同定していない。固定ambientでは中心fiber=P1、全indexed normal形式fiber=Spf k[[s]]。全部のP1の点がsmooth properとはしない。

次は楕円データ上のWeyl reflectionとmarking認識、有限inverse Serreアルゴリズムの座標実装、内在的条件からの超曲面認識を進める。詳細な着手方法は研究方針にある。

## 検証と保存

証明記載・今回の検討・有限検算・外部入力・未証明・新規性を区別する。誤りは依存する本文・ノート・方針へ反映する。一次資料を確認し、有限rankだけで全次数AS性を結論しない。証明・反例・再現資産を削らず、履歴・重複・不要物だけを整理する。

日本語LuaLaTeX、build/非追跡。二つのsurface検算、静的チェック、組版・描画を手動で実行する。GitHub mainへの通常fast-forwardと遠隔確認、現行自己完結bundleのLibrary保存は常設許可に基づいて行う。既存Libraryファイルは無断削除しない。Actions、force push、不要なPR、旧版ZIPの内包は行わない。生成・検証・GitHub・Libraryの状態を分け、実際に成功したことだけを報告する。
