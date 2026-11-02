# Stage5 fixed full mathematical proof package v1

Root 881d17365a7019add4410343d568625dacae67d26aa17548bda2de7f9b860dbb

Contract 873515c4586d37a2bde324010bea6ae30f820927b7c25ded15b784a79eef7e45

This fixed text reproduces the exact mathematical claims, definitions, three component proofs, the proposed combination and the bounded primary map. It was prepared for independent fixed review; that review and later acceptance are not inferred from the document itself. Status comments inside reproduced components refer to their authoring times. Later status is governed by dated evidence records.

# Exact root statement

Establish the following finite input-contamination reliability theorem, under Definitions D1-D7. The true stationary source, actual terminal query, one common observation channel, complete observed information, positive output format and two distinct implementation cost models are part of this contract. Prior project Facts and probe012 file reviews are sources only; establish or legally discharge every load-bearing premise in this new project's normal native evidence chain.

C1. There is one deterministic predictor family A_(N,k,Q), independent of unknown u,t and of the channel, with the exact smoothed-count/clipping/grid rule D3. For every N>=3 and public (k,Q) in D2, every D1 source, and every admissible source-independent randomized batch channel T in D2, its actual terminal average KL satisfies
R_av(A,T;u,t) <= 16000000/(3N) + 135680*k/N + 3/Q.
The algorithm receives only Z,N,k,Q; clean counts are proof variables. Prove the pathwise count/row perturbation, common probability domination through clipping, true-source reciprocal visits and whole-prefix terminal bridge, and positive-grid transfer. Cover k=0, Q=2, Q=4/ties/zero counts and the actual N=3,4,5 no-prefix uniform branch. Do not assume the corrupted path is Markov, replace the terminal query by an independent query, or provide clean endpoints to the predictor.

C2. For every N>=6 and 1<=k<=floor((floor(N/2)-2)/1024), put u0=k/N, Delta=1/640000, t_-=1/2-Delta/2, t_+=1/2+Delta/2 and c=Delta^2/8=1/3276800000000. There exists ONE globally admissible randomized batch T_(N,k), independent of Q, the predictor and the actual hidden source label, such that TV(L_(u0,t_+)(Z | S_N=00), L_(u0,t_-)(Z | S_N=00))<=1/64, where Z=T_(N,k)(X_1^N) and channel-private coins are averaged. For every common possibly randomized predictor using the entire Z (even unrestricted probability outputs and unlimited subsequent computation), there is one SAME t_* in {t_-,t_+} for which
R_00(A,T_(N,k);u0,t_*) >= c and R_av(A,T_(N,k);u0,t_*) >= c*k/N.
The channel is fixed before the predictor; t_* may depend on that predictor. Its support preserves the last pair and changes at most k earlier bits for EVERY input and EVERY private seed. Prove the full reverse-history coupling, intermediate pairs, adaptive boundaries and truncated last block; then the unnormalized Jordan residual flow, one-row common kernel, hard-budget finite seed implementation and actual-terminal same-witness testing argument. Two source-labelled attacks, population/count aliases, or an average transport budget alone do not meet C2.

C3. Construct the D3 predictor as BOTH (i) a Z-only causal finite JOINT attention frontend plus exact selected-query arithmetic and (ii) a Z-only direct eight-count baseline. For each individual observed Z and public tuple they must emit identical guarded output bits. Prove all closed-box arithmetic guards, full products/remainders and safe casts, source-bearing state erasure and no clean bypass. Supply explicit finite generators and prove that each implementation separately obeys every applicable resource bound in D5, including all input/feature/endpoint acquisition, physical banks, scalar-vs-bit distinction, masks/zero coefficients, copies, holds, code/metadata/address handling, online work/storage/peak, output and offline generation/peak. The actual 46-operation output table, JOINT 17+46 and DIRECT 8+46 plus paid acquisition are specified in D4. Do not replace D5 with a new looser envelope, equate the two accounting models, assert old Bstar inclusion, or treat Python integer semantics as unit-cost hardware.

C4. Integrate C1-C3 in the same observation experiment: for either concrete implementation, C1 applies to C2's SAME channel and its selected SAME source witness. State precisely that the pollution contribution has an O(k/N) upper and an Omega(k/N) full-Z lower, with the separate 1/N and 1/Q terms only upper-bounded here. Preserve the direct-count strong baseline and the exact primary comparison in D6; no novelty, JOINT efficiency superiority, all-source bad-risk statement, deterministic-channel attainment, per-time sensor or all-layer/IEEE conclusion is part of the theorem. [Non-scientific operational metadata omitted.] Existing source reviews and old SOLVED roots do not discharge this new contract. After this accurate stage closes, the v10 mother problem still requires synthesis; no frozen prior root is reopened.


---

# Definitions D1-D7

Source: `inputs/STAGE_DEFINITIONS.md`; SHA256 `fc104078b9455bdd86586decd50902df6688400cc00f06e6b105699efefd0e02`. Source text follows unchanged.

# D1. True source, history and loss

The alphabet is {0,1}. For unknown 0<u<1/4 and 1/4<=t<=3/4 put w=(1-u)/3 and r=ut/w. The pair state order is (00,01,10,11). The stationary pair law is pi=(u,w,w,w), and next-one probabilities in that order are (t,1/2,1-r,1/2). The pair transition shifts the last bit and appends the next symbol. Start (X1,X2) with pi and generate X1,...,X_(N+1) by this law. The observed clean history is only X1,...,XN; Y=X_(N+1) is not observed. The actual terminal pair is S_N=(X_(N-1),X_N). Natural logarithms are used.

For a predictor receiving the corrupted history below, let q_A(.|Z,N,k,Q) be its output probability vector. Define R_av(A,T;u,t)=E KL(p_(u,t)(.|S_N)||q_A) and R_00=E[the same loss | S_N=00]. Expectations include the source, independent private channel coins and any independent private predictor coins. Arbitrary probability outputs in the lower theorem may have infinite KL. The fixed finite upper predictor is strictly positive. These are actual same-trajectory terminal risks, not cumulative regret divided by N or independent test-query risks.

# D2. Public domain and the common batch observation channel

N is any integer >=3 and Q=2^b with integer b>=1. If N>=6, set m=floor(N/2), M=m-2 and allow integer 0<=k<=floor(M/1024). For N=3,4,5 define k=0; the predictor is a genuine uniform no-prefix branch. The constant 1/1024 defines this conservative domain and is not asserted necessary.

Before ANY encoder/predictor computation, one randomized batch T maps the complete already-observed X1..XN to Z1..ZN. For EVERY binary input x and EVERY independent private seed omega, T(x,omega) has the same last two bits as x and differs in at most k of positions1..N-2. The rule may use all observed input bits and their terminal pair, plus public N,k,Q. It cannot read future Y, the actual hidden u,t or source label, or source-dependent coins. A channel is one fixed rule over all inputs and all D1 sources; it is not chosen at runtime using the realized source index. The lower theorem's T_(N,k) is additionally independent of Q and predictor.

All algorithms and baselines see ONLY Z,N,k,Q. They receive no clean history/prefix/gap/E_m/counts, hidden parameters or private channel seed. Since the last pair is preserved, S_N equals the last pair of Z. Any prefix endpoint E_m used by an implementation is the DIRTY pair (Z_(m-1),Z_m), without extra protection. Internal arithmetic is exact finite arithmetic, separately charged. There is no post-statistic eta cut in this experiment. This is not a time-causal sensor, IEEE fault or all-layer perturbation model. The external channel's own computation/randomness is unrestricted and not part of predictor cost; handling all observed input by the predictor is charged.

For C2 a public two-point experiment uses u0=k/N and t_+/-=1/2+/-1/1280000. Computing a fixed table from both public witness laws is allowed; selecting a row by the actual hidden label is not. T must be globally legal also when other D1 parameters produce its input. Private channel randomness is averaged in the TV/risk statement but the edit constraint is pointwise in every seed. Predictor-private randomization is fresh and independent of channel coins.

# D3. Exactly specified unknown-parameter predictor and output

For N>=6 and a path z, C_sc(z) counts triples ending at positions3..m, with preceding two symbols s and next symbol c. There are M eligible triples. Let D_s=C_s0+C_s1, alpha=3k+1. Select the row s by the actual last two Z symbols. In the 00 row, r1=clip_[1/4,3/4]((C_001+alpha)/(D_00+2alpha)), r0=1-r1. In row10, r0=min(3/4,(C_100+alpha)/(D_10+2alpha)), r1=1-r0. Rows01 and11 use uniform. No true source parameter enters these formulas.

For the selected counts C0,C1 define D=C0+C1+2alpha and Zden=4D. N<6 and Q=2 output uniform. For row00 with Q>=4 set z1=min(3D,max(D,4(C1+alpha))), J=floor((2Q*z1+Zden)/(2Zden)); output (Q-J,J)/Q. Half ties go upward. For row10 set z0=min(3D,4(C0+alpha)), z1=Zden-z0, j_c=ceil((Q-1)*z_c/Zden), e=Q-j0-j1; output (j0,j1+e)/Q. In both Q-1 and the division numerator Zden-1, the constant is literal1, not alpha. Rows01/11 are uniform. All candidate branches actually evaluated by the straight-line program must be defined, including when the final uniform MUX discards one.

The final observable port is THREE b+1-bit fields (out0,out1,Q), each least-significant bit first, thus 3(b+1) bits. The two output numerators are positive and sum to Q. Every retained intermediate/source-bearing bank other than this final output is explicitly erased; public code/indices may remain but cannot contain hidden source data. N=3,4,5 reads exactly N observed bits and writes this same port without instantiating a prefix/head or fictitious sixth input.

# D4. Two finite implementations, arithmetic and deterministic acquisition

The source implementations copied to inputs/source-stage4/outputs/012-input-contamination/prover/ are fixed specifications and provenance, not automatically accepted proofs: robust_program_v1.py SHA256 5945d29df95eb1499005250e7d0f3835aff91f9846b8e6ce6ac3ef516c0d5600, resource_interface_v1.py SHA256 b11f8f06eec9b1ff2e305b5385e1efc69d3076b527027971a764e58d1ec9603e, finite-program-v1.json SHA256 3875340ee76fa75ad61cc9db5e4483bb03e1971eeaa9b5d8973545bb2a83ec44. The exact semantics are D3 plus the finite operations below; their new-project realization and costs must be proved. The original semantic library c3c4_program_v1.py SHA256 88de55d3243dcff63c1deffc226a645a7fb7949e3a32d662ab55141630f9b570 is also source-only.

JOINT: let h=ceil(log2(256(N-2))), A=2^h, p=4h+4ceil(log2(m+4))+64, R_s=2^p. Four charged singleton bindings produce the causal local lags and observed terminal/dirty prefix endpoint selectors; two-AND triple features and a single zero-score uniform finite head produce eight j_sc=floor(A*C_sc(Z)/M) and eleven explicit zero internal words. Its exact finite zero-score value is R_s, with numerator A*R_s*C_sc and denominator M*R_s. The internal 19 words and eight controls are implementation registers, NOT an observation restriction on other predictors. No real-softmax approximation, free triple table, or clean endpoint is assumed. Six row-selection MUXes and exact count snapping floor((2M*j+A)/(2A)) plus two control ORs use the 17-operation table. Every independent closed j in[0,A] yields a count in[0,M]; on actual observed Z the snap is exact.

DIRECT: own and read the same full Z batch, initialize eight counters, scan every eligible triple and all eight public labels, compute its two AND/equality features and increment each matching counter. Endpoints come only from this owned Z. Six MUXes and two control ORs select the counts. Acquisition loop/control/input reads and cleanup are charged in addition to the eight selected-row operations.

Both then execute the same 46-operation output table: from the frozen 41-operation output insert after CONST1 the five operations k=CONST(public k), twok=SHL(k,1), threek=ADD(twok,k), alpha=ADD(threek,one), twoalpha=SHL(alpha,1). Only three subsequent operands change to Dsum+twoalpha, C0+alpha, C1+alpha; all grid literal1 operations and eager candidates remain. JOINT has 17+46=63 selected-row/output operations, DIRECT 8+46=54 plus acquisition. This table must be presented self-contained in its new proof, including the retained paid CONST0/CONST2, ceiling residual and terminal MUXes.

On the closed independent count box C0,C1 in[0,M], D<=3m, Zden<=12m, nearest dividend<32mQ and each ceiling dividend<12mQ. Guards must cover that whole box, not just realizable count sums. With beta as D5, use exact finite primitives with g(beta)=1024beta^2 bit steps and 32beta+32 bit scratch. Multiplication retains the full 2beta-bit product; restoring division retains the full numerator, beta+1-bit shifted remainder and full quotient before a range-justified cast. Carry/borrow, MIN/MAX/MUX/select and comparison costs are real. Neither primitive validity nor the finite compiler is assumed from an old Fact without lawful new-project support.

# D5. Fixed separately priced full resource vectors

These are sufficient finite implementation bounds, not equality of consumption, optimality or a shared-cap advantage. DIRECT uses an owned-batch packed bit-register machine; JOINT uses principal extracted-query one-shot batch hybrid dense tokenwise tied matrices plus a separately charged finite evaluator. Every Boolean neural channel occupies a full beta-bit physical scalar. The models must not be silently identified, flattened, streamed or treated as unit-cost RAM. All zero matrix/mask entries and retained identities are stored/evaluated. JOINT initially pays all n token banks; nonquery release follows actual full source-state erasure. No old D6 Bstar is a cap or premise here.

Define bitlength(x)=floor(log2(x))+1 for positive integers, ell=ceil(log2(N+2)), tau=bitlength(k+1), n=N+1. For N>=6, s=ell+b+tau+p+32 with p in D4; for N<6, s=ell+b+tau+32 with no p or prefix parameters. Let beta=128s, g=1024beta^2 and Z_meta=1024ns.

For DIRECT, N>=6:
G=(512n+2048)g, E=L=0, W=0, dense_slots=P_bits=mask_bits=I_holds=0,
core=G, W_work=8N+8192beta+Z_meta.
All neural coordinates are zero. Packed-memory residence and each accessed bit are separately paid; zero neural coordinates do not mean free memory.

For JOINT, N>=6:
W=2048beta,
G=64g+256*19(h+1)+8192beta+128(b+1),
L=16G+96,
E=512n^2+16nW+256W+1024(h+b+ell+tau+1),
dense_slots=(132+L)(W+1)^2,
P_bits=dense_slots*beta,
mask_bits=4n^2+(m+1)^2,
I_holds=132nW+LW,
core=256(132n+L)(W+1)^2*beta^2+E*g,
W_work=4nWbeta+Z_meta.
Frontend depth allowance132 consists of128 construction layers and four extraction/clear phases. Query depth is L, width per token W, five total heads and at most four simultaneous heads, value width8, QK dimension at most4, score magnitude0. E is finite word-step bundles, each expanded by g, distinct from neural depth and dense MAC work. Metadata is public only; dirty inputs/counts/endpoints are data banks. Actual copies, full-bank scans, liveness and all source-bearing cleanup must justify these numbers.

For N=3,4,5 BOTH implementations use the actual-input uniform packed bit-register branch:
G=(128(N+1)+512)g, core=G, E=L=W=dense_slots=P_bits=mask_bits=I_holds=0,
W_work=8N+8192beta+Z_meta.
All heads/layers/values/QK/score coordinates are zero; no N-to6 statistical padding is permitted.

For either implementation and every N define:
a=beta+bitlength(G+E+Z_meta+N+L+1)+32,
K_code=4096*g*(beta+a)+4096*(s+1)*(beta+a)^2,
U_stored=P_bits+mask_bits+Z_meta+K_code,
T_online=4096(a+beta)^2*core,
peak_online=U_stored+W_work,
a_gen=beta+bitlength(U_stored+T_online+N+L+1)+s+32,
Emit=U_stored+L+1024,
T_gen=1024s^2+4096*Emit*a_gen^2,
W_gen=64a_gen+64*Emit*a_gen,
peak_gen=U_stored+W_gen.
Here g is the defined number 1024beta^2. a is the per-field runtime address-record width and a_gen the separate flat generator address width. The final output length is3(b+1), GPU work0. The separately fixed resource calculator is a transcription reference for these full vectors, not a proof of the charges.

All input storage/read/validation, full products/remainders, dirty endpoint/control handling, prior copies, physical scalar storage, all-live-state holds, instruction/operand/coefficient fetch and dispatch/address arithmetic, explicit cleanup, public metadata/code/constants, final field initialization/writes and simultaneous storage/working peaks are included. The generator enumerates the primitive wiring, new SSA, loop/phase descriptors, masks/dense zeros, all padded code/metadata bits and final port wiring; all stored bits and layer delimiters are generated with the displayed offline cost/peak. No free hardware primitive, Python GC or precomputed hidden statistic is allowed. No actual allocation of enormous netlists is required for a finite constructive proof, but a formula without an explicit generator/liveness argument is insufficient.

# D6. Quantifier interpretation, baselines and sources

C1 quantifier order is one deterministic family A, then all public tuples, all D1 parameters and all admissible channels. C2 order is each public(N,k>=1), then one globally lawful T independent of Q and predictor, then every Q and every common possibly randomized full-Z predictor, then a witness t_* that simultaneously supports conditional and average bounds. The latter predictor may even know the public two-point experiment and channel; it never receives the private channel seed. Infinite later computation does not add unobserved clean information.

C1 applies to C2's T for either concrete implementation. The two implementations agree on every Z, so this contract cannot establish JOINT statistical superiority. It gives an O(1/N+k/N+1/Q) average upper and an Omega(k/N) contamination lower, plus a positive rare00 conditional lower. It does not claim matched 1/N or1/Q lower terms, full conditional classification, every-source damage, small unconditional history TV, deterministic attack attainment, practical constants, optimized resources or a learning result.

Bounded existing primary mapping: Chen/Gao/Ren, arXiv1511.04144v2, is iid Huber-mixture robust testing/modulus, not this common hard-edit dependent observation rule. Pydi/Jog, ICML2020/PMLR119 pp7814-7823 main plus supplement, includes class-dependent point maps and Wasserstein distribution attacks, transport tail cost and submeasures. A whole dependent trajectory can be one feature; dependence itself is not a novelty exclusion. Generic testing/transport/submeasure ideas are prior tools. The new proof must establish the actual D1 conditional full-path Hamming bound and one hard-budget common input-row kernel; class-labelled maps or expected transport alone cannot substitute. These three fixed PDFs and exact location maps are provenance. No claim of novel or publication-central results is required or inferred from the bounded comparison.

Sources live only under inputs/source-stage4/ with original relative layout and author/hash records. The previous native C1/C3 Fact identifiers in those files remain old-project provenance, not active new-project Fact IDs. Necessary clean source/visits/full-prefix/grid and deterministic finite primitive/frontend/compiler premises must be self-contained or admitted by a genuinely supported mechanism with matching semantics in this project's normal evidence chain. Do not replay old root/final_audit or old unchanged diagnostics. Old Dot absolute-cube formulas, 5/4 exponents and periodic logarithmic-history claims are not mathematical premises. Preserve the earlier conditional Theta(eta) erratum in historical scope; it is not a parameter or claim of this new model.

# D7. Evidence and completion

This historical contract required fixed full mathematical review with accurate claims, definitions, dependencies and source versions. Existing source-file reviews and finite diagnostics are not substitutes for the required proof evidence. The recorded evidence level is LLM_CHECKED_PROOF, not formal verification or external peer review. Same-model agreement is not independent cross-model validation. Historical administrative completion requirements are omitted from this public export; their unresolved status is not relabelled a scientific pass. Completion of this stage would not settle the broader research problem.


---

# C1 complete current proof

Source: `outputs/001-input-contamination/prover/c1-proof-v1.md`; SHA256 `c80a71242b438eda82b4b1717838a15da30232db18c4b97096f29f45c5101fc3`. Source text follows unchanged.

# Stage5 C1: self-contained actual-terminal input-contamination upper

Author: Prover, 2026-10-26. Fixed proof v1.
Exact obligation: `b5f118d33a9d9687ac8e3d48ca7df6e5c0403aeba52c026d88087e385e813354`.
Contract: `873515c4586d37a2bde324010bea6ae30f820927b7c25ded15b784a79eef7e45`.
Submission predecessors: **[]**.

