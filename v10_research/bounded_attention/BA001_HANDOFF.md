# BA001 author handoff

## Result first

The extension succeeds for a precisely bounded family: one dense M-key block, fixed D scalar heads, trailing-r local inputs, exact first/last-r side windows, positive weights in [a,b], values in [-1,1], source-independent position/M/Q/beta-dependent tables, and downward-Q quantization. Unlimited real decoding and source-independent randomization are allowed.

The complete proof gives both:

- Stationary all-Q rare-suffix logarithmic lower for K>=3,M>=64,beta<=1/16: `c/Q ln(1+(1/8)min{Q/(M max(beta,1/M)),M/Q})`.
- Separate stationary IID `c_I/Q` lower for every beta<=1 and Q>=1, within the same family, not imported from original SRC.

There is also the full-history IID `1/(128sqrt(M+2))` floor. Maxima, not additions, combine witnesses. Constants depend only on D,r,a,b under value normalization; a general value bound V must also enter them.

## Proof innovations and checks

All finitely many boundary queries are frozen and covered simultaneously, so no false IID assertion after endpoint conditioning occurs. Numerator/denominator bounded differences yield exact concentration even with arbitrary positional tables. Comparison curves are ratios of means, not means of ratios. Product-Bernoulli differentiation gives uniform Lipschitz bounds; no monotonicity is used. The single IP002 parameter prior is preserved across all stationary suffix events and the true future exit mass remains in the target.

`check_ba001.py` passes 852 exact local-sum / numerical cutoff checks, and exhibits a nonzero ratio-of-means versus mean-of-ratio gap to make that distinction concrete. This is author corroboration only, not independent review, a universal proof, formal verification, or actual original-emitter execution.

## Draft changes before first freeze

The initial draft used an unnecessarily intricate sharper tube count. Before first manuscript freeze it was simplified, and N was consistently changed from `ceil(2C+3)+1` to `ceil(2C+4)+1` to cover intervals of length 2C+4 directly. The early model-only freeze did not freeze text or a manuscript hash. Section 8 (the generic IID c/Q theorem) was added at the parent's request before first manuscript freeze. No accepted predecessor was changed.

## Pending independent review / interface audit

The first manuscript freeze and hash are recorded in `BA001_source_bindings_v1.json`. Review should scrutinize encoder-family quantifiers, side windows and query union, per-coin influence bounds, curve covering cardinality, common prior, true target, high-Q completion and independent IID c/Q branch. Root is separately auditing exact SRC inclusion; this manuscript makes no unverified interface inclusion or architecture-universal assertion. No blocker remains on author derivation.
