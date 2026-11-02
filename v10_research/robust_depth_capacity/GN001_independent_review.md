# GN001 full independent adversarial review

2026-11-02. **PASS.** This is independent LLM mathematical/interface review, not external peer review, formal verification, novelty certification, or training validation.

## Material reviewed

`GN001_theorem.md`; accepted IC001 and IR001 theorem statements and boundary/initialization restrictions; FA001 v3 §§1–6; GD001 uniform growing-depth extension; RG001 geometry as read-only background. The separate independent geometry review and exact-rational checker are supplied alongside this report. I also inspected the author's `check_gn001_finite.py` and its successful finite diagnostics.

## Findings

1. **The geometric modification is real and sufficient.** The shifted first tent must be T_ext, followed by k−1 ordinary tents. Its phase law starts moving at every row start and reaches the opposite endpoint at phase 1−eta. It stays clipped thereafter while the outer coordinate moves. Recursive edge intervals tile [0,1] without gaps. The independent proof establishes simplicity, injectivity, nonincident separation >=1/N, and minimum moving speed >=N^(J−1). Vertices carry zero duration. The local inverse bound holds at vertices and global endpoints without an additive plateau term; strict image distance <1/N is retained.

2. **Noise constants are safe.** Finite arithmetic contributes 1/Q, the attack c/Q, and the final floor at most 1/Q coordinatewise. Clipping is nonexpansive relative to an ideal cube point. Thus r0=sqrt(J)(c+2)/Q. A nearest curve projection is within 2r0 of the true curve point. N<=Q/[4sqrt(J)(c+2)] gives 2r0<=1/(2N), strictly inside the local-inverse scale. The recovery constant is exactly 2sqrt(2J)(c+2). Its pointwise nature covers randomized history-dependent attacks. Empirical-mean sampling error is the sole extra 1/(2sqrt(M)) term; adding a separate mean-rounding term would double-count the FA certificate.

3. **Capacity/depth algebra is valid for all declared Q.** When Q>=sqrt(M), scalar fallback gives multiplier 1/2+c+2. Otherwise R=(sqrt(M)/Q)^(1/(J−1))>1 and the least dyadic N>=R obeys 2<=N<2R. Q^J>=(2B)^(J−1)sqrt(M) implies 2R<=Q/B. Also Q N^(J−1)>=sqrt(M), and log2 N<1+log2(sqrt(M)/Q)/(J−1). These prove the stated sufficient risk and depth bounds. Small Q or absence of an admissible snake introduces no false universal construction claim: fallback is always available, while the statistical-order sufficient claim has its explicit capacity condition. The necessary and sufficient constants are appropriately different.

4. **The rational-description extension is valid and explicitly new.** FA001's defining conversion proof needs |theta_fin−theta|<2^−P, not a dyadic ideal coefficient. Exact signed long division of 2^P a by positive b provides that same bound, with negative remainder correction and the declared bit costs. The affine perturbation estimate, rounded-state neighborhood bounds, Taylor positivity and normalized-sum analysis are otherwise unchanged. All new ideal coefficients and reachable states have uniform bounds independent of N. Consequently the GD stagewise recurrence and bootstrap apply with constants fixed by the per-stage bounds, not by the whole growing-depth network. Initial mean evaluation and all coefficient/activation rounding sites are included. No illicit exact-lattice claim is used.

5. **Finite decoder is constructive.** Edge/time endpoints have O_J(log N) rational bitlength: fixed J bounds recursion depth and denominator factors. Nearest-edge projection and squared-distance comparison use exact rational arithmetic; selected inverse requires O_J(log N+h) bits. Enumerating O_J(N^(J−1)) edges is explicitly paid. This is not a logarithmic-time decoder or a real-valued projection oracle.

6. **Lower transfer respects scope.** Zero attack is admissible. IC001 uses only the same bounded ideal primitive family plus a fixed E/Q tube, so finite rational descriptions do not defeat it. Enlarging the fixed primitive bounds once merely changes C and gamma. Positional boundary bits are not replaced by arbitrary nonlocal side information; fixed public initialization and all-formal-history frozen-branch hypotheses remain stated. Arbitrary initialization includes both the fixed initial pair used for the statistical lower and the stationary product initial pair used for IR; these are separate valid minimax witnesses. IID upper claims are not transferred to general Markov sources.

7. **Resource accounting is conservative, with two clarified notational points.** Scalar fallback must use constant decoder edge count E_J=1, now explicitly included. Generation must stream compact rational records and bit masks with reusable O_J(w) scratch, retaining the rational edge table in E_J w bits; otherwise a claimed padded (U+F)w generator array would need an additional phase-peak charge beyond the displayed compact S0. The author applied this explicit compact-generator clarification; I checked the amended text. No outstanding condition remains and no mathematical construction change was required. The address-scan/unrolling alternative is deliberately much more expensive and its true program, tape, work and phase scratch are charged. Primitive depth is not confused with PURE or bit-operation depth.

## Independent executed diagnostics

- `GN001_independent_geometry.py/.json`: PASS; 10 parameter cases, 1,680 phase identities, 22,201 nonincident edge pairs, 2,610 sampled local-inverse inequalities, plus endpoint, interval-tiling, speed, and exact formula/table checks.
- `GN001_independent_full_checks.py/.json`: PASS; 39,600 signed rational conversions, 640 full-product affine perturbation checks, 8,000 GD precision inequalities, 45,956 exact squared capacity/selection checks.
- Author's `GN001_finite_diagnostics.json`: inspected PASS; six finite rational-snake cases and corner attacks. The script's hardcoded precision coefficient 16 is a diagnostic choice, not an independently certified universal c_FA. Universal validity comes from the symbolic FA/GD proof and finite search for its architecture constant.

Finite enumerations are supporting evidence only. No numerical tests establish universal bounded-depth behavior by themselves. No substantive mathematical counterexample or unclosed theorem gap was found.

Reviewed theorem SHA-256: `743367f687c79ea9b3abfbecaa70b206fe62afb5fbb56d1643331aacbfc18383`.
