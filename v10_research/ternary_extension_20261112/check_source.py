from fractions import Fraction as F
from itertools import product
import json
if not __debug__:
    raise RuntimeError('Assertions must be enabled')
f=[F(1),F(-1,2),F(-1,2)]
checks=paths=0
for h in (F(1,2),F(3,4)):
    for theta in (-h,F(0),h):
        def P(x,y,z): return (1+theta*f[x]*f[y]*f[z])/3
        for x,y in product(range(3),repeat=2):
            assert sum(P(x,y,z) for z in range(3))==1; checks+=1
        for y,z in product(range(3),repeat=2):
            assert sum(P(x,y,z)/9 for x in range(3))==F(1,9); checks+=1
        for x,y,u,v in product(range(3),repeat=4):
            assert P(x,y,u)*P(y,u,v)>=(1-h)**2/9; checks+=1
        for n in range(2,7):
            total=var=F(0)
            for word in product(range(3),repeat=n):
                prob=F(1,9)
                for j in range(n-2): prob*=P(*word[j:j+3])
                a=sum((-1)**j*f[word[j]] for j in range(n))/n
                b=sum(f[(word[j]+j)%3] for j in range(n))/n
                total+=prob;var+=prob*(a*a+b*b);paths+=1
            assert total==1;checks+=1
            assert var<=2*(1+16/(1-h)**2)/n;checks+=1
    gap=sum(h*abs(f[x]*f[y])*sum(abs(z) for z in f)/27 for x,y in product(range(3),repeat=2))
    assert gap==8*h/27;checks+=1
print(json.dumps({'assertions':checks,'enumerated_paths':paths,'arithmetic':'exact Fraction','status':'pass','scope':'source, mixing, heterogeneous-observable variance and TV separation; not architecture numerics'},indent=2))
