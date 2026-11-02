# Stage 4 C2: full finite FULL19 observation-law lower

Author of this self-contained stage-4 adaptation and independent mathematical
check: Counter, 2026-10-26. Original construction and argument: Prover,
2026-10-25, source010, §§2,4–7. Exact obligation:

    a287207d73eed1edaa4f7b16c5d2e17f174154036432c3655450afc6bf022359

Provenance pins, verified before writing:

* Current PROBLEM.md: SHA256
  34f29e9aa714e81bbd9c92408930d0ce38c051f92f42e1e9ebf7f8158b5a8fab.
* Current inputs/STAGE_DEFINITIONS.md, D1–D8: SHA256
  1648c98212f71be946dfc8b39ab54497fbad41649bbe3fedc03296c401b8c0ca.
* Lead stage-4 mathematical-checkpoint-v1.md: SHA256
  df163b669169b0d59eb28d643b204e76e730dab6795da73e668ab22a27baa564,
  with outputs/001-relative-code/lead/checkpoint-manifest-v1.json.
* Original Prover source at inputs/source-stage3/outputs/
  010-relative-noise-probe/prover/relative-noise-proof-v1.md: SHA256
  a1d49bd0a71f4bdeeaa367c5e58d1089588a959a6bf71c24cab0aa4db6c96256;
  author/version corroborated by its fixed-manifest-v1.json.

These are attribution and definition pins. No source native Fact, old root,
discussion PASS, main/delta review or clean statistical theorem is a premise.
All mathematical steps needed for C2 are proved below. The gateway submission
uses predecessors=[]. This file makes no C1, C3 resource or arbitrary-encoder
lower claim. The original source §11 conditional-rate error is outside this
proof and is not adopted: on the later comparison schedule the displayed
total conditional upper is Theta(eta), not O(eta²).

## 1. Statement, experiment and complete visible information

Fix an integer d>=6, eta=2^(-d), u=eta/65536=2^(-d-16), and
N=2^L with M=N/2-2 and M u²>=2^40. Put m=N/2. We construct one
public deterministic map Phi_* on the entire closed cut box, using only
public A, eta and terminal control. For every common source-independent
possibly randomized decoder of the D2 FULL19 cut, there is one
t_* in {1/4,3/4} for which, under that same map and source,

    R_00 >= 3/64,                  R_av >= 3u/64.                 (1)

The decoder may output any probability distribution on {0,1}, with
unlimited computation and knowledge of Phi_*. Positive dyadic outputs at
every Q=2^b>=2 are included. The map is fixed before the decoder and t_*.

Here is the complete experiment used in the proof. In pair-state order
00,01,10,11, set w=(1-u)/3, r=ut/w and

    P = [[1-t,t,0,0], [0,0,1/2,1/2],
         [r,1-r,0,0], [0,0,1/2,1/2]],
    pi = (u,w,w,w).

Initialize S_2=(X1,X2) from pi. Observe X1,...,XN; no future symbol is
visible. The true terminal query is S_N=(X_(N-1),X_N). The sample keys
are exactly the M triples ending at j=3,...,m; the prefix endpoint is
E_m=S_m=(X_(m-1),X_m). There is no terminal-query sample. The next-one
probabilities at states 00,01,10,11 are t,1/2,1-r,1/2. In particular,
the target on terminal event 00 is Bernoulli(t). Risks are expected
natural-log KL at the actual terminal query and its conditional version
given S_N=00. We prove stationarity below, so this event has probability u.

Retain the original public schedules, without retuning:

    h=ceil(log2(256(N-2))), A=2^h,
    p=4h+4ceil(log2(m+4))+64, R=2^p.

For query ab, P1 has score I{lag2=a}L2+I{lag1=b}L2, P2 has score
I{lag2=a}L2+I{lag1=b}L3, T has score I{lag2=b}L2, U has score 0.
P1 and P2 use values I{current=c} and I{lag2=c}, c=0,1. T uses values
I{lag1=c} and I{key ends at 3}I{lag1=c}. U uses values I{lag2=c},
I{lag1=c}, I{key ends at 3}I{lag1=c}, and I{key ends at 3}. Their
exact finite evaluator is specified and bounded in §2. In original order,
the nineteen stored integers are

    (q10,q11,v10,v11,q20,q21,v20,v21,h0,h1,h00,h01,
     alpha0,alpha1,nu0,nu1,f0,f1,rho).                         (2)

