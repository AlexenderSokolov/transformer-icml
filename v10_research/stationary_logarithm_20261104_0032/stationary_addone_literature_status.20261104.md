# Literature status audit: ordinary full-history add-one prediction

Checked 4 November 2026 UTC. Read-only research; no numerical experiments, publication, repository updates, or author contact. This is a bounded literature search, not a certification of priority.

## Finding

The target is the ordinary estimator `(N_ij+1)/(N_i+k)`, using the entire observed trajectory and queried at its actual terminal state, with a supremum over all stationary k-state first-order chains and no mixing hypothesis. I found no subsequent primary-source theorem that resolves the HJW question for this estimator. The strongest dated status evidence is an explicit open question in Han's 28 February 2025 slides. Han–Wu's February 2026 tutorial still proves unrestricted achievability using suffix averaging; its ordinary add-one guarantee has a spectral-gap hypothesis.

Safe wording: **The candidate's first-order specialization addresses the question explicitly posed in HJW Remark 1, also explicitly open in Han's February 2025 talk. No resolving theorem was identified in the later sources checked through 4 November 2026. This search does not establish novelty or priority.** Mathematical validity of the candidate is a separate audit.

## Primary-source matches and exclusions

### 1. HJW: exact question, estimator and risk

Yanjun Han, Soham Jana, Yihong Wu, *Optimal prediction of Markov chains with and without spectral gap*. NeurIPS 2021; IEEE Transactions on Information Theory 69(6), 3920–3959, June 2023. arXiv submitted 26 June 2021, v2 dated 3 May 2022.

