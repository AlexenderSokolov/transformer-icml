# BC001 — Stationary binary frontier for finite evaluators of bounded causal architectures

2026-11-02, post-stage-5 research. Author candidate v1; independent review and root acceptance pending. Stage-5 freeze and paper_v3 are untouched.

## 1. Exact family and theorem

Let K=2, M>=64, N=M+2 observed symbols, n=N+1 including a synthetic terminal query, and Q=2^h, integer h>=4. The source is any homogeneous binary second-order source with hidden stationary pair law Π and all-state certificate P²(s,t)>=βΠ(t), 0<=β<=1, initialized at Π. Loss is expected TV for the next-symbol law at the ACTUAL last pair, not an independent stationary query.

Use CF001 §1's temporally causal finite-evaluator family, now with K=2. Explicitly fix depth, heads, dimensions, affine/ReLU DAG sizes, coefficient/range/Lipschitz bounds, local radius r>=3, and output count D>=8, independent of M,h,β. Require enough capacity for the prototype in §5 (one head, one global layer, width at least 16, local radius three, coefficient magnitude bound at least two and affine row-sum bound at least two). The main supplied-table construction only needs row-sum-one projections, so CF001's original larger budget already suffices. The optional explicit local AND alternative in §5 requires row-sum bound three instead and is not claimed under the smaller bound. Initial historical features are supplied finite dyadic tables of trailing causal windows. Historical tables, masks and all parameters are independent of future source symbols. Masks are public, independent of source data and boundary labels, causal, nonempty, and have density >=c with fixed 0<c<=1/3. Ideal affine Q/K/V, bounded dot-product scores, and affine/ReLU updates obey FA001 v3 and CA001 v3's uniform primitive bounds on every formal history. Fixed larger depths may contain identity padding. Every numerical description, supplied table and mask has its full actual cost charged.

The boundary field S contains first/last three symbols, or the chosen fixed larger windows (b<=2r symbol slots). It enters the encoder only through the appended terminal query, never through historical parameters or states. The decoder may also read S. Historical computation is genuinely causal. Branch freezing in the proof is only a stronger information experiment, uniformly valid even on histories inconsistent with the frozen label.

Evaluation is exactly FA001 v3 at target parameter h+3, so fractional precision P_f=4(h+3)+C_arch and internal denominator d_f=2^P_f. Afterwards take coordinatewise downward Q-grid floors. Retain ONLY this D-coordinate bank, S, and source-independent public metadata/randomness. Decoder history rereads, other tokens' outputs, clean numerators, denominators and residuals are forbidden. The decoder may be arbitrary; costs of the particular upper decoder below are charged separately. All constants and bounds are uniform seedwise; all choices are source-law-independent. Call the minimax stationary risk R_BC.

Put e=max(sqrt(β),1/M), t=M e, and

    W(Q,t)=[1+ln(1+Q/t)]/Q,   F=max(M^(-1/2), W(Q,t)).

There are explicit c_arch>0 and absolute C=131619 such that

    c_arch F <= R_BC <= min(1,C F).                     (BC1)

The upper is a β-blind finite program. This is a theorem about finite evaluators of fixed-depth ideal architectures, NOT about fixed-depth PURE bit expansions, every Transformer, or arbitrary initialization.

## 2. Markov concentration for a nonlinear causal output

Use CA001 v3's influence constants C0,Γ,Λ after local-radius and dense-mask adjustments. For every frozen boundary branch and each output coordinate f, replacing source symbol i changes f by at most d_i; sum d_i<=C0, sum d_i²<=Λ/M, and d_i<=Γ/M for i>=n/2. These are bounds on the IDEAL pre-cut vector. No Lipschitzness of finite rounding is assumed.

The binary active-chain reference experiment is BI001 v2 §§1–2. Write a=1/(2M), p∈[1/4,3/4], W0=00,A=01,B=10,C=11, and source rows θ_W0(1)=a, θ_A(1)=p, θ_B(1)=1-e, θ_C(1)=1/2. Its stationary law is (xe/a,x,x,2px), x=(e/a+2+2p)^(-1). When β<=1/256 its all-state certificate holds. Set

    J=floor(min{1/(4e), M²/(4Q²)}).

