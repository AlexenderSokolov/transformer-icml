# 032 REL-V-BANK-JOINT-K — complete finite proof

Obligation: 02da4576308aa8b8abc12ded4c285018a0c3ef4375f713b027fde13927e15fff.
The frozen statement is outputs/032-v-bank-joint-k/lead/frozen-statement-v1.md,
SHA256 7311bf5eca3b4800d0da5a9e292ed8299c224856137f7016ffe0ebf64e15ab64.
The native exact statement is byte-identical to that file (9476 bytes).
This proof addresses its entire conjunction, including the finite source,
fault kernel, risk bounds, sequence equivalence and preservation of costs.

## 0. Imported premises and scope

The only direct mathematical Fact predecessors are:

* SRC fef8372728290b45, Evidence
  e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505:
  the actual Pi program, positive V bank, coordinate error and full costs.
* 016 a53804d650803060, Evidence
  fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88:
  add-one actual risk at most min(1,48T), its real-threshold TRUNC,
  and the original Pi joint-fault upper bound.
* MM5 946d42d5bf502eb4, Evidence
  aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82:
  every common full-history probability predictor has some homogeneous
  source and initial law with actual risk at least 2^-16 min(1,T).

These are admitted premises in their own scopes; their proofs and old
dependencies are not changed. The source-writing in sections 2–3 of
outputs/030-anchor-joint-k-high-kappa/prover/high-kappa-proof-v1.md is
reused and fully proved below in the new range. No 030 CLOCK/PARTIAL
or anchor-phase result is imported. Neither 031 nor any Dot result is
a premise. Finite diagnostics accompanying this proof are not premises.

Fix arbitrary integers K>=22, M>=1, D>=0 and h>=h_N, where
    h_N=ceil(log2(128(K+1)(M+3)^3)), Q=2^h.
Write N=M+2 and n_tok=M+3. The observation is the complete X_1^N,
Y_i=(X_(i+1),X_(i+2)), with counted departures 0<=i<M. The target is
theta_(Y_M), from that same trajectory. Every source theta is a fixed
homogeneous second-order probability table, with legal pair shifts,
possibly zero entries and arbitrary initial pair law mu. Counts are
    C_c=sum_(i=0)^(M-1) 1{Y_i=Y_M, X_(i+3)=c}, J=sum_c C_c.
All K coordinates are included, and p_c^+=(C_c+1)/(J+K).
Set T=K^(5/2)/sqrt(M+1) and eta=D/Q. Here TV(p,q)=||p-q||_1/2,
Psi(0)=0, Psi(x)=x(1+ln(1/x)) for 0<x<1, and Psi(x)=1 for x>=1;
all logarithms in Psi and harmonic bounds are natural logarithms.

We use exactly SRC-Pi, not the anchor program. Before the cut all
computation is clean. Its actual bank satisfies, for every history,
    V in {1,...,2Q}^K, |V_c-Q(C_c+1)/M|<=78.                 (0.1)
After the cut the original suffix recomputes S_W=sum_c W_c, outputs
floor(Q W_c/S_W)/Q for c<K-1 and gives the last coordinate the residual.
It sees only W and the originally retained exact public/query/endpoint/
flag bits. It cannot reread clean V, old sums, quotients, scratch or history.
The supremum R below is precisely R_V^Pi from the frozen statement:
first a homogeneous source and mu, then a legal common Markov kernel
with pointwise positive-bank and L1-budget constraints. A kernel may
use only the permitted observed data and source-independent seed.
The source can depend on public parameters, but not secretly change
with the realized path. The loss is total actual TV, not excess loss.

## 1. Legal precision and the full upper bound

Let A_prec=128(K+1)(M+3)^3. This is an integer at least 16 and at least
2M. Hence h_N>=max(4,ceil(log2 M)+1)=h0, Q>=2M and Q/8 is an integer.
We will also use the stronger consequence
    Q>=A_prec>78KM, so epsilon_V:=78KM/Q<1.              (1.1)
