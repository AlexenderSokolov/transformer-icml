# Exact count snapping on the declared finite grid

Fixed version v1, 2026-10-25. Project icml-flow-heads, contract
22e80d3d620c36cfc0bbd297101a5efabe634d7fd696b4cae200963af52af02a.
Exact target: 2b5ba74d6d15e652767bfd1543e6a04065654751a94cba20adbe3e6c53895d6b.
The unique native predecessor is C1 Fact **b2f4d10fa0a69e00**, Evidence
15df56a560e38b8bb7fc84382d374a1e31298a0463efdbde0ab5e20f044291f3
(VALID, PASS, discharged C1 obligation 7920eabc...). Its accepted proof
has SHA256 36260d168f17b9da129179070a70c5e87019a45d98c60f1c343a9e1c5e60287b.
The native verdict for the present submission, not this document, determines
admission. No old comparison draft is used as a proved premise.

## 1. Statement, interface, and exact predecessor use

For integers K>=2, N>=3 put M=N-2, n=N+1. The observed input is
X_1,...,X_N, with a synthetic query at n, no X_{N+1}. A query is either
an external pair s=(a,b), or the actual observed endpoint E_N. Define
mathematically C_(s,c)=sum_{t=3}^N 1{(X_{t-2},X_{t-1},X_t)=(a,b,c)}.
These integers are proof objects, not uncharged input registers.

Let h>=4, Q=2^h, G_h={A/Q: A integer, 0<=A<=Q},
ell=ceil(log2(N+K+2)), and p=4h+4ell+64. For a word bound below also put

    m=ceil(log2(M+1)), k=ceil(log2(K+1)), w=h+m+k+8.          (1)

Here w=O(p). Each closed-grid coordinate uses h+1 numerator bits,
including the endpoint A=Q. Known M is obtained by an exact subtraction
from declared N during program generation and stored in m bits;
its constant/metadata and all uses
are charged. h,Q, word layouts and every loop length are fixed by K,N,h,
never by the test law. All claims below are pointwise for every path and
query. D1's stationarity/positivity are therefore permitted but unnecessary
for the new deterministic claims; no uniform stochastic rate is asserted.

We construct two additional predictors:

* **B-C-snap**, a paid K^3-feature uniform-count head and a new integer
  readout, nominally exact in counts if Q>=2M;
* **D3-snap**, the admitted D3 finite prefix through its recovered clipped
  joint frequency, followed by the new integer readout, nominally exact
  in counts if Q>=256M.

At a common h>=4 with Q>=256M the two predictors output identical bits
on every path and query. Each output has TV distance at most (K-1)/Q
from the exact empirical add-one distribution

    p^+(c|s)=(C_(s,c)+1)/(sum_d C_(s,d)+K).                (2)

This compares implementation error relative to the same empirical target,
not sampling error relative to an unknown transition law. Complete resource
functions and precise perturbation scopes are proved below. Equality of
outputs implies neither resource optimality nor componentwise dominance.

Only the following admitted C1 conclusions are used, within their domains:

1. Two charged zero-score singleton causal heads produce l2_t,l1_t from
   predecessors and the actual endpoint at the synthetic query, with paid
   flags/mode/positions/masks and exact bit selection. D3's four heads
   expose 9K+1 coordinates, maximum Q/K dimension 2K, value dimensions
   2K,2K,2K,3K+1. No later attention or historical-workspace readout exists.
2. The finite evaluator uses p fractional working bits, stored finite
   log constants, and integer arithmetic. With integer R=2^p and a finite
   score s=S/R in [0,2], it forms T_0=R,
   T_j=floor(T_{j-1}S/(jR)), j=1,...,8p, and W=sum_j T_j. It accumulates
   integer weighted numerators/denominators exactly and returns
   floor(Q A/D)/Q. These are implemented integer operations, not oracles.
   Its closed-grid outputs have ideal-head error <=2/Q. The full C1
   predictor domain is h>=max(4,ceil(log2 M)+1).
3. In that domain the D3 finite prefix computes dT,d1,d2 and all boundary
   terms with h-grid arithmetic (retaining an extra fractional bit for
   halves), then a_c=clip(c_hat,c,0,1) on G_h. For exact bit queries,
   flags and endpoint, arbitrary correlated head-coordinate error <=eta
   and product/quotient error <=zeta give

       |a_c-C_(s,c)/M| <=35eta+6zeta.                    (3)

   Nominally eta=2/Q, zeta=1/Q, so the bound is 76/Q.
