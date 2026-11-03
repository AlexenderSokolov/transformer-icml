# Exact four-counter DP for the pilot half-pooling readout

2026-11-03. Candidate derivation and exhaustive diagnostic; no independent review or novelty claim. This result is for the fixed selected-row bank in `pilot.Model(mode='half')`, not arbitrary learned positional weights, arbitrary Transformers, or arbitrary word-dependent readouts.

## Claim and reconstruction

Let M>=2, L=floor(M/2), R=M-L. For input h of length M+2, allowed z differ from h only at indices 0,...,M-1 and at no more than k indices, 0<=k<=M. Terminal u=(h_M,h_{M+1})=(z_M,z_{M+1}) is protected and known before the scan. Among departures i=0,...,M-1 whose pair (z_i,z_{i+1}) equals u, define J=number of departures, C1=number followed by 1, D=number with i<L, and E=number with i<L and successor 1. These are integer counters in [0,M]. C1 is successor 1, not the earlier exact-attacker note's successor 1-first(u): when u_0=0 the counts agree; when u_0=1, C1=J-C. Similarly E=D minus the corresponding first-half successor-0 count.

The six rails in pilot order (uniform 0, uniform 1, first-half 0, first-half 1, second-half 0, second-half 1) are exactly

    (J-C1)/M, C1/M, (D-E)/L, E/L,
    (J-D-C1+E)/R, (C1-E)/R.

The complete nine-coordinate pilot input appends u_0,u_1,1/M. The `half` implementation requires M>=2, making L and R nonzero. The fixed model output, or any other fixed deterministic readout of these nine coordinates, is thus a function of (J,C1,D,E,u,M). This is an algebraic identity over rationals; pilot computes floating-point quantities and the diagnostic compares those within numerical tolerance.

## Recurrence and exactness

Enumerate possible z_0,z_1, charging mismatches to h. Append z_t for t=2,...,M+1. At t<M try both bits, adding 1 if the bit differs from h_t; at t>=M use only h_t. For i=t-2, if the previous two bits equal u, increment J and increment C1 by z_t; if also i<L, increment D and increment E by z_t. The new window is the old second bit followed by z_t. At each layer, retain for each (window,J,C1,D,E) the minimum edit cost, discarding costs greater than k. Output all terminal banks with their minimum costs, or evaluate a utility on each bank and select a maximizing one.

Each legal z corresponds to one path, including triples crossing the half split or the editable/protected boundary, and conversely. If two prefixes share window and counters, every common continuation adds identical counters and edit costs and has the same final protected endpoint. Thus the higher-cost prefix is dominated; induction proves exact minimum cost for each reachable bank. Any objective depending only on the reconstructed bank, fixed h and other declared fixed public inputs can be evaluated after the scan. A readout depending on z_0,z_1 can be covered by additionally retaining this initial pair (a constant factor), but the supplied implementation intentionally returns only the pilot bank and does not preserve that pair. Longer word-dependent side information must be separately included, with costs reestablished.

There are at most 4(M+1)^4 states in a layer and two choices per state, so O(M^5) transitions, O(M^4) rolling states and O(M^4) final readout evaluations. Counters and costs each take O(log(M+1)) bits. Full predecessor layers cost O(M^5 log(M+1)) bits to reconstruct a witness; rolling storage needs O(M^4 log(M+1)) bits. Alternatively rerunning successive prefixes during traceback gives O(M^6) transitions and rolling memory plus O(M) output bits. The provided implementation keeps all layers when witnesses are requested and reconstructs all bank witnesses, which adds output-sensitive work and memory; a single maximizing witness can instead be traced once. Counts, comparisons, indexing, utility evaluations, encoding and witness output have their own bit/operation costs; the unit-cost bounds are not a practical-efficiency claim. Dictionary implementation costs are not guaranteed worst-case; dense indexing supports the stated state count.

## Objective, information, and numerical restrictions

For each h, maximizing squared loss (f(z)-p(h))^2 is an h-only attack if p(h) is a permitted h-only value or estimate. Likewise the actual pilot attack uses the soft target B(h)=(C1(h)+1)/(J(h)+2) and cross-entropy; since B(h) and its fixed model are computed from h, this maximization is source-blind. The DP does not compute a population conditional probability, train the readout, or guarantee generalization. The realized label Y or hidden source parameter theta used in the utility would create a label-aware or source-aware oracle, respectively. An arbitrary fixed bank utility may depend on h and other authorized fixed inputs but is not automatically source-blind if it is given hidden source information.

Exact maximization assumes exact utility evaluation and comparison (or an exact comparison oracle), including for neural and cross-entropy readouts. Floating-point or transcendental approximation and ties/NaNs require separate error or comparison analysis; the algebraic bank identity alone does not justify an exact real-valued argmax from approximate evaluations. The code supplies a generic utility interface and the diagnostic uses an integer-valued test readout, not a claim of exact cross-entropy optimization under floating point.

## Independent diagnostic

`python v10_research/four_counter_dp_20261103/verify.py 6`

The verifier independently enumerates all words h, edit masks, and budgets for M=2,...,6. For every generated z it constructs counts by directly filtering the list of triples, compares the reconstructed nine inputs to the actual `Model.forward(..., cache=True)['x']` at absolute tolerance 1e-15, and takes minima over all masks. It compares every complete bank-to-minimum-cost map with the DP, validates every returned witness and protected terminal, and tests optimization of a nonconstant integer-valued readout against enumeration. This includes k=0 and k=M, odd and even M, and adjacent edits. See `VERIFICATION.txt` for counts. Finite testing is not a proof.
