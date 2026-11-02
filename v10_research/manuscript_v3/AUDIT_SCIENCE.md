# Independent scientific audit of revision 3 and Chinese stage-5 guide

Date: 2026-11-02. Reviewer: `independent LLM reviewer`, separate from the author. **PASS recommendation for the revised TeX hash below and the bound guide artifacts.** This is not root acceptance, formal verification, external peer review, a visual-layout acceptance, or permission to publish/upload/send.

## Binding and resolved required correction

Initial assigned TeX SHA-256: `567378793ca270bdd9bc8b982a210dd3a61986e86fc1e4a300c5dd551f7dbb95`.
Final reviewed TeX SHA-256: `6a96169c9438030288c0ae7b4a5895b857ca47673174c755a24c4ab8990cf4f5`.
Frozen v2 TeX SHA-256: `7f07d3af383542b4bb3ccf4e6c050da70077d296e046514241c05335ef3a6e19`.

The root reported one required support-domain correction during this audit. In the initial Lemma 10.2 proof, the square inequalities e²≥βy and b²≥βw appeared before restriction to x>0. They are not unconditional statements about arbitrary unsupported rows in singleton support. The author moved the x=0 singleton/zero-weight case first and explicitly assumed x>0 before the inequalities. I inspected the exact two-hunk `audit-deltas/support_scope_fix.diff` and revised proof. The correction restores the accepted BU001 hypothesis; it changes no theorem, constant, new scientific result or accepted source. The original target is retained in `audit-deltas/pre_support_fix.tex`. The PASS is for the corrected hash, not the original hash.

All 119 entries of the author's previous-version preservation manifest match current bytes. All 27 guide source bindings match. All five new module proofs match their version-specific root acceptance receipt hashes. These checks are recorded in `AUDIT_SCIENCE_CHECKS.json`. An eventual different TeX or guide hash needs a fresh delta check; this report does not silently bind future layout edits.

## Scope and inputs

Read the complete v2→v3 TeX delta (including its new sections), complete new §§9–10, abstract/main-claim changes and revised global alphabet domain; compared the UI001, TR001, BI001 v2, BU001 v2 and BS001 proofs and their acceptance/review evidence. Checked Chinese final mathematical source, extracted all native-equation/prose content, and inspected essential fraction/radical/subscript/superscript OMML structure. Full old dependency reproof and literature priority research are not claimed. Existing statistical/finite-implementation imports retain the manuscript's express dossier dependency.

## Findings

### 1. Global domain and old results

The experiment now permits K≥2, but Theorem 3.1 explicitly assumes K≥3, its threshold corollary names that hypothesis, the rescaled lower is introduced under K≥3, and the old fixed-band and histogram claims retain K≥3. The three-symbol lower is not transplanted into the binary theorem. The new binary claims concern the one-block local positive-ratio family, not the fixed-depth causal family. D,r remain fixed architectural constants; upper inclusion requires D≥K³,r≥3 (binary D≥8). Real lower envelopes are distinguished from integer-weight/dyadic-grid actual programs.

### 2. UI001 uniform grid floor

The heavy-window selection is deterministic conditional on an encoder seed and freezes all boundary branches. It is not adaptive to realized large weights or p. Selected endpoints give N≥m, while N≤Lm; heavy-pattern overlap gives the stated Chebyshev union bound. Partially revealed windows are charged by their number/maxima, not incorrectly assigned their unconditional maximizing-pattern probability. Efron–Stein is conditional on p and revealed B and yields the κ-free variance after the selected denominator charge. The ratio-of-means derivative is bounded by 8r; no expectation-of-ratio replacement occurs.

The posterior is the truncated Bernoulli likelihood, not uniform. On T, distance(y,I)≤3/√N and p(1−p)≥3/16 give the stated 16√N mode derivative; the 16N second derivative and short integration interval give density≤128√N. This remains valid for a truncated boundary mode. The posterior interval mesh and nine-grid-label bound give constant R0, with the actual boundary fixed by B. Intersecting posterior interval and tube events, excluding decoder-output neighborhoods, then averaging both seeds uses a common prior. Constants and the small-history/full-history branch agree with UI001. Finite real κ,Q and negative coordinate flooring introduce no omitted case.

### 3. Full K≥3 joint surface

