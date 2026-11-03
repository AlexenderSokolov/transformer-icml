# KH001 accepted stronger-side histogram handoff

Root accepted KH001 at2026-11-02 13:37:01.035403 UTC after reading the complete original proof, actual editorial diff and fresh full review. Authority: intake/KH001_acceptance.json. Historical candidate wording remains in immutable proof bytes.

## Exactly accepted result

For the **exact eight triple counts plus initial/final PAIRS**, supplied beta and unknown actual k, no one-constant known-k-rate adaptive predictor exists on any prescribed curve beta>=1/M eventually with beta sqrt(M)->0. Stationary sources already suffice. This is NOT a full-history obstruction or a larger-boundary-window theorem.

The finite theorem uses c=2^-12, delta=sqrt(beta), T=floor1/(8beta), beta in[1/M,1/16], and integer k satisfying32<=k<=T, k²>=4M, k delta>=6/c, delta^5 k³>=2^20, delta³ k²>=2^21. With S the same predictor's supremum clean risk over the explicit stationary family,

    R_null >=[(c k/(64M)-S)log((T+1)/k)]_+,
    H_2(M,k,beta)<=2k/M.

The asymmetric stationary null has1->0 rate1/(2M),0->1 rate beta. Its full long-prefix word probabilities are explicitly charged, its target at00 is beta, and null weights need not be constant. Exact stationary binary-order2 reversal is used only for conditional concentration; the original rare event probability j/M remains in clean-risk accounting. Reversed J00 has a+1 departure correction, which is paid. Canonicalization preserves the exact statistic, and the actual fixed-null Hamming distance is checked on every output.

The map is fixed per public(M,beta,k), source-independent across the whole family, and has no hidden-law or unseen-clean-data input. It is not asserted beta-blind across public experiments. Real probabilities are allowed by the unrestricted kernel model; no efficient/rational implementation follows.

Together with accepted KA001, KH001 completes the **power-law** classification for this statistic: beta=M^-gamma is adaptive at gamma<=1/2 or gamma>=2 and nonadaptive at1/2<gamma<2. The remaining full-history critical/stronger-side gap stays open. A broader arbitrary-domain classification is a separate KH002 candidate, not silently included here.

## Exact versions and actual revision history

- Accepted proof: KH001_histogram_strong_side_obstruction.md, SHA311adf683a22370fe765f61045a96af4a201e611ceeb9136f53a2b1f8cc7fd27.
- Fresh full review: reviews/KH001_independent_full_review.md, SHA0d091d9b6830232e698c6d29ea428a9fe3c21aa4acbba7bbaeb32cb4b5ab5839.
- Root receipt binds both. The independent received snapshot is identical to accepted bytes, and its actual received-to-reviewed diff is empty.

The author ACTUALLY copied the pre-freeze proof before editing it: revisions/KH001_pre_freeze_editorial.md, SHA293dbc410fd0fc49b4221174fff570a6ad4ddecd79c08704208660db2cee38cd. The actual unified diff/record show only the three-position matrix enumeration clarification, updated KA001 acceptance status, and casual->causal typo. No equations/constants/arguments changed. This copy is not a reconstructed earlier version.

The retrospective KH001_RESEARCH_HISTORY.md clearly labels itself as history, not a contemporaneous transcript or reviewed theorem. It preserves the failed symmetric-null/free-prefix route and its asymmetric repair, the reversal count correction and exact-interface limits. It is not an accepted proof premise.

## Diagnostics and inherited sources

Author exact checks:48 complete finite-domain clean families,768 actual-beta and768 null certificate entries,192 three-step atoms,256 generic four-exit reversal families,32,767 exhaustive words and458,753 fixed-null distance comparisons,92 exact full-word null probabilities.

Fresh independent checks:222,601 exact assertions, including108 complete rational family cases,1,728 clean and1,728 null certificate entries,432 atoms; symbolic four-exit reversal/full square; exact coupling marginals; three algebraic irrational-delta cases including one genuinely irrational beta;8,191 exhaustive words,98,305 fixed-null distances,6,096 full-word reversal checks,21 bridge-event identities and345 direct null probabilities. Structural small-word tests are not mislabeled as joint finite-domain tests.

The author read the complete fresh review and separate BK002 enumeration confirmation before this handoff. Finite diagnostics are corroboration, not formal verification. No external peer-review or novelty assertion is made.

KH001_ACCEPTED_BINDINGS.json and build_kh001_bindings.py bind exact proof/review/receipt, diagnostic implementations/results, actual editorial provenance and dependencies. BK001 supplies canonicalization; SC003/BT002 supply the restricted-statistic-compatible known-k benchmark; KA001 supplies only the combined power-law table's other regions. Accepted files remain unchanged.
