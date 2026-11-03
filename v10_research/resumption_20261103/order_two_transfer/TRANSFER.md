# O2T001 — transfer back to binary order two at the critical certificate

Local candidate, 2026-11-03. Independent review and root acceptance required. No external writes. This is an interface-transfer theorem, not a new all-certificate phase diagram. Historical pending labels in accepted source candidates are superseded only by their respective root receipts.

## 1. Experiment fixed before the comparison

For each M≥64 use X_0,...,X_(M+1), Y_i=(X_i,X_(i+1)), and a homogeneous binary order-two table θ_ab(c). There are M pair departures i=0,...,M−1. Admit exactly sources with a stationary Π satisfying **P²(u,v)≥Π(v)/M for every pair u,v**, including unsupported rows. The supplied certificate is 1/M, not necessarily optimal. Permit every initial PAIR law μ, including mass outside stationary support. θ,Π,μ are hidden.

A single source-independent offline kernel on all words changes at most k of positions 0,...,M−1 on every output and preserves both final symbols; k ranges over 0,...,M. It cannot see predictor seeds or subsequent channel noise. The one encoder/decoder at fixed M works for every k, source, initial law and legal kernel. It may depend on M and known fixed channel W, not hidden quantities. Loss is unconditional expected unsquared TV to **θ_(Y_M), a next-SYMBOL law** at the actual protected terminal pair. Normalize by g_M(k)=max{M^(−1/2),k/M}.

Two distinct receiver models:

* Supplemental: exact eight triple counts and final pair are free. An optional initial pair changes nothing: the triple-flow imbalance reconstructs the initial pair from counts and final pair (sum of outgoing minus incoming edges equals initial-state indicator minus terminal-state indicator), a purely combinatorial identity independent of source order. No other raw windows or path-dependent information are supplied.
* Whole-message: NO counts, endpoint, raw symbols or path-dependent seed are free. All sample-dependent information passes through R binary physical channel inputs.

The full corrupted word is accessible to the encoder in both models. R is fixed before the sample, not adaptive or variable. W is a fixed known binary-input finite-output memoryless channel, independent of M. Its noise is fresh conditional on the entire pre-channel experiment. Independent public/private coins are allowed; public coins carry no path-dependent information. No feedback, timing, length, mask, edit-location or noise-seed side channel. Outputs/erasure indicators from W are observed exactly; counts in the supplemental model are uncorrupted *as messages*, though computed from the corrupted source word.

## 2. The genuine order-two upper interface (not first-order FOU)

Sources: recovered_science/positional_manuscript_finite_20261102/main.tex and its entire sections/proofs_positive.tex; acceptance: recovered_science/intake/positional_finite_manuscript_root_acceptance.json. The author read the complete actual main and positive proof, not just an abstract or candidate receipt. In particular:

For u=(a,b), set d(u)=1−a, J'_u=H_ab0+H_ab1, C'_u=H_ab,d(u), and A'_u=Σ_(i=0)^(floor(M/2)−1)1{(Z_i,Z_(i+1))=u}. At protected u=Y_M form G=1{512A'_u≥J'_u}. The exact receiver's designated probability is qhat=C'_u/J'_u if J'_u>0 and G=1, otherwise 0. Convert to symbol-1 probability qhat when d=1, and 1−qhat when d=0.

The proposition labeled `prop:finite-upper` (do not rely on a floating numerical proposition number) proves for every start and every legal kernel

    R_exact ≤ min{1,65536/√M+65536/(M√β)+2^23 k/M}.

Consequently at β=1/M,

    R_exact ≤ min{1,2^17/√M+2^23 k/M} ≤ C2 g_M(k),
    C2=2^17+2^23=8519680.                         (O2)

This is the ORIGINAL order-two half gate on M pair departures: no discarded X_0 or first-order transition pooling. Equality in the gate is accepted. At J'=0, G=1, but the separate denominator check returns qhat=0. Hence a single exact supplemental bit suffices on all words.

### Load-bearing all-start audit

The proof is not a stationary argument disguised as an arbitrary-start bound. Actual-terminal occupation is ≤16w/(M+1) without irreducibility. Independent row stacks prove empirical deviation ≤512/√(M+1), without conditioning stacks on terminal row or count. Every relevant fixed-window count perturbation is ≤6k, with terminal protection fixing the selected row. Pathwise gate reduction uses reciprocal term 48k E[1{A≥J/1024}/(J+1)], imbalance E[q1{J>0,A<J/256}], and tails at 6156k+1,3078k+1. The half reciprocal bound is 130944/M for every four-state chain/start, by conditioning on the deterministic prefix and applying the actual-terminal occupation inequality in the suffix. Thus the corruption coefficient is 48·130944+16(6156+3078)=6433056<2^23.

