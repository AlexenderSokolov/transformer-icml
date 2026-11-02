# C2: joint history and positive-output-grid classification, repaired candidate v2

Prover, 2026-10-25. Exact obligation:
`8b179af3ef2fe36eca7503ff37e9baca6ba118d546cf884db6ad7e4da0d0b6f8`.
This proof uses current D1–D4 and the admitted C1 Fact
`e418ec34b7dbc4a6`, native evidence
`4857f1b1b5d10ab74a979362e3d0c3068c9634016e4ce6b6a0609ed577eb2eea`.
That is its sole native predecessor; its exact scope is used below.
No source009 Fact, previous discussion verdict or C3 theorem is a premise.
Version v1 was submitted unchanged and rejected for one local output-cost
gap (failure `b97ba0738f1848747bd400c3e74405482a403fe463232e79f62fa7068938d708`).
Version v2 adds section2a and updates only admission/dependency prose.
Its statistical and representation arguments are unchanged. This v2 is
an unsubmitted repair candidate, awaiting fixed-version review.

## 1. Definitions and precise finite inequalities

The binary D1 law has parameters 0<u<1/4 and 1/4<=t<=3/4, with
w=(1-u)/3, r=ut/w. Its pair distribution in order (00,01,10,11) is
(u,w,w,w); the next-1 probabilities are (t,1/2,1-r,1/2). The observation
is X_1^N, N>=3, with its actual terminal pair S_N. Natural-log risks are

    R_N(u,t;q)=E KL(p(.|S_N)||q(X_1^N)),
    R_N,00(u,t;q)=E[KL(p(.|00)||q(X_1^N)) | S_N=00].

Let Q=2^b, b>=1 integer. The positive binary Q-grid is

    Delta_Q^+ = {(j/Q,(Q-j)/Q): j=1,...,Q-1},

in canonical coordinate order (next0,next1). M_N,Q and C_N,Q(u) are
the infimum over grid-valued full-history predictors, allowing
source-independent private randomization, of the supremum average risk
over (u,t), and conditional00 risk over t at fixed u, respectively.
The latter comparator may know u. Our one attaining family does not.

The conclusions are the following simultaneous finite inequalities:

    max{3/[16384(N+6)], delta_Q/3}
       <= M_N,Q <= 6000000/N+3/Q,                        (C2.1)

    max{3/[16384(1+(N-2)u)], 1/(2Q^2)}
       <= C_N,Q(u) <=1000000/(1+Nu)+3/Q^2,               (C2.2)

where delta_Q=-log(1-1/Q). More strongly, the two upper bounds hold
pointwise in (u,t) for the same parameter-independent program below.
Since all its outputs are positive grid vectors, both risks are also
at most log Q. These are output-format conclusions, not lower bounds on
internal precision, depth, architecture or online arithmetic.

The exact statistical premise from the C1 companion is that the
unquantized branch program a_N there obeys, for every allowed N,u,t,

    R_N(a_N)<=1000000/N,   R_N,00(a_N)<=160000/(1+Nu),

and that the unrestricted full-history minimax lower bounds are
3/[16384(N+6)] and 3/[16384(1+(N-2)u)], including randomized comparators
and known-u conditional comparison. Nothing else is imported.

## 2. One common exact integer branch program

If N=3,4,5, return (1/2,1/2). If Q=2, return (1/2,1/2) for every N.
These two branches require no statistical estimate. Otherwise N>=6,Q>=4:
use m=floor(N/2), M=m-2, triples only at 3,...,m, and actual query S_N.
If S_N is01 or11 return (1/2,1/2). For the selected row let C0,C1 be
its two successor counts, D=C0+C1, d=D+2. These are nonnegative integers;
in particular d>=2. Define positive integers in canonical order as follows:

    row00: z1=min(3d,max(d,4(C1+1))), z0=4d-z1;
    row10: z0=min(3d,4(C0+1)),        z1=4d-z0.

