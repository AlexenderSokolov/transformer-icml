from pathlib import Path
from html import escape
import re
p=Path(__file__).parent;s=(p/'report_source.txt').read_text();parts=s.split('\n\n')
h='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Route A sensitivity bottleneck</title><style>body{max-width:1050px;margin:2em auto;padding:0 1em;font:16px/1.6 system-ui;color:#17212b}h1,h2{color:#163d5b}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px/1.55 ui-monospace,monospace;background:#f3f6f9;padding:.8em;border-radius:5px}.warn{border-left:4px solid #b56a1c;padding:1em;background:#fff7e9}</style><body>'''
for i,part in enumerate(parts):
 lines=part.splitlines()
 if not lines:continue
 if i==0:h+='<h1>'+escape(lines[0])+'</h1><p class="warn">'+escape(' '.join(lines[1:]))+'</p>'
 elif re.match(r'^\d+\. ',lines[0]):h+='<h2>'+escape(lines[0])+'</h2><pre>'+escape('\n'.join(lines[1:]))+'</pre>'
 else:h+='<pre>'+escape(part)+'</pre>'
h+='</body></html>'
with (p/'sensitivity_bottleneck_v1.html').open('x') as f:f.write(h)
