# C3 finite causal realization: complete fixed candidate v1

Prover, 2026-10-25. Exact current obligation
`c82d400c69019a551db29a66e99faec5bfbf281097c5c8ae57075ea5789772fb`.
This is a deterministic proof for every binary input path, under current
PROBLEM.md D1–D6. No old native Fact is used. The resource appendix below
is part of this proof, not an unproved Big-O reference. It is also provided
separately as `c3-resource-ledger-v1.md`. The accompanying word-program
interpreter/certificate and code audit are checks, not mathematical premises.
The candidate awaits fixed-version review; no gateway submission is made.

## 1. Exact claim and finite computation convention

For integers N>=3 and b>=1 let Q=2^b. A public-length binary input
X_1,...,X_N is observed; X_(N+1) is not. Coordinates are (next0,next1).
The output is the following exact D4/C2 integer function. For N<6,
Q=2, or actual terminal pair S_N in {01,11}, it is uniform. Otherwise
put m=floor(N/2), M=m-2, and let C0,C1 count only triples ending at
positions3,...,m whose first two symbols equal S_N. Set d=C0+C1+2.
For row00, z1=min(3d,max(d,4(C1+1))), Z=4d and

    J=(2Qz1+Z) div (2Z),      output=(Q-J,J)/Q.           (1)

For row10, z0=min(3d,4(C0+1)), z1=4d-z0, Z=4d, and

    k_c=((Q-1)z_c+Z-1) div Z,
    e=Q-k0-k1,               output=(k0,k1+e)/Q.         (2)

Here div is integer Euclidean quotient. We construct these counts from
four actual statistical heads, not a supplied count table, and prove
that the final integer words equal those of a charged eight-counter
sequential algorithm on every path. This transfers the output function
of C2, not an unadmitted risk theorem. The proof does not need stationarity
or the unknown u,t, and therefore applies to every D1 observation.

The principal architecture uses causal unscaled dot-product attention,
finite coefficient/exp/aggregation arithmetic specified below, and exact
bit/ReLU pointwise circuits, without LayerNorm. Two attention layers are
present, with four heads in each. Their *internal finite evaluations* are
charged in bit operations, stored evaluator code and working space; they
are not silently counted as a few Boolean layers. The separate fully
flattened circuit expands all of those operations as well. Integer
quotients, scalar-to-bit interfaces, routing and holds are all implemented.

Define, also for the harmless small-N resource envelope,

    n=N+1, m=floor(N/2), n_m=m+1,
    ell=ceil(log2(N+2)), h=max(4,ceil(log2(256(N-2)))),
    Q_A=2^h, p=4h+4ceil(log2(m+4))+64, R=2^p,
    v=b+ell+8, B=128p, O=32v.                            (3)

Ceil-log2 here is computed as bitlength(x-1) on positive integers.
It is not a real-log oracle. All schedules are public functions of N,b.
Q_A,p are independent of output Q. For N<6 the program reads its input
interface and emits the uniform words; it does not run a nonexistent
M<=0 statistics circuit. For N>=6 the reference code computes its
frontend even when the final output branch is uniform. We charge that
larger execution; an early public Q=2 bypass is optional, not assumed.

## 2. Physical causal binding, masks and information lifetime

At physical positions1,...,N place two-bit one-hots x_i=e_(X_i).
Place a synthetic zero-symbol query x_n=(0,0) at physical n=N+1, after
all observations. This is not X_(N+1). Public metadata includes positions,
N,m,M,h,p,b, a query flag and z_i=1{i=3}; z_n=0. Store positions in
ell-bit registers; the resource appendix pays for their bits and uses.

The first attention layer has four paid heads with zero Q,K and V=x.
Each row has a single permitted key, represented by an explicit Boolean
mask. For historical row i, heads1,2 select i-1,i-2, falling back to i
if unavailable. Heads3,4 select i. At the physical query n the four
selected keys are, respectively, m,m-1,N,N-1. All keys are <= their
query position. A singleton softmax is exactly one; the finite integer
evaluator returns its bit values exactly. Thus the historical records
contain lag1,lag2, while the query has separately

    E_m=(X_(m-1),X_m) from heads2,1,
    S_N=(a,b)=(X_(N-1),X_N) from heads4,3.

In the local head/flow formulas the letter b denotes the second query
symbol; it is distinct from the public precision integer in(3). Code
uses `bits` for precision in the word program. Output precision literals
are stored separately and loaded at readout, not carried as b-bit words
in the frontend token channels.

