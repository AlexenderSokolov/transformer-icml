# SRC-Pi: self-contained deterministic realization and complete charges

Fixed author proof v1, 2026-10-27.
Obligation: 6010cac30ffe4aea77e6d7a9e4e3f5686e4f44b2bf31c1674d33dfdf7dc46f84.
Contract: e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af.
Predecessors: [].

This proves the entire fixed S1–S5 statement at
outputs/002-source-realization/lead/src-pi-statement-v1.md.
The construction is the original finite program, with its already specified
guards, ordered quotient decoder, and corrected resource conventions. The
proof below derives I; it does not assume I or use the conditional statistical
root. Source files are provenance for the fixed construction, not admitted
premises. All arguments needed here are included below. In particular, no
positivity, stationary initialization, stochastic convergence theorem,
file-review PASS, or old Fact is a premise.

## 1. Quantifiers, objects, and the finite model

Fix arbitrary integers K>=2, N>=3, M=N-2, n=N+1 and

    h>=max(4,ceil(log2 M)+1), Q=2^h,
    ell=ceil(log2(N+K+2)), p=4h+4ell+64.

Fix any string X_1,...,X_N in A={0,...,K-1} and any declared query
s=(a,b) in A². None of these strings is excluded by its probability under
some source. Define, only for the proof,

    n_ij=sum_(t=3)^N 1{(X_(t-2),X_(t-1))=(i,j)}, u_ij=n_ij/M,
    C_s,c=sum_(t=3)^N 1{(X_(t-2),X_(t-1),X_t)=(a,b,c)},
    c_s,c=C_s,c/M, n_s=sum_c C_s,c, rho=1/M,
    p_s,c^+=(C_s,c+1)/(n_s+K).

The program never receives or builds this pair/triple table. Its only
data inputs are the observed symbols, declared query/mode, and public
metadata. Every loop bound, mask, parameter, word layout, constant and
routing choice below is a deterministic function of K,N,h. Each run
returns one requested row. Statements for all queries mean correctness
of every such run, not K² outputs supplied at the cost of one run.

The main implementation is batch causal attention, evaluated by the
specified finite integer algorithms, followed by tokenwise Boolean/ReLU
arithmetic. Attention uses unscaled dot products, with no LayerNorm or
unrepresented square-root scaling. Its finite numerical work is charged
separately from neural layer count. The tokenwise map is executed and
charged at all n positions; only position q=N+1 supplies the requested
output. A fully expanded neural implementation has its separate bounds
in Section 10 below.

Write TV(v,w)=(1/2)sum_c |v_c-w_c|. We prove both nominal correctness
and the stated correlated grid-replacement property for this same
program. Delta below is a nonnegative perturbation radius, not a
probabilistic hypothesis; epsilon_p=2^(-p) denotes internal precision.

## 2. Causal front end and its complete data interface

The observed input is x_t=e_(X_t) at t<=N. The synthetic token x_q=0.
It contains no X_(N+1). Public metadata includes position/type, t,N
and z_t=1{t=3}; z_q=0. Explicit Boolean masks use no numerical minus
infinity. Storing these masks and positions is charged.

Two singleton heads in the first attention layer have zero Q,K and
value x. Their masks choose t-1 and t-2 respectively, with self as
fallback when that predecessor is unavailable. Since a singleton
normalized weight is exactly one, these heads copy exactly under the
finite evaluator given below. They produce

    l1_t=e_(X_(t-1)), l2_t=e_(X_(t-2))  (3<=t<=N),
    l1_q=e_(X_N),     l2_q=e_(X_(N-1)).

Both heads, their projections, masks and residual routing are paid.
The token x is retained separately. Compute the bit vector
F_t,c=ReLU(l1_t,c+z_t-1)=z_t l1_t,c. At q choose query one-hots A,B
from either external e_a,e_b or the two copied endpoint vectors.
For bit inputs, the mode selector

    ReLU(v+m-1)+ReLU(w-m)

equals v at m=1 and w at m=0. In either mode retain the actual endpoint
l2_q,l1_q in separate exact registers. An external query does not
overwrite the endpoint. Other rows may use their copied l2,l1 as their
legal query one-hots.

There are four heads in the second attention layer. The following
table describes their ideal real comparison values. Actual finite
log constants and their evaluation are specified in Section 4.

|Head|Q at q|K at key t|V at key t|Output|
|---|---|---|---|---|
|P1|((ln 2)A,(ln 2)B)|(l2_t,l1_t)|(x_t,l2_t)|(q1,v1)|
|P2|((ln 2)A,(ln 3)B)|(l2_t,l1_t)|(x_t,l2_t)|(q2,v2)|
|T|(ln 2)B|l2_t|(l1_t,F_t)|(hvec,h0)|
|0|0|0|(l2_t,l1_t,F_t,z_t)|(alpha,nu,f,rho)|

At q the allowed keys are exactly 3,...,N, a nonempty set since M>=1.
Other rows use the causal prefix of this set and self fallback if empty.
All value coordinates are query-independent local bits, including the
initial-position flags. The QK dimensions are 2K,2K,K,1; the value
dimensions are 2K,2K,2K,3K+1. Thus there are 9K+1 statistical coordinates.
There are six heads in total and at most four in a layer.

