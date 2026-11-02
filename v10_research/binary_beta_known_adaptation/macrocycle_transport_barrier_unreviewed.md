# Supplied-beta adaptation — macrocycle ordering and Hamming geometry

2026-11-02. **UNREVIEWED contributor research.** This is not an independent review, accepted theorem, or a full adaptive-estimator result. Accepted AB001–AB003 are unchanged.

## Result first

There is an exact clean macrocycle inequality connecting ordering to Hamming distance from a one-flip trajectory. It quantitatively explains why a same-beta histogram canonicalization need not extend to a full-history erasure.

For designated binary exits (a,b,e,tau), let

    h=b+e-be, alpha=a*b/h, delta=tau*e/h,
    sigma=alpha+delta-alpha*delta.

The 00 and 11 occupation counts in successive complete 00->11->00 macrocycles are independent geometric variables U_i~Geom(alpha), V_i~Geom(delta); all pairs are independent. Therefore W_i=min(U_i,V_i) are IID Geom(sigma). For any observed path completing n cycles,

    distance_H(word, {1^l 0^(N-l):0<=l<=N})
         >=sum_(i=1)^n W_i.                          (MC1)

Consequently, uniformly over every initial pair law and every observation horizon,

    P(complete at least n cycles AND distance_H<=k)
        <=P(Binomial(k,sigma)>=n).                   (MC2)

If k*sigma<=n/2, the last probability is at most

    exp[-(log 2-1/2)n].                              (MC3)

The theorem is about the entire ordering, not a terminal histogram. It does not supply k to an estimator; k is the radius in the analytical statement.

For the same-beta stationary family described in §4 below, this implies an exponentially small clean probability of lying within k edits of **any** one-flip word whenever both diagonal occupation scales are much larger than k. Thus a canonicalization-based histogram lower must solve a genuinely different full-history transport problem to become a full-history lower.

## 1. Definitions and geometric macro-occupation laws

Use the pair chain Y_j=(X_(j+1),X_(j+2)), j=0,...,M, with departures j=0,...,M-1. Assume a,b,e,tau>0 and h>0; if a diagonal cannot be reached, the event of completing n>=1 corresponding cycles is empty and can be separated instead.

Let S_0 be the first hit of 00. Define S_1 as the next hit of 11, S_2 the next hit of 00, and continue alternating. The i-th complete cycle is [S_(2i-2),S_(2i)). Its 00 and 11 departure occupation counts are

    U_i=sum_(j=S_(2i-2))^(S_(2i-1)-1) 1{Y_j=00},
    V_i=sum_(j=S_(2i-1))^(S_(2i)-1) 1{Y_j=11}.

In particular U_i,V_i>=1. The endpoints beginning the next leg are excluded from the preceding leg, so different cycles use disjoint departure indices.

Starting at 01, the probability of hitting 11 before 00 is

    p=b+(1-b)(1-e)p=b/h.

Starting at 10, the probability of hitting 00 before 11 is e/h. Therefore at each visit to 00, the probability that the ensuing excursion hits 11 before returning to 00 is alpha=a*b/h. The analogous success probability at 11 is delta=tau*e/h.

Strong Markov at the returns to each diagonal gives

    U_i~Geom(alpha), V_i~Geom(delta)

on {1,2,...}. Strong Markov at the opposite-diagonal hits makes U_i independent of V_i, and makes successive pairs independent. The initial hitting time S_0 and arbitrary initial law do not affect these post-hit laws.

The source may be continued beyond the observed horizon to define the infinite sequence. No assertion of independence after conditioning on the number of completed observed cycles is made. For every fixed n, the unconditional first n pairs have the stated laws, and an event requiring completion by M is a subset of the event used below.

Since min of independent geometric variables is geometric,

    P(W_i>=m)=[(1-alpha)(1-delta)]^(m-1)
              =(1-sigma)^(m-1).

## 2. Deterministic Hamming lower

Map each departure index j with Y_j=00 to the single observed symbol X_(j+2)=0, and each index with Y_j=11 to X_(j+2)=1. These positions are distinct for distinct departure indices and belong to the observed word when a cycle completes by M.

Within cycle i, all U_i selected zeros occur before all V_i selected ones. Consider any monotone comparison word 1^l0^(N-l). If its cut is before the first selected one, all V_i selected ones are on its zero side and are mismatches. If the cut is at or after the first selected one, all U_i selected zeros lie on its one side and are mismatches. Hence the cycle contributes at least min(U_i,V_i) mismatches.

The selected positions of different cycles are disjoint. Summing proves (MC1) simultaneously for every cut, so no union bound over possible one-flip locations is needed. Arbitrary off-diagonal symbols can only add mismatches and were ignored.

This bound permits edits anywhere; it remains a necessary condition for the stricter protected-endpoint corruption model.

## 3. Probability bound without conditioning away the horizon

If at least n cycles complete by M and the word is within k edits of a monotone one-flip word, then sum_(i=1)^n W_i<=k. By the geometric waiting-time/binomial identity,

    P(sum_(i=1)^n W_i<=k)=P(Binomial(k,sigma)>=n).

This is zero when k<n. It remains valid with arbitrary initial law: apply the fixed-state strong Markov law after S_0 and discard the additional restriction that all n cycles finish by the observed horizon. No random threshold n is substituted into an unconditional law.

For B~Binomial(k,sigma), exponential Markov at base two gives

    P(B>=n)<=2^-n E 2^B
              =2^-n(1+sigma)^k
              <=exp(-n log2+k sigma).

Thus k sigma<=n/2 implies (MC3). More generally one may sum these fixed-n bounds to obtain a time-uniform tail over n>=n0; no such optional-stopping conclusion is assumed without that sum or a separate martingale argument.

