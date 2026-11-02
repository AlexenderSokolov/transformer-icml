# Exact conditional statistical root: self-contained proof v1

2026-10-27. Author proof.
Obligation: a92235561a82e3ac845de304718b82c944869ccc236c5d248be1f24b25cdac3b.
Contract: e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af.
Submission predecessors: [] (no old or new Fact is used as a premise).

## 0. Claim, scope and proof organization

We prove the exact conditional conjunction G1–G6, the statistical transfer
part of G7, U1/UC/U2. For every integer K>=2, fix an arbitrary common
deterministic finite predictor family F satisfying the all-path predicate I
below. All upper statements concern this same F. The information lower
bounds separately quantify every common possibly randomized full-history
predictor and do not assume I. Initial laws and zero transition coordinates
are unrestricted. A source is time homogeneous within each experiment.
Sourcewise limits fix K,theta,mu; a supremum at each N may select different
theta,mu. No fixed-source witness is inferred from a changing-source bound.

Sections 3–4 prove G1; §§5–6 prove G4 and the finite-chain prerequisites;
§7 proves G2; §8 proves G3 for every allowed periodic residue; §9 proves G5;
Appendix A proves G6 with all the original Counter tables separately;
§10 proves exactly the conditional statistical transfer in G7;
§§11–13 prove U1/UC/U2. Section numbers 3–8 preserve the source proof's
internal dependency order. Every mathematical argument needed is included
here. In the proof, a reference to an example means the complete example in
Appendix A, not an external file or old review verdict.

This text extracts and adapts the fixed G/U author proofs and Counter tables
listed in the accompanying manifest. The two old independent file reviews
were read to preserve their quantifier and dependency checks. Their PASS
labels and all old Fact identifiers are provenance, not premises. No claim
about realization or costs of the concrete Pi is admitted by this proof.

## 1. Source, observation, counts and all risk conventions

Let A={0,...,K-1}, S=A², D=K². Fix theta in the full product of K-simplexes
indexed by S and mu in Delta(S). Starting with (X_1,X_2)~mu, the conditional
law of X_(j+3) given X_1,...,X_(j+2) is theta_(X_(j+1),X_(j+2)). Thus

    Y_j=(X_(j+1),X_(j+2)),
    P((a,b),(b,c))=theta_(a,b)(c),
    N>=3, M=N-2>=1, E_N=Y_M,
    n_s(M)=sum_(j=0)^(M-1) 1{Y_j=s},
    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},
    p_N^+(c|s)=(C_s,c(M)+1)/(n_s(M)+K).

All other pair transitions are zero. The last counted successor is X_N;
Y_M is not another departure and X_(N+1) is not observed. At arbitrary
pair horizon m>=0 use the same counts with m in place of M. Let
G_j=sigma(X_1,...,X_(j+2)) and H_N=G_M. The predictor receives only the
complete observed history, declared query s and public K,N,h. Actual query
is the observed endpoint E_N. theta,mu, support, closed classes, stationary
laws, future stacks and hidden source labels are not inputs. A common
randomized algorithm in a lower bound may also have an independent random
seed with the same law in all sources.

TV(p,q)=(1/2)sum_c|p_c-q_c|. We use the source proofs' convenient aliases

    R_N(s)=TV(F_(K,N,h)(X_1^N;s),theta_s) [root notation Z_N(s)],
    Z_N=R_N(E_N) [root notation Z_N(E_N)],
    p_N(s)=P(E_N=s)=mu P^M(s), R_act=E Z_N.

Fixed risk is E R_N(s) for a specified public s; all risk is E max_s R_N(s).
Conditional risk E[Z_N|E_N=s] is defined only if p_N(s)>0. For H_N-measurable
simplex weights w_s the weighted risk is E sum_s w_s R_N(s); empirical
weights are w_s=n_s/M. No independent-query experiment is substituted.
All outputs and losses used in upper bounds are in a simplex and [0,1].
Write u_s=n_s/M and C_s(B)=sum_(c in B)C_s,c; theta_s(B) is defined likewise.
delta_c denotes the point mass at symbol c. U=U_K denotes the uniform K-vector
when used as a probability vector; the
different scalar U_K(M,Q) in §13 is explicitly a risk-bound function.
All unmarked logarithms are natural; log2 in a precision ceiling is base 2.
In §7, L_s is the limiting loss (root notation ell_s); total final visits
are always denoted n_s(infinity). In §6, the Poisson solution is called
g_s and its right-hand side f_s; the root calls that solution f_s instead.

## 2. The antecedent I and the common precision schedule

For every alphabetic history x_1^N, every s and every integer

    h>=h_0(M)=max(4,ceil(log2 M)+1), Q=2^h,

assume F outputs a probability vector and satisfies

    TV(F_(K,N,h)(x_1^N;s),p_N^+(s))
      <=r_h(n_s):=78KM/[Q(n_s+K)]+(K-1)/Q.             (I)

This is a deterministic antecedent, including histories having probability
zero under any particular theta and including n_s=0. We do not prove I for
Pi, assume it for an arbitrary comparator, or infer any implementation cost
from it. By reverse triangle inequality, for every history,

    |R_N(s)-TV(p_N^+(s),theta_s)|<=r_h(n_s).

Use the same public schedule for all asymptotic G claims:

    h_N=ceil(log2(128(K+1)(N+1)^3)), e_N=(N+1)^(-2).

It is legal: 128(K+1)(N+1)^3>=16 and exceeds 2^(ceil(log2 M)+1).
Since n_s+K>=K and 78M+K-1<=128(K+1)(N+1),

    max_s TV(F_(K,N,h_N)(s),p_N^+(s))
       <=(78M+K-1)/2^h_N<=e_N.                        (II)

Consequently all row, maximum, weighted, actual and positive-event
conditional risks of F differ from their ideal add-one versions by at most
e_N. For the last assertion average a pointwise inequality on that event;
no division of e_N by the event probability is needed. This differs from
conditioning a high-probability statistical event, which does incur its
failure mass divided by the conditioning probability. The schedule h_0
will be used only for the separately proved actual uniform bound in §13.

## 3. Finite visits: independent row stacks and one observed joint event

### 3.1 A valid construction without infinite-visit assumptions

On a proof probability space put independent arrays
xi_(s,r), s in S, r=1,2,..., each row iid with law theta_s, and independent
Y_0~mu. At time j, if Y_j=(a,b)=s has already been departed v_s(j) times,
take X_(j+3)=xi_(s,v_s(j)+1), and set Y_(j+1)=(b,X_(j+3)).

Here is a precise deferred-revelation argument. For any fixed finite
realized symbol history with positive probability, its row departure
counts and the sequence of inspected array indices are determined by that
history. The event specifying that history constrains only the inspected
prefix of each array and Y_0. Independence of product coordinates leaves
the next uninspected coordinate of the current row with law theta_s.
Partitioning on finite histories proves the same conditional law given
G_j. Induction therefore gives the exact finite-dimensional source law in
§1. Zero-probability histories cause no conditioning claim. A row is allowed
never to be visited or to have only finitely many departures.

For the actual finite history, its n_s successors are exactly the first n_s
entries of row s's stack. This is a pathwise identity. The statement
"the first r stack entries are iid" is unconditional; we do NOT say they
are iid conditional on n_s=r or on eventual return. All stacks are proof
variables only; no such stack, source parameter or future value is exposed
to the network.

### 3.2 The elementary exponential inequality

If a conditionally centered random variable D has conditional range length
at most H, then

    E[exp(lambda D)|past] <= exp(lambda² H²/8).             (MGF)

For a fixed distribution on [a,b], the second derivative of its log-mgf is
the variance under exponential tilting. That variance is <=(b-a)²/4:
the mean minimizes E(V-c)² and the midpoint gives this bound. Integrate
the derivative bound twice from zero, using centering, to obtain (MGF),
for either sign of lambda. It applies conditionally to each distribution.
Iteration and exponential Markov give for m such martingale differences

    P(|sum D_i|>=x) <=2 exp(-2x²/(m H²)), H>0.             (H)

This includes iid Bernoulli indicators with H=1. The zero-range case is
deterministic and is treated without division by zero.

### 3.3 The simultaneous TV event, including empty rows

Let

    A_alpha=K log 2+log(2K²M/alpha),
    t_alpha(r)=sqrt(A_alpha/(2r)), r>=1.

For each s, r=1,...,M and subset B of A, apply (H) to
1{xi_(s,l) in B}-theta_s(B), l=1,...,r. A two-sided violation of
t_alpha(r) has probability at most 2 exp(-A_alpha). Union over K² M 2^K
choices gives total at most alpha. This is an unconditional union at
deterministic stack lengths; it remains valid when only a finite prefix
of a stack is ever revealed by the source.

Define V_alpha to be the event, in H_N, that simultaneously for all n_s>0
and B subset A,

    |C_s(B)/n_s-theta_s(B)| <=t_alpha(n_s).

