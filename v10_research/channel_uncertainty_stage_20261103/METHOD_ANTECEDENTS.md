# Method antecedents: UMC001 / UWC001 / CAF001

Date: 2026-11-03. Narrow attribution check, not a novelty search, proof review, or exhaustive priority determination. No external writes; no copyrighted PDFs are included. Read scope and failed access attempts are recorded in `READ_SCOPE.json`.

## Bottom line

Robust testing over distribution neighborhoods, separating undetected error from erasure, and rejecting uncertain decisions are established methods. They should **not** be presented as new general theories in this stage. The local claims are specific compositions with the accepted adaptive Markov prediction interfaces and finite communication lower bounds. The passages inspected below do not establish the exact current experiment or its frontier; this is a limited comparison, **not** proof that no earlier work subsumes it.

## Three directly readable primary passages

### 1. Robust testing in TV neighborhoods

Aytijhya Saha and Aaditya Ramdas, *Robust likelihood ratio tests for composite nulls and alternatives*, arXiv:2408.14015v1 (2024), [§1.1 and §2.1, equations (1), (2), (16), (17), Theorem 2.1](https://arxiv.org/html/2408.14015v1).

Read: the paper separately defines mixture-contamination neighborhoods and TV balls, explicitly noting the latter are larger. Its own Theorem 2.1 constructs a test supermartingale under conditional TV-neighborhood uncertainty, assuming the clipping constants remain strictly ordered. Equation (17) controls expectations of bounded functions by TV. This is direct primary evidence for robust testing under TV misspecification, not a theorem about Markov prediction communication. The historical attribution to Huber in §1.1 is **this later paper's report**, not our direct reading of Huber's theorem. We do not transfer its least-favorable construction between neighborhood definitions.

Huber, *A Robust Version of the Probability Ratio Test*, Ann. Math. Statist. 36 (1965), 1753–1758, [DOI](https://doi.org/10.1214/aoms/1177699803), remains the classical lead. Its DOI and Project Euclid PDF access attempts failed; the HTML wrapper exposed no article body. **Original theorem not read.**

### 2. Error/erasure separation, including unknown channels

Neri Merhav and Meir Feder, *Universal Decoding With an Erasure Option*, [arXiv:cs/0604069v1](https://arxiv.org/pdf/cs/0604069v1), §2, equations (1)–(5), (9); §4, equations (15)–(18), Theorem 1 and its proof.

Read: finite-alphabet DMC coding with equiprobable messages; decoder regions include an erasure region, and unsuccessful decoding separates into erasure and undetected error. Their own universal decoder has a competitive-minimax criterion and Theorem 1 bounds its criterion by a polynomial factor relative to the best decoder. This supplies primary evidence that erasure/error separation and unknown-channel erasure decoding predate this stage. Its average-message coding criterion is not the current conditional maximal gate guarantee, nor the adaptive prediction loss. Its §2 attribution of the known-channel tradeoff to Forney is indirect evidence only.

Forney, *Exponential error bounds for erasure, list, and decision feedback schemes*, IEEE Trans. Inform. Theory 14(2) (1968), 206–220, [DOI](https://doi.org/10.1109/TIT.1968.1054129): bibliographic lead checked; DOI access failed. **Original theorem not read or imported.**

### 3. Reject-option recognition

C. K. Chow, *On Optimum Recognition Error and Reject Tradeoff*, IEEE Trans. Inform. Theory 16(1) (1970), 41–46, DOI 10.1109/TIT.1970.1054406. [Readable scan of original paper](https://www.researchgate.net/profile/Fabrice-Clerot/post/Do-you-know-a-Bayes-classifier-which-creates-unrecognized-regions/attachment/59d61e9ec49f478072e97562/AS%3A271742742794240%401441799926252/download/Chow%2B-%2BOn%2Boptimum%2Brecognition%2Band%2Breject%2Btradeoff.pdf).

Read: pp. 41–42, §§I–III, especially equations (2′), (4′). Recognition accepts when the largest posterior class probability exceeds a threshold and otherwise rejects. The paper distinguishes errors from rejected cases and discusses their tradeoff. This is primary evidence for the generic reject option, not a derivation of the local two-slot rule. Chow's rule uses class priors/conditional densities; CAF's abstention uses a nonerasure-count threshold and a separately justified baseline prediction risk. The publication was read as an original-paper scan on a third-party host, not an author-hosted copy; no redistribution permission is inferred.

## What is elementary / what remains experiment-specific

* **UMC/UWC midpoint and nominal event.** In the local rowwise TV ball, the triangle inequality gives separation at least d−2α; the mixture (P0+P1)/2 is exactly d/2 from both rows. This elementary geometry establishes the intersection boundary, not a newly discovered robust-testing principle. The event A={P1>P0}, its nominal midpoint threshold, and bounded-indicator concentration give a sufficient uniform test, not an assertion that this is Huber's minimax-optimal clipped test.
* **Do not conflate uncertainty models.** For fixed ε, mixture contamination {(1−ε)P+εH} lies within the radius-ε TV ball and is generally a proper subset. Example: P=(1/2,1/2), ε=1/4, Q=(3/4,1/4) lies in the TV ball but violates the contamination requirement Q_i≥(1−ε)P_i. The local full-support contaminated witness is one admissible member, not a parametrization of the full ball.
* **CAF two-slot construction.** Correct/wrong/erased outcomes and thresholded abstention use classical error/erasure and rejection ideas. The local probabilities c=q1(1−q0), w=q0(1−q1), e=q0q1+(1−q0)(1−q1), and their uniform small-radius bounds require the local calculation. Both/neither exclusive-event hits must be erased.
* **Risk composition.** The local inequality risk ≤ risk_exact + p_abstain risk_base + p_wrong follows by conditioning on the full pre-channel state and receiver coins, then bounding nonnegative losses. A small marginal abstention probability alone does not justify multiplying baseline risk. None of the inspected external passages is used as a substitute for this step.
* **Frontier and whole-code result.** The partial-support order ln L + ln M/[1+ln(1/α)], its joint-uniform quantifiers, the arbitrary-code likelihood-transport lower, and UWC's paid-payload/efficient-code construction must be credited to the explicit local derivations and inherited dependencies, not to a general erasure coding exponent. The underlying concatenation is not claimed as a new coding method; historical coding-method attribution is outside this narrow check.

The current task additionally fixes an offline source-independent attack, protected terminal symbols, conditional memoryless hidden W, source-specific exact-gate interfaces, and risk normalization max{M^(-1/2),k/M}. Supplemental free counts and whole-message paid counts are different experiments. No direct subsumption of these complete specifications was established in this bounded reading pass; no novelty certification follows.
