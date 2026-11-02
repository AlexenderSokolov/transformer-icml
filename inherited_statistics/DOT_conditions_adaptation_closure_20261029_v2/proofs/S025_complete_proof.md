# S025 近 IID 适应与原已闭合并集 完整科学证明

编排说明（非原文）：本副本保留完整科学证明或完整科学审查推理；省略身份控制、私有位置、原提交状态、重复管理表及执行记录。原件未改，复制字节不改写。精确复制／删略／新增区间、原件全文身份见 COPY_MAP.json；原章节号及审查所引行号沿用原件，按同名章节与公式定位。SOURCES.md 给准确科学版本和可读闭包。有限检查仅为补充证据，不是形式验证；本次装配没有重做数学审查。

当前版本：S025 v1 七单元独立科学审查通过并已最终接纳。同一 S024 算法给 1308δ+(7715/2)i，并在原始 Ω_closed 同时满足 8000 r_closed。Goal B 仅于该原比较并集闭合；不覆盖 Goal A 未闭合区或任意 oracle 证书。NEXT 的完整合法反例在 §2，不能删略或当作已接纳 S024 定理的失败。

## 0. Result, failed successor, and scope

The proposed S024 inequality NEXT is **false**, even at beta=1. Section 2
provides a full-history stationary IID countersequence. This refutes only
that unproved sufficient successor, not any accepted S024 theorem and not
the selector. In its g=1 regime the fixed-g test never rejects pooling, so
an arbitrary original-row tail beyond g/2 is unnecessary.

The same fixed S024 algorithm nevertheless has the following new bound,
for every K>=2, M>=1, beta in [0,1], and every arbitrary-start member of
D_2(beta):

    E TV(A,theta_(Y_M)) <= min(1,4000(i+delta)),
    i=min(1,sqrt(K/(M+1))), delta=1-beta.                     (NI)

The sharper proved coefficients are 1308 delta+(7715/2)i. Together with
accepted S024, (NI) gives, for this ONE beta-blind predictor,

    sup_(D_2(beta)) L_A <=8000 r_closed(K,M,beta)
            simultaneously for every beta in Omega_closed; (ADAPT)

    1/(32sqrt(6)) <= Gamma(K,M) <=8000.                      (GAMMA)

Here Omega_closed and its minimum benchmark are exactly the original
handoff comparison union, spelled out in Section 9. No nonconstant
adaptation penalty is necessary on that union. This does not solve the
unclosed Goal A regions or identify their minimax benchmark. The algorithm
need not select a suffix in order to attain the already matched scales.
No claim of all-parameter oracle-certificate adaptation is made.

The new mathematical bridge is a hidden IID-innovation coupling with a
weighted **clipped** row-edit ratio. Its expectation at an IID endpoint is
at most 216 delta+78 i. Unlike a total-history coupling error M delta, this
bound is uniformly useful for arbitrarily large M. It preserves the actual
dependent history, endpoint, arbitrary initial pair, and all boundary data.
IID triple laws are used only on the coupled IID reference, never assigned
to the original non-IID source.

## 1. Fixed experiment, actual algorithm, and dependencies

Let n=M+1, alphabet {0,...,K-1}, K>=2, M>=1. A source is a fixed homogeneous
second-order table theta with legal pair kernel
P((a,b),(b,c))=theta_ab(c). Its initial pair has arbitrary law mu. Observe
exactly X_1,...,X_(M+2), and put

    Y_j=(X_(j+1),X_(j+2)), 0<=j<=M,
    C_s(c)=sum_(j=0)^(M-1) 1{Y_j=s,X_(j+3)=c},
    n_s=sum_c C_s(c), J=n_(Y_M),
    q(c)=(C_(Y_M)(c)+1)/(J+K),
    b(c)=(sum_(j=3)^(M+2)1{X_j=c}+1)/(M+K),
    g=min(1,sqrt(K^5/n)), a=min(1,sqrt(K^3/n)),
    t=64sqrt(K/(J+K)), T=min(g,t),
    A=b if TV(q,b)<=T, and A=q otherwise.                    (ALG)

