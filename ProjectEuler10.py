# -*- coding: utf-8 -*-
#project euler problem 10
#200万以下の全ての素数の和を計算しなさい.
import time
import math
x=2000000
time1=time.time()

if x==0:
    x=100000
s=[2]
for i in range(3,x+1):
    if i>x:
        break
    #if len(s)>=1000000:
    #    break
    for j in s:
        if i%j==0:
            break
        else:
            if j>math.sqrt(i):
                s.append(i)
                break
print sum(s)
print time.time()-time1, "seconds"
del(s,time1,x,i,j)