# JOR selector audit

Date: 2026-11-12. Status: bounded independent derivation, not a proof of the manuscript's lower theorem or a priority certificate. No shared checkout edited.

## Sources

- Manuscript oracle and its pathwise/expectation estimates: https://github.com/AlexenderSokolov/transformer-icml/blob/main/v10_research/positional_manuscript_consolidated_20261103/sections/proofs_positive.tex (Proposition `prop:count-oracle`). Inspected baseline manuscript commit: `2ca64346e0dbb19ccf12b5c0f06f12cd0ff31a70`.
- Jain, Orlitsky, Ravindrakumar (2022), Lemma 3 and its proof: https://arxiv.org/html/2202.05453v1 . The geometric selection lemma needs simultaneous valid-radius containment, not merely separate expected errors.

## Candidate family

Write q for the designated next-symbol probability at the protected terminal row, C', J' for its corrupted counts, and C, J for its clean counts. For each integer budget b >= 1, the manuscript's candidate is

    a_b = (C' - 6b)_+ / (J' + 6b + 2).

If the actual attack budget k <= b, its pathwise oracle argument supplies

    |a_b - q| <= 2 E_0 + min{q, (24b+2)/(J+2)},
    E_0 = 1{J>0} |C/J - q|.

This statement applies to a k-budget attack because that attack is also legal under the larger allowance b. The target is random, but it is the same protected target for every candidate on a given realization.

Take an increasing geometric grid starting at b_0 = ceil(sqrt(M)), doubling and terminating at M (deduplicate the endpoint). Set g_j = b_j/M. Let j_* be its first point with b_j >= k, taking j_*=0 when k <= b_0. Then g_* = g_{j_*} <= 2 g_M(k), where g_M(k)=max{M^(-1/2), k/M}. Starting at b_0 instead of zero costs only a universal constant.

## Explicit pairwise JOR selector

Fix a deterministic t>0 and set r_j=t g_j. Select the smallest index j_hat such that

    |a_{b_j_hat} - a_{b_l}| <= r_j_hat + r_l  for every l >= j_hat.

Return a_{b_j_hat}. The largest index is always admissible. This algorithm uses only counts, endpoint, M and the fixed grid, and does not use k.

On the event that |a_{b_j}-q| <= t g_j for all j>=j_*, index j_* is admissible, so j_hat<=j_*. Pairwise consistency with j_* and the triangle inequality give

    |a_{b_j_hat}-q| <= 3t g_* <= 6t g_M(k).

No independence of candidates or deterministic target is required for this geometric argument.

## A shared random envelope eliminates a naive union-bound penalty

Put D=J+2, b_*=b_{j_*}, and define

    W = 2 E_0/g_* + min{q,(24b_*+2)/D}/g_*.

For b>=b_*,

    min{q,(24b+2)/D}/(b/M)
      = M min{q/b, (24+2/b)/D}

is nonincreasing in b. The empirical-error term divided by b/M is also nonincreasing. Hence

    sup_{j>=j_*} |a_{b_j}-q|/g_j <= W.

Using the manuscript's empirical expectation bound and weighted-occupation estimate yields E W <= C_0 with a universal constant. Its stated estimates permit C_0=191488: the displayed oracle calculation is 31744/sqrt(M)+159744 b_*/M, and b_*>=sqrt(M).

Thus the available estimates give simultaneous control without a log(number of candidates) union penalty. But a bounded expectation is not deterministic fixed-radius containment. Markov's inequality gives only P(W>t)<=C_0/t. Bounded loss and the selector guarantee imply

    R(selector) <= min{1, 6t g_M(k) + C_0/t}.                 (A)

For a fixed target budget, optimizing this expression gives O(sqrt(g_M(k))), not O(g_M(k)). Such an optimizer depends on the unknown k and is therefore only diagnostic, not a fully adaptive algorithm prescription. A fixed t=t(M) gives (A) simultaneously for all k. This displayed bound does not establish a uniformly constant competitive factor.

## Abstract counterexample to the mean-risk implication

This is NOT a Markov-source/attack counterexample and is NOT a disproof of the manuscript theorem. It demonstrates only why separate mean-risk oracle guarantees cannot automatically be fed into JOR with constant radii.

Fix target q=1, scales 0<g_0<<g_1<1/(4t), and an event B of probability p=g_1. Let a_0=1 always and let a_1=0 on B, 1 otherwise. Then

    E|a_0-q|=0 <= g_0,   E|a_1-q|=g_1.

On B, the candidate distance is 1>t(g_0+g_1). The two-candidate pairwise selector rejects a_0 and returns a_1=0, producing risk g_1, arbitrarily larger than g_0. The candidates are decreasing in their budget index, as is the manuscript's shrinkage family. This ordering alone does not repair the generic mean-risk inference.

## What remains unresolved

No contradiction to the claimed lower bound has been obtained. That conclusion does not validate its proof. A real challenge would require stronger tails or a different direct expected-loss analysis yielding O(g_M(k)) uniformly for one map, or an explicit source/attack calculation exhibiting such performance.

The most useful next bounded test is direct evaluation of the selector on the manuscript's lower-witness family. There the candidates are explicit functions of (C',J'); one can ask whether rare terminal-row occupation creates the excess loss and whether the order is logarithmic.

## Suggested exposition

The known-budget candidates admit a common random normalized-error envelope with bounded expectation. This alone does not supply the simultaneous fixed-radius validity required by a generic consistency selector. The direct envelope/Markov argument yields (A), not constant-factor adaptation. The obstacle should not be described merely as dependence or a random target.
