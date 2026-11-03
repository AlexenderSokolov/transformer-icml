# Independent adversarial review: BSC likelihood-transfer lower bound

2026-11-03. Reviewer: `challenge_bsc_likelihood_bound`. Local mathematical review; no external writes. This review was derived independently, before reading the parallel author's new proof. **Verdict: the proposed logarithmic necessity is valid under the stated fixed-length fresh-BSC observation model.** This is not a claim to have reviewed the parallel author's artifact, nor external/formal verification.

## Inputs actually read in full

1. `recovered_science/first_order_positional_probe/triple_access/FOT001_candidate.md`, SHA256 `700db043416260a3d7e4796d6513ee60b90c2f2704a4d183be526d2aef9fef1d`.
2. Its `review/independent_analytic_review.md`, SHA256 `a80890e1ef23997ae2adeb72d004f40897cd139b9ef4b7431858767ac41d0eb9`.
3. `recovered_science/binary_mixture_window/window_preserving/WPC001_window_preserving_canonicalization.md`, SHA256 `a8328eb7907e20c006314e198948168b9d1da4045932d10c611dcfab42b566a6`.

The original source uses N ordinary edges, M=N−1 editable positions/triple departures, and N+1=M+2 raw symbols. We keep this indexing. Set r=2 in FOT001. Although its baseline then also includes the first pair, proving a lower bound with that extra free observation proves it for the requested weaker baseline (triple counts and protected last pair).

## Observation and randomness quantifiers

Fix N and one law-independent encoder/decoder scheme, independent of unknown k. The encoder sees only the corrupted word and outputs exactly R bits. The channel flips these bits with fresh independent Bernoulli(η) noise, η in (0,1/2). The decoder sees the exact baseline and noisy R-bit string. Shared encoder/decoder random seeds are allowed if independent of source and attack sampling. Independent private randomness is allowed. The scheme may depend on N, η, the supplied certificate, and design constants. All risks below average all source, attack, seed, encoder, channel, and decoder randomness. Nothing is conditioned on a favorable random seed in the final risk assertion.

A shared seed U can be conditioned on. For each u let E_u(z|w) be the encoder kernel, H_u(v|w)=sum_z E_u(z|w)W(v|z), and D_u be the decoder kernel. Correlated private encoder/decoder randomization can be subsumed by enlarging the shared seed: supplying independent design randomness to both parties only strengthens their capabilities. All seed laws are the same under the clean and attacked experiments. No source-dependent uncharged auxiliary observation is permitted.

## Elementary channel domination: no common-component loss

