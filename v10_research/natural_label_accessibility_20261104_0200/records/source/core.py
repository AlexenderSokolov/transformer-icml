"""Supplied-triple attention readout. Pure deterministic numerical operations."""
import numpy as np

WIDTH=32
PARAM_COUNT=64+21*WIDTH+WIDTH+WIDTH+1

def unpack(p):
    if p.shape!=(PARAM_COUNT,):raise ValueError('parameter shape')
    return p[:64].reshape(2,4,8),p[64:736].reshape(21,32),p[736:768],p[768:800],p[800:801]

def initial_parameters(rng):
    p=np.zeros(PARAM_COUNT,dtype=np.float64)
    S,W,b,v,c=unpack(p)
    W[:]=rng.normal(0,np.sqrt(2/53),W.shape)
    v[:]=rng.normal(0,np.sqrt(2/33),v.shape)
    return p

def simulate_from_draws(p,starts,draws):
    p=np.asarray(p,dtype=float);starts=np.asarray(starts,dtype=np.int64);draws=np.asarray(draws,dtype=float)
    n=len(p);M=draws.shape[1]-1
    if p.shape!=(n,4) or starts.shape!=(n,) or M<1:raise ValueError('simulation shape')
    if np.any((p<0)|(p>1)) or np.any((starts<0)|(starts>3)) or np.any((draws<0)|(draws>=1)):raise ValueError('simulation range')
    full=np.empty((n,M+3),np.int8);full[:,0]=starts//2;full[:,1]=starts%2
    for i in range(M+1):
        u=2*full[:,i]+full[:,i+1];full[:,i+2]=(draws[:,i]<p[np.arange(n),u]).astype(np.int8)
    return full[:,:-1].copy(),full[:,-1].copy()

def statistics(words):
    w=np.asarray(words)
    if w.ndim!=2 or w.shape[1]<3 or np.any((w!=0)&(w!=1)):raise ValueError('binary words')
    n=len(w);ts=4*w[:,:-2]+2*w[:,1:-1]+w[:,2:]
    H=np.zeros((n,8),np.int64);np.add.at(H,(np.arange(n)[:,None],ts),1)
    U=(2*w[:,-2]+w[:,-1]).astype(np.int64);C=H[np.arange(n),2*U+1];J=C+H[np.arange(n),2*U]
    return H,U,J,C,(C+1)/(J+2)

def pooling(p,H,U,learned):
    S=unpack(p)[0]
    a=S[:,U,:].transpose(1,0,2) if learned else np.zeros((len(H),2,8))
    a=a-np.max(np.where(np.asarray(H)[:,None,:]>0,a,-np.inf),axis=2,keepdims=True)
    a=np.where(np.asarray(H)[:,None,:]>0,a,-np.inf)
    mass=np.asarray(H,dtype=float)[:,None,:]*np.exp(a)
    return mass/mass.sum(axis=2,keepdims=True)

def forward(p,H,U,M,learned):
    S,W,b,v,c=unpack(p);pool=pooling(p,H,U,learned)
    x=np.concatenate([pool.reshape(len(H),16),np.eye(4)[U],np.full((len(H),1),1/M)],axis=1)
    hidden=np.tanh(x@W+b);z=hidden@v+c[0]
    ez=np.exp(-np.abs(z));s=np.where(z>=0,1/(1+ez),ez/(1+ez));eta=1/(M+2)**2
    q=eta+(1-2*eta)*s
    return q,(pool,x,hidden,s,eta)

def predict(p,H,U,M,learned):return forward(p,H,U,M,learned)[0]

def ce(t,q):return -t*np.log(q)-(1-t)*np.log1p(-q)

def kl(t,q):
    t=np.asarray(t,dtype=float);q=np.asarray(q,dtype=float)
    if np.any((t<0)|(t>1)) or np.any((q<=0)|(q>=1)):raise ValueError('KL domain')
    a=np.where(t>0,t,1.);b=np.where(t<1,1-t,1.)
    ans=t*np.log(a/q)+(1-t)*np.log(b/(1-q))
    return np.maximum(ans,0.)

def loss_grad(p,H,U,M,target,learned):
    q,(pool,x,h,s,eta)=forward(p,H,U,M,learned);S,W,b,v,c=unpack(p)
    target=np.asarray(target,dtype=float)
    d=(q-target)/(q*(1-q))*(1-2*eta)*s*(1-s)/len(H)
    grad=np.zeros_like(p);gS,gW,gb,gv,gc=unpack(grad)
    gv[:]=h.T@d;gc[0]=d.sum();dh=(d[:,None]*v[None,:])*(1-h*h)
    gW[:]=x.T@dh;gb[:]=dh.sum(axis=0)
    if learned:
        dp=(dh@W.T)[:,:16].reshape(len(H),2,8)
        ds=pool*(dp-(pool*dp).sum(axis=2,keepdims=True))
        for head in range(2):np.add.at(gS[head],U,ds[:,head,:])
    return float(ce(target,q).mean()),grad

def adam_step(p,g,m,v,step,cfg):
    m1=cfg['beta1']*m+(1-cfg['beta1'])*g
    v1=cfg['beta2']*v+(1-cfg['beta2'])*g*g
    p1=p-cfg['lr']*(m1/(1-cfg['beta1']**step))/(np.sqrt(v1/(1-cfg['beta2']**step))+cfg['epsilon'])
    return p1,m1,v1
