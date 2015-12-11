#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 41

n桁の数がPandigitalであるとは, 1からnまでの数を各桁に1つずつもつことである.
例えば2143は4桁のPandigital数であり, かつ素数である.

n桁のPandigitalな素数の中で最大の数を答えよ.
"""
import Euler
import time
time1 = time.time()
answer = 0
for i in range(9999999, 1000000, -1):
    if Euler.pandigital_check(i) * Euler.primecheck(i):
        answer = i
        break

if answer == 0:
    for i in range(9999, 1000, -1):
        if Euler.pandigital_check(i) * Euler.primecheck(i):
            answer = i
            break

print(answer)
print(time.time() - time1, "seconds")