4. Closed-grid scalar-to-bit extraction, Boolean/ReLU integer circuits,
   positive-divisor long division, signed rails and identity holds are
   available with the explicitly charged resource bounds recalled below.
   The C1 prefix has full word lengths O(p), width O(Kp), depth O(Kp^2),
   sparse gates O(Kp^2+K^2), holds O(K^2p^3), and the full bounds used in §7.

The formulas used in the D3 prefix remain exactly the accepted ones:

    dT=1+alpha_b, d_k=(1+lambda_k nu_b)/(1-U_k/2),
    g_c=dT h_c-nu_c +rho J_c -(dT h0_c-f_c),
    c_hat,c=(d2 q2,c)-(d1 q1,c)-g_c,

with lambda_1=1,lambda_2=2, the accepted downward h-grid products/divisions,
and true endpoint J. Their computation, all normalizer divisions, both
product heads and the boundary/initial-flag terms are paid, not supplied
as an additional frequency oracle. No change is made to the accepted
Pi_(N,h), its smoothing rule, its acceptance proof or its C3 experiment.
D3-snap is a separately specified alternative readout.

## 2. Count lemma, closed endpoints, and a legal circuit

For A in {0,...,Q} define the integer function

    R_(M,Q)(A)=floor((2MA+Q)/(2Q)).                       (4)

For C in {0,...,M}, the strict hypothesis

    |A/Q-C/M| <1/(2M)                                  (5)

implies |MA/Q-C|<1/2. Thus C<MA/Q+1/2<C+1 except that
the left strict inequality can be weakened; taking its floor gives C.
More exactly, for this particular half-up rule, R(A)=C if and only if

    (C-1/2)/M <= A/Q < (C+1/2)/M.                       (6)

We use the symmetric strict condition (5), which works uniformly without
choosing a tie direction for the true count. The radius cannot be changed
to a symmetric non-strict one: M=1, Q=16, A=8 is halfway between C=0
and C=1; (4) returns 1 and fails for C=0. At A=0 and A=Q the exact
outputs are 0 and M. For every input in the closed grid, even outside
(5), the output is an integer in [0,M].

There is no continuous floor primitive in (4). Use C1's grid extraction
on A=Q a, from index h down to 0:

    b_j=ReLU(A_j-(2^j-1))-ReLU(A_j-2^j),
    A_(j-1)=A_j-2^j b_j.

Each subtraction can be followed by ReLU since the result is nonnegative
on the declared integer domain. This extracts h+1 exact bits, including
the bit at h when a=1. Compute 2M times this integer by shifted partial
products and ripple additions, retaining the full product, add Q, and
take the high bits after discarding precisely h+1 low bits. This last
operation is routing of integer bits, not a real-valued rounding oracle.

For completeness the primitive gate basis is, on bit inputs,
AND(u,v)=ReLU(u+v-1), NOT(u)=ReLU(1-u), and
XOR(u,v)=ReLU(u-v)+ReLU(v-u). Nonnegative sums can be passed through
ReLU. OR is u+v-AND(u,v), and a mux is the OR of two disjoint selected
ANDs. Ripple sum/carry and difference/borrow use a constant number of
these gates per bit. Shift-and-add multiplication uses O(w^2) such gates
and sequential layers with O(w) scratch. Restoring division by a positive
w-bit divisor shifts a w+1-bit remainder, compares/subtracts the divisor,
and multiplexes the new remainder for each numerator bit, again O(w^2)
gates/layers and O(w) scratch. All loop lengths are unrolled. Original
inputs/outputs, carries, partial products, constants and each live bit's
identity connection through every intermediate layer are counted in §6.

The product in (4) is <(2M+1)Q<2^(h+m+2); its numerator fits h+m+2 bits.
The w of (1) is ample for it, even for M=1. The count itself needs at
most m bits. Grid extraction coefficients have at most h+2 bits including
sign. No arithmetic overflow or implicit unbounded integer register is used.
The executable circuit in circuit.py expands this construction directly
into affine/ReLU gates and includes the endpoint bit.

## 3. The paid uniform-feature comparator

Use the same two paid singleton predecessor heads. At every historical
position t>=3 construct all F=K^3 bit coordinates

    T_(ijc),t=ReLU(l2_t,i+l1_t,j+x_t,c-2).               (7)

