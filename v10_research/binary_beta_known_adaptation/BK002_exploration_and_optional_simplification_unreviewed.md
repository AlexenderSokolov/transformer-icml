# BK002 development record and optional alternative — UNREVIEWED

2026-11-02. This file records genuine research routes and an optional simplification. It is NOT part of the frozen BK002 proof and is not an independently accepted theorem. The current reference-sampler proof was kept unchanged during fresh review to avoid unnecessary version churn.

## 1. Actual route to the same-beta full-history witness

The first contemplated repair of the old beta=0 alternative kept a stationary law with comparable diagonal masses. Its positive-beta certificate forced a<=O(1/(M sqrt(beta))), so the suffix range a≈k/t was cut at t≈k M sqrt(beta), reproducing rather than exceeding the known profile. That failure is real and remains in AB002 / same_beta_route_barriers_unreviewed.md.

A different stationary-mass family avoids that restriction. Fix b=delta, e=1-delta and a common 11 exit rate tau, while varying a. Its stationary 11 mass is

    Pi11=[1+e*tau/(a*delta)+2tau/delta]^-1.

Choosing tau=c L/M, delta=L/k keeps delta/tau=M/(ck), so the 11 mass stays bounded below throughout a≈ck/t_suffix with t_suffix<=M/8. The all-state small cross entries obey b*tau=beta*(ck/M), and a>=delta covers the remaining potentially restrictive entries.

Initially the construction used L≈log n with M=n^10,k=n^9. The reference active suffix loses at most exp(-2L) relative to a legal clean continuation, and the long prefix costs only exp(-2cL)/(cL). This still leaves the clean-risk penalty below the corruption gain. Root independently derived a general growing-L range-envelope version, taking L≈log(k/sqrt(M))/8.

The decisive simplification was L=1: for every k/sqrt(M) tending to infinity, a>=delta already holds eventually. Constant likelihood loss is enough. The final candidate then chose c=1/4, not BK001's c=2^-12, and used exact Bernoulli/one-quarter bounds rather than exponential estimates. These choices produced the saved BK002 finite inequality. No general-L theorem had been saved or accepted before this simplification; this is a research-history account, not a fabricated prior proof version.

## 2. Root-proposed actual-clean-sampling alternative

After the current BK002 proof was saved, root proposed sampling the actual Q_a continuation instead of the reference R and accepting only if it never visits11, ends00, and has at most k ones. This is a different kernel, potentially simplifying the proof; it is not needed to correct any known defect in the saved version.

Couple Q_a and R until the first 01->11 transition. Before disagreement, each 01 departure follows an emitted one, so disagreement probability is at most delta E_R L<=1/16 for the final BK002 intervals. The reference budget failure is at most1/16 and its terminal00 probability at least9/16. Thus actual-clean acceptance is at least7/16, conservatively1/4. The accepted clean error is then bounded directly by e_(a,t), without the factor4 likelihood conversion.

With the final c=1/4 prefix ratio v/w<=4, same-a integration would bound the negative term by8 S log(2T/k). Using only acceptance1/4 and a-r>=a/2 yields a positive coefficient3k/(4096M), rather than the saved reference proof's3k/(2048M). Either route would suffice for the same asymptotic conclusion.

This alternative was deliberately NOT substituted into the candidate during its fresh review. It has not received a separate independent full audit, and the accepted/final status of the reference route must be read from its own receipt. No improved-constant claim is made on the basis of this note.

## 3. Scope preserved

BK001 remains a histogram-only result at beta=1/M. BK002 uses full ordered words at beta=1/k^2 and a different stationary-mass family. The same-beta macrocycle barriers for BK001's family do not refute BK002: its escape scale is k*sqrt(beta)=1, so a bounded number of relevant macroevents and a constant no-escape likelihood cost are compatible with the budget. No claim of external novelty follows from discovering this witness; constrained-risk and contamination-adaptation themes have prior literature in other models.