All returned coordinates belong to [0,1]; clipping to this interval
is an explicit allowed operation. Select the single coordinate
U_k=v_k,a by summing ReLU(v_k,i+A_i-1) over i. Since A is one-hot,
this is exact selection, not a K-fold amplification of error. Select
alpha_b and nu_b using B in the same manner. Compute

    j=sum_i ReLU(B_i+l2_q,i-1),
    J_c=ReLU(j+l1_q,c-1).

Here j is a bit and J_c=1{(X_(N-1),X_N)=(b,c)}. These are charged
O(K) gates on exact one-hot bits, so the actual endpoint correction is
available even for external s different from the endpoint.

After the statistical layer the query decoder has only these banks:
P1(q1,v1), P2(q2,v2), T(hvec,h0), uniform(alpha,nu,f,rho),
the exact query/mode/endpoint/flag bits and public metadata. A generous
64K+32 pre-expansion scalar slots contain all these registers and copies.
There is no further attention or decoder read of historical residuals,
no raw-history port and no count-table input. The historical arrays
used by attention are real charged memory; their lifetime and release
are specified in Section 8.

## 3. Finite bit arithmetic and ReLU realization

We first give the arithmetic algorithms so the subsequent finite
evaluation and floors refer to actual circuits. For bits u,v,

    AND(u,v)=ReLU(u+v-1), NOT(u)=ReLU(1-u),
    XOR(u,v)=ReLU(u-v)+ReLU(v-u),
    OR(u,v)=u+v-AND(u,v).

These use constant-size, constant-depth ReLU gadgets. Copying a
nonnegative bit is an identity ReLU, charged whenever it is held across
a layer. Signed words use sign/magnitude bits or two nonnegative rails.
There is no real-valued threshold oracle.

A ripple adder sets sum_i=XOR(XOR(a_i,b_i),carry_i) and
carry_(i+1)=OR(AND(a_i,b_i),AND(carry_i,XOR(a_i,b_i))).
It costs O(w) gates/depth on w-bit inputs. Borrow subtraction and
comparison are implemented by the analogous finite recurrence; a
high-to-low comparator keeps equal/less bits. A mux uses two ANDs and
an OR. School multiplication adds the shifted partial products,
retaining the complete 2w-bit result. It has O(w²) active gates and
sequential depth, O(w) live scratch. Restoring long division scans
numerator bits high-to-low: shift the current remainder, append the
next bit, compare with the positive divisor, subtract it iff needed,
and emit the quotient bit. Inductively the post-step remainder is
below the divisor; the trial remainder before subtraction is below
twice the divisor. This uses O(w²) gates/depth and O(w) scratch and
returns the exact integer floor quotient and remainder. These bounds
also hold when numerator length is a fixed multiple of w. All loops
run their full public length and branches are muxes.

The scalar-to-bit map is also explicit. If H is a returned head
coordinate, let A_h=QH, an integer in [0,2^h]. For j=h,h-1,...,0 set

    b_j=ReLU(A_j-(2^j-1))-ReLU(A_j-2^j),
    A_(j-1)=A_j-2^j b_j.

On the indicated integer grid this is exactly the indicator
A_j>=2^j; induction gives 0<=A_(j-1)<2^j. The first step is legal
even when H=1 and A_h=2^h. There are h+1 bits, not h. All scaling,
threshold coefficients and residual operations are finite dyadics
and paid. The map has O(h) active gates/depth per scalar. Its
continuous extension off the grid is not claimed to implement floor.
The same construction, with top index p+1, extracts a finite score
numerator in [0,2^(p+1)] if that numerator was first stored as a scalar.

Clipping is ReLU(x)-ReLU(x-1), or signed comparison followed by mux.
Max with a public dyadic uses the same primitives. Grid additions and
subtractions are exact signed integer operations. All full products,
remainders and the guard bit for division by two are retained before
the expressly specified truncations. Final dyadic decoding is a paid
linear combination of output bits with coefficients 2^(j-h).

## 4. Finite log, exponential, and softmax evaluation

All ideal logarithms in Section 2 are only comparison values. For
x=2,3 let y=(x-1)/(x+1), respectively 1/3,1/2, and define

    S_x=2 sum_(j=0)^(p-1) y^(2j+1)/(2j+1),
    L_x=2^(-p) floor(2^p S_x).

Integrating the finite geometric-series identity with its remainder
gives ln x=2 sum_(j>=0) y^(2j+1)/(2j+1). The positive tail is at most

    2 y^(2p+1)/[(2p+1)(1-y²)] <= 2^(-2p).

Consequently 0<=ln x-L_x<2 epsilon_p. This construction is exact
rational arithmetic followed by one integer division. For y=1/d,
the common denominator

    d^(2p-1) product_(j=0)^(p-1)(2j+1)

suffices and has O(p log(p+1)) bits. Construct its factors, each
numerator term over this denominator, and sum serially; school
arithmetic on those lengths costs O(p³ log²(p+1)) bit operations
and O(p log(p+1)) scratch bits. These are offline charges. The
large exact rational integers may be arrays of bounded words; the
online stored constants are just the two p-fractional-bit dyadics.
No constant-generation oracle is used.

Use L_2,L_3 in the actual Q projections. A score is the exact sum
of at most two selected dyadics, with any dense zero terms charged.
For its ideal counterpart s_*,

    0<=s<=s_*<=ln 6<2,  |s-s_*|<=4 epsilon_p.

Singleton scores are zero. This proves the score cap 2 for every
row, not only q. The score integer can be formed directly from the
two log numerators and input bits, or extracted as in Section 3;
there is no implicit real-to-integer conversion.

