# S012 原独立数学审查的科学正文

编排说明（非原文）：原独立审查日期为 2026-10-28，结论 ACCEPTED，无数学修复要求。以下保留原审查的完整逐引理推理、科学适用范围与有限检查事实；身份及运行元数据省略。审查绑定原证明哈希，而非这份新复制件。独立上下文 LLM 审查不是形式验证，也不是外部同行评审。下文有限检查是原审查历史结果，本次编排未重跑；原命令、脚本和运行记录不在本包内。



编排恢复说明（非原文）：以下一行恢复自原审查第 7 行，作为后文 “displayed above” 的原文公式。

    R_D2 >= max{F/180, 2^-16 (1-beta)^(M+1) min(1,sqrt(K^5/(M+1)))}.

## Exact Accepted Scope

The source is a fixed homogeneous normalized table on the original K-symbol alphabet, with legal transition `(a,b)->(b,c)`, arbitrary initial pair law mu, and some hidden stationary pi satisfying `P^2(s,t)>=beta pi(t)` for every starting and destination pair. Zero edges, zero stationary masses, reducibility and mu singular to pi are allowed. The common possibly randomized predictor may read the entire `M+2` symbols and public `K,M,beta`, but not source parameters, signs, hazard labels, the stationary witness, or future symbols. The target remains the actual terminal row and the loss is expected half-L1 TV.

With `n=M+1`, `delta=1-beta`, `i=min(1,sqrt(K/n))`, `a=min(1,sqrt(K^3/n))`, `g=min(1,sqrt(K^5/n))` and `F=max(i,min(delta,a))`, the accepted exports are:

1. The all-domain lower displayed above, together with the independent IID floor `i/(32sqrt(6))`.
2. For `K>=13,0<beta<1`, the explicit family and common horizon-aligned mu give prior-average risk at least `delta^n alpha/8`, where `m=floor((K-1)/4)`, `q=floor(M/m^2)` and `alpha=min(1/2,sqrt(m^3/(q+1))/8)`.
3. If `n beta<=1`, then `2^-16 exp(-2)g <= R_D2 <= R_D2^+ <= min(1,48sqrt(K^5/n)) <=48g` for the unchanged full-history add-one rule.
4. On the exact constructed family and its specified mu, the common constant predictor `delta_0` has risk exactly `delta^n`, including beta zero and one. This is only a family upper.
5. At `M=K^4,beta=(log K)/(4K^4)`, the displayed combined lower divided by `2^-16 K^-1/4` tends to one, and the optimized accepted S011 envelope U divided by `K^-1/8` tends to one. The family minimax rate is `Theta(K^-1/4)` there. No full-class minimax identification follows.
6. Beta zero retains the exact accepted general baseline. Beta one retains the positive IID floor and pooled upper at most i, rather than interpreting the zero absorbing term as its rate. S010's distinct positive-witness theorem remains valid.


## Per-Lemma Audit

### unit_001 — Lemma 1: Reserved-symbol legal clock (`lem:s012-clock`)

- **Statement and assumptions:** the claimed full K-squared-row table and closed disjoint base phases follow from the stated finite domain with K>=13, not from a positivity or recurrence assumption.
- **Finite Euler construction:** balanced directed degrees force a maximal unused-edge walk to close; after splicing, completeness guarantees a usable attachment vertex until every edge is exhausted. Rotation to `c_5=1` is possible without a loop requirement. Distinct C-pairs prevent the retained clock rows from colliding.
- **Table and support:** C,U,V,W are disjoint, nonzero and contained in A. The paired W probabilities normalize and remain positive for alpha<=1/2, including the odd unpaired coordinate. Alphabet types make the active row assignments disjoint; all remaining rows are explicitly `delta_0`.
- **Return and invariant:** the five-step segment ends at `(1,c_6)=p_5`, because the return row is `(w,1)`, not `(w,0)`. Every active base output is nonzero and every active base successor lies in the next phase. This is exactly a legal symbol shift with no added clock states.
- **Adversarial boundaries:** checked non-loop `c_5=1,c_6!=1`, m=3, leftover letters, deleted `p_1,...,p_4`, and all zero-containing rows. No periodicity or irreducibility claim about the modified full chain is needed.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Sparse stationary law and all-pair membership (`lem:s012-member`)

- **Stationarity:** `(0,0)` is inactive and absorbing, so `pi=delta_(0,0)` is genuinely stationary.
- **Every inactive row:** first append 0, then use the inactive ending-0 row to append 0 again. Hence two-step mass at 00 is exactly one, even from leftover-symbol or removed-clock pairs.
- **Every active row:** first append 0 with probability exactly beta, followed by deterministic 0. If the first appended symbol is nonzero, the two-step pair's first coordinate is nonzero regardless of the second output, so it cannot be 00. Thus the exact mass is beta, not merely an informal regeneration lower bound.
- **All destinations and endpoints:** only 00 has positive pi mass; all other inequalities follow from nonnegative entries. Beta zero and one are directly included. No absolute continuity of mu with respect to pi is needed or added.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Every-remainder complete-history experiment (`lem:s012-history`)

