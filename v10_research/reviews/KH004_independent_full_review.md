# KH004 — independent full mathematical review

**Verdict: no substantive mathematical defect found in the frozen candidate.** The finite KH4 inequality and the unknown-budget obstruction for every prescribed integer width sequence r>=2, r=o(M^(1/3)), at beta=1/M are supported for the exact eight triple counts plus the genuine first/last-r bits. This is an independent LLM review, not root acceptance, formal verification, external peer review, or an external novelty assessment.

Candidate: `binary_certificate_adaptation_phase/KH004_constant_crossing_window_obstruction.md`.
SHA256: `ec332fdd75eed3401f389804f4f1ed21a46b1bc1d8a8c09f68088676e47da814`.
The reviewer saved an identical received snapshot. The author confirmed frozen bytes. No proof was edited by this reviewer; project acceptance is separate.

## 1. Actual accepted interfaces and review method

I read the full KH004 candidate, full KH001/KH002/KH003 statements and arguments, their actual root acceptance receipts, the SC003 model and count-based estimator, the benchmark definition in KA001, and the BK001 canonicalization/occupation argument. I inspected the SC003 and BT002 receipts and BT002 scalar completion. Exact checks bind those accepted proof bytes (including BT002 components), receipt-specified review bytes, and every file in the prior final KH003 reviewer manifest. The stale word “candidate” in accepted manuscripts is not their current status. In particular KH003 has an actual root acceptance dated 2026-11-02T14:19:42.998497+00:00. KH002 supplies context only: its histogram domain classification is not silently promoted to growing windows. KH003 is a separately valid baseline, not a premise requiring its exponent to be rewritten.

I derived the new family algebra and constants independently and wrote a fresh exact checker without importing, executing, or reading the KH004 author checker. Small finite diagnostics do not prove the infinite-domain theorem; the analytic audit below does the mathematical work. The checker tests symbolic identities, exact rational feasible cases, complete finite endpoint words, exact bridge probabilities, and same-map randomized loss transfer. The report and bindings specify the exact scope of the resulting evidence.

The model is N=M+2 bits, M departure triples, true last pair protected, unconditional binary TV (absolute probability error), offline stochastic attacks with a pointwise budget on the first M bits. Randomized predictors have independent internal seeds. The same map, with the same public (M,beta,r), must satisfy both clean and attacked guarantees; it is not supplied actual k. The attacker may depend on k but is one source-independent finite kernel for that problem. Neither a revealed mask nor an auxiliary seed is part of the observation.

The benchmark is H2=min(1,max(M^(-1/2),F2)), F2=(k/M)[1+log(1+1/(k max(sqrt(beta),1/M)))] for k>0 and F2=0 at k=0. SC003's estimator uses counts/final pair only and so is available for the richer window statistic. BT002's full-history lower also applies after restricting observations. This justifies calling H2 the known-k profile here.

## 2. Legal parameters and all sixteen certificate entries

From k<=j<=T<=M/8, x=ck/M<=c/8, y=j/M<=1/8, w=1-y-2x>=3/4. Also a=ck/(2j)<=c/2<1/4 and tau=x/(2w)<1/4. All four stationary masses and all allowed transition probabilities are positive. The equations ya=x/2 and w tau=x/2 imply stationarity. The independently generated pair kernel squares to the displayed matrix exactly.

Every entry is covered by the manuscript's disjoint partition of size 2+2+3+1+2+2+4=16. In particular the potentially restrictive (00,11) and (11,00) positions both reduce to ck>=4 beta j w, and beta j<=1/8 makes their right side at most1/2, far below ck>=64. The tau/2 crossing targets use 1/(4w)>=beta. The a/2 crossing targets use j/M<=1/8; (1-a)a>=3x follows from a>=4x and 1-a>=3/4. The remaining tau term uses (1-tau)/(2w)>=3/8. The four large entries are indeed at least9/16,1/4,3/8,9/16 respectively. No support-only minorization substitutes for an all-state check. Finally a>=4ck beta>=2beta, so the target separation is valid.

For the asymmetric first-order null, its stationary pair law gives P_*²((u,v),(s,t))/Pi_*(s,t)=T_*(v,s)/pi(s). The off-diagonals are beta+q; both diagonals dominate this because beta+q<=1. Its initialization has pi1>=2/3. The exact full-word weight includes M+1-j leading persistence factors and j-1 trailing factors. Since j>=1, the first exponent is at most M, giving a factor at least1/2; the trailing factor is at least7/8. Thus v_j>=7/(48M)>1/(8M), while v_j<=q=1/(2M). The target at terminal00 is beta, not q. The checker independently tests these full weights and all sixteen null ratios with exact fractions.

## 3. Mixing, reversal, and occupation concentration

