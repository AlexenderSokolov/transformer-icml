# S010 原独立数学审查的科学正文

编排说明（非原文）：原独立审查日期为 2026-10-28，结论 ACCEPTED，无数学修复要求。以下保留原审查的完整逐引理推理、科学适用范围与有限检查事实；身份及运行元数据省略。审查绑定原证明哈希，而非这份新复制件。独立上下文 LLM 审查不是形式验证，也不是外部同行评审。下文有限检查是原审查历史结果，本次编排未重跑；原命令、脚本和运行记录不在本包内。

编排补充（非原文）：下文 “The command” 指原审查的历史检查，其命令未附；保留全部有限实例数量、误差值和科学限制。

The complete submitted argument proves the exact positive-beta lower bound and stronger finite-family expression under the frozen domain. The bounded-survival corollary uses precisely the accepted original-full-history L1MAX upper. No new assumption, additional bridge, changed claim, or revised dependency is required.

## Exact Reviewed Claim

For integers `K>=12`, `M>=1`, public `0<beta<=K^-4`, set

`n=M+1`, `epsilon=8 sqrt(beta)`, `m=floor(K/4)`, `L=m^2`,
`q=floor(M/L)`, `alpha=min(1/2, sqrt(m^3/(q+1))/8)`, and
`g=min(1,sqrt(K^5/n))`.

In the class of legal homogeneous second-order symbol-shift kernels admitting a stationary `pi` with `P^2(s,t)>=beta pi(t)` for **every** `s,t in A^2`, with arbitrary initialization, hidden source and stationary law, and one common randomized predictor of the actual terminal row from all `M+2` observed symbols, the proof establishes

`R_D2(K,M,beta) >= (1-epsilon)^n alpha/8 >= 2^-16 (1-epsilon)^n g`.

If `n sqrt(beta)<=2`, it establishes

`2^-16 exp(-32)g <= R_D2 <= R_D2^+ <= min(1,48 sqrt(K^5/n))`,

where `R_D2^+` is the risk of the original add-one rule using **all M departures**. It covers `M=K^4, beta=K^-8`. At beta zero the original all-`K>=2` MM5 and L1MAX endpoints are inherited separately; the stationary inverse is not evaluated at zero.

This is an expected half-L1 TV result at the same-trajectory actual terminal pair, not a stationary-initialization result, a fixed/independent query result, KL-risk bound, or a claim about every weak-beta window.

## Per-Lemma Audit

### unit_001: Lawful rotated clock (`lem:rotated-clock`)

- **Statement fidelity:** PASS. The family is on the original K-symbol alphabet and the original pair state space, with `K>=12` giving `m>=3` and `L>=9`. The claimed strengthening is the legal choice `p_5=(0,0)`, not a new latent clock state.
- **Proof validity:** The finite Euler construction uses degree balance to close each maximal unused-edge walk, and completeness to locate an unused outgoing edge on the existing tour whenever any edge remains. Each splice increases the finite used-edge set. Thus the resulting cyclic word uses each ordered C-pair exactly once. Rotating the unique loop `0->0` into position 5 gives both `c_5=0` and `c_6=0`. Rotation is public and independent of signs, the predictor, and observations.
- **Full-table audit:** The table's six nondefault categories are disjoint by ordered alphabet types and uniqueness of the C-pairs. Their probability masses normalize; each W-label is positive because `0<alpha<=1/2`, including the leftover odd-m coordinate. The default row is specified for every other one of the K-squared pairs, including removed pairs `p_1,...,p_4` and unused alphabet symbols. Every successor is appended via `(a,b)->(b,c)`. There is no time-dependent table or resampled sign.
- **Phase audit:** The replacements `p_0 -> (c_1,A) -> (A,B) -> (B,Z) -> (Z,0) -> (0,0)=p_5` use exactly five legal transitions. The clock continuation returns from `p_(L-1)` to `p_0`. The disjoint sets `D_0,...,D_(L-1)` therefore identify phase from the original pair state. The phase invariant is proved, not assumed.
- **Source audit:** The full MM5 Section 2 was read. Its construction requires only `c_5=0`; the submitted choice `c_5=c_6=0` is attainable by loop rotation and leaves the original in-support path argument intact. The new stronger rotation is actually proved in S010.
- **Adversarial checks:** I checked possible conflicts involving `(0,0)`, clock loops, `(w,0)`, deleted pairs, odd m, and leftover letters. None introduces overlapping row assignments or a state outside the original shift space. Independent support-graph checks for each `K=12,...,27` agree, but the general proof—not those instances—is decisive.
- **Contribution:** Supplies the exact legal base family and the closed phase structure required for every later argument.
- **Verdict:** PASS.
- **Repair direction:** None.

