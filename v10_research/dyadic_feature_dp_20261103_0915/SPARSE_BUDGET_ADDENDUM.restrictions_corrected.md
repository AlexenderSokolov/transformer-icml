# Budget-sensitive sparse bound (additive candidate)

2026-11-03. This note supplements `RESEARCH_NOTE.dominance_corrected.md` without changing it. It derives a dependence on the edit budget that the dense O(TS) bound conceals. The argument is deterministic and uses no new samples, model runs, or claims about floating backends. Independent review remains necessary.

At layer t, after processing t of T=M+2 symbols, the number of distinct raw prefixes satisfying the Hamming budget and protected positions, before any optional illegal-transition or terminal-state restrictions, is exactly

  K_t = sum_{j=0}^{min(k,min(t,M))} binom(min(t,M),j).

The final two protected bits, once reached, are fixed by h and do not increase this count. Optional transition restrictions or terminal-state restrictions can only reduce the relevant prefixes. Every retained key is a deterministic function of at least one budget-and-protection-admissible prefix, so the number of retained keys S_t satisfies

  S_t <= min(S,K_t),   S=2^r Q product_j R_j.

Thus a sparse scan considers at most 2 sum_{t=0}^{T-1} min(S,K_t) candidate transitions. This is a transition count, not an unconditional time bound: obtaining increments and state transitions, variable-width integer additions, dictionary key operations and comparisons, exact utility evaluations, memory allocation, and witness output must be charged. An ordered balanced tree yields deterministic logarithmic dictionary operations in the number of stored states, in addition to the cost of comparing its variable-length keys. Retaining all predecessor layers uses O(sum_t S_t) records, with each record's key/pointer bit widths charged; rolling frontiers use O(max_t S_t) records plus their keys and costs. The earlier dense bound still charges initializing S entries per layer and cannot automatically claim the sparse bound.

For each fixed k, K_t=O((M+1)^k), including k=0, so sparse transitions are O(T(M+1)^k) even when b is large; readout and arithmetic still require their own costs. Equivalently, direct legal-mask enumeration performs sum_{j=0}^k binom(M,j) model evaluations and is polynomial for fixed k if each forward evaluation is polynomial. For k growing with M neither expression is generally polynomial. This refinement is an upper bound, not a claim that weighted features compress well on actual trained networks or that fixed-k evaluation is cheap.
