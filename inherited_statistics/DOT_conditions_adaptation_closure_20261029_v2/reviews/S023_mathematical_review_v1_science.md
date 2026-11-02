# S023 v1 完整科学审查与范围失败

编排说明（非原文）：本副本保留完整科学证明或完整科学审查推理；省略身份控制、私有位置、原提交状态、重复管理表及执行记录。原件未改，复制字节不改写。精确复制／删略／新增区间、原件全文身份见 COPY_MAP.json；原章节号及审查所引行号沿用原件，按同名章节与公式定位。SOURCES.md 给准确科学版本和可读闭包。有限检查仅为补充证据，不是形式验证；本次装配没有重做数学审查。

历史判断：S023 v1 为 NEEDS BOUNDED REVISION，R1/R2 真实保留，未追认。六个科学单元、两项范围错误及所需最小修复完整保留。v2 需与另一份有界复核合读。来源表只保留科学接口条目；原审查所称 19 个绑定包含另行省略的控制记录，并非本表行数。

## Useful result and overall verdict

**NEEDS BOUNDED REVISION of two scope statements, R1 and R2 below.** The mathematical proofs of the two main new bounds pass:

- For the entire first-zero-absorbing family, with arbitrary unknown nonzero rows and **arbitrary initialization**, unchanged original full-history add-one has risk `<=min(1,48 delta^M g+10 i)`. The stated `beta<=1/2` TARGET corollary follows.
- For the specified fixed-public partial-zero stochastic-return family, with **mu=delta_cc**, the actual seven-category chain and complete-history likelihood give one common predictor with risk `<=delta min(p_M,14 sqrt(p_M m^3/(M+1)))`.

The absorbing H0 identities, complete Euler/star residual calculations including default-row star reentry, state-dependent all-row recipe, full failure-history likelihood/KL, actual terminal/context-count joint law, and finite occupation/layer-cake arguments also pass. No correction to (4.1), (4.2), (5.1)–(5.6), or (6.1) is requested. The frozen submission nevertheless contains an overbroad finite-domain summary and an insufficiently explicit generalized corollary. Those must be repaired in a new version rather than silently narrowed only in this review.

The full-class TARGET and the K^5 risk gap remain **open**. Theorem B is neither an original-add-one upper nor an arbitrary-initialization theorem. Its common predictor may use the fixed public geometry, beta, tau, and eta; it is not common over unknown mixtures of those public families.

## Required bounded repairs

### R1 — Blanket K>=2 summary does not retain the clock constructions' domains

**Location:** line 276: “Finite scope: §2-§4 use every K>=2,M>=1,0<beta<1”.

The general absorbing split statements in §2, the recipe in §3, and Theorem A in §4 do hold for every K>=2. However, §§2.1–2.3 invoke the **literal accepted S012 and S015 constructions**, not their all-K risk-envelope patches. The actual S012 construction and its initialized full-history experiment require `K>=13`, so `m=floor((K-1)/4)>=3`, `L=m^2>=9`; the actual S015 star construction likewise requires `K>=13`, `m>=3`, `L=2m>=6`. These restrictions are explicit in the actual source proof bodies. For example, at K=2 the displayed m is zero, so the star count expression involving `M/(2m)` is not defined. S012's all-K theorem uses separate small-K IID witnesses; it does not supply a small-K version of this Euler geometry. S015 does not assert such a patch for its construction.

The source references implicitly identify the intended valid families, and the ray statements are asymptotic, so the calculations themselves are not refuted. But the literal blanket summary claims more than those interfaces permit.

**Smallest repair:** distinguish “general §2 identities and §§3–4: K>=2” from “the S012/S015 construction-specific statements in §§2.1–2.3: their inherited K>=13 domains.” A short explicit qualifier at the clock subsections would also prevent their local statements from being read outside those domains. No bound or proof constant needs changing.

### R2 — d-category extension must explicitly retain the target/label relation and product dimensions

**Location:** line 292, the purported extension to a public d-category family satisfying three listed conditions, with conclusion `delta min(p,2d sqrt(p m^3/(M+1)))`.

The seven-state proof obtains its **delta factor** from the exact identity

`TV(beta delta_0+delta qhat_s, beta delta_0+delta p_s)=delta TV(qhat_s,p_s)`.

