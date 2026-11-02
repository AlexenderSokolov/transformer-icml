# Exact-kernel rank and charged finite strong comparison

Fixed v2-r1, 2026-10-25. First bounded schedule repair. Project icml-flow-heads; contract
22e80d3d620c36cfc0bbd297101a5efabe634d7fd696b4cae200963af52af02a.
Exact parent obligation:
756901406268f84ece37ef08e3971802de1a5b528df804bc5275cd1e8a793c9c.
This document proposes a proof; only the native independent verdict admits it.
Fixed repair artifacts and the input/output manifest are in
outputs/005-budget-comparison/counter/comparison-v2/repair-r1/.
No root completion or final audit is claimed.

The three and only native predecessors are:

|Fact|Evidence|Use at its admitted scope|
|---|---|---|
|b2f4d10fa0a69e00|15df56a560e38b8bb7fc84382d374a1e31298a0463efdbde0ab5e20f044291f3|C1 causal finite D3, exact integer/ReLU primitives, nominal arithmetic/error/resources|
|bcd4541db2cf4c1a|f652dccd9b59f4953ab3a0939081d221dede8640e1e8615398b6aba5d00e5b87|B-C-snap, D3-snap, common integer simplex code, total grid-port margins and complete costs|
|f9a79122946f24c5|68832ce6bd94b4b08ae357de5d2e4fb34e7c0fb46ae72da5b44809faecc87cec|single-path finite-N bounds, complete finite visible code, grid attack on original decoder and finite P1 bypass|

All are read back VALID/PASS. Fixed hashes of their artifacts, the new Lead
candidate and exact primary passages are recorded in the accompanying manifest.
The earlier diagnostic failure 2311d6360469a3ac6a2f0f3689e3ac34c6f76948732549a6a17ed4ef836cf10a
is preserved: it was a genuine missing-premise diagnosis at its time, not a
refutation. The new admitted premises repair those specific missing dependencies.
No earlier draft, previous-stage Fact or teammate conversation is an additional
proved premise.
The v2 submission was genuinely rejected as wrong, with native failure
847a1b69725044466c15af52f8db672519415d41471d284f058cf5f9b2bee745: its
general-K ledger assumed parallel wide selection while its emitter serialized
that phase. The old proof/request/return remain frozen. This repaired complete
proof uses an implemented parallel birth schedule and recomputed resources in
§6; it retains the separately identified binary serial instance in §7. The
three predecessors, original Pi and its C3 experiment are unchanged. [Non-scientific operational metadata omitted.]
[Non-scientific operational metadata omitted.] other
native budget dimensions are unlimited.

## 1. Fixed objects and the classification proved

Let K>=2,N>=3,M=N-2,n=N+1. Histories, external pair queries and the actual
terminal query E_N are exactly D1. There is no X_{N+1} input. Define the
mathematical counts C_(s,c),n_s,successor marginal counts n_c over t=3,...,N.
They are not supplied as predictor registers. Put

    h>=max(4,ceil(log2 M)+1), Q=2^h,
    ell_N=ceil(log2(N+K+2)), p=4h+4ell_N+64, R=2^p,
    m=ceil(log2(M+1)), k=ceil(log2(K+1)),
    G_h={A/Q: A=0,...,Q}.                              (1)

Compare four explicitly charged predictors with common observed information:
the accepted original Pi_(N,h), D3-snap, B-C-snap, and the finite B-J-snap
constructed in §4. Original Pi, its admitted C3 experiment and its output
rounding are unchanged. The other three are named alternative readouts/front
ends, not revisions of that acceptance.

All use C1's causal unscaled-dot-product finite softmax convention, fixed
declared masks and pointwise ReLU computation, without LayerNorm. There is
no free sqrt(d) compensation or changed numerical-normalization convention.

The results are:

1. The minimum rank of the exact complete-context logit kernel modulo row
   constants is K^2-1. Its precise representation-only scope is §2.
2. The new finite B-J construction uses full score range 2, the actual
   finite exponential integers, K^2 paid pair features and K^2-1 Q/K
   dimension. At Q>=4M it recovers exact transition counts by integer
   correction, without exact transcendental/normalizer/floor oracles.
3. At common Q>=256M, the three snapped variants have bitwise identical
   outputs and inherit the admitted g_snap finite-N risk bound. Original
   Pi retains its separate g_delta bound and fixed-decoder failure/bypass.
4. Complete resources are constructive/computable, with a genuine binary
   componentwise feasibility result in the fixed serial C1 dense layout:
   B-C-snap fits that original Pi allocation without increasing D3's width,
   layers, words, stored bits, peak work or forward operations. The original
   allocation is determined solely by the original C1 arithmetic, before
   building the baseline. This is a statement about this specified finite
   lowering, not all optimized implementations of D3 or all architectures.
5. General-K constraints are actual tradeoffs: this exact joint kernel
   exceeds D3's Q/K cap for K>=3, while explicit uniform counting pays its
   K^3 table. No universal resource optimum, risk dominance or minimal-head
   conclusion follows. Primary comparison and exact remaining limits are §9.

## 2. Exact complete-context rank, only as a kernel statement

Write d=K^2. For beta>0 and arbitrary r in R^d, on the subspace
H={x:1^T x=0}, (beta I+r1^T)x=beta x. Hence the image contains H and
the rank is at least d-1. Taking r=-(beta/d)1 gives beta times the
orthogonal projection onto H, with rank exactly d-1. Consequently

    min_r rank(beta I_d+r1^T)=d-1.                      (2)

The unshifted matrix has rank d. If two rows of finite logits have equal
softmax probabilities, ratios of any two probabilities in that row show
that their logit differences are equal. Thus their logits differ only by
a row constant. Any bare bilinear QK^T representing the specified exact
kernel on d independent queries and keys has dimension at least d-1.

This is sharp. Index the last pair by d. Use keys k_j=(1{j=l})_(l<d)
and queries q_s=beta(1{s=l}-1{s=d})_(l<d). The last row has been shifted
by -beta, and each row has range beta. This is an explicit factorization.
The theorem covers neither extra pair-dependent biases nor charged nonlinear
score circuits, multiple heads, history-dependent representations, approximate
kernel matching or probability readouts. In particular it is not a finite-N
prediction lower bound or a lower bound on all one-head predictors.

## 3. Complete visible finite code and bypass audit

Use the admitted finiteN proof §5's exact cut and lifetimes, not only selected
coordinates. The four statistical banks are

    (q1[K],v1[K]), (q2[K],v2[K]), (hvec[K],h0[K]),
    (alpha[K],nu[K],f[K],rho),                           (3)

total 9K+1. In addition the decoder sees A/B, external query and mode,
actual endpoint one-hots l2_q,l1_q, declared K,N,M,h,p,positions,masks,
zero synthetic-token/flag slots and all declared query-residual copies.
All copies of a statistical master descend from the same post-quantization
port. An error at that port precedes all fanout. The old evaluator's row
denominators, numerators, score/exp scratch, projected arrays and historical
working arrays are dead/cleared before that cut and are not decoder inputs.
Their real work, clearing and memory are charged in the admitted schedule.

