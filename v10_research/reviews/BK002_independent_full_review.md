# BK002 — fresh independent full mathematical review

**Verdict: no substantive mathematical defect found in the frozen reference-sampler proof.** The exact finite constrained-risk inequality, the unrestricted full-corrupted-history supplied-beta adaptation impossibility, and the square-root public-envelope boundary are supported by the argument as written. Root acceptance remains a separate decision. This is independent LLM corroboration, not formal verification, external peer review, or a novelty assessment.

Reviewed source:

- `binary_beta_known_adaptation/BK002_full_history_supplied_beta_obstruction.md`
- SHA256 `e50381632af4825923138c086c34e7b3b082af381d4b9ec8f641825455c50e12`

The review was performed on 2026-11-02. I read the entire BK002 manuscript and the complete accepted AB001, AB003, SC003, BT002 main proof and BT002 scalar completion. I verified their source hashes against the current acceptance receipts. I also inspected SC002 §§1–2 for the ancillary fixed-positive-beta remark. The author confirmed the displayed reference-sampler version was frozen. No author proof was edited.

## 1. Exact snapshot and scope

The reviewer independently preserved the received bytes in `reviews/BK002_audit_snapshots/BK002_reference_sampler_received.md`. The final source is byte-identical; `received_to_reviewed.diff` is an actual empty unified diff. The author also preserved `binary_beta_known_adaptation/revisions/BK002_initial_candidate.md`, which has the same hash. The accompanying binding manifest records the final proof, snapshots, diff, checker, results, dependencies and acceptance receipts.

The accepted result here is a constraint on one estimator map used at a common supplied valid certificate, both on clean alternatives and on an attacked null. It is **not** a histogram restriction. It is **not** an assertion that the displayed beta is each source's maximal minorization coefficient. It is **not** a new larger known-k minimax lower. It does not settle a prescribed moving-beta curve such as beta=1/M for unrestricted full-history estimators.

The final audited manuscript did **not** adopt the optional actual-clean-continuation sampler. The proof uses the reference sampler, exact ordered-path likelihood domination by 1/4, and therefore the finite constants 3/2048 and 32. All checks below bind that actual version.

## 2. Domain and stationary family

Write T=floor(M/8). The theorem is conditional on existence of integer k satisfying k²>=4M and k<=T. It does not claim such a k exists for every M>=256; for example some floor-sensitive M immediately above 256 have an empty admissible set. This is harmless. Whenever the domain is nonempty, k>=32, so all uses of k>=2 and delta<=1/4 are conservative.

For a in I=[k/(32T),1/16],

- a>=k/(4M)>=1/k=delta;
- 0<delta<=1/4 and 0<tau=1/(4M)<=1/4;
- e=1-delta>=3/4.

For x=[e/a+2+delta/tau]^-1, Pi=(ex/a,x,x,x delta/tau) is positive and sums to one. The balances Pi00*a=Pi10*e and Pi11*tau=Pi01*delta, together with equal crossing masses, establish all four stationarity equations. This is a homogeneous second-order source initialized at its own stationary pair law, not a source changing with suffix length.

Since delta/tau=4M/k, x<=k/(4M). Moreover

    Pi11 = [1+e k/(4Ma)+k/(2M)]^-1.

The denominator is at most 1+e+1/16<3, since a>=k/(4M) and k<=M/8. Thus Pi11>=1/3. The stationary mass and the clean prefix probability remain uniformly substantial in exactly the way required later.

## 3. All sixteen minorization entries

I independently squared the actual transition matrix in state order (00,01,10,11), obtaining exactly the matrix displayed in BK002 §2. Its entries are compared with beta Pi=delta²(y,x,x,w), with y=ex/a and w=x delta/tau.

A complete partition of the sixteen entries is as follows.

