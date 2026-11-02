# S013 二步状态律 TV 包络的精确尖锐性

编排说明（非原文）：以下逐字保留原已接纳版本的完整数学论证、必要定义、范围与科学解释，仅省略身份、内部控制和来源元数据。原有数学编号及 Euler clock 名称不变。新增标题与本说明不是原证明。依赖闭包与源哈希见 ../SOURCES.md，精确字节映射见 ../COPY_MAP.json。本次编排不是重新证明或对复制件的新数学审查。



## Allowed assumptions, notation, and cited-result interface

The original experiment has alphabet `{0,...,K-1}`, homogeneous probability rows `theta_ab(c)`, legal transitions `(a,b)->(b,c)`, and arbitrary initial pair law mu. With `Y_j=(X_(j+1),X_(j+2))`, the prediction experiment observes `X_1,...,X_(M+2)` for `M>=1` and targets the row `theta_(Y_M)`. Its risk is `E TV(A(H),theta_(Y_M))`, where `TV(p,r)=(1/2)sum|p-r|`. This is distinct from the state-law quantity `TV(mu P^t,pi)` studied here.

For the generic comparison, `D_K(2,beta)` consists of sources with a stationary probability pi satisfying `P^2(s,z)>=beta pi(z)` for **all** pair states s,z; pi may have zero masses and mu need not be absolutely continuous with respect to pi. Beta is a public lower bound in this generic class, not an oracle disclosing the unknown table or its maximal coefficient. No irreducibility, full support, reversibility, stationary initialization, or positive legal transition is assumed.

Primitive conditions for the fresh construction are `K=2`, `0<beta<1`, and deterministic integer `t>=0`. We define `q=1-beta`, so `0<q<1`. Write `delta_s` for the point mass at pair state s, `Pi` for the matrix whose every row is pi, and `H=(X_1,...,X_(M+2))` for the observed history. The formulas below define, rather than assume, the lawful kernel, stationary witness and invariant. The only accepted mathematical interface used is:

**S011 Lemma 1, All-state contraction (`lem:s011-contract`).** Under the stated generic class, for every deterministic t,

    TV(mu P^t,pi)<=h_t,
    h_t=(1-beta)^floor(t/2)                    if 0<=beta<1;
    h_t=1 for t=0,1, and h_t=0 for t>=2        if beta=1.

The necessary bridge is explicit: for beta<1, `Q=(P^2-beta Pi)/(1-beta)` is stochastic, `pi Q=pi`, and `nu P^2-pi=(1-beta)(nu Q-pi Q)`. The finite triangle inequality shows that any stochastic kernel contracts TV. Iterate `floor(t/2)` two-step blocks and then at most one single step, starting with `TV(mu,pi)<=1`. For beta=1 row sums force `P^2=Pi`. S011's proof, relevant independent-review interface and actual acceptance hashes were checked; no statistical bound from S011 is needed to prove this construction.

Public-facing objects are the constructed `theta^(beta)`, `P`, stationary `pi`, initial `delta_10`, time t, and the exact TV statement. The scalar q, induction index m, stationary coordinates, matrix Pi, residual Q, and logarithms/thresholds in the negations are proof-local expressions derived from these parameters. The family-specific predictor defined below is public-facing only as a non-lower-bound witness. There are no conditional invariant assumptions or unspecified constants.

## Local lemma map

| Unit | Named result / stable label | Role |
|---|---|---|
| unit_001 | Proposition 1, Legal absorbing pair shift (`prop:s013-kernel`) | Full matrix, stationary uniqueness, exact coefficient |
| unit_002 | Invariant 2, Alternating surviving mass (`inv:s013-survival`) | Exact state law at every time and parity |
| unit_003 | Proposition 3, Exact uniform-envelope sharpness (`prop:s013-sharp`) | Match the accepted generic bound |
| unit_004 | Proposition 4, Faster-exponent negations (`prop:s013-negation`) | Explicit finite-C counterparameters |
| unit_005 | Proposition 5, Endpoint laws (`prop:s013-endpoints`) | Beta-zero nonuniqueness and beta-one reset, no zero-to-zero power |
| unit_006 | Proposition 6, Known-family zero prediction loss (`prop:s013-zero-risk`) | Preserve the mixing/statistical distinction |

## Local derivation

