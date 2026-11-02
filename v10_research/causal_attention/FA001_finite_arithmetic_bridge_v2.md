# FA001 v2 — Constructive finite-arithmetic bridge for a causal affine/ReLU subclass

2026-11-02. Version 2 preserves v1 and clarifies sequential-access costs, branch-independent masks and canonical SRC provenance. Author proof/certificate, not independent acceptance. Companion to CA001 v3 §6; does not edit or broaden CA001 silently.

## Result first

For the explicitly finite-data subclass below there is a deterministic integer evaluator whose final **pre-cut** vector satisfies, for every length and every formal history,

    ||F_fin-F_ideal||_infinity <= 2^-h = 1/Q,  Q=2^h, h>=0.

Its fractional precision is P=4h+C_arch. Accumulator length also pays log n; this is not an h-bit-everywhere implementation. All rounding sites, signed products, denominators, offline data, work and storage are specified below. Consequently CA001's final cut argument transfers with E=1, by enlarging its good-message tubes. This proves the bridge from primitive finite arithmetic; it is not assumed as a model condition. It proves neither training reachability nor a computational advantage nor membership of the whole SRC network.

## 1. Specified subclass and changes from CA001

Let n be total positions including a synthetic terminal token. Fix depth, heads, all vector dimensions, and the number of affine/ReLU operations in each positionwise block/readout. Use maximum coordinate norm. Q,K,V are affine maps; logits are their dot products, optionally with a bounded public additive bias and a bounded dyadic scale. Positionwise updates and readout are finite DAGs of affine maps, coordinate ReLU, residual sums and concatenation. Residual sums are affine operations. Fixed or position-dependent public Q/K/V, update and readout parameters are allowed; score bias/scale may also depend on the edge. All have common uniform magnitude/operator-norm bounds. Edge-dependent Q/K/V maps are not included in this version’s preprojected-array schedule. The number of operations along a per-position block is uniformly fixed. Ideal states at layer boundaries and initial states have norm <=R, uniformly for all histories, n,h and public parameter choices, for a declared constant R. This is an ideal reachable-state assumption, NOT a numerical approximation assumption. Intermediate ranges within the finite DAG follow from the primitive coefficient bounds and R, and are explicitly computed by interval bounds.

Every public number is given by a finite signed dyadic description (integer numerator and binary denominator exponent) of bitlength <=B_param. All such descriptions are supplied finite input/program data and counted. Norm bounds, R, and architecture sizes are fixed independently of n,h,B_param. Choose rational upper bounds for these constants, so subsequent integer constants can be constructed without real-number oracles. We do not claim a procedure that decides bounded reachability: the theorem is conditional on that primitive architecture property, as is CA001. Uniform bounded coefficients without a bound on their description length do not imply constant parameter storage.

Masks are public, source-independent, independent of the boundary branch label, causal and nonempty. The same mask is used for every frozen branch, as required by CA001 §9. For CA001 membership also require its fixed density |K_t|>=ct, with c>0. The numerical proof itself only needs nonempty masks. In particular it does not extend CA001's statistical proof to sparse masks. Mask storage or a specified generator is charged. Initial states are public dyadic finite tables of individual symbols or fixed-radius causal windows, with a fixed finite source alphabet; position dependence is allowed but its entire table is counted. The synthetic token table is fixed independently of history. Table selection is exact; selected coordinates are converted as below. Thus no arbitrary uncomputable initial map is hidden in this construction.

A fixed number of frozen boundary branches is permitted: each branch has its own finite-data tables and parameters; all the same bounds must hold on **every formal history with that branch fixed**, including inconsistent boundary symbols, exactly as CA001 §7. Read the actual finite boundary label once, select the branch, charge acquisition and retained label bits, and never give the decoder extra state except its explicitly granted label. All branches' stored data count unless a paid generator supplies them. The proof is uniform branchwise and needs no conditioning independence.

