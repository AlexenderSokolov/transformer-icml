from itertools import product, combinations
from fractions import Fraction
import gzip,json,sys
from collections import defaultdict

def scan(h,z,r,mode):
    T=len(h); q=1; w=(0,)*r; b=[0]* (3 if mode=='signed' else 4)
    for t,x in enumerate(z):
        a=w[-1] if r else 0; c=w[-2] if r==2 else 0
        if mode=='signed':
            inc=((2*t%5-2)*x+a-h[(t+2)%T], (1-2*x)*(t%3+1)+c, x-a+c)
            q=(q*2+x+a+t)%4
        else:
            aw=1+(t%2)+x; bw=1+a
            inc=(aw*(2*x-1), aw, bw*(x+a-1), bw)
            q=(q+x+t)%4
        b=[v+v2 for v,v2 in zip(b,inc)]; w=(w+(x,))[-r:] if r else ()
    return (q,w,tuple(b))

def increment(h,t,q,w,b,x,mode):
    r=len(w); T=len(h); a=w[-1] if r else 0; c=w[-2] if r==2 else 0
    if mode=='signed':
        inc=((2*t%5-2)*x+a-h[(t+2)%T], (1-2*x)*(t%3+1)+c, x-a+c)
        nq=(q*2+x+a+t)%4
    else:
        aw=1+(t%2)+x; bw=1+a
        inc=(aw*(2*x-1),aw,bw*(x+a-1),bw); nq=(q+x+t)%4
    return nq,((w+(x,))[-r:] if r else ()),tuple(v+v2 for v,v2 in zip(b,inc))

def utility(key,mode):
    q,w,b=key
    if mode=='signed':return Fraction(b[0]**2+2*b[1]-b[2]+q+sum(w),1+sum(abs(x) for x in b))
    n1,d1,n2,d2=b
    assert d1>0 and d2>0
    return Fraction(n1,2*d1)+Fraction(n2,4*d2)+q+sum(w)

out=sys.argv[1]; count=0; words=0; states=0
with open(out,'xb') as raw, gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as gz:
 def emit(o):gz.write((json.dumps(o,separators=(',',':'))+'\n').encode())
 for mode in ('signed','heads'):
  for r in (0,2):
   for M in range(1,6):
    for h in product((0,1),repeat=M+2):
     for k in range(M+1):
      d=3 if mode=='signed' else 4
      dp={(1,(0,)*r,(0,)*d):(0,())}
      for t in range(M+2):
       nxt={}
       for (q,w,b),(cost,pref) in dp.items():
        for x in ((0,1) if t<M else (h[t],)):
         c=cost+(t<M and x!=h[t])
         if c>k:continue
         key=increment(h,t,q,w,b,x,mode)
         if key not in nxt or c<nxt[key][0]:nxt[key]=(c,pref+(x,))
       dp=nxt
      brute={}; masks=[]
      for s in range(k+1):
       for mask in combinations(range(M),s):
        z=tuple(x^(i in mask) if i<M else x for i,x in enumerate(h)); key=scan(h,z,r,mode)
        if key not in brute or s<brute[key][0]:brute[key]=(s,z)
        masks.append((mask,z,key)); words+=1
      assert set(dp)==set(brute) and all(dp[x][0]==brute[x][0] for x in dp)
      for key,(cost,z) in dp.items():
       assert z[-2:]==h[-2:] and sum(x!=y for x,y in zip(z[:M],h[:M]))==cost<=k and scan(h,z,r,mode)==key
       if mode=='heads':
        prior=[0]+list(z[:-1]) if r else [0]*len(z)
        a=[1+t%2+x for t,x in enumerate(z)]; b=[1+p for p in prior]
        n1,d1,n2,d2=key[2]
        assert Fraction(n1,2*d1)==sum(Fraction(ai*(2*x-1),2) for ai,x in zip(a,z))/sum(a)
        assert Fraction(n2,4*d2)==sum(Fraction(bi*(x+p-1),4) for bi,x,p in zip(b,z,prior))/sum(b)
      assert max(map(lambda x:utility(x,mode),dp))==max(map(lambda x:utility(x,mode),brute))
      emit({'mode':mode,'r':r,'M':M,'h':h,'k':k,'masks':masks,'map':[(key,v[0],v[1]) for key,v in sorted(dp.items())]})
      count+=1;states+=len(dp)
print('cases',count,'mask_records',words,'terminal_keys',states,'PASS')
