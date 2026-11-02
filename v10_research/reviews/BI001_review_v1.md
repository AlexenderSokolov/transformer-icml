# BI001 independent hostile review — v1

Date: 2026-11-02. Reviewer: independent LLM reviewer.

## Result first

**PASS of the mathematical lower BI1, with an explicit upper-comparison scope qualification.** I found no fatal gap in the supplied candidate. This is a recommendation to the root reviewer, **not acceptance**. The candidate and accepted dependencies were not modified.

The binary construction genuinely proves the advertised stationary rare-suffix lower with cutoff `max(sqrt(beta),1/M)`. In particular it closes the binary no-mixing-constraint logarithmic lower in this fixed-dimensional one-global-block local-ratio family. It does **not** determine the optimal positive-beta binary cutoff. The same beta=0 bound holds throughout `beta<=M^-2`, because the constructed cutoff is then exactly `1/M`.

For a matched upper/lower statement using SB001, explicitly retain **D>=8, r>=3, legal dyadic Q in the square-root band, and a sufficiently large fixed target-risk multiplier**. BI1's lower holds for every fixed D,r>=1; the SB001 upper is not established for every such small architecture. The manuscript's shorthand “the order is matched there” must be read with these inherited upper-inclusion qualifications, not as feasibility at all D,r or all arbitrarily small risk constants.

## Materials and independence

Read the complete BI001 candidate, BA001's model and proof, SH001's exact model and necessity argument, UI001's uniform-IID theorem and proof, SB001 v2's construction/inclusion/upper, and their acceptance records. Source hashes are recorded in `BI001_independent_checks_v1.json` and the review binding file. I derived the pair kernel, stationary distribution, reference-chain powers, likelihood ratio and constants independently. The diagnostic script is newly written, not a reuse of the author's checks. A later root message reported a compatible preliminary judgment; this review's initial source, coupling and endpoint checks preceded that message.

## 1. Model and stationary initialization

The experiment is SH001's bounded local positive-weight ratio model, **with its K>=3 restriction replaced by K=2 for this new theorem**. The inherited conditions `kappa>=1`, `Q>=1`, `D,r>=1`, source-independent tables/seeds, dense M-position denominators, bounded values, fixed boundary side information and unrestricted post-grid decoder remain essential. This is not a lower for unrestricted deep/global computation or arbitrary history side channels.

In pair order W=00,A=01,B=10,C=11, the one-step kernel derived directly from the four binary next-symbol rows is

```
P = [1-a, a,   0,   0]
    [  0, 0, 1-p,  p]
    [  e,1-e,  0,   0]
    [  0, 0, 1/2,1/2].
```

With `x=1/(e/a+2+2p)`, direct multiplication gives `Pi P=Pi` for `Pi=x(e/a,1,1,2p)`, and its entries sum to one. All entries are positive in the stated domain. This is an actual stationary initialization, not a deterministic W start or a fictitious p-independent stationary law. Pi depends on p, and no decoder access to it is granted. Since `e/a>=2` and `2+2p<=7/2`, `Pi_W>=(2)/(2+7/2)=4/11`.

I independently multiplied all 16 entries of P² and obtained exactly the candidate's matrix. There are no unsupported initial states to omit. The following analytic inequalities check the all-state certificate, not merely typical-state mixing:

* `a<=1/128`, `1/M<=e<=1/16`, `e²>=beta`, and `e>=4beta`.
* Column W: all nontrivial entries are at least `e/4>=beta`, while `(1-a)²>=beta`. Since `Pi_W<=1`, all dominate `beta Pi_W`.
* Columns A,B: `x<=a/e`. The smallest special entry is `ea>=beta a/e`, precisely by `e²>=beta`. The row-W entries `a(1-a)` and `a(1-p)` are at least `a/4>=beta a/e`. The remaining entries are at least 1/8, larger than `beta x`.
* Column C: the row-W entry satisfies `ap>=beta(2pa/e)` because `e>=2beta`; all other entries are at least 1/8 and `beta Pi_C<=beta<=1/256`.

Thus the constructed homogeneous source is legal for every specified beta, including beta=0. No larger-beta claim is used.

## 2. Rare-event geometry and exact density

Let the history length be n=M+2. An event E_j has n-j initial zeros followed by a suffix of j bits whose first bit is 1 and which never visits 00. The pair at that first 1 is A. There are exactly `M-j` zero-to-zero transitions after the initial pair and before the launch, one launch of probability a, and j-1 subsequent transitions.

Relative to the chain R started at A, each actual active B transition incurs a factor `1-e`; all other suffix transition probabilities agree exactly. Consequently the displayed Radon–Nikodym factor

