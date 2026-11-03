# Source-bound independent review of CHANNEL-LIKELIHOOD-LOWER

2026-11-03. Reviewer `challenge_bsc_likelihood_bound`. **Favorable review of the actual current candidate, including its finite constants and matching upper interface.** This is a local independent LLM review, not formal verification, external peer review, root acceptance, or publication permission. No source files were edited.

## Actual read scope and binding

I read the entire actual `CHANNEL_LIKELIHOOD_LOWER.md`, SHA256 `d410a88fa63ae0de06bb7140296f85fc0ca3fa7b63c8bed8964fec81a4b9072e`, after my separate independent derivation. This review is consequently distinct from `independent_bsc_likelihood_challenge.md`, which deliberately did not certify an unread author artifact.

I also read, in full:

- FOT001 candidate and its independent analytic review, and WPC001 deterministic proof, as bound in my prior review;
- FOU001 `first_order_positional_probe/UPPER_CANDIDATE.md` and its `upper_review/REVIEW.md`;
- all 769 lines of `positional_manuscript_20261102/sections/proofs_positive.tex`, including the actual universal occupation, stack empirical, return/hitting, tilted joint-tail, generic imbalance, deterministic gate, half-reciprocal, and weighted-minimum proofs;
- FOT002 `triple_access/FOT002_matched_original_experiment.md`;
- existing FOT003 `triple_access/BOUNDARY_RECONSTRUCTION_NOTE.md`, its `boundary_review/REVIEW.md`, and its restored root receipt;
- the current new proof's history README, reconstructed before text, and actual-terminal-loss diff. The full before text is redundant with the current proof except for the two inspected difference regions.

`source_bound_checks.json` records hashes of the current author proof, actual upper/interface proof sources, history, and complete generic proof source. `source_bound_bindings.json` additionally binds the lower and FOT003 dependencies and this review's declared source set. No claimed PASS rests solely on acceptance receipts or finite checks.

## History provenance and actual-terminal correction

The current definition of ell_a is the true clean loss at the actual last symbol, simplifying to the a-row only on F. Therefore S is genuinely an unconditional clean risk and S≤Γ_N/sqrt(N) is valid. The reconstructed before text instead defines loss against a globally; taken literally that would not support the clean-risk comparison. The repair is substantive and sufficient.

The history README explicitly states that the before file was **reconstructed by reversing two actual edits**, not captured as a contemporaneous pre-edit filesystem snapshot. I inspected the byte-level comparison: its only differences from the current source are the actual-terminal definition and the erasure-channel limitation/list renumbering. The supplied diff matches those regions. I did not witness the initial author write, and do not independently certify its historical bytes beyond that declared reconstruction; this review neither invents nor relabels it as a preserved early snapshot. This provenance limitation does not affect verification of the present proof.

## Lower-bound proof verification

Sections 1–4 correctly fix a single code/decoder before taking the source/budget/attack supremum. The encoder is law independent and sees the post-attack word; a shared seed is independent and the BSC remains fresh conditional on all pre-channel information. The attack is the original single-proposal source-independent FOT001 kernel and ignores all scheme randomness.

For any output v, max_h W(v|h)≤κ min_h W(v|h), with κ=((1−η)/η)^R. Thus arbitrary mixtures at the two words obey the same domination. At common exact baseline and terminal 00, integrating the triangle inequality under the attacked channel preserves the target gap a−β. Only the nonnegative clean-target loss is then multiplied by κ. Conditioning and averaging independent shared seeds is legitimate and does not require clean risk bounded separately for each seed.

The imported structural lemma agrees with the actual FOT001 proof: the fixed ordinary-00 mixture label uses v=j+1; the null input has J00=j−2; C_r(y), not the null input, has y's exact baseline; the null mass and mixture mass give v_j/μ_j≥ρ; actual-distance/final-pair acceptance makes the kernel legal on every word. The displayed transport discards/reweights only nonnegative null losses before applying the signed triangle bound. The restricted true clean loss is bounded by unconditional S. Hence equation (8) is valid exactly as written. All-state certificate and stationary-witness inclusion remain unchanged.

## Finite normalized inequality and constants

For finite Γ_N, the clean identity kernel supplies S≤Γ_N/sqrt(N), while the constructed attacked null supplies R_null≤Γ_N g_N(k). Dropping only the positive-part strengthening of (8), moving its Γ_N penalty to the left, and dividing by k/N for k≥sqrt(N) gives

    Γ_N ≥ ρ c L / [64(1+ρ κ L sqrt(N)/k)].

There is no hidden assumption that t/64−κS is positive, and no need for an optimizer or any interchange of infimum and supremum. Infinite Γ_N is immediate.

For N≥2^160 and k=ceil(N^(3/4)), every displayed FOT001 condition holds. In particular x≥2^104, 2≤k/128, k≤2N^(3/4)≤N/8, At= k/(16N)≤N^(-1/4)/8, and N/k²≤N^(-1/2)≤2^-80. Also floor(x/4) lies between x/8 and x/4, giving 2^-6≤ρ≤2^-5.

The ceiling yields L≥log(2N^(1/4))≥log N/4; k≥N^(3/4) yields L≤log4+log N/4. Writing s=log N, exp(s/8) dominates log4+s/4 at s=160log2 (1048576 versus about 29.1122), and its derivative exp(s/8)/8 exceeds 1/4 thereafter. Consequently L≤N^(1/8) throughout the stated domain. Under κ≤N^(1/8),

    ρ κ L sqrt(N)/k ≤ (1/32)N^(1/8+1/8+1/2−3/4)=1/32.

