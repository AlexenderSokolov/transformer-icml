#!/usr/bin/env bash
# CANDIDATE ONLY: do not execute before independent source/launcher approval.
set -u
set -o noclobber
cd "$(dirname "$0")" || { printf 'Cannot enter launcher directory.\n' >&2; exit 90; }
attempt=full_trace_attempt_v1
mkdir "$attempt" || { printf 'Cannot exclusively create attempt directory: %s\n' "$attempt" >&2; exit 91; }
exec 3>"$attempt/stdout.log" || { printf 'Cannot open stdout capture.\n' >&2; exit 92; }
exec 4>"$attempt/stderr.log" || { printf 'Cannot open stderr capture.\n' >&2; exit 93; }
printf 'command: python full_trace_checker_candidate_v5.py\n' >"$attempt/start.log" || { printf 'Cannot create start record.\n' >&4; exit 94; }
rc=0
for f in full_trace_cases_v1.jsonl full_trace_run_v1.log; do
  if [ -e "$f" ]; then printf 'Refusing to overwrite: %s\n' "$f" >&4; rc=95; fi
done
approved_checker=795823bb3aad9b96558a1ee09d29a32d2028a7d855aef75176e9f16862e82cdf
actual_checker=$(sha256sum full_trace_checker_candidate_v5.py 2>&4) || rc=97
actual_checker=${actual_checker%% *}
if [ "$rc" -eq 0 ] && [ "$actual_checker" != "$approved_checker" ]; then
 printf 'Refusing unreviewed checker hash: %s\n' "$actual_checker" >&4; rc=98
fi
if [ "$rc" -eq 0 ]; then python full_trace_checker_candidate_v5.py >&3 2>&4; rc=$?; fi
exec 3>&-
exec 4>&-
{
 printf 'command: python full_trace_checker_candidate_v5.py\nexit_status: %s\n' "$rc"
 for f in full_trace_launcher_candidate_v5.sh full_trace_checker_candidate_v5.py full_trace_cases_v1.jsonl full_trace_run_v1.log "$attempt/start.log" "$attempt/stdout.log" "$attempt/stderr.log"; do
  if [ -f "$f" ]; then sha256sum "$f"; else printf 'MISSING %s\n' "$f"; fi
 done
} >"$attempt/end.log" || { printf 'Cannot create end record.\n' >&2; exit 96; }
exit "$rc"
