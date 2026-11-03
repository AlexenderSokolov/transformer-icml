# Current reproduction entry after scalar-extraction amendment

The current program and test_program.py include six tests. Run `python v10_research/finite_positional_attention_20261103/test_program.py` explicitly. Root reran all six on the final amended code in an isolated copy, plus the three independent check scripts; all passed. ROOT_REPLAY.json contains outputs and scope.

REPRODUCE.md, GREEN.log, MANIFEST.json and the original independent bindings.json are retained historical artifacts describing the five-test packed-word version. They are not silently relabeled as current. MANIFEST_SCALAR_REVISION.json and review_independent/AMENDMENT_BINDINGS.json bind the final scalar-extraction version and its actual before snapshots/diff. The original datapath is AST-identical; only the paid scalar extraction helper/test and its proof were added.

The original repository-wide unittest discovery found zero tests; it is not evidence of broader coverage. This evaluator checks exact arithmetic and indices, not trained-network performance or measured emitted-network resource counts. No formal or external peer review is claimed.
