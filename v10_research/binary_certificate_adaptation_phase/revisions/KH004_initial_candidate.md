# KH004 — Larger boundary-window obstruction via constant crossing (candidate)

2026-11-02. New author candidate; fresh full independent review and root acceptance required. KH003's frozen smaller-window result remains a valid separate baseline, not an error or a proof dependency here. No accepted proof is modified.

Observation is **the eight exact triple counts plus the actual first and last r symbols**. The result is not for full histories, all interior length-r pattern counts or arbitrary radius-r local encoders.

## 1. Finite statement

Use the binary protected-terminal-pair experiment, N=M+2 and integer M>=64. The predictor knows M, supplied beta and integer width r>=2, but not actual budget k. It may randomize and has no computational restriction. Loss is unconditional TV at the true protected terminal pair. Attacks are source-independent offline stochastic maps with a pointwise Hamming budget on the first M symbols.

Put c=2^-12, beta in[1/M,1/16], T=floor1/(8beta). Assume integers k,r satisfy

    k<=T, k>=64/c,
    k^3>=2^22 M^2, k^2>=2^23 M,
    r>=2, r<=k/4,
    r c k/M<=1/16, 16r/(c k)<=1/16,
    J0=max{k,ceil(16 c r k)}<=T.                    (1.1)

For j=J0,...,T define a stationary clean source Q_j by

    x=ck/M, y=j/M, w=1-y-2x,
    a=ck/(2j), b=1/2, e=1/2, tau=x/(2w),
    Pi=(y,x,x,w), theta(1)=(a,1/2,1/2,1-tau).

These sources satisfy the SAME supplied all-state certificate P²>=beta Pi. Let S be the same predictor map's supremum clean risk over this family. There is an explicit stationary null and one common legal kernel such that

    R_null >=[(ck/(128M)-2S)log((T+1)/J0)]_+.       (KH4)

Also H_2(M,k,beta)<=2k/M. Consequently, at beta_M=1/M, no such unknown-k predictor attains the known-k profile uniformly over all budgets on ANY prescribed width sequence

    r_M>=2, r_M=o(M^(1/3)).                         (1.2)

The impossibility already uses stationary sources. It is not a sharp-threshold claim at M^(1/3).

## 2. Source legality, stationarity and all sixteen certificate positions

We have k<=j<=T<=M/8, so 0<x<=c/8, 0<y<=1/8, w>=3/4, 0<a<=c/2<1/4 and 0<tau<=1/4. The balances ya=xe and w tau=xb, together with equal crossing masses, prove stationarity and full support.

In state order00,01,10,11 the squared kernel is exactly

    [(1-a)^2, (1-a)a, a/2,          a/2]
    [1/4,     1/4,     tau/2,       (1-tau)/2]
    [(1-a)/2, a/2,     1/4,         1/4]
    [tau/2,   tau/2,   (1-tau)tau,  (1-tau)^2].

Compare every column with beta(y,x,x,w):

1. Positions(00,11) and(11,00) require a/2>=beta w and tau/2>=beta y. Both reduce to ck>=4 beta j w, which holds since beta j<=1/8, w<=1 and ck>=64.
2. Positions(01,10) and(11,01) have tau/2=x/(4w)>=beta x, since beta<=1/16 and w<=1.
3. Positions(00,10) and(10,01) have a/2=xM/(4j)>=2x>=beta x. Position(00,01) has (1-a)a>=3x>=beta x.
4. Position(11,10) has (1-tau)tau>=3x/(8w)>=3x/8>=beta x.
5. Positions(01,01) and(10,10) have1/4>=beta x.
6. Positions(01,11) and(10,11) have(1-tau)/2>=3/8 and1/4, respectively, each>=beta w.
7. Positions(00,00),(01,00),(10,00),(11,11) have entries at least9/16,1/4,3/8,9/16, respectively, while each target is<=1/16.

These are2+2+3+1+2+2+4=16 distinct positions. The certificate is all-state, not a support-only assertion. Also a>=4ck beta>=2beta, a target separation used later.

## 3. Asymmetric null and exact full-word weights

Use the same first-order asymmetric null as KH001:1->0 rate q=1/(2M),0->1 rate beta, initialized at its own stationary law pi1=beta/(beta+q). Its pair law is Pi_*(u,v)=pi(u)T_*(u,v), and

    P_*²((u,v),(s,t))/Pi_*(s,t)=T_*(v,s)/pi(s)
                                      >=beta+q>=beta.

Both off-diagonal ratios equal beta+q; the diagonal ones are at least that because beta+q<=1. Since beta>=2q, pi1>=2/3.

For each j use the disjoint null word x^(j)=1^(N-j)0^j. Its full probability, including the long prefix, is

    v_j=pi1(1-q)^(M+1-j) q(1-beta)^(j-1).

