# CA001 boundary branches: causal edges versus temporal causality

2026-11-02. Independent scope clarification, not a change to or reopening of the accepted mathematical lower-bound audit.

**Source binding:** `CA001_causal_bounded_softmax_candidate_v3.md`, SHA256 `88e952f840009d8345c4482ca8cd14231f9dd9a28a3d522f12cd7e03b65ea21e`, especially §§1, 4, 7, 9. The frozen candidate is unchanged.

## Interpretation

The primary §1 architecture is end-to-end history-causal: the state at history position t depends only on symbols at positions at most t, and the synthetic terminal position follows the entire history. The fixed-radius causal preprocessing option preserves that property.

The **enlarged §7 boundary-branch model need not be end-to-end history-causal**. It permits all initial-state tables and historical network parameters to depend on an exact side value S containing, for example, the final source symbol. Conditional on a fixed s, attention edges are causal and every branch obeys the required local/Lipschitz contracts. But choosing the actual branch S(X) may broadcast a future symbol to earlier positions. For a minimal example, let S=X_N be binary and set the initial scalar state at every historical position to S. Within each frozen branch the local table is constant (diameter zero), yet the actual state at position 1 reveals X_N. A lower-triangular attention mask alone cannot remove this side-information route.

Accordingly, describe this variant as **a finite-side-information branch extension with causal attention within each frozen branch**, not as an unrestricted family of standard end-to-end causal Transformers.

## Why the lower theorem is unaffected

The audit's replacement, variance and expectation-curve bounds apply to each *frozen* branch on all formal histories, including histories inconsistent with its side value. They need not be replacement bounds for the actual composed encoder `X -> F_{S(X)}(X)` when changing X changes S. The proof never requires that stronger statement: it proves simultaneous branchwise concentration, selects the actual branch, and counts S in the complete decoder message. At most `3^b` witness branches are included. Thus permitting this stronger finite side channel does not invalidate either lower bound or their constants.

The dense-mask variant separately requires public masks independent of the branch. It does not cure or authorize future-information broadcasts through other branch-dependent components.

## Causal subclass suitable for an actual upper/interface argument

A sufficient restriction is:

- historical initial tables depend only on their declared causal local windows and public metadata;
- maps/parameters used at history positions are independent of future boundary symbols;
- any dependence on the full exact boundary value S is confined to the appended synthetic terminal initial query and/or terminal processing/readout, after the history has been observed;
- the decoder may receive S as already granted, and all other primitive, dimension, density, and uniform-bound contracts still hold.

The narrower choice proposed in the synthesis—S only in the synthetic terminal initial query, with earlier tables/parameters independent of future boundary—is sufficient. It is a subclass of §7, so the lower remains valid without another statistical proof. This is a causal-scope statement only: membership of any concrete SRC-like network, its arithmetic implementation, and any upper bound still require their own checks.
