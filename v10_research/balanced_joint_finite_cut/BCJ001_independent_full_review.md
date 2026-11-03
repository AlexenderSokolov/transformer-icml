# BCJ001 — fresh independent full mathematical and paid-interface review

2026-11-02. **PASS for the exact frozen candidate and its stated scope; root acceptance remains separate.** Reviewer is an independent LLM reviewer, separate from the author. This is not formal verification, external peer review, or novelty certification. No proof or acceptance receipt was modified by this review.

Reviewed theorem SHA256: `95d5aac1ee2504955e55c1e82241c8a07d219661e2620c6e083acf5c8701554d`.

## Findings first

No blocking mathematical, interface, or paid-resource defect was found. The fixed twelve-coordinate encoder and single deterministic budget-blind decoder support both displayed upper bounds and the stated fixed-prefix lower. On each fixed nonempty band beta>=c/M, they establish the claimed capped maximum order for stationary and arbitrary starts. Below that band only the displayed bracket is established. The lower is not validly transferable to optimized encoders, and the candidate does not make that transfer.

The important changes from previously accepted eight-coordinate work were reviewed afresh: the extra first-half information changes the encoder class, so JP001's precision lower is not automatically inherited; the twelve-coordinate IID tube proof supplies a new complete-bank lower. Likewise the gate now receives independently perturbed real pseudo-counts, not counts of any common word. Its deterministic proof uses only nonnegativity and selected-row numerator<=denominator, not a consistency relation between the two banks.

## Read scope and dependency checks

Read the entire frozen BCJ001 theorem, source-binding manifest and author diagnostic source. Read CB004, BP001 and CB005 in full, together with JP001, JB001, FA001 v3, SM002 and BT002 main/scalar proofs and their acceptance receipts. Existing inherited results were checked for exact interfaces rather than presumed from titles. Independent diagnostics verified all eight listed proof hashes and acceptance-receipt hashes against the manifest and their root-accepted statuses; the receipt's own proof hash must agree. BT002's separately bound scalar component hash was also verified. The accompanying review-bindings file freezes the actual reviewed sources and artifacts.

CB004 explicitly supplies arbitrary-start inverse occupation and clean comparator/tail interfaces, although its final theorem is stationary. BP001 supplies only stationary weighted imbalance. CB005's accepted receipt specifically supplies the all-start version, including unsupported singleton starts; its proof does not replace arbitrary-start analysis with stationary reversal. BCJ001 uses CB005 only for that weighted clean bias. BT002 main §1 and its acceptance receipt both explicitly state the **uncapped** `2^-54 max{s,F}` lower; equation (6.3) has not strengthened a capped statement by mistake.

## Model and twelve-coordinate encoder

The first source attack preserves positions M+1,M+2 and may edit at most k earlier symbols. The second attack is one vector operation with an infinity bound, not one changed scalar. Its order is actual finite bank, additive noise, clipping, final Q-floor. Both stages have the stated source-information exclusions; upper bounds are pathwise and do not need independence between attacks or errors.

At departure j the key j+3 has the trailing triple and a first-half row indicator. The latter tests public j<n; it does not inspect later symbols or derive a hidden statistical mask. A paid local table with per-position entries is a valid implementation. The last four values are L_u/M, not L_u/n: all twelve values go through the same uniform head and the same M keys. The protected terminal pair selects the same clean row after editing. Public half-position bits do not survive as additional statistical observations; their format is fixed independently of the source.

Zero Q/K maps yield equal finite scores. The positive Taylor recurrence always has W>=D from its initial term, even for P=h. Thus Z=MW and N_i=W D A_i, and a full-width integer quotient gives floor(D A_i/M)/D exactly. This is cancellation inside an explicitly specified integer evaluator, not a substituted ideal softmax or FA001 approximation premise. Exact copy/identity maps preserve the grid. With Q dividing D, noiseless nested flooring gives the stated Q-count labels. Clipping is 1-Lipschitz around each true corrupted frequency. Equation (2.2) correctly pays internal floor, real noise, clipping and final floor in that order.

