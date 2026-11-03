# Certificate-free binary order-two full-history question: already closed negatively

2026-11-03. Local audit/corollary, not a new root acceptance, publication, or novelty claim. No external writes.

## Result first

There is no family of predictors, indexed only by horizon, which attains a universal constant times `M^(-1/2)+k/M` for every homogeneous binary order-two source, arbitrary initial pair, and source-independent strict-k whole-word corruption preserving the last two symbols. Full corrupted history and unlimited computation do not help. **This follows directly from already accepted AB001**, rather than from the new counterexample to a particular half gate.

A precise useful corollary is that the worst-case factor relative to `g_M(k)=max(M^(-1/2),k/M)` is Theta(log M) for this certificate-free full-history class. The upper is the ordinary empirical predictor and universal occupation bound; the lower is AB001. This is a normalized-risk statement, not a claim that log M is the price of not knowing k relative to the certificate-free known-k minimax risk.

## Prior obligations read and provenance

Read the complete recovered AB001 proof and full independent review; AB001 acceptance receipt; recovered FOC001 `first_order_positional_probe/ORDER_ADAPTATION_CANDIDATE.md`; the richer-count first-order consolidation; O2T001; and the universal occupation/empirical portions and certificate interfaces of the positive supplement. FOC001 explicitly already says full-history joint budget/certificate adaptation fails for general order two. The first-order theorem and critical-certificate order-two theorem do not remove this obstruction.

Authoritative recovered proof:
`../../resumption_20261103/remote_recovery/files/v10_research/binary_budget_adaptation/AB001_joint_blindness_obstruction.md`.
Its SHA256 is `865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d`, exactly matching `../../resumption_20261103/remote_recovery/files/v10_research/intake/AB001_acceptance.json`.

**Original/public review provenance reconciled:** the recovered public review `review_joint_blindness_full.md` hashes to `a87760d42e80ca57631abf3096a8b1c84a5627995f1b0561817973a91a030170`, whereas the original acceptance receipt records `07050ce099a0e1770f0dd4b59c11911938e1bed798246c23256093d25f4629c5`. This is an explicitly recorded privacy-reconciled export, not an unexplained mismatch. Both `../../resumption_20261103/remote_recovery/files/provenance/increment3/BINDING_RECONCILIATION.json` (entry at lines160–169) and `INHERITED_DEPENDENCIES.json` (entry at lines122 onward) bind these two hashes to the same review path and say to reuse the existing export. Those entries were read directly. This audit does not claim the original private review bytes were recovered. The public review identifies the exact matching proof hash and PASS verdict; the mathematical proof was also reread directly. Historical candidate labels do not supersede the accepted proof receipt.

## Exact finite lower reduction

For any one randomized predictor A_M on the full observed word, let Lambda_M(A) be its supremum risk/g_M(k) over all certificate-free binary order-two sources, all initial laws, all legal kernels, and k=0,...,M. Put T=floor(M/8). AB001 proves, for its stationary alternative family and a single legal kernel C_(M,k),

`R_*(A,C_(M,k)) >= [(3k/(1024M)) log((T+1)/k) - (8/3) S_M(A) log(2T/k)]_+`,

where S_M(A) is the supremum clean risk over its stationary alternative family. For every integer sqrt(M)<=k<=T, both families are in the current certificate-free class, so

`S_M(A) <= Lambda_M(A)/sqrt(M)`, and `R_*(A,C_(M,k)) <= Lambda_M(A) k/M`.

Because a positive-part lower bound also implies the untruncated lower bound, rearrangement gives the entirely finite inequality

`Lambda_M(A) >= [(3/1024) log((T+1)/k)] / [1+(8/3)(sqrt(M)/k) log(2T/k)]`.       (CF1)

For sufficiently large M, k=floor(M^(3/4)) is admissible, the denominator tends to one, and the numerator is asymptotic to `(3/4096) log M`. The bound is uniform in A, so it survives an infimum over all predictors. In particular no universal bounded factor exists. The sum-versus-max normalization differs by at most two.

