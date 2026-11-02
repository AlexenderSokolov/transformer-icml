# BAI001 — Arbitrary binary initialization: audited partial progress

2026-11-02. Research note only; neither an upper theorem nor a counterexample. No accepted files changed.

## Target
Extend BU001's stationary square-root-beta precision upper to arbitrary initial pair laws, with unchanged SB001 decoder and actual-terminal TV. This note records two tempting but invalid routes, and a valid structural lemma.

## 1. Full-support lemma
Write pair states 00,01,10,11, stationary masses y,x,x,w and row parameters a=theta00(1), b=theta01(1), e=theta10(0), t=theta11(0). If beta>0 and x>0, the all-state two-step certificate implies

    ea=P²(10,01)>=beta x>0,
    bt=P²(01,10)>=beta x>0.

Therefore a,e,b,t>0. Stationarity ya=xe and wt=xb forces y,w>0. Thus the nontrivial binary class has full stationary support, and BU001's ordinary-hitting-time bounds apply to every possible initial state, not merely stationary starts.

If x=0, positive beta forces stationary support to consist of exactly one absorbing diagonal. These degenerate classes require a separate argument; the full-support constraints cannot simply be passed to their boundary at unchanged beta.

## 2. Failed transient-waiting counterexample
A tempting candidate starts at00, uses a=1/(2M), e=0, t=1/2, and b=p in[1/4,3/4]. The active chain on01,10,11 then has stationary law (x,x,2px), x=1/(2+2p), while00 is transient. Its initial long wait followed by an active suffix would reproduce BI001's no-cutoff logarithm.

However this source is NOT in D2(beta) for ANY beta>0:

    P²(10,01)=ea=0 < beta x.

Thus it cannot establish initialization separation. Checking only transitions from00 misses exactly this all-state certificate obstruction. Adding e>0 changes stationary masses and reinstates the product constraint; the claimed separation must not be reused.

## 3. What a split-path argument actually proves
For a full-support source, BU001 gives H_s<=5/(sqrt(beta) p_s q_s), with q00=a,q11=t,q01=q10=1. Its hitting/return moment argument extends to arbitrary initial states: initial hitting has an exponential moment bounded by a universal constant, and successive returns have the same stationary-return law regardless of initialization. Consequently, for an absolute c>0, the number N of visits to a fixed state in an initial interval of length proportional to M obeys

    P_mu(N<j)<=C exp(-c sqrt(beta) M p_s q_s)

whenever j<=c M p_s (integer endpoint adjustments absorbed).

Split at a deterministic midpoint. The event {Y_M=s,J<j} implies low fixed-s prefix occupation AND low actual-terminal suffix occupation. Conditional on the midpoint, the latter has probability at most C j/M by the accepted universal terminal-occupation lemma, uniformly over its initial law. The Markov property therefore multiplies the bounds:

    P_mu(Y_M=s,J<j)
      <= C (j/M) exp(-c sqrt(beta) M p_s q_s),
      j<=c M p_s.

This is a useful high-layer bound. It does NOT finish the desired integration.

## 4. Exact remaining gap
For V=min(q_s,A/(J+k)), the preceding bound applies only to layers u>=C A/(M p_s). Lower layers cannot be bounded by C A/M using stationary cancellation: arbitrary initial terminal mass need not be O(p_s). Applying only universal occupation there gives potentially

    (A/M) log(1/p_s),

which has no uniform control by the desired log(1+1/(sqrt(beta) A)). Starting in a very low-stationary-mass sticky state illustrates why terminal-mass domination is false. Its actual count is typically large, so this is an analysis gap, not a counterexample to the target upper.

A successful proof needs state-dependent transient control that uses small row-prediction error during long diagonal/alternating waits, or a direct regenerative argument that controls the initial waiting segment jointly with later visits. Full initial TV mixing at square-root-beta is not available. No claim that the global spectral gap is square-root-beta is made.

## Sources and scope
BU001 weighted stationary return upper, BI001 v2 binary rare-suffix lower, and AU001 exact residual suffix mixture were read directly. AU001's residual mixture has decay beta, not sqrt(beta), so it cannot be substituted without new analysis. This note is a transparent obstruction record, not an independent review or acceptance receipt.

## 5. Additional structural leads, not established bounds

For singleton stationary support00, a=0 and the all-state certificate requires

    e(1-b)>=beta, e>=beta, te>=beta.

Thus a sticky transient11 (small t) forces rapid escape from the alternating01/10 region (large e). Conversely a long-lived random active region with small e forces t and1-b to be large. This product tradeoff is consistent with, but does not prove, a square-root-beta arbitrary-start cutoff. The symbol-swapped statement holds for singleton11.

A potentially useful scalar interpolation is: for t>=1,z>=1 and fixed c>0,

    min{(1+ln z)/z, exp(-c t)}
      <= C_c [1+ln(1+z/t)]/z.

Indeed when z>=t², ln(z/t)>=one-half ln z; when z<t², z exp(-ct)<=t² exp(-ct) is bounded. Therefore a suitable exponentially small *precision-dependent late-regeneration residual*, combined with the universal precision bound, could suffice. Marginal weighted TV by itself is inadequate: a complete suffix law or actual-terminal weighted error on late-coupling paths must be controlled. No such pathwise/regenerative estimate has been proved here.

## 6. Valid counterexample to weighted marginal square-root mixing (NOT precision upper)

The root suggested checking a=e³,b=t=1/2. That positive-a family does NOT have beta of order e: x=e²/(1+3e²), and the exceptional cell has ratio

    P²(10,01)/pi01=ea/x=e²(1+3e²).

So it cannot refute square-root-beta mixing at M~1/e. But its EXACT boundary a=0 gives a valid and informative obstruction.

Take 0<e<=1/4, a=0, b=t=1/2, stationary pi=delta00, arbitrary initialization01, and beta=e/2. The only nonzero stationary target is00. The four corresponding P² entries are

    1, e/2, e, e/2,

so the complete all-state D2(beta) certificate holds. All other right-hand sides are zero. This is a genuine binary second-order homogeneous source.

Compare its active paths on01,10,11 with the BI001 reference kernel at p=1/2 (where10 always returns01). Every reference path of length M has actual-source density (1-e)^N10 >=(1-e)^M until absorption. For M>=3, reference endpoint01 has probability at least1/8 by the reference three-step minorization. The true minority probability on row01 is1/2. Consequently

    E[ min(theta_YM(0),theta_YM(1)) 1{Y_M!=00} ]
      >= (1/16)(1-e)^M.

With M=floor(1/e), this is bounded below by a positive absolute constant. In contrast

    1/M + exp(-c M sqrt(beta)) -> 0

for every fixed c>0 as e decreases to zero. Thus even prediction-minority-weighted marginal convergence to stationarity need NOT occur at square-root-beta, in the complete arbitrary-start class.

This does not refute the desired precision upper: the long-lived active trajectory has been observed from its beginning, so its relevant row counts are typically of order M rather than a newly entered rare suffix. A valid upper must distinguish an active initial prefix from a late exit out of a waiting region; marginal coupling alone discards precisely this distinction.