Its **m^3 factor** is the product of `m^2` equiprobable contexts and `m` possible labels. These are explicit in §5 and hence fully available for Theorem B. They are not consequences of merely having (i) a source-independent d-state category chain, (ii) a uniform-context conditional product experiment with an independent actual endpoint, and (iii) public outside-query rows. In particular, those three phrases alone do not specify the actual query target as the same delta-scaled law learned by the product labels, or explicitly fix the context/label cardinalities. Without that identification the proof supplies no stated delta-scaled target-loss bridge. A category-count bound alone cannot supply it.

This is an insufficiently specified generalized scope claim, **not a counterexample to Theorem B**, and this review does not assert a new lawful source counterexample to TARGET. The words “same”/“extends directly” can express the intended inheritance, but the corollary must say what is retained rather than present the three conditions as a complete replacement hypothesis set.

**Smallest repair:** either delete the broader corollary, or explicitly restrict it to d-category extensions retaining §5's public target relation `theta_s=beta delta_0+delta p_s`, a common public query set of size m^2 and label set of size m, the complete trace-conditional product law, q equal to earlier visits of the actual query category, and the stated public outside-query targets/common initialization and observable completion. Under those retained premises the proof indeed replaces 49 by d^2 and 14 by 2d; no change in that formula is required. More generally, with d_context contexts and w labels the same argument uses `d_context*w`, not an unexplained m^3.

**Disposition of R1/R2:** return to the original author for a bounded versioned scope repair and fresh bounded independent recheck. Preserve frozen v1 and this report. No main theorem redesign or new mathematical route is requested.

## Unit 1 — Exact absorbing H0 and the accepted clock residual laws

**Mathematical verdict: PASS on the actual inherited clock domains; R1 applies to the summary.** Candidate lines 31–86.

### General absorbing identity

For a fixed supported history, the end-aligned block starting at `(a,b)` and ending at `(c,d)` has the unique legal midpoint `(b,c)`. Its unsplit weight is exactly `theta_ab(c) theta_bc(d)=P^2((a,b),(c,d))`. The failed-block joint weight is therefore `P^2(s,t)-beta 1{t=00}`, not a product of symbol-refresh probabilities. Multiplying all such factors, the initial law, and the optional ordinary prefix proves (2.1) for **every complete observed history**, retaining both symbols of every block. Each failed-block row sums to delta; the prefix is unrestricted, so summing yields `P(H0)=delta^r`.

On a positive-mass history, dividing the joint weight by the original weight cancels blocks not ending at 00 and yields exactly (2.2). Every denominator then used is positive; zero-probability histories are not divided by. Since 00 is absorbing, a history ending outside 00 has never had pair 00. Its block factors therefore suffer no subtraction, proving (2.3) for arbitrary complete-history events inside `{Y_M!=00}`. This does not identify H0 with nonabsorption: the residual can itself absorb, including at 00, whose residual self-loop is one. For M=1, r=0, all products are empty and H0 has probability one.

### Euler: full residual rows and initialized mass

S012's active base D has no zero symbols and is closed under its base transitions; every inactive row and every ending-zero row outputs 0. From active s, two nonzero base outputs have original mass `delta^2 Q_s(c)Q_(b,c)(d)`, hence residual mass `delta Q_s(c)Q_(b,c)(d)`. A base first output c followed by a second refresh has original mass `delta beta Q_s(c)`, hence residual easy mass `beta Q_s(c)` at `(c,0)`. A first refresh gives original mass beta at 00, removed exactly by the subtraction. The active/easy residual totals are delta and beta. An inactive start appends two zeros, so its residual row is exactly delta_00. No off-support row was silently left unspecified.

The initialized base phase ends in UV at the horizon. A failed active path cannot reenter D. The ordinary prefix contributes delta^p and each of r residual blocks contributes delta, so the conditional active mass is `delta^(r+p)=delta^(M-r)`. Terminal D membership coincides with the full base event G and with terminal UV membership under that initialization. Thus the **joint** informative mass is `delta^r delta^(M-r)=delta^M`, and the entire source-specific base-history likelihood remains intact given G. This statement is not extended to arbitrary mu for this clock.

### Star: VV/VS/SV and default-row reentry

The source proof explicitly verifies that every vulnerable row's zero successor is genuinely default, that safe rows output zero deterministically, and that no safe phases are consecutive. In a VV block, first refresh yields 00, second refresh after a base first output yields a nonzero-ending-zero default pair, and two base outputs remain active. Dividing after subtracting beta at 00 gives residual active mass delta and easy mass beta. In a VS or SV block, the original active/00 masses are delta/beta, so the residual active law has total mass one. The next phase types are determined by actual pair phase, independently of the random label. There is no SS block.