The five small slots are (h00,h01,f0,f1,rho); all other fourteen are
called bulk slots below. Each word is an integer in [0,A]. The visible
controls are eight protected one-hot bits for (S_N,E_m). All public
parameters, code, positions and masks are fixed, source-independent
metadata. No raw history, clean master, clean count, clean descendant,
extra residual or history-bearing seed survives the D3 cut. This exact
information restriction is part of the experiment; it is not a theorem
about every encoder of the same nominal capacity.

A legal map must obey, on every legal full code/control input,

    0<=j'_i<=A,        |j'_i-j_i|<=floor(eta j_i).              (3)

Coordinates and protected controls may be correlated. We shall retain
all small slots and controls exactly, while collapsing the fourteen
bulk slots on a high-probability prefix event. Initial-pair information
carried by the small slots is explicitly included in the resulting law.

## 2. Actual finite log/exp evaluator and integer-code error

Define exact rational sums

    B_q=2 sum_(k=0)^(p-1) 1/((2k+1)q^(2k+1)), q=3,2,
    L2=floor(R B_3),       L3=floor(R B_2).

For an allowed integer score S, compute with full products before division

    T0=R,
    Tj=floor(T_(j-1) S/(jR)), j=1,...,8p,
    W(S)=sum_(j=0)^(8p) Tj.

The actual stored integer for a bit value V is exactly

    j_V=floor(A sum_keys W(S_key)V_key / sum_keys W(S_key)).   (4)

There is no rounding of these sums before the displayed final division.
When S=0, Tj=0 for j>=1 and W(0)=R exactly.

To bound the evaluator rather than substitute ideal exponentials, integrate
2/(1-y²) from 0 to y. This gives
log((1+y)/(1-y))=2 sum_(k>=0)y^(2k+1)/(2k+1). At y<=1/2, the tail
after p terms is bounded by

    2 (1/2)^(2p+1)/((2p+1)(1-1/4)) <= 2^(-2p).

Thus 0<=log2-L2/R<2/R and 0<=log3-L3/R<2/R. If s*=log of the
ideal edge weight, s=S/R obeys

    0<=s<=s*<=log6<2,              s*-s<=4/R.

The recurrence underestimates s^j/j!. A floor error smaller than 1/R
at a normalized step contributes at most
(1/R) sum_(r>=0)2^r/r!<8/R to that step and its subsequent terms:
products of subsequent denominators are at least r!. There are 8p
steps, so total recurrence error is <=64p/R. For j>=9,
2^j/j!<=2^(-j): check j=9 and then use ratio 2/(j+1)<=1/2.
Consequently the Taylor tail after 8p terms is <=2^(-8p)<=1/R.
Finally exp has derivative <8 on [0,2], so the score error costs
<=32/R. For every edge,

    1<=W/R<=exp(s*)<=6,
    0<=exp(s*)-W/R<=(64p+33)/R<=100p/R=:e_w.                 (5)

In particular omega:=W(L2)/R lies in [2-e_w,2]. These are finite
one-sided inequalities for the actual L2,L3,Tj,W, with no real-arithmetic
replacement of the stored program.

For a bit-weighted average, write numerator/denominator as per-key
empirical averages. Each changes from ideal to actual by <=e_w, both
denominators are >=1, and each numerator is between 0 and its
denominator. Subtraction of the two ratios therefore costs <=2e_w.
For p>=32, 200p<=2^(p/2) (true at 32 and the right side grows faster);
our p>=4h+64 implies 200p/R<=2^(-p/2)<=1/A. The final floor in (4)
adds less than 1/A. Hence for every coordinate

    |j_V/A - ideal EMPIRICAL weighted ratio| <= 2/A.          (6)

