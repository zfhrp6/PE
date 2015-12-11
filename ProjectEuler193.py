#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 193

正の整数 n が、任意の素数の2乗によって割り切れないとき、
n を"平方因子を含まない"(squarefree)と呼ぶ。
1, 2, 3, 5, 6, 7, 10, 11 は平方因子を含まないが、 4, 8, 9, 12 は平方因子を含む。

2^50 未満で平方因子を含まない数はいくつあるか?
"""
import time
import Euler
t0 = time.time()
answer = 0
i = 0
while i < 2 ** 50:
    i += 1
    if i % 10000 == 0:
        print(i)
    all_list = Euler.factoring(i)
    set_list = list(set(all_list))
    if all_list == set_list:
        answer += 1
    del(all_list, set_list)

print(answer)
print(time.time() - t0, "seconds")
