"""Read-only exact arithmetic audit of retained float/hardness diagnostic records.

No archived program is imported or executed. No checkpoint is loaded, no model
is initialized, no RNG or network is used, and verify_records writes nothing.
The root is the directory directly containing the named research units.
Finite diagnostics validate their saved arithmetic, not the general theorems.
"""
from collections import Counter
from decimal import Decimal, ROUND_CEILING, localcontext
from fractions import Fraction as F
import gzip
import json
from math import comb, isfinite
from pathlib import Path

FILES = {
 'weighted': 'position_weighted_attack_hardness_20261103_0903/review_independent_20261103_0906/candidate_records.jsonl.gz',
 'dyadic': 'dyadic_feature_dp_20261103_0915/review_independent_20261103_0917/full_records.jsonl.gz',
 'growing': 'growing_features_hardness_20261103_0922/review_independent_20261103_0924/full_records.jsonl.gz',
 'pointwise': 'fixed_source_pointwise_tv_hardness_20261103_0934/review_independent_20261103_0935/full_case_records.jsonl.gz',
 'expected': 'fixed_source_expected_tv_hardness_20261103_0939/review_independent_20261103_0940/full_case_records.jsonl.gz',
 'factor': 'constant_factor_expected_tv_hardness_20261103_0945/review_independent_20261103_0947/full_case_records.jsonl.gz',
 'additive': 'constant_additive_expected_tv_hardness_20261103_0954/review_independent_20261103_0955/full_case_records.jsonl.gz',
 'conditional': 'expected_risk_prior_art_audit_20261103_0957/conditional_cases.jsonl',
 'intervals': 'conditional_bank_interval_certificate_20261103_0854/review_independent/reconstructed_intervals.json',
 'bounds': 'float_readout_bound_20261103/bounds.json',
 'trained': 'trained_half_float_check_20261103/trained_results.json',
}
EXPECTED_COUNTS = {
 'weighted': {'record':155152,'case':246},
 'dyadic': {'record':5120},
 'growing': {'normalization':28900,'assignment':29898,'full_mask':1410,'gap':4376},
 'pointwise': {'formula':47,'mask':1323,'summary':47},
 'expected': {'formula':3,'candidate':1728,'history_summary':192,'formula_summary':3},
 'factor': {'normalization':1728,'formula':3,'case':180,'history_summary':12,'formula_summary':3},
 'additive': {'normalization':1728,'formula':3,'case':180,'history_summary':12,'formula_summary':3},
 'conditional': {'record':5},
}

class VerificationError(ValueError):
    """The retained record fails a specific audit invariant."""

class Audit:
    def __init__(self):
        self.checks=0
        self.counts={}
        self.context='initialization'
    def ok(self, condition, label):
        self.checks+=1
        if not condition: raise VerificationError(self.context+': '+label)
    def eq(self,a,b,label):
        self.ok(a==b,label)


def safe_path(root, relative):
    root=Path(root).absolute()
    for p in (root,*root.parents):
        if p.is_symlink(): raise VerificationError('symlink in root: '+str(p))
    if not root.is_dir(): raise VerificationError('missing input root')
    rel=Path(relative)
    if rel.is_absolute() or '..' in rel.parts or str(rel) not in FILES.values():
        raise VerificationError('input outside fixed allowlist')
    p=root
    for part in rel.parts:
        p=p/part
        if p.is_symlink(): raise VerificationError('input symlink: '+str(p))
    if not p.is_file() or not p.resolve().is_relative_to(root.resolve()):
        raise VerificationError('missing input or input path escape: '+relative)
    return p


def no_duplicate_keys(items):
    out={}
    for k,v in items:
        if k in out: raise VerificationError('duplicate JSON key: '+k)
        out[k]=v
    return out


def parse(s):
    def bad(v): raise VerificationError('non-finite JSON number: '+v)
    return json.loads(s,parse_float=Decimal,parse_constant=bad,object_pairs_hook=no_duplicate_keys)


def records(root,key,a):
    p=safe_path(root,FILES[key]); counts=Counter()
    opener=gzip.open if p.suffix=='.gz' else open
    with opener(p,'rt',encoding='utf-8') as f:
        for lineno,line in enumerate(f,1):
            a.context=FILES[key]+':'+str(lineno)
            r=parse(line); kind=r.get('kind',r.get('type','record'))
            counts[kind]+=1
            yield r
    a.eq(dict(counts),EXPECTED_COUNTS[key],'exact retained record census')
    a.counts[key]=dict(counts)


def read_json(root,key,a):
    a.context=FILES[key]
    return parse(safe_path(root,FILES[key]).read_text(encoding='utf-8'))


def frac(x):
    if isinstance(x,list):
        if len(x)!=2 or any(type(v) is not int for v in x) or x[1]<=0:
            raise VerificationError('invalid rational pair')
        y=F(*x)
        if [y.numerator,y.denominator]!=x: raise VerificationError('non-canonical rational pair')
        return y
    return F(x)