## 0. Claim, scope and provenance

Under this project's D1-D3, the deterministic family defined in §§1,10
uses only Z,N,k,Q, is independent of unknown u,t and of the channel, and
for every legal public tuple, every D1 source and every D2 channel satisfies

    R_av <= 16000000/(3N) + 135680 k/N + 3/Q.             (T)

All expectations refer to the actual same-history terminal pair S_N.
This file proves every statistical and grid premise used in (T), with no
Fact predecessor. Historical sources are confined to this workspace's
inputs/source-stage4. The clean argument below is attributed to Prover
stage4 c1-proof-v2 §§1-7 and elementary inequalities; the pollution and grid
argument to Prover probe012 upper-program-certificate-v1 §§1-4. Their exact
byte hashes are appended. These are derivation sources, not admitted
premises: all needed arguments are written here. Current PROBLEM.md/D1-D7
and inputs/AUTONOMOUS_RESEARCH.md determine scope. No old campaign is accessed.

This is C1 only. D4-D5 constructions and resource vectors belong to C3;
no old primitive/compiler interface is assumed here. The family is a
finite algorithm: scan the observed string, form eight counts, evaluate
the exact integer output formulas, write the three specified fields, then
clear other mutable data. Its implementation costs are not asserted here.
GPU work is zero; no diagnostic suite is rerun. Native acceptance, if
obtained, is recorded separately from this fixed mathematical text.

## 1. Experiment, one predictor and proof-only clean comparator

Fix N>=3 and Q=2^b with integer b>=1. If N>=6, put m=floor(N/2),
M=m-2>=1 and allow integer 0<=k<=floor(M/1024). For N=3,4,5 set k=0.
For unknown 0<u<1/4 and 1/4<=t<=3/4 put w=(1-u)/3 and r=ut/w.
Then 1/4<w<1/3, 0<r<3/4 and r>=3u/4. The pair chain
S_i=(X_(i-1),X_i), i>=2, has, in state order (00,01,10,11),

    P = [[1-t, t,   0,   0],
         [0,   0, 1/2, 1/2],
         [r, 1-r,   0,   0],
         [0,   0, 1/2, 1/2]],          pi=(u,w,w,w).

Start S_2 with pi. The next-one target probabilities p_s(1) are
(t,1/2,1-r,1/2). Only X_1^N is observed by the channel; Y=X_(N+1) is not.
The source-independent randomized batch channel has independent private
coins omega and returns Z=T(X_1^N,omega). For every input and every seed,
it preserves positions N-1,N and changes at most k of positions 1,...,N-2.
It may inspect the entire history, including S_N. Our predictor sees only
Z,N,k,Q: no clean prefix, endpoint, count, u,t, future Y or seed. Its query is

    s=(Z_(N-1),Z_N)=S_N.

All risks average KL(p_s||q) over source and channel coins. Given X_1^N
and the independent channel coins, Y still has law p_(S_N), so this is
the excess expected next-symbol logarithmic loss. No Markov or other
probability model is imposed on Z.

For N>=6 and any path y, C_sc(y) counts j=3,...,m such that
(y_(j-2),y_(j-1))=s and y_j=c. Put D_s(y)=C_s0(y)+C_s1(y).
There are exactly M eligible triples. Write C_sc,D_s for y=X only as
proof variables, and C'_sc,D'_s for y=Z, the algorithm's actual counts.
Set alpha=3k+1. Its pre-grid vector rho is

    rho_00,1 = clip_[1/4,3/4]((C'_00,1+alpha)/(D'_00+2alpha)),
    rho_00,0 = 1-rho_00,1;
    rho_10,0 = min(3/4,(C'_10,0+alpha)/(D'_10+2alpha)),
    rho_10,1 = 1-rho_10,0;
    rho_01 = rho_11 = (1/2,1/2).

The actual predictor applies exactly §10's integer grid formulas to the
selected dirty counts and writes (out0,out1,Q) in three b+1-bit fields,
least significant bit first. Both candidate formulas can be evaluated
before selecting the terminal branch: §10 proves both are defined on
the whole independent count box. Public Q=2 selects uniform at the output.

For N=3,4,5 the actual algorithm reads exactly its N observed bits, writes
(Q/2,Q/2,Q), and clears its mutable input/scratch copies. It instantiates
no m,M, prefix, count table or fictitious sixth observation.

For the proof only, define the clean add-one comparator a_s by

    a_00,1 = clip_[1/4,3/4]((C_00,1+1)/(D_00+2)),
    a_00,0 = 1-a_00,1;
    a_10,0 = min(3/4,(C_10,0+1)/(D_10+2)),
    a_10,1 = 1-a_10,0;
    a_01 = a_11 = (1/2,1/2).

Its actual-terminal risk is R_N=E KL(p_(S_N)||a_(S_N)); for N<6 its
comparison output is uniform. Sections 2-7 prove directly

    R_N <= 1000000/N.                                   (C1.1)

In §§2-7, V denotes a centered count, p a local successor probability,
and R the reverse kernel, distinct from observed Z, true scalar r and
pre-grid vector rho. Put g=N-m when N>=6. All clean quantities in §§2-9
remain unavailable to the algorithm.

## 2. Elementary inequalities used below

Write kl(p,q) for Bernoulli KL. For 0<q<1, log z<=z-1 gives

    kl(p,q) <= (p-q)^2/[q(1-q)].                           (C1.6)

Indeed apply the log inequality separately to p/q and (1-p)/(1-q) and
simplify; endpoint values of p follow by limits. Also

    kl(p,q) >= 2(p-q)^2.                                  (C1.7)

For fixed q in (0,1), the difference of the two sides as a function of p
has value and derivative zero at p=q and second derivative
1/[p(1-p)]-4>=0. Integration on either side of q proves the assertion;
boundary cases follow by limits, with infinite KL handled in the usual way.

For finite laws mu,nu put TV(mu,nu)=1/2 sum_h |mu(h)-nu(h)|.
The positive and negative parts of mu-nu have equal mass TV, so TV is
also the supremum of absolute probability differences over events.

A common stochastic kernel contracts TV: expand each output difference,
apply the triangle inequality and sum kernel rows. Further, if 0<=f<=L,

    |E_mu f-E_nu f| <= L TV(mu,nu).                        (C1.9)

For example, write f(h)=integral_0^L 1{f(h)>v}dv and use the event
definition of TV. These elementary facts also cover randomized tests by
integrating a function with values in [0,1].

## 3. Stationarity, reverse kernel and uniform mixing

The four incoming masses for pi P are

    u(1-t)+wr=u,   ut+w(1-r)=w,   (w+w)/2=w,   (w+w)/2=w.

Hence pi P=pi. The initialized pair chain is stationary and in particular
Pr(S_N=00)=u and Pr(S_N=s)=w for each other row, for every N.

Two-step paths from (00,01,10,11) to10 have respective probabilities
t/2, 1/4, (1-r)/2, 1/4: from00 or10 go through01, and from01 or11
go through11. Each is >=1/8. Therefore

    P^2(x,10)>=1/8,   P^3(x,00)>=r/8>=3u/32.              (C1.10)

The following three-step paths all end at01:

    00->01->10->01: t(1-r)/2 >=1/32;
    01->11->10->01: (1-r)/4 >=1/16;
    10->01->10->01: (1-r)^2/2 >=1/32;
    11->11->10->01: (1-r)/4 >=1/16.

Thus P^3(x,01)>=1/32 for every x. Directly applying
R(i,j)=pi_j P(j,i)/pi_i gives the stationary reverse kernel

    R = [[1-t,   0,   t,   0],
         [r,     0, 1-r,   0],
         [0,   1/2,   0, 1/2],
         [0,   1/2,   0, 1/2]].

If sigma exchanges01 and10, then R(i,j)=P(sigma(i),sigma(j)) and
pi is sigma-invariant. Consequently R^3(x,10)>=1/32. This is a
conjugacy, not P=R or ordinary detailed balance: P(00,01)>0 while
P(01,00)=0 already rules out ordinary reversibility with positive pi.

Whenever every row of K puts mass at least eta on a common state z,
K=eta*delta_z+(1-eta)*K' for a stochastic K'. The common term cancels
in differences of probability measures; TV contracts by at most 1-eta.
Apply this to R^3 and use pi R=pi, which follows directly from the reverse
kernel formula. Extra steps also contract TV. Since TV<=1 initially,

    TV(R^g(s,.),pi) <= d_g=(31/32)^floor(g/3)              (C1.11)

for all starting states s, uniformly over the entire parameter domain.

## 4. Entire-prefix bridge for the actual terminal query

For any consistent path s_2,...,s_N, stationarity and the reverse formula
give the telescoping identity

    pi_(s_2) product_(i=2)^(N-1) P(s_i,s_(i+1))
      = pi_(s_N) product_(i=2)^(N-1) R(s_(i+1),s_i).

Therefore, conditional on the actual S_N=s, the whole backward pair path
is an R-chain started at s. After g=N-m backward steps, S_m has law
R^g(s,.). Given S_m, its earlier backward path to S_2 has a common kernel
independent of s. A consistent path S_m,...,S_2 uniquely specifies X_1^m.
The unconditional stationary prefix is the image of pi under exactly
the same kernel. By TV contraction and (C1.11),

    TV(Law(X_1^m | S_N=s), Law(X_1^m)) <= d_g.             (C1.12)

This compares the entire prefix, including every count and its dependence
on its endpoint. There is no independence assertion and no division by pi_s.

For each s let f_s(X_1^m) be the loss of the fixed row-s estimator above,
and K_s=E f_s for a stationary prefix. Both row00 coordinates are >=1/4;
row10 has q_1>=1/4 and q_0>=1/(M+2) (the upper clipping cannot violate
this since M>=1). As -sum p_c log p_c>=0,

    0<=f_00<=log4,
    0<=f_10<=log max(M+2,4),     f_01=f_11=0.             (C1.13)

Apply (C1.9) to (C1.12) separately for each fixed row, then weight by the
actual terminal law pi. Since u+w<1 and m=M+2,

    R_N <= u K_00+w K_10+d_g log max(m,4).                (C1.14)

We make this comparison for the unquantized estimator. The loss caps here
do not depend on any later output precision Q.

## 5. Tools for dependent counts at a deterministic horizon

### 5.1 Spaced visits

Suppose P^ell(x,s)>=p for all x. Inspect only source positions

    i_j=2+ell*j,   j=1,...,B,   B=floor((M-1)/ell).

Every inspected position is in 2,...,m-1. Conditional on all information
through the previous inspected position (through S_2 for j=1), its
indicator I_j=1{S_(i_j)=s} has success probability at least p. Hence for
lambda>0, successive conditioning gives

    E exp(-lambda sum_j I_j) <= (1-p+p exp(-lambda))^B.

Set lambda=log2. Exponential Markov inequality, log(1-z)<=-z and
log2<3/4 imply

    Pr(sum_j I_j<=Bp/2)
       <= exp((log2)Bp/2-Bp/2) <= exp(-Bp/8).             (C1.15)

No independence of I_j is needed, and D_s>=sum_j I_j pathwise.
For row00 take ell=3,p=3u/32. If M>=6 then
B=floor((M-1)/3)>=M/6 (check residues modulo3), so with x=Mu,

    Pr(D_00<x/128) <= exp(-x/512).                        (C1.16)

Indeed Bp/2>=x/128 and Bp/8>=x/512. For row10 take ell=2,p=1/8.
For M>=64, B=floor((M-1)/2)>=M/4>=16 and define the deterministic
integer d_vis=floor(B/16). Since floor z>=z/2 for z>=1,

    d_vis>=B/32>=M/128, d_vis>=1,
    Pr(D_10<d_vis) <= exp(-M/256).                            (C1.17)

Here d_vis<=B/16=Bp/2, so (C1.15) applies. These are proof thresholds, not
inputs or event labels given to the predictor.

### 5.2 Martingale variance

Fix a row s and one chosen successor, with true probability p. Put
C=C_s,c, D=D_s and V=C-pD. For i=2,...,m-1 its increment is
1{S_i=s}(1{X_(i+1)=c}-p). The row indicator is measurable before the
successor is sampled, so the increment's conditional mean is zero and
conditional second moment is p(1-p)1{S_i=s}. For i<j, conditioning the
product on information through X_j makes its expectation zero. Summing
these identities at the deterministic horizon yields

    E V^2=p(1-p) E D,       E D=M pi_s.                   (C1.18)

This is unconditional variance, not a claim about the law of C given D.

### 5.3 Fixed-length row-stack events

Independently for each row s, prepare an infinite sequence of iid
Bernoulli successor bits with that row's probability, independent of the
initial pi draw. Each visit uses its row's next unused bit. Conditional on
the generated past, the next unused bit has the required row law: events
specifying a past only constrain finitely many already used bits. Induction
on time therefore reproduces exactly the Markov path law. This is a proof
coupling, not extra data or randomness available to the algorithm.

Let B_s(k) count the chosen successes in the first k stack bits. Then
C=B_s(D) pathwise. Since partial sums are nondecreasing, for deterministic
integer d_vis>=1,

    {D>=d_vis, C<p*d_vis/2} subset {B_s(d_vis)<p*d_vis/2}.

The latter involves exactly d_vis iid bits. Their exponential moment, by the
same calculation as (C1.15), gives

    Pr(D>=d_vis,C<p*d_vis/2) <= exp(-p*d_vis/8).                        (C1.19)

The random visit count D can depend on the used stack. We never assert
that C conditional on D is binomial; such an assertion would in general
be false. (C1.18) and (C1.19) serve separate purposes.

## 6. Stationary-prefix row risks with explicit constants

### 6.1 Rare row00, interior successor

Set x=Mu and V=C_00,1-tD_00. Projection onto [1/4,3/4] cannot increase
distance to t in that interval. For the projected estimate q, q(1-q)>=3/16.
Writing v=(C+1)/(D+2), we have v-t=(V+1-2t)/(D+2). By (C1.6),
(A+B)^2<=2A^2+2B^2 and |1-2t|<=1,

    kl(t,q)<=12(V^2+1)/(D+2)^2,       E V^2<=x/4.          (C1.20)

When M>=6, split on D>=x/128. On this event, taking an unconditional
second moment is sufficient and gives expectation at most
12(x/4+1)/(x/128+2)^2. After multiplication by 1+x this is

    49152 (x+1)(x+4)/(x+256)^2 <=49152.

On its complement, use the genuine loss cap log4 and (C1.16).
Since x exp(-x/512)<=512/e, (1+x)exp(-x/512)<257, and log4<3/2,
the complementary contribution after multiplication by 1+x is <386.
The sum is less than 50000. For 1<=M<6, x<5/4, and the deterministic
cap log4 by itself satisfies the same bound. Thus, for every M>=1,

    K_00 <= 50000/(1+Mu).                                (C1.21)

This also covers zero counts, repeated visits, and paths ending partway
through a run of row00 visits.

### 6.2 Common row10, arbitrarily rare successor

Let p=r, C=C_10,0, D=D_10, v=(C+1)/(D+2), q=min(v,3/4) and V=C-pD.
For v>=p the derivative of (p-v)^2/v is 1-p^2/v^2>=0. Whenever clipping
occurs, v>3/4>p, so clipping cannot increase this ratio. Since 1-q>=1/4,
(C1.6) and (C1.18) give

    kl(p,q)<=8(V^2+1)/[(D+2)(C+1)],     E V^2<=pM.         (C1.22)

For M>=64 choose d_vis from (C1.17), and partition all paths into

    G={D>=d_vis,C>=p*d_vis/2}, H={D>=d_vis,C<p*d_vis/2}, J={D<d_vis}.

On G, (C1.22) and E[V^2;G]<=E V^2 yield

    E[loss;G] <=8(pM+1)/[d_vis max(1,p*d_vis/2)]
              <=16M/d_vis^2+8/d_vis <=263168/M.                  (C1.23)

For H a logarithmic loss bound is needed. For 0<q<=3/4,

    kl(p,q)<=p log_+(p/q)+4q,  log_+(z)=max(0,log z).     (C1.24)

Indeed drop the nonpositive (1-p)log(1-p), and bound
-(1-p)log(1-q)<=-log(1-q)<=q/(1-q)<=4q. On H,

    q>=1/(M+2),   q<=v<=(p*d_vis/2+1)/(d_vis+2)<=p/2+1/d_vis.

Also (M+2)/d_vis<=256. With y=p*d_vis and (C1.19), this proves

    E[loss;H]
      <=[y log_+(256y)+2y+4] exp(-y/8)/d_vis <=108/d_vis
      <=13824/M.                                        (C1.25)

For completeness, log_+(256y)<=8+y for y>0 (use log y<=y-1 and
log256<6 when the logarithm is positive). The numerator is at most
10y+y^2+4. Its product with exp(-y/8) is at most 40+64+4=108:
max y exp(-y/8)=8/e<4 and max y^2 exp(-y/8)=256/e^2<64.
This works uniformly as p tends to zero; no lower bound on p was used.

On J, (C1.13), (C1.17) and log(M+2)<=M for M>=64 give

    E[loss;J] <= M exp(-M/256) <=65536/M,                 (C1.26)

because max_(x>=0) x^2 exp(-x/256)=262144/e^2<65536.
The sum in (C1.23)–(C1.26) is 342528/M. For M>=64,
342528(1+1/64)<400000, so this is at most 400000/(M+1).
For 1<=M<64 the cap log max(M+2,4)<=log65<5 is more than sufficient.
We have therefore proved, for all M>=1,

    K_10 <=400000/(M+1).                                 (C1.27)

Every bad event was multiplied by a valid loss bound. In particular a
TV bound of one is never substituted for a bound on KL loss.

## 7. Actual-terminal rates, including all small N

For N>=6 substitute (C1.21),(C1.27) into (C1.14):

    R_N <=50000u/(1+Mu)+400000w/(M+1)
            +d_g log max(m,4).                          (C1.28)

We have u/(1+Mu)<=1/(M+1), w<1/3, and M+1>=N/4. The sum of the first
two terms is at most (50000+400000/3)*4/N<800000/N.
Since g>=N/2, floor(g/3)>=N/6-1 and log(31/32)<=-1/32,

    d_g<=2 exp(-N/192).

The elementary estimate log max(m,4)<=N then shows that the last term
in (C1.28) is at most 73728/N: indeed
max_(x>=0) 2x^2 exp(-x/192)=294912/e^2<73728.
This proves (C1.1) for N>=6.

For N=3,4,5 the comparison output is uniform and every binary KL
loss to uniform is at most log2 < 1000000/N. This proves (C1.1) for
every N>=3, without invoking a zero or negative prefix length.

## 8. Pathwise separate count/row perturbations and clipping domination

Fix an arbitrary clean binary input X_1^N and an arbitrary legal private
seed omega. A changed symbol at i can affect only triples ending at
i,i+1,i+2, intersected with 3,...,m. Their union has at most 3k windows.
On each affected window, each fixed triple indicator changes by at most
one, and each fixed row indicator changes by at most one. Each unaffected
indicator agrees. Summing each type of indicator separately gives

    |C'_sc-C_sc| <= 3k,       |D'_s-D_s| <= 3k.            (P1)

The row bound is direct, not the sum of two coordinate bounds. This holds
even when the dirty prefix endpoint changes or edits depend on S_N. It
concerns each input and seed, not an average edit budget.

