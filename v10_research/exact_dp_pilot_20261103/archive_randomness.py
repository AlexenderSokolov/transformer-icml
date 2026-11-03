#!/usr/bin/env python3
"""Replay original data draw exactly and archive every RNG state and uniform."""
import json,pathlib,numpy as np
D=pathlib.Path(__file__).resolve().parent
expected=json.loads((D/'data.json').read_text());rng=np.random.default_rng(845120); records=[]; ii=0
for m in [16,32,64,128]:
    for si,table in enumerate([[.5,.5,.5,.5],[.15,.5,.5,.85],[.03,.5,.5,.97]]):
        before_start=rng.bit_generator.state;start=int(rng.integers(0,4));before_uniforms=rng.bit_generator.state
        uniforms=[];states=[]; z=[start//2,start%2]
        for i in range(m):
            states.append(rng.bit_generator.state);u=float(rng.random(1)[0]);uniforms.append(u)
            row=2*z[-2]+z[-1];z.append(int(u<table[row]))
        word=''.join(map(str,z));old=expected[ii];ii+=1
        assert (word,start,table,m,si)==(old['word'],old['start_pair'],old['table'],old['M'],old['source_index'])
        records.append(dict(M=m,source_index=si,table=table,start_pair=start,word=word,before_start_state=before_start,before_uniforms_state=before_uniforms,before_each_uniform_states=states,uniforms=uniforms,after_uniforms_state=rng.bit_generator.state))
(D/'randomness_replayed.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS: all original histories, starts and tables reconstructed; all uniform draws and states archived')
