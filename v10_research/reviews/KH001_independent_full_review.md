# KH001 — fresh independent full mathematical review

**Verdict: no substantive mathematical defect found in the frozen candidate.** The finite constrained-risk bound KH1 and its prescribed-curve, unknown-k impossibility conclusion are supported for the **exact triple histogram plus initial/final pairs**. Together with accepted KA001, they give the stated power-law classification for that statistic only. Root acceptance remains a separate action.

This is independent LLM mathematical corroboration, not formal verification, external peer review, or an external novelty assessment. No proof or accepted scientific artifact was changed by this reviewer.

Reviewed candidate: `binary_certificate_adaptation_phase/KH001_histogram_strong_side_obstruction.md`.

SHA256: `311adf683a22370fe765f61045a96af4a201e611ceeb9136f53a2b1f8cc7fd27`.

Date: 2026-11-02 UTC. The author explicitly confirmed these bytes frozen. The independent snapshot `reviews/KH001_audit_snapshots/KH001_received.md` is byte-identical. I read the entire pre-freeze candidate and then the complete actual editorial diff; the only mathematical exposition correction was explicitly including the third matrix position with value a e. Neither an inequality nor a constant changed. Later proof bytes are not covered by this verdict.

## 1. Accepted interfaces and exact observation model

I read the complete KH001 candidate, accepted BK001, BK002, KA001, SC003, BT002 main proof and BT002 scalar proof, together with all five current acceptance receipts. I additionally inspected SC002's experiment and ordinary-add-one upper interface. The checker verifies accepted proof/component hashes and receipt-specified review hashes. Candidate-era headings saying “not accepted” do not supersede these exact receipts.

The model has N=M+2 binary bits and M pair-chain departures. The source is homogeneous order two, with an all-state P²>=beta Pi certificate for a qualifying stationary pair law. The witnesses here start at their own stationary laws. The attacker sees the original full word, changes at most k of its first M bits on every realization, and preserves the actual final pair. Loss is unconditional TV at that original pair; in binary notation it is the absolute error of the predicted probability of symbol 1.

The predictor's statistic is precisely the eight exact overlapping-triple counts and the two endpoint pairs. It may know M, beta, and the entire fixed prescribed curve; it may randomize independently and compute without limit. It does not know the actual budget. Its identical map A_(M,beta) occurs in the clean and attacked experiments. The adversary is not histogram-restricted.

The accepted known-k benchmark is H2=min(1,max(s,F2)), s=M^(-1/2), with F2=0 at k=0 and

`F2=(k/M)[1+log(1+1/(k max(sqrt(beta),1/M)))]`

otherwise. SC003's upper itself uses only triple counts and the final pair. BT002's full-history lower remains valid for the restricted observation. Thus the same benchmark applies to this histogram experiment; no unproved restricted-statistic benchmark is being assumed. BK001 supplies the canonicalization argument. KA001 is needed only for the combined power-law table, not for finite KH1 or its stronger-side negative region.

## 2. Finite domain, stationary parameters, and all sixteen entries

The finite statement is conditional on an integer k meeting all displayed inequalities. It does not assert this set is nonempty for every small M or every beta in [1/M,1/16]. Section 8 separately proves eventual nonemptiness on each claimed curve.

Put delta=sqrt(beta), c=1/4096, e=1-delta. From k<=j<=T<=M/8 and delta<=1/4, we obtain x<=c/8, y<=1/8, w>=1-1/8-c/4>=3/4, a<=c, and 0<tau=x delta/w<=1/4. Also

`a=ck e/j >= 4ck delta² >= delta`,

where the last inequality follows from k delta>=6/c. Therefore a>=2beta. Every mass is strictly positive. The balances ya=xe and w tau=x delta, and equal crossing masses, verify all four coordinates of Pi P=Pi. Neither j nor 2ck is asserted to be a realized departure count; they are stationary expectations.

I reconstructed P directly from its next-bit probabilities and multiplied it. The displayed square is correct. A complete disjoint certificate partition is:

1. (01,10) and (11,01): delta tau=delta²x/w>=delta²x.
2. (11,00): tau e=delta ya/w>=delta²y.
3. (00,11), (01,11), (10,11): a delta, delta(1-tau), delta², each >=delta²w.
4. (11,10): (1-tau)tau=x delta(1-tau)/w>=delta²x.
5. (01,01), (10,10): e delta and delta e, each >=delta²x.
6. **Three** positions (00,01), (00,10), (10,01): (1-a)a, a e, e a. Since x=ya/e<=a/e and e,1-a>=3/4 while delta²/e<=1/12, all three are >=delta²x.
7. (00,00), (01,00), (10,00), (11,11): (1-a)², e², e(1-a), (1-tau)², each >=9/16, while the corresponding targets are <=1/16.

The group sizes are 2+1+3+1+2+3+4=16. This proves the all-state certificate, not merely stationarity or supported-state inequalities. The initial candidate's “two entries” wording omitted the separate position a e despite its identical bound; that clerical enumeration issue was corrected before freezing. The analogous old BK002 review typo is treated in a separate immutable-source clarification, not by editing its accepted bytes.

## 3. Asymmetric null, full-word probabilities, and genuine target

The null's symbol transition probabilities are 1-to-0=r=1/(2M), 0-to-1=beta. Its stationary symbol law is pi1=beta/(beta+r), pi0=r/(beta+r), and its pair law is pi(u)T(u,v). For every start (u,v) and target (s,t),

`P_*²((u,v),(s,t))/Pi_*(s,t)=T(v,s)/pi(s)`.

Both off-diagonal ratios equal beta+r. Each diagonal ratio is at least this number because beta+r<=1. Hence all sixteen entries satisfy the supplied certificate beta. Since beta>=2r, pi1>=2/3. The null is not symmetric and its true row-00 probability of symbol 1 is **beta**, not r.

For x^(j)=1^(M+2-j)0^j, counting transitions from its stationary first bit gives exactly

`v_j=pi1 (1-r)^(M+1-j) r (1-beta)^(j-1)`.

The long prefix, including its initial-pair contribution, is retained. Since j>=1, its exponent is at most M; Bernoulli gives (1-r)^M>=1/2. Also beta(j-1)<=1/8 gives the suffix factor >=7/8. Thus v_j>=7/(48M)>=1/(8M), and v_j<=r=1/(2M). Different j need not have equal weights. All relevant x^(j) have initial pair 11, final pair 00, and are disjoint word events.

## 4. Three-step atom, stationary variance, and exact binary reversal

The four explicit three-step paths into 11 have probabilities (1-a)a delta, delta(1-tau)², e a delta, and (1-tau)³. Each is at least a delta/2, which is at least lambda=ck delta/(4j). A common atom yields TV contraction alpha_h=(1-lambda)^floor(h/3), uniformly over initial states. This is a property of this constructed family, not a general square-root-beta mixing assertion.

For a stationary copy W and a state subset D,

`|Cov(1_D(W0),1_D(Wh))|<=Pi(D) alpha_h`.

The exact sum over h>=1 is 3/lambda-1, at most 3/lambda. Covariance expansion therefore gives Var(J_D)<=7M Pi(D)/lambda for the M departure indices. No independence of visits or stationary variance after endpoint conditioning is assumed.

For a general full-support stationary binary order-two source with exits (a,b,e,tau), Pi=(y,x,x,w) obeys ya=xe and w tau=xb. Let R exchange 01 and 10. Direct matrix substitution gives R P* R=P, where P*=diag(Pi)^(-1)P^T diag(Pi). The independent symbolic checker verifies all sixteen identities with a,b,e,tau distinct; the identity does not require b=1-e. Equivalently, the stationary triple probabilities 001/100 and 011/110 match, and all other binary triples are palindromes. The reversed full stationary word has the same law.

Thus F={Y0=11,YM=00} has probability y P^M(00,11). Reversing a word conditional on F gives P started at 00 and conditioned on its endpoint 11. This is a Markov bridge law, not a claim that the conditioned process is stationary.

## 5. Endpoint probability and the non-free rare event

