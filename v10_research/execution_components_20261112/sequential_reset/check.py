import math,random,json
if not __debug__: raise RuntimeError('Do not use -O')
rng=random.Random(7241); checks=0; worst=0
for m in [7,12,20]:
 for k in [1,2,3]:
  for trial in range(20):
   pairs=[rng.uniform(-1,1) for _ in range(m)]
   h=[v for x in pairs for v in (x,-x)]
   held=h[2*k:]; H=math.sqrt(sum(x*x for x in h)); D=math.sqrt(1+H*H/(2*m));q=1-D**-3
   initial=math.sqrt(sum(x*x for x in h[:2*k])); prior=initial
   for step in range(80):
    mu=sum(h)/(2*m); d=math.sqrt(1+sum((x-mu)**2 for x in h)/(2*m))
    for r in range(2*k):h[r]-=(h[r]-mu)/d
    now=math.sqrt(sum(x*x for x in h[:2*k]))
    assert now<=q*prior+1e-13
    assert h[2*k:]==held
    assert abs(sum(h))<1e-12
    assert now<=q**(step+1)*initial+1e-12
    checks+=4;prior=now
   worst=max(worst,prior)
# Full-coordinate subtraction of LN preserves the common-mode exactly.
h=[2.,0.,1.,1.];mu=sum(h)/4;d=math.sqrt(1+sum((x-mu)**2 for x in h)/4)
y=[x-(x-mu)/d for x in h]
assert abs(sum(y)/4-1)<1e-15;checks+=1
print(json.dumps({'seed':7241,'cases':180,'reset_steps_per_case':80,'assertions':checks,'max_final_scratch_norm':worst,'scope':'reset component only; no sequential predictor or risk test'},indent=2))
