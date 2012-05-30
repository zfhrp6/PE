# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 204

ハミング数とは, どの素因数も5以下であるような正整数のことである.
最初から順に並べると, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15となる.
10^8以下のハミング数は1105個ある.

素因数がn未満の正整数を, type nの一般化ハミング数と呼ぶことにする.
するとハミング数はtype 5の一般化ハミング数である.

10^9以下のtype 100の一般化ハミング数の個数を答えよ.
"""
import time
import Euler
time1=time.time()
i=0
count=0
while i<=10**9:
    i+=1
    if i%1000==0:
        print i
    if Euler.primecheck(i):
        count+=1
    elif Euler.factoring(i)[-1]<=100:
        count+=1
print count
print time.time()-time1, "seconds"