The two paid singleton heads produce both lags at historical tokens and the
actual endpoint at q. Early fallback rows are outside the statistical query
mask. There is no additional endpoint head or future symbol. History values
are query-independent functions of local copied symbols and the position
flag. The initial flag vector z_t l1_t is required: uniform f alone identifies
X2, whereas the partial h0 bank supplies the selected initial-pair correction.
Actual endpoints are retained even for an external query different from E_N.

For ideal heads the admitted C1 identities are

    d_k=(1+lambda_k nu_b)/(1-v_k,a/2), lambda_1=1,lambda_2=2,
    g_bc=(1+alpha_b)hvec_c-nu_c+rho J_c
                       -((1+alpha_b)h0_c-f_c),
    c_(ab,c)=d2 q2,c-d1 q1,c-g_bc.                       (4)

These include both boundary endpoints, with no N->infinity substitution.
Finite normalizers/products/quotients are exactly the admitted truncations;
their correlated frequency error is <=35eta+6zeta, not an uncharged count.
An additional useful ideal audit identity is, for every lag2 coordinate i,

    u_ib=[d_k v_k,i/(1+1{i=a})-alpha_i]/lambda_k.        (5)

Indeed the corresponding unnormalized numerator is
(1+1{i=a})(alpha_i+lambda_k u_ib). Thus the complete v_k, not only U_k,
contains an entire empirical pair column. In binary K=2 that column plus
alpha determines the other column. This is an identity, not a stochastic
prediction-risk lower bound; finite use must pay for its errors and arithmetic.

The audit rules out these invalid failure mechanisms:

|Damaged object|Surviving information that must be checked|
|---|---|
|derived U,d,g,c or one late copy|Original masters permit paid recomputation unless the master port itself is replaced before fanout.|
|only one binary head coordinate|An intact complementary coordinate can exploit a known simplex relation in the ideal code; finite independent downward rounding must also be charged.|
|rho / alleged lost sample length|N is declared. Paid integer division or count snapping can exploit known M.|
|endpoint correction / replacing endpoint by external s|Both actual endpoint one-hots remain; mode does not overwrite them.|
|only P2 next-symbol master|P1, both complete v vectors and all auxiliary banks survive; the admitted unknown-XOR P1 counterconstruction works.|
|a summary collision with historical RAM/evaluator numerators accessible|The information model has changed. Raw history enables paid direct counting; the admitted summary experiment has no such port.|

The admitted finiteN result is stronger than a collision example: at its rational
witness K=2,N=2^25,h=39,p=324, on the declared unknown genuine second-order
XOR family, expected actual-terminal TV is <.021 for clean original Pi,
>.10 for its specified decoder under the stated integer P2 attack, and <.032
for its paid P1 replacement under the same attack. These are native admitted
finite-N bounds, not rederived/simulated here. They use the full surviving
code and a single correlated path event. They do not say that all decoders
fail; the P1 replacement explicitly disproves that inference. The new snapped
or B-J readouts are not silently substituted into that original experiment.

## 4. Finite joint matching and exact integer correction

Put F=K^2. With the same two local heads and endpoint/query-mode convention,
form F history bits Y_ij=ReLU(l2_i+l1_j-1), and F query pair bits from A/B.
Both banks, all projections, values and modes are paid. A joint-match head
reads next-symbol one-hot; a uniform head reads (next-symbol one-hot,Y,z).
Total statistical values are F+2K+1. Historical values remain query-independent.

Use the rank-achieving Q/K factorization of §2 with beta=2. At the last
query row its dot-product scores are -2 for other keys and 0 for the last
key. Before finite exp, compute and add the row constant 2 P_query,last.
The selector, integer addition, cache/control and storage are charged.
All resulting scores are exactly 0 or 2. Q/K dimension remains F-1: the
row shift is a stated evaluation operation, not an extra bilinear feature
or an unreported pair bias. This is legal finite softmax evaluation under
D5, since for exact real softmax a common row shift cancels from numerator
and denominator; the specified finite algorithm evaluates the shifted
formula. There is no finite exp call on a negative logit. If a different
model forbids even charged row shifts inside evaluation, its replacement
is an extra constant-key coordinate (dimension F), which must be reported;
that is a different restricted model, not the present D5 convention.

The finite C1 evaluator at score 0 has weight R. At score 2 its actual
integer weight is generated offline by exact integer arithmetic:

    T0=R, Tj=floor(2 T_(j-1)/j), j=1,...,8p,
    E=sum_j Tj, Delta=E-R.                              (6)

The T0,T1,T2 sum is 5R; all other terms are nonnegative. Downward recurrence
gives E<=R sum_{j=0}^{8p}2^j/j!<R exp(2)<8R. For the last elementary
bound, the sum through j=4 is 7; the tail from j=5 is at most
(4/15)/(1-1/3)=2/5, since subsequent ratios are <=1/3. Thus

    5R<=E<8R, 4R<=Delta<7R, E/Delta<=5/4.              (7)

Computing/storing E is finite school arithmetic, O(p^3) bit operations
and O(p) live bits, or the same repeated evaluator if caching is disabled.
The new architecture does not use exact exp(2), log constants or normalizers.

The uniform outputs are floor(Q n_c/M)/Q and floor(Q n_ij/M)/Q. Select
the query's pair coordinate with F gates and a sum, then use the admitted
paid count-snap circuit on that coordinate and the K successor marginals.
At Q>=2M it recovers exact n_s,n_c. All F returned pair coordinates and
their materialized storage/projection/selection costs remain charged.

The finite match head's denominator and returned integer numerator are

    D=RM+Delta n_s,
    A_q,c=floor(Q(R n_c+Delta C_(s,c))/D).               (8)

These are identities of the implemented integer attention evaluator. D is
reconstructed from paid recovered n_s, not an exposed normalizer oracle.
With epsilon_c in [0,1) denoting the discarded fractional part, define

    B_c=D A_q,c-QR n_c=Q Delta C_(s,c)-D epsilon_c,
    Bbar_c=clip_integer(B_c,0,Q Delta M),
    C*_c=floor((2Bbar_c+Q Delta)/(2Q Delta)).            (9)

Before clipping, B_c/(Q Delta) differs downward from the true count by
strictly less than D/(Q Delta)<=ME/(Q Delta)<=(5/4)M/Q.
Clipping is nonexpansive to the true count in [0,M]. If Q>=4M, the
distance is strictly below 5/16<1/2; the admitted half-up count argument
then proves C*_c=C_(s,c), for every history and query. This new proof
uses only the integer identities, not ideal softmax approximation.

All expressions are implemented with legal signed/unsigned Boolean/ReLU
words. In all admissible bad-input cases the snapped uniform counts still
lie in [0,M], so RM<=D<=EM. A_q,c is a closed-grid numerator in [0,Q],
and -QRM<=B_c<=QEM. Use a signed word of

    w_J=p+h+m+k+16                                    (10)

bits for these integers and full products. They are strictly inside its
signed range, since E<8R. Compare sign/magnitude (or equivalent two's-
complement signed words), clip with comparison/mux gates, then divide by
the positive integer 2QDelta with the school restoring circuit. No real
floor is used. After clipping/rounding every C*_c is in [0,M], including
outside recovery. The shared final program is exactly

    T=sum_c C*_c+K, m_c=floor(Q(C*_c+1)/T), c<K-1,
    m_(K-1)=Q-sum_(c<K-1)m_c.                          (11)

