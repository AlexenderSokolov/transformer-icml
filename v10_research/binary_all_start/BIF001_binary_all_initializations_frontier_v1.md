# BIF001 — Binary frontier for both stationary and arbitrary initialization

2026-11-02. NEW author candidate v1; fresh independent review and root acceptance required. All imported version-specific ingredients are root accepted. This file does not change them, paper_v3, or any delivery freeze.

## 1. Experiment, interfaces, and results

Fix K=2, M>=64, integer κ>=1, and dyadic Q=2^h, integer h>=4. Observe X_1,...,X_(M+2) from a homogeneous second-order source. Write Y_j=(X_(j+1),X_(j+2)), 0<=j<=M. The source has a hidden stationary probability Π with the ALL-STATE certificate P²(i,j)>=βΠ(j), 0<=β<=1; unsupported starting states are included. In the arbitrary-start experiment Y_0 has ANY distribution μ. The stationary experiment restricts μ=Π. Loss is expected TV from the source row at the ACTUAL terminal pair Y_M. No independently resampled query is used.

First take exactly BS001 §1's one-block family: fixed D>=8,r>=3; trailing local r-windows L_i at i=3,...,M+2, public padding; exact boundary S consisting of first/last min(r,M+2) symbols with consistent overlap. The at-most-D retained ratios are

 B_d= sum_i w_di(L_i,q(S))v_di(L_i,q(S)) / sum_i w_di(L_i,q(S)),
 Z_d=floor(Q B_d)/Q,

with actual weights 1<=w_di<=κ and |v_di|<=1. Tables may depend on position, coordinate, public promises and source-independent seeds, but not source law or nonlocal interior history. q is a function only of S. All M keys have positive weights. The decoder sees ONLY Z,S,public metadata and source-independent randomness and may return an arbitrary real simplex vector. No additional exact interior port, denominator, history reread, hard selected-key mask, or recursive global block is permitted. Real weights in the envelope are allowed in the lower-bound family; the upper uses {1,κ}. Mathematical padding to D is an inclusion, not free physical storage.

Set

 e0=max(sqrt(β),1/M), t=M e0, z=κQ, s=M^(-1/2),
 W(z,t)=[1+ln(1+z/t)]/z, F=max{s,1/Q,W(z,t)}.

Let R_stat and R_all be minimax risk in this SAME family for the two initialization experiments. Let T_SB be the unchanged accepted SB001 finite predictor. Then

 c_(D,r) F <= R_stat <= R_all <= risk_all(T_SB)
 <= min{1, 2^17/sqrt(M)+3/Q+2^17 W(z,t)}
 <= min{1, C F},                                      (BIF1)
 C=2^18+3=262147.

Here c_(D,r) is EXACTLY BS001 §1's positive explicit constant min{(1/256)/5,c_I/2,c_B/48}, with c_I,c_B defined there. It is independent of β,M,κ,Q. This use of the accepted lower theorem includes its complete finite-domain proof, summarized in §6 below. The new content is the arbitrary-start upper. For stationary initialization, the sharper accepted BU001 constant 544 on W remains valid; (BIF1) uses a common envelope for both experiments.

There is also a second, distinct family: exactly BC001 §1's fixed-depth bounded-score temporally causal FA001 finite evaluators, with its capacity and masks, cut and paid costs. Define R_C,stat and R_C,all for that family. With F_C=max{s,W(Q,t)},

 c_arch F_C <= R_C,stat <= R_C,all <= min{1,C F_C}.     (BIF2)

The lower constant is exactly BC001 §4's c_arch. The upper follows from its EXACT historywise κ=1 uniform-histogram labels, not from approximate closeness or an assertion that the two implementations coincide. Section 8 spells out this distinction.

## 2. Support classification: no missing positive-β boundary

Write W0=00,A=01,B=10,C0=11 and parameters

 a=θ_00(1), b=θ_01(1), e=θ_10(0), t_exit=θ_11(0).

(In the occupation argument only, use t_exit, not the scale t=M e0.) Stationarity gives Π=(y,x,x,w), ya=xe and wt_exit=xb.