These F gates each have three input coefficients and a bias. Store their
outputs explicitly; the feature table is not placed in the input. The
uniform head has Q=K=0, Q/K dimension 1, and V=(T,z), of dimension F+1.
Its query-row mask is the same paid historical set t=3,...,N; unused
rows use legal causal prefixes and singleton fallbacks. Every value is
query-independent. Endpoint/external query selection uses the paid bit
mode gate; no query is broadcast backwards to historical positions.

At zero score the admitted evaluator's recurrence has T_0=R and every
T_j=0 for j>=1, so W=R exactly. Thus its output coordinate is exactly

    H_(ijc)=floor(Q C_(ijc)/M)/Q,                       (8)

and the flag coordinate is floor(Q/M)/Q. Known length is already present;
the flag is included/charged but not needed for snapping. For uniform
attention the known-zero recurrence may be compiled to W=R directly:
this is precisely the same finite output, not an exact transcendental
oracle. We use this specialization and count all integer accumulation
and division operations. No negative logits occur anywhere in B-C-snap.

At q form K^2 pair bits P_ij=ReLU(A_i+B_j-1). For every i,j,c select
ReLU(H_(ijc)+P_ij-1), F gates, and sum over i,j for each c. Exactly one
pair bit is 1; hence a_c is exactly H_(abc), not a sum of noisy unrelated
coordinates. This selection is valid on all [0,1] coordinates. Only the
selected K values are bit-expanded and snapped, saving K^3 snap modules
but not erasing the feature/table/attention/selection costs.

Equation (8) gives 0<=C/M-a_c<1/Q. If Q>=2M, M|a_c-C/M|<M/Q<=1/2,
so (4) recovers every selected count exactly, including equality Q=2M.
These requirements imply the admitted full-family lower bound on h;
in particular h>=4 is retained, even if M is small.

The evaluator's internal integer accumulators are charged computation
and workspace. Only its rounded head outputs are readout ports; the
proof does not supply those accumulators as uncharged counts. Even though
a uniform evaluator necessarily accumulates bit values, the large table
and all operations remain in the resource ledger.

## 4. D3-snap and exact common simplex output

For D3-snap retain the complete admitted finite front end and frequency
recovery prefix in §1. Apply (4) to each a_c. By (3), Q>=256M implies

    M|a_c-C_(s,c)/M| <=76M/Q <=76/256 <1/2.             (9)

All original C1 restrictions on h are then satisfied. No hypothesis about
context frequency is needed for this deterministic recovery. The count
circuits are additional paid modules following that prefix; they do not
alter any accepted predictor or reuse an uncharged normalizer.

Here is the **total** new readout for either comparator, also on bad
inputs where correct count recovery is not guaranteed. For the K recovered
integers C*_c in [0,M], compute

    D=sum_c C*_c+K,
    m_c=floor(Q(C*_c+1)/D), c=0,...,K-2,
    m_(K-1)=Q-sum_{c<K-1}m_c,     output m_c/Q.         (10)

D satisfies K<=D<=KM+K, on every admissible input. Its register is **not**
bounded merely by M+K: independent snapped coordinates need not sum to M
outside the recovery event. For (1), D<2^(m+k); C*_c+1<=M+1<=2^m;
the division dividend Q(C*_c+1)<=2^(h+m) needs h+m+1 bits. Thus w covers
every new readout register, including sums and output buffers. Counts can
be accumulated sequentially with O(w) scratch and K persistent count words.
The zero-context case produces D=K, so there is never division by zero.

For c<K-1, 0<=m_c/Q<= (C*_c+1)/D and the rounding deficit is <1/Q.
Their sum is at most 1, so the last residual is an integer in [0,Q].
Every output has an h+1-bit closed-grid code and the total is exactly one,
even when K>Q or some dyadic output coordinates are zero. The first K-1
deficits sum to the opposite last-coordinate error. It follows that

    TV(m/Q, (C*+1)/D) <= (K-1)/Q.                       (11)

This is an implemented integer add-one and quotient circuit, not K
independently rounded probabilities. The long divisions, sums, final
residual subtraction and dyadic output decoding are all paid. At zero
counts, (10) is a legal dyadic approximation to uniform, not a claim that
1/K itself is dyadic.

