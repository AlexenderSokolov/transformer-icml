from itertools import product,combinations

def reconstruct(first,last,number,free):
 a,b,c,d=free;delta=lambda s:int(last==s)-int(first==s);e=b+delta(0);f=delta(1)-b+c+d;g=d-delta(3);return (a,b,c,d,e,f,g,number-a-b-c-d-e-f-g)

def full_features(z,m):
 counts=[[0]*8,[0]*8];L=m//2
 for i in range(m):counts[int(i>=L)][4*z[i]+2*z[i+1]+z[i+2]]+=1
 return (2*z[0]+z[1],tuple(counts[0]),tuple(counts[1]))

def dp(h,k):
 m=len(h)-2;L=m//2;st={}
 for a,b in product(range(2),repeat=2):
  if m==1 and b!=h[1]:continue
  cost=(a!=h[0])+int(m>1 and b!=h[1]); ini=2*a+b;state=(ini,ini,ini if L==0 else -1,(0,)*4,(0,)*4)
  if cost<=k:st[state]=(cost,(a,b))
 for t in range(2,m+2):
  i=t-2;nxt={}
  for (ini,last,mid,left,right),(cost,word) in st.items():
   for c in ([h[t]] if t>=m else [0,1]):
    nc=cost+int(t<m and c!=h[t]);
    if nc>k:continue
    triple=2*last+c;la=list(left);rb=list(right)
    if triple<4:(la if i<L else rb)[triple]+=1
    newpair=2*(last%2)+c;middle=newpair if i+1==L else mid; key=(ini,newpair,middle,tuple(la),tuple(rb))
    if key not in nxt or nc<nxt[key][0]:nxt[key]=(nc,word+(c,))
  st=nxt
 result={}
 for (ini,last,mid,left,right),(cost,word) in st.items():
  key=(ini,reconstruct(ini,mid,L,left),reconstruct(mid,last,m-L,right));
  if key not in result or cost<result[key][0]:result[key]=(cost,word)
 return result

def brute(h,k):
 m=len(h)-2;out={}
 for n in range(k+1):
  for ix in combinations(range(m),n):
   z=list(h)
   for i in ix:z[i]^=1
   key=full_features(z,m)
   if key not in out or n<out[key][0]:out[key]=(n,tuple(z))
 return out

def U(key,h):
 ini,L,R=key;return (ini*11+7*h[-1]+sum((i+1)*(v*v+3*v) for i,v in enumerate(L+R)))%101

checks=0; winners=0
for m in range(1,7):
 for h in product(range(2),repeat=m+2):
  for k in range(m+1):
   a=dp(h,k);b=brute(h,k);assert {q:v[0] for q,v in a.items()}=={q:v[0] for q,v in b.items()},(m,h,k)
   if a:
    key=max(a,key=lambda q:U(q,h));cost,z=a[key];assert z[-2:]==h[-2:] and sum(z[i]!=h[i] for i in range(m))==cost<=k and full_features(z,m)==key and U(key,h)==max(U(x,h) for x in b);winners+=1
   checks+=1
 print('m',m,'cumulative full histogram compact DP/maps/witnesses',checks,flush=True)
print('PASS comparisons',checks,'maximizing witnesses validated',winners)
