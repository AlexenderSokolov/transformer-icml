"""REVIEW CANDIDATE: do not execute before independent checker sign-off.
Symbolic-ln2 powers-of-two backend; this does not test dyadic exp or framework floats.
Creates new output files only; case exceptions are retained rather than suppressed.
"""
import hashlib,itertools,json,math,sys,traceback
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPORT='79e81b718fbb89990d4a679fbd6fd5f1aec30a65e29ac8ddb9fb43cca5afec3a'
SCHEMA='5d2e0cc8b598e4c7d53ac7974a5bbdfc366fd7aeef5cd581ab0189cfd9f0e0d2'
LAYOUT='13e50cde5084938e28bf6cef2bcf5b639ab7954b2b16261884b214303f0fa1c4'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def J(x):
 if isinstance(x,F): return {'numerator':x.numerator,'denominator':x.denominator}
 if isinstance(x,list): return [J(v) for v in x]
 if isinstance(x,tuple): return [J(v) for v in x]
 if isinstance(x,dict): return {str(k):J(v) for k,v in x.items()}
 return x
def vec(v): return {'dimension':len(v),'entries':[[i,J(x)] for i,x in enumerate(v) if x]}
def project(mat,x,size):
 out=[F(0)]*size
 for r,c,w in mat: out[r]+=w*x[c]
 return out
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def relu(x): return max(F(0),x)
def case(index,N,ed,bits,checker_hash,partial):
 eta=F(1,ed); b=math.ceil(math.log2(N*ed)); c=math.ceil(math.log2(32*(N+1)))
 D=math.isqrt(N+32)+1
 if (D-1)**2>=N+33: D-=1
 assert D*D>=N+33 and (D-1)*(D-1)<N+33
 h=D*D; d=2*h; a=N+4
 states=[]
 for i in range(1,N+1):
  x=[F(0)]*d; x[0]=1; x[1]=bits[i-1]; x[2]=int(i>=3); x[3]=int(i==1); x[3+i]=1
  states.append(list(map(F,x)))
 Qm=[]; Km=[]; Vm=[(0,1,F(1))]
 for lag in (1,2):
  Qm.append([(r,3+(r+1+lag),F(D*c)) for r in range(N) if r+1+lag<=N])
  Km.append([(r,4+r,F(1)) for r in range(N)])
 Q2=[(r,a+6+r,F(D*b)) for r in range(4)]+[(4,0,F(D*(b+1)))]
 K2=[(r,a+2+r,F(1)) for r in range(4)]+[(4,3,F(1))]
 V2=[(0,a+10,F(1))]
 O1=[[(a,0,F(1))],[(a+1,0,F(1))]]; O2=[(a+11,0,F(1))]; OFFN=[(a+2+k,k,F(1)) for k in range(8)]+[(a+10,8,F(1))]
 matrices={'offn':OFFN,'o1_lag1':O1[0],'o1_lag2':O1[1],'o2':O2,'q1_lag1':Qm[0],'q1_lag2':Qm[1],'k1_lag1':Km[0],'k1_lag2':Km[1],'v1':Vm,'q2':Q2,'k2':K2,'v2':V2}
 rec={'schema':'one_hot_full_trace_v1','schema_sha256':SCHEMA,'layout_sha256':LAYOUT,'report_sha256':REPORT,'checker_sha256':checker_hash,'case_index':index,'N':N,'bits':''.join(map(str,bits)),'bit_vector':bits,'eta':eta,'b':b,'c':c,'D':D,'head_dim':h,'model_dim':d,'layout':{'one':0,'x':1,'v':2,'z':3,'positions':[4,N+3],'copy1':a,'copy2':a+1,'K':[a+2,a+5],'Q':[a+6,a+9],'Y':a+10,'output':a+11},'projection_maps':matrices,'input_states':[vec(x) for x in states], 'first_attention':[],'first_ffn':[],'second_attention':{},'oracle':{},'assertions':{}}
 partial.update(rec); rec=partial; checks=rec['assertions']; partial['failure_stage']='first_attention'
 for i in range(1,N+1):
  row=[]; copies=[]
  for li,lag in enumerate((1,2)):
   edges=[]; scores=[]; partial['partial_work']={'position':i,'lag':lag,'edges':edges}
   q=project(Qm[li],states[i-1],h); partial['partial_work']['Q_coefficient_ln2']=vec(q)
   for j in range(1,i+1):
    key=project(Km[li],states[j-1],h); val=project(Vm,states[j-1],1)[0]; rawdot=dot(q,key); score=rawdot/D
    if score.denominator!=1: raise ArithmeticError('noninteger symbolic score')
    scores.append(int(score)); edges.append({'j':j,'K':vec(key),'V':val,'dot_coefficient_ln2':rawdot,'score_coefficient_ln2':score})
   mx=max(scores); total=F(0); num=F(0)
   for e,k in zip(edges,scores):
    weight=F(2)**(k-mx); e.update({'row_max_coefficient_ln2':mx,'row_shift_coefficient_ln2':-mx,'centered_coefficient_ln2':k-mx,'weight':weight,'numerator_contribution':weight*e['V'],'denominator_contribution':weight}); num+=weight*e['V']; total+=weight
   cp=num/total; copies.append(cp); row.append({'lag':lag,'Q_coefficient_ln2':vec(q),'edges':edges,'numerator':num,'denominator':total,'output':cp})
   checks[f'copy_{i}_{lag}_normalization']=total==(1+F(i-1,2**c) if i-lag>=1 else i)
   checks[f'copy_{i}_{lag}_mask']= [e['j'] for e in edges]==list(range(1,i+1))
   checks[f'copy_{i}_{lag}_projection'] = all(e['score_coefficient_ln2']==(c if e['j']==i-lag else 0) and e['V']==bits[e['j']-1] for e in edges)
   if i-lag>=1: checks[f'copy_{i}_{lag}_margin']=abs(cp-bits[i-lag-1])<=F(1,32)
  pre=list(states[i-1]); residual=pre[:]; writes=[]
  for li,cp in enumerate(copies):
   head=[F(0)]*h; head[0]=cp; write=project(O1[li],head,d); writes.append(vec(write)); residual=[u+w for u,w in zip(residual,write)]
  states[i-1]=residual
  checks[f'attention_residual_{i}']=residual[a]==copies[0] and residual[a+1]==copies[1] and all(residual[k]==pre[k] for k in range(d) if k not in (a,a+1))
  rec['first_attention'].append({'i':i,'heads':row,'pre_residual_state':vec(pre),'output_projection_writes':writes,'post_attention_residual_state':vec(residual)})
 partial['failure_stage']='first_ffn'
 for i in range(1,N+1):
  x=states[i-1]; pre=list(x); v=x[2]; z=x[3]; gates=[]; ff_features=[]; partial['partial_work']={'position':i,'gates':gates,'pre_residual_state':vec(pre)}
  for typ in ('K','Q'):
   for k,(u,w) in enumerate(itertools.product((0,1),repeat=2)):
    f1=x[a+1] if typ=='K' else x[a]; f2=x[a] if typ=='K' else x[1]
    s1=f1 if u else 1-f1; s2=f2 if w else 1-f2; A=s1+s2
    p1=2*A+2*v-F(9,2); p2=2*A+2*v-F(11,2); h1=relu(p1); h2=relu(p2); out=h1-h2
    dst=(a+2 if typ=='K' else a+6)+k; ff_features.append(out)
    target=(bits[i-3],bits[i-2]) if typ=='K' and i>=3 else ((bits[i-2],bits[i-1]) if typ=='Q' and i>=3 else None)
    expected=int(target==(u,w)) if target is not None else 0
    checks[f'gate_{i}_{typ}_{u}{w}']=out==expected
    gates.append({'type':typ,'pattern':[u,w],'input_1':s1,'input_2':s2,'sum':A,'preactivation_1':p1,'preactivation_2':p2,'hinge_1':h1,'hinge_2':h2,'output':out,'oracle':expected,'destination':dst})
  y_hinge=relu(x[1]-z); y=y_hinge+z/2; ff_features.append(y); delta=project(OFFN,ff_features,d)
  states[i-1]=[u+w for u,w in zip(pre,delta)]; x=states[i-1]
  checks[f'ffn_residual_{i}']=all(x[k]==pre[k]+delta[k] for k in range(d))
  checks[f'value_{i}']=y==(F(1,2) if i==1 else bits[i-1]); checks[f'bit_retained_{i}']=x[1]==bits[i-1]
  rec['first_ffn'].append({'i':i,'gates':gates,'Y_input_x':x[1],'Y_z':z,'Y_hinge':y_hinge,'Y':y,'ffn_features':vec(ff_features),'pre_residual_state':vec(pre),'ffn_write':vec(delta),'post_residual_state':vec(x)})
 partial['failure_stage']='second_attention_and_oracle'
 edges=[]; scores=[]; partial['partial_work']={'edges':edges}; q=project(Q2,states[-1],h); partial['partial_work']['Q_coefficient_ln2']=vec(q)
 for j in range(1,N+1):
  key=project(K2,states[j-1],h); val=project(V2,states[j-1],1)[0]; rawdot=dot(q,key); score=rawdot/D
  if score.denominator!=1: raise ArithmeticError('noninteger second score')
  match=dot(states[-1][a+6:a+10],states[j-1][a+2:a+6]); scores.append(int(score)); edges.append({'j':j,'K':vec(key),'V':val,'first_flag':states[j-1][3],'match':match,'dot_coefficient_ln2':rawdot,'score_coefficient_ln2':score})
 mx=max(scores); num=F(0); total=F(0)
 for e,k in zip(edges,scores):
  weight=F(2)**(k-mx); e.update({'row_max_coefficient_ln2':mx,'row_shift_coefficient_ln2':-mx,'centered_coefficient_ln2':k-mx,'weight':weight,'numerator_contribution':weight*e['V'],'denominator_contribution':weight}); num+=weight*e['V']; total+=weight
 output=num/total; pre_second=list(states[-1]); head2=[F(0)]*h; head2[0]=output; write2=project(O2,head2,d)
 zero_head=[F(0)]*d; zero_ffn=[F(0)]*d
 states[-1]=[u+w+z+f for u,w,z,f in zip(pre_second,write2,zero_head,zero_ffn)]
 target=bits[-2:]; candidates=[]; Jcount=Ccount=0
 for j in range(3,N+1):
  pair=bits[j-3:j-1]; same=pair==target; value=bits[j-1]; candidates.append({'j':j,'pair':pair,'match':same,'value':value})
  if same: Jcount+=1; Ccount+=value
 baseline=F(Ccount+1,Jcount+2); error=abs(output-baseline); bound=F(N-1-Jcount,2**b*(Jcount+2)+N-1-Jcount)
 checks['output_simplex']=0<=output<=1 and output+(1-output)==1
 checks['second_mask']=[e['j'] for e in edges]==list(range(1,N+1))
 checks['second_projection']=all(e['score_coefficient_ln2']==b*e['match']+(b+1)*e['first_flag'] for e in edges)
 checks['second_normalization']=total==1+F(Jcount,2)+F(N-1-Jcount,2**(b+1))
 checks['second_residual_and_zero_components']=states[-1][a+11]==output and all(states[-1][k]==pre_second[k] for k in range(d) if k!=a+11) and not any(zero_head) and not any(zero_ffn)
 for e in edges:
  j=e['j']; expected_match=int(j>=3 and bits[j-3:j-1]==target)
  checks[f'oracle_edge_{j}']=e['match']==expected_match and e['score_coefficient_ln2']==b*expected_match+(b+1)*int(j==1)
 checks['independent_match_count']=sum(int(e['match']) for e in edges)==Jcount
 checks['error_contamination']=error<=bound; checks['error_eta']=bound<=F(N,2**(b+1))<=eta/2
 checks['n3_or_zero_count_recorded']=N!=3 or Jcount in (0,1)
 rec['second_attention']={'Q_coefficient_ln2':vec(q),'edges':edges,'numerator':num,'denominator':total,'output':output,'probabilities':[1-output,output],'pre_residual_state':vec(pre_second),'output_projection_write':vec(write2),'zero_head_write':vec(zero_head),'zero_ffn_write':vec(zero_ffn),'post_residual_state':vec(states[-1])}
 rec['oracle']={'target':target,'candidates':candidates,'J':Jcount,'C':Ccount,'add_one':baseline,'absolute_error':error,'contamination_bound':bound}
 checks['exception_free']=True; rec['passed']=all(checks.values()); rec['failure_stage']=None; rec['partial_work']=None; rec['stage_status']={'case_setup':'completed','first_attention':'completed','first_ffn':'completed','second_attention_and_oracle':'completed'}; return rec

