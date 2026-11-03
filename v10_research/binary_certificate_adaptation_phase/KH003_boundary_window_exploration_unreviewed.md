# KH003 exploration — histogram plus growing boundary windows (UNREVIEWED)

2026-11-02. Actual successor reasoning, not an accepted theorem. KH001/KH002 bytes remain unchanged. This addresses the exact gap root warned about: canonicalization alone does NOT preserve the original boundary windows. The proposed repair conditions original clean comparison words on those windows and pays their probability.

## Candidate finite extension

Let r>=2 be an integer window width. Use KH001 finite parameters and additionally

    r<=k/4, r delta<=1/16,
    J0=max{k,ceil(16 c r k)}<=T.

For each j=J0,...,T, use exactly its Q_j, asymmetric null and fixed null word x^(j). In the reversed chain Z started00, condition on E={Z_M=11}, with P(E)>=1/2. Let B mean its first r symbols are0 and its last r symbols are1; in original orientation this means the clean word's first r are1 and last r are0.

Before conditioning E:
- failure of first-r zeros costs at most(r-2)a_j, since until the first exit the pair remains00;
- on E, failure of last-r ones implies at least one01->11 transition in the last r-2 departure steps. The union bound is at most(r-2)delta, regardless of previous states.

Thus P(B^c|E)<=2r(a_j+delta)<=1/4, because j>=16 c r k gives a_j<=1/(16r), and r delta<=1/16. This charges the ORIGINAL clean windows, not merely canonical output windows.

KH001's good-count event G has P(G^c|E)<=111/256. Therefore

    P(G intersect B|E)>=145/256-1/4=81/256>1/4,
    P(B|E)>=3/4,
    P(G|E,B)>=81/256>1/4.

The original stationary event F_r (first-r1, last-r0) has probability

    P(F_r)>=[j/(2M)](3/4)=3j/(8M),

so its conditional clean error is <=8SM/(3j)<=4SM/j. The rare-event cost is retained.

On G, original |J00-j|<=k/4 and Jcross<=k/16. Write L0=N000, L1=N111. As U=N001<=Jcross and E_skeleton<=2Jcross,

    L0=J00-U >=j-5k/16>=11k/16>=r-2,
    L1=M-L0-E_skeleton >=M-j-3k/8>=53M/64>=r-2.

Hence canonicalization has first-r1 and last-r0 on G. Its Hamming distance to the fixed input is <=7k/16<k.

Crucial kernel refinement: sample a genuine Q_j word conditional on F_r, canonicalize once, and accept ONLY IF both the actual distance<=k AND the output first/last-r windows equal the input windows. Otherwise output input. On G both tests pass, hence acceptance>=1/4. Checking windows also ensures every accepted sample, not just G, has the identical augmented predictor statistic before/after canonicalization.

Null target stays beta and a_j>=2beta. Triangle inequality therefore yields

    E loss given x^(j)>=a_j/8-4SM/j.

With the same nonconstant null-weight bounds, separately bounding positive/error parts gives

    R_null >=[(c k/(128M)-2S)
                 log((T+1)/J0)]_+.

Known H_2<=2k/M remains. This finite argument needs full independent review, especially the final-window transition union and all indices.

## Candidate growing-window consequence at beta=1/M

If r_M>=2 and r_M=o(M^(1/6)), put U=M/r_M, L=M^(5/6), and k=floor(sqrt(U L)). Then U/L->infinity, k/L->infinity, kr_M/M->0, r_M/k->0, r_M/sqrt(M)->0. Thus all KH001 finite conditions and the additional window conditions eventually hold. T/J0->infinity and k/sqrt(M)->infinity. A clean O(M^-1/2) guarantee would therefore force an unbounded logarithmic excess over H_2.

This would rule out histogram plus first/last-r symbols even for growing r=o(M^(1/6)), at the critical beta=1/M. It would NOT prove full-history nonadaptivity, arbitrary local-summary impossibility, or a neural architecture lower without a separately proved representation interface.

## More general candidate window condition

For supplied beta>=1/M, let U=1/(r beta), L=max{sqrt(M),beta^(-5/6)}. If

    r beta sqrt(M)->0, r beta^(1/6)->0,

then L/U->0. Taking k=floor(sqrt(U L)) again gives the required conditions and T/J0->infinity. The critical specialization above follows. Nested actual-beta extension could use beta_w=max(beta,1/M) and add beta^(-1/2) to L, but this is not needed for the first candidate.

No accepted claim is made here. No diagnosis of boundary preservation is bypassed, and no public artifact was changed.
