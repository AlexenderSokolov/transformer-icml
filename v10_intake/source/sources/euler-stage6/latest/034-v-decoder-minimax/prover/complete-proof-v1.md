# 034 REL-V-DECODER-MINIMAX — complete finite proof

Obligation: 7e9edb773c2453ce6ca6ab0962158682e758dd98a2e5feefd614a6b6e185c6f8.
Frozen statement: outputs/034-v-decoder-minimax/lead/frozen-statement-v1.md,
SHA256 0385830f0ad7f25dee0334213fcd8d099a6ae6b551ba06efc5ccc32c5261586e.
Its 11914 bytes equal the native exact statement. This is one proof of
the whole DEC-MATCH/DEC-SEQUENCE/implementation-cost conjunction, including
the new source, all-coordinate erasure and side-information/Bayes bridges.

## 0. Admitted premises and experiment

The only direct Fact predecessors are:

* SRC fef8372728290b45, Evidence
  e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505:
  the actual finite Pi prefix, positive V-bank error, exact residual
  interface, cut lifecycle, original suffix and complete costs.
* MM5 946d42d5bf502eb4, Evidence
  aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82:
  any common full-history probability predictor has supremum actual
  TV risk at least 2^-16 min(1,K^(5/2)/sqrt(M+1)).
* 032 372cbc90282df2cd, Evidence
  1a61c7931a3b8ee13da63e8e24e758106308055d829d8e5e60195fbca96d0cf0:
  its fixed original-suffix V-MATCH upper bound; its finite Euler word,
  stay circle and elementary parameter bounds in the T<1 branch.

These existing proofs are not being resubmitted or altered. The 032
deterministic-label path law is NOT used as the random-label path law:
the latter is proved below from a new fixed transition table. Neither
033, 031, 015, 030 nor Dot is a premise. The use of 016 through 032's
admitted upper bound is transitive, not an additional direct use.
No diagnostic computation or team discussion is a mathematical premise.

Fix arbitrary integers K>=22, M>=1, D>=0 and h>=h_N, with
    N=M+2, n_tok=M+3,
    h_N=ceil(log2(128(K+1)(M+3)^3)), Q=2^h.
The observation is the whole X_1^N. Put Y_i=(X_(i+1),X_(i+2)); the
counted departures are exactly 0<=i<M and the target is theta_(Y_M).
Each experiment has one fixed homogeneous second-order table theta,
legal shift transitions, and an arbitrary initial pair law mu. Zero
edges are allowed. The supremum may choose theta,mu using public
parameters but cannot change them along the realized path. Define
    C_c=sum_(i=0)^(M-1) 1{Y_i=Y_M,X_(i+3)=c}, J=sum_c C_c,
    T=K^(5/2)/sqrt(M+1), eta=D/Q, x=K^4 eta.
TV is half the L1 distance. Psi(0)=0, Psi(v)=v(1+ln(1/v)) for 0<v<1,
and Psi(v)=1 for v>=1. Logarithms in Psi and integrals are natural.

Use the same clean original SRC-Pi prefix. On every history its actual
bank, as opposed to an ideal count encoding, satisfies
    V in {1,...,2Q}^K, |V_c-Q(C_c+1)/M|<=78.             (0.1)
The cut is after all V entries and before every final sum/quotient.
An admissible common kernel replaces V by W in that same positive
integer alphabet, with ||W-V||_1<=D on every history. It may use the
complete observed history, V, public parameters and source-independent
randomness, but none of the excluded hidden source/future/private-seed
inputs. The suffix receives W and precisely the allowed exact retained
bits, never the history or clean statistical/scratch banks.

For a fixed allowed decoder A, let r(A) denote its supremum risk over
these sources and kernels. A can use public parameters, arbitrary
computation, and a source-independent private seed, and outputs a
K-dimensional probability vector. Its choice precedes the source
supremum. We prove lower bounds uniformly for every such A, then take
inf_A r(A)=R_dec,V. All risks here are total actual mean risks.

## 1. Precision, upper implementation, statistical lower bound

