"""Verify independently reviewed bindings and record root's actual authorization."""
import json, hashlib
from pathlib import Path
import experiment as e
P=Path(__file__).resolve().parent
review=P/'independent_review_20261103/REVIEW.md'
review_hashes=P/'independent_review_20261103/REVIEW_INPUT_HASHES.json'
checked=json.loads(review_hashes.read_text())['sha256'];current=e.review_inputs()
for key,h in checked.items():
 if current.get(key)!=h:raise RuntimeError(f'reviewed input changed or omitted: {key}')
# Six supporting enumeration documents/scripts were bound by the prior, root-reviewed pre-run seal.
previous=json.loads((P.parent/'rare_weight_ablation_20261103'/'PRE_RUN_HASHES.json').read_text())['files']
missing=set(current)-set(checked)
for key in missing:
 if previous.get(key)!=current[key]:raise RuntimeError(f'additional supporting input differs from previous seal: {key}')
if len(checked)!=12 or len(current)!=18 or len(missing)!=6:raise RuntimeError('unexpected binding coverage')
doc={'independent_review':'approved','root_permission':'approved','review_sha256':hashlib.sha256(review.read_bytes()).hexdigest(),'review_input_manifest_sha256':hashlib.sha256(review_hashes.read_bytes()).hexdigest(),'reviewed_direct_count':len(checked),'supporting_prior_seal_count':len(missing),'root_approval':'Root reviewed the independent review and design and approved sealing the exact reviewed inputs and running the six fixed follow-up fits.','files':current}
with (P/'REVIEW_AND_RUN_APPROVAL.json').open('x') as f:json.dump(doc,f,indent=2,sort_keys=True);f.write('\n')
print('All 12 independent-review inputs and all 6 additional prior-sealed supporting inputs match; marker created exclusively.')