It is total: K<=T<=KM+K, not merely M+K on bad inputs. Dividend,
denominator, count and output buffers fit (10); each output needs h+1
bits including endpoint Q. The predecessor proves legality, zero-count
handling and TV <=(K-1)/Q to add-one after exact count recovery. Its
arithmetic/gates/lifetimes are reused, not reproved as a free primitive.

At common Q>=256M, §§4 and the count-snap Fact show

    B-J-snap(s)=B-C-snap(s)=D3-snap(s)                  (12)

as identical integer output words, for all histories and queries. This
does not identify any of them with original Pi.

There is a nonempty restricted correlated grid-port margin. Let delta_U,
delta_q bound total coordinate changes AFTER clipping and re-storage on G_h,
in the uniform and match masters respectively, injected before all fanout.
Queries,endpoints,feature/binding bits,length,cache constants and subsequent
arithmetic are exact. Uniform count recovery is sufficient under
M(1/Q+delta_U)<1/2, with the admitted strict-floor nominal boundary at
Q=2M separately valid. Once those counts are correct, (9)'s count error is
strictly bounded by

    (5/4)M(1/Q+delta_q).                               (13)

If this is <1/2, output (12) stays nominal. For example at Q>=8M,
delta_U=delta_q=1/Q is a genuine nonzero-grid radius satisfying both.
At the common Q>=256M, the same radius 1/Q also satisfies the admitted
D3-snap margin M(76/Q+35/Q)<1/2 and B-C's margin. Thus all three snapped
codes keep their common nominal output under their declared total-radius
post-aggregation port model; original Pi retains its separate g_delta bound.
Correlations are unrestricted; extra re-encoding belongs in delta. If
the margins fail, only this exact recovery guarantee ceases. The circuit
still produces a legal simplex with T<=KM+K. No all-decoder lower bound
or fixed-noise arbitrary-long-history guarantee follows.

## 5. Fair finite-score specialization, including original D3

Specialization is applied equally to all architectures and preserves
their actual finite outputs. Let L2,L3 be the admitted stored p-grid log
numerators. D3's possible full score numerators are

    0,L2,2L2,L3,L2+L3.                                (14)

Generate the integer C1 recurrence result separately at all five scores.
Store the five O(p)-bit weights and select the appropriate one using paid
exact score comparisons or matching-bit muxes. Include Q/K projection and
score/match operations under the same chosen implementation convention.
The four nonzero generations cost O(p^3) bit operations, in addition to
the admitted O(p^3 log^2(p+1)) log-constant generation. The cache's words,
selectors, control and code are charged; the primitive reads no history
outside its declared Q/K/V inputs. Uniform B-C uses only R; B-J uses R,E
with (6). All caches are theta-independent and generated by the same
integer algorithm, not arbitrary learned count tables.

Crucially the finite recurrence value at L2+L3 need not equal the product
of the separately rounded values divided by R. The bounded diagnostic
at valid K=2,N=5,h=10,p=120 gives an integer difference 67 from the
downward product of the separate cached weights. This diagnostic is not
a statistical experiment or a premise for consistency. It prevents an
invalid implementation simplification. The proof and programs always
cache the full scores; their difference/readout error remains governed
by the admitted C1 bound, not by a false exact finite product identity.

Per-edge exp recurrence work is thus removed for D3 as well as B-J.
With generic fixed-word dot/aggregate operations, cached attention costs
O(n^2 Kp^2) for D3, O(n^2(K^2+K)p^2) for B-J, and
O(n^2(K^3+K)p^2) for B-C. These include streamed positive integer
denominators/numerators and all final h-grid divisions; no numerical n^2
weight array is retained. A noncached convention instead retains the
additional O(n^2p^3) term where applicable. No advantage is inferred by
charging exponentiation repeatedly to one architecture but not another.

## 6. Repaired fixed schedules and complete resource functions

The numerical programs and the layer schedules are distinct objects. Fix these
identities throughout this proof:

|Use|Actual program and schedule|
|---|---|
|Original Pi and D3-snap|Frozen ../fixed_circuits.py: original(), including its parallel header extraction and serial arithmetic|
|General-K B-C/B-J in §§6,8|repair-r1/general_parallel.py: bc()/bj(), which import the frozen arithmetic, annotate parallel_front(), and use the new last-use policy|
|Binary componentwise theorem in §7 only|Frozen ../fixed_circuits.py: bc(), named bc_serial by the repair module; unchanged serial selection and retained nine scalar masters|

Paths are relative to comparison-v2/repair-r1 except the explicit repair-r1
prefix, which is relative to comparison-v2. The imports resolve to the pinned
current-project files, not an older compiler. The old v2 proof, program,
request, wrong return and the preliminary r1 checkpoint files are frozen.
The old general-K ledger was FALSE for its supplied serial schedule. Native
failure 847a1b69725044466c15af52f8db672519415d41471d284f058cf5f9b2bee745
is preserved, not reclassified as a service error. The repair below changes
actual birth layers and the table retention policy, rather than rewording that
same schedule. The §7 serial instance remains separate.

The old invalid claim has a precise legal counterfamily: N=3,M=1,h=8,
Q=256 and K increasing. Then p=Theta(log K). The frozen BC/BJ serial
fronts have respectively K^3/K^2 successively born selection gates and
tables born at 0. Summing their last-use layers gives Omega(K^6)/
Omega(K^4) holds and Omega(K^3)/Omega(K^2) depth. Thus the old uniform
O(Kp^2) depth and O(F+K^2p^3) holds cannot describe those serial fronts.
This counterfamily is not erased by the new parallel implementation.

### 6.1 Exact wide phases, births and releases

At the post-aggregation cut, layer 0 contains the entire paid table of
h-grid master scalars, exact A/B query bits and the declared common metadata.
This is the representation before selection; no table is supplied for free.
Let F_C=K^3 and F_J=K^2. In general B-C its table has F_C+1 scalar
coordinates, including the flag. In B-J the uniform bank has F_J+K+1
coordinates and the match bank K. Historical feature generation, Q/K/V,
head evaluation and these materialized outputs are all charged below.

The new readout schedule is explicitly:

|Layer|General B-C|General B-J|
|---|---|---|
|1|K^2 independent P_ij=ReLU(A_i+B_j-1)|same K^2 P_ij|
|2|K^3 independent Z_ijc=ReLU(H_ijc+P_ij-1)|K^2 independent Z_ij=ReLU(U_ij+P_ij-1)|
|3|K independent S_c=sum_ij Z_ijc|one S_s=sum_ij Z_ij|
|4 onward|old serial grid extraction, K snaps and simplex arithmetic on S|old serial extraction/snaps of S_s and K marginals, D, signed correction, simplex|

