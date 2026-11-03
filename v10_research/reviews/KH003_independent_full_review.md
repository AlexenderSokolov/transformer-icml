# KH003 — independent full mathematical review

**Verdict: no substantive mathematical defect found in the frozen candidate.** The finite constrained-risk inequality, the critical-certificate growing-boundary-window consequence, and the bounded-width public-domain classification are supported for **the exact triple histogram plus the first and last r symbols**. Root acceptance is a separate decision.

Reviewed candidate: `binary_certificate_adaptation_phase/KH003_boundary_window_obstruction.md`.

SHA-256: `09adb8433d97011dbe7772ed9b0f1f903ed245d73299db02d7d6bc477fc358a4`.

Date: 2026-11-02 UTC. The author confirmed these bytes frozen during the audit. The independent received snapshot is byte-identical. The reviewer did not edit the candidate or accepted theorem bytes. This is independent LLM mathematical corroboration and exact finite diagnostics, **not formal verification, external peer review, or a novelty assessment**. Changed proof bytes would need a new review binding.

## 1. Complete reading and accepted interfaces

I read the complete KH003 candidate, its actual initial version, the complete saved clarification diff, and the exploratory note. I also read the complete accepted KH001, KH002, and BK001 proof texts and their current acceptance receipts; the complete KH001 and KH002 independent reviews; KA001's complete proof and receipt; SC003's complete proof and receipt; and BT002's accepted benchmark statement, scalar completion, and receipt. Their accepted proof/component hashes and receipt-specified review hashes are checked by the separate diagnostic. The remaining accepted BT002 construction is used as an accepted benchmark interface, not purportedly reproved by this boundary-window audit.

The current receipts are substantive: KH001 is root-accepted at proof hash `311adf683a22370fe765f61045a96af4a201e611ceeb9136f53a2b1f8cc7fd27`; KH002 is root-accepted at `970bfefb6041cdb989148819eb526c789d86591992375b84b05de2dd72bf9702`; BK001 is root-accepted at `edbfc9cd372df7497ff7462eded0e6c85a3ee4f99f21bd7310f460bd1f0fcb5a`. In particular KH003 §7 does not currently depend on an unaccepted KH002 assertion. Candidate-era pending-review labels inside immutable accepted proofs do not override their later exact receipts.

The word has N=M+2 binary symbols and M pair-chain departures. A source is homogeneous order two and has a qualifying stationary pair law Pi satisfying P²(u,v)>=beta Pi(v) on every starting and target pair state. The witnesses used here are stationary. The adversary is an offline stochastic map on the original full word, with at most k edits on every outcome and the final pair protected. Loss is unconditional TV at that original true terminal pair, hence absolute symbol-1 probability error in the binary case. No edit mask or attack seed is observed.

The predictor's actual statistic is

    T_r(w) = (all eight overlapping-triple counts, w[1:r], w[N-r+1:N]).

It may know M, actual supplied beta, r, and the public domain or prescribed width sequence, and may randomize independently. It does not know the actual k. The exact same map at the same metadata is used in its clean and attacked guarantees. The attacker is not restricted to T_r.

The known-k profile is H2=min(1,max(s,F2)), with s=M^(-1/2), F2=0 at k=0, and

    F2=(k/M)[1+log(1+1/(k max(sqrt(beta),1/M)))]

for positive k. SC003's upper itself uses only triple counts and the terminal pair. BT002's full-word lower applies also to the less informative observation T_r. Thus this really is the known-k benchmark for the new observation interface; there is no unlicensed full-history upper requiring discarded order.

## 2. Finite domain and inherited source family

The finite statement is conditional on all listed inequalities; it does not claim that the domain is nonempty at every M or beta. Since beta>=1/M and T=floor(1/(8beta)), T<=M/8. The new starting index satisfies J0>=k, so restricting the KH001 family to J0<=j<=T preserves every inherited source, endpoint, and concentration bound. The extra restrictions imply r<=k/4<=M/32, so the two boundary windows are disjoint and fit inside the word.

