# S025 完整独立科学审查

编排说明（非原文）：本副本保留完整科学证明或完整科学审查推理；省略身份控制、私有位置、原提交状态、重复管理表及执行记录。原件未改，复制字节不改写。精确复制／删略／新增区间、原件全文身份见 COPY_MAP.json；原章节号及审查所引行号沿用原件，按同名章节与公式定位。SOURCES.md 给准确科学版本和可读闭包。有限检查仅为补充证据，不是形式验证；本次装配没有重做数学审查。

当前判断：七单元全部 PASS，随后最终接纳 S025。审查确认原 Ω_closed 与全部适用尺度最小值，不偷换为较小并集；同一个算法、任意初始律和完整实际终点实验均保留。原 NEXT 真反例完整保留；其否定不推翻 S024 的已接纳定理。有限诊断摘要不是形式证明。

## 1. Exact accepted statements and unchanged experiment

For integers K>=2, M>=1, write n=M+1 and

    i=min(1,sqrt(K/n)), a=min(1,sqrt(K^3/n)),
    g=min(1,sqrt(K^5/n)), delta=1-beta.

The source is a fixed legal homogeneous second-order table, with pair kernel
P((a,b),(b,c))=theta_ab(c), arbitrary initial pair law mu, and an existential
hidden stationary pi satisfying P^2(s,t)>=beta*pi(t) for every s,t. All
M+2 symbols X_1,...,X_(M+2) are observed, exactly departures 0,...,M-1 are
counted, and the target is theta_(Y_M) for the unobserved X_(M+3), where
Y_j=(X_(j+1),X_(j+2)). Loss is unconditional expected half-L1 TV at this
actual terminal pair, not an independent-query or squared-TV target.

Let q be the original full-history terminal-row add-one, J its original
terminal-row count, and b the pooled add-one from exactly X_3,...,X_(M+2).
The single algorithm, identical to accepted S024, is

    t=64sqrt(K/(J+K)), T=min(g,t),
    A=b if TV(q,b)<=T, and A=q otherwise.

Ties select b. This is one deterministic history-to-simplex map fixed from
K,M before any source supremum or comparison of beta values. It reads no
beta, source table, initial law, stationary law, class label, refresh label,
auxiliary sample, unseen next symbol or coupled reference. No suffix or
thinned rule silently replaces either actual count vector.

For this SAME A, S025 proves throughout the complete finite domain

    sup_(D_2(beta)) E TV(A,theta_(Y_M))
       <=min(1,1308delta+(7715/2)i)
       <=min(1,4000(delta+i)).                                (NI)

Define h_b=delta^floor(b/2) for beta<1, and at beta=1 define it as one for
b<2 and zero for b>=2. Put N={delta<=a}, B={h_floor(M/2)<=1/n},
H=max(a,delta^(M/2)), F=max(i,min(delta,a)). The exact original union is

    Omega_closed={beta=0 or beta=1}
       union {0<=beta<=1/2 and M<=K^4}
       union {N or B or beta>=1/2}.

At every fixed K,M,beta in this union, r_closed is the minimum of ALL
applicable scales: g at beta=0; i at beta=1; H in the stated S019 strip;
and F on N, B or beta>=1/2. Combining NI with accepted S024 proves

    sup_(D_2(beta)) L_A <=8000 r_closed(K,M,beta)
       simultaneously for every beta in Omega_closed,
    1/(32sqrt(6)) <= Gamma(K,M) <=8000.

Gamma has the contract's infimum over ONE common beta-blind predictor,
then supremum over beta in this union and the source class, normalized by
r_closed. Thus no nonconstant adaptation penalty is necessary on precisely
this union. This does not assert a sharp numerical constant, estimation of
beta, all-public-certificate oracle adaptation, or Goal A's full joint
minimax/original-rule characterization. A rule need not actually select a
suffix to attain every matched scale in the specified comparison family.