For β>0 and x>0, P²(B,A)=ea>=βx and P²(A,B)=bt_exit>=βx. Thus a,b,e,t_exit>0. The stationarity identities imply y,w>0: stationary support is full. This uses the certificate on ALL starting states, not merely its supported restriction.

If x=0, stationary support lies on the diagonal. Every supported diagonal is absorbing by ya=wt_exit=0. Two absorbing diagonals cannot both have positive stationary mass, because P²(00,11)=0 would contradict βΠ(11)>0. Hence Π is a singleton absorbing diagonal. Accepted BAI003 v2 applies to arbitrary remaining rows and ANY initial state; no transient-start case is lost. At β=0 this classification is unnecessary: use the universal weak-β upper in §5.

## 3. Full-support occupation: complete composition

For a full-support positive-β kernel, let q=(a,b,e,t_exit), the TRUE chosen exit probabilities, and J_u(m)=sum_(j=0)^(m-1)1{Y_j=u}. For A0>0 set

 V_m=sum_u 1{Y_m=u} min(q_u,A0/(J_u(m)+2)).

IMPORTANT: q_A=b,q_B=e, NOT the unit crossing caps used in BU001's stationary occupation lemma. BAI004's UNIT-cap crossing bounds dominate these true-exit weights, while its crossing-start reduction needs these actual weights.

Assume βM²>=1 and M>=64; put G=1+ln(1+1/(sqrt(β)A0)). From a diagonal start W0, at ANY horizon m>=8 the four terminal contributions are:

 * terminal W0: <=4A0/m, by BAI004 v5 §2's arbitrary-chain initial-equals-target reciprocal-return identity;
 * terminal A: <=40A0/m [1+ln(1+1/(max(sqrt(β),1/m)A0))], BAI004 §1;
 * terminal B: the same with 100, BAI004 §9;
 * terminal C0: <=8192A0 G/m, BOD001.

The first bound follows from min(q,A0/(J+2))<=A0/J on the target event, where J>=1. The middle two are valid even if βm²<1. Since max(sqrt(β),1/m)>=sqrt(β), their logarithmic factors are <=G. BOD001 does NOT require βm²>=1. Summation gives

 E_W0 V_m <=(8336A0/m)G.                              (3.1)

Symbol exchange gives the same bound from C0. Thus (3.1) holds for all suffix horizons used below, even those below 1/sqrt(β); there is no hidden cutoff-domain failure.

For crossing starts set h_cross=b+e-be. If h_cross<=s, BAI004 §6 gives E q_(Y_M)<=2(b+e)<=4s, hence E V_M<=4s. More explicitly crossing endpoints contribute at most b+e, and last-entry geometric sums give aP(Y_M=W0)<=e and t_exit P(Y_M=C0)<=b. The no-initial-diagonal premise holds for either crossing start; if an exit is zero its weighted contribution is zero rather than a division by zero.

If h_cross>s, let T_diag be the first diagonal hit and u=floor(M/2). Before that hit the chain alternates crossing states; each two-step block exits with probability h_cross. Hence

 P(T_diag>u)<=(1-h_cross)^floor(u/2)
 <= exp(-sqrt(M)/8) <= 3s.                            (3.2)

The last inequality follows by maximizing x exp(-x/8) at x=8: maximum 8/exp(1)<3, with x=sqrt(M). On T_diag<=u the suffix horizon m=M-T_diag is at least ceil(M/2)>=32. Full prior terminal count is at least suffix prior count. Strong Markov and monotonicity in that count yield

 E V_M <=3s+sup_(diag i,ceil(M/2)<=m<=M) E_i V_m
 <=3s+(16672A0/M)G.                                  (3.3)

The failure-event cost is <=1. This is a first-hit and actual-count argument, NOT a global mixing bound. The two crossing cases, the diagonal cases (3.1), and convex mixtures of four initial states give the common bound

 sup_μ E_μ V_M <=4s+(16672A0/M)G.                     (3.4)

No initial distribution is supplied to the program.

## 4. Deterministic decoder reduction for the correct row weights

