# JP001 handoff — post-stage8 only

**Result:** fixed uniform K^3 histogram prefix, protected endpoint, k source edits plus one-shot vector l-infinity port noise delta and Q-floor: stationary AND arbitrary-start minimax are Theta_K(min(1,max(M^-1/2,f_e(k/M+delta+1/Q)))). Here e=max(beta,1/M) for K>=3 and max(sqrt(beta),1/M) for binary K=2. The finite uniform evaluator is exact at any P>=h, encoder independent of k/delta; upper uses finite rational certified-budget arithmetic and is beta-blind.

**Evidence:** complete theorem `JP001_theorem.md`; fresh independent full review PASS after one resolved certificate-encoding clarification; independent exact diagnostics rerun PASS. Final reviewed theorem SHA-256: c94e7d59d463a642853b8e3c52588f735c24175885f9cfddf05fbd8f3f2c0fab. Full review and all exact version hashes are separately bound. Root acceptance still required; no frozen or accepted source was edited.

**New useful precision detail:** the noise lower is exact for real shifts, D-grid shifts, and even fine-Q-grid shifts. The latter uses eta=floor(Qc a)/Qc−floor(Qa)/Q, avoiding any hidden need to subtract the D-grid remainder. Coarsening is a source-independent map of the actual finite bank. BF/BS family inclusions—not FR's distinct SRC interface—supply the noiseless precision lower.

**Limitations:** “one-shot” means a whole vector with bounded individual coordinates, NOT one nonzero scalar; no redesigned/deep-encoder universality, training, sharp-K/resource-optimality or unknown-budget adaptation. The physical injection/isolation device is outside the reliable bit-machine implementation. Optional output Q-rounding is separately paid/dominated.

**Review history:** an initial capacity error occurred after reviewer had already written its completed artifacts; resuming the same agent confirmed completion and final bindings. This did not substitute author judgment for independent review. The only required correction was full numerator+denominator bitlength for rho. All genuine distinctions and the fine-grid refinement are preserved in `JP001_issues_and_resolution.md`.
