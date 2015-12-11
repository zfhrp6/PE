#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 138

底の長さbが16, 脚の長さLが17の二等辺三角形を考える.

ピタゴラスの定理より, 三角形の高さh = √(172 − 82) = 15となる.
高さは底の長さより1だけ短い.

b = 272, L = 305とすると, h = 273となり, これは底の長さより1だけ長い.
この三角形はh = b ± 1という性質を持つ二等辺三角形の中で二番目に小さい.

h = b ± 1, b, Lが全て正の整数であるとし,
そのような二等辺三角形の中で小さい順に12個取ったときの∑Lを求めよ.
"""
import time
import math
t0 = time.time()
answer = 0
b = 0
count = 0
while True:
    b += 2
    if b % 100000 == 0:
        print(b)
    h = b - 1
    l = math.sqrt((1.0 * b / 2) ** 2 + h ** 2)
    if l % 1 == 0.0 and 2 * l > b:
        count += 1
        answer += l
    if count >= 12:
        break
    h = b + 1
    l = math.sqrt((1.0 * b / 2) ** 2 + h ** 2)
    if l % 1 == 0.0 and 2 * l > b:
        count += 1
        answer += l
    if count >= 12:
        break

print(answer)
print(time.time() - t0, 'seconds')