Excluded: epsilon=0 layernorm, arbitrary Lipschitz real maps with no evaluator, real exp/log primitives, noncomputable public parameters, unspecified table/generator costs. Even positive-epsilon layernorm is excluded from this version: its additional finite sqrt/division certificate is not asserted. This is a substantial strict subclass, not a replacement for CA001's ideal generality. Fixed local preprocessing here is a paid table, not unpaid singleton attention interleaved between layers.

## 2. Signed integer semantics and affine microsteps

Set D=2^P and epsilon=1/D. Store a real x as signed integer X representing X/D. Define rho_P(x)=floor(Dx)/D; for negative inputs floor is toward minus infinity, so |rho_P(x)-x|<epsilon. Implement signed floor division of a signed numerator by a positive integer using magnitude long division and the sign/remainder adjustment. Never clamp signed values to nonnegative. Parameter conversion uses the exact supplied dyadic numerator and shifts/division, returning rho_P(theta); it costs input bit reads and exact arithmetic on O(B_param+P) bits. Biases are converted too. This yields absolute coefficient error <epsilon. Denominator exponents are part of their descriptions; huge exponents need not allocate huge zero arrays: compare exponent to the available numerator length and determine the quotient/remainder sign, or shift only the relevant bits. A conventional numerator/denominator-bit representation is also legal and charged by its full length.

For affine y_j=b_j+sum_k a_jk x_k, form the exact signed integer

    N_j = D B_j + sum_k A_jk X_k,
    Y_j = floor(N_j/D).

All products and the entire sum retain their full precision before this single division. ReLU is exact integer max(0,Y_j). Additions may be performed exactly when already on the same grid; treating them as affine operations only makes the error bound looser. Initial table entries, each affine output, each logit after full dot product, every Taylor recurrence step, each attention output, and each affine readout output are the **only** truncation sites. Computing logits with a scale and bias uses the same finite sequence of affine/product-and-round instructions; no fused-product precision is silently discarded. Exact comparisons implement ReLU and signed floor corrections.

For any fixed affine DAG, compute a bound recursively: input discrepancy eta and input ideal bound U give a one-affine output discrepancy

    <= ||A||_infinity eta + d epsilon(U+eta) + epsilon + epsilon,

where d is fan-in, one epsilon is bias conversion and one is output floor. ReLU is globally 1-Lipschitz. Induction gives constants for the whole DAG on eta<=1; in particular an affine projection discrepancy <=k(eta+epsilon), with rounded projection magnitude bounded by a public constant. All constants below can be obtained by this elementary rational recursion and enlarged to integers. There is no assertion that the finite rounded map itself is Lipschitz.

## 3. Uniform neighborhood bounds and positive-shift exponential

Suppose layer-boundary discrepancy delta<=1. Rounded states then lie in the cube of radius R+1. Use affine interval bounds, converted-coefficient bounds |theta_fin|<=|theta|+1, and output-rounding bound <=1 to bound all rounded Q/K/V and rounded scores on this entire cube. Choose an integer a>=1 such that both rounded and ideal logits lie in [-a,a]. This is a coarse architecture-only constant computed from the primitive bounds, not an observed-data clipping rule. Enlarge it for any scaled-score intermediate operations. Put A=2a. The shifted finite score x=s_fin+a is an exact grid value in [0,A]; its integer S=Dx lies in [0,AD]. The same positive shift cancels in ideal softmax.

Set j0=ceil(8A^2)+2 and J=j0+P. Compute exact integers

    T_0=D,
    T_j=floor(T_(j-1) S/(jD)), j=1,...,J,
    W=sum_(j=0)^J T_j.

This is the SRC §4 integer Taylor recurrence, with a positive shift and a generalized fixed score range. It uses only exact products and positive-divisor integer division. Put w_hat=W/D. Induction proves 0<=T_j/D<=x^j/j! and 1<=w_hat<=exp(x)<=3^A=:H. Here exp is only a mathematical comparison function; H is a computable integer. The standard elementary series gives e<3.