All queries are exact one-hot pairs, so at most one selected term is nonzero
in each sum. Thus the sums are in G_h and the numerical function is unchanged,
even on arbitrary admissible grid tables after perturbation. Every layer-2
parent is born at 0 or 1, and every layer-3 parent at 2. All later arithmetic
parents precede their consumer layers. parallel_front() annotates these exact
nodes in the frozen emission order and checks their arities/biases; measure()
starts remaining serial arithmetic at layer 4. It never serializes the wide
layer-2 gates. The new schedule is implemented, not an appeal to possible
parallelism.

Every used table entry has last consumer layer 2. Query pair bits also have
last consumer layer 2; selected gates have last consumer layer 3. General
B-C releases ALL original table inputs after selection, including at K=2;
the unused flag can die at the cut. General B-J releases the F_J pair table
there, while its K marginal masters and K match masters may remain through
the readout. After layer 3 all surviving scalar/bit arithmetic has O(Kp)
channels. The full table is visible and paid before this release. The binary
bc_serial of §7 instead retains its nine scalar masters and has the old
serial layer counts. These are different live representations, despite
identical nominal output words. No D3 C3 lower bound is transported between
them by output equality.

For a table entry born at 0 and last consumed at 2, precisely one intervening
identity is required. The entire wide selection contributes O(F_C) or
O(F_J) such holds, not the serial O(F_C^2) or O(F_J^2) exposure. Parallelism
can INCREASE peak width: input/output banks that serial evaluation released
at different times can now overlap. It is the new interval profile, not the
old peak, that is used below. The deterministic K=4,M=1,h=8 B-C fixture
has 154 core live channels in the new schedule versus 134 in the old serial
schedule, before adding common metadata. Neither is a minimum-width claim.

### 6.2 Integer gates and actual computable profiles

Use the admitted Boolean/ReLU basis, closed-grid h+1 extraction, ripple
addition/borrow, full-range shifted school multiplication, comparison/mux
and positive restoring division. Signed integers retain their full words;
clipping tests the sign then uses unsigned comparison. Every intervening
identity is paid. Loop lengths depend only on K,N,h and are unrolled.
The exact school primitives used in the frozen emitter have 10w nodes for
addition, 13w for subtraction, 5 per bit for mux, and

    d(w)=18w^2+19w                                      (17)

for restoring division. Variable multiplication has (21w^2+w)/2 nodes;
constant multiplication has 10w times the constant's popcount. One scalar's
grid extraction has 4h+5 nodes. A fixed integer right shift is routing.
No floor, count or exact-exp oracle appears.

The unchanged original() emits C1's actual D_k=floor(2Q(Q+lambda V)/(2Q-U)),
floor(AB/Q) products, signed boundary/difference, clipping, rho floor/max,
smoothing and the original simplex output. It retains all 9K+1 raw masters
and their h+1-bit descendants. Header expansions are parallel, subsequent
arithmetic serial as in C1. Its word is fixed from original ranges BEFORE
any baseline is built:

    w_D=2h+k+3.                                        (15)

It covers 6Q^2 normalizer/product numerators, signed [-16Q,16Q], 2KQ sums
and 2Q^2 simplex dividends. No diagnostic, idle layer or larger word is added
to original Pi to fit a comparator. New B-C words are w_C=h+m+k+8; B-J
uses w_J=p+h+m+k+16 from (10). Their bad-event divisor is at most KM+K.
Use b=128p bits for stored coefficients and online scalar/word allowances,
as in the admitted finite implementation. It covers these full products,
finite attention accumulators, addresses and dyadic thresholds. Scalar
parameter generation, known length and all program storage remain charged.

For an emitted circuit P let a_v be its assigned birth layer and z_v its
last consumer, with retained banks/bit outputs last used in the reserved final
decode layer L=1+max_v a_v. Define

    G=number of emitted nodes, T=sum_v arity(v),
    I_core=sum_v max(0,z_v-a_v-1),
    c_l=#{v:a_v<=l<=z_v}, l=0,...,L.                    (16)

This is the actual overlap profile for the chosen schedule. All parent
inequalities are checked. Inputs/constants are born at 0; materialized wide
tables are not delayed inputs. The reserved layer L explicitly decodes
h+1 output bits to each of K dyadic scalars. It adds K affine/ReLU nodes
and K(h+1) decoding terms; its intermediate bit outputs are already retained.
No change to any earlier rounding is made.

Use C0=8K+2ell_N+4 for the fixed common token/copy/initial-flag, external
query, A/B, t/N and mode/history/query/z fields. Boolean constant rails are
in the circuit. General BC/BJ already have 2K A/B input nodes, so put
C=C0-2K. The actual chosen layer-shaped allocation is

    u_l=c_l+C+K 1{l=L},
    I=I_core+C(L-1),
    lambda_addr=ceil(log2(G+I+n+F+2)).                  (16r)

Here F=F_C or F_J. Inclusive intervals may reserve a zero padding slot at a
consumer layer; only STRICT intervening identities count in I. Thus this
is a realizable charged dense layout and the sparse identity count is not
mistaken for all dense zero slots. Two rolling arrays are allocated at the
maximum width; all zeros/biases in each actual layer matrix are stored and
executed. resource_profile() computes u_l, I, the consecutive products and
the following parameter/work functions from the repaired program itself.

For input width a, output width o and a list H={(d_i,v_i)}, the complete
zero-inclusive Q/K/V/output coefficient and bias packet is

    P_att(a,o;H)=a sum_i(2d_i+v_i)+o sum_i v_i
                    +sum_i(2d_i+v_i)+o.               (16a)

In a fixed-width format P_att(W)=P_att(W,W;H), recovering exactly the
square packet used by §7. For that separately fixed binary layout, its
original formula is unchanged:

    P_dense_serial=WK+(r+L_P)(W^2+W)
                         +P_local(W)+P_stat(W).       (16b)

For the general repaired baselines instead choose these explicit pre-cut
widths, paying even the zero slots:

    V_pre=C0+F_C+3 for BC; r=2,
    V_pre=C0+2F_J+2K+3 for BJ; r=3.

The BJ width holds separate history/query pair banks, K next-symbol fields,
uniform/flag fields and the common fields. The BC width holds its explicit
triple feature bank and common fields. The r phases form the features and
mode-selected query, with the extra BJ query-pair phase. Local and global
output projections release front-end slots at the stated cut. Put
H_local={(1,K),(1,K)}, H_C={(1,F_C+1)}, and
H_J={(F_J-1,K),(1,F_J+K+1)}. The actual general layer-shaped packet is

    P_dense=K V_pre+r(V_pre^2+V_pre)
          +P_att(V_pre,V_pre;H_local)
          +P_att(V_pre,u_0;H_C or H_J)
          +sum_{l=1}^L u_l(u_{l-1}+1).                (16c)

This counts embedding, every bias, both local heads, actual statistical
heads and each readout matrix, including the final decode. With embedding
counted as a layer, full depth is 1+r+2+L. W=max(V_pre,max_l u_l) is the
full width of this allocation. Matrix bits are exactly b P_dense. Additionally
store V_pre local residual routes and C0 exact common-field routes through
global output, each with a coefficient and two source/destination addresses;
their bits are (b+2 lambda_addr)(V_pre+C0). This counts the residuals rather
than treating them as additional free projections. No old statistical master
is in that residual route. The binary fixed-width instance uses the same
local residual width and common-field routes for both architectures, so its
componentwise comparison is unchanged. Add the mask/position/cache/program
fields below for full stored bits. Fixed-width padding instead
uses W in all actual layer products; it is a DIFFERENT stored format with
its larger counted costs, not mixed into the layer-shaped table.

