# IP002 — A stationary finite-domain lower for the complete finite SRC master

2026-11-02. **New second-stage author candidate, pending independent review.** IP001 and all earlier accepted files remain unchanged. The root proposed the stationary initialization and finite-domain cutoff; this note tests and proves that extension. It is excluded from the first frozen delivery bundle. No external novelty, original-emitter execution, or formal-validation claim is made.

## 0. Theorem and scope

Let `R_master,stat(K,M,beta,Q)` denote the minimax actual-terminal expected-TV risk in the following experiment. A homogeneous second-order source belongs to D2(beta): its legal pair kernel P has a stationary pair law Pi satisfying

    P^2(s,r)>=beta Pi(r) for EVERY pair s,r.

The initial pair is distributed according to that same Pi. The source table and Pi are unknown. The observed history has M+2 symbols. It is processed by **exactly the actual complete finite SRC statistical master prefix** retained by accepted NB002, in actual-query mode. The decoder sees all `9K+1` downward-Q-grid masters, every original exact endpoint/query/mode/flag side field, and public metadata; it has no raw-history reread or clean evaluator/statistical side port. Arbitrary computation, source-independent randomness, and arbitrary **real** simplex outputs are allowed. Here `Q=2^h`, `h>=4`, and the actual finite evaluator uses

    p_word=4h+4 ceil(log2(M+K+4))+64.

For every integer K>=3, integer M>=64, real beta in [0,1/16], and legal dyadic Q with `16<=Q<=M/4`, put

    b=max(beta,1/M).

Then

    R_master,stat(K,M,beta,Q)
      >= (2^-331/Q) ln(1+(1/8) min{Q/(Mb), M/Q}).     (IP2-S)

This is a **stationary-initialized, internal complete-master information lower**, not an output-format lower. It also lower-bounds the corresponding arbitrary-initialization experiment, since the stationary class is a subclass. The lower remains valid if the decoder knows beta, b, and the witness-family form and receives extra exact initial/terminal pairs plus the selected-event label and suffix length.

Accepted SM002 separately supplies, in this same original stationary experiment and for every legal Q,

    R_master,stat(K,M,beta,Q)>=2^-226/Q.              (IP2-IID)

Two consequences, at fixed K>=3, are:

1. On `M=t^4`, `beta=t^-3`, attaining risk `O_K(t^-2)` still requires `Q=Omega_K(t^2 ln t)`, **even with stationary initialization**. Here M beta=t tends to infinity. NB002 supplies the matching sufficient precision threshold order.
2. At beta=0, attaining `O_K(M^-1/2)` risk at stationarity also requires `Q=Omega_K(sqrt(M) ln M)`, with matching NB002 sufficiency. This consequence needs only the same three-symbol witness; it is not a separate alphabet-optimization result, and K=2 remains outside this argument.

These are precision-threshold and frontier constraints, **not a full intermediate-beta minimax risk formula**. We do not identify the sharp stationary rate uniformly in K and beta, nor claim that the displayed lower matches an upper for every Q. The constants are intentionally conservative.

## 1. Actual finite bank and exact side contract

For final position `q=M+3`, the keys are positions `r=3,...,M+2`. With fixed query `(u,v)` and key triple `(a,c,d)`, the heads are:

| Head | Actual finite score | Local bit values | Blocks |
|---|---|---|---|
| P1 | L2 1{a=u}+L2 1{c=v} | (e_d,e_a) | q1,v1 |
| P2 | L2 1{a=u}+L3 1{c=v} | (e_d,e_a) | q2,v2 |
| T | L2 1{a=v} | (e_c,F_r) | hvec,h0 |
| 0 | 0 | (e_a,e_c,F_r,z_r) | alpha,nu,f,rho |

Here `z_r=1{r=3}` and `F_r=z_r e_(X_2)`. The source entry probability below is denoted alpha_entry, to distinguish it from the statistical master block alpha.

Let R=2^p_word. The finite rational-log construction produces downward constants `0<=L2<=ln2`, `0<=L3<=ln3`. At each whole score z the actual recurrence is

    T_0=R,
    T_k=floor(T_(k-1)(Rz)/(kR)), k=1,...,8p_word,
    W(z)=sum_(k=0)^(8p_word) T_k.