Put R=2^p, S=Rs, J_exp=8p, and compute exactly

    T_0=R,
    T_j=floor(T_(j-1) S/(jR)), 1<=j<=J_exp,
    W=sum_(j=0)^J_exp T_j,  hat w=W/R.

Each floor is the long division of a full integer product by a
positive integer; there is no intermediate rounded multiplication.
Induction gives 0<=T_j/R<=s^j/j!, hence 1<=hat w<=exp(s)<=6.
If e_j=s^j/j!-T_j/R, then

    0<=e_j<=s e_(j-1)/j+epsilon_p.

An error introduced at step k contributes to the sum of subsequent
term errors by at most
epsilon_p sum_(r>=0) 2^r/r! <8 epsilon_p, since
(k+1)...(k+r)>=r!. Thus sum_(j=1)^J_exp e_j<=8J_exp epsilon_p.
For j>=9, 2^j/j!<=2^(-j) (the base case and successive ratios
prove it). The omitted exponential tail is <=2^(-J_exp)<=epsilon_p.
The derivative of exp on [0,2] is <8. Therefore for the ideal
weight w_*=exp(s_*),

    0<=w_*-hat w
      <=(64p+1)epsilon_p+32epsilon_p
      <=100p epsilon_p.                                      (4.1)

For a row with m>=1 allowed keys, keep exact integer denominator
D=sum_t W_t and each bit-value numerator A_c=sum_t W_t v_(t,c).
Here D/R>=m, all numerators lie in [0,D], and there is no rounding
inside the sums. Return

    H_c=Q^(-1) floor(Q A_c/D).                               (4.2)

The ideal and finite real numerator and denominator sums differ
by at most m(100p epsilon_p). Subtracting their ratios, using
both denominators >=m and the ideal ratio <=1, gives error
<=200p epsilon_p before the final head quotient. That quotient
adds <1/Q. For p>=32, 200p<=2^(p/2); the inequality holds at
32 and remains true at successive integers. Our p>=4h+64 implies
200p epsilon_p<=2^(-h). Hence

    H_c in G_h={j/Q:0<=j<=Q}, |H_c-H_c^ideal|<=2/Q.          (4.3)

This proves the head assertion for all paths, all rows and all
coordinates, including statistical h0,f,rho. Singleton values are
copied exactly because their numerator is either zero or their
denominator. The sums include enough integer bits for m<=n;
their precise word bounds and operation costs are below.

## 5. Exact path algebra of the ideal comparison heads

Let alpha_i=sum_j u_ij and nu_j=sum_i u_ij. The uniform head gives
alpha,nu,rho=1/M and f_c=rho 1{X_2=c}, since exactly one key has
z_t=1. The partial-head mean weight is dT=1+alpha_b. Summing its
values with weights 1+1{lag2=b} gives

    dT hvec_c=nu_c+u_bc,
    dT h0_c=f_c+rho 1{(X_1,X_2)=(b,c)}.

Thus initial_bc=dT h0_c-f_c is the initial pair mass. Define

    g_bc=dT hvec_c-nu_c+rho J_c-initial_bc.

The list (X_1,X_2),...,(X_(N-2),X_(N-1)) differs from
(X_2,X_3),...,(X_(N-1),X_N) by exactly the initial and terminal
pairs. It follows, without an asymptotic boundary approximation, that

    g_bc=(1/M)sum_(t=3)^N 1{(X_(t-1),X_t)=(b,c)}.           (5.1)

This identity includes M=1. It uses the actual endpoint, even when
the declared query is external.

For product head k let lambda_1=1, lambda_2=2. Its ideal weight is

    (1+1{lag2=a})(1+lambda_k 1{lag1=b}).

Expanding and averaging gives

    d_k=1+alpha_a+lambda_k nu_b+lambda_k u_ab,
    d_k U_k=2(alpha_a+lambda_k u_ab), U_k=v_k,a.

Subtracting half the second equation from the first yields

    d_k=(1+lambda_k nu_b)/(1-U_k/2).                        (5.2)

The denominator is >=1/2 because U_k in [0,1]. If
r_c=(1/M)sum_t 1{X_t=c} and
B_c=(1/M)sum_t 1{X_(t-2)=a,X_t=c}, where both sums run t=3,...,N,
expanding the same product against the successor value gives

    d_k qk_c=r_c+B_c+lambda_k g_bc+lambda_k c_s,c.

Subtract the k=1 identity from the k=2 identity and use
lambda_2-lambda_1=1 to obtain the required recovery:

    c_s,c=d2 q2_c-d1 q1_c-g_bc.                            (5.3)

All quantities in this derivation are path sums. No stationary law,
positivity, accessibility or probabilistic event has been used.
In particular, the derivation is valid when n_s=0.

## 6. Actual directed readout, guard ranges and ordered output

Now use the finite grid words returned by (4.2), with hats to
distinguish them from Section 5. Under the later optional master
replacement, use the replacement grid words in these very same
operations. Clipping and exact one-hot selection give every selected
input in [0,1].

If U,V are the integer numerators of hat U_k and hat nu_b, compute

    D_k=floor(2Q(Q+lambda_k V)/(2Q-U)), hat d_k=D_k/Q.       (6.1)

