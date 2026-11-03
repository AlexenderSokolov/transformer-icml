# PBF001: a sharp bias window and a constrained population update

3 November 2026. Root-authored candidate for separate review, not yet accepted or published. This is a corollary inside PGT001's supplied-feature scalar model. It is not a theorem about learning attention, general SGD, or finite-precision training, and makes no novelty claim.

## 1. The fixed model and question

Use PGT001's clean uniform-row-prior training experiment and critical all-state protected-terminal testing experiment, with M>=64. The exact Bayes count rule is B, the first-terminal-bit fallback is F, the supplied hard half gate is G, and H=GB+(1-G)F. Put

    s=M^(-1/2), K=(log M)/2, ell=1+log((M+2)/2),
    w0=sigmoid(b-K), w1=sigmoid(b+K),
    q_b=omega_b B+(1-omega_b)F, omega_b=wG.

Here wG means w1 on G=1 and w0 on G=0. In this note b>=0. This contains all iterates of PGT001's unconstrained population gradient descent from b=0. The source, kernel, target, randomization, and normalized risk factors Gamma_stat and Gamma_all are exactly those stated in PGT001 and CTO001. They compare one fixed map at each horizon across all unknown budgets, normalized by g_M(k)=max(s,k/M).

The question is not only the b->infinity limit: how far may the bias grow with the horizon while keeping a uniform robust factor, and can a constrained population update stay in that range?

## 2. Imported accepted interfaces

The source proofs are imported at their exact stated scope:

- Every full-history prediction map has Gamma_stat>=c0=1/96, by the clean IID/oracle floor in the accepted finite positional manuscript.
- CTO001 supplies cB ell<=Gamma_stat(B)<=Gamma_all(B)<=560+192(1+log M), with cB=2^(-30). Since 1+log M<=ell+log2<=2ell and ell>=1, Gamma_all(B)<=944 ell.
- PGT001 section3 proves Gamma_all(H)<=CH=2^17+2^23+208. This follows before its sigmoid approximation: the accepted empirical gate costs 2^17 s+2^23 k/M, and its difference from H costs at most16s+192k/M.
- PGT001 proves that the clean population loss L_M(b) is continuously differentiable and -1<L_M'(b)<0 for every finite b, and that L_M(0)-L_M(B)=O(log M/sqrt M), with the explicit finite conditions in its section6.

The fixed word domain is finite, and every prediction risk is at most one. All factors above are consequently finite. The lower floor applies to arbitrary full-history maps and independent prediction seeds; it does not assume a count-only observation.

## 3. Exact mixture identity and finite bounds

There is the exact pathwise identity

    q_b = w0 B + (1-w0)H + (1-w1)1{G=1}(F-B).       (1)

On G=0 it is the defining mixture of B and F. On G=1 the first two terms equal B, and the last gives the defining mixture with weight w1. Its remainder has uniform absolute value at most

    1-w1 <= exp(-b-K)=s exp(-b).                    (2)

The scalar w0 depends only on public M,b, not on the observation or source. Convexity of absolute loss, (1), (2), and g_M(k)>=s give

    Gamma_all(q_b) <= w0 Gamma_all(B)
                         +(1-w0)Gamma_all(H)+exp(-b).

For the lower bound, the reverse triangle inequality gives on every word and true target p

    |q_b-p| >= w0 |B-p| -(1-w0)|H-p| - |remainder|.

Average in any stationary testing experiment, divide by that experiment's own g, and use the UNIFORM upper bound on H. Then take a supremum over those same experiments. If a supremum for B is not attained, use an approximating sequence; no worst source is assumed common to B and H. We obtain

    Gamma_stat(q_b) >= w0 Gamma_stat(B)
                              -(1-w0)CH-exp(-b).

Set x=ell sigmoid(b-K) and D=CH+1. Since b>=0, exp(-b)<=1. The exact finite conclusion is

    max{c0,cB x-D} <= Gamma_stat(q_b)
                  <= Gamma_all(q_b) <= D+944 x.     (3)

The full-history floor c0 is essential when the subtraction is negative. Without it the lower inequality alone would not prove a constant-factor statement near x=0.

Let T=2D/cB and c=min{c0/(1+T),cB/4}. Then

    c(1+x) <= Gamma_stat(q_b)
            <= Gamma_all(q_b) <= D(1+x),           (4)

