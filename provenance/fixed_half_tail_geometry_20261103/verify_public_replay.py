#!/usr/bin/env python3
"""Verify the published identities and rerun fixed-checkpoint diagnostics in temporary copies."""
from pathlib import Path
import hashlib,json,os,subprocess,tempfile,shutil,sys
if not __debug__:
    raise RuntimeError('Optimized Python is not supported; scientific assertions must remain active')
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
STAGE='v10_research/fixed_half_tail_geometry_20261103'
def require(ok,message):
    if not ok: raise RuntimeError(message)
def digest(b):return hashlib.sha256(b).hexdigest()
def safe_path(p):
    q=Path(p)
    require(not q.is_absolute() and '..' not in q.parts,'Unsafe repository-relative path')
    return q
inventory=json.loads((ROOT/'provenance/PUBLIC_INVENTORY.json').read_text())
rows={x['path']:x for x in inventory['files']}
mapping=json.loads((HERE/'SOURCE_EXPORT_MAP.json').read_text())
checks=json.loads((HERE/'PUBLICATION_SCOPE_AND_CHECKS.json').read_text())
inputs={x['path']:x['public']['sha256'] for x in mapping['files']}
inputs.update({x['path']:x['sha256'] for x in checks['exact_inherited_dependencies']})
for path in [str(Path(__file__).relative_to(ROOT)),str((HERE/'SOURCE_EXPORT_MAP.json').relative_to(ROOT)),str((HERE/'PUBLICATION_SCOPE_AND_CHECKS.json').relative_to(ROOT))]:
    data=(ROOT/safe_path(path)).read_bytes()
    require(path in rows and digest(data)==rows[path]['sha256'] and len(data)==rows[path]['bytes'],'Public metadata identity mismatch: '+path)
for path,sha in inputs.items():
    data=(ROOT/safe_path(path)).read_bytes()
    require(path in rows and sha==rows[path]['sha256'] and digest(data)==sha and len(data)==rows[path]['bytes'],'Public input identity mismatch: '+path)
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
with tempfile.TemporaryDirectory(prefix='public-fixed-half-replay-') as tmp:
    dest=Path(tmp)
    for path,sha in inputs.items():
        q=dest/safe_path(path);q.parent.mkdir(parents=True,exist_ok=True)
        q.write_bytes((ROOT/path).read_bytes());require(digest(q.read_bytes())==sha,'Copy identity mismatch')
    p=subprocess.run(['bash',STAGE+'/replay_verify.sh'],cwd=dest,env=env,capture_output=True)
    require(p.returncode==0,'Author isolated replay failed: '+p.stderr.decode(errors='replace'))
    print(p.stdout.decode(),end='')
    review=STAGE+'/review_independent/'
    for program,expected in [('independent_check.py','independent_output.txt'),('replay_analysis.py','analysis_output.txt')]:
        p=subprocess.run([sys.executable,review+program],cwd=dest,env=env,capture_output=True)
        require(p.returncode==0,'Independent replay failed: '+p.stderr.decode(errors='replace'))
        require(p.stdout==(ROOT/review/expected).read_bytes(),'Independent output differs: '+expected)
        print('PASS byte-for-byte independent output: '+expected)
    require((dest/review/'REPLAY_RESULTS.json').read_bytes()==(ROOT/review/'REPLAY_RESULTS.json').read_bytes(),'Independent replay JSON differs')
    print('PASS byte-for-byte independent replay JSON')
    p=subprocess.run([sys.executable,STAGE+'/interactive_probe_error.py'],cwd=dest,env=env,capture_output=True)
    require(p.returncode!=0 and b'UnboundLocalError' in p.stderr and b"local variable 'x'" in p.stderr,'Historical failed probe did not reproduce its expected failure')
    print('PASS historical probe reproduces expected UnboundLocalError; path-dependent stderr is not claimed byte-identical')
print('PASS verified '+str(len(inputs))+' public inputs; no training and no changes to repository sources/results')
