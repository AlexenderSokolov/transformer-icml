from pathlib import Path
import hashlib,json,difflib
p=Path('v10_research/first_order_positional_probe'); r=p/'order_review'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
initial=json.loads((r/'initial_bindings.json').read_text())
before=p/'revisions/FOC001_before_initial_pair_repair.md'; after=p/'ORDER_ADAPTATION_CANDIDATE.md'; diff=p/'revisions/FOC001_initial_pair_repair.diff'
assert h(before)==initial[str(after)]['sha256']
expected=''.join(difflib.unified_diff(before.read_text().splitlines(keepends=True),after.read_text().splitlines(keepends=True),fromfile=before.name,tofile=after.name))
assert diff.read_text()==expected
assert 'g_M(k)=max(M^(-1/2),k/M)' in after.read_text()
for path,binding in initial.items():
 if path!=str(after): assert h(Path(path))==binding['sha256'],path
out={'status':'PASS','before_matches_initial_binding':True,'diff_matches_actual_bytes':True,'inherited_sources_unchanged':True,'corrected_candidate_sha256':h(after)}
(r/'repair_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
