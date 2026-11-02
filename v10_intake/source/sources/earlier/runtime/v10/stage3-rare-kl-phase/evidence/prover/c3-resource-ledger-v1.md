# C3 resource appendix: operation list, compiler and complete sufficient functions

This appendix is part of `c3-proof-v1.md`. All constants below are
conservative constructive bounds, not measured hardware performance.
It certifies the actual finite program, including attention evaluation,
using the public quantities(3) in that proof. No resource premise is
imported from a source-stage Fact. The machine-readable functions are in
`c3_word_program_v1.py`; the symbolic lists and sample certificates are
separately pinned. A finite interpreter test does not replace the following
all-width construction and inequalities.

## A. Bit gates, full words and explicit hold convention

The elementary Boolean basis is AND,OR,XOR,NOT, with COPY and constant
write/erase each charged as one elementary step. A fanout is a separately
addressed wire; an identity across each layer is separately counted.
Unsigned operands have w bits. Signed values use a sign bit and magnitude
or two nonnegative rails with equivalent bit operations. A product retains
2w bits in scratch before any proved zero-high-bit cast. A divider accepts
up to2w numerator bits and a positive w-bit divisor, retaining a w+1-bit
shifted remainder. We will use w>=2 and

    g(w)=1024w^2.                                       (A1)

Every primitive below uses at most g(w) elementary steps and at most32w+32
scratch bits, in addition to its operand/result words. This bound includes
temporary writes/clears and operand copies required by the operation;
holds of *other* live registers are counted separately.

Here is an explicit justification, rather than a unit-cost-word assumption:

| Primitive | Construction and elementary-step upper bound |
|---|---|
| CONST,COPY,SHL,SHR | Wire each retained bit, write zeros/sign as needed, erase old scratch: <=8w+8. Shifts in this program are public constants. |
| ADD,SUB | Ripple sum uses two XORs, two ANDs and one OR per bit; borrow uses two XORs, NOT, two ANDs and two ORs per bit. Including carries/result copies: <=16w+16. |
| EQ, comparison | Subtract with borrow and/or OR-reduce the XORs; <=32w+32. |
| MUX,MIN,MAX | Per bit two ANDs and one OR plus one flag complement; comparison followed by mux for min/max: <=64w+64. |
| Signed ADD/SUB/MIN/MAX | Compare signs/magnitudes, compute the two possible magnitude sums/differences, mux, canonicalize a zero sign: <=256w+128. |
| MUL | For each of w multiplier bits select a shifted partial product of2w bits and add it with a2w ripple adder; retain the full product. <=64w^2+64w. |
| DIV | For each of2w numerator bits, shift the remainder, compare/subtract the divisor, mux the remainder and write one quotient bit. At most64(w+1) steps per bit, plus initialization/copies: <=256w^2+128w. |

The largest listed bound is <=512w^2 for w>=2. Doubling it for sign
and scratch conventions gives(A1). Divisions in this program have
nonnegative dividends; the general signed division case is not needed.
The named scratch banks are a2w product, a2w quotient, a(w+1) remainder,
a(w+1) trial difference, two2w ripple banks, fourw selection/magnitude
banks, and <=4w+8 carry/control bits: below32w+32. No multiplication,
division, floor or bit extraction is an uncharged primitive.

Each elementary gate can be serialized in at most four affine/ReLU layers:
AND=ReLU(x+y-1), NOT=ReLU(1-x), XOR=ReLU(x-y)+ReLU(y-x), and
OR=ReLU(x+y)-ReLU(x+y-1). A final nonnegative output copy occupies
another layer when needed; four layers suffice with four temporary
channels. COPY is ReLU on a nonnegative register; erasure is a zero
affine row. All other still-live channels receive identity rows. We use
the larger factor16 throughout, reserving room for two-rail updates and
boundary copies. A serialized G-step bit program with S retained channels
therefore has depth<=16G+32, width<=S+8, and holds<=depth*width.
All its static wire addresses are part of the program, not computed from
a hidden-data address oracle. Loops below have public bounds and can be
unrolled before input arrives.

