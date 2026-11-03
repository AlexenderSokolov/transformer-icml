# CB005 — Independent full all-start review

2026-11-02. Reviewer: independent LLM reviewer, separate from the author.

## Result

**PASS recommendation for the exact candidate, not root acceptance.** No blocking mathematical, interface, constant, or unsupported-start defect found. Reviewed full proof:

`critical_beta_adaptation/CB005_all_start_critical_adaptation.md`

SHA256 `5e514451e88672533b5a376e43265b8a382ac0b59e816e3ef06212ea5be6db52`.

The same deterministic balance-gated full-corrupted-history estimator, with neither k nor beta as input, satisfies for M>=64, 0<=k<=M and every qualifying beta>0:

    R_all <= min{1, 2^16/sqrt(M) + 2^16/(M sqrt(beta)) + 2^23 k/M}.

Actual initialization is arbitrary, including outside stationary support. At beta=1/M the statistical coefficient is 2^17. On beta>=c/M the map attains the known-k order simultaneously over all budgets, with constants depending only on fixed c>0. This does not establish subcritical adaptation, sqrt(beta) mixing, neural implementation, external novelty, or formal verification.

## 1. Sources, acceptance, and review boundary

I read CB005 completely, frozen CB004 completely, BP001 completely, and the full existing two-component independent review. I read complete BU001 v2 and SC003, their acceptance receipts, the CB004/BP001 root receipts, and BT002's exact theorem/experiment and scalar completion. I independently reconstructed every new CB005 step and the entire CB004 all-start-valid gate reduction. The present review does not purport to reprove all older accepted research, or to freshly review the entire BT002 transport construction.

Actual accepted proof hashes were verified, not merely copied from provenance prose:

- CB004: `a322c2fe08b76cf84f587b91e4ab504e2e02468e8c1a617fd7b868e14f643155`.
- BP001: `22b60eedf31f1e990e990a8b64ad733a1a3acc9723a421fdc6d677866c771271`.
- BU001 v2: `2dc9cf9d13faa6cfa15fffd5ec83a67326ccc95eb6a63291c7b2349136b166f5`.
- SC003: `4235fc6b9de9d04368354d22f15774d66965ca572f21f197e456537e9bcba837`.
- BT002 main: `40d5345657b8f255cd1cef496fb84090aae18a6cd6bc7c083daa09c2ce913562`.
- BT002 scalar: `4be9d338e0d3e6b840441f4356e77b71db4da9f1208d74bd85f4790539ba9026`.

All 19 files in the frozen CB004/BP001 binding manifest still match. The new manifest additionally binds root receipts, this review, independent diagnostics, and author diagnostics. Stale manuscript headers saying candidate/pending do not override the separately hash-verified root receipts for the inherited units. CB005 itself remains a new candidate pending root disposition.

SC003 supplies the all-state protected-terminal experiment, support classification, arbitrary-start clean empirical comparator, and universal terminal occupation interface. BU001 supplies only its full-support target hitting-scale inequality; stationary initialization is not needed to interpret the deterministic maximum hitting time of the same full-support chain. BP001 supplies a separately frozen derivation of return moments, but its stationary reversal is NOT used to extend the new result. The reciprocal-return identity is proved internally, so the older BOD001/BAI004 mentions are historical corroboration, not unchecked quantitative premises.

## 2. Reset row and universal first-hit density

For distinct v,u, changing only row u to a deterministic transition to v does not alter the law of the first hit from v. The positive return from u in the modified chain is exactly 1+D_u, including defective return laws. The modified chain need not satisfy any binary pair constraint: this is a generic finite-state argument.

The Schur complement is valid in formal power series since both determinants have constant term 1. It gives

    1-F(z)=det(I-zQ)/det(I-zQ_(-u)).

Taking formal logarithms gives coefficient (tr(Q^r)-tr(Q_(-u)^r))/r. Its alternative expansion sum_j P(T_j=r)/j is nonnegative. Since Q_(-u) is a nonnegative substochastic matrix, its trace powers are nonnegative; since Q is stochastic, tr(Q^r)<=d. Retaining just j=1 and setting r=t+1 proves P_v(D_u=t)<=d/(t+1). There is no irreducibility or stationarity assumption in this step. The bound is valid for periodic, absorbing, reducible, and nonhitting starts.

## 3. Hitting potential and loop rotation

