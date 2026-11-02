# Independent audit — CF001 v1

## Result first

**ACCEPT for the precisely specified finite-evaluator encoder family and finite parameter domain. No mathematical or interface blocker found.** This is an independent review of the new upper-witness membership and downstream transfer, as well as the lower/completion synthesis—not acceptance merely because CA001 and FA001 were accepted. It is not certification of an emitter, a fixed-depth PURE implementation, arbitrary Transformers, training, resource optimality, or novelty.

Frozen target: `v10_research/causal_attention/CF001_finite_causal_risk_frontier_v1.md`, SHA256 `b87da8c885adf3ec519bc6d85fea8049ee17e89bd56a8babc246aaf7ae22af95`. All target/source manifest hashes were checked. No frozen source was edited.

## 1. The new witness really belongs to the stated ideal subclass

The singleton-copy effects are absorbed into explicitly permitted causal radius-three initial tables, not smuggled in as sparse attention inside the recursive architecture. A historical state needs the token, its two predecessors, the first-key-gated predecessor vector, and the flag, all bits. These are local, with public short-row fallback. The terminal query uses only its permitted exact boundary label; it does not insert the future symbol. The first flag's gated vector is `z_t e_(X_2)`, which at its sole nonzero row t=3 is a legitimate local predecessor feature.

For P1/P2 the Q and K projections give precisely the two one-hot matching terms; T and uniform heads give the remaining listed SRC comparisons. Log coefficients are dyadic and less than two. Values are coordinate projections, not hard query-dependent selection. There are 2K+2K+2K+(3K+1)=9K+1 output coordinates, fitting width 12K+4. Output concatenation is affine with row norm one and is 1-Lipschitz for the sum of input-head norms. State norm one, score cap two, coefficient row bound two, and score Lipschitz bound 4K suffice on all formal histories. These are proved primitive properties, not the desired information-theoretic conclusion assumed as a hypothesis.

Masks have sizes 1 at t=1,2; t−2 at 3<=t<=N; and M at n=M+3. Every size is at least t/3. They are public, branch-independent, and source-independent. Identity padding is legal: the update copies the previous state while ignoring zero-valued heads; it does not require softmax to implement an exact identity. Its finite 0/1 affine coefficients and aligned grid make those copies exact. Additional zero output coordinates preserve membership and are charged.

Historical tables/parameters are independent of the actual future boundary. Reading that boundary first in an offline implementation does not itself introduce functional anticipation: the only encoder use is the terminal query. The stronger branch-frozen class used in the lower proof need not itself be temporally causal. CF001 correctly distinguishes these statements. A larger allowed boundary window requires its own fixed branch count; `3^6` is sufficient only for the stated six-symbol window, as the text expressly says.

## 2. Source precision and actual closed-grid master contract

The source precision is p0=4h+4ceil(log2(M+K+4))+64, matching the SRC/NB002 word parameter, not FA001's fractional precision. SRC's rational series is finite and gives each downward log error <2·2^−p0. A P1/P2 logit changes by at most 4·2^−p0; softmax's L1 differential bound gives at most twice that discrepancy in total weight variation. Bit values therefore give head-coordinate error <=8·2^−p0<=1/(8Q). This last inequality follows already from p0>=h+6, with very substantial slack here.

FA001 at target h+3 independently supplies pre-cut error <=1/(8Q) relative to the dyadic-coefficient ideal network. Parameter conversion may truncate the longer p0-bit descriptions; this is covered by FA001 and is not an assertion that p0<=P. Final downward Q-rounding contributes <1/Q. Hence the total true-log-head discrepancy is <5/(4Q)<2/Q. Agreement of old and new rounded labels is neither implied nor needed.

The separate range proof is essential and valid. Initial bit tables are exact. The first global block's value projections use only 0/1 coefficients, so each finite value is an exact bit. FA001's positive shifted Taylor weights and full numerator sums give a weighted average in [0,1]; floor to its fine grid remains in [0,1], including both endpoints. Concatenation, identity padding and projection preserve these grid values exactly. Final coarse floor remains a closed [0,1] Q-grid word. Thus the new bank satisfies the old suffix's legal-domain premise, not merely an error bound near that domain.

