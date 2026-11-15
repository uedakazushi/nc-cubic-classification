# Rains resonance と anticanonical heart：現行研究ノート

2026-11-15 / resonance-hearts-v1。再開時は `00_research_plan.md`、公表用原稿 `papers/nc_del_pezzo_resonance_hearts.tex`、本ノートを読む。heartの名称は Rains heart、VdB heart、AS heart、anticanonical heart に統一する。

## 中心結果（負 Euler 指数）

smooth elliptic Rains surface X_q、選ばれた O_X=e、tau=S^{-1}[2]、境界 restriction Li^*、自然変換theta→idを持つ。根 alpha^2=-2, alpha·K=0 の共鳴の規約を O_E(alpha)⊗q^m=O_E、m=chi(e,M) とする。Rains 2019 §11 と 2022 §4 の既約純一次元根sheafの存在結果の適用範囲に限る。特に simple root、Li^*M=0、m<0 なら以下を証明した。

- theta M≅M, tau M≅M（境界 triangle theta M→M→i_*Li^*M）。
- 非零の Hom(e,M) は M の既約性から全射だが、Rains 2019 Cor10.16は root quotient の chi≥1 を与えるので m<0 に反する。よって Hom(e,tau^nM)=0 (all n)。Cor7.23から Ext²=0、Eulerから dim Ext¹(e,tau^n M)=-m。Rains heart のAZ generationは**確実に失敗**。これは単なる数値的non-amplenessの主張ではない。
- N=⊕_{n≥0}Ext¹(e,tau^nM) は gが同型として作用する、k[g]有限生成の次数付きR加群（各次数 -m）。πN≠0で境界外。R/(g-1)=(R[g^{-1}])_0 の有限次元右加群 V=(N[g^{-1}])_0 は dim_k V=-m。導来切断がこの対象で定義できれば Phi(M)=πN[-1]、従って Rains heart→anticanonical heart の**自然関手は非t-exact**。
- Rが標準noetherian qgrを与え、(πR,(1))がAZ-ampleなら、構造対象・tauを保つRains heartとanticanonical heartのabel同値は不存在。これは別の無標識abel同値、導来同値の不存在を意味しない。

## ring側で変わらないこと

Rains 2022 Proposition 5.1により中心正則元 g∈R1 があり、R/(g)=B(E,L,σ)（deg L=d）。したがって全 n≥0 で dim R_n=1+d n(n+1)/2。これは共鳴で跳ばない。同時に、ringのHilbert関数が不変であることは、qgrの導来滑らかさやRains heartとのt-exactnessを保証しない。負指数共鳴で確実に変わるのは、境界 g≠0 上で `A=R/(g-1)` が次元 -m の有限次元右加群を持つことと、自然な導来切断でその対象が cohomological degree 1 に現れること。

## 負指数だけのZariski密度

E⊂P² smooth cubic、q∈Pic⁰(E) non-torsion、p1,p2,p4,p5,p6を固定しL=O_E(1)とする。p3(n)∈Eを O_E(p3(n))=L(-p1-p2)⊗q^{-n} (n≥1) で選ぶと、alpha=h-e1-e2-e3のrestrictionはq^n、共鳴指数m=-n。p3(n)は相異なり、一般位置に失敗するのは有限点のみなので、genuine del Pezzoを保ちつつ稠密。こうした1次元ファイバーを基地パラメータとともに動かすと、負指数共鳴の合併は関連する六点/楕円gluingパラメータチャート全体でも稠密。一次文献Rains 2022 §4も有効根が稠密な超曲面族で出ると明言する。

## 三つのresonance指数を区別

| index m | 根sheafのHom/Ext | Rains→anticanonical の意味 | 論理状態 |
|---|---|---|---|
| m<0 | Hom^0=0、Ext^1=-m、Ext^2=0 | 非零の有限次元 affine moduleが[-1]へ移り、自然比較はt-exactでない | Rains既約sheaf存在条件の下で証明 |
| m>0 | Hom^0-Ext^1=m>0、Ext^2=0 | Hom^0非零。Ext^1是否は未決 | 同期する全共鳴のt-exactnessは未解決 |
| m=0 | genuine del Pezzo SではO_E(alpha)非自明で共鳴自体が不在 | weak classical avatarでは(-2)曲線O_E(-1)がderived orbitにも不可視で反標準収縮により消失 | 既知古典的壁と今回の負指数denseを区別 |

genuine Sのm=0排除：±alphaが有効ならH=-K ampleとH·alpha=0に矛盾。RRでchi(alpha-H)=0、h0=h2=0からh1=0、反標準曲線制限列よりh0(E,O_E(alpha))=0。従ってalpha|Eは自明でない。

## 重要な未解決の比較

1. **既存dP1論文の導来同値を独立監査**：`papers/dp1_anticanonical_models.tex` はgenuine smooth S/Eの全qでPhi:D^b(Rains heart)≈D^b(qgr R_q)、qgr smooth/hdim2を主張・証明記載している。しかし今回、その完全忠実性、本質的全射性、有限性の証明を独立再検証していない。正しければdense negative mで「導来圏不変、heartは変化」。今回の新定理はその強い同値を入力としていない。
2. **正指数共鳴**：Ext¹(e,M)が零になるか、特定の既約根sheaf以外にheartを変える対象があるか。非comm affine A=R/(g-1)の有限次元加群の分類と関連する。
3. **正確なZariski稠密nessの成分と次数**：root sheaf存在が適用される一連のRains型族に関して証明済み。全てのnc del Pezzo moduliの全成分への稠密性や、各共鳴の非同値を無条件に主張しない。
4. **AS/VdBとの照合**：構造対象のpointed性、対象の存在、自然比較と導来同値を区別する。前回の古典的weak dPのzero-index障害は別のメカニズム。
5. **リング理論とsmoothness**：Rのnoetherian/χ、gの中心正則性、graded localizationとqgr_Rの有限性を確認する。qgrRの特異化は負指数mだけでは従わない。

## 一次文献と再現

- Rains, *The birational geometry of noncommutative surfaces*, arXiv:1907.11301v1, §7 Definition7.1, Cor7.23; §9 Definition9.1; §10 Cor10.16; §11 pp139–141 (simple root irreducible sheaf existence when determinant matches).
- Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2, §4 pp33–35 (dense effective roots, q-power resonance, numerical ample); §5 Eq(5.1) theta→id→i_*Li*, Proposition5.1 orbit ring central regular g.
- `papers/dp1_anticanonical_models.tex`: det restriction formula det Li_q^*v=O_E(c1(v))⊗q^{m-r} in its specified gluing convention; manuscript-derived equivalence remains unverified independently.
- `papers/sections/cubic_corner_root_walls.tex`: classical weak dP m=0 wall, proof of actual derived loss, not the present m<0 dense phenomenon.
- `computations/verify_resonance_hearts.py`: E6/E8 intersection arithmetic and negative m extension dimensions; **not** an algorithm proving root sheaf existence or derived equivalence.

Source claims and new formal consequences are distinguished in the focused paper. Recompile using `latexmk papers/nc_del_pezzo_resonance_hearts.tex` (LuaLaTeX via repository .latexmkrc). No PDF/ZIP tracked in GitHub; GitHub main canonical; do NOT save Library on successful push.
