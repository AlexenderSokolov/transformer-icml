# Pilot implementation ledger

- Fixed exploratory protocol saved before unit-test sampling and main-run sampling. Its timestamp is a declared preparation timestamp; PRE_RUN_HASHES.json records the actual code/config seal time.
- Red test run: missing pilot module, retained in tests_red.log.
- Implemented simulator, posterior/controls, positional pooling, exact analytical gradients, Adam, and strict source-independent attack API.
- Green core run: 9 tests, maximum all-parameter finite-difference error 1.4411493217325252e-10, retained in tests_green.log.
- Implementation was kept separate from earlier frozen scientific files.
- Ruling: smoke uses rescanning candidate features, not the proposed incremental three-triple optimization. Exact rescans are simpler to audit; timing will determine whether optimization is necessary before any larger run.
- Ruling: the smoke uses only starts 00 and 11, three sources, one initialization and 200 steps. It explicitly cannot support the larger design's confirmation criteria or general-source conclusions.
