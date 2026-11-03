# Independent review of FPA001

Review date: 2026-11-03. Reviewer distinct from the construction author. This is a substantive mathematical and implementation review, not external peer review or formal verification. Final verdict and exact hashes are recorded in bindings.json after all checks finish.

## Mathematical and causal audit

Read the complete candidate and actual evaluator, not only a synopsis, against the direction assessment, complete accepted ACG001 candidate and ROOT_ACCEPTANCE.json, SRC-Pi's complete statement and bearing proof sections 2–4 and 9–10, and the positional manuscript's precise finite-horizon comparison theorem. ACG001's acceptance binds candidate 66ca3f2c092eeceb78cdafab97854580df329b28dd5b4d3bb34c28bb5a44d4ed. SRC-Pi is an allowed-semantics precedent, not an imported implementation of this different prefix.

The index transformation t=i+2 is correct. The q=M+2 singleton copies acquire Z_M,Z_(M+1), whereas legal query keys 2 through M+1 correspond to precisely M departures. The terminal pair is not another departure. Flags 2<=t<2+floor(M/2) select exactly the intended first half, including odd horizons. Both missing-lag fallbacks and nonquery uniform-head singleton self masks are causal and nonempty. Query values never flow backwards.

The twelve direct rails are four J/C/D triples, not eight successors plus four half counts. Row(a,b) AND XOR(raw,a) counts precisely the designated successor 1-a. Thus J is paid directly; no factor-two reconstruction error is needed. Every zero-score query head is uniform over the explicitly permitted keys. The exact accumulator and integer nearest-rounding formula give the simultaneous all-path error 2^(-h-1), including 0, 1 and h=0. The replacement-port triangle inequality gives eta=2^(-h-1)+delta without independence assumptions.

Canonical grid numerators plus endpoint bits are the entire downstream data-dependent interface. Readout does not receive M, Z, exact counters or feature arrays. Public h,r and padded fixed schedules do not hide history. The implementation contract is logical access restriction, not malicious-host secure erasure. Corrupting off-grid scalars, endpoints, arithmetic or comparator bits is outside the theorem. No extra error-resilient arithmetic is implied.

Unsigned clipping min(C,J),min(D,J) agrees exactly with ACG001 after the analysis-only common scaling M/2^h. Exact comparison 512D>=J accepts equality; J=0 rejects. Guarded denominator and restoring division produce a legal dyadic binary distribution with error at most 2^-r. Source dependence is only through ACG001; e=M eta yields the displayed coefficient 1072176 eta. The final selected row is valid because attacks protect both terminal symbols. No exact gate-bit recovery, stochastic margin or positive visit-probability assumption is used.

## Finite arithmetic audit

The full-adder/complement subtraction carry implements unsigned comparison. Restoring division's trial remainder fits the fixed width: it cannot exceed the scanned dividend prefix, whose length never exceeds the original w-bit dividend. This addresses the otherwise possible mistaken assumption that one extra guard bit is always free. All actual divisors used are positive. Zero-divisor totalization is irrelevant to accepted outputs.

Prefix width bit_length(M+3)+h+16 holds 2^(h+1)M+M, denominator 2M and every exact accumulation. Suffix h+r+16 holds shifted 512D, 2^r C, guarded divisions, quotient and complement even at r=0. Public shifts are wires, and data-dependent choices use explicit muxes. Packed representation encoding/decoding in Python is not an analog floor oracle. Boolean/ReLU formulas and output dyadic coefficients are finite.

## Complete resource and comparison audit

The candidate distinguishes finite-attention hybrid shape O(p²) depth/O(p) width from attention's charged integer evaluation. The PURE expansion is separately and conservatively charged, not sold at the hybrid depth. All n tokens receive pointwise work; evaluate executes n suffix calls after public zeroing. Historical processing, endpoint acquisition, feature circuits, scratch, holds, clear operations, masks, public addresses, program generation, zero coefficients, output and phasewise memory all appear in the ledger.

Sparse permitted masks have O(n) total edges, so linear-in-n attention arithmetic is defensible here. Dense-mask scanning adds its separate quadratic cost. This is not a construction restricted to ordinary dense causal masks. Active-list/sparse-circuit and dense-mask/dense-circuit profiles are kept distinct. O(np^4) conservative sparse online work includes full O(p) record-address overhead; fixed public routes may be hardwired in the PURE expansion. Offline generation and output writing are explicitly charged. These are proved asymptotic upper bounds, not measured emitted neural-network sizes.

Bank fractional h about half log2 M is only sufficient precision at this specific cut. Exact accumulators, addresses and public horizon words still need order log M; whole batch memory includes resident input and masks. No reduced whole-network precision result follows.

The exact count-only lower comparison is an observation restriction and a simultaneous-over-budgets competitive-factor statement. It cannot become an architecture-wide depth lower bound, and its obstruction disappears when positional evidence is allowed. The ordinary one-pass same-information full/half counter is explicitly cheaper and matches the risk, or reproduces the very same rounded bank when rounding once at the end. The theorem makes no training, neural superiority, optimality or priority claim. This is a legitimate explicit robustness/implementation bridge, not an independent discovery of uniform indicator aggregation.

## Independent executable evidence

check.py was written independently using direct departure-index recurrences and exact Fraction oracles. It checks small-word full banks, several odd/even and power-of-two horizons, all-zero/all-one/alternating/random paths, nearest-grid error, paid mask endpoints, arbitrary canonical replacement banks (including inconsistent counts), exact gate equality and adjacent integers, positive-divisor arithmetic over full words, legal simplex output and designated-symbol routing. checks.json records totals and the exact tested program hash. These finite checks corroborate indexing/arithmetic only; they are not the all-path or stochastic proof.

The reviewer requested two text clarifications before freeze: replace stale pending-ACG language with the actual accepted import; state the precise count-only competitive-factor regime rather than an unspecified boundary-information comparison. Final receipt states whether both were resolved.

## Final verdict

PASS for the exact candidate and evaluator bound in bindings.json, within their declared finite singleton-mask hybrid model and canonical numeric-bank fault scope. Both requested text clarifications are resolved in candidate 50eeb61314fcdcc06d4e88f1e0405797238d788db6f911557d6954326de5acc5. No unresolved mathematical, indexing, finite-arithmetic or full-cost blocker found. Separate scientific acceptance remained pending at this historical review date.

Independent executable checks completed successfully: 1,644 bank/path settings; 2,440 arbitrary replacement/threshold outputs; 1,680 division/comparison cases; 11 metadata horizons. A separate instrumented check_batch.py verifies nine full-batch executions, the exact n suffix calls, zero nonquery inputs, final query-only cut and replacement consistency. All nine source bindings and all nine author artifact hashes matched. Author's five-test GREEN.log is supplementary evidence; this verdict additionally relies on the independent checks and proof audit, not merely that log.
