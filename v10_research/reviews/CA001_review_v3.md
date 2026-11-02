# Independent hostile audit: CA001 v3

**Verdict: PASS for the stated ideal-real, final-grid-cut family, including the declared dense-public-mask and finite-local/boundary variants.** No mathematical blocker found. The two explicit constants `c1=1/(8192 A_s)` and `c2=1/(256 A_I)` are valid. This is not acceptance of an actual emitted network, all-operations finite arithmetic, arbitrary causal Transformers, an exact h-bit word interpretation, or novelty. No candidate/source file was edited.

Frozen target: `v10_research/causal_attention/CA001_causal_bounded_softmax_candidate_v3.md`, SHA256 `88e952f840009d8345c4482ca8cd14231f9dd9a28a3d522f12cd7e03b65ea21e`. Directly read its adjacent v3 bindings, BA001 v1, and the local corrected-Hahn comparison. External papers were not independently re-retrieved or recertified in this audit.

## 1. Primitive perturbation: passes, including changing attention weights

For endpoint logits in `[-B,B]^t`, the connecting logit segment remains in that box. Every interpolated weight is at most `exp(2B)/t`. The exact softmax differential gives

`sum_i |d alpha_i| <= 2 sum_i alpha_i |d s_i|`.

Integration supplies the manuscript's L1 difference bound without interpolating hidden states. Split the pooled-output difference into endpoint-weighted value differences and endpoint values times weight differences. Their bounds are respectively `C V_L sum delta_i/t` and `2VC S(delta_t+sum delta_i/t)`. This verifies the full query/key/value expression and, under the stipulated sum-norm Lipschitz map, `delta' <= (aI+bA)delta` with exactly the displayed nonnegative `a,b`. The query contribution is not lost; no assumption of fixed weights was smuggled in. Component hypotheses must hold uniformly across the compared formal histories, not just observed training examples.

## 2. Matrix powers, row/square sums, and the real early-token obstruction

Multiplying causal averaging matrices yields the displayed weakly ordered intermediate-index sum. Dropping order only adds nonnegative terms, and `sum_{u=i}^t 1/u <= 1+log(t/i)`. Since `I` commutes with `A`, binomial expansion gives the off-diagonal envelope with `K_L=(a+b)^L-a^L`. The diagonal `a^L I` term is zero at `(T,i)` for `i<T`. The synthetic initial state is fixed, so it contributes no replacement error.

The v3 definition `d_i=G Delta (Bmat^L)_{Ti}` is crucial and correct. `Bmat 1=(a+b)1` gives `sum_{i<T}d_i<=G Delta(a+b)^L`; this is **not** a claim that the larger logarithmic envelopes have that row sum. For `m=2L-2`, substitution `y=log(1/x)` gives

`I_m = integral_0^infty (1+y)^m exp(-y)dy = sum_k binom(m,k) k!`.

The decreasing integrand dominates its right-endpoint Riemann sum. Squaring the entry envelope therefore gives `sum d_i^2 <= (G Delta K_L)^2 I_m/T <= Lambda/M`. The first history coin can be much larger than `1/M` without invalidating this square sum. Late positions satisfy `w_i<=1+log 2`; the earliest coin of a length-j suffix is `M+3-j`, which exceeds `(M+3)/2=T/2` whenever `j<=M/4`. Thus the late suffix constant `Gamma/M` is valid. Zero `K_L`, `G`, or `Delta` causes no division-by-zero obligation: the curves are constant and use one mesh point.

**The stronger uniform `O(1/T)` statement is false.** Take scalar inputs in `[0,1]`, zero logits, one head, identity values on that bounded reachable range, and `F(h,o)=o` for two layers. With initial terminal token zero, flipping source position 1 changes the real terminal output by exactly `H_T/T`. All activations remain in `[0,1]`; this is an admissible actual ideal network, not merely a worst-case matrix majorant. Consequently `T` times the change diverges. This counterexample must be retained.

## 3. Nonlinear whole-network expectation and complete-message tubes

The replacement inequalities hold for each full nonlinear final coordinate. Efron–Stein gives the manuscript's conservative `Var <= sum d_i^2/2` under product coins. Differentiating the finite Bernoulli polynomial gives the sum of one-coordinate conditional differences, bounded by `sum d_i`. There is no need for, and no use of, an expectation-of-ratio identity. These facts prove both the suffix bounds (`Gamma j/M`, `Gamma²j/(2M²)`) and the fully IID bounds (`C0`, `Lambda/(2M)`) despite arbitrary public positional dependence.

For each fixed branch, the curve is deterministic. With `U=max(Gamma,sqrt(Lambda))`, each coordinate/branch failure probability at the chosen threshold is at most `1/(10 D H_b)`; union gives total failure at most `1/10`. If `U=0`, the claim follows from deterministic zero variance instead of Chebyshev division. This is pointwise in p, which suffices after integration against the prior.

On the suffix regime, scaled fluctuation is at most `tau/2`; mesh error is at most 1, and downward rounding adds less than 1. The manuscript's radius `tau+2` is conservative. On the IID regime `Q<=sqrt(M)`, scaled fluctuation is at most `tau`, so the same radius works. An interval of length `2tau+4` contains at most `floor(2tau+4)+1 <= Nbox` integers, regardless of sign or translation. Parameter meshes have at most `2+Gamma Qj/(2M)` and `2+C0 Q/2` points, respectively, bounded by the stated expressions. Union over frozen side values counts their labels as well as their banks. Thus `A_s(1+Qj/M)` and `A_I Q` bound the **complete** good-message alphabets, not just one coordinate.

Unbounded fixed output offsets do not break this proof: an arbitrary translate of each finite tube contains the same bounded number of grid labels. Conversely an infinite grid is not an h-bit memory. Under the optional absolute output bound the manuscript's `floor(2R_out Q)+2` per-coordinate count and `h+O(1)` statement are correct. Public metadata are fixed in each experiment. Source-independent shared encoder/decoder seeds can be conditioned upon; all constants and success bounds must remain uniform seedwise, and the same prior is then averaged over seeds. Random seeds are not themselves counted as a finite message without that conditioning argument.

## 4. Stationary source and every numerical lower-bound constant

The three-symbol transition law satisfies stationarity by direct substitution. For active columns the rowwise minorization reduces to `1-eta>=alpha`; for W it reduces to `1-alpha>=eta`; unused-symbol rows equal pi. Thus `Tsrc>=beta0 pi`, including unsupported starting states, and the second-order pair-chain identity gives the declared all-state `P²>=beta Pi`. Since `beta0>=2alpha`, `pi(W)>=1/2` and `Pi(W,W)>=1/4`. The stationary law is the actual initialization, not an oracle supplied to the decoder.

For `Q<=M/4`, the two quantities defining the unfloored cutoff are at least 4, so `J>=4`, `J>=U/2`, and `J<=M/4`. The event formula has exactly `M-j` remaining W-to-W transitions after the stationary starting pair. Its probability is independent of p. An explicit conservative check is `(1-alpha)^M>=1-Malpha=1/2` and `(1-eta)^(j-1)>=1-eta(j-1)>=3/4`; together with `Pi(W,W)>=1/4` and `alpha=1/(2M)`, this even gives `e_j>=3/(64M)>1/(32M)`.

Conditional on that event, the suffix symbols are independent Bernoulli(p), and the single uniform p prior remains uniform for every j. The events are disjoint. The next-step target at the actual active terminal symbol retains its exit probability eta; the manuscript correctly uses `eta delta_W+(1-eta) Bernoulli(p)`, not the active-conditional target.

For the finite-message lemma, radius `ell/(8R)` around at most R decoder values covers at most `ell/4` of the parameter interval. Joint good-and-outside probability is at least `0.9-0.25=0.65`; its error contribution is `0.65 ell/(8R)>ell/(16R)`. Independent decoder randomness can be fixed and averaged. With `ell=1/2` and `1-eta>=1/2`, conditional TV loss is at least `1/[64 A_s(1+Qj/M)]`. Multiplying `e_j>=1/(32M)` gives exactly `1/(2048 A_s M)` times the harmonic sum.

For `u=Q/M<=1/4`, shift j by 2, use `1+u(k+2)<=(1+2u)(1+uk)` and `1/(1+2u)>=1/2`, integrate the decreasing summand over `[0,J-1]`, and use `J-1>=J/2` plus `log(1+x/2)>=log(1+x)/2`. This proves the stated `sum >= log(1+uJ)/(4u)`. The floor bound gives `uJ >= min{Q/(M beta0),M/Q}/8`. Hence the advertised c1 is valid.

For the large-Q completion, Bernoulli alternatives at `1/2 +/- 1/(16sqrt(M+2))` have KL at most `1/8` by the elementary Bernoulli KL upper bound and Pinsker TV at most `1/4`. Threshold testing then gives average loss at least `3/(128sqrt(M+2))`, stronger than the recorded `1/(128sqrt(M+2))`. The logarithmic target for `Q>M/4` is at most `2c1/M`, dominated by that weaker recorded floor. For the IID tube, the lemma gives `1/(32 A_I Q)` for `Q<=sqrt(M)`; for larger Q, `sqrt(M+2)<=sqrt(2M)<2Q` yields `1/(128sqrt(M+2))>=1/(256Q)`. Since `A_I>=1`, c2 works. These are bounds on the same minimax risk, combined by maximum, not addition. The construction's alphabet must permit the three-symbol witness for the logarithmic theorem, as in the expressly imported BA001 statistical model.

## 5. Optional local preprocessing, formal branches, and masks

A coin changes at most r window states. For their nonnegative matrix bounds b_u, set `e_i=G Delta sum_{u=i}^{min(N,i+r-1)}b_u`. Summing multiplicities gives the factor r row bound. Cauchy–Schwarz gives `e_i²<=(G Delta)² r sum_{u in window(i)}b_u²`; summing, with each u present at most r times, gives the factor r² square bound. Late affected windows stay late. The proposed replacements of C0, Gamma, and sqrt(Lambda) therefore suffice without interpolating arbitrary local tables.

Frozen-branch concentration would be invalid on consistent histories alone. V3 explicitly requires the bounds and local contract on **all formal histories with the branch fixed**, including inconsistent boundary values. This closes that loophole. Simultaneous concentration for all at most `3^b` branches can then be followed by selecting the actual side value; no conditional-IID claim is needed. The initial synthetic state may depend on s but not on the sampled formal history once s is frozen. Any exact function of s adds no more labels. Arbitrary exact interior statistics remain excluded.

For masks, logit interpolation uses the same public subset in both endpoints and weights are at most `exp(2B)/(ct)`. Expanding the key sum to all preceding indices and bounding `|K_t|<=t` proves the conservative query term with the same `1/c` inflation. The identical nonnegative recurrence and all descendants follow. The declared fallback masks have density at least `1/3` (worst row t=3); the terminal mask has size `T-3>=T/3`. A positionwise-only fallback is bounded by enlarging a. Singleton global copy heads, source-dependent masks, and arbitrary interleaved exact copies do not acquire coverage through this argument.

## 6. Boundaries, evidence, and disposition

Section 6 is a valid **conditional** perturbation transfer: an independently proved uniform `E/Q` pre-cut error merely widens the mesh tubes by E. It does not establish that condition. Failure-probability variants require an explicit remaining success budget and, if necessary, revised constants. No stability of intermediate rounding follows from the real Lipschitz proof; no FA001 or actual-SRC membership is granted here.

The BA001 comparison is appropriately qualified: finite arbitrary local tables versus recursive bounded-Lipschitz causal features are different families, and neither bare definition is asserted to contain the other. The local literature record correctly flags the weight-change correction as load-bearing; this audit verifies CA001's independent formula, not external priority. A minor metadata issue only: v3 bindings still describe the preserved v2 entry as “Current author candidate”; the v3 target and hash are nevertheless unambiguous. A standalone presentation could restate BA001's alphabet/statistical minimax definition rather than importing it, without changing the proof.

Independent executable evidence: `CA001_independent_checks_v3.py` and its JSON report. **9,023 checks passed, zero violations**, covering triangular powers, actual row/square sums, local multiplicities, random full/dense-mask perturbations, stationary/minorization identities, suffix/harmonic constants, IID completion, and the real zero-logit counterexample. These finite checks are supplementary; the analytic arguments above establish the arbitrary-size claims. No source edits, external communication, arithmetic implementation, or novelty claim occurred.
