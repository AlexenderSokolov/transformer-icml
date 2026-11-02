# First genuine checkpoint: conditional grid bridge

Lead, 2026-10-25. Candidate proof, not a native Fact. Root
`d0bdd1d8bf611bb7a6e9c4bb14d8b14e5a71ae8cc5c97776fc079ac13c63b428`,
contract `d9e5e1f1efba187dfce2e80b395a1db533e89e8a97bd11c6f2f1e51d1ee9bb3e`.
Only this project's PROBLEM.md D1-D7 govern; source-stage2/PROBLEM.md has different definitions.

## 1. Exact integer map and coordinate convention

Let positive integers z0,z1 have Z=z0+z1 and a=z1/Z in [1/4,3/4].
For dyadic Q>=4 compute the Euclidean quotient and remainder of
`2*Q*z1+Z` by `2*Z`, and let J be the quotient. Algebraically
J=floor(Qa+1/2). It follows that |J/Q-a|<=1/(2Q), including exact ties;
if Qa=k+1/2, J=k+1 (half upwards). Because Q/4 and 3Q/4 are integers,
Q/4<=J<=3Q/4. Thus both output coordinates are strictly positive and sum
exactly to one. J represents **next-1**: in canonical alphabet order (0,1),
the output is `(Q-J,J)/Q`, not `(J,Q-J)/Q`.

For Q=4: a in [1/4,3/8) goes to 1/4, a in [3/8,5/8) goes to 1/2,
and a in [5/8,3/4] goes to 3/4. Endpoints are fixed; both ties go upwards.
For Q=2 output (1,1)/2. For zero counts, d=2 and
z1=min(3d,max(d,4(C1+1)))=4, Z=8, hence a=1/2 and every grid gives 1/2.
The formula works for every positive rational a in the closed interval,
not only for attainable Markov counts. Quotient/remainder is a finite
integer algorithm, not a real floor or bit extraction oracle.

## 2. Legal risk bridge, with explicit dependence

The C1 obligation must reprove, rather than inherit, the unquantized
actual-terminal bounds R_N(a)<=10^6/N and
R_N,00(a)<=160000/(1+Nu). Here a denotes the full unquantized branch
program in D4, not a parameter-known estimator. Source009 Sections2-6 give
the candidate proof: reverse entire-prefix TV bridge, then fixed-horizon
martingale variance, spaced visits and a deterministic-length row stack.
There is no conditional-binomial assumption and no squared-TV argument.

Pointwise Pinsker for Bernoulli gives (t-a)^2<=kl(t,a)/2; it remains true
after conditioning on actual S_N=00. For t,q in [1/4,3/4], log x<=x-1
gives kl(t,q)<=(16/3)(t-q)^2. Consequently, for the nearest-grid q,

    kl(t,q) <= (16/3) kl(t,a) + 8/(3 Q^2).

Indeed (t-q)^2<=2(t-a)^2+2(a-q)^2. Conditional expectation therefore yields

    R_N,00(q) <= (2560000/3)/(1+Nu) + 8/(3Q^2)
                <= 1000000/(1+Nu)+3/Q^2.

This implication is conditional on the C1 native statistical proof; the
rounding calculation alone has not established that premise.

## 3. One common program and average risk

N<6: uniform. For N>=6 use one m=floor(N/2) prefix, triples 3..m only,
and actual S_N. Q=2: uniform. Q>=4: rows01/11 uniform; row00 use the map
above; row10 keep the source009 positive ceil/residual map, residual to
coordinate1. For its positive integers z, with A=Q-1, compute j_c=ceil(Az_c/Z),
then add Q-j0-j1 to j1. Ceil sums lie in {A,A+1}; residual is 0 or1.
Thus both integers are in [1,Q-1], and q_c>=(1-1/Q)z_c/Z. For every target,
KL(p||q)<=KL(p||z/Z)+delta_Q, delta_Q=-log(1-1/Q)<=2/Q.

For N>=6,Q>=4 the modified average risk is bounded by

    (16/3)u R_old,00 + w R_old,10 + w delta_Q + 8u/(3Q^2)
    <= (16/3)*10^6/N + delta_Q + 2/(3Q^2)
    <= 6000000/N + 3/Q.

Rows01/11 have zero loss. This uses nonnegativity of each old row risk and
u<1/4. For Q=2 uniform has average loss<=log2<3/Q and conditional00 loss
<=1/3<3/Q^2 (chi-square at q=1/2 even gives <=1/4).
For N<6 uniform satisfies the displayed coarse upper bounds directly.
Every branch is finite, parameter independent, and will be charged in C3.

## 4. Conditional representation witness and minimax quantifiers

For each fixed u in (0,1/4), Q>=4 choose
t_Q=1/4+1/(2Q). It lies in [1/4,3/8], midway between two grid points,
so every allowable output's next-1 coordinate has distance at least 1/(2Q).
For Q=2 choose t_Q=1/4, whose distance from the unique grid value 1/2 is
1/4=1/(2Q). Pinsker gives kl(t_Q,q)>=1/(2Q^2) for every history and seed;
conditioning on S_N=00 preserves it. These t_Q<1/2 avoid the first-order
curve t=(1-u)/(1+2u)>1/2 for all allowed u. This witness is independent of N;
it is not the two-law statistical testing witness.

If C1 is admitted with its stated lower bounds and the source009 same-family
row10 limit is reverified, the precise conclusions are

    max{3/[16384(N+6)],delta_Q/3} <= M_N,Q <= 6000000/N+3/Q,
    max{3/[16384(1+(N-2)u)],1/(2Q^2)} <= C_N,Q(u)
       <= 1000000/(1+Nu)+3/Q^2.

The average format witness fixes t=1/2 and takes u down to0: row10 has
mass w->1/3 and next-1 probability 1-r->1, yielding delta_Q/3. It is a
supremum over allowed positive laws. Statistical and format witnesses are
different; max-to-sum gives order statements, never an additive bound on
one source. The conditional comparator may know u; the common algorithm
does not. No internal precision, depth or architecture lower bound follows.

## 5. Remaining load-bearing work and provenance

C1 exact native statistical chain; C2 full native joint classification;
C3 self-contained finite frontend and snap proof (old Facts unavailable as
premises), actual S_N/E_m adapter, new converter gates and complete resource
ledger, same-bit eight-counter streaming baseline; C4 fixed primary mapping,
independent fixed-version review, root proof and final audit remain open.
The oldest roots and all historical queues remain unchanged.

Read sources: current PROBLEM.md, AUTONOMOUS_RESEARCH.md, plan v10,
previous-stage/IDENTITY.json, source009 Lead handoff, Verifier review, and
proof-v1 Sections1-7,9-10. Source proof SHA256
fb85e0c52db17f676379f9765070ffa8e57fabb52e3866d5610374e40a717e91;
source review SHA256 264149c815ce5629565464da198a73cc7ba10c743f25a01be021d04d891b6626.
These are sources only. Actual local hashes are recorded with this checkpoint.
Budget: GPU use0; [Non-scientific operational metadata omitted.]
At most two mathematical routes: statistics/grid and implementation/comparison.
