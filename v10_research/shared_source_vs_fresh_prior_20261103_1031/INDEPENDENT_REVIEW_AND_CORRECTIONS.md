# Independent review and wording corrections

A separate reviewer checked (A.1), the restricted-information two-point bound (A.2), the retained prior-average form of B.3, the mixture and ε factors, the single predictor-independent strict kernel, the n≥33 sequence, and the B_G comparator against the cited accepted proof sources. The mathematical calculations and quantifiers were found consistent under their stated assumptions. This review is independent model checking, not formal verification or external peer review.

Two precise corrections to the frozen note:

1. In §B, “transition probabilities” should read “valid binary next-symbol probabilities”: every stationary pair mass and every valid probability for the next bit is strictly positive. The 4×4 pair transition matrices necessarily contain zero entries for overlap-incompatible moves. The corrected statement still implies positive mass for every finite binary word.
2. The phrase “not a lower bound ... for all N” should read: inequality (B.3) holds for every N in the stated fresh-source independent-training experiment, conditional on its ε; it does not assert that the right-hand side is positive or that training succeeds uniformly for all N. It is not a sample-complexity lower bound and does not apply to the shared-source experiment A without additional argument.

The review confirms the B_G upper is (2^17+16)M^-1/2+(2^23+192)k/M; its smoothed version adds M^-1/2. The underlying accepted notes and the frozen audit remain unchanged.
