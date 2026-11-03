# CB004 + BP001 — Fresh independent full two-component review

2026-11-02. Reviewer: independent LLM reviewer, separate from both candidate authors.

## Result first

**Recommendation: PASS for the exact two-component STATIONARY theorem below. No blocking mathematical, observation-interface, quantifier, or constant defect found. Root acceptance remains a separate action.**

Reviewed candidates, both read completely:

- `critical_beta_adaptation/CB004_stationary_critical_adaptation.md`: `a322c2fe08b76cf84f587b91e4ab504e2e02468e8c1a617fd7b868e14f643155`.
- `critical_beta_adaptation/balance_probe/BP001_stationary_weighted_balance.md`: `22b60eedf31f1e990e990a8b64ad733a1a3acc9723a421fdc6d677866c771271`.

The supported claim is that the **same** deterministic full-corrupted-history map, with active gate `J'>0 and 512 J1'>=J'`, uses neither budget k nor certificate beta and satisfies

    R_stat <= min{1, 2^16/sqrt(M) + 4096/(M sqrt(beta)) + 2^23 k/M}

for integer M>=64, integer 0<=k<=M, and every positive qualifying all-state certificate beta. It therefore attains the known-k stationary minimax order simultaneously over budgets on every band beta>=c/M, with constants allowed to depend on fixed c>0.

**Arbitrary-initialization adaptation is NOT established.** The path reversal and stationary endpoint mass multiplier are indispensable to the current proof. This review is an independent LLM mathematical audit with finite exact diagnostics, not formal verification, external peer review, a novelty assessment, publication, or acceptance. No candidate or accepted source file was edited.

## 1. Imported statements and their exact domains

I read complete accepted BU001 v2, its complete v1 full review and v2 delta review, review bindings, and acceptance receipt. The accepted proof hash is `2dc9cf9d13faa6cfa15fffd5ec83a67326ccc95eb6a63291c7b2349136b166f5`. The import used here is its **target-specific hitting bound**, not its precision decoder or a mixing theorem. I additionally read IU001 sections 1–2, including its complete supported-reversal/Kac proof, to verify the return-time domain.

I read complete SC003 and its full review/receipt. Its accepted hash is `4235fc6b9de9d04368354d22f15774d66965ca572f21f197e456537e9bcba837`. The required interfaces are its binary source/attack experiment, fixed designated orientations, clean empirical comparator, universal terminal-occupation inequality, and positive-certificate support classification. These imports hold for arbitrary initial laws; only the new BP001 ingredient requires stationarity.

I read complete BT002 main and scalar proofs, full independent review, and receipt. Their accepted hashes are respectively `40d5345657b8f255cd1cef496fb84090aae18a6cd6bc7c083daa09c2ce913562` and `4be9d338e0d3e6b840441f4356e77b71db4da9f1208d74bd85f4790539ba9026`. Its stationary full-history lower uses the same protected-terminal, hidden-seed/mask experiment and applies even when k is supplied. No new audit of every older imported theorem is represented here. The new reasoning in BOTH current components was independently reconstructed in full.

For any existing qualifying source, summing a certificate row gives beta<=1. Thus the statement's beta>0 is not a hidden permission to apply estimates at beta>1; such source classes are empty. Finite positive-beta supported chains are closed and irreducible, because P^2(i,j)>=beta Pi(j)>0 on positive support. In the nontrivial binary case the support is full. In the remaining case it is one absorbing diagonal.

## 2. Return-time moments, Kac, and both mgf estimates

BP001's generic lemma concerns a finite irreducible chain and a target of mass p>0. All hitting/return expectations are finite. Finiteness of higher moments can also be justified before induction: from every state a positive-probability bounded-length path hits the target, and taking the minimum of these finitely many probabilities gives geometric domination in blocks. Periodicity causes no problem.

Let D be the ordinary first hit (D=0 when started at the target), T the positive return, and Hbar=max(H,1/p). Kac gives E T=1/p. From a target start the first transition followed by an ordinary hit gives 1/p<=1+H. These statements are used only on irreducible positive support. No Kac identity is asserted at a transient or zero-mass target.

