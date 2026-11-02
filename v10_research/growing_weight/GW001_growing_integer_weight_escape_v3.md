# GW001 — Costed escape by length-growing effective logits

2026-11-02. Author candidate v3, narrow implementation/provenance revision after independent acceptance of v2; revision review pending. This changes the finite attention weight rule, not merely the decoder. No novelty, computational advantage, or ordinary finite exponential-evaluator equivalence is claimed. BF001 v2 is contextual only and is not a proof dependency.

## 1. Result, experiment, and changed conditions

Let K>=2, M>=1, N=M+2, n=N+1=M+3, h>=4 an integer, Q=2^h. Observe X_1,...,X_N from a homogeneous second-order source with unknown transition rows theta and arbitrary unknown initial pair distribution. Put Y_j=(X_(j+1),X_(j+2)), j=0,...,M. The prediction target is theta_(Y_M). For every beta in [0,1], the optional D2(beta) restriction is the existence of stationary Pi with P²(s,t)>=beta Pi(t) for all pair states, including unsupported states. Our predictor does not read beta, Pi, or theta.

There is a single deterministic finite causal program G_(K,M,h), with two paid singleton local-copy heads and one K-coordinate dense statistical head, whose risk satisfies simultaneously for every beta

    E TV(G,theta_(Y_M))
      <= min(1, 2^13 Hstat + Psi((2K+1)K^4/(M+1)) + (K-1)/Q)              (GW1)
      <= min(1, [2^13 K^(5/2)+2K²sqrt(2K+1)]/sqrt(M+1) + (K-1)/Q).             (GW2)

Here Psi(0)=0, Psi(x)=x(1+ln(1/x)) on 0<x<1, and Psi(x)=1 on x>=1. With delta=1-beta and rate horizon v=M+1,

    a=min(1,sqrt(K³/v)), g=min(1,sqrt(K⁵/v)),
    hstar=min(1,sqrt(K⁴/v)),
    Hstat=max(a,delta^v g,delta^(M/2) hstar).

These are R011's exact ORIGINAL scales; Hstat<=g. The only non-elementary statistical dependency of GW1 is the accepted R011 original-add-one risk upper. The terminal occupation lemma used below is re-proved here. All deterministic implementation assertions are proved here, independently of R011.

The actual weight rule is the public integer cache

    W=M,                 cache=(1,W,W²),
    m_i=1{X_(i-2)=a_query}+1{X_(i-1)=b_query},
    weight_i=W^(m_i).

It has weight range [1,M²], NOT a range bounded uniformly in M. Its mathematical softmax-equivalent natural logit is m_i ln W, with effective range [0,2 ln W]. Calling m_i a small score code does not make these bounded natural logits. The code-to-weight evaluator has changed. Neither log nor exp is executed: W is a copy of M, and W² an exact integer product. This is not SRC's truncated-exponential recurrence, cached or uncached.

BA001 assumes fixed D,r,a,b, actual weights in fixed [a,b], bounded values, one dense local summary block, and no historical decoder reread. G preserves the latter restrictions with D=K and r=3, but violates precisely fixed weight dynamic range (equivalently its effective logit range grows with M). Singleton preprocessing is limited to local shifts, and terminal query acquisition uses these same paid heads. No interior exact side statistic is exposed. Its decoder can be viewed inside BA001's otherwise stronger boundary-side contract, but not inside its fixed-weight encoder family.

## 2. Complete causal program and cut

Use observed input one-hots x_t=e_(X_t), t<=N, and synthetic token x_n=0. Public positions and masks are finite stored bits. No unobserved next symbol is input. First layer: two zero-query/zero-key singleton heads, each with value projection x, select respectively t-1 and t-2 when available, otherwise self. Their weights are exactly one, their returned bit vectors exact even on the Q-grid. Preserve x_t by an explicit copy. Thus for t>=3, l1_t=x_(t-1), l2_t=x_(t-2), including at t=n.

