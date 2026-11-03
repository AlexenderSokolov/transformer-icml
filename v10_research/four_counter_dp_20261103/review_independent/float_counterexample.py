"""Deterministic check: no PRNG or sampled words."""
from pathlib import Path
from fractions import Fraction
import importlib.util,sys
sys.dont_write_bytecode=True
path=Path(__file__).resolve().parents[1]/'four_counter.py'
spec=importlib.util.spec_from_file_location('four_counter',path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
h=(0,0,0,0,0); k=1
expected_bank=(1,0,0,0); banks=module.solve_banks(h,k,True);cost,witness=banks[expected_bank]
score,returned,bank=module.maximize(h,k,lambda x:int(x[0]==Fraction(1,3)))
assert witness==(0,1,0,0,0) and cost==1 and score==0 and bank[0]-bank[1]!=1
assert Fraction(bank[0]-bank[1],3)!=Fraction(1,3) and Fraction(expected_bank[0]-expected_bank[1],3)==Fraction(1,3)
print('h=00000 k=1: implementation returns', ''.join(map(str,returned)), 'score',score,'bank',bank)
print('exact rational utility optimum 1 attained by', ''.join(map(str,witness)), 'bank',expected_bank)
