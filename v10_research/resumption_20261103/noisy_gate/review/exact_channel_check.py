#!/usr/bin/env python3
"""Exact rational checks; corroboration only, not a proof of minimax claims."""
from fractions import Fraction as F
from itertools import product
from math import comb
import json

rows = []
for eta in (F(0), F(1,10), F(1,4), F(1,3), F(1,2)):
    for r in range(13):
        overlap = sum((F(comb(r,j)) * min(eta**j * (1-eta)**(r-j), eta**(r-j) * (1-eta)**j) for j in range(r+1)), F(0))
        tail = sum((F(comb(r,j)) * eta**j * (1-eta)**(r-j) for j in range(r+1) if 2*j > r), F(0))
        tie = F(comb(r,r//2)) * eta**(r//2) * (1-eta)**(r//2) if r % 2 == 0 else F(0)
        assert overlap == 2*tail + tie
        majority_error = tail + tie/2
        assert overlap == 2*majority_error
        if r <= 6:
            words = list(product((0,1), repeat=r))
            masses=[]
            for y in words:
                vals=[]
                for x in words:
                    d=sum(a!=b for a,b in zip(x,y))
                    vals.append(eta**d*(1-eta)**(r-d))
                masses.append(min(vals))
            assert sum(masses,F(0)) == (2*eta)**r
            assert all(v==eta**r for v in masses)
        assert overlap >= (2*eta)**r
        rows.append({'eta':str(eta),'R':r,'repetition_overlap':str(overlap),'majority_error':str(majority_error),'all_words_overlap':str((2*eta)**r)})
print(json.dumps({'status':'PASS','arithmetic':'fractions.Fraction exact rational','rows':rows},indent=2))
