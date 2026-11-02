# PE1 — Same-information digital protection at the SRC cuts

Date: 2026-11-02. Status: revised construction and elementary coding converse, with independent same-model review and the corrections/extension incorporated; see review-v1.md. The review is not a formal certification. Not a newly admitted Euler Fact, formal verification, implementation benchmark, or coding-theory novelty claim.

## Executive finding

The fixed-port 034–035 impossibility is **not** a robustness lower bound for all encodings in SRC's reported resource class. At the same amplitude and the same per-coordinate finite grid, encoding each original master numerator as binary rails before the one-shot noisy storage boundary gives exact recovery under every correlated coordinate canonical-grid perturbation of size strictly less than 1/2; perturbations of size at most 1/4 admit a constant-gain cleaner. At noise at least 1/2, every bounded-amplitude encoding has a constant actual-risk lower bound under the original exact-side-information contract. All original information, not additional statistics, is preserved. The output is exactly the original clean finite SRC output on every history.

The protection costs O(Kh) scalar channels and O(Kh²) allocated noisy payload bits, with a paid finite encoder/cleaner/decoder. Its added depth, width, coefficients, all-token dense work, movement, and phasewise storage fit within the original *asymptotic* SRC upper envelopes. This does not assert equal constants or a lower resource optimum.

An elementary finite packing theorem gives the exact zero-error channel capacity for this one-shot bounded-coordinate-noise model. A direct counter can use the identical protection mechanism and achieve the same statistical rate. Thus the scientific consequence is a correction of the scope of the architecture/robustness story, not a Transformer advantage or a new error-correcting-code invention.

The indispensable model limitation is explicit: the encoder and decoder arithmetic are reliable, and corruption occurs only at the chosen encoded-state boundary. If the adversary can corrupt the old raw master before encoding, 035 still applies and this construction does not repair it.

## 1. Imported objects and exactly what is used

All paths are the original mother experiment: K≥2, M≥1, N=M+2, observed X_1,…,X_N, a fixed homogeneous second-order table θ with zero transitions allowed, arbitrary initial pair law μ. Only departures 0,…,M−1 are counted. The target is θ_(Y_M), Y_i=(X_(i+1),X_(i+2)), and TV is half L1. No new samples, future observations, source-dependent parameters, independent test queries, or conditional-terminal risk are introduced.

The only mathematical imports for the main upper result are:

1. **SRC**, Fact `fef8372728290b45`, full proof §§3, 8, 9: actual finite evaluator; H∈G_h^(9K+1), G_h={0,1/Q,…,1}, Q=2^h; exact bit extraction; original retained side bits and erasure schedule; original downstream finite program; the full resource ledger.
2. **016**, Fact `a53804d650803060`, statement L1+ and L1-I, with its full proof and review as inherited accepted evidence: for all K≥2, M≥1 and h≥h0(M)=max(4,ceil(log₂M)+1), clean SRC risk ≤min(1,64T), T=K^(5/2)/sqrt(M+1); exact add-one risk ≤min(1,48T).
3. **MM5**, Fact `946d42d5bf502eb4`, the common full-history lower bound ≥2^-16 min(1,T), only when establishing the statistical lower side.

034 `d3e63f7b5e389adf` and 035 `ed3adf29f858da12` are used for comparison and scope, not re-proved. Their domain K≥22, h≥h_N remains unchanged; their cut encodings are expressly fixed. The exact 032–035 proof/review interfaces were inspected. In particular 033 is fixed suffix, while 035 is all decoders at the **raw** 9K+1-coordinate master port. They must not be conflated.

The statistical statement and the protection itself have different generality: the coding lemma holds for any finite message; the specific SRC risk comes from the inherited statistical theorem. No learning/optimization result is imported or proved.

## 2. Fair one-shot communication/storage model

Fix public K,M,h and the original exact side information S (query/mode, actual endpoint, public metadata and the exact flags from SRC). The history prefix computes the same actual H as SRC. A deterministic public encoder E may read H and public parameters, **not additional history statistics**. It writes a codeword Z=E(H)∈G_h^m into m charged physical coordinate slots. Clean H and all encoder/evaluator scratch are erased or inaccessible before the noisy boundary. Copies of encoded Z are not protected exceptions; every coordinate is subject to the noise.

