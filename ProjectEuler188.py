#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 188

数aの正整数bによるhyperexponentiationまたはtetrationを a↑↑b と書き, 以下のように再帰的に定義する.
a　↑↑　1 = a,
a　↑↑　(k+1) = a^(a　↑↑　k).
定義によれば 3↑↑2 = 3^3 = 27であり, 3↑↑3 = 3^27 = 7625597484987となる.
また, 3↑↑4は大体10^(3.6383346400240996*10^12)となる.

1777↑↑1855の最後の8桁を求めよ.
"""
import time
t0 = time.time()
answer = 1777
for i in range(1854):
    answer = (answer % 100000000) ** 1777

print(answer % 100000000)
print(time.time() - t0, "seconds")