`Pi_W (1-a)^(M-j) a (1-e)^N_B`

is exact. Its lower bound is uniform in path and p: use `Pi_W>=1/4`, `(1-a)^M>=1/2`, `N_B<=j-1`, and `(1-e)^j>=1-ej>=3/4`. The resulting `3/(64M)` exceeds the stated `1/(32M)`. Different j have different first-1 locations, so the events are disjoint.

Importantly, E_j generally has p-dependent probability. The proof does **not** use its conditional law or claim a uniform posterior after E_j. It integrates the pointwise density lower against the same uniform p prior and the reference path law. This is sufficient for averaging the lower bounds over all j. The additional oracle j strengthens the decoder only; the reference experiment need not itself be an admissible stationary source.

## 3. Mixing, arbitrary positional tables, overlapping windows

Direct matrix powers give

`R²(:,B)=(p/2,1-p,1/4)` and `R³(:,A)=(p/2,1-p,1/4)`.

The second equality is not a mistaken copy: B is the only state with an incoming one-step edge to A, and that transition has probability one. The shared atom `(1/8) delta_B` is therefore available for every two-step transition law uniformly over p and starting state.

For the coupling, start two reference chains at the two possible next states following a common prefix. At two-step boundaries use the common atom, and fill each intermediate step by its correct conditional Markov bridge. Once the boundary states agree, use common transitions thereafter. This construction has the correct entire path marginal for each chain. A block has at most two differing states and the probability of reaching block b without guaranteed coalescence is at most `(7/8)^b`. Hence expected differing state count is at most 16, including the initial differing state. Extend chains beyond a finite horizon if needed; truncation can only lower the count.

The emitted bit is a function of the pair state, so the number of differing bits is no larger. For arbitrary position-dependent trailing-window functions, each differing bit affects at most r summands, and each summand changes by at most `2 kappa`. This proves an expected total difference bound `32 kappa r`, with the candidate's `34 kappa r` safely slack. Fixed prefix terms cancel. Windows crossing the zero-prefix boundary and short/padded windows obey the same incidence count. Even if r exceeds the history length, each bit is in no more than r displayed windows.

Revealing successive transitions gives a Doob martingale whose conditional next-state expectation range is bounded by `34 kappa r`. Orthogonality of increments therefore implies the stated variance bound. This argument does not assert independence of overlapping windows; their covariance is controlled through the martingale coupling.

For the parameter derivative, differentiate the finite product of transition factors, inserting R' at one time. R' is zero off row A and has signed entries -1,+1 to B,C in that row. Given a common prefix ending at A, the derivative contribution is precisely a difference of continuation expectations from B versus C. The past cancels; the same coupling bound applies. Summing over at most j-1 insertion times gives `34 kappa r j`, not j². The tables must be independent of p, as required. Time-inhomogeneous tables cause no problem because the coupled paths use the same time index.

For any j>=4, factor `R^(j-1)=R^(j-4)R³`; the final A probability is at least 1/8. This holds for the reference law without conditioning on boundary side information.

## 4. Boundary-query freezing and complete message tube

Freezing each possible binary boundary pattern before expectations is necessary and done correctly. The number of patterns is at most `H=2^(2r)`, including consistent overlaps; unattainable patterns need not be counted. Arbitrary real query values cannot create additional labels beyond these patterns. Simultaneous control of every frozen branch avoids the false claim that the chain retains its original law after conditioning on the observed boundary.

Numerators and denominators are each sums of terms bounded in absolute value by kappa; deterministic prefix contributions do not affect variance or derivatives. The denominators and their expectations are at least M, and the absolute mean numerator does not exceed the mean denominator. With the displayed T, union-Chebyshev gives exactly

`2DH * (34r)²/T² = 1/32`.

Exact ratio subtraction gives the tube radius `2 kappa T sqrt(j)/M`; quotient differentiation gives `68 kappa r j/M`. These use ratios of means, not means of ratios.

The scaled tube radius is at most T by the chosen cutoff. An economical equally spaced mesh of the interval of length 1/2 has at most `2+34r zj/M` points, within the manuscript's larger count. Derivative approximation adds at most one scaled unit and flooring less than one. A radius-(T+2) interval contains at most `ceil(2T+4)+1=N` integers. Thus the displayed `A0(1+zj/M)` includes the entire bank and boundary side label. Negative numerator values and noninteger real Q create no exception: Q times a returned grid value is still an integer.

Encoder seeds may determine different meshes, but the conditional cardinality bound and the prior are seed-independent. Granting the seed to the decoder and then averaging is valid.

## 5. Informative endpoint and common-prior Bayes calculation