The certificate enters the imbalance bound 65536/(M√β). In full support, flow identities and two specific all-state certificate entries give ΣΠ(u)q_u max{H_u,1/Π(u)}≤40/√β; endpoint/lower-tail/joint-tail bounds are uniform over starts. The support lemma says positive all-state certificates permit only full support or one absorbing diagonal. For singleton 00, active states A=01,B=10,C=11 are compared to the reflected chain obtained by redirecting B→00 to B→A. Original active-path probability is dominated by reflected-path probability without conditioning on survival. With weights (b,0,τ), the reflected weighted scales sum to ≤2, yielding 1728/M; the remaining e·Pr(Y_M=B) is the first-hit point mass Pr(D_00=M+1)≤4/(M+2). Boundary b or τ=0 follows by continuity only in the reflected finite-path law, not an unproved certificate-preserving approximation. Absorbing 11 follows by symbol exchange. Hence unsupported starts are genuinely covered.

For the exact-baseline factor Γ_0^(2)(M), the accepted finite-window theorem at r=2 gives

    2^−30 ell_M ≤ Γ_0^(2)(M) ≤ 2^20 ell_M,
    ell_M=1+ln((M+2)/2).                            (BL)

The upper uses only counts and final pair. The lower grants both endpoint pairs and is therefore valid with or without initial pair. The original full-history floor gives Γ≥1/96. We import these accepted results, not claim a fresh reproof of all negative/finite-horizon lemmas here.

## 3. Why all required lower bounds survive expansion

Embed any stationary first-order table T as θ_ab(c)=T(b,c). Its stationary pair law is Π(s,z)=π(s)T(s,z). Then

    P²((a,b),(s,z))=T(b,s)T(s,z).

Thus the sufficient ratios for all states are T(b,s)/π(s). The accepted BSC001/FOT001 alternatives T(0,1)=a,T(1,0)=t have ratios (1−a)(a+t)/t,a+t,a+t,(1−t)(a+t)/a; their parameter domain bounds each below by β=1/M. The null T(0,1)=β,T(1,0)=β/2 has ratios 3(1−β),3β/2,3β/2,3(1−β/2)/2, again ≥β. They are stationary admissible members of the new order-two/all-start class. Their legal kernels, exact baseline collisions, actual terminal targets and same-k comparisons remain literally unchanged. Enlarging the table class cannot weaken a minimax lower. It does NOT transfer a first-order upper.

The IID Bernoulli(p) subfamily, p∈[1/4,3/4], has P²(u,v)=Π(v) on every row and constant next-symbol target p, so both the full-history floor and whole-message cardinality lower are valid members. These inclusions preserve the same normalization g_M and same M, not a hidden horizon conversion.

## 4. Supplemental four-channel classification

The accepted BCC001, BSC001 channel arguments are source-free once interfaces (O2),(BL) and the admitted lower witnesses are supplied. Here are the precise replacements. Put c0=2^−30, C0=2^20, cf=1/96 and Cg=C2. Remove symbols null under both rows; S_b is row b's support. Define λ=Σ_y min{W(y|0),W(y|1)} and h=Σ_y√(W(y|0)W(y|1)).

1. **Identical rows:** channel outputs can be simulated by a baseline-only receiver, so Γ_W^(2)(M,R)=Γ_0^(2)(M) for every finite R. No constant schedule.
2. **Disjoint supports:** one input transmits G exactly; factor ≤C2. Zero inputs fail asymptotically by (BL). Minimum constant-adaptation supplemental length is one.
3. **Unequal overlapping supports:** length order Θ_W(log log M). The common product submeasure of mass λ^R works for every randomized full-word code, giving Γ≥max{cf,c0 ell_M λ^R}. Choose an exclusive event E with W(E|0)=0 and p=W(E|1)∈(0,1), relabeling inputs if needed. Encode G=0 as (0,1), G=1 as (1,0); event E identifies the bit, otherwise erase. Two physical uses give an exactly balanced *coarsened* BEC, independent of the pre-channel state, failure ε=1−p. Repeating n=floor(R/2) blocks and using the baseline on all-erased failure gives Γ≤C2+C0 ell_M ε^n. The raw output is not claimed equivalent to a BEC.
4. **Equal supports, distinct rows:** length order Θ_W(log M). Define κ=max_y max{W(y|0)/W(y|1),W(y|1)/W(y|0)}∈(1,∞). Product likelihood domination for any input mixtures is κ^R. The accepted BSC001 transport proof applies unchanged to the embedded first-order witnesses: if M+1≥2^160 and κ^R≤(M+1)^(1/8), Γ≥2^−32 ln(M+1). It transports only nonnegative clean-loss penalty, not target separation; same legal attack and actual-terminal clean loss remain essential. Thus bounded factors eventually require R>ln(M+1)/(8 ln κ). For sufficiency repeat the genuine O2 gate and likelihood-test; each conditional bit error is ≤h^R, so Γ≤C2+√M h^R. Choosing h^R≤M^−1/2 attains C2+1.

