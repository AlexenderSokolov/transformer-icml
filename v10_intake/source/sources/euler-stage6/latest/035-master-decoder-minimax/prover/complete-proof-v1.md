# 035 REL-MASTER-DECODER-MINIMAX — complete finite proof

Obligation: 8599a1da51c3a58933ee7131d0fd6e995e1f2c8ed84a355e4d1832443e20f57d.
Frozen statement: outputs/035-master-decoder-minimax/lead/frozen-statement-v1.md,
SHA256 35098190dd9e303fcf413a311df3058b129868f76a99514be7ad0c72c67cff1c.
The native exact statement and frozen file are byte-identical (13615 bytes).
This proves the entire HDEC-MATCH/HDEC-SEQUENCE/original-implementation-cost
conjunction, including the new source and complete master information bridge.

## 0. Direct premises, quantifiers and the full interface

Only the following admitted Facts are direct predecessors:

* SRC fef8372728290b45, Evidence
  e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505:
  actual Pi, finite head error, all master coordinates, retained exact
  bits and lifecycle, original suffix legality, and full construction costs.
* MM5 946d42d5bf502eb4, Evidence
  aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82:
  the common full-history actual TV minimax lower bound.
* 033 a1a95aa68be0723e, Evidence
  3dd4849df0b1a9bf560d3e2ee0216cd46dd84ddb97fa6863faf53a8aa089cc0a:
  only its fixed original-suffix upper bound, specialized to D=0.
* 034 d3e63f7b5e389adf, Evidence
  dbadc5e7ba8291254d133f41b62bbb5acb0368631d6a7cb0b9fda79b4a5b8d3a:
  proof section 5's finite uniform-prior Beta/bin absolute-loss lemma
  and section 6's scalar logarithmic inequality, in their exact domains.

No arbitrary-decoder information conclusion is imported from the 033 rho
attack or inferred backwards from the 034 V cut. No four-group source or
a>=4 estimate from 032/034 is imported. The five-group source, every head
change and the multi-pair conditioning are proved below. Old proofs and
dependencies are neither reopened nor altered. Numerical diagnostics and
team discussions are not mathematical premises.

Fix arbitrary integers K>=22, M>=1 and h>=h_N, and a public real delta>=0,
where N=M+2, n_tok=M+3, h_N=ceil(log2(128(K+1)(M+3)^3)), Q=2^h.
The observation is the whole X_1^N; Y_i=(X_(i+1),X_(i+2)). Only departures
0<=i<M are counted, and the target is theta_(Y_M) from this same trajectory.
Every experiment uses a fixed homogeneous second-order table with legal
shifts and arbitrary initial pair law mu; zero probabilities are allowed.
The source can depend on public parameters, but not change along the path.
Put T=K^(5/2)/sqrt(M+1), x=K^5 delta. TV is half L1 distance, and
    Psi(0)=0; Psi(u)=u(1+ln(1/u)) for 0<u<1; Psi(u)=1 for u>=1.
All logarithms in Psi and harmonic comparisons are natural.

Use the original clean SRC prefix, including its finite log/exp evaluation,
full accumulations, directed quotients and clipping. Its actual master H
lies in G_h^(9K+1), G_h={0,1/Q,...,1}. The complete coordinate interface is
    P1(q1,v1), P2(q2,v2), T-head(hvec,h0), uniform(alpha,nu,f,rho).
The T-head name is distinct from the statistical scale T. SRC gives for
every finite input string and query, not just positive-probability paths,
    ||H- H^id(X)||_infty <=2/Q,                        (0.1)
where H^id denotes the ideal comparison heads specified by SRC.
The actual input is H, not H^id. We will pay (0.1) explicitly.

The cut is post-quantization and pre-fanout, with one canonical master
per coordinate. An admissible common kernel replaces all these masters
by Hbar in the same grid with ||Hbar-H||_infty<=delta on EVERY history.
All downstream copies start from Hbar. The kernel may read observed
history, current H, public data and its independent seed, but not hidden
theta,mu, future data or a decoder's private seed. There is no V edit,
extra arithmetic fault or bad-event allowance. The decoder receives all
Hbar and the complete retained exact bits audited in section 5 below,
with none of the excluded history/evaluator/statistic/snapshot ports.

For a fixed common decoder A, write r(A) for its supremum risk over the
allowed sources and kernels. A may depend on all public parameters and
use unlimited computation and an independent private seed, but not hidden
source parameters. We establish a lower bound for every fixed A before
taking inf_A r(A)=R_dec,H. All losses are total actual mean TV losses.

## 1. Upper bound, identity lower bound, and real-budget branches

