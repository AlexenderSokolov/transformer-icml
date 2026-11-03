# ACG001 independent full source-bound review

2026-11-03. Disposition: **PASS for the stated approximate-statistics interface**, subject to root acceptance and the explicitly accepted stochastic dependencies. No correction required. This is independent LLM mathematical review, not formal verification, external peer review, an architecture construction, or novelty certification. No external writes and no candidate edits.

## Reviewed source and acceptance chain

Read the entire actual ACG001 CANDIDATE.md, SHA256 66ca3f2c092eeceb78cdafab97854580df329b28dd5b4d3bb34c28bb5a44d4ed, and the complete recovered finite manuscript sections/proofs_positive.tex (including the ancillary source-probability proofs). Read the complete original finite manuscript acceptance receipt, O2T001 candidate and root acceptance, author dependency bindings, root independent review and PMC interface addendum/bindings. Source bindings and precise checked receipt entries are in bindings.json. The source positive proof SHA256 is a629caebe01e614a71738f2036bd9016708f35871a15b6902dd98be967f69e88 and matches both its manuscript acceptance and O2T001 dependency binding. Historical pending headings do not change those acceptance receipts.

The imported statements are exactly Lemma occupation with d=4 and integer w>=1, Lemma empirical for M>=64, Lemma imbalance for the first floor(M/2) departures, and equation p-half-inverse inside Proposition finite-upper. They use the actual terminal pair, not an independent or stationary query. All permit arbitrary initial laws; imbalance requires the all-state positive certificate, including unsupported rows. These four stochastic statements are imported accepted dependencies, not claimed newly established by finite checks. O2T001 itself is critical-certificate-only, but the original accepted positive proof explicitly supplies the beta-dependent imbalance inequality; ACG001 correctly imports that source directly for its general-beta display rather than extending O2T001's constant-rate claim.

## Independent analytic verification

### Experiment and clipping

There are M departures from a word of length M+2. D counts exactly indices 0,...,floor(M/2)-1, not an observed suffix or the terminal pair. The two protected final symbols select exactly the same row before and after editing. For u=(a,b), d=1-a; assigning qhat to d gives binary unsquared TV |qhat-theta_u(d)| for either a. On rejection the other symbol has probability one, not necessarily symbol zero. This preserves O2T001's next-symbol target and does not establish a next-pair decoder.

Projection of tilde J onto [0,M] cannot increase its distance from J'. For C', the moving-upper-endpoint issue needs proof and is correctly handled: the upper output is <=max(tilde C,0)<=C'+e. At the lower end, a negative tilde C implies C'<=e; an untruncated nonnegative tilde C is >=C'-e; and clipping at bar J gives bar J>=J'-e>=C'-e. Thus |bar C-C'|<=e, including bar J=0. The same proof applies to D'. No count-consistency or integrality of the estimates is assumed. Each edit affects at most three triples; summing changes gives the safe per-coordinate 6k bound, also for a fixed first-half index restriction. Triangle inequality gives Delta=6k+e for all three clipped coordinates. Adjacent edits do not invalidate this union bound.

### Real-valued gate perturbation

Write G={bar J>0,512 bar D>=bar J}, H={1024D>=J}, B={J>0,256D<J}. Clipping keeps each used ratio in [0,1]. On G with integer J>0, if J>=2Delta>0, bar J>=J/2 and

    |bar C/bar J-C/J| <= (|bar C-C|+(C/J)|J-bar J|)/bar J <=4Delta/J <=8Delta/(J+1).

If 0<J<2Delta, then 8Delta/(J+1)>4J/(J+1)>=2, so the unit ratio-difference bound is sufficient. At Delta=0 both ratios coincide. This proves the displayed comparator on G intersect H without any lower bound such as Delta>=1.

For acceptance outside H, (J-Delta)/512<=bar D<=D+Delta<J/1024+Delta implies J<1026Delta. At J=0, H always holds, so this false-status case is absent. For rejection outside B with J>0, bar J=0 implies J<=Delta. Otherwise 512bar D<bar J, and J/256-Delta<=bar D<(J+Delta)/512 gives J<513Delta. If Delta=0, both erroneous-status events with J>0 are impossible. Gate equality is acceptance, making the rejection inequality strict as required.

