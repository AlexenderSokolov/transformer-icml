# GN001 handoff

## Useful result
For fixed J>=2,c>=0, arbitrary-initialization IID Bernoulli prediction with exactly J bounded Q-grid outputs under coordinatewise precut c/Q attack, a changed no-plateau recursive snake yields risk

    1/(2sqrt(M)) + 2sqrt(2J)(c+2)/(Q N^(J-1))

for any dyadic N>=2 with N<=Q/[4sqrt(J)(c+2)], at fixed width and O_J(1+log N) primitive depth. Scalar-mean fallback covers Q>=sqrt(M). Therefore sufficiently large capacity ratio Q^J/sqrt(M) permits statistical risk at depth O_J(1+log_+(sqrt(M)/Q)); accepted IC/IR zero-attack lower bounds give distinct-constant necessary capacity and depth. No same-constant iff is claimed.

## Main new proof point
Shifted tent starts moving immediately, so recursive curve is injective with minimum speed N^(J-1); local inverse has no N^-J plateau term. New coefficients are rational, not dyadic. GN explicitly proves the finite rational-description conversion extension to FA/GD; signed long division gives identical coefficient error, paying all input bits and work. Generic growing-depth precision P=4h+c_FA(d+2) absorbs mean and all arithmetic error into E=1, not a fictitious exact rational evaluator.

## Evidence and scope
Read GN001_theorem.md, GN001_derivation_notes.md, GN001_independent_geometry_review.md and GN001_independent_review.md. Exact scripts/JSON cover geometry, rational conversion/affine recurrence/capacity, and a fully rounded finite snake plus nearest-segment decoder. Hardcoded precision16 in the latter is a diagnostic choice, not universal c_FA. Full theorem constructs c_FA from fixed primitive bounds. Reviews are independent LLM evidence, not formal verification or external peer review.

Sources hash-bound in GN001_source_bindings.json. Initial derivation preserved separately; frozen sources untouched. Root alone decides acceptance. No user messages, external publication/contact, purchases, or frozen-file edits were performed by this agent.

## Scientific boundaries
IID upper only; lower witnesses may transfer to larger classes but upper does not. No original-FG robustness, arbitrary nonlocal side information, fixed-bit-everywhere, efficient-decoder, PURE logarithmic depth, internal-fault, learning or novelty claim. Decoder enumerates O_J(N^(J-1)) rational edges and costs are fully paid. Parent is separately exploring a general-Markov composition; GN does not claim it.
