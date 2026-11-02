# AB001 / AB002 — Independent full mathematical review

Date: 2026-11-02. Reviewer role: independent LLM reviewer, not the author. **Verdict: PASS, with the exact scope below.** No mathematical revision is required for the reviewed versions. This is an independent LLM mathematical review plus finite diagnostics, not formal verification, external peer review, or a novelty certification.

## Reviewed versions

- `AB001_joint_blindness_obstruction.md`: SHA256 `865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d`.
- `AB002_addone_failure_and_open_beta_known.md`: SHA256 `7848267fa73e33775ca2aa467230980ee5f89e1d5ae0ae140c0d7955909d219b`.

The first draft IDs collided with an earlier bounded-attention result. I independently diffed the preserved original drafts against the renamed AB001/AB002 candidates: only result IDs, equation labels, and internal references changed, with no mathematical delta. This review and the rerun diagnostic bind the renamed authoritative candidates above.

I read both files completely, independently rederived their probability and counting identities, and wrote a separate exact-rational diagnostic rather than relying on the author's checks. I also inspected the accepted SC003/BT002 receipts and the relevant clean-occupation, stability, beta=1 row-domination, and pooling interfaces in `source_corruption_manuscript/nonbinary_endpoint.tex`. The new negative arguments are self-contained; the old interfaces are used only to identify the comparison rate and the two stated adaptive endpoint regimes.

## 1. Exact accepted scope

AB001 proves an obstruction to **one map independent of both k and beta**, even for stationary initialization, in the binary full-corrupted-history experiment with a strict offline Hamming budget and the actual final pair protected. Its finite constrained-risk inequality is valid for every randomized estimator, with no fixed-histogram or computational restriction.

AB002 proves that ordinary selected-row add-one has an unbounded logarithmic loss relative to the known-k profile at beta=1/M. This remains a failure of that estimator when beta is supplied, because the estimator ignores beta.

Neither result establishes impossibility or attainability of k-blind adaptation for a supplied intermediate beta. The author explicitly retains that question as open. The two clean source families in AB001 are not silently placed in the same advertised beta class.

## 2. Membership, stationarity, and source probabilities

For Q_a, the claimed stationary vector follows from the equal crossing masses and the two exact flows

    Pi_00 a = Pi_10(1-a),  Pi_11 r = Pi_01 [r(1-a)/a].

On a in [1/M,1/4], the parameters are legal and all stationary coordinates are positive. Beta=0 imposes no further all-state condition. The argument does not need or assert a positive certificate for these alternatives.

For Q_*, the first-order pair identity

    P_*^2((u,v),(c,d))/Pi_*(c,d)=2 T_r(v,c)

shows the minimum ratio is exactly 2r=1/M on all sixteen pairs of states. Thus the null is in the intended positive-beta class with stationary initialization, not merely with a support-restricted minorization.

A one-flip word has N-1=M+1 first-order transitions, exactly one flip and M non-flips. Its probability is therefore (r/2)(1-r)^M. The lower bound 1/(8M) follows from the elementary Bernoulli inequality. The clean prefix probability has exponent M-t-1, and division gives exactly (1-r)^(t+1)/(1-a). The off-by-one choices in the two word probabilities agree with the M departures and the N=M+2 symbols.

## 3. Kernel permissions and full-history comparison

The AB001 kernel is defined on every input word, using identity outside the specified one-flip words. Its auxiliary parameter a and continuation law depend only on public M,k, the observed suffix length, and private randomness. The constants r and b_a are construction parameters, not unknown source information read from an oracle. The same map remains a legal map when applied to any source.

Every accepted suffix differs from the original zero suffix exactly at its emitted ones. The count test imposes <=k replacements on each realization. The terminal-pair test leaves the last two bits 00, hence excludes edits at positions M+1 and M+2. This remains correct at t=1, where the first zero is itself one protected terminal symbol. Rejections are identity. The proof is not an expected-cost argument.

The output is a full sampled word, and e_(a,t) evaluates the estimator on that full word with its complete original prefix. No fixed statistic or histogram sufficiency claim is used. In the null risk, the target remains the null row value r at the true terminal pair 00. The clean alternative target a appears only in a valid triangle inequality.

