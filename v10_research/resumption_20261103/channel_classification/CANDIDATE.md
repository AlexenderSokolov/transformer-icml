# Fixed binary-input finite-output channels: candidate four-way classification

2026-11-03. Local author derivation, not root accepted, not published. The equal-support necessity is explicitly CONDITIONAL on acceptance of the new finite-likelihood-ratio lower-bound argument in `../bsc_sharp/CHANNEL_LIKELIHOOD_LOWER.md`. Nothing here retroactively accepts that argument. Other cases use accepted FOT002/FOT003 plus elementary channel reductions.

## 1. Common experiment and exact scope

Use the original first-order v10 experiment: raw word X_0,...,X_(M+1), eight exact triple counts, actual protected terminal pair, arbitrary initial PAIR law, hidden first-order table, strict source-independent offline attack editing at most k of the first M positions, k=0,...,M. The supplied all-state pair certificate is beta=1/M if the restricted class is chosen. Loss is unconditional unsquared TV for the actual terminal target. The initial pair can also be given: FOT003 makes it exactly reconstructible from these counts and terminal pair. No larger raw windows are given.

One rule is used for all tables, initial laws, budgets, and kernels at fixed M. After corruption, an arbitrary law-independent encoder scans the full corrupted word and emits H in {0,1}^R. R is fixed in advance. The receiver observes the noiseless baseline Z and the entire channel output V in Y^R. The finite alphabet Y and binary-input stochastic matrix W(y|b) are fixed independently of M and known to both sides. Conditional on the complete pre-channel experiment the channel is fresh memoryless W^R. The encoder may have private coins; the receiver may have private coins. Shared coins are allowed only as independent free baseline randomization. No path-dependent seed revelation, feedback, timing, variable/adaptive lengths, channel-aware attack, or other free side information is allowed. R counts physical binary channel inputs, not output symbols or alphabet logarithms.

Let Gamma_W(M,R) be infimum over such rules of supremum risk/g_M(k), where g_M(k)=max(M^(-1/2),k/M). Infimum follows the joint supremum. Define ell_M=1+ln((M+2)/2). Accepted inputs, for M>=64, are

    c0 ell_M <= Gamma_0(M) <= C0 ell_M,
    c0=2^(-33), C0=2^17;
    exact gate risk <= 1024 M^(-1/2)+2^20 k/M;
    Cg=1024+2^20;
    full-history normalized floor cf=1/96.

The last bound applies to ANY randomized full-history procedure, hence to any composite encoder-channel-decoder rule. It does not rely on the false assertion that an arbitrary R-bit message is less informative than the particular historical one-bit gate. Lower witnesses are stationary certificate-valid sources, while uppers cover arbitrary initial pairs and all first-order tables. Thus both source-class conventions give the conclusions below.

“Constant-factor length order” means: some finite constant B independent of M can be achieved for all sufficiently large M, and every uniformly bounded sequence of factors has the claimed necessary order. No sufficiency for arbitrary B below the intrinsic floor is asserted. For example our upper constructions attain B=Cg+1 after sufficiently many transmissions.

## 2. Classification

Remove symbols with W(y|0)=W(y|1)=0, and put S_b={y:W(y|b)>0}. Nonempty supports remain. Define

    lambda=sum_y min(W(y|0),W(y|1)).

The following four cases are exhaustive and disjoint:

1. **Identical rows:** W(.|0)=W(.|1). Then Gamma_W(M,R)=Gamma_0(M) for every finite R (even R depending on M). No length schedule gives constant adaptation.
2. **Disjoint supports:** S_0 intersect S_1 is empty. One physical input transmits a bit with zero error; R=1 suffices and R=0 does not suffice asymptotically. The minimum constant-adaptation length is one.
3. **Unequal but overlapping supports:** S_0 != S_1 and S_0 intersect S_1 is nonempty. Then 0<lambda<1 and the constant-adaptation length order is Theta_W(log log M).
4. **Equal supports, distinct rows:** S_0=S_1 and W(.|0)!=W(.|1). Then the constant-adaptation length order is Theta_W(log M), CONDITIONAL for necessity on the pending finite-likelihood lemma. Sufficiency is unconditional relative to accepted exact gate.

Constants may depend on the fixed W. These are order statements, not sharp leading constants. In case 3 we do not claim matching Gamma(M,R) exponents or an exact risk curve for arbitrary W.

## 3. Universal common-component lower, including all encoder randomization

For one use let m(y)=min_b W(y|b). For R uses define m_R(v)=product_i m(v_i), whose mass is lambda^R. Every codeword channel law dominates m_R pointwise. Therefore for every word w, baseline z, and private encoder input mixture, the resulting output law P_w also dominates m_R. For R=0 use the single empty transcript of mass one, including when lambda=0.

If lambda>0 let q_R=m_R/lambda^R. For an arbitrary fixed encoder/decoder procedure, construct a baseline-only decoder D0: draw V from q_R independently and run the same receiver D(Z,V). If there is shared seed U, draw the baseline's same free U, then draw V independently of it. Pointwise in the pre-channel variables and U, nonnegative conditional loss gives

    risk_i(E,D) >= lambda^R risk_i(D0)