In both cases Z=z0+z1=4d>0. For row00, d<=z1<=3d and d<=z0<=3d,
so a=z1/Z belongs to [1/4,3/4] and equals the C1 clipped next-1 estimate.
For row10, 0<z0<=3d and z1>=d>0; z0/Z equals the C1 upper-clipped
next-0 estimate. This recovers precisely the two unquantized branches,
including all possible zero counts.

**Row00 nearest grid.** Compute by integer Euclidean division the
quotient J and remainder of 2Qz1+Z divided by 2Z. Return

    (q0,q1)=(Q-J,J)/Q,
    J=floor((2Qz1+Z)/(2Z))=floor(Qa+1/2).                (C2.3)

J is the **next-1 numerator**. Reversing the displayed coordinates
would implement the wrong predictor. Integer quotient/remainder is the
actual rule; floor in the identity only explains its value.

**Row10 positive ceiling/residual.** Put A=Q-1. Compute

    k0=(A z0+Z-1) div Z,   k1=(A z1+Z-1) div Z;
    e=Q-k0-k1;
    (j0,j1)=(k0,k1+e),    (q0,q1)=(j0,j1)/Q.             (C2.4)

Here div denotes integer Euclidean quotient. Thus k_c=ceil(A z_c/Z);
the residual always goes to coordinate1. This convention agrees with
canonical next0/next1 order, irrespective of which probability was estimated.

All arithmetic consists of finite integer additions, comparisons, products
and Euclidean divisions with positive denominators. For example restoring
division scans the dividend bits from high to low, shifts the remainder,
compares it with the divisor, subtracts when necessary and emits a quotient
bit; induction leaves remainder in [0,divisor). Finite input integers and
public N,Q give finite loop bounds. This is not a real floor oracle.
The local output/bit costs are proved in section2a. Physical recovery of
these counts and the full architecture ledger remain C3's separate task.

## 2a. Local converter, output encoding and finite bit costs (v2 repair)

This lemma concerns the finite function of the selected exact counts and
the two actual terminal bits specified in section2. It charges that local
function and its output. It neither supplies those counts for free to the
complete predictor nor claims a causal frontend: producing these inputs
from the history and all network/mask/attention costs remain C3. In
constant branches the converter does not request counts. No C3 theorem
is a predecessor of this lemma.

Fix public N>=3 and b>=1, Q=2^b. Write
ell=ceil(log2(N+1)) and K=b+ell+6. These are public word-layout constants,
not real-number operations executed on observed data. All main registers
are unsigned K-bit binary words, with leading zeroes. A second K-bit
scratch word can hold a full product if a generic multiplier is used.

The output port emits the next-1 numerator j1 in **exactly b bits**, most
significant bit first, with leading zeroes when needed. Its interpretation
is the canonical vector ((Q-j1)/Q,j1/Q); 1<=j1<=Q-1 guarantees this
encoding fits. The denominator Q and layout b are public port parameters.
The port therefore emits no denominator and no second numerator in this
convention. The decoder obtains the next-0 numerator by subtraction in
b+1 bits, with at most 16(b+1) elementary bit reads/writes/Boolean
operations using a borrow chain. Both numerators fit in b bits.

If an application instead emits both numerators, its output is exactly
2b bits, and includes that subtraction and b additional bit writes. If it
also emits the literal binary denominator, the denominator is the b+1
bit string 1 followed by b zeroes: total output is exactly 3b+1 bits
and an additional b+1 writes. Two explicitly emitted dyadic scalars
0.(b fractional bits) use 2b fractional bits, with their fixed punctuation
and radix convention specified by the port. No variable-length,
self-delimiting header is asserted to be free: these counts are for the
declared public fixed-width interfaces. A different wire format must
charge its own header.

For a nonconstant branch, D=C0+C1<=M=m-2 and d=D+2<=m, so
Z=4d<=4m and 0<zc<Z. The nearest dividend and denominator obey

    2Qz1+Z < 8mQ+4m <= 9mQ <16mQ,   2Z<=8m,