At a common Q>=256M, §§3--4 recover the identical integer vector C in
both architectures. They use the same count order 0,...,K-1, denominators,
downward divisions and last-residual rule. Therefore (10) gives identical
integer numerators and hence **bitwise identical** h+1-bit output words,
not just two approximations to the same target. Equation (11) becomes
the asserted bound relative to (2). This proof also covers the actual
terminal query, with no query/history independence assumption.

## 5. Perturbation margins and exact limits of the guarantee

The perturbation interface is deliberately restricted. After each finite
statistical aggregation, clip the affected coordinate and store it **on
G_h**. Define delta as the total absolute difference between that stored
coordinate and the corresponding nominal finite head coordinate. This
includes any clipping and subsequent re-encoding error. Equivalently an
adversary can choose another member of G_h directly. All errors can depend
on the path/query and can be correlated. Inject once before fanout; copies
then carry the stored coordinate, with no extra uncharged perturbations.
Only this post-aggregation model is asserted: query/endpoint/mode/length
bits, binding/features, arithmetic gates, and constant/mask storage are
exact. The accepted finite arithmetic rounding remains, with zeta=1/Q.
An arbitrary real-valued input to bit extraction is outside this model.

For B-C-snap let each returned head coordinate change by at most delta_B.
Exact one-hot selection preserves that bound. A convenient sufficient
condition is

    M(1/Q+delta_B)<1/2.                                (12)

The nominal case delta_B=0 and Q=2M is separately valid by the strict
floor error in §3, even though (12) itself is then not strict. A sharper
uniform margin, including that boundary, is available if desired: with
g=gcd(M,Q), the maximum downward error over C=0,...,M is

    e_B=(M-g)/(MQ) <1/Q.

Indeed residues QC modulo M run through 0,g,...,M-g because Q/g and M/g
are coprime (their multiplication permutes those residue classes).
Thus e_B+delta_B<1/(2M) is another sufficient condition. This is a
coordinate-grid margin; a positive numerical radius need not contain
a nonzero grid step. Clipping can only reduce error to the true frequency.

For D3-snap, if all 9K+1 statistical coordinates change by at most delta_D,
their ideal-head error is at most eta=2/Q+delta_D. Apply the admitted
correlated-error bound with unchanged exact queries/endpoint/flags and
zeta=1/Q. All subsequent a_c are again on G_h. A sufficient condition is

    M(76/Q+35delta_D)<1/2.                              (13)

This pays for normalizer recovery, differencing and boundary terms through
the admitted constant 35, rather than treating c as a new head. The
guarantee includes perturbed rho even though the new final output does
not use rho for smoothing: rho is still used in the D3 boundary correction.
If the actual c register itself is perturbed and re-stored as an additional
port, its total additional error must be added to (13); that is not the
model just stated. Extra multiplication/division error similarly belongs
in 35eta+6zeta, not silently in the nominal 76/Q.

If both (12) (or its sharpened form) and (13) hold at the same Q, perturbed
outputs remain identical to the nominal common output. When those
sufficient inequalities fail, exact snapping is no longer certified.
This alone proves no actual prediction failure, no all-readout lower bound
and no impossibility at other precision schedules. The unconditional
simplex validity and the KM+K denominator bound still hold.

Two explicit failed extensions explain the interface restrictions:

* A symmetric non-strict count radius fails at M=1,Q=16,C=0,A=8 as in §2.
* Omitting re-storage error is false even for the uniform head. Set
  M=7,Q=16,C=1, so nominal a=2/16. Perturb this real value by -1/10000
  and truncate back to G_h: the stored result is 1/16. The uncharged
  re-encoding changes it by a full 1/16, and (4) returns 0 instead of 1.
  The erroneous condition 7(1/16+1/10000)<1/2 would have promised recovery.
  Total delta, not the pre-storage real perturbation alone, is required.

For the range issue, take every selected a_c=1. Then each C*_c=M and
D=KM+K. Already K=2,M=1 gives D=4>M+K=3. This is an allowed bad-event
input to the new readout, so a word provisioned only to the smaller
bound is unjustified. These are mathematical counterexamples to proposed
extensions, not claims that an experiment or a native verifier rejected
a proof. The original accepted Pi and its C3 decoder remain untouched.

## 6. Layer, hold, liveness and parameter ledger for the new readout

The resource convention is the admitted C1 convention: attention is a
finite implemented primitive with its word/work/operation costs separately
charged; L counts attention/pointwise neural layers. Each ReLU coefficient
and all zeros in a dense layout are stored. A sparse layout includes
addresses and explicit identity wires; it is a different declared storage
format, not a free sparse oracle. Both are reported below.

