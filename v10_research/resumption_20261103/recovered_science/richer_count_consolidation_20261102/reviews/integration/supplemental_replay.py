"""Replay two separately checked annotations; never modify accepted artifacts."""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile

root = Path(__file__).resolve().parents[4]
d = root / 'v10_research/richer_count_consolidation_20261102'
validation = json.loads((d / 'SOURCE_VALIDATION.json').read_text())
count = 0
for item in validation['proof_receipt_bindings']:
    receipt = json.loads((root / 'v10_research/intake' / (item['unit'] + '_root_acceptance.json')).read_text())
    proof = root / item['path']
    matches = [value for key, value in receipt['artifacts'].items() if Path(key).name == proof.name]
    assert len(matches) == 1, item['unit']
    assert matches[0]['sha256'] == hashlib.sha256(proof.read_bytes()).hexdigest(), item['unit']
    count += 1
assert count == 4
with tempfile.TemporaryDirectory(prefix='richer-integration-replay-') as tmp:
    reconstructed = Path(tmp) / 'reconstructed_final.tex'
    reconstructed.write_bytes((d / 'revisions/main.before_integration_wording.tex').read_bytes())
    proc = subprocess.run(['patch', '--batch', '--fuzz=0', str(reconstructed), str(d / 'revisions/integration_wording.diff')], capture_output=True, text=True)
    assert proc.returncode == 0, (proc.stdout, proc.stderr)
    assert reconstructed.read_bytes() == (d / 'main.tex').read_bytes()
print(json.dumps({'direct_receipt_matches': count, 'actual_wording_diff_reconstructs_final': True}, indent=2))
