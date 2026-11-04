# Sharp stationary terminal KL rates and network output corollaries

Composition and comparison note, 4 November 2026 (UTC). The new statistical proof has two passing independent exact-file analytical audits. The output results below substitute that bound into separately reviewed pathwise construction and arithmetic guarantees. The substantive conclusions remain conditional on independent external review. This is not formal verification, a software execution certificate, or a literature-priority claim.

## 1. Statistical theorem and indexing

Let A>=2, n>=1, and L=n+2+A. Observe X_1,...,X_{n+2} from a homogeneous second-order source with a stationary initial pair distribution. Its transition rows may contain zeros; the pair chain may be reducible or periodic. Set

    Y_i=(X_{i+1},X_{i+2}),                    0<=i<=n,
    J_s=sum_{i=0}^{n-1}1{Y_i=s},
    C_{s,b}=sum_{i=0}^{n-1}1{Y_i=s,X_{i+3}=b},
    B_s(b)=(C_{s,b}+1)/(J_s+A),
    W(A,n)=min{log(n+A),
                14000 A^3/(n+1) [1+log_+((n+1)/A^3)]}.

Here log_+(x)=max{log x,0}, and other logarithms are natural. The new theorem gives

    E D_KL(p_{Y_n}||B_{Y_n})<=W(A,n).                    (1)

This is the actual terminal pair of the observed word. There is no independent test context, conditional-binomial assumption, or averaging over suffix estimators. Full-history add-one itself is the predictor in (1).

The exact theorem source is `stationary_addone_sharp_log.candidate.v1.md`, SHA-256

    90e949efc52cd8f3d57108ca334f9083a9858950183dd8e6f60d6664d92c6195.

Two exact-source analytical audits passed:

- `stationary_addone_sharp_log.independent_review.v1.md`, SHA-256 `02ef46cd71c27d218f72942e80484f36fc23253e16779ae49cb989d670335d23`.
- `stationary_addone_sharp_log.redteam_review.v1.md`, SHA-256 `05935d27057e2038dbb2033b97da78e845a7f13c966235bcbedd8cfc78d63df6`.

Their existence does not replace external review or establish novelty. The original candidate header is preserved rather than silently changing its reviewed bytes.

## 2. Pathwise KL transfer

For probability vectors P,B,Q with B and Q strictly positive, Jensen's inequality gives

    D(P||Q)-2D(P||B)
      =sum_b P_b log[B_b^2/(P_b Q_b)]
      <=log(sum_b B_b^2/Q_b)
      =log[1+sum_b (B_b-Q_b)^2/Q_b]
      <=sum_b (B_b-Q_b)^2/Q_b.                          (2)

Zero P_b terms are omitted. If Q_b>=q_min, then the last expression is at most q_min^{-1} sum_b(B_b-Q_b)^2. Since B-Q has zero sum, its positive and negative parts both have mass TV(B,Q), so

    sum_b(B_b-Q_b)^2<=2 TV(B,Q)^2.                       (3)

The support floor is essential. TV closeness by itself does not imply a finite forward-KL transfer.

## 3. Exact-real five-block network

Let R be the ordinary A-way vocabulary softmax output of the unchanged five-block causal attention/ReLU construction embedded in this package. For each fixed A, its finite parameters are fixed independently of n and the unknown source. Retain all its assumptions: the explicit positional features (1,i,i^2,log i), A smoothing BOS tokens, full causal attention support, no LayerNorm, and the stated architecture and gates. There is no claim of a trained network, fixed finite word width, or removal of those positional features.

The inherited all-word bounds are

    TV(R,B)<=min{1,(44A+1)/L},
    R_b>=1/[1+(A-1)L]>=1/(AL).

Equations (1)-(3) therefore imply

    E D_KL(p_{Y_n}||R)
      <=min{log[1+(A-1)L],
             2W(A,n)+2A(44A+1)^2/L}.                   (4)

The network is unchanged. Only its statistical input bound has improved.

The five blocks retain H_heads=A^2+1 allocated heads per block, d_h=4 ceil(sqrt(A+10))^2, width d_model=H_heads d_h=O(A^3), and active head counts (2,0,A^2+1,A,A). A changing alphabet changes this architecture and its vocabulary. The growing-A formulas concern this explicit family, not one network with an unbounded vocabulary.

## 4. Specified integer and dyadic evaluation

