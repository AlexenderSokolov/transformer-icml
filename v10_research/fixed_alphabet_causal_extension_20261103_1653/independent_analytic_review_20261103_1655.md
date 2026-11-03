# Independent analytic review: fixed finite-alphabet extension

**Disposition.** No mathematical defect found in the stated architecture, numerical error bounds or resource upper bounds, subject to the exact-arithmetic model and the inherited R011 statistical theorem. The latter's theorem statement and review were checked against the actual hash-matching files; their deep dependencies were not independently reproved here. This is not an implementation test, formal verification, novelty certification or training result.

## Bound inputs and method

- Candidate `alphabet_extension_candidate_v1.html`: SHA-256 `f0a9621a62655aaa41cf4c45fcfcf183580511ed52465be1bf11b988e45e24ff`.
- All-alphabet statistical proof `../../cloud_work/conditions-20261028/research/resume_20261030/R011_global_rates_and_constant_adaptation_v1.md`: SHA-256 `aaafd3823ab11e20ffdeff2164115c6c91db5efea6e2dffd9c3c78da0b7fbbbf`.
- Independent statistical review `../../cloud_work/conditions-20261028/research/resume_20261030/R011_independent_review_v1.md`: SHA-256 `5afb4c07939f861db02a6aafdd25bf51e94f8ad799848119e37aba67aefd539a`.
- The binary fixed-point backend and Gaussian lemma have respective SHA-256 `e532e78809c4edf7d4e47ec39ad548c06ad339c55e9f56b8d75a85ea86a7143b` and `d21062d3d1bf660a955bba10df9c466cf0eabaa61e57251236b8a870e15f9ad7`; see the separate backend review `../four_block_integer_backend_20261103_1645/independent_analytic_review_20261103_1655.md`.

Method: analytic source comparison, derivations and SHA-256 checks. No numerical or random experiment, enumeration, simulation, or scientific-code execution. No source document was modified.

## 1. Model capacity, heads and gates

With m=ceil(sqrt(A+10)), D=4m² and A²+1 allocated heads, scaled scores have divisor sqrt(D)=2m and D≥A. The reserved-coordinate count is exactly A³+2A²+7A+8: A³ anchor coordinates, two A² context/query blocks, seven A-vectors, four position inputs, three flags and z. The chosen d_model=(A²+1)D exceeds it. Q/K factors sqrt(D) are integers depending only on A, so all intended scores are realized without irrational weights.

Two block-1 heads perform the advertised lag copies, with componentwise snap implemented by four ReLUs per symbol across the two heads. The two flags b and v use two hidden units each and m uses one, for 4A+5. Block 2 has one hidden ReLU per context for g and one for q, or 2A² total. At valid candidate positions the snapped coordinates are onehots, so the unique pair gate equals 1; at invalid positions v=0 and T coordinates lie in [0,1], so every g is 0. At the terminal position q is the unique actual terminal pair. Block 3 uses A² anchor heads and one zero-score marker head; selecting p requires A³ ReLU units before the affine sum over heads. Block 4 uses A heads. The total A²+A+3 active head instances agrees with the candidate. For fixed A all weight values and widths are independent of N; positions and arithmetic precision are not bounded uniformly in N.

## 2. BOS, count indexing and boundaries

At positions 1,...,A the BOS values sum to the all-ones A-vector, contributing +1 per symbol and +A in the denominator. At i=A+k, k=3,...,N, the predecessor pair is (X_(k−2),X_(k−1)) and the value is X_k. Thus exactly M=N−2 observed departures are counted, from k=3 through k=N; the terminal pair (X_(N−1),X_N) is the query, and X_(N+1) is not observed. Nonmatching data have score 0, while every BOS and matching candidate has score N. Their weighted mixture gives o_h=(C_h+1+e^(−N)D_h)/(J_h+A+e^(−N)K_h) with K_h=N−J_h and D_h a nonnegative vector summing to K_h. Its TV distance to B_h=(C_h+1)/(J_h+A) is at most e^(−N)K_h/(J_h+A+e^(−N)K_h)≤Ne^(−N)/A. The uniform marker has exactly one unit value among L keys and returns 1/L before numerical rounding.

At N=2 there are no candidate triples; B_h is the uniform distribution. Terminal lag-one copying still targets the first data token, and the exact real or rounded anchor can differ from uniform because unmatched data retain nonzero weight. The displayed bound, rather than an equality claim, handles this boundary. R011 starts at M=1 and must not be applied there; the candidate correctly uses TV≤1 at N=2.

