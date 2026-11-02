编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R008 independent mathematical review v1

## Verdict / useful result

**ACCEPT.** For every integer K>=2 on M=K^5, beta=log(K)/K^5, frozen R008 proves risk(ALG)<=min(1,20000/K) uniformly over the ENTIRE legal absorbing-stationary subclass with witness pi=delta_00 and arbitrary initial pair law. ALG is the same history-only count-guard predictor of accepted R001. Its subclass worst risk and the restricted common randomized minimax risk are Theta(1/K) asymptotically. No mathematical revision is required.

The decisive transfer is genuinely eventwise: the trimmed exceptional event costs 2epsilon+(13/5)B; the pair-success term uses R004's actual early/dyadic capped certificates. No scalar original-risk bound is mistaken for a radius bound. This is not an arbitrary-pi theorem, an all-parameter sharp-adaptation theorem, or a zero-risk endpoint adaptation assertion.

## Procedure and exact bindings

Independent mathematical review. The complete frozen R008, R006, R002, R001 and R004 proof bodies were read. Their four complete independent reports were read. Recovered S020 was read through Section 5.3, including its full finite-augmentation event-loss proof. Scientific source identities were recomputed and matched. The assigned R008 hash matched actual bytes.

No R007 text was read or used. No source edits occurred. This is independent mathematical review, not formal verification; inherited accepted lower interfaces are used without claiming a fresh audit of every historical primitive construction. Diagnostics are not mathematical premises.

Scientific input identities below have public locators in SOURCE_INDEX.json.

| Object | SHA-256 |
|---|---|
| `R008_absorbing_blind_corollary_v1.md` | `dd15415de1102f2c4df2c20f3ca7ec771815375510e32f041844468b2469a89f` |
| `R006_absorbing_cutset_v1.md` | `c0e368ffc620e8f9a48c66a7092dd047f6fec04bcce8bf468fc4be8d970dc7d5` |
| `R006_independent_review_v1.md` | `c6f7b9a934bf2017d7283d2f86474481eee3e18ce12b4613649bbad5d80294d6` |
| `R002_critical_prefix_obstruction_and_arrival.md` | `87f86a5a7f4a291e50bb78a761b765f3e3f0289bec31c823e2ed30eb65a4bc98` |
| `R002_independent_review_v1.md` | `69a3cc715dadf2f112ce6310280010548a3fdb5ad2c6f7f839e95915b2a30590` |
| `R001_mixed_prefix_and_blind_transfer.md` | `e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1` |
| `R001_independent_review_v1.md` | `9238ec0d916ae1b2c3c8bb5a7daacfb9df69d9928864d0d0f11a2f5a2133eadf` |
| `R004_grouped_regeneration_v1.md` | `f83f79f77ca377cb8a8991eef6a39eed4f9dabb02d810078a83e437ddaa9c2b0` |
| `R004_independent_review_v1.md` | `d1975609265a1055df3a5bb2f3c7c7a6eaaf0bac2f841fc418caada11c58bbe4` |

Additional inspected scientific source: `S020 (SOURCE_INDEX.json)`, SHA-256 `a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb`.

R002's accepted results explicitly leave full-class (O) unproved. R008 imports its proved trimming lemma, not (O). R006 supplies the actually proved absorbing-class count input. Stale author-status sentences in dependency proof bodies are historical.

## 1. Exact algorithm, experiment and class

R001 defines q as original K-letter terminal-row add-one using every departure 0,...,M-1, and pooled b_pool from all M observed outputs. With n=M+1,

    g=min(1,sqrt(K^5/n)),
    rho(J)=min(g,64sqrt(K/(J+K))),
    ALG=b_pool if TV(q,b_pool)<=rho(J), otherwise q.

Thus triangle inequality gives ell_ALG<=ell_q+rho(J) on each original history. All are probability vectors; loss and radius each lie in [0,1]. The coefficient b in R008's occupation bound is not the pooled predictor. No beta, stationary witness, absorbing symbol, labels, source table or initial law is read by ALG. All statements concern unconditional half-L1 loss at the actual Y_M; no query-state replacement, omitted midpoint, terminal departure, suffix estimator or class-dependent algorithm is introduced.

R006 covers every legal table with pi=delta_00: theta_00(0)=1 and theta_ab(0)theta_b0(0)>=beta for all a,b, without equality, restricted excursion geometry or a stationary start. Its proof includes singular zero-potential endpoints and arbitrary off-support initialization. Hence the count input is uniform over the entire claimed subclass, not merely the star family.

## 2. Critical count input and constants

For K>=2, M=K^5 and beta=log(K)/K^5, beta<1/16, so all interior label constructions apply and R004's beta<=1/2 domain holds. R006 proves

    q0=delta^floor(M/2)>0,
    P(E,J<w)<=min(q0,epsilon+bw),
    epsilon=2delta^M<=2/K,
    b=8(K^2+q0 K^3)/(M+1)>0.

This applies to any augmented E with mass at most q0, so applies to R001's compatible-label E without a new coupling choice. The estimates q0<=2/sqrt(K), b<=24/K^(5/2), and K+log(1/q0)<=2K imply

    q0 b[K+log(1/q0)]<=96/K^2.

