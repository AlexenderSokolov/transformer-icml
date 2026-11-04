# Independent exact-file review: tilted occupation terminal KL

Date: 3 November 2026.

## Verdict and exact scope

**PASS for the new statistical proof in Sections 1–7.** No mathematical gap was found in the candidate's arbitrary-start, full-history add-one terminal forward-KL theorem.

Reviewed source:

- `tilted_occupation_terminal_kl.candidate.v1.md`
- SHA256: `c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281`

The source file was read in full and its checksum was independently verified. This review does not modify that frozen source. The review was analytical; no simulation, training, numerical experiment, external upload, or public repository write was performed.

Section 8's statistical transfer inequality is also valid **conditional on its cited pathwise TV and support bounds**. The earlier architecture construction establishing those premises was not independently rechecked here. The literature, attribution, priority, and minimax comparisons in Section 9 were not independently rechecked here. This PASS must not be represented as an independent audit of those older construction or literature facts.

The proved conclusion is fixed-alphabet O_A(log n/n), with the displayed A^5 dependence. It is not a claim of optimal growing-alphabet dependence or binary first-order minimax optimality.

## 1. Occupation lemma and indexing

Let J_s(l)=sum_{i=0}^{l-1}1{Y_i=s}. For integer w>=1 define

    b_l(z)=P_z(Y_l=s,J_s(l)<w),
    M_l=max_z b_l(z).

Removing initial path steps can only decrease the count of departures from s. The Markov property therefore gives b_{l+1}(z)<=sum_y Q(z,y)b_l(y), so M_l is nonincreasing. On any deterministic infinite path, the flag {Y_l=s,J_s(l)<w} selects only the first w occurrences of s, including time zero when applicable. Thus sum_{l=0}^n b_l(z)<=w, and

    (n+1)M_n <= sum_{l=0}^n M_l
                 <= sum_z sum_{l=0}^n b_l(z) <= Dw.

Mixtures over starting states preserve this bound. Neither stationarity nor irreducibility is needed. In particular it applies to every tilted kernel used later, with the same arbitrary initial distribution.

## 2. Likelihood and deviation bounds

For p in (0,1), changing a single outgoing symbol probability to q in (0,1), and rescaling all other probabilities in that row by (1-q)/(1-p), preserves both the allowed pair-chain transitions and path support. Keeping the same initial distribution cancels its factor in the path likelihood. The exact ratio is

    (p/q)^K ((1-p)/(1-q))^(J-K).

On K/J>=q>p, or K/J<=q<p, its logarithm is at most -J d(q||p). The terminal event already belongs to the observed path; no extra terminal-state likelihood is missing. On m<=J<2m the arbitrary-start occupation lemma under the changed kernel gives the joint bound

    P(Y_n=s,m<=J<2m,K/J deviates beyond q)
        <= [2Dm/(n+1)] exp[-m d(q||p)].

The candidate's centered-Bernoulli exponential bound is valid: |Z|<=1 and E Z^2<=p imply

    log E exp(+-lambda Z) <= p lambda^2/[2(1-lambda/3)],
    0<=lambda<3.

Using lambda=delta/(p+delta/3) in the binary-KL variational formula gives the asserted lower bound delta^2/[2(p+delta/3)]. The selected delta=sqrt(2pt/m)+2t/(3m) makes this at least t/m. Also J<2m implies

    J delta <= sqrt(4Jpt)+4t/3.

Thus the strict random-J deviation event is contained in the appropriate deterministic empirical-frequency tail. Endpoint thresholds outside (0,1) have impossible strict tails and need no endpoint tilt. When p=0 or p=1, K=Jp almost surely, so the deviation event is empty.

A different deterministic tilted kernel can be used for each threshold. Layer-cake integration requires separate probability bounds, not one simultaneous alternative law and not a union bound over a continuum. It never conditions the row count to be binomial.

## 3. Scalar inequality and integration in the frozen candidate

For z=jp, a=k+1, x=(j+1)p, the source's inequalities follow from

    sqrt(2zu)<=z/2+u,
    z<=2k+10u/3,
    (k-z)^2<=8ku+128u^2/9,
    (x-a)^2<=16ku+31u^2,
    x<=2a+10u/3.

The generalized KL inequality h(x,a)<=(x-a)^2/a gives h<=47u when a>=u. When a<u, a>=1 and x<6u give h<=6u log(6u)+u<=48u(1+log u). These cases include the boundary symbol probabilities.

The rowwise scaling identity in Equation (12) is exact; its nonnegative correction follows from log(1+v)<=v. Taking u=2t gives the source's threshold f_m(t)=192t(1+log t)/m. Its layer-cake calculation is valid and yields

    E[1{E_m}Z] <= 384r + 2304r/e <1536r,
    r=D/(n+1).

Summing nonnegative expectations over symbols, disjoint dyadic bands, and terminal states is legitimate. With J=0 the row is uniform and its loss is at most log A; the occupation lemma with w=1 gives the stated contribution D^2 log A/(n+1). The deterministic cap log(n+A) is also valid because each add-one probability is at least 1/(n+A).

