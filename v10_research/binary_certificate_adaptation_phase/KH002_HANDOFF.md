# KH002 accepted exact histogram-domain classification handoff

Root accepted KH002 at2026-11-02 13:49:27.429240 UTC after reading the complete frozen proof and full fresh independent review. Authority: intake/KH002_acceptance.json. Historical candidate wording remains unchanged.

## Exact result and interface

The observation is **eight exact triple counts plus initial/final PAIRS**. Given any public domain E of integer M>=64 and supplied beta in[0,1], a family blind to actual k attains the known-k binary profile simultaneously for all0<=k<=M with one finite constant if and only if

    sup_E G(M,beta)<infinity,
    G(M,0)=0,
    G(M,beta)=min{M²beta,1/(beta sqrt(M))} for beta>0.

Equivalently the domain lies in some fixed union beta<=B/M² or beta>=1/(B sqrt(M)), B>=1. The same ordinary-add-one rule works throughout that union, independent of beta and the domain, for every initial law. Failure outside such a union already uses stationary sources. This allows sparse, irregular and oscillating domains; a subsequence suffices for impossibility. Constants and predictors may depend on the whole public domain.

The lower applies accepted KH001 at witness certificate beta_w=max(beta,1/M) to the SAME actual-beta estimator map. All source laws remain unchanged and qualify for the actual class by nesting. Their null target is beta_w, NOT beta; public predictor input and benchmark remain actual beta. The budget construction explicitly contains beta^(-1/2) to pay the actual-beta benchmark.

This does NOT classify unrestricted full histories, larger boundary windows or arbitrary local feature summaries, and does not prove that ordering suffices for adaptation. KH003's boundary-window extension is a separate candidate.

## Immutable proof, full review and diagnostics

- Proof KH002_histogram_domain_classification.md:970bfefb6041cdb989148819eb526c789d86591992375b84b05de2dd72bf9702.
- Fresh full review reviews/KH002_independent_full_review.md:4ae4315cc3fe19cfc020b040ae49b7485591806b46f636a7add2f85d38fed502.
- Root receipt binds both. Author initial snapshot and independent received snapshot are byte-identical. No KH002 proof revision occurred.

The author read the complete independent review. Author checks passed33 full finite budget/actual-beta cases,132 clean families,2,112 witness and2,112 actual certificate entries plus2,112 actual null entries, and210 union-membership checks. Fresh independent diagnostics passed31,408 exact assertions, including2,569 bounded-G/union equivalences,108 complete geometric-budget and15 slow/sparse/crossing cases,369 certified radical floors,375 stationary witnesses/6,000 entries at each certificate,75 nulls/1,200 entries at each certificate, and57 explicit target/metadata distinctions.

The first AUTHOR diagnostic run stopped with KeyError on an optional review_sha256 receipt field. The actual prior script, failure note and true one-line schema-guard diff are preserved in revisions/. No mathematical assertion failed, and no proof byte changed. The succeeding exact run is separately bound. These finite diagnostics are corroboration, not formal verification.

## Provenance and inherited scope

KH002_ACCEPTED_BINDINGS.json and build_kh002_bindings.py bind exact accepted proof/review/receipt, both snapshots, author and independent diagnostics, the actual checker-only correction and source receipts. Accepted KH001 supplies the finite histogram lower, KA001 the two ordinary-add-one upper bands, and SC003/BT002 the known-k benchmark. The restricted-statistic upper is available because SC003 uses only triple counts/final pair.

No accepted source was edited. No external peer-review, formal-verification or novelty certification is claimed.
