# SC002 independent mathematical review

2026-11-02. **Verdict: PASS at the stated finite domain and full-corrupted-history interface.** No blocking mathematical defect found. This is a separately assigned LLM mathematical review, not external peer review, formal verification, or novelty certification.

Frozen theorem: `SC002_theorem.md`, SHA-256 `40a8950861b486f532ac625fa479cb49cd79241dbb4b08efce6296ae9b6a1f0e`. The author and accepted source files were not edited. Later changes are not covered by this verdict.

## Reviewed conclusion

For each fixed K>=3, M>=64, beta in [0,1], and integer 0<=k<=M, both stationary and arbitrary-initialization risks have order

`min(1,max(M^(-1/2),(k/M)[1+ln(1+1/(max(beta,1/M) k))]))`,

with the corruption term defined as zero at k=0. The experiment exposes the entire corrupted word, preserves the final pair, and permits offline randomized symbol replacement without a visible mask or seed. The theorem's explicit lower `2^-15 H` and upper `C_K H` are supported. This is not a binary or joint-K-sharp result.

## 1. Pathwise perturbation and upper transfer

Each edited symbol changes at most three triple locations and each changed triple changes histogram l1 by at most two. Restriction to the preserved endpoint row cannot increase that bound. For positive-mass nonnegative u,v, inserting v/A and using |A-B|<=||u-v||_1 indeed gives TV(u/A,v/B)<=||u-v||_1/A, with the denominator belonging to the clean vector. Thus the selected-row perturbation is at most min(1,6k/(J+K)), even when row membership changes.

R011 ORIGINAL applies to this exact clean full-history add-one q. Its scale max(a,D,T) is at most K^(5/2)/sqrt(M), uniformly in beta; this uses an upper bound only and does not confuse the minimax L scale with the original-rule H scale. The corruption argument does not invoke the more delicate pooled selector.

IU001 Lemma 4.1 has exactly the required stationary actual-terminal clipped reciprocal inequality for every A>0 and integer smoothing kappa>=1. Its 480/(beta A) becomes 80/(beta k). AU001's universal occupation bound works for arbitrary initial laws, including off stationary support. The half-suffix count uses the same endpoint and is pathwise no larger than the full count.

The AU exact mixture is applicable at every pair state: its residual R is stochastic, and its powers define only a residual initial law. Extension to a full suffix uses ordinary P transitions, not R. Therefore the residual suffix is legitimately bounded by universal occupation. No event-conditioned stationary theorem is smuggled into the proof. With m>=M/2 and A=6k, the stationary coefficient becomes 12K² k/M and the residual argument is at most 12K^4 k/M. At beta=1 the residual is omitted; r>=16 ensures no zero-power ambiguity.

## 2. Residual envelope and finite cases

For beta>=1/M, z=M/k>=1 and t=M beta>=1. With D=12K^4, the two cases z<D and z>=D prove `eta Psi(D/z)<=5D[1+ln(1+z/t)]/z`. The steps eta<=e exp(-t/4), ln z<=ln(1+z/t)+ln t and e exp(-t/4)ln t<=4 are all valid. There is no hidden assumption that z is a dyadic precision parameter; the scalar proof works for every real z>=1.

The log coefficient is conservative: `17+ln(1+80x)<=17+ln80+ln(1+x)<=(17+ln80)(1+ln(1+x))`. For beta<1/M the universal Psi bound is at most 6K^4 F, including beta=0; no division by beta occurs. The overall cap yields C_K H even if F>1. k=0 is excluded before every division by k and uses the clean risk only. k=M and all M mod 4 cases are included.

## 3. Full-word erasure and the finite-message lower

The exact combinatorial ratio equals 1/binom(l,r). Conditional on the rounded count, the output arrangement is uniform regardless of p, including empty and incomplete count cells. Conditional on the joint rounded count and two untouched endpoint bits, that arrangement remains a p-independent channel. Therefore arbitrary full-word decoding composes with a fixed channel to give a randomized decoder from the stated finite message set; the argument is not merely a histogram lower.

The finite-message Bayes lemma works for arbitrary stochastic encoding. Conditioning on an independent decoder seed gives at most D output points, and the union-of-balls argument bounds the probability of small error regardless of which message was drawn. Integrating yields ell/(4D). One need not assume the posterior stays uniform after endpoint observations: both bits are included among the messages. The initial uniform prior is preserved only by the p-independent event label.