The divisor lies in [Q,2Q]. This implements the denominator
1-hat U_k/2 with its extra fractional bit intact. The ratio of
its input coordinates is approximated downward by <zeta=1/Q.
Set hat dT=1+hat alpha_b exactly. For a product of nonnegative
h-grid numbers with numerators A,B, compute floor(AB/Q)/Q:
one exact full product and one quotient, error <zeta. Use this
for dT hvec, dT h0, d1 q1, d2 q2. Subtraction/addition in
(5.1),(5.3) is exact signed arithmetic; rho J is exact selection
by a bit. No independently estimated u_s is used as a final divisor.

These formulas have global legal ranges on the whole product grid:

    hat d1 in [1,4], hat d2 in [1,6], hat dT in [1,2].

Products with a head scalar lie in [0,4], [0,6], [0,2].
The two expressions dT hvec-nu and dT h0-f each lie in [-1,2].
Their flow combination lies in [-3,4]; d2q2-d1q1 lies in [-4,6];
the recovered signed c lies in [-8,9]. Thus [-16,16] is a safe
readout box, irrespective of the radius of a grid replacement.
Integer products and division trial remainders are stored in their
full separate words, not clipped to this scalar readout box.

Clip the recovered frequency to a_c in [0,1]. It is still an h-grid
number. Set

    d_M=ceil(log2 M), r0=2^(-d_M-1),
    r=max(hat rho,r0), x_c=a_c+r, V_c=Qx_c.

Because h>=d_M+1, Qr0=2^(h-d_M-1) is a positive integer. Also
0<r0<=rho/2, and hat rho in [0,1] implies r<=1. Consequently

    x_c in (0,2],  V_c in {1,...,2Q}.                      (6.2)

V_c is the existing fixed-point x register's integer payload, not
an exact count input or a free new scaling operation. Keep all K
payloads before starting the following sum. Set T=sum_c V_c>0
and compute by exact long division

    m_c=floor(Q V_c/T), c=0,...,K-2,
    m_(K-1)=Q-sum_(c<K-1)m_c, Pi_c=m_c/Q.                  (6.3)

All first m_c are nonnegative and their sum is at most Q, so
the residual coordinate is nonnegative and all coordinates sum
exactly to one. In fact positivity of all K weights makes the
first K-1 exact shares sum strictly less than one; thus the last
residual numerator is at least one. Other coordinates may be zero.
This argument does not require Q>=K.

For c<K-1 write epsilon_c=V_c/T-m_c/Q in [0,1/Q).
The last-coordinate error equals sum_(c<K-1)epsilon_c, whence

    TV(Pi,V/T)=sum_(c<K-1)epsilon_c <=(K-1)/Q.              (6.4)

The asymmetry of (6.3), including the residual last coordinate,
is part of the original program. All quotient, summation,
subtraction, storage and dyadic decoding operations are paid.

## 7. Deterministic error propagation and the derivation of I

Suppose each finite statistical coordinate used by the readout
differs from the corresponding ideal value by at most eta.
For nominal operation take eta=2/Q by (4.3). For a replacement
within delta of its nominal grid master, take eta=2/Q+delta.
All replacement coordinates still belong to G_h; they need not
form probability vectors within individual banks. Exact one-hot
selection preserves eta. Arithmetic remains precisely the directed
operations of Section 6, with zeta=1/Q.

For (5.2) put v=1-U/2 and t=1+lambda nu_b. Both ideal and actual
v are >=1/2, |hat v-v|<=eta/2, |hat t-t|<=lambda eta and
t<=1+lambda. By subtracting the two ratios,

    |hat t/hat v-t/v|
      <=2 lambda eta+2(1+lambda)eta.

Charging the actual quotient (6.1) yields error 6eta+zeta for
d1 and 10eta+zeta for d2; dT has error eta. For example

    |hat dT hat hvec-dT hvec|
       <=|hat dT-dT||hat hvec|+dT|hat hvec-hvec|
       <=3eta

before its product rounding. Including the subtracted nu gives
4eta+zeta. The same argument applies to dT h0-f. Multiplication
of rho by exact J is bit selection. For d_k qk use
|hat d_k-d_k||hat qk|+d_k|hat qk-qk| and then charge its
product rounding; the ideal d1<=4 and d2<=6. The full ledger is

|Quantity|Coordinate error relative to its ideal value|
|---|---|
|dT|eta|
|d1; d2|6eta+zeta; 10eta+zeta|
|dT hvec-nu; dT h0-f|4eta+zeta each|
|rho J|eta|
|g|9eta+2zeta|
|d1 q1; d2 q2|10eta+2zeta; 16eta+2zeta|
|recovered c_s,c|35eta+6zeta|

The last row follows by adding the errors of the three terms in
(5.3). Clipping does not increase distance from c_s,c in [0,1].
Moreover max(t,r0) is 1-Lipschitz and fixes rho>=r0, so
|r-rho|<=eta. Therefore the actual computed weights satisfy

    |a_c-C_s,c/M|<=35eta+6zeta=76/Q+35delta,
    |x_c-(C_s,c+1)/M|<=36eta+6zeta=78/Q+36delta.           (7.1)

No independence, stochastic law, or cancellation of random
errors occurs in this calculation. Shared coordinates can have
arbitrarily correlated changes. All ranges in Section 6 depend
on grid membership, not smallness of eta or delta.

For positive real vectors x,y, write X=sum x, Y=sum y. Adding
and subtracting x/Y gives

    ||x/X-y/Y||_1
      <=|Y-X|/Y+||x-y||_1/Y
      <=2||x-y||_1/Y.

