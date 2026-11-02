# Bounded dense-attention family: targeted primary-source comparison

Checked **2026-11-02**. **Finding:** the checked sources establish the dilution mechanism and show precisely why it is not an arbitrary-decoder impossibility. They do not directly state BA001's stationary, complete-quantized-summary, actual-terminal expected-TV lower bound. This is a scoped comparison, **not** a novelty certificate, comprehensive survey, or independent validation of BA001.

## 1. Candidate actually compared

Read locally: `comparison.md`, `precision_frontier_followup.md`, and `../bounded_attention/BA001_bounded_local_attention_lower_v1.md` (author candidate, independent review pending at inspection). The model is **one global summary block**, not D layers: D bounded-value ratio coordinates, each pooling all M positions with unnormalized weights in fixed `[a,b]`, over radius-r local windows. Tables may vary arbitrarily by position and public M,Q,beta. Queries depend only on finitely many exact boundary symbols. Downward coordinate rounding precedes an unrestricted, possibly randomized decoder.

BA001's stated candidate bound is

```
R >= c(D,r,a,b)/Q * log(1 + (1/8) min{Q/(M beta0), M/Q}),
beta0=max(beta,1/M),  M>=64, 0<=beta<=1/16, Q>=1.
```

Do not shorten this to a universal `log(1+Q)/Q` family theorem: the finite-horizon cutoff matters. Its good-message bound is `O(1+Qj/M)` only over the suffix lengths where `Q sqrt(j)/M` is controlled. Its large-Q completion uses a separate full-history sampling lower bound.

## 2. Hahn: the exact nearby dilution result