Indeed (M+3)^3>=M and 128(K+1)>78K. These facts hold for every allowed
h, with no upper restriction on h, including M=1.

For completeness, the normalization in the 016 specialization uses
the true J. Put V_c^*=Q(C_c+1)/M, so sum V^*=Q(J+K)/M. For any legal
kernel outcome W, (0.1) and the pointwise budget imply
    ||W-V^*||_1<=D+78K.
For positive vectors u,v, adding and subtracting u/(sum v) gives
    TV(u/(sum u),v/(sum v))
       <=min(1,||u-v||_1/(sum v)).
This follows because |sum u-sum v|<=||u-v||_1. The ordered output
changes W/(sum W) by TV at most (K-1)/Q. Thus, pathwise,
    TV(Pi^T,p^+) <= (K-1)/Q
        +min(1,M(78K/Q+eta)/(J+K)).                     (1.2)
No averaging of the edit constraint or independence of the kernel
and J was used. Kernel randomization leaves the pre-cut source law
and the true counts unchanged.

The add-one risk and real-threshold TRUNC from 016 applied to (1.2)
(equivalently, its joint-fault bound with delta=gamma=0) give
    R<=min(1,48T+(K-1)/Q
        +Psi(K^4 M(78K/Q+eta)/(M+1))).                 (1.3)
TRUNC allows every nonnegative real threshold, so D=0, J=0 and
nonintegral normalized budgets need no exceptional rounding assumption.
There is no master error or bad-event term in this experiment.

For z>=0 the elementary integral identity
    Psi(z)=integral_0^1 min(1,z/t) dt
shows monotonicity and subadditivity: the integrand at z_1+z_2 is at
most the sum of the two integrands. Also Psi(z)<=2sqrt(z). For 0<z<1,
put v=ln(1/z); then Psi(z)/sqrt(z)=(1+v)exp(-v/2)<=2, since its maximum
is 2exp(-1/2); z=0 and z>=1 are immediate.
Consequently, using Q>=2M,
    Psi(K^4 M(78K/Q+eta)/(M+1))
       <=Psi(39T^2)+Psi(K^4 eta)
       <=2sqrt(39)T+Psi(K^4 eta).
Moreover (K-1)/Q<=T: use Q>=2M, sqrt(M+1)<=2M for M>=1, and
K-1<=K^(5/2). Since 49+2sqrt(39)<63<64, (1.3) proves
    R<=min(1,64T+Psi(K^4 eta)).                         (UPPER)
This upper bound holds uniformly over every permitted kernel and
source, including budgets exceeding the maximal bank distance.

## 2. Statistical lower bound and the nontrivial source range

The identity kernel is legal for every D. The clean Pi is a common
full-history probability predictor, so MM5 gives
    R>=2^-16 min(1,T).                                 (STAT-LOW)
The witnessing source need not be the clock source below. We will
combine their supremum lower bounds by max, never as one-source sums.
If T>=1, STAT-LOW already implies the claimed 2^-80 capped lower bound.
For the remaining source construction assume T<1. Integer M then
satisfies M>=K^5, since M+1>K^5.

Put a=floor((K-6)/4), P=a^2, L=P+5, m=floor(M/L), and U=a^2 L.
For K>=22 we have a>=4 and
    4a+6<=K<=4a+9<=8a, so K/8<=a<K/4.
In particular L<=K^2 and M/L>=K^3; hence m>=4. We shall use
    K^4/4096<=a^4<=U<=K^4,                            (2.1)
    U(K+1)/M<=2K^5/M<=4K^5/(M+1)=4T^2.               (2.2)
The last comparison uses M+1<=2M. These are elementary finite bounds,
not assumptions about aligned horizons or a concentration regime.

## 3. Explicit homogeneous source and full observed path law

Partition 4a symbols into the disjoint groups
    A={0,...,a-1}, B={a,...,2a-1},
    C={2a,...,3a-1}, Dgrp={3a,...,4a-1}.