The following is a concrete schedule for K input frequencies on G_h:

|Phase|Active work and depth|Data kept live across it|
|---|---|---|
|Closed-grid expansion|K parallel h+1-bit extractions; O(h) layers, O(Kh) gates|K selected scalar inputs, extracted bits, query/length metadata|
|Snap counts|K serial w-bit multiply/add/bit-routing blocks; O(Kw^2) gates/layers|all remaining input words, K count slots, one O(w)-bit scratch block|
|Add-one/denominator|K additions/summation; O(Kw) gates/layers|K count words, D and output accumulator|
|Simplex divisions|K-1 restoring w-bit divisions, then a residual; O(Kw^2) gates/layers|K count words, D, K output words, O(w) scratch|
|Decode output|K nonnegative dyadic affine rows|all h+1 output bits per coordinate|

Word bounds are in §§2,4, including the bad-event D. All inputs, counts,
outputs, numerator/remainder scratch and metadata together need O(Kw)
live bit/scalar channels. School arithmetic overwrites the dead partial
product/remainder before the next step; no O(w^2) activation history is
retained. Unused old bits are released after their final use. If all D3
query residuals are retained as well, reserve O(Kp) channels instead.

Thus for this new standalone readout there are universal-constant bounds

    G_R,L_R=O(Kw^2), W_R=O(Kw), I_R=O(K^2w^3),           (14)

where G_R counts new arithmetic/extraction/decoding gates before holds,
and I_R counts identity connections through intervening layers. The hold
bound is L_R times the live-channel bound, including carries, count words,
length constants and both input/output buffers; it is not just G_R.
All scalar activation/parameter words fit 128p bits: (1) bounds the new
integers, C1 bounds the retained prefix integers, and dense affine sums
need only O(log(F+Kp))=O(p) additional guard bits. Binary arithmetic uses
bit channels, with exact Boolean outputs; signed prefix values use the
admitted signed rails. The bit-extraction coefficients <=Q and dyadic
output coefficients require O(h) bits and are included in that word bound.

The program in circuit.py gives finite, computable counts as well as these
uniform upper bounds. Serialize its topologically ordered affine/ReLU DAG,
retain a node's value until its statically computed last use, and insert
one identity at each intervening layer. If birth(v), last(v) are those
indices, the number of intermediate identity wires is exactly
sum_v max(0,last(v)-birth(v)-1), with output/retained input words included
as final uses. The peak channel count is the maximum overlap of these
live intervals (plus an optional final output-copy layer). Each transition
can be written as an ordinary dense affine/ReLU layer over its active
channels, or as addressed sparse gates and identities. Its matrices are
not obtained from a free lookup table. The reference interpreter retains
a debugging trace; the charged execution uses the last-use rolling schedule.
The four bounded fixtures in check-results.json report actual gate,
hold and liveness counts for this new block, not an architecture lower bound.

For a separately stored block, (14) gives dense coefficient slots
O(K^3w^4) and dense stored bits O(K^3w^4 p). Sparse program+parameter
bits are O((Kw^2+K^2w^3)p), because a coefficient and a gate/layer
address each need O(p) bits. Addresses fit since log(Kw^2+1)=O(p).
On the common per-neuron 128p-bit activation representation the rolling
readout array costs O(nKw p), not zero memory for Boolean gates.
Dense generic bit operations are O(nK^3w^4p^2). A pointwise implementation
at every token is allowed, though only q's output is used.

Relative to the C1 frequency-recovery prefix, conservatively reserving
all O(Kp) prior query channels throughout the added block gives the
following explicit extra bounds (before subtracting any unused old code):

    new arithmetic gates/layers: O(Kw^2),
    extra live scratch/output channels: O(Kw),
    extra hold connections: O(K^2 p w^2),
    added dense slots: O(K^3 p^2 w^2),
    added dense parameter bits: O(K^3 p^3 w^2),
    added sparse program/parameter bits:
        O((Kw^2+K^2 p w^2)p),
    added rolling online bits: O(nKw p),
    added dense bit operations: O(nK^3 p^4 w^2).          (15)

The old terminal stage (rho floor/max, adding rho, frequency normalization
and its output quotients) is **replaced**, not presumed to have zero cost.
Counting the entire old C1 upper bound plus (15) is a safe larger bound;
the actual schedule executes only the prefix through a_c and then (10).
There is no claim that (15) is a signed saving relative to original Pi.
Since w=O(p), this charged replacement preserves the polynomial orders
in the next section without proving unchanged exact constants.

