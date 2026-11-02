# SM002 — IID lower bound for the complete finite SRC master interface

2026-11-02. **Author candidate; not independently reviewed, not formal validation.** The parent proposed the tube argument; this note supplies a complete finite-interface proof. No accepted source or earlier candidate is changed. There is no external novelty claim.

## Result first

Fix any integers K>=2, M>=1, h>=4 and Q=2^h. Execute exactly the finite SRC statistical master prefix used by accepted NB002, with its public p_word=4h+4ceil(log2(M+K+4))+64, actual rational-log/integer-exponential evaluator, all 9K+1 post-quantization master coordinates, actual endpoint query, and the exact side information declared at that cut. Give the subsequent decoder arbitrary computation, arbitrary real simplex outputs and source-independent randomization. Do not give it a raw-history reread, clean evaluator words, or additional statistical ports.

For every beta in [0,1], the minimax actual-terminal expected-TV risk in this fixed-master experiment satisfies

    R_master(K,M,beta,Q) >= 2^(-226)/Q.                  (SM-L1)

This is an **internal-master information lower bound**, not an output-format obstruction. Real outputs are allowed. The lower is witnessed within IID sources, with stationary initialization, using only two letters; it holds for every K>=2. Source law and target remain homogeneous and unchanged across a trajectory.

Together with the inherited full-history statistical lower,

    R_master >= max{2^(-17) L, 2^(-226)/Q}.              (SM-L2)

The two witnesses need not coincide and their risks are not added. If the separately proved strong-mixing NB002 upper is accepted, then for beta>=1/2 this identifies, at fixed K,

    R_master = Theta_K(max{(M+1)^(-1/2), Q^(-1)}).       (SM-L3)

The upper in this comparison uses the same fixed prefix and the existing NB002 suffix; no new encoder is selected according to beta. The lower allows a larger arbitrary-decoder class. Consequently the half-logarithmic master precision exponent, with no log-log overhead, is both necessary and sufficient in this strong-mixing regime. This is not a joint-K optimality result, and it does not say every architecture or every precision format obeys this lower.

The explicit constant 2^(-226) is deliberately crude. Its size is irrelevant to the asymptotic separation; improving it is not a research objective here.

## 1. Exact experiment and sources

The deterministic source is

    v10_intake/source/sources/euler-stage6/facts/fef8372728290b45.md

especially proof Sections 2, 4 and 8. Its full old suffix requires a larger h, but accepted NB002 proves the legality of the retained statistical prefix for every h>=4 and replaces that suffix. This note concerns only that same prefix. It also follows directly from the formulas below that its finite head divisions are positive at every such h.

At q=N+1, N=M+2, the valid keys are t=3,...,N. There are four statistical heads:

| Head | Finite score at key triple (a,b,c), query s=(u,v) | Values |
|---|---|---|
| P1 | L2 1{a=u}+L2 1{b=v} | (e_c,e_a) |
| P2 | L2 1{a=u}+L3 1{b=v} | (e_c,e_a) |
| T | L2 1{a=v} | (e_b,F_t) |
| 0 | 0 | (e_a,e_b,F_t,z_t) |

Here z_t=1{t=3}, F_t=z_t e_(X_2), and the finite dyadics L2,L3 are generated from the public parameters. Each full score is evaluated separately; in particular the weight at L2+L3 is not a product of rounded weights.

Write R=2^(p_word). For a nonnegative finite score z, the actual evaluator uses

    T_0=R,
    T_j=floor(T_(j-1) (R z)/(j R)), 1<=j<=8p_word,
    W(z)=sum_(j=0)^(8p_word) T_j.

The source's induction gives, exactly,

    1 <= w(z):=W(z)/R <= exp(z) <= 6.                  (1)

The upper follows because z<=ln 6; the lower follows from T_0=R. The uniform score has w(0)=1. All these weights are fixed public rational numbers for a fixed K,M,h, independent of the unknown source parameter. The actual output master is exactly

    H_c=Q^(-1) floor(Q A_c/D),
    A_c=sum_t w(z_t) value_(t,c), D=sum_t w(z_t).      (2)

Using w=W/R in this display merely cancels the same positive integer R from numerator and denominator. It does not substitute ideal exponentials for the finite evaluator. In particular D>=M.

The complete master bank is

    (q1,v1), (q2,v2), (hvec,h0), (alpha,nu,f,rho).

Only this bank and exact query/mode/endpoint/flag bits plus public metadata survive the cut. The source explicitly releases clean numerators, denominators, weights, terms, remainders, historical projections and unused historical outputs before exposing it. These are not decoder inputs in this theorem. All acquisition and historical work remains paid in the realization; releasing access is not a claim that those costs disappear.

