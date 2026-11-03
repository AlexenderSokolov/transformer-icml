# KH004 exploration — constant crossing removes the sqrt(beta) variance loss (UNREVIEWED)

2026-11-02. Separate actual research; not a premise or revision of frozen KH003. No theorem accepted. The intended stronger result is a boundary-window obstruction r=o(M^(1/3)) at beta=1/M, versus KH003's r=o(M^(1/6)). No full-history or arbitrary local-encoder conclusion follows.

## Alternative clean family and exact candidate domain

Keep c=1/4096, beta in[1/M,1/16], T=floor1/(8beta), j in[J0,T]. Use

    x=ck/M, y=j/M, w=1-y-2x,
    a=ck/(2j), b=1/2, e=1/2, tau=x/(2w).

Stationary balances ya=xe, w tau=xb hold. Assume

    k<=T, k>=64/c,
    k^3>=2^22 M^2, k^2>=2^23 M,
    r>=2, r<=k/4,
    r c k/M<=1/16, 16r/(c k)<=1/16,
    J0=max{k,ceil(16 c r k)}<=T.

All probabilities are legal: a<=c/2, tau<=1/4, w>=3/4. For all-state P²>=beta Pi, the only nontrivial diagonal-target conditions are a/2>=beta w and tau/2>=beta y. Both reduce to ck>=4 beta j w<=1/2, implied by k>=64/c. Cross targets follow from tau/2=x/(4w)>=beta x, a/2=xM/(4j)>=2x>=beta x, and (1-tau)tau>=3x/8>=beta x. The remaining constant entries are >=1/4 or >=3/8, and the other00 self-loop entry >=9/16, above targets<=1/16. Also a>=2beta.

The full squared matrix is

    [(1-a)^2, (1-a)a, a/2,          a/2]
    [1/4,     1/4,     tau/2,       (1-tau)/2]
    [(1-a)/2, a/2,     1/4,         1/4]
    [tau/2,   tau/2,   (1-tau)tau,  (1-tau)^2].

A three-step atom into11 has mass at least a/4>=lambda=ck/(16j). For00,01,10,11 use respectively paths00->00->01->11,01->11->11->11,10->00->01->11,11->11->11->11. Generic binary reversal remains valid.

## Better concentration

Stationary subset count variance is <=7M Pi(D)/lambda. Couple reverse-start00 to a stationary path via the same three-step atom. Markov/Chebyshev with KH003's thresholds give

    P(sigma>k/32)<=1536j/(c k²),
    P(|J00(W)-j|>k/8)<=7168j²/(c k³),
    P(Jcross(W)>k/32)<=917504j/k².

Since lambda M/4>=ck/8 and k>=64/c, endpoint11 probability is at least w-1/8>=1/2. After conditioning and using j<=M/8, total failure is at most

    917504 M²/k³+1802240 M/k²
    <=7/32+55/256=111/256.

Thus the same corrected original count event G and fixed-null Hamming bound hold, now with k>>M^(2/3), not k>>M^(5/6).

## Late-window bound must change

The old crude bound r*b is useless when b=1/2. Instead every candidate last-window011 transition occurs at a departure index m>=M-r. Since r<=k/4<=M/32, m>=M/2, and floor(m/3)>=M/8. Mixing gives

    P_00(Y_m=01)<=x+alpha_m,
    alpha_m<=1/(1+lambda M/8)<=16/(ck).

The unconditional late-window failure on endpoint11 is at most

    (r/2)[x+16/(ck)].

Dividing by endpoint probability>=1/2 bounds it by

    rck/M+16r/(ck)<=1/8.

The original first-r-zero reverse-window failure after conditioning is <=2ra<=1/16 by j>=16crk. Thus total boundary failure is <=3/16<1/4. This retains genuine original-window conditioning; it is not an uncharged free prefix.

All KH003 subsequent probability, canonicalization, strict-window/output test and loss accounting therefore give the SAME candidate finite inequality

    R_null >=[(ck/(128M)-2S)log((T+1)/J0)]_+.

The true null remains the asymmetric first-order source with target beta; its full-word factors are unchanged. Known H2<=2k/M follows as before.

## Growing-window consequence if the proof is confirmed

At beta=1/M, suppose r=o(M^(1/3)). Let U=M/r, L=M^(2/3), k=floor(sqrt(U L)). Then k/L->infinity, k/U->0, r/k->0, and every finite condition eventually holds. In particular k³/M²->infinity, k²/M->infinity, rk/M->0 and r/k->0. Also k/sqrt(M)->infinity, J0/M->0 and T/M->1/8, so log(T/J0)->infinity.

A clean O(M^-1/2) guarantee would then force the same unbounded logarithmic excess for histogram plus first/last-r windows. This is a stronger METHOD RANGE, not a proved sharp boundary at M^(1/3). The new family and the near-terminal mixing argument require fresh full independent review before any acceptance.
