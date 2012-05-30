# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 46

Christian Goldbachは全ての奇合成数は平方数の2倍と素数の和で表せると予想した.
    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2
後に, この予想は誤りであることが分かった.
平方数の2倍と素数の和で表せない最小の奇合成数を答えよ.
"""
import time
import math
import Euler
t0=time.time()
primes=tuple(Euler.prime_make(10000))
i=31
#奇合成数と素数の差の半分が平方数になる。という条件に変形している。
while True:
    i+=2
    if i%100==1:
        print i
    if i in primes:
        continue
    flag=True
    for j in [x for x in primes if x<=i][::-1]:
        if math.sqrt((i-j)/2)%1==0.0:
            flag=False
            break
    if flag==True:
        answer=i
        break

print "answer=%d"%(answer)
print time.time()-t0, "seconds"
