# BK001 — Fresh independent full audit

**Verdict: no substantive defect found in the specified version.** The finite constrained-risk inequality (BK1) and its supplied-beta, unknown-budget **histogram-only** impossibility consequence are supported by the complete audit below. This is a recommendation for the root to consider, **not acceptance**. It is independent LLM corroboration, not formal verification, external peer review, or a novelty assessment.

Review date: 2026-11-02 UTC. Candidate SHA256:

`edbfc9cd372df7497ff7462eded0e6c85a3ee4f99f21bd7310f460bd1f0fcb5a`

Candidate: `BK001_histogram_adaptation_obstruction.md`. The reviewed version uses the elementary rational endpoint-mixing bound in §4. I initially read the preceding exponential version, then reread the changed argument and checked this stabilized hash. No proof file was edited. The author diagnostics were not read or reused; the independent script was written from the theorem and independent calculations.

## 1. Scope, interfaces, and acceptance provenance

I read the complete BK001 proof, complete AB001–AB003 manuscripts and their acceptance receipts, complete SC003 manuscript, and BT002's main and scalar manuscripts and receipt. The exact source/receipt hashes are included in `BK001_independent_checks.json` and `BK001_independent_review_bindings.json`; the script verifies that the accepted proof files still match their receipts.

The inherited experiment is a binary second-order source on `N=M+2` symbols. Its pair chain has `M` departures; the actual final pair is protected, and loss is unconditional binary TV, hence absolute error in the predicted probability of symbol 1. An admissible offline stochastic corruption kernel is a single map on all full input words, changes at most `k` of the first `M` symbols on each realization, and does not receive the unknown source parameter. BK001 restricts the predictor, but not that adversary, to the exact eight triple counts and the initial/final pairs. Estimator randomization remains allowed and private.

The accepted known-budget profile is

`H2=min{1,max{M^(-1/2),F2}}`,

where `F2=0` at `k=0`, and otherwise

`F2=(k/M)[1+log(1+1/(k max(sqrt(beta),1/M)))]`.

SC003's known-k upper estimator already uses only triple counts and the final pair. BT002's full-history lower remains valid when predictors are restricted. Thus using the same known-k profile for the histogram-restricted comparison is legitimate; no extra benchmark gap is being hidden. BK001 needs only this interface, not a new proof of either accepted result.

AB001 excludes joint blindness to k and beta for full-word predictors, but its clean alternatives do not all share the null beta. AB002 explicitly leaves the supplied-beta problem open. AB003 gives a joint-blind histogram estimator through square-root budgets. BK001 uses `k=n^9`, `sqrt(M)=n^5`, so does not contradict AB003. Its new obstruction does not solve the supplied-beta problem for unrestricted full-word predictors.

## 2. Parameter domain and stationary flow

For every integer `n>=4096`, `M=n^10`, `k=n^9`, and every integer `k<=j<=floor(M/8)`, all parameters are exact rationals. `k<=floor(M/8)` holds since `n>=8`. Also `delta^2=beta=1/M`, `x=c/n`, and `y=j/M` is in `[1/n,1/8]`.

The elementary bounds used in the manuscript hold:

- `0<delta<=1/4`, `e=1-delta>=3/4`;
- `0<a=c k e/j<=c<=1/4`;
- `a>=8c e/n>=4c/n>=n^(-5)=delta`;
- `w=1-y-2x>=3/4`, and `w<=1`;
- `0<t=x delta/w<=1/4`.

For the pair-state order `00,01,10,11`, the transition matrix independently reconstructed from the next-symbol probabilities is

```
P = [1-a, a, 0, 0]
    [0,   0, e, delta]
    [e, delta, 0, 0]
    [0,   0, t, 1-t].
```

The equations `ya=xe`, `wt=x delta`, and `e+delta=1` give all four stationary coordinates:

`Pi P=(y(1-a)+xe, ya+x delta, xe+wt, x delta+w(1-t))=(y,x,x,w)`.

All stationary masses are positive. Neither the probability parameters nor the expected counts must be integers. In particular, `E Jcross=2ck` is generally nonintegral for odd n. The argument never treats this expectation as an attainable deterministic count or requires an integer number of prescribed transitions. The exact diagnostics explicitly include such odd-n cases.