### unit_001: Proposition 1 — Legal absorbing pair shift (`prop:s013-kernel`)

**Statement.** For `K=2` and `0<beta<1`, define the successor probabilities of symbol 1 by

    theta_00(1)=1,  theta_01(1)=beta,  theta_10(1)=1,  theta_11(1)=1,
    theta_ab(0)=1-theta_ab(1).

These rows define a legal homogeneous pair-shift matrix P with unique stationary probability `pi=delta_11`. Its largest all-state two-step minorization coefficient relative to pi, and over all stationary witnesses, is exactly beta.

**Proof.** Every displayed row has two nonnegative entries summing to one. In state order `(00,01,10,11)`, the complete matrices are

             [ 0  1  0  0 ]                  [ 0  0  q  beta ]
    P =      [ 0  0  q beta],       P^2 =     [ 0  q  0  beta ] .
             [ 0  1  0  0 ]                  [ 0  0  q  beta ]
             [ 0  0  0  1 ]                  [ 0  0  0   1   ]

All nonzero transitions have exactly the required shift form: `00->01`, `01->10` or `11`, `10->01`, and `11->11`. Thus no arbitrary four-state matrix has been substituted for a legal source. Homogeneity follows because the same fixed beta is used at every step. The second matrix follows by multiplying the first; for example a two-step departure from 01 returns to 01 with probability q or is absorbed at 11 with probability beta.

State 11 is absorbing, so `pi P=pi`. If nu is any stationary probability, its coordinates obey

    nu(00)=0,
    nu(01)=nu(00)+nu(10)=nu(10),
    nu(10)=q nu(01).

Consequently `beta nu(01)=0`, and beta>0 gives `nu(01)=nu(10)=0`; normalization gives `nu(11)=1`. This proves uniqueness without a support or irreducibility assumption.

For every target z other than 11, `pi(z)=0`, so the minorization inequality there is automatic. At target 11 the four two-step probabilities are `(beta,beta,beta,1)`. Hence `P^2(s,z)>=beta pi(z)` for every s,z, and any coefficient alpha satisfying the same all-state inequality must have `alpha<=P^2(10,11)=beta`. Since the stationary law is unique, choosing a different stationary witness cannot increase the coefficient. ∎

### unit_002: Invariant 2 — Alternating surviving mass (`inv:s013-survival`)

**Statement.** Under Proposition 1, let the initial pair law be `mu=delta_10`. For every integer `m>=0`, the following named state-law invariant holds:

    delta_10 P^(2m)   = q^m delta_10 + (1-q^m)delta_11,              (I-even)
    delta_10 P^(2m+1) = q^m delta_01 + (1-q^m)delta_11.              (I-odd)

**Proof.** At m=0, the even identity is the initial law itself. One application of P sends 10 deterministically to 01 and fixes 11; hence `(I-even)` at any m implies `(I-odd)` at that same m. One further application sends the mass at 01 to `q delta_10+beta delta_11` and fixes 11. Thus

    [q^m delta_01+(1-q^m)delta_11]P
       =q^(m+1)delta_10+[q^m beta+1-q^m]delta_11
       =q^(m+1)delta_10+(1-q^(m+1))delta_11,

which is `(I-even)` at m+1. This establishes both identities by induction for all m, including the first two actual transitions. No spectral approximation or limiting argument is used. ∎

### unit_003: Proposition 3 — Exact uniform-envelope sharpness (`prop:s013-sharp`)

**Statement.** Under Proposition 1 and Invariant 2, for every deterministic integer `t>=0`,

    TV(delta_10 P^t,delta_11)=q^floor(t/2).                         (E)

In particular the generic envelope h_t from the accepted S011 contraction interface cannot be lowered at any fixed interior beta and integer t, uniformly over legal binary pair shifts and initial laws.

**Proof.** For any probability nu on the four states,

    TV(nu,delta_11)
      =(1/2)[sum_(z!=11)nu(z)+|nu(11)-1|]=1-nu(11).

Invariant 2 gives nonabsorbed mass exactly q^m for both t=2m and t=2m+1, proving (E). At t=0 and t=1 it is exactly 1, not q. At t=2 and t=3 it is q. These finite cases agree with the same all-time formula.

