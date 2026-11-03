#!/usr/bin/env python3
"""Independent explicit flip-mask oracle for the C++ DP, with complete test records."""
import itertools,json,math,pathlib,random,subprocess,sys
D=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(D.parent/'learned_position_pilot_20261103'))
import numpy as np
import pilot

def stats(z):
    m=len(z)-2;row=z[-2:];j=c=d=0
    for i in range(m):
        if z[i:i+2]==row:
            j+=1;c+=int(z[i+2]);d+=int(i<m//2)
    a=(c/j if j and 512*d>=j else int(row[0]));eps=1/math.sqrt(m)
    return j,c,d,(1-2*eps)*a+eps

def target(z):
    j,c,_,_=stats(z);return (c+1)/(j+2)

def ce(p,q):return -p*math.log(q)-(1-p)*math.log1p(-q)

def oracle(h,k):
    m=len(h)-2;p=target(h);best=-1;args=[]
    for n in range(k+1):
        for positions in itertools.combinations(range(m),n):
            z=list(h)
            for i in positions:z[i]='1' if z[i]=='0' else '0'
            z=''.join(z);v=ce(p,stats(z)[3])
            if v>best+1e-12:best=v;args=[z]
            elif abs(v-best)<=1e-12:args.append(z)
    return best,args

def run_dp(h,k):
    p=subprocess.run([str(D/'dp'),str(len(h)-2),str(k),h,'3000000','10'],capture_output=True,text=True,check=True)
    parts=p.stdout.strip().split(',')
    assert len(parts)==11,parts
    return dict(status=parts[0],wall_s=float(parts[1]),cpu_s=float(parts[2]),rss_kb=int(parts[3]),peak_states=int(parts[4]),nodes=int(parts[5]),objective=float(parts[6]),j=int(parts[7]),c=int(parts[8]),d=int(parts[9]),word=parts[10])

def validate(h,k,record):
    assert record['status']=='ok',record
    z=record['word'];m=len(h)-2
    assert len(z)==len(h) and z[m:]==h[m:] and sum(a!=b for a,b in zip(h[:m],z[:m]))<=k
    j,c,d,q=stats(z);assert (j,c,d)==(record['j'],record['c'],record['d'])
    assert abs(ce(target(h),q)-record['objective'])<1e-12
    word=np.array([[int(a) for a in z]],dtype=np.int8)
    ps=pilot.statistics(word);assert (j,c,d)==tuple(int(ps[x][0]) for x in ['J','C','D'])
    assert abs(q-float(ps['Q'][0]))<1e-12
    b0,args=oracle(h,k);assert abs(record['objective']-b0)<1e-12,(h,k,record,b0,args)
    clean=np.array([[int(a) for a in h]],dtype=np.int8)
    for family in ['training','heldout']:
        for proposal in pilot.proposals(clean,k,family)[:,0,:]:
            x=''.join(map(str,proposal));assert x[m:]==h[m:]
            assert sum(a!=b for a,b in zip(x[:m],h[:m]))<=k
            assert ce(target(h),stats(x)[3])<=b0+1e-12
    return dict(h=h,k=k,word=z,objective=record['objective'],oracle_best=b0,oracle_maximizer_count=len(args),status='pass')

def main():
    cases=[]
    for h in map(''.join,itertools.product('01',repeat=6)):
        for k in range(5):cases.append((h,k))
    rng=random.Random(20261103)
    for m in range(5,9):
        for _ in range(8):
            h=''.join(str(rng.randrange(2)) for _ in range(m+2))
            for k in range(4):cases.append((h,k))
    result=[]
    for h,k in cases:result.append(validate(h,k,run_dp(h,k)))
    with (D/'test_cases.jsonl').open('w') as f:
        for r in result:f.write(json.dumps(r,sort_keys=True)+'\n')
    print(json.dumps(dict(status='PASS',cases=len(result),exhaustive_M4=320,seeded_M5_to_M8=128)))
if __name__=='__main__':main()
