# Fresh scientific integration review

Reviewer: delegated `review_richer_count_consolidation_addendum`, 2 November 2026.

## Decision and precise scope

**PASS for the final byte-bound consolidation addendum.** No unresolved mathematical or scope blocker remains. Read the complete final source after author freeze, including the actual three-change wording diff. The reviewer-requested positive-table specialization now explicitly requires both a>0 and t>0 before dividing by either. Root's two neutral-status edits correctly leave mutable review/acceptance disposition to STATUS/receipt. The theorem statements and constants are unchanged.

Final main.tex SHA256: `f5f20b1bce67e3c000d56cde43a9169f79c27d665b085be72ae98368a14b0c31`.
Final PDF SHA256: `8704b536fa4f88d212343142a11272673f2dbcbe7d97bde5da9f2c1dc1efc95b`.

The original first read was of 11pt source; the final source is 10pt with unchanged margins. The author transparently records that the initial eight-page build and 11pt before-file were not retained, and does not fabricate them. The actual retained wording before-file is already 10pt. This layout-only change is not a scientific blocker. This reviewer read the final complete TeX rather than inferring its content from a delta; final PDF visual QA remains the separately reported author/root evidence.

This is review of a consolidation interface and dependency map, not fresh independent proof of every imported stochastic lemma. It is neither a standalone full-proof supplement nor a new theorem branch. Root retains scientific disposition. No formal verification, external peer review, priority certification or publication authorization follows.

## Actual reading and dependency boundary

Read complete main.tex, SOURCE_MAP, SOURCE_VALIDATION, README, STATUS, root selection decision, complete accepted FOU001 and FOT001 proofs and their independent reviews, complete FOT002 interface and its complete review, both actual initial-pair and message-scope repair diffs, all four unit receipts and finite-v2 receipt. Read the natural FOL001 candidate and final rebind as context only. Read the complete WPC001 deterministic relocation, the actual protected-two-symbol IID oracle-floor proof, accepted v2 finite-horizon proof and finite theorem statement, both bounded prior-work audit narratives and their version/read-scope ledger data. The generic positive supplement and full v2 negative proof beyond the IID floor are accepted dependencies, not re-proved or represented as fully reread here. FOU's complete independent review explicitly checked the generic positive proofs and their two-state specialization; its byte-bound acceptance is the dependency used here.

The final ledger has 42 exact dependency hashes. Historical candidate headings do not negate later accepted receipts. FOL's prior-work audit records an earlier candidate hash; the later rebind explicitly preserves and supersedes that historical scope rather than falsely asserting a current-hash audit. These are provenance layers, not conflicting theorem states.

## 1. Common experiment, observation and quantifiers

The source has M+2 symbols, M triple departures, M+1 ordinary edges, and an arbitrary hidden initial PAIR law. T governs transitions only from X1 onwards. Stationary starts are the special pi(a)T(a,b) law, so the stationary class is contained in the arbitrary-pair class. The selected actual terminal pair is protected and its first-order next-law is T(X(M+1),.). Lifting binary predictions to next-pair distributions with fixed first coordinate preserves TV. No independent test query appears.

The strict kernel edits only coordinates 0,...,M-1, on every input and random outcome. It receives a word, not the true source; predictor/attack randomness is independent. For every fixed (M,r), one map serves all integer budgets 0,...,M. Infimum then supremum ordering is explicit, including randomized maps, and neither extremum needs to be attained. The model and known-budget comparison use the same observation and source convention, not mismatched information or a per-budget logarithmic lower claim.

## 2. Upper transfer, initial-pair repair and measurability

The identity-table initial-pair-01 example correctly shows why all M+1 edges cannot be treated as homogeneous. Discarding X0 leaves M actual T transitions. Summing triple counts over their last coordinate counts edges 0,...,M-1; adding the corrupted final pair and subtracting the corrupted initial pair leaves exactly edges 1,...,M. Both pairs are available at r>=2. An edit of Z0 cancels. Counts are nonnegative and sum to M.

For each positive-probability clean X0=b, prepending fixed b, applying K and dropping the first output produces a source-independent suffix kernel on every suffix input. Its budget is at most k and its terminal symbol remains protected; it is in the larger natural upper attack class. The conditional initial suffix law is arbitrary, but all later transitions follow T. Applying one and the same suffix predictor under both b values and averaging is valid by uniformity. The proof does not provide b or any clean input to the predictor.

The available suffix length is r'=min(r,M+1). No claim to recover the truncated prefix is needed; the gate uses only its last m+1 symbols, m=min(r'-1,floor(M/2)). Those reveal m ordinary departures, not r-2 pair departures. Selected J', C', and O' are all measurable. The FOU bound at N'=M is 2^17 ell' gM, with ell'<=ell; r=M+2 gives ell'=ell=1. No extra horizon factor is paid in the upper. Known-k estimators require only reconstructed counts and terminal symbol and give 2^16 gM. Reducible and periodic tables remain covered, with reducible weighted terms handled separately rather than dividing by zero.

## 3. Richer-count lower and constants