For v_sc=(C_sc+1)/(D_s+2) and v'_sc=(C'_sc+alpha)/(D'_s+2alpha),
(P1) and alpha=3k+1 imply

    C'_sc+alpha >= C_sc+1,
    D'_s+2alpha <= D_s+9k+2,
    v'_sc >= gamma_s v_sc,
    gamma_s=(D_s+2)/(D_s+9k+2) in (0,1].                 (P2)

This common multiplicative bound holds for both coordinates. Clipping
preserves it: for 0<=l<=h<=1 let f(x)=min(h,max(l,x)). If 0<gamma<=1,

    max(l,gamma*y) >= gamma*max(l,y),
    min(h,gamma*a) >= gamma*min(h,a)  for a>=0.

Thus f(gamma*y)>=gamma*f(y) for y>=0, and x>=gamma*y implies
f(x)>=gamma*f(y) by monotonicity. Also
1-f(x)=clip_[1-h,1-l](1-x), so applying the same argument to the other
raw coordinate proves simultaneous domination of both coordinates after
clipping. For row00 use [1/4,3/4] on coordinate1, and for row10 use
[0,3/4] on coordinate0. Both resulting coordinates remain strictly positive.
Consequently, for s=00,10 and each clean input and channel seed,

    rho_sc >= gamma_s a_sc,  c=0,1,
    KL(p_s||rho_s)-KL(p_s||a_s)
      = sum_c p_sc log(a_sc/rho_sc)
      <= log(1/gamma_s)=log(1+9k/(D_s+2)).                (P3)

Rows01,11 have zero loss. The right side depends only on clean counts,
with no channel randomness remaining. Apply (P3) with the actual s=S_N
before averaging. At k=0, alpha=1 and X=Z, so rho=a exactly before the
grid; no visit-tail restriction is needed for its zero added term.

## 9. Reciprocal visits and actual terminal weighting

For k>=1 the public domain forces M>=1024, so both clean visit estimates
(C1.16)-(C1.17), proved in §5.1, apply. Set x=Mu. Since 1/(D+2)<=1/2,
splitting on the good visit event yields

    E_stat[1/(D_00+2)]
      <= 128/(x+256)+(1/2)exp(-x/512)
      <= 512/(1+x).                                    (P4)

After multiplication by 1+x, the first term is at most 128 and the
second at most (1+512/e)/2, whose sum is less than 257. This includes
x<1. Similarly d_vis>=M/128 and
{D_10<M/128} is contained in {D_10<d_vis}, so

    E_stat[1/(D_10+2)]
      <= 128/(M+256)+(1/2)exp(-M/256)
      <= 512/(M+1).                                    (P5)

The multiplied terms sum to at most 128+(1+256/e)/2<193. These are
unconditional stationary-prefix expectations under the true D1 source;
no law for corrupted counts has been asserted.

The whole-prefix bridge (C1.12) and bounded-function inequality (C1.9)
apply to these clean reciprocals, with range [0,1/2], giving

    E[1/(D_00+2)|S_N=00] <= 512/(1+Mu)+d_g/2,
    E[1/(D_10+2)|S_N=10] <= 512/(M+1)+d_g/2,              (P6)
    d_g=(31/32)^floor((N-m)/3).

The bridge is applied to the true entire prefix only after the channel
has been eliminated from the pathwise bound. It is not applied to Z,
channel randomness, or an independent replacement query.

For N>=12, floor((N-m)/3)>=N/12: use N-m>=N/2 and
N/6-1>=N/12. Hence d_g<=exp(-N/384)<=384/N. For 6<=N<12, the
same bound follows from d_g<=1. Also, for every N>=6,

    M+1>=N/4,    u/(1+Mu)<=1/(M+1),
    w<1/3,      u+w=(1+2u)/3<1/2.

Weight (P6) by the actual stationary probabilities u and w from §3:

    sum_(s=00,10) pi_s E[1/(D_s+2)|S_N=s]
      <= 512u/(1+Mu)+512w/(M+1)+(u+w)d_g/2
      <= 8192/(3N)+96/N.                               (P7)

Finally log(1+z)<=z, (P3), (C1.1) and (P7) imply

    R_av(rho) <= 1000000/N+9k*(8192/3+96)/N
              = 1000000/N+25440 k/N.                   (P8)

For k=0, use rho=a and (C1.1) directly. Thus (P8) covers all N>=6 and
public k without applying large-M lemmas to small M. The channel can be
any globally legal randomized D2 rule: (P1)-(P3) hold for each seed, and
the source-only inequalities survive averaging. The source-independence
and no-future conditions of D2 are retained throughout.

## 10. Exact positive grid, independent closed counts and all corners

For N>=6 write C0,C1 for the selected dirty row counts. In this arithmetic
argument allow them to vary independently over the integers in [0,M],
with sum possibly 2M. Define

    D=C0+C1+2alpha,        Zden=4D.

This D is the smoothed selected denominator, unlike D_s in §§1-9. Since
alpha>=1, k<=M/1024 and m=M+2, the entire independent box obeys

    2<=D<=2M+6k+2<=3m,
    Zden<=12m,            2Zden<=24m.                    (G1)

Indeed 2M+6M/1024+2<=3M+6. Moreover, for c=0,1,
0<4(Cc+alpha)<Zden because the other smoothed count is positive.

The row00 candidate is exactly

    z1=min(3D,max(D,4(C1+alpha))),
    J=floor((2Q*z1+Zden)/(2Zden)),
    q00=(Q-J,J)/Q.                                      (G2)

This is nearest-integer rounding of Q*rho_00,1 with half ties upward.
For dyadic Q>=4, Q/4 and 3Q/4 are integers. As z1/Zden is in [1/4,3/4],
J is in [Q/4,3Q/4] and

    |J/Q-rho_00,1|<=1/(2Q).                              (G3)

Thus both output numerators are positive. At Q=4 the internal thresholds
are 3/8 and 5/8; equality returns 1/2 and 3/4 respectively. The interval
endpoints remain 1/4 and 3/4. This includes every tie, regardless of whether
a particular pair of counts realizes the threshold.

The row10 candidate is exactly

    z0=min(3D,4(C0+alpha)),  z1=Zden-z0,
    j_c=floor(((Q-1)*z_c+Zden-1)/Zden)
       =ceil((Q-1)*z_c/Zden),  c=0,1,
    e=Q-j0-j1,             q10=(j0,j1+e)/Q.              (G4)

Q-1 and Zden-1 subtract literal 1, not alpha. Both z_c lie strictly between
0 and Zden. The two pre-ceiling quantities sum to the integer Q-1. If they
are integers, their ceiling sum is Q-1; otherwise their nonzero fractional
parts sum to 1, so their ceiling sum is Q. Hence e belongs to {0,1},
j0,j1>=1, and j0+j1<=Q. Both final numerators are in [1,Q-1] and sum
to Q. Exact divisibility, nonzero remainders and zero residual are covered.
For both coordinates,

    q10_c >= (1-1/Q)*rho_10,c.                            (G5)

Rows01,11 use uniform, as does public Q=2. At Q=2 the eagerly evaluated
row00 candidate can have J=2 and Q-J=0, but J remains in [1,2] and every
division/subtraction is defined. The final uniform selection discards it
and returns (1,1)/2. Row10 at Q=2 has j0=j1=1 and e=0. No logarithm or
loss of an unused zero-coordinate candidate is evaluated by the algorithm.

If C0=C1=0, both pre-grid rows are uniform: (G2) returns J=Q/2, while
in (G4) each ceiling of (Q-1)/2 is Q/2 since Q is even, and e=0. Thus
both return uniform. With only one zero count, alpha>0 keeps all smoothed
coordinates positive; the preceding proofs apply without an exception.

All eagerly evaluated candidates obey these whole-box integer guards,
including Q=2 and uniform terminal branches:

    0<z1_(nearest)<=3D,
    nearfull=2Q*z1_(nearest)<=6QD,
    nearnum=2Q*z1_(nearest)+Zden <=(6Q+4)D
            <=8QD<=24mQ<32mQ,
    0<z_c_(ceiling)<Zden,
    ceilnum_c=(Q-1)*z_c_(ceiling)+Zden-1
              <Q*Zden<=12mQ.                           (G6)

Every divisor is positive; Q-J, Zden-z0, Q-1, Zden-1 and e are
nonnegative. Exact division's remainder is below 2Zden for the nearest
candidate and below Zden for each ceiling. Thus (G2)-(G4) define a finite
integer function on every independent closed count pair, without an
appeal to realizability or modular-overflow conventions. Products are
full integers; C3's finite-width/physical cost construction is separate.
The selected final numerators sum to Q and lie in [1,Q-1]. Each, and the
literal denominator Q, fits b+1 bits, giving the specified 3(b+1)-bit port.
After these writes, erasing every other mutable cell is a deterministic
finite continuation and supplies no clean side input.

## 11. Grid loss transfer and the required upper

For Q>=4 and row00, set p=t, v=rho_00,1 and q=J/Q. All lie in
[1/4,3/4]. The Bernoulli bounds (C1.6)-(C1.7), (G3) and the square
triangle bound yield, for each individual history and channel seed,

    kl(p,q) <= (16/3)(p-q)^2
            <= (32/3)(p-v)^2+8/(3Q^2)
            <= (16/3)kl(p,v)+8/(3Q^2).                  (G7)

For row10, coordinate domination (G5) yields

    KL(p_10||q10) <= KL(p_10||rho_10)-log(1-1/Q)
                  <= KL(p_10||rho_10)+2/Q,              (G8)

using -log(1-z)<=z/(1-z)<=2z for 0<=z<=1/2. Rows01,11 have zero loss.
Nonnegativity of KL permits the common multiplier 16/3. Average these
pathwise inequalities over the actual terminal query, source and channel
coins, without making the terminal pair independent of any count. With
(P8) and the loose sum of the two grid remainders,

    R_av(A,T;u,t)
      <= (16/3)R_av(rho)+8/(3Q^2)+2/Q
      <= 16000000/(3N)+135680 k/N+3/Q,                   (G9)

because (16/3)*25440=135680 and 8/(3Q^2)+2/Q<=3/Q for Q>=4.
At Q=2 the actual output is uniform, with
KL(p_s||uniform)<=log2<3/2=3/Q, so (T) follows without (G7).
For N=3,4,5 the genuine uniform no-prefix branch has loss at most log2,
which is less than 16000000/(3N), proving (T) for every public Q and
k=0 in that branch. No statistical padding to N=6 is used.

One parameter-free deterministic family therefore satisfies (T) for
all stated parameters and admissible channels. Every use of stationarity,
reverse conditioning, visits or martingales concerns X only. Corruption
enters only through the deterministic per-seed window bound. Clean counts
and the comparator remain proof variables. This proves precisely the
selected C1 claim, subject to the normal independent truth-gateway verdict.

## Appendix P. Fixed sources, not proof predecessors

- current project; `PROBLEM.md`; SHA256 `960299dbb9730b6f8b7d9de81128fabcca03b7342a456beb57572e52d490caca`; D1-D7, exact C1.
- responsibility instructions; `inputs/AUTONOMOUS_RESEARCH.md`; SHA256 `e21e211cfda567f2f5bdca8b5bc7bd42fd59527938bc1ec77d5e50ff22003424`; scope and execution.
- Prover stage4; `inputs/source-stage4/outputs/001-relative-code/prover/c1-proof-v2.md`; SHA256 `f8f6a56b4b458ff3d0033fa8cd29d27e3e32067dd643c2a9e51ba411ed6dadcf`; clean proof and elementary inequalities §§1-7.
- Prover probe012; `inputs/source-stage4/outputs/012-input-contamination/prover/upper-program-certificate-v1.md`; SHA256 `b1a0de75230bb5ec2cd58417e09f2c0bb3ca7818e2fd513c6e0333f81b7beab4`; pollution, reciprocal, grid §§1-4.


---

# C2 complete current proof

Source: `outputs/001-input-contamination/counter/c2-proof-v1.md`; SHA256 `f10c16cca4efde271b33c3fa2de62244098912c110991b30ccd4e40489852e99`. Source text follows unchanged.

# C2: self-contained common-channel full-history lower, v1

Counter, 2026-10-26. Fixed fifth-stage proof for current obligation
`52a14a0c60279133c7acc7067c15eb4cfbff32368f8a721e59df9bf3eecd9ff1`.
Predecessors: `[]`. Assumptions: exactly current PROBLEM.md D1-D2 and D6.
No historical Fact, old root, file review, primary theorem, diagnostic, or
architecture-restricted observation premise is used below.

Provenance: adapted from the supplied source-stage4 probe012 Counter
common-channel-lower-v1.md. Its old C1 admission interface is removed;
stationarity, reversal, common atom and contraction are proved directly here.
The original source files are unchanged. Grid parameter Q is public; letters
P,Q in the finite transport lemma denote two laws only. The stationary pair
law is pi; a coupling of full histories is a separate object.

## 1. Exact statement and quantifiers

Fix integers N>=6, m=floor(N/2), M=m-2 and
1<=k<=floor(M/1024). Put

    u0=k/N, Delta=1/640000,
    t_-=1/2-Delta/2, t_+=1/2+Delta/2,
    c=Delta²/8=1/3276800000000.                         (1)

There exists one source-independent randomized batch channel T_(N,k),
independent of the predictor and of Q, such that for EVERY binary input x and
EVERY channel seed it keeps x_(N-1),x_N and changes at most k other bits, and

    TV(L_(u0,t_+)(Z | S_N=00),
       L_(u0,t_-)(Z | S_N=00)) <= 1/64.                (1a)

For every public Q and every common randomized predictor whose data are
Z=T(X),N,k,Q, including unrestricted probability outputs, unlimited
computation, and even knowledge of the public two-point experiment/T, one
SAME t_* in {t_-,t_+}, at u=u0, satisfies

    R_00 >= c,                 R_av >= c k/N.           (2)

The channel has no future X_(N+1), realized hidden parameter/label, clean
side channel or source-dependent seed. Its independent private seed is not
given to the predictor. It may inspect the entire already observed history,
including its preserved terminal pair: this is a batch channel, not a
time-causal sensor. The predictor remains an unknown-u,t procedure on all D1;
only the lower-bound witnesses are fixed by (1). For k=0 define the channel
as identity; this lower asserts nothing at k=0. N=3,4,5 therefore have identity
contamination and the separate uniform predictor branch, with no fake prefix.

## 2. Finite residual transport without normalization

Let E be a finite Hamming fiber consisting of binary strings with the same
last pair. Let P,Q be probability laws on E and mu=P-Q. Write

    mu_+(x)=max(mu(x),0), mu_-(x)=max(-mu(x),0),
    tau=sum mu_+=sum mu_-=TV(P,Q).

TV uses sup-event distance, equal to half the L1 norm for probability laws.
The Jordan parts here retain mass tau; they are NOT normalized to mass1.
Take any coupling Pi of P,Q, with Hamming cost
C=sum_(x,y) Pi(x,y)d(x,y).

The off-diagonal quantities f(x,y)=Pi(x,y), x!=y, form a directed flow with
outgoing-minus-incoming divergence P(x)-Q(x)=mu(x). First remove directed
cycles. On each positive-flow cycle subtract its minimum edge weight from
every cycle edge. Divergence is unchanged, no new edge is added, at least
one edge disappears, and cost cannot increase. A fixed lexicographic rule
makes the procedure deterministic; finitely many steps give an acyclic flow.

Add a super-source a with edges a->x of weight mu_+(x), and a super-sink b
with edges y->b of weight mu_-(y). Every original vertex is now balanced.
The augmented graph is acyclic. If source flow remains, follow positive
edges from a. An intermediate vertex reached by positive flow has a positive
outgoing edge by balance. Acyclicity forces the path to end at b. Subtract
the smallest edge weight along this path, and record that amount lambda
on the original endpoint pair x,y. Balance persists; at least one edge
disappears. Repeating terminates after finitely many removals. When no source
edge remains, there can be no nonzero balanced acyclic residual component:
such a component would have a vertex with incoming0 and outgoing>0.

Consequently the recorded endpoint weights Gamma(x,y) have marginals
mu_+,mu_-. In particular their TOTAL MASS is tau. They go only from
positive-divergence to negative-divergence vertices. Triangle inequality
along each collapsed path gives

    sum Gamma(x,y)d(x,y) <= C.                         (3)

This proof permits transshipment through vertices of any divergence sign;
the super-source/sink capacities account exactly for the Jordan endpoints.
It is not an assertion that the original coupling restricted to positive and
negative supports already has those marginals. If tau=0 all flow can be
removed as cycles and Gamma is empty. Rational Pi gives rational Gamma.

## 3. One kernel on every input, with a hard bound for every seed

Fix integer k>=1. For each Gamma edge with d(x,y)<=2k, list the differing
coordinates in a fixed public order (low-to-high bits of the stored encoding)
and change the first floor(d(x,y)/2) of them
in x to their values in y. Call the result z_xy. Then

    d(x,z_xy)=floor(d(x,y)/2)<=k,
    d(y,z_xy)=ceil(d(x,y)/2)<=k.

The protected tail is identical throughout the fiber. This is a fixed
Hamming midpoint, not an assumption about midpoints in arbitrary metrics.
Call such edges good, and the remaining edges bad. Define rows as follows:

* If mu(x)>0, the row at x has weight Gamma(x,y)/mu_+(x) for each outgoing
  edge, sending it to z_xy when good and to x when bad.
* If mu(y)<0, the row at y has weight Gamma(x,y)/mu_-(y) for each incoming
  edge, sending it to the SAME z_xy when good and to y when bad.
* If mu(v)=0, its row is identity.

Every row sums1 by the Gamma marginal identities, including tau=0 by
using identity everywhere. Positive and negative supports are disjoint, so
an input has exactly ONE row K(v,.), fixed without the true source label.
For an explicit bad-fraction identity define, on the indicated supports,

    b_+(x)=sum_(y:bad) Gamma(x,y)/mu_+(x),
    b_-(y)=sum_(x:bad) Gamma(x,y)/mu_-(y).

Each is in[0,1]; its entire row fraction remains at that input. If
m(v)=min(P(v),Q(v)), then P=m+mu_+, Q=m+mu_- and hence

    PK=mK+mu_+ K,   QK=mK+mu_- K.

In particular mK cancels because it is subjected to the SAME K(v,.) at each
input under both laws. It need not remain at v and is not given a fictitious
identity branch. Expanding the residual rows gives the exact identities

    (P-Q)K=sum_bad Gamma(x,y)(delta_x-delta_y)
          =sum_x mu_+(x)b_+(x)delta_x
           -sum_y mu_-(y)b_-(y)delta_y,
    B:=sum_bad Gamma(x,y)
      =sum_x mu_+(x)b_+(x)=sum_y mu_-(y)b_-(y),
    TV(PK,QK)=B<=sum Gamma(x,y)d(x,y)/(2k)<=C/(2k).     (4)

The equality TV=B follows because the positive and negative residual
supports in this display are disjoint. The good signed masses cancel
exactly at the SAME z_xy, including when midpoint outputs collide with
other inputs. Bad edges satisfy d>2k, so their mass is bounded as displayed.
No division by tau has occurred: Gamma and B retain their original masses.

Every nonzero row outcome moves at most k bits, even on bad edges, since
bad fractions stay at the input. This proves support legality on ALL inputs,
not just in expectation. For rational laws and coupling all row probabilities
are rational. Choose a common denominator D for all entries of the finitely
many rows. In a fixed ordering of a row's distinct outputs write their
probabilities as n_1/D,...,n_r/D, with integer n_i>=0 and sum_i n_i=D.
An independent uniform seed J in {0,...,D-1} chooses output i exactly when
sum_(a<i)n_a<=J<sum_(a<=i)n_a; zero-size intervals are skipped. This fixed
interval partition realizes K. Every seed at every input selects
a supported legal output. D may be enormous; the channel's computation and
randomness are external/unrestricted in this experiment. This is a finite
existence construction, not a claim of an efficient adversary.

## 4. The two true conditional history laws and reverse kernels

For D1 set w=(1-u)/3, r_t=ut/w. Since 0<u<1/4,
0<u/w=3u/(1-u)<1; hence 0<r_t<3/4 and 1-r_t>1/4.
The forward pair matrix, in order00,01,10,11, is directly

    F_t=[[1-t,t,0,0], [0,0,1/2,1/2],
         [r_t,1-r_t,0,0], [0,0,1/2,1/2]].

For pi=(u,w,w,w), multiplication gives

    pi F_t=(u(1-t)+wr_t, ut+w(1-r_t), w, w)
          =(u,w,w,w)=pi,

using wr_t=ut. All four masses are positive and sum1. Start with pi as
D1 requires; thus every pair S_i has this stationary law.
For any supported transition i->j, Bayes' formula gives the predecessor
probability pi(i)F_t(i,j)/pi(j). Its rows are therefore exactly

    R_t=[[1-t,0,t,0], [r_t,0,1-r_t,0],
         [0,1/2,0,1/2], [0,1/2,0,1/2]].               (5)

For example reverse00 receives contributions u(1-t)/u and wr_t/u=t;
reverse01 receives ut/w=r_t and w(1-r_t)/w; reverse10 and reverse11
each receive w/(2w) from01 and11. All omitted entries are0. These rows
sum1 and pi R_t=pi, either by the displayed entries or by summing
pi(j)R_t(j,i)=pi(i)F_t(i,j) over j.

For every legal lower tuple, k<=M/1024<N/2048, so
0<u0=k/N<1/2048<1/4. Both t_± lie in[1/4,3/4]. Thus these are legal D1
sources. Each allowed appended bit has strictly positive probability, so
every binary input in a terminal fiber has positive conditional probability.

Here are actual THREE-transition reverse paths to c0=10:

    start    path                         path probability
    00       00 -> 10 -> 01 -> 10          t(1-r_t)/2
    01       01 -> 10 -> 01 -> 10          (1-r_t)^2/2
    10       10 -> 11 -> 01 -> 10          (1-r_t)/4
    11       11 -> 11 -> 01 -> 10          (1-r_t)/4.

Because t>=1/4 and 1-r_t>=1/4, every listed probability is>=1/32.
Consequently R_t^3(s,10)>=alpha:=1/32 for every s and every D1 parameter.
Put beta=31/32 and define the actual stochastic matrix

    B_t(s,e)=(R_t^3(s,e)-alpha*1{e=10})/beta.

Nonnegativity and row sums1 follow from the preceding bound. For any two
probability laws a,b on the four states,
(a-b)R_t^3=beta(a-b)B_t. A stochastic matrix contracts finite TV:
for a signed mass v, sum_e |sum_s v(s)B_t(s,e)|<=sum_s |v(s)|.
Since pi R_t=pi, iteration in blocks of3 and contraction of the remaining
0,1,2 steps imply

    R_t^3(s,.)=alpha delta_c0+beta B_t(s,.),
    TV(R_t^j(s,.),pi)<=D_j:=beta^floor(j/3),
    sum_(j>=0)D_j=3/(1-beta)=96.                      (6)

This directly proves the common atom and all contraction estimates used
below. Stationary reversal does not make the terminal query independent.

Let H=N-2. Under the true conditional law given S_N=00, write

    A_j=S_(N-j)=(X_(N-j-1),X_(N-j)), 0<=j<=H.

Indeed multiplying pi(s_(i+1))R_t(s_(i+1),s_i)
=pi(s_i)F_t(s_i,s_(i+1)) along any supported path telescopes to

    pi(s2) product_(i=2)^(N-1) F_t(s_i,s_(i+1))
      =pi(sN) product_(i=2)^(N-1) R_t(s_(i+1),s_i).

Unsupported paths have weight0 on both sides. Divide by the actual
Pr(S_N=00)=u and set sN=00: A_0=00 and A is exactly a length-H R_t path
under the true conditional history law. The reverse support imposes
second(A_(j+1))=first(A_j), so each such pair path reconstructs one and
only one binary history with that terminal pair. It includes all input symbols, with no crop/count substitution
and no TV error amplified by the rare factor1/u. We now
couple A^+ and A^- with kernels R_+,R_- and common starting state00.

The one-step row TV difference is

    h(00)=Delta, h(01)=(u/w)Delta, h(10)=h(11)=0,
    0<=h<=Delta, pi h=2uDelta.                         (7)

## 5. An adaptive coupling of complete paths

At a decision boundary whose states match at s, use a maximal ONE-step
coupling of R_+(s,.) and R_-(s,.). Explicitly place min of their point masses
on each equal-state pair. Write d(e)=min(R_+(s,e),R_-(s,e)) and
l_±(e)=R_±(s,e)-d(e). If h(s)>0, place residual joint mass
l_+(e)l_-(f)/h(s) on(e,f); if h(s)=0 use only the diagonal mass.
The residual supports are disjoint and their masses both equal h(s), so
this is a rational maximal coupling with mismatch probability exactly h(s).
A mismatch at this step is an episode birth.

At a decision boundary with states a!=b, commit to THREE transitions.
First couple endpoints using (6): with an independent probability alpha,
both endpoints equal c0; otherwise draw endpoints from B_+(a,.) and B_-(b,.)
(independently is sufficient). Given the endpoints, independently sample
the actual conditional three-step path of each individual chain. For example
the plus bridge through v1,v2 to e has probability

    R_+(a,v1)R_+(v1,v2)R_+(v2,e)/R_+³(a,e).            (8)

Zero endpoint probabilities are never selected. Multiplying (8) by the
endpoint marginal shows that the entire plus block has precisely its genuine
three-transition Markov path law; the same holds for minus. In particular
neither of the two intermediate pairs is omitted. The chance that the
endpoints match is at least alpha, whether or not the residual draws happen
also to match. Decisions resume only at the end of this committed block;
coincidence at an intermediate pair does NOT terminate the commitment.

If only one or two transitions remain before H, sample the same full block
and keep its corresponding prefix, stopping the observed construction at H.
Equation (8) implies every such truncated prefix has its genuine one-chain
Markov marginal. Auxiliary unused draws are integration variables in this
finite coupling, not extra clean observations supplied to the channel or
predictor, and have no relation to the invisible future target Y.

### Why adaptive block choices preserve the full one-chain law

A proof is needed because, inside a coupled block, conditioning on BOTH
chains' intermediate history need not give the single-chain transition R_t.
We do not make that false claim.

Conceal unused block draws until their pair positions are revealed. Boundary
times tau_i are stopping times for this reveal process with its commitment
phase; at a boundary, the next scheduled length1 or3 is a function only of
the two current states. The drawn block's individual marginal, conditional
on the entire joint boundary past, is the appropriate Markov block from that
chain's current state, as just proved. There is no adaptive decision inside
a committed block.

For a fixed position j<H, partition according to the last boundary tau<=j
and its scheduled length. The event that j lies in that block is determined
at its start: its length is already fixed there. Conditional on the joint
past AT THAT START and on this chain's own revealed prefix within the block,
its next transition has law R_t at its present state. This follows by
disintegrating that block's genuine Markov marginal; information from the
other chain's intermediate coordinates is not conditioned upon. For any
bounded test function of this chain's path through j, integrate this equality
on each disjoint block-start event and sum over starts. This proves

    E[f(A_(j+1)) | A_0,...,A_j]=R_t f(A_j).

More formally, for each possible start tau and scheduled length l, let
E_(tau,l) be the event that a boundary occurs there, chooses length l, and
tau<=j<tau+l. For fixed j<H these events are disjoint and exhaust the
sample space. Each event is measurable at that start, with no condition on
later coordinates. For any bounded g of this chain's history through j,
the conditional block-marginal calculation gives

    E[1_(E_(tau,l))*g*(f(A_(j+1))-R_t f(A_j))]=0.

Summing yields the conditional transition identity above, even though the
start events need not be measurable from this chain's history alone. This
also applies to a truncated final block since j<H. Induction proves the
ENTIRE individual path law, not merely state marginals or boundary laws.
Revealing endpoints in advance and then using them as decision information
inside the block would invalidate the argument; the committed rule avoids it.

## 6. Episode charging and every-symbol Hamming cost

Suppose a birth occurs on a matched one-step decision j->j+1. Charge the
born pair position j+1 once. Recovery then consists of committed three-step
attempts until the first matched decision boundary, or the horizon. Given
the history and born pair, each attempted full block fails to match endpoints
with conditional probability at most beta, uniformly in its starting states.
By induction, the probability that the r-th recovery attempt is started is
at most beta^(r-1). This uses fresh block coins, not independence of the
pair states at stopping times. Hence the conditional expected number of
attempts started is at most sum_(r>=0) beta^r=32.

Count a final partial block as a full3 for this upper bound. Its START is
preceded only by full failed blocks, so the same tail bound on starting it
applies. A born episode's total charged positions consequently have
conditional expectation at most

    1+3*32=97.                                        (9)

Intermediate equal pairs cost0 but may be overcharged until the commitment
ends. Each actual disagreement belongs to an episode: initial states match,
and a new disagreement outside recovery can only arise at a matched
one-step decision. Episodes need not have independent lengths.

Let I_j indicate that j is a matched one-step decision boundary and B_j
indicate its mismatch birth (both are0 when j is inside a committed block).
On the boundary event the maximal coupling gives birth probability h(A_j^+).
Taking conditional expectation there and setting the complement to0 yields
E B_j=E[I_j h(A_j^+)]. Therefore

    E B_j<=E h(A_j^+).

Use (9) AFTER conditioning on a birth and its actual born states; its bound
is uniform. The tower property and finite summation give

    E sum_(j=1)^H 1{A_j^+!=A_j^-}
       <=97 sum_(j=0)^(H-1) E B_j
       <=97 sum_(j=0)^(H-1) E h(A_j^+).                (10)

By the full marginal result and (6),(7), the difference from stationary
expectation is at most Delta times TV: apply 0<=h<=Delta separately to
the positive and negative parts of the zero-total-mass law difference.
Thus

    E h(A_j^+) <=2uDelta+Delta D_j,
    sum_(j=0)^(H-1) E h(A_j^+) <=2NuDelta+96Delta.     (11)

For each FREE symbol X_i, 1<=i<=N-2, its associated reversed pair is
A_(N-i-1)=S_(i+1), and its FIRST component is X_i. Equivalently the first
components of A_1,...,A_H are X_(N-2),...,X_1. Thus

    d_Ham(X^+,X^-)
      =sum_(j=1)^H 1{first(A_j^+)!=first(A_j^-)}
      <=sum_(j=1)^H 1{A_j^+!=A_j^-}.                   (12)

The last two symbols are both00. No free symbol, including X1, is missing
or counted using an endpoint-only proxy. Combining (10)–(12) supplies a
coupling Pi of the TWO TRUE CONDITIONAL HISTORY LAWS P,Q with cost

    C<=97(2Nu+96)Delta<=10000(1+Nu)Delta.              (13)

The last inequality compares coefficients: 194<=10000 and9312<=10000.
This proves the proposed path bridge with its original constants. No seed
replacement, clean oracle or weaker observation space is needed.

## 7. The global common observation channel

Take u=u0=k/N in the preceding construction, so Nu=k. From (1),(13),

    C<=10000(1+k)Delta=(1+k)/64<=k/32.                (14)

Use that CONDITIONAL coupling Pi in §§2–3 on the terminal00 fiber. It
produces one kernel K with TV(PK,QK)<=1/64 by (4),(14). Extend it to a
global T by identity on all other terminal fibers. Each row preserves its
tail and has support within k edits in the first N-2 bits. Every raw binary
input belongs to exactly one such fiber, including inputs unlikely for either
witness. Full support of D1 makes all conditional P,Q masses rational and
positive; mu=0 cases were explicitly given rows anyway.

The design is an offline finite function of PUBLIC N,k. All entries of
F_±,R_±,pi, the maximal couplings, common-atom endpoint distributions,
and positive-denominator bridges are rational at the fixed witness pair.
The adaptive sampling tree has finite depth (at most H blocks, with only
its last block possibly extending by two auxiliary positions). Summing
its finitely many rational branch weights gives a rational coupling of
complete histories. Enumerate the two rational conditional laws and this
fixed coupling, remove cycles/collapse paths using fixed lexicographic
choices, form the midpoint rows, and store them. All operations preserve
rationality. Take the least common multiple of the finitely many positive
row denominators, including the identity rows on other fibers, and realize
T with the independent uniform integer seed from section3. This enumerates
a finite globally defined input/seed function without an average-only
legality exception. A random seed then selects that ONE row at the
actual observed x. In particular T does NOT run the plus conditional
coupling when the true source is plus and the minus coupling otherwise.
The reverse coupling is only a device for computing a fixed transport table.
The residual sign mu(x) used to define the row is a fixed function of x,
not a read of the actual hidden source label. Publicly selecting u0=k/N for
a difficult subproblem is therefore different from providing hidden u to an
unknown-parameter predictor or choosing source-dependent private coins.

The same T is legal when any other D1 u,t happens to generate the input;
only its bad-risk guarantee is restricted to the pair (1). T is independent
of Q and every post-observation encoder/predictor. Its private finite seed
is independent of the source and not disclosed. The observation-law TV
bound is for Z marginalized over that seed; no claim is made that it holds
conditional on each seed, or that a deterministic common attack attains it.

Since T preserves S_N, the actual conditional observed laws given S_N=00
are EXACTLY PK and QK. We have not asserted small unconditional history TV,
conditioned on independent queries, or replaced the true terminal pair.
Y=X_(N+1) was never observed. By D1's second-order Markov property,
Pr(Y=1 | X_1^N,channel coins,predictor coins)=p_(u,t)(1|S_N).
The preserved S_N is a function of Z; conditioning further down to Z
therefore leaves this same target. In particular on the actual event
S_N=00 the target is Bernoulli(t). The risk definitions used below are
R_00=E[kl(t,q1)|S_N=00] and
R_av=E[KL(p_(u,t)(.|S_N)||q)], including both independent private coins.
This is exactly the D1 excess log-loss experiment.

## 8. Arbitrary full-Z randomized predictors and the same witness

Fix any common randomized predictor from Z,N,k,Q to q=(1-q1,q1). Its fresh
private randomization is a common Markov kernel and cannot increase TV.
Even prior knowledge of T and the public witness pair could be supplied
without weakening the following bound. Threshold q1 at1/2 to test plus
against minus. On a testing mistake, |q1-t|>=Delta/2. For Bernoulli laws,
kl(t,q)>=2(t-q)²: integrate derivative (q-t)/(q(1-q)) and use q(1-q)<=1/4.
At q=0 or1 the interior target has infinite KL, so endpoints cause no gap.
Each mistake costs at least Delta²/2.

Let L_- and L_+ denote the two actual conditional Z laws. For any randomized
test with plus-decision probability a(z) in[0,1],

    err_-+err_+=1-[integral a dL_+-integral a dL_-]
              >=1-TV(L_-,L_+)>=63/64.

Indeed sum_z a(z)(L_+(z)-L_-(z)) is at most the positive Jordan mass
TV(L_-,L_+) because 0<=a<=1. This also proves the randomized testing
bound directly, without any restriction on the predictor's output format.
The unordered pair of laws is {PK,QK}. Hence

    max_(t=t_-,t_+) R_00
      >=(Delta²/4)(1-1/64)>=Delta²/8=c.                (15)

Choose one t_* attaining this two-element maximum. On that SAME source
and SAME T, nonnegativity of KL and stationarity yield

    R_av>=Pr(S_N=00)R_00=u0 R_00>=c k/N.              (16)

This proves (2) for all full-Z predictors, including all encoders, infinite
computation and unrestricted probability outputs. It does not say every
source suffers (2), every admissible attack is bad, the terminal query can be
changed, or old fixed-FULL19 results imply this lower. Exact input loss
occurs before every encoder, so later re-encoding/locked-output tricks
cannot restore an unobserved clean history. The strongest comparison
baseline here is expressly allowed to use every observed Z symbol.

## 9. Dependency and scope certificate

Every load-bearing lemma is proved in sections2-8 from D1-D2. Section4
establishes the source and mixing calculations directly; section5 proves
full-path marginals rather than only endpoints. All N,k in the exact C2
domain are covered. No property of D3-D5 is needed for this stronger lower.
The conclusion applies to DIRECT, JOINT, and every other full-Z randomized
predictor, even unlimited ones. Their finite implementation/cost properties
remain separate current-project obligations.

For root integration the quantifiers are

    for every legal (N,k>=1), exists one T_(N,k),
    for every Q and every common full-Z predictor A,
    exists t_* in {t_-,t_+} with BOTH inequalities(2).

The one channel is globally hard-k for every binary input and every seed,
fixed before A and independent of Q and the actual source label. The TV
and risk bounds average its private seed. No all-source bad-risk statement,
deterministic-channel attainment, small unconditional history TV, matched
1/N or 1/Q lower, JOINT superiority, novelty, or all-layer/IEEE/sensor
conclusion follows. The separate d6-scope-map-v1.md gives the exact bounded
primary/strong-DIRECT mapping; it is scope provenance, not a premise here.

Prior diagnostic code/results were not rerun and are not proof dependencies.
GPU work is0. The research policy limits GPU to0, so the reserved GPU
quantity for final audit is0 as well; the remaining dimensions are unlimited.
The current C2 proof will use the normal truth gateway with predecessors=[];
only its actual returned verdict and identifiers establish admission.


---

# C3 complete current proof

Source: `outputs/001-input-contamination/prover/c3-proof-v1.md`; SHA256 `5ac089baa1a28d2f89db223e16542ba43ac153c6930e81806c6627d0e0e22827`. Source text follows unchanged.

# Stage5 C3: explicit affine emitter, finite programs and separate full costs

Prover, 2026-10-26. Fixed proof v1.
Obligation `c9d1bbb51ee633f91f029e917ded7f6e1de7f6e9e227f681761ee9ed66b81bec`.
Contract `873515c4586d37a2bde324010bea6ae30f820927b7c25ded15b784a79eef7e45`.
Predecessors: **[]**. All finite premises used here are proved below.

## 0. Claim and interpretation

There exist the two D4 implementations of the exact D3 function, agreeing
on every individual binary observation Z and legal public tuple, within
EVERY corresponding D5 bound. DIRECT is a packed bit-register owned-batch
machine; JOINT is the principal extracted-query batch hybrid with tied
dense tokenwise affine/ReLU layers and a separately charged finite evaluator.
One Boolean neural channel occupies a full beta-bit physical scalar.
Neither implementation is assigned the other's accounting model.

This proof contains no probability argument or C1/C2 reproving. Their
current accepted Facts are not needed as predecessors: the elementary
output guards are proved again locally as finite-domain statements.
Historical files and the new affine-emitter seed are sources, not Facts.
The new seed's concrete two-layer coefficients, alias rule and address
bound are proved and connected to actual primitives and generation here.
Only local workspace copies are used; no old diagnostic is rerun. This
[Non-scientific operational metadata omitted.]
model, counter, contract or resource formula. It does not submit the root.

All arrays mentioned below have explicit bounded rectangular indices.
A bit-register READ/WRITE accesses a labelled bit cell; full words are
read/written bit by bit. Address arithmetic, instruction and coefficient
fetches and dispatch are charged in §10. This is the D5 machine interface,
not a unit-cost arbitrary-integer operation. A finite program/generator
may be specified by bounded loops without allocating its enormous output
inside the proof checker. §§3-4,9-11 give those loops and their expansions.
The companion iterator is a transcription aid; no theorem here depends
on executing Python or treating its integers/GC as hardware primitives.

## 1. Parameters, representations and exact algorithm

Let N>=3, Q=2^b, integer b>=1. For N>=6 define m=floor(N/2), M=m-2,
0<=k<=floor(M/1024), n=N+1, ell=ceil(log2(N+2)), tau=bitlength(k+1),

    h=ceil(log2(256(N-2))), A=2^h,
    p=4h+4ceil(log2(m+4))+64, R_s=2^p,
    s=ell+b+tau+p+32, beta=128s, g=1024beta^2.

For N=3,4,5, k=0 and s=ell+b+tau+32; do not instantiate m,M,h,A,p,
heads or prefix builders. Always n=N+1, Z_meta=1024ns=8n beta.
In particular s>=37 and beta>=4736. In the large branch h>=10,p>=116,
p>=h and h+b+ell+tau<=s. Integers, exponent lengths and powers of two
are computed from public parameters before observations arrive.

In a finite evaluator, an unsigned beta-bit word is a packed field. In a
neural state its bit representation uses beta Boolean scalar channels,
each with beta physical bits. A scalar integer such as a head output is
one beta-bit scalar until the explicit extraction in §6. Full products and
quotients occupy 2beta bits in scratch until justified casts. Signed dense
coefficients use beta-bit two's-complement storage and are decoded signed;
all persistent algorithmic quantities in the present word program are
nonnegative. MAC scratch retains the sign and full product. No modular
product, shortened shifted remainder or unit-cost DIV is used.

For every observed binary string Z, C_sc(Z) counts triples ending at
3,...,m, with preceding pair s and final bit c. Each C_sc is in [0,M].
DIRECT computes the eight integers directly. JOINT computes
j_sc=floor(A C_sc/M) by its actual finite head and appends eleven zero
words; the first eight coordinates have order 000,001,010,011,100,101,110,111.
Both compute eight endpoint controls from observed bits only: four
one-hots for (Z_(N-1),Z_N), followed by four for (Z_(m-1),Z_m).
These are dirty controls, never supplied clean endpoints. Let a,bq be
the actual observed terminal bits. The two ORs extracting them are

    a = ctl[2] OR ctl[3],   bq = ctl[1] OR ctl[3].

After selected-row acquisition each runs the identical 46-operation table
below with alpha=3k+1. The returned port consists of out0,out1,Q, each
b+1 bits, least-significant bit first, and every other source-bearing
location is physically erased. All inputs are Z,N,k,Q; there is no clean
history, parameter, seed or alternative count input.

## 2. Complete selected-row and output tables

Each named result below is a distinct beta-bit SSA destination; repeated
names between tables receive distinct table prefixes. OR/MUX act on the
Boolean control bits. Word MUX(c,x,y) selects x when c=1 and y otherwise.
The JOINT two control ORs above precede these fifteen operations:

| # | destination | operation |
|---:|---|---|
|1|left0|MUX bq,j010,j000|
|2|right0|MUX bq,j110,j100|
|3|selected0|MUX a,right0,left0|
|4|left1|MUX bq,j011,j001|
|5|right1|MUX bq,j111,j101|
|6|selected1|MUX a,right1,left1|
|7|qa|CONST A|
|8|twoqa|SHL qa,1|
|9|twoM|CONST 2M|
|10|full0|MUL twoM,selected0|
|11|num0|ADD full0,qa|
|12|C0|DIV num0,twoqa|
|13|full1|MUL twoM,selected1|
|14|num1|ADD full1,qa|
|15|C1|DIV num1,twoqa|

Thus JOINT uses exactly 17 selected-row operations. DIRECT uses the two
ORs and the first six MUXes with each j replaced by its eight acquired
integer C; the third and sixth destinations are C0,C1. It uses exactly
8 such operations, in addition to the acquisition scans in §5.

The common output table is exactly the following 46 operations. Here
Dsum is the unsmoothed sum, d the smoothed denominator, and Zden an
integer denominator, not the observed string. CONST0 and CONST2 are
retained real operations. The symbol one is always literal 1.

| # | destination | operation |
|---:|---|---|
|1|zero|CONST 0|
|2|one|CONST 1|
|3|kword|CONST public k|
|4|twok|SHL kword,1|
|5|threek|ADD twok,kword|
|6|alpha|ADD threek,one|
|7|twoalpha|SHL alpha,1|
|8|two|CONST 2|
|9|Qword|CONST 2^b|
|10|U|SHR Qword,1|
|11|publicUniform|CONST I{Q=2}|
|12|Dsum|ADD C0,C1|
|13|d|ADD Dsum,twoalpha|
|14|twod|SHL d,1|
|15|threed|ADD twod,d|
|16|Zden|SHL d,2|
|17|twoZ|SHL Zden,1|
|18|twoQ|SHL Qword,1|
|19|c1plus|ADD C1,alpha|
|20|raw1|SHL c1plus,2|
|21|lower1|MAX d,raw1|
|22|z1|MIN threed,lower1|
|23|nearfull|MUL twoQ,z1|
|24|nearnum|ADD nearfull,Zden|
|25|J|DIV nearnum,twoZ|
|26|near0|SUB Qword,J|
|27|c0plus|ADD C0,alpha|
|28|raw0|SHL c0plus,2|
|29|z0ceil|MIN threed,raw0|
|30|z1ceil|SUB Zden,z0ceil|
|31|Qminus|SUB Qword,one|
|32|Zminus|SUB Zden,one|
|33|ceilfull0|MUL Qminus,z0ceil|
|34|ceilnum0|ADD ceilfull0,Zminus|
|35|j0|DIV ceilnum0,Zden|
|36|ceilfull1|MUL Qminus,z1ceil|
|37|ceilnum1|ADD ceilfull1,Zminus|
|38|j1|DIV ceilnum1,Zden|
|39|jsum|ADD j0,j1|
|40|residual|SUB Qword,jsum|
|41|ceil1|ADD j1,residual|
|42|selected0|MUX a,j0,near0|
|43|selected1|MUX a,ceil1,J|
|44|uniform|OR publicUniform,bq|
|45|out0|MUX uniform,U,selected0|
|46|out1|MUX uniform,U,selected1|

There are 63 JOINT or 54 DIRECT selected-row/output word operations.
The endpoint bit bq forces rows01/11 uniform; when bq=0, a distinguishes
00 from10. Thus the final terminal MUXes implement exactly the D3 cases.

### 2.1 Guards on independent closed inputs, not just real histories

For arbitrary independent j in [0,A], floor((2Mj+A)/(2A)) is in [0,M]:
the dividend is at most A(2M+1), and its ratio is at most M+1/2.
For actual j=floor(AC/M),

    0 <= C-Mj/A < M/A <= 1/256 < 1/2.

Indeed A>=256(N-2)>256M. Consequently nearest snapping returns exactly C.
Selection uses only the observed terminal controls. Eleven unused words
may independently lie in [0,A]; they are read, retained and later cleared,
but cannot affect the selected result. Controls may be either valid pair
one-hot independently; no source consistency is needed for the guards.

For independent C0,C1 in [0,M], not assuming their sum <=M, put
D=C0+C1+2alpha, Zden=4D. Then

    2<=D<=2M+6k+2<=3m,
    Zden<=12m, 2Zden<=24m, 0<4(Cc+alpha)<Zden.

The last strict inequality follows because the other smoothed count is
positive. Nearest z1 lies in [D,3D]. Thus J rounds Q*z1/Zden to nearest,
with half ties upward. If Q>=4, Q/4 and3Q/4 are integers, so
Q/4<=J<=3Q/4. At Q=4 the switch points 3/8 and5/8 select 1/2 and3/4
at equality. If Q=2, 1<=J<=2; the possible zero in Q-J is unused because
publicUniform selects (1,1). No unused candidate is evaluated as a log.

For the ceiling branch both z_c are in (0,Zden) and sum to Zden. The
unrounded (Q-1)z_c/Zden sum to the integer Q-1. If integral, the two
ceilings sum to Q-1; otherwise their fractional parts sum to1 and the
ceilings sum toQ. Hence residual is0 or1; both final numerators are
positive and sum toQ, with each at mostQ-1. This also covers exact
remainder zero, Q=2, and all zero counts. At C0=C1=0 both branches are
uniform; a single zero count is harmless because alpha>=1.

All SUBs are nonnegative, every DIV divisor positive, and the full
integer products/dividends satisfy

    snapnum<=A(2M+1),
    nearnum<= (6Q+4)D<=8QD<=24mQ<32mQ,
    ceilnum_c=(Q-1)z_c+Zden-1<Q Zden<=12mQ.

The subtractions Q-1 and Zden-1 use literal1, not alpha. These estimates
cover eagerly evaluated candidates even in a discarded uniform branch.
They contain fewer than h+ell+4 bits for snapping and b+ell+6 for output.
Head accumulation and products use fewer than p+h+ell+8 bits. All these
bounds, coefficients used in extraction (<=2^h), public alpha, and
counts are <2^(beta/16): beta/16=8s leaves ample sign/carry space.
The generic primitives below retain full products/remainders before these
bounds justify a beta-bit cast. Output numerators and Q fit b+1 bits,
including Q's endpoint bit. This proves bit-identical D3 output once §5's
acquisition is proved, not merely equal real-valued probabilities.

## 3. Concrete finite primitives and public gate iterator

The Boolean basis is AND, OR, XOR, NAND, NOT, COPY, CONST0, CONST1 and
MUX. Each is one logical assignment with public source/destination indices.
It has at most three input bits. No conversion to NAND is made. A COPY
includes its read and write; a padded word action writes all destination
bits including zeros. The following explicit routines suffice at width
w>=2; use w=beta at runtime. Scratch below excludes retained SSA inputs
and final outputs and is reused between operations.

A ripple adder maintains carry c. At bit i generate, in order,

    t=XOR(x_i,y_i); u=AND(x_i,y_i); v=AND(c,t);
    dst_i=XOR(t,c); next=OR(u,v); c=COPY(next).

This is six assignments per bit. Computing t,u,v before dst_i makes the
routine safe even for in-place dst=x or dst=y. Copy the final carry to
a separate flag before clearing scratch. Do not infer no overflow from
modular arithmetic: a call's static range proof or its wider destination
justifies clearing that flag. A borrow chain uses

    t=XOR(x_i,y_i); nx=NOT(x_i); u=AND(nx,y_i);
    nt=NOT(t); v=AND(nt,borrow); dst_i=XOR(t,borrow);
    next=OR(u,v); borrow=COPY(next).

It has eight assignments per bit and retains its final borrow. Unsigned
comparison uses this borrow and equality uses an OR reduction of XORs.
MIN/MAX use a comparison followed by one MUX per output bit. Word MUX
uses one MUX per bit. Fixed shifts, constants and copies are explicit
bit loops, not machine instructions of uncharged size.

For multiplication use a 2w-bit zero accumulator P and a 2w-bit addend.
For j=0,...,w-1 set addend_i=AND(x_(i-j),y_j) when j<=i<j+w, zero
otherwise, and add it to P with the 2w ripple routine. After j iterations
P equals x times the j low bits of y; P<2^(2w). The final carry is zero
by this bound, and all 2w result bits are retained before a cast. Each
iteration costs at most 2w addend assignments, 12w ripple assignments,
seven flag writes/clears and public control; zeroing addend and flags at
the end leaves the inputs/product alone. A conservative bound on logical assignments, including copied
temporaries and cleanup, is64w^2+64w. Bit-data accesses and address/dispatch
charges are distinguished below; no dynamic counter is silently charged
as a single Boolean gate. This is a full product even when later used by DIV.

For division, keep the entire 2w-bit numerator U, a w-bit positive divisor
v, a 2w-bit quotient and a (w+1)-bit remainder. Initially remainder=0.
Process numerator bits j=2w-1,...,0: shift the remainder left and append
U_j, subtract the zero-extended divisor in w+1 bits retaining borrow,
set take=NOT(borrow), MUX the difference or shifted remainder, and write
take into quotient bit j. If the old remainder is <v, the trial value is
2r+U_j<2v<2^(w+1); the new remainder is again in [0,v). Induction gives
U=quotient*v+remainder at the end. The quotient is 2w bits until a proved
range justifies a cast. This proves zero numerator, v=1 and all exact or
nonzero remainders. Shifting a shortened w-bit trial remainder is forbidden.

A division step needs w+1 shift writes, 8(w+1)+9 subtract/flag operations,
w+1 MUXes, a NOT and a quotient write, plus <=16(w+1) control/copy/clear
steps if expanded without recycling. Over 2w steps plus initialization,
full input/output retention and final zeroing, 256w^2+128w is a safe bound.
No quotient-dependent stopping or data-dependent iterator is required.

The following bounds count logical assignments, including scratch cleanup.
The iterator is a generator; execution uses the explicit wiring library
and pays its fetch/PC/address control in §10.

| operation | logical assignments |
|---|---:|
| CONST/COPY/fixed SHL/SHR |8w+8|
| ADD/SUB retaining carry/borrow |16w+16|
| EQ/unsigned compare |32w+32|
| word MUX/MIN/MAX |64w+64|
| full 2w multiplication |64w^2+64w|
| full-numerator restoring DIV |256w^2+128w|

Each row is <=1024w^2, but we also need a BIT-ACTION bound rather than
merely a gate bound. A direct count of the displayed data iterator gives
14w^2+12w+6 assignments for MUL and20w^2+49w+14 for DIV, before harmless
extra padding clears. A basis assignment needs at most three input-bit
reads, a truth operation and a destination-bit write, hence at most five
bit-data actions. Adding <=32w+32 full scratch/input-copy zero writes and
<=64w+32 ancillary copy/flag actions gives, for the worse DIV case,

    100w^2+341w+134 <= 1024w^2  (w>=2).

The inequality follows at w=2 and the difference is increasing thereafter.
The shorter primitives satisfy it as well; ADD/SUB have <=16w+16 logical
assignments and the other linear routines can be implemented by one
borrow/equality chain plus one bitwise MUX. For actual w=beta>=4736 there
is also more than512beta^2 of slack for the O(beta) scan-bundle controls
used in §§5,7. Full padded instruction and a-bit address accesses are
separately paid by §10's surcharge, not assumed to take one bit action.
Thus g(beta)=1024beta^2 is valid for the stipulated finite bit primitives,
without any NAND expansion. Input snapshots, product and quotient fields, shifted
remainder and difference, two addend/sum buffers and flag cells require
at most 20w+32 scratch bits, within 32w+32; one can allocate the larger
fixed bound and zero unused cells. Even storing separately a 2w numerator,
2w product, 2w quotient, w+1 remainder, w+1 difference, 2w addend,
2w sum, 4w input copies and32 flags totals16w+34<=20w+32.

A primitive iterator is a finite counter automaton, not a subroutine
oracle. Its state is (opcode, phase, outer j, inner i, microstep, base
addresses). ADD has one bit loop with six microsteps; SUB eight; MUL has
outer j, addend i and ripple i phases; DIV has outer j and shift/subtract/
select phases, each one inner i loop. No stack recursion is used. CONST,
COPY, MUX, EQ and compare have one bit loop. For each microstep the above
list fixes its opcode and indices base+i, base+j or base+i-j. At a phase
boundary increment/reset bounded counters and advance the fixed phase
label. This enumerates exactly the gates and writes, including full width
zeros. Depth of arithmetic loop nesting is at most two, with a finite
microstep selector; ≤12 simple counter actions advance one descriptor.
Operand-address formation uses ≤8 additions/comparisons. These generation
actions are charged separately in §11, not multiplied into the logical
word-operation count or silently absorbed into a free iterator.

## 4. Literal two-layer affine renderer, including every alias

Reserve s0=W-2 and s1=W-1 in the fixed W=2048beta channels, disjoint
from all primitive data, controller fields and destinations. The augmented
index W denotes the affine bias convention; it is not an extra resident
activation. Store the redundant constant row/column in (W+1)^2 slots and
pay its evaluation too. The evaluator supplies literal1 as a public MAC
operand, rather than maintaining an uncharged W+1st state cell.

For an instruction z=op(operands), let each row be a list of (column,
coefficient) terms. The stored coefficient at (row,column) is the SUM
of all terms with that column. Thus coincident source indices add; they
are never overwritten by a dictionary assignment.

Layer1 copies every non-scratch data row with the identity term (i,1).
Its scratch row lists are:

| opcode | s0 terms | s1 terms |
|---|---|---|
|AND/OR/XOR/NAND x,y| (x,1),(y,1),(W,-1) | empty |
|MUX c,x,y| (c,1),(x,1),(W,-1) | (y,1),(c,-1) |
|NOT/COPY/CONST0/CONST1| empty | empty |

Apply ReLU. Layer2 sets both scratch rows empty, copies every other row
except z with its identity term, and gives z the following terms:

| opcode | z terms |
|---|---|
|AND| (s0,1) |
|OR| (x,1),(y,1),(s0,-1) |
|XOR| (x,1),(y,1),(s0,-2) |
|NAND| (W,1),(s0,-1) |
|MUX| (s0,1),(s1,1) |
|NOT| (W,1),(x,-1) |
|COPY| (x,1) |
|CONST0| empty |
|CONST1| (W,1) |

In either layer the augmented constant row has (W,1). Every absent entry
is an emitted/evaluated zero. Coefficients after collision aggregation
are in [-2,2]; signed beta-bit encoding suffices.

On Boolean inputs, ReLU(x+y-1)=xy. Hence the second-layer formulas are
xy, x+y-xy, x+y-2xy, 1-xy, 1-x, x or the constant. For MUX the scratch
values are cx and (1-c)y; they cannot both equal1, even when operands
alias each other or the control. Their sum is exactly MUX(c,x,y).
If x=y the first scratch coefficient at that index is2. If y=c in MUX,
the second scratch row cancels to zero. Layer1 preserves all data, so z
may alias ANY operand without destroying a needed source. Layer2 writes
z, preserves all other data, and resets both scratch cells even if their
old values were nonzero. This proves the templates for arbitrary allowed
aliases, not just for distinct SSA variable names.

Each logical Boolean assignment uses two layers. The actual basis of §3
is compiled directly, not first expanded to NAND. Reads/copies/clears are
COPY/CONST assignments or physical evaluator actions already paid below.
A bit circuit of B assignments therefore uses 2B layers and W channels,
with an explicit identity coefficient for every held active coordinate.

For a scalar integer j in [0,2^h], bit extraction is also explicit. At
index i descending from h to0, maintain remainder v<2^(i+1), except
initially v<=2^h. Form in one layer
f=ReLU(v-(2^i-1)), g0=ReLU(v-2^i); in the next layer write bit=f-g0;
in a third write v-2^i*bit, and in a fourth clear the two temporaries.
For integer v the difference is 1 iff v>=2^i; the new remainder is in
[0,2^i). All data needed at a stage are preserved until use. The
coefficient rows have at most three terms, with magnitudes <=2^h.
The endpoint j=A therefore has its high bit retained. Initialize high
padding bits to zero. Nineteen words take 4*19(h+1) extraction layers;
256*19(h+1) in G is more than sufficient even counting reads, copies,
control bits and zero writes. This is not a rounded real comparison.

There are 63 word operations in JOINT. By §3 each consumes <=g actual
bit actions and at most that many logical assignments. Initialization,
logical copies and cleanup of the layout in §7 take <=8192beta actions,
and the three guarded port fields take <=128(b+1). Thus the actual
compiled Boolean/extraction work is at most

    G=64g+256*19(h+1)+8192beta+128(b+1).

The extra word allowance over63 is retained. With the extraction's
four-layer steps and <=64 fixed transition/padding layers, the actual
query depth is at most 16G+96=L. One can pad to L using explicit
identity/zero layers, not implicit zero-cost skipped matrices. All
padding matrices and holds are charged. No per-gate whole-bank clearing
is introduced: each dense layer overwrites its destination bank.

## 5. Actual Z-only acquisition in the two separate implementations

### 5.1 JOINT frontend and finite attention evaluator

The frontend has an explicit scalar-slot map at each token: current
one-hot at0,1; synthetic-query flag2, eligible flag3, public position4,
owned raw input5; the four head outputs in consecutive pairs8..15;
eight first-AND temporaries16..23; eight triple features24..31;
terminal one-hots32..35 and dirty prefix one-hots36..39; nineteen scalar
masters40..58; eight numerator accumulators60..67, denominator68 and
two full-product limbs69,70; public weight/scale/literal fields71..95.
The finite evaluator's Boolean scratch begins at128 and reserves
32beta+32 cells; a following64beta region contains its full a-bit address
records and public literals. This whole map uses fewer than100beta cells,
leaving disjoint copies within the four banks. At query n the retained
scalar region P in B3 is [512beta,512beta+27), far from both this map and
the later <=512beta query layout. The final port uses B3's §6 four-beta
range beginning at186beta+32. Renderer scratch is always W-2,W-1.
These fixed disjoint addresses also specify the emitter's field names.

For triple label abc, the first AND reads10+a and8+b into16+label,
and the second reads that result and current coordinate c into24+label.
Terminal control ab reads14+a and12+b into32+2a+b; prefix control ab
reads10+a and8+b into36+2a+b. All gates therefore have explicit public
indices. The one-hot input complement is ReLU(1-raw-query_flag), so the
synthetic row has both value coordinates zero. Other rows give1-Z_i,Z_i.
The public flags/position fields are loaded from metadata with the paid
input/routing bundles. Scalar masters are copied from P to each word's
base slot in §6; one at a time copy the scalar to a separate extraction
remainder in the64beta transfer range, initialize its other bit slots,
then extract downward. The base slot becomes bit0 only at the final
step, after its scalar value is no longer needed. This avoids an alias
between the original scalar and an early extracted bit.

Read exactly N binary observations into owned full-beta scalar cells,
form (1-Z_i,Z_i), and create at n=N+1 a synthetic zero-valued query.
It is not an extra observation. Four zero-score singleton heads select
keys i-1 (fallback i), i-2 (fallback i), i, i on historical row i.
On query n they select m,m-1,N,N-1 respectively. These masks are nonempty
and causal. Store and examine all 4n^2 mask bits, including zeros. The
heads have value dimension2; all Q/K entries are literal zero, hence
score magnitude0 and QK dimension at most4 (dimension0 would suffice).
The finite zero-score weight is exactly R_s. A singleton's full numerator
A R_s times its bit, divided by R_s, is exactly A times that bit; the
following exact scale cast recovers the bit. No approximation to exp or
softmax is required or used. All full products are within §2.1's guard.

Each historical token then owns current and two lag one-hots. At every
eligible position form each of eight triple features by two ANDs:
first the two lag indicators, then AND with the current-symbol indicator.
All sixteen gates are actual charged affine/ReLU gates, not a triple
table supplied as input. At query n form four pair one-hots from heads
4,3 for S_N and four from heads2,1 for the dirty prefix endpoint.
The identical tokenwise operations on other rows are harmless and paid.

Crop public indices 1,...,m into a prefix view and route actual query n
to its query slot m+1; this is an index map and paid copy within the
existing banks, not a new observation or a fifth data allocation.
Store the entire (m+1)^2 mask. Query m+1 allows keys3,...,m. For other
rows i>=3 allow keys3,...,i, and for i=1,2 allow key i as a nonempty
causal fallback. These unused rows can be evaluated and discarded. The
mask generation and evaluation therefore have well-defined values at
all entries, including zeros and the small m=3 case.

The fifth head has score0, eight triple-feature values and exact weight
R_s. At the actual query its denominator is M R_s>0, numerator for
coordinate sc is A R_s C_sc(Z), and its integer output is exactly

    floor(A R_s C_sc/(M R_s)) = floor(A C_sc/M).

No clean path or Markov assumption enters this deterministic identity.
Append eleven explicit zero words; retain all nineteen scalar words
and all eight dirty controls until their paid extraction/erasure. The
nineteen words are internal registers, not an information restriction
on a competing predictor.

Here is an explicit frontend schedule within the 128 construction layers;
unused layers are padded by stored identity/zero matrices:

| block | layers available | actual construction |
|---|---:|---|
|input one-hots, query zero, public flags/positions|8|constant/copy/NOT rows and paid input writes|
|four singleton projections, finite calls and routing|16|four parallel heads plus fixed value copies|
|eight triple indicators|32|sixteen sequential two-layer AND assignments|
|eight endpoint one-hots|16|eight two-layer AND assignments|
|prefix routing, value projection and fifth finite call|16|fixed index map, eight value copies and one head|
|concatenate/pad19 and controls|16|copies and eleven zero rows|
|prepare retained-query region|16|fixed destinations and initialized padding|
|reset/identity padding|8|explicit identity or zero rows|
|total|128||

Four further phase layers for retained copy, old-state clear, query
handoff and phase reset give the fixed132 frontend allowance. Serial
full-bank sweeps and finite attention arithmetic are charged in E, not
hidden in four layers. Every matrix in the table is tied tokenwise;
nonlocal input binding occurs only through the displayed attention masks
and the charged finite evaluator's fixed index-map transfers. The
coefficient rows are explicit identity/zero/NOT/COPY rows or §4's
three-term gate rows. Thus they have a literal renderer too.

An explicit finite evaluator loops head,row,key,value-coordinate. It
reads every mask bit, including excluded keys, and gates their values to
zero. It initializes denominator and value accumulators, accumulates
full R_s-scaled values, shifts by h and performs the full division and
range-justified cast. Public row/key/coordinate increments/comparisons
are included as word-bundle actions; no data-dependent search occurs.
A singleton entry needs at most16 bundles (mask read, two value reads,
two gated/scaled values, two numerator additions, denominator addition,
index updates, temporary clears). Four full scans use <=64n^2; row
initialization, quotients, scale casts and reset add <=64n. The fifth
head entry needs <=32 bundles (eight reads, eight gated values, eight
additions, mask/denominator and loop/clear work); its row setup/final
normalizations add <=64n. Input reads, public routing and endpoint
handling add <=64n^2. Since n>=7, their sum is <256n^2. Doubling to
512n^2 pays all ancillary input validation, value copies and scans.
A bundle may be an arithmetic operation with control, or a full-width
store with its short-index updates. The sharp data-action bounds below
§3 leave room in g for such O(beta) control work. General instruction
fetch/address costs receive the additional §10 surcharge.

There are five total heads, at most four simultaneous, maximum value
width8, QK<=4 and score magnitude0. All n full token banks remain
charged until the physical sweep in §7, even though only the eventual
query result is needed.

### 5.2 DIRECT paid batch scan

Own the same entire Z in a packed bit array; create its needed copy and
scratch in the 8N allocation. Initialize eight beta-bit counters.
For each j=3,...,m and each of the eight public lexicographic labels
(a0,b0,c0), read the three bits, use their bit/complement to make the
three equality indicators, use two ANDs, and increment that label's
counter by the feature. Read and write each counter explicitly. Use all
eight labels rather than an uncharged source-dependent counter address.
Three equality actions, two ANDs, an ADD, reads/writes, label advance
and temporary reset fit twelve bundles per label; triple reads and
outer controls bring the total below128 per triple. Input ownership,
validation/copy, metadata work and final input clear fit a further64n
bundles. Dirty endpoints and one-hots are computed from the owned Z with
fewer than64 bundles. Execute the actual8+46 operations in §2.

The induction after each eligible triple states that each counter is
exactly its count in the processed prefix; therefore DIRECT obtains
C_sc(Z). Section2.1 proves JOINT snaps to these same integers, so both
programs execute the same output table on the same counts and controls.
This proves per-string guarded-port equality, not just equality in law.

Packed scratch need only the eight counters, eight controls, 54 SSA
results, full primitive workspace, public literals/address records and
output copies. Even reserving 512beta bits for those fields, and
4096beta for duplicate/cleanup buffers, is within8192beta. Together
with 8N owned/input/copy bits and a Z_meta public working copy, this is
W_work=8N+8192beta+Z_meta. Clearing all those bit cells is explicitly
charged; no Python object lifetime is a physical-memory premise.
The action counts just listed, initialization/54 operations, full
port writes and scratch clears are dominated by (512n+2048)g=G:
metadata read/write needs at most16n beta bit actions, packed scratch
clears at most8192beta, and output length is <beta. These quantities
fit the margin beyond128n+118 word bundles since beta>=4736.
DIRECT has E=L=W=dense_slots=P_bits=mask_bits=I_holds=0 and core=G;
its ordinary memory and every access remain paid in the other coordinates.

## 6. Query address width and disjoint live layout

The runtime address-record width a is exactly D5:

    Haddr=G+E+Z_meta+N+L+1,
    a=beta+bitlength(Haddr)+32.

It is NOT a beta-bit word. We prove a<2beta before allocating records.
For JOINT, using h+b+ell+tau<=s and beta=128s,

    G<=2^17 beta^2, L<=2^22 beta^2,
    E<=2^9 n^2+2^15 n beta+2^19 beta+8beta+1024,
    Z_meta=8n beta.

These follow directly from D5, W=2048beta, h+1<=s+1 and beta>=4736.
Adding terms gives Haddr<2^24(n+beta)^2. As n<2^ell, elementary binary
length bounds give

    a<=beta+60+2ell+2ceil(log2 beta)<2beta.

For the last strict inequality, ell<=s=beta/128, and for beta>=4736,
60+2ceil(log2 beta)<beta/16. One proof uses ceil(log2 x)<=log2 x+1:
x/16-62-2log2 x is positive at4736 and has positive derivative thereafter.
Thus the extra terms are <5beta/64. For SMALL, n<=6 and
G=(128n+512)1024beta^2, E=L=0 obey the same Haddr envelope.
For DIRECT at N>=6 do NOT use JOINT's bound on G: here

    G=2^19(n+4)beta^2,
    Haddr<2^22 n beta^2,
    a<=beta+56+ell+2ceil(log2 beta)<2beta.

The displayed looser constants absorb bitlength endpoint rounding.
All comparisons remain valid for arbitrarily large b,N,k. Segmented
index fields fit a; no flat runtime pointer of bitlength(U_stored) is
assumed. Flat generator addresses use a_gen separately in §11.

Use these disjoint logical-cell ranges in each query bank, by cumulative
sums starting at coordinate0:

| length | role |
|---:|---|
|27beta|19 acquired masters and8 observed controls, each padded to a word|
|63beta|distinct JOINT17+46 results, including paid constants|
|32beta+32|full-product, quotient, shifted-remainder and primitive scratch|
|64beta|public literals and sixteen full a-bit address/controller records|
|4beta|three final guarded fields and finite serialization reserve|
|64beta|retained-query transfers, MAC/controller data scratch and copies|

The sum is254beta+32. Sixteen address records use <32beta cells; the
remaining32beta in that range suffice for all fixed literals and bounded
loop state. A conservative doubling of every range plus80 extra flag
cells uses508beta+144<512beta, since beta>=4736. This contains the two
rails/copies if one elects to retain them; the actual unsigned program
needs only one Boolean rail. The two renderer scratch cells W-2,W-1
are outside these ranges. More than1536beta spare cells remain before W.
The scalar-form masters, extraction remainder and its two scalar
scratch cells occupy the transfer region until bit extraction finishes;
they do not require a new bank. MAC signed/full-product scratch and
finite evaluator fields fit the same reserved regions in its own bank.
Public metadata working storage is the separately paid Z_meta and
contains no Z bits, counts, endpoints or source-dependent flags.

At most eight copies/zeroings of the <=512beta live logical fields are
needed for initialization, scalar/bit handoff, final port copy and logical
scratch cleanup. Including both a read and a write costs <=8192beta;
additional complete physical scans are paid in E. The final port needs
3(b+1) initialization writes, reads and writes of its two numerators
and Q, and old-copy clearing, less than128(b+1) actions. This justifies
the nonprimitive terms of G without multiplying E by the number of gates.

## 7. Four physical banks, paid clears and release order

Allocate exactly four rolling banks B0,B1,B2,B3, each nW physical beta-bit
scalar fields before extraction. Owned Z/input one-hots, lag and triple
fields, cropped values, endpoint controls, head accumulators, products,
remainders, scalar masters and all layer copies occupy the named ranges
or spare cells within these banks. Attention scans reuse accumulators
one row at a time while the entire n-token data remains resident.
B3's query region holds finite-evaluator/controller scratch and a
reserved retained-query region P. No stack of previous layers or fifth
external accumulator bank exists.

During query neural computation, B0,B1,B2 cycle as input, first-layer
output and committed output; B3 contains the finite evaluator's bounded
scratch/control and the eventual port region. A dense destination is
written in full, including zero/identity rows. Old copies in the other
banks remain physically charged until overwritten or finally swept.
Only the current neural state's identity rows count as neural identity
holds; old buffer residence is storage in W_work, not a fictitious
unpriced neural layer. Every buffer access is separately charged.

The actual physical trace is as follows; all scans have public bounds.

1. Initialize the four nW banks, including unused fields. Read/copy N
   observations and then execute the paid frontend. No token bank is
   released during the132 frontend phases.
2. Traverse the four banks to copy the nineteen scalar masters and eight
   controls into disjoint P at query n, including explicit zero padding.
   Complete these copies first. Traverse again and overwrite every
   physical field outside P and the public-only scan controller with
   zero: input/tail, endpoint copies, lags, triple values, head sums,
   product/remainder scratch and both old layer buffers are all included.
   Clear the controller's source-bearing temporary after its last use.
3. Only now release nonquery token allocations. Initialize the query
   layout, copy P's fields into its master/transfer region, and overwrite
   old P. Extract all nineteen words into bits as in §4, retaining the
   eight observed controls. No external input pointer is read again.
4. Evaluate the63 selected/output operations with the three-bank cycle.
   After both final numerators are available, initialize a disjoint
   guarded port in B3, copy all3(b+1) final bits there in the declared
   order, including literal Q, and only then clear old output fields.
5. Sweep all four query banks by (bank,channel,physical-bit) order,
   skipping only the designated guarded port and public scan indices.
   Zero all old inputs, masters, controls, arithmetic intermediates,
   old ports, extraction/renderer/MAC/controller data scratch and copies.
   The controller has no observation-dependent address; it clears its
   final data temporary before return. Only public code/indices and the
   final port remain. High physical padding bits are zero too.

The batch initialization and two traversals in steps1-2 require at most
12nW full-scalar bundles. Reserving16nW covers input-routing/handoff
passes as well. A scalar sweep bundle includes a full beta-bit write,
a short increment/compare/reset sequence (at most six O(beta) operations)
and scratch reset; these together are <g. General a-bit instruction and
address manipulation is charged in §10. After release, at most eight
complete four-bank query passes, including layout initialization, old-P
purge and final clearing, plus fixed field transfers, require <64W
bundles, within256W. No such full-bank sweep is inserted per gate.

Initial/master/control/port literal transfers and physical serialization
need fewer than1024(h+b+ell+tau+1) extra bundles: there are19(h+1) bit
extracts, eight controls, three(b+1)-bit output fields and a fixed number
of public loop/literal transfers; fewer than16 bundles per such bit plus
256(h+ell+tau+1) for public initialization/clears suffice. Extraction's
neural work is already in G; this additional payment covers its physical
interface and may deliberately count copies twice.

Together with §5.1 the finite evaluator and all physical sweeps obey

    E=512n^2+16nW+256W+1024(h+b+ell+tau+1).

All source-bearing data are in the four banks throughout. The worst
simultaneous working memory is 4nWbeta+Z_meta. After release it is
smaller; W_work continues to charge that maximum. Dense layer destination
writes are paid in dense MAC work, and full physical sweeps in E*g.
Neither garbage collection nor "unused later" is treated as erasure.

## 8. All fixed D5 resource coordinates

The expressions below are the fixed bounds, not newly enlarged envelopes.
For JOINT at N>=6 use

    W=2048beta,
    G=64g+256*19(h+1)+8192beta+128(b+1),
    L=16G+96,
    E=512n^2+16nW+256W+1024(h+b+ell+tau+1),
    dense_slots=(132+L)(W+1)^2,
    P_bits=dense_slots*beta,
    mask_bits=4n^2+(m+1)^2,
    I_holds=132nW+LW,
    core=256(132n+L)(W+1)^2*beta^2+E*g,
    W_work=4nWbeta+Z_meta.                                (R1)

For DIRECT at N>=6 use

    G=(512n+2048)g, E=L=W=0,
    dense_slots=P_bits=mask_bits=I_holds=0,
    core=G, W_work=8N+8192beta+Z_meta.                     (R2)

For N=3,4,5, BOTH use the packed uniform branch

    G=(128n+512)g, E=L=W=0,
    dense_slots=P_bits=mask_bits=I_holds=0,
    core=G, W_work=8N+8192beta+Z_meta.                     (R3)

All neural coordinates, including heads, values, QK, scores and layers,
are zero in R2 and R3. In R1 there are132 frontend/phase layers, L query
layers, widthW, five total/at most four simultaneous heads, value width8,
QK<=4, score0. All these were constructed in §§4-7.

For each implementation and every N retain EXACTLY

    a=beta+bitlength(G+E+Z_meta+N+L+1)+32,
    K_code=4096*g*(beta+a)+4096*(s+1)*(beta+a)^2,
    U_stored=P_bits+mask_bits+Z_meta+K_code,
    T_online=4096(a+beta)^2*core,
    peak_online=U_stored+W_work,
    a_gen=beta+bitlength(U_stored+T_online+N+L+1)+s+32,
    Emit=U_stored+L+1024,
    T_gen=1024s^2+4096*Emit*a_gen^2,
    W_gen=64a_gen+64*Emit*a_gen,
    peak_gen=U_stored+W_gen.                              (R4)

The output length is3(b+1), GPU work0. These are sufficient upper bounds
for each realization; padding may attain some storage bounds without
making actual work optimal or equating the models. No shared-budget,
Bstar inclusion, statistical or architectural superiority follows.

### 8.1 Dense evaluation, physical scalars and identity holds

Store every coefficient, bias slot and redundant affine row as a signed
beta-bit field. Store all zeros and identities, including padding layers.
The132 frontend matrices act at all n tokens; the L query matrices at
one token after actual release. This gives dense_slots and P_bits, and
at most132nW+LW active identity-channel holds. Attention masks have
exactly the declared full rectangular sizes and include their zeros.
One may evaluate every crop row in the finite evaluator, so zero mask
entries are also actually read. No sparse matrix discount is taken.

A full signed MAC is implemented by magnitude extraction/sign handling,
the shift-add product, full signed accumulation and a proved-safe cast.
For general beta-bit operands the elementary multiplication assignment
count is14beta^2+12beta+6; even counting <=5 bit reads/writes/truth actions
per assignment, sign conversion, full2beta accumulation, initialization,
fetches and scratch zeroing, <=256beta^2 elementary bit actions suffice
for beta>=4736. All product bits are retained. Actual partial sums in
our matrices have at most three nonzero terms (or one identity), with
bounded scalar/literal magnitudes from §2.1. Even the crude bound
4*2^(2s+4) is far below the signed beta-bit range; zero entries introduce
no growth. Scalar extraction coefficients <=2^h and the public positions
and R_s also obey this bound. Thus accumulation never relies on modular
overflow. Evaluating the entire (W+1)^2 matrix, even zero coefficients,
costs <=256(W+1)^2 beta^2. Multiply by132n+L and add E*g for the separate
finite evaluator/physical sweeps to obtain core in R1. The general
instruction/address surcharge in §10 is additional, so basic operand
fetches may be counted twice, conservatively.

The finite evaluator's bit scratch is located in B3's declared cells.
If a scratch bit is represented as a neural Boolean scalar we pay beta
physical bits for it too. A constant row is an affine evaluation
convention, not a fifth bank or a free resident scalar. Four banks plus
public metadata give the simultaneous W_work bound in R1 even during
copies. U_stored remains resident concurrently, yielding peak_online.
For DIRECT/SMALL the analogous argument uses packed bits as in R2/R3;
no neural scalar width is silently substituted there.

## 9. Stored executable code, metadata and exact acquisition of operands

Use segmented addresses (bank,token,channel,bit) for data and
(layer,row,column,coefficient-bit) for dense parameters; masks use
(head,row,key), libraries (primitive,record,field-bit). A full field
is represented in a bits and retained as such. All segment bounds fit a:
W=2048beta, layer<=132+L, token<=n, bit<=2beta, and library record<=g;
the code size has logarithm bounded by a few times log2(beta+a), which
is also below a since beta>=4736 and a<2beta. Mask row/key segments fit
ell+1. Flat runtime addressing of all coefficient bits is unnecessary.
Multiplications used for segment offsets are explicit finite arithmetic;
repeated linear scans can instead increment the last segment and carry.
The word fields for such counters and the full a-bit records are in §6.

An explicit primitive library uses at most24 types: the Boolean basis,
word constant/copy/shifts/add/sub/compare/equality/select/min/max/full
multiply/divide, bit read/write and a combined scan-next/reset routine
share their displayed circuits. Counting overlapping types only once
keeps the number <=24. A type's finite wiring list has <=g records,
each <=64(beta+a) bits: opcode, up to three source tuples, destination
tuple, literal/shift fields, next-record/phase information and padding.
This is explicit bit-circuit wiring, not a stored instruction that grants
unit-cost multiplication. The total is <=1536g(beta+a), below the first
4096g(beta+a) part of K_code. Shared macro templates are instantiated by
public bases; their index arithmetic is paid, not precomputed data.

Fewer than512 other descriptors suffice: 63 table entries, at most32
head/input/crop descriptors, sixteen mask/position cases, at most64
literal/parameter/format records, at most64 scan/phase/port records and
padding. Each occupies <=64(beta+a) bits. Their total32768(beta+a) is
below4096(s+1)(beta+a)^2 since (s+1)(beta+a)>=8. This covers either the
smaller DIRECT table or the SMALL program too. The unused remainder
of K_code is actually generated and stored as zeros. Dense query gates
are already stored as dense matrices; their full unrolled instruction
list is not redundantly claimed to fit a constant-sized SSA table.
The finite evaluator uses the shared primitive library; query matrices
are emitted by iterating the SSA and primitive descriptions.

Public metadata is explicitly encoded as at most64 records per token,
each at most8s bits, and a duplicate. Fields describe the position,
validity/synthetic-query flag, four key-selector cases, crop index map,
eight feature labels, eight endpoint labels, nineteen master labels,
head shapes, public N,k,b,h,p and literal powers of two, and format/loop
bounds. Public scalar literals A,R_s,Q have lengths <=s. Segmented
runtime a-bit addresses belong to K_code and the controller range,
not to a falsely truncated metadata field. No large flat address or
source statistic is stored in an8s metadata record. The total is
2*64*8ns=Z_meta. A separate full working copy of this public metadata
is charged in W_work. Unused positions and padding are generated zeros.
All observations, counts, dirty controls and masks applied to data live
in the charged data banks, never disguised as public metadata.

## 10. Complete online address/dispatch surcharge and small branch

A basic logical bit assignment accesses at most three inputs and one
output. Expand an actual execution into bit reads, truth operations,
writes and public control. For a word operation the gate counts in §3
leave enough slack for all bit-data accesses within g, as proved in §3.
For each such action or dense MAC bundle, instruction/operand/coefficient
fetch and dispatch read fewer than128(a+beta) padded bits and perform at
most32 public increment, comparison, reset, sign-extension or offset
operations. The fixed tuple formats in §9 witness this: at most four
operand tuples, one instruction record of length64(a+beta), an opcode/
phase record and a carry chain through at most eight segment counters.
No source-dependent pointer or unbounded search occurs. Field reads and
writes are literal bit loops. A padded instruction record is streamed one
field at a time into the sixteen declared address records and literal
slots; its entire64(a+beta)-bit stored record is never an extra live buffer.
Address arithmetic acts on a-bit fields:
the sharp elementary routines of §3 cost less than128a^2 per full
schoolbook operation for a>=4736. Since a<2beta, a+beta>3a/2, so this is
less than64(a+beta)^2. Simpler increment/copy/compare operations cost
less. Source-data arithmetic was already counted in core and is not
reperformed as an address operation. Thus32 such operations plus the
128(a+beta) fetched bits are below4096(a+beta)^2 per core action.
Therefore

    actual online time <=4096(a+beta)^2 * core.

This deliberately large multiplier pays full padded field reads, all
instruction/operand/coefficient addresses and dispatch. It is not a
claim that an a-bit record is one beta-bit register or that a word access
is a unit hardware instruction. The array model permits a labelled bit
read/write; its entire address manipulation and each accessed bit are
charged. Mask/parameter/metadata bits read by the evaluator have the
same surcharge. Keeping all stored arrays and working banks concurrently
proves the exact peak_online formula, not merely separate maxima that
could fail at a copy boundary.

The early N=3,4,5 branch is taken before any prefix parameter or head
builder. It owns exactly N input bits and pays their reads/validation,
initializes a fresh three-field port, writes Q/2,Q/2,Q least significant
bit first, then zeros owned input and every scratch/old port copy.
Public Q=2 is ordinary here. Output length3(b+1)<beta; packed temporary
and copy storage fits8192beta, owned inputs/copies8N, public working
metadata Z_meta. Input and metadata read/clear uses <64n g, port and
fixed scratch processing <256g, both below(128n+512)g. All neural
coordinates are zero, as in R3. No fictitious sixth input, m/M, frontend
or max(N,6) statistical padding is executed. R4 supplies its separate
stored code, dispatch, online work and peaks with the SMALL parameters.

## 11. Full finite generator and its per-unit work

Here is a generator for the complete realization, including all zero
storage. Its counters and transitions are part of the construction.
There is no oracle giving an arbitrary matrix coefficient or a "next
gate" for free. The generator sees only N,k,Q (or b from its dyadic
representation). Its output sections, in order, are HEADER, LIBRARY,
DESCRIPTORS, METADATA, MASKS, FRONTEND MATRICES, QUERY MATRICES, and
padding/delimiters. DIRECT/SMALL skip the empty neural sections. The
resulting program/arrays have exactly their allocated lengths in R4.