- **Initial laws and visits:** `k=(2-d) mod L` and `M=qL+d` give exactly phase-2 times `d,d+L,...,d+qL=M`, with only the first q being observed departures. All six initial cases lie in D_k and are sign-independent. Fixed initial W symbols in phases 3/4 are initial information, not q_sigma labels.
- **Full bijection:** extraction uses the actual full-history indices. Reconstruction supplies the initial pair, every U/V choice, each observed label exactly once, the fixed residual segment, and deterministic fillers. It stops before the final label. The shared W symbol in adjacent pairs is a repeated appearance of one observed draw. All tuples are possible because W probabilities are positive.
- **Path law:** each of q+1 contexts contributes precisely two factors 1/m, including factors from mu when k=1/2; each of q labels contributes precisely one q_sigma. Thus the entire experiment, not merely a reduced statistic, has the displayed product law and an independent uniform actual endpoint.
- **Survival:** the auxiliary M independent coins reproduce the full modified path law. No coin has yet caused absorption before the first 1, so that first 1 occurs on an active row and creates an observed zero. Therefore E has probability delta^M, and its conditional full-history law is exactly the base law. Hazard histories remain in the algorithm's domain and in unconditional risk.
- **Small horizons:** M=1 uses initial A plus one B draw; M=2 uses two draws; q=0 has no labels; impossible M=0 is not invoked. Singular mu is permitted.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Lemma 4: Full conditional information and common tests (`lem:s012-info`)

- **Conditioning and prior:** every `(E,T=s)` event has the same positive probability delta^M/m^2 under every sign. The common uniform sign prior remains uniform after that conditioning, but not after observing the rest of H. The proof makes precisely this distinction.
- **Full information:** the public bijection with T fixed retains the entire conditional history. A single bit flip changes exactly two context-label atoms, giving one-triple KL `(2alpha/m^3) log((1+alpha)/(1-alpha))`; q-fold likelihood multiplication gives exactly q times this value, even when the changed context is the conditioned actual endpoint.
- **Caps:** `log((1+alpha)/(1-alpha))<=4alpha`; both amplitude branches separately imply `8q alpha^2/m^3<=1/8`. At q=0 the experiment conditioned on T is deterministic and KL is zero.
- **Testing:** the finite grouping/convexity argument proves Pinsker with the correct 1/2 normalization. Integrating a source-independent seed gives one common [0,1]-valued test and error sum at least 1-TV>=3/4. Pairing all other fixed bits under the same cube prior gives average error at least 3/8.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Proposition 5: New-target finite-family lower (`prop:s012-lower`)

- **Changed target:** on survival the target is beta delta_0 plus delta q_sigma, not the old q_sigma row. Each paired W contrast is exactly `2delta alpha sigma/m`.
- **Pathwise loss:** a wrongly decoded contrast costs at least delta alpha/m of half-L1 loss on its two coordinates. Ties assigned plus obey the one-sided error statement. Disjoint output pairs may be summed; arbitrary predicted mass elsewhere only adds nonnegative loss.
- **One common experiment:** for every fixed endpoint and bit, composing the same predictor with the common reconstruction yields an admissible test for Lemma 4. Averaging with actual endpoint weights 1/m^2 and r/m>=1/3 gives conditional loss at least delta alpha/8.
- **Unconditional and minimax order:** multiplication by the common survival probability delta^M gives delta^(M+1) alpha/8. Loss off E is only dropped as nonnegative, not declared uninformative. For each fixed B the source supremum dominates this finite-prior average, and infimum is taken afterwards. No hard sign is asserted to defeat every B simultaneously.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Proposition 6: All-K constants and endpoints (`prop:s012-allk`)

- **High K:** `m>=K/8` holds from K>=13. At q=0 the amplitude is 1/2. At q>=1, `q+1<=2M/m^2` gives `t>=z/256`; the two cap cases yield `min(1,t)>=min(1,z)/256`. Together with alpha/8>=min(1,t)/64 this is even `2^-14 g`, so the exported `2^-16 g` is valid.
- **Small K:** `g<=K^2 i<=144i` for K=2,...,12, and `144*32sqrt(6)<65536`. S006's actual stationary IID witnesses belong to every public-beta class and retain all M+2 informative data symbols. This is not a lower bound inferred in the wrong subclass direction and not an invented small clock.
- **Beta zero:** finite Cesaro averages give a stationary probability for every legal table, so the class becomes exactly unrestricted. The MM5/L1MAX baseline and its constants are retained.
- **Beta one:** equal row sums force `P^2=Pi`; summing the exact two-step product over the last symbol forces every theta row equal to p. Conversely such IID rows qualify for arbitrary mu. The M transition outputs justify pooling; the stationary IID subclass lower separately uses all M+2 symbols. The pooled upper is at most i by the displayed finite ratio.
- **Maximum and preservation:** both lower bounds apply before infimum to every common B, so maximum, not sum, is valid. On S010's domain `0<1-8sqrt(beta)<=1-beta`; its conservative certificate is dominated while its distinct positive-source witness feature remains intact.
- **Verdict:** PASS. Repair direction: None.

