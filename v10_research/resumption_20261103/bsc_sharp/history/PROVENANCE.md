# Provenance limitation — reconstructed earlier draft

The first author write used an overbroad shorthand defining loss against parameter a on all words; that definition is wrong off the endpoint event F. Author self-check and root reading independently identified the same issue. The current source defines genuine clean loss at the actual terminal symbol, equal to a-target loss only on F, and uses that unconditional clean risk in the k=0 comparison.

`CHANNEL_LIKELIHOOD_LOWER.before_actual_terminal_fix.md` is a **post-edit reconstruction**, obtained by reversing the two known string edits (actual-terminal repair and the added erasure-support limitation). It is NOT a pre-edit filesystem snapshot. The provenance record states that the earlier draft text was available during review and was read before repair. However, no independent pre-edit source hash was recorded, and no automated byte-for-byte comparison with an exported creation-command transcript has been performed. Therefore this artifact is not certified as a byte-exact preserved original.

`actual_terminal_loss_fix.diff` proves the differences between the two currently available files only. It does not by itself prove the historical identity or timestamp of either file. The scientific correction is explicit and reviewable despite this archival limitation. No hypothetical failed proof is being presented as an executed historical artifact.

The repaired candidate was actually hashed with sha256sum after the edits: d410a88fa63ae0de06bb7140296f85fc0ca3fa7b63c8bed8964fec81a4b9072e. Subsequent edits to that source, if any, require a new binding.
