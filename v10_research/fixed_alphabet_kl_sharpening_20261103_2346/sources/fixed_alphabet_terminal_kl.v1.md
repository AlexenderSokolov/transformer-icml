# Fixed finite alphabets: full-history terminal KL and a five-block output upgrade

Analytical extension, version 1, 3 November 2026. No numerical experiment, simulation, training, repository mutation or external upload was performed. The proof concerns the actual full-history add-one estimator at the actual terminal context. It is not a minimax-existence substitution. Independent analytical review is a separate obligation, not a claim of formal verification or literature priority.

## 1. Quantifiers, notation and result

Fix a publicly known integer alphabet size A>=2. Observe X_1,...,X_{n+2} from an arbitrary homogeneous second-order source on [A], with n>=1 observed transitions. Its A^2 transition rows and its initial pair distribution are arbitrary and unknown. Zero probabilities, deterministic rows, reducibility and periodicity are allowed. Put N=n+2, L=N+A, Y_i=(X_{i+1},X_{i+2}) for 0<=i<=n, and

    J_s = sum_{i=0}^{n-1} 1{Y_i=s},
    C_{s,b} = sum_{i=0}^{n-1} 1{Y_i=s, X_{i+3}=b},
    J=J_{Y_n},  theta_b=theta_{Y_n}(b),
    B_b=(C_{Y_n,b}+1)/(J+A),                 b in [A].

All logarithms are natural, and KL is forward D(P||Q)=sum_b P_b log(P_b/Q_b), with 0 log 0=0. TV is half the L1 distance. Define

    t=t_{A,n}=max{A, log[2 A^3 n(n+1)^2]},
    c=c_{A,n}=A^4/(n+1)                    for arbitrary initial pairs,
    c=c_{A,n}=A^2/(n+1)                    for stationary initial pairs,
    a=a_{A,n}=min{32 A t^2, 48 A t(1+log t)},
    U=U_{A,n}=c a[1+log(n+A)] + log(n+A)/(n+1)^2,
    V=V_{A,n}=min{log(n+A), U}.

Then the actual full-history add-one estimator satisfies

    E D(theta||B) <= V.                                      (1)

For each fixed A this is O_A(log^2(n+2) loglog(n+3)/(n+1)), uniformly over the stated arbitrary-initial class. The stationary subclass has the improved A^2 occupation factor. Constants are intentionally loose; this is not an optimal A-dependence or logarithmic rate.

For each fixed A, one fixed finite parameter set, independent of n and of the source, implements a five-block exact-real causal attention/ReLU model whose final output is an ordinary A-way vocabulary softmax R. With the architecture detailed below,

    TV(R,B) <= min{1,(44A+1)/L},
    R_b >= 1/[1+(A-1)L] >= 1/(AL)  for every b,
    E D(theta||R) <= 2V + 2A(44A+1)^2/L.                    (2)

Also E D(theta||R)<=log[1+(A-1)L], so this deterministic cap can be taken in (2). The first two claims hold pathwise for every word, including n=0/N=2. For n=0, the statistical logarithmic expression in (1) is replaced by the elementary bound log A.

The five blocks have H=A^2+1 allocated heads each, head dimension d_h=4 ceil(sqrt(A+10))^2, and model width d_model=H d_h=O(A^3). Active head counts are (2,0,A^2+1,A,A). Inputs explicitly include the source-independent positional features (1,i,i^2,log i), A BOS tokens and symbol onehots. The model has no LayerNorm and uses ordinary full causal masks. There is no externally supplied count division, log of a probability, position-times-state feature, or horizon-dependent learned coefficient.

## 2. Terminal occupation, including arbitrary starts

The pair process Y is a homogeneous chain on D=A^2 states. The following argument holds for any D-state homogeneous chain. Fix an integer w>=1 and write

    b_m(s)=P_s(number of earlier visits to Y_m before time m < w),
    B_m=max_s b_m(s).

For m>=ell, earlier full-history visits dominate the visits within the last ell departures. Conditioning on Y_{m-ell} and using homogeneity gives B_m<=B_ell. This is a monotonicity statement for the worst initial state, not for each fixed b_m(s).