Writing e_j=x^j/j!-T_j/D, we have 0<=e_j<=x e_(j-1)/j+epsilon. A truncation error introduced at step k contributes to the sum of all following term errors at most

    epsilon sum_(r>=0) A^r/[(k+1)...(k+r)] <= H epsilon.

Thus total retained-term error is <=HJ epsilon. For j>=8A^2, the last ceil(j/2) factors of j! give j!>=(j/2)^(j/2), hence A^j/j! <= (2A^2/j)^(j/2)<=2^-j. (For odd j the last factors only strengthen this inequality.) Therefore the omitted tail after J is <=sum_(j>J)2^-j=2^-J<=epsilon. We obtain

    0 <= exp(x)-w_hat <= (HJ+1)epsilon.                 (FA1)

Any ideal logit s_* in [-a,a] satisfies

    |w_hat-exp(s_*+a)| <= H|s_fin-s_*|+(HJ+1)epsilon.    (FA2)

The mean-value argument stays within [0,A]. No finite exp or log oracle is used.

## 4. Exact signed normalized sums: no key-count error

For m>=1 keys, finite value coordinate V_i represents v_hat_i=V_i/D, possibly negative. Accumulate exactly

    Z=sum_i W_i,       N=sum_i W_i V_i,
    O=floor(N/Z),      o_fin=O/D.

Thus N/Z is the grid numerator of the weighted mean. Do NOT divide by an additional D in O; the factor D is already in the value encoding. Products are full signed products and sums have log m guard bits. Z>=mD>0 because every W_i>=D. Final signed floor contributes <epsilon and cannot cause an illegal denominator. No cancellation assumption is needed.

Let w_i^*=exp(s_i^*+a), |v_i^*|<=V, and max_i |v_hat_i-v_i^*|<=eta_v, max_i |w_hat_i-w_i^*|<=eta_w. Both weight sums are >=m. Split value error first and compare the two weighted averages of the SAME ideal values. Their numerators differ by at most m V eta_w and their denominators by at most m eta_w. The identity for the difference of two ratios, using the ideal weighted-average magnitude <=V, gives

    |o_fin-o_*| <= epsilon+eta_v+2V eta_w.             (FA3)

This is independent of m, even with signed values. For dot-product scores, bounded Q/K imply by expanding the product difference that |s_fin-s_*|<=k_s(delta+epsilon), including converted scale/bias and logit rounding. Affine values similarly give eta_v<=k_v(delta+epsilon). Equations FA2–FA3 and J=j0+P yield computable architecture constants k1,k2 such that every head satisfies

    ||o_fin-o_*||_infinity <= k1 delta+k2(P+1)epsilon. (FA4)

No softmax denominator is bounded below by an unproved constant: its lower bound mD is built into the T_0 term.

## 5. Layerwise bootstrap and actual pre-cut theorem

On the bounded ideal and rounded attention-output ranges (convex averages of bounded values, followed by <epsilon rounding), apply the affine/ReLU DAG recursion of §2 to the residual/feed-forward block. Combining its finitely many heads with FA4 gives computable nonnegative constants alpha,beta, common to all layers,

    delta_(l+1) <= alpha delta_l+beta(P+1)epsilon,

provided delta_l<=1. Initial conversion gives delta_0<=epsilon. Let C_0=1 and C_(l+1)=alpha C_l+beta. Then delta_l<=C_l(P+1)epsilon as long as the induction remains in the neighborhood. The readout recursion gives likewise error <=C_out(P+1)epsilon. Choose a rational integer upper bound C_*>=1 on all C_l and C_out. In constructing these constants the actual block outputs may lie outside the ideal reachable set; all local error estimates used the R+1 input cube and global affine/ReLU bounds, not an assumed rounded-state reachability property.

Choose a fixed integer C_arch>=1 by finite search until

    C_* (C_arch+5) 2^-C_arch <= 1.

Such an integer exists. For h>=0, P=4h+C_arch, and

    (P+1) 2^-P / 2^-h
      =(4h+C_arch+1)2^(-3h-C_arch)
      <=(C_arch+5)2^-C_arch.

