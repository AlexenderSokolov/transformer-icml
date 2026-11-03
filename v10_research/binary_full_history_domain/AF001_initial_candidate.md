# AF001 — Exact supplied-certificate domain criterion for full-history budget adaptation (candidate)

2026-11-02. New synthesis candidate; fresh full independent review and root acceptance required. The ALL-START positive direction is explicitly CONDITIONAL on independent root acceptance of CB005's displayed interface below. The stationary positive interface CB004 and the weak/negative KA001 interfaces are already separately accepted. No accepted proof is changed.

## 1. Exact experiment and public-domain assertion

Use the binary protected-endpoint source-corruption experiment: M+2 symbols from an unknown homogeneous order2 source, integer M>=64, a qualifying stationary pair law Pi with the all-state certificate P²>=beta Pi, beta in[0,1]. An offline source-independent stochastic kernel may change at most k of the first M symbols on EVERY outcome; the final pair is protected. The predictor sees the whole corrupted word, M and the actual supplied beta, but not k, the source, Pi, mask, seed or original interior. Loss is unconditional TV at the true protected terminal row.

Let E be any public subset of pairs(M,beta). A budget-adaptive family on E means maps A_(M,beta), independent of actual k, and one finite constant C such that risk<=C H_2(M,k,beta) for all(M,beta) in E and every integer0<=k<=M. The maps and constant may depend on the entire public domain E. The SAME map at a fixed supplied beta must work for both the clean actual budget0 and all corrupted budgets.

The known-k profile is

    s=M^-1/2, e_beta=max{sqrt(beta),1/M},
    F_2=(k/M)[1+log(1+1/(k e_beta))] for k>=1,
    F_2=0 for k=0, H_2=min{1,max{s,F_2}}.

Define

    G_full(M,0)=0,
    G_full(M,beta)=min{M²beta,1/(M beta)} for beta>0.

**Domain classification.** For stationary initialization, such a full-history family exists if and only if

    sup_((M,beta) in E) G_full(M,beta)<infinity.      (AF1)

Conditional on accepted CB005's all-start upper, the SAME equivalence holds when the guarantee is required for every initial pair law, including unsupported states.

Equivalently, adaptation is possible exactly when E lies in some fixed union

    beta<=B/M² OR beta>=1/(B M), B>=1 finite.        (1.1)

Sufficiency may select a rule using the ACTUAL supplied beta and the fixed public domain bound B. This is not a single beta-blind rule on that union. The negative direction already uses stationary witnesses and arbitrary full-word predictors.

## 2. Exact inherited interfaces and conditional dependency

Accepted KA001's weak-band upper supplies ONE ordinary add-one predictor, independent of k and beta, for every initial law and every budget on beta<=B/M², with constant

    C_weak(B)=2^16+96[1+(1/2)log B], B>=1.          (2.1)

Accepted CB004 supplies a stationary balance-gated empirical rule A_bal, independent of both k and beta. Its exact all-start analogue, currently the separate CB005 candidate, is the CONDITIONAL interface

    R_all(A_bal)<=min{1,2^16/sqrt(M)
                       +2^16/(M sqrt(beta))
                       +2^23 k/M}, beta>0.         (2.2)

The stationary CB004 bound is at least as strong as(2.2), replacing its second2^16 by4096. No all-start conclusion is licensed by CB004 alone. AF001's all-start assertion must remain conditional until CB005's exact proof, full review and root receipt are bound. If its interface changes, this dependency must be checked again, not silently assumed.

The rule A_bal uses the protected terminal row u. From the corrupted word it computes J1'_u, its departure count in the first floor(M/2) times, full departure count J'_u, and full designated-successor count C'_u. Designations are00->1,01->1,10->0,11->0. It outputs C'/J' when J'>0 and512J1'>=J', otherwise designated probability0. This description fixes the same map used in both inherited results.