For Q<=M/4, J>=4 and J<=M/4. The disjoint events E_j, 4<=j<=J, have fixed zero prefix of length N-j followed by an initial 1 and j-1 transitions of the active reference chain

    R_p = [[0,1-p,p],[1,0,0],[0,1/2,1/2]]

on A,B,C. The actual source path measure dominates (32M)^(-1) times the reference measure ν_pj on every such path, even though event probabilities depend on p. The reference chain begins at A. Also ν_pj(terminal A)>=1/8 for j>=4. These facts are exact BI001 v2 source calculations, not conditional IID assertions.

Here is the new transfer to arbitrary nonlinear causal f. Since R_p²(s,B)>=1/8 for every s,p, two active chains from any two states can be coupled in two-step blocks, meeting with probability at least 1/8 each block and thereafter remaining equal. Conditional bridges fill intermediate states. Expected number of differing states, including the initial state, is <=2 sum_{k>=0}(7/8)^k=16. Emitted-symbol disagreements are no more numerous. Any two realized continuations with the same prefix therefore satisfy, by telescoping single-symbol replacements,

    |f(path)-f(path')| <= (Γ/M) × number of differing symbols.

All suffix indices are late, and local preprocessing is ALREADY included in Γ; do not multiply by r again. Hence differences between continuation expectations after any two alternative next states are <=16Γ/M, safely <=L_c/M with L_c=34Γ. The bound holds for every fixed common prefix and every frozen branch; mismatched formal boundary labels are allowed by the model contract.

Reveal the j-1 reference transitions successively. Each Doob martingale increment has conditional range <=L_c/M; its conditional variance is at most (L_c/M)². Orthogonality gives

    Var_ν f <= L_c² j/M².                               (BC2)

Differentiate the finite path-probability polynomial with respect to p. In each of j-1 single-transition insertions only row A changes, with signed entries -1,+1 to B,C. Prefix laws have total mass one and the difference of continuation expectations is <=L_c/M. Consequently

    |d E_ν f/dp| <= L_c j/M.                            (BC3)

No ratio-of-expectations replacement, IID Efron–Stein argument, spectral-gap assumption, or derivative of a discontinuous finite network is involved. When Γ=0 the quantities are deterministic and the same statements hold with zero right sides.

## 3. Complete finite-message tube and binary logarithmic lower

Let H_b=2^b and define

    τ_B=L_c sqrt(32 D H_b),
    N_B=ceil(2τ_B+6)+1,
    A_B=H_b(2+L_c) N_B^D,   c_B=1/(524288 A_B).

Chebyshev plus union over all D H_b frozen-coordinate functions gives a simultaneous event G_pj of reference probability >=31/32 with |f-Ef|<=τ_B sqrt(j)/M. If τ_B=0 use the deterministic event. A parameter mesh of spacing at most M/(L_c Qj) gives at most (2+L_c)(1+Qj/M) centers per branch, within 1/Q of every expectation curve point; a zero-speed curve needs one point.

FA001 proves actual pre-cut error <=1/(8Q) on EVERY history, uniformly over branches. Relax to E=1. Since Q sqrt(j)/M<=1/2, each final integer bank QZ on G_pj lies within τ_B+3 of a mesh point: concentration <=τ_B/2, mesh <=1, finite evaluation <=1, downward rounding <1. Thus the p-independent set of complete good messages, including actual S and granted j, has size <=A_B(1+Qj/M). Parameter-dependent good events do not undermine this fixed covering set. Extra zero padding is only mathematical inclusion unless its writes/storage are paid.

For completeness, the target-specific counting step is as follows. Under the SAME uniform prior on the interval of length ell=1/2, surround the <=R_j decoder values by intervals of radius ell/(64R_j). Their prior measure is <=1/32. For each p, probability of G_pj and terminal A is >=1/8-1/32=3/32. Integrated probability of that event outside those intervals is >=1/16. On terminal A the actual target Bernoulli parameter is p. Therefore reference average loss on A is >=1/(2048R_j). Fix and then average decoder/encoder independent seeds; the prior is the same for all seeds. Use pathwise domination and sum disjoint E_j to get

    R_BC >= [1/(65536 A_B M)] sum_{j=4}^J 1/(1+Qj/M)
          >= (c_B/Q) ln(1+min{Q/(M e),M/Q}/8),           (BC4)

for β<=1/256 and Q<=M/4. The final inequality follows by u=Q/M<=1/4, shifting j=k+4, using 1+u(k+4)<=2(1+uk), integrating, J-3>=J/4, and J>=half its defining real cutoff. No witness parameter is handed to the decoder.

## 4. Floors and exhaustive all-regime completion

CA001 v3's binary IID argument applies to this same family and FA error transfer. Define

    τ_I=sqrt(5 D H_b) max(Γ,sqrt(Λ)),
    N_I=ceil(2τ_I+6)+1,
    A_I=H_b(2+C0)N_I^D, c_I=1/(256 A_I).

Then R_BC>=c_I/Q for every β. These IID sources satisfy every all-state certificate; no range-uniform UI001 strengthening is needed since architecture bounds are fixed. The standard two-point binary IID full-history test also yields R_BC>=c_S/sqrt(M), c_S=1/256: choose p±=1/2±1/(16sqrt(M+2)), history KL<=1/8, TV<=1/4. Granting the whole history only strengthens the experiment.

The following is BS001 §3's scalar argument with z=Q. If β>1/256, W<=1/Q+16/M<=1/Q+2/sqrt(M). If Q>M/4, W<=5/sqrt(M). If Q>M^(3/4), likewise W<=5/sqrt(M), since [1+ln(1+Q)]/Q^(1/3)<=1+ln2+3/exp(1)<3. In the remaining domain β<=1/256, Q<=min(M/4,M^(3/4)); put x=Q/t,y=M/Q. Then x<=Q<=y³, and

    ln(1+x)<=24 ln(1+min(x,y)/8).

For x<=y use log concavity; for x>y use 1+y³<=(1+y)³ followed by concavity. Thus W<=1/Q+24 L, where L is BC4 without c_B. Combining the three separate minimax inequalities, not summing risks of different sources, proves (BC1)'s lower with

    c_arch=min{c_S/5,c_I/2,c_B/48}.

All Q,β in the declared finite domain are covered; BC4 is not extrapolated.

## 5. Exact finite upper membership — zero purity is preserved

Construct the complete eight-coordinate triple histogram. At historical position i use the eight bits

    v_abc(i)=1{(X_(i-2),X_(i-1),X_i)=(a,b,c)}, a,b,c∈{0,1}.

Trailing windows are padded publicly at i=1,2. This is a paid radius-three finite table with exact 0/1 entries. Under the separately enlarged affine row-sum-three budget, an alternative from six local one-hot bits computes each triple bit as ReLU(u+v+w-2); all integer coefficients, additions and outputs are exact in FA's signed fixed grid. The predecessor features are supplied by the paid local input window, NOT singleton heads sneaked into the dense causal family. Local table generation/lookup is charged. Choose the synthetic initial state identically zero: terminal query bits are unnecessary for this head, and S is used only by the decoder. Width 16 accommodates eight old triple-feature slots and eight head-output slots; no extra query slots are required. A larger budget may carry unused terminal pair query bits, with their actual storage paid.

Use one head with Q/K projections identically zero, no bias, values the eight bit coordinates. Its logits are exactly zero on every edge. Let K_1={1},K_2={1,2}, K_t={3,...,t} for 3<=t<=N, and K_n={3,...,N}. These masks are public, causal, boundary-independent and satisfy |K_t|>=t/3. Set the update to exact concatenation/projection of the eight attention outputs; readout is coordinate projection, padded with exact zeros if necessary. Additional fixed layers copy these coordinates through identity updates and ignore their zero-valued heads. All states/values lie in [0,1], all parameters are integers in {-2,-1,0,1,2}, attention scores are zero, and the stated fixed budget suffices. Local lookup has bounded diameter on all formal histories. No historical dependence on terminal S occurs.

Importantly this construction uses the UNCHANGED FA001 evaluator, not an alternative weight cache. Its positive score shift is a fixed integer a_shift; every finite zero score is exactly zero, so every edge obtains the SAME positive Taylor integer W_*. It need not equal d_f or one. Values are encoded exactly as V_i=d_f v_i. At terminal n, if C_abc is the triple count among the M keys, the exact signed accumulators are

    Z=M W_*, N_abc=W_* d_f C_abc,
    O_abc=floor(N_abc/Z)=floor(d_f C_abc/M).

Positive W_* cancels exactly before the only quotient floor; no approximate exponential identity is needed. Concatenation, coordinate projections and identity padding all use exact zero/one coefficients and preserve these grid values. For integer k=d_f/Q,

    floor(O_abc/k)=floor(Q C_abc/M).

This nested-floor identity follows by Euclidean division or floor(floor(kx)/k)=floor(x). Therefore the actual exported bank is EXACTLY the downward-Q-quantized uniform histogram. In particular count zero produces exact zero, count M produces exact one, and no minority coordinate is invented by approximation. A generic E/Q envelope alone would not establish the purity needed for BU001's improved rounding lemma.

The decoder uses S only to select the two coordinates of the actual terminal pair AFTER quantization. If their integer sum is positive, normalize them; otherwise use the uniform binary vector. Apply ordered binary simplex Q-rounding, costing at most 1/Q TV. No count C, denominator M W_*, unquantized row mass, clean empirical probability, β, Π, return time or exit parameter crosses the cut. This is exactly SB001's histogram decoder at κ=1, with exactly the same input labels; it is not an assertion that the entire encoder implementation equals SB001.

Accepted BU001 v2 consequently applies verbatim at z=Q:

    risk_stat <= min{1,2^17/sqrt(M)+3/Q+544 W(Q,t)}
              <= min{1,131619 F}.

The imported proof uses stationary reversal, weighted return-time tails and the special diagonal-row purity inequality; it supplies no arbitrary-start claim. Equality of the actual histogram labels is the justified bridge to that proof.

## 6. Complete paid resource certificate

The selected encoder is the compact sequential multi-tape FA001 v3 evaluator, not a unit-cost RAM. Let n=M+3, b_p be actual maximum dyadic-description bitlength, U actual count of supplied numerical records including local/position tables and any fixed-count duplicates, F_pub actual public mask/metadata bitlength, and q=ceil(log2(n+1)). With P_f above use

    w=O_arch(P_f+q+log(P_f+1)+log(U+F_pub+2)).

For explicit fixed-width data U=O_arch(n²), F_pub=O_arch(n²+nq), and here b_p=O_arch(1) for numerical coefficients (indices/metadata remain separately paid). Materialize fixed tables, padded masks and metadata by public nested loops, charging O_arch((U+F_pub)w²) bitwork conservatively and their full stored volume. No logarithm generator or external source-dependent generator is needed. Every table entry and dense zero coefficient is written and read.

Retain and charge the complete FA schedule: descriptions Ub_p+F_pub; parameter conversion O_arch(U(b_p+P_f)²) work and UP_f converted compact records; all n tokens' QKV/projections and n² candidate-edge scans including masks, Taylor recurrences even though equal weights could be reused, full signed products and log n guard bits, exact accumulations and row quotients, affine/ReLU updates, local-window scans and boundary acquisition, tape scans/rewinds/copies/clears, output serialization, and O_arch(w^4) finite-control/microcode construction/storage. The encoder forward work is O_arch(n²(P_f+1)w²); numerical rolling arrays/scratch are O_arch(nw). A safe retained-data peak is

    S_enc=O_arch(Ub_p+UP_f+F_pub+n+nw+w^4+b_p+P_f).

This includes all simultaneously live public records, masks, input, code, outputs and workspace, not only rolling activations. Public records use P_f+O_arch(1) bits, not w-bit padded slots; scratch and hidden records use w-bit slots. Choosing padded records instead replaces UP_f by Uw, including writes/clears. Data are supplied/generated in FA's declared sequential order; any alternate layout pays reformatting. Integer division includes negative-floor sign correction even though this witness's final sums are nonnegative. No n² numerical attention matrix is retained.

Pay decoder computation at every token (using that token's own exact local endpoints), retain/write the complete all-token eight-coordinate bank and output rows, and export only the terminal prediction. Historical outputs have no path to the terminal decoder. An explicit conservative implementation inherits SB001 v2 §6's COMPLETE addressed ledger at κ=1 as an overcharge: n=M+3,K=2, ell=ceil(log2(n+K+2)), k=1, b_d=64(h+ell+k+1),

    T0=O(n² K^6 b_d²),
    S_d=O(n²+n K³ b_d+K^6 b_d+b_d²),
    forward work O(T0 S_d b_d), forward peak O(T0 b_d+S_d),
    offline work O((T0+S_d)b_d²), offline peak O(T0 b_d+S_d+b_d²).

Only its pointwise suffix is needed; charging the complete bounds is a safe upper, NOT execution of singleton heads as part of the new architecture. The suffix scans the eight bank coordinates, muxes the terminal-pair block, adds, checks zero, uses a selected positive divisor, normalizes, ordered-rounds and serializes. Its full products use 2b_d bits and guarded temporaries <=4b_d+4. Addresses/opcode records, all-token work, dense zeros, holds, copies, clear/reset and construction remain paid. Implementing merely the suffix cannot exceed this full finite program's operation/storage budget, and input-bank conversion writes O_arch(n(b_d+w)) bits.

A conservative composed certificate ADDS encoder data/work/code, decoder data/work/program and conversion volumes; take the maximum of the full simultaneous sums over generation, conversion, forward and cleanup phases. Do not take minima of separate implementations' peaks. At the cut disable all decoder access to history/hidden/QKV/numerator tapes; release or explicitly zero dead numerical data with their full O_arch(nw+UP_f) writes charged. Boundary S and final grid bank are the only data-dependent retained ports. This is an abstract access convention, not an uncharged physical isolation device.

If PURE expansion is desired, separately unroll the actual COMPOSED bitwork T_bit and live bits S_bit: depth O(T_bit), width O(S_bit), O(T_bit S_bit) sparse gates/holds and O(T_bit S_bit²) dense slots, with full finite coefficients, index lengths, generation and rolling storage paid. This does not preserve fixed attention depth or justify mixing PURE/compact/addressed resource minima. No runtime/memory optimality, trained attainability or fixed-total-bit claim follows.

## 7. Consequences, provenance and stopping boundary

At κ fixed (here no tunable growing score range), statistical-order stationary risk is possible exactly when, up to fixed target multipliers,

    Q ≳ sqrt(M)[1+ln(1+1/(sqrt(M) max(sqrt(β),1/M)))].

This follows from BC1 by BS001 §5's scalar inversion with z=Q; the RHS already dominates sqrt(M). Necessity is for every fixed target multiplier, while sufficiency is for a sufficiently large fixed multiplier. β=1/M permits Q≈sqrt(M), whereas β<=M^-2 requires Q≈sqrt(M)log M. The larger-alphabet CF001 cutoff remains β, not sqrt(β), in its own stationary/arbitrary-start theorem.

Direct source/receipt hashes are recorded in BC001_source_bindings_v1.json. Status headings in old proofs are superseded only by their exact version-specific acceptance receipts. Numerical diagnostics are finite corroboration, not proof; independent review is separate from root acceptance and external peer review. This work is standalone post-stage-5 research and changes no accepted proof, frozen bundle or paper_v3. The improved arbitrary-start binary frontier remains OPEN. No external publication, upload, novelty-priority assertion or user contact is undertaken.