In actual-query mode, the exact data-dependent residuals are functions of the actual endpoint, with synthetic token x_q=F_q=z_q=0; the mode and position flags are public. To be conservative, we grant the decoder **both the initial pair and terminal pair** as extra exact side information. On the binary witness these have at most 16 joint values. The granted initial pair is not needed by the nominal cut, but can only strengthen the decoder. The explicitly listed local flags are functions of these boundary symbols and public positions. This does not grant all historical flags or symbols, which the source cut does not expose.

## 2. Binary IID witness and unconditioned frequency concentration

Use alphabet symbols 0 and 1. Let the unknown parameter x range over I=[1/4,3/4], and assign **every source row**, including off-support pair rows, the probability vector

    p_x(1)=x, p_x(0)=1-x, p_x(c)=0 for c>=2.

Initialize the pair from p_x tensor p_x. Then all N observed symbols are IID p_x, and the actual-terminal next-symbol target is p_x for every history and endpoint. Also

    P^2(s,(a,b))=p_x(a)p_x(b)=pi_x(a,b)

for every starting pair s, including off support. Thus every witness is in D2(beta) for every beta in [0,1], with one stationary law pi_x. We will not condition the IID observation law on the terminal pair.

For each binary triple d=(a,b,c), define

    Z_d=(1/M) sum_(t=3)^N 1{(X_(t-2),X_(t-1),X_t)=d},
    tau_d(x)=p_x(a)p_x(b)p_x(c).

The vector Z has eight entries, is nonnegative and sums to one. Its expectation is tau(x). The indicators in one Z_d are independent when their indices differ by at least three. Each variance and absolute covariance is at most 1/4, by Cauchy-Schwarz. There are M diagonal terms and at most 4M ordered off-diagonal terms at distance one or two. Therefore

    Var_x(Z_d) <= 5/(4M).                              (3)

The bound includes M=1 and 2; overcounting nonexistent pairs is harmless. By Chebyshev and the union bound, the event

    G_x={max_d |Z_d-tau_d(x)| <= 10/sqrt(M)}

satisfies, uniformly over x,

    P_x(G_x) >= 9/10,
    ||Z-tau(x)||_1 <= 80/sqrt(M) on G_x.                (4)

Although the notation G_x uses the unknown parameter, this is only an analysis event, never an encoder/decoder input. It may depend on x; the eventual Bayes argument explicitly permits this. The bound controls all four possible endpoint queries simultaneously because the same Z is used for all of them. It does not replace the actual endpoint by an independent query.

## 3. A finite family of deterministic mean curves

Fix one binary query s. For every nonboundary head coordinate, its unrounded finite-evaluator value is a ratio

    F(Z)= [sum_d a_d Z_d]/[sum_d w_d Z_d],
    0<=a_d<=w_d, 1<=w_d<=6.                            (5)

The coefficient a_d is the finite weight times a value bit. This covers q1,v1,q2,v2,hvec,alpha,nu. For the uniform head the denominator is simply one. Let its deterministic comparison coordinate be F(tau(x)). These are means of the underlying empirical frequencies passed through the same finite rational head map, not expectations of the random normalized head output.

