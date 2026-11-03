# Positional counts restore robust prediction with an unknown edit budget

## Abstract

For binary second-order Markov prediction, the exact triple histogram can be sufficient for evaluating a clean path likelihood yet insufficient for adapting to an unknown number of adversarial edits. At the critical all-state certificate `beta = 1/M`, histogram-based adaptation is impossible, even after retaining moderately growing endpoint windows. Nevertheless, four first-half row counts restore the known-budget risk order for every edit budget. A single empirical estimator gated by occupation balance works for arbitrary initial states, including states outside stationary support. Combining this construction with full-history lower bounds gives an exact classification of the supplied-certificate domains on which adaptation is possible. An explicitly paid twelve-coordinate finite encoder preserves the strong-band result under both source edits and noisy quantization. This note connects these results; complete proofs and their exact review records remain in the linked source files.

## 1. Experiment and oracle benchmark

Observe a binary word of length `M+2` from an unknown homogeneous second-order source, with `M >= 64`. Its pair chain has transition matrix `K` and some stationary law `Pi` satisfying the **all-state** certificate

    K²(i,j) >= beta Pi(j).

The actual initial pair law need not equal `Pi` and may start outside its support. A source-independent offline randomized corruption kernel changes at most `k` of the first `M` symbols on every outcome, where `0 <= k <= M`. The last two symbols are protected. The predictor sees neither the clean interior nor the attack mask/seed. Its loss is unconditional expected TV distance from the source's true next-symbol law at the actual protected terminal pair.

With the budget supplied, the minimax risk has the order

    H₂(M,k,beta) = min{1, max{s, F₂}},       s = M^(-1/2),
    F₂ = (k/M)[1 + log(1 + 1/(k e_beta))],  e_beta = max{sqrt(beta), 1/M},

where `F₂ = 0` for `k = 0`. The upper holds for every initial law; stationary witnesses give the matching lower. Adaptation asks whether the **same** map at fixed public metadata can attain this benchmark for the clean experiment and every corrupted budget, without receiving `k`. [Known-budget upper](../binary_source_corruption/SC003_theorem.md), [matching lower](../binary_erasure_transport/BT002_entropy_bridge_lower.md), [scalar completion](../binary_erasure_transport/BT002_scalar_completion.md).

Uniform adaptation over all certificates is impossible even with the full corrupted word and supplied `beta`. That result does not settle a prescribed certificate curve: its difficult witnesses lie below the critical `1/M` scale. [Full-history obstruction](../binary_beta_known_adaptation/BK002_full_history_supplied_beta_obstruction.md), [certificate-dependent extension](../binary_certificate_adaptation_phase/KA001_certificate_phase_partial.md).

## 2. What histogram compression loses

At `beta = 1/M`, no predictor observing only the eight triple counts and the initial/final pairs can attain `H₂` simultaneously for all budgets. This is a statistical impossibility without computational restrictions. Retaining the genuine first and last `r` symbols does not repair it when `r = o(M^(1/3))`. The latter observation model is exact: it is not all interior length-`r` pattern counts or an arbitrary local-feature encoder. [Histogram obstruction](../binary_beta_known_adaptation/BK001_histogram_adaptation_obstruction.md), [endpoint-window obstruction](../binary_certificate_adaptation_phase/KH004_constant_crossing_window_obstruction.md).

Thus clean likelihood sufficiency is not robust adaptation sufficiency. The missing information need not be the entire ordering, however. A coarse indication of **when each row occurred** is enough. The construction below uses the global triple histogram, four first-half pair-departure counts, and the protected terminal pair; it does not need the initial pair.

## 3. A budget-blind occupation-balance gate

Write `Y_j = (X_(j+1), X_(j+2))`, for `0 <= j <= M`, and `n = floor(M/2)`. From the corrupted word compute, for the protected terminal row `u`:

- `J'`: its departure count over `0 <= j < M`;
- `J1'`: its departure count over `0 <= j < n`;
- `C'`: its full count followed by the designated symbol `d(u)`.

The designation is the complement of the first bit: `00 -> 1`, `01 -> 1`, `10 -> 0`, `11 -> 0`. Estimate the probability of this symbol by

    q_hat = C'/J'  if J' > 0 and 512 J1' >= J';
            0      otherwise.

