# C3 dependency reconstruction and changed integer guard

Lead, 2026-10-25. Proof checkpoint for obligation
`c82d400c69019a551db29a66e99faec5bfbf281097c5c8ae57075ea5789772fb`.
Not a Fact; Prover must check and submit the complete realization proof.
Sources are source002 Prover, source005 count-snap Counter, source009 Prover,
all under inputs/source-stage2. Their authorship and original failure records
remain intact. No premise below is justified merely by a source native PASS.

## Actual wiring, not an external count input

For N>=6 set m=floor(N/2), M=m-2, n=N+1, n_m=m+1,
h=max(4,ceil log2(256(N-2))), Q_A=2^h,
p=4h+4ceil log2(m+4)+64. Input positions1..N contain two-coordinate one-hot
symbols; the physical query is at N+1 with zero symbol. Four first-layer
zero-score singleton heads form historical lag1/lag2; at query these two
heads read m,m-1 to obtain E_m. Two further paid heads read N,N-1 at query
and self elsewhere to obtain S_N. Every selected position is causal.
The query is formed before routing. Crop to positions1..m and the query;
its buffer address m+1 does not mean it arrived early. Full singleton masks
cost4n^2 bits and crop/address/copy/erase costs are charged.

Write S_N=(a,b), retain E_m separately. For keys j=3..m, i=X_(j-2),
k=X_(j-1), c=X_j, z=1{j=3}, use four heads:

| Head | score | value |
|---|---|---|
| P1 | log2*1{i=a}+log2*1{k=b} | (onehot(c),onehot(i)) |
| P2 | log2*1{i=a}+log3*1{k=b} | (onehot(c),onehot(i)) |
| T | log2*1{i=b} | (onehot(k),z*onehot(k)) |
| U | 0 | (onehot(i),onehot(k),z*onehot(k),z) |

The flag product is ReLU(lag1+z-1). Values are query-independent. QK
dimensions are4,4,2,1; value dimensions4,4,4,7, hence19 statistical masters.
The query never becomes a sample. Other evaluated rows use causal prefixes
with singleton fallback to avoid empty masks. Scores are nonnegative and<2.
After finite attention only these19 numbers, the four one-hots for S_N,E_m,
and paid public metadata survive at query. No later history read is allowed.

## Finite-path algebra to reconstruct, with both boundaries

Let u_ik be the empirical pair mass of source pairs j=3..m, alpha_i=sum_k u_ik,
nu_k=sum_i u_ik, rho=1/M, f_c=rho*1{X_2=c}. Head T gives h_c,h0_c;
U gives alpha,nu,f,rho. Put dT=1+alpha_b, J_c=1{E_m=(b,c)}.
Direct weighted sums show

    dT h_c=nu_c+u_bc,
    dT h0_c=f_c+rho*1{(X_1,X_2)=(b,c)}.

Source pair and successor pair lists telescope at the first and last pair.
Thus g_c=dT h_c-nu_c+rho J_c-(dT h0_c-f_c) equals the empirical mass of
successor pair(b,c). Let U_k be Pk's lag2 coordinate selected by a, and qk_c
its successor output; lambda1=1, lambda2=2. Direct summation gives

    d_k=1+alpha_a+lambda_k nu_b+lambda_k u_ab,
    d_k U_k=2(alpha_a+lambda_k u_ab),
    d_k=(1+lambda_k nu_b)/(1-U_k/2).

Expanding the product kernel gives d_k qk_c=r_c+A_c+lambda_k(g_c+c_ab,c),
where r_c is successor marginal and A_c the lag2=a/successor=c mass.
Subtracting k=1 from k=2 cancels r_c,A_c and yields

    c_ab,c=d2 q2_c-d1 q1_c-g_c=C_ab,c/M.

These identities hold for M=1 and zero row counts. No source-law parameter
enters, and no pair/triple table is supplied to this frontend.

## Finite evaluator and error, without an exact transcendental oracle

Let R=2^p and delta=1/R. For x=2,3 set y=(x-1)/(x+1)=1/3,1/2 and generate
Lx=floor(R*2 sum_{j=0}^{p-1} y^(2j+1)/(2j+1)). Integration of the geometric
series gives the log identity and tail<=2^(-2p), so
0<=log x-Lx/R<2delta. Exact rational generation has common denominator
q^(2p-1) product_{j=0}^{p-1}(2j+1), q=3 or2, of O(p log(p+1)) bits.
Store only these two finite coefficients; generation is paid separately.