On any deterministic state sequence, at most the first w occurrences of each state have fewer than w earlier visits. Therefore sum_{m=0}^n b_m(s)<=Dw for each initial state s. Since max_s b_m(s)<=sum_s b_m(s),

    (n+1)B_n <= sum_{m=0}^n B_m
              <= sum_s sum_{m=0}^n b_m(s) <= D^2 w.

Taking a mixture over the initial state proves

    P(J<w) <= min{1, D^2 w/(n+1)}.                          (3)

For stationary initialization the improved D factor follows from a finite-window charging argument. Fix s. Among r=n,...,2n, at most w times have Y_r=s and fewer than w copies of s in the preceding n positions: if w+1 times were marked, the last has all w earlier marked times in its preceding n-window. Each marked event has, by stationarity, the probability of {Y_n=s,J_s<w}. Thus that probability is at most w/(n+1); sum over s. This argument only extends the chain for analysis, not the observations given to the estimator.

In either case, with c defined above, summation by parts gives

    E[1/(J+A)]
      = 1/(n+A) + sum_{k=0}^{n-1} P(J<=k)/[(k+A)(k+A+1)]
      <= 1/(n+A) + c sum_{k=0}^{n-1}(k+1)/[(k+A)(k+A+1)]
      <= c[1+log(n+A)].                                     (4)

Here c>=1/(n+A), A>=2, and the summand is at most 1/(k+A). In particular zero visits are included. This reproduces the general occupation interface of the binary v2 proof, with D=A^2; no mixing or stationary minimum is introduced.

## 3. Categorical row stacks and simultaneous concentration

For each context s in [A]^2, generate n independent categorical variables with probabilities theta_s, independently across rows and independently of the initial pair. At each departure from s, consume its next unused stack entry as the next symbol. This generates exactly the prescribed source: each path constrains exactly its consumed row prefixes and has the initial-pair probability multiplied by its usual transition product.

Let K_{s,b,j} count symbol b in the first j entries of row s. Pathwise C_{s,b}=K_{s,b,J_s}. There is no claim that a stack stays iid after conditioning on J_s, the terminal row or the observed path. Instead, for every deterministic row/symbol/prefix, Bernstein's inequality for its Bernoulli indicator sum yields

    |K_{s,b,j}-j theta_s(b)|
       <= sqrt(2j theta_s(b) t) + 2t/3                      (5)

outside probability 2e^(-t). The variance is bounded by j theta_s(b). Union over A^2 rows, A symbols and j=1,...,n yields a single event G_t with

    P(G_t^c)<=2 A^3 n e^(-t) <=(n+1)^(-2).                  (6)

Every deterministic-prefix inequality then holds on G_t at the random selected row and random selected count, without conditional independence. Dependence between symbol counts within one categorical stack does not affect the union bound. The j=0 inequality is deterministic.

For completeness the scalar Bernstein bound can be obtained from

    E exp(lambda Z) <= exp[lambda^2 E Z^2/(2(1-lambda/3))],
                      0<=lambda<3,

for a centered |Z|<=1 variable, by expanding the exponential, using |E Z^r|<=E Z^2 and r!>=2*3^(r-2), then 1+x<=exp x. Independence, exponential Markov and optimization give tail exp[-u^2/(2(v+u/3))]; setting u=sqrt(2vt)+2t/3 and applying both signs proves (5). No selected random time appears in this calculation.

## 4. Forward KL at each simultaneous good prefix

Fix any row and deterministic prefix length j>=0, write its true probabilities p_b, counts k_b, and q_b=(k_b+1)/(j+A). On G_t, t>=A>=2 and (5) hold. For each coordinate set z=jp_b, a_b=k_b+1, x_b=(j+A)p_b. The elementary inequality sqrt(2zt)<=z/2+t gives

    z<=2k_b+10t/3,
    (k_b-z)^2<=4zt+8t^2/9<=8k_b t+128t^2/9.

As |A p_b-1|<=A-1<=t,

    (x_b-a_b)^2
      <= 2(k_b-z)^2+2(A-1)^2
      <=16k_b t+31t^2.                                     (7)

