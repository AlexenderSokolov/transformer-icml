# Independent adversarial review of the stationary add-one candidate

Date: 2026-11-04 UTC.

Reviewed exact file: `stationary_addone_sharp_log.candidate.v1.md`.

SHA-256: `90e949efc52cd8f3d57108ca334f9083a9858950183dd8e6f60d6664d92c6195`.

## Finding

No mathematical error or missing hypothesis was found in this independent analytical review. I checked the stationary density comparison, both likelihood cancellations, all scalar loss inequalities, dyadic summation, degeneracies, terminal indexing, and the matching published lower theorem. This is a proof review, not a literature-priority certification. No numerical experiment, external upload, or external repository mutation was performed.

## 1. The stationary comparison is valid, including reducible chains

A state with positive stationary mass lies in a closed finite irreducible class. All positive-probability outgoing transitions of that class remain within it, and a strictly positive group rescaling preserves its support and irreducibility. The expected return excursion is finite even when the class is periodic.

Before the first positive return to s, the only altered departure is the first one. Thus every expected occupation v_Q(z), for z different from s, is a nonnegative linear combination of first-departure probabilities whose ratios lie in [r_min,r_max]. At s both occupation vectors equal 1, and r_min <= 1 <= r_max. This proves (4), including self-loops.

Give the tilted chain the original weights on closed classes. In the changed class, pi(s)/nu(s)=L_Q/L_P. Therefore pi(z)/nu(z) <= (pi(s)/nu(s))/r_min. On unchanged positive-weight classes the left side is 1 and the right side is at least 1. Zero-stationary-mass states do not enter original-positive paths. There is no omitted irreducibility or uniqueness assumption.

## 2. Both coefficients in (9) follow from different valid integrations

For a path with j target departures and k first-group departures, its likelihood ratio is exactly

    [pi(Y_0)/nu(Y_0)] exp{-j d(q||p) -(k-jq)lambda}.

The shifted event imposes -(k-jq)lambda <= -|lambda|. Since r_max/r_min=exp(|lambda|), comparison (5) gives a likelihood ratio at most exp{-j d(q||p)}. Integrating over E under stationary Q and applying the fixed-target occupation inequality gives (2m/(n+1))exp{-m d(q||p)}.

Separately, comparison (6), together with exp{-|lambda|}/r_min=1/r_max<=1, gives a likelihood ratio at most (pi(s)/nu(s))exp{-j d(q||p)}. Integrating over E uses Q_nu(Y_n=s)=nu(s), leaving exactly pi(s)exp{-m d(q||p)}.

Taking the minimum is legitimate because both calculations bound the same original probability. The two integrations need not make their upper bounds tight on the same paths. This proves the rare-target mass refinement. No conditional binomial law, independent test state, or time reversal is used.

The occupation inequality itself follows by translating each shorter window to the suffix ending at n, using stationarity only, and counting the first w occurrences along a forward trajectory.

## 3. Threshold and scalar-loss checks

The centered Bernoulli log moment-generating bound holds for both signs using |Z|<=1 and E Z^2<=p. Substituting a=delta/(p+delta/3) in the KL variational inequality gives d(p +/- delta||p)>=delta^2/[2(p+delta/3)]. The stated delta makes this at least t/m. On m<=j<2m, j delta<=sqrt(4jpt)+4t/3, so the additional one-count shift is preserved. If q crosses an endpoint, that corresponding strict deviation event is impossible. For p=0 or p=1 the observed count is deterministically jp on every original-positive path.

For (12), the premise gives z<=2k+10u/3 and (k-z)^2<=8ku+128u^2/9. Consequently ((j+1)p-k-1)^2<=16ku+31u^2 for u>=1. If k+1>=u, h<=47u. Otherwise x=(j+1)p<6u and k+1>=1 give h<=6u log(6u)+u<=48u(1+log u). All directions and constants check.

The identity (13) is exact. Its remainder is (A-1)-(j+1)log(1+(A-1)/(j+1))>=0. The replacement u=4t dominates the extra +1 in (11) for t>=1. The layer-cake integral is bounded by [576+3456/e]beta/m<2304beta/m.

## 4. The low-count estimate is a full-row bound

For j>=1 and 0<p<1, ell>log4 implies k+1<(j+1)p/4<=jp/2, hence k<jp/2-1. This is contained in the precise shifted lower-tail event for q=p/2; there is no lost unit or missing boundary case.

The binary KL curvature satisfies 1/[t(1-t)]>=1/p on [p/2,p], so d(p/2||p)>=p/8. Also j+1<=2m, which bounds ell by log_+(2mp). Splitting at log4 therefore gives

    E[1_E ell] <= beta [log4+log_+(2mp) exp(-mp/8)] < 10 beta.

The last inequality follows uniformly from log_+(2z)<=2z and 2z exp(-z/8)<=16/e<8. The decomposition weights this quantity by p before summing, so its contribution is 10 beta, not 10A beta. At p=1 the logarithm is zero; p=0 has its declared zero weighted contribution. Formally one may define ell=0 at p=0, but this is only a notational convenience and not a proof repair.

## 5. Count summation and constants

The sum of target coefficients satisfies sum_s beta_s,m<=min{2Dm/(n+1),1}, regardless of how small or unequal the stationary masses are. The targetwise minimum of the two loss bounds may be factored because both have the same beta coefficient.

For m<A, the dyadic weighted logarithmic sum is bounded by 26A. For A<=m<=T, every band costs at most 2304A/T and the count of bands is at most 1+log(T/A)/log2. For m>=A and m>T, the geometric reciprocal sum is less than 2/T. These ranges partition all positive-count bands, including T<A. The no-visit contribution is at most D log(A)/(n+1)<=H.

The constant sum is 52+4608+9216+1=13877. Since 4608/log2<=9216 and log_+(R/2)<=log_+(R), the advertised 14000 H(1+log_+R) bound follows. All inequalities are uniform in n and A. The trivial log(n+A) bound and n=0 treatment are correct.

## 6. External theorem and scope

I read the local published HJW PDF, especially Theorem 22 and equation (103), rather than relying solely on the candidate's literature summary. The theorem has a constant C_m depending only on order m, uniformly in alphabet and sample size. Its risk is the expected forward KL at the actual terminal context of a stationary trajectory. Taking N=n+2 and order 2 matches this candidate exactly.

Enlarging C_2 to at least 2 preserves the theorem and narrows its range harmlessly; on that range N/A^3>=8. Thus the candidate's 1+log_+((n+1)/A^3) and denominator n+1 are within absolute constant factors of HJW's log(N/A^3) and denominator N. This establishes the claimed uniform growing-alphabet rate implication if the upper proof is accepted.

The same argument applies to ordinary first-order chains with D=A=k and n=N-1, giving an upper bound 14000 k^2/N [1+log_+(N/k^2)]. In the Theorem 1 regime 3<=k<=sqrt(N)/C, with C enlarged to at least 2, this matches that theorem's minimax rate. HJW Remark 1 explicitly asks whether the ordinary full-history add-one estimator attains that rate. The mathematics reviewed here answers that question as stated in the 2023 paper. Whether it remains unresolved in later literature, or whether this proof has publication priority, requires a separate literature check. The binary first-order log-log rate is not attained, exactly as the candidate states.
