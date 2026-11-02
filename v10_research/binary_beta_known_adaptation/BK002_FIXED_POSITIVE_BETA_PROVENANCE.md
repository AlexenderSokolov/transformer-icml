# BK002 ancillary fixed-positive-beta provenance clarification

This clarification does not change the accepted BK002 proof bytes or any theorem constant. The full independent review noted that BK002 §9's fixed-positive-beta k-blind remark should be tied to the generic ordinary-add-one upper, not to the k-aware SC003 estimator alone.

The relevant source is `source_symbol_corruption_mixing/SC002_theorem.md`, §§1–2. Its theorem statement restricts the matching nonbinary frontier to K>=3, but the upper-bound proof uses only histogram l1 stability, the K-state clean comparator, K^2-state occupation and the all-state mixture argument. Those steps also apply at K=2; the three-symbol restriction enters its matching lower construction, not those upper steps. The fresh BK002 reviewer explicitly audited this upper-interface use.

For fixed beta>0, the resulting k-blind ordinary-add-one upper is a constant depending on beta times max(M^-1/2,k/M), since 1+log(1+1/(beta k))<=1+log(1+1/beta). This does not supply a constant uniform as beta moves, and therefore does not contradict BK002. No new claim that SC002's full nonbinary theorem has been silently relabeled binary is made.

Exact source and receipt hashes are bound in `BK002_ACCEPTED_BINDINGS.json`. The accepted proof remains SHA256 e50381632af4825923138c086c34e7b3b082af381d4b9ec8f641825455c50e12.
