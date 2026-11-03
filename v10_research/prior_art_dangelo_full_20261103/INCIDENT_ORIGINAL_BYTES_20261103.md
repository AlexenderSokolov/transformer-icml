# Preservation incident: D’Angelo audit original bytes

On 2026-11-03 the author reported `AUDIT.md` as completed to the research coordinator, and then edited that already-consumed file in place. This violated the agreed requirement to preserve every consumed source version. The exact complete original bytes and their SHA-256 were not captured before the edits. They cannot be verified or recovered from the partial conversation and must not be claimed to have been recovered.

Known from the author’s actions, the later edits removed an unsupported sentence suggesting an ordinary non-BOS candidate could trigger the BOS indicator; added the Appendix D.3 candidate-range discrepancy; and added the explicit Lemma D.1 Taylor-approximation/no-remainder-bound description. This is an account of known changes, not a substitute for the lost complete version or its hash.

Current preserved artifact bindings (SHA-256):

- `v10_research/prior_art_dangelo_full_20261103/AUDIT.md`: `dbf4ca4474c8a681ca9280d95c4741f39825656adfa9d02d087c28373b3af116`.
- `v10_research/prior_art_dangelo_full_20261103/SELF_CHECK.md`: `af88c81b3a20dcf9662fc1dce028547d41aa803aa43a2e227aaf6aae20033836`. This is author self-check, not independent review.
- `v10_research/review_dangelo_independent_20261103/REVIEW.md`: `028e588fdcb220ddd51dbe3b16ac33554c299bfd18a09b00beb9b403c75fcf85`. This is the separate independent source/algebra review; do not infer it reviewed the missing original bytes.
- `v10_research/prior_art_dangelo_full_20261103/ADDENDUM_INDEPENDENT_REVIEW_20261103.md`: `48a6d23363202c6cbdc3928848a598f54850a80d28b7b8b8372e0f4db0e81855`. This author-prepared addendum incorporates the independent review’s count-weighting, positional/indexing, and candidate-range cautions and cites the primary source.

All these files remain distinct. Do not edit a delivered or consumed artifact in place; issue any later correction as a new, separately hashed file. The exact scope of the independent review remains what is stated in its own text; its SHA binds that text, not an unknown earlier byte version of the audit.