### unit_002: All-start one-visit invariant (`inv:one-visit`)

- **Statement fidelity:** PASS. The claim is for every starting pair and target, every path, and every block of L consecutive state times. It is not restricted to the closed clock support or a stationary start.
- **In-support argument:** A visit to any fixed `t in D` identifies its unique phase. On all subsequent transitions phase advances by one modulo L. Two visits to t therefore differ by a positive multiple of L, so an L-state block (time span L-1) cannot contain two visits.
- **Outside-support argument:** Every state outside D is genuinely in the default category. Starting from `(a,b)` outside D, the next state is `(b,0)`. If this is still outside D it also defaults, giving `(0,0)=p_5` on the next step. Equality `(a,b)=(b,0)` would force `a=b=0`, impossible outside D. Thus the possible two-state transient prefix is distinct. Closure of D precludes any later return to an outside state.
- **Uniformity check:** An outside target is visited at most once over the entire path, while an inside target has L-spaced visits after entry. These two cases exhaust all targets and prove the full later-block assertion, including a block straddling the transient/closed-support boundary. Expected occupation inequalities follow by integrating a pathwise indicator bound, and hold for arbitrary initial distributions and all h.
- **Adversarial checks:** The potentially dangerous repeated transient `(a,b)->(b,0)->(0,0)` is explicitly excluded by the loop rotation. One cannot get this conclusion merely from MM5's earlier `c_5=0`; the added `c_6=0` is load-bearing and is present. Support-graph shortest-return checks found return time L on D and no return outside D for every pair at `K=12,...,27`.
- **Contribution:** This is exactly the all-start occupation control used in the stationary atom bound. No mixing or stationary-start assumption is added.
- **Verdict:** PASS.
- **Repair direction:** None.

### unit_003: Complete base experiment (`lem:full-experiment`)

- **Statement fidelity:** PASS. It preserves every initial observation and gives an actual full-history bijection, not a projection to less-informative data. The terminal pair is `Y_M`, not an appended independent sample.
- **All-residue initialization:** For `M=qL+d`, `k=(2-d) mod L`, the six listed initialization cases cover all residues exactly. Cases k=1 and k=2 place respectively the first A and first A,B uniform factors in the initial law. Cases k=3 and k=4 use the public fixed `v_*`, `w_*`, not an uncounted unknown-row label. The remaining cases start from fixed clock pairs. Every initial law is sign-independent and is legal under arbitrary initialization.
- **Departure indices:** From the established phase invariant, the phase-2 times are exactly `d,d+L,...,d+qL=M`. The first q are observed departures and the last is the unobserved-departure terminal pair. At q>=1, the latest training label occurs at `t_q=M-L<=M-1`; all labels belong to the given full history. At q=0 there are no labels. The M=1 and M=2 initial-data cases are addressed correctly; k=2 with q=0 would imply excluded M=0.
- **Bijection:** The explicit inverse chooses the fixed initial prefix or reconstructs its random initial A/B, appends the next context at phases 0 and 1, the designated label at phase 2, and the fixed public continuations elsewhere. It stops before the terminal label. Repeated appearances of Z in overlapping pairs are the same observed symbol, not independent extra data. Extracting at the fixed indices is the inverse, and positivity of U,V choices and W masses makes every encoded tuple realizable.
- **Exact law:** Multiplying the initial mass and all M transition factors gives `m^(-2(q+1)) product_i q_sigma(Z_i|A_i,B_i)`. There are exactly two uniform factors per context and one unknown factor per training label. This factorization proves q iid training triples and one independent uniform actual terminal pair **for this constructed family**, without asserting such independence for general sources.
- **Conditional information audit:** Given any `T=s`, the entire H is still bijective with D through a common public map. Its probability `m^-2` is independent of sigma. No side information, initial symbols, or deterministic copies are discarded in the subsequent testing reduction.
- **Source audit:** Full MM5 Sections 3–4 were independently read and checked against the submitted all-remainder initialization and inverse. The rotation only changes the already-public clock continuation; it does not change the factor count or the terminal index.
- **Supplemental checks:** Exact rational likelihood/reconstruction checks used a nonconstant sign pattern, alpha=1/4, and an extra unused letter: 61,308 tuples for m=3, K=13, M=1,...,26 and 16,624 for m=4, K=17, M=1,...,31. Every phase, including q=0 and partial-prefix cases, was covered. These check the structural/probability identities for their stated instances; they do not claim exhaustive testing of every sign or the horizon-specific capped alpha.
- **Contribution:** Establishes the exact experiment needed for full conditional KL and testing, including initial observations and the actual terminal query.
- **Verdict:** PASS.
- **Repair direction:** None.