The integer 128(K+1)(M+3)^3 is at least 16, at least 2M and at least
M+1. Consequently
    h_N>=h0=max(4,ceil(log2 M)+1), Q>=2M, Q>=M+1,
    Q/8 is an integer.                                (1.1)
These hold for all h>=h_N and M>=1.

The allowed decoder class contains the original SRC suffix: recompute
S_W=sum W, return floor(QW_c/S_W)/Q for c<K-1 and put the residual in
coordinate K-1. Positivity of all K bank entries makes this a legal
probability output on every permitted W. The side bits can be ignored.
By the exact 032 upper theorem in this same precision and fault domain,
    R_dec,V <= R_V^Pi <= min(1,64T+Psi(x)).              (1.2)
This imports no assertion about arbitrary decoders from 032; it only
selects an allowed particular decoder to upper-bound an infimum.

For each fixed A, choose the identity kernel, legal for every D. Its
composition with the clean SRC prefix and retained-bit extraction is
a common full-history probability predictor, with the same independent
seed. Public h,D do not encode the hidden source. MM5 therefore yields
    r(A)>=2^-16 min(1,T).                              (1.3)
In particular this lower bound holds even if the decoder's computation
is unlimited. The source witnessing (1.3) need not be the source below.

We use the elementary facts
    Psi(v)=integral_0^1 min(1,v/u) du,
    Psi(v)<=2sqrt(v), Psi(v)>=min(1,v).                 (1.4)
The integral identity follows by splitting at u=v if v<1; it also
proves monotonicity and subadditivity. For 0<v<1, writing s=ln(1/v)
gives Psi(v)/sqrt(v)=(1+s)e^(-s/2)<=2, by differentiation (the maximum
is 2e^(-1/2)); the endpoints and v>=1 are immediate.

Set D0=min(D,Q/8), eta0=D0/Q, x0=K^4 eta0. Then
    Psi(x0)=Psi(x).                                    (1.5)
Indeed for D<=Q/8 the arguments are equal, while for D>Q/8 both are
at least K^4/8>1. If T>=1, (1.3) already pays the requested capped
lower bound. If T<1 but x0<=256T^2, (1.4) gives Psi(x)<=32T, so again
the statistical lower bound pays T+Psi(x) up to a numerical constant.
The new source/kernel argument is needed only when
    T<1 and x0>256T^2.                                 (1.6)
In the next two sections the source itself only needs T<1.

## 2. Fixed random-label source, without changing the clock length

Since T<1 and M is an integer, M>=K^5. Use the 032 parameters
    a=floor((K-6)/4), P=a^2, L=P+5, m=floor(M/L), U=a^2 L.
Their admitted finite bounds, also immediate from 4a+6<=K<=4a+9,
are
    a>=4, K/8<=a<K/4, L<=K^2, m>=4,
    K^4/4096<=U<=K^4, U/M<=4T^2.                       (2.1)
For the last bound one may use the stronger 032 bound
U(K+1)/M<=4T^2. No alignment assumption on M is made.

Let Agrp,Bgrp,Cgrp,Dgrp be successive disjoint a-symbol intervals
starting at 0,a,2a,3a, and let
    (p0,q0,p1,q1,xi,zeta)=(4a,4a+1,4a+2,4a+3,4a+4,4a+5).
All these symbols exist; p0,p1 are distinct and p1<=K-4<K-1.
The group Dgrp is unrelated to the edit budget D.
Use the finite 032 Euler word w_0,...,w_P, closed at 0, whose successive
ordered pairs list all a^2 pairs once, including loops; fix its public
deterministic choice. Write w^0=w and w^1=w+a. Only its existence and
the stay-circle structure are imported, not a random-label path law.

For each z in Cgrp x Dgrp fix a real parameter t_z in [0,1]. Define
one homogeneous table theta^t by the following complete list of
nondefault rows; a displayed symbol denotes its point mass:

* For s=0,1: (p_s,q_s)->w^s_0, (q_s,w^s_0)->w^s_1;
  (w^s_i,w^s_(i+1))->w^s_(i+2) for 0<=i<=P-2.