Let Q be the output of the embedded specialized integer/dyadic evaluator, with

    s=ceil(log_2(AL)),    b=32s,    H=2^b,    F=H^2.

The algorithm uses exact integer positions and squares, constructed log positions, exact dyadic gates, max-shifted exponential approximation, and mass-preserving normalization. Its inherited pathwise guarantees are

    Q is a nonnegative exact H-grid simplex,
    TV(Q,B)<=min{1,(46A+2)/L},
    Q_b>=1/(4AL).

Consequently (1)-(3) give

    E D_KL(p_{Y_n}||Q)
      <=min{log(4AL),
             2W(A,n)+8A(46A+2)^2/L}.                   (5)

This is a theorem about that algorithm and its exact rounding rules. Additional rounding, generic IEEE floating point, a GPU kernel, automatic mixed precision, or an unspecified softmax backend is not certified by (5).

### Fractional bits and signed range

The value b counts fractional bits, not the complete signed machine-word width. The evaluator also represents signed raw scores, rowwise maxima before max shifting, integer positions and squares, exact accumulation, and wider temporary products.

- Raw copy-score magnitudes are O(L^3); narrow-head scores are O(L^2).
- The broad-head O(L) statement applies at the terminal position only. Earlier selected probability coordinates can be as large as A^2, and earlier broad scores may have a larger polynomial magnitude. They still require only O(log A+log L) magnitude bits.
- Signed differences, linear accumulations, and row sums receive their corresponding O(log A+log L) magnitude and guard allowance.
- Since F=H^2, repeated-squaring products on the F grid may need approximately 4b bits before exact division. Other products receive the constant-factor wider temporaries specified by the inherited evaluator.

Overall working integer lengths are O(b+log A+log L)=O(log(AL)), including those wider temporaries. This does not mean b total signed bits or a fixed exponent range. The length-dependent precision schedule is a paid evaluation resource, not a length-dependent learned coefficient.

The inherited conservative schoolbook cost and row-streamed storage are

    O(((A^2+2A+3)L^2+L)b^3
       +(A^3 L^2+A^6 L)b^2) bit operations,

    O(A^3 L b+b^2+A^6 log(A+2)) bits of storage.

These are analytical resource bounds, not timings or a claim that the algorithm was executed.

## 5. Zero observed transitions

For n=0, use L=A+2 and the uniform add-one row. Its KL is at most log A. Do not evaluate W(A,n) through the n>=1 theorem. The all-word transfer guarantees instead yield

    E D_KL(p_{Y_0}||R)
      <=min{log[1+(A-1)L],
             2log A+2A(44A+1)^2/L},

    E D_KL(p_{Y_0}||Q)
      <=min{log(4AL),
             2log A+8A(46A+2)^2/L}.

The inherited evaluator handles this shortest word without introducing a nonexistent data transition.

## 6. Fixed and growing alphabet comparisons

Both output penalties in (4)-(5) are O(A^3/L) with absolute constants, and L>=n+1. Therefore B, R, and the specified Q all have stationary worst-case upper bounds

    O(A^3/(n+1) [1+log_+((n+1)/A^3)]).                  (6)

In particular, A^3/n -> 0 is sufficient for uniform consistency along growing-alphabet sequences. This is stronger than the earlier sufficient condition A^3 log n/n -> 0. No necessity statement is needed here.

Han, Jana and Wu (HJW), published Theorem 22, use N observed symbols and state, for each order r>=2, a minimax rate

    Theta_r( A^{r+1}/N * log[N/A^{r+1}] ),
    2<=A<=N^{1/(r+1)}/C_r.

For second order, N=n+2 and r=2. The unspecified absolute constant C_2 can harmlessly be enlarged to at least 2. Then N/A^3>=8, so 1+log_+((n+1)/A^3) is an absolute constant multiple of log(N/A^3), and 1/(n+1)<=2/N. Thus (1), (4), and (5) match HJW's minimax order throughout this growing-alphabet domain:

    Theta( A^3/(n+2) * log[(n+2)/A^3] ).                (7)

The lower bound applies to each predictor because HJW's infimum covers every measurable probability-vector prediction based on the observed history. It is a worst-case bound over stationary sources, not a pointwise lower bound at every source. For every fixed A>=2 this gives Theta_A(log n/n). HJW's Theorem 24 explicitly covers binary second-order sources.