For a **default start** `(a,b)`, its first output is 0, so the full residual row is exactly `[theta_(b,0)(d)-beta 1{d=0}]/delta` at `(0,d)`. If `(b,0)` is vulnerable active, its nonzero base law remains; otherwise the row is delta_00. Such off-global-support starts really can reenter D. Conversely, a first failure from the accepted initialized active path enters one of the specifically verified default successors that next absorb; arbitrary off-support reentry does not invalidate that initialized survival calculation.

Each two-step block has one or two vulnerable departures. The prefix pays `delta^v0`, and block j pays `delta^(v_j-1)`, giving `delta^(H_M-r)` on H0 and joint mass `delta^H_M`. Safe symbol coins are irrelevant to the emitted history, so G is not no symbol refresh. The same source-specific full product law is retained given G, not on all of H0.

On the requested ray, the Euler conditional mass is Theta(K^-1/4). For the star, the accepted exact count gives `H_M-r=M/(2m)+O(m)+O(1)`, so `beta(H_M-r)->0`; with `-ln delta~beta`, its conditional mass tends to one. The accepted product/target scaling makes its conditional statistical scale Theta(K^-1/2), and restricted total risk Theta(K^-3/4), not a new global lower. Both source-specific asymptotic comparisons use K tending to infinity through the construction domain.

## Unit 2 — All-row state-dependent recipe and unique stationary law

**Verdict: PASS.** Candidate lines 88–109.

For b!=0, `t_b in [beta,1]` gives `h_ab=beta/t_b in [beta,1]`; for b=0, `h_a0=t_a` is also a probability. The nonzero-supported r_ab normalizes every row and introduces no illegal shift. The unique path to 00 appends 0 twice. For b!=0 its mass is `(beta/t_b)t_b=beta`; for b=0 its mass is t_a, including t_0=1. Thus all K^2 starts satisfy the minorization with the stationary absorbing point mass.

For uniqueness, if nu is stationary, stationarity under P^2 and absorption imply `nu(00^c)<=delta nu(00^c)`; beta>0 forces that mass to zero. This argument covers reducibility and zero rows and uses no initial-law condition.

The residual formulas enumerate disjoint first-output cases. For b!=0, a first zero followed by a nonzero d has weight `(beta/t_b)(1-t_b)r_(b,0)(d)/delta`; a nonzero c followed by any d has weight `(1-beta/t_b)r_ab(c)theta_(b,c)(d)/delta`; the 00 weight is zero. For `(a,0)`, a!=0, the 00 weight is `(t_a-beta)/delta`, and the nonzero-first-output part is exactly as displayed. At 00 the residual self-loop is one. All terms are nonnegative and their total is `(1-beta)/delta=1` by the original two-step normalization. This checks every endpoint, not only a row total.

The stated reciprocal-hazard tradeoff is exact. At t_a=beta, rows ending in a are forced to output zero; at t_a=1 the row `(a,0)` absorbs. No weighted original-risk inequality or TARGET follows from these algebraic facts alone.

## Unit 3 — Theorem A, unchanged original rule and arbitrary mu

**Verdict: PASS.** Candidate lines 111–149.

Conditioning mu on its second symbol being nonzero is a harmless mixture decomposition; the first symbol is allowed to be zero. Independent beta coins before first-zero absorption give `P(G)=delta^M`. Given G, no unknown-row draw or initial symbol was conditioned: the **entire** original history has the fixed homogeneous base table R and the same conditional initial law. R is defined on all rows, with ending-zero rows equal to delta_0. Therefore the accepted L1MAX original K-alphabet add-one theorem applies to that exact base experiment, with arbitrary initialization and zero entries allowed. It is not applied to a residual Q2 chain, a selected row stack, or generic H0.

On G, the terminal base row is nonzero-supported. Its TV distance to the actual `beta delta_0+delta r` is exactly beta. The triangle inequality therefore gives (4.3), with the original full counts and the correct actual target. The predictor does not observe G or the coins.

For first-zero departure t=M-1, the actual terminal pair `(b,0)` has b!=0 and has no past departures, since no preceding pair ended in zero. Its add-one loss to delta_0 is `(K-1)/K`. For t<=M-2, terminal pair 00 has exactly `M-t-2` observed departures, all labeled zero, and loss `(K-1)/(M-t-2+K)`. This proves the exact B_M formula, including zero count and last-departure failure. Initial first-coordinate zero causes no extra occurrence of 00 before that first output zero because the initial second coordinate is nonzero.