* (w^0_(P-1),w^0_P)->xi; (w^0_P,xi)->zeta;
  (xi,zeta)->(1-1/m)delta_p0+(1/m)delta_p1;
  (zeta,p_s)->q_s for s=0,1.
* (w^1_(P-1),w^1_P)->Unif(Cgrp);
  (w^1_P,c)->Unif(Dgrp) for each c in Cgrp.
* (c,e)->t_(c,e) delta_p0+(1-t_(c,e))delta_p1 for every
  c in Cgrp, e in Dgrp; (e,p0)->q1 and (e,p1)->q1.
* (p0,q1)->w^1_0.

All unlisted rows are delta_0. The row (p1,q1)->w^1_0 is already in
the first item; it is not duplicated with a different assignment.
The row (p0,q0) retains its Agrp transition.

The internal Euler pairs are distinct and their last pair is excluded
from the earlier internal assignments. Disjoint symbol groups and
distinct markers separate all cross-group and marker rows. In
particular the new rows (e,p0) and (p0,q1) conflict with none of
(zeta,p_s), (p0,q0), (p1,q1), (q_s,w^s_0) or internal pairs. Thus
every row has one probability law, including t_z=0 or 1. Appending
a symbol always shifts (u,v) to (v,symbol). This is a legal fixed
second-order table, not a table reselected when a query is visited.

Use the unchanged stay circle
    y0=(p0,q0), y1=(q0,w0),
    y_r=(w_(r-2),w_(r-1)) for 2<=r<=P+1,
    y_(P+2)=(w_P,xi), y_(P+3)=(xi,zeta), y_(P+4)=(zeta,p0).
Put d=M-mL, k=(L-2-d) mod L, and mu=delta_(y_k). Here 0<=d<L,
and this initial law does not depend on t. The observed gate remains
random with activation probability 1/m.

The Agrp stay circuit emits w_0,...,w_P,xi,zeta,p0,q0 in exactly
L steps from (p0,q0). The new Bgrp circuit starting at either
(p0,q1) or (p1,q1) emits
    w^1_0,...,w^1_P,c,e,p_label,q1
in exactly P+5=L steps, with two uniform choices c,e followed by
the label p_label in {p0,p1}. At its end it is again at one of the
two starting pairs. The subsequent first row is identical for both
labels. Thus labels cannot change the circuit length or the query
choice distribution. A query has phase L-2 from either starting
pair. Activation at gate departure v leads to the first query at
v+L; consecutive queries are separated by L.

The gate phase in the stay circle is L-2, so its first nonnegative
departure from y_k is exactly d. Until activation, gates occur at
d+iL, i=0,...,m-1; the terminal slot is M=d+mL. For d=0 the initial
gate is genuinely random and included in the law. For d=L-1, k=L-1
and the initial pair is (zeta,p0): no probability of an unobserved
earlier gate is paid. All of the initial residue remains observed.

## 3. Full random-label path law and the complete side information

Let A_j be first activation at gate index m-j-1, for 0<=j<m. Exactly
j completed query departures then precede the actual terminal query.
Its activation mass is
    p_j=(1/m)(1-1/m)^(m-j-1)>=1/(4m).                  (3.1)
For example the finite estimate (1+1/r)^r<=sum_(i=0)^r 1/i!<3<4
with r=m-1 proves the lower bound by inversion; bound the factorial
tail by the geometric series starting at 1/2. Smaller exponents of
1-1/m only increase the mass after the 1/m factor.

Fix t, A_j, a sequence z_1,...,z_(j+1) in Cgrp x Dgrp, and j labels
ell_1,...,ell_j in {0,1}, where ell_i=1 denotes output p0. These
choices specify a UNIQUE complete observed history: the initial
stay residue, stay gates, activation gate, internal Bgrp paths,
choices and the two possible equal-length label-return paths are
all specified. Conversely distinct specified sequences differ in
an observed symbol. Multiplication of the genuine transitions gives
    p_j a^(-2(j+1))
       product_(i=1)^j t_(z_i)^ell_i (1-t_(z_i))^(1-ell_i).     (3.2)
At t_z endpoints interpret the factor by the corresponding chosen
probability, so no ambiguous 0^0 is needed. The terminal choice
z_(j+1) is fully observed. Its outgoing label would be at departure
M and is not observed or counted. There is no independent test query.

