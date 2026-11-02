# C1: finite causal realization, deterministic error, and pointwise-law consistency

Fixed proof version v1, 2026-10-25. Project `icml-flow-heads`, contract
`22e80d3d620c36cfc0bbd297101a5efabe634d7fd696b4cae200963af52af02a`.
Exact obligation: `7920eabcfdc46f9f423c5d0b4831cf856320e56ad1fb88f4f70d1f30df2982e5`.
This is a self-contained proposed proof, not an admission. No predecessor Fact is used.
Only the native submission verdict may admit it. C2--C4 and the mother problem remain open.

## 1. The precise claim and finite evaluation convention

Let K>=2, N>=3, M=N-2, and let X_1,...,X_N be any path over {0,...,K-1}.
For a query s=(a,b), set

    n_ij = sum_{t=3}^N 1{(X_{t-2},X_{t-1})=(i,j)},  u_ij=n_ij/M,
    C_ab,c = sum_{t=3}^N 1{(X_{t-2},X_{t-1},X_t)=(a,b,c)},
    c_ab,c=C_ab,c/M,  rho=1/M,
    p^+_N(c|a,b)=(C_ab,c+1)/(n_ab+K).

The counts in this display are mathematical comparison objects, not supplied input
registers. The circuit below never builds a pair or triple table.

For every integer h>=max(4,ceil(log2 M)+1), put

    ell=ceil(log2(N+K+2)), p=4h+4ell+64, Q=2^h, delta=2^(-p).

There is a D3--D5 predictor Pi_{N,h}, with two paid local copying heads and four
statistical heads, such that for every path and every query simultaneously,

    TV(Pi_{N,h}(s),p^+_N(.|s))
       <= K(35 eta+6 zeta+eta)/(u_ab+K/M)+(K-1)/Q
       <= (78M+K-1)/Q,                       (1)

where this construction has eta=2/Q and zeta=1/Q. The first inequality also
holds for arbitrary correlated head-coordinate perturbations bounded by eta,
and multiplication/division errors bounded by zeta, subject to the explicit
exact-bit and clipping hypotheses in Section 4. Pi has nonnegative dyadic
coordinates summing to exactly one. Its ideal unrounded readout is add-one,
including uniform output for a zero context count. Finite output quantization
can give zero coordinates; no log-loss or strict-positive-output claim is made.

The finite model is causal unscaled dot-product softmax attention, no LayerNorm,
ReLU pointwise maps, residual slots, and a specified integer implementation of
finite softmax evaluation. Its scores approximate the specified real D2 logits;
it does not call exact transcendental or rounding oracles. Integer quotient,
rounding, and clipping are implemented by the Boolean/ReLU circuits below.
Rounding to a dyadic head register happens inside that finite attention
evaluator. Scalar-to-bit ReLU conversion is asserted only on this register's
finite grid, not on arbitrary real inputs. This distinction is part of the
implementation model, not an assumption that a continuous ReLU map computes
floor on a real interval. Neural layers and attention-kernel evaluation costs
are both charged, and distinguished in Section 7.

All parameters, masks, constants, and precision choices depend on K,N,h only.
One theta-independent schedule is

    h_N=ceil(log2(128(K+1)(N+1)^3)).          (2)

For every fixed generally nonuniform stationary strictly positive second-order
law theta, this schedule satisfies

    max_s TV(Pi_{N,h_N}(s),theta(.|s)) -> 0 almost surely.       (3)

Actual-terminal almost-sure error, expected error, and each fixed-terminal-state
conditional expected error also tend to zero. This is a growing finite family,
not a fixed finite network consistency theorem. No uniform rate over all
strictly positive theta is asserted.

## 2. Causal wiring and the complete interface

Use N observed positions plus one synthetic query q=N+1 with x_q=0, not an
unobserved next symbol. At historical positions x_t=e_{X_t}. Paid position
metadata stores t,N, a query bit, and z_t=1{t=3}; z_q=0. External query one-hots
and a mode bit live only at q. Position metadata takes O((N+1)log(N+2)) bits.
Masks are explicit Boolean arrays, charged O((N+1)^2) bits (a constant number).
Masked edges do not require a stored numerical minus infinity.

The first attention layer has two heads with zero Q,K and V=x. Their singleton
masks select t-1 and t-2, respectively, falling back to self for unavailable
predecessors. Singleton softmax is exactly 1, and the integer evaluator copies
exactly. Both heads are paid. At t>=3 they produce

    l1_t=e_{X_{t-1}}, l2_t=e_{X_{t-2}};

