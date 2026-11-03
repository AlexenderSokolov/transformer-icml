# Independent first-order upper audit

Date: 2026-11-02. Reviewer: an independent LLM reviewer. **PASS for the revised, byte-bound upper candidate and known-budget sandwich, within the scope below.** No positional lower, logarithmic necessity, minimal-message claim, old triple-count result, or manuscript replacement is accepted by this review.

## Sources and method

Read the complete `UPPER_CANDIDATE.md` and `PLAN.md`; read the entire actual `positional_manuscript_20261102/sections/proofs_positive.tex`, including all generic proofs and their source-specific specializations, not merely lemma names or receipts. Inspected the actual oracle-floor addition diff and the later domain/normalization clarification diffs. Independently checked the algebra, stochastic dependencies, boundary cases, dimensions, and quantifier directions. Supplemental executable finite checks are `checks.py` and their observed output `checks_output.json`; these do not replace the analytic proofs.

Final bindings are in `bindings.json`. Sources were not edited by this reviewer. Root revised the two initially reported issues, preserving before/diff artifacts:

1. Originally the term competitive factor did not distinguish normalization by explicit `g` from exact known-budget minimax. The revised definition is explicit, fixes one map for all budgets at each `(N,r)`, and correctly pays 96 for conversion to exact-oracle normalization.
2. Originally the budget domain was not explicit. The revised files require integer `N>=64`, `0<=k<=N`, `1<=r<=N+1`. This is necessary for the stated uncapped `g/96` lower and its displayed simplification.

No remaining blocking issue found after these revisions.

## 1. Experiment and exact two-state hitting scale

The word has `N+1` symbols, `N` departures, four edge counts, and one protected terminal symbol. For a binary row, predicting its flip probability induces a valid two-symbol distribution; its TV loss is absolute error in that flip probability. Histogram row sums recover J and the off-diagonal cells recover C. Protection preserves the selected row under every attack realization. No certificate enters the argument.

For `a,t>0`, stationarity is `(t,a)/(a+t)`, maximum ordinary hitting means are `1/t,1/a`, and reciprocals of stationary masses are `(a+t)/t,(a+t)/a`. Thus `h=(B/t,B/a)`, `B=max(1,a+t)`, and the weighted sum is exactly `aB/(a+t)+tB/(a+t)=B<=2`. This includes periodic deterministic alternation `a=t=1`; none of the imported arguments requires aperiodicity.

For `a=0<t`, state 0 is absorbing. Starting in 1, an endpoint in 1 implies no previous hit of 0, and appending the next 1-to-0 transition gives exactly `t P(X_N=1)=P(D_0=N+1)`. Reset-row first-hit density with d=2 gives `2/(N+2)`. Starting in 0 gives zero. Mixtures follow by linearity. Symbol exchange covers `t=0<a`, including deterministic exit. For `a=t=0`, each state is absorbing and both true flip weights are zero, for every initial mixture. These exhaust reducible binary transition tables. Although attacks can create apparent flips, the stochastic weighted terms vanish, not necessarily the estimator loss; the deterministic perturbation and empirical terms still account for that loss. No irreducible-only lemma is applied directly on a reducible boundary.

## 2. Reuse of the actual generic proofs

