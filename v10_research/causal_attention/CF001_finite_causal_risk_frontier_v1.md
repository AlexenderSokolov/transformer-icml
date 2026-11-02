# CF001 — A finite-arithmetic fixed-depth causal encoder risk frontier

2026-11-02. Root synthesis and constructive-membership candidate; independent review pending. CA001 v3 and FA001 v3 are separately accepted. This file proves the remaining concrete upper membership and states a temporally causal subclass, rather than claiming every branch-conditioned scheme is an ordinary causal Transformer.

## 1. Exact finite family and theorem

Fix K>=3, M>=64 and Q=2^h with integer h>=4. The source, hidden all-state two-step D2(beta) certificate and actual-terminal expected-TV loss are exactly those of FR001, with beta in [0,1]. Let N=M+2 and n=M+3 include the appended synthetic query position.

Fix an architecture budget independent of M,Q: depth, heads per layer, dimensions, number of affine/ReLU operations per position, local preprocessing radius, uniform coefficient/range/Lipschitz bounds and output dimension D. The budget permits at least the explicit prototype in Section 3: one global block, four statistical heads, local radius three, state width 12K+4, output D>=9K+1 (surplus coordinates zero), affine row-sum bounds at least two, state bound at least one, score bound at least two, and the corresponding score Lipschitz bound at least 4K. Longer fixed depths may pad with identity updates and unused zero-valued heads. Each chosen network must separately obey all of its stated uniform bounds; budget capacity alone does not certify arbitrary parameters.

Admissible ideal encoders are the finite-data affine/ReLU subclass of FA001 v3, with public causal masks having density at least c>0; allow c<=1/3 to include Section 3. Initial history states use fixed-radius causal local tables. Historical tables, parameters and masks are independent of future source symbols. The exact side field S consists of the first and last three observed symbols (or a fixed larger boundary window allowed by the architecture budget). Dependence on S is confined to the appended terminal initial query; the decoder may also read S. This restriction makes the composed predictor end-to-end history-causal. Arbitrary S-dependent historical parameter branches from CA001 Section 7 are NOT being advertised as temporally causal here.

Every ideal numerical datum is a supplied finite dyadic with actual description length charged. Encoding is performed by FA001's signed-integer compiler with target precision parameter h+3, then the final vector is rounded downward at the requested resolution Q. Thus its fractional precision is P=4(h+3)+C_arch, and its accumulator width additionally pays log n. The compiler's stored public parameters use the declared compact P+O_arch(1) slots; its alternative padded format has different charges. All histories, including formal inconsistent boundary histories used for the proof, must satisfy the component bounds. Intermediate layer normalization and arbitrary unevaluated nonlinear maps are not included.

The cut contains precisely the resulting D grid coordinates, S and public metadata. No clean pre-cut state, numerator, denominator, residual, historical output or raw-history reread is supplied. The post-cut decoder may compute arbitrarily, use source-independent common randomness and return any real simplex vector. Its computational costs, if a particular decoder is implemented, are separate from the information lower. All encoder/decoder choices are source-law-independent; they may know the public class promise beta. Let R_C,stat and R_C,all optimize both encoder and decoder in this specified finite family, for hidden-stationary and arbitrary initialization respectively.

Write

    beta0=max(beta,1/M),
    W=[1+ln(1+Q/(M beta0))]/Q,
    H=max(M^(-1/2),W).

There exist explicit positive constants c_arch and C_K, independent of M,beta,Q, such that

    c_arch H <= R_C,stat <= R_C,all <= min(1,C_K H),          (CF1)
    C_K=2^16 K^(5/2)+2^14 K^3+5320K^5.

The upper is attained by one beta-blind finite encoder/decoder family, different in its evaluated prefix from the original SRC program. No equality of its quantized labels with the original prefix is asserted. This proves a fixed-budget, fixed-depth finite-arithmetic encoder-class rate, not a theorem for all Transformers, growing depth or vanishing normalization constants.

## 2. Lower after a proved finite compiler

FA001 proves, not assumes, that every compiled vector is within 2^(-(h+3))=1/(8Q) of its ideal vector uniformly in every formal history. CA001's complete-message tube proof therefore applies with E=1/8; we may safely relax to E=1. Intermediate rounding need not be Lipschitz. The uniform end-to-end approximation and the enlarged final tube, not identical grid labels, justify the transfer.

Use CA001's constants C0,Gamma,Lambda after the fixed local-radius and mask-density adjustments, and H_b for the finite number of possible witness boundary values (H_b=3^6 suffices for the stated six-symbol side field). Put

    tau=sqrt(5 D H_b) max(Gamma,sqrt(Lambda)),
    N_E=ceil(2tau+6)+1,
    A_s=H_b(2+Gamma)N_E^D,
    A_I=H_b(2+C0)N_E^D,
    c_1=1/(8192A_s), c_2=1/(256A_I).