## 7. Complete front-end and inference resource functions

Put F=K^3, B=128p. Include all token Q/K/V projection matrices; zeros
are charged in a dense layout, and every nonzero coefficient and hold
gets an address in a sparse program. Two rolling neural layers are used.
Only one query is evaluated per run. Max over contexts in the statement
does not mean free parallel evaluation of K^2 queries.

B-C-snap first copies with O(K) scalar width, then uses a constant
number of wide phases of width O(F+K): form the F features and query
pair bits, evaluate the uniform head, select all F coordinates and sum
to K selected values. The F outputs stay live until this selection.
They are then dead; **they are not held through every arithmetic layer**.
After selection the new readout has width O(Kp) and depth O(Kp^2).
Retaining all declared query/endpoint registers changes only these constants.
There are O(F+K^2) front-end nonzero gates/projection coefficients and
O(F+K^2) front-end holds, in addition to (14). This accounts for feature,
table, mask, readout and live-wire costs separately.

The fixed maximum widths and depth can be reported as

    B-C: L=O(Kp^2+1), W=O(F+Kp), H_total=3, H_layer=2,
         D_qk=1, B_param,B_arith<=B, score_range=0;
    D3:  L=O(Kp^2+1), W=O(Kp), H_total=6, H_layer=4,
         D_qk=2K, B_param,B_arith<=B, score_range<=2.     (16)

For B-C, the statistical layer has one head; H_layer=2 is the maximum
from its first layer's two local heads. Total statistical value dimensions
are F+1 versus 9K+1. B-C's table remains K^3-sized even at binary K=2.
The complete value stream also retains O(K) inputs/endpoints/metadata.
No large-value channel or position encoding is uncharged.

The following table uses **layer-shaped dense matrices**, storing all
zeros inside the actual consecutive layer widths. A constant number of
wide phases followed by the narrow readout has dense slot count
O((F+K)^2+K^3p^4), not O(LF^2) holds. Shapes, phase boundaries and
routing are part of the specified program. If a format instead pads every
layer to maximum width, its larger cost is given after the table.

|Resource|B-C-snap|D3-snap|
|---|---|---|
|Dense coefficient slots|O(F^2+K^3p^4)|O(K^3p^4)|
|Dense stored parameter bits|O(F^2p+K^3p^5)|O(K^3p^5)|
|Sparse nonzero gates/projection entries before holds|O(F+K^2+Kp^2)|O(K^2+Kp^2)|
|Explicit layer-spanning identity wires|O(F+K^2p^3)|O(K^2p^3)|
|Sparse program+parameter bits, incl. addresses/holds|O(Fp+K^2p^4)|O(K^2p^4)|
|Positions and explicit Boolean masks|O(n log(n+1)+n^2)|O(n log(n+1)+n^2)|
|Peak rolling activation/attention-scratch bits, excl. stored parameters|O(n(F+Kp)p)|O(nKp^2)|
|Finite attention aggregation/division/score bit operations|O(n^2(F+K)p^2)|O(n^2(K+p)p^2)|
|Dense QKV+pointwise bit operations|O(n(F^2p^2+K^3p^6))|O(nK^3p^6)|

To justify the B-C attention entry, use its exact known-zero weights;
stream a row into F+1 accumulators of O(p) bits, then divide each
numerator by its exact positive denominator, O(p^2) operations per
coordinate. There are O(n^2) scanned edges, O(nF) final quotients and
two local copying heads. Each accumulator word is at most M times a
bit, or MR in the unsimplified admitted representation, fitting B bits.
No numerical n-by-n weight matrix is stored. The projected token array,
F row accumulators and head-output buffers fit the listed workspace.

D3 retains both finite log approximations, their parameter generation,
two product heads, auxiliary partial head, uniform head, all masks and
positions, all 9K+1 head outputs, and the normalizer/boundary/difference
arithmetic of C1. Adding/replacing the new readout as in (15) gives the
D3 entries. Its finite-attention p^3 term per edge is still present as
n^2(K+p)p^2; it is not replaced by a count oracle. Prefix bounds from
C1 and w=O(p) yield every displayed order, including p^6 for dense
generic arithmetic, not the incorrect p^5 operation count.

