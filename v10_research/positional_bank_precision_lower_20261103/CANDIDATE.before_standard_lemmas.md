# PBP001: matching precision lower bound for the fixed positional bank

2026-11-03. Candidate for root review, not accepted or published. Root supplied the collision-interval proof route; this unit verifies it and supplies constants, the complementary full-history floor, and exact diagnostics. The lower proof is self-contained. The matching upper bound imports accepted ACG001. FPA001 is used only to identify its exact observation cut, not as an accepted theorem.

## 1. Precisely fixed experiment and claim

Fix integers M>=64 and h>=0, and Q=2^h. Given a binary word X_0,...,X_(M+1), define J_u,C_u,D_u exactly as ACG001: departures i=0,...,M-1, pair u=(a,b), designated successor 1-a, and half departures i=0,...,floor(M/2)-1. Form the twelve coordinates (J_u/M,C_u/M,D_u/M), each separately rounded to the nearest point of {0,1/Q,...,1}, with a fixed tie rule. Call the resulting bank B. The observation is ONLY O=(B,X_M,X_(M+1)), plus source-independent public metadata. The endpoint is exact. No raw history, scratch counts, other token banks, rounding residual, or additional feature port is available. FPA001's ties-up prefix produces precisely this bank.

Let C_M be ACG001's clean (k=0) class: homogeneous binary order-two sources with arbitrary initial law admitting a stationary pair law Pi and all-state P^2(u,v)>=Pi(v)/M. Let

    R*(M,h)=inf_decoder sup_source in C_M E TV(output,next-symbol law at actual endpoint).

The infimum permits arbitrary computation, arbitrary real-valued binary probability output, and independent randomized decoder seeds. It does not restrict to FPA001's particular gate or finite readout. There are numerical universal constants such that

    (1/1600000) max{M^(-1/2),2^(-h)}
       <= R*(M,h)
       <= min{1,667160 max{M^(-1/2),2^(-h)}}.                 (1)

In particular R*=Theta(max{M^(-1/2),2^(-h)}). Both lower components already hold on the clean stationary IID Bernoulli subclass p in [1/8,1/4]. This is a lower bound for THIS deterministic coordinatewise rounded bank, not for all encoders using 12(h+1) bits, all positional summaries, all neural networks, or total arithmetic precision. It is not a robustness lower in delta and does not claim a k/M lower. The clean subclass remains a valid lower for any adversarial model allowing zero edits.

## 2. Exact expectation polynomials and monotonicity

Under stationary IID Bernoulli(p), write t=floor(M/2)/M. In lexicographic row order 00,01,10,11 the means are

    J/M: (1-p)^2, p(1-p), p(1-p), p^2;
    C/M: p(1-p)^2, p^2(1-p), p(1-p)^2, p^2(1-p);
    D/M: t(1-p)^2, tp(1-p), tp(1-p), tp^2.

Each summand has this law even where adjacent pairs/triples overlap, including the final triple ending at X_(M+1). Linearity of expectation needs no independence between summands. D has floor(M/2) terms, with denominator M, not floor(M/2), M+1, or the number of input symbols. For M>=64, t>=1/3.

On I=[1/8,1/4], the J derivative magnitudes are at least 3/2,1/2,1/2,1/4. The two C derivatives are (1-p)(1-3p)>=3/16 and p(2-3p)>=13/64. D multiplies J derivatives by t. Thus EVERY coordinate is strictly monotone with derivative magnitude at least d=1/12 throughout I. There are no constant coordinates in this M domain; the duplicated coordinates cause no difficulty.

## 3. A common rounding cell containing two separated means

Rounding thresholds are T_Q={(j+1/2)/Q: j=0,...,Q-1}. Each of twelve monotone mean functions has at most Q roots of f(p) in T_Q on I. Retain distinct roots in the interior of I; with the two endpoints they partition I into at most 12Q+1 open intervals. One interval (a,b) has length

    L=b-a >= (1/8)/(12Q+1) >=1/(104Q).

Choose p_0=a+L/3 and p_1=a+2L/3, so Delta=p_1-p_0=L/3>=1/(312Q), and Delta<=1/24. Both mean vectors round to one common bank b*. More strongly, for each coordinate f and each j=0,1,

    dist(f(p_j),T_Q) >= d L/3 >=1/(3744Q)=:rho.           (2)

To check this even for the first/last interval: no threshold lies strictly between f(a) and f(b). A threshold below or above that value interval is separated from f(p_j) by at least its distance to the corresponding endpoint value, which the derivative lower bound makes >=dL/3. Thresholds outside f(I) obey the same reasoning; no extension of the derivative bound outside I is used. Ties at a or b are irrelevant because p_j is interior. The argument is valid for h=0, including the single threshold 1/2.

## 4. Concentration of actual counts, not rounding of expectations

For any one normalized coordinate F, changing one raw input bit changes its count by at most three: at most three departure triples contain that bit; pair and half-pair coordinates in fact need at most two. There are N=M+2 independent input bits. Thus the sum of squared bounded-difference constants is at most

    (M+2)(3/M)^2 <=10/M,  M>=64.

The bounded-difference inequality gives

    Pr_p(|F-E_p F|>=rho) <=2 exp(-M rho^2/5).

