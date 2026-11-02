# RP001 handoff

## Result
For IID Bernoulli next-symbol estimation with arbitrary initial pair, a CHANGED two-coordinate encoder attains O(M^-1/2+Q^-2) after arbitrary coordinatewise pre-Q-quantization noise c/Q, for any fixed c and sufficiently large dyadic Q. Primitive depth is O(log Q), width and state/coefficient bounds are fixed, and a uniform P=2 log2 Q exact finite evaluator is supplied. This closes the J=2 existence question left open by FN001's encoder-specific failure, subject to root acceptance. It does not recover Q^-J for arbitrary J>2.

## Evidence
- `RP001_theorem.md`: full continuous asymmetric-saw formula, geometric proof, decoder, finite arithmetic, causal/statistical scope, paid ledger, failed approaches.
- `RP001_independent_review.md`: fresh separate-agent LLM adversarial review; PASS, not formal certification or blind/model-independent review.
- `RP001_independent_checks.py/json`: independently authored exact rational tests.
- `check_rp001.py`, `RP001_diagnostics.json`: author exact tests (40,527 uniform-lattice; 10,493 formula; 8,037 noise cases).
- `RP001_source_bindings.json`: imported accepted receipts/proofs/reviews and attribution.
- Root's independently convergent alternate formulation is preserved separately in `ROOT_ALTERNATE_SNAKE_NOTE.md`; it is not needed by the reviewed proof.

## Important boundaries
Noise is AFTER reliable fine evaluation but BEFORE Q quantization; clipping to [0,1] is explicitly part of the channel, or perturbations must stay in range. Only two final labels survive. No arbitrary boundary-bit restriction is needed by the upper because all side data are unused. No internal-noise, learning, full Markov upper, optimal decoder-complexity or novelty claim. Geometric packing/nearest-curve decoding is established prior art, especially Uss et al. (2025); iterated ReLU tent is established as recorded in FG001.

## Useful successor
The live mathematical gap is an explicit fixed-width bounded-primitive O(log Q) robust scalar-to-J-rail construction achieving Q^-J for each fixed J>2. A naive recursive Hilbert/snake claim does not suffice without an actual network, decoder, and exact/controlled evaluator. Alternatively optimize the present O(Q) nearest-edge decoder via root's row-rounding approach; that is an efficiency refinement, not necessary to the existence result. Root controls successor selection.

No frozen artifacts were modified; no private proof was uploaded or externally communicated; no purchase/publication/contact action occurred.
