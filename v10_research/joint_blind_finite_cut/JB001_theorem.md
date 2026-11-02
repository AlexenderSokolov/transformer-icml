# JB001 — Budget-blind decoding of a binary noisy histogram cut

2 November 2026. Root-authored candidate; independent full review and acceptance required. This note does not change JP001 or AB003.

## Experiment and claim

Use exactly JP001's fixed, paid binary uniform-histogram prefix and information cut: M>=64, Q=2^h>=16, working D=2^P with P>=h, eight triple coordinates, only the protected terminal pair and public source-independent metadata in addition to the eight labels. The source has the all-state two-step certificate beta. Initialization can be stationary or arbitrary. At most k of the first M observed symbols are replaced, and the actual finite bank then receives a one-shot vector perturbation bounded coordinatewise by delta, with 0<=delta<=1/4, followed by clipping and Q-flooring. The target is the clean original actual-terminal next-law. No mask, seed, count or history bypass is allowed.

Let

    s=M^(-1/2), e=max(sqrt(beta),1/M),
    f_e(x)=x[1+ln(1+1/(M e x))] for x>0, f_e(0)=0,
    tau=k/M+delta+1/Q.

There is ONE deterministic finite-rational decoder depending on M and the received labels and terminal pair, but NOT on k, delta, beta, or any numerical budget certificate, such that, whenever tau<=s,

    risk <= min{1, 2^20 s + 2^22 f_e(tau)}.          (JB1)

The same decoder works simultaneously for all such triples (k,delta,beta), all allowed cooperating attacks, and both initialization conventions. The fixed encoder already depends on none of these budgets. Consequently this restricted operating region admits simultaneous budget-blind attainment of JP001's known-budget fixed-prefix minimax order min(1,max(s,f_e(tau))). This is not an all-budget adaptation theorem, a redesigned-encoder lower bound, or a claim that working precision and output precision equal h. The decoder is defined outside tau<=s too, but no sharp risk guarantee there is asserted.

## Decoder

Let z be the eight nonnegative received grid labels. At the protected terminal pair u, form rational pseudo-counts tilde C=M z_(u,d(u)) and tilde J=M sum_c z_(u,c), where d(u) is the complement of the first bit of u. Compute the integer threshold

    B=12 ceil(sqrt(M))

by exact integer square-root and comparison. Return designated probability tilde C/tilde J if tilde C>B; otherwise return zero. Return its complement in the other coordinate. An active branch has tilde J>=tilde C>B>0. Thus this is a legal rational simplex vector even if the complete pseudo-histogram does not sum to M. No soft subtraction or estimated contamination budget is used.

## Pathwise count error

The actual pre-port bank is a_i=floor(D C'_i/M)/D, with C' the corrupted-word counts. JP001 proves this exact identity by cancellation of the common positive finite Taylor weight, not an approximation argument. For any port attack, clipping around the true frequency C'_i/M and the two floors give

    |z_i-C'_i/M| <= delta+1/D+1/Q <= delta+2/Q.

Source replacement changes the complete triple histogram by l1 at most 6k. Therefore the selected two-coordinate pseudo-row and clean row satisfy

    ||tilde C_row-C_row||_1 <= d,
    d=6k+2M(delta+2/Q) <=6M tau.                    (1)

In particular |tilde C-C|<=d and |tilde J-J|<=d. Endpoint protection is what makes these the same row. The number d is an analysis variable, not an input. Under tau<=s, d<=6sqrt(M)<=B/2.

## Hard-threshold lemma for real nonnegative pseudo-counts

Write q for the true designated probability and E=1{J>0}|C/J-q|. The AB003 deterministic argument extends unchanged to real pseudo-counts; here is a complete verification of that extension.

If tilde C<=B then C<=B+d<=3B/2. For q>0 and J>3B/q this implies q<=2E. Otherwise the threshold term q 1{J<=3B/q} pays the loss. At J=0 it also pays q; when q=0 define the term to be zero.

If tilde C>B, then C>B-d>=B/2>=d, so J>=1. Put p=C/J and p'=tilde C/tilde J. Inserting tilde C/J gives

    |p'-p| <= (|tilde C-C|+p'|tilde J-J|)/J <=2d/J.