For a finite irreducible chain, all hitting moments exist. A uniform positive chance of hitting in a bounded number of steps supplies geometric block domination if an a priori moment argument is wanted. At v!=u the first-step equation gives Ph-h=-1; at u, Kac gives Ph(u)=1/p-1. Consequently

    Ph-h=-1+1_u/p,
    E_v J_u(r)=p[r+E_v h(Y_r)-h(v)]<=p(r+H).

The sign of the potential term is correct. The loop identity is not an appeal to reversibility: for each j,

    sum_v P^j(v,u)P^(r-j)(u,v)=P^r(u,u).

Summing j=0,...,r-1 yields exactly r P^r(u,u)=sum_v E_v[J_u(r)1{Y_r=v}]. Removing the endpoint event only enlarges the nonnegative quantity. This proves the return heat-kernel bound dp(1+H/r).

For v!=u, split the first-hit convolution at floor(r/2). Early hits leave at least r/2 return steps and contribute at most dp(1+2H/r). Later first-hit probabilities are at most 2d/r; the remaining return probabilities are a prefix occupation sum of length ceil(r/2), at most p(ceil(r/2)+H). The combined expression is bounded by dp[2+2/r+4H/r]<=4dp(1+H/r). At r=1 the early sum is empty, and the same enlarged bound remains valid. Starting at u is covered directly by the return bound. Thus (3.3) is pointwise, arbitrary-start, and target-specific; it is not a mixing estimate.

## 4. Moment induction and tilted chain

The ordinary hitting/positive-return family is survival-closed: after positive time, surviving states are outside the target; at time zero the positive return retains its own law. For r>=2,

    V^r <= r sum_(j=0)^(V-1) (V-j)^(r-1)

and conditioning on survival prove E V^r<=r! Hbar^(r-1) E V. The zero ordinary hit at u is harmless. Nonnegative power-series expansion and lambda Hbar=1/4 give E exp(lambda D)<=4/3 and E exp(lambda T)<=exp(2lambda/p). The quadratic negative-exponential inequality gives f<=exp[-3lambda/(4p)]. The linear lower bound gives f>=1-lambda/p>=3/4 and h_i>=1-lambda E D_i>=3/4. Also h_i,f<=1.

The ordinary hitting equation h_i=e^-lambda sum_j P_ij h_j for i!=u and the positive-return equation f=e^-lambda sum_j P_uj h_j prove that (4.3) is stochastic. Its support is exactly that of P, so irreducibility is retained. No minorization or binary-source property of Q is needed.

The tilted ordinary hitting mean is at most H/h_i<=4H/3<=2H. The return mean obeys

    E_Q T=E[T e^-lambda T]/f >= E T-lambda E T^2 >=1/(2p),
    E_Q T <= E T/f <=4/(3p)<=2/p.

For the lower inequality, division by f<=1 only increases a nonnegative numerator. Kac therefore gives p_Q<=2p and 1/p_Q<=2/p. Along with H_Q<=2H this yields Hbar_Q<=2Hbar. Applying (3.3) to Q gives 8dp(1+2Hbar/l)<=16dp(1+Hbar/l), exactly the slack in (4.4).

For a path i=Y_0,...,Y_l=u, the product telescopes to

    Q(path)=P(path)e^(-lambda l) f^(-J_u(l))/h_i.

There is one factor 1/f per DEPARTURE from u, not per arrival, which matches the count times 0,...,l-1. Starting at u has h_i=1 and requires no exceptional factor. Ending at u has h_u=1. On J_u(l)>4lp+1, f^J<=f^(4lp), so summing the exact likelihood identity yields

    P_i(Y_l=u,J_u(l)>4lp+1)
       <=h_i exp(lambda l) f^(4lp) Q^l(i,u)
       <=16dp(1+Hbar/l) exp[-l/(2Hbar)].

The p factor is thereby retained inside the JOINT event. There is no illicit multiplication of separate unconditional probabilities. The positive tilt is only an analysis device; its dependence on unknown source quantities adds no predictor input.

The lower tail uses K=ceil(lp/16). Fewer than K counted visits means D+T_1+...+T_(K-1)>=l. This includes equality at the excluded terminal index. Because K-1<=lp/16, exponential Markov gives (4/3)exp[-7l/(32Hbar)]<=2exp[-l/(8Hbar)]. At K=1 no return variables are used. Strong Markov supplies IID returns before horizon/endpoint conditioning, not after it.

## 5. Generic arbitrary-start weighted imbalance