1. The entries (01,10) and (11,01) are delta*tau. They dominate delta²*x by x<=tau/delta=k/(4M).
2. The entry (11,00) is tau*e. Its target satisfies delta²*y=delta²*e*x/a<=e*delta*tau/a<=e*tau.
3. The entries (00,11), (01,11), and (10,11) are a*delta, delta*(1-tau), and delta². They dominate delta²*w because a>=delta, 1-tau>=delta*w, and w<=1.
4. The entry (11,10) is (1-tau)*tau>=delta*tau>=delta²*x.
5. The entries (01,01) and (10,10) are e*delta and delta*e, at least delta²*x.
6. The entries (00,01) and (10,01) are (1-a)*a and e*a. Because x<=a/e, it is enough that 1-a and e exceed delta²/e. The stated bounds give delta²/e<=1/12, while both left factors exceed 3/4.
7. The remaining four entries are (1-a)², e², e(1-a), and (1-tau)². Each is at least 9/16, while its target is at most delta²<=1/16.

This accounts for 2+1+3+1+2+2+4=16 entries, including every starting state. The proof is not merely a stationary-support check.

For the symmetric first-order null, Pi*(s,t)=T_r(s,t)/2 and P*²((u,v),(s,t))=T_r(v,s)T_r(s,t). As r<=1/2, T_r(v,s)>=r, giving P*²>=2r Pi*. Here 2r=1/M>=1/k²=beta. A common **valid advertised** certificate is all that the class requires; equality with each maximal coefficient is unnecessary. The actual null target at pair 00 is r.

## 4. Exact full-word and prefix probabilities

The null word x^(t)=1^(M+1-t)0^(t+1) has N=M+2 bits. It starts in 11 for all relevant t, crosses once from 1 to 0, and ends in 00. Multiplying from the stationary first bit gives

    (1/2)(1-r)^(M-t) r (1-r)^t
      = (r/2)(1-r)^M.

This confirms the exponent M, including the initial-pair contribution. The words are disjoint. The bounds 1/(8M)<=v<=1/(4M) follow from r=1/(2M) and Bernoulli's inequality.

Under Q_a, the first-zero prefix uses initial 11 mass w(a), M-t-1 subsequent 11-to-11 transitions, and one 11-to-10 transition of probability tau. Thus its exact probability is w(a)(1-tau)^(M-t-1)tau, as stated. The remaining suffix has exactly t transitions from pair 10. Since w(a)>=1/3 and (1-tau)^M>=3/4, the prefix mass is at least 1/(16M), whence v<=4 w_(a,t).

For a **fixed** a, first-zero events indexed by t=1,...,M-1 are disjoint portions of a single stationary-source experiment. Restricting to terminal pair 00 makes the true next-symbol-1 probability exactly a. Thus their weighted e_(a,t) contributions sum to at most the unconditional clean risk, and hence at most S. No conditioning is charged for free, and no source is selected independently for each suffix length when applying this clean guarantee.

## 5. Reference suffix, acceptance, and exact ordered likelihood

From initial pair 10, the reference process cannot visit 11. Its symbol-1 probabilities are delta from 10, a from 00, and zero from 01; all are at most a. Hence E_R L<=at<=k/16 on I_t. Markov's inequality gives P_R(L>k)<=1/16.

From every reachable pair, the next zero has probability at least 1-a. Therefore two successive final zeros have probability at least (1-a)²>=9/16, without conditioning on earlier successes. The t=1 observation in the manuscript is valid but unnecessary in the actual domain, where t>=k>=32. Subtracting the budget failure gives P_R(G)>=1/2.

For each individual reference-supported suffix, the only transition probability changed in the actual source is 01-to-10: its reference probability is 1 and actual probability is 1-delta. Every departure from 01 follows an emitted one because the starting pair is 10. Thus N01<=L, including the possible final emitted one that has not yet departed. On G, N01<=k, and

    actual_path_mass/reference_path_mass
      = (1-1/k)^N01 >= (1-1/k)^k >= 1/4.

The last bound holds for every real k>=2 by the derivative calculation in the manuscript, or by the standard monotonicity of that sequence. This identity concerns each complete **ordered** suffix; the unchanged full prefix then makes it an identity on each corresponding full output word. It does not discard timing or order and does not invoke type classes, IID row observations, or sufficient histograms.

Summing against any nonnegative full-word functional proves (4.3). In particular it remains valid for an estimator that uses arbitrary order information, unlimited computation, and independent randomization.

## 6. Kernel legality and loss comparison

