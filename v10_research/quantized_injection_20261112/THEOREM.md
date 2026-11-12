# Quantized information collapse of the audited injective scalar

2026-11-12. A theorem for one explicit representation, not a lower bound for all networks or a finite-precision execution theorem.

## Setup and inherited exact-real encoder

Fix 0<c<1/2, a=1-2c, N>=3. The stationary spin source has uniform initial pair and transition P_theta(x|u,v)=(1+theta uvx)/2, |theta|<=a. Let T=(X_(N-1),X_N). Use precisely the width-four, gain-two, epsilon-one, one-read PreLN encoder in fixed-c-bridge/BRIDGE_OBSTRUCTION.md:

 p_i=i/(N+1), v_i=2sqrt2/sqrt(3+p_i^2), gamma_i=2sqrt(2/3)*v_i*p_i,
 Z=exp(8/3)+sum_i exp(gamma_i), w_i=exp(gamma_i)*v_i/Z,
 A=sum_i w_i X_i.

Its parameters are fixed bounded coefficients; scores are bounded, |A|<2, 0<w_i<=W/N for W=2 exp(4). Exact A is injective by the existing Lindemann-Weierstrass proof. Nothing below proves a quantitative transcendence separation.

Fix a terminal-only, zero-centered nearest-grid quantizer Y=Delta floor(A/Delta+1/2), with 0<Delta<=1. The tie convention is fixed. Its number of attainable labels is at most M=floor(4/Delta)+2. Internal arithmetic is exact in this theorem; only the terminal representation is quantized. This is not rounding every intermediate network operation. No rescaling of A before quantization is allowed without charging its effect on Delta and the bounded-gain contract.

## Uniform source-average collapse

For this spin source E X_i=0 and E X_i X_(i+k)=0 unless k is divisible by 3, in which case it is theta^(2k/3). This follows from the independent innovation representation (or the known three-spin Ising correlations). Therefore, by 2|w_i w_j|<=w_i^2+w_j^2,

 E_theta A^2 <= C_c/N,
 C_c=W^2 (1+a^2)/(1-a^2).

Indeed the covariance Toeplitz absolute row sum is at most 1+2 sum_(r>=1) a^(2r), and sum_i w_i^2<=W^2/N. This loose constant is explicit and uniform in N and theta.

Let epsilon_theta=P_theta(Y!=0). The zero bin contains (-Delta/2,Delta/2), so Chebyshev gives epsilon_theta<=min(1,4 C_c/(N Delta^2)). Coupling (Y,T) with (0,T) on the same trajectory gives

 TV(Law_theta(Y,T), delta_0 times Uniform({-1,+1}^2)) <= epsilon_theta.

No conditional concentration given T is assumed. The endpoint pair has exactly the same uniform marginal for every theta. Hence

 TV(Law_h(Y,T),Law_(-h)(Y,T)) <= epsilon_h+epsilon_(-h)
                                          <=8 C_c/(N Delta^2),

with the trivial cap at one understood, for every fixed 0<h<=a.

For Delta=N^(-beta), 0<=beta<1/2, the two quantized observation laws merge in TV, even though their unquantized exact laws preserve full-history information. This is a coarse-bin theorem, not a claim at beta>=1/2. A quantizer whose boundary passes through zero need not collapse to ONE symbol; the centered-bin assumption is essential to this proof.

## Information and prediction-risk consequences

All entropies use base two. For actual epsilon_theta,

 I_theta(X;Y | T) <= H_theta(Y) <= h2(epsilon_theta)+epsilon_theta log2(M-1).

The bound follows by separating the zero-label event and maximizing entropy on the remaining labels. Thus if Delta=N^(-beta), beta<1/2, this conditional information is O_c(N^(2beta-1) log N), tending to zero (beta=0 is also covered). By contrast exact A has

 I_theta(X;A | T)=H_theta(X|T)=(N-2) h2((1+theta)/2),

because A is injective and the innovation vector is independent of the uniform terminal pair. The exact-real information is linear in N while this particular quantized observation loses it.

Under the equal prior theta in {-h,+h}, any measurable predictor q(Y,T) of the next-plus probability has average absolute risk at least

 (h/2) [1-TV(Law_h(Y,T),Law_(-h)(Y,T))]
 >= (h/2) [1-8 C_c/(N Delta^2)]_+.

Proof: for a common observed pair T, the two target probabilities (1+h T_1 T_2)/2 and (1-h T_1 T_2)/2 differ by h. Sum the two absolute losses on the common part of their observation measures; its mass is 1-TV. Randomized predictors obey the same bound by averaging. Hence the worst of the two risks has the same lower bound. This permits an arbitrary decoder after quantization, not only the original bounded head.

## Recovery resolution: necessary versus sufficient

At theta=0, X is uniform on 2^N words. Any whole-word decoder using (Y,T) succeeds with probability at most min(1,4M/2^N), because at most one word per label/pair can be guessed correctly; source-independent randomization cannot improve this maximum. Without T replace 4M by M. This counting result holds for any deterministic encoder into M labels, but concerns exact whole-word recovery, NOT next-token risk.

For Delta=2^(-p), p>=0, 4M<=2^(p+5), so whole-word success >=1-rho requires p>=N-5+log2(1-rho). This is a necessary linear resolution exponent for this bounded scalar grid, not a sufficient precision guarantee and not a general prediction lower bound.

Let g_N=min_(x!=x') |A(x)-A(x')|. Exact injectivity gives g_N>0 at each finite N. If Delta<g_N, the quantizer is injective; a lookup decoder then recovers the word. If an additive observation error is bounded by eta<g_N/2, nearest-codeword decoding also works. Pigeonholing the 2^N code points inside (-2,2) gives g_N<=4/(2^N-1). No explicit positive lower bound on g_N is supplied: linear p may be insufficient. Numerical distinctness cannot replace such a lower bound.

## Why this is not an architecture lower bound

The result quantizes one preselected encoder at one fixed scale and with one fixed grid origin. Another encoder may place a useful statistic at macroscopic scale; a charged O(log N)-bit statistic can have O(N^-1/2) estimation error without retaining the word. Fine-grid beta>=1/2 is unresolved here. Adaptive quantizers, rescaling gains, alternative representation channels, and intermediate rounding models require separate theorems. The raw whole-word counting bound does not imply a next-token risk lower bound. Conversely, exact A injection alone gives no useful decoder with bounded gain.

## Prior and novelty limits

Quantization and finite-alphabet information bounds are classical; see Gray and Neuhoff, Quantization, IEEE TIT 44(6), 2325-2383 (1998), DOI 10.1109/18.720541. A primary metadata/search record was checked; attempted university PDF retrieval failed, so no detailed theorem is attributed to that unread PDF. Merrill and Sabharwal, The Parallelism Tradeoff: Limitations of Log-Precision Transformers, TACL 2023, https://aclanthology.org/2023.tacl-1.31/ was read: its arithmetic/circuit simulation result has a different contract and does not imply the present terminal quantization claim. The source and covariance are prior three-spin Ising facts (Turban 2016, arXiv:1605.05199). The present proof uses elementary variance, entropy, counting and two-point decision bounds; no new general quantization method or established novelty is claimed.

check.py enumerates small source laws with binary64 encoder weights, verifies covariance and TV coupling numerically, and records measured entropy/risk quantities. It is not a certificate of transcendence, smallest gap, or large-N asymptotics. The conservative analytical risk constants are generally vacuous at these small sizes.