The inherited arbitrary-initial-pair theorem remains separate, with upper bound O(A^5 log(n+2)/(n+1)). Stationarity is indispensable to the new proof as given; the A^3 sharpened expression is not claimed for arbitrary starts.

## 7. Ordinary first-order implication and the 2023 open question

The statistical proof uses D context states and A output symbols only through the final sum over targets and symbols. It gives

    14000 DA/(n+1) [1+log_+((n+1)/(DA))]                 (8)

whenever the single-row group tilts used in that proof are legal kernels in the model. They are legal for an arbitrary ordinary k-state Markov chain: a row has k possible next states, and scaling one transition probability and its complement preserves the kernel's support.

For an ordinary stationary k-state chain observed as Z_1,...,Z_N, put n=N-1, D=k, and A=k. Its usual full-history add-one predictor uses

    N_i=sum_{t=1}^{N-1}1{Z_t=i},
    N_{ij}=sum_{t=1}^{N-1}1{Z_t=i,Z_{t+1}=j},
    B_i(j)=(N_{ij}+1)/(N_i+k),

and predicts at the actual terminal state Z_N. For N>=2, (8) gives

    E D_KL(P(.|Z_N)||B_{Z_N})
      <=min{log(N-1+k),
             14000 k^2/N [1+log_+(N/k^2)]}.             (9)

HJW's Theorem 1 gives minimax order

    Theta( k^2/N * log[N/k^2] ),
    3<=k<=sqrt(N)/C,

for an absolute constant C. After enlarging C to at least 2, (9) matches that rate throughout the stated domain. No network architecture claim for first-order chains is added here; (9) is a statistical add-one corollary.

HJW's 2023 Remark 1 asks whether the usual full-history add-one estimator, rather than the suffix-averaged estimator used there, achieves that rate. Conditional on independent external review of the present proof, (9) is a potential answer to that stated 2023 question for k>=3. Current literature priority is not established, and these internal analytical audits are not external peer review. No claim is made that the question remains open today or that this proof is the first answer.

Binary first-order chains are different: HJW recall the minimax rate Theta(log log N/N), whereas (9) only gives O(log N/N) for k=2. This work does not attain the binary first-order minimax rate. The binary second-order Theta(log N/N) statement is a distinct result and does not conflict with it.

## 8. Source bindings and inherited scope

The new theorem and two mathematical audits are identified in Section 1. The following frozen materials are embedded in the HTML package in full:

- `sources/fixed_alphabet_terminal_kl.v1.md`: complete inherited exact-real five-block construction and pathwise transfer prerequisites. Its older statistical rate is historical and is replaced only through the explicit interface (1)-(4).
- `sources/precision_budget_constructive_candidate.v1.md`, SHA-256 `e555323ee18b39b0003863e9d41084d6f2222a575c340b0a9bb8c87213d01a16`: complete integer/dyadic evaluator, support floor, precision schedule, and bit bounds.
- `reviews/exact_real_analytical_review.v1.md`, `reviews/precision_analytical_review.v1.md`, and `reviews/precision_adversarial_review.v1.md`: independent reviews of those inherited prerequisites, including signed range and guard space.
- `sources/prior_stationary_output_corollaries.v1.md` and `reviews/prior_stationary_output_corollaries.independent_review.v1.md`: prior reviewed composition interface, retained as historical source text with its older logarithm.
- `sources/primary_source_matching_lower_audit.v1.md`: primary-publication model, terminal loss, higher-order lower theorem, and N=n+2 indexing audit. Its older upper-bound limitations refer to the prior candidate, not to (1).

Exact hashes for every embedded file and original source paths are recorded in the package ledger. The original frozen documents keep their prior labels and limitations; the leading theorem and this composition identify the new stationary refinement. A final-file review verifies this composition and packaging, not every inherited lemma afresh.

Primary source: Yanjun Han, Soham Jana and Yihong Wu, "Optimal prediction of Markov chains with and without spectral gap," IEEE Transactions on Information Theory 69(6), 2023, pp. 3920-3959. DOI: https://doi.org/10.1109/TIT.2023.3239508 . Author preprint: https://arxiv.org/abs/2106.13947v2 . Primary HTML: https://arxiv.org/html/2106.13947v2 . The published PDF was inspected for Theorems 1, 22, 24 and Remark 1; its SHA-256 is `375c730cb4c9f6dd2eaa4439e59800764faeddbebee73f220e22d6d2cf3116a3`.
