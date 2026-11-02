# SB001 — A complete triple bank needs only log-log effective score range

2026-11-02. Author candidate; LLM reviewer algebra/ledger audit passed, root independent acceptance pending. Successor to GW001 v3, not an edit or claim about the old exponential evaluator. No novelty, training, computational advantage, external validation, or universal-architecture lower is claimed.

## 1. Result and changed experiment

Fix K>=2, M>=64, N=M+2, n=M+3, h>=4, Q=2^h, and a public integer κ>=1. Observe the same second-order source and actual terminal query as GW001: Y_j=(X_(j+1),X_(j+2)), j=0,...,M; initialization is arbitrary and unknown. Optional D2(β) means all-state P²(s,t)>=βΠ(t), with Π unknown, β in [0,1]. The algorithm uses neither Π nor β. Denote by Hstat the ORIGINAL R011 scale recorded exactly in GW001 §1; Hstat<=K^(5/2)/sqrt(M+1).

There is a deterministic causal finite program T with two paid singleton-copy heads, paid local pair/triple feature gates, and one dense K³-coordinate statistical head. Its query/key dimension is K², its values are query-independent one-hot triples in [0,1], and it retains every one of the K³ downward-Q-grid coordinates. Its weight cache is exactly {1,κ}: matching pairs receive κ, all other pairs receive 1. These are ACTUAL integer weights. Effective natural logits are 0 and lnκ; no log or exp is evaluated. This changes the original finite exponential evaluator, as GW001 did, but changes GW001's feature dimensions, complete bank, and decoder as well.

Put D_K=K^5(K+1), and Ψ(x)=x(1+ln(1/x)) for 0<x<1, Ψ(0)=0, Ψ(x)=1 for x>=1. Then

 R(T)<=min{1, 2^13 Hstat + Ψ(K^5/(M+1))
                    + Ψ(D_K/(κQ)) + (2K-1)/Q}.                 (SB1)

In particular, with the wholly integer, β-blind choices

 L=bitlength(M+1), κ=L, h=max(4,ceil(L/2)), Q=2^h,

one has sqrt(M+1)<=Q<=2sqrt(M+1), and

 R(T)<=min{1,[ (2^13+2)K^(5/2)+3D_K+2K-1 ]/sqrt(M+1)}.      (SB2)

Its effective logit range is lnκ=lnln(M+1)+O(1), improving GW001's sufficient O(ln M) range to O(lnln M) at the same half-log grid precision. Values remain bounded; neither a hard match mask nor an exact count side port is introduced.

For the lower, fix K>=3 and integers D,r>=1 independently of M, with r>=3 and D>=K³ if this construction is to be included. Consider BA001's entire one-dense-global-summary family, with actual weights in [1,κ] and values in [-1,1], boundary side information as in BA001, and Q between c_-sqrt(M) and c_+sqrt(M), for fixed positive c_-,c_+. The finite BA001 constants imply, for β=0,

 R_family >= c_(D,r,c_-,c_+) κ^(-(D+1)) ln(M)/sqrt(M).        (SB3)

Consequently any such encoder family attaining R<=C/sqrt(M), with fixed C, must obey

 lnκ >= lnln(M)/(D+1)-O_(D,r,c_-,c_+,C)(1).                 (SB4)

Thus the necessary and sufficient ORDER of effective score range is Θ(lnln M), for fixed dimensions/locality and this dense single-block comparison. This does NOT match κ itself, does not give a dimension-uniform constant, and is not a lower for arbitrary deep/global-feature architectures. The upper holds for arbitrary initialization; the lower already holds on the smaller stationary subclass. For K=2 only the upper is asserted.

## 2. Complete causal encoder and decoder cut

Input is x_t=e_(X_t), t<=N, and x_n=0. As in GW001, two zero-Q/K singleton heads copy l1_t=x_(t-1) and l2_t=x_(t-2) when available, otherwise self. Preserve x_t explicitly. These heads, masks, projections, scans and copies are paid, not ideal historical ports.

