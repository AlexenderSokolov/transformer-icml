# S024 固定计数阈值选择器 完整科学证明

编排说明（非原文）：本副本保留完整科学证明或完整科学审查推理；省略身份控制、私有位置、原提交状态、重复管理表及执行记录。原件未改，复制字节不改写。精确复制／删略／新增区间、原件全文身份见 COPY_MAP.json；原章节号及审查所引行号沿用原件，按同名章节与公式定位。SOURCES.md 给准确科学版本和可读闭包。有限检查仅为补充证据，不是形式验证；本次装配没有重做数学审查。

历史阶段限定：S024 v1 已接纳，但只证明 Ω_row 的 1472 r_closed 适应；其中 §9 的 NEXT 仅是当时尚未证明的充分候选。它现已被 S025 §2 的合法 IID 反例否定，并不是当前下一义务；其原字节在下文完整保留。S024 接纳定理和同一阈值 64 的算法未被否定。全原始 Ω_closed 的闭合来自本包 S025，不追溯归于 S024。

## 0. Main result and exact scope

There is one deterministic predictor, with inputs only K, M and the actual
complete observed history, that simultaneously preserves the general and
IID rates and attains the original-row-optimal closed-region rates:

    general arbitrary source:                  risk <= min(1,49g),
    IID table, arbitrary initial pair:          risk <= min(1,858i),
    stationary initialization, any table:       risk <= min(1,176a),
    arbitrary initialization under condition B: risk <= min(1,337a),
    arbitrary initialization, beta >= 1/2:      risk <= min(1,337a),
    arbitrary initialization, S019 strip:       risk <= min(1,1472H).

Here n=M+1, a=min(1,sqrt(K^3/n)), g=min(1,sqrt(K^5/n)),
i=min(1,sqrt(K/n)), delta=1-beta, and H=max(a,delta^(M/2)). The S019
strip is exactly K>=2, 1<=M<=K^4, 0<=beta<=1/2. Condition B is S011's
exact h_floor(M/2)<=1/(M+1), with h_b=delta^floor(b/2) for beta<1,
and h_b=1 for b<2, h_b=0 for b>=2 at beta=1.

The one algorithm is

    J = n_(Y_M),                         original full-history row count,
    q = original terminal-row add-one,
    b = pooled add-one from X_3,...,X_(M+2),
    T(H) = min{g, 64 sqrt(K/(J+K))},
    A(H) = b if TV(q,b)<=T(H), and q otherwise.                 (ALG)

The constant 64 and the rule are fixed for every source and every beta.
Neither a, beta, delta, h, H, a stationary law, a class label nor a hidden
regeneration label is read by the algorithm. Although a is public from K,M,
it is used only to state the analysis.

The nontrivial new bridge is an IID rejected-error bound at the *random
original terminal count*:

    E[ TV(q,p) 1{TV(q,p)>32 sqrt(K/(J+K))} ] <= i               (TAIL)

when M>=5 and n>K (the other finite cases use the loss cap). Its proof
uses an exponential conditional-multinomial tail on S022's analysis-only
three disjoint-triple groups, followed by a pathwise weighted comparison.
The remainder is bounded by

    72 exp(-4K) sqrt(K^3/n) <= i,

not merely exp(-cK). Thus fixed K and arbitrarily large M are covered.
No IID tail is asserted for beta<1.

The second new bridge bounds the expected count radius, not row noise.
It inherits S001's stationary occupancy and S018's exact full-symbol-history
split construction. No stack union over M and no logarithmic confidence
radius is used. This makes the new guard preserve a and H while the S022
guard alone only gave a pathwise additive g.

The precise matched extension is described in Section 8. The noncapped
near-IID region delta<a remains unresolved for this predictor; the all-beta
337a bound at strong beta is not relabeled as the smaller F rate.

## 1. Experiment, inputs, and frozen dependencies

