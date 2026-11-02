# BC001 v1 pre-acceptance revision note

2026-11-02, author revision log. No accepted dependency or stage-5 frozen file changed.

1. Replaced the scalar-completion notation `3/e` by `3/exp(1)` to distinguish Euler's constant from the manuscript's cutoff variable `e=max(sqrt(β),1/M)`.
2. Root review identified an overbroad capacity sentence: the initial draft required affine row-sum bound at least three and simultaneously said CF001's original budget already sufficed, although CF001 only promised a bound of at least two. The corrected main prototype uses supplied exact 0/1 triple-feature tables, requiring only row-sum-one projections, within the declared row-sum-at-least-two budget. The optional explicit `ReLU(u+v+w-2)` local-AND alternative separately requires row-sum bound three. These two implementation alternatives are no longer conflated.
3. Made the main synthetic initial state explicitly zero. S is used only by this prototype's decoder; no terminal query coordinates are needed. Width 16 suffices for eight old triple-feature slots plus eight head-output slots. A larger implementation may carry unused terminal query coordinates only while paying their additional storage.

These were pre-acceptance clarifications, not changes to the Markov lower, exact finite histogram identity, risk theorem or cost-ledger alternatives. The original text existed in the drafting tool transcript; no pre-change filesystem snapshot was retained, and none is reconstructed. The final proof SHA256 after these changes is `38712b68da30e08d14f41567e84f53b4073b7e2d46280313adc8b69859fc850e`. The independent reviewer is asked to bind this note along with the final proof.