A common history-dependent adversarial kernel may replace Z by Zbar∈G_h^m with

    ||Zbar−Z||∞ ≤ δ

on every history. It has the same observed-history permission as the original fault kernel, and no hidden θ, μ, future symbol, or private decoder seed. The decoder sees only (Zbar,S), and applies a fully paid deterministic decoding program followed by the original suffix. No clean hash, statistic, count table, duplicate bank, hidden timing signal, or source-dependent codebook survives.

This is genuinely the same clean information experiment: E is injective, and H is a deterministic function of E(H). Consequently σ(E(H),S)=σ(H,S) on clean histories. It is **not** the same numerical-dimension experiment: the channel count m may increase, and it is charged. It is also not the old raw-cut adversary followed by a coding step. The storage boundary is redesigned so that the vulnerable state is encoded.

The adversary is stronger, not weaker, in the number of coordinates it may touch: it may corrupt *all* m coordinates simultaneously, with arbitrary correlations. Neither independent noise nor majority averaging is assumed. Canonical corruptions keep the same h-grid and the same amplitude interval [0,1]; the code does not silently restrict damaged rails to Boolean values.

## 3. Binary master protection: exact theorem

Let d=9K+1 and B=d(h+1). For H_i=A_i/Q, 0≤A_i≤Q, write its ordinary h+1-bit expansion

    A_i = Σ_(j=0)^h 2^j b_(i,j),   b_(i,j)∈{0,1}.

The endpoint H_i=1 uses the top bit b_(i,h)=1 and all lower bits zero; h bits would be insufficient. Set E(H)_(i,j)=b_(i,j), as an element of the **same** G_h. Its physical numerator is Qb_(i,j), not a one-bit replacement alphabet.

### Theorem PE1-H

For every K≥2, M≥1, h≥h0(M), and 0≤δ<1/2, there is a common finite protected implementation PE-H of the same SRC predictor such that for every full observed history, every declared query, and every permitted correlated kernel,

    PE-H(X; Zbar) = Pi_(K,N,h)(X)

coordinate by coordinate, including the ordered finite output rounding. Therefore

    sup_(θ,μ,kernel) E TV(PE-H, θ_(Y_M)) ≤ min(1,64T).

For the original full source class, the infimum risk over all decoders after this fixed encoded prefix has the matching statistical order

    2^-16 min(1,T) ≤ R_dec,encoded ≤ min(1,64T).

For every public sequence in this domain, the encoded minimax risk tends to zero iff T→0. It need not have K^5δ→0: δ can be any fixed number below 1/2, and even approach 1/2 strictly from below along a sequence of canonical-grid experiments.

### Proof

Define, on [0,1],

    g(y)=2 ReLU(y−1/4) − 2 ReLU(y−3/4).

If the clean bit is zero, every admissible corrupted rail lies in [0,1/4] and g(y)=0. If the bit is one, every admissible rail lies in [3/4,1] and g(y)=2[(y−1/4)−(y−3/4)]=1. Both boundary points are included. Thus g(Zbar_(i,j))=b_(i,j) for every rail, pointwise and without independence.

The thresholds 1/4 and 3/4 are dyadic on G_h because h≥4. Multiplication by two, subtraction, and ReLU can be evaluated exactly with SRC's signed full-width words; no rounding, threshold oracle, or real transcendental operation is required. There are two ReLUs and one affine difference per rail. Intermediate values have bounded magnitude ≤2. The recovered outputs are *exact* bits, not approximations.

For the remaining range 1/4<δ<1/2, use instead the finite-grid cleaner

    g_Q(y)=ReLU(Qy−(Q/2−1))−ReLU(Qy−Q/2).

If b=0 then j=Qy is an integer with j≤floor(Qδ)≤Q/2−1, so g_Q(y)=0. If b=1 then j≥Q−floor(Qδ)≥Q/2+1, so the two ReLU arguments are nonnegative and their difference is exactly one. This decoder does not even need to read δ. Its coefficients and thresholds have O(h) bits; intermediate magnitude O(Q) is charged and fits the original 128p word allocation. All multiplication/subtraction is exact finite integer/grid arithmetic. There is no continuous-real threshold oracle.