Second layer: one statistical head with query (l2_t,l1_t), key (l2_i,l1_i), value x_i. Its unscaled exact dot product is the integer code m_(t,i) in {0,1,2}. The weight selector returns cache[m]. For t>=3 the public causal allowed keys are 3,...,min(t,N). For t=1,2 use self fallback. Thus every row is nonempty, every allowed value is one-hot, and at terminal t=n the allowed keys are exactly all M positions 3,...,N. These are public position masks, not query-selective masks. Maximum QK dimension is 2K; value dimension K. The two preprocessing heads can run together, followed by the statistical head: total three physical heads, at most two per layer.

For every row compute exact integers

    D_t=sum_allowed weight_(t,i),
    A_(t,c)=sum_allowed weight_(t,i) x_(i,c),
    z_(t,c)=floor(Q A_(t,c)/D_t), c=0,...,K-1.

All sums and divisions are exact integers; returned scalars are z_(t,c)/Q. Carry out the decoder tokenwise at all n rows, not only the terminal row:

    u_(t,c)=z_(t,c) for c<K-1,
    u_(t,K-1)=Q-sum_(c<K-1) z_(t,c),
    G_(t,c)=u_(t,c)/Q.

Since sum_c A_(t,c)=D_t>0, all output coordinates are nonnegative, the last residual is in [0,Q], and they sum to Q. Closed endpoint z=Q is allowed and requires h+1 unsigned bits. Only G_n is the requested output; storing all row outputs is nevertheless charged. The final residual replaces the last returned scalar; no extra head is required.

Cut contract: after the statistical stage, terminal decoder reads only its K grid scalars and public K,Q. It does not receive D_n, A_n, W-weight sums, m codes, exact empirical counts, other token outputs, or historical residuals. Such buffers are internal attention workspace only. The full batch program can physically retain arrays while finishing other rows, but there is no decoder edge from them; they are explicitly cleared/released after use. Thus this is not an output-grid-only estimator disguised as an attention interface.

## 3. Deterministic accuracy on every history

Write s=(X_(N-1),X_N), J=sum_(i=3)^N 1{(X_(i-2),X_(i-1))=s}, and C_c for the matching triples with successor c. These are proof quantities, not runtime inputs. Let B_c=A_(n,c)/D_n be the exact real comparison ratio, and q_c=(C_c+1)/(J+K) the original add-one predictor.

If J>=1, matching total weight is J W². Every nonmatch has m<=1 and weight<=W, so its total R<= (M-J)W<=MW. If R>0 let r be the normalized nonmatch successor law. Then

    B=(J W²/(J W²+R))(C/J)+(R/(J W²+R))r,
    TV(B,C/J)<=R/(J W²+R)<=M/(WJ)=1/J.

For R=0 the same bound holds with B=C/J, without defining r. Also

    q=(J/(J+K))(C/J)+(K/(J+K))Uniform_K,
    TV(C/J,q)<=K/(J+K).

For J>=1, 1/J<=(K+1)/(J+K), because J+K<=(K+1)J. For J=0, both B and q are simplex vectors and their distance is at most one, also bounded by (2K+1)/(J+K). Therefore for every history

    TV(B,q)<=min(1,(2K+1)/(J+K)).                           (3.1)

The cap includes the empty-row case; no separate P(J=0) term is required. This bound uses no runtime empty-row test.

For c<K-1 let e_c=B_c-floor(QB_c)/Q in [0,1/Q). The residual output has last-coordinate error sum_(c<K-1)e_c. Therefore

    TV(G_n,B)=sum_(c<K-1)e_c <=(K-1)/Q,
    TV(G_n,q)<=min(1,(2K+1)/(J+K))+(K-1)/Q.                 (3.2)

This proof does not condition the source on the terminal query and does not claim successor independence given J.

## 4. Occupation control and risk proof

For any homogeneous Markov chain on d states, let J_m count visits before time m to its terminal state. Fix integer w>=1 and let b_m(y)=P_y(J_m<w), B_m=max_y b_m(y). The complete counts dominate counts in a suffix of l steps, so conditioning only on the suffix starting state gives B_m<=B_l for m>=l. For any deterministic path, at most the first w occurrences of each state satisfy J_t<w; consequently sum_(t=0)^m 1{J_t<w}<=dw. Taking expectations for every starting state and using max<=sum yields

    sum_(t=0)^m B_t <= sum_y sum_(t=0)^m b_t(y) <= d²w.

