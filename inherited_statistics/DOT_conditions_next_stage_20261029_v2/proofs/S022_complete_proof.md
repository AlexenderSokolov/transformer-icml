# S022 未知 beta 的两端点共同选择器 完整科学证明

编排说明（非原文）：本文件保留完整科学证明或完整科学审查推理；只省略身份控制、原提交状态、管理路径、重复来源管理表与执行记录。所有复制区间逐字节保留，原件未改；新增、复制和省略字节区间及原件全文身份见 COPY_MAP.json。原章节号和审查所引行号沿用原件，不是本副本行号；按同名章节与公式定位。来源的准确科学版本和当前可读闭包见 SOURCES.md。有限枚举只是补充证据，不是证明或形式化验证。本次装配没有重做数学审查。

当前版本：S022 v1 已独立数学审查并最终接纳。结论只同时覆盖 β=0 与 β=1，不是整个 Ω_closed 的适应结论。科学来源身份集中于 SOURCES.md；下一步近 IID 段落仍为待证明目标。

## 0. Result and exact new bridge

A single observable selector preserves the general arbitrary-initialization
rate and attains the IID rate, without reading beta or a class label:

> Compute the original terminal-row add-one vector q and the pooled add-one
> vector b. Put g=min(1,sqrt(K^5/(M+1))). Output b when TV(q,b)≤g, and q
> otherwise.

For all integers K≥2, M≥1, this deterministic rule satisfies

    sup_(theta,mu) E TV(A,theta_(Y_M)) ≤ min(1,49g),             (T0)
    sup_(p,mu), theta_s=p E TV(A,p) ≤ min(1,853i),              (T1)
    i=min(1,sqrt(K/(M+1))).

Both suprema concern the same algorithm at fixed K,M and the same observed
experiment. In particular a universal common constant 853 works for both
beta=0 and beta=1. The second class retains **arbitrary initial pair laws**.
Existing all-algorithm lower bounds identify both displayed rates as their
respective public-class minimax orders. No necessary nonconstant endpoint
adaptation penalty exists.

The new nontrivial bridge is a second-moment bound for the **original** row
rule under IID transitions and arbitrary initial pair:

    E TV(q,p)^2 ≤ min(1,423 K^3/(M+1)).                         (SM)

It is proved below from deterministic deletion of four boundary departures
**in an auxiliary comparison only**, and a three-way partition into disjoint
IID triples. The actual algorithm still uses the entire original row counts.
No independent validation data, future symbol, random-time target, or
conditional-IID claim at a selected original count is used.

## 1. Frozen experiment and finite quantifiers

Let A_K={0,...,K−1}, S=A_K^2, K≥2 and M≥1 integers, n=M+1. A source is a fixed
homogeneous second-order probability table theta=(theta_s)_(s in S) with the
legal pair transition (a,b)→(b,c) of probability theta_ab(c). Zeros, reducible
and periodic kernels are allowed. The initial pair has any law mu on S.
Observe H=(X_1,...,X_(M+2)), put

    Y_j=(X_(j+1),X_(j+2)),                      0≤j≤M,
    C_s(c)=sum_(j=0)^(M−1) 1{Y_j=s, X_(j+3)=c},
    n_s=sum_c C_s(c),
    q(H)(c)=(C_(Y_M)(c)+1)/(n_(Y_M)+K),
    T(c)=sum_(j=3)^(M+2) 1{X_j=c},
    b(H)(c)=(T(c)+1)/(M+K).

Exactly M departures are observed; departure M and X_(M+3) are unobserved.
TV(v,w)=||v−w||_1/2. The loss is TV(A(H),theta_(Y_M)), with the actual terminal
pair of this same history. Every displayed expectation is unconditional.

The class D_2(beta) consists of those (theta,mu) for which some hidden
stationary law pi satisfies P_theta^2(s,t)≥beta*pi(t) for all s,t. The original
mu is unrestricted. At beta=0 this is the full class (every finite kernel has
a stationary law). At beta=1, S005 §2 proves theta_s=p for every row, for some
unknown p, including rows outside stationary support. Its full-history law is

    P_(p,mu)(H=h)=mu(h_1,h_2) product_(j=3)^(M+2) p(h_j).       (IID)

Thus X_3,...,X_(M+2) are IID p and independent of the initial pair, and the
actual target theta_(Y_M) equals p on every history. The initial pair itself
need not be IID or supported on supp(p)^2.

