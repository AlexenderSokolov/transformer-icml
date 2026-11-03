#!/usr/bin/env python3
"""Read-only retained-record consistency checks, not scientific replay or proof.

Only fixed public numeric paths are read. No archived program is imported or run;
no case space, model, transition matrix or scientific output is regenerated.
Input coverage is bound to ordered keys extracted from the frozen saved records.
Deliberate duplicate inputs (different case_index) and provenance copies remain.
Run with Python 3.10+ on POSIX: python -I -B verify_retained_records.py PUBLIC_ROOT
"""
import csv
from fractions import Fraction
import hashlib
import io
import json
import os
import re
import stat
import sys

MAX_FILE = 16 * 1024 * 1024
MAX_LINE = 65536
MAX_RECORDS = 40000
MAX_INTEGER_DIGITS = 80
MAX_RATIONAL_LENGTH = 160
STATES = ('00','01','10','11')

class VerificationError(ValueError):
    """A saved input did not satisfy the declared archival checks."""

def require(test, message):
    if not test:
        raise VerificationError(message)

def integer(value, low=0, high=1000000):
    require(type(value) is int and low <= value <= high, 'invalid bounded integer')
    return value

def boolean(value):
    require(type(value) is bool, 'expected JSON boolean')
    return value

def fields(obj, names):
    require(type(obj) is dict and set(obj) == set(names.split()), 'unexpected or missing schema field')

