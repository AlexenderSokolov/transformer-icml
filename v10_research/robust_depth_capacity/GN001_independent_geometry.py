#!/usr/bin/env python3
"""Independent exact-rational checks; finite diagnostics do not replace proof."""
from fractions import Fraction as F
from pathlib import Path
import json

def relu(x): return max(F(0),x)
def clip(x): return min(F(1),relu(x))
def tent(x): return 2*x-4*relu(x-F(1,2))
def ext(x): return tent(x)+4*relu(x-1)
def iterate(x,k):
    for _ in range(k): x=tent(x)
    return x

def fold(t,N,j):
    k=N.bit_length()-1; eta=F(1,2*N**(j-1)+2)
    v=iterate(ext(t+eta/(2*N)),k-1)
    return clip((v-eta/2)/(1-eta))
def stair(t,N,j):
    k=N.bit_length()-1; L=N**(j-1)
    a=iterate(t,k+1)
    b=iterate(ext(t+F(1,4*N)),k)
    z=relu(F(1,2)-b)
    for _ in range((j-1)*k): z=min(F(1),2*z)
    s=a/2+min(1-a,z)
    return t-s/N

def curve(t,N,j):
    if j==1:return (t,)
    return curve(fold(t,N,j),N,j-1)+(stair(t,N,j),)

def edges(N,j):
    if j==1:return [(F(0),F(1),(F(0),),(F(1),))]
    child=edges(N,j-1); eta=F(1,2*N**(j-1)+2); ans=[]
    for i in range(N):
        selected=child if i%2==0 else [(1-b,1-a,y,x) for a,b,x,y in reversed(child)]
        for a,b,x,y in selected:
            ans.append(((i+(1-eta)*a)/N,(i+(1-eta)*b)/N,x+(F(i,N),),y+(F(i,N),)))
        end=selected[-1][3]
        ans.append((F(i+1,N)-eta/N,F(i+1,N),end+(F(i,N),),end+(F(i+1,N),)))
    return ans

def dist2(x,y):return sum((a-b)**2 for a,b in zip(x,y))
def interp(x,y,r):return tuple(a+(b-a)*r for a,b in zip(x,y))
def segment_dist2(e,f):
    total=F(0)
    for a,b,c,d in zip(e[2],e[3],f[2],f[3]):
        lo,hi=sorted((a,b)); lo2,hi2=sorted((c,d))
        gap=max(F(0),lo-hi2,lo2-hi)
        total+=gap*gap
    return total

def main():
    reports=[]
    for N,J in [(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4),(8,2),(8,3),(16,2)]:
        phase=0
        for j in range(2,J+1):
            eta=F(1,2*N**(j-1)+2)
            phases={F(z,16) for z in range(17)}|{eta/2,1-eta,1-eta/2}
            for i in range(N):
                for r in phases:
                    t=(i+r)/N; v=min(F(1),r/(1-eta)); expected=v if i%2==0 else 1-v
                    assert fold(t,N,j)==expected,(N,j,i,r)
                    expected_s=F(i,N)+max(F(0),r-1+eta)/(N*eta)
                    assert stair(t,N,j)==expected_s
                    phase+=1
        es=edges(N,J); endpoints=[es[0][2]]+[e[3] for e in es]
        assert len(set(endpoints))==len(endpoints)
        assert es[0][0]==0 and es[-1][1]==1
        assert endpoints[0]==(F(0),)*J
        assert endpoints[-1]==(F(0),)*(J-1)+(F(1),)
        paircount=localcount=0
        minspeed=None
        for idx,e in enumerate(es):
            a,b,x,y=e
            assert b>a
            assert sum(xx!=yy for xx,yy in zip(x,y))==1
            speed=sum(abs(xx-yy) for xx,yy in zip(x,y))/(b-a)
            minspeed=speed if minspeed is None else min(minspeed,speed)
            assert speed>=N**(J-1)
            for r in [F(0),F(1,3),F(1,2),F(1)]:
                assert curve(a+(b-a)*r,N,J)==interp(x,y,r)
            if idx:
                prev=es[idx-1]; assert prev[1]==a and prev[3]==x
                assert sum((yy-xx)*(vv-uu) for xx,yy,uu,vv in zip(x,y,prev[2],prev[3]))==0
                for r in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
                    for s in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
                        t1=prev[0]+(prev[1]-prev[0])*r;t2=a+(b-a)*s
                        d2=dist2(interp(prev[2],prev[3],r),interp(x,y,s))
                        if d2<F(1,N*N):
                            assert (t2-t1)**2*N**(2*(J-1))<=2*d2
                            localcount+=1
            for f in es[:max(0,idx-1)]:
                assert segment_dist2(e,f)>=F(1,N*N)
                paircount+=1
        reports.append(dict(N=N,J=J,edges=len(es),phase_checks=phase,nonincident_pairs=paircount,local_inverse_checks=localcount,minimum_speed=str(minspeed),passed=True))
    out=dict(status='PASS',arithmetic='Python Fraction exact rational',scope='Finite geometry diagnostics only; independent of author implementation',cases=reports)
    target=Path(__file__).with_suffix('.json');target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
