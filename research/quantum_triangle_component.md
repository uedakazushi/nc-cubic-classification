# 固定量子so3包絡の4次元族：成分性の現状

2026-11-17 / triangle-component-v1。入口は `00_research_plan.md`。
証明は `papers/sections/cubic_quantum_triangle_deformations.tex`。
単独抜粋は `research/quantum_triangle_note.tex` から組版する。

## 結論と正確な範囲

固定三乗根包絡の `[U/A4]` は局所的に極大なH3族ではない。
その滑らかな楕円境界を持つ稠密開部分は、7次元の滑らかな既約H3表示stack
`[V/A4]` の余次元3正則閉部分stackとして実現される。
このため、これらの代数的族を受け入れる局所有限型のintrinsic pointed H3モジュライstackが
構成されれば、元の4次元族の像の閉包はその既約成分ではない。
全stackの代数性や7次元族の成分性・versal性を新たに証明したという意味ではない。
対象は構造対象を保つexact同値であり、導来同値類だけの商ではない。

## 構成と依存関係

q^2+q+1=0。包絡の三関係を
`yz-qzy=tx+a t^2`, `zx-qxz=ty+b t^2`, `xy-qyx=tz+c t^2`
へ拡張する。tは中心。全係数PBW/CY AS4。

X_h=x^3+q^2 t^2x（巡回）、d=-(q+2)/3 とし、
Omega_(a,b,c)=Omega_0+d t^2(ax+qby+cz)。
これらとt^3は常に中心三次の基底をなす。
従って元のP4切断を保ったまま独立な三係数を動かせる。
全中心の三次式も論文に保持した。

切断係数u=[alpha:beta:gamma:delta:epsilon]、Delta=alpha^3+27beta gamma delta。
T_ell={beta gamma delta Delta !=0}上では境界がa,b,cに依存しない滑らかな楕円THCRで、
translationは正確に位数3。
`cubic_finite_order_relative.tex` の `thm:finite-order-relative-H3-open` を
A3×T_ellに適用するとH3開集合Vを得る。
{0}×U_ellを含むので非空・既約・7次元である。

全graded包絡同型は共通次数スカラー、二符号変更、巡回置換のみ。
理由は Z(B)_1=kt、境界量子多項式環のpoint graph、tX係数による平行移動の消滅。
a,b,c≠(0,0,0)は元の固定包絡に戻らない。
H3反標準環の二次包絡は内在的に復元されるため、幾何学的pointed exact同値でも消えない。
3方向は一次変形にとどまらず明示A3族へ積分されている。

使用した既存入力（確認時 main 944ad1631f893c1d644052211e32eb12d23dc881）：
- `cubic_quantum_triangle_full_cuts.tex`: 元のUの非空性、H3認識、幾何学的矢。
- `cubic_finite_order_relative.tex`: 固定有限位数楕円境界族のH3開性、表示族の底変更。
- `nc-cubic-classification.tex`: intrinsic反標準環と二次包絡の復元。

## 確実性と検証

新しいPBW・中心・群作用の恒等式は元の関係から記号的に再計算した。
係数環QQ[q,a,b,c]/(q^2+q+1)であり、有限標本からの外挿ではない。
一次座標変更の24×16行列はQ(q)上rank15、核は共通次数スカラー一本。
したがってda,db,dcは座標変換で消えない。

通常の証明：全中心の生成と唯一の関係、全包絡矢、既存H3開性の適用、7次元族、非成分性。
既存H3開性の全依存定理の独立再監査は未実施。
全intrinsic圏族の相対再構成・降下は未解決のままであり、表示族の商と区別する。
全Hochschild接空間の次元を7と主張しない。

## 次の課題

1. 7次元族の一般点で全H3変形を計算する。まず固定位数3・中央境界を保つ範囲の
   全対称PBW係数を平行移動と対角変換で正規化し、この7次元chartの局所被覆を調べる。
2. 楕円translationが3-torsionを離れる横断方向を、中心三次元の持上げと同時に構成する。
   PBW性だけではH3性は出ない。有限位数を横断するH3開性は既存定理の範囲外。
3. 必要な相対再構成を証明し、7次元またはそれ以上の族を全intrinsic局所stackに接続する。

## 文献と再現

- Etingof--Ginzburg, JEMS 12 (2010), 1371--1416, DOI 10.4171/JEMS/235,
  Proposition 7.3.1(ii), Theorem 3.3.2。一次資料の該当箇所を確認。
- Berger--Taillefer, J. Noncommut. Geom. 1 (2007), 241--270, DOI 10.4171/JNCG/6,
  Theorem 1.1(i)。低次potential追加のPBW/CY定理を一次資料で確認。
- Huang, Center of the universal Askey--Wilson algebra at roots of unity,
  arXiv:1509.08719。関連する既知の中心研究。規約の完全比較・新規性の網羅調査は未了。

```sh
python3 computations/verify_quantum_triangle_deformations.py
latexmk -lualatex research/quantum_triangle_note.tex
```

コードはPython3/SymPyのみを使い、証明書JSONを同じcomputationsディレクトリへ再生成する。
PDF・中間生成物はGit追跡しない。GitHub mainが正本、LibraryはGitHub保存失敗時だけ。
