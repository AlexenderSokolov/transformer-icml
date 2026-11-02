# BK002 — separate all-sixteen-entry enumeration clarification

2026-11-02. Narrow author addendum; fresh independent confirmation and root adoption are separate. **No accepted proof, review, diagnostic, snapshot, binding manifest or receipt has been edited.** This corrects an enumeration omission in prose, not a certificate inequality or a theorem/rate conclusion.

## Exact affected sources

- Accepted proof `binary_beta_known_adaptation/BK002_full_history_supplied_beta_obstruction.md`, SHA256 `e50381632af4825923138c086c34e7b3b082af381d4b9ec8f641825455c50e12`: §2 bullet naming the entries `(1-a)a` and `e*a` does not explicitly name the equal entry `a*e` at position `(00,10)`.
- Accepted fresh review `reviews/BK002_independent_full_review.md`, SHA256 `41f6a35a5224271a6f8cc70a8b84e4099526257b47aef19eb6f64779ca41c3a4`: §3 item6 names only two positions, and its following sentence incorrectly states `2+1+3+1+2+2+4=16` (that sum is15).

The actual displayed squared matrix is correct in both sources. Their exact diagnostic implementations already test all sixteen starting/target positions. The omitted prose position has entry `a*e=e*a`, the same target `delta^2*x`, and the same inequality as explicitly treated position `(10,01)`.

## Complete corrected position partition

State order is `(00,01,10,11)` and the target row is `delta^2(y,x,x,w)`.

1. Two positions `(01,10)` and `(11,01)` have entry `delta*tau` and target `delta^2*x`.
2. One position `(11,00)` has entry `tau*e` and target `delta^2*y`.
3. Three positions `(00,11)`, `(01,11)`, `(10,11)` have entries `a*delta`, `delta*(1-tau)`, `delta^2`, with target `delta^2*w`.
4. One position `(11,10)` has entry `(1-tau)*tau` and target `delta^2*x`.
5. Two positions `(01,01)` and `(10,10)` have entries `e*delta` and `delta*e`, with target `delta^2*x`.
6. **Three** positions `(00,01)`, `(00,10)`, `(10,01)` have entries `(1-a)*a`, `a*e`, `e*a`, with target `delta^2*x`.
7. Four positions `(00,00)`, `(01,00)`, `(10,00)`, `(11,11)` have entries `(1-a)^2`, `e^2`, `e*(1-a)`, `(1-tau)^2`.

Thus the count is **2+1+3+1+2+3+4=16**, and every pair of starting/target states appears exactly once.

For the newly explicit position `(00,10)`, the accepted bounds give `x<=a/e`, `delta^2/e<=1/12`, and `e>=3/4`. Hence

    delta^2*x <= a*(delta^2/e) <= a/12 <= a*e.

This is precisely the accepted argument for the equal product `e*a`. No additional parameter condition, constant, likelihood comparison, source family, kernel, statistic restriction, risk bound or asymptotic quantifier is needed or changed. The three entries in item6 were covered by two distinct algebraic expressions; the prose incorrectly counted expressions as matrix positions.

## Related-source boundary

KH001's pre-freeze draft inherited the same shorthand and was explicitly corrected before its frozen review; its actual before copy and diff preserve that history. Accepted BK001's independent full review instead supplies a complete four-by-four ratio matrix and was not silently rewritten or declared defective. This addendum binds the two BK002 sources above only; it is not a retrospective alteration of their immutable text or root receipt.

This clarification is not a new theorem and does not amount to a new external novelty, formal-verification, or external-peer-review claim.
