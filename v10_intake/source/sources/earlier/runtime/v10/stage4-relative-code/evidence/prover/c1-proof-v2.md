# Stage4 C1: actual-terminal JOINT relative-integer-code upper bounds, fixed proof v2

Author: Prover stage4, 2026-10-26. Exact obligation:
`36441ab5cb65fa3d086e3d2fc5b847cff5acc127ac7ff3a8dfbf0c8137945811`.
Contract: `38d15641fecff6dbee957b6e036c052ecb7f07e6354623e800f7a126cf5270ef`.
This is a self-contained proof under the current project's D1-D4.
Submission predecessors are **[]**. Source proofs and Lead's checkpoint
are attributed construction/proof lineage, never admitted premises.
Every mathematical premise needed here is proved below. Native admission
status and the independent verdict are recorded separately after submission.

## 0. Scope and fixed provenance

Only this workspace's inputs are used for historical source material.
The minimum statistical source is Prover stage3's clean upper proof,
`inputs/source-stage3/outputs/001-conditional-grid/prover/c1-proof-v1.md`
§§1-7. Sections 2-7 below reproduce its mathematical argument, with local
visit-threshold notation clarified and the lower-bound conclusions omitted.
The relative-code argument is rederived from Prover 010 §§8-10. The causal
adapters/bit construction/output schedule are attributed to Prover stage3;
the concrete JOINT selection/snap schedule is attributed to Counter 010.
Full author/path/hash pins are in Appendix P and `c1-manifest-v2.json`.

This proof establishes only the selected C1: one program, both finite
risk bounds, clean estimator premise, actual finite acquisition, lawful
closed-box decoding and erasure. It proves no old minimax lower, C2 lower,
full Bstar coordinate bound or optimized architecture claim. Full Bstar is
the separate C3/C4 obligation. In particular the old 010 §11 assertion
that both displayed uppers are O(eta^2) along the comparison schedule is
not used: the displayed conditional total upper is Theta(eta), with only
its noise contribution O(eta^2).


This v2 repairs the actual rejected v1, whose immutable SHA256 is
`c79376878e1487cf09ecec1e7ef30c86f5ef41b3529a11ef09daf131aad9f686`.
Native failure `9384763cb5650698a5693149ced39abbeba6bfc0bb7e63059f3d3166c42e175d`
and its raw report are preserved in `c1-gateway-v1.json`. The v1 local
rename changed standalone d to d_vis but missed nine concatenated
products of p and the old visit variable. Since public d is different, the displayed tail
bound was false as written. Every such product in §§5.3/6.2 is now
explicitly p*d_vis. Appendix R independently tracks the correction
through all risk constants. There is no added mathematical premise,
changed predictor, altered source or altered quantifier. This is a
specific repaired submission, not a repeat of the unchanged proof.

## 1. Source, clean comparator and the one executable predictor

Fix public integers N>=3, b>=1, d>=6, Q=2^b and eta=2^-d. The unknown
source parameters satisfy 0<u<1/4 and 1/4<=t<=3/4. Set w=(1-u)/3,
alpha=u/w=3u/(1-u), r=alpha*t. Then 0<alpha<1, 0<r<3/4 and r>=3u/4.
For S_i=(X_(i-1),X_i), state order 00,01,10,11, the transition and
initial pair laws are

    P = [[1-t, t,   0,   0],
         [0,   0, 1/2, 1/2],
         [r, 1-r,   0,   0],
         [0,   0, 1/2, 1/2]],       pi=(u,w,w,w).

Observe exactly X_1,...,X_N; the future X_(N+1) is unavailable. The
target next-1 probabilities are (t,1/2,1-r,1/2). For a history-based
predictor q, let R_N(q)=E KL(p(.|S_N)||q), and let R_N,00(q) denote
the same expectation conditional on the actual S_N=00. These are the
contract's R_av and R_00. Logs are natural; coordinates are ordered (0,1).

For N=3,4,5 the actual program reads the N-symbol input through its input
interface, initializes its output bank and writes (Q/2,Q/2,Q). It instantiates
no prefix frontend, E_m, count computation or cut. Its predictor is uniform.

For N>=6 set m=floor(N/2), M=m-2>=1, g=N-m,

    h=ceil(log2(256(N-2))), A=2^h,
    p=4h+4ceil(log2(m+4))+64, R=2^p.

