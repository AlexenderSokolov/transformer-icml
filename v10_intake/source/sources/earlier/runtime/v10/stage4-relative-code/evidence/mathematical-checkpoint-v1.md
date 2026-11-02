# Stage 4 mathematical checkpoint v1

Lead, 2026-10-26. New-project proof assembly; **not an admitted Fact**.
Root `82f3b230a8e39f7ef988c219960127d8a94bee1c31d31ae51a328ab8580a3a29`;
contract `38d15641fecff6dbee957b6e036c052ecb7f07e6354623e800f7a126cf5270ef`.
Definitions are this project's `inputs/STAGE_DEFINITIONS.md`, D1–D8.
All source paths below start at this project's `inputs/source-stage3/`.
Author/version lineage is recorded in `checkpoint-manifest-v1.json`.
The old proof and reviews are immutable provenance, including the wrong
§11 sentence and the main review's admitted omission. Delta controls reuse.

## 1. Exact admission boundary and minimal dependencies

Native state was read before work: this root is OPEN; no component,
Fact, Evidence or acceptance exists here. Native continued research is
RUNNING on this exact root. The available Euler API exposes submission
to an independent gateway, but no cross-project evidence-import operation.
We therefore do **not** submit old Fact IDs as new predecessors. Reuse means
reusing attributed proof text/constructions inside self-contained new
proofs, then obtaining new gateway evidence for the exact new obligations.
No old root or old full classification needs re-audit.

The minimum statistical premise is only the following lemma S, rather
than the whole old C1 minimax classification:

* For the D1 stationary law, with N>=6, m=floor(N/2), M=m-2, clean
  triple counts C from keys3..m and the actual terminal query S_N, let
  a_1=clip_[1/4,3/4]((C_001+1)/(C_000+C_001+2)) on row00;
  a_0=min(3/4,(C_100+1)/(C_100+C_101+2)) on row10; the other rows
  are uniform. For N=3,4,5 use uniform without a prefix frontend.
  Then R_av(a)<=1000000/N and R_00(a)<=160000/(1+Nu), simultaneously,
  uniformly in D1 u,t. The algorithm does not know u,t.

Lemma S is established by the proof ingredients in §2 below, which are
to be included in the new C1 submission, with no separate old-Fact
predecessor. Its source is old Prover `outputs/001-conditional-grid/
prover/c1-proof-v1.md`, §§1–7 only. Old Fact `e418ec34b7dbc4a6` /
Evidence `4857f1b1b5d10ab74a979362e3d0c3068c9634016e4ce6b6a0609ed577eb2eea`
identifies its lineage, not a premise admitted in this project.

The old C2 grid classification is not a needed statistical premise.
We prove its converter's positivity, tie convention and the two pointwise
risk inequalities directly in §3. Its lower bounds are unused.
Old C2 Fact `4f0e99ed26dfeeeb` / Evidence
`a4152a1fc70cbd2d4ece0bea8390fb68c0ed76beb4e11a8d9dd495a8250764ee`
likewise remains provenance.

The minimum finite-program premises P are: the four causal singleton
adapters; the finite log/exp evaluator; the actual signed 63-instruction
MIX recovery; the 41-instruction output; bit primitives with full products
and restoring division; and their principal hybrid dense ledger and
enumerating generator. These are re-established in the new C3/C4 component
using old Prover `c3-proof-v1.md` §§2,4,7 and appendix A–F,I, together
with the specified word program. Its clean statistical/minimax conclusions,
padded layout, flattened layout and sequential baseline are not premises.
Old C3 Fact `a47d648004a9a607` / Evidence
`3e576827ab335e24f661561d9aa89f035a36925f450dd2daf0be3b166ab3cd27`
does not certify the new noisy boundary. Closed-box guards and actual
erasure must be checked anew as part of this component.

This gives two mathematical routes, not a new general plan:
A = S + direct grid/relative-count argument -> new C1;
B = full finite observation-law lower -> new C2; finite P + paid
alternatives + C1/C2 -> new C3/C4 and same-witness comparison.
Acceptance of the combination requires independent review of that complete mathematical statement;
component admission alone does not establish acceptance of the combination.


## 2. Statistical lemma S: explicit sufficient proof interface

Write w=(1-u)/3, r=ut/w and beta=31/32. The D1 pair kernel is

    P=[[1-t,t,0,0],[0,0,1/2,1/2],[r,1-r,0,0],[0,0,1/2,1/2]].