The family has x=ck/M, y=j/M, w=1-y-2x, a=ck(1-delta)/j, b=delta, e=1-delta, tau=x delta/w, and Pi=(y,x,x,w). The stationarity balances are ya=xe and w tau=x delta. KH001's proof checks all sixteen entries of P²>=delta² Pi, legal positive probabilities, and a>=2beta. The separate diagnostic reconstructs P from its next-bit probabilities, verifies stationarity coordinate by coordinate, and checks all sixteen entries at both witness and actual certificates in its finite cases.

The endpoint-conditioned comparison is not KH001's histogram risk inequality applied without modification to a richer estimator. That would be invalid. KH003 uses KH001's **source and probability facts**, then proves a fresh statistic-preserving risk transfer for T_r. This is the essential distinction allowing the extension.

## 3. Reversal and the good event use original counts

Let F={Y0=11,YM=00}. For a stationary full-support binary order-two law, swapping pair coordinates after time reversal returns the same kernel. Thus reversing a stationary word conditional on F gives P started at 00 and conditioned on E={Z_M=11}. The genuine original event has probability

    P_Qj(F)=y P_00(E)>=j/(2M),

while P_00(E)>=1/2. These are different probabilities; only the second is a constant-probability endpoint event.

KH001's concentration uses a stationary comparison chain, a three-step common atom of mass lambda=ck delta/(4j), and coupling before reverse endpoint conditioning. Its final failure bound is

    229376/(delta^5 k^3) + 450560/(delta^3 k^2)
    <=7/32+55/256=111/256.

The reverse departure count satisfies J00(Z)=J00(Y)+1, not equality. That correction has already been included in KH001's original-word good event G, which gives |J00(Y)-j|<=k/4 and Jcross(Y)<=k/16. KH003 uses these **original-word** counts in its loop and Hamming calculations. It does not silently substitute reverse counts or reuse unconditioned stationary variance after conditioning on the boundary event.

## 4. The first clean boundary window

Write the reversed symbols z1,...,zN, initially z1z2=00. Having the first r symbols all zero requires the first r−2 departures to remain at 00. Until the first failure, each has exit probability a. Under the unconditioned P_00 law the failure probability is in fact exactly

    1-(1-a)^(r-2) <= (r-2)a.

The manuscript's weaker displayed inequality is valid. It does not assume independence after conditioning on E. At r=2 no transition needs to be constrained and the failure probability is zero.

The index lower bound J0>=ceil(16crk) ensures j>=16crk, so a=ck(1-delta)/j<=1/(16r). This remains true on both sides of the max defining J0, including r<=256 when J0 can simply equal k. Ceilings are in the correct direction.

## 5. The late clean boundary window and exact last-zero indices

On E, z_(N−1)z_N=11. If the last r symbols are not all one, their last zero has a unique 1-based index

    N−r+1 <= q <= N−2.

Every symbol after this last zero in the terminal window is one. Consequently z_q z_(q+1) z_(q+2)=011. With pair convention Z_m=(z_(m+1),z_(m+2)), this is the departure m=q−1, namely an 01-to-11 transition.

The possible departure indices are

    m=N−r,...,N−3 = M−r+2,...,M−1,

exactly r−2 positions. For each such **unconditioned** departure, its probability is P_00(Z_m=01) times delta, at most delta. Therefore

    P_00(E and last-r ones fail) <= (r−2)delta.

There is no assumption about the state entering the late window, no independence of the positions, and no assertion that the bridge's conditional transition probability is at most delta. The union bound is taken before conditioning, and E only licenses the last-zero witness. At r=2 the witness range and failure event are both empty.

Combining early and late failures and dividing by P_00(E)>=1/2 gives

    P_00(B^c | E) <= 2(r−2)(a+delta)
                     <=2r(a+delta)<=1/4,

where B denotes the two constant reversed boundary windows. The final bound uses ra<=1/16 and r delta<=1/16. Both genuine windows have therefore been paid for under the correct bridge law.

