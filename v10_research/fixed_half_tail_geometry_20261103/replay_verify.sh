#!/usr/bin/env bash
# Replay entirely in a disposable, isolated workspace. Does not write historical artifacts.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
A=v10_research/fixed_half_tail_geometry_20261103
C=v10_research/readout_conditioning_calibration_20261103
L=v10_research/learned_position_pilot_20261103
T="$(mktemp -d "${TMPDIR:-/tmp}/fixed-half-replay.XXXXXXXX")"
trap 'rm -rf "$T"' EXIT
mkdir -p "$T/$A" "$T/$C/calibration_v1/checkpoints" "$T/$L"
cp "$ROOT/$A/analyze.py" "$ROOT/$A/verify.py" "$T/$A/"
cp "$ROOT/$C/calibration.py" "$T/$C/"
cp "$ROOT/$L/pilot.py" "$T/$L/"
cp "$ROOT/$C/calibration_v1/frozen_data.npz" "$ROOT/$C/calibration_v1/final_predictions.npz" "$T/$C/calibration_v1/"
cp "$ROOT/$C/calibration_v1/checkpoints/"half_count_scaled_*_step*.npz "$T/$C/calibration_v1/checkpoints/"
(
 cd "$T"
 OPENBLAS_NUM_THREADS=1 python "$A/analyze.py" > "$A/run.log"
 OPENBLAS_NUM_THREADS=1 python "$A/verify.py" > "$A/verify.log"
)
for f in RESULTS.json run.log verify.log; do
 cmp "$ROOT/$A/$f" "$T/$A/$f"
 printf 'PASS byte-for-byte replay: %s  ' "$f"
 sha256sum "$T/$A/$f" | cut -d' ' -f1
done
printf 'All replay writes occurred under the disposable directory; the directory was removed on exit.\n'
