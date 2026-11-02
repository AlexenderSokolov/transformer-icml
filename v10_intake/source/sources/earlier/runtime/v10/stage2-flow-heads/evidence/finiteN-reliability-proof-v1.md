# Finite-history prediction and located grid reliability of the original D3 decoder

Fixed version v1, 2026-10-25. Contract
22e80d3d620c36cfc0bbd297101a5efabe634d7fd696b4cae200963af52af02a.
Exact obligation af879858f3020c501dff7a366f8e1cfdcda36eb6a8c4f2a79fa1af839eb41390.
This proof is submitted for independent native review; the document does not
admit itself. Its two native predecessors, and only admitted prerequisites, are:

* C1 Fact b2f4d10fa0a69e00, Evidence
  15df56a560e38b8bb7fc84382d374a1e31298a0463efdbde0ab5e20f044291f3;
* count-snap Fact bcd4541db2cf4c1a, Evidence
  f652dccd9b59f4953ab3a0939081d221dede8640e1e8615398b6aba5d00e5b87.

Both were read back as VALID/PASS before this work. The Lead and old Counter
finite-N files are candidate derivations, not premises. Exact source hashes
are recorded in Section 12 and the companion manifest. [Non-scientific operational metadata omitted.]
request, model, session, counter, route, or campaign setting is changed.

## 1. Objects, finite family, and result

Throughout K>=2, N>=3, M=N-2, n=N+1. D1 means a stationary, strictly positive
second-order Markov law theta on {0,...,K-1}, with unknown transition vectors
theta_s for contexts s=(a,b). Set S_t=(X_{t-2},X_{t-1}), t=3,...,N, and

    n_s=sum_t 1{S_t=s}, C_s,c=sum_t 1{S_t=s,X_t=c}, u_s=n_s/M,
    c_s,c=C_s,c/M, E_N=(X_{N-1},X_N),
    p^+_N(c|s)=(C_s,c+1)/(n_s+K).

These counts are mathematical objects, not free predictor registers. Pi_{N,h}
is precisely the original finite predictor admitted in C1, not D3-snap. Put

    h>=max(4,ceil(log2 M)+1), Q=2^h,
    l_N=ceil(log2(N+K+2)), p=4h+4l_N+64,
    G_h={A/Q: A integer, 0<=A<=Q}.                         (1)

The C1 finite evaluator returns these closed-grid head coordinates with
ideal-coordinate error <=2/Q; its specified product/division truncations have
absolute error <1/Q. Its two local copying heads, four statistical heads,
fixed masks, actual endpoint access, query-independent values, finite log/exp
algorithm, clipping and final integer simplex program are retained. The
original output order is 0,...,K-1, with last-coordinate residual normalization.

We prove: one simultaneous random-visit event for general K; explicit source-
dependent occupancy/risk bounds and full resource substitution; a nonempty
correlated grid-error region for the original Pi; an actual integer P2-port
attack causing finite-N prediction failure of that specified decoder; and
an implemented, theta-independent intact-P1 replacement readout on an unknown
genuine second-order XOR family, with a compatible finite-N achievable bound.
We separately compose the admitted count-snap variants on the same sampling
event, retaining their own interfaces and costs. No universal decoder lower
bound, optimal resource claim, or closure of root C2 comparison/C4 is asserted.

The error model is specified fully in Section 5. In it delta bounds the TOTAL
change of a coordinate after clipping and re-storage in G_h, including any
re-encoding. It is not an unrounded real perturbation. All copies descend
from the same replaced master word. Exact queries, endpoint and binding bits,
constants, masks, and nominal finite arithmetic remain intact.

## 2. A single event with random context-visit counts

Write F_j for the observed history through X_j. For a fixed context s, let
T_1<T_2<... be its visits among t>=3. They are predictable: {T_j=t} is in
F_{t-1}. Almost surely they are all finite. One justification is C1's finite-
pair-chain ergodicity; alternatively apply the positive two-step bound in
Section 3 with ell=min_{s,c}theta_s,c>0. The successors X_{T_j} are iid with
law theta_s. Here is the needed justification, not an assertion of independence
from n_s. If Z is any bounded function of the first j-1 visited successors,
then Z 1{T_j=t} is F_{t-1}-measurable and

    E[Z g(X_{T_j})]
      =sum_t E[Z 1{T_j=t} E(g(X_t)|F_{t-1})]
      =(theta_s g) E Z.

Truncation/dominated convergence justifies the sum; induction proves the iid
claim. The random terminal count n_s depends on the same path and need not
be independent of these successors. We will union over possible visit counts.

We use the elementary bounded-range exponential inequality: for a centered
random variable of conditional range length d, its conditional log-mgf is
at most lambda^2 d^2/8. To see this, differentiate the log-mgf twice: its
second derivative is the variance under a tilted distribution on the same
interval, at most d^2/4; integrate twice using zero derivative/value at zero.
Conditional iteration then gives, for m bounded-range martingale differences
with range at most d, a two-sided tail 2 exp(-2m t^2/d^2) for their average.
This argument also proves the ordinary iid Hoeffding inequality used below.

For 0<alpha<1 define

    A_alpha=K log 2+log(2K^2 M/alpha),
    t_alpha(j)=sqrt(A_alpha/(2j)), j>=1.                  (2)

For each context s, subset A of the alphabet, and first j visited successors,
apply the preceding inequality with d=1 to their membership indicators.
Union over at most K^2 * M * 2^K choices. With probability at least 1-alpha,
on ONE event V_alpha, simultaneously for every s with n_s>=1,

    TV(C_s/n_s,theta_s)<=t_alpha(n_s),
    |C_s(A)/M-u_s theta_s(A)|<=u_s t_alpha(n_s) for every A. (3)

We used TV=max_A |p(A)-q(A)| on a finite alphabet. The union over subsets is
only a probability proof device, not a network with 2^K features. At n_s=0
the second difference in (3) is identically zero; the empirical probability
C_s/n_s is left undefined, not divided by zero.
More precisely, define V_alpha to be the F_N-measurable event that the
displayed observed-count inequalities hold. Its complement is contained in
the finite union of first-j-visit deviation events just bounded. The infinite
source extension is used to bound that union even if some first-j visits
occur after N; it supplies no future input to the predictor and does not
make V_alpha a future-data event. The event F in Section 7 is defined by
its observed-count inequalities in the same way.