## 2. Seven-unit mathematical audit

### Unit 1 — Genuine full-IID countersequence to NEXT (lines 108–138)

**PASS.** For even m>=32, K=m^2, M=m^3, d=K/4 is an integer. Taking p
uniform on d symbols, every theta row equal to p, and mu=p tensor p gives
a legal stationary member of D_2(1). All M+2 symbols, including the initial
pair, are IID p. For j<=M-2 the compared pairs have disjoint coordinates,
and their equality probability is 1/d^2. For j=M-1 equality forces three
successive symbols to agree and has probability d*(1/d)^3=1/d^2 as well.
Thus E J=M/d^2=16/m and P(J=0)>=1-16/m.

On J=0, q is uniform on all K symbols, e_theta=3/4, g=1, t=64, and T=1.
Consequently the proposed S024 NEXT left side is at least
(3/4)(1-16/m)>=3/8 while i<=m^(-1/2) tends to zero and delta=0.
No absolute C can make NEXT<=C(i+delta). This is a full-data counterfamily,
not a lower bound manufactured by deleting initial information.

The counterexample does NOT refute any accepted S024 theorem or ALG. At
g=1, the g test alone cannot reject pooling because TV(q,b)<=1. The
candidate correctly rejects only the unproved sufficient successor.

### Unit 2 — IID-reference threshold 20 (lines 140–186)

**PASS.** The imported MT is a deterministic-m smoothed-multinomial excess
tail, not a conditional law of an original selected count. Its S024 proof
uses the mean <=3r/2, independent-sample sensitivity 1/(m+K), the conditional
Doob range/MGF bound, and a valid strict-tail layer-cake integral to obtain
4r exp(-4K), including m=0 and sparse laws. That actual proof and its full
independent review were read.

For M>=5, the interior indices 2,...,M-3 use only X_3,...,X_M under the
IID-reference law. The terminal pair uses the two independent final IID
symbols. Within each single residue modulo three the triples are disjoint;
conditional selected output counts at a fixed row really are multinomial.
Different residue groups are not independent and need not be. Empty groups
are allowed. The exact weights (N_s^r+K)/(N_s+3K) reproduce the three-prior
interior vector pathwise; dropping them only after deterministic domination
does not assume independence between a weight and its error.

Restoring all four omitted departures and replacing three priors by one
costs at most (4+2K)/(N_s+K)<=4K/(N_s+K)<=4u_s. Together with the three
local radii this gives baseline (4+3sqrt(3))u_s. Since
J_s^0+K<=N_s+K+4<=3(N_s+K), this baseline is at most
(9+4sqrt(3))r_s^0<16r_s^0. On e_s^0>20r_s^0 it is less than 4e_s^0/5,
so e_s^0<=5Z_s. The weaker threshold 20 therefore remains valid.

Endpoint averaging, weight removal and MT give the factor 20exp(-4K).
For N~Bin(L,w), w E[1/(N+1)]<=1/(L+1), with zero weighted contribution
when w=0. Weighted Cauchy–Schwarz over all K^2 rows gives
sqrt(K^3/(L_r+1)). The smallest residue satisfies L_*+1>=n/9, yielding

    E[e_0 1{e_0>20r_0}] <=180exp(-4K)sqrt(K^3/n)
                         <=(5/2)i<=3i.

The final comparison uses exp(4K)>=(4K)^4/24>=72K for K>=2 and n>K.
The n^(-1/2) factor is retained even at fixed K and arbitrarily large M.
No IID claim is assigned to the original non-IID source.

### Unit 3 — Exact innovation coupling and clean actual endpoint (188–226)

**PASS.** The unique legal two-step path gives the product identity
P^2((a,b),(c,d))=theta_ab(c)theta_bc(d). Summing the all-state minorization
over d yields theta_ab(c)>=(1-delta)p(c), p(c)=sum_d pi(c,d), for EVERY
row, including off-support initial states and zero p coordinates.
For delta>0 the residual is nonnegative and has total one. For delta=0
all rows equal p and the arbitrary residual is never used.