The sparse readout format is also explicit. It stores a bias/record for
each emitted node, a coefficient/source for each term, one coefficient/
addressed identity per hold, and the final K dyadic output rows. A valid
fixed-field cost for that chosen record format is

    B_sparse_readout=b[T+G+I+K(h+2)]
       +lambda_addr[2G+T+3I+K(h+3)].                   (16s)

Headers identify input/constant/gate records. Count the actual nonzero
input/projection/front-end records additionally: BC O(F_C+K^2+K),
BJ O(F_J+K), D3 O(K^2+K), with their coefficient/address bits. These
are the explicitly given feature gates, sparse identity/basis Q/K maps,
mode muxes, value/output routes and row-shift controls, NOT a free table.
Nonzero addresses and constant parameters are generated by those fixed loops.
The dense format counts zero entries too; no sparse saving is used in §7's
dense comparison.

### 6.3 Why the repaired uniform bounds follow

The first three post-cut layers have O(F+K) nodes/channels and O(F+K^2)
terms, with O(F+K^2) strict holds. They occupy only a constant number of
wide matrices. Their table-input lifetimes end at layer 2 and selected
gates at 3, including in the general K=2 schedule. Starting at layer 4,
only O(K) masters, O(Kp) bits/registers and O(p)-bit scratch remain.
There are O(Kp^2) serial arithmetic nodes/layers, so the narrow-phase hold
bound is O(K^2p^3). The BJ constant multiplications by E-R and QR have
O(p) bits and hence O(p^2) gates each, included in this bound. Therefore

    L=O(Kp^2), W=O(F+Kp),
    G,T=O(F+K^2+Kp^2), I=O(F+K^2p^3).

For BJ the K^2 term is already F_J; for BC it is bounded by F_C. These
are proved for the REPAIRED general schedule, not the frozen serial bc/bj.
The constant number of wide matrices contributes O(F^2); all narrow
matrices contribute O(Kp^2 (Kp)^2)=O(K^3p^4). Adjacent wide/narrow
transitions obey ab<=(a^2+b^2)/2, so add no missing term. Thus (16c)
is O(F^2+K^3p^4), coefficient bits O(F^2p+K^3p^5). Since
log(G+I+n+F)=O(p), sparse coefficient/address bits are O(Fp+K^2p^4).
The initial r feature/mode layers and projection packets satisfy the same
bounds by their stated widths/dimensions. No old peak-width number was
substituted in this argument.

The full updated layer-shaped table is:

|Resource|original Pi / D3-snap (frozen serial arithmetic)|general BC parallel-r1|general BJ parallel-r1|
|---|---|---|---|
|Total/max-layer heads|6 / 4|3 / 2|4 / 2|
|Maximum Q/K dimension|2K|1|K^2-1|
|Statistical value coordinates|9K+1|K^3+1|K^2+2K+1|
|Score range|<=2|0|2, paid row shift|
|Neural depth|O(Kp^2)|O(Kp^2)|O(Kp^2)|
|Maximum width|O(Kp)|O(F_C+Kp)|O(F_J+Kp)|
|Dense coefficient slots|O(K^3p^4)|O(F_C^2+K^3p^4)|O(F_J^2+K^3p^4)|
|Dense parameter bits|O(K^3p^5)|O(F_C^2p+K^3p^5)|O(F_J^2p+K^3p^5)|
|Sparse nodes/terms before holds|O(K^2+Kp^2)|O(F_C+K^2+Kp^2)|O(F_J+Kp^2)|
|Identity holds|O(K^2p^3)|O(F_C+K^2p^3)|O(F_J+K^2p^3)|
|Sparse parameter/address bits|O(K^2p^4)|O(F_Cp+K^2p^4)|O(F_Jp+K^2p^4)|
|Rolling/attention working bits, excluding stored data|O(nKp^2)|O(n(F_C+Kp)p)|O(n(F_J+Kp)p)|
|Cached attention bit operations|O(n^2Kp^2)|O(n^2(F_C+K)p^2)|O(n^2(F_J+K)p^2)|
|Layer-shaped dense projection/pointwise bit operations|O(nK^3p^6)|O(n(F_C^2p^2+K^3p^6))|O(n(F_J^2p^2+K^3p^6))|

Original Pi and D3-snap use the previously declared frozen original
arithmetic, which has no wide K^3/K^2 table. These O bounds do not change
the separate original-Pi binary resource vector in §7. For general BC/BJ,
the exact resources are (16r),(16a),(16c),(16s), not only this table.

### 6.4 Full work, operation and generation ledgers

All computation convention choices are explicit. Keep two rolling neural
arrays of nW b-bit slots. For an attention stage store projected token
arrays with C_H=sum_i(2d_i+v_i) columns; local-stage storage is recycled
before global attention. A single row/head is accumulated at a time.
Let C_proj=max(C_local,C_stat), v_max=max_i v_i over these stages.
One valid actually allocated work function for general BC/BJ is

    B_work=b[2nW+n C_proj+2(v_max+1)+64].               (16w)

The two row buffers cover old/new accumulators and their exact positive
denominator. The 64 words cover the fixed finite integer multiply/divide,
cache lookup/row shift and sign/rounding scratch. Full products fit the
admitted b allowance. This includes the finite evaluator's real workspace;
its denominators/numerators and projected arrays are zeroed before the
declared summary cut and do not become decoder ports. Work clearing costs
are charged below. Add input data and mask/position storage to online work
when these are kept in RAM; add stored parameters/programs for total peak
memory. Peak width is recomputed from repaired u_l; the K=4 increase is
included. We do not infer memory dominance from a faster schedule.

Let mu(b) be the instruction count of the SAME fixed school b-bit
multiply/add template on every coefficient/bias slot, generated by the
addition/multiplication/rounding loops above. It is an explicit computable
O(b^2) function independent of coefficient values; no zero-skipping is
given only to one architecture. Dense projection/pointwise execution costs
n P_dense mu(b), plus the fixed sign/ReLU/rounding work per row and
n(V_pre+C0)b bit-copy operations for the paid residual routes. The
statistical allowed-edge count remains e_M=2+M(M+1)/2+M. For an explicit
attention operation function, iterate those e_M edges for every head,
compute the d_i dot products or the fixed feature-selected score, perform
the paid full-score cache selection (and BJ row shift), and update its
v_i numerators plus denominator with school integer operations. Finally
perform n sum_i v_i fixed-word divisions to return G_h coordinates.
Add the two local singleton-mask heads, their final divisions, and clearing
n C_proj+2(v_max+1)+64 words before the cut. All loop bounds and word
operations are fixed by K,N,h. This defines an actual computable count,
bounded by the table's cached attention row; it never repeatedly evaluates
exp on an edge only for D3. Full-score caches are exactly §5, so the finite
value at L2+L3 is generated independently, without false factorization.