For any two probability vectors z,z' on the eight triples, both denominators in (5) are at least one, both ratios lie in [0,1], and

    |F(z)-F(z')|
      <= |sum a_d(z_d-z'_d)|/sum w_d z_d
         + F(z') |sum w_d(z_d-z'_d)|/sum w_d z_d
      <= 12 ||z-z'||_1.                                (6)

The remaining coordinates are boundary flag means. Only the first key can contribute to h0 and f; rho is a single uniform flag mean. Consequently their unrounded magnitudes obey

    0<=h0_c<=6/M, 0<=f_c<=1/M, rho=1/M.                (7)

Assign their comparison coordinates the constant zero. This is a comparison curve only: the actual bank still contains every one of these statistical coordinates, and no coordinate is deleted.

Write H_s(x) for the resulting complete comparison vector. All entries for symbols c>=2 are identically zero in both the actual bank and H_s. Hence only 19 scalar coordinates can vary: nine binary coordinate blocks and rho. By (4), (6), (7), every unrounded finite head value B_s satisfies on G_x

    ||B_s-H_s(x)||_infinity <= 960/sqrt(M),             (8)

simultaneously for all four binary queries. The boundary bound is valid because 6/M<=960/sqrt(M) for every M>=1.

The curve is uniformly Lipschitz. Write r_x=(1-x,x); tau(x)=r_x tensor r_x tensor r_x. Its derivative has l1 norm at most

    ||tau'(x)||_1 <= 3 ||r'_x||_1 ||r_x||_1^2=6.

Using (6), or differentiating the positive-denominator ratio, gives

    ||H_s(x)-H_s(y)||_infinity <=72 |x-y|.             (9)

Boundary comparison coordinates are constant. The finite weights may depend on K,M,h, so the comparison curves may too, but both constants in (8),(9) are uniform in those public parameters. There is no need for a single limiting curve or an ideal-head approximation.

## 4. Only O(Q) complete good messages when Q<=sqrt(M)

Suppose Q<=sqrt(M). Choose a mesh of I with consecutive spacing at most 1/(72Q), including both endpoints. It needs at most

    ceil(36Q)+1 <=38Q

points. Every x is within 1/(72Q) of one mesh point x_j. By (8),(9), on G_x every unrounded active coordinate differs from H_s(x_j) by at most 961/Q. The actual master is its downward Q-grid quantization (2), which changes it by less than 1/Q. Thus its integer numerator m_i satisfies

    |m_i-Q H_(s,i)(x_j)| <=962.                        (10)

An interval of length 1924 contains at most 1925 integers, fewer than 2^11. Therefore, for each fixed s and mesh point, there are at most

    (2^11)^19=2^209

possible complete master vectors satisfying (10). This is a bound on the **joint complete bank**, not on a selected coordinate. All additional-letter coordinates are zero, and all boundary statistical coordinates h0,f,rho have been included among the 19.

Taking the union over four binary queries, at most 38Q mesh points, and at most 16 granted exact boundary-side values gives a set of complete decoder messages of cardinality at most

    4 * 38Q * 16 * 2^209 < 2^221 Q.                    (11)

The factor 16 already contains the terminal pair, so multiplying by the four queries is an intentional safe overcount. Public metadata and fixed mode/flags add no further choices. The message set in (11) is fixed by K,M,h and the known witness family, not by the unknown true x. On G_x the actual complete decoder input belongs to that one common finite set, for every x in I.

It is essential here that Q<=sqrt(M). Without that condition, concentration alone allows a larger tube than one fixed number of Q-grid cells. The complementary range will use a separate statistical lower bound, not an invalid extrapolation of (11).

## 5. Good-event finite-message Bayes lemma

**Lemma.** Let x be uniform on an interval of length ell>0. An arbitrary experiment has, for each x, an event G_x with probability at least 9/10. Suppose that whenever G_x occurs the full decoder message lies in one fixed set of at most R messages. The event need not be observable and may depend on x. Then every decoder with source-independent randomization and real scalar output Z obeys

    E|Z-x| >= ell/(16R).                               (12)

**Proof.** Fix its independent random seed. On the R good messages its scalar outputs comprise at most R real values z_1,...,z_R. Put a=ell/(8R). The union of radius-a intervals around those values intersects the prior interval in length at most 2Ra=ell/4. Thus its prior probability is at most 1/4. Since the unconditional probability of G is at least 9/10,

    P(G and x outside this union) >=9/10-1/4=13/20.

On that event every possible good-message output is at distance at least a from x. Hence

    E|Z-x| >= (13/20)a =13ell/(160R) >=ell/(16R).

The bound is uniform in the fixed seed, so averaging the seed proves the claim. In particular no independence of G from x, no posterior-uniformity claim, and no deterministic parameter-to-message quantization assumption is used. Only the good-message alphabet and its probability matter. ∎

Apply this lemma with ell=1/2, scalar output Z equal to the decoder's probability assigned to symbol 1, and R<=2^221 Q from (11). For every simplex output z,

    TV(z,p_x) >= |z(1)-x|.

The Bayes expected TV is therefore at least

    1/(32 R) >= 2^(-226)/Q.                            (13)

A source supremum is at least this single-prior average. The entire observed history is still stochastic, and the complete master channel can be noisy conditional on x; (12) allows that. The next-symbol target is exactly p_x, not an empirical vector. This proves SM-L1 when Q<=sqrt(M), even after granting the extra exact initial pair.

## 6. The complementary Q>sqrt(M) range: a binary statistical lower

For completeness, this short proof stays inside the same binary IID witness family instead of relying on whether an inherited IID lower used more letters. Put N=M+2 and

    x_+=1/2+1/(16sqrt(N)),
    x_-=1/2-1/(16sqrt(N)),
    d=x_+-x_-=1/(8sqrt(N)).

Both lie in I. The chi-squared divergence of one Bernoulli observation, with the minus law as reference, is

    chi²_1=d²/[x_-(1-x_-)] <=1/(12N),                  (14)

because x_-(1-x_-)>=3/16. Independence gives for all N symbols

    1+chi²_N=(1+chi²_1)^N <=exp(1/12)<=12/11.

The last inequality follows from the exponential series termwise bound exp(t)<=sum_(j>=0)t^j=1/(1-t) for 0<=t<1. By Cauchy-Schwarz applied to the likelihood ratio,

    TV(P_+^N,P_-^N) <=(1/2)sqrt(chi²_N)
                     <=1/(2sqrt(11))<1/4.             (15)

For any full-history scalar estimator z, integrating the pointwise triangle inequality |z-x_+|+|z-x_-|>=d against the minimum of the two densities yields

    (E_+|z-x_+|+E_-|z-x_-|)/2
       >= (d/2)(1-TV(P_+^N,P_-^N))
       >=3/(64sqrt(N)) >=1/(32sqrt(N)).                (16)

The same holds with independent decoder randomness by integrating over the seed. A fixed-master decoder has no more information than the full history and any granted boundary symbols are already functions of it, so (16) applies to this experiment. Since N=M+2<=3M and Q>sqrt(M),

    1/(32sqrt(N)) >=1/(32sqrt(3M)) >1/(64Q).           (17)

This is stronger than SM-L1. It covers every remaining Q, including all small M when the tube regime is empty. No limit argument, approximate query independence or output quantization is involved. Equations (13),(17) prove the lower for every M>=1 and h>=4.

## 7. Statistical comparison, strong mixing, and exact scope

Every fixed-master predictor is a full-history predictor with an additional information restriction. Therefore the inherited R011 lower 2^(-17)L applies to its minimax risk. Combining that lower with SM-L1 by maximum gives SM-L2. This argument is valid whether or not beta is supplied to the decoder; the binary family lies in every class and beta says nothing about x within that family.

For beta>=1/2, R011 gives L=F=max(i,min(1-beta,a)), with

    i=min(1,sqrt(K/(M+1))), a=min(1,sqrt(K^3/(M+1))).

At fixed K, i<=L<=a implies L=Theta_K((M+1)^(-1/2)), uniformly over beta in that interval. The separately authored strong-mixing upper for the *same NB002 finite predictor* is of the form

    risk <=min(1,C_0 L+C_1 K^3/Q).

If independently accepted, it combines with SM-L2 to give SM-L3. The tiny numerical lower constant does not undermine that order statement. At fixed K, a uniform constant-order minimax bound over beta>=1/2 therefore forces Q=Omega_K(sqrt(M)); a half-log public master schedule suffices by the separate upper. The necessity is now a complete-master statement even when the output is permitted to be real, not merely the existing output-grid necessity.

The source initialization in this lower is stationary. The upper allows arbitrary initialization. The lower therefore remains valid if the restricted minimax class additionally requires stationarity, but no claim that its upper is independently optimal in every stationary weak-beta regime is made here.

Contrast with PL001 is conditional on that separate candidate's acceptance: its weak-mixing/logarithmic obstruction uses a different homogeneous family and implies an additional log M factor for the same fixed prefix when arbitrary weak-mixing sources are admitted. SM002 does not contradict it; the IID family proves the smaller 1/Q obstruction and does not cap what more general sources can force.

This is not a lower bound for all bounded-score attention architectures, altered encoders, extra paid ports, data-dependent quantization scales, or arbitrary word formats. It does not imply time/space superiority, training attainability, physical-fault robustness, or joint-K optimality. The lower allows unlimited suffix resources, so its content is entirely the specified prefix's finite information bottleneck.

## 8. Hazards examined and evidence status

- **Incorrect conditioned IID shortcut:** avoided. All concentration is for the unconditional IID history and controls every fixed binary query at once; the actual endpoint is selected afterward pathwise.
- **Ignoring side ports:** avoided. The complete 9K+1 bank is included; binary support makes other-letter entries exactly zero. Endpoint/local bits are retained and an extra initial pair is granted. Clean evaluator words and raw history are not permitted by the actual source cut.
- **Replacing finite weights by ideal exponentials:** avoided. The proof uses actual W(z)/R in [1,6], at all five full scores, throughout the rational maps and their curves.
- **Treating means of ratios as ratios of means:** avoided. H_s is only a deterministic comparison curve, and (6) proves its pathwise approximation on G_x.
- **Assuming the good event has parameter-independent probability or leaves the prior uniform:** avoided. Lemma (12) uses only uniform lower probability and a global good-message alphabet.
- **Multiplying many coordinate alphabet sizes across the entire parameter interval:** avoided. Coordinate products are taken only within a bounded-width tube box; there are O(Q), not O(Q^19), such boxes along the curves.
- **Extending the tube to Q>sqrt(M):** not done. A separate binary statistical lower covers that regime.
- **Overclaiming the result:** constants are crude; SM-L3 depends on the separately reviewed upper; neither component certifies external novelty. A source-hash manifest and finite algebra diagnostics accompany this author candidate, but those are not an independent proof or an emitted-network test.
