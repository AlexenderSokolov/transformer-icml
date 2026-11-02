# Independent hostile audit — FA001 v2

## Result first

**ACCEPT the constructive all-operations finite-arithmetic bridge for its explicitly specified subclass, not merely a conditional CA001 transfer.** No mathematical or sequential-access blocker was found. The certified claim is the existence of the specified deterministic signed-integer evaluator, with final pre-cut error at most `1/Q`, fractional precision `P=4h+C_arch`, and the separately charged length-dependent accumulator/data/control storage. It is **not** an h-bit-everywhere algorithm, a certificate for arbitrary old emitters, or a claim about unrestricted Transformers.

One nonblocking storage-layout clarification matters: interpret the `O(w)` public numerical slots in §6.1 as compact `P+O_arch(1)` slots; hidden/projected/scratch words may use `w` slots. This is a permitted `O(w)` choice and realizes §6's `UP` term. If an implementer instead pads **every public parameter record to Θ(w)**, replace `UP` by `Uw` in peak and zeroing/write charges. The latter implementation does not inherit the smaller peak ledger. This review does not silently mix the two choices.

Reviewed target SHA256: `c50fb971193d255ae543a374597778b2447eac9cefec7b26176af58caa4917fd`. No frozen source was edited. Separate bindings record all inspected sources and review diagnostics.

## 1. Scope and model-interface audit

- FA001 is a strict finite-data affine/ReLU subclass. Fixed dimensions/depth/fan-in, uniform coefficient bounds, and bounded ideal reachable states are primitive conditions; the desired numerical error is derived, not a model assumption. Bounded reachability itself is not algorithmically decided here.
- Every dyadic datum has a supplied bounded-length finite description. A compact external generator is not supplied for free. Its time, program, data expansion and peak scratch must be added, or the explicit-table implementation selected.
- Position-dependent Q/K/V is compatible with the one-pass projections. Edge-dependent **bias/scale** is compatible with the row stream. Edge-dependent Q/K/V is expressly excluded and cannot be smuggled into this execution schedule.
- A nonempty causal public mask is enough for the numerical result. CA001 v3's statistical conclusion additionally needs fixed density, source-law/source-symbol independence, and branch independence. The numerical result does not prove sparse-mask CA001.
- Boundary branches must satisfy every bound on every formal history, including histories inconsistent with the frozen boundary label. This exactly matches CA001 v3 §7 and supports simultaneous branchwise comparison before actual-label selection; it does not condition IID inputs on their endpoints.
- Fixed-radius causal preprocessing is a fully paid finite table. It is not permission for interleaved singleton attention. A synthetic initial token remains fixed within each branch.
- The terminal decoder receives only the final cut and allowed finite label, with public metadata; neither residual arrays nor a clean accumulator nor raw-history rereading is granted.
- Positive-epsilon layer normalization, non-ReLU nonlinearities, arbitrary Lipschitz real maps and real exp/log oracles remain outside this certificate. No special SRC score cache, logarithm construction, network size or reconstruction algorithm is imported.

## 2. Signed conversion and affine microsteps

For signed integer `u` and denominator exponent `e`, conversion is `floor(u*2^(P-e))`. If `e<=P`, its shifted numerator has at most `b+P+O(1)` bits. If `e>P`, compare `e-P` to the numerator's bitlength before shifting. A larger exponent gives quotient zero for positive numerators and minus one for negative nonzero numerators; equality has the same rule because the magnitude is strictly below `2^bitlength`. Otherwise only existing numerator bits are inspected. Thus even a binary-encoded exponent of enormous numerical value does not force an enormous zero array. The stated conservative quadratic conversion work and linear scratch in `b+P` suffice.

The affine formula `DB+Σ AX`, then signed floor division by `D`, has the correct scaling. Expanding against the ideal affine map gives exactly the stated terms: ideal row norm times input discrepancy, at most `d ε (U+η)` from coefficient perturbations, bias conversion `<ε`, and final floor `<ε`. Negative values are neither clipped nor truncated toward zero. ReLU is exactly integer max. Fixed DAG induction supplies finite rational upper constants.

