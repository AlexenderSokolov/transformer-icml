# Stage3 primary pins and applicability notes

Counter，2026-10-25。页码为PDF一基；以下均为位置与释义，无长段摘录。
HJW、Paulin 仅读 inputs/source-stage2 的固定字节，没有重新下载或改写来源。
唯一新增作品是 Geiger–Böcherer；未从它的 references 再检索。

| ID | 作者、标题、固定版本、来源 | 页数 / 字节 / SHA256 |
|---|---|---|
| P1 | Yanjun Han, Soham Jana, Yihong Wu. Optimal prediction of Markov chains with and without spectral gap. [2106.13947v2](https://arxiv.org/pdf/2106.13947v2)，revision metadata 2022-05-03，title-page May5,2022。原始文件 inputs/source-stage2/outputs/009-rare-kl-rate/counter/sources/2106.13947v2.pdf。 | 66 / 691599 / 0b7b2e83fd0e405507eccb02b954129e4a0dc5f7926e1cc6d3a71f45e3e40cf7 |
| P2 | Daniel Paulin. Concentration inequalities for Markov chains by Marton couplings and spectral methods. [1212.2015v5](https://arxiv.org/pdf/1212.2015v5)，revision 2018-11-13。原始文件同一来源目录1212.2015v5.pdf。 | 42 / 700521 / 7a54a70c47954687e87800c5e7dcc9df37a47568ed13f35c5c170a5728d92a82 |
| P3 | Bernhard C. Geiger, Georg Böcherer. Greedy Algorithms for Optimal Distribution Approximation. [Entropy18(7):262](https://doi.org/10.3390/e18070262)，published 2016-07-18。下载 publisher [PDF](https://mdpi-res.com/d_attachment/entropy/entropy-18-00262/article_deploy/entropy-18-00262.pdf)，本目录entropy-18-00262-published.pdf。不是用未固定arXiv版本代替journal版本。 | 10 / 284964 / cae05b607164d7ff44315b3cd5ab1f9b00f5514bd799b3984f561cb72f4e6e84 |

P1 的 p2(1) 与 p39(94) 允许把风险映射到实际末端。pp4–5 的(8)–(9)、
Theorem3/Corollary4，pp27–28 的(65)/Lemma16，是 ordinary reversible first-order
定理；固定gap而非min-pi是其parametric结论的条件。p22 Theorem13 另有 binary
first-order gap-dependent estimator。pp38–40 的 Lemma20 和 Theorems22/24 分开符号
逆序和高阶全类率；pp48–50 的 Lemmas30/31 及(118)–(122)是 uniform-context、
uniform-positive高阶子族的Frobenius estimation。D1整体不满足前述一阶假设或后述
uniform-context/positive条件，pair链也不普通可逆。不能搬用全类lower。

P1 Lemma30 的常数条件及分式在本次文本抽取中显示异常，p48 所用例子
c1=1/2,c2=3/2 与抽取顺序不相容；本映射只依后续 Lemma31 的明确假设及 proof。
未将抽取异常当作可用前提或已确认的原文排版错误。
本文风险证明也不调用 source P1 Lemma23 的归一化公式。

P2 pp13–14 的 reverse、pseudo gap 和 N_q 由(3.2)–(3.4)定义；point initial 的
N_q=1/pi(s)。Proposition3.4/(3.9)–(3.10) 区分uniform mixing和带L2 initial prefactor
的界。p16 Theorem3.7/(3.18)为stationary variance；p17 Theorem3.11/(3.25)是
stationary nonreversible Bernstein，要求bounded centered f。p18 Proposition3.15/(3.29)
给path-event additive TV；Proposition3.16/(3.32)给uniform-ergodic衰减。
这些是本reverse-prefix bridge的标准工具邻居，非未知source预测风险/网格/电路定理。
按v5编号和适用域引用，不将HJW引Pau15编号当作v5同号命题。

P3 p1(1c)使用同向natural-log KL；pp2–3 Algorithm1/Proposition1/Table1给known-target
greedy M-type优化；p4 Lemma1给M>=支持大小时的支持保持。p5 Proposition2/(8)给
approximation bound；p6(10)把已知Markov rows的误差按stationary mass加权。
这是直接量化先例，但没有未知law样本量、terminal-history条件实验或本文整数bit成本。
P3 p5(9)前印刷的M>t_i不足以推出P_M可行；按p4的定义应要求t_i>=1/M；
p4(5)明确采用更严格M>1/t_i。不能把该target-dependent阈值说成全target统一阈值。

本地有限方法：pypdf6.1.3仅用于读页。对PDF的全文提取文件是分析中间物，不是新增
研究作品，不作为任何定理前提。上述映射与主报告不同于文献全覆盖或新颖性证明。