Ties select b. These are exactly the original full counts and original
pooled counts, not shortened substitutes. TV is half L1. The actual target
is theta_(Y_M) for the unobserved X_(M+3). All risks are unconditional
expected TV, not a conditional, squared, KL, independent-query, or
random-time loss.

D_2(beta) requires an existential hidden stationary pi with
P^2(s,t)>=beta pi(t) for every s,t, including off-support starts. The
algorithm reads only K,M and the observed history; its deterministic seed
is a source-independent one-point law. Beta, delta, pi, p, residual laws,
refresh labels, and all coupled reference variables below are analysis
objects only. The same A is fixed before every source supremum and before
comparison of beta values.

Direct frozen scientific dependencies, read in their actual bodies:

1. Accepted S024, `closed_class_adaptation_diagnostic_v1.md`, together
   with its full independent review: exactly ALG has general
   49g, IID 858i, stationary 176a, condition-B/strong-beta 337a, and S019
   strip 1472H upper bounds. Its Section 2 proves the deterministic-m
   smoothed-multinomial excess tail

       E[E_m 1{E_m>3sqrt(K/(m+K))}]
           <=4sqrt(K/(m+K)) exp(-4K).                        (MT)

   Its Section 3 provides the exact IID triple decomposition and pathwise
   restoration used in Section 3 below. The unproved NEXT is not imported.
2. Accepted S022, full proof/review: the original row add-one
   under IID transition outputs and arbitrary initial pair satisfies

       E TV(q,p)^2 <=min(1,423K^3/n).                        (SM)

   Only this IID statement is used; no non-IID second moment is assumed.
3. Actual S006 Lemmas 1 and 5 and S011 Proposition 2: all-state two-step
   minorization gives theta_s(c)>=(1-delta)p(c), for the hidden vector
   p(c)=sum_d pi(c,d), at every row. Its row-center and arbitrary-mu
   pooled-martingale arguments are restated where needed. Their stationary
   matched upper is not transferred to arbitrary mu.
4. S024's already audited S001/S011/S019 and endpoint interfaces are
   inherited only at their stated domains for Section 9. S011's IID
   all-full-history-algorithm lower i/(32sqrt(6)) gives GAMMA's lower.

No external theorem or literature result is needed. All new scalar,
binomial, coupling and deterministic comparisons are proved below.

## 2. A legal countersequence to NEXT, not to ALG

Take any even integer m>=32, set K=m^2, M=m^3, and let p be uniform on a
fixed subset of d=K/4 symbols. Put theta_s=p at every row and mu=p tensor p.
This is a legal member of D_2(1); every one of the M+2 observed symbols is
IID p. It is a valid stationary subclass of the arbitrary-mu experiment.

For every departure j<M,

    P(Y_j=Y_M)=1/d^2.

For j<=M-2 the two pairs have disjoint coordinates and the claim follows
by independent uniform pairs. For j=M-1, equality requires the three
successive symbols X_M,X_(M+1),X_(M+2) all equal, also of probability 1/d^2.
Thus E J=M/d^2=16/m, and Markov's inequality gives

    P(J=0)>=1-16/m>=1/2.

On J=0 the original add-one q is uniform on all K symbols, so
TV(q,p)=1-d/K=3/4. Also g=1, because M+1<=K^5, and t=64. Hence T=1 there.
For the precise proposed S024 quantity, with delta=0,

    E[e_theta 1{e_theta>T/2}] >=(3/4)(1-16/m)>=3/8,
    i=sqrt(m^2/(m^3+1))<=m^(-1/2) ->0.                      (FAIL)

No parameter-independent C can make NEXT<=C(i+delta). This is a finite
counterfamily followed by an explicit limit, not a discarded-history lower.
The same histories do not force a bad selector decision: the g=1 test
cannot itself reject, since TV(q,b)<=1. A correct proof must restrict that
part of the analysis to actual rejection. This diagnosis motivates the
replacement in Section 8.

## 3. A slightly lower IID count-tail threshold

We need a threshold-20 version of S024's threshold-32 IID tail. Under an
all-row IID p table, arbitrary mu, M>=5 and n>K, write q^0,J^0 for the
original full-history terminal rule/count, e_0=TV(q^0,p), and
r_0=sqrt(K/(J^0+K)). Then

    E[e_0 1{e_0>20r_0}] <=3i.                               (IT20)

