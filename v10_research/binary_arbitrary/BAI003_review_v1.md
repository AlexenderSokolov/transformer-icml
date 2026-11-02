# Independent review — BAI003 v1

2026-11-02. Reviewer: `independent LLM reviewer`, independently auditing the NEW BAI003 run-count lemma rather than importing BAI002 acceptance. Author file unchanged. This is an independent LLM review, not external peer review or formal verification.

## Verdict

**Main theorem PASS; one tiny auxiliary-proof endpoint repair requested before clean acceptance.** No substantive mathematical gap or counterexample was found. The claimed uniform no-log precision upper for all absorbing-diagonal binary sources, at M>=64, follows from the proof. The auxiliary lemma is claimed for M>=8, but the initial-B paragraph applies a bound stated for horizons>=8 at horizon M-1=7 when M=8. Add the direct observation that its integrand is at most1<=64/8 for M=8, and use the shift argument only for M>=9. This does not change any statement, constant, or source scope.

The exact reviewed files are bound in `BAI003_review_source_bindings_v1.json`.

## New lemma audit

### 1. Run duration laws and renewal coefficients

An A-run has duration2G_b-1; a C-run has durationG_t+1. Their displayed probability generating functions are correct, as is the product F. Complete cycle durations are positive and at least3, so the formal series sum F^k/k is coefficientwise finite at every order. L_n is nonnegative.

Discarding1/k bounds L_n by the probability of some cycle completion at n, because cycle completion events at a fixed n are disjoint across k. Starting at C, completion requires an A→C transition at the final step, giving the bound b. Starting at A instead, completion requires a C→B transition immediately before the final B→A transition, giving t. The two cycle-length laws coincide by convolution commutativity. The determinant identity and formal trace/log identity are valid; coefficient comparison gives exactly the displayed subtractions for the one-step C loop and two-step A/B loop. Stochasticity makes tr(R^n)<=3. Thus L_n<=min(b,t,3/n) is proved without a mixing estimate.

### 2. Geometric identity and exact terminal reductions

The identity

    g_q(r,N)/[q(N-1)] = g_q(r-1,N-1)/(r-1)

follows from binomial coefficients for N>=r>=2. The inequality using denominator1+q(N-1) is in the correct direction. Removing one A-run and one A visit lowers duration2N-r by1; removing one C-run and one C visit lowers durationN+r by2.

For terminal A, appending A→C multiplies the original path probability by b and makes the total completed A visits exactly J_A+1. Starting A yields k+1 A-runs and k C-runs, so the reduction contributes L_M for k>=1. The k=0 term is correctly indexed by even M. Starting C yields k of both run types; reduction leaves an extra C-run plus k-1 cycles, giving D_C L at M. The one-cycle term is correctly bounded by F at M+1.

For terminal C, appending C→B→A multiplies by t and adds two time steps. Starting C leaves cycles at M after reduction; starting A leaves an extra A-run, giving D_A L at M. The one-cycle term is at M+2. The k=0 initial-C term is t(1-t)^M divided by a denominator>=1, so the displayed upper is valid.

These manipulations concern complete independent geometric runs, not IID empirical samples selected by the endpoint. For fixed visit totals, the g probabilities aggregate all ordered run lengths with the correct multiplicities; no extra combinatorial factor is missing.

### 3. Uniform coefficient estimates

The point-mass estimates for long A- and C-runs imply F_n<=8/n for n>=4 with the stated convolution split. For D_C L and D_A L, the short-wait part costs6/M. On the long-wait part, M>=8 ensures l-2>=M/4 for C and (l-1)/2>=M/8 for A. Using L<=t or L<=b then gives the squared-rate exponential bounds. Their maxima are64/(Euler_e² M) and256/(Euler_e² M), below9/M and35/M. Hence15/M and41/M are valid.

The four initial-A/C cases actually cost at most5/M,23/M,4/M,49/M, so the common56/M is safe. The initial-B deterministic shift preserves the A/C prior-visit counts. For M>=9,56/(M-1)<=64/M is correct. The single M=8 endpoint needs only the trivial cap described in the verdict.

The conversion from q/(1+qj) to min(q,A0/(j+2)) is valid with factor2max(A0,1). Summing the two row bounds gives256max(A0,1)/M. Finite-horizon continuity legitimately extends the result to all b,t in[0,1] with uniform constants.

## Transfer and actual program audit

1. On any true terminal-active path, absorbing00 was never visited. The full-path density relative to the reflected chain is a product of1-e factors on B departures and is at most one. The actual endpoint and count functional are therefore dominated together; arbitrary initial mass at00 contributes no active term.

2. The B-row bound is correct: because00 is absorbing, a B→00 transition at M+1 is its first visit to00. Therefore eP(Y_M=B)<=P(J_(M+1)=0)<=16/(M+2). This is an unconditional actual-terminal occupation statement at the shifted horizon, not an endpoint-independent assertion.

3. BU001 v2 section4 supplies a historywise inequality, not a stationarity-dependent one. Its floor proof indeed extends to ANY chosen successor with true probability q: the floor displacement is bounded by min(p_hat,1-p_hat)<=p_hat and by the rounding-radius bound, then the truncation is1-Lipschitz. The four successor conventions used here are consistent. The statistical comparator remains the true source throughout.

4. The inherited allzero-bank bound64/z+16/M, final-rounding term3/Q, and empirical comparison2S+2B0 are unchanged. Combining256(6M/z+1)/M,16/(M+2), and the empty-bank terms gives1600/z+288/M. The numerical inequality to2^17/sqrt(M) at M>=64 is safe.

5. There is no hidden runtime count, run detector, virtual transition, reflected sample, or altered decoder. All new objects are analytical. The proof covers arbitrary b,t,e and initialization, including nonunique stationary classes at beta=0. It does not cover full-support sources or establish the general arbitrary-start square-root-beta theorem.

## Independent corroboration

`BAI003_review_diagnostic_v1.py` independently computes exact finite-horizon distributions of `(Y_M,J_A)` and `(Y_M,J_C)` by dynamic programming and compares them against the proposed run-coefficient bounds. It tests8 interior parameter pairs, including rates1e-6 and near-one rates, at horizons8,9,16,31,64,100 and all initial active states. All192 nontrivial initial-A/C coefficient comparisons passed, with no positive excess. The maximal observed ratio to the coarse64/M target was below0.044. The deterministic initial-B cases were also computed. This is finite floating-point corroboration, not proof.

## Required local repair

Add one sentence before the initial-B shift calculation: for M=8 the left side of the separate bound(2.2) is at most1<=64/M; assume M>=9 for the remaining shift. No theorem weakening, constant change, or new hypothesis is required. A versioned delta review can close this textual endpoint issue.