For each integer finite score S=Rs, evaluate T0=R,
Tj=floor(T_(j-1)S/(jR)) for j=1..8p, and W=sum_j Tj. All are integer
products and positive-divisor long divisions. Retain full products until
the stated quotient; do not add an extra rounding step. Since 0<=s<=s*<2,
1<=W/R<=exp(s*)<=6. If e_j=s^j/j!-Tj/R, then
e_j<=s e_(j-1)/j+delta. Each introduced error contributes at most8delta
to all subsequent terms. Summing8p terms and the Taylor tail adds at most
(64p+1)delta; |s-s*|<=4delta adds at most32delta. Hence ideal-weight error
<=100p delta. Summing finite weights and bit-valued weighted numerators
exactly over any nonempty row, both denominators are at least its key count.
The normalized-coordinate error is <=200p delta. Final output numerator is
floor(Q_A*A/D), including its own <1/Q_A error. Since p>=4h+64 and
200p<=2^(p/2), each master has error eta<=2/Q_A. Singleton copies are exact.

Rounded masters have numerator0..Q_A and need h+1 bits, including1. Grid
extraction at index j=h..0 uses ReLU(A_j-(2^j-1))-ReLU(A_j-2^j), then
subtracts2^j times the extracted bit. This is exact on the finite integer
register; no continuous real floor is claimed. Signed recovery uses sign
and magnitude bits/two rails and preserves signs until final clip.

With clipped inputs, normalizer denominators lie in[1/2,1]. If master error
is eta and product/quotient error is zeta, subtraction of the normalizer
ratios gives d1 error<=6eta+zeta and d2 error<=10eta+zeta. For dT h-nu and
dT h0-f errors are<=4eta+zeta each; rho J error<=eta. Thus g error<=9eta+2zeta.
Product d1 q1 error<=10eta+2zeta, d2 q2 error<=16eta+2zeta. Final recovered
joint frequency has error<=35eta+6zeta. These use no independence assumption.

For integer masters over Q_A, implement

    Dk=floor(2Q_A(Q_A+lambda_k nu_b)/(2Q_A-U_k)); DT=Q_A+alpha_b;
    Ic=floor(DT*h0_c/Q_A)-f_c;
    Gc=floor(DT*h_c/Q_A)-nu_c+rho*J_c-Ic;
    Hc=floor(D2*q2_c/Q_A)-floor(D1*q1_c/Q_A)-Gc;
    Ac=clip(Hc,0,Q_A).

Here every displayed master in the integer formula denotes its numerator.
Products truncate once, zeta=1/Q_A; additions and signed subtractions are
exact. D1/Q_A in[1,4], D2/Q_A in[1,6], DT/Q_A in[1,2]; Hc/Q_A in[-8,9],
so[-16,16] is safe. Head numerator end point1 and sign guards must not be lost.
Projection does not increase error, hence |Ac/Q_A-Cc/M|<=76/Q_A<1/(2M).
Compute Cc=floor((2M Ac+Q_A)/(2Q_A)) by integer multiplication and bit shift.
Its symmetric strict snap radius gives the exact count, including0 and M.
For arbitrary closed-grid inputs the result remains in[0,M], so guards use
D=C0+C1<=2M even though nominally D<=M. QA is independent of output Q.

The strict radius cannot become non-strict: M=1,QA=16,Ac=8 is a tie and maps
to1, which would fail if the target count were0. This retained source005
failure concerns that modified claim, not nominal snapping under76/QA.

## New readout, guards and complete resource domains to certify

Use the new integer program and first checkpoint for clipping/branch proofs.
Let ell=ceil log2(N+2), v=b+ell+8. After snap release all19 masters,
normalizers, flags,E_m and history; retain only counts, query selector and
public metadata. With d=D+2<=2M+2, Z=4d<=8m and row00 z1<=3Z/4,

    2Q*z1+Z <=12mQ+8m <=16mQ  (Q>=2).

