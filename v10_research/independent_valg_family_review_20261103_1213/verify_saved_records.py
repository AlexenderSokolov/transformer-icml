#!/usr/bin/env python3
import json, itertools, hashlib
from fractions import Fraction as F
from pathlib import Path
source=Path('v10_research/rare_fast_mixing_family_audit_20261103_1211')
records=[json.loads(s) for s in (source/'cases_v2.jsonl').read_text().splitlines()]
assert len(records)==16
states=('00','01','10','11')
expected={(u,t,tp,N) for u,t,tp in [(F(1,100),F(1,4),F(3,4)),(F(1,5),F(1,4),F(3,4)),(F(249,1000),F(3,4),F(1,4)),(F(1,10000),F(1,2),F(9,16))] for N in (2,3,4,7)}
seen=set();count=0
for r in records:
 i=r['inputs']; u,t,tp,N=F(i['u']),F(i['t']),F(i['tp']),i['N']; seen.add((u,t,tp,N)); w=(1-u)/3; h=u*t/w; hp=u*tp/w
 pi=[u,w,w,w]; P=[[1-t,t,0,0],[0,0,F(1,2),F(1,2)],[h,1-h,0,0],[0,0,F(1,2),F(1,2)]]; Q=[[1-tp,tp,0,0],[0,0,F(1,2),F(1,2)],[hp,1-hp,0,0],[0,0,F(1,2),F(1,2)]]
 def prod(A,B):return [[sum(A[x][z]*B[z][y] for z in range(4)) for y in range(4)] for x in range(4)]
 R=[[pi[y]*P[y][x]/pi[x] for y in range(4)] for x in range(4)]
 for key,A in [('P',P),('P2',prod(P,P)),('reverse_P',R),('reverse_P2',prod(R,R))]: assert [[F(z) for z in row] for row in r[key]]==A
 assert list(map(F,r['pi']))==pi and F(r['h'])==h and F(r['hp'])==hp and F(i['w'])==w
 saved={x['word']:x for x in r['path_probabilities']}; assert len(saved)==2**N
 edge=[[F(0) for j in range(4)] for i in range(4)]; mass=qm=end=F(0)
 for b in itertools.product('01',repeat=N):
  bits=''.join(b); s=[states.index(bits[j:j+2]) for j in range(N-1)]; p=q=pi[s[0]]
  for x,y in zip(s,s[1:]):p*=P[x][y];q*=Q[x][y]
  z=saved[bits];assert F(z['P'])==p and F(z['Q'])==q and z['terminal']==bits[-2:]
  mass+=p;qm+=q;count+=1
  if bits[-2:]=='00':
   end+=p
   for x,y in zip(s,s[1:]):edge[x][y]+=p/u
 assert mass==qm==1 and end==u==F(r['terminal_00_probability']) and F(r['path_total'])==mass
 assert edge==[[F(z) for z in row] for row in r['conditional_forward_edge_counts']]
 occ=[sum(edge[x][y] for x in range(4)) for y in range(4)]
 assert occ==list(map(F,r['reverse_expected_occupation'])) and list(map(F,r['conditional_KL_coefficients']))==occ[:2]
 assert r['full_KL_coefficients']==[f'(N-2)*u={(N-2)*u}',f'(N-2)*w={(N-2)*w}'] and r['assertions']=='PASS'
assert seen==expected and count==624
assert (source/'cases_v1.jsonl').read_bytes()==(source/'cases_v2.jsonl').read_bytes()
print(f'PASS: {len(records)} distinct parameter cases, {count} exact paths independently recomputed; per-case P/Q probabilities, matrices, terminal mass, edge/occupation counts and KL coefficients verified. v1/v2 JSONL byte-identical; no randomness.')
for f in ('family_audit_report_v3.html','cases_v2.jsonl'):
 print('sha256',f,hashlib.sha256((source/f).read_bytes()).hexdigest())
