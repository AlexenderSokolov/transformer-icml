# EP001 fresh independent full boundary review

**Verdict: PASS; no mathematical or scope-blocking defect identified.** This is an independent review of the complete root-authored candidate, not a historical-proof reconstruction. Acceptance remains the root's decision. No candidate bytes were edited.

Reviewed candidate: `EP001_endpoint_corruption.md`, SHA-256 `bf58470664861f28dbd8746d5b0c54eea1beadd98e87c2c80600b1ec68c796fa`.

## 1. Experiment and quantifiers

I read the complete candidate and the accepted R011, SC002, SC003 statements/proofs, with their acceptance receipts. Only the R011 ORIGINAL upper and SC002/SC003 IID floors are imported. This review does not reopen their historical dependencies. Their file hashes match the acceptance receipts (recorded separately).

The new experiment permits edits anywhere in the M+2 observations; k remains in 0,...,M. The true hidden original final pair, not the observed corrupted pair, indexes the target. Randomization and arbitrary computation are allowed; the observations do not include an edit mask or attack seed. Upper bounds hold for every admissible kernel, even if history-adaptive. Lower witnesses use parameter-free common maps on whole words. A fixed witness law can depend on public beta, as usual for a source supremum. Granting the decoder that law makes the endpoint lower stronger, not weaker as a minimax assertion.

Stationary initialization is a subclass of arbitrary initialization with the same admissible estimators/attacks, so the middle inequality is correct. Separate witnesses justify a maximum of lower bounds, not a sum.

## 2. All-state certificate and off-support rows

For u=(a,b), the pair reached after two shifts is (c,d) with probability theta_ab(c) theta_bc(d). Summing d gives theta_ab(c). Consequently P²(u,·)>=beta Pi implies theta_u>=beta pi coordinatewise with pi(c)=sum_d Pi(c,d). All starting pairs u are covered, including zero-Pi pairs. Stationarity also makes the two symbol marginals agree, although the displayed summation itself already identifies the required pi.

For beta<1, r_u=(theta_u-beta pi)/(1-beta) is a probability vector. Thus TV(theta_u,pi)=(1-beta)TV(r_u,pi)<=delta. For beta=1 all rows equal pi by coordinatewise domination plus unit mass. Generated symbols 3,...,N are then IID pi even from an arbitrary initial pair. The claim does not assert that the arbitrary initial pair is itself IID.

## 3. Pooled upper and clean branch

D_t=e_Xt-E[e_Xt|F_(t-1)] has conditional mean zero. For t<r, D_t is F_(r-1)-measurable, so E<D_t,D_r>=0. Conditional squared Euclidean norm is 1-||m_t||². This proves the stated second-moment identity without independence or stationary assumptions. Half-L1 <=sqrt(K)/2 times L2, followed by Jensen, gives sqrt(K)/(2sqrt(M)).

Both the average conditional vector and the actual terminal target lie within delta of pi pathwise. No conditional-independence relationship between terminal target and the martingale is needed: triangle inequality applies pathwise. This supplies 2delta, not delta. Each changed generated symbol changes the empirical probability vector by TV <=1/M; initial-only edits make no contribution. Simultaneous, adjacent, endpoint, and randomized edits obey the same k/M bound. Although initial edits could alter a recomputed transition count, this estimator only pools symbol frequencies and never recomputes hidden source evolution.

For k=0, the ORIGINAL rule in accepted R011 has risk <=8192 H_R011. Its a,D,T are each <=K^(5/2)/sqrt(M): caps and factors delta^r can only reduce them, and sqrt(M+1)>=sqrt(M). Therefore the imported uniform bound is correct even when the right side exceeds one. The clean branch is indispensable to this particular proof because pooled bias does not vanish at fixed beta<1.

For k>=1 the pooled bound is <=(sqrt(K)/2+3) max(s,epsilon,delta), separately capped by one. The proposed C_K=max(8192 K^(5/2),sqrt(K)/2+3) covers both branches. The profile cap is harmless (all three scales are already <=1 on this domain). No parameter or stationary law is required by either branch; k is used only to distinguish zero from positive budget.

## 4. Endpoint uncertainty lower

