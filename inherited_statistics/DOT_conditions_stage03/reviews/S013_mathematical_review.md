# S013 原独立数学审查的科学正文

编排说明（非原文）：原独立审查日期为 2026-10-28，结论 ACCEPTED，无数学修复要求。以下保留原审查的完整逐引理推理、科学适用范围与有限检查事实；身份及运行元数据省略。审查绑定原证明哈希，而非这份新复制件。独立上下文 LLM 审查不是形式验证，也不是外部同行评审。下文有限检查是原审查历史结果，本次编排未重跑；原命令、脚本和运行记录不在本包内。



## Accepted Mathematical Scope

For every `0<beta<1`, set `q=1-beta` and define successor-one probabilities on rows `(00,01,10,11)` as `(1,beta,1,1)`. The resulting homogeneous legal binary pair shift has unique stationary law `pi=delta_11`, exact maximal all-state two-step minorization coefficient beta, and

    TV(delta_10 P^t,pi)=q^floor(t/2),  every integer t>=0.

Thus this is the exact supremal state-law distance over `D_2(2,beta)` and arbitrary initial laws at each time, by the accepted S011 upper envelope. At every fixed interior beta, no finite nonnegative C permits a uniform-in-time replacement by `C(1-beta)^t`, even if C depends on that fixed beta. For each fixed `c>1/2`, no finite nonnegative C independent of beta and t permits `C exp(-c beta t)` uniformly over the class. Fixed-K dependence in those constants is harmless because K=2 is fixed.

At beta zero, the displayed family has all stationary laws `a delta_11+(1-a)(delta_01+delta_10)/2`, maximal all-state coefficient zero, and distance one from initial 10 to the witness delta_11 forever. At beta one, the unique stationary law is delta_11 and all initial pairs reset there within two steps; the initial-10 distance is one at times zero and one and zero thereafter.

For the known family with public beta, the endpoint-only predictor in Proposition 6 exactly returns the target row for every history, every arbitrary initial law and every M>=1, including both beta endpoints. Its definition is also a legal common algorithm on the full class, but zero risk is asserted only on the specified family. The full-class beta parameter remains a lower bound, not an oracle for an unknown table or maximal coefficient.

## Per-Lemma Audit

### unit_001 — Proposition 1: Legal absorbing pair shift (`prop:s013-kernel`)

- **Statement fidelity:** exactly K=2, interior beta, legal homogeneous shifts, uniqueness and maximal coefficient over all stationary witnesses; no irreducibility, full-support or recurrent-start assumption.
- **Proof validity:** the four rows of P follow directly from `(a,b)->(b,c)`. Multiplication gives the stated P-squared rows: residual mass q is at 10 for starts 00 and 10, at 01 for start 01, and all other mass is at 11. The stationary equations force `nu(00)=0`, `nu(01)=nu(10)=q nu(01)`, hence all mass at 11 for beta>0.
- **Coefficient and assumptions:** targets outside 11 have zero stationary mass and impose no positive lower bound. At target 11 the four probabilities are `(beta,beta,beta,1)`, so beta works and no larger coefficient works. Uniqueness discharges the optimization over stationary witnesses; it is not assumed.
- **Adversarial check:** the transient state 00 is included in the all-state condition. Initial pair 10 has zero pi mass but is explicitly allowed by the contract. Direct exact-arithmetic multiplication also passed at interior and endpoint parameters.
- **Contribution:** supplies the lawful example and its exact class parameter before the survival argument.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Invariant 2: Alternating surviving mass (`inv:s013-survival`)

- **Statement fidelity:** the invariant is named, its initial law is specified, and both identities quantify over every integer m>=0.
- **Proof validity:** the even base m=0 is exactly delta_10. One step maps 10 to 01 and fixes 11. The following step sends the surviving 01 mass to q times 10 and beta times 11, giving absorbing mass `q^m beta+1-q^m=1-q^(m+1)`. This is a genuine induction, not a spectral or asymptotic surrogate.
- **Assumption audit:** P and q come from Proposition 1; no generated invariant is treated as a primitive assumption.
- **Adversarial check:** the first four laws are delta_10, delta_01, `q delta_10+beta delta_11`, and `q delta_01+beta delta_11`, so the floor exponent and parity are correctly aligned.
- **Contribution:** establishes the complete time-dependent probability law used in exact sharpness.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Proposition 3: Exact uniform-envelope sharpness (`prop:s013-sharp`)

