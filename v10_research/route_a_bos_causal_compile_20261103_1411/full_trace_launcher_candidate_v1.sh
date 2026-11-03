#!/usr/bin/env bash
# CANDIDATE ONLY: do not execute before independent source/launcher approval.
set -u
set -o noclobber
cd "$(dirname "$0")" || exit 90
for f in full_trace_cases_v1.jsonl full_trace_run_v1.log full_trace_stdout_v1.log full_trace_stderr_v1.log full_trace_launch_status_v1.log; do
  if [ -e "$f" ]; then printf 'Refusing to overwrite: %s\n' "$f" >&2; exit 91; fi
done
exec 3>full_trace_stdout_v1.log || exit 92
exec 4>full_trace_stderr_v1.log || exit 93
python full_trace_checker_candidate_v2.py >&3 2>&4
rc=$?
exec 3>&-
exec 4>&-
{
  printf 'command: python full_trace_checker_candidate_v2.py\nexit_status: %s\n' "$rc"
  printf '%s\n' 'sha256 values for source and created artifacts:'
  for f in full_trace_checker_candidate_v2.py full_trace_cases_v1.jsonl full_trace_run_v1.log full_trace_stdout_v1.log full_trace_stderr_v1.log; do
    if [ -f "$f" ]; then sha256sum "$f"; else printf 'MISSING %s\n' "$f"; fi
  done
} >full_trace_launch_status_v1.log || exit 94
exit "$rc"
