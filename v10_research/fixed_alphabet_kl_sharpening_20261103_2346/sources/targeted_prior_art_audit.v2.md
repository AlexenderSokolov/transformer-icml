# Targeted prior-art audit: ordinary add-one terminal KL at fixed alphabet

Checked through 3 November 2026. Target: the candidate at `../fixed_alphabet_kl_sharpening_20261103_2346/tilted_occupation_terminal_kl.candidate.v1.md`, an all-kernel, all-initial-pair expected forward-KL bound O_A(log(n+2)/(n+1)) for the actual terminal row of ordinary full-history add-one. Alphabet dependence is loose, of order A^5 in the principal term. This is a literature comparison, not a fresh mathematical review of the candidate.

## Finding

No inspected primary theorem was verified to establish that exact estimator, arbitrary-initialization, same-path endpoint guarantee. This is a bounded search result, not evidence of novelty or priority. Exact ordinary add-one must be distinguished from a minimax existence bound, and uniformity over kernels from asymptotics for each fixed well-mixing kernel.

For fixed alphabet and order two, the candidate matches the order in n of the stationary minimax rate. It does not establish the sharp growing-alphabet rate. For first-order binary chains, O(log n/n) would still exceed the known minimax O(log log n/n) rate.

## Primary theorem comparisons

1. **Han–Jana–Wu, 2023; inspected arXiv v2.** Eq. (1) is already actual same-history terminal forward KL with stationary initialization. Remark 1, Eqs. (5)–(6), separates ordinary add-one from suffix-averaged add-one and leaves ordinary add-one optimality open. Theorem 22 covers fixed order m >= 2, 2 <= A <= n^(1/(m+1))/C_m, with stationary minimax rate of order A^(m+1) log(n/A^(m+1))/n. The candidate matches its fixed-A n-order, not its alphabet dependence. Section 6 says the nonstationary extension is unclear. These are v2 pinpoints, not journal numbering.
   - https://arxiv.org/pdf/2106.13947v2
   - https://doi.org/10.1109/TIT.2023.3239508

2. **Han–Wu, invited tutorial listed February 2026 on the author's website.** Section III assumes stationarity. Theorem III.2 restates the general-chain minimax rate. Lemma III.3, Eq. (14), and the ensuing construction in Section III-B still average suffix predictors. Theorem III.9 obtains O(k^2/n) for ordinary add-1 only under explicit spectral-gap and state-size conditions: k at least order log n log log n and gap at least order log^2(n)/k, within the stationary irreducible reversible class. Its cited improvement is an iid KL concentration result, not arbitrary-start terminal occupation.
   - Primary tutorial: https://yanjunhan2021.github.io/paper/BITS.pdf
   - Author's date listing: https://yanjunhan2021.github.io/

3. **Mourtada, 2025 preprint, inspected revision dated January 26, 2026.** Theorem 1, Eq. (16), is an iid Laplace-estimator concentration theorem: probability at most 4 delta above 110000[d + log(1/delta) log log(1/delta)]/n, in its stated delta range. Section 1.5 explicitly fixes iid sampling. The proof controls raw moments; this does not by itself justify conditioning a Markov row count or selecting its terminal row.
   - https://arxiv.org/pdf/2504.21787v3

4. **Hao–Orlitsky–Pichapati, 2018.** Theorem 1 advertises O(k^2 log log n/n), but Section 4 uses a hybrid, including add-1/2 on complementary histories. It is not ordinary add-one. HJW's introduction expressly identifies implicit mixing in the advertised prediction upper proof. The inspected arXiv Section 10, Lemma 9, omits the relevant proof; Section 12's concentration is for positive-transition classes. This cannot be used as a verified unrestricted competing theorem.
   - https://arxiv.org/pdf/1810.11754
   - Published proceedings: https://proceedings.neurips.cc/paper_files/paper/2018/file/d34ab169b70c9dcd35e62896010cd9ff-Paper.pdf

