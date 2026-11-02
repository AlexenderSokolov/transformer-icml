# S021 v2 有界修复的独立数学复核

编排说明（非原文）：本文件保留完整科学证明或完整科学审查推理；只省略身份控制、原提交状态、管理路径、重复来源管理表与执行记录。所有复制区间逐字节保留，原件未改；新增、复制和省略字节区间及原件全文身份见 COPY_MAP.json。原章节号和审查所引行号沿用原件，不是本副本行号；按同名章节与公式定位。来源的准确科学版本和当前可读闭包见 SOURCES.md。有限枚举只是补充证据，不是证明或形式化验证。本次装配没有重做数学审查。

当前判断：v2 的 R1 和 N1 均通过，随后最终接纳。复核是完整 v1 科学审查加 v2 精确差异核查，不冒称另一次全新全文数学审查。原文对修复报告、旧检查器与源行号的提及是历史证据；本包中的完整 v1 反例已经逐字节保留。

The original v1 remains **NEEDS REVISION**, with its false standalone statement, counterexample, and independent report preserved unchanged. Acceptance here binds only the exact v2 bytes below; it does not retroactively accept v1.


## R1 — Initialization scope: PASS

**v2 locations:** line 123, “Under conditions 1–4”; line 133, explicit use of condition 4's common initialization supported in a specified phase `D_k`. The definition of condition 4 remains unchanged at line 115.

This is precisely the smallest safe repair requested in the full review. Starting in `D_k`, before the first failed scheduled vulnerable coin, induction through safe/vulnerable phases places the actual process in its scheduled actual-pair phase. Therefore the forced-zero-successor argument applies to the actual vulnerable row. The fixed initialization also makes the vulnerable schedule/count deterministic and parameter-independent. On G, the full base history is recovered and condition 4 puts the actual terminal pair in S. Thus the survival/default-target statements now have all the assumptions their proof uses.

The structural inequalities `L<=K²−1`, `Z<=min(K−1,floor(L/2))` remain valid under the stronger local assumption set. No circularity is introduced: condition 4 specifies the base experiment, while the coin coupling proves the corresponding actual-source conditional experiment and complement target. Lemma B and Theorem C already required conditions 1–4, so no downstream formula or scope expansion is involved.

The old counterexample remains a genuine counterexample to v1: its `mu=delta_(2,2)` is outside `D_0={(1,1)}` and hence fails the initialization now expressly required by v2. It was excluded by the corrected hypothesis, not disproved, erased, or mislabeled. The full counterexample subsection is retained verbatim in the repair report; the saved v1 checker still reproduces it.

## N1 — Public-null-history completion: PASS

**v2 location:** line 27 now outputs `delta_0` if terminal membership is in U×V but the complete observed history is outside S015 Lemma 4's public base reconstruction support.

This support is known from the geometry and common horizon-aligned initialization, not from hidden signs or row values. Every inherited paired-sign W law is strictly positive, so the support used here is common across the entire finite family. On it, all observed departures from a U×V row have W labels and `sum_w C_s(w)=N_s`; the positive-count empirical law is normalized. At zero count, Unif(W) is normalized. On all remaining histories, the new fixed-output guard (or the outside-U×V branch) is normalized. Thus this defines a common kernel on the full original history space.

For the actual family, terminal membership in U×V implies G and therefore implies membership in that public base support. The newly assigned branch is common-null and does not alter any risk calculation or conditional experiment. In particular the review's `(u,v,0,u,v)` history is rejected and assigned delta_0. No latent G indicator, sign, future data, or source-specific support is furnished to the predictor.

## Exact-diff confinement and inherited five-unit disposition

The saved unified diff was applied **in memory**, checking every removed/context line, and reconstructed the frozen v2 exactly. Independent line comparison found six changed regions only:

1. Version heading.
2. Historical bounded-repair note.
3. Preliminary empirical predictor's N1 support guard.
4. Lemma A's R1 assumption heading.
5. Lemma A's explicit initialized-phase sentence.
6. Versioned freeze/preservation note.

The complete Theorem C / finite weak-hazard domain / requested-ray block is byte-identical. The direct-source-binding section is byte-identical. All other scientific material is unchanged.

| Contracted unit | v2 disposition | Basis |
|---|---|---|
| 1. Exact S015 center/empirical risk, finite scales, S012 comparison | PASS | Full v1 unit audit inherited; N1 independently resolved above |
| 2. Safe-count structure and survival bridge | PASS | Full v1 structural/proof audit inherited; R1 independently resolved above |
| 3. Observable arbitrary-row predictor and selected-endpoint product law | PASS | Unchanged conditions-1–4 statement/proof; full v1 audit inherited |
| 4. Finite all-period envelope, weak-hazard corollary and K⁵ ray | PASS | Entire result/proof block byte-identical; full v1 audit inherited |
| 5. Failed Euler membership, state-dependent membership recipe and successor limitations | PASS, membership only | Unchanged material; full v1 audit inherited; no successor prediction lower accepted |

The accepted main scope remains **one fixed public template** with all four explicit conditions, including full observed product data and independent uniform actual endpoint. For `K>=2`, `M>=K⁵`, `0<beta<1`, `delta=1-beta`, its restricted minimax upper is

    min{1, delta^(-K²) max(sqrt(2K⁴/M) delta^(M/2),
                            sqrt(K⁵/M) delta^(M(1-1/K)))}.

On `M=K⁵`, `beta=ln K/(2K⁵)`, this is at most `5K^(-1/2)`. The exact S015 shrinking family has restricted rate `Theta(K^(-3/4))`, and the exact S012 family has restricted rate `Theta(K^(-1/2))`. These do not supply a full-class upper, an unknown-geometry-mixture upper, a stronger full-class lower, or a completed minimax rate. The state-dependent absorption construction has accepted all-state membership only; its harder statistical testing problem remains open.


