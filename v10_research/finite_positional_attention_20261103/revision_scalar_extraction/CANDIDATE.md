# FPA001: a paid finite positional-attention realization

2026-11-03. Candidate, not an admission. The deterministic construction below is self-contained; the statistical corollary imports ACG001, accepted by the root on 2026-11-03 after independent review and isolated replay. This is a new program in SRC-Pi's transparent model class, not the original SRC-Pi program and not an ordinary learned dense-causal Transformer.

## Statement

For every integer M>=1, h,r>=0 there is a fixed finite causal attention/Boolean-ReLU batch-hybrid program with binary observed input Z_0,...,Z_(M+1) and a zero synthetic token at q=M+2. It uses two paid zero-score singleton copying heads, paid public positional flags, twelve query-independent local Boolean feature rails, and one paid zero-score uniform head. Parameters and schedules depend only on M,h,r. Its exact endpoint bits and twelve post-rounding master numerators B_(u,J),B_(u,C),B_(u,D) satisfy, on every binary word,

    |B_(u,J)/2^h - J'_u/M| <= 2^(-h-1),
    |B_(u,C)/2^h - C'_u/M| <= 2^(-h-1),
    |B_(u,D)/2^h - D'_u/M| <= 2^(-h-1).

Here u=(a,b), J'_u counts departures i=0,...,M-1 with (Z_i,Z_(i+1))=u; C'_u counts those with Z_(i+2)=1-a; D'_u counts those with i<floor(M/2). Each numerator is an integer in [0,2^h]. At the specified cut there is no raw-input, feature-array, accumulator, clean-bank-copy, or other history port. The two endpoint bits are acquired by the same copying layer, not supplied for free.

Replace the twelve master numerators jointly by arbitrary canonical integers B* in [0,2^h], subject to |B*/2^h-B/2^h|<=delta coordinatewise. Endpoint bits, public metadata, subsequent comparator and arithmetic circuits remain exact. This is the entire numeric fault port; arbitrary analog errors or bit faults in other registers are NOT covered. The all-path interface error is eta=2^(-h-1)+delta. Correlations and dependence on the attacked observation are unrestricted.

At the actual endpoint u, select J,C,D from the replacement bank, clip C,D to [0,J], accept iff J>0 and 512D>=J, and output a dyadic approximation to C/J on designated symbol 1-u_first, zero if rejected. The other probability is its exact complement. The finite output is always in the binary simplex and is within 2^-r TV of that exact rational gate output, including J=0, gate equality, empty rows and h=0.

By accepted ACG001, under its binary order-two experiment with M>=64, protected last two symbols, at most k edits among the first M symbols, arbitrary initial pair law, and all-state P²(u,v)>=Pi(v)/M, this single k-blind predictor has actual-terminal next-symbol unsquared TV risk

    R <= min(1, 131072/sqrt(M) + 6433056 k/M
                + 1072176[2^(-h-1)+delta] + 2^-r).

Neither k nor delta is supplied to the predictor. This is O(M^-1/2+k/M+eta+2^-r). Taking h,r >= ceil(log2(M)/2), delta=O(M^-1/2) gives the critical rate. It is a sufficient fractional bank precision statement, not low precision for the entire program.

## 1. Causal construction, indices and exact masks

There are n=M+3 tokens indexed 0,...,M+2. Input raw_t=Z_t for t<=M+1; raw_q=0. Binary acquisition costs M+2 bits; no one-hot representation is assumed free. Public positions cost O(n ell) bits with ell=ceil(log2(n+1)). Public query flag is 1{t=q}; half flag F_t=1{2<=t<2+floor(M/2)}. Their generation uses public comparisons and does not inspect data.

First attention layer: head 1 has Q=K=0, V=raw, and mask {t-1} if t>=1 else {t}; head 2 similarly uses {t-2} if t>=2 else {t}. Singleton normalized weight is exactly one. These are explicit structural masks, NOT large-score approximations to a dense causal attention row. They produce l1_t and l2_t. For a legal departure key t=i+2, they equal Z_(i+1),Z_i; at q they equal Z_(M+1),Z_M. Residual holding of raw and both copied bits is paid. No future target appears in the synthetic token.