### unit_004: Exact invariant law (`lem:invariant-law`)

- **Statement fidelity:** PASS for every `0<epsilon<1`. The constructed stationary law is not presumed from an unverified positive-matrix or regeneration assertion, and no illegal one-step pair reset is used.
- **Legal smoothing:** R samples one uniform successor symbol and retains the shift. Its square has every row equal to the pair-uniform row U. Thus expansion of `P=((1-epsilon)P_0+epsilon R)` gives a nonnegative two-noise component `epsilon^2 Pi_U` in P-squared. Each all-pair entry is at least `epsilon^2/K^2`.
- **Normalized B-series:** With `B=P^2-epsilon^2 Pi_U`, B is entrywise nonnegative and has constant row sum `1-epsilon^2`. Consequently `B^j 1=(1-epsilon^2)^j 1`, and the maximum absolute row-sum norm of B-to-j is the same geometric quantity. The matrix series converges absolutely in a finite-dimensional norm; two-sided geometric telescoping proves it equals `(I-B)^-1`. The row `epsilon^2 U sum_j B^j` is nonnegative and has total mass exactly one by the scalar geometric sum.
- **Invariance and uniqueness:** The valid series shift gives `pi B=pi-epsilon^2 U`, and `pi Pi_U=U` uses the proved normalization. Hence `pi P^2=pi`. For probability rows x,y the rank-one component cancels and the remaining stochastic kernel gives L1 contraction factor `1-epsilon^2<1`, proving uniqueness. Associativity shows `pi P` is also a P-squared-invariant probability, so uniqueness gives `pi P=pi`. This correctly bridges P-squared invariance to P invariance rather than simply assuming they are equivalent.
- **Alternative resolvent:** Setting `nu=pi R` is legitimate after existence and P-invariance are established. Iterating `pi=epsilon nu+(1-epsilon)pi P_0` leaves a nonnegative remainder of mass `(1-epsilon)^J`, tending to zero in L1. The geometric summand masses justify the infinite resolvent identity and every later block sum. Dependence of nu on pi is not circular: the first construction already established pi.
- **Adversarial checks:** I checked the noncommuting expansion, normalization before the rank-one simplification, the direction of row multiplication, the uniqueness/P-invariance step, and the vanishing remainder. All hold. The claim excludes epsilon=0 and epsilon=1, so division by `1-epsilon^2` is within its stated range.
- **Supplement:** Eight finite matrix instances independently agreed with both resolvents and P-invariance. This is numerical corroboration, not a substitute for the exact convergence proof.
- **Contribution:** Supplies the stationary probability actually used to verify class membership and the resolvent needed for the uniform atom estimate.
- **Verdict:** PASS.
- **Repair direction:** None.

### unit_005: Atom and public-beta membership (`lem:membership`)

