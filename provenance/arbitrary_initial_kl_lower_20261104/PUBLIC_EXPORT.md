# Arbitrary-initialization A⁵ terminal-KL correction

This append-only scientific addition follows [the two-upper-bound archive](https://github.com/AlexenderSokolov/transformer-icml/commit/109ac29309af3fe508dafef493fd891421dfb0fa). It does not rewrite an earlier proof, review, or scientific source. Repository entry points gain a new dated section and the exact-byte inventory is updated.

## Result and reading order

- [Chinese correction](../../v10_research/arbitrary_initial_kl_lower_20261104/v10_stage_correction_arbitrary_init_20261104_0122.zh.v1.md).
- [Independent KL-transfer analysis](../../v10_research/arbitrary_initial_kl_lower_20261104/kl_lower_transfer_audit_20261104.md).
- [Observation, quantifier and source-provenance audit](../../v10_research/arbitrary_initial_kl_lower_20261104/arbitrary_initial_kl_lower_audit_20261104.md).

For integer A≥2 and n≥1, the inherited MM5 full-history, actual-terminal TV minimax lower bound implies

    R_KL^all(A,n) ≥ 2^(-31) min{1,A^5/(n+1)}.

The source class allows arbitrary initial-pair distributions. Pinsker and Jensen preserve the order of the source supremum and predictor infimum. Combined with the separately reviewed ordinary add-one upper O(A^5 log(n+2)/(n+1)), this identifies the necessary A⁵ polynomial factor. The growing-alphabet logarithm, full saturation law and exact consistency threshold remain unresolved. The separate stationary A³ theory is not an arbitrary-initialization upper bound. The minimax log A cap comes from the uniform predictor, not an improved add-one cap.

## Provenance and corrections retained

The original Chinese correction addressed an earlier analytical synthesis that had compared the arbitrary-initialization upper only with the stationary HJW lower. That synthesis is not claimed to be a member of this public addition; the mistaken comparison and corrected statement are explicitly restated in the correction itself.

The directly inspected original MM5 hash is 19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3. Its old report cites 5fef432092c4d7394021f1651dbcd086b660028b2a62c1297342340892dd6d24. This historical difference remains unresolved. Neither audit presents the old report as a byte-level review of the current original.

The [public scientific MM5 copy](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/inherited_statistics/DOT_conditions_stage02/inherited/MM5_statistical_proof.md) was read back during this publication: 21262 bytes, SHA-256 4d5e865ebe00846662cef1830be02bf52cc2b839eca8a0600f8baa501ada6078, Git blob d8aef0a80a3dd33a01dba631a454d4fccf4ffda1. This is a distinct scientific copy, not the original 19d2 source. The earlier odd-m correction changes the later review wording, not MM5's proof or constant.

`PUBLIC_SOURCE_MAP.json` binds every original and exported analytical document by size and SHA-256, supplies current Git blob identities, and records each nonmathematical edit with exact line ranges and segment hashes. Original locations and removed operational text are not published. Original scientific hashes inside the documents are preserved; those hashes must not be mistaken for the current derivative hashes. This export keeps every mathematical formula, assumption, quantifier, boundary case and scientific limitation unchanged.

## Verification boundary

From a complete checkout, run `python3 tools/public_verify.py` and `python3 -m unittest discover -s tests -v`. These existing checks verify public membership, bytes and integrity-verifier rejection cases. They do not establish mathematical truth. No model, training, numerical mathematical experiment, sampling, browser rendering or historical preparation script is run by this addition.

The two audits are independent-context LLM analytical checks, not external peer review, formal verification, cross-model certification or novelty clearance. MM5 is inherited project mathematics; the KL transfer uses standard inequalities. Missing 20:35 micro-pilot original results remain missing. There are no reconstructed raw logs or claimed recovered training outcomes.