Use six further distinct symbols
    (p0,q0,p1,q1,xi,zeta)=(4a,4a+1,4a+2,4a+3,4a+4,4a+5).
All belong to {0,...,K-1}. In particular
    p1=4a+2<=K-4<K-1, and p1!=0.                       (3.1)
The group Dgrp is unrelated to the integer edit budget D.

There exists a finite word w_0,...,w_P with w_0=w_P=0 such that its
P consecutive ordered pairs enumerate all a^2 ordered pairs once,
including loops. To prove existence, use the complete directed graph
on a vertices, with one edge per ordered pair. Every vertex has equal
in- and out-degree a. Starting at 0, follow unused outgoing edges
until no such edge remains; balance forces this trail to close at 0.
If unused edges remain, connectivity gives a vertex on the existing
closed trail with an unused outgoing edge (otherwise all outgoing
edges from its vertex set were used, preventing unused vertices or
edges outside it in this complete graph). The same balance argument
produces a further closed trail there. Splice it into the first one.
Each operation uses additional edges and at most a^2 edges exist, so
after finitely many operations the resulting closed trail uses all
edges exactly once. Choose the lexicographically first resulting word
among all such finite words. This makes the source fully specified.
Write w^0=w and w^1=w+a coordinatewise.

Define the following second-order rows, with unmentioned rows delta_0:

* For s=0,1: (p_s,q_s)->w^s_0, (q_s,w^s_0)->w^s_1,
  and (w^s_i,w^s_(i+1))->w^s_(i+2) for 0<=i<=P-2.
* The last A pair (w^0_(P-1),w^0_P)->xi,
  (w^0_P,xi)->zeta, and
  (xi,zeta)->(1-1/m)delta_p0+(1/m)delta_p1.
  For s=0,1 put (zeta,p_s)->q_s.
* The last B pair (w^1_(P-1),w^1_P)->Unif(C).
  For every c in C, (w^1_P,c)->Unif(Dgrp).
  For c in C,e in Dgrp, (c,e)->p1; for e in Dgrp, (e,p1)->q1.

Every displayed row is a probability law. The internal ordered pairs
are distinct by the Euler-word property, and the last internal pair
is excluded from the earlier deterministic assignments. The two
internal alphabets, the two query alphabets and the six markers are
disjoint. Thus the remaining displayed cross-group and marker rows
are distinct and do not conflict with internal rows or one another.
Every step from (x,y) appends a symbol z and moves to (y,z), the required
legal shift. This is one fixed homogeneous table depending only on
K,M. It does not use time, an adaptive hidden label or future samples.

To specify the initial pair, introduce the A stay-circle pairs
    y0=(p0,q0), y1=(q0,w0),
    y_r=(w_(r-2),w_(r-1)) for 2<=r<=P+1,
    y_(P+2)=(w_P,xi), y_(P+3)=(xi,zeta),
    y_(P+4)=(zeta,p0).
This list has L pairs and its gate has phase P+3=L-2. It is used only
to name the initial pair, not to make the observed gate deterministic.
Let d=M-mL, 0<=d<L, k=(L-2-d) mod L, and mu=delta_(y_k).
All observed gates retain their genuine probabilities 1-1/m and 1/m.

From (p0,q0), a stay circuit emits
    w_0,...,w_P,xi,zeta,p0,q0
in exactly P+5=L steps. The activation route replaces its gate output
p0 by p1 and the next output q0 by q1. A B circuit from (p1,q1) emits
    w^1_0,...,w^1_P,c,e,p1,q1
in exactly L steps, where c and e are the two uniform choices.
The B query (c,e) has phase L-2 relative to (p1,q1). Consequently a
gate activated at time t is followed by the first B query at t+L,
and later queries are separated by L steps.

