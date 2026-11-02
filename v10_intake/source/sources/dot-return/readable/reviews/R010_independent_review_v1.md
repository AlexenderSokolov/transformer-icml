编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# Independent mathematical review of R010 v1

Date: 2026-10-30 UTC. Independent mathematical review.

## Verdict: ACCEPT

The frozen candidate proves the stated original-add-one expected-TV lower for every integer K>=2, M>=1. Its inherited IID upper and strong-beta original-rule upper are correctly identified and applied. No mathematical revision is required. This acceptance concerns a **new reconstruction**, not recovered historical S027 bytes, historical provenance, novelty, or a common-algorithm minimax lower at rate a.

The source files were read but not edited.

## Exact inspected identities

Public scientific locators are in SOURCE_INDEX.json.

1. Candidate: `proofs/R010_original_iid_lower_reconstruction_v1.md`
   SHA256: `df55677a4594521c428c8bf4ac93f0fbf5ec8e0ed7f46595b049648249889ace`.
2. Recovered full S022: `S022 (SOURCE_INDEX.json)`
   SHA256: `028f43ae12886781bfd3641712c66720d24c667b59ca22a74c5dbbea5b0a5774`.
   In particular Sections 1–4 were read, including the full multinomial and boundary-restoration proofs.
3. Recovered full S011: `S011 (SOURCE_INDEX.json)`
   SHA256: `8286e13dabe19b4b7adc72ab11bc65a5a8594f70c507c6321bc398f46860c762`.
   Its original-rule certificate, condition B, finite absorption proof, strong-beta specialization, and separate beta-one convention were checked directly. S024 was not needed as a substitute interface.

## 1. Experiment and quantifiers

S022 and S011 define exactly M observed departures, indexed 0 through M−1, and target the actual terminal pair Y_M=(X_(M+1),X_(M+2)). R010 uses this same experiment and original K-letter add-one vector. Its witnesses choose mu=p tensor p, a permitted subclass of the arbitrary-initialization supremum; hence every symbol is genuinely IID in the lower constructions. Restricting initialization for a lower is legitimate. The upper remains uniform in arbitrary mu.

Neither the lower witness nor its analysis changes the algorithm, target, available observations, or full-history experiment. In particular, the auxiliary truncation is restored rather than used as the reported estimator.

## 2. Small and moderate horizons

For d=floor(K/2), d>=K/3 for all K>=2, including K=2 and K=3. For disjoint uniform-d pairs, equality has probability 1/d². The unique overlapping pair j=M−1 has equality precisely when three consecutive symbols agree, also of probability d/d³=1/d². Thus E J=M/d² is correct, even at M=1 or d=1.

The estimator has outside-support mass (K−d)/(J+K), and TV is at least that mass by the defining supremum over subsets. Jensen for the convex reciprocal gives

    E TV >= (K−d)/(M/d²+K) >= 1/(2+18M/K³).

For M<128K³ this is at least 1/2306, strictly above 2^−24 a since a<=1. This covers zero counts, all capped cases, and the small alphabet cases without any occupancy approximation.

## 3. Large-horizon second and fourth moments

For M>=128K³, L=M−2 auxiliary departures end at j=M−3, so the last symbol they use is X_M. The entire auxiliary vector is independent of the actual terminal pair, whose symbols are X_(M+1), X_(M+2). This independence is unconditional under the chosen stationary IID law and therefore remains available when conditioning on any fixed terminal row.

For a fixed row/output, define F_j=sigma(X_1,...,X_(j+2)). Z_j is F_(j+1)-measurable and has conditional mean zero given F_j. For i<j, Z_i is F_j-measurable. Thus orthogonality and E S²=Lv hold, with v=(K−1)/K⁴ between 1/(2K³) and 1/K³.

I independently checked every partition of four index multiplicities:

* [4]: sum <=Lv.
* [3,1]: when the largest index has exponent one, conditioning kills the term. In the other ordering, a gap >=3 separates the triples and the earlier singleton has mean zero. At most 2L close pairs remain; coefficient 4 and |Z_i Z_j³|<=|Z_j|³<=Z_j² give <=8Lv.
* [2,2]: separated pairs have expectation v²; at most 2L close pairs each have expectation <=v. Coefficient 6 gives <=3L²v²+12Lv. Overcounting separated pairs by all unordered pairs is an upper bound.
* [2,1,1]: only the largest-index-squared ordering survives. If j−i>=3, the first triple is independent of both later triples. If k−j>=3, the last triple is independent of the two earlier triples, whose product has expectation zero by orthogonality. Thus both gaps must lie in {1,2}; there are at most 4L triples, each bounded in absolute expectation by v, with coefficient 12. Contribution <=48Lv.
* [1,1,1,1]: the largest singleton has conditional mean zero.