Paid local Boolean AND gates form p_t(a,b)=l2_t(a)l1_t(b) and v_t(a,b,c)=p_t(a,b)x_t(c). Each observed row's v_t is a one-hot triple; the synthetic terminal triple is zero. Statistical query and key are p_t,p_i. Their exact dot product is 0 or 1 and the cache maps it to 1 or κ. For t>=3 the public allowed keys are 3,...,min(t,N); t=1,2 use self fallback. In particular all M terminal keys participate with strictly positive weight. No mask depends on the query.

For EVERY row, compute the exact denominator D_t=sum_allowed w_ti and all K³ numerators A_tabc=sum_allowed w_ti v_i(a,b,c). Return and retain the COMPLETE bank

 z_tabc=floor(Q A_tabc/D_t), with represented value z_tabc/Q.

The decoder receives this bank, the exact pair p_t, and public K,M,Q,κ only. It scans/selects the K coordinates for p_t, calling them z_c, and computes s=sum_c z_c. If s>0 let p_c=z_c/s; if s=0 let p_c=1/K. Ordered Q-simplex rounding outputs floor(Qp_c)/Q for c<K-1 and the residual in the last coordinate. This is done at every row. Only the terminal output is the requested prediction, but all-token storage/work is charged.

Neither D_t nor A_tabc nor an unquantized total row mass is visible beyond the cut. No historical feature array or earlier token output is reread by the decoder. Physical workspace is explicitly released after its statistical use; all decoder edges obey this cut. The exact pair side information has only K² possibilities and is already covered by BA001's stronger boundary grant. Empty-block normalization is an ordinary paid post-grid operation, not an exact test of J=0.

## 3. Deterministic error, including empty/vanishing rows

Fix a history. Let J count earlier occurrences of terminal pair (X_(N-1),X_N), and C_c its successor counts; these are proof variables, never decoder inputs. The selected true block has coordinates r C_c/J when J>0, where

 r=κJ/[M+(κ-1)J].

If nonnegative numbers y_c sum to r>0 and f_c=floor(Qy_c)/Q, write e=sum(y_c-f_c)<K/Q. When sum f_c>0, the triangle inequality applied to f/(r-e),f/r,y/r gives TV(f/(r-e),y/r)<=e/r. If every floor vanishes, r<K/Q, and any simplex fallback has TV<=1. Therefore, INCLUDING the all-zero floor branch,

 TV(p,C/J)<=min(1,K/(Qr))
  <= K/Q + min(1,K(K+1)M/[κQ(J+K)]), J>=1.                  (3.1)

Indeed 1/r=(κ-1)/κ+M/(κJ), J+K<=(K+1)J, and min(1,x+y)<=x+min(1,y) for x,y>=0. No lower bound on the mass surviving rounding is assumed.

For the original add-one q_c=(C_c+1)/(J+K), TV(C/J,q)<=K/(J+K). Ordered simplex rounding costs at most (K-1)/Q. At J=0, TV(T,q)<=1 and K/(J+K)=1 covers it. Hence on EVERY history,

 TV(T,q)<=K/(J+K)+min(1,A/(J+K))+(2K-1)/Q,
 A=K(K+1)M/(κQ).                                           (3.2)

The key improvement over successor-only values is that nonmatching triples fall in DIFFERENT bank coordinates: they dilute the selected block but do not contaminate its conditional successor law. Post-grid normalization alone cannot recover sub-grid mass; pre-grid κ amplification is what reduces that error.

## 4. Risk integration and integer operating point

GW001 §4 reproduces the universal occupation lemma for arbitrary starts of any homogeneous K²-state pair chain:

 P(J<w)<=min(1,K^4 w/(M+1)), integer w>=1.

Its exact layer-cake consequence, for every a>0, is

 E min(1,a/(J+K))<=Ψ(K^4 a/(M+1)).                          (4.1)