For np>=1 the two good count events give J2<=4mp+1<=9np and J1>=np/16, hence balance at least 1/145. Therefore every strict imbalance with c<=1/256 lies in the specified lower/upper-tail union.

For the first-window lower-tail event, condition on the ENTIRE deterministic-time prefix through Y_n. Its suffix terminal probability is bounded by 4dp(1+Hbar/m). Multiplying by the unconditional lower-tail probability contributes at most 8dp(1+Hbar/n)exp[-n/(8Hbar)]. This multiplication is justified by the uniform conditional bound, not independence. For the second-window upper tail, condition only on Y_n and use the joint tilted inequality, contributing at most 16dp(1+Hbar/n)exp[-n/(8Hbar)]. Their sum is precisely (5.2).

Writing x=n/Hbar and L=pqHbar, the weighted result is 24d L/n (x+1)e^-x/8. The maximum occurs at x=7 and equals 8e^-7/8<4; for example e^(7/8)>1+7/8+(7/8)^2/2>2 proves the strict comparison without numerical approximation. Thus the bound is 96dL/n.

If np<1, do not invoke concentration: the pointwise kernel gives 4d(pq+L/M). Since Hbar>=1/p, L>=q and pq<q/n<=L/n; using M>=n gives at most 8dL/n. This also covers q=0 without division. Summing targets and n>=M/3 gives 288d sum L/M. At J=0 the strict imbalance event is false. The argument works for every initial state and hence every mixture; no stationary endpoint distribution appears.

## 6. Full-support binary specialization

The positive all-state certificate makes the full-supported pair chain irreducible. BU001's H is then the maximum over every actual possible pair start, so no hidden support restriction remains. It supplies sqrt(beta) p gamma H<=5 with gamma=(a,1,1,tau). Since 1/p<=1+H, p gamma<=1 and beta<=1,

    p gamma Hbar<=6/sqrt(beta)<=10/sqrt(beta).

Using q=(a,b,e,tau)<=gamma gives sum L<=40/sqrt(beta), hence 288*4*40=46080<2^16. No b=e assumption, stationary reversal, or global coupling has entered this specialization. Summing a certificate row proves beta<=1 whenever the class is nonempty.

## 7. Singleton support and all unsupported starts

SC003's classification is applicable: with positive crossing stationary mass, P²(10,01)=ea>=beta x and P²(01,10)=b tau>=beta x force all four exit probabilities positive and thus full support; otherwise there is exactly one supported absorbing diagonal.

For absorbing 00, a=0 and every path ending in A=01,B=10,C=11 has never previously hit 00. Replacing the killing edge B->00 by B->A produces exactly the stochastic reflected R. For each active ordered path, only B->A factors increase, from 1-e to 1. Thus original unconditioned path mass is dominated by R path mass, with occupation counts and endpoint unchanged. This is not a comparison of conditional survivor distributions.

For b,tau>0, R is irreducible and its stationary law is (tau,tau,b)/(2tau+b). The target-A ordinary hitting times from B,C are 1 and 1+1/tau; the target-C times from A,B are 2/b-1 and 2/b. Therefore H_A=1+1/tau, H_C=2/b. The proposed bounds on Hbar also cover inverse stationary masses. The weighted products are at most

    b(2tau+1)/(2tau+b)<=1,
    tau(b+2)/(2tau+b)<=1,

using b<=1 and tau<=1 respectively. Generic (5.1) with weights (b,0,tau) yields 288*3*2/M=1728/M.

At b=0 or tau=0, approximate only the auxiliary reflected matrix by positive parameters. For fixed M, the finite path sum, fixed strict count event, and weights depend polynomially on entries and weights; hence the uniform bound passes to the boundary. No limiting claim about original-source certificate preservation or irreducibility is made.

The omitted target B has original weight e. Since B->00 is the only incoming transition from the active set, and 00 cannot be left,

    e P_i(Y_M=B)=P_i(T_00=M+1)<=4/(M+2)

for any active start. The first-hit bound is applicable even if some starts never hit. Dropping imbalance only enlarges this contribution. Starting at 00 contributes zero designated loss; arbitrary mixtures follow. The total is at most 1732/M<2048/M, which lies below 2^16/(M sqrt(beta)). Symbol exchange permutes the public designated orientations correctly and proves the 11 case with the SAME estimator. No stationary or transient target is assigned an invalid Kac formula.

## 8. Frozen gate interface and final assembly

