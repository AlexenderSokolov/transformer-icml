# Stage5 C3: explicit affine emitter, finite programs and separate full costs

Prover, 2026-10-26. Fixed proof v1.
Obligation `c9d1bbb51ee633f91f029e917ded7f6e1de7f6e9e227f681761ee9ed66b81bec`.
Contract `873515c4586d37a2bde324010bea6ae30f820927b7c25ded15b784a79eef7e45`.
Predecessors: **[]**. All finite premises used here are proved below.

## 0. Claim and interpretation

There exist the two D4 implementations of the exact D3 function, agreeing
on every individual binary observation Z and legal public tuple, within
EVERY corresponding D5 bound. DIRECT is a packed bit-register owned-batch
machine; JOINT is the principal extracted-query batch hybrid with tied
dense tokenwise affine/ReLU layers and a separately charged finite evaluator.
One Boolean neural channel occupies a full beta-bit physical scalar.
Neither implementation is assigned the other's accounting model.

This proof contains no probability argument or C1/C2 reproving. Their
current accepted Facts are not needed as predecessors: the elementary
output guards are proved again locally as finite-domain statements.
Historical files and the new affine-emitter seed are sources, not Facts.
The new seed's concrete two-layer coefficients, alias rule and address
bound are proved and connected to actual primitives and generation here.
Only local workspace copies are used; no old diagnostic is rerun. This
[Non-scientific operational metadata omitted.]
model, counter, contract or resource formula. It does not submit the root.

All arrays mentioned below have explicit bounded rectangular indices.
A bit-register READ/WRITE accesses a labelled bit cell; full words are
read/written bit by bit. Address arithmetic, instruction and coefficient
fetches and dispatch are charged in §10. This is the D5 machine interface,
not a unit-cost arbitrary-integer operation. A finite program/generator
may be specified by bounded loops without allocating its enormous output
inside the proof checker. §§3-4,9-11 give those loops and their expansions.
The companion iterator is a transcription aid; no theorem here depends
on executing Python or treating its integers/GC as hardware primitives.

## 1. Parameters, representations and exact algorithm

Let N>=3, Q=2^b, integer b>=1. For N>=6 define m=floor(N/2), M=m-2,
0<=k<=floor(M/1024), n=N+1, ell=ceil(log2(N+2)), tau=bitlength(k+1),

    h=ceil(log2(256(N-2))), A=2^h,
    p=4h+4ceil(log2(m+4))+64, R_s=2^p,
    s=ell+b+tau+p+32, beta=128s, g=1024beta^2.

For N=3,4,5, k=0 and s=ell+b+tau+32; do not instantiate m,M,h,A,p,
heads or prefix builders. Always n=N+1, Z_meta=1024ns=8n beta.
In particular s>=37 and beta>=4736. In the large branch h>=10,p>=116,
p>=h and h+b+ell+tau<=s. Integers, exponent lengths and powers of two
are computed from public parameters before observations arrive.

In a finite evaluator, an unsigned beta-bit word is a packed field. In a
neural state its bit representation uses beta Boolean scalar channels,
each with beta physical bits. A scalar integer such as a head output is
one beta-bit scalar until the explicit extraction in §6. Full products and
quotients occupy 2beta bits in scratch until justified casts. Signed dense
coefficients use beta-bit two's-complement storage and are decoded signed;
all persistent algorithmic quantities in the present word program are
nonnegative. MAC scratch retains the sign and full product. No modular
product, shortened shifted remainder or unit-cost DIV is used.

For every observed binary string Z, C_sc(Z) counts triples ending at
3,...,m, with preceding pair s and final bit c. Each C_sc is in [0,M].
DIRECT computes the eight integers directly. JOINT computes
j_sc=floor(A C_sc/M) by its actual finite head and appends eleven zero
words; the first eight coordinates have order 000,001,010,011,100,101,110,111.
Both compute eight endpoint controls from observed bits only: four
one-hots for (Z_(N-1),Z_N), followed by four for (Z_(m-1),Z_m).
These are dirty controls, never supplied clean endpoints. Let a,bq be
the actual observed terminal bits. The two ORs extracting them are

    a = ctl[2] OR ctl[3],   bq = ctl[1] OR ctl[3].

After selected-row acquisition each runs the identical 46-operation table
below with alpha=3k+1. The returned port consists of out0,out1,Q, each
b+1 bits, least-significant bit first, and every other source-bearing
location is physically erased. All inputs are Z,N,k,Q; there is no clean
history, parameter, seed or alternative count input.

## 2. Complete selected-row and output tables

Each named result below is a distinct beta-bit SSA destination; repeated
names between tables receive distinct table prefixes. OR/MUX act on the
Boolean control bits. Word MUX(c,x,y) selects x when c=1 and y otherwise.
The JOINT two control ORs above precede these fifteen operations:

| # | destination | operation |
|---:|---|---|
|1|left0|MUX bq,j010,j000|
|2|right0|MUX bq,j110,j100|
|3|selected0|MUX a,right0,left0|
|4|left1|MUX bq,j011,j001|
|5|right1|MUX bq,j111,j101|
|6|selected1|MUX a,right1,left1|
|7|qa|CONST A|
|8|twoqa|SHL qa,1|
|9|twoM|CONST 2M|
|10|full0|MUL twoM,selected0|
|11|num0|ADD full0,qa|
|12|C0|DIV num0,twoqa|
|13|full1|MUL twoM,selected1|
|14|num1|ADD full1,qa|
|15|C1|DIV num1,twoqa|

Thus JOINT uses exactly 17 selected-row operations. DIRECT uses the two
ORs and the first six MUXes with each j replaced by its eight acquired
integer C; the third and sixth destinations are C0,C1. It uses exactly
8 such operations, in addition to the acquisition scans in §5.

The common output table is exactly the following 46 operations. Here
Dsum is the unsmoothed sum, d the smoothed denominator, and Zden an
integer denominator, not the observed string. CONST0 and CONST2 are
retained real operations. The symbol one is always literal 1.

| # | destination | operation |
|---:|---|---|
|1|zero|CONST 0|
|2|one|CONST 1|
|3|kword|CONST public k|
|4|twok|SHL kword,1|
|5|threek|ADD twok,kword|
|6|alpha|ADD threek,one|
|7|twoalpha|SHL alpha,1|
|8|two|CONST 2|
|9|Qword|CONST 2^b|
|10|U|SHR Qword,1|
|11|publicUniform|CONST I{Q=2}|
|12|Dsum|ADD C0,C1|
|13|d|ADD Dsum,twoalpha|
|14|twod|SHL d,1|
|15|threed|ADD twod,d|
|16|Zden|SHL d,2|
|17|twoZ|SHL Zden,1|
|18|twoQ|SHL Qword,1|
|19|c1plus|ADD C1,alpha|
|20|raw1|SHL c1plus,2|
|21|lower1|MAX d,raw1|
|22|z1|MIN threed,lower1|
|23|nearfull|MUL twoQ,z1|
|24|nearnum|ADD nearfull,Zden|
|25|J|DIV nearnum,twoZ|
|26|near0|SUB Qword,J|
|27|c0plus|ADD C0,alpha|
|28|raw0|SHL c0plus,2|
|29|z0ceil|MIN threed,raw0|
|30|z1ceil|SUB Zden,z0ceil|
|31|Qminus|SUB Qword,one|
|32|Zminus|SUB Zden,one|
|33|ceilfull0|MUL Qminus,z0ceil|
|34|ceilnum0|ADD ceilfull0,Zminus|
|35|j0|DIV ceilnum0,Zden|
|36|ceilfull1|MUL Qminus,z1ceil|
|37|ceilnum1|ADD ceilfull1,Zminus|
|38|j1|DIV ceilnum1,Zden|
|39|jsum|ADD j0,j1|
|40|residual|SUB Qword,jsum|
|41|ceil1|ADD j1,residual|
|42|selected0|MUX a,j0,near0|
|43|selected1|MUX a,ceil1,J|
|44|uniform|OR publicUniform,bq|
|45|out0|MUX uniform,U,selected0|
|46|out1|MUX uniform,U,selected1|