Its failure is contained in that stack union, so P(V_alpha)>=1-alpha.
On a finite alphabet TV(p,q)=max_B |p(B)-q(B)|: choose B containing
precisely the positive coordinates of p-q; its mass is half the L1 norm.
Thus the same V_alpha controls all empirical row TVs, and also

    |C_s(B)/M-u_s theta_s(B)|<=u_s t_alpha(n_s).            (J)

At n_s=0 both terms on the left are zero; define the right of (J) to be
zero, without defining C_s/n_s or t_alpha(0). The event is a statement
about observed counts and is measurable in H_N. Using unrevealed proof
stacks for a probability bound does not turn it into a future-data event.

For r>0 add-one is r/(r+K) times the empirical row plus K/(r+K) times
the uniform vector U. Since TV(empirical,U)<=1-1/K (check vertices and
use convexity), its distance to the empirical row is <=(K-1)/(r+K).
Together with (I) and the triangle inequality this gives, on V_alpha,

    R_N(s)<=g_(N,h,alpha)(n_s) for every s,                (V)
    g(r)=min{1,t_alpha(r)+(K-1)/(r+K)
                     +78KM/[Q(r+K)]+(K-1)/Q}, r>=1,
    g(0)=1.

All positive terms decrease with r; with this definition g is nonincreasing
on {0,...,M}. No division by an empirical zero count is performed. No claim
of independence between n_s, the terminal state, heads or successors is
used. No new statistical head or exponential-size subset table is created.

If an occupancy event additionally bounds |u_s-v_s|<=a_s for specified
numbers v_s, (J) gives the SAME-event joint bound

    |C_s(B)/M-v_s theta_s(B)|<=u_s t_alpha(n_s)+a_s.


## 4. Risk transfers with the exact nonstationary denominator

Since 0<=R_N(s)<=1, splitting the SAME V_alpha proves

    E R_N(s) <=min(1,E g(n_s)+alpha),
    E max_s R_N(s) <=min(1,E max_s g(n_s)+alpha),
    E Z_N <=min(1,E g(n_(E_N))+alpha),                    (R)
    E[Z_N|E_N=s] <=min(1,E[g(n_s)|E_N=s]+alpha/p_N(s))
                                         when p_N(s)>0.

Likewise E sum_s w_s R_N(s)<=min(1,E sum_s w_s g(n_s)+alpha)
for ANY H_N-measurable simplex weights, including n_s/M and the point
mass at the actual endpoint. If a deterministic query subset S0 is used,
take maxima over that subset; no row outside S is silently deleted from
a claim stated for all K² rows. The conditional estimate follows from
P(V_alpha^c and E_N=s)<=alpha, not from independence.

Useful occupancy forms, for an integer v>=1, are

    E R_N(s)<=min(1,g(v)+alpha+P(n_s<v)),
    E max_(s in S0)R_N(s)
       <=min(1,g(v)+alpha+P(min_(s in S0)n_s<v)),
    E Z_N<=min(1,g(v)+alpha+P(n_(E_N)<v)),                 (RV)
    E[Z_N|E_N=s]
       <=min(1,g(v)+[alpha+P(E_N=s,n_s<v)]/p_N(s)).       (RC)

For example (RC) follows by restricting first to E_N=s and the intersection
V_alpha intersect {n_s>=v}; the complementary mass is at most
alpha+P(E_N=s,n_s<v). The latter joint mass can be much smaller than
P(n_s<v). Unequal row thresholds v_s can be used on the same event, with
their own g(v_s), and a maximum only where a maximum is actually desired.

Thus a valid sufficient finite-N-to-asymptotic conditional interface is
g_N(v_N)->0 and [alpha_N+P(E_N=s,n_s<v_N)]/p_N(s)->0.
This is a sufficient interface, not a necessary condition. The mere fact
p_N(s)->0 neither proves failure nor proves consistency; Appendix A gives both
behaviors for transient conditioning events.

## 5. Absorption and a nonstationary block-visit interface

### 5.1 Finite graph and absorption tail

In the directed graph of positive entries of P, mutual reachability
partitions the vertices into strongly connected components. Its quotient
has no directed cycles: such a cycle would merge its components. Following
outgoing edges in this finite acyclic quotient reaches a sink. A sink
component is closed and irreducible; write R for the union of all such
classes. Every state therefore has a path to R, with repeated vertices
removed to give length at most D-1.

There is at least one positive edge in each stochastic row, and finitely
many edges, so

    p_*=min{P(x,y):P(x,y)>0}>0.

This is a source-specific proof quantity; it may be arbitrarily small over
the full class. Put tau=inf{j>=0:Y_j in R}. From any starting state the
chance of reaching R within the next D steps is at least a0=p_*^D: use
one of the preceding paths, whose probability is at least p_*^D since
its length is <=D-1 and p_*<=1. At times 0,D,2D,..., condition on G_j
on the event of not yet being absorbed. Induction yields, for integer b>=0,

    eta_mu(b):=P_mu(tau>b)<=(1-a0)^floor(b/D).             (T)

The zero-block product is 1, including 0^0 when a0=1. If mu is already
supported on R, eta_mu(b)=0 exactly. Since the right tends to zero, tau
is finite almost surely. Once reached, a closed class cannot be left;
denote it C_infty. It is measurable as the class of Y_tau. No uniqueness
of the whole-chain stationary law has been used.

For later use, the Markov property at an a.s. finite stopping time follows
directly by partitioning {tau=t} in G_t and applying the finite-history
Markov property at each t, then summing. This justifies conditioning on
the random entrance without assuming a law for its state or its time.

### 5.2 General closed-class (L,a) assumption and its universal instance

An (L_C,a_C) visit certificate for a closed class C means an integer L_C>=1
and 0<a_C<=1 such that

    inf_(x in C) P_x(exists j in {0,...,L_C-1}:Y_j=s)
        >=a_C, for every s in C.                         (LC)

The block has L_C STATES and counts its first state. This convention is
essential for the last block to fit among departure indices 0,...,M-1.
For every class the universal choice is

    L_C=D,       a_C=p_*^(D-1).

Indeed a simple within-class path from x to s has length at most |C|-1
<=D-1; when x=s its length is zero and success probability is one.
Periodicity does not obstruct hitting during a block, even though it can
obstruct a transition to s at an exact prescribed time. One may instead
use better certified class-specific pairs or a common pair (L,a) valid
for all reachable closed classes.

Fix integers 0<=b<M and a common (L,a). Put

    B=floor((M-b)/L),       v=floor(a B/2).

We use the bound only when v>=1; otherwise (RV) is replaced by risk<=1.
On {tau<=b}, C=C(Y_b) is G_b-measurable. For fixed s in this C define
J_i to be the indicator of a visit to s in

    Y_(b+iL),...,Y_(b+(i+1)L-1), i=0,...,B-1.

The block start is r_i=b+iL. Conditional on G_(r_i), its success
probability is at least a by (LC), since Y_(r_i) is in C. All earlier
J's are G_(r_i)-measurable: their last inspected index is at most r_i-1.
Thus, on {tau<=b}, iterated conditioning gives

    E[exp(-lambda sum_i J_i)|G_b]
         <=(1-a+a exp(-lambda))^B, lambda>0.             (BM)

One can formalize the conditional assertion by fixing each G_b atom with
Y_b in R, then taking its known class and its finitely many s's. We never
condition on a future terminal state or on the event of a particular
eventual class before that class is G_b-known.

At lambda=log 2, exponential Markov and log(1-a/2)<=-a/2 yield

    P(sum J_i<=a B/2|G_b)
       <=exp(-a B(1-log 2)/2)<=exp(-a B/8).              (BT)

Here log 2<3/4. Distinct nonoverlapping blocks give distinct counted
departure indices and their last index is b+BL-1<=M-1. Hence
n_s>=sum J_i, regardless of visits before b or in the omitted final
partial block. If n_s<v=floor(a B/2), then sum J_i<=a B/2.
The floor is conservative; no claim of an unrounded threshold is needed.
Union over at most D states in the G_b-known class, then add absorption
failure, to obtain the precisely defined event bound

    P({tau>b} union
      {tau<=b and min_(s in C(Y_b)) n_s<v})
        <= eta_mu(b)+D exp(-a B/8).                     (B)

C(Y_b) in the second set is used ONLY on tau<=b. There is no minimum
over a nonexistent closed class on its complement. One may cap the right
at 1. Since E_N=Y_M lies in the same closed class on tau<=b, (B) implies

    E Z_N <= min(1,g(v)+alpha+eta_mu(b)+D exp(-a B/8)).   (F)

On its good event it also controls the maximum over C_infty, which equals
C(Y_b) there. It does not control a full K² maximum if other rows exist.
If the initial distribution is inside one closed class C, take b=0 and
replace D by |C|, eta=0, to control max_C. For full irreducibility C=S
this is the stated full-query target with arbitrary initial mu.

For class-specific certificates, condition on {tau<=b,C(Y_b)=C}; use
B_C=floor((M-b)/L_C), v_C=floor(a_C B_C/2) and |C| in (BT).
For example whenever all reachable v_C>=1 the terminal bound is

    E Z_N <= min(1, alpha+eta_mu(b)
       +sum_C P(tau<=b,C(Y_b)=C)
                    [g(v_C)+|C| exp(-a_C B_C/8)]).       (FC)

