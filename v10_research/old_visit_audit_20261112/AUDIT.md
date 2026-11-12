# Independent local audit: old-visit reciprocal occupation

Date: 2026-11-12. Scope: one load-bearing upper-bound lemma, not the whole paper.

## Frozen input and conclusion

Audited commit: `2ca64346e0dbb19ccf12b5c0f06f12cd0ff31a70`.
Source: `v10_research/positional_manuscript_consolidated_20261103/sections/proofs_positive.tex`.
The first-hit/return argument is at lines 214-263; the old-visit lemma and proof are at lines 445-501.

Independent re-derivation found no gap in this local argument, including its return-time dependencies. This is an LLM mathematical review with finite exact diagnostics, not formal verification, external peer review, a novelty certification, or approval of the entire main theorem. The negative-bound transport and mixture argument and the weighted-imbalance lemma were not audited in this unit. No old receipts, manuscript, or frozen evidence were changed.

## Definitions and quantifiers

Let Y_0,...,Y_M be any homogeneous chain on d states, with arbitrary initial law. Let J_u count occurrences of u at departure indices 0,...,M-1, and O_u those at indices 0,...,M-m-1. The selected row is u=Y_M; the terminal occurrence is not a departure. Here M>=2, 0<=m<=floor(M/2), and c>0. Neither irreducibility nor stationary initialization is required.

The audited claim is

    E[1{O >= c J}/(J+1)]
      <= (3 d^2 + 2 d^3 sum_{s=m+1}^{floor((M-1)/2)} 1/s)/M
      <= (3 d^2 + 2 d^3)(1+log(M/(m+1)))/M.

Empty sums are zero. For d=4 the numerator constant in the last bound is 176.

## Independent derivation

1. Fix target u. If F(z) is the formal generating function of its first positive return (defective returns allowed), Schur complementation gives

       1-F(z) = det(I-zP)/det(I-zP_{-u}).

   Expanding -log(1-F) and -log determinants as formal power series yields

       sum_{j>=1} Pr_u(T_j=s)/j
         = [tr(P^s)-tr(P_{-u}^s)]/s <= d/s.

   Nonnegative entries and stochasticity suffice; recurrence is not needed.

2. Started at u, the event Y_s=u and J_u(s)=j is exactly the event that the j-th positive return occurs at s. The start is a departure and the end is not. Hence

       K_u(s) = E_u[1{Y_s=u}/(J_u(s)+1)]
              = sum_{j>=1} Pr_u(T_j=s)/(j+1) <= d/s.

3. For start v!=u, change only row u to send u deterministically to v. Its first return is 1+D_u under the original start v. The preceding trace bound, retaining its first-return summand, therefore gives Pr_v(D_u=t)<=d/(t+1). This auxiliary matrix need not preserve the order-two pair-state graph; it is used only as a finite-state proof device.

4. On J_u>0, the gate O_u>=c J_u forces O_u>=1 by integrality. Thus D_u<=M-m-1. Conditioning at D_u=t gives the exact identity

       E_v[1{Y_M=u,O_u>=1}/(J_u+1)]
         = sum_{t=1}^{M-m-1} Pr_v(D_u=t) K_u(M-t).

   There is no extra unit shift in the denominator: there are no target departures before t, and the first hit is precisely the first departure in the post-hit process.

5. For t<=M/2, K_u(M-t)<=2d/M and the first-hit probabilities sum to at most one, so this part is at most 2d/M. The start v=u contributes K_u(M)<=d/M and is covered by the same bound. For t>M/2, Pr_v(D_u=t)<=2d/M; setting s=M-t gives the harmonic term (2d^2/M) sum_{s=m+1}^{floor((M-1)/2)}1/s.

6. J_u=0 must not be silently discarded: O_u>=c J_u is true there. At endpoint u it means D_u=M, contributing at most d/(M+1)<=d/M; it is impossible if the process starts at u. Add this term, average over initial states, then sum over d terminal targets. This gives the first claimed bound. For a nonempty sum use sum_{s=a}^b 1/s<=1/a+log(b/a)<=1+log(M/a); the empty case is immediate.

## Boundary checks

- Reducible, absorbing and periodic chains are allowed in the trace and convolution arguments.
- J=0 is explicitly retained.
- m=0, m=floor(M/2), odd/even M, and arbitrary c>0 are covered.
- The analysis may enlarge the gate to an old visit. The implemented proportional gate must not consequently be weakened to merely one old visit.
- This argument uses no conditional independent-sample assertion given terminal state or occupation.

## Fresh finite diagnostic

`check_old_visit.py` is a new standard-library diagnostic, independent of the repository's historical scripts. It propagates the exact law over (current state, total target departures, old target departures), using rational arithmetic. It also computes first-hit distributions through a separate killed-chain recursion and compares the convolution exactly.

It tests five explicitly listed two/three-state matrices, M=2,...,10, all allowed m and all start/target states, and c in {1/1024,1/2,1,2}. The matrices include identity absorbing, deterministic two-cycle, one-way absorption, asymmetric irreducible, and three-state cases. No random seed is needed. The tests are deliberately small and their loose inequalities are not a universal certificate.

Run from the repository root:

```sh
python v10_research/old_visit_audit_20261112/check_old_visit.py
```

The recorded `diagnostic_results.json` is actual output of this new script. A second execution was compared byte-for-byte. Optimized Python is rejected so assertions cannot be silently disabled.

## Provenance and verification limits

This is a new audit, not a recovery of historical work. Source hash, script hash, execution version and verification notes are recorded in `RUN_RECEIPT.json`. The existing public inventory is extended only for these new artifacts; prior entries and historical hashes are preserved. No claim of a full repository integrity run or CI success is made unless separately reported.

## Next bounded task

Audit the histogram/window-preserving legal transport and occupation-mixture domination in the negative proof. Independently check every Hamming-budget, boundary-window and measure-domination condition before accepting the main finite-horizon characterization. Separately audit weighted imbalance, particularly the reflected-chain domination for singleton stationary support.
