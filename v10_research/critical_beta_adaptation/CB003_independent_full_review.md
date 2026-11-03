# CB003 — independent full review of the fixed-veto bypass

2026-11-02. **PASS, no proof revision requested.** This is an independent LLM mathematical review plus finite exact diagnostics, not formal verification or external peer review.

## Scope and reading

I read the entire `CB003_fixed_veto_bypass.md` and checked the exact definitions of AB003's active hard-threshold estimator and CB002's near-prefix modification in their accepted sources. I also checked the accepted SC003/BT002 comparison profile and the four corresponding intake receipt hashes. I did not re-review those inherited theorems in full in this review. CB003's source certificate, kernel, exact ordered-word counts and lower-bound calculation are proved within CB003 and were independently audited here. The received proof snapshot is `review_snapshots/CB003_received.md`.

The conclusion is only failure of the specific composition W(AB003) over all budgets at beta=1/M. It does not exclude other full-history estimators and does not contradict CB002's risk-increment bound.

## Complete proof audit

1. **Edit locations and legal budget.** The prefix edit block3,...,h+3 has h+1 positions. The stated large-M domain places it strictly inside the initial all-one run and the first n+1 symbols, with unchanged ones on each side. The suffix edits are at zero-run positions3,6,...,3ell. Since3ell<=t-1, they leave suffix positions t and t+1 unchanged. Their global positions are at most M. The two edit sets are disjoint and their total cardinality is at most k/32+k/4<k. Recognition of the one-flip input words and the ensuing edits form one deterministic map, identity elsewhere, with no unknown source parameter as input.

2. **Veto disabled.** The original prefix has no zeros. The suffix begins after the tested prefix and does not affect its count. The edited first n+1 symbols therefore contain exactly h+1 zeros, so the terminal00 branch of W does not activate. The terminal11 branch is irrelevant because the endpoint remains00.

3. **Exact terminal-row counts.** Originally there are t-1 triples000 and no001. A new internal zero block of length h+1 contributes h-1 triples000 and one001, adding h row00 departures and one designated exit. Each isolated suffix one changes three previously000 triples to001,010,100. Spacing three makes these affected triple sets disjoint, including for adjacent inserted ones in that spacing scheme; the first affected suffix triple starts at the first zero, beyond the original mixed boundary triples. Each inserted suffix one adds one designated exit and removes two row00 departures. This gives exactly C'=ell+1 and J'=t-1-2ell+h.

4. **Prediction and pointwise loss.** The numerator is at least k/4>=16h>12h, so AB003's active branch is indeed used. The denominator is positive and at most2t. Hence qhat>=k/(8t). Since t<=M/8 and k>=1, r<=k/(16t), yielding loss at least k/(16t). Because W is disabled, this is the actual W(AB003) prediction, not a histogram surrogate for a different estimator.

5. **Null, unconditional probabilities and harmonic sum.** The symmetric first-order source has stationary pair law T_r/2. Its two-step pair transition ratio to that law is2T_r(v,s)>=2r=1/M for all16 pairs. The one-flip word probability is (r/2)(1-r)^M, including its initial-pair factor. Bernoulli's inequality gives the common lower bound1/(8M). The input events are disjoint. Multiplying their pointwise loss lower bounds, summing and using the decreasing-function integral gives exactly the displayed k/(128M) logarithmic lower bound. The target is always the true law at the original protected00 endpoint; no conditional-IID assertion is needed.

6. **Failure of this candidate.** At beta=1/M and k>=sqrt(M), the accepted comparison profile is at most2k/M by log(1+x)<=x. For k=floor(M^(3/4)), every finite-domain condition eventually holds and log((T+1)/k) diverges. The resulting unbounded ratio proves the claimed candidate failure. It remains a legal maximum-k witness even though this particular map uses fewer than k edits.

No substantive or statement-scope defect was found. In particular, the closing discussion correctly distinguishes loss remaining in the baseline from harm caused by adding a veto.

## Fresh independent exact checks

`CB003_independent_checks.py` passed using exact integers and Fraction arithmetic:

-28 materialized large-domain words, including M=2^20, non-square nearby M, and M=2^22;
-7,710 smaller geometric instances of the exact count identities;
-100 identity-branch recognition tests;
-all16 certificate entries for four null tables (64 entries total), plus stationarity;
-233 exact small-M full-word probabilities including the initial-pair factor;
-28 checks of the large-budget profile domain;
-four accepted proof/receipt hashes.

The large-word tests independently count all overlapping triples, verify exact prefix counts, Hamming distance and protected symbols, and compute the estimator and loss as exact fractions. Giant rational powers are not materialized: the large-M word-probability lower uses the independently audited analytic Bernoulli argument. The saved finite checks corroborate tested instances only and do not replace the universal proof above.

The received and reviewed proof bytes are identical; no revision was necessary.