Accepted KA001 also supplies, for M>=4096 and

    256/M²<=beta<=1/(16M),
    k=floor(beta^-1/2), T=floor(M/8),

the same-actual-beta full-history constrained-risk inequality

    R_null >=[(3k/(2048M))log((T+1)/k)
                             -32S log(2T/k)]_+,    (2.3)

with stationary clean/null sources in D_2(beta), one common strict source-independent kernel, and H_2(M,k,beta)<=2k/M. S is the SAME map's supremum clean risk over its explicit family. This is the accepted BK002 family applied by exact class nesting; the actual supplied predictor metadata is never changed.

## 3. A concrete budget-blind selector on the bounded union

Assume(AF1), choose a finite B>=1 with G_full<=B on E. Define, for every public pair, the total rule

    A^B_(M,beta)=ordinary add-one, if M²beta<=B;
                A_bal, otherwise.                 (3.1)

This selector depends on beta and B, not k or clean data. The same branch is used for clean and corrupted histories at that public pair. At beta=0 it uses add-one; no expression dividing by beta is evaluated.

For every pair in E outside the weak branch, the bounded minimum forces1/(M beta)<=B, hence beta>=1/(BM). On that branch,

    1/(M sqrt(beta))<=sqrt(B)/sqrt(M).

Using(2.2), or the stronger accepted stationary CB004 interface, gives

    R(A_bal)<=min{1,2^16(1+sqrt(B))s+2^23(k/M)}
             <=C_strong(B) H_2,

where C_strong(B)=2^16(1+sqrt(B))+2^23. Indeed H_2 dominates min{1,max{s,k/M}}, and the sum is bounded by that maximum times the sum of coefficients; the final unit cap is harmless.

The weak branch uses(2.1). Thus one permissible domain constant is

    C_E=max{C_weak(B),C_strong(B)}.                  (3.2)

Both procedures are total maps and the branch is public. They need not estimate which source parameter regime is true beyond the supplied certificate. Overlap of the bands is allowed; the weak-first convention resolves it. The rule is defined outside E too, but no guarantee there is asserted.

Stationary sufficiency already follows from accepted interfaces. All-start sufficiency follows from the SAME selector if and only if the requested CB005 upper interface is independently accepted. No unsupported-start conclusion is imported from stationary reversal.

## 4. Unbounded G forces an actual-beta constrained-risk contradiction

Suppose sup_E G_full is infinite. Select(M_n,beta_n) in E with G_full>=n. Then beta_n>0 and

    M_n² beta_n>=n, M_n beta_n<=1/n.

Multiplying the two terms defining G gives M_n, so G_full<=sqrt(M_n); equivalently these two displayed inequalities directly imply M_n>=n². Therefore M_n->infinity,

    M_n² beta_n->infinity, M_n beta_n->0.            (4.1)

No monotonicity, regular curve, graph representation or unique beta per horizon is needed. An unbounded subsequence is enough.

Eventually each selected pair lies in the exact finite band of(2.3). Set k_n=floor(beta_n^-1/2), T_n=floor(M_n/8). KA001's exact rounding gives

    k_n sqrt(beta_n)>=3/4,
    k_n/sqrt(M_n)>=(3/4)/sqrt(M_n beta_n)->infinity,
    M_n/k_n>=M_n sqrt(beta_n)->infinity.

All k_n are legal integer budgets; the finite theorem proves k_n²>=4M_n and k_n<=M_n/16. Thus both logarithms in(2.3) are eventually positive, its first diverges, and

    log(2T_n/k_n)/log((T_n+1)/k_n)->1,

because the numerator differs by the bounded additive term log(2T_n/(T_n+1)).

If a candidate adaptive family had one finite constant C on E, its actual k=0 guarantee at the SAME supplied beta_n would give S_n<=C/sqrt(M_n). The ratio of the penalty to the positive term in(2.3) is at most

    (65536 C/3)(sqrt(M_n)/k_n)
       log(2T_n/k_n)/log((T_n+1)/k_n)->0.

