# C2: self-contained common-channel full-history lower, v1

Counter, 2026-10-26. Fixed fifth-stage proof for current obligation
`52a14a0c60279133c7acc7067c15eb4cfbff32368f8a721e59df9bf3eecd9ff1`.
Predecessors: `[]`. Assumptions: exactly current PROBLEM.md D1-D2 and D6.
No historical Fact, old root, file review, primary theorem, diagnostic, or
architecture-restricted observation premise is used below.

Provenance: adapted from the supplied source-stage4 probe012 Counter
common-channel-lower-v1.md. Its old C1 admission interface is removed;
stationarity, reversal, common atom and contraction are proved directly here.
The original source files are unchanged. Grid parameter Q is public; letters
P,Q in the finite transport lemma denote two laws only. The stationary pair
law is pi; a coupling of full histories is a separate object.

## 1. Exact statement and quantifiers

Fix integers N>=6, m=floor(N/2), M=m-2 and
1<=k<=floor(M/1024). Put

    u0=k/N, Delta=1/640000,
    t_-=1/2-Delta/2, t_+=1/2+Delta/2,
    c=Delta²/8=1/3276800000000.                         (1)

There exists one source-independent randomized batch channel T_(N,k),
independent of the predictor and of Q, such that for EVERY binary input x and
EVERY channel seed it keeps x_(N-1),x_N and changes at most k other bits, and

    TV(L_(u0,t_+)(Z | S_N=00),
       L_(u0,t_-)(Z | S_N=00)) <= 1/64.                (1a)

For every public Q and every common randomized predictor whose data are
Z=T(X),N,k,Q, including unrestricted probability outputs, unlimited
computation, and even knowledge of the public two-point experiment/T, one
SAME t_* in {t_-,t_+}, at u=u0, satisfies

    R_00 >= c,                 R_av >= c k/N.           (2)

The channel has no future X_(N+1), realized hidden parameter/label, clean
side channel or source-dependent seed. Its independent private seed is not
given to the predictor. It may inspect the entire already observed history,
including its preserved terminal pair: this is a batch channel, not a
time-causal sensor. The predictor remains an unknown-u,t procedure on all D1;
only the lower-bound witnesses are fixed by (1). For k=0 define the channel
as identity; this lower asserts nothing at k=0. N=3,4,5 therefore have identity
contamination and the separate uniform predictor branch, with no fake prefix.

## 2. Finite residual transport without normalization

Let E be a finite Hamming fiber consisting of binary strings with the same
last pair. Let P,Q be probability laws on E and mu=P-Q. Write

    mu_+(x)=max(mu(x),0), mu_-(x)=max(-mu(x),0),
    tau=sum mu_+=sum mu_-=TV(P,Q).

TV uses sup-event distance, equal to half the L1 norm for probability laws.
The Jordan parts here retain mass tau; they are NOT normalized to mass1.
Take any coupling Pi of P,Q, with Hamming cost
C=sum_(x,y) Pi(x,y)d(x,y).

The off-diagonal quantities f(x,y)=Pi(x,y), x!=y, form a directed flow with
outgoing-minus-incoming divergence P(x)-Q(x)=mu(x). First remove directed
cycles. On each positive-flow cycle subtract its minimum edge weight from
every cycle edge. Divergence is unchanged, no new edge is added, at least
one edge disappears, and cost cannot increase. A fixed lexicographic rule
makes the procedure deterministic; finitely many steps give an acyclic flow.

Add a super-source a with edges a->x of weight mu_+(x), and a super-sink b
with edges y->b of weight mu_-(y). Every original vertex is now balanced.
The augmented graph is acyclic. If source flow remains, follow positive
edges from a. An intermediate vertex reached by positive flow has a positive
outgoing edge by balance. Acyclicity forces the path to end at b. Subtract
the smallest edge weight along this path, and record that amount lambda
on the original endpoint pair x,y. Balance persists; at least one edge
disappears. Repeating terminates after finitely many removals. When no source
edge remains, there can be no nonzero balanced acyclic residual component:
such a component would have a vertex with incoming0 and outgoing>0.

Consequently the recorded endpoint weights Gamma(x,y) have marginals
mu_+,mu_-. In particular their TOTAL MASS is tau. They go only from
positive-divergence to negative-divergence vertices. Triangle inequality
along each collapsed path gives

    sum Gamma(x,y)d(x,y) <= C.                         (3)

