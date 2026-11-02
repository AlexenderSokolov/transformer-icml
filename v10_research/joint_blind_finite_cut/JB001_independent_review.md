# JB001 — Independent full review

2026-11-02. **Verdict: PASS. No mathematical or resource revision required.** This is an independent LLM audit with exact finite diagnostics, not formal proof verification, external peer review, novelty certification, or root acceptance. No theorem file was edited. This work is post-stage8 and was not published.

## Exact reviewed version and scope

Complete reviewed theorem: `JB001_theorem.md`, SHA-256

`9d28b2b655be1cf643ac8fc0881aa3952047bc618850c64e31a051e8cc67c9c3`.

I read the entire new theorem, the entire accepted JP001 theorem and independent review and its receipt, and the entire accepted AB003 theorem (including its range-envelope corollary), independent review, and receipt. I additionally read the relevant exact interfaces in SC003, BIF001, BAI003 v2, BC001, and FA001 v3: SC003's clean comparator and universal occupation; BIF001's support classification and arbitrary-real-A full-support occupation proof; BAI003 v2's complete absorbing-case proof; BC001's exact uniform-bank and cost sections; FA001's finite arithmetic, positive Taylor weights, exact accumulator semantics, and sequential cost schedule. Receipt hashes for all seven direct proof files match. JP001 and AB003's accepted independent-review hashes also match. Full machine-readable bindings are in `JB001_independent_checks.json` and `JB001_independent_review_bindings.json`.

The approved scope is exactly one fixed paid binary eight-coordinate uniform histogram prefix, source edits among the first M symbols, one-shot vector coordinatewise port noise, final Q flooring, and only the protected terminal pair plus source-independent public information at the cut. The new decoder is blind to k, delta, beta, and every numerical budget certificate. The upper is simultaneous only where k/M+delta+1/Q<=M^(-1/2). This is neither an all-budget adaptation result nor a lower bound for redesigned encoders.

## 1. Exact experiment and port

The source, clean target, protected endpoints, attack timing, and both initialization conventions agree with JP001. Editing the interior cannot change the row selected by the terminal pair. The target is the original source law at that actual terminal pair, not a corrupted law or an independently sampled query.

The encoder's finite arithmetic identity is exact, not an approximation inherited outside its precision range. With zero Q/K scores, FA001's Taylor recurrence produces a common positive integer W on every edge, with its zeroth term already ensuring W>=D>0 for every P>=h. Exact indicator values are D times zero or one, so the terminal denominator is MW and the coordinate numerator is WD C'. Their exact quotient is floor(D C'/M). Zero/one affine copies preserve it. The smaller precision assumption P>=h is therefore sufficient even though FA001's general approximation theorem has a larger precision schedule. At zero port noise, Q divides D and nested flooring returns exactly floor(Q C'/M)/Q.

The claim retains JP001's actual eight-coordinate bank, not the distinct 9K+1 SRC bank. No first-boundary, numerator, denominator, count, hidden state, history, attack-mask, or seed port is silently imported. The common Taylor weight need not equal one or D and need not be numerically approximated by an exponential for this argument.

## 2. Pathwise noise and edit error

For a true corrupted frequency x in [0,1], clipping fixes x and is nonexpansive. Since the finite bank differs from x by less than 1/D, a coordinate perturbation of magnitude at most delta followed by the Q floor gives an error at most delta+1/D+1/Q<=delta+2/Q. This remains true at clipping boundaries and for attacks selected from the full history and actual bank. A vector attack may affect all eight coordinates; it is not one-scalar sparsity.

One changed symbol affects at most three counted triples, each contributing at most two to histogram l1 distance. Hence the full histogram difference is at most 6k even for adjacent edits. Restriction to the selected two-coordinate row cannot increase this bound. Adding the two port errors gives

    d=6k+2M(delta+2/Q)<=6M(k/M+delta+1/Q).

This implies both scalar errors |tilde C-C|<=d and |tilde J-J|<=d. In the stated region d<=6sqrt(M)<=B/2. Neither d nor any attack parameter is a decoder input. Nonnegative pseudo-counts need not be integers, sum to M, or be realized by any word.

## 3. Hard-threshold extension to real pseudo-counts

The proof extends AB003 correctly. I rederived it for arbitrary nonnegative real two-coordinate pseudo-rows, assuming only the l1 error bound and d<=B/2.