All are uniform architecture constants. The frozen-branch proof is valid on the larger side-conditioned family, so it remains valid on our temporally causal restriction. It yields the same stationary source witnesses as CA001:

    R_C,stat >=1/(128sqrt(M+2)) >= M^(-1/2)/256,
    R_C,stat >=c_2/Q,
    R_C,stat >=(c_1/Q) ln(1+min{Q/(M beta0),M/Q}/8)
                  for beta<=1/16.

These are simultaneous separate minimax inequalities, not a sum of risks attained by one source. Optimizing a source-independent randomized encoder is permitted: CA001 uses the same prior after conditioning on each source-independent seed and averages before the source supremum.

For completeness the all-Q scalar completion is as follows. If beta>1/16, W<=1/Q+2M^(-1/2). If Q>M/4 or Q>M^(3/4), W<=5M^(-1/2), using ln(1+x)<=4x^(1/4) and M>=64. In the remaining domain put x=Q/(M beta0), y=M/Q. Since x<=Q and Q<=M^(3/4), when x>y one has x<=y^3; hence ln(1+x)<=3ln(1+min(x,y)). Bernoulli's inequality gives ln(1+t)<=8ln(1+t/8). Thus W<=1/Q+24 ln(1+min(x,y)/8)/Q there. Consequently

    c_arch=1/max{1280,1/c_2+512,1/c_2+24/c_1}

proves the lower in CF1, with no extrapolation of a tube or deletion of its second cutoff. The stationary inclusion gives R_C,stat<=R_C,all.

## 3. A concrete ideal prototype in the subclass

We now verify an admissible upper witness; it is not assumed merely from the phrase 'contains SRC'. Use the four ideal statistical maps P1,P2,T,0 from the original SRC construction. Historical initial features are local bits from the triple (X_(t-2),X_(t-1),X_t), with the public first-key flag z_t=1{t=3} and F_t=z_t e_(X_2). Early rows use the original predecessor/self fallback, which is a public position-dependent radius-three table. Every table entry is zero or one. At the terminal synthetic position, x_n=0, the two lag/query one-hots are the actual last pair from S, and flag features are zero. This is the only use of terminal S within the encoder's historical computation.

At every statistical row the allowed keys are 3,...,min(t,N) when t>=3, and self otherwise. These public masks do not depend on S. Their sizes are at least t/3 for M>=64; at t=3 equality holds, at t=1,2 self is adequate, and at t=n the size is M=n-3>=n/3.

Generate the original finite downward dyadics L2,L3 approximating ln2,ln3, with

    p0=4h+4ceil(log2(M+K+4))+64,
    0<=ln2-L2<=2*2^-p0, 0<=ln3-L3<=2*2^-p0.

Their finite rational-series generator and all of its public data/bitwork are inherited as a paid subroutine from SRC; no real logarithm oracle is introduced. Choose the following IDEAL real-softmax score/value maps, with these supplied dyadic coefficients:

 P1: score=L2*1{lag2=queryfirst}+L2*1{lag1=querysecond}; values=(token,lag2).
 P2: score=L2*1{lag2=queryfirst}+L3*1{lag1=querysecond}; values=(token,lag2).
 T:  score=L2*1{lag2=querysecond}; values=(lag1,F).
 0:  score=0; values=(lag2,lag1,F,z).

The equality bits are dot products of one-hot query and key subcoordinates, so these scores are affine Q/K projections followed by dot product, not nonlinear uncomputed matching or hard masks. Values are linear coordinate projections of the local bit state. Scores lie in [0,ln6] subset [0,2], values in [0,1], and all formal frozen-query histories preserve these facts. On bounded reachable states, score differences are bounded by 4K times the sum of maximum-norm state differences, a conservative bound from the 2K-term dot product. Projection row-sum norms are at most two. Initial state diameter is at most one, and a concatenation of the four head outputs has maximum norm at most one and update Lipschitz constant one for the sum norm on head inputs.

Use one affine concatenation/projection update to place these 9K+1 outputs in the state, then a coordinate projection readout (and zero padding if D is larger). Width 12K+4 is more than sufficient. For a greater fixed depth, subsequent updates copy the state exactly and ignore zero-valued attention heads; their masks may be full causal masks. All fixed primitive bounds remain satisfied. Thus this is a genuine instance of the chosen ideal affine/ReLU family. No historical parameter is selected by the actual future boundary; only the appended query reads S. The ideal network is temporally causal.

## 4. Compiled master accuracy and the NB002 suffix

Compile Section 3 with FA001 at target h+3. Its pre-cut vector is within 1/(8Q) of the ideal dyadic-coefficient softmax vector on every history. Coordinatewise final downward Q-rounding adds less than 1/Q.

