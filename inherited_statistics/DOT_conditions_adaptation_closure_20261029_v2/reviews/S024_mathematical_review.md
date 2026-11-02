# S024 完整独立科学审查

编排说明（非原文）：本副本保留完整科学证明或完整科学审查推理；省略身份控制、私有位置、原提交状态、重复管理表及执行记录。原件未改，复制字节不改写。精确复制／删略／新增区间、原件全文身份见 COPY_MAP.json；原章节号及审查所引行号沿用原件，按同名章节与公式定位。SOURCES.md 给准确科学版本和可读闭包。有限检查仅为补充证据，不是形式验证；本次装配没有重做数学审查。

历史阶段判断：六个科学单元全部 PASS，随后接纳 S024 的精确 Ω_row 范围。文中 NEXT 及全 Ω_closed 尚未证明的叙述是当时状态；S025 后来否定 NEXT 并另证全原始并集，不能改写本审查原字节或把 NEXT 误报为 S024 已接纳引理。有限检查摘要保留其原证据性质，代码与执行记录不随包附送。

## 1. Exact accepted scope and information restriction

For all integers K>=2, M>=1, n=M+1, put

    i=min(1,sqrt(K/n)), a=min(1,sqrt(K^3/n)),
    g=min(1,sqrt(K^5/n)), delta=1-beta, H=max(a,delta^(M/2)).

From exactly X_1,...,X_(M+2), let Y_j=(X_(j+1),X_(j+2)), use departures
0,...,M-1 for the original row counts, and write J=n_(Y_M). Let q be the
original full-history terminal-row add-one and b the pooled add-one formed
from exactly the M transition outputs X_3,...,X_(M+2). The one algorithm is

    T=min(g,64sqrt(K/(J+K))),
    A=b if TV(q,b)<=T, and A=q otherwise.

Ties select b. For this same history-to-simplex map, simultaneously:

| Source / initialization domain | Accepted risk upper |
|---|---|
| Every legal homogeneous order-two table, arbitrary mu | min(1,49g) |
| All-row IID table, arbitrary mu | min(1,858i) |
| Any legal table, stationary initial pair | min(1,176a) |
| D_2(beta), arbitrary mu, exact condition B below | min(1,337a) |
| D_2(beta), arbitrary mu, every beta>=1/2 | min(1,337a) |
| D_2(beta), arbitrary mu, 0<=beta<=1/2 and M<=K^4 | min(1,1472H) |

Here D_2(beta) has the original all-starting-state two-step minorization
P^2(s,t)>=beta*pi(t) for some hidden stationary pi. At beta<1,
h_b=delta^floor(b/2); at beta=1, h_b is one for b<2 and zero for b>=2.
Condition B is exactly h_floor(M/2)<=1/(M+1).

No beta, stationary law, row table, class label, regeneration label,
independent validation trajectory or unseen next output is read by A.
Neither analysis-only deletion/striding nor burn/split suffixes replace the
actual q. All losses are unconditional expected half-L1 TV at the actual
terminal row of this same full history. The initial law is unrestricted
except in the explicitly stationary line.

Define, at fixed K,M,

    Omega_row = {0,1}
      union {0<=beta<=1/2 and M<=K^4}
      union {delta>=a and [beta>=1/2 or B]}.

Using precisely the contract's minimum r_closed of all applicable accepted
endpoint, H-strip and S011 F scales, the candidate proves

    sup_(D_2(beta)) L_A <=1472 r_closed(K,M,beta)
          for every beta in Omega_row, for the same A;

    1/(32sqrt(6)) <= Gamma_row(K,M) <=1472.

The last lower is an inherited nonzero baseline, not a new adaptation-cost
lower. No nonconstant penalty is necessary on this enlarged subset.
The nontrivial near-IID region delta<a outside its endpoint/capped overlaps,
all-Omega_closed adaptation, and the displayed NEXT tail remain **unproved
and excluded**. Stationary initialization is not silently assigned to D_2.