for every instance i=(k,table,initial law,kernel). Thus

    sup_i risk_i(E,D)/g_i >= lambda^R Gamma_0(M),
    Gamma_W(M,R) >= max{cf, lambda^R c0 ell_M}.       (1)

The artificial common-component event need not be observable to the receiver. The construction does not choose a law-dependent encoder or kernel. When lambda=0,R>0 the overlap contribution is simply zero. In particular the baseline and full-history bounds combine as a maximum, not an unjustified sum. A sum form is possible after a factor-two weakening.

If Gamma_W(M,R)<=B and 0<lambda<1, necessarily

    R >= ln(c0 ell_M/B)/ln(1/lambda)                  (2)

whenever the numerator is positive. This is Omega_W(log log M). It applies to arbitrary codes, not just repeated gate bits.

## 4. Identical rows and disjoint supports

Identical rows make V independent of the input, entire pre-channel experiment, and independent shared seed. A baseline-only randomized receiver can sample V itself and run D. Conversely the channel can be ignored. This proves exact equality to Gamma_0, not just an overlap bound. Arbitrarily large finite lengths do not help.

For disjoint supports, send the historical exact gate G(w) in one input and decode b according to the support containing the output. Every positive-probability output lies in exactly one support. Outputs outside both may receive any fallback. This yields factor <=Cg. R=0 is exactly the baseline with diverging lower bound c0 ell_M. This proves the asymptotic minimum one, without claiming every desired target B can be reached by one bit.

## 5. Unequal overlapping supports: exact detectable-erasure simulation

At least one support difference is nonempty. Relabel inputs if necessary so E=S_1\S_0 is nonempty. Then

    W(E|0)=0, p=W(E|1)>0.

Overlap implies p<1, since row 1 places positive mass on an element of S_0 intersect S_1. This covers strict support inclusion as well as incomparable supports; exclusive events in both directions are unnecessary.

Encode gate 0 by (0,1), gate 1 by (1,0), using TWO physical channel inputs. Inspect each output only for membership in E. If E occurs at the second position, output gate 0; if at the first, output gate 1; if neither, output erasure. Both positions cannot report E with positive probability: exactly one input is 1 and the other is 0. An arbitrary fallback can be fixed on that null event.

For either gate value, the input-1 position triggers E with probability p; the input-0 position never does. Thus the decoded channel has the EXACT conditional probabilities

    P(decoded=gate | complete pre-channel state)=p,
    P(decoded=erasure | complete pre-channel state)=1-p,
    P(decoded=wrong gate | complete pre-channel state)=0.

Hence the failure indicator is independent of the full pre-channel state (including the gate, path, source and attack); this independence is stronger than merely a small average bit error. Repeat n disjoint two-input blocks using the same gate. Fresh memoryless noise makes decoded blocks independent conditional on the pre-channel state; their all-erased probability is epsilon^n, epsilon=1-p in (0,1), again independent of that state. On at least one successful block the exact gate is known, and all successes agree.

The receiver deliberately discards any other information in the outputs. On success run the accepted exact-gate estimator; on all-erased failure run the accepted baseline estimator. With n=floor(R/2), pad any remaining input with fixed zero and ignore its output. Nonnegativity and independence give

    Gamma_W(M,R) <= (1-epsilon^n) Cg + epsilon^n C0 ell_M
                 <= Cg + epsilon^floor(R/2) C0 ell_M. (3)

This remains a valid relaxed bound for n=0. To attain Cg+1 it suffices that

    n >= max{0, ceil(ln(C0 ell_M)/ln(1/epsilon))}, R=2n.

Together with (2), this proves Theta_W(log log M). The raw output process need not be equivalent to a BEC: the explicitly coarsened decoded output IS a BEC, which is enough for the upper. It would be an error to assert full transcript equivalence for a general channel.

## 6. Equal supports: likelihood necessity and testing sufficiency

### 6.1 Conditional necessity

Finiteness and common support imply

    kappa=max_(y in S_0) max{W(y|0)/W(y|1),W(y|1)/W(y|0)} < infinity.

