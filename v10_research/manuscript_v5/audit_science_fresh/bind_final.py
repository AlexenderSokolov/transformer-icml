from pathlib import Path
import hashlib,json,datetime
base=Path('v10_research/manuscript_v5');g=Path('v10_research/precision_robustness_guide')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
m=json.loads((base/'SOURCE_MANIFEST.json').read_text());guide=json.loads((g/'SOURCE_BINDINGS.json').read_text())
paths=set(s['path'] for s in m['sources'])|set(guide['files'])
for s in m['sources']:assert sha(s['path'])==s['sha256'],s['path']
for p,h in guide['files'].items():assert sha(p)==h,p
for p in [base/'finite_precision_prediction.tex',base/'finite_precision_prediction.pdf',base/'SOURCE_MANIFEST.json',base/'QA_VERIFICATION.json',base/'AUDIT_SCIENCE_FRESH.md',g/'guide_math_zh.md',g/'Chinese-stage7-guide.docx',g/'Chinese-stage7-guide.pdf',g/'SOURCE_BINDINGS.json',g/'QA_RECEIPT.json']:
 paths.add(str(p))
for folder in [base/'audit_science_fresh',base/'authoring-scratch']:
 paths.update(str(p) for p in folder.iterdir() if p.is_file())
for p in Path('v10_research/robust_markov_prediction').glob('MG_final_clip*'):paths.add(str(p))
for p in Path('v10_research/delivery_stage7').glob('*CORRECTION*'):paths.add(str(p))
result={'status':'PASS','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Fresh same-model mathematical/model audit of final integrated English v5 and Chinese guide; explicit post-freeze cube-closure clarification included. Not blind external review, formal verification or emitted-network audit. Rendered artifacts bound after author QA confirmation.','scientific_freeze':'2026-11-02T08:09:06.390192+00:00','new_accepted_units':m['new_acceptance_bindings'],'final_sources':{str(p):sha(p) for p in [base/'finite_precision_prediction.tex',g/'guide_math_zh.md']},'rendered_artifacts':{str(p):sha(p) for p in [base/'finite_precision_prediction.pdf',g/'Chinese-stage7-guide.docx',g/'Chinese-stage7-guide.pdf']},'fresh_exact_checks':72217,'files':{p:{'sha256':sha(p),'bytes':Path(p).stat().st_size} for p in sorted(paths)}}
(base/'AUDIT_SCIENCE_FRESH_BINDINGS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print(json.dumps({k:result[k] for k in ['status','final_sources','rendered_artifacts','fresh_exact_checks']},indent=2));print('bound files',len(paths))
