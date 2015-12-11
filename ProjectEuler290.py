#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 290

0 ≤ n < 10^18 であり n の桁の合計が 137n の桁の合計と等しいような整数 n はいくつあるか。
"""
import time
time1 = time.time()
sums = 0
i = 0
while i < 7490000:
    i += 1


print(sums % 1000000000)
print(time.time() - time1, "seconds")