Consequently the risk is eventually at least

    [3k_n/(4096M_n)]log((T_n+1)/k_n).

Divide by the ACTUAL-beta benchmark H_2<=2k_n/M_n. The risk/profile ratio is at least(3/8192)log((T_n+1)/k_n), which diverges and contradicts that same finite C.

This argument invokes KA001's finite inequality at actual metadata, not merely its every-horizon curve wording. The clean family may depend on the selected attacked budget because the clean guarantee is uniform over the class, but the predictor map does not change. Stationary witnesses suffice, so necessity applies to both stationary-only and all-start guarantees without any CB005 assumption.

## 5. Edge cases, certificate labels and beta blindness

- At beta=0, G_full is defined as0 and the weak branch is valid. No inverse-beta formula is used.
- An empty domain is vacuous and lies in every sufficiently large fixed band union.
- Bounded horizons have bounded G_full, even with infinitely many beta values, since G_full<=sqrt(M). Independently loss<=1 and H_2>=M^-1/2 allow a finite constant.
- Finite exceptional horizons are absorbed in B or the risk constant. Sparse horizons and arbitrarily oscillating supplied certificates are included.
- A domain may alternate between fixed weak and critical-strong bands and remain adaptive; the public beta chooses the rule. A sequence entering the intervening region with both quantities in(4.1) diverging defeats any uniform constant.
- Beta is a valid lower certificate, not necessarily its maximal value or a transition probability. The decoder is allowed to use the actual supplied label. Nesting in the lower proof does not replace that label or the true target law.

The supplied-beta qualifier is essential. For example

    E_*={(M,0),(M,1/M):M>=64}

has G_full<=1. Selector(3.1) with B=1 uses add-one at beta0 and the balance rule at beta1/M. Accepted AB001's jointly blind stationary obstruction applies to exactly these two certificate types: clean alternatives are admitted at beta0 and its attacked null at beta1/M. Therefore one cannot in general require the SAME beta-blind map on this bounded union. AF001 is not a reversal of AB001/BK002.

This is simultaneous adaptation across actual budgets. It is not a pointwise failure claim for every individual positive k, and it does not identify an advertised maximum budget with the realized actual one.

## 6. Consequences and observation-resource boundary

For beta=M^-gamma, gamma>=0, the two terms are M^(2-gamma) and M^(gamma-1). Their minimum is bounded exactly when gamma<=1 or gamma>=2. Thus supplied-beta full-history adaptation is possible in those two outer ranges and impossible for1<gamma<2; the all-start positive assertion retains the CB005 condition until acceptance. Fixed valid positive factors at the boundary curves are absorbed into B.

The procedure needs much less than arbitrary ordering: the global triple histogram, four first-half row occupations and the protected terminal pair suffice, plus actual supplied beta for the selector. This follows from the explicit inherited algorithms, not from a new encoder implementation.

Accepted KH002 instead classifies global triple histograms plus initial/final PAIRS by min{M²beta,1/(beta sqrt(M))}. Thus, in particular at beta=1/M, dropping the coarse temporal half-count information can prevent budget adaptation even though the full-word experiment permits it. Boundary-window refinements have their own exact accepted scopes. No conclusion about arbitrary local encoders, attention resources, trained networks or bit complexity follows without a separately proved representation reduction.

## 7. Acceptance boundary and provenance

The stationary inputs KA001/CB004 and the negative BK002/KA001 interfaces are accepted separately. CB005's ALL-START upper is a new dependency under fresh audit at the time of this draft. AF001 is itself a new candidate; accepted component status does not bypass its fresh full review.

No proof above assumes the unproved weighted-semigroup route in WT001. The explicit class/metadata, budget, initialization, exceptional-horizon and beta-blindness distinctions must remain in any review and final handoff. Diagnostics are finite corroboration, not formal verification, external peer review or a novelty assessment.