For any real x>=0 and integer J, J<x implies J<ceil(x), including when x is an integer; max(1,ceil(x)) additionally covers J=0. Thus w1=max(1,ceil(1026Delta)) and w2=max(1,ceil(513Delta)) are valid INTEGER arguments of the occupation lemma. Since max(1,ceil(x))<=x+1, w1+w2<=1539Delta+2 even at Delta=0. In the separate bar J=0 case, J>0 forces Delta>0 and J<=Delta<513Delta, hence the second tail also covers it.

The cases now exhaust all outcomes: positive clean J and accepted/H uses the empirical plus reciprocal terms; accepted/not-H uses the first tail; rejected/B has loss q; rejected/not-B and positive J uses the second tail; J=0 is covered by both tails. This proves (5) for all admissible real coordinates and every q in [0,1]. Extra nonnegative terms do no harm. Predictor coins and adversarial randomization do not require a probabilistic independence step in this pathwise proof.

### Averaging, constants, and legal probability output

Averaging only the clean reference terms invokes the four exact accepted interfaces. Their clean law is unaffected by introducing a legal edit kernel or independent predictor coins. The perturbation contribution is

    [8*130944+16*(1026+513)]Delta/M =1072176Delta/M.

The remaining tails cost <=32/(M+1), and 512/sqrt(M+1)+32/(M+1)<=65536/sqrt(M) for M>=64. The imbalance contribution remains 65536/(M sqrt(beta)). Hence (1) follows; beta=1/M combines the first two terms into 131072/sqrt(M), and 6*1072176=6433056 gives (2). A further legal probability within xi of qhat increases TV by at most xi by triangle inequality. The cap at one requires the final output to be a probability, as stipulated. No maximum over hidden states replaces the actual-terminal expectation.

### Quantization and costs

Nearest rounding on {0,2^-h,...,1} has error at most 2^(-h-1), including ties and endpoints. Multiplying by known M yields e<=M2^(-h-1), and the coefficient becomes 536088*2^-h. Since h>=ceil(log2(M)/2) implies 2^-h<=M^-1/2, and xi<=M^-1/2, the result is a constant multiple of max(M^-1/2,k/M) for the same decoder at every unknown k. This is a sufficient precision, not a lower bound or an optimal constant.

The grid has 2^h+1 values, so a straightforward unsigned numerator representation uses h+1 bits per coordinate, including h=0 and value 1. Twelve coordinates therefore use at most 12(h+1) bits plus the protected two bits, conditional on M being known. No streaming-update claim follows: independently rounding the final exact statistics is not equivalent to repeated rounding during accumulation. Candidate explicitly excludes acquisition, address/prefix selection, accumulators, weights, readout, training, resident raw input and other architectural costs. The bank has a paid first-half statistic. No count-only, neural superiority, channel-payload, total-precision, or minimum-bank-size conclusion follows.

## Exact finite diagnostics

review_independent/check.py independently implements rational projection and gate comparisons using fractions.Fraction. It checks all small admissible integer triples J,C,D through J=6 with coordinate perturbations, including negative raw estimates and a moving clipping endpoint; additional large J values straddle 256,512,513,1024,1026 and their neighbors. It explicitly forces exact gate equality and either side with fractional D, uses Delta=0 and tiny fractions (including 1/4096, 1/1026, 1/513), verifies strict false-status inclusions and integer ceilings, checks both output orientations, nearest-grid errors, bit width, and all one-symbol protected edits of small binary words. The rational q grid includes 0,1,1/3,1/2, the empirical value and the predicted value. The completed run passed: 18,900 clipping cases; 61,380 pathwise cases; 273,501 loss checks; 135 J=0 cases; 8,187 Delta=0 cases; 36,996 fractional-Delta cases; 2,511 gate equalities; 3,520 ceiling cases; 76,626 quantization cases; and 14,344 protected word/edit pairs. Exact run status appears in checks.json.

These diagnostics validate implementation and boundary examples only; they do not substitute for the universal real-valued proof above or for the imported stochastic results. Small-word enumeration below M=64 checks pathwise counting identities, not the theorem's stochastic domain. The final bindings include candidate, reviewed dependencies, checker, results and this complete review; the root author separately supplied SOURCE_BINDINGS.json, which is also read and bound here.

## Scope decision

Acceptable as a local mathematical prerequisite for a separately paid finite-precision implementation. No new statistical principle, unrestricted no-mixing order-two theorem, general-order extension, architecture construction, learning guarantee, necessary precision claim, or end-to-end memory theorem. No blocking defect or candidate change requested.