The attack is a total stochastic map on the finite set of input words: identity off the specified null words, and on each such word a uniform auxiliary a draw followed by the explicit reference sampler and acceptance test. Its auxiliary a is sampled from a public interval determined by M,k,t, not read from an unknown source. The table is the same on every source.

The first zero and preceding prefix are retained. An accepted replacement ends in 00 and changes exactly the number L<=k of suffix ones relative to the original all-zero suffix. Consequently every changed position lies among positions 1,...,M; the last two actual bits are protected. Rejections are identity. The budget is pointwise, not merely in expectation. There is no rejection resampling that would alter the claimed acceptance law.

A uniform continuous auxiliary draw defines a legitimate stochastic map by integration. In this reference construction each output probability is polynomial in a with rational coefficients, so the additional claim about a finite rational kernel is also sound. No efficiency claim follows or is required.

On accepted outputs, the null's actual target is r while the clean comparison's target is a. Since a>=1/k>=1/M=2r, the triangle inequality yields a-r>=a/2. Multiplying by acceptance probability at least 1/2 and subtracting the reference comparison error gives a/4 minus that error. Exact domination bounds the error by 4 e_(a,t). Discarding rejected losses is legitimate because they are nonnegative. This proves (5.1), including possibly negative right sides.

Estimator randomization can be averaged after applying the pointwise triangle inequality and nonnegative-functional domination; it need not be coupled with the attack seed, and the attack does not inspect that seed.

## 7. Common-a integration, signs, and finite constants

I_t has width k/(32t), density 32t/k, and mean 3k/(64t). Also I_t is contained in I because k<=t<=T. Therefore the positive contribution after (5.1), before summing v, is 3k/(256t). The lower v bound gives 3k/(2048M) times the harmonic sum. Monotonicity gives

    sum_(t=k)^T 1/t >= integral_k^(T+1) dx/x
                       =log((T+1)/k).

For the error term, the constants are exactly

    factor 4 from likelihood domination
    × factor 4 from v/w
    × factor 2 from density <= 2/a
    =32.

The density inequality follows from a<=k/(16t). Exchanging a finite sum and a nonnegative integral, and applying the clean guarantee at each **same** a, bounds the error by

    32 S integral_[k/(32T),1/16] da/a
       =32 S log(2T/k).

No prior is claimed to remain uniform after observing a prefix or endpoint. The positive and error contributions are separately nonnegative before subtraction, so lowering the former and raising the latter has the correct sign. Risk is nonnegative, which justifies the final positive part. At T=k both logarithms are still well-defined and positive; the finite statement can be weak or clipped to zero there, with no logical defect.

Thus the exact displayed BK2 inequality, with constants 3/2048 and 32, follows for every admissible finite M,k and every full-history estimator under the stated common-map premise.

## 8. Impossibility and range envelope

A universal adaptive C H_2 guarantee at the clean point k=0 of the **same advertised beta=1/k²** applies to every Q_a, giving S<=C/sqrt(M). Here k names the later attacked-budget scale in the construction, not an input that changes the clean estimator branch.

The ratio of the error bound to the positive term is exactly bounded by

    (65536 C/3)(sqrt(M)/k)
      log(2T/k)/log((T+1)/k).

On any sequence with k/sqrt(M)→infinity and log(M/k)→infinity in the finite domain, the log ratio tends to one and the other factor tends to zero. This leaves a fixed positive multiple of (k/M)log(M/k). The example k=floor(M^(3/4)) satisfies all finite conditions eventually.

At the same supplied beta, max(sqrt(beta),1/M)=1/k. Hence F_2=(1+log 2)k/M. Moreover the finite domain already gives M^-1/2<=k/M, so H_2<=2k/M. The ratio of the constrained-risk lower to this benchmark diverges. This proves uniform-in-beta impossibility even with stationary initialization. The arbitrary-start impossibility follows because it includes the stationary subclass.

There is no contradiction with known-k minimax estimation: a method invoked with a large known maximum budget need only achieve the correspondingly larger rate on an identity attack. BK002 demands the clean k=0 rate as well from the same map. Nor is it a defect that beta numerically reveals the adversarial scale: it does not identify whether the current history is clean or attacked.

