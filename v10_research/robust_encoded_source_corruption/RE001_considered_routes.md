# RE001 considered routes and boundaries

These are analytical routes considered and rejected, not invented failed experiments. The only actual reviewer-identified implementation defect so far is recorded separately in RE001_issues_and_resolution.md.

1. **Apply the old clean MG risk theorem to the corrupted word as if it were Markov.** Invalid: an offline history-adaptive edit kernel need not preserve a homogeneous Markov law. The proof instead bounds recovered corrupted counts against CLEAN counts pathwise, then takes occupation/statistical expectations under the clean law.
2. **Treat all compander/snake errors as a global additive raw-frequency budget O(epsilon).** It is valid but wasteful for K>=3 and can reintroduce a logarithmic precision price. The refined error is square-root mass plus epsilon²+epsilon/chi, with a cross term absorbed into k/M+epsilon².
3. **Use ordinary add-one with a unit occupation cap and transplant e=max(sqrt(beta),1/M) for binary.** Invalid interface: that cutoff is for the designated true-q weighted occupation functional, not general unit caps. The data-derived row radius and lower envelope split the square-root term before applying the weighted inequality.
4. **Keep GD's one-sided zero-purity decoder claim after signed finite/noise errors and packing.** Invalid: reconstruction may create positive mass at zero coordinates. Symmetric inverse error and confidence subtraction are necessary; the diagnostics include empty clean rows with false reconstructed mass.
5. **Clip only after the external fault.** Insufficient to establish pre-fault cube membership. The accepted MG clarification requires exact final working-lattice clipping before the fault, paid in d before selecting P.
6. **Transfer JP001's fixed-uniform-bank precision lower to the new encoder.** Invalid: the coarse-label experiment changes. Only the source-edit/full-history lower transfers universally through information reduction. The construction-specific scalar R and universal D=RK³ alphabet exponents remain distinct.
7. **Output on the original coarse Q grid for free.** Its additional O(K/Q) loss generally destroys the packed gain; output is a paid finite rational simplex vector unless separately fine-rounded.

No genuine failed numerical case occurred in the new main RE001 diagnostic run. This statement does not promote finite tests to a universal proof. Auxiliary binary radical checks use floating tolerance, while main radical checks use exact squaring; both evidence types are retained and identified.
