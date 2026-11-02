# FR001 independent composition review

2026-11-02. **ACCEPT on the stated domain and fixed complete-master interface.** No blocking finding and no frozen-source edit required. This is an independent-context LLM composition/scope/resource audit, not formal verification, a fresh reconstruction of all underlying proofs, or external peer review.

Candidate: `precision_frontier/FR001_full_risk_frontier_v1.md`, SHA256 `7c1305193d61115b0f95f3ed28a0321beeaf9a82dac7172c49fde4e8620f4d1f`.

## 1. Evidence actually inspected

I read FR001, AU001, SF001 and PF001 in full, including their theorem statements, hypotheses and composition arguments; inspected the actual NB002 theorem, retained finite-prefix domain/interface, integer decoder, output rounding and resource ledger; read R011's actual class, statistical scale and predictor theorem, and the separate NB002 output-only companion. I also inspected the prior independent review discussions and the AU001/SF001/PF001/NB002 root acceptance receipts. The present task inherits the already accepted deeper proofs rather than counting their verdicts alone as evidence of the required theorem statements.

All ten entries in FR001's author manifest match their actual byte lengths and SHA256 hashes. Each of the four acceptance receipts names the actual proof hash now on disk. Historical “candidate/pending” headings in frozen proofs do not invalidate later matching acceptance receipts. Independent review bindings accompany this file, including direct NB002, R011 and output-only sources omitted from the short author manifest.

## 2. Same experiment and correct inequalities

AU001 §1 is an arbitrary-initialization upper for K>=2, M>=64, integer h>=4, every beta in [0,1], and the all-state two-step minorization class, including off-support starts. SF001's theorem is a stationary-initialization lower on K>=3 with exactly the same M,h,beta domain and class condition. Both use the actual terminal pair and unconditional expected TV on the same observed trajectory. Neither supplies the hidden stationary law to the decoder. Their common domain is precisely FR001's K>=3, M>=64, h>=4, beta in [0,1].

The lower is against arbitrary real simplex outputs, arbitrary computation and source-independent randomization at the original complete finite SRC cut: all 9K+1 masters, original exact query/endpoint/mode/flag fields and public metadata, but no raw-history or clean evaluator port. NB002 §§2,8 explicitly retain that cut and read only those data; its suffix is a legal deterministic member of the lower's larger decoder class. Its Q-grid simplex output is, in particular, a legal real simplex output. Its h>=4 legality is the proved frequency-prefix extension, not a claim that the old complete SRC smoothing program was legal there.

For any common decoder D, its supremum over stationary initializations is no larger than its supremum over arbitrary initializations. The admissible decoder classes are identical (including if beta is public), so taking infima proves R_stat<=R_all. Selecting the legal NB002 decoder gives R_all<=risk_all(B_NB002). The stationary lower is not obtained by restricting an arbitrary-start lower; it is SF001's explicitly stationary theorem. At beta=0, possible nonuniqueness of stationary certificates does not upset the subset inclusion: every stationary-certified experiment is still an arbitrary-start experiment. No proof oracle or extra lower-proof side information is incorporated into FR001's observed interface.

## 3. Constants, endpoints, cap and all-Q uniformity

AU001 (AU1) states, for this exact same beta-blind map,

    risk_all(B)<=min(1,2^16 L+(2^14 K^3+5320K^5)W).

R011 defines L=max(F,D,T), with F=max(i,min(1-beta,a)), D=(1-beta)^(M+1)g and T=(1-beta)^(M/2)hstar. Its i,a,hstar are all <=g=min(1,sqrt(K^5/(M+1))). Thus L<=g<=K^(5/2)/sqrt(M). Because s=M^(-1/2)<=H and W<=H, the displayed AU001 upper is <=min(1,C_K H) with exactly FR001's C_K. SF001 supplies exactly 2^-336 H as its all-Q stationary lower. These establish every inequality in FR1 without summing different lower witnesses or choosing different predictors by beta.