This proof permits transshipment through vertices of any divergence sign;
the super-source/sink capacities account exactly for the Jordan endpoints.
It is not an assertion that the original coupling restricted to positive and
negative supports already has those marginals. If tau=0 all flow can be
removed as cycles and Gamma is empty. Rational Pi gives rational Gamma.

## 3. One kernel on every input, with a hard bound for every seed

Fix integer k>=1. For each Gamma edge with d(x,y)<=2k, list the differing
coordinates in a fixed public order (low-to-high bits of the stored encoding)
and change the first floor(d(x,y)/2) of them
in x to their values in y. Call the result z_xy. Then

    d(x,z_xy)=floor(d(x,y)/2)<=k,
    d(y,z_xy)=ceil(d(x,y)/2)<=k.

The protected tail is identical throughout the fiber. This is a fixed
Hamming midpoint, not an assumption about midpoints in arbitrary metrics.
Call such edges good, and the remaining edges bad. Define rows as follows:

* If mu(x)>0, the row at x has weight Gamma(x,y)/mu_+(x) for each outgoing
  edge, sending it to z_xy when good and to x when bad.
* If mu(y)<0, the row at y has weight Gamma(x,y)/mu_-(y) for each incoming
  edge, sending it to the SAME z_xy when good and to y when bad.
* If mu(v)=0, its row is identity.

Every row sums1 by the Gamma marginal identities, including tau=0 by
using identity everywhere. Positive and negative supports are disjoint, so
an input has exactly ONE row K(v,.), fixed without the true source label.
For an explicit bad-fraction identity define, on the indicated supports,

    b_+(x)=sum_(y:bad) Gamma(x,y)/mu_+(x),
    b_-(y)=sum_(x:bad) Gamma(x,y)/mu_-(y).

Each is in[0,1]; its entire row fraction remains at that input. If
m(v)=min(P(v),Q(v)), then P=m+mu_+, Q=m+mu_- and hence

    PK=mK+mu_+ K,   QK=mK+mu_- K.

In particular mK cancels because it is subjected to the SAME K(v,.) at each
input under both laws. It need not remain at v and is not given a fictitious
identity branch. Expanding the residual rows gives the exact identities

    (P-Q)K=sum_bad Gamma(x,y)(delta_x-delta_y)
          =sum_x mu_+(x)b_+(x)delta_x
           -sum_y mu_-(y)b_-(y)delta_y,
    B:=sum_bad Gamma(x,y)
      =sum_x mu_+(x)b_+(x)=sum_y mu_-(y)b_-(y),
    TV(PK,QK)=B<=sum Gamma(x,y)d(x,y)/(2k)<=C/(2k).     (4)

The equality TV=B follows because the positive and negative residual
supports in this display are disjoint. The good signed masses cancel
exactly at the SAME z_xy, including when midpoint outputs collide with
other inputs. Bad edges satisfy d>2k, so their mass is bounded as displayed.
No division by tau has occurred: Gamma and B retain their original masses.

Every nonzero row outcome moves at most k bits, even on bad edges, since
bad fractions stay at the input. This proves support legality on ALL inputs,
not just in expectation. For rational laws and coupling all row probabilities
are rational. Choose a common denominator D for all entries of the finitely
many rows. In a fixed ordering of a row's distinct outputs write their
probabilities as n_1/D,...,n_r/D, with integer n_i>=0 and sum_i n_i=D.
An independent uniform seed J in {0,...,D-1} chooses output i exactly when
sum_(a<i)n_a<=J<sum_(a<=i)n_a; zero-size intervals are skipped. This fixed
interval partition realizes K. Every seed at every input selects
a supported legal output. D may be enormous; the channel's computation and
randomness are external/unrestricted in this experiment. This is a finite
existence construction, not a claim of an efficient adversary.

## 4. The two true conditional history laws and reverse kernels

For D1 set w=(1-u)/3, r_t=ut/w. Since 0<u<1/4,
0<u/w=3u/(1-u)<1; hence 0<r_t<3/4 and 1-r_t>1/4.
The forward pair matrix, in order00,01,10,11, is directly

    F_t=[[1-t,t,0,0], [0,0,1/2,1/2],
         [r_t,1-r_t,0,0], [0,0,1/2,1/2]].