## 3. Gaussian-to-simplex conversion

For each a the linked Gaussian lemma gives |G_a/L−p_a|≤42/sqrt(L) uniformly, including p_a=0 or 1. Let u_a=G_a/L, δ=sum_a|u_a−p_a|≤42A/sqrt(L), and S=sum_a u_a. The simplex property gives |S−1|≤δ. If δ≤1/2, TV(u/S,p)≤δ/(1−δ)≤2δ; if δ>1/2, TV≤1. This proves the conservative min{1,84A/sqrt(L)}. It is essential that p is a simplex; in the numerical algorithm this is enforced before taking the Gaussian heads.

## 4. Finite-bit error budget

For each rounded anchor, the first A−1 coordinates are floored and the last is the residual. Since the unrounded normalized distribution is nonnegative and sums to one, the residual remains nonnegative. Each of the first A−1 decreases by less than 1/H_grid; the last increases by their sum. Consequently the rounding TV cost is at most (A−1)/H_grid. The repeated-squaring primitive gives absolute unnormalized error ε_w per weight and preserves a maximum weight of 1; standard normalization then gives TV≤Lε_w for anchor weights. The q selector is exact at the terminal, so p̃ is an exact grid simplex and obeys the advertised bound.

The first-BOS head yields z̃=floor(H_grid/L)/H_grid. Holding p̃ fixed while comparing z̃ against 1/L gives every Gaussian score error ≤L²/H_grid. The softmax TV inequality and the range λ_j∈[0,s+1] give at most (s+1)L²/(2H_grid); numerical weights, log-feature error and output floor give the remaining terms in E_h. This avoids any need for a Lipschitz estimate comparing p̃ to the real anchor before invoking the uniform Gaussian lemma. For A-way final logits, the score-vector l-infinity perturbation E_h gives conventional TV≤tanh(E_h/2)≤E_h/2, independent of A. Applying the weight routine to the final A logits gives TV≤Aε_w; the same residual rounding costs at most (A−1)/H_grid. Adding the errors gives exactly the candidate's numerical TV inequality.

## 5. All-A statistical source and growing-A distinction

R011 explicitly fixes every K≥2 and M≥1, an arbitrary initial pair law, all-state P² minorization, all observed X_1,...,X_(M+2), and unconditional expected half-L1 error at the actual terminal row. Its original K-letter add-one rule counts precisely j=0,...,M−1. Set K=A, M=N−2 and n=M+1=N−1. At β_mix=0, any finite pair kernel admits a stationary distribution and P²≥0 is vacuous; hence the class contains every homogeneous table and every initial pair law. The stated H=g=min{1,sqrt(A⁵/(N−1))} and original-risk bound min{1,2¹³ sqrt(A⁵/(N−1))} follow. This is an inherited theorem, not a new proof of its dependency chain.

For fixed A the resulting risk is O_A(N^(−1/2)). If A=A_N varies, A_N⁵/N→0 implies both the inherited risk bound and 84A_N/sqrt(N+A_N) vanish. The explicit numerical terms vanish as well: H_grid=2^(32 ceil(log₂(AL)))≥(AL)^32 and A≤L, while the numerators are polynomial in A,L and log(AL). This is a sufficient, non-sharp growth condition with a different A-dependent network at each A, not one fixed-width/fixed-weight network across the sequence.

## 6. Resource checks

The two copy heads and A² anchor heads use A-vector values, giving O(A³L²) scalar value-aggregation work; all attention dot products have total dimension O(A³), so the same bound covers dense pair scores. Their A²+O(A) exponentials per pair and L position-log computations give O((A²L²+L)b³). Dense projections and width-A³ FFNs on d_model=O(A³) cost O(A⁶L) scalar operations. Using schoolbook O(b²) arithmetic yields the displayed O((A²L²+L)b³+(A³L²+A⁶L)b²). Position/residual storage is O(A³Lb); streamed rows avoid L² storage, and bounded multiple-precision scratch is O(b²). A dense O(A⁶)-entry parameter set with O(log(A+2))-bit coefficients costs O(A⁶ log(A+2)) bits. These are upper bounds; they are not asserted optimal. Assumptions include exact masks, exact integer arithmetic, horizon-dependent precision and sufficient range, rather than ordinary fixed-word IEEE behavior.