def enc(x):
    if isinstance(x,F):return [x.numerator,x.denominator]
    if isinstance(x,(tuple,list)):return [enc(v) for v in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x


def feq(a,row,key,value): a.eq(row[key],enc(value),key)
def power2(n): return n>0 and n&(n-1)==0
def next2(n): return 1<<(n-1).bit_length()
def lit(l,z):return z[abs(l)-1] if l>0 else 1-z[abs(l)-1]
def truths(phi,z):return [any(lit(l,z) for l in cl) for cl in phi]
def norm(cl):
    s=set(cl)
    return None if any(-x in s for x in s) else sorted(s)


def mask_word(a,h,z,mask,M,k):
    a.ok(len(h)==len(z)==M+2,'history length')
    a.ok(all(type(x) is int and x in (0,1) for x in h+z),'binary retained words')
    a.ok(mask==sorted(set(mask)) and len(mask)<=k and all(type(i) is int and 0<=i<M for i in mask),'legal unique edit mask')
    a.eq([i for i,(x,y) in enumerate(zip(h,z)) if x!=y],mask,'mask exactly equals changed coordinates')
    a.eq(z[-2:],h[-2:],'protected suffix')


def source(a,r,M,trans_key='transition',square_key='transition_squared'):
    p=F(1,M*M);ps=[1-p,p]
    mat=[[ps[j%2] if i%2==j//2 else F(0) for j in range(4)] for i in range(4)]
    stat=[ps[i//2]*ps[i%2] for i in range(4)]
    square=[[sum(mat[i][k]*mat[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    feq(a,r,trans_key,mat);feq(a,r,square_key,square);feq(a,r,'stationary',stat)
    a.eq(square,[stat]*4,'P squared equals stationary rows')
    return p,stat


def weighted(root,a):
    pending=[];ids=set()
    for r in records(root,'weighted',a):
        if r.get('type')!='case':pending.append(r);continue
        cid=r['case'];a.ok(cid not in ids,'unique weighted case');ids.add(cid)
        weights=r['weights'];n=len(weights);M=r['M'];B=r['B'];G=r['G'];C=r['C'];k=r['k']
        a.ok(all(type(x) is int and x>0 for x in weights),'positive integer weights')
        a.eq(M,next2(max(n*n,4)),'padded length');a.eq(k,n,'edit budget');a.eq(C,max(weights),'C');a.eq(G,next2(sum(weights)),'dyadic normalization')
        masks=set();seen=set();original=set()
        for x in pending:
            a.eq(x['case'],cid,'candidate belongs to case');ix=x['indices']
            a.ok(ix==sorted(set(ix)) and len(ix)<=k and all(0<=i<M for i in ix),'candidate edit mask')
            a.ok(tuple(ix) not in masks,'no duplicate candidate');masks.add(tuple(ix))
            S=sum(weights[i] for i in ix if i<n);seen.add(S)
            if all(i<n for i in ix):original.add(S)
            rr=-F(abs(S-B),2*G);qd=F(3,2*M)-F(abs(S-B),2*M*G)
            a.eq(x['S'],S,'weighted subset sum');feq(a,x,'r',rr);feq(a,x,'q_d',qd)
            a.ok(-F(1,2)<=rr<=0 and F(1,M)<=qd<=F(3,2*M)<=F(3,8),'readout range')
            a.ok(qd>F(1,M+2) and (rr==0)==(qd==F(3,2*M))==(S==B),'threshold equivalence')
        a.eq(len(masks),sum(comb(M,j) for j in range(k+1)),'all legal masks retained')
        a.eq(r['masks'],len(masks),'recorded mask count');a.eq(sorted(seen),r['original_subset_sums'],'subset sum image');a.eq(original,seen,'padding does not change sums');a.eq(r['yes'],B in seen,'yes decision')
        pending=[]
    a.eq(pending,[],'no unterminated weighted case')


def scan_dyadic(h,z,r,mode):
    q=1;w=[0]*r;b=[0]*(3 if mode=='signed' else 4)
    for t,x in enumerate(z):
        prev=w[-1] if r else 0;prev2=w[-2] if r==2 else 0
        if mode=='signed':
            inc=[(2*t%5-2)*x+prev-h[(t+2)%len(h)],(1-2*x)*(t%3+1)+prev2,x-prev+prev2]
            q=(q*2+x+prev+t)%4
        else:
            aw=1+t%2+x;bw=1+prev;inc=[aw*(2*x-1),aw,bw*(x+prev-1),bw];q=(q+x+t)%4
        b=[u+v for u,v in zip(b,inc)];w=(w+[x])[-r:] if r else []
    return (q,tuple(w),tuple(b))


def tuple_key(k):return (k[0],tuple(k[1]),tuple(k[2]))
def utility(key,mode):
    q,w,b=key
    if mode=='signed':return F(b[0]**2+2*b[1]-b[2]+q+sum(w),1+sum(abs(x) for x in b))
    return F(b[0],2*b[1])+F(b[2],4*b[3])+q+sum(w)


def dyadic(root,a):
    seen_cases=set()
    for r in records(root,'dyadic',a):
        mode=r['mode'];memory=r['r'];M=r['M'];h=r['h'];k=r['k']
        a.ok(mode in ('signed','heads') and memory in (0,2) and 1<=M<=5 and 0<=k<=M,'DP case parameters')
        signature=(mode,memory,M,tuple(h),k);a.ok(signature not in seen_cases,'unique retained DP case');seen_cases.add(signature)
        best={};masks=set()
        for mask,z,key in r['masks']:
            mask_word(a,h,z,mask,M,k);a.ok(tuple(mask) not in masks,'unique DP mask');masks.add(tuple(mask))
            sk=scan_dyadic(h,z,memory,mode);a.eq(tuple_key(key),sk,'saved scan terminal key')
            best[sk]=min(best.get(sk,len(mask)),len(mask))
        a.eq(len(masks),sum(comb(M,j) for j in range(k+1)),'all legal DP masks retained')
        dp={}
        for key,cost,z in r['map']:
            sk=tuple_key(key);a.ok(sk not in dp,'unique terminal DP key');dp[sk]=cost
            mask=[i for i,(x,y) in enumerate(zip(h,z)) if x!=y];mask_word(a,h,z,mask,M,k)
            a.eq(cost,len(mask),'minimum witness cost');a.eq(scan_dyadic(h,z,memory,mode),sk,'DP witness key')
            if mode=='heads':
                prev=[0]+z[:-1] if memory else [0]*len(z)
                aw=[1+t%2+x for t,x in enumerate(z)];bw=[1+y for y in prev];b=sk[2]
                a.eq(F(b[0],2*b[1]),sum(F(v*(2*x-1),2) for v,x in zip(aw,z))/sum(aw),'first normalized head')
                a.eq(F(b[2],4*b[3]),sum(F(v*(x+y-1),4) for v,x,y in zip(bw,z,prev))/sum(bw),'second normalized head')
        a.eq(dp,best,'terminal reachable map and min-cost dominance')
        a.eq(max(utility(s,mode) for s in dp),max(utility(s,mode) for s in best),'terminal utility optimum')


def growing(root,a):
    for r in records(root,'growing',a):
        kind=r['kind']
        if kind=='normalization':
            normalized=[];contradiction=False
            for cl in r['raw']:
                nc=norm(cl)
                if nc is None:continue
                if not nc:contradiction=True;break
                normalized.append(nc)
            a.eq(r['normalized'],normalized,'normalized clauses');a.eq(r['contradiction'],contradiction,'empty clause detection')
            before=all(truths(r['raw'],r['assignment']));after=not contradiction and all(truths(normalized,r['assignment']))
            a.eq(r['truth'],before,'raw truth');a.eq(before,after,'normalization preserves truth')
        elif kind=='gap':
            M=r['M'];m=r['m'];P=r['P'];V=r['V'];a.eq(P,next2(m),'gap dyadic P')
            q=F(3,2*M)-F(V,2*M*P);target=F(1,M+2);lower=F(8,M*(M+2));deriv=(q-target)/(q*(1-q))
            feq(a,r,'q',q);feq(a,r,'derivative',deriv);feq(a,r,'lower',lower);a.ok(deriv>=lower and F(1,M)<=q<=F(3,2*M),'gap derivative bound')
        else:
            phi=r['formula'];n=r['n'];m=len(phi);M=r['M'];P=r['P'];z=r['z']
            a.eq(M,next2(max(4,n*n,m*m)),'growing padded length');a.eq(P,next2(m),'growing P')
            mask_word(a,[0]*(M+2),z,r['mask'],M,n)
            if kind=='assignment':a.eq(z[:n],r['bits'],'retained assignment')
            bank=[sum((int(i+1 in cl)-int(-(i+1) in cl))*z[i] for i in range(M)) for cl in phi]
            L=[sum(lit(l,z) for l in cl) for cl in phi];V=[max(0,1-x) for x in L]
            a.eq(r['bank'],bank,'signed clause banks');a.eq(r['literal_counts'],L,'literal counts');a.eq(r['violations'],V,'violations')
            q=F(3,2*M)-F(sum(V),2*M*P);target=F(1,M+2)
            feq(a,r,'q',q);feq(a,r,'Q',F(3,2*M));feq(a,r,'target',target);feq(a,r,'ce_gap',F(4,M*M*(M+2)*P))
            a.ok((q==F(3,2*M))==all(L),'satisfaction equivalence')
            a.ok((q-target)/(q*(1-q))>=F(8,M*(M+2)),'CE derivative lower bound')


def formula_setup(a,r,kind):
    phi=r.get('phi',r.get('raw_formula'));n=r['n'];m=len(phi);M=r['M'];P=r['P'];k=r['k']
    a.eq(r['m'],m,'formula size');a.eq(P,next2(m),'dyadic P');a.eq(k,n,'budget n');a.ok(power2(M) and M>=max(4,n*n,m*m),'padded length bound')
    normalized=[norm(cl) for cl in phi] if kind in ('factor','additive') else phi
    neg=[1 if cl is None else sum(x<0 for x in cl) for cl in normalized]
    inc=[[0 if cl is None else int(i+1 in cl)-int(-(i+1) in cl) for i in range(M)] for cl in normalized]
    a.eq(r['incidence'],inc,'clause incidence')
    if kind=='factor':p,stat=source(a,r,M,'source_transition','source_squared')
    elif kind=='additive':p,stat=source(a,r,M,'transition','square')
    else:p,stat=source(a,r,M)
    feq(a,r,'p',p)
    if kind in ('factor','additive'):
        a.eq(r['normalized'],normalized,'formula normalization');a.eq(r['negative_counts'],neg,'negative literal counts')
    elif kind=='pointwise':a.eq(r['negative_literals'],neg,'negative literal counts')
    return {'phi':phi,'n':n,'m':m,'M':M,'P':P,'k':k,'p':p,'inc':inc,'neg':neg,'stat':stat}


def check_model(a,f,z,res,kind):
    M=f['M'];P=f['P'];p=f['p'];phi=f['phi'];m=f['m']
    rows=res['layers'] if kind=='pointwise' else res['rows']
    banks=res['bank_pool_literals'] if kind=='pointwise' else res['banks']
    a.eq(len(rows),m,'layer clause count');a.eq(len(banks),m,'bank clause count');counts=[];truth=[]
    for j,cl in enumerate(phi):
        a.eq(len(rows[j]),M,'position layer length');B=0
        for i,e in enumerate(rows[j]):
            s=f['inc'][j][i];x=z[i];pa=s+x-1;pb=-s+x-1;rp=max(pa,0);rm=max(pb,0);v=rp-rm
            expected={'s':s,'x':x,'pre_plus':pa,'pre_minus':pb,'relu_plus':rp,'relu_minus':rm}
            if 'i' in e:expected['i']=i
            expected['v' if 'v' in e else 'value']=v
            a.eq(e,expected,'retained ReLU row');a.eq(v,s*x,'signed ReLU identity');B+=v
        L=f['neg'][j]+B;raw=[lit(l,z) for l in cl];ok=any(raw);a.eq(L>0,ok,'literal truth from bank')
        b=banks[j]
        if kind=='pointwise':expected={'sum':B,'pool':F(B,M),'L':F(L),'direct':sum(raw)}
        elif kind=='expected':expected={'bank':B,'avg':F(B,M),'negative_count':f['neg'][j],'L':F(L),'direct':sum(raw)}
        elif kind=='factor':expected={'bank':B,'avg':F(B,M),'L':F(L),'raw_literal_values':raw,'truth':ok}
        else:expected={'bank':B,'pooled':F(B,M),'L':F(L),'raw_values':raw,'truth':ok}
        a.eq(b,enc(expected),'retained pooled bank');counts.append(L);truth.append(ok)
    if kind in ('pointwise','expected'):
        violations=[max(0,1-L) for L in counts];V=sum(violations);q=F(3,2*M)-F(V,2*M*P)
        a.eq(res['violations'],violations,'violation list');a.eq(res['V'],V,'total violations')
        a.ok(F(1,M)<=q<=F(3,2*M) and q>p,'readout range')
        feq(a,res,'signed_difference' if kind=='pointwise' else 'signed_q_minus_p',q-p)
    else:
        S=sum(truth);q=p+F(S,(2 if kind=='additive' else M)*P)
        a.eq(res['truth'],truth,'clause truth vector');a.eq(res['S'],S,'satisfaction count')
    feq(a,res,'q',q);feq(a,res,'p',p);feq(a,res,'tv',abs(q-p))
    return abs(q-p),all(truth),sum(truth)


def assignments_check(a,phi,rows,n,details):
    seen=set();winners=[]
    for r in rows:
        z=r['bits'];a.ok(len(z)==n and all(x in (0,1) for x in z),'assignment shape');a.ok(tuple(z) not in seen,'unique assignment');seen.add(tuple(z))
        vals=[[lit(l,z) for l in cl] for cl in phi];truth=[any(v) for v in vals];sat=all(truth)
        a.eq(r[details],truth if details=='clause_truth' else vals,'assignment literal evidence');a.eq(r['satisfies'],sat,'assignment SAT')
        if sat:winners.append(z)
    a.eq(len(seen),2**n,'all assignments retained')
    return winners


def pointwise(root,a):
    f=None; masks={};formulas=0
    for r in records(root,'pointwise',a):
        kind=r['kind']
        if kind=='formula':
            a.ok(f is None,'previous formula summarized');f=formula_setup(a,r,'pointwise');f['id']=r['id'];masks={};formulas+=1
            M=f['M'];p=f['p'];Q=F(3,2*M);tau=Q-p;delta=F(1,2*M*f['P']);f.update(Q=Q,tau=tau,delta=delta)
            feq(a,r,'Q',Q);feq(a,r,'t',F(1,M+2));feq(a,r,'threshold',tau);feq(a,r,'Delta',delta)
            lower=1-F(M+2,M*M);feq(a,r,'lower_zero_probability',lower);a.ok((1-p)**(M+2)>=lower>0,'zero-history union bound')
            for law in r['initial_laws']:
                mu=list(map(frac,law['mu']));a.eq(sum(mu),F(1),'initial law mass');val=mu[0]*(1-p)**M
                feq(a,law,'history_probability',val);feq(a,law,'formula_value',val);a.eq(law['positive'],val>0,'initial support')
        elif kind=='mask':
            a.eq(r['id'],f['id'],'formula ID');z=r['word'];mask=r['mask'];mask_word(a,[0]*(f['M']+2),z,mask,f['M'],f['k'])
            a.ok(tuple(mask) not in masks,'unique pointwise mask');tv,sat,_=check_model(a,f,z,r,'pointwise');masks[tuple(mask)]=tv
            q=tv+f['p'];t=F(1,f['M']+2);feq(a,r,'surrogate',t);feq(a,r,'ce_derivative',(q-t)/(q*(1-q)))
            feq(a,r,'threshold',f['tau']);feq(a,r,'threshold_minus_tv',f['tau']-tv);feq(a,r,'Delta',f['delta'])
            a.eq(r['satisfies'],sat,'pointwise SAT');a.eq(r['crosses_threshold'],tv>=f['tau'],'threshold flag');a.eq(tv>=f['tau'],sat,'SAT threshold equivalence')
        else:
            a.eq(r['id'],f['id'],'summary ID');a.eq(r['phi'],f['phi'],'summary formula');a.eq(len(masks),sum(comb(f['M'],j) for j in range(f['k']+1)),'pointwise full mask census')
            a.eq(r['mask_count'],len(masks),'summary mask count');best=max(masks.values());feq(a,r,'best',best);a.eq(masks[tuple(r['witness'])],best,'optimal witness')
            winners=assignments_check(a,f['phi'],r['assignments'],f['n'],'clause_truth');a.eq(r['satisfiable'],bool(winners),'summary satisfiable');a.eq(best==f['tau'],bool(winners),'optimal threshold decision');f=None
    a.ok(f is None,'final formula summarized')


def expected(root,a):
    f=None;current_h=None;by_mask={};seen_h=set();mass=risk=identity=fixed=None
    for r in records(root,'expected',a):
        kind=r['kind']
        if kind=='formula':
            a.ok(f is None,'previous expected formula summarized');f=formula_setup(a,r,'expected');f['id']=r['fid'];M=f['M'];p=f['p'];Q=F(3,2*M);delta=F(1,2*M*f['P']);tau=Q-p-delta/2
            f.update(Q=Q,delta=delta,tau=tau,mus=[list(map(frac,mu)) for mu in r['initial_laws']])
            a.eq(len(f['mus']),3,'three initial laws');a.eq(f['mus'][0],f['stat'],'stationary initial law')
            for mu in f['mus']:a.ok(sum(mu)==1 and all(x>=0 for x in mu),'initial probability law')
            winners=assignments_check(a,f['phi'],r['assignments'],f['n'],'literals');f['sat']=bool(winners);f['xstar']=winners[0] if winners else None;a.eq(r['xstar'],f['xstar'],'fixed assignment')
            feq(a,r,'Q',Q);feq(a,r,'delta',delta);feq(a,r,'threshold',tau);feq(a,r,'zero_probability',(1-p)**(M+2));feq(a,r,'zero_lower_bound',1-F(M+2,M*M))
            mass=[F(0)]*3;risk=[F(0)]*3;identity=[F(0)]*3;fixed=[F(0)]*3;seen_h=set();by_mask={};current_h=None
        elif kind in ('candidate','history_summary'):
            a.eq(r['fid'],f['id'],'expected formula ID');h=r['h'];M=f['M'];p=f['p'];ones=sum(h[2:]);probs=[mu[2*h[0]+h[1]]*p**ones*(1-p)**(M-ones) for mu in f['mus']]
            feq(a,r,'history_probability_by_initial_law',probs)
            if kind=='candidate':
                if current_h is None:current_h=h
                a.eq(h,current_h,'contiguous candidates for history');mask=r['mask'];z=r['z'];mask_word(a,h,z,mask,M,f['k']);a.ok(tuple(mask) not in by_mask,'unique expected candidate')
                tv,sat,_=check_model(a,f,z,r['result'],'expected');by_mask[tuple(mask)]=(tv,r['result']);feq(a,r,'threshold',f['tau']);feq(a,r,'delta',f['delta'])
            else:
                a.eq(h,current_h,'history summary matches candidates');a.ok(tuple(h) not in seen_h,'unique retained history');seen_h.add(tuple(h));a.eq(len(by_mask),sum(comb(M,j) for j in range(f['k']+1)),'expected candidate census')
                winner=tuple(r['winner_mask']);best=max(v[0] for v in by_mask.values());a.eq(by_mask[winner][0],best,'winner attains maximum');a.eq(r['winner_result'],by_mask[winner][1],'winner result binding');a.eq(r['identity_result'],by_mask[()][1],'identity result binding')
                for j in range(3):mass[j]+=probs[j];risk[j]+=probs[j]*best;identity[j]+=probs[j]*by_mask[()][0]
                if f['sat']:
                    z=r['fixed_word'];a.eq(z,f['xstar']+h[f['n']:],'fixed policy assignment overwrite');mask=[i for i,(x,y) in enumerate(zip(h,z)) if x!=y];mask_word(a,h,z,mask,M,f['k']);a.eq(r['fixed_cost'],len(mask),'fixed policy cost');tv,sat,_=check_model(a,f,z,r['fixed_result'],'expected');a.ok(sat,'fixed satisfying policy')
                    for j in range(3):fixed[j]+=probs[j]*tv
                else:a.eq([r['fixed_word'],r['fixed_cost'],r['fixed_result']],[None]*3,'unsatisfiable fixed-policy fields')
                for name,value in [('mass_running',mass),('risk_running',risk),('identity_running',identity),('fixed_running',fixed)]:feq(a,r,name,value)
                by_mask={};current_h=None
        else:
            a.eq(r['fid'],f['id'],'formula summary ID');a.eq(len(seen_h),2**(f['M']+2),'complete retained history space');a.eq(mass,[F(1)]*3,'integrated source mass');a.eq(by_mask,{},'all histories summarized')
            for name,value in [('mass',mass),('risk',risk),('identity',identity),('fixed',fixed if f['sat'] else None),('threshold',f['tau'])]:feq(a,r,name,value)
            a.eq(r['sat'],f['sat'],'expected SAT flag')
            for j in range(3):
                a.ok(identity[j]/risk[j]>=F(3,5),'identity approximation lower bound')
                a.ok((risk[j]>f['tau'])==f['sat'],'expected threshold decision')
                if f['sat']:a.eq(risk[j],fixed[j],'fixed policy achieves optimum')
            f=None
    a.ok(f is None,'expected records complete')


def normalize_row(a,r,kind):
    raw=r['raw_clause'] if kind=='factor' else r['raw'];nc=norm(raw);z=r['bits'];rv=[lit(x,z) for x in raw];nv=[] if nc is None else [lit(x,z) for x in nc]
    a.eq(r['normalized'],nc,'clause normalization')
    a.eq(r['raw_literal_values' if kind=='factor' else 'raw_values'],rv,'raw literal values')
    a.eq(r['normalized_literal_values' if kind=='factor' else 'normalized_values'],nv,'normalized literal values')
    a.eq(r['raw_truth'],any(rv),'raw truth');a.eq(r['normalized_truth'],True if nc is None else any(nv),'normalized truth');a.eq(r['raw_truth'],r['normalized_truth'],'normalization truth equivalence')


def gap_family(root,a,kind):
    f=None;this=[];maxima=[];history=None;seen_masks=set();seen_histories=set();seen_assignments=set()
    for r in records(root,kind,a):
        rk=r['kind']
        if rk=='normalization':normalize_row(a,r,kind);continue
        if rk=='formula':
            a.ok(f is None,'previous gap formula summarized');f=formula_setup(a,r,kind);f['id']=r['id'];M=f['M'];P=f['P'];p=f['p'];den=(2 if kind=='additive' else M)*P;C=F(f['m'],den);alpha=frac(r['alpha']);lam=F(M+2,M*M);f.update(den=den,C=C,alpha=alpha,histories=r['histories'])
            feq(a,r,'C',C);feq(a,r,'lambda_bound' if kind=='additive' else 'lambda_upper',lam);feq(a,r,'zero_probability' if kind=='additive' else 'pi0',(1-p)**(M+2));a.ok((1-p)**(M+2)>=1-lam,'gap zero-history bound')
            if kind=='additive':
                eps=frac(r['epsilon']);tau=(1+alpha)*C/2;pl=1-eps/C-lam;f.update(eps=eps,tau=tau,pl=pl)
                feq(a,r,'yes_no_gap',(1-alpha)*C);feq(a,r,'midpoint',tau);feq(a,r,'midpoint_margin',C/32);feq(a,r,'policy_satisfaction_lower',pl)
                a.ok(C>F(1,4) and (1-alpha)*C>F(1,64) and C/32>eps and pl>F(61,64)>alpha,'constant additive inequalities')
            else:
                rho=frac(r['rho']);f['rho']=rho;a.ok(M>=8/(rho-alpha) and lam<=F(2,M)<=(rho-alpha)/4,'factor gap inequalities')
            this=[];maxima=[];history=None;seen_masks=set();seen_histories=set();seen_assignments=set()
        elif rk=='case':
            a.eq(r['id'],f['id'],'gap formula ID');h=r['h'];z=r['z'];mask=r['mask'];mask_word(a,h,z,mask,f['M'],f['k'])
            if history is None:history=h
            a.eq(h,history,'gap history grouping');a.ok(tuple(mask) not in seen_masks,'unique retained mask within history');seen_masks.add(tuple(mask));bits=r['bits'] if kind=='additive' else r['assignment'];a.eq(z[:f['n']],bits,'assignment encoded in edited word');seen_assignments.add(tuple(bits))
            tv,sat,S=check_model(a,f,z,r,kind);this.append(S);feq(a,r,'C',f['C'])
            if kind=='additive':
                feq(a,r,'alpha_C',f['alpha']*f['C']);feq(a,r,'midpoint',f['tau']);feq(a,r,'error_bound',f['eps']);feq(a,r,'zero_TV_baseline',F(0))
            else:feq(a,r,'rho_lower',f['rho']*f['C']);feq(a,r,'alpha_upper',f['alpha']*f['C'])
        elif rk=='history_summary':
            a.eq(r['id'],f['id'],'gap history ID');a.eq(r['h'],history,'gap history summary');a.ok(tuple(history) not in seen_histories,'distinct retained histories');seen_histories.add(tuple(history))
            a.eq(len(seen_assignments),2**f['n'],'all assignments retained for each history');seen_assignments=set()
            a.eq(r['satisfaction_counts' if kind=='additive' else 'all_satisfaction_counts'],this,'satisfaction list aggregation');mx=max(this);a.eq(r['max_S' if kind=='additive' else 'max_satisfied'],mx,'sample maximum');feq(a,r,'pointwise_optimum',F(mx,f['den']));maxima.append(mx);this=[];history=None;seen_masks=set()
        else:
            a.eq(r['id'],f['id'],'gap final ID');a.eq(seen_histories,{tuple(h) for h in f['histories']},'retained history list binding');a.eq(r['maxima' if kind=='additive' else 'scores_by_history'],maxima,'maxima aggregation');a.ok(len(set(maxima))==1,'history-independent optimum on retained histories')
            # Each history contains every assignment, so these are exhaustive assignment maxima.
            feq(a,r,'expected_optimum_any_initial_law',F(maxima[0],f['den']));feq(a,r,'yes_value',f['C']);feq(a,r,'no_upper',f['alpha']*f['C'])
            if kind=='additive':feq(a,r,'midpoint',f['tau']);feq(a,r,'policy_lower',f['pl'])
            else:a.eq(r['max_satisfied'],maxima[0],'formula maximum')
            f=None
    a.ok(f is None,'gap records complete')


def conditional_expectation(phi,prefix):
    total=F(0)
    for cl in phi:
        nc=norm(cl)
        if nc is None:total+=1;continue
        if any(abs(l)<=len(prefix) and lit(l,prefix) for l in nc):total+=1;continue
        unfixed={abs(l) for l in nc if abs(l)>len(prefix)}
        total+=1-F(1,2**len(unfixed))
    return total


def conditional(root,a):
    for r in records(root,'conditional',a):
        phi=r['original_clauses'];n=r['n'];prefix=[];initial=conditional_expectation(phi,prefix);a.eq(frac(r['initial_expectation']),initial,'exact initial clause expectation');a.eq(len(r['steps']),n,'one step per variable')
        for step in r['steps']:
            a.eq(step['prefix_before'],prefix,'conditional prefix');v0=conditional_expectation(phi,prefix+[0]);v1=conditional_expectation(phi,prefix+[1]);a.eq(frac(step['score_0']),v0,'conditional score 0');a.eq(frac(step['score_1']),v1,'conditional score 1');a.eq((v0+v1)/2,conditional_expectation(phi,prefix),'conditional averaging identity');bit=int(v1>v0);a.eq(step['chosen_bit'],bit,'greedy tie-breaking');prefix.append(bit)
        a.eq(r['assignment'],prefix,'final assignment');achieved=sum(truths(phi,prefix));a.eq(r['achieved'],achieved,'achieved clause count')
        # Deterministic finite Boolean truth-table arithmetic, no random samples.
        opt=max(sum(truths(phi,[(i>>j)&1 for j in range(n)])) for i in range(1<<n));a.eq(r['opt'],opt,'exact finite optimum')
        qualifies=all(norm(c) is None or len({abs(x) for x in c})==3 for c in phi);a.eq(r['three_distinct_or_tautology'],qualifies,'7/8 eligibility');a.ok(achieved>=initial and 2*achieved>=len(phi),'conditional policy guarantee')
        if qualifies:a.ok(8*achieved>=7*len(phi) and 8*achieved>=7*opt,'eligible 7/8 bound')
        M=r['M'];P=r['P'];a.eq(M,next2(max(n*n,len(phi)**2,128)),'conditional M');a.eq(P,next2(len(phi)),'conditional P');a.eq(r['edited_history'],prefix+r['history'][n:],'conditional fixed assignment map');mask_word(a,r['history'],r['edited_history'],r['flips'],M,n)
        for field,val in [('risk_vanishing',F(achieved,M*P)),('opt_risk_vanishing',F(opt,M*P)),('risk_constant',F(achieved,2*P)),('opt_risk_constant',F(opt,2*P))]:a.eq(frac(r[field]),val,field)


def bank_of_word(z):
    M=len(z)-2;L=M//2;u=z[-2:];J=C=D=E=0
    for i in range(M):
        sel=z[i:i+2]==u;J+=sel;C+=sel*z[i+2];D+=sel*(i<L);E+=sel*(i<L)*z[i+2]
    return [J,C,D,E]


def float_records(root,a):
    intervals=read_json(root,'intervals',a);a.eq(len(intervals),3,'three retained intervals')
    for r in intervals:
        z=list(map(int,r['word']));a.eq(r['bank'],bank_of_word(z),'retained word bank');lo=frac(r['own_lower']);hi=frac(r['own_upper']);al=frac(r['author_reconstructed_lower']);ah=frac(r['author_reconstructed_upper'])
        a.ok(lo<=hi and al<=ah and lo<=ah and al<=hi,'endpoint ordering and overlap');a.ok(hi-lo<F(1,10**25),'independent interval width')
    for r in intervals[1:]:a.ok(frac(intervals[0]['own_lower'])-frac(r['own_upper'])>F(189,6400),'saved interval separation')
    a.eq(F(189,6400)-2*F(1,1000),F(881,32000),'post-error margin')
    bounds=read_json(root,'bounds',a);a.eq(len(bounds['checkpoints']),10,'bound checkpoint count');u=F(1,2**53);bounds_count=0
    def gamma(n):return n*u/(1-n*u)
    def rounded(x):
        with localcontext() as c:c.prec=14;c.rounding=ROUND_CEILING;return str(Decimal(x.numerator)/Decimal(x.denominator))
    def lower_decimal(s):
        d=Decimal(s);return F(d)-F(10)**d.as_tuple().exponent
    for checkpoint in bounds['checkpoints']:
        a.eq([r['M'] for r in checkpoint['results']],[64,128,256,1025],'saved horizon list')
        for r in checkpoint['results']:
            M=r['M'];bounds_count+=1
            for key,n in [('delta_full',M),('delta_first',M//2),('delta_second',M-M//2)]:a.eq(r[key],rounded(u+(1+u)*gamma(n-1)),key+' exact rounded bound')
            for key,value in r.items():
                if key!='M':a.ok(frac(value)>=0,'nonnegative saved bound '+key)
            comps=['rail_logit_error','affine_logit_error','output_dot_logit_error_at_tau_zero'];total=frac(r['logit_error_at_tau_zero']);a.ok(sum(lower_decimal(r[k]) for k in comps)<=total and lower_decimal(r['logit_error_at_tau_zero'])<=sum(frac(r[k]) for k in comps),'rounded component-sum interval consistency')
    trained=read_json(root,'trained',a);M=trained['M'];zs=[]
    for key in ('zeros_A','zeros_B'):
        zeros=trained[key];a.ok(zeros==sorted(set(zeros)) and all(0<=i<M for i in zeros),'saved zero positions');z=[int(i not in zeros) for i in range(M+2)];zs.append(z);a.eq(bank_of_word(z),trained['bank'],'fixed retained zero-pattern bank')
    a.eq(sum(x!=y for x,y in zip(*zs)),trained['editable_hamming'],'fixed-word Hamming distance');a.eq(frac(trained['target_exact']),F(340,341),'target exact')
    matches=[r for c in bounds['checkpoints'] if c['path'].endswith('/smoke_v1/checkpoints/half_edit_200.npz') for r in c['results'] if r['M']==M];a.eq(matches,[trained['conditional_bound']],'saved conditional bound binding')
    rows_count=0
    for name,batch in trained['batches'].items():
        a.eq(batch['shape'],[len(name),M+2],'batch shape');a.eq(len(batch['rows']),len(name),'batch row count')
        for row in batch['rows']:
            rows_count+=1
            for key,n in [('features_hex',9),('preactivation_hex',32),('hidden_hex',32)]:
                a.eq(len(row[key]),n,key+' dimension')
                for x in row[key]:a.ok(isfinite(float.fromhex(x)) and float.fromhex(x).hex()==x,key+' canonical finite binary64')
            for key in ('logit','prediction','ce'):
                a.ok(isfinite(float(row[key])) and isfinite(float.fromhex(row[key+'_hex'])),key+' finite binary64');a.eq(float(row[key]).hex(),row[key+'_hex'],key+' decimal and hex same binary64')
            a.ok(F(0)<F.from_float(float.fromhex(row['prediction_hex']))<1,'saved prediction range')
            a.ok(all(-1<=F.from_float(float.fromhex(v))<=1 for v in row['hidden_hex']),'saved tanh range')
            a.eq(row['features_hex'][-3:-1],['0x1.0000000000000p+0']*2,'fixed suffix features')
            a.eq(row['target_float_hex'],float(F(340,341)).hex(),'saved target binary64')
            for value_key,ideal_key,error_key in [('logit','logit','absolute_logit_error_vs_100_digit_ideal'),('prediction','prediction','absolute_q_error_vs_100_digit_ideal'),('ce','ce','absolute_ce_error_vs_100_digit_ideal')]:
                actual=F.from_float(float.fromhex(row[value_key+'_hex']));ideal=frac(trained['ideal_math'][ideal_key]);reported=frac(row[error_key]);a.ok(abs(abs(actual-ideal)-reported)<F(1,10**45),'printed error internally consistent '+value_key)
    a.counts['intervals']={'record':len(intervals)};a.counts['bounds']={'checkpoint':10,'horizon':bounds_count};a.counts['trained']={'batch':len(trained['batches']),'row':rows_count}


def verify_records(root: Path) -> dict:
    """Verify only fixed allowlisted retained inputs; fail closed on first mismatch."""
    root=Path(root);a=Audit()
    # Validate every input before computing anything. This also rejects all input symlinks.
    for relative in FILES.values():safe_path(root,relative)
    for check in (weighted,dyadic,growing,pointwise,expected):check(root,a)
    gap_family(root,a,'factor');gap_family(root,a,'additive');conditional(root,a);float_records(root,a)
    return {
      'status':'PASS','files_checked':len(FILES),'assertions_checked':a.checks,
      'record_counts':a.counts,'files':list(FILES.values()),
      'checked_scope':[
        'All 155152 retained weighted masks: legality, coverage, subset sums, exact readouts, threshold decisions.',
        'All 5120 retained dyadic cases: saved-word scans, terminal reachable maps, minimum costs, normalized heads, utility optima.',
        'Growing-feature normalization, stored assignments/full masks, clause banks, exact rational gaps and derivatives.',
        'Pointwise complete stored legal-mask sets, all retained ReLU rows, bank pooling, SAT threshold and witness checks.',
        'Expected-TV complete stored histories and masks, three initial laws, exact transition squares, running probability mass and risks.',
        'Factor/additive retained clause normalizations, ReLU rows, policy words, clause scores, retained history maxima, scalar gaps.',
        'Conditional expectation from original clause sets including duplicates and tautologies, deterministic choices, finite optimum and policy edits.',
        'Saved float JSON only: exact integer word banks, rational endpoint ordering/overlap/gaps, gamma bounds, rounded sum consistency, hex/decimal scalar agreement and printed-error consistency.'
      ],
      'unchecked_scope':[
        'No archived executable or script was run; author diagnostic output duplicates and prose/log claims are not independently re-executed.',
        'No RNG, model initialization/training, NumPy/BLAS, native executable, checkpoint loading, or network access occurs in this module.',
        'Float forward values, transcendental ideal values, backend rounding, checkpoint-derived norms and interval endpoint derivations are not reproduced.',
        'Four retained histories in each factor/additive family are not a numerical enumeration of every possible history; any-initial-law extension rests on the documented assignment-overwrite argument.',
        'Finite retained checks are not proofs of general hardness, asymptotics, novelty, or bibliographic accuracy; source identity/provenance is delegated to the outer wrapper.'
      ]}