## 4. Same-beta family: a full-history neighborhood is exponentially small

The following specialization matches the scale proposed for a same-beta histogram-only obstruction. It is recorded independently as an ordering barrier, not as a review or acceptance of that obstruction.

Take M>=64 with sqrt(M) an integer, a fixed 0<c<=1, integer k>=1, and integer j. Set

    b=1/sqrt(M), e=1-b,
    x=c*k/M, y=j/M, w=1-y-2x,
    a=x*e/y=c*k*e/j,
    tau=x*b/w=c*k*b/(M-j-2c*k),
    h=b+e-be, nu=c*k*b*e/h.

Assume

    j>=800k,  M-j-2c*k>=800k,  nu>=200.              (4.1)

Then all parameters are legal, Pi=(y,x,x,w) is stationary, and the source satisfies the all-state certificate with beta=1/M. Moreover, for **every initial pair law**,

    P_Q(distance_H(word,{1^l0^(N-l)})<=k)
       <=exp(-nu/64)
          +exp[-(log2-1/2)nu/200]
       <=2 exp(-nu/1600).                            (MC4)

Here nu is order c*k/sqrt(M). Conditions (4.1) can hold asymptotically, for example with k growing faster than sqrt(M) but slower than M and j, M-j both sufficiently larger than k. Constants are deliberately conservative; no claim of a useful finite onset is made.

### 4.1 Legality, stationarity and all-state certificate

The range gives a<=1/800 and tau<=b/800, while b<=1/8, e>=7/8, and y,x,w>0. Stationarity is exactly ya=xe and w*tau=xb.

The pair two-step matrix, in order 00,01,10,11, is

    [(1-a)^2, (1-a)a, a(1-b), ab],
    [(1-b)e, (1-b)(1-e), b*tau, b(1-tau)],
    [e(1-a), ea, (1-e)(1-b), (1-e)b],
    [tau*e, tau(1-e), (1-tau)tau, (1-tau)^2].

Since 1-b=e and 1-e=b, the crossing ratios include b^2/w and e^2/y, both at least b^2. Ratios involving e*b/x are also at least b^2 because x<1/2 and e>=7/8. The remaining diagonal self-loop ratios are at least 9/16, the ratios involving e(1-a)/y are at least (7/8)(3/4), and the remaining ratios b(1-tau)/w are at least (3/4)b>=b^2. The two potentially small opposite-diagonal ratios are equal:

    ab/w = tau*e/y = b^2 * [nu*h/(y*w)] >= b^2,

because nu>=200, h>=7/8 and y*w<=1/4. These checks cover all sixteen entries and prove beta=b^2=1/M on all starting states.

### 4.2 Enough complete cycles before M

The macro hazards simplify exactly to

    alpha=nu/j, delta=nu/(M-j-2c*k).

From any current state, the chance to hit 11 within three transitions is at least a*b*e=alpha*h*e>=alpha/2. To hit 00 within three transitions it is at least tau*e=delta*h>=delta/2; if already at the target, the hitting time is zero. In both cases this is at least

    p=nu/(2M),

since both denominators in alpha,delta are at most M. The first hit of 00 and every subsequent alternating diagonal leg therefore have hitting times stochastically dominated by 3Geom(p). Strong Markov permits the successive dominating variables to be taken independent; equivalently, their conditional tail bounds can be composed.

Let n=floor(nu/100). To complete n cycles it suffices to finish the initial 00 hit and 2n alternating legs. Thus

    P(fewer than n cycles by M)
       <=P(Binomial(floor(M/3),p)<2n+1).

The binomial mean is at least nu/8 (M>=64), while 2n+1<=nu/40 when nu>=200. The usual elementary lower-tail Chernoff bound at half the mean consequently gives

    P(fewer than n cycles by M)<=exp(-nu/64).         (4.2)

The initial-law freedom is fully included in the first hitting leg.

### 4.3 Cost per complete cycle

Since sigma<=alpha+delta,

    k sigma<=nu*k[1/j+1/(M-j-2c*k)]<=nu/400.

Also n=floor(nu/100)>=nu/200, so k sigma<=n/2. Apply (MC2)-(MC3) with this fixed n and add (4.2). This yields the first bound in (MC4). The last follows from log2-1/2>1/8. No conditioning on the realized n or on a clean terminal event is inserted into the geometric law.

## 5. What this does and does not provide constructively

A possible full-history estimator would need to use the observed distribution of complete macrocycle occupancies, not merely fitted row parameters or the triple histogram. Artificial short excursions in both long diagonal traps can cheaply make the histogram resemble a same-beta source, but genuine homogeneous macrocycles require repeated substantial zero and one occupancies in alternating order. The quantities min(U_i,V_i), or an appropriate likelihood/e-process for their geometric law under candidate parameters, expose this distinction.

However, these notes do not construct a globally rate-optimal estimator. In particular:

- The true alpha,delta are not available to an estimator and would require joint candidate fitting or confidence control.
- The exact geometric law is for fixed complete-cycle indices, not the sequence conditioned on its observed terminal horizon.
- A fixed high-confidence rejection threshold could introduce extra logarithms; the desired expected-risk scale requires sharper weighting rather than an unsupported union bound.
- Proximity to a one-flip word is only one attack family. A general adversary may start from many genuine clean macrocycles.
- A strict kernel mapping a one-flip input into a canonical histogram arrangement can be legal while its output distribution is far from the entire clean path law. (MC4) rules out simply replacing that arrangement by a typical clean word at the same cost in this family, not every conceivable full-history lower.

The supplied-beta full-history all-budget adaptation problem therefore remains open. These macrocycle statements require fresh independent review before being treated as accepted results.