Set alpha=min(delta/2,1/4). The binary T is stochastic with stationary marginal (1/2,1/2). For extra symbols, setting their starting-symbol rows to binary uniform and all target probabilities outside the binary support to zero makes a well-defined first-order chain on the entire K-letter alphabet. Its second-order extension uses T(y,·) on every (x,y), including off-support pairs. Pi(u,v)=pi(u)T(u,v) is stationary. T(y,u)>=(1-2alpha)pi(u) holds for binary and unused y. Multiplying by T(u,v) gives the exact all-pair-state P² certificate with coefficient >=beta. This does not assume irreducibility on all K² states.

The attack replaces the final symbol by 0 on every word. It is one fixed deterministic parameter-free map and changes at most one symbol (sometimes zero). Given its output and even the full source law, the prefix is fully known but the original final bit has posterior probabilities 1/2±alpha, by the Markov property. No additional data secretly encode that erased bit. Its two possible next-law coordinates at symbol 1 differ by 2alpha. Weighted absolute-loss minimization occurs at a weighted median and equals (1/2-alpha)2alpha. Randomized estimates are convex combinations of deterministic risks and cannot improve the minimum. Extra-alphabet mass cannot help since TV dominates the absolute error of the coordinate {1}.

For delta<=1/2 the loss is delta(1-delta)/2>=delta/4; for delta>=1/2 it is 1/8>=delta/8. Hence delta/8 uniformly, including delta=0. This is uncertainty about a latent terminal symbol in a *known* chain, not uncertainty about estimating T. Replacing the target by the corrupted endpoint's row would destroy this argument; the candidate does not do that.

The sentence concerning a revealed replacement indicator correctly refers only to this particular attack: its indicator would identify whether the original last bit was 1. It is not a theorem that every visible-mask corruption model has zero endpoint obstruction. No such broader claim is imported or needed.

## 5. IID floors and constants

The IID binary family defines every second-order row identically, including unused-symbol contexts, so P²=1 Pi holds on every pair. Thus it lies in every beta class, K>=2. Identity attack remains admissible at positive k. The accepted parameters 1/2±1/(16sqrt(N)) give product KL<=1/8, product TV<=1/4, separation 1/(8sqrt(N)), and testing risk >=3/(128sqrt(N))>=s/64 for M>=64. The last inequality is equivalent to 9M>=4(M+2), well within the stated domain.

For count erasure, b=k+1 and n-r<=k. Conditional output arrangement is uniform among weight-r words because binom(M-r,n-r)/(binom(M,n)binom(n,r))=1/binom(M,r). The two untouched IID bits must be retained in the finite message, yielding D=4(floor(M/b)+1), exactly as stated. Extra random arrangement is a parameter-independent channel, not extra parameter information. The interval-length-1/2 finite-message absolute-loss bound is 1/(8D). Consequently risk >=1/[32(floor(M/b)+1)]>=b/[32(M+b)]>=k/(96M), since b<=M+1<=2M. The rule is extended to nonbinary words by the accepted interface's identity convention, so it remains a valid common map over the full K-letter domain.

Combining s/64, epsilon/96, and delta/8 gives max(s,epsilon,delta)/96 for k>=1. For k=0, s/64 is stronger than the requested s/96. Thus all constants and boundary cases beta=0,1; k=0,1,M; M=64; K=2 and off-support K>2 are covered.

## 6. Fresh executable diagnostics

Run: `python v10_research/terminal_symbol_corruption/EP001_boundary_review_checks.py`.

Result: PASS. The script pins the candidate hash before testing and records:

- 36 random positive rational second-order chains at K=2,3,4; exact stationary laws, maximal certificate coefficients, marginal identities and row-TV bounds.
- 18 exact binary-core/off-support certificates at K=2,3,5 and six delta values including 0,1/2,1.
- 888 exact stationary erased-prefix posterior/Bayes-loss calculations, word lengths 3,5,8.
- 9 exact path enumerations establishing martingale mean zero, cross orthogonality, variance identity and pooled triangle inequality for stationary, point-mass, and uniform initial laws.
- 21,824 exhaustive clean/corrupted binary-word comparisons checking pooled empirical perturbation, including endpoint and initial edits.
- 2,108 exact combinatorial count-erasure identities and edit budgets.
- 11,484 finite-domain constant cases across M=64,65,100,127,128,1000,10000, with all positive k, plus clean-floor KL checks.

The tests use exact rationals except explicitly numeric square-root/log constant spot checks. Small-horizon tests are algebraic diagnostics, not substitutes for the analytic all-M proof. They do not claim formal verification, novelty, neural implementation, online/offline equivalence, or a visible-mask frontier. No external actions or user sends occurred.