Starting at y_k, the first gate departure is d: the nonnegative
forward phase distance from k to L-2 is exactly d. Until activation,
the observed gates occur at d+tL for t=0,...,m-1. The terminal slot
M=d+mL is the next gate if never activated, or a B query if activated.
It is not a counted departure. If d=0, the gate at departure 0 is
random and must be included in the path probability. If d=L-1, then
k=L-1 and the initial pair is (zeta,p0); its next symbol is q0.
This is a legal prescribed initial pair. No unobserved earlier gate
or stay probability is charged to it.

For 0<=j<=m-1, let A_j denote first activation at the gate with index
m-j-1. Before the terminal slot there are then exactly j B queries.
The activation event has probability
    p_j=(1/m)(1-1/m)^(m-j-1)>=1/(4m).                  (3.2)
Here is a finite verification of the lower bound. With r=m-1>=1,
    (1+1/r)^r=sum_(i=0)^r binom(r,i)/r^i
        <=sum_(i=0)^r 1/i! <3<4.
The bound by 3 follows by bounding the tail starting at i=2 by
sum_(i=2)^infinity 2^(-(i-1)), with a strict inequality in the tail.
Invert this estimate, and note that smaller exponents of 1-1/m have
larger values. This proves (3.2).

More precisely, fix A_j and a sequence of j+1 ordered choices in
C x Dgrp. Starting at the specified initial pair, all other observed
transitions are forced: the initial A residue, the preceding stay
gates, the activation gate, the intervening clocks, and every return
from a B query. There is exactly one full observed history for this
specified sequence. Its probability is
    p_j a^(-2(j+1)).                                  (3.3)
Both symbols of the final query are observed by time M; its outgoing
symbol at departure M is not observed or counted. Histories from
different choice sequences or activation indices differ at an observed
symbol, so summing (3.3) also verifies the stated activation masses.
This is a calculation of the full observed path law, retaining every
symbol of the initial residue and all M departures.

It follows from (3.3) that, conditionally on A_j, the j old queries
and the actual terminal query are iid Unif(C x Dgrp). Conditioning
further on any terminal pair z in that set leaves the j old choices
iid uniform. There are no other occurrences of a C x Dgrp pair:
the A prefix contains neither group, and every intervening B segment
uses only B symbols, markers and the two displayed choices. Therefore
    J | (A_j,Y_M=z) ~ Bin(j,1/a^2),
    C_p1=J, C_c=0 for c!=p1, theta_(Y_M)=delta_p1.     (3.4)
In particular C_0=0. This conditional iid assertion is derived solely
from (3.3); it is not asserted for arbitrary Markov row counts. No
history was deleted and no independent test query was appended.

## 4. A globally legal kernel and the actual bank loss

Let d_edit=min(D,Q/8) and eta_0=d_edit/Q=min(eta,1/8).
For every history, define the same deterministic kernel as follows.
If the actual query belongs to the publicly specified C x Dgrp, set
    W_0=V_0+min(d_edit,2Q-V_0), W_c=V_c for c!=0;
otherwise set W=V. The increment is a nonnegative integer at most D,
and all coordinates remain in {1,...,2Q}. Hence the kernel satisfies
the budget and positive-bank constraints on every possible history,
including histories outside the support of the constructed source.
It needs only K,M,h,D, the actual query and the current V. It does
not inspect J, true counts, theta, mu, future data or a private seed.
In particular it is one admissible common Markov mapping, not a
choice made after secretly identifying the source or path probability.

On the constructed source whenever Y_M belongs to C x Dgrp, (3.4)
and the actual SRC error (0.1) show
    V_0/Q <= 1/M+78/Q < (1+1/K)/M <= 3/2,            (4.1)
where (1.1), M>=1 and K>=2 suffice. Therefore
    V_0+Q/8 < (13/8)Q <2Q.
The capacity limit never truncates d_edit on these histories. Thus
the exact actual increment is d_edit. This uses the genuine finite
V bank, not a substituted ideal count vector.

Let S=sum_c V_c. Summing the K separate SRC errors gives
    S<=Q(J+K)/M+78K.                                  (4.2)
