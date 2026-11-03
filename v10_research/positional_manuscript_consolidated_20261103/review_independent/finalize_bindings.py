"""Bind the reviewed final snapshot without modifying author or historical files."""
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
PAPER=HERE.parent
ROOT=HERE.parents[2]
OLD=ROOT/'v10_research/resumption_20261103/recovered_science/positional_manuscript_finite_20261102'
REC=ROOT/'resumption_20261103/remote_recovery/files'

def binding(p):
    b=p.read_bytes()
    return {'sha256':sha256(b).hexdigest(),'bytes':len(b)}

def read(p):return json.loads(p.read_text())
freeze=read(PAPER/'verification/SCIENTIFIC_SOURCE_FREEZE.json')
checks=read(HERE/'checks.json');build=read(HERE/'build_check.json')
assert checks['status']==build['status']=='PASS'
assert build['sources']==freeze['files']
for rel,h in freeze['files'].items():
    assert binding(PAPER/rel)['sha256']==h
    assert checks['checked_content'][str((PAPER/rel).relative_to(ROOT))]['sha256']==h
unchanged={}
for name in ['proofs_positive.tex','proofs_negative.tex','proofs_finite_horizon.tex']:
    src=OLD/'sections'/name;dst=PAPER/'sections'/name
    assert src.read_bytes()==dst.read_bytes()
    unchanged[name]={'byte_identical':True,'sha256':binding(src)['sha256'],'bytes':binding(src)['bytes'],'comparison_source':str(src.relative_to(ROOT))}
source=read(PAPER/'SOURCE_BINDINGS.json')['files']
for rel,x in source.items():assert binding(ROOT/rel)=={'sha256':x['sha256'],'bytes':x['bytes']},rel
comp=read(PAPER/'COMPANION_CONTEXT.json')
for rel,h in comp['source_sha256'].items():assert binding(REC/rel)['sha256']==h
extra=['v10_research/research_direction_review_20261103/REASSESSMENT.md']
extra += [str((REC/p).relative_to(ROOT)) for p in comp['source_sha256']]
# Verify the final PDF identity without claiming new page-image inspection.
pdf=binding(PAPER/'build/main.pdf')
assert pdf['sha256']=='6e3a3f2d836fd8e3a3fda0e4305f3dd290f3b3f23fe4113891f787e2c9576764'
assert pdf['bytes']==644513
support=['SOURCE_BINDINGS.json','CLAIM_TO_SOURCE.md','CLAIM_TO_SOURCE.json','PROVENANCE_RECONCILIATION.json','COMPANION_CONTEXT.md','COMPANION_CONTEXT.json','VALIDATION.json','verification/SCIENTIFIC_SOURCE_FREEZE.json','verification/FINAL_EDITORIAL_REBIND.json']
artifacts=[p for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='FINAL_BINDINGS.json']
local_names={'build_check_transcript.txt','build_check_final.log'}
for p in artifacts:
    s=p.read_text()
    forbidden=['/'+'/'.join(parts)+'/' for parts in [('workspace',),('home','agent'),('root',)]]
    assert not any(x in s for x in forbidden), p.name
final={
 'date':'2026-11-03',
 'decision':'PASS: no unresolved scientific or scope blocker in the exact reviewed snapshot',
 'review_type':'Independent LLM scientific/editorial audit; not formal verification, external peer review, or priority certification',
 'complete_scientific_sources_read':True,
 'source_directory':str(PAPER.relative_to(ROOT)),
 'scientific_files':{rel:binding(PAPER/rel) for rel in freeze['files']},
 'three_core_proofs':unchanged,
 'pdf':{'path':'build/main.pdf',**pdf,'pages':55,'review_scope':'Identity checked; independent clean-directory build passed; visual inspection belongs to the separate author review.'},
 'author_support_artifacts':{rel:binding(PAPER/rel) for rel in support},
 'historical_inputs_verified':{rel:{'sha256':x['sha256'],'bytes':x['bytes']} for rel,x in source.items()},
 'additional_inputs_read':{rel:binding(ROOT/rel) for rel in extra},
 'exact_original_public_pairs':checks['verified_original_export_pairs'],
 'review_artifacts':{p.name:binding(p) for p in artifacts if p.name not in local_names},
 'local_only_evidence':{p.name:binding(p) for p in artifacts if p.name in local_names},
 'publication_scope':'Exclude local_only_evidence files from public distribution. The final build JSON supplies host-path-free build status and scientific source bindings.',
 'verification_summary':{k:checks[k] for k in ['source_bindings_verified','claim_bindings_verified','companion_source_bindings_verified','finite_upper_pairs','finite_lower_large_cases','direct_bank_cases','exact_output_cases','canonical_fault_readouts','scalar_grid_extractions','all_token_suffix_cases','real_radius_pathwise_cases']},
 'limitations':['Finite tests are not exhaustive all-horizon proof verification.','External sources were read only to the stated citation-audit scopes.','No unchanged-original-byte claim for declared public exports.','No external writes, contacts, or source PDF redistribution.'],
 'self_binding_note':'This JSON excludes itself to avoid circular hashing.'
}
(HERE/'FINAL_BINDINGS.json').write_text(json.dumps(final,indent=2)+'\n')
print(json.dumps({'status':'PASS','final_bindings':binding(HERE/'FINAL_BINDINGS.json'),'scientific_sources':len(freeze['files']),'review_artifacts':len(artifacts),'core_byte_identity':True,'pages':55,'tex_warning_count':len(build['warnings'])},indent=2))