Also p'<=4p: for J>=2d use tilde C<=C+d<2C and tilde J>=J-d>=J/2; for J<2d use p>d/J>1/2 and p'<=1. At d=0 the claim is immediate. Thus

    |p'-q| <= E+min(4p,2d/J)
             <=5E+min(4q,2d/J)
             <=5E+4min(q,6d/(J+2)),

using the 4-Lipschitz truncation and J+2<=3J. In both branches,

    |qhat-q| <=5E+4min(q,6d/(J+2))
                  +q 1{J<=3B/q}.                   (2)

This is pointwise. It does not require independence of the pseudo-count errors, integer pseudo-counts, an actual word realizing those pseudo-counts, or knowledge of d by the decoder.

## Expectation and constants

Use AB003's explicitly proved fixed-state threshold calculation and its clean comparator:

    E[E] <=8193 sqrt(32)/sqrt(M+1),
    E[q_(Y_M) 1{J_(Y_M)<=3B/q_(Y_M)}] <=2600/sqrt(M).

The second calculation sums separately over the four fixed states, using integer thresholds floor(3B/q_u)+1 and zero contribution when q_u=0. It does not insert a random threshold into an unconditional occupation inequality.

To avoid any lower endpoint restriction on the inherited continuous occupation interface, enlarge 6d to A=6d+2>=2. JP001's binary weighted occupation completion, based on BIF001, BAI003 v2 and the universal weak-beta bound, gives for every real A>=2 and every initial law

    E min(q_(Y_M),A/(J+2)) <=4s+16672 f_e(A/M).

Monotonicity, subadditivity and concave scaling of f_e, together with (1), imply

    f_e(A/M) <=36 f_e(tau)+f_e(2/M)
              <=36 f_e(tau)+8s.

The final inequality follows from e>=1/M and ln(1+M/2)<=sqrt(2M), as explicitly established in JP001. Taking expectations in (2) now yields

    risk <= [5*8193sqrt(32)+2600+16+32*16672]s
                +144*16672 f_e(tau).

The statistical coefficient is less than 2^20; the other equals 2,400,768<2^22. Unit TV supplies the cap, proving (JB1).

## Lower comparison, costs and limitations

For each fixed k,delta,beta in this operating region, JP001's known-budget lower permits any decoder supplied those public budgets, so it also applies to the more restricted budget-blind decoder family. It uses the same fixed eight-coordinate prefix and terminal-pair side port. Hence the order comparison is valid, but no lower for redesigned deep encoders follows. No rho certificate is needed by this particular decoder; JP001's certificate was a requirement of its different constructive budget-aware upper, not a new source of parameter information in its lower.

Retain JP001's complete paid prefix, finite evaluator, all-token masks, dense zero slots, full-width accumulators and access-cut isolation. Only the post-cut decoder changes. Counts M z have O(h+log(M+2)) full rational description lengths, because Q is dyadic and known from the label format. Compute ceil(sqrt(M)) by squared-integer binary search, compare the threshold by integer cross-products, and serialize the probability with an explicit positive denominator. A conservative terminal decoding cost is O(v^3) bit operations and O(v^2) scratch for v=O(h+log(M+2)); all-token decoding adds the factor M+3 and separately paid code/held storage if the batch syntax requires it. Add these costs to the inherited prefix and the simultaneous handoff buffers. No free history reread, exact-real operation, noise generator or physical isolation device is claimed. The output is a finite rational probability, not automatically on the internal Q grid.

There is no inference that large joint budgets can be adapted to blindly. AB001 and AB003 already show an order boundary for a full-history source-edit budget range when both k and beta are unknown. This note transfers the constructive hard-threshold mechanism to the fixed finite noisy cut only in the explicitly restricted tau<=s region. Supplied-beta all-budget adaptation and sharp unknown-noise adaptation outside this region remain open here. Finite diagnostics and an independent LLM review, when completed, do not constitute formal verification, external peer review or novelty certification.
