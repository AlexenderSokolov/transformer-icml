# A simple source where the predictor is uniformly accurate

2026-11-03. This additive observation supplements the bounded-number 3SAT construction without altering it. Fix its M and predictor q. Let the underlying binary process be iid Bernoulli(p) with p=1/M². Its pair-state transition matrix satisfies P²(u,v)=Pi(v) for all pairs u,v, with Pi the iid pair law, so it has beta=1. For every binary input z, the construction outputs q(z) in [1/M,3/(2M)]. Therefore its next-symbol TV error for this one source, for every clean history and every legal or illegal binary corruption, is at most

  3/(2M) - 1/M².

The specific all-zero clean history used for the NP-hard attack occurs with probability (1-1/M²)^(M+2) >= 1-(M+2)/M². This elementary example shows a computational hardness of finding an exact or extremely fine maximum of the specified surrogate even where the predictor has a simple small uniform prediction-error guarantee for this single source. It does not establish its performance on the general unknown-source class, a lower bound on actual expected TV risk, or a lower bound on training; nor does it assert that the surrogate target B(h) equals the true p.