On the inactive branch, C<=B+d<=3B/2. When q>0 and J>3B/q, p=C/J<q/2, so q<=2|p-q|. Otherwise the threshold event pays q. At J=0 the event pays the whole loss; at q=0 its specified zero value is correct. There is no division by q at runtime.

On the active branch, C> B-d>=B/2>=d, so the clean integer J is at least one. The nonnegative pseudo-row gives 0<=p'<=1 and a positive denominator. Inserting tilde C/J gives

    |p'-p| <= (|tilde C-C|+p'|tilde J-J|)/J <=2d/J.

For J>=2d and d>0, tilde C<=C+d<2C and tilde J>=J-d>=J/2, hence p'<=4p. For J<2d, p>d/J>1/2 and p'<=1; d=0 is immediate. Since p and p' are nonnegative, |p'-p|<=max(p,p')<=4p. The min bound and the four-Lipschitz truncation therefore give

    |p'-q|<=5|p-q|+min(4q,2d/J)
           <=5|p-q|+4min(q,6d/(J+2)).

The last step is conservative for every integer J>=1. This proves the displayed combined envelope, including exact threshold equality and its strict active side. The lemma does not rely on independence, integer pseudo-counts, a realizability constraint, or statistical properties of the attack. All stochastic inputs remain original clean analysis variables.

## 4. Expectation interfaces and complete domains

The clean comparator coefficient is precisely SC003's (8192+1)sqrt(32)/sqrt(M+1), inherited by AB003. It does not claim that terminal-selected empirical rows are IID.

AB003's threshold-bias proof applies unchanged because the threshold B is unchanged and its event is expressed in clean counts. For each fixed state u with q_u>0, w_u=floor(3B/q_u)+1 is a fixed integer. Its selected-row event is contained in {J_terminal<w_u}; summing four separate universal-occupation bounds gives 64(3B+1)/(M+1)<=2600/sqrt(M). This is not an invalid substitution of a random threshold into an unconditional occupation bound. Zero-weight rows contribute zero, including arbitrary unsupported starting states.

The replacement A=6d+2 is sound: min(q,6d/(J+2))<=min(q,A/(J+2)) and A>=2, even when d=0. JP001's continuous occupation completion is valid for every such real A:

- Full support and beta>=M^(-2): BIF001 equation (3.4) allows every real A>0, arbitrary initial laws, and the fixed orientations (a,b,e,t). Its suffix proof does not require a stronger suffix-scale minorization.
- Positive beta and non-full stationary support: the all-state certificate forces a singleton absorbing diagonal. BAI003 v2 equation (6.2) covers arbitrary remaining rows and starts, including unsupported or transient states, and symbol exchange preserves the public orientation. For A>=2, 256A/M+16/(M+2)<=264A/M.
- beta<M^(-2), including zero: the universal layer-cake bound controls the functional without any support assumption. Its scalar comparison gives at most 16f_(1/M)(A/M). Equality beta=M^(-2) belongs to one of the positive-beta cases.

Thus the uniform 4s+16672f_e(A/M) bound has no endpoint, support, or initialization gap. The proof uses true exit weights, not unit crossing caps, and does not infer global square-root-beta mixing.

## 5. Profile algebra, constants, and simultaneous quantifiers

Since A/M<=36tau+2/M, increasing subadditivity and f_e(cx)<=cf_e(x) for c>=1 give

    f_e(A/M)<=36f_e(tau)+f_e(2/M).

These properties follow directly from JP001's derivatives and f_e(0)=0. The estimate f_e(2/M)<=8s is valid uniformly because e>=1/M and ln(1+M/2)<=sqrt(2M). No evaluation at a zero logarithmic argument is needed. Finite Q makes tau positive, although the continuous f_e(0) convention is still consistent.

The resulting statistical coefficient is

    5*8193sqrt(32)+2600+16+32*16672 <2^20,

and the profile coefficient is 144*16672=2,400,768<2^22. The exact diagnostic checks the first inequality by squaring its two positive sides, without a floating approximation. Unit binary TV supplies the cap. Replacing sqrt(M+1) by sqrt(M) only enlarges the upper bound.

The algorithm itself never varies with k, delta, beta, rho, or an estimate of these quantities. The same deterministic map therefore obeys the bound separately for every admissible tuple in the stated region, against every admissible cooperating attack. Both initialization models use this identical map. The definition remains a legal simplex-valued map outside the region, but the proof appropriately makes no sharp guarantee there.

## 6. Lower comparison and information direction

JP001's accepted known-budget lower concerns this exact fixed prefix and terminal-pair side port. A decoder receiving the budgets and an admissible certificate has at least as much information as one that ignores them. Restricting to the new blind decoder family cannot improve that lower. Its lower witnesses keep public parameter information source-independent and fixed across their priors. The certificate was required for JP001's different constructive upper, not for the existence or validity of its lower witnesses.

The statistical, editing, and precision/noise witnesses in JP001 are combined by maximum, not by an unjustified sum of risks or a common worst source. The fixed-bank precision inclusion has the correct direction and remains a statement about the fixed eight-coordinate prefix. No optimized or deep redesigned-encoder lower is inferred. Since s+f_e(tau)<=2max(s,f_e(tau)), the new capped upper and inherited capped lower give the claimed simultaneous order comparison in the restricted region.

## 7. Finite arithmetic and paid resources

There is no hidden real input to the decoder. Each received coordinate is n_i/Q with 0<=n_i<=Q; the full label length pays h+1 bits and determines Q. Exact rational pseudo-counts M n_i/Q have O(h+log(M+2)) full description length. The threshold is an integer square root followed by one exact comparison. Squared-integer binary search needs O(log M) school-arithmetic iterations, so O(v^3) bitwork with v=O(h+log(M+2)) is conservative, as is O(v^2) scratch.

More concretely, the active branch can compare M n_exit>BQ by integer products and serialize the designated output directly as n_exit/(n_0+n_1), with the other numerator its nonnegative complement. The common M/Q cancels; a fraction-reduction routine or real division is unnecessary. Its denominator is positive on the active branch. The inactive branch serializes zero and one. The whole bank may have total mass different from one without affecting validity.

A fixed-control sequential bit algorithm implements these scans, integer products, comparisons, and square-root loops with bounded code and paid counters. Thus the decoder cost need not depend on P or any compactly encoded noise certificate; P is paid by the inherited encoder, and no rho is supplied. All-token execution, if required by the chosen syntax, multiplies decoder work by M+3 and retains/charges its code, output/held records, and buffers. The theorem explicitly adds these to the full JP001 prefix and simultaneous handoff resources rather than replacing them by scratch alone.

JP001 retains all-token masks, zero coefficients, exact full-width accumulators, table generation, finite Taylor evaluation, and access-cut cleanup. No free history reread or physical noise/isolation gadget is claimed. Output precision is an explicit finite rational representation, not automatically the Q grid; the text does not conflate h, P, output bitlength, or compiled neural depth. I found no missing resource necessary to realize the asserted decoder.

## 8. Independent exact diagnostic evidence

`JB001_independent_checks.py` was written without reading or reusing the author's diagnostic program. Its PASS output is `JB001_independent_checks.json`. Every assertion uses integer or exact rational arithmetic, not floating comparisons. Results:

- 72,294 relaxed real/rational pseudo-row configurations: 7,757 active and 64,537 inactive;
- 383,000 critical-probability/midpoint inequalities, including all piecewise-linear breakpoints for each tested row, plus 7,437 threshold right-limit checks;
- 378,738 exact common-positive-Taylor-weight cancellation and nested-floor configurations;
- 11,760 scalar noisy-bank cases, including clipping and non-dyadic rational perturbations;
- 33,750 finite M>=64 edited-word/noisy-bank cases within the exact squared operating-region test, including 14,339 nonintegral selected pseudo-rows, 29,255 nonunit total pseudo-histograms, and 42,637 clipped coordinates;
- every integer M from 64 through 100000 for the threshold constant: 99,937 cases;
- exact assembly constants, singleton-A comparisons, and all seven accepted dependency proof hashes plus both main dependency review hashes.

The relaxed row tests include non-grid rational denominators, zero error, q=0 and q=1, J=0, exact threshold equality, strict fractional threshold crossings, and both d=B/2 and smaller errors. Finite bank tests include P=h and P>h, count-zero/count-M endpoints, zero noise, zero source edits, simultaneous edits and noise, and all four possible protected row labels through the chosen words.

These diagnostics corroborate only the finite instances tested. The analytic audit above, not their count or PASS status, is the justification for the full mathematical review. No failed case was suppressed and no revision was requested. Root acceptance remains a separate decision.
