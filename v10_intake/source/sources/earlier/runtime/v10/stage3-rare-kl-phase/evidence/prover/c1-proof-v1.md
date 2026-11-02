# C1: finite-history statistical classification, fixed candidate v1

Prover, 2026-10-25. Exact obligation:
`1dd6b3b9191952ba424db347dab176cd3336d5399831f867f595a13a40e5ce25`.
This is a self-contained proof candidate under the current PROBLEM.md
D1–D4 (with the scope restrictions in D5–D7). It has no native predecessors.
No prior-project Fact, count recovery theorem, or discussion verdict is a
premise. It awaits Counter's fixed report and Lead review before submission.
All logarithms are natural. Coordinates of a probability vector are (0,1).

## 1. Experiment, predictor and exact conclusions

Let 0<u<1/4, 1/4<=t<=3/4, w=(1-u)/3 and alpha=u/w=3u/(1-u).
Then 0<alpha<1, r=alpha*t is in (0,3/4), and r>=3u/4.
Let S_i=(X_(i-1),X_i), i>=2. In state order (00,01,10,11), the
transition matrix P and initial distribution pi are

    P = [[1-t, t,   0,   0],
         [0,   0, 1/2, 1/2],
         [r, 1-r,   0,   0],
         [0,   0, 1/2, 1/2]],       pi=(u,w,w,w).

Only shifts ab->bc are possible. Each permitted symbol extension has
strictly positive probability. Thus every binary history of every finite
length has positive probability. The observed history is H=X_1^N; S_N is
its actual final pair and X_(N+1) is not observed. Define

    R_N(u,t;q) = E KL(p(.|S_N)||q(H)),
    R_N,s(u,t;q) = E[KL(p(.|s)||q(H)) | S_N=s].

For a randomized q, expectation also includes a source-independent
randomization kernel given H. Comparators may use all of H. Define
M_N=inf_q sup_(u,t) R_N and C_N(u)=inf_q sup_t R_N,00, with the infimum
over all such probability predictors. In the latter fixed-u experiment
the comparator can know u. The attaining algorithm below is never given u.

For N=3,4,5, set a_N=(1/2,1/2). For N>=6 set

    m=floor(N/2), M=m-2>=1, g=N-m.

For each s let D_s=sum_(i=2)^(m-1) 1{S_i=s}; let C_s,c count those same
indices with X_(i+1)=c. These are precisely the M triples at positions
3,...,m. The unquantized prefix algorithm uses the row s=S_N and returns

    s=00: a_1=clip_[1/4,3/4]((C_00,1+1)/(D_00+2)), a_0=1-a_1;
    s=10: a_0=min(3/4,(C_10,0+1)/(D_10+2)), a_1=1-a_0;
    s=01 or11: a_0=a_1=1/2.

The later observations provide S_N but no additional estimation samples.
Every branch is defined even at D_s=0, when the output is uniform. There
is no fixed positive lower clip on row10's estimated rare successor.

We prove, for every N>=3 and every (u,t) in the stated domain,

    R_N(u,t;a_N) <= 1000000/N,                              (C1.1)
    R_N,00(u,t;a_N) <= 160000/(1+Nu).                       (C1.2)

For every fixed u and all full-history randomized comparators, we prove

    C_N(u) >= 3/[16384(1+(N-2)u)],                         (C1.3)
    inf_q sup_t R_N(u,t;q) >= 3u/[16384(1+(N-2)u)].         (C1.4)

In particular,

    M_N >= 3/[16384(N+6)].                                (C1.5)

The lower bounds remain valid if u is supplied to the comparator. Together
these give average minimax order 1/N and, for every fixed u, conditional00
minimax order 1/(1+Nu), with constants uniform in u. This is a theorem for
this specified family; it is not a theorem for all stationary order-two laws.

## 2. Elementary inequalities used below

Write kl(p,q) for Bernoulli KL. For 0<q<1, log z<=z-1 gives

    kl(p,q) <= (p-q)^2/[q(1-q)].                           (C1.6)

Indeed apply the log inequality separately to p/q and (1-p)/(1-q) and
simplify; endpoint values of p follow by limits. Also

    kl(p,q) >= 2(p-q)^2.                                  (C1.7)