Drawing the initial pair, independent B_t~Bernoulli(delta), independent
V_t~p and independent residual draws, then choosing V_t when B_t=0 and
R_(current row) otherwise, gives exactly theta as the conditional symbol
law. Multiplying conditional factors recovers every complete original
history probability, with the table fixed along a trajectory. The reference
has precisely mu(z_1,z_2) product_(t>=3)p(z_t), not a stationary-IID initial
pair unless mu happened to be that law.

The event E={B_(M+1)=B_(M+2)=0} costs at most 2delta outside. On E, the
actual endpoint is (V_(M+1),V_(M+2)); that pair is independent of all
innovations and initial data through time M and has law w_s=p(a)p(b).
E is independent of the entire reference, even though the reference full
counts themselves depend on its endpoint. These are distinct independence
claims and both are valid. At delta=1 E is empty; the proof multiplies by
1_E and never conditions on a null event. The arbitrary initial pair is
retained exactly in both histories.

### Unit 4 — Clipped weighted edits with dependent contamination (228–306)

**PASS.** Marking an interior departure if any of its three B labels is one
ensures agreement of unmarked triples. Each marked departure contributes
two units to sum_s D_s, even if the actual and reference row agree.
Each B_t can mark at most three departures, giving

    sum_s D_s=2|C|<=6 sum_(t=3)^M B_t,
    E sum_s D_s<=6Mdelta.

D_s and N_s can be highly dependent. The proof does not multiply their
expectations. Choose one deterministic largest residue of size L>=1.
Its IID row count N_s^* is Bin(L,w_s), N_s>=N_s^*, L+1>=n/9,
L>=n/18, and M/L<=18. If Lw_s<=K, then w_s/(N_s+K)<=1/L. If Lw_s>K
but N_s^*>=Lw_s/2, the ratio is <=2/L. Thus the ENTIRE weighted
contamination contribution on these good cases is pathwise at most
(2/L)sum_s D_s, even when which rows are good is random. Its expectation
is at most 216delta. This is the crucial lawful cancellation.

On the remaining cases the clip supplies at most the row weight. For
N~Bin(L,w), exponential Markov at log 2 gives
P(N<Lw/2)<=exp(-Lw/8); log 2<3/4 follows from the positive series for
exp(3/4). Hence the bad contribution is bounded by

    B=sum_(Lw_s>K) w_s exp(-Lw_s/8).

Both subsequent bounds are needed:

- If n<=K^3, B<=exp(-K/8)<=3/K<=3i.
- If n>K^3, x exp(-x/8)<=8/e<3 gives B<3K^2/L<=54K^2/n<=54i.

The last inequality in the second branch is equivalent to n>=K^3. The
first branch uses i>=1/K. The elementary maximum and 8/e<3 are valid
(e>1+1+1/2+1/6=8/3). Thus no nondecaying exp(-cK) remainder survives at
fixed K with unbounded M.

For the +8 allowance, the same exact binomial identity and N_s>=N_s^*
give sum_s w_s E[1/(N_s+K)]<=min(1/K,K^2/(L+1)). Applying
min(x,y)<=sqrt(xy) gives <=sqrt(K/(L+1))<=3i. Therefore its contribution
is <=24i. The inequality min(1,x+y)<=min(1,x)+y completes

    sum_s w_s E rho_s<=216delta+78i.

All K^2 rows are retained; zero weights vanish without division. The
budget depends only on data/innovations through M. Unit 3 therefore gives
E[1_E rho_(Y_M)]=(1-delta)^2 sum_s w_s E rho_s. This concerns the SAME
actual endpoint on E, not a newly substituted independent prediction query.

### Unit 5 — Original full counts, CT and active-only GT (308–390)

