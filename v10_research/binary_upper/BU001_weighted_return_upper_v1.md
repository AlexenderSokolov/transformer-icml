# BU001 — Binary weighted return-time upper (candidate)

2026-11-02. Author proof candidate, not independently reviewed. Stationary only. No accepted files changed.

## Main lemma

For a stationary binary second-order source in D2(beta), beta>0, let
`y=Pi00, x=Pi01=Pi10, w=Pi11`, and row exit probabilities
`a=theta00(1), b=theta01(1), e=theta10(0), t=theta11(0)`.
For the actual terminal prior count J at horizon M, define

    q_00=a, q_11=t, q_01=q_10=1.

For every A>0 and integer smoothing k>=1,

 E min(q_(Y_M), A/(J+k))
 <= (4A/M) [17+ln(1+96/(sqrt(beta) A))].                 (BU1)

The unit cap, and the inherited beta-free occupation upper, remain separately available. Constants are deliberately slack. Zero q contributes zero.

## 1. Hitting-time bounds for the forward chain

Assume x>0. Stationarity gives ya=xe and wt=xb. All-state two-step minorization gives

    e²>=beta y, b²>=beta w.

For a supported target s, H_s is the largest expected first hitting time of s over starts in stationary support (hitting time zero at s). For positive y,x,w, direct first-step equations give:

* H_00 <= b/(e t)+2/e+1/t+1.
* H_01 <= 2/a+1/t+2.
* H_10 <= 1/a+2/t+2 (by symbol symmetry).
* H_11 <= e/(b a)+2/b+1/a+1 (by symbol symmetry).

For example the exact hit times of 00 from 01,10,11 are respectively
`(b+2t)/(et)`, `(b+2t)/(et)-b/t-1`, and `(b+2t)/(et)+(1-b)/t-1`.
The exact hit times of 01 from 00,10,11 are `1/a`, `1+e/a`, and `1/t+1+e/a`.

Multiplication by sqrt(beta) p_s q_s yields a bound <=5. For 00 specifically,

 sqrt(beta) y a H_00
 <= sqrt(beta) [w+2x+e w/b+xe]
 <= sqrt(beta)(w+3x)+sqrt(w) <= 5.

For 01,

 sqrt(beta) x H_01
 <=2sqrt(beta)y/e+sqrt(beta)w/b+2sqrt(beta)x
 <=2sqrt(y)+sqrt(w)+2x <=5.

The other two follow by swapping symbols. If y=0, then e=0 and 00 is omitted from support; erase all waiting-at-00 terms, equivalently interpret y/e as zero in these bounds. If w=0 do the symmetric omission. For target00, necessarily y>0; when w=0, b=0 and its support-only hit bound is simply 2/e. The analogous target11 bound is 2/b. These statements follow directly from the same first-step equations on the smaller supported chain; no division by zero is taken. If x=0, positive beta forces stationary support to be a singleton 00 or 11: stationarity makes every supported diagonal absorbing, and the two-step minorization precludes two such classes. Its q is zero and contributes nothing.

Consequently for every relevant state

    H_s <=5/[sqrt(beta) p_s q_s].                       (1)

## 2. Reversal and exponential return tail

The stationary reversed pair chain, after swapping the coordinates of every pair, is exactly the original binary pair chain. Indeed its four rows use the same a,b,e,t, by ya=xe and wt=xb. For diagonal targets the q above is preserved; for either crossing target q=1, so the exchanged targets have identical p=x and the same bound (1).

Condition on the actual terminal state s and reverse the path. Let tau be its first positive return and tau_k its kth return. Kac's identity, proved in IU001 Lemma 2.1, gives E tau=1/p. Write Hbar=max(H_s,1/p). Since a positive return consists of one step followed by an ordinary hitting time, 1/p<=1+H_s. Thus

    Hbar <=6/[sqrt(beta) p q].

For completeness the elementary hitting-time moment induction is as follows. Consider the family of ordinary hitting laws from non-target states and the positive-return law from the target. All have mean at most Hbar. For any such stopping time T and integer m>=1,

 T^m <=m sum_(j=0)^(T-1) (T-j)^(m-1).