The comparison in (6) is with the finite observed empirical sample,
not with a population mean. Flag coordinates have sharper formulas.
Let a_b=M^(-1) sum_(j=3)^m I{X_(j-2)=b}, an analysis variable and
not a retained clean register, and let K=A/M. Directly from (4),

    rho=floor(K),
    f_c=floor(K) I{X2=c},
    h0c=floor(K omega_init/[1+(omega-1)a_b]) I{X2=c},        (7)

where omega_init=omega if X1=b, and 1 otherwise. The symbol h0c
denotes h00 or h01 for c=0 or 1. The unflagged numerator in (7) has
exactly the one initial key; all denominators include every sample key.

## 3. Finite domain consequences and the empirical good event

Since M>=2^(2d+72) and M=2^(L-1)-2<2^(L-1), integer L satisfies
L>=2d+74. For these powers of two, the unchanged schedules give exactly

    h=L+8,       A=256N,       p=8L+96,
    K=A/M=512+1024/M.                                        (8)

Indeed 256(N-2) is strictly between 2^(L+7) and 2^(L+8), and
ceil(log2(m+4))=L. In particular M>1024, floor(K)=512 and

    u<=2^-22,       eta A>=2^(d+82),
    e_w<=u/1000,    1024/M<=u/1000.                          (9)

For the last inequality, 1024/M<=u²/2^30<=u 2^-52<u/1000.
For the e_w inequality, p>=16d+688; using p<=2^(p/2) for p>=16
and 100<128 gives e_w<=2^(7-p/2)<=2^(-d-26)=u/1024<u/1000.
The domain is nonempty: N=2^(2d+74) gives
M u²=2^41-2^(-2d-31)>2^40. The proof uses every N satisfying the
stated domain, rather than only that particular sequence.

For a triple c=(i,j,k), let F_c=C_c/M be its empirical frequency
on keys 3,...,m. Its stationary mean, in lexicographic order, is

    mu_t=(u(1-t),ut,w/2,w/2,ut,w-ut,w/2,w/2).                 (10)

This follows by multiplying the initial pair probability by its
one-step transition probability. Define the analysis-only event

    G_t={max_c |F_c-mu_(t,c)|<=u/1000}.                      (11)

The map below does not calculate G_t or use u or t. The public reference
triple vector is

    F0=(0,0,1/6,1/6,0,1/3,1/6,1/6).                         (12)

It is a reference for deterministic ratios, not a zero-u source used
as a witness. For t in {1/4,3/4}, direct coordinate subtraction gives
||mu_t-F0||_1=2u(1+t). Thus on G_t,

    ||F-F0||_1<=8u/1000+2u(1+t)<=3.508u<4u.                (13)

## 4. One global map and collapse of all fourteen bulk slots

At query 00 the ideal weights for a triple (i,j,k) are
(1+I{i=0})(1+I{j=0}) for P1,
(1+I{i=0})(1+2I{j=0}) for P2,
1+I{i=0} for T, and 1 for U. Evaluation at F0 gives the fourteen
bulk ratios in original relative order:

    z=(3/10,7/10,2/5,3/5, 1/4,3/4,1/3,2/3,
       1/4,3/4, 1/3,2/3,1/3,2/3).                         (14)

Here is an explicit check of every group; displayed numerators are
unnormalized weighted averages at F0:

| Head | Denominator | Current 0,1 numerators | Lag2 0,1 numerators | Lag1 0,1 numerators |
| --- | --- | --- | --- | --- |
| P1 | 5/3 | 1/2,7/6 | 2/3,1 | — |
| P2 | 2 | 1/2,3/2 | 2/3,4/3 | — |
| T | 4/3 | — | — | 1/3,1 |
| U | 1 | — | 1/3,2/3 | 1/3,2/3 |

Index the bulk slots by (q10,q11,v10,v11,q20,q21,v20,v21,h0,h1,
alpha0,alpha1,nu0,nu1). Put k_i=floor(A z_i). Define Phi_* on
EVERY integer vector in [0,A]^19 and valid protected controls as follows.
If the terminal control equals 00, for each of these fourteen slots set

    j'_i=k_i if |k_i-j_i|<=floor(eta j_i),
    j'_i=j_i otherwise.                                    (15)