The high-β branch uses the statistical/grid floors. Large z>M/4 and z>M^(3/4) branches use only t≥1. The complement is inside the exact rescaled lower domain and satisfies x≤z≤y³, giving the factor24 logarithm comparison. Equality boundaries are included. The lower constant min{1/(256·5),cI/2,cb/48} fits every branch and both separate floors. Different lower witnesses are combined by maximum, not by summing losses. The upper uses the same complete triple bank and actual zero-block fallback. Inversion of the product threshold treats v<1 and v≥1 separately and retains the independent Q≥constant·√M requirement. Sufficient target multipliers are not advertised as arbitrary tiny constants.

### 4. Binary active-window lower

The actual stationary law depends on p and remains hidden. The full two-step certificate holds for all four pair states, with the exceptional ea entry using e0²≥β. Histories of different active lengths are disjoint. Domination by the reference active Markov path law is pointwise before prior integration, rather than an assertion that event probabilities are p-independent. The common two-step atom yields a bounded coupling disagreement count and hence positional-local-sum variance and derivative estimates; overlapping windows are permitted. The endpoint-A probability is at least1/8, and its intersection with goodness has mass≥3/32. Only that endpoint's actual target is p. The output-neighborhood argument uses the common joint prior and not a conditional uniform posterior. The truncated sum starts at4, its endpoint J*=4 is covered, and the factor524288 constant follows. No IID-active-suffix shortcut appears.

### 5. Binary return upper and exact decoder ledger

After the support correction, the supported first-step equations, balance and two square inequalities correctly give the weighted hitting bound. Zero weights are omitted before division. Stationary reversal requires pair-coordinate swapping; it is not ordinary pair-chain reversibility. Kac, the family of ordinary hitting/positive-return laws, moment induction and the λ choice justify the exponential return estimate. The small-MΠ branch uses a unit cap. Layer cake uses the integer smoothing threshold, combines the Kac–Markov and exponential bounds, and only then cancels Π on summation over at most four states. No global √β spectral-gap claim follows or is made.

For positive bank mass the floor identity is exact. Its minimum-of-empirical-probabilities bound is valid because N is a positive integer; crossing q=1 is expressly a clipping weight rather than a true exit probability. The ledger correctly charges **2S0+2B0**, **64/z+16/M** for the zero selected bank (including J=0), and **3/Q** including final output rounding. Substitution A=6M/z gives the weighted480W term; adding64/z yields544W. The remaining statistical terms fit2^17/√M. At β<M^-2, including zero, the old β-free upper is used, not a positive-β return proof. The full program/ports and paid costs are unchanged.

### 6. Binary synthesis and alphabet distinction

The binary completion uses cutoff β≤1/256, not the old three-symbol cutoff; the remaining algebra uses only t≥1 and transfers correctly. C=2^17+3+544=131619. The direct real-envelope lower and integer ceil(fQ) upper support a least feasible integer only for the stated sufficiently large target multiplier. At β=1/M the binary cutoff gives t=√M while K≥3 gives t=1, yielding constant versus logarithmic ratio in the same square-root grid band and common sufficiently large fixed coordinate budget. At β=0 both require logarithmic ratio. The improved arbitrary-start binary frontier remains explicitly open; no BAI successor claim is imported.

### 7. Chinese guide and representation scope

The final source is scientifically consistent with the reviewed theorems, domains, conditional proof explanations and unchanged SB ledger. It emphasizes actual-terminal loss, hidden certificate, positive keys, no extra exact ports, no total-cost improvement, and the stationary-only binary refinement. It does not claim external novelty, unrestricted deep-network optimality, formal verification, training attainability or runtime measurements.

The bound DOCX contains exactly126 native OMML objects and no drawings; the bound PDF has6 pages. All126 extracted equations and surrounding prose were checked for content consistency; essential radicals (especially √β versus β), fractions, exponents, thresholds and resource equations were checked in native XML, since flat text alone drops radical structure. No scientific conversion error was found. This is structural/scientific checking, not a replacement for the author's separate full-page rendered layout QA.

## Fresh corroboration and disposition

Independent `audit_science_checks.py` completed with PASS:24 exact-rational binary stationary witness/certificate checks;19,399 exact-rational positive-floor inequalities;1,920 scalar joint-surface branch cases across both cutoffs. The scalar logarithmic checks are floating-point; the finite tests corroborate algebra and do not prove universality. Their result is `audit_science_checks.json`.

**No outstanding scientific change is required for the final reviewed hash.** The sole required exposition correction was resolved and delta-reviewed. Frozen old versions, accepted proofs, guide/source bytes and receipts were not edited by this reviewer. Review artifacts are written only beneath manuscript_v3. Final layout acceptance, root acceptance and any delivery remain separate tasks.