The four stated length-three paths have probabilities (1-a)a/2, (1-tau)^2/2, a/4, (1-tau)^3. Each exceeds a/4. Since lambda=ck/(16j)=a/8, the chosen common atom is conservative. Its three-step splitting gives alpha_h=(1-lambda)^floor(h/3) as a total-variation bound from any start to stationarity.

For an indicator of D under stationarity, |Cov(I0,Ih)|<=Pi(D)alpha_h. Summing gives Var J_D<=M Pi(D)(1+2 sum alpha_h)<=7M Pi(D)/lambda. More precisely sum_(h>=1)alpha_h=3/lambda-1, so the bound has slack. Exactly M departures are counted.

The stationary reverse kernel conjugated by bit swap equals P. This follows from ya=x/2 and w tau=x/2, and was independently checked symbolically entry by entry. Thus reversing the original stationary event Y0=11,YM=00 gives a chain started00 conditioned on E={Z_M=11}, and its original probability is y P_00(E). This transformation does not make the original rare event free.

The reciprocal Bernoulli inequality and floor(M/3)>=M/4 give alpha_M<=1/(1+lambda M/4)<=8/(ck)<=1/8 (in fact the last constant is substantially smaller). Hence P_00(E)>=w-1/8>=1/2. The original event probability is at least j/(2M).

For the coupling, the split three-step kernels can use the same Bernoulli success, then fill each three-step interval by its correct conditional bridge; at the first success both boundary states equal11. Continuing with identical transitions preserves both full marginal path laws. The unbounded extension makes sigma a valid geometric-block meeting time, E sigma<=3/lambda. Occupations differ by at most sigma even if sigma>M; no independence with W is needed.

Markov at k/32 gives1536j/(c k²). Chebyshev for00, whose variance is at most112j²/(ck), at k/8 gives7168j²/(c k³). For crossing occupation, the mean2ck<=k/64; the variance is at most224j, and threshold deviation k/64 gives917504j/k². Conditioning on E costs at most2. Using j<=M/8 and c=1/4096 yields precisely917504 M²/k³+1802240 M/k². The stated finite assumptions reduce this to7/32+55/256=111/256.

Under reversal the departure set shifts from original0,...,M-1 to1,...,M. Consequently J00(reverse)=J00(original)+1 and crossing counts agree. The +1 is paid: k/8+k/32+1<=3k/16 for k>=32. Thus the good original-count event has |J00-j|<=k/4 and Jcross<=k/16 with the claimed conditional probability. No endpoint correction is lost.

## 4. Late-window flux and original-event charging

For the reversed start00, early failure before r zero bits costs at most(r-2)a unconditionally. Dividing by P(E)>=1/2 and using j>=16crk gives at most2ra<=1/16.

For late failure on E, the last zero has one-based bit index q in[N-r+1,N-2], and the triple starting there is011. Its pair departure index is q-1 in[M+2-r,M-1], exactly r-2 choices. These are legal indices; when r=2 the event and set are empty. Since r<=k/4<=M/32 and M>=64, each such m obeys m>=M/2 and floor(m/3)>=M/8. Therefore P_00(Y_m=01)<=x+alpha_m<=x+16/(ck). Multiplication by the true transition probability1/2 gives each unconditional011 flux. The union is bounded before dividing by P(E); the result is r[x+16/(ck)]<=1/8. This argument never treats either the reverse-start chain or its endpoint bridge as stationary, and never replaces the needed flux by the unusable crude r/2 bound.

Adding the early and late costs gives P(B^c|E)<=3/16. Together with concentration the direct intersection lower bound is97/256; the stated81/256 is a valid deliberately weaker bound (using3/16<=1/4). Since P(B|E)<=1, passing from P(G and B|E) to P(G|E,B) cannot decrease that lower bound. The manuscript correctly uses the upper bound1 on this denominator, not its lower bound3/4.

In the original stationary orientation F_r is exactly the reversal of E and B with the stationary initial factor y. Thus P(F_r)>=3j/(8M). Nonnegativity of unconditional clean loss gives conditional clean error<=8SM/(3j)<=4SM/j. Both the rare original endpoint and actual windows are charged. Exact nonstationary state/flag/trailing-run dynamic programs corroborate the late flux inclusion and conditioning order, and exact word enumeration corroborates the original/reversed event masses.

## 5. Canonicalization, strict kernel, same-map transfer

Removing only000/111 loops keeps the residual path legal; prepending111 loops and appending000 loops preserves every triple count, both pair endpoints, and length. The accepted BK001 endpoint flows imply E_sk<=2Jcross, N001<=Jcross, and N000=J00-N001. Comparing the canonical output to the fixed pre-sampling one-change word gives d_H<=3Jcross+|J00-j|. On G this is at most7k/16<k. The j in that comparison is not chosen after seeing the auxiliary sample.

