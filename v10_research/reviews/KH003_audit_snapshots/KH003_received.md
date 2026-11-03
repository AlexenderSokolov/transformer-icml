# KH003 — Histogram adaptation with genuine boundary windows (candidate)

2026-11-02. New author candidate; fresh full independent review and root acceptance required. Accepted KH001 and all earlier proof bytes are unchanged. KH002 is a separate dependency for the domain-classification synthesis and its exact acceptance status must be bound.

The predictor sees the eight exact triple counts and the actual first r and last r symbols. This is NOT the full history and does NOT include counts of all length-r patterns throughout the interior. No arbitrary radius-r encoder or neural architecture consequence is inferred.

## 1. Finite theorem

Use the protected-terminal-pair binary experiment with N=M+2, M>=64. Let r>=2 be an integer window width, known to the predictor. Its statistic T_r is the complete triple histogram plus the first and last r bits. The predictor may know beta and randomize but not know actual k. Its loss is unconditional TV at the true terminal pair; corruptions obey the source-independent strict Hamming model.

Put c=2^-12, beta in[1/M,1/16], delta=sqrt(beta), T=floor1/(8beta). Assume integer k satisfies accepted KH001's full finite domain

    32<=k<=T, k^2>=4M, k delta>=6/c,
    delta^5 k^3>=2^20, delta^3 k^2>=2^21,

and also

    r<=k/4, r delta<=1/16,
    J0=max{k,ceil(16 c r k)}<=T.                    (1.1)

For j=J0,...,T use KH001's exact stationary clean source Q_j:

    x=ck/M, y=j/M, w=1-y-2x,
    a_j=ck(1-delta)/j, b=delta, e=1-delta,
    tau=x delta/w, Pi=(y,x,x,w).

These have the same supplied all-state certificate beta. Let S be the same predictor map's supremum clean risk over this family. There is one common legal kernel and the same asymmetric stationary null as KH001 such that

    R_null >=[(ck/(128M)-2S)log((T+1)/J0)]_+.       (KH3)

The known-k benchmark satisfies H_2(M,k,beta)<=2k/M. All witnesses are stationary. The finite source family may depend on k; the predictor map is identical in its clean and attacked guarantees.

## 2. Accepted ingredients and notation

KH001 proves, for each j in this range:

- The all-state certificate, stationarity, legal probabilities and a_j>=2beta.
- The asymmetric null with1->0 rate1/(2M),0->1 rate beta. For x^(j)=1^(N-j)0^j, its complete word mass lies in[1/(8M),1/(2M)] and its true terminal00 target is beta.
- Under stationary Q_j, F={Y0=11,YM=00} has probability at least j/(2M).
- Reversing a stationary binary order2 word retains its law. Conditional on F, the reversed chain is the same P_j started00 and conditioned on E={Z_M=11}, with P_00(E)>=1/2.
- Under that reverse bridge, the corresponding original word has a good-count event G with

      P(G^c|E)<=111/256,
      |J00-j|<=k/4, Jcross<=k/16 on G.              (2.1)

  The +1 reverse-departure correction was already paid in this bound.
- Canonicalization preserves the triple counts, pair endpoints and length, and for the fixed pre-sampling j,

      d_H(Can(X),x^(j))<=3Jcross+|J00-j|.           (2.2)

These facts concern the genuine original clean word. No assertion about longer original boundary windows is inherited automatically.

## 3. Charge both ORIGINAL clean boundary windows

Write the reversed symbols as z_1,...,z_N, with z_1z_2=00 and terminal event E={z_(N-1)z_N=11}. Let B be the event that its first r symbols are all0 and last r symbols all1. In the original orientation, this means first-r1 and last-r0.

The first-r-zero event fails only if the pair00 exits during its first r-2 departures. Until its first exit each such conditional probability is a_j, so

    P_00(first-r zeros fail)<=1-(1-a_j)^(r-2)
                              <=(r-2)a_j.          (3.1)

For the other boundary, restrict to E. If the last r bits are not all1, choose their LAST zero at index q. Since the last two bits are11, q is between N-r+1 and N-2. The triple at q,q+1,q+2 is011, so a01->11 transition occurred. There are exactly r-2 possible departure positions q-1, each having unconditional probability at most delta. Thus

    P_00(E AND last-r ones fail)<=(r-2)delta.       (3.2)

