# Separate scalar-extraction amendment review

2026-11-03. PASS for candidate a4194b8e44eff0302d0678df0ed4cc9650a683164950f9fd87acf7e62bf1c6f9 and evaluator 9892df19071f4c8573f59ad9ca9bdc6f681632f7b37b335df2f906e29d0e51eb, subject to the original declared scope.

## Why an amendment was necessary

The root identified a genuine representation-clarity gap after the earlier PASS: exact wiring is sufficient when a master is already stored as numerator bits, but is not an implementation of extraction from a scalar grid coordinate. The prior review interpreted the evaluator's packed numerator interface and did not sufficiently distinguish that interpretation from scalar neural head coordinates. This amendment explicitly repairs that missing bridge. The original REVIEW.md and bindings.json remain unchanged as historical evidence for the prior candidate, not evidence that the wording was always complete.

Read the actual before file, complete candidate diff, amended candidate, added production scalar_grid_bits function and actual test addition. Prior candidate and program snapshots match their earlier receipt hashes. The amendment does not change the statistical theorem or primary packed datapath.

## Proof and cost audit

Scaling a canonical H=B/2^h by 2^h gives integer A in [0,2^h]. At descending j, ReLU(A-(2^j-1))-ReLU(A-2^j) equals the bit indicating A>=2^j because A is integer. Subtracting 2^j times that bit leaves A in [0,2^j-1], proving the next induction step. At H=1 the leading bit is one and the remainder zero. At h=0 the single step handles both possible scalar inputs. Off-grid inputs need not produce bits and remain explicitly excluded.

The recurrence is genuinely piecewise linear, with exact dyadic/integer coefficients and no floor oracle. Each fixed step uses constant active gates and depth; retaining emitted rails costs O((h+1)^2) holds. Threshold/scaling and exact scalar words need O(h+1) bits. Paid initial scalar decode, scaling and twelve parallel extractions are all absorbed by the original p-based widths, depth, parameter bits, all-token work and peak-memory bounds. Extraction happens after replacement, so it does not restore any clean-bank copy or open a new history port.

## Independent executable check

check_extraction.py compares the actual production scalar_grid_bits with an independent exact Fraction recurrence over every canonical numerator for h=0,...,12: 8,204 cases, including H=0, H=1 and h=0. It proves no stochastic claim. It also verifies by AST equality that every pre-existing production function/class is unchanged, so earlier substantive primary-datapath checks still apply to identical code. A deliberately off-grid half-integer example confirms why the theorem is grid-only.

The author separately records a failed-before-added extraction test and successful targeted test; these logs are supplementary to this review's independently executed test. The final amendment receipt binds the actual artifacts and reports the full-suite status at binding time. No theorem or asymptotic bound change is needed. No unresolved extraction-interface blocker remains.
