from itertools import product
for M in range(1,12):
    groups=set()
    for x in product(range(2),repeat=M+2):
        C=[0]*8
        for i in range(M):C[4*x[i]+2*x[i+1]+x[i+2]]+=1
        a,b,c,d,e,f,g,h=C
        start=2*x[0]+x[1]; end=2*x[-2]+x[-1]
        delta=[int(end==j)-int(start==j) for j in range(4)]
        assert e==b+delta[0] and f==delta[1]-b+c+d and g==d-delta[3]
        assert h==M-sum(C[:7])
        groups.add((start,end,a,b,c,d))
    print(M,len(groups))