Monotonicity gives (m+1)B_m<=d²w. Arbitrary starting distributions obey the same bound by convexity. Taking d=K²,m=M proves

    P(J<w)<=min(1,K^4 w/(M+1))                              (UC)

at the actual random terminal pair, without stationarity or mixing.

For any A>0 let V=min(1,A/(J+K)) and c=K^4/(M+1). For 0<t<1, V>t iff J<A/t-K. If this threshold is positive, put w=ceil(A/t-K); for integer J the event is exactly J<w and w<=A/t because K>=1. If nonpositive the event is empty. Thus P(V>t)<=min(1,cA/t). Integrating t in (0,1) gives E V<=Psi(cA). Taking A=2K+1 gives the numerical term of GW1. UC separately gives P(J=0)<=min(1,K^4/(M+1)), but this is not needed.

Triangle inequality, (3.2), and accepted R011 ORIGINAL give GW1, followed by the independent unit loss cap. Since a,hstar<=g and delta powers<=1, Hstat<=g<=K^(5/2)/sqrt(M+1). Finally Psi(x)<=2sqrt(x): for x>=1 this is immediate; for x=e^-u in (0,1), Psi(x)/sqrt(x)=e^(-u/2)(1+u), whose maximum for u>=0 occurs at u=1 and is 2/sqrt(e)<2. This proves GW2, all beta and arbitrary starts.

For fixed K a fully integer public precision choice is

    h=max(4,ceil(bitlength(M+1)/2)), Q=2^h.

It ensures Q>=sqrt(M+1), giving risk <=[2^13 K^(5/2)+2K²sqrt(2K+1)+K-1]/sqrt(M+1), capped at one. Thus h=0.5log2(M+1)+O(1) suffices, with no added loglog M in grid precision. The effective natural-logit range is exactly 2 ln M, independent of Q (zero when M=1). It pays for the escape even when precision is selected independently. Arithmetic word length still includes log M. No near-IID K-sharp common-minimax claim is made: the statistical comparison uses original q, not R011's adaptive ALG.

### 4.1 Optional larger range for stronger all-history approximation

The initial route W=M Q is also valid, but unnecessary for the primary risk order. In that variant, TV(B,C/J)<=1/(QJ)<=1/Q for J>=1, and the empty-row cap is already covered by K/(J+K). Therefore

    TV(G_n,q)<=K/(J+K)+K/Q,
    risk<=min(1,2^13 Hstat+Psi(K^5/(M+1))+K/Q).

Its effective logit range is 2 ln(MQ), becoming 3 ln M+O(1) at the displayed half-log grid schedule. It pays more range for uniform approximation on nonempty rows rather than occupation-averaged control. Cache generation adds an h-place shift; the dividend bound changes from M³Q to M³Q³, still within the same b below. Neither route implements logs or exponentials, and neither is asserted optimal. A more general W=M A for a public positive integer A has nonempty leakage <=1/(AJ); the same proof gives risk <=2^13 Hstat+Psi([K+(K+1)/A]K^4/(M+1))+(K-1)/Q, capped at one. This generalization is an analysis tradeoff, not a claim of a matching necessary logit budget. For arbitrary A beyond the two costed choices A=1,Q, the ledger must replace b by a sufficient multiple of h+ell+log2(A+1)+1; no arbitrary-A cache is hidden inside the original word bound.

## 5. Finite ranges and a complete conservative execution ledger

This section gives a deliberately conservative addressed Boolean bitprogram realization and a separate PURE expansion. It does not assert SRC's small batch-hybrid neural depth for a changed evaluator. All hidden constants below are absolute.

