# CB002 — independent full mathematical review

2026-11-02. Separate LLM reviewer. **PASS for the stated partial risk-increment theorem.** No author proof revision was needed. This is not formal verification, external peer review, or a solution of unknown-budget adaptation.

## Reading scope

I read the complete current `CB002_near_prefix_veto_partial.md`. I separately read SC003's experiment, orientations, universal terminal-occupation interface and positive-beta support classification (the theorem through its upper-bound assembly), together with its exact acceptance receipt. I read AB003's exact acceptance receipt for the existing small-budget guarantee and CB001's acceptance receipt/full independent review for the inherited support consequence. I did not re-review the complete inherited SC003/AB003/BK001/BK002 proofs. Their accepted statements are used only in the roles explicitly described by CB002. All three checked receipt hashes match their proof bytes.

The received candidate is preserved in `review_snapshots/CB002_received.md`. Its hash is `69c55c6ab40e939c5392beb022c213c8506e8aa464b3f0b2f3f23b0db0eabe11`.

## Full proof audit

### 1. Diagonal trace and certificate algebra

The trace includes every diagonal self-loop and omits only crossing states. Starting at01, the probability of first reaching11 rather than00 is `b/[b+e-be]`; from10 the exchanged probability is `e/[b+e-be]`. Thus the displayed trace probabilities `alpha=ab/H` and `delta=tau e/H` are correct. Under full support, the positive all-state certificate forces the parameters used as denominators to be positive and crossing excursions to finish almost surely.

The certificate entry `P^2(01,10)=b tau>=beta x`, together with `w tau=xb`, gives `b^2>=beta w`. Stationarity supplies `e=ya/x<=y/x`. The four cases proving (2.4) are exhaustive and valid; they establish the stated constant3 without imposing `theta10(1)=b`. The derivation of

`lambda=a min(1,y/w)=min(a,a delta/alpha)`

and `lambda/delta=(H/b) min(1,w/y)` is exact. Summing any certificate row gives `beta<=1`. Therefore `lambda<=3delta/sqrt(beta)` is sound.

### 2. Arbitrary-start future endpoint factor

For every nonnegative integer q, stationarity implies `w P^q(11,00)<=y` by retaining only the11 term in the stationary mixture. This is an algebraic transition-probability bound; it does not assert that the actual initial law, prefix endpoint or future endpoint is stationary. It yields (2.2), including q=0. Conditioning on the state at the deterministic prefix endpoint n is legitimate.

### 3. Independent stacks and incomplete excursions

Independent excursion random variables can be assigned in advance to each successive visit to each diagonal. Their next-diagonal indicators form independent Bernoulli stacks with parameters delta and alpha. Durations can depend on their indicator, as the manuscript explicitly allows.

When `Y_n=11`, every departure from a diagonal before n has completed its next-diagonal transition by n: otherwise the path at n would still be crossing or the next diagonal would already have been reached. Therefore the departure counts are exactly `J_11,J_00` for the completed trace segment. If the original start is a crossing state, the first diagonal may be00 or11, but the trace still ends11. Its number of11-to00 transitions is consequently at most its number of00-to11 transitions. This proves `B_11(J_11)<=B_00(J_00)` with no missing initial or final correction.

On `E_K`, fixed stack prefix lengths `m=n-K` and K satisfy the stated pointwise monotonicity inclusion. The right-hand side of (3.1) involves independent fixed-size binomials because unused stack entries exist on the same infinite probability space. No conditional-binomial or conditional-IID claim is being made about the observed random counts.

### 4. Binomial comparison and occupation bound

The low-mean branch `m delta<4K alpha` gives `lambda<=a delta/alpha<=8K/n`. In the other branch, the lower-tail base1/2 and upper-tail base2 exponential Markov bounds are correct. The stated elementary bounds on log2 imply the advertised exponents1/8 and1/16. The union bound then gives `2exp(-m delta/16)`. Combining this with `lambda<=3delta/sqrt(beta)`, `m>=n/2`, and `z exp(-z)<=1` gives the192 constant.

For a prefix endpoint other than11, `E_K` implies the actually selected row has at most K departures. SC003's accepted arbitrary-start occupation inequality applies at horizon n with integer threshold K+1. This event is not conditioned on the future terminal row. Discarding the future requirement and multiplying by `a<=1` is valid. The two contributions give (NP3). For `K>n/2` the stated unit-capped bound is trivially1; no random K is inserted into a binomial theorem.

### 5. Corruption and loss comparison

Each zero among the first n+1 clean symbols belongs to at most two of the n departure pairs, so their total non11 occupation is at most twice the prefix zero count. Each actual edit changes that count by at most one. The prefix lies within the editable part for the stated M range; in any event the strict total edit count suffices. Thus an observed near-one prefix implies a clean near-one prefix with threshold h+k, pointwise for every adaptive/randomized strict-k kernel.

The final pair is protected, so the selected designated probability is the same clean target. Overwriting a binary estimate with designated probability0 increases TV/absolute-error loss by at most the true designated probability. The two overwritten terminal states are disjoint. Summing (5.1) and its symbol exchange, then applying the unit cap, proves the increment bound. No baseline clean observations or true k are used by W.

### 6. Boundary supports and constants

The positive-beta support classification is the accepted SC003 one. If00 is absorbing, the00 designated target a vanishes. If11 is absorbing and the terminal state is00, the whole earlier path avoids11, so the small-non11 event is impossible for K<n; larger K is already in the trivial bound. This handles arbitrary unsupported starts without using full-support divisions. Symbol exchange handles the opposite orientation.

For M>=128, `n=floor(M/2)>=64` and `n>=M/3` give the constants288 and1248. For64<=M<128, the right-hand increment cap is1, which is trivially valid. At beta=1/M, `ceil(sqrt(M))<=9sqrt(M)/8` gives1572/sqrt(M)+288k/M, dominated by (NP2)'s powers of two. All constants and finite ranges are consistent.

## Fresh independent diagnostics

The independent script uses exact integer/Fraction arithmetic; square-root inequalities are checked by squaring nonnegative quantities. It passed:

-3 exact accepted-proof receipt hashes;
-96 source tables with stationarity and all16 certificate entries;
-96 trace probability identities and96 lambda bounds;
-576 future-endpoint inequalities;
-384 ordered near-occupation dynamic programs versus the exact independent-binomial comparison;
-384 weighted future-terminal calculations;
-8,190 exhaustive finite-path trace-balance checks, including initial crossing states;
-23,520 strict-Hamming prefix/protected-endpoint checks;
-8 absorbing-support/unsupported-start cases;
-9,937 finite scalar-assembly checks.

These finite diagnostics are independent of the author test and do not prove the universal result. The dynamic programs retain path ordering and occupation information, not merely a triple histogram.

## Scope decision

The theorem is valid as an arbitrary-corruption **risk-increment** bound for a near-prefix veto. At beta=1/M it is of order `M^-1/2+k/M`, uniformly over arbitrary starts and all strict protected-endpoint kernels. It is not a standalone risk upper bound for W(A): the baseline term `R(A,C)` remains. Accordingly it preserves AB003's known small-budget guarantee but does not establish its missing large-budget guarantee. The stated bypass concern for a fixed threshold remains a research direction rather than a proved impossibility. No full critical-curve adaptation, new known-k minimax frontier, formal verification, or external novelty conclusion follows.