Fix integers K>=2, M>=1, alphabet {0,...,K-1}. A source is a fixed homogeneous
second-order table theta, with legal pair transitions
P((a,b),(b,c))=theta_ab(c). Zero edges and sparse stationary laws are allowed.
The initial pair law mu is arbitrary unless explicitly declared stationary.
Observe exactly X_1,...,X_(M+2), and set

    Y_j=(X_(j+1),X_(j+2)), 0<=j<=M,
    C_s(c)=sum_(j=0)^(M-1) 1{Y_j=s, X_(j+3)=c},
    n_s=sum_c C_s(c),       J=n_(Y_M),
    q(c)=(C_(Y_M)(c)+1)/(J+K),
    b(c)=(sum_(j=3)^(M+2) 1{X_j=c}+1)/(M+K).

Exactly M departures are observed. The target is theta_(Y_M), for the
unobserved X_(M+3), and loss is TV(A,theta_(Y_M))=||A-theta_(Y_M)||_1/2.
The algorithm uses the entire original q and b. The shortened or partitioned
counts appearing below are auxiliary analysis objects only.

D_2(beta) consists of (theta,mu) for which some hidden stationary pi obeys
P^2(s,t)>=beta*pi(t) for all s,t, including off-support starting states.
The current algorithm does not read this beta. For each fixed K,M it is
one history-to-simplex map before any source supremum or beta comparison.
Both q and b are normalized probability vectors; their denominators are
positive. T(H)>0 and may be capped by g=1. Ties select b.

Direct accepted scientific interfaces:

1. **S022**, `beta_blind_endpoint_diagnostic_v1.md`, fully accepted
   by its independent full review:
   the fixed-g selector A0=b when TV(q,b)<=g and A0=q otherwise satisfies
   general risk <=49g and IID arbitrary-mu risk <=853i. Also E TV(q,p)^2
   <=min(1,423K^3/n) under IID. Only A0's IID upper is needed in the new
   rejection comparison. S022 Sections 3-4 supply the exact disjoint-triple
   law and pathwise restoration, restated with all indices below.
2. **L1MAX statistical interface** (also explicitly bound in S022): the
   original q has general risk <=min(1,48g). **S005/S022:** the pooled
   add-one b has IID arbitrary-mu mean risk <=(3/2)i.
3. **S001**, Sections 1 and 3: original q under a stationary initial pair
   has risk <=48a. For every stationary length-L pair path, L>=1, its
   actual terminal prior-visit count J_L obeys

       P_pi(J_L<w)<=min(1,K^2 w/(L+1)), integer w>=1.          (SO)

4. **S011**, Lemma 1, Proposition 3 and Corollary 4: TV(mu P^b,pi)<=h_b;
   under B the unchanged original q has risk <=min(1,81a); for beta>=1/2,
   B holds when M>=32. These are arbitrary-mu original-rule statements,
   not stationarity transferred without proof. The public minimax scale
   on its closed regimes is F=max(i,min(delta,a)), with lower F/180.
5. **S018**, Lemma 2: the exact complete-symbol-history auxiliary pair
   split has first-success label tau with P(tau=j)=beta*delta^(j-1),
   P(tau=infinity)=delta^floor(M/2). Conditional only on tau=j, the actual
   suffix (Y_(2j),...,Y_M) has the ordinary stationary P-path law, and
   its terminal count is no larger than the full J. This includes the
   legal observed midpoints; it is not merely an even-skeleton equality.
6. **S019**: in exactly its displayed strip, the unchanged q has risk
   <=min(1,128H), with common minimax lower 2^-18 H.

S003's existing eta-blind adaptation remains inherited, not a new result.
The stationary S001 result is not assigned to an arbitrary-mu D_2 class;
Sections 6-7 provide the actual burn/split bridges. No S021 failure is used
as a statistical lower bound. No external literature result is needed.

## 2. A conditional multinomial excess-tail bound

For m>=0, let V_1,...,V_m be IID p and let

    z_m(c)=(sum_l 1{V_l=c}+1)/(m+K),
    E_m=TV(z_m,p),           r_m=sqrt(K/(m+K)).

Then

    E[E_m 1{E_m>3r_m}] <=4 r_m exp(-4K).                       (2.1)

This is a deterministic-m sample statement, not a claim about the original
count J conditioned on its value.