This full-radius statement relies on canonical h-grid corruptions. The constant-gain δ≤1/4 cleaner also works on arbitrary real corrupted coordinates if its arithmetic is ideal/exact; no such continuous-arithmetic physical extension is needed here. Near 1/2 on arbitrary non-grid real inputs, g_Q is not an exact cleaner and we claim no such extension.

Reconstruct A_i by the finite sum above and H_i=A_i/Q, or pass the recovered bits directly to the already bit-expanded original readout. All subsequent inputs and exact side bits are identical to the clean finite program; deterministic computation therefore gives exactly the same output. The clean 016 risk yields the upper bound. The identity corruption is admissible, and any decoder composed with the encoder and clean prefix is a common full-history predictor. MM5 gives the lower bound; its difficult source need not match any 034–035 source. Bounds are uniform over decoders before their infimum. The sequence statement follows from the nonnegative statistical scale as usual. ∎

### Why this is not mere amplitude rescaling

The port amplitude remains [0,1], precision h is unchanged, and the physical error budget remains δ per coordinate. The paid resource is primarily the expansion from d to d(h+1) coordinates. By contrast, H↦aH followed by division by a merely changes the effective absolute noise to δ/a while spending amplitude a; under a fixed relative noise-to-amplitude ratio it provides no gain. PE1 uses a different finite codebook with a positive noise margin, not a hidden amplitude factor.

### Why repetition of raw analog masters would not prove this

If one writes r identical copies of each raw scalar, the same δ displacement can be applied to every copy. The decoder then obtains r copies of the same corrupted raw H. In particular any legal raw-master kernel from 035 can be replicated to all copies, so repetition by itself does not remove its information lower bound. PE1 succeeds because it separates *digital messages* geometrically, not because correlated noise is averaged away.

## 4. Exact finite amplitude–noise–channel tradeoff

This elementary result describes the full finite message alphabet; it is not an assertion that all possible master banks are reachable from SRC histories.

Let a physical coordinate have canonical integer payload {0,…,L}, physical amplitude L/Q, and absolute canonical noise budget e=min(L,floor(Qδ)). The decoder observes m corrupted coordinates in this alphabet. Let

    s = floor(L/(2e+1))+1 = ceil((L+1)/(2e+1)).

### Theorem PE-CAP

The maximum number of deterministic messages that can be recovered **exactly on every permitted corrupted input** is exactly s^m. Hence a set of R messages needs

    m ≥ ceil(log_s R),

when s≥2; when s=1, more than one exactly recoverable message is impossible at every finite m. A noiseless common side-information value can be handled by applying the same theorem separately within each side-information class.

### Proof

For two codewords u,v∈{0,…,L}^m, their integer l∞ noise balls intersect iff |u_i−v_i|≤2e for all i. The forward implication is the triangle inequality. Conversely, when this holds, the integer intervals [u_i−e,u_i+e]∩[v_i−e,v_i+e]∩[0,L] are nonempty for every i; choose one integer in each intersection. Any decoder receiving their common point cannot output two distinct messages exactly. A randomized decoder cannot do so with probability one either.

Partition each coordinate alphabet into consecutive intervals of length 2e+1, with a possibly shorter final interval. There are s intervals. Two codewords in the same product cell differ by at most 2e in every coordinate and therefore cannot encode distinct messages. This gives the upper bound s^m.

For the lower bound take the product alphabet

    {0, 2e+1, 2(2e+1), …, (s−1)(2e+1)}^m.

Any two codewords differ by at least 2e+1 in a coordinate, so their noise balls are disjoint. Nearest-level decoding of each coordinate works; arbitrary unused inputs can be assigned a fixed fallback. This yields s^m messages. ∎

Consequences:

* For amplitude1, L=Q, any fixed 0<δ<1/2 gives a constant-size s≥2 for sufficiently large Q, so recovering a completely unrestricted d-coordinate h-grid message requires m=Ω(dh). Binary rails use m=d(h+1), hence attain this order for every fixed δ≤1/4.
* At δ≥1/2, Q even, e≥Q/2 and s=1: no number of amplitude1 coordinates can transmit two messages exactly. The common erasure point (1/2,…,1/2) is within radius1/2 of every codeword. This excludes arbitrary-secret-message exact recovery, not all statistical learning under additional exact side information.
* For variable small δ, binary rails need not be channel-optimal. Base-s digits encode R=Q+1 possible scalar values in ceil(log_s(Q+1)) channels per scalar. General mixed-radix packing reaches ceil(d log_s(Q+1)) channels for all d-coordinate payloads, at the price of finite large-integer conversion; no efficient-cost claim is hidden in this capacity equality.
* A finite constructive general encoder ranks the d original numerators in base Q+1, converts the resulting O(dh)-bit integer to base s by restoring division, and maps each digit to the separated level. Its inverse uses finite multiply-add and range checking. School arithmetic gives polynomial, e.g. O((dh+m log(s+1))^3), bitwork and O(dh+m log(s+1)+m log(L+1)) charged working bits. This deliberately loose bound includes physical noisy payload storage; the special binary construction is considerably cheaper.
* The Ω(dh) conclusion applies to universal exact recovery of all (Q+1)^d banks. PE1 does **not** prove that the reachable SRC image has that size, nor that preserving every master bit is necessary for low prediction risk. Those would be different lower bounds.

## 5. Resource ledger for PE1-H

Write n=M+3, p=4h+4ell+64, ell=ceil(log₂(M+K+4)), d=9K+1, B=d(h+1). Original SRC is the dense/uncached batch hybrid. The implementation below keeps that representation; it does not splice in a cheaper sparse or cached entry.

### 5.1 Explicit encoder options

A black-box encoder receiving only scalar H uses SRC's exact finite-grid extraction (§3). For one coordinate, start R_h=QH and for j=h,…,0 compute

    b_j=ReLU(R_j−(2^j−1))−ReLU(R_j−2^j),
    R_(j−1)=R_j−2^j b_j.

On integer R_j this is exactly the indicated bit, and the residual lies in [0,2^j−1]. The top step handles H=1. All d coordinates are processed in parallel; completed bits are retained with paid identity holds. Depth O(h), width O(dh), active operations O(dh), and holds O(dh²). Coefficients up to Q and residuals up to Q use O(h) integer bits; no amplitude cap is asserted for these *clean internal* extractor residuals. The **vulnerable codeword** still has amplitude1. These coefficient/range costs already occur in original SRC's extractor and fit its 128p-word allowance.

A more direct changed evaluator writes its already-computed exact quotient numerator bits to 0/1 rails instead of first materializing the scalar master. This also avoids a vulnerable raw master bank, but we do not need this optimization for any bound. The conservative black-box route is fully charged.

Every noisy rail is allocated an h+1-bit payload, because corrupted values may be any integer numerator in [0,Q]. Calling this only B physical bits would be wrong. Clean Boolean information is B bits; post-noise canonical payload allocation is B(h+1)=O(Kh²) bits. Original ordinary master storage is d(h+1)=O(Kh) payload bits. With the SRC general physical-word convention use O(Bp), not O(B), bits.

### 5.2 Added dense neural costs

Use constant-depth cleaners at width O(B). Reconstruct H in one paid affine layer if retaining an unchanged scalar suffix; alternatively use cleaned bits directly. Including full copies, side-bit holds, erased originals, completed-bit holds and generous padding gives:

| Added quantity | Conservative bound |
|---|---:|
| pointwise depth | O(h) |
| maximum scalar width | O(dh) |
| active gates/terms | O(dh) |
| identity/copy/clear/hold records | O(dh²+d h) |
| single coefficient / intermediate word bits | O(h), or use existing O(p) allocation |
| dense coefficient slots | O(d²h³) |
| dense parameter bits with O(h)-bit wrapper words | O(d²h⁴) |
| dense parameter bits if padded to SRC p-bit words | O(d²h³p) |
| dense all-n pointwise bitwork, school arithmetic | O(n d²h³p²) |
| full noisy port allocation, payload / SRC-word convention | O(dh²) / O(dhp) |
| wrapper controller/address and arithmetic scratch | O(dhp+p²), generously |

The δ≤1/4 cleaner uses only constant-size dyadics. The full δ<1/2 grid cleaner uses O(h)-bit gains/thresholds and O(Q) clean intermediate magnitudes; these remain within the displayed O(p)-bit uniform format. Its table entries do not claim the entire SRC evaluator is unit-cost or robust to arithmetic faults. The width bound includes the original O(K) exact side bits, not an additional large exact statistic.