Masks/positions cost O(n^2+n log(n+1)) actual Boolean/integer bits in
each format, with shared identical masks stored once and no numerical
-infinity word. Add known K,N,M,h,p layouts, the actual finite cache words,
score controls and integer microcode. A shared O(p^4)-bit evaluator-code
allowance is valid for these fixed school loops; alternatively enumerate
and charge its exact unrolled records as part of the sparse program.
It is never a free real arithmetic primitive. Mask generation/writing
costs its actual stored bit count. D3's offline log generation costs
O(p^3 log^2(p+1)) and its four nonzero full-score cache evaluations O(p^3).
BJ additionally generates E by (6) in O(p^3); BC only requires R and known
length. Their generation scratch is the declared O(p)-word school scratch
(with the C1 log-generation bound where used), not a free parameter oracle.

Program generation builds the node/term lists, repaired birth/last-use events,
sorted live intervals and routing addresses. Sorting O(G+T+I) O(p)-bit
records and writing their fields takes O((G+T+I)p^2) bit operations and
O((G+T+I)p) work bits; writing a dense file additionally costs its b P_dense
bits. The same counts plus actual mask/cache generation are the offline
cost functions. Writing a fixed-width layout instead requires its own
larger b times actual slot count. For general width W this padded alternative
has O(Kp^3(F+Kp)^2) dense stored bits and O(nKp^4(F+Kp)^2) bit operations.
Layer-shaped and fixed-width budgets are never interchanged in the comparison.

The finite-attention plus pointwise-network convention is C1's. Fully
flattening attention into ReLU layers adds its explicitly iterated integer
operations as serial depth and the corresponding depth-times-live-width
identities and matrices. None of the smaller displayed hybrid costs is
claimed for that separate flattened convention.

Bounded repair diagnostics use only K=2,3,4 wide-front structures and three
admissible grid-table inputs. They check all parent birth inequalities,
table last use, three-layer depth, changed peak/holds and equal output words;
they run no trajectory enumeration or stochastic experiment. For example
BC K=4,M=1,h=8 has repaired readout depth 26,752, 154 core live channels,
and 2,677,705 core holds versus serial 26,833,134,2,683,225 (without
common metadata). The independently reserved full general layout has
W=190 after common fields; these are not §7's binary numbers. Algebraic
lifetime/width bounds above establish all K; the fixtures only diagnose
the specific erroneous scheduling assumption.


## 7. A binary comparison inside the original allocation

This section EXCLUSIVELY uses frozen comparison-v2/fixed_circuits.py:
original(...,snapped=False) and bc(...), the latter exported as bc_serial
by repair-r1/general_parallel.py. It does not use the repaired general
parallel bc/bj or their different last-use policy/profile. All exact binary
counts below remain those pinned in check-results-v2.json; no new general
peak or layer-shaped matrix count is substituted.


This section supplies a componentwise feasible allocation, rather than
forming a large common cap. Fix K=2 and Q>=256M. Use the original C1
serial lowering from §6, with w_D=2h+5, all 19 masters and their full
closed-grid descendants retained as in the admitted complete-code schedule.
Determine its actual L_D,W_D,I_D from original() ALONE. Use its fixed-width
dense layout, its b-bit words, its actual projection arrays, masks, cache
and rolling buffers as the budget. This is a specific implementation of
original Pi. It has not been padded or lengthened after seeing a baseline.
The claim is not about every possible lowering or minimal budget for Pi.

For B-C retain its entire nine-coordinate uniform bank through output,
plus the same actual endpoints/query/metadata. Its fixed serial count/output
word is w=h+m+10. With s_2(M) the binary popcount of M, its core count/
simplex DAG has exactly

    G_R=18w^2+(92+20s_2(M))w+8h+14.                    (18)

Replacing its two selected inputs by the real nine head masters and four
query bits adds eleven input nodes; forming four pair bits, eight selected
values and two sums adds fourteen gates. Hence the emitted B-C readout
has G_R+25 nodes. This includes actual selection, not a query-dependent
historical value. Its serial depth is at most G_R+25; the exact function
(16) is smaller because input/constant nodes have layer zero.

Since h>=8 and m<=h-7, w<=2h+3 and s_2(M)<=m. Therefore

    L_C <=112h^2+188h+57,
    2d(w_D)=144h^2+796h+1090 > L_C.                    (19)

Original Pi's two normalizer divisions ALONE are sequential and cost
2d(w_D) layers in this fixed lowering. Its other actual arithmetic,
selection, extraction and output make L_D larger. Thus B-C's whole new
readout fits the original readout layer budget; no added D3 layers are used.

For liveness the B-C readout uses at most 7w+25 channels apart from the
common query/endpoint/fixed-metadata bank. Here is a conservative explicit
register count: two count words and up to two divisor/dividend words,
one quotient word, and two old/new remainder/difference words give 7w;
the nine retained scalar masters and at most 16 carry/mux/extraction
temporaries give the extra 25. Ripple multiplication/addition uses fewer;
old partial products are released before the next word iteration. Query
bits/actual endpoints and fixed metadata are identical common banks.
In contrast the original 19(h+1) master bits remain live throughout both
normalizers and the rest of the original decoder. Thus

    7w+25 <=14h+46 <19(h+1), h>=8.                     (20)

Original scalar masters, also retained in original(), only increase its
real capacity; no unused scalar allowance is needed to prove (20).
Here is an explicit register placement, including common banks rather
than discarding their costs. Fix the C1 shared field layout first: current
token, two lag copies, initial flag vector, external query, chosen A/B,
binary t/N metadata, and mode/history/query/z bits. The fixed field bank
C0=8K+2ell_N+4 channels covers those named fields; it is fixed from C1's
inputs independently of a baseline. Boolean constant rails are already
included in the gate program, not an extra uncounted bank. Use the first C0 slots for the fields,
the next 19 for raw statistical masters at K=2, and the next 19(h+1)
for their closed-grid expansions. Actual temporary live intervals are
assigned the first free remaining slot. This is possible using the peak
overlap in (16); no data-dependent addressing or parameter oracle is
required. Actual endpoints use the same lag-copy slots throughout.
For B-C the eight historical triple features use slots C0,...,C0+7
before aggregation; afterward its nine masters use C0,...,C0+8. Pair
query bits and all count/division/output scratch use the now-free bit
bank and old scratch space. Bound (20) guarantees that bank suffices.
Replacing the flag feature bank does not lose the scalar z flag, and
at the synthetic query all historical-feature slots are zero as before.
The C1 local-copy/mode stages are unchanged. At their existing first
pointwise layer replace the two initial-flag feature gates by eight triple
feature gates in vacant channels; keep shared mode/binding registers.
At most 48 non-common scalar slots cover x,l1,l2,features and mode
temporaries here, below 19(h+1) for h>=8. No extra pre-global layer is
needed. Pair query bits are formed after aggregation and already included
in the fourteen readout gates. This explicitly allocates the feature bank.