For pi=(u,w,w,w), multiplication gives

    pi F_t=(u(1-t)+wr_t, ut+w(1-r_t), w, w)
          =(u,w,w,w)=pi,

using wr_t=ut. All four masses are positive and sum1. Start with pi as
D1 requires; thus every pair S_i has this stationary law.
For any supported transition i->j, Bayes' formula gives the predecessor
probability pi(i)F_t(i,j)/pi(j). Its rows are therefore exactly

    R_t=[[1-t,0,t,0], [r_t,0,1-r_t,0],
         [0,1/2,0,1/2], [0,1/2,0,1/2]].               (5)

For example reverse00 receives contributions u(1-t)/u and wr_t/u=t;
reverse01 receives ut/w=r_t and w(1-r_t)/w; reverse10 and reverse11
each receive w/(2w) from01 and11. All omitted entries are0. These rows
sum1 and pi R_t=pi, either by the displayed entries or by summing
pi(j)R_t(j,i)=pi(i)F_t(i,j) over j.

For every legal lower tuple, k<=M/1024<N/2048, so
0<u0=k/N<1/2048<1/4. Both t_± lie in[1/4,3/4]. Thus these are legal D1
sources. Each allowed appended bit has strictly positive probability, so
every binary input in a terminal fiber has positive conditional probability.

Here are actual THREE-transition reverse paths to c0=10:

    start    path                         path probability
    00       00 -> 10 -> 01 -> 10          t(1-r_t)/2
    01       01 -> 10 -> 01 -> 10          (1-r_t)^2/2
    10       10 -> 11 -> 01 -> 10          (1-r_t)/4
    11       11 -> 11 -> 01 -> 10          (1-r_t)/4.

Because t>=1/4 and 1-r_t>=1/4, every listed probability is>=1/32.
Consequently R_t^3(s,10)>=alpha:=1/32 for every s and every D1 parameter.
Put beta=31/32 and define the actual stochastic matrix

    B_t(s,e)=(R_t^3(s,e)-alpha*1{e=10})/beta.

Nonnegativity and row sums1 follow from the preceding bound. For any two
probability laws a,b on the four states,
(a-b)R_t^3=beta(a-b)B_t. A stochastic matrix contracts finite TV:
for a signed mass v, sum_e |sum_s v(s)B_t(s,e)|<=sum_s |v(s)|.
Since pi R_t=pi, iteration in blocks of3 and contraction of the remaining
0,1,2 steps imply

    R_t^3(s,.)=alpha delta_c0+beta B_t(s,.),
    TV(R_t^j(s,.),pi)<=D_j:=beta^floor(j/3),
    sum_(j>=0)D_j=3/(1-beta)=96.                      (6)

This directly proves the common atom and all contraction estimates used
below. Stationary reversal does not make the terminal query independent.

Let H=N-2. Under the true conditional law given S_N=00, write

    A_j=S_(N-j)=(X_(N-j-1),X_(N-j)), 0<=j<=H.

Indeed multiplying pi(s_(i+1))R_t(s_(i+1),s_i)
=pi(s_i)F_t(s_i,s_(i+1)) along any supported path telescopes to

    pi(s2) product_(i=2)^(N-1) F_t(s_i,s_(i+1))
      =pi(sN) product_(i=2)^(N-1) R_t(s_(i+1),s_i).

Unsupported paths have weight0 on both sides. Divide by the actual
Pr(S_N=00)=u and set sN=00: A_0=00 and A is exactly a length-H R_t path
under the true conditional history law. The reverse support imposes
second(A_(j+1))=first(A_j), so each such pair path reconstructs one and
only one binary history with that terminal pair. It includes all input symbols, with no crop/count substitution
and no TV error amplified by the rare factor1/u. We now
couple A^+ and A^- with kernels R_+,R_- and common starting state00.

The one-step row TV difference is

    h(00)=Delta, h(01)=(u/w)Delta, h(10)=h(11)=0,
    0<=h<=Delta, pi h=2uDelta.                         (7)

## 5. An adaptive coupling of complete paths

At a decision boundary whose states match at s, use a maximal ONE-step
coupling of R_+(s,.) and R_-(s,.). Explicitly place min of their point masses
on each equal-state pair. Write d(e)=min(R_+(s,e),R_-(s,e)) and
l_±(e)=R_±(s,e)-d(e). If h(s)>0, place residual joint mass
l_+(e)l_-(f)/h(s) on(e,f); if h(s)=0 use only the diagonal mass.
The residual supports are disjoint and their masses both equal h(s), so
this is a rational maximal coupling with mismatch probability exactly h(s).
A mismatch at this step is an episode birth.