Retain the five small slots, every protected control, and all words in
other terminal rows. Invalid one-hot controls, if included in a larger
bit box, may simply be assigned the identity map. Because every k_i is
in [0,A], (15) proves the all-input closed-box constraint (3) directly.
This deterministic rule uses only public A,eta, fixed rationals and
the cut/control input. It is independent of t, the decoder, the true
history and G_t. In fact u is not used in its construction either.

On G_t every one of its fourteen guards succeeds. To prove this, for
fixed ideal weights in [1,6] both numerator and denominator change
by at most 6||F-F0||_1. Denominators are >=1 and normalized numerators
are <=1; subtracting ratios gives a bound 12||F-F0||_1<48u. This
covers all fourteen values, including complementary values and U.
Using (6),

    |j_i-Az_i|<=48uA+2,
    |j_i-k_i|<=48uA+3,
    j_i/A>=1/4-48u-2/A>=1/8.                               (16)

The last step follows from 48u<=1/16 and 2/A<=1/16, both much
weaker than our domain. Since u=eta/65536 and eta A>=2^(d+82),

    48uA+3<=eta A/8-1<=floor(eta j_i).                      (17)

For the first inequality, move constants to obtain
4<=(1/8-48/65536)eta A=(509/4096)eta A, which holds by (9).
For the second, use j_i>=A/8 and floor(x)>=x-1. Thus (15)
really sends ALL fourteen bulk coordinates to the fixed integer k_i
on G_t. No coordinate redundancy or self-normalizer remains outside
this analysis.

## 5. Exact five small integers and the complete endpoint code

We now keep, rather than round away, all the information in (7).
At query 00, b=0 and
a_0=sum_(j,k) F_(0,j,k). Its stationary mean is
u+w=(1+2u)/3, so on G_t

    |a_0-(1+2u)/3|<=4u/1000.

Write D_T=1+(omega-1)a_0, where 2-e_w<=omega<=2. Since
0<=a_0<=1 and e_w<=u/1000,

    4/3+(66/100)u < D_T < 4/3+(671/1000)u.                  (18)

Explicitly the lower coefficient is at least
2/3-4/1000-1/1000=397/600>66/100, and the upper coefficient is
2/3+4/1000<671/1000. These strict inequalities concern the actual
finite omega, not its limiting value 2.

When X1=1, omega_init=1. With 512<=K<=512+u/1000, (18) gives

    383 < K/D_T < 384.                                     (19)

For the upper bound, 512+u/1000<384(4/3+.66u).
For the lower bound, 512>383(4/3+.671u) follows from
383*.671u<4/3, using u<=2^-22.
When X1=0, omega_init=omega, and

    767 < K omega/D_T < 768.                               (20)

For the lower bound,
512(2-u/1000)>767(4/3+.671u) is equivalent to
(.512+767*.671)u<4/3; its coefficient is <516, so (9) suffices.
For the upper bound,
2(512+u/1000)<768(4/3+.66u). All the decimal coefficients here
are terminating exact rationals, not numerical approximations.

Equations (7)–(9),(19),(20) therefore give the EXACT unchanged integers

    rho=512,            (f0,f1)=512 e_(X2),
    (h00,h01)=383 e_(X2) if X1=1,
               767 e_(X2) if X1=0.                          (21)

Here e_0=(1,0), e_1=(0,1). In particular the initial pair S_2 is
recoverable from the small slots. Replacing 383/767 by 384/768 would
be incorrect for these positive-u finite witnesses. Some small slots
are locked by (3); our map leaves them unchanged for every d and input.

For s=(x1,x2) and e a prefix pair, define T(s,e) to be the full
visible code consisting of all nineteen words (2): bulk words k in
their original positions, the five small words (21), terminal one-hot
00, prefix one-hot e, and the unchanged public metadata. This is a
deterministic common map for both witness t values. For the exact
query-00 encoder followed by Phi_*, on G_t its ENTIRE output equals

    T(S_2,E_m).                                            (22)

Equation (22) is not a constant-code claim. Both the revealed initial
pair and the protected prefix endpoint are retained jointly, along
with every small slot and both protected controls.

## 6. Mixing, overlapping triples and the reverse whole-prefix bridge