## 3. Direct attack on the NB002 transfer: it passes

I read the actual SRC §§2,4–8 deterministic construction and NB002 §§2–6,8–9, and checked the AU001 pre-integration reduction. The decisive SRC §7 hypothesis is: **each statistical coordinate differs from its ideal value by at most η, lies on the closed grid, and exact side bits remain exact**. It is not a premise that coordinates were produced by SRC's old exponential recurrence. The proof explicitly permits arbitrarily correlated coordinate changes and does not even require each head bank to sum to one.

Re-deriving the ledger: `d1` and `d2` errors are 6η+ζ and 10η+ζ, `dT` error is η. The two T-flow expressions each cost 4η+ζ; the endpoint-selected rho term costs η; hence g costs 9η+2ζ. The two product-head expressions cost 10η+2ζ and 16η+2ζ. Subtraction and clipping give recovered-row error 35η+6ζ. With η=2/Q and ζ=1/Q this is 76/Q. Uniform-head pooling uses `nu−f+rho E`, with exact endpoint E and exact grid addition/bit multiplication, giving 3η=6/Q. The initial-pair correction uses the T h0 bank, not an ungranted clean initial-pair statistic.

All suffix divisions remain legal: the recovery denominators `2Q−U` lie in [Q,2Q]; normalized positive weights are `M a_c+1` and `M y_c+1`; ordered floor/residual normalization is a simplex vector even when Q<K. The old positive `r0` smoothing stage is not used. Thus no old Q>=M legality condition returns through this transfer.

NB002 next bounds actual normalized errors by `min(1,E/A)+K/Q` and `7K/Q`, where E=76KM/Q and A=J+K. Its observable `Aminus=max(K,Ahat−E)` satisfies `K<=Aminus<=A` and `Aminus>=A−2E`. The actual error allowance therefore dominates the sum of normalized-vector errors. Its inflated radius is at least the ideal radius; old pooling implies new pooling on every path, with ties preserved. Rejection containment holds for this new bank just as for the old one.

Away from A<4E, the same pathwise bound is `e+2rho+3 min(1,E/A)+9K/Q`; the bad event contributes one by the loss cap. Near IID, the actual rejection subset preserves S025's CT/GT selection argument rather than an invalid unconditional NEXT statement. In other parameter regimes NB002 uses retained count-radius/event certificates, not merely a final scalar R011 risk. No independence of arithmetic error, query, count or source is introduced. Consequently AU001's exact pre-integration occupation expression transfers. Its suffix-law mixture and occupation estimates concern the underlying source trajectory and J, not how the bank was evaluated. They therefore yield the advertised all-Q W surcharge for this new map. This is stronger evidence than simply importing AU001's literal theorem for the unchanged old program.

## 4. Complete message, timing and side ports

The lower's message is D grid words plus the finite boundary label S and fixed public metadata. The decoder is expressly denied old clean numerators/denominators, residuals, historical outputs and history rereads. The exact last pair and endpoint required by the final NB002 computation are functions of S; flags/types are public or represented in the master bank. No additional nonlocal statistic is needed.

All-token suffix execution is a cost convention, not extra information for the terminal decoder. Historical rows may use their own exact causal local endpoints, and need only be arithmetically legal, not statistically interpretable as an M-departure experiment. Their outputs do not flow to the requested terminal prediction. Retaining local endpoint registers until their own pointwise use and then releasing them is consistent with the final cut. Public coefficient descriptions and masks are source-independent, so access to them does not create a hidden history port. Quantized masters and S are counted together even if physical copies coexist.

## 5. Lower transfer, scalar completion and quantifiers

FA001's uniform formal-history error at h+3 gives E=1/8; relaxing to E=1 is safe. Enlarging the CA001 integer tube to radius tau+3 leads to `ceil(2tau+6)+1`, exactly CF001's N_E. This does not require intermediate rounded maps to be Lipschitz. Local radius and fixed density only alter uniform architecture constants. Branch freezing must cover inconsistent histories and CF001 explicitly requires it.

