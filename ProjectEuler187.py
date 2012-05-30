# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 187

合成数とは2つ以上の素因数を含む整数のことである.
例えば15 = 3 × 5, 9 = 3 × 3, 12 = 2 × 2 × 3が合成数である.
30以下には丁度2つの素因数を含む合成数 (異なる素因数でなくてもよい) が,
10個存在する. 4, 6, 9, 10, 14, 15, 21, 22, 25, 26がそうである.
合成数n < 10^8について, 丁度2つの素因数を含む合成数 (異なる素因数でなくてもよい) の数を答えよ.
"""
import time
import Euler
t0=time.time()

primes=tuple(Euler.prime_make(50000000))

answer_count=0
for i in primes:
    if int(i)>10000:
        break
    print i
    for j in primes:
        if j<i:
            continue
        if int(i)*int(j)>=10**8:
            break
        answer_count+=1

print answer_count
print time.time()-t0, "seconds"
