# S022 两端点适应的独立数学审查

编排说明（非原文）：本文件保留完整科学证明或完整科学审查推理；只省略身份控制、原提交状态、管理路径、重复来源管理表与执行记录。所有复制区间逐字节保留，原件未改；新增、复制和省略字节区间及原件全文身份见 COPY_MAP.json。原章节号和审查所引行号沿用原件，不是本副本行号；按同名章节与公式定位。来源的准确科学版本和当前可读闭包见 SOURCES.md。有限枚举只是补充证据，不是证明或形式化验证。本次装配没有重做数学审查。

当前判断：六个科学单元全部通过，随后最终接纳。只覆盖两个端点；完整候选 v1 未修订。来源版本与哈希集中列于 SOURCES.md，原文的科学接口检查范围保留；有限检查是补充，不能替代通用证明。

## 1. Exact accepted scope

For every integer K>=2, M>=1, n=M+1, define

    g=min(1,sqrt(K^5/n)),  i=min(1,sqrt(K/n)).

Let q be the original terminal-row add-one predictor formed from every
departure 0,...,M-1, and b the pooled add-one predictor formed from exactly
X_3,...,X_(M+2). The single deterministic algorithm, using only K,M and the
actual complete history, is

    A=b if TV(q,b)<=g, and A=q otherwise.

For this same algorithm at fixed K,M:

    sup_(all legal theta, arbitrary mu) E TV(A,theta_(Y_M))
        <=min(1,49g),
    sup_(p, arbitrary mu), theta_s=p for every s  E TV(A,p)
        <=min(1,853i).

The auxiliary original-rule second moment is valid uniformly over p and mu:

    E TV(q,p)^2 <=min(1,423K^3/n).

Using the inherited minimax endpoint lower bounds, g and i are the respective
public-class minimax orders. The endpoint adaptation functional defined in
candidate §7 satisfies

    1/(32 sqrt(6)) <= Gamma_end(K,M) <=853.

Thus a nonconstant adaptation penalty is not necessary for **these two
endpoints**. No all-beta, near-IID, stationary-adaptation, all-Omega_closed,
or exact original-rule minimax characterization is accepted by this review.

The experiment remains the original one: homogeneous legal second-order
shift table, arbitrary initial pair, M observed departures, full M+2-symbol
history, actual terminal pair Y_M, and unconditional expected TV. The
second moment is only a proved intermediate tool. No unseen next output,
independent validation trajectory, query replacement, source label or
hidden parameter is available to A.

## 2. Six-unit mathematical audit

### Unit 1 — Smoothed multinomial and binomial moments

**Verdict: PASS.**

For m>=1, the coordinate variances and deterministic L1/L2 comparison give
E TV(p_hat,p)^2 <=K/(4m). Applying the exact smoothing mixture and the
two-term square inequality yields

    K m/[2(m+K)^2] + 2K^2/(m+K)^2
       <=(5/2)K/(m+K).

The last comparison is valid since m/2+2K <=(5/2)(m+K). At m=0 the smoothed
vector is uniform, its squared TV is at most one, and the displayed bound
is 5/2; no empirical vector with denominator zero is used. Replacing m+K
by m+1 is in the upper-bound direction. Zero coordinates cause no issue.

For N~Bin(L,w), the identity for E[1/(N+1)] follows by shifting the finite
binomial sum, equivalently integrating (1-w+wt)^L from t=0 to 1. For w>0,
multiplication by w bounds it by 1/(L+1). For w=0 the weighted term is zero,
and no division by w or null-event conditional law is necessary. L=0 and
w=1 are included. The two lemmas have precisely the strength used later;
the proof never squares an existing expected-TV upper bound.

### Unit 2 — IID law, arbitrary initial pair, interior and endpoint

**Verdict: PASS.**

The all-starting-state q=2,beta=1 condition forces P^2(s,t)=pi(t) by equal
row sums. The unique legal two-step route gives
P^2((a,b),(c,d))=theta_ab(c)theta_bc(d); summing over d forces every
theta_ab to be the same p. Thus the full path law is exactly
mu(x_1,x_2) times the product of p(x_j) for j=3,...,M+2, including zeros and
initial pairs outside the stationary support. Initial symbols themselves
are not declared IID. The target row equals p at every possible endpoint.

For M<=4, the universal TV^2 cap proves SM directly because K^3/n>=8/5.
All subsequent interior independence arguments are restricted to M>=5.
Here I={2,...,M-3} contains M-4 departures and its triples use precisely
coordinates within X_3,...,X_M. The actual endpoint uses X_(M+1),X_(M+2),
so it is independent of the entire interior and has law w_ab=p(a)p(b).
This independence is **not** asserted between the endpoint and the original
full row counts or deleted departures. In particular, no M=1 endpoint
product-law assertion is needed.

