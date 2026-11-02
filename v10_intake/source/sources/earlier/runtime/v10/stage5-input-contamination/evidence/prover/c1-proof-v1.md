# Stage5 C1: self-contained actual-terminal input-contamination upper

Author: Prover, 2026-10-26. Fixed proof v1.
Exact obligation: `b5f118d33a9d9687ac8e3d48ca7df6e5c0403aeba52c026d88087e385e813354`.
Contract: `873515c4586d37a2bde324010bea6ae30f820927b7c25ded15b784a79eef7e45`.
Submission predecessors: **[]**.

## 0. Claim, scope and provenance

Under this project's D1-D3, the deterministic family defined in §§1,10
uses only Z,N,k,Q, is independent of unknown u,t and of the channel, and
for every legal public tuple, every D1 source and every D2 channel satisfies

    R_av <= 16000000/(3N) + 135680 k/N + 3/Q.             (T)

All expectations refer to the actual same-history terminal pair S_N.
This file proves every statistical and grid premise used in (T), with no
Fact predecessor. Historical sources are confined to this workspace's
inputs/source-stage4. The clean argument below is attributed to Prover
stage4 c1-proof-v2 §§1-7 and elementary inequalities; the pollution and grid
argument to Prover probe012 upper-program-certificate-v1 §§1-4. Their exact
byte hashes are appended. These are derivation sources, not admitted
premises: all needed arguments are written here. Current PROBLEM.md/D1-D7
and inputs/AUTONOMOUS_RESEARCH.md determine scope. No old campaign is accessed.

This is C1 only. D4-D5 constructions and resource vectors belong to C3;
no old primitive/compiler interface is assumed here. The family is a
finite algorithm: scan the observed string, form eight counts, evaluate
the exact integer output formulas, write the three specified fields, then
clear other mutable data. Its implementation costs are not asserted here.
GPU work is zero; no diagnostic suite is rerun. Native acceptance, if
obtained, is recorded separately from this fixed mathematical text.

## 1. Experiment, one predictor and proof-only clean comparator

Fix N>=3 and Q=2^b with integer b>=1. If N>=6, put m=floor(N/2),
M=m-2>=1 and allow integer 0<=k<=floor(M/1024). For N=3,4,5 set k=0.
For unknown 0<u<1/4 and 1/4<=t<=3/4 put w=(1-u)/3 and r=ut/w.
Then 1/4<w<1/3, 0<r<3/4 and r>=3u/4. The pair chain
S_i=(X_(i-1),X_i), i>=2, has, in state order (00,01,10,11),

    P = [[1-t, t,   0,   0],
         [0,   0, 1/2, 1/2],
         [r, 1-r,   0,   0],
         [0,   0, 1/2, 1/2]],          pi=(u,w,w,w).

Start S_2 with pi. The next-one target probabilities p_s(1) are
(t,1/2,1-r,1/2). Only X_1^N is observed by the channel; Y=X_(N+1) is not.
The source-independent randomized batch channel has independent private
coins omega and returns Z=T(X_1^N,omega). For every input and every seed,
it preserves positions N-1,N and changes at most k of positions 1,...,N-2.
It may inspect the entire history, including S_N. Our predictor sees only
Z,N,k,Q: no clean prefix, endpoint, count, u,t, future Y or seed. Its query is

    s=(Z_(N-1),Z_N)=S_N.

All risks average KL(p_s||q) over source and channel coins. Given X_1^N
and the independent channel coins, Y still has law p_(S_N), so this is
the excess expected next-symbol logarithmic loss. No Markov or other
probability model is imposed on Z.

For N>=6 and any path y, C_sc(y) counts j=3,...,m such that
(y_(j-2),y_(j-1))=s and y_j=c. Put D_s(y)=C_s0(y)+C_s1(y).
There are exactly M eligible triples. Write C_sc,D_s for y=X only as
proof variables, and C'_sc,D'_s for y=Z, the algorithm's actual counts.
Set alpha=3k+1. Its pre-grid vector rho is

    rho_00,1 = clip_[1/4,3/4]((C'_00,1+alpha)/(D'_00+2alpha)),
    rho_00,0 = 1-rho_00,1;
    rho_10,0 = min(3/4,(C'_10,0+alpha)/(D'_10+2alpha)),
    rho_10,1 = 1-rho_10,0;
    rho_01 = rho_11 = (1/2,1/2).

The actual predictor applies exactly §10's integer grid formulas to the
selected dirty counts and writes (out0,out1,Q) in three b+1-bit fields,
least significant bit first. Both candidate formulas can be evaluated
before selecting the terminal branch: §10 proves both are defined on
the whole independent count box. Public Q=2 selects uniform at the output.