**All-token charge:** the same added pointwise map is executed at all n positions, although only q produces the requested answer. The bitwork expression therefore includes n. Fixed public q selectors can be used only with their own charged holds/routing; no one-token saving is needed.

Offline generation writes every wrapper coefficient including dense zeros and biases, and generates all addresses/holds/clears. With G',T',I' wrapper record counts, retain SRC's O((G'+T'+I')p²) generation work and O((G'+T'+I')p) generation scratch, plus the complete dense-bit writes. This is in addition to, not instead of, the old layout/masks/code generation.

### 5.3 Phasewise coexistence and total envelopes

During encoding, old H, accumulated encoded rails, exact side bits, and extractor residuals coexist. During the fault boundary, no accessible old H/evaluator scratch survives, but storage still allocated for these banks must be counted. During decoding, damaged rails, cleaned rails, reconstructed H/bit-bank and exact side bits can coexist. Then the original suffix's scratch, current banks and output are allocated according to its original schedule. A conservative extra per-token O(dhp+p²) live allocation covers these constant copies. Thus **add** O(n d h p+n p²) bits to the appropriate old phase totals before taking their maximum; do not replace total peak by a rolling-array number.

Here d=O(K), h≤p and in fact h≤p/4. The modified implementation is therefore still within all the following original asymptotic envelopes, with possibly larger absolute constants:

    depth O(Kp²), width O(Kp),
    word/coefficient O(p) bits,
    dense slots O(K³p⁴), dense parameter bits O(K³p⁵),
    dense all-token work O(nK³p⁶),
    uncached attention work O(n²(K+p)p²) (unchanged),
    rolling work O(nKp²),
    masks/positions O(n²+n log(n+1)) (unchanged),
    observed one-hot input O(NK) (unchanged).

The old finite log-generation, its multiword scratch, evaluator code, input acquisition, QKV, all metadata, full products/quotients/guards, output decode, offline record generation, dense file writes, and maximum of simultaneous phase totals remain charged. No compiler/profile has been executed. The claim is a constructive upper bound, not a measured equality or a claim that big-O equality means identical numerical cost.

This matters scientifically: reporting only these broad upper envelopes cannot support a positive lower bound proportional to Ψ(K^5δ) across all implementations in the envelope. The protected implementation is an explicit counterexample in the same one-shot bounded-noise physical coordinate model.

### 5.4 Sharp risk obstruction above half the amplitude

The exact-message converse can be strengthened to an actual prediction-risk obstruction using the unchanged exact-side-information contract. Allow **any** common encoder into any public finite number m of canonical [0,1] rails, even one computed from the entire observed history, with arbitrary paid computation before the cut. The encoded dimension, schedule and metadata must not be data-dependent uncharged side channels. Keep precisely the original exact side bits, and corrupt only encoded coordinates with radius δ≥1/2.

The common kernel that sends every coordinate to 1/2 is globally legal: 1/2 belongs to G_h and is at distance at most 1/2 from every clean value. After this erasure the decoder's only data are the original exact side bits. Under the actual-query mode and SRC §§2,8 these are functions of the actual terminal pair and, if retained, the initial nonzero flag F_3=e_(X_2); the other tokens/flags at the synthetic query are zero and remaining metadata are public. Thus under an iid source they provide at most three distinct iid symbols. This uses the complete original side-information audit, not removal of allowed information.

Consider the legal second-order sources in which every row equals Bernoulli(p) on symbols {0,1} and the initial pair is iid with the same p, with p_0=1/4 and p_1=3/4. All other alphabet symbols have zero probability. The target is always the same Bernoulli row for that source, so the actual query does not change the target. The two target distributions have TV distance 1/2. The overlap mass of three iid samples is

    Σ_(x∈{0,1}^3) min(P_(1/4)(x),P_(3/4)(x))
      =(1+9+9+1)/64=5/16.

When N=3 the possible X_2 flag duplicates one terminal symbol, leaving only two distinct samples; its overlap is at least the three-sample overlap by data processing. The same is true if no initial flag is retained. Any exact side output is a deterministic function of those at most three symbols, so its overlap is at least 5/16. Independent private decoder randomness can be included without changing this overlap.

