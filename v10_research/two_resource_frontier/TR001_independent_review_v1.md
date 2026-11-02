# TR001 independent hostile composition review v1

2026-11-02. Reviewer: `independent LLM reviewer`, a separately spawned reviewing agent.

## Verdict

**PASS — no mathematical or scope blocker found for TR1 and TR2 on their stated domain.** Root acceptance remains a separate decision. No source or candidate file was edited.

Reviewed candidate: `TR001_two_resource_frontier_v1.md`, SHA-256 `7dca0c09637164c2a632e1e493c7af281109bb52116400c94ee507fe18c493c6`.

This is an independent LLM mathematical composition review with independently authored finite diagnostics, not formal verification, external peer review, literature priority certification or emitted-network testing.

## Sources and exact model

Read the complete candidate and its bindings, UI001's proof, SH001's lower proof and precise domain, SB001 v2's terminal construction, decoder cut, deterministic exceptional branches, paid ledger and §7 upper, AU001's whole-suffix mixture and scalar envelope, BA001's exact model, the relevant acceptance receipts, and FR001's original Q_star definition. All 13 bound source hashes match current bytes. The accepted receipts, rather than stale candidate-status headings inside manuscripts, determine the imported status.

The family in TR001 is exactly the required local positive-ratio family: at most D scalars, all M keys, trailing locality r, weights in [1,κ], values in [-1,1], downward Q-grid quantization, and exact side information derived only from the boundary S. The lower bounds allow more general real κ,Q and therefore apply to the integer-envelope/dyadic-grid subdomain here. The upper uses integer {1,κ} weights, length-three local features and exactly K³ coordinates. Its query is the final observed pair; at the synthetic next row the preceding pair is precisely that pair. Thus n=M+2 observations and n_prog=M+3 program rows are consistent, not an off-by-one inclusion error.

The decoder's access to only the terminal bank is preserved even though the paid program computes and stores other rows. The lower grants arbitrary real decoder outputs, so final simplex rounding in the explicit upper does not incorrectly produce the 1/Q necessity. That necessity truly comes from UI001. Shared source-independent randomness does not reveal the source. Permitting public β-dependent tables is consistent with every lower, which holds at each fixed class promise.

## Statistical lower

The IID Bernoulli witnesses satisfy the all-state certificate even on unsupported pair states by specifying the same emission law in every row. Their initialized observation law is n independent Bernoulli variables, so full-history KL is n times the one-observation KL. For δ=1/(16√n),

`KL = 2δ log((1+2δ)/(1−2δ)) ≤ 16δ²`,

because 2δ≤1/2. Hence history KL≤1/16; the weaker 1/8 and TV≤1/4 used in the manuscript are valid. Nearest-parameter testing gives Bayes absolute error at least (2δ)(1−TV)/4, which exceeds the stated 1/(128√n). Since n≤4M, c_S=1/256 is valid. Granting full history and independent seeds strengthens the experiment, so the floor transfers to every encoder.

## Exhaustive completion and constants

1. W decreases in z. The derivative is `[z/(t+z)−1−log(1+z/t)]/z²<0`. It also decreases in t, so W(z,t)≤W(z,1) for t≥1.
2. For β>1/16, W≤1/Q+16/M≤1/Q+2/√M. The separate floors imply R≥min(c_I/2,c_S/4)W. No SH theorem is invoked here.
3. For z>M/4, W≤4[1+log(1+M/4)]/M≤(9/2)/√M. The elementary logarithm inequality follows by integration; 1/(1+u)≤1/√u for u>0 is valid because √u≤1+u. Thus 5 is conservative.
4. For z>M^(3/4), √M≤z^(2/3). Therefore W√M≤[1+log(1+z)]/z^(1/3)≤1+log2+3/e<3. Again 5 is conservative. Overlap with the preceding branch is harmless.
5. The complement has β≤1/16 and z≤M/4, exactly the SH domain, as well as z^4≤M³. Setting x=z/t and y=M/z gives x≤z≤y³, y≥4. When x≤y, logarithm concavity gives log(1+x)≤8log(1+x/8). When x>y, `1+x≤1+y³≤(1+y)³`, followed by the same concavity bound, gives the factor 24. Thus W≤1/Q+24L. This reasoning includes equality at every cut, particularly β=1/16, z=M/4 and z=M^(3/4).
6. From R≥c_I/Q and R≥c_H L, the last bound yields R≥min(c_I/2,c_H/48)W. Together with the other branches, c=min(c_S/5,c_I/2,c_H/48) is no larger than every needed branch constant. It is also ≤c_S and ≤c_I, hence lower-bounds the maximum F, not merely W.

