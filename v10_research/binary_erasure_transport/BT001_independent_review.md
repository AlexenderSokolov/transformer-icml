# BT001 independent review — PASS within stated conditional scope

Reviewer: independent child `independent LLM reviewer`, 2026-11-02. This is mathematical LLM review, not formal verification, acceptance, or prior-art certification. No frozen source changed.

## Verified independently before receipt of the draft

1. **Boundary obstruction.** For two long cycles and s short cycles, the uniform word law is equivalent to a uniform weak composition `(g0,g1,g2)` of s. Against the unique target `(01)^(s+3)`, the Hamming distance is exactly `2g1+3`. Hence expected cost is `2s/3+3=j/3+1`, where j=2s+6. Both words end in 01. A uniform expected-cost bound proportional only to the count change is impossible across *all* counts. This does not refute an interior-count bound.

2. **Modified witness.** For W=00,A=01,B=10,C=11 and rows `theta(1)=(a,p,1-e,e)`, stationarity is
   `Pi=x(e/a,1,1,p/(1-e))`, `x=(e/a+2+p/(1-e))^-1`.
   The two-step rows are
   - `((1-a)^2,a(1-a),a(1-p),ap)`;
   - `(e(1-p),(1-e)(1-p),p(1-e),pe)`;
   - `(e(1-a),ea,(1-e)(1-p),(1-e)p)`;
   - `(e(1-e),(1-e)^2,e(1-e),e^2)`.
   For M>=64, a=1/(2M), 1/M<=e<=1/16, p in [1/4,3/4], and beta<=e^2, every entry dominates beta times its stationary target mass. The potentially small entries `ea` and `e^2` are covered by x<=a/e and Pi_C<=1. The remaining small entries use e/4>=e^2>=beta or e(1-e)>=e^2>=beta. This is a new witness, not the unchanged BI001 source with theta_C(1)=1/2.

3. **Reference chain.** Setting active B→A and C→B deterministically gives cycles 01 and 101, with likelihood `(1-p)^s p^l`. At a fixed exact return horizon the law conditional on counts is uniform over cycle orders. Moreover `R^5(A,A)=2p(1-p)`, `R^5(B,A)=(1-p)^2`, and `R^5(C,A)=p`, so terminal-A probability is at least 1/16 for every horizon >=5.

4. **Necessary proof discipline for the conditional reduction.** Truncating an expected-cost transport should be handled by a small-neighborhood probability argument. Subtracting its constant TV failure probability directly from the finite-message risk bound `c/D` would not suffice. A common prior, parameter-free arrangement sampler, and exact protected last pair must remain explicit. The interior transport premise remains unproved and cannot be promoted to a binary logarithmic lower theorem.

Historical checkpoint: final draft review was pending at this point. The completed full review and final clarification-delta verification follow below.

## Full draft review, 08:57 UTC

Read `BT001_obstruction_and_reduction.md` in full after creation. **PASS for the stated obstruction, modified source, and explicitly conditional reduction; NOT a proof or acceptance of (T) or of the binary logarithmic lower.**

- The cheap adjacent-long merge cost and its nonuniform target density are correctly distinguished. The example `(s,l)=(1,3)` really gives target-gap density values 3 and 0 at `(4,0)` and `(2,2)`.
- The source's all-state certificate, stationary initialization, reference domination, protected endpoint, and common-prior semantics are correct.
- The simpler tail proof in the draft is valid: since every cycle lasts at most 3, the first `floor(t/3)` IID choices have completed by time t. Hoeffding controls both type counts without conditioning on terminal A. For large fixed t, subtracting its failure mass from the terminal-A lower bound gives the needed interior mass.
- Composition of adjacent count transports incurs expected Hamming cost at most the sum, by the triangle inequality and correct microcanonical intermediate marginals. The original-to-final distance truncation enforces the strict budget even if the composed path accumulated more edits. All targets still end in 01.
- `t>=2b/eta` and source counts at least `2eta t` keep every intermediate long count at least `eta t`. The map depends only on visible counts/horizon and chosen finite couplings, never on p.
- The probability-based finite-message argument survives truncation at constant failure probability. It does not subtract constant total-variation error from an `O(1/D)` risk.
- The lost low-horizon range and bounded k are legitimately absorbed into the separate `k/M` and clean `M^-1/2` baselines. A fixed absolute eta and its hypothesized C_eta are required; these constants do not depend on M,beta,k,p.

One minor clarification was requested: factorization should explicitly be conditional on **eligibility** and `(t,l0)`. To justify auxiliary randomness, sample original counts under their p-law; then generate Y from the common target law using U independent of p; finally generate X using the p-independent reverse disintegration of the chosen coupling given original counts and Y. This reproduces the original joint experiment. Conditional on U and decoder randomness, there are at most D candidate predictions. The truncation/eligibility events may depend on p,U,X; the neighborhood union bound remains valid because p and U are independent before selection. Thus this is a clarification, not a missing mathematical ingredient.

Independent finite diagnostics: 4,960 boundary words satisfy the exact distance identity; 45 rational-grid stationary/two-step certificates pass at beta=e^2. Output: `BT001_review_checks.json`. These corroborate the algebra but do not address the missing interior transport theorem. LP entries are correctly described as floating-point diagnostic optima, not rational certificates.

## Clarification delta verified, 08:58 UTC

Re-read the revised §4. It now explicitly conditions the ideal factorization on eligibility, gives the reverse-disintegration construction ensuring an independent arrangement seed, and enlarges C_eta to at least 1. These changes accurately implement the requested clarification and do not alter the conditional scope. **Final review status: PASS for the obstruction, source certificate, and conditional reduction; (T) and the binary logarithmic lower remain open. No review item remains pending.**
