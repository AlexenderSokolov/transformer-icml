# Independent review of PBP001

Date: 2026-11-03. Verdict: **PASS for the explicitly fixed observation experiment**. This is an independent mathematical/code review of a proof route supplied by the root, not a blind independent discovery or external peer review. No author files were edited.

## Material reviewed

Read the complete actual PBP001 CANDIDATE.md and author check.py, inspected its generated checks.json, and replayed the author's diagnostic output byte-identically. Read the complete accepted ACG001 candidate and its acceptance receipt. Read the exact count, rounding and cut definitions in FPA001's statement and sections 1–4 and inspected its complete program.py. FPA001 is used only to identify the cut; its acceptance is neither needed nor presumed. SOURCE_BINDINGS.json was verified against local bytes. Final hashes are in bindings.json.

## Mathematical findings

1. **Experiment and target.** The lower observation is exactly the twelve nearest-rounded normalized counts and the two protected endpoint bits, with data-independent metadata and independent decoder randomness. A binary predictor is a probability A of symbol 1. In the stationary IID submodel its actual-terminal next-symbol loss is exactly |A-p|, regardless of the realized endpoint. For an IID transition table, two pair steps discard any initial pair and give Pi exactly, including all initial states. Thus every chosen IID source satisfies the all-state certificate at 1/M. The IID start used for the lower is an allowed particular initial law.

2. **Mean curves.** All displayed J, C and D means match the exact designated-successor counts, including overlapping final triples. D divides by M and has floor(M/2) summands. Derivatives of both cubic C curves are positive on [1/8,1/4]; the four J curves are strictly monotone. Multiplication by t preserves strict monotonicity and gives the claimed 1/12 common lower bound. For M>=64, the sharper minimum possible t is 32/65, so the weakest derivative is actually 8/65. Odd horizons and duplicated coordinates do not introduce a constant coordinate.

3. **Cell geometry.** Each monotone coordinate has at most Q threshold roots, so the distinct interior roots number at most 12Q. The largest gap has length at least 1/(104Q). Trisection points have separation at least 1/(312Q), at most 1/24, and remain at least 1/(3744Q) from every coordinate threshold. The endpoint-of-I argument correctly handles thresholds outside the image of I without assuming a derivative bound there. Duplicated roots can only improve the gap bound. Grid endpoints 0 and 1 are not rounding boundaries. h=0 is covered. Fixed tie rules are immaterial on the strict concentration event.

4. **Overlapping counts and rounding.** Replacing one input bit alters at most three departure triples, hence any one count by at most three. There are M+2 independent bits. Therefore the squared bounded-difference sum is at most 9(M+2)/M² <=10/M, valid already at M=64. McDiarmid yields the claimed two-sided exponential tail; a twelve-coordinate union bound gives 24exp[-M/(5·3744²Q²)]. There is no independence assumption about different departure windows or bank coordinates, and no exchange of rounding with expectation. The strict deviation event guarantees no threshold crossing, including any tie convention.

5. **Endpoint dependence and arbitrary readout.** Coupling the observed bank to the common constant bank while retaining the very same endpoint bounds joint TV by the bank failure probability. This avoids the false assertion that bank and endpoint are independent. The endpoint's two-Bernoulli TV is at most 2Delta. C=500000000 makes each failure probability less than 1/16, so joint observation TV is at most 5/24. Independent randomization preserves the TV bound. The common-measure absolute-loss argument gives Delta(1-TV)/2, and the stated weaker 1/(1248Q) lower follows.

6. **Full-history floor and crossover.** p0=1/8 and p1=p0+1/(16sqrt(M+2)) lie in the required interval. Bernoulli KL <=delta²/[p1(1-p1)] <=(64/7)delta² yields product KL <=1/28 and Pinsker TV <1/4. The displayed loss floor 3/(128sqrt(M+2)) >=1/(64sqrt M) is correct. Data processing permits every rounded-bank decoder. For M<CQ² this gives >1/(64sqrt C Q) >=1/(1600000Q); the other regime has the stronger cell lower. Combining two universal lower bounds on the same minimax risk does not require using the same parameter pair.

7. **Upper and precision interpretation.** ACG001 equation (6), with k=xi=0, directly supplies a legal decoder of the same bank and endpoint. Its two coefficients sum to 667160. Consequently the stated Theta(max(M^-1/2,2^-h)) result and h >=(log2 M)/2-O(1) necessity at fixed risk factor are valid. The statement correctly excludes all-encoder bit lower bounds, full arithmetic or architecture precision, robustness lower bounds, training and streaming space claims. The crossover constant is a proof device, not a practical recommendation.

## Independent diagnostics

The independent check.py imports no author code. Its exact rational assertions verify:

- Count expectation formulas by exhaustive words for M=2..7 at three rational p values (18 cases).
- Single-bit sensitivities on all those words, including endpoints and split-crossing windows.
- Exact derivative minima, including the worst odd-horizon half normalization.
- Common rounded codewords and certified threshold margins for M=64,65,127,10000000001 and h=0..6 (28 cases), using rational root enclosures and rational arithmetic throughout.
- Exact constants in the concentration threshold, elementary exponential Taylor bound, KL/Pinsker comparison, crossover and upper bound.

All checks pass. The author replay was byte-identical to checks.json. These are diagnostics; the all-M, all-h theorem depends on the analytic argument reviewed above, not finite enumeration or simulations.

## Residual limitations

No mathematical blocker found. The conclusion is confined to clean C_M and the exact fixed coordinatewise rounding cut. Additional history access, side information correlated with hidden history, a different encoder or a different rounding mechanism changes the experiment. The matching upper relies on accepted ACG001 and its stated source interfaces. No public upload, commit or external write was made.