For **each** K,M define one A_(K,M), not a family indexed by beta:

    g=min(1,sqrt(K^5/n)),
    A_(K,M)(H)=b(H) if TV(q(H),b(H))≤g; otherwise q(H).        (ALG)

Ties select b. All inputs are K,M,H. The rule is deterministic (equivalently,
its source-independent seed has a one-point law); beta, eta, p, pi, theta,
mu, a class label, regeneration labels and all future data are absent.
The theorem quantifier is

    for every K≥2,M≥1, this one A_(K,M) obeys (T0) and (T1)
    simultaneously for every source/initialization in their respective classes.

A source may depend on K,M and on the fixed algorithm inside a supremum,
but remains fixed along each generated trajectory.

## 2. Exact dependencies and what is not imported

1. **L1MAX statistical proof, §8 (L1+):** for the original q in the full
   arbitrary-initialization experiment,

       E TV(q,theta_(Y_M))≤min(1,48 sqrt(K^5/n))≤48g.           (GEN)

   Its GU occupancy interface is P(n_(Y_M)<v)≤min(1,K^4 v/n).
   The present proof imports (GEN), not a high-probability or second-moment
   version. GU is an inherited dependency of (GEN), not separately needed
   in the new IID argument.
2. **S005 §2:** exact beta=1/IID-table equivalence and (IID), including
   arbitrary mu and zero coordinates. **S005 §3:** pooled add-one mean risk

       E TV(b,p)≤min(1,(3/2)sqrt(K/n))≤(3/2)i.                 (POOL1)

   **S005 §4:** for every full-history randomized common algorithm, the IID
   supremum is at least i/(32 sqrt(6)).
3. **S003 §1 and §§3,6:** the general minimax g lower at eta=1 is inherited
   through its accepted MM5 interface, with constant 2^(−16). This is needed
   only for the minimax-order interpretation, not either upper proof.
   Existing eta-blind initialization adaptation remains inherited; it is not
   re-proved or claimed as new here.
4. **S006 §§1–2, Lemma 1:** inspected for the distinction between the public
   parameter selector and the new observable selector. Its matched theorem
   requires stationarity. Its pooled near-IID martingale bound itself permits
   arbitrary mu. No S006 stationary bound is assigned to arbitrary mu here,
   and no beta<1 second-moment claim is imported.

No external literature theorem is needed for the new proof. Squared TV is
only an intermediate upper-bound tool proved directly, not the risk target;
we do not square an existing expected-TV upper bound.

## 3. Elementary smoothed multinomial second moment

**Lemma 3.1.** Let V_1,...,V_m be IID p in A_K, with m an integer ≥0. Define
q_m(c)=(sum_l 1{V_l=c}+1)/(m+K). Then

    E TV(q_m,p)^2 ≤ (5/2) K/(m+K) ≤ (5/2) K/(m+1).            (3.1)

The claim includes m=0, when q_m=u is uniform.

**Proof.** For m≥1 let p_hat be the empirical vector and u the uniform vector.
Cauchy–Schwarz on K coordinates and the multinomial coordinate variances give

    E TV(p_hat,p)^2
       ≤(K/4) E||p_hat−p||_2^2
       =(K/(4m))(1−||p||_2^2)≤K/(4m).

The exact identity q_m=[m/(m+K)]p_hat+[K/(m+K)]u, the triangle inequality,
TV(u,p)≤1, and (x+y)^2≤2x^2+2y^2 yield

    E TV(q_m,p)^2
       ≤ K m/[2(m+K)^2]+2K^2/(m+K)^2
       ≤ (5/2) K/(m+K).

At m=0 the left side is at most 1, while the right side is 5/2. The second
inequality in (3.1) follows from K≥1. No positivity is required. ∎

**Lemma 3.2.** If N~Bin(L,w), L≥0 an integer and 0<w≤1, then

    E[1/(N+1)]=[1−(1−w)^(L+1)]/[(L+1)w],
    w E[1/(N+1)]≤1/(L+1).                                   (3.2)

For w=0, the product on the left of the inequality is zero, so the inequality
continues to hold without division by w.

**Proof.** Use binom(L,m)/(m+1)=binom(L+1,m+1)/(L+1) in the finite binomial
sum and change the index to m+1. The omitted zero term has mass
(1−w)^(L+1); division by w is used only when w>0. ∎

## 4. Original IID terminal-row second moment, including all boundaries