The harmless integer constant 31 exceeds 256/9+2. The same calculation covers j=0 directly.

First, KL<=chi-square and (7) imply

    D(p||q)
      <=sum_b (p_b-q_b)^2/q_b
      =sum_b (x_b-a_b)^2/[(j+A)a_b]
      <=32 A t^2/(j+A).                                    (8)

For the sharper bound put h(x,a)=x log(x/a)-x+a. Since h(x,a)<=(x-a)^2/a, if a_b>=t, (7) gives h(x_b,a_b)<=47t. If a_b<t, then

    x_b<=2a_b+10t/3+(A-2)<7t,

and a_b>=1 yields

    h(x_b,a_b)<=x_b log_+ x_b+a_b
                <=7t log(7t)+t
                <=15t+7t log t
                <=48t(1+log t).                            (9)

The large-a case obeys the same final bound. Both vectors x and a have total mass j+A, so the exact identity

    (j+A)D(p||q)=sum_b h(x_b,a_b)

gives

    D(p||q)<=48 A t(1+log t)/(j+A).                         (10)

On every path, including the complement of G_t, q_b>=1/(j+A), hence D(p||q)<=log(j+A)<=log(n+A). Combine (8) and (10), then use (4) without conditioning and (6):

    E D(theta||B)
      <=a E[1/(J+A)] + log(n+A)P(G_t^c)
      <=U.

The deterministic cap proves (1). The A in max{A,...} is important: blindly replacing the binary numerator by A symbols without controlling the smoothing displacement A p_b-1 would not justify the stated constants.

## 5. Retain the archived finite-A first three blocks

Use the prior finite-alphabet construction at commit 0d678eefb558d5108dd5ef893b033c6f58077d81, path fixed_alphabet_causal_extension_20261103_1653/alphabet_extension_candidate_v1.html under v10_research, Git blob 9cc4a7554fdaffc08bd89d894cb887cbfef73307. The original source is available through the immutable public GitHub link in Section 11. The following statements are also specified here so the scope of the retained blocks is explicit.

There are A BOS tokens at positions i=1,...,A with values e_1,...,e_A. Data token k is at position A+k with value x_i=e_{X_k}. Write kappa=sqrt(d_h)=2 ceil(sqrt(A+10)), an integer independent of N. Each score is Q dot K divided by kappa; all unused head coordinates are zero.

Block 1 has two active vector-valued copy heads, h=1,2:

    Q_i=kappa(2i^2-2hi,-i), K_j=(j,j^2), V_j=x_j.

Scores differ from -i(j-i+h)^2 by a query-only constant. At valid data lags their wrong mass is at most 2e^(-i)/(1-e^(-i))<1/4. Apply the componentwise two-hinge map T(a)=2ReLU(a-1/4)-2ReLU(a-3/4), giving exact onehots t_1,t_2 at valid lags and values in [0,1] otherwise. The FFN also writes

    b(i)=ReLU(A+1-i)-ReLU(A-i),
    v(i)=ReLU(i-A-2)-ReLU(i-A-3),
    f(i)=ReLU(2-i).

These exactly flag BOS, valid successor positions i>=A+3, and the first BOS. Block 1 requires at most 4A+5 hidden ReLUs.

Block 2 has zero attention and a 2A^2-unit FFN writing, for each context (r,s),

    g_rs=ReLU(v+t_2[r]+t_1[s]-2),
    q_rs=ReLU(t_1[r]+x_i[s]-1).

At every valid candidate, g is its predecessor-context onehot; at every invalid candidate g=0. At terminal i=L, q is the exact actual pair onehot, including N=2.

Block 3 uses one head for each of A^2 contexts h, with query first coordinate kappa(i-A), key first coordinate g_h+b and value vector x_j. At the terminal the score is N for the A BOS and each matching valid successor, and zero for all other data positions. Therefore

    o_{h,b}=[C_{h,b}+1+e^(-N)D_{h,b}]/[J_h+A+e^(-N)K_h],
    K_h=N-J_h, D_{h,b}>=0, sum_b D_{h,b}=K_h.