## Gate and deterministic perturbation reduction

One changed symbol affects at most three triple windows. Each replacement changes a histogram by l1 at most two, giving 6k. A selected first-half pair coordinate changes by at most 2k; the common looser 6k is safe at split and endpoint boundaries as well. Two triple labels contribute at most 2M(delta+2/Q) error to the selected row sum. Hence the real d in (3.1) simultaneously bounds C,J,J1 errors and is <=6M tau.

The noisy labels are nonnegative, so C'<=J'. This is the only within-row consistency needed to make the output a probability. No premise J1'<=J', sum of labels=1, or integral pseudo-counts is used. In particular J' may exceed M without invalidating the proof.

On an active truly balanced positive row, the two ratio cases J>=2d and J<2d prove (3.3), using the integer clean J>=1 to replace J with J+1. At d=0 empirical ratios coincide. On active H-complement, J1<J/1024 and the noisy gate imply J<1026d. On rejection outside B, a zero noisy denominator implies J<=d; otherwise the strict gate failure implies J<513d. Rejection on B costs exactly q. J=0 and false statuses are safely paid by the two enlarged tails in (3.4), including real d arbitrarily close to zero. These arguments are deterministic and uniform over all admissible attack histories.

For real t>=1, the integer event J<t is contained in J<ceil(t). Applying the inherited integer-threshold inequality with two ceilings gives a sum at most 16(1539d+4)/(M+1). The +4 genuinely covers fractional thresholds; no integer-radius shortcut is used. The inverse term and tails yield 8*130944+16*1539=1072176. After d<=6M tau, 6433056<2^23. The clean comparator plus 64/(M+1) is bounded by 2^16/sqrt(M) throughout M>=64. For M<128 the displayed capped theorem is trivial, so the suffix lemma's horizon restriction is respected. BP001 or CB005 then yields exactly the respective displayed bias constants.

## Fresh complete-message precision lower

All-row Bernoulli(p) sources with stationary product initialization have P_source^2(i,j)=Pi(j) for every pair, so they qualify for each advertised beta<=1. The next-symbol parameter is p regardless of endpoint; arbitrary simplex output has binary TV exactly its probability-of-one error. No terminal-conditioned IID sample assertion is needed.

The eight triple variances sum to at most 10/M. Four half-row subfrequency variances sum to at most 3/(2M). Thus total <=23/(2M), and Chebyshev/union gives probability >=0.9 at tolerance 1/Q when M>=120Q^2. Pair overlap radius one, triple radius two and denominator M have been accounted for. Each mean-curve coordinate has derivative magnitude <=3, including the n/M factor for half rows.

A mesh spacing at most 1/(3Q) needs at most 2Q points. On the good event, each raw frequency lies within 2/Q of one mesh mean, hence its floored integer label is within 3 of the scaled mean, allowing at most seven integers. Twelve coordinates and four endpoint values give at most 8Q7^12 **complete messages in a single parameter-independent set**. This is not a bound on just one selected row and not a multiplication of O(Q) alphabet sizes across each coordinate globally.

Fixing a source-independent decoder seed leaves at most R real estimates on good messages. Prior mass in radius 1/(16R) neighborhoods is <=1/4, whereas the joint good-event probability is >=0.9. Their difference gives expected absolute error >=1/(32R). This remains valid when the good event depends on p and the channel is stochastic; no uniform conditional posterior is asserted. Averaging seeds and taking a source supremum are legitimate. The resulting constant is exactly 1/(256*7^12 Q).

For M<120Q^2 the entire IID history can be granted. The stated two Bernoulli parameters have product chi-square <=exp(1/12)-1<=1/11, giving TV<1/4 and the stated conservative two-point risk. N=M+2<122Q^2 suffices. This fills the complementary domain without extrapolating the tube and also checks a statistical floor. This review does not import SM002's different master interface; only the elementary good-message mechanism has been re-proved for this twelve-coordinate cut.

## Noise and source lower witnesses; rate comparison