For N=3,4,5 the actual algorithm reads exactly its N observed bits, writes
(Q/2,Q/2,Q), and clears its mutable input/scratch copies. It instantiates
no m,M, prefix, count table or fictitious sixth observation.

For the proof only, define the clean add-one comparator a_s by

    a_00,1 = clip_[1/4,3/4]((C_00,1+1)/(D_00+2)),
    a_00,0 = 1-a_00,1;
    a_10,0 = min(3/4,(C_10,0+1)/(D_10+2)),
    a_10,1 = 1-a_10,0;
    a_01 = a_11 = (1/2,1/2).

Its actual-terminal risk is R_N=E KL(p_(S_N)||a_(S_N)); for N<6 its
comparison output is uniform. Sections 2-7 prove directly

    R_N <= 1000000/N.                                   (C1.1)

In §§2-7, V denotes a centered count, p a local successor probability,
and R the reverse kernel, distinct from observed Z, true scalar r and
pre-grid vector rho. Put g=N-m when N>=6. All clean quantities in §§2-9
remain unavailable to the algorithm.

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

For finite laws mu,nu put TV(mu,nu)=1/2 sum_h |mu(h)-nu(h)|.
The positive and negative parts of mu-nu have equal mass TV, so TV is
also the supremum of absolute probability differences over events.

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
integer d_vis=floor(B/16). Since floor z>=z/2 for z>=1,

    d_vis>=B/32>=M/128, d_vis>=1,
    Pr(D_10<d_vis) <= exp(-M/256).                            (C1.17)

Here d_vis<=B/16=Bp/2, so (C1.15) applies. These are proof thresholds, not
inputs or event labels given to the predictor.

### 5.2 Martingale variance

Fix a row s and one chosen successor, with true probability p. Put
C=C_s,c, D=D_s and V=C-pD. For i=2,...,m-1 its increment is
1{S_i=s}(1{X_(i+1)=c}-p). The row indicator is measurable before the
successor is sampled, so the increment's conditional mean is zero and
conditional second moment is p(1-p)1{S_i=s}. For i<j, conditioning the
product on information through X_j makes its expectation zero. Summing
these identities at the deterministic horizon yields

    E V^2=p(1-p) E D,       E D=M pi_s.                   (C1.18)

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
integer d_vis>=1,

    {D>=d_vis, C<p*d_vis/2} subset {B_s(d_vis)<p*d_vis/2}.

The latter involves exactly d_vis iid bits. Their exponential moment, by the
same calculation as (C1.15), gives

    Pr(D>=d_vis,C<p*d_vis/2) <= exp(-p*d_vis/8).                        (C1.19)

The random visit count D can depend on the used stack. We never assert
that C conditional on D is binomial; such an assertion would in general
be false. (C1.18) and (C1.19) serve separate purposes.

## 6. Stationary-prefix row risks with explicit constants

### 6.1 Rare row00, interior successor

Set x=Mu and V=C_00,1-tD_00. Projection onto [1/4,3/4] cannot increase
distance to t in that interval. For the projected estimate q, q(1-q)>=3/16.
Writing v=(C+1)/(D+2), we have v-t=(V+1-2t)/(D+2). By (C1.6),
(A+B)^2<=2A^2+2B^2 and |1-2t|<=1,

    kl(t,q)<=12(V^2+1)/(D+2)^2,       E V^2<=x/4.          (C1.20)

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

Let p=r, C=C_10,0, D=D_10, v=(C+1)/(D+2), q=min(v,3/4) and V=C-pD.
For v>=p the derivative of (p-v)^2/v is 1-p^2/v^2>=0. Whenever clipping
occurs, v>3/4>p, so clipping cannot increase this ratio. Since 1-q>=1/4,
(C1.6) and (C1.18) give

    kl(p,q)<=8(V^2+1)/[(D+2)(C+1)],     E V^2<=pM.         (C1.22)

For M>=64 choose d_vis from (C1.17), and partition all paths into

    G={D>=d_vis,C>=p*d_vis/2}, H={D>=d_vis,C<p*d_vis/2}, J={D<d_vis}.

On G, (C1.22) and E[V^2;G]<=E V^2 yield

    E[loss;G] <=8(pM+1)/[d_vis max(1,p*d_vis/2)]
              <=16M/d_vis^2+8/d_vis <=263168/M.                  (C1.23)

