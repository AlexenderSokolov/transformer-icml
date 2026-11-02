# Pinned primary comparison for the admitted D1 claims

Lead, 2026-10-25. This sharpens the comparison in integration-theorem-v2
using the already pinned Counter map and its local page extracts. No new
retrieval, reference expansion, priority claim or global literature survey
was performed. These comparisons need C4 review; the three native
mathematical Facts do not independently certify a novelty claim.

Source versions and locations are fixed in counter/sources/primary-map-v1.md
(SHA256 f5b2fdcfd9b96ce74ebc8141b9dd0dde7c33caa10952aca6dacf90229a9d6f45).
The local PDFs have these hashes:

- Han–Jana–Wu, *Optimal prediction of Markov chains with and without
  spectral gap*, 2106.13947v2:
  0b7b2e83fd0e405507eccb02b954129e4a0dc5f7926e1cc6d3a71f45e3e40cf7.
- Paulin, *Concentration inequalities for Markov chains by Marton
  couplings and spectral methods*, 1212.2015v5:
  7a54a70c47954687e87800c5e7dcc9df37a47568ed13f35c5c170a5728d92a82.
- Geiger–Boecherer, *Greedy Algorithms for Optimal Distribution
  Approximation*, Entropy18(7):262, published2016:
  cae05b607164d7ff44315b3cd5ab1f9b00f5514bd799b3984f561cb72f4e6e84.

## Comparison at the theorem level

Here n is a primary paper's trajectory length, k its alphabet size and
d its Markov order; d is not this project's prefix endpoint m. M in the
quantization paper is a denominator, not this project's eligible count M.

| Pinned result | Assumptions and quantifiers | Risk/estimator or other conclusion | Exact relation to this stage |
|---|---|---|---|
| HJW Theorem3/Corollary4, PDF pp4–5, class definitions(8)–(9) | Stationary ordinary reversible first-order k-state class with absolute-gap lower bound gamma0. Theorem3 gives sufficient gap regimes; Corollary4 fixes k>=2 and characterizes parametric order by gamma0 bounded below by a positive constant. | Add-one estimate at the observed terminal state; Theorem3 bounds expected terminal KL by a constant multiple of k²/n in its stated regimes. For fixed k, Corollary4 gives O(1/n) iff gamma0=Omega(1). | This is an actual-terminal neighbor, so terminal-history dependence alone is not a novelty claim. D1's pair chain is not ordinarily reversible. Its exact first-order subcurve is distinguished; no four-state substitution transports this theorem to all of D1. Our family-specific C1 is separately proved. |
| HJW Theorem22 and binary specialization Theorem24, PDF pp39–40 | Full stationary order-d class, d>=2; constants depend on d, and k lies in the specified range up to n^(1/(d+1))/C_d. Binary d=2 is explicit in Theorem24. Higher-order reversal is a symbol-process notion, not ordinary pair detailed balance. | The full-class minimax terminal expected-KL order is k^(d+1)/n times log(n/k^(d+1)); binary order2 gives log(n)/n. The upper construction uses the stationary prediction/redundancy reduction and the add-one probability assignment(95)–(96). | Our D1 is a strict structural family with fixed binary alphabet, unknown u,t and uniform 1/N average risk. This is compatible with a larger-class logN/N minimax rate. A lower bound for the larger class does not imply a D1 lower bound. The primary does not supply the present fixed-u terminal00 minimax comparison or the same-algorithm output-grid pair of rates. We do not claim an all-stationary-second-order C/N theorem. |
| HJW Lemmas30/31, PDF pp48–50 | Uniform context stationarity and transition entries bounded above and below on the stated alphabet scale; the pseudo-gap argument uses these conditions. | Frobenius transition-estimation control for the constructed high-order family, rather than this conditional-terminal loss. | D1 has context mass u arbitrarily small and the10 successor probability r tending to0. It does not uniformly satisfy those hypotheses. No bound from these lemmas is an admitted premise of C1. The extraction anomaly around Lemma30 is not a confirmed erratum or a usable formula. |
| Paulin Propositions3.15/3.16, PDF p18, with reverse/pseudo-gap definitions pp13–14 | Comparisons of path events under different initial distributions; uniform ergodicity gives a uniform decay bound. Point-start L2 comparisons involve N_q, equal to1/pi(s) for a point mass. | Additive total-variation comparison after burn-in, not a predictor or terminal KL estimator. Other listed variance/Bernstein bounds have their own stationary/bounded-function assumptions. | These identify standard tools adjacent to the reverse entire-prefix bridge. Our C1 controls the whole prefix law uniformly using a direct finite-state minorization and then applies the appropriate bounded loss; it does not square a TV remainder or divide it by rare-context mass. No reversible gap theorem or unbounded-KL concentration statement is silently substituted. |
| Geiger–Boecherer Algorithm1/Proposition1/Table1, PDF pp2–3; Lemma1 p4; Proposition2 p5; equation10 p6 | The probability vector to approximate is supplied. The denominator M is chosen, and support preservation has explicit feasibility conditions. The Markov application is approximation of known rows with stationary weighting. | Greedy M-type approximation optimizes the same-direction KL D(target || approximation). Proposition2 gives a finite approximation bound with a target-dependent feasibility factor; it is not a sample-size inference theorem. | This is a direct probability-quantization precedent and rules out presenting finite positive probability quantization itself as new. Our input is an unknown-law finite history and an actual terminal query. The point of C2 is the joint history/output classification on D1, including conditional00, and its compatibility with one implemented estimator. Nearest Euclidean grid rounding is used for order control, not asserted to be exactly KL optimal. |