For fixed t and query choices, summing (3.2) over every label vector
gives p_j a^(-2(j+1)): every label factor sums to one, even when
query identities repeat, since t is fixed. It follows that conditional
on A_j the j old choices and the terminal choice are iid uniform
on Cgrp x Dgrp and their law is independent of t. Given these
choices, the observed labels are independent Bernoulli draws with
their respective fixed row parameters. There are no other visits
to Cgrp x Dgrp during intervening circles or the initial stay residue.
Therefore, for every possible terminal pair z,
    J | (A_j,Y_M=z) ~ Bin(j,1/a^2),                    (3.3)
    C_p0=k0, C_p1=J-k0, C_c=0 for other c,
    k0 | (J,t_z) ~ Bin(J,t_z), theta_(Y_M)=t_z delta_p0+(1-t_z)delta_p1.
More precisely the last binomial assertion remains valid conditional
on the full query choice sequence, whose occurrences determine J.
J and that sequence are independent of the parameter vector. These
conditional claims follow from (3.2), not from treating arbitrary
Markov row samples at random counts as iid.

We now specify the exact visible-bit exception, before using any
information lower bound. SRC proof sections 2 and 8 give the actual
residual inputs and their lifetimes. At the synthetic query position
q=N+1 they consist of the following:

| Retained exact information | Value or dependence in this experiment |
|---|---|
| public K,N,h,Q, positions/types, masks, constants and public phase/address metadata | fixed by public parameters and the fixed program |
| query one-hots A,B, actual/external mode and declared query if retained | actual mode is fixed, query is Y_M=z |
| actual endpoint copies l2_q,l1_q | e_(X_(N-1)),e_(X_N), hence the same z |
| synthetic token and initial-position flags x_q,z_q,F_q | zero, since q=N+1>=4 and z_t=1{t=3}, F_t=z_t l1_t |
| exact endpoint intersections/selection bits derived from these inputs | deterministic functions of query, mode and endpoint |

If initial-position flag copies are retained, the only possibly
nonzero data-dependent F_t is F_3=e_(X_2); here X_2 is the second
component of the publicly specified initial pair y_k. Thus those
flags also have no training-label dependence. Position/type masks
and branch bits for the fixed schedule are public. In actual mode
the endpoint is exactly the query; in particular its two symbols
are from disjoint groups, and the SRC intersection
1{endpoint=(query second symbol,c)} is zero for all c.

The statistical means h0,f,rho are explicitly not exact flags in
SRC section 8. They, other statistical masters, old sums/quotients,
products, division remainders, recovered frequencies and evaluator
guard/comparison scratch are not inputs of this final-cut decoder.
Historical arrays/unused historical outputs are erased or inaccessible
under that same declared interface. Remaining allocated/charged banks
do not create a port. This follows from the SRC cut and the frozen
034 decoder class; it is not an erasure assumption imposed on the
new source. We retain all the exact bits just listed, including the
actual endpoint even though it duplicates the query. Their values
are determined by public parameters and z (and the known initial
pair), not by the old labels. Any copies of these bits add no further
information. No original-history token or data-derived arithmetic
scratch is silently placed in the flag exception.

## 4. One globally legal binning kernel and actual-bank erasure

Assume branch (1.6), and put A0=eta0 M and b=floor(A0/8). From
K^4 eta0>256K^5/(M+1) and (1.1),
    D0=eta0 Q>256K Q/(M+1)>=256K,
    A0>256K M/(M+1)>=128K,
    b>=2 and b>=A0/16.                                (4.1)
For the last inequality use floor(u)>=u/2 when u>=2; here u=A0/8
is much larger than 2. All floors are ordinary public integer
definitions for the kernel, not free operations added to Pi.

Define the same deterministic kernel on every possible history as
follows. On query outside Cgrp x Dgrp return V. On a query inside,
compute the actual history counts J and k0=C_p0, and set
    k'=b floor(k0/b), v_p0=k', v_p1=J-k', v_c=0 otherwise,
    W*_c=max(1,floor(Q(v_c+1)/M)) for all K coordinates.       (4.2)