Apply this to the actual x and the mathematical comparison vector
y_c=(C_s,c+1)/M. Its sum is Y=(n_s+K)/M, whether or not n_s>0.
Together with (6.4) and (7.1) it proves

    TV(Pi^delta_s,p_s^+)
       <= KM(78/Q+36delta)/(n_s+K)+(K-1)/Q.               (7.2)

Taking delta=0 proves the required interface

    TV(Pi_(K,N,h)(X_1^N;s),p_s^+)
       <=78KM/[Q(n_s+K)]+(K-1)/Q.                       (I)

It also gives the nominal 76/Q and 78/Q coordinate bounds.
There is no division by a possibly zero empirical count:
the actual normalizer divides by the positive sum of the
actually computed x's. When n_s=0 the comparison add-one row
is uniform, and the same proof applies. When M=1 every head
uses a single key, so its bit means are exact; the boundary
algebra and the same guards remain valid. Every statement
has been proved for each string and query, hence simultaneously
on their full finite domains. A source changes input probabilities,
not this deterministic program or its fixed operation schedule.

## 8. Located master and V-bank cuts, fanout and lifetimes

We give a concrete topological execution/lifetime schedule of
the just specified dataflow. Reordering independent rows of
tokenwise work does not omit any of the n charged executions.
Evaluate the historical rows and their otherwise unused outputs
before the final query readout, and process q last. Attention
scratch can be streamed by row and by head. There is no extra
network or observational input in this schedule.

During attention, historical x,l1,l2,F and projected Q/K/V arrays
live in the charged token workspace; parameters, masks and
positions have separately charged storage. On an edge the
score numerator S, current exponential term, weight W and full
product/division scratch live until the accumulator update.
Each row/head keeps D and its value numerators A_c until the
output divisions are finished. Recycle edge scratch after
use. Write each quantized statistical result exactly once
to a previously zero master word; this output projection
is routing, not addition to an older clean residual copy.

For q there is one such post-quantization master for every
coordinate in the following complete statistical interface:

|Bank|Number of coordinates|
|---|---:|
|q1, v1|2K|
|q2, v2|2K|
|hvec, h0|2K|
|alpha, nu, f, rho|3K+1|

Retain these masters without a readout fanout until all needed
quantizations are complete. Before exposing the master cut,
erase/release their clean evaluator numerators, denominators,
weights, exponential terms, normalized scratch copies, quotient
remainders and projected-query temporaries. Historical/projected
arrays and unused historical outputs are erased/released after
their last paid use. One may finish all other tokenwise rows
before exposing q's cut; the maps act separately by row.
Thus no surviving clean evaluator copy is a query readout input.
In particular an unrounded or clean normalized q2 does not
bypass the cut. Input storage and all its uses were still charged.

The exact residual inputs at this interface are A,B, external
query/mode if retained, the actual endpoint l2_q,l1_q, zero
x_q,F_q,z_q, other declared flag bits and public constants.
Only these exact bits/metadata and the statistical masters
are subsequent readout inputs. Statistical flag-valued
means h0,f,rho are in the replaceable bank, not the exact-bit
exception. Mask/parameter knowledge supplies no new
data-dependent statistic.

At the master cut replace any or all masters by arbitrary
canonical G_h words, each at distance <=delta from its
nominal value. All subsequent scalar copies, bit expansions
and residual routing start from the replaced master. There
is no duplicate clean branch. The single-coordinate
selection, d1,d2,dT, endpoint intersection bits, J, products,
initial/flow values and recovered frequencies are computed
in the order already specified. Coordinate arithmetic is
serial with recycled scratch; retaining all masters and the
K outputs costs O(Kp) bit channels. Equation (7.1) and
global legality then apply on every joint replacement.
The experiment neither changes exact query/endpoint bits
nor permits additional arithmetic faults.

The final positive-bank cut uses a second precise boundary.
Compute all a_c, the shared r, and all x_c/V_c before any
final summation or quotient. Do not incrementally cache a
partial T while producing V. This is a valid order because
the V-producing subgraph does not depend on T. The source
already allocates the whole positive vector. Clear/release
temporary frequency/products after last use. Other banks
may remain allocated and charged, but the final decoder
reads only V and public K,Q; it has no clean comparison port.

The words at this cut have h+2-bit positive-integer payloads
(or that payload embedded in the larger physical words).
Replace V by any canonical W in {1,...,2Q}^K, keeping no
cached clean sum or quotient. The original suffix first
computes U=sum W, then (6.3) with W,U in place of V,T.
For every such replacement,

    K<=U<=2KQ, 0<QW_c<=2Q², W_c<U,
    0<=floor(QW_c/U)<Q,
    sum_(c<K-1)floor(QW_c/U)<Q.

Thus every divisor is positive, the last residual lies
in [1,Q], and every output is legal. The existing long
division only requires a positive divisor; it does not
require that W have the old smoothing lower bound Qr0
or correspond to any empirical table. A payload word
of 2h+ceil(log2(K+1))+3 bits covers the divisor, dividend
and trial remainders; the full-product storage described
in Section 9 is more generous still. No new guard,
normalizer, fallback or raw-data read is needed.

For comparison only, define the positive real vector

    V*_c=Q(C_s,c+1)/M, T*=Q(n_s+K)/M.

V* need not be integral. It is never stored as an input
to the decoder, nor is T* identified with actual T.
Multiplying (7.1) by Q proves exactly

    |V_c-V*_c|<=78+36Qdelta.                              (8.1)

