# RESC binary local-confidence lemma — companded signed reconstruction plus source edits

2026-11-02. New author lemma for the successor robust-encoded-source-corruption theorem. Not independently reviewed, formally verified, or root accepted. No frozen source is modified. This lemma proves the binary extension, including the weighted true-exit occupation interface; it does not import a unit-cap estimate into the square-root-beta bound.

## 1. Result and inputs

Take the final-pair-protected source-edit experiment of SC003/BT002, with K=2, M>=64, k in {0,...,M}, and the all-pair-state certificate P_source^2(i,j)>=beta Pi(j). Initialization may be arbitrary or stationary. Let the preserved terminal pair select a row. Its CLEAN normalized successor frequencies are x=(x_0,x_1), mass r=J/M. Its CORRUPTED frequencies are x'=(x'_0,x'_1). A decoder only sees recovered nonnegative rational frequencies y=(y_0,y_1), each in [0,1], and the exact preserved terminal pair; x,x',r,J are analysis variables, never input ports.

Assume a supplied finite rational epsilon>=0 certifies, for each coordinate,

    |y_i-x'_i| <= 4 epsilon sqrt(x'_i)+4 epsilon^2+2 epsilon/chi,       (1)

where chi>=1 is public rational (dyadic in the compander construction). This is exactly MG001's symmetric inverse estimate, with its epsilon optionally enlarged to a rational upper certificate. It remains valid for arbitrary correlated signed reconstruction errors. Source editing gives

    ||x'-x||_1 <= 6 k/M.                                            (2)

Put

    tau=k/M+epsilon^2+epsilon/chi,
    e=max(sqrt(beta),1/M),
    f_e(t)=t[1+ln(1+1/(M e t))], t>0; f_e(0)=0,
    s=M^(-1/2).

There is a beta-blind, public-budget-aware finite rational decoder, specified below, with

    risk <= min{1, 2^18 s + 2^10 epsilon + 2^24 f_e(tau)}.            (3)

It uses no clean word, source parameter, true minority/exit test, edit locations, or seed. Formula (3) is valid at k=0 and epsilon=0 without a special statistical-estimator branch. Its constants are intentionally loose.

## 2. Clean-to-recovered row bound