Set ell=ceil(log2(n+K+2)) and b=64(h+ell+1). Persistent integer payloads use b-bit words. Arithmetic temporaries use explicitly allocated constant-multiple-b words: an arbitrary b-by-b multiplication retains its full 2b-bit product, with sign and accumulation guards as needed (a safe uniform allocation is 4b+4 bits). Wider temporary arithmetic is implemented at that actual width, not truncated to b. All word, gate, storage, and addressing bounds below use O(b) to include these fixed factors. Coefficients 0,1 and final dyadics 2^-j are exactly represented using O(b) bits. Online values satisfy

    W=M, W²=M²,
    D_t,A_(t,c)<= M W² for t>=3,
    D_t,A_(t,c)<=W² for fallback rows,
    Q A_(t,c)<=Q M W²=M³2^h.

Since M>=1, the same MW² bound covers fallback rows. The dividend uses at most 3ceil(log2(M+1))+h+1 bits. School multiplication retains full double-length products in the separately allocated temporary words. Shifted division remainders and signed/accumulation guards fit the stated constant-multiple-b allowance; no claim is made that an arbitrary b-by-b product fits b bits. The sum of at most K output-grid numerators is bounded by KQ even before using the sharper simplex invariant, fitting h+ceil(log2(K+1))+1 bits. Dense QKV intermediates can conservatively sum O(K) b-bit products whose actual small values are bounded by O(K), needing only O(log K) guards; b was chosen generously. Controllers and addresses for the polynomial-size arrays/program below use O(b) bits, since log b=O(b).

Arithmetic implementation: ripple add/subtract/compare uses O(b) Boolean gates and O(b) scratch. School multiply and restoring long division with O(b) fixed steps at the actual allocated O(b)-bit width use O(b²) gates and O(b) recycled scratch. Division by D>0 is exact; all loops are fixed bound, with muxes replacing data-dependent branches. Cache lookup over three possibilities is a b-bit mux, not a real-number table oracle. Bit AND/NOT/XOR and muxes have bounded fan-in Boolean circuits. Copies and zeroing are explicit gates/writes.

Choose the following one fully paid schedule, rather than mixing sparse runtime with dense storage:

* Store all three n-by-n public masks, n O(ell)-bit positions, public layouts/counters, and one-hot observed input plus synthetic zero. Mask storage is O(n²+n ell), input storage O(NK); offline writes and acquisition copies count.
* Store all front-end projection matrices including zero slots, with O(K²) entries of O(b) bits. Evaluate those dense maps at every one of n tokens using generic school arithmetic: O(nK²b²) gates. Two singleton heads scan their public rows rather than obtaining free indexed copies. Score/value projections, original x residual copies, two local copied arrays, statistical Q/K/V arrays and row-output arrays occupy O(nKb) bits. Zero Q/K maps and singleton masks are still paid.
* For each of three heads scan all n² candidate edges (masked edges included). At each dense statistical edge, compute the 2K-term dot code with O(Kb²) generic work, select the cache weight, and execute all K numerator updates and the denominator update masked by the public edge bit. Singleton-head normalized copying is implemented by the same exact accumulate/divide machinery. There are O(n²Kb²) gates total; no numerical n² weight matrix is retained.
* Each row has a (K+1)-word numerator/denominator bank, cleared before use; edge scratch is recycled. Normalize all K coordinates using exact floor division, and run the residual decoder at every row: O(nKb²) gates. Account for all copies, shifts, cleared word writes, row bank lifetimes, input and output serialization, and public counter updates. Mask/position construction and scan-control work O(n²b²) is within the displayed bounds.
* Cache generation is public: write 1, copy M, square using a school product. Cost O(b²) gates, O(b) scratch and cache storage, no finite logarithm generation. The cache is generated once and retained across rows. No uncharged source-dependent offline data are used.

Consequently the straight-line arithmetic/control circuit has

    T0 = O(n² K² b²) elementary Boolean instructions,       (5.1)
    S  = O(n²+nKb+K²b+b²) simultaneous packed data bits.    (5.2)