**Proof.** At m=0, r_m=1 and E_m<=1, so the left side is zero. For m>=1,
write z_m as the mixture of the empirical vector and uniform vector. The
multinomial coordinate variances and L1/L2 Cauchy-Schwarz give

    E E_m <=sqrt(Km)/(2(m+K))+K/(m+K) <=(3/2)r_m.              (2.2)

Changing one sample changes E_m by at most 1/(m+K), by the triangle
inequality for TV. Here is the required bounded-differences calculation.
The Doob martingale obtained by revealing the m independent variables has,
conditional on every preceding prefix, each increment in an interval of
length at most 1/(m+K). To see this, average over the same remaining
independent variables after two choices of the current sample; the
pointwise function difference is at most that length. Centering does not
change the interval length.

For a bounded random variable W with interval length d, the log-MGF of
W-EW has second derivative equal to a tilted variance, at most d^2/4.
Its value and first derivative at zero vanish; integrating twice proves
E exp(lambda(W-EW))<=exp(lambda^2 d^2/8), also conditionally on a prefix.
Iterating the conditional bounds along the martingale and optimizing
exponential Markov therefore yields

    P(E_m-E E_m > x) <=exp(-2x^2(m+K)^2/m), x>=0.             (2.3)

Everything has finite support, so the differentiations and conditioning
are legitimate even when p has zero coordinates.

Put c_m=(m+K)^2/m and r=r_m. From (2.2)-(2.3), for y>=0,

    P(E_m>3r+y)<=exp(-2c_m(3r/2+y)^2).

Layer cake for E_m 1{E_m>3r}, followed by
(3r/2+y)^2 >=9r^2/4+3ry, gives

    E[E_m 1{E_m>3r}]
       <=exp(-(9/2)c_m r^2) [3r+1/(6c_m r)]
       <=4r exp(-4K),

because c_m r^2=K(m+K)/m>=K and
1/(6c_m r)<=r/(6K)<=r/12. The formula remains an upper bound when
3r>=1, in which case the actual tail is empty. This proves (2.1).

## 3. IID count-dependent rejection tail at the actual endpoint

Assume theta_s=p for every row and arbitrary mu. By S005/S022 the full law
is mu(x_1,x_2) times product_(j=3)^(M+2) p(x_j), including zero coordinates
and off-support starts. In particular only the transition outputs, not the
initial symbols, are declared IID.

For M>=5 define exactly the S022 interior and its residue groups:

    I={2,...,M-3}, I_r={j in I:j congruent r mod 3}, r=0,1,2,
    L_r=|I_r|, L_*=floor((M-4)/3),
    N_s^r=sum_(j in I_r)1{Y_j=s},
    C_s^r(c)=sum_(j in I_r)1{Y_j=s,X_(j+3)=c},
    q_s^r=(C_s^r+1)/(N_s^r+K),
    S_s=sum_r N_s^r, q_s^o=(sum_r C_s^r+3)/(S_s+3K),
    w_s^r=(N_s^r+K)/(S_s+3K).

The interior uses X_3,...,X_M, independent of the actual endpoint
Y_M=(X_(M+1),X_(M+2)), whose mass at s=(a,b) is w_s=p(a)p(b).
Within one residue group the triples are IID p tensor p tensor p. For a
fixed row s, conditional on all first-two-coordinate pairs in that group,
the selected third coordinates are IID p. Thus N_s^r~Bin(L_r,w_s), and
conditional on N_s^r=m the output counts are Multinomial(m,p). Different
residue groups can overlap and are not claimed independent.

Put e=TV(q,p), e_s^r=TV(q_s^r,p) and u_s=sqrt(K/(S_s+K)). The exact
convex combination q_s^o=sum_r w_s^r q_s^r is valid pathwise. Precisely
four departures 0,1,M-2,M-1 were omitted, so n_s=S_s+d_s with 0<=d_s<=4.
S022's deterministic restoration (adding these departures and replacing
three priors by the one original prior) gives

    TV(p_s^+,q_s^o)<=4K/(S_s+K)<=4u_s.                       (3.1)

