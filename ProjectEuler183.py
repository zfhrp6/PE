#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 183

Nを正整数とし, Nをk個に等分する. 即ち, r=N/kとし, N = r + r + ... + rである.
Pをその分割数の積とする. 即ち, P = r × r × ... × r = r^k.
例えば, 11を5つに分割すると, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2となる.
このとき, P = 2.2^5 = 51.53632である.
M(N)=P_maxとする.
N=11の場合には4つに分けた場合がP_max=(11/4)^4で最大となる.
M(11) = 14641/256 = 57.19140625であり, 有限小数である.
しかし, N=8の場合には最大値は3に分けられたときに得られ, M(8)=512/27となる.
これは無限小数 (循環小数) である.
さて, M(N)が無限小数のときD(N)=Nに, M(N)が有限小数のときにD(N)=-Nとする.
5 ≦ N ≦ 100のとき, ΣD(N) = 2438となる.
5 ≦ N ≦ 10000のとき, ΣD(N) を求めよ.
"""
import time
import Euler
t0 = time.time()
answer = 0


def M(n):
    maax = 0
    for k in range(1, n + 5):
        if (1.0 * n / k) ** k > maax:
            maax = (1.0 * n / k) ** k
            maax_k = k
    return (maax, maax_k)


def det_M(seq):
    div1 = set(Euler.factoring(seq[0]))
    div2 = set(Euler.factoring(seq[1]))
    check = div2.difference(div1)
    if 3 in check or 7 in check:
        return 1
    else:
        return -1

for N in range(5, 101):
    print(N)
    answer += N * det_M(M(N))

print(answer)
print(time.time() - t0, "seconds")
