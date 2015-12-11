#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 91

素数の2乗と素数の3乗と素数の4乗の和で表される最小の数は28である. 50未満のこのような数は丁度4つある.
    28 = 2^2 + 2^3 + 2^4
    33 = 3^2 + 2^3 + 2^4
    49 = 5^2 + 2^3 + 2^4
    47 = 2^2 + 3^3 + 2^4
では, 50,000,000未満の数で, 素数の2乗と素数の3乗と素数の4乗の和で表される数は何個あるか?
"""
import time
import Euler
t0 = time.time()
primes = Euler.prime_make(7080)
answerlist = []
for x in primes:    # 7079**2>50000000
    for y in [i for i in primes if i < 374]:  # 374**3>50000000
        for z in [k for k in primes if k < 90]:   # 89**4>50000000
            num = x ** 2 + y ** 3 + z ** 4
            if num < 50000000:
                answerlist.append(num)
answerlist = list(set(answerlist))
answerlist.sort()
print(len(answerlist))
print(time.time() - t0, "seconds")
