# FOC001 independent logical-interface audit

2026-11-02. Reviewer: an independent LLM reviewer, separate from the proof author. **Initial verdict: REVISION REQUIRED for the common experiment's arbitrary-pair initialization interface.** This is not rejection of the proposed order contrast: a direct suffix repair preserves its constant. Root acceptance remains separate.

## Read scope and binding

Read the complete FOC001 candidate, FOU001 `UPPER_CANDIDATE.md`, its complete `upper_review/REVIEW.md`, its acceptance receipt and binding manifest, and complete AB001 proof, full independent review (including its AB002 discussion), and acceptance receipt. Also read FOU001 PLAN and inspected the original manuscript's explicit every-initial-pair-law convention. `initial_bindings.json` binds these source bytes; complete reading is asserted only for the listed full sources above, not the entire ancillary manuscript. Eight actual receipt artifact hashes were independently verified by `checks.py`.

The initial FOC001 candidate SHA256 is `fa34556e7343f3b8337bc7db6f9b7e73c4c6d42a6f9849dbd50464ecba17aa1a`. No candidate, inherited proof, receipt, or manuscript was edited by this reviewer. This review concerns new logical interfaces, not a new reproof or external certification of accepted results.

## 1. Blocking initialization/horizon issue

The original second-order experiment permits an arbitrary initial pair `(X0,X1)`. Restricting its transition table to first order constrains transitions from X1 onward, but does not constrain the first edge X0->X1. FOU001 instead takes an ordinary homogeneous first-order chain X0,...,XN with arbitrary initial *symbol* law, and every edge follows its table.

Consequently the candidate's application at N=M+1 on the complete M+2-symbol word is not justified for the original all-pair-start quantifier. For example, choose the identity first-order table and initial pair 01 deterministically. The original process is 0111... almost surely; it is not an ordinary first-order path under that table started at X0=0. This is a counterexample to the imported theorem's premise, not a counterexample to the numerical risk claim. The displayed N=M+1 inequalities are correct when all starts instead mean ordinary first-order symbol starts, but that narrower convention is not the full common original experiment claimed.

**Repair preserving the result:** discard X0, and apply the accepted half-gate rule at N=M to the suffix X1,...,X_{M+1}. There are M genuine ordinary transitions. The full corrupted observation can compute its four pair counts, terminal symbol, and exact half-visit bit. Its bound is directly `min(1,1024/sqrt(M)+2^20 k/M)`.

A corruption kernel can depend on discarded X0. To close this point, condition on the clean X0=c. Under each such conditioning, X1 has an arbitrary initial law and its future is the same homogeneous first-order chain. Fixing c in the original kernel and then projecting its output to the suffix yields a legal source-independent strict-k suffix kernel. The kernel may still change its omitted coordinate, but that is irrelevant and can only spend budget; the suffix has at most k changes. The protected original pair implies the suffix terminal symbol is protected (indeed its penultimate symbol is also protected). Apply FOU001 uniformly for each c, then average. The proposed predictor itself never uses c, which is important because corrupted X0 need not equal clean X0. No extra information is delivered to it.

## 2. Attack-class inclusion and budget

Apart from initialization, the original proposed full-word embedding has the correct attack inclusion: original editable coordinates 0,...,M-1 are a subset of FOU's 0,...,N-1 at N=M+1, and protecting a pair is stronger than protecting one symbol. For the repaired suffix at N=M, only suffix coordinates 0,...,M-2 can be edited; this remains a subset of its permitted 0,...,M-1 coordinates. The exact original domain 0<=k<=M implies k<=N in either embedding. Source independence survives the fixed-c reduction described above. Offline/randomized attacks and every-outcome strict budgets are preserved, not replaced by expected budgets.

## 3. Target equivalence and information

Write first-order flip probabilities q0=a and q1=t. At protected final symbol v, a predicted flip p corresponds to predicted symbol-1 probability p for v=0 and 1-p for v=1. The true symbol-1 probability is a or 1-t. Thus binary unsquared TV is exactly |p-qv|. The next-symbol table at actual protected pair (u,v) depends only on v. This gives exact loss equivalence pathwise, including unsupported pairs, deterministic transition boundaries, and arbitrary pair starts; no expectation or conditioning changes the target.

