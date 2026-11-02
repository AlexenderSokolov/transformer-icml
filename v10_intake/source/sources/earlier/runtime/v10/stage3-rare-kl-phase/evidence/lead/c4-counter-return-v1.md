# Lead disposition of C4 Counter review and exact reading clarifications

Lead, 2026-10-25. Counter task [redacted routing identifier]
is ANSWERED. Its actual fixed report was read:
counter/c4-integration-review-v2.md,
SHA256061ca17c2f6ce1154f6a0d0000126038b2dcc473da3a92e55570936a538a67ce.
Its manifest has SHA256
35e0029526d38a342c0d0998e45f1de1429c683d566b0d8c2ddcd8ea107d4fa2.
Verdict is Scoped PASS, mandatory corrections=[]; this is not a C4 Fact,
independent full-package verification, root admission or final audit.

## Fixed science and evidence boundary

The reviewed v2 package remains unchanged at SHA256
7da57327e4b60288358aacde288aa27a156e944247324b6e2c40da878676ce2f,
with manifest9bf3e8dcac27b349c5d079c7f55dd9f9bc6272d63f58350c27f1cce97dc18c2c.
The following two clarifications specify how abbreviated primary-comparison
wording is to be read in the final synthesis. They do not revise any C1–C3
theorem, estimate, cost function, output interface, dependency or proof file.
The independent Verifier must check this note as well as the fixed package;
Counter's earlier verdict is not presumed to certify a new unchecked claim.

1. **Paulin initial-distribution factor.** For a point start at s,
   N_q=1/pi(s). In the pinned v5 Proposition3.15(3.27), the probability
   comparison uses sqrt(N_q) times the square root of the stationary event
   probability. Proposition3.16 also gives TV bounds involving
   sqrt(N_q-1), while its uniform-ergodicity bound(3.32) has a different
   form. Therefore shorthand saying that a bound has a “1/pi factor” must
   not be read as an assertion that every displayed probability inequality
   has the literal multiplicative prefactor1/pi(s). The combination uses
   the proved C1 reverse-prefix bound, not one of these shorthand bounds.

2. **Known-target quantization auxiliary feasible set.** On the alphabet
   used in the pinned Geiger–Boecherer argument, P_M is the auxiliary set
   of probability vectors whose coordinates are at least1/M. Thus
   t_i>=1/M for every coordinate is precisely the condition for the target
   itself to belong to P_M. It is not a restriction that every positive
   input target must obey for the general quantization problem. Targets
   outside P_M can first be approximated by a feasible t*, as described
   in the primary. Our own D1 target at10 may have an arbitrarily small
   positive coordinate; it is not excluded. Only the simpler membership
   specialization has the target-dependent threshold discussed in the
   comparison. The extraction/printing ambiguity near equation9 is not
   promoted to a confirmed erratum or an additional theorem premise.

These readings were checked against the already pinned local page extracts
Paulin-review-pages.txt (PDF p18) and GB-review-pages.txt (PDF pp4–5), whose
source PDF hashes are in the v2 package manifest. No new retrieval was used.
Both points are nonblocking clarifications, not newly discovered counterexamples.

## Remaining actual obligation

The current native readback still has C1,C2,C3 DISCHARGED:

| Unit | Fact | Evidence |
|---|---|---|
| C1 | e418ec34b7dbc4a6 | 4857f1b1b5d10ab74a979362e3d0c3068c9634016e4ce6b6a0609ed577eb2eea |
| C2 | 4f0e99ed26dfeeeb | a4152a1fc70cbd2d4ece0bea8390fb68c0ed76beb4e11a8d9dd495a8250764ee |
| C3 | a47d648004a9a607 | 3e576827ab335e24f661561d9aa89f035a36925f450dd2daf0be3b166ab3cd27 |

C4/root remain OPEN, acceptance=null. Existing C4 diagnostic
0def94abb5dd20e9fc11024c4f656ce7f0d77ef78740e17ef61155836d95a99d
is not manually cleared. Its material/primary/component requirements are
now substantively supplied, while independent combination review and C4
admission are still pending. [Non-scientific operational metadata omitted.]
prior accepted roots and protection controls remain untouched.

The next substantive task is the independent fixed-version review of v2
plus this interpretation note, reusing admitted component proofs. It must
check the actual composition, the original C4 scope and its scientific
handoff, rather than infer full closure from three component Facts or a
discussion PASS. On an actual completed review, Prover may submit C4 with
the three real predecessors, followed by the root conjunction only after
C4 admission. A separate native final_audit and actual responsibility
handoff remain required. No future PASS or acceptance ID is assumed here.

There is no currently identified mandatory mathematical repair. Remaining
uncertainty is whether independent combination review and the native gates
find an integration or scope gap. No proof of publication novelty, optimized
neural dominance, internal-resource necessity or noisy arithmetic reliability
has been obtained. Stage SOLVED will not complete the v10 mother problem.

New Fact IDs=[], Evidence IDs=[] for this disposition.