Add-one is n_s/(n_s+K) times the empirical distribution plus K/(n_s+K)
times uniform. Since TV(empirical,uniform)<=1-1/K, on V_alpha its error for
n_s>=1 is at most

    S(j)=t_alpha(j)+(K-1)/(j+K), j=n_s.                   (4)

C1's implementation bound and Section 5's error ledger give, for any allowed
grid perturbation of radius delta, simultaneously for these contexts,

    TV(Pi^delta_{N,h}(s),theta_s) <= g_delta(n_s),
    g_delta(j)=min(1, S(j)+ KM(78/Q+36delta)/(j+K)+(K-1)/Q), j>=1,
    g_delta(0)=1.                                        (5)

For the original nominal predictor delta=0. At zero count, its IDEAL readout
is uniform; a finite recovered frequency can have small residual error, so
we do not assert that the original finite output is the exact dyadic uniform
program. Risk <=1 is valid there. The snapped variants have the explicit
dyadic uniform zero-count output, with error <=(K-1)/Q to uniform, but no
small unknown-theta risk follows merely from a zero count.

At common Q>=256M the count-snap predecessor proves, on every path, that
D3-snap and B-C-snap have identical finite outputs, with implementation TV
<= (K-1)/Q to p^+_N. On V_alpha both therefore satisfy

    TV(D3-snap(s),theta_s)=TV(B-C-snap(s),theta_s)
       <= g_snap(n_s),
    g_snap(j)=min(1,S(j)+(K-1)/Q), j>=1; g_snap(0)=1.      (6)

This new stochastic composition is proved by the preceding event and triangle
inequality, not imported from the deterministic Fact. Equation (6) does not
identify either variant with original Pi. The equality is only between the
two specified snapped outputs at a common grid and count order.

Additional joint statistics can be stated on the SAME event. If also
|u_s-pi_s|<=a_s for declared constants a_s, then for every subset A,

    |C_s(A)/M-pi_s theta_s(A)|<=u_s t_alpha(n_s)+a_s,      (7)

where the first term is zero at n_s=0. For the recovered clipped neural
coordinate a_hat_s,c, the right side for a singleton gains 76/Q+35delta.
For a subset it gains |A|(76/Q+35delta). The optional independently recovered
context frequency has |u_hat_s-u_s|<=28/Q+13delta (with its exact half guard).
These are joint-statistic statements for the same history, not independent
events for different heads or queries; all head errors may be correlated.

## 3. Occupancy, general nonuniform sources, and every requested risk

For a known source class theta_s,c>=ell, 0<ell<=1/K, set, when N>=6,

    m0=floor((N-4)/2), n0=floor(ell^2(N-4)/2),
    Bocc=min(1,2K^2 exp(-ell^2 m0/8)).                    (8)

The useful assertion below assumes n0>=1; otherwise use the trivial bound one.
For t=5,...,N, conditional on F_{t-3}, the two symbols forming S_t are
generated successively, so P(S_t=s|F_{t-3})>=ell^2. Split these indices into
the two parities, of lengths m1,m2, both at least m0 and totaling N-4.
For consecutive indices of one parity, the preceding indicator is measurable
in the next conditioning field F_{t-3}. For such m indicators with conditional
success probabilities >=q=ell^2, iterative conditioning gives

    E exp(-lambda sum Y_i)<=(1-q+q exp(-lambda))^m.

At lambda=log 2, Markov's inequality and log(1-q/2)<=-q/2 give
P(sum Y_i<=qm/2)<=exp(-qm(1-log 2)/2)<=exp(-qm/8), since log 2<3/4.
If neither parity fails, their total is strictly greater than q(N-4)/2,
hence is at least n0; the omitted visits t=3,4 only increase n_s. Union over
the two parities and K^2 contexts proves

    P(min_s n_s<n0)<=Bocc.                              (9)

This checks the conditioning, strict threshold and floors in the candidates.
Combining (3) with (9) produces ONE event of probability >=1-alpha-Bocc;
on it replace n_s by n0 in (5) or (6), since all displayed positive terms
decrease with j. Set G_delta=g_delta(n0), G_snap=g_snap(n0), and
b=min(1,alpha+Bocc).

A separate nonuniform version preserves actual pi_s and dependence. Let
d(k)=sup_y TV(P^k(y,.),pi) for the stationary pair chain P. For its context
indicators I_j, |Cov(I_0,I_k)|<=pi_s d(k). Thus, with

    D_M=1+2 sum_{k=1}^{M-1} d(k),
    Var(n_s)<=M pi_s D_M.                               (10)

Chebyshev and a context union give

    P(exists s: |u_s-pi_s|>a_s)
       <= B_mix=min(1, sum_s pi_s D_M/(M a_s^2)).         (11)

For 0<a_s<pi_s, the good event has
n_s>=ceil(M(pi_s-a_s)); intersect it with V_alpha, and (5)--(7) apply
with these possibly unequal context thresholds. In particular a_s=pi_s/2
gives B_mix<=min(1,sum_s 4D_M/(M pi_s)). The pi,d parameters quantify a
declared class/particular-law theorem; they are not secretly fed to a predictor.
A family-wide bound can use known lower bounds for pi and known upper bounds
for d. For every fixed strictly positive theta, C1's P^2 positivity supplies
geometrically decaying d(k), but there is no common rate over all such theta.

Here are explicit risk transfers, also without an occupancy hypothesis. On
V_alpha, put R_s=TV(Pi^delta(s),theta_s) and g_s=g_delta(n_s). Then R_s<=g_s
simultaneously. Consequently

    E R_s <=min(1,E g_s+alpha),
    E max_s R_s <=min(1,E max_s g_s+alpha),
    E R_{E_N} <=min(1,E g_{E_N}+alpha),
    E[R_{E_N}|E_N=s] <=min(1,E[g_s|E_N=s]+alpha/pi_s).    (12)

Stationarity gives P(E_N=s)=pi_s>0. The conditional bad-event bound is
P(V_alpha^c|E_N=s)<=alpha/pi_s; no independence of E_N and data was used.
For ANY nonnegative history-dependent weights lambda_s with sum one,

    E sum_s lambda_s R_s
       <=min(1,E sum_s lambda_s g_s+alpha).              (13)

