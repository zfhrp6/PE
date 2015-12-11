#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 179

nとn + 1 の正の約数の数が同じになる 1 < n < 10^7 の整数は幾つあるか。
例として, 14 の正の約数は 1, 2, 7, 14 であり, 15 の正の約数は 1, 3, 5, 15 である.
"""
import time
import Euler
from functools import reduce
t0 = time.time()
answer = 0
n = 1
lst = [0, 1]
primes = Euler.prime_make(10 ** 5)


def factors(n, lists):
    lists
    if n == 1:
        return {1: 1}
    elif n == 2:
        return {2: 1}
    elif n == 3:
        return {3: 1}
    xd = {}
    for i in lists:
        moto = n
        while n % i == 0:
            if i in xd:
                xd[i] += 1
            else:
                xd[i] = 1
            n = n / i
        if i > moto / 2 + 8:
            break
    if xd == {}:
        xd[n] = 1
    return xd


def how_divs(n):
    return reduce(lambda x, y: (x + 1) * (y + 1), factors(n, primes).values())

lastdivs = 1

while n < 10 ** 7:
    n += 1
    if n % 10000 == 0:
        print(n, " answer:" + str(answer))
    """
    lst[n%2]=how_divs(n)
    if lst[n%2]==lst[n%2-1]:
        answer+=1
    """
    ndivs = how_divs(n)
    if ndivs == lastdivs:
        answer += 1
    lastdivs = ndivs

print(answer)
print(time.time() - t0, "seconds")
