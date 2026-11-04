# Exact-file review of the stationary output composition

Date: 4 November 2026 (UTC).

Verdict: **PASS**, as a composition of the newly reviewed statistical theorem with the inherited pathwise architecture and arithmetic guarantees. No change is required.

## Exact binding and review scope

Reviewed source: `stationary_output_corollaries.v1.md`.

SHA-256: `27a41007b136087cc34e63dcb2facf0a6df667bad1a3fcea80d448a1e12162ab`.

The source was read in full and its hash checked. Its statistical theorem and review bindings agree with the frozen files already reviewed. The inherited composition and precision-source hashes were also checked and agree with Section 6. The cited precision adversarial review, including its signed-range Section 7, was read. Relevant exact-real source statements and its KL-transfer derivation were inspected.

This is an independent audit of the substitution, scope, boundary cases, and faithful inheritance of the numerical-model requirements. It is **not** a fresh independent proof of every architecture or arithmetic lemma, an implementation test, formal verification, or external peer review. No numerical tests, simulations, training, external uploads, or repository mutations were performed. Source files were not modified.

## Findings

1. **Statistical substitution and actual terminal query.** V_stat is copied correctly from the reviewed stationary theorem, including its constant 4608, dyadic count K_n, cap, and A^2 prefactor. The source requires stationarity of the original pair law and permits zeros, periodicity, reducibility, and multiple stationary classes. The same observed-word terminal pair is used throughout; no independent query or terminal-state conditioning assumption is introduced.

2. **Exact-real transfer.** The inherited source gives the all-word TV bound (44A+1)/L and support floor 1/[1+(A-1)L]. Substitution into the established pointwise KL inequality gives exactly 2 V_stat + 2A(44A+1)^2/L. The alternative cap log[1+(A-1)L] follows directly from the support floor. No architecture assumption or coefficient changes with this statistical substitution.

3. **Finite-bit transfer.** The precision source gives an exact nonnegative H-grid simplex, the TV bound (46A+2)/L, support floor 1/(4AL), and pointwise penalty 8A(46A+2)^2/L. These are reproduced correctly. Taking expectations gives equation (3); log(4AL) is a valid separate cap. The argument uses positivity and the squared-error transfer, not TV alone. The explicit algorithm restriction and prohibition on unspecified additional rounding are appropriate.

4. **Transfer constants.** The inherited inequality is D(T||Q) <= 2D(T||B) + sum_b (B_b-Q_b)^2/Q_b. Because B-Q sums to zero, its squared norm is at most 2 TV(B,Q)^2. Combining this with the respective floors 1/(AL) and 1/(4AL) yields exactly the factors 2A and 8A in the two output penalties.

5. **Zero transitions.** At n=0 the source does not evaluate log_2 n or V_stat. B is uniform, so substitution of log A is valid. The stated L=A+2 and both boundary formulas match the inherited all-word guarantees. The precision source explicitly covers N=2 and explains why no nonexistent data transition is used.

6. **Precision schedule and range.** The schedule s=ceil(log_2(AL)), b=32s, H=2^b, F=H^2 is identical to the reviewed arithmetic source. The note correctly distinguishes fractional precision from total signed width. Its copy O(L^3), narrow O(L^2), terminal-only broad O(L), and earlier-coordinate A^2 statements match the adversarial review. Signed raw scores and maxima, accumulation and guard space, and approximately 4b-bit temporary F-grid products are properly retained. Thus O(b+log A+log L) working lengths are not misrepresented as b total signed bits or a fixed exponent range.

7. **Resources and implementation limitations.** The displayed schoolbook operation and row-streamed storage bounds exactly match the precision source. Length-dependent evaluation precision is not presented as a learned parameter. Changing A is correctly treated as changing the architecture/vocabulary family. Generic IEEE, GPU, mixed-precision, fixed-word, training, and executed-performance guarantees are expressly excluded.

8. **Alphabet dependence and lower comparison.** Each output penalty is O(A^3/L), with absolute constants, and L>=n+1. Hence the statistical O(A^3 log(n+2)/(n+1)) bound and its sufficient consistency condition carry over to R and the specified Q. HJW's observed length is N=n+2; its domain and logarithm are retained. The fixed-eta subregime comparison is correct. The minimax lower bound applies to every history-dependent probability-vector predictor, including R and this Q, so the fixed-A stationary worst-case Theta_A(log n/n) conclusion follows. It is not a pointwise lower bound or a full growing-alphabet optimality claim.

The preserved arbitrary-start theorem is not silently upgraded: the composition expressly retains its A^5 bound. The conclusion is therefore accepted within the inherited exact-real and specified integer/dyadic models, with all stated qualifications.