### unit_007 — Corollary 7: Bounded-hazard matching (`cor:s012-bounded`)

- **Survival bridge:** n>=2 and n beta<=1 imply beta<=1/2; integrating `(1-x)^-1<=2` gives delta^n>=exp(-2n beta)>=exp(-2), including beta=0 separately.
- **Estimator distinction:** L1MAX applies to the unchanged full-history add-one on this smaller source class. Admissibility gives R_D2<=R_D2^+, and cap comparison gives the final 48g.
- **Old sequence:** `n beta=K^-2+K^-6<1` and `K^5>K^4+1` for every K>=2, so g=1 and the claimed positive lower constant truly closes this example, not merely its old certificate gap.
- **Verdict:** PASS. Repair direction: None.

### unit_008 — Proposition 8: Exact same-family upper (`prop:s012-family-upper`)

- **On E:** the actual target has exactly delta mass outside 0, giving loss delta against delta_0.
- **Off E:** a hazard at the last observed departure leaves an ending-0 terminal pair whose target is already delta_0; an earlier hazard reaches 00 by the next departure. Thus loss is zero also at M=1 and a hazard at t=0.
- **Exact risk and endpoints:** multiplying gives delta^(M+1) on every sign. At beta zero it is one; at beta one M>=1 ensures observed absorption and risk zero, without conditioning on a null survival event.
- **Scope:** this predictor needs no hidden parameter. Its upper applies only to this family and its specified mu, and cannot be promoted to a full-class upper. It legitimately bounds the strength available from any testing refinement on these same sources.
- **Verdict:** PASS. Repair direction: None.

### unit_009 — Proposition 9: Remaining scalar-certificate window (`prop:s012-window`)

- **Exact inherited envelope:** all three S011 formulas and their burn ranges are reproduced unchanged. Only U_+ belongs to the original rule; the suffix and pooled branches remain separate, with public deterministic certificate selection.
- **Lower scale:** the integral remainder bound proves delta^n=K^-1/4(1+o(1)); g=1, eventually F=a=K^-1/2(1+o(1)), and the IID term is still smaller. The stronger family amplitude eventually equals 1/2 by (3.33), yielding its separate Theta(K^-1/4) minimax sandwich.
- **Every burn:** `ell+1<=K^4+1<K^5` forces u_g(ell)=1 uniformly. Every h_b is at least h_(M-1), so every suffix candidate is at least h_(M-1)=K^-1/8(1+o(1)). This lower bounds the optimized numerical certificate, not the estimator's risk.
- **Matching public choice:** `ell_*=floor(K^(7/2))` is admissible; u_s(ell_*)<=48K^-1/4 and beta ell_* tends to zero. Its h factor is K^-1/8(1+o(1)). The sandwich proves the ratio-one asymptotic after optimizing over every burn, without guessing an exact minimizer.
- **Other branches:** uniformly in b, the original burn penalty is at least `13K^(13/32)(1+o(1))`, so all original candidates cap at one eventually, as does u_g(M). Pooling caps at one since delta tends to one. Consequently U eventually equals U_suf.
- **Controlled errors independently checked:** writing `rho=-log(1-beta)-beta`, one has `0<=rho<=beta^2/(2delta)`. Therefore

      |log(delta^n)+(log K)/4| <= beta+n beta^2/(2delta),
      |log(h_(M-1))+(log K)/8| <= beta+M beta^2/(4delta),
      |log(h_(b_*))+(log K)/8|
          <= beta(ell_*/2+1)+M beta^2/(4delta).

  All right sides tend to zero on the exact sequence. These are numerical, source-independent error controls already furnished by the submitted integral bound, not an additional hypothesis or repair. After dividing the suffix upper by K^-1/8, the additive stationary error is at most `48K^-1/8`, which also tends to zero.
- **Nonclaim:** the diverging ratio K^1/8 is a remaining certificate separation and a limitation of this witness family, not a proof of the full-class exponent or a uniform absorption of different exponential constants.
- **Verdict:** PASS. Repair direction: None.

## Independent Adversarial Checks

Acceptance rests on the general symbolic audit above. Reviewer-owned inline Python commands, not a reused producer checker, additionally performed:

1. **12,750 exact full-table row checks** using `Fraction`: m=3,4,5; each K=4m+1,...,4m+4; beta in `{0,1/5,1}`. Euler words were deliberately rotated to `c_5=1,c_6!=1`. Checked normalization, no base zero output, disjoint phases, every base successor phase, all inactive rows, stationarity at 00, and exact two-step mass beta/one.
2. **43 exact full-history experiments**, m=3 with M=1,...,26 and m=4 with M=1,...,17, beta=1/5, a fixed rational amplitude 1/2 and mixed signs. Structural/history identities hold for this amplitude independently of the horizon's testing choice. **139,076 full histories** were inspected, including hazard histories. All initial phases (9 and 16 respectively), q=0 and multiple complete cycles were covered. Checked normalization, exact survival probability, the count of supported conditional histories, exact path-product factors, actual endpoint weights, public reconstruction of every symbol, and exact delta^(M+1) constant-predictor risk.
3. An actual-family neighboring conditional product at m=3,q=2 and its prescribed alpha=3/8: **729 atoms**, exact TV `13/243`, and full conditional KL `0.04380318668690391`, agreeing with the displayed exact formula to below 1e-14. The public full-history bijection transfers this calculation to the actual conditional histories. The randomized-test error-sum floor is `230/243`, exceeding 3/4.
4. **5,460 finite scalar probes**, K=2,...,500 and small, clock-boundary and polynomial horizons: checked the small-K floor comparison, high-K amplitude comparison and both testing-amplitude caps. Only these square-root calculations used ordinary floating arithmetic (tolerances at most 1e-14).
5. **33,379 every-burn scalar checks** at K=2,3,5,8,13 along the logarithmic-beta window: verified u_g=1 and every suffix candidate above h_(M-1). At these small K the optimized certificate still caps at one; the report does not pretend finite probes establish the asymptotic, which instead follows from the uniform analytic bounds.

All checks passed. They are supplementary finite checks, not formal verification or an infinite-parameter proof. No checker file was written.

## Hidden Subclaim, Assumption and Notation Audit

The nine named units cover the full table, Euler existence, closure/phase invariant, all-pair membership, every-residue initialization, full-history reconstruction and product law, conditional information, randomized testing/prior handling, changed-target loss, all-K conversion, endpoint baselines, bounded-hazard specialization, exact family upper and optimized scalar certificate. Supporting finite inequalities are proved locally or supplied by precisely identified accepted interfaces. No independent load-bearing claim is missing from the local map.

The primitive assumptions are exactly the finite legal-shift experiment, fixed source, public parameters, arbitrary mu, existential stationary witness, all-pair minorization and information restrictions. Closure, phase, survival, product law, source membership, endpoint independence and testing are derived; none is silently assumed. Conditioning on E is only local with explicit common positive probability where used. No stationary initialization, irreducibility, positive support, random-row IID shortcut, or hidden oracle is added.

Public objects are the class/risks, original estimator, rate functions and stated certificates. Clock alphabets, phase sets, signs, reconstruction, coins and tests are proof-local. Optional m,q,alpha parameters have declared finite-family scope. The predictor does not receive these proof-local random quantities. Existing helper notation does not conceal an additional theorem assumption.

## Target Claim, Explicit Rate and Assembly Audit

Every integer K>=2,M>=1 and beta in [0,1] is covered. The conditional clock proof uses K>=13 and 0<beta<1, with small K and both beta endpoints handled separately. All statistical claims remain finite deterministic-horizon expected half-L1 TV at the actual same-trajectory endpoint, with exactly M departures and all M+2 available symbols. No loss, horizon, query or probability-mode substitution occurs.

Constants are explicit and source-independent. The conversion from finite-family alpha to g retains caps and small M. The conditional-to-unconditional conversion contributes delta^M and the changed target contributes one additional delta, with neither factor dropped. The exp(-2) bridge and the scalar-window o(1) errors have complete displayed controls. Limits in Proposition 9 vary only K along its exact specified sequence.

The assembly is noncircular: Lemmas 1–3 construct lawful sources and the exact conditional experiment; Lemma 4 and Proposition 5 prove the new-target family lower; Proposition 6 gives all-K coverage and the maximum with accepted S011; Corollary 7 uses accepted original-rule L1MAX; Proposition 8 independently bounds only the witness family; Proposition 9 uses only the accepted S011 envelope and new explicit scalar calculations. The full weak-beta joint minimax question remains open outside the proved regimes.

## Review Rationale and Action Boundary

The exact bounded contract is proved without a new assumption, changed interface, missing bridge or dependency repair. **ACCEPTED with no retry** is therefore the smallest justified outcome. This is a material partial advance on the wider question, not an assertion that all joint-rate research is complete.