Direct multiplication proves pi P=pi for pi=(u,w,w,w). Its stationary
reverse kernel is P conjugated by exchanging01 and10, not P itself.
P^3 has a common atom01 of mass1/32 and the reverse cube has atom10
of the same mass: the four paths to01 have probabilities
t(1-r)/2,(1-r)/4,(1-r)^2/2,(1-r)/4, all >=1/32. Subtracting that
common atom proves TV contraction by beta every three transitions.

Let g=N-m and d_g=beta^floor(g/3). Reversing the stationary path and
then applying the common earlier-path kernel gives, for every terminal s,

    TV(Law(X_1^m | S_N=s), Law(X_1^m)) <= d_g.

This is a whole-prefix comparison, including counts and E_m. No division
by u, conditional-binomial assertion, or independent terminal query is used.
For stationary-prefix row losses K_00,K_10, the genuine caps are log4
and log max(m,4); hence

    R_00(a)<=K_00+d_g log4,
    R_av(a)<=u K_00+w K_10+d_g log max(m,4).

Here are the deterministic-horizon ingredients closing these K bounds.
For D visits to a row and C chosen successors with probability p,
Z=C-pD is a sum of martingale differences, so
E Z^2=p(1-p)M pi_row. Spaced visits obey the exponential-moment
bound Pr(sum I_j<=Bp/2)<=exp(-Bp/8) whenever the conditional visit
probabilities are >=p. From P^3(x,00)>=3u/32 and P^2(x,10)>=1/8:

    Pr(D_00<Mu/128)<=exp(-Mu/512)                 (M>=6);
    d0=floor(floor((M-1)/2)/16)>=M/128>=1,
    Pr(D_10<d0)<=exp(-M/256)                     (M>=64).

For the row10 successor, use independent row stacks only as a proof
coupling. {D>=d0,C<p d0/2} implies a lower-tail event for the first
d0 stack bits, whose probability is <=exp(-p d0/8). This does not
condition a binomial law on the random D.

The elementary inequality kl(p,q)<=(p-q)^2/[q(1-q)] gives on row00
loss<=12(Z^2+1)/(D+2)^2. Splitting at D=Mu/128 yields
K_00<=50000/(1+Mu): the good contribution times1+Mu is <=49152,
and the bad contribution is <386. Small M uses log4.
On row10, clipping only decreases (p-v)^2/v for v>3/4>p, so
loss<=8(Z^2+1)/[(D+2)(C+1)]. Split into
D>=d0,C>=p d0/2; D>=d0,C<p d0/2; and D<d0. Their contributions
are <=263168/M,13824/M,65536/M, respectively. For the middle event
use loss<=p log_+(p/q)+4q, q>=1/(M+2), q<=p/2+1/d0, and
[y log_+(256y)+2y+4]exp(-y/8)<=108 with y=p d0.
Thus K_10<=400000/(M+1); M<64 is covered by log65.

Finally M+1>=N/4, u/(1+Mu)<=1/(M+1), w<1/3, and
d_g<=2exp(-N/192). The average statistical contribution is <800000/N,
and the bridge is <=73728/N. Also 1+Nu<=3(1+Mu), and the conditional
bridge times1+Nu is <75; 150000+75<160000. These prove S. For
N=3,4,5 the real uniform branch has loss<=log2 and the two bounds
hold directly. No six-observation statistical input is constructed.

## 3. C1 relative count, KL and exact output closure

For N>=6 the paid triple features and zero-score head give
j_c=floor(A C_c/M) exactly since W(0)=R. The eleven padding integers
are zero and locked. On any D3 returned input put
C'_c=floor((2M j'_c+A)/(2A)). Then 0<=C'_c<=M. If C_c=0,
j_c=j'_c=C'_c=0. Otherwise M/A<=1/256 and

    |C'-C|<=eta C+129/256.

If C'!=C, integrality forces eta C>=127/256; hence
|C'-C|<=(256/127)eta C<3eta C. The same conclusion holds when
C'=C. This is pathwise for correlated maps and, by conditioning,
randomized independent maps. Clean C is a comparison variable only.

Set epsilon=3eta. Add-one numerators and their sum change by factors
in[1-epsilon,1+epsilon]. Thus each coordinate ratio of the noisy
pre-grid r to clean a belongs to[L,1/L], L=(1-epsilon)/(1+epsilon).
Common interval clipping contracts ratios toward1; apply it to the
Bernoulli coordinate and its complement separately. All coordinates
remain positive, including row10's rare successor.

For any target v, Jensen on its positive support proves

    KL(v||r)-2KL(v||a)
      <=log(sum a_i^2/r_i)
      =log(1+sum (a_i-r_i)^2/r_i)
      <=4epsilon^2(1+epsilon)/(1-epsilon)^3<=48eta^2.

