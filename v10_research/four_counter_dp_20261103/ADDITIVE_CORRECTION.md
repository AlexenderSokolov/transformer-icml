# Additive correction: exact rational inputs and verification dependency

2026-11-03. This note supplements the original files without changing them. An independent review identified an important difference between the theoretical interface and the present implementation.

The mathematical reconstruction in `RESEARCH_NOTE.md` is an identity over exact rational numbers, and an implementation passing exact integer counters (or exact rational rails) to a fixed utility, combined with exact evaluation and comparison, supports the claimed exact bank-utility optimization. However, `four_counter.py`'s `model_inputs` uses Python `/` and therefore converts its reconstructed rails, including `1/M`, to binary floating-point values before the generic utility is called. An exact comparator alone cannot recover the original exact rationals once that conversion has occurred. For example, at M=3, a rail computed as `1/3` in this implementation does not compare equal to `Fraction(1, 3)`. Consequently, `maximize` as written is not a generic exact-rational utility oracle, and claims of exact rational optimization should not be attributed to it. Its generic utility receives the float-converted inputs. The tested minimum-edit bank reachability/cost map and integer-valued diagnostic objective are unaffected by this qualification. The pilot-input test remains a floating-point comparison with the tolerance stated in the original note. Exact real-valued neural and transcendental utility optimization also retains the original evaluation and comparison caveats.

The diagnostic imports the following external local dependency, whose hash was not included in the unit's original `SHA256SUMS`:

- `v10_research/learned_position_pilot_20261103/pilot.py`: SHA-256 `b297c441d6a54c21dd15d8dcd6b69edc8b561adbeb28dd697f2067f50ea2529c`.

The original implementation, verification outputs, note, and original manifest remain unchanged. The original manifest was rechecked successfully when this correction was written.