The complete four singleton masks cost exactly4n^2 bits. Query formation
occurs here at physical n, before any routing. A paid fixed routing map
copies records1,...,m and the query to a buffer of length n_m and erases
the other records. Calling the query's buffer slot m+1 does not move its
physical observation time. The prefix record at key j is
(x_j,lag2_j,lag1_j,z_j). Form F_(j,c)=ReLU(lag1_(j,c)+z_j-1), an exact
bit product. These values do not depend on the query.

The second attention layer uses the following heads at the query:

| Head | Query Q | Key K at j | Value V at j |
|---|---|---|---|
| P1 | ((log2) e_a,(log2) e_b) | (lag2,lag1) | (x,lag2) |
| P2 | ((log2) e_a,(log3) e_b) | (lag2,lag1) | (x,lag2) |
| T | (log2)e_b | lag2 | (lag1,F) |
| U | 0 | 0 | (lag2,lag1,F,z) |

This table specifies ideal weights for the algebra; section4 replaces
log and exp by finite operations. The QK dimensions are4,4,2,1; value
dimensions4,4,4,7. There are exactly19 statistical output coordinates.
At the query, eligible keys are exactly3,...,m. The synthetic query and
all discarded tail positions are ineligible. If other rows are evaluated,
use eligible keys3 through their retained historical position, or self
when that prefix is empty, and their local lag pair as query. These rows
are unused and do not change the query's output. All masks are causal and
nonempty. Their explicit representation costs4n_m^2 further bits.

After the second layer, extract at the query just those19 coordinates,
the eight one-hot bits representing S_N,E_m, and paid public metadata.
Erase/release historical arrays and all unused query intermediates.
All subsequent recovery work is pointwise on this interface: no raw
history, hidden count table, clean statistic residual or later attention
enters the decoder. Mathematical empirical counts below are comparison
objects, not registers supplied to this interface. After snapping the
two counts, discard the19 masters, all normalizers and E_m; only counts,
S_N and public readout constants enter (1),(2). The appendix charges
copies, extraction, erases, static routing maps and every intervening hold.

For a convention forbidding crop/extraction as layout operations, a
separately enlarged padded batch construction retains all n physical
positions, masks the query to the same prefix, and carries all unused
slots with zeros/identities. Its larger mask/width/hold bill appears in
the appendix; no free compaction is needed for existence.

## 3. Algebra of the four ideal heads for every finite prefix

For this section N>=6, so M>=1. Define empirical source-pair masses

    u_ik=M^(-1) sum_(j=3)^m 1{X_(j-2)=i,X_(j-1)=k},
    alpha_i=sum_k u_ik, nu_k=sum_i u_ik, rho=1/M,
    f_c=rho*1{X_2=c},
    c_(ab,c)=M^(-1) sum_(j=3)^m 1{(X_(j-2),X_(j-1),X_j)=(a,b,c)}.

The uniform head returns alpha,nu,f,rho. Its initial flag selects exactly
key3, so f is an initial *symbol* mass, not an initial pair mass.
For head T the weight is1+1{lag2=b}. Its mean weight dT=1+alpha_b and
its two kinds of outputs h_c,h0_c obey, by direct summation,

    dT h_c=nu_c+u_bc,
    dT h0_c=f_c+rho*1{(X_1,X_2)=(b,c)}.                  (4)

Let J_c=1{E_m=(b,c)}. The list of source pairs
(X_1,X_2),...,(X_(m-2),X_(m-1)) and the list of successor pairs
(X_2,X_3),...,(X_(m-1),X_m) cancel except at their endpoints. Hence

    g_c=dT h_c-nu_c+rho J_c-(dT h0_c-f_c)
       =M^(-1)sum_(j=3)^m 1{(X_(j-1),X_j)=(b,c)}.       (5)

This exact flow identity uses E_m, never S_N, at its terminal boundary.
It is valid for M=1 and for zero selected-row counts.

For k=1,2 let lambda_k=1,2. The product head weight is
(1+1{lag2=a})(1+lambda_k 1{lag1=b}). Its mean d_k and its lag2 output
coordinate U_k selected by e_a satisfy

    d_k=1+alpha_a+lambda_k nu_b+lambda_k u_ab,
    d_k U_k=2(alpha_a+lambda_k u_ab),
    d_k=(1+lambda_k nu_b)/(1-U_k/2).                     (6)