The scalar domination by `min(1,K/(M-t))` is valid for K>=2. For every t>=0, `beta delta^t<=1/(t+1)`; for t>0 this follows by maximizing beta(1-beta)^t, and t=0 is direct. Splitting t below/at M/2 gives an early total at most `min(1,2K/M)` and a late total at most `(2/M) sum_(u=1)^M sqrt(K/u)<=4sqrt(K/M)`. The early part is at most `2sqrt(K/M)`. Hence `B_M<=min(1,6sqrt(K/M))<=9i`, with `(M+1)/M<=2` and `6sqrt(2)<9`; the i=1 cap is direct. Also `beta delta^M<=1/M<=sqrt(K/(M+1))`, since K M^2>=M+1 for K>=2,M>=1, and the capped case is trivial. Thus the additional target shift costs at most i.

If the initial second coordinate is zero, the path is known and never visits an unknown row. Starting at 00 gives loss `(K-1)/(M+K)`; starting at `(a,0)`, a!=0, gives `(K-1)/(M-1+K)`. Both are at most `min(1,K/M)<=2i`, including M=1. Convexity over these initial cases and the nonzero-second-coordinate case yields (4.1) uniformly over **all** mu. The loss cap one gives its outer minimum; no lower bound on either mixture weight is used.

For beta<=1/2, `loss 1_H0<=loss`, `i<=a`, and `delta^M<=2delta^(M+1)`, proving (4.2). TARGET consequently holds on this subclass; it is not thereby proved on general recipes. At `M=K^5`, `delta^M<=K^-1/2`, g<=1, i<=K^-2, giving the stated ray upper. At beta=0 the direct base theorem applies; beta=1 is separately deterministic and no residual denominator or null-event conditioning is used. These are family endpoints, not new full-class IID/minimax assertions.

## Unit 4 — Partial-zero family, seven categories, and complete information

**Verdict: PASS.** Candidate lines 151–227.

The nonzero component cases are disjoint and exhaustive for every non-00 pair, including unused symbols and off-initial-support rows. Only UV rows depend on unknown p_ab. Setting t_c=tau and all other nonzero t's to one gives exactly the stated return row `(c,0)` and absorption on every other ending-zero row. The general recipe therefore verifies all-state membership and unique stationary delta_00; no support-only membership check is used. Initialization is the same point cc for every p and horizon.

For beta<tau<1, the row c0 both returns and absorbs with positive probability. If also 0<eta<1, cc has both a self-loop and an exit to another actual pair. A self-loop is incompatible with a disjoint cyclic phase partition of period L>1; the cc base row's mixed zero/nonzero behavior in a canonical constant-beta representation also fails the L=1 safe/nonzero dichotomy. Thus the claimed **interior** family is genuinely outside the accepted template. Boundary tau/eta cases can degenerate and are not claimed individually to retain this novelty.

The seven displayed categories are disjoint and exhaust the initialized support. Their transition probabilities can be verified row by row: C-ending c rows use hazard u and either append c or a uniform U symbol; c0 uses tau; the U, V, and W stages use beta; E and A are absorbing toward A. Random W labels change individual Wc pairs, but not their category transition probabilities. Hence the category process is exactly a homogeneous source-independent seven-state chain, not merely a finite-valued summary of a non-Markov trajectory. Equation (5.1) is its actual fixed-horizon endpoint probability. Unique predecessors give (5.2) for M>=2, while p_1=0.

For a fixed full history, every C→Uc appends one U draw, every Uc→Vc one V draw, every Vc→Wc one unknown W draw, and all other outputs are determined by the category transition. Multiplying these actual transition factors proves (5.3). Extraction and chronological reconstruction are inverse: initial cc, every zero/return, every failure, every orphan final context, and every repeated appearance of a W label in overlapping pairs are retained. The same emitted label is multiplied once. Summing normalized draws in generation order gives trace mass w(z), even for zero coordinates of p; the trace contains no unaccounted label-dependent information.