T0 intentionally overbounds the sharper attention-plus-projection sum; it includes initialization, copies, clears and all-token output. S includes input, masks, positions, matrices, projected arrays, cache, numerator/denominator bank, all row outputs, controller/address state and arithmetic scratch. It is not only rolling scratch. Local-copy and statistical stages release obsolete buffers explicitly; counting them together in S is conservative.

To avoid a free random-access machine, store the unrolled instructions with explicit operand/destination bit addresses and opcode: each uses O(b) bits and total program P=O(T0 b). One concrete sequential evaluator scans its entire S-bit data tape for each instruction's O(1) accesses, comparing O(b)-bit addresses, and writes the destination in another scan. Its evaluation cost is

    Tserial=O(T0 S b), working bits S+O(b),
    stored program O(T0 b), total forward peak O(T0 b+S).   (5.3)

Instruction stream reading adds O(T0 b) already covered. The fixed tape scanning/control algorithm has finite O(b²) microcode/table storage and O(b²) scratch, charged within P+S; there is no unit-cost addressing assumption. Alternatively the known-address circuit may be wired directly and use T0 gate operations, but then its wires/holds must be charged as below; we do not identify that gate-operation count with the tape evaluator's runtime.

Offline construction runs fixed loops in K,M,h, expands school arithmetic and mask/control circuits, assigns known wire/bit addresses, generates cache and matrices, and writes every instruction, mask, position and zero coefficient. A conservative bound is

    offline bitwork O(T0 b²+S b²),
    offline peak O(T0 b+S+b²).                             (5.4)

This follows by sequentially emitting O(T0) records with O(b)-bit addresses using school arithmetic (O(b²) per record), plus scanning/generating each of S data locations with the same allowance. No sorting is necessary: records are emitted in execution order. Public K,M,h are given in binary, and any input one-hot conversion from packed symbols is a separate O(NKb²)-work O(NK+ell)-space scan, already absorbable in these generous bounds if selected. The declared input convention is one-hot; no input-conversion saving is presumed.

The total peak is the maximum over offline and forward phase sums, including retained program, input, masks, matrices/cache, outputs, working arrays and controller, not the rolling-bank entry alone. The bounds (5.3)-(5.4) deliberately allow generated data to coexist. If all output rows are exported rather than only the terminal K words, their O(nK(h+1)) serialization is charged and fits; the specified answer is one row. Asking for all K² arbitrary external queries would be additional work, not provided here.

## 6. Separate PURE Boolean/ReLU expansion

One can instead unroll the T0 known-address Boolean instructions, retain all other live bits by explicit identity holds, and implement every Boolean instruction by constant-size exact ReLU bit gadgets: AND(x,y)=ReLU(x+y-1), NOT(x)=1-x, and OR(x,y)=x+y-AND(x,y); XOR and mux follow from these. All their inputs/outputs are exactly bits. Ripple arithmetic was already compiled into these operations. Gates are globally hardwired to their known addresses: no RAM oracle remains. A final finite dyadic linear map decodes the h+1 output bits; coefficients have O(b)-bit exact representations.