Only terminal A has target Bernoulli(p). Discarding the nonnegative loss at B,C is legitimate, but would invalidate a naive whole-path IID or uniform-posterior argument. The candidate instead uses the correct target-specific finite-alphabet argument.

For every p, the joint event of being good and ending at A has probability at least `1/8-1/32=3/32`. For any fixed decoder seed, the union of radius `ell/(64R_j)` intervals around all good-message scalar outputs has uniform-prior probability at most 1/32. It is safe to subtract this prior probability from the joint good-A probability; no independence from the path or goodness is needed. The remaining joint probability is at least 1/16. On it binary TV loss is at least `ell/(64R_j)=1/(128R_j)`. The resulting `1/(2048R_j)` bound is correct.

Average decoder seeds, then encoder seeds, always retaining the same uniform p prior across j. Integrating the exact pathwise domination and adding disjoint E_j yields the stated coefficient `1/(65536 A0 M)`. The source supremum dominates that common-prior average, uniformly in all encoders; encoder/decoder infima preserve the conclusion.

## 6. Integer cutoff, constants and necessity

Both real cutoff terms are at least four, so J>=4, including the worst boundary `e=1/16,z=M/4` where only j=4 remains. Also J>=U/2, J<=M/4, eJ<=1/4, and `z sqrt(J)/M<=1/2`. No empty suffix sum is hidden.

For `u=z/M<=1/4`, writing j=k+4 gives

`1+u(k+4)<=(1+4u)(1+uk)<=2(1+uk)`.

The decreasing-sum integral on `[0,J-3]` and `J-3>=J/4` imply

`sum_(j=4)^J 1/(1+uj) >= log(1+uJ)/(8u)`.

The logarithmic scaling uses `log(1+x/4)>=log(1+x)/4`. Floor loss gives `uJ >= (1/8) min(z/(Me),M/z)`. Multiplying constants indeed yields `c=1/(524288 A0)`.

At beta=0, e=1/M, so the lower has SH001's same expression with a new architecture-only constant. SH001's necessity case split applies: if z>M/4 the budget is already of order sqrt(M), while within the tube domain the two log branches force kappa of order log(M) in a fixed square-root Q band. This does not invoke a tube outside its domain. The identical implication holds for beta<=M^-2. UI001 is compatible and supplies a separate kappa-uniform c/Q floor; it is not needed to repair any step of BI1.

## 7. SB001 compatibility and topology-specific obstruction

SB001 explicitly allows K=2 for its upper. Its terminal dense bank then has eight scalar triple coordinates, weights exactly in `{1,kappa}`, values in [0,1], local window length three, and exact terminal pair side information contained in the permitted boundary grant. The two preprocessing copy heads implement those local windows; they do not give the decoder an extra interior message. All terminal M keys have positive weights. Thus its upper fits the BI comparison family when D>=8,r>=3. Arbitrary-start upper guarantees imply stationary upper guarantees. The accepted upper remains a changed finite program with legal dyadic Q and integer kappa, not an implementation of arbitrary real tables.

Finally the proposed same-topology obstruction is exact:

`P²(B,A)=ea`, `Pi_A=1/(e/a+2+2p)`, hence `e²+ea(2+2p)>=beta` is necessary for this source's certificate.

When e,a are both of order 1/M this forces beta=O(M^-2). This says nothing about other binary topologies or the best achievable binary lower at intermediate beta. The candidate appropriately does not elevate this calculation to a universal impossibility theorem.

## 8. Independent diagnostics and evidence limits

Executed `python reviews/BI001_independent_checks_v1.py` successfully. Results:

* symbolic exact stationarity/normalization, full 4x4 P², both active-chain columns, and the topology-obstruction identity;
* 75 rational parameter cases testing every minorization entry, including extremal p and e;
* 675 enumerated reference paths for j=4,...,10, with exact original-history probabilities equal to density times reference probability and the uniform density bound;
* 336 exact positional/query-dependent local-sum cases, including overlapping windows, signed numerator values and positive denominator weights; exhaustive conditional Doob ranges, exact variance and exact parameter derivatives satisfy all bounds;
* 60 cutoff and harmonic cases, including J=4; cutoff arithmetic and harmonic sums are rational-exact, while logarithms are checked at 80-digit precision.

Finite checks corroborate but do not establish the universal theorem; the preceding coupling, likelihood and Bayes arguments provide the mathematical justification. No formal proof assistant, external novelty search, new network execution, publication or upload was performed. Review artifacts remain local. There are no unresolved blockers to the lower theorem; upper-comparison qualifications above should remain explicit in any root acceptance or downstream corollary.