Total stored bits in either layout are the corresponding parameter
column plus n^2+n log(n+1), constants M,Q and layout metadata O(p).
Total peak online bits add the workspace column. For a fixed-width
dense format padded to each architecture's W in (16), replace the B-C
dense slots by O(Kp^2(F+Kp)^2), bits by O(Kp^3(F+Kp)^2), dense operations
by O(nKp^4(F+Kp)^2), and rolling workspace by O(n(F+Kp)p).
D3 has the same orders as its table. This explicitly charges padding
instead of switching storage conventions during a comparison.

The finite evaluator has stored code as well as data: use shared unrolled
p-bit add/multiply/divide subroutines and finite loop/index control. A
conservative O(p^4) bits covers this microprogram, its constants and
addresses (the uniform specialization needs no more). Coordinate/edge
indices use O(log(nF+p))=O(p) bits. This code is included in the displayed
sparse/dense stored-bit upper bounds, which both dominate p^4; it is not
replicated as a new stored program for each of the n^2 evaluated edges.
The edge/coordinate loops and all their arithmetic executions are charged
in the operation column. A fully expanded evaluator is the separate
flattened convention below, with its larger holds/parameter costs.

Offline generation also costs resources. C1's D3 log-constant generation
needs O(p^3 log^2(p+1)) bit operations and O(p log(p+1)) scratch, plus
writing the chosen parameter format. B-C needs no log/exp constants.
For either new unrolled program, if G denotes the gates before holds in
the relevant table, generating its gate DAG and last-use/hold schedule
uses O((G+I)p) scratch bits and O((G+I)p^2) bit operations, a safe bound
for explicit addresses/constants and finite shifts; add the size of the
chosen stored parameter layout to the writing cost. A streaming compiler
may use less; no such saving is assumed. This is separate from inference
workspace, as it is for C1. Repeated mask/position writing is likewise
charged to the displayed stored size. A flattened Boolean/ReLU convention
can serialize the attention's explicitly counted bit operations and retain
the displayed live words; each step's hold wires and its dense matrices
then have depth-times-width and depth-times-width-squared costs. The
principal table, like C1, uses charged finite-attention primitives.

## 8. The legitimate comparison and the sufficient precision schedules

For target implementation TV epsilon>0, sufficient choices are

    h_B=max(4, ceil(log2(2M)), ceil(log2((K-1)/epsilon))),
    h_D=max(ceil(log2(256M)), ceil(log2((K-1)/epsilon))). (17)

They satisfy 0<=h_D-h_B<=7, since the two count-recovery thresholds
differ by a factor 128 and the other term is shared. This compares two
**sufficient** schedules. It is not a seven-bit necessary precision gap,
a memory lower bound, a statement that the error constants are sharp,
or a comparison of total stored bits. In particular p=4h+4ell+64,
K^3 feature storage, words, wires and matrices must still be substituted
when comparing resources. Even the uniform-floor arithmetic may snap
exactly below the stated sufficient 2M threshold; divisibility can make
its frequency quantization exact. No necessity is inferred from (17).

At a common Q>=256M the new count-plus-output stages are the identical
program (4),(10). Their front ends are quite different: B-C pays F
features, F+1 statistical values, F selection gates and an explicit large
table, while D3 pays four soft heads, finite exp/log evaluation,
normalizer recovery and two-head/boundary differencing. B-C uses only
one-dimensional zero-score Q/K and fewer heads. D3's alphabetic table
does not grow as K^3. Neither set of output identities removes these
costs. For K=2 the table has eight features (nine values with the flag),
not a free counter; the formulas in §7 apply with F=8.

A legal same-budget decision must specify a storage convention and a
componentwise cap on (16), total stored bits, peak work and bit operations,
and verify the corresponding resource functions for the constructed
programs. This proof supplies feasible charged constructions and their
tradeoffs, not a universal numerical cap or an optimization theorem.
In particular, one algorithm lying below a sufficient upper bound for
another does not imply it uses less than the other's minimum resources.
The count/smoothing/output equality proves zero pathwise prediction
separation between these variants at the common precision, but **does
not prove componentwise resource dominance**. No same-budget advantage,
minimal-head claim, all-decoder impossibility or novelty is presumed.

This closes only the exact scoped count-snap comparison unit. It neither
changes the root contract nor closes the finite-N/reliability/integration
obligations. [Non-scientific operational metadata omitted.]