For a positive-return law, on survival at time j>0 the state is not the target, so the residual law is an ordinary hitting law. At j=0 the original positive-return law remains in the family. The zero ordinary hitting law contributes zero moments. For r>=2, conditional induction bounds the residual (r-1)-st moment by (r-1)! Hbar^(r-1), using the uniform residual mean bound. The deterministic power-sum inequality and sum_j P(V>j)=E V then prove

    E V^r <= r! Hbar^(r-1) E V.

Thus the proof's stronger factor E V, rather than just a uniform Hbar^r bound, is justified. Nonnegative series justify exchanging expectation and the positive exponential expansion. At lambda=1/(4Hbar),

    E exp(lambda D) <= 1 + lambda E D/(1-lambda Hbar) <=4/3,
    E exp(lambda T) <= 1 + 4lambda/(3p) <= exp(2lambda/p).

The elementary quadratic upper for exp(-x), together with the r=2 moment, gives

    E exp(-lambda T) <=1-lambda/p+lambda^2 Hbar/p
                         =1-3lambda/(4p) <= exp(-3lambda/(4p)).

Here lambda/p<=1/4, so no spurious negative polynomial upper is used. IID positive returns are constructed after the first hit by strong Markov. D and the return sequence may consequently be combined in the first positive mgf bound; there is no IID assertion about selected row samples or about returns after conditioning on a count event.

## 3. Exact visit indices and deterministic windows

For L_l counting times 0,...,l-1, put K=ceil(lp/16). The integer event L_l<lp/16 is exactly L_l<K. It means that the K-th visit time D+T_1+...+T_(K-1) is at least l, including the equality endpoint. Since K-1<lp/16, the mgf exponent is at most -7lambda l/8. Its bound (4/3)exp[-7l/(32Hbar)] is no larger than 2exp[-l/(8Hbar)]. If lp<16, K=1 and no return variables are needed.

For the upper tail, K=floor(4lp)+1>4lp. The event L_l>4lp+1 entails at least K+1 visits, whether 4lp is integral or not. Therefore the sum of the first K positive returns is <=l-1-D<=l. The negative mgf gives exponent lambda l-3lambda K/(4p)<=-2lambda l. Thus both inequalities in BP001 (2.4) hold uniformly over starting states. Conditioning on the random state at the beginning of any deterministic shifted window preserves them. No independence between the two windows is needed for their union bound.

## 4. Weighted hitting scale, reversal, and stationary imbalance

The required weight is **gamma=(a,1,1,tau)**. The designated true probabilities q=(a,b,e,tau) are not generally invariant under the pair-coordinate swap. BP001 makes the distinction correctly and only uses q<=gamma at the end.

For full support, BU001's H_s is the maximum over all four states, exactly as needed. Its target hitting bound is sqrt(beta) Pi(s) gamma_s H_s<=5. For example, stationarity ya=xe and w tau=xb converts the 00 expression after multiplication by sqrt(beta)ya into terms controlled by e^2>=beta y and b^2>=beta w. These are consequences of the actual all-state certificate, not a substitute sufficient certificate. The crossing-target bound already uses weight 1. With 1/p<=1+H, p gamma<=1 and beta<=1,

    p gamma Hbar <=p gamma(H+1)<=6/sqrt(beta)<=10/sqrt(beta).

This is a target return/hitting scale. It does not imply a global sqrt(beta) spectral gap or mixing rate.

The stationary triple flux identities ya=xe and xb=w tau, together with the palindromic triples, give equality of each triple's probability and its reversed triple. Consequently conditional on endpoint s, Z_j=swap(Y_(M-j)) is an ordinary forward P-chain started at swap(s). Its target v=swap(s) has Pi(v)=Pi(s) and gamma_v=gamma_s. The operation is neither ordinary detailed balance of the unflipped pair chain nor a replacement of the observed terminal target.

The exact index maps are correct:

- Original first half j=0,...,n-1 becomes reverse indices m+1,...,M (length n).
- Original second half j=n,...,M-1 becomes reverse indices 1,...,m (length m).