All sufficient target factors are feasible constants such as C2+1, not arbitrary tiny requested constants. Supports/rows fixed in M and finiteness are essential. No partial-support fixed-R exponent is claimed sharp. For fixed BSC crossover 0<η<1/2 this gives Θ_η(log M); detectable erasures retain Θ(log log M).

## 5. Whole-message transfer with no free receiver query

Encode the **selected** order-two row statistics, not all rows:

    (J,C,d,G), B=2ceil(log2(M+1))+2,
    J=J'_(Y_M), C=C'_(Y_M), d=1−Z_M.

The encoder knows the true protected pair (Z_M,Z_(M+1)) and uses BOTH symbols to select the row. The receiver needs only d once J,C are selected. It reconstructs qhat as in §2 and outputs symbol-1 probability qhat if d=1, otherwise 1−qhat. The d bit is paid even on rejection: qhat=0 means output complement of d, not a universal symbol-0 fallback. Invalid decoded fields receive any fixed distribution. This payload reproduces (O2) exactly, including J=0 and equality cases. B is a sufficient fixed width, not a minimal exact description claim.

This compression relies on next-SYMBOL loss. If the required action were a distribution on next PAIRS, one would also need the terminal second symbol to locate the common successor support; the payload assertion must then be revised. We make no such target change.

The accepted WMC001 code proof depends only on B and maximal message error, so carries over unchanged. For h=0 send B bits directly. For 0<h<1 set δ=1/4, a=1−H_2(δ)>0 and choose integer

    R≥max{B/a, (B ln2+0.5ln M)/(δ(−ln h))}.

A finite greedy binary code has K=2^B labels, minimum distance ceil(δR), and maximal ML error ≤2^B h^(δR)≤M^−1/2. Conditional on EVERY corrupted payload this holds; no average-to-maximal-error leap. Coupling gives risk ≤(C2+1)g_M(k). Hence O_W(log M) for every distinct-row W.

For the reverse bound, the embedded clean IID prior p uniform on [1/4,3/4] has only Q=2^R possible input labels. Freeze independent shared coins and a random counterfactual channel/decoder reconstruction A_h for each label. Each realized prediction lies in a set of ≤Q points independent of p; integrating distance to that set gives prior average error ≥1/(8Q). This remains true for any sample-dependent randomized encoder selection. Therefore Γ_total,W^(2)≥√M/(8·2^R), forcing R≥0.5log2 M−log2(8C) for a bounded factor C. Identical rows instead make the entire receiver output independent of p, yielding clean prior risk ≥1/8 and Γ≥√M/8 for every R.

Thus **total physical communication is Θ_W(log M) for all distinct-row channels**, even disjoint supports or erasures; identical rows are impossible. These are different models from §4, not competing bounds on one model.

## 6. Resources and limits

A single scan maintains eight triple counters, four first-half row counters, position and rolling bits; at the end select Y_M and form the payload. This costs O(log M) auxiliary bits, O(M) word-RAM updates or O(M log M) naive bit operations; raw input reading is included, resident input storage M+2 bits is not auxiliary space. No sample copy need be stored. Supplemental counts are uncharged receiver inputs; total communication pays for selected counts. Neither model gives scan or codebook storage for free.

WMC001's conservative explicit-code ledger survives because B is unchanged: K<16(M+1)^2, R=O_W(log M), codebook KR=O_W(M² log M) bits per endpoint, greedy preprocessing O(2^R K R), brute-force ML polynomial in M. For fixed rational W, common-denominator integer likelihoods support exact finite arithmetic; arbitrary real W yields statistical existence, not an unprovided computable-real access model. ECC-style efficient alternatives, if separately accepted, transfer whenever their guarantee is uniform maximal payload error and costs depend only on (B,M,W); this note does not accept any pending efficient-code candidate by association.

**Scope boundary:** earlier first-order results cover unrestricted first-order tables. This theorem covers general binary order-two tables ONLY with the supplied all-state critical certificate 1/M. The original positive proof does give a β-dependent bound, but its 1/(M√β) term does not justify uniform g_M factors for all β. No no-mixing order-two theorem, full-β phase diagram, general order, corrupted public-count channel, unknown/M-dependent W, variable-length protocol, neural realization, learnability or novelty certification is claimed.

Dependencies: accepted positional finite manuscript receipt; BCC001 channel_classification/ROOT_ACCEPTANCE.json; BSC001 bsc_sharp/ROOT_ACCEPTANCE.json; WMC001 whole_message_cost/ROOT_ACCEPTANCE.json, with their bound source files. Independent LLM review is not formal verification or external peer review. Candidate remains local and unpublished.