Only the analysis changes. Let S_add be arbitrary-start actual-terminal risk of the accepted add-one predictor and B0=E[2/(J+2)]. Accepted SB001 gives

 S_add<=8192sqrt(32)/sqrt(M+1),
 B0<=2sqrt(32)/sqrt(M+1).

Here J=J_(Y_M)(M). For J>0, empirical chosen exit fraction p_hat and true exit q=q_(Y_M) obey
 E[1{J>0}|p_hat-q|]<=S_add+B0.

The selected row bank has mass ρ=κJ/[M+(κ-1)J]; its two floors n0,n1 and N=n0+n1 are exactly as in BU001 §4. For N>=1, writing n1=Qρ p_hat-f1,n0=Qρ(1-p_hat)-f0 with f0,f1 in[0,1), v=n1/N satisfies

 |v-p_hat|<=min(p_hat,1-p_hat),
 |v-p_hat|<=min(1,2/(Qρ)).

This remains true when the chosen exit is successor 0: simply exchange the two labels. Therefore for EVERY row, including A,B,

 |v-p_hat|<=min(p_hat,2/(Qρ))
 <=min(q,2/(Qρ))+|p_hat-q|.

For J>=1, 2/(Qρ)<=2/Q+6M/[z(J+2)]. Setting A0=6M/z, triangle inequality yields

 |v-q|<=min(q,A0/(J+2))+2/Q+2|p_hat-q|.

On N=0 the uniform fallback costs at most one. BU001's historywise floor calculation and universal terminal occupation give P(N=0)<=64/z+16/M, with no stationary assumption. Indeed N=0 implies J<4M/z, including J=0; use integer threshold ceil(4M/z) in the universal bound. Final ordered binary simplex rounding costs <=1/Q. Consequently, for ANY initialization,

 R(T_SB)<=2S_add+2B0+E V_M+64/z+16/M+3/Q.             (4.1)

The import is BU001's deterministic floor and universal count bounds, NOT its stationary reciprocal-occupation theorem. BAI003 v2 §7 independently records this exact all-rows extension.

## 5. Explicit constant and domain ledger

**Full support, βM²>=1.** Substitute (3.4) and A0=6M/z into (4.1). Since

 G=1+ln(1+z/(6M sqrt(β)))
 <=G_star=1+ln(1+z/(M e0)),

and e0=sqrt(β) in this case, the occupation-plus-64/z term is at most

 (100032G_star+64)/z <=100096G_star/z <2^17 W(z,t).

The statistical terms obey, using M>=64,

 2S_add+2B0+4s+16/M
 <=[(16384+4)sqrt(32)+4+2]s <2^17 s.                 (5.1)

This proves the displayed common upper in (BIF1) for this case.

**Singleton stationary support, βM²>=1.** Section 2 and BAI003 v2 give
 R<=min{1,2^17s+3/Q+1600/z}.
Since G_star>=1 and 1600<2^17, this is dominated by (BIF1), including arbitrary transient initial states and zero parameters in their rows.

**Weak certificate 0<=β<M^-2.** No support or row-positivity assumption is imposed. The unchanged arbitrary-start SB001 bound is

 R<=S_add+Psi(32/(M+1))+Psi(96/z)+3/Q,
 Psi(v)=v[1+ln(1/v)] for 0<v<1, and Psi(v)=1 for v>=1.

The continuous value at zero is 0. Use Psi(v)<=2sqrt(v) and
 Psi(96/z)<=96[1+ln(1+z)]/z. The statistical coefficient is (8192+2)sqrt(32)<2^17. Here e0=1/M and t=1, so this proves (BIF1) with room to spare. β=0 is included. The equality β=M^-2 belongs to the strong case; all its full-support suffixes are covered by §3 without imposing a strong suffix certificate.

These cases exhaust β in[0,1] and all stationary supports. Dyadic Q>=16, integer κ>=1 and M>=64 are precisely the implementation domain; auxiliary lemmas only require horizons >=8. The probability cap gives min{1,...} in every case. Since each term s,1/Q,W<=F, the total constant is C=262147. No claim of numerically useful or optimal universal constants is made.