At a decision boundary with states a!=b, commit to THREE transitions.
First couple endpoints using (6): with an independent probability alpha,
both endpoints equal c0; otherwise draw endpoints from B_+(a,.) and B_-(b,.)
(independently is sufficient). Given the endpoints, independently sample
the actual conditional three-step path of each individual chain. For example
the plus bridge through v1,v2 to e has probability

    R_+(a,v1)R_+(v1,v2)R_+(v2,e)/R_+³(a,e).            (8)

Zero endpoint probabilities are never selected. Multiplying (8) by the
endpoint marginal shows that the entire plus block has precisely its genuine
three-transition Markov path law; the same holds for minus. In particular
neither of the two intermediate pairs is omitted. The chance that the
endpoints match is at least alpha, whether or not the residual draws happen
also to match. Decisions resume only at the end of this committed block;
coincidence at an intermediate pair does NOT terminate the commitment.

If only one or two transitions remain before H, sample the same full block
and keep its corresponding prefix, stopping the observed construction at H.
Equation (8) implies every such truncated prefix has its genuine one-chain
Markov marginal. Auxiliary unused draws are integration variables in this
finite coupling, not extra clean observations supplied to the channel or
predictor, and have no relation to the invisible future target Y.

### Why adaptive block choices preserve the full one-chain law

A proof is needed because, inside a coupled block, conditioning on BOTH
chains' intermediate history need not give the single-chain transition R_t.
We do not make that false claim.

Conceal unused block draws until their pair positions are revealed. Boundary
times tau_i are stopping times for this reveal process with its commitment
phase; at a boundary, the next scheduled length1 or3 is a function only of
the two current states. The drawn block's individual marginal, conditional
on the entire joint boundary past, is the appropriate Markov block from that
chain's current state, as just proved. There is no adaptive decision inside
a committed block.

For a fixed position j<H, partition according to the last boundary tau<=j
and its scheduled length. The event that j lies in that block is determined
at its start: its length is already fixed there. Conditional on the joint
past AT THAT START and on this chain's own revealed prefix within the block,
its next transition has law R_t at its present state. This follows by
disintegrating that block's genuine Markov marginal; information from the
other chain's intermediate coordinates is not conditioned upon. For any
bounded test function of this chain's path through j, integrate this equality
on each disjoint block-start event and sum over starts. This proves

    E[f(A_(j+1)) | A_0,...,A_j]=R_t f(A_j).

More formally, for each possible start tau and scheduled length l, let
E_(tau,l) be the event that a boundary occurs there, chooses length l, and
tau<=j<tau+l. For fixed j<H these events are disjoint and exhaust the
sample space. Each event is measurable at that start, with no condition on
later coordinates. For any bounded g of this chain's history through j,
the conditional block-marginal calculation gives

    E[1_(E_(tau,l))*g*(f(A_(j+1))-R_t f(A_j))]=0.

Summing yields the conditional transition identity above, even though the
start events need not be measurable from this chain's history alone. This
also applies to a truncated final block since j<H. Induction proves the
ENTIRE individual path law, not merely state marginals or boundary laws.
Revealing endpoints in advance and then using them as decision information
inside the block would invalidate the argument; the committed rule avoids it.

## 6. Episode charging and every-symbol Hamming cost

Suppose a birth occurs on a matched one-step decision j->j+1. Charge the
born pair position j+1 once. Recovery then consists of committed three-step
attempts until the first matched decision boundary, or the horizon. Given
the history and born pair, each attempted full block fails to match endpoints
with conditional probability at most beta, uniformly in its starting states.
By induction, the probability that the r-th recovery attempt is started is
at most beta^(r-1). This uses fresh block coins, not independence of the
pair states at stopping times. Hence the conditional expected number of
attempts started is at most sum_(r>=0) beta^r=32.

Count a final partial block as a full3 for this upper bound. Its START is
preceded only by full failed blocks, so the same tail bound on starting it
applies. A born episode's total charged positions consequently have
conditional expectation at most

    1+3*32=97.                                        (9)