The terms are nonnegative and no larger than the corresponding exponential-series terms times R. Thus the actual normalized rational weights satisfy

    1<=w(z):=W(z)/R<=exp(z)<=6,  w(0)=1.              (1.1)

All five whole scores are evaluated separately; rounded exponential weights are never multiplied to replace the whole-score evaluator. Every scalar master is exactly

    floor(QB)/Q,
    B=[sum_r w(z_r)V_r]/[sum_r w(z_r)],               (1.2)

where V_r is the corresponding local bit. Denominators are at least M. Cancelling the integer R in this expression does not substitute an ideal real computation.

All nine K-vector blocks and rho are retained. Exact side inputs are the actual endpoint copies, actual query one-hots and their derived selectors, fixed actual-query mode, any fixed external-query slot, synthetic zero token/flags, declared local initial-flag bits and copies, and public positions/types/masks/constants. Clean head numerators, denominators, weights, terms, remainders, historical projections, unused historical outputs and the raw history have no decoder read port after this cut. Historical work and storage are still paid; the information restriction does not remove their costs.

The legal prefix domain h>=4 is the accepted NB002 extension, not a retroactive extension of the old removed SRC smoothing suffix. This proof does not change the encoder or its side contract.

## 2. Stationary three-symbol source family

Use distinct symbols W,C0,C1, and let the sole unknown parameter p range over `I=[1/4,3/4]`, with p_0=1-p and p_1=p. Set

    alpha_entry=1/(2M),  eta=b-alpha_entry.

Since `1/M<=b<=1/16` and M>=64, all these quantities are legal and `0<eta<=1/16`. Define a first-order symbol kernel T by

    T(W,W)=1-alpha_entry,
    T(W,Ci)=alpha_entry p_i,
    T(Ci,W)=eta,
    T(Ci,Cj)=(1-eta)p_j.

Let

    pi(W)=eta/b=1-alpha_entry/b,
    pi(Ci)=alpha_entry p_i/b,
    pi(other symbols)=0.                             (2.1)

Every unused-symbol row is defined to equal pi; all other unlisted entries are zero. Row sums and pi's total mass equal one. Incoming W mass under pi is

    (eta/b)(1-alpha_entry)+(alpha_entry/b)eta=eta/b,

and incoming Cj mass is

    (eta/b)alpha_entry p_j+(alpha_entry/b)(1-eta)p_j
      =alpha_entry p_j/b.

Hence pi T=pi. From every symbol x to every symbol y,

    T(x,y)>=b pi(y).                                 (2.2)

The W-to-active and active-to-W inequalities are equalities. The other two supported inequalities reduce to `1>=b`; unused rows satisfy pi>=b pi, and unsupported target columns require only zero. This includes unused starting symbols.

Embed the source by setting `theta_(a,c)(d)=T(c,d)` for every pair. Define

    Pi(u,v)=pi(u)T(u,v).                              (2.3)

Summing incoming pair probabilities and using pi T=pi proves Pi P=Pi. For **every** initial and target pair,

    P^2((a,c),(u,v))=T(c,u)T(u,v)
      >=b pi(u)T(u,v)=b Pi(u,v)>=beta Pi(u,v).         (2.4)

Thus the whole homogeneous family is in D2(beta), including at beta=0. The certificate b may exceed the requested beta, which is allowed by the class definition.

Now initialize **at Pi itself**, rather than at a point mass. This is a genuinely stationary pair process. Pi depends on p and is hidden, as an unknown stationary source permits. Crucially,

    Pi(W,W)=(1-alpha_entry/b)(1-alpha_entry)>=1/4,    (2.5)

and this probability is independent of p: `alpha_entry/b<=1/2`, and `1-alpha_entry>=1/2`. No entire stationary law is supplied to the decoder, and no claim of a parameter-independent initial law is made.

## 3. Stationary path events preserve ONE prior

Define

    A=min{1/(4b), M^2/(4Q^2)},  J=floor(A).           (3.1)

