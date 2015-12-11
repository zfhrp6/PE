#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 27

オイラーは以下の二次式を考案している:
    n^2 + n + 41.

この式は, nを0から39までの連続する整数としたときに40個の素数を生成する.
しかし, n = 40のとき40^2 + 40 + 41 = 40(40 + 1) + 41となり41で割り切れる.
また, n = 41のときは41^2 + 41 + 41であり明らかに41で割り切れる.
計算機を用いて, 二次式 n^2 - 79n + 1601という式が発見できた.
これはn = 0 から 79 の連続する整数で素数を生成する.
係数の積は, -79 × 1601 で -126479である.

さて, |a| < 1000, |b| < 1000 として以下の二次式を考える (ここで|a|は絶対値):
    n^2 + an + b
n=0から始めて連続する整数で素数を生成したときに最長の長さとなる上の二次式の, 係数a, bの積を答えよ.
"""
import time
import math
time1 = time.time()

sosu = [2]  # make_primes start
for i in range(3, 3000, 2):
    if i > 3000:
        break
    if len(sosu) >= 10001:
        break
    for j in sosu:
        if i % j == 0:
            break
        else:
            if j > math.sqrt(i):
                sosu.append(i)
                break  # make_primes end
sosu = tuple(sosu)

answer_n = 0
for a in range(-999, 1000, 2):
    for b in sosu[:9000]:
        if b >= 1000:
            break
        n = -1
        while True:
            n += 1
            if n ** 2 + a * n + b not in sosu:
                break
        if answer_n < n - 1:
            answer_n = n - 1
            answer = a * b
            print(a, b)
print(answer)
print(time.time() - time1, "seconds")