Let eta=k/M, d=||y-x||_1, and rhat=y_0+y_1. By (1), (2), Cauchy-Schwarz, and r'<=r+6eta,

    d <=6eta+4epsilon sqrt(2r')+8epsilon^2+4epsilon/chi
      <=4sqrt(2) epsilon sqrt(r)+8sqrt(3) epsilon sqrt(eta)
         +6eta+8epsilon^2+4epsilon/chi.

The inequality 8sqrt(3) epsilon sqrt(eta)<=8epsilon^2+6eta follows from
(2sqrt(2)epsilon-sqrt(6) sqrt(eta))^2>=0. Consequently

    d <=6epsilon sqrt(r)+16tau.                                    (4)

Also |rhat-r|<=d. Neither d nor r is computed by the decoder.

## 3. A radius using decoded data only

For epsilon>0 obtain a rational upper square root S satisfying

    sqrt(rhat)<=S<=sqrt(rhat)+epsilon.                              (5)

A fully finite method is given in section 6. If epsilon=0 set S=0; every occurrence of S is multiplied by epsilon. Define the nonnegative rational radius

    Bhat=12epsilon S+68tau.                                        (6)

Then, on every realization,

    d<=Bhat<=18epsilon sqrt(r)+132tau.                             (7)

For the lower inequality at epsilon>0, use r<=rhat+d and (4):

    d<=6epsilon sqrt(rhat)+6epsilon sqrt(d)+16tau
      <=6epsilon sqrt(rhat)+d/2+18epsilon^2+16tau,

so d<=12epsilon sqrt(rhat)+36epsilon^2+32tau<=Bhat. For the upper inequality, (5), sqrt(rhat)<=sqrt(r)+sqrt(d), and
12epsilon sqrt(d)<=d+36epsilon^2 give

    Bhat<=12epsilon sqrt(r)+d+48epsilon^2+68tau
         <=18epsilon sqrt(r)+132tau.

At epsilon=0, (4) gives d<=16tau<=68tau=Bhat<=132tau, proving both inequalities without using (5). These bounds are deterministic and do not require y to have total mass one across the global bank.

## 4. Binary lower-envelope decoder and correct pathwise split

Use SC003's PUBLIC orientation: the designated successor is the complement of the terminal pair's first bit. Thus the true designated probabilities on rows 00,01,10,11 are q=(a,b,e_exit,t_exit). These are proof variables only; the program uses just the pair symbols.

Let y_exit be the corresponding recovered coordinate. Set B=M Bhat, tilde C=M y_exit, tilde J=M rhat, and output designated probability

    qhat=(tilde C-B)_+/(tilde J+B+2),                               (8)

with other probability 1-qhat. The numerator is nonnegative and at most tilde J; the denominator is strictly positive. All quantities are rational and obtained from the allowed cut and public M,k,epsilon,chi.

Let C be the clean designated count and J the clean row count. By (7), the complete selected-row l1 count discrepancy is at most B. Thus

    n=(tilde C-B)_+ <= C,
    0<=C-n<=2B,
    D=J+2 <=D'=tilde J+B+2 <=D+2B.

Therefore qhat<=C/(J+2), and

    0<=C/(J+2)-qhat<=4B/(J+2).

For J>0, put p=C/J. Then

    0<=p-qhat<=min(p,(4B+2)/(J+2)).

The function p->min(p,z) is 1-Lipschitz, for every fixed realized z. Taking z=(4B+2)/(J+2) yields

    |qhat-q|<=2|p-q|+min(q,(4B+2)/(J+2)).                           (9)

No independence is used even though B is random and data-dependent. At J=0, C=0 and qhat=0. Since 4B+2>=2, the last minimum in (9) equals q, so (9) holds with empirical term zero.

Use (7) and min(q,u+v)<=u+min(q,v), u,v>=0, to obtain the key bound

    |qhat-q| <=2 1{J>0}|p-q|
                +72epsilon sqrt(M)/sqrt(J+2)
                +min(q,A/(J+2)),
    A=528 M tau+2.                                                (10)

Indeed 4M Bhat<=72epsilon M sqrt(r)+528M tau, and
M sqrt(r)/(J+2)=sqrt(MJ)/(J+2)<=sqrt(M)/sqrt(J+2).

Crucially, the term placed inside the weighted true-q occupation functional is ONLY the deterministic additive floor A. The square-root-mass term is handled by universal square-root occupation. Replacing q by a unit cap in the final term would forfeit the binary square-root-beta cutoff; this proof does not do so.

## 5. Expected risk, including every beta/support case

SC003 section 3, using the ORIGINAL clean add-one comparator, gives

    E[1{J>0}|p-q|] <=8193 sqrt(32)/sqrt(M+1).                       (11)

For the four-state pair chain at every initialization,
P(J<w)<=min(1,16w/(M+1)) at integer w>=1. MG001's layer-cake argument therefore gives

    E[(J+2)^(-1/2)]<=8/sqrt(M+1).                                 (12)

The accepted continuous-budget completion in JP001 section 2 gives, for EVERY real A>=2,

    E min(q,A/(J+2)) <=4s+16672 f_e(A/M).                           (13)

Its q is exactly the fixed orientation in (8), not the unit crossing cap. For clarity: BIF001 section 3.4 proves (13) on full stationary support with beta>=M^-2; its first-diagonal-hit argument covers arbitrary starts. For positive-beta singleton support, BAI003 v2 gives <=256A/M+16/(M+2)<=264A/M, and symbol exchange preserves this orientation. For beta<M^-2, the universal bound Psi(16A/(M+1))<=16f_(1/M)(A/M) applies. These cases exhaust beta in [0,1], including unsupported initial states and beta=0. No support test is performed by the decoder.

The scalar function f_e is increasing, concave, and subadditive, with f_e(cz)<=c f_e(z) for c>=1. Hence

    f_e(A/M)<=528 f_e(tau)+f_e(2/M)<=528 f_e(tau)+8s.                (14)

The last bound follows from e>=1/M and ln(1+M/2)<=sqrt(2M), as recorded and proved in JP001. Equations (10)-(14) imply the sharper explicit intermediate estimate

    risk <=[2*8193sqrt(32)+4+8*16672]s
               +576epsilon+(528*16672)f_e(tau),

whose three coefficients are respectively below 2^18,2^10,2^24. Capping by unit TV proves (3). The result is uniform over attacks because all reductions before expectation are pathwise.

## 6. Finite rational upper square root and extra cost

No real square-root oracle is a decoder input. For epsilon>0 choose the least integer p>=0 with 2^-p<=epsilon, using exact comparisons to the supplied rational epsilon. Write rhat=u/v, u>=0,v>0, with finite integer numerator and denominator. Let j be the least nonnegative integer satisfying

    j^2 v >=2^(2p)u,

and set S=j/2^p. Integer square root or binary search with full exact products computes j. Minimality gives (5), with error strictly below 2^-p except at an exact grid point. Zero rhat gives j=0. The case epsilon=0 bypasses this operation and uses S=0.

If b covers full numerator/denominator lengths of y, supplied epsilon, chi, M,k and all guards, then p=O(b), and S, tau, Bhat and the final common-denominator output use O(b) bits up to fixed constants. Binary search needs O(b) exact squared-integer comparisons, so a conservative extra online budget per decoded token is O(b^3) Boolean bitwork, O(b^2) temporary data, and O(b^4) finite microcode/control if independently compiled. Charge all tokens if the chosen syntax decodes every token: O(n b^3+b^4) work and O(n b+b^2+b^4) extra retained/code bits, plus actual buffers during handoff. The complete main theorem must add these costs to, not replace, the paid MG encoder/snake/compander decoder ledger. Public certificates require their FULL binary descriptions, not unit-cost real constants.

This operation is reliable post-cut exact arithmetic. It does not claim that square roots are performed by a fixed-depth bounded primitive neural layer; any PURE expansion separately pays its actual Boolean depth/width. Only labels, protected terminal pair and public budgets are read after the cut.

## 7. Consequence and limits

At epsilon=O(s), chi>=bitlength(M+1), subadditivity and the universal e>=1/M bound give
f_e(epsilon^2+epsilon/chi)=O(s). Thus (3) becomes

    risk=O(s+f_e(k/M)),

with fixed constants at any fixed epsilon/s budget. BT002's accepted source-corruption lower, including its separate scalar completion, gives the matching statistical/source floor for BOTH initialization experiments. This says that the selected robust deep construction reaches the full-corrupted-word source-edit profile at that operating point. It does NOT prove a global optimized-encoder minimax frontier in arbitrary Q, depth, width or fault radius, nor a sharp packing exponent.

The clipping clarification MG_final_clip_clarification.md remains mandatory for whatever finite encoder supplies (1): the actual bank is exactly clipped to [0,1] BEFORE the fault, with those extra stages counted before choosing global finite precision. This local decoder does not repair an unproved upstream finite-evaluation certificate.