- [Primary HTML, Remark 1 and equations (4)–(6)](https://arxiv.org/html/2106.13947v2#S1.R1).
- [Version history](https://arxiv.org/abs/2106.13947).
- Theorem 1: rate `k²/n log(n/k²)` for `3 <= k <= sqrt(n)/C`; its lower bound remains valid for irreducible reversible chains.
- Equation (5) defines the ordinary add-one estimator. Equation (6) averages that estimator over all terminal suffix lengths. Remark 1 explicitly leaves the full-history term and constant add-c variants open.
- Theorem 3 gives full-history add-one `O(k²/n)` only with quantitative absolute spectral-gap conditions. These do not solve the unrestricted question.
- The binary optimal predictor is a trajectory-dependent hybrid, not ordinary add-one.

The abstract and theorem were read directly. The final IEEE PDF surfaced at [NSF PAR](https://par.nsf.gov/servlets/purl/10539616), but a later direct fetch returned HTTP 502; use the verified arXiv text for this audit's exact location.

### 2. Explicit status in February 2025

Yanjun Han, *Next-symbol prediction without mixing: optimal rates, algorithms, and hardness*, NYU Courant Graduate Student/Postdoc Seminar, **28 February 2025**.

[Author's PDF](https://yanjunhan2021.github.io/slides/mc_prediction_slides.pdf), slide 19, physical PDF pages 52–53, states: **“Open question: simple add-1 estimator with full data is optimal?”** Slide 18 immediately preceding it defines the suffix-average estimator.

This is direct evidence of the authors' stated status in February 2025, not a statement about every subsequent unpublished result.

### 3. February 2026 tutorial does not close it

Yanjun Han and Yihong Wu, *Next-symbol Prediction from Compression: Statistical and Computational Foundations*. The [author-maintained publication list](https://yanjunhan2021.github.io/publication.html) dates the invited paper February 2026.

[Author's PDF](https://yanjunhan2021.github.io/paper/BITS.pdf):

- Theorem III.2, printed p.6, restates the unrestricted k>=3 minimax rate.
- Lemma III.3 / Corollary III.4, printed p.7, obtain it via an average of add-one estimators over terminal suffixes. The displayed predictor is explicitly a sum over suffix lengths.
- Theorem III.9, printed p.9: if `k >= c log n log log n` and `gamma_0 >= c log² n/k`, the parametric `O(k²/n)` risk is attained by ordinary add-one. The class is stationary, irreducible and reversible.
- The improvement uses Mourtada's i.i.d. KL concentration result in place of HJW Lemma 17.

The tutorial contains no located theorem giving the unrestricted fixed-time guarantee for the ordinary estimator. Its continued suffix averaging is suggestive context, not an explicit November 2026 open-status declaration. Use the original HJW theorem for quantitative statements rather than tutorial typographical expressions for redundancy/higher order.

### 4. Most recent close hit: different batch-regret problem

Marco Bondaschi and Michael Gastpar, *Batch Universal Prediction via Conditional Additive Smoothing*, submitted **30 October 2026**, [primary HTML](https://arxiv.org/html/2610.41859v1).

Section IX studies binary chains with `(p,q) in [delta,1-delta]^2`, fixed delta>0, n independent training sequences of length ell and an independent test sequence. Theorem 14 concerns the non-updating KT/add-half predictor (equation 130): transition batch regret `1/n + O_delta(1/(n sqrt(n ell)))`. Theorem 16 gives asymptotic minimax batch regret, including `1/n+o(1/n)` with stationary initialization.

This differs in loss, samples, alphabet regime, mixing restrictions, and estimator. It is not a resolution of HJW Remark 1.

Mechanism near-hit: Appendix I-A, equations (396), (418)–(420), cancels a stationary-initial-law denominator `(p+q)^m` with a deliberately chosen prior to obtain beta posteriors. This is a Bayesian lower-bound construction, not row-tilted path comparison with a +/-1 count shift or the terminal-occupation coefficient in the candidate.

### 5. Mamba headline is not a resolving theorem

Bondaschi et al., *From Markov to Laplace: How Mamba In-Context Learns Markov Chains*, ICLR 2026; arXiv first submitted **14 February 2025**, revised **22 June 2026**. [Primary paper](https://arxiv.org/html/2502.10178), [version history](https://arxiv.org/abs/2502.10178).

The abstract calls Laplacian smoothing Bayes and minimax optimal. Actual Theorem 1 proves exact representation of the Laplacian estimator by MambaZero, for arbitrary input sequences. Section 2.4's minimax assertion is asymptotic and cites Xie–Barron 1997 (memoryless redundancy) and Hao et al. 2018; it supplies no new uniform stationary no-gap terminal-risk theorem. Its data model uses row-Dirichlet transition priors. Do not infer resolution from the abstract's broad terminology.

### 6. i.i.d. smoothing results are not terminal-state Markov results

Jaouad Mourtada, *Estimation of discrete distributions in relative entropy, and the deviations of the missing mass*, Mathematical Statistics and Learning 9(1), 69–144 (2026); arXiv submitted **30 April 2025**, v3 **23 January 2026**. [Primary HTML](https://arxiv.org/html/2504.21787), [publisher PDF](https://ems.press/content/serial-article-files/52576).

The sampling model in Section 1.1 is i.i.d. The Laplace concentration theorem and its use in the 2026 tutorial are not a direct conditional-binomial argument for Markov counts. Section 6.1, Lemma 3 and equations (58)–(60), already decomposes smoothed KL loss into a regular component and severely underestimated coordinates. This is a relevant antecedent for loss-sensitive analysis, not the candidate's stationary occupation lemma.

Canonne, Sun and Suresh, *Concentration Bounds for Discrete Distribution Estimation in KL Divergence*, arXiv v2 **13 June 2023**, [primary HTML](https://arxiv.org/html/2302.06869). Section 1 expressly assumes independent samples. Theorems 1–2 control deviations of Laplace KL loss; this is the sole paper returned by one HJW citation-graph query. It does not establish unrestricted Markov terminal-risk optimality.

### 7. Infinite-memory extension still averages

Han, Tianze Jiang and Wu, *Prediction from compression for models with infinite memory, with applications to hidden Markov and renewal processes*, COLT 2024; arXiv **23 April 2024**. [Primary text](https://arxiv.org/html/2404.15454).

Proposition 1 in Section 2 defines an averaged suffix predictor, controlling its risk by redundancy plus a memory term. Theorems for HMMs and renewal processes concern that reduction and different models. This is not a full-history add-one resolution.

## Mechanism-priority assessment

The candidate inspected was `stationary_addone_sharp_log.candidate.v1.md`, SHA-256 `90e949efc52cd8f3d57108ca334f9083a9858950183dd8e6f60d6664d92c6195`, especially Sections 2–6. I searched for row perturbation/tilting, stationary likelihood cancellation, terminal occupation, self-normalized Markov transitions, and Laplace prediction.

**Found antecedents, not the exact combination:**

- Thiede, Van Koten and Weare, *Sharp entrywise perturbation bounds for Markov chains*, SIAM J. Matrix Anal. Appl. 36(3), 917–941, published **2 July 2015**. [Primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4610747/). Section 3, Theorem 1 and equation (14), use the return-cycle identity `pi_z/pi_s = E_s[number of visits to z before return to s]`, also citing Norris's Theorem 1.7.5. Thus the excursion representation underlying the candidate is established classical material. Its main results bound stationary-distribution sensitivity, not fixed-time prediction loss. I did not locate the candidate's shifted likelihood cancellation or joint terminal tail there.
- Jeffrey J. Hunter, *Stationary Distributions and Mean First Passage Times of Perturbed Markov Chains*, Research Letters in Information and Mathematical Sciences 3, 85–98 (**2002**). [Primary author-institution PDF](https://mro.massey.ac.nz/bitstream/handle/10179/4371/Stationary_Distributions_and_Mean_First_Passage_Times_of_Perturbed_Markov_Chains.pdf?isAllowed=y&sequence=1). Section 4 explicitly studies one-row perturbations and relative changes in stationary probabilities. This is further background, not a located prediction application.
- Mourtada's deterministic KL decomposition and Bondaschi–Gastpar's prior cancellation are nearby but different mechanisms, described above.

I did **not** identify an earlier source with the exact joint coefficient `min{2m/(n+1),pi_s} exp[-m d(q||p)]`, obtained by combining one-row change of measure, stationary density comparison, a +/-1 count shift, and fixed-terminal occupation. That negative search result does not establish that either this lemma or its combination is novel. In particular, do not advertise exponential tilting, excursion stationarity, or loss decomposition themselves as new.

## Coverage and limitations

Coverage included current web search, full primary texts for the close matches above, date-restricted paper searches through 2026-11-04, HJW exact-title citation searches, author publication pages, and an independent second targeted search. A citation-graph tool returned only one HJW citer, plainly insufficient for a complete citation census; other discovery routes were used, but completeness is not claimed. Author pages and search indexes can omit recent, non-English, unindexed or unpublished work. No inference is made about the user's pre-existing unpublished work. No authors were contacted.

The literature supports careful historical positioning. It does not yet support an unqualified “first proof,” “new theorem,” or “this problem remained open until today” claim.
