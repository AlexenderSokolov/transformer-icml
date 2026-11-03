"""Validate update framing/checksums and optionally require the fixed complete run."""
import argparse
from collections import Counter
from experiment import CFG, read_update_records

def validate_records(records, complete=False):
 count=0;sequences=Counter();last={}
 for meta,grad,params in records:
  key=(meta['arm'],meta['seed']);step=meta['step']
  if step!=last.get(key,0)+1:raise ValueError(f'nonconsecutive step {key}: {step}')
  last[key]=step;sequences[key]+=1;count+=1
 if complete:
  expected={(arm,seed):2000 for seed in CFG['initialization_seeds'] for arm in ('corrected','rare_boost')}
  if len(expected)!=6 or CFG['optimization']['steps']!=2000:raise ValueError('unexpected fixed protocol seeds or budget')
  if dict(sequences)!=expected or count!=12000:raise ValueError(f'incomplete or unexpected journal: {count} records; per-fit counts {dict(sequences)}')
 return count,sequences,last

def main():
 p=argparse.ArgumentParser();p.add_argument('journal');p.add_argument('--complete',action='store_true',help='require all six fixed 2,000-record prepared sequences');args=p.parse_args()
 count,sequences,last=validate_records(read_update_records(args.journal),complete=args.complete)
 print(f'Validated {count} complete update records ({"all expected prepared records" if args.complete else "prefix integrity only"})')
 for key,n in sequences.items():print(f'{key[0]} seed {key[1]}: {n} records, last step {last[key]}')

if __name__=='__main__':main()