For internal DAG nodes whose discrepancy is larger than one, one must use the displayed general one-affine inequality and the already available bounded-node interval ranges, rather than reasserting a unit-discrepancy hypothesis at every internal node. This yields the same architecture-only linear constants. The layer-boundary unit neighborhood is what is bootstrapped.

## 3. Exponential inequalities, including odd indices

Rounded Q/K/V and scores on the entire input cube of radius `R+1` admit finite interval bounds using converted coefficient bounds. Selecting an integer `a` covering both ideal and rounded logits and all score intermediates does not clip data or assume numerical correctness. The exact shift gives `0<=S<=AD`, `A=2a`.

Each recurrence product `T_(j-1) S` is retained in full before division by the positive `jD`. Positivity and induction give `0<=T_j/D<=x^j/j!`. Consequently `D<=W<=HD`, where `H=3^A` is a computable integer and `exp(A)<3^A` is only a proof comparison.

Each of the `J` floors introduces less than ε. Its propagation into retained terms is bounded by `Σ A^r/[(k+1)...(k+r)] <= exp(A)<=H`, since the denominator is at least `r!`. Counting all introductions yields `HJ ε`, without an uncharged exponential operation.

For integer `j>=8A²`, the last `ceil(j/2)` factorial factors are each at least `j/2`; since `j/2>=1`, their product is at least `(j/2)^(j/2)` even for odd `j`. Thus `A^j/j! <= (2A²/j)^(j/2) <= 2^-j`. The omitted tail is bounded by the geometric sum `2^-J<=ε`. FA1 follows. FA2 follows from the mean-value bound `exp'<=H` on the entire segment between the shifted scores. No hidden-state interpolation is needed for this step.

## 4. Signed normalization and width audit

`N=Σ W_i V_i`, `Z=Σ W_i`, `O=floor(N/Z)` correctly returns a grid numerator. An extra division by D would be erroneous; the certificate does not make it. `Z>=mD` is proved by the constant Taylor term, independent of cancellation or key count. Signed floor contributes strictly less than ε in real units.

For the comparison of ideal values under two weight systems, use the finite denominator at least m. The numerator perturbation is at most `m V η_w`; the denominator perturbation multiplies an ideal weighted mean of magnitude at most V, hence another `m V η_w`. This proves the `2Vη_w` bound. Value error contributes at most `η_v` by convexity. Signed values are harmless. There is no factor m in FA3 or FA4.

Explicit magnitude envelopes: `T_j,W_i=O_arch(D)`; Taylor full products `O_arch(D²)`; `jD=O_arch((P+1)D)`; `V_i=O_arch(D)`; `Z=O_arch(nD)`; `|N|=O_arch(nD²)`. These require respectively `P+O_arch(1)`, `2P+O_arch(1)`, `P+log(P+1)+O_arch(1)`, and `2P+q+O_arch(1)` bits, with a sign bit where needed. Intermediate affine/score full products obey comparable bounds because fan-in is fixed. Long division remainders fit the divisor/trial-remainder envelope. Final multiplication by integer Q has at most `P+h+O_arch(1)<=2P+O_arch(1)` bits. The `w` definition covers them all. A b-bit parameter description is separately charged, not squeezed into w.

## 5. Bootstrap, precision and exact cut

The finite attention output stays in the convex hull of bounded rounded values up to one floor error. Together with the bounded ideal attention output, this justifies positionwise block constants without assuming rounded states lie in the ideal reachable set. The recurrence is valid whenever the **input layer-boundary** discrepancy is at most one. Defining all `C_l` and `C_out` by finite rational recursion and selecting their common upper bound is constructive.

The inequality `(4h+C+1)2^-3h <= C+5` holds for every integer h>=0. The prescribed finite search for `C_arch` therefore makes every layer and readout error at most `2^-h<=1`. Induction establishes the neighborhood premise before using it at the next layer. Constants do not depend on n or description length.

The exact signed final label is `floor(O_out/2^(P-h))` for powers of two, and `floor(Q O_out/D)` for general integer Q. The cut's **decoded value** is within `2/Q` of the ideal pre-cut value. Label equality is false at grid boundaries and is not asserted. With E=1, CA001 v3 §6 enlarges the old tube radius by one; for example its box factor can be replaced by `ceil(2τ+6)+1`. Bounded readout follows from bounded input states and fixed affine/ReLU primitive coefficients/biases, so output labels have `h+O_arch(1)` bits per coordinate, not necessarily exactly h bits.

