from pathlib import Path
import json,hashlib,zipfile,re
from lxml import etree
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent
WORK=BASE.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
freeze_path=BASE/'delivery_stage7/SCIENTIFIC_FREEZE.json'
freeze=json.loads(freeze_path.read_text())
files={};accepted=[]
def bind(p,expected=None):
 assert p.is_file(),p
 digest=sha(p)
 if expected: assert digest==expected,(p,digest,expected)
 key=str(p.relative_to(WORK));files[key]=digest
 return digest
bind(freeze_path)
for u in freeze['new_units']+['GD001','FA001']:
 p=BASE/'intake'/f'{u}_acceptance.json'
 bind(p,freeze['receipts'].get(str(p.relative_to(WORK))))
 r=json.loads(p.read_text());bind(BASE/r['proof'],r['sha256'])
 for k in ('review','delta_review','revision_note'):
  if isinstance(r.get(k),str):bind(BASE/r[k])
 for f in r.get('reviews',[]):bind(BASE/f)
 for f,h in r.get('component_proofs',{}).items():bind(BASE/f,h)
 accepted.append({'unit':u,'proof':r['proof'],'sha256':r['sha256'],'accepted_utc':r['time_utc'],'scope':r.get('scope','')})
# Preserve the exact inherited stage-six closure and its already frozen source identities.
prior=BASE/'depth_initialization_guide/SOURCE_BINDINGS.json';bind(prior)
old=json.loads(prior.read_text())
for name,h in old['files'].items():bind(BASE/name,h)
for name in ['Chinese-stage6-guide.docx','Chinese-stage6-guide.pdf']:
 bind(BASE/'depth_initialization_guide'/name)
for name in ['analog_channel_comparison.md','folded_capacity_comparison.md','depth_companding_comparison.md']:
 bind(BASE/'prior_art'/name)
for p in (WORK/'v10_intake/source/sources/dot-return/readable/proofs').glob('R011_global_rates_and_constant_adaptation_v1.md'):bind(p)
bind(WORK/'v10_intake/source/sources/dot-return/readable/reviews/R011_independent_review_v1.md')
# Relevant predecessor source records cited by accepted units.
for folder in ['robust_markov_prediction','noise_precision_frontier','mixing_depth','folded_noise']:
 for p in (BASE/folder).glob('*source_bindings.json'):bind(p)
# Explicitly reviewed post-freeze implementation correction, not a twelfth unit.
cb=BASE/'robust_markov_prediction/MG_final_clip_clarification_review_binding.json'
corr=json.loads(cb.read_text());assert corr['status']=='PASS';bind(cb)
bind(BASE/'robust_markov_prediction/MG_final_clip_clarification.md',corr['clarification_sha256'])
bind(BASE/'robust_markov_prediction/MG_final_clip_clarification_independent_review.md',corr['review_sha256'])
manifest={'freeze_utc':freeze['scientific_freeze_utc'],'accepted_units':accepted,'files':dict(sorted(files.items())),'guide_source_sha256':sha(ROOT/'guide_math_zh.md'),'postfreeze_implementation_correction':{'note':'MG final pre-fault working-lattice clip; fixed stages and costs included, no new rate theorem','review_status':'PASS','binding':'robust_markov_prediction/MG_final_clip_clarification_review_binding.json'},'scope':'Stage7 exact accepted units plus unchanged stage6 predecessor closure and separately reviewed implementation correction. No postfreeze candidate rate used. Attribution notes are contextual, not proof dependencies.'}
(ROOT/'SOURCE_BINDINGS.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(ROOT/'Chinese-stage7-guide.docx') as z:
 x=etree.fromstring(z.read('word/document.xml'));ns={'m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
 eq=x.xpath('//m:oMath',namespaces=ns);txt=''.join(x.xpath('//*[local-name()="t"]/text()'))
 assert len(eq)>=145 and not x.xpath('//*[local-name()="drawing"]')
 assert not any(n.startswith('word/media/') for n in z.namelist())
 assert not any(t in txt for t in ['[[PAGE]]','/workspace/','/tmp/','ROOT_LEDGER','\\frac','\\rm'])
 assert not any(re.search('[\u3400-\u9fff]',''.join(e.itertext())) for e in eq)
reader=PdfReader(ROOT/'Chinese-stage7-guide.pdf');assert len(reader.pages)==11
texts=[p.extract_text() for p in reader.pages]
assert all(len(t)>400 for t in texts)
assert all('\ufffd' not in t for t in texts)
report={'status':'STRUCTURAL_AND_SOURCE_CHECKS_PASS','freeze_utc':manifest['freeze_utc'],'pages':len(reader.pages),'native_editable_OMML_objects':len(eq),'formula_images':0,'page_text_characters':[len(t) for t in texts],'source_receipt_hash_checks':'PASS','visual_review':{'status':'PENDING','required_pages':list(range(1,12))},'science_review':'Pending fresh independent guide audit','outputs':{n:sha(ROOT/n) for n in ['Chinese-stage7-guide.docx','Chinese-stage7-guide.pdf']},'build_inputs':{n:sha(ROOT/n) for n in ['guide_math_zh.md','guide_final_math_zh.md','build_guide.py','verify_guide.py']}}
(ROOT/'QA_RECEIPT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':len(reader.pages),'native_math':len(eq),'bound_sources':len(files),'checks':'PASS'},ensure_ascii=False))