For fixed q in (0,1), the difference of the two sides as a function of p
has value and derivative zero at p=q and second derivative
1/[p(1-p)]-4>=0. Integration on either side of q proves the assertion;
boundary cases follow by limits, with infinite KL handled in the usual way.

For two finite probability laws mu,nu, let TV(mu,nu)=1/2 sum|mu-nu|.
Then

    TV(mu,nu) <= sqrt(KL(mu||nu)/2).                       (C1.8)

To see this without a testing theorem, take A={h:mu(h)>=nu(h)}. Then
mu(A)-nu(A)=TV. Group the KL sum over A and its complement. Each group's
sum is at least its grouped contribution: this follows by convexity of
x log x with nu weights (the zero-weight cases follow by limits).
Thus KL(mu||nu)>=kl(mu(A),nu(A))>=2TV^2 by (C1.7).

A common stochastic kernel contracts TV: expand each output difference,
apply the triangle inequality and sum kernel rows. Further, if 0<=f<=L,

    |E_mu f-E_nu f| <= L TV(mu,nu).                        (C1.9)

For example, write f(h)=integral_0^L 1{f(h)>v}dv and use the event
definition of TV. These elementary facts also cover randomized tests by
integrating a function with values in [0,1].

## 3. Stationarity, reverse kernel and uniform mixing

The four incoming masses for pi P are

    u(1-t)+wr=u,   ut+w(1-r)=w,   (w+w)/2=w,   (w+w)/2=w.

Hence pi P=pi. The initialized pair chain is stationary and in particular
Pr(S_N=00)=u and Pr(S_N=s)=w for each other row, for every N.

Two-step paths from (00,01,10,11) to10 have respective probabilities
t/2, 1/4, (1-r)/2, 1/4: from00 or10 go through01, and from01 or11
go through11. Each is >=1/8. Therefore

    P^2(x,10)>=1/8,   P^3(x,00)>=r/8>=3u/32.              (C1.10)

The following three-step paths all end at01:

    00->01->10->01: t(1-r)/2 >=1/32;
    01->11->10->01: (1-r)/4 >=1/16;
    10->01->10->01: (1-r)^2/2 >=1/32;
    11->11->10->01: (1-r)/4 >=1/16.

Thus P^3(x,01)>=1/32 for every x. Directly applying
R(i,j)=pi_j P(j,i)/pi_i gives the stationary reverse kernel

    R = [[1-t,   0,   t,   0],
         [r,     0, 1-r,   0],
         [0,   1/2,   0, 1/2],
         [0,   1/2,   0, 1/2]].

If sigma exchanges01 and10, then R(i,j)=P(sigma(i),sigma(j)) and
pi is sigma-invariant. Consequently R^3(x,10)>=1/32. This is a
conjugacy, not P=R or ordinary detailed balance: P(00,01)>0 while
P(01,00)=0 already rules out ordinary reversibility with positive pi.

Whenever every row of K puts mass at least eta on a common state z,
K=eta*delta_z+(1-eta)*K' for a stochastic K'. The common term cancels
in differences of probability measures; TV contracts by at most 1-eta.
Apply this to R^3 and use pi R=pi, which follows directly from the reverse
kernel formula. Extra steps also contract TV. Since TV<=1 initially,

    TV(R^g(s,.),pi) <= d_g=(31/32)^floor(g/3)              (C1.11)

for all starting states s, uniformly over the entire parameter domain.

## 4. Entire-prefix bridge for the actual terminal query

For any consistent path s_2,...,s_N, stationarity and the reverse formula
give the telescoping identity

    pi_(s_2) product_(i=2)^(N-1) P(s_i,s_(i+1))
      = pi_(s_N) product_(i=2)^(N-1) R(s_(i+1),s_i).

Therefore, conditional on the actual S_N=s, the whole backward pair path
is an R-chain started at s. After g=N-m backward steps, S_m has law
R^g(s,.). Given S_m, its earlier backward path to S_2 has a common kernel
independent of s. A consistent path S_m,...,S_2 uniquely specifies X_1^m.
The unconditional stationary prefix is the image of pi under exactly
the same kernel. By TV contraction and (C1.11),

    TV(Law(X_1^m | S_N=s), Law(X_1^m)) <= d_g.             (C1.12)

