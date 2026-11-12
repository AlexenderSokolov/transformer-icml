# Independent lower-bound audit: relocation and occupation mixture

Date: 2026-11-12. Frozen mathematical source: commit `2ca64346e0dbb19ccf12b5c0f06f12cd0ff31a70`, `v10_research/positional_manuscript_consolidated_20261103/sections/proofs_negative.tex`, Git blob `bb1351ffab5b63dc12dd1a695e174c3b8f08f136`.

## Outcome and scope

Independent reconstruction found no gap in the interior loop-relocation lemma or the occupation-mixture domination lemma. New finite exact diagnostics support their indexing and combinatorics. This is a local LLM mathematical audit, not formal verification, external peer review, validation of the full main theorem, or novelty certification. The source manuscript and historical evidence are unchanged.

The finite critical lower-bound proof was also inspected for the legality of the kernel and the order of measure comparisons. No specific flaw was identified there, but the complete coupling/count-concentration proof and the final finite-horizon theorem have not received a separate exhaustive audit in this unit. Small-word tests below do not satisfy that proposition's large-parameter domain.

## 1. Occupation mixture: independently reconstructed accounting

Let A=00, B=01, C=10, D=11. A path starts at D and ends at A, has M departures, j departures from A and u exits A->B. Delete every departure from A. There remain exactly L=M-j retained edges, with the final edge C->A. For a nonterminal visit to A, replace the retained C->A followed by the deleted exit A->B by a marked C->B of weight 1/2. A direct C->B has the same weight and is unmarked. This gives the stated K(z), including distinct marked and unmarked choices; combining them without retaining marks would lose the exit count.

There are u completed A visits plus one terminal A visit, hence u+1 holding slots. Their total number of deleted A loops is j-u. Weak compositions count these by binomial(j,u). The terminal slot can contain zero loops: the final pair itself is not a departure. Starting at D supplies no initial A slot. Keeping the non-loop edge labels and holding-slot sizes reconstructs a unique binary word.

The resulting identity is

    Q_a(F,J_A=j,U=u) = Pi_a(D) binomial(j,u) a^u (1-a)^(j-u) h_(M-j,u).

For u>=1, integration against da/a gives h/u times the expectation of Pi_a(D) under Beta(u,j-u+1). The stationary factor is inside that expectation and cannot be cancelled. Since it is at most one, the contribution is at most h/u. The u=0 case is not covered; the assumption u0>=1 is essential to this argument.

At z=1, K is stochastic. Writing c_n for the C-state probability from D, one has c_0=0, c_1=t and c_n=c_(n-2)/2+t d_(n-1). Induction yields c_n<=2t (valid also when this bound is loose). Therefore sum_u h_(L,u)=c_(L-1)/2<=t. This sum is at the fixed outside horizon L=M-j, not at a fixed number of marks. Summing h/u for u>=u0 yields t/u0. Restricting the parameter interval or adding an a-dependent event only removes nonnegative mass, so no parameter-independence condition on that event is needed.

## 2. Relocation: attachment indices and the Hamming bound

For r boundary symbols, freeze edge indices i<r-2 and i>=M-r+2. These edge sets and the unchanged initial pair fix exactly the required prefix/suffix. Removing only interior 111 and 000 loops preserves every non-loop edge in order and all attachment states. Reinsert the same total number of edges, so the suffix starts again at its original absolute index.

When both movable loop types are present, the assumed ordered 11-before-00 visit makes it possible to place the full one-loop block before the full zero-loop block. When one type is absent, its distinguished block is empty and every symbol of that type is an 'other' symbol in the counting proof. There is no unstated order assumption on other symbols. When both types are present but the ordering fails, this audit does not apply the transformation.

For a word with a distinguished block of A1 ones before A0 zeros, o other ones, z other zeros, and j=A0+q, the cut comparison gives

    distance <= max(z+q, 2o+z-q).

If a distinguished one is after the target cut, all distinguished zeros are after it; otherwise every one after the cut belongs to the o others. This proves both branches, including empty-block cases.