This includes empirical visit weights n_s/M (zero-count terms then vanish),
stationary weights pi_s, fixed external queries and the actual terminal delta
weight. It specifies the weighting experiment instead of silently treating
an endpoint as a fresh independent query. Replacing g by g_snap proves the
same statements for the two snapped variants.

On an occupancy intersection with uniform bound G and bad probability b,
(12)--(13) simplify to expected max/fixed/actual-terminal/path-weighted risk
<=min(1,G+b), and conditional-terminal risk <=min(1,G+b/pi_s). If thresholds
differ, use their individual G_s in (12)--(13) and max_s G_s when needed.
For the ell class, (P^2)_{v,s}>=ell^2 implies pi_s>=ell^2. Conditional risk
therefore has the explicit class bound min(1,G+b/ell^2). A high-probability
statement is also immediate: each error and the maximum are at most G on
that one event. All formulas are valid for the true next-symbol conditional
law theta(.|E_N), not a fiction of independent terminal selection.

## 4. Explicit accuracy/resource choices for the ORIGINAL family

For a requested expected-risk target epsilon in (0,1), a convenient sufficient
class prescription is alpha=epsilon/4 and the following verifiable constraints:

    m0 >= (8/ell^2) log(8K^2/epsilon),
    n0 >= 8 [K log 2+log(8K^2M/epsilon)]/epsilon^2,
    n0+K >= 8(K-1)/epsilon.                              (14)

They give Bocc<=epsilon/4, t_alpha(n0)<=epsilon/4, and smoothing <=epsilon/8.
Choose the ACTUAL precision and working precision to be

    h_* = max(4,ceil(log2 M)+1,
              ceil(log2((8/epsilon)[78KM/(n0+K)+K-1]))),
    P_* = 4h_*+4ceil(log2(N+K+2))+64.                    (15)

Then implementation error is <=epsilon/8, good-event error <=epsilon/2,
and expected max/fixed/actual-terminal/weighted risk <=epsilon. These are
sufficient, not necessary or optimal, conditions; they can be met for every
fixed positive ell by taking N large. No access to n_s or theta is needed to
choose precision. To ensure conditional-terminal risk <=epsilon, replace the
bad-event budgets by alpha=epsilon ell^2/4 and Bocc<=epsilon ell^2/4, update
the logarithms in (14) accordingly, and keep the good-event target epsilon/2.
Alternatively use known pi/mixing class bounds from (10)--(11). For an
implementation-only target v one may always use the pathwise C1 choice
h>=ceil(log2((78M+K-1)/v)) in addition to its domain lower bound.

Here are the FULL functions with (15) substituted. For general requested h,
replace P_* by the explicit p in (1); no accuracy primitive remains implicit.
The convention is charged finite attention plus pointwise ReLU layers, exactly
as in C1. A constant factor 128P_* bounds activation/parameter words, with
full products retained and guard fractions; this is a storage allowance,
not a change of the admitted truncation operations.

| Resource of original Pi | Uniform upper bound after substitution |
|---|---|
| L, W | O(K P_*^2), O(K P_*) |
| Heads, QK dimension, score range | total 6, max/layer 4; 2K; at most 2 |
| Parameter/arithmetic bits per word | <=128P_* |
| Dense coefficient slots / bits | O(K^3 P_*^4) / O(K^3 P_*^5) |
| Nonzero arithmetic/projection gates before holds | O(KP_*^2+K^2) |
| Layer-spanning identity wires | O(K^2P_*^3) |
| Sparse program/parameter bits including addresses/holds | O(K^2P_*^4) |
| Stored positions/masks | O(n log(n+1)+n^2) |
| Rolling working bits excluding stored parameters/masks | O(n K P_*^2) |
| Finite attention bit operations | O(n^2(K+P_*)P_*^2) |
| Dense QKV/pointwise bit operations | O(n K^3P_*^6) |
| Offline finite log generation operations / scratch | O(P_*^3 log^2(P_*+1)) / O(P_* log(P_*+1)) |

Total dense stored bits add n^2+n log(n+1) to the dense parameter entry;
peak online bits add nKP_*^2 as well. The sparse format is separate and
uses its displayed addressed-program entry. A conservative O(P_*^4) bits
for finite arithmetic evaluator code fits both parameter bounds. Code/layout
generation, if charged separately, can explicitly write G=O(KP_*^2+K^2)
gates and I=O(K^2P_*^3) holds using O((G+I)P_*) scratch and
O((G+I)P_*^2) bit operations, plus writing the chosen stored format and masks.
This is a safe construction bound, not a cost-free compiler. The p^6 dense
term includes generic p-bit multiplication and cannot be lowered to p^5 by
assuming all weights are shifts. One query is run at a time; evaluating all
K^2 queries separately multiplies time/output storage accordingly.

For the variant comparison, the count-snap Fact retains D3-snap's separate
replacement block: w=h+ceil(log2(M+1))+ceil(log2(K+1))+8=O(p),
new arithmetic/depth O(Kw^2), live channels O(Kw), added holds O(K^2 p w^2),
dense slots O(K^3 p^2 w^2), bits O(K^3 p^3 w^2), and operations
O(nK^3 p^4 w^2), safely added to the old upper bound. Its total orders equal
the D3 table, with possibly larger constants; it is a different predictor.
B-C-snap pays F=K^3 features and statistical values F+1. In the admitted
layer-shaped dense layout its dense bits are O(F^2p+K^3p^5), sparse bits
O(Fp+K^2p^4), working bits O(n(F+Kp)p), attention operations
O(n^2(F+K)p^2), and dense operations O(n(F^2p^2+K^3p^6)), plus the same
positions/masks. Its L=O(Kp^2), W=O(F+Kp), total heads 3, max/layer 2,
D_qk=1, score range zero. Its wide feature phase ends before the narrow
arithmetic phase; padding all layers to W instead would cost
O(Kp^3(F+Kp)^2) dense bits and O(nKp^4(F+Kp)^2) dense operations.
Thus (6) is not a componentwise budget-dominance statement. The sufficient
nominal grids remain Q>=2M for B-C-snap and Q>=256M for D3-snap, together
with output precision (K-1)/Q. They never replace original Pi in Section 7.

## 5. Complete finite visible code, copies, and buffer lifetimes

Fix the following implementation schedule of the admitted family. At the
synthetic query q=N+1 there is no future token. The two paid singleton heads
copy l2_q=e_{X_{N-1}}, l1_q=e_{X_N}. The query one-hots A,B are selected by
the declared mode from either these or external e_a,e_b; actual endpoints
are retained independently. The query's original token slot is zero.