This compares the entire prefix, including every count and its dependence
on its endpoint. There is no independence assertion and no division by pi_s.

For each s let f_s(X_1^m) be the loss of the fixed row-s estimator above,
and K_s=E f_s for a stationary prefix. Both row00 coordinates are >=1/4;
row10 has q_1>=1/4 and q_0>=1/(M+2) (the upper clipping cannot violate
this since M>=1). As -sum p_c log p_c>=0,

    0<=f_00<=log4,
    0<=f_10<=log max(M+2,4),     f_01=f_11=0.             (C1.13)

Apply (C1.9) to (C1.12) separately for each fixed row, then weight by the
actual terminal law pi. Since u+w<1 and m=M+2,

    R_N,00 <= K_00+d_g log4,
    R_N <= u K_00+w K_10+d_g log max(m,4).                (C1.14)

We make this comparison for the unquantized estimator. The loss caps here
do not depend on any later output precision Q.

## 5. Tools for dependent counts at a deterministic horizon

### 5.1 Spaced visits

Suppose P^ell(x,s)>=p for all x. Inspect only source positions

    i_j=2+ell*j,   j=1,...,B,   B=floor((M-1)/ell).

Every inspected position is in 2,...,m-1. Conditional on all information
through the previous inspected position (through S_2 for j=1), its
indicator I_j=1{S_(i_j)=s} has success probability at least p. Hence for
lambda>0, successive conditioning gives

    E exp(-lambda sum_j I_j) <= (1-p+p exp(-lambda))^B.

Set lambda=log2. Exponential Markov inequality, log(1-z)<=-z and
log2<3/4 imply

    Pr(sum_j I_j<=Bp/2)
       <= exp((log2)Bp/2-Bp/2) <= exp(-Bp/8).             (C1.15)

No independence of I_j is needed, and D_s>=sum_j I_j pathwise.
For row00 take ell=3,p=3u/32. If M>=6 then
B=floor((M-1)/3)>=M/6 (check residues modulo3), so with x=Mu,

    Pr(D_00<x/128) <= exp(-x/512).                        (C1.16)

Indeed Bp/2>=x/128 and Bp/8>=x/512. For row10 take ell=2,p=1/8.
For M>=64, B=floor((M-1)/2)>=M/4>=16 and define the deterministic
integer d=floor(B/16). Since floor z>=z/2 for z>=1,

    d>=B/32>=M/128, d>=1,
    Pr(D_10<d) <= exp(-M/256).                            (C1.17)

Here d<=B/16=Bp/2, so (C1.15) applies. These are proof thresholds, not
inputs or event labels given to the predictor.

### 5.2 Martingale variance

Fix a row s and one chosen successor, with true probability p. Put
C=C_s,c, D=D_s and Z=C-pD. For i=2,...,m-1 its increment is
1{S_i=s}(1{X_(i+1)=c}-p). The row indicator is measurable before the
successor is sampled, so the increment's conditional mean is zero and
conditional second moment is p(1-p)1{S_i=s}. For i<j, conditioning the
product on information through X_j makes its expectation zero. Summing
these identities at the deterministic horizon yields

    E Z^2=p(1-p) E D,       E D=M pi_s.                   (C1.18)

This is unconditional variance, not a claim about the law of C given D.

### 5.3 Fixed-length row-stack events

Independently for each row s, prepare an infinite sequence of iid
Bernoulli successor bits with that row's probability, independent of the
initial pi draw. Each visit uses its row's next unused bit. Conditional on
the generated past, the next unused bit has the required row law: events
specifying a past only constrain finitely many already used bits. Induction
on time therefore reproduces exactly the Markov path law. This is a proof
coupling, not extra data or randomness available to the algorithm.

Let B_s(k) count the chosen successes in the first k stack bits. Then
C=B_s(D) pathwise. Since partial sums are nondecreasing, for deterministic
integer d>=1,

    {D>=d, C<pd/2} subset {B_s(d)<pd/2}.

The latter involves exactly d iid bits. Their exponential moment, by the
same calculation as (C1.15), gives

    Pr(D>=d,C<pd/2) <= exp(-pd/8).                        (C1.19)

