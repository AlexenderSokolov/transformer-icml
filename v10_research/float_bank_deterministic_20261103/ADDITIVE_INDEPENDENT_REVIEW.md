# Additive note: independent review of float collision

3 November 2026. This note adds findings from `review_independent/REVIEW.md` without altering `REPORT.md`, `SHA256SUMS`, or any original research files. The reviewer used literal triple counting, the actual pilot forward path, fixed words and fixed parameter values, with no random draws or model random initialization. The review's code, output, settings and input bindings are respectively `review_independent/check_fixed.py`, `review_independent/check_fixed.log`, and `review_independent/INPUT_BINDINGS.json`.

## Stronger equivalence of the witness

At M=1025, A and B are length-1027 all-ones words except zero-based positions {515,518} and {519,522}, respectively. In addition to having the same (J,C1,D,E)=(1021,1019,512,512), their initial, half-split, and protected terminal pairs are all (1,1). Their full eight-triple histograms agree separately within each half. In lexicographic 000,001,010,011,100,101,110,111 order, these are:

- First half: (0,0,0,0,0,0,0,512).
- Second half: (0,0,0,2,0,2,2,507).

They therefore have the same exact rational pilot inputs: (2/1025, 1019/1025, 0, 1, 2/513, 169/171, 1, 1, 1/1025). Nonetheless the recorded two-row half-mode NumPy evaluation produces different uniform successor-1 features, `0x1.fd00bfd00bfd6p-1` for A and `0x1.fd00bfd00bfd7p-1` for B. Hence even the full half-wise triple histograms augmented with those equal boundary pairs do not determine the actual floating-point output for this recorded batch invocation. This is not a counterexample to any exact-arithmetic identity or exact-arithmetic DP theorem.

The same witness is legal from clean A with k=4. The independent check reproduces the original intentionally constructed, non-trained readout's q(A)=0.5 and q(B)=0.6816993976515352, and cross-entropies 0.6931471805599453 and 0.38539989350195286 against the common clean target B(A)=340/341. AB, BA, AA, and BB batches show the difference follows the words when the rows are exchanged in this tested setup. These facts do not establish an erroneous global argmax or a failure for trained pilot weights.

## Batch shape and numerical scope

The independent check also runs A alone. In that singleton call, A's uniform successor-1 feature is `0x1.fd00bfd00bfd7p-1` and the intentionally constructed readout gives q(A)=0.6816993976515352, instead of the `...bfd6` feature and q(A)=0.5 when A is in the two-row AB call. Thus the operational objective must specify its full evaluation layout and backend; a bank collision in a two-row call is not a claim that A has the same numerical result across all batching protocols. The check records Python 3.12.14, NumPy 2.3.5, scipy-OpenBLAS 0.3.30, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, and `MKL_NUM_THREADS` unset. Results may vary with implementation, architecture and shape.

For a conditional augmented-state DP, the review also notes that its record-level bounds must include at least O(log(M+1)) bits for the edit cost per stored state, in addition to accumulator bit patterns, window, other live reduction state, indexing and any backpointers. No equivalence proof for a particular backend reduction or polynomial exact-float DP is supplied.

## Immutable input bindings

The reviewer bound its work to the original `REPORT.md` SHA-256 `35de02c883155a8066bfc27afaccb717baffedaad301603ea4e9fe59157e464f` and original manifest `SHA256SUMS` SHA-256 `a3f1f1e0727aa8163e03dd1cdc7c9332d8e7246903f27153be6a37daa85c0d1e`. The original manifest was verified again when this additive note was written. A separate `ADDITIVE_REVIEW_BINDINGS.sha256` binds this note, the original report and manifest, and the independent review files; it does not modify or replace the original manifest. No random sampling or rerun was required to write this note.
