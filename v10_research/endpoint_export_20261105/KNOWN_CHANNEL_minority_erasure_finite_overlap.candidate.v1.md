# Finite overlap comparison for one-sided one-edit channels

5 November 2026 UTC. Pure analytical candidate, pending independent review. No scientific execution, numerical diagnostic, public write, or fitted-minimax theorem. Earlier reviewed files are preserved unchanged.

## 1. Finite-alternative result

Fix 0<beta<1 and B<infinity, and let N=M+2 with M>=2. Let theta_0,theta_1 be two positive stationary binary order-two sources. Assume theta_0 has P_0^2>=beta Pi_0, that pi_0(1)<=1/2, and that their transition entries satisfy

    max_(u,c) |log(theta_1,u(c)/theta_0,u(c))|<=B.       (F1)

Both endpoints may be required to belong to D2(beta) with symbol 1 a minority; the proof only needs the preceding assumptions. Entries may tend to zero with the horizon. B bounds relative changes, not a positive transition floor.

Let C be the same disclosed source-independent S=1 online channel under both alternatives, with actual counter e in {0,1}, at most one edit on every path, and

    a_i(0)=0 for i<=N-2.                               (F2)

Thus its fixed public nonterminal operation can erase 1 but cannot insert 1. Both endpoint positions remain arbitrary within the strict budget. The channel does not know which source is true or consult its marginal. An endpoint certificate rho can be imposed but is not needed in this result.

Write P_j for the full stationary raw-word law under theta_j, P_j^Z for its output law, and p_j(z) for its own source-specific next-1 posterior. Define

    d_H^2(theta_0,theta_1)
      =sum_u Pi_0(u) sum_(c=0,1)
             (sqrt(theta_1,u(c))-sqrt(theta_0,u(c)))^2.

There is a finite constant C_(beta,B), independent of N and all channel hazards, such that

    sum_z min{P_0^Z(z),P_1^Z(z)} |p_0(z)-p_1(z)|
       <= C_(beta,B) d_H(theta_0,theta_1).              (F3)

This is an overlap-weighted finite comparison. It does not assert the same upper under P_0^Z alone, and it does not permit a separately fitted theta_1(z) to be substituted into its integrated statement.

## 2. Stationary geometric transition path

For t in [0,1] define

    Z_u(t)=sum_c theta_0,u(c)^(1-t) theta_1,u(c)^t,
    theta_t,u(c)=theta_0,u(c)^(1-t)theta_1,u(c)^t/Z_u(t).

Let Pi_t be the stationary pair law of theta_t, and let P_t be its stationary raw-word law. Positivity on all legal pair transitions gives an irreducible pair chain and a differentiable stationary law.

By Holder's inequality Z_u(t)<=1. From (F1), Z_u(t)>=exp(-tB) and

    exp(-2B)<=theta_t,u(c)/theta_0,u(c)<=exp(2B).       (F4)

The constants in (F4) are deliberately loose.

For completeness, the finite-state stationary tree formula writes Pi(s) as the total weight of directed in-arborescences rooted at s, divided by the total weight over all roots. There are four pair states and each spanning tree has three transition factors. If every legal transition ratio lies between exp(-D) and exp(D), each tree ratio lies between exp(-3D) and exp(3D), and normalization puts every stationary coordinate ratio between exp(-6D) and exp(6D). The legal zero entries are the same for all paths and contribute no trees under any parameter.

Apply this formula to (F4), and separately to the endpoint ratio (F1):

    exp(-12B)<=Pi_t(u)/Pi_0(u)<=exp(12B),
    exp(-6B)<=Pi_1(u)/Pi_0(u)<=exp(6B).               (F5)

The two-step transition entries are products of two legal transition entries. Hence

    P_t^2(s,u)>=exp(-4B) P_0^2(s,u)
              >=beta exp(-16B) Pi_t(u).               (F6)

Thus the entire path has a supplied uniform certificate beta_*=beta exp(-16B).

## 3. The source-wise derivative bound is uniform along this path

The reviewed result in `KNOWN_CHANNEL_one_edit_minority_erasure_score.candidate.v1.md` applies at every path point with pi_t(1)<=1/2, using beta_*.

If pi_t(1)>1/2 instead, (F5) and pi_0(0)>=1/2 give

    pi_t(0)>=exp(-12B)/2,
    min_c pi_t(c)>=exp(-12B)/2.                        (F7)

This portion of the path is uniformly bounded away from either constant-symbol boundary. Its stationary triple probabilities are at least

    beta_*^2 (exp(-12B)/2)^3
       = beta^2 exp(-68B)/8.                           (F8)

For every strict-one-edit channel, the count covariance is at most six in absolute integrated value. Equation (F8) therefore gives the same type of bound C_(beta,B)sqrt(p_abc) for every triple, without requiring a minority-erasure argument on this balanced portion. The transition-score combination, stationary initial-law L2 resolvent, and direct-row derivative from Sections 4-6 of the reviewed score note then apply unchanged.