Return W* if it is in {1,...,2Q}^K and ||W*-V||_1<=D; otherwise
return V. Since 0<=k'<=k0<=J<=M, these definitions make sense on
all histories, even when their true counts have other labels.
The final guard makes the kernel globally legal and canonical.
It uses only public data, full-history counts and current V, not
theta,t,mu, future data or a decoder seed. For public parameters
outside (1.6) we can simply choose identity. Thus the kernel is a
single common mapping, independent of the hidden parameters.

On every activated history of the new source, (3.3) holds. For any
0<=v_c<=M, Q(v_c+1)/M lies in [Q/M,2Q]; rounding and the max in
(4.2) give
    1<=W*_c<=2Q, |W*_c-Q(v_c+1)/M|<=1.
The only differences between v and the true count vector are equal
opposite changes k0-k' in coordinates p0,p1. Using all K errors in
(0.1), rather than just the two ideal coordinates, yields
    ||W*-V||_1 <=79K+2Q(k0-k')/M
       <=79K+D0/4 <D0<=D.                             (4.3)
Indeed 0<=k0-k'<b<=eta0 M/8, and D0>256K makes 79K<3D0/4.
The guard therefore ALWAYS passes on every such history, including
zero-probability label choices when the same deterministic bound is
considered. Consequently the actual visible W, with every coordinate
and every finite-evaluator rounding effect accounted for, is exactly
the deterministic function (4.2) of (J,k'). The other K-2 entries
are constant functions of public M,Q. They cannot retain tiny
finite-arithmetic encodings of the old labels: (4.3) pays to replace
them as well. No clean counts or ideal vector are handed to A.

For the lower-bound argument we may give a decoder the augmented
observation
    (A_j,z_1,...,z_(j+1),J,k'),                         (4.4)
besides public parameters and its private seed, on activated paths.
This observation determines the actual W by (4.2) and every exact
retained bit by section 3. It therefore simulates the TRUE input
to any original decoder A exactly. An arbitrary rule using (4.4)
is at least as well informed as A. We give no labels ell_i, no k0,
and no parameter t. In particular, a lower bound for every rule
based on (4.4) is also a lower bound for A on these events. On the
nonactivation event we need no such simulation, because its loss
is nonnegative and can be dropped in a lower bound.

## 5. Self-contained Bayes bound with every bin boundary

Give the finitely many parameters (t_z) the product uniform prior
on [0,1]. This is only a proof device: each parameter realization
is still one fixed homogeneous source, and the kernel (4.2) is the
same for all realizations. First condition on A_j and its full query
choice sequence, including the terminal z. By (3.2) that conditioning
does not change the product prior. Sum out the unobserved-to-decoder
labels at other rows; each of those conditional probability laws
sums to one. At the J occurrences of the terminal row, the count k0
has Bin(J,t_z) law. Thus no extra likelihood depending on t_z comes
from the augmented unlabeled choice sequence or other rows.

For nonnegative integers r,s, integration by parts gives
    I(r,s)=integral_0^1 u^r(1-u)^s du = r! s!/(r+s+1)!.
For a direct induction, I(0,s)=1/(s+1); when r>=1 the boundary terms
vanish and I(r,s)=r I(r-1,s+1)/(s+1). Iteration proves the formula.
It follows for every 0<=k<=J that
    P(k0=k | J,unlabeled choices)=binom(J,k) I(k,J-k)=1/(J+1),
    E[t_z | k0=k,J,unlabeled choices]
        =I(k+1,J-k)/I(k,J-k)=(k+1)/(J+2).             (5.1)
This includes J=0. All such events have positive prior probability.
Within a given integer bin k'=b floor(k/b), k is uniform over that
bin's intersection with {0,...,J}.

For any K-dimensional probability output q,
    TV(q,t_z delta_p0+(1-t_z)delta_p1)>=|q_p0-t_z|.     (5.2)
The singleton-coordinate inequality follows because positive and
negative coordinate differences have equal total mass. It allows q
to place mass on any of the other K-2 symbols. At fixed augmented
observation and a fixed decoder seed, q_p0 is a fixed real number.
For each k in its bin, conditional Jensen and (5.1) give
    E[|q_p0-t_z| | k,J,choices]>=|q_p0-(k+1)/(J+2)|.
For s consecutive integers the minimum, over all real centers, of
the sum of absolute deviations is floor(s^2/4). Pairing the first
and last entries shows that a median minimizes the sum; for s=2r
the sum is r^2, and for s=2r+1 it is r(r+1). This covers all ties
and all choices of center. Hence, putting n=J+1 and writing s_i for
the successive bin sizes, the overall Bayes loss is at least
    sum_i floor(s_i^2/4) / [n(n+1)],                  (5.3)
whenever n>=2.

Here is a finite bound uniform over b>=2, including the final short
bin. For every integer s>=2, floor(s^2/4)>=s^2/8.
If b>=n>=2, there is one bin and (5.3)>=n/[8(n+1)]>=1/16.
If 2<=b<n, let q_bins=floor(n/b). The full bins alone have total
size q_bins b>=n/2. Ignoring the nonnegative last-bin contribution,
    sum_i floor(s_i^2/4)>=q_bins b^2/8>=nb/16.
Then (5.3)>=b/[16(n+1)]>=b/(32n). Thus in either case it is at least
(1/32)min(1,b/n). The last bin may be a singleton; it was not used
to assert a positive within-bin spread.

When J=0, n=1 and (5.3) alone would be zero, so it must not be used.
There are no labels at the terminal row, and its parameter is still
uniform, independent of the choices and the single bin. For every
q_p0 in [0,1],
    integral_0^1 |q_p0-u| du=(q_p0^2+(1-q_p0)^2)/2>=1/4.
This is stronger than (1/32)min(1,b). It handles this boundary directly.
All preceding estimates apply separately for every private seed;
integrating that independent seed retains the same lower bounds.

We have proved for every rule using (4.4), conditional on J and the
unlabeled choices, after averaging its visible bin and hidden parameter,
    Bayes TV >=(1/32)min(1,b/(J+1))
       >= A0/[512(J+1+A0)].                          (BIN-LOSS)
For the second comparison use b>=A0/16 and
min(1,b/n)>=b/(n+b)>=A0/(16n+A0)>=A0/[16(n+A0)].
This proof covers b>J+1, J=0, arbitrary output ties, random outputs,
and all K output coordinates. The infimum in the frozen BIN-LOSS is
the one over rules that observe the bin; it is not an infimum that
is allowed to inspect the hidden k or t.

## 6. Finite harmonic lower bound and the logarithmic scale

The loss bound in BIN-LOSS is independent of the particular unlabeled
choice sequence except through J. Average it using (3.3). For the
positive convex function u->1/(u+1+A0), conditional Jensen gives
    Bayes E[TV | A_j,Y_M=z]>=A0/[512(1+A0+j/a^2)].
There is no conditioning on arbitrary random row counts and asserting
iid; the exact path law justified this conditional binomial variable.
The bound is the same for each terminal z. Dropping the nonactivation
loss and using (3.1) now gives, for every original decoder A,
    Bayes E TV >= A0/(2048m) sum_(j=0)^(m-1) 1/(1+A0+j/a^2).
For a positive decreasing function, its value at each left endpoint
dominates its integral over the following unit interval. Therefore
    sum_(j=0)^(m-1) 1/(c+j/a^2)>=a^2 ln(1+m/(a^2 c)), c>0.
Since m=floor(M/L)>=M/(2L) and M/m>=L, the preceding two inequalities
prove exactly
    Bayes E TV >= eta0 U/2048
       *ln(1+M/[2U(1+eta0 M)]).                      (DEC-HARMONIC)
The j=0 term and m floor were retained. These estimates hold for every
horizon residue d; no conditioning removed the initial prefix.

Set z0=eta0 U and b0=U/M. Then (2.1) gives
    x0/4096<=z0<=x0, b0<=4T^2.
Under (1.6), b0<x0/64, so 2(b0+z0)<=10x0. DEC-HARMONIC consequently
implies
    Bayes E TV >= x0/(2048*4096) ln(1+1/(10x0)).       (6.1)
Both replacements have the correct direction: the prefactor uses
the lower bound on z0, whereas the logarithm uses the upper bound
on the denominator b0+z0.

For completeness the scalar inequality used here is
    v ln(1+1/(10v))>=Psi(v)/16, v>0.                  (6.2)
If v>=1, ln(1+w)>=w/(1+w) (integrate 1/(1+t) on [0,w]) gives the
left side at least 1/(10+1/v)>=1/11. If 0<v<=1, put s=ln(1/v)>=0.
The function f(s)=ln(1+e^s/10) satisfies f(0)>=1/11 and
f'(s)=e^s/(10+e^s)>=1/11. Thus f(s)>=(1+s)/11, proving (6.2) even
with 11 in place of 16. Combining (6.1), (6.2) and (1.5) yields
    Bayes E TV >=2^-27 Psi(x).                       (6.3)

This is a lower bound for each fixed A under the SAME legal kernel
throughout the prior. Its averaged risk is at most the supremum over
fixed parameter realizations, hence at most r(A). No parameter vector
or latent label is given to A or to the kernel. Thus (6.3) implies
r(A)>=2^-27 Psi(x) in branch (1.6), uniformly over all allowed A.
The usual supremum interpretation suffices even if a maximizing
source is not attained; it is not necessary to exchange inf and prior
or to claim one source is difficult across all parameters.

## 7. All branches, the fixed constant, and sequence equivalence

Let F=min(1,T+Psi(x)). For every A:

* If T>=1, (1.3) gives r(A)>=2^-16>=2^-120 F.
* If T<1 and x0<=256T^2, then F<=33T. Hence (1.3) gives
  r(A)>=2^-16 T>=2^-22 F>=2^-120 F, since 33<=64.
* In the remaining branch, (1.3) and (6.3) are two supremum lower
  bounds, possibly from different sources. Taking their MAX gives
  r(A)>=max(2^-16 T,2^-27 Psi(x))
       >=2^-28(T+Psi(x))>=2^-120 F.

The numerical max comparison does not assert that two risks add on a
single source. Now take inf_A, preserving the uniform lower constant,
and combine with (1.2). For all frozen finite parameters we obtain
    2^-120 min(1,T+Psi(K^4 D/Q))
      <=R_dec,V(K,M,h,D)<=R_V^Pi(K,M,h,D)
      <=min(1,64T+Psi(K^4 D/Q)).                     (DEC-MATCH)
In particular D=0 and the small-edit cases use the statistical branch;
M=1 is covered without constructing a clock with invalid m. Arbitrarily
large D uses the legal capped D0 kernel and (1.5), not an unbounded
bank move. All h>=h_N, every M residue and all K coordinates remain.
The conservative 2^-120 is proved as stated; constants are not claimed
optimal and have not been separated into subsidiary obligations.

For a public sequence in the domain, write T_n,x_n for the two
nonnegative arguments. If T_n->0 and x_n->0, continuity of Psi at
zero and the upper bound give R_dec,V,n->0. Conversely, if the risk
tends to zero, the lower bound forces min(1,T_n+Psi(x_n))->0. The
uncapped nonnegative sum must then tend to zero. Thus T_n->0 and
Psi(x_n)->0, and Psi(x_n)>=min(1,x_n) implies x_n->0. This proves
    R_dec,V(K_n,M_n,h_n,D_n)->0 iff
    K_n^(5/2)/sqrt(M_n+1)->0 and K_n^4 D_n/Q_n->0.     (DEC-SEQUENCE)
The necessary terms can have different witnessing sources. This is
worst-source/allowed-kernel mean consistency at the specified cut,
not a uniform almost-sure or single-witness-across-n assertion.

## 8. Same actual upper implementation and full cost accounting

The chosen upper decoder is the original SRC suffix, with its original
prefix, finite arithmetic and ordering; it changes no nominal Pi
computation. Its actual word parameter and position count are
    p=4h+4ell+64, ell=ceil(log2(M+K+4)), n_tok=M+3.
The statistical denominator M+1 is not the number of charged positions.
SRC's full dense/uncached batch hybrid bounds remain:

| Resource | Same SRC bound or structure |
|---|---|
| neural depth / width | O(Kp^2) / O(Kp) |
| total heads / maximum per layer; QK dimension; score cap | 6 / 4; at most 2K; 2 |
| single coefficient and full arithmetic word | at most 128p bits, including full products, remainders, guards |
| dense coefficient slots / parameter bits | O(K^3 p^4) / O(K^3 p^5), including zeros and bias |
| active gates/projections / identity holds | O(Kp^2+K^2) / O(K^2 p^3) |
| alternative sparse program/coefficient/address/hold format | O(K^2 p^4) bits, not substituted for dense storage or work |
| masks and positions | O(n_tok^2+n_tok log(n_tok+1)) bits |
| observed input | O(NK) one-hot bits, or paid binary acquisition/conversion |
| rolling working arrays only | O(n_tok Kp^2) bits |
| uncached finite attention bitwork | O(n_tok^2 (K+p)p^2) |
| dense pointwise and QKV bitwork | O(n_tok K^3 p^6) |
| finite rational log generation / scratch | O(p^3 log^2(p+1)) / O(p log(p+1)) |
| finite arithmetic evaluator code | O(p^4) bits |

All n_tok positions, input/query/actual-endpoint acquisition, QKV/masks,
complete arithmetic products/divisions/guards, residual copy, holds,
clear and final output decode are charged. The offline package retains
the layout, masks/positions, microcode and actual-format gate/term/hold
generation. For record counts G_rec,T_rec,I_hold this generation and
assembly uses O((G_rec+T_rec+I_hold)p^2) bitwork and
O((G_rec+T_rec+I_hold)p) working bits. Dense output pays to write all
coefficient bits, including zeros. At each phase sum every simultaneously
live program/parameter, input, metadata/mask, QKV, residual, bank,
controller/address, temporary and output allocation, and then maximize
over phases. Rolling working arrays do not replace total peak. Cached,
sparse or PURE-expanded alternatives keep their separate original costs;
no cheaper entries from them are spliced into this nominal realization.

Unlimited computation for the lower-bound decoder class is permission
in the minimax experiment, not a free realized algorithm. The upper
bound is supplied by the paid original Pi suffix. Likewise full-history
counts in (4.2) are an explicitly permitted adversarial computation,
not a new count-table input to the decoder. Physical injection or
protection, count scanning, selector, data movement, storage and program
costs would all be additional if implemented. There is no new snapshot,
cache, encoder or history reread in the nominal Pi.

No compiler, literal ledger, network batch execution/measurement or
profile was run. The accompanying bounded integer/Fraction checks
only diagnose finite path identities, bin boundaries and algebra;
the general proof is the one above. [Non-scientific operational metadata omitted.]
are both zero, in accordance with the current budget.

## 9. Scope, dependencies and remaining boundaries

The result concerns any common decoder at the specified unencoded V
port with exactly the retained bits audited in section 3. Within that
interface, replacing the original readout cannot improve the joint
K,M,D/Q risk order up to absolute constants. It does not constrain
algorithms that change the prefix, encode V, store extra snapshots or
statistics, or reread the history. It is not physical error-correction
impossibility, a resource lower bound for every Transformer, or a sharp
arbitrary-decoder master-fault theorem. In particular 033's publicly
repairable rho attack is not used as an information lower bound.
Neither K<22 nor h0-only precision is covered.

The only direct predecessors are SRC, MM5 and 032. The new random-label
table/path law, all-coordinate guarded erasure, complete retained-bit
simulation, Beta/bin loss and harmonic comparison were proved here.
All old roots and Fact dependencies, including 031–033, are preserved
without reverse dependencies or resubmission. The 027 two obstacles,
030 small-K/low-kappa gaps, 029 OPEN/PARKED, 021 closure, 022 OPEN/PARKED,
[Non-scientific operational metadata omitted.]
Dot's exclusive conditional-statistics continuation and missing delivery
endpoint remain separate; no actual delivery or replacement is claimed.
This single nonroot conjunction does not resolve the v10 mother task.
