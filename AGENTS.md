# Codex実行指示

2026-11-14 / v7。最初に00_research_plan.md、次にnotes/research_notes.md、現行論文を読む。公開研究プロジェクトであり、研究継続用の自己完結した一式として維持する。

## 研究の優先順位

非可換cubic n-foldのintrinsicな定義、ambientへのモジュライ射と像を研究する。まずn=3。豊富列付きAbel圏、一般Z-algebra、周期同型付きZ-algebra、次数付き代数、中心三次対、滑らかなtailsを持つ対象を区別する。

厳密なZ-algebra stack、全同定付き圏、弱い2-stack、E_0だけ同定するpointed stackを区別する。全対象は有限窓の商stackの2逆極限で定義済み。Phi:A↦Q(A)の厳密fiberは正規三次incidence集合層であり、固定同型類のaction groupoidとそのfpqc stack化を区別する。相対category比較にはsaturation・Hom基底変換・相対復元を仮定する。

体上の三次イデアルを保つ1周期性は証明済み。一般族では二因子stabilizerの150×50整数行列がrank48（非零minor mod1000003=815096）なので、Zhang twistによる追加同一視は有限個。一般の中心三次点では全indexed normal incidenceの形式fiberも4次元形式円板である。ただし任意のZ ambient族の相対周期化は未証明。

可換P4点では有限Beilinson窓・射影基底・minimal hullの一意性により、実際のQmod写像による規格化CYとAbel/Zの全Artin比較を証明した。基底を忘れると形式PGL5作用が必要。接空間126だけから同定したと要約しない。37次元成分と全特殊fiberに沿う完備incidenceの余次元0は、この実際の形式模型へ移る。全大域モジュライの有限型性・成分性、一般非可換点での同じ比較、smooth proper三次部分の支配性は別の未解決課題。

Rat113の37次元成分の一般正則性には整数線型代数証明書がある。poisson-p4の全147分類を前提にしない。中心対41・ambient37、PGL商17・13、ambient忘却4、可換cubic忘却7を混同しない。可換点の接写像の核10・像10も一般fiber4とは異なる。GL商のGm安定化群を明示する。独立なformality座標の全高次での互換性は未確認。

## 正確性と保存

証明・追加仮定・既知入力・新規性・有限検算・未証明事項を区別する。一次資料の適用範囲を確認し、未確認を無条件入力へ昇格させない。有限体の非零minorは特性零の非零証明に使えるが、有限体の零は恒等式の証明にならない。修正時は依存する本文・要約・方針を整合させる。

数学的重要性に応じて計画・論文構成を柔軟に改善し、有効な証明・反例・必要な再現資産を削らない。研究ノートは作業日誌にしない。認証情報・第三者非公開資料・他研究の不要な内部資料を公開しない。

日本語LuaLaTeX、現行.latexmkrc、build/非追跡を使用する。最新mainから通常のfast-forward pushを行い遠隔HEADを確認する。継続保存は既に許可されている。GitHubを正本とし、Libraryは実際のpush失敗時のみ緊急退避に用いる。Actions・force push・旧ZIP・不要なPRなし。参照するnc-cubic A/B、nc-cubic2、poisson-p4、asz4の正本はこのタスクでは変更しない。