There are 63 JOINT or 54 DIRECT selected-row/output word operations.
The endpoint bit bq forces rows01/11 uniform; when bq=0, a distinguishes
00 from10. Thus the final terminal MUXes implement exactly the D3 cases.

### 2.1 Guards on independent closed inputs, not just real histories

For arbitrary independent j in [0,A], floor((2Mj+A)/(2A)) is in [0,M]:
the dividend is at most A(2M+1), and its ratio is at most M+1/2.
For actual j=floor(AC/M),

    0 <= C-Mj/A < M/A <= 1/256 < 1/2.

Indeed A>=256(N-2)>256M. Consequently nearest snapping returns exactly C.
Selection uses only the observed terminal controls. Eleven unused words
may independently lie in [0,A]; they are read, retained and later cleared,
but cannot affect the selected result. Controls may be either valid pair
one-hot independently; no source consistency is needed for the guards.

For independent C0,C1 in [0,M], not assuming their sum <=M, put
D=C0+C1+2alpha, Zden=4D. Then

    2<=D<=2M+6k+2<=3m,
    Zden<=12m, 2Zden<=24m, 0<4(Cc+alpha)<Zden.

The last strict inequality follows because the other smoothed count is
positive. Nearest z1 lies in [D,3D]. Thus J rounds Q*z1/Zden to nearest,
with half ties upward. If Q>=4, Q/4 and3Q/4 are integers, so
Q/4<=J<=3Q/4. At Q=4 the switch points 3/8 and5/8 select 1/2 and3/4
at equality. If Q=2, 1<=J<=2; the possible zero in Q-J is unused because
publicUniform selects (1,1). No unused candidate is evaluated as a log.

For the ceiling branch both z_c are in (0,Zden) and sum to Zden. The
unrounded (Q-1)z_c/Zden sum to the integer Q-1. If integral, the two
ceilings sum to Q-1; otherwise their fractional parts sum to1 and the
ceilings sum toQ. Hence residual is0 or1; both final numerators are
positive and sum toQ, with each at mostQ-1. This also covers exact
remainder zero, Q=2, and all zero counts. At C0=C1=0 both branches are
uniform; a single zero count is harmless because alpha>=1.

All SUBs are nonnegative, every DIV divisor positive, and the full
integer products/dividends satisfy

    snapnum<=A(2M+1),
    nearnum<= (6Q+4)D<=8QD<=24mQ<32mQ,
    ceilnum_c=(Q-1)z_c+Zden-1<Q Zden<=12mQ.

The subtractions Q-1 and Zden-1 use literal1, not alpha. These estimates
cover eagerly evaluated candidates even in a discarded uniform branch.
They contain fewer than h+ell+4 bits for snapping and b+ell+6 for output.
Head accumulation and products use fewer than p+h+ell+8 bits. All these
bounds, coefficients used in extraction (<=2^h), public alpha, and
counts are <2^(beta/16): beta/16=8s leaves ample sign/carry space.
The generic primitives below retain full products/remainders before these
bounds justify a beta-bit cast. Output numerators and Q fit b+1 bits,
including Q's endpoint bit. This proves bit-identical D3 output once §5's
acquisition is proved, not merely equal real-valued probabilities.

## 3. Concrete finite primitives and public gate iterator

The Boolean basis is AND, OR, XOR, NAND, NOT, COPY, CONST0, CONST1 and
MUX. Each is one logical assignment with public source/destination indices.
It has at most three input bits. No conversion to NAND is made. A COPY
includes its read and write; a padded word action writes all destination
bits including zeros. The following explicit routines suffice at width
w>=2; use w=beta at runtime. Scratch below excludes retained SSA inputs
and final outputs and is reused between operations.

A ripple adder maintains carry c. At bit i generate, in order,

    t=XOR(x_i,y_i); u=AND(x_i,y_i); v=AND(c,t);
    dst_i=XOR(t,c); next=OR(u,v); c=COPY(next).

This is six assignments per bit. Computing t,u,v before dst_i makes the
routine safe even for in-place dst=x or dst=y. Copy the final carry to
a separate flag before clearing scratch. Do not infer no overflow from
modular arithmetic: a call's static range proof or its wider destination
justifies clearing that flag. A borrow chain uses

    t=XOR(x_i,y_i); nx=NOT(x_i); u=AND(nx,y_i);
    nt=NOT(t); v=AND(nt,borrow); dst_i=XOR(t,borrow);
    next=OR(u,v); borrow=COPY(next).

It has eight assignments per bit and retains its final borrow. Unsigned
comparison uses this borrow and equality uses an OR reduction of XORs.
MIN/MAX use a comparison followed by one MUX per output bit. Word MUX
uses one MUX per bit. Fixed shifts, constants and copies are explicit
bit loops, not machine instructions of uncharged size.

For multiplication use a 2w-bit zero accumulator P and a 2w-bit addend.
For j=0,...,w-1 set addend_i=AND(x_(i-j),y_j) when j<=i<j+w, zero
otherwise, and add it to P with the 2w ripple routine. After j iterations
P equals x times the j low bits of y; P<2^(2w). The final carry is zero
by this bound, and all 2w result bits are retained before a cast. Each
iteration costs at most 2w addend assignments, 12w ripple assignments,
seven flag writes/clears and public control; zeroing addend and flags at
the end leaves the inputs/product alone. A conservative bound on logical assignments, including copied
temporaries and cleanup, is64w^2+64w. Bit-data accesses and address/dispatch
charges are distinguished below; no dynamic counter is silently charged
as a single Boolean gate. This is a full product even when later used by DIV.

For division, keep the entire 2w-bit numerator U, a w-bit positive divisor
v, a 2w-bit quotient and a (w+1)-bit remainder. Initially remainder=0.
Process numerator bits j=2w-1,...,0: shift the remainder left and append
U_j, subtract the zero-extended divisor in w+1 bits retaining borrow,
set take=NOT(borrow), MUX the difference or shifted remainder, and write
take into quotient bit j. If the old remainder is <v, the trial value is
2r+U_j<2v<2^(w+1); the new remainder is again in [0,v). Induction gives
U=quotient*v+remainder at the end. The quotient is 2w bits until a proved
range justifies a cast. This proves zero numerator, v=1 and all exact or
nonzero remainders. Shifting a shortened w-bit trial remainder is forbidden.

A division step needs w+1 shift writes, 8(w+1)+9 subtract/flag operations,
w+1 MUXes, a NOT and a quotient write, plus <=16(w+1) control/copy/clear
steps if expanded without recycling. Over 2w steps plus initialization,
full input/output retention and final zeroing, 256w^2+128w is a safe bound.
No quotient-dependent stopping or data-dependent iterator is required.

The following bounds count logical assignments, including scratch cleanup.
The iterator is a generator; execution uses the explicit wiring library
and pays its fetch/PC/address control in §10.

