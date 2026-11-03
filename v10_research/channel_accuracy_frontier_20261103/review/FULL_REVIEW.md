# CAF001 source-bound analytic challenge

2026-11-03. Reviewer: independent LLM reviewer. Verdict: **PASS of the actual bound candidate, conditional on the explicitly accepted source-statistical interfaces; root disposition remains separate.** No external publication or edits to accepted sources. This is mathematical LLM review, not formal verification or external peer review.

## Provenance and what was read

The candidate already existed at first file access. I read the complete candidate immediately, then rederived its bounds and challenged the corner cases. Thus this is an independent reasoning/source-bound review, **not a blind pre-candidate derivation**. I do not claim otherwise. Complete BCC001, BSC001, O2T001 candidates, UMC001 candidate, and all four ROOT_ACCEPTANCE receipts were read. The combined initial source output truncated the middle of BSC001; a separate read of lines 40–135 supplied that entire missing segment. FOT001/2/3 and the underlying statistical manuscript are accepted imports through those interfaces, not freshly re-proved in this review. bindings.json records actual current byte digests, verifies each accepted source hash against its receipt, and binds the candidate and finite checker.

## 1. Statement and model audit

The fixed nominal finite alphabet and fixed d>0, fixed alpha_max<d/2, known radius in its entire closed interval, and hidden channel fixed within an experiment are sufficient for the claimed joint quantifiers. Procedures may depend on radius, M and nominal rows, but not true channel or budget. Noise is fresh conditional on prestate. Physical length counts input slots and is fixed in advance. Separate F suffix-gate and critical-certificate O2 half-gate interfaces are correctly maintained; no first-order upper has been exported to unrestricted O2. Terminal query is next-symbol, free data are exactly corrupted triple counts and protected final pair, and independent coins carry no path information.

The target G_j+2 is feasible, not arbitrarily small. Lower bounds for any fixed finite B are asymptotic obstructions even if B lies below the floor. The use of a minimum feasible integer R is valid once an explicit upper proves the feasible set nonempty, and requires no attained minimax infimum.

## 2. Independently reconstructed lower chain

For any fixed robust procedure its worst case contains nominal W0. At R=0 this gives c_j L, eventually excluding zero length. For overlapping nominal supports the product common submeasure has mass lambda0^R, independent of chosen codewords and retained under arbitrary mixtures. Sampling its normalized version makes a legitimate baseline-only decoder with the same independent seed. Nonnegative loss gives Gamma>=c_j L lambda0^R. As c_j L/B eventually exceeds sqrt(L), this forces a positive multiple of ln L uniformly over radius.

For alpha>0 take Q_b=(1-alpha/2)P_b+(alpha/2)U on the entire stipulated alphabet. Its row TV distance is at most alpha/2, all coordinates at least alpha/(2s), and its two rows remain distinct. Thus kappa<=2s/alpha. The lower theorem needed here is the explicit finite BSC001 implication, as accepted and extended to finite outputs by BCC001 and to O2 by embedded stationary witnesses in O2T001. It is not merely the fixed-channel asymptotic conclusion: N>=2^160 and kappa^R<=N^(1/8) imply Gamma>=2^-32 ln N, with no residual dependence on kappa. Hence if that last factor exceeds B, feasibility implies R>ln(M+1)/(8ln(2s/alpha)). Since ln(2s/alpha)<=max(1,ln(2s))*(1+ln(1/alpha)), the required t term follows with uniform constants.

This remains valid for alpha_M: for each M the finite theorem applies to the frozen witness, and a rule not knowing W is a subclass of allowed fixed-W rules. The original legal predeclared source attack remains unchanged. Likelihood transport multiplies only actual-terminal nonnegative clean loss, after actual nonnegative null-loss transport; it does not multiply target separation or transport a signed lower bound. Arbitrary encoding mixtures and independent shared seeds are expressly handled in BSC/BCC.

For equal nominal supports the fixed finite kappa0 already forces ln M, irrespective of radius. For disjoint nominal supports combine the t lower with integer R>=1. For unequal overlapping supports combine it with ln L. These bounds combine by max>=half the sum; no addition of independent lower risks is assumed. alpha=0 never uses the contaminated witness or divides by zero; t=0 is a definition. Common nominal null symbols are included in contamination, and omitted only from nominal same-support ratios.

## 3. Generic robust test

A={P1>P0} gives p1-p0=d. Every admissible W has q0<=tau-gamma0 and q1>=tau+gamma0 for gamma0=d/2-alpha_max>0. The nominal-event threshold therefore has both conditional errors <=exp(-2R gamma0^2), not just average error. The Bernoulli log-mgf proof and equality/tie conventions are sound. Coupling with identical receiver coins bounds risk by exact risk plus error, so normalizing costs at most sqrt(M). R=ceil(ln M/(4 gamma0^2)) gives extra factor <=1. It uses neither hidden-W likelihood nor calibration. The uniform positive gamma0 is precisely where excluding a moving identifiability boundary is essential.

## 4. Disjoint small-radius branch