- **Statement fidelity:** PASS. The conclusion is an all-state `P^2(s,t)>=beta pi(t)` certificate at the fixed public beta, including unused/default pairs and arbitrary initialization. Beta is not made source-dependent or treated as an oracle for a maximal coefficient.
- **Occupation-to-atom calculation:** For the probability nu and each block starting at hL, the all-start occupation invariant gives `sum_(r=0)^(L-1) (nu P_0^(hL+r))(t)<=1`. Since all summands are nonnegative and `(1-epsilon)^(hL+r)<=(1-epsilon)^(hL)`, the stationary resolvent yields `pi(t)<=epsilon/[1-(1-epsilon)^L]`. Reordering is allowed by nonnegativity and also by the preceding L1 convergence.
- **Elementary bound:** Bernoulli's inequality gives `(1-epsilon)^(-L)>=1+L epsilon/(1-epsilon)>=1+L epsilon`. Rearrangement of positive quantities gives `1-(1-epsilon)^L>=L epsilon/(1+L epsilon)`, hence the claimed upper bound `1/L+epsilon`. No small-epsilon asymptotic approximation is used.
- **Finite constants:** Writing `K=4m+r` with `0<=r<=3` and `m>=3` gives `r<=m` and thus `m>=K/5`, including the tight K=15 case. Therefore `1/L<=25/K^2`. The public domain gives `epsilon=8 sqrt(beta)<=8/K^2<=1/18`, so `pi(t)<=33/K^2`. The exact two-noise component is `epsilon^2/K^2=64 beta/K^2`, which dominates `beta pi(t)` because `64>=33`.
- **All-state/source audit:** Every row was smoothed. The two-noise event has the same pair-uniform probability from every source pair, while the atom bound covers every target pair. The initial law is unrestricted by the class and remains the common horizon-aligned law. The stationary law may depend on the fixed hidden sign without being shown to the algorithm.
- **Adversarial checks:** No supported-start minorization, one-step all-pair positivity, or stationary initialization is silently substituted. Floating-point tests at K=12,15,16,19 and epsilon scales 1 and 0.1 times `8/K^2` found positive all-pair margins and the stated atom bounds. The inequalities above prove the complete domain independently of those cases.
- **Contribution:** Puts every member of the finite hard family inside the exact public-beta class before the risk lower bound is applied.
- **Verdict:** PASS.
- **Repair direction:** None.

### unit_006: Full-history conditional binary testing (`lem:conditional-testing`)

- **Statement fidelity:** PASS. The testing bound concerns the complete base history conditional on any actual terminal row, including when the flipped bit is a bit of that very row. Randomized common tests and a single common finite sign prior are covered.
- **KL calculation:** Neighboring signs differ in exactly two W probabilities of one uniformly selected context. Their one-triple KL is exactly `(2 alpha/m^3) log((1+alpha)/(1-alpha))`, in either direction. The exact complete-history likelihood from unit_003 gives q times this expression after conditioning on T=s. This is not a data-processing upper bound from discarding side observations; it uses a bijection on the whole support.
- **Amplitude branches:** `log((1+alpha)/(1-alpha))<=4alpha` holds throughout `(0,1/2]`. In the square-root branch `8q alpha^2/m^3=q/[8(q+1)]<=1/8`. In the capped branch, `m^3>=16(q+1)` gives the same bound. q=0 has KL exactly zero.
- **Finite testing tools:** The stated convexity/log-sum argument collapses KL to the set of positive likelihood differences. Binary KL has second derivative at least four, giving `D>=2 TV^2` and hence TV at most one quarter. The boundary cases are harmless because the support is common and positive; equal laws give zero TV. For any [0,1]-valued randomized test, summing the positive difference mass gives error sum at least `1-TV>=3/4`. An arbitrary independent seed can be integrated into the test kernel, so no finite/deterministic algorithm restriction is introduced.
- **Prior audit:** Pairing the two bit choices with all other signs fixed, then averaging over the entire hypercube, yields conditional bit error at least 3/8. The same sign prior is used for every row and bit. Since every sign gives `Pr(T=s)=m^-2`, conditioning on the actual terminal row does not reweight the sign prior.
- **Source audit:** Full MM5 Sections 5–7 were read; the testing tools and all information conditions used here are explicitly rederived. There is no appeal to the black-box MM5 risk theorem for the changed target.
- **Contribution:** Supplies the conditional testing lower bound applicable to the original predictor restricted to the latent no-noise histories.
- **Verdict:** PASS.
- **Repair direction:** None.

### unit_007: Smoothed actual-target lower (`prop:smoothed-loss`)