### 11.1 Initialization and finite state

First test N. In SMALL, do not calculate any prefix parameter. In the
large branch derive m,M,ell,tau,h,p,s,beta and the literal powers by
bitlength scans, shifts and additions. The number of input/literal bits
is <=16s, and fewer than128 such linear scans/additions suffice;
1024s^2 bounds this initialization for s>=37. Computing large cap
expressions (G,E,L,K_code,U_stored,T_online and a_gen) is NOT charged
as an O(1) part of this initialization: use a fixed expression tree of
fewer than128 additions/multiplications/bitlength operations. Charge
one node to each of128 explicit header units, from the +1024 allowance
in Emit. Each unit emits its public header delimiter; if retained in the
runtime image, its format bits occupy the already reserved K_code padding. Schoolbook operations on at most a_gen-bit magnitudes cost
<1024a_gen^2 per node, including addresses and carries, below the
4096a_gen^2 per-unit allowance. All intermediate positive quantities
can be ordered so that their magnitudes are bounded by the final
U_stored+T_online+N+L+1 or its displayed parameter components; the
added beta+s+32 in a_gen covers full public literals and indices.
In particular addresses of emitted bits never exceed U_stored and
layer indices never exceed132+L. Resource upper bounds such as T_gen
are certificate formulas; their binary value need not be used as an
online loop counter. No circular unit-cost computation of a_gen is used:
ordinary variable-length binary registers grow to at most that proved
bound during these fixed expression evaluations.