In particular reverse index 0 is NOT counted, and reverse index M IS counted. These are the shifted windows actually covered by the uniform-start lemma.

If np>=1, the two good-count events imply J2<=4mp+1<=9np because m<=2n. Together with J1>=np/16, they give J1/(J1+J2)>=1/145>1/256. Thus every strict imbalance with c<=1/256 is covered by the stated two tails. Multiplying their union bound by p gamma and setting z=n/(8Hbar) gives

    p gamma P(imbalance | endpoint s)
       <=30 exp(-z)/(sqrt(beta)Hbar)
       <=240/(n sqrt(beta)).

If np<1, the bound follows directly from p gamma<=p<1/n and beta<=1. Summing at most four states and n>=M/3 gives 2880/(M sqrt(beta))<4096/(M sqrt(beta)). The strict event is empty at J=0, so there is no missing zero-count contribution inside BP001. The independent unit bound supplies the cap.

For singleton stationary support, the entire stationary path remains on its absorbing diagonal and gamma=q=0 there. The contribution is exactly zero; no division by a zero weight or unsupported stationary mass is made. This does not analyze arbitrary transient initial states.

## 5. Generic balanced inverse occupation

For each fixed target u, condition on the deterministic-time prefix through Y_n=v, and let its u-count be j. The suffix is an ordinary m-step chain from v. The original total balance event implies J2_u<=1023j. Its conjunction with endpoint u is contained in the universal actual-terminal event with integer threshold w=1023j+1, hence has probability <=16(1023j+1)/(m+1).

On that event 1/(J_u+1)<=1/(j+1). The exact bound (1023j+1)/(j+1)<=1023 includes j=0. Averaging prefixes, summing four possible endpoints, and using m+1>=M/2 gives 130944/M. There is no division by P(Y_M=u), and no conditional IID inference. For M>=128 the suffix horizon is >=64 and lies in the stated SC003 interface domain. Smaller M is not smuggled through this argument; the final capped result is trivial for 64<=M<128.

## 6. Hamming perturbation, gate switches, and pathwise loss

A first-M symbol replacement changes at most three selected departure triples; histogram l1 change is at most twice that. The full count, selected success count, and first-half count each therefore change by at most d=6k. Edits straddling the split and simultaneous adjacent edits do not increase this union bound. The protected final pair ensures that clean and corrupted counts select the same row.

On active G' and true H with J>0, if J>=2d then J'>=J/2 and the two empirical probabilities differ by at most 4d/J<=8d/(J+1). If 0<J<2d the unit probability difference is covered by the same bound. At d=0 the empirical fractions coincide. J=0 is deliberately excluded from this normalization and paid by tails later.

The active-but-unbalanced inequalities imply

    J/1024+d > (J-d)/512, hence J<1026d=6156k.

For false rejection outside B and J>0, either J'=0 and J<=d, or

    J/256-d < (J+d)/512, hence J<513d=3078k.

Strict versus weak inequalities and equality at each gate threshold are correct. At k=0 neither false-status case with J>0 can occur. If the gate rejects on B, output zero has exactly loss q. The remaining J=0 and switch cases are covered by the two integer tail thresholds 6156k+1 and 3078k+1. Overlap only enlarges the bound. These cases prove CB004 (3.5) pointwise before taking clean-path/attack expectations, so randomized history-adaptive corruption is fully covered. Binary TV is the designated-coordinate absolute error.

## 7. Assembly and constants

SC003's clean empirical comparator is for the actual terminal row and has coefficient 8193 sqrt(32). It follows by comparing empirical C/J on J>0 to original clean add-one, not by pretending terminal-selected successor samples are IID. Its universal occupation interface with the exact positive integer tail thresholds contributes

    16[(6156+3078)k+2]/(M+1).

The inverse term contributes 48*130944 k/M. Replacing M+1 by M only enlarges the budget term, and the total coefficient is exactly 6433056<2^23. For M>=64,

    8193 sqrt(32)/sqrt(M+1)+32/(M+1)
       <=[8193*6+4]/sqrt(M)<2^16/sqrt(M).

