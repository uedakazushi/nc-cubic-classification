# Fricke・Askey–Wilson・DAHAとの比較

2026-11-17 / triangle-component-v3 / 文献比較。現行研究方針は `00_research_plan.md`、主要な成分原稿は `papers/quantum_cubic_component.tex`。本ノートは現在有効な**関係式の同定**と、全8次元成分への拡張が未証明である範囲を分離する。

## 1. 正確に証明できるAskey–Wilson特殊化

(q^2+q+1=0)、(Delta_q) をTerwilligerの規約の普遍Askey–Wilson代数とする。中央元 (alpha,eta,gamma) は
[
rac{alpha}{q+q^{-1}}=A+rac{qBC-q^{-1}CB}{q^2-q^{-2}},
]
と巡回式で定義される。(q+q^{-1}=-1) なので、第一式は厳密に
[
BC-qCB=(1-q)(A+alpha)
]
へ変形できる。従って (x=A/(1-q)), (y=B/(1-q)), (z=C/(1-q)) と置くと
[
yz-qzy=x+alpha/(1-q),quad
zx-qxz=y+eta/(1-q),quad
xy-qyx=z+gamma/(1-q).
]
よって非斉次化
[
V_{a,b,c}=klangle x,y,zangle/
(yz-qzy-x-a, zx-qxz-y-b, xy-qyx-z-c)
]
について、生成元と定義関係の両方向の対応から
[
V_{a,b,c}simeq
Delta_q/(alpha-(1-q)a, eta-(1-q)b, gamma-(1-q)c).
]
ここは**証明済みの表示同型**である。Askey–Wilson Casimirと三乗根で増える中心元は、現行原稿の (Omega,X,Y,Z) に対応するが、元の規約による具体的な比例・低次補正の完全な対応表は未作成である。

## 2. Fricke型の4次元部分族とdominance

上記包絡の中心Casimir直線だけを切断する (Omega=-D) を考える。全中心式から (e=-(2q+1)/9), (f=(1-q)/3),
[
ell_a=((2q+1)a^3+2(q-1)a+3qbc)/9
]
（他は巡回）、(K,L) を現行原稿の同名式とすると中心は
[
XYZ-e(X^2+Y^2+Z^2)
-(Da+ell_a)X-(Db+ell_b)Y-(Dc+ell_c)Z
+D^3-fD^2+DK-L=0.
]
適当な非零スケール変換により標準Fricke cubic
[
u^2+v^2+w^2+uvw+A u+B v+C w+D_0=0
]
に移せる。4係数への写像のJacobianは (a=b=c=0) において、全体の固定非零スケールを除き
[
-3D(D-2f/3)^4.
]
従って (D
eq0,2f/3) では非零で、この4パラメータ族はFricke係数空間をdominantに覆う。これは全8次元成分の分類ではなく、**Fricke–Askey–Wilson部分族についての計算で証明済みの結果**である。元の固定包絡の1パラメータFricke pencilは (a=b=c=0) への制限。

注意：固定包絡の全中心三次直線は (mathbb P^4) であるが、その一般の切断は (Omega=-D) と同値ではない。一般に (X,Y,Z) の係数を含むため、楕円境界は滑らかであり、Frickeの三角境界ではない。

## 3. DAHAの正確な既知対応と区別

- Terwilliger, *The Universal Askey–Wilson Algebra and DAHA of Type ((C_1^\vee,C_1))*, SIGMA 9 (2013), 047, doi:10.3842/SIGMA.2013.047, arXiv:1202.4673。普遍Askey–Wilson代数から普遍階数1 DAHAへの**単射**。中央特殊化後の全商がspherical DAHAと同型であることまでは、本研究では証明していない。
- Oblomkov, *Double affine Hecke algebras of rank 1 and affine cubic surfaces*, IMRN 2004 (18), 877–912, doi:10.1155/S1073792804133072, arXiv:math/0306393。型 (C_1^\vee C_1) のDAHAが三角境界を持つFricke型affine cubicに対応し、そのspherical部分が量子化を与える。これは通常 (widetilde D_4) 側の幾何学。
- Etingof–Oblomkov–Rains, *Generalized double affine Hecke algebras of rank 1 and quantized del Pezzo surfaces*, Adv. Math. 212 (2007), 749–796, doi:10.1016/j.aim.2006.11.008, arXiv:math/0406480v3。星型 (widetilde D_4,widetilde E_6,widetilde E_7,widetilde E_8)。**(widetilde D_4) では三角境界の三次曲面**、**(widetilde E_6) ではnodal有理曲線境界の三次曲面**。本研究の一般の滑らかな楕円境界を持つ8次元族を (widetilde E_6) GDAHAと無条件に同一視しない。
- Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*, JEMS 12 (2010), 1371–1416, doi:10.4171/JEMS/235, arXiv:0709.3593。三次del Pezzoと単純楕円特異点 (widetilde E_6) のPoisson変形・量子化。一般8次元成分に対するより近い幾何学的比較対象。

## 4. 推奨用語と未解決課題

**暫定名：elliptic (E_6) quantization component（楕円 (E_6) 量子化成分）**。一般点の成分同定が未証明なので、文献上の正式名称ではなく研究内部の呼称とする。
**Fricke–Askey–Wilson locus** を上記の ((a,b,c,D)) の4次元部分族に使う。

次に行うことは、(i) AW Casimir・三乗中心の規約込みでの元の対応と、(ii) このroot-of-unity AW商から実際のspherical DAHAの中心特殊化への同型（存在する範囲を限定）を構成すること、(iii) 8次元一般点のEtingof–Ginzburg族とH3の相対moduliの比較、(iv) DAHAのbraid群・mapping class作用がFricke–AW部分族上の自己同型／圏の自己同値にどう現れるかを解明すること。直接同型が未証明の箇所に「DAHA成分」という断定的名称は使わない。