The generator is a finite counter automaton with these levels:

1. output section and public template state;
2. primitive type or SSA position (at most24 or63 respectively);
3. primitive phase and its outer and inner bit indices from §3;
4. layer phase (0/1 for a Boolean gate, 0..3 for scalar extraction);
5. row and column of the complete (W+1)-square matrix;
6. coefficient encoding bit.

The library/wire section instead uses record/field/bit counters. Masks
use head,row,key; metadata uses token,record,field,bit; the port uses
field,bit. All are bounded integer loops. The primitive has at most two
nested loops and finite microstep state. The total nested counter stack
has at most twelve a_gen-bit fields at any moment; up to sixteen more
hold parameters, sparse row terms and accumulated offsets. No recursive
call stack or search through previous matrices is required.

### 11.2 Descriptor transitions and literal coefficient emission

For each primitive descriptor the iterator executes the displayed
ADD/SUB/MUL/DIV microstep lists. Base+i, base+j, base+i-j determine
all register endpoints. At a completed inner loop, reset its index,
advance the finite phase or outer index; at a word boundary move to the
next of the explicitly printed63 SSA states. The generator's finite
control has one state per printed instruction, so it does not search
through a variable-length history to discover the next opcode. At most
six counters can reach a boundary together; at most twelve reset/
increment comparisons and eight endpoint additions plus fixed phase
updates suffice to produce the next gate. Even allowing opcode decoding
and zero/copy phases, <=48 elementary counter actions suffice. Charge
this transition to the next layer delimiter, not to an absent "free"
step. The L delimiter allowance covers query layers, with frontend's
132 and the128 header units fitting in the additional1024 units.

