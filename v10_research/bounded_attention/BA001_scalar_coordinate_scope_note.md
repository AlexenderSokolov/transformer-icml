# BA001 scalar-coordinate clarification

2026-11-02. Clarification accompanying the first frozen manuscript; no theorem or constant is changed.

The parameter D counts **scalar summary output coordinates**, not physical attention heads. The definition provides one weighted-ratio representation for each coordinate d and imposes no requirement that the weights or denominators be distinct. Multiple value coordinates may share exactly the same weight table and denominator. Consequently a multi-value physical head is represented by one d for each retained scalar coordinate.

Thus the proposed SRC specialization D=9K+1 refers to its scalar master bank, not to 9K+1 physical attention heads. The source has four statistical attention heads and two singleton endpoint-copy heads (six total); the latter are covered only insofar as their outputs belong to the permitted exact boundary side information. Exact inclusion is subject to the separate source-interface audit.