For each u=(a,b) in lexicographic order, local feature circuits produce

    R_(t,u)=(1-XOR(l2_t,a)) AND (1-XOR(l1_t,b)),
    V_(t,u,J)=R_(t,u),
    V_(t,u,C)=R_(t,u) AND XOR(raw_t,a),
    V_(t,u,D)=R_(t,u) AND F_t.

There are exactly twelve feature rails. They use only each token's already-copied local data and its public half flag. C uses the designated successor 1-a, so a whole eight-coordinate successor histogram is unnecessary. No endpoint/query information is broadcast backwards.

Second attention layer: one head has one-dimensional Q=K=0, twelve-dimensional V as above. At q its mask is EXACTLY {2,...,M+1}, hence EXACTLY M legal departure keys, including the triple ending at Z_(M+1) and excluding q. At every nonquery token t its mask is singleton {t}. This deliberate harmless choice differs from SRC-Pi's nonquery causal-prefix mask. It remains causal, never empty, and changes no q statistic. Nonquery statistics are computed, then cleared by the public query flag. All three head scores equal zero on allowed keys, so score cap zero suffices. No log/exp approximation, anchor inversion, content matching or query-dependent value is used.

For a row with L allowed keys, sum each feature exactly to integer S (0<=S<=L), then output

    B=floor((2 * 2^h * S + L)/(2L)).

This is nearest dyadic rounding with ties upward. A finite bit-circuit division implements the floor; it is not a real-arithmetic oracle. At q the twelve S are exactly the mathematical J',C',D'. L=M follows from the mask, not from count estimation. Other rows have L=1. The denominator is fixed public metadata computed from the enumerated mask, not a hidden statistical port. The number 1 occupies h+1 bits in the numerator grid.

## 2. Exact finite circuits and overflow proof

Let p=ell+h+r+32. All word widths below are <=2p. Use little-endian bit rails. Bit AND is ReLU(x+y-1), NOT is ReLU(1-x), XOR is ReLU(x-y)+ReLU(y-x), and OR is x+y-AND(x,y). These formulas hold on bits; nothing asserts floor on arbitrary reals. A constant-size two-input mux is (s AND x) OR ((NOT s) AND y), coordinatewise. Carries are full-adder bits; subtraction uses complement plus initial carry one. The final carry from x+(NOT y)+1 is exactly the unsigned predicate x>=y, and the low word is x-y modulo 2^w.

Addition/comparison use ripple chains, O(w) depth and gates, O(w) live rails. Division uses exactly w public iterations from most significant input bit to least: shift partial remainder, bring down one bit, subtract denominator, select subtraction iff carry indicates nonnegative, and emit that carry as quotient bit. For positive denominator its invariant is prefix=quotient_prefix*denominator+remainder, with 0<=remainder<denominator. The shifted remainder is no larger than the scanned dividend prefix, hence fits w bits. Thus it computes quotient and remainder exactly, with O(w²) Boolean gates/depth and O(w) live rails. Holds of other live rails increase a layered sparse representation to O(w³) records. Denominator zero is never selected on an accepted readout; the total circuit is defined there but its output is gated off.

Feature accumulators require ceil(log2(M+1)) bits, not h bits. The rounding dividend is at most 2^(h+1)M+M and denominator 2M. The evaluator chooses w=bit_length(M+3)+h+16, which strictly contains both and all partial sums. Accumulation never rounds. It uses no repeated h-grid addition. Copy operations need only exact bits.

At the cut, convert h+1-bit master words into padded bit rails with exact wiring. Select each of J,C,D through four row-select muxes controlled by the two exact endpoint bits, rather than uncharged dynamic array addressing. In the canonical grid, J already lies in [0,2^h]; clip C,D to J using comparator and mux. Lower clipping is automatic from unsigned canonical inputs. This agrees with ACG001's sequential clipping after multiplication by M/2^h. Its error-preservation proof applies even if the three bank values are inconsistent as counts.

