# Supplied-beta adaptation — exact barriers to the old rare-prefix route

2026-11-02. **UNREVIEWED research-contributor notes.** These are new derivations, not an accepted theorem or an independent review. Accepted AB001–AB003 are unchanged. The full-history, supplied-beta, unknown-k adaptation question remains open here.

## Findings first

1. Varying stationary masses does not rescue the same-beta version of AB001: a slow initial 11 trap and a fixed positive certificate force the entire stationary 00 designated-exit risk to be small.
2. There is an exact likelihood penalty for the isolated-fake-exit words used in AB002. If their long initial 11 prefix is at least as long as their 00 row sample, every same-beta source pays an exponential penalty of order exp(-c k sqrt(beta)) relative to the unconstrained rowwise MLE. This is valid conditional on initial pair 11, so it is not merely a stationary-start observation.
3. These are route barriers, not a general impossibility theorem, not a complete obstruction to every transport kernel, and not a proof of an adaptive estimator. In particular they do not concern canonicalized words with additional visits to 11 later in the word.

## 1. General stationary flow barrier

Write the fixed designated exits as (a,b,e,tau) at states (00,01,10,11), and write a qualifying full-support stationary law as

    Pi=(y,x,x,w),  ya=xe,  w*tau=x*b.

The all-state two-step certificate gives

    ea>=beta*x,   b*tau>=beta*x.

For beta>0, stationarity then yields the exact necessary inequalities

    e^2>=beta*y,  b^2>=beta*w,
    x<=a sqrt(y/beta),  x<=tau sqrt(w/beta).

Consequently

    y*a=x*e<=tau sqrt(w/beta),
    w*tau=x*b<=a sqrt(y/beta).                       (1.1)

For example, any stationary clean alternative whose 11 exit rate obeys tau<=c/M satisfies, at beta>=c_beta/M,

    E[ q_00 1{terminal context=00} ]=y*a
        <= (c/sqrt(c_beta)) M^-1/2.

Thus a clean O(M^-1/2) guarantee alone cannot force accurate nonzero 00 predictions on this family: suppressing the entire 00 designated probability has only statistical-order stationary risk. This conclusion allows arbitrary stationary mass y and arbitrary e; it is not limited to AB001's equal diagonal masses.

This is not a proof that suppressing 00 is globally optimal, because losses at other rows must still be controlled. It only shows that the proposed constrained-risk lower cannot force a larger contribution from this row using that clean family. For arbitrary initial laws, (1.1) still constrains the table but does not by itself bound actual-terminal probability; §2 treats a particular long-prefix pattern directly.

The positive-beta singleton-support cases do not provide an overlooked high-exit 00 alternative with a long 11 prefix: if 00 is absorbing, a=0; if 11 is absorbing, a word beginning 11 and later leaving it has probability zero.

## 2. An exact same-beta likelihood barrier for isolated fake exits

### 2.1 Pattern and unrestricted reference likelihood

Consider any legal binary word beginning with 11 and ending with 00, with precisely these departure counts:

    111: L, 110: 1,
    100: k+1, 101: 0,
    010: k,   011: 0,
    001: k,   000: J-k,

where L>=J>=k>=1. Such words consist of a long initial run of ones followed by a zero-like part with k isolated ones, no subsequent 11, and a protected final 00. They have M=L+J+2k+2 departures. Their exact conditional likelihood from initial pair 11 under a source with designated parameters (a,b,e,tau) is

    ell_Q = tau(1-tau)^L e^(k+1) (1-b)^k
             a^k(1-a)^(J-k).                        (2.1)

The unrestricted rowwise MLE has

    a_hat=p=k/J, b_hat=0, e_hat=1, tau_hat=1/(L+1).

Let ell_MLE be (2.1) evaluated at these values, with 0^0=1. This is only a comparison likelihood; that unrestricted MLE need not belong to D_2(beta).

### 2.2 Claimed bound

For every beta in (0,1], every table in D_2(beta), and every qualifying initial law,

    P_Q(word | initial pair 11)
       <= 4 exp[-k sqrt(beta)/8] ell_MLE.            (2.2)

Conditional probability means the ordinary Markov law started at 11, whether or not its actual initial law assigns positive mass there. Multiplying by any initial mass <=1 preserves an unconditional upper bound. No source parameter is supplied to an attacker or estimator; this statement compares likelihoods in the analysis only.

### 2.3 Proof: certificate constraint

If the word has zero probability, the claim is immediate. Otherwise a,e,tau are positive and neither diagonal can be absorbing. The positive-beta support classification therefore gives full stationary support. Its normalizing formula is

    1/x=e/a+2+b/tau.

Since b*tau>=beta*x,

    beta <= b*tau/x
          = b*tau*e/a+2b*tau+b^2
          <= b^2+3b*tau/a.                          (2.3)

Boundary tables that give positive probability are covered by these same identities; at positive beta full support also prevents the problematic zero factors. This proof does not substitute a stationary initialization for the conditional initial pair 11.

### 2.4 Proof: likelihood comparisons

First, the 11 row likelihood ratio obeys, for every 0<=tau<=1 and L>=1,

    [tau(1-tau)^L]
      /[(1/(L+1))(L/(L+1))^L]
      <=4 exp(-L*tau/2).                             (2.4)