The denominator is in[1/2,1], uniformly even for a rare or absent row.
Define successor marginal r_c=M^(-1)sum_j1{X_j=c} and
A_c=M^(-1)sum_j1{X_(j-2)=a,X_j=c}. Expanding the product weights gives

    d_k q_(k,c)=r_c+A_c+lambda_k(g_c+c_(ab,c)).

Subtracting k=1 from k=2 eliminates r_c,A_c and yields

    c_(ab,c)=d2 q_(2,c)-d1 q_(1,c)-g_c.                  (7)

Thus the small head interface determines the requested joint frequency
through actual weighted averages and both finite-path boundaries. No
normalization constant or empirical table has been supplied for free.

## 4. Finite log coefficients and finite attention evaluator

Let delta=2^(-p). For q=3,2, respectively, form exactly the rational sum
S_q=2 sum_(j=0)^(p-1) [1/((2j+1)q^(2j+1))], then store
L_2=floor(R S_3), L_3=floor(R S_2). Only these integer coefficients,
interpreted divided by R, are retained online. L_3 needs p+1 numerator
bits since log3>1; p denotes fractional precision, not total word size.

Integrating the geometric series 2/(1-y^2) from0 to y proves
log((1+y)/(1-y))=2 sum_(j>=0)y^(2j+1)/(2j+1) for |y|<1.
At y=1/q the tail after p terms is at most
2 y^(2p+1)/((2p+1)(1-y^2))<=2^(-2p). Therefore

    0<=log2-L_2/R<2delta, 0<=log3-L_3/R<2delta.           (8)

A finite offline construction uses common denominator
D_q=q^(2p-1) product_(j=0)^(p-1)(2j+1), sums the integer numerators
2D_q/((2j+1)q^(2j+1)), multiplies by R and divides by D_q. All term
divisions are exact until that final floor. The appendix gives its
operation list and a sufficient8p^2+32-bit word bound, including full
products, so exact rational generation is paid, not an oracle.

Use the finite coefficients L_2/R,L_3/R in Q. Each finite score s=S/R
is a sum of at most two selected coefficients. With ideal score s*,

    0<=s<=s*<=log6<2,   |s-s*|<=4delta.                  (9)

Unscaled attention requires no square-root coefficient. Integer score S
can be formed directly from its one-hot bits. If a scalar score register
is exposed, the exact finite-grid extraction in section6 supplies the
same integer; its work is charged in the per-edge bound.

For each allowed edge evaluate integer terms and weight

    T_0=R,
    T_j=(T_(j-1) S) div (jR), j=1,...,8p,
    W=sum_(j=0)^(8p) T_j.                               (10)

The full product is retained before division; no intermediate rounded
multiplication is substituted. By induction 0<=T_j/R<=s^j/j!, so
1<=W/R<=exp(s)<=exp(s*)<=6. Let e_j=s^j/j!-T_j/R.
Then0<=e_j<=s e_(j-1)/j+delta. An error introduced at step k contributes
to the sum of all later terms by at most
delta sum_(r>=0)2^r/r!<8delta. Consequently the sum of the8p term
errors is <=64p delta. For j>=9,2^j/j!<=2^(-j) (check j=9 and the
successive ratio2/(j+1)<=1/2), hence the tail after8p terms is <=delta.
The derivative of exp on[0,2] is <8; (9) adds at most32delta. Thus

    0<=exp(s*)-W/R<=(64p+33)delta<=100p delta.            (11)

For a row with k>=1 eligible keys, accumulate exactly denominator D=sum W
and, for each bit-valued coordinate, numerator A=sum W*value. There is
no rounding during aggregation. Its returned master numerator is

    H=(Q_A A) div D,      returned scalar H/Q_A.         (12)

The finite and ideal denominator are at least k after scaling by R.
The differences of the scaled numerators and denominators are at most
k*100p delta. Subtracting normalized ratios bounds their difference
by200p delta, since each normalized numerator is in[0,1]. The final
division in (12) has error <1/Q_A. For p>=32,200p<=2^(p/2), as is
true at32 and preserved on incrementing p. From p>=4h+64 it follows
200p delta<=2^(-h). Therefore every one of the19 masters satisfies

    0<=H<=Q_A,  |H/Q_A-ideal coordinate|<=eta=2/Q_A.      (13)

This includes both endpoints0 and1. For singleton bit copies the ratio
and the last quotient are exact. Dependence or shared errors between
heads play no role. The finite evaluator is fixed before any data are
seen and never computes or receives u,t.

## 5. Signed recovery and its deterministic error