This is the claimed interface between the master bank
and the actual positive weights; it has not been inferred
from I.

Clearing a dead scalar/bit buffer consists of explicit zero
writes; release with no further read is also allowed by the
declared lifetime convention. The cost of zeroing the whole
historical/projected working arrays is O(nKp²) bit writes.
Per-row accumulators and edge scratch have O(p)-bit words
and their clears/copies are absorbed by the attention
bounds below. Holding masters until the cut, then positive
weights until the final sum, is absorbed by the O(Kp)
live-channel and O(K²p³) hold bounds. Consequently the two
boundaries are available within the original asymptotic
construction costs and preserve its nominal function.

These are located program interfaces and access rules.
They are not an information lower bound for algorithms
that can reread the original history. Canonical word
replacement also does not include inconsistent rail copies,
reserved-bit corruption, arbitrary negative words or
overflowing numbers. A physical injector, snapshot device,
new normalizer or bridge is an additional implemented
object with its own acquisition, wiring, storage and
operation costs, not a free component of nominal Pi.

## 9. Word bounds and complete batch-hybrid resource proof

All O constants in this section are absolute, independent
of K,N,h, history, query and source. These are construction
upper bounds, not measured profiles of an unavailable emitter.

### 9.1 Words, guards, circuit schedule and neural size

Scores have p fractional bits and magnitude <2. In the
exponential recurrence, individual terms and the accumulated
weight are <=6R (the generous bound 8R also suffices).
Their products require at most 2p+6 bits. A recurrence
divisor jR uses at most p+ceil(log2(8p))+1 bits. A row sum
is <=6nR and uses at most p+ell+4 bits; the final head
dividend QA_c uses at most p+h+ell+4 bits. Quotient
remainders and their one-step shifts add only a constant
number of bits to the corresponding divisor lengths.

The readout has the fixed scalar ranges of Section 6.
Formula (6.1) has divisor between Q and 2Q and dividend
at most 6Q². Other h-grid scalar products retain their
full numerators. At the final normalizer T<=2KQ,
QV_c<=2Q². Its safe payload allowance
2h+ceil(log2(K+1))+3 also covers shifted trial remainders.
Extraction thresholds have magnitude at most 2^h for heads
and 2^(p+1) for scores. All query/flag operations act on
exact bits.

For definiteness store signed scalar working registers
with 16p integer and 16p fractional positions, retaining
full double-width products in separate temporaries before
any quotient. Allow sign bits and integer accumulation
guards within 128p bits. This accommodates every number
just listed: h<=p/4, ell<=p/4, and log2 p<p. A dense
pointwise neuron sums at most O(Kp) products, needing only
O(log(Kp)) extra integer guards; log2 K<=ell and the
finite fixed gate gadgets can be allocated within this
allowance. Dense zero slots do not require extra range.
The specified full words can represent the grid values,
their guard fractional bits and each exact bit gate.
No Boolean operation is numerically rounded.

Thus single online coefficients and arithmetic words,
including full products and remainders, may all be
allocated at <=128p bits. Offline log-generation integers
of O(p log(p+1)) total bits are multiword arrays, with
their separately stated scratch cost; the claim does
not compress such a whole array into one online word.
Layout record sorting likewise uses its separately
charged storage. These distinctions avoid a hidden
fixed-machine-word assumption.

Expand O(K) head scalars into bits in parallel, retain
query/endpoint bits, and process the O(K) products,
divisions and recovered coordinates serially. A school
product/quotient on O(p) bits has O(p²) active gates/depth
and O(p) scratch. Keep O(Kp) live channels for the head
words, exact bits and output words. Parallel extraction,
selection, clipping and the final dyadic decoding add
at most the same orders. Consequently

    neural L=O(Kp²), W=O(Kp).

These figures include the constant number of copying,
flag and statistical-attention stages. QKV projections
are actual charged linear maps. There are O(Kp²+K²)
active arithmetic/projection gates or nonzero records
before holds; O(K²) conservatively covers the front
projections. Identity holds across every intervening
layer cost O(LW)=O(K²p³) records, including retained
masters, residuals, carries and unfinished outputs.

Dense storage has O(LW²)=O(K³p⁴) coefficient slots
including zeros and biases, and O(K³p⁵) bits. Sparse
storage counts active records and holds separately,
with O(p)-bit coefficients and O(log(LW+1))=O(p)-bit
addresses, so the complete addressed sparse program
costs O(K²p⁴) bits. Actual gate arities in the bit
gadgets are bounded; extraction and decoding summands
are charged as terms. There is no free fanout storage.

### 9.2 Attention work, caching and all-token dense work

For an allowed/scanned edge, forming its dense score
and value contributions costs O(Kp²) using generic
O(p)-bit school arithmetic. The uncached exponential
has 8p exact product/division steps at O(p²) bit
operations each, hence O(p³). Bit-valued weighted
aggregation and row normalization fit O(Kp²) per
edge plus O(Kp²) per row. There are O(n²) edges
across a fixed number of heads, so

    uncached attention bitwork = O(n²(K+p)p²).             (9.1)

Stream a row's weights into its O(K) numerator accumulators
and one denominator. Do not store an n² numerical weight
matrix. The full projected token arrays are charged
working memory. The exact score-to-integer extraction,
loop counters, copies, resets and row output divisions
fit (9.1). The two singleton heads are included.