## 2. Six-unit independent proof audit

### Unit 1 — Exact multinomial excess tail (candidate lines 128–182)

**PASS.** For deterministic m>=1, the add-one vector is the exact mixture
of empirical and uniform vectors. Coordinate variances followed by
L1/L2 and expectation Cauchy–Schwarz give

    E E_m <=sqrt(Km)/(2(m+K))+K/(m+K) <=(3/2)r,
    r=sqrt(K/(m+K)).

The noise term is at most r/2, and the smoothing term r^2 is at most r.
Changing one independent output changes the TV loss by at most 1/(m+K).
Averaging the same remaining independent variables after two possible
current values proves the stated conditional Doob-increment range length;
this is not an assumed variance of an adaptively selected row. The bounded
range log-MGF argument is valid for each conditional finite distribution,
including zero coordinates and deterministic outputs. Iteration and
optimization give exp(-2x^2(m+K)^2/m).

Let c=(m+K)^2/m. At threshold 3r, the mean bound leaves deviation 3r/2.
The exact strict-tail layer-cake identity gives

    E[E_m 1{E_m>3r}]
      <=exp(-(9/2)c r^2) [3r+1/(6cr)]
      <=4r exp(-4K).

Indeed c r^2=K(m+K)/m>=K and 1/(6cr)<=r/(6K)<=r/12 for K>=2.
The final relaxation is in the correct direction. If 3r>=1 the actual tail
is empty; the same upper remains valid. At m=0 it is separately zero because
r=1 and TV<=1. Strict versus nonstrict atoms at the threshold cause no
layer-cake discrepancy. The lemma is not assigned to the original count J
conditioned on its value.

### Unit 2 — Actual IID endpoint tail (candidate lines 184–267)

**PASS.** The inherited IID structure is exact for every initial pair law:
only X_3,...,X_(M+2) are declared IID p, independent of the initial pair.
At M>=5, the interior indices 2,...,M-3 use only X_3,...,X_M and are
independent of the actual endpoint (X_(M+1),X_(M+2)), of mass p(a)p(b).
For each fixed residue modulo three, the triples have disjoint coordinates.
Conditioning on that group's entire list of first-two-coordinate pairs
leaves its third coordinates IID p. Thus a fixed-row selected count has the
stated Bin(L_r,w_s) law and the selected output count vector has the
Multinomial(m,p) law conditional on N_s^r=m. Cross-residue independence is
neither true in general nor used. Conditioning is never imposed on all
groups, the original selected row, or the original J.

The exact convex weights (N_s^r+K)/(S_s+3K) sum to one and reproduce the
three-prior interior vector pathwise. Exactly the four distinct departures
0,1,M-2,M-1 are restored. To check the imported deterministic restoration:
adding their d_s<=4 observations costs at most d_s/(S_s+d_s+K), while
changing one prior to three costs at most 2K/(S_s+3K). Therefore

    TV(p_s^+,q_s^o)<=(4+2K)/(S_s+K)<=4K/(S_s+K)<=4u_s,
    u_s=sqrt(K/(S_s+K)).

Deleted symbols may depend on the endpoint and on the interior; this bound
is pathwise and makes no independence claim about them.

Separate each group error into its part <=3sqrt(K/(N_s^r+K)) and its
excess part. Cauchy–Schwarz on the three square roots gives the baseline
3sqrt(3K/(S_s+3K))<=3sqrt(3)u_s. Consequently

    e_s<= (4+3sqrt(3))u_s+Z_s.

The crucial constant comparison is valid, including the smallest K:

    n_s+K<=S_s+K+4<=3(S_s+K),
    32sqrt(K/(n_s+K)) >=(32/sqrt(3))u_s
                         >=2(4+3sqrt(3))u_s.

