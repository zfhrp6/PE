#!/usr/bin/env python
# coding:utf-8
"""
Project Euler Problem 123

p_n を n 番目の素数とする. (p_1 = 2, p2 = 3, ...)
r を (p_n - 1)^n + (p_n + 1)^n を p_n^2 で割った余りとする.

例えば, n = 3 のとき, p_3 = 5 であり, 4^3 + 6^3 = 280 ≡ 5 mod 25.

余り r が 10^9 より大きくなる n の最小値は 7037 である.

余り r が 10^10 より大きくなる最初の n を求めよ.
"""
import time
import Euler
t1 = time.time()
primes = Euler.prime_make(1000000)
primes.insert(0, 0)
primes = tuple(primes)
for i in range(7038, len(primes)):
    if i % 2 == 0:
        continue
    m = ((primes[i] - 1) ** i + (primes[i] + 1) ** i) % (primes[i] ** 2)
    if i % 100 < 3:
        print(i, m)
    if m > 10 ** 10:
        break

print(i)
print(time.time() - t1, "seconds")