The other symbol receives the complementary probability. This is one deterministic map, independent of both `k` and `beta`. Its all-start risk satisfies

    R_all <= min{1, 2^16 s + 2^16/(M sqrt(beta)) + 2^23 k/M},  beta > 0.

In particular, at `beta = 1/M` it is bounded by `min{1, 2^17 s + 2^23 k/M}`. On every band `beta >= c/M`, for fixed `c > 0`, the same map therefore attains

    Theta_c(min{1, max{s, k/M}})

simultaneously over all budgets. This is also the known-budget order on that band, since `F₂ <= k/M + 1/(M sqrt(beta))`. The constants are conservative, not practical performance estimates. Four counters suffice; their minimality is not claimed. [All-start proof](../critical_beta_adaptation/CB005_all_start_critical_adaptation.md), [stationary proof and deterministic gate reduction](../critical_beta_adaptation/CB004_stationary_critical_adaptation.md).

### Why a positional gate is useful

Editing `k` symbols changes each relevant count by at most `6k`. A corrupted gate decision disagreeing with a well-separated clean decision forces the clean terminal-row count to be `O(k)`. Universal terminal-occupation bounds then pay for these decisions at order `k/M`. On balanced clean histories, a deterministic-time split gives a terminal-weighted inverse-count expectation of order `1/M`, controlling the empirical-ratio perturbation.

The remaining clean cost is the weighted imbalance event

    E[q_(Y_M) 1{J1_(Y_M) < J_(Y_M)/256}] <= C/(M sqrt(beta)).

The all-start proof obtains a joint terminal/occupation tail retaining the target stationary mass, using a hitting potential, a loop identity and an auxiliary exponential tilt. It treats absorbing singleton support and unsupported starts separately. It neither assumes global square-root-beta mixing nor treats row observations as IID after conditioning on the terminal state. The earlier stationary proof uses a separate reversal argument and remains valid on its original scope. [Weighted stationary argument](../critical_beta_adaptation/balance_probe/BP001_stationary_weighted_balance.md), [all-start argument](../critical_beta_adaptation/CB005_all_start_critical_adaptation.md).