## 6. Lower bounds and exhaustive frontier completion

Stationary sources with μ=Π are a subset of arbitrary-start sources, using exactly the same admissible procedure family. Thus R_stat<=R_all. Accepted BS001 proves cF<=R_stat from three separate lower witnesses, not their risk sum: c_S s with c_S=1/256; c_I/Q uniformly in every finite real κ; and c_B L only for β<=1/256,z<=M/4, where
 L=ln(1+min{z/t,M/z}/8)/z.

For clarity the necessary all-regime completion is as follows. W decreases in z. If β>1/256 then W<=1/Q+2s. If z>M/4 then W<=5s. If z>M^(3/4) then W<=5s, using [1+ln(1+z)]/z^(1/3)<=1+ln2+3/exp(1)<3. Otherwise β<=1/256 and z<=min(M/4,M^(3/4)). Put x=z/t,y=M/z; x<=z<=y³ and y>=4. For x<=y, log concavity gives ln(1+x)<=8ln(1+x/8); for x>y, ln(1+x)<=3ln(1+y)<=24ln(1+y/8). Thus W<=1/Q+24L. Taking maxima of the separate lower bounds gives c=min{c_S/5,c_I/2,c_B/48}. This covers every finite-domain case without extending the rare-suffix lower beyond its domain. Together with §§3–5 it proves (BIF1).

## 7. Unchanged one-block implementation and its complete cost meaning

T_SB uses two paid singleton-copy heads and paid local pair/triple features; the complete eight-coordinate one-hot triple bank uses weights κ on keys whose preceding pair matches the terminal pair and 1 on all others. Every coordinate is downward-Q-quantized BEFORE selecting the terminal two-coordinate row. Positive rows are normalized; zero rows use uniform fallback; final ordered simplex rounding is paid. All M keys remain. The only data-dependent retained ports are the grid bank and allowed boundary S. No β,Π,μ,q,return time,exact count or clean denominator is a runtime port. The new weighted proof does not modify the decoder or encoder.

For complete costs use the unchanged SB001 v2 §6 ledger, also reproduced in BS001 §4. Put n_prog=M+3, ell=ceil(log2(n_prog+K+2)), k=bitlength(κ), b_word=64(h+ell+k+1), K=2. Persistent words have b_word bits; full products use 2b_word and guarded temporaries <=4b_word+4. All three n_prog² masks, inputs/synthetic row, dense zero coefficients, local features, every head's n_prog² edge scans, integer cache generation, all-token complete banks, divisions/mux/fallback/rounding, copies/clears, counters/addresses/serialization are paid. No numerical n_prog² weight matrix is retained. Set

 T0=O(n_prog² K^6 b_word²),
 S0=O(n_prog²+n_prog K³ b_word+K^6 b_word+b_word²).

The addressed sequential alternative has program/address storage O(T0 b_word), forward bitwork O(T0 S0 b_word), forward peak O(T0 b_word+S0), offline bitwork O((T0+S0)b_word²), offline peak O(T0 b_word+S0+b_word²).

The SEPARATE PURE alternative sets T=T0+b_word,S'=S0+b_word: depth O(T), width O(S'), sparse gates/holds O(TS'), sparse wiring/coefficient bits O(b_word TS'), dense coefficient bits O(b_word T(S')²), dense forward/offline bitwork O(b_word² T(S')²), rolling numeric storage O(b_word S'). Sparse offline work is O(b_word² TS') when chosen. Phase peaks add all simultaneously retained program/parameters, public constants/masks, inputs/outputs, rolling arrays and scratch; duplicate rails are charged twice. Do not take minima across alternatives. All-token costs remain even if only the terminal output is exported. Arithmetic bitwidth, grid h, lnκ, offline work and compiled depth are different quantities.

## 8. Fixed-depth causal finite evaluators: same labels, different compiler