Replacing 1+1/32 by 2 is safe. The conservative resulting power is

    (2^-6)(2^-16)(log N/4)/(64·2)=2^-31 log N.

The original g_M with M=N−1 is at most N/(N−1) times g_N, so the corresponding factor is at least (N−1)/N times Γ_N, hence at least 2^-32 log(M+1). This verifies (9)–(11), not just their order. The schedule conclusion follows for any fixed bounded factor B after log(M+1)>2^32 B; it does not claim a bound uniform over growing B or a sharp leading constant.

## Complete matching-upper dependency audit

The actual generic occupation proof is pathwise-low-visit counting plus a decreasing worst-start suffix probability, so it is uniform over starting laws and does not require irreducibility. The Bernoulli-stack proof never conditions independent stack increments on the selected terminal row/count; it bounds a maximum over rows and uses tail integration. Reducing from four to two rows and replacing occupation constant16 by4 only improves the conservative 512/sqrt(N+1) bound.

The generic irreducible imbalance argument uses valid target-specific endpoint and lower/joint occupation tails. Its joint tail is established by an explicit stochastic tilted matrix and exact path likelihood, not by multiplying dependent endpoint and occupation probabilities. For binary first-order tables with positive flip rates a,t, h_0=B/t and h_1=B/a with B=max(1,a+t), and sum p_u q_u h_u=B≤2. Thus 288d times that sum is at most1152 for d=2. For a reducible one-absorbing binary table, the only nonzero flip-weighted terminal event equals a first-hit atom one step later and is bounded by2/(N+2); if both states absorb the weighted bias is zero. Periodicity poses no obstruction.

The deterministic gate proof uses protected row selection and safe perturbations |C'−C|,|J'−J|,|D'−D|≤6k. Its accepted/true ratio error is ≤48k/(J+1); false acceptance/rejection give the stated 6156k and3078k cutoffs, with zero counts covered. For the exact first-half gate, condition on the deterministic prefix, let its target count be j, and use the suffix occupation lemma on J_2≤1023j. Dividing by j+1 and summing two target rows gives

    E[1{J_half≥J/1024}/(J+1)] ≤ 2·2^3·1023/N=16368/N.

The two occupation tails contribute (36936k+8)/(N+1); the corruption constant is exactly48·16368+36936=822600<2^20. The clean empirical and imbalance terms satisfy512/sqrt(N+1)+1160/N≤657/sqrt(N)≤1024/sqrt(N) for N≥64. Thus FOU001's exact bit upper is justified by the full proofs actually read, including all starts and boundary tables, not just by its prior review.

FOT002 correctly drops raw X0, leaving M homogeneous transitions. Conditional on clean X0=b the induced suffix kernel prepends b, applies the original fixed kernel, and drops its first output symbol; it is legal, law independent, and has no greater budget. The same suffix predictor works for every b and averaging is valid. This conditional b is an analysis device, not a decoder input. Original terminal-pair protection is stronger than the suffix theorem's terminal-symbol protection.

The author candidate states the endpoint-pairs baseline. The requested baseline with only exact triple counts and protected final pair is already information-equivalent by **existing accepted FOT003**, not a new discovery in this review: out−in plus terminal one-hot recovers the corrupted initial pair, and directly

    N_ab(corrupted truncated suffix)=sum_d H_dab.

I independently rederived this before locating the restored FOT003 note, then actually read and bound that note and its review. This observation must be attributed to that existing interface. It establishes the same upper and lower with no separately supplied initial pair; no longer window or half-visit ordering is reconstructed.

## BSC majority wrapper

Let P0,P1 be the R-fold BSC output laws for repetition of zero and one. Fair-tie majority is symmetric Bayes testing, so its error for either sent bit is

    δ_R=(1/2)sum_v min(P0(v),P1(v))
        ≤(1/2)sum_v sqrt(P0(v)P1(v))
        =(1/2)[2sqrt(η(1−η))]^R.

The bound is uniform conditional on any corrupted path and its encoded gate bit. Couple the exact and noisy decoders using the same additional randomness: on correct decoding their actions agree, and on error their unsquared TV losses differ by at most1. Thus noisy risk≤exact risk+δ_R. Dividing by g_M≥M^-1/2 gives factor≤1024+2^20+sqrt(M)δ_R. The candidate length condition R≥log(sqrt(M)/2)/[-log a_η], rounded upward to an integer when positive, makes the last term at most1. R=0 is harmless when that numerator is nonpositive if a no-information fair tie is permitted; the theorem's M≥64 domain already makes it positive.

This completes the actual upper-and-lower proof chain for Θ_η(log M), under fixed η∈(0,1/2), law-independent fixed-length full-corrupted-word encoding, exact counts, fresh post-attack BSC, hidden budget, original arbitrary initial pair class, and actual-terminal unsquared TV loss. The endpoint cases and variable-η qualifications in the candidate are correctly separated.

## Supplemental checks and verdict

The local checks recorded in `source_bound_checks.json` independently verify 16,352 suffix right-margin identities for all binary words at M=1,...,9 and all four pairs; the finite denominator endpoint and power arithmetic; source hashes; and the exact before/current difference regions. They are corroboration, not the proof of the stochastic or asymptotic claims.

No blocking error remains in the current bound author source. The former global-a loss definition is corrected and its reconstructed history is transparently labeled. The sharper finite normalized inequality and Θ(log M) conclusion pass this source-bound mathematical review. Application to the final-pair-only baseline uses already restored FOT003, as stated above. No accepted sources, manuscript, or external repository were changed.