Indeed the denominator is at least 1/[euler_e*(L+1)], the numerator is at most tau exp(-L*tau), and (L+1)/L<=2. With u=L*tau, the resulting 2*euler_e*u*exp(-u) is at most 4 exp(-u/2), since max_(u>=0) u exp(-u/2)=2/euler_e. The row likelihood ratio is also at most one, by the definition of its MLE.

If a<p/2, the 00 row likelihood ratio is exp[-J D(p||a)]. Monotonicity in a below p and the elementary bound

    D(p||p/2)>=p(log 2-1/2)

give ratio <=exp[-(log 2-1/2)k]<=exp(-k/8). The inequality also holds at p=1 by its limiting convention. All other row ratios are <=1. Since sqrt(beta)<=1, this proves (2.2) in this case.

Now suppose a>=p/2=k/(2J). The 00 row ratio is <=1, e^(k+1)<=1, and (1-b)^k<=exp(-k*b). By (2.4), the full ratio is at most

    4 exp[-k*b-L*tau/2].                             (2.5)

Equation (2.3) yields two cases. If b^2>=beta/2 then k*b>=k sqrt(beta/2). Otherwise

    b*tau>=beta*a/6>=beta*k/(12J).

Arithmetic-geometric mean and L>=J give

    k*b+L*tau/2 >=2 sqrt(k*L*b*tau/2)
                 >=k sqrt(beta*L/(6J))
                 >=k sqrt(beta/6).

Both cases are stronger than the exponent required in (2.2). This proves the claimed inequality.

### 2.5 Interpretation and limitations

At beta=1/M, any such pattern with k/sqrt(M) diverging is exponentially disfavored by every same-beta clean source relative to its own unconstrained empirical-row fit. Thus the original fake-isolated-exit kernel cannot simply be declared clean-looking in that regime. A same-beta conditional clean comparison must pay for its long-prefix/exit-survival event; conditioning away that probability would invalidate constrained-risk accounting.

The factor ell_MLE depends on the observed word/counts. Summing (2.2) over a class of words requires controlling the sum of these MLE likelihoods, so (2.2) alone is not a hypothesis test with a proved uniform error, a complete transport obstruction, or an adaptive risk bound. A pattern test using the conditional ordering information is a plausible constructive direction, but no such estimator theorem is proved here. A beta-constrained likelihood fit alone is insufficient as a generic proposed remedy: for a homogeneous second-order source, likelihood is a function only of the initial pair and full triple counts. If a same-beta histogram-only adaptation obstruction is established, it also applies to any estimator based solely on that likelihood fit. A full-history estimator would then have to exploit order information ancillary to the clean sufficient statistic.

The current statement deliberately excludes words with later 11 visits, even if all 111 self-loops are moved to the front. Those words have nonzero 011/110 cycle counts and a different likelihood balance. A proposed histogram-only obstruction based on rearranging those cycles is not contradicted by (2.2).

## 3. Failed constructions preserved

### Active suffix with b=0

A long 11 wait followed by a closed {00,01,10} active suffix with a>0, e=1-a, b=0 is legitimate at beta=0. It is not in any positive-beta class with positive crossing mass because P^2(01,10)=b*tau=0 while Pi_10>0. This is precisely the old AB001 cross-class mechanism, not a supplied-beta obstruction.

### Shrinking the alternative stationary 00 mass

Allowing small y can permit a much larger a than the equal-mass AB001 family. However (1.1) bounds y*a and, for a zero-like suffix, small stationary mass also increases the relative return hazard toward 11. It does not justify transferring the same clean-risk subtraction unchanged. Section 2 quantifies this for the isolated-exit pattern, without stationarity of the initial law.

### Singleton alternative absorbing at 11

Starting a clean alternative at crossing state 01 and letting it eventually absorb at 11 can permit a large transient 00 exit a. But a positive certificate requires a*b>=beta. If the initial crossing prefix must survive for order M time, its 01->11 hazard b is paid on order M/2 visits. For a shrinking a≈k/t, b>=beta/a makes the shared long prefix exponentially unlikely at beta≈1/M. Keeping a bounded below avoids this but gives only order-k suffix windows, not an extra harmonic logarithm. This is a route diagnosis, not a universal bound for every such family.

## 4. Ancillary ordering versus clean sufficient statistics

For a fixed initial pair, a clean homogeneous second-order source gives every word with the same triple counts exactly the same probability, the product of row-transition probabilities to those counts. Conditional on a nonempty type class and the initial pair, its word arrangement is therefore uniform and parameter-independent. Stationary initialization only adds a source-dependent initial-pair factor, which disappears after conditioning on that pair.

This does not mean order may be discarded in the corruption experiment: an attack can change the conditional arrangement law, so unusual concentration of self-loops or dwell times can provide evidence of corruption. A canonicalization attack that moves all 111 loops to the front can preserve a clean sufficient statistic while strongly violating this conditional uniformity. Conversely, to obtain a full-history adaptation lower one must account for the entire output arrangement, not merely match its histogram. Replacing a canonical output by a uniform random clean arrangement can require far more Hamming changes; it is a separate transport claim and cannot be assumed.

Thus a same-beta histogram-only lower, if valid, would be a meaningful separation of required information rather than a resolution of full-history adaptation.

## 5. What remains open

Find one estimator A_(M,beta), independent of k, attaining H_2 for every budget, or construct a genuinely same-beta full-history lower disproving it. Neither varying stationary masses, conditioning away an unlikely prefix/suffix, nor restricting the predictor to a terminal histogram answers that question. Exact ordering information may be decisive. All claims in these notes require a fresh independent review before acceptance.