Define the excess parts

    Z_s=sum_r w_s^r e_s^r 1{e_s^r>3sqrt(K/(N_s^r+K))}.

By Cauchy-Schwarz on the three nonnegative numbers sqrt(N_s^r+K),

    sum_r w_s^r 3sqrt(K/(N_s^r+K))
       <=3sqrt(3K/(S_s+3K)) <=3sqrt(3)u_s.

Consequently, pathwise at every row,

    TV(p_s^+,p) <=(4+3sqrt(3))u_s+Z_s.                       (3.2)

Let t_s=64sqrt(K/(n_s+K)). Since n_s+K<=S_s+K+4<=3(S_s+K),

    t_s/2>=32u_s/sqrt(3)>=2(4+3sqrt(3))u_s.                  (3.3)

The last comparison is 14>=8sqrt(3), true since (7/4)^2>3. Equations
(3.2)-(3.3) imply the deterministic tail comparison

    TV(p_s^+,p)1{TV(p_s^+,p)>t_s/2} <=2Z_s.                  (3.4)

Indeed, on this event the baseline in (3.2) is at most half the error,
so Z_s is at least half the error. This step neither conditions on n_s
nor makes its count-dependent weights independent of their errors.

Drop only weights <=1 in (3.4). Using endpoint independence, the valid
conditional multinomial law, and (2.1),

    E[e 1{e>32sqrt(K/(J+K))}]
       <=8 exp(-4K) sum_r sum_s w_s E sqrt(K/(N_s^r+K)).       (3.5)

For N~Bin(L,w), the elementary finite sum gives
w E[1/(N+1)]=[1-(1-w)^(L+1)]/(L+1)<=1/(L+1) when w>0;
for w=0 the weighted term is zero. Weighted Cauchy-Schwarz therefore gives

    sum_s w_s E sqrt(K/(N_s^r+K))
       <=sqrt(K sum_s w_s E[1/(N_s^r+K)])
       <=sqrt(K^3/(L_r+1)).                                 (3.6)

All K^2 rows, including zero-mass rows, are covered. Empty groups are
covered by L_r=N_s^r=0. S022's finite horizon arithmetic gives
L_*+1>=n/9 for every M>=5. Substituting in (3.5) yields

    E[e 1{e>32sqrt(K/(J+K))}]
       <=72 exp(-4K) sqrt(K^3/n).                            (3.7)

For K>=2, the fourth positive term of the exponential series gives
exp(4K)>=(4K)^4/24=(32/3)K^4>=72K (as K^3>=8>27/4).
Thus (3.7) is at most sqrt(K/n), proving (TAIL) whenever n>K.
No rate is lost as M tends to infinity with K fixed.

## 4. General and IID guarantees of the same algorithm

For an arbitrary legal source put e=TV(q,theta_(Y_M)). On the pooled
branch, d=TV(q,b)<=g, so the selected loss is at most e+g. On the row
branch it equals e. Thus the inherited general q bound gives

    sup_(theta,mu) L_A <=min(1,49g).                           (4.1)

This is pathwise safety, with all dependence on the actual endpoint intact.

Now suppose the table is IID p and write f=TV(b,p), e=TV(q,p),
t=64sqrt(K/(J+K)). Let A0 be the accepted S022 fixed-g selector.
The new selector can differ only by rejecting pooling additionally when
d>t. Hence, pointwise,

    TV(A,p)<=TV(A0,p)+(e+f)1{d>t}.

Since d<=e+f, the elementary deterministic inequality

    (e+f)1{e+f>t}
        <=2e1{e>t/2}+2f1{f>t/2}

holds: if only one summand exceeds t/2, it dominates the other. Therefore

    E TV(A,p)<=853i+2E[e1{e>t/2}]+2E f<=858i.                 (4.2)

Here (TAIL) and E f<=(3/2)i were used when M>=5,n>K. If n<=K,
i=1 and the loss cap suffices. If M<=4, i>=sqrt(2/5)>1/2, so the cap
also suffices. Finally take min with one. These cases include K=2, M=1,
zero counts, sparse p, arbitrary initial pair, and both threshold branches.