at q they produce l1_q=e_{X_N}, l2_q=e_{X_{N-1}}. Thus these same two heads
also obtain the actual endpoint E_N, with no extra access to history. Outputs
write initially zero residual slots; x is retained separately. Compute
F_t,c=ReLU(l1_t,c+z_t-1), exactly z_t l1_t,c. Query-mode selection uses
ReLU(v+m-1)+ReLU(w-m): m=1 selects v, m=0 selects w, on bit inputs.
At q choose A,B either from the external s or from l2_q,l1_q. Always keep
l2_q,l1_q separately. External s never replaces E_N. Historical queries can
use their l2,l1, so every evaluated row has bounded scores and bit values.

The second attention layer has four heads. At q its allowed keys are exactly
t=3,...,N. At historical rows use the causal prefix of these keys, or self if
the prefix is empty; these other outputs are unused. The unscaled convention
is softmax(Q dot K), without an unrepresented sqrt(d) factor.

| Head | Q at q | K at a historical key | V at that key | Output |
|---|---|---|---|---|
| P1 | ((log 2)A,(log 2)B) | (l2,l1) | (x,l2) | (q1,v1) |
| P2 | ((log 2)A,(log 3)B) | (l2,l1) | (x,l2) | (q2,v2) |
| T | (log 2)B | l2 | (l1,F) | (h,h0) |
| 0 | 0 | 0 | (l2,l1,F,z) | (alpha,nu,f,rho) |

This table first describes ideal real heads. Section 5 replaces log constants
and softmax evaluation by the specified finite operations. All values are
query-independent bits computed from local causal data and paid flags. QK
dimensions are 2K,2K,K,1; value dimensions are 2K,2K,2K,3K+1, totaling 9K+1.
Only these alphabetic dimensions are O(K), independent of precision.

Clip each returned head scalar to [0,1]. Select U_k=sum_i A_i v_k,i by
ReLU(v_k,i+A_i-1) and exact addition; since A is one-hot this selects one
coordinate and does not multiply its error by K. Select alpha_b and nu_b in
the same way. Let j=sum_i ReLU(B_i+l2_q,i-1), a bit, and
J_c=ReLU(j+l1_q,c-1). Then J_c=1{E_N=(b,c)}. These O(K) gates implement
the actual endpoint correction even when s is external and different from E_N.

The global-layer query interface consists of all 9K+1 head coordinates,
A,B, the external query and mode if retained, actual endpoint l2_q,l1_q,
declared N/position constants, and their query-residual copies. A generous
64K+32 scalar slots before bit expansion cover them. All later work is
pointwise at q; no later attention, readout of historical residuals, hidden
count table, or additional endpoint access is permitted. The historical
working array remains charged evaluation memory, not a readout input. Every
temporary of the readout is covered by the live-register bound in Section 7.
This declares the interface; it is not a C3 adversary or lower-bound theorem.

For K=2 and sign-coded i,a, 1{i=a}=(1+ai)/2. Removing query-row constants
gives beta_1 ai+beta_2 bj with 2beta_1=log 2 and
2beta_2=log(1+lambda). The categorical construction for K>2 follows the table
directly and uses no uniform-binary spectral premise.

## 3. Exact algebra for every finite path

Define alpha_i=sum_j u_ij, nu_j=sum_i u_ij. The uniform head gives exactly
these, rho=1/M, and f_c=rho 1{X_2=c}. The T-head mean weight is
dT=1+alpha_b, and direct summation of its bit values gives

    dT h_c=nu_c+u_bc,
    dT h0_c=f_c+rho 1{(X_1,X_2)=(b,c)}.       (4)

Consequently initial_bc=dT h0_c-f_c is the initial *pair* mass; f_c alone
is only a symbol mass. Let

    g_bc=(dT h_c-nu_c)+rho J_c-initial_bc.     (5)

The lists of pairs (X_1,X_2),...,(X_{N-2},X_{N-1}) and
(X_2,X_3),...,(X_{N-1},X_N) cancel except at their endpoints. Thus
g_bc=M^{-1}sum_{t=3}^N 1{(X_{t-1},X_t)=(b,c)}. This includes M=1;
there is no asymptotic neglect of either endpoint.