Here is the complete deduction from the accepted local IID interfaces.
Let I={2,...,M-3}; partition it by j modulo three. At a fixed row s, let
N_s^r,C_s^r be the reference group counts, N_s=sum_r N_s^r,
u_s=sqrt(K/(N_s+K)), and

    q_s^r=(C_s^r+1)/(N_s^r+K),
    w_s^r=(N_s^r+K)/(N_s+3K),
    Z_s=sum_r w_s^r TV(q_s^r,p)
                   1{TV(q_s^r,p)>3sqrt(K/(N_s^r+K))}.

S024's exact convex combination, four-boundary-departure restoration and
Cauchy-Schwarz give, pathwise at every row,

    TV(q_s^0,p)<=(4+3sqrt(3))u_s+Z_s,
    J_s^0+K<=N_s+K+4<=3(N_s+K).

Therefore the baseline is at most (9+4sqrt(3))r_s^0<16r_s^0,
using sqrt(3)<7/4. On e_s^0>20r_s^0 this baseline is less than 4e_s^0/5,
so e_s^0<=5Z_s. The IID endpoint is independent of I and has mass
w_s=p(a)p(b). In a single residue, disjoint triples are IID p tensor p
tensor p, and conditional selected outputs at a fixed row are multinomial.
Different residue groups are not claimed independent. Drop only weights
w_s^r<=1 and apply MT to obtain

    E[e_0 1{e_0>20r_0}]
       <=20 exp(-4K) sum_r sum_s w_s E sqrt(K/(N_s^r+K)).

For N~Bin(L,w), w E[1/(N+1)]<=1/(L+1), including w=0 by a zero weighted
term. Weighted Cauchy-Schwarz bounds each residue sum by
sqrt(K^3/(L_r+1)). With L_*+1>=n/9 for M>=5 this gives

    E[e_0 1{e_0>20r_0}] <=180 exp(-4K) sqrt(K^3/n).

The exponential-series term (4K)^4/24 gives exp(4K)>=72K for every K>=2
(as already checked in S024), so the last display is <=(5/2)i<=3i.
Zero p coordinates, empty residue groups, arbitrary initial pairs and all
four restored departures are retained. This is exclusively an IID-reference
lemma, not a conditional claim about the original dependent source.

## 4. Exact hidden IID-innovation coupling

Fix one source and one witnessing pi. Summing the legal product identity
P^2((a,b),(c,d))=theta_ab(c)theta_bc(d)>=(1-delta)pi(c,d) over d gives

    theta_s(c)>=(1-delta)p(c), p(c)=sum_d pi(c,d).

For delta>0 define the stochastic residual
R_s=(theta_s-(1-delta)p)/delta. For delta=0 every row equals p and choose
arbitrary R_s, which will never be used.

On an auxiliary probability space first draw the actual initial pair from
mu. Independently draw, for t=3,...,M+2:

- B_t IID Bernoulli(delta);
- V_t IID p;
- independent auxiliary uniforms for drawing from R_s.

All three collections and the initial pair are independent. Generate the
actual source recursively: if B_t=0 set X_t=V_t; if B_t=1 draw X_t from
R_(X_(t-2),X_(t-1)). Its conditional transition law is exactly theta, so
this construction preserves every original complete-history probability.
It neither conditions away contaminated prefixes nor changes theta along
one trajectory.

Define the IID reference by Z_1=X_1,Z_2=X_2,Z_t=V_t for t>=3. Its law is
exactly mu(z_1,z_2) product_(t=3)^(M+2)p(z_t), including off-support starts.
All original and reference counts below retain the same M departures.

Assume M>=5 and define the terminal refresh event

    E={B_(M+1)=B_(M+2)=0}.

Its complement has probability 1-(1-delta)^2<=2delta. On E, the actual
endpoint equals the reference endpoint (V_(M+1),V_(M+2)). This pair is
independent of everything used to construct X_1,...,X_M and Z_1,...,Z_M,
and has law w_s=p(a)p(b). E itself is independent of the entire IID reference.
These statements remain true for arbitrary mu. At delta=1, E is empty;
all bounds below remain valid without any conditioning on a null event.

