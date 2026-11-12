# Independent review: gain-two conversion and paired scratch reset

Date: 2026-11-12. Verdict: PASS for the stated conversion and clean paired-reset components, with conditional noise scope retained. These are two separately checked claims; neither certifies a sequential statistical estimator.

## Reviewed versions

RESULT.md SHA256 bb30daf8f90c4c5f81ea057681c1bcac4d9536759de78a5c19503b957a61b295

GAIN2_PATCH.md SHA256 6f063bfc1a41cde5a64d6e134f073bb3b15722a1a89a102006adb02127af3a05

check.py SHA256 3f95d6b6cab0b7bd7b1c4869a4dc9c27eb6e29954b788f72419e00004f80e0a8

results.json SHA256 73a69d547dd375f8fa4c906b71a24dde049dd9d25161580c1b6f7b4fc5fcbabb

gain2_results.json SHA256 2c1362a245665cb151f655aca482085f0c60a4cd75bab2a5ed0d366fed8a129d

RECEIPT.json SHA256 38973863e736c15c69dd2d837a4572b81c995872e1d464d3df9d132456c2de48

## A. Gain conversion

With unchanged epsilon and zero shift, LN2(h)=2LN1(h) for every physical state, including noncentered/noisy states. Every affine consumer must be rescaled: (W/2)LN2(h)+b=W LN1(h)+b. The correction includes Q and K separately if nonzero, as well as V, FFN first matrices and final normalized readout. Biases, second FFN matrices, attention output projection, residual identity and embeddings stay unchanged. Thus attention scores/values, residual updates and outputs agree layer by layer. The reset functional coefficient becomes minus 1/2, not minus 1. All LN gain-vector squared norms increase by 3d per occurrence; a numerical cap or aggregate budget requires separate accounting. This algebra is exact, not limited to a data distribution.

I independently replayed the complete scalar-position diagnostic in memory after replacing the LN function by twice its output, halving every actual normalized consumer, and replacing the final 5*LN(v) by 2.5*LN2(v). Q,K remain zero. All 105 configurations and 27,540 gate/alignment assertions passed. Every non-timing result field, including all per-case records, was identical to the frozen gain-one results. This additional replay is distinct from the author's 300 random affine-consumer identity checks. It did not overwrite historical scripts or results. The precise in-memory source transformation was: change `return [(x-mu)/d for x in h]` to `return [2*((x-mu)/d) for x in h]`; change every `z=ln(h)` to `z=[v/2 for v in ln(h)]`; change the payload value list to `ln(h)[10]/2`; change `out=5*ln(h)[12]` to `out=2.5*ln(h)[12]`; omit only final persistence calls. Gain conversion does not turn the bit readout into a probability-softmax head.

## B. Clean reset derivation and implementation

At width 2m, opposite-coordinate pairs imply mean zero and d^2=C+||w||^2/m, C=1+sum(nonscratch scalar squares)/m>=1. A paired output correction minus the selected normalized first coordinate and plus it in the second coordinate gives T_C(w)=(1-1/d)w while every nonscratch physical coordinate remains unchanged. A literal ReLU realization uses 2k hidden units for k scratch pairs, with first matrix Frobenius sqrt(2k), second matrix 2sqrt(k), zero biases. Thus fixed k has constant layerwise norms; no inverse or free coordinate overwrite is assumed.

On a fixed-C convex scratch ball inside the common H envelope, d<=D=sqrt(1+H^2/(2m)). The Jacobian is (1-1/d)I+ww^T/(m d^3). Its tangential eigenvalue is 1-1/d and its radial eigenvalue 1-C/d^3. Since C>=1 and d>=1, both are nonnegative and at most 1-D^-3=q<1. Therefore ||T_C(w)||<=q||w||, and full paired scratch norm after L steps is at most q^L H. The nonscratch component of the ideal target is unchanged, so this equals full-state reset error. The stated logarithmic L suffices when epsilon<H; zero steps suffice when epsilon>=H. H=0 is handled explicitly rather than applying log q. Different rows may have different C, and the weights do not need C, but held nonscratch coordinates and hence C are fixed during each clean reset.

## C. Noise and scope

The revised manuscript now explicitly requires a common H covering the actual perturbed states before and after every update, or a separately proved invariant ball. Initial clean H alone is insufficient. Under this hypothesis, paired scratch-only perturbations of full norm delta per block give q^L H+delta/(1-q). If the execution model perturbs both residual sites, their combined effect must be charged; the per-block wording does not automatically give the same delta for two independent sites. Errors in retained lanes are not corrected. Arbitrary full-vector errors may break pairing, so the paired contraction theorem is not a full-state contraction for them. A uniform common-mode shift is invisible to LN and persists; the implementation does not solve physical mean drift. No stability of a persistent numerical accumulator follows from the reset lemma.

The revision correctly calls p in the generic bound an absolute-error-radius exponent. Interpreting it as fractional bits additionally requires a specified arithmetic scheme and certified local errors, with range and coefficient costs charged. The proposed O(N log(N/eta)) sequential schedule is conditional on further compilation and stability assumptions, explicitly unproved here. The root-N statistical formula assumes access to a correctly computed innovation estimate and endpoint product; it is not the output of an executed Transformer in this unit.

## D. Numerical evidence and limits

I independently ran the unchanged check.py. It passed 180 cases, 80 reset steps per case and 57,601 assertions, including exact preservation of held coordinates and mean-zero clean pairing. Maximum final scratch norm was 3.875848235205616e-62. This matches the saved diagnostic. The common-mode check deliberately demonstrates an unremoved mean, not robustness to arbitrary errors. These are binary64 finite tests of the reset component; no sequential predictor, risk experiment, noisy-state invariant-ball certificate, training, novelty or formal verification is claimed.

## Conclusion

Gain conversion and the clean paired scratch reset are valid, bounded-size components. The literal mother gain-2 convention can be met by the explicit rescaling. The reset preserves held physical lanes in exact clean arithmetic and contracts scratch uniformly on the declared ball. It does not supply arbitrary-noise physical reset, accumulator stability, simultaneous predecessor alignment, an ordinary final probability head or a matching end-to-end statistical upper bound.