The exact bound is strict since Z<=8m-8; v therefore covers this new
dividend and divisor2Z<=16m. The old8mQ dividend bound is not reused for
this branch. Full multiplication uses2v bits, shifted remainder v+1.
The row10 old dividend remains<8mQ. Uniform branches write Q/2 twice.
Unsigned output words are b+1 bits with paid public denominator2^b;
optional dyadic decoding is a paid affine map. Every valid numerator is1..Q-1.

Ripple add/subtract/compare/mux take O(v) gates, school product/restoring
division O(v^2), with O(v) scratch. The revised block has fewer than64 such
word operations; a conservative certificate to check is G_R,L_R<=20000v^2,
W_R<=64v+32 and I_R<=(64v+32)(20000v^2+2), then factor16 for a serial ReLU
schedule. A full word-op list and analogous finite frontend certificate must
appear in the submitted proof; this checkpoint does not assert checked counts.

The resulting functions to prove, retaining source009's declared domains,
are L=O(p^2+v^2), W=O(p+v), H_total=8,H_layer=4,Dqk<=4, scores[0,2].
Frontend words<=128p, output-block coefficient words<=32v. Phase-shaped
dense slots O(p^4+v^4), neural bits O(p^5+v^5), holds O(p^3+v^3), sparse
addressed code O(p^4+v^4). Masks exactly4n^2+4n_m^2, positions/crop/address
metadata O(n ell+p+b). Rolling activations/scratch O(np^2+v^2), plus selected
stored program/masks for peak total. Finite attention operations
O(n^2(2+p)p^2); generic dense pointwise/QKV operations O(n_m p^6+np^2+v^6).
Offline log generation O(p^3 log^2(p+1)) operations and O(p log(p+1)) scratch;
phase-separated layout generation O(p^5+v^5) operations, O(p^4+v^4) scratch,
plus writing all code, masks and metadata. Reading N,b and computing lengths
uses integer bitlength/doubling, not real-log oracles.

These are hybrid finite-attention bounds: the cost inside the softmax
primitive is charged above but not silently included in its neural-layer count.
For a flattened serial Boolean/ReLU implementation, choose
T_f=C[n^2(2+p)p^2+n_m p^2+v^2+np^2], S_f=C[np^2+v^2],
B_f=C[p+v+log n]. Then depth O(T_f), width O(S_f), holds O(T_f S_f),
dense slots O(T_f S_f^2), dense bits O(T_f S_f^2 B_f), sparse code
O(T_f S_f B_f), dense generic operations O(T_f S_f^2 B_f^2) are safe.
Stored masks/positions are additionally charged. Padding every phase to
global width or expanding shared parameters must be costed separately.

Eight-counter baseline: sequential input arrivals,8 ell-bit counters,
last two symbols and index; updates only j=3..m, then consume the rest to
form S_N. Pay input access,8 triple matches, counter increments and final
row mux. Count work O(N ell), live O(ell); add identical readout O(v^2) active
gates/O(v) scratch and selected program layout. Loop/address-safe executed
count cost O(N ell^2); shared counting code O(ell^2). A neural unrolling of
the counting block has L=O(N ell),W=O(ell),holds O(N ell^2),dense slots
O(N ell^3),bits O(N ell^4),generic operations O(N ell^5), plus readout.
These are **sequential-input block** bounds. A one-shot full-history batch
network must additionally keep all unconsumed input and its cross-layer holds;
it cannot cite W=O(ell) as its full width. Exact frontend count recovery and
identical integer branches imply identical output bits and risks, not optimized
resource dominance. No precision necessity, noise guarantee or neural advantage.

For average target epsilon<=1 the coarse C2 bounds allow N>=12000000/epsilon,
Q dyadic>=6/epsilon. Conditional evaluation allows1+Nu>=2000000/epsilon,
Q>=sqrt(6/epsilon), rounded to a dyadic; the algorithm never receives u.
Substitute these into p,v and the costs, without calling output b internal h.

## Diagnostics and next gate

New code is adapted inside outputs/001-conditional-grid/lead/ only; source
hash/author are in code-provenance-v1.json. New tests check rational nearest
grid independently, Q2/Q4/ties/zero, finite frontend vs eight counters and
the retained wrong-endpoint path10001110. Diagnostic PASS is not a proof.
The environment has python3, not the python alias; the first launch failed
before running code and was retried with python3. No source diagnostic was run.
Fixed full proof plus Counter audit must precede independent Verifier review
and native submission. No final audit has been requested prematurely.