Use exactly BC001's family: fixed depth/heads/dimensions/affine-ReLU DAG sizes and uniform coefficient/range/Lipschitz bounds, local radius r>=3, output count D>=8, enough capacity for one head/one global layer/width16 and coefficient/affine-row-sum bounds at least two. Initial historical features are supplied finite dyadic trailing-window tables. Public causal nonempty masks have fixed density >=c, 0<c<=1/3, independent of data and boundary. Boundary first/last fixed windows enter the encoder only through the appended query, never historical states or parameters. Historical computation is genuinely causal. Larger depth can identity-pad. Every table/mask/description is paid. Source-independent seedwise bounds hold. The optional locally computed AND implementation requires row-sum budget three; it is NOT silently included in the smaller budget.

Evaluate with unchanged FA001 at target h+3, fractional precision P_f=4(h+3)+C_arch, d_f=2^P_f, then downward Q-grid floor. Retain ONLY the D-coordinate bank,S,public metadata/randomness; no clean numerator/denominator/other token or hidden state is exposed. Decoder may be arbitrary; upper decoder costs are charged below. This is NOT the one-block real-weight family and has no freely growing κ.

BC001 §5's upper is a paid trailing-radius-three eight-bit triple table, one zero-Q/K uniform head, width16 concatenation/projection, and optional exact identity padding. Masks are K_1={1},K_2={1,2},K_j={3,...,j} for 3<=j<=M+2, and K_(M+3)={3,...,M+2}; density >=1/3. Terminal query state can be zero; S is needed only by the decoder. It uses NO singleton-copy head in this dense-causal family.

At EVERY history all finite scores are exactly zero, so the unchanged FA Taylor evaluator produces a common positive integer weight W_*. With triple count C_abc the terminal exact accumulators are

 Z=M W_*, N_abc=W_* d_f C_abc,
 O_abc=floor(d_f C_abc/M).

With integer k_f=d_f/Q, floor(O_abc/k_f)=floor(Q C_abc/M). Thus its exported bank equals SB001's κ=1 bank EXACTLY, on every formal history and hence under every initialization. Zero counts stay zero. This is stronger than an E/Q approximation and is necessary for the deterministic minority-floor argument. Exact projections/identity padding preserve these labels. The post-cut decoder receives the same bank and boundary, so the arbitrary-start bound §5 applies with z=Q. Since W(Q,t)>=1/Q, its three terms are <=C F_C. Stationary lower and class inclusion from accepted BC001 give (BIF2); its lower proof and finite-domain case ledger remain unchanged.

Costs remain BC001 §6's COMPOSED costs, not a re-use of singleton-head execution. Write n=M+3, actual maximum description bitlength b_p, actual supplied record count U, public mask/metadata bitlength F_pub, q_idx=ceil(log2(n+1)), and
 w_word=O_arch(P_f+q_idx+log(P_f+1)+log(U+F_pub+2)).
For explicit fixed-width data U=O_arch(n²),F_pub=O_arch(n²+nq_idx), numerical coefficient b_p=O_arch(1); index costs are separate. Generate tables/masks by charged public loops, conservatively O_arch((U+F_pub)w_word²) work and full storage. Pay descriptions Ub_p+F_pub, conversion O_arch(U(b_p+P_f)²) and UP_f compact records, all-token QKV/projections, every candidate edge/mask scan, Taylor recurrence despite common weights, full products/guard bits, accumulations/quotients, affine/ReLU, local windows/boundary acquisition, tape scans/rewinds/copies/clears and output serialization. Full finite control costs O_arch(w_word^4). Encoder forward work O_arch(n²(P_f+1)w_word²), numerical rolling arrays O_arch(nw_word), and safe retained-data peak

 S_enc=O_arch(Ub_p+UP_f+F_pub+n+nw_word+w_word^4+b_p+P_f).

Public converted records use P_f+O_arch(1) bits; padding them instead costs Uw_word including writes. No n² numeric attention matrix is retained. Layout/reformatting and signed negative-floor correction remain charged.