## 3. Every all-state certificate entry

Multiplication gives exactly the displayed sixteen-entry `P^2`. To audit the inequalities without relying on an incomplete list of entries, divide column v by `beta Pi(v)=delta^2 Pi(v)`. Using the stationary identities, the resulting ratio matrix is

```
[(1-a)^2/(delta^2 y), (1-a)e/(delta^2 y), e^2/(delta^2 y), a/(delta w)]
[e^2/(delta^2 y),    e/(delta x),         1/w,              (1-t)/(delta w)]
[e(1-a)/(delta^2 y), e^2/(delta^2 y),     e/(delta x),      1/w]
[a/(delta w),       1/w,                 (1-t)/(delta w),  (1-t)^2/(delta^2 w)].
```

Every entry is at least one: `w<=1`, `a>=delta`, `e,1-a,1-t>=3/4`, `delta<=1/4`, `x<=c<=1/4`, and `y<=1/8` suffice. In particular, the small two-step cross entries really are covered by `1/w`, not omitted or replaced by a stationary-only assertion. No initial-state restriction is used.

For the symmetric first-order null, `Pi_*(s,t)=T_r(s,t)/2` and

`P_*^2((u,v),(s,t))/Pi_*(s,t)=2T_r(v,s)>=2r=1/M`.

This is all-state as well, with equality for an appropriate flip. Its row-00 target is `r`. The phrase “same beta” means the same valid advertised lower certificate, not that every alternative's maximal minorization constant must equal beta; the experiment requires the former.

## 4. Three-step atom, stationary variance, and conditioned endpoint mass

The four specified paths into 11 have probabilities

`(1-a)a delta`, `delta(1-t)^2`, `ea delta`, `(1-t)^3`.

Each is at least `a delta/2`. Since `a>=ck/(2M)`, this is at least

`lambda=ck/(4 M^(3/2))=c/(4n^6)`.

Thus `P^3=lambda delta_11+(1-lambda)R`, with a valid Markov remainder and `0<lambda<1`. For h steps, apply contraction over `floor(h/3)` three-step blocks, and contraction/nonexpansion over the remaining steps, comparing with the invariant Pi. This gives the stated uniform TV bound `alpha_h=(1-lambda)^floor(h/3)`. It is a property of this explicit family, not a general square-root-beta mixing theorem.

In stationarity,

`Cov(1_D(Y0),1_D(Yh))=sum_(u in D) Pi(u)[P^h(u,D)-Pi(D)]`,

whose absolute value is at most `Pi(D) alpha_h`. The exact infinite sum is `3/lambda-1`; the paper's upper `3/lambda` is valid. The usual covariance expansion therefore gives `Var(J_D)<=7M Pi(D)/lambda`. It covers both the singleton 00 and the union `{01,10}` and does not assert independent visits.

For the stabilized endpoint argument, Bernoulli's inequality gives `(1-lambda)^m<=1/(1+m lambda)`. As `floor(M/3)>=M/4`,

`alpha_M<=1/(1+c n^4/16)`.

For `n>=64`, `n^3>=32/c`, so this is at most `1/(2n)<=y/2`. Hence `P^M(11,00)>=y/2`, and multiplication by the stationary initial probability `w>=1/2` yields

`P(F_j)>=y/4=j/(4M)`.

This probability is small near the lower endpoint j=k; it is **not** treated as constant. The conditional clean error bound `4SM/j` follows by restricting the unconditional risk to `F_j`, where the genuine target is exactly a_j. No prior is conditioned to remain uniform, and no conditional stationarity is asserted.

## 5. Canonicalization and fixed-null-length distance

A word gives a directed pair-graph path from 11 to 00. Deleting a self-loop leaves its vertex unchanged, so removing the 111 and 000 edges preserves the entire remaining legal path in its original order. This is an explicit construction; it does not rely on existence of a newly chosen Euler trail or a source-dependent shuffle.

Prepending all deleted 111 loops and appending all deleted 000 loops yields a length-N word with identical eight triple counts and the same initial/final pairs. If `L1=N111`, `L0=N000`, and `E=M-L0-L1`, the reconstructed word is

