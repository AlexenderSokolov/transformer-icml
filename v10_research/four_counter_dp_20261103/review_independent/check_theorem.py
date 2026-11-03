from pathlib import Path
import itertools,importlib.util,sys
import numpy as np
sys.dont_write_bytecode=True;B=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('dp4',B/'four_counter.py');a=importlib.util.module_from_spec(s);s.loader.exec_module(a);sys.path.insert(0,str(B.parent/'learned_position_pilot_20261103'));import pilot
maps=words=witnesses=0;worst=0
for m in range(2,7):
 model=pilot.Model(203,'half');L=m//2;R=m-L
 for h in itertools.product((0,1),repeat=m+2):
  brute={}
  for mask in itertools.product((0,1),repeat=m):
   z=tuple(h[i]^mask[i] for i in range(m))+h[m:];sel=[(i,z[i+2]) for i in range(m) if z[i:i+2]==h[-2:]];bank=(len(sel),sum(c for i,c in sel),sum(i<L for i,c in sel),sum(c for i,c in sel if i<L));cost=sum(mask);brute[bank]=min(brute.get(bank,m+1),cost)
   J,C,D,E=bank;x=((J-C)/m,C/m,(D-E)/L,E/L,(J-D-C+E)/R,(C-E)/R,*h[-2:],1/m);real=model.forward(np.asarray([z],np.int8),cache=True)[1]['x'][0];worst=max(worst,float(np.max(abs(real-x))));words+=1
  for k in range(m+1):
   expected={v:c for v,c in brute.items() if c<=k};got=a.solve_banks(h,k,True);assert {v:c for v,(c,z) in got.items()}==expected
   for bank,(c,z) in got.items():
    assert z[-2:]==h[-2:] and sum(x!=y for x,y in zip(z,h))==c<=k;sel=[(i,z[i+2]) for i in range(m) if z[i:i+2]==h[-2:]];assert bank==(len(sel),sum(v for i,v in sel),sum(i<L for i,v in sel),sum(v for i,v in sel if i<L));witnesses+=1
   objective=lambda x:sum((i+1)*(v+1)**2 for i,v in enumerate(x)); val,z,bank=a.maximize(h,k,lambda x:objective(x));assert val==max(objective(a.model_inputs(m,h[-2:],b)) for b in expected);assert bank in expected;maps+=1
 print('M',m,'cumulative maps',maps,'input words',words,'witnesses',witnesses,flush=True)
print('PASS max numerical feature discrepancy',worst)