Thus the general and IID conclusions are for exactly the same ALG, not
separate algorithms selected according to beta. The S022 second moment
was not extrapolated to a non-IID table.

## 5. Stationary terminal-count radius, without a noise union bound

Let

    r_K(j)=sqrt(K/(j+K)), j>=0.

It is nonincreasing and lies in [0,1]. For every ordinary stationary
length-L experiment, including L=0 and J_0=0,

    E_pi r_K(J_L)<=min(1,2sqrt(K^3/(L+1))).                    (5.1)

For L=0 both capped sides equal one. For L>=1 and 0<t<1, set
x=K/t^2-K. This is positive and

    {r_K(J_L)>t}={J_L<x}={J_L<ceil(x)}.

The integer w=ceil(x)>=1 satisfies w<=x+1<=K/t^2 because K>=1.
SO at this precise integer threshold, not an unproved real-threshold
version, therefore gives

    P(r_K(J_L)>t)<=min(1,K^3/((L+1)t^2)).

Integrating from zero to one yields at most min(1,2sqrt(K^3/(L+1))):
for z<1, integral_0^1 min(1,z/t^2)dt=2sqrt(z)-z; for z>=1 it is one.
This proves (5.1). It concerns only a count functional; no claim about
row noise conditional on a count was needed.

On every history the selected loss is at most the original q loss plus
64r_K(J). Thus stationary initialization, S001, and (5.1) give

    L_A<=min(1,(48+128)a)=min(1,176a).                        (5.2)

This is a new guarantee for ALG, not a new stationary rate or a replacement
of S003's eta-adaptation theorem.

## 6. Arbitrary-start burn bridge and the non-pooling F regimes

Fix any deterministic burn 0<=b0<=M-1 and L=M-b0. Its observed suffix
has the ordinary length-L experiment with initial pair law mu P^b0 and
the same actual endpoint. Its count J_suffix is <=J pathwise. Since r_K
is decreasing and bounded by one, contraction of TV under the suffix-path
kernel and (5.1) imply

    E_(theta,mu) r_K(J)
       <=min(1,2sqrt(K^3/(M-b0+1))+TV(mu P^b0,pi))
       <=min(1,2sqrt(K^3/(M-b0+1))+h_b0).                    (6.1)

This does not replace the actual estimator by a suffix. It only dominates
a decreasing full-count functional by a suffix-count functional. The
expectation comparison uses a bounded function of the *whole actual
suffix*, so endpoint dependence is retained.

Under condition B use b0=floor(M/2), which is allowed even at M=1.
Then L+1>=n/2 and h_b0<=1/n. If a<1,

    E r_K(J)<=(2sqrt(2)+1)a<4a,

because 1/n<=a. If a=1 the same 4a upper is trivial. S011 gives the
unchanged q risk <=81a under B. The pathwise guard bound gives

    L_A<=min(1,81a+64*4a)=min(1,337a).                        (6.2)

For beta>=1/2 and M>=32, S011 verifies B, including integer floors and
beta=1. If M<32 then n<=32 and a>=sqrt(8/32)=1/2, hence the cap gives
L_A<=1<=2a. Therefore (6.2) holds for every beta>=1/2 and every M>=1.

Whenever delta>=a, F=max(i,min(delta,a))=a. Consequently (6.2) is the
correct public-class F rate, without beta input, throughout the entire
strong-beta non-pooling region and throughout B with delta>=a. Under
beta>=1/2 but delta<a, (6.2) is only an a upper, not an F-adaptation claim.
The exact IID guarantee still applies independently at beta=1.

## 7. S019 H strip through the exact original-history count split

For 0<beta<1, S018's exact pair-split construction and (5.1) give

    E r_K(J) <= delta^r +sum_(j=1)^r beta delta^(j-1)
                         min(1,2sqrt(K^3/(M-2j+1))),
    r=floor(M/2).                                           (7.1)