For H a logarithmic loss bound is needed. For 0<q<=3/4,

    kl(p,q)<=p log_+(p/q)+4q,  log_+(z)=max(0,log z).     (C1.24)

Indeed drop the nonpositive (1-p)log(1-p), and bound
-(1-p)log(1-q)<=-log(1-q)<=q/(1-q)<=4q. On H,

    q>=1/(M+2),   q<=v<=(p*d_vis/2+1)/(d_vis+2)<=p/2+1/d_vis.

Also (M+2)/d_vis<=256. With y=p*d_vis and (C1.19), this proves

    E[loss;H]
      <=[y log_+(256y)+2y+4] exp(-y/8)/d_vis <=108/d_vis
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

For N=3,4,5 the comparison output is uniform and every binary KL
loss to uniform is at most log2 < 1000000/N. This proves (C1.1) for
every N>=3, without invoking a zero or negative prefix length.

## 8. Pathwise separate count/row perturbations and clipping domination

Fix an arbitrary clean binary input X_1^N and an arbitrary legal private
seed omega. A changed symbol at i can affect only triples ending at
i,i+1,i+2, intersected with 3,...,m. Their union has at most 3k windows.
On each affected window, each fixed triple indicator changes by at most
one, and each fixed row indicator changes by at most one. Each unaffected
indicator agrees. Summing each type of indicator separately gives

    |C'_sc-C_sc| <= 3k,       |D'_s-D_s| <= 3k.            (P1)

The row bound is direct, not the sum of two coordinate bounds. This holds
even when the dirty prefix endpoint changes or edits depend on S_N. It
concerns each input and seed, not an average edit budget.