The last inequality is equivalent to 14>=8sqrt(3), or 49>=48 after
positive rescaling/squaring. The margin is small but strictly positive;
there is no erroneous 32 versus 64 threshold substitution. On the original
row-tail event, its baseline is at most half its error, so e_s<=2Z_s.
Only after obtaining that deterministic inequality are weights bounded by
one and discarded. This legitimately avoids any dependence assumption
between random weights, counts and errors.

Endpoint independence and Unit 1 now yield

    E[e 1{e>32sqrt(K/(J+K))}]
       <=8 exp(-4K) sum_r sum_s w_s E sqrt(K/(N_s^r+K)).

Weighted Cauchy–Schwarz uses sum_s w_s=1. The exact binomial identity
w E[1/(N+1)]<=1/(L+1), together with N+K>=N+1 and K^2 rows, bounds each
group's sum by sqrt(K^3/(L_r+1)). At w=0 the weighted summand vanishes;
no null conditioning or division by w is needed. Empty groups are valid.
The finite arithmetic L_*+1>=n/9 for every M>=5 therefore gives

    72 exp(-4K) sqrt(K^3/n).

The exponential-series term (4K)^4/24=(32/3)K^4>=72K holds for every
K>=2, so this is at most sqrt(K/n). In the asserted TAIL domain n>K this
is exactly i. In particular the remainder still decays as n^(-1/2) for
fixed K and arbitrarily large M: no bare exp(-cK) term or hidden log M has
been substituted. No beta<1 IID tail is inferred.

### Unit 3 — One fixed guard, general 49g and IID 858i (lines 269–302)

**PASS.** On the pooled branch loss<=original-row loss+T<=original-row
loss+g; on the row branch its loss is the original-row loss. The inherited
original q general upper is exactly 48g in the same arbitrary-start
experiment, hence 49g and cap one. The full q is never thinned.

Relative to the accepted S022 selector A0 using threshold g, the new rule
can differ only by additionally rejecting when d=TV(q,b)>t, where
t=64sqrt(K/(J+K)). The candidate overbounds this difference by
(e+f)1{d>t}; it need not identify the difference event exactly. Since
d<=e+f, the deterministic two-summand bound is valid:

    (e+f)1{e+f>t}<=2e1{e>t/2}+2f1{f>t/2}.

If only one exceeds t/2 it dominates the other; if neither does, the left
side is zero. This also handles equality and the pooled tie convention.
All correlations between q,b,J and the test remain intact. Thus the
accepted S022 853i, Unit 2's i, and pooled mean <=3i/2 give

    853i+2i+3i=858i.

This invocation uses M>=5,n>K. For n<=K, i=1 and the loss cap suffices.
For M<=4, i>=sqrt(2/5)>1/2, again making the cap sufficient. These cases
cover small horizons, arbitrary initial symbols, zero output probabilities
and zero terminal counts. Both guarantees concern exactly the same rule.

### Unit 4 — Stationary radius and arbitrary-start burn (lines 304–374)

**PASS.** For L>=1 and 0<t<1, let x=K/t^2-K>0. Integer-valued J_L gives

    {r_K(J_L)>t}={J_L<x}={J_L<ceil(x)},
    1<=ceil(x)<=x+1<=K/t^2.

Applying S001's occupancy inequality at this actual integer threshold
proves P(r_K(J_L)>t)<=min(1,K^3/((L+1)t^2)). The scalar integral equals
2sqrt(z)-z for z<1 and one for z>=1, hence

    E_pi r_K(J_L)<=min(1,2sqrt(K^3/(L+1))).

L=0 is proved separately: J_0=0 and both capped sides equal one. Neither a
conditional row-noise law nor an occupation-mass lower bound is used.
On any history the guard adds at most 64r_K(J) to the original q loss,
so S001's 48a plus the radius budget 128a gives 176a, with all caps valid.

