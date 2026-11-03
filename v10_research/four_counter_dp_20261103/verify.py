"""Independent exhaustive word and mask enumeration against selected-row DP."""
import itertools
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'learned_position_pilot_20261103'))
from pilot import Model
from four_counter import solve_banks, model_inputs, maximize


def brute_bank(z):
    m=len(z)-2; half=m//2; row=z[-2:]
    triples=[z[i:i+3] for i in range(m)]
    s=[(i,t) for i,t in enumerate(triples) if t[:2]==row]
    return len(s),sum(t[2] for _,t in s),sum(i<half for i,_ in s),sum(t[2] for i,t in s if i<half)


def main(max_m):
    nword=nmap=nwitness=0
    for m in range(2,max_m+1):
        model=Model(123,mode='half')
        for h in itertools.product((0,1),repeat=m+2):
            # Generate actual features independently via pilot, and brute edit-cost map.
            costs={}
            for mask in itertools.product((0,1),repeat=m):
                z=tuple(h[i]^mask[i] for i in range(m))+h[m:]
                bank=brute_bank(z); cost=sum(mask)
                costs[bank]=min(cost,costs.get(bank,m+1))
                x=model.forward(np.array([z]),cache=True)[1]['x'][0]
                if not np.allclose(x,model_inputs(m,h[-2:],bank),rtol=0,atol=1e-15):
                    raise AssertionError((m,h,z,x,bank))
                nword+=1
            for k in range(m+1):
                expected={b:c for b,c in costs.items() if c<=k}
                got=solve_banks(h,k,witnesses=True)
                assert {b:c for b,(c,_) in got.items()} == expected,(m,h,k)
                for b,(c,z) in got.items():
                    assert z[-2:]==h[-2:] and sum(x!=y for x,y in zip(z,h))==c and brute_bank(z)==b
                    nwitness+=1
                # Rational-valued fixed nonlinear readout; avoid floating-point ties.
                util=lambda x: (int(x[7])*11 + int(x[6])*7 + round(x[0]*m)*3
                    + round(x[1]*m)*5 + round(x[3]*(m//2))*13)**2
                value,z,b=maximize(h,k,util)
                assert value == max(util(model_inputs(m,h[-2:],b0)) for b0 in expected)
                assert brute_bank(z)==b
                nmap+=1
        print(f'M={m} passed',flush=True)
    print(f'PASS: {nmap} complete bank-map and objective comparisons; {nword} independent pilot input comparisons; {nwitness} reconstructed witnesses')

if __name__=='__main__': main(int(sys.argv[1]) if len(sys.argv)>1 else 6)
