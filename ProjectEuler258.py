#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 258

数列を以下のように定義する。

    * 0 ≤ k ≤ 1999 に対して g_k = 1
    * k ≥ 2000 に対して g_k = g_(k-2000) + g_(k-1999)

k = 10^18 に対して g_k mod 20092010 を求めよ。
"""
import time
import math
time1 = time.time()

anslist = []
for i in range(2001):
    anslist.append(1)

j = 1999
while math.log10(j) <= 18:
    j += 1
    if j % 2001 == 0:
        anslist[j % 2001] = anslist[j % 2001] + anslist[2000]
    else:
        anslist[j % 2001] = anslist[j % 2001] + anslist[j % 2001 - 1]


print(anslist[j % 2001] % 20092010)
print(time.time() - time1, "seconds")