Because b<=1/16 and Q<=M/4, both arguments in A are at least four. Also b>=1/M implies A<=M/4. Therefore

    J>=4,  J>=A/2,  J<=M/4,
    bJ<=1/4,  Q sqrt(J)/M<=1/2.                     (3.2)

For j=2,...,J let E_j be the complete observed-word event

    X_1,...,X_(M+2)=W^(M+2-j),C_(B1),...,C_(Bj).

The E_j are disjoint. They require the initial pair WW, one entry into the active class, no earlier entry and no later exit. The stationary probability of a particular active word is exactly

    Pi(W,W) alpha_entry (1-alpha_entry)^(M-j)
       (1-eta)^(j-1) product_(l=1)^j p_(B_l).         (3.3)

Summing the coin product shows that

    e_j:=P_p(E_j)=Pi(W,W) alpha_entry
                    (1-alpha_entry)^(M-j)(1-eta)^(j-1)
                                                               (3.4)

is p-independent. Conditional on E_j, and **before any endpoint conditioning**, the j active coins are IID with probabilities (1-p,p). In particular, dependence of the full initial Pi on p introduces no hidden likelihood tilt on this selected event: the relevant initial factor Pi(W,W) is constant in p.

Bernoulli's inequality gives

    (1-alpha_entry)^(M-j)>=(1-alpha_entry)^M>=1/2,
    (1-eta)^(j-1)>=1-eta(j-1)>=1-bJ>=3/4.

Together with (2.5),

    e_j>=3/(64M)>=1/(32M).                           (3.5)

Use the **single prior** p uniform on I for all j. Equation (3.4) ensures that this same prior remains uniform conditional on each E_j. We never select a different source for each suffix length.

Every selected word has `M-j` WWW triples, two boundary triples WWC_(B1) and WC_(B1)C_(B2), and `j-2` active triples. Since j<=M/4, its first three symbols are W; the flagged first key is WWW. Initial pair and initial-flag value are fixed. The exact terminal pair ranges over four active choices.

At any of these actual endpoints, the **true** next-symbol distribution is

    eta delta_W+(1-eta)[(1-p)delta_C0+p delta_C1].     (3.6)

Past survival of the active class does not set its next exit probability eta to zero.

For a lower we may additionally grant exact initial and terminal pairs and the event oracle J*=j on E_j and bottom outside their union. This is a well-defined history function. On a fixed E_j, it adds only the four possible terminal-pair labels beyond fixed/public information. Every original exact side field in §1 is determined by these boundary symbols and public inputs. Strengthening the decoder in this way does not delete or obscure any original port.

## 4. Conditional triple concentration and finite comparison curves

Fix j and condition only on E_j. Put n=j-2. For each of the eight active triples d let N_d be its count among the n wholly active triples, and let tau_d(p) be the product of its three coin probabilities. If n>=1,

    E_p N_d=n tau_d(p),  Var_p(N_d)<=5n/4.            (4.1)

Indeed, indicators at separation at least three use disjoint IID coins; there are at most n diagonal terms and 4n ordered overlapping pairs, each variance or absolute covariance at most 1/4. Consequently the event

    G_(p,j)={max_d |N_d-n tau_d(p)|<=10 sqrt(n)}

has conditional probability at least 9/10 by Chebyshev and the eight-term union bound. If n=0, define G_(p,j) as the whole conditional experiment. There is no zero-denominator exception at j=2.

Let z be the empirical distribution of all M triples and define the deterministic probability vector

    zbar_j(p)=(1-(j-2)/M)delta_WWW+((j-2)/M)tau(p).   (4.2)

This comparison replaces the two random boundary triples by WWW. Its boundary l1 discrepancy is at most 4/M. On G_(p,j), therefore,

    ||z-zbar_j(p)||_1
      <=[4+80 sqrt(j-2)]/M<=84 sqrt(j)/M.             (4.3)

The curve in (4.2) is not asserted to be the exact expectation of z; the boundary difference is paid explicitly. Nor is a ratio of expectations asserted to be an expected ratio.

For each fixed active query s, any unrounded nonboundary head coordinate has the exact finite-weight form

    F_s(z)=[sum_d a_(s,d)z_d]/[sum_d w_(s,d)z_d],
    0<=a_(s,d)<=w_(s,d),  1<=w_(s,d)<=6.             (4.4)

