# BU001 fresh independent hostile review

2026-11-02. Reviewer: independent LLM reviewer, not the candidate author. **Recommendation: mathematically sound within stationary binary scope; no blocking gap found.** This is a review recommendation, not root acceptance, formal verification, or external peer review. Candidate and accepted dependencies were not modified.

## Sources and scope

Read the complete BU001 candidate, IU001 beta-sensitive upper (especially Lemma 2.1), AU001 residual-suffix upper, SB001 v2 (decoder, comparator, universal occupation and entire finite-resource ledger), UI001 IID floor, and BI001 v2 binary lower. Checked their intake acceptance records, including BI001 acceptance at 05:52:32 UTC. Main BU1 is for integer M>=1, 0<beta<=1, A>0, integer k>=1. BU2 inherits the actual SB program domain: K=2, integer M>=64, h>=4, Q=2^h, public integer kappa>=1. It is stationary only. The implicit domain inheritance should remain explicit in any downstream theorem statement.

## 1. All-state certificate, support, hitting times

Stationary support is closed. For beta>0, P² restricted to that support is strictly positive, hence irreducible and positive recurrent, including at beta=1. Stationary binary pairs satisfy Pi01=Pi10=x, ya=xe, wt=xb. If y,x,w>0, irreducibility forces a,e,b,t>0. The all-state entries P²(10,01)=ea and P²(01,10)=bt imply e²>=beta y and b²>=beta w after using balance. These are necessary consequences of the genuine certificate, not a replacement sufficient certificate.

Independently solved first-step systems. Both displayed exact hitting vectors (lines 34–36) are correct. For target00 the equations are h10=1+(1-e)h01 and h11=1/t+h10; substitution gives h01=(b+2t)/(et). For target01 they directly give (1/a,1+e/a,1/t+1+e/a). The displayed upper bounds and their symbol swaps dominate every supported start.

The weighted H bounds follow as stated: xe replaces ya; xb/t=w; sqrt(beta)w/b<=sqrt(w), sqrt(beta)y/e<=sqrt(y), and e<=1. The constants 5 and subsequently 6 are conservative. No lower bound on an unknown stationary mass was inserted.

If y=0 with x>0, support closure forces e=0 and target00 is absent; waiting at00 must actually be deleted rather than evaluated as 0/0. Likewise w=0 forces b=0. With w=0 and target00, h01=2/e and h10=2/e−1, so the stated 2/e bound is exact for the maximum. The symmetric case is valid. Pure support {01,10} is incompatible with positive beta (its two-step chain has two deterministic classes). If x=0, positive beta permits only one supported diagonal; that diagonal is absorbing and its q=0. Thus every nontrivial relevant division has positive denominator and q=0 contributions disappear without invoking a return bound with infinite RHS.

## 2. Reversal, Kac, moments, exponential tail

On positive support, reversal followed by pair-coordinate flip reproduces the forward pair kernel exactly. This follows by checking triple probabilities: only 001/100 and 011/110 need nontrivial balance, supplied respectively by ya=xe and xb=wt. Unsupported rows need not have a reverse definition. Crossing targets interchange; their masses and weights are equal, so (1) survives. No detailed balance of the unflipped pair chain is assumed.

IU001 Lemma 2.1 applies: support positivity guarantees its finite return and uniqueness argument; E tau=1/p and E tau_k=k/p hold. The maximal hitting mean can be that of the flipped target in the reversed analysis; its proved uniform bound is the same. A positive return has mean <=1+H, and sqrt(beta)pq<=1 yields Hbar<=6/(sqrt(beta)pq).

The moment induction is valid for integer hitting/positive-return times. At j>0 on survival, the state is non-target, and the remaining law is an ordinary hitting law; j=0 retains the original family member. The elementary power-sum inequality, conditional induction bound <=(m−1)! Hbar^(m−1), and sum_j P(T>j)=ET give m! Hbar^(m−1)ET. Finite-state geometric domination justifies finiteness, or truncated induction followed by monotone convergence suffices. Nonnegative exponential series and lambda Hbar<=1/4 give the stated return mgf. Successive return increments are independent with the same return law by strong Markov, not IID observed successor samples.

For mu=Mp>=16, ceil(mu/16)<=mu/8 and integer counting makes {J<mu/16} exactly {tau_ceil(mu/16)>M}. The exponent is at most −3lambda M/4=−sqrt(beta)mu q/32. For mu<16, the RHS 2exp(−sqrt(beta)mu q/48) exceeds one. Consequently (2) holds uniformly, including small M and beta=1. No global sqrt(beta) mixing claim is made.

## 3. Layer cake and thresholds

For 16alpha<u<q and positive threshold, j=ceil(A/u−k) is >=1, <=A/u, and <mu/16 because k>=1. For nonpositive threshold the event is empty. Thus the two event bounds alpha/u and B apply jointly. Integrating min(alpha/u,B) over (0,q) yields at most alpha[1+ln_+(Bq/alpha)]; the initial layers cost <=16alpha. The maximum bound v exp(−sqrt(beta)v/48)<=48/sqrt(beta), with v=mu q, establishes line102. Summation over supported states cancels p only after the conditional estimate. If q<=16alpha, the direct q cap suffices. This proves BU1 without any endpoint independence or hidden positive-mass cutoff.

