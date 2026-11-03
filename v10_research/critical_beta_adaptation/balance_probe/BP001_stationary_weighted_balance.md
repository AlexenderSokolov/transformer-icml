# BP001 — Stationary binary weighted half-occupation balance

2026-11-02. **New proof candidate; independent review pending.** This proves the stationary clean-bias ingredient for an order-sensitive occupation-balance gate. It does NOT prove the arbitrary-initialization analogue or an adaptive estimator by itself.

## 1. Statement

Use the binary homogeneous second-order model of SC003. The pair chain Y_j=(X_(j+1),X_(j+2)), j=0,...,M, is initialized at a qualifying stationary law Pi, and satisfies the ALL-STATE certificate P^2(i,j)>=beta Pi(j), beta>0. Put

    n=floor(M/2), m=M-n,
    J1_u=sum_(j=0)^(n-1)1{Y_j=u},
    J2_u=sum_(j=n)^(M-1)1{Y_j=u}, J_u=J1_u+J2_u.

Write a=theta00(1), b=theta01(1), e=theta10(0), tau=theta11(0), and the designated probabilities q=(a,b,e,tau). For M>=64 and every fixed0<c<=1/256,

 E_Pi[q_(Y_M) 1{J1_(Y_M)<c J_(Y_M)}]
       <=min{1,4096/(M sqrt(beta))}.                 (BP1)

The event is false when J=0, because its definition is the strict inequality0<0. The stronger bound with weights gamma=(a,1,1,tau) is also proved. Thus at beta>=c_beta/M, with fixed c_beta>0, the clean cost of zeroing this weighted terminal prediction on imbalance is O_(c_beta)(M^-1/2).

The original source, terminal query and unconditional loss are preserved. Only the proof conditions on the stationary terminal state and reverses the path. No row observations are asserted IID after terminal conditioning. Arbitrary starts remain outside(BP1).

## 2. Generic finite-state return-time concentration

Let a finite irreducible Markov chain have stationary target mass p>0. Let H be the largest ordinary mean hitting time of that target over all states, with zero hitting time at the target. Let

    Hbar=max(H,1/p).

All starts in this lemma are arbitrary. Let D be the first ordinary target hit and T a positive return time from the target. Kac gives E T=1/p; E D<=H<=Hbar. The family of ordinary hitting laws and the positive-return law is closed under conditioning on survival and the current state. Consequently, for every member V of that family and integer r>=1,

    E V^r <=r! Hbar^(r-1) E V.                       (2.1)

For completeness, the deterministic inequality V^r<=r sum_(j=0)^(V-1)(V-j)^(r-1), conditional expectation on survival, and induction prove(2.1). The zero ordinary hitting time at the target is harmless.

Take lambda=1/(4Hbar). Expansion in nonnegative powers and(2.1) give

    E exp(lambda D)<=4/3,
    E exp(lambda T)<=exp(2lambda/p).                (2.2)

Also e^(-x)<=1-x+x^2/2 and E T^2<=2Hbar/p imply

    E exp(-lambda T)
       <=1-lambda/p+lambda^2 Hbar/p
       <=exp(-3lambda/(4p)).                       (2.3)

For any integer l>=1 let L_l count target visits at times0,...,l-1. Using fresh IID positive returns AFTER the first hit, not any terminal-conditioned sample, we obtain the uniform-start bounds

    P(L_l<lp/16)<=2exp[-l/(8Hbar)],
    P(L_l>4lp+1)<=exp[-l/(2Hbar)].                  (2.4)

Here are the exact count indices. For the lower tail take K=ceil(lp/16). Fewer than K observed visits means the K-th visit occurs at D+T_1+...+T_(K-1)>=l. By(2.2), its probability is at most

    (4/3)exp[-lambda l+2lambda(K-1)/p]
       <=(4/3)exp[-7lambda l/8]
       <=2exp[-l/(8Hbar)].

This is also valid when lp<16, since K=1 uses no return variables. For the upper tail take K=floor(4lp)+1>4lp. The event L_l>4lp+1 supplies at least K+1 visits and implies T_1+...+T_K<=l, because D>=0. By(2.3), its probability is at most

    exp[lambda l-3lambda K/(4p)]
       <=exp[-2lambda l]=exp[-l/(2Hbar)].

The strong Markov property makes these post-hit returns IID before any horizon restriction. No claim of independence after conditioning on L_l is made. Bounds(2.4) apply to a deterministic window starting at any time, by conditioning on its initial state and averaging.

## 3. Binary certificate supplies the needed weighted hitting scale