- **Statement fidelity:** PASS. The target remains the smoothed row `theta^(sigma,epsilon)_(Y_M)`, not its unsmoothed version. The assertion holds for each common randomized full-history predictor selected using the fixed public K,M,beta, then for its minimax infimum.
- **Latent experiment:** The independent coins are a legitimate construction of the M observed successor mixtures, independent of initial pair, signs, row-randomness seeds, and algorithm randomness. Event E says that precisely these M coins all select the base transition, so its probability is `(1-epsilon)^M`. It does not need an additional initial-pair coin or a future-symbol coin. Conditional on E the complete observed-history law is exactly unit_003's base law.
- **Information audit:** E is not disclosed to the predictor and is not asserted independent of the observed H. Conditioning is only an analytical restriction on a fixed common kernel. All observations, the original initial law, the actual terminal pair, and the independent algorithm seed remain present. The joint conditional prior is uniform because `Pr_sigma(E,T=s)=(1-epsilon)^M/m^2` is the same for all signs.
- **Changed target:** Uniform smoothing adds the same epsilon/K to both coordinates in each label pair, so the actual target contrast is exactly `2(1-epsilon)alpha sigma_(s,j)/m`. A wrong order test forces predicted contrast to be at least this far from the true contrast. The two-coordinate triangle inequality yields TV contribution at least `(1-epsilon)alpha/m` per wrong bit. Negative-sign ties are errors and satisfy the boundary inequality; positive-sign ties require no contribution. Pairs of coordinates are disjoint, and all remaining coordinates add nonnegative loss.
- **Conditional averaging:** Given E,T=s, unit_006 applies to the unchanged common randomized test on the full reconstructed history. The single finite sign prior contributes at least 3/8 per bit. Summing over m-squared terminal rows weighted by `1/m^2` and b bits gives `(1-epsilon)^(M+1) 3alpha b/(8m)`. Since `b/m>=1/3` for m>=3, this is at least `(1-epsilon)^(M+1)alpha/8`.
- **Quantifier audit:** Loss outside E is discarded only by nonnegativity; no comparison between arbitrary old and new TV losses is asserted. Every finite-family source already belongs to D. For each fixed A, its class supremum dominates its finite-prior average, then the infimum over A preserves the common lower bound. Beta-dependent algorithm choice is permitted because beta is fixed before this argument. Neither infimum/supremum reversal nor one sign simultaneously hard for all algorithms is claimed.
- **Adversarial checks:** The survival exponent M and extra target-contraction factor `1-epsilon` have distinct justified origins. Conditioning on a latent event is not used to supply extra observable information. The proof does not replace the actual endpoint by a query sample, condition on a sign-dependent terminal marginal, or rely on an invalid pointwise TV contraction lower bound.
- **Contribution:** Establishes the stronger finite-family expression requested by the contract with the actual changed target.
- **Verdict:** PASS.
- **Repair direction:** None.

### unit_008: Capped rate and bounded survival (`prop:capped-rate`)

- **Statement fidelity:** PASS. It converts the finite-family expression into the required capped rate and proves exactly the stated bounded-survival corollary, example, and separate beta-zero endpoint, without expanding the positive-beta domain to K<12.
- **Capping:** `alpha/8=min(1/16,t/64)>=min(1,t)/64` is valid for all t. If q=0, `t=m^(3/2)>1`, giving at least 1/64, already stronger than the requested capped constant. Thus small M and no-training cases do not require asymptotics.
- **q>=1 comparison:** `q+1<=2q<=2M/m^2`. With `m>=K/5>=K/8`, `t^2>=m^5/(2M)>=K^5/[2*8^5(M+1)]=z^2/256^2`. Both z<=1 and z>=1 then give `min(1,t)>=min(1,z)/256`. Hence `alpha/8>=2^-14 g>=2^-16 g`; the submitted constant deliberately retains valid slack.
- **Survival conversion:** For epsilon<=1/18, the proved elementary inequality `log(1-epsilon)>=-2epsilon` yields `(1-epsilon)^n>=exp(-16n sqrt(beta))`. Thus the extra condition `n sqrt(beta)<=2` gives the explicit `exp(-32)` factor. No unquantified tail or hidden constant is introduced.
- **Upper interface:** I read the exact L1MAX definition of counts, target, and risk, and its complete Section 8 L1+ conclusion. It applies uniformly over every fixed homogeneous theta and arbitrary initial law, with exactly M observed departures and the same terminal pair. Restricting that source class to D proves the upper for the **original** add-one predictor, not a suffix or altered algorithm. Choosing that permissible common rule gives `R_D2<=R_D2^+`. This is valid inherited evidence rather than a fresh review of every L1MAX proof lemma.
- **Concrete sequence:** At `M=K^4`, `beta=K^-8`, `n sqrt(beta)=1+K^-4<=2`, beta is in range, and `K^5>=K^4+1`, so g=1. The claimed constant-risk conclusion follows exactly, though the numerical lower constant is small.
- **Zero-beta boundary:** The finite-state Cesaro construction correctly provides a stationary probability for every legal pair kernel: the averaged law stays in a compact simplex and its P-invariance defect is bounded by `2/J`. Therefore D at beta zero is the original full class. The accepted MM5 and L1MAX endpoints apply for all K>=2. This does not evaluate `(I-B)^-1` or divide by epsilon at zero. MM5's inherited small-K GU interface is not independently re-proved by this review.
- **Scope audit:** The proof expressly declines sharp all-beta rates, optimal survival exponent, necessity of burn, full weak-window closure, and implementation/resource claims. The example `M=K^4,beta=K^-6` is correctly not declared a constant-risk consequence.
- **Contribution:** Completes all constants and exported rate interfaces in the frozen target without dropping exposed K,M,beta dependence.
- **Verdict:** PASS.
- **Repair direction:** None.

