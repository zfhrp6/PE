# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 145

ある正の整数nについて、[n + reverse(n)]が奇数のみで表されるようなnが存在する。
えば、36 + 63 = 99, 409 + 904 = 1313 のように。この性質を持つ数を、reversibleと呼ぶことにする。
つまり、36, 63, 409, 904はrevesibleである。
先頭の0はnでもreverse(n)でも許されない。
1000未満には120個のreversibleな数が存在する。
10億(10^9)未満では、いくつのreversibleな数が存在するか。
"""
import time
import math
import Euler
t0=time.time()
answer=0
i=0
while i<10**9:
    i+=1
    if i%10==0:
        continue
    if i%1000000==1:
        print i
    num=i+int(str(i)[::-1])
    if "0" in str(num) or "2" in str(num) or "4" in str(num) or "6" in str(num) or "8" in str(num):
        continue
    else:
        answer+=1
print answer
print time.time()-t0, "seconds"