Bit layers have coefficients in{-2,-1,0,1,2}. Scalar grid extraction has
thresholds up to2^h and coefficients up to2^h; scalar output decoding
has coefficients2^(-j), j<=b. Fixed-point QKV uses L2/R,L3/R and bits.
Every such literal fits the declared B or O total coefficient word.
Boolean activation values are exact bits; extraction scalar registers
are bounded by2Q_A, and affine intermediates by a fixed multiple of that.
There is no rounding of these exact Boolean/ReLU operations.

## B. Full online word ranges and named-register liveness

Use frontend word B=128p and output word O=32v from(3). For N>=6,
ell<=h and p>=4h+64. An exp term is <8R, score<2R, product<16R^2;
jR<=8pR. Aggregation over at most n keys is <=6nR; numerator scaling
is <=6nR Q_A. All these need fewer than2p+h+ell+16 bits, even including
full products, sign and remainder guards. Since p>=100 here and
log2 p<p, B covers these and all loop indices and literal coefficients.

Recovery normalizer numerators are <=6Q_A^2, products<=6Q_A^2;
the signed range is[-16Q_A,16Q_A]. A snapped numerator is at most
(2M+1)Q_A. All fit B. On *arbitrary* closed-grid input each of the two
counts is in[0,M], so the output word proof uses D<=2M. Equation(19)
in the main proof bounds its largest new dividend by16mQ, with margin
inside v bits. The2v full-product and v+1 remainder banks fit O=32v.
N<6 uses zero counts in any padded unused arithmetic branch; d=2 remains
positive. No M<=0 recovery is executed.

During recovery retain all23 input words and all63 result names from
section C, rather than relying on an unchecked liveness optimization.
This is86 words, including the19 head masters. Double their allocation
for sign rails, add32B+32 scratch, all19 scalar extraction registers,
their h+1-bit outputs, eight endpoint bits and32 public metadata words:
this is below512B channels. Reserve

    W_F=1024B.                                         (A2)

The output program has4 inputs and41 result words:45 names. The same
signed/scratch/public-metadata argument fits below512O channels; reserve

    W_O=1024O.                                         (A3)

Here a bit channel is a scalar activation of value0 or1. For uniform
coefficient/activation storage accounting each such scalar is allocated
a full B or O-bit representation, overcharging its one useful bit.
The head masters and extraction scalar channels use that same bound.
This explains why rolling *bits* multiply the channel count by a word
length; a channel count is not a stored-bit count.

Before query extraction, each token's projected values, local copies,
19 output masters, one-hots, flags and frontend metadata also fit W_F
channels. A streaming row evaluator adds at most eight accumulator words,
one denominator, and the scratch in section A. It does not store a
numerical n-by-n weight matrix. All per-token arrays and both rolling
layers are paid below. After output begins, frontend banks can be erased;
the padded alternative charges them when kept.

Output-Q literals and the precision b are stored readout-program metadata,
not b-bit words carried in each frontend token. They are loaded into the
O-word output phase after recovery. Their storage is charged in Z0 and
the output program even for arbitrarily large b; no claim that b fits
inside a B-bit frontend register is needed.

## C. Exact recovery list: 19 shared operations plus22 per coordinate

Inputs are19 masters in order
q10,q11,v10,v11,q20,q21,v20,v21,h0,h1,h00,h01,
alpha0,alpha1,nu0,nu1,f0,f1,rho, followed by exact bits a,b,e0,e1.
h0,h1 are T's unflagged coordinates and h00,h01 its flagged coordinates.
MUX(flag,x,y) returns x if flag=1, else y. All masters in this list are
integer numerators. The complete shared list is:

| No. | Result | Primitive and operands |
|---|---|---|
|1|zero|CONST 0|
|2|qa|CONST Q_A|
|3|twoqa|SHL qa,1|
|4|twoM|CONST 2M|
|5|U1|MUX a,v11,v10|
|6|U2|MUX a,v21,v20|
|7|V|MUX b,nu1,nu0|
|8|alpha|MUX b,alpha1,alpha0|
|9|twov|SHL V,1|
|10|num1a|ADD qa,V|
|11|num1|MUL twoqa,num1a|
|12|den1|SUB twoqa,U1|
|13|D1|DIV num1,den1|
|14|num2a|ADD qa,twov|
|15|num2|MUL twoqa,num2a|
|16|den2|SUB twoqa,U2|
|17|D2|DIV num2,den2|
|18|DT|ADD qa,alpha|
|19|matchE0|EQ e0,b|

