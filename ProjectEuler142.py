# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 142

x + y, x - y, x + z, x - z, y + z, y - zが全て平方数となる整数の組 x > y > z > 0で,
最小の x + y + z を求めよ.
"""
import time
import math
import Euler
t1=time.time()
a=2
answer=99999999999999
def issq(n):
    if int(math.sqrt(n))**2==n:
        return 1
    else:
        return 0

while answer==99999999999999:
    a+=1
    if math.sqrt(a)%1!=0:
        continue
    print a
    for c in [h**2 for h in range(1,int(math.sqrt(a)))]:
        for d in [k**2 for k in range(1,int(math.sqrt(c)))]:
            f=(a-c)
            e=(a-d)
            b=(c-e)
            if f<1 or e<1 or b<1 or issq(f)*issq(e)*issq(b)==0:
                if ((a+b)/2.0%1==0):
                    if ((e+f)/2.0%1==0):
                        if ((c-d)/2.0%1==0):
                            answer=(a+b+e+f+c-d)/2.0

print answer,(a+b)/2.0,(e+f)/2.0,(c-d)/2.0
print time.time()-t1, "seconds"