from fractions import Fraction as F
from math import comb, floor, ceil, exp
import json

for M in (8, 64, 1024, 4096, 16384):
    n = M // 4
    k = M // 1024
    threshold = F(M,512)+2*k
    last = (threshold.numerator-1)//threshold.denominator
    for theta in (F(1,4),F(1,2),F(3,4)):
        for row in ('00','01','10','11'):
            p=F(1)
            for b in row:
                p *= theta if b=='1' else 1-theta
            mu=n*p
            assert mu >= F(M,128)
            assert threshold <= mu/2
            tail=sum((F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(min(last,n)+1)), F(0))
            bound=exp(-M/1024)
            assert float(tail)<=bound
            print(json.dumps({'M':M,'k':k,'theta':str(theta),'row':row,'p':str(p),'mu':str(mu),'strict_threshold':str(threshold),'exact_tail_float':float(tail),'bound':bound},sort_keys=True))
print('PASS: 60 deterministic exact-binomial checks')