There is no illicit requirement that a predictor adapt to a supplied beta: the current class has no beta input whatsoever. Both prior witness families simply belong to it. Stationary initial laws suffice; a uniform guarantee for all deterministic initial pairs would imply the stationary guarantee by averaging.

## The actual source-independent attack (not a count-only collision)

Use r=1/(2M). The stationary clean alternatives have

`theta00(1)=a, theta01(1)=r(1-a)/a, theta10(1)=a, theta11(1)=1-r`,
`Pi_a=((1-a)/2,a/2,a/2,(1-a)/2)`, with `1/M<=a<=1/4`.

The stationary null is the first-order symmetric flip-r chain, whose pair chain satisfies the all-state certificate 1/M. Its one-flip words are `x^(t)=1^(M+1-t)0^(t+1)` and each has probability `(r/2)(1-r)^M >=1/(8M)`.

For public M,k and observed x^(t) with k<=t<=T, the kernel draws an auxiliary parameter uniformly from `[k/(8t),k/(4t)]`, simulates t symbols from pair10 with that parameter's displayed table, and accepts only if the continuation never reaches11, ends00, and has at most k ones. It then replaces only the t originally zero symbols. Otherwise it returns the original word. It is identity on all other inputs. Thus it is one map defined on every word, reads no true source parameter or predictor seed, has at most k substitutions on every realization, and preserves the final pair exactly. Its auxiliary table is part of the fixed attack recipe, not oracle access to the unknown source. Continuous auxiliary mixing defines an ordinary kernel on a finite word space.

Acceptance probability is at least1/4, by comparison with the no-consecutive-ones reference continuation: terminal00 probability >=9/16, budget failure <=1/4, and coupling failure <=1/16. The accepted output is the full word used in the clean alternative risk, not only its counts. The null target is still r at its actual final pair00. Integrating clean errors over auxiliary a and all suffix lengths is exactly AB001's proof of CF1's input inequality; no estimator information restriction is introduced.

## Matching elementary upper for the normalized factor

Let J,C be the clean departure/one-successor counts for the actual terminal row, and J',C' the corresponding corrupted counts. Output C'/J' if J'>0 and zero otherwise. This is a single budget-blind map and needs no certificate. The final pair is protected, so row selection agrees. Each edit changes at most three triple indicators; retain the accepted conservative bound `|J-J'|,|C-C'|<=6k`.

For J>0, a deterministic ratio comparison gives

`|qhat' - C/J| <= min(1,12k/J) <= min(1,24k/(J+1))`.

When J'=0, J<=6k, so the same unit bound covers that case. The clean empirical lemma gives expected loss on J>0 at most512/sqrt(M+1), and `P(J=0)<=16/(M+1)`.

Write N=M+1 and b=384k/N. The universal actual-terminal occupation bound implies, for x>=1,

`P(J+1<=x)<=16x/N`.

Layer-cake integration therefore bounds `E min(1,24k/(J+1))` by `b(1+log(1/b))` if 0<b<=1 and by1 otherwise. No independence of J and empirical rows is assumed. Consequently, for 1<=k<=M,

`R <= min(1, 528/sqrt(M) + 384(k/M)[1+log(M/k)])`,                  (CF2)

and for k=0, `R<=528/sqrt(M)`. Thus `Lambda_M <=528+384(1+log M)`. Together CF1 and CF2 establish Theta(log M) asymptotically. Constants are conservative bookkeeping, not a new research direction.

## What is and is not necessary

The exact condition P²>=Pi/M is sufficient and excludes AB001's problematic clean alternatives, but this does not prove it is logically necessary for every useful subclass. First-order sources already show it is not necessary source by source. What is established is that dropping all structural restrictions and retaining one unknown-k predictor cannot preserve the target O(M^-1/2+k/M), even with full history.

The separate sticky-cycle example below diagnoses the half gate itself. It does not establish all-estimator impossibility; CF1 does. The newly requested no-certificate question should not be reopened as an unsolved predictor-design problem. A genuinely different next question would require an explicitly intermediate source class or supplied-parameter experiment, with prior results checked first.
