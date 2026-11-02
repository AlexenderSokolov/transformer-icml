# Targeted independent proof cross-check of UI001

2026-11-02. Reviewed `UI001_range_uniform_iid_floor_v1.md`, SHA256 `c4bd8a5d7324ed1cf03c1d746a253b592fbe9a63e9e6020be95e657c13307dde`. The earlier `ATTACK_UI001.md` is unchanged and records the genuinely independent, initially unseen-draft attack. This document is the subsequent candidate-aware mathematical audit.

## Verdict

**The candidate's nonadaptive top-m argument adequately resolves the giant-unrealized-weight and mutually conflicting-head concerns raised in the attack. No mathematical gap found in this targeted proof audit.** This is a substantive proof check, not a reinterpretation of the earlier absence of a counterexample. It is not formal verification, an external novelty check, or evidence for models outside the stated local one-block contract.

## Critical distinction that resolves the attack

The proof never needs the actual selected weight sum to approximate the sum of selected envelopes or their largest member. It needs only the selected known mass W to dominate m times the largest *remaining* envelope a_*.

Each of the m selected envelopes is >=a_*. Every realized maximizing pattern therefore contributes >=a_*. The success indicators have expectations >=q=4^{-r}. Their dependency graph has maximum degree <=2r-2, so Var(success count)<=(2r-1)m. Chebyshev bounds failure of count>=qm/2 by 4(2r-1)/(q²m). Thus W>=qm a_*/2 outside an O_r(1/m) exceptional event, independently of κ. A single unrealized gigantic maximum has no adverse effect on this argument.

For F fixed head/query branches, a union bound gives the simultaneous event E. Independence between branches is unnecessary. Even when heads assign their largest weights to mutually exclusive patterns on a given window, each needs only a small fraction q/2 of successes across m windows. Bounded local dependence, not cross-head independence, supplies the high-probability count. E is measurable in the fixed oracle B because every selected window is fully revealed.

## Remaining links checked

- U is fixed independently of p and bits after fixing the independent encoder seed; m<=N<=Lm. Consequently the posterior likelihood is exactly p^t(1-p)^(N-t), and residual bits remain conditionally IID at fixed p.
- At most rN unselected windows intersect U. Their unconditional envelopes may indeed become unattainable, but the proof does not invoke an expectation lower bound on them. Their total envelopes are <=rN a_*<=(2rL/q)μ by the known-mass certificate. Disjoint windows retain E[w_i|B]>=q a_i. This proves (3.1) without κ.
- Resampling a remaining bit affects at most r terms. The squared change bound and Efron–Stein give 2r² sum a_i², hence Vμ²/m using a_*<=2μ/(qm). Fixed selected terms have zero variation. Further windows that become entirely fixed cause no problem because including them only weakens the upper bound.
- Chebyshev at μ/(4Q), union over numerator/denominator and F branches, gives failure <=32FVQ²/m<=.01. Dn>=3μ/4 and exact ratio subtraction yield <1/Q tube error.
- The conditional derivative bound <=8r follows from the free-bit score bound, including partially fixed windows; arbitrary signed bounded values do not change it.
- The posterior interval I_B has high posterior mass on T by Hoeffding plus Markov. On T, distance(y,I)<=3/sqrt(N), so at the constrained mode |ell'|<=16sqrt(N); |ell''|<=16N. Integrating over delta=1/(64sqrt(N)) in an available inward direction proves the stated 128sqrt(N) density bound even at prior endpoints. Thus the earlier concern about false unconditional endpoint density bounds is avoided.
- N>=m>=Q² makes the Lipschitz mesh have O_r(1) points on I_B; two 1/Q errors plus downward rounding fit the conservative 9^D grid bound. B fixes the actual query, so no extra side alphabet remains.
- Good posterior joint probability is >=.98; radius epsilon neighborhoods of the R0 decoder outputs have posterior mass <=1/4. The risk arithmetic, averaging over B and independent decoder/encoder seeds, and the common uniform prior are valid.
- When M<m the full-history c/sqrt(M+2) floor implies the displayed c(D,r)/Q; ceil and real-Q inequalities are in the correct direction. At-most-D padding and the all-state stationary IID embedding cause no exception.

The adaptive alternative in the independent attack remains a separate plausible route but is unnecessary for repairing this candidate: the candidate already controls precisely the appropriate residual envelope scale.