| operation | logical assignments |
|---|---:|
| CONST/COPY/fixed SHL/SHR |8w+8|
| ADD/SUB retaining carry/borrow |16w+16|
| EQ/unsigned compare |32w+32|
| word MUX/MIN/MAX |64w+64|
| full 2w multiplication |64w^2+64w|
| full-numerator restoring DIV |256w^2+128w|

Each row is <=1024w^2, but we also need a BIT-ACTION bound rather than
merely a gate bound. A direct count of the displayed data iterator gives
14w^2+12w+6 assignments for MUL and20w^2+49w+14 for DIV, before harmless
extra padding clears. A basis assignment needs at most three input-bit
reads, a truth operation and a destination-bit write, hence at most five
bit-data actions. Adding <=32w+32 full scratch/input-copy zero writes and
<=64w+32 ancillary copy/flag actions gives, for the worse DIV case,

    100w^2+341w+134 <= 1024w^2  (w>=2).

The inequality follows at w=2 and the difference is increasing thereafter.
The shorter primitives satisfy it as well; ADD/SUB have <=16w+16 logical
assignments and the other linear routines can be implemented by one
borrow/equality chain plus one bitwise MUX. For actual w=beta>=4736 there
is also more than512beta^2 of slack for the O(beta) scan-bundle controls
used in §§5,7. Full padded instruction and a-bit address accesses are
separately paid by §10's surcharge, not assumed to take one bit action.
Thus g(beta)=1024beta^2 is valid for the stipulated finite bit primitives,
without any NAND expansion. Input snapshots, product and quotient fields, shifted
remainder and difference, two addend/sum buffers and flag cells require
at most 20w+32 scratch bits, within 32w+32; one can allocate the larger
fixed bound and zero unused cells. Even storing separately a 2w numerator,
2w product, 2w quotient, w+1 remainder, w+1 difference, 2w addend,
2w sum, 4w input copies and32 flags totals16w+34<=20w+32.

A primitive iterator is a finite counter automaton, not a subroutine
oracle. Its state is (opcode, phase, outer j, inner i, microstep, base
addresses). ADD has one bit loop with six microsteps; SUB eight; MUL has
outer j, addend i and ripple i phases; DIV has outer j and shift/subtract/
select phases, each one inner i loop. No stack recursion is used. CONST,
COPY, MUX, EQ and compare have one bit loop. For each microstep the above
list fixes its opcode and indices base+i, base+j or base+i-j. At a phase
boundary increment/reset bounded counters and advance the fixed phase
label. This enumerates exactly the gates and writes, including full width
zeros. Depth of arithmetic loop nesting is at most two, with a finite
microstep selector; ≤12 simple counter actions advance one descriptor.
Operand-address formation uses ≤8 additions/comparisons. These generation
actions are charged separately in §11, not multiplied into the logical
word-operation count or silently absorbed into a free iterator.

## 4. Literal two-layer affine renderer, including every alias

Reserve s0=W-2 and s1=W-1 in the fixed W=2048beta channels, disjoint
from all primitive data, controller fields and destinations. The augmented
index W denotes the affine bias convention; it is not an extra resident
activation. Store the redundant constant row/column in (W+1)^2 slots and
pay its evaluation too. The evaluator supplies literal1 as a public MAC
operand, rather than maintaining an uncharged W+1st state cell.

For an instruction z=op(operands), let each row be a list of (column,
coefficient) terms. The stored coefficient at (row,column) is the SUM
of all terms with that column. Thus coincident source indices add; they
are never overwritten by a dictionary assignment.

Layer1 copies every non-scratch data row with the identity term (i,1).
Its scratch row lists are:

| opcode | s0 terms | s1 terms |
|---|---|---|
|AND/OR/XOR/NAND x,y| (x,1),(y,1),(W,-1) | empty |
|MUX c,x,y| (c,1),(x,1),(W,-1) | (y,1),(c,-1) |
|NOT/COPY/CONST0/CONST1| empty | empty |

Apply ReLU. Layer2 sets both scratch rows empty, copies every other row
except z with its identity term, and gives z the following terms:

| opcode | z terms |
|---|---|
|AND| (s0,1) |
|OR| (x,1),(y,1),(s0,-1) |
|XOR| (x,1),(y,1),(s0,-2) |
|NAND| (W,1),(s0,-1) |
|MUX| (s0,1),(s1,1) |
|NOT| (W,1),(x,-1) |
|COPY| (x,1) |
|CONST0| empty |
|CONST1| (W,1) |

In either layer the augmented constant row has (W,1). Every absent entry
is an emitted/evaluated zero. Coefficients after collision aggregation
are in [-2,2]; signed beta-bit encoding suffices.

On Boolean inputs, ReLU(x+y-1)=xy. Hence the second-layer formulas are
xy, x+y-xy, x+y-2xy, 1-xy, 1-x, x or the constant. For MUX the scratch
values are cx and (1-c)y; they cannot both equal1, even when operands
alias each other or the control. Their sum is exactly MUX(c,x,y).
If x=y the first scratch coefficient at that index is2. If y=c in MUX,
the second scratch row cancels to zero. Layer1 preserves all data, so z
may alias ANY operand without destroying a needed source. Layer2 writes
z, preserves all other data, and resets both scratch cells even if their
old values were nonzero. This proves the templates for arbitrary allowed
aliases, not just for distinct SSA variable names.

Each logical Boolean assignment uses two layers. The actual basis of §3
is compiled directly, not first expanded to NAND. Reads/copies/clears are
COPY/CONST assignments or physical evaluator actions already paid below.
A bit circuit of B assignments therefore uses 2B layers and W channels,
with an explicit identity coefficient for every held active coordinate.

For a scalar integer j in [0,2^h], bit extraction is also explicit. At
index i descending from h to0, maintain remainder v<2^(i+1), except
initially v<=2^h. Form in one layer
f=ReLU(v-(2^i-1)), g0=ReLU(v-2^i); in the next layer write bit=f-g0;
in a third write v-2^i*bit, and in a fourth clear the two temporaries.
For integer v the difference is 1 iff v>=2^i; the new remainder is in
[0,2^i). All data needed at a stage are preserved until use. The
coefficient rows have at most three terms, with magnitudes <=2^h.
The endpoint j=A therefore has its high bit retained. Initialize high
padding bits to zero. Nineteen words take 4*19(h+1) extraction layers;
256*19(h+1) in G is more than sufficient even counting reads, copies,
control bits and zero writes. This is not a rounded real comparison.

There are 63 word operations in JOINT. By §3 each consumes <=g actual
bit actions and at most that many logical assignments. Initialization,
logical copies and cleanup of the layout in §7 take <=8192beta actions,
and the three guarded port fields take <=128(b+1). Thus the actual
compiled Boolean/extraction work is at most

    G=64g+256*19(h+1)+8192beta+128(b+1).

The extra word allowance over63 is retained. With the extraction's
four-layer steps and <=64 fixed transition/padding layers, the actual
query depth is at most 16G+96=L. One can pad to L using explicit
identity/zero layers, not implicit zero-cost skipped matrices. All
padding matrices and holds are charged. No per-gate whole-bank clearing
is introduced: each dense layer overwrites its destination bank.

## 5. Actual Z-only acquisition in the two separate implementations

### 5.1 JOINT frontend and finite attention evaluator

