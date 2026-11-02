# SC003 — Fresh independent FULL theorem review

2026-11-02. Reviewer task: `audit_binary_corruption_bound`, directly commissioned by root. **Verdict: PASS; no blocking mathematical, scope, or resource defect found.** Root acceptance remains a separate decision.

Reviewed target: `v10_research/binary_source_corruption/SC003_theorem.md`.

SHA-256: `4235fc6b9de9d04368354d22f15774d66965ca572f21f197e456537e9bcba837`.

This is a fresh same-model independent LLM review of the **whole theorem**, not the author's earlier algebra/orientation subreview, external peer review, or formal verification. I read the complete target, SC001, SC002, BIF001, BAI003 v2, and ORIGINAL R011; inspected their acceptance receipts and the relevant BIF/BAI review context; reconstructed the new argument independently; and wrote and ran new diagnostics. Accepted imports are identified below. I did not change the author manuscript or any frozen manuscript/package. No external action, publication, or novelty check was undertaken.

## 1. Experiment, minimax order, and observable inputs

The experiment is SC002's **full corrupted history** experiment specialized to binary symbols, not SC002's three-symbol lower theorem. The word has M+2 symbols and precisely M departure triples. The offline randomized attack can replace at most k positions among the first M, including adjacent positions, and preserves the last two. The source is homogeneous second order, with arbitrary unknown initial pair law and an existential stationary law satisfying the certificate on all four pair states. The target is the original next-symbol law at the preserved actual terminal pair, not a corrupted law or independently sampled query.

The k-aware estimator is one fixed map for each public M,k and does not read beta, theta, Pi, the initial law, the edit mask, clean counts, or the attack seed. The proof may analyze source-dependent quantities without making them algorithmic inputs. The stationary experiment is a restriction of the arbitrary-start experiment with the same permissible attack and predictor interfaces, so R_stat <= R_all. The lower witnesses are stationary IID sources and remain valid even if the predictor is told beta and k. In particular there is no quantized-bank or retained-representation restriction in either lower.

The nested source/attack suprema do not themselves require one attack across all parameters. The corruption lower supplies the stronger common-kernel property anyway. This is correctly distinguished from claiming that the upper knows or estimates the attack.

## 2. Exact orientations and symbol symmetry

Index states as 00,01,10,11. The public designated successor is the complement of the **first**, not the second, bit. Thus its true probability vector is exactly (a,b,e,t), with successors (1,1,0,0). These are BIF001 §3's true crossing weights b,e, not unit crossing caps. No source-dependent minority test is implicit.

Global symbol complementation sends u to its bitwise complement and sends its designated successor to the complemented designated successor. The row-weight vector transforms as (a,b,e,t) to (t,e,b,a); the designated clean/corrupted counts and masses are unchanged after this relabeling. Therefore the estimator is equivariant. Applying the absorbing-00 result to an absorbing-11 source by this operation does not introduce a law-dependent algorithm branch.

## 3. Pathwise corruption and the new downward envelope

A changed observed symbol belongs to at most three of the M counted triples. The union of affected triples has size at most 3k, even with overlapping/adjacent edits. Replacing one triple label changes a complete histogram by l1 at most two. Hence the full histogram change is at most B=6k. Restriction to the two coordinates of the same selected row gives

    |C'-C| + |(J'-C')-(J-C)| <= B.

The terminal protection is essential here: the clean and corrupted selected row indices really are equal. This is a joint-row bound, not two separate budget assumptions.

For k>=1, let n'=(C'-B)_+, D=J+2, D'=J'+B+2. The joint bound implies |J'-J|<=B and |C'-C|<=B. Consequently D' >= D, n'<=C, and n'>=0. Also C-n'<=2B: if C'>B this follows from C-C'+B<=2B, while if C'<=B then C<=C'+B<=2B. Likewise 0<=D'-D<=2B. Thus the exact identity

    C/D - n'/D' = (C-n')/D + (n'/D')(D'-D)/D

is nonnegative and at most 4B/D, since n'/D'<=1. In particular arbitrary attack-created false exit mass cannot invalidate the lower envelope. This proof does not transfer a quantization purity assertion to a corruption problem.