For r=2 both failure events are empty. Divide their union bound by P_00(E)>=1/2. Since j>=16crk implies a_j<=1/(16r), and r delta<=1/16,

    P_00(B^c|E)<=2r(a_j+delta)<=1/4.               (3.3)

No stationary distribution at the reversed start or endpoint-conditioned IID law is used. The late-window estimate is an unconditional transition union bound on E, not an assumption about the state just before that window.

Combining (2.1) and (3.3),

    P_00(G intersect B|E)>=1-111/256-1/4
                           =81/256>1/4,
    P_00(B|E)>=3/4,
    P_00(G|E,B)>=81/256>1/4.                       (3.4)

The last inequality uses P(B|E)<=1, not an unjustified lower bound on that denominator.

Let F_r be the ORIGINAL stationary event first-r1/last-r0. It is F intersect the reversal of B. Therefore

    P_Qj(F_r)>= [j/(2M)](3/4)=3j/(8M),
    E[|A(T_r(X))(1)-a_j| | F_r]
                              <=8SM/(3j)<=4SM/j.  (3.5)

Thus the rare event and the genuine boundary conditioning are both charged.

## 4. Canonical output windows and a mandatory acceptance test

Write L0=N000, L1=N111, U0=N001 and E_sk=M-L0-L1. Accepted endpoint-flow identities give U0<=Jcross, E_sk<=2Jcross, and L0=J00-U0. On G,

    L0>=j-5k/16>=11k/16>=r-2,
    L1=M-L0-E_sk>=M-j-3k/8>=53M/64>=r-2.          (4.1)

The second line uses j,k<=M/8; r<=k/4 makes its last inequality valid. Canonicalization prepends all L1 loops at initial11 and appends all L0 loops at final00. Hence on G it has first-r1 and last-r0. Also (2.2) gives distance<=7k/16<k. In fact F_r alone already forces L0,L1>=r-2: its constant boundary windows contain these self-loops. Thus these particular output windows are automatically preserved under this canonicalization. We nevertheless retain an explicit output-window check in the kernel below; it is safe and makes the accepted-statistic interface directly testable.

Define the kernel, fixed per public(M,beta,k,r), to be identity except on x^(j), J0<=j<=T. On such an input:
1. sample an actual stationary Q_j word conditional on F_r;
2. canonicalize once;
3. output it ONLY if its Hamming distance to the actual input is<=k AND its first/last-r windows equal those of that input;
4. otherwise output the unchanged input.

There is no resampling until success. These are public auxiliary laws, not hidden true-source parameters. They can be hardcoded into one finite stochastic map, common to all sources; arbitrary real probabilities are allowed. The kernel has no unseen-clean-data or predictor-seed input.

Both tests pass on G, so acceptance probability conditional on F_r is at least1/4 by (3.4). Every output respects the strict budget and protected final pair. The null input itself has first-r1/last-r0: j>=k>=4r and N-j>=7M/8+2>=r.

Most importantly, EVERY accepted output, not only those on G, has

    T_r(Can(X))=T_r(X),

because X was conditioned on its genuine windows and the defined kernel explicitly checks them on output. Alternatively, the constant-window loop observation above proves this equality. Canonicalization without the genuine original-window condition would not justify equality for this augmented statistic.

## 5. Loss and nonconstant null masses

On accepted samples the clean target is a_j, the null target is beta, and a_j-beta>=a_j/2. Acceptance mass is at least1/4. Subtracting no more than the entire conditional clean error in (3.5) yields

    E[null loss | x^(j)]>=a_j/8-4SM/j.              (5.1)

Rejecting outcomes only adds nonnegative loss. Independent predictor randomness is averaged in the same nonnegative loss function.

The null word masses v_j need not be equal. Bound the positive and penalty parts separately, using1/(8M)<=v_j<=1/(2M) and a_j>=ck/(2j):

    R_null >= sum_(j=J0)^T [ck/(128Mj)-2S/j]
            =(ck/(128M)-2S) sum_(j=J0)^T 1/j.