Intermediate equal pairs cost0 but may be overcharged until the commitment
ends. Each actual disagreement belongs to an episode: initial states match,
and a new disagreement outside recovery can only arise at a matched
one-step decision. Episodes need not have independent lengths.

Let I_j indicate that j is a matched one-step decision boundary and B_j
indicate its mismatch birth (both are0 when j is inside a committed block).
On the boundary event the maximal coupling gives birth probability h(A_j^+).
Taking conditional expectation there and setting the complement to0 yields
E B_j=E[I_j h(A_j^+)]. Therefore

    E B_j<=E h(A_j^+).

Use (9) AFTER conditioning on a birth and its actual born states; its bound
is uniform. The tower property and finite summation give

    E sum_(j=1)^H 1{A_j^+!=A_j^-}
       <=97 sum_(j=0)^(H-1) E B_j
       <=97 sum_(j=0)^(H-1) E h(A_j^+).                (10)

By the full marginal result and (6),(7), the difference from stationary
expectation is at most Delta times TV: apply 0<=h<=Delta separately to
the positive and negative parts of the zero-total-mass law difference.
Thus

    E h(A_j^+) <=2uDelta+Delta D_j,
    sum_(j=0)^(H-1) E h(A_j^+) <=2NuDelta+96Delta.     (11)

For each FREE symbol X_i, 1<=i<=N-2, its associated reversed pair is
A_(N-i-1)=S_(i+1), and its FIRST component is X_i. Equivalently the first
components of A_1,...,A_H are X_(N-2),...,X_1. Thus

    d_Ham(X^+,X^-)
      =sum_(j=1)^H 1{first(A_j^+)!=first(A_j^-)}
      <=sum_(j=1)^H 1{A_j^+!=A_j^-}.                   (12)

The last two symbols are both00. No free symbol, including X1, is missing
or counted using an endpoint-only proxy. Combining (10)–(12) supplies a
coupling Pi of the TWO TRUE CONDITIONAL HISTORY LAWS P,Q with cost

    C<=97(2Nu+96)Delta<=10000(1+Nu)Delta.              (13)

The last inequality compares coefficients: 194<=10000 and9312<=10000.
This proves the proposed path bridge with its original constants. No seed
replacement, clean oracle or weaker observation space is needed.

## 7. The global common observation channel

Take u=u0=k/N in the preceding construction, so Nu=k. From (1),(13),

    C<=10000(1+k)Delta=(1+k)/64<=k/32.                (14)

Use that CONDITIONAL coupling Pi in §§2–3 on the terminal00 fiber. It
produces one kernel K with TV(PK,QK)<=1/64 by (4),(14). Extend it to a
global T by identity on all other terminal fibers. Each row preserves its
tail and has support within k edits in the first N-2 bits. Every raw binary
input belongs to exactly one such fiber, including inputs unlikely for either
witness. Full support of D1 makes all conditional P,Q masses rational and
positive; mu=0 cases were explicitly given rows anyway.

The design is an offline finite function of PUBLIC N,k. All entries of
F_±,R_±,pi, the maximal couplings, common-atom endpoint distributions,
and positive-denominator bridges are rational at the fixed witness pair.
The adaptive sampling tree has finite depth (at most H blocks, with only
its last block possibly extending by two auxiliary positions). Summing
its finitely many rational branch weights gives a rational coupling of
complete histories. Enumerate the two rational conditional laws and this
fixed coupling, remove cycles/collapse paths using fixed lexicographic
choices, form the midpoint rows, and store them. All operations preserve
rationality. Take the least common multiple of the finitely many positive
row denominators, including the identity rows on other fibers, and realize
T with the independent uniform integer seed from section3. This enumerates
a finite globally defined input/seed function without an average-only
legality exception. A random seed then selects that ONE row at the
actual observed x. In particular T does NOT run the plus conditional
coupling when the true source is plus and the minus coupling otherwise.
The reverse coupling is only a device for computing a fixed transport table.
The residual sign mu(x) used to define the row is a fixed function of x,
not a read of the actual hidden source label. Publicly selecting u0=k/N for
a difficult subproblem is therefore different from providing hidden u to an
unknown-parameter predictor or choosing source-dependent private coins.

The same T is legal when any other D1 u,t happens to generate the input;
only its bad-risk guarantee is restricted to the pair (1). T is independent
of Q and every post-observation encoder/predictor. Its private finite seed
is independent of the source and not disclosed. The observation-law TV
bound is for Z marginalized over that seed; no claim is made that it holds
conditional on each seed, or that a deterministic common attack attains it.