For J>0, p=C/J satisfies p-C/D=2p/(J+2). Combining this with the preceding bound gives

    0<=p-qhat<=min(p,(4B+2)/(J+2)).

Triangle inequality followed by the 1-Lipschitz property of x -> min(x,c) gives

    |qhat-q| <= |p-q|+min(p,A/(J+2))
               <=2|p-q|+min(q,A/(J+2)), A=24k+2.

At J=0 the clean C=0, the lower envelope forces qhat=0 despite possible corrupted row mass, and min(q,A/2)=q because A>=2. Thus (2.4) holds on every clean/corrupted history and every attack realization. Binary TV is exactly the designated-coordinate absolute error. A true q=0 row has C=0 almost surely under the clean source and therefore qhat=0, without requiring the estimator to know q=0. Non-realizable clean words are not used to make any statistical claim.

At k=0 a different, explicitly specified add-one branch is used. The attack is necessarily identity; no argument improperly sets B=0 in the k>=1 estimator and calls that add-one.

## 4. Original clean comparator and universal occupation

R011 ORIGINAL, not its separate pooled/selected ALG, bounds the original add-one risk. For K=2, all scales a,D,T in its H are at most sqrt(32/(M+1)); hence its upper implies S<=8192 sqrt(32)/sqrt(M+1) for all beta and all starts. This is the same actual-terminal clean target as required here.

On J>0, the distance between p=C/J and clean add-one (C+1)/(J+2) is |2p-1|/(J+2)<=1/(J+2). Taking expectations with the indicator and using nonnegativity of the full add-one loss gives (3.1). It does not condition an empirical row into an IID sample.

I also checked the occupation interface directly. For a d-state chain, let b_m(y)=P_y(J_m<w) and B_m=max_y b_m(y). A terminal suffix has no more prior target visits than the full path, so B_m is nonincreasing. For each realized path, at most dw times can be visits numbered at most w to their respective current states. Therefore sum_{t=0}^m b_t(y)<=dw for each y, and sum_t B_t<=sum_y sum_t b_t(y)<=d^2 w. It follows that B_m<=d^2 w/(m+1). With d=4 this is the stated 16w/(M+1), for arbitrary initial mixtures.

For layer height v>0, a nonempty event J<A/v-2 is represented exactly by integer threshold w=ceil(A/v-2)>=1, and w<=A/v. Integrating min(1,16A/((M+1)v)) proves (3.2). The strict inequality and integer ceiling cause no extra +1 cost, and J=0 is included. As an independent check on the inverse-count constant, use A=1: E[1/(J+2)]<=Psi(16/(M+1))<=sqrt(32/(M+1)). The last scalar bound follows from max_{0<x<=1} sqrt(x)(1+ln(1/x))=2/sqrt(e)<sqrt(2); the x>=1 case is immediate. Thus even the sharper +1 rather than BIF's +2 in the empirical comparator is justified.

## 5. Weighted occupation and exhaustive support partition

The functional V=min(q_{Y_M},A/(J+2)) uses true row probabilities only in the proof. No support test or value of q is computed by the estimator.

**Full support, beta>=M^-2.** BIF001 §3 (3.4) is precisely an all-start weighted occupation result for these q and every A>0, M>=64, beta M^2>=1. I read its full composition: the diagonal-start constants 4+40+100+8192=8336, the first-diagonal-hit suffix reduction, the small-crossing-hazard true-weight bound, and the resulting 4s+16672(A/M)G. Its suffixes have horizon at least ceil(M/2)>=32; the component bounds do not impose beta times squared suffix horizon >=1. Its use here is an import of that occupation lemma, not its architecture-specific minimax theorem or decoder. Since k<=24k+2<=26k for k>=1 and e0=sqrt(beta), monotonicity of the logarithm in A gives (4.2) with 16672*26=433472.