For any output q at a shared side observation, the triangle inequality gives

    TV(q,Bernoulli(1/4))+TV(q,Bernoulli(3/4)) ≥ 1/2.

Weight by the common part of the two observation laws, integrate outputs/seeds, and obtain r_0+r_1≥(5/16)(1/2)=5/32. Consequently every decoder and every such encoded prefix has worst-source risk at least

    max(r_0,r_1) ≥ 5/64.

Thus, with fixed amplitude1 and original exact side bits, the one-shot canonical-grid threshold is sharp: below 1/2 the protected SRC reaches the statistical rate (within its stated resource class); at or above 1/2 no finite channel expansion or pre-cut computation can make uniform risk vanish. This does not restrict models that add exact data-dependent side channels, change amplitude, or alter the corruption metric.

## 6. The final V port under the same global L1 edit budget

This is a separate corruption metric. Let clean V∈{1,…,2Q}^K be the actual finite SRC bank, not ideal counts. Write U_c=V_c−1∈{0,…,2Q−1}; it has exactly h+1 bits. Let B_V=K(h+1) and choose a public integer r≥1 with

    rQ > 2D.

For each bit b, write r identical positive integer coordinates

    Z_(b,t)=1+Qb,   t=1,…,r.

Every coordinate belongs to the original physical positive payload range {1,…,2Q}, because Q+1≤2Q. The total encoded dimension is m=r B_V. Let the adversary replace the complete encoded bank by arbitrary canonical positive coordinates with **one global** budget ||Zbar−Z||₁≤D. No error exemption is made for replicas.

Decode each bit from S_b=Σ_(t=1)^r (Zbar_(b,t)−1), using threshold rQ/2. If b=0, S_b≤D<rQ/2; if b=1, S_b≥rQ−D>rQ/2. Hence the bit is exact. Reconstruct V_c=1+Σ_j2^j b_(c,j), erase decoder scratch, and invoke the original positive-bank suffix. The clean output is again reproduced on every path.

A finite choice is r=floor(2D/Q)+1. The strict inequality handles ties correctly. This encodes the original actual V exactly; it does not manufacture an ideal bank or ignore the nominal SRC error 78. One can protect both cuts in succession: use PE1-H at the master cut and this V code at the final cut, so the second clean bank is precisely the original V.

**Charges:** the noisy payload has rK(h+1) slots, each h+2 bits; sum accumulators have O(h+log(r+1)) bits. Copying/writing the code costs O(rK(h+1)(h+2)) bit moves. Summing/thresholding/reconstruction costs at most O(rK(h+1)(h+log(r+1))²) bitwork with fully padded school operations. All simultaneous original/encoded/damaged/decoded banks, address/controller/program and input/output storage are additional, not free. A fixed finite comparator or ReLU integer-step gadget handles the threshold; there is no real division oracle. For constant r the same O(Kh)-width/O(h)-depth dense wrapper construction remains inside SRC's envelopes. For growing r we make no such absorption claim: the explicit r-dependent port, arithmetic, dense expansion and movement costs must be carried.

This is a budget-per-whole-bank theorem. If an alternative model increases D in proportion to the number of allocated coordinates, repetition need not help. Indeed rQ>2D fails when D scales as a sufficiently large fixed fraction of mQ=r B_V Q. No claim of constant-relative-fraction adversarial L1 correction is made; that would need a genuinely different code and ledger.

## 7. Strong direct counting comparator, charged on the same information

Protection does not exploit an attention-specific property. A direct exact counter can use the same observation X_1^N, same actual endpoint/query, and the same one-shot corruption channel, with no hidden θ or future symbol.

### 7.1 A simple strong batch comparator

Keep the same already-paid full one-hot input buffer O(NK), acquire the actual endpoint from its last two observed symbols, and before the cut scan the observed triples t=3,…,N. For each c keep an exact b-bit counter C_c for triples whose first two symbols match the actual endpoint and whose successor is c, where b=ceil(log₂(M+1)). Fixed public loops test the pair and update all K counters by gated increment, so no data-dependent lookup or free RAM is required. Acquisition and the scan are causal: every symbol has already been observed at this prediction time. All history is erased/inaccessible after the cut. This baseline does not assume an earlier late-query/no-re-read boundary; such a boundary would be a different experiment.