Compare the ideal dyadic-coefficient head to SRC's ideal TRUE-log head, which appears in the deterministic frequency identities. Each score changes by at most 4*2^-p0. The softmax differential gives an L1 probability-weight change at most twice the maximum score change. Since values are bits, each output coordinate changes by at most 8*2^-p0<=1/(8Q). Therefore every new actual master differs from the original ideal identity value by less than

    1/(8Q)+1/Q+1/(8Q)=5/(4Q)<2/Q.                  (4.1)

The actual master also lies in [0,1] on the closed Q-grid, not merely near that interval. All initial feature/value bits are exactly represented. The value projection uses only coefficients zero or one, so those values remain exact bits. Positive Taylor weights and exact weighted sums yield head outputs in [0,1] after downward fine-grid rounding. Concatenation, identity padding and coordinate projection use exact zero/one coefficients and do not alter those grid values; final coarse rounding preserves [0,1]. Exact query, endpoint and permitted initial-flag side fields come from S and public metadata, not from approximate head values.

Use the same finite NB002 decoder map on these new masters. Its actual deterministic proof requires precisely closed [0,1] grid masters within 2/Q of the ideal four-head values, exact permitted side bits, and its stated full-word arithmetic. It does not require the old particular exponential recurrence once that head bound is established. The unchanged all-path error ledger gives recovered row-frequency error <=76/Q and pooled-frequency error <=6/Q. These imply the same probability-vector errors, observable radius inflation, monotone rejection containment and pre-integration bound used by NB002/AU001. No independence of numerical errors is assumed. Inspecting NB002 Sections 2–6 establishes this transfer; it is not an inference from a final scalar risk bound.

Consequently the newly compiled encoder followed by that decoder obeys AU001's bound

    risk_all <=min(1,2^16 L_stat
                    +(2^14K^3+5320K^5)W),

where L_stat is R011's common statistical scale, and L_stat<=K^(5/2)/sqrt(M). This proves the upper constant C_K in CF1. The whole program is NOT the identical original NB002 program: its statistical head evaluator was replaced, while its downstream map and deterministic accuracy envelope are retained. Equality of branch decisions with ideal ALG or equality of old and new master labels is neither needed nor claimed.

The decoder is applied/charged at all token rows as in NB002, using each row's own exact local endpoints and the public parameters; only the final row is the requested prediction. Such other rows need not have the final-row statistical interpretation. Keep their own local acquisition data only as needed for their causal pointwise suffix, then release all unused historical arrays. The final decoder receives only the final grid bank and S. There is no edge from a historical clean numerator or any other token's output to that decoder.

## 5. Full resource and interpretation lock

The encoder pays FA001's actual sequential finite-data implementation: all supplied dyadic descriptions and public masks/tables, their conversion, compact converted records, all-token QKV and edge scans, full signed products and length-dependent accumulators, row quotients, affine/ReLU maps, boundary acquisition, tape moves/rewinds/copies/clears, code/control, actual format writes, generator work and simultaneous phase peaks. Its internal fraction P=4(h+3)+C_arch is not its complete word: full words also pay log n and fixed range/guard allowances. Original input description bitlength B_param remains separate.

For this witness the finite L2/L3 generator adds the actual SRC cost O(p0^3 log^2(p0+1)) and associated code/scratch/output writes; it is not included for free in FA001's supplied-data option. Local table or mask materialization must pay its actual expanded volume. A fixed causal local-copy/gate implementation may replace a table only with its own charged realization; no cheaper convention is silently selected.

The post-cut NB002 arithmetic and every token's pointwise execution are then added with their full existing charges: its p0 word-size parameter, <=128p0 complete products/guards, dense zero-inclusive coefficients, explicit holds, normalized/output banks, controller/addresses and all-token work. A conservative composition adds both implementations' work and retained-data volumes, counting simultaneously live encoder outputs, S and decoder inputs together. Shared buffers may be reused only under an explicit lifetime schedule, not by taking minima of separate peaks. For exactly D output coordinates, added zero pads cost their actual D grid-word storage/writes and architecture-index widths; these are included in FA001's dimension-dependent budget. No claim reuses an unaugmented numerical six-head or p0 ledger for arbitrary added dimensions.

PURE expansion, if chosen, uses the composed actual bitwork and live memory, pays all identity holds/dense zeros/coefficients and offline generation, and has its own larger depth/width bounds. It is not a fixed-depth finite scalar Transformer merely because the ideal encoder had fixed attention depth. The mathematical encoder family is a finite evaluator of a fixed-depth ideal architecture with certified error; this distinction is essential.

The result does not prove trained attainability, optimal joint-K rates, optimal runtime/memory, all-depth impossibility, or equality of complete resource costs across encoders. It permits no free nonlocal history statistic before or after the cut. Finite boundary branches used in the lower proof are a stronger side-information argument; only the terminal-query-dependent subclass is called temporally causal here. Known bounded-attention sensitivity, finite-message and rare-context ideas remain prior art. The source-bound corrected-Hahn/Chiang–Cholak comparison is retained; no novelty certification is made.