For deterministic burn 0<=b0<=M-1, the complete observed suffix is an
ordinary length M-b0 experiment with initial law mu P^b0 and the same
actual endpoint. Its terminal prior-visit count is at most J pathwise.
Since r_K is decreasing and belongs to [0,1], total variation contraction
through the whole suffix-path kernel gives the candidate's (6.1), with
coefficient one on TV(mu P^b0,pi). This compares a bounded count functional
of complete paths, not the risks of different estimators.

Under B, b0=floor(M/2) is legal even at M=1, L+1>=n/2, and h_b0<=1/n.
When a<1, 1/n<=a and the radius mean is at most (2sqrt(2)+1)a<4a;
when a=1 the same inequality is trivial. S011 Proposition 3 supplies the
separate original-rule 81a upper. Thus 81+64*4=337, without assigning a
suffix theorem to the original q.

For beta>=1/2, S011 Corollary 4 proves B for every M>=32, with exactly
floor(floor(M/2)/2)=floor(M/4) and the separately defined beta-one case.
At M<32, a>=1/2 and cap one supplies <=2a. The 337a upper therefore holds
for all strong beta and every M. It becomes an F-rate statement only when
delta>=a, for then F=a since i<=a. It is not an F bound when delta<a.

### Unit 5 — Full-symbol S018 split and 21H / 1472H (lines 376–427)

**PASS.** S018 Lemma 2 applies to every 0<beta<1, arbitrary mu and all-state
minorization. Its residual Q_2 is a normalized two-step pair kernel, not a
new one-step source table. For a block from (a,b) to (c,d), the unique
legal midpoint is (b,c), and both emitted symbols are retained. Marginalizing
the label gives exactly theta_ab(c)theta_bc(d); multiplying all block factors
and the possible final odd step recovers every original complete-symbol
history probability. Zero-product blocks cannot acquire mass in either
nonnegative mixture component.

Only conditioning on the first-success label tau=j yields the ordinary
stationary suffix starting at pair time 2j. S018's exact joint identity is
beta*delta^(j-1) times pi at that endpoint times the full future P-path
product. Its proof sums the preceding midpoint/prefix and leaves future
labels unconstrained. There is no claim of stationarity conditional on the
observed midpoint, complete prefix, all labels, or a row-stack event.

For the new functional r_K, full J>=suffix J pathwise and monotonicity
suffice. Partitioning by tau therefore gives (7.1) with exact no-success
mass delta^floor(M/2) and all lengths M-2j. L=0 at the last even success is
included by Unit 4; the final odd success has L=1. No auxiliary label is
revealed to A, and no rows or midpoints are omitted from the actual rule.

For 0<beta<=1/2 and a<1, integrality implies M>=K^3>=8. Taking
h=floor(M/4), the early labels have M-2j+1>=n/2 and total weight <=1,
so contribute at most 2sqrt(2)a. All late denominators are distinct positive
integers, ending at one for even M and two for odd M; their reciprocal-root
sum is at most 2sqrt(M). Thus the entire late sum is at most

    4 beta delta^h K^(3/2)sqrt(M)
       <=4sqrt(2)a (beta M)delta^h
       <=16sqrt(2/e)a.

The last step uses h>=M/4-1, log(1-beta)<=-beta, beta<=1/2, and the
maximum 4/e of y exp(-y/4), all in the claimed direction. Parity gives
no-success mass <=sqrt(2)delta^(M/2), retaining the exact power rather than
replacing it by a faster decay. The total coefficient is

    2sqrt(2)+16sqrt(2/e)+sqrt(2)<21.

Beta zero and a=1 are cap-one cases. Hence the radius bound 21H is valid
for all beta<=1/2, without requiring M<=K^4. Only on the actual S019 strip
is the separate original-q risk upper 128H available; adding 64*21H gives
128+1344=1472H there. Outside the strip (7.2) remains solely a count-radius
bound, not an unproved original-row or selected-rule H risk theorem.
No log M arises in the new radius argument. The inherited S019 risk theorem
retains its bounded-history scope, where its own logarithm was absorbed.

### Unit 6 — Exact closed-set minimum, lower quantifiers and scope (lines 429–605)

