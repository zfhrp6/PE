# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 32

7254は面白い性質を持っている.
39 × 186 = 7254と書け, 掛けられる数/掛ける数/積に1から9の数が1回ずつ出現する.
掛けられる数/掛ける数/積に1から9の数が1回ずつ出現するような積の総和を求めよ.

HINT: いくつかの積は, 1通り以上の掛けられる数/掛ける数/積の組み合わせを持つが1回だけ数え上げよ.
"""
import time
import math
time1=time.time()
sum=0
ijlist=[]
for i in range(1,100):
    for j in range(100,10000):
        if i*j>=10000 or i*j<1000:
            continue
        if "0" in str(i)+str(j)+str(i*j):
            continue
        if len(list(set(list(str(i)+str(j)+str(i*j)))))==9 and i*j not in ijlist:
            sum+=i*j
            ijlist.append(i*j)
print sum
print time.time()-time1, "seconds"