# Resource and execution-contract audit of public-source scalar-position alignment

2026-11-12. This is a separate resource/robustness audit, not a claim that the bit module solves prediction. The clean construction already passed its independent review. This audit distinguishes literal mismatches, exact repairs, and conditional execution bounds. The new robust formula received a separate independent analytical PASS; no noisy-network experiment was run.

## Frozen sources actually read

Repository AlexenderSokolov/transformer-icml, main commit `2ca64346e0dbb19ccf12b5c0f06f12cd0ff31a70`: `v10_research/execution_contract_prior_audit_20261106/RESEARCH_REPORT.zh.v2.html` (Git blob `b018dcbc9b80fbd992b3f9b02f7bb713835bd0f7`), embedded Frozen comparison contract, Architecture/Error sections; `v10_research/fixed_width_rare_risk_frontier_20261106/RESEARCH_REPORT.zh.v3.html` (blob `1d8e7d0df2888a03f74709fea500a4edc9bb5a37`), architecture, precision and complete-resource ledger. These were located through the exact commit tree and fetched from GitHub; older local HTML copies were not treated as byte-identical canonical sources.

Also read commit `03f91a4d0a4408dd1e520b8a0151e9ba38452176`, `v10_research/fixed_c_checkpoint_20261112/MEAN_FIELD_THEOREM.md`, Git blob `ab9f745a18ca74ad364be1b4a070097f26d42927`, Sections 1, 7, 8.

Construction reviewed: `CONSTRUCTION.md` SHA256 `3f546de8576087211fee415b1a10897b602faef0e92645e52ee2c23b53ba0e5a`, script SHA256 `d07d739d2d8bfb3d45e170fe8e85435e99a511fc50b3ddcef168326cec642b25`, as archived in the scalar-position alignment unit.

## 1. What the original contracts actually say

The execution audit fixes full-feature PreLN epsilon 1, gain 2, zero shift, N raw rows and a public synthetic terminal, full self-inclusive causal softmax, and an ordinary final affine-softmax probability output. It permits source-independent parameters depending on public length and accuracy budgets. Its sufficiently large state/matrix/bias/Lipschitz envelope is fixed before N varies, not an arbitrary tiny prescribed cap. Each row receives an arbitrary input-aware, adaptive vector of Euclidean norm at most 2^-p after EVERY attention residual and EVERY FFN residual. Inputs, positions, coefficients, internal arithmetic and final head are exact. Thus p is an absolute-disturbance-radius exponent, explicitly not storage, mantissa or coefficient bits. An upper must prove a bounded tube for every allowed policy.

The rare frontier likewise specifies gain 2 and a fixed complete state/value/operator/bias/primitive envelope, but it treats a different rare stationary source and conditional risk. Its precision categories must remain separate. The fixed-c checkpoint uses abstract common-domain state/Lipschitz bounds including actual LN constants, permits public positions, and explicitly warns that aggregate full-network Frobenius is different from per-layer budgets. Its adversarial-noise extension requires an explicit comparison budget; it is not automatically exogenous noise.

## 2. Literal mismatches and exact repair

The published bit module uses gain 1 at every LN, not the old gain 2 convention. It is therefore not literally an instance of that exact parameterization. An exact repair is available: replace each LN gain 1 by gain 2 and divide each immediately consuming first FFN matrix, attention value projection and final bit-readout functional by 2. Keep hidden/output biases and second FFN/output matrices unchanged. Q=K=0 remains zero. Every residual map and final bit function is then identical on all physical states, not just clean trajectories. LN gain norm becomes 2 sqrt(14). This is an algebraically justified reparameterization; the published binary64 script tests the original gain 1 implementation, not this parameter array.

More importantly the final functional 5 LN(v) is a bit readout, not an ordinary vocabulary-softmax probability head. No risk/output compiler follows just by reparameterizing gains. One public source j may depend on N and is source-independent, which is compatible with public-length parameter choice; simultaneous per-row predecessor recovery is absent.

## 3. Occurrences, storage and all-row computation

For D actual standard blocks plus a final LN, there are 2D+1 LN gain vectors. Their exact squared Euclidean occurrence contribution is 28D+14 at unit gain, or 112D+56 at gain 2. Thus a depth-independent aggregate concatenated parameter norm is already impossible for this implementation, even before FFN weights. With fixed-width allocated matrices, total occurrence slots and sum of squared parameter norms are Theta(D), aggregate norm Theta(sqrt(D)). Repeated identical coefficient values may reduce unique stored parameters but do not remove charged occurrences or executed layers. Untied descriptions using O(log N) bits for public thresholds have a conservative O(D log N) bit bound; this is not a necessity and tied descriptions may be smaller. The arbitrary precision tolerance eta is reflected in D as well.

All N+1 physical width-14 states exist, so persistent state count is Theta(N), not constant. Pointwise execution takes O(ND) fixed-width arithmetic work. A literal dense causal attention realization allocates/work Theta(N^2) for its useful read; an exactly equivalent uniform-prefix-sum implementation takes O(N), but its arithmetic schedule must be declared in finite arithmetic. Dummy zero attention may be computationally optimized, yet the original error contract still injects after its residual site. Depth is not total runtime.

## 4. Position and coefficient precision are separate from residual p