For v_sc=(C_sc+1)/(D_s+2) and v'_sc=(C'_sc+alpha)/(D'_s+2alpha),
(P1) and alpha=3k+1 imply

    C'_sc+alpha >= C_sc+1,
    D'_s+2alpha <= D_s+9k+2,
    v'_sc >= gamma_s v_sc,
    gamma_s=(D_s+2)/(D_s+9k+2) in (0,1].                 (P2)

This common multiplicative bound holds for both coordinates. Clipping
preserves it: for 0<=l<=h<=1 let f(x)=min(h,max(l,x)). If 0<gamma<=1,

    max(l,gamma*y) >= gamma*max(l,y),
    min(h,gamma*a) >= gamma*min(h,a)  for a>=0.

Thus f(gamma*y)>=gamma*f(y) for y>=0, and x>=gamma*y implies
f(x)>=gamma*f(y) by monotonicity. Also
1-f(x)=clip_[1-h,1-l](1-x), so applying the same argument to the other
raw coordinate proves simultaneous domination of both coordinates after
clipping. For row00 use [1/4,3/4] on coordinate1, and for row10 use
[0,3/4] on coordinate0. Both resulting coordinates remain strictly positive.
Consequently, for s=00,10 and each clean input and channel seed,

    rho_sc >= gamma_s a_sc,  c=0,1,
    KL(p_s||rho_s)-KL(p_s||a_s)
      = sum_c p_sc log(a_sc/rho_sc)
      <= log(1/gamma_s)=log(1+9k/(D_s+2)).                (P3)

Rows01,11 have zero loss. The right side depends only on clean counts,
with no channel randomness remaining. Apply (P3) with the actual s=S_N
before averaging. At k=0, alpha=1 and X=Z, so rho=a exactly before the
grid; no visit-tail restriction is needed for its zero added term.

## 9. Reciprocal visits and actual terminal weighting

For k>=1 the public domain forces M>=1024, so both clean visit estimates
(C1.16)-(C1.17), proved in §5.1, apply. Set x=Mu. Since 1/(D+2)<=1/2,
splitting on the good visit event yields

    E_stat[1/(D_00+2)]
      <= 128/(x+256)+(1/2)exp(-x/512)
      <= 512/(1+x).                                    (P4)

After multiplication by 1+x, the first term is at most 128 and the
second at most (1+512/e)/2, whose sum is less than 257. This includes
x<1. Similarly d_vis>=M/128 and
{D_10<M/128} is contained in {D_10<d_vis}, so

    E_stat[1/(D_10+2)]
      <= 128/(M+256)+(1/2)exp(-M/256)
      <= 512/(M+1).                                    (P5)

The multiplied terms sum to at most 128+(1+256/e)/2<193. These are
unconditional stationary-prefix expectations under the true D1 source;
no law for corrupted counts has been asserted.

The whole-prefix bridge (C1.12) and bounded-function inequality (C1.9)
apply to these clean reciprocals, with range [0,1/2], giving

    E[1/(D_00+2)|S_N=00] <= 512/(1+Mu)+d_g/2,
    E[1/(D_10+2)|S_N=10] <= 512/(M+1)+d_g/2,              (P6)
    d_g=(31/32)^floor((N-m)/3).

The bridge is applied to the true entire prefix only after the channel
has been eliminated from the pathwise bound. It is not applied to Z,
channel randomness, or an independent replacement query.

For N>=12, floor((N-m)/3)>=N/12: use N-m>=N/2 and
N/6-1>=N/12. Hence d_g<=exp(-N/384)<=384/N. For 6<=N<12, the
same bound follows from d_g<=1. Also, for every N>=6,

    M+1>=N/4,    u/(1+Mu)<=1/(M+1),
    w<1/3,      u+w=(1+2u)/3<1/2.

Weight (P6) by the actual stationary probabilities u and w from §3:

    sum_(s=00,10) pi_s E[1/(D_s+2)|S_N=s]
      <= 512u/(1+Mu)+512w/(M+1)+(u+w)d_g/2
      <= 8192/(3N)+96/N.                               (P7)

Finally log(1+z)<=z, (P3), (C1.1) and (P7) imply

    R_av(rho) <= 1000000/N+9k*(8192/3+96)/N
              = 1000000/N+25440 k/N.                   (P8)

For k=0, use rho=a and (C1.1) directly. Thus (P8) covers all N>=6 and
public k without applying large-M lemmas to small M. The channel can be
any globally legal randomized D2 rule: (P1)-(P3) hold for each seed, and
the source-only inequalities survive averaging. The source-independence
and no-future conditions of D2 are retained throughout.

## 10. Exact positive grid, independent closed counts and all corners

For N>=6 write C0,C1 for the selected dirty row counts. In this arithmetic
argument allow them to vary independently over the integers in [0,M],
with sum possibly 2M. Define

    D=C0+C1+2alpha,        Zden=4D.

This D is the smoothed selected denominator, unlike D_s in §§1-9. Since
alpha>=1, k<=M/1024 and m=M+2, the entire independent box obeys

    2<=D<=2M+6k+2<=3m,
    Zden<=12m,            2Zden<=24m.                    (G1)

Indeed 2M+6M/1024+2<=3M+6. Moreover, for c=0,1,
0<4(Cc+alpha)<Zden because the other smoothed count is positive.

The row00 candidate is exactly

    z1=min(3D,max(D,4(C1+alpha))),
    J=floor((2Q*z1+Zden)/(2Zden)),
    q00=(Q-J,J)/Q.                                      (G2)

This is nearest-integer rounding of Q*rho_00,1 with half ties upward.
For dyadic Q>=4, Q/4 and 3Q/4 are integers. As z1/Zden is in [1/4,3/4],
J is in [Q/4,3Q/4] and

    |J/Q-rho_00,1|<=1/(2Q).                              (G3)

Thus both output numerators are positive. At Q=4 the internal thresholds
are 3/8 and 5/8; equality returns 1/2 and 3/4 respectively. The interval
endpoints remain 1/4 and 3/4. This includes every tie, regardless of whether
a particular pair of counts realizes the threshold.

The row10 candidate is exactly

    z0=min(3D,4(C0+alpha)),  z1=Zden-z0,
    j_c=floor(((Q-1)*z_c+Zden-1)/Zden)
       =ceil((Q-1)*z_c/Zden),  c=0,1,
    e=Q-j0-j1,             q10=(j0,j1+e)/Q.              (G4)

Q-1 and Zden-1 subtract literal 1, not alpha. Both z_c lie strictly between
0 and Zden. The two pre-ceiling quantities sum to the integer Q-1. If they
are integers, their ceiling sum is Q-1; otherwise their nonzero fractional
parts sum to 1, so their ceiling sum is Q. Hence e belongs to {0,1},
j0,j1>=1, and j0+j1<=Q. Both final numerators are in [1,Q-1] and sum
to Q. Exact divisibility, nonzero remainders and zero residual are covered.
For both coordinates,

    q10_c >= (1-1/Q)*rho_10,c.                            (G5)

Rows01,11 use uniform, as does public Q=2. At Q=2 the eagerly evaluated
row00 candidate can have J=2 and Q-J=0, but J remains in [1,2] and every
division/subtraction is defined. The final uniform selection discards it
and returns (1,1)/2. Row10 at Q=2 has j0=j1=1 and e=0. No logarithm or
loss of an unused zero-coordinate candidate is evaluated by the algorithm.

If C0=C1=0, both pre-grid rows are uniform: (G2) returns J=Q/2, while
in (G4) each ceiling of (Q-1)/2 is Q/2 since Q is even, and e=0. Thus
both return uniform. With only one zero count, alpha>0 keeps all smoothed
coordinates positive; the preceding proofs apply without an exception.

All eagerly evaluated candidates obey these whole-box integer guards,
including Q=2 and uniform terminal branches:

    0<z1_(nearest)<=3D,
    nearfull=2Q*z1_(nearest)<=6QD,
    nearnum=2Q*z1_(nearest)+Zden <=(6Q+4)D
            <=8QD<=24mQ<32mQ,
    0<z_c_(ceiling)<Zden,
    ceilnum_c=(Q-1)*z_c_(ceiling)+Zden-1
              <Q*Zden<=12mQ.                           (G6)

Every divisor is positive; Q-J, Zden-z0, Q-1, Zden-1 and e are
nonnegative. Exact division's remainder is below 2Zden for the nearest
candidate and below Zden for each ceiling. Thus (G2)-(G4) define a finite
integer function on every independent closed count pair, without an
appeal to realizability or modular-overflow conventions. Products are
full integers; C3's finite-width/physical cost construction is separate.
The selected final numerators sum to Q and lie in [1,Q-1]. Each, and the
literal denominator Q, fits b+1 bits, giving the specified 3(b+1)-bit port.
After these writes, erasing every other mutable cell is a deterministic
finite continuation and supplies no clean side input.

## 11. Grid loss transfer and the required upper

For Q>=4 and row00, set p=t, v=rho_00,1 and q=J/Q. All lie in
[1/4,3/4]. The Bernoulli bounds (C1.6)-(C1.7), (G3) and the square
triangle bound yield, for each individual history and channel seed,

    kl(p,q) <= (16/3)(p-q)^2
            <= (32/3)(p-v)^2+8/(3Q^2)
            <= (16/3)kl(p,v)+8/(3Q^2).                  (G7)

For row10, coordinate domination (G5) yields

    KL(p_10||q10) <= KL(p_10||rho_10)-log(1-1/Q)
                  <= KL(p_10||rho_10)+2/Q,              (G8)

using -log(1-z)<=z/(1-z)<=2z for 0<=z<=1/2. Rows01,11 have zero loss.
Nonnegativity of KL permits the common multiplier 16/3. Average these
pathwise inequalities over the actual terminal query, source and channel
coins, without making the terminal pair independent of any count. With
(P8) and the loose sum of the two grid remainders,

    R_av(A,T;u,t)
      <= (16/3)R_av(rho)+8/(3Q^2)+2/Q
      <= 16000000/(3N)+135680 k/N+3/Q,                   (G9)

because (16/3)*25440=135680 and 8/(3Q^2)+2/Q<=3/Q for Q>=4.
At Q=2 the actual output is uniform, with
KL(p_s||uniform)<=log2<3/2=3/Q, so (T) follows without (G7).
For N=3,4,5 the genuine uniform no-prefix branch has loss at most log2,
which is less than 16000000/(3N), proving (T) for every public Q and
k=0 in that branch. No statistical padding to N=6 is used.

One parameter-free deterministic family therefore satisfies (T) for
all stated parameters and admissible channels. Every use of stationarity,
reverse conditioning, visits or martingales concerns X only. Corruption
enters only through the deterministic per-seed window bound. Clean counts
and the comparator remain proof variables. This proves precisely the
selected C1 claim, subject to the normal independent truth-gateway verdict.

## Appendix P. Fixed sources, not proof predecessors

- current project; `PROBLEM.md`; SHA256 `960299dbb9730b6f8b7d9de81128fabcca03b7342a456beb57572e52d490caca`; D1-D7, exact C1.
- responsibility instructions; `inputs/AUTONOMOUS_RESEARCH.md`; SHA256 `e21e211cfda567f2f5bdca8b5bc7bd42fd59527938bc1ec77d5e50ff22003424`; scope and execution.
- Prover stage4; `inputs/source-stage4/outputs/001-relative-code/prover/c1-proof-v2.md`; SHA256 `f8f6a56b4b458ff3d0033fa8cd29d27e3e32067dd643c2a9e51ba411ed6dadcf`; clean proof and elementary inequalities §§1-7.
- Prover probe012; `inputs/source-stage4/outputs/012-input-contamination/prover/upper-program-certificate-v1.md`; SHA256 `b1a0de75230bb5ec2cd58417e09f2c0bb3ca7818e2fd513c6e0333f81b7beab4`; pollution, reciprocal, grid §§1-4.
