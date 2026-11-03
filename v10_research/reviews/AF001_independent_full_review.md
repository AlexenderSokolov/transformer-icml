# AF001 — Independent full domain-classification review

2026-11-02. Reviewer: independent LLM reviewer.

**PASS recommendation for the frozen proof; root acceptance is separate.** No blocking mathematical, scope, metadata, initialization, or constant defect found. Reviewed final proof SHA256:

`17860bb034c34c388d12ccb83b942dc88fb4bf88ee15c2d7d63df099a230ebd4`.

The exact supplied-beta full-history criterion is boundedness on the public domain E of min(M² beta,1/(M beta)), with value zero at beta=0. It holds for stationary-only and arbitrary-initial-law guarantees, including unsupported starts. The upper selector may depend on the actual supplied beta and a fixed bound for E. It is not generally beta-blind. No author proof or acceptance record was edited.

## 1. Review scope, sources, and immutable evidence

I read the entire initial AF001 and the entire frozen revision, then its actual status-only diff. I read complete KA001, BK002, CB004, CB005, AB001, KH002, SC003, BT002 main and scalar proof. I also read the full KA001, BK002 and CB005 independent reviews. The new argument was reconstructed independently, not accepted from prior review conclusions. Existing deeper results are inherited at their explicit accepted interfaces; this is not a fresh recursive re-audit of every ancestor of SC003/BT002 or CB005.

The actual root receipts for KA001, BK002, CB004, CB005, AB001, KH002, SC003 and BT002 were read and programmatically checked against their proof bytes. All six receipt-specified review hashes and both BT002 component hashes match. In particular CB005's receipt really accepts the ALL-START bound used here, at proof `5e514451e88672533b5a376e43265b8a382ac0b59e816e3ef06212ea5be6db52` and review `b8976cae54be86f6b9c110f207256c38ec5c81913cc1156af0bd913cba47c57a`. CB004 alone would not license it. Old candidate/pending headers in immutable ancestors are superseded by their exact receipts, not silently edited.

The author confirmed final freeze. The independently saved `AF001_audit_snapshots/AF001_received.md` is identical to the final proof. The preserved original draft and actual diff show only CB005 dependency-status updates, not a changed formula or proof argument. The final binding manifest records all inspected direct proofs, receipts, relevant reviews, revision artifacts, independent checker/results and this review.

## 2. Experiment and benchmark

The model agrees with the accepted binary protected-endpoint experiment: integer M>=64, homogeneous order2 source, existential stationary pair law and ALL-STATE P²>=beta Pi, actual supplied beta in [0,1], strict pointwise k first-M edits, final pair unchanged, source-independent offline stochastic kernel, and unconditional TV at that true terminal row. The predictor sees full corrupted history and actual metadata, but not source, Pi, seed, mask, original interior or actual k.

At each fixed public pair the clean and every corrupted experiment use the SAME map. The uniform constant can depend on the whole fixed E, but not on its varying M,beta,k. The benchmark H_2 is exactly SC003/BT002's accepted capped known-k profile. At k=0 it equals M^-1/2; the logarithmic corruption term is not evaluated. Randomized predictors are permitted by the negative interface. Stationary witnesses are sufficient to refute the all-start guarantee, not vice versa.

## 3. Bounded-domain sufficiency and constants

For beta>0, min(x,y)<=B is equivalent to x<=B or y<=B. With x=M²beta and y=1/(M beta), this is precisely the asserted weak/strong union. At beta=0 the explicit zero definition agrees with the weak branch and avoids inverse-beta arithmetic. If the supremum is finite, take B>=max(1,sup G); no computability or effective recovery of B from arbitrary E is asserted or needed.

The weak-first branch M²beta<=B selects ordinary add-one. KA001 provides its all-start, all-budget bound with C_weak(B)=2^16+96(1+log B/2). Otherwise, on E, the union forces beta>=1/(BM). CB005's SAME balance gate then gives second term 2^16/(M sqrt(beta))<=2^16 sqrt(B)/sqrt(M). Together with its other two terms this is at most the asserted C_strong(B)H_2, where C_strong(B)=2^16(1+sqrt(B))+2^23.

For clarity, s<=1 and k/M<=1; H_2>=max(s,k/M) on the entire legal budget domain. More generally the capped-envelope argument in the manuscript is valid: min(1,A s+D epsilon)<=(A+D)min(1,max(s,epsilon)) for A,D>=0, A+D>=1. Thus neither the unit cap nor large k invalidates the comparison. The maximum of the two branch constants works uniformly. Overlap is resolved by weak-first; definition outside E creates no extra claim. The gate division is only evaluated at positive corrupted count, so both maps are total.

The algorithm does not estimate hidden mixing or choose a branch from clean counts. It uses the actual supplied label and public B; source parameters appearing in the bounds remain analysis-only. The orientations and threshold 512 match both frozen CB004 and CB005. All-start sufficiency is inherited solely from accepted KA001 and CB005, not a misuse of stationary reversal.

## 4. Arbitrary domains and subsequence extraction

If G is unbounded, choose a pair with G>=n for each integer n. Both positive terms are then >=n, so M²beta>=n and M beta<=1/n. Their product is M, implying M>=n². Consequently M tends to infinity, M²beta tends to infinity, and M beta tends to zero. This remains true for repeated horizons, multiple labels at one horizon, sparse sets, nonclosed sets, or wildly oscillating labels. No interpolation into an every-horizon curve is needed.