There are exactly five possible finite full scores
for these heads: 0,L_2,2L_2,L_3,L_2+L_3. A cached
version evaluates the same finite exponential recurrence
once at each such score, stores the resulting O(p)-bit
integers, and selects the appropriate integer weight
on each edge. In particular the value at L_2+L_3 is
evaluated separately; it is not a product of independently
rounded exponentials. Hence the cached version gives
exactly the same head outputs as the uncached version.
The nonzero cache generation costs O(p³) total, in
addition to finite log generation; cache storage and
selectors are charged. Its attention work is

    equally cached attention bitwork = O(n²Kp²).          (9.2)

The term “equally cached” denotes a comparison convention:
any comparator using such a cache must also pay its own
generation, storage and selection. No comparative
advantage is inferred here.

In the dense pointwise/QKV convention evaluate all matrix
slots at all n tokens. Each O(p)-bit multiply/add has
generic O(p²) bitwork. Therefore

    dense pointwise/QKV bitwork
       =O(n L W² p²)=O(nK³p⁶).                            (9.3)

This is p⁶, not p⁵; specialized shift weights do not
justify changing the generic dense accounting rule.
One-hot selection and zero terms are not free dense
operations. Sparse storage does not automatically
inherit a claimed sparse runtime improvement.

### 9.3 Stored data, rolling work, offline generation and peak

Masks/positions require O(n²+n log(n+1)) bits. Observed
one-hot input is O(NK) bits; query and endpoint acquisition,
mode, residual copies and metadata are charged too.
Binary acquisition or conversion, if chosen instead,
has its actual additional program/work cost. All required
front-end copies were realized above by paid heads and
gates.

Two rolling neural layers, live QKV arrays, scalar/bit
banks, scratch and controller/address words fit
O(nKp²) working bits with scalar-neural physical words
of O(p) bits. This excludes separately stored
parameters/program, input, masks and positions. A packed
Boolean/register evaluator may store a logical bit in
one physical bit and fixed words in packed binary, whereas
a scalar-neural bit channel has its allocated O(p)-bit
scalar representation. These are distinct storage
conventions. The displayed rolling bound is conservative
for the scalar convention and covers the packed one; it
does not claim that packed sizes equal neural matrix
sizes.

Finite arithmetic evaluator code can be stored using
a conservative O(p⁴) bits: fixed school-bit gadgets,
their bounded-word loop templates and addresses, and
the 8p-step recurrence require no more than that.
K,N,h counters and loop/layout metadata are explicit.
This code is charged, not a free interpreter; the
allowance fits each stated program bound since K>=2.

Complete offline construction includes computing K,N,h
layouts and fixed masks/positions, generating logs and
cache entries, selectors and arithmetic microcode,
assigning every gate/term/hold record an address, and
writing the chosen format. Let G,T_rec,I_hold be the
actual numbers of generated gate, term and hold
records. Each has O(p) address/coefficient bits and
log(G+T_rec+I_hold+1)=O(p). The explicit nested loops
above generate the records. Even comparison sorting
and arranging them costs at most

    O((G+T_rec+I_hold)p²) bitwork,
    O((G+T_rec+I_hold)p) working bits.

Indeed O(log(G+T_rec+I_hold+1)) comparisons per record,
each on O(p) bits, give that safe bound; generation
itself fits the same allowance. Dense files additionally
pay the actual coefficient-bit writes, including
zero slots and biases. Sparse files pay addressed
nonzeros and every hold. Explicit position/mask writing,
layout bookkeeping, microcode/cache writes and their
generation work are additional named offline charges;
none is subsumed by reporting only the log computation.
The log generation and scratch are respectively
O(p³ log²(p+1)) and O(p log(p+1)), as proved in Section 4.

At each execution/construction phase, total live
memory is the sum of the simultaneously live program
or parameters, input, masks/metadata, QKV, residuals,
masters/positive/output banks, controller/address
state, temporary workspace, and output. Total peak
is the maximum of these phase sums. In particular
offline log/sorting scratch coexists with any retained
generated data and is included when live. For example,
the forward dense schedule has the safe sum of
O(K³p⁵), O(n²+n log(n+1)), O(NK), and O(nKp²),
with code, query and metadata included as described.
The sparse format substitutes its actual O(K²p⁴)
stored program, not the dense parameter figure.
If offline and forward buffers coexist, count both;
if an offline buffer is released before forward,
it contributes to its earlier phase peak instead.

This phase rule, rather than the rolling-work entry
alone, defines total peak. The schedule never silently
stores all neural layers for training; if all activations
were retained, that would be an additional cost. All
input/query/endpoint acquisition, residual copy,
identity hold, clearing and final decode operations
are included. Evaluating all K² requested rows as
separate runs costs their actual additional time
and output storage.

For reference, the proved batch-hybrid coordinates are:

|Coordinate|Uniform upper bound / exact structure|
|---|---|
|neural depth; width|O(Kp²); O(Kp)|
|heads total / max layer; max QK dimension; score cap|6 / 4; 2K; 2|
|single coefficient / arithmetic word|<=128p bits, with full products and guards|
|dense slots / parameter bits|O(K³p⁴) / O(K³p⁵)|
|active gates/projections; identity holds|O(Kp²+K²); O(K²p³)|
|sparse program incl coefficients, addresses and holds|O(K²p⁴) bits|
|masks / positions|O(n²+n log(n+1)) bits|
|observed one-hot input|O(NK) bits|
|rolling working arrays, excluding stored data|O(nKp²) bits|
|uncached attention; equally cached attention|O(n²(K+p)p²); O(n²Kp²)|
|dense pointwise / QKV bitwork|O(nK³p⁶)|
|finite rational log work / scratch|O(p³ log²(p+1)) / O(p log(p+1))|
|finite evaluator code|O(p⁴) bits|

