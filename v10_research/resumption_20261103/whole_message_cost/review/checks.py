#!/usr/bin/env python3
"""Supplemental finite checks only; not a proof of asymptotic theorem."""
import itertools, math, json
from fractions import Fraction

def run():
    result={}
    words=0
    for M in range(1,11):
        for z in itertools.product((0,1), repeat=M+2):
            # Single streaming scan: ignore initial edge, retain both rows until terminal selection.
            J=[0,0]; C=[0,0]; H=[0,0]
            for i in range(1,M+1):
                u=z[i]; J[u]+=1; C[u]+=z[i]!=z[i+1]
                if i<=M//2: H[u]+=1
            u=z[-1]; payload=(u,J[u],C[u],int(512*H[u]>=J[u]))
            assert J[u]==sum(z[i]==u for i in range(1,M+1))
            assert C[u]==sum(z[i]==u and z[i+1]!=u for i in range(1,M+1))
            b=math.ceil(math.log2(M+1)); bits=f'{J[u]:0{b}b}'+f'{C[u]:0{b}b}'+f'{u:b}'+str(payload[-1])
            assert len(bits)==2*b+2
            jj=int(bits[:b],2); cc=int(bits[b:2*b],2); uu=int(bits[2*b]); gg=int(bits[-1])
            assert (uu,jj,cc,gg)==payload
            flip=Fraction(cc,jj) if jj and gg else Fraction(0)
            predicted_one=flip if uu==0 else 1-flip
            assert 0<=predicted_one<=1
            words+=1
    result['exhaustive_payload_words_M1_to10']=words
    entropy=-.25*math.log2(.25)-.75*math.log2(.75)
    for R in range(1,513):
        d=(R+3)//4
        v=sum(math.comb(R,j) for j in range(d))
        assert math.log2(v)<=R*entropy+1e-12
    result['GV_ball_volume_R1_to512']=True
    greedy=[]
    for R in range(1,13):
        d=(R+3)//4; code=[]
        for x in range(1<<R):
            if all((x^y).bit_count()>=d for y in code): code.append(x)
        v=sum(math.comb(R,j) for j in range(d))
        assert len(code)*v>=1<<R
        greedy.append([R,d,len(code)])
    result['greedy_code_sizes']=greedy
    tests=0
    for M in [64,65,100,1024,10**6,10**12]:
        B=2*math.ceil(math.log2(M+1))+2
        for h in [.01,.5,math.sqrt(.75),.999,.999999]:
            R=math.ceil(max(B/(1-entropy),4*(B*math.log(2)+.5*math.log(M))/(-math.log(h))))
            assert R*(1-entropy)>=B-1e-9
            assert B*math.log(2)+R/4*math.log(h)<=-.5*math.log(M)+1e-8
            tests+=1
    result['length_and_error_log_checks']=tests
    # ML for equally likely BSC codewords: pairwise likelihood-error includes ties.
    paircases=0
    for R in range(1,9):
        q=Fraction(1,4); h=2*math.sqrt(float(q*(1-q)))
        x=0
        for xp in range(1,1<<R):
            err=Fraction(0)
            for y in range(1<<R):
                dx=(x^y).bit_count(); dp=(xp^y).bit_count()
                px=q**dx*(1-q)**(R-dx); pp=q**dp*(1-q)**(R-dp)
                if pp>=px: err+=px
            assert float(err)<=h**((x^xp).bit_count())+1e-12
            paircases+=1
    result['exact_BSC_pairwise_ML_cases_R1_to8']=paircases
    for D in range(1,101):
        ell=Fraction(1,2); width=ell/D
        integral=D*width*width/4/ell
        assert integral==Fraction(1,8*D)
    result['optimal_uniform_quantizer_bayes_integrals_D1_to100']=True
    result['status']='PASS; finite diagnostics, not formal proof'
    return result

if __name__=='__main__': print(json.dumps(run(),indent=2))