**Version:** Michael Hahn, *Theoretical Limitations of Self-Attention in Neural Sequence Models*, published TACL 8 (2020), pp. 156–171. **Locations:** §3 model; §6 Lemma 5 and Theorem 6, p. 165; Lemma 5 proof, pp. 166–167. [Primary published PDF](https://aclanthology.org/2020.tacl-1.11.pdf)

Lemma 5 bounds the last activation's change by `O(1/n)` after changing one nonfinal input symbol. Constants depend on fixed parameters, heads and depth. The proof bounds logits by A and each dense softmax weight by `exp(2A)/(n−1)`; it uses bounded activations and Lipschitz positionwise processing. Dot-product attention is controlled on the bounded reachable domain, not asserted globally Lipschitz on all Euclidean inputs. Theorem 6 concerns next-symbol **cross-entropy** for its specified PARITY automaton and 2DYCK PCFG: asymptotic unigram level for the former, positive excess for the latter, using a Lipschitz prediction map. It is not a quantized-summary theorem, arbitrary-decoder lower bound, or classification-accuracy impossibility. The displayed softmax denominator ranges across the input positions; the argument is not a theorem for arbitrary sparse masks.

**Essential correction/version supplement:** Hahn's author supplement dated **May 5, 2021**, §S2, pp. 8–10, adds the missing attention-weight-change term in the published induction. It explicitly identifies bounded positional embeddings and Lipschitz maps as necessary hypotheses of that proof and bounds the additional variation term. Cite this with Lemma 5 rather than reproducing the uncorrected induction. [Primary author supplement](https://mhahn.info/files/transformers-proof.pdf)

## 3. Chiang–Cholak: why sensitivity is not information loss

**Version:** David Chiang and Peter Cholak, *Overcoming a Theoretical Limitation of Self-Attention*, ACL 2022, pp. 7654–7664. **Locations:** §2.2 positional conventions; §3 exact constructions; §4.2 Proposition 2, p. 7659; §5.3 Eq. (2)/Proposition 3, p. 7661. [Primary published PDF](https://aclanthology.org/2022.acl-long.527.pdf)

Their fixed-size constructions recognize PARITY and FIRST exactly despite shrinking confidence; positional encodings are allowed as arbitrary functions on positions. Proposition 2 uses layer normalization with **epsilon=0** to convert recognition into arbitrarily small cross-entropy. Such normalization is not Lipschitz near zero variance. They explicitly distinguish positive epsilon, which restores Lipschitz continuity and does not escape Hahn's asymptotic lemma. Proposition 3 gives arbitrarily small FIRST cross-entropy, with or without layer normalization, using attention logits multiplied by `log n`. This is a different attention rule, violating a length-independent logit bound. Their statements are recognition/cross-entropy results, not bounded-precision guarantees.

## 4. Finite-precision/Markov cross-checks, without resurveying

**Rajaraman et al., arXiv v1, July 25, 2024.** §6 Theorem 6.1 requires a one-layer transformer approximating conditional 3-grams on ternary length-T inputs to additive `1/(3T)`. With p-bit embeddings and unnormalized scores it gives `2pH+dp+2>=T/3`; Appendix D uses communication complexity. This is a worst-input representation requirement, not expected unknown-source prediction risk. §5 Theorem 5.1 constructs three-layer, one-head conditional k-grams with RPE and layer normalization; Remark 5.2 explicitly leaves finite-precision error unbounded in that proof. These are not BA001's one bounded local-summary block. [Primary version, Theorem 6.1/Appendix D and Remark 5.2](https://arxiv.org/html/2407.17686v1)

**Chakrabarti–Pitassi–Alman, arXiv v1, February 2, 2026.** §2.2 Theorem 2.4 separates p from p−1 fixed-point bits for one-layer, one-head, value-dimension-one transformers computing equality on their specific padded representation, with `m=2p−1,n>4p`. Appendices A.3–A.4 specify finite arithmetic, and B.2 supplies the proof. This is a Boolean expressivity separation with a particular input/arithmetic contract; it neither proves a stationary Markov TV rate nor equates per-operation precision with final-bank rounding. [Primary version and theorem](https://arxiv.org/html/2602.02707v1)

The waiting/harmonic and finite-message precedents already audited in `precision_frontier_followup.md` remain relevant; no new claim of first logarithmic quantization penalty or first rare-context mechanism is justified. Their exact loss/budget differences remain unchanged. That earlier note is the evidence record for those sources; this pass does not pretend to have reread all of them.

## 5. What follows, and what must still be proved (our comparison)

### The established mechanism is not the candidate theorem

For a dense weighted mean with `a<=w<=b`, bounded values and bounded local influence, altering O(j) local terms gives an O(j/M) envelope. This is the same dilution mechanism exposed by Hahn. But a small real difference can preserve a perfectly decodable bit; Chiang–Cholak makes that distinction concrete. Nor does an O(j/M)-diameter D-dimensional box automatically contain only `O(1+Qj/M)` rounded messages: its generic count is a Dth power.

BA001 instead needs the **whole** good message to lie near finitely many short one-parameter curves, with stochastic thickness O(sqrt(j)/M). Covering those curves when thickness is at most the grid scale produces the linear label count. This is an additional distributional geometric argument, not a corollary of single-token sensitivity alone. Finite-message Bayes loss and the common-prior harmonic sum are standard once that complete count and event probabilities are established.

The local proof's freeze-every-boundary-query maneuver matters: it must retain concentration under the unconditional Bernoulli suffix and only then select the actual boundary branch. Conditioning directly on a terminal query and continuing to assert IID would not be justified. Similarly, the good set may depend on the latent parameter, but the containing message alphabet used by the covering argument must not.

### Scope checklist before positioning as an attention-family result

* **Depth:** D here counts outputs. General fixed-depth transformers can create nonlocal intermediate features, and are not included merely because their depth is fixed. Hahn's multi-layer sensitivity does not automatically give BA001's independent-suffix concentration/curve lemma.
* **Positions:** BA001 can permit arbitrarily complicated positional tables because it bounds their *resulting* weights and values directly. That is not permission for unbounded effective scores/values. Hahn's bounded-embedding hypothesis and BA001's bounded-table hypothesis are different sufficient conditions.
* **Masks:** selecting only rare active positions destroys the M-sized denominator. Local hard copying can be absorbed only into a genuinely fixed-radius feature map; globally selective or growing historical ports cannot. A causal model whose intermediate rows pool different prefix lengths needs its own proof, not a silent replacement of n by M in Hahn.
* **Layer normalization/readout:** unrestricted discontinuous operations *after* the rounded cut are already covered if the message argument holds. Before the cut, epsilon=0 normalization, length-dependent amplification or unbounded values can change the encoder class. Positive fixed epsilon is not by itself an all-operations finite-precision certificate.
* **Uniformity:** constants must remain controlled across encoders and M,Q. Length-growing score ranges (including log-length scaling), increasing D/r, or extra real side channels cannot be hidden in a constant.
* **Loss:** cross-entropy lower bounds do not transfer into same-rate TV lower bounds. The candidate must independently establish stationary-source event probabilities and loss at the actual terminal pair.

## 6. Defensible conclusion and audit boundary

**Not directly covered by the checked theorem statements; substantially built from standard mechanisms.** If BA001 survives independent review, describe it as a distributional, complete-information-cut extension for a declared one-block bounded local-attention family—not as a new discovery of attention dilution, a general transformer lower bound, or an optimality theorem for all finite-precision encoders.

This pass inspected the primary locations above and the local candidate; it did not independently re-prove the external papers or BA001. A DOI-page retrieval returned HTTP 403; no retry or bypass was attempted, and the independently retrieved public ACL PDF supplied the evidence. No private proof details were sent to external search, no contact was made, and no accepted/frozen research record was modified.