Adding BP001's coefficient proves the claimed expression for M>=128; for 64<=M<128 its unit-capped RHS is 1. Since 2^16+4096<2^17, the critical beta=1/M corollary is valid. The independent unit-loss cap can be taken after assembly.

## 8. Observation ports, same-map quantifiers, and benchmark comparison

The algorithm needs only public M, the full corrupted eight-coordinate triple histogram, four corrupted first-half row counts, and the protected terminal pair. These can be collected during one scan before selecting the terminal row. Rational output is total: use C'/J' only when J'>0 and the gate holds, otherwise output the fixed designated zero. The analysis-only clean counts, q, gamma, beta, k, Pi, initial law, mask, and attack seed are not predictor inputs. First-half counts contain order information not recoverable from the total histogram alone; no stronger arbitrary-order necessity claim follows.

For a fixed M there is one map A_M, unchanged across every budget and every certificate. The derived guarantee holds for every admissible source and every permitted attack at each k; it does not choose a new k-aware comparator as the actual estimator. A source can satisfy multiple advertised certificates without requiring a different map. The pathwise corruption proof would even tolerate more adversary knowledge than allowed, so source independence is not an omitted upper-bound assumption.

On beta>=c/M, 1/(M sqrt(beta))<=c^(-1/2) M^(-1/2). Thus the risk is bounded by a c-dependent constant times max{M^(-1/2),k/M}, capped by 1. Since H_2 is at least that capped lower envelope, this gives an upper of constant times H_2. Conversely BT002's lower applies to each fixed k even for k-aware estimators; a k-blind map cannot evade it. SC003 and BT002 already bind the known-k benchmark to H_2 in the same observation experiment.

For clarity, the claimed critical-profile equivalence has an elementary direct check: ln(1+x)<=x gives F_2<=k/M+1/(M sqrt(beta)) whenever beta>=M^-2. At beta=1/M this is <=k/M+M^-1/2. No growing logarithm is discarded below the critical band. These conclusions concern stationary initialization only; the all-start bias E[q 1_B] remains unproved in the current manuscripts.

## 9. Fresh exact diagnostics and evidence limits

I wrote and ran `CB004_BP001_independent_checks.py` without importing either author's diagnostic implementation or a prior reviewer script. Its output is `CB004_BP001_independent_checks.json`. The run passed **752,062 checks**:

- 625 rational binary kernels examined; 209 have positive genuine all-state certificates, consisting of 81 full-support and 128 singleton cases.
- Exact stationary pair-flip flux identities, invariant unit-crossing weights, Kac identities, supported hitting bounds, and ordinary/positive-return moment inequalities through order 6.
- 1,024 finite lower/upper visit-tail checks through horizon 128, across every target/start of four finite irreducible kernels, including non-binary and periodic examples. Exponential comparisons use exact rational Taylor upper enclosures, not floating-point tolerances.
- 65,472 exact shifted-window identities over all binary words through M=10.
- 87,376 exhaustive clean-word/edit-mask pairs through M=7, including adjacent edits, terminal protection, perturbations, gate cases, and three rational target probabilities for the complete reduction.
- 18,000 larger synthetic count perturbations around the 256/512/1024 and 3078k/6156k thresholds, including k=0 and counts near 10^9.
- Exact integer ceiling/floor, inverse-occupation ratio, constant, accepted-receipt, and candidate-hash checks.

The finite rational grid's maximum beta*(p gamma H)^2 and beta*(p gamma Hbar)^2 are both 1, below the proved bounds 25 and 36. This is not evidence that the universal constants can be replaced by the observed maxima. The small-horizon tests validate local identities and reductions, not a new theorem below M=64; the large displayed final-risk constants are frequently vacuous at diagnostic horizons. The universal conclusion rests on sections 1–8, not on the number of passing checks.

## Final disposition

Recommend root acceptance of **both exact hashes together**, as a stationary full-history, unknown-k and unknown-beta adaptive estimator theorem. BP001 alone is only the stationary weighted-bias ingredient; CB004 requires BP001. Retain the explicit arbitrary-start gap and all observation restrictions. Neither manuscript nor prior accepted result was changed, and acceptance remained a separate decision.