**PASS.** At each row, the interior L1 count-vector difference is bounded
by D_s. Exactly the four distinct departures 0,1,M-2,M-1 were omitted
from each history; their two count vectors have combined L1 mass at most
eight. Therefore both the full vector difference and total-count difference
are <=D_s+8. All initial and terminal boundary data remain in the actual
algorithm. No independence of any boundary departure is required.

For positive vectors u,v with totals A,B, the candidate's normalization
identity gives L1 difference <=(||u-v||_1+|A-B|)/B. Applied to full
add-one counts, B=J_s^0+K>=N_s+K, so

    TV(q_s,q_s^0)<=rho_s,
    n_s+K<=(1+W_s)(J_s^0+K).

On E the rows coincide, and theta_s is within delta of p. Hence
e<=e_0+W+delta. The CT split is valid:

1. If W>1/4, then 4rho>=1>=e.
2. If W<=1/4 and W+delta>=e/4, then e<=4rho+4delta.
3. Otherwise e_0>3e/4. On e>32sqrt(K/(J+K)), the count comparison gives
   e_0>48r_0/sqrt(5)>20r_0 and e<(4/3)e_0.

Thus the pathwise transfer (6.4) holds. Charging E^c by 2delta, applying
CE, and using the IID-reference IT20 yields

    4(216delta+78i)+4delta+2delta+(4/3)*3i
        =870delta+316i.                                    (CT)

For GT, g<1 implies n>K^5 and g=sqrt(K^5/n), i=sqrt(K/n). The split at
W+delta=e/2 is valid even for W>1 because 2rho>=2>=e. Otherwise e_0>e/2,
and on e>g/2 one has e_0>g/4. The accepted full-reference IID second
moment, with its arbitrary initial pair and all restored departures, gives

    E[e_0 1{e_0>g/4}]<=(4/g)E e_0^2
       <=1692K^3/(ng)=1692i.

The other costs give 2(216delta+78i)+4delta+3384i
=436delta+3540i. This is asserted ONLY when g<1. Unit 1 shows why an
unrestricted g=1 version would be false. No original-source conditional
multinomial law, non-IID second moment, or unconditional endpoint/count
independence enters either transfer.

### Unit 6 — Actual observable rejection, NI and complete finite domain (392–441)

**PASS.** The pooled bound is a genuine dependent-path martingale argument.
With F_j generated by X_1,...,X_(j+2), D_j=e_(X_(j+3))-theta_(Y_j) has
conditional mean zero, E||D_j||_2^2<=1 and orthogonal cross terms.
L1/L2 followed by expectation Cauchy–Schwarz bounds the smoothed noise by
sqrt(KM)/(2(M+K)); smoothing costs at most K/(M+K); the average row and
actual target row are each within delta of p. Thus

    E f<=2delta+sqrt(KM)/(2(M+K))+K/(M+K)
        <=2delta+(3/2)i.

For n>K the last comparisons follow from Mn<=(M+K)^2 and
Kn<=(M+K)^2. For n<=K the loss cap suffices. No IID law is used here.

The new deterministic selector bound SEL is valid with all ties. Pooling
has loss f. If a rejected path has e<=f, f already dominates. Otherwise
e>f and d<=e+f<2e. Rejection means d>min(t,g), equivalently d>t OR d>g.
The latter alternative is impossible at g=1. Therefore

    loss<=f+e1{e>t/2}+1{g<1}e1{e>g/2}.

This restriction to an actual rejected path repairs NEXT without changing
the algorithm. Since t/2=32sqrt(K/(J+K)), CT applies, and GT applies only
where included. Adding the three budgets gives exactly

    1308delta+(7715/2)i <=4000(delta+i).