## 6. Intersection probability and the genuine rare event

No independence between G and B is needed. Under E,

    P(G intersect B | E) >= 1−111/256−1/4 =81/256,
    P(B | E)>=3/4.

Then P(G | E,B)=P(G intersect B | E)/P(B | E)>=81/256, because the denominator is **at most one**. Using its lower bound 3/4 in this lower-bound calculation would be an invalid direction; the candidate explicitly avoids that mistake.

Let F_r be the genuine original stationary event with first-r ones and last-r zeros. It implies F and reverses precisely to E intersect B. Hence

    P_Qj(F_r)=y P_00(E intersect B)
             =P_Qj(F)P_00(B | E)>=3j/(8M).

This identity also proves that the conditional auxiliary sampling law is well-defined. On F_r the clean terminal pair is 00, so the true clean target is a_j. If S is the same-map supremum unconditional clean risk over the family, nonnegativity yields

    E[clean loss | F_r] <= S/P_Qj(F_r)
                         <=8SM/(3j)<=4SM/j.

The original event's order-j/M probability remains present. Reversal has not made that original clean conditioning free.

## 7. Loop geometry and the fixed null suffix length

For an original word from 11 to 00, define L0=N000, L1=N111, U0=N001, and E_sk=M−L0−L1. BK001's endpoint flows imply U0<=Jcross, E_sk<=2Jcross, and L0=J00−U0. Thus on G,

    L0 >= j−k/4−k/16 = j−5k/16 >=11k/16>=r−2.

Also L0<=J00<=j+k/4 and E_sk<=k/8, giving

    L1 >= M−j−3k/8 >=53M/64>=r−2.

The middle numerical bound uses j,k<=M/8. The last follows from r<=k/4<=M/32. These inequalities are all about actual original counts, not stationary means substituted for counts.

Canonicalization removes 111 and 000 self-loops, prepends the former at the initial 11 vertex, leaves all other edges in their existing order, and appends the latter at final 00. It preserves length, endpoint pairs, and all eight triple counts. The leading run has at least L1+2 ones and the trailing run at least L0+2 zeros, including the endpoint pairs contributed by the skeleton. Therefore the displayed loop bounds suffice for the output windows.

For the actual input x^(j)=1^(N−j)0^j, BK001's exact bound is

    d_H(Can(X),x^(j))<=3Jcross(X)+|J00(X)−j|<=7k/16<k

on G. Here j is selected from the **observed designated null word before auxiliary sampling**. It is not selected later to match a random zero occupancy, nor is the canonicalization granted as an uncharged permutation. The full Hamming distance to the actual observed input is charged.

## 8. The actual revision and the redundant output-window check

I inspected the actual before copy at SHA-256 `17a4c9ea015a18a874b670b7d920cd43605eb4d862f38c3afe161de96282a410`. The saved unified diff exactly equals the computed before/after diff, including its file labels. There are three explanatory replacements and no change to the kernel, constants, source family, theorem, or asymptotic hypotheses.

The important correction is valid: **F_r alone** already implies L1,L0>=r−2, because the first constant window contains r−2 copies of 111 and the final constant window contains r−2 copies of 000. Consequently every canonicalization of an F_r word has the desired output windows, not merely those samples on G. The explicit output-window test is redundant for these constant conditioned windows, although it is legitimately retained as a required step of the defined kernel. The section heading's “mandatory acceptance test” can refer to that definition; it does not establish logical indispensability.

The initial wording that the output test itself was indispensable overstated the matter. The frozen revision removes that claim and gives the self-loop reason. Its remaining caution is correct: canonicalization applied to arbitrary pair-conditioned clean words, without genuine constant-window conditioning or another argument, does not preserve arbitrary longer original boundary windows.

## 9. One legal common kernel and equality for every accepted sample