The generic first-hit pointmass scale used as background was established by Norris, Peres and Zhai. The self-contained derivation here is not presented as discovery of that scale. The literature reading was limited to the stated proposition and its proof, not a comprehensive novelty search. [Original paper, Proposition 1.1 and Lemma 2.1](https://arxiv.org/pdf/1408.0822), [precise reading-scope note](../critical_beta_adaptation/CB005_first_hit_prior_art_note.md).

## 4. Exact supplied-certificate domains

Let `E` be any public set of pairs `(M,beta)`, with `beta in [0,1]`. Adaptation on `E` requires one finite constant uniform over its horizons, supplied labels and all budgets; the maps and constant may depend on `E`. For `beta > 0`, define

    G_hist = min{M² beta, 1/(sqrt(M) beta)},
    G_full = min{M² beta, 1/(M beta)},

and set both quantities to zero at `beta = 0`.

| Available observation | Necessary and sufficient condition |
| --- | --- |
| Triple histogram and initial/final pairs | `sup_E G_hist < infinity` |
| Full corrupted word | `sup_E G_full < infinity` |

Both classifications hold for stationary-only guarantees and for guarantees over arbitrary initial laws. The upper proofs cover all starts; stationary sources already witness impossibility. Sparse or oscillating domains are included. [Histogram classification](../binary_certificate_adaptation_phase/KH002_histogram_domain_classification.md), [full-history classification](../binary_full_history_domain/AF001_full_history_domain_classification.md).

For the full-history positive direction, boundedness is equivalent to containment in a fixed union

    beta <= B/M²  OR  beta >= 1/(B M),   B >= 1.

Choose ordinary add-one in the first region and the balance gate otherwise. The selector uses the **actual supplied beta** and public `B`, but not `k`. Although each component rule is beta-blind, this combined selector is not generally beta-blind. The histogram positive result is stronger in that particular respect: the same ordinary add-one rule works on its permitted weak/strong union.

For `beta = M^(-gamma)`, `gamma >= 0`, the full-word ranges are `gamma <= 1` or `gamma >= 2`; the histogram ranges are `gamma <= 1/2` or `gamma >= 2`. Hence positional counts create a genuine separation throughout `1/2 < gamma <= 1`. The weak-certificate positive region is relative to the larger beta-dependent oracle benchmark; it does not mean that reducing the certificate makes absolute estimation easier.

## 5. A paid finite cut retaining the useful information

The positional statistic can be represented without granting a free history side channel. Fix a twelve-coordinate encoder: eight global triple frequencies and four first-half row **subfrequencies**, all normalized by `M`. A paid radius-three local table includes the public half-position indicator. A uniform causal head aggregates the twelve coordinates. With dyadic fractional precision `D = 2^P`, grid size `Q = 2^h >= 16`, and `P >= h`, its actual finite output is exactly

    a_i = floor(D A'_i/M)/D,

where `A'_i` is the relevant corrupted count. This is an identity for the specified integer evaluator, not an ideal-real softmax substitution.

After source editing, one vector perturbation satisfies `||eta||_infinity <= delta`, with `0 <= delta <= 1/4`; clipping to `[0,1]` and flooring to the `Q` grid follow. Only the twelve received labels, protected terminal pair, and public format metadata cross the cut. Counts, denominators, history and unexported state do not. The same rational gate ignores `k`, `delta` and `beta` and obeys

    R_all <= min{1, 2^16 s + 2^16/(M sqrt(beta))
                       + 2^23(k/M + delta + 1/Q)}.

For this **fixed encoder**, on `beta >= c/M`, matching lower bounds give

    R* = Theta_c(min{1, max{s, k/M, delta, 1/Q}}),

for both initialization conventions, even when competing decoders receive the budgets. The extra four ports require a fresh complete-message precision lower; an eight-port lower cannot simply be inherited. Below this band the proved upper/lower bracket is not asserted to match. [Finite-cut theorem and complete lower](../balanced_joint_finite_cut/BCJ001_theorem.md).

### What is paid

Let `N = M+3`, `ell = ceil(log2(N+4))`, numerical-record count `U = O(N²)`, and mask/metadata count `F = O(N² + N ell)`. With constant-size scalar descriptions `b = O(1)`, the full arithmetic width is

    w = O(P + ell + log(P+1) + log(U+F+2)).

The sequential multitape construction pays `O((U+F)w² + w⁴)` generation/conversion work and `O(N²(P+1)w²)` forward work. A safe encoder peak is

    O(Ub + UP + F + N ell + Nw + w⁴ + b + P).

These quantities include public positional tables, dense zero projections, masks, all-token evaluation, full products, accumulation guards, quotient remainders, scans and rewinds. Fractional precision is not total working-bit width. Terminal decoding uses `v = O(h+ell+1)` bits, `O(v²)` arithmetic work and `O(v)` data scratch, with a separately paid conservative `O(v⁴)` arithmetic-template allowance. The complete schedule sums work across generation, execution, handoff/cleanup and decoding, and counts all simultaneously live storage at phase overlaps. Optional all-token output or final grid rounding incurs its stated additional cost.

The cut is an abstract information-access contract, not a physical protection/noise device. These are conservative realizability bounds, not optimized computational costs, a fixed neural-depth theorem, or a lower bound for redesigned encoders.

## 6. Failed routes and remaining boundaries

Exact-run and near-prefix vetoes gave valid risk-increment bounds but did not by themselves remove the baseline estimator's corruption error. A concrete attack bypasses the fixed near-prefix wrapper around the small-budget threshold rule, retaining a harmonic excess of order `(k/M) log(M/k)` in the stated range. That is a failure of the particular wrapper, not an impossibility for all order-sensitive estimators. Occupation balance succeeds by controlling a different property of the path. [Exact-run partial result](../critical_beta_adaptation/CB001_long_run_veto_partial.md), [near-prefix partial result](../critical_beta_adaptation/CB002_near_prefix_veto_partial.md), [explicit bypass](../critical_beta_adaptation/CB003_fixed_veto_bypass.md).

Open boundaries include the sharp growing endpoint-window threshold, the least positional information needed, and matching finite-cut rates below the strong band. None of the results classifies arbitrary local encoders or trained architectures. The linked proofs underwent independent LLM mathematical review and finite diagnostic checks, not formal verification or external peer review. No external novelty certification is claimed. Exact source, review and acceptance bindings are collected in [the source map](SOURCE_MAP.json); this synthesis adds no new theorem or proof appendix.