Counts are formed from precisely M departures; the last observed successor X_N is counted, but no departure of Y_M is counted. On every history the resulting row is exactly the add-one row

    p_c^+=(C_c+1)/(Σ_a C_a+K).

Encode all Kb counter bits into amplitude1 rails before the same δ<1/2, h-grid noise boundary, erase clean counts/scratch/history, clean each rail with g (δ≤1/4) or g_Q (all δ<1/2), and reconstruct the counters. The decoder computes the denominator and finite ordered output

    q_c=floor(Q(C_c+1)/(J+K))/Q, c<K−1,
    q_(K−1)=1−Σ_(c<K−1)q_c.

This is a probability vector and TV(q,p^+)≤(K−1)/Q on every history. Therefore

    sup risk ≤ min(1,48T+(K−1)/Q) ≤ min(1,49T)

for h≥h0(M), regardless of the correlated permitted master-style perturbation. The last inequality follows from Q≥2M and sqrt(M+1)≤2M, K−1≤K^(5/2).

A conservative complete sequential-bit implementation ledger (not a neural-depth claim) is obtained by putting w=h+b+ceil(log₂(K+1))+O(1):

* Input acquisition/copy/clear: O(NK) bits/work; actual endpoint acquisition O(K).
* Fixed triple scan and K gated b-bit increments: O(MK(b+1)) bitwork; no raw table of K³ counts.
* Live counted state plus endpoint/control: O(Kb+K+w) bits before protection.
* Noisy rail bank: Kb(h+1) payload bits, or O(Kbw) if using padded physical words; decoded/original/damaged constant copies are included in the phase total.
* Counter protection, storage writes, comparisons and reconstructions: O(Kb(h+w)) conservative bitwork and O(Kbw+w²) phase work storage.
* Sum, smoothing and K ordered integer quotients: O(Kw²) bitwork and O(Kw+w²) bits including output; all remainders/guards are retained.
* Compact fixed-loop code, public counts and layout: O(Kw+w²) bits is a safe bound; offline full generation/zero writes O(Kw²+Kb(h+1)+w³). No exponential table is used.
* Full batch phase peak includes the O(NK) input if it remains allocated, plus code/public parameters, counters, all rail copies, scratch, metadata and output. It is bounded by O(NK+Kbw+w²), not by counter size alone.

The count scan is not claimed to be a depth-O(Kp²) Transformer: a direct sequential implementation can have depth proportional to M if unrolled. Conversely it has no attention n² work. These are genuinely different resource tradeoffs. A comparison must report both rather than declaring coordinatewise neural superiority from one cheaper ledger entry. A full online single-pass comparator without a batch reread can instead keep a table for all K² rows or use the already accepted capped/combinatorial streaming scheme (`5110203ec700e7e1`); its state and update costs must be carried, not silently replaced by the batch K-counter costs.

### 7.2 No clean-information cheating between encoders

The PE-H construction preserves the complete original H information and is therefore the strictly same-information answer to the question. The direct counter is a separate prefix comparator: it has the same raw observed history but changes the sufficient statistic. It does not get H *and* counts after the cut. All count production, erasure and physical protection are paid. It shows that the protection phenomenon itself cannot certify an attention advantage.

For a comparator that must preserve exactly the original clean H information, one can simply implement the same finite head computation and apply the same code; nothing in the coding theorem depends on the name of the front end. Conversely proving a lower risk for direct counts than the original H would require a separate statistical comparison, not this exact code theorem.

## 8. Robustness model boundary: what this does not solve