For each fixed public (M,beta,k,r), the map is identity except on the distinct designated words x^(j), J0<=j<=T. On such an input it samples once from the public auxiliary stationary Q_j law conditional on F_r, canonicalizes, and checks both Hamming distance and output windows against the actual input. Failed tests output that unchanged input. There is **no resampling until acceptance** and no renormalization onto accepted samples.

The auxiliary transition and stationary tables are specified by public construction. They do not come from the unknown true source, and the map does not receive a hidden clean interior, qualifying stationary law, or estimator seed. One finite stochastic map is fixed across source laws in this public experiment. Dependence on the public certificate, width and selected attack budget is allowed; a single beta-blind or width-blind adversary across all different experiments is not claimed. Real probabilities are permitted by the unrestricted finite-kernel model; no efficient, causal, rational-only, or computable-probability implementation is inferred.

Every accepted output is within k of the actual input and has the same final pair. Rejection and all other inputs are identity. Thus the budget and protected terminal pair hold on **every** outcome. The original input itself has first-r ones/last-r zeros because j>=k>=4r and N−j>=7M/8+2>=r.

G has conditional probability at least 81/256 under F_r and passes both tests, so acceptance is at least 1/4. Every accepted output, not just those on G, satisfies

    T_r(Can(X))=T_r(X).

The genuine conditioning and explicit output check directly establish this; the constant-window loop observation independently shows the check is redundant here. The predictor's entire input distribution, including the same public metadata, is therefore equal on this clean sample and its canonicalized output. Independent predictor randomization can be averaged into the nonnegative loss functional without revealing or coupling its seed to the attacker.

## 10. True null target, nonconstant word weights, and KH3

The null has 1-to-0 rate rho=1/(2M), 0-to-1 rate beta, and stationary pi1=beta/(beta+rho). Its true target at terminal 00 is **beta**, not rho. The complete null-word mass is

    v_j=pi1(1−rho)^(M+1−j) rho(1−beta)^(j−1).

KH001's bounds 1/(8M)<=v_j<=1/(2M) retain the long-prefix factor and do not assert equal masses across j. The new j range is a subset of the accepted range, so these bounds still apply.

On an accepted auxiliary sample, the clean target is a_j and the null target remains beta. Since a_j>=2beta, their gap is at least a_j/2. Acceptance probability at least 1/4 and triangle inequality give

    E[null loss | x^(j)] >= a_j/8−E[clean loss | F_r]
                          >=a_j/8−4SM/j.

The accepted clean-error contribution is no greater than the full conditional clean error. Rejected losses are nonnegative. This is why one must not resample until success or replace the comparison by a differently normalized clean law.

The signed bracket cannot simply be multiplied by the lower v_j bound. Instead bound the positive and error terms separately:

    v_j(a_j/8) >= (1/(8M))(ck/(16j))=ck/(128Mj),
    v_j(4SM/j) <= (1/(2M))(4SM/j)=2S/j.

Summing the disjoint null words and discarding all other nonnegative loss gives

    R_null >= (ck/(128M)−2S) sum_(j=J0)^T 1/j.

For a nonnegative coefficient the harmonic integral lower bound is log((T+1)/J0). For a negative coefficient use risk nonnegativity. This proves KH3 with its stated positive part. The finite statement also allows J0=T: the sum then has one term and the integral bound remains valid. No stronger assumption J0<T is hidden.

Because delta>=1/sqrt(M) and k>=2sqrt(M), the log(1+u)<=u bound gives F2<=k/M+1/(M delta)<=2k/M, while s<=k/(2M). Thus H2<=2k/M including the cap. The benchmark is unchanged by the extra observed windows.

## 11. Critical-certificate growing widths and floors

At beta=1/M, let r=r_M>=2 be integer with r=o(M^(1/6)), without any monotonicity requirement. Set U=M/r, L=M^(5/6), and k=floor(sqrt(U L)). Then U/L=M^(1/6)/r tends to infinity, while U,L and sqrt(U L) tend to infinity. If q=sqrt(U L), 0<=q−k<1 implies k/q tends to one. Consequently

    k/L -> infinity,   k/U ->0.

