# 研究方針：非可換三次超曲面とambientのモジュライ

2026-11-14 / v9。再開時は本書、対象次元に応じた研究ノート、現行論文の順に読む。

## 恒常的な原則・保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性により目標を柔軟に最適化する。方針変更は現行方針として書き直し、作業履歴を蓄積しない。証明記載、今回の証明検討、有限計算、外部入力、予想、未完成、新規性確認を区別する。誤りの影響は関連する本文・要約・ノートへ反映する。

一次資料を確認して適用範囲を記す。公表価値のある数学と完全な証明は日本語LuaLaTeXで保持する。軽量化は履歴・重複・中間物の除去によって行い、数学的内容を削らない。ノートには有効な着想・反例・障害・再現上の制約を残す。

研究継続用bundleはこのGitHubリポジトリの現行ソース一式。区切りごとの承諾不要の保存許可があり、mainへ通常のfast-forwardで保存する。GitHubを正本とし、Libraryは実際のGitHub保存失敗時の緊急退避に限る。既存Libraryファイルを無断で削除しない。Actions、force push、不要なPR、旧ZIP、PDFのGit追跡は行わない。生成、検証、組版、遠隔保存を別々に確認する。

## 現在の対象と規約

目標は非可換cubic n-foldの内在的定義、二次包絡によるambient復元、モジュライ間の射、像の成分性とファイバーである。三次三様体(n=3)と三次曲面(n=2)を明確に分ける。ユーザーのsurface比較に対応してn=2の独立した短稿を置く。既存のn=3原稿をsurfaceの議論で置換しない。

厳密Z代数、周期構造付き代数、次数付き代数、豊富列付き圏、pointed圏、裸の導来圏を別のモジュライとして扱う。中心性は選んだ次数付き表示に依存し、正規性と同一ではない。GL商、PGL商、Poissonスカラーの射影化も区別する。

## 三次曲面：現在の結果と最優先課題

読む順序は `research/cubic_surface_comparison.md`、`papers/cubic_surface_ambient_moduli.tex`。日付・版はsurface-v1。

- 滑らかな三次曲面X=V(F)の全Poisson構造はh∈H0(O_X(1))であり、i_Pi Omega=dF∧dhでP3へ一意延長する。像はR(1,3)錐に稠密。一般ファイバーはF+c h^3のペンシルの開部分。Poissonスカラーを保持するとincidence23、ambient22、PGL4一般有理商8→7である。本文定理2.1、2.2。
- 全Jacobi・発散零微分96×60のrank38、源微分60×24のrank22と積零により、22次元錐の一般正則性を確認。軌道rank15、二因子stabilizerの60×32行列rank30も有理数上の非零minorで証明。コードと小証明書は `computations/verify_surface_incidence.py` と `computations/surface_incidence_certificate.json`。
- 量子側は二次包絡でambientを一意復元。PBW随伴S0[t]、低次数中心(0,0,1)、中心三次持上げという明記した仮定の下でZ(B)_3=k Omega+k t^3。中心三次fiberはP1。二因子stabilizer有限なら固定ambientの全indexed正規三次形式fiberもk[[s]]。全ncP3の大域分類ではない。
- CY正規化とsmooth proper・saturationの下でSerre=(-1)[2]、H=Serre^{-1}[2]=(1)。指定OとSerreから反標準環、次いでambientを復元できる。三次三様体の平方根問題はsurfaceには現れない。任意の正規商で無条件に同じSerre式を使わない。
- AOU(arXiv:2404.00175)のmarkedモジュライは既知の8次元toric GIT模型。9頂点3-CY potentialとambientの4頂点4-CY potentialは異なる。AOU Theorem9.4の導来同値を、heart・構造対象・相対Homを確認せず全域のambient射と読み替えない。

次の具体的着手は、AOU有限代数Lambdaの指定頂点P0からA_m=Hom(P0,(S_Lambda^{-1}[2])^m P0)のm=0,1,2,3,4を相対計算し、底変更と二次包絡のAS性を確認すること。良い開集合上の比較射とそのgeneric degreeを構成し、その後に境界・ample性・smooth proper性・marking忘却を調べる。8次元の一致だけで双有理性を結論しない。

## 三次三様体と射影空間：保持する研究

`notes/research_notes.md` と `papers/nc_cubic_threefold_moduli.tex` (v8) が現行の詳細を保持する。今回この原稿の全証明を再監査したわけではない。

主要な既存論点は、相対二次包絡と正規incidence、有限窓の逆極限によるfpqc stack、豊富列と頂点スカラーの比較、Frobenius周期によるpointed potential商、可換P3/P4のflattening形式模型、体上の対のgcd周期性、一般二因子stabilizerの有限性、可換P4の全Artin比較、Rat113の37次元錐と41次元中心対、13/17の一般有理商である。本文の各仮定とvalidation.jsonの実行範囲を参照し、これらを全大域分類と呼ばない。

n=3での次課題は、有限型AS chart、三次イデアルを保つ相対周期降下、smooth proper三次部分の支配性、formality座標の高次互換性、豊富列を忘れた内在性。n=4ではgcd(6,3)=3のため1周期性を前提にしない。新しいsurface結果はn=3の未解決箇所を解消するものではない。

## 再現と到達基準

surface稿は `latexmk papers/cubic_surface_ambient_moduli.tex`、計算は `python3 computations/verify_surface_incidence.py`。検証範囲は `research/surface_validation.json`。旧主原稿の再現方法はREADME.mdとvalidation.jsonを参照する。有限検算、組版、外部査読、形式検証を混同しない。必要ファイルと参照の整合を確認し、保存先のcommitを確認して一区切りとする。