For the global projection/storage allocation, map the nine uniform outputs
to nine of the original nineteen output slots. Its eight triple entries
can occupy the old q1/v1/q2/v2 slots and its flag the old rho slot. Its
value projection needs nine columns instead of the original total nineteen;
the input features occupy previously vacant residual channels at the same
fixed W_D. It uses one Q/K coordinate from the old uniform head and no
nonzero score coefficients, rather than original dimensions 4,4,2,1.
The old concatenated Q/K/V/output parameter arrays have enough columns;
repartitioning freed head columns into one uniform value block is allowed
resource reallocation, not extra storage or a new data port. The same two
local heads and their endpoint slots remain. Statistical heads fall from
four to one, total modules from six to three; no claim of minimum heads
among all networks is made.

All new pointwise coefficients have magnitude <=Q (Boolean coefficients
or extraction thresholds) and dyadic fractional word length <=h. M appears
as fixed bits for multiply-by-2M; it is not a large real multiplier weight.
They fit the original b-bit parameter format. Also w<w_D, so new scratch
word lengths fit existing arithmetic allowances. With the same W_D and
fewer actual layers, ordinary dense parameter slots/bits and generic
pointwise multiply/add executions do not increase. Zeros are charged in
both layouts. This pads a baseline to an existing width when needed; it
does not pad D3 to create a budget. One run still evaluates only one query.

Hold wires are also paid. Apart from the common bank, a safe bound is
(7w+25)L_C for the new readout plus at most 128 extra front-end feature
holds. The original master-bit holds alone are at least
19(h+1)(2d(w_D)-1). Substituting (19)--(20), the difference is bounded
below by the difference of these polynomials:

    19(h+1)(144h^2+796h+1089)
      -(14h+46)(112h^2+188h+57)-128 >0.                 (21)

Every coefficient of the expanded difference is positive. Common-bank
holds are smaller because L_C<L_D. Thus wire/liveness costs do not hide
the allocation. The exact diagnostic counts at M=1,h=8 are 69,548
original readout layers/357 live channels versus 8,715/98 for B-C (the
latter includes the extra four retained endpoint controls); at M=7,h=11
they are 111,773/456 versus 14,129/118. These are checks of the fixed
algorithms, not proofs by enumeration; inequalities (19)--(21) prove the
general claim.
The additional shared metadata reservation C0 is added identically to
these core live counts (subtracting controls already included); it is
not omitted from full rolling/parameter accounting.

The remaining budget components are explicit as well. Local-copy/mode
positions and masks are the same; the single statistical mask is an old
uniform-mask instance, so no additional stored mask is needed. All nine
uniform accumulators and output divisions fit within the original nineteen
value-coordinate updates/divisions, and its one positive denominator fits
within the original four. With fair full-score caches, uniform weight R
needs no more selectors/score/word work than original uniform coordinates
plus freed product-head coordinates. Streamed row/query buffers are no
larger than the old four-head workspace, and rolling dense arrays use the
same W_D and b with fewer layers. To check serial-head memory explicitly,
the original statistical Q/K/V token arrays have
2(4+4+2+1)+19=41 columns, the new head has 2+9=11. Even if the old heads
are streamed one at a time (maximum old value width seven), the baseline's
two additional row accumulator words are more than offset by 30n fewer
projected token words, since n>=4. They can also occupy unused future
bit-expansion slots during attention. These buffers are cleared before
the cut, so they do not supply free counts to a readout. Thus the complete
projected-array/accumulator peak, not just summed value dimensions,
respects the old allocation. In (16a), the old global packet is
60W_D+41+W_D and the new one is 20W_D+11+W_D; local packets are unchanged.
Combine these exact counts with r=2, (19)--(20) and (16b) for the full
zero-inclusive parameter/operation comparison.
B-C requires no log generation or nonzero
score cache; its constant M and code are inside the counted gates/metadata.
Writing its smaller dense layer/projection format and generating its
addressed arithmetic uses no more than the original chosen template's
corresponding budgets. Thus total stored bits, online peak bits, cache/
generation allowances and forward bit operations fit the original fixed
dense implementation. This comparison is not asserted for an unreported
compressed sparse format; §6 supplies its separate computable ledger.

The substantive conclusion is therefore: within this exact binary original-
Pi allocation, a legal B-C-snap reaches g_snap and the count-simplex target
with fewer statistical modules, while original Pi keeps its g_0 bound.
This proves an achievable baseline at that same complete budget. A smaller
upper bound is NOT pointwise risk dominance, nor an optimal-resource theorem.
This comparison fixes the common error experiment at nominal evaluation
(delta=0). The separate small-grid-error comparisons in the predecessors
and (13) use the explicitly stated port radii. A P2-only fault is defined
on original D3's code; it is not silently declared the same hardware fault
on an architecture without a P2 port.
Neither D3-snap nor B-J is claimed to embed componentwise without separately
testing its emitted resource vector; their extra readout words/layers are
not erased by interface feasibility.

## 8. Full-K tradeoffs, risks, and precise comparison limits

For the general BC/BJ resource comparisons in this section, the program is
parallel-r1 of §6.1 and the full actual resource vector is (16r),(16a),
(16c),(16s),(16w), with paid residual routes, masks, cache and generation.
Its O(Kp^2) depth and O(F+K^2p^3) holds follow from the implemented births,
not the rejected serial front. Its peak may increase. Binary §7 instead uses
(16b) and its frozen serial instance, with an independent cap allocation.
The general schedule releases the table after selection; the binary serial
instance retains it. Equality of outputs does not equate their visible
representations or transport the original D3 attack to these architectures.

For K>=3, K^2-1>2K. Hence the specified exact single joint kernel cannot
fit D3's Q/K cap 2K in the bare representation of §2. Paid row shifts do
not remove that rank restriction. Nonlinear score circuits, other kernels
or many heads are outside it unless separately charged/analyzed. B-C has
Q/K dimension 1 but its chosen materialized feature/value bank has K^3+1
coordinates. The actual h-grid output array in that format occupies
(K^3+1)(h+1) bits before word padding, versus (9K+1)(h+1) for D3. For
K>=4 this specified table is larger. This is a cost of the actual explicit
array, not a minimum-memory lower bound on all counting schemes. Full
width/parameters/operations are in §6; dimensions alone do not settle
componentwise feasibility. A same-budget baseline may reallocate vacant
channels, use another nonlinear counting construction or improve its
program; those alternatives are not banned to manufacture an advantage.

Sharper itemwise matching is legal too: Q=(A,B), K=(l2,l1) uses the same
2K dimension with exact logits 0,1,2 and a paid finite cache for those
three scores. Thus D3's chosen log-2/log-3 scores are not declared optimal
within the score cap. Reusing its old recovery coefficients after changing
scores would require a new derivation and new finite error/cost ledger;
no failure of that unanalysed readout is claimed. The actual sharper joint
baseline in §4 and the binary budget counterconstruction already prevent
a D3 advantage/minimality conclusion. Full-K results here remain the
explicit representation/table tradeoff, not a theorem excluding sharper
or nonlinear predictors.

Binary B-J has dimension 3<=4 and nine statistical values<=19, hence real
alphabetic feasibility. Its full signed w_J correction, F features and
row-shift/cache code remain paid. We do not infer full binary embedding
from these two inequalities. B-C's §7 allocation supplies an actually
checked same-component conclusion, while B-J supplies a sharper finite
joint-matching alternative and the explicit general-K representation tradeoff.

