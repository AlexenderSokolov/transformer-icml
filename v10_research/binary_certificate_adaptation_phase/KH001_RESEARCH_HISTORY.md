# KH001 research history and preserved limitations

This is a retrospective author history note, not an independently reviewed theorem or a contemporaneous transcript. It records actual routes discussed during the research assignment; it does not claim earlier failed proof files existed.

## Earlier stronger-side route and correction

The initial idea was to restrict useful suffix lengths to order1/beta while keeping the original full histogram. Root correctly warned that this does not make an earlier prefix free. A symmetric first-order null requiring flip rate r>=beta/2 has complete one-flip-word probability `(r/2)(1-r)^M`, exponentially small when M beta grows. Replacing M by1/beta only in the harmonic suffix range would leave this full-word probability loss unpaid. No valid theorem was claimed from that shortcut.

The repair uses an asymmetric stationary first-order null:1->0 rate1/(2M),0->1 rate beta. Its dominant1 state can support the full long waiting prefix while its terminal0 suffix has length O(1/beta). KH001 explicitly retains the prefix power and computes the complete word probability. Its terminal00 target is beta, not the old symmetric-null value1/(2M); the loss gap is paid using a_j>=2beta.

Reversal was introduced to avoid dividing concentration errors by the rare original event probability j/M. It does not remove this rarity from clean-risk accounting. The original-conditioned law is analyzed as a reverse-start00 chain conditioned to end11; this latter endpoint has probability at least1/2. Root flagged the departure-count correction: `J00(reverse)=J00(original)+1`. The proof pays that +1 explicitly, and the author checker exhaustively verifies it. Cross-pair departure counts are unchanged.

## Actual saved proof history

The first saved `KH001_histogram_strong_side_obstruction.md` already contained the asymmetric full-word null, corrected target, reversed conditioning, +1 count correction and strict-distance test. Before the final editorial changes, its ACTUAL bytes were copied to `revisions/KH001_pre_freeze_editorial.md`; they were not reconstructed from a later file. The actual unified diff and before/after hashes are saved beside it.

The three textual changes before freezing were: (i) reviewer-requested enumeration of all three matrix positions represented by `(1-a)a` and `ae=ea`; (ii) updating KA001's now-completed root acceptance status; (iii) correcting 'casual attacker' to 'causal attacker'. No displayed mathematical equation, constant or argument changed in that edit. Later review status is separate.

The same enumeration shorthand in immutable BK002 was handled by a SEPARATE source-bound addendum, not by editing accepted history. The addendum's review/adoption status is separate from KH001.

## Deliberate scope

KH001 uses exactly the triple histogram and initial/final PAIRS. Canonicalization does not preserve general boundary triples or fixed larger symbol windows, and no extension to those interfaces is silently made. Full-history procedures can see the atypical ordering of canonicalized words. No full-history positive result or impossibility follows from KH001 alone.

The fixed kernel may depend on public beta through hardcoded table entries. It is one source-independent map at that fixed public problem, not one map uniform over beta. It does not query hidden source parameters or unseen clean symbols. General real beta is allowed because the experiment permits unrestricted stochastic kernels on a finite set; no rational implementation or efficient sampler is claimed.

The candidate's finite theorem and stronger-side obstruction do not rely on KA001. The combined power-law table does use the separately accepted KA001 positive and lower regions. A potential extension to arbitrary prescribed histogram curves and beta below1/M is new unfinished work, not part of the frozen KH001 theorem.
