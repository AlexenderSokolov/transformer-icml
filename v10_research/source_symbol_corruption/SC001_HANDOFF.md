# SC001 handoff — post-stage7 only

## Scientific outcome

Full-observation, pre-encoder symbol corruption has intrinsic minimax risk
Theta_K(max{M^-1/2, Psi(k/M)}) for fixed K>=3, beta=0, arbitrary initialization, M>=2, 0<=k<=M, when final two symbols are preserved exactly. All computation and all corrupted symbols remain available. A separate stationary recurrent witness gives the same fixed-K order under stationary initialization. No binary or positive-beta frontier is asserted.

The lower uses a SINGLE unknown-parameter-independent kernel, which uniformly deletes n mod(k+1) ones among editable active coins. Conditional on rounded count, the surviving arrangement is exactly uniform, independently of p. Thus the FULL corrupted word factors through a finite alphabet of rounded count plus four protected-pair labels. This eliminates the initially proposed concentration cutoff and proves the full logarithm directly.

The upper counts triples on the corrupted word. At most 3k triples change, so selected-row l1 change is <=6k. Normalization plus general terminal occupation gives additive Psi(6K^4k/(M+1)), on top of inherited clean risk.

## Artifacts

- SC001_theorem.md: exact experiment, common kernel, full proof, constants, failure log, sources.
- SC001_stationary_corollary.md: recurrent stationary strengthening, including clean stationary IID floor.
- SC001_diagnostics.py/json: exact enumeration/factorial identities and finite inequalities (PASS).
- SC001_source_bindings.json: dependencies and successful MG001/R011 acceptance-hash checks.
- SC001_independent_review.md and SC001_review_checks.py/json: fresh LLM reviewer review, to be consumed by root before acceptance.

## Status and evidence

Author proof candidate; root acceptance remains separate. Independent LLM review is not formal verification or external peer review. No external novelty claim. Accepted sources and stage7 frozen delivery were not edited. No external send, publication, purchase, or local-work restart occurred. Workspace lacks a top-level .git repository; git status was unavailable, not needed for mathematics or file access.

## Meaning for parent research

This obstruction cannot be evaded by relocating internal cuts, more precise internal computation, alternate digital coding, or full corrupted-history rereads. It changes fault timing from computational information loss to intrinsic data uncertainty. Statistical-order tolerance is k=O_K(sqrt(M)/ln M). A clean accurate endpoint is essential to the current target contract.

## Next substantive possibilities, not claimed

The exact erasure lemma also appears compatible with stationary weak-mixing IP/SH rare-window sources, potentially removing their concentration cutoff when investigating source corruption. A matching general-beta upper and optimality analysis are separate work. Binary, causal attack, visible-mask, and exposed-attack-randomness versions are genuinely different experiments and remain open here. Do not substitute internal-bank lower bounds for any of them.