The lower is FOT001, not a consequence of the weaker four-count observation. It uses N=M+1 ordinary edges. Its exact fixed-v skeleton retains the stationary factor, includes terminal zero loops, and has H=N-v-u. Integrating the a term gives at most 1/u for u>=1. The residual renewal recursion R0=1, R1=1-t, Rn=(1-t)R(n-1)+tR(n-2) bounds the fixed-v sum by t. On endpoint event 11...00, j=v-1. The null word instead has J00=j-2; the addendum correctly does not identify the null histogram with the alternative/output histogram.

WPC relocation preserves the sampled alternative's eight counts and windows, with frozen endpoint positions restored by equal interior length. Its Hamming bound is 3Jcross+4r-5. The separate ordinary-00 good-event condition and forced-first-edge coupling discrepancy 1+sigma are retained. The kernel makes one predeclared proposal and checks actual Hamming distance and protected final pair, otherwise returning identity on every input. Nonnegative losses are discarded and coefficients reduced before the signed triangle inequality. The lower applies to every fixed randomized map and uses its own clean risk at the same horizon.

At the same budget, gN<=gM<=((M+1)/M)gN. Thus sup R/gM >= M/(M+1) sup R/gN, followed by infimum, giving 2^-33 ell from FOT's 2^-32 ell. Budgets 0,...,N-1 are exactly 0,...,M; the certificate is 1/(N-1)=1/M. All-state lower witnesses lie in the certificate class, whereas the upper needs no certificate. Inclusion proves the stated factor chain for either convention.

## 4. Actual IID floor and exact-oracle normalization

The protected-two-symbol IID proof is independently applicable inside the first-order class: P^2=Pi on every row. Clean testing gives 1/(64 sqrt M), including when identity is admitted at a larger supplied budget. The edit kernel uniformly retains a bucketed number of ones among the M editable symbols. It has a strict per-input k bound, and conditional arrangement is parameter-independent given retained size AND final pair. Four protected labels are counted, not conditioned away. The frozen independent seeds argument gives 1/[32(floor(M/(k+1))+1)]>=k/(96M). Separate minimax witnesses combine to gM/96 even with full corrupted history. Information restriction preserves the lower.

Pointwise g/96<=Roracle<=2^16 g gives 2^-16(R/g)<=R/Roracle<=96(R/g). Suprema and infima preserve these inequalities, yielding 2^-16 Lambda<=D<=96 Lambda and the 2^-49 ell lower. There is no inferred Dstat<=Dall ordering after their different oracle normalizations.

## 5. Width sequences and exact-message scope

Positive liminf rM/M gives bounded eventual logarithms, and bounded loss handles the finitely many smaller horizons. Vanishing liminf gives a divergent subsequence, ruling out a finite uniform factor. Nonmonotonic widths are covered. Fixed alpha is held before taking the horizon limit; ceil(alpha(M+2)) has the stated logarithmic order with absolute constants. No stronger second-order alpha constant is transferred.

The message corollary is explicitly separate, over r=2 only: exact triple counts, BOTH endpoint pairs, and a fault-free message, without growing windows or other channels. The encoder scans the corrupted suffix and computes the half-visit threshold bit. The decoder reconstructs J and C and separately tests J>0. FOU's bound 1024/sqrt M+2^20 k/M transfers by the same conditional-kernel argument. One-symbol alphabet is constant and leaves the r=2 baseline, whose lower factor diverges. Thus the two-symbol minimum is correct only under that baseline. Scanning/counters are uncharged; noisy bits, raw sampled coordinates and bounded-precision implementations are not asserted.

## 6. Certified second-order extension and bounded literature

The extension uses the original M+2/M/protected-pair/eight-count experiment but retains the all-state P^2>=Pi/M assumption for the upper. Accepted v2 constants are 2^-30 ell and 2^20 ell. Neither no-certificate first-order sufficiency nor its message access is transferred to arbitrary second-order tables. Full-history joint budget/certificate adaptation and unknown-order claims are excluded, consistent with root's selected scope.

The addendum accurately inherits rather than enlarges the two local primary-source audits. It distinguishes unsquared-TV risk from HJW's squared-TV discussion and expressly does not resolve the binary squared-loss open question. Generic geometric/confidence selection requires simultaneous valid balls, not merely separate expected risks; a random terminal target alone is not called a barrier. Robust counts in other attack/target models are acknowledged, preventing a broad anti-count assertion. No exhaustive novelty, priority, architecture or performance claim appears. External papers were not re-browsed in this integration review; only fidelity to the supplied audited evidence and its reading limits was assessed.

## 7. Fresh executable corroboration

The fresh checks.py imports no author checker. It passes 4,088 exact corrupted-suffix reconstructions with first-symbol cancellation, 4,088 scan-bit evaluations, 36,864 suffix-window/gate instances, and 123,671 exact rational horizon/oracle-floor cases. It verifies all 42 SOURCE_MAP digests, byte sizes and SOURCE_SHA256SUMS entries. These finite checks corroborate the interfaces; they do not prove all stochastic inequalities or replace the accepted proof dependencies. Build/render QA is a separate author/root gate.

No accepted source or addendum source was edited by this reviewer; writes are confined to this integration-review directory. No external write was performed.

Final closure: independently reran all checks after final freeze (42 source hashes), verified the four direct proof/receipt identities, and applied the actual retained wording diff with zero fuzz to recover final main.tex byte-for-byte. The final source and ledger are consistent. No open recommendations remain.