Let hats denote finite masters divided by Q_A, all in[0,1]. Selecting
U1,U2,nu_b,alpha_b with exact one-hot/bit muxes preserves the bound eta.
For n_lambda=1+lambda nu_b and v_lambda=1-U/2, both true and finite
v are >=1/2. Subtracting the ratios and using n_lambda<=1+lambda gives

    |hat n/hat v-n/v|<=2lambda eta+2(1+lambda)eta.

Implement their quantized normalizers and dT on integer numerators:

    D_k=[2Q_A(Q_A+lambda_k V)] div (2Q_A-U_k),
    DT=Q_A+alpha_b.                                    (14)

Thus D1/Q_A error<=6eta+zeta, D2/Q_A error<=10eta+zeta,
where zeta=1/Q_A. DT/Q_A error<=eta. The quotient denominator belongs
to[Q_A,2Q_A]; using (14) retains the half-bit algebra exactly.

For each c implement, with all masters below denoting integer numerators,

    Ic=(DT*h0_c div Q_A)-f_c,
    Gc=(DT*h_c div Q_A)-nu_c+rho*J_c-Ic,
    Hc=(D2*q2_c div Q_A)-(D1*q1_c div Q_A)-Gc,
    Ac=min(Q_A,max(0,Hc)).                              (15)

rho*J_c is an exact mux on a bit. All other products are full integer
products followed by one division. Additions and subtractions are exact,
signed until the final clip. For dT h, for example,
|hat dT hat h-dT h|<=|hat dT-dT|*|hat h|+dT*|hat h-h|<=3eta.
Include its one product quotient, subtract nu or f, and get4eta+zeta.
The same argument and d1<=4,d2<=6 prove the complete error table:

| Quantity | Absolute error |
|---|---|
| d1,d2 | 6eta+zeta, 10eta+zeta |
| dT h-nu and dT h0-f | 4eta+zeta each |
| rho J | eta |
| g | 9eta+2zeta |
| d1 q1,d2 q2 | 10eta+2zeta, 16eta+2zeta |
| recovered joint frequency | 35eta+6zeta |

Every entry is a triangle inequality; no stochastic or independent-error
claim is used. Projection onto[0,1] cannot increase distance to a true
joint frequency in that interval. Substituting (13) gives

    |Ac/Q_A-Cc/M|<=76/Q_A.                              (16)

Ranges are valid even for arbitrary closed-grid master inputs: D1/Q_A
is in[1,4], D2/Q_A in[1,6], DT/Q_A in[1,2]. The two terms
DT*h/Q_A-nu and I are in[-1,2] in scaled units; G is in[-3,4].
The difference of the two product terms is in[-4,6], so H is in[-8,9].
A signed guard of[-16Q_A,16Q_A] is sufficient; unsigned subtraction
before clipping would not implement this program. The word list in the
appendix explicitly preserves these signs.

## 6. Closed-grid expansion and exact count snap

For a scalar master H/Q_A first scale exactly by Q_A, obtaining integer
H in[0,2^h]. Starting from A_h=H, for j=h,...,0 use

    bit_j=ReLU(A_j-(2^j-1))-ReLU(A_j-2^j),
    A_(j-1)=A_j-2^j bit_j.                              (17)

Inductively0<=A_j<2^(j+1), so bit_j is exactly0 or1 and the new
remainder lies in[0,2^j). This uses h+1 bits, including H=Q_A.
The same construction at p+1 handles a score numerator S<2R if needed.
On nongrid real inputs it is simply a continuous piecewise-linear map;
no claim of continuous real floor is made. Thresholds and their storage,
scaling and identity wires are charged.

For any A in{0,...,Q_A}, define

    snap(A)=(2M A+Q_A) div (2Q_A).                      (18)

If |A/Q_A-C/M|<1/(2M) for integer C, then
C-1/2<MA/Q_A<C+1/2; adding1/2 and taking the integer quotient yields C.
Since Q_A>=256(N-2)>=256M, (16) gives
76M/Q_A<=76/256<1/2, strictly. Applying (18) to both Ac therefore
returns exactly C0,C1 for every input path, including zeros and endpoint M.
Even without the nominal closeness premise, A in[0,Q_A] gives snap(A)
in[0,M]. Consequently readout guards must allow C0+C1<=2M, even though
the nominal recovered counts satisfy C0+C1<=M.

Multiplication and the positive divisor in (18) are implemented by the
finite bit operations in the appendix. Dividing by2Q_A can alternatively
be a paid shift/routing of bits. This proof uses only the strict radius;
it neither asserts that Q_A>=256(N-2) is necessary nor introduces a
perturbation theorem for arbitrary intermediate registers.