The last numerical inequality holds for eta<=1/64. This direct proof
does not need a new external theorem or a fault-independence assumption.

Take D=C'_0+C'_1+2<=2M+2 and Z=4D. Row00 clips z1 to[D,3D]
and uses J=floor((2Qz1+Z)/(2Z)). For dyadic Q>=4 it is half-up
nearest rounding inside[Q/4,3Q/4], so both output coordinates are
positive. For row10 z0=min(3D,4(C'_0+1)), z1=Z-z0 are positive;
k_i=ceil((Q-1)z_i/Z) have sum Q or Q-1. The residual e=Q-k0-k1
is0 or1 and is added to coordinate1. Outputs sum exactly to Q and
have numerators in[1,Q-1]. Zero counts and ties are included. Q2,
rows01/11 and N<6 are explicitly uniform. The Q4 row00 thresholds
are3/8 and5/8, with equality rounded up.

The full snapped numerator is <=A(2M+1); 2A has h+2 bits.
For closed boxes, not merely clean images,

    Z<=8m-8, 2Qz1+Z<16mQ, 2Z<16m,
    (Q-1)z_i+Z-1<QZ<8mQ.

Retain full products and shifted remainders before casts. These fit
B=128p and O=32(b+ell+8). The emitted format is two guarded (b+1)-bit
numerators and the literal Q in (b+1)bits: **3(b+1)** bits.

For row00, using kl(t,x)<=16(t-x)^2/3 on the clipped interval and
(t-r1)^2<=kl(t,r1)/2 gives

    KL(p00||grid(r))<=(32/3)KL(p00||a)+256eta^2+8/(3Q^2).

For row10 grid(r)_i>=(1-1/Q)r_i, so loss is at most
2KL(p10||a)+48eta^2-log(1-1/Q), with the last term<=2/Q.
Rows01/11 have zero loss. Apply S, using32/3 as a common multiplier:

    R_av<=12000000/N+256eta^2+3/Q,
    R_00<=1800000/(1+Nu)+256eta^2+3/Q^2.

For Q2, uniform loss<=log2<3/4=3/Q^2. For N=3,4,5 the statistical
constants alone dominate log2. These are one common unknown-u,t
program's two bounds for every allowed map; no fitted parameter enters it.

## 4. C2 full finite observation-law interface

This component must submit the full proof, not a population alias.
Here is the load-bearing chain checked against source Prover §§2,4–7.
Let N=2^L, u=2^(-d-16), Mu^2>=2^40. Then L>=2d+74,
h=L+8, A=256N, p=8L+96, K=A/M=512+1024/M, and
100p/2^p<=u/1000, 1024/M<=u/1000. The finite evaluator gives
1<=W/R<=exp(s*)<=6 with error<=100p/2^p. Each integer coordinate
has normalized error<=2/A from its **empirical** ideal weighted ratio.

For the actual empirical triple vector F and its stationary mean
mu_t=(u(1-t),ut,w/2,w/2,ut,w-ut,w/2,w/2), set
G_t={max|F_c-mu_tc|<=u/1000}. Against the public reference
F0=(0,0,1/6,1/6,0,1/3,1/6,1/6), ||F-F0||_1<4u on G_t.
The fourteen query00 bulk ratios at F0 are

    z=(3/10,7/10,2/5,3/5,1/4,3/4,1/3,2/3,
       1/4,3/4,1/3,2/3,1/3,2/3).

Define a single public map Phi_* on every closed19-word/valid-control
input: if S_N=00, replace bulk coordinate j_i by floor(Az_i) exactly
when its relative-integer guard permits; otherwise retain it. Retain
all five small slots and the controls in all cases. This is globally
admissible by construction and depends on no t or decoder.
On G_t each bulk replacement is permitted since
|j_i-floor(Az_i)|<=48uA+3<=eta A/8-1<=floor(eta j_i).

The small slots remain informative. Their actual finite formulas use
D_T=1+(W(L2)/R-1)alpha0. On G_t,
4/3+.66u<D_T<4/3+.671u. Hence
383<K/D_T<384 and 767<K(W(L2)/R)/D_T<768. Exactly,

    rho=512, (f0,f1)=512 e_X2,
    (h00,h01)=383 e_X2 if X1=1; =767 e_X2 if X1=0.

Thus the complete corrupted observation on G_t is T(S2,E_m), with
terminal control00, not a constant19-vector. Values384/768 would be
incorrect. All public metadata and eight protected bits remain included.

The common-atom mixing proof bounds every triple frequency variance
by193/M<=200/M, including overlapping triples. Chebyshev over eight
coordinates gives Pr(G_t^c)<=1600000000/(Mu^2)<1/32. The reverse
whole-prefix bridge costs d_(N-m)<1/32, and
TV(Law(S2,E_m),pi tensor pi)<=d_M<1/32. Therefore the actual
conditional full-code law L_t obeys

    TV(L_t,T_*(pi tensor pi))<3/32,
    TV(L_1/4,L_3/4)<3/16.

The common comparison law includes the initial pair and E_m, and pi
is the same for both witnesses. No independence of G_t and endpoints
has been asserted. Decoder randomization is a common Markov kernel,
so it contracts TV. Threshold the output next-one probability at1/2.
Every mistaken test has KL>=1/8. The sum of its two error probabilities
is >=1-TV, giving max_t R_00>(1-3/16)/16=13/256>=3/64.
Choose that conditional witness t_*; on that **same** source,
R_av>=Pr(S_N=00)R_00=u R_00>=3u/64.

## 5. Complete finite common domain and same-map comparison

For each integer d>=32 fix eta=2^-d, N=2^(2d+74), b=2d,
Q=2^(2d), u=2^(-d-16). Exactly,

    M=2^(2d+73)-2,
    Mu^2=2^41-2^(-2d-31)>2^40,
    Nu=2^(d+58), h=2d+82, p=16d+688.

Thus this one finite tuple lies in the domains of C1, C2 and D6.
Let Phi_* be the map in §4. Its guard is defined on the whole common
19-word/control box, so the identical function is lawful on JOINT too.
In particular a nonzero replacement of JOINT's padding zero is rejected.
Apply C2 to the actual 63-word MIX readout followed by the shared output;
choose its conditional witness t_*. C1 applies to JOINT at that same
t_* and Phi_*; it does not require equal returned encodings.

Substitution into the full finite expressions, not merely the noise terms,
gives

    U_av=(12000000*2^-74+259)eta^2<260eta^2,
    260eta^2/(u/64)=260*2^(22-d)<=260/1024<1;
    U_00<2^(-d-37)+2^(8-2d)+3*2^(-4d)
         <=2^-69+2^-56+3*2^-128<1/64.

The first strict inequality uses12000000<2^74; the second row uses
1800000<2^21. Hence JOINT has R_av<u/64 and R_00<1/64,
while this same MIX witness has R_av>=3u/64 and R_00>=3/64.
Subtracting gives strict gaps >u/32 and >1/32.

The mandatory erratum follows without changing any parameter:

    1800000/(1+Nu)=(1800000/2^58)*eta/(1+eta/2^58).

This positive statistical term is Theta(eta); the displayed conditional
total upper expression is Theta(eta), its noise term O(eta^2), and the
average expression O(eta^2). None is a matching actual-risk assertion.
Old §11's both-quadratic statement is wrong; finite formula10.4 survives.

## 6. Constructive resource composition to be admitted with C3/C4

The actual MIX program is the D4 fixed63-word recovery, not a constant
decoder. On arbitrary closed inputs 0<=U_i<=A, all denominators
2A-U_i>=A. Normalizer numerators are <=6A^2; signed intermediate
guard[-16A,16A] is retained. MAX(H,0) followed by MIN(...,A) precedes
count snapping, yielding each count in[0,M]. JOINT uses protected query
selection then the18-word selection/snap construction. Both use the
41-word output just proved, including the all-box16mQ guard.

For all N>=6,b>=1,d>=6 the ledger is **exactly** Bstar in D6. Its
monotone composition must be justified with explicit primitive costs,
not by declaring the existence of an envelope. The following algebra
identifies the required comparisons against the attributed source ledgers:

    E_M=(256p+512)n^2+1024n,
    E_J=512n^2+4096nB+1024(h+1), E_*=E_M+E_J;
    G_F uses63>=18 with common extraction/sign/copy reserve;
    G_O uses41 plus64(b+1) guarded output operations;
    P_*=128+4, M_*=4n^2+4n_m^2>=4n^2+n_m^2;
    Z_*=Z_M+Z_J, a_*>=a_M,a_J.

Both use B=128p,O=32(b+ell+8), W_F=1024B,W_O=1024O. Bit
primitives have explicit ripple/shift-add/restoring constructions with
<=g(w)=1024w^2 steps and <=32w+32 scratch; full2w products and
(w+1)-bit shifted remainders are retained. Serial ReLU simulation costs
<=16G+32 layers with paid identity holds. Dense zero coefficients are
stored. This is the principal extracted-query one-shot batch hybrid;
post-extraction recovery is on the query. The n factor in T_run is a
work overcharge, not all-token/all-phase state retention.

The cut schedule copies only19 quantized words and eight controls into
a fresh fixed port bank, zeros/releases all other data-bearing input,
lag, feature, head, accumulator and scratch banks, permits external
overwrite, then loads recovery solely from the returned bank. Four
COPY/CONST/phase layers fit P_*. Actual clearing work also fits:
four batch banks contain4096nB^2 bits, whereas the additional reserve
4096nB*g(B) exceeds this by1024B. The1024(h+1)g(B) term covers
port serialization/readback. Phi's arbitrary computation is external,
but its interface and the loss of all clean ancestors are charged.

With common physical domains and larger nonnegative arguments, D_*,
P_bits,I_*,K_*,U_*,W_run and T_run in D6 dominate both ledgers
componentwise. In particular K_* includes both-width libraries and
256(p+1)V_*^2, dominating both source loop/code allowances.
Peak_run=U_*+W_run, including batch residency, code, masks and metadata.
The exact rational log generator uses B_log=8p^2+32 and
T_log=(32p+64)g(B_log); the enumerating offline compiler charges all
coefficients, identities, zeros, masks, addresses and output fields.
The D6 larger A_gen and U_*+L_* then dominate both generator tuples,
including peak_gen=U_*+W_gen. Each inequality must accompany the
corresponding actual schedule in the new C3/C4 submission.

For N=3,4,5 instantiate no cut, frontend, fake E_m or statistics. Read
the actual N symbols through the paid interface, then write guarded
numerators Q/2,Q/2 and literal Q. Public input/output and initialization
costs fit the N=6 envelope: there are fewer input slots, no statistical
or recovery work, and the same b-dependent output block/words. This
is padding of a cost bound, not padding of the stochastic experiment.

## 7. Paid strong alternatives and bounded primary scope

A public rational gain g=M/A applied to local triple values gives
the exact uniform average C/A, hence j=floor(A*C/A)=C. The finite
implementation can accumulate the original bit indicators exactly and
use the identity to avoid an intermediate rational rounding; it must
charge those accumulations and conversion. This is an encoder change,
not a decoder of FULL19.

Let kappa=min(d,h). Every integer0<=j<2^kappa has eta j<1 and
is locked. With ell_C=ceil(log2(M+1)), concatenate the eight exact
ell_C-bit counts and split into at most19 kappa-bit blocks whenever
8ell_C<=19kappa. Padding gives legal words below2^kappa<=A.
For our comparison schedule, ell_C=2d+73 and kappa=d, so the
condition is16d+584<=19d, holding exactly for integers d>=195.

A precomputed compact next-one grid numerator is in1..Q-1 and uses
b bits. The same packing works if b<=19kappa, in particular b=2d
on the schedule. Computing the output **before** the cut and retaining
its packed bits changes the encoder. After unpacking, pay the subtraction
Q-J and writes of two guarded numerators and literal Q; compact b bits
must not replace the final3(b+1)-bit port accounting.

These alternatives pay acquisition, bindings, features/counting, full-word
conversion and packing, port copies/clears, unpacking, and output. One
sufficient charge for an R-bit packed payload is a public serial bit
copy/shift/mask program with O(R+19kappa) such bit operations, each
expanded via the stated primitives; the new component must give explicit
finite bounds, not claim they inherit Bstar for free. They do not need
to be excluded or prove superiority to refute a universal-encoder
extrapolation. Correlated D3 errors preclude an independence-based
repetition argument.

Keep only the three pinned primary mappings in the source Counter map:
Higham1993 (1.2),(2.3)–(2.5),(3.6) for operationwise relative error and
cancellation context; Blanchard–Higham–Higham fixed2020 manuscript,
Algorithm3.1/Theorem3.3/(3.6), for arithmetic normalization on fixed inputs;
van Erven–Harremoes arXiv1206.2459v2 (6)–(7), Theorem30/(52)–(53),
for the classical order2/chi-square KL bridge. None supplies our integer
channel, statistical source law, complete bit-cost certificate or novelty.
The three PDFs/texts are already local; no new primary search is needed.
No Dot absolute cube,5/4 or periodic log-history theorem is a dependency.

## 8. Remaining gates and handoff semantics

This checkpoint supplies a substantive proof interface and the complete
same-source/same-map finite substitution. It does not turn source reviews
or proofs into Facts. Next: fixed self-contained C1; fixed full-code C2;
The remaining scientific work at this checkpoint was a fixed C3/C4 proof with finite primitives and explicit alternative costs, followed by independent review of that exact version.





Accepted scope, the erratum, evidence and unresolved T1–T3 questions remain distinct. A prepared scientific document does not establish later review or acceptance, and this checkpoint does not claim completion of the broader problem.





