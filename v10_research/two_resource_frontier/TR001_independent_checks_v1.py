"""Independent finite scalar diagnostics; not formal verification."""
from pathlib import Path
from decimal import Decimal as D, getcontext, ROUND_CEILING
import hashlib, json
getcontext().prec=65
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
ONE=D(1)
def W(z,t): return (ONE+(ONE+z/t).ln())/z
def le(x,y): assert x<=y+D('1e-58')*max(ONE,abs(x),abs(y)),(x,y)
counts={'source_hashes':0,'legal_surface_points':0,'A':0,'B':0,'C':0,'D':0,'threshold_implications':0,'allocations':0,'scalar_necessity':0,'scalar_sufficiency':0,'kl':0}
for e in json.loads((HERE/'TR001_source_bindings_v1.json').read_text())['sources']:
    assert hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest()==e['sha256']
    counts['source_hashes']+=1
Ms=sorted(set([64,65,80,127,128,255,256,257,511,512,4095,4096,4097]+[2**p for p in range(6,81,3)]))
for mi in Ms:
    m=D(mi); a=m.sqrt(); s=ONE/a
    betas=sorted(set([D(0),ONE/(2*m),ONE/m,2/m,D(1)/32,D(1)/16-D('1e-15'),D(1)/16,D(1)/16+D('1e-15'),D(1)/2,ONE]))
    for beta in betas:
        t=max(ONE,m*beta); f=ONE+(ONE+a/t).ln(); star=a*f
        for h in sorted(set([4,5,6,10,max(4,mi.bit_length()//2),max(4,3*mi.bit_length()//4),mi.bit_length(),mi.bit_length()+8])):
            q=D(2**h)
            for ki in [1,2,3,7,31,256,2**40]:
                zi=2**h*ki; z=D(zi); w=W(z,t); counts['legal_surface_points']+=1
                assert max(s,ONE/q,w)<D(1)/4
                # Every applicable branch, not only first one.
                if beta>D(1)/16:
                    le(w,ONE/q+2*s); counts['A']+=1
                if 4*zi>mi:
                    le(w,D(9)/2*s); counts['B']+=1
                if zi**4>mi**3:
                    le(w,3*s); counts['C']+=1
                if beta<=D(1)/16 and 4*zi<=mi and zi**4<=mi**3:
                    x=z/t; y=m/z
                    le(x,z); le(z,y**3)
                    L=(ONE+min(x,y)/8).ln()/z
                    le((ONE+x).ln(),24*(ONE+min(x,y)/8).ln())
                    le(w,ONE/q+24*L); counts['D']+=1
                for B in [ONE,D(2),D(8),D(64),D(1000)]:
                    if w<=B/a:
                        le(star/B**2,z); counts['threshold_implications']+=1
        # Legal integer/dyadic sufficient allocation, computed without binary logs.
        qi=16
        while D(qi)<a: qi*=2
        q=D(qi); k=max(1,int((star/q).to_integral_value(rounding=ROUND_CEILING)))
        assert a<=q<=2*a and q*k>=star
        le(D(k),ONE+star/q); le(W(q*k,t),2/a)
        counts['allocations']+=1
    n=m+2; delta=ONE/(16*n.sqrt()); xx=2*delta
    kl=2*delta*((ONE+xx)/(ONE-xx)).ln()
    le(kl,16*delta**2); le(n*kl,ONE/16)
    le(s/256,ONE/(128*n.sqrt())); counts['kl']+=1
# Independently cover continuous generic dimensionless threshold variables,
# including v<1, v=1, u tiny, and extremely large u.
for ep in range(-50,51,2):
    u=D(10)**ep; f=ONE+(ONE+u).ln()
    for vp in range(-20,21):
        v=D(2)**vp; b=max(ONE,(ONE+(ONE+v*u).ln())/v)
        le(f/b**2,v); counts['scalar_necessity']+=1
    for mult in [D('0.0001'),D('.1'),ONE,D(2),D(100),D(10)**20]:
        le(W(mult*f,ONE/u),2*max(ONE,ONE/mult))
        counts['scalar_sufficiency']+=1
report={'verdict':'PASS','arithmetic':'65-digit Decimal logarithms; exact Python integer domain predicates where applicable; comparison tolerance 1e-58 relative to max(1, magnitudes)','counts':counts,'candidate_sha256':hashlib.sha256((HERE/'TR001_two_resource_frontier_v1.md').read_bytes()).hexdigest(),'limits':'Finite checks corroborate scalar completion and threshold algebra only; do not test minimax risk or establish a universal proof.'}
(HERE/'TR001_independent_checks_v1.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
