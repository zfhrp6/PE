# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 119

512 という数は興味深い数である. というのも, 各桁の和を何乗かしたものに等しくなっているからである:
    5 + 1 + 2 = 8, 8^3 = 512 である. この特性を持つ他の数は例えば 614656 = 28^4 である.
この数列の第 n 項を a_n と定義し, また 2 桁以上であるとしよう.
a_2 = 512, a_10 = 614656 となる.
a_30 を求めよ.
"""
import time
import math
import Euler
time1=time.time()
lis=[]
i=9
while len(lis)<31:
    i+=1
    if Euler.primecheck(i):
        continue
    j=1
    while True:
        j+=1
        if (Euler.sum_numbers_expo(i,1))**j==i:
            lis.append(i)
            print i
            break
        if (Euler.sum_numbers_expo(i,1))**j>i:
            break

print lst[-1]
print time.time()-time1, "seconds"
