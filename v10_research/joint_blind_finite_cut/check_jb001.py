from fractions import Fraction as F
from pathlib import Path
import hashlib, json, math, random

rng = random.Random(711026)
root = Path(__file__).resolve().parent
def counts(word):
    c = [0] * 8
    for a,b,d in zip(word, word[1:], word[2:]):
        c[4*a+2*b+d] += 1
    return c
def floor_grid(x, q):
    return F((x.numerator*q)//x.denominator, q)

total = active = inactive = zero_rows = 0
for M in [64,65,127,256,1024,4096]:
    rt = math.isqrt(M)
    ceiling = rt + (rt*rt < M)
    Q = 1
    while Q < 16*ceiling: Q *= 2
    D = 4*Q
    for trial in range(100):
        if trial % 3 == 0: word = [int('0011'[i%4]) for i in range(M+2)]
        elif trial % 3 == 1: word = [rng.randrange(2) for _ in range(M+2)]
        else: word = [0] * (M+2)
        k = rng.randrange(rt//3+1)
        delta = F(1,4*Q)
        tau = F(k,M)+delta+F(1,Q)
        assert M*tau*tau <= 1
        changed = word.copy()
        for i in rng.sample(range(M),k): changed[i] ^= 1
        c, cp = counts(word), counts(changed)
        assert sum(abs(a-b) for a,b in zip(c,cp)) <= 6*k
        bank=[]
        for v in cp:
            a=floor_grid(F(v,M),D)
            eta=delta*rng.choice([-1,0,1])
            z=floor_grid(min(F(1),max(F(0),a+eta)),Q)
            assert abs(z-F(v,M)) <= delta+F(2,Q)
            bank.append(z)
        u=2*word[-2]+word[-1]
        exit_bit=1-word[-2]
        C=c[2*u+exit_bit]; J=c[2*u]+c[2*u+1]
        Ct=M*bank[2*u+exit_bit]; Jt=M*(bank[2*u]+bank[2*u+1])
        d=6*k+2*M*(delta+F(2,Q)); B=12*ceiling
        assert d<=F(B,2)
        assert abs(Ct-C)+abs((Jt-Ct)-(J-C))<=d
        pred=Ct/Jt if Ct>B else F(0)
        active += Ct>B; inactive += Ct<=B; zero_rows += J==0
        for q in [F(0),F(1,17),F(1,4),F(1,2),F(3,4),F(1)]:
            E=abs(F(C,J)-q) if J else F(0)
            bias=q if q>0 and J*q<=3*B else F(0)
            rhs=5*E+4*min(q,6*d/F(J+2))+bias
            assert abs(pred-q)<=rhs, (M,k,J,C,Ct,Jt,q)
            total += 1

constant_rhs=2**20-2600-16-32*16672
assert constant_rhs>0 and (5*8193)**2*32<constant_rhs**2
assert 144*16672==2400768<2**22
proof=root/'JB001_theorem.md'
result={'status':'PASS','exact_pathwise_checks':total,'actual_finite_bank_histories':active+inactive,
        'active_histories':active,'inactive_histories':inactive,'empty_clean_rows':zero_rows,
        'theorem_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'scope':'Exact rational finite-bank/edit/real-pseudocount algebra and squared constants only; deterministic samples, not universal proof, statistical experiment or formal verification.'}
(root/'JB001_author_diagnostics.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
