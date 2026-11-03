# Fixed-half gate on slow sources: scope audit and retraction

2026-11-03. Author-side mathematical analysis; independent review required. No new random sampling, model fitting, or public writes. No deterministic numerical test was run. This is an audit of a proposed finite-episode lower bound, not a claim of an independently novel theorem.

## 1. Finding and retraction

The proposed certification separation used clean episodes from a slow-source alternative Q_a and an adversarial risk lower bound on a different null source Q_*. That cross-source construction cannot establish an episode-complexity lower bound when training and testing are required to use the same source or a fixed mixture. Indeed, the very rejection region hiding the feature under Q_a is observed with constant probability under Q_*. Furthermore the count-only predictor has a direct O(k/M) risk upper on every Q_a for k≈M^(3/4). Hence neither the individual Q_a nor any mixture supported entirely on that family supplies the originally proposed logarithmic risk separation in this budget regime.

The cross-source observation itself can be derived from accepted ingredients, but the original proposal must not be presented as a same-source lower or a learning impossibility. White-box access, arbitrary input queries, analytically implementing the known fixed gate, or changing the training prior all invalidate its restricted observation interpretation.

## 2. Source, training and prediction definitions

M≥64, integer k and manuscript Proposition B.3's domain: c=2^-16, A=2^12, t=ck/M, 2≤r≤k/128, k≤M/8, ck≥1024, At<1/4, and M/k²≤Ac²/2^20. The protected endpoint is U=(X_M,X_{M+1}); W=(X_0,...,X_{M+1}), with M historical departures. The label V=X_{M+2} is not part of W, the row counts, the attack or gate. Every training episode is an independent stationary trajectory; in the null-source experiment below all episodes have the same fixed Q_*. For an alternative training experiment, one may first independently draw a∈[At,1/4] from a specified prior, then draw a stationary Q_a trajectory; the conditional results are uniform in a. Source parameters can be supplied to the certifier: none of our indistinguishability calculations relies on keeping them secret.

The manuscript Q_a transition table, ordered by pair 00,01,10,11, is

  P_a = [[1−a,a,0,0], [0,0,1/2,1/2], [1/2,1/2,0,0], [0,0,t,1−t]],
  π_a=(t/a,2t,2t,1)/D_a, D_a=1+t/a+4t.

These stationary sources have the all-state certificate β=1/M under the stated domain, as verified in B.3. They are NOT AB001's different Q_a, which was only asserted at β=0.

The stationary Q_* is a binary first-order source with T(0,1)=β=1/M and T(1,0)=q*=1/(2M), stationary symbol masses (1/3,2/3), and induced pair process. It also meets the all-state β=1/M certificate. The next-symbol target is its original row at the protected endpoint; in particular target probability of 1 at 00 is 1/M.

For a word w, J_u counts departures from row u, C_u counts those whose following symbol is 1, and D_u counts row-u departures with index i<floor(M/2). For its endpoint u define

  B(w)=(C_u+1)/(J_u+2), F(w)=first(u),
  G(w)=1{J_u>0 and 512D_u≥J_u}, B_G(w)=G(w)B(w)+(1−G(w))F(w),
  s=M^-1/2, q_0(w)=s+(1−2s)B(w), q_1(w)=s+(1−2s)B_G(w).

The same B, F, G and smoothing are used in both. They agree on every G=1 word. On G=0, B lies strictly between 0 and 1 and F∈{0,1}, so they differ. They are explicit fixed programs, not two fitted networks or evidence of feature learning.

## 3. Matched-null clean episodes distinguish them

For j=2,...,T=floor(M/8), let x(j)=1^(M+2−j)0^j. It is a complete word of M+2 symbols with endpoint 00 and initial pair 11. All its early-half row-00 counts vanish, hence D_00=0; J_00=j−2 and C_00=0. Thus G(x(j))=0, F(x(j))=0, B(x(j))=1/j, and

  q_1(x(j))=s,
  q_0(x(j))−q_1(x(j))=(1−2s)/j ≥6/M.

The last inequality uses M≥64, s≤1/8 and j≤M/8. These words are disjoint. Their exact stationary Q_* word masses are, by B.3 (B.14),

  v_j=(2/3)(1−q*)^(M+1−j) q*(1−β)^(j−1) ≥1/(8M).

Since floor(M/8)−1≥M/16 for M≥64, the union E of these words has probability at least 1/128. Independent Q_* episodes give P(no E in N)≤(1−1/128)^N≤exp(−N/128).

In the restricted identification experiment, an oracle is one of the two *known candidate functions* q_0,q_1, held fixed. A certifier receives independent clean Q_* words and the oracle's output only at those words; it may know the source and the words, and may also see next-labels. Upon seeing E it compares the output with s+3/M. If both the oracle output and the public s are each computed with absolute error at most 1/M, the combined error is ≤2/M, so the threshold still separates a zero gap from a gap ≥6/M. The certifier can choose randomly if E never occurs, or declare inconclusive. For N≥128 log(1/δ), probability of an inconclusive outcome is ≤δ. This is a sufficient upper bound for this two-candidate identification task, not a lower bound for training, robustness certification in general, or arbitrary model classes. It uses probabilities/labels from clean episodes only and never exposes the future label to the predictor or attacker.