def main():
 required={'no_bos_causal_compilation_reviewed_v4.html':REPORT,'full_trace_schema_candidate_v1.html':SCHEMA,'trace_layout_candidate_v1.html':LAYOUT}
 for file,expected in required.items():
  actual=sha(HERE/file)
  if actual!=expected: raise RuntimeError(f'source hash mismatch: {file} {actual} != {expected}')
 checker_hash=sha(Path(__file__)); output=HERE/'full_trace_cases_v1.jsonl'; log=HERE/'full_trace_run_v1.log'
 if output.exists() or log.exists(): raise FileExistsError('exclusive new output already exists')
 count=passed=failed=0; exceptions=[]; n3_count=zero_count=0
 with output.open('x') as out:
  for N in range(3,9):
   for ed in (4,32):
    for bits in itertools.product((0,1),repeat=N):
     count+=1
     partial={'schema':'one_hot_full_trace_v1','schema_sha256':SCHEMA,'layout_sha256':LAYOUT,'report_sha256':REPORT,'checker_sha256':checker_hash,'case_index':count,'N':N,'bits':''.join(map(str,bits)),'eta':F(1,ed),'b':math.ceil(math.log2(N*ed)),'c':math.ceil(math.log2(32*(N+1))),'assertions':{},'failure_stage':'case_setup'}
     try: r=case(count,N,ed,list(bits),checker_hash,partial)
     except Exception as exc:
      r=partial; r['passed']=False; r['assertions']['exception_free']=False; stages=['case_setup','first_attention','first_ffn','second_attention_and_oracle']; failed_stage=r.get('failure_stage','case_setup'); idx=stages.index(failed_stage); r['stage_status']={name:('completed' if k<idx else 'failed' if k==idx else 'not_run') for k,name in enumerate(stages)}
      for name in stages[idx:]: r['assertions']['stage_'+name]=False
      r['exception_type']=type(exc).__name__; r['exception_message']=str(exc); r['exception_traceback']=traceback.format_exc(); exceptions.append(count)
     if N==3: n3_count+=1
     if r.get('oracle',{}).get('J')==0: zero_count+=1
     out.write(json.dumps(J(r),separators=(',',':'))+'\n')
     if r.get('passed'): passed+=1
     else: failed+=1
 with log.open('x') as f:
  f.write(json.dumps({'schema_sha256':SCHEMA,'layout_sha256':LAYOUT,'report_sha256':REPORT,'checker_sha256':checker_hash,'records_sha256':sha(output),'intended':1008,'written':count,'passed':passed,'failed':failed,'exception_indices':exceptions,'N3_records':n3_count,'J_zero_completed_records':zero_count,'command':'python full_trace_checker_candidate_v5.py','scope':'symbolic-ln2 powers-of-two backend; not generic finite floating-point','status':'PASS' if (count==1008 and failed==0) else 'FAIL'},indent=2)+'\n')
 print(f'written={count} passed={passed} failed={failed}'); sys.exit(0 if count==1008 and failed==0 else 1)
if __name__=='__main__': main()