Here is why the accepted split applies to this new functional. Conditional
only on tau=j, its suffix count has the ordinary stationary length
L_j=M-2j law; full J is at least that count. Monotonicity of r_K gives
its pathwise domination, and on no success r_K<=1. Summing those exact
label probabilities proves (7.1). No stationary-suffix claim conditional
on the prefix or observed midpoint is made. The underlying construction
retains both emitted symbols of every two-step block via its unique legal
midpoint (a,b)->(b,c)->(c,d), as in S018. The labels remain analysis-only.
For even M the last successful suffix can have L_j=0, explicitly included
in (5.1); for odd M the smallest suffix length is one.

For every 0<=beta<=1/2, in fact without requiring M<=K^4, (7.1) implies

    E r_K(J)<=min(1,21 max(a,delta^(M/2))).                   (7.2)

If beta=0 or a=1 the bound is trivial. Otherwise M>=K^3>=8, and put
h=floor(M/4), v=delta^(M/2). For j<=h, M-2j+1>=n/2, so the early sum
in (7.1) is at most 2sqrt(2)a. For j>h, use delta^(j-1)<=delta^h and
sum_(j=h+1)^r (M-2j+1)^(-1/2)<=sum_(ell=1)^M ell^(-1/2)<=2sqrt(M).
The late sum is at most

    4 beta delta^h K^(3/2)sqrt(M)
       <=4sqrt(2)a (beta M)delta^h
       <=16sqrt(2/e)a.

For the last inequality set y=beta M; h>=M/4-1 and ln(1-beta)<=-beta
show y delta^h<=exp(beta)y exp(-y/4)<=4/sqrt(e), since beta<=1/2 and
the maximum of y exp(-y/4) is 4/e. Finally

    delta^r<=sqrt(2) v

by parity and delta>=1/2. The total coefficient on H=max(a,v) is
2sqrt(2)+16sqrt(2/e)+sqrt(2)<3+16+3/2=20.5<21, using e>2.
This proves (7.2), including both parities and all short-suffix terms.

On the S019 strip its accepted original-q upper is 128H. Therefore the
same ALG satisfies

    L_A<=min(1,128H+64*21H)=min(1,1472H).                     (7.3)

No reproof of the S019 minimax order is claimed. The new conclusion is
that a single rule which is also IID-optimal and general-optimal preserves
this H guarantee. Equation (7.2) outside the strip is only a count-radius
bound; it does not assert an all-source H risk rate outside the strip.

## 8. Simultaneous matched closed subset and remaining gap

Define the following subset of the original Omega_closed, at fixed K,M:

    Omega_row = {beta=0, beta=1}
      union {0<=beta<=1/2 and M<=K^4}
      union {delta>=a and [beta>=1/2 or condition B]}.

All quantifiers include K>=2,M>=1. On this enlarged subset, ALG satisfies

    sup_(D_2(beta)) L_A <=1472 r_closed(K,M,beta),
                 simultaneously for every beta in Omega_row.  (8.1)

The r_closed benchmark is exactly the user-contract minimum of all
applicable accepted endpoint, S019 H, and S011 F scales. To check overlaps:
- The beta-zero and beta-one bounds are directly g and i, respectively.
- On the last non-pooling set F=a, and (6.2) applies. If H also applies,
  both its upper and this F upper hold for the same rule, so their minimum
  can be used without changing the algorithm.
- On the H strip any extra applicable S011 F certificate either has
  delta>=a with B/strong beta (already covered), or delta<=a. In the
  latter case delta>=1/2, so F>=1/2 and the loss cap gives risk<=2F.
  This includes the equality delta=a when only condition N is applicable.
Thus taking the smallest applicable scale does not introduce an unproved
near-IID assertion. Constants 49,858,337,1472 and 2 are all <=1472.

For the corresponding infimum-over-one-predictor adaptation ratio,

    Gamma_row(K,M)=inf_A sup_(beta in Omega_row)
                  sup_(D_2(beta)) L_A/r_closed(K,M,beta),

all denominators are positive and the accepted endpoint lower implies

    1/(32sqrt(6)) <= Gamma_row(K,M) <=1472.                    (8.2)

The lower is inherited and merely prevents a zero normalized benchmark;
no new necessary adaptation penalty is asserted. The new upper removes
any necessity for a nonconstant penalty on this larger comparison subset.