where Q>=4. The ceiling dividends satisfy
(Q-1)zc+Z-1<QZ<=4mQ and their denominator is Z. In the nearest
branch Qz1, its doubled value, and the subsequent added value are
nonnegative increasing partial products/sums; all have the same
16mQ bound. Since m<=N/2 and N<2^ell, 16mQ<=8NQ<2^(b+ell+3).
Thus the positive operands, dividends and accumulated products fit
strictly within K bits. A restoring-division remainder is less than its
divisor after each iteration, and less than twice the divisor after a
shift and next-bit insertion; this temporary value also fits in K bits.
The row10 residual is computed as Q-(k0+k1), whose nonnegativity follows
from section3. No signed underflow is used. Q itself needs b+1 bits and
also fits. These bounds include zero counts and both clipping endpoints;
they do not use an internal attention precision Q_A.

Here is an explicit word-operation inventory. Multiplication by2 or4
means a fixed zero-fill shift. A min/max means one comparison followed
by a select. Each DIV returns quotient and remainder by the loop below.

    Normalization (row00, 10 word operations):
      D=C0+C1; d=D+2; Z=d<<2; h=d<<1; U=h+d;
      v=C1+1; V=v<<2; W=max(d,V); z1=min(U,W); z0=Z-z1.
    Normalization (row10, 9 word operations):
      D=C0+C1; d=D+2; Z=d<<2; h=d<<1; U=h+d;
      v=C0+1; V=v<<2; z0=min(U,V); z1=Z-z0.
    Nearest row00 (6 word operations):
      p=Q*z1; h=p<<1; a=h+Z; d2=Z<<1;
      (J,rho)=DIV(a,d2); j0=Q-J; j1 aliases J.
    Ceil/residual row10 (11 word operations):
      A=Q-1; h=Z-1; p0=A*z0; p1=A*z1;
      a0=p0+h; a1=p1+h;
      (k0,rho0)=DIV(a0,Z); (k1,rho1)=DIV(a1,Z);
      h2=k0+k1; e=Q-h2; j1=k1+e; j0 aliases k0.

The branch controller compares N with6, compares b with1, computes
whether the two-bit row is00 or10, and takes the appropriate uniform
or active branch. At most 12 comparisons/Boolean flags/selects suffice:
two integer comparisons, at most four bit negations/equalities, two
ANDs, two ORs and two branch selects. Uniform output constructs
j1=2^(b-1), the b-bit string 1 followed by b-1 zeroes; its numerator
is Q/2 for every allowed branch, including b=1. No empty division
is executed. At most eight further word copies/selects route the
chosen output pair and scratch values. There are at most16 K-bit
input/constant loads or constant-word initializations (counts if
needed, N,b,Q,0,1,2,6, and branch flags/scratch zeroes). Even charging
both normalization/conversion branch capacities, we need at most

    10+9+6+11+12+8+16=72 word operations.

A completely specified bit implementation uses ripple-carry addition,
borrow subtraction, high-to-low comparison, and bitwise selection.
Each has at most 32K elementary bit reads/writes/Boolean operations
before address/control costs; min or max is charged as at most64K.
Shifts and copies take at most2K such operations, and constants at
most K writes. Schoolbook multiplication executes K rounds:
form the K shifted partial-product bits and add into a 2K-bit
accumulator with a ripple adder. Per round at most 80K elementary
operations suffice (K ANDs, at most2K writes/copies, and at most
32*2K adder operations, with spare operations for the carry). Thus
the whole product uses at most80K^2 such operations.

DIV(a,d) initializes quotient and remainder to zero, then scans
exactly K dividend bits from high to low. Each round shifts the
remainder and inserts the next bit, compares with d, subtracts d
when necessary, selects the resulting remainder, and writes one
quotient bit. The comparison, subtraction, select and shift require
at most128K elementary operations per round. Its invariant is that
the scanned dividend prefix equals d times the partial quotient
plus the stored remainder in [0,d). Induction proves the returned
quotient and remainder exactly, including tie dividends and exact
divisibility. Total at most128K^2 elementary operations.

