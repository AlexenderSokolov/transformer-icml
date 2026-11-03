from pathlib import Path
from html import escape
import re
p=Path(__file__).parent;s=(p/'report_source.txt').read_text()
def repl(a,b):
 global s
 assert s.count(a)==1,(a[:60],s.count(a));s=s.replace(a,b)
repl('uniformly over its domain and, if randomized, for every seed in a common source-independent seed distribution.', 'uniformly over its domain and, if randomized, for every relevant seed. The seed is independent of the entire source path under each source and has a common distribution, or more generally its conditional law given S_N=00 must be identical for the two sources. Equal seed marginals without either condition are insufficient.')
repl('The larger of these two population errors is at least (1−Λ_qλ)/4. For each t,', 'Average this SUM over the common conditional seed law, then use max of the two expected losses ≥ half their sum; this gives (1−Λ_qλ)/4. Do not average a per-seed maximum and interchange max with expectation. For each t,')
repl('Average over the same seed law. The two conditional trajectory distributions need not be coupled', 'The two conditional trajectory distributions need not be coupled')
repl('An independent LLM review checked the sensitivity argument, norm algebra, population comparator and sharpened pooled-moment calculation. Their mathematical review is scoped, not independent formal verification or a complete validation workflow. check_population.py records all 90 exact-rational population cases and uses no randomness. It is a finite diagnostic, not proof of (3)–(8).', 'An independent LLM review checked the sensitivity argument, norm algebra, population comparator and sharpened pooled-moment calculation, and identified the seed-conditioning correction now incorporated in this v2. Its separate independent_sensitivity_review_v1.html binds the original v1 source; this v2 retains the correction as well as the original v1 and both clarification files. Their mathematical review is scoped, not formal verification or a complete validation workflow. check_population.py records all 90 exact-rational population cases; check_reverse_moments.py records eight exact rational reverse-chain moment checks. Neither uses randomness or proves (3)–(8).')
(p/'report_v2_source.txt').open('x').write(s)
parts=s.split('\n\n');h='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Route A sensitivity bottleneck v2</title><style>body{max-width:1050px;margin:2em auto;padding:0 1em;font:16px/1.6 system-ui;color:#17212b}h1,h2{color:#163d5b}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px/1.55 ui-monospace,monospace;background:#f3f6f9;padding:.8em;border-radius:5px}.warn{border-left:4px solid #b56a1c;padding:1em;background:#fff7e9}</style><body>'''
for i,part in enumerate(parts):
 lines=part.splitlines()
 if not lines:continue
 if i==0:h+='<h1>'+escape(lines[0])+' — v2</h1><p class="warn">'+escape(' '.join(lines[1:]))+'</p>'
 elif re.match(r'^\d+\. ',lines[0]):h+='<h2>'+escape(lines[0])+'</h2><pre>'+escape('\n'.join(lines[1:]))+'</pre>'
 else:h+='<pre>'+escape(part)+'</pre>'
h+='</body></html>'
(p/'sensitivity_bottleneck_v2.html').open('x').write(h)
print('PASS: v2 incorporates seed correction, preserves v1 and all addenda')