**Positive beta, non-full stationary support.** Pair stationarity gives Pi=(y,x,x,w), ya=xe, wt=xb. If x>0, the all-state two-step inequalities ea>=beta x and bt>=beta x force a,b,e,t>0, then y,w>0. If x=0, stationary mass is confined to diagonals and each positively weighted diagonal is absorbing. Two supported absorbing diagonals contradict positive minorization from either diagonal to the other. Thus exactly a singleton absorbing stationary support remains; no transient initial state is excluded.

For absorbing 00, BAI003 v2 §6 (6.2) is stated for arbitrary other rows, all starts, every A>0 and horizon at least 8. Its weights (0,b,e,t) agree exactly. I read its alternating-renewal proof and original/reflected complete-path domination: the reflected target is not substituted for the actual target. The B contribution is bounded through first entry into absorbing 00 and the universal occupation bound at horizon M+1. The corrected v2 initial-B shift uses M-1 only for M>=9 and handles M=8 separately. SC003's M>=64 lies safely in its domain. With A>=1,

    256A/M+16/(M+2) <= (256*26+16)k/M =6672k/M.

Symbol complementation covers absorbing 11 as in §2 above, including boundary row probabilities. No beta-size condition is needed for this absorbing lemma.

**Weak beta, including zero.** If 0<=beta<M^-2, e0=1/M and no support classification is used. V<=min(1,A/(J+2)), A<=26k, and monotonicity of Psi give Psi(416k/M). For z=M/k>=1, when z<416 the proposed upper 416(1+ln(1+z))/z exceeds one; for z>=416 direct substitution proves the inequality. This establishes (4.4) without division by beta. Equality beta=M^-2 is explicitly in the strong branch; at that equality its two e0 definitions agree.

These cases cover every beta in [0,1] and every stationary support compatible with the certificate. Arbitrary mixtures of deterministic starts are retained throughout.

## 6. Constants, endpoints, and fixed-beta interpretation

Combining the pathwise loss with the comparator and the largest occupation bound costs

    [2*8193*sqrt(32)+4]s +433472 F.

The first coefficient is approximately 92697.2137322, below 2^17=131072; the second is below 2^19=524288. The absorbing coefficient 6672 and weak coefficient 416 are smaller still. Replacing sqrt(M+1) by sqrt(M) only enlarges the upper. Unit TV supplies the cap independently. The clean k=0 branch fits within the same statistical coefficient, with F defined as zero rather than evaluated through a singular formula.

M=64, k=0,1,M and beta=0,M^-2,1 are all covered. At beta=1/M the full-support occupation cutoff is sqrt(beta), as asserted. This is not a global marginal-mixing estimate. For each fixed positive beta, e0>=sqrt(beta), k>=1 implies the bracket is bounded by 1+ln(1+1/sqrt(beta)); this establishes the stated fixed-beta order when combined with the lower floors. It does not establish a uniform moving-beta logarithmic lower.

## 7. Both lower floors, with full observation accounted for

For any p in (0,1), setting all four source rows equal to Bernoulli(p) and starting from its product pair law makes the entire M+2-symbol word IID. On all pair states P^2 has every row equal to Pi. Hence these witnesses lie in every beta class, including beta=1, and their actual terminal target is Bernoulli(p) independent of which pair was observed.

For the clean floor, identity corruption is allowed for every k. At p±=1/2±1/(16sqrt(N)), N=M+2, the stated per-symbol KL bound is conservative and valid; multiplying by N gives <=1/8, so Pinsker yields TV<=1/4. The target separation is 1/(8sqrt(N)). Nearest-target testing and triangle inequality give average loss at least separation*(1-TV)/4=3/(128sqrt(N)), which is >=s/64 for M>=64. Randomized predictors do not evade this testing reduction.

For the corruption floor, the rule rounds the number n of ones in the first M positions down to r=(k+1)floor(n/(k+1)) and chooses r retained ones uniformly. Its edit count is n-r<=k, its definition uses only the input word and public k, and both protected terminal bits remain unchanged. Conditional on n, uniform IID arrangements and uniform retained subsets imply probability 1/binom(M,r) for each output arrangement of weight r. Mixing over n in the same coarse cell preserves that parameter independence. Conditional on p the final pair U is independent of the editable IID block, so the whole corrupted word factors through (r,U), with at most 4(floor(M/(k+1))+1) labels. The protected pair is counted rather than conditioned away.