On E_M, any earlier Vc→E failure would have absorbed before the terminal Vc, so every earlier Vc departure is a completed label draw. A trace ending Vc with Q=q has exactly q full triples and one final context, each context generated by its own independent U/V choices. Therefore (5.4) gives the **entire conditional history** as q IID uniform-context labeled triples plus a uniform independent actual endpoint. That exact source-specific product law proves the binomial joint (5.5); it is not a generic stopped-count assertion. Summing yields `P(E_M,T=s)=p_M/m^2`. Since E_M implies the actual endpoint is not 00, the general absorbing identity adds H0 to this same joint atom without changing its mass. Legal c→0→c returns can still occur.

For neighboring signs, (5.3) retains every observed Vc→Wc ratio, including labels before later absorption. Conditional on any category trace, every such label has an independent uniform context; uncompleted contexts have the same public law under both neighbors. The exact full-history neighboring KL is consequently `E[L_W]*(2alpha/m^3)*log((1+alpha)/(1-alpha))`. Given a trace ending Vc and T=s it is the same expression with L_W=q. Common trace probabilities then allow averaging q over `E_M,T=s`, whose q law equals that under E_M because the actual endpoint is independent uniform given each trace. There is no hidden conditioning penalty or omitted failure information. The inequality `log((1+alpha)/(1-alpha))<=4alpha` for alpha<=1/2 proves (5.6).

The actual target is `beta delta_0+delta p_s`; a flipped coordinate contrast is `2delta alpha/m`. An erroneous sign decision costs at least delta alpha/m in half-L1 on that coordinate pair. This target conversion is correct and is why R2 must preserve it when extending the proof. No unproved lower bound is extracted from the KL formulas.

## Unit 5 — Theorem B's observable common estimator and occupation proof

**Verdict: PASS for the specified family.** Candidate lines 229–263. The extrapolation at line 292 is separately R2.

Every non-UV row is public, even though it need not be delta_0, so the predictor is exact outside the actual query event E_M. On a UV endpoint, the public reconstruction guard excludes histories incompatible with the public category mechanism, not histories excluded only by a hidden zero probability in p. On compatible terminal-UV histories, every earlier UV departure carries a W label; hence the empirical W law normalizes. At zero count the uniform default normalizes. The fallback delta_0 normalizes on the remaining histories. Thus one source-blind kernel is defined on **all histories**, and it never receives Q, G, H0, unknown supports, or latent labels as extra advice.

For n>=1 independent m-label draws, coordinate variance followed by Cauchy–Schwarz gives expected TV at most `(1/2)sqrt(m/n)<=sqrt(m/(n+1))`; at n=0 the loss cap one satisfies the same latter bound. Given a trace ending UV and actual T=s, the exact product law gives `N_s~Bin(q,1/m^2)` and IID selected labels. The binomial inverse moment displayed at line 243 is exact, including q=0 and m=1. Jensen/Cauchy–Schwarz then yields `min(1,sqrt(m^3/(q+1)))`. Multiplying by delta is the exact target-mixture TV identity, not an absorption-probability substitute. Averaging and using zero loss outside E_M proves (6.2).

For completeness, the occupation argument was independently rederived. For any D-state homogeneous chain and integer w>=1, let `B_t=max_y P_y(J_t<w)`. A suffix of length l ending at the same actual terminal state has no greater count; conditioning at its deterministic start gives `B_t<=B_l` for l<=t. On each path, the event “fewer than w previous visits to the current state” can occur at most D w times. Taking expectations under each deterministic start and using max<=sum gives `sum_(t=0)^M B_t<=D^2 w`, not D w. Monotonicity then gives `(M+1)B_M<=D^2 w`. The proof uses neither stationary initialization nor irreducibility, positivity, or an auxiliary random query. At D=7 this is the precise coefficient 49. On E_M its terminal count J_M is exactly Q, giving (6.3), including M=1 and zero count.

For B=m^3 and 0<t<1, the strict event `min(1,sqrt(B/(Q+1)))>t` is exactly `Q<ceil(B/t^2)-1`; any positive integer threshold is less than or equal to B/t^2. Thus the joint tail is at most `min(p_M,49B/((M+1)t^2))`. Layer-cake integration gives at most `min(p_M,2sqrt(49 p_M B/(M+1)))`, with p_M=0 handled directly and the split point sqrt(49B/((M+1)p_M)) used only when it lies below one. This proves the constant 14 and both caps, not just an uncapped asymptotic.