The reciprocal Bernoulli estimate and floor(M/3)>=M/4 yield

`alpha_M <= 1/(1+lambda M/4)`.

Since j<=1/(8beta), M beta>=1 and k delta>=6/c,

`lambda M/4 = ck delta M/(16j) >= (c/2)k delta M beta >=3`.

Consequently P^M(00,11)>=w-1/4>=1/2. Multiplication by y gives P(F)>=j/(2M). The event under the original stationary clean law is still rare; reversal does not make its probability constant.

On F the genuine clean target is a_j. Its contribution is part of the unconditional clean risk, so

`E[|A(T(X))(1)-a_j| | F] <= S/P(F) <= 2SM/j`.

The factor M/j is explicitly present in the later loss comparison. Different sources Q_j have separate clean-risk guarantees; using their supremum S and paying these weights is legitimate. No single clean expectation is improperly substituted for an unweighted sum over different sources.

## 6. Coupling construction, stopping time, and departure corrections

Start Z at 00 and initialize W from Pi. They may be independent initially; they cannot remain independent while being coupled. At each three-step block, split each transition row into lambda delta_11+(1-lambda)R_u. Use a fresh common success coin. On success both endpoints are 11; otherwise draw endpoints from their residual rows, for example independently. For each chain, fill the block using its original P-bridge conditional on its own endpoints. This mixture reproduces the entire correct path marginal, not merely the boundary states. Once success occurs, use identical future transitions.

Let sigma be that first successful block boundary; it need not be the earliest accidental meeting. The fresh coins give E sigma=3/lambda, so the manuscript's inequality is valid. A common extension beyond time M can define sigma when the finite observed horizon ends first. After sigma the paths agree, hence |J_D(Z)-J_D(W)|<=sigma on every realization. The stationary marginal of W is unconditional. Sigma need not be independent of W, and the proof never uses such independence.

For the reversed path Z_m=R Y_(M-m), its departures correspond to original indices 1,...,M rather than 0,...,M-1. Because the original endpoints are 11 and 00,

`J00(Z)=J00(Y)+1`, and `Jcross(Z)=Jcross(Y)`.

This is the precise endpoint correction. On sigma<=k/32, |J00(W)-j|<=k/8 and Jcross(W)<=k/32, one obtains

`|J00(Y)-j|<=k/8+k/32+1<=3k/16<k/4`,

`Jcross(Y)<=k/16`.

The inequality uses k>=32 and explicitly pays the one departed endpoint. No sample mean is treated as an exact count.

## 7. Concentration constants and conditioning denominator

Before conditioning the coupling, Markov and stationary Chebyshev give exactly

`P(sigma>k/32)<=384j/(c delta k²)`,

`P(|J00(W)-j|>k/8)<=1792j²/(c delta k³)`,

`P(Jcross(W)>k/32)<=229376j/(delta k²)`.

For the third bound, E Jcross(W)=2ck<=k/64, so the event implies deviation greater than k/64; its variance bound is 56j/delta. These computations are unconditional even though the eventual target is a bridge.

Only after these bounds does the argument condition on Z_M=11. Its probability is at least 1/2, so the union bound costs at most two. There is no factor M/j here, because this is the reverse-start endpoint event; the separate original stationary rare-event factor remains in Section 5's clean-risk accounting.

Using j<=1/(8delta²) gives

`conditional failure <=229376/(delta^5 k³)+450560/(delta³ k²)`.

The second constant is 393216+57344, respectively the coupling-time and crossing-count terms. The finite assumptions bound the two displayed contributions by 7/32 and 55/256. Their sum is 111/256<1/2. Thus the stated acceptance at least one-half is justified without conditional-stationary variance, conditional IID, or uncharged endpoint probabilities.

## 8. Canonicalization and strict fixed-null Hamming budget

Removing each 111 or 000 self-loop preserves the current pair vertex; the remaining ordered skeleton is a valid path from 11 to 00. Prepending the removed 111 loops and appending the removed 000 loops preserves all eight exact triple counts, both endpoint pairs and the full length.

