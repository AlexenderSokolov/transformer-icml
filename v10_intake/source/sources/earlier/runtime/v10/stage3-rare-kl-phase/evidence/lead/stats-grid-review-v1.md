# Lead fixed-version review and next evidence gate

2026-10-25. Current stage3 root
`d0bdd1d8bf611bb7a6e9c4bb14d8b14e5a71ae8cc5c97776fc079ac13c63b428`.
This is research discussion, not independent verification or native admission.
Lead and Prover use the same model; their agreement is not cross-model validation.

## Fixed bytes inspected

| Artifact | SHA256 |
|---|---|
| Prover c1-proof-v1.md | 5884ffc213a0aaa950b48f881abd4519440800737485b5c3aae9d293c38fb38d |
| Prover c2-proof-v1.md | a008ec575571973d7df08ece2468c901744a6c3680df08b15a008c38ff1d7105 |
| Counter adversarial-review-v1.md | b9273b1e96d5fd16d5eaaa5ed8ce75e8385cd57d6ec9dbe2589582a54f86ad64 |
| Counter manifest-v1.json | 10025085403cd5b4f6098236ccd2ff5f26d0f6425eaf56e075ce0c076b71d139 |

Paths are relative to outputs/001-conditional-grid/. Lead read both proofs,
the Counter report, primary map, diagnostic script/result and handoff.
All33 Counter input/output manifest entries match both their hashes and byte
lengths. Hash verification certifies identity, not mathematical correctness.
No source or fixed proof bytes were modified and no old diagnostics rerun.

## Mathematical assessment of C1

No load-bearing gap found in this review. Scope is exactly current D1-D4:
unknown u,t, same-history S_N, one separated prefix and the stated rows.
The explicit forward/reverse kernels and pi are consistent; R=σPσ does not
claim ordinary reversibility. The common three-step mass gives the entire
prefix TV bridge through the reverse conditional path, with no1/u division.
The loss comparison uses unquantized caps and therefore no logQ multiplier.

The random count arguments preserve their separate hypotheses: predictable
martingale increments at a deterministic horizon supply unconditional second
moments; spaced-visit conditional MGFs supply visit tails; a fixed-length row
stack supplies only the monotone event inclusion. The reported false-shortcut
witness is correct: for M=2, D00=1 has two events of mass ut each, one with
C=1 and one with success probability t; hence Pr(C=1|D=1)=(1+t)/2.
At u=1/8,t=3/8 this is11/16, not3/8. The actual proof never uses that shortcut.

For row00 the good-event constant49152 and complementary contribution<386
are below50000. For row10,263168+13824+65536=342528; M>=64 gives
342528/M<=400000/(M+1), with smaller M handled by the deterministic cap.
The H event keeps the rare p log term. M+1>=N/4 and the mixing remainder
<=73728/N imply the stated10^6/N average bound. The conditional ratio
(1+Nu)/(1+Mu)<=3 and remainder<75 give160000/(1+Nu).
N=3,4,5 do not use a nonexistent count-recovery horizon.

Full-history lower testing retains the reverse-path drift boundary term
1-Pr(Y_n=00). Path KL<=40(1+(N-2)u)Delta^2 with Delta=1/(32sqrt(1+(N-2)u))
gives TV<=sqrt5/16 and conditional lower3/[16384(1+(N-2)u)]. Only then is
the common terminal mass u applied to obtain the average lower. Independent
seeds and history-dependent source-independent kernels are covered by the
same acceptance-probability testing inequality. Known u is shared between
the two experiments. All statistical witnesses avoid the first-order curve;
the upper bound includes that curve. The triangular obstruction is not a
fixed-positive-u inconsistency or an almost-sure claim.

## Mathematical assessment of C2

No load-bearing gap found. The actual integer map returns (Q-J,J)/Q with J
the next1 numerator, half-up ties, and dyadic closed interior endpoints.
Q2, Q4, tinyN and zero-count branches are complete. The pointwise inequality
kl(t,q)<=16/3 kl(t,a)+8/(3Q^2) follows by Pinsker in the correct direction,
the interior chi-square bound and the nearest-grid error. Taking conditional
expectations needs no additional mixing argument. The same program's row10
ceil/residual rule retains its multiplicative coordinate bound and average
increment delta_Q. Thus it is one algorithm attaining both claimed orders.

For every fixed u, the t_Q midpoint witness is in D1, avoids the first-order
curve, and gives1/(2Q^2) for every history/seed. The different average witness
t=1/2,u down to0 gives delta_Q/3. Statistical/representation bounds are
combined by max. The advertised sum-order constants follow from that max;
they are not a lower bound added on one source. A target already on the
grid can have zero representation error, so the lower is not pointwise in t.
The uniform bound is not exact KL-optimal quantization: Counter's t=.37,Q4
counterexample is a valid distinction and is retained in the synthesis.

## Remaining uncertainty and dependencies

C1/C2 have no native Facts yet. Their statistical proof and quantization
bridge remain candidates until the independent verifier and normal gateway
accept the exact scopes. C2 must use C1's returned Fact ID, not its obligation
ID/hash or a source-stage Fact. The main proof + Counter + Lead review gate
has now been met; send these fixed bytes to the new Verifier.

C3 remains genuinely unfinished: the checkpoint and bounded code checks do
not yet prove the full operation list, concrete gate/word/hold certificate,
all finite attention arithmetic, and separate input/storage/evaluation domains.
Delegate its self-contained proof to Prover on the existing C3 obligation.
It must reconstruct all source002/005 load-bearing steps, charge the new
16mQ dividend, preserve E_m vs S_N, and certify the same-bit eight-counter
baseline without claiming global optimized dominance. C4 needs the fixed
full package and final independent review/admission/audit after C3.

Counter used the one allowed directed supplemental retrieval for the published
Geiger–Böcherer probability-quantization primary. Its pinned page/theorem map
must be incorporated with HJW/Paulin. No further search is authorized by this
bounded allowance. We have not established publication novelty, neural
advantage, internal-precision necessity, learnability or noise reliability.

## Native readback and coordination records

Readback at this review: all5 obligations OPEN, both routes ACTIVE,
all_evidence=[], acceptance=null; GPU budget LIMITED0. The complete zero-GPU
[Non-scientific operational metadata omitted.]

Prover request[redacted routing identifier] and Counter request
[redacted routing identifier] are both ANSWERED. Counter's return has
already been consumed in this Lead turn; [Non-scientific operational metadata omitted.]
not cause duplicate unchanged review assignments.

Diagnostic9fc456884c8bc452db60e856c443ae1cce960862deb0d3e9a5b28028859ed6d6
records assistant-only scheduling rejection. Its Lead/Counter review conditions
are now met; Lead handles remaining dispatch. Preserve it as historical
coordination evidence, not a C1 mathematical refutation. Diagnostic
0def94abb5dd20e9fc11024c4f656ce7f0d77ef78740e17ef61155836d95a99d remains
applicable to missing full C3/C4 and primary synthesis; the primary source is
now available, but no claim of its completed integration is made here.

Fact IDs=[]; Evidence IDs=[]; no gateway or final audit in this review.
