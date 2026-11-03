# Additive clarification: initial pairs

The completed-run report says the generator's starts were not stored. They were not stored as a separate generator array, but the initial pair of every retained word is exactly its first two bits and is therefore recoverable from `ablation_v1/frozen_data.npz`. Initial pairs for rejected and truncated candidate words are not available in that file. The discarded candidate words, latent transition tables, and random uniforms were not preserved. No rejected candidates or latent tables have been reconstructed.