p_i=i/N and t_±=(j±1/2)/N have O(log N) rational descriptions, but are not generally finite dyadic values. The original adversarial execution contract makes them exact. The clean sign margin before amplification is at least 1/(8N sqrt(45/28)). Consequently a constant-size positional/threshold rounding error cannot simply be ignored. O(log N) fractional resolution with a sufficiently small constant protects the initial classification signs; a full final-accuracy certificate must also propagate initialization/coefficient errors through the remaining maps. If every initial row is perturbed by e0 in Euclidean norm, a conservative propagated contribution is Lambda^(2D)e0. Rounding every input coordinate or every parameter is not part of the old residual-only model and must be separately proved. Storing an explicit N-position table costs O(N log N) rational-description bits, while a public formula may use a succinct description; neither accounting should be silently substituted for the other.

## 5. Explicit full-state adversarial sufficient bound

Let 0<eta<1. Build the clean module at accuracy eta/2 and let D be its actual block count. In max-row Euclidean norm, every residual map has global Lipschitz constant at most Lambda=3000. For unit-gain epsilon-1 LN, the Lipschitz constant is at most 1 on all vectors. ReLU is globally 1-Lipschitz, so every FFN residual is globally at most 1+||W2||_F ||W1||_F Lipschitz. Specifically the threshold bound is 1+.801 sqrt(8), the two-register amplifier is at most 1+sqrt(320), the scalar amplifier at most 1+sqrt(80), and the gate at most 1+40 sqrt(4008)<3000. These bounds cross all plateau and amplifier boundaries and do not assume a fixed ReLU activation pattern. Uniform averaging is 1-Lipschitz in max-row norm, giving attention-residual bound 1+sqrt(2)<3. Zero-attention residuals are identity maps but still receive the prescribed errors. The gain-2 reparameterization has exactly the same residual maps. These bounds are independent of N and do not require perturbed states to remain paired or mean zero.

There are 2D perturbed residual sites, INCLUDING zero-attention sites. Final LN, head, coefficients and internal arithmetic remain ideal. If each site has max-row error <=delta, comparison with the clean execution gives

    e_(2D) <= delta sum_(r=0)^(2D-1) Lambda^r
           <= 2D delta Lambda^(2D-1).

It suffices to choose

    delta <= eta/[20D Lambda^(2D-1)],
    p >= ceil(log2(20D/eta)+(2D-1)log2 Lambda).

Then e<=eta/10 at every site. The final bit functional is 5-Lipschitz, so total bit error is at most eta/2+5 eta/10=eta. Every physical perturbed row has norm <=sqrt(16.5)+eta/10, not merely bounded centered norm. A once-fixed envelope H=sqrt(16.5)+1 therefore suffices for every such policy. This gives p=O(log N+log(1/eta)) as an error-radius exponent, with very conservative constants. It is not an executed floating-point certificate or a storage-bit theorem. A prespecified H below the required tube is not certified.

For illustration only, eta=1e-5 and the displayed schedule give (N,D,p_sufficient)=(2,59,1379),(8,62,1448),(128,72,1679),(512,78,1818),(1000000,106,2465). These are deliberately loose analytic Lipschitz budgets, not empirical precision thresholds. Five in-memory arithmetic assertions checked the error-budget inequality; no noisy-network experiment was run for this audit.

## 6. Two distinct necessary warnings

At the only nonzero attention residual, the synthetic terminal has broadcast pair (v,-v), v=c_j X_j/(N+1), with c_j>0 public. An input-aware error (-v,+v) on that pair costs exactly sqrt(2)c_j/(N+1). If the permitted delta reaches that value, this policy makes terminal broadcast zero. Every subsequent block is row-local and the scalar amplifier preserves zero; final bit output is 0, hence error 1 for every source sign. Thus robust bit accuracy eta<1 for this particular implementation requires delta<sqrt(2)c_j/(N+1), equivalently p>log2(N+1)-log2(sqrt(2)c_j). This attack reduces the terminal state norm and does not rely on leaving the physical envelope. It is a module-specific deterministic bit statement, NOT a statistical prediction-risk lower bound.

Separately, full-vector LN ignores rowwise mean shifts. Injecting delta times the unit all-ones vector at every residual produces exactly 2D delta accumulated mean displacement, while final LN output is unchanged. Since clean rows are centered, physical norm along this policy is sqrt(||h_clean||^2+(2D delta)^2). Any fixed all-policy raw-state envelope requires 2D delta<=H. Therefore fixed positive delta cannot support arbitrarily deep physical-state admissibility, even though the pure-mean policy causes no prediction error. For D~log N this warning alone only forces p>=log2 D-O(1), much weaker than the seed attack. A policy restriction excluding tube exits is not the same as proving all allowed norm-bounded errors stay in the tube.

## 7. Verdict

The clean result is a genuine fixed-width, bounded-per-layer, logarithmic-depth single-public-source alignment module. Under the original residual-only error model, an explicit sufficiently small logarithmic-order p and a sufficiently large raw-state H can be certified as above, after accounting for all sites. Exact gain-2 reparameterization repairs one literal mismatch. It still lacks the required statistical estimator and ordinary final probability head. It is not an instance of a fixed aggregate all-depth parameter budget, a constant-noise robust module, or a finite-machine precision theorem. No general network risk conclusion follows from its local erasure attack. The source documents themselves keep these precision and resource notions separate; the audit does not change them.