There are M sampled triples, precisely those ending at 3,...,m. Write
C_s,c for their row/successor counts and D_s=C_s,0+C_s,1. The clean
comparison predictor a_N, never supplied as post-cut data, uses row S_N:

    00: a_1=clip_[1/4,3/4]((C_00,1+1)/(D_00+2)), a_0=1-a_1;
    10: a_0=min(3/4,(C_10,0+1)/(D_10+2)), a_1=1-a_0;
    01,11: a=(1/2,1/2).

The small-N clean comparator is also uniform. In §§2-7 we prove directly

    R_N(a_N)<=1000000/N,                          (C1.1)
    R_N,00(a_N)<=160000/(1+Nu).                   (C1.2)

The attaining JOINT program, constructed in §8, forms eight paid local
triple features, obtains j_c=floor(A C_c/M) from one finite zero-score
head, and pads them with eleven explicit zero words. Its only cut data
are these nineteen (h+1)-bit words and eight protected one-hot controls
for S_N and E_m=(X_(m-1),X_m). Every other clean ancestor is overwritten
before recovery. An arbitrary D3 map returns closed integers j'_c with
|j'_c-j_c|<=floor(eta*j_c). Using only the returned selected words, the
program snaps C'_c=floor((2M j'_c+A)/(2A)), then applies the exact D4
add-one/clipping/grid formulas in §11. It never knows u,t or the map.
We prove for this same program, simultaneously, for every allowed map,

    R_av <=12000000/N+256eta^2+3/Q,
    R_00 <=1800000/(1+Nu)+256eta^2+3/Q^2.         (T)

In the following purely statistical sections, p denotes a local row
success probability, not the public finite-evaluator precision p. The
symbol d_vis denotes a visit threshold, never the public error exponent d.
The reverse kernel is denoted R there, distinguished by its matrix arguments
from the integer weight scale R=2^p in the finite program.

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
integer d_vis=floor(B/16). Since floor z>=z/2 for z>=1,

    d_vis>=B/32>=M/128, d_vis>=1,
    Pr(D_10<d_vis) <= exp(-M/256).                            (C1.17)

Here d_vis<=B/16=Bp/2, so (C1.15) applies. These are proof thresholds, not
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
integer d_vis>=1,

    {D>=d_vis, C<p*d_vis/2} subset {B_s(d_vis)<p*d_vis/2}.

The latter involves exactly d_vis iid bits. Their exponential moment, by the
same calculation as (C1.15), gives

    Pr(D>=d_vis,C<p*d_vis/2) <= exp(-p*d_vis/8).                        (C1.19)

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

For M>=64 choose d_vis from (C1.17), and partition all paths into

    G={D>=d_vis,C>=p*d_vis/2}, H={D>=d_vis,C<p*d_vis/2}, J={D<d_vis}.

On G, (C1.22) and E[Z^2;G]<=E Z^2 yield

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

## 8. Paid causal features, actual finite acquisition and erased cut

### 8.1 A concrete causal frontend

Use the one-shot batch input with n=N+1 positions. At positions 1,...,N,
store x_i=(1-X_i,X_i); at n store the constant (0,0), a synthetic query
after all observations, not a future symbol. The input bit and its
complement are explicitly read/formed. Public positions and masks are
fixed independently of the history and parameters u,t.

Four zero-score singleton heads have values x. At each historical position
i, heads 1 and 2 select i-1 and i-2 respectively, falling back to i when
the index is unavailable; heads 3 and 4 select i. At physical query n,
the selected positions are respectively m,m-1,N,N-1. All masks are
nonempty and causal. The finite singleton ratio is exactly the selected
bit: in integer A-grid form it is A times the bit, and division by A
recovers that bit exactly. Hence historical records contain the two local
lags, while the query contains the distinct E_m and S_N. Two-bit pair
one-hots are the four ANDs of the respective symbol one-hots; there are
exactly four bits per pair. These controls are computed, not supplied.

A fixed paid routing copies records 1,...,m and the physical query to
a buffer of length m+1. Its last slot retains physical time N+1; changing
the buffer address does not make a later observation visible earlier.
The original/tail banks are cleared after the needed copies. At retained
key k define, for each (i,j,c) in lexicographic order,

    V_ijc(k)=ReLU(lag2_i(k)+lag1_j(k)+x_c(k)-2).