**Not completed:** the meaningful near-IID portion delta<a, where F can
be much smaller than a, is not covered by (8.1) unless the endpoint or a
trivial capped overlap above applies. Neither is all Omega_closed proved.
The algorithm uses only row and pooling candidates; its analysis does not
claim that suffix selection has been solved in every closed region.

## 9. Concrete next bridge, failed shortcuts, and stopping boundary

A precise sufficient successor is an actual-target excess-tail bound for
this same fixed rule in the remaining near-IID range. Put

    e_theta=TV(q,theta_(Y_M)),
    f_theta=TV(b,theta_(Y_M)),
    T=min(g,64sqrt(K/(J+K))).

The deterministic comparison used above gives, for every source,

    L_A <=3 E f_theta +2 E[e_theta 1{e_theta>T/2}].            (9.1)

The all-row center from S011/S006, and its arbitrary-mu martingale pooled
bound plus the add-one smoothing bias, give E f_theta<=2delta+(3/2)i
(the cap handles n<=K; for n>K, K/(M+K)<=sqrt(K/n), and the martingale
term is <=i, so the deliberately weaker 2delta+2i is also available).
For precision, a direct smoothing calculation gives <=2delta+(3/2)i:
the noise term is sqrt(KM)/(2(M+K))<=i/2 and the smoothing term
K/(M+K)<=i, while the row/center bias remains <=2delta.

It would therefore suffice to prove, uniformly for delta<=a, arbitrary mu
and all K,M,

    E[e_theta 1{e_theta>T/2}] <=C(i+delta),                    (NEXT)

with one absolute constant. This is a finite, full-history, actual-terminal
statement. The S022 IID independence and the new proof of (TAIL) do not
establish it for beta<1. It is the next bounded mathematical obligation,
not an assertion that it is true or that no other selector can work.

Specific shortcuts not used:
1. A fixed g guard has only an additive g safety budget, so S022 alone
   does not preserve the smaller a/H oracle rates.
2. Replacing the threshold by a fixed a can reject pooling on rare terminal
   rows; its IID guarantee does not follow from the available second moment.
   The count-dependent threshold is essential to the present proof.
3. exp(-cK) alone is not an O(i) error at arbitrary M. Equation (3.7)
   retains the necessary n^(-1/2) factor before comparing to i.
4. Conditional IID is used only for one disjoint-triple group at a fixed
   row. It is never assigned to the full original row count or to beta<1.
5. The bound on E r_K(J) is an occupation result, not a bound on row noise.
   It cannot by itself prove (NEXT) or near-IID F adaptation.
6. Hidden split labels are not supplied to the algorithm. S018's exact
   full-history law, including midpoints, is retained; no extra validation,
   auxiliary trajectory, future label or independent test query is added.
7. A public-beta choice of a different rule per regime would not prove
   simultaneous adaptation. ALG is fixed once from K,M and the history.

## 10. Diagnostics and source bindings

The symbolic proof is Sections 2-8. The companion
`closed_class_adaptation_check_v1.py` was executed successfully on
2026-10-29 UTC; its saved JSON reports **PASS**. It checked:

- 8,144 exact rational actual-history summary, restoration and count-tail
  inequalities, including 8,064 exhaustive binary histories and 80
  compressed periodic histories with horizons up to 10^12+1;
- 8,099 pooled branches, 45 row branches, 15 count-only rejections which
  differ from S022, and 61 nonempty row-tail events;
- 56 exact binomial excess-tail calculations (the final exponential-bound
  comparison used floating point), including m=0 and sparse p;
- 19,703 exact integer radius-event conversions;
- 100,000 finite horizon comparisons, 999 exact exponential-series
  polynomial comparisons, and 426 floating geometric-radius budgets.

The compressed cases represent genuine periodic symbol histories by exact
integer residue counts; they do not stand in for IID expectations. Large
alphabets up to K=512 and both very long horizon parities were included.
The finite diagnostics check algebra/indices and exercise new branches;
they neither prove the universal probability theorem nor independently
review it. No numerical result is a mathematical premise.