The frontend has an explicit scalar-slot map at each token: current
one-hot at0,1; synthetic-query flag2, eligible flag3, public position4,
owned raw input5; the four head outputs in consecutive pairs8..15;
eight first-AND temporaries16..23; eight triple features24..31;
terminal one-hots32..35 and dirty prefix one-hots36..39; nineteen scalar
masters40..58; eight numerator accumulators60..67, denominator68 and
two full-product limbs69,70; public weight/scale/literal fields71..95.
The finite evaluator's Boolean scratch begins at128 and reserves
32beta+32 cells; a following64beta region contains its full a-bit address
records and public literals. This whole map uses fewer than100beta cells,
leaving disjoint copies within the four banks. At query n the retained
scalar region P in B3 is [512beta,512beta+27), far from both this map and
the later <=512beta query layout. The final port uses B3's §6 four-beta
range beginning at186beta+32. Renderer scratch is always W-2,W-1.
These fixed disjoint addresses also specify the emitter's field names.

For triple label abc, the first AND reads10+a and8+b into16+label,
and the second reads that result and current coordinate c into24+label.
Terminal control ab reads14+a and12+b into32+2a+b; prefix control ab
reads10+a and8+b into36+2a+b. All gates therefore have explicit public
indices. The one-hot input complement is ReLU(1-raw-query_flag), so the
synthetic row has both value coordinates zero. Other rows give1-Z_i,Z_i.
The public flags/position fields are loaded from metadata with the paid
input/routing bundles. Scalar masters are copied from P to each word's
base slot in §6; one at a time copy the scalar to a separate extraction
remainder in the64beta transfer range, initialize its other bit slots,
then extract downward. The base slot becomes bit0 only at the final
step, after its scalar value is no longer needed. This avoids an alias
between the original scalar and an early extracted bit.

Read exactly N binary observations into owned full-beta scalar cells,
form (1-Z_i,Z_i), and create at n=N+1 a synthetic zero-valued query.
It is not an extra observation. Four zero-score singleton heads select
keys i-1 (fallback i), i-2 (fallback i), i, i on historical row i.
On query n they select m,m-1,N,N-1 respectively. These masks are nonempty
and causal. Store and examine all 4n^2 mask bits, including zeros. The
heads have value dimension2; all Q/K entries are literal zero, hence
score magnitude0 and QK dimension at most4 (dimension0 would suffice).
The finite zero-score weight is exactly R_s. A singleton's full numerator
A R_s times its bit, divided by R_s, is exactly A times that bit; the
following exact scale cast recovers the bit. No approximation to exp or
softmax is required or used. All full products are within §2.1's guard.

Each historical token then owns current and two lag one-hots. At every
eligible position form each of eight triple features by two ANDs:
first the two lag indicators, then AND with the current-symbol indicator.
All sixteen gates are actual charged affine/ReLU gates, not a triple
table supplied as input. At query n form four pair one-hots from heads
4,3 for S_N and four from heads2,1 for the dirty prefix endpoint.
The identical tokenwise operations on other rows are harmless and paid.

Crop public indices 1,...,m into a prefix view and route actual query n
to its query slot m+1; this is an index map and paid copy within the
existing banks, not a new observation or a fifth data allocation.
Store the entire (m+1)^2 mask. Query m+1 allows keys3,...,m. For other
rows i>=3 allow keys3,...,i, and for i=1,2 allow key i as a nonempty
causal fallback. These unused rows can be evaluated and discarded. The
mask generation and evaluation therefore have well-defined values at
all entries, including zeros and the small m=3 case.

The fifth head has score0, eight triple-feature values and exact weight
R_s. At the actual query its denominator is M R_s>0, numerator for
coordinate sc is A R_s C_sc(Z), and its integer output is exactly

    floor(A R_s C_sc/(M R_s)) = floor(A C_sc/M).

No clean path or Markov assumption enters this deterministic identity.
Append eleven explicit zero words; retain all nineteen scalar words
and all eight dirty controls until their paid extraction/erasure. The
nineteen words are internal registers, not an information restriction
on a competing predictor.

Here is an explicit frontend schedule within the 128 construction layers;
unused layers are padded by stored identity/zero matrices:

| block | layers available | actual construction |
|---|---:|---|
|input one-hots, query zero, public flags/positions|8|constant/copy/NOT rows and paid input writes|
|four singleton projections, finite calls and routing|16|four parallel heads plus fixed value copies|
|eight triple indicators|32|sixteen sequential two-layer AND assignments|
|eight endpoint one-hots|16|eight two-layer AND assignments|
|prefix routing, value projection and fifth finite call|16|fixed index map, eight value copies and one head|
|concatenate/pad19 and controls|16|copies and eleven zero rows|
|prepare retained-query region|16|fixed destinations and initialized padding|
|reset/identity padding|8|explicit identity or zero rows|
|total|128||

Four further phase layers for retained copy, old-state clear, query
handoff and phase reset give the fixed132 frontend allowance. Serial
full-bank sweeps and finite attention arithmetic are charged in E, not
hidden in four layers. Every matrix in the table is tied tokenwise;
nonlocal input binding occurs only through the displayed attention masks
and the charged finite evaluator's fixed index-map transfers. The
coefficient rows are explicit identity/zero/NOT/COPY rows or §4's
three-term gate rows. Thus they have a literal renderer too.

An explicit finite evaluator loops head,row,key,value-coordinate. It
reads every mask bit, including excluded keys, and gates their values to
zero. It initializes denominator and value accumulators, accumulates
full R_s-scaled values, shifts by h and performs the full division and
range-justified cast. Public row/key/coordinate increments/comparisons
are included as word-bundle actions; no data-dependent search occurs.
A singleton entry needs at most16 bundles (mask read, two value reads,
two gated/scaled values, two numerator additions, denominator addition,
index updates, temporary clears). Four full scans use <=64n^2; row
initialization, quotients, scale casts and reset add <=64n. The fifth
head entry needs <=32 bundles (eight reads, eight gated values, eight
additions, mask/denominator and loop/clear work); its row setup/final
normalizations add <=64n. Input reads, public routing and endpoint
handling add <=64n^2. Since n>=7, their sum is <256n^2. Doubling to
512n^2 pays all ancillary input validation, value copies and scans.
A bundle may be an arithmetic operation with control, or a full-width
store with its short-index updates. The sharp data-action bounds below
§3 leave room in g for such O(beta) control work. General instruction
fetch/address costs receive the additional §10 surcharge.

There are five total heads, at most four simultaneous, maximum value
width8, QK<=4 and score magnitude0. All n full token banks remain
charged until the physical sweep in §7, even though only the eventual
query result is needed.

### 5.2 DIRECT paid batch scan

Own the same entire Z in a packed bit array; create its needed copy and
scratch in the 8N allocation. Initialize eight beta-bit counters.
For each j=3,...,m and each of the eight public lexicographic labels
(a0,b0,c0), read the three bits, use their bit/complement to make the
three equality indicators, use two ANDs, and increment that label's
counter by the feature. Read and write each counter explicitly. Use all
eight labels rather than an uncharged source-dependent counter address.
Three equality actions, two ANDs, an ADD, reads/writes, label advance
and temporary reset fit twelve bundles per label; triple reads and
outer controls bring the total below128 per triple. Input ownership,
validation/copy, metadata work and final input clear fit a further64n
bundles. Dirty endpoints and one-hots are computed from the owned Z with
fewer than64 bundles. Execute the actual8+46 operations in §2.

The induction after each eligible triple states that each counter is
exactly its count in the processed prefix; therefore DIRECT obtains
C_sc(Z). Section2.1 proves JOINT snaps to these same integers, so both
programs execute the same output table on the same counts and controls.
This proves per-string guarded-port equality, not just equality in law.