Each corruption map is globally defined on all input words and uses at most k changes outside the final pair. It does not read p, beta, a source table or an unobserved future. The IID and marker maps are different witnesses, but each is fixed across its own entire p-family. Their separate lower bounds can legitimately be maximized. The text correctly distinguishes this stronger common-kernel fact from the nested sup_source sup_kernel minimax notation.

## 4. Stationary source, all-state minorization and event law

For a=1/(2M), e=beta0-a, beta0 in [1/M,1/16], positivity and stationarity are immediate by direct substitution. The W-to-active and active-to-W coordinate ratios equal beta0. The W-to-W and active-to-active inequalities reduce to beta0<=1. Unused-symbol rows equal pi, so they too satisfy the symbol minorization; unsupported target columns have zero right-hand side. This proves the pair certificate for EVERY starting pair, including those with unused symbols, through `P²((x,y),(u,v))=T(y,u)T(u,v)`.

The initial law is the stationary pair law pi(u)T(u,v), not pi tensor pi. Its WW mass is p-independent and at least 1/4. Counting the transition exponents in E_j gives exactly `Pi(WW)(1-a)^(M-j)a(1-e)^(j-1)`. On the admissible range j<=floor(1/(4beta0))<=M/4, the Bernoulli inequalities yield event probability at least 3/(64M), hence at least 1/(32M). The conditional active sequence is IID(p), before endpoint conditioning. One prior therefore works across every j.

The target is the actual future row `e delta_W+(1-e)[(1-p)delta_C0+p delta_C1]` at every active terminal pair. The e mass is retained despite the no-return past event. Applying the real-valued error lemma to q(C1)/(1-e), including outputs outside the prior interval, gives the factor 1-e>=1/2. There is no target substitution or external query.

The message-count bound gives conditional loss at least 1/[64(1+(j-2)/(k+1))]. Summing and integrating yields b/(2048M) ln(1+(L-1)/b). Since floor(A)-1>=A/2 for A>=4, and b ln(1+c/b) increases in b, the step to epsilon ln(1+1/(beta0 k))/16384 is valid. The logarithm concavity inequality supplies precisely the factor 1/8. No concentration cutoff is needed.

## 5. IID floors and final constants

All rows of the stationary IID witness are the same, including off-support starting rows. Its two-step pair kernel is exactly the constant stationary pair law, so it is legal at beta=1 and all smaller beta. The common IID erasure map has at most 4(floor(M/(k+1))+1) messages; the claimed epsilon/96 floor follows from M+b<=3M and b>=k.

For identity corruption, the two-point IID family has total sample KL<=1/8, hence TV<=1/4. The conservative testing reduction gives 3/(128sqrt(M+2))>=s/64 for M>=64. This lower is independent of erasure and applies at k=0.

For beta0<=1/16, taking the maximum of epsilon/96 and epsilon log(1+1/(beta0 k))/16384 is at least F/32768. For beta0>1/16 the logarithm is at most ln17<3, so the IID floor alone is at least F/384. Maximizing with the clean floor gives 2^-15 max(s,F), and therefore the capped claim. No addition of incompatible witness risks occurs.

## 6. Independent diagnostics and dependency boundary

`SC002_review_checks.py` was independently written and executed; output is in `SC002_review_checks.json`. It passed:

- 18,432 exact-rational all-pair minorization entries, with an unused fourth symbol;
- 828 exact-rational stationary event lower bounds;
- 450 explicit enumerations of the complete exchangeability-erasure output distribution;
- 517,184 lower scalar comparisons over M=64,...,512 and every k, with beta cutoff cases;
- 960 residual-envelope cases, including all M mod 4 classes, beta=1 and very large horizons;
- 9,937 IID KL and clean-floor comparisons.

Source and erasure tests use exact rational arithmetic. Scalar/log/KL grids use floating point with stated tolerances and are only corroboration, not proofs. The smallest tested integrated-lower/log-lower ratio was about 1.51888; maximum residual/envelope ratio was about 0.18650. No failures or suppressed cases were encountered.

I directly read the complete SC002 proof and inspected AU001 §§2–4, IU001's stationary integration, R011's exact ORIGINAL interface and the acceptance receipts. The ancestor context also contains SC001's full theorem, stationary extension and review, and the complete IU/AU proofs and reviews. The audit inherits the accepted foundational clean-risk and occupation interfaces, not a newly reconstructed transitive proof closure. Bindings are recorded separately. No external prior-art search or publication action was taken; no novelty conclusion follows.