The persistent query-visible scalar banks at the statistical cut are:

| Bank | Coordinates |
|---|---|
| P1 | q1[0:K], v1[0:K] |
| P2 | q2[0:K], v2[0:K] |
| partial T | hvec[0:K], h0[0:K] |
| uniform | alpha[0:K], nu[0:K], f[0:K], rho |
| query/residual | A[0:K], B[0:K], external query banks, mode, zero x_q, zero F_q, z_q=0 |
| actual endpoint | l2_q[0:K], l1_q[0:K] and any exact declared copies |
| fixed metadata | K,N,M,h,p,Q, q index/type, word layouts, masks/positions and program constants |

Here [0:K] denotes K coordinates, not an extra endpoint coordinate. The four
statistical banks total 9K+1. Endpoint/query/flag BIT inputs are exact in this
model. The statistical flag outputs h0,f,rho ARE included among the possibly
perturbed scalars. Retaining all listed residual banks fits C1's 64K+32
pre-expansion scalar allowance and O(Kp) bit channels after expansion. Masks
and parameters are charged stored data; the readout does not acquire a new
data-dependent channel by knowing fixed constants.

There is one master word per statistical coordinate. Its output projection
is routing into a previously zero bank, not a residual sum with an old clean
copy. The perturbation acts after the finite quantizer returns that G_h word
and BEFORE any readout fanout or residual duplication. It replaces it by
another member of G_h at distance <=delta. All later copies, scalar or bit,
are exact copies of the replaced master; none bypasses the cut. Every bank
above remains visible, including intact P1, both v vectors and the entire
uniform/partial heads. The attack of Section 7 changes only q2's two next-
symbol coordinates. It does not remove intact information to manufacture
a lower bound. Additional independent corruptions of downstream copies,
arithmetic gates or endpoint bits are outside this located experiment.

The finite evaluator has real charged workspace, with these lifetimes:

1. Historical x,l1,l2,F and projected Q/K/V arrays live through the attention
   phase and are charged O(nKp^2) bits; masks/positions are separately charged.
   An edge uses finite score numerator S, exponential terms T_j, integer
   weight W, and product/quotient scratch, recycled after its accumulator
   update. A row retains denominator D and all value numerators A_c until
   its output divisions finish. These have the C1 O(p)-bit bounds.
2. Rows can be evaluated with the synthetic query last. As each final head
   bank is returned, all of that head's A_c,D,W, exponent terms, quotient
   remainder and projected-query temporaries are dead and overwritten with
   zero before its post-quantization port is exposed. In particular no
   clean q2 quotient, normalized copy, or exact P2 numerator survives that
   port. Query/global statistics are written only to their master banks.
3. When global attention is over, historical/projected arrays and unused
   historical outputs are dead; the final pointwise query decoder has only
   the enumerated query banks. They may be freed or zeroed; explicitly zeroing
   them takes O(nKp^2) bit operations, already dominated by the full forward
   bounds. Streaming scratch clearing is likewise included. This is a
   specified memory/readout interface, not a claim that any physically
   retained historical RAM is inaccessible without an access rule.
4. Original readout temporaries are selected U1,U2,alpha_b,nu_b and endpoint
   intersection bit; J[0:K]; d1,d2,dT; K coordinate products and signed
   initial/flow/difference values (which may instead be recycled serially);
   clipped a[0:K], rho floor r0, smoothing r; positive x[0:K], sum T;
   K output words and one integer division remainder/partial-product block.
   All copies are descendants of the master banks, or fixed constants/exact
   endpoint/query bits. Release scratch at its last use; retaining all masters
   throughout the readout still costs only O(Kp) live channels and O(K^2p^3)
   holds. No historical data or head-evaluator accumulator is a readout input.

Exact overwriting and designated lifetimes preserve the nominal predictor's
input/output function and fit its admitted cost upper bounds. A model allowing
arbitrary inspection of history or pre-erasure P2 accumulators is a DIFFERENT
experiment; the fixed-decoder result here is not promoted to that experiment.

## 6. Correlated grid propagation and a nonempty robustness region

In the preceding model each perturbed coordinate differs from its ideal head
value by eta=2/Q+delta. The nominal arithmetic still has zeta=1/Q; perturbation
rounding is already in delta and must not be counted as an unbounded real
input to grid extraction. Exact one-hot selection preserves eta. With
v=1-U/2 in [1/2,1] and numerator 1+lambda nu_b, direct subtraction of ratios
gives normalizer errors 6eta+zeta for d1 and 10eta+zeta for d2. The dT error
is eta. Since each head scalar is clipped into [0,1], the separate bounds are

    dT hvec-nu: 4eta+zeta; dT h0-f: 4eta+zeta;
    rho J: eta; flow g: 9eta+2zeta;
    d1 q1: 10eta+2zeta; d2 q2: 16eta+2zeta.

For example |hat dT hat h-dT h|<=eta+2eta, then the product rounding and
subtracted nu contribute zeta+eta. In a product d_k q_k use
|hat d_k-d_k| |hat q_k|+d_k |hat q_k-q_k|, with d1<=4,d2<=6, followed by
its rounding. The signed flow is exactly
g=dT hvec-nu+rho J-(dT h0-f), retaining BOTH initial and actual endpoint
corrections. Adding these errors recovers 35eta+6zeta, with no independence
assumption; the independent u diagnostic has 13eta+2zeta. Thus

    |a_hat_s,c-c_s,c|<=76/Q+35delta.                     (16)

Original smoothing uses r=max(hat rho,r0), r0=2^{-ceil(log2 M)-1}>0. Since
rho=1/M>=r0, |r-rho|<=eta. Its actual positive sum divisor is computed from
the clipped coordinates and r, not an independently estimated u_s. The
positive-vector normalization inequality
TV(x/sum x,y/sum y)<=||x-y||_1/sum y, applied to y_c=c_s,c+1/M, then final
integer simplex quantization, gives exactly

    TV(Pi^delta(s),p^+_N(s))
       <=KM(78/Q+36delta)/(n_s+K)+(K-1)/Q.               (17)

On all admissible perturbed inputs the original program remains legal:
head clipping preserves its denominator bounds, signed intermediate ranges
are the admitted [-16,16] allowance, r>0, and last-coordinate residual
normalization has nonnegative coordinates summing exactly to one. This
holds on bad sampling events too. Delta does not change the allowed grid
or the word range.

