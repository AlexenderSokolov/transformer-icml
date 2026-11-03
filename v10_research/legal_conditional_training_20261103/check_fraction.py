from fractions import Fraction as F
p=F(1,5)
loss=lambda q: (1-p)*q*q+p*(1-q)*(1-q)
q1,q2,q3=F(1,10),F(3,10),F(2,5)
legal=max(loss(q1),loss(q2)); fixed=loss(q3)
label_aware=(1-p)*max(q1*q1,q2*q2)+p*max((1-q1)**2,(1-q2)**2)
assert (legal,fixed,label_aware)==(F(17,100),F(1,5),F(117,500))
assert legal < fixed < label_aware
print('legal varying:',legal,'constant:',fixed,'label aware varying:',label_aware)
print('squared target risk:',(q1-p)**2,(q3-p)**2)