The stationary full-history IID floor, IID 1/Q message floor, and rare-suffix logarithmic floor are distinct simultaneous minimax inequalities. They are not added as if one source attained their sum. The decoder can output arbitrary real simplex vectors. Thus the 1/Q term here is a complete-message obstruction, not a falsely imported output-grid lower bound. Conditioning on source-independent shared randomness preserves the same uniform prior and uniform constants; averaging over the seed before the source supremum handles randomized encoders as well as decoders.

I checked the all-Q completion independently. For beta>1/16, `ln(1+x)<=2sqrt(x)` with x=Q/(M beta0) gives W<=1/Q+2/sqrt(M), using Q>=16. For the Q>M/4 region, x<=Q and `ln(1+x)<=4x^(1/4)` give W<=1/Q+4Q^−3/4<=5/sqrt(M) for M>=64. For Q>M^(3/4), the same inequality gives W<=5/sqrt(M). In the remaining region x<=Q<=M^(3/4), y=M/Q, and if x>y then x<=y³. Consequently `ln(1+x)<=3ln(1+min(x,y))`; Bernoulli's inequality gives the further factor eight. Retaining both cutoffs gives exactly CF001's 24 coefficient. Statistical floor constant 1/256 then yields denominators 1280, 1/c2+512, and 1/c2+24/c1 as stated.

All K>=3, M>=64, integer h>=4 and beta endpoints are covered; no limit or large-Q extrapolation is hidden. The stationary class inclusion has the correct minimax direction. The single beta-blind upper witness uses the inherited `L_stat<=K^(5/2)/sqrt(M)` and the two nonnegative terms are each bounded by their coefficient times H. This proves the displayed C_K. Neither source-law-dependent selection nor decoder beta blindness is needed for the lower.

## 6. Resources and interpretation

The result's encoder is an actual finite evaluator of a fixed-depth ideal architecture. Its bitwise/PURE expansion is not thereby fixed-depth. CF001 explicitly keeps these notions separate. FA001's P=4(h+3)+C_arch fractional precision is not the full word; full accumulator/product/counter widths pay log n and guards. Supplied p0-bit dyadic descriptions and their conversion/storage are separately charged. Compact converted parameter slots are P+O_arch(1), while workspace uses full w-bit slots; the alternative padded layout has its own charges.

The SRC rational log generator is explicitly added with its actual O(p0³ log²(p0+1)) work and scratch/output/code. Public tables or masks do not receive free generation or free compressed access. FA001's sequential scans, rewinds, QKV, all rows, full products, quotients and lifetime costs are retained. NB002's complete downstream arithmetic and all-token execution are added with its own p0/full-product/dense-zero/hold/normalizer/controller costs. This does not claim the composed prefix fits NB002's old 128p0 word allowance: that allowance belongs to the suffix; FA001 pays its own words. The proposed conservative sum is a valid upper accounting rule, not a measured tight ledger. Peak is a sum of simultaneous live components before maximization, not the minimum of two separate peaks.

No claim of an original emitted network, a six-head resource identity for arbitrary D, cheaper scalar-neural implementation, or advantage over paid direct counting follows. These restrictions are load-bearing and must remain in summaries of the result.

## 7. Diagnostics and evidence limits

The companion independent script checks compatible but arbitrarily perturbed closed-grid masters, SRC recovery, normalized error envelopes, observable denominator inequalities and monotone rejection. It also evaluates illustrative new positive-shift Taylor heads after finite downward log generation/conversion, rather than reusing the old prefix's exponential routine. A separate scalar sweep and mask-density sweep supplement the analytic audit. The chosen illustrative precision is not claimed to compute the general FA001 C_arch; the universal guarantee comes from FA001's proved constructive constant selection. These checks are finite corroboration, not a proof, statistical-risk simulation, emitted-network audit or performance measurement.

Diagnostic result: **PASS** — 912 arbitrary compatible-bank cases, 48 new finite-head cases, 50,000 scalar completion cases, and 500,292 mask rows; 37 cases exercised actual new rejection. No check failed. All ten declared source-manifest hashes and byte counts matched.

Disposition: accept CF1 with the exact family, boundary/cut restrictions, domain and implementation distinctions above. The absence of a universal Transformer, training, novelty, sharp joint-K or resource-optimality conclusion is not a missing proof of this stated theorem.