Apply a=K and a=A to (3.2). Since K^4 A/(M+1)<=D_K/(κQ), monotonicity and the accepted original-add-one risk bound 2^13Hstat give SB1. No endpoint-conditioned independence is used.

For SB2, L>=7 and h=ceil(L/2), hence sqrt(M+1)<=Q<=2sqrt(M+1), Q<=2^L-1, and ln(1+Q)<=L. For any D>=1,z>0,

 Ψ(D/z)<=D[1+ln(1+z)]/z.

This follows by the cap if z<=D, and by ln(z/D)<=ln(1+z) otherwise. With z=LQ, 1+LQ<=L(1+Q), ln L<=L, and 1<=L, it follows that Ψ(D_K/(LQ))<=3D_K/Q. Finally Ψ(x)<=2sqrt(x), as proved in GW001, yields SB2. The budget computation uses only bitlength, an integer half/ceiling, and power-of-two construction; no transcendental setup oracle is needed.

## 5. Explicit growing-range lower from BA001

BA001's theorem is finite and uniform over the contents of its source-independent local tables. Although its fixed-family asymptotic interpretation requires fixed a,b, its displayed finite bound may be applied separately at EACH M with a=1,b=κ(M). One must retain its deteriorating constant; treating it as uniform would be invalid.

Let H=3^(2r), u=r sqrt(40DH). Its constants become T=κu, L_B=4κr, C_B=4κu and

 N_B=ceil(8κu+4)+1 <= κ(8u+6),
 A_B=H(2+4κr)N_B^D <= C_BA κ^(D+1),
 C_BA=H(2+4r)(8u+6)^D.                                    (5.1)

Thus BA1 gives, for M>=64, β<=1/16, every Q>=1,

 R_family >= [8192 C_BA κ^(D+1)Q]^-1
       ln(1+(1/8)min{Q/(M max(β,1/M)),M/Q}).                (5.2)

At β=0 and c_-sqrt M<=Q<=c_+sqrt M, the minimum is at least min(c_-,1/c_+)sqrt M. For all sufficiently large M the logarithm is at least (1/4)ln M, while 1/Q>=1/(c_+sqrt M). This proves SB3 with eventual constant 1/(32768 c_+ C_BA), and SB4 follows by taking logarithms. Finite smaller M are irrelevant to the asymptotic assertion, not silently covered by an eventual logarithmic comparison.

The upper fits r=3, D=K³ and nonnegative bounded values; zero coordinates can pad to larger fixed D. BA permits coordinatewise different weights and even query-dependent values, so its class is larger and its lower is valid for this subclass. The two local preprocessing heads only compute windows of length three; they do not introduce extra interior side messages. Scaling every weight by the same fixed factor changes no ratio, so interpreting κ as the maximum/minimum weight ratio is equivalent. For genuine softmax weights, that ratio is exp(effective logit range); no assertion of equality to the OLD finite exponential evaluator is made.

## 6. Full finite implementation ledger (separate alternatives)

All constants in this ledger are absolute; K is NOT hidden in cost notation. Let ell=ceil(log2(n+K+2)), k=bitlength(κ), and b=64(h+ell+k+1). Persistent words are b bits. Products retain their full 2b bits; guarded temporaries use at most 4b+4 bits. Working arithmetic is exact on those actual widths. D_t,A_tabc<=Mκ (self fallbacks also fit), QA_tabc<=2^h Mκ, block sums <=KQ, and decoder dividends Qz_c<=Q². All fit the allocation. No assumption says arbitrary b-by-b products fit a b-bit word.

A deliberately conservative dense schedule is:

* Store all three n-by-n public masks, positions, public layouts, one-hot input and synthetic zero. Explicit writes/copies and optional packed-input conversion are charged.
* Pay O(nK³) Boolean gates for pair/triple AND features plus all residual copies and zeroing. Use a common O(K³)-dimensional feature buffer. Store and evaluate every entry, INCLUDING zeros, of dense Q/K/V and copy maps of total size O(K^6); generic arithmetic costs O(nK^6 b²).
* Each of the three heads scans all n² candidate edges, masked ones included. Statistical edges compute the K²-dot code, choose the two-entry cache via bit mux, and perform all K³ numerator updates and denominator update. This costs O(n²K³b²); singleton heads use the same paid normalization machinery, not free indexed access. No n² numerical weight matrix is retained.
* Retain the full all-token K³ bank. Exact division at every coordinate costs O(nK³b²). Paid block selection scans all K³ coordinates using the exact query pair and bit muxes; pay additions, zero tests, normalization and final ordered rounding at all n rows. Evaluate divisions with a safe nonzero selected denominator (s if positive, K otherwise), so no inactive divide-by-zero is formed. Allocate/clear all banks and release obsolete buffers explicitly.
* Cache creation writes 1 and copies public κ; there is no log/exp generation. Budget generation in SB2 scans public M's bits and uses integer operations. Masks, loop counters, output serialization and instruction/address construction are paid.

Ripple arithmetic costs O(b) gates; full school multiplication and restoring division cost O(b²) gates with O(b) recycled scratch; all loops have fixed bounds and use muxes. A complete known-address Boolean program has conservative bounds

 T0=O(n²K^6b²) instructions,
 S=O(n²+nK³b+K^6b+b²) simultaneous data bits.                (6.1)

S includes input, masks, positions, all matrices, feature/QKV arrays, full bank and output rows, cache, row accumulators, controllers/addresses and arithmetic scratch, not just rolling space. Addresses have O(b) bits because all array/program sizes are polynomial in n,K,b and log b=O(b).

For a fully paid addressed sequential evaluator, store O(T0 b) bits of instruction/opcode/address records. Each elementary instruction scans the S-bit tape for its O(1) reads/writes, comparing O(b)-bit addresses. This yields

 forward bitwork O(T0 S b), forward peak O(T0 b+S),
 offline bitwork O((T0+S)b²), offline peak O(T0 b+S+b²).     (6.2)

Microcode and table/control construction cost O(b²), included. The offline builder emits in execution order, assigning known addresses and generating every coefficient, mask, zero and cache record; no unit-cost RAM or uncharged source-dependent preprocessing is used. Peak is the maximum of FULL simultaneous phase sums. Exporting only the terminal K values does not erase the retained complete bank or all-token work.