Writing T=T0+b, S'=S+b, safe bounds are

    depth O(T), width O(S'),
    sparse gate/hold records O(T S'),
    addressed sparse coefficient/wiring bits O(b T S'),
    dense coefficient bits O(b T (S')²),
    generic dense forward bitwork O(b² T (S')²),
    two scalar-neural rolling layers O(b S') bits.

Every inactive dense zero slot and every identity hold is included. Offline writes/generation cost at most O(b² T(S')²) in dense format (or O(b² T S') in addressed sparse format), with the chosen file plus input/public constants, outputs and generation scratch counted in that phase's peak. Forward peak adds the chosen stored parameters, input/masks/public constants if separately retained, rolling arrays and output; storing constants both as parameter rails and data is permitted only with both charged. T0's causal data dependencies are preserved: outputs at t depend only on observations <=t, and the synthetic terminal row on observations <=N. The overall bit circuit may schedule work globally, but never gives a row a future data dependency.

This PURE implementation has no attention oracle remaining. The abstract finite attention program has three heads; the flattened Boolean/ReLU network should not be described as a three-ordinary-softmax-head Transformer with SRC's old depth/width. (5.3) and this expansion are alternative complete implementations, not coordinates to mix into an artificial best-of-both ledger.

## 7. Boundaries and interpretation

1. Dense positive weighting is retained; no query-dependent hard mask, growing value range, nonlocal key feature, or exact count port is needed. Effective logit growth is the declared escape.
2. Statistical h can be half-logarithmic without the weak-mixing loglog surcharge. Total arithmetic precision and effective natural-logit range remain logarithmic in history length. There is no fixed-total-resource statement.
3. This does not refute BA001 or pending BF001. Their uniform constants require a fixed actual weight interval, whereas the primary W=M construction has b/a=M²; only the optional W=MQ variant has b/a=M²Q². Plugging this into their constants does not yield a fixed-family lower.
4. It neither improves R011's K-sharp common-minimax algorithm nor supplies a new minimax lower for growing-logit architectures. Nor does it establish optimal logit/precision tradeoff: it is an explicit sufficient operating point.
5. The construction is a changed integer-weight finite attention rule with a mathematical real-softmax identity. It is not an exact implementation of ordinary exp evaluated by the old finite evaluator. The broader mechanism of length-dependent logits is known; no literature-priority claim is made.

## 8. Source bindings

Read sources: accepted R011 proof and root acceptance; SRC-Pi §§1–4,9–10 for the old finite evaluator, causal local-copy mechanism and complete-cost conventions; G/U §11.1 for the occupation argument reproduced above; BA001 exact scope; BF001 v2 for context only. A SHA-256 manifest accompanies this candidate. Source reviews are evidence of prior acceptance, not a substitute for the new deterministic proof or independent review of GW001.

## 9. Revision log (v1 to v2)

Root's full read found a scope-summary typo in §7 item 3: v1 quoted the optional W=MQ weight ratio M²Q² as though it belonged to the primary W=M construction. Corrected that sentence to state primary b/a=M² and optional b/a=M²Q² explicitly. The theorem, construction, proof, word bounds, and finite-cost ledger are unchanged. Frozen v1 is preserved byte-for-byte. This is a scope correction, not a change of evaluator or statistical assumptions.

### v2 to v3: implementation-width and canonical-provenance clarification

The independently accepted v2 theorem and risk proof are unchanged. Section 5 now distinguishes b-bit persistent payloads from full 2b-bit multiplication products and guarded constant-multiple-b temporaries (safe uniform allocation 4b+4). This removes the overly literal suggestion that every arbitrary allocated b-by-b product fits a b-bit register. Every existing O(b) space and O(b²) arithmetic-work bound already allows this fixed multiplier, so no asymptotic cost coordinate changes. Frozen v1 and v2 remain unchanged.

Canonical intake bindings are added alongside, not in place of, historical source hashes:

* `v10_intake/source/sources/dot-return/readable/proofs/R011_global_rates_and_constant_adaptation_v1.md` and its sibling `reviews/R011_independent_review_v1.md`. A byte/text comparison verifies the canonical R011 proof equals the historical bound proof after removing exactly its added first editorial paragraph and following blank line; the scientific body is unchanged. This identity is recorded in the v3 manifest. The historical proof's old pending-status wording is provenance, not a reset of its later root acceptance.
* `v10_intake/source/sources/euler-stage6/facts/fef8372728290b45.md`: current SRC statement/proof. Its self-contained English proof body matches the historical `SRC-proof.md` apart from the trailing blank line. The inspected singleton-copy, finite evaluator, full-product, complete-cost, and separate PURE interfaces are unchanged; GW001 still changes the evaluator explicitly.
* `v10_intake/source/sources/euler-stage6/facts/a12539a93d9f1ee3.md`: current G/U statement/proof. It contains the historical `GU-proof.md` body verbatim, including §11.1's actual-terminal first-w charging argument. GW001 reproduces that argument rather than importing an h-restricted network assertion.

These identities are local byte/text checks, not a new mathematical acceptance or an external review claim.