Eventually beta lies in [256/M²,1/(16M)] and M>=4096. Thus the exact finite KA001 inequality, not just its curve-summary wording, applies at each selected public pair. Integer floors are not asymptotic handwaving: k=floor(beta^-1/2) satisfies k sqrt(beta)>=3/4, k²>=4M, and k<=M/16<=floor(M/8). Hence all budgets are legal and the finite BK002 hypotheses hold.

These inequalities also give k/sqrt(M)>=3/(4sqrt(M beta)) tending to infinity and M/k>=M sqrt(beta) tending to infinity. With T=floor(M/8), log((T+1)/k) diverges. The other logarithm differs by log(2T/(T+1)), bounded between zero and log2 eventually. Its ratio to the first therefore tends to one. These conclusions do not require monotonic M or beta.

## 5. Actual certificate versus witness certificate

Write delta_sup=sqrt(beta), delta_wit=1/k. Generally these differ. Since k<=1/delta_sup, beta<=1/k². BK002's clean sources at witness certificate 1/k² therefore belong to the actual class D_2(beta). Its null certificate 1/M also dominates actual beta. The null's true target at 00 remains r=1/(2M); it is not replaced by beta. Source tables, stationary laws, and kernel are those of BK002, unchanged.

Fix the map A_(M,beta). BK002's ordered-word constrained-risk argument is universal over maps and so applies to this one. Its clean S and corrupted null risk both use this exact actual-beta map. Only class inclusion is used to license the assumed clean guarantee S<=C/sqrt(M). There is no assumed guarantee at the witness metadata, and knowing beta does not tell the map whether the actual budget was zero or k.

The kernel remains the common strict-k source-independent map: hardcoding a budget selected from the public pair in a lower-bound witness is allowed. The auxiliary source-like parameter is sampled, not read from the hidden source. The full-word likelihood comparison, protected endpoint and outcome-wise budget are preserved. Clean alternatives may depend on the selected attacked budget, because the clean guarantee is uniform over all sources in the actual class; the estimator may not change with that budget.

## 6. Quantitative contradiction

The inherited positive term is (3k/(2048M))log((T+1)/k), and penalty is 32S log(2T/k). Substituting S<=C/sqrt(M) gives their ratio at most

    (65536 C/3)(sqrt(M)/k) log(2T/k)/log((T+1)/k),

which tends to zero. Eventually it is at most one half, leaving positive lower bound (3k/(4096M))log((T+1)/k). The actual-beta profile is <=2k/M: its cutoff is sqrt(beta), k sqrt(beta)>=3/4 gives logarithm <=log(7/3)<1, and k>=2sqrt(M) covers the statistical term. Hence risk/H_2>=(3/8192)log((T+1)/k) diverges. The same finite C is contradicted even when it and the maps depend on E. The positive-part operation causes no issue once the penalty is less than half the positive term.

This proves simultaneous clean-and-all-budget nonadaptation only. It is not a failure statement for each individual positive budget, and does not substitute an advertised maximum for the realized budget. Necessity uses stationary witnesses and needs no CB005 premise.

## 7. Endpoints, blindness, and observation resource

At beta=0 the weak bound handles all sources/starts. Empty E is vacuous. Since G²<=M, bounded horizons have bounded G even with infinitely many beta labels; loss<=1 and H_2>=M^-1/2 independently confirm a finite constant. Finite exceptional horizons are therefore harmless. Oscillation between fixed weak and critical-strong bands is allowed, whereas an unbounded intermediate subsequence is fatal.

The power-law calculation is exact: exponents are 2-gamma and gamma-1; their minimum is nonpositive exactly for gamma<=1 or gamma>=2. Fixed valid positive multipliers enter B. Certificates outside [0,1] are not silently included.

For E_* containing beta=0 and beta=1/M at each M, G<=1 and the selector uses different public-label branches. AB001 indeed uses clean alternatives admitted at beta0 and its attacked null at beta1/M. Its full-history obstruction therefore rules out demanding one beta-blind map on this very union. The manuscript correctly avoids claiming a globally beta-blind rule merely because each component algorithm is beta-blind.

The upper needs only triple histogram, four first-half row counts and terminal pair; ordinary add-one needs a subset of these. KH002's exact histogram-plus-initial/final-PAIR criterion gives unbounded sqrt(M) at beta=1/M, so the separation stated is valid. This does not prove minimality of the four counts or any limitation for arbitrary richer encoders, boundary windows, networks, attention or computation.

## 8. Independent finite diagnostics and disposition

The new checker was written without reading or importing the author checker. The author later communicated aggregate counts; these were not used as code or correctness evidence. Every pass/fail assertion uses exact integers or rational arithmetic. The only logarithmic comparison tested uses exp(1)>1+1+1/2>7/3; no floating tolerance enters.

The run passed **57,615 assertions**, including 15,480 union equivalences, 4,020 squared strong-absorption checks, 4,680 exact finite-band floor/class/profile cases, and 135 independently constructed stationary witness sources. Of these sources, 102 use actual beta distinct from the witness certificate. All 2,160 matrix entries were checked against BOTH certificates. Large sparse exact sequence points through M=2^16384 corroborate the scaling identities without floating overflow. All eight root-receipt proof bindings, six specified review bindings and two component bindings pass; proof and snapshot hashes agree before and after.

Finite diagnostics are corroboration, not formal verification of limits or universal quantifiers; those arguments are reviewed above. Recommend accepting only the frozen hash with the supplied-beta selector, both-init scope, same-map clean/budget requirement, actual-label nesting and observation restrictions intact. No substantive revision is requested. This is independent LLM review, not external peer review, novelty certification, or formal proof checking.