This is an exact probability vector. It is a mixture of B_h and a distractor distribution with mass at most Ne^(-N)/A, even at J_h=0. An A^3-unit FFN writes p_b=sum_h ReLU(o_{h,b}+q_h-1); at terminal this selects precisely o_{Y_n}. A uniform zero-score head with value f(j) writes z=1/L. Thus terminal p is an exact simplex and

    TV(p,B)<=Ne^(-N)/A.                                    (11)

The first three blocks are unchanged. Only the prior broad-Gaussian output block is replaced by the two blocks below. The prior construction's specialized finite-bit backend is not automatically inherited by this replacement.

## 6. Block 4: A bounded-error rescaling heads

For each symbol b use one head

    Q_b=kappa(p_b+1/2+z,-z), K_j=(j,j^2), V_j=j.

At terminal, scores differ by a query-only constant from -(j-mu_b)^2/L, with

    mu_b=1/2+L(1/4+p_b/2).

The head output y_b is its discrete-Gaussian mean on 1,...,L. The inherited interior mean bound gives |y_b-mu_b|<10. Here is its analytical justification. For f(x)=(x-mu)e^(-(x-mu)^2/L), total variation on the real line equals 4 sqrt(L/(2e)). Unit-cell quadrature therefore has error at most 2 sqrt(L/(2e)). Both cell-boundary distances from mu to the ends of [1/2,L+1/2] are at least L/4, so the integral has absolute value at most (L/2)e^(-L/16). There are at least floor(sqrt L)>=sqrt L/2 supported integers within distance sqrt L of mu, giving normalizer at least sqrt L/(2e). Consequently

    |y_b-mu_b|<=2sqrt(2e)+e sqrt L e^(-L/16)
                 <=2sqrt(2e)+sqrt(8e)<10.

The last maximum follows analytically at L=8. Here L>=4. A 2A-unit FFN writes

    x_b=ReLU(2y_b-i/2-1)-ReLU(2y_b-3i/2-1).

At terminal this is projection of 2y_b-L/2-1 onto [0,L]. Projection cannot increase the distance to Lp_b, so

    0<=x_b<=L, |x_b-Lp_b|<=20.                             (12)

The x_b need not sum to L. The subsequent normalization proof deliberately does not assume that they do.

## 7. Block 5: A narrow-Gaussian logits and ordinary softmax

For each b use a head

    Q_b=kappa(2x_b,-1), K_j=(j,j^2), V_j=log j.

Its scores differ from -(j-x_b)^2 by a query-only constant. The head output ell_b is the expectation of log J under these weights on 1,...,L. Block 5's FFN is zero. The final fixed linear readout supplies logits ell_1,...,ell_A to ordinary vocabulary softmax:

    G_b=exp(ell_b), S=sum_b G_b, R_b=G_b/S.

For any center 0<=mu<=L, the constant-variance geometric-mean lemma gives

    |exp(E log J)-mu|<=24, 1<=exp(E log J)<=L.              (13)

For completeness, a supported integer lies within distance one of mu, so the weight normalizer is at least e^(-1). The unimodal lattice bound sum_{j in Z}e^(-(j-mu)^2/2)<=1+sqrt(2pi), together with |s|e^(-s^2)<=e^(-s^2/2), implies E|J-mu|<=e(1+sqrt(2pi))<10. Jensen gives exp(E log J)<=mu+10. For mu<=2 this and the lower bound 1 suffice. For mu>2, the negative log deficit on mu/2<=J<mu is at most 20/mu. The remainder is at most

    e e^(-mu^2/4) sum_{1<=j<mu/2}log(mu/j)
      <= e mu e^(-mu^2/4)<=4/mu.

The sum is bounded by its decreasing-function integral from 0 to mu/2, which is less than mu. Hence E log(J/mu)>=-24/mu, giving exp(E log J)>=mu exp(-24/mu)>=mu-24. This proves (13).

Combining (12)-(13), |G_b-Lp_b|<=44 for every b. Normalization is handled without a large-L condition:

    ||R-p||_1
      <= ||G/S-G/L||_1 + ||G/L-p||_1
      = |1-S/L| + sum_b |G_b/L-p_b|
      <= 2 sum_b |G_b/L-p_b| <=88A/L.