**PASS.** The benchmark is the contract's minimum, not a chosen convenient
scale. The full case check is:

1. At beta=0, the endpoint gives g. If H also applies, M<=K^4 forces g=1
   and H=1. If the S011 N condition applies at beta=0, delta=1<=a forces
   a=F=g=1. Condition B is impossible here for M>=1, and strong beta does
   not apply. Thus an additional certificate cannot create a smaller
   uncontrolled endpoint-zero denominator.
2. At beta=1, the endpoint scale is i; S011's F is also i, and no H-strip
   certificate applies. Hence r_closed=i exactly.
3. On delta>=a with B or strong beta, F=a and the same algorithm has the
   337a upper. If H also applies, its 1472H upper holds for the same rule,
   so the minimum can be taken without any beta-dependent selection.
4. On the H strip, any additional S011 F certificate is from N, B, or
   strong beta. If delta>=a and B/strong beta holds, item 3 applies. If
   delta<=a, then delta>=1/2 on the strip, so F>=1/2 and cap one gives
   risk<=2F. Equality delta=a under N alone is included. These cases
   exhaust all possible applicable F certificates on the strip.

All certificate constants are <=1472. Taking their applicable minimum is
therefore valid uniformly for the one fixed algorithm, at each fixed K,M
and simultaneously over all beta in Omega_row. This subset lies in the
contract's Omega_closed. No missing near-IID certificate is used to enlarge
it. The role of the public beta in analysis does not alter A's input list.

Every finite benchmark is strictly positive because the scales have positive
i (and a,g,H). For any one admissible possibly randomized beta-blind A,
its beta=1 worst risk is at least i/(32sqrt(6)) by the accepted full-history
IID lower. That lower uses all M+2 symbols in a legal stationary IID subclass
of the arbitrary-start class and applies to every common kernel before
infimization. Since beta=1 belongs to Omega_row and r_closed=i there, taking
the supremum over beta and then infimum over A preserves the normalized
lower 1/(32sqrt(6)). The explicit one A supplies the upper 1472. There is
no exchange of source supremum and algorithm infimum, no different rule per
beta, and no assertion of one universally hard source.

The successor comparison (9.1) itself is valid. On rejection d>T, use the
same elementary two-error split; on pooling the loss is f_theta. This gives
L_A<=3E f_theta+2E[e_theta 1{e_theta>T/2}]. S011's all-row hidden center
is valid off stationary support and under arbitrary mu. Its martingale
pooled calculation, with direct add-one smoothing, gives

    E f_theta <=2delta+sqrt(KM)/(2(M+K))+K/(M+K)
                <=2delta+(3/2)i.

For n>K, the noise inequality follows from M n<=(M+K)^2; the smoothing
inequality from K n<=(M+K)^2. At n<=K, the cap supplies the claimed weaker
right side. Thus NEXT would be a sufficient new obligation when delta<=a
because F=max(i,delta) there. **NEXT is not proved by S024 and is not
accepted by this report.** The IID conditional-law proof is unavailable
for beta<1, and an occupation-radius bound alone is not a noise tail bound.
The warnings about hidden labels, fixed-g safety, rare rows, no log M,
fixed-K large-M remainders and public-parameter selectors are accurate.
No external mathematical theorem, S021 failure, stationary-only upper or
implementation claim is silently used as an additional premise.

## 3. Source interfaces and byte identities