All assertions in this section are for the actual stationary pair chain.
For the present parameters, 0<r<3/4, t>=1/4 and 1-r>=1/4. Directly,
the incoming masses to 00,01,10,11 under pi are

    u(1-t)+wr=u,   ut+w(1-r)=w,   (w+w)/2=w,   (w+w)/2=w.

Thus pi P=pi. All pi entries are positive. Three-step paths to 01
from each starting pair have probabilities

    00->01->10->01: t(1-r)/2 >=1/32,
    01->11->10->01: (1-r)/4  >=1/16,
    10->01->10->01: (1-r)^2/2>=1/32,
    11->11->10->01: (1-r)/4  >=1/16.

Hence every row of P^3 contains the common atom (1/32) delta_01.
Subtracting it expresses P^3 as that constant kernel plus beta times
a Markov kernel, beta=31/32. With TV defined as supremum over events,
any Markov kernel contracts TV: for a signed difference of two laws,
integrating a function between 0 and 1 is bounded by its TV. Iteration
and stationarity give, for every pair s and k>=0,

    TV(P^k(s,.),pi)<=D_k:=beta^floor(k/3).                    (23)

The stationary reverse kernel P_rev(i,j)=pi_j P(j,i)/pi_i has rows

    00 ->00:1-t,10:t;
    01 ->00:r,10:1-r;
    10 ->01:1/2,11:1/2;
    11 ->01:1/2,11:1/2.

This is P conjugated by exchanging labels 01 and 10; pi is unchanged
by that exchange. Therefore P_rev^3 has common atom 10 of mass 1/32,
and TV(P_rev^k(s,.),pi)<=D_k. This proves the reverse estimate
without assuming detailed balance.

For a fixed triple c let Y_j be its indicator at key j. Define
g_c(s) as the conditional mean of the triple indicator on one next
transition from pair s. It lies in [0,1] and pi g_c=mu_(t,c).
For l>=1, the Markov property applied after time j yields

    E[Y_(j+l)|X1,...,Xj]=(P^(l-1)g_c)(S_j).

Its difference from mu_(t,c) is at most D_(l-1) by (23). Multiplying
by Y_j and taking expectations proves
|Cov(Y_j,Y_(j+l))|<=D_(l-1). This explicitly includes l=1 and l=2,
where the triples overlap; no independent-sample reduction occurs.
Since Var(Y_j)<=1 and

    sum_(l>=1)D_(l-1)=3/(1-beta)=96,

expanding the variance of the M-key average gives

    Var(F_c)<= [1+2 sum_(l>=1)D_(l-1)]/M
             =193/M<=200/M.                                 (24)

Chebyshev on each coordinate at threshold u/1000 and a union bound
over all eight triple coordinates imply

    Pr_t(G_t^c)<=1600000000/(M u²)
                <=1600000000/2^40<1/32.                     (25)

This probability concerns the true random prefix under its stationary
law. It is not conditioned on the random visit counts.

Let g=N-m=M+2. Reversing the stationary path, conditional on S_N=s,
the pair at m is drawn from P_rev^g(s,.), and then the entire earlier
pair path is drawn with the same reverse-transition kernel. Under the
unconditional stationary prefix, S_m instead has law pi and the very
same earlier-path kernel is used. Applying contraction to this common
kernel and reconstructing X1,...,Xm from the consistent pair path gives

    TV(Law_t(X1^m|S_N=s),Law_t(X1^m))<=D_g.                  (26)

This is one bound for the WHOLE prefix, including every count, flag,
initial pair and E_m jointly. It does not condition a good event
separately or divide an unconditional error by Pr(S_N=s)=u.

For the two endpoints under the unconditional stationary prefix,

    Pr_t(S_2=s,E_m=e)=pi_s P^M(s,e).

Using (23) and averaging the row TV distances gives

    TV(Law_t(S_2,E_m),pi tensor pi)<=D_M.                    (27)

This is a comparison to a product law, not an assertion of true
independence. The two endpoints remain dependent in the actual law.
Both D_M and D_g are <1/32: M>=480 and floor(M/3)>=160, while
(32/31)^32>1+32/31>2 implies beta^160<1/32. The given domain
is vastly stronger than this last numerical threshold.

## 7. One common reference law for the actual full conditional cut

