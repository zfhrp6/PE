# -*- coding: utf-8 -*-
#project euler Problem 45
"""
三角数, 五角数, 六角数は以下のように生成される.
三角数	Tn=n(n+1)/2	1, 3, 6, 10, 15, ...
五角数	Pn=n(3n-1)/2	1, 5, 12, 22, 35, ...
六角数	Hn=n(2n-1)	1, 6, 15, 28, 45, ...

T285 = P165 = H143 = 40755であることが分かる.

次の三角数かつ五角数かつ六角数な数を求めよ."""
import time
time1=time.time()

tn=[]
pn=[]
hn=[]
for i in range(140,500000):
    tn.append(i*(i+1)/2)
    pn.append(i*(3*i-1)/2)
    hn.append(i*(2*i-1))
s_t=set(tn)
s_p=set(pn)
s_h=set(hn)
print s_t&s_p&s_h
print time.time()-time1, "seconds"