Consequently C_*(P+1)epsilon<=2^-h<=1. Induct from l=0: each layer stays within discrepancy <=1, legitimizing precisely the next neighborhood estimate. This closes the bootstrap without assuming its conclusion. The readout obeys the stated <=1/Q uniform bound. The constants depend only on fixed architecture, coefficient/range bounds, and fixed local/branch parameters, NOT n,h,B_param or the selected history. For arbitrary integer Q>=1 take h=ceil(log2 Q); then 2^-h<=1/Q, and the same transfer holds with the final cut at resolution Q.

For Q=2^h, the final integer cut label is exactly floor(O_out/2^(P-h)), since P>=h. Its distance from ideal pre-cut output is <=2/Q, but equality with the ideal rounded label is NOT promised: arbitrarily small perturbations can cross a grid boundary. CA001's tube proof, rather than label equality or Lipschitzness of rounding, is the valid transfer. Integer Q uses the full product Q O_out before division by D. The output has h+O_arch(1) bits per coordinate because bounded ideal states/readout and the <=1 error imply a fixed output range.

## 6. Complete constructive cost ledger (one explicit conservative implementation)

Let b=B_param, q=ceil(log2(n+1)), U be the number of supplied numerical scalars across all branches, local/position tables and edge biases, and F be mask/other explicit public-data bitlength. U and F count the actual selected sequential layout, including any duplicated numerical records and padded mask cells described in §6.1; if a compact supplied format is expanded, charge the additional format generation/writes and use these expanded counts in storage bounds. The fixed architecture factors are suppressed in O_arch. Use

    w=O_arch(P+q+log(P+1))

bits per online signed word; this includes sign, integer range, full products (up to 2P+q+O_arch(1) bits), all summation guards, jD divisors, long-division remainders, counters and addresses within the online arrays. Parameter descriptions and converting scratch use O(b+P), separately. No claim packs a b-bit description into w bits. Addresses to U/F-sized public-data arrays cost additionally log(U+F+2); include that in w if it is larger. With explicit fixed-width architecture tables U=O_arch(n^2), F=O_arch(n^2+nq), it is already absorbed in q plus input-description lengths.