For each c=0,1 execute these22 operations in order, adding a c suffix
to every result name. The displayed constants c are public literal bits.

| Relative no. | Result | Primitive and operands |
|---|---|---|
|1|PH0full|MUL DT,h0c|
|2|PH0|DIV PH0full,qa|
|3|PHfull|MUL DT,hc|
|4|PH|DIV PHfull,qa|
|5|PQ1full|MUL D1,q1c|
|6|PQ1|DIV PQ1full,qa|
|7|PQ2full|MUL D2,q2c|
|8|PQ2|DIV PQ2full,qa|
|9|I|SUB PH0,fc|
|10|base|SUB PH,nuc|
|11|matchE1|EQ e1,c|
|12|J|AND matchE0,matchE1|
|13|boundary|MUX J,rho,zero|
|14|gplus|ADD base,boundary|
|15|g|SUB gplus,I|
|16|diff|SUB PQ2,PQ1|
|17|H|SUB diff,g|
|18|lower|MAX H,zero|
|19|A|MIN lower,qa|
|20|snapfull|MUL twoM,A|
|21|snapnum|ADD snapfull,qa|
|22|C|DIV snapnum,twoqa|

There are exactly63 word instructions, not an estimated block count.
The signed SUB operations are required. `c3-word-operations-v1.json`
expands all the names without the table's abbreviations. Grid expansion
of the19 scalar masters occurs before this list. Formula(17) needs at
most six ReLU nodes/layers per extracted bit including the remainder;
the following generous gate reserve also covers all scale/copy operations:

    G_F=63 g(B)+256*19*(h+1)+1024B,
    L_F=16 G_F+32.                                     (A4)

G_F counts elementary arithmetic/extraction steps, before unrelated holds.
The last1024B allowance copies all final count/query/public words into
the next phase and erases prior query state; section B's allocation
makes that allowance sufficient. Complete depth and holds are counted
with W_F. The frontend's63-operation dependency graph uses only its
declared inputs, as can also be read directly from the list.

## D. Exact output list: 41 word operations

Inputs are C0,C1,a,b. Here b is the terminal symbol; output bit precision
is the public integer denoted b in(3), with Q precomputed. To avoid
ambiguity the code argument for precision is `bits`. The program is:

| No. | Result | Primitive and operands |
|---|---|---|
|1|zero|CONST 0|
|2|one|CONST 1|
|3|two|CONST 2|
|4|Q|CONST 2^(public precision)|
|5|U|SHR Q,1|
|6|publicUniform|CONST 1{N<6 or public precision=1}|
|7|D|ADD C0,C1|
|8|d|ADD D,two|
|9|twod|SHL d,1|
|10|threed|ADD twod,d|
|11|Z|SHL d,2|
|12|twoZ|SHL Z,1|
|13|twoQ|SHL Q,1|
|14|c1plus|ADD C1,one|
|15|raw1|SHL c1plus,2|
|16|lower1|MAX d,raw1|
|17|z1|MIN threed,lower1|
|18|nearfull|MUL twoQ,z1|
|19|nearnum|ADD nearfull,Z|
|20|J|DIV nearnum,twoZ|
|21|near0|SUB Q,J|
|22|c0plus|ADD C0,one|
|23|raw0|SHL c0plus,2|
|24|z0ceil|MIN threed,raw0|
|25|z1ceil|SUB Z,z0ceil|
|26|Qminus|SUB Q,one|
|27|Zminus|SUB Z,one|
|28|ceilfull0|MUL Qminus,z0ceil|
|29|ceilnum0|ADD ceilfull0,Zminus|
|30|k0|DIV ceilnum0,Z|
|31|ceilfull1|MUL Qminus,z1ceil|
|32|ceilnum1|ADD ceilfull1,Zminus|
|33|k1|DIV ceilnum1,Z|
|34|ksum|ADD k0,k1|
|35|residual|SUB Q,ksum|
|36|ceil1|ADD k1,residual|
|37|selected0|MUX a,k0,near0|
|38|selected1|MUX a,ceil1,J|
|39|uniform|OR publicUniform,b|
|40|out0|MUX uniform,U,selected0|
|41|out1|MUX uniform,U,selected1|