- **Statement fidelity:** exact TV with coefficient one, all deterministic integer times including 0 and 1; this is state-law TV, not terminal-row prediction loss.
- **Proof validity:** for a probability nu, `TV(nu,delta_11)=1-nu(11)` under the stated half-L1 normalization. Applying both invariant identities yields exactly `q^floor(t/2)`. The same source and initialization attain the bound at all times.
- **Cited-result audit:** S011 Lemma 1, `lem:s011-contract`, is restated in current notation, independently read and checked. Its residual stochastic kernel contracts TV without stationary-support or reversibility assumptions. Its endpoint-safe h_t and stronger intermediate factor `TV(mu,pi)` are exactly as used; the witness has initial TV one.
- **Adversarial check:** t=0,1 give one, not q; t=2,3 give q. Membership was proved for every start, not only a recurrent subset. The supremum statement needs only the stated uniform upper and this matching witness, with no interchange of a limit and supremum.
- **Contribution:** exactly closes the sharp state-law-envelope target, not a statistical rate target.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Proposition 4: Faster-exponent negations (`prop:s013-negation`)

- **Statement fidelity:** first fix an interior beta and then allow every finite C; separately fix any c>1/2 and finite C before choosing beta and t. C may depend on fixed K=2, but the second negation disallows dependence on varying beta or t. The assertions do not rule out c<=1/2.
- **First negation:** for C>0, `lambda=-log q>0` and the displayed finite integer `m=1+floor(max(0,log C)/lambda)` satisfies `m lambda>log C`, including C<1 and C=1. At t=2m the ratio is `exp(m lambda)>C`. C=0 fails already at time zero. Even beta-dependent C cannot fix the claim for that fixed beta.
- **Second negation:** `beta=(2c-1)/(4c)` is strictly between zero and one half. The integral estimate `lambda<=beta/(1-beta)` and `1/(1-beta)=4c/(2c+1)<2c` show `d=2c beta-lambda>0`. Thus the same integer selection using d is finite and gives ratio `exp(md)>C`. Every division and logarithm is justified before use. The extension to arbitrarily small positive beta follows from the sufficient strict condition `beta<1-1/(2c)`.
- **Adversarial check:** c approaching one half from above still gives positive beta and d; C=0, C<1, C=1 and large finite C all have explicit handling. No limiting approximation is needed for either counterexample.
- **Contribution:** establishes precisely the two forbidden uniform exponential improvements without asserting statistical impossibility.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Proposition 5: Endpoint laws (`prop:s013-endpoints`)

- **Statement fidelity:** the same row definitions are evaluated directly at both endpoints, and beta-zero nonuniqueness is explicit.
- **Beta zero:** the only recurrent classes are the 01/10 two-cycle and the absorbing singleton 11. The stationary coordinate equations give exactly the stated convex family. Any witness with positive cycle mass fails positive all-state minorization from state 11; the pure delta_11 witness fails it from state 10. Thus optimization over stationary witnesses still gives coefficient zero. From 10 the alternating point masses remain TV one from delta_11.
- **Beta one:** all successor symbols are one, so P-squared has every row delta_11, stationary uniqueness follows, and the maximal coefficient is one by probability row sums. The first two transitions from 10 are 10 to 01 to 11.
- **Baseline audit:** h_t is identically one at beta zero; at beta one h_0=h_1=1 and h_t=0 for t>=2. The exact inherited endpoint conclusions are preserved without `0^0`, a fictitious beta-zero uniqueness statement, or an early one-step reset from 10.
- **Contribution:** closes both optional endpoint obligations without changing the interior theorem.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Proposition 6: Known-family zero prediction loss (`prop:s013-zero-risk`)

- **Statement fidelity:** the original full-history actual-terminal experiment is retained, M>=1 and arbitrary mu are allowed, and family knowledge plus public beta are explicit.
- **Proof validity:** `Y_M=(X_(M+1),X_(M+2))` is observed. Outputting successor-one probability beta precisely on row 01 and one on the other rows returns the table row exactly on every history, including histories of probability zero. The output is a probability vector for all beta in [0,1]. Loss is therefore pathwise zero, hence expected loss zero.
- **Information audit:** the map uses the endpoint and public data only; it reads neither mu nor hidden pi nor the future. Fixing this known-family map also defines an admissible algorithm on the full class, but its exactness is not asserted for other unknown sources. There is no hidden maximal-coefficient oracle.
- **Adversarial check:** histories beginning in 00, all initial point masses, M=1, both endpoints and both terminal-pair parities are covered. An independent enumeration of binary histories for M=1,...,7 passed; the universal argument is the row-by-row equality, not enumeration.
- **Contribution:** positively demonstrates why this state-law witness alone is not an arbitrary-algorithm prediction minimax lower. This does not assert that the full-class minimax risk is zero.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim Scan