The cases are exhaustive and the coefficients are correct. Equal-symbol contexts cause no exception. Therefore E S⁴<=69Lv+3L²v² is valid universally; the proof does not assume adjacent triples independent.

Since L>=M/2, sigma²=Lv>=M/(4K³)>=32. Consequently E S⁴<=72 sigma⁴ (indeed the resulting constant could be much smaller). Cauchy–Schwarz on the event S²>=sigma²/2 gives probability at least 1/288 exactly as claimed. This is a lower probability argument from second and fourth moments, not the invalid square root of an expected-squared-loss lower.

## 4. Dependent denominator and original boundary restoration

Given terminal row s, all L auxiliary context indicators still have expectation 1/K²; the remaining two context indicators are each at most one. Thus E[J_s+K | Y_M=s]<=m_D=L/K²+K+2. Markov gives a bad-denominator probability <=1/576 at threshold 576m_D. Subtracting this from the 1/288 noise event yields joint probability >=1/576. The argument permits arbitrary correlation between S and J_s.

The original numerator C_s(c)−J_s/K differs from S by precisely the departures j=M−2 and j=M−1. Each centered contribution has magnitude <=1 even after endpoint conditioning. Add-one prior bias cancels exactly for uniform p, so there is no unaccounted smoothing term. Since sigma>=sqrt(32), sigma/sqrt(2)−2>=sigma/(2sqrt(2)).

Also L/K²>=K+2 follows already from L>=M/2>=64K³ and K>=2. Hence m_D<=2L/K², and the displayed coordinate lower is

    sigma/(576 * 2sqrt(2) * 1152 L/K²)
       >= sqrt(K)/(2654208 sqrt(L)).

Summing coordinate expectations and then averaging terminal rows is legitimate without simultaneous coordinate events. Half the L1 sum gives K^(3/2)/(5308416 sqrt(L)). Since L<M+1 and a is uncapped in this regime, this is at least a/5308416>=2^−24 a. Both restoration and numerical constants check.

## 5. Inherited uppers and membership

S022 Sections 3–4 establish E TV(q,p)²<=min(1,423K³/(M+1)) for the same ORIGINAL q and every p,mu. The disjoint-triple multinomial law is limited to auxiliary fixed-row residue groups, as required. The proof restores four boundaries for arbitrary mu, uses pathwise convexity for random weights, obtains 47K³/(L_*+1), and checks L_*+1>=(M+1)/9. Its square-root use is an upper via Cauchy–Schwarz, giving R010's sqrt(423) bound; no lower is inferred this way.

For any all-row IID p, the legal pair kernel satisfies P²(s,(c,d))=p(c)p(d) for every starting pair, including off-support pairs. The law pi=p tensor p is stationary. Thus the witnesses satisfy all-state minorization for every beta in [0,1], not merely on their stationary support.

S011's condition B bounds the unchanged original rule by min(1,81a), not only a suffix or common selector. Its proof uses the separate original certificate (2.1) and the deterministic burn only analytically. For beta>=1/2 and M>=32, q=floor(M/4)>=8, and 2^q>=4q+4>=M+1 proves B. At beta=1, S011 defines h_b=0 for b>=2, avoiding 0^0 and residual division. Here b=floor(M/2)>=16, so the same conclusion applies. For M<32, a>=1/2 and the loss cap suffices. R010's inheritance is therefore sound.

## 6. Supplemental check and limits

An exact integer-scaled finite enumeration checked E S=0, E S²=Lv, and E S⁴<=69Lv+3L²v² for all row/output choices at K=2, L=1,...,8 and K=3, L=1,...,6: 226 cases, all passed. Constants 2654208 and 5308416<2^24 were separately checked. These finite checks supplement, and do not replace, the universal multiplicity proof above.

The accepted conclusions are the original-rule IID order a, the every-beta original-rule lower 2^−24 a, and strong-beta original-rule upper 81a, all in expected actual-terminal TV. No conclusion about recovering S027, an optimal numerical constant, common minimax rate a in the IID class, the whole weak-beta original-rule rate, or external novelty is licensed by this review.