Consequently B=min(q0,80sqrt(q0 b[K+log(1/q0)]))<=800/K, since sqrt(96)<10. These are finite inequalities, not merely asymptotic approximations. R008 uses no version of the unproved arbitrary-pi obligation.

## 3. Finite augmentation, trimming, and null events

R001 constructs both label systems by their conditional kernels given the complete original history, taking a conditional product. This preserves each history-label marginal but does not assert unconditional independence. Attaching this finite kernel to original independent row stacks preserves their unconditional marginal. S020's event-loss lemma explicitly accepts arbitrary such finite augmented events and upper mass bounds.

Let m=P(E) and d=min(epsilon,m). Remove d mass in increasing J order. Because J has finite support, full levels and at most one fractional boundary level suffice. A single independent Bernoulli coin, with any real probability in [0,1], implements the fractional level. This is a finite augmentation; no continuous auxiliary variable is required, no original stack law changes, and no concentration is conditioned on E or E'. For every integer w>=1,

    P(E',J<w)=max(0,P(E,J<w)-d)<=bw,
    P(E')<=q0.

If epsilon>=m the trimmed event is empty and its contributions vanish directly. Otherwise d=epsilon gives the inequality from the count input. R008 uses positive q0 as an upper mass in the logarithm, never the possibly zero actual mass of E'. Thus null events create no log(0), division by zero or undefined conditional law.

S020 with q=q0 and c=b/q0 yields E[ell_q 1_E']<=B. R001's radius lemma, on this SAME event, yields E[rho(J)1_E']<=(8/5)B. Its layer-cake proof uses integer thresholds ceil(4096K/t^2-K) and is valid for upper masses, including a null event. The removed portion contributes at most d to each of original loss and radius. Therefore

    E[ell_ALG 1_E]
      <=2d+B+(8/5)B
      <=2epsilon+(13/5)B
      <=(4+2080)/K=2084/K.

Using the direct ALG loss cap could improve the removal constant, but R008's factor two is valid and sufficient.

## 4. Grouped pair-success transfer, not scalar GS

At this critical ray a=sqrt(K^3/(K^5+1))<1 and a<=1/K. Hence R004's nontrivial event partition exists for EVERY admitted K (M>=32, r>=16); its a=1 scalar-cap shortcut is never needed. Write h=floor(r/2), H=h+1. Early labels j<=h form Fearly. Late labels form F_v according to v<=r-j+1<2v for powers of two v<=H. The last success with zero suffix is included in v=1. These disjoint groups partition Eplus.

Their actual event certificate parameters are

    Fearly: (q,b)=(1,K^2/(r+1)),
    F_v: (q,b)=(q_v,q_v K^2/v), q_v=beta v delta^h in (0,1).

The mass caps may exceed actual event masses, which both S020 and R001 allow. For D(q,b)=min(q,80sqrt(qb[K+log(1/q)])), define C as the sum of these capped certificates. R004's early bound <=114a and dyadic late bound <=5920a bound C itself, not just actual loss, because dropping certificate caps only increases their expressions. Thus C<=6034a<6400a.

For each SAME group, R001 bounds radius by (8/5)D(q,b). Adding groupwise safety gives

    E[ell_ALG 1_Eplus]<=(13/5)C<=16640a<=16640/K.

This verifies precisely the additional information needed for same-ALG transfer. It would not follow from the scalar GS assertion alone; R008 explicitly and correctly imports the event partition and certificates instead.

## 5. Cover, total constant and cap

G has mass delta^M<=1/K. Original loss and rho are individually at most one, so its safety contribution is at most 2/K. No residual-stack conditional theorem is needed here.

G, E and Eplus cover the joint space: pair failure is either no symbol success or symbol success, and pair success is Eplus. G may overlap Eplus; nonnegative loss allows the cover sum, and disjointness is not falsely required. Therefore

    risk(ALG)<=2084/K+2/K+16640/K=18726/K<20000/K.

Independently TV loss is at most one. Taking both bounds proves min(1,20000/K) for every K>=2, including small K where this certificate is trivial. Every departure and the actual endpoint are retained throughout.

## 6. Matching and preserved scope

Accepted R002 Section 2 supplies a genuine common-predictor statistical lower Omega(1/K) on its legal star family, with full original observations and the actual endpoint. It is asymptotic in K and applies to randomized predictors as well, not merely original add-one. That family is contained in the absorbing subclass. Minimax monotonicity therefore transfers its lower to the entire subclass; minimax is no larger than this fixed ALG's worst risk, and R008 supplies the uniform O(1/K) upper. Both quantities are consequently Theta(1/K) asymptotically.

This does not claim a lower for every individual source, a finite all-K matching lower, a general-pi upper, a zero-risk endpoint result, an all-parameter absorbing adaptation theorem, or a minimax conclusion drawn from an occupation obstruction. R007, missing S026–S032 bytes and unproved (O) are not premises. The corollary establishes exactly the useful SAME-ALG critical-ray extension of accepted R006.

## Final disposition

**ACCEPT, no substantive or editorial revision required for the stated corollary.** Frozen sources remain unchanged. No unresolved scientific check remains within this review.
