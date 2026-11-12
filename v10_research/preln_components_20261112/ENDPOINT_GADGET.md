# Exact full-feature PreLN endpoint-to-target gadget

2026-11-12. Revised construction with mandatory final full-feature LayerNorm. The earlier no-final-LN draft is preserved as GADGET_NO_FINAL_LN_DRAFT.md and is NOT the current interface claim. Independent review identified that missing final normalization; this revision repairs it by preserving balanced constant-energy output lanes. This solves ONLY the last endpoint-gating step once a bounded estimator has been placed in the specified logit/padding representation. It does not compute that estimator from raw data, compile the entire robust relay through PreLN, or prove a resource frontier.

## 1. Inputs and costed representation

Fix c in (0,1/2), a=1-2c, K_c=log((1-c)/c), K=K_c+1, and LayerNorm epsilon>0. Given an estimate qhat_theta in [-a,a], let

    l=log((1+qhat_theta)/(1-qhat_theta)),
    r=sqrt(K²-l²).

Use the following width-13 terminal state, with coordinates numbered from zero:

    h=(l,-l,r,-r,x,-x,y,-y,A,-A,0,0,0), A=1.

Here x,y are the ACTUAL freely supplied endpoint spins. Coordinates 10,11 are reserved for a balanced parity pair, and coordinate 12 is an unused spare. The final output will overwrite the balanced original logit pair. The input has zero mean and constant squared norm 2K²+4+2A², independent of the estimate and endpoint signs.

This representation is an INPUT CONTRACT, not free computation: the upstream network must construct l and r (or their finite-table values for a quantized estimator), and preserve them to this accuracy. Their costs are not settled here. Because K>K_c, padding stays strictly positive and no square-root endpoint singularity is required. An initial full-vector representation error eta is explicitly allowed in the noise bound below.

No data-dependent parameter is installed. K,c,epsilon and all gadget weights are fixed independently of theta,N and the observed word. The supplied pair itself, not an already supplied parity bit, is enough.

## 2. PreLN and block convention

Each block has a full self-inclusive causal attention layer with output projection zero, followed by its attention-residual error e, then an ordinary one-hidden-layer ReLU PreLN FFN residual, then its error f. Thus at the terminal

    u=h+e,
    h_new=u+W2 ReLU(W1 LN_epsilon(u))+b2+f.

All 13 features participate in each LN: LN(u)=(u-mean(u)1)/sqrt(mean((u-mean(u)1)^2)+epsilon), gamma=1,beta=0. Attention may have all scores zero and all values zero; the error after its zero residual is still charged. The blocks' row-local weights are shared across rows. Only the terminal output is used.

## 3. Block 1: parity using TWO hidden ReLUs

Let sigma0=sqrt((2K²+4+2A²)/13+epsilon). The first hidden preactivations are

    LN(u)_4+LN(u)_6,  -LN(u)_4-LN(u)_6.

Their ReLU sum is |LN(u)_4+LN(u)_6|. Write

    g0 = sigma0*(ReLU(sum)+ReLU(-sum))-1

into coordinate 10, and -g0 into coordinate 11; all other FFN correction coordinates are zero. Equivalently W2 has identical columns with entries +sigma0 at row10 and -sigma0 at row11, and b2 has -1 at row10,+1 at row11.

On the clean contracted input, sigma0 is exactly its full-feature normalization scale, so g0=|x+y|-1=xy. The output becomes

    h1=(l,-l,r,-r,x,-x,y,-y,A,-A,xy,-xy,0).

It still has zero mean, now with constant squared norm 2K²+6+2A². No multiplication gate or parity oracle is assumed.

## 4. Block 2: conditional negation in balanced lanes using TWO ReLUs

Let sigma1=sqrt((2K²+6+2A²)/13+epsilon). Let t=LN(u)_0 and v=LN(u)_10. The hidden preactivations are

    -t-Kv, t-Kv.

The FFN correction to coordinate0 is

    d1=sigma1*(ReLU(-t-Kv)-ReLU(t-Kv)),

and coordinate1 receives -d1. All other correction coordinates are zero. On the clean input t=l/sigma1, v=xy/sigma1, and |l|<K. If xy=+1, both preactivations are negative, hence d1=0. If xy=-1, both are positive and d1=-2l. The residual therefore changes the original balanced logit pair (l,-l) into (lxy,-lxy).

The state remains zero-mean with the SAME squared norm 2K²+6+2A²: the logit magnitude has not changed, the original padding remains, and the endpoint/parity/anchor lanes are untouched. This is why no extra output-padding circuit is needed.

