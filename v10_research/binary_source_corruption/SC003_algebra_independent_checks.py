"""Exact finite diagnostics, independent of SC003 author script; not a proof."""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter
import json
row_cases = 0
for n,m,np,mp in product(range(9), repeat=4):
    j,jp=n+m,np+mp
    for B in (0,1,2,6,12):
        if abs(np-n)+abs(mp-m)>B: continue
        h=F(max(np-B,0),jp+B+2);v=F(n,j+2)
        assert 0<=h<=v
        assert v-h<=F(3*B,j+2)
        for q in (F(0),F(1,7),F(1,2),F(6,7),F(1)):
            A=4*B+2
            if j:
                p=F(n,j)
                assert 0<=p-h<=min(p,F(A,j+2))
                assert abs(h-q)<=2*abs(p-q)+min(q,F(A,j+2))
            else:
                assert h==0 and abs(h-q)<=min(q,F(A,2))
            row_cases+=1
word_cases=0
for M in range(1,8):
    for word in product((0,1), repeat=M+2):
        C=Counter(zip(word,word[1:],word[2:]));s=word[-2:];exit=1-s[0]
        n=C[s+(exit,)];m=C[s+(1-exit,)];j=n+m
        for k in range(min(M,3)+1):
            for r in range(k+1):
                for ix in combinations(range(M),r):
                    z=list(word)
                    for i in ix:z[i]^=1
                    z=tuple(z);D=Counter(zip(z,z[1:],z[2:]));np=D[s+(exit,)];mp=D[s+(1-exit,)];B=6*k
                    assert sum(abs(C[t]-D[t]) for t in set(C)|set(D))<=B
                    h=F(max(np-B,0),np+mp+B+2)
                    assert h<=F(n,j+2)
                    assert F(n,j+2)-h<=F(3*B,j+2)
                    assert z[-2:]==s
                    word_cases+=1
print(json.dumps({'status':'PASS','row_exact_rational_cases':row_cases,'full_word_exact_cases':word_cases,'orientations':{'00':1,'01':1,'10':0,'11':0}},indent=2))