A genuinely nonempty grid robustness condition follows. For an implementation
budget v>0 on n_s>=n0, any radius satisfying

    1/Q <=delta <= ((v-(K-1)/Q)(n0+K)/(KM)-78/Q)/36      (18)

permits at least one nonzero grid step and guarantees the implementation
term <=v. A sufficient condition for this interval to be nonempty is
Q>=[114KM/(n0+K)+K-1]/v, in addition to (1). Arbitrary adaptive, query-
dependent and correlated replacements within the radius are allowed. This
is prediction robustness, not exact count recovery; with a positive occupancy
fraction its sufficient delta need not shrink as 1/M.

For clarity, the separate count-snap predecessor guarantees exact unchanged
output under M(76/Q+35delta_D)<1/2 for D3-snap and
M(1/Q+delta_B)<1/2 for B-C-snap (the nominal B-C case Q=2M has its own strict
floor proof). Outside those sufficient margins the variants remain legal,
but their recovered integers need not sum to M: each count lies in [0,M],
and their denominator is bounded by KM+K, not M+K. The predecessor's word
w and hold schedule pay for that bad-event bound. These are not noise lower
bounds for prediction and do not modify original Pi's readout or acceptance.

## 7. Actual post-quantization integer attack on the ORIGINAL decoder

Now K=2, N>=6, theta_s,c>=ell>=3/8. Fix a dyadic epsilon_a in (0,1/8]
and a tolerance t in (0,epsilon_a/8]. Assume n0 from (8) is positive.
For binary data one needs only the subset {0}; the visit argument in Section 2,
unioned over four contexts and j=n0,...,M, gives a single event F with

    P(F^c)<=B=min(1,8 exp(-ell^2 m0/8)+8M exp(-2n0 t^2)),
    on F: n_s>=n0 and |C_s,0/n_s-theta_s,0|<=t for all s. (19)

This is independent of neither the terminal query nor the attack, but neither
independence is needed. The event is a property of the original observed path.

Let A0,A1 be the NOMINAL integer numerators in the finite q2 bank at its
post-quantization, pre-fanout port. Compute the mathematical integer

    Z2=M+n_a. +2n_.b+2n_s, so d2=Z2/M in [1,6],
    k=min(floor(Q epsilon_a n_s/Z2),A1),
    (A0,A1) -> (A0+k,A1-k).                              (20)

This is the attack algorithm, not free predictor side information. For dyadic
epsilon_a=E/2^e, its floor is the integer quotient of Q E n_s by 2^e Z2.
The adversary is permitted to read the observed history and query, but not
theta or future data, and it supplies only the replacement q2 words to the
decoder. It scans the observed symbols to count n_s,n_a.,n_.b, keeping the
previous two symbols and three counters; it uses no full pair/triple table.
With w_A=h+e+ceil(log2(M+1))+ceil(log2(K+1))+10, all its integer products,
divisors and counts fit O(w_A) bits. Ripple counters/bit comparisons and
restoring division cost O(N(K+w_A)+w_A^2) bit operations and O(K+w_A)
working bits in addition to its input access. If it owns a retained copy of
the history, charge O(N log K) input-storage bits (or O(NK) for one-hot
storage). Its finite code is O(w_A^3+K w_A) addressed bits using unrolled
arithmetic and a fixed length-N scan control. Counts and Z2 die before the
readout; they never become decoder inputs. No counted operation is an oracle.

C1's head evaluator sums the bit next-symbol values using a common positive
denominator, then floors the two output ratios separately. Consequently
A0,A1>=0 and A0+A1<=Q, although the sum need not equal Q. The attack preserves
this original sum, and 0<=k<=A1 ensures both new coordinates lie in G_h.
Its magnitude is k/Q<=epsilon_a u_s/d2<=epsilon_a, and all other statistical
coordinates and their descendants are unchanged. There is no clean q2 copy
by the precise port/lifetime declaration in Section 5.

Assume additionally the finite support condition

    2/Q <= (ell-t-epsilon_a)n0/(6M).                     (21)

On F, the ideal q2,1 satisfies d2 q2,1>=c_s,1>=(ell-t)u_s. The nominal
finite A1/Q is at least q2,1-2/Q, hence by (21) at least epsilon_a u_s/d2.
Thus the minimum in (20) does not bind on F. Set a=epsilon_a u_s/d2. The
ideal reference vector q2^*=(q2,0+a,q2,1-a) lies in the simplex. The attacked
FINITE coordinate errors to this reference are at most 3/Q: 2/Q from the
nominal evaluator and less than 1/Q from integer k rounding. All other head
coordinates are within 2/Q, so one may use the common eta'=3/Q, zeta=1/Q.
This compares to an attacked reference code, not to another stationary law.

The reference normalizers and boundary terms are unchanged, and the exact
difference identity now yields

    c_s,0^*=c_s,0+epsilon_a u_s,
    c_s,1^*=c_s,1-epsilon_a u_s.                         (22)

Both are nonnegative on F, sum to u_s, and are at most 1. In particular
clipping is nonexpansive relative to them. Repeating the error argument of
Section 6 against this reference is legitimate: ideal q2^* is still in [0,1]
and (22) still has the required range and mass. It yields

    TV(Pi^attack(s),p^bad_N(s)) <= (114M+1)/Q,
    p^bad_N(0|s)=(C_s,0+1+epsilon_a n_s)/(n_s+2).         (23)

