# 034 Prover handoff — normal gateway accepted

OID `7e9edb773c2453ce6ca6ab0962158682e758dd98a2e5feefd614a6b6e185c6f8` is DISCHARGED / VALID.
The entire frozen DEC-MATCH / DEC-SEQUENCE / original SRC upper implementation
cost conjunction was submitted once through `euler_team_submit_proof`.

- Fact: `d3e63f7b5e389adf`
- Evidence: `dbadc5e7ba8291254d133f41b62bbb5acb0368631d6a7cb0b9fda79b4a5b8d3a` (PASS / VALID)
- Fact SHA256: `f60b0d2057aa2357a5fb424fda8cf6ec0c72b43c770dee330987838528f39a92`
- Complete proof SHA256: `17ba6dc117edec4d1315a175f972ab541226eded4525e23652e194c656c1650f`
- Actual request SHA256: `e95bae3d226c5b1f1fe4b4d73778283b9584a63cd29263e35a58a66e4d1bcc57`
- Frozen/native statement: 11914 identical bytes,
  `0385830f0ad7f25dee0334213fcd8d099a6ae6b551ba06efc5ccc32c5261586e`.

The proved finite result, for K>=22,M>=1,integer h>=h_N,D>=0, is

    2^-120 min(1,T+Psi(K^4 D/Q)) <= R_dec,V <= R_V^Pi
       <= min(1,64T+Psi(K^4 D/Q)), T=K^(5/2)/sqrt(M+1).

Accordingly R_dec,V tends to zero along a legal public parameter sequence
iff T tends to zero and K^4 D/Q tends to zero. This includes every horizon
residue, D=0, arbitrary large D, M=1 and all permitted high precisions.

## Direct dependency and new proof map

Only these direct Facts are registered:

| Fact | Evidence | Use |
|---|---|---|
| SRC fef8372728290b45 | e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505 | actual bank error, exact bits/cut lifetime, original suffix and full costs |
| MM5 946d42d5bf502eb4 | aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82 | statistical lower bound for every composed common full-history predictor |
| 032 372cbc90282df2cd | 1a61c7931a3b8ee13da63e8e24e758106308055d829d8e5e60195fbca96d0cf0 | original-suffix upper bound; Euler word/stay-circle and parameter bounds |

016 is only transitive through 032; 033 is motivation, not a premise.
New proof sections 2–3 establish the changed Bernoulli-label source and
its complete path law, with equal-length returns and all initial residues.
Section 3 lists all exact retained inputs; section 4 simulates them and
the full actual W from augmented unlabeled choices,J,k'. The 79K payment
erases all K finite-evaluator coordinates, using a globally legal guard.
Section 5 proves the Beta/bin bound, including the last short bin, b>J+1,
J=0 and random outputs. Sections 6–7 prove finite harmonic/log comparisons,
the per-A lower bound before inf, and sequence equivalence. Section 8
preserves all same-SRC dense/uncached costs and simultaneous phase peak.

## Evidence and bounded verification

The actual submitted proof is `complete-proof-v1.md`; the exact tool
request is `submit-request-v1.json`. Raw and parsed receipts are
`gateway-raw-receipt-v1.json` and `gateway-receipt-v1.json`. Admission and
preservation are checked in `acceptance-check-v1.json` and
`native-preservation-check-v1.json`, using saved native before/after states.
`submission-manifest-v1.json` binds the submitted material; `manifest-v1.json`
binds the final delivery. Neither manifest is a mathematical premise.

Exact integer/Fraction diagnostics: 5049 random-label full paths across
102 residue configurations, 5151 Beta identities, 15049 bin boundary
checks, 1728 budget-guard examples. These are finite diagnostics, not the
general proof and not a compiler, literal ledger or network measurement.
The gateway is the independent admission step; finite checks and team
discussion are not Facts. 26 old Fact hashes
match their preexisting native Evidence. Only this target obligation
changed; old evidence/dependencies, root acceptance and budget are preserved.

## Remaining uncertainty and protected scope

No remaining gap in this frozen conjunction was identified by the normal
gateway. The theorem applies to the specified unencoded V interface;
it does not limit changed encoders/prefixes, extra snapshots/statistics or
history rereads. Arbitrary-decoder master sharp rates, physical correction
and true resource tradeoffs remain outside this admission. Unlimited
decoder computation in the lower class is not a free construction.

Counter files present at bundle creation: [].
Their separate complementary review is coordinated by Lead; this Prover
did not create/delegate another task or treat a team report as admission.

031–033 were neither resubmitted nor reopened. Dot's exclusive statistics
scope and missing delivery endpoint remain unchanged; no delivery or
replacement is claimed. The old 027 obstacles, 030 small-K/low-kappa gaps,
[Non-scientific operational metadata omitted.]
[Non-scientific operational metadata omitted.] [Non-scientific operational metadata omitted.]
No compiler/ledger/batch/profile runs; [Non-scientific operational metadata omitted.]
changes. This nonroot admission does not complete the v10 mother problem.