5. **Bondaschi et al., From Markov to Laplace, ICLR 2026.** Section 2.1 uses Dirichlet-random rows and uniform initial tokens; Eq. (3) is prior-and-position averaged cross-entropy. Section 2.4's minimax wording cites earlier work rather than proving the target all-start endpoint result. **Bondaschi–Gastpar, October 30, 2026**, Section IX and Theorem 16, concern uniformly positive binary transitions, independent training sequences and a fresh test sequence, with batch regret.
   - https://arxiv.org/pdf/2502.10178v2
   - https://arxiv.org/pdf/2610.41859

6. **Arnon et al., October 2026.** The newly checked Claim 2.11 in Section 2.2 bounds the Laplace estimate from N independent samples of P against another target Q. It does not analyze a row count selected from a single Markov history. Its sequential-sampling theorems address a different computational problem.
   - https://arxiv.org/pdf/2610.14615v2

## Mechanism predecessors and the precise combination

- **Norris–Peres–Zhai:** Proposition 1.1 and Lemma 2.1 are the kernel-uniform hitting/shift-and-sum predecessor. Their specified-target first-hit bound has D/t, and their new-endpoint-state bound has D^2/t. The candidate's fixed-target first-w occupancy lemma is an explicit extension of that argument, not a new foundational concentration principle.
  - https://arxiv.org/pdf/1408.0822
  - https://doi.org/10.1017/S0963548317000074

- **Garivier, 2013:** Theorem 1 gives a time-uniform information-deviation bound, and Section II-A proves it by geometric peeling and exponential supermartingales. Section II-C, Eq. (3) and the following bound, handles predictably selected sample counts; context-tree transition estimation is an explicit motivation in Section I-A. The rate function is binary KL for Bernoulli observations. These establish classical predecessors for the Chernoff and random-count components. They do not state the candidate's terminal-event occupation multiplier or its expected forward-KL theorem.
  - https://arxiv.org/pdf/1309.3376v1

- **Dolgopyat–Sarig:** Example 1.6, "Change of measure," gives positive row reweighting and normalization of a Markov kernel while retaining the initial law. Thus changing transition rows and factoring path likelihoods are standard tools. Their local-limit/large-deviation setting is not the present prediction theorem; the later large-deviation development assumes uniform ellipticity.
  - https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/mc-llt-monograph9.pdf

The specific step to describe is the following combination, without a priority assertion. For a deterministic count band and threshold, change the row from p to q, preserving other-symbol proportions and the initial law. Bound the path likelihood ratio on the deviation event, then apply the kernel-uniform fixed-target occupancy bound under Q. This gives the multiplicative occupation-times-Chernoff bound. The changed law need not preserve stationarity, so an arbitrary-start occupancy lemma is essential even when the original source is stationary. Neither the row likelihood ratio nor the occupancy argument should be described as intrinsically new.

## Search boundary

Targeted searches covered ordinary/add-one/add-1/Laplace Markov prediction, endpoint/nonstationary guarantees, change of measure/tilting, terminal occupation, and self-normalized context counts. The 2026 Han–Wu tutorial and its 2025/2026 iid concentration reference were checked directly, together with the October 2026 smoothing and sequential-sampling papers. Word searches for tilting/change of measure in HJW, HOP and NPZ were supplemented by reading their relevant proof sections; a missing keyword is not a mathematical exclusion proof.

The Falahatgar–Orlitsky–Pichapati–Suresh 2016 original full text remains unavailable in this check. Its later primary-paper descriptions are not a substitute for independently verifying all of its claims. DOI: https://doi.org/10.1109/ISIT.2016.7541787 . Some classical coding results are cumulative-regret bounds and do not automatically control the last prediction. No exhaustive citation-graph or unpublished-work search is claimed.

No numerical work, simulation, training, external upload or public repository mutation was performed.
