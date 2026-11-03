# CB003 — The fixed near-prefix veto does not repair AB003 at large budgets

2026-11-02. **New restricted-estimator counterexample; fresh review pending.** This closes a concrete candidate left open by CB002. It is not an impossibility theorem for unrestricted full-history predictors at beta=1/M.

## 1. Exact finite statement

Use the protected first-M Hamming corruption model and let

    M>=2^20, h=ceil(sqrt(M)), n=floor(M/2), T=floor(M/8),
    64h<=k<=T, ell=floor(k/4), beta=1/M, r=1/(2M).

Let A be the exact AB003 estimator, with hard designated-exit threshold B=12h. Let W(A) be exactly CB002's near-prefix-veto modification using the first n+1 symbols and threshold h. Under the stationary symmetric first-order flip-r source Q_*, represented as a second-order source, there is one deterministic source-independent protected strict-k kernel C such that

    R_*(W(A),C) >= (k/(128M)) log((T+1)/k).          (CB3)

Q_* satisfies the all-state certificate beta=1/M. Its true designated probability at terminal00 is r. In particular W(A), although clean-safe and small-budget optimal, does NOT attain the known-k critical-curve profile uniformly over all budgets.

Only this particular estimator is being evaluated. Neither CB002's risk-increment theorem nor the open possibility of a different full-history adaptive estimator is contradicted.

## 2. One explicit legal kernel

For each integer k<=t<=T, let

    x^(t)=1^(M+1-t)0^(t+1).

The kernel is identity except on these distinguishable input words. On x^(t), make these deterministic edits:

1. Change the h+1 positions3,4,...,h+3 in its initial1-run to0.
2. Number the t+1 symbols of its terminal zero-run from1 through t+1. Change its positions3,6,...,3ell to1.

These two sets are disjoint. The first set lies inside the first n+1 symbols, well before the zero suffix, and is surrounded by unchanged ones. The initial1-run has length at least M+1-T>=7M/8+1, while h+4<=n+1 for the stated M domain. The second set consists of isolated ones separated by two zeros, with two zeros before the first such one. Since ell<=k/4 and t>=k>=4,

    3ell<=3k/4<=k-1<=t-1.

Thus the final two symbols, at suffix positions t,t+1, remain00. All edits are among the first M positions. The number of edits is

    h+1+ell <= k/32+k/4 < k,

because k>=64h and h>=1 imply h+1<=2h<=k/32. The map uses only M,k and the observed t, never the source parameter, clean history of another experiment, seed or mask. It is defined on every binary word and is a valid strict-budget kernel.

The original and edited words both end00. The first n+1 observed symbols contain EXACTLY h+1 zeros; none of the edited suffix enters this prefix. Hence W's terminal00 veto is disabled. Its terminal11 branch is irrelevant.

## 3. Exact terminal-row counts

Before editing, the terminal00 row has

    C_00,1=0, J_00=t-1.

The inserted prefix zero block of length h+1 creates h-1 triples000 and one triple001, so it adds h to J_00 and one to C_00,1. Its mixed boundary triples110,100,011 do not belong to row00. Each isolated suffix one changes three disjoint000 triples to001,010,100. It therefore adds one designated exit and subtracts two00-row departures. There is no overlap between these triple sets or the original main1-to0 boundary. Consequently the final counts are exactly

    C'=ell+1, J'=t-1-2ell+h.                       (3.1)

Since ell+1>=k/4>=16h>12h, AB003 is on its active branch and outputs

    qhat=(ell+1)/(t-1-2ell+h).

The denominator is positive, and J'<=t+h<=2t. Therefore

    qhat>=k/(8t).

The veto is disabled, so W(A) returns the SAME value. Since t<=M/8 and k>=1 imply r=1/(2M)<=k/(16t), its loss on this edited input is at least

    qhat-r>=k/(16t).                               (3.2)

This is a direct calculation of the ordered output and the actual estimator. It does not borrow a histogram-only impossibility for a full-history map.

## 4. Same-beta null and unconditional sum

For the first-order kernel T_r, its stationary pair law is Pi_*(u,v)=T_r(u,v)/2 and

    P_*^2((u,v),(s,z))=T_r(v,s)T_r(s,z)
                         >=2r Pi_*(s,z).

Hence the supplied beta=2r=1/M is valid on every pair state. The distinct one-flip input words x^(t) have common stationary probability

    v=(r/2)(1-r)^M>=1/(8M),

by (1-r)^M>=1-Mr=1/2. Sum(3.2) over these disjoint genuine input events and discard all other nonnegative losses:

    R_*>= (k/(128M)) sum_(t=k)^T 1/t
        >= (k/(128M)) log((T+1)/k).

This proves(CB3) with unconditional TV at the protected actual terminal row. No terminal-conditioned IID assertion is used.

At beta=1/M and k>=sqrt(M), the accepted known-k profile is at most2k/M. Along k=floor(M^(3/4)), the finite domain eventually holds and log((T+1)/k) diverges. Thus the risk/profile ratio of W(A) is unbounded. The attack's actual edit count is at most k, so it is a witness even under an advertised maximum-k convention.

## 5. Interpretation and successor

The CB002 component's uniform increment bound remains true: it controls the harm caused by ADDING the veto, not the baseline's remaining error when the veto is bypassed. Spending only O(sqrt(M)) edits in the early prefix disables this fixed test; the remaining budget still creates the harmonic false-exit mechanism. This rigorously rules out the simplest assembled candidate W(AB003), not all order-sensitive procedures.

The next useful question is a source-certificate and ordering test that cannot be bypassed with a fixed statistical-size prefix perturbation while leaving the fake tail exits. Conditional ordering or macrocycle geometry remains a possible direction. No full critical-curve adaptation or impossibility is claimed.

## 6. Provenance

Read AB003's accepted full estimator proof and receipt; CB002's complete candidate specifies W; SC003/BT002 provide only the known-k comparison profile. The null certificate and all new count/kernel calculations are proved above. Fresh independent review and finite exact checks are required. No publication, external/formal review, neural/training or novelty claim is made.