| Interface | Actual use and scope |
|---|---|
| S022 accepted fixed-g selector | IID arbitrary-mu 853i for A0 only; its 423K^3/n second moment is not extrapolated to beta<1 |
| L1MAX through S022's audited interface | General original-q 48g, arbitrary mu, actual terminal expected TV |
| S005 through S022's audited interface | Exact all-row IID law, pooled mean 3i/2, full-data IID lower |
| S001 §§1,3 | Original stationary-q 48a and stationary integer terminal-occupation tail |
| S011 Lemma 1, Proposition 3, Corollary 4 | Exact h_b contraction, original-rule 81a under B, all strong-beta finite specialization |
| S011 Proposition 2 / S006 Lemmas 1,5 | All-state row center and arbitrary-start pooled martingale bound; not a stationary matched theorem transferred to arbitrary mu |
| S018 Lemma 2 | Exact complete-symbol split, tau weights, conditional-only-on-tau stationary suffix, pathwise count domination |
| S019 | Original-q 128H and common-minimax lower 2^-18 H only for M<=K^4,beta<=1/2 |
| S011 / accepted endpoint lowers | Public-class rate interpretation and universal-algorithm IID floor; no new lower family |

## 4. Independent finite diagnostics

The reviewer independently wrote and executed:

- `S024_review_checker_v1.py`
  SHA-256 `5c43845734d34696b3f4ec25b39e571d9b27c9192cd7801dfd51d3bd94d58e93`.
- `S024_review_checker_v1_results.json`
  SHA-256 `5d5dde16d24a9120f4fa4e2b54d339ad9a6d3da9222414529d9179b61bba9e2f`.

The final execution completed with **PASS**. It did not read or import
the producer checker. Exact rational arithmetic was used for probability
identities, counts, tail-event decisions and deterministic comparisons;
90-digit Decimal was used only for final exponential/radical numeric
comparisons, and ordinary floating point for finite geometric sums and
final scalar overlap comparisons.

1. 34 multinomial excess-tail cases, including m=0, sparse binary/ternary
   laws, m up to 512, and nine nonempty tails. The largest tested
   tail/bound ratio was approximately 1.34e-14.
2. 350 exact joint selected-count/output-count atoms from independently
   enumerated disjoint triples, compared with the binomial–multinomial
   factorization, including empty groups and zero masses.
3. 1,920 exhaustive binary complete histories at M=5,...,8 and 264
   genuine periodic histories summarized by exact residue arithmetic,
   including K up to 512 and both parities at M=10^30 and 10^30+1.
   The compressed summaries were additionally matched against direct
   enumeration in 72 small cases.
4. 8,261 rowwise mixture/restoration/tail comparisons; 448 nonempty
   original-row-tail events; 2,069 pooled and 115 row branches, including
   33 count-only rejections relative to S022. Original data and every
   restored departure remain in these history summaries.
5. 18,368 exact integer radius-event conversions, 50,000 finite-horizon
   comparisons (including huge integer horizons), and 1,000 exact
   exponential-series polynomial comparisons.
6. 3,192 complete finite geometric-radius budgets, keeping every late
   suffix atom, both parities and zero-length cases. The largest tested
   mixture/H ratio was approximately 2.375.
7. 171 minimum-overlap cases at exact rational-square rates, including
   delta=a, N-only capped cases, beta endpoints and H/F overlaps.
8. Frozen candidate hash, all 14 listed hashes, and 18 scientific-copy
   output-span hashes verified.

These checks supplement the symbolic audit; they do not prove an infinite
family theorem, turn periodic paths into IID expectations, or independently
certify an unproved near-IID tail. In particular huge periodic histories
exercise deterministic algebra only, not a large-M stochastic-risk claim.

## 5. Assembly, errors and stopping boundary

All six contracted units close:

    deterministic multinomial concentration
      + exact IID disjoint triples / independent actual endpoint
      + pathwise random weights / four-departure restoration
        -> original count-dependent IID excess tail;

    fixed observable guard + original general bound + accepted S022
        -> simultaneous 49g / 858i;

    stationary occupation -> decreasing count-radius moment
      + full-suffix TV burn / exact full-symbol pair split
      + respective original-q risk interfaces
        -> 176a / 337a / 1472H;

    one fixed A + exact applicable-scale overlap audit
      + inherited all-common-algorithm IID lower
        -> stated Omega_row / r_closed / Gamma_row conclusions.

No mathematical error, missing domain case or required author revision was
found.