Bernoulli's inequality gives(1-q)^M>=1/2 and(1-beta)^(j-1)>=7/8, so

    1/(8M)<=v_j<=1/(2M).                           (3.1)

The true null target at00 is beta, not q. No constant-v_j assumption is made.

## 4. Faster explicit mixing and corrected reversed concentration

The four paths00->00->01->11,01->11->11->11,10->00->01->11,11->11->11->11 have probabilities(1-a)a/2,(1-tau)^2/2,a/4,(1-tau)^3. Each is at least a/4, so in particular

    P_j³(u,11)>=lambda=ck/(16j).

A common atom yields TV contraction alpha_h=(1-lambda)^floor(h/3). Covariance summation for a stationary copy W gives

    Var J_D(W)<=7M Pi(D)/lambda

for any state subset D and exactly M departure indices.

The exact stationary binary-order2 reversal identity R P* R=P, with R swapping01/10, follows from ya=xe and w tau=xb (accepted KH001). Therefore the original event F={Y0=11,YM=00} has probability y P_00(Y_M=11), and its reversed conditional law is the same chain started00 conditioned on E={Z_M=11}.

The reciprocal Bernoulli bound gives alpha_M<=1/(1+lambda M/4)<=8/(ck)<=1/8, since j<=M/8 and k>=64/c. Thus P_00(E)>=w-1/8>=1/2 and

    P_Qj(F)>=j/(2M).                               (4.1)

Couple reverse-start Z to stationary W at three-step blocks using the common atom, filling each block by its correct conditional bridge. After the first common-atom success use identical transitions. The marginals retain the original path laws. Its meeting-boundary time sigma has E sigma<=3/lambda; extending beyond M if needed makes it always defined. For every D, |J_D(Z)-J_D(W)|<=sigma, without independence assumptions.

The stationary means are E J00(W)=j and E Jcross(W)=2ck. Markov/Chebyshev with thresholds k/32,k/8,k/32 give

    P(sigma>k/32)<=1536j/(c k²),
    P(|J00(W)-j|>k/8)<=7168j²/(c k³),
    P(Jcross(W)>k/32)<=917504j/k².

For the last bound use2ck<=k/64 and deviation k/64. Condition on E, costing at most2. With j<=M/8 the total failure is at most

    917504 M²/k³+1802240 M/k²
       <=7/32+55/256=111/256.                      (4.2)

When reversing back, departures shift from original indices0,...,M-1 to1,...,M; J00(reverse)=J00(original)+1 and Jcross is unchanged. The same thresholds and k>=32 therefore give a good original-count event G with

    P(G^c|E)<=111/256,
    |J00-j|<=k/4, Jcross<=k/16 on G.               (4.3)

The+1 is included: k/8+k/32+1<=3k/16<k/4.

## 5. Genuine boundary windows: the late bound uses mixing, not r b

Let the reversed bits start00 and let B mean first-r0 and last-r1. The original corresponding event is first-r1/last-r0. Before conditioning E, first-r0 failure costs at most(r-2)a; after conditioning it costs at most2ra<=1/16, since j>=16crk gives a<=1/(32r).

For the late boundary, on E a failure of last-r1 has a last zero at some index between N-r+1 and N-2; it forces an011 transition at one of exactly r-2 departure indices m>=M+2-r. At each such index m>=M-r>=M/2, and floor(m/3)>=M/8 because M>=64 and r<=k/4<=M/32. Uniform mixing from00 gives

    P_00(Y_m=01)<=x+alpha_m,
    alpha_m<=1/(1+lambda M/8)<=16/(ck).

The last inequality uses j<=M/8. The conditional probability of the next1 given01 is b=1/2. Thus the UNCONDITIONAL probability of late-window failure AND E is at most (r/2)[x+16/(ck)]. Divide only afterward by P(E)>=1/2:

    P(late-window failure|E)
       <=rck/M+16r/(ck)<=1/8.

This does not assert stationarity of the reverse-start or conditioned chain, and does not use the useless crude r*b bound. Adding the first-window cost gives

    P(B^c|E)<=3/16<=1/4.                            (5.1)

Hence P(G intersect B|E)>=81/256>1/4 and P(B|E)>=3/4. Conditional on E and B, G still has probability at least81/256, since division by P(B|E)<=1 can only increase it.

For the original stationary event F_r=first-r1/last-r0, (4.1) and(5.1) imply

    P_Qj(F_r)>=3j/(8M),
    E[|A(T_r(X))(1)-a| | F_r]<=8SM/(3j)<=4SM/j.     (5.2)

The genuine windows and original rare event are both charged.

## 6. Canonicalization, strict kernel and statistic identity

Use accepted KH001 canonicalization: remove all000/111 self-loops from the pair path, prepend111 loops at initial11, retain the other edges in order, and append000 loops at terminal00. It preserves the complete triple histogram, pair endpoints and length, and

    d_H(Can(X),x^(j))<=3Jcross+|J00-j|