For risk composition use finiteN Fact f9a79122946f24c5 without reproof.
On its SINGLE event V_alpha, let

    A_alpha=K log 2+log(2K^2 M/alpha),
    S(j)=sqrt(A_alpha/(2j))+(K-1)/(j+K), j>=1,
    g_snap(j)=min(1,S(j)+(K-1)/Q), g_snap(0)=1,
    g_delta(j)=min(1,S(j)+KM(78/Q+36delta)/(j+K)+(K-1)/Q),
    g_delta(0)=1.                                    (22)

The event has probability at least 1-alpha simultaneously for all observed
context counts. By (12), B-J now inherits g_snap as well as the two admitted
snapped variants. Original Pi uses g_delta, nominal delta=0. The snapped
zero-count output is the shared dyadic uniform approximation; original Pi
need not have exactly that finite output. On zero count only the stated
risk bound one is used, not division by zero or free rare-context knowledge.

Every admitted fixed/max-context, actual-terminal, conditional-terminal
and history-weighted transfer applies to the new B-J through equality.
For example expected terminal error is <=E g_snap(n_(E_N))+alpha, and
conditional-terminal error has the bad-event term alpha/pi_s, not alpha
without justification. Declared occupancy/min-transition or mixing bounds
may be substituted exactly as in that Fact. No new independence is assumed.
The actual h,p from (1) are substituted into §6's resource functions; a
sufficient common implementation-error choice is
Q>=max(256M,(K-1)/epsilon), with the next power of two and h>=4.
The thresholds 2M,4M,256M are sufficient schedules, not necessary precision
separations. Count recovery removes an implementation M/Q penalty for
these variants; it does not remove statistical uncertainty about theta.
The accepted C1 theta-independent schedule
h_N=ceil(log2(128(K+1)(N+1)^3)) already satisfies Q>=256M. Consequently
the three snapped variants also inherit max-context almost-sure convergence
for every fixed strictly positive D1 law from their common add-one target
and vanishing (K-1)/Q, using the admitted empirical-count consistency.
This introduces no theta-dependent tuning and no new lower bound.

## 9. Exact primary comparison and handoff limits

The primary HTML snapshots in outputs/003-comparison/counter/sources were
read directly at the fixed IDs below, after verifying their original hashes.
They are primary literature evidence about predecessors, not extra Euler Facts
or substitutes for the three admitted prerequisites. No broad screening was
performed. The comparison is at information, architecture, resources and risk:

* [D'Angelo et al., 2607.02800v1](https://arxiv.org/html/2607.02800v1#S3.Thmproposition1),
  Proposition 3.1, Lemma 4.1 and Appendix D.2 (IDs S3.Thmproposition1,
  S4.Thmlemma1,A4.SS2): itemwise lag matching and exact-mask/cumulative
  counts are already explicit. D.2 inverts subset counts by alternating
  inclusion-exclusion and obtains the polynomial in exp(beta)-1. Their
  two-layer disentangled construction uses k local copy heads and one
  matcher, with optional BOS pseudocounts. Thus neither product expansion
  nor subtracting shared lower-order terms is new. It does not supply
  this fixed finite evaluator's count snapping, full gate budget, or the
  stated correlated finite-N port-risk experiment. Their ideal hard
  positional copying and soft interpolation cannot be imported as D5's
  finite implementation or as an optimal probability-risk theorem.
* [Ye et al., 2410.05258v1](https://arxiv.org/html/2410.05258v1#S2.SS1),
  §2.1, equation (1)/Figure 2: subtracting two normalized softmax maps
  with a scalar and head normalization is a direct predecessor to common
  attention-background cancellation. D3 instead recovers two path-dependent
  normalizers, subtracts the unnormalized numerators and corrects initial/
  terminal flows. The paper's empirical cancellation results do not prove
  this exact transition-count identity or its stochastic finite-grid risk.
  Its architecture/normalization and resource accounting are different;
  no performance superiority is inferred from the analogy.
* [Zhou et al., 2410.05493v3](https://arxiv.org/html/2410.05493v3#A7.SS2.SSS2),
  Theorem 4 and G.2.2 equations (32)--(38): forward/backward normalized
  context statistics and positions reconstruct counts by a product of
  ratios ending in total length. The construction explicitly addresses
  count recovery; equation (36) takes the matching coefficient to infinity.
  Its variable-order CTW/Bayesian task and sufficiently wide feedforward
  functions are not this fixed-score finite-bit resource/risk theorem.
  Length and backward statistics are real information channels, so a
  normalized-coordinate argument cannot ignore them. Known M in the
  present new readouts is similarly declared and paid.
* [Rajaraman et al., 2407.17686v1](https://arxiv.org/html/2407.17686v1#S5.Thmtheorem1),
  Theorem 5.1 and Remark 5.2: a three-layer one-head nonlinear-normalized
  construction represents fixed-order conditional k-grams in O(S)
  embedding dimension. The remark discusses precision but says its stated
  proof does not bound the finite-precision error. Thus a low alphabetic
  interface or conditional-frequency expressivity is already prior work;
  their representation restrictions are not finite-history stochastic risk
  lower bounds under the complete D3 code.
* [Ekbote et al., 2508.07208v2](https://arxiv.org/html/2508.07208v2#S4),
  §4 Theorem 3/Remark 2 and Appendix B: two single-head layers with
  relative positions, MLP and directional normalization represent arbitrary
  fixed-order conditional k-grams in 6S+3 dimensions; the source also
  discusses parameter/precision sufficient bounds. Strong shallow nonlinear
  counting must therefore be allowed as a comparator. Its architecture,
  score/normalization assumptions and separate training analysis do not
  instantiate D3's charged finite code or prove its located-noise risk.
  Our binary negative comparison is a fixed implementation result, not a
  new general claim that shallow counting is possible.

Both old failures (2311d636... and 847a1b69...) and all source/v2 drafts remain
unchanged. In the first-round repair, only general-K birth/lifetime
implementation and its resource ledger are changed; bounded structural
diagnostics in repair-r1/ check that implemented change. The earlier
rank/integer-recovery/risk/source arguments are preserved.
The old failure and source drafts remain unchanged. Its old missing C1 and
finite-N premises are now supplied at exact native scope; the new rank,
finite-joint correction, fair cache and actual binary allocation were checked
in this proof rather than admitted by discussion. Bounded diagnostics only
exercise these new circuits/cache identities, with no statistical enumeration.

Remaining limits are precise. No optimum full-K resource frontier, universal
memory/precision lower bound, or all-decoder failure theorem has been proved
or is used to close this parent. General-K joint/table tradeoffs are the
scoped negative classification, not a promised D3 advantage. The admitted
C3 theorem concerns its exact post-aggregation grid model; endpoint/query/
arithmetic-fault models are outside that theorem and are not silently claimed.
Root C4 still requires one joined fixed-version C1--C3 package with common
definitions/manifests, independent root audit and stage-to-mother handoff.
Local admission of this comparison would not perform that audit or close
the mother objective. No root closure is asserted here.