- **Public-data acquisition/offline:** read/store Ub+F bits, including mask cells, local/position tables, all branches, biases and parameter descriptions; observed alphabet symbols cost O(n) bits for fixed alphabet (or their actual encoding). Constructing those data from some external generator is NOT free: add its actual time, program and peak scratch. Our executable option is a supplied explicit finite table, whose reading/copying is counted. Arbitrary undocumented generation complexity is not claimed bounded by Ub+F.
- **Parameter conversion:** U exact conversions, conservative O(U(b+P)^2) bitwork and O(b+P) reusable scratch, plus UP converted storage bits. Copies/format writes are included. If original descriptions remain live, they remain in peak. Constant construction of j0,H,C_arch and rational bounds is finite architecture-only offline work/storage; it is charged, albeit independent of n,h. Reading h and allocating output layouts is charged.
- **Online arithmetic:** school signed addition/comparison O(w), full multiplication and long division O(w^2). A score/value projection has fixed fan-in. Per scanned edge, J=O_arch(P+1) Taylor steps cost O_arch((P+1)w^2); signed value products and exact accumulations cost O_arch(w^2). Scan every causal edge, checking the mask, even if absent: at most O_arch(n^2(P+1)w^2) bitwork, including all row quotients, fixed affine/ReLU blocks/QKV on all n tokens, mask reads, loop/copy/clear overhead, input lookup, boundary acquisition, and final cut conversion. This bound uses the sequential multi-tape execution schedule specified immediately below; no constant-time arbitrary-address RAM or free wired-array addressing is assumed. Data-dependent table lookup can scan the fixed-alphabet local table and select by comparisons, at O_arch(1) words per position. Arbitrary sparse runtime claims are not made.
- **Numerical workspace:** two rolling hidden arrays and projected QKV arrays O_arch(nw) bits, O_arch(w) row accumulators and Taylor/division scratch; no n^2 numerical attention-weight matrix. Values and weights are consumed rowwise. Signed weighted-sum accumulators remain full width. Masks and public parameter tables are stored separately, not hidden in this rolling bound.
- **Program/control:** fixed-loop finite arithmetic templates plus public counters can use a conservative O_arch(w^4) stored bits, construction/write work O_arch(w^4); this deliberately loose allowance pays bit-arithmetic microcode rather than assuming a free interpreter. Alternatively hardwire the full instruction schedule; charge its O(T w) addressed records rather than this compact code. Online bound above is for the explicit finite-loop evaluator, not generic dense scalar neural evaluation. The selected implementation is a fixed-control multi-tape bit machine with the sequential access schedule below. Arithmetic routines are explicit repeated scans on O(w)-bit scratch tapes; grade-school multiplication/division cost O(w²), including tape-head moves. Constant finite control and a conservatively bounded written microcode description are charged; the w^4 description is NOT scanned in full before each bit operation. A universal interpreter with that behavior would have additional time cost. No direct-access fetch from the stored public arrays is assumed.
- **Peak memory:** take the maximum, over construction/conversion/forward phases, of the SUM of all simultaneously live input, descriptions, converted data, masks/metadata, code, output, controller and working arrays. A safe retained-data bound is O_arch(Ub+UP+F+n+nw+w^4+b+P), not merely O(nw). Offline generator scratch, if any, adds at its actual phase. Releasing descriptions after conversion lowers forward peak but not their earlier peak.
- **Terminal interface:** finish readout, produce the cut vector and allowed boundary label, then disable decoder access to history, QKV, accumulators and residuals. Release dead arrays or explicitly zero them (O_arch(nw+UP) writes if zeroed); public model/masks carry no source information. No stale clean sum, hidden state or raw-input port is granted. A physical isolation/injection device is not supplied by this abstract access convention and needs separate charges if requested.

### 6.1 Sequential access schedule underlying the compact-program bound

Use a fixed number of sequential bit tapes (architecture/branch count is fixed), with explicit left/right head motion costing one operation per crossed bit. Each numerical record has a fixed O_arch(w)-bit slot including padding. Supplied data are in the declared order: branch-major, layer/head-major, then position order for Q/K/V and update parameters, and row-major (t,i) order for masks and score bias/scale. Input formats that are not in this order require a separately charged sorting/reformatting phase; this certificate does not assume free permutation. A one-time sequential copy can separate these finitely many data types onto tapes, costing their full description and converted-data lengths. Rewinds of each such tape also cost its length. Fixed branch count permits either separate tapes or scans past unselected branches, with the same asymptotic paid volume. Duplicated tapes/records count in stored data; only a fixed multiplicative duplication is needed here.