Charge all-token pointwise decoding, all banks and output rows, exporting terminal only. A conservative upper is the COMPLETE addressed SB001 decoder ledger from §7 at κ=1 (k=1), although only its suffix executes: this overcharge does NOT execute its singleton heads as causal encoder layers. Add conversion O_arch(n(b_d+w_word)) written bits, with b_d=64(h+ceil(log2(n+K+2))+2). Add encoder/decoder data, work, code and conversion volumes, and maximize simultaneous sums over generation/conversion/forward/cleanup. At the cut disable all history/hidden/QKV/numerator access; release or clear dead numerical data with O_arch(nw_word+UP_f) writes paid. The cut is the same abstract access convention, not a free isolation device.

Optional PURE unrolling is of the actual COMPOSED bitwork T_bit and live bits S_bit: depth O(T_bit), width O(S_bit), sparse gates/holds O(T_bit S_bit), dense slots O(T_bit S_bit²), with full indices/coefficients/generation/storage paid. It does NOT preserve fixed attention depth. No minima across distinct compilers or a fixed-depth PURE theorem are claimed.

## 9. Both-initialization thresholds and alphabet contrast

Let a_scale=sqrt(M), u=1/(sqrt(M)e0), f=1+ln(1+u), Z_star=a_scale f. For either one-block initialization experiment, statistical-order risk has the joint condition

 Q ≳sqrt(M), AND κQ ≳Z_star.                         (9.1)

To make this precise, if risk<=C0/a_scale, put B=max{1,C0/c}. The lower yields Q>=a_scale/B and [1+ln(1+vu)]/v<=B, v=z/a_scale. If v>=1, v>=f/B. If v<1, concavity gives f<=B and the numerator >=1 gives v>=1/B>=f/B². Thus z>=Z_star/B² always. Conversely Q>=a_scale,z>=a_scale f imply W<= (f+ln f)/(a_scale f)<=2/a_scale, hence risk_all<=2C/a_scale. Fixed positive multiples adjust only constants. Legal dyadic/integer schedules exist by rounding Q upward and then κ upward; promise-based selection is separately paid setup, not a free runtime logarithm.

In any fixed band c_-sqrt(M)<=Q<=c_+sqrt(M), put f_Q=1+ln(1+Q/t). For risk<=C0/sqrt(M), the lower implies κ>=c f_Q/(C0 c_+), even allowing real κ. Choosing integer κ=ceil(f_Q)<=2f_Q gives W<=2/Q and arbitrary-start upper <=[2^17+(3+2^18)/c_-]/sqrt(M). Thus for a sufficiently large fixed target multiplier the least integer envelope is Θ(f_Q) for BOTH experiments. No feasibility for arbitrarily tiny target multipliers is asserted.

At β=1/M and Q≈sqrt(M), binary f_Q=Θ(1), so κ_min=Θ(1), stationary AND arbitrary-start. For fixed K>=3, accepted TR001 remains unchanged: its cutoff max(β,1/M) gives κ_min=Θ(log M) for both initialization experiments at the same sufficiently large target-order convention. Compare the same all-state certificate, actual-terminal loss, one-block positive-weight/local interface, and fixed dimensions admitting both uppers (e.g. D>=K³,r>=3 for a fixed K). Constants are not uniform in architecture or alphabet. The new conclusion upgrades the binary side, not the K>=3 theorem.

For the fixed-causal family κ=1 and W>=1/Q; the same inversion gives Q≳Z_star for both initializations. In particular β=1/M permits Q≈sqrt(M), whereas β<=M^-2 requires Q≈sqrt(M)log M. These statements concern the specified finite-evaluator family, not every Transformer or fixed-depth bit expansion.

## 10. Provenance and limits

Direct proof and receipt hashes are recorded in BIF001_source_bindings_v1.json. The imported accepted versions are BAI003 v2, BAI004 v5 (root receipt 06:48:06 UTC), BOD001 (06:46:59 UTC), BU001 v2, SB001 v2, BS001, BC001, and TR001 for the unchanged larger-alphabet comparison. Old candidate headings do not override exact receipts. Fresh BIF review is a separate requirement; acceptance of ingredients is not acceptance of this synthesis. Scalar/exact finite diagnostics corroborate, not prove, universal statements. No global sqrt(β) mixing claim, new predictor, added port, implementation speedup, external novelty/peer-review claim, publication, upload or contact is made.