The dyadic Q_c construction divides both Q and D and meets its perturbation budget. Coarsening all twelve coordinates once is a legal source-independent vector attack. Exact nested floors reproduce the same twelve-port encoder at Q_c, including the half coordinates. The alternate fine-Q-grid shifts leave a residual in [0,1/Q) and stay in [0,1], so clipping is inert. The factor-four comparison with delta covers both sides of delta=1/16; when delta<1/Q the noiseless floor dominates.

A full corrupted history simulates this exact finite encoder, its protected pair, and public metadata. Thus BT002's protected-source-corruption lower survives the restriction to the twelve labels. Public budgets fixed throughout a witness prior do not reveal the unknown parameter. Different worst sources may prove the IID and corruption bounds; taking their maximum is valid and summing their risks is unnecessary. Stationary witnesses also lower-bound the arbitrary-start minimax problem.

On beta>=c/M the bias term is <=s/sqrt(c), and f_e(k/M)<=k/M+s/sqrt(c). Together with f_e(k/M)>=k/M the displayed upper and lower imply the claimed Theta_c capped maximum. The map itself never changes with k,delta,beta. This is genuinely simultaneous attainment, not a family of informed decoders chosen separately for each budget.

## Paid realization and isolation

The ledger is a conservative finite sequential multitape implementation, not a fixed-depth neural claim. FA001 permits position-dependent finite local tables, bounded 0/1 entries and the given dense public causal masks. BCJ001 explicitly charges twelve indicator projections, dense zero Q/K slots, all-token work, padding, synthetic query, masks, indices/position counters and protected endpoint acquisition. Generating j<n by counters or reading an explicit per-position table costs at most the declared public generation and forward allowances. No free half-position head is needed.

U=O(N^2), F=O(N^2+N ell) cover explicit numerical records and public masks/metadata. Numerical scalar description b=O(1) does not erase index costs: ordered layouts have implicit sequential indices, while counters/metadata are paid in ell, F and w. Compact converted public records require P+O(1) bits; arithmetic/hidden-state words separately require full w bits, including integer range, full products, log M accumulation guards, Taylor divisors, remainders and addresses. The statement does not identify h or P fractional bits with total word width.

The explicit construction work includes w^4 arithmetic-template generation plus full table conversion/copying. Forward work O(N^2(P+1)w^2) includes all candidate mask tests, Taylor steps, sequential scans and rewinds; common weights are not used as an unpaid shortcut. Stored microcode is not rescanned in full per operation. Retained descriptions, converted records, metadata, arrays and controller scratch appear in the simultaneous peak sum.

After the cut, row selection among twelve labels is fixed finite scanning/muxing. M cancels from both the gate and ratio, so integer label numerators need only O(h+ell+1) full bits. Multiplication by 512 is a fixed shift, zero-test/addition are exact, and numerator<=denominator gives nonnegative complementary output. Unreduced rational serialization avoids hidden real division or gcd costs. The O(v^2) terminal work and separate O(v^4) template allowance are conservative. Optional all-token output and Q-rounding are separately charged. Dead input/history/QKV/accumulator/nonexported output tapes are disabled at handoff with copying/clearing costs retained. This is an abstract access contract, not a free physical security/noise gadget.

## Independent checks and final scope

`BCJ001_independent_checks.py` passed 8,800 boundary-enriched rational gate cases, including 1,006 with half pseudo-count above total pseudo-count; 37,980 exact positive-Taylor/full-quotient/nested-floor/coarsening cases; fractional ceiling checks; explicit coefficient and mesh inequalities; and eight dependency receipt/hash checks. The tests deliberately include tiny real radii and rows around 256,512,1024 to exercise gate boundaries. Finite diagnostics support, but do not replace, the preceding proof review.

**Verdict:** eligible for root acceptance as a fixed twelve-coordinate paid finite-cut, all-budget unknown-k/delta/beta result on every fixed beta>=c/M band, with the stated stationary/all-start bracket elsewhere. No claim about redesigned encoders, optimal computational resources, fixed neural depth, training, practical constants, physical reliability, external priority or formal verification follows.