## 4. Acceptance estimate and randomized estimators

The reference process starts with last bit 0, emits a one with probability a only after a zero, and never has consecutive ones. Its expected number of emitted ones is at most at, and its terminal-00 probability is at least (1-a)^2 (or the stronger 1-a when t=1).

Before the first coupling disagreement, a possible 01->11 event follows an emitted one. Independent auxiliary transition marks give disagreement probability at most b_a times the reference expected number of emitted ones, bounded by r(1-a)t<=1/16. Combining this with the <=1/4 budget-failure bound and >=9/16 endpoint probability yields acceptance >=1/4. This argument does not condition reference successors on their final context.

Since a>=2r, accepted losses satisfy the required mean bound a/8-e_(a,t). Dropping rejected losses is legal because TV is nonnegative. An independent estimator seed can be averaged at every stage; there is no hidden shared randomness with the corruption kernel.

## 5. Integrated constrained-risk inequality

For each fixed a, first-zero events are disjoint and their terminal-00 clean losses are nonnegative parts of the same unconditional clean risk. Therefore sum_t w_(a,t)e_(a,t)<=S_M(A) is sound.

The auxiliary intervals have density 8t/k, mean 3k/(16t), and lie inside the family parameter range. On a in I_t, 8t/k<=2/a. Combining this with v_t<=4w_(a,t)/3, then exchanging the finite sum and nonnegative integral, gives the full negative term bound

    (8/3) S_M(A) integral_[k/(8T),1/4] da/a
      =(8/3)S_M(A)log(2T/k).

This is the substantive common-integration step: the proof does not subtract one clean risk from unrelated parameter-specific experiments. The positive coefficient 3/1024 and the harmonic lower log((T+1)/k) are correct. Taking the positive part is justified by nonnegativity of risk.

For k=floor(M^(3/4)), the ratio of the clean penalty to the positive term vanishes under S_M(A)<=C/sqrt(M). Meanwhile at beta=1/M the known-k profile is <=2k/M for large M. Thus the claimed logarithmic contradiction follows with the same estimator used for k=0,beta=0 and for the positive-budget null. It does not connect different maps A_(M,beta), nor different maps indexed by a supplied k.

## 6. Independent audit of AB002

The k flipped offsets 3j-1 are separated by two zeros and stop before the final pair. Each flip removes two distinct terminal-row 00 departures and creates one 001 departure. I independently enumerated the resulting full strings and verified

    J'=t-1-2k, C'=k.

The add-one prediction, its lower loss bound k/[2(t+1)], and the harmonic integral yielding (AB2) follow. No corruption of a selected-query row or a hidden clean count is assumed in the algorithm; clean counts only describe the counterexample.

The failed-route note correctly identifies P^2(01,10)=b*r as the obstruction. The stationary Q_a family has the exact ratio 2r^2(1-a)/a^2, so beta=2r would require a^2<=r(1-a). This rules out the large-a alternative range needed by the same-beta version of this construction. It is appropriate to preserve this as a failure rather than claim a stronger adaptation impossibility.

The beta<=M^-2 regime follows from generic pathwise count stability, universal terminal occupation, and the accepted clean add-one interface, all valid for K=2. The beta=1 pooling regime follows from all-state row domination, which forces every next-symbol law to be the same; generated symbols from position 3 onward are IID even with an arbitrary initial pair. These ancillary statements are consistent with the reviewed source interfaces.

## 7. Independent diagnostics and limits

`review_joint_blindness_checks.py` produced `review_joint_blindness_checks.json` with PASS:

- 6 exact all-state null-certificate checks;
- 270 exact alternative-stationarity and likelihood/density identities;
- 270 exact dynamic-programming acceptance probabilities, minimum tested value 9/16 (the theorem uses the weaker 1/4);
- 76,656 exact full-word strict-budget, endpoint, count, and add-one-loss checks;
- 90 floating-point harmonic/log diagnostics, separately labeled.

The probability, matrix, count, and loss checks use rational arithmetic. Tested M values and ranges are stated in the script. These finite checks corroborate the independently reviewed proof but do not replace its universal arguments. Root acceptance and any incorporation into a new manuscript remain separate actions.