1. **Pre-encoding faults:** if the adversary may first replace raw H by Hbar under the old 035 rule and the encoder sees only Hbar, composing E with any decoder is an old permitted decoder. Therefore 035 still gives its lower bound. Encoding cannot undo information already erased.
2. **Continuous arithmetic noise:** errors inside head computation, encoder extraction, cleaner gates, all copies over time, the final normalizer or output are excluded here exactly as arithmetic faults were excluded from 032–035. Extending to them requires a new physically complete model and theorem. Repeated clean refresh does not become free.
3. **Exact side bits:** original query/endpoint/flag exceptions remain. No new exact data-dependent side bit is introduced. If these bits become noisy, they too must be encoded or their fault effects analyzed.
4. **Unit-cost physical precision:** the allocated h-bit range of every damaged rail is paid. No claim that a scalar analog coordinate stores h bits at a universal constant physical energy/area is made; the bit ledger is the specified abstract resource model.
5. **Architecture optimality and training:** this is a finite implemented program with chosen coefficients. It establishes neither trainability nor a resource lower bound for arbitrary Transformer families.
6. **Coding novelty:** positive noise margins, radix encoding and finite packing are elementary digital communication ideas. The contribution here is a source-specific checked bridge and a falsification of an overly broad reading of the old fragility bounds. A paper should not advertise these elementary coding facts as new.
7. **Actual SRC image:** the exact capacity converse is universal-message coding. Low-risk encoding of the reachable master manifold may need fewer channels, or lossy probability encoding may be better. No matching low-risk resource converse is proved here.

## 9. A purposeful next question

The one-shot-port question is now scientifically bounded: below the sharp half-amplitude noise threshold, digital encoding gives exact correction at logarithmic channel expansion, already inside SRC's broad upper envelopes; above the threshold every encoded prefix has constant risk. Direct counting shares the positive result. Merely designing another ad hoc port protector would add little.

A particularly natural source-level follow-on is corruption of the observed symbols before any encoder: if k observed symbols are changed while the true actual terminal pair is kept, every edited symbol affects at most three counted triples and the queried count vector changes in L1 by at most 6k. A direct add-one upper bound of statistical risk plus Ψ(6K⁴k/(M+1)) follows from the already proved return-count tail, but that elementary bound is not by itself a major new theorem. A meaningful program would seek a matching full-class minimax lower bound and/or β-adaptive robustness with exactly audited endpoint information. The root researcher is developing this candidate; it is not proved or assigned an accepted status in this file.

A second meaningful choice is a model in which representation cannot evade the fault budget by moving the cut: e.g. one adversarial noisy storage/write event at an unknown time, or bounded perturbations after every declared arithmetic layer with an explicit margin/refresh budget, fixed channel count, fixed amplitude/precision, and the same causal input access for SRC and a counter. A useful next theorem must specify fault timing, permitted refresh, exact gates/coefficients, and total state before claiming a neural depth–reliability tradeoff. Whether such a model is relevant to realistic trained networks is a separate empirical/learning question.

Alternatively, if the paper's center is prediction under partial mixing, prioritize the concrete R011-to-network selector bridge rather than spend further effort on standard channel coding. The protection result should then serve as a short scope theorem/limitation: raw-port lower bounds reveal a fragile representation, not universal physical necessity.

## 10. Verification status

This file contains complete symbolic arguments for the new protection and finite coding capacity statements. Finite diagnostics, when present in the companion files, only test the stated formulas and boundaries; they do not establish universal correctness. Independent review is recorded separately, without being called formal verification or an Euler admission. Imported 016/MM5/SRC are used within their documented domains, not newly re-certified. No GPU experiment, training run, actual hardware injector, old compiler, publication, purchase, or external contact was performed.


## 11. Review resolution and version history

- v1 contained the δ≤1/4 bounded-gain construction, exact finite packing theorem, raw/V coding and direct counter ledger.
- Independent LLM review `review-v1.md` confirmed the core proofs and corrected the uniform-format costs to O(K²h³p) parameter bits and O(nK²h³p²) bitwork. Both local h-word and uniform p-word alternatives are now explicitly separated in the ledger; only the p-word version is used to compare with the unchanged SRC format.
- Review supplied the full canonical-grid δ<1/2 cleaner and the δ≥1/2 actual-risk lower bound 5/64. Their complete proofs are incorporated above.
- General odd-L amplitude thresholds are governed by e≥ceil(L/2); the stated sharp real threshold1/2 uses L=Q=2^h, which is even. No odd-grid assertion is imported.
- Review boundaries retained: same information is not the literal same unencoded cut; old scalar corruption remains uncorrectable by a downstream code; asymptotic resource-class inclusion is not numerical cost identity or resource optimality.
- The reviewer reports 268 bounded-gain-cleaner cases, 1,020 full-threshold cases and 28 small exact-capacity instances. These diagnostics are recorded as the reviewer's execution, not independently re-run here; separate reproducible author diagnostics are stored alongside this file.