## 5. Clipped weighted row-edit lemma

Use the interior I={2,...,M-3}. Let N_s be the total IID-reference interior
count of row s. Mark a departure j in I contaminated if at least one of
B_(j+1),B_(j+2),B_(j+3) equals one; call the set of marked indices C.
Define the nonnegative row-edit budget

    D_s=sum_(j in C) [1{Y_j=s}+1{Y_j^0=s}],
    W_s=(D_s+8)/(N_s+K), rho_s=min(1,W_s).                   (EDIT)

Here Y_j^0=(Z_(j+1),Z_(j+2)). This budget can count an unchanged triple;
only upper domination is needed. All these variables depend only on the
initial pair and innovations through time M, not on the terminal innovations.
Since each B_t can mark at most three interior triples,

    sum_s D_s=2|C|<=6 sum_(t=3)^M B_t,
    E sum_s D_s<=6M delta.                                  (5.1)

The essential weighted bound, for M>=5,n>K, is

    sum_s w_s E rho_s <=216 delta+78 i.                     (CE)

**Proof.** Choose the largest residue group of I modulo three, using a
fixed deterministic tie rule. Let its size be L>=1 and its row count N_s^*.
Then N_s>=N_s^*, N_s^*~Bin(L,w_s), and

    L+1>=n/9, L>=n/18, M/L<=18.                             (5.2)

The first follows from the smallest-group arithmetic in Section 3; the
second follows from L+1<=2L. Put lambda_s=Lw_s.

First bound the contamination part min(1,D_s/(N_s+K)). If lambda_s<=K,
then w_s/(N_s+K)<=w_s/K<=1/L. If lambda_s>K and N_s^*>=lambda_s/2,
then w_s/(N_s+K)<=2/L. Thus the sum over these good cases is at most
(2/L)sum_s D_s, whose expectation is <=216 delta by (5.1)-(5.2).
No independence between D_s and any count is assumed.

In the remaining cases lambda_s>K and N_s^*<lambda_s/2, use the clip at
one. For N~Bin(L,w) with lambda=Lw>0,

    P(N<lambda/2)<=exp(-lambda/8).                          (5.3)

To derive it, exponential Markov at t=log 2 and
(1-w+w e^-t)^L<=exp(-lambda(1-e^-t)) give exponent at most
lambda(log 2)/2-lambda/2<=-lambda/8. Here log 2<3/4 follows from
exp(3/4)>=1+3/4+(3/4)^2/2>2. Thus the remaining weighted sum is at most

    B=sum_(lambda_s>K) w_s exp(-lambda_s/8).

If n<=K^3, then i>=1/K and B<=exp(-K/8)<=3/K<=3i, using
max_(x>=0) x exp(-x/8)=8/e<3. If n>K^3, the same scalar maximum gives

    B<3K^2/L<=54K^2/n<=54i.

Consequently the contamination contribution is <=216 delta+54i in both
cases, including all sparse p and zero weights.

For the boundary allowance, the exact binomial identity and N_s>=N_s^*
give

    sum_s w_s E[1/(N_s+K)]
       <=min(1/K,K^2/(L+1))
       <=sqrt(K/(L+1))<=3i.

The middle inequality is min(x,y)<=sqrt(xy). Finally
min(1,x+y)<=min(1,x)+y, so the +8 in EDIT contributes at most 24i.
Combining the two parts proves CE. All sums contain all K^2 rows; weights
zero contribute zero without division or null conditioning. The binomial
law concerns only the reference disjoint triples. QED.

In particular, by terminal refresh independence,

    E[1_E rho_(Y_M)]
       =(1-delta)^2 sum_s w_s E rho_s
       <=216 delta+78i.                                   (5.4)

This is a statement about the same actual endpoint on E, not an independent
query substituted into the prediction experiment. Off E will always be
charged by its actual probability <=2delta.

## 6. Pathwise full-count perturbation and count-tail transfer