If the coefficient is negative use risk nonnegativity; otherwise use the harmonic integral. This proves (KH3), without multiplying a possibly negative bracket by the lower null-mass bound. KH001's comparison H_2<=2k/M remains unchanged.

## 6. Growing windows on the critical curve

Let beta_M=1/M and integer r_M>=2 satisfy

    r_M=o(M^(1/6)).                                (6.1)

Take U=M/r_M, L=M^(5/6), and k=floor(sqrt(U L)). Then U/L=M^(1/6)/r_M->infinity, so k/L->infinity and k/U->0. In particular

    k/sqrt(M)->infinity, k^3/M^(5/2)->infinity,
    k^2/M^(3/2)->infinity, k/sqrt(M)->infinity,
    r_M/k->0, r_M/sqrt(M)->0, k r_M/M->0.

The r_M/k limit follows from r_M=o(M^(1/6)) and k>>M^(5/6). These imply all finite conditions eventually. Also J0<=k+16cr_M k+1, so J0/M->0, while T/M->1/8. Thus

    log((T+1)/J0)->infinity.                        (6.2)

If one budget-blind predictor attained H_2 with any finite constant C on this prescribed width sequence, its clean risk S<=C/sqrt(M). This is negligible relative to ck/(128M), even after multiplying S by2. Eventually (KH3) gives at least ck/(256M) times (6.2), while H_2<=2k/M. The risk-to-benchmark ratio diverges.

Thus histogram plus first/last-r_M symbols is nonadaptive at beta=1/M for every width sequence (6.1), already stationary. This does NOT claim a sharp window-length boundary: r of order M^(1/6) or larger is not resolved by this proof. The harmonic requirement is M/(r_M k)->infinity, not merely M/k->infinity.

## 7. Bounded-window domain synthesis

Assume KH002's exact accepted public-domain criterion and notation G(M,beta). Let a public domain consist of triples(M,beta,r), integer2<=r<=r0 for some fixed finite r0, and2r<=M+2. A one-constant histogram-plus-boundary-window family exists for every budget if and only if G is bounded on this domain.

Sufficiency is ordinary add-one from KA001/KH002; extra windows can be ignored. For necessity, an unbounded-G sequence has M^2 beta->infinity and beta sqrt(M)->0. Use KH002's exact witness beta_w=max(beta,1/M) and

    U=1/beta_w,
    L=max{sqrt(M),beta_w^(-5/6),beta^(-1/2)},
    k=floor(sqrt(U L)).

Its proof gives all KH001 finite conditions at beta_w, k sqrt(beta)->infinity and k/U->0, k/L->infinity. Bounded r gives r<=k/4, r sqrt(beta_w)<=1/16 eventually and J0/k bounded, hence T/J0->infinity. Apply the finite window theorem to the SAME actual-beta map by class nesting. Exactly as in KH002, the null target remains beta_w, while supplied metadata and benchmark are actual beta. The actual-beta H_2<=2k/M; the clean O(M^-1/2) penalty vanishes relative to k/M. The divergent harmonic factor contradicts adaptation.

This synthesis needs accepted KH002, not just its candidate statement. It yields a bounded-boundary-width domain criterion, not an arbitrary growing-width phase diagram.

## 8. Deliberate exclusions and provenance

The observation retains only triple counts and two genuine boundary windows. It does not preserve all length-r pattern counts, sliding-window embeddings, arbitrary local feature summaries or the full ordered word. No conclusion about an encoder follows without a separately proved reduction to this exact statistic.

The earlier KH003_boundary_window_exploration_unreviewed.md records the actual exploratory derivation. Original-window conditioning, its probability cost and the reversed transition indices must be justified. The explicit output-window test is retained in this attack, although it is redundant for these constant conditioned windows as explained in §4; no minimality claim about the test is made.

Independent full review and exact diagnostics must separately audit these additions, all inherited source bindings, randomization, finite-k legality and the growing-window/domain limits. No external novelty, external peer review, formal verification, efficient or causal attack, revealed edit mask, edited target, neural/training consequence or publication claim is made.