Conditioning on survival and the state at time j, the remaining law belongs to the same family (at j=0 it is the original law). Induction gives

 E T^m <= m! Hbar^(m-1) E T.

Take lambda=sqrt(beta) p q/24, so lambda Hbar<=1/4. Expansion in nonnegative powers and the moment bound imply

 E exp(lambda tau)<=1+lambda/[p(1-lambda Hbar)]
                    <=exp(2lambda/p).

Strong Markov at successive returns gives E exp(lambda tau_k)<=exp(2k lambda/p). If Mp>=16, k=ceil(Mp/16)<=Mp/8, and hence

 P_s(J<Mp/16)=P_s(tau_k>M)
 <=exp(-lambda M+2k lambda/p)
 <=exp(-sqrt(beta) Mp q/32).

If Mp<16, the unit probability cap gives the following common bound, valid for all M:

 P_s(J<Mp/16)<=2 exp(-sqrt(beta) Mp q/48).                (2)

This is not a claim that the pair chain's global spectral gap improves to sqrt(beta).

## 3. Weighted reciprocal integration

Put mu=Mp, alpha=A/mu. Kac and Markov give P_s(J<j)<=j/mu for integer j>=1. For V=min(q,A/(J+k)), split layer cake at 16alpha. The part below that threshold is <=16alpha. For a layer u with 16alpha<u<q, the positive integer threshold ceil(A/u-k) is at most A/u and less than mu/16. Therefore

 P_s(V>u)<=min(alpha/u, B),
 B=2exp(-sqrt(beta)mu q/48).

Integration over (0,q) yields

 E_s V<=alpha [17+ln_+(B q/alpha)].

Since (mu q)exp(-sqrt(beta)mu q/48)<=48/sqrt(beta),

 E_s V<=A/(Mp) [17+ln(1+96/(sqrt(beta)A))].

Multiply by p and sum over the at most four supported states to obtain BU1. This proof also covers q<=16alpha directly by the unit cap q<=16alpha.

## 4. Unchanged SB001 decoder: precision application

Let z=kappa Q, J>0, r=kappa J/[M+(kappa-1)J], and let p_hat be the empirical exit fraction relative to the natural row default (00→0, 11→1; either default can be used for crossing rows). Let n0,n1 be the two downward floors, N=n0+n1.

When N>=1 write n0=Qr(1-p_hat)-f0, n1=Qr p_hat-f1 with f0,f1 in [0,1). Then normalized exit probability v=n1/N satisfies

    v-p_hat=[p_hat f0-(1-p_hat)f1]/N.

Consequently |v-p_hat|<=min(p_hat,1-p_hat), and also the existing SB floor bound <=min(1,2/(Qr)). In particular for any true exit q in [0,1],

 |v-p_hat|<=min(q,2/(Qr))+|p_hat-q|.

For crossing contexts simply use q=1. On the all-zero branch Qr<2. For Q>=16, this implies J<4M/z: solve (Q-2)kappa J<2(M-J). Hence its probability is O(1/z+1/M) by the inherited universal occupation lemma; J=0 is included by using the integer threshold ceil(4M/z)+1. No decoder modification is necessary.

For J>=1, 2/(Qr)<=2/Q+6M/[z(J+2)]. Thus use BU1 with A=6M/z, plus the 2/Q term. Comparing unsmoothed empirical rows with the accepted smoothed empirical predictor costs the inherited statistical risk plus E[2/(J+2)]; the latter is O(log M/M)=O(M^-1/2), by the universal occupation bound. The additional |p_hat-q| above is bounded in exactly the same fashion. Final ordered binary simplex rounding costs <=1/Q.

Combining gives for a universal constant C and unchanged SB001 binary program, under stationary initialization,

 R <= C min{1, M^-1/2 + Q^-1
          +[1+ln(1+z/(M max(sqrt(beta),1/M)))]/z}.        (BU2)

For beta>=M^-2 use BU1; for beta<M^-2 use unchanged SB beta-free upper (which has log(1+z)/z) instead. Constants absorb fixed K=2 and all J=0/allzero exceptional terms. This is a candidate derivation requiring independent review, not an accepted upper or an arbitrary-initialization theorem.
