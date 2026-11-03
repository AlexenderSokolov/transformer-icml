"""Independent exact finite corroboration; no imports from author checkers."""
from itertools import product
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
T=HERE.parent
pairs=list(product(range(2), repeat=2))
triples=list(product(range(2), repeat=3))
counts=Counter()
witness=None
for length in range(2,15):
    by_obs={}
    for z in product(range(2), repeat=length):
        M=length-2
        h=Counter(tuple(z[i:i+3]) for i in range(M))
        out={u:sum(h[u+(c,)] for c in (0,1)) for u in pairs}
        inc={u:sum(h[(c,)+u] for c in (0,1)) for u in pairs}
        initial,final=z[:2],z[-2:]
        rec={u:out[u]-inc[u]+int(final==u) for u in pairs}
        assert rec=={u:int(initial==u) for u in pairs}
        direct=Counter(tuple(z[i:i+2]) for i in range(1,M+1))
        assert all(inc[u]==direct[u]==out[u]+int(final==u)-int(initial==u) for u in pairs)
        assert sum(inc.values())==M
        # Editing discarded first coordinate cannot change in-degree suffix counts.
        w=(1-z[0],)+z[1:]
        hh=Counter(tuple(w[i:i+3]) for i in range(M))
        assert all(sum(hh[(c,)+u] for c in (0,1))==inc[u] for u in pairs)
        counts['word_flow_reconstruction_suffix_and_first_edit_checks']+=1
        y=z[1:]; u=z[-1]
        J=sum(inc[(u,b)] for b in (0,1)); C=inc[(u,1-u)]
        jd=sum(y[i]==u for i in range(M)); cd=sum(y[i]==u and y[i+1]!=u for i in range(M))
        assert (J,C)==(jd,cd)
        half=sum(y[i]==u for i in range(M//2))
        bit=int(512*half>=J)
        decoded=Fraction(C,J) if J>0 and bit else Fraction(0)
        scanned=Fraction(cd,jd) if jd>0 and 512*half>=jd else Fraction(0)
        assert decoded==scanned
        counts['scan_bit_decoder_checks']+=1
        obs=(tuple(h[t] for t in triples),final)
        if obs in by_obs:
            old,oldbit=by_obs[obs]
            assert old[:2]==initial
            if witness is None and oldbit!=bit:
                witness={'first':old,'second':z,'first_bit':oldbit,'second_bit':bit}
        else: by_obs[obs]=(z,bit)
        for r in range(2,length+1):
            rp=min(r,M+1); m=min(rp-1,M//2)
            suffix=z[-(m+1):]
            O=J-sum(suffix[i]==u for i in range(m))
            directO=sum(y[i]==u for i in range(M-m))
            assert O==directO
            assert (Fraction(C,J) if J>0 and 512*O>=J else 0)==(Fraction(cd,jd) if jd>0 and 512*directO>=jd else 0)
            counts['raw_suffix_gate_checks']+=1
    counts['distinct_valid_observation_classes']+=len(by_obs)
# Verify all acceptance receipt and prior review SHA bindings against actual bytes.
receipt=json.loads((ROOT/'intake/FOT002_root_acceptance.json').read_text())
for rel,info in receipt['artifacts'].items():
    data=(T/rel).read_bytes()
    assert len(data)==info['bytes'] and hashlib.sha256(data).hexdigest()==info['sha256']
    counts['acceptance_receipt_artifact_bindings']+=1
bindings=json.loads((T/'interface_review/bindings.json').read_text())['files']
for rel,sha in bindings.items():
    p=ROOT.parent/rel
    assert hashlib.sha256(p.read_bytes()).hexdigest()==sha
    counts['prior_interface_review_bindings']+=1
result={'status':'PASS','arithmetic':'exact integers and fractions','word_lengths':[2,14],'M_range':[0,12],'counts':dict(counts),'same_baseline_different_scan_bit_witness':witness,'limits':'Finite checks corroborate universal telescoping; accepted stochastic bounds are not re-proved.'}
(HERE/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
