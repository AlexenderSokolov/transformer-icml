"""Replay finite diagnostics in temporary copies, leaving source files untouched.
This validates execution and exact expected output, not the probability proofs.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,shutil,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
OUT=HERE/'verification'; OUT.mkdir(exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
cases=[
 ('ACG001','v10_research/approximate_gate_statistics_20261103/review_independent',['check.py'],'check.py','checks.json'),
 ('PBP001','v10_research/positional_bank_precision_lower_20261103',['check.py'],'check.py','checks.json'),
 ('FPA001','v10_research/finite_positional_attention_20261103',['program.py','test_program.py'],'test_program.py',None),
]
def run(case):
 name,rel,files,entry,expected=case
 source=ROOT/rel
 before={f:sha(source/f) for f in files}
 with tempfile.TemporaryDirectory(prefix='v10-manuscript-replay-') as td:
  work=Path(td)/rel; work.mkdir(parents=True)
  for f in files: shutil.copyfile(source/f,work/f)
  r=subprocess.run([sys.executable,entry],cwd=work,text=True,capture_output=True)
  # Logs contain only output of the copied scripts, not host workspace paths.
  (OUT/(name+'_replay.log')).write_text(r.stdout+r.stderr)
  result={'unit':name,'exit_code':r.returncode,'sources_sha256':before,'source_files_unchanged':before=={f:sha(source/f) for f in files}}
  if expected and r.returncode==0:
   actual=(work/expected).read_text() if (work/expected).exists() else r.stdout
   same=json.loads(actual)==json.loads((source/expected).read_text())
   result['expected_report_semantically_equal']=same
   result['expected_report_sha256']=sha(source/expected)
   result['replayed_report_sha256']=hashlib.sha256(actual.encode()).hexdigest()
   assert same,result
  assert r.returncode==0 and result['source_files_unchanged'],result
  return result
with ThreadPoolExecutor(max_workers=3) as pool:
 results=list(pool.map(run,cases))
report={'status':'PASS_FINITE_DIAGNOSTICS_NOT_PROOF_VERIFICATION','cases':results}
(OUT/'REPLAY_RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