All K positive add-one contributions remain in this inequality.
The true label p1 is different from 0 and is not the residual output
coordinate by (3.1). Its actual output q_p1 is consequently
    q_p1=floor(Q V_p1/(S+d_edit))/Q
          <=V_p1/(S+d_edit).
The resulting distribution q has TV(q,delta_p1)=1-q_p1, so
    TV(Pi^T,delta_p1)
       >=(S-V_p1+d_edit)/(S+d_edit)
       >=d_edit/(S+d_edit)
       >=eta_0 M/(J+K+78KM/Q+eta_0 M)
       >=eta_0 M/(J+K+1+eta_0 M).                    (4.3)
The direction of the target-coordinate floor helps this lower bound;
there is no need to lower bound the wrong-label output after its floor.
This reasoning includes the residual mass and all K bank coordinates.
For d_edit=0 the claimed lower term is zero, with all denominators
positive. We have bounded the total loss, not its difference from
clean loss, and have used no lower bound on such an excess.

## 5. Conditional Jensen and a finite harmonic lower bound

Let A_edit=eta_0 M and B_edit=K+1+A_edit>0. Given A_j and Y_M=z,
the function x -> 1/(B_edit+x) is convex on x>=0. By the finite
conditional law (3.4), Jensen's inequality applied to (4.3) yields
    E[TV | A_j,Y_M=z] >= A_edit/(B_edit+j/a^2).
For A_edit=0 this is the same zero lower bound. The estimate is
uniform in z; (3.3) justifies summing over all terminal choices.
Using (3.2) and nonnegativity of loss on unactivated histories gives
    R_clock:=E_source TV(Pi^T,theta_(Y_M))
      >= A_edit/(4m) sum_(j=0)^(m-1) 1/(B_edit+j/a^2)
      >= A_edit a^2/(4m) ln(1+m/(a^2 B_edit)).        (5.1)
The last step uses the decreasing positive function
t -> 1/(B_edit+t/a^2): its left-endpoint rectangles on [0,m] dominate
its integral. Thus the j=0 term and the finite upper limit are both
retained. There is no infinite-horizon approximation.

Since m=floor(M/L), we have M/m>=L. Also M/L>=4, so
m>=M/(2L). Substituting these two bounds in the two nonnegative,
increasing factors of (5.1) gives the all-residue source bound
    R_clock >= eta_0 U/4
        *ln(1+M/[2U(K+1+eta_0 M)]), U=a^2 L.        (HARMONIC)
This bound has been proved for every T<1, every permitted h and D,
with all initial residues and the actual 78K total bank error paid.
It uses no high-kappa, aligned-horizon or concentration assumption.

## 6. Scalar comparison, saturation and max of source risks

Put x=K^4 eta_0, z=eta_0 U and b=U(K+1)/M. Equations (2.1)–(2.2)
turn HARMONIC into
    R_clock >= (z/4) ln(1+1/[2(b+z)]),
    x/4096<=z<=x, 0<b<=4T^2.                        (6.1)
The identity
    Psi(K^4 eta_0)=Psi(K^4 eta)                      (6.2)
holds for every D. If eta<=1/8 it is immediate. Otherwise K^4/8>=1
for K>=22, so both arguments have Psi value 1. Thus the capped kernel
budget already suffices for arbitrarily large budgets; it remains a
member of every larger legal budget class. Nothing assumes D is less
than the maximal possible distance between two banks.

Continue to assume T<1. If x<=T^2, then
    Psi(K^4 eta)=Psi(x)<=2sqrt(x)<=2T.
Consequently STAT-LOW implies
    R>=2^-16 T
      >=2^-18 min(1,T+Psi(K^4 eta)),                 (6.3)
because the last capped expression is at most 3T. This branch includes
D=0, without any attempted positive clock lower bound for zero budget.

If x>T^2, then x>0 and b+z<5x. Therefore (6.1) yields
    R_clock >= x/(4*4096) ln(1+1/(10x)).             (6.4)