Alternatively compile all Boolean operations into exact bounded-fan-in ReLU bit gadgets and explicitly hold every other live bit. Put T=T0+b, S'=S+b. A separate PURE expansion has

 depth O(T), width O(S'), sparse gate/hold records O(TS'),
 addressed sparse wiring/coefficient bits O(bTS'),
 dense coefficient bits O(bT(S')²),
 dense forward and offline-generation bitwork O(b²T(S')²),
 rolling two-layer numeric storage O(bS').                  (6.3)

Final dyadic decoding uses exact O(b)-bit coefficients. Sparse offline work is O(b²TS') if that format is selected. Each phase's peak ADDS its chosen stored parameters/program, input/public constants/masks if separately retained, output, rolling arrays and generation scratch; duplicated constant rails are charged twice. These are alternative complete implementations, not mix-and-match minima. The flattened PURE network is not asserted to be three ordinary softmax heads or to retain SRC's old depth/width. Causality follows from the fixed allowed-key sets and local feature windows.

At SB2's choice k=O(loglog M), while h and ell are O(log M); arithmetic word length still grows as O(log M). The effective-score saving is not a fixed-total-precision or fixed-total-resource result.

## 7. Optional mixing-dependent effective-range order

This refinement follows from AU001's general stationary occupation and exact suffix-mixture lemmas, NOT by changing its predictor. Set t=M max(β,1/M), z=κQ and G(z,t)=1+ln(1+z/t). The SAME program satisfies

 R(T)<=min{1,2^13Hstat+Ψ(K^5/(M+1))
                  +C_K G(κQ,t)/(κQ)+(2K-1)/Q},             (7.1)
 C_K=48K³(K+1)+10D_K.

Proof: for β>=1/M, take the AU001 suffix m=ceil(M/2) and ε=(1-β)^floor(M/4). The stationary component for a=A=K(K+1)M/z has expectation at most

 (2K³(K+1)/z)[17+ln(1+480z/(K(K+1)t))]
 <=48K³(K+1)G(z,t)/z.

Here 480/[K(K+1)]<=480 and ln480<7. The residual expectation is at most εΨ(2D_K/z), which AU001 §4's elementary argument, valid for any z>0, bounds by 10D_K G(z,t)/z: for z<2D_K use the cap, otherwise use ε<=e exp(-t/4), ln z<=ln(1+z/t)+ln t, and e exp(-t/4)ln t<=4. At β=1 the residual vanishes. For β<1/M, UC gives Ψ(D_K/z)<=D_KG(z,1)/z. This proves (7.1) in all cases.

Let f=1+ln(1+Q/t) and choose a public integer κ between f and f+1. Since 1+κQ/t<=κ(1+Q/t),

 G(κQ,t)/κ <=(f+lnκ)/κ<=2.

Thus at Q~sqrt M the upper still has O_K(M^-1/2) risk, with 1+lnκ=O(1+ln f). This is budget selection USING a known β promise, not learning β. The program takes κ as a public integer; it does not execute the transcendental expression. If exact rational β is supplied and one wants a paid selection rule, use a dyadic bitlength overestimate of 1+Q/t; rational division/ceiling and bitlength require additional input-bitlength accounting, so that optional budget-selection cost is not silently included in (6.1). The β-blind choice of §1 needs no such caveat.

There is a matching ORDER lower for this mixing-dependent effective range as well. For β<=1/16 and Q~sqrt M, (5.2)'s truncated minimum is >=[Q/t]/max(1,c_+²). Therefore its logarithm dominates a positive fixed multiple of ln(1+Q/t), by ln(1+ax)>=min(1,a)ln(1+x). BA2 has A_I=H(2+8κr)N_B^D <= H(2+8r)(8u+6)^D κ^(D+1), giving a separate c/(κ^(D+1)Q) floor. Their MAXIMUM controls c f/(κ^(D+1)Q). Risk <=C/sqrt M thus forces

 (D+1)lnκ >= ln f-O(1).                                  (7.2)

For β>1/16, f<=1+16c_+/sqrt M is bounded, so the order assertion for 1+lnκ is trivial. Consequently the least feasible 1+effective-range has order Θ(1+ln f), uniformly across β at fixed K,D,r,c_±, in the stated family for a sufficiently large fixed target risk multiplier. Necessity holds for every fixed multiplier C; sufficiency establishes an explicit K-dependent multiplier, not feasibility for arbitrarily tiny C. This statement compares order with constants; (7.2) is not a pointwise positive lower on lnκ when f is bounded. At Q~sqrt M, f is within fixed factors of 1+ln(1+1/[sqrt M max(β,1/M)]). No all-Q optimal tradeoff or exact threshold in κ is asserted.

## 8. Dependencies and evidence limits

Directly read GW001 v3 (original-add-one comparator, complete finite-cost template), BA001 v1 (entire quantitative lower, including BA2), AU001 v1 (general occupation and residual-mixture proof), and SF001 v1 (context only; no original-master lower is transplanted into this changed interface). R011's ORIGINAL risk inequality is inherited through GW001, not claimed newly proved here. This manuscript proves the new deterministic inequality, occupation substitutions, growth of lower constants and complete changed-program accounting. A separate diagnostic checks finite deterministic examples; neither diagnostics nor an LLM audit is formal verification or an external peer review.
