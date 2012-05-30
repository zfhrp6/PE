# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 303

正の整数 n に対し, f(n) を,
    n の倍数であり 10 進数で表すと 2 以下の数字のみが用いられる最小の数
と定義する.

ゆえに, f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222 である.
また, Σ{f(n)/n}_1~100 = 11363107 である.
Σ{f(n)/n}_1~10000 を求めよ.
"""
import time
import math
import Euler
t0=time.time()
answer=0

def funcc(n):
    i=0
    while True:
        i+=n
        ls=list(str(i))
        if ("3" in ls or "4" in ls or "5" in ls or "6" in ls
            or "7" in ls or "8" in ls or "9" in ls):
                continue
        else:
            break
    return i

for n in range(1,1001):
    print n
    fn=funcc(n)
    print "___",fn/n
    answer+=fn/n


print answer
print time.time()-t0, "seconds"