No unsupported independent subclaim was found. Full matrix legality, stationary uniqueness and optimization over stationary witnesses are contained in Proposition 1; the recurring hypothesis is the named Invariant 2; exact supremal sharpness and the stronger initial-TV intermediate equality are contained in Proposition 3; the two finite-C negations and arbitrarily-small-beta extension are contained in Proposition 4; endpoint stationarity and coefficients are contained in Proposition 5; pathwise exact prediction and its scope are contained in Proposition 6. The general stochastic-TV contraction bridge is both restated and derived using the checked S011 interface. No candidate numerical screen, source-priority claim or unreviewed statistical theorem enters the proof.

## Target Claim Audit

The complete bounded contract is proved under its original conditions. The class includes zeros in pi and legal transition probabilities, reducibility and arbitrary initial laws. Homogeneity is genuine. The dependence and quantifier order are preserved; K remains two, beta is fixed or varied exactly as declared, and t is deterministic and integer. No source-dependent C, stopping-time extension, independent test query, recurrent-support restriction or unknown-table disclosure is introduced. The fresh exact obstruction strengthens the relevant mixing conclusion without changing or withdrawing the accepted S011 copy-family obstruction.

## Explicit Rate Audit

- Exposed variables: beta and t; M occurs only in the separate zero-risk comparison. K=2 is fixed.
- Norm and mode: half-L1 TV of probability laws, deterministically exact, all integer times. Prediction TV is separately pathwise zero and hence zero in expectation.
- Constants: the exact envelope has coefficient one. Every finite C in the two negations is accounted for; fixed c>1/2 is quantified before beta and t in the second. There is no hidden constant or unproved term absorption.
- Auxiliary parameters: q, lambda, d and m are explicitly derived; positivity and finiteness precede their use. The integral inequality supplies the strict margin needed for d.
- Baselines: beta zero, beta one, t=0 and t=1 are all directly traced. Both parities are proved rather than inferred asymptotically.
- No probability conversion, limit exchange or asymptotic-only quantifier upgrade is used. No claim is made for optimal exponential constants c<=1/2, full prediction-risk sharpness or the remaining joint-rate problem.

## Notation Surface Audit

The public source, P, pi, initial law, time and exact TV claim are explicitly identified. q, Pi, Q, stationary coordinates and exponent-counterexample auxiliaries remain proof-local. The family-specific predictor is public-facing only as a non-lower-bound witness. Every helper is defined from declared parameters or already proved objects. The six named theorem-style results and stable labels make the assembly traceable without relying on audit unit numbers as mathematical authority. No unnecessary helper dictionary or unproved derived invariant is exported.

## Target-Step Assembly Audit

Proposition 1 constructs a source satisfying the original all-state condition with exact beta. Invariant 2 gives its full state law. Proposition 3 combines it with S011 Lemma 1 to establish equality with the generic envelope. Proposition 4 negates the two proposed faster uniform forms. Proposition 5 checks endpoint baselines; Proposition 6 discharges the requested mixing-versus-prediction distinction. These named results cover every contract obligation with no new bridge, model change or dependency repair needed.


## Independent Finite Sanity Checks

A reviewer-owned inline Python command independently constructed the pair matrix from the successor table using exact `fractions.Fraction` arithmetic, rather than importing a producer checker. For beta in `{0,1/1000,1/7,1/2,6/7,999/1000,1}`, it checked the complete matrix square, exact minimal two-step 11 mass, 1,820 all-start/time TV cases (all four initial point masses, t=0,...,64), the exact initial-10 parity laws, several beta-zero stationary mixtures, and 7,112 binary-history predictor equalities for M=1,...,7. Six rational values of c, including 500001/1000000, also passed the exact positive lower-bound check `2c beta-beta/(1-beta)>0` at the prescribed beta. All checks passed.

These finite computations supplement, but do not replace, the independently checked algebra, induction and real-parameter inequalities. They do not constitute formal verification or evidence about other unknown source families.

## Review Rationale

ACCEPTED is warranted because every bounded-contract obligation is proved by the frozen artifact, the only mathematical dependency is precisely restated and validly bound to an actually accepted S011 interface, and the statistical nonimplication is explicitly demonstrated rather than merely asserted. No repair target is needed.