## 7. Exact C2 readout, expanded words and all branches

For N>=6 every snapped count lies in[0,M]. Then d=C0+C1+2<=2M+2,
Z=4d<=8m-8. In row00, a=z1/Z is exactly the clipped add-one next1
estimate and lies in[1/4,3/4]. For Q>=4, (1) is nearest-grid rounding:
J=floor(Qa+1/2), |J/Q-a|<=1/(2Q), and a half-integer tie rounds upwards.
Q/4 and3Q/4 are integers, so Q/4<=J<=3Q/4, including both endpoints.
The output is canonically (Q-J,J)/Q. For Q=4 the intervals are
[1/4,3/8),[3/8,5/8),[5/8,3/4], with output next1 of1/4,1/2,3/4.

In row10 z0/Z=min(3/4,(C0+1)/d); z0,z1 are strictly positive.
The two numbers (Q-1)z_c/Z sum to integer Q-1. Their ceilings sum to
Q-1 orQ, so e in(2) is0 or1, and the final two integers lie in[1,Q-1]
and sum toQ. The residual goes to coordinate1. It also follows that
q_c>=(1-1/Q)z_c/Z. At zero counts both rows have z0=z1=4, so both
readouts are uniform. Q=2 is specified separately as the unique positive
grid vector, as are rows01,11 and N=3,4,5. Thus every nominal output
is strictly positive and has exactly unit sum; no target parameter is used.

The new nearest numerator obeys

    2Q z1+Z <=(3Q/2+1)Z <=2Q(8m-8)<16mQ,               (19)

valid for Q>=2. Its divisor2Z<16m. Row10 numerators are <QZ<8mQ.
Since m<N+2<=2^ell, all these quantities and public2Q fit within
v=b+ell+8 bits. Products physically retain2v bits before a proved
zero-high-bit cast; shifted remainders use v+1 bits. The appendix uses
the still larger total output word O=32v, including coefficients,
signed rails for shared operations, guards and all temporary products.
Output numerators use b+1-bit guarded words, plus the paid public
denominator exponent b or denominator2^b; dyadic scalar decoding is a
separate paid affine operation. p and h have not been changed to depend on b.

The accompanying41-operation straight-line readout computes both interior
and ceiling candidates then multiplexes according to S_N and the public
small-N/Q flag. It has the same integer outputs as the reference code's
lazy branches. Its denominators are positive even for unselected candidates;
Q=2 may give a zero *unselected* nearest candidate, but the emitted vector
is uniform. We charge all41 operations rather than claiming that lazy
execution and a fixed feed-forward DAG have the same active cost.

## 8. Strong sequential baseline and all-path code equivalence

A permitted baseline consumes the same N symbols in order, not a count
table. Keep eight counters T_(i,k,c), a public index and the last two bits.
On arrival j=3,...,m increment exactly the counter for
(X_(j-2),X_(j-1),X_j); at all other positions keep counters unchanged.
Continue consuming through N so the final retained pair is actual S_N.
Select T_(a,b,0),T_(a,b,1) by paid bit muxes and apply exactly(1),(2),
including the same uniform branches, ties, coordinate order and residual.
Each counter is at most M<N+2, so ell bits suffice.

Induction on arrival position proves that the baseline counters equal
the prefix triple counts defined in section1. Sections3–6 prove that
the finite heads recover exactly those same selected counts. Section7
then gives bitwise identical numerator words on every binary path and
every N,b. This proof is stronger than bounded examples; it does not
infer optimized cost dominance from equality of outputs.

The code audit compares the pinned Lead program, a fresh19-master finite
evaluator and the explicit63-operation recovery/41-operation output
interpreter with direct counting. It also audits the source's `multiply`
and `divide` loop invariants. Python's arbitrary-precision integers serve
only as an interpreter: range proofs and the resource appendix supply
the finite machine/circuit bounds. The reference diagnostic metadata,
assertions, Fraction checks and caching bookkeeping are not predictor
outputs; deleting checks that do not affect returned numerators does not
delete a mathematical operation needed to compute them. A real implementation
may store only two generated log coefficients for its fixed N, not an
unbounded cross-N cache.

For the baseline, the appendix gives both sequential-arrival live-state
bounds and a separately enlarged one-shot batch network. In the latter
all2N one-hot input bits are held until consumed, charged on every
intermediate layer. Its width contains2N explicitly. Merely adding2N
static input bits while claiming full network width O(log N) is not used.

