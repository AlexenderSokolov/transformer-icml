# WM001 independent review v1

2026-11-02. Reviewer: separately dispatched child `independent LLM reviewer`. **PASS for the stated method-obstruction lemma.** This is an independent LLM audit, not formal verification, root acceptance, or external peer review. Manuscript unchanged.

## Verified claims

1. The displayed kernel is the genuine binary pair kernel, with all four row parameters strictly between zero and one on 0<ε≤1/8. The stated stationary law is positive and satisfies πP=π.
2. Direct multiplication confirms all sixteen entries in the ratio table. Its denominator is Dπ_j (the unnormalized stationary vector), so multiplying its minimum ε² by D gives exactly β*=ε²D. The three binding cells are correct. All other entries dominate ε² throughout the stated domain, not merely on the numerical grid.
3. For the reflected active chain started at C, r_A(k)=r_B(k−1), and the displayed two-step recursion bounds both crossing probabilities by 2ε. Consequently r_C(k)≥1−4ε.
4. A valid coupling uses an independent ε-mark on each reflected B departure. Before the first mark, the original and reflected chains agree. The probability of any such mark within n steps is at most ε times the expected number of reflected B departures, bounded by 2nε². The original chain's post-separation behavior is irrelevant. This justifies (3) without imposing an absorbing boundary on the full-support original kernel.
5. With n=floor(1/(16ε²)), the finite-horizon constants hold: P^n(C,C)≥3/8, π_C≤1/16, and the difference is at least 5/16. The minority vector is exactly (ε³,1/2,ε,ε).
6. Keeping the C term proves marginal lower bound 5ε/16. Keeping the C term twice, using (P^nq)(C)≥q_CP^n(C,C), proves future-weighted lower bound 15ε/128. No independence or replacement of the future factor is assumed.
7. Since n~1/(16ε²) and sqrt(β*)~ε, each proposed O(1/n)+O(exp(−c n sqrt(β*))) bound is o(ε), for any fixed positive constants. Replacing the total horizon with M=2n only changes constants. Thus both proposed uniform endpoint inequalities are rigorously refuted within full stationary support.

## Scope audit

The manuscript properly distinguishes these false endpoint/midpoint-transfer estimates from the open precision frontier. It does not lower-bound SB001 error or claim a new minimax separation. Initial active trajectories can carry large occupation counts, so the obstruction does not justify discarding count-sensitive renewal approaches. No boundary-support shortcut or unsupported square-root spectral-gap assertion is used.

## Independent evidence

`WM001_review_checks_v1.py` independently builds P and π, verifies symbolic stationarity and the full table, and certifies each table entry minus ε² as nonnegative on 0<ε≤1/8 by the substitution ε=1/(8+v), v≥0: numerator and denominator polynomials have nonnegative coefficients, with positive denominator constant term. It also checks (4)–(6) using exact rational matrix powers at ε=1/8,1/10,1/16 (including a non-dyadic horizon). All checks pass. The output is `WM001_review_checks_v1.json`; the exact reviewed artifact hashes are `WM001_review_bindings_v1.json`.

No mathematical defect or required revision found. Recommend root acceptance **only as a method-obstruction result**, leaving the arbitrary-start precision upper open.
