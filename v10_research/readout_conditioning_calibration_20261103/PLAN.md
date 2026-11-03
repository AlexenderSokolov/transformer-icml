# Bounded supervised readout calibration

Root approved the unchanged PROPOSAL.md. Work only in this new directory. Preserve the design, original smoke, source code and report amendment.

1. Write tests and observe missing-module failure, without drawing data.
2. Implement literal teacher, independent feature decoder, fixed-feature readout and scaled gradient, plus nine-fit runner.
3. Seal code/config/upstream hashes before any calibration sampling. Run checks before fitting: exact collision indices/counts, oracle identity, matched initialization, all readout gradients and count-only floor.
4. Draw/freeze the two datasets and shared minibatch sequence only after static checks. Verify oracle and matched initialization on all fixed words before fitting.
5. Execute exactly the nine approved fits; retain all declared checkpoints, per-update diagnostics and stratum metrics. Stop on failed checks or after the fixed budget. No attacks and no publication.
6. Deliver source-bound results for root replay/independent review; separate target fitting, conditioning evidence, and unsupported natural robustness claims.