## Hidden Subclaim Scan

No unreviewed independent mathematical premise was found. The nontrivial supporting claims are located and checked as follows:

1. Finite Euler existence, public rotation, and disjoint legal table: unit_001.
2. Closed phase propagation and transient nonrepetition for all starts: units_001–002, with named phase and transient-entry invariants.
3. Exact source-independent complete-history inverse and factorization, including all residue prefixes: unit_003.
4. `R^2=Pi_U`, positivity and normalized resolvent, convergence, uniqueness, and P-invariance: unit_004.
5. All-start occupation summation and stationary atom/minorization constants: unit_005.
6. Finite KL-to-TV/testing inequalities, both alpha branches, randomization, and common conditional sign prior: unit_006.
7. Coin conditioning, target contrast, sign-error loss, actual-row averaging, and minimax order: unit_007.
8. Capped finite comparison, exponential conversion, class restriction for L1+, and finite-state beta-zero stationarity: unit_008.

The latent E is a proof event with an exactly established probability, not an added theorem hypothesis. The generated invariant law, support closure, and occupation control are conclusions before use. Ordinary finite-dimensional algebra, convexity, geometric summation, and compactness do not conceal an imported source theorem or an unproved mixing condition. The diagnostic is not used as mathematical evidence.

## Target Claim Audit

All six explicit S010 contract obligations are discharged:

- The actual inherited four-alphabet MM5 mechanism is implemented on legal second-order rows, including every default row, with the stronger loop placement proved.
- The no-repeat occupation invariant is genuinely all-start, with entry within two steps and no repeated transient prefix.
- The stationary distribution is constructed, normalized, proved unique and P-invariant, and both infinite-series limits are justified.
- Public-beta membership is checked for all source/target pairs using explicit `33/K^2` and `64 beta/K^2` bounds.
- The full conditional observation experiment, actual target, unchanged common predictor information, randomized tests, and conditional sign prior are preserved. The changed-target loss is independently decoded rather than imported from MM5 risk.
- Capped finite constants, the bounded-survival corollary, concrete sequence, inherited upper, separate zero-beta endpoint, provenance, and negative scope boundaries are correctly stated.

The minimax source supremum may choose the fixed source and initial law separately for each public K,M,beta and each algorithm, as allowed. There is no changing source within a trajectory or extra stationary initialization requirement. Source law pi and latent coins remain hidden. No positive-beta claim is made for K=2,...,11.

## Explicit Rate Audit

- Exposed variables are exactly K,M,beta; n,epsilon,m,L,q,alpha,g are explicitly defined from them.
- Norm and probability mode remain expected half-L1 TV, averaged over the true source path and any source-independent algorithm randomization.
- The horizon is fixed: M observed departures, n=M+1 in the survival-times-target expression. The lower-bound initial law is allowed to depend on M. There is no all-horizon claim for one fixed initialization.
- There are no unspecified constants. The new constants 8, 33, 64, 3/8, 2^-16, and 32 each have a displayed derivation or direct parameter definition. The 48 is identified as inherited L1MAX evidence.
- The two conditional-probability conversions have exact factors: `(1-epsilon)^M` for E and `1/m^2` for the actual terminal row. The additional `(1-epsilon)` is target contrast, not event probability.
- The q=0, q>=1, both alpha branches, odd/even m, extra alphabet letters, default rows, ties, M=1, M=2, and all initialization phases have explicit coverage.
- The corollary uses the exact threshold `n sqrt(beta)<=2`; outside it only the displayed survival lower is claimed.
- The positive-beta lower tends to `2^-16 g` for fixed K,M as beta tends to zero. The zero-beta theorem itself is separately inherited with its all-K scope. No singular resolvent substitution is used.

## Notation Surface Audit