For a Boolean layer, form the row-term list by §4. At most three terms
are present, including the bias. Iterate every row, every column and
every beta encoding bit. Test equality of each term's column to the
current column, add ALL matching coefficients, and emit the signed
encoding bit. Coefficient collisions therefore produce2 or cancellation,
never a lost operand. Even zero coefficients are encoded beta bits and
all identity rows are visited. The coefficient is in [-2,2], so its
signed bit is selected by comparisons with the bit index; no large
integer exponentiation or numerical oracle is needed.

Frontend layers use the same finite gate rows, plus fixed disjoint
COPY/NOT/CONST/projection row ranges. Row membership takes at most
sixteen endpoint comparisons (eight ranges). Extraction uses at most
three nonidentity rows with coefficients1,-1,-2^i and biases
-(2^i-1),-2^i. Their signed encoding bits are explicit comparisons
against i and the sign bit; no lookup into an exponentially long table.
Phase matrices are fixed identity/zero/copy lists. Thus at most three
column tests, three small coefficient additions, eight bit-selection
operations and six row/column/bit counter updates, in addition to the
sixteen range/opcode tests, suffice per emitted coefficient bit: fewer
than48 actions. A frontend multiple-copy row is selected from disjoint
ranges; there is never a sum over all W potential nonzero sources.
This bound describes how the coefficient is COMPUTED. It does not omit
the cost of EMITTING every one of the (W+1)^2 beta coefficient bits.