AU001's upper has no Q ceiling and treats beta<1/M, including zero, separately from positive beta; its equality crossover and beta=1 endpoints are legal. SF001's lower has no Q ceiling because its §3 completes the restricted IP002 domain using stationary IID floors. In particular it retains the IP002 minimum and finite Q cutoff before the scalar completion. FR001 imports that completed theorem, not IP002 alone. Consequently beta may vary with M arbitrarily, and Q may be any legal dyadic at every finite parameter value. The constants have no hidden beta, M or Q dependence. Their K dependence is deliberately not sharp.

For the cap claim, Mb>=1 implies W<=[1+ln(1+Q)]/Q. The latter function decreases on Q>0; at Q=16 it is <1/4 since ln17<3. Also s<=1/8. Hence H<1/4 throughout the domain. The upper unit cap remains essential to the literal risk bound when C_K H>1; the claim is not that risk equals an uncapped expression with constant one. Nonetheless 2^-336 H<=R<=C_K H proves the stated Theta_K relation. The large constants do not invalidate this finite-domain rate classification.

## 4. Threshold meaning

PF001 supplies a genuinely uniform finite threshold: every legal Q>=Q_star suffices with one fixed B_K/sqrt(M) multiplier, and a legal dyadic lies in [Q_star,4Q_star]. Conversely, for every fixed C>0, a guarantee R_stat<=C/sqrt(M), or the stronger R_all guarantee, implies Q>=c(C)Q_star. Its c(C) is positive and independent of M,beta,K>=3. FR001 correctly states existence of a fixed K-dependent sufficient multiplier rather than sufficiency for every prescribed multiplier. It also explicitly allows budgets larger than the threshold; the displayed h_star is a threshold location, not an equation required of every successful h.

The same fixed map at supplied K,M,h never reads beta. Choosing a near-minimal hardware budget from a known beta promise is distinct from learning an unknown beta. FR001 keeps that distinction. The examples beta=0 or O(1/M), and beta sqrt(M) bounded below, follow from the expressions with the usual fixed constants in those conditions. They introduce no new domain or algorithm.

## 5. Resources and output-only comparison

NB002 §9 directly supports six heads, hybrid depth O(Kp^2), width O(Kp), zero-inclusive dense coefficient bits O(K^3p^5), all-token pointwise/QKV bitwork O((M+3)K^3p^6), and uncached attention O((M+3)^2(K+p)p^2), with p=4h+4ceil(log2(M+K+4))+64. Its masks, positions, inputs, master/output banks, history/QKV, control/addressing, explicit holds/copies/clears, finite evaluator, cache creation, offline generation/sorting/format writes and simultaneous-phase peak charges persist. AU001 performs no suffix computation at runtime; its mixture is an analysis of full suffix laws under the original kernel. Thus FR001 causes no new computational charge or unauthorized deletion of an old one. The separate PURE expansion is correctly not assigned hybrid costs.

Terminology clarification (nonblocking): NB002 bounds complete online coefficient/arithmetic words, including full products and guards, by **128p bits**. Thus FR001's phrase “full arithmetic word p=...” should be read as its inherited word-size parameter/O(p) scale, not an exact assertion that every product fits in precisely p bits. The instruction that all NB002 charges remain and the explicit inherited formula make the intended bound recoverable. Future expository summaries should retain “<=128p bits” to avoid this shorthand ambiguity.

The output-only comparison is independently justified by the actual companion theorem: exact full-history ALG followed by ordered Q-grid rounding has risk <=min(1,2^16 L+(K-1)/Q). R011's bound on L then makes Q of order sqrt(M) sufficient at fixed K, uniformly over beta including zero. This comparator has history access and paid direct counting, unlike FR001's frozen bank decoder. The claim is therefore a representation-specific separation, not an output-grid or architecture-universal lower bound. Neither larger suffix computation behind the cut nor real outputs reverse the information lower; a changed encoder or extra pre-cut statistics can change the experiment.

## 6. Final disposition

Accept FR1, FR2 and the quoted threshold consequence on the explicitly stated domain. The contribution is a precise elementary composition of accepted all-Q upper/lower theorems, not a new lower mechanism or external novelty certificate. K=2 logarithmic necessity, M<64 completion, sharp joint-K rates, new encoders, training and broader architectural optimality remain open exactly as stated. No frozen proof was modified.