1. Scan input symbols sequentially. A fixed-radius window is maintained in a fixed-size shift register; for each position scan its entire fixed-alphabet local table, selecting the matching entry by exact comparisons/muxes. Each position's table has architecture-constant entry count. Acquire the finitely many boundary symbols with counters during this or an additional full scan, costing O_arch(nw) tape work; freeze the selected branch before evaluation. Append the synthetic initial state and write the initial hidden-state tape in position order. Public tables/parameters may all be converted sequentially, with the §6 conversion cost and retained-data storage, rather than pretending an input-dependent branch magically discards acquisition costs.
2. At each layer, scan the hidden-state tape and position-ordered Q/K/V parameter tapes in parallel. Compute each projected record and append it to separate Q and K/V tapes (and, if useful, a constant number of copies for the fixed heads). Keep a sequential hidden-state copy for residual updates. The projection pass and its rewinds cost O_arch(nw²) arithmetic plus O_arch(nw) movement. Shared position-independent matrices are loaded into a fixed number of scratch words, or duplicated as position records with their O_arch(nP) writes/storage counted.
3. For row t, read the next query and residual-state records from their forward-moving tapes; hold these O_arch(w) bits in scratch. Scan the K/V tape from its beginning, either through the causal prefix or through the full n positions while skipping i>t. Stream the corresponding row-major mask and edge bias/scale records on their own forward-moving tape. The mask stream can use complete n-entry rows with zeros beyond t; that representation costs O_arch(n²) bits. Compute each permitted score, Taylor weight and exact signed numerator/denominator update in the O_arch(w)-bit arithmetic scratch. Advance records by actual bit moves. After the scan, rewind K/V to its beginning by at most O_arch(nw) bit moves. Thus all key scans AND rewinds across all rows cost O_arch(n²w), below the stated arithmetic bound. Edge data are read only sequentially, O_arch(n²w) converted bits in total. No numerical attention matrix is retained. A fixed number of heads is processed with a fixed number of tapes or repeated full passes, both covered by architecture constants.
4. Divide the row accumulators, apply that row's residual/feed-forward block using the next sequential update-parameter records, and append its output to the next hidden-state tape. Reset scratch by explicit writes O_arch(w) per row. At layer end, rewind the completed output and the necessary public tapes; overwrite/reuse the now-dead old hidden/Q/K/V tapes in the next layer. These full-array motions cost O_arch(nw+n²w) per fixed layer, including row-major public edge streams. Readout and final cut conversion are sequential on the terminal record. Public tape copies and both rolling layer tapes are already included in the data/workspace sums.

Numerical scratch arithmetic uses fixed-width bit scans and public loop counts, with conditional results selected by exact Boolean operations; sign corrections and ReLU comparisons require no random access. Loop-counter updates and position tests take O(w) per relevant loop iteration and fit the O_arch(n²(P+1)w²) allowance. Tape construction, conversion, format writing and resets are never omitted. This is an explicit compact-program sequential model; choosing an addressed unrolled program instead requires its separately stated O(Tw) records and storage. The two descriptions are alternatives, not selectively combined coordinates.

The ledger is a bit/register construction, not an assertion that arithmetic expansion preserves fixed neural depth/width. If a pure ReLU/Boolean compiled network is desired, unroll T actual bit operations with S live bits, use constant-size exact Boolean/ReLU gadgets and paid identity holds: a conservative depth O(T), width O(S), O(TS) gates/holds and O(TS^2) dense slots, each finite coefficient's bitlength paid. Retaining all layers or training is additional storage. No complexity comparison follows from this upper bound.

## 7. Diagnostics, provenance and limits

`check_fa001.py` uses exact Python integers/Fraction to check the recurrence, signed normalization, precision choice and a small two-layer causal affine/ReLU network against high-precision Decimal exp. Its JSON is diagnostic evidence, not a proof and not exhaustive architecture membership certification. Tests include negative values, denominator legality, varying key counts, public dense masks, and finite branches/parameter choices. No measured generic-machine timings stand in for the bit ledger.

Canonical SRC fact: `v10_intake/source/sources/euler-stage6/facts/fef8372728290b45.md`. The root GW reconciliation identifies its English proof body with the archived SRC proof below up to a trailing blank line; both files are hash-bound, without treating the fact identifier alone as proof acceptance.

Source: CA001 v3 §§1,6,7,9 defines the ideal target and transfer obligation; SRC-Pi `cloud_work/conditions-20261028/handoff/DOT_CONDITIONS_20261028/sources/euler/SRC-proof.md` §4 supplies the integer Taylor/full-product/division pattern and §§9–10 motivate explicit guard/storage/phase and hybrid/PURE distinctions. FA001 extends that pattern to general bounded signed affine values, signed hidden-state rounding, shifted bounded logits and repeated layers. SRC's special five-score cache, log constants, positive statistical-bank algebra and architecture sizes are NOT imported. No external literature priority claim is made.

Open limits: constants may be very large; this is existence with explicit constructive dependence, not practical precision optimization. No training theorem, no optimality, no superiority to equally informed direct baselines, no certification of an arbitrary old emitter. Independent mathematical and interface review remain required.