Library wiring records are produced by the same primitive iterator;
fields are fixed opcode, endpoints and literals. The iterator advances
once per record and record bits are then streamed. Descriptor advances
cost <=48 actions and can be attached to that record's first emitted
bit (all records have positive length). A record bit needs <=12 further
counter/copy actions, so <=60 actions at that first bit. Padding records
are explicit zero loops with the same counters. No gate expansion is
repeated by seeking from the start of an earlier primitive.

For masks, each emitted bit is the Boolean formula in §5: row=query
versus historical, key equal to one of the four selected indices, or
3<=key<=row in the cropped head (with fallback for rows1,2). At most
sixteen compare/add/Boolean actions plus eight counter actions compute
it. Metadata uses the explicit record formats in §9, with current
position/label constants copied bitwise; <=40 actions per bit suffice.
Parameter/header or padding bits and guarded-port descriptors use
shorter versions of the same loops. The generator emits final-port
wiring/format, not observed output data. Every unused code, metadata,
mask, coefficient and padding bit is emitted as well.

### 11.3 Work, storage and simultaneous generation peak

For clarity, an elementary counter action above is an increment,
addition/subtraction, comparison, reset or bounded field copy/bit select
on at most a_gen bits (a constant number of concatenated fields can be
streamed). Ripple carry, subtraction/borrow, lexicographic comparison
and explicit bit writes implement each in <=32a_gen^2 bit steps,
including reading its finite-control instruction. For an explicit
address-free implementation of a generator counter action, keep its fixed
number of registers as binary tracks, scan from low to high for carry,
from high to low for comparison, and sweep to copy/select a requested bit.
Even a bounded-register selection followed by a full bit-index scan uses
<32a_gen^2 track reads/writes/moves. In the header, shift/add multiplication
or restoring division uses at most a_gen outer passes, each with a
constant number of length2a_gen track sweeps, within1024a_gen^2. Thus the
generator bound includes access to its counters rather than recursively
assuming a unit-cost large-word address operation. General
per-bit units require at most64 counter actions, hence <=2048a_gen^2;
the common4096a_gen^2 allows the remaining finite-state dispatch,
byte/bit encoding and delimiter writes. Transitions not immediately
emitting a bit are attached to the actual positive-length record or
layer delimiter just specified; there is no uncharged long seek.

Exactly U_stored stored bits are emitted. At most L query delimiters,
132 frontend/phase delimiters,128 cap/header units and a fixed number
(<256) of section switches suffice. They are below L+1024. Thus the
number of charged units is at most Emit=U_stored+L+1024, and total work
is at most1024s^2+4096 Emit a_gen^2=T_gen. This is an explicit terminating
algorithm for each finite public tuple, not an instruction to allocate
an enormous netlist during this proof run.

The counter automaton, the128-node public expression evaluation (whose
values may conservatively all be retained) and the full arithmetic scratch
need fewer than256 a_gen-bit working words. Since Emit>=3, these already
fit64a_gen+64 Emit a_gen. The still more conservative allocation of64
initial words plus64 words per emitted unit is exactly the prescribed
W_gen=64a_gen+64 Emit a_gen. Retain every already
emitted bit of the stored program simultaneously, and the peak is at
most U_stored+W_gen=peak_gen. The generator's flat file address fits
bitlength(U_stored+T_online+N+L+1)<a_gen, unlike runtime's segmented a.
Its program is a fixed finite counter machine with the printed finite
state lists; no observation, u,t or channel seed enters its constants.
This proves both online and offline simultaneous peaks in the SAME
fixed D5 formulas, without granting an O(1) coefficient oracle.

## 12. Scope, new splice checks and completion

Sections1-2 prove exact closed-domain semantics; §§3-4 prove the finite
primitives and literal renderer; §5 constructs both actual acquisitions;
§§6-7 allocate and clear all physical state; §§8-11 prove every separate
D5 coordinate and a finite complete emitter. Therefore each individual Z
produces exactly the same D3 guarded port in DIRECT and JOINT. C1 applies
to this function once combined by Lead; no statistical premise was needed
for this construction. C2 is not a finite-program predecessor.

The new standalone c3_affine_iterator_v1.py checks only the new splice:
117 varied full-product/full-numerator primitive cases,278 successive
complete dense two-layer transitions from actual in-place multiplication
and restoring-division iterators, and784 emitted coefficient bits
including colliding operand/destination indices. Its checks include
nonzero initial scratch, full dense zero/identity entries, signed encoding
and final primitive/renderer scratch clearing. These finite checks are
transcription evidence only, not a proof of all-N costs or an admission.
The seed's earlier8832 alias cases and12 examples, and all old diagnostic
suites, were not rerun. The analytic arguments above cover the entire
parameter domain and are the submitted proof.

The source seed and method/preparation reviews have no Fact status in
this proof. Source versions and the new artifacts are hashed separately.
No old Bstar, shared-cap claim, mathematical oracle, free scalar bit,
Python integer time or garbage collection is used. Only a normal gateway
verdict on this exact C3 obligation can admit this result. Root combination,
fixed independent review and final_audit remain outside this submission.

## Appendix P. Fixed provenance and artifact boundary

- `PROBLEM.md`; SHA256 `960299dbb9730b6f8b7d9de81128fabcca03b7342a456beb57572e52d490caca`; current contract, D1-D7.
- `inputs/c3-affine-emitter/AFFINE_EMITTER_SEED.md`; SHA256 `7ea9c78e8a0c6586d1d2a5d46ae5fd937c10e4b02d6dcbad86548b358b1d08a0`; new constructive seed, source only.
- `inputs/c3-affine-emitter/method-review.json`; SHA256 `eb7188b397e463b90d6cafba53e722230ce20bb68eb482a3c58446739a6c6c87`; independent method discussion, no Fact.
- `outputs/001-input-contamination/verifier/preparation-review-v1.md`; SHA256 `d31f00c7748d05ca7974f7ef3cbff18424f954a07a0ec315d5830bbbc760d8b0`; interface discussion, no Fact.
- `inputs/source-stage4/outputs/001-relative-code/prover/c3c4-integrated-v1.md`; SHA256 `2fc89f6bca30288d766fcdb71b26875943f2d6efb5fc9a181b401dba1f7e243a`; historical primitive/frontend/table lineage only.
- `inputs/source-stage4/outputs/012-input-contamination/prover/finite-program-v1.json`; SHA256 `3875340ee76fa75ad61cc9db5e4483bb03e1971eeaa9b5d8973545bb2a83ec44`; historical exact operation transcription.
- `inputs/source-stage4/outputs/012-input-contamination/prover/upper-program-certificate-v1.md`; SHA256 `b1a0de75230bb5ec2cd58417e09f2c0bb3ca7818e2fd513c6e0333f81b7beab4`; historical D5/program source only.


---

# C4 and root combination

Source: `outputs/001-input-contamination/lead/fixed-combination-v1.md`; SHA256 `023534f2978bee9d8132100c1cdd4a85c9208d1afa1a99924dd510617915a553`. Source text follows unchanged.

# Stage5 fixed combination: C1–C4 in one observation experiment

Lead, 2026-10-26. Root: `881d17365a7019add4410343d568625dacae67d26aa17548bda2de7f9b860dbb`.
Contract: `873515c4586d37a2bde324010bea6ae30f820927b7c25ded15b784a79eef7e45`.
Definitions: the unchanged D1–D7 in `inputs/STAGE_DEFINITIONS.md`, SHA256
`fc104078b9455bdd86586decd50902df6688400cc00f06e6b105699efefd0e02`.

Historical status: the three components had been accepted, while this combined text remained a candidate for independent review rather than a newly accepted theorem. Later status must be read from dated scientific evidence records; component passes do not establish acceptance of the combination.

## 1. Current-project premises and their actual evidence

| Component | Current Fact | Current Evidence | Native status and predecessors |
|---|---|---|---|
| C1 | `f9e055bd405c4b56` | `61f169db99848f6794e334ea287037fae00a592f4b5e5254d580c0b9f74a599f` | DISCHARGED / VALID / LLM_CHECKED_PROOF / PASS; [] |
| C2 | `df40a215d931bd32` | `3448f22a5b9e86526c831f0518a83b828eaf69eb2acf455fb0057f354dae7cd3` | DISCHARGED / VALID / LLM_CHECKED_PROOF / PASS; [] |
| C3 | `39367951834d7aa7` | `426929d6b208d95764b59cd20f658f51c91334448c86cfb5cdb9b8bf2d5e4b00` | DISCHARGED / VALID / LLM_CHECKED_PROOF / PASS; [] |

Canonical Fact hashes, respectively:

- `19a572c3d885cba4205e2744f5605005218618ede8ed0deca347b586f2b693cd`;
- `7d7b0a5414b61fbf2117c9b980d4e7580b0ea9311de07c9dc4a3faa1ef54aaa8`;
- `421bf5095b3abe9d5ace680cecab8080cf03de703946c3017b614aa97adedacc`.

The corresponding complete authored proofs are
`../prover/c1-proof-v1.md`,
`../counter/c2-proof-v1.md`, and
`../prover/c3-proof-v1.md`.
Their respective SHA256 digests are
`c80a71242b438eda82b4b1717838a15da30232db18c4b97096f29f45c5101fc3`,
`f10c16cca4efde271b33c3fa2de62244098912c110991b30ccd4e40489852e99`,
`5ac089baa1a28d2f89db223e16542ba43ac153c6930e81806c6627d0e0e22827`.

Lead read the complete relevant proofs and checked all six authored/canonical hashes, actual embedding of each authored proof in its canonical Fact, and the empty predecessor headers. The C3 manifest's thirteen source/artifact digests were checked too. `all-components-native-readback-v1.json` fixes the actual native records at frontier
`47764359856c626063a362ea0f080309b80ec551ea175c80134fbb6996945041`.

Thus the mathematical predecessor list for the proposed root proof is exactly these THREE current-project Facts. There is no old-project Fact, historical FILE SCOPED PASS, preparation discussion, method review or local diagnostic in that list. C1 proves the necessary clean/source premises directly; C2 proves the source reversal and residual construction directly; C3 proves the finite primitives/frontend/compiler/generator directly. In particular, C3 needs neither the statistical C1 nor C2 as a predecessor.

## 2. The precise family and shared experiment

Use the exact D3 family A, with alpha=3k+1 and the specified smoothing, clipping, ties, grid corrections and output port. For N>=6 its triple counts are those of the OBSERVED Z prefix at positions3..m. The query is the actual last pair, preserved by every allowed channel. The prefix endpoint, if computed, is the dirty pair (Z_(m-1),Z_m). For N=3,4,5 the genuine branch reads exactly N bits and emits uniform; it never forms a prefix or an artificial sixth input.

C3 constructs two deterministic algorithms A^J and A^D. For every binary z and every allowed public tuple, the entire three-field port of each is equal to that of A:

    port_J(z,N,k,Q) = port_D(z,N,k,Q) = port_A(z,N,k,Q).

The port contains (out0,out1,Q), each b+1 bits, least-significant bit first. Both numerators are strictly positive and sum to Q. Equality of ports entails equality of the two probability vectors. All three maps use only Z,N,k,Q; none uses the clean counts, unknown parameters, private channel coins or future Y. Clean counts in C1 are proof variables only.

Fix any legal D1 source and any globally legal D2 batch channel T. On the underlying source/channel probability space, substitute Z=T(X_1^N,omega) into this pointwise identity. It holds for every history and every seed, hence the KL losses against p_(u,t)(.|S_N) agree sample by sample. Therefore both average risks, and the conditional risks given S_N=00, are exactly equal for A^J,A^D,A. The conditioning event has probability u>0. This is a deterministic transfer, requiring no Markov property of Z and no independence between the terminal query and the prefix.