* **Occupation:** the decreasing worst-start suffix probability and the pathwise bound of at most `dw` low-prior-visit occurrences imply `d^2 w/(N+1)` without stationarity or irreducibility. At d=2 this is `4w/(N+1)`.
* **Kac:** finite irreducibility ensures finite hitting/return expectations; expected excursion occupation is invariant and its target coordinate is one. The proof uses no source-order structure and allows periodic chains.
* **Return trace / first hits:** the Schur-complement identity and formal logarithmic trace series give `sum_j P(T_j=s)/j<=d/s`, including defective returns. Replacing the target row by a deterministic jump to the starting state yields the first-hit density. The auxiliary chain need not remain in the model, which is legitimate for this universal bound.
* **Endpoint and tails:** the Poisson hitting identity yields expected occupation; loop rotation bounds returns and splitting first hits bounds endpoint mass. Survival-conditioned hitting/return laws have mean at most h, giving the stated moment induction and exponential transforms. The lower occupation tail uses fresh return cycles before horizon restriction. The joint upper tail is proved through the explicit tilted stochastic matrix, with path likelihood `e^{-lambda ell} f^{-J}/h_i`; it is not an unjustified product of endpoint and occupation probabilities. All these proofs are generic finite-state arguments.
* **Imbalance:** conditional future endpoint control can be multiplied by the unconditional first-half lower tail because the endpoint bound is uniform over the conditioned split state. The second-half term uses the joint bound. The deterministic implication uses `m<=2n` and `np>=1`, giving ratio at least `1/145>1/256`; small-mass targets use endpoint control alone. The maximum of `(x+1)e^{-x/8}` is below 4. Thus the generic bound is `288d/N sum p q h`; d=2 and sum<=2 give 1152/N. Reducible boundaries are handled directly as above.
* **Old reciprocal:** post-hit departure count has no extra unit shift; a hit at t leaves exactly `N-t` transitions in the return kernel. A positive old count forces `t<=N-m-1`, hence harmonic cutoff `s>=m+1`. Zero terminal count is included via first-hit density at N, even when the gate is true at zero. Summing targets gives `(3d^2+2d^3)L/N=28L/N` at d=2. No dependence on the threshold c is needed after the positive-old-visit implication.
* **Weighted minimum:** the generic target split at `h>N`, and otherwise at `J>=Np/48`, gives `384d^2 A/N +192d sum p q h/N`. Prefix conditioning in the low-count branch is valid and its exponential maximization is safe. Substitution gives `1536A/N+768/N`. The direct reducible bound is smaller.

The certificate-specific four-state support/hitting calculations and reflected three-state reduction are NOT imported. They are unnecessary here and do not constrain binary first-order tables.

## 3. Two-row empirical comparison

Build two independent Bernoulli stacks, independent of the initial symbol. Each departure consumes one variable in its row; path probabilities are the desired products, including q=0 or 1. The terminal empirical residual is the selected stack partial sum, but no conditional independence at the random selected row/count is asserted.

For a dyadic v, the two-sided union over two rows gives tail `4 exp(-x^2/v)`, no larger than the actual proof's `8 exp(-x^2/v)`. Occupation gives `P(v<=J<2v)<=min(1,8v/(N+1))`, no larger than the proof's `p_v=min(1,32v/(N+1))`. Consequently every bound in its event/tail integration, using the conservative 8 and 32, still holds unchanged. The two dyadic series bounds are below 56 and 236 times `(N+1)^-1/2`; their sum is below 512. At most `2N` stack variables per row are needed. Thus 512 is valid with two rows for arbitrary starts and all transition boundaries.

## 4. Suffix reconstruction and deterministic gate

The last `m+1` symbols expose `m` edges, starting at `N-m`, and exactly the m departure states in `N-m,...,N-1`. The symbol `X_N` is not a departure. Hence `m=min(r-1,floor(N/2))`, and subtracting the suffix row count from J gives a direct old-prefix count on both clean and corrupted words. At r=1, m=0 and O=J. At maximal r the old prefix still contains the full first half. Prefix raw symbols need not be used by the estimator; ignoring allowed information is legal.

A symbol edit changes at most two edges and at most one occurrence in any fixed departure-index set. Therefore `|C'-C|<=2k`, `|J'-J|<=k`, `|O'-O|<=k`; the reused simultaneous 6k bounds are conservative. Subtraction does not double the O perturbation because it is exactly a direct count. The accepted pathwise proof then applies without change: ratio perturbation on accepted/true gates costs `48k/(J+1)`; false acceptance forces `J<6156k`; false rejection off imbalance forces `J<3078k`. The enlarged integer thresholds cover J=0. Equality is accepted, and k=0 introduces no false-status cases at positive J. Attack randomness is handled pathwise.

Using d=2, the two occupation tails sum to `(36936k+8)/(N+1)`. Old reciprocal contributes `48*28=1344` times `Lk/N`. Imbalance is at most1152/N including reducible cases. Thus the non-corruption terms are bounded by `512/sqrt(N+1)+1160/N<=657/sqrt(N)<=1024/sqrt(N)` for N>=64. This proves equation (4), including its cap at one.

The conversion `1024+1344+36936=39304` uses L>=1 and the definition of g. Also `m+1=min(r,floor(N/2)+1)` and `L<=ell+ln2<=2ell`. Therefore the revised **g-normalized** factor `2^17 ell` is valid. With the oracle floor it yields the separately stated `96*2^17 ell<=2^24 ell` exact-oracle-relative bound. These are not the same normalization.

## 5. Separate exact scan-bit model