This conditioning is legitimate because the event is G_b-measurable.
It keeps initial absorption and different class visit difficulties separate.
The universal parameters prove a finite bound for every fixed theta.
With b=floor(M/2), alpha=N^(-2), h=h_N, B grows linearly and so does v
eventually; eta and block failures vanish exponentially while g(v)->0.
This block argument alone gives no common rate over tables with arbitrarily small p_*; §§11–13 prove a different uniform actual bound.

## 6. Poisson linear algebra, periodic chains, and the initial boundary

### 6.1 Existence without a mixing or reversibility hypothesis

Restrict P to a finite closed irreducible class C. A stationary probability
pi exists: Cesaro averages m^(-1) sum_(j=0)^(m-1) nu P^j have a convergent
subsequence in the compact simplex, and their stationarity defect is
(nu P^m-nu)/m, which tends to zero. Every coordinate of pi is positive:
some pi_x>0; for any y a positive path x->y of length l gives
pi_y=(pi P^l)_y>=pi_x P^l(x,y)>0.

If Pg=g for a real vector g, choose a maximum coordinate. A convex
combination equals that maximum only if each positive-probability successor
has the same value. Propagate along positive paths to prove g constant.
Thus ker(I-P) is one-dimensional and rank(I-P)=|C|-1. Its image lies in
{f:pi f=0}; this hyperplane has the same dimension, hence is exactly its
image. The left nullspace also has dimension one, which proves uniqueness
of the normalized stationary pi. Therefore, for

    f_s(x)=1{x=s}-pi_s,

there exists a finite real g_s satisfying (I-P)g_s=f_s. No infinite series
sum P^j f_s is used. Periodic P is allowed. Subtract a constant to arrange
min g_s=0 and set H_s=max g_s-min g_s<infinity.

### 6.2 Explicit finite-horizon boundary and tail

For any starting distribution nu on C and m>=1 state observations, the
telescoping identity is

    sum_(j=0)^(m-1)(1{Y_j=s}-pi_s)
      =g_s(Y_0)-g_s(Y_m)+sum_(j=0)^(m-1) D_(j+1),
    D_(j+1)=g_s(Y_(j+1))-P g_s(Y_j).                     (PI)

Each D is centered conditional on G_j and has conditional range length
at most H_s. The boundary has absolute value at most H_s. Hence for
H_s>0 and x>0,

    P_nu(|n_s(m)-m pi_s|>H_s+x)
          <=2 exp(-2x²/(m H_s²)),                       (P)
    E_nu n_s(m)-m pi_s =nu g_s-nu P^m g_s,
    |E_nu n_s(m)-m pi_s|<=H_s.                          (PB)

Equation (PB), rather than an assumption of zero bias, is the explicit
initial-distribution term. If H_s=0, then f_s=0, and the corresponding
count is exactly m pi_s; no zero denominator is used. A solution g_s
could be obtained by a finite linear solve with one normalization, but
it is an analysis parameter, not an additional network operation or input.

For arbitrary mu in the whole chain, fix b<M and condition on G_b on
tau<=b. Let m=M-b. Apply (PI) to Y_b,...,Y_M in its now known class C.
Writing n_post(s)=sum_(j=b)^(M-1)1{Y_j=s}, its initial boundary is exactly

    g_s^C(Y_b)-(P_C^m g_s^C)(Y_b)

in conditional expectation; its absolute value is <=H_s^C. This is a
uniform conditional bound, so integration over the entrance histories
is valid. The full counts satisfy n_s>=n_post(s). In particular on a
post-block deviation good event,

    n_s>=ceil(m pi_s^C-H_s^C-x_s).                       (PL)

Use a positive threshold only if this right side is positive. For a
two-sided comparison to M pi_s^C, the pre-b segment contributes
|sum_(j<b)(1{Y_j=s}-pi_s^C)|<=b; thus

    |n_s-M pi_s^C| <= b+H_s^C+x_s                        (PF)

outside the same post-block tail. The extra b must not be suppressed.
Union over s in C costs sum_s 2 exp(-2x_s²/(m(H_s^C)²)), treating H=0
deterministically, and unconditional absorption failure adds eta_mu(b).
These are alternative finite-N occupancy inputs for (RV)–(RC), valid
without stationary initialization or aperiodicity. Equivalently one may
condition on a finite tau and Y_tau by the stopping-time argument in §5;
then use m=M-tau where tau<M. This does not assume stationarity at entry.

For example if m pi_s^C/2>H_s^C, set x_s=m pi_s^C/2-H_s^C. The event
n_post(s)<floor(m pi_s^C/2) is bounded by the corresponding term of (P).
The strict inequality and floor make this implication valid at integer
thresholds too. These sufficient bounds are not sharp dependence claims.

## 7. Almost-sure, L1 and exact finite-row classification

For a fixed stack row and symbol, (H) gives

    P(|r^(-1)sum_(l<=r)1{xi_(s,l)=c}-theta_s(c)|>e)
          <=2 exp(-2r e²).

For each rational e>0 its sum over r is finite. The probability that such
events occur after any index r0 is at most their tail sum; letting r0 grow
shows that infinitely many violations have probability zero. Intersecting
countably many rational e and the finitely many s,c proves the stack strong
law simultaneously for ALL rows, including rows the actual path visits only
finitely often. We only evaluate that strong law along r=n_s when n_s
actually tends to infinity.

Within any closed class, (P) likewise implies n_s(m)/m->pi_s>0 almost
surely for every s. For example for m>=2H_s/e, a deviation >m e has
probability <=2 exp(-m e²/(2H_s²)); the same summability argument applies.
For H_s=0 the assertion is deterministic. There are finitely many starting
states and classes. Conditional on each {tau=t,Y_tau=x}, the future has
the corresponding within-class law; countably many t and finitely many x
show this probability-one result holds after the random entrance as well.

By (T), tau<infinity a.s. Consequently the visited class C_infty has
each n_s tending to infinity, whereas every s outside C_infty has only
finitely many departures (all before tau). On the common probability-one
stack event, for s in C_infty,

    C_s/n_s ->theta_s,     p_N^+(s)->theta_s.

Since K² is finite, taking the maximum over the random but eventually
identified C_infty and using (II) proves

    H_N^C:=max_(s in C_infty) R_N(s)->0 a.s. and in L1.   (CL)

L1 follows directly from boundedness: for 0<=V_N<=1 converging a.s. to
zero, E V_N<=e+P(V_N>e); the latter probability tends to zero by the same
event-tail argument, and e can decrease to zero. For all sufficiently
large N, E_N is in C_infty, so Z_N<=H_N^C. Thus

    Z_N->0 a.s.,                 E Z_N->0.              (AE)

The empirical-frequency-weighted error also vanishes: its within-class
part is at most H_N^C, and its outside-class part is at most the number
of pre-tau departures divided by M, which tends to zero. Arbitrary
history-dependent weights retain the finite-N transfer in §4, but their
convergence requires control of their mass on finite-visit inaccurate
rows; arbitrary weights do not automatically concentrate on C_infty.

There is also an exact description of what survives on such rows. Put
n_s(infinity)=sum_(j>=0)1{Y_j=s}. On {s notin C_infty} it is finite,
as are the corresponding C_s,c(infinity), and the counts are eventually
constant. Define the random limiting error

    L_s=0,                                          s in C_infty;
    L_s=TV((C_s(infinity)+1)/(n_s(infinity)+K),theta_s),
                                                    s notin C_infty.

Then for every s simultaneously,

    R_N(s)->L_s a.s.,       E R_N(s)->E L_s,
    max_(s in S0)R_N(s)->max_(s in S0)L_s a.s. and in L1. (FL)

Here the expectation convergence follows by applying bounded convergence
to the difference from the limit. Thus for this particular theta,mu and
family F, max_S0 a.s. consistency, L1 consistency, and the condition

    P(for all s in S0\C_infty:
       (C_s(infinity)+1)/(n_s(infinity)+K)=theta_s)=1     (EX)

are equivalent. This is an exact probabilistic characterization, not an
algorithm which knows future visit counts. The sufficient coverage
condition P(S0 subset C_infty)=1 makes (EX) vacuous. If a finite-visit
row theta_s has a zero coordinate, its finite add-one vector is strictly
positive, so it cannot satisfy that equality. For other rows accidental
equality is possible, as Appendix A, E2 shows.

Full pair-chain irreducibility makes C_infty=S deterministically and
recovers the full K² maximum for every initial law. For a fixed
s, P(s in C_infty)=1 is sufficient. With multiple possible classes,
P(s in C_infty)>0 alone is not sufficient for unconditional E R_N(s)->0.
The next section proves conditional-terminal consistency for any reachable
recurrent s despite exactly that distinction.

## 8. Periodic recurrent states: a genuine eventual denominator lower bound

### 8.1 Elementary periodic skeleton proof

Let C be a finite closed irreducible class, and fix o in C. Let T_o be
the set of positive lengths of positive-probability walks o->o. It is
nonempty and closed under addition by concatenation. Put d=gcd T_o.
A finite subset of return lengths has this gcd: successively adjoining
lengths strictly decreases a positive integer gcd until it stabilizes.