For product head k, lambda_1=1,lambda_2=2 and its weight is
(1+1{lag2=a})(1+lambda_k 1{lag1=b}). Therefore

    d_k=1+alpha_a+lambda_k nu_b+lambda_k u_ab,
    d_k U_k=2(alpha_a+lambda_k u_ab),
    d_k=(1+lambda_k nu_b)/(1-U_k/2).          (6)

Here 1-U_k/2 belongs to [1/2,1], d1 in [1,4], d2 in [1,6]. No normalizer
oracle and no division by a rare context frequency is used. If
r_c=M^{-1}sum_t 1{X_t=c} and A_c=M^{-1}sum_t 1{X_{t-2}=a,X_t=c}, then
expanding the product weight gives

    d_k q_k,c=r_c+A_c+lambda_k g_bc+lambda_k c_ab,c.

Subtracting the k=1 identity from k=2 yields

    c_ab,c=d2 q2,c-d1 q1,c-g_bc,
    u_ab=(d2 U2-d1 U1)/2.                   (7)

The first is the prediction readout. The second is an optional consistency
diagnostic, not a separately approximated final denominator. These formulas
operate only on O(K) head coordinates for the supplied query.

## 4. Audited pathwise error table

Assume the clipped head coordinates are each within eta of their ideal values,
the query one-hots, flags, singleton copies and endpoint are exact, and every
readout multiplication or division has absolute error at most zeta. All additions,
subtractions, and multiplication/division by 2 in this section are exact by
keeping the required guard fractional bit. No independence is assumed.
Write hats for computed quantities. Selecting U,alpha_b,nu_b preserves eta.

For n=1+lambda nu_b and v=1-U/2, both original and perturbed v>=1/2,
|hat n-n|<=lambda eta, |hat v-v|<=eta/2, and n<=1+lambda. Thus

    |hat n/hat v-n/v| <= 2 lambda eta+2(1+lambda)eta.

After division error this is 6eta+zeta for d1 and 10eta+zeta for d2.
Also |hat dT-dT|<=eta. For each c,

    |hat dT hat h_c-dT h_c| <= |hat dT-dT| |hat h_c|+dT eta <=3eta,

and the identical bound holds with h0. Subtracting nu or f and charging the
one product gives 4eta+zeta. Multiplication of rho by the exact bit J is exact
selection, so its error is eta. This proves the following table, including its
signs, without treating shared errors as independent:

| Computed quantity | Absolute coordinate error |
|---|---|
| dT | eta |
| d1 | 6eta+zeta |
| d2 | 10eta+zeta |
| dT h-nu | 4eta+zeta |
| dT h0-f | 4eta+zeta |
| rho J | eta |
| g | 9eta+2zeta |
| d1 q1 | 10eta+2zeta |
| d2 q2 | 16eta+2zeta |
| recovered c | **35eta+6zeta** |
| diagnostic (d2 U2-d1 U1)/2 | 13eta+2zeta |

For the product rows use, for example,
|hat d_k hat q_k-d_k q_k|<=|hat d_k-d_k|+d_k eta and then add zeta.
The last row is half the sum of the preceding two product bounds. Clipping
recovered c to [0,1] cannot increase its distance to the true c in [0,1].

For reference, if logits have coordinate error sigma, values error v, and
finite aggregation adds a coordinate error a, the head bound
eta<=v+exp(2sigma)-1+a is valid: normalized weight ratios lie between
exp(-2sigma) and exp(2sigma), so their L1 difference is at most
exp(2sigma)-1. We will use a tighter direct construction instead. This table
does not cover perturbed query bits or perturbed endpoint copies: such errors
change scores/selections and require additional terms. In particular it is
not by itself a solution of C3.

## 5. Finite log, exponential, softmax, and rounded head registers

All online fixed-point arithmetic in this section is integer arithmetic on
the displayed numerators, implemented as in Section 6. There is no stochastic
rounding. A p-fractional-bit grid is used inside softmax; h bits are retained
in its output.

For x=2,3, y=(x-1)/(x+1)=1/3,1/2, respectively, generate the rational

    S_x=2 sum_{j=0}^{p-1} y^{2j+1}/(2j+1),
    L_x=2^(-p) floor(2^p S_x).

The identity log x=2 sum_{j>=0} y^{2j+1}/(2j+1) follows by integrating the
geometric series 2/(1-y^2) from 0 to y (absolute convergence here). Its tail
is at most 2 y^{2p+1}/((2p+1)(1-y^2))<=2^(-2p). Hence

    0<=log x-L_x<2delta.                    (8)