Packed scratch need only the eight counters, eight controls, 54 SSA
results, full primitive workspace, public literals/address records and
output copies. Even reserving 512beta bits for those fields, and
4096beta for duplicate/cleanup buffers, is within8192beta. Together
with 8N owned/input/copy bits and a Z_meta public working copy, this is
W_work=8N+8192beta+Z_meta. Clearing all those bit cells is explicitly
charged; no Python object lifetime is a physical-memory premise.
The action counts just listed, initialization/54 operations, full
port writes and scratch clears are dominated by (512n+2048)g=G:
metadata read/write needs at most16n beta bit actions, packed scratch
clears at most8192beta, and output length is <beta. These quantities
fit the margin beyond128n+118 word bundles since beta>=4736.
DIRECT has E=L=W=dense_slots=P_bits=mask_bits=I_holds=0 and core=G;
its ordinary memory and every access remain paid in the other coordinates.

## 6. Query address width and disjoint live layout

The runtime address-record width a is exactly D5:

    Haddr=G+E+Z_meta+N+L+1,
    a=beta+bitlength(Haddr)+32.

It is NOT a beta-bit word. We prove a<2beta before allocating records.
For JOINT, using h+b+ell+tau<=s and beta=128s,

    G<=2^17 beta^2, L<=2^22 beta^2,
    E<=2^9 n^2+2^15 n beta+2^19 beta+8beta+1024,
    Z_meta=8n beta.

These follow directly from D5, W=2048beta, h+1<=s+1 and beta>=4736.
Adding terms gives Haddr<2^24(n+beta)^2. As n<2^ell, elementary binary
length bounds give

    a<=beta+60+2ell+2ceil(log2 beta)<2beta.

For the last strict inequality, ell<=s=beta/128, and for beta>=4736,
60+2ceil(log2 beta)<beta/16. One proof uses ceil(log2 x)<=log2 x+1:
x/16-62-2log2 x is positive at4736 and has positive derivative thereafter.
Thus the extra terms are <5beta/64. For SMALL, n<=6 and
G=(128n+512)1024beta^2, E=L=0 obey the same Haddr envelope.
For DIRECT at N>=6 do NOT use JOINT's bound on G: here

    G=2^19(n+4)beta^2,
    Haddr<2^22 n beta^2,
    a<=beta+56+ell+2ceil(log2 beta)<2beta.

The displayed looser constants absorb bitlength endpoint rounding.
All comparisons remain valid for arbitrarily large b,N,k. Segmented
index fields fit a; no flat runtime pointer of bitlength(U_stored) is
assumed. Flat generator addresses use a_gen separately in §11.

Use these disjoint logical-cell ranges in each query bank, by cumulative
sums starting at coordinate0:

| length | role |
|---:|---|
|27beta|19 acquired masters and8 observed controls, each padded to a word|
|63beta|distinct JOINT17+46 results, including paid constants|
|32beta+32|full-product, quotient, shifted-remainder and primitive scratch|
|64beta|public literals and sixteen full a-bit address/controller records|
|4beta|three final guarded fields and finite serialization reserve|
|64beta|retained-query transfers, MAC/controller data scratch and copies|

The sum is254beta+32. Sixteen address records use <32beta cells; the
remaining32beta in that range suffice for all fixed literals and bounded
loop state. A conservative doubling of every range plus80 extra flag
cells uses508beta+144<512beta, since beta>=4736. This contains the two
rails/copies if one elects to retain them; the actual unsigned program
needs only one Boolean rail. The two renderer scratch cells W-2,W-1
are outside these ranges. More than1536beta spare cells remain before W.
The scalar-form masters, extraction remainder and its two scalar
scratch cells occupy the transfer region until bit extraction finishes;
they do not require a new bank. MAC signed/full-product scratch and
finite evaluator fields fit the same reserved regions in its own bank.
Public metadata working storage is the separately paid Z_meta and
contains no Z bits, counts, endpoints or source-dependent flags.

At most eight copies/zeroings of the <=512beta live logical fields are
needed for initialization, scalar/bit handoff, final port copy and logical
scratch cleanup. Including both a read and a write costs <=8192beta;
additional complete physical scans are paid in E. The final port needs
3(b+1) initialization writes, reads and writes of its two numerators
and Q, and old-copy clearing, less than128(b+1) actions. This justifies
the nonprimitive terms of G without multiplying E by the number of gates.

## 7. Four physical banks, paid clears and release order

Allocate exactly four rolling banks B0,B1,B2,B3, each nW physical beta-bit
scalar fields before extraction. Owned Z/input one-hots, lag and triple
fields, cropped values, endpoint controls, head accumulators, products,
remainders, scalar masters and all layer copies occupy the named ranges
or spare cells within these banks. Attention scans reuse accumulators
one row at a time while the entire n-token data remains resident.
B3's query region holds finite-evaluator/controller scratch and a
reserved retained-query region P. No stack of previous layers or fifth
external accumulator bank exists.

During query neural computation, B0,B1,B2 cycle as input, first-layer
output and committed output; B3 contains the finite evaluator's bounded
scratch/control and the eventual port region. A dense destination is
written in full, including zero/identity rows. Old copies in the other
banks remain physically charged until overwritten or finally swept.
Only the current neural state's identity rows count as neural identity
holds; old buffer residence is storage in W_work, not a fictitious
unpriced neural layer. Every buffer access is separately charged.

The actual physical trace is as follows; all scans have public bounds.

1. Initialize the four nW banks, including unused fields. Read/copy N
   observations and then execute the paid frontend. No token bank is
   released during the132 frontend phases.
2. Traverse the four banks to copy the nineteen scalar masters and eight
   controls into disjoint P at query n, including explicit zero padding.
   Complete these copies first. Traverse again and overwrite every
   physical field outside P and the public-only scan controller with
   zero: input/tail, endpoint copies, lags, triple values, head sums,
   product/remainder scratch and both old layer buffers are all included.
   Clear the controller's source-bearing temporary after its last use.
3. Only now release nonquery token allocations. Initialize the query
   layout, copy P's fields into its master/transfer region, and overwrite
   old P. Extract all nineteen words into bits as in §4, retaining the
   eight observed controls. No external input pointer is read again.
4. Evaluate the63 selected/output operations with the three-bank cycle.
   After both final numerators are available, initialize a disjoint
   guarded port in B3, copy all3(b+1) final bits there in the declared
   order, including literal Q, and only then clear old output fields.
5. Sweep all four query banks by (bank,channel,physical-bit) order,
   skipping only the designated guarded port and public scan indices.
   Zero all old inputs, masters, controls, arithmetic intermediates,
   old ports, extraction/renderer/MAC/controller data scratch and copies.
   The controller has no observation-dependent address; it clears its
   final data temporary before return. Only public code/indices and the
   final port remain. High physical padding bits are zero too.

The batch initialization and two traversals in steps1-2 require at most
12nW full-scalar bundles. Reserving16nW covers input-routing/handoff
passes as well. A scalar sweep bundle includes a full beta-bit write,
a short increment/compare/reset sequence (at most six O(beta) operations)
and scratch reset; these together are <g. General a-bit instruction and
address manipulation is charged in §10. After release, at most eight
complete four-bank query passes, including layout initialization, old-P
purge and final clearing, plus fixed field transfers, require <64W
bundles, within256W. No such full-bank sweep is inserted per gate.

Initial/master/control/port literal transfers and physical serialization
need fewer than1024(h+b+ell+tau+1) extra bundles: there are19(h+1) bit
extracts, eight controls, three(b+1)-bit output fields and a fixed number
of public loop/literal transfers; fewer than16 bundles per such bit plus
256(h+ell+tau+1) for public initialization/clears suffice. Extraction's
neural work is already in G; this additional payment covers its physical
interface and may deliberately count copies twice.