The random visit count D can depend on the used stack. We never assert
that C conditional on D is binomial; such an assertion would in general
be false. (C1.18) and (C1.19) serve separate purposes.

For a concrete check of that failure, take a prefix of length4 (M=2)
and count row00's next-1 successes. The event D=1 either starts at00
and immediately exits to01 (probability ut, with C=1), or starts at10
and enters00 on the first transition (probability wr=ut, with the next
success having probability t). All other initial states contribute zero
to D=1. Hence Pr(C=1 | D=1)=(1+t)/2, not t. At u=1/8,t=3/8 this
is11/16 instead of3/8. This example refutes only the unused shortcut;
the deterministic-horizon and fixed-stack arguments above remain valid.

## 6. Stationary-prefix row risks with explicit constants

### 6.1 Rare row00, interior successor

Set x=Mu and Z=C_00,1-tD_00. Projection onto [1/4,3/4] cannot increase
distance to t in that interval. For the projected estimate q, q(1-q)>=3/16.
Writing v=(C+1)/(D+2), we have v-t=(Z+1-2t)/(D+2). By (C1.6),
(A+B)^2<=2A^2+2B^2 and |1-2t|<=1,

    kl(t,q)<=12(Z^2+1)/(D+2)^2,       E Z^2<=x/4.          (C1.20)

When M>=6, split on D>=x/128. On this event, taking an unconditional
second moment is sufficient and gives expectation at most
12(x/4+1)/(x/128+2)^2. After multiplication by 1+x this is

    49152 (x+1)(x+4)/(x+256)^2 <=49152.

On its complement, use the genuine loss cap log4 and (C1.16).
Since x exp(-x/512)<=512/e, (1+x)exp(-x/512)<257, and log4<3/2,
the complementary contribution after multiplication by 1+x is <386.
The sum is less than 50000. For 1<=M<6, x<5/4, and the deterministic
cap log4 by itself satisfies the same bound. Thus, for every M>=1,

    K_00 <= 50000/(1+Mu).                                (C1.21)

This also covers zero counts, repeated visits, and paths ending partway
through a run of row00 visits.

### 6.2 Common row10, arbitrarily rare successor

Let p=r, C=C_10,0, D=D_10, v=(C+1)/(D+2), q=min(v,3/4) and Z=C-pD.
For v>=p the derivative of (p-v)^2/v is 1-p^2/v^2>=0. Whenever clipping
occurs, v>3/4>p, so clipping cannot increase this ratio. Since 1-q>=1/4,
(C1.6) and (C1.18) give

    kl(p,q)<=8(Z^2+1)/[(D+2)(C+1)],     E Z^2<=pM.         (C1.22)

For M>=64 choose d from (C1.17), and partition all paths into

    G={D>=d,C>=pd/2}, H={D>=d,C<pd/2}, J={D<d}.

On G, (C1.22) and E[Z^2;G]<=E Z^2 yield

    E[loss;G] <=8(pM+1)/[d max(1,pd/2)]
              <=16M/d^2+8/d <=263168/M.                  (C1.23)

For H a logarithmic loss bound is needed. For 0<q<=3/4,

    kl(p,q)<=p log_+(p/q)+4q,  log_+(z)=max(0,log z).     (C1.24)

Indeed drop the nonpositive (1-p)log(1-p), and bound
-(1-p)log(1-q)<=-log(1-q)<=q/(1-q)<=4q. On H,

    q>=1/(M+2),   q<=v<=(pd/2+1)/(d+2)<=p/2+1/d.

Also (M+2)/d<=256. With y=pd and (C1.19), this proves

    E[loss;H]
      <=[y log_+(256y)+2y+4] exp(-y/8)/d <=108/d
      <=13824/M.                                        (C1.25)

For completeness, log_+(256y)<=8+y for y>0 (use log y<=y-1 and
log256<6 when the logarithm is positive). The numerator is at most
10y+y^2+4. Its product with exp(-y/8) is at most 40+64+4=108:
max y exp(-y/8)=8/e<4 and max y^2 exp(-y/8)=256/e^2<64.
This works uniformly as p tends to zero; no lower bound on p was used.

