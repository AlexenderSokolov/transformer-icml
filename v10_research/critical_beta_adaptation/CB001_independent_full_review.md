# CB001 — independent full mathematical review

2026-11-02. Reviewer: separate LLM reviewer. **PASS for the corrected partial lemma and its stated consequences.** This is not formal verification or external peer review, and it does not establish unknown-budget adaptation.

## Reviewed scope

I read all of `CB001_long_run_veto_partial.md`, then checked the cited support details directly against accepted BK001 §§4–9, BK002 §§3–5, SC003's positive-beta support discussion, AB003's theorem/estimator statement, and the four corresponding exact intake receipts. The initial received CB001 bytes are preserved at `review_snapshots/CB001_initial_received.md`. I did not independently re-review the entire inherited SC003/BK001/BK002/AB003 theorems; their accepted statements are used only in the limited roles just listed.

## Proof audit

1. **Certificate and stationarity.** For a general binary second-order table, `P^2(01,10)=b tau`, so `b tau>=beta x`. Together with `w tau=xb` and full-support positivity, this yields `b^2>=beta w`. No incorrect identification of `theta10(1)` with `b` occurs. Both normalization identities in(2.2) are exact.

2. **Endpoint factor for arbitrary starts.** Stationarity gives `w P^h(11,00)<=y` for every integer horizon, including zero. Consequently `a P^h(11,00)<=min(a,tau e/b)`. The split at `w=1/4` proves the asserted `2tau/sqrt(beta)` upper bound: the large-w branch uses `b^2>=beta w`; the small-w branch uses `sqrt(w)/(1-w)<=2/3` and `e+2a<=3`. The qualifying stationary law is used algebraically, not imposed as the actual initial law.

3. **Run-event counting.** A run of `L+2` ones corresponds to `L` pair-state11 self-transitions after a genuine entry. Counting run entries, rather than every position inside a run, is valid. Pathwise entries are at most exits plus one, and unconditional expected exits are at most `M tau` for every starting law. Strong Markov conditioning at each fixed entry time gives the displayed factorization. The union bound does not assert independence of run counts and the endpoint.

4. **Constants and boundary sources.** The two binomial-mass inequalities are correct. For `L=floor(M/2)`, they give the stated20 constant. Positive all-state minorization permits only full support or a singleton absorbing diagonal: when crossing mass is positive, the two cited entries force all designated exits positive; when it vanishes, simultaneous stationary mass on both absorbing diagonals contradicts the all-state certificate. In each singleton case the relevant weighted event is zero even from unsupported starts, as the note states.

5. **Predictor consequence.** Setting a binary designated estimate to zero increases absolute-error/TV loss by at most the true designated probability. The two terminal states are disjoint. Summing gives the40 constant, with a valid unit cap on the increment. This is a risk-increment guarantee, not a standalone guarantee for arbitrary baselines and not a corruption-risk guarantee.

6. **BK002 support.** The reference attack preserves the long initial all-one prefix; both accepted and rejected outputs fall in the veto at terminal00. The sticky null's target there is `r=1/(2M)`. The clean alternatives used by BK002 are correctly NOT asserted to qualify at `beta=1/M`.

7. **BK001 support.** A source-symbol edit changes at most three indicators of triple111. Thus a legal output has `N111>=M-j-3k>=M/2` in the cited domain. The canonicalization puts all111 self-loops at the start, so every accepted output has the required run; rejections also do. This is an order-dependent property, not available from the histogram alone. Equation(5.1) follows by retaining clean modified risk on non-attacked inputs and bounding attacked loss by r.

## Small clarification requested and resolved

The first inequality in(CB2) holds for arbitrary `1<=L<=M`. Its displayed second inequality `2/((L+1)sqrt(beta))<=4/(M sqrt(beta))` holds only when `L=floor(M/2)` (or more generally `L+1>=M/2`). The surrounding text indicates that intended specialization, but the displayed chain should explicitly mark it. This is a statement-precision correction, not a defect in the derived general-L bound or the intended critical-curve conclusion. The author applied exactly this clarification: CB2 now ends at the general-L bound, followed by a separate sentence explicitly specializing to L=floor(M/2). I read the exact received-to-final diff; no other proof changes occurred. Independent diagnostics were rerun against the corrected proof bytes.

## Fresh independent diagnostics

`CB001_independent_checks.py` uses exact `Fraction`/integer arithmetic throughout; square-root inequalities are squared only after checking nonnegative sides. It passed:

-72 source tables, verifying stationarity and all16 certificate entries;
-1,224 endpoint horizons;
-1,152 full ordered-word run-event dynamic programs across all four starts;
-288 initial-run calculations;
-24 absorbing-support/unsupported-start cases;
-16,380 exhaustive entry-count paths;
-8,768 canonical-support comparisons;
-four exact accepted-proof receipt hashes.

The dynamic programs compute ordered events, not histogram surrogates. Finite results corroborate the proof only for tested instances. The recorded maximum scaled DP value is not asserted to be a sharp constant.

## Scope decision

The corrected note's partial theorem is mathematically sound; the CB2 specialization is now explicit. It does not prove OPEN-CB, stability of the veto under arbitrary Hamming edits, preservation of AB003's nonzero-budget guarantee, or complete critical-curve adaptation. In particular, removing two existing witness supports does not imply that other legal attacks are controlled. The remaining obstacle is accurately stated and must remain open.