`1^(L1+2) [E emitted skeleton bits] 0^L0`.

For the baseline `1^(N-L0)0^L0`, only those E skeleton positions can differ. This comparison is also valid when `L0=0`; the baseline is merely an intermediate Hamming-space word and need not have the final pair 00. Two monotone words with L0 and j terminal zeros differ at exactly `|L0-j|` positions. Consequently the first distance bound holds for the **fixed pre-sampling** null word `x^(j)`.

The pair-path endpoint imbalance gives `N100=N001+1` and `N011=N110-1`. Therefore, writing `U=N001`, `V=N110`,

- `U<=J10-1`, `V<=J01+1`, hence `U+V<=Jcross`;
- `E=U+V+Jcross<=2Jcross`;
- `L0=J00-U` and `U<=Jcross`.

These prove `d_H(Can(X),x^(j))<=3Jcross+|J00-j|` without identifying random sample occupations with j. This is the needed correction to the dangerous variable-null-length shortcut: the clean sample is always of length N, and its random loop/occupation mismatch is explicitly paid.

The independent diagnostics enumerate all 131,071 binary words with initial 11/final 00 of lengths 4 through 20. They verify valid edge reconstruction, exact histograms, all flow identities, and 2,097,153 comparisons with fixed null suffix lengths `2<=j<=N-2`. This corroborates, but does not replace, the general argument above.

## 6. Conditional concentration and constants

The expectations used for Chebyshev are **unconditional stationary** expectations, `E J00=j` and `E Jcross=2ck`. They need not equal the bridge's conditional means. For each bad event, the proof first bounds its unconditional probability and then divides by the positive lower bound on `P(F_j)`. This is valid irrespective of correlation with the endpoints.

For J00, variance and threshold k/4 give

`P(|J00-j|>k/4 | F_j) <= (7My/lambda)(16/k^2)(4/y)`

`=448M/(lambda k^2)=1792 M^(5/2)/(c k^3)`.

For Jcross, `2ck<=k/32`, so exceeding k/16 entails a deviation greater than k/32. The corresponding calculation is

`(14Mx/lambda)(1024/k^2)(4/y)`

`=229376 M^(5/2)/(k^2 j) <=229376 M^(5/2)/k^3`.

The signs of strict inequalities and possible nonintegrality of means or thresholds cause no difficulty for Chebyshev. Since `M^(5/2)/k^3=n^(-2)`, the union bound at the smallest allowed n is exactly

`(1792/c+229376)/4096^2=231/512<1/2`.

Thus the proof actually supplies success at least `281/512`; its weaker one-half is valid. On G_j, the deterministic distance is at most `3k/16+k/4=7k/16<k`.

No massive-horizon conditional path distribution was numerically enumerated. The probability statement is established by the analytical argument; the exact diagnostics independently reproduce its rational constants and finite inequalities.

## 7. One source-independent strict-k kernel

The null recognition event is unambiguous because different integer j give distinct words. The attack uses only the observed word, public M,k,c and j read from that word. Its Q_j is a public auxiliary law; it is not supplied the actual source law, actual stationary law, or an unknown clean path. The same map can be applied under every source and is identity off the recognized null words.

Conditional sampling is well-defined because `P(F_j)>0`. Every transition/initial probability is rational, and finite path probabilities remain rational after conditioning. An enormous finite table suffices; no efficiency assertion is required. There is no requirement that expected occupation values be integers.

Every canonical candidate shares the input's initial pair 11 and final pair 00. The explicit distance test enforces `d_H<=k` realization by realization, and the two protected final positions never change. Rejection is identity. Rearrangement of the sampled auxiliary clean word is not granted as a free adversarial operation on the actual null input: its entire resulting Hamming distance to that input is charged and tested.

Preservation of the initial pair is stronger than required by the corruption model, but necessary here to preserve the predictor's stated statistic. The exact equality `T(Can(X))=T(X)` also holds for randomized histogram estimators after averaging their independent seeds. It need not hold for predictors that see the order of the full word; this is the unique information restriction used in the lower-bound transfer.