On J, (C1.13), (C1.17) and log(M+2)<=M for M>=64 give

    E[loss;J] <= M exp(-M/256) <=65536/M,                 (C1.26)

because max_(x>=0) x^2 exp(-x/256)=262144/e^2<65536.
The sum in (C1.23)–(C1.26) is 342528/M. For M>=64,
342528(1+1/64)<400000, so this is at most 400000/(M+1).
For 1<=M<64 the cap log max(M+2,4)<=log65<5 is more than sufficient.
We have therefore proved, for all M>=1,

    K_10 <=400000/(M+1).                                 (C1.27)

Every bad event was multiplied by a valid loss bound. In particular a
TV bound of one is never substituted for a bound on KL loss.

## 7. Actual-terminal rates, including all small N

For N>=6 substitute (C1.21),(C1.27) into (C1.14):

    R_N <=50000u/(1+Mu)+400000w/(M+1)
            +d_g log max(m,4).                          (C1.28)

We have u/(1+Mu)<=1/(M+1), w<1/3, and M+1>=N/4. The sum of the first
two terms is at most (50000+400000/3)*4/N<800000/N.
Since g>=N/2, floor(g/3)>=N/6-1 and log(31/32)<=-1/32,

    d_g<=2 exp(-N/192).

The elementary estimate log max(m,4)<=N then shows that the last term
in (C1.28) is at most 73728/N: indeed
max_(x>=0) 2x^2 exp(-x/192)=294912/e^2<73728.
This proves (C1.1) for N>=6.

For the conditional risk, N<=2M+5 and u<1/4 imply
1+Nu<=3(1+Mu). Hence the K_00 contribution in (C1.14), multiplied by
1+Nu, is at most 150000. The mixing contribution satisfies

    (1+Nu)d_g log4 <=3(1+N/4) exp(-N/192)<75.

To check the last number directly, the maximum over N>=0 is
144 exp(-47/48); exp(47/48)>=1+47/48>144/75.
Thus 150000+75<160000 proves (C1.2). For N=3,4,5 the output is uniform
and every binary KL loss to uniform is <=log2. Since 1+Nu<1+5/4,
both (C1.1) and (C1.2) follow directly. No M=0 or negative-M lemma was
invoked for these branches.

## 8. Full-history conditional lower bound

Fix u, write n=N-2, and let P_t^00 denote the law of the full observed
history conditional on actual S_N=00. By the exact backward factorization
in section4, this experiment is equivalent to an R-chain Y_0,...,Y_n
started at Y_0=00; the backward path determines the full history and vice
versa. For j=0,...,n-1 put U_i=sum_j Pr_t(Y_j=i), so U_i<=n.
The conditional drift of 1{Y_j=00} is -t in state00, r=alpha*t in state01,
and zero elsewhere. Summing its expectations yields

    t U_00 = 1-Pr_t(Y_n=00)+alpha*t U_01,
    U_00 <= 1/t+alpha*n.                                 (C1.29)

The term 1-Pr(Y_n=00) is retained. It represents information in the
terminal zero run; declaring that the terminal context conveys no
information before an earlier rare visit would discard it incorrectly.

Choose t_0,t_1 in [5/16,7/16], Delta=t_1-t_0>0. Since
t_1(1-t_1)>=55/256>1/5, (C1.6) gives

    kl(t_0,t_1)<=5 Delta^2,
    kl(alpha*t_0,alpha*t_1)<=5 alpha Delta^2.              (C1.30)

For the latter, the denominator is alpha*t_1(1-alpha*t_1), which is
at least alpha*t_1(1-t_1)>alpha/5. Only reverse rows00 and01 differ.
All allowed edges have positive probability under both laws and the same
structural zeros, so their full-path log likelihood ratio is the sum of
the transition log ratios. Taking expectation under t_0 proves the
chain-rule identity, with initial state equal to00 under both laws.
By (C1.29), (C1.30), 1/t_0<=16/5 and alpha<4u,

    KL(P_(t_0)^00 || P_(t_1)^00)
      <=5 Delta^2(U_00+alpha U_01)
      <=(16+40nu) Delta^2 <=40(1+nu) Delta^2.             (C1.31)

This accounts for every one of the N-2 reverse transitions in the entire
observed history, with no separated prefix or independent query assumed.