Let C_s^0,J_s^0,q_s^0 be the reference FULL row vector/count/add-one.
On an unmarked interior departure the actual and reference triples agree.
Consequently their interior count-vector L1 difference at s is at most D_s.
There are exactly four omitted boundary departures 0,1,M-2,M-1 in each
history; their combined row count-vector L1 difference is at most eight.
Thus, pathwise for every row,

    ||C_s-C_s^0||_1<=D_s+8,
    |n_s-J_s^0|<=D_s+8.                                    (6.1)

No boundary symbol or initial information is removed from either actual
predictor. The constant eight simply avoids assuming anything about those
boundaries' dependence.

For positive finite vectors u,v with totals A,B, the identity
u/A-v/B=(u-v)/B+u(1/A-1/B) gives

    ||u/A-v/B||_1 <=(||u-v||_1+|A-B|)/B.

Apply it with u=C_s+1, v=C_s^0+1, B=J_s^0+K>=N_s+K. Then

    TV(q_s,q_s^0)<=min(1,W_s)=rho_s,
    n_s+K <=(1+W_s)(J_s^0+K).                              (6.2)

The first inequality also holds with W_s without the clip. On E evaluate
at the common endpoint and write e=TV(q,theta_(Y_M)),
e_0=TV(q^0,p), W=W_(Y_M), rho=rho_(Y_M), r_0=sqrt(K/(J^0+K)).
Since every target row is within delta of p,

    e<=e_0+W+delta.                                        (6.3)

We claim the actual source count-tail bound

    E[e 1{e>32sqrt(K/(J+K))}] <=870 delta+316 i.             (CT)

To prove it first work pathwise on E. If W>1/4 then e<=1<=4rho. Otherwise
W<=1/4 and (6.2) gives
sqrt(K/(J+K))>=r_0/sqrt(5/4). Put v=W+delta. If v>=e/4 then
e<=4rho+4delta. If v<e/4 and the displayed tail event holds, (6.3) gives

    e_0>3e/4>24r_0/sqrt(5/4)=48r_0/sqrt(5)>20r_0,
    e<(4/3)e_0.

The strict numerical comparison follows by squaring positive sides:
2304>2000. Combining the three cases yields on E

    e 1{e>32sqrt(K/(J+K))}
       <=4rho+4delta+(4/3)e_0 1{e_0>20r_0}.                 (6.4)

Take expectations. The contribution outside E is at most 2delta. Use
(5.4), IT20, and independence of E from the reference. The result is

    4(216delta+78i)+6delta+(4/3)3i
        =870delta+316i,

as claimed. In particular, no IID law is imposed on J or on an original
count after conditioning on the terminal pair.

## 7. Fixed-g tail only in its genuinely active regime

Suppose g<1. Then n>K^5, g=sqrt(K^5/n), i=sqrt(K/n). We claim

    E[e 1{e>g/2}] <=436 delta+3540 i.                       (GT)

On E put v=W+delta again. If v>=e/2 then e<=2rho+2delta:
when W<=1 this follows directly, and when W>1 the right side is at least
two while e<=1. If v<e/2 and e>g/2, then (6.3) gives e_0>e/2>g/4 and
e<2e_0. Thus on E,

    e 1{e>g/2}<=2rho+2delta+2e_0 1{e_0>g/4}.

For the IID reference, SM gives

    E[e_0 1{e_0>g/4}] <=(4/g) E e_0^2
       <=1692 K^3/(ng)=1692 i.                             (7.1)

Add the off-E cap 2delta and apply (5.4) to obtain
2(216delta+78i)+4delta+3384i=436delta+3540i. This proves GT only for g<1.
It is deliberately not asserted at g=1; Section 2 proves that extension
would fail. The exact IID reference includes its arbitrary initial pair
and every boundary departure when SM is invoked.

## 8. Replacement for NEXT: actual rejection and near-IID risk

Let f=TV(b,theta_(Y_M)) and d=TV(q,b). The pooled martingale calculation
is valid for arbitrary mu and gives

    E f<=2delta+sqrt(KM)/(2(M+K))+K/(M+K)
        <=2delta+(3/2)i.                                   (8.1)