Since T preserves S_N, the actual conditional observed laws given S_N=00
are EXACTLY PK and QK. We have not asserted small unconditional history TV,
conditioned on independent queries, or replaced the true terminal pair.
Y=X_(N+1) was never observed. By D1's second-order Markov property,
Pr(Y=1 | X_1^N,channel coins,predictor coins)=p_(u,t)(1|S_N).
The preserved S_N is a function of Z; conditioning further down to Z
therefore leaves this same target. In particular on the actual event
S_N=00 the target is Bernoulli(t). The risk definitions used below are
R_00=E[kl(t,q1)|S_N=00] and
R_av=E[KL(p_(u,t)(.|S_N)||q)], including both independent private coins.
This is exactly the D1 excess log-loss experiment.

## 8. Arbitrary full-Z randomized predictors and the same witness

Fix any common randomized predictor from Z,N,k,Q to q=(1-q1,q1). Its fresh
private randomization is a common Markov kernel and cannot increase TV.
Even prior knowledge of T and the public witness pair could be supplied
without weakening the following bound. Threshold q1 at1/2 to test plus
against minus. On a testing mistake, |q1-t|>=Delta/2. For Bernoulli laws,
kl(t,q)>=2(t-q)²: integrate derivative (q-t)/(q(1-q)) and use q(1-q)<=1/4.
At q=0 or1 the interior target has infinite KL, so endpoints cause no gap.
Each mistake costs at least Delta²/2.

Let L_- and L_+ denote the two actual conditional Z laws. For any randomized
test with plus-decision probability a(z) in[0,1],

    err_-+err_+=1-[integral a dL_+-integral a dL_-]
              >=1-TV(L_-,L_+)>=63/64.

Indeed sum_z a(z)(L_+(z)-L_-(z)) is at most the positive Jordan mass
TV(L_-,L_+) because 0<=a<=1. This also proves the randomized testing
bound directly, without any restriction on the predictor's output format.
The unordered pair of laws is {PK,QK}. Hence

    max_(t=t_-,t_+) R_00
      >=(Delta²/4)(1-1/64)>=Delta²/8=c.                (15)

Choose one t_* attaining this two-element maximum. On that SAME source
and SAME T, nonnegativity of KL and stationarity yield

    R_av>=Pr(S_N=00)R_00=u0 R_00>=c k/N.              (16)

This proves (2) for all full-Z predictors, including all encoders, infinite
computation and unrestricted probability outputs. It does not say every
source suffers (2), every admissible attack is bad, the terminal query can be
changed, or old fixed-FULL19 results imply this lower. Exact input loss
occurs before every encoder, so later re-encoding/locked-output tricks
cannot restore an unobserved clean history. The strongest comparison
baseline here is expressly allowed to use every observed Z symbol.

## 9. Dependency and scope certificate

Every load-bearing lemma is proved in sections2-8 from D1-D2. Section4
establishes the source and mixing calculations directly; section5 proves
full-path marginals rather than only endpoints. All N,k in the exact C2
domain are covered. No property of D3-D5 is needed for this stronger lower.
The conclusion applies to DIRECT, JOINT, and every other full-Z randomized
predictor, even unlimited ones. Their finite implementation/cost properties
remain separate current-project obligations.

For root integration the quantifiers are

    for every legal (N,k>=1), exists one T_(N,k),
    for every Q and every common full-Z predictor A,
    exists t_* in {t_-,t_+} with BOTH inequalities(2).

The one channel is globally hard-k for every binary input and every seed,
fixed before A and independent of Q and the actual source label. The TV
and risk bounds average its private seed. No all-source bad-risk statement,
deterministic-channel attainment, small unconditional history TV, matched
1/N or 1/Q lower, JOINT superiority, novelty, or all-layer/IEEE/sensor
conclusion follows. The separate d6-scope-map-v1.md gives the exact bounded
primary/strong-DIRECT mapping; it is scope provenance, not a premise here.

Prior diagnostic code/results were not rerun and are not proof dependencies.
GPU work is0. The research policy limits GPU to0, so the reserved GPU
quantity for final audit is0 as well; the remaining dimensions are unlimited.
The current C2 proof will use the normal truth gateway with predecessors=[];
only its actual returned verdict and identifiers establish admission.
