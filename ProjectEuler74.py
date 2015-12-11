#!/usr/bin/env python
# coding:utf-8
"""
Project Euler Problem 74

145は各桁の階乗の和が145と自分自身に一致することで有名である.
    1! + 4! + 5! = 1 + 24 + 120 = 145.
169の性質はあまり知られていない. これは169に戻る数の中で最長の列を成す.
このように他の数を経て自分自身に戻るループは3つしか存在しない.
    169 -> 363601 -> 1454 -> 169
    871 -> 45361 -> 871
    872 -> 45362 -> 872
どのような数からスタートしてもループに入ることが示せる.
例を見てみよう.
    69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
    78 -> 45360 -> 871 -> 45361 (-> 871)
    540 -> 145 (-> 145)
69から始めた場合, 列は5つの循環しない項を持つ.
また100万未満の数から始めた場合最長の循環しない項は60個であることが知られている.
100万未満の数から開始する列の中で, 60個の循環しない項を持つものはいくつあるか?
"""
import time
import math
t1 = time.time()

answer = 0


def fac(n):
    re = 0
    n = list(str(n))
    for i in n:
        re += math.factorial(int(i))
    return re

lengths = [2, 1, 1]

for i in range(3, 1000001):
    if fac(i) == i:
        continue
    moto = i * 1
    thisloop = []
    thisloop.append(i)
    while fac(i) not in thisloop:
        if fac(i) < moto:
            length = len(thisloop) + lengths[fac(i)]
            lengths.append(length)
            break
        i = fac(i)
        thisloop.append(i)
    lengths.append(len(thisloop))
    if len(thisloop) == 60:
        answer += 1

print(answer)
print(time.time() - t1, "seconds")