For completeness, with F_j=sigma(X_1,...,X_(j+2)), the vectors
D_j=e_(X_(j+3))-theta_(Y_j) have conditional mean zero and conditional
squared Euclidean norm at most one. Cross terms vanish by conditioning,
so E||sum D_j||_2^2<=M. L1/L2 and expectation Cauchy-Schwarz give the
noise term in (8.1); smoothing costs K/(M+K). The average row and actual
terminal row are each within delta of p pathwise, costing 2delta.
For n>K, Mn<=(M+K)^2 and Kn<=(M+K)^2 prove the last comparison. For
n<=K, i=1 and the loss cap suffices. This is not an IID calculation.

Here is the stronger, rejection-restricted deterministic replacement:

    TV(A,theta_(Y_M))
       <=f+e 1{e>t/2}+1{g<1} e 1{e>g/2}.                  (SEL)

On pooling the left side is f. On a rejected path with e<=f it is already
at most f. Otherwise e>f and d<=e+f<2e. Rejection means d>t or d>g;
the latter is impossible when g=1 because d<=1. Hence at least one tail
on the right of SEL contains e, proving the inequality including all ties.
No validation label or independent test is present.

For M>=5,n>K, apply CT, GT when active, and (8.1):

    L_A<= (2delta+3i/2)+(870delta+316i)
                        +(436delta+3540i)
        =1308delta+(7715/2)i
        <=4000(delta+i).                                   (8.2)

When g=1, simply omit GT; the weaker displayed bound still holds.
If n<=K then i=1 and cap one proves NI directly. If M<=4 then
n<=5 and i>=sqrt(2/5)>1/2, so the cap again proves it. These cases include
K=2, M=1, zero counts, sparse p, arbitrary off-support initial pairs,
beta=0, beta=1, reducible/periodic legal tables when allowed, both parities,
and arbitrarily large M at fixed K. Taking cap one and source suprema proves
NI on its complete finite domain.

For delta<=a, F=max(i,min(delta,a))=max(i,delta), so (8.2) gives

    sup_(D_2(beta)) L_A<=min(1,8000F).                       (8.3)

This theorem uses the same fixed 64 and g as accepted S024, not a new
parameter-dependent algorithm. The hidden common center and coupling are
never supplied to ALG.

## 9. Exact union, overlapping certificates, and one-algorithm quantifiers

Define h_b=delta^floor(b/2) for beta<1; for beta=1 define h_b=1 when b<2
and h_b=0 when b>=2. Let B be h_floor(M/2)<=1/n, N be delta<=a, and
H=max(a,delta^(M/2)). The original comparison union is

    Omega_closed = {beta=0 or beta=1}
       union {0<=beta<=1/2 and M<=K^4}
       union {N or B or beta>=1/2}.                         (9.1)

At each fixed K,M,beta, r_closed is the minimum of every applicable scale:

- g at beta=0;
- i at beta=1;
- H on 0<=beta<=1/2, M<=K^4;
- F=max(i,min(delta,a)) on N, B, or beta>=1/2.

Every scale in that finite nonempty applicable set now has a uniform
upper for the SAME ALG. The endpoint g and i bounds are S024's 49g and
858i. Its strip bound is 1472H. For an applicable F certificate:

- if delta<=a, use the new 8000F bound (8.3), including equality;
- if delta>a, applicability cannot come from N, so B or strong beta holds;
  S024 gives 337a=337F.

This covers the union without choosing a new predictor at any beta.
Taking the smallest applicable bound proves ADAPT with constant 8000.
The overlaps can also be checked explicitly: beta=1 has r_closed=i because
F=i and no H strip applies. At beta=0, N requires a=1, so F=g=1; B is
impossible; if H applies then M<=K^4 forces g=H=1. Thus r_closed=g there.
On H/F overlaps the appropriate near/non-near branch above proves F for
the same algorithm which already has the H bound. Equality delta=a is
covered by both rate descriptions and introduces no gap.

All finite denominators are strictly positive, because i>0. For every
possibly randomized admissible beta-blind predictor, the beta=1 IID
full-data lower and r_closed=i imply a normalized worst risk at least
1/(32sqrt(6)). Supremizing over all beta in (9.1), then infimizing over
ONE common predictor, preserves that lower. The explicit ALG gives the
upper 8000. This proves GAMMA and no extra positive adaptation lower is
claimed. The result is a constant-order conclusion, not an optimal numerical
constant or an assertion that beta itself can be accurately estimated.