Assume full stationary support and write Pi=(y,x,x,w). Use gamma=(a,1,1,tau), not the designated crossing weights b,e. Accepted BU001 v2, section1, proves for each target s

    sqrt(beta) Pi(s) gamma_s H_s<=5,                (3.1)

where H_s is its maximum ordinary hitting mean. Its proof uses the actual full-state certificate, stationarity ya=xe and w tau=xb, and the necessary b^2>=beta w and e^2>=beta y. For example, for s=00 it uses

    H_00<=b/(e tau)+2/e+1/tau+1,

and multiplying by sqrt(beta) ya bounds the result by5. For crossing targets the unit cap is essential for a uniform reversal statement, and is already included in BU001.

Since a positive return is one step plus an ordinary hit, 1/Pi(s)<=1+H_s. Therefore

    Pi(s) gamma_s Hbar_s
       <=Pi(s)gamma_s(H_s+1)
       <=6/sqrt(beta)<=10/sqrt(beta).              (3.2)

We use the slack constant10. Beta<=1 follows by summing a certificate row. The bound is on a target hitting scale, not on global mixing or a claimed sqrt(beta) spectral gap.

## 4. Stationary reversal and exact shifted windows

For a stationary binary second-order source, the reversed word has the same source kernel. Equivalently, the reversed pair chain after exchanging the coordinates of each pair is P again. This follows from the four nontrivial triple-flux identities, of which the two distinct ones are

    Pi00 theta00(1)=ya=xe=Pi10 theta10(0),
    Pi01 theta01(1)=xb=w tau=Pi11 theta11(0).

The other triples are palindromic. Pair masses satisfy Pi01=Pi10. In particular, conditioned on the original terminal pair s, the reversed pair chain

    Z_j=swap(Y_(M-j)), j=0,...,M,

is an ordinary P-chain starting at v=swap(s). Moreover Pi(v)=Pi(s) and gamma_v=gamma_s.

The original count J1_s is EXACTLY the count of v in reverse indices m+1,...,M, a window of length n. The original J2_s is its count in reverse indices1,...,m, a window of length m. These are shifted state-count windows, not the reverse departure counts0,...,M-1. The uniform-start bounds(2.4) apply to each shifted window by the Markov property; no off-by-one endpoint is discarded.

Write p=Pi(v). If np>=1, simultaneous events

    J1_s>=np/16, J2_s<=4mp+1

imply, since m<=2n,

    J2_s<=9np,
    J1_s/(J1_s+J2_s)>=1/145>1/256.

Thus the original imbalance event is contained in the union of a lower tail for the reverse late window and an upper tail for the reverse early window. Conditional on the original endpoint s, its probability is at most

    2exp[-n/(8Hbar_v)]+exp[-m/(2Hbar_v)]
       <=3exp[-n/(8Hbar_v)].                       (4.1)

Both tail estimates are uniform over the random state at the beginning of their window.

## 5. Weighted assembly and stationary support boundary

For np>=1, multiply(4.1) by p gamma_v, use(3.2), and put z=n/(8Hbar_v). Since z exp(-z)<=1,

 p gamma_v P(imbalance | Y_M=s)
   <=30 exp[-n/(8Hbar_v)]/(sqrt(beta)Hbar_v)
   <=240/(n sqrt(beta)).                           (5.1)

If np<1, simply use p gamma_v<=p<1/n, which is also bounded by the last expression. Sum over the four states and use n>=M/3:

    E[gamma_(Y_M) 1_imbalance]
       <=960/(n sqrt(beta))
       <=2880/(M sqrt(beta))<4096/(M sqrt(beta)).

Unit loss gives the cap. Since q<=gamma coordinatewise, this proves(BP1).

For completeness, under a positive all-state certificate a qualifying binary stationary support is either full or a singleton absorbing diagonal, as established in SC003. In the singleton case stationary initialization stays on that diagonal and its designated exit q (and gamma) is zero, so the left side is zero. This proof does not claim arbitrary unsupported starts in that case; the theorem is explicitly stationary.

## 6. Provenance and remaining work

Read complete accepted BU001 v2 and its exact receipt; its weighted hitting-scale bound(3.1) is the only imported quantitative premise beyond standard finite-state Markov/Kac facts proved or recorded there. The concentration argument, shifted-window accounting and imbalance assembly are given above. SC003 supplies the model and support classification. This does not re-review SC003, BIF001 or the entire prior frontier.

A separate deterministic gate analysis and the generic balanced-history inverse-occupation bound are needed to turn(BP1) into a stationary adaptive estimator. They are not silently included here. The arbitrary-start weighted gate-bias inequality is still open in this note: stationary reversal and the Pi(s) multiplier cannot be replaced by an arbitrary initial law without additional work. This is neither formal/external peer review nor a novelty/publication claim.
