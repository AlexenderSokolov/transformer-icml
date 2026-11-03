# Additive clarification: batch context for the regret guarantee

3 November 2026. This note responds to independent review and supplements `REPORT.md` without modifying it or its original checksum manifest. It makes the evaluation context in the 2ε+η statement explicit.

## What objective is compared

Fix the candidate set, order, layout, dtype, backend, threading and batch or slot context **before** defining a floating objective. For example, let N legal candidates be ordered z_1,...,z_N; place them all in one specified N-row batch, and define U_all(z_i) to be the score returned at slot i in that complete batch. Each slot and its surrounding batch are part of this definition. If the ideal bank score I satisfies |U_all(z_i)-I(z_i)|<=ε uniformly for all i, and the returned legal witness z_hat has I(z_hat)>=max_i I(z_i)-η, then for z_star maximizing U_all,

  U_all(z_star)-U_all(z_hat) <= 2ε+η.

The U_all value of z_hat is **the value it has in that same predetermined all-candidate batch and assigned slot**, not the result of a later singleton invocation. The mathematical statement needs no actual float evaluation of the witness: the score is defined by that protocol and the bound is conditional on its uniform error premise. If one reports an observed floating score for the witness, one must evaluate or retain it in the corresponding context; a singleton value cannot be substituted as the same number.

The independent float-collision review explicitly observed a concrete violation of singleton/batch equality: the same word A has different uniform rail values in the AB two-row batch and in a singleton call. This makes the distinction operational, not cosmetic. Nothing in this clarification asserts that this witness changes the trained model's global maximizer.

## Alternative fixed-filler protocol and cost

One can instead predefine a deterministic context C(z): put z into one designated slot of a fixed B-row batch with fixed filler words, and use the returned score in that slot. The function U_fill(z) is then the same protocol for every candidate; the same argument applies to max U_fill and the witness's U_fill score if the stated error bound holds uniformly. U_fill is a different objective from U_all unless bitwise equivalence is proved. Each numerical evaluation of this fixed-filler protocol entails preparing and evaluating the B-row context, with O(BM) pooling work and O(BM) input/intermediate storage for the fixed-size architecture, plus readout, actual allocation, and comparison costs. It is not a free singleton score.

For an N-row all-candidate context, actually reconstructing and evaluating the pilot's full batch to obtain the witness's prescribed score requires preparing the specified N rows and running that invocation: O(NM) pooling work and O(NM) input/intermediate storage in the stated full-array protocol, plus readout, allocation, comparisons and witness-output costs. If the full batch and its output have already been retained, reading its saved witness score need not repeat that work, but retention has its own storage cost. An implementation-specific method with smaller cost would need a proof it reproduces the relevant full-batch slot; simply rerunning the witness alone is not such a proof.

## Cross-context variant

Suppose, separately, a singleton protocol defines U_single and has a proven uniform error ε_single against the same ideal score I, while the all-candidate protocol has error ε_all. Then the cross-context numerical inequality

  max_z U_all(z) - U_single(z_hat) <= ε_all+ε_single+η

follows. This is a comparison of scores in two **different** protocols; it does not establish equality, or an all-candidate objective value from a singleton measurement. To claim regret under the singleton protocol instead, prove its own uniform bound for all candidates and compare max U_single to U_single(z_hat), giving 2ε_single+η. None of these bounds establishes the necessary backend, transcendental, target or cross-entropy error premises; those remain conditional as in the original report. No random sampling, model initialization, new model evaluation, or publication was performed for this note.

## Scope of the sharpness example

The 2ε constant is sharp for **abstract scalar objectives** with only a uniform absolute error premise. The diagnostic's two computed scores (-ε,+ε) include a negative value and are not themselves an example of cross-entropy. Adding any common offset c>=ε gives ideal scores (c,c) and computed scores (c-ε,c+ε): all are nonnegative and an ideal tie-breaking choice can still attain regret 2ε. Nonnegativity alone, however, does not show these scores arise from the pilot's specific fixed readout, shared target and floating protocol. Thus this construction establishes no CE-specific sharpness claim for the pilot.