Compute 512D by a nine-place bit shift with enough leading zero rails, compare to J, and AND with J>=1. Equality accepts exactly. For safe total division select denominator J on acceptance and 1 otherwise. Compute m=floor(2^r C / safeJ), then mux m to zero on rejection. The quotient calculation needs h+r+2 bits at most before rejection; w=h+r+16 suffices also for 512D. On acceptance C<=J, so 0<=m<=2^r. Subtract m from 2^r exactly to form its complement, and use endpoint bit u_first to route both symbol coordinates. Dyadic decode uses coefficients 2^(i-r), each with O(r+1) bits. Probability rounding contributes less than 2^-r, safely bounded by 2^-r including r=0. No stochastic gate margin is assumed.

All pointwise feature and suffix circuits are shared and executed at all n tokens, not charged only at q. After public type gating, other tokens' suffix inputs are zero constants. Their computation remains charged. The reference evaluator's evaluate() performs these n suffix calls. The prefix()/readout() split separately exposes only the q cut for fault-interface testing.

## 3. All-path interface and statistical composition

For every legal key t=i+2, direct substitution of copied bits into the feature equations proves their claimed indicator identities. Sum over the explicit q mask. A normalized zero-score head averages uniformly because every allowed exp(0) is exactly one. The rational finite evaluator therefore agrees exactly before final rounding with the three normalized counts in every row. For any x in [0,1], nearest grid rounding with ties upward has absolute error <=1/(2*2^h), including both endpoints; the numerator formula realizes this rounding. This proves the deterministic interface for ALL binary words, not only positive-probability paths of a selected source.

Replacement triangle inequality gives eta=2^(-h-1)+delta. The readout uses these normalized values directly, since common factors M and 2^h cancel from the ratio and comparison. Multiplying only for analysis gives ACG001 estimates with e=M eta, NOT an actual decoder multiplication or input of clean counts. The endpoint is unchanged by the protected-endpoint attack and acquired correctly by copying. Apply ACG001 with this e and xi=2^-r to obtain the displayed risk. That import is the only stochastic step; source-dependent information never enters the program. No source-independent attack assumption is needed for the deterministic interface itself.

## 4. Cut and fault lifecycle

The master cut is after the twelve q numerators have been rounded, before endpoint-conditioned selection, comparison or division, and before any readout fanout. Every suffix copy originates from the replaced master. The endpoint's two bits and h/r/public type/layout remain exact. Nonquery banks and endpoint rails are zeroed with public query-type muxes. Raw input, copied historical arrays, feature arrays, finite attention accumulators, rounding numerators/denominators/quotients/remainders and clean master duplicates are released or overwritten before the cut becomes a permitted downstream observation. Registers retained for public M/layout are data-independent and cannot encode the old counts. There is no later attention layer or raw-memory read.

The readout signature in program.py is a canonical bank, endpoint, h and output precision r. Prefix returns no M, input, scratch or count table. Fault replacement returns a new canonical record with the same endpoint/h, with no original-bank handle. Python caller-owned data can of course still exist outside that interface; the claim is a declared program access rule, not a secure-erasure or hostile-host security theorem. Likewise the external fault injector is not free neural hardware; its construction and cost are excluded from the nominal program, exactly as in SRC-Pi. Corruption of the endpoint or arithmetic requires a new interface theorem.

## 5. Resource ledger: one complete representation at a time

These are constructive upper bounds, not profiles inferred from Python timings. The circuit recipes above give each gate and hold; no old SRC emitter is asserted to have run. Parameters are source-independent. Define p=ell+h+r+32, n=M+3. Counts below include acquisition, exact routing, public flags, copies, live holds, clearing and output decode.

