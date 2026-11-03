#!/usr/bin/env python3
"""Bounded read-only consistency checks of three retained numeric record files.

This is not scientific replay, a theorem check, or a practical fixed-word or
ordinary floating-softmax guarantee. It never imports archived programs,
reconstructs networks, enumerates words, advances chains, or regenerates results.
Saved input coverage is bound to ordered keys extracted from the frozen records.
Full output authenticity requires the enclosing archive's independent byte hashes.
Run on POSIX with Python 3.10+: python -I -B verify_retained_records.py PUBLIC_ROOT
"""
from fractions import Fraction
import hashlib
import json
import math
import os
import re
import stat
import sys

MAX_FILE = 512 * 1024
MAX_LINE = 16384
MAX_RECORDS = 1100
MAX_RATIONAL_DIGITS = 2048
MAX_RATIONAL_LENGTH = 4097
SENS = 'v10_research/route_a_sensitivity_bottleneck_20261103_1341/'
COMP = 'v10_research/route_a_bos_causal_compile_20261103_1411/'

class VerificationError(ValueError):
    """An input violates the declared archival consistency or safety checks."""

def require(condition, message):
    if not condition:
        raise VerificationError(message)

def integer(value, low=0, high=1000000):
    require(type(value) is int and low <= value <= high, 'invalid bounded integer')
    return value

def fields(value, names):
    require(type(value) is dict and set(value) == set(names.split()), 'unexpected or missing schema field')