For a conservative sequential bit-operation model, also charge
address construction and control. Use fixed arrays for at most
128 K-bit registers including scratch, loop indices and constants;
they occupy at most128K bits. K>=9, so an address and loop counter
fit in K bits: ceil(log2(128K))<=K for K>=11, and for K=9,10 the
entire same array can instead use at most2K address bits. Uniformly
use 2K-bit addresses. For every elementary operation, reserving
128K extra elementary bit operations pays for forming/advancing
these addresses, a counter increment, a comparison and branch
control with ripple operations; fixed shifts have known addresses.
Consequently each word operation above costs at most
32768K^3 bit operations, including this conservative overhead.
For 72 operations, initialization/erasure of the 128-word workspace,
and any of the explicit output ports above, the sufficient local
online bound is

    T_convert(N,b) <= 3000000 K^3 bit operations,
    S_convert(N,b) <= 256K bits of live working storage.

The memory bound includes the at most128 K-bit data registers and
room for 2K-bit addressing/control; the fixed program is constant
length with bounded loops, rather than an unrolled K-dependent
instruction tape. Public parameter/constant storage is included in
the 16 charged loads and the stated workspace. Erasing all scratch
requires at most128K writes; transmitting at most3b+1 output bits
and the optional subtraction is covered by the numerical slack.
These costs apply unchanged to zero counts, Q=2, Q=4, N=3,4,5,
uniform rows, half-up ties and row10 residual1. The uniform-only
branches in fact need just initialization and O(b) output writes.

This is an explicit sufficient cost bound, not an optimal cost claim or
an architecture theorem. It closes the local D3 output encoding and D4
finite conversion cost statements. The full history-to-count frontend,
working state of the observed history, and architecture-specific masks,
positions, routing and holds must still be charged in C3.

## 3. Positivity, exact simplex, ties and smallest grids

For (C2.3), the intervals [k-1/2,k+1/2) prove |J-Qa|<=1/2. At an exact
tie Qa=k+1/2 the quotient is k+1, so ties go upwards. Since Q is dyadic
and Q>=4, Q/4 and 3Q/4 are integers. Monotonicity gives

    Q/4<=J<=3Q/4,    |q1-a|<=1/(2Q).                     (C2.5)

Therefore both output coordinates are positive and sum exactly to one.
Both clipped endpoints a=1/4 and3/4 are fixed. For Q=4 the map is

    [1/4,3/8) ->1/4,
    [3/8,5/8) ->1/2,
    [5/8,3/4] ->3/4,

with both ties assigned upwards. For Q=2 the separately specified uniform
branch is the unique positive-grid output and requires no interior rule.

For (C2.4), x_c=A z_c/Z are strictly positive and x0+x1=A is an integer.
Either both are integers or both have positive fractional parts adding
to one. Their ceiling sum is respectively A or A+1=Q. Hence e is0 or1;
both k_c are at least1, and j0+j1=Q with j0,j1 in [1,Q-1]. In addition,

    q_c>= (1-1/Q) z_c/Z, c=0,1.                          (C2.6)

This proof also validates the converter at Q=2 should it be called;
the specified common program uses the simpler uniform branch there.

If D=0 then C0=C1=0 and d=2; both integer pairs are (4,4). Row00 has
a=1/2 and J=Q/2. In row10, Q is even, so k0=k1=ceil((Q-1)/2)=Q/2,
e=0, also giving uniform output. Thus zero visits to a selected row are
fully covered. At Q=4 row10's proof is unchanged and gives one of the
three positive vectors, always with the residual to coordinate1.
Rows01,11 and all N<6 have exactly representable uniform output for
every allowed Q. Every history, branch and tie has now been specified.

## 4. Pointwise rounding inequalities

For Bernoulli p,q, the elementary bounds proved in C1 section2 are

    2(p-q)^2 <= kl(p,q) <= (p-q)^2/[q(1-q)].

In row00, t,a,q1 are all in [1/4,3/4]. By (C2.5),

    kl(t,q1) <=(16/3)(t-q1)^2
      <=(32/3)(t-a)^2+(32/3)(a-q1)^2
      <=(16/3)kl(t,a)+8/(3Q^2).                          (C2.7)

This is a pointwise inequality on each observed history. It does not
approximate the joint law by independence, square a TV bound, or make
any concentration assertion about random visits. Conditional expectation
given actual S_N=00 is therefore legitimate.