We prove (SM) for every p and every mu, with theta_s=p. If M≤4 then n≤5 and
K³/n≥8/5, so TV²≤1 directly proves the asserted cap. Hence assume M≥5.

### 4.1 Deterministic interior, three partitions, and independent endpoint

Keep only the departure indices

    I={2,3,...,M−3},                  |I|=M−4,
    I_r={j in I: j≡r mod 3},          r=0,1,2,
    L_r=|I_r|,                       L_* = min_r L_r=floor((M−4)/3).

An empty I_r is permitted. Write, for every fixed row s=(a,b),

    C^r_s(c)=sum_(j in I_r) 1{X_(j+1)=a,X_(j+2)=b,X_(j+3)=c},
    N^r_s=sum_c C^r_s(c),
    q^r_s(c)=(C^r_s(c)+1)/(N^r_s+K),
    C^o_s=sum_r C^r_s,               N^o_s=sum_r N^r_s,
    q^o_s(c)=(C^o_s(c)+3)/(N^o_s+3K).

These are **auxiliary analysis vectors**; ALG never substitutes them for q.
Every interior triple uses only symbols X_3,...,X_M. The terminal pair
Y_M=(X_(M+1),X_(M+2)) is independent of all these symbols under (IID), and has
law w_s=p(a)p(b). This remains true for every initial pair law mu because
(IID) makes all transition outputs IID p independently of the initial pair.

Within each single r, distinct triple starting indices differ by at least 3,
so their three symbol sets are disjoint. Their triples are therefore IID with
law p⊗p⊗p. The three different r groups can overlap and are **not claimed
independent**; no proof step requires independence between groups.

For fixed r,s, N^r_s~Bin(L_r,w_s). Conditional on the list of the L_r first-two-
coordinate pairs, the third coordinates are independent IID p, independent
of that list. Thus the outputs selected by the occurrences of s are IID p
conditional on that list; averaging lists at a fixed N^r_s=m preserves the
multinomial(m,p) output-count law. This conditional-IID statement belongs only
to disjoint independent triples at a fixed row, not to original adaptive row
counts or counts conditioned on the original endpoint.

Apply Lemmas 3.1–3.2, then independent actual-endpoint averaging:

    E TV(q^r_(Y_M),p)^2
      =sum_s w_s E TV(q^r_s,p)^2
      ≤(5/2)K sum_s w_s E[1/(N^r_s+1)]
      ≤(5/2) K³/(L_r+1).                                   (4.1)

All K² rows are retained in the final upper sum. Rows with w_s=0 contribute
zero on the left and require no null-event conditional law.

### 4.2 Count-dependent weights do not create a conditioning gap

Exactly, for every row s and every path,

    q^o_s = sum_(r=0)^2 [(N^r_s+K)/(N^o_s+3K)] q^r_s.         (4.2)

The weights are nonnegative and sum to one. By convexity of TV and of the
square on nonnegative numbers,

    TV(q^o_s,p)^2
      ≤sum_r [(N^r_s+K)/(N^o_s+3K)] TV(q^r_s,p)^2
      ≤sum_r TV(q^r_s,p)^2.                                  (4.3)

This is pathwise; no random weight is declared independent of a row error.
Evaluating at the same actual Y_M, taking expectations and using (4.1),

    E TV(q^o_(Y_M),p)^2 ≤(15/2) K³/(L_*+1).                  (4.4)

### 4.3 Restore every deleted departure and the exact original smoothing

The excluded departure indices are exactly 0,1,M−2,M−1, four distinct indices
when M≥5. For a given row let D_s=C_s−C^o_s≥0 and d_s=sum_c D_s(c), so
0≤d_s≤4 and n_s=N^o_s+d_s. Define the intermediate one-prior vector

    q^(o,1)_s=(C^o_s+1)/(N^o_s+K).

Adding d_s actual observations gives the exact convex combination (when d_s>0)

    p^+_s=[(N^o_s+K)/(N^o_s+d_s+K)] q^(o,1)_s
             +[d_s/(N^o_s+d_s+K)] (D_s/d_s),

and for d_s=0 the two vectors agree. Consequently

    TV(p^+_s,q^(o,1)_s)≤d_s/(N^o_s+d_s+K).

Also

    q^o_s=[(N^o_s+K)/(N^o_s+3K)] q^(o,1)_s
                     +[2K/(N^o_s+3K)]u,

so TV(q^(o,1)_s,q^o_s)≤2K/(N^o_s+3K). Therefore, pathwise and for all rows,

    D'_s:=TV(p^+_s,q^o_s)
       ≤(4+2K)/(N^o_s+K)
       ≤4K/(N^o_s+K),                                    (4.5)