where D>=944. Indeed, if x<=T use the floor c0. If x>T, cB x-D>=cB x/2>=cB(1+x)/4, because T>=1. Thus the robust factor is uniformly

    Theta(1+ell sigmoid(b-(log M)/2)),  M>=64,b>=0.

All constants are numerical and independent of both M and b. They inherit large conservative statistical constants and do not establish a practical numerical threshold. This is a factor in the specified critical testing experiment, not a new minimax rate for arbitrary encoders.

## 4. Which bias schedules preserve a uniform factor

For any sequence b_M>=0 indexed by integers M>=64, a single finite constant bounds the factors of q_(b_M) at every horizon if and only if

    sup_M ell_M sigmoid(b_M-K_M) < infinity.        (5)

Equivalently, there is a finite real C such that, for all sufficiently large M,

    b_M <= (log M)/2 - log ell_M + C.              (6)

For sufficiency, sigmoid(z)<=exp(z) gives x<=exp(C) on that tail; finitely many initial horizons have finite factors. For necessity let x<=A uniformly. Since ell_M tends to infinity, eventually ell_M>=2A and w0<=A/ell_M<=1/2. The inverse-logit identity gives

    b_M-K_M=log(w0/(1-w0)) <=log(2A/ell_M).

This proves (6); A is positive because w0>0. No monotonicity of b_M in M is needed. Equation (6) is a criterion for this fixed one-bias family only. It is neither a universal neural parameter bound nor a statement that clean optimization automatically stops there.

## 5. A projected update that stays robust

Define the public cap

    cap_M = K_M - log ell_M.

It is positive for every M>=64. To check this, sqrt M-1-log((M+2)/2) is increasing: its derivative is 1/(2sqrt M)-1/(M+2)>0. At M=64 it is 7-log33>0, for example log33<4 since e^4>33. Thus sqrt M>ell_M and cap_M>0.

For any fixed finite a>0, initialize b0=0 and use the exact projected population update

    b_(t+1)=min{cap_M, b_t-a L_M'(b_t)}.            (7)

All iterates remain in [0,cap_M]. Because L_M'<0 everywhere, they increase strictly until the cap and stay there thereafter. Loss decreases strictly before the cap and is constant after it. The cap is the unique minimizer of L_M over this interval.

This update reaches the cap after finitely many steps at each fixed M. Continuity and strict negativity give

    m_M=min_(b in[0,cap_M]) [-L_M'(b)] >0.

Until hitting the cap each increment is at least a m_M, so a conservative hitting bound is ceil(cap_M/(a m_M))+1. This is an existence bound; no efficient evaluation of m_M or iteration bound uniform in M is claimed.

For every b in[0,cap_M],

    sigmoid(b-K_M) <= sigmoid(-log ell_M)=1/(1+ell_M),
    x<=ell_M/(1+ell_M)<1.

Equation (3) therefore yields the common all-iteration guarantee

    Gamma_all(q_(b_t)) <= CH+945.                  (8)

At the same time L_M(b_t)<=L_M(0), so the explicit initial excess bound of PGT001 also holds at every iterate; in particular the clean excess is O(log M/sqrt M) along horizons. This conclusion uses the earlier weak-certificate prior averaging and entropy argument, not a new assumption that every training source belongs to the critical testing class.

## 6. Scope and interpretation

At each fixed M, the unconstrained update in PGT001 eventually exceeds any specified finite cap. Its fixed-M limit family has unbounded factors across horizons. This does not assert a common finite iteration at which every horizon crosses a chosen bias schedule. The explicitly projected update (7), in contrast, remains inside a sufficient and order-sharp bias window of the same fixed family. This is a concrete mathematical constraint preserving a supplied positional safeguard while improving clean loss within that constraint.

The positional feature, Bayes computation, source prior and clean population oracle are specified inputs to the model. They are not learned here. The real logarithmic cap, sigmoid, exact gradient, comparisons, storage and precision remain unpriced; (7) is not a finite-bit training implementation. The result does not establish general SGD behavior, necessity of this cap in other models, monotone robustness along the unconstrained path, a practical degradation horizon, or a new general principle of constrained optimization. Constant-factor closure uses the existing count-only lower and robust gate upper, not a newly constructed adversary. There is no external novelty certification, external write, or frozen manuscript modification.