The HJW full-class comparison is at the level of expected actual-terminal
KL, not an independent fresh-context experiment. Conversely, a rowwise
known-target quantizer does not by itself yield a conditional-terminal
statistical bound when the target and row visit counts are inferred from
the same history. The C1 to C2 bridge uses its proved conditional expected
KL and Pinsker in the MSE direction, not a change in the statistical law.

## Resources and quantifier limitations

The particular cited HJW and Paulin results are statistical or probability
theorems. Their conclusions do not provide our full N,b causal circuit
ledger, internal Q_A, output-bit protocol, masks, holds, finite exp/log
evaluator, offline generation or input-domain comparison. This statement
concerns those pinned results, not a claim that their papers or all other
works contain no computational discussion. Geiger–Boecherer supplies an
explicit algorithm; it does not give this project's finite bit-cost ledger
for learning a row from a dependent history. Abstract algorithm steps and
our charged bit operations are not interchangeable complexity measures.

In this project the statistical minimax lower class is stronger than the
constructed prefix family: it permits full history and independent seeds,
and for the conditional bound may even know u. The common upper algorithm
does not know u or t. Format lower bounds range over strictly positive
Q-grid outputs. They do not quantify over an internal-arithmetic budget
and hence cannot establish necessary Q_A, depth, number of heads or neural
width. C3 contributes sufficient constructive functions in individually
declared models and a paid same-output eight-counter baseline. It does
not show an optimized neural budget advantage over that baseline.

The known-target feasibility discussion around the quantization paper's
equation9 must not be read as a uniform threshold over all positive targets.
The stated feasible set requires each positive target coordinate at least
1/M; arbitrarily small target coordinates preclude a target-independent
threshold of that type. Neither the printed/extracted ambiguity nor a
finite diagnostic is treated as an established publication error.

## Scientific assessment for the responsibility handoff

The strongest obtained claims are the D1 finite-N statistical theorem,
the joint average versus conditional positive-grid rates, and their exact
nominal implementation with complete sufficient costs. They are a
mechanism/risk classification and implementation integration. Publication
novelty, optimal constants, neural advantage, practical training,
learnability and noisy-arithmetic reliability remain unproved.

普通中文解释：00出现得少，难点首先是历史里有没有足够的00证据；但一旦固定
条件00，它的两种后继概率都离0和1有固定距离，舍入的小误差只产生平方阶KL。
10本身常见，它的一种后继却可以任意稀少，严格正网格必须至少分给它1/Q，
所以平均风险仍会承受一阶的精度损失。两个结论由同一个分支算法达到。
把输出写得更细，不能补出没观测到的稀有情境；把这件事证明出来，也不等于
证明神经网络更省资源、更容易训练或能抵抗任意算术噪声。

T1在这个指定族上的预期KL结论和T2的历史/输出联动已有承重原生前提。
更广的未知规律、训练所得机制、扰动进入位置及累积可靠性、严格同预算下的
结构收益与必要资源仍属于母题。C4/root审查和最终审计尚待完成；阶段SOLVED
不关闭这些问题，也不重开历史停放路线。