Together with §5.1 the finite evaluator and all physical sweeps obey

    E=512n^2+16nW+256W+1024(h+b+ell+tau+1).

All source-bearing data are in the four banks throughout. The worst
simultaneous working memory is 4nWbeta+Z_meta. After release it is
smaller; W_work continues to charge that maximum. Dense layer destination
writes are paid in dense MAC work, and full physical sweeps in E*g.
Neither garbage collection nor "unused later" is treated as erasure.

## 8. All fixed D5 resource coordinates

The expressions below are the fixed bounds, not newly enlarged envelopes.
For JOINT at N>=6 use

    W=2048beta,
    G=64g+256*19(h+1)+8192beta+128(b+1),
    L=16G+96,
    E=512n^2+16nW+256W+1024(h+b+ell+tau+1),
    dense_slots=(132+L)(W+1)^2,
    P_bits=dense_slots*beta,
    mask_bits=4n^2+(m+1)^2,
    I_holds=132nW+LW,
    core=256(132n+L)(W+1)^2*beta^2+E*g,
    W_work=4nWbeta+Z_meta.                                (R1)

For DIRECT at N>=6 use

    G=(512n+2048)g, E=L=W=0,
    dense_slots=P_bits=mask_bits=I_holds=0,
    core=G, W_work=8N+8192beta+Z_meta.                     (R2)

For N=3,4,5, BOTH use the packed uniform branch

    G=(128n+512)g, E=L=W=0,
    dense_slots=P_bits=mask_bits=I_holds=0,
    core=G, W_work=8N+8192beta+Z_meta.                     (R3)

All neural coordinates, including heads, values, QK, scores and layers,
are zero in R2 and R3. In R1 there are132 frontend/phase layers, L query
layers, widthW, five total/at most four simultaneous heads, value width8,
QK<=4, score0. All these were constructed in §§4-7.

For each implementation and every N retain EXACTLY

    a=beta+bitlength(G+E+Z_meta+N+L+1)+32,
    K_code=4096*g*(beta+a)+4096*(s+1)*(beta+a)^2,
    U_stored=P_bits+mask_bits+Z_meta+K_code,
    T_online=4096(a+beta)^2*core,
    peak_online=U_stored+W_work,
    a_gen=beta+bitlength(U_stored+T_online+N+L+1)+s+32,
    Emit=U_stored+L+1024,
    T_gen=1024s^2+4096*Emit*a_gen^2,
    W_gen=64a_gen+64*Emit*a_gen,
    peak_gen=U_stored+W_gen.                              (R4)

The output length is3(b+1), GPU work0. These are sufficient upper bounds
for each realization; padding may attain some storage bounds without
making actual work optimal or equating the models. No shared-budget,
Bstar inclusion, statistical or architectural superiority follows.

### 8.1 Dense evaluation, physical scalars and identity holds

Store every coefficient, bias slot and redundant affine row as a signed
beta-bit field. Store all zeros and identities, including padding layers.
The132 frontend matrices act at all n tokens; the L query matrices at
one token after actual release. This gives dense_slots and P_bits, and
at most132nW+LW active identity-channel holds. Attention masks have
exactly the declared full rectangular sizes and include their zeros.
One may evaluate every crop row in the finite evaluator, so zero mask
entries are also actually read. No sparse matrix discount is taken.

A full signed MAC is implemented by magnitude extraction/sign handling,
the shift-add product, full signed accumulation and a proved-safe cast.
For general beta-bit operands the elementary multiplication assignment
count is14beta^2+12beta+6; even counting <=5 bit reads/writes/truth actions
per assignment, sign conversion, full2beta accumulation, initialization,
fetches and scratch zeroing, <=256beta^2 elementary bit actions suffice
for beta>=4736. All product bits are retained. Actual partial sums in
our matrices have at most three nonzero terms (or one identity), with
bounded scalar/literal magnitudes from §2.1. Even the crude bound
4*2^(2s+4) is far below the signed beta-bit range; zero entries introduce
no growth. Scalar extraction coefficients <=2^h and the public positions
and R_s also obey this bound. Thus accumulation never relies on modular
overflow. Evaluating the entire (W+1)^2 matrix, even zero coefficients,
costs <=256(W+1)^2 beta^2. Multiply by132n+L and add E*g for the separate
finite evaluator/physical sweeps to obtain core in R1. The general
instruction/address surcharge in §10 is additional, so basic operand
fetches may be counted twice, conservatively.

The finite evaluator's bit scratch is located in B3's declared cells.
If a scratch bit is represented as a neural Boolean scalar we pay beta
physical bits for it too. A constant row is an affine evaluation
convention, not a fifth bank or a free resident scalar. Four banks plus
public metadata give the simultaneous W_work bound in R1 even during
copies. U_stored remains resident concurrently, yielding peak_online.
For DIRECT/SMALL the analogous argument uses packed bits as in R2/R3;
no neural scalar width is silently substituted there.

## 9. Stored executable code, metadata and exact acquisition of operands

Use segmented addresses (bank,token,channel,bit) for data and
(layer,row,column,coefficient-bit) for dense parameters; masks use
(head,row,key), libraries (primitive,record,field-bit). A full field
is represented in a bits and retained as such. All segment bounds fit a:
W=2048beta, layer<=132+L, token<=n, bit<=2beta, and library record<=g;
the code size has logarithm bounded by a few times log2(beta+a), which
is also below a since beta>=4736 and a<2beta. Mask row/key segments fit
ell+1. Flat runtime addressing of all coefficient bits is unnecessary.
Multiplications used for segment offsets are explicit finite arithmetic;
repeated linear scans can instead increment the last segment and carry.
The word fields for such counters and the full a-bit records are in §6.

An explicit primitive library uses at most24 types: the Boolean basis,
word constant/copy/shifts/add/sub/compare/equality/select/min/max/full
multiply/divide, bit read/write and a combined scan-next/reset routine
share their displayed circuits. Counting overlapping types only once
keeps the number <=24. A type's finite wiring list has <=g records,
each <=64(beta+a) bits: opcode, up to three source tuples, destination
tuple, literal/shift fields, next-record/phase information and padding.
This is explicit bit-circuit wiring, not a stored instruction that grants
unit-cost multiplication. The total is <=1536g(beta+a), below the first
4096g(beta+a) part of K_code. Shared macro templates are instantiated by
public bases; their index arithmetic is paid, not precomputed data.

Fewer than512 other descriptors suffice: 63 table entries, at most32
head/input/crop descriptors, sixteen mask/position cases, at most64
literal/parameter/format records, at most64 scan/phase/port records and
padding. Each occupies <=64(beta+a) bits. Their total32768(beta+a) is
below4096(s+1)(beta+a)^2 since (s+1)(beta+a)>=8. This covers either the
smaller DIRECT table or the SMALL program too. The unused remainder
of K_code is actually generated and stored as zeros. Dense query gates
are already stored as dense matrices; their full unrolled instruction
list is not redundantly claimed to fit a constant-sized SSA table.
The finite evaluator uses the shared primitive library; query matrices
are emitted by iterating the SSA and primitive descriptions.