At g=1 omitting GT only improves the result. If n<=K then i=1. If M<=4
then i>=sqrt(2/5)>1/2. In either case the cap proves NI without an interior
independence assertion at a nonexistent interior. Finally cap one and
uniformity permit the source supremum. This includes K=2, M=1, both
parities, zero counts, sparse p, off-support starts, beta=0 and beta=1,
and arbitrary large M at fixed K. Reducible/periodic tables are covered
whenever compatible with the primitive class conditions.

When delta<=a, F=max(i,delta) and i+delta<=2F, giving 8000F. The constants
64 and g remain unchanged; beta affects only the proof's case analysis.

### Unit 7 — Original union, minimum overlaps, quantifiers and scope (443–626)

**PASS.** The candidate's Omega_closed and r_closed exactly match the
original handoff RESEARCH_PLAN, not a conveniently reduced union or a
single selected benchmark. All applicable certificates hold for the same
ALG: accepted S024 supplies 49g at beta=0, 858i at beta=1, 1472H on the
S019 strip, and 337a on B or strong beta. For an F certificate, if delta<=a
the new 8000F applies, including equality. If delta>a, N cannot be its
reason for applicability, so B or strong beta holds and F=a; use 337a.

Hence EACH applicable scale is an upper certificate with constant <=8000
for the SAME rule. Taking their finite minimum is valid without a
beta-dependent algorithm choice. At beta=0, N forces a=1 and therefore
F=g=1; B is impossible; H applicability forces g=H=1. Thus r_closed=g.
At beta=1, F=i and there is no H-strip certificate, hence r_closed=i.
H/F overlaps and delta=a are fully covered. No stationary-only guarantee
is silently assigned to arbitrary mu.

Every denominator is positive since 0<i<=a<=g and H,F>=i. For any ONE
possibly randomized beta-blind predictor, the inherited full-data IID
lower at beta=1 is i/(32sqrt(6)). The underlying S005 witnesses use
mu=p tensor p and all M+2 informative IID symbols; no initial information
is discarded. Fixing a predictor first, taking its source supremum, then
the beta supremum and finally the infimum preserves the normalized lower.
The one explicit ALG gives the upper 8000. This is the contract's Gamma
quantifier, not an interchange of infimum and supremum or a family of
different algorithms chosen separately for each beta.

The failure log is mathematically accurate: NEXT actually fails; total-path
coupling would cost Mdelta; D_s/N_s independence is unavailable; a bare
exp(-cK) remainder is inadequate; full boundary counts are endpoint
dependent; IID-reference laws cannot be imposed on original triples.
The new proof avoids each issue by the stated mechanism. Its exact novelty
boundary is also accurate: MT, SM, row-center structure and earlier closed
regions are inherited; the weighted clipped edit bridge, its tail transfer
and the complete-union assembly are new work in this manuscript, not a
claim of literature priority.

The following scientific interfaces were checked against their actual
bodies, in addition to the predecessor audits. Predecessor proofs are
inherited at their stated domains, not newly re-certified in full here.

| Source | Actual interface checked and used |
|---|---|
| S024 §§2–3 | MT, IID disjoint triples, pathwise four-boundary/prior restoration, finite residue arithmetic |
| S024 §§4–8 | SAME count-guard 49g/858i/176a/337a/1472H; its accepted narrower union and excluded NEXT |
| S022 §§3–4 | Exact original full-reference IID second moment 423K^3/n, arbitrary mu |
| S006 Lemmas 1,5 | All-row center from legal two-step minorization, arbitrary-mu pooled martingale; stationary matched theorem not transferred |
| S011 Proposition 2, Proposition 3, Corollary 4, Proposition 5 | Same all-state center, exact N/B/strong-beta F domains, original-rule B upper, full-data IID lower and endpoints |
| S001 §§1,3 | Stationary original upper and integer actual-terminal occupancy interface inherited by S024 |
| S018 Lemma 2 | Full-symbol pair splitting, conditional-only-on-first-success stationary suffix, exact geometric weights/count domination inherited by S024 |
| S019 statement and §§1–3 | Original-count 128H and matched 2^-18H only on M<=K^4,beta<=1/2 |
| S005 §§1–4 | Exact IID law, arbitrary initial-pair domain, full M+2-data randomized-algorithm IID lower behind Gamma |

