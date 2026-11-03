# Preservation disclosure and post-hoc endpoint reconstruction

3 November 2026. The earlier `conditional_bank_interval_certificate_20261103_0854/run_v2.log` records approximate decimal midpoints and pass/fail assertions about exact rational endpoint comparisons and widths. It did **not** retain the rational endpoints or other intermediate values at the time. The previous report's reference to exact rational comparisons describes what its script computed and asserted, not a contemporaneous record of all endpoints. The earlier files remain untouched.

The files in this new directory are a **post-hoc deterministic reconstruction**, not recovered original endpoint records. `reconstruct_endpoints_v2.py` copies the earlier script unchanged and appends output of each final exact rational lower and upper CE endpoint, interval width, and conservative gaps. `reconstruction_v2.log` is the new run's output. The parameters, exact integer arithmetic, and inputs are unchanged: N=50, outward grid 10^-30, M=2, clean 0000, k=1, target 1/4, and the weights described in the original report. No random data or model evaluation was performed. Exact agreement of the earlier and reconstructed endpoint values is an inference from deterministic execution of the same unchanged preceding code, not a claim that the missing earlier intermediate values were recorded. No NumPy/BLAS error bound follows from these results.

During preparation, the first copied file inherited read-only permissions; appending failed with `Permission denied`. The shell continued and ran the unchanged copied script, so `reconstruct_endpoints.py` and `reconstruction.log` contain no exact endpoint output. This terminal failure was not independently logged at the time; this sentence is the disclosure. Both files were sealed, and the successful reconstruction was produced separately as `reconstruct_endpoints_v2.py` and `reconstruction_v2.log`. The outputs and original source bindings are in `SHA256SUMS`.

Reproduce from workspace root:

  PYTHONDONTWRITEBYTECODE=1 python -B v10_research/bank_certificate_posthoc_endpoints_20261103_0857/reconstruct_endpoints_v2.py