If each stationary training episode independently draws from w Q_*+(1−w)P_alt for any w>0, the same E probability is ≥w/128, so N≥(128/w)log(1/δ) suffices. This is constant in M only for a weight w bounded below independently of M. If w=w(M) tends to zero, the upper scales as 1/w(M). No assertion is made about arbitrary dependent episode draws.

At accuracy 1/M, output words need O(log M) bits. Computing B and G from the same word needs a one-pass counter for each of four row occupancies, successor-one counts and first-half occupancies plus endpoint, O(log M) auxiliary bits total, O(M) work, and paid division/output rounding. The threshold test is not a neural advantage.

## 4. No logarithmic count-only penalty on a single Q_a in this regime

Take any stationary manuscript Q_a, any source-independent or even source-aware strict-k word attack protecting the endpoint, and let Z be its output. The pathwise smoothing/ratio inequality in CTO001 gives

  |B(Z)−B(X)| ≤ min{1,12k/(J_U(X)+2)},

and the clean add-one error is ≤560/sqrt(M), uniformly over sources. The attack does not know or use V; the argument also holds for any randomized legal attack.

B.3 establishes a common atom with λ=a/4 and, for each stationary row occupation J_u over M departures,

  Var(J_u)≤7Mπ_u/λ.

Let H be the simultaneous event J_u≥Mπ_u/2 for all four rows. Since D_a<2, a≤1/4, and a≥At, every π_u≥t and λ≥At/4. Chebyshev and a union bound give

  P(H^c)≤Σ_u 28/(Mπ_uλ)≤112/(Mtλ)
        ≤448/(M A t²)=448·2^20 M/k².

On H, preserving the endpoint and stationarity P(U=u)=π_u yield

  E[1_H 12k/(J_U+2)]
     ≤Σ_u π_u ·24k/(Mπ_u)=96k/M.

Therefore uniformly over a and attacks,

  R_a(B)≤min{1,560 M^-1/2+96k/M+448·2^20 M/k²}.             (1)

The same holds for q_0 with an additional s. The theorem's nonempty range can be illustrated without floating numerical tests by the exact sequence M=2^(4n), k=2^(3n), n≥20 and r=2: every stated B.3 condition holds, and (1) is O(M^-1/4), not Ω(M^-1/4 log M). This bound is very loose at all practical scales: the constant multiplying M/k² is 469,762,048. No conclusion is drawn about smaller budgets or other sources. The accepted half gate has its own O(M^-1/2+k/M) all-critical-source guarantee, including Q_a and Q_*; that is the relevant same-information classical comparator.

## 5. What the failed cross-source proposal did show

For completeness, the author first proposed to train only on Q_a and test against the Q_* witness transport. One can quantify why its clean observations hide G. For each row u, m=floor(M/2), E D_u=mπ_u and Var(D_u)≤7mπ_u/λ. Since m−M/4≥M/8, Chebyshev gives P(D_u<Mπ_u/4)≤224/(Mπ_uλ), while P(J_u>2Mπ_u)≤7/(Mπ_uλ). If all four D_u≥Mπ_u/4 and J_u≤2Mπ_u, then G=1 for whichever U appears. Therefore

  P_Qa(G=0)≤min{1,3696/(M A t²)}
             =min{1,3696·2^20 M/k²}.                         (2)

For N independent Q_a episodes or a prior over Q_a, the probability of any G=0 is at most N times (2). An episode-only oracle transcript for the fixed q_0/q_1 candidates can consequently have total-variation distance at most that quantity, by coupling both transcripts on the same words and labels. This is only an observational upper bound in this restricted access model. It has no force when the certifier can inspect the code or actively choose words. In particular it is NOT a lower bound on any learning algorithm, and it does not establish matched-source robust risk separation.

The manuscript's count-window lower on Q_* can amplify alternatives integrated over a, whereas (1) says count-only B is competitive separately on the Q_a family at k≈M^3/4. Applying the former to Q_* but (2) to Q_a was the precise source mismatch. The matched Q_* clean calculation in §3 shows why that maneuver cannot be silently repaired with a constant-weight shared mixture.

## 6. Antecedents, status and limitations

Manuscript B.3 and proof: positional_manuscript_consolidated_20261103/main.tex, SHA-256 5c4a5a91e08a4ba0eaf40eff7b19010b88f3e6f3d616f80bdfa58ad1756f8fa1. CTO001 CANDIDATE.md SHA-256 1405c661827773bba64c8d8ae91f8eb8a9b2bf17ffc6a66e3be69525f1674bb2; PGT001 CANDIDATE.md SHA-256 91dcb755e6544fa04e728ab92bf48a7cb864e1e28fc9e4cbdbe0fc38257cb0be. AB001 full proof SHA-256 865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d. CTO's independently uniform row-parameter prior and independent uniform starting pair differ from the Q_a and Q_* stationary experiments here.

For external context, Ashtiani, Pathak and Urner, ICML 2020, https://proceedings.mlr.press/v119/ashtiani20a.html, already study black-box certification and learning under adversarial perturbations. Only their abstract was inspected here; this is no novelty audit or implication that their results prove or refute the source-specific calculations. This note supplies a scope correction, not a claim of an original robust-learning separation. The manuscript interfaces and CTO are imported, not reproved end-to-end. A full independent review remains required.
