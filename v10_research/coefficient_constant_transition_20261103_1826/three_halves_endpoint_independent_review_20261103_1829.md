# Independent analytic review: endpoint c=3/2

Reviewed `three_halves_endpoint_addendum_v1.html`, SHA-256 `0fd1ee653f8314403fc9db27f921d9816dc486364c42091af76587d5365e7cc0`, together with `constant_scale_transition_v1.html`, SHA-256 `2d8d6b8c668d1726cd16673b161f8c4a779f3889ea9f13dc0ccc1381ae0d27d0`. The four-block graph, dependent stationary source and Gaussian final-output estimate are as in the companion. This is an analytic review, not a numerical implementation or formal verification.

## Finding

The displayed endpoint score gaps, historical segment analysis, anchor limits, actual-terminal query, and expected risk 27/160 are correct under the stated assumptions. This fixes c=3/2 before the N limit and does not resolve c>3/2 or a varying c_N approaching that endpoint.

## Historical rows

With D=L+3/2, ζ=(3/2)r/D, the relevant switching positions are r1=D/3 and r2=D. Removing i<H, |r−r1|≤H, and i>L−H removes O(log L) rows. Remaining rows lie more than H from both switching positions. If i<D/6 then ζ<1/4 and the nearest-score gap is at least i/2≥H/2. Otherwise i≥D/6 and the runner-up gap is at least 3iH/D≥H/2. On sufficiently large L the winning key is a data key and the total other-key mass is at most Le^(−H/2)<1/4, so the original snap is exact. The two bands have relative lengths 1/3 and 2/3; their context pairs match the companion's unshifted and one-shifted cases. Stationary ergodic prefix differences give the four anchor constants p00=13/20, p01=1/2, p10=1/4, p11=2/5. The exceptional keys and BOS weights are negligible compared with Θ(N) good matches; soft nonmatches contribute at most Ne^(−N) after scaling.

## Terminal row and risk

At i=L, ζ_L=3/2−(15/4)/(L+3/2), which is strictly between 1/2 and 3/2 for L≥4, so shift 1 wins. The score gap to shift 2 is (L+3/2)(3−2ζ_L)=15/2; the gap to shift 0 is (L+3/2)(2ζ_L−1)=2L−9/2≥L/2. For any integer key at distance m≥2 from the winner, curvature ≥L and center distance ≤1/2 give gap ≥Lm(m−1). Summing the two tails gives S≤e^(−15/2)+e^(−L/2)+2e^(−2L)/(1−e^(−2L))<1/3. Hence wrong mass S/(1+S)<1/4. For N≥3 the winning key j=L−2 is data X_(N−2), giving query (X_(N−2),X_N). For N=2 the corresponding key is BOS; the draft correctly does not identify it with X₀.

The companion's fixed-window source calculation applies at α=1/3: (11−6α)/[32(2−α)]=27/160. The selected moving comparator need not converge itself; the model's L1 difference from it vanishes and stationarity fixes the true terminal-window law. Reverse triangle inequality and the uniform 168/sqrt(N+2) final softmax approximation therefore justify the claimed expected-TV limit.

Only source reads and SHA checks were performed. No tests, enumeration, simulations, source overwrites, or external writes were used.