Condition on the complete first-half path and its target count j. The remaining horizon m2 is deterministic; the balance event implies suffix count at most1023j. Universal suffix occupation bounds the fixed-target terminal event by `d^2(1023j+1)/(m2+1)`. Dividing by j+1, summing d targets, and using `m2+1>=N/2` gives `2d^3*1023/N=16368/N`, including j=0. Hence `48*16368+36936=822600<2^20`.

The encoder bit is computed on the full corrupted word, then transmitted exactly. It is neither a sampled raw coordinate nor a faulted message. The histogram/terminal decoder's separate J'>0 check handles zero counts even though the bit then equals one. This proves the scan-bit upper only; no minimality is inferred.

## 6. Known-budget upper

For k>=1, protected-edit bounds imply the lower-envelope estimator is between zero and clean C/(J+2), with residual at most `(24k+2)/(J+2)`. The min-function Lipschitz argument gives twice the clean empirical loss plus `min(q,A/(J+2))`; at J=0 the estimate is zero and the latter term equals q since A>=2. With A<=26k this gives `1024/sqrt(N)+768/N+39936k/N`. For N>=64, `768/N<=96/sqrt(N)`, so the coefficient is `41056<2^16`.

For k=0 the add-one estimator differs from C/J by at most1/(J+2) at positive J. Zero occupation costs at most4/(N+1). The occupation/layer-cake proof gives reciprocal expectation at most4/sqrt(N+1), so 1024/sqrt(N) is safely valid. No scan bit or positional window is needed for either oracle branch.

## 7. Independently rewritten known-budget lower

For the stationary IID subfamily the next-symbol-1 probability is p at both possible actual terminal symbols. Thus all predictors, even terminal-dependent ones, have loss `|output-p|` in symbol-1 orientation. The two IID alternatives separated by `1/(8sqrt(N+1))` have whole-word KL at most1/8 by the stated Bernoulli inequality, and therefore total variation at most1/4. Nearest-target testing gives average absolute error at least `3/(128sqrt(N+1))>=1/(64sqrt(N))`. Data processing covers any coarser observation and randomization.

The strict quantizer is a single source-independent kernel for each k: retain a uniform h-subset of existing ones with `h=(k+1)floor(n1/(k+1))`, and keep the last symbol unchanged. Every input and every random outcome changes at most k coordinates. Conditional on n1, any h-subset has probability exactly `1/binom(N,h)` by the displayed combinatorial identity. Conditioning additionally on protected U does not change this: at fixed p, U is independent of the editable IID symbols. Mixing n1 conditional on h and U preserves the same uniform arrangement law. Thus the full corrupted word is a p-independent channel from at most `2(floor(N/(k+1))+1)` labels. The two labels for the protected symbol are retained, not discarded by conditioning.

A source-independent seed can realize that channel for every label; an additional independent seed realizes a randomized decoder. After freezing seeds there are at most D possible real output values. Whatever the p-dependent distribution of the label, error less than v requires p in the union of their radius-v neighborhoods. Under the uniform interval prior, that union has mass at most2Dv/ell0. Integrating its complement yields ell0/(4D). Averaging seeds is valid and preserves the lower bound. The inequalities to `(k+1)/(16(N+k+1))` and then `k/(48N)` hold on the revised domain k<=N.

Taking separate worst-case clean and edit witnesses yields at least max of their two lower rates, hence the claimed g/96 (indeed these conservative displayed constants already imply g/64). The lower holds for the full corrupted word, so it remains valid for pair counts plus boundary windows, even overlapping or full windows. IID sources are stationary first-order sources; inclusion gives the all-start floor. The ordering `g/96<=Rstat<=Rall<=2^16g` is therefore justified for the stated same-information known-k minimax quantities.

## 8. Finite verification evidence and limitations

`checks.py` completed successfully. It exhaustively checked 43,688 clean/corrupted protected-terminal word pairs for N=1..7 and 334,960 window instances, verifying tighter perturbation bounds, suffix reconstruction, and old-prefix domination. It checked 22,960 quantizer combinatorial cases over N=1..40, all budgets and counts, and exact arithmetic for the displayed coefficients. It checked the L/ell index and clean lower inequalities for every r at every N=64..2000.

These finite checks are explicitly supplemental: they are not a verification of every stochastic inequality for all real transition tables or every large-horizon gate configuration. Those claims are supported by the analytic proofs above and the fully read generic proof source. No external writes, repository changes, installations, or edits to the accepted manuscript were performed. This audit supplies an independent local acceptance recommendation for this upper candidate only; it does not supply publication authorization or scientific acceptance for the separate positional lower.