This equals the triple indicator on bits. Alternatively two successive
ANDs give it: eight features require sixteen ANDs, with explicit fanout
copies. No pair or triple table is an input oracle. A single statistical
head with zero Q,K and eight values V has eligible query keys exactly
3,...,m. Nonquery rows, if evaluated, use keys 3 through their own prefix
position or a singleton self fallback when empty. No future key, discarded
tail or synthetic query is a sample. The four singleton heads followed by
one statistical head use five total heads, at most four simultaneous,
value width at most eight and scores zero. QK dimension one suffices for
zero scores and is within the declared bound four. The stored Boolean
masks have finite size 4n^2+(m+1)^2 and are public.

### 8.2 Exact finite weight, including acquisition intermediates

The D2 evaluator at integer score S uses T_0=R and
T_j=floor(T_(j-1)S/(jR)) for j=1,...,8p, with W(S)=sum_j T_j.
At S=0, T_j=0 for every j>=1, so W(0)=R exactly. Thus for each
feature the actual finite integer, with no intermediate sum rounding, is

    floor(A sum_(k=3)^m W(0)V_c(k)/sum_(k=3)^m W(0))
       =floor(A R C_c/(M R))=floor(A C_c/M).       (8.1)

The implementation can cancel the public common R before accumulation:
initialize eight integer accumulators to zero, visit all publicly masked
keys, add the actual feature bits, multiply each resulting sum by A and
divide by M. This computes the exact finite-head function, without a
free count input. Alternatively retain R throughout. Then denominators
are MR>0, weighted numerators <=MR and full A-weighted dividends <=AMR.
Both versions are finite and exactly equal. With ell=ceil(log2(N+2)),
ell<=h, their necessary ranges use at most p+h+ell+2 bits; B=128p is
ample even for the uncancelled version. Generating 2^p, A, zero scores,
masks and positional literals is an explicit finite write/shift process;
no log coefficient or transcendental approximation is needed at score zero.
Each j_c is in the closed range [0,A], so h+1 bits include its endpoint A.

### 8.3 Actual destructive boundary, not a clean residual path

Use disjoint frontend banks for raw input, lags/controls, features, head
accumulators/outputs, routing copies and evaluator scratch. All unassigned
locations start at zero. After computing the query summary, allocate a
fresh fixed port P and copy its eight quantized integers; explicitly write
eleven zero integers. Copy just the four one-hot bits of S_N and four
of E_m into protected port P_ctl. Do not retain an address or length
chosen from the data. Public metadata consists only of N,m,M,h,p,Q,d,
positions, masks and the fixed program.

Next execute public-bound zero-write loops over *every* other data bank:
raw histories including the tail; original/routed one-hots and lags;
all pair/triple features and unused token outputs; weighted sums,
denominators, accumulator counts, unquantized masters, clean quantized
copies; temporary product, quotient, remainder and carry registers;
old controls and any scalar/bit extraction copies. Only P and P_ctl are
excluded. Release the erased banks. Clears are actual constant writes,
not instructions to stop naming live values. No seed depending on input
exists, since this encoder and decoder are deterministic. If physical
storage is reused, first initialize it to zero. The external map overwrites
P and returns it; decoder inputs are then read only from the returned P,
P_ctl and public metadata. No internal pre-map duplicate of P survives.

The data-dependent state across this boundary is therefore exactly
19(h+1)+8 bits. Subsequent recovery can keep copies of the *returned*
words, but cannot read a clean ancestor. This holds at actual terminal
queries and for all histories. The arbitrary map's own computation is
external under D3; its predictor interface copies/reads/clears above are
real operations. We assert their existence and ranges here, not a complete
resource bound: their Bstar charges are part of the separate C3/C4 proof.

## 9. Integer channel, zero/small locks and pathwise count perturbation

For each of all nineteen slots, D3 gives 0<=j'<=A and
|j'-j|<=floor(eta*j). If j=0 or eta*j<1 then j'=j exactly. In particular
all eleven padding words and any zero-count feature are locked. For a
nonzero feature with j<2^d the code itself is also locked; this is an
integer, not continuous, radius condition. Since h may be smaller than d,
every integer below 2^min(d,h) is in this protected small range as well.