Public metadata is explicitly encoded as at most64 records per token,
each at most8s bits, and a duplicate. Fields describe the position,
validity/synthetic-query flag, four key-selector cases, crop index map,
eight feature labels, eight endpoint labels, nineteen master labels,
head shapes, public N,k,b,h,p and literal powers of two, and format/loop
bounds. Public scalar literals A,R_s,Q have lengths <=s. Segmented
runtime a-bit addresses belong to K_code and the controller range,
not to a falsely truncated metadata field. No large flat address or
source statistic is stored in an8s metadata record. The total is
2*64*8ns=Z_meta. A separate full working copy of this public metadata
is charged in W_work. Unused positions and padding are generated zeros.
All observations, counts, dirty controls and masks applied to data live
in the charged data banks, never disguised as public metadata.

## 10. Complete online address/dispatch surcharge and small branch

A basic logical bit assignment accesses at most three inputs and one
output. Expand an actual execution into bit reads, truth operations,
writes and public control. For a word operation the gate counts in §3
leave enough slack for all bit-data accesses within g, as proved in §3.
For each such action or dense MAC bundle, instruction/operand/coefficient
fetch and dispatch read fewer than128(a+beta) padded bits and perform at
most32 public increment, comparison, reset, sign-extension or offset
operations. The fixed tuple formats in §9 witness this: at most four
operand tuples, one instruction record of length64(a+beta), an opcode/
phase record and a carry chain through at most eight segment counters.
No source-dependent pointer or unbounded search occurs. Field reads and
writes are literal bit loops. A padded instruction record is streamed one
field at a time into the sixteen declared address records and literal
slots; its entire64(a+beta)-bit stored record is never an extra live buffer.
Address arithmetic acts on a-bit fields:
the sharp elementary routines of §3 cost less than128a^2 per full
schoolbook operation for a>=4736. Since a<2beta, a+beta>3a/2, so this is
less than64(a+beta)^2. Simpler increment/copy/compare operations cost
less. Source-data arithmetic was already counted in core and is not
reperformed as an address operation. Thus32 such operations plus the
128(a+beta) fetched bits are below4096(a+beta)^2 per core action.
Therefore

    actual online time <=4096(a+beta)^2 * core.

This deliberately large multiplier pays full padded field reads, all
instruction/operand/coefficient addresses and dispatch. It is not a
claim that an a-bit record is one beta-bit register or that a word access
is a unit hardware instruction. The array model permits a labelled bit
read/write; its entire address manipulation and each accessed bit are
charged. Mask/parameter/metadata bits read by the evaluator have the
same surcharge. Keeping all stored arrays and working banks concurrently
proves the exact peak_online formula, not merely separate maxima that
could fail at a copy boundary.

The early N=3,4,5 branch is taken before any prefix parameter or head
builder. It owns exactly N input bits and pays their reads/validation,
initializes a fresh three-field port, writes Q/2,Q/2,Q least significant
bit first, then zeros owned input and every scratch/old port copy.
Public Q=2 is ordinary here. Output length3(b+1)<beta; packed temporary
and copy storage fits8192beta, owned inputs/copies8N, public working
metadata Z_meta. Input and metadata read/clear uses <64n g, port and
fixed scratch processing <256g, both below(128n+512)g. All neural
coordinates are zero, as in R3. No fictitious sixth input, m/M, frontend
or max(N,6) statistical padding is executed. R4 supplies its separate
stored code, dispatch, online work and peaks with the SMALL parameters.

## 11. Full finite generator and its per-unit work

Here is a generator for the complete realization, including all zero
storage. Its counters and transitions are part of the construction.
There is no oracle giving an arbitrary matrix coefficient or a "next
gate" for free. The generator sees only N,k,Q (or b from its dyadic
representation). Its output sections, in order, are HEADER, LIBRARY,
DESCRIPTORS, METADATA, MASKS, FRONTEND MATRICES, QUERY MATRICES, and
padding/delimiters. DIRECT/SMALL skip the empty neural sections. The
resulting program/arrays have exactly their allocated lengths in R4.

### 11.1 Initialization and finite state

First test N. In SMALL, do not calculate any prefix parameter. In the
large branch derive m,M,ell,tau,h,p,s,beta and the literal powers by
bitlength scans, shifts and additions. The number of input/literal bits
is <=16s, and fewer than128 such linear scans/additions suffice;
1024s^2 bounds this initialization for s>=37. Computing large cap
expressions (G,E,L,K_code,U_stored,T_online and a_gen) is NOT charged
as an O(1) part of this initialization: use a fixed expression tree of
fewer than128 additions/multiplications/bitlength operations. Charge
one node to each of128 explicit header units, from the +1024 allowance
in Emit. Each unit emits its public header delimiter; if retained in the
runtime image, its format bits occupy the already reserved K_code padding. Schoolbook operations on at most a_gen-bit magnitudes cost
<1024a_gen^2 per node, including addresses and carries, below the
4096a_gen^2 per-unit allowance. All intermediate positive quantities
can be ordered so that their magnitudes are bounded by the final
U_stored+T_online+N+L+1 or its displayed parameter components; the
added beta+s+32 in a_gen covers full public literals and indices.
In particular addresses of emitted bits never exceed U_stored and
layer indices never exceed132+L. Resource upper bounds such as T_gen
are certificate formulas; their binary value need not be used as an
online loop counter. No circular unit-cost computation of a_gen is used:
ordinary variable-length binary registers grow to at most that proved
bound during these fixed expression evaluations.

The generator is a finite counter automaton with these levels:

1. output section and public template state;
2. primitive type or SSA position (at most24 or63 respectively);
3. primitive phase and its outer and inner bit indices from §3;
4. layer phase (0/1 for a Boolean gate, 0..3 for scalar extraction);
5. row and column of the complete (W+1)-square matrix;
6. coefficient encoding bit.

The library/wire section instead uses record/field/bit counters. Masks
use head,row,key; metadata uses token,record,field,bit; the port uses
field,bit. All are bounded integer loops. The primitive has at most two
nested loops and finite microstep state. The total nested counter stack
has at most twelve a_gen-bit fields at any moment; up to sixteen more
hold parameters, sparse row terms and accumulated offsets. No recursive
call stack or search through previous matrices is required.

### 11.2 Descriptor transitions and literal coefficient emission

For each primitive descriptor the iterator executes the displayed
ADD/SUB/MUL/DIV microstep lists. Base+i, base+j, base+i-j determine
all register endpoints. At a completed inner loop, reset its index,
advance the finite phase or outer index; at a word boundary move to the
next of the explicitly printed63 SSA states. The generator's finite
control has one state per printed instruction, so it does not search
through a variable-length history to discover the next opcode. At most
six counters can reach a boundary together; at most twelve reset/
increment comparisons and eight endpoint additions plus fixed phase
updates suffice to produce the next gate. Even allowing opcode decoding
and zero/copy phases, <=48 elementary counter actions suffice. Charge
this transition to the next layer delimiter, not to an absent "free"
step. The L delimiter allowance covers query layers, with frontend's
132 and the128 header units fitting in the additional1024 units.

For a Boolean layer, form the row-term list by §4. At most three terms
are present, including the bias. Iterate every row, every column and
every beta encoding bit. Test equality of each term's column to the
current column, add ALL matching coefficients, and emit the signed
encoding bit. Coefficient collisions therefore produce2 or cancellation,
never a lost operand. Even zero coefficients are encoded beta bits and
all identity rows are visited. The coefficient is in [-2,2], so its
signed bit is selected by comparisons with the bit index; no large
integer exponentiation or numerical oracle is needed.

