from fractions import Fraction as F
from pathlib import Path
import json
states=['00','01','10','11'];data=[]
for word,a in [('00011011',F(1,4)),('00100111',F(3,4))]:
 p=[F(1,2)]*3+[a]; pi0=F(1)/(3+F(1,2)/(1-a)); pi=[pi0,pi0,pi0,F(1,2)*pi0/(1-a)]
 P=[[1-p[0],p[0],0,0],[0,0,1-p[1],p[1]],[1-p[2],p[2],0,0],[0,0,1-p[3],p[3]]]
 assert sum(pi)==1 and [sum(pi[i]*P[i][j] for i in range(4)) for j in range(4)]==pi
 J=[0]*4; C=[0]*4; path_prob=pi[states.index(word[:2])]; factors=[]
 for i in range(2,len(word)):
  s=states.index(word[i-2:i]); y=int(word[i]);J[s]+=1;C[s]+=y;factor=p[s] if y else 1-p[s];path_prob*=factor;factors.append({'context':states[s],'outcome':y,'probability':str(factor)})
 data.append({'word':word,'theta_11':str(a),'stationary_pi':list(map(str,pi)),'factors':factors,'trajectory_probability':str(path_prob),'terminal':word[-2:],'J':J,'C':C,'r':str(F(sum(C),sum(J))),'old_successor':[sum(C[:2]),sum(C[2:])],'recent_successor':[C[0]+C[2],C[1]+C[3]],'add_half_output':str((F(C[3])+F(1,2))/(J[3]+1))})
assert data[0]['trajectory_probability']=='9/1408' and data[1]['trajectory_probability']=='3/640'
assert data[0]['J']==data[1]['J']==[2,2,1,1] and data[0]['C']==[1,2,1,0] and data[1]['C']==[2,1,0,1]
assert data[0]['old_successor']==data[1]['old_successor']==[3,1] and data[0]['recent_successor']==data[1]['recent_successor']==[2,2]
assert data[0]['add_half_output']=='1/4' and data[1]['add_half_output']=='3/4'
bound=F(1,4)*min(F(data[0]['trajectory_probability']),F(data[1]['trajectory_probability']));assert bound==F(3,2560)
output={'cases':data,'equal_prior_lower':str(bound),'rng':False}
p=Path('two_worlds.json');p.write_text(json.dumps(output,indent=2)+'\n');print('PASS: independent exact rational derivation; full case records in two_worlds.json; bound',bound)
