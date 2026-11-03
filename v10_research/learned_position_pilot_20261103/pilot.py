"""Small positional-pooling experiment. No hidden table or label enters attacks."""
import numpy as np

def validate_words(words):
    w=np.asarray(words)
    if w.ndim!=2 or w.shape[1]<3 or not np.all((w==0)|(w==1)):
        raise ValueError('expected binary words of shape (batch,M+2), M>=1')
    return w

def local_selected(words):
    w=validate_words(words);M=w.shape[1]-2;U=2*w[:,-2]+w[:,-1]
    pair=2*w[:,:M]+w[:,1:M+1];match=pair==U[:,None];one=w[:,2:]
    return np.stack([match*(1-one),match*one],axis=2).astype(np.float64)

def statistics(words):
    w=validate_words(words);M=w.shape[1]-2;e=local_selected(w)
    J=e.sum(axis=(1,2));C=e[:,:,1].sum(axis=1);D=e[:,:M//2].sum(axis=(1,2));B=(C+1)/(J+2)
    accepted=(J>0)&(512*D>=J);ratio=np.divide(C,J,out=np.zeros(len(w)),where=J>0)
    A=np.where(accepted,ratio,w[:,-2]);s=1/np.sqrt(M)
    # Q is only used at M>=64 in the experiment. It is not a valid smoothing for M<4.
    Q=(1-2*s)*A+s
    return dict(J=J,C=C,D=D,B=B,A=A,Q=Q,U=2*w[:,-2]+w[:,-1])

def simulate_words(p,starts,M,rng=None,uniforms=None):
    p=np.asarray(p,dtype=np.float64);starts=np.asarray(starts)
    if M<1 or p.shape!=(len(starts),4) or np.any(~np.isfinite(p)) or np.any((p<0)|(p>1)) or np.any((starts<0)|(starts>3)):
        raise ValueError('invalid source or horizon')
    if uniforms is not None and np.asarray(uniforms).shape!=(M,len(starts)):raise ValueError('invalid uniform array')
    w=np.empty((len(starts),M+2),dtype=np.int8);w[:,0]=starts//2;w[:,1]=starts%2;idx=np.arange(len(starts))
    for i in range(M):
        u=2*w[:,i]+w[:,i+1];v=uniforms[i] if uniforms is not None else rng.random(len(starts))
        w[:,i+2]=(v<p[idx,u]).astype(np.int8)
    return w

def prior_batch(n,M,rng):
    p=rng.random((n,4));starts=rng.integers(0,4,n);w=simulate_words(p,starts,M,rng=rng)
    return w,p

def position_basis(M):
    t=(np.arange(M)+.5)/M;r=t*7;j=np.minimum(np.floor(r).astype(int),6);a=r-j
    phi=np.zeros((M,8));phi[np.arange(M),j]=1-a;phi[np.arange(M),j+1]=a
    return phi

def sigmoid(x):
    x=np.asarray(x);out=np.empty_like(x,dtype=float);pos=x>=0
    out[pos]=1/(1+np.exp(-x[pos]));ex=np.exp(x[~pos]);out[~pos]=ex/(1+ex)
    return out

def cross_entropy(target,q):
    target=np.asarray(target);q=np.asarray(q)
    # All experiment soft targets are strictly interior. Endpoint predictions legitimately incur infinity.
    with np.errstate(divide='ignore',invalid='ignore'):
        a=np.where(target==0,0,-target*np.log(q));b=np.where(target==1,0,-(1-target)*np.log1p(-q))
    return a+b

class Model:
    def __init__(self,seed,mode='learned'):
        if mode not in ['learned','uniform','random','half']:raise ValueError('unknown mode')
        self.mode=mode;rng=np.random.default_rng(seed)
        a=rng.normal(0,.01,(2,8));W=rng.normal(0,np.sqrt(2/41),(9,32));v=rng.normal(0,np.sqrt(2/33),32)
        self.params=dict(a=a,W=W,b=np.zeros(32),v=v,c=np.zeros(1))
    def pooling(self,M):
        phi=position_basis(M)
        if self.mode=='uniform':alpha=np.full((3,M),1/M)
        elif self.mode=='half':
            if M<2:raise ValueError('half control requires M>=2')
            n=M//2;alpha=np.zeros((3,M));alpha[0]=1/M;alpha[1,:n]=1/n;alpha[2,n:]=1/(M-n)
        else:
            logits=self.params['a']@phi.T;logits-=logits.max(axis=1,keepdims=True);a=np.exp(logits);a/=a.sum(axis=1,keepdims=True)
            alpha=np.vstack([np.full(M,1/M),a])
        return alpha,phi
    def forward(self,words,cache=False):
        w=validate_words(words);M=w.shape[1]-2;e=local_selected(w);alpha,phi=self.pooling(M)
        f=np.einsum('hi,bic->bhc',alpha,e,optimize=True)
        x=np.column_stack([f.reshape(len(w),6),w[:,-2:],np.full(len(w),1/M)])
        p=self.params;hidden=np.tanh(x@p['W']+p['b']);raw=hidden@p['v']+p['c'][0];s=sigmoid(raw)
        eps=(M+2.)**-2;q=eps+(1-2*eps)*s
        if cache:return q,dict(e=e,alpha=alpha,phi=phi,x=x,hidden=hidden,s=s,M=M,eps=eps)
        return q
    def predict(self,words):return self.forward(words)
    def loss_grad(self,words,target):
        q,c=self.forward(words,cache=True);target=np.asarray(target);n=len(q)
        if target.shape!=(n,):raise ValueError('target shape mismatch')
        d=(q-target)/(q*(1-q))*(1-2*c['eps'])*c['s']*(1-c['s'])/n
        hidden=c['hidden'];dh=d[:,None]*self.params['v'][None,:]*(1-hidden**2)
        grad=dict(v=hidden.T@d,c=np.array([d.sum()]),W=c['x'].T@dh,b=dh.sum(axis=0),a=np.zeros((2,8)))
        if self.mode=='learned':
            dx=dh@self.params['W'].T;df=dx[:,:6].reshape(n,3,2)
            for h in range(2):
                da=np.einsum('bc,bic->i',df[:,h+1,:],c['e'],optimize=True);alpha=c['alpha'][h+1]
                ds=alpha*(da-np.dot(da,alpha));grad['a'][h]=ds@c['phi']
        return float(cross_entropy(target,q).mean()),grad
    def save(self,path):np.savez(path,mode=np.array(self.mode),**self.params)

class Adam:
    def __init__(self,params,readout_lr=.003,pool_lr=.01,beta1=.9,beta2=.999,epsilon=1e-8):
        self.m={k:np.zeros_like(v) for k,v in params.items()};self.v={k:np.zeros_like(v) for k,v in params.items()};self.t=0
        self.readout_lr=readout_lr;self.pool_lr=pool_lr;self.beta1=beta1;self.beta2=beta2;self.epsilon=epsilon
    def step(self,params,grad):
        self.t+=1
        for k in params:
            g=grad[k];self.m[k]=self.beta1*self.m[k]+(1-self.beta1)*g;self.v[k]=self.beta2*self.v[k]+(1-self.beta2)*g*g
            m=self.m[k]/(1-self.beta1**self.t);v=self.v[k]/(1-self.beta2**self.t);lr=self.pool_lr if k=='a' else self.readout_lr
            params[k]-=lr*m/(np.sqrt(v)+self.epsilon)

def proposals(words,k,family):
    w=validate_words(words);M=w.shape[1]-2
    if not isinstance(k,(int,np.integer)) or k<0 or k>M:raise ValueError('invalid edit budget')
    if family not in ['training','heldout']:raise ValueError('unknown attack family')
    if k==0:return w[None].copy()
    if family=='training':indices=[np.arange(s,s+k) for s in [0,(M-k)//2,M-k]]
    else:indices=[np.arange(s,s+k) for s in [(M-k)//4,3*(M-k)//4]]+[np.floor(np.linspace(0,M-1,k)).astype(int)]
    result=[w.copy()]
    for positions in indices:
        for op in [0,1,2]:
            z=w.copy();z[:,positions]=op if op<2 else 1-z[:,positions];result.append(z)
    return np.stack(result)

def attack(predict,words,k,family):
    w=validate_words(words);candidates=proposals(w,k,family);nprop,batch,length=candidates.shape
    target=statistics(w)['B'];q=predict(candidates.reshape(-1,length)).reshape(nprop,batch)
    losses=cross_entropy(target[None,:],q);selected=losses.argmax(axis=0);z=candidates[selected,np.arange(batch)].copy()
    return z,dict(selected=selected,objective=losses[selected,np.arange(batch)],changed=np.sum(z!=w,axis=1))

def stress_sources(M):
    t=2/M
    return dict(iid_half=np.array([.5]*4),sticky_a_quarter_t_2_over_M=np.array([.25,.5,.5,1-t]),sticky_a_equals_t_2_over_M=np.array([t,.5,.5,1-t]))
