# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 171

正の整数nについて、f(n)を各桁の数字(10進数)の平方の和と定義する。例えば、

f(3) = 3^2 = 9,
f(25) = 2^2 + 5^2 = 4 + 25 = 29,
f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36

0 < n < 10^20について、f(n)が平方数となるようなnの和の末尾9桁を求めよ。
"""
import time
import math
import Euler
time1=time.time()
sums=0
i=0
while i<10**20:
    i+=1
    if math.sqrt(Euler.sum_numbers_expo(i,2))%1==0:
        sums+=i


print sums%1000000000
print time.time()-time1, "seconds"