The stationary 176a bound from S024 remains a separate simultaneous
initialization-specific statement. It is not silently assigned to all
arbitrary-start sources. No claim is made about all unclosed Goal A regions
or about minimizing every public oracle upper outside the comparison union.

## 10. Failure log, novelty boundary, and next necessary action

1. **Actual disproved successor:** NEXT fails at exact IID by Section 2.
   This was discovered before importing it as a premise. Accepted S024 is
   unaffected. The repair is actual rejection restriction SEL, not deleting
   the counterexample or changing the threshold.
2. **Total-path coupling:** charging the probability of any contamination
   yields at best M delta, which is useless in long histories. We instead
   control a clipped rowwise edit ratio at a clean actual endpoint. The
   total 6M delta is used only after the weight/denominator cancellation
   by L, making the final bound O(delta), not O(M delta).
3. **Unclipped inverse count:** D_s and N_s are dependent. Multiplying their
   separate expectations would be unjustified, and an unbounded edit ratio
   cannot simply be charged on a count-lower-tail event. Section 5 uses a
   pathwise good-count bound and clips at one on the bad event.
4. **Naive count lower tail:** a bare exp(-cK) remainder cannot be O(i) for
   fixed K and unbounded M. Section 5 retains a second K^2/L bound and splits
   at n=K^3, preserving the required n^(-1/2) decay. IT20 similarly retains
   the full exp(-4K)sqrt(K^3/n) factor.
5. **IID transfer shortcut:** the dependent original triples are never
   assigned IID or conditional multinomial laws. Only reference innovations
   have those laws. The actual table remains fixed and all-history exact.
6. **Boundary/endpoint shortcut:** treating the full edited counts as
   independent of the actual endpoint would be false. The budget uses only
   the interior, restores both histories' four boundary departures by the
   deterministic +8, and charges failed terminal refreshes by <=2delta.
7. **Different algorithm per regime:** none is introduced. All inherited
   and new risk inequalities concern precisely ALG; only proofs split into
   parameter cases. In particular no beta-dependent threshold, suffix,
   validation split, extra trajectory or future/query replacement appears.

The new work is the counterexample to NEXT, clipped weighted contamination
lemma, its exact terminal-refresh bridge, tail transfers, and union
assembly. The IID multinomial interface, IID second moment, common-center
structure, and already closed non-near regions are inherited rather than
relabeled as new results. No external literature-priority claim is made.

## 11. Finite diagnostics and source bindings

The producer-owned script `near_iid_adaptation_check_v1.py` was
executed successfully on 2026-10-29 UTC. Its saved result
`near_iid_adaptation_check_v1.json` is PASS.

It checked:

- 24,192 exhaustively enumerated binary coupled complete histories at
  M=5,6 with identical initial pairs and clean final innovations; 97,101
  row-edit/normalization/count comparisons in total;
- 24 exact joint-law experiments on homogeneous legal row-mixture tables,
  including all binary point initial pairs: 1,152 complete actual-history
  probabilities and 15,360 terminal/interior factorization identities;
- 45 genuine long coupled paths, at K=2,3,4 and M up to 50,000, including
  constant, periodic and seeded arbitrary paths with both horizon parities;
- 24,237 count-tail and selector comparisons, with 24 nonempty actual
  count tails, 30 nonempty reference tails, 15 row selections and 24,222
  pooled selections; 45 active fixed-g comparisons with 30 nonempty tails;
- 100,000 finite horizon comparisons and 985 exact countersequence cases;
- 462 binomial lower-tail calculations and 162 weighted scalar budgets,
  including sparse reference laws, K up to 512 and n up to 10^12+1.

All count, normalized-vector, guard, complete-law and factorization
comparisons use exact rational arithmetic. Only final exponential and
weighted scalar comparisons use floating point. The row-mixture law checks
verify the coupling construction, not a claim that those test tables have
a prescribed two-step coefficient. Long paths exercise deterministic
inequalities, not a Monte Carlo risk assertion. These finite checks
supplement, and do not prove, the universal symbolic theorem.