where K≥2 is used in the last step. Although this displayed bound can exceed
one, it is a valid upper bound. Squaring and using N^o_s+K≥K gives, for any
one fixed residue r,

    (D'_s)^2≤16K²/(N^o_s+K)^2
             ≤16K/(N^o_s+K)
             ≤16K/(N^r_s+1).                              (4.6)

The deleted observations may be dependent on the endpoint, initial pair and
interior symbols. Inequalities (4.5)–(4.6) are deterministic and need no
independence of deleted observations. Their final upper bound uses only the
interior counts, which are independent of the endpoint. Thus (3.2) gives

    E (D'_(Y_M))²≤16 K³/(L_r+1)≤16 K³/(L_*+1).              (4.7)

The triangle inequality and (x+y)²≤2x²+2y² now yield

    E TV(q,p)²
      ≤2 E TV(q^o_(Y_M),p)²+2 E (D'_(Y_M))²
      ≤47 K³/(L_*+1).                                     (4.8)

To compare the finite horizons, floor(x)+1≥x+1/3 at the integer values
x=(M−4)/3; more directly writing M−4=3a+b, b∈{0,1,2}, gives

    L_*+1=a+1≥(M−3)/3.

For M≥5, 3(M+1)/(M−3)≤9. Hence L_*+1≥n/9, and (4.8) implies

    E TV(q,p)²≤423 K³/n.

Combine with the universal loss cap and the M≤4 case to prove (SM). ∎

**What the lemma does not claim.** It gives no IID law after conditioning on
n_(Y_M), and it does not claim a strided or shortened predictor has general
arbitrary-source g risk. The original q alone is used in (GEN) and ALG.
In particular periodic-skeleton failures for thinned data are irrelevant to
the general bound; no thinned predictor is proposed for the general class.

## 5. General-class guarantee of the one common algorithm

Fix any legal theta and arbitrary mu. On the branch selecting q the loss is
TV(q,theta_(Y_M)). On the branch selecting b, the triangle inequality and
ALG's observable test imply

    TV(b,theta_(Y_M))≤TV(q,theta_(Y_M))+TV(q,b)
                     ≤TV(q,theta_(Y_M))+g.

Therefore on every complete history,

    TV(A,theta_(Y_M))≤TV(q,theta_(Y_M))+g.

Take expectations, apply (GEN), and use TV≤1 to obtain (T0). This bound
retains dependence of q, b, endpoint and target; there is no validation
sample. It works for arbitrary homogeneous theta and mu, including periodic
or reducible sources. If g=1, the test always chooses b since TV(q,b)≤1;
this is harmless because the claimed general rate g is then already one.

## 6. IID guarantee of the same algorithm

Fix any p and any initial pair law mu, with theta_s=p. Put, on the same path,

    e=TV(q,p),   f=TV(b,p),   d=TV(q,b).

If g=1 then ALG always chooses b, and (POOL1) proves risk≤(3/2)i, hence (T1).
Now suppose 0<g<1. This implies n>K⁵, so

    g=K^(5/2)/sqrt(n),       i=sqrt(K/n) (<1).

On a rejected pooled branch, d>g and the triangle inequality gives e+f≥d>g.
On all histories the selected loss obeys

    TV(A,p)≤f+(e+f)1{d>g}
            ≤f+(e+f)1{e+f>g}
            ≤f+(e+f)²/g
            ≤f+2(e²+f²)/g.                                (6.1)

No independence between the test and either error is asserted or needed.
By Lemma 3.1 with m=M, the IID pooled rule satisfies

    E f²≤(5/2) K/(M+K)≤(5/2) K/n.                          (POOL2)

Use (SM), (POOL1) and (POOL2) in (6.1):

    E TV(A,p)
      ≤(3/2)i + [846 K³/n+5K/n]/g
      =(3/2)i+846i+(5/K²)i
      ≤(3/2+846+5/4)i
      =(3395/4)i <853i.                                   (6.2)

The looser displayed integer constant 853 is therefore valid. (Even
bounding K by K³ would give 852.5i.) Apply the loss cap and take the supremum
over p,mu to prove (T1). All constants are independent of K,M,p,mu. ∎

## 7. Endpoint adaptation conclusion and limits

Define the endpoint comparison value

    Gamma_end(K,M)=inf_A max{
      sup_(D_2(0)) L_A/g,
      sup_(D_2(1)) L_A/i},

where the infimum is over a single beta-blind complete-history algorithm,
possibly randomized with a source-independent seed. Both denominators are
strictly positive at every finite K,M. The accepted endpoint lower bounds
apply to each such fixed algorithm, while ALG is admissible. Thus

    1/(32 sqrt(6)) ≤ Gamma_end(K,M) ≤853                     (7.1)

for all K≥2,M≥1. The upper is the new endpoint adaptation conclusion, not an
optimal numerical constant. The lower is inherited and merely records that
the normalized benchmark is nonzero; no new adaptation lower bound is claimed.

This does not prove that ALG automatically attains the stationary a rate,
the S019 H rate, or the S011 F rate at every beta in Ω_closed. The general
pathwise guard adds g, which can be larger than these smaller benchmarks.
Likewise (SM) is established only for IID transition tables; its proof does
not transfer to beta<1 merely by writing delta=1−beta. No full-domain or
Ω_closed-wide adaptation assertion is made.

## 8. Failed shortcuts and why the bridge is substantive

1. **Original rule alone:** S005's accepted separation already rules out its
   universal IID optimality; repeating that fact would not answer Goal B.
   Here the output is a new observable choice of the two existing rules.
2. **Pooling alone or a fixed positive pooled fraction:** take K=2 and
   theta_ab=delta_(1−b), initialized at (0,1), so the symbols alternate.
   For even M, pooled add-one is exactly (1/2,1/2), while the actual target
   is a point mass. Its TV risk is 1/2 as M→∞, although g→0. A fixed convex
   mixture λ b+(1−λ)q with any constant λ>0 has risk≥λ/2 on this deterministic
   path, since the target's wrong-coordinate mass includes λ/2. Thus such a
   fixed positive pooled weight is not a general-rate solution. This is only
   a failure of that restricted choice, not an all-algorithm obstruction.
3. **Square a first-moment bound:** E e≤Ca does not imply E e²≤C²a². For
   bounded loss only E e²≤E e follows automatically. Such a bound would
   leave an inadequate rejection tail after division by g. Section 4 proves
   the needed squared-risk inequality from the actual data experiment.
4. **Treat original adaptive row counts as conditionally IID:** not used.
   The only conditioned multinomial calculation is for nonoverlapping IID
   triples at a fixed row, with endpoint independence proved from disjoint
   symbol sets. The four deleted departures are restored pathwise.
5. **Use independent validation or random-time regret:** neither is present.
   Test TV(q,b) is a function of the actual history. Inequality (6.1) is
   deterministic and keeps the original terminal target.
6. **Ignore arbitrary initial pair at beta=1:** not used. Only transition
   outputs are IID; first two departures can be contaminated by arbitrary
   initial symbols, and those departures are among the four restored terms.


It checked 155 exact binomial cases, 35 local multinomial cases, 168 exact
IID experiments over 13,886 positive-probability complete histories, 13,468
interior decompositions, 40,404 restoration inequalities, 42,158 guard
inequalities, and 9,996 finite horizon comparisons. Point initializations
include pairs outside a sparse p's stationary support. Exact calculations
use rational arithmetic.

Seeded IID simulations at (K,M)=(2,511) and (3,3887) exercised the g<1 regime;
all their tested histories selected pooling. A deterministic alternating
source at (2,512) exercised the original-row rejection branch. These are
supplemental implementation/arithmetic checks, not a universal proof and not
an independent mathematical review. No simulation is a premise of the
symbolic argument.


The precise next bridge is **near-IID at arbitrary initialization**: for
D_2(beta), S006's q=2 structure supplies a hidden all-row center within
radius delta=1−beta, and its pooled martingale mean bound is valid for any
mu. To extend the present selector one needs a valid local error/tail or
comparison bound beyond exact IID, strong enough that the selection
remainder is controlled by F=max(i,min(delta,a)), not merely g. The IID
triple independence in Section 4 is unavailable there; it must be replaced
by a proved dependent-path argument, not assumed.

A second, connected formulation is a multiscale observable guard over the
original, pooling and deterministic suffix rules with a theorem comparing
its risk to the **minimum of all applicable accepted closed-region scales**
for the same K,M,beta. This is not obtained by choosing a new algorithm
separately for each beta. The immediate question is whether a guard scale
can shrink from g to the relevant oracle scale while retaining the
arbitrary-source safety inequality. No such extension is claimed here.