In particular k/sqrt(M) tends to infinity and

    delta^5 k^3=k^3/M^(5/2)=(k/L)^3 ->infinity,
    delta^3 k^2=k^2/M^(3/2)=(k/L)^2 M^(1/6) ->infinity.

Also k delta=k/sqrt(M) tends to infinity, r/k tends to zero, r delta=r/sqrt(M) tends to zero, and kr/M=k/U tends to zero. Since r>=2, k/M<=kr/(2M) tends to zero. These limits imply every inherited and additional finite numerical threshold eventually, including k<=T, r<=k/4 and r delta<=1/16.

The ceiling is controlled by

    J0<=k+16crk+1,

so J0/M tends to zero. Meanwhile T/M=floor(M/8)/M tends to 1/8. Hence J0<=T eventually and log((T+1)/J0) tends to infinity. The relevant harmonic range pays the product rk: merely knowing k/M tends to zero would not suffice for arbitrary growing r.

An all-budget guarantee with a single finite C on this prescribed sequence gives S<=C/sqrt(M) from k=0 at the **same** beta and r. Therefore 2S is negligible relative to ck/(128M). Eventually KH3 is at least

    [ck/(256M)] log((T+1)/J0).

Its ratio to H2<=2k/M is at least (c/512) times that diverging logarithm. This contradicts any such finite C, even if C and the maps depend on the whole prescribed width sequence. Stationary witnesses already suffice.

This is a sufficient nonadaptivity regime, not a sharp width threshold. The proof does not decide r of order M^(1/6), larger r, or full history. The diagnostic's large finite near-threshold widths are finite tests, not substitutes for this analytic little-o argument.

## 12. Bounded-width arbitrary-domain synthesis

Here the inherited KH002 public-domain ranges remain M>=64 integer and beta in [0,1]. Add integer 2<=r<=r0 for one fixed finite r0, and 2r<=M+2. Define G(M,0)=0 and G(M,beta)=min(M²beta,1/(beta sqrt(M))) for positive beta, independent of r.

If G is bounded, the same ordinary add-one estimator from KA001/KH002 works on the fixed weak/strong union and ignores the extra windows. It uses only triple counts and the final pair, is independent of k, beta, r and the domain, and its constant can depend on the fixed band bound. The positive bound holds for all starts, not just stationary starts.

If G is unbounded on the triple domain, select a sequence of triples with G>=n. Exactly KH002's argument gives M tending to infinity, M²beta tending to infinity and beta sqrt(M) tending to zero. Set beta_w=max(beta,1/M) and use

    U=1/beta_w,
    L=max(sqrt(M),beta_w^(−5/6),beta^(−1/2)),
    k=floor(sqrt(U L)).

KH002 proves L/U tends to zero, k/L tends to infinity, k/U tends to zero, and k sqrt(beta) tends to infinity. All KH001 conditions at beta_w hold eventually. Since r<=r0, additionally r<=k/4 and r sqrt(beta_w)<=1/16 eventually. The bound

    J0/k<=1+16cr0+1/k

is uniform, so T/J0 tends to infinity. This validates KH003's finite-window theorem at the witness certificate along the selected sequence.

Fix the actual map A_(M,beta,r). Every witness satisfies beta_w>=beta and thus lies in the actual source class. Apply the **new finite window inequality**, universal over maps on T_r, to this fixed actual map. No map at metadata beta_w is substituted, and the width metadata is unchanged. The clean S<=C/sqrt(M) guarantee is at actual beta. The null's true target remains beta_w, because changing a valid certificate label does not change its transition law. The clean gap and word probabilities likewise remain those constructed at beta_w.

The actual-beta benchmark comparison is licensed by k sqrt(beta)>=1, not by incorrectly using the witness cutoff: sqrt(beta)>=1/k>=1/M, so F2(M,k,beta)<=k/M+1/(M sqrt(beta))<=2k/M. Together with the clean floor this gives H2(M,k,beta)<=2k/M. The clean penalty is negligible compared with k/M and the harmonic range diverges, contradicting adaptation with one constant on the selected triple sequence.

