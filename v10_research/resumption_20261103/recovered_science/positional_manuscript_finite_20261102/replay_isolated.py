"""Copy hash-bound inputs into a fresh /tmp tree; never write accepted artifacts.
Run from the original workspace. --build additionally builds in the temporary copy.
"""
from pathlib import Path
import hashlib,json,shutil,tempfile,subprocess,sys
here=Path(__file__).resolve().parent;root=here.parents[1]
base=Path(tempfile.mkdtemp(prefix='finite-manuscript-replay-'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
deps=json.loads((here/'HANDOFF_DEPENDENCIES.json').read_text())
for rel,meta in deps.items():
 src=root/rel
 assert sha(src)==meta['sha256'],rel
 dst=base/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
new=base/here.relative_to(root)
for f in ['build_local.sh']:
 shutil.copyfile(here/f,new/f)
expected=(here/'reviews/integration/checks_results.json').read_bytes()
r=subprocess.run([sys.executable,str(new/'reviews/integration/checks.py')],cwd=base,capture_output=True,text=True)
(base/'replay.stdout.txt').write_text(r.stdout);(base/'replay.stderr.txt').write_text(r.stderr)
assert r.returncode==0,r.stderr
assert (new/'reviews/integration/checks_results.json').read_bytes()==expected
# The review's regenerated source_bindings is diagnostic output only: glob order
# may differ in this copy. It does not replace the accepted review binding.
result={'integration_results_byte_identical':True,'dependency_hashes_verified':len(deps),'isolated_root':str(base),'build_requested':'--build' in sys.argv}
if '--build' in sys.argv:
 with (base/'build.stdout.txt').open('w') as out:
  subprocess.run(['bash',str(new/'build_local.sh')],stdout=out,stderr=subprocess.STDOUT,check=True)
 result['build_succeeded']=True
 result['rebuilt_pdf_sha256']=sha(new/'build/main.pdf')
 # TeX timestamps/IDs may differ; rebuild PDF identity is not promised.
(base/'REPLAY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