The genuine constant windows in F_r themselves force at least r-2 copies of each diagonal loop. Moving those loops to the endpoints consequently preserves these windows for every F_r sample, not only good ones. The manuscript's extra good-event loop-count bounds are also valid: N000>=j-5k/16 and N111>=M-j-3k/8>=53M/64. An explicit output-window test is retained safely even though redundant under this conditioning.

The kernel samples once from Q_j conditioned on F_r, canonicalizes once, and accepts only on the stated two tests; otherwise it is identity. There is no conditioning on repeated successes. Its sampler is a fixed auxiliary table indexed by the observed one-change input, not access to the true source parameter, unseen clean data, or predictor seed. General real probabilities are legal in this finite unrestricted-kernel model. Every output, including rejection, obeys the first-M Hamming budget and protected terminal pair. On G both checks pass, and acceptance is at least1/4.

For every accepted sample the exact T_r input agrees with that of the genuine clean sample. The fixed predictor's conditional output distribution therefore agrees as well; an independent seed can be integrated into its loss function. This does not require deterministic prediction. Interior longer-pattern histograms and full ordering are not preserved in general, and no inference is made for them.

## 6. Finite loss inequality and asymptotic consequence

On acceptance triangle inequality gives null error at least(a-beta) minus clean error. Since a-beta>=a/2 and acceptance>=1/4, subtracting at most the entire nonnegative conditional clean error gives a/8-4SM/j. Rejection adds only nonnegative loss. Multiplying the positive term by the lower bound1/(8M) and the error term by the upper bound1/(2M) yields ck/(128Mj)-2S/j. This is correct even if the resulting bracket is negative: no negative quantity is multiplied by a lower mass bound. Disjoint null words permit summation. If the resulting coefficient is nonnegative, sum1/j>=log((T+1)/J0); if negative, risk nonnegativity supplies the positive part. This proves exactly KH4.

For the benchmark, log(1+u)<=u and beta>=1/M yield F2<=k/M+1/(M sqrt(beta))<=k/M+M^(-1/2)<=2k/M. Also M^(-1/2)<=k/M here, so H2<=2k/M follows for the maximum definition and its cap.

At beta=1/M choose U=M/r and L=M^(2/3), with k=floor(sqrt(UL)). The assumption r=o(M^(1/3)) says U/L->infinity. Hence k/L->infinity and k/U->0; the floor is negligible because UL diverges. Consequently k³/M²->infinity, k²/M->infinity, k/sqrt(M)->infinity, r/k->0, rk/M->0 and k/M->0. Each finite inequality then holds eventually, including the constant-heavy lower bounds, both window-probability bounds, k<=T, and r<=k/4. Moreover J0<=k+16crk+1 gives J0/M->0, while T/M->1/8. The harmonic logarithm diverges.

Any all-budget guarantee with fixed finite C forces S<=C/sqrt(M) at actual k=0 for the very same predictor map. Since k/sqrt(M)->infinity, its2S penalty is negligible relative to ck/(128M). Eventually KH4 is at least ck/(256M) times the divergent logarithm, whereas H2<=2k/M. The ratio is at least c/512 times that logarithm and diverges, contradicting the guarantee. Maps and C may depend on the entire prescribed width sequence; no uniformity over all width sequences is needed.

The change from KH003 is genuine: constant crossing gives atom of order k/j and variance-driven k>>M^(2/3); near-terminal mixing supplies the different late-window control. It improves the demonstrated obstruction to every r=o(M^(1/3)), without establishing that exponent as sharp. The finite domain is nonempty asymptotically, not vacuous; exact diagnostics include r=M^(5/18), strictly beyond the old M^(1/6) regime.

## 7. Evidence and disposition

Fresh code: `reviews/KH004_independent_exact_checks.py`.
Results: `reviews/KH004_independent_exact_checks.json`.
Bindings: `reviews/KH004_independent_review_bindings.json`.
Snapshot: `reviews/KH004_audit_snapshots/KH004_received.md`.

The final run passed 246,675 exact assertions. The checker tests four feasible huge-integer parameter cases at three j positions each, all16 rational certificate entries, symbolic stationarity/reversal/squared kernel, null weights, all8191 endpoint words of lengths4 through16, fixed-j Hamming bounds, genuine window preservation, reverse departure corrections,6096 exact stationary word reversals,126 boundary dynamic programs,15 original-event mass identities, and45 randomized same-map loss-transfer cases. Exact checks cover finite cases; the analytic argument establishes the uniform inequalities and asymptotics. No numerical sampling or author diagnostic substitutes for those arguments.

**Recommendation:** eligible for the root's separate acceptance decision at the exact frozen hash. No mathematical revision is required by this review. No full-history, arbitrary local encoder, all interior pattern-count, neural/training, sharp-threshold, efficient/causal attack, visible-seed/mask, edited-target, external novelty, external peer-review, or formal-verification claim is supported beyond the explicit statement. The earlier accepted KH003 result remains unchanged.