For the envelope result, if b_M/sqrt(M) is unbounded, choose M_n→infinity along which that ratio diverges and let k_n=min(b_Mn,floor(M_n^(3/4))). Then k_n/sqrt(M_n)→infinity, k_n is allowed by the envelope, both finite inequalities hold eventually, and log(M_n/k_n)→infinity. The same contradiction therefore applies even to estimators designed using the public envelope.

Conversely, an O(sqrt(M)) envelope has a finite global integer bound L after absorbing finitely many exceptional M. Accepted AB003 §8 supplies a deterministic estimator blind to both k and beta, threshold 12L ceil(sqrt(M)), and risk at most min(1,2^18 L M^-1/2+2^22 F_2). This is a constant multiple of H_2, with the permitted dependence on L. Its arbitrary-start guarantee implies the stationary one. Consequently the claimed if-and-only-if boundary is correctly quantified. It is not a pointwise impossibility at each k>sqrt(M), particularly not at k comparable to M.

## 9. Dependency and ancillary-scope audit

The receipt-bound AB001, AB003, SC003, BT002 main and BT002 scalar source hashes all match their accepted bytes. The AB001 and AB003 receipt-specified review hashes also match. These were verified from disk, not inferred from candidate headings that still say “candidate.”

- The finite BK2 proof is self-contained probabilistically and does not borrow AB001's invalid-at-common-positive-beta alternatives.
- AB001 supplies context and the general constrained-risk strategy, not the new common-beta certificate.
- AB003 §8 is the required upper direction of the sharp envelope claim.
- SC003 and BT002 together justify calling H_2 the accepted known-k binary profile. The adaptation contradiction itself only needs the proposed benchmark formula and the clean guarantee; it does not reuse BT002 transport.

Nonblocking exposition note: §9's fixed-positive-beta k-blind remark is consistent with the generic add-one upper, not with the k-aware SC003 theorem alone. SC002 §§1–2 gives that ordinary-add-one proof using only the pair-state occupation interfaces and all-state minorization; its upper argument applies to K=2 as well (the K>=3 restriction is needed for its matching lower/frontier statement). For a fixed beta>0, its bracket is bounded by 1+log(1+1/beta), yielding a beta-dependent constant times max(M^-1/2,k/M). Thus the remark is correct, but an explicit citation to the generic upper would improve provenance. This does not affect any BK2 calculation or the envelope equivalence.

No causal attacker, public edit mask/seed, editable endpoint, efficient adversarial implementation, neural resource, training, formal verification, or external novelty conclusion is warranted. The manuscript correctly preserves those restrictions.

## 10. Independent exact diagnostics

`reviews/BK002_independent_exact_checks.py` was written independently, without reading or importing the author's checker. I did see the author's reported aggregate counts, which were not used as a correctness argument. The independent implementation builds the transition matrix from successor bits rather than copying the squared matrix, then checks the displayed square and all inequalities using `fractions.Fraction`.

The completed run reports:

- 235 exact stationary alternative cases, covering 3,760 all-state certificate entries;
- 752 exact null certificate entries;
- 312 exact prefix-probability, interval and density cases, including floor-sensitive domains;
- 18 exact reference/actual continuation DPs at legal theorem points with horizons 32 through 80;
- 108 nonnegative-functional and loss tests, including order-sensitive binary-word-modulo-7 decoding and independent randomized decoding;
- 1,932 exhaustive accepted ordered-path likelihood/budget/endpoint checks over separate small structural tests;
- 298 exact checks of (1-1/k)^k>=1/4;
- explicit exact coefficient checks for 3/2048, 32 and 65536/3.

The minimum reference acceptance among the legal DP instances is approximately 0.8857142857, safely above 1/2; the JSON retains its exact rational value. The small exhaustive path tests are explicitly labeled structural tests outside the main theorem's M,k domain, not misrepresented as finite-domain theorem instances. The DP order-sensitive functionals are tests of the full-word inequality, not a replacement for its general pathwise proof.

All diagnostics pass **for tested instances only**. They do not formally verify the universal integration, asymptotic, or quantifier arguments; those were independently reconstructed above. No substantive revision is requested. Any later proof-byte change requires a new hash binding and review of its actual diff.
