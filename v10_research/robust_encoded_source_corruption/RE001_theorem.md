# RE001 — Robust deep encoding of symbol-edited Markov trajectories

2026-11-02. POST-STAGE8 candidate. Fresh full independent review and root acceptance required. This is a new theorem, not a change to any frozen proof, manuscript or archive. Independent LLM review and finite diagnostics are not formal verification or external peer review; no novelty claim is made.

## 1. Result first: source corruption survives; the uniform-bank precision penalty need not

Fix K>=2, R>=2, M>=64, 0<=k<=M integers, beta in [0,1], Q=2^h>=2, and L>=0 with chi=2^L. The clean source is homogeneous second-order on K symbols. Its pair kernel T admits a hidden stationary Pi satisfying T^2(u,v)>=beta Pi(v) on ALL pair states, including unsupported starts. Write Y_j=(X_(j+1),X_(j+2)), j=0,...,M. The actual target is theta_(Y_M). Initialization is either Pi or an arbitrary unknown pair law. Risk is unconditional expected TV.

An offline source-independent randomized kernel edits at most k of positions 1,...,M of the M+2-symbol observed word; it preserves positions M+1,M+2. It may inspect the whole word but receives no source table, stationary law, initial law, future symbol, or hidden parameter. The encoder sees ONLY this corrupted word Z. It never sees the clean word, edit mask or attack seed. Its paid causal local triple table and uniform pool feed a compander and robust geometric packing. Exactly D=RK^3 coordinates cross the information cut, after the explicitly required exact pre-fault clipping to [0,1], an arbitrary one-shot vector perturbation of coordinatewise magnitude <=delta, channel clipping and downward Q-grid rounding. The port attack may cooperate with the edit kernel and be history adaptive but is not supplied an unknown source parameter. Every upper below is pathwise in both attacks.

Only these D labels, the protected terminal pair S=(Z_(M+1),Z_(M+2))=Y_M, and source-independent public metadata reach the decoder. No raw/corrupted history, initial symbols, clean or corrupted counts, exact row mass, hidden work array, timing channel, other-token output or unquantized rail survives. The rational post-cut output is NOT constrained to the same Q grid. Optional output rounding has a separately charged error.

For finite setup supply a nonnegative rational certificate rho satisfying

    delta <= rho <= 2(delta+1/Q),       u=rho+2/Q.             (1)

Its description uses FULL binary numerator and denominator lengths, not a compact denominator-exponent encoding. It is a public budget, never inferred from the observed word. Let b_rho be its full bitlength. The encoder may use this public budget to choose its packing scale. No irrational delta oracle is needed. Delta may be any nonnegative real; for large budgets the capped risk statement is simply uninformative. Fixed c/Q port noise is obtained by taking rho=ceil(c)/Q (including rho=0 if c=0).

Choose either of two realizable branches:

* **Scalar branch:** expose t=g_L(x')/2 in one of the R coordinates per triple, pad the rest by zeros, and set epsilon=2u.
* **Packed branch:** choose a dyadic integer N>=2 satisfying 4R u N<=1. Apply GN001's shifted no-plateau R-dimensional snake to t, and set

      epsilon = 8R u/N^(R-1).                                (2)

All these epsilons are positive rationals. They safely upper-bound the exact compander-space reconstruction error. The complete bounded-primitive depth is d=O_R(1+L+log N), with N=1 in the scalar branch; width is O_R(K^3), independent of M,Q,L,N. Fixed bounds on primitive fan-in, heads, coefficients and reachable states are uniform. Every actual affine/ReLU stage, including the final clips, is counted. A sufficient uniform fractional precision is

    P >= 4h+c_FA(d+2),                                       (3)

enlarged to cover the paid coefficient/guard requirements. The finite evaluator and all decoder resources are specified in §7; h is cut precision, not working precision or output precision.

Put s=M^(-1/2), e=max(beta,1/M) for K>=3 and e=max(sqrt(beta),1/M) for K=2. Define f_e(0)=0 and

    f_e(v)=v[1+ln(1+1/(M e v))], v>0,
    tau=k/M+epsilon^2+epsilon/chi.                            (4)

There are finite constants C_K depending only on fixed K such that the constructed deterministic finite rational decoder satisfies, for every allowed attack and BOTH initialization models,

    risk <= min{1,C_K[s+epsilon+f_e(tau)]}.                    (RE1)

For K>=3, the decoder is both k-blind and beta-blind and is just add-one applied to the reconstructed corrupted frequencies. For K=2 it is beta-blind but uses public k and epsilon,chi to compute a data-derived confidence radius and a fixed-orientation lower envelope (§5). There is no claim of binary unknown-k adaptation.

For ANY encoder/decoder seeing only the corrupted word (including arbitrary reliable computation and no cut), accepted SC002 and SC003+BT002 imply the source-statistical lower

    risk_minimax,stat >= c_K H_edit,
    H_edit=min{1,max{s,f_e(k/M)}}.                            (RE2)

The same lower holds for this architecture with port noise, because zero port noise is admissible and full corrupted history can simulate its complete finite encoder/decoder. Consequently, whenever epsilon<=A_R s and chi>=bitlength(M+1), RE1 is O_(K,R)(H_edit). The constructed noisy-cut predictor then attains the full-corrupted-history statistical order. This is an optimality claim for the surviving source/statistical term at that sufficient resource schedule, NOT a sharp global Q/delta/depth/encoder minimax theorem. In particular no matching unrestricted lower for epsilon, its scalar exponent R, or the architecture's total work is proved.

## 2. Actual encoder, geometric recovery and mandatory pre-fault clip

Let C'_abc count the M triples of the CORRUPTED word and x'_abc=C'_abc/M. These are encoder-analysis variables, not decoder side ports. At every historical token use its own causal prefix triple histogram; never copy terminal counts backwards. The exact radius-three local table is paid as in MG001/FA001, not an uncharged singleton-attention head. Public short-prefix fallbacks are used at positions 1,2. Uniform zero-logit statistical pooling has positive mask density. The synthetic terminal is public and is not counted as a symbol. Acquiring the two final symbols is a paid fixed-position operation. Optional zero-output heads, dense zero slots and masks are all paid.

On each of the K^3 frequencies apply the GD compander

    u_0=x', v_0=0,
    u_(j+1)=min(1,4u_j),
    v_(j+1)=v_j+2^(-j) ReLU(u_j-1/4),
    g_L(x')=v_L+2^(-L)u_L.

Retain old u until both updates finish. Its range is [0,3/2], t=g_L(x')/2 is in [0,3/4], coefficients are bounded by four and each iteration consists of a fixed number of actual primitive stages. The scalar branch exposes t. The packed branch composes the explicit GN001 shifted no-plateau snake P_R(t), built with dyadic N by bounded tent, shifted tent, clipping and saturated-doubling stages. GN001's rational descriptions are converted by exact signed quotient floor(2^P a/b), with the complete description length and conversion costs paid. No coefficient of size N is hidden in one stage. Only pointwise geometry is imported from GN001; its IID statistical argument is NOT used.

Apply the GD uniform-FA recurrence to this ENTIRE composition, including the initial pool, compander and snake. Fixed per-stage bounds yield a computable integer A>=2 with total error <=A^(d+2)(P+1)2^(-P). Choosing c_FA as in GD001, namely A(c_FA+5)2^(1-c_FA)<=1, gives the uniform <=1/Q tube and closes its own error<=1 bootstrap. Rational conversion has coefficient error <2^-P, so the same recurrence applies by GN001's explicit extension. This is not substitution of growing depth into an unquantified fixed-architecture constant.

**Before the fault**, for every raw P-lattice coordinate z compute

    C(z)=ReLU(z)-ReLU(z-1).

The signed guarded integer subtraction and ReLUs are exact on that lattice; actual output is in [0,1]. The ideal output was already in that interval, so this projection preserves the <=1/Q tube. Count these fixed clip stages in d BEFORE selecting P. Merely clipping after the fault would not prove the declared actual pre-fault cube membership; MG_final_clip_clarification.md is an essential dependency.

After attack, channel clipping and Q-floor, each coordinate is within delta+2/Q<=u of the ideal bank. The scalar branch therefore yields compander-space error <=2u=epsilon. In the packed branch nearest-segment projection w on the paid rational edge table has

    ||w-P_R(t)||_2 <= 2 sqrt(R)u <=1/(2 sqrt(R)N)<1/N.

GN001's local inverse gives

    |t_hat-t| <= 2 sqrt(2R)u/N^(R-1).

Clip 2t_hat to [0,g_L(1)] and invert g_L exactly to obtain y in [0,1]. The compander-space error is <=4sqrt(2R)u/N^(R-1)<=epsilon. The last inequality uses R>=2. Every recovery claim is pointwise for all histories, signs, correlated faults and boundaries. There is no stationary plateau error and no exact frequency-lattice premise. Scalar fallback uses the same clipping and inverse but no edge table. Unused padding is charged, not free.

## 3. New deterministic composition with SOURCE edits

Let C be the clean triple histogram, x=C/M, and S the common protected terminal pair. For one coordinate, the compander inverse obeys

    |y-x'| <=4 epsilon sqrt(x')+4epsilon^2+2epsilon/chi.        (5)

For completeness, its slopes are 2^j on [4^(-(j+1)),4^-j] and chi on [0,4^-L]. Hence for v<=w,

    w-v <=(2sqrt(w)+1/chi)[g_L(w)-g_L(v)].

If y<=x', this immediately suffices. If y=x'+a>x', use sqrt(x'+a)<=sqrt(x')+sqrt(a) and 2epsilon sqrt(a)<=a/2+2epsilon^2; rearrangement proves (5). This symmetric estimate allows y>0 even at x'=0. No one-sided zero-purity assertion is transferred through packing/noise.

One source edit changes at most three overlapping triples, each with histogram l1 change <=2. Telescoping over the k edits, including adjacent edits, gives

    ||x'-x||_1 <= alpha=6k/M.

Let r=sum_b x_(S,b)=J/M, r'=sum_b x'_(S,b), and Delta=sum_b|y_(S,b)-x_(S,b)|. Then r'<=r+alpha, and (5), Cauchy--Schwarz and sqrt(r+alpha)<=sqrt(r)+sqrt(alpha) give

    Delta <=alpha+4epsilon sqrt(Kr)+4epsilon sqrt(Kalpha)
                   +4Kepsilon^2+2Kepsilon/chi.

Use 4epsilon sqrt(Kalpha)<=alpha+4Kepsilon^2 to get the central new bound

    Delta <=4epsilon sqrt(Kr)+12k/M+8Kepsilon^2+2Kepsilon/chi
           <=4sqrt(K)epsilon sqrt(r)+8K tau.                 (6)

Clean quantities C,J,r are solely proof variables. They are not reconstructed exactly, tested by the algorithm, or smuggled through the cut. The square-root cross term is absorbed into k/M+epsilon^2, NOT into epsilon sqrt(k/M) treated as a new risk floor.

## 4. K>=3: add-one plus continuous occupation

Decoder selects S and outputs the EXACT rational simplex vector

    p_hat_b=(y_(S,b)+1/M)/(sum_c y_(S,c)+K/M).

It needs no edit budget, mixing parameter, clean row count or support test. For nonnegative vectors a,b with positive masses A,B, TV(a/A,b/B)<=||a-b||_1/A. Thus comparison with clean add-one gives

    TV(p_hat,p_clean_addone)
      <= min(1, Delta/(r+K/M))
      <=4sqrt(K)epsilon sqrt(M)/sqrt(J+K)
         + min(1,M B_K/(J+K)),
    B_K=12k/M+8Kepsilon^2+2Kepsilon/chi <=8K tau.              (7)

The universal actual-terminal occupation inequality for the K^2-state pair chain is P(J<w)<=min(1,K^4 w/(M+1)) for integer w>=1, for EVERY initial law. Its layer-cake consequence is

    E (J+K)^(-1/2) <=2K^2/sqrt(M+1).

No conditioning on the terminal row makes its successors IID. The bound gives an O_K(epsilon) expectation for the first term in (7), even with empty rows.

JP001 §2 supplies the explicitly completed continuous-A occupation interface, proved there from accepted IU001 and AU001, for every real A>0:

    E_mu min(1,A/(J+K)) <= L_K f_e(A/M),
    L_K=2K^2(17+ln480)+10K^4, e=max(beta,1/M).               (8)

Its domain includes beta=0 and arbitrary/unsupported starts; it does not require integer A or an actual edit count. Its proof uses the complete ordinary-T suffix mixture and the universal residual occupation bound, not an additive mixing burn error. Values A/M>=1 are handled by the unit cap. This exact interface, not a substitution in SC002's integer-k headline, is the dependency used here.

Since f_e is increasing, concave with f_e(0)=0, and f_e(cv)<=c f_e(v) for c>=1, (7)--(8) imply the explicit upper

    risk <= min{1,2^13 K^(5/2)s+8K^(5/2)epsilon
                        +8K L_K f_e(tau)}.                 (9)

The clean add-one comparator is R011 ORIGINAL as stated in MG001/SC002. This proves RE1 for K>=3 with any C_K dominating the three displayed coefficients.

## 5. K=2: data-derived row confidence radius

Use the public designated successor equal to the complement of the first symbol of S. The true designated probabilities on rows 00,01,10,11 are q=(a,b,e_exit,t_exit), exactly SC003/JP001's orientation. The decoder does not know these probabilities and does not test minority/support properties.

For the decoded two-coordinate row y, write rhat=y_0+y_1 and drow=||y-x||_1. Equation (6) and 4sqrt(2)<=6 give

    drow<=6epsilon sqrt(r)+16tau,   |rhat-r|<=drow.            (12)

From allowed data only compute a rational Sroot with

    sqrt(rhat)<=Sroot<=sqrt(rhat)+epsilon.

One finite procedure is: choose the least integer p>=0 with 2^-p<=epsilon by rational comparisons; write rhat=a/b, a>=0,b>0; choose the least integer j>=0 with j^2 b>=2^(2p)a by exact squared-integer binary search; set Sroot=j/2^p. Minimality proves the displayed bounds, including rhat=0. No real-root instruction is used. All epsilons supplied by §1 are strictly positive. The limiting lemma also permits epsilon=0 by setting Sroot=0 and bypassing this operation.

Set the observed-data radius

    Bhat=12epsilon Sroot+68tau.

Then, deterministically,

    drow<=Bhat<=18epsilon sqrt(r)+132tau.                    (13)

For the first inequality use r<=rhat+drow and (12):

    drow<=6epsilon sqrt(rhat)+6epsilon sqrt(drow)+16tau
         <=6epsilon sqrt(rhat)+drow/2+18epsilon^2+16tau.

Rearrangement gives drow<=12epsilon sqrt(rhat)+36epsilon^2+32tau<=Bhat. For the other direction, sqrt(rhat)<=sqrt(r)+sqrt(drow), the Sroot approximation, and 12epsilon sqrt(drow)<=drow+36epsilon^2 give

    Bhat<=12epsilon sqrt(r)+drow+48epsilon^2+68tau
         <=18epsilon sqrt(r)+132tau.

At epsilon=0 the two inequalities follow directly from drow<=16tau and Bhat=68tau. The radius does not require the recovered global histogram to sum to one.

Let y_exit be the public designated coordinate, B=M Bhat, tilde C=M y_exit and tilde J=M rhat. Output designated probability

    qhat=(tilde C-B)_+/(tilde J+B+2),                          (14)

with other probability 1-qhat. The denominator is positive and 0<=(tilde C-B)_+<=tilde J, so this is an exact rational simplex vector. It uses only allowed decoded data and public M,k,epsilon,chi.

By (13), complete selected-row count l1 discrepancy is <=B. If C,J are the CLEAN designated count and mass, then n=(tilde C-B)_+ satisfies 0<=n<=C, 0<=C-n<=2B, while D=J+2<=D'=tilde J+B+2<=D+2B. Thus

    0<=C/(J+2)-qhat<=4B/(J+2).

For J>0 let pemp=C/J. Since pemp-C/(J+2)=2pemp/(J+2),

    0<=pemp-qhat<=min(pemp,(4B+2)/(J+2)),
    |qhat-q|<=2|pemp-q|+min(q,(4B+2)/(J+2)).

The latter uses the 1-Lipschitz map z->min(z,c) with c fixed at its realized value. Random/data-dependent B creates no independence requirement. At J=0, n=C=0 and qhat=0; the same last inequality holds with empirical term zero because its minimum equals q. Applying (13) and min(q,u+v)<=u+min(q,v) yields

    |qhat-q|<=2 1{J>0}|pemp-q|
              +72epsilon sqrt(M)/sqrt(J+2)
              +min(q,A/(J+2)),
    A=528M tau+2.                                           (15)

This is the essential binary split. ONLY the deterministic additive floor is put inside true-q weighted occupation. The square-root-mass error is handled separately and is not incorrectly converted to a unit cap with the binary mixing cutoff.

The accepted SC003 clean comparator and universal four-state occupation give

    E 1{J>0}|pemp-q|<=8193sqrt(32)/sqrt(M+1),
    E (J+2)^(-1/2)<=8/sqrt(M+1).

JP001 §2's continuous-budget completion, importing precisely BIF001 §3.4 and BAI003 v2 §6, gives for every real A>=2

    E min(q,A/(J+2))<=4s+16672 f_e(A/M),
    e=max(sqrt(beta),1/M).                                  (16)

Its q is exactly this public orientation. Full support with beta>=M^-2 is BIF001's weighted arbitrary-start inequality. Positive-beta singleton support costs <=256A/M+16/(M+2)<=264A/M; symbol exchange preserves the orientation. Beta<M^-2 is covered by universal occupation, Psi(16A/(M+1))<=16 f_(1/M)(A/M). All unsupported starts and beta=0 are included; the program performs none of these case tests.

Monotonicity/subadditivity give f_e(A/M)<=528f_e(tau)+f_e(2/M). Since e>=1/M and ln(1+M/2)<=sqrt(2M), f_e(2/M)<=8s. Taking expectations in (15) therefore gives

    risk<=min{1,[2*8193sqrt(32)+4+8*16672]s
                  +576epsilon+528*16672 f_e(tau)}
         <=min{1,2^18 s+2^10 epsilon+2^24 f_e(tau)}.          (17)

This proves RE1 for K=2 and all budgets, including k=0. The untruncated full lemma, independently authored as a subtask but NOT itself an independent review of this theorem, is retained in RESC_binary_lemma.md.

## 6. Finite-scale packing schedule and statistical/source-optimal corollary

Let t0>0 be a public rational target compander error scale, supplied by its FULL binary numerator and denominator description of length b_t0 (not compact exponent coding). Its acquisition and all exact setup comparisons are charged in §7. If u<=t0 use scalar fallback, yielding epsilon<=2t0. Otherwise choose the least dyadic integer N>=2 with

    t0 N^(R-1) >=u.

The selection uses exact integer cross products, not square roots or logarithms. Then N<2(u/t0)^(1/(R-1)). The sufficient capacity condition

    u^R <= t0/(8R)^(R-1)                                  (10)

implies 4R u N<=1 and hence makes this a legal packed branch. It gives epsilon<=8R t0 and

    d=O_R(1+L+log_+(u/t0)).                                (11)

Condition (10) is sufficient, not necessary; it may be unnecessarily strong in the scalar branch. For statistical scale choose j=floor(floor(log2 M)/2) by integer bitlength and t0=2^-j, so s<=t0<2s. Choose m=bitlength(M+1), L=ceil(log2 m), hence m<=chi<2m. This selection is entirely finite and source independent. Under (10), epsilon<=16R s and d=O_R(1+loglog(M+2)+log_+(u sqrt(M))). A small finite difference between strict and non-strict t0<=2s is immaterial; the exact bound is t0<2s for this M range.

To show the source profile survives, note e>=1/M, so f_e(v)<=f_(1/M)(v)=v[1+ln(1+1/v)]. The function is increasing and subadditive. If epsilon<=A s and chi>=m, then epsilon^2<=A^2/M and epsilon/chi<=A/(m sqrt(M)). For fixed A>0:

* f_(1/M)(A^2/M)=O_A(s), since (1+ln M)/sqrt(M) is bounded on M>=64, with larger v handled directly.
* f_(1/M)(A/(m sqrt(M)))=O_A(s), since ln(1+m sqrt(M)/A)<=ln(1+1/A)+ln m+(ln M)/2, and ln m<=m, ln M<=m ln2.

The inequality in the second bullet uses m sqrt(M)>=1, so 1+m sqrt(M)/A <=(1+1/A)m sqrt(M). Therefore

    s+epsilon+f_e(tau) <= C_A[s+f_e(k/M)],

and capping is equivalent up to constants to H_edit. The lower RE2 uses SC002 for K>=3 and BT002 with SC003's matching upper for K=2. Those lower witnesses apply to the ENTIRE corrupted word and preserve the same terminal pair, with hidden seed/mask and common source-independent corruption kernels. A finite encoded observation can be simulated from that full word under zero port noise; fixed public budgets do not invalidate the lower. More precision or deeper encoding cannot restore information erased BEFORE encoding.

For delta=c/Q with fixed c>=0 and rho=ceil(c)/Q, u=(ceil(c)+2)/Q. A sufficient dyadic schedule has Q=Theta_(R,c)(M^(1/(2R))), epsilon=O_(R)(s), chi=Theta(log M), and d=O_(R,c)(log M). Thus the full statistical/source profile can be attained behind a genuinely noisy coarse-Q cut. The fixed uniform histogram prefix of JP001 instead has the additional precision/noise contribution f_e(delta+1/Q). That lower is architecture-specific and cannot be applied to this redesigned compander/packing encoder. The deep construction uses RK^3 rather than K^3 cut coordinates, a fixed R-fold width expansion, and a paid decoder: this comparison is not a theorem that depth alone at identical coordinate count removes every obstruction.

No all-Q sharp-depth frontier, necessary scalar exponent R, optimized output-dimensional capacity law, sharp growing-K dependence, efficient decoder or internal-fault theorem follows. The inherited universal label-count lower involves D=RK^3, not R, so their gap remains. We do not transplant JP001's fixed-uniform coarsening lower into a different representation.

## 7. Complete finite realization and conservative resource ledger

Reliable post-cut computation uses only labels, S and public metadata. GN001 supplies an explicit rational table of E_R=O_R(N^(R-1)) moving segments, E_R=1 for scalar fallback. Generate it recursively, retaining O_R(log N) numerator/denominator lengths per endpoint. Enumerate all segments, project by rational coordinate clamp, compare squared distances by exact integer cross products, resolve ties publicly, and invert the chosen affine segment. This is polynomial-table enumeration, NOT a logarithmic-time decoder. Enumerate g_L's L+2 rational breakpoints and scan/invert its L+1 affine pieces with a fixed tie rule. All inverse coordinates have O_R(h+log N+L) rational lengths. The sum/normalization of fixed K such coordinates has O_(K,R)(h+log N+L+log(M+1)) bitlength; a common denominator may be a product, so there is no K-uniform length claim.

The binary confidence computation is exact finite integer arithmetic specified in §5; it uses public k, epsilon,chi and the decoded row mass, not a clean statistic. If b covers full rational input lengths, the root-grid exponent p=O(b), squared comparison operands have O(b) bits and binary search uses O(b) comparisons: conservatively O(b^3) work and O(b^2) scratch per token, plus O(b^4) separately compiled finite control. These extra terms are explicitly added below. Full numerator/denominator descriptions are used for rho, epsilon and all budget certificates. If the automatic schedule in §6 is executed, also read and charge its full target description b_t0; otherwise N is directly specified and set b_t0=0. Setup scale-selection comparisons/doublings operate on these guarded words and are included in public generation work. The statistical target has b_t0=O(log(M+1)), but an arbitrary target is not assumed short. Let n=M+3, ell=ceil(log2(n+K+2)); use conservative fully expanded public record/mask counts

    U=O_(K,R)(d n^2),  F=O_(K,R)(d n^2+n ell),
    Bp=O_(K,R)(h+log N+L+ell+b_rho+b_t0+1),
    w=C_(K,R)[P+Bp+ell+log(d+1)+log(P+1)+log(U+F+2)+1],
    b=C'_(K,R)[h+log N+L+ell+b_rho+b_t0+1].

Here w is the guarded encoder/machine word bound, b is decoder rational word bound, and h+1 is the distinct cut-label length (endpoint Q included). Bp safely overcounts public budgets alongside actual coefficients. Working conversion uses exact signed quotient and costs O((Bp+P)^2) bit operations per supplied numerical record, with O(Bp+P) scratch. A safe overcounting Boolean arithmetic instruction ledger is

    T0=O_(K,R)(d n^2(P+1)w^2+(U+F+E_R+n+(L+1)^2)w^2+w^4
              +U(Bp+P)^2+nK^3[E_R+(L+1)^2+1]b^2
              +nK^3R(w+b)+n b^3+b^4),
    S0=O_(K,R)(UBp+UP+F+nK^3w+w^4+Bp+P
              +K^3E_R b+nK^3b+(L+1)b+b^2+b^4).

All terms count actual tokens/layers, radius-three acquisition, dense QKV/affine zero slots, excluded mask edges, dummy heads, Taylor steps, signed full products, guarded count accumulation, parameter conversion/generation and public scans. Final exact pre-fault clips, all intermediate rails and writes are included in d and fixed constants. Public rational table generation fits the displayed E_R and L^2 work; chosen generator program and actual scratch are included. The edit/noise adversary is an external channel, not a free reliable simulation gadget the implementation claims to execute.

At handoff read each O(w)-bit pre-cut bank word, emit its h+1-bit attacked/clipped/floored label supplied by the channel, and form the O(b)-bit decoder representation. Charge O(nK^3R(w+b)) conversion/reading/writing work and simultaneous old/new-bank storage. Do not identify w, b and h. Cut isolation disables all nonexported source-dependent tapes before any decoder access; zeroing/cleanup writes, if chosen, are paid. Historical-token outputs cannot feed the terminal decoder. The n factor conservatively pays all-token decoding if required by batch syntax, not an assumed free terminal-only exception. Source-independent parameter/certificate acquisition and output serialization are charged. If decoder output is rounded onto a separate grid Q_out, add <=K/Q_out TV and its exact divisions/serialization; setting Q_out=Q silently would generally destroy the benefit.

For an explicit non-unit-cost addressed sequential realization, let v=C max(w,b,Bp). Store O(T0 v) instruction/address bits and scan the S0-bit data tape per bounded-arity bit instruction. Safe online bitwork is O(T0 S0 v), peak O(T0 v+S0) plus actual chosen-generator scratch; safe offline work is O((T0+S0)v^2) with actual phase sums. These loose bounds suffice to remove a unit-cost real/RAM oracle. A separate Boolean/ReLU PURE unrolling pays its actual larger depth, width, sparse/dense held slots and generation costs; primitive depth (11) is not PURE or bit-machine depth. No lower or practical optimality is asserted for these resources.

## 8. Dependencies and preserved nonclaims

Direct mathematical dependencies: accepted MG001/MG002, GD001 upper and uniform-FA extension, GN001 pointwise no-plateau geometry and rational-description extension, MG final-pre-fault-clip clarification and its independent review, JP001 continuous real-A occupation completion, SC002, SC003 and BT002 (including its finite-domain scalar completion). The stage8 companion is read only for exact statistical-model and scope alignment; it is unchanged. Source/review/receipt hashes are recorded in RE001_source_bindings.json. Dependency receipts are verified separately. The new steps are (6), the binary data-radius lemma, their composition with the noisy finite cut, and the explicit finite-scale schedule.

No clean-history bypass, iid-conditioned-row argument, q-to-unit-cap replacement in the binary logarithm, hidden support/minority test, source-dependent budget certificate, coarse-Q output rounding, zero-purity assertion after signed faults, off-support minorization omission, uncharged final clip, or free post-cut arithmetic is used. No publication/contact, training, novelty, external peer-review or formal-verification claim is made.