Hybrid neural shape: two attention layers, three heads total (max two in a layer), Q/K dimension 1, max value dimension 12, score cap 0; between/after them shared tokenwise Boolean/ReLU circuits. Depth O(p²), width O(p) per token. Attention's exact finite evaluation work is charged separately; its integer accumulator is not a free neural count rail. This is the same type of hybrid semantics as SRC-Pi, not a claim that one usual hardware softmax layer performs these bit operations at unit cost.

Single circuit coefficients have O(p) bits (Boolean coefficients constant, output dyadics O(r)). Physical scalar/word encodings use O(p) bits. Shared pointwise circuit has O(p²) active arithmetic gates and O(p³) gates/holds conservatively when layered with O(p) live rails. Dense coefficients have O(p⁴) slots, O(p⁵) bits including zeros and biases. Sparse addressed records, including every hold, use O(p⁴) bits. These are ALTERNATIVE parameter representations. The head projections add constant many small matrices and fit these bounds. Finite evaluator code and bounded-word templates conservatively cost O(p⁴) bits.

Masks have two honest representation choices:

- Literal dense: 3n² mask bits, plus O(n ell) position/type/half metadata. Mask generation and writing cost O(n² ell) bitwork conservatively. Online dense scanning costs O(n² p), even though most rows are singleton.
- Explicit active-key lists used by program.py: first two lists have n keys each; third has n-1+M keys, total 3n-1+M keys. Each key and row boundary uses O(ell) bits. Thus O(n ell) mask/list bits, O(n ell²) conservative generation/address work. This is explicit paid sparse structural masking, NOT dense-causal attention or free addressing. Each stored route is read and charged. Converting to dense pays the preceding dense costs.

Finite attention arithmetic on these actual masks costs O(n p²): O(n) selected keys total, twelve O(p)-bit additions per key, and twelve O(p²) round-divisions per row, plus copying/projections/clearing. The dense-mask version adds O(n² p). No logarithm or exponential generation/caches are needed because all scores are zero. Word addresses and controller use O(p) bits; each addressed operation may conservatively incur O(p) overhead already absorbed in the more generous online bounds below.

Sparse pointwise execution including all holds costs O(n p³) bit operations conservatively. Thus one complete sparse-list/sparse-circuit hybrid implementation has online bitwork O(n p³), stored program/parameters/code O(p⁴), stored masks/positions O(n ell), and observed input M+2 bits. Sparse controller/address overhead fits O(n p⁴) if charging a full O(p) per record lookup; this latter larger O(n p⁴) is the unconditional reported sparse online upper bound. Do not substitute dense coefficient counts into that runtime.

One complete dense-mask/dense-circuit implementation has online upper bound O(n² p²+n p⁶), including coefficient-bit operations on zero terms, all-token pointwise maps, dense QKV projections and mask scans. Stored dense parameters/code are O(p⁵), masks/metadata O(n²+n ell). The quadratic term is a conservative full dense-mask evaluation allowance, not an assertion that every sparse implementation performs quadratic work.

Working activation arrays are O(np) packed live bits if all rails are stored as bits and words packed; a conservative scalar-channel allocation in which every Boolean channel occupies an O(p)-bit physical scalar is O(np²). Q/K/V, feature residuals, all twelve bank words per token before clearing, endpoint holds, controller and scratch fit these allowances. Input is O(n) bits and output O(r) packed bits (or O(rp) scalar allocation). No training tape or all-layer retention is included; those would be additional costs.

TOTAL online peak is the sum of simultaneously live parameters+code, masks+metadata, input, QKV/residual/banks, controller/scratch, output. With the conservative scalar allocation this is O(p⁴+n ell+np²) bits for sparse/sparse, or O(p⁵+n²+n ell+np²) bits for dense/dense. The O(h) cut bank cannot be advertised as this total memory. Even choosing h≈(log M)/2 leaves accumulators, addresses and public horizon words of order log M, input order M and paid masks.

