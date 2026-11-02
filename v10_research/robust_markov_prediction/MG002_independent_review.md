# MG002 independent review — partial-capacity general Markov extension

2026-11-02. **PASS**, subject to root acceptance of MG001 and MG002. Independent LLM review plus exact finite diagnostics, not formal verification, external peer review, hardware/network emission audit or novelty certification.

Reviewed MG002 theorem SHA-256: `7b9c72da1bbaa6ddafcba66fabe80cf25b467703bfeca7b9afa8e00f0f8e8d93`.

Read the entire MG002 theorem, current clarified MG001 theorem and its independent review, full GN001 theorem and independent review, and GN001 root acceptance receipt. The accepted GN001 theorem hash is `743367f687c79ea9b3abfbecaa70b206fe62afb5fbb56d1643331aacbfc18383`. Current MG001 theorem hash is `c4f114bb7510f3dd5ead7461d9ebead092e2abe103fc92f96e3af9fbd4ac6623`. No theorem edited by this reviewer.

## Findings

1. **The transferred dependency is pointwise geometry, not IID risk.** GN001's shifted no-plateau curve is defined for every input in [0,1]. Its separated nonincident edges and minimum moving speed yield the local inverse estimate for arbitrary nearby observed coordinates. Nothing in that estimate requires its input to be an empirical IID mean. Applying it to g_L(x)/2 is therefore legitimate. The MG statistical argument remains the separate actual-terminal triple-count/occupation proof, with arbitrary initial pair law.

2. **Noise bookkeeping remains complete.** The generic finite approximation applies to the entire compander-plus-GN composition; its 1/Q tube already includes the original pool floor and all rational coefficient conversion and activation floors. Adding attack c/Q and the final floor gives c+2, exactly as GN001's geometry expects. No duplicate empirical-mean arithmetic term is added. Multiplying the recovered scalar by two gives 4sqrt(2R)(c+2)/(Q N^(R-1)); range clipping cannot increase it. The absence of a plateau term is guaranteed by GN001's no-pause timing, not assumed for the old RG curve.

3. **The scalar fallback handles large Q honestly.** For Q>=sqrt(M), transmitting just t and ignoring padded coordinates gives compander-space error <=2(c+2)/Q. Padding is still counted in width, cut alphabet, parameters and work. This branch needs no separated snake, so Q values without an admissible N do not produce a gap in the stated sufficient theorem. The capacity condition is sufficient and may be unnecessarily strong for scalar fallback, but is not claimed necessary there.

4. **Capacity algebra and integer selection are exact.** In the snake branch u=(sqrt(M)/Q)^(1/(R-1))>1. The smallest dyadic N>=u has N>=2 and u<=N<2u, including u already dyadic. Squaring the selection test gives the executable Q^2 2^(2k(R-1))>=M with k>=1. From Q^R>=(2B0)^(R-1)sqrt(M), direct rearrangement gives 2u<=Q/B0. Consequently N<Q/B0 (the weaker stated <= is safe), and GN locality holds. Also Q N^(R-1)>=sqrt(M). The claimed error multiplier A0 therefore bounds both branches. Integer upper bounds substituted consistently for setup constants only strengthen the sufficient capacity condition; no irrational setup oracle is required.

5. **The general-Markov risk follows with the constant multiplier.** MG001's symmetric inverse estimate is valid for every epsilon, not only epsilon<=M^-1/2. Substituting epsilon<=A0/sqrt(M) gives residual 4A0^2/M+2A0/(chi sqrt(M)). The same capped-Psi/subadditivity proof gives O_(K,R,c)(M^-1/2), because A0 is fixed once R,c are fixed. Empty rows and false positive reconstructed masses remain covered by add-one normalization. Hstat's beta=0 fallback treats the unrestricted homogeneous class.

6. **The finite-data extension is properly explicit.** GN001 proves signed rational-to-P-grid conversion with error below 2^-P and its full division/scratch costs; FA's remaining perturbation proof uses only this error and the uniform ideal bounds. Thus the composed stage recurrence and GD bootstrap apply without an exact-rational-lattice claim. Dyadic compander parameters are already a subclass. N<=Q/B0 implies all rational snake descriptions and decoder integers fit the stated O_(K,R)(h+L+log M) guard bounds. No parameter of order N is smuggled into a bounded primitive; repeated saturated doubling is counted.

7. **Resource and family inheritance are intact.** MG002 inherits the clarified MG001 choice of a paid radius-three local TABLE for the common dense-family comparison, not a sparse singleton head. It also inherits explicit wide encoder-word to decoder-word bank conversion and coexistence costs. E_R=1 is explicitly selected for scalar fallback. In the snake branch E_R=O_R(N^(R-1))=O_R(sqrt(M)/Q), since N<2u. This is a table-size statement, not constant-cost rational arithmetic or total-time efficiency. Dense zero slots, masks, all-token work, parameter generation, conversion, exact inverse/normalization, clearing and offline phase peaks are preserved. The smaller primitive depth is never asserted to be PURE or bit-machine depth.

8. **Depth and lower scopes are honest.** Log N<1+log_+(sqrt(M)/Q)/(R-1), so adding compander depth gives the displayed upper. IR's necessary logarithmic term uses the same fixed-position boundary and uniform finite-approximation family; the theorem does not claim to resolve the remaining additive compander term for every Q or K. The output-dimension capacity gap R versus D=RK^3 is explicitly retained. At the minimal sufficient Q scale, both named upper and lower have order log M, with no same-constant frontier assertion.

## Executable independent checks

`MG002_independent_checks.py/.json` use exact integer squared inequalities with computable integer upper bounds for radical constants. Across R=2,...,6, c in {0,1,3}, h=1,...,24 and lengths around powers 2^6,...,2^64, 51,823 capacity-admissible cases passed: 27,431 scalar cases and 24,392 snake cases. The checks verify branch selection, minimal dyadic N, separation capacity, target recovery scale and the table-size upper. No floating-point logarithm or root decides an inequality.

These diagnostics do not verify the full evaluator; the complete symbolic FA/GN/MG argument is necessary. No blocking mathematical or interface gap was found.
