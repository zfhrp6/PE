#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 37

3797は面白い性質を持っている.
まずそれ自身が素数であり, 左から右に桁を除いたときに全て素数になっている (3797, 797, 97, 7).
同様に右から左に桁を除いたときも全て素数である (3797, 379, 37, 3).
右から切り詰めても左から切り詰めても素数になるような素数は11個しかない. 総和を求めよ.

注: 2, 3, 5, 7を切り詰め可能な素数とは考えない.
"""
import time
import Euler
time1 = time.time()
anslist = []
i = 9
while len(anslist) < 11:
    i += 2
    if Euler.primecheck(i) == 0:
        continue
    checkn = 1
    for j in range(1, len(str(i))):
        if Euler.primecheck(int(str(i)[j:])) * Euler.primecheck(int(str(i)[:j])) != 1:
            checkn = 0
            break
    if checkn == 0:
        continue
    if j == len(str(i)) - 1:
        anslist.append(i)


print(sum(anslist))
print(time.time() - time1, "seconds")
