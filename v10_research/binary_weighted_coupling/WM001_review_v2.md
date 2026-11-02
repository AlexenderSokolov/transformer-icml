# WM001 independent delta review v2

2026-11-02. Reviewer: separately dispatched child `independent LLM reviewer`. **PASS for the strengthened method-obstruction lemma.** V1 review and artifacts are preserved. This is an independent LLM audit, not formal verification, root acceptance, or external peer review. No manuscript edit made.

## Delta and exact checks

V2 appends Section 6 to the previously reviewed v1 proof. The new full-support family is a=ε,b=h,e=1/2,t=εh with 0<h≤ε≤1/32. Independent symbolic multiplication confirms π=(1/2,ε,ε,1)/(3/2+2ε) and all sixteen displayed two-step ratios. Every ratio divided by D' is at least h²; the A,B cell equals h². Therefore the exact maximal certificate β*=h²D' is correct, including all source states.

The domain inequality εh≥h² uses h≤ε, an essential and explicitly stated hypothesis. Other cells also satisfy the claimed bound throughout the stated domain. The minority vector (ε,h,1/2,εh) is exact.

## Probabilistic argument

Reflecting A→C into A→B produces the stated three-state chain. Its crossing-state probabilities satisfy r_A(k)=εr_W(k−1)+r_A(k−2)/2 for k≥2, with initial values 0 and ε, so both crossing probabilities are at most 2ε. Independent h-marks on reflected A departures give separation probability at most 2nεh. This is the same valid first-separation coupling used in v1, without assumptions about the original process after separation.

At n=floor(1/(16εh)), n≥64, 4ε≤1/8 and 2nεh≤1/8 imply P^n(W,W)≥3/4. Also π_W≤1/3, so the deviation is at least 5/12. Keeping the W contribution gives marginal residual at least 5ε/12 and future-weighted residual at least (5/12)(3/4)ε=5ε/16. These constants are correct.

## All-power consequence and scope

For an arbitrary fixed α>0 choose fixed k≥1 with α(k+1)>1 and set h=ε^k. This respects the parameter domain. Then n~ε^(−k−1)/16, while n sqrt(β*)~sqrt(3/2)/(16ε). Thus n^(−α)=o(ε) and the proposed square-root-beta exponential is also o(ε). Both endpoint residuals remain Ω(ε), refuting every such universal fixed-polynomial-remainder inequality. In particular the statistical-floor remainder n^(−1/2) cannot repair the coupling strategy. Using total horizon 2n leaves the contradiction unchanged.

This statement concerns endpoint/midpoint residuals only. It does not establish a decoder-risk lower bound or settle the arbitrary-start precision frontier, as the manuscript correctly emphasizes. The initial W visits remain available to a count-sensitive proof.

## Independent verification artifacts

`WM001_review_checks_v2.py` verifies symbolic stationarity and the entire table, then certifies all sixteen domain inequalities by ε=1/(32+u), h=1/((32+u)(1+v)), u,v≥0. Each difference numerator and denominator has nonnegative polynomial coefficients, with a positive denominator constant term. This covers the complete parameter domain, not just grid points. Exact rational matrix-power checks pass at (ε,h)=(1/32,1/32),(1/32,1/64),(1/40,1/40), with horizons 64,128,100. Results and reviewed hashes are in `WM001_review_checks_v2.json` and `WM001_review_bindings_v2.json`.

No mathematical defect or required revision found. Recommend root acceptance of v2 as the stronger method-obstruction unit, preserving the open status of the precision upper.