For row10 let v=(z0,z1)/Z. Equation (C2.6) gives, for every target
probability vector p and every history,

    KL(p||q)<=KL(p||v)+delta_Q.                          (C2.8)

Indeed log(v_c/q_c)<=delta_Q for each coordinate; weighting and summing
proves the claim. The statement requires no knowledge of the target.
Finally

    1/Q<=delta_Q<=1/(Q-1)<=2/Q,                          (C2.9)

as follows by integrating 1/(1-x) from0 to1/Q and bounding the integrand
between1 and1/(1-1/Q).

## 5. Conditional and average upper bounds for all N,Q

For N>=6,Q>=4, (C2.7) and the C1 actual-terminal conditional bound give

    R_N,00(q)<= (2560000/3)/(1+Nu)+8/(3Q^2)
              <=1000000/(1+Nu)+3/Q^2.                   (C2.10)

Write the old row risks as R_N,s(a_N). The two constant rows have zero
loss. Weighting (C2.7),(C2.8) by the stationary actual terminal masses
u,w and using nonnegativity of old row losses gives

    R_N(q)
      <=(16/3)u R_N,00(a_N)+w R_N,10(a_N)
          +w delta_Q+8u/(3Q^2)
      <=(16/3)R_N(a_N)+delta_Q+2/(3Q^2)
      <=6000000/N+3/Q.                                  (C2.11)

Here 16/3<6, u<1/4, w<1, and
2/Q+2/(3Q^2)<=3/Q for Q>=2. The two upper conclusions hold for the
same estimator, not a choice depending on which risk is evaluated.

If Q=2, uniform prediction has average binary loss <=log2<3/Q.
On row00 the chi-square bound at1/2 gives
kl(t,1/2)<=4(t-1/2)^2<=1/4<3/Q^2. This proves both upper conclusions
for every N when Q=2. If N=3,4,5 and Q>=4, the uniform average loss is
<=log2<6000000/N; its conditional loss is <=1/4 and
1+Nu<9/4, so it is also <=1000000/(1+Nu). This covers all small-N
branches separately from the M>=1 prefix proof.

For every branch q_c>=1/Q, so KL(p||q)<=log Q pointwise. This supplies
the optional log Q cap without affecting the sharper statistical/format
sum bounds. In particular no spurious log Q multiplier enters the C1
reverse-prefix comparison.

## 6. Conditional representation witness for each fixed u

Fix any u in (0,1/4). For Q>=4 choose

    t_Q=1/4+1/(2Q).

This belongs to [1/4,3/8] and is exactly halfway between adjacent grid
values (Q/4)/Q and (Q/4+1)/Q. Every positive-Q-grid next-1 probability
has distance at least1/(2Q) from t_Q. For Q=2 take t_Q=1/4; its distance
from the unique allowed value1/2 is1/4=1/(2Q). Thus on every full
history and every admissible realization of the private seed,

    kl(t_Q,q1)>=2/(2Q)^2=1/(2Q^2).                       (C2.12)

The inequality holds almost surely if the grid requirement is stated
almost surely. Conditioning on S_N=00 preserves it because this event
has mass u>0. It follows that C_N,Q(u)>=1/(2Q^2), even with u known.
The witness uses the actual D1 family and does not depend on N. Since
t_Q<=3/8<1/2 and the first-order curve has t=(1-u)/(1+2u)>1/2, each
of these laws is genuinely order two.

## 7. Average representation witness within exactly D1

Fix t=1/2 and let u decrease to0 within (0,1/4). At row10 the next-0
probability is r=ut/w and the next-1 probability is1-r. Any positive-Q-grid
output obeys q1<=1-1/Q. With h2(r)=-r log r-(1-r)log(1-r), for every
observed history ending in10 and every seed,

    KL((r,1-r)||q)
      =-h2(r)-r log q0-(1-r)log q1
      >=(1-r)delta_Q-h2(r).                              (C2.13)

The remaining row losses are nonnegative, and terminal10 has mass w.
Therefore every grid predictor, for each allowed positive u, has

    R_N(u,1/2;q)>=w[(1-r)delta_Q-h2(r)].

