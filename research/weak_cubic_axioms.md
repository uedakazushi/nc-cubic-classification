# 現行研究ノート：weak cubicの四問

2026-11-15 / recognition-v3。最初に00_research_plan.mdを読む。完全な新証明はpapers/weak_cubic_axioms.tex。証明の重複は避け、再開に必要な補足をここに残す。

## 構造的な整理

定義に全整数のh0が入るので仮定1は自動。Rの負次数は零。sがheartを保つという条件は、負twistも使うため両方向のexact autoequivalenceとして読む。rankは裸のAbel圏には未定義なので、s不変のtorsion Serre部分圏とrank関数を固定するか、整域section環の商斜体から定義する。反例では後者が使える。

全weak対象、条件2付き、AS4二次包絡＋正則三次核という超曲面認識部分、R13中心拡大型部分は別々。含意を逆にしない。smooth proper enhancementを要求する定義と、今回のgd2＋Serreの定義も同一視しない。

## 反例の代数

Bの変数を(t,x,y,z)と書けば、tx=ζxt、ty=ζyt、tz=ζzt、xy=yx、xz=ζzx、yz=ζzy。F=t³+x³+y³+z³。q行積1、q³1なのでBはCY4、Fは中心正則。R=B/(F)は標準cubic Hilbert値を持つ。三次中心は一般R13より大きく、x³,x²y,xy²,y³,t³,z³の6次元。中心一次・二次は零。

t局所化のdegree0ではu1,u2が可換、ui u3=ζu3 ui、Σui³+1=0。r=u1/u2、v=u2³、w=-1-(r³+1)v。中心体k(r,v)上のsymbol algebra(v,w)_ζはw付値でvの残余が非cubeなのでdivision。この理由でRのrank1/torsion-freeの意味が保証される。単に中心元でdomainを割ったからdomain、と推論していない。

tailsのgd2はKanazawaの指数=変数数の定理をそのまま引用せず、指数3・変数4へ局所証明を適用。中心完備化でnormal yiの三乗がradicalに入るので(yi)がnilpotent ideal mod radicalとなりyi自体radical。正規正則元によるgldim降下と、all-nonzero fibreのtwisted finite group algebraの半単純性からchart gldim2。全局所perfect性を貼り合わせた後にSerre双対を使う。

## R13閉包を排除する不変量

Z(B)1だけでは周期表示の差を排除できない。四頂点の非零線型元が二次零因子にならない開集合で、四つのnormal line Liとreturn φ0φ1φ2φ3が射影恒等であるというprojective incidenceを取る。proper射影なので像は閉、四つの独立基底変更で不変。中心tを持つR13一般点はこれを満たす。

量子Bのnormal line pairのsupportはqの同一行のclass。4と3が互いに素なことを使って行の比例は一致になる。classは{0},{1,2},{3}、returnの指数は(0,1,1,1)、(2,0,0,1)、(2,2,2,0)。どれも射影恒等でない。従ってcomponent exclusionはpointed/rolled-up表示においても成立する。

## 提示と代数性

Artin平坦変形で低次数生成・関係上界が保持される証明は有限次元Nakayamaを各次数に適用する。全次数の平坦性を先に仮定しており、categoryの任意変形へ無条件に適用しない。

P=incidence(J2⊂V² rank6,J3⊂V³ rank45,VJ2+J2V⊂J3)は有限型projective。J3はminimal cubic generatorsではなく全次数3のkernel。B=Q(R)のoverlap次元kなら新三次関係はk−3本。AS4ではk=4。

全upper-rank minor idealはNoetherian性で有限生成だが、全部のlower-rank opensの交わりが一つの通常開集合とは限らない。Artin近傍では各非零minorが単元に持ち上がるので有限型formal hullが得られる。全stack代数性へ飛躍しない。通常の族にはnoetherian/saturation/relative Serre/Hom basechangeを指定する必要がある。

## Generic fibreの意味

R13 central incidenceはP(E3)、rankE3=2。kt³の内在的sectionはBrauer-conicの捩れを分裂する。一般の有限自己同型で割ってもcoarse birational fibreはrational。K(λ)が正確な関数体。weak条件の成立は保持稿のgeometric generic central valueで確認するが、全P1の点で成立するわけではない。特にt³商は除外される。一般k=Qbarの固定ambientに超越λを選ぶことはできず、幾何学的一般体へ進むものとして述べる。

## 一次資料と参照箇所

- Artin–Zhang, Noncommutative projective schemes, Adv.Math.109(1994),228–287, DOI10.1006/aima.1994.1087。Theorem4.5、χとSerre消滅の区別。DOI書誌確認。元PDFの全再監査ではない。
- Kanazawa, arXiv:1409.4101v2, Proposition2.4、§2.3/Lemmas2.8–2.9。今回一次PDFを確認。本文の主定理は指数=変数個数。今回のFano cubicはlocal proofの適用で別に証明する。
- Yekutieli–Zhang, Serre duality for noncommutative projective schemes, Proc.AMS125(1997),697–707。著者公開ページ https://www.math.bgu.ac.il/~amyekut/publications/nc-serre/nc-serre.html 。balanced dualizing input。著者ページ確認、PDF取得失敗もあり全原文再監査としない。
- Pym, arXiv:1403.6444, §3.1および§3.4。quantum polynomialとcentral Sklyanin拡大を区別。全6成分の成分交叉の分類を本稿の前提にはしない。
- Behrend–Noohi, arXiv:1507.07054 / https://webspace.maths.qmul.ac.uk/b.noohi/papers/NCStable.pdf 、§1,§3.5。graded algebraモジュライと有限切断。内在的weak substackの代数性をこの論文だけで宣言しない。
- AOU, arXiv:2404.00175v1, Introduction,§5,§9。複数のnc cubic定義と9頂点marking。全weak分類との一致は既知入力ではない。
- Rennemo–Segal–Van den Bergh, arXiv:1705.01366v2, Lemmas3.2,3.3を今回確認。任意の超越体拡大がglobal dimensionを保つとはしていない。centre localisation後に代数的分離拡大を用いる。

## 確実性

新反例は通常の証明と有限計算を用いて今回検討した。外部独立査読、proof assistant、新規性の網羅確認はなし。保持したsurface/R13稿は今回全再監査しておらず、そこでのWeyl商・有限Hessian商の主張を新たに検証したと報告しない。新稿の最重要な否定結果はそれらの一般商の詳細に依存しない。