## 4. Independent direct-integral proof with constant 58

This is a separate analytical derivation supporting the same rate. It does not replace or modify the frozen candidate's constant 1536.

Fix a target state s, a symbol b, a dyadic band E={Y_n=s,m<=J_s<2m}, and p=p_s(b). Put

    x=C_{s,b}/J_s on E,
    delta=1/(2m), epsilon=1/J_s,
    H=2Dm/(n+1),
    f(p,y)=p log(p/y)-p+y.

Here 0 log 0=0. On the band, delta<=epsilon<=1/m and the add-one coordinate is y=(x+epsilon)/(1+A epsilon). Direct algebra gives

    f(p,y)<=f(p,x+epsilon)+Ap epsilon,
    f(p,x+epsilon)-f(p,x+delta)
        =epsilon-delta-p log[(x+epsilon)/(x+delta)]
        <=epsilon-delta.

Define the nonnegative functions

    G_-(x)=integral_x^p (p-t)/(t+delta) dt,  x<=p,
    G_+(x)=integral_p^x (t-p)/t dt,          x>=p.

For x<=p, integrating the derivative of f(p,x+delta), and using f(p,p+delta)<=delta, shows

    f(p,x+delta)<=delta+G_-(x).

For x>=p, f(p,x+delta)<=f(p,x)+delta=G_+(x)+delta. The formulas extend to p=0 by continuity where needed. Since epsilon-delta<=1/(2m), altogether

    f(p,y) <= (1+Ap)/m
              +G_-(x)1{x<p}+G_+(x)1{x>=p}.             (A)

For 0<p<1, apply the already established tilted-occupation probability bound at each deterministic t, then use Tonelli's theorem. The expectation of the last two terms of (A), multiplied by 1{E}, is at most H(I_-+I_+), where

    I_-=integral_0^p [(p-t)/(t+delta)] exp[-m d(t||p)] dt,
    I_+=integral_p^1 [(t-p)/t] exp[-m d(t||p)] dt.

For t>=p,

    d'(t||p)=log[t(1-p)/(p(1-t))]>=(t-p)/t,

so I_+<=1/m. For p/2<=t<=p,

    -d'(t||p)>=log(p/t)>=(p-t)/p,
    (p-t)/(t+delta)<=2(p-t)/p,

which bounds that part of I_- by 2/m.

For 0<=t<=p/2, binary KL decreases toward p, and

    d(t||p)>=d(p/2||p)>=c p,
    c=(1-log 2)/2.

The last inequality follows from

    (1-q)log[(1-q)/(1-p)]>=p-q

at q=p/2. Hence the remaining integral is bounded by

    p log(1+mp) exp(-cmp).

Writing z=mp and using log(1+z)<=z gives

    p log(1+mp) exp(-cmp)
        <=[1/m] z^2 exp(-cz)
        <=4/(c^2 e^2 m)<24/m.

Thus I_-<=26/m and I_+<=1/m. Since P(E)<=H, Equation (A) yields

    E[1{E}f(p,y)] <= H(28+Ap)/m.                       (B)

If p=0 or p=1, x=p almost surely, the two G terms vanish, and the stronger deterministic part of (A) proves (B) without any tilt.

Summing (B) over the A symbols gives 29AH/m, since sum_b p_b=1. Also sum_b f(p_b,y_b)=D_KL(p||y), because both rows sum to one. One band's loss for a fixed terminal state is therefore at most

    58AD/(n+1).

There are K_n=1+floor(log_2 n) bands and D possible terminal states. Adding the previously established J=0 term proves the alternate bound

    E D_KL(p_{Y_n}||B_{Y_n})
      <= [D^2/(n+1)] [log A+58 A K_n], n>=1.           (C)

This derivation handles the variable, history-dependent sample count through fixed bands and unconditional joint tails. No conditional-binomial or independence assumption is introduced.

## 5. Conditional verification of the output transfer

For probability rows B and R with R strictly positive, the entropy variational inequality gives

    D_KL(p||R)<=2D_KL(p||B)+log sum_b B_b^2/R_b
              <=2D_KL(p||B)+sum_b(B_b-R_b)^2/R_b.

Since the positive and negative differences each sum to TV(B,R),

    sum_b(B_b-R_b)^2<=2 TV(B,R)^2.

Consequently the source's premises TV(B,R)<=(44A+1)/L and min_b R_b>=1/(AL) imply its transfer penalty 2A(44A+1)^2/L. This verifies the transfer calculation, not the earlier architecture proof of those two premises.

## Final assessment

The frozen new proof passes independently. Its critical valid step is applying an arbitrary-start, kernel-uniform occupation bound under each tilted transition law. It does not multiply unrelated marginal probability bounds. The stronger direct-integral bound (C) provides a separate check of the rate. Architecture premises and literature status remain outside this independent review's verified scope.