## 9. Retained failure witnesses and exact exclusions

These failures concern specified false extensions, not a refutation of
the nominal construction just proved. No old graph record is modified.

1. **Wrong flow endpoint.** For history10001110, N=8,m=4, E_m=00 and
   S_N=10. The prefix triples are100,000, so selected counts are[1,0].
   Replacing E_m by S_N in(5),(15) produces[2,0] after snap. Binding and
   paying the actual query does not license changing the prefix boundary.
2. **Omitted endpoint bit.** A closed h-grid includes numerator2^h.
   At h=1,A=2, a one-bit extraction cannot encode required binary10.
   Formula(17) begins at h, not h-1. Likewise L3 needs p+1 numerator
   bits; fractional precision is not total word width.
3. **Nonstrict symmetric snap radius.** M=1,Q_A=16,A=8 is at distance
   1/2 from true C=0 but(18) returns1. The sufficient nominal error is
   strictly below the half-count radius.
4. **Uncharged re-storage.** M=7,Q_A=16,C=1 has nominal downward uniform
   frequency2/16. Perturbing that real value by-1/10000 and truncating
   back to the grid gives1/16 and snap0. Charging only1/10000 and not
   the storage step wrongly promises recovery from
   7(1/16+1/10000)<1/2. This is a failure of that perturbation model;
   the present theorem is nominal and uses exact declared interfaces.
5. **Bad-event range too small.** If both clipped master frequencies are1,
   both snapped counts are M. The denominator C0+C1+2 is2M+2, not at
   most M+2. With M=1 it is4 rather than3. Guards use the larger range.
   The old8mQ nearest-dividend guard also fails on allowed nonnominal
   counts: N=16,m=8,M=6,Q=4,C0=C1=6 gives Z=56,z1=28 and dividend280,
   exceeding8mQ=256. The corrected16mQ=512 bound covers it.
6. **Swapped output coordinates.** At t=a=1/4,Q=4, correct(3,1)/4 has
   loss0, whereas(1,3)/4 has loss(log3)/2. J in(1) is next1.
7. **Nearest need not minimize KL.** At t=37/100,Q=4, nearest next1 is
   1/4, yet its KL is about.03521294, exceeding the loss about.03419150
   at1/2. We claim the prescribed output, not exact targetwise KL optimization.
8. **Fixed lower clip in row10.** A fixed q0>=tau>0 leaves limiting
   row10 loss at least-log(1-tau) as t=1/2,u decreases to0, while the
   row mass tends to1/3. The program retains only an upper clip there.
9. **Other statistical scope failures remain.** At M=2,row00,
   Pr(C=1|D=1)=(1+t)/2, so random visit counts do not create conditional
   binomial samples. Ordinary pair reversibility fails because
   P(00,01)>0 but P(01,00)=0. Zero output solely on terminal10 can make
   average risk infinite while conditional00 risk remains finite.
   At u=1/8,t=1/4,Q=4 the true row00 distribution has zero representation
   error, so minimax format floors are not pointwise in every t.
   These are preserved C1/C2/Counter scope checks, not new C3 premises.

Internal precision necessity, perturbation reliability, optimized neural
advantage, training guarantees, practical constants and publication novelty
do not follow from this construction. The same-bit baseline is explicitly
inside the allowed information domain. No new literature retrieval is used.

## 10. Evidence status and remaining review gate

The governing Lead checkpoint hash is
`ff29424bef9a5225e3d79c6790804514980ccf6f3f047d55a6d229f9640c6ce8`;
the pinned Lead code hash is
`5eae6f7c009cd5e612c74274117109099b249a54dbdd62a6ee15e3da093662d6`.
Both were checked before derivation. Source002 realization and005 snapping
were read only as provenance; every required path identity, finite-error
bound and snap claim is proved here. No source Fact or review verdict
is inherited. Current statistical C1/C2 are separate from old realization
[Non-scientific operational metadata omitted.]

The attached resource appendix replaces the unverified small-block claim
with concrete operation lists and sufficient functions. These are
deliberately loose upper bounds and a stated compiler, not measured
hardware costs. Independent review of this fixed proof/certificate and
the normal native gateway remain open. No claim of native acceptance,
C4 completion, root acceptance or mother-problem completion is made.
At writing, actual Fact IDs=[] and actual Evidence IDs=[]. Consultation
requests belong in the handoff because only Lead may schedule them.

---

The complete resource appendix follows; its separately pinned copy is
`c3-resource-ledger-v1.md`.

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