Distinct rows imply kappa>1. For every codeword pair h,h' and every output v in the common product support,

    W^R(v|h) <= kappa^R W^R(v|h').

Outside that support both sides vanish. Integrating any two unrelated input distributions preserves the inequality. This includes randomized encoders conditioned on arbitrary common independent seed. Thus the precise channel comparison required in Sections 2–5 of the pending likelihood note holds, with its block likelihood factor replaced by kappa^R.

For clarity, that comparison feeds the same legally predeclared FOT001 mixture attack: at a clean proposal y and relocation w having identical Z and terminal pair 00, if ell_a(y) is the rule's clean-target loss and b_a(y) its relocated null-target loss, the pointwise TV triangle inequality and likelihood comparison give

    b_a(y) >= a-beta-kappa^R ell_a(y).

Only the clean loss pays the likelihood factor. The attack does not depend on the encoder, decoder, their coins, or the channel outputs. Transport actual nonnegative null loss first, then apply this signed inequality. The pending note obtains, with N=M+1, k=ceil(N^(3/4)), N>=2^160,

    kappa^R <= N^(1/8)
        => Gamma_W(M,R) >= 2^(-32) ln(M+1).          (4)

This document checks the channel substitution, but treats the mixture lemma/transport underlying (4) as a pending dependency, NOT an accepted new premise. Subject to its acceptance, a uniformly bounded factor forces, for all sufficiently large M,

    R > ln(M+1)/(8 ln kappa),                       (5)

giving Omega_W(log M) against every admissible fixed-length code. The bound cannot be exported to unequal-support channels: their relevant likelihood ratios are infinite.

### 6.2 Sufficiency with a worst-case, not merely Bayes-average, error bound

Put h=sum_y sqrt(W(y|0)W(y|1)). By Cauchy–Schwarz, h<=1, and equality would force identical probability rows. Common support gives h>0. Therefore 0<h<1 here.

Repeat the historical gate R times. Write P_b(v)=product_i W(v_i|b), and decode 0 when P_0(v)>=P_1(v), otherwise 1. Ties are assigned to 0 just to make a definite rule. Then

    P_0(error)=sum_(P_1>P_0) P_0(v) <= sum_v sqrt(P_0(v)P_1(v))=h^R,
    P_1(error)=sum_(P_0>=P_1) P_1(v) <= sum_v sqrt(P_0(v)P_1(v))=h^R.

Each inequality holds separately, so no unjustified conversion from average error to maximum conditional error is made. Conditional on every corrupted word, the gate-decoding error is at most h^R. Couple the decoded-gate and exact-gate receivers using the same receiver randomness. They coincide on correct decoding; TV loss lies in [0,1]. Thus for every instance

    risk_noisy <= risk_exact + h^R,
    Gamma_W(M,R) <= Cg + sqrt(M) h^R.                (6)

It suffices to take R>=ceil(ln(sqrt(M))/[-ln h]) to attain Cg+1. This is O_W(log M), establishing the matching conditional order. The argument is also a generic O(log M) upper whenever the rows are distinct, but the erasure simulation is sharper in case 3.

## 7. Why the partition matters, and excluded generalizations

Positive overlap alone supplies only the common-component Omega(log log M) lower. It does NOT characterize silent-noise difficulty. Equal finite supports additionally give a bounded all-input likelihood ratio, allowing the stronger pending v10 transport bound. Unequal supports furnish a detectable event; complementary two-slot coding balances its probability between gate values and supplies a known-failure branch. Disjoint supports give exact decoding in one use. Identical rows carry no information.

The conclusions concern physical use complexity with noiseless observed outputs/flags. They do not include general input alphabets, infinite output alphabets (equal support need not bound ratios), M-dependent channels (constants can diverge), variable/adaptive-length or feedback protocols, correlated channel noise, approximate counts, additional windows, source-specific encoders, or second-order source classes. “Known fixed channel” does not mean the encoder knows the source table. An arbitrary seed conveying path-dependent information is excluded.

## 8. Dependency and review ledger

- **Accepted FOT002:** `../recovered_science/first_order_positional_probe/triple_access/FOT002_matched_original_experiment.md`; receipt `../recovered_science/intake/FOT002_root_acceptance.json`. Supplies baseline sandwich, exact-gate risk, and full-history IID floor. The proof discards X0 and handles arbitrary initial PAIR laws by conditional fixed-prefix kernels; no homogeneous initial edge is assumed here.
- **Accepted FOT003:** `../recovered_science/first_order_positional_probe/triple_access/BOUNDARY_RECONSTRUCTION_NOTE.md`; receipt `../recovered_science/intake/FOT003_root_acceptance.json`. Supplies exact initial-pair reconstruction and suffix counts as triple in-degrees. Separate initial pair is informationally redundant.
- **Pending likelihood lower:** `../bsc_sharp/CHANNEL_LIKELIHOOD_LOWER.md`, especially Sections 2–6, importing accepted FOT001 structural mixture. Only case 4 necessity, (4), (5), and the full four-case sharp classification depend on its acceptance. No pending BSC review is represented as accepted.
- **Earlier erasure comparison:** `../noisy_gate/VISIBLE_ERASURE_COMPARISON_v2.md`. Read as methodological context; Sections 3 and 5 above give the common-component and switching arguments directly, without importing a false arbitrary-code versus one-gate information ordering.
- **New in this note:** exhaustive support partition; general randomized-code minorizer proof; single-sided exclusive-event balanced two-use BEC simulation; separate conditional-error Bhattacharyya calculation; explicit finite-support likelihood substitution and dependency separation.
- **Status:** author derivation only. Needs independent adversarial review of quantifiers, boundary support cases, shared coins and scope, plus independent/root disposition of the likelihood lower. No formal verification, novelty claim, manuscript edits, commits, uploads, or public publication.