Indeed M(36eta'+6zeta)+1/Q=(114M+1)/Q. No final-output quantization lower
bound is used: the error in (23) is subtracted from a real finite-history
decoder bias. Reverse triangle inequality gives on F, for EVERY context,

    TV(Pi^attack(s),theta_s)>=L,
    L=[epsilon_a n0/(n0+2)-t-1/(n0+2)-(114M+1)/Q]_+.     (24)

To verify the smoothing term, write p^bad(0)-theta_s,0 as
epsilon_a n_s/(n_s+2)+[n_s/(n_s+2)](C_s,0/n_s-theta_s,0)
 +(1-2theta_s,0)/(n_s+2), and use monotonicity in n_s for the lower bound.
The clean original decoder on F has error at most

    Gclean=min(1,t+1/(n0+2)+(78M+1)/Q).                  (25)

Thus expected fixed-context, maximum-context, actual-terminal, and arbitrary
history-weighted attacked risks are at least (1-B)L; their clean upper bounds
are min(1,Gclean+B). Conditional-terminal attacked risk at E_N=s is at least
(1-min(1,B/pi_s))L, with the corresponding clean upper bound
min(1,Gclean+B/pi_s). These follow by integrating the SAME event, not by
separately sampling queries. The lower bound concerns precisely original
Pi's difference/clip/rho-smoothing/integer-simplex readout under (20).
Its truth does not require, and does not imply, that every decoder of the
entire surviving code fails. The next section constructs a contrary decoder.

## 8. Unknown genuine second-order XOR family and its martingale event

Identify symbols 0,1 with signs -1,+1. Consider the declared UNKNOWN family

    0<|tau|<=1/4,
    P_tau(Y=y|i,j)=(1+tau i j y)/2.                     (26)

Every transition is at least 3/8, and tau!=0 makes the dependence on the
second lag genuine (indeed both signs affect the transition). The uniform
pair law is stationary: the incoming mass to (j,y) is
sum_i (1/4)(1+tau i j y)/2=1/4. C1 uniqueness proves it is the D1 stationary
law here. This uniformity is proved only for (26), not assumed in Sections 2--4.

For the history triples let i_t=X_{t-2}, j_t=X_{t-1}, Y_t=X_t in signs, and

    A=M^{-1}sum_t i_t, Bm=M^{-1}sum_t j_t, Pm=M^{-1}sum_t i_t j_t.

The notation Bm avoids confusion with the bad-event probability B. Define
two martingale averages

    Z1=M^{-1}sum_t(Y_t-tau i_t j_t),
    Z2=M^{-1}sum_t j_t(Y_t-tau i_t j_t).

Their conditional ranges have length 2. For r>0,
P(|Z1|>r or |Z2|>r)<=4 exp(-M r^2/2) by the proved exponential lemma.
Shifting a list of M signs or products by one changes its mean by at most
2/M. Hence, on the complementary event,

    |A-Bm|<=2/M,
    |Bm-tau Pm|<=r+2/M,
    |Pm-tau A|<=r+2/M.                                  (27)

For u=|tau|<=1/4, substitute the last bound and |A|<=|Bm|+2/M into the
middle one. This gives (1-u^2)|Bm|<=(1+u)(r+2/M)+2u^2/M. It follows that

    |Bm|<=(4/3)r+14/(5M),
    |A|<=(4/3)r+24/(5M),
    |Pm|<=(4/3)r+16/(5M),

so each is at most 2r+5/M. These explicit constants check the candidate
elimination, rather than treating pair frequencies as population limits.

For query signs a,b and intact P1 define

    w_t=(1+1{i_t=a})(1+1{j_t=b}),
    H_s=(9Pm+3a Bm+3b A+ab)/4,
    T_s=d1(q1,+-q1,-).

Expanding w_t=(9+3a i_t+3b j_t+ab i_t j_t)/4 shows
H_s=M^{-1}sum_t w_t i_t j_t and T_s=M^{-1}sum_t w_t Y_t.
Consequently T_s=tau H_s+Z_s, where
Z_s=M^{-1}sum_t w_t(Y_t-tau i_t j_t) is a martingale average whose conditional
range is at most 8. Union over four queries gives
P(max_s |Z_s|>z)<=8 exp(-M z^2/32). If

    (15/4)(2r+5/M)<=1/8,                               (28)

then |H_s-ab/4|<=1/8 on (27), so every |H_s|>=1/8. On a SINGLE event X
of probability at least 1-B_X, where

    B_X=min(1,4exp(-M r^2/2)+8exp(-M z^2/32)),            (29)

these denominator bounds and |T_s-tau H_s|<=z hold for every query.
Neither this proof nor the upcoming decoder knows tau. It uses a source
class bound only to prove (27), and explicit finite sums instead of a
population identifiability or aliasing argument.

## 9. Fully finite intact-P1 replacement decoder and its cost

Keep the ENTIRE finite front end and complete visible banks of Section 5,
including attacked P2 and all unused intact coordinates. The replacement
reads only q1,v1,alpha,nu, query A/B and fixed metadata; actual endpoint
selects the query in terminal mode, as before. It is not given raw history,
counts, tau, evaluator numerators, or a clean P2 duplicate.

First consider the exact formulas it approximates. The uniform coordinates
give A=alpha_+-alpha_- and Bm=nu_+-nu_-. Select U1=v1,a. From the intact
P1 normalizer and lag2 mass,

    u_ab=d1 U1/2-alpha_a,
    Pm=ab(4u_ab-1-a A-b Bm).                            (30)

The second formula follows by expanding the empirical indicator for pair
(a,b): 4u_ab=1+aA+bBm+abPm. It recovers just a selected scalar moment;
no free table of all four contexts is provided. H_s,T_s are then the
expressions of Section 8.

The FINITE program is as follows. Use the admitted d1 quotient from U1 and
nu_b, truncated downward to h fractional bits. Compute its product with
U1 with the admitted h-grid product, then divide by 2 exactly, retaining
h+1 fractional bits, and subtract alpha_a to obtain u_tilde. Compute
A_tilde=hat alpha_+-hat alpha_- and Bm_tilde=hat nu_+-hat nu_- exactly,
then Pm_tilde by (30) using signed integer operations. Form H_tilde from
its linear expression, keeping h+2 fractional bits for the division by 4.
The factor 4u_tilde is representable already on the h-grid. Compute
T_tilde by multiplying d1_tilde by the signed q1,+-q1,- difference,
truncating TOWARD ZERO at h fractional bits, with absolute error <1/Q.

Set the exact grid-comparison bit e_s=1{|H_tilde|>=1/16}. In its h+2-
fractional-bit integer representation, the threshold is the integer
2^(h-2). Use comparison and mux gates, not a discontinuous real threshold.
If e_s=0, set tau_tilde=0. If e_s=1, form T_tilde/H_tilde by signed integer
long division, truncate toward zero to h fractional bits, and clip to
[-1/4,1/4]. For a total branch circuit, select denominator |H_tilde| when
e_s=1 and the positive value 1 otherwise, select numerator T_tilde or 0,
and apply the divisor's sign only in the enabled branch. Thus even an
unused branch never divides by zero. The absolute value and sign XOR use
signed magnitude/rail bits, not real-input floor or bit extraction.

Finally the intended binary probability of symbol 0 is
(1-ab tau_tilde)/2, which is on an h+1 fractional grid. If t_int=Q tau_tilde
is its signed integer parameter code, output

    m0=floor((Q-ab t_int)/2), m1=Q-m0, (m0/Q,m1/Q).      (31)

This is an exact integer division by 2 followed by a residual, not two
separately rounded probabilities. Since |tau_tilde|<=1/4, it is a legal
simplex for every admissible code, including fallback and bad sampling
events; final TV quantization error is <1/Q. There is no dependence on tau.

All operations are finite neural circuits. C1's closed-grid extraction uses
h+1 bits and is applied ONLY to G_h heads. Subsequent signed integers are
already bit words. AND(u,v)=ReLU(u+v-1), NOT(u)=ReLU(1-u), and
XOR(u,v)=ReLU(u-v)+ReLU(v-u) implement Boolean gates on bits. Ripple
add/subtract/compare use O(w) gates, shifted partial-product multiplication
and restoring division use O(w^2) gates/layers and O(w) scratch. Restoring
division scans numerator bits high-to-low, shifts the remainder, compares
and conditionally subtracts the positive denominator; each remainder stays
below that denominator. For signed division, divide magnitudes and apply
the XOR of signs, implementing truncation toward zero with the stated
error. Comparisons and clipping use bit comparison/mux. Fixed factors and
extra fractional guards are shifts, with explicit held wires. Nothing
extracts bits from a perturbed real number outside a declared finite grid.

The signed ranges are valid on ALL clipped head inputs: d1_tilde in [1,4],
u_tilde in [-1,2], |A_tilde|,|Bm_tilde|<=1, |Pm_tilde|<=9,
|H_tilde|<24, and |T_tilde|<=4. The enabled unrounded quotient has magnitude
<=64. A signed magnitude allowance 128 with h+2 fractional positions,
full product words and ordinary guard bits is ample; 128p-bit words dominate
these bounds. Input extraction coefficients <=Q and all other fixed
coefficients have O(p) bits. No overflow is hidden in a signed affine sum.

There are a constant number of new arithmetic blocks at K=2. The replacement
needs O(p^2) new gates/layers, O(p) scratch/live channels (while retaining the
O(Kp) master banks), O(p^3) extra identity/hold wires, O(p^4) dense slots,
O(p^5) dense parameter bits, O(p^4) addressed sparse bits and O(n p^6)
dense bit operations if evaluated pointwise at every token. Added rolling
working bits are O(n p^2). Original four-head attention, endpoint copies,
masks, positions and evaluator costs are fully retained; conservatively
adding these costs to all of C1 is a valid upper bound, not a claim of
negative cost when replacing its old readout. The new code needs no new
log/exp constants. Last-use scheduling retains all masters and only a
constant number of O(p)-bit sign/magnitude/remainder words across each
school-arithmetic block; old partial products are overwritten before the
next one. These lifetimes justify the O(p^3) holds instead of omitting them.
Explicit program generation can use O(p^4) scratch and O(p^5) operations,
plus writing the chosen layout, within the general Section 4 construction.

We now prove its finite error, separately from its bit implementation. Let
the INTACT head-coordinate errors to the exact ideal code be <=eta, with
arithmetic product/division errors <=zeta and exact guards. One obtains

    |u_tilde-u_ab|<=6eta+zeta,
    |Pm_tilde-Pm|<=28eta+4zeta,
    |H_tilde-H_s|<=66eta+9zeta,
    |T_tilde-T_s|<=14eta+2zeta.                          (32)

Indeed the d1U1 product error is <=10eta+2zeta; divide it by two and
subtract alpha_a. The sign moment errors are <=2eta each. Thus the Pm
error is 4(6eta+zeta)+4eta, and the H error is
[9(28eta+4zeta)+12eta]/4. For T, the q1 sign difference has error <=2eta
and magnitude <=1 even for clipped coordinates. Its product error is
4(2eta)+(6eta+zeta)+zeta. This establishes every constant in (32).

If 66eta+9zeta<=1/16, then on X the gate is enabled, since |H_s|>=1/8.
Compare directly to the unknown tau, using |tau|<=1/4:

    |T_tilde/H_tilde-tau|
      <=16[z+14eta+2zeta+(66eta+9zeta)/4].               (33)

The quotient's additional error is <=zeta; clipping to [-1/4,1/4] cannot
increase error to tau. Binary TV of the model probabilities is half the
parameter error. Applying (31) gives, on X,

    max_s TV(Pi^P1(s),theta_tau,s)
       <=8z+244eta+35zeta+1/Q.                          (34)

For the actual nominal finite intact coordinates eta=2/Q,zeta=1/Q, the
condition is 141/Q<=1/16 and the bound is 8z+524/Q. P2 attack (20) leaves
every input of this readout untouched, so this bound holds under that attack
on the SAME original history. Expected max/fixed/actual-terminal/weighted
risk is <=min(1,8z+524/Q+B_X). Conditional-terminal risk has B_X/pi_s in
place of B_X; here pi_s=1/4 was proved. An intersection with F is available
with bad probability at most B+B_X if simultaneous pathwise statements for
both decoders are desired. We did not confuse separate event probabilities
with independent events.

## 10. A rationally certified finite-N separation and robustness witness

Choose exactly

    K=2, N=2^25, M=33554430, ell=3/8,
    epsilon_a=1/8, t=1/64, h=39, Q=2^39,
    l_N=26, p=324, r=1/512, z=1/256.                    (35)

Then m0=16777214 and n0=2359295. All h domain restrictions hold and Q>=256M.
The two exponents in (19) are

    ell^2 m0/8=9*16777214/512>200,
    2n0 t^2=2*2359295/4096>200.

Since e>2 and 8+8M<2^29, B<2^29*2^{-200}=2^{-171}<2^{-100}.
This is an analytic positive upper bound, not a declaration that an
underflowed exponential is zero. Direct rational comparison verifies
(21), (28), 141/Q<=1/16, and (114M+1)/Q<7/1000. In particular

    (1-2^{-100})[n0/(8(n0+2))-1/64-1/(n0+2)-(114M+1)/Q]>1/10,
    1/64+1/(n0+2)+(78M+1)/Q+2^{-100}<21/1000.            (36)

For (29), M r^2/2>63 and M z^2/32>15. Again e>2 gives
B_X<2^{-61}+2^{-12}. Thus a rational, deliberately conservative certificate is

    8z+524/Q+2^{-61}+2^{-12}<32/1000.                   (37)

For every unknown tau in (26), the original clean terminal expected TV is
<.021, attacked ORIGINAL decoder terminal expected TV is >.10, and the
implemented intact-P1 replacement under the very same P2 attack has expected
TV <.032. The same numerical expected max/fixed/weighted assertions follow
from the simultaneous bounds. Conditional-terminal statements retain their
explicit denominators from Sections 7 and 9; no .032 conditional constant
is asserted from the coarser (37). No trajectory of length 2^25 was simulated
to establish these inequalities. They are a finite existence/class witness,
not an efficient practical sample-size recommendation.

There is also a concrete NONZERO correlated-grid robustness region at this
precision. Set delta=2^{-33}=64/Q. The sharper frequency-sensitive bound
from (17), on F, yields expected original-decoder risk at most

    1/64+1/(n0+2)+2M(78/Q+36*2^{-33})/(n0+2)+1/Q+2^{-100}<16/1000. (38)

It holds uniformly for arbitrary allowed correlated perturbations of all
statistical banks at this radius. Independently, the D3-snap exact-count
margin M(76/Q+35*2^{-33})<142/1000<1/2 holds, as does the B-C-snap margin
at the same radius. Consequently those two different variants still output
their common unperturbed count-simplex bits. This exact-count observation
does not replace the proof of (38) for the original Pi and is not used in
the attacked-original lower bound.

For completeness, resource substitution in the witness is literal:
n=33554433, P_*=p=324 for this chosen grid, per-word allowance 128p=41472 bits,
L=O(2*324^2), W=O(2*324), H_total=6, D_qk=4, score cap 2. Original dense
stored bits are

    O(8*324^5+n^2+n log(n+1)),

and online working bits excluding stored data are O(2n*324^2); forward bit
operations are

    O(n^2*326*324^2+8n*324^6).

Original sparse stored program bits are O(4*324^4), plus positions/masks.
The P1 replacement adds the Section 9 costs at p=324, and retains all those
prefix/mask costs. For count-snap w=39+25+2+8=74; its replacements and the
B-C F=8 feature front end keep exactly their Section 4 resource identities.
These are upper-bound polynomials with universal constants, not claimed
exact hardware sizes or evidence of componentwise budget dominance. In
particular the explicitly stored masks have n^2 cost; no quadratic memory
has disappeared from this large-N mathematical witness.

## 11. Scope, implementation pitfalls, and what has been established

The original Pi and all constants/rounding of C1 remain unchanged. The
count-snap variants and the P1 replacement are separately named, fully charged
readouts. The finite P2 attack is adaptive but theta-independent, acts on
integer words after quantization before all fanout, and does not hide or
destroy intact P1/v1/v2/partial/uniform/endpoint information. Its lower bound
is a bias of the specified difference decoder. The P1 counterconstruction
shows why the same argument cannot prove a complete-code all-decoder lower
bound on the unknown XOR family. We claim no such impossibility and no
sampling advantage from output quantization alone.

Three tempting extensions are specifically excluded, with their repairs:

* Charging only a small REAL perturbation before grid re-storage is false:
  the admitted count-snap counterexample M=7,Q=16,C=1 moves the nominal
  2/16 down by 1/10000 then truncates to 1/16. Its total port change is
  1/16, not 1/10000. Our delta includes all re-storage, and (20) works
  directly on integer words; the old failed convention is not reused.
* Snapped bad-event counts may each be M. Thus their denominator can be
  KM+K (for K=2,M=1 this is 4, exceeding M+K=3). Word bounds and lifetimes
  use the larger range. Original Pi is not silently changed to this decoder.
* Supplying a surviving clean q2 duplicate or allowing the decoder to inspect
  the attacker/history/evaluator buffers would change the experiment. We
  explicitly charge and end their lifetimes, enumerate all surviving banks,
  and limit the result to the specified access model. Even without such a
  duplicate, the intact P1 bypass remains available and is proved above.

The concrete candidate constants survive after these conventions are made
precise. In particular (37) uses a weaker rigorously proved .031495-scale
upper bound instead of treating an approximate .031251 evaluation as proof.
Necessary bounded diagnostics in the companion program check finite integer
attack, signed/fallback/division/simplex operations and rational witness
inequalities; they are not premises for the probability theorems and do not
enumerate large history sets. No old failure evidence or source was edited.

## 12. Exact input provenance and native handoff

The fixed source files and SHA256 values used in this proof are:

| Source | SHA256 |
|---|---|
| PROBLEM.md | 882e1705c029384ef98b791df1fae20da5d074ceeaf8962eb5d5795e370b5531 |
| outputs/002-realization/prover/proof-v1.md (admitted C1 artifact) | 36260d168f17b9da129179070a70c5e87019a45d98c60f1c343a9e1c5e60287b |
| outputs/005-budget-comparison/counter/count-snap-v1/proof-v1.md (admitted count-snap artifact) | 8b9308eaebe171021dba4ce729531b86316966b8298235919e16602bdf5a5e6a |
| outputs/004-finiteN-reliability/lead/risk-composition-v2.md (fully read, unadmitted) | d17bcea2f21bb5fe00395fdbd4345c8c7c33d08c3d68d09dd09522e0e279da08 |
| outputs/004-finiteN-reliability/lead/transfer-checkpoint-v1.md (unadmitted) | 09036bf452b98b7bf961e57aa65e466579fb9904098e1982aa4892fa10a24a8f |
| outputs/003-comparison/counter/finiteN-v1.md (unadmitted) | 9e70aa01ec8606f9b5c71670a111fd6ea0be0513bbe9b6806ab3808b3d2d238d |

Submission is to exact obligation af879858f3020c501dff7a366f8e1cfdcda36eb6a8c4f2a79fa1af839eb41390,
with native predecessor Fact IDs b2f4d10fa0a69e00 and bcd4541db2cf4c1a.
The gateway's actual independent verdict determines acceptance, not these
derivations, a teammate discussion or diagnostics. Native budget: GPU use 0,
[Non-scientific operational metadata omitted.] all other dimensions
are unlimited. No new goal, route, monitor, task restoration or campaign
setting is created. Root C2 strong comparison and C4 integration remain open.
