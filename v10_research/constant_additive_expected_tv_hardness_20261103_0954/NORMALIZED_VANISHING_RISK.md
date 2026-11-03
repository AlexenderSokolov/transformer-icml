# Constant additive gap after normalizing a vanishing risk

2026-11-03. This is a separate consequence of the **earlier**, less-rescaled model in `../constant_factor_expected_tv_hardness_20261103_0945/RESEARCH_NOTE.scope_corrected.md`. It does not modify the present construction or claim a constant additive gap in its unnormalized TV.

In that earlier model q(z)=p+S(z)/(MP), with p=1/M², 0<=S<=m<=P and M,P powers of two. Therefore every history and edit has actual-source TV q-p<=1/M. As proved there, its optimal expected true TV is R*=S*/(MP), so its normalized value is

  M R* = S*/P.

Using Håstad's satisfiable versus at-most-15/16-satisfiable gap with all original m clauses retained, the normalized yes value is m/P>1/2, while the no value is at most (15/16)(m/P). Their difference is (1/16)(m/P)>1/32. Thus the midpoint separates the cases by more than 1/64: an algorithm that computes M R* with absolute error at most 1/64 on all these instances would decide the NP-hard promise. Dividing by M shows this is a precision of 1/(64M) in the original expected TV, not a constant absolute-TV error. The previous 7/8 multiplicative-value conclusion is consistent with and sharper in its own metric.

The earlier model still enjoys TV<=1/M for this one known iid source, not for the general source class, and the classical constant-p predictor has exactly zero source risk. The normalized quantity is a deliberately rescaled computational evaluation target; this observation makes no claim that ordinary unnormalized TV has a constant gap while vanishing uniformly. No new experiment or random operation was performed; independent review is needed for the arithmetic and scope.