## 6. Complete cost and sequential model audit

The accepted execution is the **compact-program sequential multitape evaluator**, not a hybrid of its space and a free-RAM time bound:

1. Retain/read the supplied ordered descriptions and public masks at actual input volume, bounded by `Ub+F`. Convert all U entries with signed arithmetic, using the separately charged `O(U(b+P)^2)` work and `O(b+P)` scratch. Use compact `P+O_arch(1)` public numerical slots; this resolves the storage interpretation noted above.
2. Local-table lookup scans an architecture-constant number of symbol/window entries per position. Boundary acquisition scans source symbols with counters. No random lookup or conditioning shortcut is needed.
3. Projection passes read hidden states and position-indexed coefficients sequentially. A fixed number of heads/branches/data kinds permits a fixed number of tapes or paid constant repetitions.
4. For every row, the key tape is scanned and rewound, costing `O(nw)` actual moves per row. Row-major masks and edge bias/scale records are forward streams. Full n-entry mask rows may be used and are charged. This proves `O(n²w)` movement, dominated by `O(n²(P+1)w²)` arithmetic. No weight matrix is retained.
5. Fixed-dimensional updates follow their sequential position records. Output is appended to a new rolling tape. Full rewinds, copies, clears and tape-head moves are included; public reformatting/sorting from another layout remains separately paid.
6. School arithmetic on a constant number of scratch tapes admits repeated scans in quadratic word length, including head motion. Counter operations fit the generous bound. Fixed arithmetic finite control does not need to reread an entire written `w^4` microcode object per bit operation. If that slower universal-interpreter design is selected, its extra time cannot be omitted.
7. Peak is the sum of all simultaneously live volumes, not merely the rolling `nw`: raw input, descriptions, converted data, masks, code, outputs, counters, arrays and conversion scratch. The displayed retained-data bound is sufficient for the compact public slot choice. Constant construction is architecture-only but still charged. A generator's possibly larger phase peak remains additional.
8. Logical access disabling/releasing suffices for the abstract terminal interface; paid zeroing is an alternative, not a magically free physical isolation device. Deleting source data from decoder access is not deleting its earlier resource cost.

If the pure compiled alternative is chosen, unroll the actual bit-machine computation (including tape access/control) and charge identity holds. `O(T)` depth, `O(S)` width, `O(TS)` gates/holds and `O(TS²)` dense slots are conservative valid upper bounds. Bit-level coefficient descriptions are finite and charged. These are **alternative** implementation costs, not a claim that all finite arithmetic is still a fixed-depth fixed-width neural layer. No computational superiority follows.

## 7. Independent diagnostics and provenance

`reviews/FA001_independent_checks_v2.py` is independently written and uses exact integers/Fraction, not the author's helper and not floating-point/Decimal exp. Its output is `reviews/FA001_independent_checks_v2.json`:

- 1,275 signed dyadic conversion checks, including exponent `2^4096` handled without constructing its denominator;
- 69 Taylor comparisons against rigorous rational lower/upper exp intervals;
- 300 odd/even factorial-tail checks;
- 30 signed normalization checks across key counts up to 257;
- precision/final-cut checks for 301 h values per constant, including `C_*=10^100`;
- an exact counterexample to label agreement (`ideal=1/4`, `actual=63/256`, `Q=4`).

All passed. These are finite diagnostics, not an exhaustive proof, runtime measurement or automatic membership test. The proof acceptance above rests on the reviewed inequalities and explicit execution schedule.

The actual CA001 v3 text was inspected, including §§6–7 and §9. The archived SRC proof's arithmetic/Taylor and interface/cost passages were inspected; it provides a pattern rather than acceptance of this expanded theorem. Source and artifact hashes are independently checked in the companion binding file. The canonical fact's recorded hash is verified without treating its identifier alone as proof acceptance.

**Final scope:** accepted constructive bridge and properly restricted CA001 E=1 transfer; no broader activation class, no arbitrary-source-network membership, no training or novelty claim, no free offline data, no free RAM, and no mixed hybrid/PURE accounting.