The count/gate algorithm is a deterministic function of the received corrupted word and M. It needs neither k nor beta nor the table, edit mask, clean word, attack seed, or clean omitted coordinate. In a corrected suffix implementation, wording must identify the pair counts as suffix counts, not promise the original full-word histogram alone suffices. An exact computed bit is not a noisy or sampled raw bit.

## 4. H2 comparison and constants

For 0<=k<=M, `g=max(M^-1/2,k/M)<=1`. At k>=1 the logarithm in F2 is nonnegative, giving F2>=k/M for every beta including beta=0. At k=0, F2=0 and H2=M^-1/2. Hence `g<=min(1,max(M^-1/2,F2))=H2`; the cap does not invalidate the inequality because g<=1. The original proposed N=M+1 scaling is arithmetically valid, while the suffix repair needs no shift. Both lead to `(1024+2^20)g<=2^21 H2`. No certificate is used by the rule, so restricting to each qualifying certificate class is legitimate. Reducible/periodic and beta=0 cases are inherited from the accepted FOU001 scope.

## 5. Negative transfer and genuinely second-order family

AB001 uses precisely M+2 symbols, first-M-coordinate strict corruption, protected actual final pair, full corrupted-word observations, unconditional unsquared TV, and the identical H2 profile. Its map is shared across both budget and certificate values. Stationary witnesses suffice to refute both stationary-only and arbitrary-start guarantees. No computational or histogram restriction is imported.

The clean Q_a alternatives are genuinely second order throughout their entire parameter interval, not merely generically. Equality of the last-bit-1 rows would require `r(1-a)/a=1-r`, equivalently a=r. But a>=1/M=2r>r. Both contexts 01 and 11 have positive stationary mass, so this dependence cannot be dismissed as an unsupported-context artifact. The null Q_* is first order, with all-state beta=1/M. Thus the negative result for the class of sources of order at most two uses both the first-order null and genuinely second-order alternatives; it is not a statement about a class excluding all first-order tables. The candidate naturally uses this usual at-most-two interpretation.

Under a hypothetical universal C guarantee, the clean beta=0,k=0 risks obey S_M<=C/sqrt(M). Choosing k=floor(M^(3/4)) gives k<=floor(M/8) eventually; the AB001 clean penalty is negligible relative to the positive term. The attacked null has H2<=2k/M for large M. Their risk/profile ratio grows logarithmically. No finite onset uniform in C is asserted. These are the accepted AB001 quantifiers, and the interface does not strengthen them.

## 6. Non-transfer boundaries

The candidate correctly disclaims a beta-informed obstruction: clean alternatives and attacked null use distinct certificates, and a beta-indexed algorithm may change maps. It correctly disclaims unknown-order estimation and any exact source-specific minimax interpretation of H2. It does not infer a neural advantage, novel lower proof, minimal gate alphabet, positive-certificate phase diagram, or noisy-message guarantee. The local-count scientific-use bullet is contextual, not a new result established by this interface audit; no additional local-count theorem was re-audited here.

## 7. Supplemental checks

`checks.py` independently executed with `checks_output.json`: 21,840 exhaustive small protected-pair/suffix-attack embeddings; 256 exact rational target-orientation cases; 12 exact rational Q_a stationarity/genuine-order samples; 125 separately labeled floating H2 diagnostics; and eight inherited receipt-binding checks. It records the initial-pair counterexample. These tests corroborate, but do not replace, the analytic arguments and do not prove a universal stochastic theorem by enumeration.

**Acceptance recommendation:** do not accept the initial bytes as an arbitrary-pair-start common-experiment corollary. After author repairs initialization/horizon and count-observation wording, the revised bytes need a rebind and targeted reread. The order contrast and 2^21 constant require no stronger inherited theorem.