These constants are computed exactly as rationals before the final integer
division, then stored using p fractional bits. This is an explicit finite
construction: for y=1/q, the common denominator
q^{2p-1} product_{j=0}^{p-1}(2j+1) suffices and has O(p log(p+1)) bits.
School arithmetic computes the p numerator terms, their sum, and the final
division in O(p^3 log^2(p+1)) bit operations, using O(p log(p+1)) live bits
with serial accumulation. This parameter-generation cost is charged separately;
the online network stores only the two resulting constants. It uses no oracle.

Use L_2,L_3 in the Q projections. Every dot product is an exact sum of at
most two selected dyadics; zero projection terms can also be evaluated and
charged densely. For each allowed edge, its finite score s satisfies
0<=s<=s_*<=log 6<2 and |s-s_*|<=4delta, where s_* is the ideal score.
The fixed score-range cap is 2. Singleton scores are zero.
The evaluator can form the integer score directly from the stored integer
log numerators and input bits. If a scalar score register is used instead,
the grid-extraction construction of Section 6, with highest index p+1,
extracts its nonnegative integer numerator S<=2^(p+1) exactly. This costs
O(p) gates per edge and is included in the evaluator bound. Thus neither
the score-to-integer nor the head-to-bit interface is implicit.

To evaluate exp(s), set J=8p, R=2^p, S=R s (an integer), and integers

    T_0=R,
    T_j=floor(T_{j-1} S/(j R)), j=1,...,J,
    W=sum_{j=0}^J T_j,  hat w=W/R.          (9)

Every product and quotient here is computed exactly by integer algorithms;
the quotient implements the one stated downward truncation. No separate
rounded multiplication is inserted before it. All terms are nonnegative.
Inductively T_j/R<=s^j/j!, so 1<=hat w<=exp(s)<=exp(s_*)<=6.

Let e_j=s^j/j!-T_j/R. Then 0<=e_j<=s e_{j-1}/j+delta.
An error introduced at step k contributes at most
delta sum_{r>=0}2^r/r!<8delta to the sum of all later term errors, since
(k+1)...(k+r)>=r!. Thus sum_{j=1}^J e_j<=8J delta.
For j>=9, 2^j/j!<=2^(-j) (check j=9 and use the ratio 2/(j+1)<=1/2).
It follows that sum_{j>J} s^j/j!<=2^(-J)<=delta. Finally the mean value
bound for exp on [0,2] is less than 8, so

    0<=w_*-hat w<=(64p+1)delta+32delta<=100p delta,             (10)

where w_*=exp(s_*) is the ideal product/partial/uniform weight.

For a row with m>=1 allowed keys, sum W exactly into denominator D and,
for each bit value coordinate v_t, numerator A=sum_t W_t v_t. No intermediate
fractional rounding occurs in these sums; D/R is in [m,6m]. Produce the head
coordinate H=2^(-h) floor(2^h A/D). This is an integer long division.
The ideal corresponding numerator and denominator differ by at most
m(100p delta); both finite and ideal denominators are at least m. Since a
normalized numerator is in [0,1], subtraction of the two ratios gives

    |A/D - ideal head coordinate| <=200p delta.

The final head quantization consumes its own error, strictly less than 2^(-h).
For p>=32, 200p<=2^(p/2) (true at 32 and preserved as p increases);
our p>=4h+64 gives 200p delta<=2^(-h). Therefore every head coordinate lies
on the **closed** h-grid [0,1] and has error at most eta=2^(1-h).
All four heads and all paths obey this same bound. At a singleton the ratio
is exactly its bit value, so copying is exact. Uniform/partial heads are
evaluated and charged by the same scheme. No assumption on N versus a hidden
machine word is needed: the integer part includes log(N+1) bits.

## 6. Explicit ReLU/bit readout, signs, and exact simplex

Here is the local gate basis. For bits u,v,
AND(u,v)=ReLU(u+v-1), NOT(u)=ReLU(1-u), and
XOR(u,v)=ReLU(u-v)+ReLU(v-u). OR follows from u+v-AND(u,v).
Each uses a constant number of ReLU neurons/layers. Identity wires for every
still-live bit are explicit, paid coefficients; nonnegative identity is ReLU.
Signed quantities use a sign bit and magnitude bits (or two nonnegative rails).

