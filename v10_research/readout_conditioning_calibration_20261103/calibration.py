"""Supervised fixed-half readout calibration. No attacks and no learned pooling."""
import sys
from pathlib import Path
import numpy as np
UPSTREAM=Path(__file__).resolve().parent.parent/'learned_position_pilot_20261103'
sys.path.insert(0,str(UPSTREAM))
import pilot
M=64
SCALE=np.array([64,64,32,32,32,32,1,1,1],dtype=np.float64)

def collision_words(r1=8,r2=54):
    words=[]
    for r in [r1,r2]:
        if not 2<=r<=60:raise ValueError('r outside collision family')
        words.append(np.array([0]+[1]*r+[0,0]+[1]*(62-r)+[0],dtype=np.int8))
    return np.stack(words+[1-w for w in words])

def literal_statistics(words):
    """Independent list-path count/target oracle; no pilot count helper is called."""
    w=np.asarray(words)
    if w.ndim!=2 or w.shape[1]!=66 or not np.all((w==0)|(w==1)):raise ValueError('expected binary M=64 words')
    H=np.zeros((len(w),4,2),dtype=np.int64);J=[];C=[];D=[];Q=[]
    for n,row in enumerate(w.tolist()):
        U=2*row[-2]+row[-1];d=0
        for i in range(64):
            u=2*row[i]+row[i+1];H[n,u,row[i+2]]+=1
            if i<32 and u==U:d+=1
        j=int(H[n,U,0]+H[n,U,1]);c=int(H[n,U,1]);a=c/j if j>0 and 512*d>=j else row[-2]
        J.append(j);C.append(c);D.append(d);Q.append(.75*a+.125)
    return dict(H=H,J=np.array(J),C=np.array(C),D=np.array(D),Q=np.array(Q))

def features(words,condition):
    w=pilot.validate_words(words)
    if w.shape[1]!=66:raise ValueError('calibration is fixed at M=64')
    if condition not in ['half_normalized','half_count_scaled','uniform_control']:raise ValueError('unknown condition')
    e=pilot.local_selected(w);full=e.mean(axis=1)
    first=full if condition=='uniform_control' else e[:,:32].mean(axis=1)
    last=full if condition=='uniform_control' else e[:,32:].mean(axis=1)
    return np.column_stack([full,first,last,w[:,-2:],np.full(len(w),1/64)])

def decode_features(x):
    """Exact fixed-half feature decoder, separate from the literal word oracle."""
    x=np.asarray(x);j=x[:,0]+x[:,1];c=x[:,1];d=(x[:,2]+x[:,3])/2
    ratio=np.divide(c,j,out=np.zeros(len(x)),where=j>0);a=np.where((j>0)&(512*d>=j),ratio,x[:,6])
    return .75*a+.125

def kl(target,pred):return pilot.cross_entropy(target,pred)-pilot.cross_entropy(target,target)
def collision_floor():return float(np.log(2)-pilot.cross_entropy(np.array([.125]),np.array([.125]))[0])

class Readout:
    def __init__(self,seed,condition):
        if condition not in ['half_normalized','half_count_scaled','uniform_control']:raise ValueError('unknown condition')
        self.condition=condition;self.scale=SCALE.copy() if condition=='half_count_scaled' else np.ones(9)
        upstream=pilot.Model(seed,'half');self.params={k:v.copy() for k,v in upstream.params.items() if k!='a'}
        self.params['W']/=self.scale[:,None]
    def forward(self,x,cache=False):
        x=np.asarray(x,dtype=np.float64)
        if x.ndim!=2 or x.shape[1]!=9:raise ValueError('expected 9 normalized feature coordinates')
        xs=x*self.scale;p=self.params;h=np.tanh(xs@p['W']+p['b']);s=pilot.sigmoid(h@p['v']+p['c'][0]);eps=1/66**2;q=eps+(1-2*eps)*s
        return (q,dict(xs=xs,h=h,s=s,eps=eps)) if cache else q
    def predict(self,x):return self.forward(x)
    def loss_grad(self,x,target):
        q,cache=self.forward(x,cache=True);target=np.asarray(target);n=len(q)
        if target.shape!=(n,):raise ValueError('target shape')
        d=(q-target)/(q*(1-q))*(1-2*cache['eps'])*cache['s']*(1-cache['s'])/n
        dh=d[:,None]*self.params['v'][None,:]*(1-cache['h']**2)
        grad=dict(W=cache['xs'].T@dh,b=dh.sum(axis=0),v=cache['h'].T@d,c=np.array([d.sum()]))
        return float(pilot.cross_entropy(target,q).mean()),grad,cache
    def effective_W(self):return self.scale[:,None]*self.params['W']
    def save(self,path):np.savez(path,condition=np.array(self.condition),scale=self.scale,effective_W=self.effective_W(),**self.params)