We use the following elementary integer lemma. If positive integers
a_1,...,a_k have gcd one, their nonnegative integer combinations contain
all sufficiently large integers. Indeed their generated residues modulo
a_1 form an additive subsemigroup of the finite group Z/a_1. Every such
subsemigroup containing zero is a subgroup, since the additive inverse
of any element is a nonnegative multiple of it. The gcd assumption makes
this subgroup the whole group. Choose one nonnegative combination b_r
in each residue r. Every integer n>=max b_r in that residue equals
b_r+t a_1 for t>=0, proving the lemma. Apply it to a finite set of
return lengths divided by d. By concatenation,

    all sufficiently large multiples of d belong to T_o. (SL)

For any v in C, all positive walks o->v have the same length modulo d:
append a fixed path v->o to two of them, producing two returns whose
length difference is divisible by d. Assign v that residue r(v). Every
positive edge increments r by one modulo d. Every residue occurs, since
a positive return walk of length a positive multiple of d traverses all
d residues. Write C_0,...,C_(d-1) for the residue classes, with o in C_0.
Transitions run C_r to C_(r+1). Invariance of pi therefore gives
pi(C_r)=1/d, and d pi restricted to C_r is stationary for P^d there.

For v,w in C_0 choose positive paths v->o and o->w. Their lengths are
both divisible by d (append an o->v path to the first if needed to see
this). Insert at o any sufficiently large multiple-of-d return from
(SL). Consequently, for every sufficiently large q,

    P^(qd)(v,w)>0.

There are finitely many v,w, so one q0 works for every pair. The same
argument with matching residues works on every C_r. Thus R=(P^d)|C_0
is stochastic and a power R^q0 is strictly positive. In particular the
skeleton is irreducible and aperiodic; these are conclusions of the graph
argument, not unstated hypotheses.

For completeness, positivity supplies the needed convergence. Let m0=|C_0|,
delta=min_(v,w in C_0)R^q0(v,w)>0 and e=m0 delta<=1. Every row of
R^q0 is e times uniform plus (1-e) times a stochastic residual. A stochastic
kernel contracts TV: write the signed input difference as positive and
negative masses, or use the subset formula. Thus for any two input laws
the q0-step TV distance contracts by 1-e. If e=1 convergence after q0
steps is exact. Since the stationary law is rho(w)=d pi_w on C_0,
iteration and the remaining fewer than q0 steps give R^q(o,.)->rho.
In particular, taking o=s if desired,

    P^(qd)(s,s)->d pi_s>0.                              (RET)

This proof supplies precisely the periodic skeleton limit used below.
It never claims that the original periodic P^m converges in TV.

### 8.2 Arbitrary initial distribution and all reachable residues

Let s be a recurrent state reachable from mu, meaning it lies in a closed
irreducible class C and mu P^m(s)>0 for some finite m>=0. Choose o=s
in the preceding construction, and define

    J_s={r in {0,...,d-1}: exists m>=0,
                          m=r mod d and mu P^m(s)>0}.

For each r in this nonempty finite set choose ONE such m_r and let
q_r=mu P^(m_r)(s)>0. These are fixed early-time witnesses, not a bound
conditioned on a random future entrance. For all integers l>=0,

    mu P^(m_r+ld)(s) >= q_r P^(ld)(s,s).                 (ENT)

This is the ordinary Markov law at deterministic time m_r, restricted to
the event Y_(m_r)=s. Subsequent transitions stay in the closed class.
Other entrance histories add nonnegative probability and cannot destroy
this lower bound. It therefore covers multiple entrances and arbitrary
random entrance times without needing a common entrance residue.

By (RET), choose l0 so P^(ld)(s,s)>=d pi_s/2 for all l>=l0. Set

    M_s=max_(r in J_s) m_r+d l0,
    c_s=(d pi_s/2) min_(r in J_s) q_r>0.

If M>=M_s and mu P^M(s)>0, its residue r belongs to J_s by definition.
Then M=m_r+ld for an integer l>=l0, and (ENT) proves

    p_(M+2)(s)=mu P^M(s)>=c_s.                          (DEN)

Conversely for M>=M_s every residue in J_s has positive probability by
that same inequality. Residues outside J_s have zero probability at ALL
times, by their definition. Thus the eventual support and denominator
claim include exactly the allowed periodic times; they do not assign a
conditional expectation on a null event.

Finally, nonnegative loss gives for any p_N(s)>0

    E[Z_N|E_N=s]=E[Z_N 1{E_N=s}]/p_N(s)
                   <=E Z_N/p_N(s).

Use (AE) and (DEN) to obtain conditional terminal mean consistency along
every sufficiently large allowed N. Crucially, the numerator is E Z_N.
Neither E max_all_rows R_N nor E R_N(s) is asserted to tend to zero on
paths absorbed into other classes; Appendix A, E5 demonstrates that they need not.


## 9. G5: full-query consistency for every initial law iff irreducibility

**Claim U.** If the pair chain has at least two closed irreducible classes,
then for every supported finite history and every N>=3,

    max_(s in A²) TV(p_N^+(s),theta_s)>=1/K,
    max_(s in A²) R_N(s)>=1/K-e_N.                      (U)

Proof. A path can visit at most one closed class. Choose another closed
class C, which is never visited along this history; every row in C has
n_s=0. C is a proper subset of A². Some s in C has a forbidden next symbol:
otherwise, from any (a,b) in C, closure under all K successors gives all
(b,c) in C, and a second step gives all (c,d) in C, forcing C=A². At a
forbidden symbol theta_s(c)=0 but p_N^+(c|s)=1/K. Hence TV(U_K,theta_s)
>=1/K, proving the first assertion. Equation(I) proves the second.
The query s may depend on the path, as a maximum explicitly permits. This
is not a lower bound for its ACTUAL terminal query.

For a finite chain, stationary laws are exactly mixtures of the stationary
laws of its closed irreducible classes. Here is sufficient justification:
Cesaro averages give a stationary law in each class: their stationarity
defect is (nu P^m-nu)/m, tending to zero, and the finite simplex is compact.
If Pg=g, a maximum of g can average to that maximum only when every positive
successor has that value; irreducibility propagates it throughout the class.
Thus ker(I-P) consists of constants. Rank gives a one-dimensional left
nullspace and hence uniqueness of its stationary probability. Its positive
mass at some x propagates by invariance along a positive path to every y,
so every coordinate is positive. A stationary law has
no transient mass, since invariance and the absorption tail force that
mass to tend to zero. Distinct classes give disjoint stationary laws.
Consequently a unique whole-chain stationary law is NECESSARY for the
full-K² consistency of F, at any initial law. It is not
sufficient: E3 has a unique stationary law and fails at a transient row.
This is a genuine property of this decoder/default, not a necessary
condition for every possible algorithm to be correct at some one source.

A further quantifier refinement is useful. For a GIVEN theta, F
full-K² consistency for EVERY initial mu holds iff its pair chain is
irreducible. Sufficiency follows from §7. For necessity, multiple classes
are excluded by the displayed structural bound (U). With one proper closed class C, if a row outside C is
nonuniform, initialization inside C never observes it and fails. If every
outside row is uniform, start at some outside s. A positive simple path
from s to C has no return to s. On that positive-probability event n_s(infinity)=1,
so the add-one limit has a coordinate 2/(K+1) and the other coordinates
1/(K+1), different from U_K. Equation(FL) then excludes consistency.
For ONE prescribed mu, irreducibility is not necessary (E2).


## 10. G7: exactly the statistical transfer and its boundary

An executed common deterministic program, including its output and its
execution cost on a fixed history/query/public precision, does not depend
on the probability measure later assigned to that history. Thus, if a
separate normal proof establishes the concrete Pi's legal simplex output
and I on every path, this theorem instantiates to that very Pi. Nothing
about its existence, all-path implementation correctness, full cost ledger
or comparison with a strong direct baseline follows from I alone. Such
claims remain the independent SRC-Pi obligation.

The direct ideal add-one statistic satisfies all sampling parts of the
proof with implementation error zero. A finite direct procedure must still
pay for its data acquisition, counts, division/rounding and output. Its
statistical validity grants no free extra port to another program. The
original G7 and its complete source cost text are preserved unmodified in
the copied source package. Its current stage2 directory is
inputs/source-v10/inputs/general-assumptions-20261027/stage2/.
No statement in this proof infers Pi's costs from the conditional family F.

## 11. U1/UC: uniform terminal occupancy and a vanishing risk modulus

### 11.1 Suffix domination, first-v charging and the exact K^4 bound

For any fixed homogeneous pair kernel P, integer v>=1 and m>=0 define

    b_(m,v)(y)=P_y(n_(Y_m)(m)<v),
    B_(m,v)(P)=max_y b_(m,v)(y),
    beta_(K,v)(m)=sup_theta B_(m,v)(P_theta).

