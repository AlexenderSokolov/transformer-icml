# BOD001 — Opposite-diagonal arbitrary-start weighted occupation

2026-11-02. Author candidate v1; fresh independent review required. No accepted file modified.

## Result

Let W=00,A=01,B=10,C=11, with transitions W→A of probability a, A→C of probability b, B→W of probability e, C→B of probability t (the other successors are W,B,A,C respectively). Assume a,b,e,t>0 and an all-state certificate P²(i,j)>=beta Pi(j), beta>0, with full stationary support. For M>=8 and A0>0, write J_C=sum_{j=0}^{M-1}1{Y_j=C}. Then

 E_W[1{Y_M=C} min(t,A0/(J_C+2))]
 <= (8192 A0/M)[1+ln(1+1/(sqrt(beta) A0))].             (BOD1)

The symbol-swapped C→W assertion holds identically. In fact beta M²>=1 is unnecessary for this particular statement (though needed in the intended sharper global cutoff). No mixing theorem is used.

## 1. Exact first-hit mean and uniform killed survival

Let T be the first hit of C and let h_i=E_i T, with h_C=0. Put rho=b+e-be and

 m=h_W=[rho+a(2-b)]/(ab), lambda=1/m.

First-step equations give h_A=m-1/a and h_B=1+h_A+e/a. Hence

 m<=H:=max_i h_i<=m+1<=2m,

where m>=2 since T>=2 from W. Also lambda<=b<=rho: indeed rho+a(2-b)>=a. This includes endpoints equal to one; rho>0.

For any transient start, Markov's inequality gives P(T>L)<=1/2 at L=ceil(4m), since H<=2m. Strong Markov at block endpoints gives P_i(T>n)<=2^{-floor(n/L)}. Since L<=5m and ln(2)/5>1/16,

 P_i(T>n)<=2 exp(-lambda n/16), n>=0.                 (1.1)

## 2. A first-hit density envelope, not marginal mixing

Write W_k,A_k,B_k for killed probabilities at time k from initial W. They obey

 A_k=a W_{k-1}+(1-e)B_{k-1}
    =a W_{k-1}+(1-e)(1-b)A_{k-2}.

Initial A_0=B_0=0. Thus, for n>=2, the first-hit density d_n=P_W(T=n) satisfies

 d_n=b A_{n-1}
     =ab sum_{j=0}^{floor((n-2)/2)}(1-rho)^j W_{n-2-2j}.

By (1.1),

 d_n<=2ab exp(-lambda(n-2)/16)
       /[1-(1-rho)exp(lambda/8)].

For 0<=lambda<=1, exp(lambda/8)<=1+lambda/4, so the denominator is >=rho-lambda/4>=3rho/4. Also exp(lambda/8)<=9/8+1/100<3/2. Consequently

 d_n<=4(ab/rho) exp(-lambda n/16).

Independently d_n<=b P_W(T>n-1)<=3b exp(-lambda n/16). Combining and noting

 min(b,ab/rho)/lambda
 =min(1,a/rho)[rho/a+2-b]<=3,

we obtain the uniform envelope

 d_n<=12 lambda exp(-lambda n/16), n>=1.             (2.1)

For n=1 the left side is zero. This is a bound on a first-hitting density from one diagonal to the other, not on global weighted marginals.

## 3. Cumulative weighted target visits

Let p=Pi(C). The accepted BU001 v2 §1 proves, for this same target and all-state certificate,

 sqrt(beta) p t H<=5.                                (3.1)

Here H is the maximum ordinary hit mean already defined, not a relaxation/mixing time. For completeness, this imported inequality follows from stationarity ya=xe, wt=xb, and b²>=beta w, together with the direct hit-time bounds in that source.

A useful finite-time identity requires no stationary initialization. The hitting potential h has

 (Ph-h)(i)=-1+1{i=C}/p.

For i≠C this is the first-step equation; for i=C it follows from Kac's positive-return mean 1/p, since 1+(Ph)(C)=1/p. Summing expectations for times 0,...,M from initial C gives, for V=sum_{n=0}^M1{Y_n=C},

 E_C V=p[M+1+E_C h(Y_{M+1})]
       <=p(M+1+H).

Using H>=m>=2 and (3.1),

 E_C(tV)<= (10/sqrt(beta))(1+M lambda).               (3.2)

All counts in this formula are the global count, not reset counts on separate excursions.

## 4. Reciprocal return coefficient and harmonic aggregation

For a finite d-state chain and a target s, the first positive return pgf F_s has Schur identity

 1-F_s(z)=det(I-zP)/det(I-zP_{-s}).

Formal logarithm expansion yields

 E_s[1{Y_n=s}/J_s(n)]
 =[z^n](-log(1-F_s(z)))
 =[tr(P^n)-tr(P_{-s}^n)]/n<=d/n, n>=1.

Indeed the coefficient is sum_{k>=1}P(tau_k=n)/k, and at the kth return the prior count equals k. This proves, for

 f(n)=E_C[1{Y_n=C}min(t,A0/(J_C(n)+2))],

 f(n)<=4A0/n for n>=1.                               (4.1)

Pathwise summing over all target visits gives

 sum_{n=0}^M f(n)=E_C sum_{j=0}^{V-1}min(t,A0/(j+2)).

For every integer V>=0, integral comparison (or splitting at tV=A0) gives

 sum_{j=0}^{V-1}min(t,A0/(j+2))
 <=A0[1+ln(1+tV/A0)].

Jensen and (3.2) imply

 sum_{n=0}^M f(n)
 <=A0[1+ln(1+10(1+M lambda)/(sqrt(beta) A0))].        (4.2)

## 5. First-hit convolution completes the proof

There are no C visits before T, so strong Markov gives the desired left side exactly as sum_{r=1}^M d_r f(M-r). Split r at floor(M/2). The early portion is at most8A0/M by (4.1). For the late portion, (2.1) and (4.2) give

 12 lambda exp(-lambda M/32) A0
 [1+ln(1+10(1+M lambda)/(sqrt(beta) A0))].

Set x=M lambda, s=sqrt(beta) A0, G=1+ln(1+1/s)>=1. Since 10(1+x)>=1,

 1+ln(1+10(1+x)/s)<=G+ln(10)+ln(1+x)<=4G+x.

The elementary maxima satisfy x exp(-x/32)<=12 and x² exp(-x/32)<=555. Hence the late portion is at most

 (12A0/M)(48G+555)<=(7236 A0/M)G.

Adding the early portion is bounded by8192 A0G/M. This proves (BOD1). Symmetry exchanges W,C and a,t and b,e.

## Scope

This closes only the opposite-diagonal weighted actual-terminal occupation component, subject to independent review. BU001 v2 supplies its accepted hitting-mean certificate inequality; the Schur and finite-time potential identities are proved here. BS001 and BAI003 were read for scope and accepted status, not used to assert an arbitrary-start theorem. There is no new predictor, port, runtime query, external publication, global mixing claim, or lower-bound claim.