def rational(value):
    require(type(value) is str and len(value) <= MAX_RATIONAL_LENGTH, 'rational must be a bounded string')
    require(re.fullmatch(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?', value) is not None, 'invalid rational syntax')
    pieces=value.split('/')
    require(all(len(x.lstrip('-')) <= MAX_INTEGER_DIGITS for x in pieces), 'rational integer too long')
    try: result=Fraction(value)
    except (ValueError, ZeroDivisionError) as exc: raise VerificationError('invalid rational') from exc
    require(str(result) == value, 'noncanonical rational')
    return result

def probability(value):
    result=rational(value);require(0 <= result <= 1,'probability out of range');return result

def rationals(obj, names):
    return {k:rational(obj[k]) for k in names.split()}

def word(value, length=None, min_length=2, max_length=80):
    require(type(value) is str and min_length <= len(value) <= max_length and set(value) <= {'0','1'}, 'invalid stored binary word')
    require(length is None or len(value)==length, 'word length mismatch')
    return value

def array(value, length):
    require(type(value) is list and len(value)==length,'array length/type mismatch');return value

def counts(value):
    """Count transitions in this already-recorded word only; no new words."""
    value=word(value);j=[0]*4;c=[0]*4
    for i in range(2,len(value)):
        s=2*int(value[i-2])+int(value[i-1]);j[s]+=1;c[s]+=int(value[i])
    return j,c,2*int(value[-2])+int(value[-1])

def vector(value,length=4,kind='rational'):
    array(value,length)
    return [(integer(x) if kind=='integer' else rational(x)) for x in value]

def strict_json(text):
    require(type(text) is str and len(text.encode('utf-8')) <= MAX_LINE,'JSON line too long')
    def pairs(items):
        result={}
        for k,v in items:
            require(k not in result,'duplicate JSON object key');result[k]=v
        return result
    def parse_integer(s):
        require(len(s.lstrip('-')) <= MAX_INTEGER_DIGITS,'JSON integer too long');return int(s)
    def reject_float(s):raise VerificationError('JSON floats and nonfinite values are forbidden')
    try: value=json.loads(text,object_pairs_hook=pairs,parse_int=parse_integer,parse_float=reject_float,parse_constant=reject_float)
    except (ValueError,RecursionError) as exc:raise VerificationError('invalid strict JSON: '+str(exc)) from exc
    budget=[0]
    def inspect(x,depth):
        budget[0]+=1;require(depth<=16 and budget[0]<=20000,'JSON resource limit')
        if type(x) is dict:
            require(len(x)<=128,'too many object keys')
            for k,v in x.items():require(len(k)<=128,'JSON key too long');inspect(v,depth+1)
        elif type(x) is list:
            require(len(x)<=4096,'JSON array too long')
            for v in x:inspect(v,depth+1)
        elif type(x) is str:require(len(x)<=1024,'JSON string too long')
    inspect(value,0);return value

class SafeRoot:
    """Descriptor-relative POSIX reads, refusing every symlink component."""
    def __init__(self,root):
        require(hasattr(os,'O_NOFOLLOW') and os.open in os.supports_dir_fd,'safe POSIX descriptor reads unavailable')
        self.fd=None
        absolute=os.path.abspath(os.fspath(root));fd=None
        try:
            fd=os.open('/',os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
            for part in absolute.split('/')[1:]:
                if not part:continue
                nxt=os.open(part,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd);os.close(fd);fd=nxt
            self.fd=fd
        except (OSError,ValueError) as exc:
            if fd is not None:os.close(fd)
            raise VerificationError('root is not an accessible non-symlink directory') from exc
    def __enter__(self):return self
    def __exit__(self,*args):
        if self.fd is not None:os.close(self.fd);self.fd=None
    def open(self,path):
        require(type(path) is str and path and not path.startswith('/') and '\\' not in path,'unsafe input path')
        pieces=path.split('/');require(all(x not in ('','.','..') and '\x00' not in x for x in pieces),'unsafe input path component')
        fd=None;f=None
        try:
            fd=os.dup(self.fd)
            for p in pieces[:-1]:
                nxt=os.open(p,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd);os.close(fd);fd=nxt
            f=os.open(pieces[-1],os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,dir_fd=fd)
            info=os.fstat(f);require(stat.S_ISREG(info.st_mode) and info.st_size<=MAX_FILE,'input not a bounded regular file')
            result=os.fdopen(f,'rb');f=None;return result
        except (OSError,ValueError,TypeError) as exc:
            raise VerificationError('unsafe or unreadable input: '+path) from exc
        finally:
            if fd is not None:os.close(fd)
            if f is not None:os.close(f)

def validate_family(o):
    fields(o,'P P2 assertions conditional_KL_coefficients conditional_forward_edge_counts full_KL_coefficients h hp inputs path_probabilities path_total pi reverse_P reverse_P2 reverse_expected_occupation terminal_00_probability')
    i=o['inputs'];fields(i,'N t tp u w');n=integer(i['N'],2,7);require(n in (2,3,4,7),'family N out of scope')
    z=rationals(i,'t tp u w');require(all(0<x<1 for x in z.values()),'family input range')
    require(z['u']+3*z['w']==1,'saved stationary weights')
    for name in ('P','P2','reverse_P','reverse_P2'):
        for row in array(o[name],4):require(sum(probability(x) for x in array(row,4))==1,'saved matrix row sum')
    for row in array(o['conditional_forward_edge_counts'],4):require(all(x>=0 for x in vector(row)),'negative saved edge count')
    require([probability(x) for x in array(o['pi'],4)]==[z['u'],z['w'],z['w'],z['w']],'saved pi weights');probability(o['h']);probability(o['hp'])
    occ=vector(o['reverse_expected_occupation']);require(all(x>=0 for x in occ) and sum(occ)==n-2,'saved occupation sum')
    require(vector(o['conditional_KL_coefficients'],2)==occ[:2],'saved conditional coefficient equality')
    array(o['full_KL_coefficients'],2)
    require(o['full_KL_coefficients']==['(N-2)*u='+str((n-2)*z['u']),'(N-2)*w='+str((n-2)*z['w'])],'saved full coefficient equality')
    require(o['assertions']=='PASS','invalid saved assertion status')
    paths=o['path_probabilities'];require(type(paths) is list and len(paths)=={2:4,3:8,4:16,7:128}[n],'saved embedded path count')
    seen=set();tot=Fraction(0);qtot=Fraction(0);end=Fraction(0)
    for p in paths:
        fields(p,'P Q terminal word');w=word(p['word'],n);require(w not in seen,'duplicate embedded word');seen.add(w)
        require(p['terminal']==w[-2:],'saved path terminal');a=probability(p['P']);b=probability(p['Q']);tot+=a;qtot+=b
        if p['terminal']=='00':end+=a
    require(tot==rational(o['path_total'])==1 and qtot==1,'saved path probability sums')
    require(end==rational(o['terminal_00_probability'])==z['u'],'saved terminal probability sum')
    return [i['u'],i['t'],i['tp'],n]

def validate_exact(o):
    fields(o,'N word J C K error upper');n=integer(o['N'],3,9);w=word(o['word'],n);j,c,q=counts(w)
    require(integer(o['J'])==j[q] and integer(o['C'])==c[q],'stored word counts mismatch')
    require(integer(o['K']) in (1,2,3,4,8),'unsupported K')
    e=rational(o['error']);b=rational(o['upper']);require(0<=e<=1 and e<=b,'saved error/bound fails')
    return [n,w,o['K']]

SPLINE_RATIONALS='A A0 Aclip B H_K P_hq P_zH absolute_error bound_first bound_second bound_total e_h e_q e_r h h_prime network_output q q_prime r r_prime z'
def validate_spline(o):
    fields(o,SPLINE_RATIONALS+' C C_all J K N case_index m passed shifts_tenths terminal_query word')
    n=integer(o['N'],3,7);require(integer(o['m'])==n-2,'m mismatch');m=n-2
    array(o['word'],n);require(all(type(x) is int and x in (0,1) for x in o['word']),'invalid integer word')
    w=''.join(str(x) for x in o['word']);j,c,q=counts(w)
    array(o['terminal_query'],2);require(all(type(x) is int for x in o['terminal_query']) and o['terminal_query']==o['word'][-2:],'terminal query mismatch')
    require(integer(o['J'])==j[q] and integer(o['C'])==c[q] and integer(o['C_all'])==sum(c),'stored word counts mismatch')
    k=integer(o['K'],1,4);idx=integer(o['case_index'],0,27);sh=array(o['shifts_tenths'],3)
    require(all(type(x) is int and -1<=x<=1 for x in sh),'invalid saved shifts')
    require(sh==([0,0,0] if idx==0 else [(idx-1)//9-1,((idx-1)//3)%3-1,(idx-1)%3-1]),'case index/shift mismatch')
    a=rationals(o,SPLINE_RATIONALS)
    for key in ('q','r','h','q_prime','r_prime','h_prime','B','network_output'):require(0<=a[key]<=1,'saved port range')
    require(a['A']==Fraction(o['C'],m) and a['B']==Fraction(o['C']+1,o['J']+2),'stored A/B ratio')
    require(a['q']==Fraction(sum(c)+c[q],m+j[q]) and a['r']==Fraction(sum(c),m) and a['h']==Fraction(j[q],m),'stored port ratios')
    for name in ('q','r','h'):require(a['e_'+name]==abs(a[name+'_prime']-a[name]),'saved port error mismatch')
    require(a['bound_first']>=0 and a['bound_second']>=0 and a['bound_total']==a['bound_first']+a['bound_second'],'saved bound sum')
    require(a['absolute_error']==abs(a['network_output']-a['B']),'saved absolute error')
    require(boolean(o['passed'])==(a['absolute_error']<=a['bound_total']) and o['passed'],'saved pass status/bound mismatch')
    return [n,o['word'],k,idx]

def validate_worlds(o):
    fields(o,'cases equal_prior_lower rng');require(boolean(o['rng']) is False,'unexpected RNG status');array(o['cases'],2);key=[];probs=[]
    for c in o['cases']:
        fields(c,'word theta_11 stationary_pi factors trajectory_probability terminal J C r old_successor recent_successor add_half_output')
        w=word(c['word'],8);j,cc,q=counts(w);require(vector(c['J'],4,'integer')==j and vector(c['C'],4,'integer')==cc,'two-world counts mismatch')
        require(c['terminal']==w[-2:],'two-world terminal mismatch');pi=[probability(x) for x in array(c['stationary_pi'],4)];require(sum(pi)==1,'stationary probabilities')
        factors=array(c['factors'],6);prob=pi[STATES.index(w[:2])]
        for index,f in enumerate(factors,2):
            fields(f,'context outcome probability');require(f['context']==w[index-2:index] and integer(f['outcome'],0,1)==int(w[index]),'stored factor context mismatch');prob*=probability(f['probability'])
        require(prob==probability(c['trajectory_probability']),'saved factor product mismatch');probs.append(prob)
        require(vector(c['old_successor'],2,'integer')==[cc[0]+cc[1],cc[2]+cc[3]],'old successor count')
        require(vector(c['recent_successor'],2,'integer')==[cc[0]+cc[2],cc[1]+cc[3]],'recent successor count')
        require(rational(c['r'])==Fraction(sum(cc),6),'stored pooled ratio')
        require(probability(c['add_half_output'])==Fraction(2*cc[q]+1,2*j[q]+2),'stored add-half output')
        probability(c['theta_11']);key.append(w)
    require(len(set(key))==2,'duplicate world words')
    require(rational(o['equal_prior_lower'])==min(probs)/4,'saved equal-prior lower consistency')
    return key

def validate_collision(o,independent=False):
    if independent:
        fields(o,'B_a B_b C_a C_all C_b J d fidelity_lower_bound gamma h k m max_port_error n passed q_a q_b q_mid query r word_a word_b')
        names=('word_a','word_b','C_a','C_b','C_all','q_a','q_b','max_port_error','fidelity_lower_bound')
    else:
        fields(o,'C1 C2 J collision_radius d gamma k m minimax_fidelity_lower n pooled_ones q1 q2 word1 word2')
        names=('word1','word2','C1','C2','pooled_ones','q1','q2','collision_radius','minimax_fidelity_lower')
    wa,wb,ca,cb,total,qa,qb,err,lb=names
    n=integer(o['n'],1,8);k=integer(o['k'],0,8);d=integer(o['d'],1,n);a=word(o[wa]);b=word(o[wb]);ja,cc_a,s=counts(a);jb,cc_b,t=counts(b)
    require(s==t==0 and len(a)==len(b),'collision word terminal/length')
    require(integer(o['m'])==len(a)-2 and integer(o['J'])==ja[s]==jb[t],'collision stored counts')
    require(integer(o[ca])==cc_a[s] and integer(o[cb])==cc_b[t] and integer(o[total])==sum(cc_a)==sum(cc_b),'collision saved successor counts')
    require(o['m']==6*n+3+2*k and o['J']==2*n+1 and o[cb]-o[ca]==d,'collision saved parameter/count relations')
    gamma=rational(o['gamma']);require(gamma in ((Fraction(1,10),Fraction(1,2),Fraction(1),Fraction(3),Fraction(10)) if independent else (Fraction(1,2),Fraction(1),Fraction(3))),'collision gamma out of scope')
    q1=probability(o[qa]);q2=probability(o[qb]);e=rational(o[err]);lower=rational(o[lb]);require(e==(q2-q1)/2>0 and lower==Fraction(o[cb]-o[ca],2*(o['J']+2)),'saved collision error/lower bound')
    require(q1==(o[total]+gamma*o[ca])/(o['m']+gamma*o['J']) and q2==(o[total]+gamma*o[cb])/(o['m']+gamma*o['J']),'saved collision port ratios')
    if independent:
        require(o['query']=='00' and boolean(o['passed']) is True,'saved collision status')
        require(rational(o['q_mid'])==(q1+q2)/2 and rational(o['h'])==Fraction(o['J'],o['m']) and rational(o['r'])==Fraction(o[total],o['m']),'saved midpoint or common ratios')
        require(rational(o['B_a'])==Fraction(o[ca]+1,o['J']+2) and rational(o['B_b'])==Fraction(o[cb]+1,o['J']+2),'saved B ratios')
    return [n,k,d,o['gamma'],a,b]

def validate_positionwise(o):
    fields(o,'W d e_beta fidelity_lower_bound k midpoint n passed q_a q_b required_q_error row_occupancies word_a word_b')
    n=integer(o['n'],1,8);k=integer(o['k'],0,8);d=integer(o['d'],1,n);a=word(o['word_a']);b=word(o['word_b']);ja,ca,qa=counts(a);jb,cb,qb=counts(b)
    fields(o['row_occupancies'],'00 01 10 11');require([integer(o['row_occupancies'][s]) for s in STATES]==ja==jb,'positionwise occupancy mismatch')
    require(qa==qb==0 and cb[0]-ca[0]==d,'positionwise recorded word relation')
    z=rationals(o,'W e_beta fidelity_lower_bound midpoint q_a q_b required_q_error');require(z['W']>0 and z['e_beta']>1,'saved weight range')
    require(z['midpoint']==(z['q_a']+z['q_b'])/2 and z['required_q_error']==(z['q_b']-z['q_a'])/2>0,'saved positionwise midpoint/error')
    require(z['fidelity_lower_bound']==Fraction(d,2*(ja[0]+2)) and boolean(o['passed']) is True,'saved positionwise lower/status')
    require(0<=z['q_a']<=1 and 0<=z['q_b']<=1,'saved positionwise probability range')
    return [n,k,d,o['e_beta'],a,b]

def validate_refined(o):
    fields(o,'C J bound9 error gamma shifts word');w=word(o['word'],min_length=3,max_length=7);j,c,q=counts(w)
    require(integer(o['J'])==j[q] and integer(o['C'])==c[q],'refined saved counts')
    sh=array(o['shifts'],3);require(all(type(x) is int and -1<=x<=1 for x in sh),'refined saved shifts')
    require(rational(o['gamma']) in (Fraction(1,2),Fraction(1),Fraction(3)),'refined gamma')
    e=rational(o['error']);require(0<=e<=1,'refined saved error range')
    require(e<=rational(o['bound9']),'refined saved error/bound; all retained rows have a non-null bound')
    return [w,o['gamma'],sh]

def terminal_group_key(o):return [o['terminal'],o['J'],o['C_total'],o['A'],o['B']]
def validate_terminal(o):
    fields(o,'A B B_values C_by_state C_total F_any_start F_fixed_start J N alpha heads radius start terminal word')
    n=integer(o['N'],3,8);w=word(o['word'],n);j,c,q=counts(w)
    require(vector(o['J'],4,'integer')==j and vector(o['C_by_state'],4,'integer')==c,'terminal saved word counts')
    require(integer(o['start'],0,3)==STATES.index(w[:2]) and integer(o['terminal'],0,3)==q,'terminal endpoints')
    require(integer(o['C_total'])==sum(c) and integer(o['A'])==c[0]+c[1] and integer(o['B'])==c[0]+c[2] and integer(o['alpha'])==1,'terminal saved margins')
    for name in ('F_any_start','F_fixed_start'):
        xs=o[name];require(type(xs) is list and 1<=len(xs)<=n,'terminal stored candidate list')
        require(all(type(x) is int and 0<=x<=j[0] for x in xs) and xs==sorted(set(xs)) and c[0] in xs,'terminal saved candidate values')
    require(set(o['F_fixed_start'])<=set(o['F_any_start']),'fixed-start containment')
    vals=[probability(x) for x in array(o['B_values'],len(o['F_any_start']))]
    require(rational(o['radius'])==(max(vals)-min(vals))/2,'saved radius equality')
    for index,head in enumerate(array(o['heads'],2)):
        fields(head,'D exp_beta matching_C matching_J q recovered');mj=integer(head['matching_J']);mc=integer(head['matching_C']);e=rational(head['exp_beta']);d=rational(head['D']);p=probability(head['q']);r=rational(head['recovered'])
        matching=[s for s in range(4) if (s//2 if index==0 else s%2)==int(w[-2+index])]
        require(mj==sum(j[s] for s in matching) and mc==sum(c[s] for s in matching),'saved head counts')
        require(e==(Fraction(2) if index==0 else Fraction(1,2)) and d>0 and r==mc,'saved head parameters')
        require(d*p==e*mc+(sum(c)-mc)/e,'saved weighted-average equality')
    return [n,w]

def validate_record(kind,obj):
    validators={'family':validate_family,'exact':validate_exact,'spline':validate_spline,'worlds':validate_worlds,'collision':validate_collision,'port_collision':lambda o:validate_collision(o,True),'positionwise':validate_positionwise,'refined':validate_refined,'terminal_paths':validate_terminal}
    require(kind in validators,'unknown record kind')
    try:return validators[kind](obj)
    except VerificationError:raise
    except (KeyError,TypeError,IndexError,ValueError,ZeroDivisionError) as exc:raise VerificationError('invalid '+kind+' record') from exc

TSV_FIELDS='N path terminal J00 J01 J10 J11 C00 C01 C10 C11 C_first0 C_first1 C_second0 C_second1 previous_same_key trigger'.split()
def canonical_int_text(value,low=0,high=1000000):
    require(type(value) is str and re.fullmatch(r'0|[1-9][0-9]*',value) is not None and len(value)<=8,'invalid TSV integer');return integer(int(value),low,high)

def lines(stream):
    total=0
    while True:
        raw=stream.readline(MAX_LINE+1)
        if not raw:break
        total+=len(raw);require(total<=MAX_FILE and len(raw)<=MAX_LINE,'input size/line limit')
        require(raw.endswith(b'\n') and raw.strip(),'blank or unterminated record')
        try:yield raw.decode('utf-8')
        except UnicodeDecodeError as exc:raise VerificationError('invalid UTF-8') from exc

def key_encoding(key):return json.dumps(key,ensure_ascii=True,sort_keys=True,separators=(',',':'))

def validate_stream(kind,stream):
    digest=hashlib.sha256();seen=set();count=0;embedded=0;groups={};fixed={};terminal_records=[];duplicate_inputs=0;tsv_seen={};trigger_count=0
    def accept(key):
        nonlocal count
        encoded=key_encoding(key);require(encoded not in seen,'duplicate retained record key');seen.add(encoded);digest.update((encoded+'\n').encode());count+=1;require(count<=MAX_RECORDS,'record limit')
    if kind in ('buggy','corrected'):
        reader=csv.reader(lines(stream),delimiter='\t',strict=True)
        try:header=next(reader)
        except StopIteration:raise VerificationError('missing TSV header')
        require(header==TSV_FIELDS,'TSV header mismatch')
        for row in reader:
            require(len(row)==len(header),'TSV column count');o=dict(zip(header,row));n=canonical_int_text(o['N'],7,8);w=word(o['path'],n);j,c,q=counts(w)
            require(canonical_int_text(o['terminal'],0,3)==q,'TSV terminal mismatch')
            require([canonical_int_text(o['J'+s]) for s in STATES]==j and [canonical_int_text(o['C'+s]) for s in STATES]==c,'TSV word counts mismatch')
            marg=[c[0]+c[1],c[2]+c[3],c[0]+c[2],c[1]+c[3]]
            require([canonical_int_text(o[k]) for k in ('C_first0','C_first1','C_second0','C_second1')]==marg,'TSV saved margins')
            group=(n,q,tuple(j),*marg);previous=tsv_seen.get(group);require(o['previous_same_key']==('' if previous is None else previous[0]),'TSV previous saved key')
            trigger=canonical_int_text(o['trigger'],0,1);trigger_count+=trigger
            if kind=='corrected':require(trigger==int(previous is not None and previous[1][q]!=c[q]),'corrected saved trigger inconsistent')
            # Deliberately do not require the discarded buggy scientific predicate to be true.
            require(trigger_count<=1,'multiple recorded stopping triggers');require(not trigger_count or trigger==1,'rows after a stopping trigger')
            tsv_seen[group]=(w,c);accept([n,w])
        require(trigger_count==1,'missing final saved stopping marker')
    elif kind=='worlds':
        raw=stream.read(MAX_LINE+1);require(len(raw)<=MAX_LINE,'JSON document too long')
        try:o=strict_json(raw.decode('utf-8'))
        except UnicodeDecodeError as exc:raise VerificationError('invalid UTF-8') from exc
        key=validate_record(kind,o)
        for w in key:accept([w])
    else:
        for line in lines(stream):
            o=strict_json(line);key=validate_record(kind,o);accept(key)
            if kind=='family':embedded+=len(o['path_probabilities'])
            if kind=='spline' and o['case_index']==14:duplicate_inputs+=1
            if kind=='terminal_paths':
                g=key_encoding(terminal_group_key(o));f=key_encoding([terminal_group_key(o),o['start']]);groups.setdefault(g,set()).add(o['C_by_state'][0]);fixed.setdefault(f,set()).add(o['C_by_state'][0]);terminal_records.append((g,f,o['F_any_start'],o['F_fixed_start']))
        if kind=='terminal_paths':
            for g,f,a,b in terminal_records:require(set(a)==groups[g] and set(b)==fixed[f],'saved feasibility set differs from retained-word group')
    return {'records':count,'ordered_key_sha256':digest.hexdigest(),'embedded_paths':embedded,'deliberate_duplicate_inputs':duplicate_inputs,'discarded_history':kind=='buggy'}

# Filled from retained input keys, never by generating a scientific case space.
FILE_SPECS = [{'path': 'v10_research/independent_arch_spline_review_20261103_1226/perturbation_cases_v2.jsonl',
  'kind': 'spline',
  'records': 27776,
  'ordered_key_sha256': '5135ef0e0c7323fd7f899d47c2ae144f38e34f57db1e80ee62485cbbf3513802',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 992,
  'discarded_history': False},
 {'path': 'v10_research/independent_port_collision_20261103_1256/exact_cases.jsonl',
  'kind': 'port_collision',
  'records': 1620,
  'ordered_key_sha256': 'fd5fe6fbff7eaaecaf2675d6e9e858e55f131ed5351fdabe2f5a56ced0884c5a',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/independent_port_collision_20261103_1256/positionwise_cases.jsonl',
  'kind': 'positionwise',
  'records': 1620,
  'ordered_key_sha256': '091cbc3ade6247d7011fe5057660c6ebf15885c0a5fa7cae83d1dc2659cd4d94',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/independent_route_b_review_20261103_1226/buggy_replay.tsv',
  'kind': 'buggy',
  'records': 9,
  'ordered_key_sha256': 'bd532512530d4664a7da3dc189ff6c127d065519069babb861123e0cb4eddd6f',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': True},
 {'path': 'v10_research/independent_route_b_review_20261103_1226/corrected_replay.tsv',
  'kind': 'corrected',
  'records': 168,
  'ordered_key_sha256': 'bfce60525b3caa0741bc3c2805892475fecdf895223412e4206037880e5b938e',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/independent_route_b_review_20261103_1226/two_worlds.json',
  'kind': 'worlds',
  'records': 2,
  'ordered_key_sha256': '6f43d0330e694b27ffcd341e50e0cec8dae771e13be6ad53a5eaac039243b23c',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/independent_terminal_port_review_20261103_1259/paths.jsonl',
  'kind': 'terminal_paths',
  'records': 504,
  'ordered_key_sha256': 'd6ce1f9cfe540a98989a5814bb5d83cbf8ef0a7139781c55d4ff9a9093be6fc5',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/rare_fast_mixing_family_audit_20261103_1211/cases_v1.jsonl',
  'kind': 'family',
  'records': 16,
  'ordered_key_sha256': '489d35c5534dc92170cc18fa4636e9628cab16adcdcbd80465f57955f1bdaf42',
  'embedded_paths': 624,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/rare_fast_mixing_family_audit_20261103_1211/cases_v2.jsonl',
  'kind': 'family',
  'records': 16,
  'ordered_key_sha256': '489d35c5534dc92170cc18fa4636e9628cab16adcdcbd80465f57955f1bdaf42',
  'embedded_paths': 624,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/route_a_rare_soft_threshold_20261103_1255/cases.jsonl',
  'kind': 'collision',
  'records': 972,
  'ordered_key_sha256': 'db0c089eaabfbe3d5bb97a6a1b83cb4eec0c8f637e7f1ef87d42afc8f717f4b1',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/route_a_rare_soft_threshold_20261103_1255/refined_port_cases.jsonl',
  'kind': 'refined',
  'records': 20088,
  'ordered_key_sha256': 'd15d1ee3b6f9e6c17b444bc726e0db365114737e37d625c69bcbcefc0a29af13',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/route_a_terminal_inference_20261103_1223/exact_cases.jsonl',
  'kind': 'exact',
  'records': 5080,
  'ordered_key_sha256': 'a9b57c97eb5bc743ae827c2a01ebe174d422b60049e830379fd72bb980f1d324',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False},
 {'path': 'v10_research/route_b_finite_prefix_20261103_1223/buggy_replay.tsv',
  'kind': 'buggy',
  'records': 9,
  'ordered_key_sha256': 'bd532512530d4664a7da3dc189ff6c127d065519069babb861123e0cb4eddd6f',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': True},
 {'path': 'v10_research/route_b_finite_prefix_20261103_1223/corrected_replay.tsv',
  'kind': 'corrected',
  'records': 168,
  'ordered_key_sha256': 'bfce60525b3caa0741bc3c2805892475fecdf895223412e4206037880e5b938e',
  'embedded_paths': 0,
  'deliberate_duplicate_inputs': 0,
  'discarded_history': False}]

def verify_records(root):
    """Return a deterministic report. Read fixed data paths only; write nothing."""
    require(FILE_SPECS,'no frozen file specification');results=[]
    with SafeRoot(root) as safe:
        for spec in FILE_SPECS:
            with safe.open(spec['path']) as stream:
                before=os.fstat(stream.fileno());result=validate_stream(spec['kind'],stream);after=os.fstat(stream.fileno())
                require((before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns),'input changed while reading')
            for key in ('records','ordered_key_sha256','embedded_paths','deliberate_duplicate_inputs','discarded_history'):
                require(result[key]==spec[key],spec['path']+': frozen coverage mismatch: '+key)
            results.append({'path':spec['path'],'kind':spec['kind'],**result})
    return {'status':'PASS_RETAINED_RECORD_CONSISTENCY_ONLY','not_a_formal_proof':True,'no_scientific_case_generation':True,'files':results,'total_file_records':sum(x['records'] for x in results),'scope':'Typed saved records, exact retained input-key coverage, recorded-word counts, elementary saved-field consistency. No archived code execution, theorem verification, matrix/model recomputation, or new experimental cases. Discarded buggy records are preserved history.'}

def main(argv=None):
    args=sys.argv[1:] if argv is None else argv
    if len(args)!=1:
        print(json.dumps({'status':'ERROR','error':'usage: verify_retained_records.py PUBLIC_ROOT'}));return 2
    try:report=verify_records(args[0])
    except (VerificationError,OSError,csv.Error) as exc:
        print(json.dumps({'status':'FAIL','error':str(exc)},sort_keys=True));return 1
    print(json.dumps(report,sort_keys=True,indent=2));return 0

if __name__=='__main__':sys.exit(main())
