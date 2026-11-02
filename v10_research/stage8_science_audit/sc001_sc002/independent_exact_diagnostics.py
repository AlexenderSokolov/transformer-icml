#!/usr/bin/env python3
"""Fresh, exact-rational finite checks; none are proof substitutes."""
from fractions import Fraction as Q
from itertools import product, combinations
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'v10_research/stage8_science_audit/sc001_sc002'
counts=Counter()
def hist(x): return Counter(zip(x,x[1:],x[2:]))
def distance(a,b): return sum(x!=y for x,y in zip(a,b))
# Multi-edit exhaustive test, including endpoint row changes in interior memberships.
for K,Nmax in [(2,8),(3,6)]:
  for N in range(3,Nmax+1):
    for end in product(range(K),repeat=2):
      words=[w+end for w in product(range(K),repeat=N-2)]
      hs=[hist(w) for w in words]
      for i,x in enumerate(words):
        h=hs[i]; u=[h[end+(c,)]+1 for c in range(K)]; A=sum(u)
        for j,y in enumerate(words):
          g=hs[j]; k=distance(x,y)
          delta=sum(abs(h[t]-g[t]) for t in h.keys()|g.keys())
          assert delta<=6*k
          v=[g[end+(c,)]+1 for c in range(K)]; B=sum(v)
          tv=sum(abs(Q(a,A)-Q(b,B)) for a,b in zip(u,v))/2
          assert tv<=min(Q(1),Q(6*k,A))
          counts['multi_edit_histogram_and_clean_mass_normalization']+=1
# Entire-word output factorization, including terminal labels, across distinct p.
for ell in range(9):
  for b in range(1,11):
    transition=defaultdict(lambda:Q(0))
    for word in product((0,1),repeat=ell):
      ones=[i for i,x in enumerate(word) if x]; n=len(ones); r=b*(n//b)
      for kept in combinations(ones,r):
        z=tuple(int(i in kept) for i in range(ell))
        assert distance(word,z)==n-r<=b-1
        transition[n,z]+=Q(1,comb(ell,n)*comb(n,r))
    for (n,z),v in transition.items():
      r=sum(z); assert v==Q(1,comb(ell,r))
      counts['erasure_conditional_arrangement_entries']+=1
    for p in [Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4)]:
      full=defaultdict(lambda:Q(0)); rounded=defaultdict(lambda:Q(0))
      for (n,z),v in transition.items():
        prob=comb(ell,n)*p**n*(1-p)**(ell-n)*v
        full[z]+=prob
      for z,v in full.items(): rounded[sum(z)]+=v
      assert sum(full.values())==1
      for z,v in full.items():
        assert v==rounded[sum(z)]/comb(ell,sum(z))
        for U in product((0,1),repeat=2):
          mass=p**sum(U)*(1-p)**(2-sum(U))
          assert v*mass==rounded[sum(z)]*mass/comb(ell,sum(z))
          counts['full_word_rounded_count_terminal_factorization']+=1

def mm(A,B):
  return [[sum((a*b for a,b in zip(row,col)),Q(0)) for col in zip(*B)] for row in A]
def power(A,n):
  d=len(A); R=[[Q(i==j) for j in range(d)] for i in range(d)]
  while n:
    if n&1:R=mm(R,A)
    A=mm(A,A);n//=2
  return R

def witness(M,beta0,p):
  a=Q(1,2*M); e=beta0-a; pi=[e/beta0,a*(1-p)/beta0,a*p/beta0,Q(0)]
  T=[[1-a,a*(1-p),a*p,Q(0)], [e,(1-e)*(1-p),(1-e)*p,Q(0)], [e,(1-e)*(1-p),(1-e)*p,Q(0)],pi]
  states=list(product(range(4),repeat=2))
  Pi=[pi[u]*T[u][v] for u,v in states]
  P=[[T[y][v] if y==u else Q(0) for u,v in states] for x,y in states]
  return a,e,pi,T,Pi,P
for M in [64,65,66,67,96,127,128,129,256]:
  for beta0 in sorted(set([Q(1,M),Q(1,32),Q(1,16)])):
    for p in [Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4)]:
      a,e,pi,T,Pi,P=witness(M,beta0,p)
      assert all(sum(row)==1 for row in P)
      assert mm([Pi],P)[0]==Pi
      P2=mm(P,P)
      for row in P2:
        for value,target in zip(row,Pi):
          assert value>=beta0*target
          counts['all_state_pair_minorization_entries']+=1
      L=int(1/(4*beta0))
      assert 4<=L<=Q(M,4)
      assert L-1>=1/(8*beta0)
      for j in range(2,L+1):
        event=Pi[0]*(1-a)**(M-j)*a*(1-e)**(j-1)
        assert event>=Q(3,64*M)>=Q(1,32*M)
        counts['stationary_rare_suffix_event_bounds']+=1
        # Sum all active words, independently from direct event formula.
        if j<=6:
          total=Q(0)
          for bits in product((0,1),repeat=j):
            active=[1+x for x in bits]
            prob=Pi[0]*(1-a)**(M-j)*T[0][active[0]]
            for x,y in zip(active,active[1:]):prob*=T[x][y]
            assert prob/event==p**sum(bits)*(1-p)**(j-sum(bits))
            total+=prob
            counts['direct_path_conditional_iid_entries']+=1
          assert total==event
# Exact all-state suffix mixture with unsupported initial symbols and every M mod 4.
for M in [64,65,66,67]:
  beta=Q(1,32); _,_,_,_,Pi,P=witness(M,beta,Q(1,3))
  J=[Pi[:] for _ in P]; P2=mm(P,P)
  R=[[(x-beta*y)/(1-beta) for x,y in zip(a,b)] for a,b in zip(P2,J)]
  assert all(all(x>=0 for x in row) and sum(row)==1 for row in R)
  assert mm([Pi],R)[0]==Pi
  u=M//2;r=M//4;eta=(1-beta)**r
  direct=power(P,u); residual=mm(power(R,r),power(P,u-2*r))
  for row,target,stat in zip(direct,residual,J):
    for lhs,v,w in zip(row,target,stat):
      assert lhs==(1-eta)*w+eta*v
      counts['exact_all_state_suffix_mixture_entries']+=1
# Original SC001 stationary equal-a/e event identity at minimum and later horizons.
for M in range(2,65):
  a=e=Q(1,M)
  for j in range(2,M+1):
    event=(1-a)/2*(1-a)**(M-j)*a*(1-e)**(j-1)
    assert event==(1-a)**M/(2*M) and event>=Q(1,8*M)
    counts['sc001_stationary_event_identity_and_bound']+=1
# Rational IID message floor for every budget, including maximum legal budget.
for M in range(2,513):
  for k in range(1,M+1):
    b=k+1
    assert Q(1,32*(M//b+1))>=Q(b,32*(M+b))>=Q(k,96*M)
    counts['iid_message_floor_integer_cases']+=1
result={'status':'PASS','arithmetic':'exact integers and fractions.Fraction only; no floating tolerances','checks':dict(counts),'total_asserted_cases':sum(counts.values()),'scope':'Finite corroboration of algebra, full-word factorization and selected finite cases, not proof or statistical simulation.'}
(OUT/'independent_exact_diagnostics.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