A union bound over twelve coordinates and (2) gives, separately at p_0,p_1,

    Pr_p(B != b*) <= epsilon :=24 exp[-M/(5*3744^2 Q^2)].  (3)

This controls the random bank itself. It never replaces E round(F) by round(E F). Shared bits and coordinate dependence do not need to be independent. Define C=500000000. If M>=CQ^2 then epsilon<=1/16. One fully elementary verification: C>30*3744^2, and e^6>384 (its nonnegative Taylor terms through degree 10 already exceed 384), so 24e^{-C/(5*3744^2)}<24/384.

## 5. Keeping the protected endpoint without falsely declaring independence

Let P_j be the joint law of (B,E), E=(X_M,X_(M+1)), at p_j. Couple it to Q_j=(b*,E) using the SAME endpoint E. Equation (3) yields TV(P_j,Q_j)<=epsilon, irrespective of bank-endpoint dependence. Under IID, the endpoint marginal is Bernoulli(p_j) tensor Bernoulli(p_j). A coordinatewise uniform coupling gives TV(Q_0,Q_1)<=2Delta. Consequently

    TV(P_0,P_1)<=2epsilon+2Delta<=1/8+1/12=5/24<1/2.     (4)

One must not claim B is independent of E: the final departures explicitly use the endpoint. The coupling is what makes this step valid.

For a decoder let A be its probability of symbol 1. In the IID submodel the target probability is p at every actual endpoint, so the loss is exactly |A-p|. To see the two-point inequality for randomized decoders, append the same independent seed law to both observations; their TV does not increase. Integrate |A-p_0|+|A-p_1|>=Delta against the common subprobability measure of mass 1-TV(P_0,P_1). Hence

    max_j E_j|A-p_j| >= (Delta/2)(1-TV(P_0,P_1))
                    >=Delta/4 >=1/(1248Q)              (5)

when M>=CQ^2. Any public source-independent randomization can be included in that seed. Source-dependent advice or a seed correlated with hidden history is not allowed.

## 6. Self-contained full-history IID floor and the other regime

This subsection avoids needing a separate admission for an IID lower. It applies even to a decoder that sees the entire N=M+2 bits. Take p_0=1/8 and p_1=p_0+delta, delta=1/(16 sqrt N), both in I. The elementary Bernoulli relative-entropy bound is

    KL(Ber(p_0)||Ber(p_1)) <=delta^2/[p_1(1-p_1)]
                            <=(64/7)delta^2.

The first inequality follows from log x<=x-1; the second from p_1 in I. Product KL is at most 1/28. Pinsker gives full-history TV<=sqrt(1/56)<1/4. Data processing and the preceding two-point argument imply

    R*(M,h)>=3delta/8=3/(128 sqrt(M+2))>=1/(64 sqrt M).    (6)

The last inequality is equivalent to 9M>=4(M+2), true for M>=64. The IID table theta_u(1)=p has stationary pair law Pi=Ber(p)^tensor2 and P^2(u,v)=Pi(v) at EVERY initial pair u; thus the subclass meets C_M, including the all-state condition.

If M<CQ^2, (6) implies R*>1/(64 sqrt C Q)>=1/(1600000Q), using sqrt C<25000. If M>=CQ^2, (5) implies the same weaker constant. Combine this all-regime precision lower with (6) to obtain the lower half of (1). The two lower experiments need not use the same parameter pair: each lower holds for every decoder and therefore for the same minimax risk.

## 7. Matching upper and exact scope of the precision conclusion

Accepted ACG001 equation (6), with k=0 and xi=0, applies to the same nearest-rounded bank and exact endpoint. Its sequential clipping and rational gate are legal arbitrary decoders, giving

    R*<=min{1,131072/sqrt M+536088/Q}
       <=min{1,667160 max{M^(-1/2),1/Q}}.

Thus for any fixed risk factor K, achieving R*<=K/sqrt M requires Q>=sqrt M/(1600000K), or h>=0.5 log2 M-log2(1600000K). Conversely ACG001 gives sufficiency for h>=ceil(0.5 log2 M); a finite suffix adds its separately controlled 2^-r error. The lower is fractional precision necessity for these twelve direct normalized rails. Accumulation precision, addresses, input storage, score precision, parameters, masks and other program resources are NOT lower bounded here.

No all-encoder bit-count lower follows: arbitrary encoders could spend their bits on a different parameter summary, and arbitrary architectures could expose different information. Adding hidden history or other counts invalidates the observation premise. The constants are intentionally loose, and the crossover C is only a proof device, not a practical sample-size recommendation.

## 8. Diagnostics and source status

`check.py` uses only exact rational/integer arithmetic. It enumerates short binary words to verify expectation formulas and per-bit sensitivity, checks rational derivative minima, isolates threshold roots by exact sign bisection and verifies certified interior pairs for selected M,h, and checks the numerical inequalities used above with rational Taylor sums. It also exhibits that expectation and rounding do not commute. These finite checks diagnose the proof and indexing; they do not replace the all-M argument, concentration inequality, or two-point theorem.

`SOURCE_BINDINGS.json` pins the exact ACG001 acceptance and statement, and the FPA001 candidate/program identifying the cut. This candidate has no independent review or root acceptance at author delivery. No publication, commit, network transmission, or changes to other units were performed.