Computing both candidates avoids data-dependent circuit length. All
divisors are positive. This includes the uniform branches and canonical
order exactly. It implements the same integer function as conditional
execution of the Lead readout, while intentionally paying for extra work.
Define

    G_O=41 g(O)+1024O,       L_O=16G_O+32.               (A5)

The added1024O covers copies, zero writes, erasures and two optional
dyadic affine decoding rows. They can instead be omitted when the output
interface is two numerator words with public Q. The output alone occupies
2(b+1) guarded numerator bits plus b+1 denominator bits, or the exponent
b and its length-delimited encoding; both fit the retained metadata bound.

## E. Adapter, features, finite attention: explicit loop work

All masks are Boolean arrays, not an unstored minus-infinity constant.
The input/feature schedule has the following bounded loops. Loops over
row/key/head are public and can be unrolled; all indexed reads/writes
and index arithmetic are included in the budgets below.

1. Encode N binary symbols as one-hots, add the zero query, and write
   positions/flags/public constants. For each of four singleton heads,
   every row i scans its n mask entries and both value coordinates,
   selects `mask[i,j] AND value[j,c]`, and OR-accumulates. Since the
   mask is a singleton this OR is exactly the source's sum and equals
   the selected bit. Include output clears, index tests and writes.
   A bound128n^2+256n **word instructions of width B** covers even
   these bit operations, vastly overcharging actual four-gate pairs.
2. Copy the chosen prefix/query buffer and erase the tail. At each retained
   row form two flag products and the bit selections for QKV. Generate
   QKV as paid finite affine maps with the table's literal coefficients.
   At the query a,b come from its separately bound actual terminal pair.
   This uses at most64n word instructions in addition to the above;
   static addresses and copies of full declared slots are covered by the
   extra1024n word reserve in(A6) below. There are fewer than128
   feature/adapter/routing/projection layers in the hybrid graph,
   including both attention layers, initial/terminal zero writes and
   the query-only extraction. We allocate all128, not just used rows.
3. For each of four statistical heads and each evaluated row, clear at
   most eight accumulators (seven value coordinates plus denominator).
   Scan its at most n_m keys, load the mask, and form a score by bit
   selection of at most two log coefficients and one add. For a masked
   key add zero contributions; for unmasked keys run(10). Each of8p
   iterations uses MUL, a public jR constant/load, DIV, ADD-to-total,
   and at most two loop/index instructions: at most6 word operations.
   Initializing T,total, preparing/selecting the score, loading values,
   muxing at most seven weighted bits, eight accumulator additions,
   mask/index work and scratch cleanup need at most64 further word
   operations per key. If a scalar score interface is used, its <=p+2
   extracted bits cost at most10(p+2) elementary steps, covered by the
   additional16p operations in the next envelope. Thus each key is
   charged64p+64 word operations. Computing exp(0) for the uniform
   head or a masked edge is permitted and paid; skipping it cannot
   increase this envelope.
4. Each final head coordinate is one SHL by h, one DIV and one write,
   with at most19 outputs per evaluated row. Include accumulator erases,
   loop-control copies and master bounds: at most256n further word
   instructions, dominated by the reserve below.

Together all these operations, including masks/addresses, are bounded by

    E=(256p+512)n^2+1024n,
    T_A=E g(B) elementary bit operations.                (A6)

The factor256p comes from4 heads times64p, with n_m<=n. The remaining
512n^2 covers their4*64 constant part and the128n^2 adapter allowance,
leaving128n^2 for boundary/initialization slack. The1024n remainder
covers all described per-row projection/accumulator work, reading the
input and crop/extraction writes, even writing the reserved W_F token
banks bitwise: a word operation pays1024B^2 bit steps, not one bit write.
There is no exact exp or softmax operation hidden in this bound.

Dense QKV and pointwise matrix execution is additionally charged in the
chosen dense model below; using that column together with T_A may
double-charge projection work, which is harmless. The few neural layers
of the hybrid model do not include the8p recurrence as neural layers.
The flattened model includes all T_A steps explicitly.

