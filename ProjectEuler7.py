# -*- coding: utf-8 -*-
#project euler problem 7
#10001 番目の素数を求めよ。
#coding:utf-8
#!/usr/bin/env python
import time
import math
time1=time.time()

s=[2]
for i in range(3,5000000):
    if i>5000000:
        break
    if len(s)>=10001:
        break5
    for j in s:
        if i%j==0:
            break
        else:
            if j>math.sqrt(i):
                s.append(i)
                break
print s[-1]
print time.time()-time1, "seconds"
del(s,time1,i,j)