Consequently, with I_step(t) the stationary one-step Fisher information along this path and the channel held fixed,

    E_(P_t,C)|dot p_t(Z)|<=C_(beta,B) sqrt(I_step(t))  (F9)

for all t. This argument does not assume that the erased symbol stays a minority under nonlinear stationary interpolation.

## 4. Raw geometric domination has no horizon factor

Equation (F5) gives

    Pi_t(u)>=exp(-18B) Pi_0(u)^(1-t)Pi_1(u)^t.

Since each Z_u(t)<=1, all normalized path transitions are at least their unnormalized geometric interpolants. Thus, for every raw word x,

    P_t(x)>=exp(-18B) P_0(x)^(1-t)P_1(x)^t.            (F10)

The constant in (F10) has no factor N. Normalizing each transition row only increases the corresponding geometric term. The stationary initial-law comparison was paid separately.

## 5. One-edit posterior fibers convert raw domination into output domination

Fix any channel-reachable z. Every source assigns positive probability to every raw word, so the output support is common to all t. Any two supported raw preimages x,y have d_H(x,y)<=2. At most six historical triple positions differ.

Let L(x)=log(P_1(x)/P_0(x)). Each transition log ratio is in [-B,B], and each initial-pair log ratio is in [-6B,6B] by (F5). Therefore

    max_(x,y preimages of z) |L(x)-L(y)|<=24B.         (F11)

Let mu_0(.|z),mu_1(.|z) be the two raw posteriors. The channel factor cancels from their density ratio. Its logarithmic oscillation is bounded by 24B; normalization then puts that density ratio between exp(-24B) and exp(24B). Hence

    sum_x mu_0(x|z)^(1-t)mu_1(x|z)^t>=exp(-24B).      (F12)

Applying the common channel to (F10), then using (F12), yields

    P_t^Z(z)
      >=exp(-18B) sum_x C(z|x)P_0(x)^(1-t)P_1(x)^t
      >=exp(-42B) P_0^Z(z)^(1-t)P_1^Z(z)^t
      >=exp(-42B) min{P_0^Z(z),P_1^Z(z)}.              (F13)

This is the precise common-measure bridge needed for integrating (F9). A raw Hellinger comparison alone would not imply (F13); the bounded one-edit fiber oscillation is used explicitly.

## 6. Integrate the actual posterior target

The finite model and common positive output support permit differentiation and integration pointwise in z. Equations (F9) and (F13) give

    sum_z min{P_0^Z,P_1^Z}|p_1-p_0|
      <=exp(42B) integral_0^1 E_(P_t,C)|dot p_t(Z)| dt
      <=C_(beta,B) integral_0^1 sqrt(I_step(t)) dt.     (F14)

This keeps the direct future-row derivative and the full stationary initial-law score; neither is dropped.

It remains to bound the path length by the displayed row geometry. Write q_j,u=theta_j,u(1) and

    Delta ell_u=logit(q_1,u)-logit(q_0,u).

Geometric transition interpolation is linear in log odds, so dot ell_u=Delta ell_u. Equations (F4)-(F5) give

    I_step(t)
      <=exp(16B) sum_u Pi_0(u)q_0,u(1-q_0,u)
                                    (Delta ell_u)^2.  (F15)

For r in [exp(-B),exp(B)],

    |log r|<=2 exp(B/2)|sqrt(r)-1|.

Applying this separately to the success and failure ratios, and using (a-b)^2<=2a^2+2b^2, gives

    q_0(1-q_0)(Delta ell)^2
       <=8 exp(B) H^2(Ber(q_0),Ber(q_1)).              (F16)

Therefore I_step(t)<=8 exp(17B)d_H^2 throughout the path. Substitute in (F14) to prove (F3).

## 7. What this does and does not imply for fitting

The finite comparison is genuine and has no positive transition floor. It requires bounded endpoint relative transition changes, with constants depending on B. It applies to one fixed common channel and two fixed sources; its left side uses their actual output-law overlap.

It does not finish a minimax upper for a fitted source. In particular:

1. Replacing theta_1 by theta_hat(Z) selects a different source at each output. The sum in (F3) was proved for one fixed theta_1 and does not justify that substitution.
2. Converting overlap loss to P_0-weighted loss by a trivial bound adds TV(P_0^Z,P_1^Z). At the usual local estimation scale, full-history TV need not vanish, so this conversion can erase a root-M conclusion.
3. Typical fitted rare rows need not obey a fixed B relative-ratio bound when their counts are small. Smoothing alone does not prove that condition uniformly, and boundary sources need separate handling.
4. The common-erasure orientation is a fixed channel property. Neither the channel nor the predictor is allowed to consult the true source to relabel symbols.

A future estimator proof could use (F3) within a testing or local aggregation argument, but would have to establish that construction, its uniform error, and its treatment of rare/boundary parameters. No such construction is supplied here.
