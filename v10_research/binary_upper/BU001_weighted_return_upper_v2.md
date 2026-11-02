# BU001 — Binary weighted return-time upper (candidate v2)

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

For beta>0 the supported chain is irreducible: if p_t>0, P²(s,t)>=beta p_t>0 for every supported start s. Stationarity makes support closed. Thus all supported hitting/return times below are finite, and Kac applies as proved in IU001.

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

A supported target with q_s=0 contributes identically zero to BU1 and is omitted before any division. For diagonal targets with x>0, q_s=0 cannot occur: if y>0 and a=0, stationarity forces e=0, contradicting e²>=beta y; the 11 argument is symmetric. Crossing targets always have q_s=1. The x=0 singleton case was handled above.

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

## 4. Unchanged SB001 decoder: explicit precision application

All following quantities except the decoded bank are analysis objects, not new inputs. Put z=kappa Q, Q>=16, M>=64. Write S for the actual-terminal risk of the accepted add-one row predictor u=(C+1)/(J+2). The inherited bound in SB001 is

    S<=2^13 Hstat<=2^13 sqrt(32)/sqrt(M+1).

Let B=E[2/(J+2)]. The inherited universal occupation lemma and Psi bound give

    B<=Psi(32/(M+1))<=2sqrt(32)/sqrt(M+1).

For J>0 let p_hat be the empirical exit fraction, q_actual its true exit probability, and u_exit the corresponding add-one probability. Pathwise |p_hat-u_exit|<=2/(J+2). Thus

    E[1_{J>0}|p_hat-q_actual|]<=S+B.                     (4.1)

The exit convention is 00→1 and 11→0; either successor can be designated exit on crossing rows. For diagonal rows the weight q_s of BU1 equals q_actual; for crossing rows q_s=1.

The selected bank has true total mass r=kappa J/[M+(kappa-1)J]. Let n0,n1 be its downward integer floors and N=n0+n1. On N>=1 necessarily J>0. Write n0=Qr(1-p_hat)-f0, n1=Qr p_hat-f1, where f0,f1 belong to [0,1). The pre-output-rounded normalized exit v=n1/N obeys

    v-p_hat=[p_hat f0-(1-p_hat)f1]/N.

The positive difference is at most p_hat/N<=p_hat and trivially at most 1-p_hat; the negative difference is at most (1-p_hat)/N<=1-p_hat and trivially at most p_hat. Hence

    |v-p_hat|<=min(p_hat,1-p_hat),
    |v-p_hat|<=min(1,2/(Qr)).

The second bound is the existing SB001 rounding bound. For a diagonal row, 1-Lipschitzness of p↦min(p,d) therefore gives

    |v-p_hat|<=min(q_s,2/(Qr))+|p_hat-q_actual|.

For a crossing row q_s=1 the same inequality holds (even without its last term). Also, for J>=1,

    2/(Qr)<=2/Q+6M/[z(J+2)].

Combining with the triangle inequality to the true target, on N>=1,

    |v-q_actual|<=min(q_s,A/(J+2))+2/Q
                       +2|p_hat-q_actual|,
    A=6M/z.                                             (4.2)

On N=0 the unchanged uniform fallback has loss at most one. If J>0 and N=0, both raw coordinates are below 1/Q, so Qr<2. Rearrangement gives

    (Q-2)kappa J<2(M-J), hence J<4M/z.

J=0 also satisfies this last strict inequality. Since J is integer and 4M/z>0, take w=ceil(4M/z)>=1 in the universal occupation bound to obtain

    P(N=0)<=16 ceil(4M/z)/(M+1)<=64/z+16/M.              (4.3)

Final ordered binary simplex rounding costs at most 1/Q. Integrate (4.2), use (4.1), and separately charge (4.3):

    R<=2S+2B+E min(q_Y,A/(J+2))+64/z+16/M+3/Q.           (4.4)

For beta>=M^-2, BU1 gives

 E min(q_Y,A/(J+2))
 <=24/z [17+ln(1+16z/(sqrt(beta)M))]
 <=480/z [1+ln(1+z/(sqrt(beta)M))],

where ln16<3. Moreover

 2S+2B+16/M
 <=[(2^14+4)sqrt(32)+16]/sqrt(M)
 <=2^17/sqrt(M).

For beta<M^-2, including beta=0, simply use the unchanged SB001 beta-free bound

 R<=S+Psi(32/(M+1))+Psi(96/z)+3/Q,

and Psi(96/z)<=96[1+ln(1+z)]/z. Its statistical terms are also bounded by 2^17/sqrt(M). Consequently, writing e0=max(sqrt(beta),1/M), the single explicit candidate bound is

 R<=min{1, 2^17/sqrt(M)+3/Q
                +(544/z)[1+ln(1+z/(M e0))]}.            (BU2-v2)

This is for stationary initialization only. The constant is deliberately conservative, not a numerical optimality claim. The proof treats q_s=0 by its zero weighted contribution and still charges zero-bank error separately; it never substitutes 0 into a denominator.

## 5. Source identity, implementation, and evidence limits

The exact sources read are recorded by SHA-256 in `BU001_source_bindings_v1.json`; no source was edited. The candidate BI001 lower and structural note are background, not assumed accepted theorems. The upper uses the binary structural identities proved again in Section 1, IU001's Kac argument, and the accepted SB001 empirical risk/occupation/decoder bounds. AU001's residual-mixture result is not needed for this stationary theorem.

The finite program is literally unchanged SB001: same two paid local-copy heads, complete eight-coordinate triple bank, query pair side value, integer weights {1,kappa}, Q-grid floors, uniform zero-bank fallback, post-cut normalization, final simplex rounding, and no extra exact ports or history rereads. Every implementation/resource/cost term of SB001 v2 §6 remains unchanged. No online q, stationary mass, beta, return time, or empirical count port is added. Configuring kappa from a known beta promise is separate paid setup, as in SB001 §7; BU2-v2 itself holds for every existing legal public kappa,Q configuration.

`check_bu001_v1.py` and `BU001_diagnostics_v1.json` corroborate 10,000 positive random kernels × four targets. Floating-point PGF checks allow absolute tolerance 1e-7; the recorded maximum ratio exceeds one by about 4.2e-9 in nearly singular cases. These are finite floating-point diagnostics, not exact proof or universal verification. Zero-support cases and the universal theorem rely on the written argument. Independent review is required. No arbitrary-start extension, accepted status, external novelty, or implementation benchmarking is claimed.