CB004's deterministic and inverse-occupation arguments were independently reconstructed, not merely presumed stationary-safe from their labels. Condition on the prefix through n with target count j. Its true balance event implies suffix count <=1023j. SC003's all-start terminal-occupation inequality gives 16(1023j+1)/(m+1), and dividing by j+1 yields <=16368/(m+1) per target. Summing four targets gives 130944/M. For its imported horizon restriction, use M>=128; for 64<=M<128 the final capped bound is already 1.

Every changed first-M symbol affects at most three selected triples; all count perturbations, including the first-half count at a split-straddling edit, are <=6k. The protected pair selects the same terminal row. With d=6k, the active balanced case costs clean empirical error plus 8d/(J+1); for J>=2d this follows from ratio perturbation and 4d/J<=8d/(J+1), while smaller positive J is covered by unit loss. J=0 is paid separately.

An active gate with J1<J/1024 implies J<1026d=6156k. A rejection outside J1<J/256 and with J>0 implies J<513d=3078k, unless J'=0, in which case J<=d. At k=0 neither false-status case with J>0 occurs. Rejection on true imbalance costs exactly q; zero count is covered by the two integer thresholds 6156k+1 and 3078k+1. Thus the reduction is valid pathwise for arbitrary source starts and every permitted attack realization, and integration covers randomized offline corruption without revealing its seed or mask.

SC003's actual-terminal empirical comparator has coefficient 8193 sqrt(32), uniformly over starts. The inverse and count-tail terms have total budget coefficient

    48*130944 +16*(6156+3078)=6433056<2^23.

The leftover 32/(M+1) plus comparator is bounded by 2^16/sqrt(M) for M>=64; the exact elementary upper (8193*6+4)/sqrt(M)<2^16/sqrt(M) suffices. Add the new all-start clean imbalance 2^16/(M sqrt(beta)) and take the independent unit cap. This proves CB5 and its critical specialization, including k=0, k=M, odd M, zero occupations, and boundary source probabilities.

The estimator is a total rational map: C'/J' only when J'>0 and 512J1'>=J', otherwise fixed designated zero. It reads the corrupted full triple histogram, four first-half counts, and protected terminal pair. Unknown source, Pi, beta, k, clean counts, and randomness remain analysis-only. A different k-aware map is not substituted in the clean case.

## 9. Oracle comparison and limitations

On beta>=c/M, the new additional term is <=c^-1/2 M^-1/2, hence risk O_c(min{1,max(M^-1/2,k/M)}). The stationary IID lower floors already proved within complete SC003 apply to the all-start minimax class, so this scale cannot be improved even with supplied k. This alone suffices for the claimed bandwise oracle order; the accepted stronger BT002 lower is consistent and also applies by restriction.

A direct scalar check is ln(1+x)<=x: since max(sqrt(beta),1/M)>=sqrt(beta), the known-k F satisfies F<=k/M+1/(M sqrt(beta))<=k/M+c^-1/2 M^-1/2 on the band. Thus no moving-beta logarithm is discarded outside its justified band. Constants are deliberately large and often make finite-horizon examples vacuous; no optimal constant is claimed.

## 10. Independent diagnostics and disposition

`CB005_independent_exact_checks.py` is newly written by this reviewer without importing author scripts. It tests reset/trace coefficients including defective returns, hitting potentials, occupation/loop identities, pointwise kernels, exact rational Doob likelihoods by joint endpoint/count dynamic programming, singleton reflection and absorption hazard identities including boundary probabilities, source/receipt hashes, and assembly constants. Additional joint upper/lower tails are verified using rational Taylor upper enclosures for the positive exponential; no floating tolerance is used. The rational discount 3/4 used for transform identity checks is explicitly a structural test of the identity for general discount, NOT falsely represented as exp(-1/(4Hbar)).

The frozen previous independent script was also rerun and passed all 752,062 checks. Its runtime field changes on execution, so the rerun output is separately preserved as `CB005_frozen_dependency_rerun.json`, and the original frozen diagnostic JSON was restored byte-for-byte and its hash verified. No candidate proof, frozen proof, accepted source, or acceptance receipt was edited. All final dependency hashes match their pre-review bindings.

Exact check counts and final file hashes are recorded in the diagnostic JSON and binding manifest. These finite tests corroborate the reviewed mathematical proof; they are not universal or formal verification. Recommend root acceptance of the exact CB005 hash, retaining the all-state certificate, arbitrary unsupported starts, protected actual terminal target, hidden seed/mask, strict first-M edits, unknown-k/beta same-map requirements, and the explicit nonclaims above.