Frontend layers use the same finite gate rows, plus fixed disjoint
COPY/NOT/CONST/projection row ranges. Row membership takes at most
sixteen endpoint comparisons (eight ranges). Extraction uses at most
three nonidentity rows with coefficients1,-1,-2^i and biases
-(2^i-1),-2^i. Their signed encoding bits are explicit comparisons
against i and the sign bit; no lookup into an exponentially long table.
Phase matrices are fixed identity/zero/copy lists. Thus at most three
column tests, three small coefficient additions, eight bit-selection
operations and six row/column/bit counter updates, in addition to the
sixteen range/opcode tests, suffice per emitted coefficient bit: fewer
than48 actions. A frontend multiple-copy row is selected from disjoint
ranges; there is never a sum over all W potential nonzero sources.
This bound describes how the coefficient is COMPUTED. It does not omit
the cost of EMITTING every one of the (W+1)^2 beta coefficient bits.

Library wiring records are produced by the same primitive iterator;
fields are fixed opcode, endpoints and literals. The iterator advances
once per record and record bits are then streamed. Descriptor advances
cost <=48 actions and can be attached to that record's first emitted
bit (all records have positive length). A record bit needs <=12 further
counter/copy actions, so <=60 actions at that first bit. Padding records
are explicit zero loops with the same counters. No gate expansion is
repeated by seeking from the start of an earlier primitive.

For masks, each emitted bit is the Boolean formula in §5: row=query
versus historical, key equal to one of the four selected indices, or
3<=key<=row in the cropped head (with fallback for rows1,2). At most
sixteen compare/add/Boolean actions plus eight counter actions compute
it. Metadata uses the explicit record formats in §9, with current
position/label constants copied bitwise; <=40 actions per bit suffice.
Parameter/header or padding bits and guarded-port descriptors use
shorter versions of the same loops. The generator emits final-port
wiring/format, not observed output data. Every unused code, metadata,
mask, coefficient and padding bit is emitted as well.

### 11.3 Work, storage and simultaneous generation peak

For clarity, an elementary counter action above is an increment,
addition/subtraction, comparison, reset or bounded field copy/bit select
on at most a_gen bits (a constant number of concatenated fields can be
streamed). Ripple carry, subtraction/borrow, lexicographic comparison
and explicit bit writes implement each in <=32a_gen^2 bit steps,
including reading its finite-control instruction. For an explicit
address-free implementation of a generator counter action, keep its fixed
number of registers as binary tracks, scan from low to high for carry,
from high to low for comparison, and sweep to copy/select a requested bit.
Even a bounded-register selection followed by a full bit-index scan uses
<32a_gen^2 track reads/writes/moves. In the header, shift/add multiplication
or restoring division uses at most a_gen outer passes, each with a
constant number of length2a_gen track sweeps, within1024a_gen^2. Thus the
generator bound includes access to its counters rather than recursively
assuming a unit-cost large-word address operation. General
per-bit units require at most64 counter actions, hence <=2048a_gen^2;
the common4096a_gen^2 allows the remaining finite-state dispatch,
byte/bit encoding and delimiter writes. Transitions not immediately
emitting a bit are attached to the actual positive-length record or
layer delimiter just specified; there is no uncharged long seek.

Exactly U_stored stored bits are emitted. At most L query delimiters,
132 frontend/phase delimiters,128 cap/header units and a fixed number
(<256) of section switches suffice. They are below L+1024. Thus the
number of charged units is at most Emit=U_stored+L+1024, and total work
is at most1024s^2+4096 Emit a_gen^2=T_gen. This is an explicit terminating
algorithm for each finite public tuple, not an instruction to allocate
an enormous netlist during this proof run.

The counter automaton, the128-node public expression evaluation (whose
values may conservatively all be retained) and the full arithmetic scratch
need fewer than256 a_gen-bit working words. Since Emit>=3, these already
fit64a_gen+64 Emit a_gen. The still more conservative allocation of64
initial words plus64 words per emitted unit is exactly the prescribed
W_gen=64a_gen+64 Emit a_gen. Retain every already
emitted bit of the stored program simultaneously, and the peak is at
most U_stored+W_gen=peak_gen. The generator's flat file address fits
bitlength(U_stored+T_online+N+L+1)<a_gen, unlike runtime's segmented a.
Its program is a fixed finite counter machine with the printed finite
state lists; no observation, u,t or channel seed enters its constants.
This proves both online and offline simultaneous peaks in the SAME
fixed D5 formulas, without granting an O(1) coefficient oracle.

## 12. Scope, new splice checks and completion

Sections1-2 prove exact closed-domain semantics; §§3-4 prove the finite
primitives and literal renderer; §5 constructs both actual acquisitions;
§§6-7 allocate and clear all physical state; §§8-11 prove every separate
D5 coordinate and a finite complete emitter. Therefore each individual Z
produces exactly the same D3 guarded port in DIRECT and JOINT. C1 applies
to this function once combined by Lead; no statistical premise was needed
for this construction. C2 is not a finite-program predecessor.

The new standalone c3_affine_iterator_v1.py checks only the new splice:
117 varied full-product/full-numerator primitive cases,278 successive
complete dense two-layer transitions from actual in-place multiplication
and restoring-division iterators, and784 emitted coefficient bits
including colliding operand/destination indices. Its checks include
nonzero initial scratch, full dense zero/identity entries, signed encoding
and final primitive/renderer scratch clearing. These finite checks are
transcription evidence only, not a proof of all-N costs or an admission.
The seed's earlier8832 alias cases and12 examples, and all old diagnostic
suites, were not rerun. The analytic arguments above cover the entire
parameter domain and are the submitted proof.

The source seed and method/preparation reviews have no Fact status in
this proof. Source versions and the new artifacts are hashed separately.
No old Bstar, shared-cap claim, mathematical oracle, free scalar bit,
Python integer time or garbage collection is used. Only a normal gateway
verdict on this exact C3 obligation can admit this result. Root combination,
fixed independent review and final_audit remain outside this submission.

## Appendix P. Fixed provenance and artifact boundary

- `PROBLEM.md`; SHA256 `960299dbb9730b6f8b7d9de81128fabcca03b7342a456beb57572e52d490caca`; current contract, D1-D7.
- `inputs/c3-affine-emitter/AFFINE_EMITTER_SEED.md`; SHA256 `7ea9c78e8a0c6586d1d2a5d46ae5fd937c10e4b02d6dcbad86548b358b1d08a0`; new constructive seed, source only.
- `inputs/c3-affine-emitter/method-review.json`; SHA256 `eb7188b397e463b90d6cafba53e722230ce20bb68eb482a3c58446739a6c6c87`; independent method discussion, no Fact.
- `outputs/001-input-contamination/verifier/preparation-review-v1.md`; SHA256 `d31f00c7748d05ca7974f7ef3cbff18424f954a07a0ec315d5830bbbc760d8b0`; interface discussion, no Fact.
- `inputs/source-stage4/outputs/001-relative-code/prover/c3c4-integrated-v1.md`; SHA256 `2fc89f6bca30288d766fcdb71b26875943f2d6efb5fc9a181b401dba1f7e243a`; historical primitive/frontend/table lineage only.
- `inputs/source-stage4/outputs/012-input-contamination/prover/finite-program-v1.json`; SHA256 `3875340ee76fa75ad61cc9db5e4483bb03e1971eeaa9b5d8973545bb2a83ec44`; historical exact operation transcription.
- `inputs/source-stage4/outputs/012-input-contamination/prover/upper-program-certificate-v1.md`; SHA256 `b1a0de75230bb5ec2cd58417e09f2c0bb3ca7818e2fd513c6e0333f81b7beab4`; historical D5/program source only.