Thus TV(R,p)<=44A/L. Also G_b>=1 and each other G_a<=L give the exact support floor

    R_b>=1/[1+(A-1)L].                                     (14)

For N>=2, N^2e^(-N)<=4e^(-2) and Ne^(-N)<=2e^(-2), so

    L Ne^(-N)/A
      = (N^2/A+N)e^(-N)
      <=(4/A+2)e^(-2)<=4/e^2<1.

Together with (11), this proves the pathwise approximation in (2). No complement-coordinate trick specific to binary output is used.

## 8. Multiclass KL transfer

For distributions T,P,Q with P,Q strictly positive, the entropy variational inequality gives

    D(T||Q)<=2D(T||P)+log sum_b P_b^2/Q_b
            <=2D(T||P)+sum_b (P_b-Q_b)^2/Q_b.              (15)

One proof is to use E_T f<=D(T||P)+log E_P exp f with f=log(P/Q), then sum P^2/Q=1+sum(P-Q)^2/Q and log(1+u)<=u. True probabilities T_b may be zero.

Apply this pointwise with P=B,Q=R. Their positivity holds at every history, including zero visits. For a zero-sum vector delta=B-R, its positive and negative parts each sum to TV(B,R), hence sum_b delta_b^2<=2TV(B,R)^2. By (14),

    sum_b (B_b-R_b)^2/R_b
      <=AL sum_b (B_b-R_b)^2
      <=2AL TV(B,R)^2
      <=2A(44A+1)^2/L.                                    (16)

Taking expectation in (15) and using (1) proves (2). An additive probability approximation by itself would not justify this step; the explicit floor (14) is essential. No terminal-state independence or conversion of a TV risk through reverse Pinsker is asserted.

## 9. Explicit A-dependent resource accounting

- One parameter set is fixed across all N and all sources for each preselected A. It may depend on A. A growing alphabet is a family of different architectures and vocabularies, not one fixed-width network.
- There are exactly five residual attention/ReLU blocks with H=A^2+1 allocated heads per block and d_h=4ceil(sqrt(A+10))^2 per head, as in the prior finite-A model. Active heads by block are (2,0,A^2+1,A,A), totaling A^2+2A+3. Their values have dimension at most A<=d_h.
- Reserve disjoint slots for four position features; A token coordinates; 2A raw copies; 2A snapped copies; three flags; A^2 candidate and A^2 query coordinates; A^3 row-head outputs; A selected probabilities; scalar z; A y coordinates; A x coordinates; A final logits. This uses at most A^3+2A^2+9A+8 slots. The original width H d_h already exceeds this because d_h>=4(A+10). No increase to the existing finite-A head dimension or width is necessary.
- Active FFN hidden widths are at most (4A+5,2A^2,A^3,2A,0). A common width max{4A+5,2A^2,A^3,2A} suffices. In particular, saying the maximum is always A^3 would be inaccurate at A=2. The asymptotic FFN width remains O(A^3).
- All masks permit exactly j<=i. Every key/value is from the observed prefix; the terminal symbol is a legal key, not the unobserved next symbol. BOS smoothing and early invalid candidates are explicitly accounted for.
- Dense parameter storage has O(A^6) entries. With the displayed integer kappa and fixed rational coefficients, coefficient descriptions use O(log(A+2)) bits. This statement concerns fixed weights, not exact-real log positions or evaluated softmax values.
- Positions (1,i,i^2,log i) are paid source-independent inputs. Integer position i and its square require O(log L) bits per exact integer, or paid generation; exact log i is a real-number assumption. Intermediate x and y grow as O(L); positional magnitudes reach O(L^2); raw copy scores reach O(L^3), row matching gaps are N, rescaling scores are O_A(L), and narrow-head scores reach O(L^2). Final logit magnitudes are at most log L.
- Straightforward dense causal evaluation has Theta((A^2+2A+3)L^2) active-head query-key visits. Charging head dimensions/vector aggregation and dense projections/FFNs gives a conservative O(A^3 L^2+A^6 L) exact-real arithmetic-operation bound, in addition to positional generation and the chosen cost of exp/log evaluation. Row-streamed activations and dense weights use O(A^3 L+A^6) real slots; materializing every attention matrix adds O(A^2 L^2) slots.
- No finite-bit bound is proved for the new two-block output. The prior four-block specialized backend does not automatically control rescaling error multiplied by L, narrow-Gaussian score error, or final probability support under output rounding. Generic IEEE arithmetic, constant word length, fixed exponent range, training attainability and optimal compute are not certified.