Endpoint flow supplies N100=N001+1 and N110=N011+1. With d=J01+J10, u=N001, p=N010, w=N101 and frozen loop counts f1,f0:

    o=d+1-p+f1, z=d+1-w+f0, q=u+f0,
    f0+f1<=2r-4, d>=1, u<=d-1.

Thus z+q<=2d+2f0 and 2o+z-q<=3d+3+2f1, both at most 3d+4r-5. The target word is 1^(M+2-j)0^j, whose departure count is j-2, not j. For 2<=j<=M it shares endpoint 00, so the full Hamming distance is entirely within editable coordinates.

## 3. Kernel and signed-loss sanity check

The proposal measures nu_j integrate the alternative family at fixed j, with u>=u0; their mass bound comes from the previous lemma before normalizing. The null mass v_j>=1/(8M) supplies v_j/mu_j>=u0/(8Mt). Crucially, the kernel uses one proposal and identity rejection on every failed distance/endpoint check. It is not repeated rejection sampling. This ensures a strict per-outcome edit budget even outside the good event.

Relocation preserves the proposal's windows, not the null input's windows. The null-to-output window changes are legal because their cost is included in the Hamming test. The sampler depends on the declared horizon/budget and a predeclared auxiliary mixture, not on the true source or the predictor's random seed.

Loss comparison must retain this order: discard nonnegative losses from other inputs/rejections; lower bound v_j/mu_j on nonnegative accepted losses; restrict to the good event; only then apply loss_against_beta >= a-beta-loss_against_a. The displayed proof respects this order and uses unconditional clean risk for the subtraction. No invalid multiplication of a signed expression by a lower mass bound was found.

## 4. Fresh diagnostic and actual results

Run `python v10_research/lower_transport_audit_20261112/check_lower.py` from the repository root. The new script is standard-library-only and does not import or execute historic research programs.

- Enumerated every word starting 11 and ending 00 for M=2,...,14 and every allowed r. All 50,354 eligible cases passed length, exact eight-count histogram, actual prefix/suffix, Hamming bound, protected endpoint and j-2 shift checks. These include 9,481 both-loop ordered cases and 40,873 cases with at least one movable loop type absent. The 1,529 ineligible both-loop unordered cases were explicitly skipped, not counted as successes.
- For five exact rational (a,t) pairs and M=2,...,10, directly multiplied full stationary word probabilities and compared them against an independently computed marked-skeleton identity: 1,410 identities passed.
- Checked 2,505 exact skeleton-mass and beta-derived upper bounds. These are rational bounds after Pi<=1, not numerical quadrature of the stationary integral.
- Repeated the diagnostic with byte-identical JSON output. Optimized Python is rejected so scientific assertions cannot be disabled.
- The repository's seven existing public-integrity regression tests passed in an isolated copy. They test the verifier, not mathematics.

The test set includes parameter pairs outside the finite lower proposition's narrow domain because the two audited lemmas have wider domains. It gives no empirical validation of the full proposition at those small horizons.

## 5. Important finite-scale limitation

The proposition assumes M/k^2 <= A c^2 / 2^20 = 2^-40 and k<=M/8. Combining these implies M>=2^46 (about 7.0e13). This is not a contradiction: the bound is designed to prove asymptotic necessity with loose universal constants. It does mean that ordinary small experiments cannot be called direct finite-domain tests of that proposition. Use small tests for the exact structural identities, and separately design mechanism/rate illustrations with clearly stated status. Do not present the present constants as a practical sample threshold.

## 6. Integrity boundaries and next work

The branch baseline has 3,899 inventory entries whose declared Git blob identities agree with the remote tree, but 293 other tracked files remain absent from the inventory. This pre-existing membership defect is preserved, not concealed by deleting files or rehashing unrelated evidence. Only this unit's new artifacts are added. A full repository byte verification is not claimed; baseline membership already prevents a full pass.

Next bounded units: independently audit the weighted-imbalance lemma and the finite-horizon assembly; analyze the JOR selector directly on lower-witness families; compare the 2026 context-tree-weighting Transformer construction before making architectural novelty claims. No need to rerun these two local combinatorial audits without a changed source or a specific new concern.