For m>=l>=0, full counts dominate the last l departure counts for the
same random endpoint Y_m. Given G_(m-l), the suffix is a length-l chain
with kernel P started at the known Y_(m-l). Therefore

    b_(m,v)(y)<=E_y b_(l,v)(Y_(m-l))<=B_(l,v)(P),
    B_(m,v)(P)<=B_(l,v)(P).                            (MON)

This uses no conditioning on Y_m, stationarity or reverse kernel. At m=0
the counts vanish, so B_(0,v)=beta_(K,v)(0)=1. Taking max over starting
states bounds any initial law by convexity. Individual b need not decrease:
the full K=2 table 00:(1/2,1/2),01:delta_1,10:delta_0,11:delta_1 has
b_(1,1)(00)=1/2 and b_(2,1)(00)=3/4.

For any deterministic sequence in D states, the event n_(y_t)(t)<v marks
only the first v occurrences of its current state. Hence for every T

    sum_(t=0)^T 1{n_(y_t)(t)<v}<=Dv.                   (CH)

Take expectations separately for every initial y, and then use max<=sum:

    sum_(t=0)^m B_(t,v)(P)
       <=sum_y sum_(t=0)^m b_(t,v)(y)<=D²v.

By (MON), (m+1)B_(m,v)<=D²v, and consequently

    beta_(K,v)(m)<=min(1,K^4 v/(m+1)).                 (UC)

We did not exchange sum and max. For the preceding geometric table at v=1,
B_0=B_1=1, B_2=B_3=3/4 and B_m=(3/4)2^(-(m-3)) for m>=3, giving
sum_m B_m=17/4>4=Dv. The four initial states verify these values directly:
from 00 the endpoint is new only at exit or first absorption; from 10
there is one extra initial step, from 01 first absorption is at step 1,
and 11 is absorbing. For m>=2 the 10-start probability is the 00-start
probability at m-1. This also explains the extra factor in the safe proof.

### 11.2 The independent compactness proof, including degenerate tables

For fixed P, §5 gives finite a.s. entry into one closed class, and §7 gives
diverging counts at each state in that class. Thus n_(Y_m)(m)->infinity
a.s. and B_(m,v)(P)->0 for each fixed v (finitely many starting states).
Alternatively (CH) shows the indicator can be nonzero only finitely often
on any infinite path. For fixed m,v each b is a finite sum of products of
transition probabilities: the event is a fixed function of the finite
path, including paths with zero mass. Thus B is continuous on the entire
compact product Theta_K of closed simplices; no support stratum is removed.

For delta>0, at each theta choose m_theta with B_(m_theta,v)<delta/2.
Continuity gives a relative neighborhood on which it is <delta. Choose a
finite subcover of Theta_K and take the maximum of those m_theta. Equation
(MON) then implies B_(m,v)<delta uniformly for every larger m. Thus beta
tends to zero for fixed K,v, also proved explicitly by (UC). Both proofs
include reducible, periodic and zero-edge limit matrices.

### 11.3 Infinite row-stack tail, rho and risk quantifiers

The stacks in §3 are unconditionally iid at every deterministic length j.
Use its exponential bound and the subset formula for TV, now unioning over
all j>=v, all K² rows and 2^K subsets. For 0<epsilon<1 this gives

    P(exists s,j>=v: TV(empirical stack(s,j),theta_s)>epsilon)
       <=A_K(v,epsilon),
    A_K(v,epsilon)=min(1,
       2^(K+1)K² exp(-2v epsilon²)/(1-exp(-2epsilon²))). (A)

The sum is a geometric series. The infinite-stack event need not itself be
H_N-measurable; a violation in the actual observed finite prefix is contained
in it. Future entries are proof variables and are never counted as data.
On its good event and J=n_(Y_M)(M)>=v,

    TV(p_N^+(Y_M),theta_(Y_M))<=epsilon+(K-1)/(v+K).

Using TV<=1 on the two possibly correlated bad events gives, uniformly in
theta,mu, for 1<=v<=M,

    E TV(p_N^+(Y_M),theta_(Y_M))
       <=min(1,epsilon+(K-1)/(v+K)+A_K(v,epsilon)
                                             +beta_(K,v)(M)).

Define exactly

    rho_K(M)=min(1,inf_(1<=v<=M,0<epsilon<1)
      [epsilon+(K-1)/(v+K)+A_K(v,epsilon)+beta_(K,v)(M)]).

For increasing M every old v remains available and its beta is nonincreasing;
hence rho is nonincreasing. Given delta>0 choose epsilon<delta/3 first,
then fixed v with (K-1)/(v+K)+A_K(v,epsilon)<delta/3, then M>=v with
beta_(K,v)(M)<delta/3. Thus rho_K(M)->0. Taking the infimum in the bound and
then applying (II) yields

    sup_(theta,mu) R_act(F_(h_N))<=min(1,rho_K(M)+e_N).  (U1)

For each fixed t>0, Markov's inequality bounds the corresponding supremum
of P(Z_N>t) by (rho+e_N)/t. This proves fixed-K uniform mean and uniform
in-probability consistency. It supplies no common a.s. event for a sequence
of changing-source experiments, and does not make fixed/all/conditional
risks uniformly consistent. Appendix A's contrary witnesses remain valid.

## 12. Computability of the defined beta and rho to any rational error

For denominator L, enumerate every K-simplex rational grid in each row.
Every row theta_s is within TV (K-1)/L of the row obtained by flooring its
first K-1 coordinates and putting the residual in the last one. The shift
map sends distinct appended symbols to distinct successors, so the pair-row
TV is the same. Couple two chains from the same y using common next states
while possible: their chance to first disagree in m transitions is at most
m(K-1)/L. Such a coupling exists by matching each coordinate's minimum
mass and distributing the residuals. Therefore every path-event probability,
and then its maximum over initial states, differs by at most m(K-1)/L.
For the exact maximum b_grid over the finitely many grid tables and states,

    b_grid<=beta_(K,v)(m)<=min(1,b_grid+m(K-1)/L).      (GRID)

Each grid event probability is rational and obtained by a finite path sum;
equivalently a dynamic program stores the state and each count capped at v.
For prescribed rational eta>0 choose L>m(K-1)/eta. This gives a two-sided
absolute certificate; at m=0 the answer is exactly 1.

For rho at fixed M, put a_M=1/(2M) and C_K=2^(K+1)K². If epsilon<=a_M
and v<=M then 2v epsilon²<=1/2, so C_K exp(-2v epsilon²)>1 and A=1.
The outer cap is then 1. Thus it suffices to minimize on [a_M,1], extending
continuously at 1; that endpoint also caps to 1 and is a limit of allowed
epsilon. On this rational compact interval

    1-exp(-2epsilon²)>=d_M:=1/(2M²+1),

since exp(x)>=1+x. Differentiating the raw fraction
F_v(epsilon)=C_K exp(-2v epsilon²)/(1-exp(-2epsilon²)) gives the uniform bound

    |F'_v|<=4 C_K[M/d_M+1/d_M²].

Taking min with 1 preserves its Lipschitz constant; adding epsilon gives

    Lambda=1+4 C_K[M(2M²+1)+(2M²+1)²].                (LIP)

Smoothing and beta are constant in epsilon; finite min over v and outer
cap preserve that modulus. Exponentials at rational arguments have certified
rational intervals: for x>=0 rational, S_n=sum_(j=0)^n x^j/j! is a lower
bound on exp(x), and when n+2>x the remaining tail is at most
[x^(n+1)/(n+1)!]/[1-x/(n+2)]. These converge, and reciprocals certify
exp(-x). The positive margin d_M makes subsequent divisions effective.

For rational eta>0, compute each beta with width <eta/8 by (GRID), evaluate
the scalar terms with interval width <eta/8, and use a finite epsilon mesh
containing both endpoints with spacing <eta/(4 Lambda). The minimum of
the computed upper endpoints is an upper bound on the true minimum.
The minimum lower endpoint minus Lambda times the mesh spacing is a lower
bound. Their gap is <eta; cap in [0,1] and take the finite minimum over v.
This is a terminating computation to any required positive rational absolute
error, not an undecidable exact-equality search. These possibly enormous
enumerations are proof-side computations; no practical or free predictor
implementation cost is asserted.

## 13. U2: explicit risk, legal minimum precision and separate lower witnesses

### 13.1 Inverse moments from the occupancy tail

Set J=n_(Y_M)(M), c=K^4/(M+1), W=1/(J+1), and

    H(c)=1 (c>=1), H(c)=c(1+ln(1/c)) (0<c<1).

For 0<t<=1, W>t is equivalent to J<ceil(1/t)-1. This integer threshold
is zero only when the event is empty, and otherwise is at most 1/t. By UC,
P(W>t)<=min(1,c/t). Integrating this tail over [0,1] gives E W<=H(c).
Also UC at v=1 gives P(J=0)<=min(1,c). For J>=1,
1/sqrt(J)<=sqrt(2)/sqrt(J+1); hence

    E[1/(J+K)]<=H(c),
    E[1{J>=1}/sqrt(J)]<=sqrt(2)E sqrt(W)<=2sqrt(2c).   (MOM)