## 10. Prior results, scope and remaining gaps

Han, Jana and Wu, *Optimal prediction of Markov chains with and without spectral gap*, IEEE Transactions on Information Theory 69(6), 2023, pp. 3920-3959, DOI 10.1109/TIT.2023.3239508, treat stationary higher-order same-trajectory prediction. Their fixed-order finite-alphabet minimax theorem includes the A^3 complexity for order two in its stated regime. Their Remark 1 distinguishes full-history add-one from suffix-averaged add-one; their higher-order upper proof uses the stationary redundancy-to-prediction reduction. Therefore those optimal stationary minimax guarantees are not silently assigned to the full-history predictor implemented here, or to arbitrary initialization. Sources: [published article](https://par.nsf.gov/servlets/purl/10539616), [author preprint, Sections 5 and 6](https://arxiv.org/html/2106.13947v2#S5). The locally available published PDF was inspected; a fresh fetch of the published URL failed, while the author preprint was accessible.

For each fixed A, (1)-(2) establish a rigorous estimator-specific O_A(log^2 n loglog n/n) upper and an O_A(1/n) output-approximation penalty. They do not establish the optimal O_A(log n/n) rate for full-history add-one. Uniform O(1/n) over the full stationary second-order class is ruled out already by its binary subfamily, so that is not a target claimed here.

The displayed inequalities are valid for every finite A,n, but the fixed-A asymptotic notation must not be read uniformly over growing A. In the regime A<=O(log(n+2)), the loose arbitrary-start statistical factor is of order A^5 times logarithmic factors divided by n, and the stationary version has A^3 instead. Outside that regime t>=A explicitly records the larger smoothing cost. No optimal alphabet-growth threshold follows.

The prior finite-A construction already supplies A^2 row heads, categorical BOS smoothing, exact terminal selection and A-way broad-Gaussian readout. This note keeps its first three blocks and replaces the readout using the binary narrow-Gaussian rescaling mechanism applied independently to A coordinates, followed by a multiclass normalization and support argument. Conditional n-gram, position-copy and smoothed-attention mechanisms have prior literature, including the sources cited in the archived finite-A note. No novelty, exhaustive prior-art clearance, Transformer-wide lower bound or training claim is made.

## 11. Source bindings

- Public finite-A source: https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/v10_research/fixed_alphabet_causal_extension_20261103_1653/alphabet_extension_candidate_v1.html . Git blob 9cc4a7554fdaffc08bd89d894cb887cbfef73307, fetched read-only through the GitHub connector. The linked public Git blob is the provenance reference; no separate local copy is asserted in this export.
- Predecessor binary statistics, version 2, Sections 3-5.1. The complete categorical argument needed here is reproduced in Sections 2-4 above. The statistical proof above is its categorical extension, not an import of its binary rate as a theorem about A symbols.
- Predecessor narrow-Gaussian clipped-bridge output lemmas, version 2, Sections 5-7, with the corresponding independent version-2 review. The required scalar arguments are reproduced in Sections 6-8 above. Only their scalar rescaling/geometric-mean/transfer machinery is used; their special rare-family statistics are not imported.
- The published HJW PDF was inspected during preparation; its SHA-256 is 375c730cb4c9f6dd2eaa4439e59800764faeddbebee73f220e22d6d2cf3116a3. Relevant published locations include Remark 1, Lemma 6, Section V and the stationarity discussion on p. 3952. This local provenance is a research binding, not a public-download promise.

This artifact preserves the earlier binary and finite-A files. The extension was obtained analytically; no experiment supplies any step of its proof.