For each channel output v and every pair of codewords z,z',

    W(v|z)/W(v|z') ≤ κ,      κ=((1−η)/η)^R.

Indeed the coordinate likelihood ratio is at most (1−η)/η; multiplication gives the bound. Every W(v|z)>0. For any two distributions p,q over codewords,

    sum_z p(z)W(v|z) ≤ κ sum_z q(z)W(v|z).

This follows directly from max_z W(v|z) ≤ κ min_z W(v|z), and does not require a coupling between p and q. Thus H_u(v|w) ≤ κ H_u(v|y) for every u,w,y,v, including randomized and path-dependent encoders. The reverse bound also holds but is not needed.

Let b(y) be the exact baseline and w=C_2(y). WPC001 gives b(w)=b(y), even if the augmented baseline includes the first pair. For fixed u,v, average decoder randomness and denote loss against the alternative target by l_a(u,b(y),v), and against the null target by l_*(u,b(y),v). On F, both true terminal symbols are zero. Their target TV distance is a−β, where β=1/(N−1). The ordinary unsquared TV triangle inequality gives

    l_* ≥ (a−β) − l_a.

First integrate this inequality under the ATTACKED channel H_u(·|w). Its constant target-distance term remains exactly a−β, since the channel has total mass one. Only then dominate the NONNEGATIVE clean-target loss:

    E_U sum_v H_U(v|w) l_*
      ≥ (a−β) − E_U sum_v H_U(v|w) l_a
      ≥ (a−β) − κ E_U sum_v H_U(v|y) l_a.

Write the last clean loss as ell_a(y). This is the critical distinction from transferring the entire null risk, which would unnecessarily shrink the positive target gap by κ^{-1}. A common component is unnecessary.

## Reusing the legal original attack, with correct sign ordering

Use exactly FOT001's null, ν_j, μ_j, single proposal, acceptance test, and deterministic C_2. The attack depends on N,k and the predeclared auxiliary alternative family but not the actual source, encoder, or seed. It is legal even in a class that disallows any seed access. Its pointwise budget is at most k, and it protects the actual final pair on all inputs, including rejected proposals and zero-mass labels.

Let S=sup_{a∈[At,1/4]} R_clean(Q_a) for the FIXED scheme. The original nonnegative transport steps remain valid before using any signed bound: discard unused null inputs and rejected proposals; replace v_j/μ_j by ρ=u0/(8Nt) on nonnegative null loss; restrict to F∩G. Now apply the displayed channel triangle bound. The result is

    R_null ≥ ρ ∫ [ (a−β) Q_a(F∩G)
                         − κ E_Qa[1_(F∩G) ell_a(Y)] ] da/a
           ≥ ρ (t/64 − κ S)L.

Here c=2^-16, A=2^12, t=ck/N, u0=floor(ck/4), and L=log(4N/k), precisely as in FOT001. Its unconditional clean risk controls the restricted nonnegative loss; no conditional risk or fixed favorable seed is substituted. Nonnegativity yields

    R_null ≥ ρ[(t/64 − κ S)L]_+.

The actual corrupted output is w, not y. No false equality of encoder outputs or BSC distributions is assumed. Only equality of their exact baseline and bounded channel likelihood ratios is used. The null input x^(j) need not have y's counts; as in the original proof, its J00 is j−2, not j.

## Explicit constant-factor contradiction in the original horizon

Suppose the scheme has R_A(Q,K) ≤ C g_M(k) simultaneously for all allowed sources, all legal attacks, and all integer budgets, with fixed finite C>0 independent of M. This includes k=0 with the identity attack, so

    S ≤ C/sqrt(M) ≤ 2C/sqrt(N).

Set k=ceil(N^(3/4)), r=2. For N≥2^80 all FOT001 finite assumptions hold (enlarging N if desired avoids equality at an endpoint). Also k≤2N^(3/4), u0≥ck/8, and ρ≥1/64. If κ≤N^(1/8), then

    κS ≤ 2C N^(-3/8) ≤ (c/128)N^(-1/4) ≤ t/128

as soon as N≥(256C/c)^8. Hence

    R_null ≥ (c/8192)(k/N)L.

Since k≥sqrt(M), g_M(k)=k/M, and M/N≥1/2,

    R_null/g_M(k) ≥ (c/16384)L
                  ≥ (c/65536)log N = 2^-32 log N.

We used L≥log(2N^(1/4))≥(1/4)log N, paying the ceiling and horizon conversion explicitly. Thus log N>2^32 C contradicts the assumed constant C. One sufficient threshold is

    N > max{2^80, (256C/c)^8, exp(2^32 C)}.

The gigantic threshold is only a finite certificate, not a sharp practical constant. Consequently for every fixed C and sufficiently large N, a C-factor scheme must obey

    R > log N / [8 log((1−η)/η)].

With N=M+1 this is Ω_η(log M). It is a sequence/uniform-factor assertion: for each finite C a threshold N0(C,η) exists. It does not say that every small finite N requires the same asymptotic lower bound, nor allow C=C_N to grow silently. The supplied mixing certificate remains β=1/M. Arbitrary-initial-pair classes contain all stationary witnesses used here.

## Adversarial cases checked

- **Randomized codebook:** domination is uniform over every pair of mixtures; arbitrary stochastic encoders are covered.
- **Shared encoder/decoder seed:** condition on the independent shared seed, prove domination there, then average. Replacing the seed-conditional clean risk by an unjustified uniform bound is not needed.
- **Seed-dependent attack:** unnecessary. The exhibited attack is seed independent. Allowing stronger attacks cannot defeat this lower bound.
- **Source-independent kernel:** original ν_j integrates a fixed parametric family once; it does not consult the actual source. No encoder access is used, although dependence on a fixed public design would not by itself violate source independence.
- **Different channel input for every path:** explicitly allowed. Channel outputs for y and C_2(y) need not agree; they are compared by domination. A genuinely different channel law beyond the fixed fresh iid BSC is a different model.
- **Zero-probability outputs:** none for fixed R and η in (0,1/2). R=0 gives a singleton channel and κ=1. The endpoints η=0 and η=1/2 are outside the statement; the former invalidates this finite domination, the latter conveys no word information and has κ=1.
- **Unknown-law oracle:** excluded. A decoder given law-dependent unnoised information would have different decision kernels across the two experiments, so the common triangle step would not prove anything. A fixed law-independent full-word encoder is allowed in full generality.
- **Variable length, noiseless seed carrying word data, fresh noise leaked to decoder, or extra uncharged transcript:** not covered; these change the observation model. Independent shared seed alone cannot carry word data.
- **Sup clean risk and minimax quantifiers:** the same fixed scheme is evaluated for all a, null, attacks, and k. An infimum over all such schemes preserves the lower bound; attainment is not assumed. A scheme told k could choose a different clean decoder and invalidate the tradeoff, which is why k-hidden is essential.
- **Strict-k terminology:** the original proof uses pointwise at-most-k edits, not exactly k flips. If “strict-k” were newly intended as exactly k, the reused attack would not establish that changed claim; retain the original pointwise-budget definition.
- **Target/loss:** actual-terminal unsquared TV is essential to this direct triangle argument. The protected final pair makes the clean and null target rows comparable at terminal zero. No squared-TV substitution is made.

## Scope of verdict

I find no counterexample or mathematical gap in this lower-bound extension under the explicitly stated model. Together with an independently valid O(log M) upper construction it would close the bit-order threshold. I have not checked that upper construction in this review, and do not certify the parallel author's unread draft. The result is a sharper lower bound than the common-component Ω(log log M) argument, not a consequence of that weaker argument alone.