Indeed if c<1, E sqrt(W)<=int_0^1 min(1,c/t²)dt=2sqrt(c)-c;
if c>=1 use E sqrt(W)<=1. No reciprocal at J=0 was used.

### 13.2 Finite M, arbitrary legal h, and h_N versus h_0

Choose alpha=1/(M+1) in §3 and set

    A=K ln2+ln(2K²M(M+1)).

On its one observed-history good event, the ideal actual error is bounded
by unit loss when J=0, and by sqrt(A/(2J))+(K-1)/(J+K) when J>=1.
Off the event it is <=1. Applying MOM and adding its failure probability
proves, for every theta,mu,

    E TV(p_N^+(Y_M),theta_(Y_M))<=S_K(M),
    S_K(M)=min(1,min(1,c)+2sqrt(Ac)+(K-1)H(c)+1/(M+1)). (S)

Now average I directly, using E[1/(J+K)]<=H(c):

    sup_(theta,mu)R_act(F_h)<=U_K(M,Q),
    U_K(M,Q)=min(1,S_K(M)+(78KM H(c)+K-1)/Q).          (UQ)

The realization term is pathwise and incurs no extra statistical failure
or conditioning factor. At h_N equation II instead gives min(1,S_K(M)+e_N).
At the lowest legal h_0=max(4,ceil(log2 M)+1), Q_0>=2M, whence

    R_act(F_(h_0))<=min(1,S_K(M)+39K H(c)+(K-1)/(2M)). (U0)

For each fixed K, c=O_K(1/(M+1)), A=O_K(log(M+1)) and
H(c)=O_K(log(M+1)/(M+1)); therefore these h_N and h_0 upper bounds are
O_K(sqrt(log(M+1)/(M+1))). Finite small M is handled by the caps at 1.
The two schedules need not emit identical vectors. U0 proves actual mean
consistency; it does not transfer II or the precise finite-visit external
row limits to h_0. Nothing here is a lower bound on internal precision.

### 13.3 Any common randomized full-history predictor: iid actual lower bound

Fix N>=3,K>=2 and any such predictor. Put

    p_±=1/2±1/(8sqrt(N)), d=p_+-p_-=1/(4sqrt(N)).

Let every row of theta_± give symbol 1 probability p_±, symbol 0 probability
1-p_± and the remaining symbols zero; take mu_± as the corresponding iid
pair law. Thus the complete X_1^N consists of N iid draws. Every possible
actual endpoint has the same true next distribution, so the target is
actual prediction, not a difficult external row. For the two history laws
P_± the one-draw chi-square is

    d²/[p_-(1-p_-)]<=4/(15N),

because p_-(1-p_-)=1/4-1/(64N)>=15/64. If L is the likelihood ratio,
E_- L² multiplies over the independent draws, giving

    1+chi²(P_+||P_-)<=(1+4/(15N))^N<=exp(4/15).

Cauchy–Schwarz applied to (1/2)E_-|L-1| bounds history TV by half the
square root of chi-square. Using exp(x)<=1/(1-x) for 0<=x<1 (termwise
power-series comparison),

    TV(P_+,P_-)<=1/sqrt(11)<1/2.

For each common history x, the actual query and conditional randomized
output law are identical in the two experiments. Integrating the output
triangle inequality against min(P_+(x),P_-(x)) yields

    risk_+ + risk_- >= d sum_x min(P_+(x),P_-(x))
                    =d[1-TV(P_+,P_-)]>=d/2.

Thus at least one source has actual mean TV >=d/4=1/(16sqrt(N)). This
holds for every N and every common randomized algorithm, without I and
without a computation restriction. The witness can depend on N and the
algorithm; no single source is claimed to meet this lower bound at every N.
K>2 is a lawful zero-coordinate embedding; K=2 is strictly positive iid.

### 13.4 Final-output grid lower bound and a separate rounding interface

If every output lies in the denominator R=2^b simplex grid, b>=1, choose
the iid source with symbol-1 probability p=1/2+1/(2R), symbol-0 probability
1-p, remaining probabilities zero, and iid initialization. Since R/2 is an
integer, every output coordinate j/R differs from p by at least 1/(2R).
The singleton subset formula for TV gives, for every output and every seed,

    TV(output,theta_(E_N))>=1/(2R).

This is a format lower bound with a different witness from §13.3. The two
bounds cannot be added as though attained by one common source, and the
grid bound says nothing about internal h, parameter bits, width or depth.

For any simplex vector q, define F_R(q)_c=floor(R q_c)/R for c<K-1 and
F_R(q)_(K-1)=1-sum_(c<K-1)F_R(q)_c. All coordinates are nonnegative;
the last increase equals the sum of the first K-1 decreases. Thus
TV(F_R(q),q)=sum_(c<K-1)(q_c-floor(Rq_c)/R)<=(K-1)/R.
This is an error interface. Any actual arithmetic/rounding/output module
and its direct-count front end require their own full implementation costs.

### 13.5 Limits of the result

The sqrt(log N) gap, sharp K dependence and optimal joint resource–risk
relations remain open. Similar N exponents do not constitute matched sharp
rates. None of the iid, rare-row or output-format lower bounds establishes
optimality for the whole Transformer class. No KL, training attainability,
architecture advantage, or implementation/cost theorem follows here.

## Appendix A. G6: complete Counter examples and their proofs

Every row table below specifies next-symbol probabilities and uses the pair
shift rule of §1, not an arbitrary transition map on pair names. Exact risk
formulas are for ideal add-one. Every comparison or limit mentioning F in
this appendix uses h_N, so II transfers each displayed row/maximum/mean or
positive-event conditional risk within e_N. The lower bounds for arbitrary
common algorithms do not assume I. For every geometric parameter p or r
used below, 0<p<1 or 0<r<1 is understood. The complete tables and variants
are separate sources; no rows from different examples are merged.

### E1. Unreachable external row: two fixed indistinguishable sources

K=2, mu=delta_00. Give ALL four rows, in symbol order(0,1):

| row | source A | source B |
| --- | --- | --- |
| 00 | delta_0 | delta_0 |
| 01 | delta_1 | delta_1 |
| 10 | delta_0 | delta_0 |
| 11 | delta_0 | delta_1 |

Both entire histories are zero for every N. For ANY common possibly
randomized history/query predictor, its query11 output has the same law.
For each output q, TV(q,delta_0)+TV(q,delta_1)>=1. Expected query11 risks
therefore sum to at least1 at every N. Both fixed-source risks cannot
tend to zero; one fixed source has limsup risk>=1/2. This does NOT say
one preselected source has risk>=1/2 for every N. For F
itself, n_11=0 implies each of these two fixed-source row risks lies in
[1/2-e_N,1/2+e_N] at every N. The actual endpoint is00 with true delta_0;
its ideal risk is 1/(M+2)=1/N, so this is NOT a terminal lower bound.

Unique stationary laws do not rescue the external-row task. Replace the
11 rows by (a,1-a), with a=1/4 in A' and 3/4 in B', keeping the other
three rows. Every state feeds00 eventually; both whole chains have the
unique stationary law delta_00. Their query11 TV separation is1/2, so
any common predictor has a risk-sum lower1/2, maximum at least1/4, and
one fixed source has limsup at least1/4. F has row11 risk within e_N of
1/4 in BOTH sources. Observation and true terminal risks remain identical.

Denied quantifier: one common algorithm cannot estimate every arbitrary
unobserved row on this full source class, nor its K² maximum. No every-row
failure, endpoint failure, or fixed-source-per-N selection is inferred.

### E2. Finite visits need not be logically necessary: retain the lucky case

K=2, mu=delta_00, theta_00=delta_0, and theta_01=theta_10=theta_11=(1/2,1/2).
All rows are specified. The history stays00; its ideal row00 risk is1/N,
and each other row has zero count, uniform prediction and zero error.
Thus the ideal all-row maximum is1/N, and F's maximum is at most1/N+e_N.
The chain is reducible and initialization does not sample the other rows.
It has only one closed class, {00}, consistently with the structural bound in §9.

This POSITIVE example disproves the sourcewise assertion 'every requested
row must be visited infinitely often' as a logical necessity for this F.
It does not contradict E1, whose universal quantifier ranges over two
arbitrary unknown rows. Perturb any one of those unvisited true rows while
leaving the observed source unchanged, and its fixed-row guarantee is lost.

### E3. Unique stationary, geometric transient: exact conditional bias

K=2, mu=delta_00, 0<p<1, with ALL rows

    00:(p,1-p), 01:delta_1, 10:delta_0, 11:delta_1.

The complete pair matrix, ordered00,01,10,11, is

    [[p,1-p,0,0], [0,0,0,1], [1,0,0,0], [0,0,0,1]].

The only closed class is{11}; its stationary law is uniquely delta_11,
and that class is aperiodic. Let T be the first step exiting00. Then
P(T=t)=p^(t-1)(1-p), Y_j=00 for j<T, Y_T=01,
Y_j=11 for j>=T+1. For every M>=1:

- E_N=00 iff T>M: probability p^M. On this event n_00=M,
  C_00,0=M; ideal output ((M+1)/(M+2),1/(M+2)). Its exact risk is
  r00(M)=|(M+1)/(M+2)-p|=|1-p-1/(M+2)| ->1-p.
- E_N=01 iff T=M: probability (1-p)p^(M-1). Here n_01=0; the exact
  ideal risk to theta_01=delta_1 is1/2 for every M. The endpoint has
  JUST arrived and supplies no unobserved successor sample.
- E_N=11 iff T<=M-1: probability1-p^(M-1), positive only for M>=2.
  Conditional on T=t there are n_11=M-t-1 departures, so its ideal
  risk is1/(M-t+1).
- E_N=10 has probability0 for this initialization; no conditional risk
  at10 is assigned.

Consequently the exact ideal actual-terminal MEAN is

    p^M r00(M)+(1-p)p^(M-1)/2
       +sum_(t=1)^(M-1) (1-p)p^(t-1)/(M-t+1).           (E3)

The sum is empty when M=1. Splitting at T<=floor(M/2) gives, for M>=2,
an upper bound 2/(M+2)+p^floor(M/2), which tends to zero. Pathwise it
also tends to zero after absorption. F inherits the same mean
limit, but its conditional00 risk tends to1-p and conditional01 risk
tends to1/2, each within e_N of the exact displayed ideal risk.

For a fixed external row00, total departures n_00(infinity)=T<infinity. Its limiting
add-one vector is (T/(T+2),2/(T+2)), so limiting error is|T/(T+2)-p|.
For p=2/3, the event T=1 alone has probability1/3 and error1/3,
giving limiting expected fixed-row risk at least1/9. Thus unique stationary
law is insufficient for full-row, fixed-transient-row, and transient
conditional guarantees. It is compatible with actual-terminal consistency.
The conditional failure follows from survivorship selection, not from a
false iid assumption about successors after conditioning on the endpoint.

Denied quantifiers: E Z_N->0 does not imply conditional convergence for
EVERY s with p_N(s)>0 at every N. Unique stationarity and reachability do
not make a transient query recurrent. This example leaves the recurrent
allowed-time assertion intact.

### E4. Legal period4 on ALL pair states, including zero-event bookkeeping

K=2, theta_00=delta_1, theta_01=delta_1, theta_11=delta_0,
theta_10=delta_0. The pair cycle is

    00 -> 01 -> 11 -> 10 -> 00.

Its full matrix in order00,01,10,11 is

    [[0,1,0,0], [0,0,0,1], [1,0,0,0], [0,0,1,0]].

This is a valid shift/appended-symbol table, irreducible with period4,
unique stationary law uniform on the four states. For mu=delta_00,
write v_0=00,v_1=01,v_2=11,v_3=10. Then Y_j=v_(j mod4), and

    n_(v_r)=floor((M+3-r)/4),    r=0,1,2,3.

Each successor in a row is deterministic. Exact ideal row error is
1/(n_(v_r)+2). Both the ideal all-row maximum and actual-terminal risk
are 1/(floor(M/4)+2), hence vanish. Conditioning on v_r is legal ONLY
when M=r mod4, where probability1 and risk is this same quantity. All
other conditional times are undefined, not zero-risk declarations.
All rows are infinitely visited despite zero transitions, nonstationary
point initialization and failure of ordinary-time TV mixing.

For a multi-phase initial law mu=q delta_00+(1-q)delta_01, 0<q<1,
p_N(00)=q at M=0 mod4, 1-q at M=3 mod4, and0 at residues1,2. Positive
values are bounded below by min(q,1-q). A uniform stationary initial law
makes every p_N(s)=1/4 at every N, but does not eliminate periodicity.

Denied necessity claims: strict positivity, stationary initialization and
aperiodicity are not necessary for even FULL-row consistency target.
Failed proof route retained: the formal series sum_j P^j f can diverge
on a periodic chain (on a two-cycle take f=(1/2,-1/2)). That invalidates
the series proof, not learning. The finite equation (I-P)g=f has solution
g=(1/4,-1/4) in that example and supplies the lawful alternative.

### E5. Reducible stationary mixture: row mean is not terminal mean

K=2, ALL rows 00:delta_0, 01:delta_1, 10:delta_0, 11:delta_1;
mu=(delta_00+delta_11)/2, itself stationary. There are two absorbing closed
classes and multiple stationary distributions. Histories are all0 or all1.
At every M>=1 exact ideal risks are

    E terminal risk =1/(M+2),
    E fixed row00 risk =1/4+1/[2(M+2)],
    E max_all_rows risk =1/2,
    E[terminal risk|E_N=00]=E[terminal risk|E_N=11]=1/(M+2).

The two conditioning events have probability1/2;01 and10 have probability0.
Every formula transfers to F within e_N. A recurrent fixed row can have
nonzero UNCONDITIONAL mean because half the paths select the other class,
yet zero limiting conditional terminal risk. This is why the numerator
used in §8 must be E Z_N, not an imagined vanishing E R_N(s).

Even a stationary distribution positive on every pair is insufficient for
pathwise row coverage without ergodicity. A complete variant is

    00:delta_0, 01:delta_0, 10:delta_1, 11:delta_1,
    mu=uniform on all four pairs.

Its closed classes are{00},{11},{01,10}, and mu is stationary with full
support. Exact fixed00 mean is3/8+1/[4(M+2)], but conditional00 risk is
1/(M+2). The exact actual mean is
1/[2(M+2)]+1/[2(floor(M/2)+2)] ->0. Positive ensemble stationary frequency
does not say one path visits the corresponding class.

Denied quantifiers: stationarity or positive stationary MASS does not imply
all-row/fixed-row consistency for arbitrary reducible unknown laws.
Nonuniqueness does not prevent actual-terminal or recurrent conditional
consistency. Nothing here contradicts an irreducible-chain theorem.

### E6. Deterministic initial pair, genuinely random final class

K=3, mu=delta_01; complete table in order(0,1,2):

| row | theta | row | theta | row | theta |
| --- | --- | --- | --- | --- | --- |
| 00 | delta_0 | 01 | (1/2,0,1/2) | 02 | delta_2 |
| 10 | delta_0 | 11 | delta_2 | 12 | delta_2 |
| 20 | delta_0 | 21 | delta_2 | 22 | delta_2 |

At Y_1 the state is10 or12, each half. At Y_2 it is00 or22 respectively,
and stays there. The other rows feed one of these two classes; there is
no omitted third class. For M=1 the actual ideal risk is2/3. For M>=2,
its current absorbing row has n_s=M-2 departures, so

    E terminal risk =2/(M+1),
    E fixed00 risk =1/3+1/(M+1),
    E max_all_rows risk =2/3,
    E[terminal risk|E_N=00]=2/(M+1),  p_N(00)=1/2.

The same holds symmetrically for22. The transient initial row01 is visited
once; its limiting ideal error is1/4 on either branch. This is an explicit
case of (FL), not convergence to a deterministic global pi. Conditional
recurrence learns the selected class, not the union of all possibly
selected classes. F has the same limits by(I).

### E7. Random final class AND a rare transient conditional failure

To address both phenomena in ONE law, take K=3, mu=delta_00 and complete
rows

| row | theta | row | theta | row | theta |
| --- | --- | --- | --- | --- | --- |
| 00 | (p,(1-p)/2,(1-p)/2) | 01 | delta_1 | 02 | delta_2 |
| 10 | delta_0 | 11 | delta_1 | 12 | delta_2 |
| 20 | delta_0 | 21 | delta_1 | 22 | delta_2 |

The first exit time T from00 is geometric with P(T=t)=(1-p)p^(t-1).
Its exit symbol1 or2 has equal probability; one step later it is absorbed
at11 or22. Thus C_infty is genuinely random, each class with probability
1/2. E_N=00 iff T>M, probability p^M>0, n_00=M, and its exact ideal
conditional risk is

    |(M+1)/(M+3)-p|=|1-p-2/(M+3)| ->1-p.                (E7a)

On T=M its current state01 or02 has n_s=0 and exact risk2/3. On T=t<=M-1
its absorbing row has n_s=M-t-1 and risk2/(M-t+2). Hence the exact ideal
terminal mean is

    p^M |1-p-2/(M+3)| +(1-p)p^(M-1)*2/3
       +sum_(t=1)^(M-1)(1-p)p^(t-1)*2/(M-t+2),          (E7b)

which tends to zero (or simply use eventual absorption). F's
actual mean tends to zero, while conditional00 tends to1-p.
This meets the requested 'mean zero but conditional nonzero' behavior in
a random-closed-class example as well as in the unique-class E3.

### E8. Genuinely random multi-entry periodic test (complete separate table)

K=3, mu=delta_22, 0<p<1. All next-symbol vectors in order(0,1,2):

| row | theta row | row | theta row | row | theta row |
| --- | --- | --- | --- | --- | --- |
| 00 | delta_1 | 01 | delta_0 | 02 | delta_0 |
| 10 | delta_1 | 11 | delta_0 | 12 | delta_0 |
| 20 | delta_1 | 21 | delta_0 | 22 | (1-p,0,p) |