for the fixed pre-sampling j. On G this is<=7k/16<k.

A word in F_r already contains at least r-2 of each diagonal self-loop, so its canonicalization also has first-r1/last-r0. One can also verify on G that N000>=j-5k/16>=11k/16>=r-2 and N111>=M-j-3k/8>=53M/64>=r-2. Retain an explicit output-window check anyway.

The kernel is identity except on x^(j), J0<=j<=T. On such an input it samples an actual stationary Q_j word conditional on F_r, canonicalizes once, and accepts only if the output's Hamming distance to that actual input is<=k AND its first/last-r windows equal those of the input. Rejection is identity; there is no repeated sampling. On G both checks pass, so acceptance is at least1/4.

This is one fixed map per public(M,beta,k,r), common across source laws. Its auxiliary probabilities are specified in advance and may be hardcoded; it has no hidden true-law, unseen-clean-data or predictor-seed input. Real probabilities are permitted by the unrestricted finite-kernel model. Every output has the protected final pair and passes the strict distance test. The null input's windows fit because j>=k>=4r and N-j>=7M/8+2>=r.

For EVERY accepted sample, T_r(Can(X))=T_r(X). This is the exact observation restriction used in the proof; interior longer-pattern counts need not match.

## 7. Finite loss bound and benchmark

On accepted samples the clean target is a and null target beta, with a-beta>=a/2. Acceptance is at least1/4. Subtract at most the entire conditional clean error from(5.2) and discard nonnegative rejection loss:

    E[null loss | x^(j)]>=a/8-4SM/j.

Average independent predictor randomness throughout. Apply the two null-weight bounds(3.1) separately to positive and penalty parts. Since a=ck/(2j),

    R_null >=sum_(j=J0)^T[ck/(128Mj)-2S/j]
            =(ck/(128M)-2S)sum_(j=J0)^T 1/j.

Use nonnegativity when the coefficient is negative and the harmonic integral otherwise. This proves(KH4). No possibly negative bracket is multiplied by an incorrectly directed mass bound.

For the comparison beta>=1/M and k>=2sqrt(M) yield

    F_2<=k/M+1/[M sqrt(beta)]<=k/M+M^-1/2<=2k/M,
    H_2<=2k/M.

The k>=2sqrt(M) condition follows from(1.1). Known-k SC003 uses only counts/final pair, so the same known-k benchmark is available for this richer statistic.

## 8. Growing-window consequence and honest comparison

At beta=1/M assume(1.2), and set U=M/r, L=M^(2/3), k=floor(sqrt(U L)). Since U/L=M^(1/3)/r->infinity, k/L->infinity and k/U->0. In particular

    k³/M²->infinity, k²/M->infinity, k/sqrt(M)->infinity,
    r/k->0, rk/M->0, k/M->0.

The r/k limit follows from r=o(M^(1/3)) and k>>M^(2/3). All fixed thresholds in(1.1) hold eventually, including k>=64/c, the two boundary probabilities and r<=k/4. Moreover J0<=k+16crk+1 implies J0/M->0, while T/M->1/8. Thus log((T+1)/J0)->infinity.

An all-budget profile guarantee with finite constant C has S<=C/sqrt(M) from actual k=0. In(KH4),2S is negligible relative to ck/(128M). Eventually the risk is at least ck/(256M) times the divergent logarithm, whereas H_2<=2k/M. Their ratio diverges. Predictor and constant may depend on the full prescribed width sequence; the contradiction defeats every fixed constant. Stationary witnesses suffice.

KH003's b=delta construction remains valid and gives r=o(M^(1/6)) at beta=1/M. Here constant b=e=1/2 gives an atom of order k/j rather than k/(j sqrt(M)), so the variance-driven budget requirement improves from k>>M^(5/6) to k>>M^(2/3). A separate near-terminal mixing calculation replaces its small-b boundary estimate. These are genuinely different source families and proof steps. The old result is not retroactively rewritten.

Neither exponent is claimed sharp for the observation problem. This theorem does not cover r comparable to M^(1/3), full-word observation, all length-r pattern counts, arbitrary local-radius encoders, or any neural/training architecture without an independently proved exact representation reduction.

## 9. Provenance and review requirements

KH001 supplies canonicalization, general binary reversal and the accepted model interfaces; the new family, all-state certificate, concentration constants and late-window mixing estimate are proved above rather than imported from KH003. SC003/BT002 supply the benchmark. The actual KH004_constant_crossing_exploration_unreviewed.md is preserved as history, not a proof premise.

Fresh full independent review and exact diagnostics must audit every new probability/constant/interface and the asymptotic width selection. No external novelty, external peer review, formal verification, efficient/causal attack, revealed edit mask or seed, editable target, publication or neural/training claim is made.
