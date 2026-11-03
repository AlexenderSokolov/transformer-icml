from itertools import product
import csv
for mode in ('buggy','corrected'):
    with open(mode+'_replay.tsv','x',newline='') as f:
        out=csv.writer(f,delimiter='\t')
        out.writerow(['N','path','terminal','J00','J01','J10','J11','C00','C01','C10','C11','C_first0','C_first1','C_second0','C_second1','previous_same_key','trigger'])
        stop=False
        for N in range(7,17 if mode=='buggy' else 19):
            seen={}
            for x in product((0,1),repeat=N):
                J=[0]*4;C=[0]*4
                for i in range(2,N):
                    s=2*x[i-2]+x[i-1];J[s]+=1;C[s]+=x[i]
                q=2*x[-2]+x[-1]
                marg=(C[0]+C[1],C[2]+C[3],C[0]+C[2],C[1]+C[3])
                key=(q,tuple(J),*marg)
                prev=seen.get(key)
                hit=prev is not None and (prev[1]!=C[q] if mode=='buggy' else prev[1][q]!=C[q])
                out.writerow([N,''.join(map(str,x)),q,*J,*C,*marg,'' if prev is None else ''.join(map(str,prev[0])),int(hit)])
                if hit:
                    print(mode,'N',N,'x',''.join(map(str,prev[0])),'y',''.join(map(str,x)),'q',q,'J',J,'C1',prev[1],'C2',C,'marg',marg)
                    stop=True;break
                seen[key]=(x,C[:])
            if stop:break