At M=K^5, `m<=K` and p_M<=1 yield the displayed 14K^-1 bound, uniformly over all allowed public tau/eta. For M>=K^5 the stated finite formula is valid. All-state absorption gives the additional `p_M<=delta^floor(M/2)`; that estimate is not needed for Theorem B. m=1 has a singleton unknown-label simplex and zero estimation error, so the displayed upper remains valid although sign tests are vacuous. tau=beta, tau=1, eta=0, eta=1, zero p entries, unused symbols, and public-null histories are all covered by the same exact argument.

## Unit 6 — Scope, failure ledger, dependencies, and remaining frontier

**Verdict: main finite claims and limits PASS; frozen text requires R1/R2.** Candidate lines 265–334.

The correct domains are:

| Claim | Initialization / information | Valid finite domain |
|---|---|---|
| General absorbing H0 full-history identity; recipe/residual/unique stationary law | Any mu; hidden absorbing witness used only in analysis | K>=2, M>=1, 0<beta<1 |
| Literal S012 Euler and S015 star residual/initialized product computations | Their exact common horizon-aligned initial laws and inherited geometry | K>=13, M>=1, 0<beta<1 |
| Theorem A | Arbitrary mu, arbitrary unknown nonzero rows; original full-history add-one | K>=2, M>=1, 0<beta<1; direct separate beta=0,1 comments |
| Theorem A TARGET corollary | Same | Additionally beta<=1/2 |
| Theorem B | Fixed public geometry/beta/tau/eta, mu=delta_cc; new common predictor | m>=1, K>=3m+2, M>=1, 0<beta<1, tau in [beta,1], eta in [0,1] |
| Paired-sign interpretation of §5.4 | Same fixed partial-zero family; 0<alpha<=1/2 | Meaningful bits only m>=2 |
| d-category extension | Must retain the explicit target/product/public-family assumptions in R2 | Not accepted as a complete standalone three-condition statement in frozen v1 |

The failure ledger correctly rejects identifying H0 with no zeros, no symbol refresh, or no absorption; falsely inferring small star active mass on H0; substituting geometric mean delay for actual endpoint alignment; applying conditional IID row-stack arguments without a full likelihood; declaring failure histories uninformative; or replacing K^2-state structure by an unproved smaller generic occupation coefficient. The finite self-checks do not become a proof or independent review.

The stated next frontier is appropriately limited: Theorem A controls t_b=1 but does not extend by deleting nonabsorbing zero-return paths; Theorem B only controls a constant-size public category mechanism with complete product data and public outside-target rows. Growing clock/category complexity and label-dependent return laws can break its premises, but no such mechanism is asserted hard. An upper extension would need a weighted original-row loss/count inequality using the reciprocal hazards, without assuming the special public product/lumping structure. The candidate supplies neither a counterexample to TARGET nor a proof of global truth.

## Direct-source identities and actual interfaces inspected

All **19** SHA256 bindings below were recomputed and agree with the candidate's table. The manifest additionally binds the candidate and two author-check artifacts, giving **22/22** checked entries including sizes and line counts. “Read” records this review's work, not the author's claimed reading history.