Decode S1 as 1 and all remaining symbols as 0; this explicitly assigns nominally null outputs. Under each input the error is <=alpha by row TV. A wrong majority, even with adverse ties, requires at least ceil(R/2) incorrect primitives. Union over subsets yields 2^R alpha^(R/2). At alpha<=1/16, 2<=alpha^-1/4, so this is <=alpha^(R/4). R>=2ln M/ln(1/alpha) yields M^-1/2. Taking max with 1 and ceiling is sufficient for extremely small radius as well as ordinary radius. Dalpha/ln(1/alpha)<=1+1/ln16 bounds constants uniformly. For the large-radius branch Dalpha is bounded by 1+ln16, so fallback O(ln M) is O(t). At radius zero one physical use is exactly correct and asymptotically optimal. No numerical underflow is part of the mathematical rule.

## 5. Unequal overlapping supports: reconstruction and adversarial cases

One nonempty exclusive event suffices, even with strict support inclusion. After swapping channel labels if needed it has P0(E)=0 and P1(E)=p in (0,1). The complementary two-slot inputs have correct probability c=q1(1-q0), wrong probability w=q0(1-q1), and erasure probability q0q1+(1-q0)(1-q1), identical for either semantic gate. Both hits must be erased, and the candidate does this. For alpha<=a_P=(p/24)^2<=p/4, c>=(p-alpha)(1-alpha)>=9p/16>=p/2 and w<=alpha.

Let H count nonerased blocks. Conditional independence and mean H/n>=p/2 give Pr(H<pn/4)<=exp(-np^2/8). Literal real-threshold comparison is equivalent to integer ceiling and has no rounding hole. On a wrong nonabstained decision, with ties included as errors, at least H/2>=pn/8 blocks are wrong. With r=p/8 and alpha<r, mgf Markov at ln(r/alpha) gives Pr(Z>=rn)<=(e alpha/r)^(rn). Because 8e alpha/p<=sqrt(alpha) for alpha<=(p/24)^2 and e<3, this is <=alpha^(pn/16). This argument is valid even when rn<1: Markov is for a real threshold. For alpha=0 wrong blocks are impossible, independent of any majority tie convention because H>0 on nonabstention.

The conditional risk composition is the central point. After sampling receiver coins in advance, losses of baseline and exact estimator are fixed by prestate. Pointwise loss_actual<=loss_exact+1_abstain loss_base+1_wrong,nonabstained. Condition first, apply uniform conditional abstention bound, and average: baseline risk receives exp(-np^2/8), not an unjustified product of marginal quantities. Wrong-decision loss is bounded by 1. This proves G_j+C_j L exp(-np^2/8)+sqrt(M)alpha^(pn/16). Exact independence of abstention from the path is available for fixed W via the symmetric construction, but unnecessary.

The displayed max/ceil n makes each extra term <=1: n>=(8/p^2)ln(C_j L) and n>=(8/p)ln M/ln(1/alpha). Physical length is 2n, no stopping after a useful output. The constant ln C_j and integer rounding are absorbed by ln L for M>=64. In the small branch Dalpha/ln(1/alpha) is uniformly bounded; in the complementary branch Dalpha is bounded above by its threshold value, so the generic test has cost O(t). alpha_max=0 and empty fallback intervals are properly covered. Vanishing p is not a uniform parameter: p is fixed by the nominal channel, and constants may depend on it.

## 6. Uniform threshold, examples and costs

A single M0 can ensure M+1>=2^160, 2^-32 ln(M+1)>B, c_j L>B and L>=(B/c_j)^2. These are monotone conditions solely in fixed interface constants and B. The resulting M0 can be enormous but exists independently of radius, including exponentially and super-exponentially shrinking schedules. The three example schedules follow directly. No claim about the number of calibration samples is smuggled into treating radius as a known input.

All transmitted constructions have O(ln M) length with fixed nominal data/alpha_max. Scanning and count-state costs are inherited correctly. Nominal event tests use fixed alphabet lookup; rational thresholds admit exact comparison. Conservative log bounds can replace transcendental ceilings while preserving sufficient inequalities and constant-factor orders. Reading a long supplied rational alpha is an extra input cost, explicitly not bounded uniformly by polylog M. Arbitrary real data require an access/representation assumption for effective computation. No source or likelihood oracle is charged as free implementation.

## 7. Finite checker and limits

Persisted checks.py uses exact rational enumeration for two-slot multinomial and binary-majority event probabilities; comparison to analytic exponential bounds is floating point with disclosed tolerance. 1080 two-slot cases, 192 majority cases, and 64 log-coordinate length inequalities passed. p ranges from .01 to .99; radius includes zero, threshold, and subthreshold; n includes 1 and noninteger threshold cases. Large log(1/alpha) inputs avoid floating point underflow in the resource check. This catches finite rounding, tie and probability-expression errors, not universal proof or the imported source-statistical lemmas.

No correction is requested. Root should reread the actual candidate and this review, verify bindings, and independently replay checks.py before accepting. If the candidate changes, this verdict binds only the hash in bindings.json; a final-version addendum or renewed review is required.
