from pathlib import Path
p=Path(__file__).parent
old='an added uniform head plus finite decoder computes the same-prefix add-one statistic'
new='an added uniform head plus the ideal rational decoder computes the same-prefix add-one statistic exactly, and the finite-K ReLU spline approximates it with error bound (2)'
for source,target in [('consolidated_v2_source.txt','consolidated_v3_source.txt'),('route_a_terminal_report_v2.html','route_a_terminal_report_v3.html')]:
 data=(p/source).read_text();assert data.count(old)==1,(source,data.count(old));data=data.replace(old,new).replace('consolidated v2','consolidated v3')
 (p/target).open('x').write(data)
print('PASS: one clarified sentence in each artifact; v1/v2 preserved')
