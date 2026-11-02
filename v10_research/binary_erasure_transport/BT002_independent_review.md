# BT002 independent full review — PASS

2026-11-02,09:09 UTC. Reviewer: independent child `independent LLM reviewer`. This is an independent mathematical LLM review, not formal verification, publication review, root acceptance, or external novelty certification. No author or frozen file changed by this reviewer.

## Verdict and exact scope

**PASS:** the binary full-history stationary corruption lower

    R_stat >=2^-54 max{M^-1/2, F},
    F=(k/M)[1+ln(1+1/(e k))], e=max(sqrt(beta),1/M).

for M>=64, integer0<=k<=M, beta∈[0,1], with corruption term defined0 at k=0, is supported by the supplied proof. The logarithmic witness uses one source-independent offline strict-Hamming-budget kernel and one common uniform parameter prior across all suffix lengths. The attack seed is hidden and the exact final pair is preserved. Computation is unrestricted. IID floors are separate admissible minimax witnesses.

This does **not** prove BT001's interior neighboring-count O(1) transport conjecture, an efficient sampler, causal corruption, public attack seeds, visible edit masks, or edited-terminal-pair variants. Combination with SC003's upper is a separate dependency-binding/acceptance step.

Reviewed snapshots:
- `BT002_entropy_bridge_lower.md`: SHA256 `40d5345657b8f255cd1cef496fb84090aae18a6cd6bc7c083daa09c2ce913562`.
- `BT002_scalar_completion.md`: SHA256 `4be9d338e0d3e6b840441f4356e77b71db4da9f1208d74bd85f4790539ba9026`.

## Full mathematical checks

1. **Uniform coupling and concentration.** Independently computed the R_p^5 A-column `(2p(1-p),(1-p)^2,p)`. For p∈[1/8,7/8], a shared atom1/64 at five-step boundaries gives expected emitted-bit disagreements<=320 from any initial states. Conditional block bridges preserve the chain marginals, including when the remaining horizon is truncated. Revealing one transition yields Doob conditional range<=321; L=326 is safe. Conditional Hoeffding gives the stated `t L² lambda²/8` mgf bound for every Hamming-Lipschitz f, including a McShane extension if f is initially defined only on support.

2. **Entropy-to-transport.** The finite entropy variational inequality and optimization give `L sqrt(t KL/2)`. Finite metric transport LP duality applies on the finite bit cube; zero-probability words are harmless. No stationarity, IID path, or unjustified conditional concentration is being assumed. The bridge measure has the appropriate KL direction toward its unconditioned canonical law; symmetry is invoked only for Wasserstein distance.

3. **Parameter interpolation.** A hybrid sequence with p-prefix and q-suffix changes one transition at a time. At the changed step disagreement probability<=|p-q|; the common-q tail costs<=320. Thus `(3)` follows. This argument remains valid despite the reference chain's non-IID cycle lengths.

4. **Exact microcanonical event.** Prefix-free cycles01 and101 give a bijection between count-(s,l) returns and cycle permutations. Their total probability is exactly `binom(s+l,l) p^l(1-p)^s`; at p_hat=l/(s+l), l is a binomial mode. The lower bound1/(m+1) and KL<=ln(t+1) follow. The final two bits of every returned path are01. Canonical A-bridges share this endpoint. The metric triangle bound `(5)` is valid even though its intermediate measures need not have endpoint A.

5. **Constants and finite coupling.** Rational count laws and rational grid bridges admit a rational optimal finite transport vertex. The grid spacing and size bounds are correct. Numerically and algebraically,
   `1024 sqrt(2·2^-44)+326/2^20 <1/1024`.
   The cutoff ensures `ln(t+1)<=2ln(k+2)`. Truncation is based on the ORIGINAL-to-final Hamming distance, so it enforces a strict k budget. The marker/initial1 are preserved and the protected final pair is unchanged. Requiring at least two prefix zeros makes the all-word recognizer unambiguous relative to starting pair A; its behavior elsewhere is identity.

6. **Good-event mass.** At true p∈[1/4,3/4], endpoint A has probability>=1/16. On a return at t the number m of complete cycles lies between ceil(t/3) and floor(t/2). A union over these deterministic indices of IID cycle-choice deviations, each bounded by2exp(-m/32), proves the tail bound. This is not conditioning a binomial experiment on its stopping time. At t>=4096, `2t exp(-t/96)<=1/128`; eligibility mass>=1/32 is conservative. Removing truncation failure<=1/1024 leaves success>=1/64.

7. **Common kernel and finite-message small-ball step.** The output bridge law depends only on public t,k and the q label, not original counts within the label or true p. The original-to-output coupling depends only on visible counts, never p. Reverse disintegration makes an auxiliary arrangement seed independent of p: first generate counts, then the common q-bridge output using that seed, then the original word by the selected coupling's conditional law. The bad label can use a fixed public word; the bad branch is excluded from success. Once this seed and decoder randomness are fixed, only D_t candidate predictions remain, regardless of the stochastic p-dependent label selection. The near-p union has prior mass<=1/128. Subtracting this from success probability and only THEN multiplying by rho is valid; subtracting constant TV error directly from vanishing risk would not have been. Constants `(9)` follow.

8. **Actual stationary source and harmonic sum.** Independently rechecked BT001's modified source stationarity and all-state certificate using `x<=a/e`, `beta<=e²`, `e<=1/16`. Its path density factor relative to the deterministic-C reference is `Pi_W(1-a)^(M-j)a(1-e)^(N_B+N_C)`. The supplied bound>=1/(32M) is valid for j<=1/(4e). With author t cutoff1/(8e), j=t+1 meets this bound and lies<=M/4. Same source parameter, stationary initialization, prior, and kernel are used for every disjoint suffix event. Pointwise domination, not a false uniform conditional prior, justifies summation. On retained events the actual target at A is exactly p.

9. **IID floors.** Product Bernoulli KL<=5/64 and Pinsker imply the clean2-point floor with ample slack. The SC001 erasure applied to first M IID bits, with protected last two bits counted as four labels, yields `1/[32(1+M/(k+1))]>=k/(64M)`. Every IID source used satisfies every beta certificate. Taking maximum of separate minimax witnesses is legitimate.

10. **Finite-domain scalar completion.** Independently checked both branches k<=M^(1/4) and k>M^(1/4), the `log(k+2)<=2sqrt(k)` inequality, and the two minimum branches. The truncated-sum integral handles floor endpoints and empty sums correctly. The initial draft used denominator4 whereas the probability proof used8; this was reported and is resolved by generalizing the scalar statement to C and specializing C=8. The exact specialization constant is approximately1828.465519<1830<2048. Combining sum coefficient2^-43 with the IID floors therefore yields2^-54. For beta>1/256, `F<=epsilon+2s` and the floors give576R>=max{s,F}; k=0 is covered separately.

## Independent diagnostics

`check_bt002_review.py` and `BT002_review_checks.json` record **5,392 passing checks**:
- 15 rational fifth-power entries;
- 145 exact return-count probability identities;
- 4,950 rational binomial-mode bounds;
- 12 rational grid-spacing/size checks;
- 270 scalar sum-completion stress checks across very large scales, using an integral lower proxy.

These diagnostics corroborate the algebra but are not substitutes for the argument or formal verification. No review blocker remains in the reviewed snapshots.