Apply the REQUIRED final LayerNorm over all 13 features, with epsilon_f>0, gamma=1,beta=0. Its clean scale is the fixed constant

    sigma_f=sqrt((2K²+6+2A²)/13+epsilon_f).

Use the ordinary affine head with logits (sigma_f*LN_final(h)_0,0). Its clean output is exactly

    sigmoid(l*xy)=(1+qhat_theta*xy)/2.

Thus the current gadget includes full-feature PreLN before BOTH standard one-hidden-layer FFNs AND full-feature final LN before the affine-softmax head. It uses two hidden units per FFN, width13, and two outer blocks. It still does not construct the required upstream estimate/logit/padding representation.

## 5. Arbitrary full-vector residual errors

Let ||e||_2,||f||_2<=delta at EACH of the four error sites. These errors can be fully adaptive and input-aware. Let the incoming state differ from its contracted representation by at most eta in Euclidean norm.

LayerNorm is globally 1/sqrt(epsilon)-Lipschitz for gamma=1. The first FFN correction is 2sigma0-Lipschitz as a function of its normalized input: the scalar absolute-sum has input Lipschitz sqrt(2), and the balanced two-coordinate output adds sqrt(2). For the second correction, W1 has norm sqrt(2)max(1,K) and W2 has norm 2sigma1, so 4sigma1 max(1,K) is a conservative Lipschitz bound (the product gives the slightly smaller 2sqrt(2)sigma1 max(1,K)). Hence the two complete residual-map Lipschitz constants are

    B0=1+2sigma0/sqrt(epsilon),
    B1=1+4sigma1 max(1,K)/sqrt(epsilon).

Successive full-state errors satisfy

    E1 <= B0*(eta+delta)+delta,
    E2 <= B1*(E1+delta)+delta.

The final full-LN/affine-softmax probability error is at most sigma_f*E2/(4sqrt(epsilon_f)): final LN is globally 1/sqrt(epsilon_f)-Lipschitz, the affine head has norm sigma_f, and sigmoid is 1/4-Lipschitz. This includes perturbations in anchors, padding, marker/endpoint, parity, logit and all other coordinates. There is no hidden assumption that errors preserve zero mean, constant norm, or balanced pairs. Those equalities are used only for the exact reference execution; the global Lipschitz comparison handles arbitrary perturbations.

For an upstream estimator with expected absolute parameter error e_stat, the actual source-average prediction risk is at most e_stat/2+sigma_f*E2/(4sqrt(epsilon_f)) (or use an expected eta bound and the same affine recurrence). No independence between the estimator and endpoint is needed. For any fixed epsilon,epsilon_f,c the gadget therefore tolerates a fixed positive delta for any prescribed fixed additional probability error, independently of N.

## 6. Explicit norms and remaining contracts

Block1 W1 has norm2, W2 has norm2sigma0, and bias norm sqrt(2). Block2 W1 has norm sqrt(2)max(1,K), W2 has norm 2sigma1, and zero bias. The hidden widths are 2 and2, state width13, and number of outer blocks2. The output head norm is sigma_f and its bias is zero. Final LN epsilon_f is explicitly charged. All constants depend only on c,epsilon,epsilon_f (and A=1), never N. Full-state output norms remain bounded by the displayed input bound plus bounded corrections and four bounded errors; LN outputs have norm at most sqrt(13).

The exact real coefficients l,r are state values supplied by the upstream computation; sigma0,sigma1,sigma_f,K are fixed architecture coefficients. If these are quantized, propagate that additional error separately. Hardware LN/ReLU/softmax arithmetic errors are not implied by the additive-residual model. There is no claim of exact target probabilities under noise.

The obstacle left is specific: compiling the estimator and stable relay into the logit/padding representation under mandatory PreLN, a fixed width/total-norm budget, and all intervening residual errors. Endpoint parity and final target formation themselves are no longer an unspecified step, provided that representation is attained.

## 7. Revision and test boundary

The original draft's direct affine head would have failed if a mandatory final LN were silently inserted: its appended scalar logit changed mean and variance. The revised paired-lane overwrite fixes that exact issue, not by dropping final LN or freezing its normalization. All clean norm calculations are exact algebra; arbitrary full-vector errors are controlled by the explicit Lipschitz recurrence instead of assuming normalization stays constant under noise. `check_endpoint.py` tests the CURRENT paired-lane/final-LN gadget; files named `no_final_ln_draft` retain the superseded diagnostic only.

For full-parameter norm accounting, each displayed gamma=1 LayerNorm also has gain-vector Euclidean norm sqrt(13), beta norm zero. This is a fixed cost here because width13 is fixed, but must be updated to sqrt(d) in a separate digital-input converter at growing width. The final head has Frobenius norm sigma_f, not one.
