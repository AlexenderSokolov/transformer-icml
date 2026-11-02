# JP001 — Joint source corruption and one-shot port noise for a fixed uniform histogram prefix

2026-11-02. POST-STAGE8 author candidate; independent full review and root acceptance required. Accepted sources and frozen stage8 are unchanged.

## 1. Result and exact experiment

Fix K>=2, M>=64, 0<=k<=M integers, Q=2^h>=16 dyadic, and integer P>=h, D=2^P. Let 0<=delta<=1/4. The second-order source and hidden stationary certificate Pi obey P_source^2(s,t)>=beta Pi(t) on ALL pair states, beta in [0,1]. (P_source is distinct from the fractional-bit parameter P.) Observe X_1,...,X_(M+2); Y_j=(X_(j+1),X_(j+2)). Arbitrary initialization means any law of Y_0; stationary initialization means Pi. Loss is unconditional expected TV to theta_(Y_M), the actual protected terminal-pair row.

A source-independent randomized kernel changes at most k of positions 1,...,M before encoding and preserves the last two symbols. It may inspect the whole observed word. The fixed encoder is a paid radius-three exact local triple table, followed by zero-Q/K-logit uniform attention on keys 3,...,M+2. It exports the complete K^3 histogram. Its actual finite evaluator uses exact full-width accumulators and the FA001 common positive Taylor weight; at the terminal query its pre-port output is exactly

    a_abc = floor(D C'_abc/M)/D,                       (1)

where C' counts corrupted triples. There are no other numerical truncations after this quotient except exact coordinate copying. This is the BC001 uniform construction generalized from 8 to K^3 bits, not the original 9K+1 SRC master bank. Unlike FA001's approximation theorem, identity (1) needs only P>=h, not P=4h+C_arch.

A second, ONE-SHOT VECTOR attack adds eta to this bank, with |eta_abc|<=delta for EACH coordinate (an l-infinity ball), clips each coordinate to [0,1], and then applies floor(Q x)/Q. It may be history-adaptive and cooperate with source editing, but has no theta/Pi/initial-law/future input. It can read the actual bank. No attack mask or seed is revealed. The two kernels can be treated as one joint kernel with these sequential constraints; the upper is pathwise. “One-shot” does NOT mean at most one scalar may be changed. The latter model is not proved here.

ONLY the K^3 final labels, exact protected terminal pair and source-independent public metadata cross the cut. No original initial boundary, raw/corrupted history, counts, denominator, unquantized values, hidden states, or attack seed survive. Public metadata may include K,M,h,P,k, beta and a budget certificate below; no source-dependent number can be disguised as metadata. Decoder is arbitrary randomized real simplex-valued for the lower bound. The constructive upper is deterministic, beta-blind and finite rational. The encoder depends on neither k nor delta.

For implementability supply either rational delta with its full description paid, or a finite rational/dyadic certificate rho satisfying

    delta <= rho <= 2(delta+1/Q).                     (2)

The construction uses rho, not an oracle for an arbitrary real delta. Constants hold uniformly over any certificate obeying (2). The experiment may equivalently fix such a source-independent certificate as public input. Existence of a short dyadic certificate follows by rounding delta+1/Q upward to a dyadic scale; it is supplied, not inferred from noisy data. The lower allows arbitrary knowledge of these public numbers; they are fixed across every witness prior.

Put s=M^(-1/2), e=max(beta,1/M) for K>=3 and e=max(sqrt(beta),1/M) for K=2. Define f_e(0)=0 and

    f_e(x)=x[1+ln(1+1/(M e x))], x>0,
    tau=k/M+delta+1/Q, H=min(1,max(s,f_e(tau))).

Let c_U(K)>0 be the following accepted fixed-uniform-bank lower constant: for K=2 use BS001 §1's c with D_arch=8,r=3,kappa=1; for K>=3 use BF001 §1's c_F with D_arch=max(K^3,9K+1),r=3,a=1,b=6. Define

    c_K=min(c_U(K),2^-54,2^-15)/12,
    b_K=6+4K,
    L_K=2K^2(17+ln480)+10K^4,
    C_K=2^20(1+b_K)+2^13 K^(5/2)+b_K L_K.

These deliberately loose constants are finite, positive and depend only on K. Then

    c_K H <= R_stat <= R_all <= min(1,C_K H).         (JP1)

Here R is infimum over post-cut decoders and supremum over source laws and admissible joint attacks, for this ONE fixed prefix. This is not an optimized-encoder, architecture-universal, neural-depth-optimality, training, or sharp-growing-K claim. Both initialization risks are therefore Theta_K(H), uniformly in every listed parameter and admissible public certificate.

## 2. Exact evaluator and robust pathwise comparison

The local table stores K^3 indicator bits for the trailing triple, using public padding at positions 1,2. Use BC001's causal masks K_1={1}, K_2={1,2}, K_t={3,...,t} for 3<=t<=M+2, and K_(M+3)={3,...,M+2}. Density is at least 1/3. Historical tables never use a future boundary. Synthetic query state is zero; final-pair selection occurs only in the decoder. Zero Q/K maps, including dense zero slots, give equal scores. FA001's positive score shift yields the SAME positive Taylor integer W_* on every edge, even at arbitrary P>=h. With exact bit value V_i=D v_i, terminal accumulators are Z=M W_* and N_abc=W_* D C'_abc. Exact quotient gives (1). Identity padding and projections preserve it. Count guards and full products are essential.

Let z be the received grid bank and define rational pseudo-counts tilde C=M z. Clipping is 1-Lipschitz and fixes C'/M. Therefore

    |z_abc-C'_abc/M| <= delta+1/D+1/Q <= rho+2/Q.

Each symbol edit affects at most three triples, each with histogram l1 change <=2. Thus ||C'-C||_1<=6k for clean C, without a separation assumption on edit positions. For the selected K-coordinate row, preserved terminal pair gives

    ||tilde C_row-C_row||_1 <= B,
    B=6k+K M(rho+2/Q) <= b_K M tau.                  (3)

Every pseudo-count is nonnegative, even for attacks hitting the cube boundary. Clean C and clean row mass J are analysis variables, never decoder inputs.

### K>=3

Output (tilde C_row+1)/(tilde J+K). For nonnegative row vectors u,v with masses A,B'>0, insertion of v/A and |A-B'|<=||u-v||_1 gives TV(u/A,v/B')<=||u-v||_1/A. Consequently distance to clean add-one is <=min(1,B/(J+K)). Accepted R011/SC002 gives clean risk <=2^13 K^(5/2)s.

For every real A>0, IU001's stationary occupation bound and AU001's exact complete-suffix mixture give

    E_mu min(1,A/(J+K)) <= L_K f_e(A/M).             (4)

For clarity, the continuous-A and finite-domain completion is as follows. Write x=A/M. If x>=1 the left side is <=1<=f_e(x). If x<1 and beta>=1/M, let suffix length m=ceil(M/2), eta=(1-beta)^floor(M/4). IU gives stationary term <=2K^2 x[17+ln(1+480/(beta A))]. AU's ordinary-P residual term is <=eta Psi(2K^4 x). With t=M beta>=1,z=1/x>1, eta<=euler_e exp(-t/4), ln z<=ln(1+z/t)+ln t, and euler_e exp(-t/4)ln t<=4. Splitting z<2K^4 and its complement bounds the residual by 10K^4 f_e(x). The stationary term is <=2K^2(17+ln480)f_e(x). If beta<1/M, the universal occupation bound gives Psi(K^4 A/(M+1))<=K^4 x[1+ln(1+1/x)] by the same two scalar cases. This proves (4), including beta=0, without additive burn error. Thus (3), monotonicity and concavity below give risk <=2^13 K^(5/2)s+b_K L_K f_e(tau).

### K=2

Use SC003's fixed public orientation d(u)=complement of the first bit of u. Let tilde C_exit be that coordinate. For ALL budgets, including k=delta=0, output designated probability

    qhat=(tilde C_exit-B)_+/(tilde J+B+2),

with other probability 1-qhat. This is a valid rational simplex output, without a true-exit/minority/source test. Unlike SC003's exact-full-history implementation, the k=0 branch here still needs protection against grid loss.

SC003's pathwise algebra works unchanged for real nonnegative pseudo-counts. In detail D0=J+2, D1=tilde J+B+2 obey D1>=D0 and 0<=D1-D0<=2B. For n=(tilde C_exit-B)_+, 0<=n<=C_exit and 0<=C_exit-n<=2B. Hence 0<=C_exit/D0-n/D1<=4B/D0. With p=C_exit/J for J>0 and true public-oriented probability q,

    |qhat-q| <=2|p-q|+min(q,A/(J+2)), A=4B+2.        (5)

At J=0, n=0 and the second term equals q since A>=2, so the same bound with first term zero holds.

The accepted clean comparator in SC003 gives E 1{J>0}|p-q| <=8193 sqrt(32)s. BIF001 §3.4 (full support and beta>=M^-2), BAI003 v2's singleton-support bound imported in SC003 §4, and the universal weak-beta bound give, for THIS q and EVERY real A>=2,

    E min(q,A/(J+2)) <=4s+16672 f_e(A/M).            (6)

Indeed full support is exactly BIF's inequality. Singleton support costs <=256A/M+16/(M+2)<=264A/M. Weak beta uses Psi(16A/(M+1))<=16 f_(1/M)(A/M). Positive-beta support classification is exactly SC003/BIF, including unsupported starts and symbol exchange; no source-dependent estimator branch occurs.

Below we prove monotonicity, subadditivity and f_e(cx)<=c f_e(x) for c>=1. Also f_e(2/M)<=8s: since e>=1/M, ln(1+M/2)<=sqrt(2M) (integrate 1/(1+t)<=1/sqrt(t)), giving (2/M)[1+sqrt(2M)]<=8/sqrt(M). Therefore

    f_e(A/M)<=4b_K f_e(tau)+8s.

Combining (5),(6), the risk is <=[2*8193 sqrt32+4+8*16672]s+66688 b_K f_e(tau), dominated by the stated C_K max(s,f_e(tau)). Unit TV and C_K>=1 yield the upper in (JP1). The estimator is beta-blind; binary budget awareness is explicit.

## 3. Three independent lower witnesses, not summed risks

First, source editing with eta=0: any decoder behind this fixed bank can be simulated from the full corrupted word, including all public parameters and its own independent seed. Accepted SC002 (K>=3) and BT002 (K=2) therefore give R_stat >= c_E max(s,f_e(k/M)), with c_E=2^-15 or 2^-54 respectively; k=0 uses their clean floor. Extra public budgets are source-independent constants and do not invalidate their arbitrary-decoder lower. The original lower kernels are common across their unknown-parameter families.

Second, no editing and eta=0: nested floors give z=floor(Q C/M)/Q EXACTLY since Q divides D. The fixed histogram with only terminal pair is less informative than a legal member of the BF001 or BS001 larger family with extra first/last-three boundary symbols. BF's D_arch=max(K^3,9K+1) inclusion appends constant zeros when K=3; they carry no information and are a mathematical lower inclusion, not executed coordinates. Uniform weights 1 and indicator values are legal under its [1,6] envelope. BS uses kappa=1,D_arch=8. Their family minimax lower, hence every member's lower, gives

    R_stat >= c_U(K) max(s,f_e(1/Q)).                 (7)

FR001 by itself is NOT invoked for equality of interfaces: its 9K+1 SRC bank is different. BF/BS are the justified family inclusions. The finite evaluator's exact uniform labels establish membership without a rounding-error heuristic. P can be public and arbitrarily large; its only effect at zero noise disappears by nested floors.

Third, assume delta>=1/Q. Set Q_c=max(16, the least dyadic integer >=1/delta). Then Q_c<=Q, Q_c divides Q and D, and 1/Q_c<=delta. With identity source editing use the SINGLE common map

    a -> floor(Q_c a)/Q_c.

The coordinate perturbation is nonpositive of magnitude <1/Q_c<=delta, and the resulting vector stays in [0,1]. Fine-Q rounding fixes this Q_c grid. Most importantly, for integer count C,

    floor(Q_c floor(D C/M)/D)/Q_c
        = floor(Q_c C/M)/Q_c.                        (8)

The received cut is therefore EXACTLY the old fixed uniform Q_c bank, not a noisy approximation. The attack reads only a and public Q_c, not theta or the clean count. It is a legal source-independent joint attack with zero source edits. Apply (7) at Q_c. If delta<=1/16, then delta/2<1/Q_c<=delta, and f_e(delta)<=2f_e(1/Q_c). If delta>1/16, Q_c=16 and delta<=1/4 gives f_e(delta)<=4f_e(1/16). Thus R_stat >=(c_U/4)f_e(delta). If delta<1/Q, (7) already dominates this delta term by monotonicity.

Let c0=min(c_U,2^-54,2^-15). The preceding separate minimax inequalities imply R_stat >=(c0/4)max{s,f_e(k/M),f_e(delta),f_e(1/Q)}. No common worst source across the three witnesses is required. For a=1/(M e)>0, direct differentiation gives

    f'(x)=1+ln(1+a/x)-a/(x+a)>0,
    f''(x)=-a^2/[x(x+a)^2]<0.

The continuous value f(0)=0 follows from x ln(1/x)->0. Concavity gives f(cx)<=c f(x) for c>=1. Also f(x)/x decreases, which implies f(x+y)<=f(x)+f(y), including zero arguments. Hence f(tau)<=sum of its three component values<=3 max of them. We conclude R_stat >=c0 max(s,f(tau))/12 >=c_K H. Stationary sources are a subset of arbitrary starts under identical ports and attacks, completing (JP1).

The coarsening attack is itself rational on the finite input bank. Thus the same lower holds if shifts are restricted to (1/D)Z. In fact it also holds under the stronger restriction eta in (1/Q)Z: for each input coordinate set b=floor(Q a)/Q, c=floor(Q_c a)/Q_c, and use eta=c-b. Since Q_c divides Q, 0<=b-c<1/Q_c<=delta. Now a+eta=c+(a-b), with 0<=a-b<1/Q, so its final Q floor is exactly c. This perturbed value stays in [0,1]: if c<1 then c<=1-1/Q_c, and if c=1 then a=b=1. Hence clipping changes nothing. Identity (8) gives the same coarse experiment. This alternate attack only reads the actual bank and public grids, remains common across all sources, and its shifts are fine-grid rational. The upper allows arbitrary real perturbations. No result for at-most-one-coordinate noise is proved.

## 4. Complete finite paid realization and limitations

This is a compact finite evaluator plus rational decoder certificate, not a claim of fixed neural depth for bit arithmetic. Put n=M+3, d=K^3, ell=ceil(log2(n+K+2)). Width 2d plus paid local labels accommodates old indicator/output arrays. Local tables, every zero Q/K coefficient, value projections, public causal masks, padded slots, positions, synthetic query and exact endpoint acquisition are explicitly generated/read/stored. Fixed K permits constants depending on d and table size; no free singleton-copy heads are used. Public boundary acquisition exports ONLY two final symbols.

Use FA001's sequential multi-tape schedule with its SAME Taylor recurrence, at selected fractional P>=h, and w=O_K(P+ell+log(P+1)+log(U+F+2)), where U is actual supplied numerical-record count and F actual public mask/metadata bits. For explicit fixed-width layouts U=O_K(n^2), F=O_K(n^2+n ell). Descriptions have constant numerical bitlength but all indices and masks are paid. Generate/copy them in public nested-loop order at O_K((U+F)w^2) bitwork; retain Ub+UP+F bits as appropriate. All n tokens' QKV, all n^2 candidate edges/masks, Taylor steps even though common, products, count guards, quotients, updates and copies are executed/charged. Forward bitwork is O_K(n^2(P+1)w^2); rolling numerical arrays use O_K(nw); a safe total encoder peak is O_K(Ub+UP+F+n ell+nw+w^4+b+P), including finite code/control, descriptions, masks and simultaneous buffers. FA001's bounded-error theorem is not needed at smaller P: positivity and exact zero-score cancellation prove (1) directly.

The attack is an external channel, not a claimed reliable finite physical noise injector. Reading the resulting Q-grid labels and writing the cut costs their actual K^3(h+1) bits. A general real noise sample is not passed as a hidden real input to the constructive decoder. All subsequent reliable operations are exact rational arithmetic on grid labels, M,k,rho. Let b_rho count the FULL binary numerator and denominator lengths of the supplied fraction rho (not a compact denominator-exponent encoding), plus its sign/separators, and v=O_K(P+h+ell+b_rho+1), large enough for full products, unreduced common-denominator numerators and all temporary guards. Scan the K^3 labels, select the row using the exact endpoint, form tilde C, B, tilde J, subtract/compare/mux as appropriate, and serialize rational simplex coordinates with an explicit common denominator. School rational operations after cross multiplication cost O_K(v^2) bitwork per token, including copies/clears; finite arithmetic microcode/code storage may conservatively be charged O_K(v^4). Pay all-token decoding/outputs if realized at every token: O_K(n v^2+v^4) added work and O_K(nv+v^4) retained bits plus certificate input and actual intermediate buffers. Only the terminal decoder can access the attacked terminal bank; other token outputs have no route into it. The same public budget is harmless at other positions; no risk claim for those positions is needed.

At the cut disable access to all input/history/QKV/numerator/denominator and nonexported output tapes. Release or zero dead arrays with their full writes charged. Handoff conversion, allowed terminal-label copying and public budget reads are paid. Compose encoder and decoder costs by ADDING all simultaneously live data/code/certificate/output/work buffers and taking the maximum across generation, forward, handoff and cleanup phases; do not take minima of incompatible implementations. Isolation is an explicit abstract access contract, not an uncosted physical protection gadget.

Optional ordered-simplex Q rounding adds <=K/Q TV, dominated by K f_e(tau); add that term to the upper constant and pay divisions/serialization. Main (JP1) uses finite rational output, so no optional-output constant is hidden in C_K. A PURE expansion, if desired, separately pays depth O(T_bit), width O(S_bit), gates/holds O(T_bit S_bit), dense slots O(T_bit S_bit^2) and actual index/coefficient/generation costs; it does not preserve constant neural depth. No lower on these resource quantities is established.

The result joins three separately identified obstructions under one fixed finite cut. It does not say internal arithmetic error is arbitrary adversarial P-bit noise: zero-score evaluator error is exactly downward quantization and P>=h makes it disappear at the final noiseless label. The additional delta channel is explicitly a separate perturbation site. Edited terminal pairs, unknown budgets without certificate, online-only attacks, visible attack seeds/masks, single-coordinate sparsity, new pre-cut statistics and redesigned deep encoders are outside this theorem. Diagnostics and LLM review are not formal verification, external peer review, or novelty certification.