Let L0=N000, L1=N111, E=M-L0-L1, U=N001, V=N110. The intermediate monotone word with L0 terminal zeros differs from the canonical word only on the E skeleton positions. Relative to the **fixed pre-sampling j**, the two monotone words differ in |L0-j| positions. Exact endpoint flows give N100=U+1 and N011=V-1, so U+V<=Jcross, E<=2Jcross and L0=J00-U. Therefore

`d_H(Can(X),x^(j)) <=3Jcross+|J00-j|`.

The random occupancy mismatch is paid; the proof does not reselect j from the sampled clean path. The good event gives distance <=7k/16<k. The initial pair is also preserved, stronger than the attack model requires but essential for the chosen predictor interface.

## 9. Exactly what the kernel may know, including real beta

For each fixed experiment (M,beta,k), one finite stochastic map is chosen before any source or word is sampled. It is identity off the listed null words. On x^(j), it samples from the publicly defined auxiliary Q_j conditional on F, canonicalizes once, and checks the actual Hamming distance to that input. Failed checks output the original input; there is no repeated sampling until success.

This is one common map on all input words and for all source laws in that fixed experiment. It does not receive the actual source transition table, its qualifying stationary law, the clean interior, or estimator seed. Its auxiliary Pi_j and transition numbers are specified by the construction, not read from a hidden source. The fixed beta is public class metadata, not an unknown source parameter. If runtime ports are described as only word/M/k, the finite beta-dependent table can simply be fixed in the map's description. The theorem does **not** require or claim a single beta-blind or beta-uniform attacker across all different public experiments.

The supremum over unrestricted finite stochastic kernels permits arbitrary real probabilities. Every real beta in the finite domain gives legal positive masses and positive conditioning probability. A rational or computable beta is not assumed, and no rational implementation or efficient sampler is claimed. A finite-set kernel can be specified by its mathematical output probabilities even when some of them are irrational or noncomputable. This is consistent with the model's unrestricted-kernel premise, but would not automatically transfer to a computationally restricted adversary.

Each accepted output shares the input's protected final pair and has explicitly tested distance <=k. Thus all changes are among the first M positions and the budget is strict on every outcome. Canonicalization of the auxiliary word is not a free permutation of the observed input: the full resulting Hamming distance is charged.

The equality T(Can(X))=T(X) transfers the clean predictor's distribution exactly. Independent estimator randomization is handled by averaging its loss functional. A full-word predictor can detect the rearrangement, so this transfer is precisely where the histogram restriction enters and cannot be discarded.

## 10. Risk comparison and nonconstant null weights

On accepted samples the clean target is a_j while the null target remains beta. Since a_j>=2beta, triangle inequality yields target separation at least a_j/2. Acceptance has mass at least one-half, while the accepted clean-error contribution is at most the full conditional clean error. Rejected losses are nonnegative. Hence

`E[null loss | x^(j)] >=a_j/4-2SM/j`.

One must not substitute a lower v_j bound in front of a possibly negative bracket. The manuscript instead handles its two nonnegative parts separately: v_j>=1/(8M) and a_j>=ck/(2j) give positive contribution at least ck/(64Mj); v_j<=1/(2M) gives error at most S/j. Summing disjoint null words proves

`R_null >= (ck/(64M)-S) sum_(j=k)^T 1/j`.

If the coefficient is negative, risk nonnegativity supplies zero. If it is nonnegative, sum 1/j>=log((T+1)/k) has the required direction. This proves KH1 exactly. No posterior is declared uniform, no long-prefix weight is dropped, and the same estimator metadata is used in both risks.

## 11. Benchmark and every prescribed stronger-side curve

Because delta>=1/sqrt(M) and k>=2sqrt(M), log(1+u)<=u gives F2<=k/M+1/(M delta)<=k/M+s<=2k/M. The clean floor is no larger than this, so H2<=2k/M, including its cap.