Proposition 1 places this source and initial law in `D_2(2,beta)` with exactly the advertised coefficient. S011 supplies the uniform upper h_t on that class; (E) attains it with the same source and initialization at **all** times. Therefore the supremum of `TV(mu P^t,pi)` over that binary class is exactly h_t. The same witness also attains the stronger S011 intermediate bound `h_t TV(mu,pi)`, since its initial TV is 1. This statement is solely about state-law distance, not any estimator's prediction loss. ∎

### unit_004: Proposition 4 — Faster-exponent negations (`prop:s013-negation`)

**Statement.** The following two statements are false:

1. At a fixed `beta in (0,1)`, there exists a finite nonnegative C such that all legal binary sources in `D_2(2,beta)`, all initial laws and all integers t satisfy `TV(mu P^t,pi)<=C(1-beta)^t`. In fact the single source of Proposition 1 violates this for every such C.
2. For a fixed `c>1/2`, there exists a finite nonnegative C such that all `beta in (0,1)`, all legal binary sources in `D_2(2,beta)`, all initial laws and all integers t satisfy `TV(mu P^t,pi)<=C exp(-c beta t)`.

Constants may depend on the fixed alphabet size K=2 but not on t or the source; in statement 2 they must not depend on beta. No optimality assertion for `c<=1/2` is made.

**Proof of 1.** Fix beta and write `lambda=-log(1-beta)>0`. At t=2m, Proposition 3 makes the ratio of the actual distance to `(1-beta)^t` equal to

    q^m/q^(2m)=exp(m lambda).

If C=0, t=0 already contradicts the proposed bound. For C>0 choose the explicit integer

    m=1+floor(max{0,log C}/lambda),       t=2m.

Then `m lambda>log C`, so the proposed inequality fails. C may even depend on this fixed beta without saving the bound uniformly in t.

**Proof of 2.** Again C=0 fails at t=0, so take C>0 and fix c>1/2. Choose

    beta=(2c-1)/(4c),                 0<beta<1/2.

The elementary integral estimate gives

    lambda=-log(1-beta)=integral_0^beta dx/(1-x)
           <=beta/(1-beta),
    1/(1-beta)=4c/(2c+1)<2c.

The last strict inequality is equivalent to c>1/2. Thus the explicit number `d=2c beta-lambda` is strictly positive. Choose

    m=1+floor(max{0,log C}/d),         t=2m.

On the source of Proposition 1 at this beta and initial pair 10, the ratio of actual distance to `exp(-c beta t)` is

    q^m exp(2c beta m)=exp(m d)>C.

This is the required finite counterexample for every pair (c,C). The construction also works for any positive beta with `beta<1-1/(2c)`, by the same integral estimate, so the obstruction is present at arbitrarily small positive beta rather than only at the displayed one. The proof negates a TV contraction improvement; it gives no bound below on the original statistical risk. ∎

### unit_005: Proposition 5 — Endpoint laws (`prop:s013-endpoints`)

**Statement.** The same row definitions at beta=0 and beta=1 have the following endpoint properties; no expression involving `0^0` is needed.

- At beta=0, stationary probabilities are exactly

      a delta_11+(1-a)(delta_01+delta_10)/2,       0<=a<=1.

  Thus stationarity is not unique. The maximal all-state two-step coefficient is zero even when one optimizes over stationary witnesses. From initial 10, distance to the stationary witness delta_11 is one at every time.
- At beta=1, delta_11 is the unique stationary law, the maximal coefficient is one, and from initial 10 the successive laws are delta_10 at t=0, delta_01 at t=1, and delta_11 at every t>=2.

**Proof.** At beta=0 the dynamics are `00->01`, the deterministic two-cycle `01<->10`, and absorbing 11. The stationary coordinate equations in Proposition 1 now read `nu(00)=0` and `nu(01)=nu(10)`, exactly giving the displayed family. If a<1, that witness has positive mass on 01, whereas `P^2(11,01)=0`, so no positive all-state coefficient works. If a=1, use `P^2(10,11)=0`. Coefficient zero always works. Starting at 10, the law alternates between delta_10 and delta_01 and never assigns mass to 11; the TV identity in Proposition 3 gives distance one.

At beta=1 every successor symbol is 1, so every pair becomes 11 after at most two steps. The stationary-coordinate equations force delta_11 and the two-step matrix has every row delta_11; its maximal coefficient is one. The stated initial-10 laws follow from the first two transitions. Hence both endpoints agree exactly with the endpoint-safe h_t of S011: h_t=1 for all t at beta=0, and h_0=h_1=1 with h_t=0 for t>=2 at beta=1. The nonuniqueness at zero is not silently extended to positive beta, or vice versa. ∎