For every real x>0 the elementary inequality
    x ln(1+1/(10x))>=Psi(x)/11>=Psi(x)/16           (6.5)
holds. For x>=1, use ln(1+t)>=t/(1+t) with t=1/(10x):
the left side is at least 1/(10+1/x)>=1/11, while Psi(x)=1.
For 0<x<=1 write v=ln(1/x)>=0 and f(v)=ln(1+exp(v)/10).
Then f(0)=ln(11/10)>=1/11 and f'(v)=exp(v)/(10+exp(v))>=1/11.
Integration gives f(v)>=(1+v)/11; multiplication by x proves (6.5).
Thus (6.4) gives
    R>=R_clock>=2^-18 Psi(K^4 eta).                 (6.6)
This pays both the logarithmic range and saturation, without changing
the decoder, experiment or loss.

At these same public parameters, STAT-LOW is also available, possibly
from a different source with the identity kernel. The order of the
suprema in R implies
    R>=max(2^-16 T,2^-18 Psi(K^4 eta))
      >=2^-19 (T+Psi(K^4 eta))
      >=2^-19 min(1,T+Psi(K^4 eta)).                (6.7)
This is a comparison of two lower bounds on the same supremum. It is
not an assertion that one source simultaneously realizes their sum.
For T>=1, STAT-LOW already gives 2^-16 times the capped target; for
T<1 use (6.3) or (6.7). In particular every case implies the requested
fixed, conservative lower constant 2^-80. Together with UPPER,
    2^-80 min(1,T+Psi(K^4 D/Q)) <= R_V^Pi(K,M,h,D)
       <=min(1,64T+Psi(K^4 D/Q)).                   (V-MATCH)
The larger intermediate constants above are only proof estimates,
not separate obligations or a claim of constant optimality.
M=1 and all other small horizons fall under the statistical case
whenever T>=1; no undefined m-dependent source is used there.

## 7. Exact sequence consistency equivalence

Consider any public sequence K_n>=22, M_n>=1, integer h_n>=h_N(K_n,M_n)
and integer D_n>=0, with Q_n=2^h_n. Let T_n=K_n^(5/2)/sqrt(M_n+1)
and y_n=K_n^4 D_n/Q_n. If T_n->0 and y_n->0, UPPER and
Psi(y_n)<=2sqrt(y_n) imply R_V^Pi(K_n,M_n,h_n,D_n)->0.
Conversely, convergence of these risks to zero and V-MATCH imply
min(1,T_n+Psi(y_n))->0. Since the summands are nonnegative, the
uncapped sum eventually tends to zero, hence T_n->0 and Psi(y_n)->0.
The elementary inequality Psi(y)>=min(1,y) implies y_n->0. Therefore
    R_V^Pi(K_n,M_n,h_n,D_n)->0
       iff T_n->0 and K_n^4 D_n/Q_n->0.              (SEQUENCE)
This is worst-legal-kernel mean consistency for the fixed Pi and the
specified final V cut. Different parameters or the two necessary terms
may have different witnessing sources. It is neither a single-source
all-parameter claim, a uniform almost-sure result, an excess-risk claim,
nor a sharp necessity statement for arbitrary replacement decoders.

## 8. Same realized SRC program and complete costs

The statistical denominator M+1 is distinct from n_tok=M+3. The true
SRC word parameter is p=4h+4ell+64, ell=ceil(log2(M+K+4)). None of
the analytical counts, J, source clocks or source parameters is supplied
to Pi or added to its interface. Nominal Pi retains its original six
heads, finite rational logs, separate full-score evaluation, head floors,
positive-bank construction and ordered output. The bank error used
above is the admitted finite-program bound, not an ideal real softmax
or a new count decoder. The downstream total and quotients are recomputed
from W as stipulated, with no backup of clean V or history bypass.

We keep SRC's dense/uncached batch hybrid, at all n_tok positions.
The following are the same previously proved construction upper bounds,
with absolute constants, and are not new measurements:

| Resource | Preserved SRC bound or structure |
|---|---|
| neural depth / width | O(Kp^2) / O(Kp) |
| total heads / maximum per layer; maximum QK dimension; score cap | 6 / 4; 2K; 2 |
| each online coefficient and full arithmetic word | at most 128p bits, including products, remainders, guards |
| dense coefficient slots / parameter bits | O(K^3 p^4) / O(K^3 p^5), including zero slots and bias |
| active gates/projections / identity holds | O(Kp^2+K^2) / O(K^2 p^3) |
| alternative sparse program/coefficient/address/holds format | O(K^2 p^4) bits, not substituted for dense work or storage |
| masks / position metadata | O(n_tok^2+n_tok log(n_tok+1)) bits |
| observed input | O(NK) one-hot bits, or paid binary acquisition/conversion |
| rolling work arrays only | O(n_tok Kp^2) bits |
| uncached finite attention bitwork | O(n_tok^2 (K+p)p^2) |
| dense pointwise and QKV bitwork | O(n_tok K^3 p^6) |
| rational log generation / scratch | O(p^3 log^2(p+1)) / O(p log(p+1)) |
| finite arithmetic evaluator code | O(p^4) bits |

All input/query/actual-endpoint acquisition, QKV projections, masks,
residual copy, holds and clears, full products/remainders/guards and
output arithmetic remain charged. The smaller rolling-work bound is
not a total peak; dense and sparse alternatives and cached/uncached
work cannot be mixed by selecting their cheaper entries.

The offline package includes layout for K,N,h, masks/positions,
microcode and all actual-format gate/term/hold records. For actual
record counts G_rec,T_rec,I_hold, keep the original assembly bounds
O((G_rec+T_rec+I_hold)p^2) bitwork and O((G_rec+T_rec+I_hold)p) working
bits. Writing dense coefficient bits, including zeros, is charged.
For every phase, sum all simultaneously live program/parameter,
input, mask/metadata, QKV, residual, bank, address/controller,
temporary and output bits. The total peak is the maximum of those
phase sums. Any separate PURE expansion keeps its own SRC costs;
it is not identified with the smaller hybrid dimensions here.

The fault kernel defines an information-level perturbation experiment.
If an injector or protector is physically implemented, its selection,
data movement, storage and program costs must be added. The source
and kernel proof does not make these free nominal Pi operations.
There is no new decoder, count table, snapshot, cache, suffix/pooling
port or history reread, and no claim of equal-budget advantage or
optimal physical correction. No compiler, literal ledger, batch
measurement or profile was run. [Non-scientific operational metadata omitted.]
are both zero, consistent with the current budget policy.

## 9. Conjunction and preserved boundaries

Sections 1–7 prove all finite cases of the frozen V-MATCH, the explicit
all-residue homogeneous source and its full-history path law, the
legal actual-bank injection, its finite harmonic bound, the statistical
max combination and SEQUENCE. Section 8 preserves the same actual SRC
implementation and its complete charging. The only direct Fact
predecessors are SRC,016,MM5, as listed in section 0.

The range remains K>=22 and h>=h_N. No extension to h0-only precision,
K<22, master perturbations, conditional source classes or arbitrary
decoders is claimed. The earlier binary cut information lower bound,
general master joint-K reliability, physical correction and genuine
resource comparisons retain their own unresolved scopes. The small-K/
low-kappa gaps of 030 and the two 027 method obstacles are unchanged.
The accepted 031 and all old roots/Fact dependencies are untouched;
029 stays OPEN/PARKED, 021 closed, 022 OPEN/PARKED, and all previous
[Non-scientific operational metadata omitted.]
Dot's further statistical work remains exclusive to Dot; the absence
of a registered Dot delivery endpoint is a separate recorded coordination
obstacle, not a premise or mathematical obstacle of this proof.
This single conjunction is submitted through the normal independent
gateway. Its acceptance does not declare the v10 mother problem solved.