For analysis only, let K_00(X1^m) be the deterministic map which
evaluates the actual finite FULL19 prefix encoder at query 00, applies
Phi_*, includes E_m, terminal control 00 and public metadata. Under
the real event S_N=00, this is exactly what the decoder observes.
Applying this mathematical function to an unconditional prefix below
is only a comparison of laws; it supplies no extra input to any decoder.

Let L_t be the actual conditional visible-code law under source t and
Phi_*, given S_N=00. First apply (26) to the entire function K_00:

    TV(L_t, Law_t(K_00(X1^m)))<=D_g.

Next couple K_00(X1^m) with T(S_2,E_m) on that same unconditional
prefix. By (22) these random objects are equal on G_t, so

    TV(Law_t(K_00(X1^m)),Law_t(T(S_2,E_m)))<=Pr_t(G_t^c).

Finally apply (27) through T. Define the common reference law

    Pi=T_*(pi tensor pi).

It is the same for t=1/4 and t=3/4 because pi depends only on their
shared u, and T depends only on the fixed public k and the exact flags.
It retains all nineteen integers, initial-pair information, protected
E_m and S_N, and all public metadata. Triangle inequality gives

    TV(L_t,Pi)<=D_g+Pr_t(G_t^c)+D_M<3/32,
    TV(L_(1/4),L_(3/4))<3/16.                               (28)

The coupling step does not require G_t independent of either endpoint.
The true terminal dependence is paid exactly once in (26). In particular,
we have not replaced a dependent history/terminal experiment by independent
queries, dropped locked small slots, or used population aliases as the
actual encoded observation law.

## 8. All randomized post-cut decoders, and the same witness for both risks

Let any allowed decoder be fixed. Its private randomness is independent
of source/history before conditioning on the visible cut. Thus it defines
one common Markov kernel from the complete visible code to a binary
probability distribution q=(1-q1,q1). Applying it to both conditional
laws contracts TV. Threshold q1 at 1/2: choose t_+=3/4 when q1>=1/2,
and t_-=1/4 otherwise. A testing mistake under either source implies
|q1-t|>=1/4.

For completeness the Bernoulli Pinsker inequality used here is elementary:
for fixed t in (0,1),

    d/dq kl(t,q)=(q-t)/(q(1-q)).

Integrating from t to q and using q(1-q)<=1/4, in either direction,
gives kl(t,q)>=2(t-q)². If q=0 or 1 the loss is infinite for our
interior t. Thus on a testing mistake the conditional prediction loss
is at least 1/8.

If a(z) in [0,1] is the probability that any such randomized test
chooses t_+ on visible observation z, its two error probabilities obey

    err_-+err_+
      =1-[integral a dL_+ - integral a dL_-]
      >=1-TV(L_-,L_+).                                     (29)

The displayed inequality for functions in [0,1] follows by integrating
their level sets, so it covers arbitrary private randomization. Applying
the loss bound on mistakes and (28),(29) yields

    max_(t in{1/4,3/4}) R_00(t,Phi_*,decoder)
      >=(err_-+err_+)/16
      >=(1-TV(L_-,L_+))/16
      >13/256>3/64.                                        (30)

Select a t_* attaining that two-element maximum (infinite losses cause
no difficulty). By stationarity on that SAME source, Pr(S_N=00)=u,
and all other query losses are nonnegative. Therefore

    R_av(t_*,Phi_*,decoder)
      >=u R_00(t_*,Phi_*,decoder)>=3u/64.                    (31)

Equations (30),(31) prove (1) with the same t_* and the map fixed
independently of both decoder and t. Nothing here assumes failure of a
particular readout; it proves a full observation-law lower for every
common randomized decoder of this exact frozen FULL19 encoder.

Because (15) is defined and admissible on the whole nineteen-word/control
box, precisely the same function can be applied to the JOINT interface.
In particular a zero word cannot pass a nonzero replacement guard. This
is global legality, not an information lower for JOINT or arbitrary
re-encoders. Alternative encoders, resource comparisons and the later
C3/C4 composition remain separate obligations. [Non-scientific operational metadata omitted.]
tasks and settings are unchanged. QED.