Only C={01,10} is closed; its period is2. At T=first step leaving22,
P(T=t)=(1-p)p^(t-1), Y_T=20, Y_(T+1)=01, then 01<->10 forever.
Both entrance parities have positive probability. For M>=1,

    p_(M+2)(01)=(1-p^M)/(1+p)             if M even,
               p*(1-p^(M-1))/(1+p)       if M odd.      (E8a)

It is zero at M=1, positive at every M>=2, and at least p(1-p) there.
Its two limiting values are 1/(1+p) and p/(1+p). Thus one cannot simply
say 'the chain converges to pi', or lose one entrance residue. Here the
stationary class law is (1/2,1/2), but the entrance-biased phase limits
differ; (DEN) of §8, not ordinary-time mixing, is the valid conclusion.

On E_N=01, T ranges over 1<=t<=M-1 with M-t-1 even. Put
l=(M-t-1)/2. There are exactly l historical departures of01, each appending0;
its ideal risk is 2/(l+3). Therefore the EXACT conditional ideal risk is

    [sum_(1<=t<=M-1, M-t-1 even)
         (1-p)p^(t-1)*2/((M-t-1)/2+3)] / p_(M+2)(01).   (E8b)

A finite early-t part vanishes as M grows and the remaining tail is bounded
by the geometric tail; the denominator has the proved lower bound, so
(E8b)->0. F differs by at most e_N. In contrast E_N=20 occurs
only at the first exit T=M, has probability (1-p)p^(M-1), n_20=0, and
conditional ideal risk 2/3 at EVERY M. It is a transient conditional failure,
not a periodic recurrent counterexample. This distinction also checks the
last-arrival/sample index convention.


### E9. A vanishing denominator is not itself a failure criterion

K=3, mu=delta_00, and the complete table

| row | theta | row | theta | row | theta |
| --- | --- | --- | --- | --- | --- |
| 00 | (p,1-p,0) | 01 | (1/3,1/3,1/3) | 02 | delta_2 |
| 10 | delta_2 | 11 | delta_1 | 12 | delta_2 |
| 20 | delta_2 | 21 | delta_1 | 22 | delta_2 |

The first exit from00 reaches01. Every successor of01 feeds11 or22
without returning to01 or00 (the 10 branch goes10->02->22). Thus E_N=01
iff that first exit occurs at step M. Its probability is(1-p)p^(M-1)>0,
which tends to zero, but n_01=0 and the true row is U_3. Its EXACT ideal
conditional error is0 at every N; F's is at most e_N. This is
only a positive accidental-correctness example. It is not used to excuse
missing data in a guarantee over arbitrary unknown rows. Together E3/E9
show that p_N(s)->0 alone is neither sufficient to force failure nor a
proof of consistency. The relevant sufficient finite-N condition controls
the joint bad-event numerator relative to p_N(s).

### A.10. No uniform finite-N row rate: an explicit positive stationary family

Here the source CAN depend on N to refute a class supremum. No one fixed
source is claimed inconsistent. This stronger example avoids relying just
on exact unreachable rows.

Fix K=2, M=N-2>=1, epsilon=1/(16M), and a in{1/4,3/4}. Give all rows

    00:(1-epsilon,epsilon),
    01:(1/2,1/2), 10:(1/2,1/2), 11:(a,1-a).             (S)

All entries are strictly positive; P² has all entries positive. The chain
is irreducible, aperiodic and has a unique positive stationary law. Initialize
at this law, explicitly

    Z_a=1+epsilon*(4+1/a),
    pi^a=(1,2epsilon,2epsilon,epsilon/a)/Z_a             (00,01,10,11).

Direct multiplication verifies pi^a P=pi^a. Neither the stationary law nor
a is disclosed to the common algorithm. Thus all five original structural
properties can hold and still give the following obstruction.

Let H be the observation consisting of N zeros. Under source a,

    P_a(H)=pi^a_00*(1-epsilon)^M.

Since 4+1/a<=8, pi^a_00>=1/(1+8epsilon)>=2/3. Bernoulli's inequality
(1-epsilon)^M>=1-M epsilon=15/16 gives P_a(H)>=5/8 in BOTH sources.
On H a common query11 predictor has exactly the same output law and the
true rows are separated by TV=1/2. Restricting each expectation to H,
using the smaller of its two masses, proves for EVERY common randomized A

    R_fixed11(A,a=1/4)+R_fixed11(A,a=3/4)
       >=min_a P_a(H)/2,
    max_a R_fixed11(A,a)>=min_a P_a(H)/4>=5/32.          (LB)

The all-row expected maximum is at least this fixed-row risk. Consequently
there is no r_2(N)->0 bounding either risk uniformly over even the strictly
positive STATIONARY source class without further frequency/access control.
This is an information lower bound, not a limitation peculiar to attention,
precision, direct counts, or a particular implementation.

For F, on H n_11=0 and its ideal row11 risk is1/4 in BOTH
sources. Each risk is therefore >=5/32-e_N, a direct quantitative witness.
For arbitrary A only the maximum over the two witnesses is claimed at each
N; for this triangular family one cannot label one fixed table bad at all N.

#### A.10.1 This example does NOT refute a fixed-K actual-terminal uniform rate

On H the actual query is00, and its ideal risk is

    |1/(M+2)-epsilon|=1/(M+2)-1/(16M),

which is O(1/M), not1/4. There is also an explicit upper bound for the
ENTIRE actual risk of p_N^+ on this stationary family. Let
U=M-n_00 count other departure states, and A=C_00,1 count exits from00.
Stationarity gives

    E U=M(1-pi^a_00)<=8M epsilon=1/2,
    E A=M pi^a_00 epsilon<=1/16,
    P(E_N!=00)=1-pi^a_00<=1/(2M).

Markov gives P(n_00<M/2)<=1/M. On n_00>=M/2 the row00 error is at most
(A+1)/(M/2+2)+epsilon. Splitting the endpoint expectation accordingly,

    E TV(p_N^+(E_N),theta_(E_N))
      <=(17/8)/(M+4)+1/(16M)+1/M+1/(2M)
      <=59/(16M).                                      (S-END)

F adds at most e_N. Thus this particular source sequence, while
refuting uniform row rates, has vanishing actual-terminal risk itself.
Neither this lower bound nor the fact that the existing p_*/pi-dependent
upper fails to be uniform proves that ALL actual-terminal uniform rates
are impossible.

The fixed-K uniform actual question is answered affirmatively by §§11–13 of this proof; the sharp rate remains open. This rare-row example is not an actual lower-bound witness.

### A.11. A separate, valid endpoint obstruction when K is not fixed

A bound tending to zero depending on N ONLY, uniformly over ALL finite K,
is false for the retained F. For each N take K=N+1, mu=delta_(0,1), and
for every pair(i,j) define the complete deterministic row

    theta_(i,j)=delta_(min(j+1,K-1)).                    (GROW)

The observed symbols are X_t=t-1 for 1<=t<=N. The current pair
E_N=(N-2,N-1) has no departure in the history; its next law is delta_N.
The ideal current-row prediction is U_K, of error1-1/K, and F's actual
risk is at least1-1/(N+1)-e_N. All tables are finite, homogeneous and legal.
This changes K with N, so it DOES NOT disprove a bound r_K(N) for each
fixed K, a K-dependent sample-complexity bound, or pointwise consistency
at any fixed source. It does not build or give the network the invisible
X_(N+1); theta is used only to state the loss's true target.


### A.12. Separate Prover §9.6 transient-success table, not merged with E9

For K=3, mu=delta_00, 0<r<1, the complete nine-row table is

| row | theta | row | theta | row | theta |
| --- | --- | --- | --- | --- | --- |
| 00 | (r,1-r,0) | 01 | (1/3,1/3,1/3) | 02 | delta_2 |
| 10 | delta_2 | 11 | delta_2 | 12 | delta_2 |
| 20 | delta_2 | 21 | delta_2 | 22 | delta_2 |

The 11 and 21 rows differ from Counter E9, so this is a distinct source.
After leaving 00 the chain visits 01 once, then goes to 10,11 or12, and
within two more transitions reaches the sole absorbing state 22. There
is no return to 01 or00. For M>=1, E_N=01 exactly on first exit at step M,
of probability (1-r)r^(M-1)>0. On this event n_01=0, so ideal add-one is
U_3=theta_01 and its conditional error is exactly zero. For F_(h_N) the
conditional error is <=e_N. The denominator tends to zero but prediction
succeeds. Unlike E9 this table does not have absorbing 11; no rows from
these two examples have been combined.

## 14. Conclusion of the conditional mathematical proof

The arguments above and every table in Appendix A establish G1–G6,
G7's statistical transfer, U1/UC and U2 for the exact quantified domain
K>=2, N>=3, M=N-2 and every common deterministic finite family satisfying I.
Every exceptional-event, periodic-residue, finite-visit and lower-witness
qualification is retained. The submission is this full text with no Fact
predecessors. Independent gateway admission and the Lead's subsequent
final_audit are evidence/execution steps, not mathematical premises.
The concrete Pi realization/cost obligation remains independent and open.
