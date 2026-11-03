# FOT001 actual exploration history

2026-11-02, 19:08–19:12 UTC, local author work only.

1. Read the root's unreviewed renewal-mixture proposal, natural first-order PLAN/FOL001, and WPC001. Read original certificate calculations for the exact original definition.
2. Verified the proposed fixed-v renewal identity analytically; no counterexample was found. Kept v=j+1 and the null's j−2 occupation shift distinct.
3. Derived the forced00/reversed terminal11 conditioning, adding one to the coupling discrepancy for the forced first edge. Used σ≤x/32 and increased the finite threshold to ck≥4096. Added a separate V00 lower-tail event; U alone does not guarantee j≥2.
4. Selected null β=1/(N−1), rather than silently reusing FOL001's β=1/N. Verified all pair-chain certificate entries by the first-order ratio identity.
5. Wrote FOT001_candidate.md, with finite lower, common kernel, explicit g_N factor, and paid M=N−1 conversion.
6. Wrote and ran check_fot001.py once. First run passed: 16,382 ordinary endpoint words; 1,235 coefficient identities; 1,118 beta identities; 4,095 pair-endpoint shifts; 11,769 relocations; 164 renewal checks; 48 certificate entries; 15,519 null mass checks. Exact largest displayed conditional failure bound is 7633633283/274877906944 < 1/16.

No independent review occurred within this task. No accepted file, manuscript, external repository or external state was changed. Root owns any later review and acceptance decision.
