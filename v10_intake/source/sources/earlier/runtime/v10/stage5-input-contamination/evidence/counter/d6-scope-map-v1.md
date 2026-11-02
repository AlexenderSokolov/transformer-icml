# D6 primary and strong-DIRECT scope map, v1

Counter, 2026-10-26. Current fifth-stage root integration companion to
c2-proof-v1.md, exact C2 obligation
52a14a0c60279133c7acc7067c15eb4cfbff32368f8a721e59df9bf3eecd9ff1.
This is a bounded source/model comparison, not an independent Fact or a
premise of the self-contained C2 proof. Only the two D6 works and the
specified Pydi/Jog supplement are compared. Current PROBLEM.md D1-D7 and
inputs/SOURCE_CORRECTIONS.md govern scope.

## 1. Pinned primary locations and what they support

The supplied PDFs and their page-preserving text were consulted locally;
no new retrieval, literature expansion or diagnostic rerun was needed.
PDF page numbers below count physical pages starting at1. Original source
files are preserved unchanged. SHA256 values here identify the PDF bytes,
not the convenience text files.

| Primary | Exact locations | Supported scope and limit |
| --- | --- | --- |
| Chen/Gao/Ren, *A General Decision Theory for Huber's epsilon-Contamination Model*, arXiv1511.04144v2 | PDF pp1-2, eqs(1)-(2); pp3-5 and Theorem2.1; p6 Theorem3.2; pp13-14 Lemma6.1 and Theorem2.1 proof | IID observations from a Huber mixture with arbitrary contaminating law; robust testing through TV and an estimation modulus. The separate contamination neighborhoods do not impose one shared hard-edit input kernel. Theorem3.2 is attributed there to their earlier2015 result. |
| Pydi/Jog, *Adversarial Risk via Optimal Transport and Optimal Couplings*, ICML2020, PMLR119:7814-7823, main | PDF p3 section2.1 and Theorem1; p4 Definition1/eq(5), Theorem2/eq(6), Corollary3.1/eq(7); pp5-6 section4 and Theorems5-6 | Equal-prior binary classification, class-dependent point maps and separate Wasserstein distribution attacks. Transport-tail/testing and finite submeasure ideas are strong existing tools. Their stated model permits separate class maps and does not supply the present common input-row quantifier. |
| Same work, supplement | PDF pp1-4 Theorem1, Lemmas0.1-0.3, Corollary0.1; p5 Theorem2; p7 Definition1 for unequal masses | Supplies the detailed transport/testing proof, the Markov tail bound and an explicit unequal-mass submeasure definition. Supplement Theorem1 corresponds to main Theorem2; its numbering differs. |

Official primary URLs and pinned PDF hashes:

- CGR: https://arxiv.org/pdf/1511.04144v2 ; SHA256 `538cda7c3ea92a31a394e85b2928a6309cd751b9f4afc5e1732b2bf2a4b8f645`.
- Pydi/Jog main: https://proceedings.mlr.press/v119/pydi20a/pydi20a.pdf ; SHA256 `df20b171617bd33522b798fa59e9f52ab29401fc463328869297c19dd7d5a19a`.
- Pydi/Jog supplement: https://proceedings.mlr.press/v119/pydi20a/pydi20a-supp.pdf ; SHA256 `332e09858ae7e474e967a6dcc10274de57a3a9e16f0455296efff664b1e25d74`.

The CGR digest above follows SOURCE_CORRECTIONS.md and agrees with the
actual PDF and old download manifest. The old primary-claim-map prose
shortened that digest incorrectly. This new map corrects the citation;
it does not modify that historical file, the PDF, or any old admission.

CGR's displayed testing separation is TV(P0,P1)>2epsilon and its displayed
modulus uses TV(P_theta1,P_theta2)<=epsilon/(1-epsilon). Pydi/Jog's main
Theorem2 uses the transport tail cost 1{d(x,y)>2epsilon}; Corollary3.1
bounds it through the p-Wasserstein cost divided by (2epsilon)^p.
These are relevant baseline principles; no application of either theorem
is required to justify the current finite C2 proof.

## 2. Exact bridge still required in the present model

