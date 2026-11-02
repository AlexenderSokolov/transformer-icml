#!/usr/bin/env python3
"""Offline clean rebuild of both stage8 documents from pristine restored sources."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile,traceback,zipfile
from lxml import etree
from pypdf import PdfReader
P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('report',type=Path);ap.add_argument('--render-helper',type=Path,default=Path('$DOCUMENT_RENDER_HELPER'));a=ap.parse_args()
assert not a.report.resolve().is_relative_to(P.resolve()),'Report must be outside checksummed package'
D=Path(tempfile.mkdtemp(prefix='stage8-rebuild-'));T=D/'pristine';S=D/'rebuild';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
by={x['source_path']:x for x in json.loads((P/'SOURCE_RESTORATION_MAP.json').read_text())['files']}
out={'status':'RUNNING','work':str(D),'package_manifest_sha256':sha(P/'SOURCE_MANIFEST.json'),'commands':[],'binding_reconciliations':[]}
PYTHON=os.environ.get('CODEX_PRIMARY_RUNTIME_PYTHON',sys.executable)
def save():a.report.write_text(json.dumps(out,indent=2)+'\n')
def run(cmd,cwd=None):
 r=subprocess.run([str(x) for x in cmd],cwd=cwd,capture_output=True,text=True);out['commands'].append({'command':[str(x) for x in cmd],'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr});save();assert r.returncode==0,(cmd,r.stdout[-2000:],r.stderr[-2000:]);return r
try:
 run([sys.executable,P/'verify_package.py','--restore',T]);shutil.copytree(T,S)
 inputs=['v10_research/source_corruption_manuscript/'+x for x in ['corrupted_trajectories.tex','binary.tex','nonbinary_endpoint.tex','references.bib','build.sh']]+['v10_research/source_corruption_guide/'+x for x in ['guide_math_zh.md','guide_final_math_zh.md','build_guide.py','verify_guide.py']]
 before={p:sha(S/p) for p in inputs}
 for p,h in before.items():assert h==by[p]['export_sha256']==by[p]['source_sha256']
 m=S/'v10_research/source_corruption_manuscript';g=S/'v10_research/source_corruption_guide'
 for p in m.iterdir():
  if p.is_file() and p.suffix in ['.pdf','.bbl','.aux','.blg','.log','.out','.toc']:p.unlink()
 for dn in ['build','qa']:
  if (m/dn).exists():shutil.rmtree(m/dn)
 run(['bash',m/'build.sh'],S);print('English clean rebuild complete',flush=True)
 for p in [g/'Chinese-stage8-guide.docx',g/'Chinese-stage8-guide.pdf',g/'native_math.docx']:
  if p.exists():p.unlink()
 if (g/'render').exists():shutil.rmtree(g/'render')
 run([PYTHON,g/'build_guide.py'],S)
 assert a.render_helper.is_file(),'Document render helper unavailable; provide --render-helper'
 run([PYTHON,a.render_helper,g/'Chinese-stage8-guide.docx','--output_dir',g/'render','--emit_pdf'],S)
 shutil.copyfile(g/'render/Chinese-stage8-guide.pdf',g/'Chinese-stage8-guide.pdf');print('Chinese DOCX/PDF clean rebuild complete',flush=True)
 out['documents']=[]
 for tag,rel,want in [('english','v10_research/source_corruption_manuscript/corrupted_trajectories.pdf',27),('chinese','v10_research/source_corruption_guide/Chinese-stage8-guide.pdf',9)]:
  orig=T/rel;new=S/rel;aa=D/(tag+'-original');bb=D/(tag+'-rebuilt');aa.mkdir();bb.mkdir()
  run(['pdftoppm','-r','72','-png',orig,aa/'page']);run(['pdftoppm','-r','72','-png',new,bb/'page'])
  left=sorted(aa.glob('*.png'));right=sorted(bb.glob('*.png'));assert len(left)==len(right)==want
  pages=[{'page':int(p.stem.split('-')[-1]),'delivered_png_sha256':sha(p),'rebuilt_png_sha256':sha(q),'identical':p.read_bytes()==q.read_bytes()} for p,q in zip(left,right)]
  assert all(x['identical'] for x in pages),(tag,[x for x in pages if not x['identical']])
  ta=run(['pdftotext','-layout',orig,'-']).stdout;tb=run(['pdftotext','-layout',new,'-']).stdout;assert ta==tb
  assert len(PdfReader(orig).pages)==len(PdfReader(new).pages)==want
  out['documents'].append({'name':tag,'pages':want,'delivered_pdf_sha256':sha(orig),'rebuilt_pdf_sha256':sha(new),'all_page_pngs_identical':True,'layout_text_identical':True,'page_pngs':pages});print(tag,'all pages identical',flush=True)
 orig=T/'v10_research/source_corruption_guide/Chinese-stage8-guide.docx';new=g/'Chinese-stage8-guide.docx'
 with zipfile.ZipFile(new) as z:
  xml=etree.fromstring(z.read('word/document.xml'));eq=xml.xpath('//*[local-name()="oMath"]');assert len(eq)==93;assert not any(n.startswith('word/media/') for n in z.namelist());assert not xml.xpath('//*[local-name()="drawing"]')
  out['docx']={'delivered_sha256':sha(orig),'rebuilt_sha256':sha(new),'byte_identical':orig.read_bytes()==new.read_bytes(),'native_editable_OMML_objects':len(eq),'formula_images':0,'document_xml_sha256':hashlib.sha256(z.read('word/document.xml')).hexdigest()}
 assert out['docx']['byte_identical']
 # The unchanged native verifier consumes this review binding. Reconcile just its
 # original-to-export pointers, never its other unrelated administrative graph.
 name='v10_research/binary_source_corruption/SC003_independent_full_review_bindings.json';p=S/name;original=p.read_bytes();assert hashlib.sha256(original).hexdigest()==by[name]['export_sha256'];x=json.loads(original)
 for path,h in x['files'].items():
  r=by[path];assert h==r['source_sha256'];actual=sha(S/path);assert actual==r['export_sha256']
  if h!=actual:
   out['binding_reconciliations'].append({'script':'v10_research/source_corruption_guide/verify_guide.py','binding_file':name,'json_pointer':'/files/'+path.replace('~','~0').replace('/','~1'),'source_path':path,'original_sha256':h,'export_sha256':actual,'basis':'Exact declared routing-only export delta in this verifier disposable copy'});x['files'][path]=actual
 p.write_text(json.dumps(x,indent=2))
 run([PYTHON,g/'verify_guide.py'],S)
 for p,h in before.items():assert sha(S/p)==h,(p,'source/script changed')
 out['source_and_script_sha256_unchanged']=before;out['status']='PASS';out['scope']='Clean package-only source rebuild; every page raster/text identical. DOCX byte-identical with 93 native OMML objects. Only explicitly consumed original/export metadata pointers reconciled. Generated administrative verifier outputs stay disposable. Not fresh mathematical proof or substitute for root visual approval.';save();print(json.dumps({'status':'PASS','pages':36,'OMML':93,'report':str(a.report)}))
except Exception as e:
 out['status']='FAIL';out['error']=repr(e);out['traceback']=traceback.format_exc();save();raise
