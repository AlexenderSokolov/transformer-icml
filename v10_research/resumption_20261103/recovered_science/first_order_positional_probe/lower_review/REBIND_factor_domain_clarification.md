# FOL001 review rebind — finite factor-domain clarification

2026-11-02. Independent reviewer of the original FOL001 lower candidate.

**PASS: the original universal lower-proof verdict extends to the revised candidate. The requested standalone-definition clarification is resolved.** No substantive proof change was made. This rebind does not review or assume an upper theorem and does not alter the original `REVIEW.md` or original review manifest.

## Exact provenance checks performed

1. Read the actual before file, supplied unified diff, revision note, updated manifest, and the revised section 6 with its proof paragraphs and section 7 boundary.
2. The actual before file SHA-256 is `af005e4f3649c31cd6911225f348bf4f37586964e609a431bfcad59d2bbcc015`, exactly the candidate hash recorded in the original independent review manifest and original author manifest.
3. Applied the supplied actual diff to that before file using `patch --batch --fuzz=0`, writing a temporary reconstruction outside the source tree. `cmp` confirmed byte-for-byte identity with the current candidate. Reconstructed/current SHA-256 is `2393de755fda2bb385f2c64a16ef6733d69c76b6829eaf65d076fac1c539b511`.
4. Independent line-by-line comparison found exactly one changed line, line 128, with unchanged total line count.
5. Verified every digest in `lower/MANIFEST_after_factor_domain_clarification.json`. Also verified every original independent-review manifest binding other than the intentionally revised candidate. In particular, the original review, fresh check source/output, PLAN, and original author check source/output remain unchanged. The updated author manifest binds the unchanged historical author manifest and handoff too.

## Mathematical assessment of changed context

The replacement paragraph explicitly fixes integer N>=64 and integer 1<=r<=N+1; restricts the supremum to integer k in {0,...,N}; identifies stationary binary first-order sources and source-independent strict-k kernels protecting X_N; and defines Gamma_stat(N,r)=inf_A Gamma(A;N,r) for the stated observation, including randomized predictors.

This exactly resolves the original review's definition clarification. The unchanged proof already uses only k=0 for the clean floor and an explicitly constructed integer k<=N/8 for the contradiction, so the bounded supremum is sufficient. The unchanged argument establishes the lower bound separately for every predictor A, which passes to the displayed infimum without an attainment assumption. All finite constants, witness families, mixture identities, relocation steps, kernel construction, and loss inequalities are byte-identical to the audited proof. No new hypothesis, source family, or certificate is introduced.

The prior PASS verdict therefore binds to the revised candidate hash above. Scope remains the natural first-order binary pair-count observation with N departures, N+1 symbols, and one protected terminal symbol, normalized by max(N^-1/2,k/N). This is neither an upper/equality claim nor a result for the original triple-count experiment. Root retains acceptance/integration authority.

A separate `REBIND_factor_domain_clarification_MANIFEST.json` binds this report and all relevant provenance inputs. The historical original review and manifest are intentionally preserved rather than rewritten to hide the original definition omission.