The three lower witnesses need not coincide. The manuscript correctly takes a maximum of uniformly valid lower bounds rather than summing risks or alleging a common least-favorable source. This is important in the IID-versus-rare-suffix composition.

## Upper and initialization

SB001 v2 §7 supplies precisely the displayed upper for all integer κ≥1 and all allowed grids, not only Q≈√M. Its proof uses AU001's occupation statements with arbitrary positive A, so substituting A=K(K+1)M/(κQ) has no hidden small-A or large-κ restriction. The residual suffix is an ordinary P trajectory from a residual initial distribution, not an R trajectory or a conditioned chain. At β=1 the residual disappears; β<1/M uses universal occupation. No problematic endpoint β remains.

The complete K³ triple bank separates mismatching pairs into other coordinates. The post-grid selected-block normalization, zero-sum fallback and final rounding remain identical to SB001, including positive J for which every selected coordinate floors to zero. The upper is therefore admissible without exact count or denominator leakage.

`2^13 Hstat+Ψ(K^5/(M+1)) ≤ (2^13+2)K^(5/2)/√M`, using the all-u capped Ψ bound. Adding the two numerical coefficients gives exactly the candidate C. Stationary sources are a subset for each fixed procedure, so infima preserve R_stat≤R_all in the stated direction. The explicit procedure then bounds R_all from above. Because F<1/4 on the whole domain, the unit loss cap creates no omitted asymptotic branch; the stated inequality min(1,CF) is consistent even where CF>1.

## Joint statistical-order threshold

The definition Z_star=√M[1+log(1+1/(√Mβ0))] agrees algebraically with FR001's original Q_star. It is not silently a new definition of total precision.

For necessity set a=√M, u=a/t, f=1+log(1+u), v=z/a and B=max(1,C0/c). The risk lower gives Q≥a/B and `[1+log(1+vu)]/v≤B`. If v≥1, numerator≥f, giving v≥f/B≥f/B². If v<1, log concavity gives numerator≥vf and hence f≤B; numerator≥1 also gives v≥1/B≥f/B². Thus the product condition follows in all cases, including bounded f and arbitrary fixed target multiplier. The proof makes no unwarranted minimum-attainment assumption.

For sufficiency, f≥1 implies `1+fu≤f(1+u)`, hence W(af,t)≤(f+log f)/(af)≤2/a. Decreasing W gives the full z≥af statement. If z is only ≥B0 af with B0<1, the logarithmic numerator decreases when z decreases, yielding the claimed extra factor 1/B0; if B0≥1, monotonicity suffices. The general fixed-factor target constant in (5.3) is valid.

The dyadic choice Q=2^max(4,ceil(log2√M)) satisfies √M≤Q≤2√M even at M=64 (Q=16=2√M). Integer κ=max(1,ceil(Z_star/Q)) meets the product threshold and its upper bound 1+Z_star/Q. Promise-based budget selection is explicitly distinguished from free runtime logarithms or learning unknown β. The inherited paid β-blind schedule remains a separate alternative. The manuscript does not claim arbitrary tiny target multipliers are feasible.

## Independent diagnostics

Files: `TR001_independent_checks_v1.py` and `TR001_independent_checks_v1.json`. Command:

`python v10_research/two_resource_frontier/TR001_independent_checks_v1.py`

Observed exit 0, PASS. The script uses 65-digit Decimal logarithms and exact integer branch predicates with a stated 1e−58 comparison tolerance. It checked:

- all 13 source hashes;
- 17,948 legal surface parameter points, including β=0, β=1/M, β on either side of and equal to 1/16, β=1, M near powers of two, κ up to 2^40, and grids far beyond M;
- every applicable completion branch, not merely the first match: 5,397 A checks, 8,939 B checks, 10,469 C checks, 5,221 D checks;
- 66,148 threshold implications and 349 actual dyadic/integer sufficient allocations;
- 2,091 independent dimensionless necessity checks and 306 sufficiency checks, with u from 10^−50 through 10^50 and v both below and above one;
- 35 KL/statistical-floor calculations.

These numerical tests corroborate finite algebra and boundary handling; they do not empirically evaluate minimax risks or prove the universal result. No counterexample was found or discarded.

## Remaining limitations

No revision is required for the stated theorem. Constants are extremely loose, architecture-dependent and unsuitable as practical design thresholds. The result is restricted to fixed K,D,r and one global dense positive-weight local-ratio block. Deep/global-feature extensions, growing architecture sharpness, universal Transformer optimality, original exponential-evaluator equivalence, training behavior and fixed-total-precision optimality remain outside this review. All SB001 costs remain paid and are not reduced merely by rewriting κQ. Root may accept or decline the candidate independently.