The integer 128(K+1)(M+3)^3 is at least 16, 2M and M+1. Hence
    h_N>=h0=max(4,ceil(log2 M)+1), Q>=2M and Q>=M+1.     (1.1)
These inequalities hold for all stated h and M, including M=1.
The decoder class contains the original SRC full downstream computation
from its replaced masters, exact bits and public data. Its guards, clip,
smoothing floor and positive-bank ordered output are legitimate on all
canonical master replacements by SRC. Select that decoder and use 033
with second-stage budget D=0; the second kernel is necessarily identity.
This gives precisely
    R_dec,H <= R_H^Pi <= min(1,64T+36Psi(K^5 delta)).    (UPPER)
No decoder information lower bound is taken from 033.

For every fixed A the identity master kernel is legal. Composing A with
the clean finite SRC prefix and exact-bit extraction gives a common
full-history probability predictor. Its additional public h,delta do not
reveal theta or mu. MM5 applies to this predictor and gives
    r(A)>=2^-16 min(1,T).                              (STAT)
Its witness may differ from the family below. This argument remains
valid for arbitrarily powerful or randomized decoders.

The elementary identities and estimates
    Psi(u)=integral_0^1 min(1,u/v) dv,
    Psi(u)<=2sqrt(u), Psi(u)>=min(1,u)                  (1.2)
follow by splitting the integral at u and, for 0<u<1, maximizing
(1+s)e^(-s/2) with s=ln(1/u)>=0. They include u=0 and u>=1.
Let delta0=min(delta,1/8), x0=K^5 delta0. Then Psi(x0)=Psi(x): for
delta<=1/8 the arguments coincide, and otherwise both are at least
K^5/8>1. If T>=1, STAT pays the requested capped lower bound. If T<1
and x0<=2^16 T^2, then Psi(x)<=512T, so STAT again suffices up to an
absolute constant. Only the branch
    T<1 and x0>2^16 T^2                                (1.3)
needs the erasure argument. The source itself below is valid throughout
T<1. In particular sub-grid 0<=delta<1/Q has x0<=K^5/Q<=T^2 and belongs
to the statistical branch; it is not omitted or replaced by a grid delta.

## 2. Five-group parameters and a fully specified homogeneous source

When T<1, integer M satisfies M>=K^5. Set
    a=floor((K-6)/5), P=a^2, L=P+5, m=floor(M/L), U=a^2 L,
    r=floor(a/2).
Since K>=22, a>=3 and 5a+6<=K<=5a+10<=10a. Also r>=a/3 for every
integer a>=3 (check the even and odd cases), and r<=a/2. Consequently
    a>=K/10, r>=K/30, L<=2a^2<=K^2, m>=4.             (2.1)
Here M/L>=K^3, which is more than needed for m>=4. The required bounds
follow without importing any a>=4 estimate:
    U>=a^4>=K^4/10000>=K^4/2^14,
    U<=2a^4<K^4,
    rU>=a^5/3>=K^5/300000>=K^5/2^20,
    rU<=a^5<=K^5,
    rU/M<=K^5/M<=2K^5/(M+1)=2T^2.                    (2.2)
In particular these cover a=3,r=1 and unused alphabet symbols.

Take five disjoint groups Agrp,Bgrp,Cgrp,Dgrp,Egrp with a symbols each,
starting at 0,a,2a,3a,4a. Take six distinct markers
    (p0,q0,p1,q1,xi,zeta)=(5a,5a+1,5a+2,5a+3,5a+4,5a+5).
All are in {0,...,K-1}. Select the labels
    e_(ell,+)=4a+2ell, e_(ell,-)=4a+2ell+1, 0<=ell<r.
Other symbols in Egrp and elsewhere may have zero probability.

There is a finite closed word w_0,...,w_P with w_0=w_P=0 whose P
successive ordered pairs enumerate Agrp^2 once, including loops.
Here is a finite existence proof. In the complete directed graph with
loops on a vertices, each vertex has indegree and outdegree a. Follow
unused edges from 0 until a maximal trail ends. Balance forces it to
end where it started. If edges remain unused, some vertex on the current
closed trail has an unused outgoing edge: otherwise completeness would
prevent any unused edge or unvisited vertex outside its vertices. Start
another maximal unused trail there; the remaining balanced degrees force
it to close. Splice it into the first trail. Each splice uses additional
edges, so after at most a^2 edges the procedure terminates with all edges
used. Fix a deterministic choice of such a word using public a only.
Write w^0=w, w^1=w+a coordinatewise.

For each z in Cgrp x Dgrp and 0<=ell<r fix t_(z,ell) in [0,1]. Define
theta^t by these rows; a single symbol means its point mass:

* For s=0,1: (p_s,q_s)->w^s_0; (q_s,w^s_0)->w^s_1;
  (w^s_i,w^s_(i+1))->w^s_(i+2) for 0<=i<=P-2.
* (w^0_(P-1),w^0_P)->xi; (w^0_P,xi)->zeta;
  (xi,zeta)->(1-1/m)delta_p0+(1/m)delta_p1;
  (zeta,p_s)->q_s for s=0,1.
* (w^1_(P-1),w^1_P)->Unif(Cgrp);
  (w^1_P,c)->Unif(Dgrp) for c in Cgrp.
* At z=(c,e) in Cgrp x Dgrp, assign label probabilities
  theta_z(e_(ell,+))=t_(z,ell)/r and
  theta_z(e_(ell,-))=(1-t_(z,ell))/r for 0<=ell<r.
* (e,v)->q1 for e in Dgrp and every selected label v;
  (v,q1)->w^1_0 for every selected label v.

All unlisted rows are delta_0. For the query rows, summing the two
probabilities within each pair and then over r pairs gives total one.
All other displayed rows are probability laws as well. Internal Euler
pairs occur once, their last pair is excluded from earlier assignments,
and groups/markers are disjoint. In particular the new Dgrp x Egrp and
Egrp x {q1} rows are distinct from every internal and marker row. Thus
all assignments are consistent. Every transition appends a symbol and
shifts (u,v) to (v,symbol). This gives one fixed homogeneous second-order
table for each fixed t, including all endpoint parameters t=0 or 1.

The stay circle, used to specify initialization, is
    y0=(p0,q0), y1=(q0,w0),
    y_i=(w_(i-2),w_(i-1)) for 2<=i<=P+1,
    y_(P+2)=(w_P,xi), y_(P+3)=(xi,zeta), y_(P+4)=(zeta,p0).
There are L such pairs, with gate phase L-2. Write d=M-mL, 0<=d<L,
k=(L-2-d) mod L, and set mu=delta_(y_k), independent of t.
The observed gate is still genuinely random, not a prescribed stay.

From (p0,q0) a stay circuit emits w_0,...,w_P,xi,zeta,p0,q0 in exactly
L steps. From (p1,q1), or subsequently from any (v,q1) with v a selected
label, a Bgrp circuit emits
    w^1_0,...,w^1_P,c,e,v_new,q1
in exactly L=P+5 steps. It ends at a pair (v_new,q1) starting the same
Bgrp circuit. Thus every label and every sign gives the same length
and never returns to the stay circle. Its query (c,e) is at phase L-2.
Activation at gate time g is followed by the first query at g+L and
by further queries every L steps.

## 3. Complete path law, sample counts and unknown parameters

The nonnegative phase distance from y_k to the gate is d, so until
activation the gate departures are d+iL. The counted possible gates
have indices i=0,...,m-1; M=d+mL is the terminal slot, not a departure.
If d=0 the first observed gate is random and is included in its path
probability. If d=L-1 then k=L-1 and initialization is (zeta,p0), with
next symbol q0; no unobserved earlier gate probability is paid. All
other initial residues are kept as observed deterministic prefixes.

For 0<=j<m let A_j be first activation at gate index m-j-1. There are
then j completed queries before the actual terminal query, and
    p_j=P(A_j)=(1/m)(1-1/m)^(m-j-1)>=1/(4m).           (3.1)
To check the finite constant, for s=m-1>=1,
(1+1/s)^s<=sum_(i=0)^s 1/i!<3<4 by the binomial expansion and a
geometric bound on the factorial tail. Invert this inequality; reducing
the exponent of 1-1/m increases the result.

Fix t, A_j, queries z_1,...,z_(j+1) in Cgrp x Dgrp, training pair indices
ell_1,...,ell_j in {0,...,r-1} and signs sigma_1,...,sigma_j in {+,-}.
They determine exactly one entire observed string: the known initial
residue, gates, internal circles and each labeled return are specified.
Different choices differ at an observed symbol. Their exact probability is
    p_j a^(-2(j+1)) r^(-j)
      product_(i=1)^j t_(z_i,ell_i)^(1{sigma_i=+})
                         (1-t_(z_i,ell_i))^(1{sigma_i=-}).      (3.2)
At t endpoints each factor denotes the selected probability, avoiding
any need for a 0^0 convention. The last query's two symbols are observed;
its pair index and sign at departure M are not. Every counted transition
and all label-dependent return symbols have been included in (3.2).

Sum (3.2) over signs for fixed t, queries and pair indices. Each factor
sums to one even for repeated (z,ell), because t is fixed. Thus the query
choices are conditionally iid uniform on Cgrp x Dgrp, the training pair
indices are iid uniform on {0,...,r-1}, and their joint law is independent
of t. Given those choices, the signs are independent with the indicated
fixed row/pair parameters. No general Markov sampling-at-random-count
iid assertion has been used.