As u tends to0, w tends to1/3, r tends to0, and h2(r) tends to0 (from
lim_(x->0+) x log x=0). Taking a supremum over the allowed laws gives

    sup_(u,t) R_N(u,t;q)>=delta_Q/3.                      (C2.14)

There is no exchange of limit with a predictor-dependent expectation:
the explicit right-hand bound is independent of q. This is a supremum
over strictly positive allowed laws, not an attained law at u=0. Also
t=1/2 differs from the first-order curve for every allowed u. This
argument requires no external IID witness or larger model class.

## 8. Statistical lower bounds, max-to-sum and scope

Every grid predictor is also an unrestricted probability predictor.
Thus the C1 statistical lower bounds apply to the grid class, including
all-history randomization and known-u conditional comparison. For each
predictor its worst-case risk is bounded below by each applicable
statistical or representation number; taking the infimum yields the
maxima in (C2.1),(C2.2). The witnesses used in the two arguments differ.
We do not assert their sum as a lower bound on one chosen source.

For explicit order constants, N+6<=3N and delta_Q>=1/Q imply

    M_N,Q >= (1/32768)(1/N+1/Q).

Indeed the two entries of its lower maximum are at least
1/(16384N) and1/(3Q), and max(x,y)>=(x+y)/2. Likewise,

    C_N,Q(u) >=(3/32768)(1/(1+Nu)+1/Q^2),

using 1+(N-2)u<=1+Nu and the conditional format bound1/(2Q^2).
Together with the simultaneous upper bounds, these prove the requested
uniform constant-factor orders. The constants are deliberately coarse.

For fixed u>0, increasing N and taking Q_N to infinity yields vanishing
conditional expected KL; the average bound is uniform over u,t. With
fixed Q the format witnesses give nonzero minimax floors. The C1
triangular example u_N=1/(N+1), t_N chosen from {11/32,13/32} still
prevents uniform conditional statistical consistency even if Q grows.
None of these claims is fixed-law inconsistency or almost-sure convergence.

Strict positivity is part of Delta_Q^+. If a different format permits
zero coordinates, merely permitting them does not imply infinite risk.
If a predictor actually outputs a zero coordinate with positive conditional
seed probability on a positive-probability history, every strictly
positive D1 law gives that history positive mass and the KL there is
infinite. For conditional00 risk this statement applies to histories
ending in00; for average risk it applies to any history. If zero outputs
are null at each history, the finite union over histories is null and
the positive-grid arguments apply as before. This distinction does not
change the present positive-output classification.

These bounds constrain the emitted distribution's exact grid only.
They imply no necessity result for internal count precision, attention
scores, number of heads, width or depth. C3 must separately establish the
actual finite causal realization and its full costs. The current claim
does not assume neural advantage, learnability, noisy-arithmetic
reliability, practical constants or publication novelty.

## 9. Review and native dependency gate

The Lead integer map and its coordinate convention from checkpoint
SHA256 `7c19965199c6cd92dc578c3a3f4d91009fbefc2948754b5de6e21b292dce8b4a`
are incorporated explicitly in (C2.3). No mathematical error in that
checkpoint's C2 argument was found on rederivation. The more specific
zero-coordinate conditional-risk qualification in section8 prevents
an overbroad use of the average-risk zero-output observation.

The fixed v1 main proof, Counter, Lead and independent discussion gates
were completed before its first native submission. C1 was accepted first;
v1 C2 used the actual C1 Fact above and received transport_status=ok,
verdict=wrong solely because its local encoding/converter costs were absent.
The original request, result and fixed files are retained in admissions-v1/.
Section2a is the versioned repair of that specific recorded gap. It has
not been submitted or independently checked yet. Lead should arrange only
the needed fixed-version repair review; [Non-scientific operational metadata omitted.]
Any later C2 submission must use the actual C1 Fact e418ec34b7dbc4a6 as
predecessor. A file hash, obligation ID or discussion verdict is not a Fact.
Actual C2 Fact IDs=[]; actual C2 accepted Evidence IDs=[] at v2 writing.
