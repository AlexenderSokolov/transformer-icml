# GD001 independent delta review — terminal-input scope

2026-11-02. Fresh independent review of the sole lower-manuscript delta relative to `preclarification_20261102T065250Z/`. The original full review is preserved; this receipt supplements, rather than silently rewrites, its source binding.

## Verdict: PASS

The new paragraph in lower §1 correctly closes the synthetic-terminal input scope: all historical local tables have indices strictly below T; the initial terminal state depends only on public metadata and the finite frozen boundary label S. Any source symbols used by the terminal local query must be included in the counted b0 slots before forming H_b=3^b0.

For a fixed branch S, source-coin replacement therefore leaves the initial terminal state unchanged. Its changed initial historical states are at most r, all strictly below T. Thus CA001's off-diagonal matrix-entry envelope applies to every affected state. No direct diagonal a^l term is omitted. Coins near N may affect fewer historical windows, which only improves the at-most-r bound.

Freezing the augmented label is legitimate because all primitive/range contracts are required on every formal source history with that label fixed. The proof establishes concentration simultaneously over the finite branches before selecting the actual one; it does not assume conditional independence after observing the label. Increasing the fixed b0 changes only the fixed concentration/cardinality constants, not gamma_l's exponential order or the log-log depth conclusion. The explicit upper construction's terminal pair consists of two source symbols and fits this clarified label contract.

The diff contains only this scope paragraph: no probability, harmonic bound, arithmetic certificate, complexity formula, or numerical constant was otherwise changed. The updated model is the intended CA001 frozen-boundary extension, not a claim covering unrestricted history-dependent terminal initialization.

Independent diagnostics were rerun against the final manuscript set: all 18,132 cases PASS. They support unchanged algebra but cannot detect an omitted information port; the terminal-input scope was checked mathematically as above. Final lower and original review bindings follow.

## SHA-256 bindings

```json
{
  "v10_research/growing_depth/GD001_lower_derivation.md": "3137d43739fe39e80490b7f8b1c76f85495e4b7078e31c52a8f3ea9b1831e000",
  "v10_research/growing_depth/preclarification_20261102T065250Z/GD001_lower_derivation.md": "217141c39fc71ffaa104f1e3caa5eae0fc0cd125fbdb8e44b3eb44bf1ba70c13",
  "v10_research/growing_depth/preclarification_20261102T065250Z/GD001_independent_review.md": "6dd03b39a6fca0f082bdfc259bc895cc472d0fe4f9ebf49aafc4a5c0042ad971",
  "v10_research/growing_depth/GD001_independent_review.md": "6dd03b39a6fca0f082bdfc259bc895cc472d0fe4f9ebf49aafc4a5c0042ad971",
  "v10_research/growing_depth/GD001_independent_checks.json": "4ebd10277b157e177ad47aa9340f0ac5a05df76ae22ff7a49cb27682d8ee9e58"
}
```

No formal verification, external peer review, novelty claim, or broader architecture acceptance is implied.