def rational_string(value):
    require(type(value) is str and len(value) <= MAX_RATIONAL_LENGTH, 'invalid rational string size')
    require(re.fullmatch(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?', value) is not None, 'invalid rational string syntax')
    require(all(len(x.lstrip('-')) <= MAX_RATIONAL_DIGITS for x in value.split('/')), 'rational integer too long')
    try:
        result=Fraction(value)
    except (ValueError,ZeroDivisionError) as exc:
        raise VerificationError('invalid rational') from exc
    require(str(result)==value,'noncanonical rational string')
    return result

def rational_object(value):
    fields(value,'numerator denominator')
    n=integer(value['numerator'],-1000000000,1000000000)
    d=integer(value['denominator'],1,1000000000)
    require(math.gcd(n,d)==1,'noncanonical rational object')
    return Fraction(n,d)

def strict_json(raw):
    require(type(raw) is bytes and len(raw)<=MAX_LINE,'JSON line too long')
    def pairs(items):
        out={}
        for k,v in items:
            require(k not in out,'duplicate JSON object key');out[k]=v
        return out
    def parse_integer(s):
        require(len(s.lstrip('-'))<=64,'JSON integer too long');return int(s)
    def reject_number(s):
        raise VerificationError('floating and nonfinite JSON numbers are forbidden')
    try:
        out=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_int=parse_integer,parse_float=reject_number,parse_constant=reject_number)
    except (ValueError,UnicodeError,RecursionError) as exc:
        raise VerificationError('invalid strict JSON') from exc
    budget=[0]
    def inspect(value,depth):
        budget[0]+=1
        require(depth<=6 and budget[0]<=128,'JSON resource limit')
        if type(value) is dict:
            require(len(value)<=24,'too many JSON fields')
            for k,v in value.items():
                require(len(k)<=64,'JSON key too long');inspect(v,depth+1)
        elif type(value) is list:
            require(len(value)<=16,'JSON array too long')
            for v in value:inspect(v,depth+1)
        elif type(value) is str:
            require(len(value)<=MAX_RATIONAL_LENGTH,'JSON string too long')
    inspect(out,0)
    return out

class SafeRoot:
    """Descriptor-relative POSIX reads with no symlink component or special file."""
    def __init__(self,root):
        require(hasattr(os,'O_NOFOLLOW') and hasattr(os,'O_DIRECTORY') and os.open in os.supports_dir_fd,'safe POSIX file access unavailable')
        self.fd=None;fd=None
        try:
            root=os.fspath(root)
            require(type(root) is str and '\x00' not in root,'invalid root')
            # Reject parent traversals before normalization; do not conceal links.
            require('..' not in root.split('/'),'unsafe root parent traversal')
            absolute=root if root.startswith('/') else os.getcwd()+'/'+root
            fd=os.open('/',os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
            for part in absolute.split('/')[1:]:
                if part in ('','.'):continue
                nxt=os.open(part,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd)
                os.close(fd);fd=nxt
            self.fd=fd;fd=None
        except (OSError,ValueError,TypeError) as exc:
            raise VerificationError('root must be an accessible non-symlink directory') from exc
        finally:
            if fd is not None:os.close(fd)
    def __enter__(self):return self
    def __exit__(self,*unused):
        if self.fd is not None:os.close(self.fd);self.fd=None
    def read(self,relative):
        require(type(relative) is str and relative and not relative.startswith('/') and '\\' not in relative,'unsafe relative path')
        pieces=relative.split('/')
        require(all(p not in ('','.','..') and '\x00' not in p for p in pieces),'unsafe relative component')
        fd=None;file_fd=None
        try:
            fd=os.dup(self.fd)
            for part in pieces[:-1]:
                nxt=os.open(part,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd)
                os.close(fd);fd=nxt
            file_fd=os.open(pieces[-1],os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,dir_fd=fd)
            before=os.fstat(file_fd)
            require(stat.S_ISREG(before.st_mode) and before.st_size<=MAX_FILE,'input must be bounded regular file')
            chunks=[];total=0
            while True:
                block=os.read(file_fd,min(65536,MAX_FILE+1-total))
                if not block:break
                chunks.append(block);total+=len(block)
                require(total<=MAX_FILE,'input grew beyond size limit')
            after=os.fstat(file_fd)
            require((before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns,before.st_ctime_ns)==(after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns,after.st_ctime_ns),'input changed during read')
            require(total==before.st_size,'input size changed during read')
            return b''.join(chunks)
        except (OSError,ValueError,TypeError) as exc:
            raise VerificationError('unsafe or unreadable retained input') from exc
        finally:
            if file_fd is not None:os.close(file_fd)
            if fd is not None:os.close(fd)

def validate_population(row):
    fields(row,'u gamma Lq lambda loss_minus loss_plus population_opt')
    q={k:rational_string(v) for k,v in row.items()}
    require(row['u'] in ('1/16','1/8','3/16'),'population u outside retained scope')
    require(row['gamma'] in ('0','1/2','1','3','9'),'population gamma outside retained scope')
    require(row['Lq'] in ('0','1/2','1','2','5','20'),'population Lq outside retained scope')
    require(q['lambda']==q['gamma']*q['u']/(1+q['gamma']*q['u']),'saved population lambda equality')
    require(q['population_opt']==max(Fraction(0),1-q['Lq']*q['lambda'])/4,'saved population formula equality')
    require(q['loss_minus']==q['loss_plus']==q['population_opt'],'saved endpoint loss equality')
    require(0<=q['population_opt']<=Fraction(1,4),'saved population error range')
    return [row['u'],row['gamma'],row['Lq']]

def validate_reverse_moments(row):
    fields(row,'m u t mean_r var_r mean_J var_J all_bounds')
    m=integer(row['m'],512,768)
    require(m in (512,768) and row['u'] in ('1/8','3/16') and row['t'] in ('1/4','3/4'),'reverse moment inputs outside retained scope')
    q={k:rational_string(row[k]) for k in ('u','t','mean_r','var_r','mean_J','var_J')}
    v=m*q['u'];mu=2*(1-q['u'])/3
    require(v>=60,'saved occupancy scale')
    require(0<=q['mean_r']<=1 and 0<=q['mean_J']<=m,'saved mean ranges')
    require(abs(q['mean_r']-mu)<=Fraction(16,m) and 0<=q['var_r']<=Fraction(61,m),'saved pooled moment bounds')
    require(abs(q['mean_J']-v)<=15 and 0<=q['var_J']<=61*(v+15),'saved row moment bounds')
    require(row['all_bounds'] is True,'saved reverse bound status must be true')
    return [m,row['u'],row['t']]

def validate_no_bos(row):
    fields(row,'schema N bits eta b c terminal J C copy_max_error gates_exact head_output add_one absolute_error contamination_bound passed')
    require(row['schema']=='no_bos_all_words_v1','unrecognized saved schema')
    n=integer(row['N'],3,8);word=row['bits']
    require(type(word) is str and len(word)==n and set(word)<=set('01'),'invalid retained binary word')
    terminal=row['terminal']
    require(type(terminal) is list and len(terminal)==2 and all(type(x) is int and x in (0,1) for x in terminal),'invalid saved terminal')
    require(terminal==[int(x) for x in word[-2:]],'saved terminal/word equality')
    j=integer(row['J'],0,n-2);c_count=integer(row['C'],0,j)
    b=integer(row['b'],4,8);c=integer(row['c'],7,9)
    q={k:rational_object(row[k]) for k in ('eta','copy_max_error','head_output','add_one','absolute_error','contamination_bound')}
    eta=q['eta'];require(eta in (Fraction(1,4),Fraction(1,32)),'eta outside retained scope')
    require(2**(b-1)<n/eta<=2**b and 2**(c-1)<32*(n+1)<=2**c,'saved budget bounds')
    require(0<=q['copy_max_error']<=Fraction(1,32),'saved maximum-copy-error bound')
    require(row['gates_exact'] is True and row['passed'] is True,'saved gate or pass status must be true')
    require(0<=q['head_output']<=1 and 0<=q['add_one']<=1,'saved probability ranges')
    require(q['add_one']==Fraction(c_count+1,j+2),'saved add-one/count equality')
    require(q['absolute_error']==abs(q['head_output']-q['add_one']),'saved absolute-error equality')
    require(q['contamination_bound']==Fraction(n-1-j,2**b*(j+2)+n-1-j),'saved contamination/count equality')
    require(0<=q['absolute_error']<=q['contamination_bound']<=Fraction(n,2**(b+1))<=eta/2,'saved error/budget inequalities')
    # The stored counts, copy maximum and gate flag are not recomputed from a model.
    return [n,row['eta'],word]

FILES = (
    (SENS+'population_cases.jsonl',90,'65cbb8a525be743ddf679b842e2ec858687124d15d0cc9d8af17f3e8e40fe6d4',validate_population),
    (SENS+'reverse_moment_cases.jsonl',8,'66be101bf1cf65756a622f1686aef0a0bcc2e2d54509341eaa4bdc4444d5b084',validate_reverse_moments),
    (COMP+'exhaustive_cases_v1.jsonl',1008,'e60b46b652983099336a3bb3aa3718b7ea65be1b2e338a7a479387ce113482cc',validate_no_bos),
)

def verify_records(root):
    """Return archival check results; never write, execute sources, or rerun science."""
    results=[]
    with SafeRoot(root) as safe:
        for path,expected_count,expected_keys,validate in FILES:
            raw=safe.read(path)
            require(raw.endswith(b'\n'),'retained JSONL requires final newline')
            lines=raw.splitlines(keepends=True)
            require(len(lines)<=MAX_RECORDS,'too many saved records')
            keys=hashlib.sha256();seen=set();count=0
            for line in lines:
                require(line.strip(),'blank retained JSONL line')
                row=strict_json(line);key=validate(row)
                encoded=json.dumps(key,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')
                require(encoded not in seen,'duplicate retained input key')
                seen.add(encoded);keys.update(encoded+b'\n');count+=1
            require(count==expected_count,'retained record count mismatch')
            require(keys.hexdigest()==expected_keys,'retained ordered input coverage mismatch')
            results.append({'path':path,'records':count,'bytes':len(raw),'observed_sha256':hashlib.sha256(raw).hexdigest(),'ordered_input_sha256':keys.hexdigest()})
    return {'status':'PASS','scope':'retained-record consistency only; no scientific replay','total_records':sum(x['records'] for x in results),'files':results}

def main():
    if len(sys.argv)!=2:
        print('usage: python -I -B verify_retained_records.py PUBLIC_ROOT',file=sys.stderr);return 2
    try:
        result=verify_records(sys.argv[1])
    except VerificationError as exc:
        print('FAIL: '+str(exc),file=sys.stderr);return 1
    print(json.dumps(result,sort_keys=True,indent=2));return 0

if __name__=='__main__':
    sys.exit(main())