For a uniform prior of interval length ell, fix all independent decoding randomness to obtain at most D real output points. Whatever the stochastic encoding probabilities are, the event of error <=v requires p to belong to their radius-v union, whose prior mass is at most 2Dv/ell. Integrating the complementary bound to ell/(2D) gives ell/(4D); averaging decoding randomness preserves it. Random output arrangements can be absorbed into this independent decoder randomization precisely because their conditional channel is parameter-independent. This proves a lower for arbitrary full-word decoders, not only count estimators.

Taking ell=1/2 gives 1/[32(floor(M/b)+1)] >= b/[32(M+b)] >= k/(96M), since b=k+1>=k and b<=M+1<=2M. The source supremum dominates the uniform-prior average for this single common attack. Combining this floor with the separate clean witness by their maximum gives max(s,k/M)/96. No sum of unrelated risks is used, and no three-symbol rare-suffix witness or representation lower is transplanted into the binary model.

## 8. Rational implementation and cost interpretation

A sequential implementation can retain the M+2 corrupted bits, copy the final pair, rewind, and scan all M triples. Two selected-row counters suffice. The designated bit comes from a fixed Boolean function of the preserved pair. All counters, B=6k, numerator and denominator have O(log(M+2)) bits: J'<=M and D'<=7M+2. The rational coordinates can be emitted as the shared positive denominator and complementary nonnegative integer numerators, with no division, floating point, logarithm, square root, or reduced-fraction requirement. k=0 uses the corresponding add-one integers.

Reading, retaining, rewinding/copying, counter operations, and public k/output serialization fit O(M log(M+2)) conservative bitwork and O(M+log(M+2)) total live bits. A fixed uniform program with loop counters suffices; it needs no source-dependent table or exponentially large compiled description. These are ordinary sequential full-history bounds, not fixed neural depth, bounded attention, or retained-bank claims. The statement's costs are therefore adequate for its actual algorithm.

## 9. Provenance and independent diagnostics

The four SC001/SC002/BIF001/BAI003 target hashes match their root acceptance receipts. R011 has two file identities: the SC003 author bindings point to a readable intake copy, whereas the original root receipt identifies the original proof. I compared them bytewise: removing the readable copy's two-line editorial preface leaves exactly the accepted original bytes. Thus the imported ORIGINAL theorem is unchanged. Both identities and the original acceptance receipt are included in the review bindings; this is a resolved provenance distinction, not a mathematical defect.

Fresh `SC003_independent_full_checks.py` completed successfully and wrote `SC003_independent_full_checks.json`, target-bound to the SHA-256 above. It records **304,726 checks**: 87,376 exhaustive clean-word/edit-mask pairs for M=1..7 (including adjacent/all-position edits and exact terminal preservation); 87,376 symbol-complement checks; 126,360 exact rational envelope/error checks, including 40,000 larger arbitrary joint-row perturbations; 1,016 clean-branch checks; 284 exact arrangement-erasure cells obtained by enumerating input words and retained subsets rather than only checking a binomial identity; 1,848 scalar/lower-domain checks; 462 clean-floor checks; and four accepted-proof hash checks. The R011 original/readable byte comparison and constant checks also passed. Small horizons in diagnostics test historywise algebra only and do not extend the theorem below M=64.

Diagnostics corroborate only their finite instances. The universal result rests on §§1–8 and the identified accepted analytic interfaces, not the test count or large constants. The review and all new scripts/results, target, imported proof copies, receipts, and author binding file are identified in `SC003_independent_full_review_bindings.json`.

## Final recommendation

Accept this exact target as the stated binary full-history **upper bound plus two lower floors**, subject to root's own full reading and acceptance. Do not relabel it a complete binary minimax frontier in moving-beta regimes, a matching logarithmic lower, a beta-blind-and-k-blind procedure, a global sqrt(beta) mixing theorem, a bounded-architecture result, or an external novelty/formal-verification claim. It remains post-stage7 and outside the frozen manuscript/package.