For completeness, ripple addition computes sum_i=XOR(XOR(a_i,b_i),carry_i)
and carry_{i+1}=OR(AND(a_i,b_i),AND(carry_i,XOR(a_i,b_i))). It has O(w) gates
and O(w) depth on w-bit words. Subtraction/borrow and lexicographic comparison
follow the same bit recurrence (compare high-to-low keeping equal/less bits).
A mux uses two bit ANDs and OR. School multiplication adds the shifted partial
products selected by each multiplier bit, retaining 2w bits: O(w^2) gates,
O(w^2) sequential depth and O(w) live scratch bits, with a constant number
of w-bit registers. Restoring division processes numerator bits high-to-low, shifting a
remainder and conditionally subtracting the positive divisor; the remainder
after a step is below the divisor. There are O(w) steps of O(w) gates, with
O(w^2) gates/depth and O(w) live bits. These constructions implement floor
integer quotient exactly. Loop lengths depend on K,N,h only and are unrolled.
No lookup table or uncharged variable-length program is used.

Scalar-to-bit interface: a rounded head H has integer A=QH in [0,2^h].
Extract bits from index j=h down to 0 by

    b_j=ReLU(A_j-(2^j-1))-ReLU(A_j-2^j),
    A_{j-1}=A_j-2^j b_j,

starting A_h=A. On integer inputs with 0<=A_j<2^{j+1}, b_j is exactly the
indicator A_j>=2^j, and 0<=A_{j-1}<2^j. The initial condition holds even
at A=2^h. The result uses **h+1 bits**, including the bit for H=1. Scaling by
Q, thresholds, and all residuals are exactly represented and paid; the map
is O(h) depth and gates per scalar, plus carry wires. For non-grid inputs it
is merely a continuous piecewise-linear function, not a floor algorithm.

This closes a concrete possible checkpoint defect: using only h bits for an
h-fractional-bit coordinate including 1 encodes A=2^h incorrectly. At h=1,
feeding A=2 into a one-bit version returns b0=1 rather than the required
two-bit code 10. The repair above preserves the endpoint 1. The diagnostic
was recorded natively as failure 6e15980b1981fd58b640187c627834bcf1c5a0452f9859e2576b7a567c0a963b.

Head-coordinate selection may precede or follow this expansion. When the
scalar formula ReLU(v+A_i-1) is used, it is exact on [0,1] and bit A_i, with
all additions exactly representable. Selection never treats a noisy real
one-hot as a bit. Clipping on a scalar is ReLU(x)-ReLU(x-1), or exact compare
and mux on a signed word; both implement projection onto [0,1].

Let all clipped head coordinates now have integer numerators over Q. If U,V
are the numerators of hat U_k,hat nu_b, compute the numerator of hat d_k as

    D_k=floor(2Q(Q+lambda_k V)/(2Q-U)).       (11)

The denominator is in [Q,2Q], so this is well defined and
hat d_k=D_k/Q differs from the exact ratio of its input coordinates by less
than zeta=1/Q. This formula implements the half without rounding away its
extra bit. hat dT=1+hat alpha_b is exact. A product of two nonnegative
h-grid numbers with numerators A,B is represented by floor(AB/Q)/Q;
its error is less than zeta. Use this operation for dT h, dT h0, d1 q1,
d2 q2. Additions and subtractions in (5),(7) are exact signed integer
operations. rho J is exact bit selection. If the optional u diagnostic is
formed, keep h+1 fractional bits for its final division by 2.

The directed implementation has hat d1 in [1,4], hat d2 in [1,6], hat dT
in [1,2]. Products with a clipped head lie in [0,4],[0,6],[0,2], respectively.
Thus hat u_bc and hat initial lie in [-1,2], hat g in [-3,4], the difference
hat d2 hat q2-hat d1 hat q1 in [-4,6], and recovered hat c in [-8,9].
The conservative signed range [-16,16] therefore suffices for this readout.
It is not a claim for unbounded arbitrary arithmetic noise. The internal
integer multiplications/divisions retain their full products, with O(p)
integer-bit room, and only the declared final quotient is truncated.

Put a_c=clip(hat c_ab,c,0,1). Set

    r0=2^(-ceil(log2 M)-1), r=max(hat rho,r0), x_c=a_c+r.

r0 is on the h-grid, 0<r0<=rho/2, and clipping/max fixes the true rho;
hence |r-rho|<=eta. Each x_c is a positive h-grid number in (0,2]. Let
V_c=Q x_c be its positive integer numerator and T=sum_c V_c>0. Implement

    m_c=floor(Q V_c/T), 0<=c<K-1;
    m_{K-1}=Q-sum_{c<K-1}m_c;
    Pi_c=m_c/Q.                             (12)