In each fixed residue modulo 3, triples have disjoint symbol coordinates
and are IID p tensor p tensor p. Conditioning on all first-two-coordinate
pairs in that one group leaves its third coordinates IID p. Consequently,
at a fixed row and selected count m, the selected output counts really have
the multinomial(m,p) law. Groups of different residues may overlap; the
argument neither conditions on all groups' contexts simultaneously nor
requires independence between groups.

Independent endpoint averaging and Unit 1 therefore give

    E TV(q^r_(Y_M),p)^2
       <=(5/2)K sum_s w_s E[1/(N^r_s+1)]
       <=(5/2)K^3/(L_r+1).

All K^2 rows are a valid upper sum, including rows with w_s=0, whose actual
weighted contributions vanish. Empty groups have L_r=N^r_s=0 and are
covered rather than removed from the argument.

### Unit 3 — Random convex weights, four restorations and constant 423

**Verdict: PASS.**

For each row and each path, weighting the three add-one vectors by
(N^r_s+K)/(N^o_s+3K) gives exactly (C^o_s+3)/(N^o_s+3K). The weights are
nonnegative and sum to one. Convexity of TV followed by Jensen for its
square gives the weighted squared-error sum, and dropping weights gives
the unweighted sum. This is a deterministic inequality; no error is
averaged as though its count-dependent weight were independent. Hence
the interior squared error is at most (15/2)K^3/(L_*+1).