## F. Principal hybrid layouts and explicit stored/working costs

Put

    P0=128, L_H=P0+L_F+L_O, W=max(W_F,W_O),
    M0=4n^2+4n_m^2,
    Z0=128n(ell+p+b+16),
    I=P0*n*W_F+L_F*W_F+L_O*W_O,
    D=(P0+L_F)(W_F+1)^2+L_O(W_O+1)^2,
    P_D=(P0+L_F)(W_F+1)^2 B+L_O(W_O+1)^2 O.             (A7)

M0 is the exact pair of full-mask storage sizes. Z0 is a concrete bound
for positions, lengths, public program constants other than the two
stored log coefficients, routing tables, token-to-buffer addresses,
flags, lengths of output words, all query endpoint metadata, and the
input/output interface descriptors. A crop table has <=n entries each
with <=ell+1 address bits, not O(n^2) implicit history data. Z0 also
overcharges all b-bit public powers needed by the output block. No data
value dependent source labels are present.

The hybrid resource tuple can be chosen

    L<=L_H, per-token/query W<=W,
    total heads=8, max simultaneous heads=4, D_qk<=4,
    frontend parameter/activation words B,
    output parameter/activation words O, score range[0,2]. (A8)

W is the maximum scalar-channel width of a token or the query phase,
not the total live channels of the token array. A conservative number
of identity *connections* over all evaluated tokens/phases is I. D and
P_D count every zero coefficient in the layer-shaped tokenwise dense
affine matrices; shared matrices are stored once per layer. A constant
number of unequal-width transition matrices is covered by the32 extra
layers in L_F,L_O and 2xy<=x^2+y^2. Query extraction and routing maps
are separate paid fields in Z0 and paid operations in E.

Define the address/control length and shared evaluator-code allowance

    a=bitlength(T_A+G_F+G_O+Z0+1)+ell+16,
    K0=4096g(B)(B+a)+128(p+1)(B+a)^2,
    P_S=64(I+G_F+G_O+1024n)(B+O+a).                     (A9)

P_S stores sparse nonzero arithmetic gates, literal parameters, every
identity, gate/word addresses, phase routing and output selectors. Each
element needs at most a constant number of addresses and a coefficient;
64 times their summed bit lengths is sufficient. Unlike P_S, K0 is the
*shared* finite attention-evaluator microprogram. Store the expanded
Boolean word-primitive library from section A once, with at most12
operation types, each at most g(B) gates and at most64(B+a) bits per
gate/opcode/address record. Their total is below4096g(B)(B+a).
The exp/row/key loops,8p denominator entries, two log integers, word
dispatch and index/call-control records fit the additional
128(p+1)(B+a)^2 bits: one can allocate128(B+a) bits to each of
(p+1)(B+a) public loop/control slots, far more than the stated fixed
number of loop counters and8p denominator words. No optimized compact
interpreter encoding is needed. The library is not replicated per edge.
All its repeated executions are charged by T_A; flattening duplicates
them explicitly instead. The2 stored log integers fit inside K0.

For selected neural format Fmt in {dense,sparse}, total stored bits are

    S_dense=P_D+K0+M0+Z0,
    S_sparse=P_S+K0+M0+Z0.                              (A10)

A sufficient rolling arithmetic/activation/attention-scratch bound is

    W_work=4n W_F B+4W_O O+Z0.                          (A11)

Two rolling token layers, per-row accumulators, arithmetic scratch and
query state occupy fewer than the four allocated front banks; the four
output banks cover old/new query states and scratch during the transition.
Peak online resident bits are S_Fmt+W_work, not either term alone.
The input history is in the token bank; all copy/erase work is charged.

For generic dense fixed-width execution, one multiply-accumulate on
total B-bit numbers costs <=256B^2 bit steps using section A (allocate
full products and sign guard then exact cast where proved). Therefore

    T_dense=256[(P0+L_F)n(W_F+1)^2 B^2
                     +L_O(W_O+1)^2 O^2]+T_A            (A12)