The integer long division, sum, subtraction, and final dyadic linear decoding
are all paid. Since each first quotient is below its exact normalized share,
their sum is <=Q; thus the last coordinate is nonnegative and every coordinate
is at most 1. The total is exactly 1, including cases where Q<K. If
epsilon_c=V_c/T-m_c/Q in [0,1/Q) for c<K-1, the last-coordinate error is
sum_{c<K-1}epsilon_c, and

    TV(Pi,x/sum x)=sum_{c<K-1}epsilon_c <=(K-1)/Q.              (13)

This also shows why simply rounding K separate normalized coordinates is
insufficient: already (1/3,1/3,1/3) rounded downward on the half-grid sums to
zero. The last-residual rule is asymmetric and part of the visible code.

For positive vectors x,y, the triangle inequality after adding/subtracting
x/sum y gives

    ||x/sum x-y/sum y||_1
       <= |sum y-sum x|/sum y + ||x-y||_1/sum y
       <=2||x-y||_1/sum y.

Use y_c=c_ab,c+rho and Section 4 to get ||x-y||_1<=K(35eta+6zeta+eta),
sum y=u_ab+K/M. This proves the first bound in (1), and the second follows
from u_ab+K/M>=K/M, eta=2/Q,zeta=1/Q. With exact ideal data, x=y and
x/sum x=(C+1)/(n+K); if n=0 it is uniform. No rare-frequency inverse-square
factor has been introduced.

## 7. Complete resource accounting and execution schedule

All O constants below are universal, independent of K,N,h and theta.
Bounds are conservative upper bounds for this specified construction, not
optimality or superiority claims. Put n=N+1. The fixed alphabetic interface
is as in Section 2; actual neural channels contain bit expansions and work.

Execute the scalar grid extractions in parallel across the O(K) coordinates,
then process the O(K) arithmetic quantities in Sections 4 and 6 serially.
Each school product/quotient uses O(p) scratch bits and O(p^2) gates/depth;
K coordinate outputs, all head inputs and permanent query/endpoint registers
remain live. Summation/selection uses at most O(Kp) additional gates. Thus a
pointwise ReLU network of width W=O(Kp), depth L=O(Kp^2) implements all gates,
with nonnegative bit/rail identity wires at every intervening layer. Add the
constant number of copying/flag/global-attention stages. The same network can
be evaluated at each token, with only q's output used. Queries in unused rows
use legal bounded inputs and nonempty fallback masks, as specified earlier.

Choose online parameter and arithmetic word lengths B_param,B_arith <=C p
for a universal C (for example a sufficiently generous fixed multiple such
as 64p bits). One can use signed fixed words with 16p integer and 16p fractional
positions, retaining full double-width products before exact truncation;
this is still a fixed multiple of p. To check range: scores<2, exponential
term integers<8*2^p, their products need <=2p+6 bits, denominators j*2^p
need p+log2(8p)+1 bits, row sums <=6n*2^p need p+ell+4 bits, and final
simplex T<=2KQ needs h+log2 K+2 bits. The final dividend QV<=2Q^2 needs
2h+2 bits. Bit extraction coefficients have magnitude <=2^h, and its
intermediates <=2^h. Pointwise arithmetic is either bounded signed scalar
readout or a Boolean circuit. Dense evaluation of its specified matrices
has O(Kp) summands per neuron; retaining another O(log(Kp)) integer guard
bits still fits Cp, because p>=4ell+64. There is no overflow, rounding
of Boolean gates, or lost fractional bit at subtraction.

The resource vector, in the usual attention/pointwise layer convention, is

    R=( L=O(Kp^2), W=O(Kp),
        H_total=6 (two attention layers, maximum 4 simultaneous),
        D_qk=2K, B_param=O(p), B_arith=O(p), score_range<=2 ).   (14)

If H is defined as maximum heads per layer rather than total head modules,
H=4 and the separate total is 6. This states the convention explicitly.
Ordinary dense QKV maps are included, not treated as free one-hot selectors.
The following bounds include readout multipliers/quotients and their holds:

| Resource | Bound for this implementation |
|---|---|
| Dense neural coefficient slots, including zeros and biases | O(LW^2)=O(K^3 p^4) |
| Dense stored parameter bits | O(K^3 p^5) |
| Sparse nonzero arithmetic gates/projection coefficients before holds | O(Kp^2+K^2) |
| Explicit identity/hold wires across layers | O(LW)=O(K^2 p^3) |
| Sparse program+parameter bits including addresses, holds | O(K^2 p^4) |
| Position and explicit mask bits | O(n log(n+1)+n^2) |
| Rolling online activation/temporary bits, excluding parameters/masks | O(n K p^2) |
| Extra parameter-generation workspace | O(p log(p+1)) |
| Parameter-generation bit operations | O(p^3 log^2(p+1)), plus writing chosen parameter format |
| Finite attention score/exp/aggregation bit operations | O(n^2(K+p)p^2) |
| Dense pointwise/QKV bit operations | O(n K^3 p^6) |

Here sparse addresses need O(log(LW+1))=O(p) bits, so the sparse program
bound counts both coefficients and wiring, including all carries. Dense
parameters can be chosen as the actual storage convention, giving total
stored bits O(K^3p^5+n^2+n log(n+1)), and peak online bits including these
O(K^3p^5+nKp^2+n^2+n log(n+1)). A sparse implementation can instead use
its displayed storage bound; it does not inherit an unproved speed advantage.
Retaining all layer activations for training would multiply activation
storage by L; the claimed forward evaluator uses two rolling layers.

To justify the attention bound, score and value operations for an edge cost
O(Kp^2) by ordinary p-bit multiplication, (9) has O(p) product/long-division
steps costing O(p^2) each, and bit-valued aggregation needs at most O(Kp^2).
There are O(n^2) allowed/scanned edges and O(nK) output divisions. Stream
one row's weights into its K accumulators; do not retain the entire weight
matrix. All input QKV values needed for this stream are in the charged
rolling token array. Even if numerical weight matrices were retained, they
would cost an additional O(n^2p) bits, which is not part of our streaming
schedule. Densely evaluating LW^2 products at every position with generic
Cp-bit multiplication costs O(n L W^2 p^2)=O(n K^3p^6), not p^5.

L in (14) counts neural/Transformer layers, not the number of machine gates
inside one softmax primitive. Nothing inside that primitive is free: its
algorithm, words, memory and operations were just specified. For a convention
that counts every finite evaluator arithmetic gate as a neural layer, one
may also unroll the entire finite evaluator as a causal Boolean/ReLU circuit:
serialize the O(n^2(K+p)p^2+nKp^2) active bit gates and retain O(nKp) live
bit channels, with fixed routing for the already declared edges. This gives
depth O(n^2(K+p)p^2+nKp^2), width O(nKp), and explicit carry-wire count
bounded by their product; each Boolean gate has constant ReLU depth. Large
grid-scaling coefficients still use O(p) bits. Its dense coefficient slots
are bounded by depth times width squared, and stored bits by another O(p).
This optional flattened evaluator is a much larger implementation, not an
O(K) neural-width claim. It implements the same finite causal softmax program,
not a new information path. The principal resource table uses the standard
charged-attention convention and already accounts for every operation.

One query is evaluated per run. Taking max_s in a theorem is a mathematical
maximum over this same family, not free parallel output for K^2 queries.
Running all K^2 queries independently costs K^2 times the stated inference
time and corresponding output storage. All masks, schedules, carries,
parameter-generation and readout operations are available to a same-budget
baseline as well; these bounds claim no advantage over such a baseline.

## 8. Theta-independent schedule and nonuniform-law consistency

The schedule (2) satisfies the required h lower bounds for all K>=2,N>=3.
Since 78M+K-1<=128(K+1)(N+1), (1) gives the uniform pathwise bound

    max_s TV(Pi_{N,h_N}(s),p^+_N(.|s)) <=(N+1)^(-2).          (15)

For a requested implementation error epsilon>0 at fixed K,N, one may instead
take h to be the maximum of 4,ceil(log2 M)+1, and
ceil(log2((78M+K)/epsilon)). This is still theta-independent. These are
implementation bounds, not finite-N sampling-risk claims.

Here is a proof of the probabilistic step that does not assume uniform pair
frequencies. Let Y_j=(X_{j+1},X_{j+2}), j>=0. Its finite-state transition
matrix is P_{(i,j),(j,c)}=theta_{ij,c}. In two steps,

    (P^2)_{(i,j),(r,s)}=theta_{ij,r} theta_{jr,s}>0.