On every fixed curve beta_M>=1/M eventually and beta_M sqrt(M)->0, beta_M->0. Write U=beta_M^(-1) and L=max(sqrt(M),beta_M^(-5/6)). Then L/U=max(beta_M sqrt(M),beta_M^(1/6))->0. Consequently k=floor(sqrt(UL)) has k/U->0 and k/L->infinity. Floors do not alter these limits because U,L and sqrt(UL) diverge.

It follows that k/sqrt(M)->infinity; beta_M^(5/2)k³=(k/beta_M^(-5/6))³->infinity; beta_M^(3/2)k²=beta_M^(-1/6)(k/beta_M^(-5/6))²->infinity; and k sqrt(beta_M)>=k/sqrt(M)->infinity. Also T/U->1/8 and k/U->0, so the harmonic logarithm diverges. Every finite condition therefore holds eventually.

An all-budget guarantee with any finite C_curve gives S<=C_curve/sqrt(M) from k=0 at exactly the same supplied beta_M. This is negligible compared with ck/(64M), leaving eventually at least ck/(128M) times the divergent logarithm. Division by H2<=2k/M diverges. The curve-dependent constant and eventual threshold are fully permitted; neither needs to be universal across curves. Clean alternatives may depend on the selected attacked budget because the claimed clean guarantee is uniform over the entire source class. The estimator map itself is not changed between those budgets.

Thus the claimed curve-wise histogram impossibility is established under stationary initialization. It is not a pointwise claim at every large k, nor a stronger known-k minimax lower.

## 12. Power-law closure and non-transfer to full histories

For the valid domain gamma>=0 and the exact curves beta_M=M^(-gamma), KH001 supplies the negative region 1/2<gamma<=1. Accepted KA001 supplies the full-history negative region 1<gamma<2, which also excludes histogram procedures. Its ordinary-add-one positives for 0<=gamma<=1/2 and gamma>=2 use only the histogram and terminal pair. Therefore the combined classification for this exact statistic is adaptive in those two outer regions and nonadaptive for 1/2<gamma<2.

The positive boundaries gamma=1/2 and gamma=2 are included by KA001's band results. This is not a classification for arbitrary non-power-law curves, other multiplicative boundary regimes not explicitly proved here, richer fixed boundary windows, or unrestricted ordered-word predictors. In particular the remaining full-history region is not closed by the new canonicalization argument. Nor does histogram impossibility prove that access to ordering is sufficient.

## 13. Independent exact diagnostics and disposition

The separate script `reviews/KH001_independent_exact_checks.py` was written without reading or importing author diagnostic code. Its run reports **222,601 passing assertions**, all with exact rational arithmetic or exact symbolic identities, not Monte Carlo estimates. It includes:

- 108 complete finite-domain rational clean-family cases, with 1,728 alternative and 1,728 asymmetric-null certificate entries, 432 three-step-atom checks, exact endpoint/concentration constants, and 66 nonintegral stationary-mean cases;
- a general four-exit symbolic reversal identity and the full symbolic square;
- exact stochastic residual rows and both marginals of the common-atom endpoint coupling;
- three algebraic irrational-delta cases, including one **irrational beta**, and 48 further certificate entries;
- all 8,191 initial-11/final-00 binary words of lengths 4 through 16, checking canonicalization, exact histograms, endpoint flows, reverse departure corrections and 98,305 fixed-null-suffix Hamming comparisons;
- 6,096 exact full-word reversal checks, 21 exact bridge-event identities, and 345 direct asymmetric-null full-word probability checks;
- accepted source/component/review hash verification and candidate/snapshot hashes checked at both ends of the run.

The small exhaustive examples are explicitly structural tests outside the main enormous finite domain; they are not presented as theorem-domain acceptance simulations. Finite diagnostics corroborate only their tested instances. The universal real-beta, coupling, risk, asymptotic and common-map quantifiers are mathematical arguments audited above, not formally verified by this script.

The separate binding manifest records this review, candidate/snapshot, checker/output, actual editorial history and accepted dependencies. **No further correction requested for the frozen KH001 bytes.** Any root acceptance or summary should retain the histogram-plus-endpoint-pairs restriction and the distinction from unresolved full-history adaptation prominently.