For each possible terminal z, the only visits to that row are its
occurrences among the old query choices. Consequently
    J | (A_j,Y_M=z) ~ Bin(j,1/a^2),                    (3.3)
independently of t. Given the whole query and training-index sequences,
define n_ell as the number of old occurrences of (z,ell), and k_ell as
their positive-sign count. Then sum_ell n_ell=J, and conditional on t
the k_ell are independent Bin(n_ell,t_(z,ell)). Other rows may use the
same label symbols but have different parameters; this distinction is
preserved throughout the Bayes argument.

## 4. Exact changes of ALL heads under within-row sign rearrangements

We derive the new head bridge directly from SRC's head definitions.
For a key t=3,...,N write its local triple (u,v,w)=(X_(t-2),X_(t-1),X_t).
For the actual query z=(c,e), the ideal unnormalized weights are
    P1: 2^(1{u=c}+1{v=e}),
    P2: 2^(1{u=c}) 3^(1{v=e}),
    T-head: 2^(1{u=e}), uniform: 1.
Thus P1 weights are {1,2,4}, P2 weights are {1,2,3,6}; the other two
sets are {1,2} and {1}. In particular the double-match P1 weight 4
must be included in the candidate's abbreviated weight list. This is
the same weight 4 already present in its q1 change table. All these
weights are exact integers for the ideal comparison, so ideal heads
are finite rational functions of a given finite string, not calls to
real log/exp oracles. We do not replace the clean finite SRC evaluator
by this ideal computation.

The P1/P2 value vectors are (e_w,e_u), producing (q1,v1)/(q2,v2).
The T-head values are (e_v,F_t), producing (hvec,h0). Uniform values
are (e_u,e_v,F_t,z_t), producing (alpha,nu,f,rho), where z_t=1{t=3}
and F_t=z_t e_(X_(t-1)). Let Z1,Z2,ZT be the respective ideal weight
sums. Each is at least M and the uniform denominator is M.

Change signs only at completed queries of the actual row z=(c,e),
preserving query choices, pair indices and every other row's signs.
If that row's label changes from v to v', the only changed local
triples are at three consecutive keys:
    (c,e,v), (e,v,q1), (v,q1,w^1_0),                  (4.1)
with v replaced by v' in the other history. Labels lie in Egrp, so
neither v nor v' is c or e. The three weights and affected value slots
are exactly as follows; unnamed value slots at these keys stay fixed.

| key triple | P1 weight | P2 weight | T-head weight | changed values |
|---|---:|---:|---:|---|
| (c,e,v) | 4 | 6 | 1 | current-token coordinate v of q1,q2 |
| (e,v,q1) | 1 | 1 | 2 | lag1 coordinate v of hvec,nu |
| (v,q1,w^1_0) | 1 | 1 | 1 | lag2 coordinate v of v1,v2,alpha |

The uniform weight in every row of this table is one. The actual
endpoint/query is unchanged. Every affected weight is independent
of the sign. All other keys are unchanged, hence ALL head denominators
are unchanged, including Z1,Z2,ZT. For clarity, a label at query departure
i is X_(i+3), so the three keys are i+3,i+4,i+5. The first query is no
earlier than L; the last completed query is no later than M-L. Since
L>=14, all three keys lie in 3,...,N and strictly after key 3. Different
query blocks have disjoint such triples. Thus neither an initial flag
term nor a missing terminal boundary can affect this table.

Let Delta_v be the NEW minus OLD count of actual-row label v across
all old queries. Summing the table gives the exact changes

| coordinate family at a selected label v | new minus old ideal value |
|---|---|
| q1_v | 4 Delta_v/Z1 |
| q2_v | 6 Delta_v/Z2 |
| v1_v | Delta_v/Z1 |
| v2_v | Delta_v/Z2 |
| hvec_v | 2 Delta_v/ZT |
| alpha_v, nu_v | Delta_v/M each |

Every other coordinate is unchanged. In particular h0,f,rho are
unchanged: their initial-key flag contribution and all their denominators
are fixed. Nonlabel coordinates in the listed families are unchanged
as well. This accounts for all nine K-dimensional families and rho.