is sufficient for QKV/pointwise projections plus finite attention.
This even executes the query-recovery matrices at all n token positions
although only the query result matters. Unused token states may be
reset to valid zeros before such execution so unused divisions are legal;
the reset rows were allocated. Our principal extracted-query program
executes fewer of these matrices. Biases and all dense zeros are counted.

For shared sparse addressed word execution declare a register-memory
model with a-bit public addresses: a word access reads/writes its word
and address bits and costs their lengths; arithmetic is expanded by
section A, not unit cost. A larger explicit execution bound is

    T_addr=4096(B+O+a)^2 (E+63+41+1024n).                (A13)

This column is *not* a dense neural evaluation or a physical random-access
circuit claim. The read and write address arithmetic is included. A
fully static circuit eliminating indexed-memory access is supplied in
section H. For inference including scalar output decoding, either use
the corresponding dense bound or add the already reserved output steps.
The cheaper entries of different models are never combined as a single
resource claim.

In particular sparse **neural** execution must execute its identities;
it has the sufficient bound
`4096(I+G_F+G_O+1024n)(B+O+a)^2+T_A`, including coefficient/address
reads and all held-channel copies. This differs from the shared register
machine of(A13), where unchanged resident registers do not require a
neural identity operation at each arithmetic step. A complete stored
program bound for that shared word-machine variant is

    S_shared=K0+4096g(O)(O+a)
              +128(63+41+128n)(B+O+a)+M0+Z0.

The second library term stores the O-word output primitives once, with
the same gate/address accounting as K0. The third term stores both full
word lists and all public dispatch/row/control/routing fields. That model
has rolling work W_work, peak S_shared+W_work and online cost(A13).
Sparse neural parameters and the shared word interpreter are therefore
both complete named models, with their different hold/evaluation costs
visible; neither borrows the other's cheap column.

## G. Padded token batch and globally dense batch

If every phase is padded to W and all n token positions remain present,
use L_H layers and full4n^2 masks for each attention layer (8n^2 bits).
All unconsumed and unused history symbols remain in those n banks.
The tokenwise tied-matrix padded bounds are

    slots=L_H(W+1)^2,
    parameter bits=L_H(W+1)^2 max(B,O),
    holds=L_H n W,
    working bits=4nW max(B,O)+Z0,
    operations=256L_H n(W+1)^2 max(B,O)^2+T_A.            (A14)

Add K0+8n^2+Z0 to parameter bits for total stored bits, and add total
stored bits to working bits for peak online memory. This is a one-shot
token batch convention with weight sharing; W is per-token width.

If instead every neural layer is literally a dense affine matrix on the
entire global batch vector, set W_G=nW and use

    slots=L_H(W_G+1)^2,
    parameter bits=L_H(W_G+1)^2 max(B,O),
    holds=L_H W_G,
    working bits=4W_G max(B,O)+Z0,
    operations=256L_H(W_G+1)^2 max(B,O)^2+T_A.            (A15)

Again add K0+8n^2+Z0 to stored bits and add it to work for peak memory.
This larger convention explicitly pays for block-diagonal zeros,
cross-token routing matrices and retained unconsumed input. Both(A14)
and(A15) still regard attention as a finite evaluated primitive with
separately charged T_A; neither is the completely flattened circuit.

## H. Fully flattened Boolean/ReLU circuit

Expand all E finite-evaluator word steps, all recovery/output steps,
every adapter and input/crop/projection operation, and all their publicly
bounded loops. Statically replace array accesses by fixed source wires;
this uses the already public row/key schedule, not a data-dependent
lookup primitive. The arithmetic library from section A computes the
same integer function. Define

    T_F=16(T_A+G_F+G_O+1024nB)+256,
    S_F=4nW_F+4W_O+128(B+O+a),
    B_F=4[B+O+a+bitlength(S_F)+bitlength(T_F)].           (A16)

These bound neural depth, total scalar-channel width and coefficient/
activation bits. The4nW_F allocation holds the raw input, projected
token arrays, head outputs and rolling scratch; the output and auxiliary
banks include all saved public address/counter bits. The allowance is
larger than all named words and scratch in section B. Keeping them for
the entire run is allowed, so no delicate dynamic liveness premise is
needed. Extra buffers do not become authorized decoder inputs: their
only future edges are the declared computation or identities/erases.