| Exact path | SHA256 | Review use |
|---|---|---|
| `long_history_upper_diagnostic_v1.md` | `4a49759bfd8eb75babf695e319b6aafea7ed7ae09085c3339db1684981d9a4e8` | Read in full; especially §3 general D-state occupation, §4 exact full-history/end-aligned split, §9 unproved TARGET |
| `S020_mathematical_review_v1.md` | `9630c56b9f8bf0eb74695a4c8d48555893ff99a8d7640e6bc652a0aac0655864` | Read in full; exact accepted interface and limitations, not a replacement for direct proof inspection |
| `long_history_lower_diagnostic_v2.md` | `879532785c8a195ef84263ab90e327bb50fc8e9c20315f269274070b24625fa2` | Read in full; accepted exact family sandwiches, template restrictions, full state-dependent recipe |
| `S021_mathematical_review_v1.md` | `46b519432b13ba9e30f0164cb5e1c946515345bce45117c65833de803c65f0f4` | Read in full; preserved R1 counterexample, public support completion and source-domain checks |
| `S021_mathematical_review_v2.md` | `023a5e1d3ee2ac2552e68fd151e3eafc90e17bc4fba9ddca4934be571c734ee4` | Read in full; bounded repair acceptance, not mislabeled as another full audit |
| `phase-review/BOUNDARIES.md` | `f647d958e52b349224e4f76d64489413088f1d6047ea908ce9d38df6af3bb147` | Read in full; original/suffix/pooling and finite-domain distinctions |
| `stage03/proofs/S012_complete_proof.md` | `7021dea45b1a262cd6ff71caee4cd8a1f7a973828313100d3d6ad5acbfe09132` | Lines 1–290 read: exact K>=13 construction, all rows, every-residue mu, full history/product law, target contrast and Proposition 6 all-K patches. Small-K theorem is not a small-K Euler construction. |
| `stage04/proofs/S015_complete_proof.md` | `452f4274a9b47635a4d3d7995db09f222b10d024cef935b9b1f5370ebad9db69` | Lines 1–310 read: K>=13 geometry, safe/vulnerable types, actual default reentry, every-row membership, exact initialized full likelihood, first-failure targets, count/error through Proposition 7. |
| `stage02/inherited/L1MAX_statistical_proof.md` | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` | Lines 1–45 and 317–369 read: arbitrary initialization/zeros, original full K-alphabet counts and actual terminal target, §8 exact upper `min(1,48sqrt(K^5/(M+1)))`. Imported theorem's full internal proof not recertified. |
| `stage02/inherited/GU_UC_and_IID_interfaces.md` | `f4abb8e565d58c5af9f6f52ca1e83fc78989dfeb70554e4d22ad1fab8308d275` | Read in full; §11.1 exact suffix/first-w mechanism and max<=sum direction; IID section not needed for a new theorem. |
| `phase-review/proofs/S016_complete_proof.md` | `bfb6ab6e9bd403d4a8502da6474b51f8b31940189dad339cfa5dac1b5ecbf645` | Lines 1–90 read; contextual lower envelope, algorithms/endpoints and exact star-source interface. No lower beyond this frozen interface imported. |

## Independent supplementary executable evidence

Execution completed with **PASS_INDEPENDENT_FINITE_CHECKS_NOT_PROOF**. This status concerns tested identities, not acceptance of the two overbroad manuscript statements.

1. Exact byte audit: 22 manifest entries and all 19 manuscript dependency entries.
2. Exact Fraction checks: 10,384 all-row membership checks, 4,548 state-dependent residual endpoint atoms, and 38,581 complete-history H0 comparisons, including both parities, off-support initial mass, intermediate t values, and zero row probabilities.
3. Literal Euler/star geometries at m=3,4, horizons 1–10: 40 initialized experiments, 1,510 active block checks, and 1,260 encountered off-support star residual rows with positive active reentry (repeated across horizons). Degenerate normalized W rows additionally probe the geometry formulas beyond the accepted positive sign cube; no new predecessor domain is inferred from these tests.
4. First-zero family at K=2,3, three beta values, every point initial pair, M=1–8: 312 experiments, 4,485 complete histories, exact B_M equality, deterministic zero-ending starts, and equality of the **whole no-zero history law** with delta^M times the base law. Arbitrary mixtures are justified symbolically, not by an assertion that finite point tests prove all laws.
5. Partial-zero family at m=1,2,3, with an unused symbol, interior/degenerate public parameters and zero unknown probabilities, M=1–9: 108 experiments, 632 category-lumping row checks, 32,827 complete histories, 4,506 trace-likelihood comparisons and 266 actual endpoint/count-binomial atoms. Matrix endpoint probabilities, H0 identities, integer occupation bounds and finite empirical-risk comparisons were included.
6. Neighboring positive sign rows, m=2, M=3–10: 14,031 **exact full-history likelihood ratios**, including absorbed histories, and floating evaluations of the full-history KL against its expected-label formula. At M=5, for example, the expected label count on histories already absorbed at the endpoint is exactly `128/2401`, explicitly confirming that failure histories can retain unknown-label information. No such data were omitted from the KL calculation.

Fraction arithmetic is used for kernels, history weights, ratios, count joints and binomial identities. Only square-root risk comparisons (`1e-12` tolerance) and logarithmic KL evaluations (`1e-11` tolerance) use floating arithmetic. These finite tests corroborate, and do not replace, the symbolic arguments or establish an infinite domain.

**Return NEEDS BOUNDED REVISION, exactly R1/R2.** Accept no silently broadened clock domain or target-free d-category corollary. Theorem A, Theorem B, and the supporting exact residual/likelihood/count proofs need no mathematical change on their stated intended domains. A versioned clarification by the original author can be checked by exact diff and bounded hypothesis recheck; the full audit above should be inherited for unchanged material, not rerun as invented fresh production.