Let d=K^2 and mu=min_{v,w}(P^2)_{v,w}>0. Then P^2 has every row at least
d mu times the uniform distribution; subtracting that common part proves
TV contraction by 1-d mu. A stationary distribution exists by taking a
convergent subsequence of finite-state Cesaro averages and using their
telescoping stationarity defect. Contraction gives uniqueness and geometric
convergence (the case d mu=1 has immediate two-step convergence). Its
coordinates pi_s=sum_v pi_v(P^2)_{v,s} are all >=mu>0. This pi need not be
uniform, and mu is used for this fixed-law proof only, never as input.

For any function f with pi f=0, g=sum_{j>=0}P^j f converges uniformly on
the finite state set by that contraction and solves g-Pg=f. Along the chain,

    sum_{j=0}^{M-1} f(Y_j)
      =g(Y_0)-g(Y_M)+sum_{j=0}^{M-1}(g(Y_{j+1})-Pg(Y_j)).

The last sum has bounded martingale differences. Such a sum divided by M
converges to zero almost surely: conditional centering and boundedness by C
give the elementary exponential-moment bound
E[exp(t D_j)|past]<=exp(t^2 C^2/2); iterating and optimizing t gives
P(|sum_{j<M}D_j|>=M epsilon)<=2 exp(-M epsilon^2/(2C^2)). Summation over M,
Borel--Cantelli, and rational epsilon>0 prove the assertion. The exponential
moment bound follows by convexly bounding exp on [-C,C] and then
cosh(tC)<=exp(t^2 C^2/2), so it introduces no unproved mixing-rate premise.
Taking f=1{state=s}-pi_s proves u_s=n_s/M ->pi_s almost surely.

For each s,c the differences

    Z_j=1{Y_j=s}(1{X_{j+3}=c}-theta_{s,c})

are bounded martingale differences conditional on the observed history
through X_{j+2}. The same argument gives
C_s,c/M-theta_s,c n_s/M ->0 almost surely. There are only finitely many
s,c for fixed K; intersect their probability-one events. Hence simultaneously

    u_s ->pi_s>0, c_s,c ->pi_s theta_s,c,
    (c_s,c+1/M)/(u_s+K/M) ->theta_s,c.

Taking finitely many maxima and then using (15) proves (3), without a common
positivity/mixing bound over theta.

Let Z_N=max_s TV(Pi_{N,h_N}(s),theta(.|s)); it is in [0,1] and tends to zero
almost surely, hence E_theta Z_N ->0 by bounded convergence. The actual
endpoint is E_N=Y_M, obtained by the two copied endpoint slots, and its mode
output agrees exactly with the externally queried output evaluated at that
same s. Therefore

    TV(Pi_{N,h_N}(E_N),theta(.|E_N)) <= Z_N

pointwise, proving both almost-sure actual-terminal consistency and vanishing
actual-terminal expected TV. Under the stipulated stationary initialization,
P_theta(E_N=s)=pi_s>0 for every N. For each fixed s,

    E_theta[TV(Pi_{N,h_N}(E_N),theta(.|E_N)) | E_N=s]
       <= E_theta Z_N/pi_s ->0.             (16)

There is no independence assumption between history, output, and terminal
query. Fixed-context expected risk and any frequency-weighted TV risk also
vanish by the same maximum bound. These conclusions concern prediction of
the actual next-symbol conditional law theta(.|E_N); they make no unproved
finite-N uniform stochastic or log-loss claim.

## 9. Source audit, repairs, and native scope

PROBLEM.md was read completely (SHA256
882e1705c029384ef98b791df1fae20da5d074ceeaf8962eb5d5795e370b5531).
The complete unadmitted checkpoint and its implementation audit were read:
checkpoint SHA256 c4bfa424325aae9d8895500824e079ffdce252eb99bfb2b38d2208ef40a465c0;
audit SHA256 e792c5b7044ceec55824591d40afff4e9ba6dec3fa6ad6d455bf876b366f1ce1.
They remain untouched. The path algebra and 35eta+6zeta table survive the
audit with the explicitly stated exact-bit hypotheses. The repairs are the
closed-grid integer bit, a fully directed finite transcendental evaluator,
a separately charged final head rounding, explicit signed ranges, exact
integer simplex normalization, paid holds, and the dense p^6 operation bound.
The old unsupported p^5 cost is not retained. The coefficient-generation
cost and kernel-versus-neural-layer convention are now explicit.

No large path enumeration or old compiler expansion was used. Any companion
implementation checks are only diagnostics and are not premises of this proof.
This proof alone does not establish its later independent acceptance.






Completion of this exact C1 obligation is not
closure of C2 finite-history same-budget comparison, C3 located-error
stochastic reliability, C4 integration, or the v10 mother objective.