Offline: generate the fixed bit circuits and all holds in O(p⁵) conservative bitwork and O(p⁴) scratch/record bits for sparse, then write O(p⁴) program bits. Dense writing additionally costs O(p⁵) bitwork including zeros, with no sparse-format savings. Layout/mask/metadata generation adds the representation-dependent costs above. If sorting records is used, O(p³) records of O(p) bits with O(log p) comparisons fit O(p⁵). Offline peak counts partially generated stored program/masks plus live generation scratch; safe total bounds are the same order as the corresponding online totals (or their sum if both workspaces retained). No source-specific cache generation, training, or external compilation oracle is hidden.

For a PURE all-Boolean/ReLU network with no finite-attention arithmetic primitive, use a separate explicit expansion: unroll THIS program's fixed public bit-operation schedule, replace its elementary bit operations by the gadgets above, and carry every other live rail through an explicit identity. Let T be its selected representation's conservative online bitwork (e.g. O(np⁴) sparse), S its total live bit storage including input, masks, program/constants and scratch (e.g. O(p⁴+n ell+np²)). Then depth O(T+p), width O(S+p), sparse gates/holds O((T+p)(S+p)), dense parameter bits O(p(T+p)(S+p)²), and dense bitwork O(p²(T+p)(S+p)²) are valid. This induction-on-instruction construction is fully costed but is NOT the smaller hybrid depth/width. The new content is the explicit local masked-attention prefix, not generic simulation alone.

## 6. Comparison with accepted SRC and the stronger baselines

SRC-Pi fef8372728290b45, S1–S5, is admitted in FACT_INDEX.json (accepted=true, verdict=correct). It supports the allowed finite causal attention plus Boolean/ReLU semantics, paid singleton masks and full cost conventions. This proof independently constructs its own head values, error interface and readout. SRC's original 9K+1 bank, four nontrivial statistical heads, bounded log scores, add-one reconstruction and h>=max(4,ceil(log2 M)+1) domain are NOT modified or relaxed by substitution. Our binary-only direct feature head has twelve coordinates; introduces public half-position bits; changes nonquery masks to self; changes estimator to an approximate gate; has h>=0 because it does not invert a small anchor; and has a different replacement cut. SRC's old fixed-bank lower bounds do not automatically apply here. Conversely this is not an implementation within a dense-causal-only mask restriction.

Count-only baseline: for M>=64 at certificate 1/M, the accepted positional manuscript (main.tex Theorem finite-window; proofs_finite_horizon.tex) proves that exact full triple counts plus the first and last b symbols, 2<=b<=M+2, have optimal budget-blind competitive factor between 2^-30[1+log((M+2)/b)] and 2^20[1+log((M+2)/b)] relative to g_M(k)=max(M^-1/2,k/M). Set b=2 (distinct from our output-precision r): even this stronger observation, which includes the protected endpoint and initial pair, has an Omega(1+log((M+2)/2)) competitive obstruction across budgets for the SAME map. This is not a logarithmic loss lower bound at every individual budget. Exact counts plus endpoint alone, and any rounded versions, are weaker observations and inherit the obstruction. Our half-position statistics change the observation, so no architecture-wide lower bound follows. The comparison is representational information, not depth.

Stronger ordinary baseline: one pass over the same attacked word maintains four exact J,C,D triples and a two-bit sliding window; on symbol i+2 arrival update the appropriate row and D iff i<floor(M/2). It acquires the same protected endpoint by retaining the last two input bits. This ordinary counter is k-blind, has O(log M) auxiliary bits, O(M log M) conservative bitwork plus finite output division, and meets the same risk with eta=0. If input is resident, charge its M+2 bits; if read-once, say so rather than comparing its auxiliary memory to attention batch total. It can also round only once at the end and match our bank exactly. Thus no neural statistical or computational advantage over equal positional information is asserted. Mask sparsity makes this construction cheaper than a generic quadratic attention evaluation, but does not surpass that sequential baseline.

No claim is made about learned weights, gradient training, minimal head count, necessary precision, architecture-wide optimality, pure-network depth advantage, publication novelty or empirical performance. The scientific bridge is that a paid positional-attention program can preserve the budget-blind robust statistical rate with approximate banks and exact finite readout, without recovering an exact edit-sensitive gate bit.