Every scalar channel is held across each layer. Thus complete bounds are

    identity connections <=T_F S_F,
    dense slots <=T_F(S_F+1)^2,
    dense parameter bits <=T_F(S_F+1)^2 B_F,
    sparse gates/identities/addresses bits <=64T_F(S_F+1)B_F,
    rolling work <=4S_F B_F+Z0,
    generic dense operations <=256T_F(S_F+1)^2 B_F^2.     (A17)

Add M0+Z0 to stored program size (and retain it even if an unrolled
program no longer needs a separate mask array), then add stored size
to rolling work for peak memory. K0 is unnecessary when its code is
fully expanded, but adding it is harmless. This explicit bound includes
every exponential and division bit step in its depth. It cannot be
described as a two-layer small-width Transformer, nor compared by taking
the two-layer hybrid depth and the flattened absence of a softmax oracle.

## I. Offline generation, layout construction and address costs

All public constants are generated from binary N,b by subtracting,
doubling, bitlength and shifts. Their initialization fits the linear
metadata/copy reserves already stated; for offline accounting add
1024(ell+b+p+1)^2 bit steps and64(ell+b+p+1) scratch bits.

For each q in{3,2}, form the p odd factors and q^(2p-1), multiply to D_q,
then sum2D_q/((2j+1)q^(2j+1)) and perform the final R-scaled quotient.
More explicitly, unroll odd-factor CONST and multiply for p terms,
update a q-power by multiplying q^2 at most p times, multiply the two
products, then for each term do CONST(2j+1), denominator multiply,
exact DIV, SHL-by1, ADD-to-sum, and power update. Finish with SHL-by-p
and DIV. Over both q values this uses <=32p+64 word operations, allowing
initializations, reusable q^2, and all accumulator erases. The generator's
public loop bookkeeping can be statically unrolled with these constants.

The denominator has log2 D_q<4p+ p log2(2p), which is <2p^2 for p>=100;
all individual term denominators and numerators are no larger than a
fixed multiple of D_q, and multiplication byR adds only p bits. Even
full products between two such guarded values fit

    B_log=8p^2+32,
    T_log=(32p+64)g(B_log),  W_log=64B_log.               (A18)

This larger polynomial certificate deliberately replaces any unchecked
optimal rational-arithmetic complexity claim. Only the two final log
integers survive online. Source `Fraction` rational reduction computes
the same sums but is not the proposed finite generator or its cost model.

For any chosen stored layout let U be its complete stored bit count
including its code, masks and metadata, and let Dlen be its declared
layer count (L_H, T_F or the baseline count-plus-output depth). Put

    A_gen=B_log+B+O+bitlength(U+Dlen+1)+ell+b+16,
    T_gen=T_log+1024(ell+b+p+1)^2
                    +4096(U+Dlen+1) A_gen^2,
    W_gen=64B_log+64(ell+b+p+1)
                    +64(U+Dlen+1) A_gen.               (A19)

These complete sufficient functions cover emitting the elementary gate
recurrences, fixed named-register schedule, every zero/dense coefficient,
identity wire/address, full masks, positions, crop maps, all output words
and chosen-format padding. A simple compiler enumerates the public loops
and fixed registers; for each emitted bit/field it performs a constant
number of A_gen-bit index arithmetic operations, costing <=O(A_gen^2)
with the explicit4096 slack. It need not solve a liveness optimization:
the fixed banks in B,F,H are retained. Thus the number of emitted fields
is bounded by U plus Dlen, including layer shapes and all holds. W_gen
even allows storing the entire construction record. Generation peak
including the eventual program is U+W_gen; it is separate from inference
memory. For the baseline no log coefficients are needed, so T_log,W_log
may be deleted; keeping them gives a larger valid bound.

## J. Eight-counter baseline with its own input model