## 8. Unconditional risk, source supremum, and sign control

A null word has initial probability `(1-r)/2` for 11, exactly one flip among its M subsequent transitions, and M-1 nonflips. Thus its probability is

`v=(r/2)(1-r)^M>=1/(8M)`

by `(1-r)^M>=1-Mr=1/2`. It is the **same** v for every j. All these events are disjoint. There is no off-by-one error from the `j` terminal symbols convention.

On accepted auxiliary samples, triangle inequality gives loss at least `(a_j-r)-clean_error`. Here `a_j>=delta>=2r`, and success has mass at least one-half. Hence its averaged positive contribution is at least `a_j/4`, while the accepted clean-error contribution is at most the full conditional clean error. Rejected losses and all other null events are nonnegative. Therefore

`E[null loss | x^(j)] >= [c e k/4-4SM]/j`.

S is the supremum over the finite family of unconditional clean risks. Applying its bound separately at each j is legitimate; each resulting conditional error is explicitly multiplied by the appropriate `M/j` cost. The aggregate error is a harmonic weighted sum, not an unjustified sum of unrelated clean-risk guarantees with omitted weights.

Summing first with the common exact v gives one common coefficient. If `D=ck/(64M)-S/2` is nonnegative, then `e>=1/2` and `v>=1/(8M)` imply

`R_* >= D sum_(j=k)^T0 1/j`.

If D is negative, the claimed positive-part bound is simply zero. This distinction avoids the invalid operation of replacing a multiplier by its lower bound in front of a negative expression. On the nonnegative branch, the harmonic integral gives `sum 1/j>=log((T0+1)/k)`. This proves exactly BK1.

## 9. Asymptotic contradiction and what remains open

If a supplied-beta family independent of k attained a universal finite `C H2` for all budgets, its k=0 guarantee at the **same supplied beta** `1/M` would give `S<=C/n^5`. The identical map `A_(M,1/M)` occurs in both comparisons; this is precisely where unknown-k adaptation, rather than a known-k minimax claim, enters.

Whenever `n^4>=64C/c`, the BK1 coefficient is at least `c/(128n)=ck/(128M)`. Also `k>=sqrt(M)` and beta=1/M yield

`F2<=k/M+1/sqrt(M)<=2k/M`, so `H2<=2k/M`.

Finally, `log((floor(n^10/8)+1)/n^9)~log(n/8)` diverges. Thus actual risk divided by H2 is at least `(c/256)log((T0+1)/k)` eventually, contradicting a universal C. The onset is permitted to depend on C; no fixed finite onset for all estimator constants is asserted. Both clean alternatives and null are stationary, and all comparisons use the same valid advertised beta.

The conclusion excludes full-triple-histogram-plus-endpoints estimators, including those that project only these counts onto the source class. It does **not** exclude any estimator allowed to read additional ordering information, prove that ordering is sufficient, or establish a stronger known-k minimax lower. It adds no claim about efficient/causal adversaries, neural resources, observed masks/seeds, edited final contexts, or external novelty.

## 10. Artifacts, checks, and disposition

Independent artifacts:

- `BK001_independent_checks.py`: exact Fraction/SymPy calculations and exhaustive word identities;
- `BK001_independent_checks.json`: PASS, 30 parameter cases, 480 alternative certificate inequalities, 96 null inequalities, nonintegral expected-count cases, exact conditional constants, and 2,097,153 fixed-suffix comparisons;
- `BK001_independent_review_bindings.json`: hashes of this review, candidate, independent code/output, and accepted source/receipt files.

All 30 parameter cases include exact stationarity, probability validity, all-state minorization, three-step atom, endpoint lower bound, and concentration constants. Tested n values are 4096, 4097, 5001, 8192, 65537 and 1000003, with five j values each spanning the lower/upper boundaries and an interior point. The symbolic checks establish the stationarity identities and full P² formula as rational identities, but the entire theorem remains a mathematical proof audited by an LLM, not a machine-checked formal proof.

**Disposition:** no correction requested for the hash-bound candidate. The supplied-beta full-history adaptation question remains open. Root acceptance, if any, must be a separate action and must retain the histogram restriction prominently.