For M>=5 the excluded indices are exactly the four distinct departures
0,1,M-2,M-1. Rowwise C=C^o+D with D nonnegative and d<=4. The stated
mixture for adding d observations is exact when d>0; d=0 is treated without
normalization. The difference between one-prior and three-prior smoothing
is also an exact convex mixture with the uniform vector. The two resulting
TV bounds imply

    D'_s <= (4+2K)/(N^o_s+K) <=4K/(N^o_s+K),
    (D'_s)^2 <=16K/(N^o_s+K) <=16K/(N^r_s+1).

The first relaxation may exceed one but is still a valid bound. The square
relaxation uses N^o_s+K>=K, and the last comparison uses N^o_s>=N^r_s and
K>=1. Neither deleted observations nor D'_s must be independent of the
endpoint. Its final dominating interior count is independent, so averaging
it gives 16K^3/(L_r+1). The restored p^+ is the original q, with the original
one-prior smoothing and all M departures, not a new shortened predictor.

Combining the two squared errors gives 2*(15/2)+2*16=47. With
L_*=floor((M-4)/3), writing M-4=3a+b, b in {0,1,2}, gives
L_*+1=a+1>=(M-3)/3. For M>=5, 3(M+1)/(M-3)<=9, including the boundary
M=5, so L_*+1>=n/9. This proves 47*9=423 in SM. The loss cap and the
already treated M<=4 cases complete its entire finite domain.

### Unit 4 — One observable selector and the general 49g guarantee

**Verdict: PASS.**

The algorithm uses only q,b and a threshold determined by K,M. Ties select
b. On that branch the triangle inequality gives loss<=TV(q,target)+g;
on the other branch this inequality is immediate. It holds pathwise for
the original actual target, without validation, endpoint independence or
stationarity. The imported full-source upper is precisely for this original
q in this experiment. Therefore risk<=48g+g, and cap one proves T0.

When g=1, all possible TV(q,b) are <=g and pooling is always selected.
The general guarantee is then only cap one, as it should be; no small
general-risk guarantee is improperly assigned to pooling. The row predictor
used in the imported general bound is never thinned.

### Unit 5 — IID rejection-tail control and 853i, including caps

**Verdict: PASS.**

At g=1 the selected estimator is b and the inherited arbitrary-initial-pair
pooled bound directly gives <=(3/2)i. At 0<g<1, n>K^5 and thus both relevant
uncapped formulas are valid: g=K^(5/2)/sqrt(n), i=sqrt(K/n).

Writing e=TV(q,p), f=TV(b,p), d=TV(q,b), rejection implies e+f>=d>g.
Consequently the selected loss is at most

    f+(e+f)1{e+f>g} <=f+(e+f)^2/g <=f+2(e^2+f^2)/g.

This pathwise upper may overcount f on rejection, which is harmless. The
strict rejection event matches the stated tie convention. No conditioning
on the test or independence of q,b or their errors is used.

Applying Unit 1 to the M IID transition outputs gives
E f^2 <=(5/2)K/(M+K)<=(5/2)K/n. Together with SM and the mean pooled bound,

    risk <=[3/2+846+5/K^2]i <=(3395/4)i =848.75i <853i.

The manuscript's alternative coarser 852.5i calculation is also correct:
replacing K by K^3 in the pooled squared moment gives
3/2+2*(423+5/2)=852.5. Neither numerical slack changes the theorem.
Finally cap one supplies min(1,853i); arbitrary p,mu can then be
supremized because every inequality is uniform. All finite caps, small
alphabets and zero probabilities are covered.

### Unit 6 — Endpoint lower, minimax interpretation, failures and scope

**Verdict: PASS.**

D_2(0) is the full legal class because a finite stochastic kernel has at
least one stationary law. S003's finite stationary-existence proof suffices;
no convergence, irreducibility or uniqueness is assumed. Its eta=1 general
lower is exactly the accepted MM5 all-common-algorithm interface. The
underlying MM5 scientific proof retains the entire observed history through
a source-independent bijection for its high-K family; its small-K interface
is the full-history IID testing lower in GU. Thus the use of a g lower is
not a discarded-data or selected-row lower.

D_2(1) is the all-row IID class from Unit 2. S005's hypercube lower retains
all M+2 observed symbols using its legal stationary-initialized subclass,
while the present upper works for every initial pair law. Its bound applies
to every common randomized full-history kernel, including any beta-blind A.
For every such A the second normalized component alone is at least
1/(32 sqrt(6)); taking the maximum and then the infimum preserves this
lower. The same explicit A provides both upper components <=853. Both
denominators are positive for each finite K,M. There is no exchange of
source supremum and algorithm infimum and no parameter-specific algorithm
choice hidden inside the simultaneous claim.

The general and IID matching rates are inherited endpoint interpretations,
not new lower constructions. The normalized lower is a nonzero baseline,
not evidence of a positive *additional* adaptation cost. The candidate
correctly states that the original q alone is not uniformly IID-optimal,
rather than treating SM as a matching IID risk formula for q.

The restricted-rule failures are legitimate: the binary deterministic
alternating source is a legal homogeneous table with fixed initialization;
for even M its pooled add-one vector is uniform while the actual target is
a point mass. A convex combination with fixed pooled mass lambda>0 retains
wrong-coordinate mass at least lambda/2, whereas g tends to zero. This
refutes pooling and those fixed mixtures, not all algorithms. The warnings
about squaring first-moment bounds, conditional IID at original counts,
independent validation and arbitrary initial pairs are accurate.

S006's pooled martingale lemma and its q=2 common-center argument permit
the limited successor motivation. Its matched minimax statement still
requires stationarity and is not imported for arbitrary mu. No beta<1
second-moment lemma, F adaptation, H adaptation or all-Omega_closed result
has been proved by S022.




## 3. Source identity and interface checks

The candidate, contract, full required scientific bodies, and historical
reviews were read. L1MAX and GU support the exact upper interface; S005
supports the exact IID law, pooled mean bound, full-data lower and original
rule separation; S003 plus the full MM5 scientific proof support the
general lower interpretation. S006 was read to preserve the initialization
and successor boundary, not as an extra arbitrary-start matched theorem.


Execution completed with status **PASS**. Every tested inequality used
exact rational arithmetic; randomly generated paths used a fixed seed,
but their counts and inequalities were evaluated exactly.

1. 105 binomial cases included L=0,...,20 and w=0,1/16,1/4,1/2,1.
2. 63 multinomial cases checked all count vectors for m=0,...,8 under seven
   binary/ternary p vectors, including point masses and zero coordinates.
3. 565 joint selected-count atoms were independently obtained by enumerating
   disjoint triple laws and compared with Bin(L,w)*Multinomial(m,p), for
   L=0,1,2. This explicitly includes empty groups and w=0.
4. 263 exact IID experiments enumerated 8,014 positive-probability full
   histories: binary M=1,...,8 and ternary M=1,...,5, with every point initial
   pair, including those outside p's support. Complete probability masses,
   original squared risks, pooled squared risks, endpoint laws where
   applicable, and interior group bounds passed.
5. In those histories, 37,844 count-dependent mixture identities and
   convexity checks and 113,532 restoration inequalities passed. The
   endpoint/interior product factorization was checked for each M>=5 path.
6. 99,996 finite horizon comparisons covered M=5,...,100000.
7. 308 guard inequalities were checked on 42 independently constructed
   noncapped-threshold paths. There were 41 pooled branches and one original
   row branch; thresholds included g=1/2 and g=1/4. Alternating paths and
   deterministic constant paths were among the probes.

These computations are finite arithmetic/indexing diagnostics, not a proof
of universal risk bounds. In particular the small exact experiments do not
establish the nontrivial large-horizon second-moment rate by themselves;
that rate rests on Units 1–3. The large finite-path guard checks verify
deterministic inequalities, not a simulated mean-risk theorem.

The saved producer diagnostic JSON was inspected and its stated counts
agree with manuscript §9; the producer checker was not rerun or treated as
independent evidence. Its reported simulations are not a proof premise.


The full dependency chain closes without a missing mathematical step:

    direct multinomial/binomial calculations + exact IID transition law
      -> disjoint-triple row moments + independent interior endpoint
      -> pathwise random-weight combination + four-departure restoration
      -> original-row SM;

    original full-source GEN + observable guard -> T0;
    SM + pooled first/second moments + pathwise rejection control -> T1;
    same A + inherited full-history endpoint lowers -> Gamma_end bounds.