For sequential arrivals, keep eight ell-bit counters, the last two bits,
the position, N,m, an input symbol and bounded ripple/control scratch.
At each arrival compute eight triple-match bits. For each counter perform
a conditional increment by using that enable bit as the initial carry;
each bit uses XOR and AND and so changes nothing when disabled. The public
range flag3<=j<=m disables all updates outside the prefix. Shift the
last two symbols and increment the position. At the end a binary tree of
three word muxes per successor selects the row indexed by the last pair.
Return that pair and the two selected counters to the identical output
phase D. A single observed bit may instead be supplied as a two-bit
one-hot; input encoding is included.

Per arrival there are <=64 match/control elementary gates, <=16ell
counter-update gates, <=32ell range/index gates, and <=16 copy/shift
gates. Final selection uses <=64ell+32 gates. Including initial zeros,
erasure and input reads, the following envelopes are sufficient:

    G_C=1024N(ell+1)+1024ell,
    L_C=16G_C+32, W_C=256ell+64, B_C=32(ell+1).         (A20)

The named state is below64ell+32 bits; W_C leaves room for serial
bit-gate temporaries and exact public metadata. Input arrivals are an
explicit interface, not free storage of past symbols. The *count block*
therefore has sequential width W_C, holds L_C W_C, dense slots
L_C(W_C+1)^2, coefficient bits L_C(W_C+1)^2 B_C, rolling work4W_C B_C,
and generic dense bit operations256L_C(W_C+1)^2 B_C^2.

Its shared counting program, reusing the same eight-counter loop, fits
4096(ell+1)^2 bits, including opcodes and word/bit addresses. Executed
indexed bit work is <=4096N(ell+1)^2, including index/address/control
costs, N input reads and final row selection. Add the41-operation output
program under the same chosen shared/bit or neural model. In a word model
the output costs <=41g(O) plus its copy reserve; no streaming count
claim removes the b-dependent output work and storage.

For a literal **one-shot batch input**, hold all2N one-hot symbol bits
in the initial circuit. A public unrolled schedule consumes them in order
but we conservatively retain all of them until counting finishes. Use

    W_CB=W_C+2N+2ell                                  (A21)

in every count-block width, hold, dense-slot and working-bit formula
above. In particular holds are L_C W_CB, not just O(Nell^2), and dense
slots L_C(W_CB+1)^2. The2ell allowance carries input addresses/index
while the2N history bank survives. No sequential input oracle is used
in this enlarged batch network. B_C covers scalar activations/parameters
because bits and ell-bit constants are retained, not a2N-bit integer.

For either input convention, after counting release its banks and run
the same output block of depth L_O,width W_O and coefficient bits O.
Allocate32 boundary layers for copying selected counts/query/public data.
Thus full depth<=L_C+L_O+32, maximum width<=max(W_count,W_O), holds
<= (L_C+16)W_count+(L_O+16)W_O, and full layer-shaped dense slots
<= (L_C+16)(W_count+1)^2+(L_O+16)(W_O+1)^2.
Multiply each phase's slots by its corresponding B_C or O for parameter
bits, and by256B_C^2 or256O^2 for dense online bit work. Rolling work is
<=4W_count B_C+4W_O O+Z_base, where
Z_base=128n(ell+b+16) pays for all input-index metadata and the uniform
branch/output descriptor. Total stored bits add this metadata and the
appropriate shared code; peak online bits add total stored to work.
There are no attention masks or log/exp constants in this baseline.
For a global single-width dense format pad both phases to their maximum
width and use full depth times squared padded width instead; this is a
further enlarged, explicitly computable bound.

## K. What the certificate establishes

Equations(A1)–(A21), the63/41 exact lists, the explicit exp/aggregation
loops, and the elementary gate recurrences give complete sufficient
functions in N,b. The machine-readable certificate evaluates them; it
does not estimate a hidden universal constant. They retain the familiar
hybrid phase orders L=O(p^2+v^2), W=O(p+v), but the concrete constants
are intentionally enormous. The fully flattened and global batch bounds
are separately much larger. In particular one-shot baseline width
contains2N and hybrid working storage contains the entire token array.

Equality of output words gives equality of the actual-terminal losses
whenever those losses are later analyzed. It does not imply dominance
under any optimized componentwise resource budget. The internal Q_A
schedule, finite score range, widths and number of heads are sufficient
for this program only, not necessity bounds. This nominal arithmetic
certificate is not a noise guarantee or a training/learnability claim.