Because all coefficients in this exact difference table are constant
for the actual row, it depends only on net label counts, not on the
temporal arrangement of its signs. This conclusion holds even when a
canonical rearrangement changes many more than b individual symbols.
It uses signed net numerator changes, not a Hamming-distance bound.
For two histories of the same template with |Delta_v|<=b for every
label, it proves
    ||H^id(X')-H^id(X)||_infty <=6b/M.                 (4.2)
This comparison does not assert that the actual finite evaluator itself
is arrangement-invariant; its possible extra information is removed
using the separately paid error (0.1).

## 5. Globally legal canonical-history kernel and complete side inputs

Now assume (1.3), set A0=delta0 M and b=floor(A0/64). Cancelling K^5
in x0>2^16 T^2 and using (1.1) gives
    A0>2^16 M/(M+1)>=2^15,
    delta0 Q>2^16 Q/(M+1)>=2^16,
    b>=2 and b>=A0/128.                               (5.1)
The last bound uses floor(u)>=u/2 for u>=2. The integer b is an index
for the allowed public-parameter kernel; no real floor oracle is added
to the nominal Pi or to its cost claims.

Use the following SAME deterministic kernel on every history. Parse
the string against the public graph template of sections 2–3, allowing
both signs at each pair without consulting t. Require the prescribed
initial pair, the indicated stay/activation and return structure, and
an activated actual query in Cgrp x Dgrp. If this fails, return H.
Such parsing is a finite operation on the observed string: the gate
markers distinguish activation, disjoint groups distinguish queries
and labels, and the fixed Euler pairs and fixed starting phase determine
the internal paths. For a parsed string, its activation index, query
sequence, pair indices and signs are unique. This test uses the union
of possible supports, not a hidden parameter's support.

On a parsed string compute n_ell,k_ell for its actual row, and put
    k'_ell=b floor(k_ell/b).
Construct a canonical string X' preserving the entire initial segment,
all query choices and training pair indices, and every other row's
labels. For each actual-row pair ell, in the chronological order of
its n_ell visits assign + to the first k'_ell and - to the remainder.
Both branches have identical length and rejoin the Bgrp circle, so this
defines a valid template string with the same length and actual endpoint.
It need not have positive probability for the original hidden t; SRC's
all-string head bound does not impose such a condition.

Compute H^id(X') by the integer weights above and finite rational
normalization, and define each component of H* by
    H*_i=floor(Q H^id_i(X'))/Q.                        (5.2)
All ideal components are in [0,1], so H* is canonical in G_h^(9K+1),
including the endpoints 0 and 1. Return H* if ||H*-H||_infty<=delta;
otherwise return H. Outside branch (1.3) the kernel may be identity.
This guard/fallback defines a globally valid common Markov kernel
with the pointwise budget on every legal history. It reads no unknown
t,theta,mu or decoder seed and does not alter the exact side bits.

On every activated history of the witness source, parsing succeeds.
For each pair, 0<=k_ell-k'_ell<b; the two label count changes are
opposites and both have magnitude below b. The number of changed
positions can be much larger, which is why (4.2) was essential. Use
(0.1), (4.2) and the at most 1/Q new rounding error in (5.2) to get
    ||H*-H||_infty <=6b/M+3/Q
       <=delta0(6/64+3/2^16)<delta0<=delta.            (MASTER-ERASE)
Indeed 6/64+3/65536=6147/65536<1, by (5.1). The guard ALWAYS passes
on these histories. All 9K+1 actual finite-evaluator coordinates are
overwritten, including any sub-grid-scale arrangement information
they carried. No ideal coordinate has been substituted for an actual
coordinate without paying its error.

We explicitly audit the complete exact side-input exception from SRC
proof sections 2 and 8, at the same post-quantization/pre-fanout cut:

| exact retained input | dependence on the witness histories |
|---|---|
| public K,N,h,Q, positions/types, constants, masks and fixed schedule metadata | public and fixed |
| query one-hots and declared query/mode | the actual query is the terminal z; the mode is fixed |
| actual endpoint l2_q,l1_q at synthetic position q=N+1 | exactly the same terminal z |
| synthetic x_q,z_q,F_q | all zero, since q>=4 and z_t=1{t=3} |
| exact selectors/endpoint intersections derived from these bits | functions of the foregoing public/query/endpoint bits |

If an initial flag copy F_3 is retained, it is e_(X_2), fixed by the
public initial pair y_k; all other original F_t are zero. Any copies
add no information. In actual mode z is in the disjoint Cgrp x Dgrp,
so the SRC endpoint test 1{endpoint=(query second symbol,c')} is zero
for every c'. The possible external query slot of an actual-query call
is fixed or equals the declared z, not a label-dependent new input.

Statistical means h0,f,rho are expressly part of the replaced masters,
not exact flags. The clean evaluator numerators/denominators/weights,
remainders, projected-query temporaries, historical arrays/outputs and
statistical duplicate copies have no read port after this cut under
SRC's lifecycle. Arithmetic scratch is not an extra exact-flag input.
Storage and its former processing are charged but do not authorize
a reread. This is the frozen interface, not an added erasure assumption.

On activated events give a hypothetical decoder the augmented observation
    A_j, all j+1 queries, all j training pair indices,
    every OTHER row's training signs, and (k'_ell)_(ell=0)^(r-1).       (5.3)
Here "other row" always means a row different from the actual terminal
z, even when it uses the same label symbols or pair index. This observation
determines n_ell,J and the ENTIRE canonical X', hence all of H* by (5.2)
and every exact bit in the table. It therefore exactly simulates the
real input of any decoder A, which on these events receives Hbar=H*.
This is the required information direction: a bound valid even after
giving (5.3) is valid for the original input. The augmentation does not
contain the actual row's original signs, k_ell or parameters. On the
nonactivation event we can simply drop the nonnegative loss. No hidden
source or extra samples are supplied to the actual algorithm.

## 6. Multi-pair Bayes conditioning and finite sample risk

For the proof only, give all t_(z,ell) independent Unif[0,1] priors.
Every parameter realization is still a fixed homogeneous source. The
same kernel above is used throughout this prior and never reads t.
Let G consist of A_j, all query choices, all training pair indices,
and all other-row signs. By (3.2), the choices and pair indices have
a joint law independent of every parameter. Conditional on them, the
likelihood factors over distinct (row,pair) parameters. Conditioning
on other-row signs changes only other-row factors. Thus, conditional
on every positive-probability G, the actual row parameters remain
independent uniform, their samples in disjoint pairs are independent,
and
    k_ell | t_(z,ell),G ~ Bin(n_ell,t_(z,ell)).          (6.1)
This verifies independence after the augmentation; it does not treat
the observed other-row labels as samples of t_(z,ell).

Use exactly 034 proof section 5's finite bin lemma: for a uniform
parameter t, k|t~Bin(n,t), n>=0 and integer b>=2, an estimator seeing
only b floor(k/b) has Bayes absolute error at least
    (1/32) min(1,b/(n+1)).                             (6.2)
This is a bound after averaging the bin, not a bound conditional on
an arbitrarily selected bin. Its admitted proof uses the identities
P(k=s)=1/(n+1), E[t|k=s]=(s+1)/(n+2), uniformity within each integer
bin and the median absolute-deviation sum floor(s_bin^2/4). It covers
the short last bin and b>n+1; for n=0 it separately uses the original
Unif[0,1] minimum absolute loss 1/4. That n=0 step is retained here.
For a real estimate outside [0,1], projection to [0,1] only decreases
its distance from t, so the same lower bound applies. We use no
restriction on output ties or on randomization beyond independence
of the private seed from the data-generating experiment.

Fix G, then fix the decoder seed. For one pair ell, additionally
condition on all other pairs' bins. By the conditional independence
just proved, those bins do not alter the joint law of t_(z,ell),k_ell.
The output coordinate, as a function of its own bin, is therefore an
admissible estimator for (6.2). The estimate r q_(e_(ell,+)) may be
outside [0,1], but the projection argument handles it. Apply (6.2),
then average the other bins and seed, separately for each ell.

For every K-dimensional probability output q, including mass outside
the selected Egrp labels, half the full L1 sum dominates the partial
positive-label sum:
    TV(q,theta_z)>= (1/2) sum_ell |q_(e_(ell,+))-t_(z,ell)/r|
                 = (1/(2r)) sum_ell |r q_(e_(ell,+))-t_(z,ell)|.
Linearity of expectation now gives, conditional on G and averaged over
ALL actual-row bins and their parameters,
    Bayes E TV >= (1/(64r)) sum_ell min(1,b/(n_ell+1)). (6.3)
No actual-row count k_ell or original sign was exposed in this argument.
The estimator may use all the other bins, but those bins were handled
as independent information, not as new samples for its own pair.

By (5.1) and min(1,b/u)>=b/(u+b), for u=n_ell+1>0,
    min(1,b/u)>= A0/(128u+A0)>=A0/[128(u+A0)].
The function u->1/(u+1+A0) is convex, and sum n_ell=J. Applying the
finite equal-weight convexity inequality across the r pairs yields
    sum_ell 1/(n_ell+1+A0)>=r^2/(J+r+rA0).
Consequently (6.3) proves exactly
    Bayes E TV | G >= r A0/[8192(J+r+rA0)].             (H-BIN-LOSS)
This includes r=1, every zero sample count n_ell, empty actual-row
training, all bin sizes and randomized decoders. No concentration
approximation or replacement of the full observation was used.

## 7. Harmonic averaging, Psi comparison, and fixed constants

H-BIN-LOSS depends on G only through J. Average over the other-row
signs and pair indices, then use (3.3). Conditional Jensen for the
positive convex reciprocal gives
    Bayes E[TV | A_j,Y_M=z]
       >=r A0/[8192(r+rA0+j/a^2)].
This is the same for every terminal z. Use p_j>=1/(4m), keep all
j=0,...,m-1 and drop only the nonactivation loss. The resulting bound is
    Bayes E TV >= r A0/(32768m)
        *sum_(j=0)^(m-1) 1/(r+rA0+j/a^2).             (7.1)
For c>0, comparison with the integral of a decreasing function gives
    sum_(j=0)^(m-1) 1/(c+j/a^2)>=a^2 ln(1+m/(a^2 c)).
Since m=floor(M/L)>=M/(2L) and M/m>=L, applying this to (7.1) proves
    Bayes E TV >= r delta0 U/32768
       *ln(1+M/[2U(r+r delta0 M)]).                   (H-HARMONIC)
All rounding of m and the j=0 term were paid. This works for every
remainder d and retains the entire initial prefix in the underlying law.

Let z0=r delta0 U and b0=rU/M. Equations (2.2) and (1.3) give
    x0/2^20<=z0<=x0, b0<=2T^2<x0/2^15.
Thus 2(b0+z0)<=10x0, and H-HARMONIC yields
    Bayes E TV >= x0/2^35 *ln(1+1/(10x0)).             (7.2)
We used a LOWER bound on the prefactor z0 and an UPPER bound on
the positive denominator b0+z0, so both comparisons preserve the
lower-bound direction. The 034 scalar lemma, valid for every u>0, is
    u ln(1+1/(10u))>=Psi(u)/16.
It covers both the logarithmic part and saturation: for u>=1 the
left side is >=1/11; for u<=1, writing s=ln(1/u), the function
ln(1+e^s/10) has value and derivative at least 1/11 on s>=0, so it
is at least (1+s)/11. Inserting this bound into (7.2) gives
    Bayes E TV >=2^-39 Psi(x0)=2^-39 Psi(x).            (7.3)

Every fixed decoder A is covered by the simulation (5.3) and all
preceding Bayes bounds. Its prior-average risk under the SAME legal,
t-independent kernel is at most its supremum over fixed homogeneous
source realizations, and hence at most r(A). Thus (7.3) implies
r(A)>=2^-39 Psi(x) in branch (1.3), uniformly for all A. No interchange
of infimum and supremum, common difficult source for all algorithms,
or assumption of an attained source maximum is required.

Let F=min(1,T+Psi(x)). For each fixed A the branches are now complete:

* If T>=1, STAT gives r(A)>=2^-16>=2^-160 F.
* If T<1 and x0<=2^16 T^2, then F<=513T<=1024T.
  STAT gives r(A)>=2^-26 F>=2^-160 F.
* Otherwise STAT and (7.3), from possibly different source families,
  give r(A)>=max(2^-16 T,2^-39 Psi(x))
             >=2^-40(T+Psi(x))>=2^-160 F.

Only the supremum lower bounds are compared by max; they are never
added as if produced on a single source. Taking inf_A AFTER these
uniform bounds, and using UPPER, proves for the whole frozen domain
    2^-160 min(1,T+Psi(K^5 delta))
       <=R_dec,H(K,M,h,delta)<=R_H^Pi(K,M,h,delta)
       <=min(1,64T+36Psi(K^5 delta)).                 (HDEC-MATCH)
Constants are not optimized or split into separate obligations.
Delta=0 and sub-grid delta use the statistical branch. M=1 and other
small horizons do not require a source with invalid m. Large real
delta is covered by the capped-radius legal subkernel and Psi(x0)=Psi(x).
Every h>=h_N, every horizon residue and every master coordinate remain.

For a legal public sequence, let T_n=K_n^(5/2)/sqrt(M_n+1) and
x_n=K_n^5 delta_n. If T_n->0 and x_n->0, continuity of Psi at zero
and UPPER imply R_dec,H,n->0. Conversely HDEC-MATCH makes risk->0
imply min(1,T_n+Psi(x_n))->0; the nonnegative uncapped sum must then
tend to zero. Hence T_n->0 and Psi(x_n)->0. Since Psi(x_n)>=min(1,x_n),
also x_n->0. Therefore
    R_dec,H(K_n,M_n,h_n,delta_n)->0 iff
    K_n^(5/2)/sqrt(M_n+1)->0 and K_n^5 delta_n->0.      (HDEC-SEQUENCE)
This uses the original REAL delta, not a replacement grid radius.
Witnessing sources can vary with n and between necessary terms; no
uniform almost-sure or one-source-across-all-horizons claim is made.

## 8. Original upper implementation and complete costs

The upper realization is the original SRC full suffix from its master
cut, not a new decoder or an ideal-head implementation. The actual
prefix, six heads, finite arithmetic, directed products/quotients,
guards, clip, r0 and ordered output remain the same. Its word parameter
is p=4h+4ell_word+64 with ell_word=ceil(log2(M+K+4)); ell_word is not a
label-pair index. The number of charged positions is n_tok=M+3, not the
statistical denominator M+1. SRC's dense/uncached batch hybrid bounds are
retained in their original representation and absolute-constant scope:

| Resource | Same SRC bound or structure |
|---|---|
| neural depth / width | O(Kp^2) / O(Kp) |
| total heads / max per layer; QK dimension; score cap | 6 / 4; at most 2K; 2 |
| single coefficient and arithmetic word | at most 128p bits, including full products, remainders and guards |
| dense coefficient slots / parameter bits | O(K^3 p^4) / O(K^3 p^5), zeros and biases charged |
| active gates/projections / identity holds | O(Kp^2+K^2) / O(K^2 p^3) |
| alternate sparse program/coefficient/address/hold format | O(K^2 p^4) bits, not substituted into dense costs |
| masks and position metadata | O(n_tok^2+n_tok log(n_tok+1)) bits |
| observed input | O(NK) one-hot bits, or paid binary acquisition/conversion |
| rolling working arrays only | O(n_tok Kp^2) bits |
| uncached finite attention bitwork | O(n_tok^2 (K+p)p^2) |
| dense pointwise and QKV bitwork | O(n_tok K^3 p^6) |
| finite rational log generation / scratch | O(p^3 log^2(p+1)) / O(p log(p+1)) |
| finite arithmetic evaluator code | O(p^4) bits |

All positions, input/query/actual-endpoint acquisition, QKV/masks,
full arithmetic, residual copies, holds, clears and final decode are
charged. The offline package includes public layout, masks/positions,
microcode and complete actual-format gate/term/hold generation. If their
record counts are G_rec,T_rec,I_hold, generation/assembly retains
O((G_rec+T_rec+I_hold)p^2) bitwork and O((G_rec+T_rec+I_hold)p) working
bits; dense output pays to write all coefficient bits including zeros.
At each phase sum simultaneously live program/parameters, input,
metadata/masks, QKV, residuals, banks, controller/address, temporaries
and output, then take the maximum over phases. Rolling work alone
does not equal total peak. Separate cached, sparse or PURE-expanded
alternatives retain their separate full costs, not mixed cheaper entries.

The infinite-computation decoder class strengthens an information lower
bound; it is not a free realized algorithm. The kernel's template parsing,
counting, canonical-history construction, rational ideal-head calculation,
grid rounding, guard, selector, data movement, storage and program costs
are extra if physically implemented. The same applies to any protection
mechanism. The kernel's history permission creates no decoder history
port, count table, cache or snapshot. No physical correction construction,
equal-numerical-budget advantage or global Transformer resource bound
is claimed. No compiler, literal ledger, network batch/profile measurement
was run. Bounded integer/Fraction diagnostics only checked mathematical
path/head identities and inequalities. [Non-scientific operational metadata omitted.]

## 9. Scope and preserved obligations

Sections 1–7 prove the complete finite and sequence conjunction; section 8
retains the actual original upper realization and its full costs. The new
information loss concerns the specified unencoded 9K+1 master port with
its exact side information. It does not constrain changed prefixes or
encodings, new snapshots/statistics, history rereads or physical correction.
It is not an extension of the fixed-suffix rho attack. It does not cover
K<22, h0-only precision, V edits, other arithmetic faults, excess loss,
or a common worst source across all parameters.

Direct predecessors remain exactly SRC, MM5, 033 and 034. The illustrative
weight enumeration has been made complete by including P1's weight 4;
the frozen head-change table, budget, constants, parameter domain and
target conjunction are unchanged. No hidden use of the four-group a>=4
source or a new Bayes obligation is made. All new source and head claims
are established in this body rather than by finite diagnostics.

031–034 and old roots are not resubmitted or given reverse dependencies.
The old 027 obstacles, 030 small-K/low-kappa gaps, 029 OPEN/PARKED,
[Non-scientific operational metadata omitted.]
protections are unchanged. Dot's exclusive statistics continuation,
missing delivery endpoint and fixed S001–S019 source restrictions remain;
no actual delivery or replacement Dot is claimed. Physical correction
and genuine resource relationships remain outside this result. Acceptance
of this nonroot conjunction does not complete the v10 mother task.
