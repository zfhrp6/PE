# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 135

正の整数x, y, z が等差数列として与えられたとき、
x2 - y2 - z2 = n がちょうど2個の解を持つような最小の正の整数 n は、n = 27である。
34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27
n = 1155 は、方程式がちょうど10個の解を持つ最小の値である。
ちょうど10個の解を持つような n は、100万までにいくつ存在するか?
"""
import time
import math
import Euler
time1=time.time()
n=0
check=0
count=0
primelist=Euler.prime_make(1000000)
print time.time()-time1
while n<1000000:
    n+=1
    if n in primelist:
        continue
    x=0
    while x<=n/2:
        x+=1
        if n%x==0 and n/x>x and (n/x -x)%2==0:
            check+=1
    if check==10:
        count+=1
        check=0
    if time.time()-time1>60:
        break

print count
print time.time()-time1, "seconds"