Now set

    Delta=1/[32 sqrt(1+nu)],
    t_0=3/8-Delta/2,  t_1=3/8+Delta/2.

Both belong to [5/16,7/16]. Equations (C1.8),(C1.31) give
TV(P_(t_0)^00,P_(t_1)^00)<=sqrt5/16<1/4.
Given any full-history predictor's next-1 coordinate q_1, decide law1
when q_1>=3/8 and law0 otherwise. On an error, |q_1-t_i|>=Delta/2, so
(C1.7) bounds its loss below by Delta^2/2. The sum of the two error
probabilities is at least 1-TV: for a deterministic event A it equals
1+P_0(A)-P_1(A); for a randomized test replace 1_A by its conditional
acceptance probability in [0,1] and use (C1.9). A source-independent
seed or randomization kernel therefore cannot improve this testing bound.
Taking the larger of the two conditional risks gives

    max_(i=0,1) R_N,00(u,t_i;q)
      >=Delta^2(1-TV)/4 >=3/[16384(1+nu)].                (C1.32)

Zero coordinates of q cause no problem: where the target is positive and
q has a zero, the loss is infinite and the lower inequality is automatic.
All comparator outputs and tests may depend on known u, which has the
same value in both experiments. Taking the infimum proves (C1.3).

## 9. Average lower bound, first-order subcurve and quantifiers

The two testing laws have the same actual terminal mass u. For each of
them R_N(u,t_i;q)>=u R_N,00(u,t_i;q), by nonnegativity of the other
row losses. Hence (C1.32) proves (C1.4); this multiplication occurs only
after the full conditional-history testing argument. Choosing u=1/8 gives

    3u/[16384(1+(N-2)u)]=3/[16384(N+6)],

which implies (C1.5) for the unknown-parameter minimax class as well.
For N>=3, N+6<=3N, so M_N>=1/(16384N). For every fixed u,
1+(N-2)u<=1+Nu, so (C1.3) is at least
3/[16384(1+Nu)]. The single unknown-(u,t) estimator in section1 gives
the opposite constant-factor bounds simultaneously for all u.

The law is first-order exactly when the two rows with last symbol0
coincide: t=1-alpha*t, that is

    t=(1-u)/(1+2u).

The other last-symbol pair of rows already agrees. The displayed value
lies in the allowed interval precisely for 1/10<=u<1/4; it is always
strictly greater than1/2 in our u-domain. Thus the family includes a
first-order subcurve (e.g. u=1/8,t=7/10). All upper bounds include it.
Every statistical lower witness above has t<1/2 and is genuinely order two.

At every fixed law (u,t) with u>0, (C1.1),(C1.2) imply expected-KL
convergence to zero. Conditional convergence is not uniform over laws
whose rare mass approaches zero with N. To be explicit, use fixed
t_0=11/32,t_1=13/32, Delta=1/16. When nu<=1, (C1.31) is at most
80/256, so TV<1/2 and the same test gives maximum conditional risk
at least 1/2048. Choose u_N=1/(N+1) for N>=4. For every predictor
sequence there is a choice t_N in {11/32,13/32} at each N with this
nonvanishing conditional lower bound. This is a triangular family,
not failure of convergence at a fixed positive-u source. The finite-N
minimax statement is not a claim that one fixed t maximizes risk for
all N, nor an almost-sure convergence theorem.

## 10. Scope and submission record

This proves the requested statistical claims for the explicit prefix
estimator as a function of observed data. Its actual finite causal
frontend, charge for S_N access, count recovery and complete resources
belong to C3 and are not premises or conclusions here. No source-dependent
labels, hidden samples, future symbols or altered source processes enter
the estimator or the proof. The stack construction is only a coupling.

The derivation was checked against the current D1–D7 and the Lead
checkpoint SHA256 `7c19965199c6cd92dc578c3a3f4d91009fbefc2948754b5de6e21b292dce8b4a`.
Source009 proof/review informed the candidate route, but every statistical
step used here is stated and proved above. There are no citations to old
native Facts and no old-root operation is required. This fixed candidate
is not an admission: actual Fact IDs=[], actual Evidence IDs=[] at writing.