By current C1, uniformly for this single unknown-parameter family and for every such source/channel,

    R_av(A^J,T;u,t) = R_av(A^D,T;u,t)
                   <= 16000000/(3N) + 135680*k/N + 3/Q.       (U)

The exceptional domain cases k=0, Q=2, Q=4, ties, zero counts, independent closed count inputs and N=3,4,5 are covered by C1/C3, not discarded in this transfer.

## 3. One channel, then the predictor, then one witness for both risks

Fix legal N,k>=1. C2 constructs a single T_(N,k), depending only on these public integers and the two fixed public witness distributions. Its row is indexed by its input history, never by the actual hidden source label. Its rule is independent of Q and of the predictor. Every row and every finite private seed preserve the last pair and edit at most k earlier bits; it is globally legal for all D1 sources. The construction's unrestricted external computational cost is outside predictor cost by D2.

Let u0=k/N, Delta=1/640000 and t_+/-=1/2+/-Delta/2. The full observed-law conclusion is

    TV(L_(u0,t_+)(Z | S_N=00), L_(u0,t_-)(Z | S_N=00)) <= 1/64.  (TV)

Private channel coins are averaged in these laws. The support constraint is pointwise in those coins. Neither small TV for each fixed seed nor small unconditional-history TV is asserted.

Now fix Q and any common possibly randomized full-Z predictor B, with unrestricted probability outputs and unlimited subsequent computation. C2 applies to the SAME channel just fixed, including when B knows the public two-point experiment and the channel but not the private seed. There is ONE t_* in {t_-,t_+} satisfying simultaneously

    R_00(B,T_(N,k);u0,t_*) >= c,
    R_av(B,T_(N,k);u0,t_*) >= c*k/N,
    c=Delta^2/8=1/3276800000000.                              (L)

Predictor randomization is fresh and independent, as in D1–D2. Infinite KL is allowed for this lower comparison class. The same-witness implication follows by first selecting the conditional-risk witness by testing, then using stationarity P_(u0,t_*)(S_N=00)=u0 and nonnegativity of the remaining conditional KL terms. A second witness selection is unnecessary.

Apply this conclusion to the deterministic D3 map A at the fixed Q. Since A^J and A^D are that same map on every z, the very same selected t_* works simultaneously for both concrete implementations. The source is legal: k<=M/1024 and M<N/2 give 0<u0<1/2048<1/4, while t_* lies in [1/4,3/4]. T_(N,k) is among the channels quantified in (U). Hence, in this one actual-terminal experiment, for either implementation I in {J,D},

    R_00(A^I,T_(N,k);u0,t_*) >= c,
    c*k/N <= R_av(A^I,T_(N,k);u0,t_*)
           <= 16000000/(3N) + 135680*k/N + 3/Q.                (C4)

The SAME T works for every Q and every B in (L); t_* may depend on B and Q. The simultaneous J/D witness in (C4) is justified by pointwise equality, not by claiming one universal witness for all predictors. No positive-k lower is asserted in the N=3,4,5 or k=0 branch.

## 4. Load-bearing interfaces: where each is now established

These entries locate the actual self-contained derivations, rather than replace them with assumed interfaces. The full proofs and exact definitions are reproduced in `fixed-full-proof-v1.md`.

| Required interface | Current proof and connection |
|---|---|
| True stationary law, reversal and common atom | C1 establishes the stationary source, reverse kernel/common atom, clean whole-prefix terminal bridge and visits. C2 proves the reversal and atom again for its complete history construction. No old source Fact is assumed. |
| Clean comparator and rare row10 success | C1 proves the <=1000000/N clean comparator using deterministic-horizon martingale control, fixed row-stack events, spaced visit tails, rare row10 successor treatment and actual-terminal weighting. |
| Dirty smoothing and clipping | C1 separately bounds each count and row-total change by 3k. With alpha=3k+1, the dirty numerators dominate clean count+1 and the dirty denominator is at most D_s(clean)+9k+2. A common coordinate factor (D_s(clean)+2)/(D_s(clean)+9k+2) survives clipping in both output coordinates. |
| Reciprocal visits, whole-prefix bridge, positive grid | C1 integrates reciprocal row visits under the TRUE source and whole-prefix terminal bridge, then applies the exact positive grid. This yields (U), with literal1 retained in Q-1 and Zden-1. It never analyzes Z as Markov. |
| Entire reverse history | C2 retains intermediate pairs, adaptive commitment marginals, truncated last block, the 97-episode charge and the map of every free symbol to the original history; this gives the full-history Hamming transport estimate. |
| One globally lawful row kernel | C2 removes cycles and collapses paths in the UNNORMALIZED Jordan residual flow, cancels common mass using the SAME row kernel, proves the bad-fraction identity, and converts the rational construction into a finite private seed with per-input/per-seed hard budget. Expected transport alone is not its legality argument. |
| Same-witness testing | C2 proves (TV), then conditional testing and actual-terminal stationarity give both inequalities in (L) at one t_*. |
| Exact finite semantics | C3 §§1–5 prints the actual JOINT17 / DIRECT8 and common46 operations, closed independent count/word guards, full products, shifted remainders, safe casts, literal affine gate rows and causal paid acquisition. |
| Complete costs and no bypass | C3 §§6–11 provides physical layouts, scan/copy/erase schedules, stored code/metadata/mask/dense zeros, dispatch/address charges, full finite emitters and both simultaneous online/offline peaks. Section5 uses dirty endpoints only; section7 clears source-bearing state before release and after output. |

No unresolved clean/finite interface is being hidden in this combination as “admitted from the source.” The three actual admissions bear these claims at the required LLM_CHECKED_PROOF level.

## 5. Exact implementation and resource scope

The implementation assertion is constructive and separately priced. DIRECT is an owned-batch packed bit-register machine. JOINT is the principal extracted-query dense tokenwise batch hybrid plus its paid finite evaluator. They have the same port map and different resource models. No assertion identifies the models or fits either into a historical Bstar.

C3's affine renderer specifies coefficient computation, including repeated-index sums and every zero coefficient, rather than treating “next coefficient” as an oracle. Its primitive iterator retains full 2beta-bit products and full-numerator restoring division with beta+1-bit shifted remainder. Signed dense coefficients are interpreted exactly. Boolean neural cells still consume full beta-bit physical scalars. A large Q enlarges beta and the charged frontend as prescribed by D5.

The following map is to the EXACT formulas in D5 (reproduced in the full proof); it introduces no replacement envelope.

| D5 coordinates | Constructive justification in C3 |
|---|---|
| DIRECT G,core and zero neural coordinates | §5.3 paid full-Z ownership/read, eight-label triple scan, dirty controls, eight selections plus46 outputs; §§7–8 cleanup and packed work. |
| JOINT W,G,L, heads/value/QK/score | §§3–6 explicit finite compiler, scalar extraction,128 frontend layers plus4 phases,63 selected-query operations; five total heads/at most four simultaneous/value8/QK<=4/score0. |
| JOINT E | §§5,7 finite full-batch evaluation, endpoint acquisition, copies and explicit full-bank scans before release. These are word-step bundles expanded by g, separate from dense work/depth. |
| dense_slots,P_bits,mask_bits,I_holds | §§4–5,8 evaluate/store all tied dense entries and masks, including zeros and identities. Holds are 132nW+LW. |
| W_work and physical bank peaks | §§6–8 four nW beta-bit physical banks plus metadata in the batch phase; packed DIRECT/SMALL bounds; transfers, duplications, controller fields, SSA, scratch and output all fit declared slots. |
| a,K_code,Z_meta,U_stored | §§6,9 finite segmented address records, full wiring/code descriptors and all padded public metadata; no dirty state disguised as public metadata. |
| core,T_online,peak_online | §§8–10 charge dense exact MACs, E*g, all bit reads/writes, padded instruction/coefficient fetch and address dispatch; stored and working allocations coexist. |
| a_gen,Emit,T_gen,W_gen,peak_gen | §11 gives finite expression evaluation and bounded-counter emission of all wiring, descriptors, masks, matrix entries, code/metadata padding and port wiring. Every transition is charged to an emitted bit or actual delimiter, including initialization and full simultaneous stored output. |
| N=3,4,5 and final output/GPU | §10 executes the actual N-bit uniform packed branch with no prefix; §7 writes all3(b+1) output bits then erases remaining source-bearing state. GPU work0. |

All formulas retain D5's g=1024beta^2, 32beta+32 bit scratch interface, W=2048beta where applicable, and separate runtime a and generator a_gen. The proof does not grant unit-cost Python integers, free source features, uncharged mask generation, free copies/holds, garbage collection or early release of data banks.

The companion program `../prover/c3_affine_iterator_v1.py` and its fixed results record 117 primitive cases,278 dense gate transitions and784 coefficient bits for the NEW splice. Those checks are finite transcription checks, not universal proofs or additional Facts. No old unchanged diagnostic suite was rerun. The universal mathematical construction and accounting are in the admitted C3 proof.

## 6. Strong baseline, rates, primary comparison and exclusions

The upper has the form O(1/N+k/N+1/Q); the full-Z lower is Omega(k/N). The precise claim about pollution is the O(k/N) upper contribution together with the Omega(k/N) full-observation lower demonstrated above. We do not derive matching 1/N or1/Q lower terms, a full Theta(1/N+k/N+1/Q) result, or a lower bound on the attacked-minus-clean risk difference for each predictor.

The lower comparison class includes direct counting, any statistic or encoding of the entire Z and unrestricted later computation. DIRECT remains a concrete strong baseline realizing the very same D3 probabilities. Equality of ports entails equality of risk; the separate D5 sufficient vectors establish no JOINT statistical or same-budget computational advantage, practical constants, resource optimality or old-Bstar inclusion.

The fixed primary mapping is `../counter/d6-scope-map-v1.md`, SHA256
`e4ae322376acca4e3a88e3c591700f5a074388d91637140d48b7a223122ba03f`.
Its pinned local primary PDFs and page/theorem locations support only the bounded D6 comparison:

- Chen/Gao/Ren arXiv1511.04144v2 studies iid Huber-mixture robust testing/modulus. The corrected PDF SHA256 is `538cda7c3ea92a31a394e85b2928a6309cd751b9f4afc5e1732b2bf2a4b8f645`, as fixed in SOURCE_CORRECTIONS; historical originals remain unchanged.
- Pydi/Jog ICML2020/PMLR119 main and supplement include class-dependent point maps, Wasserstein distribution attacks, transport-tail costs and submeasures. These are prior tools. A whole dependent trajectory can be one feature; dependence alone gives no novelty claim.
- The required specific steps here are the actual D1 terminal-conditioned full-path Hamming estimate and a single common input-row hard-budget kernel. C2 proves these; two label-aware maps or an average transport budget would not substitute.

There is no claim of publication novelty, every-source bad risk, full conditional classification, deterministic-channel attainment, small unconditional-history TV, small TV for every fixed seed, a time-causal sensor, an all-layer/IEEE fault theorem, training outcomes or empirical efficiency.

## 7. Completion gates and remaining scientific uncertainty

All three component gateways currently admit their exact claims, and Lead has found no specific unresolved mathematical counterexample or mismatch in their combination. The remaining mathematical validation is the independent review of THIS fixed full combination, in particular C3's complete physical/finite generator bounds and their precise match to D5, then the normal root gateway. The independent reviewer must report concrete gaps if any; component PASS does not predetermine that answer.

This text does not claim that the later combined review or administrative completion had already occurred. The historical completion failure is recorded separately and is not a mathematical counterexample.

[Private administrative workflow omitted from the public export.]

After this stage, the broader research problem still requires scientific synthesis across T1 foundational convergence, T2 joint same-risk resources and T3 reliability, with strong baselines and distinct observation/cost models explicit. This stage alone does not settle that synthesis or establish an architecture advantage.


---

# Bounded D6 primary map

Source: `outputs/001-input-contamination/counter/d6-scope-map-v1.md`; SHA256 `e4ae322376acca4e3a88e3c591700f5a074388d91637140d48b7a223122ba03f`. Source text follows unchanged.

# D6 primary and strong-DIRECT scope map, v1

Counter, 2026-10-26. Current fifth-stage root integration companion to
c2-proof-v1.md, exact C2 obligation
52a14a0c60279133c7acc7067c15eb4cfbff32368f8a721e59df9bf3eecd9ff1.
This is a bounded source/model comparison, not an independent Fact or a
premise of the self-contained C2 proof. Only the two D6 works and the
specified Pydi/Jog supplement are compared. Current PROBLEM.md D1-D7 and
inputs/SOURCE_CORRECTIONS.md govern scope.

## 1. Pinned primary locations and what they support

The supplied PDFs and their page-preserving text were consulted locally;
no new retrieval, literature expansion or diagnostic rerun was needed.
PDF page numbers below count physical pages starting at1. Original source
files are preserved unchanged. SHA256 values here identify the PDF bytes,
not the convenience text files.

| Primary | Exact locations | Supported scope and limit |
| --- | --- | --- |
| Chen/Gao/Ren, *A General Decision Theory for Huber's epsilon-Contamination Model*, arXiv1511.04144v2 | PDF pp1-2, eqs(1)-(2); pp3-5 and Theorem2.1; p6 Theorem3.2; pp13-14 Lemma6.1 and Theorem2.1 proof | IID observations from a Huber mixture with arbitrary contaminating law; robust testing through TV and an estimation modulus. The separate contamination neighborhoods do not impose one shared hard-edit input kernel. Theorem3.2 is attributed there to their earlier2015 result. |
| Pydi/Jog, *Adversarial Risk via Optimal Transport and Optimal Couplings*, ICML2020, PMLR119:7814-7823, main | PDF p3 section2.1 and Theorem1; p4 Definition1/eq(5), Theorem2/eq(6), Corollary3.1/eq(7); pp5-6 section4 and Theorems5-6 | Equal-prior binary classification, class-dependent point maps and separate Wasserstein distribution attacks. Transport-tail/testing and finite submeasure ideas are strong existing tools. Their stated model permits separate class maps and does not supply the present common input-row quantifier. |
| Same work, supplement | PDF pp1-4 Theorem1, Lemmas0.1-0.3, Corollary0.1; p5 Theorem2; p7 Definition1 for unequal masses | Supplies the detailed transport/testing proof, the Markov tail bound and an explicit unequal-mass submeasure definition. Supplement Theorem1 corresponds to main Theorem2; its numbering differs. |

Official primary URLs and pinned PDF hashes:

- CGR: https://arxiv.org/pdf/1511.04144v2 ; SHA256 `538cda7c3ea92a31a394e85b2928a6309cd751b9f4afc5e1732b2bf2a4b8f645`.
- Pydi/Jog main: https://proceedings.mlr.press/v119/pydi20a/pydi20a.pdf ; SHA256 `df20b171617bd33522b798fa59e9f52ab29401fc463328869297c19dd7d5a19a`.
- Pydi/Jog supplement: https://proceedings.mlr.press/v119/pydi20a/pydi20a-supp.pdf ; SHA256 `332e09858ae7e474e967a6dcc10274de57a3a9e16f0455296efff664b1e25d74`.

The CGR digest above follows SOURCE_CORRECTIONS.md and agrees with the
actual PDF and old download manifest. The old primary-claim-map prose
shortened that digest incorrectly. This new map corrects the citation;
it does not modify that historical file, the PDF, or any old admission.

CGR's displayed testing separation is TV(P0,P1)>2epsilon and its displayed
modulus uses TV(P_theta1,P_theta2)<=epsilon/(1-epsilon). Pydi/Jog's main
Theorem2 uses the transport tail cost 1{d(x,y)>2epsilon}; Corollary3.1
bounds it through the p-Wasserstein cost divided by (2epsilon)^p.
These are relevant baseline principles; no application of either theorem
is required to justify the current finite C2 proof.

## 2. Exact bridge still required in the present model

| Coordinate | Current D1-D2/C2 requirement | Location in new C2 proof |
| --- | --- | --- |
| Observation object | One complete binary history; last pair fixed on every input/seed | sections1,4,7 |
| Conditional experiment | Actual same-trajectory S_N=00, with probability u0=k/N | direct stationary reversal in section4; section8 |
| Quantitative coupling | Entire original conditional histories, every intermediate pair and every free symbol; no division by rare-query probability in the error bound | sections4-6: C<=97(2Nu+96)Delta<=10000(1+Nu)Delta |
| Kernel quantifier | One T from public N,k fixed before predictor/Q/actual source label; legal under every D1 source | sections3,7 |
| Residual transport | Jordan masses retain mass tau; remove cycles, collapse paths; no normalization shortcut | section2 |
| One input row | The same row acts on common mass; good signed masses cancel; bad fractions stay at their own inputs | section3: TV(PK,QK)=bad mass<=C/(2k) |
| Budget | At most k earlier flips for every raw input and every finite private seed; not an expected-distance constraint | explicit Hamming midpoints and uniform integer seed intervals, sections3,7 |
| Conclusion | TV<=1/64 after private-seed averaging; every common full-Z predictor has one t_* for R_00>=c AND R_av>=ck/N | sections7-8 |

An entire dependent trajectory can be a single feature in an optimal
transport model. Dependence alone therefore does not establish a gap from
Pydi/Jog. What is proved here is the specific D1 full-history cost bound
and the one shared hard-budget input-row channel, followed by the actual
terminal KL reduction. The generic testing, transport-tail and submeasure
steps are baseline ideas. No novelty or publication-centrality inference
is made from this bounded comparison.

## 3. Strong full-Z baseline and concrete DIRECT

The C2 comparison class contains EVERY common randomized predictor on
Z,N,k,Q, with unrestricted output probabilities and unlimited computation.
It may know the public witness pair and fixed T. In particular this includes
strong direct scanners using all observed symbols, re-encodings, all
statistics of Z, and the concrete D3-D4 DIRECT implementation. Neither
clean history nor private channel seed is supplied to any member of this
class. The proof does not restrict a baseline to the JOINT internal19 words.

The concrete DIRECT upper family owns the same full observed batch Z,
computes eight dirty-prefix triple counts, and selects the row using the
actual preserved terminal pair. Its dirty prefix endpoint has no protection
or clean side information. It uses the identical D3 smoothing/clipping/grid
rule as JOINT, including k=0, Q=2 and the real N=3,4,5 uniform branch.
C3 must separately prove bit identity for every individual observed Z.
C2 alone does not prove a resource or implementation assertion.

| Implementation | D4 finite selected-row/output table | Pricing obligation |
| --- | --- | --- |
| DIRECT | 8+46 operations, with paid full-input acquisition, count scan and cleanup in addition | Every separate D5 packed bit-register online/offline coordinate |
| JOINT | 17+46 operations, with paid frontend/input/feature/endpoint acquisition and cleanup in addition | Every separate D5 principal batch-hybrid dense/physical-scalar online/offline coordinate |

The two D5 models are distinct. The theorem neither equates those budgets
nor proves JOINT efficiency superiority, optimal costs, an old Bstar cap,
or a uniform common resource advantage. A future same-budget superiority
claim would require additional matching cost assumptions and evidence.

## 4. Exact root integration text

After current C1 and C3 are admitted, either implementation emits the same
D3 predictor on the same Z. C1 applies to the SAME globally admissible
channel constructed in C2, at u0=k/N and C2's SAME selected t_* for that
predictor. Consequently, on this same actual-terminal experiment,

    c*k/N <= R_av
           <= 16000000/(3N)+135680*k/N+3/Q,
    R_00 >= c,     c=1/3276800000000.

The selected t_* may depend on the common predictor and public tuple.
It is one source for both lower inequalities. The channel is already fixed
independently of predictor and Q. These facts give an O(k/N) contamination
upper contribution and an Omega(k/N) full-Z lower. The 1/N and1/Q terms
have upper bounds only here. Since DIRECT and JOINT agree pointwise, this
contract establishes no statistical superiority of JOINT.

Preserve the exact exclusions in D6: no every-source damage, no complete
conditional-risk classification, no small unconditional history-TV claim,
no deterministic common attack attainment, no practical/optimized constant
claim, no learning/novelty conclusion, and no time-causal sensor, all-layer
or IEEE fault theorem. Existing source reviews and old roots are provenance;
current native component/root evidence, fixed independent review, fresh
[Non-scientific operational metadata omitted.]
Completion of this stage leaves the v10 mother problem active.