### unit_006: Proposition 6 — Known-family zero prediction loss (`prop:s013-zero-risk`)

**Statement.** In the original full-history actual-terminal prediction experiment, suppose the source is known to be the family in Proposition 1 (or Proposition 5), with public beta. For any `M>=1` and any initial pair law mu, an admissible deterministic predictor has exactly zero pathwise TV loss and hence zero expected loss.

**Proof.** Given the observed full history H, its actual terminal pair `Y_M=(X_(M+1),X_(M+2))` is observed. Define the probability output

    A_beta(H)(1)=beta if Y_M=01, and 1 otherwise;
    A_beta(H)(0)=1-A_beta(H)(1).

These are nonnegative entries summing to one for every possible history. The algorithm reads only the observed endpoint, the public beta and the public family description. It does not read mu, pi, hidden parameters, a future symbol, or an independent query. By the explicit row definitions, `A_beta(H)=theta^(beta)_(Y_M)` for every history, so its TV loss is identically zero. This remains true for arbitrary initial laws, all M>=1, and both endpoints.

For clarity, in the full class `D_2(2,beta)` beta remains only a lower bound and does **not** reveal its unknown source. The same displayed mapping is still an admissible common algorithm on that larger class, but its risk is asserted to vanish only on this explicitly specified family. Thus the example cannot by itself lower-bound the minimax prediction risk on the full class. Unknown-family or unknown-beta estimation would be a different question, not a conclusion of this calculation. ∎

## Target-step assembly and implications

Proposition 1 proves legality, stationary uniqueness and exact maximal coefficient; Invariant 2 proves the all-time state-law recurrence; Proposition 3 combines that recurrence with the accepted S011 contraction interface to establish exact equality with the generic envelope. Proposition 4 supplies fully quantified faster-exponent negations. Proposition 5 preserves both endpoint baselines without a zero-to-zero power or false uniqueness at beta zero. Proposition 6 proves directly why the mixing obstruction must not be relabeled a statistical minimax lower.

Accordingly, the existing statistical certificate gap cannot be closed merely by replacing S011's generic two-step TV contraction with a uniformly faster one of the prohibited forms. Exact attainment actually precludes any pointwise smaller uniform state-law envelope on this whole legal binary class. It does **not** preclude improving an estimator-specific transfer, using source structure, deriving sharper prediction risk without a generic mixing bound, or closing the full joint-rate problem by another valid argument. The accepted S011 weaker copy-family obstruction is not changed or withdrawn.

## Explicit rate audit

- Exposed variables: beta and deterministic integer time t; binary K=2 is fixed. M>=1 appears only in the zero-prediction-loss comparison.
- Norm/mode: exact deterministic TV between state probability laws, normalized by one half; this is not expected terminal-row prediction TV. The separate predictor statement is zero pathwise and therefore zero in expectation.
- Horizon: every integer t>=0, not a stopping time. Both parities and t=0,1 are derived explicitly. No limit/exchange of expectation/supremum is needed.
- Constants: exact TV equality has coefficient one and no hidden constant. In the first negation beta is fixed and any finite C fails. In the second c>1/2 and finite C are fixed first; beta and t are explicitly chosen afterwards. Constants may depend on fixed K=2, never on the varying beta/source/t in the second statement.
- Auxiliary choices: lambda, d and integer m are the displayed proof-local expressions; positivity and finiteness are proved before division. C=0 is handled separately.
- Baseline: beta-zero h_t=1 and beta-one reset after two steps are retained exactly. No optimality claim is made for exponential constants c<=1/2.
- No stationary-support, irreducibility, recurrent-start, or unknown-maximal-coefficient oracle is added. No statistical lower bound, full joint-rate closure, neural implementation, general-q, hardware or priority claim is exported.


An inline, producer-owned exact-Fraction check independently multiplied the five matrices for beta in `{0,1/7,1/2,6/7,1}`, checked their stationary point mass and minimal two-step 11 probability, and checked 500 state-law TV cases (four initial point masses, t=0,...,24, all five betas). All passed. These are finite sanity checks, not the proof for all real beta and all t, and not an independent mathematical review.