The triples d here range over the 27 possibilities on W,C0,C1, and all weights are the actual public finite weights of §1. For probability vectors z,z', subtracting the two ratios gives

    |F_s(z)-F_s(z')|<=12||z-z'||_1.                  (4.5)

Both denominators are at least one; the numerator difference contributes at most `6||z-z'||_1`, and the denominator difference multiplied by a ratio in [0,1] contributes at most the same amount.

Define the full comparison bank H_(s,j)(p) by applying (4.4) to zbar_j(p) in q1,v1,q2,v2,hvec,alpha,nu; set its h0,f,rho coordinates to zero. The actual boundary coordinates are **not removed**. Their unrounded values satisfy

    0<=h0_c<=6/M, 0<=f_c<=1/M, rho=1/M.              (4.6)

Thus on G_(p,j), simultaneously for all four active fixed queries,

    ||B_s-H_(s,j)(p)||_infinity<=1008 sqrt(j)/M.      (4.7)

For `r_p=(1-p,p)`, the l1 norm of the derivative of `tau=r_p tensor r_p tensor r_p` is at most six. Equations (4.2),(4.5) give

    ||H_(s,j)(p)-H_(s,j)(p')||_infinity
      <=72(j/M)|p-p'|.                              (4.8)

At j=2 the curve is constant, so this loose bound still holds. The actual query is selected from the observed endpoint only **after** these simultaneous fixed-query statements. No IID claim conditional on that endpoint is used.

Every coordinate for an unused symbol is exactly zero. Accordingly all `9K+1` masters are retained, but at most `9*3+1=28` support coordinates can vary. This count includes h0,f,rho. It is independent of K because no unused symbol is present on the selected words.

## 5. Complete good-message alphabet

For each s,j, mesh I with gaps at most `M/(72Qj)` and both endpoints. At most

    ceil(36Qj/M)+1<=38(1+Qj/M)                       (5.1)

mesh points are needed. Every parameter lies within one gap of a mesh point. By (3.2),(4.7),(4.8), on G_(p,j) each unrounded active coordinate differs from the corresponding mesh curve coordinate by at most `1009/Q`; this deliberately uses the weaker tube inequality `Q sqrt(j)/M<=1`. Actual downward master quantization adds less than 1/Q. Thus each integer master numerator m_i lies within 1010 of its scaled mesh coordinate.

An interval of length 2020 contains at most 2021 integers, fewer than 2^11. A fixed box therefore has at most `2^(11*28)=2^308` complete banks. Taking the union over four fixed queries, the meshes, and four exact terminal-pair side values yields at most

    4*4*38*2^308(1+Qj/M)
       <=2^318(1+Qj/M)=:R_j                         (5.2)

complete decoder messages. Counting the query again after counting the terminal pair is a harmless overcount. The initial pair is WW, j is fixed in this conditional experiment, all other exact side fields are determined, unused coordinates are zero, and public metadata contributes no variable label.

For fixed public K,M,beta,Q and j, the union set is independent of the true p. The good event may depend on p, but on it the **whole** decoder input belongs to this same fixed set. Coordinate products are taken only inside each bounded-width box; only O(1+Qj/M) boxes are traversed. There is no unjustified claim that all empirical triples reduce to one exact scalar statistic.

## 6. Bayes lower for the correctly scaled target

The needed finite-message lemma is elementary. If p is uniform on an interval of length ell, a parameter-dependent good event has probability at least 9/10 for every p, and its complete messages belong to one fixed set of at most R labels, then any independently randomized real scalar decoder obeys

    E|Z-p|>=ell/(16R).                               (6.1)

To prove this, fix its independent seed. It has at most R output values on the good labels. Their radius `ell/(8R)` neighborhoods cover at most one quarter of the prior interval. With probability at least `9/10-1/4=13/20`, the good event occurs and p lies outside that union. Its error is then at least `ell/(8R)`, proving (6.1); average over the seed. Neither observability nor parameter-independence of the good event is needed. No claim of a uniform posterior after selecting the good event is made.

Apply the lemma conditional on E_j, with ell=1/2 and the common prior in §3. For a simplex output v set `Z=v(C1)/(1-eta)`. By the actual target (3.6),

    TV(v,theta_(Y_M))
      >=|v(C1)-(1-eta)p|=(1-eta)|Z-p|.               (6.2)

Since `1-eta>=1/2`, (5.2),(6.1) show

    E_prior[loss | E_j]>=1/(64R_j)
       >=2^-324/(1+Qj/M).                           (6.3)

The endpoint is part of the message labels, not an event conditioned on before concentration or the prior. The real scalar output need not lie in the prior interval. The decoder may use different outputs for every granted j and every endpoint. All these possibilities are already included in the bound.

## 7. Harmonic averaging proves the finite-domain theorem

For a fixed decoder, nonnegative loss, disjointness of E_j, their p-independent probabilities, and (3.5),(6.3) imply

    E_prior loss >=(2^-329/M) sum_(j=2)^J 1/(1+Qj/M).
                                                               (7.1)

This averages the same parameter prior across all j **before** taking a source supremum.

Let u=Q/M<=1/4. For j=k+2,

    1+u(k+2)<=(1+2u)(1+uk),  1/(1+2u)>=1/2.

The decreasing-function integral, followed by J-1>=J/2 and `(1+x/2)^2>=1+x`, gives

    sum_(j=2)^J 1/(1+uj)
      >=[1/(2u)]ln(1+u(J-1))
      >=[1/(4u)]ln(1+uJ).                           (7.2)

By J>=A/2 in (3.2),

    QJ/M >=(1/8) min{Q/(Mb),M/Q}.                   (7.3)

Combine (7.1)–(7.3) to obtain exactly IP2-S. Every witness source and its stationary initialization are legal by §2. The source supremum dominates this single-prior average; taking the decoder infimum preserves the bound. The proof even allowed the extra event/boundary oracle, so it also applies to the original interface.

## 8. Concrete precision consequences, not a full phase diagram

The accepted SM002 lower uses binary IID sources with stationary initialization and verifies their all-state minorization for every beta. It therefore supplies IP2-IID directly in the original stationary master experiment. We take the maximum of that separately witnessed lower and IP2-S where applicable; their risks are not added as though witnessed by a single source. No claim that SM002 survives an arbitrary new oracle is needed: both conclusions concern the original interface, while the oracle was only a proof-strengthening device for IP2-S.

### 8.1 The earlier vanishing-beta ray, now at stationarity

Fix K>=3 and take M=t^4, beta=t^-3 for sufficiently large integer t. Then b=beta. As checked directly from R011's exact scales, for `t>=max(4,K^2)`:

    L=a=sqrt(K^3/(t^4+1))=Theta_K(t^-2).

For completeness, all its scales are uncapped; `g=Ka`, `hstar=sqrt(K)a`, `a<1/2<1-beta`, so F=a. Also `D/a<=K e^-t<=1` and `T/a<=sqrt(K)e^(-t/2)<=1`. Thus max(F,D,T)=a. R011's full-class beta-blind upper applies in particular to the stationary subclass.

If stationary master risk is at most C_K t^-2, IP2-IID first forces `Q>=c_0 t^2`, where c_0=2^-226/C_K>0. If Q>t^(5/2), its magnitude already exceeds `t^2 ln t`. Otherwise Q<=t^(5/2)<=M/4 for sufficiently large t, so the finite-domain theorem applies. In this case

    min{Q/(Mb),M/Q}=min{Q/t,t^4/Q}
       >=min{c_0 t,t^(3/2)}>=c_0 t

for sufficiently large t. Hence the logarithm in IP2-S is at least `(1/2)ln t` eventually, and

    Q>= [2^-332/C_K] t^2 ln t.                      (8.1)

This proves the stationary precision necessity. Accepted NB002 provides a legal beta-blind decoder with `Q=Theta_K(t^2 log t)` and risk O_K(t^-2), so the precision-threshold order matches for this same fixed prefix.

The stationary full-history minimax benchmark is also Theta_K(t^-2): the upper just noted holds, while the stationary binary IID two-point full-history lower proved in SM002 §6 is at least `1/(32sqrt(M+2))`. Thus the stated target order is not an arbitrary larger benchmark that trivializes the stationary problem.

### 8.2 The beta=0 consequence of the same bound

At beta=0, b=1/M, so IP2-S becomes

    R_master,stat >=(2^-331/Q)
                    ln(1+(1/8)min{Q,M/Q})           (8.2)

in its finite domain. For fixed K>=3, suppose risk<=C_K/sqrt(M). IP2-IID forces Q>=c_0 sqrt(M). If Q>M^(3/4), it already exceeds a constant times sqrt(M) ln M. Otherwise, for sufficiently large M, Q<=M/4 and

    min{Q,M/Q}>=min{c_0 sqrt(M),M^(1/4)}=M^(1/4).

The log in (8.2) is eventually at least `(1/8)ln M`, giving `Q=Omega_K(sqrt(M)ln M)`. The usual dyadic ceiling can realize the matching NB002 sufficient order. Again the fixed-K stationary full-history benchmark is Theta_K(M^-1/2), by its full-class upper and the stationary IID lower.

This is simply another implication of the same finite-domain theorem. It neither settles K=2 nor supplies an alphabet-uniform sharp constant or a new full risk formula at beta=0.

## 9. What the extension establishes and does not establish

- **Stationarity is genuine.** The experiment starts at the hidden pair law Pi in (2.3), not WW. WW is only a selected event of probability bounded below independently of p. Its constant prior likelihood is explicitly paid in (3.3)–(3.5).
- **All-state certificate is genuine.** Every unused-symbol row is specified, and (2.4) covers all initial pairs, not just stationary support.
- **One prior and actual target remain intact.** The common uniform prior survives E_j because its full stationary probability is p-independent. Equation (3.6) retains eta after past no-exit conditioning.
- **Every finite master and exact side field is included.** The 28 support coordinates contain all boundary master blocks; extra alphabet coordinates are zero. The exact endpoint is handled by the finite union, never by falsely conditioning IID observations on it.
- **The finite cutoff is essential.** J is chosen to satisfy both the no-exit window and the tube width, and Q is restricted to [16,M/4] in IP2-S. Larger Q in the threshold corollaries are treated only by their already large magnitude.
- **The generalization disproves two possible explanations for the ray obstruction:** it is not removed merely by requiring stationary initialization, and it is not removed merely by having M beta tend to infinity. It does not identify the full intermediate-beta transition.
- No lower is claimed for arbitrary attention encoders, altered side ports, other quantizers, or changed finite word formats. No training, fault tolerance, joint-K optimality, or total time/space superiority result follows.
- No new upper implementation is introduced. Accepted NB002's encoder, suffix, and complete program/parameter/history/mask/arithmetic/acquisition/movement/output/phase-peak costs remain unchanged. Unlimited real suffix computation is deliberately allowed in the lower.
- Finite companion diagnostics corroborate stationarity, full stationary path factorization, minorization, actual finite full-bank formulas, tube/curve bounds and finite cutoff algebra. They are not a universal proof, independent review, formal verification, external peer review, or an original emitted-network test.

No mathematical obstruction was found in the author check. The remaining obligation is independent review of this new theorem and its stationary quantifiers.

## Sources / provenance

Exact identities and dependency roles are bound in `IP002_source_bindings_v1.json`.

- Original SRC fact `fef8372728290b45.md`, particularly the actual finite evaluator, complete head values, exact side inputs and master lifetime; 035's §5 exact-side audit corroborates the same cut.
- Accepted NB002 and review: legal h>=4 retained prefix, matching sufficient schedule, and full cost scope.
- Accepted SM002 and review: universal stationary IID c/Q lower; its good-event lemma and finite-weight method are restated and reproved above for the present source; its full-history binary IID lower is used only in fixed-K benchmark comparisons.
- Accepted SM001 and review: context for fixed-positive-beta sufficiency, whose constants are not incorrectly made uniform in vanishing beta.
- R011 complete proof: exact statistical scale and full-class beta-blind upper.
- Frozen IP001: direct precursor and the root's original ray construction. IP002 does not rely on its pending acceptance as a theorem: the full source, stationary conditioning, concentration, finite-bank, Bayes and averaging proof is supplied here. IP001 is not edited.