The table is accompanied by the explicit offline,
cache, acquisition, formatting and phase-peak charges
above. Dense/sparse and cached/uncached are different
implementation choices, not coordinates that may be
mixed opportunistically in one claimed profile.

## 10. Separate conservative PURE neural expansion

Let T_bit be all online bit operations of the selected
fixed-loop hybrid execution, including copies and
clears, and S_bit its simultaneous live work, input,
masks and public-data bits. If implementing a stored
program interpreter instead of hardwiring control,
include its program bits as constant rails and count
its actual instruction/address work in T_bit. This
definition does not assume a free RAM or addressing
operation: fixed loops can instead be wired directly
to their known locations.

Unroll every loop. Replace each Boolean instruction
by the constant-size ReLU gadget of Section 3,
branching by muxes, and carry all other live bits
through explicit identity wires. Induction on the
finite instruction sequence proves exact equality
of the binary machine state and the encoded neural
state after each step. Initial one-hot/query inputs
are bits, all intermediate arithmetic is bit encoded,
and the final dyadic decode uses finite O(p)-bit
coefficients. A conservative allowance of O(p)
additional stages/channels covers this decode.
It follows that the expanded implementation has

    depth O(T_bit+p), width O(S_bit+p),
    sparse gates/holds O((T_bit+p)(S_bit+p)),
    dense coefficient bits O(p(T_bit+p)(S_bit+p)²),
    generic dense bitwork O(p²(T_bit+p)(S_bit+p)²).

The dense bounds include all zero terms and biases.
All masks and causal data dependencies are inherited
from the finite program, so no future input or new
decoder port is introduced. There is no attention
oracle remaining. This separate flattened realization
does not have the smaller hybrid O(Kp²),O(Kp) layer
and width figures. Its storage, holds and bitwork
are the displayed expanded ones.

## 11. Scope closure and source-to-proof mapping

Sections 2–4 prove the actual finite causal implementation
and <=2/Q head errors (S1). Sections 5–7 prove the exact
path identities, legal directed guards, actual positive
V, ordered output and I (S2). Sections 7–8 prove the
located master and V interfaces, correlated perturbation
bridge and lifetime/fanout properties (S3). Sections
3–4 and 9–10 prove the complete construction charges
and convention distinctions (S4). The parameters are
common and depend only on K,N,h throughout.

This establishes S1–S4 for the fixed Pi and its stated
interfaces. It says nothing about optimality of these
bounds, coordinatewise superiority to strong direct
baselines, reduction of dominant full-network cost,
or all trained Transformers. A different NORM module,
weighted-direct front end, physical injector or
replacement bridge requires its own concrete construction
and cost. These exclusions are precisely S5. The proof
has not run an unavailable old emitter or substituted
another program's exact ledger for a Pi measurement.

The following local sources specify the fixed
construction being proved, and the mapping makes
reuse auditable. They are not needed as external
mathematical premises because the bearing arguments
appear in this body:

|Current local source|Reused content|Location in this body|
|---|---|---|
|inputs/source-v10/inputs/general-assumptions-20261027/stage2/C1-proof-v1.md §§1–7|front end, path algebra, finite logs/exps/softmax, bits/ReLU, directed guards and normalization, charges|§§1–7,9|
|inputs/source-v10/inputs/general-assumptions-20261027/stage2/finiteN-reliability-proof-v1.md §§4–6|corrected 128p/p⁶ fees, complete 9K+1 master interface, fanout/lifetimes, 35/36 propagation|§§7–9|
|inputs/source-v10/inputs/general-assumptions-20261027/stage2/root-proof-v1.md §5|full offline/peak, full-score caches, hybrid/PURE distinction|§§9–10|
|inputs/source-v10/outputs/004-mechanism-reliability/prover/mechanism-proof-v1.md §§5–6|actual positive payload cut before sum, canonical replacement and real V* bridge|§8|
|inputs/source-v10/outputs/005-native-general-handoff/lead/source-dependencies-v1.md|source boundaries and final cost conventions|§§1,9–11|

The current PROBLEM.md general-source definitions
take precedence over old D1 assumptions. The original
strict-positive/stationary statistical portions are
not imported. The current frozen reliability review
located the relevant author proof; its PASS is not
a native predecessor or a substitute for Sections 7–8.
Only the normal submission verdict can admit this
SRC-Pi proof.

The following already corrected source details are
preserved explicitly: h+1 numerator bits at the closed
head-grid endpoint; the guard fractional bit in
1-U/2; exact full products before division; the
ordered final residual; d1,d2,dT and signed guard
ranges; p⁶ dense work; all-n tokenwise execution;
full-score rather than product-of-rounded cache
values; both initial and actual endpoint corrections;
offline generation/format writes and phasewise peak;
and no stale T at the final bank cut. The offline
rational arrays versus online word limit are stated
separately in §9.1. These are explicit implementations
of the fixed source, not a weakened model or a changed
statistical theorem.

All S1–S5 quantifiers and conclusions have therefore
been proved without any admitted Fact predecessor.
End of fixed self-contained submission body.