| Coordinate | Current D1-D2/C2 requirement | Location in new C2 proof |
| --- | --- | --- |
| Observation object | One complete binary history; last pair fixed on every input/seed | sections1,4,7 |
| Conditional experiment | Actual same-trajectory S_N=00, with probability u0=k/N | direct stationary reversal in section4; section8 |
| Quantitative coupling | Entire original conditional histories, every intermediate pair and every free symbol; no division by rare-query probability in the error bound | sections4-6: C<=97(2Nu+96)Delta<=10000(1+Nu)Delta |
| Kernel quantifier | One T from public N,k fixed before predictor/Q/actual source label; legal under every D1 source | sections3,7 |
| Residual transport | Jordan masses retain mass tau; remove cycles, collapse paths; no normalization shortcut | section2 |
| One input row | The same row acts on common mass; good signed masses cancel; bad fractions stay at their own inputs | section3: TV(PK,QK)=bad mass<=C/(2k) |
| Budget | At most k earlier flips for every raw input and every finite private seed; not an expected-distance constraint | explicit Hamming midpoints and uniform integer seed intervals, sections3,7 |
| Conclusion | TV<=1/64 after private-seed averaging; every common full-Z predictor has one t_* for R_00>=c AND R_av>=ck/N | sections7-8 |

An entire dependent trajectory can be a single feature in an optimal
transport model. Dependence alone therefore does not establish a gap from
Pydi/Jog. What is proved here is the specific D1 full-history cost bound
and the one shared hard-budget input-row channel, followed by the actual
terminal KL reduction. The generic testing, transport-tail and submeasure
steps are baseline ideas. No novelty or publication-centrality inference
is made from this bounded comparison.

## 3. Strong full-Z baseline and concrete DIRECT

The C2 comparison class contains EVERY common randomized predictor on
Z,N,k,Q, with unrestricted output probabilities and unlimited computation.
It may know the public witness pair and fixed T. In particular this includes
strong direct scanners using all observed symbols, re-encodings, all
statistics of Z, and the concrete D3-D4 DIRECT implementation. Neither
clean history nor private channel seed is supplied to any member of this
class. The proof does not restrict a baseline to the JOINT internal19 words.

The concrete DIRECT upper family owns the same full observed batch Z,
computes eight dirty-prefix triple counts, and selects the row using the
actual preserved terminal pair. Its dirty prefix endpoint has no protection
or clean side information. It uses the identical D3 smoothing/clipping/grid
rule as JOINT, including k=0, Q=2 and the real N=3,4,5 uniform branch.
C3 must separately prove bit identity for every individual observed Z.
C2 alone does not prove a resource or implementation assertion.

| Implementation | D4 finite selected-row/output table | Pricing obligation |
| --- | --- | --- |
| DIRECT | 8+46 operations, with paid full-input acquisition, count scan and cleanup in addition | Every separate D5 packed bit-register online/offline coordinate |
| JOINT | 17+46 operations, with paid frontend/input/feature/endpoint acquisition and cleanup in addition | Every separate D5 principal batch-hybrid dense/physical-scalar online/offline coordinate |

The two D5 models are distinct. The theorem neither equates those budgets
nor proves JOINT efficiency superiority, optimal costs, an old Bstar cap,
or a uniform common resource advantage. A future same-budget superiority
claim would require additional matching cost assumptions and evidence.

## 4. Exact root integration text

After current C1 and C3 are admitted, either implementation emits the same
D3 predictor on the same Z. C1 applies to the SAME globally admissible
channel constructed in C2, at u0=k/N and C2's SAME selected t_* for that
predictor. Consequently, on this same actual-terminal experiment,

    c*k/N <= R_av
           <= 16000000/(3N)+135680*k/N+3/Q,
    R_00 >= c,     c=1/3276800000000.

The selected t_* may depend on the common predictor and public tuple.
It is one source for both lower inequalities. The channel is already fixed
independently of predictor and Q. These facts give an O(k/N) contamination
upper contribution and an Omega(k/N) full-Z lower. The 1/N and1/Q terms
have upper bounds only here. Since DIRECT and JOINT agree pointwise, this
contract establishes no statistical superiority of JOINT.

Preserve the exact exclusions in D6: no every-source damage, no complete
conditional-risk classification, no small unconditional history-TV claim,
no deterministic common attack attainment, no practical/optimized constant
claim, no learning/novelty conclusion, and no time-causal sensor, all-layer
or IEEE fault theorem. Existing source reviews and old roots are provenance;
current native component/root evidence, fixed independent review, fresh
[Non-scientific operational metadata omitted.]
Completion of this stage leaves the v10 mother problem active.