This proves the exact bounded-width domain criterion for stationary-only guarantees and, using the positive arbitrary-start upper, for all-start guarantees as well. Empty domains, beta=0, finite exceptional horizons, sparse domains and oscillating certificate values remain covered as in KH002. It is not a criterion for arbitrary growing-width domains.

## 13. Exact observation scope and a concrete non-transfer witness

The theorem concerns two boundary windows, not all radius-r neighborhoods throughout the word, their counts, arbitrary local encoders, sliding-window embeddings, or the full ordered history. The mathematical transfer only follows from equality of T_r.

There is a small literal qualification to the manuscript's general longer-pattern exclusion: at r=3 the length-r histogram is the triple histogram already supplied, and at r=2 the pair histogram is recoverable from triple counts plus the final pair. The exclusion is substantive for general larger r, not a claim that those already supplied shorter counts are unavailable. This wording qualification does not alter any theorem or require a proof revision.

For example, at r=4 the original word

    111100010000

canonicalizes to

    111100100000.

Both start with 1111, end with 0000, and have identical triple counts. But the count of 0000 rises from one to two, the count of 0001 falls from one to zero, and 1001 appears. Thus this construction does not generally preserve interior length-r pattern histograms even when it preserves both r-symbol boundary windows. The example is a structural scope witness, not a small instance satisfying the theorem's enormous finite inequalities.

No encoder or architecture conclusion is available unless that encoder is independently proved to factor through this exact statistic. Nor does the obstruction show that observing more order is sufficient for adaptation.

## 14. Independent exact checks, provenance, and disposition

The separate reviewer script does not import or run the author checker. The author checker and its output were inspected before the reviewer implementation, so this is **not** claimed to be a blind-to-author-diagnostics audit. The mathematical derivations above and the code are fresh reviewer work.

The final diagnostic passed **813,101 assertions**, using only exact integers and fractions, with certified adjacent-power tests for radical floors. Its coverage includes all 16,383 endpoint-11/00 words of lengths 4 through 17; 212,993 fixed-presampling-j Hamming inequalities; 76,842 last-zero witnesses; 180 exact boundary DPs with explicit late transition fluxes; 12,240 full-word reversal checks; 60 stationary boundary-event/bridge identities; 144 small exact randomized-predictor kernel transfers; 79 complete huge-domain parameter choices and 391 source-family members; 6,256 all-state entries checked at both witness and actual certificates; exact null masses and targets; and the single-suffix case J0=T. The separate output records all individual counts.

During reviewer diagnostic development, I corrected my own initial finite nesting implementation: using an integer-truncated exponent for beta_w^(−5/6) would test a nearby budget, not always the claimed exact geometric budget. The final code instead computes the certified twelfth-root floor of

    max(M³ beta_w^(−6), beta_w^(−11), beta^(−3) beta_w^(−6)),

which is exactly (sqrt(U L))^12. I also separated actual assertions from auxiliary case counters and added the J0=T check. The actual earlier diagnostic files and exact code diff are retained as audit history, not presented as the final evidence. This correction concerns the reviewer checker only; no candidate or accepted proof change was made.

Small exhaustive/DP/kernel tests are explicitly structural checks outside the full theorem domain. Huge-domain arithmetic checks test the listed inequalities and source tables, not full stochastic path enumeration at those horizons. Finite checks do not prove universal real-parameter, asymptotic, common-kernel, or estimator-family claims; those are the analytic arguments audited above. No formal or external-review status is inferred.

**No mathematical correction is requested for the frozen candidate.** The separate bindings manifest records this review, the final checker/output, the received snapshot, the actual author revision history, reviewer-checker history, and accepted dependencies. Any root acceptance or later summary should keep the exact boundary-only observation restriction, the r=2/3 qualification, the non-sharp growing-width range, and the actual-beta/witness-beta distinction explicit. This material is a future third-increment review and does not modify or delay earlier publication batches.