The proof separates the exported n,g,epsilon interface and optional finite-family parameters from proof-local alphabets, Euler word, phases, kernels, prior, event, and tests. The row count `n_s` is explicitly distinguished from n=M+1, and q replaces MM5's earlier training-block variable n without changing the count. The original legal pair kernel and actual target definitions are retained. Every proof-local helper has a construction or derivation before load-bearing use; no named admissibility package hides an assumption. The mathematical assembly refers to named local results, not merely unit identifiers.

## Target-Step Assembly Audit

The chain is complete:

1. Lawful rotated clock plus all-start one-visit proves the base source geometry.
2. Exact invariant law plus occupation control proves a stationary atom bound for the legal smoothing.
3. The two-noise component and atom bound place each member in D at the given public beta.
4. The complete base experiment and conditional testing control neighboring full histories on the latent no-noise event.
5. The smoothed actual-target contrast gives the correct wrong-bit TV cost; the common prior and actual-row average yield `(1-epsilon)^n alpha/8` for each predictor's supremum.
6. Capped finite comparison yields the requested lower, and the bounded-survival conversion plus exactly inherited L1+ yields the corollary.

Neither MM5's black-box risk inequality nor the diagnostic is used in steps 1–5 as a substitute for the modified argument. MM5 is attributed for reused construction/testing, and used as a black box only at the separately stated beta-zero endpoint. L1MAX is used only for the original full-history upper. No S001–S009 proof is required for the positive-beta derivation.

## Source, Interface, and Evidence Binding

### Exact inherited interfaces checked

- **MM5:** The source's Sections 2–4 supply the actual legal clock and full experiment, Sections 5–7 the finite testing construction, and Section 8 the finite constants/endpoint. These sections were read in full, not inferred from the old report. The obsolete upper-gap discussion in MM5 Section 9 is not a mathematical premise here.
- **L1MAX:** Its exact L1+ interface is uniform over fixed legal theta and arbitrary mu, all K>=2,M>=1, and uses the same complete history, counts and actual terminal pair. Only this interface is inherited; no implementation, neural, precision, fault, or cost statement is imported.

**L1MAX actual scope:** readable lines 1–150 (its full Sections 1–3 and beginning of Section 4), plus its complete Section 8, lines 327–379. This includes the exact source/initialization/data/target definitions and the precise L1+ upper/interface. Its remaining proof sections were not independently reviewed here.

**Not used/read as a mathematical dependency:** the global weak-mixing diagnostic, S011, or S001–S009 proofs/reviews. The review did not inherit acceptance from a diagnostic summary. The original GU/SRC proofs and the entire L1MAX upper derivation were not re-audited, and no such claim is made. No external-paper theorem is required for S010's new derivation; no web search was used.

The command completed successfully with status PASS. It independently constructs a loop-rotated Euler word, full legal base table, graph, history reconstruction, and smoothed matrices rather than executing author-supplied test code. Its precise finite scope is:

- K=12,...,27: all K-squared source pairs, legal row normalization, phase advancement, at-most-two-step transient entry, and no return shorter than L on the closed support/no return outside it.
- m=3 with M=1,...,26 and m=4 with M=1,...,31: all encoded context/label tuples for one stated nonconstant sign pattern and rational alpha=1/4, all initial phases, exact rational full path likelihood and reconstruction, totaling 77,932 cases.
- K=12,15,16,19 and epsilon equal to `8/K^2` or `0.8/K^2`: matrix B nonnegativity and row sums, normalization and P-invariance of its resolvent, agreement with the P0 stationary resolvent, atom bounds, and every-pair minorization. Maximum numerical normalization discrepancy was below `8.7e-12`; maximum invariance and alternate-resolvent discrepancy below `2.7e-15`. These are floating-point sanity checks, not interval-certified estimates or universal proofs.

## Review Rationale

ACCEPTED is the smallest correct outcome: all eight local units pass and their composition proves the exact frozen target. The difficult new interfaces are explicitly justified rather than delegated to the old lower theorem: the loop placement repairs outside-support occupation, the normalized B-series establishes the stationary law, the all-start occupation estimate makes the public-beta coefficient valid for every pair, and full-history testing is redone against the actual smoothed row under one conditional sign prior. Finite caps and the inherited upper preserve the original experiment.

There is therefore no mathematical revision obligation or dependency block. This is one independent LLM proof-step acceptance of this exact version and scope, not a formal certification, literature-wide novelty finding, or closure certificate for the larger weak-mixing research program.