## 4. Actual binary floor decoder and statistical comparison

The floor identity at line112 is exact. To justify the less standard line114: if v>=p_hat then v−p_hat <=p_hat f0/N<=p_hat; if v<=p_hat then p_hat−v<=p_hat trivially. Applying the same argument with symbols swapped gives the minimum of p_hat and 1−p_hat. This is valid even when one floor is zero, provided N>=1; it is not asserted on N=0. Combining with the inherited 2/(Qr) bound and the 1-Lipschitz map u↦min(u,B) gives line116 for a true diagonal exit probability.

**Reading clarification, not a blocking gap:** on crossing rows q=1 is a clipping weight, not necessarily the true exit probability. One must use the direct floor bound min(1,2/(Qr)), not charge |p_hat−1| as a statistical error. Let delta=|p_hat−theta_exit| with theta_exit the actual row probability. On every positive-block J>=1 history both cases then obey

    TV(output,true row) <= min(q,2/(Qr)) + 2delta + 1/Q.

The diagonal case uses line116; the crossing case even needs only delta. Thus the text's intended combination is valid, although downstream exposition should distinguish the actual crossing probability from its q=1 weight.

For J>=1, 1/r=(kappa−1)/kappa+M/(kappa J), and J+2<=3J prove line120. Therefore min(q,2/(Qr))<=2/Q+min(q,6M/[z(J+2)]). Here J,r,q,stationary masses and empirical fractions are analysis variables, not supplied decoder ports.

Write the add-one row as q_add. Then delta<=TV(q_add,true row)+2/(J+2). Its expectation is controlled by the accepted original add-one risk, <=2^13 Hstat, and the universal occupation lemma. For K=2, Hstat<=2^(5/2)/sqrt(M+1), and E[2/(J+2)]<=Psi(32/(M+1))=O(M^−1/2) on the inherited M>=64 domain. This comparison applies to the actual terminal query; no rowwise IID conditional theorem was substituted.

On N=0, Qr<2. Rearrangement gives (Q−2)kappa J<2(M−J); Q>=16 implies J<4M/z. Include J=0 using integer threshold ceil(4M/z)+1. The universal bound with K^4=16 makes its probability <=64/z+32/(M+1), capped at one. This absorbs both the uniform empty-block fallback and J=0. No replacement by a natural-default fallback is made: the actual unchanged SB decoder still uses its uniform fallback. Final ordered binary simplex rounding costs <=1/Q.

Combining these inequalities with BU1 at A=6M/z gives BU2 for beta>=M^−2. For 0<=beta<M^−2, the accepted SB beta-free estimate directly gives the same stated envelope with max(sqrt(beta),1/M)=1/M. At beta=0 the weighted-return proof is not invoked. Equality beta=M^−2 is covered by the positive branch; beta=1 has no singular step. A sufficiently large universal C permits the displayed C min(1,...) from the risk cap and the derived uncapped bound.

## 5. Implementation and relation to the lower

This is solely a new analysis of SB001's same complete 8-coordinate bank with actual weights {1,kappa}, two paid singleton-copy heads, paid triple gates, one dense statistical head, exact pair side field, positive-block normalization, uniform empty-block fallback, and final ordered rounding. No new numerical operation, beta input, count port, unrounded row mass, historical reread, mask, or retained field is added. All of SB001 §6's b=64(h+ell+bitlength(kappa)+1) widths, full products/guards, dense maps, all-token bank and work, addressed program/tape scans, offline generation, simultaneous-phase sums and separately charged PURE alternative remain applicable without improvement. BU001 is not an NB002 implementation claim.

UI001's kappa-uniform 1/Q floor and BI001 v2's truncated binary logarithmic lower are compatible with this upper. This review does not infer an unrestricted all-Q minimax equivalence from their differently shaped formulae, nor an arbitrary-start upper. Matching consequences require their exact model inclusion, parameter domains, D>=8,r>=3 for SB inclusion, legal dyadic grids, and a sufficiently large feasible risk multiplier. The new upper genuinely has sqrt(beta) rather than beta in its stationary logarithmic cutoff.

## 6. Diagnostics and disposition

Fresh script: `reviews/BU001_independent_checks_v1.py` (relative to v10_research). It does not import candidate or author diagnostics. It enumerates rational transition kernels including boundary rows, determines the unique closed support, computes the maximal genuine all-state two-step minorization coefficient, solves hitting systems exactly, checks pair-flip reversal, computes hitting/return moments through order4, and checks the squared weighted H/Hbar constants without floating square roots. It also checks exact binary floors and decoder inequalities; finite return-count and BU1 exponential/logarithmic comparisons are numerical corroboration only. Output is `reviews/BU001_independent_checks_v1.json`.

Disposition: no blocking mathematical counterexample or proof gap found. The crossing-weight versus true-probability distinction and inherited SB parameter domain are clarification notes for downstream statements. Neither candidate acceptance nor accepted source edits are performed by this review.