For any closed input word define

    C'=floor((2M j'+A)/(2A))=floor(Mj'/A+1/2).     (9.1)

The closed input bound proves 0<=C'<=M; at j'=A it gives C'=M.
For a clean j=floor(AC/M), 0<=C-Mj/A<M/A<=1/256. Thus if j'=j,
(9.1) recovers C exactly (including C=0); a locked small integer cannot
cause an erroneous count through quantization alone. For C=0, all of
j,j',C' are exactly zero.

For C>=1, the floor, channel and nearest-round errors give pathwise

    |C'-C| <= 1/2+(M/A)|j'-j|+M/A
            <= eta C+129/256.                   (9.2)

Here (M/A)eta*j<=eta*C, and the nominal public A schedule alone gives
M/A<=1/256. If C'!=C, integer separation is at least one; (9.2) forces
eta*C>=127/256. Substituting this back in (9.2) yields

    |C'-C| <=(256/127)eta*C<3eta*C.              (9.3)

When C'=C the weak bound |C'-C|<=3eta*C is automatic. Consequently
(9.3) as a weak inequality holds for all counts, including zero. We have
not discarded the additive half-integer rounding error: it is absorbed
only after using integrality on paths where the count actually changes.

The argument uses only the coordinatewise channel inequalities on the
particular history, so it permits arbitrary correlations between all
returned coordinates and both protected controls. For a randomized
admissible map, condition on its source-independent seed; the same
pathwise inequalities hold, and integrating preserves them. Global
admissibility is the premise; no conditional independence among errors,
counts or terminal state is needed. Mathematical clean C remains only
a comparison random variable and is not accessible after §8.3's cut.

Only the two words for protected S_N need to be snapped. To realize the
selection, decode its two bits a,beta from the protected one-hot by two
ORs. For each successor c, use three word MUXes: one selects between
rows 00/01 on beta, one between 10/11 on beta, then one between those
two on a. Use CONST A, SHL A by one to form 2A, and CONST 2M; for
each selected word use MUL(2M,j'), ADD A, DIV by 2A. This is six MUXes,
three constant/shift operations and six arithmetic operations, plus the
two ORs: seventeen operations, within the declared eighteen. All divides
have positive denominator and accept zero numerator. E_m is retained and
paid at the cut even though this decoder does not inspect it. The two
snapped counts may sum to 2M, and no sum-to-M invariant is presumed.

## 10. Add-one, clipping and a quadratic KL transfer

Write epsilon=3eta<=3/64. For either selected row, (9.3) implies

    (1-epsilon)(C_c+1)<=C'_c+1<=(1+epsilon)(C_c+1).

The positive denominator is the sum of these two add-one numerators,
so the same factors bound it relative to C_0+C_1+2. Thus each raw
probability coordinate, noisy divided by clean, lies in [L,1/L], where

    L=(1-epsilon)/(1+epsilon)>0.                 (10.1)

For positive x<=y, clipping both into a common interval [ell_0,h_0]
preserves order and cannot increase the ratio: if x is below the lower
endpoint its value increases; if y exceeds the upper endpoint its value
decreases; if both are on the same outer side the ratio becomes one.
The same check covers all boundary combinations. The operation on the
complement is clipping into [1-h_0,1-ell_0]. Applying this separately
to each coordinate proves that (10.1) remains true after common row00
clipping to [1/4,3/4], and after row10 clipping of its next-0 probability
to [0,3/4] (complement interval [1/4,1]). The actual inputs are strictly
positive and less than one, so no zero is introduced by the endpoint 0.

Let a denote the clean clipped vector from §1 and v the noisy clipped
vector before the grid; both have positive coordinates summing to one.
Then v_i/a_i is in [L,1/L]. For any target probability vector z, Jensen
on its positive support gives, by direct algebra,

    KL(z||v)-2KL(z||a)
      =sum_(z_i>0) z_i log(a_i^2/(z_i v_i))
      <=log(sum_(z_i>0) a_i^2/v_i)
      <=log(sum_i a_i^2/v_i)
      =log(1+sum_i(a_i-v_i)^2/v_i).              (10.2)

The identity uses sum a_i=sum v_i=1; it does not require z_i>0 at
every coordinate. From (10.1), |v_i-a_i|<=2epsilon*a_i/(1-epsilon)
and v_i>=L*a_i. Using log(1+x)<=x and sum a_i=1 therefore bounds
the last line by

    4epsilon^2(1+epsilon)/(1-epsilon)^3
      <=36eta^2*(67/64)/(61/64)^3 <48eta^2.      (10.3)

The coefficient is at most 36*67*4096/61^3=9879552/226981<48.
We have proved the pathwise inequality

    KL(z||v)<=2 KL(z||a)+48eta^2.                (10.4)

It is valid before any expectation or terminal conditioning, so it applies
to the true terminal target without treating the query as independent.
This is a direct simplex/Jensen calculation, with no external theorem or
old Fact as a premise. Constant rows have a=v=(1/2,1/2).

## 11. Exact positive dyadic output: all branches and all closed inputs

For N>=6 put D=C'_0+C'_1+2, Z=4D. There is no denominator ambiguity:
2<=D<=2M+2 and Z>=8 on every closed input. If Q=2 or the actual row is
01/11, the output is uniform. Otherwise Q is dyadic with Q>=4.

On row00 set z1=min(3D,max(D,4(C'_1+1))). Then v_1=z1/Z is the
clipped add-one probability in [1/4,3/4]. Set

    J=floor((2Q z1+Z)/(2Z)), output=(Q-J,J)/Q.    (11.1)

This is nearest rounding, with half-integer ties upward. Since Q/4 and
3Q/4 are integers, J belongs to [Q/4,3Q/4]; both coordinates are positive
and sum to one. Its error |J/Q-v_1| is <=1/(2Q). At Q=4 the intervals
[1/4,3/8), [3/8,5/8), [5/8,3/4] give respectively 1/4,1/2,3/4;
equality at each interior boundary rounds upward.

On row10 set z0=min(3D,4(C'_0+1)), z1=Z-z0. Then z0,z1>0,
v_i=z_i/Z, and v_0 is the upper-clipped add-one probability. Compute

    k_i=ceil((Q-1)z_i/Z)
       =floor(((Q-1)z_i+Z-1)/Z),
    e=Q-k0-k1, output=(k0,k1+e)/Q.              (11.2)

The fractions before ceiling sum to the integer Q-1. If both are
integers their ceiling sum is Q-1; otherwise their fractional parts sum
to one and the ceiling sum is Q. Thus e is exactly 1 or 0. Every k_i
is >=1 and <=Q-1, and the final numerators sum to Q; because the first
is >=1 the second is also <=Q-1. Exact divisibility, nondivisibility
and residual assignment to coordinate 1 are thereby fully specified.
In all cases output_i >=(1-1/Q)v_i.

If both counts are zero then D=2 and v=(1/2,1/2). Formula (11.1)
returns J=Q/2; in (11.2), Q is even and each ceiling is Q/2, giving
e=0. Thus both active readouts return uniform even at zero counts.
One count zero also causes no singularity, because of add-one.

The actual small-N branch in §1 bypasses the entire frontend and cut,
and directly writes the same uniform port. It does not create a synthetic
six-symbol input. For N>=6 the Q2 branch may still use the same cut;
its output is uniform independently of the returned words.

### 11.1 The fixed 41-operation output program

For completeness the D4 output schedule is reproduced here from Prover
stage3's appendix D. In this table a,beta are the two terminal bits;
`MUX flag,x,y` means x if flag is 1 and y otherwise. Inputs C0,C1 are
the selected C'_0,C'_1; the symbol d0 in the table is D above.

| No. | Result | Operation |
|---|---|---|
|1|zero|CONST 0|
|2|one|CONST 1|
|3|two|CONST 2|
|4|Q|CONST 2^b|
|5|U|SHR Q,1|
|6|publicUniform|CONST 1{N<6 or b=1}|
|7|countsum|ADD C0,C1|
|8|d0|ADD countsum,two|
|9|twod|SHL d0,1|
|10|threed|ADD twod,d0|
|11|Z|SHL d0,2|
|12|twoZ|SHL Z,1|
|13|twoQ|SHL Q,1|
|14|c1plus|ADD C1,one|
|15|raw1|SHL c1plus,2|
|16|lower1|MAX d0,raw1|
|17|z1|MIN threed,lower1|
|18|nearfull|MUL twoQ,z1|
|19|nearnum|ADD nearfull,Z|
|20|J|DIV nearnum,twoZ|
|21|near0|SUB Q,J|
|22|c0plus|ADD C0,one|
|23|raw0|SHL c0plus,2|
|24|z0ceil|MIN threed,raw0|
|25|z1ceil|SUB Z,z0ceil|
|26|Qminus|SUB Q,one|
|27|Zminus|SUB Z,one|
|28|ceilfull0|MUL Qminus,z0ceil|
|29|ceilnum0|ADD ceilfull0,Zminus|
|30|k0|DIV ceilnum0,Z|
|31|ceilfull1|MUL Qminus,z1ceil|
|32|ceilnum1|ADD ceilfull1,Zminus|
|33|k1|DIV ceilnum1,Z|
|34|ksum|ADD k0,k1|
|35|residual|SUB Q,ksum|
|36|ceil1|ADD k1,residual|
|37|selected0|MUX a,k0,near0|
|38|selected1|MUX a,ceil1,J|
|39|uniform|OR publicUniform,beta|
|40|out0|MUX uniform,U,selected0|
|41|out1|MUX uniform,U,selected1|

For N>=6 both candidate paths can be computed with fixed circuit length.
When Q=2, v_1 in [1/4,3/4]
can give J=1 or2 at the upper endpoint, but it remains an unsigned word
in [0,Q], so near0 is defined; the final uniform MUX enforces positivity.
The ceiling candidates remain positive by the preceding integer-sum
argument, also for Q=2. Thus the unused branches have no invalid divisor
or subtraction. For N<6 we use only the direct uniform branch, without
instantiating fictitious inputs to this table.

### 11.2 Closed-box ranges, full products, remainders and exact gates

All guards below hold on every nineteen-word box [0,A]^19 with valid
one-hot controls, even boxes that are not clean encoder images or are
unreachable under a particular map. Word selection picks a value in [0,A].
Its snap product is <=2MA and its dividend is <=A(2M+1); h+ell+2 bits
suffice. The public 2A needs h+2 bits, rather than the h+1 cut width.
Both selected counts are <=M. With m=M+2,

    Z=4D<=8M+8=8m-8<8m,
    2Z<16m,
    2Q z1+Z<=(3Q/2+1)Z<=2QZ<16mQ      (Q>=2),
    (Q-1)z_i+Z-1<QZ<8mQ.                       (11.3)

The last inequality uses positive integer z_i<=Z. Raw1,raw0 and all
intermediate sums are bounded by these declared ranges or by 4(M+1).
The nearest dividend uses the **16mQ** guard, not an unjustified 8mQ
guard based on clean counts. Z and 2Z are positive everywhere; the
ceiling remainder is in [0,Z), and the nearest remainder in [0,2Z).

Let vbits=b+ell+8. As m<2^ell, 16mQ<2^(b+ell+4), so all cast results
fit vbits and the declared output word O=32vbits. Frontend words use
B=128p; p>=4h+64 and ell<=h suffice for every acquisition/snap range
above. The output Q, twoQ and b-dependent literals are loaded only in
the O-domain, so unbounded b is not hidden inside a fixed B word.
The decoder does not execute a d-bit error multiplier; public d can stay
in its compact exponent descriptor. All loops have public finite bounds.

For an exact implementation, retain a full 2w-bit multiplication result
before casting, with w=B or O. Compute multiplication by selecting each
shifted partial product and ripple adding across the full 2w bits.
Division by a positive w-bit divisor uses restoring division: scan all
numerator bits from most significant to least; if the old remainder is
rho<DIVISOR, form rho_new=2rho+next_bit<2*DIVISOR in w+1 bits,
compare with the divisor, subtract once if needed, and emit the quotient
bit. The invariant 0<=remainder<DIVISOR is then preserved. Retain the
full quotient and w+1-bit trial remainder; cast only after (11.3) or the
snap range proves high bits zero. ADD retains its carry and SUB its
borrow before a range-justified cast. No overflow, modular product or
pre-division discarded remainder is allowed.

These are finite Boolean programs: ripple sum uses XOR/AND/OR gates;
comparison uses borrow and OR reduction; MUX uses two ANDs and an OR
per bit. Finite shifts and literal writes copy or set each bit explicitly.
MIN/MAX are compare-and-MUX. The full multiplication uses w iterations
of a 2w-bit add; restoring division uses 2w iterations with at most a
(w+1)-bit compare/subtract/MUX. For w>=2 the liberal bound 1024w^2
elementary bit steps and 32w+32 scratch bits per primitive covers these
constructions, operand/result copies and scratch clearing: multiplication
uses <=64w^2+64w steps and division <=256w^2+128w, below that bound.
No unit-cost arithmetic primitive is assumed.

For a real affine/ReLU implementation on exact bits, AND(x,y)=ReLU(x+y-1),
NOT(x)=ReLU(1-x), XOR(x,y)=ReLU(x-y)+ReLU(y-x), and
OR(x,y)=ReLU(x+y)-ReLU(x+y-1). The subtraction form is a nonnegative
bit and can be copied through a following ReLU. Serialize these finite
gates, giving every still-live channel explicit identity holds and every
erased channel a constant-zero row. All routing/addresses are fixed or
public-bound scans. This supplies an actual finite exact circuit without
using a nominal compiler Fact. Its full cost/hold/metadata dominance by
Bstar is deliberately left to the separate resource obligation.

Finally write out0,out1 and the literal Q as three (b+1)-bit words.
The actual output is positive and normalized on every legal returned
input; Q itself needs b+1 bits. The emitted format is **3(b+1) bits**,
not a compact b-bit next-one encoding. Each write is an explicit bit copy.

## 12. Grid risk transfer and simultaneous final bounds

Assume N>=6 and Q>=4. On row00 write q_1=J/Q and v_1 for the
noisy clipped probability. Both lie in [1/4,3/4]. The elementary KL
upper (C1.6), (x+y)^2<=2x^2+2y^2, the grid error <=1/(2Q), and
the Bernoulli lower (C1.7) give pointwise

    kl(t,q_1) <=(16/3)(t-q_1)^2
      <=(32/3)(t-v_1)^2+8/(3Q^2)
      <=(16/3)kl(t,v_1)+8/(3Q^2)
      <=(32/3)kl(t,a_1)+256eta^2+8/(3Q^2).     (12.1)

On row10, (11.2) implies q_i>=(1-1/Q)v_i for both coordinates.
For its target vector z, summing z_i log(v_i/q_i) proves

    KL(z||q)<=KL(z||v)-log(1-1/Q)
      <=2KL(z||a)+48eta^2+2/Q.                 (12.2)

Here -log(1-x)<=x/(1-x)<=2x for x=1/Q<=1/2, by integrating
1/(1-x). Rows01 and11 have exactly zero loss. These are pathwise
inequalities and hence preserve all true terminal dependence under
expectation, including correlated maps.

Use 32/3 as a common multiplier, 256 as a common noise coefficient,
and 8/(3Q^2)+2/Q<=3/Q for Q>=4. The now fully proved (C1.1) gives

    R_av(q)<=(32/3)*1000000/N+256eta^2+3/Q
            <=12000000/N+256eta^2+3/Q.

Conditional on actual S_N=00, (12.1) and the fully proved (C1.2) give

    R_00(q)<=(32/3)*160000/(1+Nu)+256eta^2+8/(3Q^2)
            <=1800000/(1+Nu)+256eta^2+3/Q^2.

If Q=2, uniform loss against any binary target is at most log2<3/4,
which is already smaller than 3/Q^2 and 3/Q. If N=3,4,5, the actual
no-cut uniform branch has the same loss cap; each stated statistical
constant alone dominates it (1+Nu<9/4). Thus (T) holds throughout the
exact parameter domain, including Q2/Q4, ties, zero counts and small N.

All definitions of the predictor use only its input history before the
cut and public N,b,d, then only the returned nineteen words/eight controls
after the cut. Unknown u,t enter the proof, never its code. A single
family has both bounds for every global D3 map, including independent-
seed randomized maps. No unproved statistical, grid, finite-program or
old-Fact predecessor remains for this C1 claim. Ordinary component
admission is not root completion and does not terminate the T1-T3 goal.

## Appendix P. Source authors and exact fixed hashes

The following are provenance records, not proof predecessors. All
historical paths are within the current workspace's `inputs/` tree.

- **Lead / stage4 contract** — `PROBLEM.md`
  SHA256 `34f29e9aa714e81bbd9c92408930d0ce38c051f92f42e1e9ebf7f8158b5a8fab`. Current obligation and scope.

- **Stage4 contract** — `inputs/STAGE_DEFINITIONS.md`
  SHA256 `1648c98212f71be946dfc8b39ab54497fbad41649bbe3fedc03296c401b8c0ca`. Definitions D1-D4; D6 physical word conventions only.

[Non-scientific operational metadata omitted.]
  SHA256 `df163b669169b0d59eb28d643b204e76e730dab6795da73e668ab22a27baa564`. Sections 1-3 and erasure interface; assembly, not an admitted premise.

- **Lead stage4** — `outputs/001-relative-code/lead/checkpoint-manifest-v1.json`
  SHA256 `74dffab4c716bd109dd6e5ce0a8af135c7d863d672a77ef2bb5acd8fc4af6c64`. Source lineage pins.

- **Prover stage3, 2026-10-25** — `inputs/source-stage3/outputs/001-conditional-grid/prover/c1-proof-v1.md`
  SHA256 `5884ffc213a0aaa950b48f881abd4519440800737485b5c3aae9d293c38fb38d`. Sections 1-7 clean upper argument; sections 2-7 reproduced with local notation changes; no minimax lower imported.

- **Prover 010, 2026-10-25** — `inputs/source-stage3/outputs/010-relative-noise-probe/prover/relative-noise-proof-v1.md`
  SHA256 `a1d49bd0a71f4bdeeaa367c5e58d1089588a959a6bf71c24cab0aa4db6c96256`. Sections 8-10 relative counts and direct grid closure, rederived here; section 11 erroneous asymptotic sentence excluded.

- **Prover stage3, 2026-10-25** — `inputs/source-stage3/outputs/001-conditional-grid/prover/c3-proof-v1.md`
  SHA256 `68dcb797dfe0e2103d2f35034311efa97d9ae496dedf4eafc67c600b34a8679c`. Section 2 singleton adapters; appendix A bit primitives and D output instruction list, reproduced/rechecked; no old admission or resource conclusion imported.

- **Counter 010, 2026-10-25** — `inputs/source-stage3/outputs/010-relative-noise-probe/counter/cost-ledger-v1.md`
  SHA256 `fe3807a72a4d2cbc12d7518296ae5f5d951f43aa9852ebd391bfb5733b1332ec`. Sections 1-3 concrete JOINT 18-operation selection/snap and erased cut; full ledger not claimed here.


## Appendix R. Repair verification and unchanged finite constants

This appendix is part of the self-contained proof, not a premise from
the failed review. Fix M>=64. Let B=floor((M-1)/2),
d_vis=floor(B/16)>=1, d_vis>=M/128, and p=r in (0,3/4).
The public integer d>=6 determining eta never enters these visit bounds.

On the proof coupling of §5.3, C=B_s(D) and nondecreasing partial sums
imply {D>=d_vis,C<p*d_vis/2} is contained in
{B_s(d_vis)<p*d_vis/2}. The latter uses exactly d_vis independent
Bernoulli(p) variables. For lambda=log 2 its exponential moment is
(1-p/2)^d_vis; exponential Markov and log 2<3/4 give

    Pr(D>=d_vis,C<p*d_vis/2)
      <=exp((log 2)*p*d_vis/2-p*d_vis/2)
      <=exp(-p*d_vis/8).

This explicitly proves the corrected (C1.19). In §6.2 define
y=p*d_vis, G={D>=d_vis,C>=y/2}, H={D>=d_vis,C<y/2},
J={D<d_vis}. The event partition uses this same y everywhere.
On G, unconditional martingale second moment gives

    E[loss;G] <=8(pM+1)/(d_vis*max(1,y/2))
      <=16M/d_vis^2+8/d_vis
      <=(16*128^2+8*128)/M=263168/M.

For H the add-one estimate obeys

    q>=1/(M+2),
    q<=v<=(p*d_vis/2+1)/(d_vis+2)<=p/2+1/d_vis.

Since (M+2)/d_vis<=256, the pointwise logarithmic loss bound of
(C1.24), times the corrected tail probability, yields

    E[loss;H]
      <=[y log_+(256y)+2y+4]exp(-y/8)/d_vis
      <=108/d_vis<=13824/M.

Indeed log_+(256y)<=8+y; the maxima of y exp(-y/8) and
y^2 exp(-y/8) are 8/e<4 and 256/e^2<64, so 40+64+4=108
suffices, including arbitrarily small y>0. The J term still uses
the distinct spaced-visit estimate Pr(D<d_vis)<=exp(-M/256)
and is <=65536/M. Thus the stationary row10 bound is

    K_10<=342528/M<=400000/(M+1) (M>=64),

because 342528*65/64=347880<400000. For M<64 the existing
deterministic loss cap log65<5 suffices without a stack threshold.
The row00 proof has no p*d_vis product and is unaffected:
K_00<=50000/(1+Mu). Applying the whole-prefix terminal bridge,
the averaged constant is bounded by

    4*(50000+400000/3)+73728 < 1000000,

while the conditional constant is <=150000+75<160000.
This reestablishes both clean bounds with the corrected visit variable.
The pointwise relative-count/Jensen/grid argument then multiplies these
constants by at most 32/3, and

    (32/3)*1000000<12000000,
    (32/3)*160000<1800000,
    (16/3)*48=256, 8/3<3.

These are exactly the final two finite bounds. Small N and Q2 remain
the direct uniform branches and do not use the corrected lemma.

For clarity, the rejected version's counterexample was N=132,M=64,
u=1/5,t=2/3,p=1/2,d_vis=1 and public d=1024. It falsely used
p*d/2=256 and exp(-p*d/8)=exp(-64). The corrected threshold is
p*d_vis/2=1/4 and its exponent is -p*d_vis/8=-1/16; the demonstrated
contradiction no longer applies. The counterexample and rejection remain
recorded, and no assertion is made that v1 itself was accepted.