## 4. Independently constructed finite diagnostics

The reviewer wrote and executed `S025_review_checker_v1.py`,
without reading/importing/rerunning the producer checker. Final execution
completed with **PASS**, saved to
`S025_review_checker_v1_results.json`. Final byte bindings appear
below. These computations supplement the symbolic proof, not replace it.

1. Twelve exact row-mixture coupling experiments with binary p, including
   sparse p, delta=0 and delta=1, context-dependent residuals, stochastic
   residuals, and all four point initial pairs. They enumerated 17,068
   positive-probability coupled complete atoms at M=5 or 6; checked 480
   actual complete-history Markov law/reference-product-law/clean-reference
   identities and 3,472 full-prefix/clean-terminal factorizations.
2. 68,965 exact rowwise edit, count-difference, normalized-vector and
   denominator comparisons; 17,095 exact SEL checks. There were 17,079
   pooled decisions and sixteen row selections, so the selected-row branch
   was exercised rather than silently vacuous.
3. 3,111 clean-endpoint CT-transfer checks, twenty nonempty actual count
   tails and twenty-five nonempty reference tails. Twenty-four active-g
   transfer checks all had nonempty actual g tails.
4. Twenty-seven genuine long positive-probability sample paths at K=2,3,8,
   M=10,000, 131,072 or 131,073: constant/cyclic/reference-edited paths,
   retaining the entire actual history and both horizon parities. These
   exercise deterministic inequalities, not a simulated mean-risk claim.
5. Twelve exhaustive uniform-IID endpoint-collision experiments and 1,009
   exact countersequence parameter cases. 100,004 finite residue/horizon
   checks include horizons up to 10^60+1.
6. Seventy-seven exact binomial inverse-count and lower-tail cases, with
   L=0 through selected values up to 256 and w=0,1 plus sparse/interior
   masses. Forty-five count-dependent edit-budget experiments deliberately
   make D large on low counts, checking the good/bad pathwise decomposition
   rather than assuming independence.
7. Forty-eight wide-horizon scalar remainder checks, with K up to 4,096
   and n up to 10^60+1, and 150 minimum-overlap cases including endpoints,
   equality delta=a, and capped scales. All seventeen listed bindings and
   the frozen candidate hash were checked within the independent script.

Count, probability-law and tail-event comparisons use exact Fraction
arithmetic, including comparing squares rather than approximating thresholds.
Eighty-digit Decimal is used only for final exponential/radical scalar
comparisons. The row-mixture test tables verify the coupling construction;
they are NOT asserted to possess the prescribed two-step coefficient merely
because they have a one-step common component. Universality rests on the
symbolic proof above, not these finite cases.

## 5. Assembly, issues, and review stopping boundary

All seven contracted units close without an unproved statistical bridge:

    legal all-state row center -> exact independent-innovation coupling
      -> interior clipped weighted edits + final-two-refresh independence
      -> full-count restoration + IID-reference IT20 / SM
      -> original count-tail CT and active-only fixed-g GT
      -> actual-rejection SEL + arbitrary-start pooled martingale
      -> NI + unchanged S024 certificates
      -> exact Omega_closed minimum and one-algorithm Gamma bounds.

No mathematical error, missing finite domain case, source-interface
mismatch, required author revision or unresolved proof obligation was
found within this scope.

### Independent reviewer artifacts

| Relative path | SHA-256 |
|---|---|
| `S025_review_checker_v1.py` | `f671b7461148cd8caffe1e3f19845076b49f7695c0790903fd038b3df1ba844d` |
| `S025_review_checker_v1_results.json` | `633e6c166fd2fce7601b1c6fab12168ad8a208487b73efb4803137254bb33b16` |
